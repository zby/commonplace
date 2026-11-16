"""The operator-decision record: a read-only listing over run records, packets and fix reports."""

import json

import pytest
import yaml

from commonplace.cli import review_workflows as cli
from commonplace.lib.review_workflows import decisions

NOTE = "kb/theory/foo.md"
RUN = "kb/reports/state/review/runs/v2/revise/kb/theory/foo/0123456789ab"
DECIDED = {"decided-by": "operator", "decided-at": "2026-11-12T10:00:00Z"}
ITEMS = [{"id": "1", "proposal": {"quote": "first entry", "change": "kept", "reason": "plain"}},
         {"id": "2", "proposal": {"quote": "second entry", "change": "rejected", "reason": "plain"}},
         {"id": "3", "proposal": {"quote": "third entry", "change": "deferred", "reason": "plain"}}]
DECISIONS = [{"state": "approved", **DECIDED},
             {"state": "rejected", "reason": "changes the claim", **DECIDED},
             {"state": "deferred", "reason": "the term may be registered", "revisit": "when the ledger decides",
              **DECIDED}]
TEXT = {"id": "text", "proposal": {"text": f"{RUN}/artifact/final.md", "text-sha256": "1" * 64}}


def answers(items):
    data = {"type": "types/answers.md", "description": "d", "question": f"{RUN}/artifact/question.md",
            "question-sha256": "0" * 64, "items": items}
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# Answers\n"


PENDING = answers([{**item, "state": "pending"} for item in ITEMS])
ANSWER = answers([{**item, **decision} for item, decision in zip(ITEMS, DECISIONS, strict=True)])


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def record(root, run, file, name, proposal, answer=None, at=None, key="k"):
    data = {"name": name, "input-key": "inputs", "proposal": proposal, "key": key}
    if answer is not None:
        data |= {"answer": answer, "answered-at": at}
    write(root, f"{run}/operator/{file}.json", json.dumps(data))


PACKET = """---
note: {note}
run: kb/reports/state/review/runs/v2/full-pass/kb/theory/bar/aaaaaaaaaaaa
disposition: revise
resolution: {resolution}
resolution-authority: {authority}
resolved-at: {at}
resolution-summary: {summary}
---

# Full Improvement Pass
"""


@pytest.fixture
def repo(tmp_path, monkeypatch):
    root = tmp_path
    record(root, RUN, "a", "plain-wording-answers-0123456789ab.md", PENDING, ANSWER, "2026-11-12T10:05:00Z",
           "list-key")
    record(root, RUN, "b", "abstractions-answers-0123456789ab.md", PENDING)
    record(root, RUN, "c", "publication-answers.md", answers([{**TEXT, "state": "pending"}]),
           answers([{**TEXT, "state": "approved", "decided-by": "operator", "decided-at": "2026-11-12T11:00:00Z"}]),
           "2026-11-12T11:00:05Z", "pub-key")
    write(root, "kb/reports/state/review/runs/20261112T073040Z/sweep.json", "{}")
    write(root, "kb/reports/state/review/runs/v2/revise/kb/theory/baz/bbbbbbbbbbbb/log.jsonl", "")
    write(root, "kb/reports/state/review/packets/kb/theory/bar.md",
          PACKET.format(note="kb/theory/bar.md", resolution="rejected", authority="user",
                        at='"2026-11-12T16:15:19Z"', summary="The operator kept the note."))
    write(root, "kb/reports/state/review/packets/kb/theory/qux.md",
          PACKET.format(note="kb/theory/qux.md", resolution="pending", authority="null", at="null", summary="null"))
    write(root, "kb/theory/qux.md", "# Qux\n")
    write(root, "kb/reports/state/fixes/qux.fix-report.md", "# Fix report: qux\n\n| a | b |\n")
    monkeypatch.setattr(cli, "_root", lambda: root)
    return root


def by(found, **fields):
    return [e for e in found if all(e[k] == v for k, v in fields.items())]


def test_answers_yield_one_entry_per_item_with_its_state_and_reason(repo):
    found = by(decisions.entries(repo), note=NOTE, **{"class": "plain-wording"})
    assert [(e["decision"], e["item"], e["reason"]) for e in found] == [
        ("approved", "first entry -> kept", None), ("rejected", "second entry -> rejected", "changes the claim"),
        ("deferred", "third entry -> deferred", "the term may be registered")]
    assert all(e["unit"] == "item" and e["decided-by"] == "operator" and e["proposed-by"] == "worker"
               and e["at"] == "2026-11-12T10:00:00Z" and e["key"] == "list-key" and e["run"] == RUN
               and e["workflow"] == "revise" for e in found)


