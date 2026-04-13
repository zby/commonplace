#!/usr/bin/env python3
"""Refresh generated directory indexes and generated-tail indexes for the KB."""

import sys
from pathlib import Path

from commonplace.lib import index_directory, index_generated
from commonplace.lib.project_paths import collection_dirs, collection_for_path


def main() -> int:
    root = Path.cwd().resolve()

    # Generate directory indexes for collections that have dir-index.md
    for collection in collection_dirs(root):
        index_file = collection / "dir-index.md"
        if not index_file.is_file():
            continue
        content = index_file.read_text()
        fm = index_generated.index_frontmatter(index_file, content)
        if fm.get("index_source") == "directory":
            output, count = index_directory.write_index(collection)
            print(f"Generated {output} with {count} entries")

    # Collect tags per collection (tags are collection-scoped)
    tags_by_collection: dict[Path, dict] = {}
    for collection in collection_dirs(root):
        tags = index_generated.collect_notes_by_tag(collection)
        if tags:
            tags_by_collection[collection] = tags
            total = sum(len(v) for v in tags.values())
            print(f"  {collection.name}: {total} tag assignments across {len(tags)} tags")

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
