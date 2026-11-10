"""`commonplace-review run revise` end to end on a fake harness; no model is called.

The fake worker knows each ask by its task's first line and the pass by the
pass path the task names; it logs `<kind> <pass> <launch model>` per launch
and answers from the table below. Words in the artifact's text choose the
scenario: STOP makes the plan stop, BADPLAN makes the first plan name an
unknown pass, PLAIN adds plain-wording to the plan, OVERCLAIM adds
narrow-overclaims, RETITLE makes the first readability attempt change the H1,
BADPASS makes every readability attempt change it, and TOUCH makes the last
pass edit the artifact's file, as a concurrent operator would. A file `fail-<pass>` in the working directory makes that pass's launches exit 1.
"""

from __future__ import annotations

import functools
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run, recorded_calls
from commonplace.lib import library
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.review_workflows import revise as revise_module
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

FAKE = r"""
import os, re, sys
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
KINDS = {"Assess one artifact": "assess", "Run one simplification": "pass", "List the candidates": "list",
         "Apply the operator-approved": "apply"}
kind = next(kind for start, kind in KINDS.items() if frame.removeprefix("Task:\n").startswith(start))
found = re.search(r"simplification-passes/([a-z-]+)\.md`", frame)
name = found.group(1) if found and kind != "assess" else "-"
model = sys.argv[sys.argv.index("--model") + 1]
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(f"{kind} {name} {model}\n")
if Path(f"fail-{name}").exists():
    sys.exit(1)
text = inputs["artifact"].read_text()
rejected = "was rejected" in frame


def plan():
    if "STOP" in text:
        return "purpose: p\ndefend: []\npasses: []\nstop: 'rewrite-needed: the argument is upside down'\n"
    passes = ["readability-and-flow", "place-external-systems", "opening-and-title"]
    if "PLAIN" in text:
        passes.insert(1, "plain-wording")
    if "OVERCLAIM" in text:
        passes.insert(0, "narrow-overclaims")
    if "BADPLAN" in text and not rejected:
        passes.append("make-it-shine")
    return "purpose: p\ndefend: []\npasses:\n" + "".join(f"  - pass: {p}\n" for p in passes) + "stop: null\n"


def revised():
    if kind == "apply":
        kept = re.findall(r"^- (\w+)", inputs["approved"].read_text(), re.MULTILINE)
        return text + f"{name} applied {' '.join(kept)}.\n"
    if name == "readability-and-flow" and ("RETITLE" in text and not rejected or "BADPASS" in text):
        return text.replace("\n# Alpha\n", "\n# Beta\n")
    if "TOUCH" in text and name == "opening-and-title":
        Path("kb/notes/alpha.md").write_text(text + "The operator's sentence.\n")
    scope = inputs["scope"].read_text() if "scope" in inputs else "all"
    return text.replace("user-verified: true\n", "") + f"{name} ({scope}).\n"


if kind == "assess":
    outputs["assessment"].write_text("# Assessment\n\nRanked changes.\n")
    outputs["plan"].write_text(plan().replace("purpose: p", "purpose: new") if Path("new-proposal").exists()
                               else plan())
elif kind == "list":
    listed = "- alpha: figure; replace\n  why: decorative\n- beta: word; replace\n- gamma: keep\n"
    outputs["list"].write_text(listed.replace("alpha", "delta") if Path("new-proposal").exists() else listed)
else:
    outputs["artifact"].write_text(revised())
    outputs["report"].write_text(f"# {name}\n\nDone.\n")
"""

PROFILES = ("default: s\neffort: {simple: s, judgment: j}\nprofiles:\n"
            "  s: {harness: fake, launch-model: small, effort: low}\n"
            "  j: {harness: fake, launch-model: big, effort: high}\n")
NOTE = ("---\ndescription: A note about alpha that is long enough to describe what it is for\n"
        "type: types/note.md\nuser-verified: true\n---\n\n# Alpha\n\nAlpha body {words}.\n")
