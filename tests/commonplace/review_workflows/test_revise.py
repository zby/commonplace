"""Revise runs end at their first stop; later commands act on what they left, through the CLI with a fake worker."""
from __future__ import annotations

import dataclasses
import functools
import hashlib
import json
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run
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
    plan = "purpose: p\nmust-keep: []\nstop: null\npasses:\n" + "".join(f"  - pass: {p}\n" for p in passes)
    listed = re.findall(r"^- `([^`]+)` \(criterion `[^`]+`, depth", frame, re.MULTILINE)
    if "FIXIT" in text and listed:
        plan = plan.replace("passes:\n", f"passes:\n  - pass: fix-strategy-taxonomy\n    finding: {listed[0]}\n")
    if "STOP" in text:
        plan = "purpose: p\nmust-keep: []\npasses: []\nstop: rewrite-needed\n"
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

RUN_DIR = re.compile(r"kb/reports/state/review/runs/v2/revise/kb/notes/alpha/[0-9]{8}T[0-9]{6}Z(?:-[0-9]+)?")


def revise(repo, capsys, *args):
    before = repo[2].read_text().splitlines()
    code = main(["run", "revise", *args, "--timeout", "30"], harnesses=repo[1])
    captured = capsys.readouterr()
    return code, json.loads(captured.out) if code != 2 else captured.err, repo[2].read_text().splitlines()[len(before):]


def artifact_file(repo, report, name):
    return repo[0] / report["run-dir"] / "artifact" / name


def note_text(repo):
    return (repo[0] / NOTE_PATH).read_text()


def named_plan(tmp_path, passes=("readability-and-flow",), **fields):
    path = tmp_path / "custom.yaml"
    path.write_text(yaml.safe_dump({"purpose": "p", "must-keep": [], "stop": None,
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


def waiting(report):
    """The pending answers file over the proposals the run ended at."""
    [state] = [s for s in report["passes"] if s["state"] == "waiting"]
    return state["answers"]


def answer(repo, report, decisions, default=APPROVED, file=None):
    """Decide the items of the answers file the run ended at, or of `file`; return its path."""
    file = file or waiting(report)
    path = repo[0] / file
    path.write_text(decide(path.read_text(), decisions, default))
    return file


def apply_answers(repo, capsys, *files, extra=()):
    """Name decided answers files to a new run: naming them is the operator's approval."""
    return revise(repo, capsys, NOTE_PATH, *[part for file in files for part in ("--answers", file)], *extra)


def record_answers(repo, capsys, file):
    """Keep an answers file that nothing consumes as the operator's decisions."""
    code = main(["answers", "record", file])
    captured = capsys.readouterr()
    assert code == 0, captured.err
    return json.loads(captured.out)


def publish(repo, capsys, report, *args):
    """Publish the candidate the run held, on the operator's word; return the exit code and report or error."""
    code = main(["publish", report["run-dir"], *args], harnesses=repo[1])
    captured = capsys.readouterr()
    return code, json.loads(captured.out) if code == 0 else captured.err


def continued(repo, capsys, item):
    """Run the `run revise` command a continuation item names, as an agent does."""
    words = shlex.split(item["how"]["command"])
    assert words[:4] == ["commonplace-review", "run", "revise", NOTE_PATH], words
    return revise(repo, capsys, *words[3:])


def items_of(report):
    """The continuation items of a report as (kind, actor, after) rows."""
    return [(item["kind"], item["actor"], item["after"]) for item in report["continuation"]["items"]]


def run_dirs(repo):
    base = repo[0] / "kb/reports/state/review/runs/v2/revise" / NOTE_PATH.removesuffix(".md")
    return sorted(path.name for path in base.iterdir()) if base.is_dir() else []


def git_status(repo):
    return subprocess.run(["git", "status", "--porcelain"], cwd=repo[0], check=True, capture_output=True,
                          text=True).stdout


def committed(repo):
    return subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=repo[0], check=True, capture_output=True,
                          text=True).stdout.strip()


HELD_WORDS = "LONGDESC"
"""Note words that make readability-and-flow add a validation warning, so its candidate is held."""


def test_new_run_requires_explicit_mode_and_fixed_plan_rejects_ignored_constraints(repo, capsys, tmp_path):
    original = start(repo)
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and "choose --plan FILE" in error and launches == []
    path = named_plan(tmp_path)
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path), "--must-keep", "Keep alpha")
    assert code == 2 and "takes purpose and must-keep from the plan" in error and launches == []
    assert note_text(repo) == original


def test_fixed_single_pass_has_no_planner_dependency_and_publishes_without_a_stop(repo, capsys, tmp_path,
                                                                                  monkeypatch):
    original = start(repo)
    commits = committed(repo)
    path = named_plan(tmp_path, purpose="Improve the body for its reader", **{"must-keep": ["Alpha body holds."]})
    plan = yaml.safe_load(path.read_text())
    plan["passes"][0]["scope"] = "body only"
    path.write_text(yaml.safe_dump(plan))

    def forbidden(*args, **kwargs):
        pytest.fail("fixed-plan execution constructed an assessment request")

    monkeypatch.setattr(revise_module, "_assessment_request", forbidden)
    code, done, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 0 and done["mode"] == "fixed-plan" and launches == [ORDINARY[0]]
    assert done["complete"] and done["published"] and done["continuation"] is None and done["guard"]["clean"]
    assert RUN_DIR.fullmatch(done["run-dir"]), "a run directory is a UTC stamp under the note's path"
    started = json.loads((repo[0] / done["run-dir"] / edits.START_RECORD).read_text())
    assert started == {"note": NOTE_PATH, "sha256": observations.sha(original.encode()), "brief-sha256": None}
    assert not artifact_file(repo, done, "assessment.md").exists()
    assert not artifact_file(repo, done, "final.md").exists(), "nothing is held"
    assert not (repo[0] / done["run-dir"] / revise_module.CONTINUATION).exists()
    [publication] = done["publications"]
    assert publication["entries"] == ["readability-and-flow"] and publication["number"] == 1
    assert publication["decided-by"] == "automatic"
    assert note_text(repo) == (repo[0] / publication["text"]).read_text() != original
    assert note_text(repo).endswith("readability-and-flow (body only).\n")
    assert publication["sha256"] == observations.sha(note_text(repo).encode())
    assert publication["before-sha256"] == observations.sha(original.encode())
    assert "+readability-and-flow (body only).\n" in (repo[0] / publication["diff"]).read_text()
    assert committed(repo) == commits and f" M {NOTE_PATH}" in git_status(repo), "a write to the working tree only"
    [call] = captured_inputs(repo[2])
    assert call["inputs"]["purpose"] == "Improve the body for its reader"
    assert call["inputs"]["scope"] == "body only"
    assert call["inputs"]["must-keep"] == "- Alpha body holds.\n"
    assert call["inputs"]["execution"] == (repo[0] / "kb" / revise_module.EXECUTION_REL).read_text()
    assert "passes" not in call["inputs"]
    # The run ended; a bare command never resumes it or turns into planning.
    code, error, launches = revise(repo, capsys, NOTE_PATH)
    assert code == 2 and "choose --plan FILE" in error and launches == []


def test_an_unchanged_candidate_publishes_nothing(repo, capsys, tmp_path):
    original = start(repo)
    (repo[0] / "no-candidates").touch()
    code, done, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    assert code == 0 and launches == ["list plain-wording small"] and done["complete"]
    assert not done["published"] and done["publications"] == [] and note_text(repo) == original
    assert not (repo[0] / done["run-dir"] / edits.PUBLISHED).exists()


THREE = ("readability-and-flow", "plain-wording", "place-external-systems")
"""A plan whose entries are applied without a decision, decided per item, and applied without a decision."""


