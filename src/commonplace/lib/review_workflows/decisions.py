"""The operator-decision record: kept answers files, and a read-only listing of decisions on disk.

An answers file (`types/answers.md`) becomes a decision when a command keeps
its text in a run's `ANSWERS_DIR` (`keep_answers()`): the command that
consumes it, `commonplace-revise apply FILE`, which acts
on its approved items, or `commonplace-revise answers record FILE`
(`record_answers()`), for a file whose decisions nothing consumes. Naming
the file to either command is the operator's approval of its text; there is
no other approval step. Both keep the same record: the file's repository
path as `origin`, its text, the text's hash and the time. `kept_answers()`
is the one reader.

The listing (`entries()`) writes nothing. Its entries come from three places
under kb/workflow-state/data/current/:

- the revise and rewrite run directories, named by the hash prefix of the
  start text (older runs) or by their UTC start stamp: one entry per item of
  each kept answers file, with its state, decider and reason; one `pending`
  entry per answers file a run's continuation record (`CONTINUATION`) asks
  for that no kept record names; and one `pending` publication per held
  candidate (`edits.HELD`) the run has not published. A pending entry is
  `overtaken` instead when the note no longer holds the text the run left
  it: the note is gone, or its hash is not the run's last publication or,
  without one, its start text (`overtaken()`). This is computed when
  listing;
- the publications of revise and rewrite runs, `edits.PUBLISHED`: one entry
  per publication, of class `publication`, decided by `automatic` or by the
  operator through `publish RUN`, with the decision `published`;
- records of the two retired procedures (ADR 135), kept so that recorded
  operator decisions stay visible: operator records in full-pass run
  directories; full-pass packets, with the disposition, which was the
  workflow's judgment, and the resolution once it is not `pending`; and fix
  reports, written by an agent without a run, one entry per report pointing
  at it, since their tables are free-form.

Each entry says who proposed and who decided, and whether the decision
covered one item or a bundle. A publication is approval of the final text,
never of each edit that produced it. No statistic is computed.

`earlier()` reads the same kept answers for the revise and rewrite
workflows: the operator's decided items on edit proposals and on review
findings in the other revise and rewrite runs on one note, which a new run
carries over (`types/answers.md`, "Decisions carried over"). A decision on a
finding comes from answers whose question is a review result: the
`finding-answers-<key>.md` files of a triage, or those `revise.record()`
writes over a run's findings; the listing shows it with class `finding` and
names its criterion. An item's `resolution` goes wherever its `reason`
goes. `review_inputs()` renders the rejected findings per criterion as the
input a later review of the note against that criterion receives; the input
takes part in that result's freshness (`results.criterion_sha256()`).

`earlier_stops()` reads the operator's decisions on the stops of the other
revise runs on one note (`stop-answers.md`), which the next run's assessor
receives; they are never carried over.
"""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path

import yaml

from commonplace.headless.jobs import run_lock
from commonplace.lib import answers, frontmatter
from commonplace.lib.review_workflows import edits, gates, observations, results

# BACKCOMPAT: reads packets and fix reports written before the cutover - remove after the operator says the old records are dispensable
WORKFLOWS = ("revise", "rewrite", "full-pass")
"""Run families whose run directories may hold decisions; dated sweep directories hold none.

`full-pass` is the run family of the retired full-pass workflow (ADR 135)."""
PACKETS = gates.STATE / "packets"
"""Where the retired full-pass workflow kept one current packet per note."""
FIXES = Path("kb/workflow-state/data/current/fixes")
"""Where the retired fix procedure wrote its fix reports."""

ITEM_WIDTH = 80
_RUN = re.compile(r"(?:[0-9a-f]{12}|[0-9]{8}T[0-9]{6}Z)(?:-[0-9]+)?")
"""A revise or rewrite run directory: its UTC start stamp (`edits.new_run_dir()`), or, for a run made before
runs were named by time, the hash prefix of its start text; each with an optional number."""
AUTOMATIC = edits.AUTOMATIC
_ANSWERS = re.compile(r"([a-z0-9-]+?)-answers(?:-[0-9a-f]+)?\.md")
"""An answers file a workflow writes: `<pass>-answers.md` of a per-item pass, `finding-answers-<key>.md` of a
triage or a record, `stop-answers.md`; and in runs converted from operator records, `<pass>-answers-<key>.md`
and `publication-answers.md`."""
FINDING = "finding"
"""The class of answers whose question is a review result, and whose items are the result's findings."""
ANSWERS_DIR = "answers"
"""Where a run keeps the answers files it consumed or recorded, one JSON record per file (`keep_answers()`)."""
CONTINUATION = "continuation.json"
"""The work a revise run left unfinished (`revise.continuation()`); its items name the answers files they wait for."""
STOP_ANSWERS = "stop-answers.md"
"""The answers file of a revise plan that stops: one text item, whose question is the run's `plan.yaml`."""
RECORD = "commonplace-revise answers record {file}"
_AUTHORITY = {"user": "operator", "version-guard": "version-guard"}


