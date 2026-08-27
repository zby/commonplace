from __future__ import annotations

import json

from commonplace.review.protocol.parser import ParsedReviewConsumption
from commonplace.review.protocol.prompt import NoteReviewTarget, ResolvedMarkdownLink
from commonplace.review.telemetry import (
    link_availability_telemetry_json,
    with_review_link_consumption,
)


def test_link_availability_telemetry_records_cost_for_each_pair() -> None:
    target = NoteReviewTarget(
        note_path="kb/notes/sample.md",
        criterion_paths=("criterion/one", "criterion/two"),
        note_text="# Sample\n",
        resolved_links=(
            ResolvedMarkdownLink(
                "first",
                "./shared.md",
                "kb/notes/shared.md",
                "kb/notes/shared.md",
                800,
            ),
            ResolvedMarkdownLink(
                "again",
                "./shared.md#part",
                "kb/notes/shared.md",
                "kb/notes/shared.md",
                800,
            ),
        ),
    )

    telemetry = json.loads(link_availability_telemetry_json([target]))
    availability = telemetry["commonplace"]["review_link_availability"]
    pairs = availability["pairs"]

    assert availability["version"] == 3
    assert [pair["criterion_path"] for pair in pairs] == ["criterion/one", "criterion/two"]
    assert all(pair["resolved_link_count"] == 2 for pair in pairs)
    assert all(pair["distinct_link_target_count"] == 1 for pair in pairs)
    assert all(pair["distinct_consumption_target_count"] == 1 for pair in pairs)
    assert all(pair["total_bytes"] == 800 for pair in pairs)
    assert all(
        pair["artifacts"] == [{"path": "kb/notes/shared.md", "size_bytes": 800}]
        for pair in pairs
    )
    assert all(
        pair["routes"]
        == [
            {
                "link_target_path": "kb/notes/shared.md",
                "consumption_path": "kb/notes/shared.md",
            }
        ]
        for pair in pairs
    )


def test_link_availability_counts_one_ingest_across_two_consumption_routes() -> None:
    target = NoteReviewTarget(
        note_path="kb/notes/sample.md",
        criterion_paths=("criterion/one",),
        note_text="# Sample\n",
        resolved_links=(
            ResolvedMarkdownLink(
                "source",
                "../sources/source.ingest.md",
                "kb/sources/source.ingest.md",
                "kb/sources/source.ingest.md",
                100,
            ),
            ResolvedMarkdownLink(
                "source (snapshot required)",
                "../sources/source.ingest.md",
                "kb/sources/source.ingest.md",
                "kb/sources/.snapshots/source.md",
                2400,
            ),
        ),
    )

    telemetry = json.loads(link_availability_telemetry_json([target]))
    pair = telemetry["commonplace"]["review_link_availability"]["pairs"][0]

    assert pair["resolved_link_count"] == 2
    assert pair["distinct_link_target_count"] == 1
    assert pair["distinct_consumption_target_count"] == 2
    assert pair["total_bytes"] == 2500
    assert pair["artifacts"] == [
        {"path": "kb/sources/source.ingest.md", "size_bytes": 100},
        {"path": "kb/sources/.snapshots/source.md", "size_bytes": 2400},
    ]
    assert pair["routes"] == [
        {
            "link_target_path": "kb/sources/source.ingest.md",
            "consumption_path": "kb/sources/source.ingest.md",
        },
        {
            "link_target_path": "kb/sources/source.ingest.md",
            "consumption_path": "kb/sources/.snapshots/source.md",
        },
    ]


def test_review_consumption_joins_available_cost_and_prices_distinct_paths() -> None:
    pair = ("kb/notes/sample.md", "criterion/one")
    target = NoteReviewTarget(
        note_path=pair[0],
        criterion_paths=(pair[1],),
        note_text="# Sample\n",
        resolved_links=(
            ResolvedMarkdownLink(
                "first",
                "./shared.md",
                "kb/notes/shared.md",
                "kb/notes/shared.md",
                800,
            ),
            ResolvedMarkdownLink(
                "again",
                "./shared.md#part",
                "kb/notes/shared.md",
                "kb/notes/shared.md",
                800,
            ),
            ResolvedMarkdownLink(
                "other",
                "./other.md",
                "kb/notes/other.md",
                "kb/notes/other.md",
                300,
            ),
        ),
    )
    availability = link_availability_telemetry_json([target])

    telemetry = json.loads(
        with_review_link_consumption(
            availability,
            {
                pair: ParsedReviewConsumption(
                    report_status="complete",
                    opened_paths=("kb/notes/shared.md", "kb/notes/other.md"),
                    stop_reason="sufficiency",
                    missing_fields=(),
                    malformed_fields=(),
                )
            },
        )
    )

    consumption = telemetry["commonplace"]["review_link_consumption"]
    assert consumption == {
        "version": 2,
        "pairs": [
            {
                "note_path": pair[0],
                "criterion_path": pair[1],
                "report_status": "complete",
                "opened_paths": ["kb/notes/shared.md", "kb/notes/other.md"],
                "distinct_artifact_count": 2,
                "total_bytes": 1100,
                "stop_reason": "sufficiency",
                "missing_fields": [],
                "malformed_fields": [],
                "unpriced_paths": [],
            }
        ],
    }


