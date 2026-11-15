"""Run-owned captures and observations; Workjig still owns calls and retries."""
from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import shutil
import subprocess
import sys
import time
import uuid
from dataclasses import asdict
from pathlib import Path

from commonplace.headless.jobs import recorded_calls
from commonplace.lib.library import library_root
from commonplace.lib.review_workflows import result_contract

VERSION = 2


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(root: Path, name: str) -> Path:
    rel = Path(name)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise ValueError(f"unsafe captured path: {name}")
    path = root / rel
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"captured path escapes run: {name}")
    return path


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def git_head(root: Path) -> str | None:
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def library_files(root: Path | None = None) -> dict[str, str]:
    root = (root or library_root()).resolve()
    found = {}
    for parent, directories, files in os.walk(root):
        base = Path(parent)
        directories[:] = sorted(name for name in directories if not name.startswith(".")
                                and (base / name).relative_to(root).parts != ("reports", "state"))
        for name in directories:
            if (base / name).is_symlink():
                raise ValueError(f"library symlink requires explicit repair: {base / name}")
        for name in sorted(files):
            if name.startswith("."):
                continue
            path = base / name
            if path.is_symlink():
                raise ValueError(f"library symlink requires explicit repair: {path}")
            found[path.relative_to(root).as_posix()] = sha(path.read_bytes())
    return found


def content_state(root: Path) -> dict[str, dict]:
    """Lightweight reconstruction inventory, not an ambient operational-input capture."""
    changed = subprocess.run(["git", "diff", "--no-renames", "--name-only", "-z", "HEAD"], cwd=root,
                             capture_output=True, check=False).stdout
    untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=root,
                               capture_output=True, check=False).stdout
    found = {}
    for name in sorted(set((changed + untracked).decode("utf-8").split("\0")) - {""}):
        if name.startswith("kb/reports/state/"):
            continue
        path = safe_path(root, name)
        if path.is_symlink():
            found[name] = {"kind": "symlink", "target": str(path.readlink())}
        elif path.is_file():
            found[name] = {"kind": "file", "sha256": sha(path.read_bytes())}
        elif not path.exists():
            found[name] = {"kind": "deleted"}
        else:
            raise ValueError(f"cannot inventory changed content: {name}")
    return found