class MalformedRecord(ValueError):
    """A decision record that cannot be read; the message names its path."""


def _entry(note: str, workflow: str, run: str | None, record: str, cls: str, proposed_by: str,
           decided_by: str, decision: str, unit: str, *, item: str | None = None, reason: str | None = None,
           key: str | None = None, at: str | None = None, resolution: str | None = None,
           refs: list[str] | None = None, carried_from: str | None = None, revised: bool = False) -> dict:
    return {"note": note, "workflow": workflow, "run": run, "record": record, "class": cls,
            "proposed-by": proposed_by, "decided-by": decided_by, "decision": decision, "unit": unit,
            "item": item, "reason": reason, "resolution": resolution, "refs": refs, "carried-from": carried_from,
            "revised": revised, "key": key, "at": at}


def _head(proposal: object, criterion: str | None = None) -> str:
    """One line naming an answered item.

    A finding: its criterion, level and reason. An edit proposal: its quote
    and change. A text to approve: its path.
    """
    if criterion is not None and isinstance(proposal, dict):
        line = f"{criterion}: {proposal.get('level')}: {proposal.get('reason')}"
    elif isinstance(proposal, dict) and "quote" in proposal:
        line = f"{proposal['quote']} -> {proposal.get('change')}"
    elif isinstance(proposal, dict) and "text" in proposal:
        line = str(proposal["text"])
    else:
        line = str(proposal)
    line = " ".join(line.split())
    return line if len(line) <= ITEM_WIDTH else line[:ITEM_WIDTH - 1] + "…"


# --- Kept answers --------------------------------------------------------------------------------

def keep_answers(run_dir: Path, origin: str, text: str) -> Path:
    """Keep the text of the answers file at the repository path `origin` in `run_dir`; return the record's path.

    The record is `ANSWERS_DIR/<file stem>-<hash of origin>.json` with
    `origin`, `sha256` (of the text), `at` (UTC) and `text`. Keeping the same
    file again replaces its record in that run.
    """
    path = run_dir / ANSWERS_DIR / f"{Path(origin).stem}-{answers.sha(origin.encode('utf-8'))[:8]}.json"
    observations.atomic_json(path, {"origin": origin, "sha256": answers.sha(text.encode("utf-8")),
                                    "at": observations.timestamp(), "text": text})
    return path


def kept_answers(root: Path, run_dir: Path) -> list[tuple[str, dict]]:
    """The kept answers of one run directory, each with its repository path; MalformedRecord when one breaks."""
    found = []
    for path in sorted((run_dir / ANSWERS_DIR).glob("*.json")):
        record = path.relative_to(root).as_posix()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not all(isinstance(data[key], str) for key in ("origin", "text", "at", "sha256")):
                raise KeyError("origin, text, at or sha256")
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise MalformedRecord(f"malformed kept answers: {record}: {error!r}") from error
        found.append((record, data))
    return found


def run_of(root: Path, path: Path) -> tuple[str, Path]:
    """The workflow and run directory of a file under a revise or rewrite run's `artifact/`; ValueError otherwise."""
    resolved = path.resolve()
    for workflow in EARLIER_WORKFLOWS:
        base = (root / gates.RUNS / workflow).resolve()
        if not resolved.is_relative_to(base):
            continue
        for parent in resolved.parents:
            if parent.name == "artifact" and parent.parent.parent != base and _RUN.fullmatch(parent.parent.name):
                return workflow, parent.parent
    raise ValueError(f"{path} is not a file under the artifact/ directory of a revise or rewrite run")


