#!/usr/bin/env python3
"""Select actionable findings from effective warn reviews in the DB."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from commonplace.review.review_db import (
    GATES_ROOT,
    GateReviewRow,
    connect,
    ensure_db,
    load_effective_gate_review_map,
    resolve_db_path,
    strip_explicit_review_result_lines,
)
from commonplace.review.review_metadata import git_blob_sha


SECTION_END_LOOKAHEAD = (
    r"(?=^###\s|"
    r"^##\s*(?:Result|Verdict|Outcome)\b|"
    r"^##\s+(?:pass|warn|fail|error|unknown|info|ok)\s*$|"
    r"^Verdict:|"
    r"^(?:[-*]\s*)?Outcome:|"
    r"\Z)"
)

SUMMARY_SECTION_RE = re.compile(
    rf"^###\s*Summary\s*$\s*(?P<body>.*?){SECTION_END_LOOKAHEAD}",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
FINDINGS_SECTION_RE = re.compile(
    rf"^###\s*Findings\s*$\s*(?P<body>.*?){SECTION_END_LOOKAHEAD}",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
ACTIONABLE_FINDING_RE = re.compile(
    r"^\s*-\s*warn\s*:\s*(?P<body>.+?)(?=^\s*-\s*(?:pass|info|warn|fail|error)\s*:|^###\s|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
@dataclass
class WarnEntry:
    note_path: str
    gate_id: str
    review_id: int
    review_run_id: int | None
    review_text: str
    warn_text: str


@dataclass
class NoteWarns:
    note_path: str
    warns: list[WarnEntry] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.warns)


def _extract_section(text: str, pattern: re.Pattern[str]) -> str | None:
    match = pattern.search(text)
    if match is None:
        return None
    body = match.group("body").strip()
    return body or None


def extract_warns(review_text: str, *, decision: str) -> list[str]:
    findings = _extract_section(review_text, FINDINGS_SECTION_RE)
    if findings:
        actionable = [match.group("body").strip() for match in ACTIONABLE_FINDING_RE.finditer(findings)]
        if actionable:
            return actionable

    if decision != "warn":
        return []

    summary = _extract_section(review_text, SUMMARY_SECTION_RE)
    if summary:
        return [summary]

    if findings:
        return [findings]

    body_after_result = strip_explicit_review_result_lines(review_text).strip()
    if body_after_result:
        return [body_after_result]
    return []


def _current_gate_shas(repo_root: Path) -> dict[str, str]:
    """Compute current git blob SHA for each gate file on disk."""
    gates_dir = repo_root / GATES_ROOT
    shas: dict[str, str] = {}
    for gate_file in gates_dir.rglob("*.md"):
        gate_id = str(gate_file.relative_to(gates_dir).with_suffix("")).replace("\\", "/")
        shas[gate_id] = git_blob_sha(gate_file)
    return shas


def scan_reviews(
    repo_root: Path,
    note_filter: set[str] | None = None,
) -> list[NoteWarns]:
    db_path = resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    by_note: dict[str, NoteWarns] = {}
    selected_by_gate: dict[tuple[str, str], GateReviewRow] = {}
    gate_shas = _current_gate_shas(repo_root)
    stale_gates: set[str] = set()
    with connect(db_path) as conn:
        effective_reviews = load_effective_gate_review_map(
            conn,
            note_path=next(iter(note_filter)) if note_filter and len(note_filter) == 1 else None,
            model_id=None,
        )

    for (note_path, gate_id, _model_id), review in sorted(effective_reviews.items()):
        if note_filter and note_path not in note_filter:
            continue
        if review.review_run_id is None:
            continue
        # Skip reviews made against a stale gate definition.
        # TODO: The cleaner approach is to add a gate_shas parameter to
        # load_effective_gate_review_map so freshness filtering happens in the
        # shared query layer — the target selector does the same check in its
        # own loop. Deferred to avoid changing the shared function's contract.
        current_sha = gate_shas.get(gate_id)
        if current_sha is not None and review.gate_sha != current_sha:
            stale_gates.add(gate_id)
            continue
        warns = extract_warns(review.rationale_markdown, decision=review.decision)
        if not warns:
            continue

        gate_key = (note_path, gate_id)
        selected = selected_by_gate.get(gate_key)
        if selected is None or (review.reviewed_at, review.id) > (selected.reviewed_at, selected.id):
            selected_by_gate[gate_key] = review

    for (note_path, gate_id), review in sorted(selected_by_gate.items()):
        warns = extract_warns(review.rationale_markdown, decision=review.decision)
        for warn_text in warns:
            if note_path not in by_note:
                by_note[note_path] = NoteWarns(note_path=note_path)
            by_note[note_path].warns.append(
                WarnEntry(
                    note_path=note_path,
                    gate_id=gate_id,
                    review_id=review.id,
                    review_run_id=review.review_run_id,
                    review_text=review.rationale_markdown,
                    warn_text=warn_text,
                )
            )

    notes = sorted(by_note.values(), key=lambda nw: (-nw.count, nw.note_path))
    return notes, sorted(stale_gates)


def render_json(notes: list[NoteWarns], stale_gates: list[str]) -> str:
    items = []
    for nw in notes:
        items.append(
            {
                "note_path": nw.note_path,
                "warn_count": nw.count,
                "warns": [
                    {
                        "gate_id": w.gate_id,
                        "review_id": w.review_id,
                        "review_run_id": w.review_run_id,
                        "review_text": w.review_text,
                        "text": w.warn_text,
                    }
                    for w in nw.warns
                ],
            }
        )
    if stale_gates:
        items.append({"stale_gates": stale_gates})
    return json.dumps(items, indent=2)


def print_grouped(notes: list[NoteWarns], stale_gates: list[str]) -> None:
    if stale_gates:
        print(f"WARNING: {len(stale_gates)} gate(s) changed since last review — findings skipped:")
        for g in stale_gates:
            print(f"  - {g}")
        print()
    for nw in notes:
        print(f"{nw.note_path} ({nw.count} warn findings)")
        for w in nw.warns:
            first_line = w.warn_text.split("\n")[0][:100]
            print(f"  - {w.gate_id}: {first_line}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Select notes with actionable findings from effective warn reviews.")
    parser.add_argument("note_paths", nargs="*", help="Optional note path filter.")
    parser.add_argument("--json", action="store_true", help="JSON output with full WARN text.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    note_filter = set(args.note_paths) if args.note_paths else None

    notes, stale_gates = scan_reviews(repo_root, note_filter)
    if not notes and not stale_gates:
        print("[]" if args.json else "No warn findings found.")
        return

    if args.json:
        print(render_json(notes, stale_gates))
    else:
        print_grouped(notes, stale_gates)


if __name__ == "__main__":
    main()
