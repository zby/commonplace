"""The operator-decision record: a read-only listing of decisions already on disk.

Nothing here writes state. Entries come from three places under
kb/reports/state/:

- operator records `operator/*.json` in the revise run directories: for an
  answers stop (`types/answers.md`), one entry per item of the approved
  answers file with its state, decider and reason, the publication approval
  as a bundle entry, marked `revised` when its question is the run's
  revised candidate `revised.md` (`revise.supply_revised()`) and not the
  workflow's candidate; one `pending` entry per stop without an answer. In a
  revise run, a pending entry is `overtaken` instead when the note no longer
  holds the text the run started from: the note is gone, or `edits.run_dir()`
  of its current text is another run directory. Such a run can never
  continue. This is computed when listing; nothing is written;
- records of the two retired procedures (ADR 135), kept so that recorded
  operator decisions stay visible: operator records in full-pass run
  directories; full-pass packets, with the disposition, which was the
  workflow's judgment, and the resolution once it is not `pending`; and fix
  reports, written by an agent without a run, one entry per report pointing
  at it, since their tables are free-form.

Each entry says who proposed and who decided, and whether the decision
covered one item or a bundle. A publication approval is approval of the
final text, never of each edit that produced it. No statistic is computed.

`earlier()` reads the same operator records for the revise workflow: the
operator's decided items on edit proposals and on review findings in the
other runs on one note, which a new run carries over (`types/answers.md`,
"Decisions carried over"). A decision on a finding comes from a triage stop,
`finding-answers-<key>.md`, whose question is a review result; the listing
shows it with class `finding` and names its criterion. `review_inputs()`
renders the rejected findings per criterion as the input a later review of
the note against that criterion receives; the input takes part in that
result's freshness (`results.criterion_sha256()`).
"""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path

from commonplace.lib import answers, frontmatter
from commonplace.lib.review_workflows import edits, gates, results

# BACKCOMPAT: reads packets and fix reports written before the cutover - remove after the operator says the old records are dispensable
WORKFLOWS = ("revise", "full-pass")
"""Run families whose run directories may hold operator records; dated sweep directories hold none.

`full-pass` is the run family of the retired full-pass workflow (ADR 135)."""
PACKETS = gates.STATE / "packets"
"""Where the retired full-pass workflow kept one current packet per note."""
FIXES = Path("kb/reports/state/fixes")
"""Where the retired fix procedure wrote its fix reports."""

ITEM_WIDTH = 80
_RUN = re.compile(r"[0-9a-f]{12}")
_ANSWERS = re.compile(r"([a-z0-9-]+?)-answers(?:-[0-9a-f]+)?\.md")
"""An answers stop: `<pass>-answers-<key>.md` of a per-item pass, `finding-answers-<key>.md` of a triage,
`publication-answers.md` or `stop-answers.md`."""
FINDING = "finding"
"""The class of a triage stop: its question is a review result, and its items are the result's findings."""
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


def _records(root: Path, run_dir: Path) -> list[tuple[str, dict]]:
    """The operator records of one run directory, each with its repository path; MalformedRecord when one breaks."""
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


def _criterion(root: Path, question: object) -> str | None:
    """The criterion id of the review result an answers file names as `question`; None when it cannot be read."""
    try:
        identity = answers.finding_criterion((root / str(question)).read_bytes())
        return None if identity is None else results.criterion_id(root, identity)
    except (OSError, ValueError):
        return None


def _revised(root: Path, run_dir: Path, proposal: str) -> bool:
    """Whether a publication stop's question is the run's revised candidate, not the workflow's candidate."""
    parsed = frontmatter.parse(proposal)
    question = parsed.data.get("question") if parsed.ok else None
    return question == (run_dir / "artifact" / edits.REVISED).relative_to(root).as_posix()


def _overtaken(root: Path, workflow: str, note: str, run_dir: Path) -> bool:
    """Whether a revise run can no longer continue: its note is gone or now holds another text.

    A revise run's directory is `edits.run_dir()` of the note's text when it
    started, so another current text names another directory.
    """
    if workflow != "revise":
        return False
    return not (root / note).is_file() or edits.run_dir(root, workflow, note) != run_dir


def _operator(root: Path, workflow: str, run_dir: Path) -> list[dict]:
    run = run_dir.relative_to(root).as_posix()
    note = run_dir.parent.relative_to(root / gates.RUNS / workflow).as_posix() + ".md"
    waiting = "overtaken" if _overtaken(root, workflow, note, run_dir) else "pending"
    found = []
    for record, data in _records(root, run_dir):
        name, key = data["name"], data["key"]
        answer, at = data.get("answer"), data.get("answered-at")
        common = {"key": key, "at": at if answer is not None else None}
        stop = _ANSWERS.fullmatch(name)
        if stop:
            cls = stop.group(1)
            proposer = "workflow" if cls == "publication" else "worker"   # a plan's `stop` is the assessor's
            revised = cls == "publication" and _revised(root, run_dir, data["proposal"])
            if answer is None:
                found.append(_entry(note, workflow, run, record, cls, proposer, waiting, waiting, "bundle",
                                    revised=revised, **common))
                continue
            parsed = frontmatter.parse(answer)
            items = parsed.data.get("items") if parsed.ok else None
            if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
                # The workflow refuses such an answer and waits; the record still shows it was given.
                found.append(_entry(note, workflow, run, record, cls, proposer, "operator", "invalid", "bundle",
                                    revised=revised, **common))
                continue
            criterion = _criterion(root, parsed.data.get("question")) if cls == FINDING else None
            for item in items:
                state = str(item.get("state"))
                found.append(_entry(note, workflow, run, record, cls, proposer,
                                    waiting if state == "pending" else str(item.get("decided-by")),
                                waiting if state == "pending" else state,
                                    "bundle" if cls == "publication" else "item",
                                    item=_head(item.get("proposal"), criterion),
                                    reason=item.get("reason"), resolution=item.get("resolution"),
                                    refs=item.get("refs"), carried_from=item.get("carried-from"),
                                    revised=revised, key=key, at=None if state == "pending" else str(item.get("decided-at") or at)))
        else:                               # a stop of an earlier workflow version, such as plan.yaml
            found.append(_entry(note, workflow, run, record, name, "workflow",
                                waiting if answer is None else "operator",
                                waiting if answer is None else "approve", "bundle", **common))
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
        if relative.parts[1] not in ("reports", "work") and not any(p.startswith(".") for p in relative.parts):
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


