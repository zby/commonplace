#!/usr/bin/env python3
"""Select notes with WARN-level findings in their gate reviews.

Scans review files for WARN findings and outputs a queue sorted by WARN count.

Usage:
    uv run scripts/warn_selector.py                    # all notes, all reviews
    uv run scripts/warn_selector.py --json             # JSON output
    uv run scripts/warn_selector.py kb/notes/backlinks.md  # filter to one note

Requires COMMONPLACE_REVIEW_MODEL to be set.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

from review_model import encode_model, resolve_model

REVIEWS_ROOT = Path("kb/reports/reviews")

# Two types of WARN signal:
# 1. Verdict line: **Result: WARN** — the whole review body is the finding
# 2. Inline: WARN: or WARN — at start of line or after punctuation — paragraph is the finding
VERDICT_PATTERN = re.compile(r"^\*\*Result:\s*WARN\*\*", re.MULTILINE)
INLINE_WARN_PATTERN = re.compile(r"(?:^|(?<=\.\s))(?:\*\*)?WARN(?:\*\*)?[:\s—]", re.MULTILINE)


def encode_note_path(note_path: str) -> str:
    return str(Path(note_path).with_suffix("")).replace("/", "__")


def decode_note_dir(dir_name: str) -> str:
    return dir_name.replace("__", "/") + ".md"


@dataclass
class WarnEntry:
    note_path: str
    gate_id: str
    review_path: str
    warn_text: str


@dataclass
class NoteWarns:
    note_path: str
    warns: list[WarnEntry] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.warns)


def _extract_paragraph_from(text: str, pos: int) -> str:
    """Extract from pos to next blank line or end."""
    rest = text[pos:]
    para_end = re.search(r"\n\s*\n", rest)
    if para_end:
        return rest[: para_end.start()].strip()
    return rest.strip()


def extract_warns(review_text: str) -> list[str]:
    """Extract WARN-level finding texts from a review."""
    warns = []

    # Type 1: **Result: WARN** — the whole body after the verdict is the finding
    if VERDICT_PATTERN.search(review_text):
        match = VERDICT_PATTERN.search(review_text)
        body_after = review_text[match.end() :].strip()
        if body_after:
            warns.append(body_after)
        return warns

    # Type 2: inline WARN: or WARN — extract paragraph from the WARN keyword
    for match in INLINE_WARN_PATTERN.finditer(review_text):
        warns.append(_extract_paragraph_from(review_text, match.start()))

    return warns


def scan_reviews(
    repo_root: Path,
    model: str,
    note_filter: set[str] | None = None,
) -> list[NoteWarns]:
    reviews_dir = repo_root / REVIEWS_ROOT
    if not reviews_dir.is_dir():
        return []

    encoded_model = encode_model(model)
    model_suffix = f".{encoded_model}.md"

    by_note: dict[str, NoteWarns] = {}

    for note_dir in sorted(reviews_dir.iterdir()):
        if not note_dir.is_dir():
            continue

        note_path = decode_note_dir(note_dir.name)
        if note_filter and note_path not in note_filter:
            continue

        for review_file in sorted(note_dir.glob(f"*{model_suffix}")):
            # Extract gate_id from filename: prose__source-residue.opus-4-6.md
            gate_encoded = review_file.name[: -len(model_suffix)]
            gate_id = gate_encoded.replace("__", "/")

            review_text = review_file.read_text(encoding="utf-8")
            warns = extract_warns(review_text)

            for warn_text in warns:
                if note_path not in by_note:
                    by_note[note_path] = NoteWarns(note_path=note_path)
                by_note[note_path].warns.append(
                    WarnEntry(
                        note_path=note_path,
                        gate_id=gate_id,
                        review_path=review_file.relative_to(repo_root).as_posix(),
                        warn_text=warn_text,
                    )
                )

    return sorted(by_note.values(), key=lambda nw: (-nw.count, nw.note_path))


def render_json(notes: list[NoteWarns]) -> str:
    items = []
    for nw in notes:
        items.append({
            "note_path": nw.note_path,
            "warn_count": nw.count,
            "warns": [
                {
                    "gate_id": w.gate_id,
                    "review_path": w.review_path,
                    "text": w.warn_text,
                }
                for w in nw.warns
            ],
        })
    return json.dumps(items, indent=2)


def print_grouped(notes: list[NoteWarns]) -> None:
    for nw in notes:
        print(f"{nw.note_path} ({nw.count} WARNs)")
        for w in nw.warns:
            # First line of warn text, truncated
            first_line = w.warn_text.split("\n")[0][:100]
            print(f"  - {w.gate_id}: {first_line}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Select notes with WARN-level review findings.")
    parser.add_argument("note_paths", nargs="*", help="Optional note path filter.")
    parser.add_argument("--json", action="store_true", help="JSON output with full WARN text.")
    args = parser.parse_args()

    try:
        model = resolve_model()
    except ValueError as exc:
        parser.error(str(exc))

    repo_root = Path.cwd()
    note_filter = set(args.note_paths) if args.note_paths else None

    notes = scan_reviews(repo_root, model, note_filter)

    if not notes:
        if not args.json:
            print("No WARNs found.")
        else:
            print("[]")
        return

    if args.json:
        print(render_json(notes))
    else:
        print_grouped(notes)


if __name__ == "__main__":
    main()
