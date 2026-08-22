---
description: "Draft ADR 068: COLLECTION.md states where types come from instead of listing them; an enumeration may return only as an enforced mark"
type: kb/reference/types/adr.md
tags: []
---

> **Draft.** Lives in `kb/work/type-reference-tidy-up/` until the steps in [plan.md](./plan.md) land, then moves to `kb/reference/adr/068-...`. The workshop borrows the reference ADR type as its prospective target contract; its location still makes this work in flight, not an accepted decision. Promotion changes `type:` to `../types/adr.md` and adds `status: accepted`.

# 068-Collection contracts stop enumerating available types

**Status:** draft — not an ADR of record until implementation and promotion
**Drafted:** 2026-08-22

## Context

Each type spec declares its own `name:` and `description:`. That is the ground truth, and 20 specs carried it when this workshop opened. Four further layers restated it by hand:

- `kb/reference/available-types.md` — a catalogue of all types
- `kb/types/README.md` — a catalogue of the global types
- a `## Types` table in 8 of the 10 `COLLECTION.md` files
- a `## Types` section in the three scaffold templates under `src/commonplace/_data/templates/`, which seeds the same table into every installed KB

Two of these had drifted by 2026-08-22. `available-types.md` omitted `article`, which three primary article artifacts used. `kb/reference/COLLECTION.md` omitted `type-spec`, which its two local type specs carried. The `user-instructions-COLLECTION.md` template offered `kb/types/skill.md`, a path that had not existed in this tree.

The exposition prerequisite retired `available-types.md` rather than repairing it. [`collections-and-types.md`](../../reference/collections-and-types.md) is now the single general current-state exposition: it explains how types are used, gives common examples, and points to the global and collection-local type directories without claiming an exhaustive list. It absorbed the path-resolution mechanics from the former `type-loading.md`. `kb/types/README.md` remains curated navigation for global contracts only.

Drift here is not cosmetic, because one copy is load-bearing for a procedure. `kb/instructions/cp-skill-write/SKILL.md` directs the writer to pick a type path listed in the target collection's `## Types` section and to stop if the requested shorthand is absent. `cp-skill-write-multistage` and `cp-skill-snapshot-web` read the same menu. So a stale table refuses legitimate shorthand writes: asking `cp-skill-write` for a `type-spec` under `kb/reference/` is declined today, though two such artifacts already sit there. Supplying the explicit type path bypasses the table.

Nothing in the runtime under `src/commonplace/` parses these tables. One documentation parity test checks the sources menu's snapshot pointer, but there is no general enforcement of menu contents. Most of the menu is therefore an unchecked constraint that agents obey — the configuration [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rules out, producing the failure [stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) names.

Type resolution itself does not depend on the tables. [`collections-and-types.md`](../../reference/collections-and-types.md) records that explicit resolution follows the stored path directly. Validation rejects missing type files, bare enum values, absolute paths, URLs, paths escaping `kb/`, and targets that are not type specs. The menu was not what prevented an invented type.

`kb/work/` exposes a legitimate case that an ordinary collection does not. It is a lifecycle staging layer for work aimed at any durable collection and for experiments on the contracts themselves. The agent-complexity workshop applied the real `kb/notes/types/structured-claim.md` contract to theorem sketches; the trial later demoted two sketches whose theorem/proof form did not fit the type while retaining two that did. This draft likewise uses the real reference ADR contract before promotion. Copying either type into `kb/work/types/` would not preserve the test: path-valued identity would make the copy a second type with an independently drifting contract.

The validator currently checks only referential validity. `validate_type_path()` requires the pointer to resolve to a Markdown path under `kb/`, and `resolve_type_definition()` verifies that the target is a type spec and loads its schema. Neither checks whether the referenced collection-local type belongs to the artifact's collection. The menu therefore acts as an incomplete agent-side substitute for an eligibility invariant that is deterministic from the two resolved paths.

## Decision

An ordinary collection's `COLLECTION.md` states **where types come from**, not which ones exist. After resolving the artifact's path-valued `type:` pointer, validation permits a type under `kb/types/` or under that collection's own `./types/` directory. A peer collection's local type fails.

The whole `kb/work/` subtree is the lifecycle-overlay exception: validation permits any path that resolves to a valid type spec. The exception is path-based and needs no copied type, workshop declaration, or special agent lookup. It does not change lifecycle: a draft ADR in `kb/work/` is still a draft, and decision status is added only on implementation and promotion.

Agents resolve types uniformly. Existing artifacts point directly to their type definitions. For a new write named by shorthand, a writer searches type-spec frontmatter, selects the intended path, opens that specification, writes the artifact, and runs validation. The validator—not an agent-side menu or a `kb/work/` branch in the skill—is authoritative for whether the resolved type may be used at that artifact path.

`kb/types/COLLECTION.md` already has the target shape and is unchanged by this ADR: it states that every artifact in the collection other than three named files is a type spec, rather than listing them.

Current-state type exposition has one general surface. `collections-and-types.md` explains usage, resolution, enforcement, common examples, and discovery through the live `types/` directories. It does not enumerate the shipped inventory. `kb/types/README.md` remains a curated landing for the global directory and explicitly does not claim completeness. The former `available-types.md` catalogue and separate `type-loading.md` page remain retired.

Three things follow:

