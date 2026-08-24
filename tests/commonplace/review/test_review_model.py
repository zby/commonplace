from __future__ import annotations

from commonplace.review.review_model import (
    build_model_partition,
    normalize_model_partition,
)


def test_normalize_model_partition_collapses_registered_aliases() -> None:
    aliases = {
        "opus-4-6": "claude-opus",
        "claude-opus-4.8[1m]": "claude-opus-4.8",
        "claude-fable-5": "claude-opus-4.8",
        "sonnet": "claude-sonnet-5",
        "claude-sonnet-4-6": "claude-sonnet",
        "gpt-5.4-high": "codex",
        "gpt-5.5-high": "codex-5.5",
        "luna": "luna",
        "sol": "sol",
    }

    assert {
        alias: normalize_model_partition(alias) for alias in aliases
    } == aliases


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
