"""Render review protocol prompts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

from commonplace.review.protocol.format import (
    DECISION_LINE_INSTRUCTION,
    GATE_REVIEW_END_TEMPLATE,
    GATE_REVIEW_START_TEMPLATE,
    GATE_SWEEP_DECISION_LINE_INSTRUCTION,
    NOTE_END_TEMPLATE,
    NOTE_START_TEMPLATE,
    RESULT_LINE_TEMPLATE,
)


OutputMode = Literal["stdout", "file"]


@dataclass(frozen=True)
class GateSweepNoteTarget:
    note_path: str
    review_run_id: int
    note_text: str = ""
    resolved_links: Sequence[tuple[str, str, str]] = ()
    unresolved_links: Sequence[tuple[str, str]] = ()


def render_bundle_prompt(
    *,
    note_path: str,
    gate_ids: Sequence[str],
    gate_texts: dict[str, str],
    resolved_links: Sequence[tuple[str, str, str]],
    unresolved_links: Sequence[tuple[str, str]],
    review_run_id: int,
    output_mode: OutputMode = "stdout",
    bundle_output_path: str | None = None,
) -> str:
    gates = " ".join(gate_ids)
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
        f"Write gate reviews for {note_path} for gates: {gates}",
        "",
        "Reading scope for this run:",
        "- Read the target note in full.",
        "- The requested gate definitions are included below. Do not read them from disk.",
        "- For semantic grounding or consistency checks, follow only links that appear in the target note.",
        "- When following a markdown link from the target note, use the pre-resolved path table below instead of searching for targets by name.",
        "- Ignore review backups, workshop copies, and historical artifacts unless the target note links to them explicitly.",
        "",
        "Output contract for this run:",
        *destination_lines,
        "- Use exactly one block per requested gate.",
        "- Use these exact sentinels for every block:",
        "  === GATE REVIEW START: <gate-id> ===",
        "  === GATE REVIEW END: <gate-id> ===",
        DECISION_LINE_INSTRUCTION,
        "- Make the decision line the last non-empty line inside each gate block.",
        "- End output after the final gate block.",
        "",
        f"Review run id: {review_run_id}",
    ]

    lines.append("")
    lines.append("Pre-resolved markdown links from the target note:")
    if resolved_links:
        for link_text, raw_target, repo_rel in resolved_links:
            lines.append(f"- [{link_text}]({raw_target}) -> {repo_rel}")
    else:
        lines.append("- none")

    if unresolved_links:
        lines.append("")
        lines.append("Unresolved markdown links in the target note:")
        lines.append("- Treat these as broken links if they become relevant; do not search for alternate targets.")
        for link_text, raw_target in unresolved_links:
            lines.append(f"- [{link_text}]({raw_target})")

    lines.extend(
        [
            "",
            "Bundle template:",
            "# Review Bundle",
            "",
            f"Review run id: {review_run_id}",
            f"Target: {note_path}",
            "",
        ]
    )
    for gate_id in gate_ids:
        lines.extend(
            [
                GATE_REVIEW_START_TEMPLATE.format(gate_id=gate_id),
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
                GATE_REVIEW_END_TEMPLATE.format(gate_id=gate_id),
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
        lines.append(f"=== gate: {gate_id} ===")
        lines.append(gate_texts[gate_id].rstrip())
        lines.append("")

    return "\n".join(lines)


def _normalize_gate_sweep_targets(notes: Sequence[GateSweepNoteTarget]) -> list[GateSweepNoteTarget]:
    from commonplace.review.protocol.format import RESERVED_SENTINEL_RE

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
        for lineno, line in enumerate(note.note_text.splitlines(), start=1):
            if RESERVED_SENTINEL_RE.match(line.strip()):
                raise ValueError(
                    f"reserved sentinel in {note_path} line {lineno}: {line.strip()!r}"
                )
        seen.add(note_path)
    return normalized


def render_sweep_prompt(
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

    normalized_notes = _normalize_gate_sweep_targets(notes)
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
        GATE_SWEEP_DECISION_LINE_INSTRUCTION,
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
                NOTE_START_TEMPLATE.format(note_path=note.note_path),
                GATE_REVIEW_START_TEMPLATE.format(gate_id=gate_id),
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
                GATE_REVIEW_END_TEMPLATE.format(gate_id=gate_id),
                NOTE_END_TEMPLATE.format(note_path=note.note_path),
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
