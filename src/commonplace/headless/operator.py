"""Operator input: a file the workflow proposes and the operator answers, by editing it or not.

A workflow that needs the operator calls `answer()` with a file name under
the run's `artifact/` directory and a proposal. When the file exists, its
text is the operator's answer, edited or not, and the workflow goes on.
Otherwise the proposal is written there and `answer()` returns None: the
workflow reports `waiting()` and ends. Repeating the command continues the
run by replay and reads the file.

The proposal is a callable, so a workflow asks for it only when the file is
missing: a file the operator put in place first needs no proposal. A
workflow whose proposal can change between invocations names the file after
the proposal (for example by the answer key of the ask that made it), so a
new proposal waits again instead of reading an answer to an old one.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from commonplace.headless.jobs import Run


def answer(run: Run, name: str, propose: Callable[[], str]) -> str | None:
    """The text of `artifact/<name>`; when it is missing, write `propose()` there and return None."""
    path = run.artifact / name
    if path.is_file():
        return path.read_text(encoding="utf-8")
    run.accept(name, propose())
    return None


def waiting(run: Run, root: Path, name: str, what: str, command: str) -> dict:
    """The report entry for a stop at `artifact/<name>`: what the operator does, the file and the command to repeat."""
    return {"what": what, "file": (run.artifact / name).resolve().relative_to(root.resolve()).as_posix(),
            "command": command}