NOTE_PATH = "kb/notes/alpha.md"
PASSES = REPO_ROOT / "kb/instructions/simplification-passes"


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text(encoding="utf-8") for rel in NOTE_TYPE_SPECS}
    files |= {f"kb/instructions/simplification-passes/{path.name}": path.read_text(encoding="utf-8")
              for path in PASSES.glob("*.md")}
    files |= {"kb/instructions/review-profiles.yaml": PROFILES, "kb/notes/COLLECTION.md": "# Notes\n"}
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
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


def start(repo, words: str = "", path: str = NOTE_PATH, text: str | None = None) -> str:
    """Write the artifact with the scenario words and commit everything."""
    root = repo[0]
    text = NOTE.format(words=words) if text is None else text
    (root / path).parent.mkdir(parents=True, exist_ok=True)
    (root / path).write_text(text, encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=root, check=True)
    return text


def revise(repo, capsys, *args: str) -> tuple[int, dict | str, list[str]]:
    """Run the command; return the exit code, the report (or stderr on a command error) and this run's launches."""
    _, harnesses, log = repo
    before = log.read_text().splitlines()
    code = main(["run", "revise", *args, "--timeout", "30"], harnesses=harnesses)
    captured = capsys.readouterr()
    return (code, json.loads(captured.out) if code != 2 else captured.err,
            log.read_text().splitlines()[len(before):])


def approve(repo, capsys, report: dict, *, file: str | None = None, key: str | None = None):
    """Explicit operator action, separate from every workflow invocation."""
    stop = report["waiting-for"]
    code = main(["approve", report["run-dir"], file or stop["file"], "--key", key or stop["key"]],
                harnesses=repo[1])
    captured = capsys.readouterr()
    assert code == 0, captured.err
    return json.loads(captured.out)


def assess(repo, capsys, words: str = "", *args: str, approve_plan: bool = True) -> dict:
    start(repo, words)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--purpose", "p", *args)
    assert code == 0, report
    assert launches == ["assess - big"], "the assessment is one judgment ask"
    if approve_plan:
        approve(repo, capsys, report)
    return report


def artifact_file(repo, report: dict, name: str) -> Path:
    return repo[0] / report["run-dir"] / "artifact" / name


def note_text(repo) -> str:
    return (repo[0] / NOTE_PATH).read_text(encoding="utf-8")


def states(report: dict) -> list[tuple[str, str]]:
    return [(state["name"], state["state"]) for state in report["passes"]]


def test_assessment_stops_with_both_files(repo, capsys):
    report = assess(repo, capsys, approve_plan=False)
    assert report["waiting-for"]["what"].startswith("Read assessment.md") and not report["complete"]
    run = report["run-dir"]
    assert run == f"kb/reports/state/review/runs/revise/kb/notes/alpha/{sha256(NOTE.format(words=''))[:12]}"
    assert report["waiting-for"]["file"] == f"{run}/artifact/plan.yaml"
    assert report["waiting-for"]["command"] == f"commonplace-review run revise {NOTE_PATH}"
    assert artifact_file(repo, report, "assessment.md").read_text().startswith("# Assessment")
    plan = yaml.safe_load(artifact_file(repo, report, "plan.yaml").read_text())
    assert [entry["pass"] for entry in plan["passes"]] == ["readability-and-flow", "place-external-systems",
                                                         "opening-and-title"]
    assert report["guard"]["clean"] and note_text(repo) == NOTE.format(words="")


def test_unapproved_repeats_launch_nothing_and_later_edits_do_not_change_the_answer(repo, capsys):
    report = assess(repo, capsys, approve_plan=False)
    path = artifact_file(repo, report, "plan.yaml")
    original = note_text(repo)
    path.write_text("this is not even a valid plan")
    code, waiting, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and waiting["waiting-for"] == report["waiting-for"]
    assert note_text(repo) == original
    plan = {"purpose": "p", "defend": [], "stop": None,
            "passes": [{"pass": "readability-and-flow", "scope": "approved scope"}]}
    path.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, waiting)
    plan["passes"][0]["scope"] = "unapproved scope"
    path.write_text(yaml.safe_dump(plan))
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["applied"] and launches == ["pass readability-and-flow big"]
    assert note_text(repo).endswith("readability-and-flow (approved scope).\n")