def code_files() -> dict[str, str]:
    package = Path(__file__).resolve().parents[2]
    return {path.relative_to(package).as_posix(): sha(path.read_bytes())
            for path in sorted(package.rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"}


def package_versions() -> dict[str, str]:
    return {"python": sys.version, **{dist.metadata["Name"]: dist.version
                                    for dist in importlib.metadata.distributions() if dist.metadata["Name"]}}


def executor(run) -> dict:
    harness = run.harnesses[run.profile.harness]
    executable = shutil.which(harness.executable)
    versions = package_versions()
    reported_version = None
    if executable:
        try:
            reported = subprocess.run([executable, "--version"], capture_output=True, text=True,
                                      check=False, timeout=10)
            if reported.returncode == 0:
                reported_version = reported.stdout.strip()[:500]
        except (OSError, subprocess.TimeoutExpired):
            pass
    return {"packages": versions, "source": str(Path(__file__).resolve()), "code": code_files(),
            "executable": executable, "reported-version": reported_version,
            "executable-sha256": sha(Path(executable).read_bytes()) if executable else None,
            "effective-configuration": "unassessed", "gaps": ["automatically loaded context and provider internals not verified"]}


def load(directory: Path) -> dict:
    data = json.loads((directory / "observation.json").read_text())
    try:
        if data["version"] != VERSION or data["id"] != sha(json.dumps(data["request"], sort_keys=True).encode())[:24]:
            raise ValueError("unsupported or inconsistent observation identity")
        if set(data["completed-results"]) != set(data["completed-result-sha256"]):
            raise ValueError("completed-result manifest is inconsistent")
        for item in data["inputs"]:
            if sha(safe_path(directory, item["path"]).read_bytes()) != item["sha256"]:
                raise ValueError(f"captured input changed: {item['path']}")
        for name, digest in data["completed-result-sha256"].items():
            if sha(safe_path(directory, name).read_bytes()) != digest:
                raise ValueError(f"retained completed result changed: {name}")
    except (KeyError, TypeError, AttributeError) as error:
        raise ValueError(f"malformed observation manifest: {directory}") from error
    return data


def begin(run, root: Path, pair, note: str, criterion: str, contracts: dict[str, bytes], prompt: str, call_job: str,
          call_inputs: dict[str, str], operational_inputs: dict[str, dict[str, str]]) -> tuple[Path, dict]:
    request = {"job": pair.job, "call-job": call_job, "note": pair.note, "criterion": pair.criterion, "contract": pair.contract,
               "kind": pair.kind, "criterion-id": pair.criterion_id,
               "target-sha256": sha(note.encode()), "criterion-bytes-sha256": sha(criterion.encode()),
               "contract-sha256": result_contract.fingerprint(contracts), "prompt-sha256": sha(prompt.encode()),
               "profile": asdict(run.profile), "timeout": run.timeout,
               "call-inputs": {name + ".md": sha(value.encode()) for name, value in call_inputs.items()}}
    identity = sha(json.dumps(request, sort_keys=True).encode())[:24]
    directory = run.artifact / "reviews" / identity
    record = directory / "observation.json"
    if record.exists():
        data = load(directory)
        if data["request"] != request:
            raise ValueError(f"observation identity collision: {record}")
        return directory, data
    directory.mkdir(parents=True, exist_ok=True)
    captures = {f"inputs/target/{pair.note}": ("target", pair.note, note.encode()),
                "inputs/criterion.md": ("criterion", pair.criterion, criterion.encode()),
                "inputs/prompt.txt": ("prompt", "controller", prompt.encode()),
                **{f"inputs/operational/{name}.md": ("operational", item["origin"], item["text"].encode())
                   for name, item in operational_inputs.items()},
                **{f"inputs/contract/{name}": ("contract", name, value) for name, value in contracts.items()}}
    entries = []
    for name, (role, origin, value) in captures.items():
        path = safe_path(directory, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)
        entries.append({"role": role, "origin": origin, "path": name, "sha256": sha(value), "bytes": len(value)})
    data = {"version": VERSION, "id": identity, "request": request, "kb-commit": git_head(root),
            "content-state": content_state(root),
            "library-root": str(getattr(run, "library_root", None) or library_root()),
            "library-sha256": sha(json.dumps(library_files(getattr(run, "library_root", None)), sort_keys=True).encode()),
            "context": "live authored KB; operational inputs confined to this run", "inputs": entries,
            "executor": executor(run), "state": "prepared", "completed-results": [], "completed-result-sha256": {}}
    atomic_json(record, data)
    return directory, data


def refresh(run, directory: Path, data: dict, *, state: str) -> None:
    data["state"] = state
    index = json.loads((run.root / "calls/run.json").read_text()) if (run.root / "calls/run.json").exists() else {"calls": {}}
    data["calls"] = []
    for call in recorded_calls(run.root):
        if call["job"] != data["request"]["call-job"]:
            continue
        given = index["calls"][call["call"]][call["key"]]["request"]["inputs"]
        if {name: sha(value.encode()) for name, value in given.items()} == data["request"]["call-inputs"]:
            data["calls"].append(call)
    keys = {call["key"] for call in data["calls"]}
    events = []
    log = run.root / "log.jsonl"
    if log.exists():
        for line in log.read_text().splitlines():
            event = json.loads(line)
            if event.get("key") in keys and event.get("event") in ("rejected", "failed", "stopped-call"):
                events.append(event)
    data["diagnostics"] = events
    data["launch-evidence"] = []
    for call in data["calls"]:
        for launch in call["launches"]:
            path = run.root / "calls/launches" / launch / "stdout.log"
            if not path.exists():
                continue
            for line in path.read_text(errors="replace").splitlines():
                try:
                    event = json.loads(line)
                except ValueError:
                    continue
                if isinstance(event, dict) and event.get("type") == "system" and event.get("subtype") == "init":
                    data["launch-evidence"].append({"launch": launch, "source": str(path.relative_to(run.root)),
                        "tools": event.get("tools"), "model": event.get("model"),
                        "mcp": [{key: server.get(key) for key in ("name", "status")}
                                for server in event.get("mcp_servers", []) if isinstance(server, dict)]})
    data["content-rejections"] = len({event["key"] for event in events if event["event"] == "rejected"})
    data["rejection-events"] = sum(event["event"] == "rejected" for event in events)
    atomic_json(directory / "observation.json", data)


def timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
