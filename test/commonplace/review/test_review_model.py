from __future__ import annotations

from commonplace.review.review_model import build_model_partition, normalize_model_partition


def test_normalize_model_partition_collapses_claude_opus_aliases() -> None:
    assert normalize_model_partition("opus-4-6") == "claude-opus-4-6"
    assert normalize_model_partition("opus-4.6") == "claude-opus-4-6"
    assert normalize_model_partition("claude-opus-4.6") == "claude-opus-4-6"


def test_build_model_partition_keeps_reasoning_effort_for_non_aliases() -> None:
    assert build_model_partition("gpt-5.4", "xhigh") == "gpt-5-4-xhigh"
