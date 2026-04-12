#!/usr/bin/env python3
"""Refresh generated directory indexes and generated-tail indexes for the KB."""

import sys
from pathlib import Path

from commonplace.cli import generate_notes_index, sync_generated_index

def main() -> int:
    # Generate directory indexes for collections that have index.md
    for collection in sync_generated_index.find_all_collections():
        index_file = collection / "index.md"
        if not index_file.is_file():
            continue
        content = index_file.read_text()
        fm = sync_generated_index.index_frontmatter(index_file, content)
        if fm.get("index_source") == "directory":
            output, count = generate_notes_index.write_index(collection)
            print(f"Generated {output} with {count} entries")

    # Collect tags per collection (tags are collection-scoped)
    tags_by_collection: dict[Path, dict] = {}
    for collection in sync_generated_index.find_all_collections():
        tags = sync_generated_index.collect_notes_by_tag(collection)
        if tags:
            tags_by_collection[collection] = tags
            total = sum(len(v) for v in tags.values())
            print(f"  {collection.name}: {total} tag assignments across {len(tags)} tags")

    total_assignments = sum(sum(len(v) for v in tags.values()) for tags in tags_by_collection.values())
    total_tags = sum(len(tags) for tags in tags_by_collection.values())
    print(f"Total: {total_assignments} tag assignments across {total_tags} tags\n")

    indexes = sync_generated_index.find_index_files([])
    if not indexes:
        print("No generated-tail index files found.", file=sys.stderr)
        return 1

    changes = []
    for index_path in indexes:
        collection = sync_generated_index.collection_for_path(index_path)
        notes_by_tag = tags_by_collection.get(collection, {})
        result = sync_generated_index.sync_index(index_path, notes_by_tag)
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
