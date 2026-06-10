# Workshop: Index weight and navigation policy

## Goal

Make Commonplace robust for **large collections**. Most of the framework was shaped when collections were small enough that generated artifacts were cheap to load. As a KB grows, those artifacts — especially complete inventories like `dir-index.md` — turn into context debt: an operation's per-fork load grows with total collection size rather than with the work at hand, until ordinary operations stop being feasible (see the eval finding in grounding). The system should scale so that the cost of a write, an ingest, or a connect depends on the *task*, not on how many notes already exist. This workshop is the navigation-and-index-weight slice of that goal; index policy is the first place collection growth bites.

## Question

How should Commonplace use generated indexes once full collection indexes become too heavy to load as ordinary agent context?

The immediate pressure is `dir-index.md`: it is valuable as a complete, committed inventory, but full reads of large collection indexes now cost tens of KB before the agent has selected any candidate body. This is especially painful in `cp-skill-connect`, where every authorised destination can trigger a full index read. The broader question is how to keep generated navigation surfaces useful without letting them become hidden context debt.

## Motivation: agents and humans read the same index at different costs

This is a deliberate **divergence**, and a rare one. Normally a Commonplace artifact serves agents and humans from one committed source, and that single-source property is worth protecting. The complete index is the case where it pays to split — and the reason is an asymmetry in *access mode*, not in the artifact itself.

An agent that reads an index reads it **whole**: the entire file lands in context and every byte counts against the bounded budget, whether or not any given line is relevant. Cost is **linear** in the size of the index. A human "reading" the same index on the published site does **not** consume it whole — they skim, scroll, and Ctrl-F to the few lines they want. Cost is **sublinear**; the unread bulk is free. The same complete listing is context debt for the agent and a convenience for the human.

The fix is to give each reader an access mode that is sublinear in the slice they actually need:

- **Humans** get the full listing rendered by mkdocs, where browser scroll and find already provide skim/search access.
- **Agents** get scoped `rg`/query, which restores the *same* sublinear access — it returns only matching lines, never the whole inventory.

The pathological combination is the one we have today: a committed complete index forces *whole-document linear load* on the agent, the one consumer for whom that is most expensive. The divider is access mode, not literally human-vs-agent — an agent handed a query tool reads sublinearly too, and a human handed only a raw file would skim it the same way. Keeping the note files as the single source of truth is what makes the divergence safe: only the *materialization* splits (committed curated heads + scoped query for agents; build-time full pages for humans), never the underlying truth.

This generalizes past indexes, which is why it belongs in methodology, not just here: any large generated read surface should be sized against the consumer's access mode, and serving the same content through two materializations is justified whenever two consumers have divergent access patterns over one source of truth.

## Current hypothesis (revised 2026-06-08)

The axis is **curated head vs generated complete list**, not complete-vs-focused. Curation is valuable at every scope; the denormalized complete listing is context debt at every scope. So split every navigation surface into the two — keep the curated head committed for agents, and serve the generated complete list to humans at mkdocs build time.

1. **Generated complete listings — retire from git, build at mkdocs time.** This covers both the per-collection `dir-index.md` *and* the per-tag `## Other tagged notes` generated tail. Both are pure denormalization: every title and description already lives in the note's own frontmatter, so they give an agent nothing the source files don't, while costing tens of KB on every read (the connect/write overhead the eval flagged — see grounding). They remain useful to *human* readers, so generate them at **mkdocs build time** for the published site and stop committing them. Agents reconstruct what they need with `ls` and scoped `rg`, which is cheaper because it returns only matches.

2. **Curated heads — keep committed, at every scope.** A directory's curated head is its `README.md` / `COLLECTION.md`; a tag's curated head is the editorial body of its tag index (intro + hand-grouped sections). These carry orientation generation cannot produce, and they survive once the generated tail is detached. Retiring `dir-index.md` loses no curation precisely because a directory's curation already lives in a separate file (README); the same move applied to tags means detaching the tag index's generated tail so the curated body stands alone — the tag index *is* the tag's README.

3. **Colocation is conditional on weight.** For a small tag, keeping the short generated list colocated under the curated head is the ergonomic win (orientation next to its entries). For a popular tag, the generated tail is exactly the context debt this workshop targets — so past a weight threshold the tail is detached to build-time/query (see weight pressure below). Small: colocate; large: detach.

4. **Uncurated slices — scoped `rg`/query.** Tags or slices that do not warrant a curated head are served by a scoped query (by tag, keyword, or area), not a standalone file.

Net: note files are the single source of truth; humans get full build-time listings (directory and tag); agents get curated heads plus scoped query. The pathological artifact is the *generated complete listing* at any scope — not curation, and not generated lists while they stay small and colocated.

## Design sketch

### 1. Generation of complete listings moves out of git

