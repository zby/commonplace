"""Exercise the OS boundary and evidence collection without calling a model."""

import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

from scripts.run_isolated_codex import (
    installation_sandbox,
    probe,
    run_bounded,
    sandbox,
)

pytestmark = pytest.mark.skipif(sys.platform != "linux", reason="Linux-only launcher")


@pytest.fixture
def installation(tmp_path):
    for name in ("project", "tools", "bin", "records", "vendor/bin"):
        (tmp_path / name).mkdir(parents=True)
    for file, body in (
        ("tools/commonplace-validate", "exit 0"),
        ("vendor/bin/codex", "echo codex-test"),
    ):
        path = tmp_path / file
        path.write_text("#!/bin/sh\n" + body + "\n")
        path.chmod(0o755)
    (tmp_path / "bin/commonplace-validate").symlink_to(
        tmp_path / "tools/commonplace-validate"
    )
    (tmp_path / "records/key.txt").write_text("evaluator-only answer")
    (tmp_path / "project/escape").symlink_to(tmp_path / "records/key.txt")
    return tmp_path


@pytest.mark.skipif(
    sys.platform != "linux" or not shutil.which("bwrap"),
    reason="Linux bubblewrap integration test",
)
@pytest.mark.parametrize("readonly", [False, True])
def test_real_filesystem_boundary(installation, readonly):
    run = installation
    command, env = sandbox(run, run / "vendor", readonly, authenticate=False)
    # Restricted kernels may have bwrap installed but disable user namespaces.
    available = subprocess.run(
        command + ["--", "/bin/true"], env=env, capture_output=True, check=False
    )
    if available.returncode and b"Operation not permitted" in available.stderr:
        pytest.skip(f"bubblewrap unavailable: {available.stderr.decode()}")
    assert available.returncode == 0, available.stderr.decode()
    evidence = probe(command, env, run, readonly)
    assert all(evidence["checks"].values())
    assert env["HOME"] == os.environ["HOME"]
    assert "CODEX_API_KEY" not in env
    checkout = Path(__file__).resolve().parents[3]
    check = subprocess.run(
        command
        + [
            "--",
            "/usr/bin/python3",
            "-c",
            (
                "from pathlib import Path; "
                "assert not Path('escape').exists(); "
                f"assert not Path('/proc/1/root{run}/records/key.txt').exists(); "
                f"assert not Path({str(checkout / 'AGENTS.md')!r}).exists()"
            ),
        ],
        env=env,
        check=False,
    )
    assert check.returncode == 0


def test_timeout_records_failure_and_preserves_partial_trace(tmp_path):
    result = run_bounded(
        [
            sys.executable,
            "-c",
            "import time; print('partial', flush=True); time.sleep(60)",
        ],
        {},
        "prompt",
        tmp_path,
        0.1,
    )
    assert result["timed_out"]
    assert not result["interrupted"]
    assert result["exit_code"] != 0
    assert (tmp_path / "trace.jsonl").read_text() == "partial\n"


@pytest.mark.parametrize("stop_signal", [signal.SIGINT, signal.SIGTERM])
def test_operator_stop_reaps_process_and_retains_evidence(tmp_path, stop_signal):
    code = """
import json, sys
from pathlib import Path
from scripts.run_isolated_codex import run_bounded
result = run_bounded(
    [sys.executable, '-c',
     'import os,time; print(os.getpid(), flush=True); time.sleep(60)'],
    {}, 'prompt', Path(sys.argv[1]), 60)
print(json.dumps(result))
"""
    process = subprocess.Popen(
        [sys.executable, "-c", code, str(tmp_path)],
        cwd=Path(__file__).resolve().parents[3],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        trace = tmp_path / "trace.jsonl"
        deadline = time.monotonic() + 10
        while not trace.exists() or not trace.read_text().strip():
            assert process.poll() is None
            assert time.monotonic() < deadline
            time.sleep(0.01)
        child_pid = int(trace.read_text())
        process.send_signal(stop_signal)
        stdout, stderr = process.communicate(timeout=10)
        assert process.returncode == 0, stderr
        result = json.loads(stdout)
        assert result["interrupted"]
        assert not result["timed_out"]
        assert result["termination_signal"] == stop_signal
        assert result["exit_code"] != 0
        assert int(trace.read_text()) == child_pid
        with pytest.raises(ProcessLookupError):
            os.kill(child_pid, 0)
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()


def test_rejects_checkout_as_run_directory():
    checkout = Path(__file__).resolve().parents[3]
    with pytest.raises(ValueError, match="outside the Commonplace checkout"):
        sandbox(checkout, checkout, authenticate=False)


@pytest.mark.skipif(not shutil.which("bwrap"), reason="Requires bubblewrap")
def test_installation_can_create_skills_but_cannot_change_source(installation):
    run = installation
    for name in ("source", "cache", "tmp"):
        (run / name).mkdir()
    (run / "source/INSTALL.md").write_text("installation instructions")
    uv = run / "uv"
    uv.write_text("#!/bin/sh\necho uv-test\n")
    uv.chmod(0o755)
    command, env = installation_sandbox(
        run, run / "vendor", uv, authenticate=False
    )
    available = subprocess.run(
        command + ["--", "/bin/true"], env=env, capture_output=True, check=False
    )
    if available.returncode and b"Operation not permitted" in available.stderr:
        pytest.skip("User namespaces unavailable")
    assert available.returncode == 0, available.stderr.decode()
    evidence = probe(command, env, run, False, installation=True)
    assert all(evidence["checks"].values())
    assert not (run / "project/.agents").exists()
    assert (run / "source/INSTALL.md").read_text() == "installation instructions"


def test_rejects_evaluator_directory_inside_project(installation):
    records = installation / "records"
    shutil.rmtree(records)
    records.symlink_to(installation / "project", target_is_directory=True)
    with pytest.raises(ValueError, match="Evaluator records"):
        sandbox(installation, installation / "vendor", authenticate=False)
