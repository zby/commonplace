#!/usr/bin/env python3
"""Summarize review files into a SUMMARY report and CSV tables.

Without arguments, reads ALL review files (*.prose-review.md,
*.semantic-review.md, etc.) and writes reviews/SUMMARY.md.

With a review-type argument, reads only that type and writes
reviews/SUMMARY.{review-type}.md.

In both modes, writes normalized CSV tables to reviews/csv/.

Usage: uv run scripts/summarize_reviews.py [review-type]

Examples: uv run scripts/summarize_reviews.py           # all review types
          uv run scripts/summarize_reviews.py prose-review
          uv run scripts/summarize_reviews.py semantic-review
"""

import csv
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

SUMMARY_PREFIX = "SUMMARY"


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
    findings: list[Finding] = field(default_factory=list)


def detect_review_type(path: Path) -> str | None:
    """Extract the review type from a filename like foo.prose-review.md."""
    stem = path.stem  # e.g. "foo.prose-review"
    parts = stem.rsplit(".", 1)
    if len(parts) == 2:
        return parts[1]  # e.g. "prose-review"
    return None


def parse_review(path: Path) -> NoteReview | None:
    """Parse a single review file into structured findings."""
    content = path.read_text(encoding="utf-8")
    review_type = detect_review_type(path) or "unknown"

    # Extract note filename from header
    header_match = re.search(r"===\s+\w[\w\s]+:\s+(\S+\.md)\s+===", content)
    if not header_match:
        return None
    note = header_match.group(1)

    review = NoteReview(note=note, review_type=review_type)
    current_section = None

    for line in content.splitlines():
        stripped = line.strip()

        # Detect section transitions
        if stripped in ("WARN:", "INFO:", "CLEAN:", "PASS:"):
            current_section = stripped.rstrip(":")
            if current_section == "PASS":
                current_section = "CLEAN"
            continue

        # Skip non-finding lines
        if not stripped.startswith("- ["):
            continue

        # Extract check name and finding text
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


def truncate(text: str, max_len: int = 120) -> str:
    """Truncate text with ellipsis."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def write_csv(path: Path, headers: list[str], rows: list[list[str]]) -> None:
    """Write a CSV file with headers and rows."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def export_csvs(
    reviews: list[NoteReview], csv_dir: Path, review_type: str | None
) -> None:
    """Write normalized CSV tables to csv_dir."""
    csv_dir.mkdir(parents=True, exist_ok=True)

    # Prefix for filenames when filtering by type
    prefix = f"{review_type}." if review_type else ""

    # 1. findings.csv — one row per finding (the raw data)
    findings_rows = []
    for r in reviews:
        for f in r.findings:
            findings_rows.append(
                [f.note, f.review_type, f.level, f.check, f.text]
            )
    write_csv(
        csv_dir / f"{prefix}findings.csv",
        ["note", "review_type", "level", "check", "finding"],
        findings_rows,
    )

    # 2. notes_summary.csv — aggregated per note
    note_counts: dict[str, Counter[str]] = {}
    for r in reviews:
        for f in r.findings:
            key = f.note
            if key not in note_counts:
                note_counts[key] = Counter()
            note_counts[key][f.level] += 1
    write_csv(
        csv_dir / f"{prefix}notes_summary.csv",
        ["note", "warn_count", "info_count", "clean_count"],
        [
            [
                note,
                str(counts.get("WARN", 0)),
                str(counts.get("INFO", 0)),
                str(counts.get("CLEAN", 0)),
            ]
            for note, counts in sorted(note_counts.items())
        ],
    )

    # 3. checks_summary.csv — aggregated per check
    check_counts: dict[str, Counter[str]] = {}
    for r in reviews:
        for f in r.findings:
            if f.check not in check_counts:
                check_counts[f.check] = Counter()
            check_counts[f.check][f.level] += 1
    write_csv(
        csv_dir / f"{prefix}checks_summary.csv",
        ["check", "warn_count", "info_count", "clean_count"],
        [
            [
                check,
                str(counts.get("WARN", 0)),
                str(counts.get("INFO", 0)),
                str(counts.get("CLEAN", 0)),
            ]
            for check, counts in sorted(check_counts.items())
        ],
    )

    # 4. notes_by_warnings.csv — notes ranked by warning count (desc)
    notes_warn_count: Counter[str] = Counter()
    for r in reviews:
        for f in r.findings:
            if f.level == "WARN":
                notes_warn_count[f.note] += 1
    write_csv(
        csv_dir / f"{prefix}notes_by_warnings.csv",
        ["note", "warn_count"],
        [[note, str(count)] for note, count in notes_warn_count.most_common()],
    )

    # 5. checks_without_warnings.csv — checks with zero warnings
    all_checks = set(check_counts.keys())
    warn_checks = {
        c for c, counts in check_counts.items() if counts.get("WARN", 0) > 0
    }
    no_warn = sorted(all_checks - warn_checks)
    write_csv(
        csv_dir / f"{prefix}checks_without_warnings.csv",
        ["check"],
        [[c] for c in no_warn],
    )


