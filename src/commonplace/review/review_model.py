from __future__ import annotations

import re

REASONING_EFFORT_VALUES = ("low", "medium", "high", "xhigh")

MODEL_PARTITION_REGISTRY = {
    "claude-opus": (
        "claude-opus-4-6",
        "claude-opus-4-7",
        "opus-4-6",
        "opus-4-7",
    ),
    "claude-opus-4.8": (
        "claude-opus-4-8",
        "claude-opus-4-8-xhigh",
        "claude-fable-5",
    ),
    "claude-sonnet": (
        "sonnet",
        "claude-sonnet-4-6",
        "claude-sonnet-4-20250514",
    ),
    "codex": (
        "gpt-5",
        "gpt-5-high",
        "gpt-5-2-high",
        "gpt-5-3-codex-high",
        "gpt-5-4",
        "gpt-5-4-high",
        "gpt-5-4-xhigh",
        "gpt-5.3-codex",
        "gpt-5.4",
        "gpt-5-codex",
        "gpt-5-codex-high",
        "codex-gpt-5-2",
    ),
    "codex-5.5": (
        "gpt-5-5",
        "gpt-5-5-high",
    ),
}


def encode_model(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", model).strip("-").lower()


def _model_partition_aliases() -> dict[str, str]:
    aliases: dict[str, str] = {}
    for canonical_partition, partition_aliases in MODEL_PARTITION_REGISTRY.items():
        aliases[encode_model(canonical_partition)] = canonical_partition
        for alias in partition_aliases:
            aliases[encode_model(alias)] = canonical_partition
    return aliases


MODEL_PARTITION_ALIASES = _model_partition_aliases()


def normalize_model_partition(model_partition: str) -> str:
    encoded_model = encode_model(model_partition)
    return MODEL_PARTITION_ALIASES.get(encoded_model, encoded_model)


def is_registered_model_partition(model_partition: str) -> bool:
    encoded_model = encode_model(model_partition)
    return encoded_model in MODEL_PARTITION_ALIASES


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
    encoded_model = encode_model(model)
    effort = normalize_reasoning_effort(reasoning_effort)
    if effort is None:
        return normalize_model_partition(encoded_model)

    effort_partition = f"{encoded_model}-{effort}"
    normalized_effort_partition = normalize_model_partition(effort_partition)
    if normalized_effort_partition != effort_partition:
        return normalized_effort_partition

    normalized_model = normalize_model_partition(encoded_model)
    if normalized_model != encoded_model:
        return normalized_model
    return effort_partition
