"""Parse and canonicalize review protocol output.

Output blocks are keyed by (note_path, gate_id). Structural anomalies —
nested or mismatched sentinels, unexpected or duplicate pairs, empty bodies —
raise, because the rest of the stream cannot be trusted. Missing expected
pairs do not raise: callers salvage the pairs that parsed and decide what to
do about the rest.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from commonplace.review.protocol.decisions import parse_review_decision, rewrite_review_result_footer
from commonplace.review.protocol.format import PAIR_END_RE, PAIR_START_RE


PairKey = tuple[str, str]


@dataclass(frozen=True)
class ParsedPairReview:
    note_path: str
    gate_id: str
    decision: str
    rationale_markdown: str


@dataclass(frozen=True)
class ParsedPairBundle:
    canonical_markdown: str
    reviews: dict[PairKey, ParsedPairReview]
    canonical_texts: dict[PairKey, str]
    missing: list[PairKey]


def extract_pair_reviews(
    bundle_markdown: str,
    *,
    expected_pairs: Sequence[PairKey],
) -> dict[PairKey, str]:
    expected = set(expected_pairs)
    reviews: dict[PairKey, str] = {}
    current_pair: PairKey | None = None
    current_lines: list[str] = []

    for raw_line in bundle_markdown.splitlines():
        start_match = PAIR_START_RE.match(raw_line.strip())
        if start_match is not None:
            if current_pair is not None:
                raise ValueError(f"nested pair review start before closing {current_pair[0]} :: {current_pair[1]}")
            pair = (start_match.group("note_path"), start_match.group("gate_id"))
            if pair not in expected:
                raise ValueError(f"unexpected pair in review output: {pair[0]} :: {pair[1]}")
            if pair in reviews:
                raise ValueError(f"duplicate pair in review output: {pair[0]} :: {pair[1]}")
            current_pair = pair
            current_lines = []
            continue

        end_match = PAIR_END_RE.match(raw_line.strip())
        if end_match is not None:
            pair = (end_match.group("note_path"), end_match.group("gate_id"))
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


def rewrite_pair_result_footers(
    bundle_markdown: str,
    *,
    canonical_texts: dict[PairKey, str],
) -> str:
    rewritten_lines: list[str] = []
    current_pair: PairKey | None = None

    for raw_line in bundle_markdown.splitlines():
        start_match = PAIR_START_RE.match(raw_line.strip())
        if start_match is not None:
            current_pair = (start_match.group("note_path"), start_match.group("gate_id"))
            rewritten_lines.append(raw_line)
            continue

        end_match = PAIR_END_RE.match(raw_line.strip())
        if end_match is not None:
            pair = (end_match.group("note_path"), end_match.group("gate_id"))
            if current_pair == pair and pair in canonical_texts:
                rewritten_lines.extend(canonical_texts[pair].rstrip("\n").splitlines())
            rewritten_lines.append(raw_line)
            current_pair = None
            continue

        if current_pair is None:
            rewritten_lines.append(raw_line)

    rewritten = "\n".join(rewritten_lines)
    if bundle_markdown.endswith("\n"):
        return rewritten + "\n"
    return rewritten


def parse_pair_bundle(
    bundle_markdown: str,
    *,
    expected_pairs: Sequence[PairKey],
) -> ParsedPairBundle:
    extracted = extract_pair_reviews(bundle_markdown, expected_pairs=expected_pairs)
    canonical_texts: dict[PairKey, str] = {}
    reviews: dict[PairKey, ParsedPairReview] = {}
    for pair, review_text in extracted.items():
        decision = parse_review_decision(review_text)
        canonical_text = rewrite_review_result_footer(review_text, decision=decision)
        canonical_texts[pair] = canonical_text
        reviews[pair] = ParsedPairReview(
            note_path=pair[0],
            gate_id=pair[1],
            decision=decision,
            rationale_markdown=canonical_text,
        )

    canonical_markdown = rewrite_pair_result_footers(bundle_markdown, canonical_texts=canonical_texts)
    missing = [pair for pair in expected_pairs if pair not in extracted]
    return ParsedPairBundle(
        canonical_markdown=canonical_markdown,
        reviews=reviews,
        canonical_texts=canonical_texts,
        missing=missing,
    )
