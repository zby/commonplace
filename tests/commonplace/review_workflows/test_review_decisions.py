"""The operator-decision record: a read-only listing over kept answers, publications, packets and fix reports."""

import json
from hashlib import sha256

import pytest
import yaml

from commonplace.cli import review_workflows as cli
from commonplace.lib.review_workflows import decisions

NOTE = "kb/theory/foo.md"
NOTE_TEXT = "# Foo\n"
RUN = "kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/foo/20261112T100000Z"
OLD_RUN = f"kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/foo/{sha256(NOTE_TEXT.encode()).hexdigest()[:12]}"
DECIDED = {"decided-by": "operator", "decided-at": "2026-11-12T10:00:00Z"}
ITEMS = [{"id": "1", "proposal": {"quote": "first entry", "change": "kept", "reason": "plain"}},
         {"id": "2", "proposal": {"quote": "second entry", "change": "rejected", "reason": "plain"}},
         {"id": "3", "proposal": {"quote": "third entry", "change": "deferred", "reason": "plain"}}]
DECISIONS = [{"state": "approved", **DECIDED},
             {"state": "rejected", "reason": "changes the claim", **DECIDED},
             {"state": "deferred", "reason": "the term may be registered", "revisit": "when the ledger decides",
              **DECIDED}]


def answers(items):
    data = {"type": "types/answers.md", "description": "d", "question": f"{RUN}/artifact/question.md",
            "question-sha256": "0" * 64, "items": items}
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# Answers\n"


PENDING = answers([{**item, "state": "pending"} for item in ITEMS])
ANSWER = answers([{**item, **decision} for item, decision in zip(ITEMS, DECISIONS, strict=True)])


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


def started(root, run, text=NOTE_TEXT):
    write(root, f"{run}/start.json", json.dumps({"note": NOTE, "sha256": sha256(text.encode()).hexdigest(),
                                                 "brief-sha256": None}))


def kept(root, run, name, text, at):
    """Keep the answers file `name` of `run` as a consuming run, or `answers record`, keeps it."""
    write(root, f"{run}/artifact/{name}", text)
    path = decisions.keep_answers(root / run, f"{run}/artifact/{name}", text)
    data = json.loads(path.read_text())
    path.write_text(json.dumps({**data, "at": at}))


