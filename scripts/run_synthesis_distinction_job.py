"""Run one prepared synthesis-distinction packet in an isolated Codex session."""

import argparse
import hashlib
import json
import os
import shutil
import signal
import subprocess
import time
from pathlib import Path

MODEL = "gpt-6-luna"
EFFORT = "medium"
TIME_LIMIT_SECONDS = 1800
TOKEN_LIMIT = 1_000_000


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vendor_path():
    executable = shutil.which("codex")
    if not executable:
        raise RuntimeError("codex is unavailable")
    package = Path(executable).resolve().parent.parent
    matches = list(package.glob("node_modules/@openai/codex-*/vendor/*/bin/codex"))
    if len(matches) != 1:
        raise RuntimeError("Cannot find one native Codex vendor")
    return matches[0].parent.parent


def sandbox_command(packet, records):
    if not shutil.which("bwrap"):
        raise RuntimeError("bubblewrap is unavailable")
    home = Path.home()
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex"))
    if codex_home != home / ".codex":
        raise RuntimeError("This launcher requires the default CODEX_HOME")
    auth = codex_home / "auth.json"
    if not auth.is_file():
        raise RuntimeError("Saved Codex authentication is unavailable")
    vendor = vendor_path()
    command = [
        "bwrap", "--unshare-user", "--unshare-pid", "--unshare-ipc",
        "--unshare-uts", "--die-with-parent", "--new-session",
        "--ro-bind", "/usr", "/usr",
    ]
    for name in ("bin", "sbin", "lib", "lib64"):
        path = Path("/") / name
        if path.is_symlink():
            command += ["--symlink", os.readlink(path), str(path)]
        elif path.is_dir():
            command += ["--ro-bind", str(path), str(path)]
    command += [
        "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--dir", "/etc", "--dir", "/etc/ssl",
        "--dir", "/home", "--dir", str(home),
        "--dir", str(codex_home), "--dir", "/opt", "--dir", "/work",
    ]
    for name in ("resolv.conf", "hosts", "nsswitch.conf", "passwd", "group", "ssl/certs"):
        path = Path("/etc") / name
        if path.exists():
            command += ["--ro-bind", str(path), str(path)]
    command += [
        "--ro-bind", str(vendor), "/opt/codex",
        "--ro-bind", str(auth), str(auth),
        "--bind", str(records / "sessions"), str(codex_home / "sessions"),
        "--bind", str(packet), "/work",
        "--ro-bind", str(packet / "inputs"), "/work/inputs",
        "--ro-bind", str(packet / "prompt.txt"), "/work/prompt.txt",
        "--chdir", "/work",
        "--setenv", "HOME", str(home),
        "--setenv", "CODEX_HOME", str(codex_home),
        "--setenv", "PATH", "/opt/codex/bin:/usr/bin:/bin",
        "--", "/opt/codex/bin/codex", "--no-daemon", "-a", "never",
        "exec", "--ignore-user-config", "--ignore-rules", "--ephemeral",
        "--skip-git-repo-check", "--strict-config", "--json", "-C", "/work",
        "--sandbox", "workspace-write", "--model", MODEL,
        "-c", f'model_reasoning_effort="{EFFORT}"',
    ]
    for setting in (
        "memories.use_memories=false", "memories.generate_memories=false",
        "features.memories=false", "features.apps=false",
        "features.plugins=false", "features.hooks=false",
        "features.browser_use=false", "features.browser_use_external=false",
        "features.computer_use=false", "features.shell_snapshot=false",
        "features.remote_plugin=false",
        'shell_environment_policy.exclude=["CODEX_API_KEY","OPENAI_API_KEY"]',
    ):
        command += ["-c", setting]
    return command + ["-"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", required=True, type=Path)
    parser.add_argument("--records", required=True, type=Path)
    parser.add_argument("--probe-only", action="store_true")
    args = parser.parse_args()
    packet = args.packet.resolve(strict=True)
    records = args.records.resolve()
    if not packet.is_dir() or packet.is_symlink():
        parser.error("packet must be a real directory")
    manifest = packet.with_name(packet.name + ".manifest.json")
    declared = json.loads(manifest.read_text())
    for name, expected in declared["files"].items():
        path = packet / name
        if sha256(path) != expected:
            raise ValueError(f"Packet input changed: {name}")
    if any((packet / name).exists() for name in ("output.md", "problem.md")):
        raise FileExistsError("Packet already has an output or problem report")
    records.mkdir(parents=True, exist_ok=False)
    (records / "sessions").mkdir()
    command = sandbox_command(packet, records)
    if args.probe_only:
        probe = command[: command.index("--chdir")]
        probe_code = (
            "import os,pathlib,subprocess,sys; p=pathlib.Path('/work'); "
            "assert (p/'inputs').is_dir(); "
            "assert not pathlib.Path(sys.argv[1]).exists(); "
            "assert not os.access(p/'inputs', os.W_OK); "
            "assert pathlib.Path.home().joinpath('.codex/auth.json').is_file(); "
            "assert subprocess.run(['/opt/codex/bin/codex','--version'], "
            "capture_output=True).returncode == 0"
        )
        probe += ["--chdir", "/work", "--", "/usr/bin/python3", "-c",
                  probe_code, str(Path(__file__).resolve().parents[1])]
        subprocess.run(probe, check=True)
        print(f"Isolation probe passed: {records}")
        return
    (records / "launch.json").write_text(json.dumps({
        "model": MODEL, "effort": EFFORT,
        "time_limit_seconds": TIME_LIMIT_SECONDS,
        "token_limit": TOKEN_LIMIT,
        "packet": str(packet), "manifest_sha256": sha256(manifest),
        "codex_version": subprocess.run(["codex", "--version"], capture_output=True,
                                        text=True, check=True).stdout.strip(),
        "command": command,
    }, indent=2) + "\n")
    started = time.monotonic()
    with (records / "trace.jsonl").open("wb") as trace, (records / "stderr.txt").open("wb") as errors:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=trace,
                                   stderr=errors, start_new_session=True)
        try:
            process.communicate((packet / "prompt.txt").read_bytes(),
                                timeout=TIME_LIMIT_SECONDS)
            timed_out = False
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.communicate()
            timed_out = True
    usage = []
    for line in (records / "trace.jsonl").read_text(errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed":
            usage.append(event.get("usage", {}))
    total = sum(value for item in usage for key, value in item.items()
                if key in ("input_tokens", "output_tokens") and isinstance(value, int))
    (records / "result.json").write_text(json.dumps({
        "exit_code": process.returncode, "timed_out": timed_out,
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "reported_tokens": total, "token_limit_exceeded": total > TOKEN_LIMIT,
        "usage": usage,
        "outputs": {name: sha256(packet / name) for name in ("output.md", "problem.md")
                    if (packet / name).is_file()},
        "inputs_unchanged": all(sha256(packet / name) == expected
                                for name, expected in declared["files"].items()),
    }, indent=2) + "\n")
    print(records / "result.json")
    if (process.returncode or timed_out or total > TOKEN_LIMIT or not usage or
            not any((packet / name).is_file() for name in ("output.md", "problem.md"))):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
