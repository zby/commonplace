"""Summarize offered and consumed link cost from the Commonplace review store.

Run from the repository root with ``python3 scripts/review_link_consumption.py``.
The optional positional argument overrides ``COMMONPLACE_STORE`` and the default
``kb/reports/commonplace-store.sqlite`` path.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DEFAULT_STORE = Path("kb/reports/commonplace-store.sqlite")


def _distribution(values: list[int]) -> str:
    ordered = sorted(values)
    if not ordered:
        return "-"

    def quantile(fraction: float) -> int:
        index = min(len(ordered) - 1, round(fraction * (len(ordered) - 1)))
        return ordered[index]

    return (
        f"min={ordered[0]} p50={quantile(0.5)} "
        f"p90={quantile(0.9)} max={ordered[-1]}"
    )


def _offered_count(version: object, offered: dict[str, Any]) -> int | None:
    if version == 3:
        value = offered.get("distinct_consumption_target_count")
    elif version == 1 or version == 2:
        # BACKCOMPAT: availability v1/v2 used this name for the same logical
        # count - remove after historical v1/v2 jobs are excluded from reports.
        value = offered.get("distinct_artifact_count")
    else:
        return None
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        return None
    return value


def _load_rows(
    connection: sqlite3.Connection,
) -> tuple[
    list[dict[str, Any]],
    list[dict[str, int]],
    Counter[Any],
    Counter[Any],
    Counter[Any],
]:
    rows: list[dict[str, Any]] = []
    jobs: list[dict[str, int]] = []
    versions: Counter[Any] = Counter()
    statuses: Counter[Any] = Counter()
    stop_reasons: Counter[Any] = Counter()

    job_query = """
        SELECT review_job_id, runner_model, telemetry_json
        FROM review_jobs
        WHERE telemetry_json IS NOT NULL
    """
    for job in connection.execute(job_query):
        try:
            telemetry = json.loads(job["telemetry_json"])
        except (TypeError, json.JSONDecodeError):
            continue

        commonplace = telemetry.get("commonplace") if isinstance(telemetry, dict) else None
        if not isinstance(commonplace, dict):
            continue
        availability = commonplace.get("review_link_availability")
        consumption = commonplace.get("review_link_consumption")
        if not isinstance(availability, dict) or not isinstance(consumption, dict):
            continue

        versions[("availability", availability.get("version"))] += 1
        versions[("consumption", consumption.get("version"))] += 1
        offered_by_pair = {
            (pair["note_path"], pair["criterion_path"]): pair
            for pair in availability.get("pairs", [])
        }
        job_totals = {
            "offered_count": 0,
            "consumed_count": 0,
            "offered_bytes": 0,
            "consumed_bytes": 0,
        }

        for report in consumption.get("pairs", []):
            pair_key = (report.get("note_path"), report.get("criterion_path"))
            statuses[report.get("report_status")] += 1
            if report.get("stop_reason") is not None:
                stop_reasons[report.get("stop_reason")] += 1
            offered = offered_by_pair.get(pair_key)
            if offered is None:
                continue

            offered_count = _offered_count(availability.get("version"), offered)
            offered_bytes = offered.get("total_bytes")
            consumed_count = report.get("distinct_artifact_count")
            consumed_bytes = report.get("total_bytes")
            if offered_count is None:
                continue
            job_totals["offered_count"] += offered_count or 0
            job_totals["consumed_count"] += consumed_count or 0
            job_totals["offered_bytes"] += offered_bytes or 0
            job_totals["consumed_bytes"] += consumed_bytes or 0
            rows.append(
                {
                    "job": job["review_job_id"],
                    "note": pair_key[0],
                    "criterion": pair_key[1],
                    "offered_count": offered_count,
                    "offered_bytes": offered_bytes,
                    "consumed_count": consumed_count,
                    "consumed_bytes": consumed_bytes,
                    "stop_reason": report.get("stop_reason"),
                    "report_status": report.get("report_status"),
                    "model": job["runner_model"],
                }
            )

        jobs.append({"job": job["review_job_id"], **job_totals})

    outcomes = {
        (row["review_job_id"], row["note_path"], row["criterion_path"]): (
            row["outcome"],
            row["result_kind"],
        )
        for row in connection.execute(
            "SELECT review_job_id, note_path, criterion_path, outcome, result_kind "
            "FROM review_pairs"
        )
    }
    for row in rows:
        row["outcome"], row["result_kind"] = outcomes.get(
            (row["job"], row["note"], row["criterion"]),
            (None, None),
        )

    return rows, jobs, versions, statuses, stop_reasons


def _print_group(rows: list[dict[str, Any]], key: str, label: str) -> None:
    grouped: defaultdict[Any, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row[key]].append(row)

    print(f"\n== BY {label} ==")
    print(
        f"{'value':<58} {'n':>3} {'off_n med':>9} {'con_n med':>9} "
        f"{'ratio med':>9} {'off_b med':>9} {'con_b med':>9}"
    )
    for value, group_rows in sorted(grouped.items(), key=lambda item: -len(item[1])):
        ratios = [
            row["consumed_count"] / row["offered_count"]
            for row in group_rows
            if row["offered_count"] and row["consumed_count"] is not None
        ]
        print(
            f"{value!s:<58} {len(group_rows):>3} "
            f"{statistics.median(row['offered_count'] for row in group_rows):>9.1f} "
            f"{statistics.median(row['consumed_count'] or 0 for row in group_rows):>9.1f} "
            f"{(statistics.median(ratios) if ratios else 0):>9.2f} "
            f"{statistics.median(row['offered_bytes'] for row in group_rows):>9.0f} "
            f"{statistics.median(row['consumed_bytes'] or 0 for row in group_rows):>9.0f}"
        )


def _print_report(
    rows: list[dict[str, Any]],
    jobs: list[dict[str, int]],
    versions: Counter[Any],
    statuses: Counter[Any],
    stop_reasons: Counter[Any],
) -> None:
    print("versions:", dict(versions))
    print("report_status:", dict(statuses), " stop_reason:", dict(stop_reasons))
    print("pairs matched:", len(rows), " jobs:", len(jobs))

    print("\n== PER-JOB ==")
    print(
        f"{'job':>5} {'off_n':>6} {'con_n':>6} {'ratio':>6} "
        f"{'off_b':>8} {'con_b':>8} {'con/off_b':>9}"
    )
    for job in sorted(jobs, key=lambda item: item["job"]):
        count_ratio = (
            job["consumed_count"] / job["offered_count"]
            if job["offered_count"]
            else float("nan")
        )
        byte_ratio = (
            job["consumed_bytes"] / job["offered_bytes"]
            if job["offered_bytes"]
            else float("nan")
        )
        print(
            f"{job['job']:>5} {job['offered_count']:>6} {job['consumed_count']:>6} "
            f"{count_ratio:>6.2f} {job['offered_bytes']:>8} "
            f"{job['consumed_bytes']:>8} {byte_ratio:>9.2f}"
        )

    print("\n== PER-PAIR AGGREGATE ==")
    print(" offered count :", _distribution([row["offered_count"] for row in rows]))
    print(
        " consumed count:",
        _distribution(
            [row["consumed_count"] for row in rows if row["consumed_count"] is not None]
        ),
    )
    ratios = sorted(
        round(row["consumed_count"] / row["offered_count"], 3)
        for row in rows
        if row["offered_count"] and row["consumed_count"] is not None
    )
    if ratios:
        print(
            " ratio         : "
            f"min={ratios[0]} p50={ratios[len(ratios) // 2]} "
            f"p90={ratios[round(0.9 * (len(ratios) - 1))]} max={ratios[-1]}"
        )
    print(" offered bytes :", _distribution([row["offered_bytes"] for row in rows]))
    print(
        " consumed bytes:",
        _distribution(
            [row["consumed_bytes"] for row in rows if row["consumed_bytes"] is not None]
        ),
    )

    consumed_all = [
        row
        for row in rows
        if row["consumed_count"] is not None
        and row["consumed_count"] >= row["offered_count"]
    ]
    consumed_fewer = [
        row
        for row in rows
        if row["consumed_count"] is not None
        and row["consumed_count"] < row["offered_count"]
    ]
    offered_over_five = [row for row in rows if row["offered_count"] > 5]
    consumed_over_five = [
        row for row in offered_over_five if (row["consumed_count"] or 0) > 5
    ]
    print(
        f" consumed all offered: {len(consumed_all)}   "
        f"consumed fewer: {len(consumed_fewer)}"
    )
    print(
        f" offered>5: {len(offered_over_five)}  "
        f"of which consumed>5: {len(consumed_over_five)}  "
        f"consumed<=5: {len(offered_over_five) - len(consumed_over_five)}"
    )
    print(
        " consumed count histogram:",
        dict(
            sorted(
                Counter(
                    row["consumed_count"]
                    for row in rows
                    if row["consumed_count"] is not None
                ).items()
            )
        ),
    )

    _print_group(rows, "criterion", "CRITERION")
    _print_group(rows, "outcome", "OUTCOME")
    _print_group(rows, "stop_reason", "STOP_REASON")
    _print_group(rows, "model", "RUNNER MODEL")
    print(
        "\nstop x offered>5:",
        dict(Counter(row["stop_reason"] for row in offered_over_five)),
    )
    print(
        "stop x consumed-all:",
        dict(Counter(row["stop_reason"] for row in consumed_all)),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "store",
        nargs="?",
        type=Path,
        default=Path(os.environ.get("COMMONPLACE_STORE", DEFAULT_STORE)),
    )
    args = parser.parse_args()

    connection = sqlite3.connect(f"file:{args.store}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        _print_report(*_load_rows(connection))
    finally:
        connection.close()


if __name__ == "__main__":
    main()
