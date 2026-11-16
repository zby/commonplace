"""Revision approval boundaries, exercised through the CLI with a fake worker."""
from __future__ import annotations

import dataclasses
import functools
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run, recorded_calls
from commonplace.lib import answers as answer_files
from commonplace.lib import library
from commonplace.lib.review_workflows import decisions, edits, observations, results
from commonplace.lib.review_workflows import revise as revise_module
from commonplace.lib.review_workflows.results import make_result, write_result
from tests.commonplace.review_workflows.brief_helpers import add_brief, captured_inputs
from tests.commonplace.review_workflows.result_helpers import (
    FAKE_RESULT,
    copy_contract,
    evidence,
    findings,
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
outputs = {**files.get("Required outputs", {}), **files.get("Optional outputs", {})}
task = frame.removeprefix("Task:\n")
if task.startswith("Assess one artifact"):
    kind = "assess"
elif "This operation asks before it edits" in task:
    kind = "list"
elif "The operator answered this operation's proposals" in task:
    kind = "apply"
else:
    kind = "pass"
found = re.search(r"(?:simplification-passes|fix-warnings)/([a-z-]+)\.md`", frame)
name = found.group(1) if found and kind != "assess" else "-"
model = sys.argv[sys.argv.index("--model") + 1]
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(f"{kind} {name} {model}\n")
if Path(f"fail-{name}").exists():
    sys.exit(1)
text = inputs["artifact" if kind == "assess" else "text"].read_text()
with open(os.environ["FAKE_LOG"] + ".inputs", "a") as log:
    log.write(json.dumps({"kind": kind, "pass": name,
        "inputs": {key: path.read_text() for key, path in inputs.items()}}) + "\n")
if Path(f"brief-problem-{kind}").exists():
    Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(json.dumps(
        {"kind": "unable", "message": "The requested pass conflicts with the write brief."}))
    sys.exit(0)


def result(outcome, **fields):
    data = {"type": "types/edit-result.md", "outcome": outcome, **fields}
    outputs["result"].write_text("---\n" + json.dumps(data) + "\n---\n\n# Report\n\nDone.\n")


if kind == "assess":
    passes = ["readability-and-flow", "place-external-systems", "opening-and-title"]
    if "PLAIN" in text:
        passes.insert(1, "plain-wording")
    if "OVERCLAIM" in text:
        passes.insert(0, "narrow-overclaims")
    if "BADPLAN" in text and "was rejected" not in frame:
        passes.append("make-it-shine")
    plan = "purpose: p\ndefend: []\nstop: null\npasses:\n" + "".join(f"  - pass: {p}\n" for p in passes)
    listed = re.findall(r"^- `([^`]+)` \(criterion `[^`]+`, depth", frame, re.MULTILINE)
    if "FIXIT" in text and listed:
        plan = plan.replace("passes:\n", f"passes:\n  - pass: fix-strategy-taxonomy\n    finding: {listed[0]}\n")
    if "STOP" in text:
        plan = "purpose: p\ndefend: []\npasses: []\nstop: rewrite-needed\n"
    if Path("new-proposal").exists():
        plan = plan.replace("purpose: p", "purpose: new")
    outputs["assessment"].write_text("# Assessment\n\nRanked changes.\n")
    outputs["plan"].write_text(plan)
elif kind == "list":
    proposals = [{"quote": "Alpha body", "change": "alpha", "reason": "decorative"},
                 {"quote": "A note about", "change": "beta", "reason": "word"},
                 {"quote": "long enough", "change": "gamma", "reason": "plain"}]
    if Path("new-proposal").exists():
        proposals[0]["change"] = "delta"
    if Path("no-candidates").exists():
        result("unchanged")
    else:
        result("proposed", proposals=proposals)
else:
    if kind == "apply":
        import yaml
        answers = yaml.safe_load(inputs["answers"].read_text().split("---\n")[1])
        kept = [item["proposal"]["change"] for item in answers["items"] if item["state"] == "approved"]
        revised = text.replace("user-verified: true\n", "") + f"{name} applied {' '.join(kept)}.\n"
    else:
        scope = inputs["scope"].read_text() if "scope" in inputs else "all"
        revised = text.replace("user-verified: true\n", "") + f"{name} ({scope}).\n"
    if name == "readability-and-flow" and ("BADPASS" in text or
            "RETITLE" in text and "was rejected" not in frame):
        revised = text.replace("\n# Alpha\n", "\n# Beta\n")
    if "LONGDESC" in text and name == "readability-and-flow":
        revised = revised.replace("description: ", "description: " + "padding " * 32, 1)
    if "BRIEFDRIFT" in text and name == "opening-and-title":
        path = Path("kb/notes/alpha.brief.md")
        path.write_text(path.read_text() + "Changed while the worker ran.\n")
    if "TOUCH" in text and name == "opening-and-title":
        Path("kb/notes/alpha.md").write_text(text + "The operator's sentence.\n")
    outputs["candidate"].write_text(revised)
    result("changed", changes=[f"{name} applied"])
'''
PROFILES = ("default: s\neffort: {simple: s, judgment: j}\nprofiles:\n"
            "  s: {harness: fake, launch-model: small, effort: low}\n"
            "  j: {harness: fake, launch-model: big, effort: high}\n")
NOTE = ("---\ndescription: A note about alpha that is long enough to describe what it is for\n"
        "type: types/note.md\nuser-verified: true\n---\n\n# Alpha\n\nAlpha body {words}.\n")
NOTE_PATH = "kb/notes/alpha.md"
PASSES = REPO_ROOT / "kb/instructions/simplification-passes"
EDIT_TYPES = ("kb/types/edit-result.md", "kb/types/edit-result.schema.yaml", "kb/types/answers.md",
              "kb/types/answers.schema.yaml")
FIX = "kb/instructions/fix-warnings/fix-strategy-taxonomy.md"
ORDINARY = ["pass readability-and-flow big", "pass place-external-systems small", "pass opening-and-title big"]


@pytest.fixture
def repo(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text() for rel in NOTE_TYPE_SPECS}
    files |= {f"kb/instructions/simplification-passes/{p.name}": p.read_text() for p in PASSES.glob("*.md")}
    files |= {rel: (REPO_ROOT / rel).read_text() for rel in (*EDIT_TYPES, FIX)}
    files |= {"kb/instructions/review-profiles.yaml": PROFILES, "kb/notes/COLLECTION.md": "# Notes\n"}
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    for args in (("init", "-q"), ("config", "user.email", "t@example.com"), ("config", "user.name", "t")):
        subprocess.run(["git", *args], cwd=root, check=True)
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    monkeypatch.setattr(revise_module, "Run", functools.partial(Run, sleep=lambda seconds: None))
    monkeypatch.chdir(root)
    script, log = tmp_path / "fake.py", tmp_path / "launches.log"
    script.write_text(FAKE)
    log.touch()
    harness = Harness(sys.executable, {"_subcommand": [str(script)], "_env": {"FAKE_LOG": str(log)}},
                      lambda profile: {"model": profile.launch_model}, model_used=lambda launch: "fake-model-1")
    return root, {"fake": harness}, log


def start(repo, words="", path=NOTE_PATH, text=None):
    text = NOTE.format(words=words) if text is None else text
    (repo[0] / path).parent.mkdir(parents=True, exist_ok=True)
    (repo[0] / path).write_text(text)
    subprocess.run(["git", "add", "."], cwd=repo[0], check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=repo[0], check=True)
    return text


def revise(repo, capsys, *args):
    before = repo[2].read_text().splitlines()
    code = main(["run", "revise", *args, "--timeout", "30"], harnesses=repo[1])
    captured = capsys.readouterr()
    return code, json.loads(captured.out) if code != 2 else captured.err, repo[2].read_text().splitlines()[len(before):]


def approve(repo, capsys, report):
    stop = report["waiting-for"]
    code = main(["approve", report["run-dir"], stop["file"], "--key", stop["key"]], harnesses=repo[1])
    captured = capsys.readouterr()
    assert code == 0, captured.err


def artifact_file(repo, report, name):
    return repo[0] / report["run-dir"] / "artifact" / name


def note_text(repo):
    return (repo[0] / NOTE_PATH).read_text()


def named_plan(tmp_path, passes=("readability-and-flow",), **fields):
    path = tmp_path / "custom.yaml"
    path.write_text(yaml.safe_dump({"purpose": "p", "defend": [], "stop": None,
                                   "passes": [{"pass": p} for p in passes], **fields}))
    return path


def decide(text, decisions, default=None):
    """Record the operator's decisions in an answers file's text, as the decide-items stop does.

    `decisions` maps an item's proposed `change`, or `text` for a text
    approval, to its state fields; `default` applies to every other item.
    """
    head, body = text.split("---\n")[1:]
    data = yaml.safe_load(head)
    for item in data["items"]:
        chosen = decisions.get(item["proposal"].get("change", item["id"]), default)
        if chosen is not None:
            item.update(chosen)
            if item["state"] != "pending":
                item.setdefault("decided-by", "operator")
                item.setdefault("decided-at", "2026-11-15T12:00:00Z")
    return "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n" + body


APPROVED = {"state": "approved"}


def rejected(reason):
    return {"state": "rejected", "reason": reason}


def answer(repo, report, decisions, default=APPROVED):
    """Decide the items of the answers file the report waits for; approving it is a separate step."""
    path = repo[0] / report["waiting-for"]["file"]
    path.write_text(decide(path.read_text(), decisions, default))


def approve_publication(repo, capsys, report, decision=APPROVED):
    assert report["waiting-for"]["file"].endswith("/publication-answers.md")
    answer(repo, report, {"text": decision})
    approve(repo, capsys, report)


def publish(repo, capsys, report, path=NOTE_PATH):
    approve_publication(repo, capsys, report)
    code, done, launches = revise(repo, capsys, path)
    assert code == 0 and done["complete"] and done["applied"], done
    assert launches == [], "approved publication replays all workers"
    return done


def test_new_run_requires_explicit_mode_and_fixed_plan_rejects_ignored_constraints(repo, capsys, tmp_path):
    original = start(repo)
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and "choose --plan FILE" in error and launches == []
    path = named_plan(tmp_path)
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path), "--defend", "Keep alpha")
    assert code == 2 and "takes purpose and defend from the plan" in error and launches == []
    assert note_text(repo) == original


def test_fixed_single_pass_has_no_planner_dependency_and_replays_to_publication(repo, capsys, tmp_path, monkeypatch):
    original = start(repo)
    path = named_plan(tmp_path, purpose="Improve the body for its reader", defend=["Alpha body holds."])
    plan = yaml.safe_load(path.read_text())
    plan["passes"][0]["scope"] = "body only"
    path.write_text(yaml.safe_dump(plan))

    def forbidden(*args, **kwargs):
        pytest.fail("fixed-plan execution constructed an assessment request")

    monkeypatch.setattr(revise_module, "_assessment_request", forbidden)
    _, ready, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert ready["mode"] == "fixed-plan" and launches == [ORDINARY[0]]
    assert not artifact_file(repo, ready, "assessment.md").exists()
    assert note_text(repo) == original and ready["guard"]["clean"]
    [call] = captured_inputs(repo[2])
    assert call["inputs"]["purpose"] == "Improve the body for its reader"
    assert call["inputs"]["scope"] == "body only"
    assert call["inputs"]["defend"] == "- Alpha body holds.\n"
    assert call["inputs"]["execution"] == (repo[0] / "kb" / revise_module.EXECUTION_REL).read_text()
    assert "passes" not in call["inputs"]
    path.unlink()  # repeats use captured inputs, not the now-missing source plan
    (repo[0] / "kb" / revise_module.INSTRUCTION_REL).unlink()
    unused = repo[0] / "kb/instructions/simplification-passes/plain-wording.md"
    unused.write_text(unused.read_text() + "\nUnrelated pass change.\n")
    _, repeated, launches = revise(repo, capsys, NOTE_PATH, "--profile-simple", "j")
    assert launches == [] and repeated["waiting-for"] == ready["waiting-for"]
    publish(repo, capsys, repeated)
    assert note_text(repo).endswith("readability-and-flow (body only).\n")
    # Published text has a different hash; a bare command must not turn into planning.
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and "choose --plan FILE" in error and launches == []


@pytest.mark.parametrize("missing", ["mode"])
def test_incomplete_recorded_options_never_fall_back_to_assessment(repo, capsys, tmp_path, missing):
    original = start(repo)
    path = named_plan(tmp_path)
    _, ready, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    options_path = repo[0] / ready["run-dir"] / "sweep.json"
    options = json.loads(options_path.read_text())
    del options[missing]
    options_path.write_text(json.dumps(options))
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and "--plan FILE" in error and launches == []
    assert note_text(repo) == original
    _, resumed, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert resumed["mode"] == "fixed-plan" and launches == []
    assert resumed["waiting-for"] == ready["waiting-for"]


def test_automatic_preparation_waits_for_publication_and_replays_after_approval(repo, capsys):
    original = start(repo)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess", "--purpose", "p")
    assert code == 0 and launches == ["assess - big", *ORDINARY]
    assert not report["complete"] and not report["applied"] and report["not-applied"]
    assert note_text(repo) == original and report["guard"]["clean"]
    for name in ("assessment.md", "plan.yaml", "final.md", "final.diff", "publication-answers.md"):
        assert artifact_file(repo, report, name).is_file()
    assert report["proposed"].endswith("/final.md")
    assert [p["profile"]["launch-model"] for p in report["passes"]] == ["big", "small", "big"]
    assert report["new-warnings"] == [] and "validation warnings" not in report["waiting-for"]["what"]
    code, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and repeated["waiting-for"] == report["waiting-for"]
    assert note_text(repo) == original
    done = publish(repo, capsys, repeated)
    assert note_text(repo) == artifact_file(repo, done, "final.md").read_text()
    assert "user-verified" not in note_text(repo)


@pytest.mark.parametrize("change", ["instruction", "profile", "brief", "plan"])
def test_changed_context_invalidates_publication_even_with_identical_final(repo, capsys, tmp_path, change):
    start(repo)
    brief = add_brief(repo[0], NOTE_PATH)
    path = named_plan(tmp_path)
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    candidate = artifact_file(repo, report, "final.md").read_text()
    approve_publication(repo, capsys, report)
    args = []
    if change == "instruction":
        target = repo[0] / "kb" / revise_module.EXECUTION_REL
        target.write_text(target.read_text() + "\nChanged instruction.\n")
    elif change == "profile":
        args = ["--profile-judgment", "s"]
    elif change == "brief":
        brief.write_text(brief.read_text() + "\nKeep another passage.\n")
    else:
        path = named_plan(tmp_path, purpose="new purpose")
        args = ["--plan", str(path)]
    original = note_text(repo)
    code, fresh, _ = revise(repo, capsys, NOTE_PATH, *args)
    assert code == 0 and fresh["waiting-for"] and not fresh["applied"]
    assert fresh["waiting-for"]["key"] != report["waiting-for"]["key"]
    assert artifact_file(repo, fresh, "final.md").read_text() == candidate
    assert note_text(repo) == original
    publish(repo, capsys, fresh)


@pytest.mark.parametrize("stopped", [False, True])
def test_captured_plan_edits_are_not_overrides_use_plan_option(repo, capsys, tmp_path, stopped):
    original = start(repo, "STOP" if stopped else "")
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    replacement = named_plan(tmp_path)
    artifact_file(repo, report, "plan.yaml").write_text(replacement.read_text())
    code, again, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and again["plan"] == report["plan"]
    assert note_text(repo) == original
    if stopped:
        assert again["complete"] and again["stop"] and again["waiting-for"] is None
        assert "--plan" in again["override"]["command"] and "approve-command" not in again["override"]
    code, fresh, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(replacement))
    assert code == 0 and fresh["stop"] is None and len(fresh["passes"]) == 1
    assert not any(line.startswith("assess") for line in launches)
    publish(repo, capsys, fresh)


@pytest.mark.parametrize("pass_name", ["plain-wording"])
def test_per_item_passes_stop_for_answers_and_unapproved_edits_are_not_used(repo, capsys, tmp_path, pass_name):
    original = start(repo)
    path = named_plan(tmp_path, passes=(pass_name,))
    _, waiting, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    model = "small" if pass_name == "plain-wording" else "big"
    assert launches == [f"list {pass_name} {model}"]
    assert re.search(rf"/artifact/{pass_name}-answers-[0-9a-f]{{12}}\.md$", waiting["waiting-for"]["file"])
    pending = yaml.safe_load((repo[0] / waiting["waiting-for"]["file"]).read_text().split("---\n")[1])
    assert pending["type"] == "types/answers.md" and pending["question"].endswith("/result.md")
    assert [item["state"] for item in pending["items"]] == ["pending"] * 3
    _, again, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and again["waiting-for"] == waiting["waiting-for"]
    answers = repo[0] / waiting["waiting-for"]["file"]
    answer(repo, waiting, {"beta": rejected("a registered word"),
                           "gamma": {"state": "deferred", "reason": "the term may be registered",
                                     "revisit": "when the vocabulary ledger decides"}})
    approve(repo, capsys, waiting)
    answers.write_text("unauthorized\n")
    _, ready, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [f"apply {pass_name} {model}"]
    assert ready["unapproved-edits"] and note_text(repo) == original
    assert f"{pass_name} applied alpha." in artifact_file(repo, ready, "final.md").read_text()
    [applied] = [c for c in captured_inputs(repo[2]) if c["kind"] == "apply"]
    assert "reason: a registered word" in applied["inputs"]["answers"]
    assert "unauthorized" not in applied["inputs"]["answers"]
    publish(repo, capsys, ready)


def _drop(text):
    data = yaml.safe_load(text.split("---\n")[1])
    del data["items"][1]
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n"


@pytest.mark.parametrize("damage, problem", [
    (_drop, "item 2: missing"),
    (lambda text: decide(text, {"beta": {"state": "rejected"}}), "'reason' is a required property"),
])
def test_invalid_answers_wait_for_a_corrected_file(repo, capsys, tmp_path, damage, problem):
    original = start(repo)
    path = named_plan(tmp_path, passes=("plain-wording",))
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    answers = repo[0] / waiting["waiting-for"]["file"]
    pending = answers.read_text()
    answers.write_text(damage(pending))
    approve(repo, capsys, waiting)
    code, blocked, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and not blocked["applied"] and note_text(repo) == original
    assert blocked["passes"][0]["state"] == "waiting" and problem in blocked["passes"][0]["reason"]
    assert blocked["waiting-for"]["key"] == waiting["waiting-for"]["key"] and problem in blocked["waiting-for"]["what"]
    answers.write_text(decide(pending, {"gamma": rejected("keep it")}, APPROVED))
    approve(repo, capsys, blocked)
    _, ready, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == ["apply plain-wording small"]
    assert ready["waiting-for"]["file"].endswith("publication-answers.md")


def test_changed_answers_invalidate_publication_even_if_candidate_is_identical(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=("plain-wording",))
    _, selection, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    answers = repo[0] / selection["waiting-for"]["file"]
    answer(repo, selection, {"gamma": rejected("first reason")})
    approve(repo, capsys, selection)
    _, ready, _ = revise(repo, capsys, NOTE_PATH)
    candidate = artifact_file(repo, ready, "final.md").read_text()
    approve_publication(repo, capsys, ready)
    answers.write_text(answers.read_text().replace("first reason", "the reason now differs"))
    approve(repo, capsys, selection)
    code, fresh, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and fresh["waiting-for"] and not fresh["applied"]
    assert launches == ["apply plain-wording small"]
    assert artifact_file(repo, fresh, "final.md").read_text() == candidate
    assert fresh["waiting-for"]["key"] != ready["waiting-for"]["key"]
    assert note_text(repo) == original


def test_approving_no_item_completes_without_publication(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=("plain-wording",))
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    answer(repo, waiting, {"alpha": rejected("alpha stays"), "beta": rejected("beta stays")}, default=None)
    approve(repo, capsys, waiting)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["complete"] and not done["applied"] and launches == []
    assert done["passes"][0]["reason"] == "the operator approved no item"
    assert note_text(repo) == original


@pytest.mark.parametrize("change", ["criterion", "profile", "retry"])
def test_changed_proposing_request_or_retried_proposal_requires_new_answers(repo, capsys, change):
    original = start(repo, "PLAIN")
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    answer(repo, waiting, {})
    approve(repo, capsys, waiting)
    args = []
    if change == "criterion":
        path = repo[0] / "kb/instructions/simplification-passes/plain-wording.md"
        path.write_text(path.read_text() + "\nChanged criterion.\n")
    elif change == "profile":
        args = ["--profile-simple", "j"]
    else:
        calls = recorded_calls(repo[0] / waiting["run-dir"])
        [call] = [c for c in calls if c["job"] == "plain-wording/propose" and c["status"] == "delivered"]
        (repo[0] / "new-proposal").touch()
        assert main(["retry", waiting["run-dir"], call["job"], "--key", call["key"]], harnesses=repo[1]) == 0
        capsys.readouterr()
    code, fresh, _ = revise(repo, capsys, NOTE_PATH, *args)
    assert code == 0 and not fresh["applied"] and fresh["passes"][1]["state"] == "waiting"
    assert fresh["waiting-for"]["key"] != waiting["waiting-for"]["key"]
    assert note_text(repo) == original


def test_brief_is_captured_for_assessment_passes_lists_and_apply(repo, capsys):
    start(repo, "PLAIN")
    brief = add_brief(repo[0], NOTE_PATH)
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    answer(repo, waiting, {})
    approve(repo, capsys, waiting)
    _, ready, _ = revise(repo, capsys, NOTE_PATH)
    calls = captured_inputs(repo[2])
    assert {c["kind"] for c in calls} == {"assess", "pass", "list", "apply"}
    assert all(c["inputs"]["brief"] == brief.read_text() for c in calls)
    assert all("## Headless write briefs" in c["inputs"]["execution"] for c in calls if c["kind"] != "assess")
    publish(repo, capsys, ready)


@pytest.mark.parametrize("kind", ["assess", "apply"])
def test_worker_brief_conflict_stops_without_publication(repo, capsys, kind):
    start(repo, "PLAIN")
    add_brief(repo[0], NOTE_PATH)
    original = note_text(repo)
    if kind == "apply":
        _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--assess")
        answer(repo, waiting, {})
        approve(repo, capsys, waiting)
    (repo[0] / f"brief-problem-{kind}").touch()
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 1 and "write brief" in report["stopped"] and not report["applied"]
    assert note_text(repo) == original and launches[-1].startswith(kind + " ")
    assert not any("place-external-systems" in line for line in launches)


@pytest.mark.parametrize("damage", ["wrong-name"])
def test_invalid_brief_stops_before_workers(repo, capsys, damage):
    start(repo)
    brief = add_brief(repo[0], NOTE_PATH)
    if damage == "missing":
        brief.unlink()
    elif damage == "wrong-type":
        brief.write_text(brief.read_text().replace("types/write-brief.md", "types/note.md"))
    else:
        path = repo[0] / NOTE_PATH
        path.write_text(path.read_text().replace("brief: alpha.brief.md", "brief: ../escape.brief.md"))
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 1 and "brief" in report["stopped"] and launches == []


@pytest.mark.parametrize("words", ["BRIEFDRIFT", "TOUCH"])
def test_concurrent_edits_block_publication(repo, capsys, words):
    start(repo, words)
    add_brief(repo[0], NOTE_PATH)
    original = note_text(repo)
    code, report, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 1 and report["conflict"] and not report["applied"]
    if words == "BRIEFDRIFT":
        assert "write brief" in report["conflict"] and note_text(repo) == original
    else:
        assert note_text(repo).endswith("The operator's sentence.\n")
        assert report["guard"]["changed"] == [NOTE_PATH]


@pytest.mark.parametrize("words", ["BADPLAN", "RETITLE", "BADPASS"])
def test_correction_attempts_keep_safety_bounds(repo, capsys, words):
    original = start(repo, words)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 0 and note_text(repo) == original
    if words == "BADPLAN":
        assert launches.count("assess - big") == 2
    elif words == "RETITLE":
        assert launches.count("pass readability-and-flow big") == 2
        assert "\n# Alpha\n" in artifact_file(repo, report, "final.md").read_text()
    else:
        assert report["passes"][0]["state"] == "problem"
        assert report["waiting-for"] is None and "problem" in report["not-applied"]
        assert not report["applied"]
        return
    publish(repo, capsys, report)


def test_launch_failure_replay_and_explicit_plan_change_reuse_unaffected_pass(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=("readability-and-flow", "place-external-systems"))
    failure = repo[0] / "fail-place-external-systems"
    failure.touch()
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 1 and report["stopped"]
    assert launches == [ORDINARY[0]] + [ORDINARY[1]] * 3
    assert note_text(repo) == original
    failure.unlink()
    plan = yaml.safe_load(path.read_text())
    plan["passes"][1]["scope"] = "§2"
    path.write_text(yaml.safe_dump(plan))
    code, ready, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 0 and launches == [ORDINARY[1]]
    publish(repo, capsys, ready)
    assert note_text(repo).endswith("readability-and-flow (all).\nplace-external-systems (§2).\n")


def test_launch_failure_can_resume_without_changing_the_plan(repo, capsys):
    original = start(repo)
    failure = repo[0] / "fail-place-external-systems"
    failure.touch()
    code, stopped, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 1 and stopped["stopped"]
    assert launches == ["assess - big", ORDINARY[0], *([ORDINARY[1]] * 3)]
    assert note_text(repo) == original
    failure.unlink()
    code, ready, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ORDINARY[1:]
    assert ready["run-dir"] == stopped["run-dir"] and note_text(repo) == original
    publish(repo, capsys, ready)


def test_retried_assessment_changes_plan_and_invalidates_publication(repo, capsys):
    original = start(repo)
    _, ready, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    candidate = artifact_file(repo, ready, "final.md").read_text()
    approve_publication(repo, capsys, ready)
    calls = recorded_calls(repo[0] / ready["run-dir"])
    [call] = [c for c in calls if c["job"] == "assessment" and c["status"] == "delivered"]
    (repo[0] / "new-proposal").touch()
    assert main(["retry", ready["run-dir"], "assessment", "--key", call["key"]], harnesses=repo[1]) == 0
    capsys.readouterr()
    code, fresh, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["assess - big", *ORDINARY]
    assert fresh["plan"]["purpose"] == "new"
    assert fresh["waiting-for"]["key"] != ready["waiting-for"]["key"]
    assert artifact_file(repo, fresh, "final.md").read_text() == candidate
    assert note_text(repo) == original


def test_candidate_file_edits_are_not_an_override(repo, capsys):
    original = start(repo)
    _, ready, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    candidate = artifact_file(repo, ready, "final.md")
    checked = candidate.read_text()
    candidate.write_text("Unchecked replacement.\n")
    _, waiting, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and waiting["waiting-for"]["key"] == ready["waiting-for"]["key"]
    assert not waiting["applied"] and not waiting["complete"]
    assert candidate.read_text() == checked and note_text(repo) == original
    publish(repo, capsys, waiting)
    assert note_text(repo) == checked


def test_edited_artifact_starts_new_run_without_reusing_publication(repo, capsys):
    start(repo)
    _, ready, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    approve_publication(repo, capsys, ready)
    edited = note_text(repo) + "The operator's sentence.\n"
    (repo[0] / NOTE_PATH).write_text(edited)
    code, fresh, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 0 and fresh["run-dir"] != ready["run-dir"] and launches == ["assess - big", *ORDINARY]
    assert not fresh["applied"] and note_text(repo) == edited


def test_every_pass_candidate_comes_from_the_edit_route(repo, capsys, tmp_path):
    start(repo)
    path = named_plan(tmp_path, passes=("readability-and-flow", "plain-wording"))
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    answer(repo, waiting, {"beta": rejected("a registered word")})
    approve(repo, capsys, waiting)
    _, ready, _ = revise(repo, capsys, NOTE_PATH)
    held = {}
    for record in sorted((repo[0] / ready["run-dir"] / "artifact/edits").glob("*/observation.json")):
        data = json.loads(record.read_text())
        [result] = [name for name in data["completed-results"] if name.endswith("/result.md")]
        held[data["request"]["call-job"]] = yaml.safe_load((record.parent / result).read_text().split("---\n")[1])
    assert {job: data["outcome"] for job, data in held.items()} == {
        "readability-and-flow": "changed", "plain-wording/propose": "proposed", "plain-wording/apply": "changed"}
    assert held["plain-wording/propose"]["profile"]["launch-model"] == "small"
    for state in ready["passes"]:
        job = state["name"] if state["name"] == "readability-and-flow" else f"{state['name']}/apply"
        assert (repo[0] / held[job]["candidate"]).read_text() == (repo[0] / state["text"]).read_text()


def test_decisions_command_lists_the_answers_of_a_revise_run(repo, capsys, tmp_path):
    start(repo)
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    answer(repo, waiting, {"beta": rejected("a registered word")})
    approve(repo, capsys, waiting)
    _, ready, _ = revise(repo, capsys, NOTE_PATH)
    publish(repo, capsys, ready)
    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    found = json.loads(capsys.readouterr().out)
    listed = [(e["class"], e["unit"], e["decided-by"], e["decision"], e["item"], e["reason"]) for e in found]
    final = f"{ready['run-dir']}/artifact/final.md"
    assert sorted(listed) == [
        ("plain-wording", "item", "operator", "approved", "Alpha body -> alpha", None),
        ("plain-wording", "item", "operator", "approved", "long enough -> gamma", None),
        ("plain-wording", "item", "operator", "rejected", "A note about -> beta", "a registered word"),
        ("publication", "bundle", "operator", "approved", final if len(final) <= 80 else final[:79] + "…", None)]


# --- Earlier decisions ---------------------------------------------------------------------

def items(repo, report):
    """The items of the answers file the report waits for, by proposed change."""
    head = (repo[0] / report["waiting-for"]["file"]).read_text().split("---\n")[1]
    return {item["proposal"]["change"]: item for item in yaml.safe_load(head)["items"]}


def change_decision(repo, report, change, decision):
    """Record the operator's changed decision on a carried item: the earlier decision and `carried-from` go."""
    path = repo[0] / report["waiting-for"]["file"]
    head, body = path.read_text().split("---\n")[1:]
    data = yaml.safe_load(head)
    for item in data["items"]:
        if item["proposal"]["change"] == change:
            for name in ("reason", "revisit", "carried-from"):
                item.pop(name, None)
            item.update(decision)
    path.write_text("---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n" + body)


def first_decisions(repo, capsys, tmp_path, words=""):
    """A plain-wording run on the note with `words`: alpha approved, beta rejected, gamma left pending."""
    start(repo, words)
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    answer(repo, waiting, {"alpha": APPROVED, "beta": rejected("a registered word")}, default=None)
    approve(repo, capsys, waiting)
    return waiting


def test_identical_proposals_carry_earlier_decisions_and_the_stop_still_waits(repo, capsys, tmp_path):
    first = first_decisions(repo, capsys, tmp_path)
    start(repo, "changed")                                   # another text: another run
    plan = str(named_plan(tmp_path, passes=("plain-wording",)))
    _, second, launches = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    assert launches == ["list plain-wording small"] and second["run-dir"] != first["run-dir"]
    found = items(repo, second)
    assert found["alpha"]["state"] == "approved" and found["alpha"]["carried-from"] == first["waiting-for"]["file"]
    assert (found["beta"]["state"], found["beta"]["reason"], found["beta"]["decided-at"]) == (
        "rejected", "a registered word", "2026-11-15T12:00:00Z")
    assert found["beta"]["carried-from"] == first["waiting-for"]["file"]
    assert found["gamma"]["state"] == "pending" and "carried-from" not in found["gamma"]   # pending is not carried
    path = repo[0] / second["waiting-for"]["file"]
    assert edits.answered(repo[0], path, path.read_text())[1] == []
    [listed] = [c for c in captured_inputs(repo[2]) if c["kind"] == "list" and "changed" in c["inputs"]["text"]]
    told = listed["inputs"]["earlier-decisions"]
    assert "> Alpha body" in told and "Operator's reason: a registered word" in told
    assert first["waiting-for"]["file"] in told
    captured = json.loads((repo[0] / second["run-dir"] / revise_module.EARLIER_FILE).read_text())
    assert [d["proposal"]["change"] for d in captured["decisions"]] == ["alpha", "beta"]

    # The operator changes beta and decides gamma; that later decision wins in the next run.
    change_decision(repo, second, "beta", {"state": "approved", "decided-by": "operator",
                                           "decided-at": "2026-11-16T09:00:00Z"})
    answer(repo, second, {"gamma": rejected("keep it")}, default=None)
    approve(repo, capsys, second)
    start(repo, "changed again")
    _, third, launches = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    assert launches == ["list plain-wording small"]
    found = items(repo, third)
    assert {change: item["state"] for change, item in found.items()} == {
        "alpha": "approved", "beta": "approved", "gamma": "rejected"}
    assert found["beta"]["carried-from"] == second["waiting-for"]["file"] and "reason" not in found["beta"]
    assert found["alpha"]["carried-from"] == first["waiting-for"]["file"]
    assert third["waiting-for"]["file"].endswith(".md") and not third["complete"]   # every item carried; it waits
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["waiting-for"] == third["waiting-for"]

    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    listed = json.loads(capsys.readouterr().out)
    carried = {(e["run"], e["item"]): e["carried-from"] for e in listed if e["class"] == "plain-wording"}
    assert carried[(second["run-dir"], "Alpha body -> alpha")] == first["waiting-for"]["file"]
    assert carried[(second["run-dir"], "A note about -> beta")] is None
    assert main(["decisions", "--note", NOTE_PATH]) == 0
    assert f"carried-from: {first['waiting-for']['file']}" in capsys.readouterr().out


def test_a_repeat_keeps_its_earlier_decisions_after_another_run_decides(repo, capsys, tmp_path):
    first_decisions(repo, capsys, tmp_path)
    plan = str(named_plan(tmp_path, passes=("plain-wording",)))
    second_text = start(repo, "second")
    _, second, _ = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    start(repo, "third")
    _, third, _ = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    answer(repo, third, {"gamma": rejected("keep it")}, default=None)
    approve(repo, capsys, third)
    start(repo, text=second_text)                            # back to the second text: its run repeats
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["waiting-for"] == second["waiting-for"]
    assert items(repo, repeated)["gamma"]["state"] == "pending"


# --- Focused plans and findings ------------------------------------------------------------

GATE = "kb/instructions/review-gates/prose/residue.md"


def stored(repo, outcome, gate=GATE, depth=2, note=NOTE_PATH, found=None, decided=False):
    """Write a current review result for `note` against `gate`; return its repository path.

    `info` writes a `pass` result that holds one INFO-level finding. `found`
    replaces the one fixture finding. `decided` writes the result as a review
    that received the operator's current finding decisions on the pair.
    """
    root = repo[0]
    path = root / gate
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\ndepth: {depth}\nwatches: [body]\n---\n\n# Residue\n\nFlag residue.\n")
    copy_contract(root / "kb")
    level = [{"scope": "document", "quotes": [], "reason": "A fixture note", "level": "info"}]
    made = make_result(note, (root / note).read_text(), gate, path.read_text(),
                       outcome="pass" if outcome == "info" else outcome,
                       profile={"harness": "fake", "launch-model": "m", "effort": "low"}, model="fake-model-1",
                       run="r", launch="L1", completed_at="2026-11-16T00:00:00Z", body="# Review\n\nFound it.\n",
                       findings=found if found is not None else level if outcome == "info" else findings(outcome),
                       evidence=evidence(root))
    if decided:
        made = dataclasses.replace(made, criterion_sha256=results.criterion_sha256(
            path.read_text(), decisions.review_inputs(root, note)[gate]))
    return write_result(root, made).relative_to(root).as_posix()


def test_pass_runs_a_one_entry_plan_and_repeats_replay_it(repo, capsys):
    original = start(repo)
    with pytest.raises(SystemExit):
        main(["run", "revise", NOTE_PATH, "--pass", "readability-and-flow", "--assess"], harnesses=repo[1])
    capsys.readouterr()
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--pass", "polish")
    assert code == 2 and "unknown pass `polish`" in error and launches == []
    code, ready, launches = revise(repo, capsys, NOTE_PATH, "--pass", "readability-and-flow", "--purpose", "Readers")
    assert code == 0 and ready["mode"] == "fixed-plan" and launches == [ORDINARY[0]]
    assert ready["plan"] == {"purpose": "Readers", "defend": [], "stop": None,
                             "passes": [{"pass": "readability-and-flow", "scope": None}]}
    assert not artifact_file(repo, ready, "assessment.md").exists() and note_text(repo) == original
    code, error, _ = revise(repo, capsys, NOTE_PATH, "--purpose", "Others")
    assert code == 2 and "takes purpose and defend from the plan" in error
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["waiting-for"] == ready["waiting-for"]
    publish(repo, capsys, repeated)


def test_finding_runs_the_fix_with_its_result_as_input(repo, capsys):
    start(repo)
    finding = stored(repo, "warn")
    code, ready, launches = revise(repo, capsys, NOTE_PATH, "--finding", finding)
    assert code == 0 and launches == ["pass fix-strategy-taxonomy big"]
    assert ready["plan"]["passes"] == [{"pass": "fix-strategy-taxonomy", "scope": None, "finding": finding}]
    [state] = ready["passes"]
    assert state["name"] == "fix-strategy-taxonomy/prose/residue"
    assert state["finding"] == finding and state["state"] == "applied"
    [call] = captured_inputs(repo[2])
    assert call["inputs"]["finding"] == (repo[0] / finding).read_text()
    _, again, launches = revise(repo, capsys, NOTE_PATH, "--finding", str(repo[0] / finding))
    assert launches == [] and again["waiting-for"] == ready["waiting-for"]
    publish(repo, capsys, again)


def test_finding_must_be_a_review_result_of_the_same_note(repo, capsys):
    start(repo)
    start(repo, path="kb/notes/beta.md", text=NOTE.format(words="beta"))
    other = stored(repo, "warn", note="kb/notes/beta.md")
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--finding", other)
    assert code == 2 and "not of kb/notes/alpha.md" in error and launches == []
    code, error, _ = revise(repo, capsys, NOTE_PATH, "--finding", NOTE_PATH)
    assert code == 2 and "is not a review result" in error


def test_plan_entries_for_the_fix_carry_a_finding_at_its_criterion_depth(repo, capsys, tmp_path):
    start(repo)
    finding = stored(repo, "warn")
    fix = {"pass": revise_module.FIX, "finding": finding}
    path = tmp_path / "plan.yaml"
    for entries, problem in (([{"pass": revise_module.FIX}], "fixes one review finding"),
                             ([{"pass": "readability-and-flow", "finding": finding}], "takes no `finding`"),
                             ([{"pass": "opening-and-title"}, fix], "must run before `opening-and-title`"),
                             ([fix, fix], "is listed twice")):
        path.write_text(yaml.safe_dump({"purpose": "p", "defend": [], "stop": None, "passes": entries}))
        code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
        assert code == 2 and problem in error and launches == [], error
    path.write_text(yaml.safe_dump({"purpose": "p", "defend": [], "stop": None,
                                    "passes": [fix, {"pass": "readability-and-flow"}]}))
    code, _, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 0 and launches == ["pass fix-strategy-taxonomy big", ORDINARY[0]]


@pytest.mark.slow
def test_assessment_receives_fresh_warn_and_fail_results_only(repo, capsys):
    start(repo, "FIXIT")
    _, plain, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    [call] = [c for c in captured_inputs(repo[2]) if c["kind"] == "assess"]
    assert plain["findings"] == [] and not any(name.startswith("finding") for name in call["inputs"])
    assert revise_module.FIX not in call["inputs"]["passes"]
    start(repo, "FIXIT again")                  # another text, so another run: a run keeps the inputs it assessed
    warned = stored(repo, "warn")
    stored(repo, "info", gate="kb/instructions/review-gates/prose/hedging.md")
    failed = stored(repo, "fail", gate="kb/instructions/review-gates/sentence/packing.md", depth=5)
    stale = stored(repo, "warn", gate="kb/instructions/review-gates/prose/stale.md")
    gate = repo[0] / "kb/instructions/review-gates/prose/stale.md"
    gate.write_text(gate.read_text() + "Changed criterion.\n")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 0 and sorted(report["findings"]) == sorted([warned, failed]) and stale not in report["findings"]
    assert launches == ["assess - big", "pass fix-strategy-taxonomy big", *ORDINARY]
    call = [c for c in captured_inputs(repo[2]) if c["kind"] == "assess"][-1]
    given = {name: text for name, text in call["inputs"].items() if name.startswith("finding")}
    assert sorted(given.values()) == sorted((repo[0] / path).read_text() for path in (warned, failed))
    assert revise_module.FIX in call["inputs"]["passes"]
    assert report["passes"][0]["finding"] == report["plan"]["passes"][0]["finding"]
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["waiting-for"]["key"] == report["waiting-for"]["key"]


# --- Triage ------------------------------------------------------------------------------------

PACKING = "kb/instructions/review-gates/sentence/packing.md"
HEDGING = "kb/instructions/review-gates/prose/hedging.md"


def finding(reason, level="warn"):
    return {"scope": "document", "quotes": [], "reason": reason, "level": level}


def triaged(repo, capsys, report, chosen):
    """Record the operator's decisions in each triage answers file and approve it.

    `chosen` maps a criterion id to the decisions by item id, as `decide()` takes them.
    """
    for state in report["triage"]["results"]:
        path = repo[0] / state["answers"]
        path.write_text(decide(path.read_text(), chosen[state["criterion"]]))
        stop = state["waiting-for"]
        assert main(["approve", report["run-dir"], stop["file"], "--key", stop["key"]], harnesses=repo[1]) == 0
    capsys.readouterr()


def test_triage_without_warn_or_fail_findings_changes_nothing(repo, capsys):
    original = start(repo)
    stored(repo, "info")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--triage")
    assert code == 0 and report["complete"] and report["mode"] == "triage" and launches == []
    assert report["triage"] == {"results": [], "what": revise_module.NOTHING_TO_TRIAGE}
    assert report["plan"] is None and report["proposed"] is None and note_text(repo) == original


def test_triage_waits_for_each_answers_file_and_rejections_plan_nothing(repo, capsys):
    original = start(repo)
    late = stored(repo, "fail", gate=PACKING, depth=5)
    early = stored(repo, "warn")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--triage")
    assert code == 0 and launches == [] and not report["complete"] and report["plan"] is None
    listed = report["triage"]["results"]
    assert [(s["result"], s["criterion"], s["state"]) for s in listed] == [
        (early, "prose/residue", "waiting"), (late, "sentence/packing", "waiting")]     # in depth order
    assert report["waiting-for"] == listed[0]["waiting-for"]
    assert re.fullmatch(r".*/artifact/finding-answers-[0-9a-f]{12}\.md", listed[0]["answers"])
    assert (repo[0] / listed[0]["question"]).read_text() == (repo[0] / early).read_text()
    head = yaml.safe_load((repo[0] / listed[0]["answers"]).read_text().split("---\n")[1])
    assert head["question"] == listed[0]["question"]
    assert head["items"] == [{"id": "1", "proposal": findings("warn")[0], "state": "pending"}]
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["triage"] == report["triage"]

    triaged(repo, capsys, report, {"prose/residue": {"1": rejected("wrong for this note only")},
                                   "sentence/packing": {"1": rejected("the criterion is too broad")}})
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["complete"] and launches == []
    assert done["plan"]["passes"] == [] and done["plan"]["purpose"] == revise_module.TRIAGE_PURPOSE
    assert [s["state"] for s in done["triage"]["results"]] == ["decided", "decided"]
    assert done["proposed"] is None and not done["applied"] and note_text(repo) == original

    assert main(["decisions", "--note", NOTE_PATH, "--class", "finding", "--json"]) == 0
    listed = json.loads(capsys.readouterr().out)
    assert sorted((e["unit"], e["decided-by"], e["decision"], e["item"], e["reason"]) for e in listed) == [
        ("item", "operator", "rejected", "prose/residue: warn: A fixture finding", "wrong for this note only"),
        ("item", "operator", "rejected", "sentence/packing: fail: A fixture finding", "the criterion is too broad")]


def test_triage_fixes_only_results_with_an_approved_finding(repo, capsys):
    start(repo)
    two = stored(repo, "warn", found=[finding("first"), finding("second")])
    stored(repo, "warn", gate=HEDGING, depth=3, found=[finding("hedged")])
    stored(repo, "fail", gate=PACKING, depth=5)
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage", "--purpose", "Readers")
    assert [s["criterion"] for s in report["triage"]["results"]] == ["prose/residue", "prose/hedging",
                                                                     "sentence/packing"]
    triaged(repo, capsys, report, {"prose/residue": {"1": APPROVED, "2": rejected("not residue")},
                                   "prose/hedging": {"1": rejected("the hedge is needed")},
                                   "sentence/packing": {"1": APPROVED}})
    code, ready, launches = revise(repo, capsys, NOTE_PATH)
    questions = {s["criterion"]: s["question"] for s in ready["triage"]["results"]}
    assert code == 0 and launches == ["pass fix-strategy-taxonomy big", "pass fix-strategy-taxonomy big"]
    assert ready["plan"] == {"purpose": "Readers", "defend": [], "stop": None, "passes": [
        {"pass": revise_module.FIX, "scope": None, "finding": questions["prose/residue"]},
        {"pass": revise_module.FIX, "scope": None, "finding": questions["sentence/packing"]}]}
    assert [s["state"] for s in ready["passes"]] == ["applied", "applied"]
    fixes = [c for c in captured_inputs(repo[2]) if c["pass"] == revise_module.FIX]
    answered = {s["question"]: (repo[0] / s["answers"]).read_text() for s in ready["triage"]["results"]}
    assert fixes[0]["inputs"]["finding"] == (repo[0] / two).read_text()
    assert fixes[0]["inputs"][revise_module.FINDING_ANSWERS] == answered[questions["prose/residue"]]
    assert "not residue" in fixes[0]["inputs"][revise_module.FINDING_ANSWERS]
    assert fixes[1]["inputs"][revise_module.FINDING_ANSWERS] == answered[questions["sentence/packing"]]
    assert ready["waiting-for"]["file"].endswith("/publication-answers.md")
    publish(repo, capsys, ready)


def test_a_triage_repeat_keeps_its_results_after_the_store_changes(repo, capsys):
    start(repo)
    result = stored(repo, "warn")
    captured = (repo[0] / result).read_text()
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    stored(repo, "fail", found=[finding("a new finding", "fail")])      # a new review replaces the result
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["triage"] == report["triage"] and repeated["findings"] == [result]
    triaged(repo, capsys, repeated, {"prose/residue": {"1": APPROVED}})
    _, _, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == ["pass fix-strategy-taxonomy big"]
    [fix] = [c for c in captured_inputs(repo[2]) if c["pass"] == revise_module.FIX]
    assert fix["inputs"]["finding"] == captured != (repo[0] / result).read_text()


def test_a_triage_carries_over_the_decision_on_an_identical_finding(repo, capsys):
    start(repo)
    stored(repo, "warn", found=[finding("same"), finding("other")])
    _, first, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    triaged(repo, capsys, first, {"prose/residue": {"1": rejected("wrong for this note only"), "2": APPROVED}})
    start(repo, "changed")                                   # another text: another run
    stored(repo, "warn", found=[finding("same"), finding("other, reworded")], decided=True)
    _, second, launches = revise(repo, capsys, NOTE_PATH, "--triage")
    assert launches == [] and second["run-dir"] != first["run-dir"] and not second["complete"]
    head = yaml.safe_load((repo[0] / second["waiting-for"]["file"]).read_text().split("---\n")[1])
    carried, asked = head["items"]
    assert (carried["state"], carried["reason"], carried["carried-from"]) == (
        "rejected", "wrong for this note only", first["triage"]["results"][0]["answers"])
    assert asked["state"] == "pending" and "carried-from" not in asked
    captured = json.loads((repo[0] / second["run-dir"] / revise_module.EARLIER_FILE).read_text())["decisions"]
    assert sorted((d["criterion"], d["proposal"]["reason"], d["state"]) for d in captured) == [
        (GATE, "other", "approved"), (GATE, "same", "rejected")]


def frontmatter_only(text, tag):
    """The note `text` with another frontmatter line: another run, and the same body the gate watches."""
    return text.replace("type: types/note.md\n", f"type: types/note.md\ntags: [{tag}]\n")


def assessed_inputs(repo):
    return [c for c in captured_inputs(repo[2]) if c["kind"] == "assess"][-1]["inputs"]


@pytest.mark.slow
def test_the_assessor_gets_no_finding_the_operator_rejected_in_that_result(repo, capsys):
    text = start(repo, "FIXIT")
    stored(repo, "warn", found=[finding("same")])
    _, first, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    triaged(repo, capsys, first, {"prose/residue": {"1": rejected("wrong for this note only")}})
    assert results.freshness(repo[0], NOTE_PATH, GATE) == results.Freshness("stale", ("criterion",))

    # A later review that received the rejection raises it again beside two new findings.
    start(repo, text=frontmatter_only(text, "a"))
    answered = stored(repo, "warn", found=[finding("same"), finding("later"), finding("approved")], decided=True)
    assert results.freshness(repo[0], NOTE_PATH, GATE).state == "fresh"
    _, second, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    head = yaml.safe_load((repo[0] / second["waiting-for"]["file"]).read_text().split("---\n")[1])
    assert head["items"][0]["state"] == "rejected" and "carried-from" in head["items"][0]
    triaged(repo, capsys, second, {"prose/residue": {
        "2": {"state": "deferred", "reason": "after the rewrite", "revisit": "when the section is rewritten"},
        "3": APPROVED}})
    assert results.freshness(repo[0], NOTE_PATH, GATE).state == "fresh", "only a new rejection stales the pair"

    start(repo, text=frontmatter_only(text, "b"))
    revise(repo, capsys, NOTE_PATH, "--assess")
    given = assessed_inputs(repo)
    shown = yaml.safe_load(given["finding-1"].split("---\n")[1])
    assert [f["reason"] for f in shown["findings"]] == ["later", "approved"]
    assert shown["criterion-sha256"] == yaml.safe_load((repo[0] / answered).read_text().split("---\n")[1])[
        "criterion-sha256"]
    told = given["earlier-decisions"]
    assert "Reviewer's reason: same" in told and "Operator's reason: wrong for this note only" in told
    assert "Reviewer's reason: later" in told and "Revisit when: when the section is rewritten" in told
    assert "Reviewer's reason: approved" not in told

    # A new review replaces the answered result: the finding comes back, with the decision beside it.
    replaced = stored(repo, "warn", found=[finding("same"), finding("other")], decided=True)
    start(repo, text=frontmatter_only(text, "c"))
    revise(repo, capsys, NOTE_PATH, "--assess")
    given = assessed_inputs(repo)
    assert given["finding-1"] == (repo[0] / replaced).read_text()
    assert "Operator's reason: wrong for this note only" in given["earlier-decisions"]


def test_answers_create_takes_a_review_result_but_writes_outside_the_store(repo, capsys, tmp_path):
    start(repo)
    result = stored(repo, "warn")
    assert main(["answers", "create", "--from", result]) == 2
    assert "would be read as a review result" in capsys.readouterr().err
    assert main(["answers", "create", "--from", result, "--to", "kb/work/residue-answers.md"]) == 0
    capsys.readouterr()
    head = yaml.safe_load((repo[0] / "kb/work/residue-answers.md").read_text().split("---\n")[1])
    assert head["items"] == [{"id": "1", "proposal": findings("warn")[0], "state": "pending"}]


# --- The full procedure ---------------------------------------------------------------------

REVIEW_FAKE = FAKE_RESULT + r'''
import json, os, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text()
if frame.removeprefix("Task:\n").startswith("Review one note"):
    def listed(name):
        return re.search(rf"^- {re.escape(name)}: (.+)$", frame, re.MULTILINE).group(1)
    names = [a or b for a, b in re.findall(r"The criterion is `([^`]+)`|^- `([^`]+)`: its text is",
                                           frame, re.MULTILINE)]
    with open(os.environ["FAKE_LOG"], "a") as log:
        log.write("review " + ",".join(sorted(Path(name).stem for name in names)) + "\n")
    if "NOREVIEW" in Path(listed("note.md")).read_text() and "critique" in names[0]:
        Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(
            json.dumps({"kind": "unable", "message": "cannot review"}))
        sys.exit(0)
    for output in re.findall(r"^- (review[^:]*\.md): ", frame, re.MULTILINE):
        criterion = names[0] if output == "review.md" else output
        outcome = "report" if "outcome: report" in frame else "warn" if "warned" in criterion else "pass"
        Path(listed(output)).write_text(review_text(outcome, criterion))
    sys.exit(0)
'''


def review_operation(depth, gate_id=None):
    head = f"type: types/review-gate.md\ngate_id: {gate_id}\nstaleness: changed\n" if gate_id else ""
    return f"---\n{head}depth: {depth}\n---\n\n# Operation\n\nJudge it.\n"


REVIEW_FILES = {
    "kb/instructions/review-gates/prose/residue.md": review_operation(2, "prose/residue"),
    "kb/instructions/review-gates/prose/warned.md": review_operation(2, "prose/warned"),
    "kb/instructions/review-gates/sentence/packing.md": review_operation(5, "sentence/packing"),
    "kb/instructions/compression-bundle/detail-overhang.md": review_operation(4, "compression/detail-overhang"),
    "kb/instructions/compression-bundle/high-impact-simplification-synthesis.md": review_operation(4),
    "kb/instructions/critique-note.md": review_operation(1),
    "kb/instructions/composition-friction-gate.md": review_operation(1),
    "kb/instructions/premise-decomposition-gate.md": review_operation(1),
    "kb/instructions/role-in-the-kb-gate.md": review_operation(1),
    "kb/reports/COLLECTION.md": ("---\ntype: types/collection-contract.md\nunquoted-source-limit: 0\n---\n\n"
                                 "# Reports\n\nRetained operational evidence.\n"),
}
REVIEWS = {"review residue,warned", "review packing", "review detail-overhang", "review critique-note",
           "review composition-friction-gate", "review premise-decomposition-gate"}
SYNTHESIS = "review high-impact-simplification-synthesis"
ROLE = "review role-in-the-kb-gate"


@pytest.fixture
def reviewed(repo, tmp_path):
    """The revise repository with review operations that declare a depth, and a fake that also reviews."""
    for rel, text in REVIEW_FILES.items():
        (repo[0] / rel).parent.mkdir(parents=True, exist_ok=True)
        (repo[0] / rel).write_text(text)
    copy_contract(repo[0] / "kb")
    (tmp_path / "fake.py").write_text(REVIEW_FAKE + FAKE)
    return repo


@pytest.mark.slow
def test_full_reviews_then_assesses_with_findings_and_depth_one_reports(reviewed, capsys):
    repo = reviewed
    (repo[0] / "kb/notes/beta.md").parent.mkdir(parents=True, exist_ok=True)
    (repo[0] / "kb/notes/beta.md").write_text(NOTE.format(words="beta") + "\nBeta cites [Alpha](./alpha.md).\n")
    original = start(repo)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--full", "--purpose", "p")
    assert code == 0 and report["mode"] == "full" and note_text(repo) == original
    assert set(launches[:6]) == REVIEWS and launches[6:8] == [SYNTHESIS, ROLE]
    assert launches[8:] == ["assess - big", *ORDINARY]
    assert [sweep["counts"] for sweep in report["reviews"]] == [{"reviewed": 7}, {"reviewed": 1}, {"reviewed": 1}]
    store = repo[0] / "kb/reports/state/review/results" / NOTE_PATH
    role = repo[0] / report["reviews"][2]["run-dir"]
    assert role.name == "role" and not (store / "kb/instructions/role-in-the-kb-gate.md").exists()
    [given] = role.glob("artifact/reviews/*/inputs/operational/inbound.md")
    assert "kb/notes/beta.md" in given.read_text() and "Beta cites" in given.read_text()
    bundle = store / "kb/instructions/compression-bundle"
    assert (store / "prose/warned.md").is_file() and (bundle / "detail-overhang.md").is_file()
    assert not (bundle / "high-impact-simplification-synthesis.md").exists(), "the synthesis publishes no result"
    assert not (store / "kb/types").exists(), "the type lens declares no depth"
    [call] = [c for c in captured_inputs(repo[2]) if c["kind"] == "assess"]
    assert call["inputs"]["finding-1"] == (store / "prose/warned.md").read_text()
    assert "finding-2" not in call["inputs"]
    reports = sorted(text for name, text in call["inputs"].items() if name.startswith("report-"))
    assert len(reports) == 5 and all("outcome" in text for text in reports), \
        "three at depth 1, the synthesis and the role report"
    assert any("## Role" in text for text in reports) and "role report" in call["inputs"]["criterion"]
    assert len(report["findings"]) == 6
    passes = [c for c in captured_inputs(repo[2]) if c["kind"] not in ("assess", "review")]
    assert passes and all(c["inputs"].get("kb-role") == "It supplies one term.\nRelied on: the term. Unused: none."
                          for c in passes), "each pass receives the role section alone"
    (store / "prose/warned.md").unlink()       # the store changes after the assessment; the run kept its inputs
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["mode"] == "full"
    assert repeated["waiting-for"]["key"] == report["waiting-for"]["key"]
    assert repeated["findings"] == report["findings"] and repeated["reviews"] == report["reviews"]
    publish(repo, capsys, repeated)


@pytest.mark.slow
def test_full_reuses_fresh_review_results(reviewed, capsys):
    repo = reviewed
    start(repo)
    assert main(["run", "gates", NOTE_PATH, "--criteria", "prose", "--timeout", "30"], harnesses=repo[1]) == 0
    capsys.readouterr()
    _, report, launches = revise(repo, capsys, NOTE_PATH, "--full")
    assert sorted(repo[2].read_text().splitlines()[:2]) == ["review residue", "review warned"]
    assert set(launches[:5]) == REVIEWS - {"review residue,warned"} and launches[5:7] == [SYNTHESIS, ROLE]
    assert report["reviews"][0]["counts"] == {"fresh": 2, "reviewed": 5}


def gates_run(repo, capsys, *args):
    code = main(["run", "gates", NOTE_PATH, "--criteria", "prose", *args, "--timeout", "30"], harnesses=repo[1])
    report = json.loads(capsys.readouterr().out)
    assert code == 0, report
    return report


def test_a_rejection_reaches_the_next_review_of_that_pair_only(reviewed, capsys):
    repo = reviewed
    start(repo)
    gates_run(repo, capsys, "--grouping", "bundle")
    store = repo[0] / "kb/reports/state/review/results" / NOTE_PATH / "prose"
    residue, warned = (store / "residue.md").read_bytes(), (store / "warned.md").read_bytes()
    criterion = (repo[0] / "kb/instructions/review-gates/prose/residue.md").read_text()
    stored_hash = yaml.safe_load(residue.decode().split("---\n")[1])["criterion-sha256"]
    assert stored_hash == hashlib.sha256(criterion.encode()).hexdigest() == results.criterion_sha256(criterion)

    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    assert [s["criterion"] for s in report["triage"]["results"]] == ["prose/warned"]
    triaged(repo, capsys, report, {"prose/warned": {"1": rejected("the criterion is too broad")}})
    rows = {Path(row.criterion).stem: row.freshness for row in results.note_rows(repo[0], NOTE_PATH)}
    assert rows["residue"].state == "fresh" and rows["warned"] == results.Freshness("stale", ("criterion",))

    before = repo[2].read_text().splitlines()
    swept = gates_run(repo, capsys, "--grouping", "bundle")
    assert repo[2].read_text().splitlines()[len(before):] == ["review warned"], "only the pair with a rejection"
    assert (store / "residue.md").read_bytes() == residue and (store / "warned.md").read_bytes() != warned
    [given] = (repo[0] / swept["run-dir"]).glob("artifact/reviews/*/inputs/operational/finding-decisions.md")
    text = given.read_text()
    assert decisions.REVIEW_RULE in text and "Operator's reason: the criterion is too broad" in text
    assert "Reviewer's reason: A fixture finding" in text
    request = json.loads((repo[0] / swept["run-dir"] / "review-request.json").read_text())
    assert list(request["finding-decisions"]) == [f"{NOTE_PATH}::prose/warned"]
    assert all(row.freshness.state == "fresh" for row in results.note_rows(repo[0], NOTE_PATH))
    before = repo[2].read_text().splitlines()
    gates_run(repo, capsys)
    assert repo[2].read_text().splitlines()[len(before):] == []


@pytest.mark.slow
def test_a_plan_stop_leaves_an_answers_file_that_takes_a_resolution_and_refs(reviewed, capsys):
    repo = reviewed
    start(repo, "STOP")
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--full")
    stop = report["stop-answers"]
    path = repo[0] / stop["file"]
    assert path.name == "stop-answers.md" and report["waiting-for"] is None and report["complete"]
    assert [e["decision"] for e in decisions.entries(repo[0]) if e["class"] == "stop"] == ["pending"]
    original = note_text(repo)
    (repo[0] / NOTE_PATH).write_text(original + "\nAn edit after the stop.\n")   # this run can never continue
    assert [e["decision"] for e in decisions.entries(repo[0]) if e["class"] == "stop"] == ["overtaken"]
    (repo[0] / NOTE_PATH).write_text(original)
    path.write_text(decide(path.read_text(), {"text": {
        "state": "rejected", "reason": "the note needs a rewrite", "resolution": "rewrote the note",
        "refs": ["0123abc", "kb/work/some-workshop"]}}))
    assert main(["approve", report["run-dir"], stop["file"], "--key", stop["key"]], harnesses=repo[1]) == 0
    capsys.readouterr()
    [entry] = [e for e in decisions.entries(repo[0]) if e["class"] == "stop"]
    assert (entry["decision"], entry["resolution"], entry["refs"], entry["proposed-by"]) == (
        "rejected", "rewrote the note", ["0123abc", "kb/work/some-workshop"], "worker")
    assert "refs: 0123abc, kb/work/some-workshop" in decisions.text([entry])
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["stop-answers"]["key"] == stop["key"] and not repeated["unapproved-edits"]


@pytest.mark.slow
def test_full_stops_when_a_review_has_no_result(reviewed, capsys):
    repo = reviewed
    original = start(repo, "NOREVIEW")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--full")
    assert code == 1 and "ended without a result" in report["stopped"] and "critique" in report["stopped"]
    assert not any(line.startswith("assess") for line in launches) and SYNTHESIS not in launches
    assert ROLE not in launches
    assert note_text(repo) == original
    _, again, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and again["stopped"] == report["stopped"]


# --- The revised candidate -------------------------------------------------------------------

CLOSING = "readability-and-flow (all).\n"


def supply(repo, capsys, tmp_path, text, name="revised.md"):
    """Supply `text` as the revised candidate, as a session agent does on the operator's word."""
    path = tmp_path / name
    path.write_text(text)
    return revise(repo, capsys, NOTE_PATH, "--revised", str(path))


def at_publication(repo, capsys, tmp_path):
    original = start(repo)
    _, ready, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    assert ready["waiting-for"]["file"].endswith("/publication-answers.md")
    return original, ready, artifact_file(repo, ready, "final.md").read_text()


def pending_answers(repo, report):
    return yaml.safe_load((repo[0] / report["waiting-for"]["file"]).read_text().split("---\n")[1])


def test_a_revised_candidate_is_refused_unless_the_run_waits_at_publication(repo, capsys, tmp_path):
    original = start(repo)
    code, error, launches = supply(repo, capsys, tmp_path, original + "More.\n")
    assert code == 2 and "not waiting at its publication stop" in error and launches == []
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    assert re.search(r"plain-wording-answers-", waiting["waiting-for"]["file"])
    code, error, launches = supply(repo, capsys, tmp_path, original + "More.\n")
    assert code == 2 and "not waiting at its publication stop" in error and launches == []
    assert not (repo[0] / waiting["run-dir"] / "artifact/revised.md").exists()
    code, error, _ = revise(repo, capsys, NOTE_PATH, "--revised", str(tmp_path / "revised.md"), "--assess")
    assert code == 2 and "--revised takes no workflow option: --assess" in error
    assert note_text(repo) == original


def test_a_revised_candidate_replaces_the_question_and_publishes_only_on_its_approval(repo, capsys, tmp_path):
    original, ready, candidate = at_publication(repo, capsys, tmp_path)
    approve_publication(repo, capsys, ready)              # the earlier candidate was approved
    revised = candidate.replace(CLOSING, "The operator's closing sentence.\n")
    code, report, launches = supply(repo, capsys, tmp_path, revised)
    assert code == 0 and launches == [] and not report["applied"] and note_text(repo) == original
    assert report["proposed"].endswith("/artifact/revised.md")
    files = report["revised-candidate"]
    assert (repo[0] / files["revised"]).read_text() == revised
    assert (repo[0] / files["candidate"]).read_text() == candidate     # the workflow's candidate is kept
    assert "-readability-and-flow (all).\n+The operator's closing sentence.\n" in (
        repo[0] / files["diff-from-candidate"]).read_text()
    assert "+The operator's closing sentence.\n" in (repo[0] / files["diff-from-note"]).read_text()
    asked = pending_answers(repo, report)
    assert asked["question"] == files["revised"] and asked["question-sha256"] == observations.sha(revised.encode())
    assert asked["items"][0]["state"] == "pending"
    assert report["waiting-for"]["key"] != ready["waiting-for"]["key"]
    (tmp_path / "revised.md").write_text("A later edit of the supplied file.\n")   # captured; no effect
    code, withdrawn, launches = revise(repo, capsys, NOTE_PATH)       # the earlier approval is withdrawn
    assert code == 0 and launches == [] and not withdrawn["applied"] and note_text(repo) == original
    assert withdrawn["waiting-for"]["key"] == report["waiting-for"]["key"]
    assert "The candidate was revised" in withdrawn["waiting-for"]["what"]
    # Answers approving the workflow's candidate, valid against final.md, do not authorize the revised one.
    answers_file = repo[0] / report["waiting-for"]["file"]
    over_candidate = answers_file.read_text().replace(files["revised"], files["candidate"]).replace(
        observations.sha(revised.encode()), observations.sha(candidate.encode()))
    answers_file.write_text(decide(over_candidate, {"text": APPROVED}))
    approve(repo, capsys, report)
    code, refused, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and not refused["applied"] and note_text(repo) == original
    assert "not the text to publish" in refused["waiting-for"]["what"]
    answers_file.write_text(answer_files.pending(files["revised"], revised.encode()))
    done = publish(repo, capsys, refused)
    assert note_text(repo) == revised and done["proposed"] == files["revised"]
    assert done["revised-candidate"] == files and done["guard"]["clean"]
    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    [entry] = [e for e in json.loads(capsys.readouterr().out) if e["class"] == "publication"]
    assert entry["revised"] and entry["decision"] == "approved"
    assert main(["decisions", "--note", NOTE_PATH]) == 0
    assert "| approved | revised candidate |" in capsys.readouterr().out


def test_an_edited_revised_file_is_restored_and_not_published(repo, capsys, tmp_path):
    _, _, candidate = at_publication(repo, capsys, tmp_path)
    revised = candidate.replace(CLOSING, "The operator's closing sentence.\n")
    _, report, _ = supply(repo, capsys, tmp_path, revised)
    approve_publication(repo, capsys, report)
    captured = repo[0] / report["revised-candidate"]["revised"]
    captured.write_text(candidate.replace(CLOSING, "An unchecked sentence.\n"))
    code, restored, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and not restored["applied"]
    assert "approval withdrawn" in restored["waiting-for"]["what"] and captured.read_text() == revised
    publish(repo, capsys, restored)
    assert note_text(repo) == revised


@pytest.mark.parametrize("damage, problem", [
    (lambda text: text.replace("\n# Alpha\n", "\n# Beta\n"), "the H1 changed"),
    (lambda text: text.replace("type: types/note.md\n", ""), "frontmatter `type` changed"),
    (lambda text: text.replace("---\n", "", 1), "frontmatter does not parse"),
])
def test_a_revised_candidate_that_fails_a_check_is_refused_and_the_candidate_kept(repo, capsys, tmp_path, damage,
                                                                                 problem):
    original, ready, candidate = at_publication(repo, capsys, tmp_path)
    answers_file = repo[0] / ready["waiting-for"]["file"]
    pending = answers_file.read_text()
    code, error, launches = supply(repo, capsys, tmp_path, damage(candidate))
    assert code == 2 and "the revised candidate is refused" in error and problem in error and launches == []
    assert answers_file.read_text() == pending and not artifact_file(repo, ready, "revised.md").exists()
    code, error, _ = supply(repo, capsys, tmp_path, original)
    assert code == 2 and "is the note's current text" in error
    _, again, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and again["waiting-for"] == ready["waiting-for"] and again["revised-candidate"] is None
    publish(repo, capsys, again)
    assert note_text(repo) == candidate


def test_a_repeat_keeps_the_revised_candidate_and_a_second_replaces_the_first(repo, capsys, tmp_path):
    _, ready, candidate = at_publication(repo, capsys, tmp_path)
    first = candidate.replace(CLOSING, "The first revision.\n")
    _, revised, _ = supply(repo, capsys, tmp_path, first)
    _, kept, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and kept["proposed"] == revised["proposed"] and not kept["applied"]
    assert kept["waiting-for"]["key"] == revised["waiting-for"]["key"]
    assert artifact_file(repo, ready, "revised.md").read_text() == first
    assert artifact_file(repo, ready, "final.md").read_text() == candidate
    approve_publication(repo, capsys, kept)
    second = candidate.replace(CLOSING, "The second revision.\n")
    code, replaced, launches = supply(repo, capsys, tmp_path, second, name="second.md")
    assert code == 0 and launches == [] and replaced["waiting-for"]["key"] not in (
        revised["waiting-for"]["key"], ready["waiting-for"]["key"])
    assert artifact_file(repo, ready, "revised.md").read_text() == second
    assert artifact_file(repo, ready, "final.md").read_text() == candidate
    assert "+The second revision.\n" in artifact_file(repo, ready, "revised-from-final.diff").read_text()
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["waiting-for"]["key"] == replaced["waiting-for"]["key"]
    assert not repeated["applied"] and pending_answers(repo, repeated)["items"][0]["state"] == "pending"
    publish(repo, capsys, repeated)
    assert note_text(repo) == second


def test_a_changed_workflow_candidate_withdraws_the_revised_candidate(repo, capsys, tmp_path):
    _, _, candidate = at_publication(repo, capsys, tmp_path)
    supply(repo, capsys, tmp_path, candidate.replace(CLOSING, "The operator's closing sentence.\n"))
    path = named_plan(tmp_path)
    plan = yaml.safe_load(path.read_text())
    plan["passes"][0]["scope"] = "§1"
    path.write_text(yaml.safe_dump(plan))
    _, fresh, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert launches == [ORDINARY[0]] and "withdrawn" in fresh["revised-candidate"]
    assert fresh["proposed"].endswith("/final.md") and not artifact_file(repo, fresh, "revised.md").exists()
    assert pending_answers(repo, fresh)["question"] == fresh["proposed"]
    publish(repo, capsys, fresh)
    assert note_text(repo).endswith("readability-and-flow (§1).\n")


def test_a_note_changed_since_the_start_blocks_a_revised_candidate(repo, capsys, tmp_path):
    original, _, candidate = at_publication(repo, capsys, tmp_path)
    revised = candidate.replace(CLOSING, "The operator's closing sentence.\n")
    _, report, _ = supply(repo, capsys, tmp_path, revised)
    approve_publication(repo, capsys, report)
    edited = original + "The operator's own sentence.\n"
    (repo[0] / NOTE_PATH).write_text(edited)
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and launches == [] and note_text(repo) == edited     # another text is another run
    code, error, launches = supply(repo, capsys, tmp_path, revised)
    assert code == 2 and "not waiting at its publication stop" in error and launches == []
    run = repo[0] / report["run-dir"]
    profile = Profile(harness="fake", launch_model="big", effort="high")
    with Run(run, repo[0], profile, harnesses=repo[1]) as opened, pytest.raises(edits.Conflict):
        edits.publication(opened, repo[0], NOTE_PATH, original, candidate, inputs={}, command="-", revised=revised)
    assert note_text(repo) == edited


def test_a_run_stopped_at_publication_before_the_feature_accepts_a_revision_without_new_calls(repo, capsys,
                                                                                             tmp_path):
    original = start(repo)
    _, ready, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert launches == ["assess - big", *ORDINARY]
    run = repo[0] / ready["run-dir"]
    calls = [(call["job"], call["key"], len(call["launches"])) for call in recorded_calls(run)]
    kept = {name: artifact_file(repo, ready, name).read_bytes() for name in ("plan.yaml", "final.md", "final.diff")}
    assert not (run / edits.REVISED_RECORD).exists()
    candidate = kept["final.md"].decode()
    revised = candidate.replace("opening-and-title (all).\n", "The operator's opening note.\n")
    code, report, launches = supply(repo, capsys, tmp_path, revised)
    assert code == 0 and launches == []
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["waiting-for"]["key"] == report["waiting-for"]["key"]
    publish(repo, capsys, repeated)
    assert note_text(repo) == revised != original
    assert [(call["job"], call["key"], len(call["launches"])) for call in recorded_calls(run)] == calls
    assert {name: artifact_file(repo, ready, name).read_bytes() for name in kept} == kept


LONG = "padding " * 32


def test_a_candidate_that_adds_a_validation_warning_names_it_and_still_publishes(repo, capsys, tmp_path):
    original = start(repo, "LONGDESC")
    plan = str(named_plan(tmp_path))
    _, ready, launches = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    assert launches == [ORDINARY[0]] and note_text(repo) == original
    [warning] = ready["new-warnings"]
    assert "250" in warning
    assert "validation warnings the note did not have: " + warning in ready["waiting-for"]["what"]
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)     # the same captured texts, the same list
    assert launches == [] and repeated["new-warnings"] == [warning]
    assert repeated["waiting-for"] == ready["waiting-for"]
    done = publish(repo, capsys, repeated)                       # a warning does not block approval
    assert LONG in note_text(repo) and done["new-warnings"] == [warning]


def test_a_warning_the_start_text_already_had_is_not_new(repo, capsys, tmp_path):
    start(repo, "LONGDESC", text=NOTE.format(words="LONGDESC").replace("description: ", "description: " + LONG, 1))
    assert edits.validation(repo[0], NOTE_PATH, note_text(repo)).warns
    _, ready, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    assert launches == [ORDINARY[0]] and ready["waiting-for"]["file"].endswith("/publication-answers.md")
    assert ready["new-warnings"] == [] and "validation warnings" not in ready["waiting-for"]["what"]


def test_a_revised_candidate_that_adds_a_validation_warning_names_it(repo, capsys, tmp_path):
    original, ready, candidate = at_publication(repo, capsys, tmp_path)
    assert ready["new-warnings"] == []
    revised = candidate.replace("description: ", "description: " + LONG, 1)
    code, report, launches = supply(repo, capsys, tmp_path, revised)
    assert code == 0 and launches == [] and note_text(repo) == original
    [warning] = report["new-warnings"]
    assert "validation warnings the note did not have: " + warning in report["waiting-for"]["what"]
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["new-warnings"] == [warning]
    assert repeated["waiting-for"] == report["waiting-for"]
    publish(repo, capsys, repeated)
    assert note_text(repo) == revised
