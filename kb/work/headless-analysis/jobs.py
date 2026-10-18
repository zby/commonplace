"""Agent jobs for a workflow written as a Python script.

`ask()` is the one agent call: it writes a prompt, runs a headless worker that
writes named output files, and returns their contents. Results are cached by
content, so a rerun of the script after a crash, an edit or a stop resumes from
what is already answered:

- the key is the hash of the prompt text, the output names and the worker
  profile; changing any of them asks again, restoring them reuses the answer;
- only successful results are stored (as mdflow's workflow cache does), so a
  failed call is asked again on the next run;
- every record keeps its provenance: profile, harness session IDs, launch
  times and any transient failures before it.

`checked()` is the retry loop for content: a deterministic check judges each
result, and a failing result is asked again with the problems in the prompt,
so every attempt has its own key. `gather()` runs independent calls in
parallel. Everything else in a workflow is ordinary Python, which must make
control-flow decisions only from these results.
"""

from __future__ import annotations

import hashlib
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from pathlib import Path

from headless import HARNESSES, LaunchFailed, Profile, run_with_retries

POINTER = ("Read the complete invocation at `{path}` and follow it. "
           "Recover any truncated read before proceeding. You may read this supplied prompt file.")


@dataclass
class Answer:
    key: str
    outputs: dict[str, str]           # output name -> file content; absent optional outputs are missing
    refusal: str | None               # a worker's stated refusal, which is a result, not a failure
    record: dict                      # provenance, as stored


class OutOfAttempts(Exception):
    def __init__(self, job: str, problems: list):
        super().__init__(f"{job}: out of attempts; last problems: {problems[-1] if problems else None}")
        self.job = job
        self.problems = problems


class IncompleteOutputs(Exception):
    """The worker exited 0 but wrote neither every required output nor a refusal."""

    def __init__(self, job: str, missing: list[str], launch):
        super().__init__(f"{job}: worker finished without outputs {missing}")
        self.job, self.missing, self.launch = job, missing, launch


class Run:
    """One workflow run: a working directory for workers and a directory for its records."""

    def __init__(self, root: Path, cwd: Path, profile: Profile, timeout: float | None = None,
                 harnesses=HARNESSES, sleep=time.sleep):
        self.root, self.cwd, self.profile, self.timeout = Path(root), Path(cwd), profile, timeout
        self.harnesses, self.sleep = harnesses, sleep
        self.answers = self.root / "answers"
        self.answers.mkdir(parents=True, exist_ok=True)
        self._locks: dict[str, threading.Lock] = {}
        self._guard = threading.Lock()

    def log(self, **event) -> None:
        with self._guard, (self.root / "log.jsonl").open("a") as f:
            f.write(json.dumps({"time": time.time(), **event}) + "\n")

    def key(self, prompt: str, outputs: list[str], optional: list[str]) -> str:
        material = json.dumps([prompt, sorted(outputs), sorted(optional), asdict(self.profile)])
        return hashlib.sha256(material.encode()).hexdigest()

    def _lock(self, key: str) -> threading.Lock:
        with self._guard:
            return self._locks.setdefault(key, threading.Lock())

    def ask(self, job: str, prompt: str, outputs: list[str], optional: list[str] = ()) -> Answer:
        """Ask a worker for named output files; return them, from the cache if answered.

        The worker is told where to write each output and that it may write
        `refusal.md` instead. A run that exits 0 without every required output
        and without a refusal raises, and is not cached.
        """
        key = self.key(prompt, outputs, list(optional))
        record_path = self.answers / f"{key}.json"
        with self._lock(key):                       # two callers of one key launch one worker
            if record_path.exists():
                record = json.loads(record_path.read_text())
                return Answer(key, record["outputs"], record["refusal"], record)
            attempt_dir = self.root / "attempts" / f"{job}-{key[:8]}-{int(time.time())}"
            out_dir = attempt_dir / "outputs"
            out_dir.mkdir(parents=True)
            names = list(outputs) + list(optional)
            invocation = prompt + "\n\n## Outputs\n\n" + "\n".join(
                f"- `{name}`{' (optional)' if name in optional else ''}: write to `{out_dir / (name + '.md')}`"
                for name in names) + (
                f"\n\nIf you refuse the job, write your reason to `{out_dir / 'refusal.md'}` instead.")
            (attempt_dir / "prompt.md").write_text(invocation)
            self.log(event="launch", job=job, key=key, attempt=str(attempt_dir))
            try:
                delivered = run_with_retries(
                    self.profile, POINTER.format(path=attempt_dir / "prompt.md"), self.cwd,
                    attempt_dir, self.timeout, sleep=self.sleep, harnesses=self.harnesses)
            except LaunchFailed as failure:
                self.log(event="failed", job=job, key=key, reason=str(failure))
                raise
            produced = {n: (out_dir / f"{n}.md").read_text() for n in names if (out_dir / f"{n}.md").exists()}
            refusal_path = out_dir / "refusal.md"
            refusal = refusal_path.read_text() if refusal_path.exists() else None
            missing = [n for n in outputs if n not in produced]
            if missing and refusal is None:
                self.log(event="incomplete", job=job, key=key, missing=missing)
                raise IncompleteOutputs(job, missing, delivered.launch)
            record = {
                "job": job, "key": key, "prompt": prompt, "outputs": produced, "refusal": refusal,
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
                attempts: int = 3) -> Answer:
        """Ask, check, and ask again with the problems found, up to `attempts` times.

        `build_prompt(problems)` returns the prompt; `problems` lists earlier
        attempts' findings, oldest first, and is empty on the first attempt.
        `check(answer)` returns a list of problems, empty when accepted. A
        refusal is returned without checking: later jobs decide what it means.
        """
        problems: list = []
        for _ in range(attempts):
            answer = self.ask(job, build_prompt(problems), outputs, optional)
            if answer.refusal is not None:
                return answer
            found = check(answer)
            if not found:
                return answer
            problems = problems + [found]
            self.log(event="rejected", job=job, key=answer.key, problems=found)
        raise OutOfAttempts(job, problems)


def gather(*calls, max_workers: int | None = None) -> list:
    """Run independent zero-argument calls in parallel; return results in order.

    The first exception is raised after every call has finished, so no worker
    is left running when the script stops.
    """
    with ThreadPoolExecutor(max_workers=max_workers or len(calls)) as pool:
        futures = [pool.submit(c) for c in calls]
    return [f.result() for f in futures]
