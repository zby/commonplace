"""Writing one checkout file from workflow outputs: bounds, the single write and the guard.

A workflow never lets a worker write the checkout. A worker's edited text is
an output; code checks it against hard bounds (`bounds()`) and keeps the
accepted text in memory and in the run's `artifact/` directory. The next
step works on that text, not on the file. Only the workflow's last step
writes the file, through `apply()`, and only over the text the run last
knew: its start text, or the text it last published itself. Any other text
is a change made outside the run, and `Conflict` stops the write.

A run is a function of its inputs. `run_dir()` derives its directory from
the workflow, the note's path and the hash of the note's current text, so
repeating a command continues its run by replay, and an edited note opens a
new run. A run that wrote the note itself (`PUBLISHED`) is found by the text
it last wrote while it is open, and never again by its start text.

`guarded_changes()` is the checkout guard's finding minus the workflow's own
write: the file is dropped from the changed paths when it holds exactly the
final text the run applied.
"""

from __future__ import annotations

import difflib
import json
import re
import uuid
from collections.abc import Sequence
from pathlib import Path

from commonplace.headless import operator
from commonplace.headless.jobs import Run, digest
from commonplace.lib import answers, frontmatter
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.naming import WRITE_BRIEF_TYPE, write_brief_name_for
from commonplace.lib.note_parser import blank_fenced_code_blocks, find_markdown_links
from commonplace.lib.quote_matching import normalize_text
from commonplace.lib.quote_verification import parse_prose_citations
from commonplace.lib.review_workflows import gates, observations, results
from commonplace.lib.validation import CheckResults, ValidationRun

PUBLICATION = "publication-answers.md"
"""The stop file of a publication: the operator's answers over the candidate `final.md`, or the revised candidate."""
CANDIDATE = "final.md"
START = "start.md"
"""The note's text when the run started, which the run may replace."""
REVISED = "revised.md"
"""The revised candidate: the operator's revision of `final.md`, supplied with `--revised`."""
REVISED_DIFF = "revised.diff"
"""The diff from the note to the revised candidate."""
REVISION_DIFF = "revised-from-final.diff"
"""The diff from the workflow's candidate `final.md` to the revised candidate."""
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


def validation(root: Path, note: str, text: str) -> CheckResults:
    """The deterministic validator's findings for `text` as the file at `note`, without writing it."""
    path = (root / note).resolve()
    return ValidationRun(repo_root=root, paths=(path,), content_overrides={path: text}).validate(path)


def validation_fails(root: Path, note: str, text: str) -> set[str]:
    """The deterministic validator's failures for `text` as the file at `note`, without writing it."""
    return set(validation(root, note, text).fails)


def added(found: set[str], baseline: set[str]) -> list[str]:
    """The validator findings of an edited text that the text it was edited from did not have, sorted."""
    return sorted(set(found) - set(baseline))


def new_warnings(root: Path, note: str, start: str, text: str) -> list[str]:
    """The validator warnings `text` has and `start` did not have; they do not block, the operator is told.

    The comparison is the one `bounds()` makes for failures (`added()`).
    """
    return added(set(validation(root, note, text).warns), set(validation(root, note, start).warns))


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
    problems += [f"validation: {fail}" for fail in added(validation_fails(root, note, text), baseline)]
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
    return problems + [f"validation: {fail}" for fail in added(validation_fails(root, artifact, text), baseline)]


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


def diff(before: str, after: str, fromfile: str, tofile: str) -> str:
    """The unified diff from `before` to `after`, marking a last line without a newline."""
    lines = difflib.unified_diff(before.splitlines(keepends=True), after.splitlines(keepends=True),
                                 fromfile=fromfile, tofile=tofile)
    return "".join(line if line.endswith("\n") else line + "\n\\ No newline at end of file\n" for line in lines)


def candidate_key(note: str, start: str, final: str, inputs: dict) -> str:
    """The proposal key of the workflow's candidate: it binds the start text, the candidate and the context."""
    return digest(json.dumps({"artifact": note, "start-sha256": sha256(start), "final-sha256": sha256(final),
                              "context-sha256": digest(json.dumps(inputs, sort_keys=True))}, sort_keys=True))


def revised_key(key: str, revised: str) -> str:
    """The proposal key of a revised candidate: the workflow candidate's key and the revised text."""
    return digest(json.dumps({"candidate-key": key, "revised-sha256": sha256(revised)}, sort_keys=True))


