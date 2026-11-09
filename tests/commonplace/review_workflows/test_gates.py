"""The gate sweep and `commonplace-review` end to end on a fake harness; no model is called.

The fake worker reads the frame it is pointed at, logs `<note>::<criterion>`
per launch, and writes a review whose result line follows the contract the
prompt asks for. Words in the note's text choose its behaviour: FAILME gives
FAIL, MALFORMED omits the result line until the prompt carries a rejection,
CANNOT writes the problem file, and STRAY also writes a file in the checkout.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.lib import library
from commonplace.lib.review_workflows.results import read_result, result_path

FAKE = r"""
import json, os, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text()
def listed(name):
    return re.search(rf"^- {re.escape(name)}: (.+)$", frame, re.MULTILINE).group(1)
note = Path(listed("note.md")).read_text()
pair = re.search(r"The note is `([^`]+)`", frame).group(1) + "::" + re.search(r"The criterion is `([^`]+)`", frame).group(1)
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(pair + "\n")
if "CANNOT" in note:
    problem = frame.split("problem file:\n")[1].splitlines()[0]
    Path(problem).write_text(json.dumps({"kind": "unable", "message": "the note is unreadable"}))
    sys.exit(0)
if "STRAY" in note:
    Path("stray.md").write_text("written by a reviewer\n")
if "MALFORMED" in note and "was rejected" not in frame:
    result = "Verdict: fine"
elif "`## Result: REPORT`" in frame:
    result = "## Result: REPORT"
else:
    result = "## Result: FAIL" if "FAILME" in note else "## Result: PASS"
Path(listed("review.md")).write_text(f"### Summary\n\nReviewed.\n\n{result}\n")
"""

PROFILES = """default: fake
profiles:
  fake: {harness: fake, launch-model: m, effort: low}
"""


def gate(name: str, watches: str) -> str:
    return (f"---\ngate_id: prose/{name}\ntype: types/review-gate.md\nwatches: [{watches}]\n"
            f"staleness: changed\n---\n\n## Failure mode\n\n{name} fails.\n")


def note(title: str, body: str, description: str = "A note") -> str:
    return f"---\ndescription: {description}\ntype: types/note.md\n---\n\n# {title}\n\n{body}\n"


FILES = {
    "kb/instructions/review-profiles.yaml": PROFILES,
    "kb/instructions/review-gates/prose/body-gate.md": gate("body-gate", "body"),
    "kb/instructions/review-gates/prose/description-gate.md": gate("description-gate", "description"),
    "kb/instructions/critique-note.md": "# Critique\n\nWrite a critique.\n",
    "kb/types/note.md": "# Note type\n\nWrite one claim.\n",
    "kb/notes/COLLECTION.md": "# Notes\n\nOne claim per note.\n",
    "kb/notes/alpha.md": note("Alpha", "Alpha body."),
    "kb/notes/beta.md": note("Beta", "Beta body FAILME."),
}
GATE_DIR = "kb/instructions/review-gates/prose"
BODY_GATE = f"{GATE_DIR}/body-gate.md"
DESCRIPTION_GATE = f"{GATE_DIR}/description-gate.md"


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    root = tmp_path / "repo"
    for rel, text in FILES.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    git(root, "init", "-q")
    git(root, "config", "user.email", "t@example.com")
    git(root, "config", "user.name", "t")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "seed")
    (root / "other.md").write_text("another session's uncommitted work\n")
    monkeypatch.setattr(library, "_library_root", lambda _override: (root / "kb").resolve())
    monkeypatch.chdir(root)
    script, log = tmp_path / "fake.py", tmp_path / "launches.log"
    script.write_text(FAKE)
    log.touch()
    harness = Harness(sys.executable, {"_subcommand": [str(script)], "_env": {"FAKE_LOG": str(log)}},
                      lambda profile: {}, model_used=lambda launch: "fake-model-1")
    return root, {"fake": harness}, log


def review(repo, capsys, *args: str) -> tuple[int, dict, list[str]]:
    """Run `commonplace-review run gates`; return the exit code, the report and this run's launches."""
    _, harnesses, log = repo
    before = log.read_text().splitlines()
    code = main(["run", "gates", *args, "--timeout", "30"], harnesses=harnesses)
    return code, json.loads(capsys.readouterr().out), log.read_text().splitlines()[len(before):]


def write(root: Path, rel: str, text: str) -> None:
    (root / rel).write_text(text, encoding="utf-8")


