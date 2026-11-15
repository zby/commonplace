"""One edit operation run alone, `commonplace-review run edit`, on a fake worker; no model is called.

The fake worker reads its frame and the input text. The behaviour file
outside the repository names a defect the worker commits on its first
attempt only, so each test sees one rejection and an accepted correction.
Words in the note choose the outcome: UNCHANGED and PROBLEM.
"""

from __future__ import annotations

import functools
import json
import subprocess
import sys

import pytest
import yaml

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run
from commonplace.lib import frontmatter, library
from commonplace.lib.review_workflows import edit_operations, fixtures, observations
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
text = inputs["text"].read_text()
first = "was rejected" not in frame
defect = Path(os.environ["FAKE_BEHAVIOUR"]).read_text().strip() if first else ""
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(json.dumps({"inputs": {key: path.read_text() for key, path in inputs.items()}, "first": first}) + "\n")
if "PROBLEM" in text:
    Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(json.dumps(
        {"kind": "unable", "message": "The operation cannot run on this text."}))
    sys.exit(0)

def result(outcome, **fields):
    data = {"type": "types/edit-result.md", "outcome": outcome, **fields}
    if defect == "owned":
        data["input-sha256"] = "0" * 64
    outputs["result"].write_text("---\n" + json.dumps(data) + "\n---\n\n# Report\n\nDone.\n")

if "This operation asks before it edits" in frame:
    quotes = ["Nonexistent passage" if defect == "badquote" else "Alpha body", "Closing sentence"]
    result("proposed", proposals=[{"quote": quote, "change": quote.upper(), "reason": "plainer"} for quote in quotes])
elif "The operator answered" in frame:
    answers = inputs["answers"].read_text()
    applied = text
    for entry in re.findall(r"^- quote: (.*)\n  change: .*\n  reason: .*\n(  struck:)?", answers, re.MULTILINE):
        if not entry[1] or defect == "applystruck":
            applied = applied.replace(entry[0], entry[0].upper())
    outputs["candidate"].write_text(applied)
    result("changed", changes=["applied the approved entries"])
elif "UNCHANGED" in text:
    result("unchanged")
elif defect == "outcome":
    result("proposed", proposals=[{"quote": "Alpha body", "change": "x", "reason": "y"}])
else:
    candidate = text.replace("Closing sentence.", "Closing sentence, tightened.")
    removed = []
    if defect == "retitle":
        candidate = candidate.replace("# Alpha", "# Gamma")
    elif defect in ("droplink", "namedlink"):
        candidate = candidate.replace("[beta](./beta.md)", "beta")
        removed = ["./beta.md"] if defect == "namedlink" else []
    elif defect == "quote":
        candidate = candidate.replace("must stay", "may go")
    elif defect == "same":
        candidate = text
    outputs["candidate"].write_text(candidate)
    result("changed", changes=["tightened the closing sentence"], **({"removed-links": removed} if removed else {}))