def test_snapshot_route_telemetry_prices_snapshot_and_retains_ingest_lineage() -> None:
    pair = ("kb/notes/sample.md", "criterion/one")
    snapshot_path = "kb/sources/.snapshots/source.md"
    target = NoteReviewTarget(
        note_path=pair[0],
        criterion_paths=(pair[1],),
        note_text="# Sample\n",
        resolved_links=(
            ResolvedMarkdownLink(
                "source (snapshot required)",
                "../sources/source.ingest.md",
                "kb/sources/source.ingest.md",
                snapshot_path,
                2400,
            ),
        ),
    )
    availability_json = link_availability_telemetry_json([target])
    availability = json.loads(availability_json)["commonplace"]["review_link_availability"]

    assert availability == {
        "version": 3,
        "pairs": [
            {
                "note_path": pair[0],
                "criterion_path": pair[1],
                "resolved_link_count": 1,
                "distinct_link_target_count": 1,
                "distinct_consumption_target_count": 1,
                "total_bytes": 2400,
                "artifacts": [{"path": snapshot_path, "size_bytes": 2400}],
                "routes": [
                    {
                        "link_target_path": "kb/sources/source.ingest.md",
                        "consumption_path": snapshot_path,
                    }
                ],
                "unavailable_targets": [],
            }
        ],
    }

    telemetry = json.loads(
        with_review_link_consumption(
            availability_json,
            {
                pair: ParsedReviewConsumption(
                    report_status="complete",
                    opened_paths=(snapshot_path,),
                    stop_reason="sufficiency",
                    missing_fields=(),
                    malformed_fields=(),
                )
            },
        )
    )
    consumption = telemetry["commonplace"]["review_link_consumption"]

    assert consumption == {
        "version": 2,
        "pairs": [
            {
                "note_path": pair[0],
                "criterion_path": pair[1],
                "report_status": "complete",
                "opened_paths": [snapshot_path],
                "distinct_artifact_count": 1,
                "total_bytes": 2400,
                "stop_reason": "sufficiency",
                "missing_fields": [],
                "malformed_fields": [],
                "unpriced_paths": [],
            }
        ],
    }


def test_review_consumption_records_missing_and_unpriced_reports_without_raising() -> None:
    known_pair = ("kb/notes/sample.md", "criterion/one")
    missing_pair = ("kb/notes/other.md", "criterion/two")
    target = NoteReviewTarget(
        note_path=known_pair[0],
        criterion_paths=(known_pair[1],),
        note_text="# Sample\n",
        resolved_links=(
            ResolvedMarkdownLink(
                "known",
                "./known.md",
                "kb/notes/known.md",
                "kb/notes/known.md",
                500,
            ),
        ),
    )

    telemetry = json.loads(
        with_review_link_consumption(
            link_availability_telemetry_json([target]),
            {
                known_pair: ParsedReviewConsumption(
                    report_status="complete",
                    opened_paths=("kb/notes/known.md", "kb/notes/unlisted.md"),
                    stop_reason="budget",
                    missing_fields=(),
                    malformed_fields=(),
                ),
                missing_pair: ParsedReviewConsumption(
                    report_status="missing",
                    opened_paths=None,
                    stop_reason=None,
                    missing_fields=("opened_paths", "stop_reason"),
                    malformed_fields=(),
                ),
            },
        )
    )
    records = telemetry["commonplace"]["review_link_consumption"]["pairs"]

    assert records[0]["report_status"] == "malformed"
    assert records[0]["opened_paths"] == ["kb/notes/known.md", "kb/notes/unlisted.md"]
    assert records[0]["unpriced_paths"] == ["kb/notes/unlisted.md"]
    assert "total_bytes" not in records[0]
    assert records[0]["malformed_fields"] == ["opened_paths:unpriced"]
    assert records[1] == {
        "note_path": missing_pair[0],
        "criterion_path": missing_pair[1],
        "report_status": "missing",
        "missing_fields": ["opened_paths", "stop_reason"],
        "malformed_fields": [],
    }
