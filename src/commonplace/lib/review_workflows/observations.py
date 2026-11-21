"""Review semantics over Workjig-owned execution evidence.

Inputs and tasks are read through Workjig's validated view, never copied into
observations. Executor provenance is immutable and shared within a run.
Fixtures are explicit independent exports, not a second live input authority.
"""
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

from workjig import read_run

from commonplace.headless.jobs import CALLS, recorded_calls
from commonplace.lib.library import library_root
from commonplace.lib.review_workflows import result_contract

VERSION = 3
# BACKCOMPAT: retained v2 runs contain unique evidence - remove after their retirement.
READ_VERSIONS = (2, VERSION)
LIBRARY_POLICY = "git-visible-or-installed-v1"
FAMILIES = ("reviews", "edits")
"""The directories under a run's `artifact/` that hold observations: review and edit executions."""


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


def _json_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    tmp.write_bytes(_json_bytes(value))
    tmp.replace(path)


def git_head(root: Path) -> str | None:
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def library_files(root: Path | None = None, *, use_git: bool = True) -> dict[str, str]:
    """Inventory authored files, not ignored ambient data.

    Git libraries include tracked and non-ignored untracked files. Installed
    libraries without Git use visible package files. Hidden paths and report
    state are excluded in both cases. Reconstruction checks disable Git because
    the new tree may be inside its parent's ignored state directory.
    """
    root = (root or library_root()).resolve()
    eligible = None
    parents = set()
    if use_git:
        probe = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=root,
                               capture_output=True, check=False)
        if probe.returncode == 0 and probe.stdout.strip() == b"true":
            listed = subprocess.run(["git", "ls-files", "-z", "--cached", "--others",
                                     "--exclude-standard", "--", "."], cwd=root,
                                    capture_output=True, check=True).stdout
            eligible = {os.fsdecode(name) for name in listed.split(b"\0") if name}
            parents = {parent.as_posix() for name in eligible for parent in Path(name).parents}
        elif any(marker.is_file() or (marker.is_dir() and any(marker.iterdir()))
                 for marker in (parent / ".git" for parent in (root, *root.parents))):
            # Empty .git directories can be discovery barriers, not repositories.
            # A real but unreadable/untrusted repository must not fall back to
            # capturing ignored files as if this were an installed library.
            raise ValueError(f"cannot determine Git library boundary: {root}")
    found = {}
    for parent, directories, files in os.walk(root):
        base = Path(parent)
        directories[:] = sorted(name for name in directories if not name.startswith(".")
                                and (base / name).relative_to(root).parts != ("reports", "state")
                                and (eligible is None or (base / name).relative_to(root).as_posix() in parents
                                     or (base / name).relative_to(root).as_posix() in eligible))
        for name in directories:
            if (base / name).is_symlink():
                raise ValueError(f"library symlink requires explicit repair: {base / name}")
        for name in sorted(files):
            path = base / name
            if name.startswith(".") or (eligible is not None and path.relative_to(root).as_posix() not in eligible):
                continue
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


def prepare(run) -> dict:
    """Hash the library once per open Run, before concurrent assessments.

    Reopening a run recomputes this baseline: there is no cross-process cache
    that could conceal changed library content or executable versions.
    """
    if not hasattr(run, "_review_provenance"):
        selected = getattr(run, "library_root", None) or library_root()
        value = executor(run)
        digest = sha(_json_bytes(value))
        name = f"provenance/{digest}.json"
        path = safe_path(run.root, name)
        if path.exists():
            if sha(path.read_bytes()) != digest:
                raise ValueError(f"executor provenance changed: {path}")
        else:
            atomic_json(path, value)
        run._review_provenance = {
            "library-root": str(selected),
            "library-policy": LIBRARY_POLICY,
            "library-sha256": sha(json.dumps(library_files(selected), sort_keys=True).encode()),
            "executor": {"path": name, "sha256": digest},
        }
    return run._review_provenance


