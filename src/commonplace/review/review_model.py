from __future__ import annotations

import re

REASONING_EFFORT_VALUES = ("low", "medium", "high", "xhigh")
MODEL_PARTITION_ALIASES = {
    "claude-opus-4-6": "claude-opus-4-6",
    "opus-4-6": "claude-opus-4-6",
}


def encode_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", model).strip("-").lower()


def normalize_model_partition(model_partition: str) -> str:
    encoded_model = encode_model(model_partition)
    return MODEL_PARTITION_ALIASES.get(encoded_model, encoded_model)


def model_partition_alias_target(model_partition: str) -> str | None:
    encoded_model = encode_model(model_partition)
    target = MODEL_PARTITION_ALIASES.get(encoded_model)
    if target is None or target == model_partition:
        return None
    return target


def normalize_reasoning_effort(raw: str | None) -> str | None:
    if raw is None:
        return None
    effort = raw.strip().lower()
    if not effort:
        return None
    if effort not in REASONING_EFFORT_VALUES:
        return None
    return effort


def build_model_partition(model: str, reasoning_effort: str | None = None) -> str:
    encoded_model = normalize_model_partition(model)
    effort = normalize_reasoning_effort(reasoning_effort)
    if effort is None:
        return encoded_model
    return f"{encoded_model}-{effort}"
