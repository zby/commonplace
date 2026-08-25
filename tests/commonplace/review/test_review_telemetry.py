from __future__ import annotations

import json

from commonplace.review.protocol.prompt import NoteReviewTarget, ResolvedMarkdownLink
from commonplace.review.telemetry import link_availability_telemetry_json


def test_link_availability_telemetry_records_cost_for_each_pair() -> None:
    target = NoteReviewTarget(
        note_path="kb/notes/sample.md",
        criterion_paths=("criterion/one", "criterion/two"),
        note_text="# Sample\n",
        resolved_links=(
            ResolvedMarkdownLink("first", "./shared.md", "kb/notes/shared.md", 800),
            ResolvedMarkdownLink("again", "./shared.md#part", "kb/notes/shared.md", 800),
        ),
    )

    telemetry = json.loads(link_availability_telemetry_json([target]))
    pairs = telemetry["commonplace"]["review_link_availability"]["pairs"]

    assert [pair["criterion_path"] for pair in pairs] == ["criterion/one", "criterion/two"]
    assert all(pair["resolved_link_count"] == 2 for pair in pairs)
    assert all(pair["distinct_artifact_count"] == 1 for pair in pairs)
    assert all(pair["total_bytes"] == 800 for pair in pairs)
