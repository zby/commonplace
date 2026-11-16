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


def test_a_decided_item_takes_a_resolution_and_refs_and_a_pending_item_does_not(root):
    data = valid(root)
    data["items"][0].update({"resolution": "rewrote the note", "refs": ["0123abc", "kb/work/some-workshop"]})
    assert check(root, data) == []
    data = yaml.safe_load(answers.pending(QUESTION, (root / QUESTION).read_bytes()).split("---\n")[1])
    data["items"][0]["refs"] = ["0123abc"]
    assert check(root, data)


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


# --- A review result as the question: a triage ----------------------------------------------

FINDINGS = [{"scope": "passage", "quotes": ["Alpha body"], "reason": "residue", "level": "warn"},
            {"scope": "document", "quotes": [], "reason": "a remark", "level": "info"},
            {"scope": "document", "quotes": [], "reason": "missing condition", "level": "fail"}]
REVIEW = "kb/reports/state/run/findings/prose/residue.md"


def review(outcome="fail", found=FINDINGS):
    data = {"type": "types/review-result.md", "note": "kb/notes/alpha.md",
            "criterion": "kb/instructions/review-gates/prose/residue.md", "findings": found, "outcome": outcome}
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# Review\n\nFound.\n"


def test_a_review_result_asks_about_its_warn_and_fail_findings_by_position(root):
    (root / REVIEW).parent.mkdir(parents=True)
    (root / REVIEW).write_text(review())
    data = yaml.safe_load(answers.pending(REVIEW, (root / REVIEW).read_bytes()).split("---\n")[1])
    assert data["items"] == [{"id": "1", "proposal": FINDINGS[0], "state": "pending"},
                             {"id": "3", "proposal": FINDINGS[2], "state": "pending"}]   # the info finding is no item
    assert check(root, data) == []
    data["items"][0].update({"state": "rejected", "reason": "wrong for this note only", **DECIDED})
    data["items"][1].update({"state": "approved", **DECIDED})
    assert check(root, data) == []
    data["items"][0]["proposal"]["reason"] = "edited"
    assert any("item 1: its proposal differs" in fail for fail in check(root, data))
    data["items"][0]["proposal"]["reason"] = "residue"
    data["items"].append({"id": "2", "proposal": FINDINGS[1], "state": "pending"})
    assert any("item 2: not in the question" in fail for fail in check(root, data))


@pytest.mark.parametrize("outcome, found", [("pass", []), ("report", FINDINGS[:1]), ("warn", FINDINGS[1:2])])
def test_a_review_result_without_a_warn_or_fail_finding_is_no_question(root, outcome, found):
    (root / REVIEW).parent.mkdir(parents=True)
    (root / REVIEW).write_text(review(outcome, found))
    with pytest.raises(ValueError, match="a review result is a question only with outcome `warn` or `fail`"):
        answers.pending(REVIEW, (root / REVIEW).read_bytes())
    data = {"type": "types/answers.md", "description": "d", "question": REVIEW,
            "question-sha256": answers.sha((root / REVIEW).read_bytes()),
            "items": [{"id": "1", "proposal": FINDINGS[0], "state": "pending"}]}
    assert any("a review result is a question only" in fail for fail in check(root, data))
