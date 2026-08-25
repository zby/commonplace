---
description: "Accepted decision that COLLECTION.md states type eligibility instead of listing types, with kb/work allowed to use any valid type contract"
type: ../types/adr.md
tags: []
status: accepted
---

# 068-Collection contracts stop enumerating available types

**Status:** accepted
**Date:** 2026-08-22

## Context

Each type spec declares its own `name:` and `description:`; that is the ground truth. Four further layers restated it by hand: a catalogue of all types, a catalogue of the global types, a `## Types` table in most `COLLECTION.md` files, and the same table seeded by the scaffold templates into every installed KB. These copies drifted: the catalogue omitted `article` while article artifacts used it, a collection contract omitted `type-spec` while its own local type specs carried it, and a scaffold template offered a `skill` type path that did not exist.

Drift here was not cosmetic, because one copy was load-bearing for a procedure. `kb/instructions/cp-skill-write/SKILL.md` directed the writer to pick a type path listed in the target collection's `## Types` section and to stop if the requested shorthand was absent. `cp-skill-write-multistage` and `cp-skill-snapshot-web` read the same menu. So a stale table refused legitimate shorthand writes: asking `cp-skill-write` for a `type-spec` under `kb/reference/` was declined, though two such artifacts already sat there. Supplying the explicit type path bypassed the table.

Nothing in the runtime parsed these tables and nothing enforced their contents. The menu was therefore an unchecked constraint that agents obeyed — the configuration [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rules out, producing the failure [stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) names.

Type resolution itself does not depend on the tables. [`collections-and-types.md`](../collections-and-types.md) records that explicit resolution follows the stored path directly. Validation rejects missing type files, bare enum values, absolute paths, URLs, paths escaping `kb/`, and targets that are not type specs. The menu was not what prevented an invented type.

`kb/work/` exposes a legitimate case that an ordinary collection does not. It is a lifecycle staging layer for work aimed at any durable collection and for experiments on the contracts themselves, and a workshop draft is usefully validated against its real target contract before promotion (a structured-claim trial and this ADR's own draft did so). Copying the target type into `kb/work/types/` would not preserve the test: path-valued identity would make the copy a second type with an independently drifting contract.

The validator checked only referential validity — that the pointer resolves to a type spec under `kb/` — not whether a collection-local type belonged to the artifact's collection. The menu therefore acted as an incomplete agent-side substitute for an eligibility invariant that is deterministic from the two resolved paths.

## Decision

An ordinary collection's `COLLECTION.md` states **where types come from**, not which ones exist. After resolving the artifact's path-valued `type:` pointer, validation permits a type under `kb/types/` or under that collection's own `./types/` directory. A peer collection's local type fails.

The whole `kb/work/` subtree is the lifecycle-overlay exception: validation permits any path that resolves to a valid type spec. The exception is path-based and needs no copied type, workshop declaration, or special agent lookup. It does not change lifecycle: a draft ADR in `kb/work/` is still a draft, and decision status is added only on implementation and promotion.

Agents resolve types uniformly. Existing artifacts point directly to their type definitions. For a new write, a user or workflow may supply the exact type path; a shorthand requires one exact `name:` match in type-spec frontmatter; and a general write with no supplied type defaults to `kb/types/note.md`. A workflow that requires another type supplies its exact path. The writer opens the chosen specification, writes the artifact, and runs validation. The validator—not an agent-side menu or a `kb/work/` branch in the skill—is authoritative for whether the resolved type may be used at that artifact path.

Current-state type exposition has one general surface. `collections-and-types.md` explains usage, resolution, enforcement, common examples, and discovery through the live `types/` directories. It does not enumerate the shipped inventory. `kb/types/README.md` remains a curated landing for the global directory and explicitly does not claim completeness. This narrows [ADR 018](./018-types-are-path-references-to-instruction-docs.md)'s earlier allowance for per-collection discovery lists and supersedes the type-offerings placeholder in [ADR 021](./021-ship-library-content-under-kb-commonplace.md)'s collection scaffolds.

Type-wide restrictions remain owned by their type specs; collection-local placement policy remains ordinary collection prose.

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

**Operativity path.** The validator is the binding consumer: after existing type resolution confirms a real spec, it compares the artifact path, owning collection root, and resolved type path; it rejects peer-local use except beneath `kb/work/`. The three writing skills consume only the simpler uniform lookup procedure and run validation after writing. Collection authors consume the rule through `COLLECTION.md` prose, with contract force under the collection-conformance pair (ADR 041). New installations receive the same rule through the scaffold templates that `commonplace-init` copies.

**Easier:**

- Adding a type requires editing its spec, not the spec plus up to four listings.
- A drifted menu can no longer refuse a legitimate write, which is the concrete failure that motivated this.
- Workshops can test or stage against the actual prospective target contract without creating a work-local fork.
- Peer-local type use outside the owning collection becomes a deterministic failure instead of an agent convention.
- Newly installed KBs start without a stale menu and without a type path that does not resolve.
- Collection contracts get shorter and carry only clauses that bind the subtree.

**Harder / accepted costs:**

- An agent given only a shorthand type name runs a search instead of reading a table. Explicit paths, workflow-supplied paths, and the default note path avoid that search.
- A previously accepted cross-collection local type outside `kb/work/` will begin failing validation and must move, change type, or establish that its containing directory should be a collection of its own.
- Readers no longer get one exhaustive prose table of shipped types. They get common examples in the general exposition, curated global navigation in `kb/types/README.md`, and the live global or collection-local directories when they need the complete answer.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: the rule that decides between removing the copy and enforcing it
- [LLM recompute cost inverts the store-vs-recompute default](../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — rests-on: why a validated cache is ever worth its cost, and why this one is not yet
- [Stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) — evidenced-by: the failure mode the `## Types` gate reproduces on the write path
