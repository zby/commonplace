"""The toy plan's one consumer handler, assembly, and the call-log variables.

The checks and the verdict application are the standard handlers in
`commonplace.artifactrun.handlers`. Handler calls are logged, and
interrupted, by `support.record_calls`, which reads the two environment
variables named here.
"""

from __future__ import annotations

from collections.abc import Mapping

from commonplace.artifactrun import CodeAttempt

LOG_ENV = "WORKFLOW_TEST_LOG"
INTERRUPT_ENV = "WORKFLOW_TEST_INTERRUPT"


def assemble(attempt: CodeAttempt) -> Mapping[str, bytes]:
    brief = attempt.read("brief") or b""
    attempt.judge("overview", outcome="accepted", scope=("overview:cites:brief",))
    return {"overview": f"# Overview\n\nAssembled from a brief of {len(brief)} bytes.\n".encode()}
