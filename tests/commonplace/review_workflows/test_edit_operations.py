"""One edit operation run alone, `commonplace-revise try`, on a fake worker; no model is called.

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

from commonplace.cli.review_workflows import main, revise_main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run
from commonplace.lib import frontmatter, library
from commonplace.lib.review_workflows import edit_operations, fixtures, observations
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

FAKE = r'''
import json, os, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text(encoding="utf-8")
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
text = inputs["text"].read_text(encoding="utf-8")
first = "was rejected" not in frame
defect = Path(os.environ["FAKE_BEHAVIOUR"]).read_text(encoding="utf-8").strip() if first else ""
with open(os.environ["FAKE_LOG"], "a", encoding="utf-8") as log:
    log.write(json.dumps({"inputs": {key: path.read_text(encoding="utf-8") for key, path in inputs.items()}, "first": first}) + "\n")
if "PROBLEM" in text:
    Path(frame.split("problem file:\n")[1].splitlines()[0]).write_text(json.dumps(
        {"kind": "unable", "message": "The operation cannot run on this text."}), encoding="utf-8")
    sys.exit(0)

def result(outcome, **fields):
    data = {"type": "types/edit-result.md", "outcome": outcome, **fields}
    if defect == "owned":
        data["input-sha256"] = "0" * 64
    outputs["result"].write_text("---\n" + json.dumps(data) + "\n---\n\n# Report\n\nDone.\n", encoding="utf-8")

if "This operation asks before it edits" in frame:
    quotes = ["Nonexistent passage" if defect == "badquote" else "Alpha body", "Closing sentence"]
    result("proposed", proposals=[{"quote": quote, "change": quote.upper(), "reason": "plainer"} for quote in quotes])
elif "The operator answered" in frame:
    import yaml
    answers = yaml.safe_load(inputs["answers"].read_text(encoding="utf-8").split("---\n")[1])
    applied = text
    for item in answers["items"]:
        if item["state"] == "approved" or defect == "applyother":
            quote = item["proposal"]["quote"]
            applied = applied.replace(quote, quote.upper())
    outputs["candidate"].write_text(applied, newline="\n", encoding="utf-8")
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
    elif defect == "crlf":
        candidate = candidate.replace("\n", "\r\n")
    outputs["candidate"].write_bytes(candidate.encode())
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
LIBRARY = ("kb/types/edit-result.md", "kb/types/edit-result.schema.yaml", "kb/types/answers.md",
           "kb/types/answers.schema.yaml", f"kb/{NONE_OP}", f"kb/{PER_ITEM_OP}",
           f"kb/{edit_operations.EXECUTION_REL}")


@pytest.fixture
def repo(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    files = {rel: (REPO_ROOT / rel).read_text(encoding="utf-8") for rel in (*NOTE_TYPE_SPECS, *LIBRARY)}
    files |= {"kb/instructions/review-profiles.yaml": PROFILES, "kb/notes/COLLECTION.md": "# Notes\n",
              NOTE_PATH: NOTE.format(words=""),
              "kb/notes/beta.md": NOTE.format(words="").replace("# Alpha", "# Beta")}
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8", newline="\n")
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
    """Run `commonplace-revise try`; return the exit code, the report or error, and this run's launches."""
    before = repo[2].read_text().splitlines()
    code = revise_main(["try", *args, "--timeout", "30"], harnesses=repo[1])
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
    (repo[0] / NOTE_PATH).write_text(NOTE.format(words=words), encoding="utf-8", newline="\n")


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
    directory = (repo[0] / data["observation"]).parent
    observation = observations.load(directory)
    assert not (directory / "inputs").exists()
    assert not list(directory.glob("results/*/candidate.md")), "Workjig owns raw candidate bytes"
    if data["candidate"] is not None:
        assert "/calls/launches/" in data["candidate"]
    assert observation["request"]["kind"] == "edit" and observation["state"] == "completed"
    assert {item["role"] for item in observation["inputs"]} >= {"target", "criterion", "prompt", "contract"}


