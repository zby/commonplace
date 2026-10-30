"""Agent jobs for a workflow written as a Python script, over Workjig calls.

`ask()` is the one agent call: it hands a task and its named inputs to a
headless worker that writes named output files, and returns their contents.
Each request is one Workjig call named after its job, and Workjig keys the
call's record by the work it asks for, so a rerun of the script after a
crash, an edit or a stop replays what is already answered:

- changing the task, an input, the outputs or the worker profile asks
  again; restoring them reuses the answer; a changed timeout does not;
- every launch is `ask`'s decision: it raises the call's launch ceiling by
  one per launch it allows, and a call at its ceiling replays its launches
  without launching, so a rerun counts them again;
- a timed-out launch, an incomplete result or a malformed problem file is
  not an answer, but it is an attempt, since the worker spent its work: it
  counts toward `checked()`'s attempt limit across reruns;
- a launch that exits nonzero is relaunched after a backoff, at most twice
  in a row; one that still fails is an environment failure: it does not
  count and propagates, so the script stops, and a rerun after the repair
  continues the call;
- a usage-limited launch is neither an answer nor an attempt; it propagates
  the same way, and a rerun after the reset approves continuing past that
  recorded stop;
- every answer keeps its provenance: profile, the model the harness
  recorded, input digests and the Workjig call and launches it came from.

A worker that cannot do its job writes Workjig's problem file instead of its
outputs; the problem is a result the script decides about, not a failure or a
refusal (a refusal is code's rejection of a candidate, which the worker
answers). A rerun replays a problem, like an answer, until the operator
dismisses it with `dismiss()`. A call that cannot launch again, after a
dismissed answer or a malformed problem file, continues under the next
identity, `<job>#1`, `<job>#2` and so on.

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

import hashlib
import itertools
import json
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
"""Launches in a row a nonzero exit may take: the first and two relaunches."""
RETRY = RetryPolicy(on=("timeout", "incomplete", "worker_problem", "process_error", "launch_error",
                        "interrupted"),
                    backoff_seconds=30)
"""What may continue a call; whether it does is `ask`'s decision, one launch at a time."""
DEFAULT_TIMEOUT = 24 * 3600.0
"""Workjig needs a timeout; a run without one gets a day per launch."""
PROBLEM = "problem"
CALLS = "calls"
"""The directory under a run's root holding Workjig's records."""
DISMISSED = "dismissed.json"
"""The launches whose answer or worker problem the operator dismissed, by launch ID."""


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
        super().__init__(f"another run holds {root / CALLS / '.lock'}")
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


def _open_records(root: Path, cwd: Path, sleep=time.sleep) -> workjig.Run:
    """Open Workjig's records under `<root>/calls`, which holds the run lock until they close."""
    try:
        return workjig.Run(root / CALLS, cwd, sleep=sleep).__enter__()
    except workjig.RunBusyError:
        raise RunLocked(root) from None


@contextmanager
def run_lock(root: Path) -> Iterator[None]:
    """Hold the lock a `Run` on `root` would take, so no run changes its records meanwhile."""
    root = Path(root)
    lock = workjig.hold(root / CALLS)
    try:
        lock.__enter__()
    except workjig.RunBusyError:
        raise RunLocked(root) from None
    try:
        yield
    finally:
        lock.__exit__(None, None, None)