def record_answers(root: Path, path: Path) -> dict:
    """Keep an answers file that nothing consumes as the operator's decisions; launch nothing.

    The file lies under the `artifact/` of the revise or rewrite run that
    asked it, and the record is kept in that run. The validator must accept
    it against its question (`edits.answered()`); otherwise ValueError and
    nothing is kept. Recording the file again after a change, such as an
    added `resolution`, replaces the record.
    """
    root = root.resolve()
    _, run_dir = run_of(root, path)
    text = path.read_text(encoding="utf-8")
    _, problems = edits.answered(root, path, text)
    if problems:
        raise ValueError(f"the answers in {path.relative_to(root).as_posix()} are not valid; nothing was "
                         "recorded: " + "; ".join(problems))
    origin = path.resolve().relative_to(root).as_posix()
    with run_lock(run_dir):
        kept = keep_answers(run_dir, origin, text)
    data = json.loads(kept.read_text(encoding="utf-8"))
    return {"answers": origin, "recorded": kept.relative_to(root).as_posix(), "sha256": data["sha256"],
            "at": data["at"]}


def _criterion(root: Path, question: object) -> str | None:
    """The criterion id of the review result an answers file names as `question`; None when it cannot be read."""
    try:
        identity = answers.finding_criterion((root / str(question)).read_bytes())
        return None if identity is None else results.criterion_id(root, identity)
    except (OSError, ValueError):
        return None


# BACKCOMPAT: converted approve-a-text records name publication-answers.md - remove after the converted runs are deleted
def _revised(root: Path, run_dir: Path, proposal: str) -> bool:
    """Whether converted publication answers approved the run's revised candidate, not the workflow's candidate."""
    parsed = frontmatter.parse(proposal)
    question = parsed.data.get("question") if parsed.ok else None
    return question == (run_dir / "artifact" / edits.REVISED).relative_to(root).as_posix()


def _class(name: str) -> str:
    """The action class of an answers file, from its file name."""
    found = _ANSWERS.fullmatch(name)
    return found.group(1) if found else "answers"


def overtaken(root: Path, workflow: str, note: str, run_dir: Path) -> bool:
    """Whether the note no longer holds the text a revise or rewrite run left it: what its stops asked about.

    That text is the run's last publication, or its start text
    (`edits.made_for()`). A run that recorded neither is overtaken.
    """
    if workflow not in EARLIER_WORKFLOWS:
        return False
    expected = edits.made_for(run_dir)
    path = root / note
    return expected is None or not path.is_file() or observations.sha(path.read_bytes()) != expected


def _note(root: Path, workflow: str, run_dir: Path) -> str:
    return run_dir.parent.relative_to(root / gates.RUNS / workflow).as_posix() + ".md"


def _publications(root: Path, workflow: str, run_dir: Path) -> list[dict]:
    """One entry per publication of a revise or rewrite run (`edits.PUBLISHED`)."""
    record = edits.published(run_dir)
    if record is None:
        return []
    path = (run_dir / edits.PUBLISHED).relative_to(root).as_posix()
    return [_entry(_note(root, workflow, run_dir), workflow, run_dir.relative_to(root).as_posix(), path,
                   "publication", "workflow", given.get("decided-by", AUTOMATIC), "published", "bundle",
                   item=_head({"text": given["text"]}), key=given["sha256"], at=given["at"],
                   revised=bool(given.get("revised")))
            for given in record["publications"]]


def _kept(root: Path, workflow: str, run_dir: Path, shown: set[str] | None = None) -> list[dict]:
    """One entry per item of each answers file the run kept; only the records in `shown`, when given."""
    run = run_dir.relative_to(root).as_posix()
    note = _note(root, workflow, run_dir)
    waiting = "overtaken" if overtaken(root, workflow, note, run_dir) else "pending"
    found = []
    for record, data in kept_answers(root, run_dir):
        if shown is not None and record not in shown:
            continue
        cls = _class(Path(data["origin"]).name)
        proposer = "workflow" if cls == "publication" else "worker"   # a plan's `stop` is the assessor's
        parsed = frontmatter.parse(data["text"])
        revised = cls == "publication" and _revised(root, run_dir, data["text"])
        items = parsed.data.get("items") if parsed.ok else None
        if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
            found.append(_entry(note, workflow, run, record, cls, proposer, "operator", "invalid", "bundle",
                                key=data["sha256"], at=data["at"], revised=revised))
            continue
        criterion = _criterion(root, parsed.data.get("question"))
        for item in items:
            state = str(item.get("state"))
            pending = state == "pending"
            found.append(_entry(note, workflow, run, record, cls, proposer,
                                waiting if pending else str(item.get("decided-by")), waiting if pending else state,
                                "bundle" if cls == "publication" else "item",
                                item=_head(item.get("proposal"), criterion),
                                reason=item.get("reason"), resolution=item.get("resolution"),
                                refs=item.get("refs"), carried_from=item.get("carried-from"), revised=revised,
                                key=data["sha256"], at=None if pending else str(item.get("decided-at") or data["at"])))
    return found


