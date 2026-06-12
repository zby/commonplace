"""Render review protocol prompts.

One renderer for every packing shape: the prompt carries N note targets and
M gate definitions, each embedded once, and requests one output block per
requested (note, gate) pair.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

from commonplace.review.protocol.format import (
    DECISION_LINE_INSTRUCTION,
    PAIR_END_TEMPLATE,
    PAIR_KEY_SEPARATOR,
    PAIR_START_TEMPLATE,
    RESERVED_SENTINEL_RE,
    RESULT_LINE_TEMPLATE,
)


OutputMode = Literal["stdout", "file"]


@dataclass(frozen=True)
class NoteReviewTarget:
    note_path: str
    review_run_id: int
    gate_ids: tuple[str, ...]
    note_text: str
    resolved_links: Sequence[tuple[str, str, str]] = ()
    unresolved_links: Sequence[tuple[str, str]] = ()


def _validate_embedded_text(label: str, text: str) -> None:
    for lineno, line in enumerate(text.splitlines(), start=1):
        if RESERVED_SENTINEL_RE.match(line.strip()):
            raise ValueError(f"reserved sentinel in {label} line {lineno}: {line.strip()!r}")


def _validate_targets(
    notes: Sequence[NoteReviewTarget],
    gate_texts: dict[str, str],
) -> None:
    if not notes:
        raise ValueError("at least one note is required")

    seen_notes: set[str] = set()
    for note in notes:
        note_path = note.note_path.strip()
        if not note_path:
            raise ValueError("note_path must not be empty")
        if PAIR_KEY_SEPARATOR in note_path:
            raise ValueError(f"note_path must not contain {PAIR_KEY_SEPARATOR!r}: {note_path}")
        if note_path in seen_notes:
            raise ValueError(f"duplicate note in review target list: {note_path}")
        if not note.gate_ids:
            raise ValueError(f"note has no requested gates: {note_path}")
        if len(set(note.gate_ids)) != len(note.gate_ids):
            raise ValueError(f"duplicate gate requested for note: {note_path}")
        if not note.note_text.strip():
            raise ValueError(f"note_text must not be empty: {note_path}")
        _validate_embedded_text(note_path, note.note_text)
        seen_notes.add(note_path)

    requested_gate_ids = {gate_id for note in notes for gate_id in note.gate_ids}
    for gate_id in sorted(requested_gate_ids):
        if PAIR_KEY_SEPARATOR in gate_id:
            raise ValueError(f"gate_id must not contain {PAIR_KEY_SEPARATOR!r}: {gate_id}")
        gate_text = gate_texts.get(gate_id)
        if gate_text is None or not gate_text.strip():
            raise ValueError(f"missing gate text: {gate_id}")
        _validate_embedded_text(f"gate {gate_id}", gate_text)


def render_pairs_prompt(
    *,
    notes: Sequence[NoteReviewTarget],
    gate_texts: dict[str, str],
    output_mode: OutputMode = "stdout",
    bundle_output_path: str | None = None,
) -> str:
    _validate_targets(notes, gate_texts)
    gate_ids = sorted({gate_id for note in notes for gate_id in note.gate_ids})

    if output_mode == "file":
        if bundle_output_path is None:
            raise ValueError("bundle_output_path is required for file output mode")
        destination_lines = [
            f"- Write exactly one markdown document to `{bundle_output_path}`.",
            "- Do not invoke review helper scripts while writing the review bundle.",
        ]
    elif output_mode == "stdout":
        destination_lines = [
            "- Do not write files or invoke review helper scripts.",
            "- Return exactly one markdown document in this process's stdout.",
        ]
    else:
        raise ValueError(f"unknown output mode: {output_mode}")

    lines = [
        "Write gate reviews for the requested (note, gate) pairs listed below.",
        "",
        "Reading scope for this run:",
        "- All target note contents and gate definitions are included below. Do not read them from disk.",
        "- For semantic grounding or consistency checks, follow only links that appear in a target note.",
        "- When following a markdown link from a target note, use that note's pre-resolved path table below instead of searching for targets by name.",
        "- Ignore review backups, workshop copies, and historical artifacts unless a target note links to them explicitly.",
    ]
    if len(notes) > 1:
        lines.append(
            "- Evaluate each note independently. Do not compare notes against each other or use one note to calibrate another."
        )

    lines.extend(
        [
            "",
            "Output contract for this run:",
            *destination_lines,
            "- Use exactly one block per requested (note, gate) pair.",
            "- Use these exact sentinels for every block:",
            "  === PAIR REVIEW START: <note-path> :: <gate-id> ===",
            "  === PAIR REVIEW END: <note-path> :: <gate-id> ===",
            DECISION_LINE_INSTRUCTION,
            "- Make the decision line the last non-empty line inside each block.",
            "- End output after the final block.",
            "",
            "Requested pairs for this run:",
        ]
    )
    for note in notes:
        for gate_id in note.gate_ids:
            lines.append(f"- {note.note_path} :: {gate_id} (review run id: {note.review_run_id})")

    lines.extend(
        [
            "",
            "Pre-resolved markdown links by target note:",
        ]
    )
    for note in notes:
        lines.extend(
            [
                "",
                f"### {note.note_path}",
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
    for note in notes:
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
            "Requested gate definitions (authoritative for this run):",
        ]
    )
    for gate_id in gate_ids:
        lines.extend(
            [
                f"=== gate: {gate_id} ===",
                gate_texts[gate_id].rstrip(),
                "",
            ]
        )

    lines.extend(
        [
            "",
            "Output template:",
        ]
    )
    for note in notes:
        for gate_id in note.gate_ids:
            lines.extend(
                [
                    PAIR_START_TEMPLATE.format(note_path=note.note_path, gate_id=gate_id),
                    "### Summary",
                    "<short paragraph>",
                    "",
                    "### Findings",
                    "- <severity>: <finding>",
                    "",
                    "### Suggested Revision",
                    "<optional; omit if not needed>",
                    "",
                    RESULT_LINE_TEMPLATE,
                    PAIR_END_TEMPLATE.format(note_path=note.note_path, gate_id=gate_id),
                    "",
                ]
            )

    return "\n".join(lines)