PACKET = """---
note: {note}
run: kb/workflow-state/data/current/review/runs/v2/full-pass/kb/theory/bar/aaaaaaaaaaaa
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
    write(root, NOTE, NOTE_TEXT)                 # the text the run started from
    started(root, RUN)
    kept(root, RUN, "plain-wording-answers.md", ANSWER, "2026-11-12T10:05:00Z")
    write(root, f"{RUN}/artifact/abstractions-answers.md", PENDING)
    write(root, f"{RUN}/continuation.json", json.dumps({"items": [
        {"id": "1", "kind": "proposals", "answers": [f"{RUN}/artifact/abstractions-answers.md"]}]}))
    write(root, f"{RUN}/held.json", json.dumps({"candidate": f"{RUN}/artifact/final.md", "sha256": "1" * 64}))
    started(root, OLD_RUN, "# Foo, before\n")                  # a run directory named by the old text hash
    write(root, f"{OLD_RUN}/published.json", json.dumps({"publications": [
        {"number": 1, "text": f"{OLD_RUN}/artifact/publications/1.md", "sha256": sha256(NOTE_TEXT.encode()).hexdigest(),
         "at": "2026-11-11T09:00:00Z", "decided-by": "operator", "revised": True}]}))
    write(root, "kb/workflow-state/data/current/review/runs/20261112T073040Z/sweep.json", "{}")
    write(root, "kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/baz/bbbbbbbbbbbb/log.jsonl", "")
    write(root, "kb/workflow-state/data/current/review/packets/kb/theory/bar.md",
          PACKET.format(note="kb/theory/bar.md", resolution="rejected", authority="user",
                        at='"2026-11-12T16:15:19Z"', summary="The operator kept the note."))
    write(root, "kb/workflow-state/data/current/review/packets/kb/theory/qux.md",
          PACKET.format(note="kb/theory/qux.md", resolution="pending", authority="null", at="null", summary="null"))
    write(root, "kb/theory/qux.md", "# Qux\n")
    write(root, "kb/workflow-state/data/current/fixes/qux.fix-report.md", "# Fix report: qux\n\n| a | b |\n")
    monkeypatch.setattr(cli, "_root", lambda: root)
    return root


def by(found, **fields):
    return [e for e in found if all(e[k] == v for k, v in fields.items())]


def test_pending_work_is_overtaken_once_the_note_holds_another_text(repo):
    found = decisions.entries(repo)
    [stop] = by(found, **{"class": "abstractions"})
    assert (stop["decided-by"], stop["decision"], stop["item"]) == (
        "pending", "pending", f"{RUN}/artifact/abstractions-answers.md")
    [held] = by(found, **{"class": "publication"}, decision="pending")
    assert held["item"] == f"{RUN}/artifact/final.md" and held["record"] == f"{RUN}/held.json"
    write(repo, NOTE, NOTE_TEXT + "\nAn edit after the stop.\n")
    found = decisions.entries(repo)
    [stop] = by(found, **{"class": "abstractions"})
    assert (stop["decided-by"], stop["decision"], stop["at"]) == ("overtaken", "overtaken", None)
    assert by(found, **{"class": "publication"}, run=RUN)[0]["decision"] == "overtaken"
    assert [e["decision"] for e in by(found, **{"class": "plain-wording"})] == [
        "approved", "rejected", "deferred"]                      # decided entries are unaffected


def test_a_kept_answers_file_settles_the_pending_entry_and_lists_its_items(repo):
    kept(repo, RUN, "abstractions-answers.md", ANSWER, "2026-11-12T12:00:00Z")
    found = by(decisions.entries(repo), **{"class": "abstractions"})
    assert [e["decision"] for e in found] == ["approved", "rejected", "deferred"]
    assert {e["record"].rsplit("/", 1)[0] for e in found} == {f"{RUN}/answers"}


def test_publications_are_read_from_hash_named_and_timestamp_run_directories(repo):
    [published] = by(decisions.entries(repo), **{"class": "publication"}, decision="published")
    assert (published["run"], published["decided-by"], published["revised"]) == (OLD_RUN, "operator", True)


def test_an_unreadable_kept_answer_is_listed_as_invalid(repo):
    kept(repo, RUN, "abstractions-answers.md", "not answers\n", "2026-11-12T10:05:00Z")
    [entry] = by(decisions.entries(repo), **{"class": "abstractions"})
    assert (entry["decision"], entry["unit"], entry["at"]) == ("invalid", "bundle", "2026-11-12T10:05:00Z")


def test_packet_yields_disposition_and_user_resolution(repo):
    resolution, disposition = by(decisions.entries(repo), note="kb/theory/bar.md")   # untimed entries sort last
    assert (disposition["decided-by"], disposition["decision"], disposition["at"]) == ("agent", "revise", None)
    assert (resolution["decided-by"], resolution["decision"], resolution["reason"], resolution["at"]) == (
        "operator", "rejected", "The operator kept the note.", "2026-11-12T16:15:19Z")
    assert resolution["record"] == "kb/workflow-state/data/current/review/packets/kb/theory/bar.md"
    assert resolution["workflow"] == "full-pass" and resolution["unit"] == "bundle"


def test_cli_filters_and_json(repo, capsys):
    assert cli.revise_main(["decisions", "--note", NOTE, "--class", "plain-wording", "--json"]) == 0
    found = json.loads(capsys.readouterr().out)
    assert [e["decision"] for e in found] == ["approved", "rejected", "deferred"]
    assert set(found[0]) == {"note", "workflow", "run", "record", "class", "proposed-by", "decided-by",
                             "decision", "unit", "item", "reason", "resolution", "refs", "carried-from", "revised",
                             "key", "at"}
    assert cli.revise_main(["decisions", "--class", "fix-report"]) == 0
    out = capsys.readouterr().out
    assert out.splitlines()[0] == "kb/theory/qux.md" and "fix-report" in out and NOTE not in out
    write(repo, NOTE, "# Foo, edited\n")
    assert cli.revise_main(["decisions", "--note", NOTE, "--class", "abstractions", "--json"]) == 0
    assert [e["decision"] for e in json.loads(capsys.readouterr().out)] == ["overtaken"]
    assert cli.revise_main(["decisions", "--note", NOTE, "--class", "abstractions"]) == 0
    assert "worker->overtaken | overtaken" in capsys.readouterr().out


def test_malformed_kept_answers_fail_naming_their_path(repo, capsys):
    write(repo, f"{RUN}/answers/e.json", "{not json")
    assert cli.revise_main(["decisions"]) == 2
    assert f"{RUN}/answers/e.json" in capsys.readouterr().err
