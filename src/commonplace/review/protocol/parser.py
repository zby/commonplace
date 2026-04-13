"""Parse and canonicalize review protocol output."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from commonplace.review.protocol.decisions import parse_review_decision, rewrite_review_result_footer
from commonplace.review.protocol.format import BUNDLE_END_RE, BUNDLE_START_RE, NOTE_END_RE, NOTE_START_RE


@dataclass(frozen=True)
class ParsedGateReview:
    gate_id: str
    decision: str
    rationale_markdown: str


def extract_bundle_reviews(
    bundle_markdown: str,
    *,
    expected_gate_ids: Sequence[str],
) -> dict[str, str]:
    expected = set(expected_gate_ids)
    reviews: dict[str, str] = {}
    current_gate_id: str | None = None
    current_lines: list[str] = []

    for raw_line in bundle_markdown.splitlines():
        start_match = BUNDLE_START_RE.match(raw_line.strip())
        if start_match is not None:
            if current_gate_id is not None:
                raise ValueError(f"nested gate review start before closing {current_gate_id}")
            gate_id = start_match.group("gate_id")
            if gate_id not in expected:
                raise ValueError(f"unexpected gate in bundle output: {gate_id}")
            if gate_id in reviews:
                raise ValueError(f"duplicate gate in bundle output: {gate_id}")
            current_gate_id = gate_id
            current_lines = []
            continue

        end_match = BUNDLE_END_RE.match(raw_line.strip())
        if end_match is not None:
            gate_id = end_match.group("gate_id")
            if current_gate_id is None:
                raise ValueError(f"gate review end without start: {gate_id}")
            if gate_id != current_gate_id:
                raise ValueError(f"gate review end mismatch: expected {current_gate_id}, found {gate_id}")
            review_text = "\n".join(current_lines).strip()
            if not review_text:
                raise ValueError(f"empty review body for gate: {gate_id}")
            reviews[gate_id] = review_text + "\n"
            current_gate_id = None
            current_lines = []
            continue

        if current_gate_id is not None:
            current_lines.append(raw_line)

    if current_gate_id is not None:
        raise ValueError(f"unterminated gate review block: {current_gate_id}")

    missing = [gate_id for gate_id in expected_gate_ids if gate_id not in reviews]
    if missing:
        raise ValueError(f"missing gate reviews in bundle output: {', '.join(missing)}")

    return reviews


def rewrite_bundle_result_footers(
    bundle_markdown: str,
    *,
    parsed_reviews: dict[str, str],
) -> str:
    rewritten_lines: list[str] = []
    current_gate_id: str | None = None

    for raw_line in bundle_markdown.splitlines():
        start_match = BUNDLE_START_RE.match(raw_line.strip())
        if start_match is not None:
            current_gate_id = start_match.group("gate_id")
            rewritten_lines.append(raw_line)
            continue

        end_match = BUNDLE_END_RE.match(raw_line.strip())
        if end_match is not None:
            gate_id = end_match.group("gate_id")
            if current_gate_id == gate_id and gate_id in parsed_reviews:
                rewritten_lines.extend(parsed_reviews[gate_id].rstrip("\n").splitlines())
            rewritten_lines.append(raw_line)
            current_gate_id = None
            continue

        if current_gate_id is None:
            rewritten_lines.append(raw_line)

    rewritten = "\n".join(rewritten_lines)
    if bundle_markdown.endswith("\n"):
        return rewritten + "\n"
    return rewritten


def parse_bundle_output(
    bundle_markdown: str,
    *,
    expected_gate_ids: Sequence[str],
) -> tuple[str, dict[str, ParsedGateReview], dict[str, str]]:
    parsed_reviews = extract_bundle_reviews(bundle_markdown, expected_gate_ids=expected_gate_ids)
    canonical_reviews: dict[str, str] = {}
    gate_reviews: dict[str, ParsedGateReview] = {}
    for gate_id in expected_gate_ids:
        review_text = parsed_reviews[gate_id]
        decision = parse_review_decision(review_text)
        canonical_review_text = rewrite_review_result_footer(review_text, decision=decision)
        canonical_reviews[gate_id] = canonical_review_text
        gate_reviews[gate_id] = ParsedGateReview(
            gate_id=gate_id,
            decision=decision,
            rationale_markdown=canonical_review_text,
        )

    canonical_bundle_markdown = rewrite_bundle_result_footers(
        bundle_markdown,
        parsed_reviews=canonical_reviews,
    )
    return canonical_bundle_markdown, gate_reviews, canonical_reviews


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
