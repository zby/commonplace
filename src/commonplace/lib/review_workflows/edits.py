"""Writing one checkout file from workflow outputs: bounds, the single write and the guard.

A workflow never lets a worker write the checkout. A worker's edited text is
an output; code checks it against hard bounds (`bounds()`) and keeps the
accepted text in memory and in the run's `artifact/` directory. The next
step works on that text, not on the file. Only the workflow's last step
writes the file, once, through `apply()`, and only over the start text. Any
other text is a change made outside the run, and `Conflict` stops the write.

A run is a function of its inputs. `run_dir()` derives its directory from
the workflow, the note's path and the hash of the note's current text, so
repeating a command continues its run by replay, and an edited note opens a
new run.

`guarded_changes()` is the checkout guard's finding minus the workflow's own
write: the file is dropped from the changed paths when it holds exactly the
final text the run applied.
"""

from __future__ import annotations

import difflib
import json
import uuid
from pathlib import Path

from commonplace.headless import operator
from commonplace.headless.jobs import Run, digest
from commonplace.lib import frontmatter
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.naming import WRITE_BRIEF_TYPE, write_brief_name_for
from commonplace.lib.review_workflows import gates, results
from commonplace.lib.validation import ValidationRun

PRESERVED = ("title", "type", "brief")
"""Frontmatter fields no edit may change."""
NO_WRITES = ("Write nothing else: create, edit or delete no file in the repository, and run no "
             "command that changes it or its git state. Do not delegate or start another agent.")


class Stop(Exception):
    """The run cannot go on without the operator: a worker problem, a spent call or a launch failure."""


class Conflict(Stop):
    """The file on disk is not the text the workflow expected; nothing was written."""


def capture_brief(root: Path, note: str, text: str) -> dict[str, str]:
    """Capture the declared sibling brief once; a broken declaration stops before workers launch."""
    data = frontmatter.parse(text).data
    if "brief" not in data:
        return {}
    expected = write_brief_name_for(Path(note))
    if data["brief"] != expected:
        raise Stop(f"write brief: {note} must name its own sibling {expected}")
    path = root / Path(note).parent / expected
    if not path.resolve().is_relative_to(root.resolve()):
        raise Stop(f"write brief is outside the repository: {path}")
    try:
        brief = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise Stop(f"write brief cannot be read: {path}: {error}") from error
    parsed = frontmatter.parse(brief)
    if not parsed.ok or parsed.data.get("type") != WRITE_BRIEF_TYPE:
        raise Stop(f"write brief must declare {WRITE_BRIEF_TYPE}: {path}")
    return {"brief": brief}


def unchanged_brief(root: Path, note: str, start: str, captured: dict[str, str]) -> None:
    """Refuse publication if the captured writing commission changed during this invocation."""
    try:
        current = capture_brief(root, note, start)
    except Stop as error:
        raise Conflict(f"write brief changed during the run; nothing was written: {error}") from error
    if current != captured:
        raise Conflict(f"write brief for {note} changed during the run; nothing was written")


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

    The frontmatter title, type and brief declaration and the H1 are the start text's;
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


def unchanged(root: Path, note: str, start: str, proposed: Path) -> None:
    """Raise Conflict, naming the artifact file `proposed`, unless the note still holds `start`."""
    path = root / note
    if not path.is_file() or path.read_text(encoding="utf-8") != start:
        raise Conflict(f"{note} changed during the run; nothing was written. "
                       f"The proposed text is {proposed.relative_to(root).as_posix()}")


def apply(root: Path, note: str, start: str, final: str, proposed: Path) -> None:
    """Write `final` to the note, atomically and only over `start`; any other text is a Conflict."""
    unchanged(root, note, start, proposed)
    write_text(root / note, final)


def publication(run: Run, root: Path, note: str, start: str, final: str, *,
                inputs: dict, command: str) -> dict | None:
    """Require approval of the exact checked candidate, never of an editable replacement.

    Callers supply the decision context and recheck the brief before applying.
    This gate publishes no checkout artifact. Candidate and diff are derived
    from checked workflow outputs again on repeat, not read as new edit inputs.
    """
    root = root.resolve()
    name = "publication.json"
    existed = (run.artifact / name).is_file()
    diff_lines = difflib.unified_diff(start.splitlines(keepends=True), final.splitlines(keepends=True),
                                     fromfile=note, tofile=f"{note} (candidate)")
    diff = "".join(line if line.endswith("\n") else line + "\n\\ No newline at end of file\n"
                   for line in diff_lines)
    # Check before answer() restores a missing manifest from its operator record.
    changed = operator.edited(run, name)
    for filename, expected in (("final.md", final), ("final.diff", diff)):
        path = (run.artifact / filename).resolve()
        if not path.is_relative_to(run.artifact.resolve()):
            raise ValueError(f"publication file outside run artifacts: {filename}")
        changed |= (path.read_text(encoding="utf-8") != expected if path.is_file() else existed)
    candidate = run.accept("final.md", final)
    unchanged(root, note, start, candidate)
    diff_path = run.accept("final.diff", diff)
    proposal = json.dumps({"artifact": note, "start-sha256": sha256(start), "final-sha256": sha256(final),
                           "context-sha256": digest(json.dumps(inputs, sort_keys=True)),
                           "candidate": candidate.relative_to(root).as_posix(),
                           "diff": diff_path.relative_to(root).as_posix()}, indent=2) + "\n"
    approved = operator.answer(run, name, proposal, key=digest(proposal))
    instruction = ("Inspect final.md and final.diff beside this publication manifest. Approve the unchanged "
                   "manifest to authorize publication, then repeat. To revise the candidate, change the "
                   "workflow inputs or supply --plan for revision; editing final.md is not a workflow input.")
    if changed or (run.artifact / name).read_text(encoding="utf-8") != proposal or (
            approved is not None and approved != proposal):
        operator.invalidate(run, name)
        run.accept(name, proposal)
        return operator.waiting(run, root, name,
                                "The publication files changed; the generated candidate, diff and manifest "
                                "have been restored and any approval withdrawn. Inspect and approve again. "
                                "No artifact was written. " + instruction, command)
    if approved is None:
        return operator.waiting(run, root, name, instruction, command)
    return None


def run_dir(root: Path, workflow: str, note: str) -> Path:
    """The run of `workflow` over the note's current text: `runs/<workflow>/<note without .md>/<hash prefix>`.

    The same command on the same text finds the same run and continues it by
    replay; another text opens another run.
    """
    text = (root / note).read_text(encoding="utf-8")
    return root / gates.RUNS / workflow / note.removesuffix(".md") / sha256(text)[:12]


def guarded_changes(root: Path, before: dict[str, str], note: str, final: str | None) -> list[str]:
    """The paths the checkout guard saw change since `before`, less `note` when it holds the applied `final`."""
    changed = gates.changed_paths(before, gates.checkout_state(root))
    path = root / note
    if final is not None and path.is_file() and path.read_text(encoding="utf-8") == final:
        changed = [rel for rel in changed if rel != note]    # the workflow's own write
    return changed
