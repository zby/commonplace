# Worked case: `lib-modules.md`

Executed 2026-08-23; disposition completed 2026-08-24. The first artifact
taken through the full procedure and retired.

## Result

**Retired. Every passage was recoverable, and the live source supplied the
better routing surface.** One change-loop warning and one caller-context
distinction reached their code sites before deletion. Closer inspection rejected
the other proposed docstring relocations as source paraphrase.

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

## The relocation was almost entirely unnecessary

The staging-area finding above overstated what the prose holds. Applying the
rule *a docstring should carry only what the source does not* — assuming a
reader who can read the function — the 37 split as:

- **13** lack both a docstring and any doc prose. Nothing to relocate; writing
  them is a separate job.
- **24** have doc prose. Judged one by one against their function bodies,
  **one** carried something the code does not say.

The survivor is `type_resolver.resolve_type`: *a validation run supplies its
cached frontmatter loader; standalone callers omit it.* The signature shows the
parameter is optional; nothing in the file says who passes it or why. Written.

Everything else was restatement. `strip_frontmatter`'s prose is "Delegates to
`frontmatter.strip()`" against a body of `return fm_mod.strip(content)`.
`extract_title` is "First H1 heading text, or `Untitled`" against a regex and
that literal. `validate_links_from_document` is "verify each local relative link
target actually exists" against a loop doing exactly that.

Three were marginal and judged out. `move_path`'s "Git is not involved; it
detects the rename on commit" is a real absence-fact, but it is
[ADR 039](../../reference/adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md)'s;
`remove_code_regions` and `find_markdown_links_with_text` name their callers,
which a grep recovers. Under a strict reading of the rule, discoverable means
drop.

**So the prose was not a staging area after all — it was a paraphrase layer.**
Relocating it wholesale would have imported 24 restatements into the code and
called it a saving. The measurement that made it look valuable, 37 functions
without docstrings, counted absence rather than content.

## Routing experiment and retirement

After the user-level editable tool was reinstalled, `commonplace-source`
resolved to the package supplying the running commands. Searches began with
task vocabulary rather than known module names:

| Question terms | Live-source result | Reference result |
|---|---|---|
| promotion candidate, incoming links | `promotion.py` at its module docstring | no hit |
| full-pass, capture verification, transition guarding | `full_pass.py` at its module docstring | no hit |
| quotation, verbatim, quote | `quote_verification.py`, plus its call sites | incidental validation prose, not the owning module |
| collection discovery, visible walks, visibility | `project_paths.py` | the expected map entry |

Every top-level module in `commonplace.lib` has a module docstring. The authored
map listed nine of the fifteen modules. Live search therefore matched its one
covered routing case and reached three owners the map omitted. The map was
dropped rather than generated: no demonstrated question needed another
materialized layer once task vocabulary selected the source directly.

The file was deleted on 2026-08-24. Current routes now direct exact internal API
questions to `src/commonplace/lib/`, and the published URL redirects to the
reference landing. The code change this case implied remains one docstring, not
37.

Separately, and not part of this disposition, 13 functions lack both a
docstring and former reference prose. Whether they need a docstring is the same
question asked of the code alone, with no prose to salvage.

## Open

- Is the same staging-area pattern present in the other six artifacts, or is
  `lib-modules.md` unusual in holding prose the code lacks?
