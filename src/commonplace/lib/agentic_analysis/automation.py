"""Command-owned preparation, execution, reporting and bounded analysis queues.

Statuses are orchestration receipts, not another authority over worker liveness.
Only the pinned child reads its workflow/Workjig state. Effect intents are saved
before subprocesses; uncertain effects never cause replacement allocations.
"""

from __future__ import annotations

import json
import math
import os
import re
import signal
import subprocess
import threading
import uuid
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

from commonplace.lib.agentic_analysis.analyses import (
    WORKER_PROFILES,
    resolve_worker_profile,
)
from commonplace.lib.agentic_analysis.durable import lease, save
from commonplace.lib.agentic_analysis.execution import outcome
from commonplace.lib.agentic_analysis.preparation import (
    command_environment,
    draining_commands,
    preparation_for,
    prepare_worktree,
    run_command,
    select_method,
)
from commonplace.lib.agentic_analysis.run_ids import is_commit
from commonplace.lib.agentic_analysis.sources import github_checkout_path
from commonplace.lib.source_identity import normalize_source_identity

SCHEMA = "commonplace.analysis-controller.v1"
REMOTE = re.compile(r"^(?:https?://[^/\s?#]+/|ssh://[^/\s?#]+/|git@[^:\s]+:)[^/\s?#]+/[^/\s?#]+/?$")
FINAL = {"published", "local-complete"}
PAUSE = {"operator-attention", "command-failed", "preparation-failed"}


def source_identity(value: str) -> str:
    identity = normalize_source_identity(value)
    github = re.fullmatch(r"(?:git@github\.com:|(?:https?|ssh)://(?:git@)?github\.com/)([^/]+)/([^/]+)",
                          identity, flags=re.IGNORECASE)
    return f"https://github.com/{github[1]}/{github[2]}".lower() if github else identity


def target(data: dict) -> dict:
    """Validate intake without acquiring anything; retain explicit non-Git routes."""
    allowed = {"source", "source-kind", "system", "source-identity", "source-revision"}
    if not isinstance(data, dict) or set(data) - allowed:
        raise ValueError("target must be an object with source, source-kind, system, source-identity, source-revision only")
    for key, value in data.items():
        if not isinstance(value, str) or not value.strip() or any(c in value for c in "\r\n\x00"):
            raise ValueError(f"{key} must be nonempty single-line text")
    source = data.get("source", "").strip()
    kind = data.get("source-kind", "repository")
    if kind == "repository":
        if not REMOTE.fullmatch(source):
            raise ValueError("provide a repository root locator, or explicitly select --source-kind local/documents")
        identity = source_identity(data.get("source-identity", source))
        if identity != source_identity(source):
            raise ValueError("repository source-identity must agree with its normalized locator")
        system = data.get("system", normalize_source_identity(source).rsplit("/", 1)[-1])
    elif kind == "local":
        path = Path(source).expanduser().resolve()
        if not source or not path.exists():
            raise ValueError("local source must name an existing checkout, snapshot or bundle")
        source = str(path)
        identity = source_identity(data.get("source-identity", path.as_uri()))
        system = data.get("system", path.name)
    elif kind == "documents":
        if not source or not data.get("system") or not data.get("source-identity"):
            raise ValueError("documents require explicit source, system and source-identity")
        identity = source_identity(data["source-identity"])
        system = data["system"]
    else:
        raise ValueError("source-kind must be repository, local or documents")
    if not identity or not system.strip():
        raise ValueError("source identity and system must not be empty")
    revision = data.get("source-revision")
    if revision is not None and (not is_commit(revision) or github_checkout_path(identity) is None):
        raise ValueError("source-revision requires a full 40-hex commit and GitHub repository identity")
    return {"source": source, "source-kind": kind, "source-identity": identity,
            "system": system, **({"source-revision": revision} if revision is not None else {})}


def targets_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if text.lstrip().startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise ValueError("batch input must be a JSON list")
    else:
        data = [{"source": line.strip()} for line in text.splitlines() if line.strip()]
    return validate_targets(data)


def validate_targets(data: list[dict]) -> list[dict]:
    targets = [target(item) for item in data]
    identities = [item["source-identity"] for item in targets]
    if not targets or len(set(identities)) != len(identities):
        raise ValueError("batch needs at least one target and no duplicate normalized source identities")
    return targets


def limits(concurrency: int, max_workers: int, timeout: float) -> None:
    if concurrency < 1 or max_workers < 1 or not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("concurrency, max-workers and timeout must be positive finite values")
    if os.name != "posix":
        raise ValueError("analysis automation requires POSIX file locks")


