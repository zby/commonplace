"""Library helpers for selecting stale review targets from the canonical review DB."""

from __future__ import annotations

import difflib
import json
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.freshness import (
    content_sha256_for_text,
    file_content_sha256,
)
from commonplace.review.paths import criterion_id_for_path, criterion_id_from_stored_path, normalize_criterion_path, review_gates_dir
from commonplace.review.resolve_criteria import applicable_criterion_ids_for_note
from commonplace.review.review_db import (
    FreshnessBaseline,
    connect,
    ensure_db,
    load_current_freshness_baselines,
    resolve_db_path,
)
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.collection_conformance import (
    COLLECTION_CONFORMANCE_LENS,
    is_collection_conformance_request,
    note_collection_md_path,
    resolve_collection_criterion_id,
)
from commonplace.review.critique import (
    critique_criterion_path,
    is_critique_request,
    result_kind_for_criterion_path,
)
from commonplace.review.type_conformance import (
    TYPE_CONFORMANCE_LENS,
    is_type_conformance_request,
    note_type_spec_path,
    resolve_type_criterion_id,
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


def _is_user_verified(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    result = frontmatter.parse(text)
    return result.ok and result.data.get("user-verified") is True


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


def list_user_verified_notes(repo_root: Path) -> list[Path]:
    return [
        path
        for path in list_reviewable_notes(repo_root)
        if _is_user_verified(path)
    ]


def _select_notes(
    repo_root: Path,
    *,
    note_filter: list[str] | None,
    user_verified_only: bool,
) -> list[Path]:
    if note_filter and user_verified_only:
        raise ValueError("--note and --user-verified are mutually exclusive")

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
    if user_verified_only:
        return list_user_verified_notes(repo_root)
    raise ValueError("provide note paths/directories or --user-verified")


def _normalize_requested_criterion_ids(
    repo_root: Path,
    criterion_ids: list[str],
) -> tuple[Path, dict[str, str], list[str]]:
    gates_dir = review_gates_dir(repo_root)
    criterion_path_by_id: dict[str, str] = {}
    requested_criterion_ids: list[str] = []
    for raw_criterion in criterion_ids:
        criterion_path = normalize_criterion_path(repo_root, raw_criterion)
        criterion_id = criterion_id_for_path(repo_root, criterion_path)
        criterion_path_by_id[criterion_id] = criterion_path
        requested_criterion_ids.append(criterion_id)
    return gates_dir, criterion_path_by_id, requested_criterion_ids


def _normalize_type_requests(repo_root: Path, requests: list[str]) -> tuple[bool, set[str]]:
    """Split `type`/`type/{name}` requests into (match-all flag, requested type-spec paths)."""
    match_all = False
    requested_paths: set[str] = set()
    for raw in requests:
        raw = raw.strip()
        if raw == TYPE_CONFORMANCE_LENS:
            match_all = True
        else:
            requested_paths.add(resolve_type_criterion_id(repo_root, raw))
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
        if raw == COLLECTION_CONFORMANCE_LENS:
            match_all = True
        else:
            requested_paths.add(resolve_collection_criterion_id(repo_root, raw))
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


def _partition_criterion_requests(criterion_ids: list[str]) -> tuple[list[str], list[str], list[str], bool]:
    type_requests = [criterion_id for criterion_id in criterion_ids if is_type_conformance_request(criterion_id)]
    collection_requests = [criterion_id for criterion_id in criterion_ids if is_collection_conformance_request(criterion_id)]
    catalog_requests = [
        criterion_id
        for criterion_id in criterion_ids
        if not is_type_conformance_request(criterion_id)
        and not is_collection_conformance_request(criterion_id)
        and not is_critique_request(criterion_id)
    ]
    return catalog_requests, type_requests, collection_requests, any(
        is_critique_request(criterion_id) for criterion_id in criterion_ids
    )


@dataclass(frozen=True)
class StaleCriterion:
    note_path: str
    criterion_path: str
    reason: str
    result_kind: str
    diff: str | None = None

    @property
    def criterion_id(self) -> str:
        return criterion_id_from_stored_path(self.criterion_path)


def _criterion_paths_for_notes(
    repo_root: Path,
    criterion_ids: list[str],
    notes: list[Path],
) -> list[tuple[Path, str, list[str]]]:
    catalog_requests, type_requests, collection_requests, critique_requested = _partition_criterion_requests(criterion_ids)
    gates_dir, criterion_path_by_id, requested_criterion_ids = _normalize_requested_criterion_ids(repo_root, catalog_requests)
    match_all_types, requested_type_paths = _normalize_type_requests(repo_root, type_requests)
    match_all_collections, requested_collection_paths = _normalize_collection_requests(repo_root, collection_requests)
    selected: list[tuple[Path, str, list[str]]] = []
    for note_abs in notes:
        note_path = note_abs.relative_to(repo_root).as_posix()
        applicable_ids = applicable_criterion_ids_for_note(note_abs, requested_criterion_ids, gates_dir)
        paths = [criterion_path_by_id[criterion_id] for criterion_id in applicable_ids]
        type_spec_path = _applicable_type_spec_path(
            repo_root,
            note_abs,
            match_all_types=match_all_types,
            requested_type_paths=requested_type_paths,
        )
        if type_spec_path is not None:
            paths.append(type_spec_path)
        collection_md_path = _applicable_collection_md_path(
            repo_root,
            note_abs,
            match_all_collections=match_all_collections,
            requested_collection_paths=requested_collection_paths,
        )
        if collection_md_path is not None:
            paths.append(collection_md_path)
        if critique_requested:
            paths.append(critique_criterion_path(repo_root))
        for criterion_path in paths:
            if not (repo_root / criterion_path).is_file():
                raise FileNotFoundError(f"Gate not found: {criterion_path}")
        selected.append((note_abs, note_path, paths))
    return selected


def note_diff_from_text(note_path: str, previous_text: str, current_text: str) -> str | None:
    diff = "".join(
        difflib.unified_diff(
            previous_text.splitlines(keepends=True),
            current_text.splitlines(keepends=True),
            fromfile=f"a/{note_path}",
            tofile=f"b/{note_path}",
        )
    ).strip()
    return diff or None


def select_stale_criteria(
    repo_root: Path,
    *,
    model: str | None,
    criterion_ids: list[str],
    note_filter: list[str] | None = None,
    user_verified_only: bool = False,
    include_diff: bool = False,
    db_path: Path | None = None,
    freshness_baselines: dict[tuple[str, str, str], FreshnessBaseline] | None = None,
) -> list[StaleCriterion]:
    model = model.strip() if model is not None else None
    model = normalize_model_partition(model) if model else None
    if db_path is None:
        db_path = resolve_db_path(repo_root)

    notes = _select_notes(repo_root, note_filter=note_filter, user_verified_only=user_verified_only)
    selected = _criterion_paths_for_notes(repo_root, criterion_ids, notes)
    if freshness_baselines is None:
        ensure_db(db_path)
        with connect(db_path) as conn:
            freshness_baselines = load_current_freshness_baselines(conn)
    baseline_pairs = {
        (baseline_note_path, baseline_criterion_path)
        for baseline_note_path, baseline_criterion_path, _model_partition in freshness_baselines
    }

    stale: list[StaleCriterion] = []
    for note_abs, note_path, criterion_paths_for_note in selected:
        current_note_text: str | None = None
        current_note_hash: str | None = None
        for criterion_path in criterion_paths_for_note:
            criterion_abs = repo_root / criterion_path
            if model is None:
                if (note_path, criterion_path) not in baseline_pairs:
                    stale.append(
                        StaleCriterion(
                            note_path,
                            criterion_path,
                            "missing-baseline",
                            result_kind=result_kind_for_criterion_path(criterion_path),
                        )
                    )
                continue

            freshness_baseline = freshness_baselines.get((note_path, criterion_path, model))
            if freshness_baseline is None:
                stale.append(
                    StaleCriterion(
                        note_path,
                        criterion_path,
                        "missing-baseline",
                        result_kind=result_kind_for_criterion_path(criterion_path),
                    )
                )
                continue
            if current_note_hash is None:
                current_note_text = note_abs.read_text(encoding="utf-8")
                current_note_hash = content_sha256_for_text(current_note_text)
            current_criterion_hash = file_content_sha256(criterion_abs)
            if freshness_baseline.baseline_criterion_hash != current_criterion_hash:
                reason = "criterion-changed"
            elif freshness_baseline.baseline_note_hash != current_note_hash:
                reason = "note-changed"
            else:
                continue
            diff = None
            if (
                reason == "note-changed"
                and include_diff
                and current_note_text is not None
            ):
                diff = note_diff_from_text(note_path, freshness_baseline.baseline_note_text, current_note_text)
            stale.append(
                StaleCriterion(
                    note_path,
                    criterion_path,
                    reason,
                    diff=diff,
                    result_kind=result_kind_for_criterion_path(criterion_path),
                )
            )

    return sorted(stale, key=lambda s: (s.note_path, s.criterion_path))


def select_requested_criteria(
    repo_root: Path,
    *,
    criterion_ids: list[str],
    note_filter: list[str] | None = None,
    user_verified_only: bool = False,
) -> list[StaleCriterion]:
    notes = _select_notes(repo_root, note_filter=note_filter, user_verified_only=user_verified_only)

    requested: list[StaleCriterion] = []
    for _note_abs, note_path, criterion_paths_for_note in _criterion_paths_for_notes(repo_root, criterion_ids, notes):
        for criterion_path in criterion_paths_for_note:
            requested.append(
                StaleCriterion(
                    note_path,
                    criterion_path,
                    "requested",
                    result_kind=result_kind_for_criterion_path(criterion_path),
                )
            )

    return sorted(requested, key=lambda s: (s.note_path, s.criterion_path))


def render_json(records: list[StaleCriterion], *, model_partition: str | None = None) -> str:
    items = []
    for record in records:
        entry: dict[str, str] = {
            "note_path": record.note_path,
            "criterion_path": record.criterion_path,
            "criterion_id": record.criterion_id,
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


def render_grouped(records: list[StaleCriterion]) -> str:
    grouped: dict[str, list[StaleCriterion]] = {}
    for record in records:
        grouped.setdefault(record.note_path, []).append(record)
    lines: list[str] = []
    for note_path in sorted(grouped):
        lines.append(note_path)
        for record in sorted(grouped[note_path], key=lambda item: item.criterion_path):
            lines.append(f"  - {record.criterion_path} ({record.reason})")
    return "\n".join(lines)
