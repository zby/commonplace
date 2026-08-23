# Worked case: `lib-modules.md`

Executed 2026-08-23. The first artifact taken through the full disposition.

## Result

**Every passage is recoverable. Nothing in the file needs to be authored prose.**
But the file is not free to delete, because for 37 functions it holds the only
prose description in the repository. The disposition is *dissolve*, and
dissolving it is real work.

## Recovery by search, all candidates

Rule- and rationale-shaped passages were located by searching for
"never/must/deliberately/rather than/because/would", then each was searched for
another home.

| Passage | Other home | Verdict |
|---|---|---|
| "Git and gitignore are never consulted" | [ADR 039](../../reference/adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md), stated **more completely** | drop |
| Type-spec eligibility rule | [ADR 068](../../reference/adr/068-collection-contracts-stop-enumerating-available-types.md), every `COLLECTION.md`, the validator | drop |
| Durable genre from closer reading, not capture-time judgment | `kb/sources/types/snapshot.md`; ADR 045, ADR 072 | drop |
| "never edits the ingest checksum" | [ADR 072](../../reference/adr/072-ingests-own-source-authority-and-snapshots-are-local.md); `kb/sources/types/snapshot.md` | drop |
| `text.md` excluded as the implicit no-frontmatter root | `kb/types/README.md`, `kb/types/note.md`, ADR 047 | drop |
| `walk_visible` counterfactual | nowhere | **relocated to `relocation.py`** |

**One survivor in six**, and it was a warning to the change loop rather than a
description — consistent with the prediction that surviving content is what has
no locus a search could find.

## The layers

| Layer | Measure | Disposition |
|---|---|---|
| Module overview (routing map) | 1,074 B; `lib/` is 20/20 on module docstrings | Generate or drop |
| Dependency graph | recoverable from import statements | Drop |
| Per-function prose, where a docstring exists | 70 of 107 public functions | Drop as duplicate |
| Per-function prose, where none exists | **37 of 107** | **Move into the docstring, then drop** |
| Rules and rationale | 5 of 6 recorded elsewhere | Drop |
| Change-loop warning | 1 of 6 | Already relocated to the code site |

## Two findings that were not predicted

**The file is a staging area, not a duplicate.** The disposition table implied
per-module description could simply be dropped. For 37 functions that would
destroy the only prose there is. The right operation is relocation into
docstrings — the same disposition the `walk_visible` warning received, applied
at scale rather than to one sentence. Deleting first and writing docstrings
later would lose the text in between.

**The doc covers 9 of 15 modules.** `full_pass`, `hashing`, `index_directory`,
`promotion`, `quote_verification`, and `systems_matrix` have no section at all.
So the artifact was never complete, and nothing signalled that — a reader
consulting it for `promotion` finds silence and cannot tell whether the module
is absent, undocumented, or unimportant. An index that looks whole and is not is
the failure mode [stale indexes reduce discovery](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md)
names, reached here by incompleteness rather than staleness.

## What this does to the tax argument

Moving prose into docstrings does not just relocate the maintenance cost, it
lowers it. A docstring sits in the file being edited, so it is co-maintained by
proximity rather than by discipline — the editor cannot miss it the way a
separate reference file is missed. The 72-of-120 commit coupling measured
earlier is the cost of maintaining that discipline; docstrings do not need it.

## Next actions

1. Write docstrings for the 37 public functions that lack them, sourcing text
   from the corresponding `lib-modules.md` passage where one exists.
2. Decide the routing map: generated-and-checked from module docstrings, or
   dropped in favour of a `rg` over docstrings.
3. Then delete `lib-modules.md`, with a `properdocs.yml` redirect.

Step 1 is a code change of real size and is not started. Steps 2 and 3 depend on
it: deleting first would discard the source text for step 1.

## Open

- Is the same staging-area pattern present in the other six artifacts, or is
  `lib-modules.md` unusual in holding prose the code lacks?
- Does the routing map survive as a generated artifact, or does `rg` over
  docstrings make even that redundant?