def _waiting(root: Path, workflow: str, run_dir: Path, kept: set[str]) -> list[dict]:
    """The run's pending work for the operator: answers files nothing kept, and a held candidate not published."""
    run = run_dir.relative_to(root).as_posix()
    note = _note(root, workflow, run_dir)
    waiting = "overtaken" if overtaken(root, workflow, note, run_dir) else "pending"
    found = []
    path = run_dir / CONTINUATION
    if path.is_file():
        record = path.relative_to(root).as_posix()
        found += [_entry(note, workflow, run, record, _class(Path(file).name), "worker", waiting, waiting, "bundle",
                         item=file)
                  for item in json.loads(path.read_text(encoding="utf-8"))["items"]
                  for file in item.get("answers", []) if file not in kept]
    publications = (edits.published(run_dir) or {"publications": []})["publications"]
    if (run_dir / edits.HELD).is_file() and all(entry["decided-by"] == AUTOMATIC for entry in publications):
        held = json.loads((run_dir / edits.HELD).read_text(encoding="utf-8"))
        found.append(_entry(note, workflow, run, (run_dir / edits.HELD).relative_to(root).as_posix(),
                            "publication", "workflow", waiting, waiting, "bundle", item=held["candidate"],
                            key=held["sha256"]))
    return found


def _runs(root: Path, workflow: str) -> list[Path]:
    """The run directories of a revise or rewrite family, for every note, in path order."""
    base = root / gates.RUNS / workflow
    if not base.is_dir():
        return []
    found = {path.parent for name in (edits.START_RECORD, edits.PUBLISHED, CONTINUATION, edits.HELD)
             for path in base.rglob(name)}
    found |= {path.parent for path in base.rglob(ANSWERS_DIR) if path.is_dir()}
    return sorted(path for path in found if _RUN.fullmatch(path.name) and path.parent != base)


# BACKCOMPAT: reads operator records of the retired full-pass workflow - remove with the packet reader below
def _records(root: Path, run_dir: Path) -> list[tuple[str, dict]]:
    """The operator records of one full-pass run directory, each with its repository path."""
    found = []
    for path in sorted((run_dir / "operator").glob("*.json")):
        record = path.relative_to(root).as_posix()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data["name"], str) or "key" not in data or "proposal" not in data:
                raise KeyError("name, key or proposal")
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise MalformedRecord(f"malformed operator record: {record}: {error!r}") from error
        found.append((record, data))
    return found


# BACKCOMPAT: reads operator records of the retired full-pass workflow - remove with the packet reader below
def _operator(root: Path, workflow: str, run_dir: Path) -> list[dict]:
    run = run_dir.relative_to(root).as_posix()
    note = _note(root, workflow, run_dir)
    found = []
    for record, data in _records(root, run_dir):
        name, key = data["name"], data["key"]
        answer, at = data.get("answer"), data.get("answered-at")
        common = {"key": key, "at": at if answer is not None else None}
        stop = _ANSWERS.fullmatch(name)
        if stop:
            cls = stop.group(1)
            proposer = "workflow" if cls == "publication" else "worker"
            if answer is None:
                found.append(_entry(note, workflow, run, record, cls, proposer, "pending", "pending", "bundle",
                                    **common))
                continue
            parsed = frontmatter.parse(answer)
            items = parsed.data.get("items") if parsed.ok else None
            if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
                found.append(_entry(note, workflow, run, record, cls, proposer, "operator", "invalid", "bundle",
                                    **common))
                continue
            for item in items:
                state = str(item.get("state"))
                found.append(_entry(note, workflow, run, record, cls, proposer,
                                    "pending" if state == "pending" else str(item.get("decided-by")), state,
                                    "bundle" if cls == "publication" else "item", item=_head(item.get("proposal")),
                                    reason=item.get("reason"), resolution=item.get("resolution"),
                                    refs=item.get("refs"), carried_from=item.get("carried-from"), key=key,
                                    at=None if state == "pending" else str(item.get("decided-at") or at)))
        else:                               # a stop of an earlier workflow version, such as plan.yaml
            found.append(_entry(note, workflow, run, record, name, "workflow",
                                "pending" if answer is None else "operator",
                                "pending" if answer is None else "approve", "bundle", **common))
    return found


