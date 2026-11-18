"""The rewrite workflow through the CLI with a fake worker: inputs per call, the review operation, repair,
the held candidate, its publication and the accepted review as the note's current result."""
from __future__ import annotations

import dataclasses
import functools
import json
import re
import shlex
import subprocess
import sys

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run
from commonplace.lib import library
from commonplace.lib.review_workflows import (
    criteria,
    decisions,
    edits,
    observations,
    results,
)
from commonplace.lib.review_workflows import revise as revise_module
from commonplace.lib.review_workflows import rewrite as rewrite_module
from tests.commonplace.review_workflows.brief_helpers import add_brief, captured_inputs
from tests.commonplace.review_workflows.result_helpers import copy_contract
from tests.commonplace.review_workflows.test_revise import (
    EDIT_TYPES,
    FIX,
    NOTE,
    NOTE_PATH,
    PASSES,
    PROFILES,
    REVIEW_FAKE,
    REVIEW_FILES,
    artifact_file,
    decide,
    note_text,
    rejected,
)
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

REVIEW = r'''
import json, os, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text()
if frame.removeprefix("Task:\n").startswith("Review one note") and "review-a-rewrite-candidate.md`" in frame:
    def listed(name):
        return Path(re.search(rf"^- {re.escape(name)}: (.+)$", frame, re.MULTILINE).group(1))
    candidate = listed("note.md").read_text()
    kind = "review-repair" if "REPAIRED" in candidate else "review"
    given = {name: listed(name + ".md").read_text() for name in re.findall(r"^- (supplied-[^:]+)\.md: ", frame, re.MULTILINE)}
    with open(os.environ["FAKE_LOG"], "a") as log:
        log.write(kind + "\n")
    with open(os.environ["FAKE_LOG"] + ".inputs", "a") as log:
        log.write(json.dumps({"kind": kind, "prompt": frame,
                              "inputs": {"candidate": candidate, **given}}) + "\n")
    block = Path("block-all").exists() or (Path("block-1").exists() and kind == "review")
    reason = "Basis: the source says only under the condition. Required change: qualify it."
    once = Path(os.environ["FAKE_LOG"] + ".bare-reason")       # outside the checkout, which the guard watches
    if Path("bare-reason").exists() and not once.exists():
        once.touch()
        reason = "qualify it"
    if block:
        findings, outcome = [{"scope": "document", "quotes": [], "reason": reason, "level": "fail"}], "fail"
    elif Path("warn-review").exists():
        findings = [{"scope": "passage", "quotes": ["Alpha, rewritten from sources"], "reason": reason,
                     "level": "warn"},
                    {"scope": "document", "quotes": [], "reason": "The order reads well.", "level": "info"}]
        outcome = "warn"
    else:
        findings, outcome = [], "pass"
    data = {"type": "types/review-result.md", "findings": findings, "outcome": outcome}
    listed("review.md").write_text("---\n" + json.dumps(data) + "\n---\n\n# Review\n\n## Summary\n\nJudged.\n")
    sys.exit(0)
'''

FAKE = r'''
import json, os, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text()
files, section = {}, None
for line in frame.splitlines():
    header = re.fullmatch(r"(Inputs|Required outputs|Optional outputs)(?: \(.*\))?:", line)
    if header:
        section = files.setdefault(header.group(1), {})
    elif section is not None and line.startswith("- "):
        name, _, path = line[2:].partition(": ")
        section[name.removesuffix(".md")] = Path(path)
    else:
        section = None
inputs = files.get("Inputs", {})
outputs = files.get("Required outputs", {})
kind = "candidate-repair" if "blocked-candidate" in inputs else "candidate"
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(kind + "\n")
with open(os.environ["FAKE_LOG"] + ".inputs", "a") as log:
    log.write(json.dumps({"kind": kind, "prompt": frame,
                          "inputs": {key: path.read_text() for key, path in inputs.items()}}) + "\n")
if Path(f"problem-{kind}").exists():
    Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(json.dumps(
        {"kind": "unable", "message": "The commission contradicts the write brief."}))
    sys.exit(0)
if Path("drift-source").exists():
    Path("kb/sources/.snapshots/alpha/page.md").write_text("Changed while the worker ran.\n")
text = inputs["note"].read_text()
if Path("same-text").exists():
    candidate = text
else:
    candidate = text.replace("user-verified: true\n", "").replace("Alpha body", "Alpha, rewritten from sources")
if kind == "candidate-repair":
    candidate += "REPAIRED.\n"
if Path("bad-bounds").exists():
    candidate = candidate.replace("\n# Alpha\n", "\n# Beta\n")
outputs["candidate"].write_text(candidate)
outputs["report"].write_text("# Report\n\n## Affected citations\n\nNone.\n")
'''

