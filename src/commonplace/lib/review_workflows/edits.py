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
import re
import uuid
from pathlib import Path

from commonplace.headless import operator
from commonplace.headless.jobs import Run, digest
from commonplace.lib import answers, frontmatter
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.naming import WRITE_BRIEF_TYPE, write_brief_name_for
from commonplace.lib.note_parser import blank_fenced_code_blocks, find_markdown_links
from commonplace.lib.quote_matching import normalize_text
from commonplace.lib.quote_verification import parse_prose_citations
from commonplace.lib.review_workflows import gates, results
from commonplace.lib.validation import ValidationRun

PUBLICATION = "publication-answers.md"
"""The stop file of a publication: the operator's answers over the candidate `final.md`."""
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


def answered(root: Path, path: Path, text: str) -> tuple[dict, list[str]]:
    """The frontmatter of the answers file `text` at `path`, and what the validator refuses in it.

    The validator compares the answers with the question they name on disk
    (`types/answers.md`); `text` stands in for the file at `path`.
    """
    parsed = frontmatter.parse(text)
    if not parsed.ok or parsed.data.get("type") != answers.TYPE:
        return {}, [f"{path.name} is not an answers file; it must declare type: {answers.TYPE}"]
    report = ValidationRun(repo_root=root, paths=(path,), content_overrides={path.resolve(): text}).validate(path)
    return parsed.data, list(report.fails)


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


def artifact_bounds(root: Path, artifact: str, start: str, text: str, baseline: set[str]) -> list[str]:
    """The hard bounds a revised artifact breaks; empty when it keeps them.

    An artifact with frontmatter keeps the note bounds of `bounds()`. An
    artifact without frontmatter gains none, keeps its first H1 and adds no
    validation failure. No edit may change the title: an operation that judges
    titles proposes them in its report.
    """
    if not text.strip():
        return ["the revised artifact is empty"]
    if frontmatter.opens_frontmatter(start):
        return bounds(root, artifact, start, text, baseline)
    problems = ["the artifact has no frontmatter; add none"] if frontmatter.opens_frontmatter(text) else []
    title, start_title = results.note_parts(text) or {}, results.note_parts(start) or {}
    if title.get("title") != start_title.get("title"):
        problems.append(f"the H1 changed; keep `# {start_title.get('title')}`")
    return problems + [f"validation: {fail}" for fail in sorted(validation_fails(root, artifact, text) - baseline)]


_QUOTE_MARK = re.compile(r"^[ \t]*>[ \t]?", re.MULTILINE)


def quoted_spans(text: str) -> list[str]:
    """The quoted spans of a text: each Markdown blockquote, and each quotation paired with a `verbatim` citation."""
    spans, block = [], []
    for line in blank_fenced_code_blocks(frontmatter.strip(text)).splitlines() + [""]:
        if _QUOTE_MARK.match(line):
            block.append(_QUOTE_MARK.sub("", line))
        elif block:
            spans.append("\n".join(block))
            block = []
    spans += [citation.quote for citation in parse_prose_citations(text) if citation.quote]
    return [span for span in spans if span.strip()]


def preserved(start: str, text: str, removed_links: list[str]) -> list[str]:
    """What an edited text lost that it must keep: a link target not named as removed, or a quoted span."""
    kept = set(find_markdown_links(frontmatter.strip(text)))
    problems = [f"the link to `{target}` is gone; restore it, or name it under `removed-links`"
                for target in dict.fromkeys(find_markdown_links(frontmatter.strip(start)))
                if target not in kept and target not in removed_links]
    plain = normalize_text(_QUOTE_MARK.sub("", text), "prose")
    problems += [f"the quoted span `{span[:60]}` changed; quoted text is never reworded"
                 for span in quoted_spans(start) if normalize_text(span, "prose") not in plain]
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
    """Require the operator's approval of the exact checked candidate, never of an editable replacement.

    The question is the candidate `final.md`; the stop's file is a pending
    answers file over it (`types/answers.md`), whose one item names the
    candidate's hash. Publication may proceed only when the recorded answers
    pass the validator and approve that item. The proposal key binds the
    start text, the candidate and the caller's decision context, so a change
    in any of them withdraws the approval. Callers recheck the brief and the
    note's start text before applying. This gate publishes no checkout
    artifact. Candidate and diff are derived from checked workflow outputs
    again on repeat, not read as new edit inputs.
    """
    root = root.resolve()
    name = PUBLICATION
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
    run.accept("final.diff", diff)
    proposal = answers.pending(candidate.relative_to(root).as_posix(), final.encode("utf-8"))
    key = digest(json.dumps({"artifact": note, "start-sha256": sha256(start), "final-sha256": sha256(final),
                             "context-sha256": digest(json.dumps(inputs, sort_keys=True))}, sort_keys=True))
    approved = operator.answer(run, name, proposal, key=key)
    instruction = (f"Inspect final.md and final.diff. Record the operator's decision on the one item of {name}: "
                   "`approved`, or `rejected` or `deferred` with the operator's reason, with `decided-by: operator` "
                   "and `decided-at`. Approve that file, then repeat. To revise the candidate, change the "
                   "workflow inputs or supply --plan for revision; editing final.md is not a workflow input.")
    if changed:
        operator.invalidate(run, name)
        run.accept(name, proposal)
        return operator.waiting(run, root, name,
                                "The publication files changed; the generated candidate, diff and pending answers "
                                "have been restored and any approval withdrawn. Inspect and answer again. "
                                "No artifact was written. " + instruction, command)
    if approved is None:
        return operator.waiting(run, root, name, instruction, command)
    data, problems = answered(root, run.artifact / name, approved)
    if not problems and data["items"][0]["state"] != "approved":
        item = data["items"][0]
        problems = [f"the operator's answer is `{item['state']}`"
                    + (f": {item['reason']}" if item.get("reason") else "")]
    if problems:
        return operator.waiting(run, root, name, "The approved answers do not authorize publication: "
                                + "; ".join(problems) + ". No artifact was written. " + instruction, command)
    return None


def run_dir(root: Path, workflow: str, note: str) -> Path:
    """The run of `workflow` over the note's current text: `runs/v2/<workflow>/<note without .md>/<hash prefix>`.

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
