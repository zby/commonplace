"""`commonplace-review run full-pass` end to end on a fake harness; no model is called.

The fake worker knows each ask by its task's first line, logs its kind per
launch, and answers from the table `ANSWERS` below. Words in the note's
start text choose the scenario: REVISE makes the packet `revise`, RETITLE
makes the editor's first attempt change the H1, REPAIR makes the first
closing cycle `repair-needed`, HANDBACK makes closing `hand-back`, and TOUCH
makes the copyeditor edit the note's file, as a concurrent operator would.
A file `fail-<kind>` in the working directory makes that kind exit 1.
"""

from __future__ import annotations

import functools
import json
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.headless.jobs import Run
from commonplace.lib import library
from commonplace.lib.review_workflows import full_pass as full_pass_module
from commonplace.lib.review_workflows.full_pass import packet_file
from commonplace.lib.review_workflows.results import read_result, result_path
from commonplace.lib.validation import validate_note
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, REPO_ROOT

FAKE = r"""
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
KINDS = {"Review one note": "review", "Apply one method": "method", "Write the packet": "packet",
         "Edit one note": "edit", "Copyedit one note": "copyedit", "Decide the closing": "closing"}
kind = next(kind for start, kind in KINDS.items() if frame.removeprefix("Task:\n").startswith(start))
if kind == "edit" and "defects" in inputs:
    kind = "repair"
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(kind + "\n")
if Path(f"fail-{kind}").exists():
    sys.exit(1)
note = inputs["note"].read_text()
start = inputs["start"].read_text() if "start" in inputs else note
rejected = "was rejected" in frame


def packet():
    disposition = "revise" if "REVISE" in note else "keep"
    return (f"---\ndisposition: {disposition}\nupdate: determined\nmerge-target: null\n---\n\n"
            f"## Warranted contribution\n\nUpdate.\n\n## Disposition\n\n**{disposition}**\n\n"
            "## Body edits\n\nAdd one sentence.\n\n## Routed attention\n\nNone.\n")


def closing():
    if "HANDBACK" in start:
        status, defects = "hand-back", []
    elif "REPAIR" in start and "Repaired." not in note:
        status, defects = "repair-needed", ["the added sentence repeats the title"]
    else:
        status, defects = "ready", []
    return f"---\nstatus: {status}\nupdate: preserved\ndefects: {json.dumps(defects)}\n---\n\nBasis.\n"


def edit():
    text = note.replace("\n# Alpha\n", "\n# Beta\n") if "RETITLE" in note and not rejected else note
    return text.replace("user-verified: true\n", "") + "Edited.\n"


def copyedit():
    if "TOUCH" in note:
        Path("kb/notes/alpha.md").write_text(note + "The operator's sentence.\n")
    return note.replace("Edited.", "Copyedited.")


ANSWERS = {
    "review": lambda: "## Result: REPORT\n" if "`## Result: REPORT`" in frame else "## Result: PASS\n",
    "method": lambda: "# Report\n\nNothing to add.\n",
    "packet": packet, "edit": edit, "copyedit": copyedit, "closing": closing,
    "repair": lambda: note + "Repaired.\n",
}
for path in outputs.values():
    path.write_text("### Summary\n\nReviewed.\n\n" + ANSWERS[kind]() if kind == "review" else ANSWERS[kind]())
"""

PROFILES = "default: fake\nprofiles:\n  fake: {harness: fake, launch-model: m, effort: low}\n"
GATE = ("---\ngate_id: prose/{name}\ntype: types/review-gate.md\nwatches: [{watches}]\nstaleness: changed\n---\n\n"
        "## Failure mode\n\n{name} fails.\n")
INSTRUCTION = "# Full pass\n\nAnswer the decision table.\n\n## Copyedit\n\nSmooth the flow only.\n\n## Do not\n\nNo.\n"
NOTE = ("---\ndescription: A note about alpha that is long enough to describe what it is for\n"
        "type: types/note.md\nuser-verified: true\n---\n\n# Alpha\n\nAlpha body {words}.\n")