- `commonplace-refresh-indexes` stops writing per-collection `dir-index.md` to the repo; that generation moves into the mkdocs build (plugin or hook) so the published site still has browsable inventories.
- The per-tag `## Other tagged notes` generated tail gets the same treatment: not committed, injected at mkdocs build time for human readers.
- `git rm` the existing `dir-index.md` files and gitignore them; strip the committed generated tail from tag indexes.
- Curated heads stay committed: directory `README.md` / `COLLECTION.md`, and the editorial body of each tag index. A small tag may keep a short colocated list; a large one detaches it (see weight pressure).

### 2. The agent query path: scoped `rg`, no new command

Agents discover via curated heads plus scoped `rg`; **no `commonplace-*` query command is added** — rg recovers the operative part of the retired index (verified against the repo). Documented recipes:

- **By tag** — path + description for every note carrying a tag:
  ```bash
  rg -l '^tags:.*\bTAG\b' kb/notes/ --glob '*.md' \
    | xargs -r rg -N --no-heading '^description:\s*' -r ''
  ```
  The `xargs -r` guard matters: a tag matching zero files would otherwise make `rg` run with no path and search the whole repo.
- **By keyword/description** — `rg '^description:' <scoped path>`.

rg returns `path + description`, not the human H1 title; the path stands in for the title in triage. Codifying these into a command is deferred until a recurring failure justifies it (the empty-match footgun biting in practice, or title-in-output proving necessary) — per `progressive-constraining`, codify after the pattern proves the need. Recorded in ADR 025.

### 3. Navigation policy

Ordinary discovery prefers, in order:

1. already-loaded context and user-named targets
2. curated focused indexes (tag / area) — read whole, since they are scoped and colocated
3. scoped `rg` over the destination collection or tag (recipes in §2)
4. candidate body reads
5. no complete-`dir-index` step — it no longer exists in the repo; the mkdocs site serves humans

`cp-skill-write` is already off the complete index (rg duplicate check + in-hand links). `cp-skill-connect` stops reading complete destination `dir-index.md`; in standard mode it reads curated focused indexes where they exist, otherwise scoped `rg`, and reserves broad scans for deep mode.

### 4. Weight pressure decides colocation

The colocation decision (point 3) is governed by a weight threshold on the curated index as an agent read surface:

- index generation/validation reports per-index weight (bytes, entry count).
- validation warns past a soft threshold and fails past a hard one.
- past threshold, the index must detach its generated tail (to build-time/query), be curated harder, or have its tag narrowed — because a curated index is a *read surface*, it must stay context-feasible.

The complete `dir-index` is exempt: it is no longer committed or an agent read surface at all.

## Resolved (2026-06-08)

- **The governing axis is curated-head vs generated-complete-list, not complete-vs-focused.** Curation is worth committing at every scope; the denormalized complete listing is context debt at every scope. This retired the earlier framing that only focused indexes earn curation.
- **The per-tag generated tail is treated exactly like `dir-index.md`** — retired from git, regenerated by mkdocs for human readers. The full listing stays valuable to humans; it is just no longer in the agent read path or the repo.
- **The tag index is the tag's README**: its editorial body is the committed curated head; its `## Other tagged notes` tail is the detachable generated list. This dissolves the same-file-vs-sibling question — nothing generated is committed either way.
- **The motivation is promoted to theory** in [design-for-the-first-time-human-except-on-access-cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md): the agent-as-first-time-human design heuristic holds on most affordances but breaks on access cost (sublinear human skim/search vs linear agent whole-context load). This workshop is its first instance.
- **No new query command — scoped `rg` is the agent path** (recipes in §2). rg recovers the operative part of the retired index (verified); codifying into a command is deferred until a recurring failure justifies it.
- **The decision is recorded in ADR 025** (`kb/reference/adr/025-complete-generated-indexes-are-build-time-only.md`), which supersedes ADR 003 (index-first connect discovery). What remains is implementation plus the deferred mechanism decisions below.

## Open decisions

