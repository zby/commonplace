"""Library functions for ack_trivial_note_changes.

Pure logic lives here; ack_trivial_note_changes.py is the thin CLI wrapper.

A gate without a valid `watches:` declaration is skipped, never acked: no
declaration means the gate watches the whole note, so no note change is
trivial against it. Conformance pairs rely on this — neither type specs nor
COLLECTION.md contracts declare `watches:`, which is what keeps them safe to
select here via `--all-gates`.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter
from commonplace.review.review_db import (
    connect,
    load_current_freshness_baselines,
    prepare_review_db,
)
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.review_target_selector import select_stale_criteria


_TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
KNOWN_WATCHES = {"body", "title", "description"}


def _normalize_markdown(text: str) -> str:
    normalized_lines: list[str] = []
    for line in text.splitlines():
        if line.strip():
            normalized_lines.append(line.rstrip())
    return "\n".join(normalized_lines)


def _normalize_scalar(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return tuple(_normalize_scalar(item) for item in value)
    return value


def _extract_title(body_text: str) -> str:
    match = _TITLE_RE.search(body_text)
    return match.group(1).strip() if match else ""


def _extract_body_without_title(body_text: str) -> str:
    match = _TITLE_RE.search(body_text)
    if match is None:
        return _normalize_markdown(body_text)
    return _normalize_markdown(body_text[match.end() :])


def _frontmatter_other(data: dict[str, Any]) -> dict[str, Any]:
    return {
        key: _normalize_scalar(value)
        for key, value in data.items()
        if key != "description"
    }


def _note_parts(content: str) -> dict[str, Any] | None:
    parsed = frontmatter.parse(content)
    if not parsed.ok:
        return None
    body_text = frontmatter.strip(content)
    return {
        "title": _extract_title(body_text),
        "description": _normalize_scalar(parsed.data.get("description", "")),
        "body": _extract_body_without_title(body_text),
        "frontmatter_other": _frontmatter_other(parsed.data),
    }


def _load_gate_watches(criterion_path: Path) -> set[str] | None:
    try:
        parsed = frontmatter.parse(criterion_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return None
    if not parsed.ok:
        return None
    raw = parsed.data.get("watches")
    if not isinstance(raw, list) or not raw:
        return None
    watches: set[str] = set()
    for item in raw:
        if not isinstance(item, str):
            return None
        watches.add(item)
    if not watches.issubset(KNOWN_WATCHES):
        return None
    return watches


def has_only_unwatched_changes(
    previous_text: str,
    current_text: str,
    *,
    watches: set[str],
) -> bool:
    """True when no watched note part changed between the two texts.

    Callers pass texts whose raw hashes already differ; a purely cosmetic
    change (whitespace, formatting) alters no parsed part and qualifies.
    """
    previous = _note_parts(previous_text)
    current = _note_parts(current_text)
    if previous is None or current is None:
        return False
    return all(previous.get(key) == current.get(key) for key in watches)


def qualifying_pairs(
    repo_root: Path,
    *,
    model: str,
    criterion_ids: list[str],
    note_filter: list[str] | None = None,
    user_verified_only: bool = False,
    db_path: Path | None = None,
) -> list[str]:
    model = normalize_model_partition(model)
    db_path = prepare_review_db(repo_root, str(db_path) if db_path is not None else None)
    with connect(db_path) as conn:
        freshness_baselines = load_current_freshness_baselines(conn)
    stale_records = [
        record
        for record in select_stale_criteria(
            repo_root,
            model=model,
            criterion_ids=criterion_ids,
            note_filter=note_filter,
            user_verified_only=user_verified_only,
            include_diff=False,
            db_path=db_path,
            freshness_baselines=freshness_baselines,
        )
        if record.reason == "note-changed"
    ]

    current_text_cache: dict[str, str] = {}
    gate_watches_cache: dict[str, set[str] | None] = {}
    pairs: list[str] = []
    for record in stale_records:
        freshness_baseline = freshness_baselines.get((record.note_path, record.criterion_path, model))
        if freshness_baseline is None:
            continue

        if record.criterion_path not in gate_watches_cache:
            gate_watches_cache[record.criterion_path] = _load_gate_watches(repo_root / record.criterion_path)
        watches = gate_watches_cache[record.criterion_path]
        if watches is None:
            # No valid watches declaration = the gate watches the whole note;
            # nothing is trivial against it. Type-spec gates land here.
            continue

        previous_text = freshness_baseline.baseline_note_text
        if previous_text is None:
            continue

        if record.note_path not in current_text_cache:
            current_text_cache[record.note_path] = (repo_root / record.note_path).read_text(encoding="utf-8")
        current_text = current_text_cache[record.note_path]

        if has_only_unwatched_changes(
            previous_text,
            current_text,
            watches=watches,
        ):
            pairs.append(f"{record.note_path}:{record.criterion_path}")

    return sorted(set(pairs))
