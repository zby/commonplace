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

3. **Weight is a contract on the curated head, not a colocation dial.** *(Revised 2026-06-10; the original framing — small tags colocate their generated list, large ones detach it — is superseded: nothing generated is committed at any size.)* The committed curated head (`tag-readme`) is small by type contract (weight gates), and a head whose curated entries cover the tag's full membership may declare `complete: true` — legal only under the gates, enforced by validation.

4. **Uncurated slices — scoped `rg`/query.** Tags or slices that do not warrant a curated head are served by a scoped query (by tag, keyword, or area), not a standalone file.

Net: note files are the single source of truth; humans get full build-time listings (directory and tag); agents get curated heads plus scoped query. The pathological artifact is the *generated complete listing* at any scope — never curation, which may even be complete as a declared, enforced property under the weight gates.

## Design sketch

### 1. Generation of complete listings moves out of git

- `commonplace-refresh-indexes` stops writing per-collection `dir-index.md` to the repo; that generation moves into the mkdocs build (plugin or hook) so the published site still has browsable inventories.
- The per-tag `## Other tagged notes` generated tail gets the same treatment: not committed, injected at mkdocs build time for human readers.
- `git rm` the existing `dir-index.md` files and gitignore them; strip the committed generated tail from tag indexes.
- Curated heads stay committed: directory `README.md` / `COLLECTION.md`, and the tag's `<tag>-README.md`. Nothing generated is colocated; a small tag's README may instead declare enforced completeness (see §4).

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
2. curated tag READMEs — read whole, since they are small by type contract
3. scoped `rg` over the destination collection or tag (recipes in §2)
4. candidate body reads
5. no complete-`dir-index` step — it no longer exists in the repo; the mkdocs site serves humans

`cp-skill-write` is already off the complete index (rg duplicate check + in-hand links). `cp-skill-connect` stops reading complete destination `dir-index.md`; in standard mode it reads curated focused indexes where they exist, otherwise scoped `rg`, and reserves broad scans for deep mode.

### 4. Weight gates are the tag-readme type contract

