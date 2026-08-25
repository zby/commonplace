"""Parse and canonicalize review protocol output.

Output blocks are keyed by (note_path, criterion_path). Structural anomalies —
nested or mismatched sentinels, unexpected or duplicate pairs, empty bodies —
raise, because the rest of the stream cannot be trusted. Missing expected
pairs are reported on the parsed bundle; live finalization treats them as a
whole-job failure.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass

from commonplace.review.protocol.format import (
    PAIR_END_RE,
    PAIR_START_RE,
    REVIEW_CONSUMPTION_FIELD,
    REVIEW_CONSUMPTION_OPENED_PATHS_KEY,
    REVIEW_CONSUMPTION_STOP_REASON_KEY,
    REVIEW_CONSUMPTION_STOP_REASONS,
    SELF_REPORTED_MODEL_FIELD,
)
from commonplace.review.protocol.outcomes import (
    canonicalize_report_completion,
    parse_review_outcome,
    rewrite_review_result_footer,
)

PairKey = tuple[str, str]


@dataclass(frozen=True)
class ParsedPairResult:
    note_path: str
    criterion_path: str
    outcome: str | None
    result_kind: str


@dataclass(frozen=True)
class ParsedReviewConsumption:
    report_status: str
    opened_paths: tuple[str, ...] | None
    stop_reason: str | None
    missing_fields: tuple[str, ...]
    malformed_fields: tuple[str, ...]


@dataclass(frozen=True)
class ParsedJobOutput:
    reviews: dict[PairKey, ParsedPairResult]
    canonical_texts: dict[PairKey, str]
    missing: list[PairKey]
    self_reported_model: str | None
    review_consumption: dict[PairKey, ParsedReviewConsumption]


def _parse_self_reported_model(job_output_markdown: str) -> str | None:
    """Parse the optional reviewer claim from the pre-pair preamble."""
    prefix = f"{SELF_REPORTED_MODEL_FIELD}:"
    values: list[str] = []
    for raw_line in job_output_markdown.splitlines():
        line = raw_line.strip()
        if PAIR_START_RE.match(line) is not None:
            break
        if not line.startswith(prefix):
            continue
        value = line.removeprefix(prefix).strip()
        if not value:
            raise ValueError(f"{SELF_REPORTED_MODEL_FIELD} must not be empty")
        values.append(value)

    if len(values) > 1:
        raise ValueError(f"duplicate {SELF_REPORTED_MODEL_FIELD} field")
    return values[0] if values else None


def _ordered_unique(values: Sequence[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def _without_review_consumption(
    review_text: str,
) -> tuple[str, ParsedReviewConsumption]:
    """Extract soft measurement metadata without changing result validity."""
    prefix = f"{REVIEW_CONSUMPTION_FIELD}:"
    report_values: list[str] = []
    review_lines: list[str] = []
    for raw_line in review_text.splitlines():
        line = raw_line.strip()
        if line.startswith(prefix):
            report_values.append(line.removeprefix(prefix).strip())
        else:
            review_lines.append(raw_line)

    cleaned_text = "\n".join(review_lines).strip() + "\n"
    field_names = (
        REVIEW_CONSUMPTION_OPENED_PATHS_KEY,
        REVIEW_CONSUMPTION_STOP_REASON_KEY,
    )
    if not report_values:
        return cleaned_text, ParsedReviewConsumption(
            report_status="missing",
            opened_paths=None,
            stop_reason=None,
            missing_fields=field_names,
            malformed_fields=(),
        )

    missing_fields: list[str] = []
    malformed_fields: list[str] = []
    opened_paths: tuple[str, ...] | None = None
    stop_reason: str | None = None

    if len(report_values) > 1:
        malformed_fields.append(REVIEW_CONSUMPTION_FIELD)

    try:
        report = json.loads(report_values[0])
    except (json.JSONDecodeError, TypeError):
        report = None
        malformed_fields.append(REVIEW_CONSUMPTION_FIELD)

    if not isinstance(report, dict):
        if REVIEW_CONSUMPTION_FIELD not in malformed_fields:
            malformed_fields.append(REVIEW_CONSUMPTION_FIELD)
        missing_fields.extend(field_names)
    else:
        unknown_fields = sorted(set(report) - set(field_names))
        malformed_fields.extend(f"unknown:{field}" for field in unknown_fields)

        if REVIEW_CONSUMPTION_OPENED_PATHS_KEY not in report:
            missing_fields.append(REVIEW_CONSUMPTION_OPENED_PATHS_KEY)
        else:
            raw_paths = report[REVIEW_CONSUMPTION_OPENED_PATHS_KEY]
            if not isinstance(raw_paths, list):
                malformed_fields.append(REVIEW_CONSUMPTION_OPENED_PATHS_KEY)
            else:
                valid_paths: list[str] = []
                invalid_path = False
                for raw_path in raw_paths:
                    if not isinstance(raw_path, str) or not raw_path.strip():
                        invalid_path = True
                        continue
                    valid_paths.append(raw_path.strip())
                if invalid_path:
                    malformed_fields.append(REVIEW_CONSUMPTION_OPENED_PATHS_KEY)
                opened_paths = _ordered_unique(valid_paths)

        if REVIEW_CONSUMPTION_STOP_REASON_KEY not in report:
            missing_fields.append(REVIEW_CONSUMPTION_STOP_REASON_KEY)
        else:
            raw_stop_reason = report[REVIEW_CONSUMPTION_STOP_REASON_KEY]
            if not isinstance(raw_stop_reason, str):
                malformed_fields.append(REVIEW_CONSUMPTION_STOP_REASON_KEY)
            else:
                candidate = raw_stop_reason.strip()
                if candidate not in REVIEW_CONSUMPTION_STOP_REASONS:
                    malformed_fields.append(REVIEW_CONSUMPTION_STOP_REASON_KEY)
                else:
                    stop_reason = candidate

    missing = _ordered_unique(missing_fields)
    malformed = _ordered_unique(malformed_fields)
    if malformed:
        report_status = "malformed"
    elif missing:
        report_status = "partial"
    else:
        report_status = "complete"
    return cleaned_text, ParsedReviewConsumption(
        report_status=report_status,
        opened_paths=opened_paths,
        stop_reason=stop_reason,
        missing_fields=missing,
        malformed_fields=malformed,
    )


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
    self_reported_model = _parse_self_reported_model(job_output_markdown)
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
    review_consumption: dict[PairKey, ParsedReviewConsumption] = {}
    for pair, review_text in extracted.items():
        review_text, consumption = _without_review_consumption(review_text)
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
        review_consumption[pair] = consumption

    missing = [pair for pair in expected_pairs if pair not in extracted]
    return ParsedJobOutput(
        reviews=reviews,
        canonical_texts=canonical_texts,
        missing=missing,
        self_reported_model=self_reported_model,
        review_consumption=review_consumption,
    )
