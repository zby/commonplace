"""Agent jobs for a workflow written as a Python script, over Workjig calls.

`ask()` is the one agent call: it hands a task and its named inputs to a
headless worker that writes named output files, and returns their contents.
Each ask is a chain of Workjig calls whose identity is the job name and the
call's position in the chain; Workjig keys each call's record by the full
request, so a rerun of the script after a crash, an edit or a stop replays
what is already answered:

- changing the task, an input, the outputs, the worker profile or the
  timeout asks again; restoring them reuses the answer;
- a timed-out launch, an incomplete result or a malformed problem file is
  not an answer, but it is an attempt, since the worker spent its work: it
  stays in the run record, counts toward `checked()`'s attempt limit across
  reruns, and the next call in the chain asks again;
- a launch that exits nonzero is relaunched by Workjig after a backoff, at
  most twice; one that still fails is an environment failure: it does not
  count and propagates, so the script stops, and a rerun after the repair
  moves past it to the next call in the chain;
- a usage-limited launch is neither an answer nor an attempt; it propagates
  the same way, and a rerun after the reset asks again;
- every answer keeps its provenance: profile, the model the harness
  recorded, input digests and the Workjig call and launches it came from.

A worker that cannot do its job writes Workjig's problem file instead of its
outputs; the problem is a result the script decides about, not a failure or a
refusal (a refusal is code's rejection of a candidate, which the worker
answers). A rerun replays a problem, like an answer, until the operator
dismisses it with `dismiss()`; the next call in the chain then asks again.

The task names its inputs and outputs by reference, `<Inputs: name.md>` and
`<Required outputs: name.md>`: Workjig writes fresh inputs for every launch
and appends their paths, the output paths and the problem file's to the
task, so the task text stays one request across launches.

`checked()` is the retry loop for content: a deterministic check judges each
result, and a failing result is asked again with the problems in the prompt,
so each rejected attempt leads to a new request. `gather()` runs independent
calls in parallel; `Run(max_workers=n)` bounds how many workers run at once. A
run holds an exclusive lock on its root, so a second process cannot write the
same records. `accept()` materializes an accepted output under `artifact/`.
Everything else in a workflow is ordinary Python, which must make control-flow
decisions only from these results.
"""

from __future__ import annotations

import fcntl
import hashlib
import itertools
import json
import os
import threading
import time
import uuid
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Self

import workjig
from workjig import CallResult, Request, RetryPolicy

from commonplace.headless.harness import HARNESSES, Profile, model_used

SUFFIX = ".md"
COUNTED = ("timeout", "incomplete", "protocol_error")
"""Workjig statuses that spend an attempt: the worker ran and returned no answer."""
LAUNCHES = 3
"""Launches per call: the first and two relaunches after a nonzero exit."""
RELAUNCH = RetryPolicy(on=("process_error", "launch_error"), backoff_seconds=30)
DEFAULT_TIMEOUT = 24 * 3600.0
"""Workjig needs a timeout; a run without one gets a day per launch."""
PROBLEM = "problem"
CALLS = "calls"
"""The directory under a run's root holding Workjig's records."""
DISMISSED = "dismissed.json"
"""The answers and worker problems the operator dismissed, as `[call, key]` pairs."""


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def input_ref(name: str) -> str:
    """How a task names an input, which Workjig lists with its path under `Inputs`."""
    return f"<Inputs: {name}{SUFFIX}>"


def output_ref(name: str, optional: bool = False) -> str:
    """How a task names an output, which Workjig lists with its path under its outputs."""
    return f"<{'Optional' if optional else 'Required'} outputs: {name}{SUFFIX}>"


PROBLEM_REF = "<the problem file named at the end of this invocation>"


@dataclass
class Answer:
    key: str
    outputs: dict[str, str]           # output name -> file content; absent optional outputs are missing
    problem: str | None               # the worker's report that it cannot do the job: a result, not a failure
    record: dict                      # provenance
    attempts: int = 1                 # attempts reaching this answer, counted failures included


