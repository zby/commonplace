---
description: Splits the index type into a committed tag-readme type (file <tag>-README.md) whose weight gates (8KB warn/16KB fail, bytes, global) are the type contract, with an enforced complete mark (membership check) and a designed covered_by coverage mark; enforcement is reactive via the validator and the knowledge splits meaning to AGENTS.md, mechanics to the validator, maintenance to the type spec.
type: ../types/adr.md
tags: []
status: accepted
---

# 026-Split index into a committed tag-readme type with enforced marks

**Status:** accepted
**Date:** 2026-06-10

## Context

ADR 025 moved complete generated listings (`dir-index.md` pages and per-tag `## Other tagged notes` tails) to build-time-only, keeping curated heads committed for agents. That left the `index` type doing two jobs at once: being an *index* (complete enumeration) and being an *introduction to a tag* (the retired "area" role from ADR 004). The bundle worked at small scale; collection growth forces the general design move of separating the two contracts.

ADR 025 deferred two mechanism decisions this ADR settles: curated-index weight thresholds, and whether curated indexes must declare focused-routing vs archival. ADR 025's decision point 5 — colocation is conditional on weight (a small tag keeps its short generated list colocated, a popular tag detaches it) — is also now obsolete: under 025 *nothing generated is committed at any size*, so there is no colocation dial left to turn. Weight must become a contract on the curated head itself, not a placement decision about a generated tail.

Three further pressures shape the design:
- A `complete` enumeration claim is worthless unless machine-enforced — a careful agent would re-run the by-tag `rg` sweep anyway, so an unenforced claim saves no work. This is the [stale-indexes problem](../../notes/stale-indexes-are-worse-than-no-indexes.md) in its sharpest form: a marked-but-incomplete head tells exhaustive consumers to stop looking while members are missing.
- The arscontexta-style areas this descends from (ADR 004's context) carried a useful tripwire — growth forced an explicit editorial act — but a harmful membership rule: after a split, notes moved to a child tag vanished from the parent's surface while still conceptually belonging, and the parent/child structure lived nowhere readable. The hierarchy went invisible.
- Tags are flat strings today; nothing symbolic connects a tag to another tag, so a "the children cover this tag" routing claim can only live as prose that validation cannot consume and that decays silently.

## Decision

Split the `index` type into a committed `tag-readme` type plus two declared, validator-enforced marks. The `index` type shrinks to the build-time virtual pages.

1. **New committed type `tag-readme`, file `<tag>-README.md`** — the tag's curated head: narrative orientation plus selective editorial picks with context phrases. The README name unifies the *curated head* concept at one name across both scopes (directory → `README.md`, tag → `<tag>-README.md`); it is the one name a first-time reader already decodes as "curated landing, read first, not exhaustive." Rejected names: `guide` (prescriptive connotation), `area` (ADR 004 partition baggage), `map` (re-imports completeness), `tag-intro`/`topic-intro` (coins a term README already covers). No committed complete tag index exists — the complete per-tag listing stays build-time only (the mkdocs tail), ADR 025 unchanged.

2. **Weight gates are the type contract — they revise ADR 025's decision point 5.** Every `tag-readme` is gated at soft 8 KB warn / hard 16 KB fail, measured in **bytes** (the unit of context cost; entry count is reported alongside as diagnosis but does not gate), **global** with no override machinery (per YAGNI and ADR 024's pattern — key an exception explicitly if one is ever earned), and **no exemptions**. The contract is that a tag's curated head is *small* — a cheap read surface. Build-time artifacts (`dir-index` pages, generated tails) are exempt because they are not committed and not agent read surfaces at all. Remedies past threshold: curate harder, split the tag, or narrow it.

