"""`operator.answer()` and `operator.waiting()`; no worker is launched."""

import sys

import pytest

from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run
from commonplace.headless.operator import answer, waiting


@pytest.fixture
def run(tmp_path):
    harness = Harness(sys.executable, {"_subcommand": ["-c", "pass"]}, lambda profile: {})
    with Run(tmp_path / "run", tmp_path, Profile("fake", "m", "low"), harnesses={"fake": harness},
             sleep=lambda s: None) as run:
        yield run


def test_a_missing_file_gets_the_proposal_and_the_workflow_waits(run):
    assert answer(run, "plan.yaml", lambda: "proposed\n") is None
    assert (run.artifact / "plan.yaml").read_text() == "proposed\n"


def test_an_existing_file_is_the_answer_edited_or_not(run):
    answer(run, "plan.yaml", lambda: "proposed\n")
    assert answer(run, "plan.yaml", lambda: "another\n") == "proposed\n"
    (run.artifact / "plan.yaml").write_text("edited\n")
    assert answer(run, "plan.yaml", lambda: "another\n") == "edited\n"


def test_a_file_put_in_place_first_asks_for_no_proposal(run):
    run.artifact.mkdir(parents=True, exist_ok=True)
    (run.artifact / "plan.yaml").write_text("given\n")

    def propose() -> str:
        raise AssertionError("no proposal is needed")
    assert answer(run, "plan.yaml", propose) == "given\n"


def test_waiting_names_the_file_from_the_repository_root(run, tmp_path):
    assert waiting(run, tmp_path, "plan.yaml", "Edit the plan.", "repeat it") == {
        "what": "Edit the plan.", "file": "run/artifact/plan.yaml", "command": "repeat it"}