def test_a_run_publishes_and_ends_at_a_per_item_pass_and_later_runs_continue_it(repo, capsys, tmp_path):
    original = start(repo)
    code, ended, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=THREE)))
    assert code == 0 and launches == [ORDINARY[0], "list plain-wording small"] and not ended["complete"]
    assert [s["state"] for s in ended["passes"]] == ["applied", "waiting", "pending"]
    file = waiting(ended)
    assert file == f"{ended['run-dir']}/artifact/plain-wording-answers.md"
    [first] = ended["publications"]
    assert first["entries"] == ["readability-and-flow"] and note_text(repo) == (repo[0] / first["text"]).read_text()
    published = note_text(repo)
    assert published != original and published.endswith("readability-and-flow (all).\n")

    record = ended["continuation"]
    assert record == {"file": f"{ended['run-dir']}/{revise_module.CONTINUATION}",
                      **json.loads((repo[0] / ended["run-dir"] / revise_module.CONTINUATION).read_text())}
    assert record["made-for"] == {"note": NOTE_PATH, "sha256": first["sha256"], "text": first["text"]}
    proposals, entry = record["items"]
    assert items_of(ended) == [("proposals", "operator", []), ("direct-entry", "worker", ["1"])]
    assert proposals["answers"] == [file] and proposals["how"]["step"] == "Proposals awaiting decision"
    assert proposals["how"]["command"] == f"commonplace-review run revise {NOTE_PATH} --answers {file} --purpose p"
    assert proposals["how"]["record"] == f"commonplace-review answers record {file}"
    assert file in proposals["evidence"] and any(e.endswith("/result.md") for e in proposals["evidence"])
    assert entry["effort"] == "simple" and entry["how"]["command"].endswith("--pass place-external-systems --purpose p")
    [stop] = [e for e in decisions.entries(repo[0]) if e["class"] == "plain-wording"]
    assert (stop["decision"], stop["item"]) == ("pending", file)

    answer(repo, ended, {"beta": rejected("a registered word")})
    code, done, launches = apply_answers(repo, capsys, file, extra=("--purpose", "p"))
    assert code == 0 and launches == ["apply plain-wording small"] and done["mode"] == "answers"
    assert done["run-dir"] != ended["run-dir"] and done["complete"] and done["published"]
    assert done["answers"] == [file] and done["continuation"] is None and done["guard"]["clean"]
    [second] = done["publications"]
    assert second["entries"] == ["plain-wording"] and second["before-sha256"] == first["sha256"]
    assert note_text(repo).endswith("readability-and-flow (all).\nplain-wording applied alpha gamma.\n")
    [kept] = decisions.kept_answers(repo[0], repo[0] / done["run-dir"])
    assert kept[1]["origin"] == file and kept[1]["text"] == (repo[0] / file).read_text()
    assert not artifact_file(repo, done, "final.md").exists(), "approved items need no second approval"
    assert not [e for e in decisions.entries(repo[0]) if e["decision"] == "pending"]

    # The proposals were made for the text before the second publication: their answers are stale now.
    code, error, launches = apply_answers(repo, capsys, file)
    assert code == 2 and "no longer holds the text the proposals" in error and launches == []
    code, last, launches = continued(repo, capsys, entry)
    assert code == 0 and launches == [ORDINARY[1]] and last["published"] and last["complete"]
    assert note_text(repo).endswith("plain-wording applied alpha gamma.\nplace-external-systems (all).\n")


def test_an_edit_after_the_proposals_overtakes_their_answers(repo, capsys, tmp_path):
    start(repo)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=THREE)))
    edited = note_text(repo) + "The operator's sentence.\n"
    (repo[0] / NOTE_PATH).write_text(edited)
    [stop] = [e for e in decisions.entries(repo[0]) if e["class"] == "plain-wording"]
    assert stop["decision"] == "overtaken"
    file = answer(repo, ended, {"beta": rejected("a registered word")})
    before = run_dirs(repo)
    code, error, launches = apply_answers(repo, capsys, file)
    assert code == 2 and "no longer holds the text the proposals" in error and launches == []
    assert note_text(repo) == edited and run_dirs(repo) == before, "a refused command opens no run"
    recorded = record_answers(repo, capsys, file)
    assert recorded["answers"] == file and recorded["recorded"].startswith(ended["run-dir"] + "/answers/")
    listed = [(e["decision"], e["reason"]) for e in decisions.entries(repo[0]) if e["class"] == "plain-wording"]
    assert sorted(listed, key=str) == [("approved", None), ("approved", None), ("rejected", "a registered word")]


def test_automatic_preparation_publishes_without_a_stop(repo, capsys):
    original = start(repo)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess", "--purpose", "p")
    assert code == 0 and launches == ["assess - big", *ORDINARY]
    assert report["complete"] and report["published"] and report["not-published"] is None
    assert report["guard"]["clean"] and report["continuation"] is None and report["held"] is None
    for name in ("assessment.md", "plan.yaml"):
        assert artifact_file(repo, report, name).is_file()
    for name in ("final.md", "final.diff", edits.HELD):
        assert not artifact_file(repo, report, name).exists()
    [publication] = report["publications"]
    assert publication["entries"] == ["readability-and-flow", "place-external-systems", "opening-and-title"]
    assert note_text(repo) == (repo[0] / publication["text"]).read_text() != original
    assert [p["profile"]["launch-model"] for p in report["passes"]] == ["big", "small", "big"]
    assert report["new-warnings"] == []
    assert "user-verified" not in note_text(repo)


def test_a_held_candidate_is_published_only_by_naming_its_run(repo, capsys, tmp_path):
    original = start(repo, HELD_WORDS)
    code, ended, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    assert code == 0 and launches == [ORDINARY[0]] and note_text(repo) == original
    assert not ended["published"] and ended["publications"] == [] and not ended["complete"]
    [warning] = ended["new-warnings"]
    assert "250" in warning and "is published only when the operator names this run" in ended["not-published"]
    held = ended["held"]
    assert held["candidate"] == ended["proposed"] == f"{ended['run-dir']}/artifact/final.md"
    assert held["command"] == f"commonplace-review publish {ended['run-dir']}"
    [item] = ended["continuation"]["items"]
    assert (item["kind"], item["actor"], item["how"]["command"]) == ("held-candidate", "operator", held["command"])
    assert item["how"]["revised"] == held["command"] + " --revised FILE" and warning in item["what"]
    assert item["how"]["step"] == "A candidate held back for a validation warning"
    [pending] = [e for e in decisions.entries(repo[0]) if e["class"] == "publication"]
    assert (pending["decision"], pending["item"]) == ("pending", held["candidate"])
    candidate = artifact_file(repo, ended, "final.md").read_text()

    code, done = publish(repo, capsys, ended)
    assert code == 0 and LONG in note_text(repo) and note_text(repo) == candidate
    assert done["new-warnings"] == [warning] and done["published"]["decided-by"] == "operator"
    assert done["published"]["entries"] == ["readability-and-flow"] and not done["published"]["revised"]
    [entry] = [e for e in decisions.entries(repo[0]) if e["class"] == "publication"]
    assert (entry["decided-by"], entry["decision"], entry["revised"]) == ("operator", "published", False)
    code, error = publish(repo, capsys, ended)
    assert code == 2 and "already published" in error


@pytest.mark.parametrize("change", ["note", "brief", "candidate"])
def test_publishing_a_held_candidate_is_refused_once_its_inputs_change(repo, capsys, tmp_path, change):
    start(repo, HELD_WORDS)
    brief = add_brief(repo[0], NOTE_PATH)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    original = note_text(repo)
    if change == "note":
        (repo[0] / NOTE_PATH).write_text(original + "The operator's sentence.\n")
    elif change == "brief":
        brief.write_text(brief.read_text() + "\nKeep another passage.\n")
    else:
        artifact_file(repo, ended, "final.md").write_text(original + "Unchecked replacement.\n")
    before = note_text(repo)
    code, error = publish(repo, capsys, ended)
    assert code == 2 and ("nothing was written" in error or "not the candidate the run held" in error)
    assert note_text(repo) == before and not (repo[0] / ended["run-dir"] / edits.PUBLISHED).exists()