3. **`complete: true` — an enforced membership mark.** A `tag-readme` may declare that it links *every* note carrying the tag. Validation enforces the claim with the same membership query as the rg recipe. The mark is legal **only while full membership fits under the weight gates** — a growing tag drops the mark (readers fall back to the scoped rg) or splits; a complete README hitting the soft warn is the early signal that the tag is outgrowing completeness (`learning-theory`, 18.8 KB / 55 entries, cannot declare complete). The mark is an **accelerator, never a load-bearing wall**: no consumer's correctness may depend on it, because scoped `rg` always recovers full membership at the cost of one tool call. When present, exhaustive consumers like `cp-skill-connect` skip the by-tag rg for that tag; readers may always re-derive membership without it.

4. **`covered_by: [children]` — a designed coverage mark, adoption deferred to the first real case.** A grown tag can make a different enforceable claim than `complete`: not "every member is linked here" but "every member carries at least one of these child tags," checked as membership(T) ⊆ ∪ membership(child_i). The mark *is* the machine-readable children list — `covered_by: [child-a, child-b]` in the parent's frontmatter carries both the claim and its parameters so they cannot drift (the ADR 024 move: the contract lives on the artifact that makes it). This is the **only symbolic tag-to-tag relation** the system introduces; "Related Tags" prose stays editorial and no general tag ontology is added. The child-side `parents:` alternative was rejected (the coverage claim is the parent's contract; a child can serve several parents; a derived child set can change a parent's meaning without editing it). Unlike `complete`, `covered_by` is weight-immune (it links a handful of children, not every member) and survives growth. Validation warns past a soft fan-out of ~7 children (count, not bytes — routing value needs the alternatives held in mind at once); no hard fail, because the remedy is recursive and editorial (group children under intermediate tags). Adoption is deferred until a real tag exercises it; the natural first candidate is `learning-theory` when its README migrates. The *unenforced* prose version of the claim must never be written — that is the routing-level stale-index failure.

5. **Enforcement is reactive via the validator; the write path carries no tag discipline.** `cp-skill-write` stays single-artifact and tags stay free at write time. The membership/coverage checks are a new **cross-artifact** mechanism class — a new note can invalidate a marked README while validating clean itself — and fire when the marked README is next validated (sweeps, fix runs). The validator's warning/failure message **names the fixing instruction** ([maintain-curated-indexes](../../instructions/maintain-curated-indexes.md) / the FIX-SYSTEM route) so the maintenance loop is self-routing. Accepted cost: the entry and phrase are written cold at fix time rather than hot at write time — eventual correctness over write-path complexity.

6. **Knowledge split: meaning → AGENTS.md, mechanics → validator, maintenance → type spec.** The type spec is the authoritative home for the whole contract (gates, checks, exits, when to declare or drop a mark) and is **maintenance-path only**: a `tag-readme` is understood standalone (self-describing field names, ordinary curated body), so readers never load the spec — only maintenance work does, routed there by the validator message. The marks' read-side *meaning* is frontloaded into AGENTS.md in two sentences (`complete: true` → the README is the membership surface, the rg sweep is skippable; `covered_by: [children]` → the typed routing is trustworthy; both validator-enforced), because that operative consequence is not fully inferable from the field names. This constrains future field naming: a mark whose name needs the spec to decode would put the spec back on every reader's path.

7. **Directory READMEs stay free form, and the hub becomes `tags-README.md`.** Directory READMEs serve heterogeneous jobs (operator guide, survey landing, project framing) and `COLLECTION.md` already carries each collection's enforceable contract — unification with tags happens at the *name* level, not the type level. The navigation hub (`tags-index.md`) becomes `tags-README.md` under the `tag-readme` type, complete-marked over the set of tag-READMEs and enforced the same way (the schema must cover the hub's binding alongside the per-tag binding). The `index` type shrinks to the build-time virtual pages.

This **extends ADR 025** (the build-time-only direction is unchanged) and **refines its decision point 5**: colocation-by-weight is replaced — nothing generated is committed at any size, so weight is a contract on the committed curated head instead.

## Consequences

