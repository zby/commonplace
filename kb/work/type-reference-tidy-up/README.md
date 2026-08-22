# Type reference tidy-up

## Goal

One source of truth for what types exist and a deterministic rule for which type an artifact may use. Type-spec frontmatter (`name:`, `description:`) is ground truth for type identity and description. For an ordinary collection, validation permits the global types plus that collection's own local types.

`kb/work/` is the deliberate validator exception because it is a lifecycle staging layer rather than a durable content register. An artifact anywhere under `kb/work/` may point to any valid type spec. This lets workshops draft for any durable collection and test the real contracts without copying them into `kb/work/types/` and creating second path-valued types.

The work: consolidate type exposition around the live type specs, remove unchecked copies of type metadata, enforce collection-local eligibility in the validator, preserve the workshop exception there, and repoint the consumers that read the menus today.

## Why now

The drift is not cosmetic — one copy is a hard gate. `kb/instructions/cp-skill-write/SKILL.md:26` tells the writer to "pick one listed type path" from the target collection's `## Types` section and to **stop** if the requested type is not listed. So a stale menu silently refuses legitimate writes.

Observed at the start of the workshop on 2026-08-22:

| Layer | Scope | State |
|---|---|---|
| Type-spec `name:`/`description:` (20 specs) | ground truth | — |
| `kb/reference/available-types.md` | all types | drifted — omitted `article` (3 primary article artifacts use it); retired during the exposition prerequisite |
| `kb/types/README.md` | global types | accurate today, unenforced |
| 8 × `COLLECTION.md` `## Types` | per-collection menu | drifted — `kb/reference/` omits `type-spec`, which its 2 local type specs use |
| 3 × `src/commonplace/_data/templates/user-*-COLLECTION.md` | seeds every install | ships `kb/types/skill.md`, which does not exist; section otherwise empty |

Live failure: asking `cp-skill-write` for a `type-spec` by shorthand under `kb/reference/` is refused, though two such artifacts already sit there. Supplying the explicit path bypasses the stale menu, which is the behavior the replacement rule generalizes.

## What closes this workshop

- A decision recorded on whether `COLLECTION.md` enumerates types (draft ADR in this directory).
- One general current-state exposition showing how artifacts use types, giving common examples, and routing readers to global and collection-local type directories.
- Validation permits global plus owned-local types in ordinary collections and any valid type under `kb/work/`.
- The consumers that read the enumeration repointed at a derivation that cannot drift.
- The shipped scaffold no longer seeding a stale or phantom menu.
- `kb/types/README.md` remains curated global navigation without claiming exhaustiveness; the retired catalogue has no successor copy.
- No enumeration left that is neither code-checked nor recomputed on read.

## Evaluation boundary

In scope: where the list of available types lives, who reads it, deterministic collection-local eligibility, and the lifecycle exception for the `kb/work/` subtree.

Out of scope: the type vocabulary itself (no types added, removed, or renamed); path syntax and type-spec loading (now described in [`collections-and-types.md`](../../reference/collections-and-types.md)); whether an `artifact_function` axis should exist — that stays in [artifact function as a routing field](../../reference/proposals/artifact-function-as-a-routing-field.md).

## Bookkeeping

Working files live here. The ADR draft points directly to the reference ADR type, which the `kb/work/` validator exception permits, but it is not accepted while it remains in `kb/work/`; adoption adds the accepted lifecycle status and promotes the file to `kb/reference/adr/`. Findings that outlive the tidy-up go to `kb/notes/`; everything else is consumed with the workshop.

---

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: the safety half of the rule this workshop applies
- [LLM recompute cost inverts the store-vs-recompute default](../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — rests-on: the value half; why a cache is ever worth keeping
- [Stale indexes reduce discovery when they suppress fallback search](../../notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) — evidenced-by: the failure mode the `## Types` gate reproduces
