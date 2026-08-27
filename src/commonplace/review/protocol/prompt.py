"""Render review protocol prompts.

One renderer for every grouping shape: the prompt carries N note targets and
M assay criteria and requests one output block per persisted (note, criterion_path)
pair. Notes and criteria are embedded once from the snapshots captured at job
creation. Conformance criteria retain a short mechanical wrapper explaining
how to apply the embedded type spec or COLLECTION.md contract.

Freshness boundary: the freshness baseline hashes only the note and criterion
texts. Everything this module renders around them — the reading scope, output
contract, templates, and conformance wrappers — remains outside the freshness
hash, so editing it does NOT invalidate baseline
assays. Keep this layer mechanical (how to read inputs and emit a result);
judgment-bearing criteria must live in criterion files, where the hash sees
them. In particular a conformance wrapper may say how to apply a type spec or
COLLECTION.md as a gate, never what a good note of the type or collection
looks like — conformance criteria that need sharpening go into the dependency
document itself (an authored `## Review` section), not into a richer wrapper.
A scaffolding change that shifts judgments is a system upgrade and needs a
deliberate corpus-wide re-review or ack outcome.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from commonplace.review.collection_conformance import is_collection_md_criterion_path
from commonplace.review.protocol.format import (
    OUTCOME_LINE_INSTRUCTION,
    PAIR_END_TEMPLATE,
    PAIR_KEY_SEPARATOR,
    PAIR_START_TEMPLATE,
    REPORT_LINE_TEMPLATE,
    RESERVED_SENTINEL_RE,
    RESULT_LINE_TEMPLATE,
    REVIEW_CONSUMPTION_FIELD,
    SELF_REPORTED_MODEL_FIELD,
)
from commonplace.review.type_conformance import is_type_spec_criterion_path


def _type_conformance_wrapper_lines() -> tuple[str, ...]:
    """Gate block rendered for a type spec serving as a gate.

    Mechanical only: it says how to apply authoring instructions as a gate,
    never what a good note of the type looks like — those criteria belong in
    the type spec, where the freshness hash sees them.
    """
    return (
        "This is a type-conformance gate. The gate is the note's type spec:",
        "authoring instructions and a template, not a Failure mode / Test procedure.",
        "The embedded type spec below is the authoritative gate text for this pair.",
        "Judge whether the note does what the type spec's authoring instructions ask.",
        "If the type spec carries a `## Review` section, treat it as the operative test.",
        "- PASS: the note does what the authoring instructions ask.",
        "- WARN: the note conforms overall, but specific instructions go unmet; name each unmet instruction as a finding.",
        "- FAIL: the note does not do what the authoring instructions ask.",
        "Structural checks (frontmatter fields, schema conformance) are the deterministic validator's job; do not re-check them here.",
    )


def _collection_conformance_wrapper_lines() -> tuple[str, ...]:
    """Gate block rendered for a COLLECTION.md serving as a gate.

    Mechanical only: it says how to apply a collection contract as a gate,
    never what a good note of the collection looks like — those criteria
    belong in the COLLECTION.md, where the freshness hash sees them.
    """
    return (
        "This is a collection-conformance gate. The gate is the authoring contract",
        "(COLLECTION.md) of the collection the note lives in: conventions and routing",
        "rules, not a Failure mode / Test procedure.",
        "The embedded contract below is the authoritative gate text for this pair.",
        "Judge whether the note follows the collection's authoring conventions:",
        "placement, title and description conventions, quality goal, and outbound linking rules.",
        "If the COLLECTION.md carries a `## Review` section, treat it as the operative test.",
        "- PASS: the note follows the collection's conventions.",
        "- WARN: the note conforms overall, but specific conventions go unmet; name each unmet convention as a finding.",
        "- FAIL: the note does not follow the collection's conventions: wrong placement, or its conventions are systematically unmet.",
        "Structural checks (frontmatter fields, schema conformance) are the deterministic validator's job; do not re-check them here.",
        "The note's conformance to its type spec is the type-conformance pair's job; judge only what the collection contract asks beyond the type contract.",
    )


@dataclass(frozen=True)
class ResolvedMarkdownLink:
    link_text: str
    raw_target: str
    link_target_path: str
    consumption_path: str
    size_bytes: int


@dataclass(frozen=True)
class UnavailableMarkdownTarget:
    link_text: str
    raw_target: str
    target_path: str
    reason: str


@dataclass(frozen=True)
class NoteReviewTarget:
    note_path: str
    criterion_paths: tuple[str, ...]
    note_text: str
    resolved_links: Sequence[ResolvedMarkdownLink] = ()
    unavailable_targets: Sequence[UnavailableMarkdownTarget] = ()


def available_link_cost(note: NoteReviewTarget) -> tuple[int, int, int, int]:
    """Return occurrences, logical targets, consumption targets, and bytes."""
    link_target_paths: set[str] = set()
    sizes_by_path: dict[str, int] = {}
    for link in note.resolved_links:
        link_target_paths.add(link.link_target_path)
        sizes_by_path.setdefault(link.consumption_path, link.size_bytes)
    return (
        len(note.resolved_links),
        len(link_target_paths),
        len(sizes_by_path),
        sum(sizes_by_path.values()),
    )


def _markdown_table_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def _validate_embedded_text(label: str, text: str) -> None:
    for lineno, line in enumerate(text.splitlines(), start=1):
        if RESERVED_SENTINEL_RE.match(line.strip()):
            raise ValueError(f"reserved sentinel in {label} line {lineno}: {line.strip()!r}")


def _validate_targets(
    notes: Sequence[NoteReviewTarget],
    criterion_texts: dict[str, str],
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
        if not note.criterion_paths:
            raise ValueError(f"note has no requested criteria: {note_path}")
        if len(set(note.criterion_paths)) != len(note.criterion_paths):
            raise ValueError(f"duplicate criterion requested for note: {note_path}")
        if not note.note_text.strip():
            raise ValueError(f"note_text must not be empty: {note_path}")
        _validate_embedded_text(note_path, note.note_text)
        seen_notes.add(note_path)

    requested_criterion_paths = {criterion_path for note in notes for criterion_path in note.criterion_paths}
    for criterion_path in sorted(requested_criterion_paths):
        if PAIR_KEY_SEPARATOR in criterion_path:
            raise ValueError(f"criterion_path must not contain {PAIR_KEY_SEPARATOR!r}: {criterion_path}")
        criterion_text = criterion_texts.get(criterion_path)
        if criterion_text is None or not criterion_text.strip():
            raise ValueError(f"missing criterion text: {criterion_path}")
        _validate_embedded_text(f"criterion {criterion_path}", criterion_text)


def render_pairs_prompt(
    *,
    notes: Sequence[NoteReviewTarget],
    criterion_texts: dict[str, str],
    result_kind: str,
    job_output_path: str,
) -> str:
    _validate_targets(notes, criterion_texts)
    criterion_paths = sorted({criterion_path for note in notes for criterion_path in note.criterion_paths})
    destination_lines = [
        f"- Write exactly one markdown document to `{job_output_path}`.",
        "- Do not write or edit any other file.",
        "- Do not invoke review helper scripts while writing the job output.",
        (
            "- If your environment explicitly states your exact model ID, add exactly one top-level line "
            f"before the first pair block: `{SELF_REPORTED_MODEL_FIELD}: <model-id>`."
        ),
        "- The model line is optional. Omit it when the model ID is unavailable; do not guess or infer it.",
        (
            "- Inside every pair block, before the result line, include exactly one "
            f"`{REVIEW_CONSUMPTION_FIELD}:` JSON object with `opened_paths` and `stop_reason`."
        ),
        (
            "- `opened_paths` lists each distinct repo-relative consumption target you used from that "
            "target note's pre-resolved link table. Use `[]` if you used no linked artifact. "
            "Do not include the target note, criterion, or a lineage-only link target."
        ),
        (
            "- For a `(snapshot required)` route, report the derived snapshot shown in the "
            "Consumption target column, not its linked ingest in the Resolved link target column."
        ),
        (
            "- `stop_reason` is exactly `budget` if a reading limit prevented further inspection, "
            "or `sufficiency` if you had enough evidence. This bookkeeping never changes the result."
        ),
    ]

    if result_kind not in {"verdict", "report"}:
        raise ValueError(f"invalid result kind: {result_kind}")
    result_instruction = (
        OUTCOME_LINE_INSTRUCTION
        if result_kind == "verdict"
        else "- Inside each block, include exactly one completion line: `## Result: REPORT`. Do not emit PASS, WARN, FAIL, or ERROR."
    )
    result_template = RESULT_LINE_TEMPLATE if result_kind == "verdict" else REPORT_LINE_TEMPLATE
    task_line = (
        "Write verdicts for the requested (note, criterion) pairs listed below."
        if result_kind == "verdict"
        else "Write the requested report for each (note, criterion) pair listed below. Emit each critique as that pair's block."
    )

    lines = [
        task_line,
        "",
        "Reading scope for this job:",
        "- All target note contents and review criteria are included below. Do not read them from disk.",
    ]
    lines += [
        "- For semantic grounding or consistency checks, follow only links that appear in a target note, except for one exact local path that an active criterion explicitly tells you to derive from such a link.",
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
            "- Use exactly one block per requested (note, criterion) pair.",
            "- Use these exact sentinels for every block:",
            "  === PAIR REVIEW START: <note-path> :: <criterion-path> ===",
            "  === PAIR REVIEW END: <note-path> :: <criterion-path> ===",
            result_instruction,
            "- Make the result line the last non-empty line inside each block.",
            "- End output after the final block.",
            "",
            "Requested pairs for this job:",
        ]
    )
    for note in notes:
        for criterion_path in note.criterion_paths:
            lines.append(f"- {note.note_path} :: {criterion_path}")

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
            (
                resolved_link_count,
                distinct_link_target_count,
                distinct_consumption_target_count,
                total_bytes,
            ) = available_link_cost(note)
            lines.extend(
                [
                    (
                        f"Available cost: {resolved_link_count} resolved link(s), "
                        f"{distinct_link_target_count} distinct link target(s), "
                        f"{distinct_consumption_target_count} consumption target(s), "
                        f"{total_bytes} bytes total. "
                        "The total charges each consumption target once."
                    ),
                    "",
                    "| Link | Resolved link target | Consumption target | Whole-file size |",
                    "| --- | --- | --- | ---: |",
                ]
            )
            for link in note.resolved_links:
                link_text = _markdown_table_cell(link.link_text)
                raw_target = _markdown_table_cell(link.raw_target)
                link_target_path = _markdown_table_cell(link.link_target_path)
                consumption_path = _markdown_table_cell(link.consumption_path)
                lines.append(
                    f"| [{link_text}]({raw_target}) | `{link_target_path}` | "
                    f"`{consumption_path}` | {link.size_bytes} bytes |"
                )
        else:
            lines.append("- none")

        if note.unavailable_targets:
            lines.extend(
                [
                    "",
                    "Unavailable local targets:",
                    "- These targets are unavailable; do not search for substitutes.",
                ]
            )
            for target in note.unavailable_targets:
                lines.append(
                    f"- [{target.link_text}]({target.raw_target}) -> "
                    f"`{target.target_path}` ({target.reason})"
                )

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
            "Requested review criteria (authoritative for this job):",
        ]
    )
    for criterion_path in criterion_paths:
        lines.append(f"=== criterion: {criterion_path} ===")
        if is_type_spec_criterion_path(criterion_path):
            lines.extend(_type_conformance_wrapper_lines())
        elif is_collection_md_criterion_path(criterion_path):
            lines.extend(_collection_conformance_wrapper_lines())
        lines.extend([criterion_texts[criterion_path].rstrip(), ""])

    lines.extend(
        [
            "",
            "Output template:",
        ]
    )
    for note in notes:
        for criterion_path in note.criterion_paths:
            block = [PAIR_START_TEMPLATE.format(note_path=note.note_path, criterion_path=criterion_path)]
            if result_kind == "verdict":
                block.extend(
                    [
                        "### Summary",
                        "<short paragraph>",
                        "",
                        "### Findings",
                        "- <severity>: <finding>",
                        "",
                        "### Suggested Revision",
                        "<optional; omit if not needed>",
                    ]
                )
            else:
                block.append("<the complete report shape required by the assay criterion>")
            block.extend(
                [
                    "",
                    (
                        f'{REVIEW_CONSUMPTION_FIELD}: '
                        '{"opened_paths": [<JSON strings for each distinct opened path>], '
                        '"stop_reason": "<budget|sufficiency>"}'
                    ),
                    "",
                    result_template,
                    PAIR_END_TEMPLATE.format(note_path=note.note_path, criterion_path=criterion_path),
                    "",
                ]
            )
            lines.extend(block)

    return "\n".join(lines)