INSTRUCTIONS = REPO_ROOT / "kb" / rewrite_module.INSTRUCTIONS_DIR
SOURCE = "kb/sources/alpha.ingest.md"
SNAPSHOT = "kb/sources/.snapshots/alpha/page.md"
SNAPSHOT_TEXT = "Full external source text: SNAPSHOT-MARKER-7f3a.\n"
COMMISSION = """\
---
note: kb/notes/alpha.md
sources:
  - path: kb/sources/alpha.ingest.md
    role: the ingest that states the claim
  - path: kb/sources/.snapshots/alpha/page.md
    role: the full source for exact wording
---

# Commission: Alpha

## Intended contribution

The reader learns that alpha holds, and under which condition.

## Must keep

The Alpha example.

## Must exclude

Any claim about beta.

## Reserved decisions

A retitle.

## Current direction

Rewrite the body from the sources; the existing claim overreaches.
"""
STEPS = ["candidate", "review"]
ROLE_REL = "kb/instructions/role-in-the-kb-gate.md"


@pytest.fixture
def repo(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text() for rel in (*NOTE_TYPE_SPECS, *EDIT_TYPES)}
    files |= {f"kb/{rewrite_module.INSTRUCTIONS_DIR}/{path.name}": path.read_text() for path in INSTRUCTIONS.glob("*.md")}
    files |= {rel: REVIEW_FILES[rel] for rel in (ROLE_REL, "kb/reports/COLLECTION.md")}
    files |= {"kb/instructions/review-profiles.yaml": PROFILES, "kb/notes/COLLECTION.md": "# Notes\n",
              SOURCE: "# Alpha ingest\n\nAlpha holds when the condition is met.\n",
              "kb/sources/.gitignore": ".snapshots/\n", SNAPSHOT: SNAPSHOT_TEXT,
              NOTE_PATH: NOTE.format(words="")}
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    copy_contract(root / "kb")
    for args in (("init", "-q"), ("config", "user.email", "t@example.com"), ("config", "user.name", "t")):
        subprocess.run(["git", *args], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=root, check=True)
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    monkeypatch.setattr(rewrite_module, "Run", functools.partial(Run, sleep=lambda seconds: None))
    monkeypatch.chdir(root)
    script, log = tmp_path / "fake.py", tmp_path / "launches.log"
    script.write_text(REVIEW + REVIEW_FAKE + FAKE)
    log.touch()
    harness = Harness(sys.executable, {"_subcommand": [str(script)], "_env": {"FAKE_LOG": str(log)}},
                      lambda profile: {"model": profile.launch_model}, model_used=lambda launch: "fake-model-1")
    commission = tmp_path / "commission.md"
    commission.write_text(COMMISSION)
    return root, {"fake": harness}, log, commission

def rewrite(repo, capsys, *args):
    before = repo[2].read_text().splitlines()
    code = main(["run", "rewrite", NOTE_PATH, "--commission", str(repo[3]), *args, "--timeout", "30"],
                harnesses=repo[1])
    captured = capsys.readouterr()
    return code, json.loads(captured.out) if code != 2 else captured.err, repo[2].read_text().splitlines()[len(before):]


def publish(repo, capsys, report, *args):
    """Publish the candidate the run held, on the operator's word; no worker is launched."""
    before = repo[2].read_text()
    code = main(["publish", report["run-dir"], *args], harnesses=repo[1])
    captured = capsys.readouterr()
    assert code == 0, captured.err
    assert repo[2].read_text() == before, "publishing launches nothing"
    return json.loads(captured.out)


def calls(repo):
    return {call["kind"]: call for call in captured_inputs(repo[2])}


