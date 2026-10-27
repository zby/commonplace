"""Advisory capture is all-attempt, replayable and independent of acceptance."""

import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from commonplace.headless.harness import Harness, Profile
from commonplace.lib.agentic_analysis import audit as module
from tests.commonplace.link_helpers import symlink_or_skip

ROOT = Path(__file__).resolve().parents[3]


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def trace(path, failed=True):
    events = [{"type": "session", "id": "s"},
              {"type": "tool_execution_start", "toolCallId": "t", "args": {"command": "false"}},
              {"type": "tool_execution_end", "toolCallId": "t", "toolName": "bash", "isError": failed,
               "result": {"content": [{"type": "text", "text": "Command exited with code 1"}]}}]
    path.write_text("\n".join(json.dumps(e) for e in events) + "\n")


def add_call(run_dir, job, statuses, *, harness="pi", protocol="pi-json"):
    path = run_dir / "calls/run.json"
    data = json.loads(path.read_text()) if path.exists() else {"calls": {}}
    attempts = []
    for index, status in enumerate(statuses):
        directory = run_dir / "calls/launches" / f"{job}-{index}"
        directory.mkdir(parents=True)
        trace(directory / "stdout.log")
        (directory / "prompt.txt").write_text("Original assignment")
        attempts.append({"launch_dir": str(directory), "launch_id": directory.name, "status": status})
    data["calls"][job] = {"key": {"request": {"worker": {"name": harness, "output_protocol": protocol}},
                                  "attempts": attempts}}
    write_json(path, data)


@pytest.fixture
def analysis(tmp_path):
    run_dir = tmp_path / "run"
    artifact = run_dir / "artifact"
    artifact.mkdir(parents=True)
    (artifact / "boundary.md").write_text("---\nsource: null\n---\nBoundary\n")
    (artifact / "synthesis.md").write_text("Accepted synthesis\n")
    write_json(run_dir / "receipt.json", {"published": True})
    write_json(run_dir / "code/opening.json", {"inputs-commit": "a" * 40})
    write_json(run_dir / "code/acquire.json", {"path": str(tmp_path / "source"), "revision": "b" * 40})
    library = tmp_path / "kb"
    target = library / module.INSTRUCTION
    target.parent.mkdir(parents=True)
    target.write_text((ROOT / "kb" / module.INSTRUCTION).read_text())
    add_call(run_dir, "runtime", ["process_error", "delivered"])
    return SimpleNamespace(run_dir=run_dir, worktree=tmp_path, library=library,
                           method=SimpleNamespace(frozen="boundary"),
                           layout=SimpleNamespace(path=lambda role: role + ".md"),
                           run=SimpleNamespace(artifact=artifact, profile=Profile("pi", "test-model", "medium"),
                                               timeout=10800, harnesses={"pi": None}, log=lambda **kw: None))


def answer(directory, text="No material defect established.", calls=2, stop="stop", terminal=True):
    events = [{"type": "tool_execution_start"} for _ in range(calls)]
    events.append({"type": "message_end", "message": {"role": "assistant", "model": "test-model",
                   "stopReason": stop, "content": [{"type": "text", "text": text}]}})
    if terminal:
        events.append({"type": "agent_end"})
    (directory / "stdout.log").write_text("\n".join(json.dumps(e) for e in events))


def test_collect_all_attempts_and_missing_unsupported(analysis):
    root = analysis.run_dir
    add_call(root, "old-memory", ["timeout", "delivered"])
    add_call(root, "codex-job", ["delivered"], harness="codex", protocol="codex-json")
    (root / "calls/launches/old-memory-0/stdout.log").unlink()
    inventory, scanner = module.collect(root)
    assert len(inventory) == scanner["attempt_count"] == 5
    assert scanner["failure_count"] == 3
    assert scanner["unscanned_attempt_count"] == scanner["partial_attempt_count"] == 1
    assert len(scanner["traces"]) == 4
    assert any(t["scan_issues"] for t in scanner["traces"])
    assert {i["status"] for i in inventory} == {"timeout", "process_error", "delivered"}
    assert next(i for i in inventory if i["job"] == "codex-job")["reason"] == "unsupported harness/protocol"


def test_collect_does_not_follow_redirected_traces(analysis):
    stdout = analysis.run_dir / "calls/launches/runtime-0/stdout.log"
    outside = analysis.worktree / "personal-session.jsonl"
    stdout.rename(outside)
    symlink_or_skip(stdout, outside)
    inventory, scanner = module.collect(analysis.run_dir)
    assert inventory[0]["scan_status"] == "unscanned"
    assert inventory[0]["reason"] == "trace outside run launch tree"
    assert "stdout_sha256" not in inventory[0]
    assert scanner["failure_count"] == 1 and len(scanner["traces"]) == 1