1. ~~mkdocs generation mechanism~~ — **resolved: extend the existing mkdocs hook (`src/commonplace/docs/mkdocs_hooks.py`), not a new plugin or a `--for-build` CLI.** The hook already drives nav (`on_config`) and a per-page metadata badge (`on_page_markdown`), and CI already runs `commonplace-refresh-indexes` before `mkdocs build` — build-time generation already exists; ADR 025 only removes its *write to git*. Mechanism: inject the per-tag generated tail via `on_page_markdown` on tag-index pages (already identified by `index_source: tag` / `index_key`), and emit per-collection `dir-index` pages as virtual files via `on_files`, both reusing the in-memory `index_directory` / `index_generated` lib functions. `commonplace-refresh-indexes`'s repo-writing role and its CI step are dropped; the lib modules stay. A plugin adds packaging overhead and a second pattern; a `--for-build` CLI must still write somewhere, which is the committed-artifact problem being removed.
2. ~~The query command's shape and output~~ — **resolved: no command; scoped `rg` (ADR 025).**
3. Soft/hard weight thresholds for curated indexes: bytes or entry count; global, collection-local, or per-index?
4. Do curated indexes need to *declare* focused-routing (cheap to read) vs archival, or is "curated = focused" sufficient?
5. ~~Reference-sweep scope before removal~~ — **resolved: enumerated (2026-06-09) by `rg -l 'dir-index'` over the repo.** The live surface to update:
   - **Primary (named in step 5):** `CLAUDE.md`/`AGENTS.md` Key Indexes, `kb/reference/navigation.md`, `cp-skill-connect/SKILL.md`.
   - **Other live docs:** `kb/index.md`; the READMEs of `kb/notes/`, `kb/instructions/`, `kb/sources/`, `kb/reference/`, `kb/agent-memory-systems/`; `cp-skill-write/SKILL.md`; `evaluate-scenarios/SKILL.md`; `re-ingest.md`; `evaluate-log-entry-for-note-creation.md`; `kb/reference/collections-and-types.md`; `kb/reference/storage-architecture.md`; `kb/types/index.md` (the index type spec describes the generated tail); notes `a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` and `symbolic-context-engineering-is-bounded-by-symbol-availability.md`; `kb/agent-memory-systems/review-framework-design.md`.
   - **Code:** `generate_notes_index.py` (standalone CLI that only writes dir-index — retire); `index_directory._best_landing` (parent→child `dir-index.md` nav links — logic moves into the mkdocs hook, since the virtual pages still need it); `promotion.py` (exclusion filters only — leave as-is).
   - **Leave untouched:** historical artifacts under `kb/reports/**`, old connect reports, ADR 003 (already marked superseded), and other workshops' in-flight docs.
   - **Scale check:** 67 committed `dir-index.md` files; 17 tag indexes in `kb/notes/` carry an `## Other tagged notes` tail to strip (check each against its curated body so nothing editorial is cut).
6. ~~ADR~~ — **done: ADR 025 (supersedes 003).**

## Candidate implementation sequence

1. ~~Decide the mkdocs generation mechanism~~ — **done: extend `mkdocs_hooks.py` (decision #1).**
2. ~~Document the scoped `rg` recipes (§2) in `navigation.md`~~ — **done (2026-06-09):** recipes plus the build-time-only policy live in `kb/reference/navigation.md`.
3. ~~Move complete-listing generation into the mkdocs build~~ — **done (2026-06-09):** `mkdocs_hooks.py` emits `dir-index` pages as virtual files (`on_files`) and appends tag tails (`on_page_markdown`) via in-memory `index_directory.collect_index_pages` / `index_generated.generated_section_for_index`; collection READMEs get a build-time "Complete file listing" link. The repo-writing CLIs (`commonplace-refresh-indexes`, `commonplace-sync-generated-index`, `commonplace-generate-notes-index`) and the CI refresh step are retired.
4. ~~`git rm` + gitignore + strip tails~~ — **done (2026-06-09):** 67 `dir-index.md` files removed and gitignored; 16 tag indexes stripped to their curated bodies.
5. ~~Update references per the enumerated sweep list (decision #5)~~ — **done (2026-06-09):** primary docs, live docs, code consumers, plus `test/scenarios/` cost tables and the connect-report trace template.
6. Add curated-index weight reporting + validation thresholds.
7. ~~Promote the durable conclusions~~ — theory note and ADR 025 both done; reference-doc updates landed with step 5.

## Closure criteria

- Complete listings (per-collection inventory and per-tag tail) are build-time (mkdocs) only — not committed, not in any agent read path.
- Curated heads stay committed at every scope (directory READMEs, tag-index editorial bodies); their generated lists are colocated only while small, detached past the weight threshold.
- Agents have one cheap, scoped query path that replaces complete-index reads.
- `cp-skill-connect` has a standard discovery policy with no complete `dir-index.md` reads.
- The access-mode asymmetry is promoted to a methodology note; the contract change is recorded in an ADR, and references (navigation, `CLAUDE.md`, skills) are updated.

## Grounding

- [Navigation](../../reference/navigation.md) - grounds: current progressive-disclosure stack and future search-layer direction.
- [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) - target: current standard discovery path that makes full destination directory indexes mandatory.
- [cp-skill-write](../../instructions/cp-skill-write/SKILL.md) - precedent: focused writing path already removed whole-dir-index reads for duplicate detection.
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) - motivation: the eval finding that complete dir-index reads dominate write/connect per-fork overhead.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - principle: compute scoped-to-need rather than committing a heavy denormalized surface.
- [Index curation adds orientation that generation cannot produce](../../notes/index-curation-adds-orientation-that-generation-cannot-produce.md) - rationale: curated indexes earn their committed place; complete inventories do not.
- [Two context boundaries govern collection operations](../../notes/two-context-boundaries-govern-collection-operations.md) - rationale: the title-plus-description boundary must stay context-feasible, which a scoped query gives and a complete index does not.
