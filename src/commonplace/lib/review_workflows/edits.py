"""Writing one checkout file from workflow outputs: bounds, the write-once log and the guard.

A workflow never lets a worker write the checkout. A worker's edited text is
an output; code checks it against hard bounds (`bounds()`), and `Writes`
applies an accepted text to the file only from the text it expects to find
there, recording each change in `artifact/writes.json` as the hashes of the
text it replaced and the text it wrote, in order. A rerun replays the
workflow's decisions, and each write the record already holds is skipped, so
an edit is never applied twice. A new write is recorded first and happens
only when the file on disk is the text it expects.

A run opens only on the text it left. That is the start text before its
first write and the text of its last recorded write after it. The text that
write replaced is also accepted: the process died between the record and the
file, and the replay finishes that write. Any other text was changed outside
the run, and `Conflict` stops the run before it launches a worker.

`guarded_changes()` is the checkout guard's finding minus the workflow's own
write: the file is dropped from the changed paths when it holds exactly the
text the log says the run last wrote.
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path

from commonplace.headless.jobs import Run
from commonplace.lib import frontmatter
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.review_workflows import gates, results
from commonplace.lib.validation import ValidationRun

WRITES = "writes.json"
PRESERVED = ("title", "type")
"""Frontmatter fields no edit may change."""
NO_WRITES = ("Write nothing else: create, edit or delete no file in the repository, and run no "
             "command that changes it or its git state. Do not delegate or start another agent.")


class Stop(Exception):
    """The run cannot go on without the operator: a worker problem, a spent call or a launch failure."""


class Conflict(Stop):
    """The file on disk is not the text the workflow expected; nothing was written."""


def rejection(problems: list[list[str]]) -> str:
    """The prompt's tail on a retry: the problems of the attempt before."""
    if not problems:
        return ""
    return "\nAn earlier answer was rejected. Write it again, correcting:\n" + "".join(
        f"- {problem}\n" for problem in problems[-1])


def validation_fails(root: Path, note: str, text: str) -> set[str]:
    """The deterministic validator's failures for `text` as the file at `note`, without writing it."""
    path = (root / note).resolve()
    return set(ValidationRun(repo_root=root, paths=(path,), content_overrides={path: text}).validate(path).fails)


def bounds(root: Path, note: str, start: str, text: str, baseline: set[str]) -> list[str]:
    """The hard bounds an edited note breaks; empty when it keeps them.

    The frontmatter title and type and the H1 are the start text's;
    `user-verified` is gone when the body changed; and the validator finds
    no failure that the start text did not have (`baseline`).
    """
    parsed, before = frontmatter.parse(text), frontmatter.parse(start)
    if not frontmatter.opens_frontmatter(text) or not parsed.ok:
        return ["the edited note's frontmatter does not parse; keep the note's frontmatter"]
    problems = [f"frontmatter `{key}` changed; keep it as it was" for key in PRESERVED
                if parsed.data.get(key) != before.data.get(key)]
    parts, start_parts = results.note_parts(text), results.note_parts(start)
    if start_parts is not None and parts["title"] != start_parts["title"]:
        problems.append(f"the H1 changed; keep `# {start_parts['title']}`")
    if (start_parts is None or parts["body"] != start_parts["body"]) and "user-verified" in parsed.data:
        problems.append("the body changed, so remove `user-verified` from the frontmatter")
    problems += [f"validation: {fail}" for fail in sorted(validation_fails(root, note, text) - baseline)]
    return problems


def write_text(path: Path, text: str) -> None:
    """Write exactly `text` atomically: readers see the old bytes or the new ones."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{uuid.uuid4().hex[:6]}.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    tmp.replace(path)


class Writes:
    """The file changes this run made, in order, recorded in `artifact/writes.json`."""

    def __init__(self, run: Run, root: Path, note: str, start: str):
        """Open the log; raise Conflict unless the file holds the text the run left (`start` before any write)."""
        self.run, self.path = run, root / note
        record = run.artifact / WRITES
        self.log: list[dict] = json.loads(record.read_text(encoding="utf-8")) if record.is_file() else []
        self.step = 0
        current = sha256(self.path.read_text(encoding="utf-8")) if self.path.is_file() else None
        left = self.log[-1]["to"] if self.log else sha256(start)
        self.interrupted = bool(self.log) and current != left and current == self.log[-1]["from"]
        if current != left and not self.interrupted:
            raise Conflict(f"{self.path.name} is not the text this run left in it; nothing was written")

    def move(self, old: str, new: str) -> None:
        """Change the file from `old` to `new`, once across reruns; raise Conflict if it does not hold `old`."""
        entry = {"from": sha256(old), "to": sha256(new)}
        if self.step < len(self.log):
            if self.log[self.step] != entry:
                raise Conflict(f"write {self.step + 1} differs from the one this run recorded; "
                               "an answer was dismissed or an input changed after the run wrote the note")
            self.step += 1
            if self.interrupted and self.step == len(self.log):
                write_text(self.path, new)                # the write a dead process recorded and did not make
                self.interrupted = False
            return
        current = self.path.read_text(encoding="utf-8") if self.path.is_file() else None
        if current != old:
            raise Conflict(f"{self.path.name} changed during the pass; nothing was written")
        self.log.append(entry)
        self.run.accept(WRITES, json.dumps(self.log, indent=2))
        write_text(self.path, new)
        self.step += 1


def guarded_changes(root: Path, before: dict[str, str], run_dir: Path, note: str) -> list[str]:
    """The paths the checkout guard saw change since `before`, less `note` when it holds the run's last write."""
    changed = gates.changed_paths(before, gates.checkout_state(root))
    record = run_dir / "artifact" / WRITES
    left = json.loads(record.read_text(encoding="utf-8"))[-1]["to"] if record.is_file() else None
    path = root / note
    if left is not None and path.is_file() and sha256(path.read_text(encoding="utf-8")) == left:
        changed = [rel for rel in changed if rel != note]    # the workflow's own write
    return changed