def run_root(directory: Path) -> Path:
    if directory.parent.name not in FAMILIES or directory.parent.parent.name != "artifact":
        raise ValueError(f"not a run observation directory: {directory}")
    return directory.parents[2]


def executor_record(directory: Path, data: dict) -> dict:
    if data["version"] == 2:
        return data["executor"]
    reference = data["executor"]
    path = safe_path(run_root(directory), reference["path"])
    raw = path.read_bytes()
    if sha(raw) != reference["sha256"]:
        raise ValueError(f"executor provenance changed: {path}")
    return json.loads(raw)


def read_inputs(directory: Path, data: dict | None = None) -> dict[str, bytes]:
    """Resolve logical export paths from their sole owner, with exact-byte checks.

    `path` is the name used when exporting an independent fixture, not a file
    that a caller should open under the observation directory.
    """
    data = data if data is not None else json.loads((directory / "observation.json").read_bytes())
    if data["version"] not in READ_VERSIONS:
        raise ValueError("unsupported observation version")
    if data["version"] == 2:
        values = {item["path"]: safe_path(directory, item["path"]).read_bytes() for item in data["inputs"]}
    else:
        root = run_root(directory)
        safe_path(root, f"{CALLS}/run.json")
        view = read_run(safe_path(root, CALLS))
        request = data["request"]
        matches = [call for call in view.calls if
                   call.call_id.partition("#")[0] == request["call-job"]
                   and {name: sha(value.encode()) for name, value in call.inputs.items()} == request["call-inputs"]
                   and sha(call.task.encode()) == request["prompt-sha256"]] if view else []
        if not matches:
            raise ValueError(f"Workjig input evidence unavailable: {directory}")
        call = matches[0]
        values = {item["path"]: (call.task if item["role"] == "prompt" else call.inputs[item["input"]]).encode()
                  for item in data["inputs"]}
    for item in data["inputs"]:
        if sha(values[item["path"]]) != item["sha256"]:
            raise ValueError(f"captured input changed: {item['path']}")
    return values


def load(directory: Path) -> dict:
    data = json.loads((directory / "observation.json").read_bytes())
    try:
        if data["version"] not in READ_VERSIONS or data["id"] != sha(json.dumps(data["request"], sort_keys=True).encode())[:24]:
            raise ValueError("unsupported or inconsistent observation identity")
        if set(data["completed-results"]) != set(data["completed-result-sha256"]):
            raise ValueError("completed-result manifest is inconsistent")
        executor_record(directory, data)
        # Preparation or interruption can precede Workjig's first durable call.
        # Recorded calls/results must never silently lose their input evidence.
        if data["version"] == 2 or data.get("calls") or data["completed-results"]:
            read_inputs(directory, data)
        for name, digest in data["completed-result-sha256"].items():
            if sha(safe_path(directory, name).read_bytes()) != digest:
                raise ValueError(f"retained completed result changed: {name}")
    except (KeyError, TypeError, AttributeError) as error:
        raise ValueError(f"malformed observation manifest: {directory}") from error
    return data


def find(run_artifact: Path, observation: str) -> Path:
    """The directory of a run's observation, whichever family holds it."""
    for family in FAMILIES:
        directory = safe_path(run_artifact / family, observation)
        if (directory / "observation.json").is_file():
            return directory
    raise ValueError(f"no observation {observation} in {run_artifact}")


