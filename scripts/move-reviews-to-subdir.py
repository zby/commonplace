#!/usr/bin/env python3
"""One-off: move individual system reviews into kb/agent-memory-systems/reviews/.

Keeps at the top level: README.md, related-systems-index.md, and cross-system
analyses (comparative-review, thalo-type-comparison, types/).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from commonplace.lib.relocation import (
    find_repo_markdown_files,
    rebase_and_rewrite_in_moved_file,
    rewrite_links_to_moved_files,
    collect_review_export_updates,
    move_path,
)
from commonplace.review import review_db


REPO_ROOT = Path.cwd().resolve()
KB_ROOT = REPO_ROOT / "kb"
COLLECTION = KB_ROOT / "agent-memory-systems"
REVIEWS_SUBDIR = COLLECTION / "reviews"

# Files that stay at the collection root
KEEP_AT_ROOT = {
    "README.md",
    "related-systems-index.md",
    "agentic-memory-systems-comparative-review.md",
    "thalo-type-comparison.md",
}


def compute_moves() -> dict[Path, Path]:
    """Return a dict of old_path -> new_path for files to move."""
    moves = {}
    for f in COLLECTION.iterdir():
        if not f.is_file() or f.suffix != ".md":
            continue
        if f.name in KEEP_AT_ROOT:
            continue
        moves[f.resolve()] = (REVIEWS_SUBDIR / f.name).resolve()
    return moves


def main(apply: bool = False) -> int:
    if not COLLECTION.is_dir():
        print(f"Collection does not exist: {COLLECTION}", file=sys.stderr)
        return 1

    moves = compute_moves()
    print(f"Files to move: {len(moves)}")
    for old, new in sorted(moves.items()):
        print(f"  {old.relative_to(REPO_ROOT)} -> {new.relative_to(REPO_ROOT)}")

    # Compute markdown updates across repo
    updates: dict[Path, tuple[Path, str, list[str]]] = {}
    for md_file in find_repo_markdown_files(REPO_ROOT):
        original = md_file.read_text(encoding="utf-8")
        md_resolved = md_file.resolve()
        if md_resolved in moves:
            new_path = moves[md_resolved]
            updated, changes = rebase_and_rewrite_in_moved_file(
                original, md_file, new_path, moves
            )
            target = new_path
        else:
            updated, changes = rewrite_links_to_moved_files(original, md_file, moves)
            target = md_file
        if changes:
            updates[md_file] = (target, updated, changes)

    print(f"\nMarkdown files to update: {len(updates)}")
    total_link_changes = sum(len(changes) for _, _, changes in updates.values())
    print(f"Total link changes: {total_link_changes}")

    # Review exports and DB
    review_export_moves: list[tuple[Path, Path]] = []
    review_export_file_updates: list[tuple[Path, str]] = []
    review_db_rekeys: list[tuple[str, str]] = []
    db_path = review_db.resolve_db_path(REPO_ROOT)
    has_db = db_path.exists()

    for old_md, new_md in moves.items():
        src_review_dir, dst_review_dir, file_updates = collect_review_export_updates(
            old_md, new_md, repo_root=REPO_ROOT, kb_root=KB_ROOT
        )
        if src_review_dir.exists():
            review_export_moves.append((src_review_dir, dst_review_dir))
            for f, content in file_updates.items():
                rel = f.relative_to(src_review_dir)
                review_export_file_updates.append((dst_review_dir / rel, content))
        if has_db:
            review_db_rekeys.append(
                (
                    old_md.relative_to(REPO_ROOT).as_posix(),
                    new_md.relative_to(REPO_ROOT).as_posix(),
                )
            )

    print(f"Review export dirs: {len(review_export_moves)}")
    if has_db:
        print(f"Review DB rekeys: {len(review_db_rekeys)}")

    if not apply:
        print("\nDry run. Pass --apply to execute.")
        return 0

    # Create reviews/ subdirectory
    REVIEWS_SUBDIR.mkdir(exist_ok=True)

    # git mv each file
    for old, new in moves.items():
        subprocess.run(
            [
                "git", "mv",
                str(old.relative_to(REPO_ROOT)),
                str(new.relative_to(REPO_ROOT)),
            ],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    # Write updated markdown files
    for _, (target, updated, _changes) in updates.items():
        target.write_text(updated, encoding="utf-8")

    # Move review export directories
    for src_review_dir, dst_review_dir in review_export_moves:
        move_path(src_review_dir, dst_review_dir, repo_root=REPO_ROOT)
    for target, content in review_export_file_updates:
        target.write_text(content, encoding="utf-8")

    # Rekey review DB
    if has_db and review_db_rekeys:
        with review_db.connect(db_path) as conn:
            for old, new in review_db_rekeys:
                review_db.rekey_note_path(conn, old_note_path=old, new_note_path=new)
            conn.commit()

    print(f"\nMoved {len(moves)} files.")
    print("Done.")
    return 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(apply=args.apply))
