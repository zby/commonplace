#!/usr/bin/env python3
"""Summarize review files into a small markdown report and ranked CSV tables.

Without arguments, reads ALL review files (*.prose-review.md,
*.semantic-review.md, etc.) and writes kb/reports/SUMMARY.md.

With a review-type argument, reads only that type and writes
kb/reports/SUMMARY.{review-type}.md.

In both modes, writes normalized CSV tables to kb/reports/reviews/csv/. It also writes a
parallel set of `current.*` tables limited to notes with `status: current`.
The CSVs are ordered so an orchestrator can prioritize by reading only the
first few rows.

Usage: uv run scripts/summarize_reviews.py [review-type]

Examples: uv run scripts/summarize_reviews.py           # all review types
          uv run scripts/summarize_reviews.py prose-review
          uv run scripts/summarize_reviews.py semantic-review
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

SUMMARY_PREFIX = "SUMMARY"
TOP_ROWS = 5
LEVEL_PRIORITY = {"WARN": 0, "INFO": 1, "CLEAN": 2}


@dataclass
class Finding:
    note: str
    check: str
    text: str
    review_type: str
    level: str  # WARN, INFO, CLEAN


@dataclass
class NoteReview:
    note: str
    review_type: str
    note_status: str | None = None
    findings: list[Finding] = field(default_factory=list)


@dataclass
class ReviewTables:
    findings_headers: list[str]
    findings_rows: list[list[str]]
    notes_summary_headers: list[str]
    notes_summary_rows: list[list[str]]
    checks_summary_headers: list[str]
    checks_summary_rows: list[list[str]]
    checks_low_signal_headers: list[str]
    checks_low_signal_rows: list[list[str]]
    notes_by_warnings_headers: list[str]
    notes_by_warnings_rows: list[list[str]]


@dataclass
class SummaryStats:
    reviewed_notes: int
    total_warn: int
    total_info: int
    clean_notes: int


def detect_review_type(path: Path) -> str | None:
    """Extract the review type from a filename like foo.prose-review.md."""
    stem = path.stem
    parts = stem.rsplit(".", 1)
    if len(parts) == 2:
        return parts[1]
    return None


def parse_review(path: Path) -> NoteReview | None:
    """Parse a single review file into structured findings."""
    content = path.read_text(encoding="utf-8")
    review_type = detect_review_type(path) or "unknown"

    header_match = re.search(r"===\s+\w[\w\s]+:\s+(\S+\.md)\s+===", content)
    if not header_match:
        return None
    note = header_match.group(1)

    review = NoteReview(note=note, review_type=review_type)
    current_section = None

    for line in content.splitlines():
        stripped = line.strip()
        if stripped in ("WARN:", "INFO:", "CLEAN:", "PASS:"):
            current_section = stripped.rstrip(":")
            if current_section == "PASS":
                current_section = "CLEAN"
            continue

        if not stripped.startswith("- ["):
            continue

        match = re.match(r"- \[([^\]]+)\]\s*(.*)", stripped)
        if not match:
            continue

        check = match.group(1)
        text = match.group(2)

        if current_section in ("WARN", "INFO", "CLEAN"):
            review.findings.append(
                Finding(
                    note=note,
                    check=check,
                    text=text,
                    review_type=review_type,
                    level=current_section,
                )
            )

    return review


def review_targets_existing_note(review: NoteReview, notes_dir: Path) -> bool:
    """Return whether the reviewed note still exists in kb/notes/."""
    return (notes_dir / review.note).exists()


def parse_note_status(path: Path) -> str | None:
    """Return a note's frontmatter status, if present."""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return None

    frontmatter_match = re.match(r"^---\n(.*?)\n---\n?", content, re.DOTALL)
    if not frontmatter_match:
        return None

    status_match = re.search(
        r"(?m)^status:\s*(.*?)\s*$",
        frontmatter_match.group(1),
    )
    if not status_match:
        return None

    return status_match.group(1).strip().strip("'\"") or None


