# Order of concerns in revision

## Goal

Ground the rule "higher-order concerns before lower-order concerns" in
checked literature, then decide what the library should hold: adjustments to
existing theory notes, a new note, or both.

The operator opened this workshop on 2026-11-13. The rule was adopted that
day as the ordering of the
[one improvement procedure](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)'s
default composition: check what a note is (its claim, boundary, existence,
place) before working on how it says it. The proposal defines a concern as
higher-order than another when settling it differently would discard work
done on the other. The wording was recalled from writing instruction and
cites nothing yet.

## Current result

The bounded library change is implemented. [Unresolved revision choices put dependent polish at risk of rework](../../theory/resolve-revision-choices-before-polishing-text-that-depends-on-them.md) owns the discarded-work mechanism. The low-degree-of-freedom note now distinguishes it from option preservation, and the procedure proposal cites the new note and grounded Purdue guidance. The [vocabulary collision ledger](../../reference/vocabulary-collision-ledger.md) keeps higher-order concerns separate from second-order lessons without registering a shared hierarchy.

The literature acquisition remains partial. [Composition research](./composition-research.md) records the accepted Purdue ingest and blocked Faigley–Witte/Sommers acquisitions; [editing and planning research](./editing-planning-research.md) records the accepted JPL ingest and blocked Sacerdoti acquisition. JPL's levels commission services rather than prescribe an execution order. Historical terminology priority and a checked planning precedent remain unresolved. The new note makes no historical-priority claim and leaves broader design transfer conjectural. The workshop remains open for those source gaps, not for another theory rewrite by default.

## What the library already holds

- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md)
  is the nearest rule. It orders by the size of the feasible set, grounds
  that in Alexander and in constraint search, and names phrasing and
  narrative order as the flexible end.
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../theory/productive-deferral-requires-option-evidence-and-convergence.md)
  covers the lower-order work and the weak proposals that an improvement run
  saves for later.
- [An author should fix what the executor can't determine, not what it will](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md)
  keeps who decides apart from when.
- [Narrowing bought to survive review is paid for in content](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md)
  describes the failure the rule is meant to prevent: lower-order repair
  applied to a higher-order fault.
- The simplification passes declare a `depth` order with no stated source.

## The open question

Order by dependency and order by degrees of freedom usually agree and can
come apart. A note's claim is the highest-order concern and may have many
viable formulations. A required frontmatter key has one viable value and is
about as low-order as a concern gets. So the existing note may not entail
the rule. The workshop should settle whether the rule is an instance of
that note, a second ordering criterion beside it, or the more general
statement of which degrees of freedom is a correlate.

A second question follows from the design parallel: whether this is a rule
about revising texts or about any revisable artifact with levels (a note, a
proposal, code), with design methodology as the wider precedent.

## Leads, unverified

Recalled, not checked. Each needs a source located, snapshotted and
ingested before the library cites it.

- Technical editing: Van Buren and Buehler, *The Levels of Edit* (Jet
  Propulsion Laboratory, 1976; second edition 1980): ordered, separately
  commissioned levels of edit.
- Composition research: Sommers, "Revision Strategies of Student Writers
  and Experienced Adult Writers" (1980); Faigley and Witte, "Analyzing
  Revision" (1981), whose surface versus text-base distinction turns on
  whether a change alters the summary of the text; Flower, Hayes and
  colleagues on detection, diagnosis and strategy in revision (1986).
- Writing-centre practice: the source of the terms higher-order and
  lower-order concerns themselves, which is not yet identified.
- Publishing practice: developmental, line, copy and proof stages.
- Planning: Sacerdoti's ABSTRIPS (1974) on ordering decisions by
  criticality; Stefik on least commitment (1981).
- Software: separating structural from behavioural change; pass ordering by
  which analyses a transformation invalidates.

## Vocabulary

"Higher-order" and "lower-order" are kept as the names of the levels. The
KB also uses "second-order" for a lesson that targets a prior commitment
([reflection makes retained lessons second-order](../../theory/reflection-makes-retained-lessons-second-order.md)).
Decide whether that double sense needs an entry in the
[vocabulary collision ledger](../../reference/vocabulary-collision-ledger.md),
and whether the two terms become registered definitions once sourced.

## How to advance the work

1. Identify the source of the terms and choose the two or three leads that
   bear most on the open question. Faigley and Witte's test and the levels
   of edit are the first candidates.
2. Snapshot and ingest them with `cp-skill-snapshot-web` and
   `cp-skill-ingest`; retain quotes with `cp-skill-ground` where a note
   will rest on a specific passage.
3. State what each source says about ordering, about what makes a concern
   higher-order, and about who chooses the level of a revision.
4. Decide the library change: add the precedent to the existing
   low-degree-of-freedom note, write a new note on ordering by what a
   change invalidates, or both; then update the procedure proposal's
   attribution.
5. If the levels generalise beyond texts, say so in the note and name the
   design-methodology precedent, or record why not.

## Scope

In scope: literature that bears on ordering revision work, and the
resulting theory changes. Out of scope: designing or evaluating the check
itself, which belongs to
[higher-order check evaluation](../higher-order-check-evaluation/README.md).
Full copies of sources stay in private snapshots; the library holds bounded,
attributed quotations.

## Completion

Close when the rule's wording in the procedure proposal cites checked
sources, the open question is answered in a library note, and the
vocabulary decision is recorded. Close without a new note if the sources
show the existing note already entails the rule, with that note amended to
say so.
