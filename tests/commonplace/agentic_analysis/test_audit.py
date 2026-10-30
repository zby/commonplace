"""Advisory capture is all-attempt, replayable and independent of acceptance."""

import json
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
        events.append({"type": "agent_settled", "aborted": False})
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
        return {"returncode": 0, "workjig_status": "delivered"}, "No material defect established."

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


@pytest.mark.parametrize("failure,state", [(OSError("missing pi"), "failed")])
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
    assert module.result(tmp_path, "No material defect established.")["state"] == state
    assert (tmp_path / "report.md").exists() == (stop == "stop" and terminal)


def test_launch_strips_profile_flags_and_passes_exact_prompt(tmp_path):
    script = tmp_path / "fake.py"
    script.write_text(
        "import json,sys,pathlib\n"
        "prompt = pathlib.Path(sys.argv[-1].split('`')[1])\n"
        "frame = prompt.read_text()\n"
        "output = pathlib.Path(frame.split('- report.md: ')[1].splitlines()[0])\n"
        "output.write_text('Audit report')\n"
        "print(json.dumps({'argv': sys.argv[1:], 'frame': frame}))\n")
    (tmp_path / "prompt.txt").write_text("Exact commissioned task")
    harness = Harness(sys.executable, {"_subcommand": str(script), "print": True, "mode": "json"},
                      lambda profile: {"model": profile.launch_model, "thinking": profile.effort})
    profile = Profile("pi", "test-model", "medium", {"approve": True, "extension": "not-allowed"})
    metrics, report = module.launch(tmp_path, tmp_path, profile, harness, 3)
    assert metrics["returncode"] == 0 and metrics["workjig_status"] == "delivered"
    assert report == "Audit report"
    event = json.loads((tmp_path / "stdout.log").read_text())
    argv = event["argv"]
    assert "Exact commissioned task" in event["frame"]
    records = json.loads((tmp_path / "calls/run.json").read_text())
    attempts = next(iter(records["calls"]["advisory-audit"].values()))["attempts"]
    assert len(attempts) == 1
    assert attempts[0]["status"] == "delivered"
    assert "--no-context-files" in argv and "--no-session" in argv
    assert "--no-extensions" in argv and "--no-skills" in argv and "--no-mcp" in argv
    assert argv[argv.index("--system-prompt") + 1] == module.FLAGS["system-prompt"]
    assert argv[argv.index("--append-system-prompt") + 1] == module.FLAGS["append-system-prompt"]
    assert argv[argv.index("--tools") + 1] == "read,bash"
    assert not any(arg.startswith("--tools=") for arg in argv)
    assert "--approve" not in argv and "not-allowed" not in argv
    assert str(Path(metrics["launch_dir"]) / "prompt.txt") in argv[-1]


def test_timeout_terminates_audit_process(tmp_path):
    script = tmp_path / "sleep.py"
    script.write_text("import time\ntime.sleep(60)\n")
    harness = Harness(sys.executable, {"_subcommand": str(script)}, lambda p: {})
    (tmp_path / "prompt.txt").write_text("Audit within budget")
    metrics, report = module.launch(tmp_path, tmp_path, Profile("pi", "test", "medium"), harness, 0.05)
    assert metrics["workjig_status"] == "timeout" and not report
    assert metrics["returncode"] != 0
    assert (tmp_path / "stdout.log").is_file() and (tmp_path / "stderr.log").is_file()


@pytest.mark.parametrize("behavior,state,workjig_status", [
    ("delivered", "complete", "delivered"),
    ("missing", "failed", "incomplete"),
    ("exit", "failed", "process_error"),
    ("timeout", "timeout", "timeout"),
    ("child", "failed", "process_error"),
])
def test_workjig_audit_outcomes_are_advisory_and_not_relaunched(
        analysis, behavior, state, workjig_status):
    script = analysis.worktree / "auditor.py"
    script.write_text(
        "import json,pathlib,subprocess,sys,time\n"
        f"behavior = {behavior!r}\n"
        "if behavior == 'timeout': time.sleep(60)\n"
        "if behavior == 'exit': sys.exit(1)\n"
        "if behavior == 'child':\n"
        "    subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\n"
        "frame = pathlib.Path(sys.argv[-1].split('`')[1]).read_text()\n"
        "output = pathlib.Path(frame.split('- report.md: ')[1].splitlines()[0])\n"
        "if behavior != 'missing': output.write_text('File report, not terminal acknowledgement')\n"
        "print(json.dumps({'type': 'message_end', 'message': {'role': 'assistant',\n"
        "    'stopReason': 'stop', 'content': [{'type': 'text', 'text': 'Done'}]}}))\n"
        "print(json.dumps({'type': 'agent_settled', 'aborted': False}))\n")
    analysis.run.harnesses["pi"] = Harness(
        sys.executable, {"_subcommand": str(script)}, lambda p: {}, protocol="pi-json")
    analysis.run.timeout = 0.05 if behavior == "timeout" else 3
    module.advisory_audit(analysis, completed=True)
    status = json.loads((analysis.run_dir / "audit/status.json").read_text())
    assert status["state"] == state
    assert status["workjig_status"] == workjig_status
    directory = Path(status["directory"])
    records = json.loads((directory / "calls/run.json").read_text())
    attempts = next(iter(records["calls"]["advisory-audit"].values()))["attempts"]
    assert len(attempts) == 1
    assert attempts[0]["status"] == workjig_status
    if behavior == "delivered":
        assert (directory / "report.md").read_text() == "File report, not terminal acknowledgement\n"
    else:
        assert not (directory / "report.md").exists()
    assert module.audit(analysis, completed=True) == status
    assert len(module.collect(analysis.run_dir)[0]) == 2  # Audit records are not production attempts.
    assert (analysis.run.artifact / "synthesis.md").read_text() == "Accepted synthesis\n"


def test_unconfirmed_cleanup_remains_unresolved_without_automatic_retry(analysis, monkeypatch):
    import workjig.harness
    from workjig.platform import OwnershipError

    original = workjig.harness._cleanup_group

    def uncertain(process):
        original(process)
        raise OwnershipError("termination unconfirmed")

    monkeypatch.setattr(workjig.harness, "_cleanup_group", uncertain)
    analysis.run.harnesses["pi"] = Harness(sys.executable, {"_subcommand": ["-c", "pass"]}, lambda p: {})
    status = module.audit(analysis, completed=True)
    assert status["state"] == "failed" and "OwnershipError" in status["reason"]
    records = json.loads((Path(status["directory"]) / "calls/run.json").read_text())
    attempts = next(iter(records["calls"]["advisory-audit"].values()))["attempts"]
    assert len(attempts) == 1 and attempts[0]["status"] == "running"
    assert module.audit(analysis, completed=True) == status