@pytest.mark.parametrize("change", ["instruction", "profile"])
def test_changed_assessment_inputs_invalidate_approval_even_when_proposed_text_matches(repo, capsys, change):
    report = assess(repo, capsys)
    args = []
    if change == "instruction":
        instruction = repo[0] / "kb" / revise_module.INSTRUCTION_REL
        instruction.write_text(instruction.read_text() + "\nChanged assessment instruction.\n")
    else:
        args = ["--profile-judgment", "s"]
    code, waiting, launches = revise(repo, capsys, NOTE_PATH, *args)
    assert code == 0 and waiting["waiting-for"] and not waiting["applied"]
    assert launches == [f"assess - {'small' if change == 'profile' else 'big'}"]
    assert waiting["run-dir"] == report["run-dir"]
    assert waiting["waiting-for"]["key"] != report["waiting-for"]["key"]
    old = report["waiting-for"]
    assert main(["approve", report["run-dir"], old["file"], "--key", old["key"]], harnesses=repo[1]) == 2
    assert "proposal changed" in capsys.readouterr().err
    code, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and repeated["waiting-for"] == waiting["waiting-for"]
    approve(repo, capsys, waiting)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["applied"] and not any(line.startswith("assess") for line in launches)


def test_a_repeat_runs_the_passes_in_order_on_their_effort_profiles_and_applies_once(repo, capsys):
    report = assess(repo, capsys)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["complete"] and done["run-dir"] == report["run-dir"], done
    assert launches == ["pass readability-and-flow big", "pass place-external-systems small",
                        "pass opening-and-title big"]
    assert states(done) == [("readability-and-flow", "applied"), ("place-external-systems", "applied"),
                            ("opening-and-title", "applied")]
    assert [state["profile"]["launch-model"] for state in done["passes"]] == ["big", "small", "big"]
    text = note_text(repo)
    assert text.endswith("readability-and-flow (all).\nplace-external-systems (all).\nopening-and-title (all).\n")
    assert "user-verified" not in text and done["guard"]["clean"], "the artifact write is expected"
    assert done["applied"] and (repo[0] / done["proposed"]).read_text() == text
    code, again, launches = revise(repo, capsys, NOTE_PATH)
    assert again["run-dir"] != report["run-dir"] and launches == ["assess - big"], "the revised text is a new run"
    assert note_text(repo) == text


def test_an_edited_plan_is_honoured_and_replays_what_did_not_change(repo, capsys):
    report = assess(repo, capsys)
    plan_file = artifact_file(repo, report, "plan.yaml")
    plan = yaml.safe_load(plan_file.read_text())
    plan["passes"] = [plan["passes"][0], {"pass": "place-external-systems", "scope": "the TL;DR"}]
    plan_file.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, report)
    (repo[0] / "fail-place-external-systems").touch()
    code, _, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 1 and launches == ["pass readability-and-flow big"] + ["pass place-external-systems small"] * 3
    assert note_text(repo) == NOTE.format(words=""), "nothing is written before the end"
    (repo[0] / "fail-place-external-systems").unlink()
    plan["passes"][1]["scope"] = "§2"
    plan_file.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, report)
    code, _, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["pass place-external-systems small"], "the first pass replays"
    assert note_text(repo).endswith("readability-and-flow (all).\nplace-external-systems (§2).\n")


def test_an_invalid_operator_plan_is_a_command_error(repo, capsys):
    report = assess(repo, capsys)
    plan_file = artifact_file(repo, report, "plan.yaml")
    plan_file.write_text("purpose: p\ndefend: []\npasses:\n  - pass: opening-and-title\n"
                         "  - pass: readability-and-flow\n  - pass: polish\n")
    approve(repo, capsys, report)
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and launches == []
    assert "`stop` is missing" in error
    plan_file.write_text("purpose: p\ndefend: []\nstop: null\npasses:\n  - pass: opening-and-title\n"
                         "  - pass: readability-and-flow\n  - pass: polish\n")
    approve(repo, capsys, report)
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and launches == []
    assert "`readability-and-flow` (depth 4) must run before `opening-and-title` (depth 6)" in error
    assert "unknown pass `polish`" in error


