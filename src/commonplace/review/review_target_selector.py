"""Library helpers for selecting stale review targets from the canonical review DB."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.paths import GATES_ROOT
from commonplace.review.resolve_gates import applicable_gate_ids_for_note
from commonplace.review.review_db import (
    append_acceptance_event,
    connect,
    ensure_db,
    load_current_acceptances,
    resolve_db_path,
)
from commonplace.review.review_metadata import (
    file_text_at_provenance,
    git_blob_sha,
    iso_now,
    review_note_provenance,
)
from commonplace.review.review_model import normalize_model_id

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
    gate_id: str
    reason: str
    diff: str | None = None


def note_diff_since(
    repo_root: Path,
    note_path: str,
    note_abs: Path,
    accepted_note_sha: str,
    accepted_note_commit: str | None,
) -> str | None:
    import difflib

    previous_text = file_text_at_provenance(
        repo_root,
        path=Path(note_path),
        commit=accepted_note_commit,
        blob_sha=accepted_note_sha,
    )
    if previous_text is None:
        return None

    current_text = note_abs.read_text(encoding="utf-8")
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
    model: str,
    gate_ids: list[str],
    note_filter: list[str] | None = None,
    current_only: bool = False,
    include_diff: bool = False,
    db_path: Path | None = None,
) -> list[StaleGate]:
    gates_dir = repo_root / GATES_ROOT
    model = model.strip()
    if not model:
        raise ValueError("model is required")
    model = normalize_model_id(model)
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
    ensure_db(repo_root, db_path)
    with connect(db_path) as conn:
        acceptances = load_current_acceptances(conn)

    stale: list[StaleGate] = []
    for note_abs, note_path in zip(notes, note_paths):
        current_note_sha = git_blob_sha(note_abs)
        applicable_gate_ids = applicable_gate_ids_for_note(note_abs, gate_ids, gates_dir)
        for gate_id in applicable_gate_ids:
            gate_abs = gates_dir / f"{gate_id}.md"
            if not gate_abs.is_file():
                raise FileNotFoundError(f"Gate not found: {gate_id}")

            # Bundles resolve directly from gate directories, so the gate file hash is the whole contract today.
            current_gate_sha = git_blob_sha(gate_abs)
            acceptance = acceptances.get((note_path, gate_id, model))
            if acceptance is None:
                stale.append(StaleGate(note_path, gate_id, "missing-review"))
                continue
            if acceptance.accepted_gate_sha != current_gate_sha:
                stale.append(StaleGate(note_path, gate_id, "gate-changed"))
                continue
            if acceptance.accepted_note_sha != current_note_sha:
                diff = None
                if include_diff:
                    diff = note_diff_since(
                        repo_root,
                        note_path,
                        note_abs,
                        acceptance.accepted_note_sha,
                        acceptance.accepted_note_commit,
                    )
                stale.append(StaleGate(note_path, gate_id, "note-changed", diff=diff))

    return sorted(stale, key=lambda s: (s.note_path, s.gate_id))


def render_json(records: list[StaleGate]) -> str:
    items = []
    for record in records:
        entry: dict[str, str] = {
            "note_path": record.note_path,
            "gate_id": record.gate_id,
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
        for record in sorted(grouped[note_path], key=lambda item: item.gate_id):
            print(f"  - {record.gate_id} ({record.reason})")


def ack_pairs(repo_root: Path, pairs: list[str], model: str, *, db_path: Path | None = None) -> None:
    model = normalize_model_id(model)
    if db_path is None:
        db_path = resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    with connect(db_path) as conn:
        for pair in pairs:
            if ":" not in pair:
                print(f"error: invalid pair (expected note:gate): {pair}", file=sys.stderr)
                sys.exit(1)
            note_path, gate_id = pair.split(":", 1)
            note_abs = repo_root / note_path
            gate_abs = repo_root / GATES_ROOT / f"{gate_id}.md"
            if not note_abs.is_file():
                print(f"error: note not found: {note_path}", file=sys.stderr)
                sys.exit(1)
            if not gate_abs.is_file():
                print(f"error: gate not found: {gate_id}", file=sys.stderr)
                sys.exit(1)

            try:
                note_sha, note_commit = review_note_provenance(repo_root, Path(note_path))
            except ValueError as exc:
                print(f"error: {exc}", file=sys.stderr)
                sys.exit(1)
            current_gate_sha = git_blob_sha(gate_abs)
            append_acceptance_event(
                conn,
                note_path=note_path,
                gate_id=gate_id,
                model_id=model,
                accepted_review_id=None,
                accepted_note_sha=note_sha,
                accepted_note_commit=note_commit,
                accepted_gate_sha=current_gate_sha,
                accepted_at=iso_now(),
                acceptance_kind="trivial-change-ack",
            )
            print(f"acked: {note_path} {gate_id}")
        conn.commit()