# BACKCOMPAT: reads packets and fix reports written before the cutover - remove after the operator says the old records are dispensable
def _packet(root: Path, path: Path) -> list[dict]:
    record = path.relative_to(root).as_posix()
    parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    data = parsed.data
    if not parsed.ok or "note" not in data or "disposition" not in data or "resolution" not in data:
        raise MalformedRecord(f"malformed packet: {record}: "
                              f"{'; '.join(parsed.errors) or 'needs note, disposition and resolution'}")
    note, run = str(data["note"]), data.get("run")
    found = [_entry(note, "full-pass", run, record, "packet", "worker", "agent", str(data["disposition"]), "bundle")]
    if data["resolution"] != "pending":
        authority = data.get("resolution-authority")
        found.append(_entry(note, "full-pass", run, record, "packet", "worker",
                            _AUTHORITY.get(authority, str(authority)), str(data["resolution"]), "bundle",
                            reason=data.get("resolution-summary"),
                            at=None if data.get("resolved-at") is None else str(data["resolved-at"])))
    return found


# BACKCOMPAT: reads packets and fix reports written before the cutover - remove after the operator says the old records are dispensable
def _notes(root: Path) -> dict[str, list[str]]:
    """Note paths under kb/ by file stem, for fix reports that name their note only by stem."""
    found: dict[str, list[str]] = {}
    for path in (root / "kb").rglob("*.md"):
        relative = path.relative_to(root)
        if relative.parts[1] not in ("reports", "workflow-state", "work") and not any(p.startswith(".") for p in relative.parts):
            found.setdefault(path.stem, []).append(relative.as_posix())
    return found


# BACKCOMPAT: reads packets and fix reports written before the cutover - remove after the operator says the old records are dispensable
def _fix_report(root: Path, path: Path, notes: dict[str, list[str]]) -> dict:
    record = path.relative_to(root).as_posix()
    parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    if not parsed.ok:
        raise MalformedRecord(f"malformed fix report: {record}: {'; '.join(parsed.errors)}")
    stem = path.name.removesuffix(".fix-report.md")
    matches = notes.get(stem, [])
    # The note's current path when exactly one note has the stem; otherwise the stem itself.
    note = matches[0] if len(matches) == 1 else parsed.data.get("note_path") or stem
    return _entry(str(note), "fix", None, record, "fix-report", "agent", "agent", "report", "bundle")


def _run_order(name: str) -> tuple[str, int]:
    """A run directory's name as its stamp and collision number, so `<stamp>-2` follows `<stamp>`."""
    stamp, _, number = name.partition("-")
    return stamp, int(number or 1)


def entries(root: Path) -> list[dict]:
    """Every decision entry, grouped by note and ordered by time where known (untimed last).

    One answers file may be kept by more than one run, such as by `answers
    record` and then by the run `apply` started; the same text is
    listed once, from the record kept last.
    """
    found: list[dict] = []
    runs = {workflow: _runs(root, workflow) for workflow in EARLIER_WORKFLOWS}
    kept: dict[str, set[str]] = {}                  # the origins of every kept answers file, by note
    latest: dict[tuple[str, str], tuple] = {}       # (origin, text hash) -> (time kept, run order, record)
    for workflow, listed in runs.items():
        for run_dir in listed:
            for record, data in kept_answers(root, run_dir):
                kept.setdefault(_note(root, workflow, run_dir), set()).add(data["origin"])
                same = (data["origin"], data["sha256"])
                latest[same] = max(latest.get(same, ("", (), "")), (data["at"], _run_order(run_dir.name), record))
    shown = {kept_last[-1] for kept_last in latest.values()}
    for workflow, listed in runs.items():
        for run_dir in listed:
            found.extend(_kept(root, workflow, run_dir, shown))
            found.extend(_publications(root, workflow, run_dir))
            found.extend(_waiting(root, workflow, run_dir, kept.get(_note(root, workflow, run_dir), set())))
    base = root / gates.RUNS / "full-pass"
    if base.is_dir():
        for records in sorted(base.rglob("operator")):
            if records.is_dir() and _RUN.fullmatch(records.parent.name):
                found.extend(_operator(root, "full-pass", records.parent))
    packets = root / PACKETS
    if packets.is_dir():
        for path in sorted(packets.rglob("*.md")):
            found.extend(_packet(root, path))
    fixes = root / FIXES
    reports = sorted(fixes.glob("*.fix-report.md")) if fixes.is_dir() else []
    if reports:
        notes = _notes(root)
        found.extend(_fix_report(root, path, notes) for path in reports)
    return sorted(found, key=lambda entry: (entry["note"], entry["at"] is None, entry["at"] or ""))


