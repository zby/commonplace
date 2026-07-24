---
description: "Proposal: attach tag scope to membership claims (marks, sweep recipes) rather than to the tag string — options: formalized collection scope, repo scope, or a declared per-README dual scope"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, document-system]
---

# Tag scope is declared where membership claims are made

Tags today have no declared scope, and the system's consuming surfaces disagree about what scope they assume: the validator enforces the tag-README marks over one collection, one navigation recipe sweeps three collections, another sweeps one, and the reader-facing wording of the `complete` mark ("every note carrying the tag") names no scope at all. The disagreement is currently a live, validator-invisible falsehood: a note outside `kb/notes/` carries a covered tag with none of its declared children.

The reframing this proposal rests on: a bare tag string needs no scope. An `rg` sweep is always explicit about the paths it searches, so tagging a note commits to nothing scope-shaped. Scope becomes real only where a **membership claim** is made — a `complete` or `covered_by` mark, a documented sweep recipe, or a skip rule that lets a consumer trust a mark instead of sweeping. So the design question is not "what scope do tags have" but "what scope do membership claims declare and enforce, and how do readers learn it."

## Current state (as of 2026-07-24)

- **Enforcement is collection-scoped.** The validator's `complete`/`covered_by` checks build membership from a single-collection scan (`collect_collection_tag_index(collection_dir)` in `src/commonplace/lib/index_generated.py`, consumed by the `tag-readme` type rule in `validation.py`). A note in another collection can never satisfy or violate a mark as far as the validator sees.
- **Reader-facing surfaces disagree.** The `tag-readme` type spec and `navigation.md` state the `complete` claim without a scope qualifier ("links **every** note carrying the tag"); `AGENTS.md`'s by-tag recipe sweeps `kb/notes/ kb/reference/ kb/instructions/`; `navigation.md`'s canonical by-tag recipe sweeps `kb/notes/` only; the hub `tags-README.md` is the one surface that qualifies its own mark ("complete over the tag pages in this collection").
- **Tags already cross collections.** `kb-maintenance` has 19 members in `kb/notes/` and 14 in `kb/reference/`; `computational-model`, `tool-loop`, `foundations`, and others leak similarly into `kb/reference/` and `kb/agentic-systems/`. Conversely `trace-learning` (102 members) exists only in `kb/agent-memory-systems/` — a de facto collection-local tag vocabulary.
- **One repo-scope violation is live and invisible.** `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md` carries `learning-theory` but none of the six `covered_by` children declared by `kb/notes/learning-theory-README.md`. At collection scope the mark is true and validates clean; at the scope `AGENTS.md`'s recipe implies, the reader-facing coverage claim is false.
- **Tag-READMEs exist only in `kb/notes/`** (21 files including the hub). Marks currently declared: `complete` on the hub, `discovery-README.md`, and `artifact-analysis-README.md` (neither tag leaks outside `kb/notes/`, so their claims are true at either scope today); `covered_by` on `learning-theory-README.md`.
- **`cp-skill-connect` is already coherent under collection scope.** It prospects per destination collection and reads the destination's own `<tag>-README.md`, skipping the by-tag `rg` only for that destination when the mark is present.
- ADR 004 made tags freeform strings; ADR 026 made the marks enforced-or-omitted precisely because a claim that tells exhaustive consumers to stop looking must never be silently false — the property the current scope mismatch violates at repo scope.

## The design space

1. **Formalized collection scope.** A tag is `(collection, string)`; the same string in two collections is two tags. This hardens what the validator and `cp-skill-connect` already do. Changes are mostly prose: qualify the mark's meaning everywhere it is stated ("every note in this collection"), make `AGENTS.md`'s three-collection recipe either per-collection or explicitly a union of independent scoped sweeps, and let any collection grow its own tag-READMEs (`trace-learning` in `kb/agent-memory-systems/` is the first real candidate outside `kb/notes/`). Cross-collection topical routing remains the job of authored links and the hub's editorial prose. Cost: there is no single enforceable surface for "everything about kb-maintenance anywhere" — readers who want it must know to union sweeps, and no mark can ever license skipping that union.

