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

# Used as the reviewer system prompt; the task prompt rendered below carries
# the per-job specifics.
REVIEW_RUNNER_SYSTEM_PROMPT = (
    "Your goal is to write a series of review artifacts for the requested gates. "
    "The task prompt provides the exact note, gate definitions, and output contract for the job. "
    "Stay within the target note, the provided gate definitions, and only the linked neighborhood that the active gates require. "
    "Do not do broad repository exploration or search for alternate gate definitions. "
    "Treat helper scripts as command interfaces; inspect workflow files or script source only if a command fails and you need to debug it."
)


@dataclass(frozen=True)
class NoteReviewTarget:
    note_path: str
    review_job_id: int
    gate_paths: tuple[str, ...]
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
        if not note.gate_paths:
            raise ValueError(f"note has no requested gates: {note_path}")
        if len(set(note.gate_paths)) != len(note.gate_paths):
            raise ValueError(f"duplicate gate requested for note: {note_path}")
        if not note.note_text.strip():
            raise ValueError(f"note_text must not be empty: {note_path}")
        _validate_embedded_text(note_path, note.note_text)
        seen_notes.add(note_path)

    requested_gate_paths = {gate_path for note in notes for gate_path in note.gate_paths}
    for gate_path in sorted(requested_gate_paths):
        if PAIR_KEY_SEPARATOR in gate_path:
            raise ValueError(f"gate_path must not contain {PAIR_KEY_SEPARATOR!r}: {gate_path}")
        gate_text = gate_texts.get(gate_path)
        if gate_text is None or not gate_text.strip():
            raise ValueError(f"missing gate text: {gate_path}")
        _validate_embedded_text(f"gate {gate_path}", gate_text)


def render_pairs_prompt(
    *,
    notes: Sequence[NoteReviewTarget],
    gate_texts: dict[str, str],
    output_mode: OutputMode = "stdout",
    bundle_output_path: str | None = None,
) -> str:
    _validate_targets(notes, gate_texts)
    gate_paths = sorted({gate_path for note in notes for gate_path in note.gate_paths})

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
        "Reading scope for this job:",
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
            "Output contract for this job:",
            *destination_lines,
            "- Use exactly one block per requested (note, gate) pair.",
            "- Use these exact sentinels for every block:",
            "  === PAIR REVIEW START: <note-path> :: <gate-path> ===",
            "  === PAIR REVIEW END: <note-path> :: <gate-path> ===",
            DECISION_LINE_INSTRUCTION,
            "- Make the decision line the last non-empty line inside each block.",
            "- End output after the final block.",
            "",
            "Requested pairs for this job:",
        ]
    )
    for note in notes:
        for gate_path in note.gate_paths:
            lines.append(f"- {note.note_path} :: {gate_path} (review job id: {note.review_job_id})")

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
            "Target note contents (authoritative for this job):",
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
            "Requested gate definitions (authoritative for this job):",
        ]
    )
    for gate_path in gate_paths:
        lines.extend(
            [
                f"=== gate: {gate_path} ===",
                gate_texts[gate_path].rstrip(),
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
        for gate_path in note.gate_paths:
            lines.extend(
                [
                    PAIR_START_TEMPLATE.format(note_path=note.note_path, gate_path=gate_path),
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
                    PAIR_END_TEMPLATE.format(note_path=note.note_path, gate_path=gate_path),
                    "",
                ]
            )

    return "\n".join(lines)
