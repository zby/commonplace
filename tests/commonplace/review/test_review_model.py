from __future__ import annotations

from commonplace.review.review_model import build_model_partition, normalize_model_partition


def test_normalize_model_partition_collapses_registered_aliases() -> None:
    assert normalize_model_partition("opus-4-6") == "claude-opus"
    assert normalize_model_partition("opus-4.6") == "claude-opus"
    assert normalize_model_partition("claude-opus-4.6") == "claude-opus"
    assert normalize_model_partition("claude-opus-4.8") == "claude-opus-4.8"
    assert normalize_model_partition("claude-opus-4.8[1m]") == "claude-opus-4.8"
    assert normalize_model_partition("claude-fable-5") == "claude-opus-4.8"
    assert normalize_model_partition("sonnet") == "claude-sonnet-5"
    assert normalize_model_partition("claude-sonnet-5") == "claude-sonnet-5"
    assert normalize_model_partition("claude-sonnet-4-6") == "claude-sonnet"
    assert normalize_model_partition("gpt-5.4-high") == "codex"
    assert normalize_model_partition("gpt-5.5-high") == "codex-5.5"
    assert normalize_model_partition("luna") == "luna"
    assert normalize_model_partition("sol") == "sol"


def test_build_model_partition_collapses_effort_for_registered_models() -> None:
    assert build_model_partition("claude-opus-4.8[1m]") == "claude-opus-4.8"
    assert build_model_partition("gpt-5.4", "xhigh") == "codex"
    assert build_model_partition("gpt-5.5", "high") == "codex-5.5"
    assert build_model_partition("luna", "high") == "luna"
    assert build_model_partition("sol", "high") == "sol"
    assert build_model_partition("unknown-model", "high") == "unknown-model-high"