def test_a_malformed_assessor_plan_costs_one_attempt(repo, capsys):
    start(repo, "BADPLAN")
    code, report, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["assess - big"] * 2
    assert report["waiting-for"]["file"].endswith("/artifact/plan.yaml")


def test_a_stop_plan_ends_cleanly_with_the_assessment(repo, capsys):
    start(repo, "STOP")
    code, report, _ = revise(repo, capsys, NOTE_PATH, "--purpose", "p")
    assert code == 0 and report["complete"] and report["stop"].startswith("rewrite-needed")
    assert report["waiting-for"] is None and artifact_file(repo, report, "assessment.md").is_file()
    code, again, launches = revise(repo, capsys, NOTE_PATH)
    assert (code, again["stop"], launches) == (0, report["stop"], [])


def test_plain_wording_stops_with_its_list_and_applies_only_unstruck_entries(repo, capsys):
    report = assess(repo, capsys, "PLAIN")
    start_text = note_text(repo)
    code, waiting, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["pass readability-and-flow big", "list plain-wording small"]
    assert "plain-wording list" in waiting["waiting-for"]["what"]
    assert states(waiting)[1:] == [("plain-wording", "waiting"), ("place-external-systems", "pending"),
                                   ("opening-and-title", "pending")]
    assert note_text(repo) == start_text and not waiting["applied"]
    assert waiting["proposed"] in waiting["not-applied"] and "waits for the operator" in waiting["not-applied"]
    listed = repo[0] / waiting["waiting-for"]["file"]
    assert listed.name.startswith("plain-wording-list-")
    listed.write_text(listed.read_text().replace("- beta: word; replace\n", ""))
    approve(repo, capsys, waiting)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["complete"] and done["run-dir"] == report["run-dir"], done
    assert launches == ["apply plain-wording small", "pass place-external-systems small",
                        "pass opening-and-title big"], "the list replays"
    assert "plain-wording applied alpha gamma.\n" in note_text(repo)


@pytest.mark.parametrize("change", ["criterion", "profile"])
def test_changed_strike_inputs_require_new_approval_and_unapproved_repeat_launches_nothing(repo, capsys, change):
    assess(repo, capsys, "PLAIN")
    code, waiting, _ = revise(repo, capsys, NOTE_PATH)
    assert code == 0
    code, repeated, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == [] and repeated["waiting-for"] == waiting["waiting-for"]
    approve(repo, capsys, waiting)
    args = []
    if change == "criterion":
        path = repo[0] / "kb/instructions/simplification-passes/plain-wording.md"
        path.write_text(path.read_text() + "\nChanged pass instruction.\n")
    else:
        args = ["--profile-simple", "j"]
    code, fresh, launches = revise(repo, capsys, NOTE_PATH, *args)
    assert code == 0 and not fresh["applied"] and fresh["waiting-for"]
    assert launches == [f"list plain-wording {'big' if change == 'profile' else 'small'}"]
    assert fresh["waiting-for"]["key"] != waiting["waiting-for"]["key"]
    assert note_text(repo) == NOTE.format(words="PLAIN")


@pytest.mark.parametrize("job", ["assessment", "plain-wording/list"])
def test_a_retried_call_with_a_new_proposal_cannot_reuse_approval(repo, capsys, job):
    waiting = assess(repo, capsys, "PLAIN")
    if job != "assessment":
        _, waiting, _ = revise(repo, capsys, NOTE_PATH)
        approve(repo, capsys, waiting)
    calls = recorded_calls(repo[0] / waiting["run-dir"])
    [call] = [call for call in calls if call["job"] == job and call["status"] == "delivered"]
    (repo[0] / "new-proposal").touch()
    assert main(["retry", waiting["run-dir"], job, "--key", call["key"]], harnesses=repo[1]) == 0
    capsys.readouterr()
    code, fresh, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and not fresh["applied"] and fresh["waiting-for"]
    assert launches == (["assess - big"] if job == "assessment" else ["list plain-wording small"])
    assert fresh["waiting-for"]["key"] != waiting["waiting-for"]["key"]
    assert note_text(repo) == NOTE.format(words="PLAIN")


