#!/usr/bin/env python3
"""Refresh generated directory indexes and generated-tail indexes for the KB."""

import sys
from pathlib import Path

from commonplace.lib import index_directory, index_generated
from commonplace.lib.project_paths import collection_dirs, collection_for_path


def main() -> int:
    root = Path.cwd().resolve()

    # Generate directory indexes for every collection. write_index recurses
    # into qualifying subdirectories. kb/reports/ is operational and excluded
    # from the published site, so it doesn't get auto-indexed.
    # COLLECTION_MAX_DEPTH caps recursion per collection. instructions stops
    # at one level because each cp-skill-* subdir is essentially a single
    # SKILL.md and the review-gates/ tree is a deep but flat catalog of gate
    # definitions — neither benefits from nested dir-indexes.
    COLLECTION_MAX_DEPTH = {"instructions": 1}
    for collection in collection_dirs(root):
        if collection.name == "reports":
            continue
        max_depth = COLLECTION_MAX_DEPTH.get(collection.name)
        output, count = index_directory.write_index(
            collection,
            max_depth=max_depth,
            ignore_root=root,
        )
        print(f"Generated {output} with {count} entries")

    # Collect tags per collection (tags are collection-scoped)
    tags_by_collection: dict[Path, dict] = {}
    for collection in collection_dirs(root):
        tags = index_generated.collect_notes_by_tag(collection)
        if tags:
            tags_by_collection[collection] = tags
            total = sum(len(v) for v in tags.values())
            print(
                f"  {collection.name}: {total} tag assignments across {len(tags)} tags"
            )

    total_assignments = sum(
        sum(len(v) for v in tags.values()) for tags in tags_by_collection.values()
    )
    total_tags = sum(len(tags) for tags in tags_by_collection.values())
    print(f"Total: {total_assignments} tag assignments across {total_tags} tags\n")

    indexes = index_generated.find_index_files([], root)
    if not indexes:
        print("No generated-tail index files found.", file=sys.stderr)
        return 1

    changes = []
    for index_path in indexes:
        collection = collection_for_path(index_path, root)
        notes_by_tag = tags_by_collection.get(collection, {})
        result = index_generated.sync_index(index_path, notes_by_tag, root)
        if result:
            changes.append(result)

    if changes:
        print(f"\nChanged {len(changes)} index(es):")
        for change in changes:
            print(change)
    else:
        print("All generated sections are in sync.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
