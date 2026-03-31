#!/usr/bin/env python3
"""Select stale (note, gate) pairs using review metadata.

Staleness rules:
  - Review file missing or metadata missing        → stale (missing-review)
  - Gate fingerprint != review gate fingerprint    → stale (gate-changed)
  - Note blob sha != accepted note sha in review   → stale (note-changed)

See scripts/REVIEW-SYSTEM.md for the full design.
"""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from review_model import encode_model, resolve_model
from review_metadata import (
    ReviewMetadata,
    blob_text_at_sha,
    file_text_at_commit,
    git_blob_sha,
    inject_review_metadata,
    iso_now,
    last_commit_for_path,
    parse_review_metadata,
)

GATES_ROOT = Path("kb/instructions/review-gates")
REVIEWS_ROOT = Path("kb/reports/reviews")
NOTES_ROOT = Path("kb/notes")


# ---------------------------------------------------------------------------
# Path encoding (matches resolve_gates.py)
# ---------------------------------------------------------------------------

def encode_note_path(note_path: str) -> str:
    return str(Path(note_path).with_suffix("")).replace("/", "__")


def encode_gate_id(gate_id: str) -> str:
    return gate_id.replace("/", "__")


def review_path_for(note_path: str, gate_id: str, model: str) -> Path:
    return REVIEWS_ROOT / encode_note_path(note_path) / f"{encode_gate_id(gate_id)}.{encode_model(model)}.md"


# ---------------------------------------------------------------------------
# Gate discovery
# ---------------------------------------------------------------------------

def list_all_gate_ids(gates_dir: Path) -> list[str]:
    return [
        f.relative_to(gates_dir).with_suffix("").as_posix()
        for f in sorted(gates_dir.rglob("*.md"))
    ]


def list_bundle_gate_ids(gates_dir: Path, bundle: str) -> list[str]:
    bundle_dir = gates_dir / bundle
    if not bundle_dir.is_dir():
        raise FileNotFoundError(f"Bundle directory not found: {bundle}")
    return [f"{bundle}/{f.stem}" for f in sorted(bundle_dir.glob("*.md"))]


# ---------------------------------------------------------------------------
# Note discovery
# ---------------------------------------------------------------------------

def _has_frontmatter(path: Path) -> bool:
    try:
        with path.open(encoding="utf-8") as f:
            return f.read(4) == "---\n"
    except (OSError, UnicodeDecodeError):
        return False


def _is_index(path: Path) -> bool:
    return path.name == "index.md" or path.name.endswith("-index.md")


def list_reviewable_notes(notes_dir: Path) -> list[Path]:
    return sorted(
        p for p in notes_dir.glob("*.md")
        if not _is_index(p) and _has_frontmatter(p)
    )


# ---------------------------------------------------------------------------
# Diff generation
# ---------------------------------------------------------------------------

def note_diff_since(
    repo_root: Path,
    note_path: str,
    note_abs: Path,
    metadata: ReviewMetadata,
) -> str | None:
    """Unified diff from the accepted note revision to the current working tree."""
    previous_text: str | None = None
    if metadata.last_accepted_note_sha:
        previous_text = blob_text_at_sha(repo_root, metadata.last_accepted_note_sha)
    if previous_text is None and metadata.last_accepted_note_commit:
        previous_text = file_text_at_commit(repo_root, metadata.last_accepted_note_commit, Path(note_path))
    if previous_text is None:
        return None

    current_text = note_abs.read_text(encoding="utf-8")
    diff = "".join(
        difflib.unified_diff(
            previous_text.splitlines(keepends=True),
            current_text.splitlines(keepends=True),
            fromfile=f"a/{note_path}",
            tofile=f"b/{note_path}",
        )
    ).strip()
    return diff or None


# ---------------------------------------------------------------------------
# Staleness evaluation
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class StaleGate:
    note_path: str
    gate_id: str
    reason: str
    diff: str | None = None


def evaluate_gate(
    repo_root: Path,
    note_path: str,
    gate_id: str,
    model: str,
    note_abs: Path,
    gate_abs: Path,
    include_diff: bool = False,
) -> StaleGate | None:
    review_abs = repo_root / review_path_for(note_path, gate_id, model)

    if not review_abs.is_file():
        return StaleGate(note_path, gate_id, "missing-review")

    metadata = parse_review_metadata(review_abs.read_text(encoding="utf-8"))
    if metadata is None:
        return StaleGate(note_path, gate_id, "missing-review")
    if metadata.note_path and metadata.note_path != note_path:
        return StaleGate(note_path, gate_id, "missing-review")
    if metadata.gate_id and metadata.gate_id != gate_id:
        return StaleGate(note_path, gate_id, "missing-review")
    if metadata.last_accepted_note_sha is None or metadata.gate_fingerprint is None:
        return StaleGate(note_path, gate_id, "missing-review")

    current_gate_fingerprint = git_blob_sha(gate_abs)
    if current_gate_fingerprint != metadata.gate_fingerprint:
        return StaleGate(note_path, gate_id, "gate-changed")

    current_note_sha = git_blob_sha(note_abs)
    if current_note_sha != metadata.last_accepted_note_sha:
        diff = note_diff_since(repo_root, note_path, note_abs, metadata) if include_diff else None
        return StaleGate(note_path, gate_id, "note-changed", diff=diff)

    return None