FILES = {
    "kb/instructions/review-profiles.yaml": PROFILES,
    "kb/instructions/review-gates/prose/body-gate.md": GATE.format(name="body-gate", watches="body"),
    "kb/instructions/review-gates/prose/title-gate.md": GATE.format(name="title-gate", watches="title"),
    "kb/instructions/critique-note.md": "# Critique\n\nWrite a critique.\n",
    "kb/instructions/run-full-improvement-pass-on-note.md": INSTRUCTION,
    "kb/instructions/run-compression-bundle-on-note.md": "# Compression\n\nApply the criteria.\n",
    "kb/instructions/compression-bundle/core-claim-obscured.md": "# Core claim obscured\n",
    "kb/instructions/composition-friction-gate.md": "# Friction\n",
    "kb/instructions/premise-decomposition-gate.md": "# Premises\n",
    "kb/instructions/cp-skill-connect/SKILL.md": "# Connect\n",
    "kb/notes/COLLECTION.md": "# Notes\n\nOne claim per note.\n",
}
NOTE_PATH = "kb/notes/alpha.md"
METHOD_ASKS = 5      # compression, friction, premises, connect, critique
GATE_ASKS = 1        # both prose gates in one bundle call


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    root = tmp_path / "repo"
    for rel in (*NOTE_TYPE_SPECS, "kb/types/full-pass-report.md", "kb/types/full-pass-report.schema.yaml"):
        FILES[rel] = (REPO_ROOT / rel).read_text(encoding="utf-8")
    for rel, text in FILES.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    for args in (("init", "-q"), ("config", "user.email", "t@example.com"), ("config", "user.name", "t")):
        subprocess.run(["git", *args], cwd=root, check=True)
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    monkeypatch.setattr(full_pass_module, "Run", functools.partial(Run, sleep=lambda seconds: None))
    monkeypatch.chdir(root)
    script, log = tmp_path / "fake.py", tmp_path / "launches.log"
    script.write_text(FAKE)
    log.touch()
    harness = Harness(sys.executable, {"_subcommand": [str(script)], "_env": {"FAKE_LOG": str(log)}},
                      lambda profile: {}, model_used=lambda launch: "fake-model-1")
    return root, {"fake": harness}, log


def start(repo, words: str = "") -> str:
    """Write the note with the scenario words and commit everything."""
    root = repo[0]
    text = NOTE.format(words=words)
    (root / NOTE_PATH).write_text(text, encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=root, check=True)
    return text


def full_pass(repo, capsys, *args: str) -> tuple[int, dict, list[str]]:
    """Run the full pass; return the exit code, the report and this run's launches by kind."""
    _, harnesses, log = repo
    before = log.read_text().splitlines()
    code = main(["run", "full-pass", NOTE_PATH, "--timeout", "30", *args], harnesses=harnesses)
    return code, json.loads(capsys.readouterr().out), log.read_text().splitlines()[len(before):]


def note_text(repo) -> str:
    return (repo[0] / NOTE_PATH).read_text(encoding="utf-8")


def packet(repo) -> tuple[dict, str]:
    from commonplace.lib import frontmatter
    text = packet_file(repo[0], NOTE_PATH).read_text(encoding="utf-8")
    return frontmatter.parse(text).data, text


def assert_valid_packet(repo) -> None:
    result = validate_note(packet_file(repo[0], NOTE_PATH), repo_root=repo[0])
    assert not result.fails, result.fails


def test_keep_writes_the_copyedited_text_and_closes_ready(repo, capsys):
    text = start(repo)
    code, report, launches = full_pass(repo, capsys)
    assert code == 0, (report["stopped"], report["conflict"])
    assert (report["disposition"], report["closing-status"], report["restored"]) == ("keep", "ready", False)
    assert report["guard"] == {"clean": True, "changed": []}, "the pass's own write is expected"
    final = note_text(repo)
    assert final.endswith("Copyedited.\n") and "user-verified" not in final
    assert sorted(launches) == sorted(["method"] * 4 * 2 + ["review"] * (2 + 2 * GATE_ASKS)
                                      + ["packet", "edit", "copyedit", "closing"])
    data, body = packet(repo)
    assert (data["resolution"], data["final-sha256"] != data["start-sha256"]) == ("not-required", True)
    assert body.count("## Closing cycle: initial") == 1
    assert_valid_packet(repo)
    # The gate results are ordinary result files, hashed over the written text.
    gate = read_result(result_path(repo[0], NOTE_PATH, "prose/body-gate"))
    assert gate.run == report["run-dir"] and text != final


