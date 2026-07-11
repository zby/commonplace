"""Library helpers for selecting stale review targets from the canonical review DB."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.freshness import (
    AcceptanceSnapshot,
    GateSnapshot,
    NoteSnapshot,
    classify_staleness,
    content_sha256_for_text,
    file_content_sha256,
)
from commonplace.review.paths import gate_id_for_path, gate_id_from_stored_path, normalize_gate_path, review_gates_dir
from commonplace.review.resolve_gates import applicable_gate_ids_for_note
from commonplace.review.review_db import (
    AcceptanceState,
    connect,
    ensure_db,
    load_current_acceptances,
    resolve_db_path,
)
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.collection_conformance import (
    COLLECTION_GATE_LENS,
    is_collection_gate_request,
    note_collection_md_path,
    resolve_collection_gate_id,
)
from commonplace.review.critique import (
    critique_gate_path,
    is_critique_request,
    result_kind_for_gate_path,
)
from commonplace.review.type_conformance import (
    TYPE_GATE_LENS,
    is_type_gate_request,
    note_type_spec_path,
    resolve_type_gate_id,
)

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


def _select_notes(
    repo_root: Path,
    *,
    note_filter: list[str] | None,
    current_only: bool,
) -> list[Path]:
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
        return notes
    if current_only:
        return list_current_notes(repo_root)
    raise ValueError("provide note paths/directories or --current")


def _normalize_requested_gate_ids(
    repo_root: Path,
    gate_ids: list[str],
) -> tuple[Path, dict[str, str], list[str]]:
    gates_dir = review_gates_dir(repo_root)
    gate_path_by_id: dict[str, str] = {}
    requested_gate_ids: list[str] = []
    for raw_gate in gate_ids:
        gate_path = normalize_gate_path(repo_root, raw_gate)
        gate_id = gate_id_for_path(repo_root, gate_path)
        gate_path_by_id[gate_id] = gate_path
        requested_gate_ids.append(gate_id)
    return gates_dir, gate_path_by_id, requested_gate_ids


def _normalize_type_requests(repo_root: Path, requests: list[str]) -> tuple[bool, set[str]]:
    """Split `type`/`type/{name}` requests into (match-all flag, requested type-spec paths)."""
    match_all = False
    requested_paths: set[str] = set()
    for raw in requests:
        raw = raw.strip()
        if raw == TYPE_GATE_LENS:
            match_all = True
        else:
            requested_paths.add(resolve_type_gate_id(repo_root, raw))
    return match_all, requested_paths


def _applicable_type_spec_path(
    repo_root: Path,
    note_abs: Path,
    *,
    match_all_types: bool,
    requested_type_paths: set[str],
) -> str | None:
    """The note's type-conformance gate path, when type pairs were requested for it."""
    if not match_all_types and not requested_type_paths:
        return None
    type_spec_path = note_type_spec_path(repo_root, note_abs)
    if type_spec_path is None:
        return None
    if match_all_types or type_spec_path in requested_type_paths:
        return type_spec_path
    return None


def _normalize_collection_requests(repo_root: Path, requests: list[str]) -> tuple[bool, set[str]]:
    """Split `collection`/`collection/{path}` requests into (match-all flag, COLLECTION.md paths)."""
    match_all = False
    requested_paths: set[str] = set()
    for raw in requests:
        raw = raw.strip()
        if raw == COLLECTION_GATE_LENS:
            match_all = True
        else:
            requested_paths.add(resolve_collection_gate_id(repo_root, raw))
    return match_all, requested_paths


def _applicable_collection_md_path(
    repo_root: Path,
    note_abs: Path,
    *,
    match_all_collections: bool,
    requested_collection_paths: set[str],
) -> str | None:
    """The note's collection-conformance gate path, when collection pairs were requested for it."""
    if not match_all_collections and not requested_collection_paths:
        return None
    collection_md_path = note_collection_md_path(repo_root, note_abs)
    if collection_md_path is None:
        return None
    if match_all_collections or collection_md_path in requested_collection_paths:
        return collection_md_path
    return None


def _partition_gate_requests(gate_ids: list[str]) -> tuple[list[str], list[str], list[str], bool]:
    type_requests = [gate_id for gate_id in gate_ids if is_type_gate_request(gate_id)]
    collection_requests = [gate_id for gate_id in gate_ids if is_collection_gate_request(gate_id)]
    catalog_requests = [
        gate_id
        for gate_id in gate_ids
        if not is_type_gate_request(gate_id)
        and not is_collection_gate_request(gate_id)
        and not is_critique_request(gate_id)
    ]
    return catalog_requests, type_requests, collection_requests, any(
        is_critique_request(gate_id) for gate_id in gate_ids
    )


