"""Canonical target identity encoding."""

from __future__ import annotations

import json


def canonical_json(data: dict[str, str]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def review_pair_target_key(
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str,
) -> str:
    return canonical_json(
        {
            "criterion_path": criterion_path,
            "model_partition": model_partition,
            "note_path": note_path,
        }
    )