def revised_files(note: str, start: str, final: str, revised: str) -> dict[str, str]:
    """The run's `artifact/` files of a revised candidate: the text, its diff from the note and from `final`."""
    return {REVISED: revised, REVISED_DIFF: diff(start, revised, note, f"{note} (revised candidate)"),
            REVISION_DIFF: diff(final, revised, f"{note} (candidate)", f"{note} (revised candidate)")}


def revised_problems(root: Path, note: str, start: str, revised: str) -> list[str]:
    """What a revised candidate breaks: the candidate bounds of `artifact_bounds()`, and no text to publish.

    The per-pass bounds of an edit operation (`preserved()`) do not apply:
    the revision is the operator's.
    """
    problems = artifact_bounds(root, note, start, revised, validation_fails(root, note, start))
    if revised == start:
        problems.append("the revised candidate is the note's current text; reject the candidate instead")
    return problems


def publication_instruction(revised: bool, warnings: Sequence[str] = (), *, change: str, notice: str = "") -> str:
    """What the operator does at the publication stop, for the candidate or for a revised candidate.

    `warnings` are the text's new validation warnings (`new_warnings()`); the text names each one.
    `change` is the workflow's way to change the candidate otherwise, such as revise's `--plan`.
    `notice` is what else the workflow tells the operator before the decision; it opens the text.
    """
    warned = ("" if not warnings else
              "The text to publish has validation warnings the note did not have: " + "; ".join(warnings)
              + ". Tell the operator each one before asking for the decision; a warning does not block "
              "approval. ")
    warned = notice + warned
    inspect = ("Inspect final.md and final.diff" if not revised else
               f"The candidate was revised. Inspect the revised candidate {REVISED}, {REVISION_DIFF} (from the "
               f"workflow's candidate final.md) and {REVISED_DIFF} (from the note)")
    return (f"{warned}{inspect}. Record the operator's decision on the one item of {PUBLICATION}: "
            "`approved`, or `rejected` or `deferred` with the operator's reason, with `decided-by: operator` "
            "and `decided-at`. Approve that file, then repeat. To accept the candidate with a revision, supply "
            f"the full revised text with --revised FILE; to revise it otherwise, {change}. Editing the files "
            "under artifact/ is not a workflow input.")


def publication(run: Run, root: Path, note: str, start: str, final: str, *,
                inputs: dict, command: str, change: str, revised: str | None = None,
                warnings: Sequence[str] = (), notice: str = "") -> dict | None:
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

    With `revised`, the operator's revised candidate captured by the run,
    `final.md` stays the workflow's candidate, the question is `revised.md`
    and the key also binds the revised text (`revised_key()`).

    `warnings` are the new validation warnings of the text to publish; the
    waiting text names them. They bind no key. `change` is the workflow's
    way to change the candidate otherwise, and `notice` what else it tells
    the operator (`publication_instruction()`).
    """
    root = root.resolve()
    name = PUBLICATION
    existed = (run.artifact / name).is_file()
    expected = {CANDIDATE: final, "final.diff": diff(start, final, note, f"{note} (candidate)")}
    if revised is not None:
        expected |= revised_files(note, start, final, revised)
    # Check before answer() restores a missing manifest from its operator record.
    changed = operator.edited(run, name)
    for filename, text in expected.items():
        path = (run.artifact / filename).resolve()
        if not path.is_relative_to(run.artifact.resolve()):
            raise ValueError(f"publication file outside run artifacts: {filename}")
        changed |= (path.read_text(encoding="utf-8") != text if path.is_file() else existed)
    question = run.accept(CANDIDATE, final)
    if revised is not None:
        question = run.accept(REVISED, revised)
    unchanged(root, note, start, question)
    for filename, text in expected.items():
        if filename not in (CANDIDATE, REVISED):
            run.accept(filename, text)
    published = final if revised is None else revised
    proposal = answers.pending(question.relative_to(root).as_posix(), published.encode("utf-8"))
    key = candidate_key(note, start, final, inputs)
    if revised is not None:
        key = revised_key(key, revised)
    approved = operator.answer(run, name, proposal, key=key)
    instruction = publication_instruction(revised is not None, warnings, change=change, notice=notice)
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
    asked = question.relative_to(root).as_posix()
    if not problems and ((data.get("question"), data.get("question-sha256"))
                         != (asked, answers.sha(published.encode("utf-8")))):
        problems = [f"the answers name the question {data.get('question')}, not the text to publish {asked}"]
    if not problems and data["items"][0]["state"] != "approved":
        item = data["items"][0]
        problems = [f"the operator's answer is `{item['state']}`"
                    + (f": {item['reason']}" if item.get("reason") else "")]
    if problems:
        return operator.waiting(run, root, name, "The approved answers do not authorize publication: "
                                + "; ".join(problems) + ". No artifact was written. " + instruction, command)
    return None


# --- The publication stop of a workflow ------------------------------------------------------
#
# Every rewrite run, and a revise run whose candidate adds a validation
# warning, end the same way: the candidate `final.md` waits for approval, the
# operator may accept it with a revision, and the note is written once. The
# workflow's report carries the fields `proposed`, `revised_candidate`,
# `new_warnings` and `waiting_for`; `publish()` returns why the text is not
# written yet.

REVISED_RECORD = "revised.json"
"""The revised candidate the run captured: its text, and the workflow candidate's hash and key it revises."""
PUBLICATION_FILES = (CANDIDATE, "final.diff", PUBLICATION, REVISED, REVISED_DIFF, REVISION_DIFF)
"""The files a run writes at its publication stop; one of them is the last a run waiting there accepted."""
NOT_AT_PUBLICATION = ("the run of {artifact} for its current text is not waiting at its publication stop; repeat "
                      "the run and supply the revised candidate when its report waits on publication-answers.md")


