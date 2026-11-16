"""The rewrite workflow through the CLI with a fake worker: inputs per call, review binding, repair and publication."""
from __future__ import annotations

import functools
import json
import subprocess
import sys

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run
from commonplace.lib import library
from commonplace.lib.review_workflows import decisions, edits, observations
from commonplace.lib.review_workflows import revise as revise_module
from commonplace.lib.review_workflows import rewrite as rewrite_module
from tests.commonplace.review_workflows.brief_helpers import add_brief, captured_inputs
from tests.commonplace.review_workflows.result_helpers import copy_contract
from tests.commonplace.review_workflows.test_revise import (
    EDIT_TYPES,
    NOTE,
    NOTE_PATH,
    PROFILES,
    REVIEW_FAKE,
    REVIEW_FILES,
    ROLE,
    approve_publication,
    artifact_file,
    note_text,
)
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

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
if "reconstruction" in outputs:
    kind = "reconstruct"
elif "claim-account" in outputs:
    kind = "claim-account"
elif "candidate" in outputs:
    kind = "candidate-repair" if "blocked-candidate" in inputs else "candidate"
else:
    kind = "review-repair" if "REPAIRED" in inputs["candidate"].read_text() else "review"
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(kind + "\n")
with open(os.environ["FAKE_LOG"] + ".inputs", "a") as log:
    log.write(json.dumps({"kind": kind, "prompt": frame,
                          "inputs": {key: path.read_text() for key, path in inputs.items()}}) + "\n")
if Path(f"problem-{kind}").exists():
    Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(json.dumps(
        {"kind": "unable", "message": "The commission contradicts the write brief."}))
    sys.exit(0)
if kind == "reconstruct":
    outputs["reconstruction"].write_text("# Reconstruction\n\n## Support\n\nAlpha holds.\n\n## Inference\n\nNone.\n\n"
                                         "## Conflicts\n\nNone.\n\n## Scope\n\nAll.\n\n## Gaps\n\nNone.\n")
elif kind == "claim-account":
    outputs["claim-account"].write_text("# Claim account\n\n## Alpha holds\n\nState it.\n")
elif kind.startswith("candidate"):
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
    outputs["report"].write_text("# Report\n\n## Kept\n\nNone.\n\n## Replaced\n\nThe body.\n\n## Omitted\n\nNone.\n")
else:
    sha = re.search(r"The candidate's SHA-256 is `([0-9a-f]+)`", frame).group(1)
    if Path("wrong-hash").exists():
        sha = "0" * 64
    block = Path("block-all").exists() or (Path("block-1").exists() and kind == "review")
    finding = "## Finding 1\n\nAnchor: the body\nBasis: the reconstruction\nRequired change: qualify it\n\n"
    outputs["review"].write_text(f"---\ncandidate-sha256: {sha}\n---\n\n# Review\n\n"
                                 + (finding if block else "") + ("block\n" if block else "accept\n"))
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
STEPS = ["reconstruct", "claim-account", ROLE, "candidate", "review"]
ROLE_SECTION = "It supplies one term.\nRelied on: the term. Unused: none."
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
    script.write_text(REVIEW_FAKE + FAKE)
    log.touch()
    harness = Harness(sys.executable, {"_subcommand": [str(script)], "_env": {"FAKE_LOG": str(log)}},
                      lambda profile: {"model": profile.launch_model}, model_used=lambda launch: "fake-model-1")
    commission = tmp_path / "commission.md"
    commission.write_text(COMMISSION)
    return root, {"fake": harness}, log, commission


def rewrite(repo, capsys, *args, commission=True):
    before = repo[2].read_text().splitlines()
    given = ["--commission", str(repo[3])] if commission else []
    code = main(["run", "rewrite", NOTE_PATH, *given, *args, "--timeout", "30"], harnesses=repo[1])
    captured = capsys.readouterr()
    return code, json.loads(captured.out) if code != 2 else captured.err, repo[2].read_text().splitlines()[len(before):]


def publish(repo, capsys, report):
    approve_publication(repo, capsys, report)
    code, done, launches = rewrite(repo, capsys, commission=False)
    assert code == 0 and done["complete"] and done["applied"], done["waiting-for"]
    assert launches == [], "an approved publication replays every call"
    return done


def calls(repo):
    return {call["kind"]: call for call in captured_inputs(repo[2])}


