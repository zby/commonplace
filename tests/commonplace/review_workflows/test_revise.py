"""Revision approval boundaries, exercised through the CLI with a fake worker."""
from __future__ import annotations

import functools
import json
import subprocess
import sys

import pytest
import yaml

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run, recorded_calls
from commonplace.lib import library
from commonplace.lib.review_workflows import revise as revise_module
from tests.commonplace.review_workflows.brief_helpers import add_brief, captured_inputs
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
inputs, outputs = files.get("Inputs", {}), files.get("Required outputs", {})
KINDS = {"Assess one artifact": "assess", "Run one simplification": "pass",
         "List the candidates": "list", "Apply the operator-approved": "apply"}
kind = next(kind for start, kind in KINDS.items() if frame.removeprefix("Task:\n").startswith(start))
found = re.search(r"simplification-passes/([a-z-]+)\.md`", frame)
name = found.group(1) if found and kind != "assess" else "-"
model = sys.argv[sys.argv.index("--model") + 1]
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(f"{kind} {name} {model}\n")
if Path(f"fail-{name}").exists():
    sys.exit(1)
text = inputs["artifact"].read_text()
with open(os.environ["FAKE_LOG"] + ".inputs", "a") as log:
    log.write(json.dumps({"kind": kind, "pass": name,
        "inputs": {key: path.read_text() for key, path in inputs.items()}}) + "\n")
if Path(f"brief-problem-{kind}").exists():
    files["Optional outputs"]["problem"].write_text("The requested pass conflicts with the write brief.")
    sys.exit(0)
if kind == "assess":
    passes = ["readability-and-flow", "place-external-systems", "opening-and-title"]
    if "PLAIN" in text:
        passes.insert(1, "plain-wording")
    if "OVERCLAIM" in text:
        passes.insert(0, "narrow-overclaims")
    if "BADPLAN" in text and "was rejected" not in frame:
        passes.append("make-it-shine")
    plan = "purpose: p\ndefend: []\nstop: null\npasses:\n" + "".join(f"  - pass: {p}\n" for p in passes)
    if "STOP" in text:
        plan = "purpose: p\ndefend: []\npasses: []\nstop: rewrite-needed\n"
    if Path("new-proposal").exists():
        plan = plan.replace("purpose: p", "purpose: new")
    outputs["assessment"].write_text("# Assessment\n\nRanked changes.\n")
    outputs["plan"].write_text(plan)
elif kind == "list":
    listed = "- alpha: figure; replace\n  why: decorative\n- beta: word; replace\n- gamma: keep\n"
    outputs["list"].write_text(listed.replace("alpha", "delta") if Path("new-proposal").exists() else listed)
else:
    if kind == "apply":
        kept = re.findall(r"^- (\w+)", inputs["approved"].read_text(), re.MULTILINE)
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
    outputs["artifact"].write_text(revised)
    outputs["report"].write_text(f"# {name}\n\nDone.\n")