def revised_report_files(root: Path, run: Run) -> dict[str, str]:
    """The report's names for the files of a revised candidate."""
    return {"candidate": (run.artifact / CANDIDATE).relative_to(root).as_posix(),
            "revised": (run.artifact / REVISED).relative_to(root).as_posix(),
            "diff-from-candidate": (run.artifact / REVISION_DIFF).relative_to(root).as_posix(),
            "diff-from-note": (run.artifact / REVISED_DIFF).relative_to(root).as_posix()}


def revision(run: Run, root: Path, note: str, start: str, final: str, context: dict, report) -> str | None:
    """The revised candidate the run captured, while `final` is the candidate it revises; otherwise None.

    A revision of another candidate is withdrawn: its record and files are
    removed and the report says why. The record keeps the key of the current
    candidate, so a later `supply_revised()` binds the same context.
    """
    path = run.root / REVISED_RECORD
    if not path.is_file():
        return None
    record = json.loads(path.read_text(encoding="utf-8"))
    if record["candidate-sha256"] != answers.sha(final.encode("utf-8")):
        path.unlink()
        for name in (REVISED, REVISED_DIFF, REVISION_DIFF):
            (run.artifact / name).unlink(missing_ok=True)
        report.revised_candidate = {"withdrawn": "The workflow's candidate changed since the revised candidate was "
                                                 "supplied, so the revised candidate is withdrawn. Supply it again "
                                                 "with --revised if it still applies to the new candidate."}
        return None
    key = candidate_key(note, start, final, context)
    if record["candidate-key"] != key:
        observations.atomic_json(path, {**record, "candidate-key": key})
    report.revised_candidate = revised_report_files(root, run)
    return record["text"]


def publish(run: Run, root: Path, note: str, start: str, final: str, context: dict, brief: dict[str, str],
            command: str, report, *, change: str, notice: str = "") -> tuple[str, str | None]:
    """Stop at publication for the changed `final`, or write the approved text.

    Returns the text to publish and, while it is not written, why. `start`
    is the text the note must hold for the write: the run's start text, or
    the text the run last published itself. The text to publish is `final`,
    or the operator's revised candidate while it revises `final`
    (`revision()`). The captured `brief` is checked before the stop and again
    before the write (`unchanged_brief()`). `notice` opens the waiting text
    (`publication_instruction()`).
    """
    unchanged_brief(root, note, start, brief)
    revised = revision(run, root, note, start, final, context, report)
    published = final if revised is None else revised
    report.proposed = (run.artifact / (CANDIDATE if revised is None else REVISED)).relative_to(root).as_posix()
    report.new_warnings = new_warnings(root, note, start, published)
    report.waiting_for = publication(run, root, note, start, final, inputs=context, command=command, change=change,
                                     revised=revised, warnings=report.new_warnings, notice=notice)
    if report.waiting_for is None:
        unchanged_brief(root, note, start, brief)
        apply(root, note, start, published, root / report.proposed)
        return published, None
    what = "" if revised is None else ", the operator's revised candidate"
    return published, (f"The proposed text is {report.proposed}{what}; it is not applied: "
                       "final publication needs explicit approval.")