def begin(run, root: Path, pair, note: str, criterion: str, contracts: dict[str, bytes], prompt: str, call_job: str,
          call_inputs: dict[str, str], operational_inputs: dict[str, dict[str, str]],
          *, criterion_input: str, family: str = "reviews", profile=None) -> tuple[Path, dict]:
    """Index one execution's inputs under `artifact/<family>/<identity>`, or find it on replay.

    `profile` is the call's own profile when it differs from the run's.
    """
    request = {"job": pair.job, "call-job": call_job, "note": pair.note, "criterion": pair.criterion, "contract": pair.contract,
               "kind": pair.kind, "criterion-id": pair.criterion_id,
               "target-sha256": sha(note.encode()), "criterion-bytes-sha256": sha(criterion.encode()),
               "contract-sha256": result_contract.fingerprint(contracts), "prompt-sha256": sha(prompt.encode()),
               "profile": asdict(profile or run.profile), "timeout": run.timeout,
               "call-inputs": {name + ".md": sha(value.encode()) for name, value in call_inputs.items()}}
    identity = sha(json.dumps(request, sort_keys=True).encode())[:24]
    directory = run.artifact / family / identity
    record = directory / "observation.json"
    if record.exists():
        data = load(directory)
        if data["request"] != request:
            raise ValueError(f"observation identity collision: {record}")
        return directory, data
    directory.mkdir(parents=True, exist_ok=True)
    captures = {f"inputs/target/{pair.note}": ("target", pair.note, note.encode(),
                                            "note" if family == "reviews" else "text"),
                "inputs/criterion.md": ("criterion", pair.criterion, criterion.encode(), criterion_input),
                "inputs/prompt.txt": ("prompt", "controller", prompt.encode(), None),
                **{f"inputs/operational/{name}.md": ("operational", item["origin"], item["text"].encode(),
                                                    f"supplied-{name}" if family == "reviews" else name)
                   for name, item in operational_inputs.items()},
                **{f"inputs/contract/{name}": ("contract", name, value, f"output-contract-{index}")
                   for index, (name, value) in enumerate(sorted(contracts.items()))}}
    entries = []
    for name, (role, origin, value, given) in captures.items():
        if given is not None and call_inputs[given].encode() != value:
            raise ValueError(f"observation input differs from Workjig request: {name}")
        entries.append({"role": role, "origin": origin, "path": name, "sha256": sha(value), "bytes": len(value),
                        **({"input": given + ".md"} if given is not None else {})})
    data = {"version": VERSION, "id": identity, "request": request, "kb-commit": git_head(root),
            "content-state": content_state(root),
            **prepare(run),
            "context": "live authored KB; operational inputs confined to this run; library baseline at controller start",
            "inputs": entries, "state": "prepared", "completed-results": [], "completed-result-sha256": {}}
    atomic_json(record, data)
    return directory, data


def refresh(run, directory: Path, data: dict, *, state: str) -> None:
    data["state"] = state
    calls = recorded_calls(run.root)
    view = read_run(run.root / CALLS)      # read second: it holds at least every call listed above
    recorded = {(call.call_id, call.request_hash): call for call in view.calls} if view is not None else {}
    data["calls"] = []
    for call in calls:
        if call["job"] != data["request"]["call-job"]:
            continue
        given = recorded[call["call"], call["key"]].inputs
        if {name: sha(value.encode()) for name, value in given.items()} == data["request"]["call-inputs"]:
            # Workjig owns status, attempts and launches; retain only foreign keys.
            data["calls"].append({"call": call["call"], "key": call["key"]})
    keys = {call["key"] for call in data["calls"]}
    events = []
    log = run.root / "log.jsonl"
    if log.exists():
        for line in log.read_text().splitlines():
            event = json.loads(line)
            if ((event.get("key") in keys and event.get("event") in ("rejected", "failed", "stopped-call", "no-progress"))
                    or (event.get("job") == data["request"]["call-job"] and event.get("event") == "controller-error")):
                events.append(event)
    data["diagnostics"] = events
    # Native/Workjig traces own launch context. Do not create another mutable
    # projection here; leave any historical v2 launch evidence untouched.
    data["content-rejections"] = len({event["key"] for event in events if event["event"] == "rejected"})
    data["rejection-events"] = sum(event["event"] == "rejected" for event in events)
    atomic_json(directory / "observation.json", data)


def timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