def test_narrow_overclaims_runs_only_with_a_defend_list(repo, capsys):
    assess(repo, capsys, "OVERCLAIM")
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and "pass narrow-overclaims big" not in launches
    assert done["passes"][0]["state"] == "skipped" and "interactive path" in done["passes"][0]["reason"]
    assert states(done)[1:] == [(name, "applied") for name in
                                ("readability-and-flow", "place-external-systems", "opening-and-title")]
    assert done["applied"], "a skipped pass does not hold the text back"
    second = assess(repo, capsys, "OVERCLAIM again")
    plan_file = artifact_file(repo, second, "plan.yaml")
    plan = yaml.safe_load(plan_file.read_text())
    plan["defend"] = ["Alpha body holds."]
    plan_file.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, second)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches[0] == "pass narrow-overclaims big"
    assert done["passes"][0]["state"] == "applied"


def test_an_edited_note_opens_a_new_run(repo, capsys):
    report = assess(repo, capsys, "PLAIN")
    revise(repo, capsys, NOTE_PATH)                                           # stops for the strikes
    edited = note_text(repo) + "The operator's sentence.\n"
    (repo[0] / NOTE_PATH).write_text(edited, encoding="utf-8")
    code, fresh, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and fresh["run-dir"] != report["run-dir"] and launches == ["assess - big"]
    assert note_text(repo) == edited


def test_an_operator_edit_during_the_run_is_a_conflict(repo, capsys):
    assess(repo, capsys, "TOUCH")
    code, report, _ = revise(repo, capsys, NOTE_PATH)
    assert code == 1 and "changed during the run" in report["conflict"] and report["proposed"] in report["conflict"]
    assert note_text(repo).endswith("The operator's sentence.\n") and not report["applied"]
    assert report["guard"]["changed"] == [NOTE_PATH]


def test_a_problem_pass_applies_nothing(repo, capsys):
    report = assess(repo, capsys, "BADPASS")
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches.count("pass readability-and-flow big") == 2, "the third attempt replays"
    assert states(done) == [("readability-and-flow", "problem"), ("place-external-systems", "applied"),
                            ("opening-and-title", "applied")]
    assert note_text(repo) == NOTE.format(words="BADPASS") and not done["applied"]
    assert done["not-applied"] == (f"The proposed text is {report['run-dir']}/artifact/texts/opening-and-title.md; "
                                   "it is not applied: readability-and-flow ended with a problem.")


def test_a_repeat_after_a_launch_failure_does_not_ask_again(repo, capsys):
    report = assess(repo, capsys)
    (repo[0] / "fail-place-external-systems").touch()
    code, stopped, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 1 and "place-external-systems" in stopped["stopped"]
    assert launches == ["pass readability-and-flow big"] + ["pass place-external-systems small"] * 3
    (repo[0] / "fail-place-external-systems").unlink()
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["run-dir"] == report["run-dir"]
    assert launches == ["pass place-external-systems small", "pass opening-and-title big"]
    assert note_text(repo).count("readability-and-flow (all).") == 1


def test_a_pass_output_that_breaks_a_bound_costs_one_attempt(repo, capsys):
    report = assess(repo, capsys, "RETITLE")
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches.count("pass readability-and-flow big") == 2
    assert done["passes"][0]["state"] == "applied"
    events = [json.loads(line) for line in (repo[0] / report["run-dir"] / "log.jsonl").read_text().splitlines()]
    [rejected] = [event for event in events if event["event"] == "rejected"]
    assert "the H1 changed; keep `# Alpha`" in rejected["problems"]
    assert "\n# Alpha\n" in note_text(repo)