def test_a_rewrite_runs_its_calls_to_publication_and_writes_only_after_approval(repo, capsys):
    original = note_text(repo)
    brief = add_brief(repo[0], NOTE_PATH)
    subprocess.run(["git", "add", "."], cwd=repo[0], check=True)
    subprocess.run(["git", "commit", "-q", "-m", "brief"], cwd=repo[0], check=True)
    start = note_text(repo)
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == STEPS and not report["applied"] and report["guard"]["clean"]
    assert report["waiting-for"]["file"].endswith("/artifact/publication-answers.md")
    assert [review["verdict"] for review in report["reviews"]] == ["accept"] and not report["repair-used"]
    assert note_text(repo) == start != original
    run = repo[0] / report["run-dir"]
    assert report["run-dir"].startswith("kb/reports/state/review/runs/v2/rewrite/kb/notes/alpha/")
    for name in ("commission.md", "brief.md", "sources.md", "start.md", "reconstruction.md", "claim-account.md",
                 "candidate-1.md", "candidate-1-report.md", "review-1.md", "final.md", "final.diff"):
        assert (run / "artifact" / name).is_file(), name
    found = calls(repo)
    contracts = {"type-contract", "collection-contract"}
    shared = {"instruction", "commission", "brief", *contracts}
    assert set(found["reconstruct"]["inputs"]) == shared | {"sources", "source-1"}
    assert set(found["claim-account"]["inputs"]) == shared | {"reconstruction"}
    assert set(found["candidate"]["inputs"]) == shared | {"reconstruction", "claim-account", "note", "kb-role"}
    assert set(found["review"]["inputs"]) == shared | {"reconstruction", "claim-account", "note", "candidate",
                                                       "candidate-report", "kb-role"}
    assert found["candidate"]["inputs"]["kb-role"] == found["review"]["inputs"]["kb-role"] == ROLE_SECTION
    assert report["role"] == {"report": f"{report['run-dir']}/role", "reused": False}
    given = (run / "role").glob("artifact/reviews/*/inputs/operational/inbound.md")
    assert [path.read_text().startswith(f"# Inbound contexts of `{NOTE_PATH}`") for path in given] == [True]
    for kind in ("reconstruct", "claim-account"):              # the note is withheld from the first two calls
        assert all(text != start and "Alpha body ." not in text for text in found[kind]["inputs"].values())
        assert f"do not open `{NOTE_PATH}`" in found[kind]["prompt"]
    assert found["candidate"]["inputs"]["note"] == start
    assert all(call["inputs"]["brief"] == brief.read_text() for call in found.values())
    assert found["review"]["inputs"]["candidate"] == artifact_file(repo, report, "final.md").read_text()
    code, again, launches = rewrite(repo, capsys, commission=False)
    assert code == 0 and launches == [] and again["waiting-for"] == report["waiting-for"]
    assert note_text(repo) == start
    publish(repo, capsys, again)
    assert note_text(repo) == artifact_file(repo, report, "final.md").read_text()
    assert "Alpha, rewritten from sources" in note_text(repo) and "user-verified" not in note_text(repo)


def test_an_ignored_source_is_referenced_by_path_and_hash_and_never_copied(repo, capsys):
    code, report, _ = rewrite(repo, capsys)
    assert code == 0
    assert [(s["path"], s["mode"]) for s in report["sources"]] == [(SOURCE, "captured"), (SNAPSHOT, "referenced")]
    sha = observations.sha(SNAPSHOT_TEXT.encode())
    listing = (repo[0] / report["run-dir"] / "artifact/sources.md").read_text()
    assert f"`{SNAPSHOT}`" in listing and sha in listing and "source-1" in listing
    reconstruct = calls(repo)["reconstruct"]
    assert reconstruct["inputs"]["source-1"] == (repo[0] / SOURCE).read_text()
    assert not any("SNAPSHOT-MARKER" in text for text in reconstruct["inputs"].values())
    run = repo[0] / report["run-dir"]
    assert not any(b"SNAPSHOT-MARKER" in path.read_bytes() for path in run.rglob("*") if path.is_file())
    (repo[0] / SNAPSHOT).write_text(SNAPSHOT_TEXT + "Changed.\n")       # a referenced source must not drift
    code, changed, launches = rewrite(repo, capsys, commission=False)
    assert code == 1 and "referenced sources changed" in changed["stopped"] and launches == []


def test_a_block_takes_one_repair_and_a_fresh_review_of_the_repaired_candidate(repo, capsys):
    (repo[0] / "block-1").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == [*STEPS, "candidate-repair", "review-repair"]
    assert report["repair-used"] and [r["verdict"] for r in report["reviews"]] == ["block", "accept"]
    found = calls(repo)
    review = artifact_file(repo, report, "review-1.md").read_text()
    assert found["candidate-repair"]["inputs"]["review"] == review
    assert found["candidate-repair"]["inputs"]["blocked-candidate"] == artifact_file(repo, report,
                                                                                    "candidate-1.md").read_text()
    assert "review" not in found["review-repair"]["inputs"]               # the second reviewer sees no prior review
    final = artifact_file(repo, report, "final.md").read_text()
    assert final == artifact_file(repo, report, "candidate-2.md").read_text() and final.endswith("REPAIRED.\n")
    publish(repo, capsys, report)
    assert note_text(repo) == final