Easier:
- A tag's curated head is bounded by type contract, so it stays a cheap whole-read surface as the collection grows; `cp-skill-connect` skips the by-tag rg where a `complete` README guarantees coverage.
- Completeness and coverage become checkable properties rather than trust: the validator queues the gap, so curation debt becomes a validator-visible, self-routing maintenance queue without touching the write path.
- `covered_by` makes the parent/child tag structure machine-readable and enforced, fixing arscontexta's invisible-hierarchy failure while keeping the growth tripwire.

Harder / migration:
- Define the `tag-readme` type spec + schema (binding field for the tag key; optional `complete` and `covered_by`), with three new validator checks: weight gates on every instance, membership check when `complete: true`, coverage check + fan-out warn when `covered_by`.
- Migrate the 16 tag indexes + hub: re-type, rename `<tag>-index.md` → `<tag>-README.md` and `tags-index.md` → `tags-README.md` via `commonplace-relocate-note` (backlink rewrites + mkdocs redirects), behind a rename-list review gate.
- Update instruction surfaces: `cp-skill-connect` (skip rg on `complete`, optionally recurse `covered_by`), AGENTS.md (mark meanings + Key Indexes renames), `kb/notes/COLLECTION.md` (types table), `navigation.md`, `maintain-curated-indexes.md` (lifecycle procedure), FIX-SYSTEM/validation docs (three new warning classes). `cp-skill-write` and `kb/types/note.md` are deliberately unchanged.
- `learning-theory-index` must trim to selective or split before it can migrate cleanly; the hard fail lands only after it is under the gate (ADR 024 blast-radius / audit-before-flipping).

Risks / watch:
- A `complete` README inevitably grows into the gate and must drop the mark; the design makes the drop *cheap* (default exit: drop to selective, fall back to rg) rather than preventing it. Splitting is an editorial act justified by real substructure, never a completeness rescue.
- The forbidden state is partial migration — some child-tagged notes keep the parent tag and some don't — which makes the parent neither complete nor honestly selective and re-hides the structure (the arscontexta failure). Children must keep the parent tag (tags overlap, ADR 004).
- The `covered_by` catch-all-child smell (`T-misc`) makes coverage trivially satisfiable while destroying routing value; watch for it when the mark is first adopted.

## Links

- [025-complete-generated-indexes-are-build-time-only](./025-complete-generated-indexes-are-build-time-only.md) — part-of: extends 025 and refines its decision point 5 (colocation-by-weight is replaced — nothing generated is committed at any size)
- [004-replace-areas-with-tags](./004-replace-areas-with-tags.md) — part-of: `covered_by` keeps the area tripwire while fixing the invisible-hierarchy failure, and children keep the parent tag because tags overlap per 004
- [024-schema-severity-is-per-constraint-fail-by-default](./024-schema-severity-is-per-constraint-fail-by-default.md) — part-of: the global-no-override gate and audit-before-flipping sequencing follow 024's pattern
- [stale-indexes-are-worse-than-no-indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the marked-but-incomplete head is the catastrophic state, which is why the marks must be machine-enforced or not exist
- [design-for-the-first-time-human-except-on-access-cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md) — rationale: the access-mode asymmetry that keeps complete listings build-time-only while curated heads stay committed
- [index-curation-adds-orientation-that-generation-cannot-produce](../../notes/index-curation-adds-orientation-that-generation-cannot-produce.md) — rationale: the groupings and phrases are the durable value that survives a mark's drop
- [frontloading-spares-execution-context](../../notes/frontloading-spares-execution-context.md) — rationale: frontloading the marks' read-side meaning into AGENTS.md delivers it at zero extra reads
- [feasibility-is-the-heaviest-forks-net-load](../../notes/feasibility-is-the-heaviest-forks-net-load.md) — rationale: connect is the exhaustive consumer whose per-destination cost the weight gates bound
- [maintain-curated-indexes](../../instructions/maintain-curated-indexes.md) — procedure: the maintenance loop the validator messages route to for declaring/dropping marks and executing exits
- [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) — procedure: the exhaustive consumer that skips the by-tag rg when a destination README declares `complete: true`
