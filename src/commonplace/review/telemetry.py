"""Compose deterministic review measurements with opaque harness telemetry."""

from __future__ import annotations

import json
from collections.abc import Sequence

from commonplace.review.protocol.prompt import NoteReviewTarget, available_link_cost

_COMMONPLACE_KEY = "commonplace"
_LINK_AVAILABILITY_KEY = "review_link_availability"
_HARNESS_TELEMETRY_KEY = "harness_telemetry_json"
_LINK_AVAILABILITY_VERSION = 1


def _note_link_availability(note: NoteReviewTarget) -> dict[str, object]:
    resolved_link_count, distinct_artifact_count, total_bytes = available_link_cost(note)

    return {
        "resolved_link_count": resolved_link_count,
        "distinct_artifact_count": distinct_artifact_count,
        "total_bytes": total_bytes,
        "unavailable_targets": [
            {
                "link_text": target.link_text,
                "raw_target": target.raw_target,
                "target_path": target.target_path,
                "reason": target.reason,
            }
            for target in note.unavailable_targets
        ],
    }


def link_availability_telemetry_json(notes: Sequence[NoteReviewTarget]) -> str:
    """Serialize per-pair whole-file link availability for one review job."""
    pairs: list[dict[str, object]] = []
    for note in notes:
        availability = _note_link_availability(note)
        for criterion_path in note.criterion_paths:
            pairs.append(
                {
                    "note_path": note.note_path,
                    "criterion_path": criterion_path,
                    **availability,
                }
            )

    payload = {
        _COMMONPLACE_KEY: {
            _LINK_AVAILABILITY_KEY: {
                "version": _LINK_AVAILABILITY_VERSION,
                "pairs": pairs,
            }
        }
    }
    return json.dumps(payload, ensure_ascii=True, sort_keys=True)


def with_harness_telemetry(
    existing_telemetry_json: str | None,
    harness_telemetry_json: str,
) -> str:
    """Preserve opaque harness telemetry beside code-generated measurements.

    The harness value remains uninterpreted and byte-for-byte intact as a JSON
    string. Existing non-object or invalid telemetry is also retained rather
    than preventing job finalization.
    """
    payload: dict[str, object]
    if existing_telemetry_json is None:
        payload = {}
    else:
        try:
            existing = json.loads(existing_telemetry_json)
        except json.JSONDecodeError:
            payload = {"preexisting_telemetry_json": existing_telemetry_json}
        else:
            if isinstance(existing, dict):
                payload = existing
            else:
                payload = {"preexisting_telemetry": existing}

    payload[_HARNESS_TELEMETRY_KEY] = harness_telemetry_json
    return json.dumps(payload, ensure_ascii=True, sort_keys=True)
