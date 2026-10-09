---
type: reference/types/design-proposal.md
description: "Proposal: make generic conformance reviews consume and track the shared source and record contracts that analysis member types now inherit"
---

# Shared analysis contract conformance

Analysis member types inherit source and record requirements. Their generic
type-conformance review must either assess those requirements from pinned
inputs or state a narrower result; a member-type snapshot alone no longer
contains the whole contract.

## Current state (as of 2026-10-01)

- Commit `d77388b4` separates the source contract (since split between the
  [boundary type](../../agentic-system-analyses/types/agentic-system-boundary.md) and the worker rules)
  and [record contract](../../agentic-system-analyses/instructions/agentic-analysis-records.md) from four member
  types. The analysis workflow declares both files to its analysts,
  reconciliation and verification. Changes reopen the affected jobs and
  block publication against an earlier method commit.
- Generic type-conformance reviews capture the target artifact and its
  type-spec criterion. `src/commonplace/review/freshness.py` captures and
  compares those two texts, without the type's shared dependencies.
- `src/commonplace/review/protocol/prompt.py` embeds the type-spec text but
  permits link following only from target notes, with one limited exception
  for an exact path derived from such a link. It neither embeds nor
  authorizes general traversal of the criterion's shared-contract links.
- The store can represent arbitrary criterion identities, but the current
  selector and path resolver do not admit these reference documents as
  generic conformance criteria. Storage support alone does not provide the
  missing delivery and selection path.
- This boundary affects generic type-conformance assays. The analysis
  workflow's own verification receives the shared contracts already.

## Options

### Factored shared-contract reviews

Derive separate artifact/shared-contract pairs alongside the member-type
pair. Each reviewer receives its actual contract as criterion text, and
ordinary two-input freshness tracks it. A full conformance claim requires
the relevant pairs together. This follows the existing
[factored-pairs direction](./factored-dependency-pairs-for-review-freshness.md).

Operativity: the selector admits the shared criteria for the member types
that inherit them; the renderer makes their assessment scope explicit;
consumers distinguish member-specific conformance from full conformance.
This requires implementation. Its oracle is the retained contract's
content, with deterministic syntax checks excluded. Factoring is warranted
only where each judgment can be made independently from its two inputs.

### Materialized complete criteria

Generate a complete review criterion containing the member and shared
requirements. The reviewer receives and hashes one actual criterion
artifact. Generation and consistency checks must keep it aligned with
every input; expanding only the prompt would leave freshness incorrect.

Operativity: criterion generation and selection supply the materialized
artifact, and dependency changes refresh it before review or acceptance.
This requires implementation and retains larger review packets and derived
copies. The oracle remains the retained requirements, not the generator.

### Keep member types self-contained

Return shared requirements to each member type. The existing review path
then receives and tracks them, but authors and reviewers load repeated
text. Compact producer views would need a separate, checked consumption
path if the worker-reading gains are to survive.

Operativity: the current type-spec snapshot supplies the complete criterion.
This option trades the cleanup's single ownership for larger contracts or
additional view generation; it needs no wider review input model.

## Forces and free choices

- Delivery and freshness are separate requirements: permission to follow
  a link would not make changes to its target invalidate an existing review.
- The analysis workflow has explicit dependencies; generic type reviewers
  are another consumer and need their own mapping.
- Factored pairs add review calls. Materialized criteria add generation and
  derived-copy maintenance. Repeated member contracts add reading and drift.
- Select the conformance scope, the criterion delivery path and the result
  policy together. Do not silently count a member-only result as complete
  conformance, or introduce a general multi-input target without a judgment
  that requires it.

## Adoption criteria

An adopted option must demonstrate that a reviewer receives every required
clause, that changing either shared contract invalidates the appropriate
acceptance, and that unaffected types keep their present behavior. The
result must name its conformance scope. Before choosing factored pairs,
show on representative member findings that the judgments can be assessed
independently; otherwise retain the coupled requirement in one materialized
criterion. No option is adopted here.
