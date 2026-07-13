"""Library functions for warn_selector.

Pure logic lives here; warn_selector.py is the thin CLI wrapper.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from commonplace.lib.hashing import file_content_sha256
from commonplace.review.protocol.outcomes import strip_explicit_review_result_lines
from commonplace.review.review_db import (
    ReviewPairRow,
    connect,
    load_current_freshness_baselines,
    load_effective_review_pair_map,
    prepare_review_db,
)


SECTION_END_LOOKAHEAD = (
    r"(?=^###\s|"
    r"^##\s*Result\b|"
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
    criterion_path: str
    review_pair_id: int
    review_job_id: int
    result_path: str | None
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


def extract_warns(review_text: str, *, outcome: str) -> list[str]:
    findings = _extract_section(review_text, FINDINGS_SECTION_RE)
    if findings:
        actionable = [match.group("body").strip() for match in ACTIONABLE_FINDING_RE.finditer(findings)]
        if actionable:
            return actionable

    if outcome != "warn":
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


def _current_gate_content_hash(criterion_path: Path) -> str | None:
    if not criterion_path.is_file():
        return None
    return file_content_sha256(criterion_path)


def _load_review_text(repo_root: Path, review: ReviewPairRow) -> str | None:
    if review.result_path is None:
        return None
    try:
        return (repo_root / review.result_path).read_text(encoding="utf-8")
    except OSError:
        return None


def scan_reviews(
    repo_root: Path,
    note_filter: set[str] | None = None,
    *,
    db_path: Path | None = None,
) -> tuple[list[NoteWarns], list[str]]:
    if db_path is None:
        db_path = prepare_review_db(repo_root)

    by_note: dict[str, NoteWarns] = {}
    selected_by_gate: dict[tuple[str, str], tuple[ReviewPairRow, str, list[str]]] = {}
    stale_gates: set[str] = set()
    with connect(db_path) as conn:
        effective_reviews = load_effective_review_pair_map(
            conn,
            note_path=next(iter(note_filter)) if note_filter and len(note_filter) == 1 else None,
            model_partition=None,
        )
        freshness_baselines = load_current_freshness_baselines(conn)

    for (note_path, criterion_path, model_partition), review in sorted(effective_reviews.items()):
        if note_filter and note_path not in note_filter:
            continue
        freshness_baseline = freshness_baselines.get((note_path, criterion_path, model_partition))
        if freshness_baseline is None:
            stale_gates.add(criterion_path)
            continue
        current_criterion_hash = _current_gate_content_hash(repo_root / criterion_path)
        if current_criterion_hash is None or current_criterion_hash != freshness_baseline.baseline_criterion_hash:
            stale_gates.add(criterion_path)
            continue
        if review.outcome is None:
            continue
        review_text = _load_review_text(repo_root, review)
        if review_text is None:
            continue
        warns = extract_warns(review_text, outcome=review.outcome)
        if not warns:
            continue

        gate_key = (note_path, criterion_path)
        selected_tuple = selected_by_gate.get(gate_key)
        selected = selected_tuple[0] if selected_tuple is not None else None
        if selected is None or (review.completed_at or "", review.review_pair_id) > (
            selected.completed_at or "",
            selected.review_pair_id,
        ):
            selected_by_gate[gate_key] = (review, review_text, warns)

    for (note_path, criterion_path), (review, review_text, warns) in sorted(selected_by_gate.items()):
        for warn_text in warns:
            if note_path not in by_note:
                by_note[note_path] = NoteWarns(note_path=note_path)
            by_note[note_path].warns.append(
                WarnEntry(
                    note_path=note_path,
                    criterion_path=criterion_path,
                    review_pair_id=review.review_pair_id,
                    review_job_id=review.review_job_id,
                    result_path=review.result_path,
                    review_text=review_text,
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
                        "criterion_path": w.criterion_path,
                        "review_pair_id": w.review_pair_id,
                        "review_job_id": w.review_job_id,
                        "result_path": w.result_path,
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


def render_grouped(notes: list[NoteWarns], stale_gates: list[str]) -> str:
    lines: list[str] = []
    if stale_gates:
        lines.append(f"WARNING: {len(stale_gates)} gate(s) changed since last review — findings skipped:")
        for g in stale_gates:
            lines.append(f"  - {g}")
        lines.append("")
    for nw in notes:
        lines.append(f"{nw.note_path} ({nw.count} warn findings)")
        for w in nw.warns:
            first_line = w.warn_text.split("\n")[0][:100]
            lines.append(f"  - {w.criterion_path}: {first_line}")
    return "\n".join(lines)
