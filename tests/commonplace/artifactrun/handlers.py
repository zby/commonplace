"""Code-job handlers for the toy plan that no standard handler covers yet.

The checks are the standard `commonplace.artifactrun.handlers.check`. Handler
calls are logged, and interrupted, by `support.record_calls`, which reads the
two environment variables named here.

A verification line `block <role>: <reason>` refuses that role's handed
version; every other subject is accepted against the verification.
"""

from __future__ import annotations

from collections.abc import Mapping

from commonplace.artifactrun import CodeAttempt

LOG_ENV = "WORKFLOW_TEST_LOG"
INTERRUPT_ENV = "WORKFLOW_TEST_INTERRUPT"

VERIFIED = ("report", "other", "summary")


def _text(attempt: CodeAttempt, name: str) -> str | None:
    """An input's text; None when absent or not declared by this job."""
    try:
        data = attempt.read(name)
    except KeyError:
        return None
    return None if data is None else data.decode("utf-8")


def apply_verification(attempt: CodeAttempt) -> Mapping[str, bytes]:
    """Judge the versions the verifier was handed, never the current members."""
    blocked = {}
    for line in (_text(attempt, "verdict") or "").splitlines():
        if line.startswith("block "):
            role, _, reason = line.removeprefix("block ").partition(": ")
            blocked[role] = reason
    for role in VERIFIED:
        relation = f"verification:verifies:{role}"
        if role in blocked:
            attempt.judge(f"{role}-seen", outcome="refused", scope=(relation,), findings=blocked[role])
        else:
            attempt.judge(f"{role}-seen", outcome="accepted", scope=(relation,))
    # The verdict's content acceptance covers its citations of every subject it
    # was handed; the verifies relations above are covered only by the subject
    # judgments.
    attempt.judge(
        "verdict",
        outcome="accepted",
        scope=tuple(f"verification:cites:{role}" for role in VERIFIED),
    )
    return {}


def assemble(attempt: CodeAttempt) -> Mapping[str, bytes]:
    brief = _text(attempt, "brief") or ""
    attempt.judge("overview", outcome="accepted", scope=("overview:cites:brief",))
    return {"overview": f"# Overview\n\nAssembled from a brief of {len(brief)} bytes.\n".encode()}