@pytest.mark.parametrize("defect, problem", [
    ("retitle", "the H1 changed"),
    ("droplink", "the link to `./beta.md` is gone"),
    ("quote", "the quoted span `A quoted line that must stay.` changed"),
    ("same", "the candidate equals the input text"),
    ("owned", "remove controller-owned or unknown fields: input-sha256"),
])
def test_each_bounds_failure_goes_back_to_the_worker(repo, capsys, defect, problem):
    repo[3].write_text(defect)
    code, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert code == 0 and report["outcome"] == "changed" and len(launches) == 2, report
    assert any(problem in found for found in rejections(repo, report)), rejections(repo, report)


def test_candidate_line_endings_are_retained_as_the_worker_wrote_them(repo, capsys):
    """The result cites Workjig's output file, so its hash is over the bytes the worker wrote."""
    words = "Alpha — 東京"
    set_note(repo, words)
    repo[3].write_text("crlf")
    code, report, _ = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert code == 0 and report["outcome"] == "changed", report
    data = result(repo, report).data
    written = (repo[0] / data["candidate"]).read_bytes()
    assert b"\r\n" in written and b"\r\n" not in NOTE.encode()
    assert words.encode("utf-8") in written
    assert data["candidate-sha256"] == observations.sha(written)
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 0, capsys.readouterr().err


def test_a_named_link_removal_is_accepted(repo, capsys):
    repo[3].write_text("namedlink")
    code, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH)
    assert code == 0 and len(launches) == 1 and result(repo, report).data["removed-links"] == ["./beta.md"]


def test_text_option_edits_a_saved_text_and_records_its_hash(repo, capsys):
    saved = NOTE.format(words="A saved start text.")
    (repo[0] / "kb/notes/saved.md").write_text(saved, encoding="utf-8", newline="\n")
    code, report, launches = edit(repo, capsys, NONE_OP, NOTE_PATH, "--text", "kb/notes/saved.md")
    assert code == 0 and launches[0]["inputs"]["text"] == saved
    data = result(repo, report).data
    assert data["note"] == NOTE_PATH and data["input-sha256"] == observations.sha(saved.encode())
    assert "A saved start text." in (repo[0] / data["candidate"]).read_text()
    assert (repo[0] / NOTE_PATH).read_text() == NOTE.format(words="")


def test_reserved_roles_and_answers_for_a_none_operation_are_command_errors(repo, capsys):
    (repo[0] / "kb/notes/answers.md").write_text("---\ntype: types/answers.md\n---\n\n# Answers\n")
    code, error, launches = edit(repo, capsys, NONE_OP, NOTE_PATH, "--input", "text=kb/notes/beta.md")
    assert code == 2 and "reserved" in error and launches == []
    code, error, launches = edit(repo, capsys, NONE_OP, NOTE_PATH, "--input", "answers=kb/notes/answers.md")
    assert code == 2 and "only a per-item operation" in error and launches == []


def propose(repo, capsys) -> tuple[dict, str]:
    """Run the per-item operation's first run and create its pending answers; return the report and its path."""
    code, proposed, _ = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH)
    assert code == 0 and proposed["outcome"] == "proposed", proposed
    assert revise_main(["answers", "create", "--from", proposed["result"]]) == 0
    created = json.loads(capsys.readouterr().out)
    return proposed, created["answers"]


def decide(repo, path: str, states: dict[str, dict]) -> str:
    """Record the operator's decision on items of the answers file at `path`, as the decide-items stop does."""
    file = repo[0] / path
    head, body = file.read_text().split("---\n")[1:]
    data = yaml.safe_load(head)
    for item in data["items"]:
        if item["id"] in states:
            item.update(states[item["id"]])
            if item["state"] != "pending":
                item.setdefault("decided-by", "operator")
                item.setdefault("decided-at", "2026-11-15T12:00:00Z")
    text = "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n" + body
    file.write_text(text)
    return text