class OutOfAttempts(Exception):
    def __init__(self, job: str, problems: list, failure: str | None = None):
        super().__init__(f"{job}: out of attempts; last problems: {problems[-1] if problems else None}"
                         + (f"; last failure: {failure}" if failure else ""))
        self.job = job
        self.problems = problems
        self.failure = failure        # the last timed-out, incomplete or malformed result's reason


class Exhausted(Exception):
    """An ask spent its allowed attempts on results that were not answers."""

    def __init__(self, job: str, failure: str):
        super().__init__(f"{job}: attempts spent without an answer; last failure: {failure}")
        self.job, self.failure = job, failure


class LaunchFailed(Exception):
    """A call's launches failed for a reason outside the task: the environment needs a repair."""

    def __init__(self, job: str, result: CallResult):
        super().__init__(f"{job}: {describe(result)}")
        self.job, self.result = job, result


class UsageLimited(LaunchFailed):
    """The harness reported an exhausted usage window. Relaunching before the
    reset cannot succeed, and the failure says nothing about the task."""


class RunLocked(Exception):
    def __init__(self, root: Path):
        super().__init__(f"another run holds {root / 'lock'}")
        self.root = root


def describe(result: CallResult) -> str:
    """A call's failure in one line: its status, launch count and the last launch's report."""
    last = result.launches[-1]
    if last.problem:
        detail = last.problem["message"]
    elif last.missing_outputs:
        detail = f"exit {last.returncode} without outputs {list(last.missing_outputs)}"
    else:
        detail = f"exit {last.returncode}"
    stderr = Path(last.launch_dir) / "stderr.log"
    tail = stderr.read_text(errors="replace").strip()[-500:] if stderr.is_file() else ""
    return f"{result.status} after {len(result.launches)} launch(es): {detail}" + (f"; {tail}" if tail else "")