def test_a_rewrite_runs_its_calls_and_holds_its_candidate_for_the_operator(repo, capsys):
    original = note_text(repo)
    brief = add_brief(repo[0], NOTE_PATH)
    subprocess.run(["git", "add", "."], cwd=repo[0], check=True)
    subprocess.run(["git", "commit", "-q", "-m", "brief"], cwd=repo[0], check=True)
    start = note_text(repo)
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == STEPS and not report["complete"] and report["guard"]["clean"]
    held = report["held"]
    assert held["candidate"] == report["proposed"] == f"{report['run-dir']}/artifact/final.md"
    assert held["command"] == f"commonplace-review publish {report['run-dir']}" and held["command"] in held["what"]
    assert [review["outcome"] for review in report["reviews"]] == ["pass"] and not report["repair-used"]
    assert report["accepted"] == {"review": report["reviews"][0]["review"], "outcome": "pass", "warn-findings": []}
    assert "finding(s) of level warn" not in held["what"]
    assert note_text(repo) == start != original
    run = repo[0] / report["run-dir"]
    assert re.fullmatch(r"kb/reports/state/review/runs/v2/rewrite/kb/notes/alpha/[0-9]{8}T[0-9]{6}Z(-[0-9]+)?",
                        report["run-dir"])
    started = json.loads((run / edits.START_RECORD).read_text())
    assert started == {"note": NOTE_PATH, "sha256": observations.sha(start.encode()),
                       "brief-sha256": observations.sha(brief.read_bytes())}
    for name in ("commission.md", "brief.md", "sources.md", "start.md",
                 "candidate-1.md", "candidate-1-report.md", "review-1.md", "final.md", "final.diff"):
        assert (run / "artifact" / name).is_file(), name
    assert json.loads((run / edits.HELD).read_text())["review"] == report["accepted"]["review"]
    found = calls(repo)
    contracts = {"type-contract", "collection-contract"}
    shared = {"instruction", "commission", "brief", *contracts}
    assert set(found["candidate"]["inputs"]) == shared | {"sources", "source-1", "note", "inbound"}
    supplied = {"commission", "brief", *contracts, "start", "sources", "source-1", "candidate-report", "inbound"}
    assert set(found["review"]["inputs"]) == {"candidate", *(f"supplied-{name}" for name in supplied)}
    assert found["review"]["inputs"]["supplied-start"] == start
    assert found["candidate"]["inputs"]["inbound"] == found["review"]["inputs"]["supplied-inbound"]
    assert found["candidate"]["inputs"]["source-1"] == found["review"]["inputs"]["supplied-source-1"]
    assert found["candidate"]["inputs"]["note"] == start
    assert all(call["inputs"]["brief"] == brief.read_text() for kind, call in found.items() if kind != "review")
    assert found["review"]["inputs"]["supplied-brief"] == brief.read_text()
    assert found["review"]["inputs"]["candidate"] == artifact_file(repo, report, "final.md").read_text()
    done = publish(repo, capsys, report)
    assert note_text(repo) == artifact_file(repo, report, "final.md").read_text()
    assert "Alpha, rewritten from sources" in note_text(repo) and "user-verified" not in note_text(repo)
    assert done["published"]["decided-by"] == "operator" and done["published"]["entries"] == []
    assert done["current-result"]["freshness"] == "fresh" and done["not-current"] is None
    stored = results.read_result(repo[0] / done["current-result"]["result"])     # validates as a review result
    assert stored.outcome == "pass" and stored.criterion == f"kb/{criteria.REWRITE_REL}"


def test_an_ignored_source_is_referenced_by_path_and_hash_and_never_copied(repo, capsys):
    code, report, _ = rewrite(repo, capsys)
    assert code == 0
    assert [(s["path"], s["mode"]) for s in report["sources"]] == [(SOURCE, "captured"), (SNAPSHOT, "referenced")]
    sha = observations.sha(SNAPSHOT_TEXT.encode())
    listing = (repo[0] / report["run-dir"] / "artifact/sources.md").read_text()
    assert f"`{SNAPSHOT}`" in listing and sha in listing and "source-1" in listing
    writer = calls(repo)["candidate"]
    assert writer["inputs"]["source-1"] == (repo[0] / SOURCE).read_text()
    assert not any("SNAPSHOT-MARKER" in text for text in writer["inputs"].values())
    run = repo[0] / report["run-dir"]
    assert not any(b"SNAPSHOT-MARKER" in path.read_bytes() for path in run.rglob("*") if path.is_file())


def test_a_referenced_source_that_drifts_during_the_run_holds_nothing(repo, capsys):
    (repo[0] / "drift-source").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and "referenced sources changed after the run captured them" in report["stopped"]
    assert SNAPSHOT in report["stopped"] and launches == STEPS
    assert report["held"] is None and not artifact_file(repo, report, "final.md").exists()


