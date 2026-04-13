#!/usr/bin/env python3
"""Rebuild the generated section of index pages with generated tails."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.index_generated import (
    collect_notes_by_tag,
    find_index_files,
    sync_index,
)
from commonplace.lib.project_paths import collection_dirs, collection_for_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rebuild generated sections of index pages with generated tails.",
    )
    parser.add_argument("index_paths", nargs="*", help="Optional index files to process.")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files.")
    args = parser.parse_args()

    root = Path.cwd().resolve()

    if args.dry_run:
        print("DRY RUN - no files will be modified\n")

    tags_by_collection: dict[Path, dict] = {}
    for collection in collection_dirs(root):
        tags = collect_notes_by_tag(collection)
        if tags:
            tags_by_collection[collection] = tags
            total = sum(len(v) for v in tags.values())
            print(f"  {collection.name}: {total} tag assignments across {len(tags)} tags")

    total_assignments = sum(sum(len(v) for v in tags.values()) for tags in tags_by_collection.values())
    total_tags = sum(len(tags) for tags in tags_by_collection.values())
    print(f"Total: {total_assignments} tag assignments across {total_tags} tags\n")

    indexes = find_index_files(args.index_paths, root)
    if not indexes:
        print("No index files found.", file=sys.stderr)
        return 1

    changes = []
    for index_path in indexes:
        collection = collection_for_path(index_path, root)
        notes_by_tag = tags_by_collection.get(collection, {})
        result = sync_index(index_path, notes_by_tag, root, args.dry_run)
        if result:
            changes.append(result)

    if changes:
        print(f"\n{'Would change' if args.dry_run else 'Changed'} {len(changes)} index(es):")
        for change in changes:
            print(change)
    else:
        print("All generated sections are in sync.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
