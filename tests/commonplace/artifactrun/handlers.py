"""Code-job handlers for the toy plan, named by dotted path in its declaration.

Each handler records its call in the file named by `LOG_ENV`, so a test can see
which code jobs an invocation ran. A handler raises `KeyboardInterrupt` when
`INTERRUPT_ENV` names its job, which simulates a killed command.

What a check decides is driven by the text it reads:

- a candidate containing `REFUSE` is refused;
- a candidate containing `CRASH` makes the handler raise;
- a contract line `forbid: <text>` refuses a candidate containing that text;
- a candidate line `needs <role>: <text>` is refused when that role's member
  is present and does not contain the text.

A verification line `block <role>: <reason>` refuses that role's handed
version; every other subject is accepted against the verification.
"""

from __future__ import annotations

import os
from collections.abc import Callable, Mapping

from commonplace.artifactrun import CodeAttempt

LOG_ENV = "WORKFLOW_TEST_LOG"
INTERRUPT_ENV = "WORKFLOW_TEST_INTERRUPT"

Handler = Callable[[CodeAttempt], Mapping[str, bytes]]

VERIFIED = ("report", "other", "summary")


def _enter(job: str) -> None:
    log = os.environ.get(LOG_ENV)
    if log:
        with open(log, "a", encoding="utf-8") as handle:
            handle.write(job + "\n")
    if os.environ.get(INTERRUPT_ENV) == job:
        raise KeyboardInterrupt(job)


def _text(attempt: CodeAttempt, name: str) -> str | None:
    """An input's text; None when absent or not declared by this check."""
    try:
        data = attempt.read(name)
    except KeyError:
        return None
    return None if data is None else data.decode("utf-8")


def _check(job: str, role: str, partners: tuple[str, ...]) -> Handler:
    def check(attempt: CodeAttempt) -> Mapping[str, bytes]:
        _enter(job)
        text = _text(attempt, "candidate") or ""
        if "CRASH" in text:
            raise RuntimeError(f"{job} crashed on its candidate")
        problems = []
        if "REFUSE" in text:
            problems.append("the candidate asks to be refused")
        for line in (_text(attempt, "contract") or "").splitlines():
            if line.startswith("forbid: ") and line.removeprefix("forbid: ") in text:
                problems.append(f"the contract forbids {line.removeprefix('forbid: ')!r}")
        for line in text.splitlines():
            if line.startswith("needs "):
                partner, _, wanted = line.removeprefix("needs ").partition(": ")
                current = _text(attempt, partner)
                if current is not None and wanted not in current:
                    problems.append(f"{partner} no longer says {wanted!r}")
        if problems:
            attempt.judge("candidate", outcome="refused", findings="\n".join(problems))
        else:
            present = tuple(p for p in partners if _text(attempt, p) is not None)
            attempt.judge(
                "candidate",
                outcome="accepted",
                scope=tuple(f"{role}:cites:{partner}" for partner in present),
            )
        return {}

    return check


check_brief = _check("check-brief", "brief", ())
check_report = _check("check-report", "report", ("brief",))
check_other = _check("check-other", "other", ("brief", "report"))
check_summary = _check("check-summary", "summary", ("report", "other"))
check_digest = _check("check-digest", "digest", ("report", "other"))


def apply_verification(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Judge the versions the verifier was handed, never the current members."""
    _enter("apply-verification")
    blocked = {}
    for line in (_text(attempt, "verdict") or "").splitlines():
        if line.startswith("block "):
            role, _, reason = line.removeprefix("block ").partition(": ")
            blocked[role] = reason
    for role in VERIFIED:
        relation = f"verification:cites:{role}"
        if role in blocked:
            attempt.judge(f"{role}-seen", outcome="refused", scope=(relation,), findings=blocked[role])
        else:
            attempt.judge(f"{role}-seen", outcome="accepted", scope=(relation,))
    attempt.judge(
        "verdict",
        outcome="accepted",
        scope=tuple(f"verification:cites:{role}" for role in VERIFIED if role not in blocked),
    )
    return {}


def assemble(attempt: CodeAttempt) -> Mapping[str, bytes]:
    _enter("assemble")
    brief = _text(attempt, "brief") or ""
    attempt.judge("overview", outcome="accepted", scope=("overview:cites:brief",))
    return {"overview": f"# Overview\n\nAssembled from a brief of {len(brief)} bytes.\n".encode()}