1. The `## Types` enumeration is removed from the remaining `COLLECTION.md` files and from the scaffold templates. Ordinary collections state the global-plus-owned-local eligibility rule; `kb/work/` states its any-valid-type exception.
2. A row that carries a *placement restriction* rather than a menu entry is not deleted but moved to its type spec, where a clause binding a shape wherever it lives belongs under ADR 042's quantifier rule.
3. `cp-skill-write`, `cp-skill-write-multistage`, and `cp-skill-snapshot-web` stop treating a collection menu as authorization. They resolve and open type definitions uniformly, fail on an ambiguous shorthand or unresolved path, and validate the artifact after writing. There is no workshop-specific agent branch.
4. Deterministic validation rejects a resolved peer-local type outside `kb/work/`, while preserving global types, owned-local types, and any valid type pointer under `kb/work/`.
5. Documentation and navigation point to the general exposition or directly to the relevant live type directory, never to a hand-maintained complete inventory.

**Reopening clause.** This ADR removes a *hand-maintained* enumeration. It does not settle that a collection may never carry one. An enumeration may return if it is built the way the marks on `tag-readme` are built — recomputable from the type specs, validated by code, and therefore **enforced-or-omitted** rather than trusted (`kb/types/tag-readme.md`, ADR 026). A generated or validator-checked list is a different artifact from the prose table this ADR removes, and it is admissible on that basis. What is ruled out is the middle state: a copy that consumers treat as authoritative and nothing recomputes.

## Considered alternatives

**Fix the tables by hand and move on.** Cheapest immediately, and it restores correctness for a while. Rejected because it leaves the mechanism that produced the drift intact — four copies, one source, no check — so the same failure recurs on the next type addition. The `article` omission and the phantom `skill` entry are evidence that hand maintenance has already failed more than once without anyone noticing.

**Validate the tables rather than the path relation** — check that every used type appears in the owning collection's menu. This would make the existing enumeration an enforced mark. Rejected because eligibility is already derivable directly from the resolved artifact path and type-spec path, except for the single explicit `kb/work/` rule. Validating the table would preserve an unnecessary third input and make the validator parse a prose projection of a simpler path invariant.

**Generate the table into `COLLECTION.md` at build time.** Removes drift by construction and preserves the reading experience. Rejected for now because it makes a binding contract file partly generated, mixing an authored obligation with machine output in one artifact; the generated-listing pattern is better placed in a catalogue than inside the contract. This remains the most likely shape if the enumeration returns.

**Keep the menu as agent-side authorization.** Rejected because agents already receive exact path-valued pointers and can look up any type definition. Authorization is deterministic and belongs in validation; duplicating it in skill prose recreates the drift surface this decision removes.

**Copy prospective target types into `kb/work/types/`.** This would make every workshop type locally discoverable under the ordinary rule. Rejected because a copied type has a different path-valued identity, must duplicate or fork the source schema and prose contract, and no longer tests the contract the artifact is meant to satisfy after promotion. Repeating this for ADRs, structured claims, articles, and other target shapes would turn a lifecycle layer into a shadow type hierarchy.

**Forbid peer-local types in workshops.** This keeps one derivation rule everywhere. Rejected because it strips the workshop layer of a useful function: drafting and testing against the actual target contract before promotion. Implicit `text` remains the default for exploratory work, but it cannot reveal whether a mature draft fits a candidate schema and authoring contract.

**Teach the write skills a workshop-specific lookup rule.** This would preserve peer-local workshop types without changing validation. Rejected because lookup does not differ: the `type:` value identifies the same spec everywhere. Only eligibility differs, so branching in agent instructions would duplicate a rule the validator can decide from paths.

Free choice left open: whether the derivation rule is stated per collection or stated once and referenced. Stated per collection for now, since `COLLECTION.md` is meant to be readable standalone; a shared statement is worth revisiting if the sentence proves identical across all of them.

## Consequences

**Operativity path.** The validator is the binding consumer: after existing type resolution confirms a real spec, it compares the artifact path, owning collection root, and resolved type path; it rejects peer-local use except beneath `kb/work/`. The three writing skills consume only the simpler uniform lookup procedure and run validation after writing. Collection authors consume the rule through `COLLECTION.md` prose, with contract force under the collection-conformance pair (ADR 041). New installations receive the same rule through the scaffold templates that `commonplace-init` copies; this is also the channel that stops the phantom `skill` type from propagating further.

**Easier:**

- Adding a type requires editing its spec, not the spec plus up to four listings.
- A drifted menu can no longer refuse a legitimate write, which is the concrete failure that motivated this.
- Workshops can test or stage against the actual prospective target contract without creating a work-local fork.
- Peer-local type use outside the owning collection becomes a deterministic failure instead of an agent convention.
- Newly installed KBs start without a stale menu and without a type path that does not resolve.
- Collection contracts get shorter and carry only clauses that bind the subtree.

**Harder / accepted costs:**

- An agent choosing a type runs a search instead of reading a table. That is a small extra step on a path that already opens the spec to author correctly, but it is a real cost on every write.
- A previously accepted cross-collection local type outside `kb/work/` will begin failing validation and must move, change type, or establish that its containing directory should be a collection of its own.
- Readers no longer get one exhaustive prose table of shipped types. They get common examples in the general exposition, curated global navigation in `kb/types/README.md`, and the live global or collection-local directories when they need the complete answer.
- Any collection-specific restriction that lived only in a table row must be spotted and migrated during execution; missing one silently drops a constraint.
- The validator, three skills, three templates, and collection contracts change together, so the change lands as a coordinated edit rather than a single-file one, and the ordering matters — validator and consumers before menus.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: the rule that decides between removing the copy and enforcing it
- [LLM recompute cost inverts the store-vs-recompute default](../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — rests-on: why a validated cache is ever worth its cost, and why this one is not yet
- [Stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) — evidenced-by: the failure mode the `## Types` gate reproduces on the write path
