"""The operator-decision record: a read-only listing of decisions already on disk.

Nothing here writes state. Entries come from three places under
kb/reports/state/:

- operator records `operator/*.json` in the revise and full-pass run
  directories: one entry per entry of an answered strike list, one bundle
  entry per approved publication manifest, one `pending` entry per stop
  without an answer;
- full-pass packets: the disposition, which is the workflow's judgment, and
  the resolution once it is not `pending`;
- fix reports, written by an agent without a run: one entry per report,
  pointing at it, since their tables are free-form.

Each entry says who proposed and who decided, and whether the decision
covered one item or a bundle. A publication approval is approval of the
final text, never of each edit that produced it. No statistic is computed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.review_workflows import edit_operations, full_pass, gates, revise

WORKFLOWS = ("revise", "full-pass")
"""Run families whose run directories may hold operator records; dated sweep directories hold none."""
FIXES = Path("kb/reports/state/fixes")
PUBLICATION = "publication.json"
ITEM_WIDTH = 80
_RUN = re.compile(r"[0-9a-f]{12}")
_LIST = re.compile(r"([a-z0-9-]+)-list-[0-9a-f]+\.md")
_AUTHORITY = {"user": "operator", "version-guard": "version-guard"}


class MalformedRecord(ValueError):
    """A decision record that cannot be read; the message names its path."""


def _entry(note: str, workflow: str, run: str | None, record: str, cls: str, proposed_by: str,
           decided_by: str, decision: str, unit: str, *, item: str | None = None, reason: str | None = None,
           key: str | None = None, at: str | None = None) -> dict:
    return {"note": note, "workflow": workflow, "run": run, "record": record, "class": cls,
            "proposed-by": proposed_by, "decided-by": decided_by, "decision": decision, "unit": unit,
            "item": item, "reason": reason, "key": key, "at": at}


def _head(entry: str) -> str:
    line = entry.splitlines()[0].removeprefix("- ").strip()
    return line if len(line) <= ITEM_WIDTH else line[:ITEM_WIDTH - 1] + "…"


def _operator(root: Path, workflow: str, run_dir: Path) -> list[dict]:
    run = run_dir.relative_to(root).as_posix()
    note = run_dir.parent.relative_to(root / gates.RUNS / workflow).as_posix() + ".md"
    found = []
    for path in sorted((run_dir / "operator").glob("*.json")):
        record = path.relative_to(root).as_posix()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            name, proposal, key = data["name"], data["proposal"], data["key"]
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise MalformedRecord(f"malformed operator record: {record}: {error!r}") from error
        answer, at = data.get("answer"), data.get("answered-at")
        common = {"key": key, "at": at if answer is not None else None}
        listed = _LIST.fullmatch(name)
        if listed:
            cls = listed.group(1)
            if answer is None:
                found.append(_entry(note, workflow, run, record, cls, "worker", "pending", "pending", "bundle",
                                    **common))
                continue
            kept, struck, _ = revise.strikes(proposal, answer)
            reasons = {entry["entry"]: entry["reason"] for entry in struck}
            for entry in ("\n".join(lines) for lines in edit_operations.items(proposal)):
                if entry in kept:
                    decision, reason = "approve", None
                elif entry in reasons:
                    decision, reason = "strike", reasons[entry]
                else:                       # deleted or edited: the current workflow blocks on such an answer
                    decision, reason = "deleted", None
                found.append(_entry(note, workflow, run, record, cls, "worker", "operator", decision, "item",
                                    item=_head(entry), reason=reason, **common))
        elif name == PUBLICATION:
            found.append(_entry(note, workflow, run, record, "publication", "workflow",
                                "pending" if answer is None else "operator",
                                "pending" if answer is None else "approve-publication", "bundle", **common))
        else:                               # a stop of an earlier workflow version, such as plan.yaml
            found.append(_entry(note, workflow, run, record, name, "workflow",
                                "pending" if answer is None else "operator",
                                "pending" if answer is None else "approve", "bundle", **common))
    return found


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


def _notes(root: Path) -> dict[str, list[str]]:
    """Note paths under kb/ by file stem, for fix reports that name their note only by stem."""
    found: dict[str, list[str]] = {}
    for path in (root / "kb").rglob("*.md"):
        relative = path.relative_to(root)
        if relative.parts[1] not in ("reports", "work") and not any(p.startswith(".") for p in relative.parts):
            found.setdefault(path.stem, []).append(relative.as_posix())
    return found


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
    packets = root / full_pass.PACKETS
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
        if entry["item"]:
            fields.append(f"item: {entry['item']}")
        if entry["reason"]:
            fields.append(f"reason: {entry['reason']}")
        fields.append(entry["record"])
        lines.append("  " + " | ".join(fields))
    return "\n".join(lines) + ("\n" if lines else "")