def test_a_block_takes_one_repair_and_a_fresh_review_of_the_repaired_candidate(repo, capsys):
    (repo[0] / "block-1").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == [*STEPS, "candidate-repair", "review-repair"]
    assert report["repair-used"] and [r["outcome"] for r in report["reviews"]] == ["fail", "pass"]
    found = calls(repo)
    review = artifact_file(repo, report, "review-1.md").read_text()
    assert review.startswith("---\ntype: types/review-result.md\n") and "outcome: fail" in review
    assert found["candidate-repair"]["inputs"]["review"] == review
    assert found["candidate-repair"]["inputs"]["blocked-candidate"] == artifact_file(repo, report,
                                                                                    "candidate-1.md").read_text()
    assert "supplied-review" not in found["review-repair"]["inputs"]      # the second reviewer sees no prior review
    final = artifact_file(repo, report, "final.md").read_text()
    assert final == artifact_file(repo, report, "candidate-2.md").read_text() and final.endswith("REPAIRED.\n")
    publish(repo, capsys, report)
    assert note_text(repo) == final


def test_a_second_block_ends_the_run_with_nothing_held(repo, capsys):
    original = note_text(repo)
    (repo[0] / "block-all").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and report["complete"] and launches == [*STEPS, "candidate-repair", "review-repair"]
    assert report["blocked"] and "--commission FILE" in report["blocked"] and "--restart" not in report["blocked"]
    assert report["held"] is None and note_text(repo) == original
    assert not artifact_file(repo, report, "final.md").exists()
    assert artifact_file(repo, report, "review-2.md").is_file()
    assert main(["publish", report["run-dir"]], harnesses=repo[1]) == 2
    assert "holds no candidate to publish" in capsys.readouterr().err


def test_a_review_result_of_another_text_is_refused(repo, capsys, monkeypatch):
    original = note_text(repo)
    swept = revise_module._sweep

    def other(*args, **kwargs):
        report = swept(*args, **kwargs)
        if report.pairs[0].result.criterion.endswith(criteria.REWRITE_REL):
            report.pairs[0].result = dataclasses.replace(report.pairs[0].result, target_sha256="0" * 64)
        return report
    monkeypatch.setattr(revise_module, "_sweep", other)
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and report["stopped"].startswith("review: ") and "it is refused" in report["stopped"]
    assert launches == STEPS and not report["reviews"] and note_text(repo) == original


def test_a_review_finding_without_its_basis_and_required_change_is_asked_again(repo, capsys):
    (repo[0] / "warn-review").touch()
    (repo[0] / "bare-reason").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == [*STEPS, "review"] and report["reviews"][0]["outcome"] == "warn"
    [retried] = [c for c in captured_inputs(repo[2]) if c["kind"] == "review"][1:]
    assert "`Basis:` and then `Required change:`" in retried["prompt"]


def test_a_warned_candidate_is_held_and_its_findings_become_triageable(repo, capsys):
    (repo[0] / "block-1").touch()
    (repo[0] / "warn-review").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == [*STEPS, "candidate-repair", "review-repair"]
    assert [r["outcome"] for r in report["reviews"]] == ["fail", "warn"]
    review = report["reviews"][1]["review"]
    [warned] = report["accepted"]["warn-findings"]
    assert report["accepted"]["review"] == review and warned["quotes"] == ["Alpha, rewritten from sources"]
    assert f"The accepted review {review} left 1 finding(s) of level warn" in report["held"]["what"]
    done = publish(repo, capsys, report)
    assert done["current-result"]["freshness"] == "fresh"
    criterion = f"kb/{criteria.REWRITE_REL}"
    [row] = results.status(repo[0], [(NOTE_PATH, criterion)])
    assert (row.freshness.state, row.outcome) == ("fresh", "warn")
    assert main(["status", NOTE_PATH, "--criteria", "type", "collection", "--json"]) == 0          # selected criteria never include the review
    assert not [pair for pair in json.loads(capsys.readouterr().out)["pairs"] if pair["criterion"] == criterion]
    for path in (REPO_ROOT / FIX, *PASSES.glob("*.md")):         # revise's operations, which the triage reads
        copy = repo[0] / path.relative_to(REPO_ROOT)
        copy.parent.mkdir(parents=True, exist_ok=True)
        copy.write_text(path.read_text())
    code = main(["run", "revise", NOTE_PATH, "--triage"], harnesses=repo[1])
    printed = capsys.readouterr()
    assert code == 0, printed.err
    triage = json.loads(printed.out)["triage"]
    [listed] = triage["results"]
    assert listed["result"] == done["current-result"]["result"]
    assert repo[2].read_text().splitlines()[-1] == "review-repair", "a triage launches nothing"
    answers = repo[0] / listed["answers"]
    answers.write_text(decide(answers.read_text(), {"1": rejected("the sources state no condition")}))
    assert results.freshness(repo[0], NOTE_PATH, criterion).state == "fresh", "an unrecorded answer counts for nothing"
    assert main(shlex.split(decisions.RECORD.format(file=listed["answers"]))[1:]) == 0
    capsys.readouterr()
    assert results.freshness(repo[0], NOTE_PATH, criterion) == results.Freshness("stale", ("criterion",))