def test_a_second_block_ends_the_run_with_nothing_published(repo, capsys):
    original = note_text(repo)
    (repo[0] / "block-all").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and report["complete"] and launches == [*STEPS, "candidate-repair", "review-repair"]
    assert report["blocked"] and "--restart" in report["blocked"] and report["waiting-for"] is None
    assert not report["applied"] and note_text(repo) == original
    assert not artifact_file(repo, report, "publication-answers.md").exists()
    assert artifact_file(repo, report, "review-2.md").is_file()
    code, again, launches = rewrite(repo, capsys, commission=False)
    assert launches == [] and again["blocked"] == report["blocked"]


def test_a_review_bound_to_another_candidate_hash_is_refused(repo, capsys):
    original = note_text(repo)
    (repo[0] / "wrong-hash").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and report["stopped"].startswith("review: ")
    assert "not the candidate it was given" in report["stopped"]
    assert launches[:len(STEPS)] == STEPS and set(launches[len(STEPS):]) == {"review"} and not report["reviews"]
    assert note_text(repo) == original


def test_a_candidate_that_breaks_the_bounds_is_refused(repo, capsys):
    original = note_text(repo)
    (repo[0] / "bad-bounds").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and report["stopped"].startswith("candidate: ") and "the H1 changed" in report["stopped"]
    assert launches[:4] == ["reconstruct", "claim-account", ROLE, "candidate"] and set(launches[3:]) == {"candidate"}
    assert note_text(repo) == original


def test_an_accepted_unchanged_candidate_ends_without_publication(repo, capsys):
    original = note_text(repo).replace("user-verified: true\n", "")
    (repo[0] / NOTE_PATH).write_text(original)
    (repo[0] / "same-text").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and report["complete"] and report["unchanged"] and launches == STEPS
    assert report["waiting-for"] is None and not report["applied"] and note_text(repo) == original


def test_a_worker_problem_stops_the_run(repo, capsys):
    (repo[0] / "problem-claim-account").touch()
    code, report, launches = rewrite(repo, capsys)
    assert code == 1 and "claim-account: worker problem: The commission contradicts" in report["stopped"]
    assert launches == ["reconstruct", "claim-account"]


def test_the_commission_is_required_checked_and_frozen_unless_restarted(repo, capsys):
    code, error, launches = rewrite(repo, capsys, commission=False)
    assert code == 2 and "needs --commission FILE" in error and launches == []
    repo[3].write_text(COMMISSION.replace("## Must exclude", "## Out of scope").replace(
        "note: kb/notes/alpha.md", "note: kb/notes/beta.md"))
    code, error, launches = rewrite(repo, capsys)
    assert code == 2 and "`## Must exclude` is missing" in error and "`note` must be kb/notes/alpha.md" in error
    assert launches == []
    repo[3].write_text(COMMISSION.replace(SOURCE, NOTE_PATH))
    code, error, _ = rewrite(repo, capsys)
    assert code == 2 and "is the note or its write brief" in error
    repo[3].write_text(COMMISSION)
    _, report, _ = rewrite(repo, capsys)
    repo[3].write_text(COMMISSION.replace("the existing claim overreaches", "keep it short"))
    code, error, launches = rewrite(repo, capsys)
    assert code == 2 and "differs from the one this run captured" in error and launches == []
    code, restarted, launches = rewrite(repo, capsys, "--restart")
    # The role report is obtained again; its inputs did not change, so its call replays without a launch.
    assert code == 0 and restarted["restarted"] and launches == [step for step in STEPS if step != ROLE]
    assert restarted["run-dir"] == report["run-dir"]
    assert restarted["waiting-for"]["key"] != report["waiting-for"]["key"]
    assert "keep it short" in calls(repo)["reconstruct"]["inputs"]["commission"]
    code, error, _ = rewrite(repo, capsys, "--restart", commission=False)
    assert code == 2 and "--restart needs --commission FILE" in error


DECIDED = {"proposal": {"quote": "Alpha body", "change": "alpha", "reason": "plain"}, "state": "rejected",
           "reason": "a registered word", "revisit": None, "decided-by": "operator",
           "decided-at": "2026-11-15T12:00:00Z",
           "answers-file": "kb/reports/state/review/runs/v2/revise/kb/notes/alpha/0123456789ab/artifact/x.md"}


def test_earlier_decisions_and_the_role_reach_only_the_candidate_repair_and_review_calls(repo, capsys, monkeypatch):
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
    for kind in ("candidate", "review", "candidate-repair", "review-repair"):
        assert found[kind]["inputs"]["earlier-decisions"] == told and found[kind]["inputs"]["kb-role"] == ROLE_SECTION
    for kind in ("reconstruct", "claim-account"):       # material about the note's text stays out of claim selection
        assert not {"earlier-decisions", "kb-role"} & set(found[kind]["inputs"])
    assert json.loads((run / rewrite_module.EARLIER_FILE).read_text()) == {"decisions": [DECIDED]}
    monkeypatch.setattr(decisions, "earlier", lambda *args, **kwargs: pytest.fail("a repeat collects again"))
    code, again, launches = rewrite(repo, capsys, commission=False)
    assert code == 0 and launches == [] and again["waiting-for"] == report["waiting-for"]


