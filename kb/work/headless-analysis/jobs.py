"""Agent jobs for a workflow written as a Python script.

`ask()` is the one agent call: it writes a prompt and its named inputs, runs a
headless worker that writes named output files, and returns their contents.
Results are cached by content, so a rerun of the script after a crash, an edit
or a stop resumes from what is already answered:

- the key is the hash of the prompt text, the inputs' sha256 digests, the
  output names and the worker profile; changing any of them asks again,
  restoring them reuses the answer;
- only successful results are stored (as mdflow's workflow cache does), so a
  failed call is asked again on the next run;
- a failed launch or an incomplete result is not an answer, but it is an
  attempt: it is appended to the key's failure log, which survives reruns and
  counts toward `checked()`'s attempt limit;
- a usage-limited launch is neither an answer nor an attempt; it propagates,
  the script stops, and a rerun after the reset resumes from the cache;
- every record keeps its provenance: profile, input digests, harness session
  IDs, launch times and any transient failures before it.

`checked()` is the retry loop for content: a deterministic check judges each
result, and a failing result is asked again with the problems in the prompt,
so each rejected attempt leads to a new key. `gather()` runs independent calls
in parallel; `Run(max_workers=n)` bounds how many workers run at once. A run
holds an exclusive lock on its root, so a second process cannot write the same
records. `accept()` materializes an accepted output under `artifact/`.
Everything else in a workflow is ordinary Python, which must make control-flow
decisions only from these results.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from pathlib import Path

from headless import HARNESSES, LaunchFailed, Profile, UsageLimited, run_with_retries

POINTER = ("Read the complete invocation at `{path}` and follow it. "
           "Recover any truncated read before proceeding. You may read this supplied prompt file.")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


@dataclass
class Answer:
    key: str
    outputs: dict[str, str]           # output name -> file content; absent optional outputs are missing
    refusal: str | None               # a worker's stated refusal, which is a result, not a failure
    record: dict                      # provenance, as stored


class OutOfAttempts(Exception):
    def __init__(self, job: str, problems: list, failure: str | None = None):
        super().__init__(f"{job}: out of attempts; last problems: {problems[-1] if problems else None}"
                         + (f"; last failure: {failure}" if failure else ""))
        self.job = job
        self.problems = problems
        self.failure = failure        # the last failed launch's or incomplete result's reason


class IncompleteOutputs(Exception):
    """The worker exited 0 but wrote neither every required output nor a refusal."""

    def __init__(self, job: str, missing: list[str], launch):
        super().__init__(f"{job}: worker finished without outputs {missing}")
        self.job, self.missing, self.launch = job, missing, launch


class RunLocked(Exception):
    def __init__(self, root: Path):
        super().__init__(f"another run holds {root / 'lock'}")
        self.root = root


class Run:
    """One workflow run: a working directory for workers and a directory for its records.

    The run holds an exclusive flock on `<root>/lock` until `close()`, so two
    processes cannot write one root's records at once; use it as a context
    manager. `max_workers`, when set, bounds the launches running at once
    across all threads; cache reads are not bounded.
    """

    def __init__(self, root: Path, cwd: Path, profile: Profile, timeout: float | None = None,
                 harnesses=HARNESSES, sleep=time.sleep, max_workers: int | None = None):
        self.root, self.cwd, self.profile, self.timeout = Path(root), Path(cwd), profile, timeout
        self.harnesses, self.sleep = harnesses, sleep
        self.answers = self.root / "answers"
        self.artifact = self.root / "artifact"
        self.answers.mkdir(parents=True, exist_ok=True)
        self._lock_fd: int | None = os.open(self.root / "lock", os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.flock(self._lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(self._lock_fd)
            self._lock_fd = None
            raise RunLocked(self.root) from None
        self._workers = threading.BoundedSemaphore(max_workers) if max_workers else None
        self._locks: dict[str, threading.Lock] = {}
        self._guard = threading.Lock()

    def close(self) -> None:
        """Release the run lock; a second call does nothing."""
        if self._lock_fd is not None:
            os.close(self._lock_fd)           # closing the descriptor releases the flock
            self._lock_fd = None

    def __enter__(self) -> Run:
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    def log(self, **event) -> None:
        with self._guard, (self.root / "log.jsonl").open("a") as f:
            f.write(json.dumps({"time": time.time(), **event}) + "\n")

    def key(self, prompt: str, outputs: list[str], optional: list[str],
            inputs: dict[str, str] | None = None) -> str:
        """The cache key; inputs enter by digest, so a changed input asks again."""
        digests = {name: digest(text) for name, text in sorted((inputs or {}).items())}
        material = json.dumps([prompt, digests, sorted(outputs), sorted(optional), asdict(self.profile)])
        return digest(material)

    def _lock(self, key: str) -> threading.Lock:
        with self._guard:
            return self._locks.setdefault(key, threading.Lock())

    def failure_records(self, key: str) -> list[dict]:
        """The key's failed launches and incomplete results, oldest first, across reruns."""
        path = self.answers / f"{key}.failures.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def failures(self, key: str) -> int:
        return len(self.failure_records(key))

    def _record_failure(self, key: str, reason: str, attempt_dir: Path, session: str | None) -> None:
        line = json.dumps({"reason": reason, "attempt": str(attempt_dir), "session": session,
                           "time": time.time()})
        with self._guard, (self.answers / f"{key}.failures.jsonl").open("a") as f:
            f.write(line + "\n")

    def _launch(self, attempt_dir: Path):
        """One worker launch with its transient retries, inside the worker limit when set."""
        def run():
            return run_with_retries(self.profile, POINTER.format(path=attempt_dir / "prompt.md"),
                                    self.cwd, attempt_dir, self.timeout, sleep=self.sleep,
                                    harnesses=self.harnesses)
        if self._workers is None:
            return run()
        with self._workers:
            return run()

    def ask(self, job: str, prompt: str, outputs: list[str], optional: list[str] = (),
            inputs: dict[str, str] | None = None) -> Answer:
        """Ask a worker for named output files; return them, from the cache if answered.

        Each input is written to the attempt's `inputs/<name>.md` and listed
        in the invocation. The worker is told where to write each output and
        that it may write `refusal.md` instead. A failed launch, or a run that
        exits 0 without every required output and without a refusal, is
        appended to the key's failure log and raised; neither is cached. A
        usage-limited launch is raised without a failure record.
        """
        inputs = dict(inputs or {})
        key = self.key(prompt, outputs, list(optional), inputs)
        record_path = self.answers / f"{key}.json"
        with self._lock(key):                       # two callers of one key launch one worker
            if record_path.exists():
                record = json.loads(record_path.read_text())
                return Answer(key, record["outputs"], record["refusal"], record)
            # The random suffix separates two attempts at one key within the same second.
            attempt_dir = (self.root / "attempts"
                           / f"{job}-{key[:8]}-{int(time.time())}-{uuid.uuid4().hex[:6]}")
            out_dir = attempt_dir / "outputs"
            out_dir.mkdir(parents=True)
            invocation = prompt
            if inputs:
                in_dir = attempt_dir / "inputs"
                in_dir.mkdir()
                for name, text in inputs.items():
                    (in_dir / f"{name}.md").write_text(text)
                invocation += "\n\n## Inputs\n\n" + "\n".join(
                    f"- `{name}`: `{in_dir / (name + '.md')}`" for name in inputs)
            names = list(outputs) + list(optional)
            invocation += "\n\n## Outputs\n\n" + "\n".join(
                f"- `{name}`{' (optional)' if name in optional else ''}: write to `{out_dir / (name + '.md')}`"
                for name in names) + (
                f"\n\nIf you refuse the job, write your reason to `{out_dir / 'refusal.md'}` instead.")
            (attempt_dir / "prompt.md").write_text(invocation)
            self.log(event="launch", job=job, key=key, attempt=str(attempt_dir))
            try:
                delivered = self._launch(attempt_dir)
            except UsageLimited as limited:
                self.log(event="usage-limited", job=job, key=key, reason=str(limited))
                raise
            except LaunchFailed as failure:
                self.log(event="failed", job=job, key=key, reason=str(failure))
                self._record_failure(key, str(failure), attempt_dir, failure.launches[-1].session)
                raise
            produced = {n: (out_dir / f"{n}.md").read_text() for n in names if (out_dir / f"{n}.md").exists()}
            refusal_path = out_dir / "refusal.md"
            refusal = refusal_path.read_text() if refusal_path.exists() else None
            missing = [n for n in outputs if n not in produced]
            if missing and refusal is None:
                incomplete = IncompleteOutputs(job, missing, delivered.launch)
                self.log(event="incomplete", job=job, key=key, missing=missing)
                self._record_failure(key, str(incomplete), attempt_dir, delivered.launch.session)
                raise incomplete
            record = {
                "job": job, "key": key, "prompt": prompt,
                "inputs": {name: digest(text) for name, text in inputs.items()},
                "outputs": produced, "refusal": refusal,
                "profile": asdict(self.profile), "attempt": str(attempt_dir),
                "session": delivered.launch.session, "started": delivered.launch.started,
                "seconds": delivered.launch.seconds,
                "transient-failures": [{"session": f.session, "stderr": f.stderr[-2000:]}
                                       for f in delivered.failed],
            }
            tmp = record_path.with_suffix(".tmp")
            tmp.write_text(json.dumps(record, indent=2))
            tmp.replace(record_path)                # atomic: a crash leaves no half record
            self.log(event="answered", job=job, key=key, refused=refusal is not None)
            return Answer(key, produced, refusal, record)

    def checked(self, job: str, build_prompt, check, outputs: list[str], optional: list[str] = (),
                attempts: int = 3, inputs=None) -> Answer:
        """Ask, check, and ask again with the problems found, up to `attempts` attempts.

        `build_prompt(problems)` returns the prompt; `problems` lists earlier
        attempts' findings, oldest first, and is empty on the first attempt.
        `inputs` is a dict, or a callable `inputs(problems, last)` returning
        one, where `last` is the rejected Answer the next attempt follows
        (None on the first), so a retry can hand the worker what it wrote.
        `check(answer)` returns a list of problems, empty when accepted. A
        refusal is returned without checking: later jobs decide what it means.

        The engine's counting rule: each answered ask along the chain of keys
        is one attempt, and so is each persisted failure of those keys, which
        includes failures from earlier runs of the script. A failed launch or
        incomplete result asks the same prompt (same key) again while attempts
        remain. UsageLimited propagates and consumes no attempt.
        """
        problems: list = []
        used = 0
        failure: str | None = None
        last: Answer | None = None
        while True:
            prompt = build_prompt(problems)
            given = inputs(problems, last) if callable(inputs) else inputs
            key = self.key(prompt, outputs, list(optional), given)
            failed = self.failure_records(key)
            if failed:
                failure = failed[-1]["reason"]
            if used + len(failed) >= attempts:
                raise OutOfAttempts(job, problems, failure)
            try:
                answer = self.ask(job, prompt, outputs, optional, given)
            except UsageLimited:
                raise
            except (LaunchFailed, IncompleteOutputs):
                continue                            # counted through the key's failure log
            used += self.failures(key) + 1
            if answer.refusal is not None:
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


def gather(*calls, max_workers: int | None = None) -> list:
    """Run independent zero-argument calls in parallel; return results in order.

    The first exception is raised after every call has finished, so no worker
    is left running when the script stops.
    """
    with ThreadPoolExecutor(max_workers=max_workers or len(calls)) as pool:
        futures = [pool.submit(c) for c in calls]
    return [f.result() for f in futures]