def test_sweep_writes_one_result_per_pair_and_a_rerun_launches_nothing(repo, capsys):
    root = repo[0]
    code, report, launches = review(repo, capsys, "kb/notes", "--criteria", "prose", "type", "collection",
                                    "critique")
    assert code == 0, report
    # Two notes (COLLECTION.md is not one) x (two gates, type, collection, critique).
    assert len(launches) == len(set(launches)) == 10 and report["counts"] == {"reviewed": 10}
    assert report["guard"] == {"clean": True, "changed": []}
    outcomes = {(pair["note"], pair["criterion"]): pair["outcome"] for pair in report["pairs"]}
    assert outcomes[("kb/notes/beta.md", BODY_GATE)] == "fail"
    assert outcomes[("kb/notes/alpha.md", "kb/types/note.md")] == "pass"
    assert outcomes[("kb/notes/alpha.md", "kb/notes/COLLECTION.md")] == "pass"
    assert outcomes[("kb/notes/alpha.md", "kb/instructions/critique-note.md")] == "report"

    result = read_result(result_path(root, "kb/notes/beta.md", "prose/body-gate"))
    assert (result.outcome, result.model, result.run) == ("fail", "fake-model-1", report["run-dir"])
    assert result.profile == {"harness": "fake", "launch-model": "m", "effort": "low"}
    assert (root / report["run-dir"] / "calls" / "launches" / result.launch).is_dir()
    assert result.body.endswith("## Result: FAIL\n")

    code, again, launches = review(repo, capsys, "kb/notes", "--criteria", "prose", "type", "collection",
                                   "critique")
    assert (code, launches, again["counts"]) == (0, [], {"fresh": 10})
    assert again["run-dir"] != report["run-dir"]


def test_note_edit_reasks_only_the_pairs_whose_watched_parts_changed(repo, capsys):
    root = repo[0]
    assert review(repo, capsys, "kb/notes", "--criteria", "prose")[0] == 0
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body, edited."))
    write(root, "kb/notes/beta.md", note("Beta", "Beta body FAILME.", description="Beta restated"))
    code, report, launches = review(repo, capsys, "kb/notes", "--criteria", "prose")
    assert code == 0
    assert sorted(launches) == [f"kb/notes/alpha.md::{BODY_GATE}", f"kb/notes/beta.md::{DESCRIPTION_GATE}"]
    assert report["counts"] == {"fresh": 2, "reviewed": 2}


def test_malformed_review_costs_one_corrected_attempt(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "MALFORMED body."))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0 and launches == [f"kb/notes/alpha.md::{BODY_GATE}"] * 2
    events = [json.loads(line) for line in (root / report["run-dir"] / "log.jsonl").read_text().splitlines()]
    assert [event["problems"] for event in events if event["event"] == "rejected"] == [
        ["invalid result signal: Verdict: fine"]]
    assert read_result(result_path(root, "kb/notes/alpha.md", "prose/body-gate")).outcome == "pass"


def test_worker_problem_leaves_no_result_and_the_other_pairs_complete(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "CANNOT be reviewed."))
    code, report, _ = review(repo, capsys, "kb/notes", "--criteria", "prose/body-gate")
    assert code == 1 and not report["ok"]
    by_note = {pair["note"]: pair for pair in report["pairs"]}
    assert by_note["kb/notes/alpha.md"]["state"] == "problem"
    assert by_note["kb/notes/alpha.md"]["problem"] == "the note is unreadable"
    assert not result_path(root, "kb/notes/alpha.md", "prose/body-gate").exists()
    assert by_note["kb/notes/beta.md"]["state"] == "reviewed"


def test_worker_writing_the_checkout_fails_the_run_through_the_guard(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "STRAY body."))
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    # The edit of alpha.md happened before the run, so only the worker's file is reported.
    assert code == 1 and report["guard"] == {"clean": False, "changed": ["stray.md"]}
    assert report["counts"] == {"reviewed": 1}


def test_status_reports_fresh_stale_missing_and_orphaned_results(repo, capsys):
    root, harnesses, _ = repo
    write(root, "kb/notes/gamma.md", note("Gamma", "Gamma body."))
    assert review(repo, capsys, "kb/notes", "--criteria", "prose/body-gate")[0] == 0   # a FAIL is a result
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body, edited."))
    write(root, "kb/notes/delta.md", note("Delta", "Delta body."))
    (root / "kb/notes/gamma.md").unlink()
    assert main(["status", "kb/notes", "--criteria", "prose/body-gate", "--json"], harnesses=harnesses) == 0
    status = json.loads(capsys.readouterr().out)
    rows = {row["note"]: (row["freshness"], row["changed"], row["outcome"], row["model"]) for row in status["pairs"]}
    assert rows == {
        "kb/notes/alpha.md": ("stale", ["note"], "pass", "fake-model-1"),
        "kb/notes/beta.md": ("fresh", [], "fail", "fake-model-1"),
        "kb/notes/delta.md": ("missing", [], None, None),
    }
    assert status["orphaned"] == [
        "kb/reports/state/review/results/kb/notes/gamma.md/prose/body-gate.md"]