'''
PROFILES = ("default: s\neffort: {simple: s, judgment: j}\nprofiles:\n"
            "  s: {harness: fake, launch-model: small, effort: low}\n"
            "  j: {harness: fake, launch-model: big, effort: high}\n")
NOTE = ("---\ndescription: A note about alpha that is long enough to describe what it is for\n"
        "type: types/note.md\n---\n\n# Alpha\n\nAlpha body links to [beta](./beta.md). {words}\n\n"
        "> A quoted line that must stay.\n\nClosing sentence.\n")
NOTE_PATH = "kb/notes/alpha.md"
NONE_OP = "instructions/simplification-passes/readability-and-flow.md"
PER_ITEM_OP = "instructions/simplification-passes/plain-wording.md"
LIBRARY = ("kb/types/edit-result.md", "kb/types/edit-result.schema.yaml", f"kb/{NONE_OP}", f"kb/{PER_ITEM_OP}",
           f"kb/{edit_operations.EXECUTION_REL}")


@pytest.fixture
def repo(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text() for rel in (*NOTE_TYPE_SPECS, *LIBRARY)}
    files |= {"kb/instructions/review-profiles.yaml": PROFILES, "kb/notes/COLLECTION.md": "# Notes\n",
              NOTE_PATH: NOTE.format(words=""),
              "kb/notes/beta.md": NOTE.format(words="").replace("# Alpha", "# Beta")}
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    for args in (("init", "-q"), ("config", "user.email", "t@example.com"), ("config", "user.name", "t"),
                 ("add", "."), ("commit", "-qm", "seed")):
        subprocess.run(["git", *args], cwd=root, check=True)
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    monkeypatch.setattr(edit_operations, "Run", functools.partial(Run, sleep=lambda seconds: None))
    monkeypatch.chdir(root)
    script, log, behaviour = tmp_path / "fake.py", tmp_path / "launches.log", tmp_path / "behaviour"
    script.write_text(FAKE)
    log.touch()
    behaviour.write_text("")
    harness = Harness(sys.executable, {"_subcommand": [str(script)],
                                       "_env": {"FAKE_LOG": str(log), "FAKE_BEHAVIOUR": str(behaviour)}},
                      lambda profile: {"model": profile.launch_model}, model_used=lambda launch: "fake-model-1")
    return root, {"fake": harness}, log, behaviour


def edit(repo, capsys, *args):
    """Run `commonplace-review run edit`; return the exit code, the report or error, and this run's launches."""
    before = repo[2].read_text().splitlines()
    code = main(["run", "edit", *args, "--timeout", "30"], harnesses=repo[1])
    captured = capsys.readouterr()
    launches = [json.loads(line) for line in repo[2].read_text().splitlines()[len(before):]]
    return code, json.loads(captured.out) if code != 2 else captured.err, launches


def result(repo, report):
    return frontmatter.parse((repo[0] / report["result"]).read_text())


def rejections(repo, report):
    log = repo[0] / report["run-dir"] / "log.jsonl"
    return [problem for event in map(json.loads, log.read_text().splitlines())
            if event["event"] == "rejected" for problem in event["problems"]]


def set_note(repo, words):
    (repo[0] / NOTE_PATH).write_text(NOTE.format(words=words))


@pytest.mark.parametrize("words, outcome, code", [("", "changed", 0), ("UNCHANGED", "unchanged", 0),
                                                  ("PROBLEM", "problem", 1)])
def test_none_operation_outcomes_are_typed_and_write_nothing(repo, capsys, words, outcome, code):
    set_note(repo, words)
    original = (repo[0] / NOTE_PATH).read_text()
    status, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert status == code and report["outcome"] == outcome and len(launches) == 1, report
    assert (repo[0] / NOTE_PATH).read_text() == original and report["guard"]["clean"]
    data = result(repo, report).data
    assert data["type"] == "types/edit-result.md" and data["outcome"] == outcome
    assert data["operation"] == f"kb/{NONE_OP}" and data["model"] == "fake-model-1"
    assert data["input-sha256"] == observations.sha(original.encode())
    assert data["profile"]["launch-model"] == "big"                     # readability-and-flow is judgment
    if outcome == "changed":
        candidate = (repo[0] / data["candidate"]).read_text()
        assert candidate.endswith("Closing sentence, tightened.\n")
        assert data["candidate-sha256"] == observations.sha(candidate.encode())
    elif outcome == "unchanged":
        assert (repo[0] / data["candidate"]).read_text() == original
    else:
        assert data["candidate"] is None and data["raw-output"] is None
        assert "cannot run" in report["problem"]
    observation = observations.load(repo[0] / data["observation"].removesuffix("/observation.json"))
    assert observation["request"]["kind"] == "edit" and observation["state"] == "completed"
    assert {item["role"] for item in observation["inputs"]} >= {"target", "criterion", "prompt", "contract"}


@pytest.mark.parametrize("defect, problem", [
    ("retitle", "the H1 changed"),
    ("droplink", "the link to `./beta.md` is gone"),
    ("quote", "the quoted span `A quoted line that must stay.` changed"),
    ("same", "the candidate equals the input text"),
    ("owned", "remove controller-owned or unknown fields: input-sha256"),
    ("outcome", "`outcome` must be changed or unchanged"),
])
def test_each_bounds_failure_goes_back_to_the_worker(repo, capsys, defect, problem):
    repo[3].write_text(defect)
    code, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert code == 0 and report["outcome"] == "changed" and len(launches) == 2, report
    assert any(problem in found for found in rejections(repo, report)), rejections(repo, report)


def test_a_named_link_removal_is_accepted(repo, capsys):
    repo[3].write_text("namedlink")
    code, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert code == 0 and len(launches) == 1 and result(repo, report).data["removed-links"] == ["./beta.md"]


def test_text_option_edits_a_saved_text_and_records_its_hash(repo, capsys):
    saved = NOTE.format(words="A saved start text.")
    (repo[0] / "kb/notes/saved.md").write_text(saved)
    code, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH, "--text", "kb/notes/saved.md")
    assert code == 0 and launches[0]["inputs"]["text"] == saved
    data = result(repo, report).data
    assert data["note"] == NOTE_PATH and data["input-sha256"] == observations.sha(saved.encode())
    assert "A saved start text." in (repo[0] / data["candidate"]).read_text()
    assert (repo[0] / NOTE_PATH).read_text() == NOTE.format(words="")


def test_reserved_roles_and_answers_for_a_none_operation_are_command_errors(repo, capsys):
    (repo[0] / "kb/notes/answers.md").write_text("- quote: Alpha body\n  change: A\n  reason: r\n")
    code, error, launches = edit(repo, capsys, NONE_OP, NOTE_PATH, "--input", "text=kb/notes/beta.md")
    assert code == 2 and "reserved" in error and launches == []
    code, error, launches = edit(repo, capsys, NONE_OP, NOTE_PATH, "--input", "answers=kb/notes/answers.md")
    assert code == 2 and "only a per-item operation" in error and launches == []


def test_per_item_operation_proposes_then_applies_only_approved_entries(repo, capsys):
    repo[3].write_text("badquote")
    code, proposed, launches = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH)
    assert code == 0 and proposed["outcome"] == "proposed" and len(launches) == 2, proposed
    assert any("occurs 0 times in the input text" in problem for problem in rejections(repo, proposed))
    data = result(repo, proposed).data
    assert data["candidate"] is None and [p["quote"] for p in data["proposals"]] == ["Alpha body", "Closing sentence"]
    assert data["profile"]["launch-model"] == "small"                   # plain-wording is simple
    listed = edit_operations.strike_list(data["proposals"])
    assert yaml.safe_load(listed) == data["proposals"]
    struck = "  change: CLOSING SENTENCE\n  reason: plainer\n"
    answered = listed.replace(struck, struck + "  struck: keep the closing words\n")
    (repo[0] / "kb/notes/answers.md").write_text(answered)
    repo[3].write_text("applystruck")
    code, applied, launches = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH, "--input", "answers=kb/notes/answers.md")
    assert code == 0 and applied["outcome"] == "changed" and len(launches) == 2, applied
    assert any("struck entry `Closing sentence` was applied" in problem for problem in rejections(repo, applied))
    candidate = (repo[0] / result(repo, applied).data["candidate"]).read_text()
    assert "ALPHA BODY" in candidate and "Closing sentence." in candidate
    assert launches[-1]["inputs"]["answers"] == answered


@pytest.mark.parametrize("answered, problem", [
    ("- quote: Alpha body\n  change: A\n  reason: r\n  struck: no\n", "approves no entry"),
    ("- quote: Absent passage\n  change: A\n  reason: r\n", "occurs 0 times"),
    ("- quote: Alpha body\n  change: A\n  reason: r\n  struck:\n", "struck without a reason"),
])
def test_unusable_answers_stop_before_any_launch(repo, capsys, answered, problem):
    (repo[0] / "kb/notes/answers.md").write_text(answered)
    code, error, launches = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH, "--input", "answers=kb/notes/answers.md")
    assert code == 2 and problem in error and launches == []


def test_edit_fixture_reruns_one_execution_and_show_validates_it(repo, capsys):
    root = repo[0]
    code, report, _ = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert code == 0
    observation = report["observation"].rsplit("/", 1)[-1]
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 0
    shown = json.loads(capsys.readouterr().out)
    [record] = shown["observations"]
    assert [item["outcome"] for item in record["results"]] == ["changed"]
    fixture = fixtures.create(root, report["run-dir"], observation, substitute_executor=True)
    name = fixture.relative_to(root).as_posix()
    assert main(["run", "gates", "--fixture", name], harnesses=repo[1]) == 2
    assert "run edit --fixture" in capsys.readouterr().err
    before = len(repo[2].read_text().splitlines())
    assert main(["run", "edit", "--fixture", name], harnesses=repo[1]) == 0
    trial = json.loads(capsys.readouterr().out)
    assert len(repo[2].read_text().splitlines()) == before + 1
    assert trial["observations"][0]["state"] == "edited" and trial["observations"][0]["outcome"] == "changed"
    assert not trial["changed"] and (root / NOTE_PATH).read_text() == NOTE.format(words="")
    assert main(["show", trial["run-dir"], "--json"], harnesses=repo[1]) == 0
    [held] = json.loads(capsys.readouterr().out)["observations"]
    assert held["results"][0]["input-sha256"] == record["results"][0]["input-sha256"]
