"""Library helpers for selecting stale review targets from the canonical review DB."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.domain.snapshots import AcceptanceSnapshot, GateSnapshot, NoteSnapshot
from commonplace.review.domain.staleness import classify_staleness
from commonplace.review.freshness import file_content_sha256
from commonplace.review.paths import gate_id_for_path, gate_id_from_stored_path, normalize_gate_path, review_gates_dir
from commonplace.review.resolve_gates import applicable_gate_ids_for_note
from commonplace.review.review_db import (
    AcceptanceState,
    append_acceptance_event,
    connect,
    ensure_db,
    load_current_acceptances,
    resolve_db_path,
    snapshot_file,
)
from commonplace.review.clock import iso_now
from commonplace.review.review_model import normalize_model_partition

NOTES_ROOT = Path("kb/notes")
REFERENCE_ROOT = Path("kb/reference")
REVIEWABLE_ROOTS: tuple[Path, ...] = (NOTES_ROOT, REFERENCE_ROOT)


def _has_frontmatter(path: Path) -> bool:
    try:
        with path.open(encoding="utf-8") as f:
            return f.read(4) == "---\n"
    except (OSError, UnicodeDecodeError):
        return False


def _is_index(path: Path) -> bool:
    return path.name == "index.md" or path.name.endswith("-index.md")


def _is_type_definition_content(path: Path, repo_root: Path) -> bool:
    try:
        rel_path = path.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return False
    return "types" in rel_path.parent.parts


def _expand_note_filter(repo_root: Path, raw: str) -> list[Path]:
    path = Path(raw) if Path(raw).is_absolute() else repo_root / raw
    path = path.resolve()
    if path.is_file():
        return [path]
    if path.is_dir():
        notes: list[Path] = []
        for child in sorted(path.glob("*.md")):
            if _is_index(child) or _is_type_definition_content(child, repo_root):
                continue
            if not _has_frontmatter(child):
                continue
            notes.append(child.resolve())
        if not notes:
            raise ValueError(f"No reviewable notes found in directory: {raw}")
        return notes
    raise ValueError(f"Note not found: {raw}")


def _frontmatter_status(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    result = frontmatter.parse(text)
    return result.data.get("status") if result.ok else None


def list_reviewable_notes(repo_root: Path) -> list[Path]:
    """Top-level `*.md` notes under each reviewable scan root that have YAML frontmatter."""
    found: list[Path] = []
    for rel_root in REVIEWABLE_ROOTS:
        root = repo_root / rel_root
        if not root.is_dir():
            continue
        for path in root.glob("*.md"):
            if _is_index(path) or not _has_frontmatter(path):
                continue
            found.append(path)
    return sorted(found)


def list_current_notes(repo_root: Path) -> list[Path]:
    return [
        path
        for path in list_reviewable_notes(repo_root)
        if _frontmatter_status(path) == "current"
    ]


@dataclass(frozen=True)
class StaleGate:
    note_path: str
    gate_path: str
    reason: str
    diff: str | None = None

    @property
    def gate_id(self) -> str:
        return gate_id_from_stored_path(self.gate_path)


def _acceptance_snapshot(acceptance: AcceptanceState | None) -> AcceptanceSnapshot | None:
    if acceptance is None:
        return None
    if acceptance.accepted_note_hash is not None and acceptance.accepted_gate_hash is not None:
        return AcceptanceSnapshot(
            accepted_note_hash=acceptance.accepted_note_hash,
            accepted_gate_hash=acceptance.accepted_gate_hash,
        )
    return None


def note_diff_from_text(note_path: str, previous_text: str, current_text: str) -> str | None:
    import difflib

    diff = "".join(
        difflib.unified_diff(
            previous_text.splitlines(keepends=True),
            current_text.splitlines(keepends=True),
            fromfile=f"a/{note_path}",
            tofile=f"b/{note_path}",
        )
    ).strip()
    return diff or None


def select_stale_gates(
    repo_root: Path,
    *,
    model: str | None,
    gate_ids: list[str],
    note_filter: list[str] | None = None,
    current_only: bool = False,
    include_diff: bool = False,
    db_path: Path | None = None,
) -> list[StaleGate]:
    gates_dir = review_gates_dir(repo_root)
    gate_path_by_id: dict[str, str] = {}
    requested_gate_ids: list[str] = []
    for raw_gate in gate_ids:
        gate_path = normalize_gate_path(repo_root, raw_gate)
        gate_id = gate_id_for_path(repo_root, gate_path)
        gate_path_by_id[gate_id] = gate_path
        requested_gate_ids.append(gate_id)
    model = model.strip() if model is not None else None
    model = normalize_model_partition(model) if model else None
    if db_path is None:
        db_path = resolve_db_path(repo_root)

    if note_filter and current_only:
        raise ValueError("--note and --current are mutually exclusive")

    if note_filter:
        notes: list[Path] = []
        seen: set[Path] = set()
        for raw in note_filter:
            for path in _expand_note_filter(repo_root, raw):
                if path in seen:
                    continue
                seen.add(path)
                notes.append(path)
    elif current_only:
        notes = list_current_notes(repo_root)
    else:
        raise ValueError("provide note paths/directories or --current")

    note_paths = [note_abs.relative_to(repo_root).as_posix() for note_abs in notes]
    ensure_db(db_path)
    with connect(db_path) as conn:
        acceptances = load_current_acceptances(conn)
    accepted_pairs = {
        (accepted_note_path, accepted_gate_path)
        for accepted_note_path, accepted_gate_path, _model_partition in acceptances
    }

    stale: list[StaleGate] = []
    for note_abs, note_path in zip(notes, note_paths):
        applicable_gate_ids = applicable_gate_ids_for_note(note_abs, requested_gate_ids, gates_dir)
        for gate_id in applicable_gate_ids:
            gate_path = gate_path_by_id[gate_id]
            gate_abs = repo_root / gate_path
            if not gate_abs.is_file():
                raise FileNotFoundError(f"Gate not found: {gate_path}")

            if model is None:
                if (note_path, gate_path) not in accepted_pairs:
                    stale.append(StaleGate(note_path, gate_path, "missing-review"))
                continue

            acceptance = acceptances.get((note_path, gate_path, model))
            if acceptance is None:
                stale.append(StaleGate(note_path, gate_path, "missing-review"))
                continue
            acceptance_snapshot = _acceptance_snapshot(acceptance)
            if acceptance_snapshot is None:
                stale.append(StaleGate(note_path, gate_path, "missing-review"))
                continue
            current_note_hash = file_content_sha256(note_abs)
            current_gate_hash = file_content_sha256(gate_abs)
            note_snapshot = NoteSnapshot(path=note_path, content_hash=current_note_hash)
            gate_snapshot = GateSnapshot(id=gate_path, content_hash=current_gate_hash)
            staleness = classify_staleness(
                note_snapshot,
                gate_snapshot,
                acceptance_snapshot,
            )
            if staleness is None:
                continue
            if staleness.reason == "note-changed":
                assert acceptance is not None
                diff = None
                if include_diff:
                    if acceptance.accepted_note_text is not None:
                        current_text = note_abs.read_text(encoding="utf-8")
                        diff = note_diff_from_text(note_path, acceptance.accepted_note_text, current_text)
                stale.append(StaleGate(note_path, gate_path, staleness.reason, diff=diff))
                continue
            stale.append(StaleGate(note_path, gate_path, staleness.reason))

    return sorted(stale, key=lambda s: (s.note_path, s.gate_path))


def render_json(records: list[StaleGate]) -> str:
    items = []
    for record in records:
        entry: dict[str, str] = {
            "note_path": record.note_path,
            "gate_path": record.gate_path,
            "reason": record.reason,
        }
        if record.diff is not None:
            entry["diff"] = record.diff
        items.append(entry)
    return json.dumps(items, indent=2)


def print_grouped(records: list[StaleGate]) -> None:
    grouped: dict[str, list[StaleGate]] = {}
    for record in records:
        grouped.setdefault(record.note_path, []).append(record)
    for note_path in sorted(grouped):
        print(note_path)
        for record in sorted(grouped[note_path], key=lambda item: item.gate_path):
            print(f"  - {record.gate_path} ({record.reason})")


def ack_pairs(
    repo_root: Path,
    pairs: list[str],
    model: str,
    *,
    db_path: Path | None = None,
) -> list[tuple[str, str]]:
    model = normalize_model_partition(model)
    if db_path is None:
        db_path = resolve_db_path(repo_root)
    ensure_db(db_path)
    acked: list[tuple[str, str]] = []
    with connect(db_path) as conn:
        for pair in pairs:
            if ":" not in pair:
                raise ValueError(f"invalid pair (expected note:gate): {pair}")
            note_path, raw_gate = pair.split(":", 1)
            gate_path = normalize_gate_path(repo_root, raw_gate)
            note_abs = repo_root / note_path
            gate_abs = repo_root / gate_path
            if not note_abs.is_file():
                raise FileNotFoundError(f"note not found: {note_path}")
            if not gate_abs.is_file():
                raise FileNotFoundError(f"gate not found: {gate_path}")

            note_snapshot = snapshot_file(conn, repo_root=repo_root, path=note_path)
            gate_snapshot = snapshot_file(conn, repo_root=repo_root, path=gate_path)
            append_acceptance_event(
                conn,
                note_path=note_path,
                gate_path=gate_path,
                model_partition=model,
                accepted_review_pair_id=None,
                accepted_note_snapshot_id=note_snapshot.snapshot_id,
                accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
                accepted_at=iso_now(),
            )
            acked.append((note_path, gate_id_from_stored_path(gate_path)))
        conn.commit()
    return acked