2. **Repo scope.** One tag namespace; marks are checked over all collections; the by-tag recipe sweeps the whole `kb/`. The existing `learning-theory` violation immediately surfaces as a validator failure (correctly, under this reading). Costs: `kb/notes/` tag-READMEs become cross-collection artifacts whose entries must link into `kb/reference/` and beyond — a linking posture the collection contracts would have to authorize; external-coverage collections lose tagging autonomy (their local idioms like `trace-learning` join a namespace shared with theory tags, sharpening same-string-different-sense risk); every mark's blast radius grows with every new collection, so `complete` becomes harder to hold as the KB grows.

3. **Declared dual scope.** Scope is a frontmatter field on the tag-README — the one artifact that reifies a tag — defaulting to collection scope, with an explicit opt-in (working name `scope: kb`) that widens that README's mark checks and its readers' skip rights to the whole repo. This is the ADR 024/026 move again: the claim's parameters live on the artifact that makes the claim, so they cannot drift from it. Bare tags without READMEs need no scope at all. Consumers read one field to know what a mark licenses; the validator enforces exactly what is declared. Cost: a collision rule is needed (what happens when a kb-scoped `<t>-README.md` coexists with a collection-local `<t>-README.md` elsewhere — likely: a kb-scoped tag name is reserved repo-wide), and the recipes must actually consume the field or it decays into decoration.

Under every option, one piece of work is identical and can ship first: align the three disagreeing surfaces (type spec, `navigation.md`, `AGENTS.md`) on one stated scope, and either fix or honestly qualify the live `learning-theory` discrepancy. Option 3 then reduces to a small delta on option 1 — a declared escape hatch whose adoption can wait, per YAGNI, until a tag actually needs a repo-wide claim.

## Free choices

- **Default scope.** Collection scope is the code's current behavior and the cheaper claim to keep true; repo scope matches what `AGENTS.md`'s recipe has been implying to readers. The default decides which existing surfaces are "wrong."
- **Where a kb-scoped README lives** (option 3 only). In place in `kb/notes/` (where all tag-READMEs already are, but then a theoretical-profile collection hosts cross-collection routing artifacts), or a dedicated home outside any collection (mirroring `kb/types/` as a global surface).
- **Cross-collection children.** Whether a `covered_by` list on a kb-scoped README may name children whose own READMEs live in other collections, or children must share the parent's scope.
- **Collision policy.** Whether a kb-scoped tag name reserves the string repo-wide — which would ride the reserved-term registry proposed in [write-time vocabulary collision controls](./write-time-vocabulary-collision-controls.md) rather than needing its own mechanism.
- **Recipe frontloading.** Whether `AGENTS.md` carries one scoped recipe with prose explaining scope, or per-scope recipes; and whether `cp-skill-connect`'s skip rule needs any change (under options 1 and 3-default it needs none).

## Adoption criteria

- Every surface that states a mark's meaning names its scope, and the validator enforces exactly that scope — no reader can be licensed to skip a sweep wider than what is checked.
- The `AGENTS.md` and `navigation.md` by-tag recipes agree with each other and with the enforced semantics.
- The live `learning-theory` discrepancy is resolved (child tag added, `covered_by` list revised, or the claim explicitly scoped to `kb/notes/`).
- If dual scope ships: declaring `scope: kb` on one README changes only that README's checks and skip rights, with no migration cost to unscoped tags.

## Risks

- **Silently false marks are the failure mode being repaired — and the easiest to reintroduce.** Any partial fix that qualifies some surfaces but not others reproduces today's state: a mark that reads as global but checks locally tells exhaustive consumers to stop looking while members exist elsewhere.
- **Same string, different sense.** Collection-local namespaces make it legitimate for `agent-memory` in `kb/notes/` and `kb/agent-memory-systems/` to drift apart semantically; without at least the collision screen from the vocabulary-controls proposal, the drift is discovered by a confused reader.
- **Scope as decoration.** A declared scope field that recipes and skills do not consume is a derived claim nobody checks — worse than leaving scope implicit, for the same reason unenforced marks are banned.

---

Relevant Notes:

- [Stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: a mark whose enforced scope is narrower than its stated scope is a marked-but-incomplete head, the exact catastrophic state the marks exist to prevent
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: scope is a parameter of the derived claim, so it must be part of what the check enforces or the claim must not be made
- [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — rationale: collection-local tag namespaces legitimize same-string-different-sense drift, which is this invariant applied to tag strings
