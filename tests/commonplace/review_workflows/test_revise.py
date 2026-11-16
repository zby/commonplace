"""Revision approval boundaries, exercised through the CLI with a fake worker."""
from __future__ import annotations

import functools
import json
import re
import subprocess
import sys

import pytest
import yaml

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run, recorded_calls
from commonplace.lib import library
from commonplace.lib.review_workflows import decisions, edits, observations
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


@pytest.mark.parametrize("missing", ["mode", "plan"])
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


def test_mode_switch_is_explicit_and_remembered(repo, capsys, tmp_path):
    start(repo)
    path = named_plan(tmp_path)
    _, fixed, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert fixed["mode"] == "fixed-plan" and launches == [ORDINARY[0]]
    _, assessed, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert assessed["mode"] == "assess" and launches == ["assess - big", *ORDINARY[1:]]
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert repeated["mode"] == "assess" and launches == []
    _, fixed_again, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert fixed_again["mode"] == "fixed-plan" and launches == []


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


@pytest.mark.parametrize("pass_name", ["plain-wording", "abstractions"])
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
    (lambda text: text.replace("reason: decorative", "reason: ambiguous"), "item 1: its proposal differs"),
    (lambda text: decide(text, {"beta": {"state": "rejected", "reason": "r", "decided-by": "agent"}}),
     "'operator' was expected"),
    (lambda text: decide(text, {"beta": {"state": "deferred", "reason": "r"}}), "'revisit' is a required property"),
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


def test_publication_refuses_answers_over_another_text_and_a_rejection(repo, capsys, tmp_path):
    original = start(repo)
    _, ready, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    file = repo[0] / ready["waiting-for"]["file"]
    pending = file.read_text()
    file.write_text(decide(pending.replace(observations.sha(artifact_file(repo, ready, "final.md").read_bytes()),
                                           "0" * 64), {"text": APPROVED}))
    approve(repo, capsys, ready)
    code, refused, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and not refused["applied"] and note_text(repo) == original
    assert "do not authorize publication" in refused["waiting-for"]["what"]
    assert "question-sha256" in refused["waiting-for"]["what"]
    assert "item text: its proposal differs" in refused["waiting-for"]["what"]
    file.write_text(decide(pending, {"text": rejected("the closing reads worse")}))
    approve(repo, capsys, refused)
    code, declined, _ = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and not declined["applied"] and note_text(repo) == original
    assert "the operator's answer is `rejected`: the closing reads worse" in declined["waiting-for"]["what"]
    publish(repo, capsys, declined)


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


@pytest.mark.parametrize("kind", ["assess", "pass", "list", "apply"])
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


@pytest.mark.parametrize("damage", ["missing", "wrong-type", "wrong-name"])
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


def test_named_plan_validation_and_no_change(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=())
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 0 and report["complete"] and not report["applied"] and launches == []
    assert note_text(repo) == original
    path.write_text("purpose: p\ndefend: []\npasses: []\n")
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 2 and "`stop` is missing" in error and launches == []
    path = named_plan(tmp_path, passes=("opening-and-title", "readability-and-flow", "polish"))
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 2 and "must run before" in error and "unknown pass `polish`" in error and launches == []
    path.unlink()
    assert revise(repo, capsys, NOTE_PATH, "--plan", str(path))[0] == 2


@pytest.mark.parametrize("defend", [[], ["Alpha body holds."]])
def test_conversation_and_interactive_passes(repo, capsys, tmp_path, defend):
    start(repo)
    path = named_plan(tmp_path, passes=("split-out-a-treatment", "narrow-overclaims"), defend=defend)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 0 and report["passes"][0]["state"] == "skipped"
    assert report["passes"][1]["state"] == ("applied" if defend else "skipped")
    if defend:
        assert launches == ["pass narrow-overclaims big"]
        publish(repo, capsys, report)
    else:
        assert report["complete"] and launches == []