def build_markdown(
    reviews: list[NoteReview], review_type: str | None, title: str
) -> str:
    """Build the markdown summary."""
    all_warns: list[Finding] = []
    warn_checks: Counter[str] = Counter()
    clean_notes: list[str] = []
    review_types_seen: set[str] = set()
    all_check_names: set[str] = set()
    warn_check_names: set[str] = set()

    for r in reviews:
        review_types_seen.add(r.review_type)
        has_warn = False
        has_info = False
        for f in r.findings:
            all_check_names.add(f.check)
            if f.level == "WARN":
                all_warns.append(f)
                warn_checks[f.check] += 1
                warn_check_names.add(f.check)
                has_warn = True
            elif f.level == "INFO":
                has_info = True
        if not has_warn and not has_info:
            clean_notes.append(r.note)

    no_warn_checks = sorted(all_check_names - warn_check_names)

    lines: list[str] = []
    lines.append(f"# {title} — {date.today()}")
    lines.append("")
    lines.append(f"Reviewed: {len(reviews)} notes")
    if not review_type and len(review_types_seen) > 1:
        types_str = ", ".join(sorted(review_types_seen))
        lines.append(f"Review types: {types_str}")
    lines.append("")

    # WARN table
    lines.append("## Findings")
    lines.append("")
    lines.append(f"### WARN ({len(all_warns)})")
    lines.append("")
    if all_warns:
        if review_type:
            lines.append("| Note | Check | Finding |")
            lines.append("|------|-------|---------|")
            for w in all_warns:
                note_stem = w.note.removesuffix(".md")
                lines.append(
                    f"| [{note_stem}](../kb/notes/{w.note}) "
                    f"| {w.check} "
                    f"| {truncate(w.text)} |"
                )
        else:
            lines.append("| Note | Review | Check | Finding |")
            lines.append("|------|--------|-------|---------|")
            for w in all_warns:
                note_stem = w.note.removesuffix(".md")
                lines.append(
                    f"| [{note_stem}](../kb/notes/{w.note}) "
                    f"| {w.review_type} "
                    f"| {w.check} "
                    f"| {truncate(w.text)} |"
                )
    else:
        lines.append("No warnings.")
    lines.append("")

    # Checks with no warnings
    lines.append("## Checks with no warnings")
    lines.append("")
    if no_warn_checks:
        for c in no_warn_checks:
            lines.append(f"- {c}")
    else:
        lines.append("All checks produced at least one warning.")
    lines.append("")

    # Most common findings
    lines.append("## Most common findings")
    lines.append("")
    top_warns = warn_checks.most_common(3)
    if top_warns:
        for check, count in top_warns:
            lines.append(f"- **{check}** ({count} warnings)")
    else:
        lines.append("No warnings to summarize.")
    lines.append("")

    # Clean notes
    lines.append("## Notes with no findings")
    lines.append("")
    if clean_notes:
        for n in sorted(clean_notes):
            stem = n.removesuffix(".md")
            lines.append(f"- [{stem}](../kb/notes/{n})")
    else:
        lines.append("All notes had at least one finding.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    review_type = sys.argv[1] if len(sys.argv) > 1 else None
    reviews_dir = Path("reviews")
    csv_dir = reviews_dir / "csv"

    if review_type:
        suffix = f".{review_type}.md"
        files = sorted(reviews_dir.glob(f"*{suffix}"))
        title = review_type.replace("-", " ").title() + " Sweep"
        output_name = f"{SUMMARY_PREFIX}.{review_type}.md"
    else:
        files = sorted(
            f
            for f in reviews_dir.glob("*.*-review.md")
            if not f.name.startswith(SUMMARY_PREFIX)
        )
        title = "Review Sweep (All Types)"
        output_name = f"{SUMMARY_PREFIX}.md"

    if not files:
        label = suffix if review_type else "*.*-review.md"
        print(f"No {label} files found in {reviews_dir}/", file=sys.stderr)
        sys.exit(1)

    # Parse all reviews
    reviews: list[NoteReview] = []
    for f in files:
        r = parse_review(f)
        if r:
            reviews.append(r)

    # Count warnings for reporting
    warn_count = sum(
        1 for r in reviews for f in r.findings if f.level == "WARN"
    )

    # Write markdown summary
    md = build_markdown(reviews, review_type, title)
    output = reviews_dir / output_name
    output.write_text(md, encoding="utf-8")
    print(f"Wrote {output} ({len(reviews)} notes, {warn_count} warnings)")

    # Write CSV tables
    export_csvs(reviews, csv_dir, review_type)
    prefix = f"{review_type}." if review_type else ""
    print(f"Wrote CSV tables to {csv_dir}/{prefix}*.csv")


if __name__ == "__main__":
    main()