def test_unanswered_stop_is_one_pending_bundle(repo):
    [pending] = by(decisions.entries(repo), **{"class": "abstractions"})
    assert (pending["decided-by"], pending["decision"], pending["unit"], pending["at"]) == (
        "pending", "pending", "bundle", None)


def test_a_pending_item_in_approved_answers_is_listed_as_pending(repo):
    record(repo, RUN, "b", "abstractions-answers-0123456789ab.md", PENDING,
           answers([{**ITEMS[0], "state": "approved", **DECIDED}, {**ITEMS[1], "state": "pending"},
                    {**ITEMS[2], "state": "pending"}]), "2026-11-12T10:05:00Z")
    found = by(decisions.entries(repo), **{"class": "abstractions"})
    assert [(e["decided-by"], e["decision"], e["at"]) for e in found] == [
        ("operator", "approved", "2026-11-12T10:00:00Z"), ("pending", "pending", None), ("pending", "pending", None)]


def test_an_unreadable_approved_answer_is_listed_as_invalid(repo):
    record(repo, RUN, "b", "abstractions-answers-0123456789ab.md", PENDING, "not answers\n", "2026-11-12T10:05:00Z")
    [entry] = by(decisions.entries(repo), **{"class": "abstractions"})
    assert (entry["decision"], entry["unit"], entry["at"]) == ("invalid", "bundle", "2026-11-12T10:05:00Z")


def test_publication_approval_is_one_bundle_and_no_candidates_has_no_entry(repo):
    found = by(decisions.entries(repo), note=NOTE)
    [publication] = by(found, **{"class": "publication"})
    assert (publication["proposed-by"], publication["decided-by"], publication["decision"], publication["unit"],
            publication["at"], publication["item"]) == (
        "workflow", "operator", "approved", "bundle", "2026-11-12T11:00:00Z", f"{RUN}/artifact/final.md"[:79] + "…")
    assert len(found) == 5
    assert [e["at"] for e in found] == ["2026-11-12T10:00:00Z"] * 3 + ["2026-11-12T11:00:00Z", None]


def test_packet_yields_disposition_and_user_resolution(repo):
    resolution, disposition = by(decisions.entries(repo), note="kb/theory/bar.md")   # untimed entries sort last
    assert (disposition["decided-by"], disposition["decision"], disposition["at"]) == ("agent", "revise", None)
    assert (resolution["decided-by"], resolution["decision"], resolution["reason"], resolution["at"]) == (
        "operator", "rejected", "The operator kept the note.", "2026-11-12T16:15:19Z")
    assert resolution["record"] == "kb/reports/state/review/packets/kb/theory/bar.md"
    assert resolution["workflow"] == "full-pass" and resolution["unit"] == "bundle"


def test_pending_packet_yields_only_the_disposition_and_fix_report_is_listed(repo):
    found = by(decisions.entries(repo), note="kb/theory/qux.md")
    assert [(e["class"], e["decided-by"], e["decision"]) for e in found] == [
        ("packet", "agent", "revise"), ("fix-report", "agent", "report")]
    assert found[1]["record"] == "kb/reports/state/fixes/qux.fix-report.md" and found[1]["run"] is None


def test_cli_filters_and_json(repo, capsys):
    assert cli.main(["decisions", "--note", NOTE, "--class", "plain-wording", "--json"]) == 0
    found = json.loads(capsys.readouterr().out)
    assert [e["decision"] for e in found] == ["approved", "rejected", "deferred"]
    assert set(found[0]) == {"note", "workflow", "run", "record", "class", "proposed-by", "decided-by",
                             "decision", "unit", "item", "reason", "resolution", "refs", "carried-from", "key",
                             "at"}
    assert cli.main(["decisions", "--class", "fix-report"]) == 0
    out = capsys.readouterr().out
    assert out.splitlines()[0] == "kb/theory/qux.md" and "fix-report" in out and NOTE not in out


def test_malformed_operator_record_fails_naming_its_path(repo, capsys):
    write(repo, f"{RUN}/operator/e.json", "{not json")
    assert cli.main(["decisions"]) == 2
    assert f"{RUN}/operator/e.json" in capsys.readouterr().err
