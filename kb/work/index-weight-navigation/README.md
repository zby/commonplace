# Workshop: Index weight and navigation policy

## Goal

Make Commonplace robust for **large collections**. Most of the framework was shaped when collections were small enough that generated artifacts were cheap to load. As a KB grows, those artifacts — especially complete inventories like `dir-index.md` — turn into context debt: an operation's per-fork load grows with total collection size rather than with the work at hand, until ordinary operations stop being feasible (see the eval finding in grounding). The system should scale so that the cost of a write, an ingest, or a connect depends on the *task*, not on how many notes already exist. This workshop is the navigation-and-index-weight slice of that goal; index policy is the first place collection growth bites.

## Question

How should Commonplace use generated indexes once full collection indexes become too heavy to load as ordinary agent context?

The immediate pressure is `dir-index.md`: it is valuable as a complete, committed inventory, but full reads of large collection indexes now cost tens of KB before the agent has selected any candidate body. This is especially painful in `cp-skill-connect`, where every authorised destination can trigger a full index read. The broader question is how to keep generated navigation surfaces useful without letting them become hidden context debt.

## Current hypothesis (revised 2026-06-07)

Split generated navigation by *who reads it*, and treat the complete inventory differently from curated indexes.

1. **Complete per-collection inventory (`dir-index.md`) — retire from git.** It is pure denormalization: every title and description it lists already lives in the note's own frontmatter, so it gives an agent nothing the source files don't, while costing tens of KB on every read (the connect/write overhead the eval flagged — see grounding). Its only real value is for *human* readers. So generate it at **mkdocs build time** for the published site and stop committing it. Agents reconstruct what they need with `ls` and scoped `rg`, which is cheaper because it returns only matches, never the whole inventory.

2. **Curated indexes (tag and area indexes) — keep committed, lists colocated.** These carry human orientation that generation cannot produce, and they are *scoped* (one tag / one area), so their auto-generated lists are bounded by the size of that slice, not the whole collection. **Keep the generated list colocated with the curated head in one file** — orientation sitting next to the entries it orients is the ergonomic win; do not split the list out. These are the focused routing surfaces write/connect may read directly.

3. **Uncurated slices — structured `rg`.** Tags or slices that do not warrant a curated index are served by a scoped query (by tag, keyword, or area), not by generating a standalone index file for each.

Net: the note files are the single source of truth; humans get build-time pages; agents get curated focused indexes plus scoped query. The pathological artifact is specifically the *unscoped complete* inventory, not generated lists in general.

## Design sketch

### 1. Generation moves out of git for the complete inventory

- `commonplace-refresh-indexes` stops writing per-collection `dir-index.md` to the repo; that generation moves into the mkdocs build (plugin or hook) so the published site still has browsable inventories.
- `git rm` the existing `dir-index.md` files and gitignore them.
- Curated tag/area indexes keep being refreshed in place (curated head preserved, list section regenerated) and committed as now.

### 2. A cheap, consistent agent query path

- Replace ad-hoc rg with a small `commonplace-*` command that prints a collection or tag slice as `title + description` lines (the same view mkdocs renders), so agents have one documented, scoped entry point instead of hand-rolling `rg "^tags:" ...` + `rg "^description:" ...`.
- Scoping is the default; an unscoped full-collection dump should be explicit/awkward, because that is the cost the retired complete index used to impose silently.
- This *codifies* the query that replaces the retired complete index.

### 3. Navigation policy

Ordinary discovery prefers, in order:

1. already-loaded context and user-named targets
2. curated focused indexes (tag / area) — read whole, since they are scoped and colocated
3. the scoped query command / `rg` over the destination collection
4. candidate body reads
5. no complete-`dir-index` step — it no longer exists in the repo; the mkdocs site serves humans

`cp-skill-write` is already off the complete index (rg duplicate check + in-hand links). `cp-skill-connect` stops reading complete destination `dir-index.md`; in standard mode it reads curated focused indexes where they exist, otherwise the scoped query / `rg`, and reserves broad scans for deep mode.

### 4. Keep curated indexes bounded (pressure)

Curated indexes keep their colocated lists, but a scoped list can still grow (a popular tag). Apply the weight-pressure idea **to curated indexes only**:

- index generation/validation reports per-index weight (bytes, entry count).
- validation warns past a soft threshold and fails past a hard one.
- an over-threshold curated index must be split, curated harder, or have its tag narrowed — because a curated index is a *read surface*, it must stay context-feasible.

The complete inventory is exempt: it is no longer an agent read surface, or even committed.

## Open decisions

1. mkdocs generation mechanism: a `commonplace-refresh-indexes --for-build` mode the mkdocs hook calls, or a dedicated mkdocs plugin?
2. The query command's shape and output: e.g. `commonplace-index notes --tag X` / `--match term`; emit exactly the old dir-index line format so mkdocs and agents share one renderer?
3. Soft/hard weight thresholds for curated indexes: bytes or entry count; global, collection-local, or per-index?
4. Do curated indexes need to *declare* focused-routing (cheap to read) vs archival, or is "curated = focused" sufficient?
5. Reference-sweep scope before removal: `CLAUDE.md` Key Indexes, `kb/reference/navigation.md`, `cp-skill-connect`, and any README / curated index that links to a `dir-index.md`.
6. ADR: this changes the generator/validator/navigation contract — almost certainly yes.

## Candidate implementation sequence

1. Decide the mkdocs generation mechanism and the query command shape.
2. Add the scoped query command (wraps rg, prints title + description).
3. Move complete-inventory generation into the mkdocs build; stop writing `dir-index.md` to the repo.
4. `git rm` + gitignore the `dir-index.md` files.
5. Update `navigation.md`, `cp-skill-connect`, `CLAUDE.md` Key Indexes, and any other references.
6. Add curated-index weight reporting + validation thresholds.
7. Promote the durable conclusion into reference docs and an ADR.

## Closure criteria

- Complete per-collection inventories are build-time (mkdocs) only — not committed, not in any agent read path.
- Curated tag/area indexes stay committed with their generated lists colocated, and have a weight-pressure mechanism.
- Agents have one cheap, scoped query path that replaces complete-index reads.
- `cp-skill-connect` has a standard discovery policy with no complete `dir-index.md` reads.
- References (navigation, `CLAUDE.md`, skills) are updated and the change is recorded in an ADR.

## Grounding

- [Navigation](../../reference/navigation.md) - grounds: current progressive-disclosure stack and future search-layer direction.
- [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) - target: current standard discovery path that makes full destination directory indexes mandatory.
- [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) - precedent: focused writing path already removed whole-dir-index reads for duplicate detection.
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) - motivation: the eval finding that complete dir-index reads dominate write/connect per-fork overhead.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - principle: compute scoped-to-need rather than committing a heavy denormalized surface.
- [Index curation adds orientation that generation cannot produce](../../notes/index-curation-adds-orientation-that-generation-cannot-produce.md) - rationale: curated indexes earn their committed place; complete inventories do not.
- [Two context boundaries govern collection operations](../../notes/two-context-boundaries-govern-collection-operations.md) - rationale: the title-plus-description boundary must stay context-feasible, which a scoped query gives and a complete index does not.
