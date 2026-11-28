"""Read-mode command trial: real Workjig calls with no model or network."""

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli import sub_worker
from commonplace.headless.harness import Harness, Profile


# The fake executable receives a pointer to Workjig's prompt, just like a harness.
def worker(pointer):
    frame = Path(re.search(r"`([^`]+prompt\.txt)`", pointer)[1]).read_text()
    action = Path(re.search(r"^- brief.md: (.+)$", frame, re.MULTILINE)[1]).read_text()
    if "edit" in action:
        Path("draft").write_text("unexpected")
    if "fail" in action:
        return 0  # incomplete output is a counted failure; no environment retry
    if action in {"problem", "limit"}:
        path = frame.split("write a JSON object to this problem file:\n")[1].splitlines()[0]
        kind = "usage_limit" if action == "limit" else "unable"
        Path(path).write_text(json.dumps({"kind": kind, "message": "blocked"}))
        return int(action == "limit")
    Path(re.search(r"^- answer.md: (.+)$", frame, re.MULTILINE)[1]).write_text("a finding")
    return 0


@pytest.mark.parametrize(("action", "status"), [("read", "answered"), ("edit", "checkout-changed"),
                         ("edit-fail", "checkout-changed"), ("fail", "launch-failed"), ("problem", "problem"),
                         ("limit", "usage-limit")])
def test_guard_and_results(tmp_path, action, status):
    def git(*args):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)

    git("init", "-q")
    draft = tmp_path / "draft"
    draft.write_text("initial")
    git("add", "draft")
    git("-c", "user.name=test", "-c", "user.email=test@example.org", "commit", "-qm", "seed")
    draft.write_text("already dirty")
    fake = Harness(sys.executable, {"_subcommand": [__file__]}, lambda _: {}, model_used=lambda _: "fake")
    report = sub_worker.launch(tmp_path, action, Profile("fake", "m", "low"), 20, harnesses={"fake": fake})
    assert report["status"] == status, report
    assert (tmp_path / report["run_dir"] / "calls").is_dir()
    if "edit" in action:
        assert report["changes"] == ["draft"] and "answer" not in report
        assert draft.read_text() == "unexpected"
        assert report["worker_status"] == ("launch-failed" if action == "edit-fail" else "answered")
    if status == "answered":
        assert (report["answer"], report["model"]) == ("a finding", "fake")


def test_setup_error_does_not_launch(tmp_path, capsys):
    assert sub_worker.main(["run", "--profile", "missing", "--brief", str(tmp_path / "missing")]) == 2
    assert json.loads(capsys.readouterr().out)["status"] == "setup-error"


if __name__ == "__main__":
    sys.exit(worker(sys.argv[-1]))