def select_stale_gates(
    repo_root: Path,
    *,
    bundle: str | None = None,
    include_all: bool = False,
    note_filter: list[str] | None = None,
    include_diff: bool = False,
) -> list[StaleGate]:
    gates_dir = repo_root / GATES_ROOT
    notes_dir = repo_root / NOTES_ROOT

    model = resolve_model()

    if include_all:
        gate_ids = list_all_gate_ids(gates_dir)
    elif bundle:
        gate_ids = list_bundle_gate_ids(gates_dir, bundle)
    else:
        raise ValueError("provide a bundle name or --all-gates")

    if note_filter:
        notes: list[Path] = []
        for raw in note_filter:
            p = Path(raw) if Path(raw).is_absolute() else repo_root / raw
            p = p.resolve()
            if not p.is_file():
                raise ValueError(f"Note not found: {raw}")
            notes.append(p)
    else:
        notes = list_reviewable_notes(notes_dir)

    stale: list[StaleGate] = []
    for note_abs in notes:
        note_rel = note_abs.relative_to(repo_root).as_posix()
        for gate_id in gate_ids:
            gate_abs = gates_dir / f"{gate_id}.md"
            result = evaluate_gate(repo_root, note_rel, gate_id, model, note_abs, gate_abs, include_diff)
            if result is not None:
                stale.append(result)

    return sorted(stale, key=lambda s: (s.note_path, s.gate_id))


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def render_json(records: list[StaleGate], model: str) -> str:
    items = []
    for r in records:
        entry: dict[str, str] = {
            "note_path": r.note_path,
            "gate_id": r.gate_id,
            "reason": r.reason,
            "review_path": str(review_path_for(r.note_path, r.gate_id, model)),
        }
        if r.diff is not None:
            entry["diff"] = r.diff
        items.append(entry)
    return json.dumps(items, indent=2)


def print_grouped(records: list[StaleGate]) -> None:
    grouped: dict[str, list[StaleGate]] = {}
    for r in records:
        grouped.setdefault(r.note_path, []).append(r)
    for note_path in sorted(grouped):
        print(note_path)
        for r in sorted(grouped[note_path], key=lambda s: s.gate_id):
            print(f"  - {r.gate_id} ({r.reason})")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def ack_pairs(repo_root: Path, pairs: list[str], model: str) -> None:
    """Rewrite review metadata to mark (note, gate) pairs as acknowledged."""
    for pair in pairs:
        if ":" not in pair:
            print(f"error: invalid pair (expected note:gate): {pair}", file=sys.stderr)
            sys.exit(1)
        note_path, gate_id = pair.split(":", 1)
        note_abs = repo_root / note_path
        gate_abs = repo_root / GATES_ROOT / f"{gate_id}.md"
        if not note_abs.is_file():
            print(f"error: note not found: {note_path}", file=sys.stderr)
            sys.exit(1)
        if not gate_abs.is_file():
            print(f"error: gate not found: {gate_id}", file=sys.stderr)
            sys.exit(1)

        review = repo_root / review_path_for(note_path, gate_id, model)
        review.parent.mkdir(parents=True, exist_ok=True)
        existing_text = review.read_text(encoding="utf-8") if review.exists() else ""
        existing_metadata = parse_review_metadata(existing_text)
        now = iso_now()
        note_sha = git_blob_sha(note_abs, write_object=True)
        gate_fingerprint = git_blob_sha(gate_abs)
        note_commit = last_commit_for_path(repo_root, Path(note_path))

        updated_metadata = ReviewMetadata(
            note_path=note_path,
            gate_id=gate_id,
            gate_fingerprint=gate_fingerprint,
            last_full_review_note_sha=(
                existing_metadata.last_full_review_note_sha if existing_metadata else None
            ),
            last_full_review_note_commit=(
                existing_metadata.last_full_review_note_commit if existing_metadata else None
            ),
            last_full_review_at=existing_metadata.last_full_review_at if existing_metadata else None,
            last_accepted_note_sha=note_sha,
            last_accepted_note_commit=note_commit,
            last_accepted_at=now,
            last_acceptance_kind="trivial-change-ack",
            review_type=existing_metadata.review_type if existing_metadata else "gate-review",
        )
        review.write_text(
            inject_review_metadata(existing_text, updated_metadata),
            encoding="utf-8",
        )
        print(f"acked: {note_path} {gate_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="List stale (note, gate) review pairs.")
    parser.add_argument("bundle", nargs="?", help="Bundle name (e.g. prose, semantic).")
    parser.add_argument("note_paths", nargs="*", help="Optional note path filter.")
    parser.add_argument("--all-gates", action="store_true", help="Check all gates.")
    parser.add_argument("--json", action="store_true", help="JSON output (includes diffs for note-changed).")
    parser.add_argument(
        "--reason", choices=["missing-review", "gate-changed", "note-changed"],
        help="Filter output to a single staleness reason.",
    )
    parser.add_argument(
        "--ack", nargs="+", metavar="NOTE:GATE",
        help="Ack (note, gate) pairs by rewriting acceptance metadata. Format: note_path:gate_id",
    )
    args = parser.parse_args()

    if not args.bundle and not args.all_gates:
        parser.error("provide a bundle name or --all-gates")
    if args.bundle and args.all_gates:
        parser.error("bundle and --all-gates are mutually exclusive")

    repo_root = Path.cwd()
    try:
        model = resolve_model()
        if args.ack:
            ack_pairs(repo_root, args.ack, model)
            return
        records = select_stale_gates(
            repo_root,
            bundle=args.bundle,
            include_all=args.all_gates,
            note_filter=args.note_paths or None,
            include_diff=args.json,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    if args.reason:
        records = [r for r in records if r.reason == args.reason]

    if args.json:
        print(render_json(records, model))
    else:
        print_grouped(records)


if __name__ == "__main__":
    main()