def entries(root: Path) -> list[dict]:
    """Every decision entry, grouped by note and ordered by time where known (untimed last)."""
    found: list[dict] = []
    for workflow in WORKFLOWS:
        base = root / gates.RUNS / workflow
        if base.is_dir():
            for records in sorted(base.rglob("operator")):
                if records.is_dir() and _RUN.fullmatch(records.parent.name):
                    found.extend(_operator(root, workflow, records.parent))
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

EARLIER_WORKFLOW = "revise"
"""The run family whose decisions a new run on the same note carries over."""


def _moment(text: str) -> datetime | None:
    """`decided-at` as a UTC-aware time; None when it is not an ISO 8601 time. A time without a zone is UTC."""
    try:
        moment = datetime.fromisoformat(text)
    except ValueError:
        return None
    return moment if moment.tzinfo is not None else moment.replace(tzinfo=UTC)


def _when(decision: dict) -> tuple[datetime, str]:
    return _moment(decision["decided-at"]), decision["answers-file"]


def earlier(root: Path, note: str, current: Path | None = None, *, findings_only: bool = False) -> list[dict]:
    """The operator's decided items on edit proposals and findings in the revise runs on `note` other than `current`.

    `current` None reads every run. `findings_only` reads only the answers
    of triage stops, so only decisions on findings are returned.

    Each run directory beside `current`, under the note's path, holds
    operator records. For each answers stop with an approved capture that
    the validator accepts, every item that `answers.decision_key()`
    identifies and whose state is not `pending` is an earlier decision: an
    edit proposal, with a `quote` and a `change`, or a finding of a review
    result, the question of a triage stop. A capture the validator refuses
    is skipped whole: the run that captured it refused it too. An item whose
    `decided-at` is not an ISO 8601 time is skipped. When the same proposal
    (same quote and change) or the same finding (same criterion and
    identical finding) was decided more than once, the latest `decided-at`
    wins. Each decision holds `proposal`, `state`, `reason`, `revisit`,
    `decided-by`, `decided-at` and `answers-file`, the repository path of
    its answers file; a decision on a finding also holds `criterion`, the
    criterion's identity, and `answered`, the hashes of the review results
    whose answers hold this same decision, the first one and those it was
    carried over to. The list is ordered by `decided-at`.
    """
    base = root / gates.RUNS / EARLIER_WORKFLOW / note.removesuffix(".md")
    if not base.is_dir():
        return []
    current = current.resolve() if current is not None else None
    latest: dict[tuple, dict] = {}
    answered: dict[tuple, list[tuple[str, str, str]]] = {}
    for run_dir in sorted(base.iterdir()):
        if not _RUN.fullmatch(run_dir.name) or not run_dir.is_dir() or run_dir.resolve() == current:
            continue
        for _, data in _records(root, run_dir):
            answer = data.get("answer")
            stop = _ANSWERS.fullmatch(data["name"])
            if answer is None or not stop or (findings_only and stop.group(1) != FINDING):
                continue
            path = run_dir / "artifact" / data["name"]
            parsed, problems = edits.answered(root, path, answer)
            if problems:
                continue
            criterion = answers.finding_criterion((root / parsed["question"]).read_bytes())
            for item in parsed["items"]:
                proposal = item["proposal"]
                same = answers.decision_key(proposal, criterion)
                if same is None or item["state"] == "pending" or _moment(item["decided-at"]) is None:
                    continue
                decision = {"proposal": proposal, "state": item["state"], "reason": item.get("reason"),
                            "revisit": item.get("revisit"), "decided-by": item["decided-by"],
                            "decided-at": item["decided-at"], "answers-file": path.relative_to(root).as_posix()}
                if criterion is not None:
                    decision["criterion"] = criterion
                    answered.setdefault(same, []).append(
                        (decision["state"], decision["decided-at"], parsed["question-sha256"]))
                if same not in latest or _when(decision) > _when(latest[same]):
                    latest[same] = decision
    for same, decision in latest.items():
        if same in answered:
            decision["answered"] = sorted({question for state, at, question in answered[same]
                                           if (state, at) == (decision["state"], decision["decided-at"])})
    return sorted(latest.values(), key=_when)


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


def review_input(found: list[dict]) -> str:
    """The operator's rejections of findings on one note and criterion, as the text a reviewer receives.

    It holds each finding, the operator's reason and the decision's date,
    and not the answers file, so a decision carried over unchanged into
    another answers file gives the same text.
    """
    lines = ["# The operator's decisions on earlier findings", "", REVIEW_RULE, ""]
    for index, decision in enumerate(found, 1):
        lines += [f"## {index}. {decision['state']}", "", *_finding_lines(decision["proposal"]),
                  f"Operator's reason: {decision['reason']}", f"Decided at: {decision['decided-at']}", ""]
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
