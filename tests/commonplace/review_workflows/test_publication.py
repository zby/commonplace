"""Publication authority binds what the operator could inspect: answers that approve the exact candidate."""

import sys

import pytest
import yaml

from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run
from commonplace.headless.operator import approve
from commonplace.lib import library
from commonplace.lib.review_workflows.edits import (
    PUBLICATION,
    Conflict,
    apply,
    publication,
)
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT


@pytest.fixture
def gate(tmp_path, monkeypatch):
    root = tmp_path.resolve()
    for rel in (*NOTE_TYPE_SPECS, "kb/types/answers.md", "kb/types/answers.schema.yaml"):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text((REPO_ROOT / rel).read_text())
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    (root / "note.md").write_text("original\n")
    run_dir = root / "run"
    harness = Harness(sys.executable, {"_subcommand": ["-c", "pass"]}, lambda profile: {})

    def invoke(context="first"):
        with Run(run_dir, root, Profile("fake", "m", "low"), harnesses={"fake": harness}) as run:
            return publication(run, root, "note.md", "original\n", "candidate\n",
                               inputs={"context": context}, command="repeat", change="change the inputs")

    return root, run_dir, invoke


def answer(run_dir, state="approved", **fields):
    """Record the operator's decision on the publication item, as the approve-a-text stop does."""
    path = run_dir / "artifact" / PUBLICATION
    head, body = path.read_text().split("---\n")[1:]
    data = yaml.safe_load(head)
    data["items"][0].update({"state": state, "decided-by": "operator", "decided-at": "2026-11-15T12:00:00Z",
                             **fields})
    path.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n" + body)


def test_the_stop_is_a_pending_answers_file_over_the_candidate(gate):
    root, run_dir, invoke = gate
    waiting = invoke()
    assert waiting["file"] == f"run/artifact/{PUBLICATION}"
    data = yaml.safe_load((run_dir / "artifact" / PUBLICATION).read_text().split("---\n")[1])
    assert data["question"] == "run/artifact/final.md"
    [item] = data["items"]
    assert item["id"] == "text" and item["state"] == "pending"
    assert item["proposal"]["text"] == "run/artifact/final.md"
    approve(run_dir, PUBLICATION, waiting["key"])
    assert "answer is `pending`" in invoke()["what"], "an approved file must also approve the item"
    answer(run_dir)
    approve(run_dir, PUBLICATION, waiting["key"])
    assert invoke() is None
    assert (root / "note.md").read_text() == "original\n", "the gate itself never publishes"


def test_a_rejection_does_not_authorize_publication(gate):
    _, run_dir, invoke = gate
    waiting = invoke()
    answer(run_dir, "rejected", reason="the closing reads worse")
    approve(run_dir, PUBLICATION, waiting["key"])
    assert "answer is `rejected`: the closing reads worse" in invoke()["what"]


def test_answers_naming_another_hash_do_not_authorize_publication(gate):
    _, run_dir, invoke = gate
    waiting = invoke()
    answer(run_dir)
    path = run_dir / "artifact" / PUBLICATION
    data = yaml.safe_load(path.read_text().split("---\n")[1])
    path.write_text(path.read_text().replace(data["items"][0]["proposal"]["text-sha256"], "0" * 64))
    approve(run_dir, PUBLICATION, waiting["key"])
    refused = invoke()
    assert "do not authorize publication" in refused["what"] and "question-sha256" in refused["what"]


@pytest.mark.parametrize("filename", [PUBLICATION, "final.md", "final.diff"])
def test_changed_inspection_files_after_approval_withdraw_it(gate, filename):
    _, run_dir, invoke = gate
    waiting = invoke()
    answer(run_dir)
    approve(run_dir, PUBLICATION, waiting["key"])
    (run_dir / "artifact" / filename).write_text("operator saw different text\n")
    restored = invoke()
    assert restored and "withdrawn" in restored["what"]
    assert invoke() is not None, "restoring files must not resurrect the withdrawn approval"
    answer(run_dir)
    approve(run_dir, PUBLICATION, restored["key"])
    assert invoke() is None


@pytest.mark.parametrize("filenames", [(PUBLICATION,), ("final.md",), ("final.diff",),
                                      (PUBLICATION, "final.md", "final.diff")])
def test_deleted_inspection_files_cannot_restore_prior_approval(gate, filenames):
    _, run_dir, invoke = gate
    waiting = invoke()
    answer(run_dir)
    approve(run_dir, PUBLICATION, waiting["key"])
    for filename in filenames:
        (run_dir / "artifact" / filename).unlink()
    restored = invoke()
    assert restored and "withdrawn" in restored["what"]
    assert invoke() is not None
    answer(run_dir)
    approve(run_dir, PUBLICATION, restored["key"])
    assert invoke() is None


def test_identical_candidate_with_changed_context_and_stale_original_cannot_publish(gate):
    root, run_dir, invoke = gate
    first = invoke()
    answer(run_dir)
    approve(run_dir, PUBLICATION, first["key"])
    changed = invoke("second")
    assert changed and changed["key"] != first["key"]
    with pytest.raises(ValueError, match="proposal changed"):
        approve(run_dir, PUBLICATION, first["key"])
    answer(run_dir)
    approve(run_dir, PUBLICATION, changed["key"])
    (root / "note.md").write_text("someone else's edit\n")
    with pytest.raises(Conflict):
        invoke("second")
    assert (root / "note.md").read_text() == "someone else's edit\n"


def test_apply_writes_only_from_the_start_text(tmp_path):
    note, proposed = tmp_path / "note.md", tmp_path / "proposed.md"
    note.write_text("start")
    apply(tmp_path, "note.md", "start", "final", proposed)
    assert note.read_text() == "final"
    note.write_text("other")
    with pytest.raises(Conflict, match="proposed.md"):
        apply(tmp_path, "note.md", "start", "final", proposed)
    assert note.read_text() == "other"
