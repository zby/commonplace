---
description: Agentic-system analysis drops the scoping job, the memory handoff protocol and the review job, derives the public review from the verified overview, and fixes source identity and the blockers form in code
type: reference/types/adr.md
status: accepted
---

# 097 — Agentic analysis drops decisions that change no result

**Status:** accepted
**Date:** 2026-09-29

## Context

After [ADR 096](./096-analysis-passes-declare-their-own-records-under-lens-prefixes.md),
an agentic-system analysis still asked workers to make decisions whose
alternatives changed nothing in the result, and then asked later steps to
accept, restate or check them:

- A `scoping` job chose `brief` or `full` depth for each lens. Both lenses
  always ran, no code read the depth, and each lens member stated its
  scope again.
- The memory specialist followed a private handoff protocol: an input
  bundle, `memory-input.md`, hashed by hand into
  `canonical-register-sha256`, plus `method-sha256` and `worker-model`.
  Only the first was checked, against gitignored run state, so no clean
  checkout could verify it.
- A `review` job wrote the public review's prose after verification. No
  check covered that prose, and it restated the Bounded synthesis.
- The caller's source identity and the boundary worker's
  `source.identity` were authored independently and never compared.
  Publication compared identities by exact string, so a difference of
  form failed after the whole analysis ran.
- The workflow continued when the Blockers text, loosely normalized,
  equalled `none`. "None found" counted as a blocker.

## Decision

Delete the `scoping` job, the `brief`/`full` depth, the overview's
`## Lens scoping` section, `memory-input.md` and its generator, and the
memory handoff protocol. The memory and epistemic jobs read `boundary.md`
and `output/runtime.md` under the same input and completion contract as
every other job. Drop `canonical-register-sha256`, `method-sha256` and
`worker-model` from the memory report type. Model identity stays in the
workflow's operational state, and `inputs-commit` pins the method.

Delete the `review` job. Code renders the public review from the verified
overview: `# <System>`, an `Evidence basis:` line built from the boundary
fields, the Bounded synthesis, and `## Limitations`. Relative links are
rewritten to resolve from the review into the retained set. The
reconciliation writes a one-sentence `## Description` of 50 to 250
characters. Code uses it as the `description` of a complete run's overview
and of the review, so verification reads it. The overview type's Bounded
synthesis contract now says the synthesis must read without the members'
context.

Normalize the source identity once, when the workflow is constructed. The
rule strips surrounding whitespace, a trailing `/` and a trailing `.git`,
and lowercases a URL's scheme and host. The run slug, destination
inspection, the boundary job's prompt and publication use that form. The
boundary validator refuses a frozen `source.identity` that differs.

The verify job's validator accepts `### Blockers` only as exactly `none`
or a Markdown list of `- ` entries. The workflow continues only on exactly
`none`.

## Considered alternatives

**Keep scoping with a separate effort budget.** Advance control over
inspection effort would need a mechanism that consumes the depth; none
existed. If a budget becomes necessary, it should be specified on its own.

**Export the memory provenance into the retained set.** Moving
`memory-input.md` into the set would make the pin checkable, but the file
only restated the boundary and runtime member the set already holds.

**Keep a separately written review for a different audience or length.**
One account serving both readers costs length. On the PageIndex set,
before ADR 096 deleted it, the review body had 464 words, the Bounded
synthesis 611 and the Limitations 220. The operator accepted the length
in exchange for publishing only verified prose.

**Keep the description outside the set.** A side file from the
reconciliation would keep the overview's code-written description, but
nothing would check the published description.

**Structured decision fields for blockers and returns.** Workflow
decisions could be represented as structured fields, from which headings
are derived. Fixing the form of the one prose section code reads removes
the misreading without a second representation.

**Remove the return route to the memory specialist.** Deferred to the
second real run. The option under test is no returns, with amendments and
limitations as the only correction.

## Consequences

A complete run now has four job kinds: `boundary`, `runtime`, the two
lenses, and rounds of `reconcile` and `verify`. Public reviews get longer
and carry only prose that verification read. A reconciliation must write
a Bounded synthesis that stands alone. Run directories opened before this
change hold `## Lens scoping` and the removed memory fields, and no longer
validate. The workflow's normalization does not extend to the publication
CLI's `inspect-destination --source-identity` argument, which is compared
exactly. The decision is untested by a real run; the second real run tests
it together with ADR 096 and cannot isolate either.

This ADR adopts the design proposal *Fewer authored decisions in
agentic-system analysis*.