def test_a_candidate_that_breaks_the_bounds_is_refused(repo, capsys):
    original = note_text(repo)
    (repo[0] / "bad-bounds").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and report["stopped"].startswith("candidate: ") and "the H1 changed" in report["stopped"]
    assert launches == ["candidate", "candidate"]  # identical correction feedback stops further attempts
    assert note_text(repo) == original


def test_an_accepted_unchanged_candidate_ends_without_a_held_candidate(repo, capsys):
    original = note_text(repo).replace("user-verified: true\n", "")
    (repo[0] / NOTE_PATH).write_text(original)
    (repo[0] / "same-text").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and report["complete"] and report["unchanged"] and launches == STEPS
    assert report["held"] is None and note_text(repo) == original
    assert not artifact_file(repo, report, "final.md").exists()


def test_a_worker_problem_stops_the_run(repo, capsys):
    (repo[0] / "problem-candidate").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and "candidate: worker problem: The commission contradicts" in report["stopped"]
    assert launches == ["candidate"]


def test_the_commission_is_required_and_checked_and_every_invocation_is_a_new_run(repo, capsys):
    with pytest.raises(SystemExit):
        main(["run", "rewrite", NOTE_PATH], harnesses=repo[1])
    assert "--commission" in capsys.readouterr().err
    repo[3].write_text(COMMISSION.replace("## Must exclude", "## Out of scope").replace(
        "note: kb/notes/alpha.md", "note: kb/notes/beta.md"))
    code, error, launches = rewrite(repo, capsys)
    assert code == 2 and "`## Must exclude` is missing" in error and "`note` must be kb/notes/alpha.md" in error
    assert launches == [] and not (repo[0] / "kb/reports/state/review/runs/v2/rewrite").exists()
    repo[3].write_text(COMMISSION.replace(SOURCE, NOTE_PATH))
    code, error, _ = rewrite(repo, capsys)
    assert code == 2 and "is the note or its write brief" in error
    repo[3].write_text(COMMISSION)
    _, report, _ = rewrite(repo, capsys)
    repo[3].write_text(COMMISSION.replace("the existing claim overreaches", "keep it short"))
    code, fresh, launches = rewrite(repo, capsys)
    assert code == 0 and launches == STEPS and fresh["run-dir"] != report["run-dir"]
    assert "keep it short" in [c for c in captured_inputs(repo[2]) if c["kind"] == "candidate"][-1][
        "inputs"]["commission"]
    assert "keep it short" not in artifact_file(repo, report, "commission.md").read_text(), "a run's record stays"


DECIDED = {"proposal": {"quote": "Alpha body", "change": "alpha", "reason": "plain"}, "state": "rejected",
           "reason": "a registered word", "revisit": None, "decided-by": "operator",
           "decided-at": "2026-11-15T12:00:00Z",
           "answers-file": "kb/reports/state/review/runs/v2/revise/kb/notes/alpha/0123456789ab/artifact/x.md"}


def test_earlier_decisions_reach_the_candidate_repair_and_review_calls(repo, capsys, monkeypatch):
    asked = []
    def earlier(root, note, current=None, findings_only=False):    # the role review asks for findings only
        return [] if findings_only else asked.append(current) or [DECIDED]
    monkeypatch.setattr(decisions, "earlier", earlier)
    (repo[0] / "block-1").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == [*STEPS, "candidate-repair", "review-repair"]
    run = repo[0] / report["run-dir"]
    assert asked == [run], "the run collects them once, excluding its own run"
    found = calls(repo)
    told = decisions.earlier_text([DECIDED])
    for kind in ("candidate", "candidate-repair"):
        assert found[kind]["inputs"]["earlier-decisions"] == told
    for kind in ("review", "review-repair"):
        given = found[kind]["inputs"]
        assert given["supplied-earlier-decisions"] == told
    assert json.loads((run / rewrite_module.EARLIER_FILE).read_text()) == {"decisions": [DECIDED]}