def test_capture_precedes_worker_and_reuses_then_invalidates(analysis, monkeypatch):
    invocations = []

    def launch(directory, worktree, profile, harness, timeout):
        invocations.append(directory)
        assert timeout == 900
        scanner = json.loads((directory / "scanner.json").read_text())
        assert scanner["failure_count"] == 2
        prompt = (directory / "prompt.txt").read_text()
        assert str(directory / "scanner.json") in prompt
        assert str(directory / "attempts.json") in prompt
        assert "at most three" in prompt and "30 tool calls" in prompt
        assert "Existing audits, other runs and personal sessions" in prompt
        answer(directory)
        return {"returncode": 0}

    monkeypatch.setattr(module, "launch", launch)
    first = module.audit(analysis, completed=True)
    assert first["state"] == "complete" and first["tool_calls"] == 2
    directory = Path(first["directory"])
    assert (directory / "report.md").read_text() == "No material defect established.\n"
    assert first["method-commit"] == "a" * 40 and first["source-revision"] == "b" * 40
    assert module.audit(analysis, completed=True) == first
    assert len(invocations) == 1
    (analysis.run.artifact / "synthesis.md").write_text("Changed accepted synthesis\n")
    second = module.audit(analysis, completed=True)
    assert second["snapshot"] != first["snapshot"]
    assert len(invocations) == 2
    assert (directory / "report.md").read_text() == "No material defect established.\n"
    assert json.loads((analysis.run_dir / "audit/status.json").read_text()) == second


@pytest.mark.parametrize("completed,harness", [(False, "pi"), (True, "codex")])
def test_scan_saved_even_when_meta_analysis_skipped(analysis, monkeypatch, completed, harness):
    analysis.run.profile.harness = harness
    monkeypatch.setattr(module, "launch", lambda *args: pytest.fail("must not launch"))
    status = module.audit(analysis, completed=completed)
    assert status["state"] == "skipped"
    assert (Path(status["directory"]) / "scanner.json").is_file()


@pytest.mark.parametrize("failure,state", [(OSError("missing pi"), "failed"),
                                           (subprocess.TimeoutExpired("pi", 900), "timeout")])
def test_audit_failure_saved_without_retry(analysis, monkeypatch, failure, state):
    attempts = []

    def launch(*args):
        attempts.append(1)
        raise failure

    monkeypatch.setattr(module, "launch", launch)
    status = module.audit(analysis, completed=True)
    assert status["state"] == state
    assert module.audit(analysis, completed=True) == status
    assert len(attempts) == 1
    assert (Path(status["directory"]) / "scanner.json").is_file()


def test_abandoned_snapshot_is_interrupted_not_relaunched(analysis, monkeypatch):
    def interrupted(*args):
        raise KeyboardInterrupt

    monkeypatch.setattr(module, "launch", interrupted)
    with pytest.raises(KeyboardInterrupt):
        module.audit(analysis, completed=True)
    status = module.audit(analysis, completed=True)
    assert status["state"] == "interrupted"


def test_capture_failure_cannot_fail_analysis(analysis, monkeypatch, capsys):
    monkeypatch.setattr(module, "collect", lambda root: (_ for _ in ()).throw(ValueError("bad manifest")))
    module.advisory_audit(analysis, completed=True)
    status = json.loads((analysis.run_dir / "audit/status.json").read_text())
    assert status["state"] == "failed" and "bad manifest" in status["reason"]
    assert "advisory audit: failed" in capsys.readouterr().err


@pytest.mark.parametrize("stop,terminal,calls,state", [("stop", True, 30, "complete"),
                                                      ("stop", True, 31, "budget-exceeded"),
                                                      ("error", True, 1, "failed"),
                                                      ("stop", False, 1, "failed")])
def test_result_requires_successful_terminal_answer(tmp_path, stop, terminal, calls, state):
    answer(tmp_path, calls=calls, stop=stop, terminal=terminal)
    assert module.result(tmp_path)["state"] == state
    assert (tmp_path / "report.md").exists() == (stop == "stop" and terminal)


def test_launch_strips_profile_flags_and_passes_exact_prompt(tmp_path):
    script = tmp_path / "fake.py"
    script.write_text("import json,sys\nprint(json.dumps({'argv': sys.argv[1:]}))\n")
    (tmp_path / "prompt.txt").write_text("Exact commissioned task")
    harness = Harness(sys.executable, {"_subcommand": str(script), "print": True, "mode": "json"},
                      lambda profile: {"model": profile.launch_model, "thinking": profile.effort})
    profile = Profile("pi", "test-model", "medium", {"approve": True, "extension": "not-allowed"})
    metrics = module.launch(tmp_path, tmp_path, profile, harness, 3)
    assert metrics["returncode"] == 0
    argv = json.loads((tmp_path / "stdout.log").read_text())["argv"]
    assert "--no-context-files" in argv and "--no-session" in argv
    assert "--no-extensions" in argv and "--no-skills" in argv and "--no-mcp" in argv
    assert argv[argv.index("--system-prompt") + 1] == module.FLAGS["system-prompt"]
    assert argv[argv.index("--append-system-prompt") + 1] == module.FLAGS["append-system-prompt"]
    assert argv[argv.index("--tools") + 1] == "read,bash"
    assert not any(arg.startswith("--tools=") for arg in argv)
    assert "--approve" not in argv and "not-allowed" not in argv
    assert str(tmp_path / "prompt.txt") in argv[-1]


def test_timeout_terminates_audit_process(tmp_path):
    script = tmp_path / "sleep.py"
    script.write_text("import time\ntime.sleep(60)\n")
    harness = Harness(sys.executable, {"_subcommand": str(script)}, lambda p: {})
    with pytest.raises(subprocess.TimeoutExpired):
        module.launch(tmp_path, tmp_path, Profile("pi", "test", "medium"), harness, 0.05)
    assert (tmp_path / "stdout.log").is_file() and (tmp_path / "stderr.log").is_file()