def _acquire(root: Path) -> int:
    """Take the exclusive flock on `<root>/lock`; the descriptor holds it until closed."""
    fd = os.open(root / "lock", os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        os.close(fd)
        raise RunLocked(root) from None
    return fd


@contextmanager
def run_lock(root: Path) -> Iterator[None]:
    """Hold the lock a `Run` on `root` would take, so no run changes its records meanwhile."""
    fd = _acquire(Path(root))
    try:
        yield
    finally:
        os.close(fd)


class Run:
    """One workflow run: a working directory for workers and a directory for its records.

    The run holds an exclusive flock on `<root>/lock` and Workjig's records
    under `<root>/calls` until `close()`; use it as a context manager.
    `max_workers`, when set, bounds the launches running at once across all
    threads; replayed calls are not bounded.
    """

    def __init__(self, root: Path, cwd: Path, profile: Profile, timeout: float | None = None,
                 harnesses=HARNESSES, sleep=time.sleep, max_workers: int | None = None):
        self.root, self.cwd, self.profile = Path(root), Path(cwd), profile
        self.timeout = DEFAULT_TIMEOUT if timeout is None else timeout
        self.harnesses = harnesses
        self.worker = harnesses[profile.harness].worker(profile)
        self.artifact = self.root / "artifact"
        self.root.mkdir(parents=True, exist_ok=True)
        self._lock_fd: int | None = _acquire(self.root)
        try:
            self.records = workjig.Run(self.root / CALLS, self.cwd, sleep=sleep).__enter__()
        except BaseException:
            self.close()
            raise
        self._workers = threading.BoundedSemaphore(max_workers) if max_workers else None
        self._guard = threading.Lock()
        self._dismissed = _dismissed(self.root)

    def close(self) -> None:
        """Release Workjig's records and the run lock; a second call does nothing."""
        records, self.records = getattr(self, "records", None), None
        if records is not None:
            records.__exit__(None, None, None)
        if self._lock_fd is not None:
            os.close(self._lock_fd)           # closing the descriptor releases the flock
            self._lock_fd = None

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    def log(self, **event) -> None:
        with self._guard, (self.root / "log.jsonl").open("a") as f:
            f.write(json.dumps({"time": time.time(), **event}) + "\n")

    def scratch(self, job: str) -> Path:
        """A directory for a job's intermediate files, the same for every launch of it."""
        path = self.root / "scratch" / job
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _call(self, request: Request) -> CallResult:
        if self._workers is None:
            return self.records.call(request)
        with self._workers:
            return self.records.call(request)

    def ask(self, job: str, prompt: str, outputs: list[str], optional: list[str] = (),
            inputs: dict[str, str] | None = None, attempts: int = 1) -> Answer:
        """Ask a worker for named output files; return them, replayed if answered.

        `prompt` names inputs and outputs with `input_ref` and `output_ref`.
        Results that are not answers spend attempts and are asked again, up
        to `attempts`, then raise `Exhausted`; a replayed one spends again. An
        environment failure raises `LaunchFailed` and a usage limit
        `UsageLimited`; a rerun moves past either.
        """
        inputs = dict(inputs or {})
        names = list(outputs) + list(optional)
        spent, failure = 0, None
        for position in itertools.count():
            request = Request(
                call_id=f"{job}#{position}", task=prompt,
                inputs={name + SUFFIX: text for name, text in inputs.items()},
                required_outputs=tuple(name + SUFFIX for name in outputs),
                optional_outputs=tuple(name + SUFFIX for name in optional),
                worker=self.worker, timeout_seconds=self.timeout, max_launches=LAUNCHES, retry=RELAUNCH)
            result = self._call(request)
            key = result.request_hash
            if not result.reused:
                for launch in result.launches:
                    self.log(event="launch", job=job, key=key, launch=launch.launch_id, status=launch.status)
            if result.reused and (request.call_id, key) in self._dismissed:
                continue                  # the operator dismissed this result: ask again, spending nothing
            if result.status in ("delivered", "worker_problem"):
                produced = {name: result.outputs[name + SUFFIX] for name in names
                            if name + SUFFIX in result.outputs}
                last = result.launches[-1]
                problem = last.problem["message"] if result.status == "worker_problem" else None
                record = {
                    "job": job, "key": key, "call": request.call_id, "prompt": prompt,
                    "inputs": {name: digest(text) for name, text in inputs.items()},
                    "outputs": produced, PROBLEM: problem, "profile": asdict(self.profile),
                    "model": model_used(self.profile, last, self.harnesses),
                    "launches": [launch.launch_dir for launch in result.launches],
                }
                if not result.reused:
                    self.log(event="answered", job=job, key=key, problem=problem is not None)
                return Answer(key, produced, problem, record, spent + 1)
            if result.status in COUNTED:
                spent, failure = spent + 1, describe(result)
                if not result.reused:
                    self.log(event="failed", job=job, key=key, reason=failure)
                if spent >= attempts:
                    raise Exhausted(job, failure)
                continue
            if result.reused:
                continue                  # an earlier run's stop, repaired since: ask again
            self.log(event="stopped-call", job=job, key=key, reason=describe(result))
            raise (UsageLimited if result.status == "usage_limit" else LaunchFailed)(job, result)
        raise AssertionError("unreachable")

    def checked(self, job: str, build_prompt, check, outputs: list[str], optional: list[str] = (),
                attempts: int = 3, inputs=None) -> Answer:
        """Ask, check, and ask again with the problems found, up to `attempts` attempts.

        `build_prompt(problems)` returns the prompt; `problems` lists earlier
        attempts' findings, oldest first, and is empty on the first attempt.
        `inputs` is a dict, or a callable `inputs(problems, last)` returning
        one, where `last` is the rejected Answer the next attempt follows
        (None on the first), so a retry can hand the worker what it wrote.
        `check(answer)` returns a list of problems, empty when accepted. A
        worker's problem is returned without checking: the script decides
        what it means.

        Counting: each answered ask is one attempt, and so is each result of
        those asks that was not an answer, including ones from earlier runs
        of the script. An environment failure or a usage limit propagates
        and consumes no attempt.
        """
        problems: list = []
        used = 0
        failure: str | None = None
        last: Answer | None = None
        while True:
            given = inputs(problems, last) if callable(inputs) else inputs   # before the prompt: it may depend on them
            prompt = build_prompt(problems)
            if used >= attempts:
                raise OutOfAttempts(job, problems, failure)
            try:
                answer = self.ask(job, prompt, outputs, optional, given, attempts=attempts - used)
            except Exhausted as exhausted:
                raise OutOfAttempts(job, problems, exhausted.failure) from None
            used += answer.attempts
            answer.attempts = used
            if answer.problem is not None:
                return answer
            found = check(answer)
            if not found:
                return answer
            problems = problems + [found]
            last = answer
            self.log(event="rejected", job=job, key=answer.key, problems=found)

    def accept(self, path: str, content: str) -> Path:
        """Write an accepted output to `artifact/<path>` atomically and log its digest.

        Which output goes where is the workflow script's decision. Rewriting
        the same bytes on a rerun is harmless. A path outside `artifact/` is refused.
        """
        target = (self.artifact / path).resolve()
        if not target.is_relative_to(self.artifact.resolve()):
            raise ValueError(f"{path} is outside {self.artifact}")
        target.parent.mkdir(parents=True, exist_ok=True)
        tmp = target.with_name(f".{target.name}.{uuid.uuid4().hex[:6]}.tmp")
        tmp.write_text(content)
        tmp.replace(target)                         # atomic: readers see old or new bytes
        self.log(event="accepted", path=path, sha256=digest(content))
        return target


def _dismissed(root: Path) -> set[tuple[str, str]]:
    path = Path(root) / DISMISSED
    return {tuple(pair) for pair in json.loads(path.read_text())} if path.is_file() else set()


def recorded_calls(root: Path) -> list[dict]:
    """The run's Workjig calls, oldest record first, as `job`, `call`, `key`, `status`, `launches`, `problem`.

    Reads only; Workjig replaces its record atomically, so a running controller does not tear it.
    """
    path = Path(root) / CALLS / "run.json"
    if not path.is_file():
        return []
    dismissed = _dismissed(root)
    calls = []
    for call_id, versions in json.loads(path.read_text(encoding="utf-8"))["calls"].items():
        job = call_id.rpartition("#")[0]
        for key, entry in versions.items():
            last = entry["attempts"][-1] if entry["attempts"] else None
            status = "delivered" if entry["result"] is not None else (last["status"] if last else "reserved")
            problem = last["problem"]["message"] if status == "worker_problem" else None
            calls.append({"job": job, "call": call_id, "key": key, "status": status,
                          "launches": [attempt["launch_id"] for attempt in entry["attempts"]],
                          "problem": problem, "dismissed": (call_id, key) in dismissed})
    return calls


def dismiss(root: Path, job: str, key: str | None = None) -> list[dict]:
    """Dismiss the job's standing worker problems, or its answer `key`, so a rerun asks again.

    Returns the dismissed calls. Holds the run lock, so no controller
    replays them meanwhile.
    """
    root = Path(root)
    with run_lock(root):
        standing = [call for call in recorded_calls(root)
                    if call["job"] == job and not call["dismissed"]
                    and (call["status"] == "worker_problem" if key is None
                         else call["key"] == key and call["status"] == "delivered")]
        if not standing:
            raise ValueError(f"{job} has no {'worker problem' if key is None else f'answer {key}'} to dismiss")
        pairs = sorted(_dismissed(root) | {(call["call"], call["key"]) for call in standing})
        tmp = root / f"{DISMISSED}.tmp"
        tmp.write_text(json.dumps([list(pair) for pair in pairs], indent=2))
        tmp.replace(root / DISMISSED)
    return standing


def acknowledge_stopped(root: Path, cwd: Path, launch_id: str) -> None:
    """Record the operator's confirmation that a launch an earlier controller left unsettled has stopped.

    Inspects and kills nothing: confirm first that the process and its children are gone.
    """
    root = Path(root)
    with run_lock(root), workjig.Run(root / CALLS, cwd) as records:
        records.acknowledge_stopped(launch_id)


def gather(*calls, max_workers: int | None = None) -> list:
    """Run independent zero-argument calls in parallel; return results in order.

    The first exception is raised after every call has finished, so no worker
    is left running when the script stops.
    """
    if not calls:
        return []
    with ThreadPoolExecutor(max_workers=max_workers or len(calls)) as pool:
        futures = [pool.submit(c) for c in calls]
    return [f.result() for f in futures]