def test_an_artifact_without_frontmatter_keeps_its_h1(repo, capsys):
    path = "kb/work/draft/notes.md"
    start(repo, text="# Draft\n\nA draft body.\n", path=path)
    code, report, _ = revise(repo, capsys, path, "--purpose", "p")
    assert code == 0, report
    approve(repo, capsys, report)
    code, done, _ = revise(repo, capsys, path)
    assert code == 0 and done["complete"], done
    assert (repo[0] / path).read_text().startswith("# Draft\n\nA draft body.\nreadability-and-flow (all).\n")


def test_a_named_plan_is_the_runs_plan_on_a_repeat(repo, capsys, tmp_path):
    start(repo, "PLAIN")
    named = tmp_path / "custom.yaml"
    named.write_text("purpose: p\ndefend: []\nstop: null\npasses:\n  - pass: readability-and-flow\n"
                     "  - pass: plain-wording\n", encoding="utf-8")
    code, waiting, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named))
    assert code == 0 and waiting["waiting-for"], waiting
    assert launches == [], "a named plan proposes without assessment; it does not approve"
    approve(repo, capsys, waiting)
    code, waiting, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["pass readability-and-flow big", "list plain-wording small"]
    approve(repo, capsys, waiting)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["applied"] and done["run-dir"] == waiting["run-dir"], done
    assert launches == ["apply plain-wording small"]
    code, _, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(tmp_path / "none.yaml"))
    assert code == 2 and launches == []


def test_a_repeat_reuses_recorded_options_and_replaces_given_ones(repo, capsys):
    report = assess(repo, capsys)
    options = json.loads((repo[0] / report["run-dir"] / "sweep.json").read_text())
    assert (options["purpose"], options["profiles"]["judgment"]["launch_model"]) == ("p", "big")
    code, waiting, launches = revise(repo, capsys, NOTE_PATH, "--profile-judgment", "s")
    assert code == 0 and launches == ["assess - small"] and waiting["waiting-for"]
    approve(repo, capsys, waiting)
    code, _, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches[0] == "pass readability-and-flow small"
    options = json.loads((repo[0] / report["run-dir"] / "sweep.json").read_text())
    assert (options["purpose"], options["profiles"]["judgment"]["launch_model"]) == ("p", "small")


def test_the_plan_and_the_strikes_are_answers_and_an_edited_plan_replays_what_did_not_change(repo, capsys):
    report = assess(repo, capsys, "PLAIN")
    start_text = note_text(repo)
    plan_file = artifact_file(repo, report, "plan.yaml")
    plan = yaml.safe_load(plan_file.read_text())
    plan["passes"][0]["scope"] = "§1"
    plan_file.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, report)
    code, waiting, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["pass readability-and-flow big", "list plain-wording small"]
    first_list = waiting["waiting-for"]["file"]

    # Approve the unchanged list and the edited plan; the passes before replay.
    approve(repo, capsys, waiting)
    plan["passes"] = plan["passes"][:2] + [{"pass": "opening-and-title", "scope": "the TL;DR"}]
    plan_file.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, report)
    (repo[0] / "fail-opening-and-title").touch()
    code, _, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 1 and launches == ["apply plain-wording small"] + ["pass opening-and-title big"] * 3
    (repo[0] / "fail-opening-and-title").unlink()

    # Edit the first pass: it and the list are asked again, and the new list waits for its own strikes.
    plan["passes"][0]["scope"] = "§2"
    plan_file.write_text(yaml.safe_dump(plan))
    approve(repo, capsys, report)
    code, waiting, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["pass readability-and-flow big", "list plain-wording small"]
    assert waiting["waiting-for"]["file"] != first_list and note_text(repo) == start_text
    approve(repo, capsys, waiting)
    code, done, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and done["applied"] and done["conflict"] is None, done
    assert launches == ["apply plain-wording small", "pass opening-and-title big"]
    assert note_text(repo).endswith("readability-and-flow (§2).\nplain-wording applied alpha beta gamma.\n"
                                    "opening-and-title (the TL;DR).\n")