def text(found: list[dict]) -> str:
    """The readable listing: a heading per note, one line per decision."""
    lines: list[str] = []
    note = None
    for entry in found:
        if entry["note"] != note:
            note = entry["note"]
            lines.append(("\n" if lines else "") + note)
        fields = [entry["at"] or "-", entry["workflow"], entry["class"], entry["unit"],
                  f"{entry['proposed-by']}->{entry['decided-by']}", entry["decision"]]
        if entry["revised"]:
            fields.append("revised candidate")
        if entry["item"]:
            fields.append(f"item: {entry['item']}")
        if entry["reason"]:
            fields.append(f"reason: {entry['reason']}")
        if entry["resolution"]:
            fields.append(f"resolution: {entry['resolution']}")
        if entry["refs"]:
            fields.append(f"refs: {', '.join(entry['refs'])}")
        if entry["carried-from"]:
            fields.append(f"carried-from: {entry['carried-from']}")
        fields.append(entry["record"])
        lines.append("  " + " | ".join(fields))
    return "\n".join(lines) + ("\n" if lines else "")


# --- Earlier decisions -----------------------------------------------------------------------

EARLIER_WORKFLOWS = ("revise", "rewrite")
"""The run families whose decisions a new revise or rewrite run on the same note carries over."""


def _moment(text: str) -> datetime | None:
    """`decided-at` as a UTC-aware time; None when it is not an ISO 8601 time. A time without a zone is UTC."""
    try:
        moment = datetime.fromisoformat(text)
    except ValueError:
        return None
    return moment if moment.tzinfo is not None else moment.replace(tzinfo=UTC)


def _when(decision: dict) -> tuple[datetime, str]:
    return _moment(decision["decided-at"]), decision["answers-file"]


def _note_runs(root: Path, note: str, workflows: tuple[str, ...], current: Path | None) -> list[Path]:
    """The run directories on `note` in `workflows`, other than `current`, in name order per workflow."""
    current = current.resolve() if current is not None else None
    found = []
    for workflow in workflows:
        base = root / gates.RUNS / workflow / note.removesuffix(".md")
        if base.is_dir():
            found += [path for path in sorted(base.iterdir())
                      if path.is_dir() and _RUN.fullmatch(path.name) and path.resolve() != current]
    return found


def _decided(root: Path, data: dict) -> dict | None:
    """The answers a kept record holds, as the validator reads them at their origin; None when it refuses them."""
    try:
        parsed, problems = edits.answered(root, root / data["origin"], data["text"])
    except (OSError, ValueError):
        return None
    return None if problems else parsed


