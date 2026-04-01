#!/usr/bin/env python3
"""Select notes with WARN-level findings from effective gate reviews in the DB."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from gate_selector import REVIEWS_ROOT, ensure_db, resolve_db_path
from review_db import connect, import_review_text, load_effective_gate_review_map
from review_metadata import parse_review_metadata
from review_model import encode_model, resolve_model


RESULT_WARN_RE = re.compile(r"^##\s*Result:\s*WARN\b.*$", re.IGNORECASE | re.MULTILINE)
INLINE_WARN_RE = re.compile(r"^(?:\*\*)?WARN(?:\*\*)?[:\s—]", re.IGNORECASE | re.MULTILINE)


def encode_note_path(note_path: str) -> str:
    return str(Path(note_path).with_suffix("")).replace("/", "__")


def decode_note_dir(dir_name: str) -> str:
    return dir_name.replace("__", "/") + ".md"


@dataclass
class WarnEntry:
    note_path: str
    gate_id: str
    review_id: int
    review_run_id: int | None
    review_path: str | None
    review_text: str
    warn_text: str


@dataclass
class NoteWarns:
    note_path: str
    warns: list[WarnEntry] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.warns)


def _extract_paragraph_from(text: str, pos: int) -> str:
    rest = text[pos:]
    para_end = re.search(r"\n\s*\n", rest)
    if para_end:
        return rest[: para_end.start()].strip()
    return rest.strip()


def extract_warns(review_text: str) -> list[str]:
    warns: list[str] = []
    result_match = RESULT_WARN_RE.search(review_text)
    if result_match is not None:
        body_after = review_text[result_match.end() :].strip()
        if body_after:
            warns.append(body_after)
        return warns

    for match in INLINE_WARN_RE.finditer(review_text):
        warns.append(_extract_paragraph_from(review_text, match.start()))
    return warns


def sync_legacy_review_rows(
    repo_root: Path,
    *,
    model: str,
    note_filter: set[str] | None = None,
) -> None:
    db_path = resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)
    reviews_dir = repo_root / REVIEWS_ROOT
    if not reviews_dir.is_dir():
        return

    encoded_model = encode_model(model)
    model_suffix = f".{encoded_model}.md"
    dirty = False
    with connect(db_path) as conn:
        for note_dir in sorted(reviews_dir.iterdir()):
            if not note_dir.is_dir():
                continue
            note_path = decode_note_dir(note_dir.name)
            if note_filter and note_path not in note_filter:
                continue
            for review_file in sorted(note_dir.glob(f"*{model_suffix}")):
                review_text = review_file.read_text(encoding="utf-8")
                if parse_review_metadata(review_text) is None:
                    continue
                try:
                    import_review_text(
                        conn,
                        repo_root=repo_root,
                        review_text=review_text,
                        review_path=review_file,
                        reviews_root=reviews_dir,
                    )
                except ValueError:
                    continue
                dirty = True
        if dirty:
            conn.commit()


def scan_reviews(
    repo_root: Path,
    model: str,
    note_filter: set[str] | None = None,
) -> list[NoteWarns]:
    db_path = resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)
    sync_legacy_review_rows(repo_root, model=model, note_filter=note_filter)

    by_note: dict[str, NoteWarns] = {}
    with connect(db_path) as conn:
        effective_reviews = load_effective_gate_review_map(
            conn,
            note_path=next(iter(note_filter)) if note_filter and len(note_filter) == 1 else None,
            model_id=model,
        )

    for (note_path, gate_id, _model_id), review in sorted(effective_reviews.items()):
        if note_filter and note_path not in note_filter:
            continue
        review_path = repo_root / REVIEWS_ROOT / encode_note_path(note_path)
        canonical_path = review_path / f"{gate_id.replace('/', '__')}.{encode_model(model)}.md"
        warns = extract_warns(review.rationale_markdown)
        for warn_text in warns:
            if note_path not in by_note:
                by_note[note_path] = NoteWarns(note_path=note_path)
            by_note[note_path].warns.append(
                WarnEntry(
                    note_path=note_path,
                    gate_id=gate_id,
                    review_id=review.id,
                    review_run_id=review.review_run_id,
                    review_path=canonical_path.relative_to(repo_root).as_posix() if canonical_path.is_file() else None,
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
                        "review_path": w.review_path,
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
        print(f"{nw.note_path} ({nw.count} WARNs)")
        for w in nw.warns:
            first_line = w.warn_text.split("\n")[0][:100]
            print(f"  - {w.gate_id}: {first_line}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Select notes with WARN-level review findings.")
    parser.add_argument("note_paths", nargs="*", help="Optional note path filter.")
    parser.add_argument("--json", action="store_true", help="JSON output with full WARN text.")
    args = parser.parse_args()

    model = resolve_model()
    repo_root = Path.cwd()
    note_filter = set(args.note_paths) if args.note_paths else None

    notes = scan_reviews(repo_root, model, note_filter)
    if not notes:
        print("[]" if args.json else "No WARNs found.")
        return

    if args.json:
        print(render_json(notes))
    else:
        print_grouped(notes)


if __name__ == "__main__":
    main()