def test_per_item_operation_proposes_then_applies_only_approved_items(repo, capsys):
    repo[3].write_text("badquote")
    code, proposed, launches = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH)
    assert code == 0 and proposed["outcome"] == "proposed" and len(launches) == 2, proposed
    assert any("occurs 0 times in the input text" in problem for problem in rejections(repo, proposed))
    data = result(repo, proposed).data
    assert data["candidate"] is None and [p["quote"] for p in data["proposals"]] == ["Alpha body", "Closing sentence"]
    assert data["profile"]["launch-model"] == "small"                   # plain-wording is simple
    assert revise_main(["answers", "create", "--from", proposed["result"]]) == 0
    path = json.loads(capsys.readouterr().out)["answers"]
    pending = frontmatter.parse((repo[0] / path).read_text()).data
    assert pending["question"] == proposed["result"]
    assert pending["question-sha256"] == observations.sha((repo[0] / proposed["result"]).read_bytes())
    assert [(item["id"], item["proposal"], item["state"]) for item in pending["items"]] == [
        ("1", data["proposals"][0], "pending"), ("2", data["proposals"][1], "pending")]
    assert revise_main(["answers", "create", "--from", proposed["result"]]) == 2
    assert "not replaced" in capsys.readouterr().err
    answered = decide(repo, path, {"1": {"state": "approved"},
                                   "2": {"state": "rejected", "reason": "keep the closing words"}})
    repo[3].write_text("applyother")
    code, applied, launches = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH, "--input", f"answers={path}")
    assert code == 0 and applied["outcome"] == "changed" and len(launches) == 2, applied
    assert any("the item `Closing sentence` is not approved but was applied" in problem
               for problem in rejections(repo, applied))
    candidate = (repo[0] / result(repo, applied).data["candidate"]).read_text()
    assert "ALPHA BODY" in candidate and "Closing sentence." in candidate
    assert launches[-1]["inputs"]["answers"] == answered


@pytest.mark.parametrize("states", [
    {"2": {"state": "deferred", "reason": "the term may be registered", "revisit": "when the ledger decides"}},
    {},
])
def test_deferred_and_pending_items_are_not_applied(repo, capsys, states):
    _, path = propose(repo, capsys)
    decide(repo, path, {"1": {"state": "approved"}, **states})
    code, applied, _ = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH, "--input", f"answers={path}")
    assert code == 0 and applied["outcome"] == "changed", applied
    candidate = (repo[0] / result(repo, applied).data["candidate"]).read_text()
    assert "ALPHA BODY" in candidate and "Closing sentence." in candidate


@pytest.mark.parametrize("change, problem", [
    (lambda repo, path: decide(repo, path, {"1": {"state": "rejected", "reason": "no"}}), "no item is approved"),
    (lambda repo, path: set_note(repo, "Edited since."), "made from another text"),
])
def test_unusable_answers_stop_before_any_launch(repo, capsys, change, problem):
    _, path = propose(repo, capsys)
    decide(repo, path, {"1": {"state": "approved"}})
    change(repo, path)
    code, error, launches = edit(repo, capsys, PER_ITEM_OP, NOTE_PATH, "--input", f"answers={path}")
    assert code == 2 and problem in error and launches == [], error


def test_answers_to_another_operation_are_refused(repo, capsys):
    _, path = propose(repo, capsys)
    decide(repo, path, {"1": {"state": "approved"}})
    other = "instructions/simplification-passes/abstractions.md"
    (repo[0] / "kb" / other).write_text((repo[0] / "kb" / PER_ITEM_OP).read_text())
    code, error, launches = edit(repo, capsys, other, NOTE_PATH, "--input", f"answers={path}")
    assert code == 2 and f"not of kb/{other}" in error and launches == [], error


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
    assert main(["--fixture", name], harnesses=repo[1]) == 2
    assert "commonplace-revise try --fixture" in capsys.readouterr().err
    before = len(repo[2].read_text().splitlines())
    assert revise_main(["try", "--fixture", name], harnesses=repo[1]) == 0
    trial = json.loads(capsys.readouterr().out)
    assert len(repo[2].read_text().splitlines()) == before + 1
    assert trial["observations"][0]["state"] == "edited" and trial["observations"][0]["outcome"] == "changed"
    assert not trial["changed"] and (root / NOTE_PATH).read_text() == NOTE.format(words="")
    assert main(["show", trial["run-dir"], "--json"], harnesses=repo[1]) == 0
    [held] = json.loads(capsys.readouterr().out)["observations"]
    assert held["results"][0]["input-sha256"] == record["results"][0]["input-sha256"]
