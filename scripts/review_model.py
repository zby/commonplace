from __future__ import annotations

import os
import re


MODEL_ENV_VAR = "COMMONPLACE_REVIEW_MODEL"
REASONING_EFFORT_VALUES = ("low", "medium", "high", "xhigh")


def encode_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", model).strip("-").lower()


def normalize_reasoning_effort(raw: str | None) -> str | None:
    if raw is None:
        return None
    effort = raw.strip().lower()
    if not effort:
        return None
    if effort not in REASONING_EFFORT_VALUES:
        return None
    return effort


def build_model_id(model: str, reasoning_effort: str | None = None) -> str:
    encoded_model = encode_model(model)
    effort = normalize_reasoning_effort(reasoning_effort)
    if effort is None:
        return encoded_model
    return f"{encoded_model}-{effort}"


def resolve_model() -> str:
    model = os.environ.get(MODEL_ENV_VAR, "").strip()
    if model:
        return model

    raise ValueError(
        f"{MODEL_ENV_VAR} is not set.\n"
        "This variable determines the review filename suffix and freshness key.\n"
        "Set it to the model producing reviews in this run, for example:\n"
        "  COMMONPLACE_REVIEW_MODEL=gpt-5-4-xhigh\n"
        "  COMMONPLACE_REVIEW_MODEL=gpt-5-codex-high\n"
        "  COMMONPLACE_REVIEW_MODEL=opus-4-6\n"
        "Do not copy a suffix from existing review files."
    )