def earlier(root: Path, note: str, current: Path | None = None, *, findings_only: bool = False) -> list[dict]:
    """The operator's decided items on edit proposals and findings in the runs on `note` other than `current`.

    The runs are those of `EARLIER_WORKFLOWS`, revise and rewrite.

    `current` None reads every run. `findings_only` reads only answers whose
    question is a review result, so only decisions on findings are returned.

    Each run directory under the note's path in those run families may keep
    answers files (`kept_answers()`). For each kept file that the validator
    accepts, every item that `answers.decision_key()` identifies and whose
    state is not `pending` is an earlier decision: an edit proposal, with a
    `quote` and a `change`, or a finding of a review result. A kept file the
    validator refuses is skipped whole. An item whose `decided-at` is not an
    ISO 8601 time is skipped. When the same proposal (same quote and change)
    or the same finding (same criterion and identical finding) was decided
    more than once, the latest `decided-at` wins. Each decision holds
    `proposal`, `state`, `reason`, `revisit`, `decided-by`, `decided-at` and
    `answers-file`, the repository path of the answers file the operator
    named, and `resolution` when the item, or another answers file holding
    this same decision, records one; a decision on a finding also holds
    `criterion`, the criterion's identity, and `answered`, the hashes of the
    review results whose answers hold this same decision, the first one and
    those it was carried over to. The list is ordered by `decided-at`.
    """
    latest: dict[tuple, dict] = {}
    answered: dict[tuple, list[tuple[str, str, str]]] = {}
    resolved: dict[tuple, str] = {}
    for run_dir in _note_runs(root, note, EARLIER_WORKFLOWS, current):
        for _, data in kept_answers(root, run_dir):
            parsed = _decided(root, data)
            if parsed is None:
                continue
            criterion = answers.finding_criterion((root / parsed["question"]).read_bytes())
            if findings_only and criterion is None:
                continue
            for item in parsed["items"]:
                proposal = item["proposal"]
                same = answers.decision_key(proposal, criterion)
                if same is None or item["state"] == "pending" or _moment(item["decided-at"]) is None:
                    continue
                decision = {"proposal": proposal, "state": item["state"], "reason": item.get("reason"),
                            "revisit": item.get("revisit"), "decided-by": item["decided-by"],
                            "decided-at": item["decided-at"], "answers-file": data["origin"]}
                if item.get("resolution"):
                    decision["resolution"] = item["resolution"]
                    resolved.setdefault((same, item["state"], item["decided-at"]), item["resolution"])
                if criterion is not None:
                    decision["criterion"] = criterion
                    answered.setdefault(same, []).append(
                        (decision["state"], decision["decided-at"], parsed["question-sha256"]))
                if same not in latest or _when(decision) > _when(latest[same]):
                    latest[same] = decision
    for same, decision in latest.items():
        found = resolved.get((same, decision["state"], decision["decided-at"]))
        if found and not decision.get("resolution"):       # a carried-over copy holds no resolution
            decision["resolution"] = found
        if same in answered:
            decision["answered"] = sorted({question for state, at, question in answered[same]
                                           if (state, at) == (decision["state"], decision["decided-at"])})
    return sorted(latest.values(), key=_when)


def earlier_stops(root: Path, note: str, current: Path | None = None) -> list[dict]:
    """The operator's decided stops of the other revise runs on `note`, ordered by `decided-at`.

    A stop counts when a kept `STOP_ANSWERS` file is accepted by the
    validator and its item is not `pending` and has an ISO 8601
    `decided-at`. Each holds `stop`, the `stop` text of that run's plan, read
    from the answers file's question; `state`, `reason`, `revisit`,
    `resolution` when the item has one, `decided-at` and `answers-file`, the
    answers file's repository path. `earlier()` does not return these: a stop
    names no passage and no change, so nothing is carried over from it.
    """
    found = []
    for run_dir in _note_runs(root, note, ("revise",), current):
        for _, data in kept_answers(root, run_dir):
            if Path(data["origin"]).name != STOP_ANSWERS:
                continue
            parsed = _decided(root, data)
            if parsed is None:
                continue
            plan = yaml.safe_load((root / parsed["question"]).read_text(encoding="utf-8"))
            for item in parsed["items"]:
                if item["state"] == "pending" or _moment(item["decided-at"]) is None:
                    continue
                stop = {"stop": plan.get("stop") if isinstance(plan, dict) else None, "state": item["state"],
                        "reason": item.get("reason"), "revisit": item.get("revisit"),
                        "decided-at": item["decided-at"], "answers-file": data["origin"]}
                if item.get("resolution"):
                    stop["resolution"] = item["resolution"]
                found.append(stop)
    return sorted(found, key=_when)


def stops_text(found: list[dict]) -> str:
    """The earlier decided stops as the readable section an assessor receives, one subsection per stop."""
    lines = ["# Earlier stops", "",
             "Assessments of other texts of this note stopped with these proposals; the operator decided each.", ""]
    for index, stop in enumerate(found, 1):
        lines += [f"## {index}. {stop['state']}", "", "Stop:", "", *_quoted(stop["stop"]), ""]
        if stop["reason"]:
            lines.append(f"Operator's reason: {stop['reason']}")
        if stop.get("resolution"):
            lines.append(f"{RESOLUTION}: {stop['resolution']}")
        if stop["revisit"]:
            lines.append(f"Revisit when: {stop['revisit']}")
        lines += [f"Decided at: {stop['decided-at']}", f"Answers file: `{stop['answers-file']}`", ""]
    return "\n".join(lines)


def _quoted(text: object) -> list[str]:
    return [f"> {line}" for line in str(text).splitlines()]