def truncate(text: str, max_len: int = 140) -> str:
    """Truncate text with ellipsis."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def write_csv(path: Path, headers: list[str], rows: list[list[str]]) -> None:
    """Write a CSV file with headers and rows."""
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def build_tables(reviews: list[NoteReview]) -> ReviewTables:
    """Build ranked CSV-ready tables from parsed reviews."""
    note_counts: dict[str, Counter[str]] = defaultdict(Counter)
    check_counts: dict[str, Counter[str]] = defaultdict(Counter)
    note_warn_checks: dict[str, Counter[str]] = defaultdict(Counter)
    first_warn_by_note: dict[str, Finding] = {}
    first_warn_by_check: dict[str, Finding] = {}
    all_findings: list[Finding] = []

    for review in reviews:
        for finding in review.findings:
            all_findings.append(finding)
            note_counts[finding.note][finding.level] += 1
            check_counts[finding.check][finding.level] += 1
            if finding.level == "WARN":
                note_warn_checks[finding.note][finding.check] += 1
                first_warn_by_note.setdefault(finding.note, finding)
                first_warn_by_check.setdefault(finding.check, finding)

    findings_headers = [
        "note",
        "review_type",
        "level",
        "note_warn_count",
        "check_warn_count",
        "check",
        "finding",
    ]
    findings_rows = sorted(
        [
            [
                finding.note,
                finding.review_type,
                finding.level,
                str(note_counts[finding.note].get("WARN", 0)),
                str(check_counts[finding.check].get("WARN", 0)),
                finding.check,
                finding.text,
            ]
            for finding in all_findings
        ],
        key=lambda row: (
            LEVEL_PRIORITY[row[2]],
            -int(row[3]),
            -int(row[4]),
            row[0],
            row[5],
        ),
    )

    notes_summary_headers = ["note", "warn_count", "info_count", "clean_count"]
    notes_summary_rows = sorted(
        [
            [
                note,
                str(counts.get("WARN", 0)),
                str(counts.get("INFO", 0)),
                str(counts.get("CLEAN", 0)),
            ]
            for note, counts in note_counts.items()
        ],
        key=lambda row: (-int(row[1]), -int(row[2]), row[0]),
    )

    checks_summary_headers = [
        "check",
        "warn_count",
        "info_count",
        "clean_count",
        "sample_note",
        "sample_finding",
    ]
    checks_summary_rows = sorted(
        [
            [
                check,
                str(counts.get("WARN", 0)),
                str(counts.get("INFO", 0)),
                str(counts.get("CLEAN", 0)),
                first_warn_by_check[check].note if check in first_warn_by_check else "",
                first_warn_by_check[check].text if check in first_warn_by_check else "",
            ]
            for check, counts in check_counts.items()
        ],
        key=lambda row: (-int(row[1]), -int(row[2]), row[0]),
    )

    checks_low_signal_headers = [
        "check",
        "warn_count",
        "info_count",
        "clean_count",
        "sample_note",
        "sample_finding",
    ]
    checks_low_signal_rows = sorted(
        [
            [
                check,
                str(counts.get("WARN", 0)),
                str(counts.get("INFO", 0)),
                str(counts.get("CLEAN", 0)),
                first_warn_by_check[check].note if check in first_warn_by_check else "",
                first_warn_by_check[check].text if check in first_warn_by_check else "",
            ]
            for check, counts in check_counts.items()
        ],
        key=lambda row: (int(row[1]), int(row[2]), -int(row[3]), row[0]),
    )

    notes_by_warnings_headers = [
        "note",
        "warn_count",
        "info_count",
        "top_warning_checks",
        "sample_warning",
    ]
    notes_by_warnings_rows = sorted(
        [
            [
                note,
                str(counts.get("WARN", 0)),
                str(counts.get("INFO", 0)),
                ", ".join(
                    check for check, _ in note_warn_checks[note].most_common(3)
                ),
                first_warn_by_note[note].text if note in first_warn_by_note else "",
            ]
            for note, counts in note_counts.items()
        ],
        key=lambda row: (-int(row[1]), -int(row[2]), row[0]),
    )

    return ReviewTables(
        findings_headers=findings_headers,
        findings_rows=findings_rows,
        notes_summary_headers=notes_summary_headers,
        notes_summary_rows=notes_summary_rows,
        checks_summary_headers=checks_summary_headers,
        checks_summary_rows=checks_summary_rows,
        checks_low_signal_headers=checks_low_signal_headers,
        checks_low_signal_rows=checks_low_signal_rows,
        notes_by_warnings_headers=notes_by_warnings_headers,
        notes_by_warnings_rows=notes_by_warnings_rows,
    )


def build_summary_stats(
    reviews: list[NoteReview],
    tables: ReviewTables,
) -> SummaryStats:
    """Compute compact summary counts for a review slice."""
    return SummaryStats(
        reviewed_notes=len(reviews),
        total_warn=sum(int(row[1]) for row in tables.notes_summary_rows),
        total_info=sum(int(row[2]) for row in tables.notes_summary_rows),
        clean_notes=sum(
            1
            for row in tables.notes_summary_rows
            if int(row[1]) == 0 and int(row[2]) == 0
        ),
    )


def csv_prefix(review_type: str | None, scope: str | None = None) -> str:
    """Build the filename prefix used for generated CSV tables."""
    parts = [part for part in (review_type, scope) if part]
    return ".".join(parts) + ("." if parts else "")


def export_csvs(
    tables: ReviewTables,
    csv_dir: Path,
    review_type: str | None,
    scope: str | None = None,
) -> None:
    """Write ranked CSV tables to csv_dir."""
    csv_dir.mkdir(parents=True, exist_ok=True)
    prefix = csv_prefix(review_type, scope)

    write_csv(
        csv_dir / f"{prefix}findings.csv",
        tables.findings_headers,
        tables.findings_rows,
    )
    write_csv(
        csv_dir / f"{prefix}notes_summary.csv",
        tables.notes_summary_headers,
        tables.notes_summary_rows,
    )
    write_csv(
        csv_dir / f"{prefix}checks_summary.csv",
        tables.checks_summary_headers,
        tables.checks_summary_rows,
    )
    write_csv(
        csv_dir / f"{prefix}checks_low_signal.csv",
        tables.checks_low_signal_headers,
        tables.checks_low_signal_rows,
    )
    write_csv(
        csv_dir / f"{prefix}notes_by_warnings.csv",
        tables.notes_by_warnings_headers,
        tables.notes_by_warnings_rows,
    )


def build_markdown(
    reviews: list[NoteReview],
    review_type: str | None,
    title: str,
    tables: ReviewTables,
    current_reviews: list[NoteReview],
    current_tables: ReviewTables,
) -> str:
    """Build a compact summary from the first few rows of ranked tables."""
    stats = build_summary_stats(reviews, tables)
    current_stats = build_summary_stats(current_reviews, current_tables)
    prefix = csv_prefix(review_type)
    current_prefix = csv_prefix(review_type, "current")
    lines: list[str] = []
    lines.append(f"# {title} — {date.today()}")
    lines.append("")
    lines.append(f"Reviewed: {stats.reviewed_notes} notes")
    lines.append(f"WARN: {stats.total_warn}")
    lines.append(f"INFO: {stats.total_info}")
    lines.append(f"Clean notes: {stats.clean_notes}")
    lines.append("")
    lines.append(f"Current notes reviewed: {current_stats.reviewed_notes}")
    lines.append(f"Current WARN: {current_stats.total_warn}")
    lines.append(f"Current INFO: {current_stats.total_info}")
    lines.append(f"Current clean notes: {current_stats.clean_notes}")
    lines.append("")
    lines.append("This summary is built from the top rows of the ranked CSV tables.")
    lines.append("For the full dataset, read `kb/reports/reviews/csv/`.")
    lines.append("")

    current_priority_rows = [
        row for row in current_tables.notes_by_warnings_rows if int(row[1]) > 0
    ][:TOP_ROWS]
    lines.append("## Priority Current Notes")
    lines.append("")
    if current_priority_rows:
        lines.append("| Note | WARN | INFO | Top checks | Sample warning |")
        lines.append("|------|------|------|------------|----------------|")
        for row in current_priority_rows:
            note_stem = row[0].removesuffix(".md")
            lines.append(
                f"| [{note_stem}](../notes/{row[0]}) "
                f"| {row[1]} "
                f"| {row[2]} "
                f"| {truncate(row[3], 40)} "
                f"| {truncate(row[4])} |"
            )
    else:
        lines.append("No current notes with warnings.")
    lines.append("")

    priority_rows = [
        row for row in tables.notes_by_warnings_rows if int(row[1]) > 0
    ][:TOP_ROWS]
    lines.append("## Priority Notes")
    lines.append("")
    if priority_rows:
        lines.append("| Note | WARN | INFO | Top checks | Sample warning |")
        lines.append("|------|------|------|------------|----------------|")
        for row in priority_rows:
            note_stem = row[0].removesuffix(".md")
            lines.append(
                f"| [{note_stem}](../notes/{row[0]}) "
                f"| {row[1]} "
                f"| {row[2]} "
                f"| {truncate(row[3], 40)} "
                f"| {truncate(row[4])} |"
            )
    else:
        lines.append("No notes with warnings.")
    lines.append("")

    hot_checks = [
        row for row in tables.checks_summary_rows if int(row[1]) > 0
    ][:TOP_ROWS]
    lines.append("## Hot Checks")
    lines.append("")
    if hot_checks:
        lines.append("| Check | WARN | INFO | Sample note | Sample finding |")
        lines.append("|-------|------|------|-------------|----------------|")
        for row in hot_checks:
            note_stem = row[4].removesuffix(".md") if row[4] else ""
            note_link = (
                f"[{note_stem}](../notes/{row[4]})" if row[4] else ""
            )
            lines.append(
                f"| {row[0]} "
                f"| {row[1]} "
                f"| {row[2]} "
                f"| {note_link} "
                f"| {truncate(row[5])} |"
            )
    else:
        lines.append("No warning-producing checks.")
    lines.append("")

    low_signal_checks = tables.checks_low_signal_rows[:TOP_ROWS]
    lines.append("## Low-Yield Checks")
    lines.append("")
    if low_signal_checks:
        lines.append("| Check | WARN | INFO | CLEAN | Sample note | Sample finding |")
        lines.append("|-------|------|------|-------|-------------|----------------|")
        for row in low_signal_checks:
            note_stem = row[4].removesuffix(".md") if row[4] else ""
            note_link = (
                f"[{note_stem}](../notes/{row[4]})" if row[4] else ""
            )
            sample_finding = row[5] if row[5] else "No warning sample"
            lines.append(
                f"| {row[0]} "
                f"| {row[1]} "
                f"| {row[2]} "
                f"| {row[3]} "
                f"| {note_link} "
                f"| {truncate(sample_finding)} |"
            )
    else:
        lines.append("No checks found.")
    lines.append("")

    lines.append("## Ranked CSV Tables")
    lines.append("")
    lines.append(
        f"- `kb/reports/reviews/csv/{prefix}notes_by_warnings.csv` — note-level queue, most urgent first"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{prefix}checks_summary.csv` — recurring failure modes, highest warning volume first"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{prefix}checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{prefix}notes_summary.csv` — full per-note totals, warning-heavy notes first"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{prefix}findings.csv` — raw finding rows for deeper drill-down, not used in this summary"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{current_prefix}notes_by_warnings.csv` — current-note priority queue for manual fixes"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{current_prefix}notes_summary.csv` — per-current-note totals, warning-heavy notes first"
    )
    lines.append(
        f"- `kb/reports/reviews/csv/{current_prefix}checks_summary.csv` — warning-producing checks within current notes"
    )
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    review_type = sys.argv[1] if len(sys.argv) > 1 else None
    reviews_dir = Path("kb/reports/reviews")
    reports_dir = reviews_dir.parent
    csv_dir = reviews_dir / "csv"
    notes_dir = Path("kb/notes")

    if review_type:
        suffix = f".{review_type}.md"
        files = sorted(reviews_dir.glob(f"*{suffix}"))
        title = review_type.replace("-", " ").title() + " Sweep"
        output_name = f"{SUMMARY_PREFIX}.{review_type}.md"
    else:
        files = sorted(
            path
            for path in reviews_dir.glob("*.*-review.md")
            if not path.name.startswith(SUMMARY_PREFIX)
        )
        title = "Review Sweep (All Types)"
        output_name = f"{SUMMARY_PREFIX}.md"

    if not files:
        label = suffix if review_type else "*.*-review.md"
        print(f"No {label} files found in {reviews_dir}/", file=sys.stderr)
        sys.exit(1)

    reviews: list[NoteReview] = []
    stale_reviews = 0
    for path in files:
        parsed = parse_review(path)
        if parsed and review_targets_existing_note(parsed, notes_dir):
            parsed.note_status = parse_note_status(notes_dir / parsed.note)
            reviews.append(parsed)
        elif parsed:
            stale_reviews += 1

    tables = build_tables(reviews)
    current_reviews = [
        review for review in reviews if review.note_status == "current"
    ]
    current_tables = build_tables(current_reviews)
    warn_count = sum(1 for row in tables.findings_rows if row[2] == "WARN")

    markdown = build_markdown(
        reviews,
        review_type,
        title,
        tables,
        current_reviews,
        current_tables,
    )
    output = reports_dir / output_name
    output.write_text(markdown, encoding="utf-8")
    print(f"Wrote {output} ({len(reviews)} notes, {warn_count} warnings)")
    if stale_reviews:
        print(f"Skipped {stale_reviews} stale review files")

    export_csvs(tables, csv_dir, review_type)
    export_csvs(current_tables, csv_dir, review_type, scope="current")
    prefix = csv_prefix(review_type)
    current_prefix = csv_prefix(review_type, "current")
    print(f"Wrote CSV tables to {csv_dir}/{prefix}*.csv")
    print(f"Wrote current-note CSV tables to {csv_dir}/{current_prefix}*.csv")


if __name__ == "__main__":
    main()
