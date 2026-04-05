from __future__ import annotations

import re
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