def test_a_warning_the_start_text_already_had_is_not_new(repo, capsys, tmp_path):
    start(repo, HELD_WORDS, text=NOTE.format(words=HELD_WORDS).replace("description: ", "description: " + LONG, 1))
    assert edits.validation(repo[0], NOTE_PATH, note_text(repo)).warns
    _, done, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    assert launches == [ORDINARY[0]] and done["complete"] and done["published"] and done["held"] is None
    assert done["new-warnings"] == []


LONG = "padding " * 32
CLOSING = "readability-and-flow (all).\n"


def test_a_revised_text_is_published_after_the_candidate_checks(repo, capsys, tmp_path):
    original = start(repo, HELD_WORDS)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    candidate = artifact_file(repo, ended, "final.md").read_text()
    source = tmp_path / "revised.md"
    for damage, problem in ((lambda text: text.replace("\n# Alpha\n", "\n# Beta\n"), "the H1 changed"),
                            (lambda text: text.replace("type: types/note.md\n", ""), "frontmatter `type` changed"),
                            (lambda text: text.replace("---\n", "", 1), "frontmatter does not parse"),
                            (lambda text: original, "is the note's current text")):
        source.write_text(damage(candidate))
        code, error = publish(repo, capsys, ended, "--revised", str(source))
        assert code == 2 and "the revised candidate is refused" in error and problem in error
        assert not artifact_file(repo, ended, "revised.md").exists() and note_text(repo) == original
    inside = artifact_file(repo, ended, "mine.md")
    inside.write_text(candidate)
    code, error = publish(repo, capsys, ended, "--revised", str(inside))
    assert code == 2 and "outside the run's artifact/" in error
    revised = candidate.replace("description: " + LONG, "description: ", 1).replace(
        CLOSING, "The operator's closing sentence.\n")              # the operator removes the warning
    source.write_text(revised)
    code, done = publish(repo, capsys, ended, "--revised", str(source))
    assert code == 0 and note_text(repo) == revised and done["new-warnings"] == []
    files = done["revised-candidate"]
    assert (repo[0] / files["revised"]).read_text() == revised
    assert (repo[0] / files["candidate"]).read_text() == candidate     # the workflow's candidate is kept
    assert "-readability-and-flow (all).\n+The operator's closing sentence.\n" in (
        repo[0] / files["diff-from-candidate"]).read_text()
    assert "+The operator's closing sentence.\n" in (repo[0] / files["diff-from-note"]).read_text()
    assert done["published"]["revised"] and done["published"]["sha256"] == observations.sha(revised.encode())
    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    [entry] = [e for e in json.loads(capsys.readouterr().out) if e["class"] == "publication"]
    assert entry["revised"] and (entry["decided-by"], entry["decision"]) == ("operator", "published")


def test_a_held_candidate_ends_the_run_before_the_next_per_item_pass_asks(repo, capsys, tmp_path):
    original = start(repo, HELD_WORDS)
    plan = named_plan(tmp_path, passes=("readability-and-flow", "plain-wording", "opening-and-title"))
    code, ended, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(plan))
    assert code == 0 and launches == [ORDINARY[0]], "the proposals are not asked for over a held text"
    assert [s["state"] for s in ended["passes"]] == ["applied", "pending", "pending"]
    assert not ended["published"] and note_text(repo) == original and ended["held"]
    assert items_of(ended) == [("held-candidate", "operator", []), ("per-item-entry", "worker", ["1"]),
                               ("direct-entry", "worker", ["2"])]
    per_item = ended["continuation"]["items"][1]
    assert per_item["effort"] == "simple" and "--pass plain-wording" in per_item["how"]["command"]
    assert ended["continuation"]["made-for"]["sha256"] == observations.sha(original.encode())
    code, _ = publish(repo, capsys, ended)
    assert code == 0 and LONG in note_text(repo)
    code, later, launches = continued(repo, capsys, per_item)
    assert code == 0 and launches == ["list plain-wording small"] and waiting(later)


def test_a_plan_stop_ends_the_run_and_a_replacement_plan_is_a_new_run(repo, capsys, tmp_path):
    original = start(repo, "STOP")
    code, ended, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 0 and ended["stop"] == "rewrite-needed" and note_text(repo) == original
    stop_file = f"{ended['run-dir']}/artifact/stop-answers.md"
    assert (repo[0] / stop_file).is_file()
    [item] = ended["continuation"]["items"]
    assert (item["kind"], item["actor"], item["answers"]) == ("plan-stop", "operator", [stop_file])
    assert item["how"]["command"] == f"commonplace-review run revise {NOTE_PATH} --plan <replacement-plan.yaml>"
    assert item["how"]["record"] == f"commonplace-review answers record {stop_file}"
    path = repo[0] / stop_file
    path.write_text(decide(path.read_text(), {"text": rejected("the note is fine")}))
    code, error, launches = apply_answers(repo, capsys, stop_file)
    assert code == 2 and "answers record" in error and launches == []
    code, fresh, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    assert code == 0 and fresh["stop"] is None and launches == [ORDINARY[0]] and fresh["complete"]
    assert note_text(repo).endswith("readability-and-flow (all).\n") and fresh["run-dir"] != ended["run-dir"]


@pytest.mark.parametrize("pass_name", ["plain-wording"])
def test_per_item_proposals_are_applied_only_from_the_named_answers(repo, capsys, tmp_path, pass_name):
    original = start(repo)
    _, ended, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=(pass_name,))))
    model = "small" if pass_name == "plain-wording" else "big"
    assert launches == [f"list {pass_name} {model}"]
    pending = yaml.safe_load((repo[0] / waiting(ended)).read_text().split("---\n")[1])
    assert pending["type"] == "types/answers.md" and pending["question"].endswith("/result.md")
    assert [item["state"] for item in pending["items"]] == ["pending"] * 3
    assert note_text(repo) == original, "nothing was applied before the stop"
    file = answer(repo, ended, {"beta": rejected("a registered word"),
                                "gamma": {"state": "deferred", "reason": "the term may be registered",
                                          "revisit": "when the vocabulary ledger decides"}})
    decided = (repo[0] / file).read_text()
    code, done, launches = apply_answers(repo, capsys, file)
    assert code == 0 and launches == [f"apply {pass_name} {model}"] and done["published"] and done["complete"]
    assert note_text(repo).endswith(f"{pass_name} applied alpha.\n")
    [applied] = [c for c in captured_inputs(repo[2]) if c["kind"] == "apply"]
    assert applied["inputs"]["answers"] == decided and "reason: a registered word" in decided
    (repo[0] / file).write_text("changed after the run\n")
    [(_, kept)] = decisions.kept_answers(repo[0], repo[0] / done["run-dir"])
    assert kept["text"] == decided and kept["sha256"] == observations.sha(decided.encode())


def _drop(text):
    data = yaml.safe_load(text.split("---\n")[1])
    del data["items"][1]
    return "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n"


@pytest.mark.parametrize("damage, problem", [
    (_drop, "item 2: missing"),
    (lambda text: decide(text, {"beta": {"state": "rejected"}}), "'reason' is a required property"),
])
def test_invalid_answers_are_refused_before_any_run(repo, capsys, tmp_path, damage, problem):
    original = start(repo)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    path = repo[0] / waiting(ended)
    pending = path.read_text()
    path.write_text(damage(pending))
    before = run_dirs(repo)
    code, error, launches = apply_answers(repo, capsys, waiting(ended))
    assert code == 2 and "not valid" in error and problem in error and launches == []
    assert note_text(repo) == original and run_dirs(repo) == before
    assert main(["answers", "record", waiting(ended)]) == 2
    assert problem in capsys.readouterr().err
    path.write_text(decide(pending, {"gamma": rejected("keep it")}, APPROVED))
    code, ready, launches = apply_answers(repo, capsys, waiting(ended))
    assert code == 0 and launches == ["apply plain-wording small"] and ready["complete"] and ready["published"]


def test_answers_that_approve_no_item_are_refused_and_recorded_instead(repo, capsys, tmp_path):
    original = start(repo)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    file = answer(repo, ended, {"alpha": rejected("alpha stays"), "beta": rejected("beta stays")}, default=None)
    code, error, launches = apply_answers(repo, capsys, file)
    assert code == 2 and "nothing to apply" in error and "answers record" in error and launches == []
    record_answers(repo, capsys, file)
    assert note_text(repo) == original
    listed = sorted(e["decision"] for e in decisions.entries(repo[0]) if e["class"] == "plain-wording")
    assert listed == ["pending", "rejected", "rejected"], "the undecided item is still the run's"


