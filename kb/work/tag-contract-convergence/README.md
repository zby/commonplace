# Tag contract convergence workshop

**Opened:** 2026-08-27

**Posed by:** the operator, after review of T1 in the system-contract consistency
workshop

**Audited starting commit:** `6660bd2ad0d53938551ac283f60463f3c3d91b8e`

**State:** active. The [readiness pass](./plans/00-readiness.md) fixed the
activation boundary, declaration syntax, resolver surface, transitional head
model, consumer ledger, and fixture. Core implementation waits for minimal I3;
no adopting ADR, live participation declaration, exact resolver, consumer
migration, canonical tag collection, or upgrade migration has landed.

## Goal

Establish one coherent contract connecting:

1. what assigning a tag asserts;
2. which artifacts participate in tag membership;
3. how exact membership is resolved;
4. what a tag head provides;
5. what `complete` and `covered_by` authorize consumers to skip;
6. how every exact-membership consumer uses the same relation;
7. how source and installed KBs keep separate but coherent tag spaces.

This workshop owns the tag subsystem redesign extracted from T1. The parent
[system-contract consistency workshop](../system-contract-consistency/README.md)
retains the original contradiction, witnesses, dependencies, and final closure
check.

## Why this is a separate workshop

T1 is no longer one local contradiction repair. It joins tag semantics,
`kb-root` ownership, collection participation, exact resolution, validation,
publishing, navigation, installed projection, and migration. Keeping that
design here lets the consistency workshop ask where operative contracts
disagree while this workshop asks what coherent architecture replaces them.

## Starting witnesses

- The [tag-readme type](../../types/tag-readme.md) and routing use unqualified
  membership language across collections, while current validation and
  generated augmentation enumerate one collection.
- [Trace-learning techniques in related
  systems](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md)
  carries `learning-theory` without any child declared by the notes collection's
  [covered head](../../notes/learning-theory-README.md), yet that head validates.
- The complete [artifact-analysis head](../../notes/artifact-analysis-README.md)
  omits a live reference proposal under the proposed participating scope.
- Published tag footers can route across a collection boundary while the page
  reached is generated from a narrower membership set.

The full starting audit remains in the [parent handoff
record](../system-contract-consistency/plans/t1-tag-scope.md).

## Design inputs, not authority

- [Tag scope is declared where membership claims are
  made](../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md)
- [Semantic contract for tags and tag
  heads](../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md)
- [Link-following and search impose different metadata
  requirements](../../notes/link-following-and-search-impose-different-metadata-requirements.md)
- [Pointer design tradeoffs in progressive
  disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md)

The recent Pirolli, Teevan, Tombros–Sanderson, Milo, and Luhmann ingests linked
from those inputs motivate a distinction among proximal cues, contextual local
navigation, and query-conditioned results. They concern humans, practitioner
method, or historical systems. They do not establish LLM-agent performance.

The parent workshop's disjoint-root decision supersedes the tag proposals'
embedded-root pruning and physically shared `kb/types/` assumptions as design
inputs. The proposals remain unchanged until adoption because this workshop
does not make them operative authority.

## Working architecture

The adopting decision should begin from these narrow choices:

- One tag string has one canonical declared sense within one `kb-root`.
- Membership is projection-relative and ranges over explicitly participating
  collections in that root.
- A minimal canonical head is required from the first stable use in a
  participating collection. It may be small before it earns richer routing.
- Provisional vocabulary may exist only outside the participating library.
  Promotion into participating content must reuse or establish a canonical tag.
- Structure enforces one canonical declared sense. Whether an assignment
  satisfies that sense belongs to the write path and semantic review; schema
  validation cannot prove one-string-one-sense.
- `complete` and `covered_by` authorize skipping only exact membership
  resolution. They never authorize stopping task-level discovery.
- The exact resolver defaults to deterministic path, title, and description
  records. Query-conditioned ranking or summaries are later operations.
- Add no new tag relations without a demonstrated consumer. `covered_by`
  remains the only current typed routing relation.
- Canonical heads are the vocabulary registry. Do not add a second manually
  maintained known-tags list unless a concrete provisional-tag lifecycle needs
  one.
- Phase 2 activates these semantics once, with live participation declarations,
  mandatory transitional heads, every exact-membership consumer, and the
  accepted ADR. Phase 1 may land dormant resolver machinery; Phase 3 later
  changes head representation without changing membership.

These are workshop selections until an ADR adopts them.

## Staged program

0. [Readiness and execution inventory — complete](./plans/00-readiness.md)
1. [Semantic foundation and exact resolver](./plans/01-semantic-resolver.md)
2. [Consumer convergence and contract activation](./plans/02-consumer-convergence.md)
3. [Canonical heads and migration](./plans/03-canonical-heads-migration.md)
4. [Independent metadata cleanup and empirical follow-up](./plans/04-cleanup-and-follow-up.md)

Phase 1 is separately landable only while its resolver and head lookup remain
dormant. Phase 2 is the single activation packet: the accepted ADR, live
declarations, head requirement, consumer switches, and witness repairs change
operative behavior together. Phase 3 changes canonical paths only after
consumers resolve semantics correctly in existing locations. Source-family
cleanup is independent and must not enlarge the core adoption patch.

## External dependencies

- I3 supplies explicit, pairwise-disjoint `kb-root` boundaries and root-local
  collection/type discovery. The selected installation shape is recorded in
  the parent workshop's [impact
  ledger](../system-contract-consistency/disjoint-root-impact-ledger.md).
- V1 supplies structured whole-product validation.
- I2 supplies the installed edition and compiler-like projection.
- I1 supplies the generic ownership-aware upgrade mechanism.

This workshop supplies migration inputs and acceptance criteria to those
programs. It does not implement parallel topology, projection, validation, or
upgrade machinery.

## Evaluation boundary

Structural closure asks whether every exact-membership consumer resolves and
uses the same eligible set, in source and installed projections. It does not
ask whether one navigation presentation improves agent task performance.

After the resolver and heads exist, a bounded agent trial may compare exact
membership records, a curated head, and query-conditioned pointers. Measure
membership recovery and task-relevant discovery separately, including false
stopping. That trial is follow-up unless an adopted decision makes a performance
claim.

## Closure condition

Close and delete this workshop after:

- an ADR adopts one tag semantic, root, participation, mark, and head contract;
- all exact-membership consumers use the resolver;
- canonical heads and source/installed migrations pass their fixtures;
- the two proposals are retired through the normal proposal lifecycle;
- independent cleanup is completed or explicitly transferred;
- the parent workshop rechecks and closes its original T1 witnesses;
- durable outcomes are linked from current navigation and this workshop has no
  remaining authority role.