def test_one_bounded_repair_then_ready(repo, capsys):
    start(repo, "REPAIR")
    code, report, launches = full_pass(repo, capsys)
    assert code == 0, report
    assert (report["closing-status"], report["repaired"], len(report["written"])) == ("ready", True, 2)
    assert note_text(repo).endswith("Copyedited.\nRepaired.\n")
    assert launches.count("repair") == 1 and launches.count("closing") == 2
    assert "## Closing cycle: recovery" in packet(repo)[1]


def test_hand_back_restores_the_start_text_and_blocks_until_the_note_changes(repo, capsys):
    text = start(repo, "HANDBACK")
    code, report, _ = full_pass(repo, capsys)
    assert code == 0, report
    assert (report["closing-status"], report["restored"]) == ("hand-back", True)
    assert note_text(repo) == text and report["guard"]["clean"]
    data, _ = packet(repo)
    assert (data["resolution"], data["final-sha256"]) == ("pending", data["start-sha256"])
    assert_valid_packet(repo)


def test_pending_disposition_survives_the_run_and_blocks_a_second_pass(repo, capsys):
    text = start(repo, "REVISE")
    code, report, launches = full_pass(repo, capsys)
    assert code == 0, report
    assert (report["disposition"], report["closing-status"], report["written"]) == ("revise", None, [])
    assert note_text(repo) == text and "edit" not in launches
    data, _ = packet(repo)
    assert (data["disposition"], data["resolution"], data["run"]) == ("revise", "pending", report["run-dir"])
    assert_valid_packet(repo)
    assert (repo[0] / report["run-dir"] / "artifact" / "packet.md").read_text() == packet(repo)[1]

    assert main(["packet", NOTE_PATH], harnesses=repo[1]) == 0
    assert json.loads(capsys.readouterr().out)["matching"]
    runs = sorted((repo[0] / report["run-dir"]).parent.iterdir())
    code, again, launches = full_pass(repo, capsys)
    assert (code, again["blocked"], again["packet"], launches) == (0, True, report["packet"], [])
    assert again["run-dir"] == report["run-dir"] and sorted((repo[0] / report["run-dir"]).parent.iterdir()) == runs

    (repo[0] / NOTE_PATH).write_text(text + "An author's edit.\n", encoding="utf-8")
    assert main(["packet", NOTE_PATH], harnesses=repo[1]) == 1
    assert json.loads(capsys.readouterr().out)["inputs"][0]["state"] == "changed"
    code, third, launches = full_pass(repo, capsys)
    assert not third["blocked"] and "packet" in launches


def test_an_editor_text_that_changes_the_title_costs_one_attempt(repo, capsys):
    start(repo, "RETITLE")
    code, report, launches = full_pass(repo, capsys)
    assert code == 0 and launches.count("edit") == 2
    events = [json.loads(line) for line in (repo[0] / report["run-dir"] / "log.jsonl").read_text().splitlines()]
    [rejected] = [event for event in events if event["event"] == "rejected"]
    assert rejected["job"] == "edit" and "the H1 changed; keep `# Alpha`" in rejected["problems"]
    assert "\n# Alpha\n" in note_text(repo)


def test_a_concurrent_edit_stops_the_write(repo, capsys):
    start(repo, "TOUCH")
    code, report, _ = full_pass(repo, capsys)
    assert code == 1 and "changed during the pass" in report["conflict"]
    assert note_text(repo).endswith("The operator's sentence.\n"), "the operator's text stays"
    assert report["written"] == [] and report["guard"]["changed"] == [NOTE_PATH]


def test_resume_after_a_launch_failure_does_not_reapply_the_edit(repo, capsys):
    start(repo, "REPAIR")
    (repo[0] / "fail-repair").touch()
    code, report, launches = full_pass(repo, capsys)
    assert code == 1 and "repair" in report["stopped"] and launches.count("repair") == 3
    written = note_text(repo)
    assert written.endswith("Copyedited.\n"), "the first write happened before the stop"

    (repo[0] / "fail-repair").unlink()
    code, resumed, launches = full_pass(repo, capsys, "--resume", report["run-dir"])
    assert code == 0, resumed
    assert sorted(launches) == sorted(["repair", "closing"] + ["method"] * 4 + ["review"] * (1 + GATE_ASKS))
    assert note_text(repo) == written + "Repaired.\n"
    writes = json.loads((repo[0] / report["run-dir"] / "artifact" / "writes.json").read_text())
    assert len(writes) == 2 and resumed["written"] == report["written"] + [writes[1]["to"]]