def test_a_fresh_role_report_of_the_full_revise_procedure_is_reused_without_a_launch(repo, capsys):
    root, start = repo[0], note_text(repo)
    revise_role = edits.run_dir(root, "revise", NOTE_PATH) / "role"
    profile = Profile(harness="fake", launch_model="small", effort="low")
    kept = revise_module.role_report(root, NOTE_PATH, start, revise_role, profile, 30, repo[1], "revise")
    assert repo[2].read_text().splitlines() == [ROLE]
    code, report, launches = rewrite(repo, capsys)
    assert code == 0 and launches == [step for step in STEPS if step != ROLE]
    assert report["role"]["reused"] and report["role"]["report"].startswith(kept.path + "/artifact/reviews/")
    assert calls(repo)["candidate"]["inputs"]["kb-role"] == ROLE_SECTION
    (root / "kb/notes/beta.md").write_text(NOTE.format(words="beta") + "\nBeta cites [Alpha](./alpha.md).\n")
    assert revise_module.stored_role(root, NOTE_PATH, start) is None, "new inbound contexts make it stale"


def test_the_publication_stop_names_each_workflow_s_way_to_change_the_candidate(repo, capsys, tmp_path):
    _, report, _ = rewrite(repo, capsys)
    what = report["waiting-for"]["what"]
    assert "change the commission and repeat with --commission FILE --restart" in what and "--plan" not in what
    path = tmp_path / "revised.md"
    path.write_text(artifact_file(repo, report, "final.md").read_text() + "The operator's sentence.\n")
    _, supplied, _ = rewrite(repo, capsys, "--revised", str(path), commission=False)
    assert "--restart" in supplied["waiting-for"]["what"] and "--plan" not in supplied["waiting-for"]["what"]
    assert "supply --plan for revision" in edits.publication_instruction(False, change=revise_module.CHANGE)


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
    assert code == 0 and launches == STEPS and report["waiting-for"] is not None
    repo[3].write_text(short.replace("## Current direction", "## Direction"))
    code, error, _ = rewrite(repo, capsys, "--restart")
    assert code == 2 and "`## Current direction` is missing" in error


def test_a_revised_candidate_is_published_only_on_its_approval(repo, capsys, tmp_path):
    original = note_text(repo)
    path = tmp_path / "revised.md"
    path.write_text(original + "More.\n")
    code, error, _ = rewrite(repo, capsys, "--revised", str(path), commission=False)
    assert code == 2 and "not waiting at its publication stop" in error
    _, report, _ = rewrite(repo, capsys)
    revised = artifact_file(repo, report, "final.md").read_text() + "The operator's sentence.\n"
    path.write_text(revised)
    code, error, _ = rewrite(repo, capsys, "--revised", str(path))
    assert code == 2 and "--revised takes no workflow option: --commission" in error
    code, supplied, launches = rewrite(repo, capsys, "--revised", str(path), commission=False)
    assert code == 0 and launches == [] and supplied["proposed"].endswith("/artifact/revised.md")
    assert "run rewrite" in supplied["waiting-for"]["command"] and note_text(repo) == original
    done = publish(repo, capsys, supplied)
    assert note_text(repo) == revised and done["revised-candidate"]["revised"] == supplied["proposed"]
    [entry] = [e for e in decisions.entries(repo[0]) if e["note"] == NOTE_PATH]
    assert entry["workflow"] == "rewrite" and entry["revised"] and entry["decision"] == "approved"


def test_decisions_lists_the_rewrite_publication_and_marks_an_overtaken_stop(repo, capsys):
    _, report, _ = rewrite(repo, capsys)
    [entry] = [e for e in decisions.entries(repo[0]) if e["note"] == NOTE_PATH]
    assert (entry["workflow"], entry["class"], entry["decision"]) == ("rewrite", "publication", "pending")
    original = note_text(repo)
    (repo[0] / NOTE_PATH).write_text(original + "An edit after the stop.\n")
    assert [e["decision"] for e in decisions.entries(repo[0])] == ["overtaken"]
    (repo[0] / NOTE_PATH).write_text(original)
    publish(repo, capsys, report)
    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    [entry] = json.loads(capsys.readouterr().out)
    assert (entry["workflow"], entry["class"], entry["decided-by"], entry["decision"]) == (
        "rewrite", "publication", "operator", "approved")
    assert entry["run"] == report["run-dir"]
