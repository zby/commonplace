"""Writing one checkout file from workflow outputs: bounds, the single write and the guard.

A workflow never lets a worker write the checkout. A worker's edited text is
an output; code checks it against hard bounds (`bounds()`) and keeps the
accepted text in memory and in the run's `artifact/` directory. The next
step works on that text, not on the file. Only a publication writes the
file, through `apply()`, and only over the text the run last knew: its
start text, or the text it last published itself. Any other text is a
change made outside the run, and `Conflict` stops the write. `apply()`
holds the note's publication lock (`publication_lock()`) across the check
and the write, so two runs on one note cannot both publish over the same
text.

Every invocation of a revise or rewrite workflow is a new run, in
`new_run_dir()`: `<runs>/<workflow>/<note path without .md>/<UTC stamp>/`.
No run is repeated or resumed. The run records the hash of its start text
and of the brief it captured in `START_RECORD` (`begin()`). A run publishes
automatically (`record_publication()`), before a per-item pass is asked for
proposals and at the end of its plan. A candidate it held (`hold()`) is
published at most once, when a later `commonplace-revise publish RUN` names
it (`publish_held()`). Each publication is recorded in `PUBLISHED`.

`guarded_changes()` is the checkout guard's finding minus the workflow's own
write: the file is dropped from the changed paths when it holds exactly the
final text the run applied.
"""

from __future__ import annotations

import contextlib
import difflib
import json
import re
import time
import uuid
from collections.abc import Iterator
from pathlib import Path

import workjig

from commonplace.headless.jobs import Run, run_lock
from commonplace.lib import answers, frontmatter
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.naming import (
    WRITE_BRIEF_TYPE,
    slugify_note_filename,
    write_brief_name_for,
)
from commonplace.lib.note_parser import blank_fenced_code_blocks, find_markdown_links
from commonplace.lib.quote_matching import normalize_text
from commonplace.lib.quote_verification import parse_prose_citations
from commonplace.lib.review_workflows import gates, observations, results
from commonplace.lib.validation import CheckResults, ValidationRun

CANDIDATE = "final.md"
"""The candidate a run holds for the operator, under the run's `artifact/`."""
START = "start.md"
"""The note's text when the run started, which the run may replace."""
REVISED = "revised.md"
"""The revised candidate: the operator's revision of `final.md`, supplied with `publish RUN --revised FILE`."""
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


def bounds(root: Path, note: str, start: str, text: str, baseline: set[str], *, allow_h1: bool = False) -> list[str]:
    """The hard bounds an edited note breaks; empty when it keeps them.

    Keep the frontmatter title, type and brief declaration, and the H1 unless
    the specialized title check allows it. Remove `user-verified` after a body
    change. The validator finds
    no failure that the start text did not have (`baseline`).
    """
    parsed, before = frontmatter.parse(text), frontmatter.parse(start)
    if not frontmatter.opens_frontmatter(text) or not parsed.ok:
        return ["the edited note's frontmatter does not parse; keep the note's frontmatter"]
    problems = [f"frontmatter `{key}` changed; keep it as it was" for key in PRESERVED
                if parsed.data.get(key) != before.data.get(key)]
    parts, start_parts = results.note_parts(text), results.note_parts(start)
    if not allow_h1 and start_parts is not None and parts["title"] != start_parts["title"]:
        problems.append(f"the H1 changed; keep `# {start_parts['title']}`")
    if (start_parts is None or parts["body"] != start_parts["body"]) and "user-verified" in parsed.data:
        problems.append("the body changed, so remove `user-verified` from the frontmatter")
    problems += [f"validation: {fail}" for fail in added(validation_fails(root, note, text), baseline)]
    return problems


def artifact_bounds(root: Path, artifact: str, start: str, text: str, baseline: set[str]) -> list[str]:
    """The hard bounds a revised artifact breaks; empty when it keeps them.

    An artifact with frontmatter keeps the note bounds of `bounds()`. An
    artifact without frontmatter gains none, keeps its first H1 and adds no
    validation failure. This is the default check; claim title repair has its
    own narrower check.
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


_DESCRIPTION_LINE = re.compile(r"^description:[^\r\n]+", re.MULTILINE)
_NOTE_H1 = re.compile(r"\A((?:[ \t]*\r?\n)*# )([^\r\n]+)")


def title_relocation(note: str, start: str, text: str) -> dict[str, str] | None:
    """The session agent's move, if a published H1 change needs a different filename."""
    before, after = results.note_parts(start), results.note_parts(text)
    if not before or not after or before["title"] == after["title"]:
        return None
    title = after["title"]
    destination = Path(note).with_name(f"{slugify_note_filename(title)}.md").as_posix()
    if destination == note:
        return None
    return {"note": note, "new-title": title, "destination": destination}


