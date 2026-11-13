"""The operator-decision record: a read-only listing over run records, packets and fix reports."""

import json

import pytest

from commonplace.cli import review_workflows as cli
from commonplace.lib.review_workflows import decisions

NOTE = "kb/theory/foo.md"
RUN = "kb/reports/state/review/runs/revise/kb/theory/foo/0123456789ab"
LIST = "- first entry, kept\n  detail line\n- second entry, struck\n"
ANSWER = "- first entry, kept\n  detail line\n- second entry, struck\n  struck: changes the claim\n"


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
run: kb/reports/state/review/runs/full-pass/kb/theory/bar/aaaaaaaaaaaa
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
    record(root, RUN, "a", "plain-wording-list-0123456789ab.md", LIST, ANSWER, "2026-11-12T10:00:00Z", "list-key")
    record(root, RUN, "b", "abstractions-list-0123456789ab.md", LIST)
    record(root, RUN, "c", "publication.json", '{"artifact": "kb/theory/foo.md"}\n',
           '{"artifact": "kb/theory/foo.md"}\n', "2026-11-12T11:00:00Z", "pub-key")
    record(root, RUN, "d", "plain-wording-list-ffffffffffff.md", "No candidates.\n")
    write(root, "kb/reports/state/review/runs/20261112T073040Z/sweep.json", "{}")
    write(root, "kb/reports/state/review/runs/revise/kb/theory/baz/bbbbbbbbbbbb/log.jsonl", "")
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


def test_strike_list_answered_yields_one_entry_per_proposed_entry(repo):
    found = by(decisions.entries(repo), note=NOTE, **{"class": "plain-wording"})
    assert [(e["decision"], e["item"], e["reason"]) for e in found] == [
        ("approve", "first entry, kept", None), ("strike", "second entry, struck", "changes the claim")]
    assert all(e["unit"] == "item" and e["decided-by"] == "operator" and e["proposed-by"] == "worker"
               and e["at"] == "2026-11-12T10:00:00Z" and e["key"] == "list-key" and e["run"] == RUN
               and e["workflow"] == "revise" for e in found)


def test_unanswered_strike_list_is_one_pending_bundle(repo):
    [pending] = by(decisions.entries(repo), **{"class": "abstractions"})
    assert (pending["decided-by"], pending["decision"], pending["unit"], pending["at"]) == (
        "pending", "pending", "bundle", None)


def test_publication_approval_is_one_bundle_and_no_candidates_has_no_entry(repo):
    found = by(decisions.entries(repo), note=NOTE)
    [publication] = by(found, **{"class": "publication"})
    assert (publication["proposed-by"], publication["decided-by"], publication["decision"], publication["unit"],
            publication["at"]) == ("workflow", "operator", "approve-publication", "bundle", "2026-11-12T11:00:00Z")
    assert len(found) == 4
    assert [e["at"] for e in found] == ["2026-11-12T10:00:00Z"] * 2 + ["2026-11-12T11:00:00Z", None]


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
    assert [e["decision"] for e in found] == ["approve", "strike"]
    assert set(found[0]) == {"note", "workflow", "run", "record", "class", "proposed-by", "decided-by",
                             "decision", "unit", "item", "reason", "key", "at"}
    assert cli.main(["decisions", "--class", "fix-report"]) == 0
    out = capsys.readouterr().out
    assert out.splitlines()[0] == "kb/theory/qux.md" and "fix-report" in out and NOTE not in out


def test_malformed_operator_record_fails_naming_its_path(repo, capsys):
    write(repo, f"{RUN}/operator/e.json", "{not json")
    assert cli.main(["decisions"]) == 2
    assert f"{RUN}/operator/e.json" in capsys.readouterr().err