*(Revised 2026-06-10: weight no longer governs colocation of a generated tail — nothing generated is committed; it is the contract that the tag's curated head stays a cheap read surface.)*

- validation reports per-README weight (bytes, with entry count as diagnosis).
- every `tag-readme` warns past the soft threshold and fails past the hard one — no exemptions.
- past threshold, the README must be curated harder, its tag split, or its tag narrowed; a `complete` mark must be dropped if full membership no longer fits under the gates.
- splits follow the split discipline (see Resolved 2026-06-10) so the tag structure stays visible.

Build-time artifacts (`dir-index` pages, generated tails) are exempt: they are not committed and not agent read surfaces at all.

## Resolved (2026-06-08)

- **The governing axis is curated-head vs generated-complete-list, not complete-vs-focused.** Curation is worth committing at every scope; the denormalized complete listing is context debt at every scope. This retired the earlier framing that only focused indexes earn curation.
- **The per-tag generated tail is treated exactly like `dir-index.md`** — retired from git, regenerated by mkdocs for human readers. The full listing stays valuable to humans; it is just no longer in the agent read path or the repo.
- **The tag index is the tag's README**: its editorial body is the committed curated head; its `## Other tagged notes` tail is the detachable generated list. This dissolves the same-file-vs-sibling question — nothing generated is committed either way.
- **The motivation is promoted to theory** in [design-for-the-first-time-human-except-on-access-cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md): the agent-as-first-time-human design heuristic holds on most affordances but breaks on access cost (sublinear human skim/search vs linear agent whole-context load). This workshop is its first instance.
- **No new query command — scoped `rg` is the agent path** (recipes in §2). rg recovers the operative part of the retired index (verified); codifying into a command is deferred until a recurring failure justifies it.
- **The decision is recorded in ADR 025** (`kb/reference/adr/025-complete-generated-indexes-are-build-time-only.md`), which supersedes ADR 003 (index-first connect discovery). What remains is implementation plus the deferred mechanism decisions below.

## Resolved (2026-06-10): split the index type into tag-README + completeness mark

The `index` type was doing two jobs: being an *index* (complete enumeration) and being an *introduction to a tag* (the old "area" role). The bundle was a working hack at small scale; growth forces the general design move of separating the contracts.

- **New committed type `tag-readme`, file `<tag>-README.md`** — the tag's curated head: narrative orientation plus selective editorial picks with context phrases. The README name mirrors the directory convention and is the one name a first-time reader already decodes as "curated landing, read first, not exhaustive" — the *curated head* concept now has one name at both scopes (directory → `README.md`, tag → `<tag>-README.md`). Rejected names: `guide` (prescriptive-register connotation), `area` (retired by ADR 004, partition baggage), `map` (the metaphor re-imports the completeness expectation), `tag-intro`/`topic-intro` (coins a term where README already carries the meaning).
- **No committed complete tag index exists.** The complete per-tag listing remains build-time only (the mkdocs tail appended to the tag-README page), exactly like `dir-index` — ADR 025 unchanged.
- **Completeness is a declared, enforced property, not a separate artifact.** A tag-README may set a frontmatter field (working name `complete: true`; absent = selective) claiming it links *every* note carrying the tag. Validation enforces the claim with the same membership query as the rg recipe — an unenforced claim would be worthless, since a careful agent would run the rg sweep anyway. When the mark is present, consumers like `cp-skill-connect` skip the by-tag rg call for that tag. On the published site, a complete README's generated tail is automatically empty (the tail already excludes curated links), so nothing special is needed at build time.
- **Directory READMEs stay free form.** They serve heterogeneous jobs (operator guide, survey landing, project framing) and `COLLECTION.md` already carries each collection's enforceable contract. Unification with tags happens at the name level (README = curated head), not the type level; type them only if a shared structure emerges.
- **Weight gates are the type contract (revises decision #3):** every `tag-readme` sits under the 8/16 KB gates, no exemptions — the contract is that the tag's curated head is *small*, a cheap read surface. The `complete` mark is therefore only legal while the tag's full membership fits under the gates: a growing tag drops the mark (readers fall back to the scoped rg) or splits. A complete README hitting the soft warn is the early signal that the tag is outgrowing completeness. `learning-theory-index` (18.8 KB) cannot declare complete; it trims to selective or splits the tag.
- **The hub** (`tags-index.md`) becomes `tags-README.md` under the same type, complete-marked over the set of tag-READMEs and enforced the same way (recommendation — confirm at migration; the schema must cover the hub's binding, today's `index_source: tag-indexes`, alongside the per-tag binding). The `index` type shrinks to the build-time virtual pages.
- **Forced splitting is kept as a tripwire, not a membership rule (arscontexta lesson).** The tag indexes descend from arscontexta-style areas: forced small (~40 notes) with *exclusive* membership — "tag the most precise area", no parent/child dual-tagging (see ADR 004's context). The useful half was the tripwire: growth forced an explicit editorial act instead of silent accretion. The harmful half was the membership rule: after a split, notes moved to the child tag vanished from the parent's surface while conceptually still belonging to it, and the parent/child structure itself lived nowhere readable — the hierarchy went invisible. The weight gates keep the tripwire (growth trips validation and forces a decision) with a wider remedies menu — trim, split, or narrow — because our heads are selective-by-default rather than forced-complete. **Split discipline:** refined case-by-case in [completeness-lifecycle.md](./completeness-lifecycle.md) — the consumer-by-consumer analysis of the `complete` mark's lifecycle (write-side obligation → growth → gate → exit), why drop-to-selective is the default exit and splitting is an editorial act rather than a completeness rescue, and why the forbidden middle — some child notes keep the parent tag, some don't — recreates arscontexta's invisible structure.

## Open decisions

1. ~~mkdocs generation mechanism~~ — **resolved: extend the existing mkdocs hook (`src/commonplace/docs/mkdocs_hooks.py`), not a new plugin or a `--for-build` CLI.** The hook already drives nav (`on_config`) and a per-page metadata badge (`on_page_markdown`), and CI already runs `commonplace-refresh-indexes` before `mkdocs build` — build-time generation already exists; ADR 025 only removes its *write to git*. Mechanism: inject the per-tag generated tail via `on_page_markdown` on tag-index pages (already identified by `index_source: tag` / `index_key`), and emit per-collection `dir-index` pages as virtual files via `on_files`, both reusing the in-memory `index_directory` / `index_generated` lib functions. `commonplace-refresh-indexes`'s repo-writing role and its CI step are dropped; the lib modules stay. A plugin adds packaging overhead and a second pattern; a `--for-build` CLI must still write somewhere, which is the committed-artifact problem being removed.
2. ~~The query command's shape and output~~ — **resolved: no command; scoped `rg` (ADR 025).**
3. ~~Soft/hard weight thresholds for curated indexes~~ — **resolved (2026-06-10): bytes, global, soft 8 KB warn / hard 16 KB fail, enforced on every `tag-readme`** — *the gates are the type contract: a tag's curated head is small, no exemptions; the `complete` mark is only legal while full membership fits under the gates (type split above).*
   - **Bytes, not entry count.** Bytes are the unit of context cost — the property the threshold protects — and the eval framework already prices everything in bytes (note ≈ 2 KB, skill body ≈ 8–12 KB, AGENTS.md ≈ 15–18 KB, fork budget ≈ 50 KB). Entry count is reported alongside as *diagnosis* (it discriminates "curate harder" from "split the tag") but does not gate: a 60-entry bare list can weigh less than a 20-entry essayish index, and it's the bytes that hurt.
   - **Calibration (measured 2026-06-10, post-tail-strip):** median curated tag index ≈ 3.5 KB; soft 8 KB ≈ one skill body — the point where a navigation aid costs as much as the procedure it serves (~25–30 entries with context phrases); hard 16 KB ≈ AGENTS.md — an index costing as much as the whole always-loaded control plane is indefensible as a routing aid. Today the soft gate flags exactly the two real outliers (`learning-theory` 18.8 KB / 55 entries, `computational-model` 10.5 KB / 35 entries) and the hard gate only `learning-theory` — which genuinely needs splitting.
   - **Global default, no override machinery.** Per YAGNI and the ADR 024 pattern: if a specific index ever earns an exception, key it explicitly on that index then; don't build the override map now.
   - **Scope: `tag-readme` artifacts.** Collection READMEs are also curated heads but serve as landing/contract pages loaded deliberately and stay free form (`kb/reference/README.md` is 14.9 KB and would warn); extending to them is cheap later if their weight starts hurting.
   - **Sequencing (ADR 024 blast-radius rule — audit before flipping):** land the soft warn first; the hard fail goes in only after `learning-theory-index.md` is trimmed or its tag split below the gate, otherwise validation is red on day one.
   - Remedies past threshold (unchanged from the design sketch): curate harder, split the tag, or narrow it.
4. ~~Declare focused-routing vs archival?~~ — **resolved (2026-06-10) by the type split above:** the declaration exists and is richer than the original question — `tag-readme` is the routing surface by type, and the `complete` mark declares the enumeration contract, machine-enforced.
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
6. Define the `tag-readme` type: type spec + schema (binding field for the tag key; optional `complete` and `covered_by: [children]` marks), and validation — weight gates on every instance (8 KB warn / 16 KB fail, bytes + entry count reported; the type contract is *small*), membership check when `complete: true`, coverage check + fan-out warn (~7 children) when `covered_by` (full rules in [completeness-lifecycle.md](./completeness-lifecycle.md)). The type spec is the **authoritative home** for the whole contract — including the `complete`/`covered_by` instructions — and is **maintenance-path only**: a tag-README is understood standalone (self-describing field names, ordinary curated body), so readers never load the spec; only maintenance work (declaring/dropping marks, fixing validator warnings, executing exits) reads it, routed there by the validator message. Skills and AGENTS.md point at it rather than duplicating. Note the new mechanism class: the membership/coverage checks are **cross-artifact** — a new note can invalidate a marked README while validating clean itself.
7. Migrate the 16 tag indexes + hub: re-type to `tag-readme`, rename `<tag>-index.md` → `<tag>-README.md` (and `tags-index.md` → `tags-README.md`) via `commonplace-relocate-note` for backlink rewrites + mkdocs redirects. **Review gate: present the full rename candidate list for approval before acting.**
8. Update the instruction surfaces (impact analysis 2026-06-10):
   - **`cp-skill-write` — deliberately unchanged** (decided 2026-06-10, reversing the first draft of this analysis). The main writing instructions do not carry tag discipline; write stays single-artifact and tags stay free at write time. Mark obligations are enforced reactively: the validator's membership/coverage checks fire when the marked README is validated (sweeps, fix runs), and **the warning/failure message must name the fixing instruction** (`maintain-curated-indexes` / the FIX-SYSTEM route) so the maintenance loop is self-routing. Cost accepted: the entry/phrase is written cold at fix time rather than hot at write time — eventual correctness over write-path complexity.
   - **`cp-skill-connect`** — skip the by-tag rg when the destination tag-README declares `complete: true` (record in trace); optionally recurse `covered_by`. Read-only contract unchanged.
   - **`AGENTS.md`** — carries the **read-side meaning of the marks** (decided 2026-06-10): `complete: true` → the README links every note carrying the tag, so the by-tag rg sweep is skippable; `covered_by: [children]` → every tagged note carries at least one listed child tag, so the typed routing is trustworthy; both validator-enforced. Plus the Key Indexes renames after migration. Maintenance of the marks stays separate — type spec only, routed to by validator messages. No procedure detail in AGENTS.md.
   - **`kb/notes/COLLECTION.md`** — types table gains `tag-readme`, `index` row shrinks; one line that tagging can carry obligations (pointer to type spec).
   - **`navigation.md`** — marks as navigation affordances (`complete` = README is the membership surface; `covered_by` = trustworthy typed routing); **`maintain-curated-indexes.md`** — gains the lifecycle procedure; **FIX-SYSTEM/validation docs** — three new warning classes (weight, fan-out, membership/coverage).
   - **`kb/types/note.md` — deliberately unchanged**: obligations attach to the tag-README, never the note type.
   - Re-key the mkdocs hook on the new type (tag badge links, tail injection, hub tail); `kb/types/index.md` shrinks to build-time virtual pages.
9. Record the type split + completeness mark in an ADR (extends, does not reopen, ADR 025).
10. ~~Promote the durable conclusions~~ — theory note and ADR 025 both done; reference-doc updates landed with step 5; the step-9 ADR covers the 2026-06-10 revision.

## Closure criteria

- Complete listings (per-collection inventory and per-tag tail) are build-time (mkdocs) only — not committed, not in any agent read path.
- Curated heads stay committed at every scope under one name: directory `README.md` (free form) and `<tag>-README.md` (`tag-readme` type, weight-gated — the contract is small; `complete: true` additionally passes the enforced membership check).
- Agents have one cheap, scoped query path that replaces complete-index reads — skippable per tag where a `complete: true` README already guarantees coverage.
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