def test_an_incoming_citation_reaches_both_workers_without_a_role_call(repo, capsys):
    passage = "Beta cites [Alpha](./alpha.md)."
    (repo[0] / "kb/notes/beta.md").write_text(NOTE.format(words="beta") + "\n" + passage + "\n")
    code, _, launches = rewrite(repo, capsys)
    assert code == 0 and launches == STEPS
    found = calls(repo)
    for text in (found["candidate"]["inputs"]["inbound"], found["review"]["inputs"]["supplied-inbound"]):
        assert "kb/notes/beta.md" in text and passage in text


def test_the_brief_sections_of_a_commission_are_required_only_without_a_write_brief(repo, capsys):
    short = COMMISSION.split("## Intended contribution")[0] + COMMISSION[COMMISSION.index("## Current direction"):]
    repo[3].write_text(short)
    code, error, launches = rewrite(repo, capsys)
    assert code == 2 and launches == []
    assert all(f"`## {name}` is missing" in error for name in rewrite_module.BRIEF_SECTIONS)
    add_brief(repo[0], NOTE_PATH)
    subprocess.run(["git", "add", "."], cwd=repo[0], check=True)
    subprocess.run(["git", "commit", "-q", "-m", "brief"], cwd=repo[0], check=True)
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == STEPS and report["held"] is not None
    repo[3].write_text(short.replace("## Current direction", "## Direction"))
    code, error, _ = rewrite(repo, capsys)
    assert code == 2 and "`## Current direction` is missing" in error


def test_a_revised_text_is_published_but_is_not_the_reviewed_result(repo, capsys, tmp_path):
    original = note_text(repo)
    _, report, _ = rewrite(repo, capsys)
    revised = artifact_file(repo, report, "final.md").read_text() + "The operator's sentence.\n"
    path = tmp_path / "revised.md"
    path.write_text(revised)
    assert note_text(repo) == original
    done = publish(repo, capsys, report, "--revised", str(path))
    assert note_text(repo) == revised and done["revised-candidate"]["revised"].endswith("/artifact/revised.md")
    assert done["current-result"] is None and done["not-current"] == rewrite_module.NOT_CURRENT
    assert results.freshness(repo[0], NOTE_PATH, f"kb/{criteria.REWRITE_REL}").state == "missing"
    [entry] = [e for e in decisions.entries(repo[0]) if e["note"] == NOTE_PATH]
    assert entry["workflow"] == "rewrite" and entry["revised"] and entry["decision"] == "published"


def test_decisions_lists_the_rewrite_publication_and_marks_an_overtaken_candidate(repo, capsys):
    _, report, _ = rewrite(repo, capsys)
    [entry] = [e for e in decisions.entries(repo[0]) if e["note"] == NOTE_PATH]
    assert (entry["workflow"], entry["class"], entry["decision"]) == ("rewrite", "publication", "pending")
    original = note_text(repo)
    (repo[0] / NOTE_PATH).write_text(original + "An edit after the run.\n")
    assert [e["decision"] for e in decisions.entries(repo[0])] == ["overtaken"]
    assert main(["publish", report["run-dir"]], harnesses=repo[1]) == 2
    assert "no longer holds the text the run held its candidate over" in capsys.readouterr().err
    (repo[0] / NOTE_PATH).write_text(original)
    publish(repo, capsys, report)
    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    [entry] = json.loads(capsys.readouterr().out)
    assert (entry["workflow"], entry["class"], entry["decided-by"], entry["decision"]) == (
        "rewrite", "publication", "operator", "published")
    assert entry["run"] == report["run-dir"]


def test_a_changed_accepted_review_refuses_publication(repo, capsys):
    original = note_text(repo)
    _, report, _ = rewrite(repo, capsys)
    review = repo[0] / report["accepted"]["review"]
    review.write_text(review.read_text().replace("outcome: pass", "outcome: warn"))
    assert main(["publish", report["run-dir"]], harnesses=repo[1]) == 2
    assert "is not the file the run held" in capsys.readouterr().err
    assert note_text(repo) == original and results.freshness(
        repo[0], NOTE_PATH, f"kb/{criteria.REWRITE_REL}").state == "missing"
