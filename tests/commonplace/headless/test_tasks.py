"""Tests for launching one kb/tasks runbook on a fake harness; no model is called.

The fake worker reads the frame it is pointed at and the runbook, appends a line to the
task's log, commits as the runbook says, and writes the result file. Words
in the runbook choose misbehaviour: STRAY also writes a file outside the
write scope, UNCOMMITTED edits the log without committing, TWICE makes two
commits, and WRONG-SUBJECT commits under another subject.
"""

import subprocess
import sys

import pytest

from commonplace.headless.harness import Harness
from commonplace.lib.tasks import launch, load_profile, load_runbook

FAKE = r"""
import re, subprocess, sys
from pathlib import Path
prompt = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text() + Path("kb/tasks/demo.md").read_text()
result = re.search(r"^- result\.md: (.+)$", prompt, re.MULTILINE).group(1)
subject = re.search(r"subject `([^`]+)`", prompt).group(1)
log = Path("kb/tasks/demo-log.md")
log.write_text(log.read_text() + "\n## run\n")
if "STRAY" in prompt:
    Path("kb/tasks/stray.md").write_text("stray\n")
if "UNCOMMITTED" not in prompt:
    if "WRONG-SUBJECT" in prompt:
        subject = "Something else"
    subprocess.run(["git", "add", str(log)], check=True)
    subprocess.run(["git", "commit", "-q", "-m", subject], check=True)
    if "TWICE" in prompt:
        log.write_text(log.read_text() + "again\n")
        subprocess.run(["git", "add", str(log)], check=True)
        subprocess.run(["git", "commit", "-q", "-m", subject], check=True)
head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
Path(result).write_text(f"commit: {head}\nappended one section\n")
"""

RUNBOOK = """# Demo task

## Run Procedure

- Append a section to the log.{marker}

## Output

Record findings in `kb/tasks/demo-log.md`.

## Write scope

`kb/tasks/demo-log.md` only. The run stages exactly this file and commits it
with the subject `Run recurring task demo`.
"""

PROFILES = """default: fake
profiles:
  fake: {harness: fake, launch-model: m, effort: low}
"""


def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    (root / "kb" / "tasks").mkdir(parents=True)
    git(root, "init", "-q")
    git(root, "config", "user.email", "t@example.com")
    git(root, "config", "user.name", "t")
    (root / "kb/tasks/demo-log.md").write_text("# Demo log\n")
    (root / "kb/tasks/profiles.yaml").write_text(PROFILES)
    (root / "other.md").write_text("someone else's uncommitted work\n")
    git(root, "add", "kb/tasks/demo-log.md", "kb/tasks/profiles.yaml")
    git(root, "commit", "-q", "-m", "seed")
    script = tmp_path / "fake.py"
    script.write_text(FAKE)
    harness = Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile: {},
                      model_used=lambda launch: "fake-model-1" if launch.status == "delivered" else None)
    return root, {"fake": harness}


def run_demo(repo, marker=""):
    root, harnesses = repo
    (root / "kb/tasks/demo.md").write_text(RUNBOOK.format(marker=marker))
    git(root, "add", "kb/tasks/demo.md")
    git(root, "commit", "-q", "-m", "add runbook")
    return launch(root, load_runbook(root, "demo"), load_profile(root, None), timeout=20,
                  harnesses=harnesses, stamp="t1")


def test_runbook_parsing_reads_scope_and_subject(repo):
    root, _ = repo
    (root / "kb/tasks/demo.md").write_text(RUNBOOK.format(marker=""))
    runbook = load_runbook(root, "demo")
    assert runbook.scope == ("kb/tasks/demo-log.md",)
    assert runbook.subject == "Run recurring task demo"
    with pytest.raises(ValueError, match="no runbook"):
        load_runbook(root, "missing")


def test_clean_run_is_ok_and_leaves_other_work_alone(repo):
    root, _ = repo
    report = run_demo(repo)
    assert report.ok, report
    assert report.new_commits == 1 and report.commit_files == ["kb/tasks/demo-log.md"]
    assert report.model == "fake-model-1"
    assert report.result.startswith(f"commit: {report.commit}")
    assert "?? other.md" in git(root, "status", "--porcelain")
    assert (root / "kb/reports/state/tasks/demo/t1/calls").is_dir()


def test_stray_file_outside_scope_is_leftover(repo):
    report = run_demo(repo, " STRAY")
    assert not report.ok
    assert report.leftover == ["?? kb/tasks/stray.md"]
    assert report.scope_ok and report.new_commits == 1


def test_uncommitted_edit_is_not_a_run(repo):
    report = run_demo(repo, " UNCOMMITTED")
    assert not report.ok
    assert report.new_commits == 0 and report.commit is None
    assert report.leftover == [" M kb/tasks/demo-log.md"]


def test_two_commits_fail(repo):
    report = run_demo(repo, " TWICE")
    assert not report.ok
    assert report.new_commits == 2 and report.commit is None and report.commit_files == []


def test_wrong_subject_fails(repo):
    report = run_demo(repo, " WRONG-SUBJECT")
    assert not report.ok
    assert report.new_commits == 1 and report.scope_ok and not report.subject_ok
