#!/usr/bin/env python3
"""Select stale review targets from the canonical review DB."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.resolve_gates import applicable_gate_ids_for_note, resolve_to_gate_ids
from commonplace.review.review_db import (
    GATES_ROOT,
    append_acceptance_event,
    connect,
    ensure_db,
    load_current_acceptances,
    resolve_db_path,
)
from commonplace.review.review_metadata import blob_text_at_sha, file_text_at_commit, git_blob_sha, iso_now, last_commit_for_path

NOTES_ROOT = Path("kb/notes")


def _has_frontmatter(path: Path) -> bool:
    try:
        with path.open(encoding="utf-8") as f:
            return f.read(4) == "---\n"
    except (OSError, UnicodeDecodeError):
        return False


def _is_index(path: Path) -> bool:
    return path.name == "index.md" or path.name.endswith("-index.md")


def _frontmatter_status(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    result = frontmatter.parse(text)
    return result.data.get("status") if result.ok else None


def list_reviewable_notes(notes_dir: Path) -> list[Path]:
    return sorted(
        p for p in notes_dir.glob("*.md")
        if not _is_index(p) and _has_frontmatter(p)
    )


def list_current_notes(notes_dir: Path) -> list[Path]:
    return [
        path
        for path in list_reviewable_notes(notes_dir)
        if _frontmatter_status(path) == "current"
    ]


@dataclass(frozen=True)
class StaleGate:
    note_path: str
    gate_id: str
    reason: str
    diff: str | None = None


def note_diff_since(
    repo_root: Path,
    note_path: str,
    note_abs: Path,
    accepted_note_sha: str,
    accepted_note_commit: str | None,
) -> str | None:
    import difflib

    previous_text = blob_text_at_sha(repo_root, accepted_note_sha)
    if previous_text is None and accepted_note_commit:
        previous_text = file_text_at_commit(repo_root, accepted_note_commit, Path(note_path))
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


def select_stale_gates(
    repo_root: Path,
    *,
    model: str,
    gate_ids: list[str],
    note_filter: list[str] | None = None,
    current_only: bool = False,
    include_diff: bool = False,
) -> list[StaleGate]:
    gates_dir = repo_root / GATES_ROOT
    notes_dir = repo_root / NOTES_ROOT
    model = model.strip()
    if not model:
        raise ValueError("model is required")
    db_path = resolve_db_path(repo_root)

    if note_filter and current_only:
        raise ValueError("--note and --current are mutually exclusive")

    if note_filter:
        notes: list[Path] = []
        for raw in note_filter:
            p = Path(raw) if Path(raw).is_absolute() else repo_root / raw
            p = p.resolve()
            if not p.is_file():
                raise ValueError(f"Note not found: {raw}")
            notes.append(p)
    elif current_only:
        notes = list_current_notes(notes_dir)
    else:
        notes = list_reviewable_notes(notes_dir)

    note_paths = [note_abs.relative_to(repo_root).as_posix() for note_abs in notes]
    ensure_db(repo_root, db_path)
    with connect(db_path) as conn:
        acceptances = load_current_acceptances(conn)

    stale: list[StaleGate] = []
    for note_abs, note_path in zip(notes, note_paths):
        current_note_sha = git_blob_sha(note_abs)
        applicable_gate_ids = applicable_gate_ids_for_note(note_abs, gate_ids, gates_dir)
        for gate_id in applicable_gate_ids:
            gate_abs = gates_dir / f"{gate_id}.md"
            if not gate_abs.is_file():
                raise FileNotFoundError(f"Gate not found: {gate_id}")

            # Bundles resolve directly from gate directories, so the gate file hash is the whole contract today.
            current_gate_sha = git_blob_sha(gate_abs)
            acceptance = acceptances.get((note_path, gate_id, model))
            if acceptance is None:
                stale.append(StaleGate(note_path, gate_id, "missing-review"))
                continue
            if acceptance.accepted_gate_sha != current_gate_sha:
                stale.append(StaleGate(note_path, gate_id, "gate-changed"))
                continue
            if acceptance.accepted_note_sha != current_note_sha:
                diff = None
                if include_diff:
                    diff = note_diff_since(
                        repo_root,
                        note_path,
                        note_abs,
                        acceptance.accepted_note_sha,
                        acceptance.accepted_note_commit,
                    )
                stale.append(StaleGate(note_path, gate_id, "note-changed", diff=diff))

    return sorted(stale, key=lambda s: (s.note_path, s.gate_id))


def render_json(records: list[StaleGate]) -> str:
    items = []
    for record in records:
        entry: dict[str, str] = {
            "note_path": record.note_path,
            "gate_id": record.gate_id,
            "reason": record.reason,
        }
        if record.diff is not None:
            entry["diff"] = record.diff
        items.append(entry)
    return json.dumps(items, indent=2)


def print_grouped(records: list[StaleGate]) -> None:
    grouped: dict[str, list[StaleGate]] = {}
    for record in records:
        grouped.setdefault(record.note_path, []).append(record)
    for note_path in sorted(grouped):
        print(note_path)
        for record in sorted(grouped[note_path], key=lambda item: item.gate_id):
            print(f"  - {record.gate_id} ({record.reason})")


def ack_pairs(repo_root: Path, pairs: list[str], model: str) -> None:
    db_path = resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    with connect(db_path) as conn:
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

            note_sha = git_blob_sha(note_abs, write_object=True)
            current_gate_sha = git_blob_sha(gate_abs)
            note_commit = last_commit_for_path(repo_root, Path(note_path))
            append_acceptance_event(
                conn,
                note_path=note_path,
                gate_id=gate_id,
                model_id=model,
                accepted_review_id=None,
                accepted_note_sha=note_sha,
                accepted_note_commit=note_commit,
                accepted_gate_sha=current_gate_sha,
                accepted_at=iso_now(),
                acceptance_kind="trivial-change-ack",
            )
            print(f"acked: {note_path} {gate_id}")
        conn.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="List stale (note, gate) review pairs.")
    parser.add_argument(
        "gate_or_bundle",
        nargs="*",
        help="Gate IDs (e.g. prose/source-residue) and/or bundle names (e.g. prose).",
    )
    parser.add_argument("--all-gates", action="store_true", help="Check all gates.")
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths.")
    parser.add_argument("--current", action="store_true", help="Filter to notes with frontmatter status: current.")
    parser.add_argument("--json", action="store_true", help="JSON output (includes diffs for note-changed).")
    parser.add_argument("--model", required=True, help="Review model partition to query or acknowledge.")
    parser.add_argument(
        "--reason",
        choices=["missing-review", "gate-changed", "note-changed"],
        help="Filter output to a single staleness reason.",
    )
    parser.add_argument(
        "--ack",
        nargs="+",
        metavar="NOTE:GATE",
        help="Ack (note, gate) pairs. Format: note_path:gate_id",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    model = args.model.strip()
    if not model:
        parser.error("--model must not be empty")

    if args.ack:
        ack_pairs(repo_root, args.ack, model)
        return

    gates_dir = repo_root / GATES_ROOT

    if args.all_gates:
        if args.gate_or_bundle:
            parser.error("gate/bundle names and --all-gates are mutually exclusive")
        bundles = sorted(d.name for d in gates_dir.iterdir() if d.is_dir())
        gate_ids = resolve_to_gate_ids(bundles, gates_dir)
    elif args.gate_or_bundle:
        gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    else:
        parser.error("provide gate/bundle names or --all-gates")

    try:
        records = select_stale_gates(
            repo_root,
            model=model,
            gate_ids=gate_ids,
            note_filter=args.note_paths,
            current_only=args.current,
            include_diff=args.json,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    if args.reason:
        records = [record for record in records if record.reason == args.reason]

    if args.json:
        print(render_json(records))
    else:
        print_grouped(records)


if __name__ == "__main__":
    main()