def create(origin: Path, targets: list[dict], *, profile: str, revision: str | None,
           state: Path | None, worktree_root: Path | None, concurrency: int,
           max_workers: int, timeout: float, require_clean_origin: bool) -> Path:
    targets = validate_targets(targets)
    limits(concurrency, max_workers, timeout)
    origin, commit = select_method(origin, revision)
    run_command(["git", "cat-file", "-e", f"{commit}:src/commonplace/lib/agentic_analysis/execution.py"], cwd=origin)
    profiles = run_command(["git", "show", f"{commit}:kb/{WORKER_PROFILES}"], cwd=origin).encode()
    resolve_worker_profile(profiles, profile)
    if require_clean_origin and run_command(["git", "status", "--porcelain", "--untracked-files=all"], cwd=origin):
        raise ValueError("origin has uncommitted changes; --require-clean-origin requires a clean checkout")
    state = (state or origin / ".commonplace/worktrees/controllers" / uuid.uuid4().hex).resolve()
    root = (worktree_root or origin / ".commonplace/worktrees").resolve()
    if state.exists():
        raise ValueError(f"controller destination already exists; use resume/report: {state}")
    items = []
    for source in targets:
        key = uuid.uuid4().hex
        label = re.sub(r"[^a-z0-9]+", "-", source["system"].lower()).strip("-")[:60] or "system"
        items.append({"target": source, "key": key, "label": label, "status": "pending",
                      "phase": "pending", "worktree": str(root / f"{label}-{key[:12]}"),
                      "run": None, "result": None, "error": None})
    record = {"schema": SCHEMA, "controller": str(state), "origin": str(origin), "method-commit": commit,
              "worker-profile": profile, "concurrency": concurrency, "max-workers": max_workers,
              "maximum-role-workers": concurrency * max_workers, "timeout": timeout,
              "require-clean-origin": require_clean_origin, "targets": items}
    state.mkdir(parents=True, exist_ok=False)
    save(state / "controller.json", record)
    return state


def report(state: Path) -> dict:
    state = state.resolve()
    record = json.loads((state / "controller.json").read_text())
    if record.get("schema") != SCHEMA or record.get("controller") != str(state):
        raise ValueError("controller schema or location differs from its binding")
    return {**record, "counts": dict(Counter(item["status"] for item in record["targets"]))}


def exit_code(record: dict) -> int:
    statuses = {item["status"] for item in record["targets"]}
    if statuses & {"pending", "active", "operator-attention"}:
        return 3
    if statuses & {"command-failed", "preparation-failed"}:
        return 1
    return 2 if "stopped" in statuses else 0


