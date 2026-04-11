from __future__ import annotations

from commonplace.review.review_model import build_model_id, normalize_model_id


def test_normalize_model_id_collapses_claude_opus_aliases() -> None:
    assert normalize_model_id("opus-4-6") == "claude-opus-4-6"
    assert normalize_model_id("opus-4.6") == "claude-opus-4-6"
    assert normalize_model_id("claude-opus-4.6") == "claude-opus-4-6"


def test_build_model_id_keeps_reasoning_effort_for_non_aliases() -> None:
    assert build_model_id("gpt-5.4", "xhigh") == "gpt-5-4-xhigh"