def test_plain_markdown_keeps_h1_and_waits_for_publication(repo, capsys):
    path = "kb/work/draft/notes.md"
    original = start(repo, path=path, text="# Draft\n\nA draft body.\n")
    _, ready, _ = revise(repo, capsys, path, "--assess")
    assert (repo[0] / path).read_text() == original
    publish(repo, capsys, ready, path)
    assert (repo[0] / path).read_text().startswith(original + "readability-and-flow")


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


def test_a_differing_change_is_asked_as_usual(repo, capsys, tmp_path):
    first_decisions(repo, capsys, tmp_path)
    start(repo, "changed")
    (repo[0] / "new-proposal").touch()                       # alpha's change becomes delta
    _, second, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    found = items(repo, second)
    assert found["delta"]["state"] == "pending" and "carried-from" not in found["delta"]
    assert found["beta"]["state"] == "rejected"


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


def test_the_fix_receives_earlier_decisions_and_an_ordinary_pass_does_not(repo, capsys, tmp_path):
    first_decisions(repo, capsys, tmp_path)
    start(repo, "changed")
    finding = stored(repo, "warn")
    code, _, launches = revise(repo, capsys, NOTE_PATH, "--finding", finding)
    assert code == 0 and launches == ["pass fix-strategy-taxonomy big"]
    fix = captured_inputs(repo[2])[-1]
    assert "Operator's reason: a registered word" in fix["inputs"]["earlier-decisions"]
    start(repo, "changed again")
    revise(repo, capsys, NOTE_PATH, "--pass", "readability-and-flow")
    assert "earlier-decisions" not in captured_inputs(repo[2])[-1]["inputs"]


def test_a_note_without_earlier_decisions_passes_none(repo, capsys, tmp_path):
    start(repo)
    revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    [listed] = captured_inputs(repo[2])
    assert "earlier-decisions" not in listed["inputs"]


# --- Focused plans and findings ------------------------------------------------------------

GATE = "kb/instructions/review-gates/prose/residue.md"


def stored(repo, outcome, gate=GATE, depth=2, note=NOTE_PATH):
    """Write a current review result for `note` against `gate`; return its repository path.

    `info` writes a `pass` result that holds one INFO-level finding.
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
                       findings=level if outcome == "info" else findings(outcome), evidence=evidence(root))
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


def test_pass_without_purpose_gets_the_focused_purpose(repo, capsys):
    start(repo)
    _, ready, launches = revise(repo, capsys, NOTE_PATH, "--pass", "opening-and-title")
    assert launches == [ORDINARY[2]] and ready["plan"]["purpose"] == revise_module.FOCUSED_PURPOSE
    code, error, _ = revise(repo, capsys, NOTE_PATH, "--pass", revise_module.FIX)
    assert code == 2 and "fixes one review finding" in error


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


def test_full_reuses_fresh_review_results(reviewed, capsys):
    repo = reviewed
    start(repo)
    assert main(["run", "gates", NOTE_PATH, "--criteria", "prose", "--timeout", "30"], harnesses=repo[1]) == 0
    capsys.readouterr()
    _, report, launches = revise(repo, capsys, NOTE_PATH, "--full")
    assert sorted(repo[2].read_text().splitlines()[:2]) == ["review residue", "review warned"]
    assert set(launches[:5]) == REVIEWS - {"review residue,warned"} and launches[5:7] == [SYNTHESIS, ROLE]
    assert report["reviews"][0]["counts"] == {"fresh": 2, "reviewed": 5}


def test_full_stops_on_a_depth_one_proposal_with_nothing_edited(reviewed, capsys):
    repo = reviewed
    original = start(repo, "STOP")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--full")
    assert code == 0 and report["stop"] == "rewrite-needed" and report["passes"] == []
    assert launches[-1] == "assess - big" and len(launches) == 9
    assert note_text(repo) == original and report["complete"] and not report["applied"]
    _, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and repeated["stop"] == "rewrite-needed"


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