class Controller:
    def __init__(self, state: Path):
        self.state = state.resolve()
        self.record = report(self.state)
        self.record.pop("counts")
        self.guard = threading.Lock()
        self.halt = threading.Event()

    def update(self, item: dict, **changes) -> None:
        with self.guard:
            if changes.get("status") in PAUSE:
                self.halt.set()
            item.update(changes)
            save(self.state / "controller.json", self.record)

    def child(self, item: dict, args: list[str], fd: int, *, probe: bool = False) -> subprocess.CompletedProcess:
        tree = Path(item["worktree"])
        commands = Path(str(preparation_for(tree)["path-prefix"]))
        argv = [str(commands / "commonplace-analysis"), *args]
        kwargs = {"cwd": tree, "env": command_environment(tree),
                  "start_new_session": True, "pass_fds": (fd,), "text": True}
        if probe:
            return subprocess.run(argv, capture_output=True, check=False, **kwargs)
        # Child stdout is evidence, never the allocation protocol. Keep logs
        # across explicit resumes; inspect-execution is the structured API.
        with (self.state / f"{item['key']}.stdout.log").open("a") as out, (
                self.state / f"{item['key']}.stderr.log").open("a") as err:
            return subprocess.run(argv, stdout=out, stderr=err, check=False, **kwargs)

    def probe(self, item: dict, fd: int) -> dict:
        response = self.child(item, ["inspect-execution", item["key"]], fd, probe=True)
        if response.returncode:
            raise ValueError(f"pinned inspection failed: {response.stderr.strip()}")
        data = json.loads(response.stdout)
        allocation = data["allocation"]
        if allocation is not None:
            expected = self.parameters(item)
            actual = allocation["parameters"]
            if (allocation["method-commit"] != self.record["method-commit"]
                    or any(actual.get(k.replace("_", "-")) != v for k, v in expected.items())):
                raise ValueError("discovered allocation differs from the controller binding")
            self.update(item, run=str(Path(item["worktree"]) / "kb/agentic-system-analyses/state" / allocation["run-id"]))
        return data

    def parameters(self, item: dict) -> dict:
        data = item["target"]
        return {"system": data["system"], "source_identity": data["source-identity"], "source": data["source"],
                "worker_profile": self.record["worker-profile"],
                **({"source_revision": data["source-revision"]} if "source-revision" in data else {})}

    def reconcile(self, item: dict, fd: int) -> None:
        if item["phase"] == "pending":
            return
        tree = Path(item["worktree"])
        preparation = preparation_for(tree)
        if preparation["commit"] != self.record["method-commit"]:
            raise ValueError("preparation differs from the controller method")
        if item["phase"] == "preparing":
            self.update(item, phase="prepared", status="pending", preparation=preparation)
            return
        if item["phase"] == "prepared":
            self.update(item, status="pending")
            return
        data = self.probe(item, fd)
        view, result = data["inspection"], data["result"]
        if view is None:
            # The intent may precede allocation, or allocation may precede its
            # parameters. Neither establishes that the old command settled.
            raise ValueError("execution intent has no inspectable run; preserve allocation evidence for the operator")
        status = outcome(view)
        if result is not None and result["inspection"] == view:
            status = result["status"]
        if status == "allocated":
            status = "operator-attention"
        self.update(item, status=status, result={"inspection": view, "execution": result},
                    error=None if status in FINAL else view.get("stopped"))

    def work(self, item: dict) -> None:
        try:
            with lease(self.state / "leases" / item["key"]) as fd:
                if item["phase"] == "pending":
                    self.update(item, status="active", phase="preparing")
                    with draining_commands():
                        preparation = prepare_worktree(
                            Path(self.record["origin"]), name=item["label"], revision=self.record["method-commit"],
                            worktree=Path(item["worktree"]), require_clean_origin=self.record["require-clean-origin"],
                        )
                    self.update(item, phase="prepared", preparation=preparation)
                if self.halt.is_set():
                    self.update(item, status="pending")
                    return
                self.update(item, phase="executing", status="active", error=None)
                args = ["execute", item["key"], "--timeout", str(self.record["timeout"]),
                        "--max-workers", str(self.record["max-workers"])]
                for name, value in self.parameters(item).items():
                    args.extend(["--" + name.replace("_", "-"), value])
                response = self.child(item, args, fd)
                data = self.probe(item, fd)
                if data["result"] is None:
                    raise ValueError(f"child exited {response.returncode} without a durable execution result")
                self.reconcile(item, fd)
        except Exception as error:  # noqa: BLE001 - retain failures and drain other owned children
            self.update(item, status="preparation-failed" if item["phase"] == "preparing" else "operator-attention",
                        error=f"{type(error).__name__}: {error}")
        if item["status"] in PAUSE:
            self.halt.set()

    def run(self, *, selected: list[str] = ()) -> dict:
        with lease(self.state / ".controller.lock"):
            self.record = report(self.state)
            self.record.pop("counts")
            known = {item["target"]["source-identity"] for item in self.record["targets"]}
            if set(selected) - known:
                raise ValueError("--target must match a recorded normalized source identity")
            # Reconcile every old effect before claiming even one pending target.
            reconciled = set()
            for item in self.record["targets"]:
                try:
                    with lease(self.state / "leases" / item["key"]) as fd:
                        self.reconcile(item, fd)
                        reconciled.add(item["key"])
                except Exception as error:  # noqa: BLE001 - missing ownership is an explicit stop
                    self.update(item, status="operator-attention", error=str(error))
            # Explicit selection may resume a discovered, settled allocation;
            # never acknowledge unsettled workers or retry preparation failures.
            for item in self.record["targets"]:
                view = (item.get("result") or {}).get("inspection") or {}
                audit = view.get("advisory-audit") or {}
                safe = (view.get("state") in ("allocated", "interrupted", "stopped")
                        and (not view.get("uncertain") or view.get("stop-type") == "UncertainLaunchError")
                        and not view.get("unsettled-launches")
                        and view.get("stop-type") not in ("UncertainEffectError", "AcquisitionUncertainError", "RecordError")
                        and not audit.get("unsettled-launches")
                        and audit.get("state") not in ("running", "interrupted"))
                if item["key"] in reconciled and item["target"]["source-identity"] in selected and safe:
                    self.update(item, status="pending")
            if any(item["status"] in PAUSE for item in self.record["targets"]):
                return report(self.state)
            self.halt.clear()  # reconciliation/explicit selection resolved every prior pause
            queue = [item for item in self.record["targets"] if item["status"] == "pending"]
            old = {}
            if threading.current_thread() is threading.main_thread():
                for signum in (signal.SIGINT, signal.SIGTERM):
                    old[signum] = signal.signal(signum, lambda *_: self.halt.set())
            try:
                with ThreadPoolExecutor(max_workers=self.record["concurrency"]) as pool:
                    active = set()
                    while active or (queue and not self.halt.is_set()):
                        while queue and len(active) < self.record["concurrency"] and not self.halt.is_set():
                            active.add(pool.submit(self.work, queue.pop(0)))
                        if active:
                            done, active = wait(active, return_when=FIRST_COMPLETED)
                            for future in done:
                                future.result()
            finally:
                for signum, handler in old.items():
                    signal.signal(signum, handler)
            return report(self.state)
