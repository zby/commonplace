# Workshop: relocation-move-map-engine

## Question

Can note and directory relocation share one move-map engine for link rewriting, file moves, and redirects?

## Why this workshop exists

[relocation.py](../../../src/commonplace/lib/relocation.py) is the largest core-lib module and contains several near-parallel operations:

- `rewrite_links_to_relocated_note` rewrites links pointing to one moved note.
- `rebase_relative_markdown_links` rewrites links inside that moved note.
- `rewrite_links_to_moved_files` rewrites links pointing to any file in a moved directory.
- `rebase_and_rewrite_in_moved_file` rewrites links inside moved directory files.
- `update_mkdocs_config` and `add_single_redirect` both parse and rewrite `redirect_maps`.

The directory path already uses the more general representation: a map of old absolute paths to new absolute paths. The single-note path can probably become the one-entry case of the same engine.

The review-execution plan changed the relocation boundary: **do not relocate historical review records.** A moved note is a fresh review target under its new path. That removes review-store rekeying from this workshop instead of forcing the move-map engine to preserve it.

## Scope

In scope:

- one link-rewrite function parameterized by `moves: dict[Path, Path]` and source old/new location;
- one MkDocs redirect-map parser/renderer used by both note and directory relocation;
- a shared relocation plan object that describes file moves, markdown writes, and MkDocs edits before apply;
- removing review-store rekeying from the relocation flow once review identity is explicitly path-keyed;
- preserving the existing `commonplace-relocate-note` and `commonplace-relocate-directory` command contracts for file moves, link rewrites, and redirects.

Out of scope:

- changing markdown link grammar beyond the current parser behavior;
- replacing `git mv` fallback behavior;
- rekeying review rows, acceptance events, or historical review artifacts when a note moves;
- adding a `review_targets` indirection table to make review relocation work;
- changing review freshness semantics. Moved paths need fresh review under the new path.

## Current Grounding

- [relocation.py](../../../src/commonplace/lib/relocation.py) - current implementation.
- [test_relocate_note.py](../../../test/commonplace/cli/test_relocate_note.py) - single-note expectations.
- [test_relocate_directory.py](../../../test/commonplace/cli/test_relocate_directory.py) - directory expectations.
- Review DB rekey integration has already been removed; this workshop should not reintroduce relocation hooks.

## Working Hypothesis

The right internal model is:

```python
@dataclass(frozen=True)
class RelocationPlan:
    moves: dict[Path, Path]
    markdown_updates: dict[Path, tuple[Path, str, list[str]]]
    mkdocs_update: tuple[str, list[str]] | None
```

`relocate_note` builds a one-entry `moves` map. `relocate_directory` builds a many-entry map. Both pass through the same planner, reporter, and applier, with only argument resolution and optional redirect defaults kept separate.

The hook layer should not be carried forward just to support review rekeying. If no non-review hook remains after code inspection, delete the relocation hook protocol and the review hook integration as part of the cleanup.

## First Work

1. Extract redirect-map parse/render helpers without changing behavior.
2. Add tests around redirect preservation and target updates that both relocation commands use.
3. Replace the four link-rewrite functions with one shared helper, or first wrap them behind a shared planner if that is safer.
4. Remove review relocation hook execution from both relocation commands, and update tests/docs to assert that moved notes require fresh review rather than historical review rekeying.
5. Collapse the apply/dry-run reporting paths only after the link rewrite behavior is stable.

## Closure Conditions

Close when this workshop produces:

- a patch plan that can be implemented in small behavior-preserving steps;
- an explicit deletion or retirement plan for review-store rekeying from relocation;
- or a decision that note relocation should remain separate, with a concrete reason beyond historical shape.