def test_brief_is_captured_for_assessment_passes_lists_and_apply(repo, capsys):
    start(repo, "PLAIN")
    brief = add_brief(repo[0], NOTE_PATH)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    _, ready, _ = apply_answers(repo, capsys, answer(repo, ended, {}))
    calls = captured_inputs(repo[2])
    assert {c["kind"] for c in calls} == {"assess", "pass", "list", "apply"}
    assert all(c["inputs"]["brief"] == brief.read_text() for c in calls)
    assert all("## Headless write briefs" in c["inputs"]["execution"] for c in calls if c["kind"] != "assess")
    [assess] = [c for c in calls if c["kind"] == "assess"]
    assert "The plan starts from the brief" in assess["inputs"]["criterion"], \
        "the planning instruction tells the assessor to add to the brief's Must keep, not restate it"
    assert ready["complete"] and ready["published"] and len(ready["publications"]) == 1
    started = json.loads((repo[0] / ready["run-dir"] / edits.START_RECORD).read_text())
    assert started["brief-sha256"] == observations.sha(brief.read_bytes())


def test_the_old_defend_name_is_refused_on_the_command_line_and_in_a_plan(repo, capsys, tmp_path):
    original = start(repo)
    with pytest.raises(SystemExit):
        main(["run", "revise", NOTE_PATH, "--pass", "readability-and-flow", "--defend", "Keep alpha"])
    capsys.readouterr()
    path = tmp_path / "old.yaml"
    path.write_text(yaml.safe_dump({"purpose": "p", "defend": ["Keep alpha"], "stop": None,
                                    "passes": [{"pass": "readability-and-flow"}]}))
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 2 and "unknown fields: defend" in error and "`must-keep` is missing" in error
    assert launches == [] and note_text(repo) == original
    _, ready, launches = revise(repo, capsys, NOTE_PATH, "--pass", "narrow-overclaims", "--must-keep", "Keep alpha")
    assert yaml.safe_load(artifact_file(repo, ready, "plan.yaml").read_text())["must-keep"] == ["Keep alpha"]
    assert launches == ["pass narrow-overclaims big"], "a non-empty must-keep list runs narrow-overclaims"
    [call] = captured_inputs(repo[2])
    assert call["inputs"]["must-keep"] == "- Keep alpha\n"


@pytest.mark.parametrize("kind", ["assess", "apply"])
def test_worker_brief_conflict_stops_without_publication(repo, capsys, kind):
    start(repo, "PLAIN")
    add_brief(repo[0], NOTE_PATH)
    file = None
    if kind == "apply":
        _, ended, _ = revise(repo, capsys, NOTE_PATH, "--assess")
        file = answer(repo, ended, {})
    original = note_text(repo)
    (repo[0] / f"brief-problem-{kind}").touch()
    code, report, launches = (apply_answers(repo, capsys, file) if file
                              else revise(repo, capsys, NOTE_PATH, "--assess"))
    assert code == 1 and "write brief" in report["stopped"] and not report["published"]
    assert note_text(repo) == original and launches[-1].startswith(kind + " ")
    assert not any("place-external-systems" in line for line in launches)
    if kind == "apply":
        assert items_of(report) == [("failure", "session-agent", []), ("per-item-entry", "worker", ["1"])]


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
    assert code == 1 and report["conflict"] and not report["published"] and report["publications"] == []
    if words == "BRIEFDRIFT":
        assert "write brief" in report["conflict"] and note_text(repo) == original
    else:
        assert note_text(repo).endswith("The operator's sentence.\n")
        assert report["guard"]["changed"] == [NOTE_PATH]


@pytest.mark.parametrize("words", ["BADPLAN", "RETITLE", "BADPASS"])
def test_correction_attempts_keep_safety_bounds(repo, capsys, words):
    original = start(repo, words)
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    if words == "BADPLAN":
        assert code == 0 and launches.count("assess - big") == 2
    elif words == "RETITLE":
        assert code == 0 and launches.count("pass readability-and-flow big") == 2
        assert "\n# Alpha\n" in note_text(repo)
    else:
        assert code == 1 and report["passes"][0]["state"] == "problem" and report["stopped"]
        assert [s["state"] for s in report["passes"]] == ["problem", "pending", "pending"]
        assert items_of(report) == [("failure", "session-agent", []), ("direct-entry", "worker", ["1"]),
                                    ("direct-entry", "worker", ["2"]), ("direct-entry", "worker", ["3"])]
        assert not report["published"] and note_text(repo) == original
        return
    assert report["published"] and note_text(repo) != original


def test_a_failed_entry_publishes_the_entries_before_it_and_a_later_run_continues(repo, capsys, tmp_path):
    original = start(repo)
    path = named_plan(tmp_path, passes=("readability-and-flow", "place-external-systems"))
    failure = repo[0] / "fail-place-external-systems"
    failure.touch()
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    assert code == 1 and report["stopped"].startswith("place-external-systems: ")
    assert launches == [ORDINARY[0]] + [ORDINARY[1]] * 3
    assert report["published"] and note_text(repo) != original
    assert note_text(repo).endswith("readability-and-flow (all).\n")
    assert [s["state"] for s in report["passes"]] == ["applied", "problem"]
    failed, entry = report["continuation"]["items"]
    assert (failed["kind"], failed["actor"], failed["how"]["step"]) == (
        "failure", "session-agent", "A worker or review failure")
    assert (entry["kind"], entry["after"], entry["effort"]) == ("direct-entry", ["1"], "simple")
    assert report["continuation"]["made-for"]["sha256"] == report["publications"][0]["sha256"]
    failure.unlink()
    code, ready, launches = continued(repo, capsys, entry)
    assert code == 0 and launches == [ORDINARY[1]] and ready["published"] and ready["complete"]
    assert note_text(repo).endswith("readability-and-flow (all).\nplace-external-systems (all).\n")


def test_a_failure_after_assessment_leaves_the_rest_of_the_plan_in_order(repo, capsys):
    start(repo)
    (repo[0] / "fail-place-external-systems").touch()
    code, stopped, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert code == 1 and stopped["stopped"] and stopped["published"]
    assert launches == ["assess - big", ORDINARY[0], *([ORDINARY[1]] * 3)]
    assert items_of(stopped) == [("failure", "session-agent", []), ("direct-entry", "worker", ["1"]),
                                 ("direct-entry", "worker", ["2"])]
    names = [item["how"]["command"].split("--pass ")[1].split()[0] for item in stopped["continuation"]["items"][1:]]
    assert names == ["place-external-systems", "opening-and-title"]
    evidence = stopped["continuation"]["items"][1]["evidence"]
    assert [Path(e).name for e in evidence] == ["assessment.md", "plan.yaml"]


def test_every_pass_candidate_comes_from_the_edit_route(repo, capsys, tmp_path):
    start(repo)
    path = named_plan(tmp_path, passes=("readability-and-flow", "plain-wording"))
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
    _, ready, _ = apply_answers(repo, capsys, answer(repo, ended, {"beta": rejected("a registered word")}))
    held = {}
    for report in (ended, ready):
        for record in sorted((repo[0] / report["run-dir"] / "artifact/edits").glob("*/observation.json")):
            data = json.loads(record.read_text())
            [result] = [name for name in data["completed-results"] if name.endswith("/result.md")]
            held[data["request"]["call-job"]] = yaml.safe_load((record.parent / result).read_text().split("---\n")[1])
    assert {job: data["outcome"] for job, data in held.items()} == {
        "readability-and-flow": "changed", "plain-wording/propose": "proposed", "plain-wording/apply": "changed"}
    assert held["plain-wording/propose"]["profile"]["launch-model"] == "small"
    for report, job in ((ended, "readability-and-flow"), (ready, "plain-wording/apply")):
        [state] = [s for s in report["passes"] if s["state"] == "applied"]
        assert (repo[0] / held[job]["candidate"]).read_text() == (repo[0] / state["text"]).read_text()