def claim_title_bounds(root: Path, note: str, start: str, text: str, baseline: set[str]) -> list[str]:
    """Allow only a supported claim title and description edit at the same path."""
    before, after = frontmatter.parse(start), frontmatter.parse(text)
    if (not before.ok or not after.ok or "title-as-claim" not in (before.data.get("traits") or ())
            or "user-verified" in before.data or "title" in before.data):
        return ["claim title repair requires an unverified claim-titled note without a frontmatter title"]

    def masked(value: str) -> str | None:
        body = frontmatter.strip(value)
        header, heading = value[:len(value) - len(body)], _NOTE_H1.match(body)
        header, count = _DESCRIPTION_LINE.subn("description:", header)
        if count != 1 or heading is None or not heading[2].strip():
            return None
        return header + heading[1] + body[heading.end():]

    start_mask = masked(start)
    if start_mask is None or start_mask != masked(text):
        return ["change only the first H1 and the description line; keep all other text exactly"]
    if ({k: v for k, v in before.data.items() if k != "description"}
            != {k: v for k, v in after.data.items() if k != "description"}):
        return ["keep every frontmatter field except description unchanged"]
    old_title, new_title = results.note_parts(start)["title"], results.note_parts(text)["title"]
    if not new_title or new_title == old_title:
        return ["repair the H1, or return unchanged with a reason"]
    try:
        relocation = title_relocation(note, start, text)
    except ValueError as error:
        return [f"choose a title suitable for relocation: {error}"]
    if relocation and ((root / relocation["destination"]).exists()
                       or (root / relocation["destination"]).is_symlink()):
        return [f"the title's relocation destination already exists: {relocation['destination']}"]
    return bounds(root, note, start, text, baseline, allow_h1=True)


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


LOCKS = gates.STATE / "publication-locks"
"""One lock directory per note, `<LOCKS>/<note path without .md>/`, held while a publication writes the note."""
LOCK_WAIT = 60.0
"""Seconds a publication waits for another publication of the same note."""


@contextlib.contextmanager
def publication_lock(root: Path, note: str, wait: float = LOCK_WAIT) -> Iterator[None]:
    """Hold the note's publication lock, shared by every revise and rewrite run and by `publish`.

    Run locks are per run, and two runs on one note have two run
    directories, so they do not exclude each other's publications. This
    lock does. It waits up to `wait` seconds, then raises Conflict.
    """
    lock, deadline = workjig.hold(root / LOCKS / Path(note).with_suffix("")), time.monotonic() + wait
    while True:
        try:
            lock.__enter__()
            break
        except workjig.RunBusyError:
            if time.monotonic() >= deadline:
                raise Conflict(f"another publication of {note} holds its lock; nothing was written") from None
            time.sleep(0.05)
    try:
        yield
    finally:
        lock.__exit__(None, None, None)


def apply(root: Path, note: str, start: str, final: str, proposed: Path) -> None:
    """Write `final` to the note, atomically and only over `start`; any other text is a Conflict.

    The check and the write happen under the note's publication lock.
    """
    with publication_lock(root, note):
        unchanged(root, note, start, proposed)
        write_text(root / note, final)


def diff(before: str, after: str, fromfile: str, tofile: str) -> str:
    """The unified diff from `before` to `after`, marking a last line without a newline."""
    lines = difflib.unified_diff(before.splitlines(keepends=True), after.splitlines(keepends=True),
                                 fromfile=fromfile, tofile=tofile)
    return "".join(line if line.endswith("\n") else line + "\n\\ No newline at end of file\n" for line in lines)


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
        problems.append("the revised candidate is the note's current text; do not publish instead")
    return problems


# --- The run directory and its start ------------------------------------------------------------

START_RECORD = "start.json"
"""The run's note, the SHA-256 of its start text and of the write brief it captured (null without one)."""


def new_run_dir(root: Path, workflow: str, note: str) -> Path:
    """Create the new run of `workflow` on `note`: `runs/v2/<workflow>/<note without .md>/<UTC stamp>/`.

    The stamp and its collision suffix are the gate sweep's (`gates.new_run_dir()`).
    A note's runs are listed in time order under the note's directory.
    """
    return gates.new_run_dir(root / gates.RUNS / workflow / note.removesuffix(".md"))


def begin(run_dir: Path, note: str, start: str, brief: dict[str, str]) -> None:
    """Record the run's start in `START_RECORD`: the note, its start text's hash and the captured brief's hash."""
    observations.atomic_json(run_dir / START_RECORD, {
        "note": note, "sha256": sha256(start),
        "brief-sha256": sha256(brief["brief"]) if "brief" in brief else None})


