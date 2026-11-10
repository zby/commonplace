"""Publication authority binds what the operator could inspect, not merely a token."""

import sys

import pytest

from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run
from commonplace.headless.operator import approve
from commonplace.lib.review_workflows.edits import Conflict, publication


@pytest.fixture
def gate(tmp_path):
    root = tmp_path.resolve()
    (root / "note.md").write_text("original\n")
    run_dir = root / "run"
    harness = Harness(sys.executable, {"_subcommand": ["-c", "pass"]}, lambda profile: {})

    def invoke(context="first"):
        with Run(run_dir, root, Profile("fake", "m", "low"), harnesses={"fake": harness}) as run:
            return publication(run, root, "note.md", "original\n", "candidate\n",
                               inputs={"context": context}, command="repeat")

    return root, run_dir, invoke


@pytest.mark.parametrize("filename", ["publication.json", "final.md", "final.diff"])
@pytest.mark.parametrize("approved_first", [False, True])
def test_changed_inspection_files_require_fresh_approval_even_after_repeated_runs(gate, filename, approved_first):
    root, run_dir, invoke = gate
    waiting = invoke()
    if approved_first:
        approve(run_dir, "publication.json", waiting["key"])
    (run_dir / "artifact" / filename).write_text("operator saw different text\n")
    if not approved_first:
        approve(run_dir, "publication.json", waiting["key"])
    restored = invoke()
    assert restored and "withdrawn" in restored["what"]
    assert invoke() is not None, "restoring files must not resurrect the withdrawn approval"
    approve(run_dir, "publication.json", restored["key"])
    assert invoke() is None
    assert (root / "note.md").read_text() == "original\n", "the gate itself never publishes"


@pytest.mark.parametrize("filenames", [("publication.json",), ("final.md",), ("final.diff",),
                                      ("publication.json", "final.md", "final.diff")])
def test_deleted_inspection_files_cannot_restore_prior_approval(gate, filenames):
    _, run_dir, invoke = gate
    waiting = invoke()
    approve(run_dir, "publication.json", waiting["key"])
    for filename in filenames:
        (run_dir / "artifact" / filename).unlink()
    restored = invoke()
    assert restored and "withdrawn" in restored["what"]
    assert invoke() is not None
    approve(run_dir, "publication.json", restored["key"])
    assert invoke() is None


def test_identical_candidate_with_changed_context_and_stale_original_cannot_publish(gate):
    root, run_dir, invoke = gate
    first = invoke()
    approve(run_dir, "publication.json", first["key"])
    changed = invoke("second")
    assert changed and changed["key"] != first["key"]
    with pytest.raises(ValueError, match="proposal changed"):
        approve(run_dir, "publication.json", first["key"])
    approve(run_dir, "publication.json", changed["key"])
    (root / "note.md").write_text("someone else's edit\n")
    with pytest.raises(Conflict):
        invoke("second")
    assert (root / "note.md").read_text() == "someone else's edit\n"