def at_publication(run_dir: Path) -> bool:
    """Whether the run's last invocation ended at its publication stop.

    It did when the last file the run accepted is one of `PUBLICATION_FILES`.
    """
    log = run_dir / "log.jsonl"
    last = None
    if log.is_file():
        for line in log.read_text(encoding="utf-8").splitlines():
            event = json.loads(line)
            if event.get("event") == "accepted":
                last = event.get("path")
    return last in PUBLICATION_FILES


def revised_source(run_dir: Path, source: Path, note: str) -> None:
    """Refuse (ValueError) a revised candidate supplied from inside the run's `artifact/`, or a missing run."""
    if source.resolve().is_relative_to(run_dir.resolve() / "artifact"):
        raise ValueError("supply the revised candidate from a file outside the run's artifact/ directory; "
                         "the run captures it there")
    if not run_dir.is_dir():
        raise ValueError(NOT_AT_PUBLICATION.format(artifact=note))


def supply_revised(run: Run, root: Path, note: str, revised: str, command: str, *, change: str) -> dict:
    """Capture the operator's revised candidate at the publication stop of `run`; launch nothing.

    Refuses (ValueError) unless the run of the note's current text waits at
    its publication stop, the note holds the text the run last knew
    (`known_text()`), `final.md` is the candidate the run proposed and the
    revised text passes `revised_problems()`. A refusal changes nothing.
    Otherwise the text is captured in `REVISED_RECORD` and as
    `artifact/revised.md`, with its diffs, and the pending publication
    answers are replaced by one over `revised.md`, which withdraws any
    approval. A second revision replaces the first in the same way. Returns
    the report's `proposed`, `revised-candidate`, `new-warnings`,
    `not-applied` and `waiting-for`.
    """
    record = operator.recorded(run, PUBLICATION)
    start_path, final_path = run.artifact / START, run.artifact / CANDIDATE
    if record is None or not at_publication(run.root) or not start_path.is_file() or not final_path.is_file():
        raise ValueError(NOT_AT_PUBLICATION.format(artifact=note))
    start, final = known_text(root, run.root), final_path.read_text(encoding="utf-8")
    if (root / note).read_text(encoding="utf-8") != start:
        raise ValueError(f"{note} no longer holds the text the run last knew: its start text or the text it "
                         "last published")
    captured = run.root / REVISED_RECORD
    if captured.is_file():
        earlier = json.loads(captured.read_text(encoding="utf-8"))
        candidate, key = earlier["candidate-sha256"], earlier["candidate-key"]
    else:
        asked = frontmatter.parse(record["proposal"]).data
        if asked.get("question") != final_path.relative_to(root).as_posix():
            raise ValueError(NOT_AT_PUBLICATION.format(artifact=note))
        candidate, key = asked.get("question-sha256"), record["input-key"]
    if answers.sha(final.encode("utf-8")) != candidate:
        raise ValueError(f"{final_path.relative_to(root).as_posix()} is not the candidate the run proposed; repeat "
                         "the run to restore it, then supply the revised candidate")
    problems = revised_problems(root, note, start, revised)
    if problems:
        raise ValueError("the revised candidate is refused; the candidate and its pending answers are kept: "
                         + "; ".join(problems))
    observations.atomic_json(captured, {"text": revised, "candidate-sha256": candidate, "candidate-key": key})
    for name, text in revised_files(note, start, final, revised).items():
        run.accept(name, text)
    question = run.artifact / REVISED
    operator.answer(run, PUBLICATION, answers.pending(question.relative_to(root).as_posix(), revised.encode("utf-8")),
                    key=revised_key(key, revised))
    proposed = question.relative_to(root).as_posix()
    warnings = new_warnings(root, note, start, revised)
    return {"proposed": proposed, "revised-candidate": revised_report_files(root, run), "new-warnings": warnings,
            "not-applied": (f"The proposed text is {proposed}, the operator's revised candidate; it is not "
                            "applied: final publication needs explicit approval."),
            "waiting-for": operator.waiting(run, root, PUBLICATION,
                                            publication_instruction(True, warnings, change=change), command)}


