"""Exact membership and traversal boundaries for collection-grouped tag lists."""

import os
from pathlib import Path

import pytest

from commonplace.lib.index_generated import (
    collect_tag_space,
    generated_section_for_head,
)
from tests.commonplace.validation_helpers import write


def test_collector_never_enters_workflow_state_or_source_snapshots(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    kb = tmp_path / "kb"
    for collection in ("sources", "workflow-state", "new-collection", "tags"):
        write(kb / collection / "COLLECTION.md", "# Collection\n")
    tagged = "---\ntags: [topic, topic]\n---\n\n# Example\n"
    member = write(kb / "sources/source.ingest.md", tagged)
    other = write(kb / "new-collection/example.md", tagged)
    head = write(kb / "tags/topic-README.md", "# Topic\n")
    private = {kb / "workflow-state", kb / "sources/.snapshots"}
    for directory in private:
        write(directory / "nested/private.md", tagged)
    scandir = os.scandir

    def guarded(path):
        assert Path(path) not in private, f"entered private tree: {path}"
        return scandir(path)

    monkeypatch.setattr(os, "scandir", guarded)
    space = collect_tag_space(tmp_path)
    assert [p for p, _, _ in space.notes_by_tag["topic"]] == [other, member]
    assert all(not space.is_member_candidate(p / "nested/private.md") for p in private)
    listing = generated_section_for_head(head, tag_space=space)
    assert "### sources" in listing and "### new-collection" in listing
    assert "private" not in listing
    site = generated_section_for_head(head, tag_space=space, published=lambda p: p == member)
    assert "[Example](../sources/source.ingest.md)" in site
    assert "Example (`new-collection/example.md`)" in site