def _finding_lines(proposal: dict) -> list[str]:
    """A finding as the reviewer wrote it: its scope, the passages it quotes, its reason and level."""
    lines = [f"Scope: {proposal.get('scope')}", ""]
    for quote in proposal.get("quotes") or []:
        lines += ["Passage:", "", *_quoted(quote), ""]
    return lines + [f"Reviewer's reason: {proposal.get('reason')}", f"Level: {proposal.get('level')}", ""]


def earlier_text(found: list[dict]) -> str:
    """The earlier decisions as the readable text a worker receives, one section per decided item."""
    lines = ["# Earlier decisions", "",
             "The operator decided these proposals in earlier runs on other texts of this note.", ""]
    for index, decision in enumerate(found, 1):
        proposal = decision["proposal"]
        if decision.get("criterion") is not None:
            lines += [f"## {index}. {decision['state']}: a finding against `{decision['criterion']}`", "",
                      *_finding_lines(proposal)]
        else:
            lines += [f"## {index}. {decision['state']}", "", "Passage:", "", *_quoted(proposal["quote"]), "",
                      "Change:", "", *_quoted(proposal["change"]), ""]
        if decision["reason"]:
            lines.append(f"Operator's reason: {decision['reason']}")
        if decision.get("resolution"):
            lines.append(f"{RESOLUTION}: {decision['resolution']}")
        if decision["revisit"]:
            lines.append(f"Revisit when: {decision['revisit']}")
        lines += [f"Decided at: {decision['decided-at']}", f"Answers file: `{decision['answers-file']}`", ""]
    return "\n".join(lines)


# --- Finding decisions as an input of later work ---------------------------------------------

REVIEW_RULE = (
    "The operator rejected these findings of earlier reviews of this note against this criterion. "
    "Do not raise the same finding again unless the note's text changed in a way that answers the "
    "operator's reason, or you have an argument that the operator's reason does not address. When you "
    "raise it again, state that argument or that change, and why the operator's reason no longer holds.")
"""The reviewer's rule for the finding decisions it receives. It is part of the input, so its hash covers it."""
RETAINED_QUESTION = (
    "A rejection whose resolution states a retained question closes the rejected diagnosis, not the question; "
    "you may still report on that question against the current text.")
"""The reviewer's rule for a rejection with a `resolution`. The input holds it only when a decision has a
resolution, so the input of every other pair, and the hash of its result, stays as it was."""
RESOLUTION = "Resolution (what was done after the decision)"


def review_input(found: list[dict]) -> str:
    """The operator's rejections of findings on one note and criterion, as the text a reviewer receives.

    It holds each finding, the operator's reason, the item's `resolution`
    when it has one, and the decision's date, and not the answers file, so a decision carried over unchanged into
    another answers file gives the same text.
    """
    resolved = any(decision.get("resolution") for decision in found)
    lines = ["# The operator's decisions on earlier findings", "", REVIEW_RULE, "",
             *([RETAINED_QUESTION, ""] if resolved else [])]
    for index, decision in enumerate(found, 1):
        lines += [f"## {index}. {decision['state']}", "", *_finding_lines(decision["proposal"]),
                  f"Operator's reason: {decision['reason']}",
                  *([f"{RESOLUTION}: {decision['resolution']}"] if decision.get("resolution") else []),
                  f"Decided at: {decision['decided-at']}", ""]
    return "\n".join(lines)


def review_inputs(root: Path, note: str) -> dict[str, str]:
    """The review input per criterion identity: the operator's rejected findings of `note` against it.

    A criterion without a rejected finding has no entry, so its review
    request and the freshness of its result stay as they were.
    """
    rejected: dict[str, list[dict]] = {}
    for decision in earlier(root, note, findings_only=True):
        if decision["state"] == "rejected":
            rejected.setdefault(decision["criterion"], []).append(decision)
    return {criterion: review_input(found) for criterion, found in rejected.items()}


def planning_decisions(found: list[dict]) -> list[dict]:
    """The decisions on findings an assessor receives: the rejected and the deferred ones."""
    return [decision for decision in found
            if decision.get("criterion") is not None and decision["state"] in ("rejected", "deferred")]


def rejected_in(found: list[dict], criterion: str, question_sha256: str) -> list[dict]:
    """The proposals the operator rejected in answers to exactly this review result (same criterion and hash)."""
    return [decision["proposal"] for decision in found
            if decision.get("criterion") == criterion and decision["state"] == "rejected"
            and question_sha256 in decision.get("answered", ())]
