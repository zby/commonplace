"""Launch one unattended task from `kb/tasks/` through a headless worker and check its commit.

A task is a runbook `kb/tasks/<name>.md` beside its log. `launch()` opens a
Workjig run under `kb/reports/state/tasks/<name>/<stamp>/`, asks one worker
to follow the runbook in the checkout itself, then checks the worker's
report against git: exactly one new commit, carrying the runbook's subject,
touching only the runbook's write scope, and no other change left in the
working tree. The checks are the admission test of
`kb/work/recurring-task-runner/`; the worker is trusted for nothing.
"""

from __future__ import annotations

import re
import subprocess
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import Run, output_ref

TASKS = Path("kb/tasks")
PROFILES = TASKS / "profiles.yaml"
STATE = Path("kb/reports/state/tasks")
RESULT = "result"

PROMPT = """\
You are running the task `{name}` unattended. Nobody will answer questions. \
If you cannot complete the run, write the problem file instead of guessing.

1. Read `{runbook}`. It is the runbook. Follow its Run Procedure, Batch (if \
present) and Output sections exactly.
2. Read the log named in its Output section before doing anything else. \
Earlier sections record what previous runs did; use them as the runbook says.
3. Write only inside the runbook's write scope: {scope}. Read whatever you \
need, but create, edit or delete no other file in the repository.
4. When the output is written, stage only those paths with `git add <path>` \
and commit with the subject `{subject}` and the trailer `Model: <your model id>`. \
Never use `git add -A`, `git add .` or `git commit -a`: the checkout may hold \
other sessions' uncommitted work. Do not push.
5. Then write {result}: its first line is `commit: <full hash>`, followed by \
at most three lines on what the run did.
"""


@dataclass(frozen=True)
class Runbook:
    name: str
    path: Path
    scope: tuple[str, ...]
    subject: str


@dataclass
class Report:
    run_dir: str
    model: str | None
    problem: str | None
    result: str
    commit: str | None
    commit_files: list[str]
    scope: list[str]
    new_commits: int
    scope_ok: bool
    subject_ok: bool
    leftover: list[str]

    @property
    def ok(self) -> bool:
        return self.problem is None and self.new_commits == 1 and self.scope_ok and self.subject_ok and not self.leftover


def _section(text: str, title: str) -> str:
    match = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if match is None:
        raise ValueError(f"runbook has no `## {title}` section")
    return match.group(1)


def load_runbook(root: Path, name: str) -> Runbook:
    path = root / TASKS / f"{name}.md"
    if not path.is_file():
        raise ValueError(f"no runbook at {path.relative_to(root)}")
    section = _section(path.read_text(encoding="utf-8"), "Write scope")
    subject = re.search(r"subject\s+`([^`]+)`", section)
    if subject is None:
        raise ValueError("the write scope names no commit subject")
    scope = tuple(item for item in re.findall(r"`([^`\n]+)`", section)
                  if item != subject.group(1) and ("/" in item or "." in item))
    if not scope:
        raise ValueError("the write scope lists no path")
    return Runbook(name, path, scope, subject.group(1))


def load_profile(root: Path, name: str | None) -> Profile:
    config = yaml.safe_load((root / PROFILES).read_text(encoding="utf-8"))
    chosen = config["default"] if name is None else name
    try:
        entry = config["profiles"][chosen]
    except KeyError:
        raise ValueError(f"no profile {chosen!r} in {PROFILES}") from None
    return Profile.from_yaml_entry(entry)


def _git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


def _status(root: Path) -> set[str]:
    return set(_git(root, "status", "--porcelain", "--untracked-files=all").splitlines())


def _in_scope(path: str, scope: tuple[str, ...]) -> bool:
    return any(path == item or path.startswith(item.rstrip("/") + "/") for item in scope)


def launch(root: Path, runbook: Runbook, profile: Profile, *, timeout: float | None = None,
           harnesses=HARNESSES, stamp: str | None = None) -> Report:
    """Run the task once in `root` and report what git shows afterwards."""
    before, head = _status(root), _git(root, "rev-parse", "HEAD").strip()
    prompt = PROMPT.format(name=runbook.name, runbook=runbook.path.relative_to(root),
                           scope=", ".join(f"`{item}`" for item in runbook.scope),
                           subject=runbook.subject, result=output_ref(RESULT))
    run_dir = root / STATE / runbook.name / (stamp or time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))
    with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses) as run:
        answer = run.ask("run", prompt, [RESULT])
    result = answer.outputs.get(RESULT, "")
    new = _git(root, "rev-list", f"{head}..HEAD").split()
    commit = new[0] if len(new) == 1 else None      # git decides, not the worker's report
    files = _git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", commit).split() if commit else []
    subject = _git(root, "log", "-1", "--format=%s", commit).strip() if commit else ""
    return Report(
        run_dir=run_dir.relative_to(root).as_posix(), model=answer.record.get("model"), problem=answer.problem,
        result=result, commit=commit, commit_files=files, scope=list(runbook.scope), new_commits=len(new),
        scope_ok=bool(files) and all(_in_scope(path, runbook.scope) for path in files),
        subject_ok=subject == runbook.subject,
        leftover=sorted(line for line in _status(root) - before if not line[3:].startswith(f"{STATE.as_posix()}/")),
    )


def report_dict(report: Report) -> dict:
    return {**asdict(report), "ok": report.ok}
