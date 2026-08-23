---
description: "Explains why orientation and comparative reading need bounded, sufficiently related note sets, while fixed sizes, membership rules, tags, and index layouts remain implementation choices"
type: kb/types/note.md
traits: [title-as-claim]
tags: []
---

# Areas exist because useful operations require reading notes together

Some useful knowledge-base operations produce their output from relationships
among notes. One-at-a-time retrieval cannot perform those operations by itself.
When the consumer has a bounded working context, it needs a selected set that
is small enough to process jointly and related enough to justify the cost.

This note calls such a read-together set an **area**. The claim concerns the
set's function, not its implementation. An area may be a persistent index, a
query result, a graph neighbourhood, a tag-selected slice, or a temporary
batch. The name does not imply any particular frontmatter field, membership
rule, hierarchy, or index layout.

## Two operations create the need for grouping

**Orientation** reconstructs what is known about a subject: accepted claims,
live tensions, and open questions. It can use full notes or a compressed
representation such as a curated index. When it uses notes directly, the larger
model comes from reading them together, because no single note contains it.

**Comparative reading** examines several notes for relationships that cannot be
judged reliably from isolated retrieval. Its outputs include:

- Redundancy between arguments that should be consolidated
- Contradiction between claims, or a scope distinction that resolves it
- Tension between compatible claims that recommend different actions
- Complementary arguments for the same conclusion
- Missing links, missing support, and gaps in the represented design space

Comparative reading usually needs more of each note than orientation does.
Titles and descriptions may help with routing, but comparison often needs the
claims, reasons, and scope in the bodies. The two operations therefore do not
need the same representation or the same set size. Orientation benefits from a
compact synthesis of current claims, tensions, and gaps. Comparative reading
benefits from broader coverage that keeps candidate notes visible. A curated
narrative can support the first, while a complete manifest can support the
second. Systems may keep those as separate views or combine both layers. [Two
context boundaries govern
collection operations](./two-context-boundaries-govern-collection-operations.md)
develops that distinction.

When one area serves both operations, the two reinforce each other.
Orientation focuses the next comparative pass. That pass then integrates the
set, which makes later orientation cheaper. This cycle explains why a
persistent area can be useful, but it does not make persistence a requirement.

## Capacity and expected yield determine the boundary

Every joint-reading operation has a capacity bound. That bound depends on the
consumer's usable context, note lengths, the resolution loaded, instruction and
tool overhead, and the room needed to reason about relationships. A fixed note
count cannot express those variables. It may still serve as a local planning
heuristic, but not as a general split threshold.

A system that streams, externalizes, or schedules pairwise comparisons may
avoid loading the whole cohort at once. Even then, it still has to choose which
relationships to inspect and preserve enough state to integrate the results.
The capacity problem moves into scheduling and state; it does not disappear.

The other constraint is expected yield. A note belongs in a pass when reading
it with the other candidates is likely to change the operation's output. For
orientation, an unrelated note consumes capacity without improving the subject
model. For comparison, it creates another pair or cluster to inspect without a
credible relationship to find.

Relatedness is relative to the operation, not merely to a taxonomy. Two notes
from different topics may be highly related for a question about a shared
mechanism. Two notes with the same tag may be poor comparison candidates
when one is already integrated and the other addresses a disjoint concern.
Prior comparative work also changes expected yield: a well-integrated set may
need another pass only after its members change or new notes enter.

The useful boundary therefore maximizes expected result per unit of joint
attention. Changing the consumer, the resolution, the question, or the state of
the notes can change that boundary without changing the subject taxonomy.

## Operational cohorts are not classifications

A classification answers what a note is about or where readers might find it.
An area answers which notes should be processed together for a stated
operation. Conflating those questions transfers constraints from one objective
to the other.

Navigation usually benefits from high recall. A note can carry many tags, and a
broad tag can remain useful even when all tagged bodies cannot be loaded at
once. Joint reading instead needs a capacity bound and enough precision to keep
expected yield above its cost. A system may use navigation metadata to propose
a cohort, but the operation still needs its own selection step.

A bounded cohort therefore does not replace broad discovery. It concentrates an
expensive operation where it is likely to pay off. Search, graph traversal, and
other widening mechanisms remain necessary for relationships that the current
boundary did not predict.

Commonplace, this agent-operated knowledge-base framework, supplies one bounded
witness. It replaced constrained `areas:` membership with free-form tags after
the size and parent/child rules required by comparative batches reduced
navigation value. The decision deliberately left future comparative reading to
a purpose-built scoping mechanism
([ADR 004](../reference/adr/004-replace-areas-with-tags.md)). This shows that a
system can separate discovery from joint-processing scope. It does not show
that tags, or any other particular mechanism, are required.

Several consequences follow from keeping those objectives separate:

- **Membership and hierarchy are operation-relative.** Overlap is useful when a
  note has high expected yield in several operations, and wasteful when repeated
  inclusion adds cost without changing results. Hierarchy may help navigation,
  but bounded context does not imply any specific cardinality or parent/child
  membership rule.
- **Omission and partitioning optimize the operation, not ontology.** Omission
  from a purportedly complete orientation set can hide knowledge, while
  omission from one comparative pass may simply mark its scope. Cohorts should
  split or merge according to capacity and cross-boundary yield, even when the
  result looks untidy as a taxonomy.
- **Stable and temporary cohorts trade selection cost against staleness.** A
  stable set amortizes selection and orientation, but it can become stale. A
  generated set follows the current question, but it pays selection cost on each
  run.

## Open Questions

- How should expected comparative yield be estimated before paying for the
  comparison?
- When does a stable cohort's amortized orientation value exceed its staleness
  and maintenance cost?
- Can observed outputs distinguish a well-integrated cohort from a poorly
  related one when both produce few new findings?

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: finite usable attention creates the capacity side of the cohort boundary
- [Stale indexes reduce discovery when they suppress fallback search](./stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) — grounds: explains why omission becomes harmful when an apparently complete set closes broader discovery
- [Two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — extends: separates full-body comparison from title-and-description orientation and derives the resulting operating regimes
- [A knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: places read-together cohorts among the resolution levels a consumer must move between
- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — extends: treats comparative-reading yield as a possible signal for evaluating cohort construction
- [004-Replace areas with tags](../reference/adr/004-replace-areas-with-tags.md) — evidenced-by: records one system separating high-recall navigation tags from future purpose-built comparative scope