'''
PROFILES = ("default: s\neffort: {simple: s, judgment: j}\nprofiles:\n"
            "  s: {harness: fake, launch-model: small, effort: low}\n"
            "  j: {harness: fake, launch-model: big, effort: high}\n")
NOTE = ("---\ndescription: A note about alpha that is long enough to describe what it is for\n"
        "type: types/note.md\nuser-verified: true\n---\n\n# Alpha\n\nAlpha body {words}.\n")
NOTE_PATH = "kb/notes/alpha.md"
PASSES = REPO_ROOT / "kb/instructions/simplification-passes"
ORDINARY = ["pass readability-and-flow big", "pass place-external-systems small", "pass opening-and-title big"]


@pytest.fixture
def repo(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text() for rel in NOTE_TYPE_SPECS}
    files |= {f"kb/instructions/simplification-passes/{p.name}": p.read_text() for p in PASSES.glob("*.md")}
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


def publish(repo, capsys, report, path=NOTE_PATH):
    assert report["waiting-for"]["file"].endswith("/publication.json")
    approve(repo, capsys, report)
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
    assert call["inputs"]["workflow"] == (repo[0] / "kb" / revise_module.EXECUTION_REL).read_text()
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
    for name in ("assessment.md", "plan.yaml", "final.md", "final.diff", "publication.json"):
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
    approve(repo, capsys, report)
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
def test_strike_selections_still_stop_and_unapproved_edits_are_not_used(repo, capsys, tmp_path, pass_name):
    original = start(repo)
    path = named_plan(tmp_path, passes=(pass_name,))
    _, waiting, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    model = "small" if pass_name == "plain-wording" else "big"
    assert launches == [f"list {pass_name} {model}"]
    assert waiting["waiting-for"]["file"].endswith(".md")
    _, again, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [] and again["waiting-for"] == waiting["waiting-for"]
    listed = repo[0] / waiting["waiting-for"]["file"]
    listed.write_text(listed.read_text().replace("- beta: word; replace\n", ""))
    approve(repo, capsys, waiting)
    listed.write_text("- unauthorized: replace\n")
    _, ready, launches = revise(repo, capsys, NOTE_PATH)
    assert launches == [f"apply {pass_name} {model}"]
    assert ready["unapproved-edits"] and note_text(repo) == original
    assert f"{pass_name} applied alpha gamma." in artifact_file(repo, ready, "final.md").read_text()
    publish(repo, capsys, ready)


def test_changed_selection_invalidates_publication_even_if_candidate_is_identical(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=("plain-wording",))
    _, selection, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    approve(repo, capsys, selection)
    _, ready, _ = revise(repo, capsys, NOTE_PATH)
    candidate = artifact_file(repo, ready, "final.md").read_text()
    approve(repo, capsys, ready)
    listed = repo[0] / selection["waiting-for"]["file"]
    listed.write_text(listed.read_text().replace("why: decorative", "why: ambiguous"))
    approve(repo, capsys, selection)
    code, fresh, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and fresh["waiting-for"] and not fresh["applied"]
    assert launches == ["apply plain-wording small"]
    assert artifact_file(repo, fresh, "final.md").read_text() == candidate
    assert fresh["waiting-for"]["key"] != ready["waiting-for"]["key"]
    assert note_text(repo) == original


def test_striking_every_entry_completes_without_publication(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=("plain-wording",))
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    (repo[0] / waiting["waiting-for"]["file"]).write_text("")
    approve(repo, capsys, waiting)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["complete"] and not done["applied"] and launches == []
    assert note_text(repo) == original


@pytest.mark.parametrize("change", ["criterion", "profile", "retry"])
def test_changed_strike_request_or_retried_proposal_requires_new_selection(repo, capsys, change):
    original = start(repo, "PLAIN")
    _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    approve(repo, capsys, waiting)
    args = []
    if change == "criterion":
        path = repo[0] / "kb/instructions/simplification-passes/plain-wording.md"
        path.write_text(path.read_text() + "\nChanged criterion.\n")
    elif change == "profile":
        args = ["--profile-simple", "j"]
    else:
        calls = recorded_calls(repo[0] / waiting["run-dir"])
        [call] = [c for c in calls if c["job"] == "plain-wording/list" and c["status"] == "delivered"]
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
    approve(repo, capsys, waiting)
    _, ready, _ = revise(repo, capsys, NOTE_PATH)
    calls = captured_inputs(repo[2])
    assert {c["kind"] for c in calls} == {"assess", "pass", "list", "apply"}
    assert all(c["inputs"]["brief"] == brief.read_text() for c in calls)
    assert all("## Headless write briefs" in c["inputs"]["workflow"] for c in calls if c["kind"] != "assess")
    publish(repo, capsys, ready)


@pytest.mark.parametrize("kind", ["assess", "pass", "list", "apply"])
def test_worker_brief_conflict_stops_without_publication(repo, capsys, kind):
    start(repo, "PLAIN")
    add_brief(repo[0], NOTE_PATH)
    original = note_text(repo)
    if kind == "apply":
        _, waiting, _ = revise(repo, capsys, NOTE_PATH, "--assess")
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
    approve(repo, capsys, ready)
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
    approve(repo, capsys, ready)
    edited = note_text(repo) + "The operator's sentence.\n"
    (repo[0] / NOTE_PATH).write_text(edited)
    code, fresh, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 0 and fresh["run-dir"] != ready["run-dir"] and launches == ["assess - big", *ORDINARY]
    assert not fresh["applied"] and note_text(repo) == edited