def started(run_dir: Path) -> dict | None:
    """The run's `START_RECORD`; None for a run that has none."""
    path = run_dir / START_RECORD
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def made_for(run_dir: Path) -> str | None:
    """The SHA-256 of the text the run left the note holding: its publication, or its start text.

    None when the run recorded neither.
    """
    record, start = published(run_dir), started(run_dir)
    if record is not None and record["publications"]:
        return record["publications"][-1]["sha256"]
    return None if start is None else start["sha256"]


# --- Publication ---------------------------------------------------------------------------------
#
# A revise run writes its candidate to the note without a stop when no
# operator decision is needed (`revise._run_plan()`). A candidate that adds a
# validation warning, and every rewrite candidate, is held (`hold()`): the run
# ends with it in `artifact/final.md`, and `commonplace-revise publish RUN`
# publishes it later (`publish_held()`). Either way the publication is
# recorded in `PUBLISHED` in the run directory.

PUBLISHED = "published.json"
"""The run's publications, in order: its automatic ones, then the operator's publication of a held candidate."""
PUBLICATIONS_DIR = "publications"
"""Where a run keeps, under `artifact/`, each text it published and its diff."""
AUTOMATIC = "automatic"
"""Who decided an automatic publication: no one; the workflow's rule published it."""
HELD = "held.json"
"""The candidate a run held for the operator: its path and hash, its diff and the diff's hash, its new warnings,
the plan entries it covers, and for a rewrite the accepted review and its hash."""
PUBLISH = "commonplace-revise publish {run}"


def published(run_dir: Path) -> dict | None:
    """The run's record of its publications; None when it published nothing."""
    path = run_dir / PUBLISHED
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def record_publication(run_dir: Path, root: Path, note: str, before: str, text: str, entries: list[str],
                       at: str, *, decided_by: str = AUTOMATIC, revised: bool = False) -> dict:
    """Write `text` over `before` and record it as the run's next publication; return its record.

    The text and its diff from `before` are kept under
    `artifact/publications/`. The note is written only while it holds
    `before` (`apply()`); otherwise `Conflict`, and nothing is recorded.
    `entries` names the plan entries the publication covers; `at` is the
    time; `decided_by` is `AUTOMATIC` or `operator`, and `revised` says that
    the operator published a revised candidate.
    """
    relocation = title_relocation(note, before, text)
    record = published(run_dir) or {"publications": []}
    number = len(record["publications"]) + 1
    artifact = run_dir / "artifact"
    path = artifact / PUBLICATIONS_DIR / f"{number}.md"
    changes = artifact / PUBLICATIONS_DIR / f"{number}.diff"
    write_text(path, text)
    write_text(changes, diff(before, text, note, f"{note} (publication {number})"))
    apply(root, note, before, text, path)
    entry = {"number": number, "text": path.relative_to(root).as_posix(), "sha256": sha256(text),
             "diff": changes.relative_to(root).as_posix(), "before-sha256": sha256(before), "entries": entries,
             "at": at, "decided-by": decided_by, "revised": revised}
    if relocation is not None:
        entry["relocation"] = relocation
    record["publications"].append(entry)
    observations.atomic_json(run_dir / PUBLISHED, record)
    return entry


def hold(run: Run, root: Path, note: str, start: str, final: str, entries: list[str], *,
         review: str | None = None) -> dict:
    """Keep `final` as the candidate the run holds for the operator; write nothing to the note.

    `start` is the note's text the candidate is held over: the run's start
    text, or its last publication. The run keeps `artifact/final.md`, its
    diff `final.diff` from `start` and `HELD`, with the hashes of the text
    held over, of the candidate and of its diff, its new
    validation warnings (`new_warnings()`) and the plan `entries` it covers.
    A rewrite also names its accepted `review`, a file the run kept, with
    its hash. `publish_held()` refuses when any of these files changed.
    Returns the report's `held`: those files, the warnings and the commands
    that publish the candidate or the operator's revision of it.
    """
    candidate = run.accept(CANDIDATE, final)
    shown = diff(start, final, note, f"{note} (candidate)")
    changes = run.accept("final.diff", shown)
    warnings = new_warnings(root, note, start, final)
    rel = candidate.relative_to(root).as_posix()
    reviewed = ({"review": review, "review-sha256": sha256((root / review).read_text(encoding="utf-8"))}
                if review is not None else {})
    observations.atomic_json(run.root / HELD, {"candidate": rel, "sha256": sha256(final),
                                               "before-sha256": sha256(start),
                                               "diff": changes.relative_to(root).as_posix(),
                                               "diff-sha256": sha256(shown), "new-warnings": warnings,
                                               "entries": entries, **reviewed})
    command = PUBLISH.format(run=run.root.resolve().relative_to(root).as_posix())
    return {"candidate": rel, "diff": changes.relative_to(root).as_posix(), "new-warnings": warnings,
            "command": command, "revised-command": command + " --revised FILE"}


