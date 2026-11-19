"""Advisory capture is all-attempt, replayable and independent of acceptance."""

import json
import os
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

import pytest
from workjig import (
    CommandWorker,
    LaunchRecord,
    Request,
    RetryPolicy,
    UnresolvedSessionError,
    read_run,
)
from workjig.payloads import PayloadStore
from workjig.records import (
    CallEntry,
    Delivery,
    RunState,
    load_state,
    material_hash,
    request_material,
    stored_material,
)

from commonplace.headless.harness import HARNESSES, Harness, Profile
from commonplace.lib.agentic_analysis import audit as module
from tests.commonplace.link_helpers import symlink_or_skip

ROOT = Path(__file__).resolve().parents[3]


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


@pytest.fixture(autouse=True)
def native_store(tmp_path, monkeypatch):
    monkeypatch.setenv("PI_CODING_AGENT_SESSION_DIR", str(tmp_path / "sessions"))
    monkeypatch.setenv("CLAUDE_CONFIG_DIR", str(tmp_path / "claude"))


def write_trace(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(record) for record in records) + "\n")


def add_call(run_dir, job, statuses, *, harness="pi", protocol="pi-json", tracked=True):
    """Record one call with a launch per status, built from Workjig's record types.

    No worker runs. Workjig serializes the record, so it is one `read_run` accepts.
    """
    path = run_dir / "calls/run.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    store = PayloadStore(path.parent)
    state = load_state(path, store) or RunState(workdir=str(run_dir))
    request = Request(job, "Original assignment", {}, ("report.md",),
                      CommandWorker(("worker",), name=harness, output_protocol=protocol,
                                    track_native_session=tracked and harness in ("pi", "claude-code")))
    retry = RetryPolicy(tuple(dict.fromkeys(status for status in statuses if status != "delivered")))
    launches = []
    locations = []
    for status in statuses:
        uid = uuid4()
        directory = run_dir / "calls/launches" / uid.hex
        directory.mkdir(parents=True)
        identifier = str(uid)
        base = Path(os.environ["PI_CODING_AGENT_SESSION_DIR"])
        if harness == "pi":
            path_native = base / f"workjig-{identifier}" / f"time_{identifier}.jsonl"
            write_trace(path_native, [
                {"type": "session", "id": identifier},
                {"type": "message", "id": "a", "message": {"role": "assistant", "content": [
                    {"type": "toolCall", "id": "t", "arguments": {"command": "false"}}]}},
                {"type": "message", "parentId": "a", "message": {"role": "toolResult", "toolCallId": "t",
                 "toolName": "bash", "isError": True, "content": [{"type": "text", "text": "Command exited with code 1"}]}}])
        else:
            base = Path(os.environ["CLAUDE_CONFIG_DIR"]) / "projects"
            path_native = base / "fixture" / f"{identifier}.jsonl"
        write_json(directory / "native-session.json", {"launch": uid.hex, "harness": "pi" if harness == "pi" else "claude",
                   "id": identifier, "location": str(path_native.parent if harness == "pi" else path_native)})
        locations.append((directory, path_native, identifier))
        (directory / "prompt.txt").write_text("Original assignment")
        launches.append(LaunchRecord(directory.name, status, str(directory), ("worker",), pid=1,
                                     returncode=0 if status == "delivered" else 1,
                                     started_at="2026-01-01T00:00:00+00:00", finished_at="2026-01-01T00:00:01+00:00",
                                     max_launches=len(statuses), retry=retry, native_session_root=str(base) if request.worker.track_native_session else None))
    outputs = {"report.md": "Report"}
    delivery = Delivery.store(outputs, launches[-1].launch_id, store) if statuses[-1] == "delivered" else None
    key = material_hash(request_material(request))
    state.calls[job] = {key: CallEntry(request, key, stored_material(request, store), launches, delivery)}
    write_json(path, state.to_json())
    return locations


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
                                               timeout=10800, harnesses=HARNESSES, log=lambda **kw: None))


def answer(directory, calls=2, stop="stop", terminal=True):
    [(_, path, identifier)] = add_call(directory, "advisory-audit", ["delivered" if terminal else "process_error"])
    msg = {"type": "message", "message": {"role": "assistant", "content": [
        {"type": "toolCall", "id": str(i), "arguments": {}} for i in range(calls)]}}
    write_trace(path, [{"type": "session", "id": identifier}, msg, {"type": "message", "message": {
        "role": "assistant", "model": "test-model", "stopReason": stop, "content": []}}])


