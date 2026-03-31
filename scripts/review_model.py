from __future__ import annotations

import os
import re


MODEL_ENV_VAR = "COMMONPLACE_REVIEW_MODEL"


def encode_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", model).strip("-").lower()


def resolve_model() -> str:
    model = os.environ.get(MODEL_ENV_VAR, "").strip()
    if model:
        return model

    raise ValueError(
        f"{MODEL_ENV_VAR} is not set.\n"
        "This variable determines the review filename suffix and freshness key.\n"
        "Set it to the model producing reviews in this run, for example:\n"
        "  COMMONPLACE_REVIEW_MODEL=gpt-5-4-high\n"
        "  COMMONPLACE_REVIEW_MODEL=opus-4-6\n"
        "Do not copy a suffix from existing review files."
    )
