import json
import sqlite3

from scripts.review_link_consumption import _load_rows, _offered_count


def test_offered_count_reads_consumption_targets_and_rejects_invalid_counts() -> None:
    offered = {
        "distinct_link_target_count": 3,
        "distinct_consumption_target_count": 5,
        "distinct_artifact_count": 9,
    }

    assert _offered_count(offered) == 5
    assert _offered_count({"distinct_artifact_count": 4}) is None
    assert _offered_count({"distinct_consumption_target_count": True}) is None
    assert _offered_count({"distinct_consumption_target_count": -1}) is None


def test_report_excludes_unsupported_jobs_from_rows_totals_and_counters() -> None:
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    try:
        connection.executescript(
            "CREATE TABLE review_jobs "
            "(review_job_id INTEGER, runner_model TEXT, telemetry_json TEXT);"
            "CREATE TABLE review_pairs "
            "(review_job_id INTEGER, note_path TEXT, criterion_path TEXT, "
            "outcome TEXT, result_kind TEXT);"
        )
        pair = {"note_path": "note.md", "criterion_path": "criterion.md"}
        for job_id, version in enumerate([1, 2, 3, 4, None], start=1):
            telemetry = {
                "commonplace": {
                    "review_link_availability": {
                        "version": version,
                        "pairs": [
                            {
                                **pair,
                                "distinct_artifact_count": 9,
                                "distinct_consumption_target_count": 5,
                                "total_bytes": 100,
                            }
                        ],
                    },
                    "review_link_consumption": {
                        "version": 2,
                        "pairs": [
                            {
                                **pair,
                                "distinct_artifact_count": 2,
                                "total_bytes": 40,
                                "report_status": "complete",
                                "stop_reason": "sufficiency",
                            }
                        ],
                    },
                },
            }
            connection.execute(
                "INSERT INTO review_jobs VALUES (?, ?, ?)",
                (job_id, "test-model", json.dumps(telemetry)),
            )

        rows, jobs, versions, statuses, stop_reasons = _load_rows(connection)
        assert len(rows) == 1
        assert rows[0]["job"] == 3
        assert rows[0]["offered_count"] == 5
        assert jobs == [
            {
                "job": 3,
                "offered_count": 5,
                "consumed_count": 2,
                "offered_bytes": 100,
                "consumed_bytes": 40,
            }
        ]
        assert versions == {("availability", 3): 1, ("consumption", 2): 1}
        assert statuses == {"complete": 1}
        assert stop_reasons == {"sufficiency": 1}
    finally:
        connection.close()