def test_collect_all_attempts_and_missing_unsupported(analysis):
    root = analysis.run_dir
    attempts = add_call(root, "old-memory", ["timeout", "delivered"])
    add_call(root, "codex-job", ["delivered"], harness="codex", protocol="codex-json")
    attempts[0][1].unlink()
    inventory, scanner = module.collect(root)
    assert len(inventory) == scanner["details"]["attempt_count"] == 5
    assert scanner["finding_count"] == 3
    assert scanner["details"]["unscanned_attempt_count"] == 2
    assert scanner["details"]["partial_attempt_count"] == 0
    assert len(scanner["traces"]) == 3
    assert {i["status"] for i in inventory} == {"timeout", "process_error", "delivered"}
    assert next(i for i in inventory if i["job"] == "codex-job")["reason"] == "unsupported harness/protocol"


def test_session_only_its_harness_can_locate_is_a_coverage_gap(tmp_path):
    """Workjig raises for a tracked Codex launch unless asked to start `codex`; the audit never asks."""
    prompt = tmp_path.resolve() / "prompt.txt"
    prompt.write_text("Original assignment")

    def unresolved(launch):
        raise UnresolvedSessionError("codex", "0196f0aa-0000-7000-8000-000000000000")

    view = SimpleNamespace(launch_files=lambda launch: SimpleNamespace(prompt=prompt), native_session=unresolved)
    call = SimpleNamespace(call_id="codex-job", request_hash="key", worker=SimpleNamespace(name="codex"))
    launch = SimpleNamespace(launch_id="launch", status=SimpleNamespace(value="delivered"))
    item, report = module.attempt_session(view, call, launch)
    assert report is None and item["scan_status"] == "unscanned"
    assert "resolve=True" in item["reason"]


def test_untracked_legacy_attempt_never_uses_stdout(analysis):
    [(directory, _, _)] = add_call(analysis.run_dir, "legacy", ["delivered"], tracked=False)
    (directory / "stdout.log").write_text('{"type":"session","id":"not-evidence"}\n')
    inventory, _ = module.collect(analysis.run_dir)
    item = next(i for i in inventory if i["job"] == "legacy")
    assert (item["session_status"], item["scan_status"]) == ("unassociated", "unscanned")
    assert "trace" not in item


def test_collect_scans_claude_native_session(analysis):
    root = analysis.run_dir
    [(_, path, identifier)] = add_call(root, "claude-job", ["delivered"], harness="claude-code", protocol="claude-stream-json")
    write_trace(path, [{"type": "assistant", "uuid": "a", "sessionId": identifier, "message": {"role": "assistant", "content": [
        {"type": "tool_use", "id": "toolu_1", "name": "Bash", "input": {"command": "false"}}]}},
        {"type": "user", "uuid": "u", "sessionId": identifier, "message": {"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": "toolu_1", "content": "Exit code 1\n", "is_error": True}]}}])
    inventory, scanner = module.collect(root)
    item = next(i for i in inventory if i["job"] == "claude-job")
    assert (item["scan_status"], item["harness"], item["reason"]) == ("scanned", "claude-code", None)
    [report] = [t for t in scanner["traces"] if t["harness"] == "claude-code"]
    assert [(f["tool_name"], f["command"], f["evidence"][0]["exit_code"]) for f in report["findings"]] == [("Bash", "false", 1)]
    assert scanner["finding_count"] == 3  # two Pi attempts in the fixture call, one Claude attempt
    # The mixed-harness audit is a consumer of the same contract as the CLIs.
    from jsonschema import Draft202012Validator

    schema = json.loads((ROOT / "scripts/scan_tools/result.schema.json").read_text())
    Draft202012Validator(schema).validate(scanner)
    assert scanner["schema_version"] == 2
    assert all(t["coverage"]["checks"]["recovery"] == "unsupported" for t in scanner["traces"])


def test_all_unscanned_attempts_report_no_failure_count(analysis, monkeypatch):
    shutil.rmtree(analysis.run_dir / "calls")
    add_call(analysis.run_dir, "runtime", ["process_error", "delivered"], harness="codex", protocol="codex-json")
    analysis.run.profile.harness = "codex"
    monkeypatch.setattr(module, "launch", lambda *args: pytest.fail("must not launch"))
    coverage = module.audit(analysis, completed=True)["trace-scan"]
    assert coverage["attempt_count"] == coverage["unscanned_attempt_count"] == 2
    assert coverage["finding_count"] is None


def test_collect_does_not_follow_redirected_traces(analysis):
    stdout = Path(module.collect(analysis.run_dir)[0][0]["trace"])
    outside = analysis.worktree / "personal-session.jsonl"
    stdout.rename(outside)
    symlink_or_skip(stdout, outside)
    inventory, scanner = module.collect(analysis.run_dir)
    assert inventory[0]["scan_status"] == "unscanned"
    assert inventory[0]["reason"] == "missing or redirected native transcript"
    assert "stdout_sha256" not in inventory[0]
    assert scanner["finding_count"] == 1 and len(scanner["traces"]) == 1


