"""Coordinator consumers: real prepared subprocesses plus bounded scheduler fixtures.

The complete route substitutes only installation (a local command environment
using the test interpreter's dependencies), model execution (a PATH executable)
and remote Git transport (Git's insteadOf to a test-local repository). Package,
startup, source, member, publication and replay guards are real.
"""

from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import sys
import tarfile
import threading
import time
from pathlib import Path

import pytest

from commonplace.cli.analysis import main
from commonplace.lib.agentic_analysis import automation as auto
from commonplace.lib.agentic_analysis import preparation
from commonplace.lib.agentic_analysis.durable import lease, save
from commonplace.lib.agentic_analysis.execution import outcome
from commonplace.lib.agentic_analysis.worktree import (
    STATE_ROOT,
    allocation_path,
    start_analysis,
)
from tests.commonplace.agentic_analysis.execution_fixtures import IDENTITY, ROOT, git
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as bound_checkout,  # noqa: F401 - binding fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - immutable baseline registration
)
from tests.commonplace.agentic_analysis.test_workflow import (
    FAKE,
    REFUSE_RUNTIME_AND_MEMORY,
)

PRODUCTION_INSTALL = preparation._install


@pytest.fixture
def command_origin(tmp_path, prepared_template, monkeypatch):
    origin = tmp_path / "origin"
    shutil.copytree(prepared_template.repo, origin)
    shutil.rmtree(origin / "src")
    shutil.copytree(ROOT / "src", origin / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for name in ("pyproject.toml", "uv.lock"):
        shutil.copy2(ROOT / name, origin / name)
    (origin / "AGENTS.md").write_text("Fixture method. Never call a provider.\n")
    (origin / ".gitignore").write_text(".venv/\n__pycache__/\n.commonplace/\nrelated-systems/\nkb/agentic-system-analyses/state/\n")
    git(origin, "add", "src", "pyproject.toml", "uv.lock", "AGENTS.md", ".gitignore")
    git(origin, "commit", "--quiet", "-m", "Pin executable fixture method")
    git(origin, "branch", "-M", "main")
    monkeypatch.chdir(origin)
    # Keep dependency reuse immutable. Every checkout receives its own commands
    # and path file, and imports its own committed src, not this checkout's code.
    def install(tree):
        commands = tree / ".venv/bin"
        commands.mkdir(parents=True)
        for name, module in (("commonplace-analysis", "commonplace.cli.analysis"),
                             ("commonplace-validate", "commonplace.cli.validate_notes")):
            script = commands / name
            script.write_text(f"#!{sys.executable}\nimport sys\nsys.path.insert(0, {str(tree / 'src')!r})\n"
                              f"from {module} import main\nraise SystemExit(main())\n")
            script.chmod(0o755)
        # Exercise the same binding/discovery probe as the production installer.
        env = preparation.command_environment(tree)
        probe = subprocess.run([str(commands / "commonplace-analysis"), "--help"], cwd=tree, env=env,
                               capture_output=True, text=True, check=True)
        assert "inspect-execution" in probe.stdout
        return {"python": sys.executable, "path-prefix": str(commands)}
    monkeypatch.setattr(preparation, "_install", install)
    fake = tmp_path / "fake"
    fake.mkdir()
    script = fake / "pi"
    script.write_text(f"#!{sys.executable}\n" + FAKE)
    script.chmod(0o755)
    scenario = fake / "scenario.json"
    scenario.write_text("{}")
    monkeypatch.setenv("PATH", str(fake) + os.pathsep + os.environ["PATH"])
    monkeypatch.setenv("FAKE_ROOT", str(ROOT))
    monkeypatch.setenv("FAKE_SCENARIO", str(scenario))
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", "/wrong/library/must-not-reach-child")
    upstream = tmp_path / "upstream"
    upstream.mkdir()
    git(upstream, "init", "--quiet")
    git(upstream, "config", "user.name", "Fixture")
    git(upstream, "config", "user.email", "fixture@example.invalid")
    (upstream / "README.md").write_text("Local acquisition fixture.\n")
    git(upstream, "add", "README.md")
    git(upstream, "commit", "--quiet", "-m", "Freeze local source")
    config = tmp_path / "gitconfig"
    config.write_text(f'[url "{upstream}"]\n\tinsteadOf = {IDENTITY}\n')
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", str(config))
    real_git = shutil.which("git")
    git_shim = fake / "git"
    git_shim.write_text(f"#!{sys.executable}\n" + (
        "import subprocess, sys\n"
        f"result = subprocess.run([{real_git!r}, *sys.argv[1:]], capture_output=True, check=False)\n"
        f"if sys.argv[-3:] == ['remote', 'get-url', 'origin'] and result.stdout.strip() == {str(upstream).encode()!r}:\n"
        f"    sys.stdout.buffer.write({(IDENTITY + chr(10)).encode()!r})\n"
        "else:\n    sys.stdout.buffer.write(result.stdout)\n"
        "sys.stderr.buffer.write(result.stderr)\nsys.exit(result.returncode)\n"
    ))
    git_shim.chmod(0o755)
    return origin, scenario, upstream


def invoke(capsys, *args):
    capsys.readouterr()
    code = main(list(args))
    captured = capsys.readouterr()
    return code, json.loads(captured.out) if captured.out.strip() else None, captured.err


@pytest.mark.slow
def test_complete_route_installs_frozen_environment_offline(command_origin, capsys, tmp_path, monkeypatch):
    # One real installation closes the boundary the smaller command fixtures
    # replace for cost. Archive committed library inputs, not ignored snapshots
    # or another writer's dirty KB bytes, then commit this implementation's src.
    fixture_origin, scenario, _ = command_origin
    archive = tmp_path / "committed-method.tar"
    subprocess.run(["git", "archive", "HEAD", "-o", str(archive)], cwd=ROOT, check=True)
    origin = tmp_path / "installed-origin"
    origin.mkdir()
    with tarfile.open(archive) as bundle:
        bundle.extractall(origin, filter="fully_trusted")
    shutil.rmtree(origin / "src")
    shutil.copytree(fixture_origin / "src", origin / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    git(origin, "init", "--quiet")
    git(origin, "config", "user.name", "Fixture")
    git(origin, "config", "user.email", "fixture@example.invalid")
    git(origin, "add", ".")
    git(origin, "commit", "--quiet", "-m", "Pin complete offline installation fixture")
    git(origin, "branch", "-M", "main")
    monkeypatch.chdir(origin)
    monkeypatch.setattr(preparation, "_install", PRODUCTION_INSTALL)
    monkeypatch.setenv("UV_OFFLINE", "1")
    scenario.write_text(json.dumps({"disposition": "blocked", "expected": {"boundary": 1}}))
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--state", str(tmp_path / "real-install-controller"))
    assert code == 0, (record, err)
    item, = record["targets"]
    assert item["status"] == "local-complete"
    tree = Path(item["worktree"])
    assert item["preparation"]["python"] == str(tree / ".venv/bin/python3")
    assert item["result"]["inspection"]["opening"]["inputs-commit"] == git(origin, "rev-parse", "HEAD")
    assert item["result"]["inspection"]["advisory-audit"]["state"] == "complete"
    assert git(origin, "status", "--porcelain") == ""


@pytest.mark.slow
def test_complete_prepared_command_correction_audit_and_fresh_controller(command_origin, capsys, tmp_path):
    origin, scenario, upstream = command_origin
    scenario.write_text(json.dumps({"report-verification": [REFUSE_RUNTIME_AND_MEMORY, "none"],
                                    "expected": {"boundary": 1, "runtime": 2, "memory": 2, "workflow": 1,
                                                 "epistemic": 1, "reconciliation": 2, "report-verification": 2,
                                                 "memory-profile": 1, "profile-verification": 1,
                                                 "synthesis": 1, "synthesis-verification": 1}}))
    before = git(origin, "rev-parse", "main")
    state = tmp_path / "controller"
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--state", str(state))
    assert code == 0, (record, err)
    item, = record["targets"]
    assert item["status"] == "published"
    tree, run = Path(item["worktree"]), Path(item["run"])
    view = item["result"]["inspection"]
    assert view["opening"]["inputs-commit"] == record["method-commit"] == before
    assert view["parameters"]["worker-profile"] == "pi-sol"
    assert view["parameters"]["command-path"] == str(tree / ".venv/bin")
    assert view["opening"]["source-identity"] == IDENTITY
    assert view["receipt"]["published"] is True
    assert view["advisory-audit"]["state"] == "complete"
    assert view["advisory-audit"]["model"] == "fake-auditor"
    assert json.loads((run / "code/acquire.json").read_text())["revision"] == git(upstream, "rev-parse", "HEAD")
    assert "fixture-only-no-model" in (run / "artifact/ARTIFACT.yaml").read_text()
    counts = {p.name: p.read_text() for p in scenario.with_name("counts").iterdir()}
    code, resumed, err = invoke(capsys, "resume", str(state))
    assert code == 0, err
    assert resumed["targets"][0]["run"] == str(run)
    assert {p.name: p.read_text() for p in scenario.with_name("counts").iterdir()} == counts
    assert len(list((tree / STATE_ROOT).glob("AAS-*"))) == 1
    assert git(origin, "rev-parse", "main") == before
    assert git(origin, "status", "--porcelain") == ""
    assert tree.is_dir() and tree.with_name(tree.name + ".preparation.json").is_file()
    assert (state / f"{item['key']}.stdout.log").is_file()


@pytest.mark.slow
@pytest.mark.parametrize("scenario_data,expected", [
    ({"disposition": "blocked", "expected": {"boundary": 1}}, "local-complete"),
    ({"disposition": "out-of-scope", "expected": {"boundary": 1}}, "local-complete"),
    ({"problem": {"boundary": [1]}, "expected": {"boundary": 1}}, "stopped"),
    ({"missing": {"boundary": [1, 2, 3]}, "expected": {"boundary": 3}}, "stopped"),
    ({"usage": {"boundary": [1]}, "expected": {"boundary": 1}}, "stopped"),
    ({"nonzero": {"boundary": [1, 2, 3]}, "expected": {"boundary": 3}}, "stopped"),
])
def test_prepared_local_and_worker_stops(command_origin, capsys, tmp_path, scenario_data, expected):
    origin, scenario, _ = command_origin
    scenario.write_text(json.dumps(scenario_data))
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--state", str(tmp_path / "controller"))
    assert code == (0 if expected == "local-complete" else 2), (record, err)
    item, = record["targets"]
    assert item["status"] == expected
    view = item["result"]["inspection"]
    assert view["advisory-audit"]["state"] == ("complete" if expected == "local-complete" else "skipped")
    assert not (origin / "kb/agentic-system-analyses/retained").exists()
    if expected == "local-complete":
        assert view["receipt"]["published"] is False
    else:
        assert view["receipt"] is None
        assert Path(item["worktree"]).is_dir()


@pytest.mark.slow
def test_explicit_resume_replays_answers_under_original_profile(command_origin, capsys, tmp_path):
    _, scenario, _ = command_origin
    scenario.write_text(json.dumps({"problem": {"synthesis": [1]}}))
    state = tmp_path / "controller"
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--worker-profile", "pi-luna", "--state", str(state))
    assert code == 2, (record, err)
    item, = record["targets"]
    counts = {p.name: p.read_text() for p in scenario.with_name("counts").iterdir()}
    tree = Path(item["worktree"])
    result = subprocess.run([str(tree / ".venv/bin/commonplace-analysis"), "retry", item["run"], "synthesis"],
                            cwd=tree, env=preparation.command_environment(tree), check=False, capture_output=True)
    assert result.returncode == 0, result.stderr
    scenario.write_text("{}")
    code, record, err = invoke(capsys, "resume", str(state), "--target", IDENTITY)
    assert code == 0, (record, err)
    resumed, = record["targets"]
    assert resumed["run"] == item["run"]
    assert resumed["result"]["inspection"]["parameters"]["worker-profile"] == "pi-luna"
    for name, count in counts.items():
        assert scenario.with_name("counts").joinpath(name).read_text() == ("2" if name == "synthesis" else count)


@pytest.mark.parametrize("data", [
    [{"source": "https://github.com/owner/repo/issues/1"}],
    [{"source": IDENTITY}, {"source": "git@github.com:EXAMPLE/system.git"}],
    [{"source": IDENTITY}, {"source": "ssh://git@GitHub.com/EXAMPLE/system.git"}],
    [{"source": IDENTITY}, {"source": "ssh://github.com/example/system"}],
    [{"source": IDENTITY}, {"source": "local docs", "source-kind": "documents", "system": "Example",
                              "source-identity": "git@GitHub.com:example/system.git"}],
    [{"source": "missing", "source-kind": "local"}],
    [{"source": "docs", "source-kind": "documents"}],
    [{"source": IDENTITY, "source-revision": "abc"}],
    [{"source": IDENTITY, "triage": "not analyst input"}],
    [{"source": IDENTITY, "source-identity": "https://github.com/other/not-approved"}],
    [{"source": IDENTITY}, {"source": IDENTITY, "source-identity": "alias:system"}],
])
def test_invalid_intake_has_no_preparation_effects(tmp_path, monkeypatch, data):
    monkeypatch.setattr(auto, "select_method", lambda *a: pytest.fail("intake must fail before method/setup"))
    with pytest.raises(ValueError):
        auto.create(tmp_path, data, profile="pi-sol", revision=None, state=tmp_path / "state", worktree_root=None,
                    concurrency=4, max_workers=3, timeout=60, require_clean_origin=False)
    assert not (tmp_path / "state").exists()


@pytest.mark.slow
def test_shared_opening_failure_pauses_before_preparing_next_target(command_origin, capsys, tmp_path):
    origin, scenario, _ = command_origin
    retained = origin / "kb/agentic-system-analyses/retained"
    retained.mkdir(parents=True, exist_ok=True)
    (retained / "not-an-artifact.txt").write_text("Invalid shared publication state.\n")
    git(origin, "add", "kb/agentic-system-analyses/retained/not-an-artifact.txt")
    git(origin, "commit", "--quiet", "-m", "Pin invalid shared publication fixture")
    targets = tmp_path / "targets.txt"
    targets.write_text(IDENTITY + "\nhttps://github.com/example/second\n")
    code, record, err = invoke(capsys, "batch", str(targets), "--concurrency", "1",
                               "--state", str(tmp_path / "state"))
    assert code == 3, (record, err)  # pending work has interruption/attention precedence
    assert record["counts"] == {"command-failed": 1, "pending": 1}
    first, second = record["targets"]
    assert first["result"]["inspection"]["stop-type"] == "OpeningFailed"
    assert "current analysis must be a directory" in first["error"]
    assert not Path(second["worktree"]).exists()
    assert not scenario.with_name("counts").exists()


@pytest.mark.slow
def test_advisory_audit_failure_reaches_outer_result_without_gating_completion(command_origin, capsys, tmp_path):
    _, scenario, _ = command_origin
    scenario.write_text(json.dumps({"disposition": "blocked", "audit-failure": True}))
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--state", str(tmp_path / "controller"))
    assert code == 0, (record, err)
    item, = record["targets"]
    assert item["status"] == "local-complete"
    assert item["result"]["inspection"]["advisory-audit"]["state"] == "failed"


@pytest.mark.slow
def test_killed_pinned_controller_leaves_unsettled_worker_without_relaunch(command_origin, tmp_path):
    origin, scenario, _ = command_origin
    info = tmp_path / "worker.json"
    scenario.write_text(json.dumps({"sleep": {"boundary": 60}, "process-info": str(info)}))
    state = auto.create(origin, [{"source": IDENTITY}], profile="pi-sol", revision=None, state=tmp_path / "state",
                        worktree_root=None, concurrency=1, max_workers=3, timeout=90, require_clean_origin=False)
    controller = auto.Controller(state)
    item, = controller.record["targets"]
    prep = preparation.prepare_worktree(origin, name=item["label"], revision=controller.record["method-commit"],
                                        worktree=Path(item["worktree"]))
    controller.update(item, phase="prepared", preparation=prep)
    process = controller_process(state)
    worker = None
    try:
        wait_for(info.exists)
        worker = json.loads(info.read_text())
        os.kill(worker["ppid"], signal.SIGKILL)
        os.killpg(worker["pid"], signal.SIGKILL)
        assert process.wait(timeout=20) == 3
        before = scenario.with_name("counts").joinpath("boundary").read_text()
        resumed = auto.Controller(state).run(selected=[IDENTITY])
        item, = resumed["targets"]
        assert item["status"] == "operator-attention"
        assert item["result"]["inspection"]["unsettled-launches"]
        assert scenario.with_name("counts").joinpath("boundary").read_text() == before == "1"
        assert len(list((Path(item["worktree"]) / STATE_ROOT).glob("AAS-*"))) == 1
    finally:
        if worker is not None:
            try:
                os.killpg(worker["pid"], signal.SIGKILL)
            except ProcessLookupError:
                pass
        if process.poll() is None:
            process.kill()
        process.wait(timeout=10)


def test_local_and_document_routes_are_explicit_and_absolute(tmp_path):
    path = tmp_path / "snapshot.txt"
    path.write_text("capture")
    local = auto.target({"source": str(path), "source-kind": "local"})
    assert local["source"] == str(path) and local["source-identity"] == path.as_uri()
    documents = {"source": "explicit supplied document bundle", "source-kind": "documents",
                 "source-identity": "documents:fixture", "system": "Fixture"}
    assert auto.target(documents) == documents


@pytest.mark.parametrize("failure", ["install", "startup", "behind"])
def test_preparation_failure_retains_evidence_without_alternate_method(command_origin, capsys, tmp_path, monkeypatch, failure):
    origin, _, _ = command_origin
    before = git(origin, "rev-parse", "HEAD")
    if failure == "install":
        def fail(tree):
            raise ValueError("fixture install refusal")
        monkeypatch.setattr(preparation, "_install", fail)
    elif failure == "startup":
        (origin / "AGENTS.md").write_text("dirty startup")
    else:
        git(origin, "checkout", "--quiet", "--detach", "HEAD~1")
    state = tmp_path / "state"
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--state", str(state))
    assert code == 1, (record, err)
    if failure == "install":
        item, = record["targets"]
        assert item["status"] == "preparation-failed" and item["run"] is None
        tree = Path(item["worktree"])
        assert json.loads(tree.with_name(tree.name + ".preparation.json").read_text())["status"] == "failed"
        assert tree.is_dir() and git(tree, "rev-parse", "HEAD") == before
        assert not (tree / STATE_ROOT).exists()
    else:
        assert not state.exists()
        assert "startup instructions" in err or "behind" in err


def scheduler_state(tmp_path, count=5):
    state = tmp_path / "controller"
    state.mkdir()
    items = [{"key": f"{i:032x}", "target": {"source-identity": f"source:{i}"}, "phase": "prepared",
              "worktree": str(tmp_path / f"tree-{i}"), "status": "pending", "run": None, "result": None,
              "error": None} for i in range(count)]
    save(state / "controller.json", {"schema": auto.SCHEMA, "controller": str(state), "concurrency": 4,
                                   "max-workers": 3, "maximum-role-workers": 12, "targets": items})
    return state


def wait_for(predicate, timeout=15):
    until = time.monotonic() + timeout
    while time.monotonic() < until:
        if predicate():
            return
        time.sleep(.02)
    pytest.fail("barrier did not arrive")


def test_four_slot_queue_opposite_completion_orders_and_mixed_outcomes(tmp_path, monkeypatch):
    state = scheduler_state(tmp_path, 6)
    monkeypatch.setattr(auto.Controller, "reconcile", lambda *a: None)
    guard = threading.Lock()
    started, active, maximum = [], set(), []
    barriers = [threading.Event() for _ in range(6)]
    statuses = ["published", "local-complete", "stopped", "published", "published", "stopped"]
    def work(self, item):
        i = int(item["key"], 16)
        with guard:
            started.append(i)
            active.add(i)
            maximum.append(len(active))
        assert barriers[i].wait(15)
        self.update(item, status=statuses[i], run=f"run-{i}", result={"receipt": f"receipt-{i}"})
        with guard:
            active.remove(i)
    monkeypatch.setattr(auto.Controller, "work", work)
    controller = auto.Controller(state)
    thread = threading.Thread(target=controller.run)
    thread.start()
    wait_for(lambda: len(started) == 4)
    assert set(started) == {0, 1, 2, 3}
    with pytest.raises(ValueError, match="still owns"):
        auto.Controller(state).run()
    barriers[2].set()  # an ordinary stop releases a slot; unrelated long jobs remain
    wait_for(lambda: 4 in started)
    assert not barriers[0].is_set() and not barriers[1].is_set()
    barriers[4].set()
    wait_for(lambda: 5 in started)
    for barrier in reversed(barriers):
        barrier.set()
    thread.join(15)
    assert not thread.is_alive() and max(maximum) == 4
    record = auto.report(state)
    assert auto.exit_code(record) == 2
    assert [item["result"]["receipt"] for item in record["targets"]] == [f"receipt-{i}" for i in range(6)]
    assert record["counts"] == {"published": 3, "local-complete": 1, "stopped": 2}


def test_restart_reconciles_before_claims_and_pauses_on_unknown_child(tmp_path, monkeypatch):
    state = scheduler_state(tmp_path)
    controller = auto.Controller(state)
    controller.update(controller.record["targets"][0], phase="executing", status="active")
    seen = []
    def reconcile(self, item, fd):
        seen.append(item["key"])
        if item["phase"] == "executing":
            raise ValueError("unsettled child; missing PID is not settlement")
    monkeypatch.setattr(auto.Controller, "reconcile", reconcile)
    monkeypatch.setattr(auto.Controller, "work", lambda *a: pytest.fail("must pause new claims"))
    record = auto.Controller(state).run()
    assert len(seen) == 5
    assert record["targets"][0]["status"] == "operator-attention"
    assert record["counts"]["pending"] == 4 and auto.exit_code(record) == 3


def test_explicit_selection_cannot_use_stale_inspection_after_a_failed_lease(tmp_path, monkeypatch):
    state = scheduler_state(tmp_path)
    record = auto.report(state)
    record.pop("counts")
    record["targets"][0].update({"phase": "executing", "status": "stopped",
                                  "result": {"inspection": {"state": "stopped"}}})
    save(state / "controller.json", record)
    monkeypatch.setattr(auto.Controller, "reconcile", lambda *a: None)
    monkeypatch.setattr(auto.Controller, "work", lambda *a: pytest.fail("stale inspection must not permit new claims"))
    with lease(state / "leases" / record["targets"][0]["key"]):
        resumed = auto.Controller(state).run(selected=["source:0"])
    assert resumed["targets"][0]["status"] == "operator-attention"
    assert resumed["counts"]["pending"] == 4


def test_inherited_child_lease_survives_parent_descriptor_close(tmp_path):
    marker = tmp_path / "ready"
    release = tmp_path / "release"
    path = tmp_path / "lease"
    with lease(path) as fd:
        process = subprocess.Popen([sys.executable, "-c", (
            "import time; from pathlib import Path; "
            f"Path({str(marker)!r}).touch(); "
            f"\nwhile not Path({str(release)!r}).exists(): time.sleep(.02)"
        )], pass_fds=(fd,), start_new_session=True)
        wait_for(marker.exists)
    try:
        with pytest.raises(ValueError, match="still owns"), lease(path):
            pass
    finally:
        release.touch()
        process.wait(timeout=10)
    with lease(path):
        pass


@pytest.mark.parametrize("stop_type", ["UncertainEffectError", "UncertainLaunchError", "RecordError"])
def test_uncertainty_is_not_an_ordinary_stop(stop_type):
    assert outcome({"state": "stopped", "stop-type": stop_type}) == "operator-attention"
    assert outcome({"state": "stopped", "stop-type": "Problem"}) == "stopped"
    assert outcome({"state": "stopped", "command-failed": True}) == "command-failed"
    assert outcome({"state": "published", "advisory-audit": {"state": "interrupted"}}) == "operator-attention"
    assert outcome({"state": "published", "advisory-audit": {
        "state": "failed", "unsettled-launches": ["audit-launch"]}}) == "operator-attention"


def test_allocation_crash_recovers_exact_reservation_and_legacy_cannot_steal_it(request, monkeypatch):
    from commonplace.lib.agentic_analysis import durable

    prepared_checkout = request.getfixturevalue("bound_checkout")
    key = "a" * 32
    params = {"system": "Example", "source_identity": IDENTITY, "source": "caller input", "worker_profile": "pi-luna"}
    original = durable.save
    def crash(path, data):
        original(path, data)
        if path == allocation_path(prepared_checkout.repo, key):
            raise RuntimeError("crash after allocation effect, before outer binding")
    monkeypatch.setattr(durable, "save", crash)
    with pytest.raises(RuntimeError, match="crash after allocation"):
        start_analysis(prepared_checkout.repo, **params, allocation_key=key)
    bound = json.loads(allocation_path(prepared_checkout.repo, key).read_text())
    monkeypatch.setattr(durable, "save", original)
    other = start_analysis(prepared_checkout.repo, **params)
    assert other.name != bound["run-id"], "legacy allocation must honor an unmaterialized reservation"
    resumed = start_analysis(prepared_checkout.repo, **params, allocation_key=key)
    assert resumed.name == bound["run-id"]
    assert start_analysis(prepared_checkout.repo, **params, allocation_key=key) == resumed
    with pytest.raises(ValueError, match="binding differs"):
        start_analysis(prepared_checkout.repo, **{**params, "worker_profile": "pi-sol"}, allocation_key=key)


@pytest.fixture
def scripted_queue(tmp_path, monkeypatch):
    state = scheduler_state(tmp_path, 6)
    record = auto.report(state)
    record.pop("counts")
    record.update({"origin": str(tmp_path), "method-commit": "fixture-commit", "worker-profile": "pi-sol",
                   "timeout": 60, "require-clean-origin": False})
    barriers = tmp_path / "barriers"
    barriers.mkdir()
    monkeypatch.setenv("QUEUE_FIXTURE", str(barriers))
    fixture = ROOT / "tests/commonplace/agentic_analysis/automation_queue_fixture.py"
    for i, item in enumerate(record["targets"]):
        item["target"].update({"source": f"input-{i}", "system": f"System {i}"})
        tree = Path(item["worktree"])
        commands = tree / ".venv/bin"
        commands.mkdir(parents=True)
        command = commands / "commonplace-analysis"
        command.write_text(f"#!{sys.executable}\nimport runpy\nrunpy.run_path({str(fixture)!r}, run_name='__main__')\n")
        command.chmod(0o755)
        save(tree.with_name(tree.name + ".preparation.json"), {
            "status": "ready", "worktree": str(tree), "commit": "fixture-commit", "token": "0123456789ab",
            "path-prefix": str(commands),
        })
        (barriers / f"{item['key']}.outcome").write_text(["published", "local-complete", "stopped", "published",
                                                       "published", "stopped"][i])
    save(state / "controller.json", record)
    try:
        yield state, barriers, record
    finally:
        # Even a failed scheduler assertion must release every scripted child;
        # test-local commands cannot outlive teardown and contaminate another case.
        for item in record["targets"]:
            (barriers / f"{item['key']}.release").touch()
        def settled():
            try:
                with lease(state / ".controller.lock"):
                    for item in record["targets"]:
                        with lease(state / "leases" / item["key"]):
                            pass
                return True
            except ValueError:
                return False
        wait_for(settled)


@pytest.mark.parametrize("first", [0, 2])
def test_scripted_commands_preserve_cross_target_bindings_and_reconcile_restart(scripted_queue, first):
    state, barriers, original = scripted_queue
    thread = threading.Thread(target=lambda: auto.Controller(state).run())
    thread.start()
    wait_for(lambda: len(list(barriers.glob("*.started"))) == 4)
    keys = [item["key"] for item in original["targets"]]
    (barriers / f"{keys[first]}.release").touch()
    wait_for(lambda: (barriers / f"{keys[4]}.started").exists())
    assert not (barriers / f"{keys[2 if first == 0 else 0]}.finished").exists()
    (barriers / f"{keys[4]}.release").touch()
    wait_for(lambda: (barriers / f"{keys[5]}.started").exists())
    for key in (reversed(keys) if first == 2 else keys):
        (barriers / f"{key}.release").touch()
    thread.join(20)
    assert not thread.is_alive()
    record = auto.report(state)
    for before, after in zip(original["targets"], record["targets"], strict=True):
        assert before["key"] in after["run"]
        assert after["result"]["inspection"]["receipt"]["target"] == before["target"]["source-identity"]
        assert after["worktree"] == before["worktree"]
        log = (state / f"{before['key']}.stdout.log").read_text()
        assert before["target"]["source-identity"] in log
        assert all(other["target"]["source-identity"] not in log
                   for other in original["targets"] if other["key"] != before["key"])
    assert record["counts"] == {"published": 3, "local-complete": 1, "stopped": 2}
    started = {p.name: p.stat().st_mtime_ns for p in barriers.glob("*.started")}
    resumed = auto.Controller(state).run()
    assert resumed["counts"] == record["counts"]
    assert {p.name: p.stat().st_mtime_ns for p in barriers.glob("*.started")} == started


def test_uncertain_scripted_child_pauses_pending_claims_without_automatic_recovery(scripted_queue):
    state, barriers, original = scripted_queue
    keys = [item["key"] for item in original["targets"]]
    (barriers / f"{keys[2]}.outcome").write_text("operator-attention")
    thread = threading.Thread(target=lambda: auto.Controller(state).run())
    thread.start()
    wait_for(lambda: len(list(barriers.glob("*.started"))) == 4)
    (barriers / f"{keys[2]}.release").touch()
    wait_for(lambda: auto.report(state)["targets"][2]["status"] == "operator-attention")
    for key in keys[:4]:
        (barriers / f"{key}.release").touch()
    thread.join(20)
    assert not thread.is_alive()
    record = auto.report(state)
    assert record["counts"]["pending"] == 2 and auto.exit_code(record) == 3
    resumed = auto.Controller(state).run(selected=["source:2"])
    assert resumed["counts"]["operator-attention"] == 1
    assert len(list(barriers.glob("*.started"))) == 4


def controller_process(state):
    return subprocess.Popen([sys.executable, "-c", (
        "import sys; from pathlib import Path; "
        f"sys.path.insert(0, {str(ROOT / 'src')!r}); "
        "from commonplace.lib.agentic_analysis.automation import Controller, exit_code; "
        f"raise SystemExit(exit_code(Controller(Path({str(state)!r})).run()))"
    )], start_new_session=True)


def test_sigterm_drains_owned_children_and_stops_new_claims(scripted_queue):
    state, barriers, original = scripted_queue
    process = controller_process(state)
    keys = [item["key"] for item in original["targets"]]
    try:
        wait_for(lambda: len(list(barriers.glob("*.started"))) == 4)
        process.send_signal(signal.SIGTERM)
        time.sleep(.2)
        assert process.poll() is None, "SIGTERM must drain, not abandon child groups"
        for key in keys[:4]:
            (barriers / f"{key}.release").touch()
        assert process.wait(timeout=20) == 3
        record = auto.report(state)
        assert record["counts"]["pending"] == 2
        assert len(list(barriers.glob("*.started"))) == 4
        assert all(item["status"] != "active" for item in record["targets"])
    finally:
        for key in keys:
            (barriers / f"{key}.release").touch()
        if process.poll() is None:
            process.kill()
        process.wait(timeout=10)


@pytest.mark.parametrize("signum", [signal.SIGINT, signal.SIGTERM])
def test_low_level_commands_keep_group_cancellation_for_descendants(tmp_path, signum):
    ready, stopped = tmp_path / "ready", tmp_path / "stopped"
    descendant = (
        "from pathlib import Path\nimport signal, sys, time\n"
        "def stop(*args):\n"
        f"    Path({str(stopped)!r}).touch()\n"
        "    sys.exit(0)\n"
        "signal.signal(signal.SIGTERM, stop)\nsignal.signal(signal.SIGINT, stop)\n"
        f"Path({str(ready)!r}).touch()\n"
        "while True: time.sleep(.02)\n"
    )
    child = f"import subprocess, sys; subprocess.run([sys.executable, '-c', {descendant!r}])"
    script = (
        "import sys, signal\nfrom pathlib import Path\n"
        "signal.signal(signal.SIGINT, signal.default_int_handler)\n"
        f"sys.path.insert(0, {str(ROOT / 'src')!r})\n"
        "from commonplace.lib.agentic_analysis.preparation import run_command\n"
        f"run_command([sys.executable, '-c', {child!r}], cwd=Path({str(tmp_path)!r}))\n"
    )
    process = subprocess.Popen([sys.executable, "-c", script], start_new_session=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        wait_for(ready.exists)
        os.killpg(process.pid, signum)
        assert process.wait(timeout=20) != 0
        wait_for(stopped.exists)
    finally:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait(timeout=10)


@pytest.mark.parametrize("signum", [signal.SIGINT, signal.SIGTERM])
def test_group_signal_drains_preparation_before_stopping_claims(tmp_path, signum):
    state = scheduler_state(tmp_path, 2)
    record = auto.report(state)
    record.pop("counts")
    record.update({"origin": str(tmp_path), "method-commit": "fixture", "concurrency": 1,
                   "require-clean-origin": False})
    for item in record["targets"]:
        item.update(phase="pending", label="fixture")
    save(state / "controller.json", record)
    started, release, finished = [tmp_path / name for name in ("started", "release", "finished")]
    installer = (
        "from pathlib import Path\nimport time\n"
        f"Path({str(started)!r}).touch()\n"
        f"while not Path({str(release)!r}).exists(): time.sleep(.02)\n"
        f"Path({str(finished)!r}).touch()\n"
    )
    script = (
        "import sys\nfrom pathlib import Path\n"
        f"sys.path.insert(0, {str(ROOT / 'src')!r})\n"
        "from commonplace.lib.agentic_analysis import automation as auto, preparation\n"
        "def prepare(*args, **kwargs):\n"
        f"    preparation.run_command([sys.executable, '-c', {installer!r}], cwd=Path({str(tmp_path)!r}))\n"
        "    return {'status': 'ready'}\n"
        "auto.prepare_worktree = prepare\n"
        f"raise SystemExit(auto.exit_code(auto.Controller(Path({str(state)!r})).run()))\n"
    )
    process = subprocess.Popen([sys.executable, "-c", script], start_new_session=True)
    try:
        wait_for(started.exists)
        os.killpg(process.pid, signum)
        time.sleep(.2)
        assert process.poll() is None, "preparation must drain, not receive the group signal"
        release.touch()
        assert process.wait(timeout=20) == 3
        assert finished.exists()
        result = auto.report(state)
        assert result["counts"] == {"pending": 2}
        assert [item["phase"] for item in result["targets"]] == ["prepared", "pending"]
    finally:
        release.touch()
        if process.poll() is None:
            process.kill()
        process.wait(timeout=10)


def test_abrupt_controller_death_retains_live_child_lease_and_reconciles_without_replacement(scripted_queue):
    state, barriers, original = scripted_queue
    process = controller_process(state)
    keys = [item["key"] for item in original["targets"]]
    try:
        wait_for(lambda: len(list(barriers.glob("*.started"))) == 4)
        process.kill()
        process.wait(timeout=10)
        record = auto.Controller(state).run()
        assert record["counts"]["operator-attention"] == 4
        assert record["counts"]["pending"] == 2
        assert len(list(barriers.glob("*.started"))) == 4
        # An orphan may still finish. Its lease, not a PID guess, prevents claims.
        for key in keys:
            (barriers / f"{key}.release").touch()
        wait_for(lambda: len(list(barriers.glob("*.finished"))) == 4)
        # finished marker precedes process exit; wait until inherited leases close.
        def settled():
            try:
                for key in keys[:4]:
                    with lease(state / "leases" / key):
                        pass
                return True
            except ValueError:
                return False
        wait_for(settled)
        resumed = auto.Controller(state).run()
        assert resumed["counts"] == {"published": 3, "local-complete": 1, "stopped": 2}
        assert len(list(barriers.glob("*.started"))) == 6
        assert all(item["run"].endswith("run-" + item["key"]) for item in resumed["targets"])
    finally:
        for key in keys:
            (barriers / f"{key}.release").touch()
        if process.poll() is None:
            process.kill()
        process.wait(timeout=10)