def publish_held(root: Path, run_dir: Path, revised: str | None = None, source: Path | None = None) -> dict:
    """Publish the candidate the run at `run_dir` held, or the operator's `revised` text; launch nothing.

    Naming the run is the operator's approval of its exact candidate. The
    note is written only while it holds the text the candidate was held
    over (the run's start text, or the run's last automatic publication),
    the write brief is the one the run captured, `final.md` is the candidate
    the run held, and the operator has not published it already. A revised text, read from the
    file `source` outside the run's `artifact/`, must also pass
    `revised_problems()`; the run keeps it as `artifact/revised.md` with its
    diffs from the note and from `final.md`. The other files the operator
    inspects, `final.diff` and a rewrite's accepted review, must also hold
    what the run held (`HELD`). ValueError, with nothing written, when a
    check fails. Returns the publication record and the new
    validation warnings of the published text.
    """
    root, run_dir = root.resolve(), run_dir.resolve()
    rel = run_dir.relative_to(root).as_posix()
    if not (run_dir / HELD).is_file() or started(run_dir) is None:
        raise ValueError(f"{rel} holds no candidate to publish")
    if source is not None and source.resolve().is_relative_to(run_dir / "artifact"):
        raise ValueError("supply the revised candidate from a file outside the run's artifact/ directory")
    with run_lock(run_dir):
        held, start_record = json.loads((run_dir / HELD).read_text(encoding="utf-8")), started(run_dir)
        note, record = start_record["note"], published(run_dir) or {"publications": []}
        if any(entry["decided-by"] != AUTOMATIC for entry in record["publications"]):
            raise ValueError(f"{rel} already published its held candidate; it publishes it at most once")
        final = (root / held["candidate"]).read_text(encoding="utf-8")
        if sha256(final) != held["sha256"]:
            raise ValueError(f"{held['candidate']} is not the candidate the run held; it was changed after the run")
        for name in ("diff", "review"):
            path = root / held[name] if name in held else None
            if path is not None and (not path.is_file()
                                     or sha256(path.read_text(encoding="utf-8")) != held[f"{name}-sha256"]):
                raise ValueError(f"{held[name]} is not the file the run held; it was changed after the run. "
                                 "Nothing was written")
        start = (run_dir / "artifact" / START).read_text(encoding="utf-8")
        last = record["publications"][-1]["text"] if record["publications"] else None
        base = start if last is None else (root / last).read_text(encoding="utf-8")
        path = root / note
        if (sha256(start) != start_record["sha256"] or sha256(base) != held["before-sha256"] or not path.is_file()
                or path.read_text(encoding="utf-8") != base):
            raise ValueError(f"{note} no longer holds the text the run held its candidate over; nothing was "
                             "written. A new run works on its current text")
        try:
            brief = capture_brief(root, note, start)
        except Stop as error:
            raise ValueError(f"the write brief cannot be read; nothing was written: {error}") from error
        if (sha256(brief["brief"]) if "brief" in brief else None) != start_record["brief-sha256"]:
            raise ValueError(f"the write brief of {note} changed since the run; nothing was written")
        text = final
        if revised is not None:
            problems = revised_problems(root, note, base, revised)
            if problems:
                raise ValueError("the revised candidate is refused; nothing was written: " + "; ".join(problems))
            for name, content in revised_files(note, base, final, revised).items():
                write_text(run_dir / "artifact" / name, content)
            text = revised
        try:
            entry = record_publication(run_dir, root, note, base, text, held.get("entries", []),
                                       observations.timestamp(), decided_by="operator",
                                       revised=revised is not None)
        except Conflict as conflict:
            raise ValueError(str(conflict)) from conflict
    report = {"run-dir": rel, "artifact": note, "published": entry, "new-warnings": new_warnings(root, note, base, text)}
    if revised is not None:
        artifact = (run_dir / "artifact").relative_to(root).as_posix()
        report["revised-candidate"] = {"candidate": held["candidate"], "revised": f"{artifact}/{REVISED}",
                                       "diff-from-candidate": f"{artifact}/{REVISION_DIFF}",
                                       "diff-from-note": f"{artifact}/{REVISED_DIFF}"}
    return report


def guarded_changes(root: Path, before: dict[str, str], note: str, final: str | None) -> list[str]:
    """The paths the checkout guard saw change since `before`, less `note` when it holds the applied `final`."""
    changed = gates.changed_paths(before, gates.checkout_state(root))
    path = root / note
    if final is not None and path.is_file() and path.read_text(encoding="utf-8") == final:
        changed = [rel for rel in changed if rel != note]    # the workflow's own write
    return changed
