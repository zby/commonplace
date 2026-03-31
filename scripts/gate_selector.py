#!/usr/bin/env python3
"""Select stale (note, gate) pairs using mtime-based staleness.

Staleness rules (like make):
  - Review file missing           → stale (missing-review)
  - Gate mtime > review mtime     → stale (gate-changed)
  - Note mtime > review mtime     → stale (note-changed), diff included in JSON output

See scripts/REVIEW-SYSTEM.md for the full design.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from review_model import encode_model, resolve_model

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

def note_diff_since(repo_root: Path, note_path: str, since_mtime: float) -> str | None:
    """Git diff of a note from the last commit before since_mtime to the working tree."""
    since_iso = datetime.fromtimestamp(since_mtime, tz=timezone.utc).isoformat()

    # Find the last commit at or before the review mtime
    result = subprocess.run(
        ["git", "log", f"--before={since_iso}", "-1", "--format=%H", "--", note_path],
        capture_output=True, text=True, cwd=repo_root,
    )
    base_commit = result.stdout.strip()
    if not base_commit:
        return None

    # Diff from that commit to the working tree
    result = subprocess.run(
        ["git", "diff", base_commit, "--", note_path],
        capture_output=True, text=True, cwd=repo_root,
    )
    diff = result.stdout.strip()
    return diff if diff else None


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

    review_mtime = os.path.getmtime(review_abs)

    if os.path.getmtime(gate_abs) > review_mtime:
        return StaleGate(note_path, gate_id, "gate-changed")

    if os.path.getmtime(note_abs) > review_mtime:
        diff = note_diff_since(repo_root, note_path, review_mtime) if include_diff else None
        return StaleGate(note_path, gate_id, "note-changed", diff=diff)

    # Caveat: if git checkout (or similar) rewrites the review file, its mtime
    # jumps to "now", potentially hiding genuine note changes. This is rare
    # (requires the review to differ across branches) but silent. Re-run the
    # sweep after branch operations if you suspect false freshness.
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
    """Touch review files to mark (note, gate) pairs as acknowledged."""
    for pair in pairs:
        if ":" not in pair:
            print(f"error: invalid pair (expected note:gate): {pair}", file=sys.stderr)
            sys.exit(1)
        note_path, gate_id = pair.split(":", 1)
        review = repo_root / review_path_for(note_path, gate_id, model)
        review.parent.mkdir(parents=True, exist_ok=True)
        review.touch()
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
        help="Ack (note, gate) pairs by touching review files. Format: note_path:gate_id",
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
