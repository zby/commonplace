"""Compose deterministic review measurements with opaque harness telemetry."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence

from commonplace.review.protocol.parser import PairKey, ParsedReviewConsumption
from commonplace.review.protocol.prompt import NoteReviewTarget, available_link_cost

_COMMONPLACE_KEY = "commonplace"
_LINK_AVAILABILITY_KEY = "review_link_availability"
_LINK_CONSUMPTION_KEY = "review_link_consumption"
_HARNESS_TELEMETRY_KEY = "harness_telemetry_json"
_LINK_AVAILABILITY_VERSION = 3
_LINK_CONSUMPTION_VERSION = 2


def _available_artifacts(note: NoteReviewTarget) -> list[dict[str, object]]:
    sizes_by_path: dict[str, int] = {}
    for link in note.resolved_links:
        sizes_by_path.setdefault(link.consumption_path, link.size_bytes)
    return [
        {"path": path, "size_bytes": size_bytes}
        for path, size_bytes in sizes_by_path.items()
    ]


def _available_routes(note: NoteReviewTarget) -> list[dict[str, str]]:
    routes: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for link in note.resolved_links:
        route = (link.link_target_path, link.consumption_path)
        if route in seen:
            continue
        seen.add(route)
        routes.append(
            {
                "link_target_path": link.link_target_path,
                "consumption_path": link.consumption_path,
            }
        )
    return routes


def _note_link_availability(note: NoteReviewTarget) -> dict[str, object]:
    (
        resolved_link_count,
        distinct_link_target_count,
        distinct_consumption_target_count,
        total_bytes,
    ) = available_link_cost(note)

    return {
        "resolved_link_count": resolved_link_count,
        "distinct_link_target_count": distinct_link_target_count,
        "distinct_consumption_target_count": distinct_consumption_target_count,
        "total_bytes": total_bytes,
        "artifacts": _available_artifacts(note),
        "routes": _available_routes(note),
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


def _telemetry_payload(existing_telemetry_json: str | None) -> dict[str, object]:
    if existing_telemetry_json is None:
        return {}
    try:
        existing = json.loads(existing_telemetry_json)
    except json.JSONDecodeError:
        return {"preexisting_telemetry_json": existing_telemetry_json}
    if isinstance(existing, dict):
        return existing
    return {"preexisting_telemetry": existing}


def _commonplace_payload(payload: dict[str, object]) -> dict[str, object]:
    existing = payload.get(_COMMONPLACE_KEY)
    if isinstance(existing, dict):
        return existing
    if existing is not None:
        payload["preexisting_commonplace"] = existing
    commonplace: dict[str, object] = {}
    payload[_COMMONPLACE_KEY] = commonplace
    return commonplace


def _available_sizes_by_pair(commonplace: Mapping[str, object]) -> dict[PairKey, dict[str, int]]:
    availability = commonplace.get(_LINK_AVAILABILITY_KEY)
    if not isinstance(availability, dict):
        return {}
    pairs = availability.get("pairs")
    if not isinstance(pairs, list):
        return {}

    sizes_by_pair: dict[PairKey, dict[str, int]] = {}
    for pair in pairs:
        if not isinstance(pair, dict):
            continue
        note_path = pair.get("note_path")
        criterion_path = pair.get("criterion_path")
        artifacts = pair.get("artifacts")
        if not isinstance(note_path, str) or not isinstance(criterion_path, str):
            continue
        if not isinstance(artifacts, list):
            continue
        sizes: dict[str, int] = {}
        for artifact in artifacts:
            if not isinstance(artifact, dict):
                continue
            path = artifact.get("path")
            size_bytes = artifact.get("size_bytes")
            if isinstance(path, str) and isinstance(size_bytes, int) and size_bytes >= 0:
                sizes.setdefault(path, size_bytes)
        sizes_by_pair[(note_path, criterion_path)] = sizes
    return sizes_by_pair


def _consumption_pair_payload(
    pair: PairKey,
    report: ParsedReviewConsumption,
    available_sizes: Mapping[str, int],
) -> dict[str, object]:
    record: dict[str, object] = {
        "note_path": pair[0],
        "criterion_path": pair[1],
    }
    missing_fields = list(report.missing_fields)
    malformed_fields = list(report.malformed_fields)
    report_status = report.report_status

    if report.opened_paths is not None:
        opened_paths = list(report.opened_paths)
        unpriced_paths = [path for path in opened_paths if path not in available_sizes]
        record["opened_paths"] = opened_paths
        record["distinct_artifact_count"] = len(opened_paths)
        record["unpriced_paths"] = unpriced_paths
        if unpriced_paths:
            malformed_fields.append("opened_paths:unpriced")
            report_status = "malformed"
        else:
            record["total_bytes"] = sum(available_sizes[path] for path in opened_paths)

    if report.stop_reason is not None:
        record["stop_reason"] = report.stop_reason

    record["report_status"] = report_status
    record["missing_fields"] = list(dict.fromkeys(missing_fields))
    record["malformed_fields"] = list(dict.fromkeys(malformed_fields))
    return record


def with_review_link_consumption(
    existing_telemetry_json: str | None,
    reports: Mapping[PairKey, ParsedReviewConsumption],
) -> str:
    """Record soft reviewer consumption reports beside available link cost."""
    payload = _telemetry_payload(existing_telemetry_json)
    commonplace = _commonplace_payload(payload)
    available_sizes = _available_sizes_by_pair(commonplace)
    commonplace[_LINK_CONSUMPTION_KEY] = {
        "version": _LINK_CONSUMPTION_VERSION,
        "pairs": [
            _consumption_pair_payload(pair, report, available_sizes.get(pair, {}))
            for pair, report in reports.items()
        ],
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
    payload = _telemetry_payload(existing_telemetry_json)
    payload[_HARNESS_TELEMETRY_KEY] = harness_telemetry_json
    return json.dumps(payload, ensure_ascii=True, sort_keys=True)
