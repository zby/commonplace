"""Parse and canonicalize review protocol output.

Output blocks are keyed by (note_path, criterion_path). Structural anomalies —
nested or mismatched sentinels, unexpected or duplicate pairs, empty bodies —
raise, because the rest of the stream cannot be trusted. Missing expected
pairs are reported on the parsed bundle; live finalization treats them as a
whole-job failure.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from commonplace.review.protocol.outcomes import (
    canonicalize_report_completion,
    parse_review_outcome,
    rewrite_review_result_footer,
)
from commonplace.review.protocol.format import PAIR_END_RE, PAIR_START_RE


PairKey = tuple[str, str]


@dataclass(frozen=True)
class ParsedPairResult:
    note_path: str
    criterion_path: str
    outcome: str | None
    result_kind: str


@dataclass(frozen=True)
class ParsedJobOutput:
    reviews: dict[PairKey, ParsedPairResult]
    canonical_texts: dict[PairKey, str]
    missing: list[PairKey]


def extract_pair_results(
    job_output_markdown: str,
    *,
    expected_pairs: Sequence[PairKey],
) -> dict[PairKey, str]:
    expected = set(expected_pairs)
    reviews: dict[PairKey, str] = {}
    current_pair: PairKey | None = None
    current_lines: list[str] = []

    for raw_line in job_output_markdown.splitlines():
        start_match = PAIR_START_RE.match(raw_line.strip())
        if start_match is not None:
            if current_pair is not None:
                raise ValueError(f"nested pair review start before closing {current_pair[0]} :: {current_pair[1]}")
            pair = (start_match.group("note_path"), start_match.group("criterion_path"))
            if pair not in expected:
                raise ValueError(f"unexpected pair in review output: {pair[0]} :: {pair[1]}")
            if pair in reviews:
                raise ValueError(f"duplicate pair in review output: {pair[0]} :: {pair[1]}")
            current_pair = pair
            current_lines = []
            continue

        end_match = PAIR_END_RE.match(raw_line.strip())
        if end_match is not None:
            pair = (end_match.group("note_path"), end_match.group("criterion_path"))
            if current_pair is None:
                raise ValueError(f"pair review end without start: {pair[0]} :: {pair[1]}")
            if pair != current_pair:
                raise ValueError(
                    f"pair review end mismatch: expected {current_pair[0]} :: {current_pair[1]}, "
                    f"found {pair[0]} :: {pair[1]}"
                )
            review_text = "\n".join(current_lines).strip()
            if not review_text:
                raise ValueError(f"empty review body for pair: {pair[0]} :: {pair[1]}")
            reviews[pair] = review_text + "\n"
            current_pair = None
            current_lines = []
            continue

        if current_pair is not None:
            current_lines.append(raw_line)

    if current_pair is not None:
        raise ValueError(f"unterminated pair review block: {current_pair[0]} :: {current_pair[1]}")

    return reviews


def parse_job_output(
    job_output_markdown: str,
    *,
    expected_pairs: Sequence[PairKey],
    result_kinds: dict[PairKey, str],
) -> ParsedJobOutput:
    expected = set(expected_pairs)
    contracted = set(result_kinds)
    if contracted != expected:
        details: list[str] = []
        missing = expected - contracted
        unexpected = contracted - expected
        if missing:
            details.append(
                "missing " + ", ".join(f"{note} :: {criterion}" for note, criterion in sorted(missing))
            )
        if unexpected:
            details.append(
                "unexpected "
                + ", ".join(f"{note} :: {criterion}" for note, criterion in sorted(unexpected))
            )
        raise ValueError(f"result-kind contract mismatch: {'; '.join(details)}")

    extracted = extract_pair_results(job_output_markdown, expected_pairs=expected_pairs)
    canonical_texts: dict[PairKey, str] = {}
    reviews: dict[PairKey, ParsedPairResult] = {}
    for pair, review_text in extracted.items():
        result_kind = result_kinds[pair]
        if result_kind == "verdict":
            outcome = parse_review_outcome(review_text)
            canonical_text = rewrite_review_result_footer(review_text, outcome=outcome)
        elif result_kind == "report":
            outcome = None
            canonical_text = canonicalize_report_completion(review_text)
        else:
            raise ValueError(f"invalid result kind for pair: {pair[0]} :: {pair[1]}: {result_kind}")
        canonical_texts[pair] = canonical_text
        reviews[pair] = ParsedPairResult(
            note_path=pair[0],
            criterion_path=pair[1],
            outcome=outcome,
            result_kind=result_kind,
        )

    missing = [pair for pair in expected_pairs if pair not in extracted]
    return ParsedJobOutput(
        reviews=reviews,
        canonical_texts=canonical_texts,
        missing=missing,
    )
