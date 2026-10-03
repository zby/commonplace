from __future__ import annotations

from commonplace.review.review_model import build_model_partition


def test_build_model_partition_collapses_effort_for_registered_models() -> None:
    cases = {
        ("claude-opus-4.8[1m]", None): "claude-opus-4.8",
        ("gpt-5.4", "xhigh"): "codex",
        ("gpt-5.5", "high"): "codex-5.5",
        ("luna", "high"): "luna",
        ("unknown-model", "high"): "unknown-model-high",
    }

    assert {
        case: build_model_partition(*case) for case in cases
    } == cases
