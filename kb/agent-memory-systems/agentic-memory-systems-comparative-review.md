---
description: "What 129 code-grounded agent-memory reviews show when set on one matrix: storage no longer divides the field, the real split is automatic-capture+automatic-activation vs authored+explicit-lookup, most pushed memory is coarse, enforcement is the authority discriminator, and almost no system verifies that its automatic activation is right."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
status: current
---

# What the matrix shows across 129 agent memory systems

Every code-grounded review in this collection classifies its system on one shared
set of axes — [storage substrate](../notes/definitions/storage-substrate.md),
[lineage](../notes/definitions/lineage.md),
[behavioral authority](../notes/definitions/behavioral-authority.md), and how
memory [reaches the next action](../notes/knowledge-storage-does-not-imply-contextual-activation.md).
Parsed into [`systems.csv`](./systems.csv) and rendered as the
[comparison table](./systems-table.md), 129 systems can be counted rather than
characterized one at a time. Six findings stand out. The headline: the question
people reach for first — files or database? — is the one that no longer divides
the field, and the questions that do divide it are about *activation* and
*verification*, not storage.

## 1. Storage stopped dividing the field

Files-family substrates (plain `files`, a git `repo`, `in-memory`) still lead at
**68%**, but **29%** are database-backed — and the modal database is plain
**SQLite (13%)**, not a vector or graph store (**9% combined**). "Filesystem-first
convergence" was the founding observation of this collection; at 129 systems it is
a slim majority, not a landscape law. More to the point, substrate predicts very
little else — file-first systems span the full range of activation and authority
below, and so do the database-backed ones. Storage is an operational floor
(inspectability vs scale), not the architectural fork it is often treated as.

## 2. The real split is a coupled bundle — and it isn't storage

How memory is *made* and how it is *activated* turn out to be the same axis. Of the
**62%** of systems that derive memory automatically from agent traces, **84% push
or do both** — automatic capture and automatic activation ship together. The
converse holds: **70%** of pull-only systems are *not* trace-derived; they are
authored or curated and wait to be asked. The population sorts into two camps:

- **Automatic camp (52%)** — trace-derived *and* pushing. The system watches the
  agent, distills memory, and injects it without being asked.
- **Curated camp (23%)** — authored *and* pull-only. A human writes; the agent
  retrieves on a deliberate, auditable lookup.
- The remaining **25%** mix the two (authored memory with a push path, or
  trace-derived memory behind an explicit search).

This — not files-vs-database — is the choice that cascades. It decides who holds
the throughput/reviewability tradeoff: the automatic camp accumulates fast and
audits weakly; the curated camp audits well and scales slowly.

## 3. Pushed memory is mostly coarse, not targeted

Among the 86 systems that push, **69% fire a coarse always-load** (session-start
profile blocks, recent notes, checkpoint state) rather than selecting for the
moment. Instance targeting is real but minority and shallow: identifier match 49%,
embedding similarity 47%, lexical 38%, and an actual **LLM relevance judgment only
16%**. Most "push" is "load the standing context," not "select the right memory
for this turn." That matters because targeting is
[bounded by symbol availability](../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md):
precise selection needs an identifier already on the table or a content inference,
and most systems have neither wired, so they fall back to loading everything
relevant-ish.

## 4. Almost nobody checks the push is right

This is the sharpest gap. Of the 86 pushing systems, **7 (8%)** test read-back
faithfulness — whether the memory that fired actually changed the agent's behavior
(ablation, perturbation, post-action audit). The rest assume context presence
equals use. Automatic activation is the most widely shipped capability in the
survey and the least verified: systems invest heavily in *deciding what to inject*
and almost nothing in *confirming the injection landed*. Knowledge storage does
not imply contextual activation, and the field is largely operating on faith that
it does.

## 5. Enforcement is the authority discriminator

Every system carries knowledge authority; instruction and routing (90% each),
validation (83%), ranking (79%), and learning (74%) are near-universal — so common
they describe the category rather than distinguish within it. The one authority
mode that actually splits the field is **enforcement, at 54%**: whether stored
memory ever acts as a *hard gate* (a check the agent can't bypass — a validation
that must pass, a blocking rule, a required proof) versus advisory context it can
override. This is the real line between memory that *informs* and memory that
*binds*, and it runs right down the middle of the population.

## 6. Extraction is automated; genuine synthesis is not

Systems readily create and tier memory — promote 73%, synthesize-labelled 67%,
consolidate 54% — but the operations that maintain *truth* over time lag:
invalidate 50%, evolve 43%, decay 35%. And **17 of 129 systems run no automatic
curation at all** (10 of them manual-only authoring). The hardest operation —
deriving a genuinely *new* claim across stored entries, as opposed to summarizing
them — remains rare and mostly aspirational even where the matrix records a
`synthesize` token. Curation is where the survey's frontier still sits: capture is
solved, lifecycle maintenance is not.

## What this means for our design

The two findings that bear on Commonplace are the curated camp's known weakness and
the verification gap. We sit squarely in the **curated camp** (authored, pull-first,
files) — which the matrix confirms is the minority bet, strong on reviewability and
weak on throughput. The standing risk is the one camp-2 systems share: manual
curation does not scale. The answer the data points to is not defecting to the
automatic camp (which trades navigability and audit for volume) but *automating the
curation itself* while keeping memory authored and inspectable. And finding 4 is a
cheap edge: faithfulness testing is nearly absent across all 129 systems, so a KB
that actually checks whether a loaded note changed an agent's behavior would be
measuring something the rest of the field assumes.

Relevant Notes:

- [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds: findings 2–4 rest on the read-back / activation distinction this note draws
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - see-also: why the dividing axes span storage, retrieval, and learning at once
- [trace-derived-learning-techniques-in-related-systems](./trace-derived-learning-techniques-in-related-systems.md) - see-also: the focused survey of the automatic camp this matrix quantifies
- [designing-agent-memory-systems](../notes/designing-agent-memory-systems.md) - rationale: the design-pressure inventory the review axes distill
