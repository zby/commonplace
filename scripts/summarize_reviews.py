#!/usr/bin/env python3
"""Summarize review files into a SUMMARY report.

Without arguments, reads ALL review files (*.prose-review.md,
*.semantic-review.md, etc.) and writes reviews/SUMMARY.md.

With a review-type argument, reads only that type and writes
reviews/SUMMARY.{review-type}.md.

Usage: uv run scripts/summarize_reviews.py [review-type]

Examples: uv run scripts/summarize_reviews.py           # all review types
          uv run scripts/summarize_reviews.py prose-review
          uv run scripts/summarize_reviews.py semantic-review
"""

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


@dataclass
class NoteReview:
    note: str
    review_type: str
    warns: list[Finding] = field(default_factory=list)
    infos: list[Finding] = field(default_factory=list)
    cleans: list[str] = field(default_factory=list)


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

        if current_section == "WARN":
            review.warns.append(
                Finding(note=note, check=check, text=text, review_type=review_type)
            )
        elif current_section == "INFO":
            review.infos.append(
                Finding(note=note, check=check, text=text, review_type=review_type)
            )
        elif current_section == "CLEAN":
            review.cleans.append(check)

    return review


def truncate(text: str, max_len: int = 120) -> str:
    """Truncate text with ellipsis."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def main() -> None:
    review_type = sys.argv[1] if len(sys.argv) > 1 else None
    reviews_dir = Path("reviews")

    if review_type:
        suffix = f".{review_type}.md"
        files = sorted(reviews_dir.glob(f"*{suffix}"))
        title = review_type.replace("-", " ").title() + " Sweep"
        output_name = f"{SUMMARY_PREFIX}.{review_type}.md"
    else:
        # All review files: anything with a double-extension pattern,
        # excluding SUMMARY files
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

    # Collect all findings
    all_warns: list[Finding] = []
    all_infos: list[Finding] = []
    warn_checks: Counter[str] = Counter()
    info_checks: Counter[str] = Counter()
    clean_checks: Counter[str] = Counter()
    clean_notes: list[str] = []

    # Track which review types are included
    review_types_seen: set[str] = set()

    for r in reviews:
        review_types_seen.add(r.review_type)
        all_warns.extend(r.warns)
        all_infos.extend(r.infos)
        for w in r.warns:
            warn_checks[w.check] += 1
        for i in r.infos:
            info_checks[i.check] += 1
        for c in r.cleans:
            clean_checks[c] += 1
        if not r.warns and not r.infos:
            clean_notes.append(r.note)

    # Collect all check names seen
    all_check_names = set(warn_checks) | set(info_checks) | set(clean_checks)
    no_warn_checks = sorted(all_check_names - set(warn_checks))

    # Build summary
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

    output = reviews_dir / output_name
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output} ({len(reviews)} notes, {len(all_warns)} warnings)")


if __name__ == "__main__":
    main()
