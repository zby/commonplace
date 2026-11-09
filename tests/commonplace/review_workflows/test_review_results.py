"""Contracts of the review result files that the gates workflow and `status` build on."""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.review_workflows.results import (
    Freshness,
    make_result,
    orphaned,
    read_result,
    result_path,
    status,
    write_result,
)

NOTE = "kb/notes/alpha.md"
GATE = "kb/instructions/review-gates/prose/residue.md"
OTHER_GATE = "kb/instructions/review-gates/prose/hedging.md"
TYPE_SPEC = "kb/types/note.md"

NOTE_TEXT = """---
description: Alpha in one line
status: seedling
---

# Alpha

Body paragraph.
"""

GATE_TEXT = """---
watches: [body]
---

# Residue

Flag source residue.
"""


def _write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _edit(root: Path, rel: str, old: str, new: str) -> None:
    path = root / rel
    path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")


def _review(root: Path, note: str, criterion: str, outcome: str = "pass", body: str = "## Result: PASS\n"):
    result = make_result(
        note, (root / note).read_text(encoding="utf-8"), criterion, (root / criterion).read_text(encoding="utf-8"),
        outcome=outcome, profile={"harness": "claude", "launch-model": "sonnet", "effort": "low"},
        model="claude-sonnet-x", run="20261109T000000Z", launch="L1", completed_at="2026-11-09T00:00:00Z",
        body=body)
    return result, write_result(root, result)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    _write(tmp_path, NOTE, NOTE_TEXT)
    _write(tmp_path, GATE, GATE_TEXT)
    _write(tmp_path, OTHER_GATE, GATE_TEXT.replace("Residue", "Hedging"))
    _write(tmp_path, TYPE_SPEC, "# Note type\n\nNo watches declared.\n")
    return tmp_path


def _states(root: Path, pairs) -> list[Freshness]:
    return [row.freshness for row in status(root, pairs)]


def test_written_result_reads_back_equal_at_its_pair_path(repo: Path) -> None:
    # The body keeps CRLF and frontmatter-like text: the reviewer's text must survive unchanged.
    result, path = _review(repo, NOTE, GATE, outcome="warn", body="## Result: WARN\r\n---\nnot: frontmatter\n")
    assert path == repo / "kb/reports/state/review/results/kb/notes/alpha.md/prose/residue.md"
    assert read_result(path) == result
    [row] = status(repo, [(NOTE, GATE)])
    assert (row.freshness, row.outcome, row.model) == (Freshness("fresh"), "warn", "claude-sonnet-x")
    assert row.profile["launch-model"] == "sonnet"


def test_note_edit_stales_only_criteria_that_watch_the_edited_part(repo: Path) -> None:
    _review(repo, NOTE, GATE)
    _review(repo, NOTE, TYPE_SPEC)
    # Description and other frontmatter are outside a body-only gate's watches.
    _edit(repo, NOTE, "Alpha in one line", "Alpha, restated")
    _edit(repo, NOTE, "seedling", "current")
    assert _states(repo, [(NOTE, GATE), (NOTE, TYPE_SPEC)]) == [
        Freshness("fresh"), Freshness("stale", ("note",))]
    _edit(repo, NOTE, "Body paragraph.", "Changed body.")
    assert _states(repo, [(NOTE, GATE)]) == [Freshness("stale", ("note",))]


def test_part_content_cannot_forge_a_part_boundary(repo: Path) -> None:
    gate = "kb/instructions/review-gates/prose/both.md"
    _write(repo, gate, "---\nwatches: [title, body]\n---\n\n# Both\n")
    _write(repo, NOTE, "---\ndescription: d\n---\n\n# A\n\nB C\n")
    _review(repo, NOTE, gate)
    # Moving text between title and body must not keep the same hash input.
    _write(repo, NOTE, "---\ndescription: d\n---\n\n# A B\n\nC\n")
    assert _states(repo, [(NOTE, gate)]) == [Freshness("stale", ("note",))]


def test_criterion_edit_stales_exactly_its_pairs_and_both_changes_are_reported(repo: Path) -> None:
    second = "kb/notes/beta.md"
    _write(repo, second, NOTE_TEXT.replace("Alpha", "Beta"))
    pairs = [(NOTE, GATE), (second, GATE), (NOTE, OTHER_GATE)]
    for note, criterion in pairs:
        _review(repo, note, criterion)
    _edit(repo, GATE, "Flag source residue.", "Flag source residue strictly.")
    assert _states(repo, pairs) == [Freshness("stale", ("criterion",))] * 2 + [Freshness("fresh")]
    _edit(repo, NOTE, "Body paragraph.", "Changed body.")
    assert _states(repo, [(NOTE, GATE)]) == [Freshness("stale", ("note", "criterion"))]
    assert _states(repo, [(NOTE, TYPE_SPEC)]) == [Freshness("missing")]


def test_unparseable_result_file_raises_with_its_path(repo: Path) -> None:
    _, path = _review(repo, NOTE, GATE)
    path.write_text("---\noutcome: [unclosed\n---\n", encoding="utf-8")
    with pytest.raises(ValueError, match="residue.md"):
        status(repo, [(NOTE, GATE)])


@pytest.mark.parametrize(("note", "criterion_id"), [
    ("../outside.md", "prose/residue"),
    ("/etc/passwd", "prose/residue"),
    (NOTE, "../../../../../../../escape"),
])
def test_paths_escaping_the_results_root_are_refused(repo: Path, note: str, criterion_id: str) -> None:
    with pytest.raises(ValueError):
        result_path(repo, note, criterion_id)


def test_orphaned_finds_results_whose_note_or_criterion_is_gone(repo: Path) -> None:
    _, kept = _review(repo, NOTE, OTHER_GATE)
    _, by_note = _review(repo, NOTE, GATE)
    second = "kb/notes/beta.md"
    _write(repo, second, NOTE_TEXT)
    _, gone = _review(repo, second, GATE)
    (repo / second).unlink()
    assert orphaned(repo) == [gone]
    (repo / OTHER_GATE).unlink()
    assert orphaned(repo) == sorted([gone, kept])
    assert by_note.is_file()