@pytest.mark.parametrize("change,reason", [
    ("replace", "hash mismatch"), ("foreign", "identity mismatch"), ("delete", "missing"),
])
def test_changed_session_never_substitutes_for_pinned_attempt(analysis, change, reason):
    first = module.audit(analysis, completed=False)
    snapshot = Path(first["directory"]) / "attempts.json"
    original = snapshot.read_bytes()
    item = json.loads(original)[0]
    trace = Path(item["trace"])
    if change == "delete":
        trace.unlink()
    elif change == "foreign":
        trace.write_text(trace.read_text().replace(item["session_id"], str(uuid4())))
    else:
        with trace.open("a") as stream:
            stream.write('{"type":"label"}\n')
    second = module.audit(analysis, completed=False)
    assert second["snapshot"] != first["snapshot"]
    updated = json.loads((Path(second["directory"]) / "attempts.json").read_text())[0]
    assert updated["scan_status"] == "unscanned" and reason in updated["reason"]
    assert "trace" not in updated  # not an authorized model input
    assert snapshot.read_bytes() == original


def test_capture_precedes_worker_and_reuses_then_invalidates(analysis, monkeypatch):
    invocations = []

    def launch(directory, worktree, profile, harness, timeout, roots, session_files):
        assert all(Path(path).parent not in roots for path in session_files)
        invocations.append(directory)
        assert timeout == 900
        scanner = json.loads((directory / "scanner.json").read_text())
        assert scanner["finding_count"] == 2
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
    # Expired auditor evidence neither triggers a new model nor rewrites the old verdict.
    Path(first["auditor"]["trace"]).unlink()
    replay = module.audit(analysis, completed=True)
    assert "missing" in replay["auditor-evidence"] and len(invocations) == 1
    assert json.loads((directory / "status.json").read_text()) == first
    (analysis.run.artifact / "synthesis.md").write_text("Changed accepted synthesis\n")
    second = module.audit(analysis, completed=True)
    assert second["snapshot"] != first["snapshot"]
    assert len(invocations) == 2
    assert (directory / "report.md").read_text() == "No material defect established.\n"
    assert json.loads((analysis.run_dir / "audit/status.json").read_text()) == second


@pytest.mark.parametrize("completed,harness,reason", [
    (False, "pi", "analysis did not complete"), (False, "claude-code", "analysis did not complete"),
    (True, "codex", "no advisory auditor for harness codex"),
])
def test_scan_saved_even_when_meta_analysis_skipped(analysis, monkeypatch, completed, harness, reason):
    analysis.run.profile.harness = harness
    monkeypatch.setattr(module, "launch", lambda *args: pytest.fail("must not launch"))
    status = module.audit(analysis, completed=completed)
    assert (status["state"], status["reason"]) == ("skipped", reason)
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


def test_truncated_native_auditor_budget_fails_closed(tmp_path):
    answer(tmp_path, calls=31)
    (item,), _ = module.collect(tmp_path)
    path = Path(item["trace"])
    path.write_bytes(b"\n".join(path.read_bytes().splitlines()[:-1]))
    assert module.result(tmp_path, "Report")["state"] == "failed"
    assert not (tmp_path / "report.md").exists()


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
    event = json.loads((Path(metrics["launch_dir"]) / "stdout.log").read_text())
    argv = event["argv"]
    assert "Exact commissioned task" in event["frame"]
    [call] = read_run(tmp_path / "calls").calls
    assert call.call_id == "advisory-audit"
    assert [launch.status for launch in call.launches] == ["delivered"]
    assert "--no-context-files" in argv and "--no-session" not in argv
    assert "--no-extensions" in argv and "--no-skills" in argv and "--no-mcp" in argv
    assert argv[argv.index("--system-prompt") + 1] == module.SYSTEM_PROMPT
    assert argv[argv.index("--append-system-prompt") + 1] == module.APPEND_SYSTEM_PROMPT
    assert argv[argv.index("--tools") + 1] == "read,bash"
    assert not any(arg.startswith("--tools=") for arg in argv)
    assert "--approve" not in argv and "not-allowed" not in argv
    assert str(Path(metrics["launch_dir"]) / "prompt.txt") in argv[-1]


@pytest.mark.parametrize("workjig_status,state", [
    ("incomplete", "failed"), ("process_error", "failed"), ("timeout", "timeout"),
])
def test_workjig_failures_remain_advisory_without_relaunch(analysis, monkeypatch, workjig_status, state):
    invocations = []

    def launch(*args):
        invocations.append(args)
        return {"workjig_status": workjig_status, "returncode": None}, ""

    monkeypatch.setattr(module, "launch", launch)
    module.advisory_audit(analysis, completed=True)
    status = json.loads((analysis.run_dir / "audit/status.json").read_text())
    assert status["state"] == state and status["workjig_status"] == workjig_status
    assert not (Path(status["directory"]) / "report.md").exists()
    assert module.audit(analysis, completed=True) == status
    assert len(invocations) == 1
    assert (analysis.run.artifact / "synthesis.md").read_text() == "Accepted synthesis\n"


