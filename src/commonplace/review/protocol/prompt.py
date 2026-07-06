"""Render review protocol prompts.

One renderer for every packing shape: the prompt carries N note targets and
M gate definitions and requests one output block per requested (note, gate)
pair. Notes and catalog gates are embedded once; a type spec serving as a
gate is referenced by repo path instead, and the worker reads it from disk —
the spec is authoring instructions the reviewer applies as criteria, not
prompt text addressed to it, and the read keeps that distinction evident.

The referenced type spec is still snapshotted at job creation and pinned by
acceptance, so freshness is unchanged. The disk read opens a window: a type
spec edited between job creation and the worker's read is judged in its new
text while acceptance pins the creation-time snapshot. A persistent edit
self-heals — the acceptance is immediately stale (`gate-changed`) against the
changed file — so only an edit reverted within the window escapes notice.

Freshness boundary: review acceptance hashes only the embedded note and gate
texts. Everything this module renders around them — the runner system prompt,
reading scope, output contract, templates, the type-conformance wrapper — is
outside the freshness hash, so editing it does NOT invalidate accepted
reviews. Keep this layer mechanical (how to read inputs and emit a verdict);
judgment-bearing review criteria must live in gate files, where the hash sees
them. In particular the type-conformance wrapper may say how to apply a type
spec as a gate, never what a good note of the type looks like — conformance
criteria that need sharpening go into the type spec itself (an authored
`## Review` section), not into a richer wrapper. A scaffolding change that
shifts judgments is a system upgrade and needs a deliberate corpus-wide
re-review or ack decision.
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
from commonplace.review.type_conformance import is_type_spec_gate_path


OutputMode = Literal["stdout", "file"]


def _type_conformance_wrapper_lines(gate_path: str) -> tuple[str, ...]:
    """Gate block rendered for a type spec serving as a gate.

    Mechanical only: it says how to apply authoring instructions as a gate,
    never what a good note of the type looks like — those criteria belong in
    the type spec, where the freshness hash sees them. The spec itself is not
    embedded; the worker reads it from the referenced repo path.
    """
    return (
        "This is a type-conformance gate. The gate is the note's type spec:",
        "authoring instructions and a template, not a Failure mode / Test procedure.",
        f"The type spec is not embedded in this prompt. Read `{gate_path}` (repo-relative)",
        "before judging; it is the authoritative gate text for this pair.",
        "Judge whether the note does what the type spec's authoring instructions ask.",
        "If the type spec carries a `## Review` section, treat it as the operative test.",
        "- PASS: the note does what the authoring instructions ask.",
        "- WARN: the note conforms overall, but specific instructions go unmet; name each unmet instruction as a finding.",
        "- FAIL: the note does not do what the authoring instructions ask.",
        "Structural checks (frontmatter fields, schema conformance) are the deterministic validator's job; do not re-check them here.",
    )


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
        if is_type_spec_gate_path(gate_path):
            # Referenced by path, not embedded: no text to require or scan.
            continue
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
    has_type_spec_gate = any(is_type_spec_gate_path(gate_path) for gate_path in gate_paths)

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
    ]
    if has_type_spec_gate:
        lines.append(
            "- Exception: type-conformance gates reference the note's type spec instead of embedding it; read each referenced type spec from disk as its gate block directs."
        )
    lines += [
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
        lines.append(f"=== gate: {gate_path} ===")
        if is_type_spec_gate_path(gate_path):
            lines.extend(_type_conformance_wrapper_lines(gate_path))
            lines.append("")
        else:
            lines.extend(
                [
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
