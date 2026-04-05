#!/usr/bin/env python3
"""Select actionable findings from effective warn reviews in the DB."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from review_db import GateReviewRow, connect, ensure_db, load_effective_gate_review_map, resolve_db_path


SUMMARY_SECTION_RE = re.compile(
    r"^###\s*Summary\s*$\s*(?P<body>.*?)(?=^###\s|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
FINDINGS_SECTION_RE = re.compile(
    r"^###\s*Findings\s*$\s*(?P<body>.*?)(?=^###\s|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
ACTIONABLE_FINDING_RE = re.compile(
    r"^\s*-\s*warn\s*:\s*(?P<body>.+?)(?=^\s*-\s*(?:pass|info|warn|fail|error)\s*:|^###\s|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
RESULT_LINE_RE = re.compile(r"^##\s*Result:\s*(?P<decision>[a-z]+)\s*$", re.IGNORECASE | re.MULTILINE)


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

    body_after_result = RESULT_LINE_RE.sub("", review_text, count=1).strip()
    if body_after_result:
        return [body_after_result]
    return []


def scan_reviews(
    repo_root: Path,
    note_filter: set[str] | None = None,
) -> list[NoteWarns]:
    db_path = resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    by_note: dict[str, NoteWarns] = {}
    selected_by_gate: dict[tuple[str, str], GateReviewRow] = {}
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

    return sorted(by_note.values(), key=lambda nw: (-nw.count, nw.note_path))


def render_json(notes: list[NoteWarns]) -> str:
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
    return json.dumps(items, indent=2)


def print_grouped(notes: list[NoteWarns]) -> None:
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

    notes = scan_reviews(repo_root, note_filter)
    if not notes:
        print("[]" if args.json else "No warn findings found.")
        return

    if args.json:
        print(render_json(notes))
    else:
        print_grouped(notes)


if __name__ == "__main__":
    main()