def test_decisions_command_lists_the_answers_of_a_revise_run(repo, capsys, tmp_path):
    start(repo)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    _, ready, _ = apply_answers(repo, capsys, answer(repo, ended, {"beta": rejected("a registered word")}))
    assert ready["published"]
    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    found = json.loads(capsys.readouterr().out)
    listed = [(e["class"], e["unit"], e["decided-by"], e["decision"], e["item"], e["reason"]) for e in found]
    text = ready["publications"][0]["text"]
    assert sorted(listed) == [
        ("plain-wording", "item", "operator", "approved", "Alpha body -> alpha", None),
        ("plain-wording", "item", "operator", "approved", "long enough -> gamma", None),
        ("plain-wording", "item", "operator", "rejected", "A note about -> beta", "a registered word"),
        ("publication", "bundle", "automatic", "published", text if len(text) <= 80 else text[:79] + "…", None)]
    assert {e["run"] for e in found} == {ready["run-dir"]}, "the consuming run keeps the answers"
    [automatic] = [e for e in found if e["class"] == "publication"]
    assert automatic["proposed-by"] == "workflow" and automatic["record"].endswith("/" + edits.PUBLISHED)
    assert automatic["at"] == ready["publications"][0]["at"]
    assert main(["decisions", "--note", NOTE_PATH]) == 0
    assert "| publication | bundle | workflow->automatic | published |" in capsys.readouterr().out


# --- Earlier decisions ---------------------------------------------------------------------

def items(repo, report):
    """The items of the answers file the run ended at, by proposed change."""
    head = (repo[0] / waiting(report)).read_text().split("---\n")[1]
    return {item["proposal"]["change"]: item for item in yaml.safe_load(head)["items"]}


def change_decision(repo, report, change, decision):
    """Record the operator's changed decision on a carried item: the earlier decision and `carried-from` go."""
    path = repo[0] / waiting(report)
    head, body = path.read_text().split("---\n")[1:]
    data = yaml.safe_load(head)
    for item in data["items"]:
        if item["proposal"]["change"] == change:
            for name in ("reason", "revisit", "carried-from"):
                item.pop(name, None)
            item.update(decision)
    path.write_text("---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n" + body)


def first_decisions(repo, capsys, tmp_path, words=""):
    """A plain-wording run on the note with `words`: alpha approved, beta rejected, gamma left pending; recorded."""
    start(repo, words)
    _, ended, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=("plain-wording",))))
    record_answers(repo, capsys, answer(repo, ended, {"alpha": APPROVED, "beta": rejected("a registered word")},
                                        default=None))
    return ended


def test_identical_proposals_carry_earlier_decisions(repo, capsys, tmp_path):
    first = first_decisions(repo, capsys, tmp_path)
    start(repo, "changed")
    plan = str(named_plan(tmp_path, passes=("plain-wording",)))
    _, second, launches = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    assert launches == ["list plain-wording small"] and second["run-dir"] != first["run-dir"]
    found = items(repo, second)
    assert found["alpha"]["state"] == "approved" and found["alpha"]["carried-from"] == waiting(first)
    assert (found["beta"]["state"], found["beta"]["reason"], found["beta"]["decided-at"]) == (
        "rejected", "a registered word", "2026-11-15T12:00:00Z")
    assert found["beta"]["carried-from"] == waiting(first)
    assert found["gamma"]["state"] == "pending" and "carried-from" not in found["gamma"]   # pending is not carried
    path = repo[0] / waiting(second)
    assert edits.answered(repo[0], path, path.read_text())[1] == []
    [listed] = [c for c in captured_inputs(repo[2]) if c["kind"] == "list" and "changed" in c["inputs"]["text"]]
    told = listed["inputs"]["earlier-decisions"]
    assert "> Alpha body" in told and "Operator's reason: a registered word" in told
    assert waiting(first) in told
    captured = json.loads((repo[0] / second["run-dir"] / revise_module.EARLIER_FILE).read_text())
    assert [d["proposal"]["change"] for d in captured["decisions"]] == ["alpha", "beta"]

    # The operator changes beta and decides gamma; that later decision wins in the next run.
    change_decision(repo, second, "beta", {"state": "approved", "decided-by": "operator",
                                           "decided-at": "2026-11-16T09:00:00Z"})
    answer(repo, second, {"gamma": rejected("keep it")}, default=None)
    record_answers(repo, capsys, waiting(second))
    start(repo, "changed again")
    _, third, launches = revise(repo, capsys, NOTE_PATH, "--plan", plan)
    assert launches == ["list plain-wording small"]
    found = items(repo, third)
    assert {change: item["state"] for change, item in found.items()} == {
        "alpha": "approved", "beta": "approved", "gamma": "rejected"}
    assert found["beta"]["carried-from"] == waiting(second) and "reason" not in found["beta"]
    assert found["alpha"]["carried-from"] in (waiting(first), waiting(second)), "both hold the same decision"
    assert not third["complete"], "every item carried; the run still ends at the answers file"
    code, _, launches = apply_answers(repo, capsys, waiting(third))
    assert code == 0 and launches == ["apply plain-wording small"]
    assert note_text(repo).endswith("plain-wording applied alpha beta.\n")

    assert main(["decisions", "--note", NOTE_PATH, "--json"]) == 0
    listed = json.loads(capsys.readouterr().out)
    carried = {(e["run"], e["item"]): e["carried-from"] for e in listed if e["class"] == "plain-wording"}
    assert carried[(second["run-dir"], "Alpha body -> alpha")] == waiting(first)
    assert carried[(second["run-dir"], "A note about -> beta")] is None
    assert main(["decisions", "--note", NOTE_PATH]) == 0
    assert f"carried-from: {waiting(first)}" in capsys.readouterr().out


def test_a_run_after_a_publication_receives_the_earlier_decisions(repo, capsys, tmp_path):
    first = first_decisions(repo, capsys, tmp_path)
    start(repo, "changed")
    _, ended, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path, passes=THREE)))
    assert ended["published"] and launches == [ORDINARY[0], "list plain-wording small"]
    found = items(repo, ended)
    assert found["alpha"]["carried-from"] == waiting(first) and found["beta"]["state"] == "rejected"
    _, done, launches = apply_answers(repo, capsys, answer(repo, ended, {"gamma": rejected("keep it")}, default=None))
    assert launches == ["apply plain-wording small"] and done["complete"] and done["published"]
    [applied] = [c for c in captured_inputs(repo[2]) if c["kind"] == "apply"]
    assert waiting(first) in applied["inputs"]["earlier-decisions"]
    assert note_text(repo).endswith("plain-wording applied alpha.\n")


def test_earlier_decisions_are_read_from_rewrite_runs_too(repo, capsys, tmp_path):
    first = first_decisions(repo, capsys, tmp_path)
    run = repo[0] / first["run-dir"]
    moved = repo[0] / first["run-dir"].replace("/v2/revise/", "/v2/rewrite/", 1)
    for name in ("answers", "artifact"):
        shutil.copytree(run / name, moved / name)
    shutil.rmtree(run / "answers")                  # only the rewrite tree now holds the operator's answers
    found = decisions.earlier(repo[0], NOTE_PATH)
    assert {decision["proposal"]["change"]: decision["state"] for decision in found} == {
        "alpha": "approved", "beta": "rejected"}
    assert all("/v2/revise/" in decision["answers-file"] for decision in found), "the origin is the file named"


def test_earlier_decisions_are_read_from_hash_named_run_directories(repo, capsys, tmp_path):
    first = first_decisions(repo, capsys, tmp_path)
    run = repo[0] / first["run-dir"]
    renamed = run.with_name("0123456789ab")
    run.rename(renamed)
    for record in (renamed / "answers").glob("*.json"):
        data = json.loads(record.read_text())
        data["origin"] = data["origin"].replace(run.name, renamed.name)
        data["text"] = data["text"].replace(run.name, renamed.name)
        record.write_text(json.dumps(data))
    found = decisions.earlier(repo[0], NOTE_PATH)
    assert {decision["proposal"]["change"] for decision in found} == {"alpha", "beta"}
    assert {e["run"] for e in decisions.entries(repo[0])} == {renamed.relative_to(repo[0]).as_posix()}


