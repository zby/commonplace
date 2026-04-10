"""Library functions for ack_trivial_note_changes.

Pure logic lives here; ack_trivial_note_changes.py is the thin CLI wrapper.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter
from commonplace.review.paths import GATES_ROOT
from commonplace.review.review_db import (
    connect,
    load_current_acceptances,
    prepare_review_db,
)
from commonplace.review.review_metadata import file_text_at_commit, file_text_at_provenance
from commonplace.review.review_target_selector import select_stale_gates


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


def _load_gate_watches(gate_path: Path) -> set[str] | None:
    try:
        parsed = frontmatter.parse(gate_path.read_text(encoding="utf-8"))
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
    previous = _note_parts(previous_text)
    current = _note_parts(current_text)
    if previous is None or current is None:
        return False

    watched_keys = set(watches)
    for key in watched_keys:
        if previous[key] != current[key]:
            return False

    changed_keys = {
        key
        for key in previous
        if previous[key] != current[key]
    }
    if not changed_keys:
        return False

    return bool(changed_keys - watched_keys)


def _load_previous_note_text(
    repo_root: Path,
    *,
    note_path: str,
    accepted_note_sha: str,
    accepted_note_commit: str | None,
    accepted_at: str | None,
) -> str | None:
    previous_text = file_text_at_provenance(
        repo_root,
        path=Path(note_path),
        commit=accepted_note_commit,
        blob_sha=accepted_note_sha,
    )
    if previous_text is None and accepted_at:
        result = subprocess.run(
            ["git", "log", "-1", f"--before={accepted_at}", "--format=%H", "--", note_path],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        commit = result.stdout.strip()
        if not commit:
            result = subprocess.run(
                ["git", "log", "--reverse", f"--after={accepted_at}", "--format=%H", "--", note_path],
                cwd=repo_root,
                capture_output=True,
                text=True,
            )
            lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            commit = lines[0] if lines else ""
        if commit:
            previous_text = file_text_at_commit(repo_root, commit, Path(note_path))
    return previous_text


def qualifying_pairs(
    repo_root: Path,
    *,
    model: str,
    gate_ids: list[str],
    note_filter: list[str] | None = None,
    current_only: bool = False,
    db_path: Path | None = None,
) -> list[str]:
    if db_path is None:
        db_path = prepare_review_db(repo_root)
    stale_records = [
        record
        for record in select_stale_gates(
            repo_root,
            model=model,
            gate_ids=gate_ids,
            note_filter=note_filter,
            current_only=current_only,
            include_diff=False,
            db_path=db_path,
        )
        if record.reason == "note-changed"
    ]

    with connect(db_path) as conn:
        acceptances = load_current_acceptances(conn)

    previous_text_cache: dict[tuple[str, str, str | None], str | None] = {}
    current_text_cache: dict[str, str] = {}
    gate_watches_cache: dict[str, set[str] | None] = {}
    pairs: list[str] = []
    for record in stale_records:
        acceptance = acceptances.get((record.note_path, record.gate_id, model))
        if acceptance is None:
            continue

        if record.gate_id not in gate_watches_cache:
            gate_watches_cache[record.gate_id] = _load_gate_watches(repo_root / GATES_ROOT / f"{record.gate_id}.md")
        watches = gate_watches_cache[record.gate_id]
        if watches is None:
            continue

        previous_key = (record.note_path, acceptance.accepted_note_sha, acceptance.accepted_note_commit)
        if previous_key not in previous_text_cache:
            previous_text_cache[previous_key] = _load_previous_note_text(
                repo_root,
                note_path=record.note_path,
                accepted_note_sha=acceptance.accepted_note_sha,
                accepted_note_commit=acceptance.accepted_note_commit,
                accepted_at=acceptance.accepted_at,
            )
        previous_text = previous_text_cache[previous_key]
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
            pairs.append(f"{record.note_path}:{record.gate_id}")

    return sorted(set(pairs))
