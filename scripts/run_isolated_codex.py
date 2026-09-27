#!/usr/bin/env python3
"""Launch one supplied prompt in an isolated Linux/Codex process.

Mechanical helper for the orchestrator instruction test-installed-commonplace.md.
Enforces filesystem/context boundaries, probes them, applies the supplied access
mode and timeout, and records raw process evidence. It has no scenario sequence,
artifact assessment, response interpretation, or acceptance verdict.
"""

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def native_vendor(explicit=None):
    if explicit:
        vendor = Path(explicit).resolve()
    else:
        executable = shutil.which("codex")
        if not executable:
            raise ValueError("codex is unavailable; supply --codex-vendor")
        package = Path(executable).resolve().parent.parent
        matches = list(package.glob("node_modules/@openai/codex-*/vendor/*/bin/codex"))
        if len(matches) != 1:
            raise ValueError("Cannot locate native Codex; supply --codex-vendor")
        vendor = matches[0].parent.parent
    if not (vendor / "bin/codex").is_file():
        raise ValueError("Codex vendor directory must contain bin/codex")
    return vendor


def sandbox(run, vendor, readonly=False, authenticate=True, auth_mode="saved"):
    """Expose only system software, the package, and the disposable project."""
    checkout = Path(__file__).resolve().parent.parent
    if run == checkout or run.is_relative_to(checkout):
        raise ValueError("Run directory must be outside the Commonplace checkout")
    if (run / "records").is_symlink():
        raise ValueError("Evaluator records must not be a symlink")
    project = run / "project"
    for name in ("project", "tools", "bin"):
        path = run / name
        if not path.is_dir() or path.is_symlink():
            raise ValueError(f"Expected a real directory: {path}")
    bwrap = shutil.which("bwrap")
    if not bwrap or sys.platform != "linux":
        raise ValueError("This launcher requires Linux and bubblewrap")
    # Keep HOME and CODEX_HOME at their original values; expose empty filesystem
    # locations there, rather than redirecting either environment variable.
    original_home = Path(os.environ["HOME"])
    runtime_home = Path(os.environ.get("CODEX_HOME", str(original_home / ".codex")))
    if not original_home.is_absolute() or not runtime_home.is_absolute():
        raise ValueError("HOME and CODEX_HOME must be absolute")
    for control in (original_home, runtime_home):
        if control == run or control.is_relative_to(run):
            raise ValueError(
                "Runtime control directory must be outside the run directory"
            )
    command = [
        bwrap,
        "--unshare-user",
        "--unshare-pid",
        "--unshare-ipc",
        "--unshare-uts",
        "--die-with-parent",
        "--new-session",
        "--ro-bind",
        "/usr",
        "/usr",
    ]
    for name in ("bin", "sbin", "lib", "lib64"):
        path = Path("/") / name
        if path.is_symlink():
            command += ["--symlink", os.readlink(path), str(path)]
        elif path.is_dir():
            command += ["--ro-bind", str(path), str(path)]
    command += [
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--tmpfs",
        "/tmp",
        "--dir",
        str(original_home),
        "--dir",
        str(runtime_home),
    ]
    for name in (
        "resolv.conf",
        "hosts",
        "nsswitch.conf",
        "passwd",
        "group",
        "ssl/certs",
    ):
        path = Path("/etc") / name
        if path.exists():
            command += ["--ro-bind", str(path), str(path)]
    command += ["--ro-bind", str(vendor), "/opt/codex"]
    for name in ("tools", "bin"):
        command += ["--ro-bind", str(run / name), str(run / name)]
    command += [
        "--ro-bind" if readonly else "--bind",
        str(project),
        str(project),
        "--chdir",
        str(project),
    ]
    env = {
        "HOME": str(original_home),
        "PATH": f"{run / 'bin'}:/opt/codex/bin:/usr/bin:/bin",
        "LANG": "C.UTF-8",
        "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if "CODEX_HOME" in os.environ:
        env["CODEX_HOME"] = os.environ["CODEX_HOME"]
    if authenticate:
        if auth_mode == "saved" and (runtime_home / "auth.json").is_file():
            auth = runtime_home / "auth.json"
            command += ["--ro-bind", str(auth), str(auth)]
        elif auth_mode == "env" and (
            key := os.environ.get("CODEX_API_KEY") or os.environ.get("OPENAI_API_KEY")
        ):
            env["CODEX_API_KEY"] = key
        else:
            raise ValueError(f"Authentication unavailable for --auth {auth_mode}")
    return command, env


PROBE = r"""
import json, os, pathlib, subprocess, sys
project, tools, bindir = map(pathlib.Path, sys.argv[1:4])
forbidden = json.loads(sys.argv[4])
readonly = sys.argv[5] == "true"
checks = {}
for name in forbidden:
    checks["hidden:" + name] = not os.path.lexists(name)
for root in (tools, bindir):
    target = root / ".isolation-write-probe"
    try:
        target.write_text("unexpected write")
    except OSError:
        checks["immutable:" + str(root)] = True
    else:
        target.unlink()
        checks["immutable:" + str(root)] = False
target = project / ".isolation-write-probe"
try:
    target.write_text("project write")
except OSError:
    checks["project_mode"] = readonly
else:
    checks["project_mode"] = not readonly
    target.unlink()
checks["installed_command"] = subprocess.run(
    ["commonplace-validate", "--help"], stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL).returncode == 0
version = subprocess.run(["codex", "--version"], capture_output=True, text=True)
checks["codex_starts"] = version.returncode == 0
print(json.dumps({"checks": checks, "codex_version": version.stdout.strip()}))
sys.exit(0 if all(checks.values()) else 1)
"""


def probe(command, env, run, readonly):
    checkout = Path(__file__).resolve().parent.parent
    personal = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    forbidden = [
        str(checkout),
        str(run / "records"),
        str(personal / "config.toml"),
        str(personal / "memories"),
        str(personal / "skills"),
        str(Path.home() / ".agents"),
    ]
    result = subprocess.run(
        command
        + [
            "--",
            "/usr/bin/python3",
            "-c",
            PROBE,
            str(run / "project"),
            str(run / "tools"),
            str(run / "bin"),
            json.dumps(forbidden),
            str(readonly).lower(),
        ],
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"Isolation probe failed: {result.stdout}\n{result.stderr}")
    return json.loads(result.stdout)


def codex_args(project, readonly):
    args = [
        "--",
        "/opt/codex/bin/codex",
        "--no-daemon",
        "-a",
        "never",
        "exec",
        "--ignore-user-config",
        "--ignore-rules",
        "--json",
        "--skip-git-repo-check",
        "--strict-config",
        "-C",
        str(project),
        "--sandbox",
        "read-only" if readonly else "workspace-write",
    ]
    for setting in (
        "sandbox_workspace_write.network_access=true",
        "memories.use_memories=false",
        "memories.generate_memories=false",
        'shell_environment_policy.exclude=["CODEX_API_KEY","OPENAI_API_KEY"]',
        "features.memories=false",
        "features.apps=false",
        "features.plugins=false",
        "features.hooks=false",
        "features.browser_use=false",
        "features.browser_use_external=false",
        "features.computer_use=false",
        "features.shell_snapshot=false",
        "features.remote_plugin=false",
    ):
        args += ["-c", setting]
    return args + ["-"]


def run_bounded(command, env, prompt, records, timeout):
    started = time.monotonic()
    timed_out = False
    interrupted = False
    termination_signal = None

    def terminate(signum, frame):
        nonlocal termination_signal
        termination_signal = signum
        raise KeyboardInterrupt

    with (
        (records / "trace.jsonl").open("w") as stdout,
        (records / "stderr.txt").open("w") as stderr,
    ):
        process = subprocess.Popen(
            command,
            env=env,
            stdin=subprocess.PIPE,
            stdout=stdout,
            stderr=stderr,
            text=True,
            start_new_session=True,
        )
        previous_handler = signal.signal(signal.SIGTERM, terminate)
        try:
            try:
                process.communicate(prompt, timeout=timeout)
            except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
                timed_out = isinstance(error, subprocess.TimeoutExpired)
                interrupted = not timed_out
                if interrupted and termination_signal is None:
                    termination_signal = signal.SIGINT
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.communicate()
        finally:
            signal.signal(signal.SIGTERM, previous_handler)
    return {
        "exit_code": process.returncode,
        "timed_out": timed_out,
        "interrupted": interrupted,
        "termination_signal": termination_signal,
        "elapsed_seconds": round(time.monotonic() - started, 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument(
        "--record", required=True, help="New raw-evidence directory name"
    )
    parser.add_argument("--prompt-file", type=Path)
    parser.add_argument("--codex-vendor", type=Path)
    parser.add_argument(
        "--auth",
        choices=("saved", "env"),
        default="saved",
        help="Saved CLI login (default), or an API key from the environment",
    )
    parser.add_argument(
        "--timeout", type=int, help="Orchestrator-supplied time limit in seconds"
    )
    parser.add_argument(
        "--access", choices=("read-only", "workspace-write"), required=True
    )
    parser.add_argument("--probe-only", action="store_true")
    args = parser.parse_args()
    if (
        not args.record
        or Path(args.record).name != args.record
        or args.record in (".", "..")
    ):
        parser.error("record must be a single directory name")
    if (args.timeout is not None and args.timeout <= 0) or (
        not args.probe_only and (not args.prompt_file or args.timeout is None)
    ):
        parser.error("Need a positive timeout and --prompt-file (unless --probe-only)")
    readonly = args.access == "read-only"
    run = args.run_dir.resolve()
    records = run / "records" / args.record
    records_created = False
    try:
        vendor = native_vendor(args.codex_vendor)
        command, env = sandbox(run, vendor, readonly, not args.probe_only, args.auth)
        records.mkdir(parents=True, exist_ok=False)
        records_created = True
        evidence = probe(command, env, run, readonly)
        save_json(records / "isolation.json", evidence)
        if args.probe_only:
            print(f"Isolation probe passed: {records}")
            return 0
        prompt = args.prompt_file.read_text()
        (records / "prompt.txt").write_text(prompt)
        # Each invocation receives an empty session-log directory. The
        # orchestrator can audit context without exposing earlier transcripts.
        sessions = records / "sessions"
        sessions.mkdir()
        runtime_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
        command += ["--bind", str(sessions), str(runtime_home / "sessions")]
        launch = command + codex_args(run / "project", readonly)
        save_json(
            records / "launch.json",
            {
                "command": launch,
                "timeout_seconds": args.timeout,
                "environment_names": sorted(env),
                "network": "shared with host",
            },
        )
        result = run_bounded(launch, env, prompt, records, args.timeout)
        save_json(records / "execution.json", result)
        print(f"Process evidence recorded: {records}")
        return (
            0
            if result["exit_code"] == 0
            and not result["timed_out"]
            and not result["interrupted"]
            else 1
        )
    except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        if records_created:
            save_json(records / "error.json", {"error": str(error)})
        print(f"Launch error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