def stopped_run(repo, capsys, words, decision=None, recorded=True):
    """An assessed run on the note with `words` whose plan stops; record `decision` on its stop, if `recorded`."""
    start(repo, words)
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    file = f"{report['run-dir']}/artifact/stop-answers.md"
    if decision is not None:
        path = repo[0] / file
        path.write_text(decide(path.read_text(), {"text": decision}))
    if recorded:
        record_answers(repo, capsys, file)
    return report, file


def test_a_decided_stop_reaches_the_next_assessor_only(repo, capsys):
    _, first = stopped_run(repo, capsys, "STOP", {**rejected("the note is fine as one note"),
                                                  "resolution": "kept the note whole"})
    start(repo, "STOP PLAIN")
    _, second, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert launches[0] == "assess - big"
    given = assessed_inputs(repo)
    told = given["earlier-decisions"]
    assert told.startswith("# Earlier stops") and "> rewrite-needed" in told
    assert "Operator's reason: the note is fine as one note" in told
    assert f"{decisions.RESOLUTION}: kept the note whole" in told and first in told
    [prompt] = [line for line in (repo[0] / second["run-dir"]).rglob("prompt.txt")
                if "Assess one artifact" in line.read_text()]
    assert "`Earlier stops`" in prompt.read_text()
    captured = json.loads((repo[0] / second["run-dir"] / revise_module.STOPS_FILE).read_text())["stops"]
    assert [stop["answers-file"] for stop in captured] == [first]

    # Edit workers do not receive stops.
    start(repo, "PLAIN")
    _, _, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert "list plain-wording small" in launches
    assert "Earlier stops" in assessed_inputs(repo)["earlier-decisions"]
    workers = [c for c in captured_inputs(repo[2]) if c["kind"] != "assess"]
    assert workers and not any("Earlier stops" in text for c in workers for text in c["inputs"].values())


@pytest.mark.parametrize("decision, recorded", [(rejected("no"), False), (None, True)])
def test_an_undecided_or_unrecorded_stop_does_not_reach_the_assessor(repo, capsys, decision, recorded):
    stopped_run(repo, capsys, "STOP", decision, recorded)
    start(repo, "changed")
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    assert "earlier-decisions" not in assessed_inputs(repo)
    assert json.loads((repo[0] / report["run-dir"] / revise_module.STOPS_FILE).read_text()) == {"stops": []}


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


def test_pass_runs_a_one_entry_plan(repo, capsys):
    original = start(repo)
    with pytest.raises(SystemExit):
        main(["run", "revise", NOTE_PATH, "--pass", "readability-and-flow", "--assess"], harnesses=repo[1])
    capsys.readouterr()
    code, error, launches = revise(repo, capsys, NOTE_PATH, "--pass", "polish")
    assert code == 2 and "unknown pass `polish`" in error and launches == []
    code, ready, launches = revise(repo, capsys, NOTE_PATH, "--pass", "plain-wording", "--purpose", "Readers")
    assert code == 0 and ready["mode"] == "fixed-plan" and launches == ["list plain-wording small"]
    assert ready["plan"] == {"purpose": "Readers", "must-keep": [], "stop": None,
                             "passes": [{"pass": "plain-wording", "scope": None}]}
    assert not artifact_file(repo, ready, "assessment.md").exists() and note_text(repo) == original
    [item] = ready["continuation"]["items"]
    assert item["how"]["command"].endswith("--purpose Readers")
    answer(repo, ready, {})
    code, done, launches = continued(repo, capsys, item)
    assert launches == ["apply plain-wording small"] and done["published"]
    assert done["plan"]["purpose"] == "Readers"


