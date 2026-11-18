"""Publishing a held candidate: only the exact candidate, only over the run's start text, under the same brief."""

import json
import sys

import pytest

from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run
from commonplace.lib import library
from commonplace.lib.review_workflows import edits
from commonplace.lib.review_workflows.edits import Conflict, apply
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

NOTE = "kb/notes/note.md"
START = "---\ndescription: The start text of the note under test\ntype: note\n---\n\n# Note\n\noriginal\n"
FINAL = START.replace("original", "candidate")


@pytest.fixture
def held(tmp_path, monkeypatch):
    """A run that held FINAL over START, as a revise run holds a candidate with a new warning."""
    root = tmp_path.resolve()
    for rel in (*NOTE_TYPE_SPECS, "kb/types/answers.md", "kb/types/answers.schema.yaml"):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text((REPO_ROOT / rel).read_text())
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    (root / NOTE).parent.mkdir(parents=True, exist_ok=True)
    (root / NOTE).write_text(START)
    run_dir = edits.new_run_dir(root, "revise", NOTE)
    harness = Harness(sys.executable, {"_subcommand": ["-c", "pass"]}, lambda profile: {})
    edits.begin(run_dir, NOTE, START, {})
    with Run(run_dir, root, Profile("fake", "m", "low"), harnesses={"fake": harness}) as run:
        run.accept(edits.START, START)
        report = edits.hold(run, root, NOTE, START, FINAL, ["plain-wording"])
    return root, run_dir, report


def test_a_run_directory_is_a_timestamp_under_the_note(held):
    root, run_dir, _ = held
    assert run_dir.parent == root / "kb/reports/state/review/runs/v2/revise/kb/notes/note"
    assert len(run_dir.name) == len("20261118T120000Z") and run_dir.name.endswith("Z")
    second = edits.new_run_dir(root, "revise", NOTE)
    assert second.parent == run_dir.parent and second != run_dir
    start = json.loads((run_dir / edits.START_RECORD).read_text())
    assert start == {"note": NOTE, "sha256": edits.sha256(START), "brief-sha256": None}


def test_holding_writes_nothing_and_names_the_command(held):
    root, run_dir, report = held
    rel = run_dir.relative_to(root).as_posix()
    assert (root / NOTE).read_text() == START
    assert report["candidate"] == f"{rel}/artifact/final.md"
    assert report["command"] == f"commonplace-review publish {rel}"
    assert report["revised-command"] == f"commonplace-review publish {rel} --revised FILE"
    assert edits.published(run_dir) is None


def test_publishing_writes_the_exact_candidate_once(held):
    root, run_dir, _ = held
    report = edits.publish_held(root, run_dir)
    assert (root / NOTE).read_text() == FINAL
    entry = report["published"]
    assert entry["decided-by"] == "operator" and entry["revised"] is False
    assert entry["sha256"] == edits.sha256(FINAL) and entry["before-sha256"] == edits.sha256(START)
    assert entry["entries"] == ["plain-wording"]
    assert (root / entry["text"]).read_text() == FINAL
    assert edits.made_for(run_dir) == edits.sha256(FINAL)
    with pytest.raises(ValueError, match="already published"):
        edits.publish_held(root, run_dir)


def test_a_changed_note_refuses_publication(held):
    root, run_dir, _ = held
    (root / NOTE).write_text(START + "someone else's edit\n")
    with pytest.raises(ValueError, match="no longer holds the text the run started from"):
        edits.publish_held(root, run_dir)
    assert (root / NOTE).read_text() == START + "someone else's edit\n"
    assert edits.published(run_dir) is None


@pytest.mark.parametrize("filename", ["final.md", "start.md"])
def test_a_changed_run_file_refuses_publication(held, filename):
    root, run_dir, _ = held
    (run_dir / "artifact" / filename).write_text("operator saw different text\n")
    with pytest.raises(ValueError):
        edits.publish_held(root, run_dir)
    assert (root / NOTE).read_text() == START


def test_a_deleted_candidate_cannot_be_published(held):
    root, run_dir, _ = held
    (run_dir / "artifact" / "final.md").unlink()
    with pytest.raises(FileNotFoundError):
        edits.publish_held(root, run_dir)
    assert (root / NOTE).read_text() == START


def test_a_changed_brief_refuses_publication(held):
    root, run_dir, _ = held
    record = json.loads((run_dir / edits.START_RECORD).read_text())
    record["brief-sha256"] = "0" * 64
    (run_dir / edits.START_RECORD).write_text(json.dumps(record))
    with pytest.raises(ValueError, match="write brief"):
        edits.publish_held(root, run_dir)
    assert (root / NOTE).read_text() == START


def test_a_revised_text_is_published_after_the_candidate_checks(held, tmp_path):
    root, run_dir, _ = held
    source = tmp_path / "revised.md"
    revised = FINAL.replace("candidate", "operator's text")
    source.write_text(revised)
    with pytest.raises(ValueError, match="H1"):
        edits.publish_held(root, run_dir, revised.replace("# Note", "# Other"), source)
    with pytest.raises(ValueError, match="current text"):
        edits.publish_held(root, run_dir, START, source)
    with pytest.raises(ValueError, match="outside the run's artifact"):
        edits.publish_held(root, run_dir, revised, run_dir / "artifact" / "mine.md")
    assert (root / NOTE).read_text() == START
    report = edits.publish_held(root, run_dir, revised, source)
    assert (root / NOTE).read_text() == revised
    assert report["published"]["revised"] is True
    assert (root / report["revised-candidate"]["revised"]).read_text() == revised
    assert "operator's text" in (root / report["revised-candidate"]["diff-from-candidate"]).read_text()
    assert (root / report["revised-candidate"]["candidate"]).read_text() == FINAL


def test_a_run_that_held_nothing_cannot_publish(held):
    root, run_dir, _ = held
    (run_dir / edits.HELD).unlink()
    with pytest.raises(ValueError, match="holds no candidate"):
        edits.publish_held(root, run_dir)


def test_apply_writes_only_from_the_start_text(tmp_path):
    note, proposed = tmp_path / "note.md", tmp_path / "proposed.md"
    note.write_text("start")
    apply(tmp_path, "note.md", "start", "final", proposed)
    assert note.read_text() == "final"
    note.write_text("other")
    with pytest.raises(Conflict, match="proposed.md"):
        apply(tmp_path, "note.md", "start", "final", proposed)
    assert note.read_text() == "other"
