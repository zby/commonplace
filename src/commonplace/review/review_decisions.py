"""Compatibility wrapper for review protocol decision parsing."""

from __future__ import annotations

from commonplace.review.protocol.decisions import (
    DECISION_VALUES,
    infer_manual_import_review_decision,
    normalize_review_decision,
    parse_review_decision,
    rewrite_review_result_footer,
    strip_explicit_review_result_lines,
    strip_legacy_frontmatter_block,
    strip_relaxed_review_result_lines,
    strip_review_metadata_block,
)


__all__ = [
    "DECISION_VALUES",
    "infer_manual_import_review_decision",
    "normalize_review_decision",
    "parse_review_decision",
    "rewrite_review_result_footer",
    "strip_explicit_review_result_lines",
    "strip_legacy_frontmatter_block",
    "strip_relaxed_review_result_lines",
    "strip_review_metadata_block",
]