class Run:
    """One workflow run: a working directory for workers and a directory for its records.

    The run holds Workjig's records under `<root>/calls`, and with them the
    exclusive run lock, until `close()`; use it as a context manager.
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
        self.records = _open_records(self.root, self.cwd, sleep=sleep)
        self._workers = threading.BoundedSemaphore(max_workers) if max_workers else None
        self._guard = threading.Lock()
        self._dismissed = _dismissed(self.root)

    def close(self) -> None:
        """Release Workjig's records and the run lock; a second call does nothing."""
        records, self.records = getattr(self, "records", None), None
        if records is not None:
            records.__exit__(None, None, None)

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

    def _call(self, request: Request, resume: str | None) -> CallResult:
        if self._workers is None:
            return self.records.call(request, resume_usage_stop=resume)
        with self._workers:
            return self.records.call(request, resume_usage_stop=resume)

    def ask(self, job: str, prompt: str, outputs: list[str], optional: list[str] = (),
            inputs: dict[str, str] | None = None, attempts: int = 1) -> Answer:
        """Ask a worker for named output files; return them, replayed if answered.

        `prompt` names inputs and outputs with `input_ref` and `output_ref`.
        Each request is one Workjig call, and every launch is this method's
        decision: it raises the call's launch ceiling by one per launch it
        allows. A call at its ceiling replays without launching, so a rerun
        walks the recorded launches and counts them again. Results that are
        not answers spend attempts, up to `attempts`, then raise `Exhausted`.
        A nonzero exit is relaunched at most twice in a row, then raises
        `LaunchFailed`; a usage limit raises `UsageLimited`. A rerun after
        the repair continues the same call, approving a recorded usage stop.
        """
        inputs = dict(inputs or {})
        names = list(outputs) + list(optional)
        spent, failure = 0, None
        for identity in itertools.count():
            call_id = job if identity == 0 else f"{job}#{identity}"
            ceiling, resume, exits = 1, None, 0
            while True:
                request = Request(
                    call_id=call_id, task=prompt,
                    inputs={name + SUFFIX: text for name, text in inputs.items()},
                    required_outputs=tuple(name + SUFFIX for name in outputs),
                    optional_outputs=tuple(name + SUFFIX for name in optional),
                    worker=self.worker, timeout_seconds=self.timeout, max_launches=ceiling, retry=RETRY)
                result = self._call(request, resume)
                key, last, fresh = result.request_hash, result.launches[-1], not result.reused
                if fresh:
                    self.log(event="launch", job=job, key=key, launch=last.launch_id, status=last.status)
                ceiling, resume = len(result.launches) + 1, None
                status = result.status
                if last.launch_id in self._dismissed:
                    if status == "delivered":
                        break                 # a delivered call cannot launch again: a new identity
                    continue                  # the operator dismissed this problem: ask again, spending nothing
                if status in ("delivered", "worker_problem"):
                    produced = {name: result.outputs[name + SUFFIX] for name in names
                                if name + SUFFIX in result.outputs}
                    problem = last.problem["message"] if status == "worker_problem" else None
                    record = {
                        "job": job, "key": key, "call": call_id, "prompt": prompt,
                        "inputs": {name: digest(text) for name, text in inputs.items()},
                        "outputs": produced, PROBLEM: problem, "profile": asdict(self.profile),
                        "model": model_used(self.profile, last, self.harnesses),
                        "launches": [launch.launch_dir for launch in result.launches],
                    }
                    if fresh:
                        self.log(event="answered", job=job, key=key, problem=problem is not None)
                    return Answer(key, produced, problem, record, spent + 1)
                if status in COUNTED:
                    spent, failure, exits = spent + 1, describe(result), 0
                    if fresh:
                        self.log(event="failed", job=job, key=key, reason=failure)
                    if spent >= attempts:
                        raise Exhausted(job, failure)
                    if status == "protocol_error":
                        break                 # Workjig never relaunches a protocol error: a new identity
                    continue
                if fresh:
                    exits += status in ("process_error", "launch_error")
                    if status == "usage_limit" or exits >= LAUNCHES:
                        self.log(event="stopped-call", job=job, key=key, reason=describe(result))
                        raise (UsageLimited if status == "usage_limit" else LaunchFailed)(job, result)
                elif status == "usage_limit":
                    resume = last.launch_id   # rerunning after the reset is the operator's approval
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


def _dismissed(root: Path) -> set[str]:
    path = Path(root) / DISMISSED
    return set(json.loads(path.read_text())) if path.is_file() else set()


def recorded_calls(root: Path) -> list[dict]:
    """The run's Workjig calls as `job`, `call`, `key`, `status`, `launches`, `problem`, `dismissed`.

    `status` and `problem` are the latest launch's. Reads only; Workjig
    replaces its record atomically, so a running controller does not tear it.
    """
    path = Path(root) / CALLS / "run.json"
    if not path.is_file():
        return []
    dismissed = _dismissed(root)
    calls = []
    for call_id, versions in json.loads(path.read_text(encoding="utf-8"))["calls"].items():
        for key, entry in versions.items():
            if not entry["attempts"]:
                continue
            last = entry["attempts"][-1]
            status = "delivered" if entry["result"] is not None else last["status"]
            calls.append({"job": call_id.partition("#")[0], "call": call_id, "key": key, "status": status,
                          "launches": [attempt["launch_id"] for attempt in entry["attempts"]],
                          "problem": last["problem"]["message"] if status == "worker_problem" else None,
                          "dismissed": last["launch_id"] in dismissed})
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
        launches = sorted(_dismissed(root) | {call["launches"][-1] for call in standing})
        tmp = root / f"{DISMISSED}.tmp"
        tmp.write_text(json.dumps(launches, indent=2))
        tmp.replace(root / DISMISSED)
    return standing


def acknowledge_stopped(root: Path, cwd: Path, launch_id: str) -> None:
    """Record the operator's confirmation that a launch an earlier controller left unsettled has stopped.

    Inspects and kills nothing: confirm first that the process and its children are gone.
    """
    root = Path(root)
    records = _open_records(root, cwd)
    try:
        records.acknowledge_stopped(launch_id)
    finally:
        records.__exit__(None, None, None)


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
