"""The answers type's deterministic acceptance: the schema and the comparison with the question."""

from __future__ import annotations

import subprocess

import pytest
import yaml

from commonplace.lib import answers, library
from commonplace.lib.review_workflows.edits import answered
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

QUESTION = "kb/reports/state/run/result.md"
PROPOSALS = [{"quote": "Alpha body", "change": "ALPHA BODY", "reason": "plainer"},
             {"quote": "Closing sentence", "change": "End", "reason": "shorter"}]
RESULT = ("---\n" + yaml.safe_dump({"type": "types/edit-result.md", "outcome": "proposed", "proposals": PROPOSALS},
                                   sort_keys=False) + "---\n\n# Report\n\nTwo proposals.\n")
DECIDED = {"decided-by": "operator", "decided-at": "2026-11-15T12:00:00Z"}


@pytest.fixture
def root(tmp_path, monkeypatch):
    root = tmp_path.resolve()
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    for rel in (*NOTE_TYPE_SPECS, "kb/types/answers.md", "kb/types/answers.schema.yaml"):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text((REPO_ROOT / rel).read_text())
    (root / QUESTION).parent.mkdir(parents=True)
    (root / QUESTION).write_text(RESULT)
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    return root


def render(data: dict) -> str:
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# Answers\n"


def check(root, data: dict) -> list[str]:
    path = root / "kb/reports/state/run/result-answers.md"
    _, fails = answered(root, path, render(data))
    return fails


def valid(root) -> dict:
    data = yaml.safe_load(answers.pending(QUESTION, (root / QUESTION).read_bytes()).split("---\n")[1])
    data["items"][0].update({"state": "approved", **DECIDED})
    data["items"][1].update({"state": "deferred", "reason": "the term may be registered",
                             "revisit": "when the vocabulary ledger decides", **DECIDED})
    return data


def test_pending_answers_name_the_question_and_copy_each_item(root):
    data = yaml.safe_load(answers.pending(QUESTION, (root / QUESTION).read_bytes()).split("---\n")[1])
    assert data["question"] == QUESTION and data["question-sha256"] == answers.sha((root / QUESTION).read_bytes())
    assert data["items"] == [{"id": "1", "proposal": PROPOSALS[0], "state": "pending"},
                             {"id": "2", "proposal": PROPOSALS[1], "state": "pending"}]
    assert check(root, data) == []


def test_decided_answers_pass(root):
    assert check(root, valid(root)) == []


def _altered(data):
    data["items"][0]["proposal"]["change"] = "Alpha"


def _missing(data):
    del data["items"][1]


def _repeated(data):
    data["items"].append(dict(data["items"][0]))


def _added(data):
    data["items"].append({"id": "3", "proposal": {"quote": "x"}, "state": "pending"})


def _no_reason(data):
    data["items"][0].update({"state": "rejected"})


def _no_revisit(data):
    del data["items"][1]["revisit"]


def _decider(data):
    data["items"][0]["decided-by"] = "agent"


def _undated(data):
    del data["items"][0]["decided-at"]


def _pending_decided(data):
    data["items"][0]["state"] = "pending"


def _state(data):
    data["items"][0]["state"] = "struck"


def _hash(data):
    data["question-sha256"] = "0" * 64


@pytest.mark.parametrize("change, problem", [
    (_altered, "item 1: its proposal differs from the question's"),
    (_missing, "item 2: missing"),
    (_repeated, "item 1: appears 2 times"),
    (_added, "item 3: not in the question"),
    (_no_reason, "'reason' is a required property"),
    (_no_revisit, "'revisit' is a required property"),
    (_decider, "'operator' was expected"),
    (_undated, "'decided-at' is a required property"),
    (_pending_decided, "items.0: forbidden combination of fields"),
    (_state, "'struck' is not one of"),
    (_hash, "question-sha256: the question file has changed"),
])
def test_each_broken_answers_file_is_refused(root, change, problem):
    data = valid(root)
    change(data)
    fails = check(root, data)
    assert any(problem in fail for fail in fails), fails


def test_a_changed_question_is_refused(root):
    data = valid(root)
    (root / QUESTION).write_text(RESULT.replace("Two proposals.", "Two proposals, edited."))
    assert any("question-sha256" in fail for fail in check(root, data))


def test_a_text_question_has_one_item_naming_its_hash(root):
    text = "kb/reports/state/run/final.md"
    (root / text).write_text("candidate\n")
    data = yaml.safe_load(answers.pending(text, b"candidate\n").split("---\n")[1])
    assert data["items"] == [{"id": "text", "proposal": {"text": text, "text-sha256": answers.sha(b"candidate\n")},
                              "state": "pending"}]
    data["items"][0].update({"state": "approved", **DECIDED})
    assert check(root, data) == []
    data["items"][0]["proposal"]["text-sha256"] = "0" * 64
    assert any("item text: its proposal differs" in fail for fail in check(root, data))


def test_an_edit_result_that_proposes_nothing_is_no_question(root):
    (root / QUESTION).write_text(RESULT.replace("outcome: proposed", "outcome: unchanged"))
    with pytest.raises(ValueError, match="only with outcome `proposed`"):
        answers.pending(QUESTION, (root / QUESTION).read_bytes())
