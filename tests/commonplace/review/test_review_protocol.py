from __future__ import annotations

import pytest

from commonplace.review.protocol.parser import extract_pair_results, parse_job_output
from commonplace.review.protocol.prompt import (
    NoteReviewTarget,
    ResolvedConsumptionTarget,
    ResolvedMarkdownLink,
    UnavailableMarkdownTarget,
    render_pairs_prompt,
)

GATE = "accessibility/undefined-terms"
GATE_TEXT = "## Check\n\nFlag terms that are used before they are defined."


def make_target(note_path: str, criterion_paths: tuple[str, ...] = (GATE,), **kwargs) -> NoteReviewTarget:
    return NoteReviewTarget(
        note_path=note_path,
        criterion_paths=criterion_paths,
        note_text=kwargs.pop("note_text", f"# Note\n\nBody of {note_path}."),
        **kwargs,
    )


def test_render_pairs_prompt_multi_note_shares_gate_and_lists_pairs() -> None:
    prompt = render_pairs_prompt(
        notes=[
            make_target(
                "kb/notes/first.md",
                note_text="# First note\n\nSome content about a [concept](./concept.md).",
                resolved_links=[
                    ResolvedMarkdownLink(
                        "concept",
                        "./concept.md",
                        "kb/notes/concept.md",
                        (ResolvedConsumptionTarget("kb/notes/concept.md", 1234),),
                    )
                ],
                unavailable_targets=[
                    UnavailableMarkdownTarget(
                        "missing",
                        "./missing.md",
                        "kb/notes/missing.md",
                        "missing file",
                    )
                ],
            ),
            make_target("kb/notes/second.md", note_text="# Second note\n\nAnother note with no links."),
        ],
        criterion_texts={GATE: GATE_TEXT},
        result_kind="verdict",
        job_output_path="job-output.md",
    )

    assert "Evaluate each note independently." in prompt
    assert "Do not read them from disk" in prompt
    assert "one exact local path that an active criterion explicitly tells you to derive" in prompt
    assert f"- kb/notes/first.md :: {GATE}" in prompt
    assert f"- kb/notes/second.md :: {GATE}" in prompt
    assert "review job id" not in prompt
    assert (
        "Available cost: 1 resolved link(s), 1 distinct link target(s), "
        "1 consumption target(s), 1234 bytes total."
    ) in prompt
    assert (
        "| [concept](./concept.md) | `kb/notes/concept.md` | "
        "`kb/notes/concept.md` | 1234 bytes |"
    ) in prompt
    assert "- [missing](./missing.md) -> `kb/notes/missing.md` (missing file)" in prompt
    # Note contents are frontloaded
    assert "=== note: kb/notes/first.md ===" in prompt
    assert "Some content about a [concept](./concept.md)." in prompt
    assert "=== note: kb/notes/second.md ===" in prompt
    # Shared gate text appears exactly once
    assert prompt.count(f"=== criterion: {GATE} ===") == 1
    # One template block per pair
    assert prompt.count(f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE} ===") == 1
    assert prompt.count(f"=== PAIR REVIEW START: kb/notes/second.md :: {GATE} ===") == 1


def test_render_pairs_prompt_single_note_shares_note_across_gates() -> None:
    prompt = render_pairs_prompt(
        notes=[make_target("kb/notes/only.md", criterion_paths=("lens/alpha", "lens/beta"))],
        criterion_texts={"lens/alpha": "Alpha gate.", "lens/beta": "Beta gate."},
        result_kind="verdict",
        job_output_path="job-output.md",
    )

    assert "Evaluate each note independently." not in prompt
    assert prompt.count("=== note: kb/notes/only.md ===") == 1
    assert "=== PAIR REVIEW START: kb/notes/only.md :: lens/alpha ===" in prompt
    assert "=== PAIR REVIEW START: kb/notes/only.md :: lens/beta ===" in prompt


def bundle_two_pairs() -> str:
    return f"""# Review output

=== PAIR REVIEW START: kb/notes/first.md :: {GATE} ===
Needs one definition.

## Result: WARN
=== PAIR REVIEW END: kb/notes/first.md :: {GATE} ===

=== PAIR REVIEW START: kb/notes/second.md :: {GATE} ===
No undefined terms found.

## Result: PASS
=== PAIR REVIEW END: kb/notes/second.md :: {GATE} ===
"""


