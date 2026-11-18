"""The one-off conversion of old operator records into kept answers, on a fixture in the old format."""

import json

import pytest
import yaml

from commonplace.lib import answers, library
from commonplace.lib.review_workflows import decisions, edits
from scripts.convert_operator_records import convert, kept_path, main
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

NOTE = "kb/notes/alpha.md"
START = "---\ndescription: A note about alpha for the conversion\ntype: note\n---\n\n# Alpha\n\nAlpha body.\n"
RUN = "kb/reports/state/review/runs/v2/revise/kb/notes/alpha/0123456789ab"
FULL_PASS = "kb/reports/state/review/runs/v2/full-pass/kb/notes/alpha/ba9876543210"
QUESTION = """---
type: types/edit-result.md
outcome: proposed
proposals:
  - {quote: Alpha body, change: alpha, reason: plain}
  - {quote: A note about, change: beta, reason: word}
---

# Report
"""


@pytest.fixture
def old(tmp_path, monkeypatch):
    """A checkout whose revise run holds operator records of the approve-and-repeat workflow."""
    root = tmp_path.resolve()
    for rel in (*NOTE_TYPE_SPECS, "kb/types/answers.md", "kb/types/answers.schema.yaml"):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text((REPO_ROOT / rel).read_text())
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    files = {NOTE: START, f"{RUN}/artifact/start.md": START,
             f"{RUN}/artifact/edits/plain-wording/result.md": QUESTION}
    question = f"{RUN}/artifact/edits/plain-wording/result.md"
    pending = answers.pending(question, QUESTION.encode())
    head, body = pending.split("---\n")[1:]
    data = yaml.safe_load(head)
    for item, state in zip(data["items"], ("approved", "rejected"), strict=True):
        item.update({"state": state, "decided-by": "operator", "decided-at": "2026-11-10T09:00:00Z"})
        if state == "rejected":
            item["reason"] = "a registered word"
    answered = "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n" + body
    name = "plain-wording-answers-0123456789ab.md"
    files[f"{RUN}/artifact/{name}"] = answered
    files[f"{RUN}/operator/1.json"] = json.dumps({"name": name, "input-key": "i", "proposal": pending, "key": "k1",
                                                  "answer": answered, "answered-at": "2026-11-10T09:05:00Z"})
    files[f"{RUN}/operator/2.json"] = json.dumps({"name": "abstractions-answers-0123456789ab.md", "input-key": "i",
                                                  "proposal": pending, "key": "k2"})
    files[f"{FULL_PASS}/operator/1.json"] = json.dumps({"name": "plan.yaml", "input-key": "i", "proposal": "p",
                                                        "key": "k3"})
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    return root, answered


def snapshot(root):
    return {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob("*") if path.is_file()}


def test_a_dry_run_reports_and_writes_nothing(old, capsys):
    root, _ = old
    before = snapshot(root)
    assert main(["--root", str(root), "--dry-run"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["dry-run"] and [c["record"] for c in report["converted"]] == [f"{RUN}/operator/1.json"]
    assert report["left-unanswered"] == [f"{RUN}/operator/2.json"] and report["started"] == [RUN]
    assert snapshot(root) == before


def test_answered_records_become_kept_answers_that_the_readers_take(old):
    root, answered = old
    report = convert(root)
    assert not report["problems"]
    [(record, kept)] = decisions.kept_answers(root, root / RUN)
    origin = f"{RUN}/artifact/plain-wording-answers-0123456789ab.md"
    assert kept == {"origin": origin, "sha256": answers.sha(answered.encode()), "at": "2026-11-10T09:05:00Z",
                    "text": answered}
    assert record == report["converted"][0]["kept"]
    assert not (root / RUN / "operator/1.json").exists() and (root / RUN / "operator/2.json").is_file()
    assert (root / FULL_PASS / "operator/1.json").is_file(), "full-pass records stay for the BACKCOMPAT reader"
    assert json.loads((root / RUN / edits.START_RECORD).read_text()) == {
        "note": NOTE, "sha256": answers.sha(START.encode()), "brief-sha256": None}
    found = {d["proposal"]["change"]: (d["state"], d["answers-file"]) for d in decisions.earlier(root, NOTE)}
    assert found == {"alpha": ("approved", origin), "beta": ("rejected", origin)}
    listed = [(e["class"], e["decision"]) for e in decisions.entries(root) if e["workflow"] == "revise"]
    assert sorted(listed) == [("plain-wording", "approved"), ("plain-wording", "rejected")]
    assert convert(root)["converted"] == [], "a second conversion finds nothing more"


def test_the_kept_path_is_the_one_keep_answers_writes(tmp_path):
    origin = f"{RUN}/artifact/plain-wording-answers.md"
    assert decisions.keep_answers(tmp_path, origin, "text") == kept_path(tmp_path, origin)
