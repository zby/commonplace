# Tag contract convergence workshop

**Opened:** 2026-08-27

**Posed by:** the operator, after review of T1 in the system-contract consistency
workshop

**Audited starting commit:** `6660bd2ad0d53938551ac283f60463f3c3d91b8e`

**State:** active. The [readiness pass](./plans/00-readiness.md) fixed the
activation boundary, declaration syntax, resolver surface, transitional head
model, consumer ledger, and fixture. On 2026-09-25 it was rebaselined for
[ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md),
which removed the installed library copy and with it the multi-root design.
Phase 1 is ready. Later the same day the program was reordered: a finding
trial (Phase 2) now tests whether any tag page helps before the contract and
head work. `kb/types/` is now a discovered collection and type specs
reject tags (commit `fd573556`). No adopting ADR, live participation
declaration, exact resolver, consumer migration, canonical tag collection, or
host migration has landed.

## Goal

Establish one coherent contract connecting:

1. what assigning a tag asserts;
2. which artifacts participate in tag membership;
3. how exact membership is resolved;
4. what a tag head provides;
5. what `complete` and `covered_by` authorize consumers to skip;
6. how every exact-membership consumer uses the same relation;
7. how a host project's tag space stays separate from the installed library's.

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

Both corpus witnesses below have since been repaired locally (see the
[rebaseline](./plans/00-readiness.md#rebaseline-for-adr-086-2026-09-25)). The
defect they exposed is latent, not gone: validation still checks one
collection, so Phase 3 acceptance uses a synthetic cross-collection witness.

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
- [Tag maintenance and derived
  browsing](../../reference/proposals/tag-maintenance-and-derived-browsing.md)
  — the Gwern-derived browsing and maintenance options; the source of the
  Phase 2 finding trial's grouped page

The recent Pirolli, Teevan, Tombros–Sanderson, Milo, and Luhmann ingests linked
from those inputs motivate a distinction among proximal cues, contextual local
navigation, and query-conditioned results. They concern humans, practitioner
method, or historical systems. They do not establish LLM-agent performance.

ADR 086 supersedes the tag proposals' embedded-root pruning and the parent
workshop's disjoint-root design. The proposals remain unchanged until adoption
because this workshop does not make them operative authority.

## Working architecture

The adopting decision should begin from these narrow choices:

- One tag string has one canonical declared sense within one KB. A host
  project's `kb/` and the installed library are separate KBs; the library is
  read-only and validated in the source checkout.
- Membership ranges over the explicitly participating collections of one KB.
  Type specs never carry tags.
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
- Phase 3 activates these semantics once, with live participation declarations,
  mandatory transitional heads, every exact-membership consumer, and the
  accepted ADR. Phase 1 may land dormant resolver machinery; Phase 4 later
  changes head representation without changing membership.
- Usefulness is tested before correctness is enforced. The operator stopped
  using tags because tag pages did not help them find things (2026-09-25).
  The Phase 2 trial compares the current page, an exact listing, a Gwern-style
  grouped page, and no tag at all; its result decides how much contract and
  head work follows. Letting heads carry tags as related-topic links would
  change membership; if wanted, the ADR decides it.

These are workshop selections until an ADR adopts them.

## Staged program

0. [Readiness and execution inventory — complete](./plans/00-readiness.md)
1. [Semantic foundation and exact resolver](./plans/01-semantic-resolver.md)
2. [Finding trial: does any tag page help find things?](./plans/02-finding-trial.md)
3. [Consumer convergence and contract activation](./plans/03-consumer-convergence.md) — scope set by Phase 2
4. [Canonical heads and host migration](./plans/04-canonical-heads-migration.md) — scope set by Phase 2
5. [Independent metadata cleanup](./plans/05-cleanup-and-follow-up.md)

Phase 1 is separately landable only while its resolver and head lookup remain
dormant. Phase 2 may rewrite or close Phases 3–4; if nothing beats plain
description search, tags become search keywords and the head and mark work is
dropped. Phase 3 is the single activation packet: the accepted ADR, live
declarations, head requirement, consumer switches, and witness repairs change
operative behavior together. Phase 4 changes canonical paths only after
consumers resolve semantics correctly in existing locations. Source-family
cleanup is independent and must not enlarge the core adoption patch.

## External dependencies

None since the 2026-09-25 rebaseline. The parent workshop's I1, I2, I3, and V1
findings no longer gate this program: there is no projected library copy to
migrate or validate, and Phase 4 uses `commonplace-init`'s existing migration
path for host projects.

## Evaluation boundary

The Phase 2 finding trial is a gate on scope, not on closure. It decides
whether tags are worth a contract at all and which tag page the contract should
serve. Its result is judged on the operator's real finding tasks, for the
operator and for fresh agents, measuring found targets, misses (including
relevant items outside the tag), items opened, and early stopping.

Structural closure then asks whether every exact-membership consumer that
survives Phase 2 resolves and uses the same eligible set, in the source
checkout and in a host project.

## Closure condition

Close and delete this workshop after:

- the Phase 2 finding trial has recorded its result and decision;
- an ADR adopts the tag contract that decision supports: at minimum one
  semantic, participation, and membership contract, plus the mark and head
  contract if tags remain a finding path;
- all surviving exact-membership consumers use the resolver;
- if heads survive, canonical heads and the source and host migrations pass
  their fixtures;
- the two proposals are retired through the normal proposal lifecycle;
- independent cleanup is completed or explicitly transferred;
- the parent workshop rechecks and closes T1;
- durable outcomes are linked from current navigation and this workshop has no
  remaining authority role.