def test_extract_pair_results_rejects_unexpected_pair() -> None:
    with pytest.raises(ValueError, match="unexpected pair"):
        extract_pair_results(bundle_two_pairs(), expected_pairs=[("kb/notes/first.md", GATE)])


def test_extract_pair_results_rejects_duplicate_pair() -> None:
    bundle = bundle_two_pairs().replace("kb/notes/second.md", "kb/notes/first.md")
    with pytest.raises(ValueError, match="duplicate pair"):
        extract_pair_results(bundle, expected_pairs=[("kb/notes/first.md", GATE)])


def test_extract_pair_results_rejects_unterminated_block() -> None:
    bundle = f"=== PAIR REVIEW START: kb/notes/first.md :: {GATE} ===\nNo end sentinel.\n"
    with pytest.raises(ValueError, match="unterminated pair review block"):
        extract_pair_results(bundle, expected_pairs=[("kb/notes/first.md", GATE)])


def test_parse_job_output_parses_outcomes_and_reports_missing() -> None:
    parsed = parse_job_output(
        bundle_two_pairs(),
        expected_pairs=[
            ("kb/notes/first.md", GATE),
            ("kb/notes/second.md", GATE),
            ("kb/notes/third.md", GATE),
        ],
        result_kinds={
            ("kb/notes/first.md", GATE): "verdict",
            ("kb/notes/second.md", GATE): "verdict",
            ("kb/notes/third.md", GATE): "verdict",
        },
    )
    assert parsed.reviews[("kb/notes/first.md", GATE)].outcome == "warn"
    assert parsed.reviews[("kb/notes/second.md", GATE)].outcome == "pass"
    assert parsed.missing == [("kb/notes/third.md", GATE)]
    assert parsed.self_reported_model is None
    assert parsed.review_consumption[("kb/notes/first.md", GATE)].report_status == "missing"
    assert parsed.review_consumption[("kb/notes/second.md", GATE)].report_status == "missing"


@pytest.mark.parametrize(
    ("report_line", "status", "opened_paths", "stop_reason"),
    [
        (
            'review-consumption: {"opened_paths": ["kb/notes/shared.md"]}',
            "partial",
            ("kb/notes/shared.md",),
            None,
        ),
        ("review-consumption: {not json}", "malformed", None, None),
        (
            'review-consumption: {"opened_paths": ["kb/notes/shared.md", 7], "stop_reason": "finished"}',
            "malformed",
            ("kb/notes/shared.md",),
            None,
        ),
    ],
)
def test_parse_job_output_keeps_partial_or_malformed_consumption_soft(
    report_line: str,
    status: str,
    opened_paths: tuple[str, ...] | None,
    stop_reason: str | None,
) -> None:
    pair = ("kb/notes/first.md", GATE)
    bundle = f"""=== PAIR REVIEW START: {pair[0]} :: {pair[1]} ===
Looks good.

{report_line}

## Result: PASS
=== PAIR REVIEW END: {pair[0]} :: {pair[1]} ===
"""

    parsed = parse_job_output(
        bundle,
        expected_pairs=[pair],
        result_kinds={pair: "verdict"},
    )

    report = parsed.review_consumption[pair]
    assert report.report_status == status
    assert report.opened_paths == opened_paths
    assert report.stop_reason == stop_reason
    assert parsed.reviews[pair].outcome == "pass"
    assert "review-consumption" not in parsed.canonical_texts[pair]


@pytest.mark.parametrize(
    ("preamble", "message"),
    [
        ("self-reported-model:\n", "self-reported-model must not be empty"),
        (
            "self-reported-model: first\nself-reported-model: second\n",
            "duplicate self-reported-model field",
        ),
    ],
)
def test_parse_job_output_rejects_malformed_self_reported_model(
    preamble: str,
    message: str,
) -> None:
    bundle = preamble + bundle_two_pairs()
    pairs = [("kb/notes/first.md", GATE), ("kb/notes/second.md", GATE)]

    with pytest.raises(ValueError, match=message):
        parse_job_output(
            bundle,
            expected_pairs=pairs,
            result_kinds={pair: "verdict" for pair in pairs},
        )