@dataclass(frozen=True)
class StaleGate:
    note_path: str
    gate_path: str
    reason: str
    diff: str | None = None
    result_kind: str = "verdict"

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
    catalog_requests, type_requests, collection_requests, critique_requested = _partition_gate_requests(gate_ids)
    gates_dir, gate_path_by_id, requested_gate_ids = _normalize_requested_gate_ids(repo_root, catalog_requests)
    match_all_types, requested_type_paths = _normalize_type_requests(repo_root, type_requests)
    match_all_collections, requested_collection_paths = _normalize_collection_requests(repo_root, collection_requests)
    model = model.strip() if model is not None else None
    model = normalize_model_partition(model) if model else None
    if db_path is None:
        db_path = resolve_db_path(repo_root)

    notes = _select_notes(repo_root, note_filter=note_filter, current_only=current_only)
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
        gate_paths_for_note = [gate_path_by_id[gate_id] for gate_id in applicable_gate_ids]
        type_spec_path = _applicable_type_spec_path(
            repo_root,
            note_abs,
            match_all_types=match_all_types,
            requested_type_paths=requested_type_paths,
        )
        if type_spec_path is not None:
            gate_paths_for_note.append(type_spec_path)
        collection_md_path = _applicable_collection_md_path(
            repo_root,
            note_abs,
            match_all_collections=match_all_collections,
            requested_collection_paths=requested_collection_paths,
        )
        if collection_md_path is not None:
            gate_paths_for_note.append(collection_md_path)
        if critique_requested:
            gate_paths_for_note.append(critique_gate_path(repo_root))
        current_note_text: str | None = None
        current_note_hash: str | None = None
        for gate_path in gate_paths_for_note:
            gate_abs = repo_root / gate_path
            if not gate_abs.is_file():
                raise FileNotFoundError(f"Gate not found: {gate_path}")

            if model is None:
                if (note_path, gate_path) not in accepted_pairs:
                    stale.append(
                        StaleGate(
                            note_path,
                            gate_path,
                            "missing-review",
                            result_kind=result_kind_for_gate_path(gate_path),
                        )
                    )
                continue

            acceptance = acceptances.get((note_path, gate_path, model))
            if acceptance is None:
                stale.append(
                    StaleGate(
                        note_path,
                        gate_path,
                        "missing-review",
                        result_kind=result_kind_for_gate_path(gate_path),
                    )
                )
                continue
            acceptance_snapshot = _acceptance_snapshot(acceptance)
            if acceptance_snapshot is None:
                stale.append(
                    StaleGate(
                        note_path,
                        gate_path,
                        "missing-review",
                        result_kind=result_kind_for_gate_path(gate_path),
                    )
                )
                continue
            if current_note_hash is None:
                current_note_text = note_abs.read_text(encoding="utf-8")
                current_note_hash = content_sha256_for_text(current_note_text)
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
            diff = None
            if (
                staleness.reason == "note-changed"
                and include_diff
                and acceptance.accepted_note_text is not None
                and current_note_text is not None
            ):
                diff = note_diff_from_text(note_path, acceptance.accepted_note_text, current_note_text)
            stale.append(
                StaleGate(
                    note_path,
                    gate_path,
                    staleness.reason,
                    diff=diff,
                    result_kind=result_kind_for_gate_path(gate_path),
                )
            )

    return sorted(stale, key=lambda s: (s.note_path, s.gate_path))


def select_requested_gates(
    repo_root: Path,
    *,
    gate_ids: list[str],
    note_filter: list[str] | None = None,
    current_only: bool = False,
) -> list[StaleGate]:
    catalog_requests, type_requests, collection_requests, critique_requested = _partition_gate_requests(gate_ids)
    gates_dir, gate_path_by_id, requested_gate_ids = _normalize_requested_gate_ids(repo_root, catalog_requests)
    match_all_types, requested_type_paths = _normalize_type_requests(repo_root, type_requests)
    match_all_collections, requested_collection_paths = _normalize_collection_requests(repo_root, collection_requests)
    notes = _select_notes(repo_root, note_filter=note_filter, current_only=current_only)

    requested: list[StaleGate] = []
    for note_abs in notes:
        note_path = note_abs.relative_to(repo_root).as_posix()
        applicable_gate_ids = applicable_gate_ids_for_note(note_abs, requested_gate_ids, gates_dir)
        gate_paths_for_note = [gate_path_by_id[gate_id] for gate_id in applicable_gate_ids]
        type_spec_path = _applicable_type_spec_path(
            repo_root,
            note_abs,
            match_all_types=match_all_types,
            requested_type_paths=requested_type_paths,
        )
        if type_spec_path is not None:
            gate_paths_for_note.append(type_spec_path)
        collection_md_path = _applicable_collection_md_path(
            repo_root,
            note_abs,
            match_all_collections=match_all_collections,
            requested_collection_paths=requested_collection_paths,
        )
        if collection_md_path is not None:
            gate_paths_for_note.append(collection_md_path)
        if critique_requested:
            gate_paths_for_note.append(critique_gate_path(repo_root))
        for gate_path in gate_paths_for_note:
            gate_abs = repo_root / gate_path
            if not gate_abs.is_file():
                raise FileNotFoundError(f"Gate not found: {gate_path}")
            requested.append(
                StaleGate(
                    note_path,
                    gate_path,
                    "requested",
                    result_kind=result_kind_for_gate_path(gate_path),
                )
            )

    return sorted(requested, key=lambda s: (s.note_path, s.gate_path))


def render_json(records: list[StaleGate], *, model_partition: str | None = None) -> str:
    items = []
    for record in records:
        entry: dict[str, str] = {
            "note_path": record.note_path,
            "gate_path": record.gate_path,
            "gate_id": record.gate_id,
            "reason": record.reason,
            "result_kind": record.result_kind,
        }
        if record.diff is not None:
            entry["diff"] = record.diff
        items.append(entry)
    return json.dumps(
        {
            "model_partition": model_partition,
            "targets": items,
        },
        indent=2,
    )


def render_grouped(records: list[StaleGate]) -> str:
    grouped: dict[str, list[StaleGate]] = {}
    for record in records:
        grouped.setdefault(record.note_path, []).append(record)
    lines: list[str] = []
    for note_path in sorted(grouped):
        lines.append(note_path)
        for record in sorted(grouped[note_path], key=lambda item: item.gate_path):
            lines.append(f"  - {record.gate_path} ({record.reason})")
    return "\n".join(lines)