# --- Automatic publication ---------------------------------------------------------------------
#
# A revise run writes its candidate to the note without a stop when no
# operator decision is needed (`revise._run_plan()`). Each such write is
# recorded in `PUBLISHED` in the run directory. The record also says whether
# the run is open: its last invocation ended waiting or stopped. An open run
# is found by the text it last published (`run_dir()`).

PUBLISHED = "published.json"
"""The run's automatic publications, in order, and whether the run is open."""
PUBLICATIONS_DIR = "publications"
"""Where a run keeps, under `artifact/`, each text it published automatically and its diff."""


def published(run_dir: Path) -> dict | None:
    """The run's record of its automatic publications; None when it published nothing automatically."""
    path = run_dir / PUBLISHED
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def known_text(root: Path, run_dir: Path) -> str:
    """The text the note must hold for the run to write it: the text the run last published, or its start text."""
    record = published(run_dir)
    if record is None:
        return (run_dir / "artifact" / START).read_text(encoding="utf-8")
    return (root / record["publications"][-1]["text"]).read_text(encoding="utf-8")


def record_publication(run: Run, root: Path, note: str, before: str, text: str, entries: list[str],
                       at: str) -> dict:
    """Write `text` over `before` and record it as the run's next automatic publication; return its record.

    The text and its diff from `before` are kept under
    `artifact/publications/`. The note is written only while it holds
    `before` (`apply()`); otherwise `Conflict`, and nothing is recorded.
    `entries` names the plan entries the publication covers; `at` is the time.
    """
    record = published(run.root) or {"open": True, "publications": []}
    number = len(record["publications"]) + 1
    path = run.accept(f"{PUBLICATIONS_DIR}/{number}.md", text)
    changes = run.accept(f"{PUBLICATIONS_DIR}/{number}.diff",
                         diff(before, text, note, f"{note} (publication {number})"))
    apply(root, note, before, text, path)
    entry = {"number": number, "text": path.relative_to(root).as_posix(), "sha256": sha256(text),
             "diff": changes.relative_to(root).as_posix(), "before-sha256": sha256(before), "entries": entries,
             "at": at}
    record["publications"].append(entry)
    observations.atomic_json(run.root / PUBLISHED, {**record, "open": True})
    return entry


def mark_open(run_dir: Path, is_open: bool) -> None:
    """Record whether a run that published automatically is open after this invocation; others have no record."""
    record = published(run_dir)
    if record is not None and record["open"] != is_open:
        observations.atomic_json(run_dir / PUBLISHED, {**record, "open": is_open})


def run_dir(root: Path, workflow: str, note: str) -> Path:
    """The run of `workflow` over the note's current text, under `runs/v2/<workflow>/<note without .md>/`.

    An open run whose last automatic publication is the note's current text
    is that run (`PUBLISHED`). Otherwise the run is the first directory named
    by the hash prefix of the text, then `-2`, `-3` and so on, that has
    published nothing automatically: a run that published is never found
    again by its start text, so a note reverted to that text opens a new
    run. The same command on the same text finds the same run and continues
    it by replay; another text opens another run.
    """
    text = (root / note).read_text(encoding="utf-8")
    first = run_dir_for(root, workflow, note, text)
    current = sha256(text)
    if first.parent.is_dir():
        for found in sorted(first.parent.iterdir()):
            record = published(found) if found.is_dir() else None
            if record is not None and record["open"] and record["publications"][-1]["sha256"] == current:
                return found
    found, number = first, 1
    while published(found) is not None:
        number += 1
        found = first.with_name(f"{first.name}-{number}")
    return found


def run_dir_for(root: Path, workflow: str, note: str, text: str) -> Path:
    """The run of `workflow` over `text` as the note's text; `run_dir()` gives it for the current text."""
    return root / gates.RUNS / workflow / note.removesuffix(".md") / sha256(text)[:12]


def guarded_changes(root: Path, before: dict[str, str], note: str, final: str | None) -> list[str]:
    """The paths the checkout guard saw change since `before`, less `note` when it holds the applied `final`."""
    changed = gates.changed_paths(before, gates.checkout_state(root))
    path = root / note
    if final is not None and path.is_file() and path.read_text(encoding="utf-8") == final:
        changed = [rel for rel in changed if rel != note]    # the workflow's own write
    return changed