def test_finding_runs_the_fix_with_its_result_as_input(repo, capsys):
    start(repo)
    finding = stored(repo, "warn")
    code, done, launches = revise(repo, capsys, NOTE_PATH, "--finding", str(repo[0] / finding))
    assert code == 0 and launches == ["pass fix-strategy-taxonomy big"]
    assert done["plan"]["passes"] == [{"pass": "fix-strategy-taxonomy", "scope": None, "finding": finding}]
    [state] = done["passes"]
    assert state["name"] == "fix-strategy-taxonomy/prose/residue"
    assert state["finding"] == finding and state["state"] == "applied"
    [call] = captured_inputs(repo[2])
    assert call["inputs"]["finding"] == (repo[0] / finding).read_text()
    assert done["published"] and note_text(repo).endswith("fix-strategy-taxonomy (all).\n")


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
        path.write_text(yaml.safe_dump({"purpose": "p", "must-keep": [], "stop": None, "passes": entries}))
        code, error, launches = revise(repo, capsys, NOTE_PATH, "--plan", str(path))
        assert code == 2 and problem in error and launches == [], error
    path.write_text(yaml.safe_dump({"purpose": "p", "must-keep": [], "stop": None,
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
    assert report["published"] and report["publications"][0]["entries"][0].startswith(revise_module.FIX)


# --- Triage ------------------------------------------------------------------------------------

PACKING = "kb/instructions/review-gates/sentence/packing.md"
HEDGING = "kb/instructions/review-gates/prose/hedging.md"


def finding(reason, level="warn"):
    return {"scope": "document", "quotes": [], "reason": reason, "level": level}


def triaged(repo, report, chosen):
    """Record the operator's decisions in each triage answers file; return the files.

    `chosen` maps a criterion id to the decisions by item id, as `decide()` takes them.
    """
    files = []
    for state in report["triage"]["results"]:
        path = repo[0] / state["answers"]
        path.write_text(decide(path.read_text(), chosen[state["criterion"]]))
        files.append(state["answers"])
    return files


def recorded(repo, capsys, files):
    for file in files:
        record_answers(repo, capsys, file)


def test_triage_without_warn_or_fail_findings_changes_nothing(repo, capsys):
    original = start(repo)
    stored(repo, "info")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--triage")
    assert code == 0 and report["complete"] and report["mode"] == "triage" and launches == []
    assert report["triage"] == {"results": [], "what": revise_module.NOTHING_TO_TRIAGE}
    assert report["plan"] is None and report["proposed"] is None and note_text(repo) == original


def test_triage_ends_at_each_answers_file_and_rejections_are_recorded(repo, capsys):
    original = start(repo)
    late = stored(repo, "fail", gate=PACKING, depth=5)
    early = stored(repo, "warn")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--triage")
    assert code == 0 and launches == [] and not report["complete"] and report["plan"] is None
    listed = report["triage"]["results"]
    assert [(s["result"], s["criterion"]) for s in listed] == [
        (early, "prose/residue"), (late, "sentence/packing")]     # in depth order
    assert re.fullmatch(r".*/artifact/finding-answers-[0-9a-f]{12}\.md", listed[0]["answers"])
    assert (repo[0] / listed[0]["question"]).read_text() == (repo[0] / early).read_text()
    head = yaml.safe_load((repo[0] / listed[0]["answers"]).read_text().split("---\n")[1])
    assert head["question"] == listed[0]["question"]
    assert head["items"] == [{"id": "1", "proposal": findings("warn")[0], "state": "pending"}]
    [item] = report["continuation"]["items"]
    assert (item["kind"], item["actor"], item["answers"]) == ("findings", "operator", [s["answers"] for s in listed])
    assert item["how"]["command"] == (f"commonplace-review run revise {NOTE_PATH} --answers {listed[0]['answers']} "
                                      f"--answers {listed[1]['answers']}")

    files = triaged(repo, report, {"prose/residue": {"1": rejected("wrong for this note only")},
                                   "sentence/packing": {"1": rejected("the criterion is too broad")}})
    code, error, launches = apply_answers(repo, capsys, *files)
    assert code == 2 and "nothing to apply" in error and launches == []
    recorded(repo, capsys, files)
    assert note_text(repo) == original

    assert main(["decisions", "--note", NOTE_PATH, "--class", "finding", "--json"]) == 0
    listed = json.loads(capsys.readouterr().out)
    assert sorted((e["unit"], e["decided-by"], e["decision"], e["item"], e["reason"]) for e in listed) == [
        ("item", "operator", "rejected", "prose/residue: warn: A fixture finding", "wrong for this note only"),
        ("item", "operator", "rejected", "sentence/packing: fail: A fixture finding", "the criterion is too broad")]


def test_triage_answers_fix_only_results_with_an_approved_finding(repo, capsys):
    start(repo)
    two = stored(repo, "warn", found=[finding("first"), finding("second")])
    stored(repo, "warn", gate=HEDGING, depth=3, found=[finding("hedged")])
    stored(repo, "fail", gate=PACKING, depth=5)
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage", "--purpose", "Readers")
    assert [s["criterion"] for s in report["triage"]["results"]] == ["prose/residue", "prose/hedging",
                                                                     "sentence/packing"]
    assert report["continuation"]["items"][0]["how"]["command"].endswith("--purpose Readers")
    files = triaged(repo, report, {"prose/residue": {"1": APPROVED, "2": rejected("not residue")},
                                   "prose/hedging": {"1": rejected("the hedge is needed")},
                                   "sentence/packing": {"1": APPROVED}})
    code, ready, launches = continued(repo, capsys, report["continuation"]["items"][0])
    questions = {s["criterion"]: s["question"] for s in report["triage"]["results"]}
    assert code == 0 and launches == ["pass fix-strategy-taxonomy big", "pass fix-strategy-taxonomy big"]
    assert ready["mode"] == "answers" and ready["answers"] == files
    assert ready["plan"] == {"purpose": "Readers", "must-keep": [], "stop": None, "passes": [
        {"pass": revise_module.FIX, "scope": None, "finding": questions["prose/residue"]},
        {"pass": revise_module.FIX, "scope": None, "finding": questions["sentence/packing"]}]}
    assert [s["state"] for s in ready["passes"]] == ["applied", "applied"]
    fixes = [c for c in captured_inputs(repo[2]) if c["pass"] == revise_module.FIX]
    answered = {s["question"]: (repo[0] / s["answers"]).read_text() for s in report["triage"]["results"]}
    assert fixes[0]["inputs"]["finding"] == (repo[0] / two).read_text()
    assert fixes[0]["inputs"][revise_module.FINDING_ANSWERS] == answered[questions["prose/residue"]]
    assert "not residue" in fixes[0]["inputs"][revise_module.FINDING_ANSWERS]
    assert fixes[1]["inputs"][revise_module.FINDING_ANSWERS] == answered[questions["sentence/packing"]]
    assert ready["complete"] and ready["published"] and ready["continuation"] is None
    [publication] = ready["publications"]
    assert publication["entries"] == ["fix-strategy-taxonomy/prose/residue", "fix-strategy-taxonomy/sentence/packing"]
    assert note_text(repo) == (repo[0] / publication["text"]).read_text()
    assert note_text(repo).endswith("fix-strategy-taxonomy (all).\nfix-strategy-taxonomy (all).\n")
    hedging = [e for e in decisions.entries(repo[0]) if e["class"] == "finding" and "hedging" in e["item"]]
    assert [(e["decision"], e["run"]) for e in hedging] == [("rejected", ready["run-dir"])], \
        "the consuming run keeps every named file, approved findings or not"
    code, error, _ = apply_answers(repo, capsys, *files)
    assert code == 2 and "no longer holds the text the review result" in error and "watches" in error


def test_triage_answers_fix_the_result_the_triage_copied_after_the_store_changes(repo, capsys):
    start(repo)
    result = stored(repo, "warn")
    captured = (repo[0] / result).read_text()
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    stored(repo, "fail", found=[finding("a new finding", "fail")])      # a new review replaces the result
    [file] = triaged(repo, report, {"prose/residue": {"1": APPROVED}})
    _, _, launches = apply_answers(repo, capsys, file)
    assert launches == ["pass fix-strategy-taxonomy big"]
    [fix] = [c for c in captured_inputs(repo[2]) if c["pass"] == revise_module.FIX]
    assert fix["inputs"]["finding"] == captured != (repo[0] / result).read_text()


def test_a_triage_carries_over_the_decision_on_an_identical_finding(repo, capsys):
    start(repo)
    stored(repo, "warn", found=[finding("same"), finding("other")])
    _, first, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    recorded(repo, capsys, triaged(repo, first, {"prose/residue": {"1": rejected("wrong for this note only"),
                                                                    "2": APPROVED}}))
    start(repo, "changed")                                   # another text: another run
    stored(repo, "warn", found=[finding("same"), finding("other, reworded")], decided=True)
    _, second, launches = revise(repo, capsys, NOTE_PATH, "--triage")
    assert launches == [] and second["run-dir"] != first["run-dir"] and not second["complete"]
    head = yaml.safe_load((repo[0] / second["triage"]["results"][0]["answers"]).read_text().split("---\n")[1])
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
    recorded(repo, capsys, triaged(repo, first, {"prose/residue": {"1": rejected("wrong for this note only")}}))
    assert results.freshness(repo[0], NOTE_PATH, GATE) == results.Freshness("stale", ("criterion",))

    # A later review that received the rejection raises it again beside two new findings.
    start(repo, text=frontmatter_only(text, "a"))
    answered = stored(repo, "warn", found=[finding("same"), finding("later"), finding("approved")], decided=True)
    assert results.freshness(repo[0], NOTE_PATH, GATE).state == "fresh"
    _, second, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    file = second["triage"]["results"][0]["answers"]
    head = yaml.safe_load((repo[0] / file).read_text().split("---\n")[1])
    assert head["items"][0]["state"] == "rejected" and "carried-from" in head["items"][0]
    recorded(repo, capsys, triaged(repo, second, {"prose/residue": {
        "2": {"state": "deferred", "reason": "after the rewrite", "revisit": "when the section is rewritten"},
        "3": APPROVED}}))
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
    start(repo, text=frontmatter_only(text, "c"))           # the assessed run published; another text again
    replaced = stored(repo, "warn", found=[finding("same"), finding("other")], decided=True)
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


def test_answers_record_takes_only_a_valid_file_under_a_run(repo, capsys, tmp_path):
    start(repo)
    result = stored(repo, "warn")
    assert main(["answers", "create", "--from", result, "--to", "kb/work/residue-answers.md"]) == 0
    capsys.readouterr()
    assert main(["answers", "record", "kb/work/residue-answers.md"]) == 2
    assert "not a file under the artifact/ directory" in capsys.readouterr().err
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    file = report["triage"]["results"][0]["answers"]
    first = record_answers(repo, capsys, file)
    path = repo[0] / file
    path.write_text(decide(path.read_text(), {"1": {**rejected("no"), "resolution": "kept as it is"}}))
    again = record_answers(repo, capsys, file)
    assert again["recorded"] == first["recorded"] and again["sha256"] != first["sha256"], "a record is replaced"
    [entry] = [e for e in decisions.entries(repo[0]) if e["class"] == "finding"]
    assert (entry["decision"], entry["resolution"]) == ("rejected", "kept as it is")


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
    original = start(repo, "PLAIN")                         # the plan ends at plain-wording
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--full", "--purpose", "p")
    assert code == 0 and report["mode"] == "full" and report["published"] and note_text(repo) != original
    assert set(launches[:6]) == REVIEWS and launches[6:8] == [SYNTHESIS, ROLE]
    assert launches[8:] == ["assess - big", ORDINARY[0], "list plain-wording small"]
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
    kinds = [row[0] for row in items_of(report)]
    assert kinds == ["proposals", "direct-entry", "direct-entry", "stale-reviews"]
    stale = report["continuation"]["items"][-1]
    assert stale["after"] == ["1", "2", "3"] and stale["actor"] == "worker"
    assert stale["how"]["command"] == f"commonplace-review status {NOTE_PATH} --stale"


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
    recorded(repo, capsys, triaged(repo, report, {"prose/warned": {"1": rejected("the criterion is too broad")}}))
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


WARNED = "kb/instructions/review-gates/prose/warned.md"


def record(repo, capsys, run_dir):
    """Run `record` on a revise run; return its report and the launches it made."""
    before = repo[2].read_text().splitlines()
    code = main(["record", run_dir], harnesses=repo[1])
    captured = capsys.readouterr()
    assert code == 0, captured.err
    return json.loads(captured.out), repo[2].read_text().splitlines()[len(before):]


def files(directory):
    return {path.relative_to(directory).as_posix(): path.read_bytes()
            for path in directory.rglob("*") if path.is_file()}


def test_record_keeps_the_operators_decisions_on_the_findings_of_an_overtaken_run(reviewed, capsys):
    repo = reviewed
    text = start(repo, "STOP")
    result = stored(repo, "warn", gate=WARNED, found=[finding("diagnosis"), finding("undiscussed")])
    stored(repo, "info")                                          # a pass result asks nothing
    _, stopped, _ = revise(repo, capsys, NOTE_PATH, "--assess")
    assert stopped["stop"] and stopped["findings"] == [result]
    run = repo[0] / stopped["run-dir"]
    split = text.replace("STOP", "STOP, split into three notes")
    (repo[0] / NOTE_PATH).write_text(split)                      # the operator's split: the run's plan is moot
    before = files(run)

    report, launches = record(repo, capsys, stopped["run-dir"])
    assert launches == [] and report["overtaken"] and report["artifact"] == NOTE_PATH
    [listed] = report["results"]
    assert (listed["result"], listed["criterion"], listed["state"]) == (result, "prose/warned", "written")
    assert re.fullmatch(r".*/artifact/finding-answers-[0-9a-f]{12}\.md", listed["file"])
    assert listed["command"] == f"commonplace-review answers record {listed['file']}"
    path = repo[0] / listed["file"]
    head = yaml.safe_load(path.read_text().split("---\n")[1])
    assert (repo[0] / head["question"]).read_text() == (repo[0] / result).read_text()
    assert [(item["id"], item["state"]) for item in head["items"]] == [("1", "pending"), ("2", "pending")]
    after = files(run)
    new = {name for name in after if name not in before}
    assert new == {"artifact/findings/prose/warned.md", f"artifact/{path.name}"}
    assert [name for name in before if after[name] != before[name]] == [], "no plan, fix or publication"

    again, launches = record(repo, capsys, stopped["run-dir"])
    assert launches == [] and [given["state"] for given in again["results"]] == ["exists"]
    assert files(run) == after

    path.write_text(decide(path.read_text(), {"1": {
        "state": "rejected", "reason": "the diagnosis is wrong",
        "resolution": "retained its question, whether the note holds three claims; answered it by the split",
        "refs": ["kb/notes/alpha-one.md", "kb/notes/alpha-two.md"]}}))
    assert edits.answered(repo[0], path, path.read_text())[1] == []
    record_answers(repo, capsys, listed["file"])
    assert main(["decisions", "--note", NOTE_PATH, "--class", "finding", "--json"]) == 0
    entries = json.loads(capsys.readouterr().out)
    assert [(e["decision"], e["reason"], e["resolution"], e["refs"]) for e in entries] == [
        ("rejected", "the diagnosis is wrong",
         "retained its question, whether the note holds three claims; answered it by the split",
         ["kb/notes/alpha-one.md", "kb/notes/alpha-two.md"]),
        ("overtaken", None, None, None)], "the undecided finding is no pending work"

    # The next run on the edited note receives the rejection with its resolution.
    _, later, launches = revise(repo, capsys, NOTE_PATH, "--assess")
    assert later["run-dir"] != stopped["run-dir"] and later["stop"] and not later["published"]
    [decision] = json.loads((repo[0] / later["run-dir"] / revise_module.EARLIER_FILE).read_text())["decisions"]
    assert (decision["state"], decision["criterion"]) == ("rejected", WARNED)
    assert decision["resolution"].startswith("retained its question")
    told = assessed_inputs(repo)["earlier-decisions"]
    assert f"{decisions.RESOLUTION}: retained its question" in told
    swept = gates_run(repo, capsys)
    [given] = (repo[0] / swept["run-dir"]).glob("artifact/reviews/*/inputs/operational/finding-decisions.md")
    text = given.read_text()
    assert decisions.RETAINED_QUESTION in text and "Operator's reason: the diagnosis is wrong" in text
    assert f"{decisions.RESOLUTION}: retained its question" in text and "undiscussed" not in text
    assert not (run / edits.PUBLISHED).exists() and note_text(repo) == split


def test_record_makes_no_second_file_for_a_result_a_triage_asked_about(repo, capsys):
    start(repo)
    stored(repo, "warn")
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--triage")
    run = repo[0] / report["run-dir"]
    before = files(run)
    recorded, launches = record(repo, capsys, report["run-dir"])
    [listed] = recorded["results"]
    assert launches == [] and not recorded["overtaken"] and listed["state"] == "exists"
    assert listed["file"] == report["triage"]["results"][0]["answers"]
    assert {name for name in files(run) if name not in before} == set()


def test_record_refuses_a_run_without_review_results(repo, capsys, tmp_path):
    start(repo)
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--plan", str(named_plan(tmp_path)))
    assert main(["record", report["run-dir"]], harnesses=repo[1]) == 2
    assert "holds no review results" in capsys.readouterr().err


@pytest.mark.slow
def test_record_takes_the_results_of_a_full_run(reviewed, capsys):
    repo = reviewed
    start(repo, "STOP")
    _, stopped, _ = revise(repo, capsys, NOTE_PATH, "--full")
    (repo[0] / NOTE_PATH).write_text(note_text(repo) + "\nSplit into three notes.\n")
    report, launches = record(repo, capsys, stopped["run-dir"])
    assert launches == [] and report["overtaken"]
    assert [(given["criterion"], given["state"]) for given in report["results"]] == [("prose/warned", "written")]


@pytest.mark.slow
def test_a_plan_stop_leaves_an_answers_file_that_takes_a_resolution_and_refs(reviewed, capsys):
    repo = reviewed
    start(repo, "STOP")
    _, report, _ = revise(repo, capsys, NOTE_PATH, "--full")
    [item] = report["continuation"]["items"]
    [file] = item["answers"]
    path = repo[0] / file
    assert path.name == "stop-answers.md" and not report["complete"] and report["guard"]["clean"]
    assert [e["decision"] for e in decisions.entries(repo[0]) if e["class"] == "stop"] == ["pending"]
    original = note_text(repo)
    (repo[0] / NOTE_PATH).write_text(original + "\nAn edit after the stop.\n")
    assert [e["decision"] for e in decisions.entries(repo[0]) if e["class"] == "stop"] == ["overtaken"]
    (repo[0] / NOTE_PATH).write_text(original)
    path.write_text(decide(path.read_text(), {"text": {
        "state": "rejected", "reason": "the note needs a rewrite", "resolution": "rewrote the note",
        "refs": ["0123abc", "kb/work/some-workshop"]}}))
    record_answers(repo, capsys, file)
    [entry] = [e for e in decisions.entries(repo[0]) if e["class"] == "stop"]
    assert (entry["decision"], entry["resolution"], entry["refs"], entry["proposed-by"]) == (
        "rejected", "rewrote the note", ["0123abc", "kb/work/some-workshop"], "worker")
    assert "refs: 0123abc, kb/work/some-workshop" in decisions.text([entry])


@pytest.mark.slow
def test_full_stops_when_a_review_has_no_result(reviewed, capsys):
    repo = reviewed
    original = start(repo, "NOREVIEW")
    code, report, launches = revise(repo, capsys, NOTE_PATH, "--full")
    assert code == 1 and "ended without a result" in report["stopped"] and "critique" in report["stopped"]
    assert not any(line.startswith("assess") for line in launches) and SYNTHESIS not in launches
    assert ROLE not in launches
    assert note_text(repo) == original
    assert items_of(report) == [("failure", "session-agent", [])]