def claude_answer(directory, calls=2):
    [(_, path, identifier)] = add_call(directory, "advisory-audit", ["delivered"], harness="claude-code",
                                       protocol="claude-stream-json")
    def assistant(content):
        return {"type": "assistant", "sessionId": identifier,
                "message": {"role": "assistant", "model": "claude-test-1", "content": content}}
    write_trace(path, [assistant([{"type": "tool_use", "id": str(i), "name": "Read", "input": {}}])
                       for i in range(calls)] + [assistant([{"type": "text", "text": "Report saved"}])])


@pytest.mark.parametrize("calls,report,state", [(30, "Report", "complete"), (31, "Report", "budget-exceeded"),
                                               (1, "  ", "failed")])
def test_claude_budget_and_report(tmp_path, calls, report, state):
    claude_answer(tmp_path, calls=calls)
    assert module.result(tmp_path, report)["state"] == state


def test_launch_uses_run_profile_harness(analysis, monkeypatch):
    analysis.run.profile = Profile("claude-code", "sonnet", "medium", {"permission-mode": "acceptEdits"})
    harnesses = {"pi": SimpleNamespace(protocol="pi-json"),
                 "claude-code": SimpleNamespace(protocol="claude-stream-json")}
    analysis.run.harnesses = harnesses
    received = []

    def launch(directory, worktree, profile, harness, timeout, roots, session_files):
        received.append((profile, harness, roots))
        claude_answer(directory)
        return {"returncode": 0, "workjig_status": "delivered"}, "No material defect established."

    monkeypatch.setattr(module, "launch", launch)
    status = module.audit(analysis, completed=True)
    [(profile, harness, roots)] = received
    assert harness is harnesses["claude-code"] and profile is analysis.run.profile
    assert analysis.run.artifact.resolve() in roots
    assert status["state"] == "complete" and status["model"] == "claude-test-1"


def test_launch_claude_code_auditor_flags(tmp_path):
    script = tmp_path / "fake.py"
    script.write_text(
        "import json,sys,pathlib\n"
        "prompt = pathlib.Path(sys.argv[-1].split('`')[1])\n"
        "frame = prompt.read_text()\n"
        "output = pathlib.Path(frame.split('- report.md: ')[1].splitlines()[0])\n"
        "output.write_text('Audit report')\n"
        "prompt.with_name('argv.json').write_text(json.dumps(sys.argv[1:]))\n"
        "print(json.dumps({'type': 'result', 'subtype': 'success', 'is_error': False}))\n")
    (tmp_path / "prompt.txt").write_text("Exact commissioned task")
    worktree = tmp_path / "worktree"
    worktree.mkdir()
    outside = tmp_path / "source"
    defaults = {**HARNESSES["claude-code"].defaults, "_subcommand": str(script)}
    harness = Harness(sys.executable, defaults, HARNESSES["claude-code"].translate, "claude-stream-json")
    profile = Profile("claude-code", "sonnet", "high", {"permission-mode": "bypassPermissions", "extra": "no"})
    trace = str(tmp_path / "native/session.jsonl")
    metrics, report = module.launch(tmp_path, worktree, profile, harness, 10, [outside, worktree / "kb", outside], [trace])
    assert metrics["workjig_status"] == "delivered" and report == "Audit report"
    argv = json.loads((Path(metrics["launch_dir"]) / "argv.json").read_text())
    assert "--session-id" in argv
    assert argv[argv.index("--model") + 1] == "sonnet" and argv[argv.index("--effort") + 1] == "high"
    assert argv[argv.index("--permission-mode") + 1] == "acceptEdits"
    assert "bypassPermissions" not in argv and "--extra" not in argv
    assert [a for a in argv if a.startswith("--tools=")] == [
        "--tools=Read", "--tools=Grep", "--tools=Glob", "--tools=Bash", "--tools=Write"]
    assert "--tools" not in argv and "read,bash" not in argv
    assert [a for a in argv if a.startswith("--add-dir")] == [f"--add-dir={outside.resolve()}"]
    assert f"--allowedTools=Read(/{trace})" in argv
    assert "--no-session-persistence" not in argv and "--strict-mcp-config" in argv
    assert argv[argv.index("--system-prompt") + 1] == module.SYSTEM_PROMPT
    assert argv[argv.index("--append-system-prompt") + 1] == module.APPEND_SYSTEM_PROMPT
