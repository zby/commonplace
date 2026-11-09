"""Contracts of the review result files that the gates workflow and `status` build on."""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library
from commonplace.lib.review_workflows.results import (
    Freshness,
    Summary,
    criterion_id,
    make_result,
    orphaned,
    read_result,
    result_path,
    status,
    stored,
    summarize,
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


def _review(root: Path, note: str, criterion: str, outcome: str = "pass", body: str = "## Result: PASS\n",
            criterion_text: str | None = None):
    if criterion_text is None:
        criterion_text = (root / criterion).read_text(encoding="utf-8")
    result = make_result(
        note, (root / note).read_text(encoding="utf-8"), criterion, criterion_text,
        outcome=outcome, profile={"harness": "claude", "launch-model": "sonnet", "effort": "low"},
        model="claude-sonnet-x", run="20261109T000000Z", launch="L1", completed_at="2026-11-09T00:00:00Z",
        body=body)
    return result, write_result(root, result)


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    # A Commonplace checkout: the library is the repository's own kb/.
    monkeypatch.setattr(library, "_library_root", lambda _override: (tmp_path / "kb").resolve())
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


def test_summary_counts_each_stored_result_once(repo: Path) -> None:
    second = "kb/notes/beta.md"
    _write(repo, second, NOTE_TEXT.replace("Alpha", "Beta"))
    _review(repo, NOTE, GATE, outcome="warn", body="## Result: WARN\n")
    _review(repo, NOTE, OTHER_GATE, outcome="fail", body="## Result: FAIL\n")
    _review(repo, NOTE, TYPE_SPEC)
    _, gone = _review(repo, second, GATE, outcome="warn", body="## Result: WARN\n")
    _edit(repo, OTHER_GATE, "Flag", "Strictly flag")                       # the fail is no longer current
    (repo / second).unlink()
    rows, orphans = stored(repo)
    assert orphans == [gone]
    assert {(row.criterion, row.freshness.state, row.outcome) for row in rows} == {
        (GATE, "fresh", "warn"), (OTHER_GATE, "stale", "fail"), (TYPE_SPEC, "fresh", "pass")}
    assert all(row.path is not None and read_result(row.path).criterion == row.criterion for row in rows)
    assert summarize(repo) == Summary(results=4, fresh=2, stale=1, orphaned=1, warn=1, fail=0)


def test_summary_of_a_project_without_results_is_empty(repo: Path) -> None:
    assert summarize(repo) == Summary()


def test_installed_library_criteria_are_library_identities(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # An installed project: the library lies outside the repository and its files are `commonplace:` identities.
    root, lib = tmp_path / "project", tmp_path / "share" / "commonplace"
    _write(root, NOTE, NOTE_TEXT)
    _write(lib, "instructions/review-gates/prose/residue.md", GATE_TEXT)
    _write(lib, "types/note.md", "# Note type\n")
    monkeypatch.setattr(library, "_library_root", lambda _override: lib.resolve())
    gate, spec = "commonplace:instructions/review-gates/prose/residue.md", "commonplace:types/note.md"
    assert criterion_id(root, gate) == "prose/residue"
    assert criterion_id(root, spec) == "commonplace/types/note"
    assert criterion_id(root, "kb/notes/types/claim.md") == "kb/notes/types/claim"

    _, path = _review(root, NOTE, gate, criterion_text=GATE_TEXT)
    assert path == result_path(root, NOTE, "prose/residue")
    assert read_result(path).criterion == gate
    _review(root, NOTE, spec, criterion_text="# Note type\n")
    assert _states(root, [(NOTE, gate), (NOTE, spec)]) == [Freshness("fresh")] * 2
    _edit(lib, "instructions/review-gates/prose/residue.md", "Flag", "Strictly flag")
    assert _states(root, [(NOTE, gate)]) == [Freshness("stale", ("criterion",))]
    (lib / "types/note.md").unlink()
    assert orphaned(root) == [result_path(root, NOTE, "commonplace/types/note")]
    with pytest.raises(ValueError):
        criterion_id(root, "commonplace:../escape.md")
