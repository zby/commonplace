"""`commonplace-review run revise` end to end on a fake harness; no model is called.

The fake worker knows each ask by its task's first line and the pass by the
pass path the task names; it logs `<kind> <pass> <launch model>` per launch
and answers from the table below. Words in the artifact's text choose the
scenario: STOP makes the plan stop, BADPLAN makes the first plan name an
unknown pass, PLAIN adds plain-wording to the plan, OVERCLAIM adds
narrow-overclaims, RETITLE makes the first readability attempt change the H1.
A file `fail-<pass>` in the working directory makes that pass's launches exit 1.
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
from commonplace.headless.jobs import Run
from commonplace.lib import library
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
    if "RETITLE" in text and name == "readability-and-flow" and not rejected:
        return text.replace("\n# Alpha\n", "\n# Beta\n")
    scope = inputs["scope"].read_text() if "scope" in inputs else "all"
    return text.replace("user-verified: true\n", "") + f"{name} ({scope}).\n"


if kind == "assess":
    outputs["assessment"].write_text("# Assessment\n\nRanked changes.\n")
    outputs["plan"].write_text(plan())
elif kind == "list":
    outputs["list"].write_text("- alpha: figure; replace\n  why: decorative\n- beta: word; replace\n- gamma: keep\n")
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


def assess(repo, capsys, words: str = "", *args: str) -> dict:
    start(repo, words)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--purpose", "p", *args)
    assert code == 0, report
    assert launches == ["assess - big"], "the assessment is one judgment ask"
    return report


def artifact_file(repo, report: dict, name: str) -> Path:
    return repo[0] / report["run-dir"] / "artifact" / name


def note_text(repo) -> str:
    return (repo[0] / NOTE_PATH).read_text(encoding="utf-8")


def states(report: dict) -> list[tuple[str, str]]:
    return [(state["name"], state["state"]) for state in report["passes"]]


def test_assessment_stops_with_both_files(repo, capsys):
    report = assess(repo, capsys)
    assert report["waiting-for"]["what"] == "plan" and not report["complete"]
    run = report["run-dir"]
    assert report["waiting-for"]["files"] == [f"{run}/artifact/assessment.md", f"{run}/artifact/plan.yaml"]
    assert f"--resume {run}" in report["waiting-for"]["next"]
    assert artifact_file(repo, report, "assessment.md").read_text().startswith("# Assessment")
    plan = yaml.safe_load(artifact_file(repo, report, "plan.yaml").read_text())
    assert [entry["pass"] for entry in plan["passes"]] == ["readability-and-flow", "place-external-systems",
                                                         "opening-and-title"]
    assert report["guard"]["clean"] and note_text(repo) == NOTE.format(words="")


def test_an_unedited_resume_runs_the_passes_in_order_on_their_effort_profiles(repo, capsys):
    report = assess(repo, capsys)
    code, resumed, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and resumed["complete"], resumed
    assert launches == ["pass readability-and-flow big", "pass place-external-systems small",
                        "pass opening-and-title big"]
    assert states(resumed) == [("readability-and-flow", "applied"), ("place-external-systems", "applied"),
                               ("opening-and-title", "applied")]
    assert [state["profile"]["launch_model"] for state in resumed["passes"]] == ["big", "small", "big"]
    text = note_text(repo)
    assert text.endswith("readability-and-flow (all).\nplace-external-systems (all).\nopening-and-title (all).\n")
    assert "user-verified" not in text and resumed["guard"]["clean"], "the artifact write is expected"
    writes = json.loads(artifact_file(repo, report, "writes.json").read_text())
    assert [entry["to"] for entry in writes] == resumed["written"]
    code, again, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert (code, launches, again["written"], note_text(repo)) == (0, [], resumed["written"], text)


def test_an_edited_plan_is_honoured_and_replays_what_did_not_change(repo, capsys):
    report = assess(repo, capsys)
    revise(repo, capsys, "--resume", report["run-dir"])
    # Re-plan in a new run from the start text: drop one pass and scope another.
    (repo[0] / NOTE_PATH).write_text(NOTE.format(words=""), encoding="utf-8")
    plan_file = artifact_file(repo, report, "plan.yaml")
    plan = yaml.safe_load(plan_file.read_text())
    plan["passes"] = [plan["passes"][0], {"pass": "opening-and-title", "scope": "the TL;DR"}]
    plan_file.write_text(yaml.safe_dump(plan))
    code, fresh, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(plan_file))
    assert code == 0 and fresh["run-dir"] != report["run-dir"]
    assert launches == ["pass readability-and-flow big", "pass opening-and-title big"], "no assessment"
    assert note_text(repo).endswith("readability-and-flow (all).\nopening-and-title (the TL;DR).\n")
    # In the run itself: an edit made before any pass ran is honoured; unchanged passes replay.
    second = assess(repo, capsys)
    plan_file = artifact_file(repo, second, "plan.yaml")
    plan = yaml.safe_load(plan_file.read_text())
    plan["passes"] = [plan["passes"][0], plan["passes"][1]]
    plan_file.write_text(yaml.safe_dump(plan))
    code, resumed, launches = revise(repo, capsys, "--resume", second["run-dir"])
    assert code == 0 and states(resumed) == [("readability-and-flow", "applied"), ("place-external-systems", "applied")]
    plan["passes"][1]["scope"] = "§2"
    plan_file.write_text(yaml.safe_dump(plan))
    code, rescoped, launches = revise(repo, capsys, "--resume", second["run-dir"])
    assert launches == ["pass place-external-systems small"], "the first pass replays"
    assert code == 1 and "re-plan in a new run" in rescoped["conflict"], "its write stands in the artifact"


def test_an_invalid_operator_plan_is_a_command_error(repo, capsys):
    report = assess(repo, capsys)
    plan_file = artifact_file(repo, report, "plan.yaml")
    plan_file.write_text("purpose: p\ndefend: []\npasses:\n  - pass: opening-and-title\n"
                         "  - pass: readability-and-flow\n  - pass: polish\n")
    code, error, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 2 and launches == []
    assert "`stop` is missing" in error
    plan_file.write_text("purpose: p\ndefend: []\nstop: null\npasses:\n  - pass: opening-and-title\n"
                         "  - pass: readability-and-flow\n  - pass: polish\n")
    code, error, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 2 and launches == []
    assert "`readability-and-flow` (depth 4) must run before `opening-and-title` (depth 6)" in error
    assert "unknown pass `polish`" in error


def test_a_malformed_assessor_plan_costs_one_attempt(repo, capsys):
    start(repo, "BADPLAN")
    code, report, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 0 and launches == ["assess - big"] * 2
    assert report["waiting-for"]["what"] == "plan"


def test_a_stop_plan_ends_cleanly_with_the_assessment(repo, capsys):
    start(repo, "STOP")
    code, report, _ = revise(repo, capsys, NOTE_PATH, "--purpose", "p")
    assert code == 0 and report["complete"] and report["stop"].startswith("rewrite-needed")
    assert report["waiting-for"] is None and artifact_file(repo, report, "assessment.md").is_file()
    code, again, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert (code, again["stop"], launches) == (0, report["stop"], [])


def test_plain_wording_stops_with_its_list_and_applies_only_unstruck_entries(repo, capsys):
    report = assess(repo, capsys, "PLAIN")
    code, waiting, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and launches == ["pass readability-and-flow big", "list plain-wording small"]
    assert waiting["waiting-for"]["what"] == "strikes" and "Delete each entry" in waiting["waiting-for"]["next"]
    assert states(waiting)[1:] == [("plain-wording", "waiting"), ("place-external-systems", "pending"),
                                   ("opening-and-title", "pending")]
    listed = repo[0] / waiting["waiting-for"]["files"][0]
    assert listed.name == "plain-wording-list.md"
    listed.write_text(listed.read_text().replace("- beta: word; replace\n", ""))
    code, done, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and done["complete"], done
    assert launches == ["apply plain-wording small", "pass place-external-systems small",
                        "pass opening-and-title big"], "the list replays"
    assert "plain-wording applied alpha gamma.\n" in note_text(repo)


def test_narrow_overclaims_runs_only_with_a_defend_list(repo, capsys):
    report = assess(repo, capsys, "OVERCLAIM")
    code, resumed, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and "pass narrow-overclaims big" not in launches
    assert resumed["passes"][0]["state"] == "skipped" and "interactive path" in resumed["passes"][0]["reason"]
    assert states(resumed)[1:] == [(name, "applied") for name in
                                   ("readability-and-flow", "place-external-systems", "opening-and-title")]
    second = assess(repo, capsys, "OVERCLAIM")
    plan_file = artifact_file(repo, second, "plan.yaml")
    plan = yaml.safe_load(plan_file.read_text())
    plan["defend"] = ["Alpha body holds."]
    plan_file.write_text(yaml.safe_dump(plan))
    code, resumed, launches = revise(repo, capsys, "--resume", second["run-dir"])
    assert code == 0 and launches[0] == "pass narrow-overclaims big"
    assert resumed["passes"][0]["state"] == "applied"


def test_an_operator_edit_between_passes_is_a_conflict(repo, capsys):
    report = assess(repo, capsys, "PLAIN")
    revise(repo, capsys, "--resume", report["run-dir"])                      # stops for the strikes
    edited = note_text(repo) + "The operator's sentence.\n"
    (repo[0] / NOTE_PATH).write_text(edited, encoding="utf-8")
    code, conflict, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 1 and "changed during the pass" in conflict["conflict"]
    assert launches == ["apply plain-wording small"] and conflict["passes"][1]["state"] == "pending"
    assert note_text(repo) == edited, "the operator's text stays"


def test_resume_after_an_interrupted_pass_does_not_reapply(repo, capsys):
    report = assess(repo, capsys)
    (repo[0] / "fail-place-external-systems").touch()
    code, stopped, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 1 and "place-external-systems" in stopped["stopped"]
    assert launches == ["pass readability-and-flow big"] + ["pass place-external-systems small"] * 3
    written = note_text(repo)
    (repo[0] / "fail-place-external-systems").unlink()
    code, resumed, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and launches == ["pass place-external-systems small", "pass opening-and-title big"]
    assert resumed["written"][0] == stopped["written"][0]
    assert note_text(repo).count("readability-and-flow (all).") == 1 and note_text(repo).startswith(written[:40])
    assert len(json.loads(artifact_file(repo, report, "writes.json").read_text())) == 3


def test_a_pass_output_that_breaks_a_bound_costs_one_attempt(repo, capsys):
    report = assess(repo, capsys, "RETITLE")
    code, resumed, launches = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and launches.count("pass readability-and-flow big") == 2
    assert resumed["passes"][0]["state"] == "applied"
    events = [json.loads(line) for line in (repo[0] / report["run-dir"] / "log.jsonl").read_text().splitlines()]
    [rejected] = [event for event in events if event["event"] == "rejected"]
    assert "the H1 changed; keep `# Alpha`" in rejected["problems"]
    assert "\n# Alpha\n" in note_text(repo)


def test_an_artifact_without_frontmatter_keeps_its_h1(repo, capsys):
    path = "kb/work/draft/notes.md"
    start(repo, text="# Draft\n\nA draft body.\n", path=path)
    code, report, _ = revise(repo, capsys, path, "--purpose", "p")
    assert code == 0, report
    code, done, _ = revise(repo, capsys, "--resume", report["run-dir"])
    assert code == 0 and done["complete"], done
    assert (repo[0] / path).read_text().startswith("# Draft\n\nA draft body.\nreadability-and-flow (all).\n")
