#!/usr/bin/env python3
"""Helpers for multi-note single-gate review prompts and parsing."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Sequence

from commonplace.review.run_review_bundle_lib import extract_bundle_reviews, rewrite_bundle_result_footers


NOTE_START_RE = re.compile(r"^=== NOTE START: (?P<note_path>.+?) ===$")
NOTE_END_RE = re.compile(r"^=== NOTE END: (?P<note_path>.+?) ===$")


RESERVED_SENTINEL_RE = re.compile(r"^===\s.+\s===$")


@dataclass(frozen=True)
class GateSweepNoteTarget:
    note_path: str
    review_run_id: int
    note_text: str = ""
    resolved_links: Sequence[tuple[str, str, str]] = ()
    unresolved_links: Sequence[tuple[str, str]] = ()


def _normalize_targets(notes: Sequence[GateSweepNoteTarget]) -> list[GateSweepNoteTarget]:
    normalized = list(notes)
    if not normalized:
        raise ValueError("at least one note is required")

    seen: set[str] = set()
    for note in normalized:
        note_path = note.note_path.strip()
        if not note_path:
            raise ValueError("note_path must not be empty")
        if note_path in seen:
            raise ValueError(f"duplicate note in gate sweep target list: {note_path}")
        if not note.note_text.strip():
            raise ValueError(f"note_text must not be empty: {note_path}")
        _check_reserved_sentinels(note.note_text, note_path)
        seen.add(note_path)
    return normalized


def _check_reserved_sentinels(text: str, source_label: str) -> None:
    """Raise if text contains lines matching the === ... === sentinel pattern."""
    for lineno, line in enumerate(text.splitlines(), start=1):
        if RESERVED_SENTINEL_RE.match(line.strip()):
            raise ValueError(
                f"reserved sentinel in {source_label} line {lineno}: {line.strip()!r}"
            )


def build_gate_sweep_prompt(
    *,
    gate_id: str,
    gate_text: str,
    notes: Sequence[GateSweepNoteTarget],
    gate_path: str | None = None,
) -> str:
    gate_id = gate_id.strip()
    if not gate_id:
        raise ValueError("gate_id must not be empty")
    if not gate_text.strip():
        raise ValueError("gate_text must not be empty")

    normalized_notes = _normalize_targets(notes)
    gate_path = gate_path or f"kb/instructions/review-gates/{gate_id}.md"

    lines = [
        f"Write gate reviews for gate {gate_id} for these notes:",
        "",
        "Reading scope for this run:",
        "- The gate definition and all target note contents are included below. Do not read them from disk.",
        "- For semantic grounding or consistency checks, follow only links that appear in each target note.",
        "- When following a markdown link from a target note, use that note's pre-resolved path table below instead of searching for targets by name.",
        "- Ignore review backups, workshop copies, and historical artifacts unless a target note links to them explicitly.",
        "- Evaluate each note independently. Do not compare notes against each other or use one note to calibrate another.",
        "",
        "Output contract for this run:",
        "- Do not write files or invoke review helper scripts.",
        "- Return exactly one markdown document in this process's stdout.",
        "- Use exactly one note block per target note.",
        "- Inside each note block, include exactly one gate review block for the requested gate.",
        "- Use these exact sentinels for every note block:",
        "  === NOTE START: <note-path> ===",
        "  === GATE REVIEW START: <gate-id> ===",
        "  === GATE REVIEW END: <gate-id> ===",
        "  === NOTE END: <note-path> ===",
        "- Inside each gate block, include a decision line in a parseable form such as `## Result: PASS` or `## Result: WARN`.",
        "- Make the `## Result:` line the last non-empty line inside each gate block.",
        "- End output after the final note block.",
        "",
        "Target notes for this run:",
    ]
    for note in normalized_notes:
        lines.append(f"- {note.note_path} (review run id: {note.review_run_id})")

    lines.extend(
        [
            "",
            f"Requested gate definition file: {gate_path}",
            "",
            "Pre-resolved markdown links by target note:",
        ]
    )
    for note in normalized_notes:
        lines.extend(
            [
                "",
                f"### {note.note_path}",
                f"Review run id: {note.review_run_id}",
                "",
                "Resolved markdown links:",
            ]
        )
        if note.resolved_links:
            for link_text, raw_target, repo_rel in note.resolved_links:
                lines.append(f"- [{link_text}]({raw_target}) -> {repo_rel}")
        else:
            lines.append("- none")

        if note.unresolved_links:
            lines.extend(
                [
                    "",
                    "Unresolved markdown links:",
                    "- Treat these as broken links if they become relevant; do not search for alternate targets.",
                ]
            )
            for link_text, raw_target in note.unresolved_links:
                lines.append(f"- [{link_text}]({raw_target})")

    lines.extend(
        [
            "",
            "Target note contents (authoritative for this run):",
        ]
    )
    for note in normalized_notes:
        lines.extend(
            [
                f"=== note: {note.note_path} ===",
                note.note_text.rstrip(),
                "",
            ]
        )

    lines.extend(
        [
            "",
            "Batch template:",
        ]
    )
    for note in normalized_notes:
        lines.extend(
            [
                f"=== NOTE START: {note.note_path} ===",
                f"=== GATE REVIEW START: {gate_id} ===",
                "### Summary",
                "<short paragraph>",
                "",
                "### Findings",
                "- <severity>: <finding>",
                "",
                "### Suggested Revision",
                "<optional; omit if not needed>",
                "",
                "## Result: PASS|WARN|FAIL|ERROR",
                f"=== GATE REVIEW END: {gate_id} ===",
                f"=== NOTE END: {note.note_path} ===",
                "",
            ]
        )

    lines.extend(
        [
            "",
            "Requested gate definition (authoritative for this run):",
            f"=== gate: {gate_id} ===",
            gate_text.rstrip(),
            "",
        ]
    )
    return "\n".join(lines)


def extract_gate_sweep_reviews(
    bundle_markdown: str,
    *,
    gate_id: str,
    expected_note_paths: Sequence[str],
) -> dict[str, str]:
    expected_paths = list(expected_note_paths)
    expected = set(expected_paths)
    reviews: dict[str, str] = {}
    current_note_path: str | None = None
    current_lines: list[str] = []

    for raw_line in bundle_markdown.splitlines():
        start_match = NOTE_START_RE.match(raw_line.strip())
        if start_match is not None:
            if current_note_path is not None:
                raise ValueError(f"nested note review start before closing {current_note_path}")
            note_path = start_match.group("note_path")
            if note_path not in expected:
                raise ValueError(f"unexpected note in gate sweep output: {note_path}")
            if note_path in reviews:
                raise ValueError(f"duplicate note in gate sweep output: {note_path}")
            current_note_path = note_path
            current_lines = []
            continue

        end_match = NOTE_END_RE.match(raw_line.strip())
        if end_match is not None:
            note_path = end_match.group("note_path")
            if current_note_path is None:
                raise ValueError(f"note review end without start: {note_path}")
            if note_path != current_note_path:
                raise ValueError(f"note review end mismatch: expected {current_note_path}, found {note_path}")
            note_block = "\n".join(current_lines).strip()
            if not note_block:
                raise ValueError(f"empty note review block: {note_path}")
            reviews[note_path] = extract_bundle_reviews(note_block, expected_gate_ids=[gate_id])[gate_id]
            current_note_path = None
            current_lines = []
            continue

        if current_note_path is not None:
            current_lines.append(raw_line)

    if current_note_path is not None:
        raise ValueError(f"unterminated note review block: {current_note_path}")

    missing = [note_path for note_path in expected_paths if note_path not in reviews]
    if missing:
        raise ValueError(f"missing note reviews in gate sweep output: {', '.join(missing)}")

    return reviews


def rewrite_gate_sweep_result_footers(
    bundle_markdown: str,
    *,
    gate_id: str,
    parsed_reviews: dict[str, str],
) -> str:
    rewritten_lines: list[str] = []
    current_note_path: str | None = None
    current_note_lines: list[str] = []

    for raw_line in bundle_markdown.splitlines():
        start_match = NOTE_START_RE.match(raw_line.strip())
        if start_match is not None:
            current_note_path = start_match.group("note_path")
            current_note_lines = []
            rewritten_lines.append(raw_line)
            continue

        end_match = NOTE_END_RE.match(raw_line.strip())
        if end_match is not None:
            note_path = end_match.group("note_path")
            if current_note_path == note_path and note_path in parsed_reviews:
                rewritten_note = rewrite_bundle_result_footers(
                    "\n".join(current_note_lines),
                    parsed_reviews={gate_id: parsed_reviews[note_path]},
                )
                rewritten_lines.extend(rewritten_note.rstrip("\n").splitlines())
            else:
                rewritten_lines.extend(current_note_lines)
            rewritten_lines.append(raw_line)
            current_note_path = None
            current_note_lines = []
            continue

        if current_note_path is not None:
            current_note_lines.append(raw_line)
        else:
            rewritten_lines.append(raw_line)

    rewritten = "\n".join(rewritten_lines)
    if bundle_markdown.endswith("\n"):
        return rewritten + "\n"
    return rewritten
