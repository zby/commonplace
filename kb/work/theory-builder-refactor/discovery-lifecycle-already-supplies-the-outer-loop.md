# Discovery lifecycle already supplies the outer loop; inquiry selection is the missing operation

> **Status:** Working document, 2026-09-12. Written in response to the
> operator's summary of a ChatGPT conversation proposing an
> "automated-scientist" outer ontology around theory refinement. Proposes not
> adopting new outer-loop machinery, but locating the missing piece inside
> terms the KB already has, and recommends against importing fresh vocabulary
> for it.

## What ChatGPT proposed

Theory refinement is the right operation for the inner update step, but as a
top-level ontology it starts too late: it presupposes a theory and evidence
already in hand. The proposal nests an outer "theory building" loop (propose
or maintain candidate theories, derive consequences, choose discriminating
observations or experiments, obtain evidence, interpret it, revise, reject,
split, merge, or retain) around an inner "theory refinement" loop (compare,
locate, revise, evaluate). Its sharpest point against the workshop's five-
operation interface: derive/compare/locate/revise/evaluate says nothing about
where cases come from, and a strong learner should construct tests that
discriminate between competing explanations rather than wait for
counterexamples.

## The outer loop already exists: discovery lifecycle

`CLAUDE.md`'s vocabulary already registers an outer ontology for exactly this:
[discovery lifecycle](../../notes/definitions/discovery-lifecycle.md),
observation/anomaly, conjecture, consequence derivation, test/accumulation,
acceptance, integration. `theory-builder-proposal.md` already cites it as the
frame for reflection's phases (line 211). The correspondence to ChatGPT's
outer loop is close:

| Discovery-lifecycle phase | Builder step or interface operation |
|---|---|
| Observation / anomaly | case capture, prior to any operation |
| Conjecture | `theory-builder.md`'s **development** — constructing a first theory, already scoped as separate from refinement |
| Consequence derivation | **Derive** |
| Test / accumulation | **Compare** and **Locate** — minus the step below, which this phase does not decompose |
| Acceptance | **Evaluate** |
| Integration | **Apply** / retain |

So "we need an outer ontology" overstates the gap: the KB already has one,
doctrine-registered, and it is not in tension with theory refinement as the
inner case — the workshop's own material already uses it that way. What is
actually missing is not a layer. It is one operation inside the phase
discovery-lifecycle deliberately leaves undecomposed: Test/accumulation
"compare[s] those consequences with cases; gather[s] support, counterevidence,
and rival explanations," without saying how a case to gather is chosen.
discovery-lifecycle's own scope section defers exactly this: "How to actually
run observation, testing, or acceptance is the business of instructions,
ADRs, and workflow notes; the definition only fixes when the compound
applies." Supplying the missing step is that kind of workflow detail, not a
change to the phase model, so it does not require editing
`discovery-lifecycle.md`.

## The gap was already named twice inside the KB, independently of ChatGPT

- `theory-refinement-interface.md`'s open questions 5 and 8 already flag it
  from reading Commonplace's own review pipeline, not from automated-science
  literature: apply and compare need a shared case, and most of what
  Commonplace compares a theory against is a quality criterion, not an
  observation — "the empirical loop is missing from the machinery."
- [Theory refinement may improve sample efficiency under structured
  shifts](../../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  already lists the required capabilities for reasoning about theories as
  "constructing candidates, deriving consequences, identifying assumptions,
  comparing explanations, **seeking discriminating evidence**, and revising
  content or scope" — an established note, not a new architectural claim.

ChatGPT's message is a third, independent route to the same finding. That is
reasonable confirmation the gap is real. It is not evidence that its proposed
outer-ontology framing is the way to close it, since the KB's own framing
already covers the same ground more precisely.

## An architecture for the missing step already sits in the KB, ingested and critiqued

[Model Discovery Agent](../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md)
(MDA) is an instance of exactly the split ChatGPT describes: an LLM proposes
mechanisms, sequential Monte Carlo maintains the structure and parameter
posterior, and Bayesian value-of-information selects the next experiment to
discriminate between the currently live candidates. Its documented limits
matter as much as its architecture: it operates inside a fixed domain
decomposition (grammar, intervention space, likelihood family, and objective
all supplied in advance) and does not establish open-ended discovery; a
misspecified observation model can make value-of-information confidently
select the wrong mechanism even when the true one is in the candidate pool.
[FALSIFYBENCH](../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md)
independently supports the same shape of claim from rule-discovery games:
falsification-seeking probe choice, not confirmation-seeking choice, predicts
success.

Two things follow. First, the KB does not need fresh "automated-scientist"
vocabulary from outside — an instance of the pattern is already a cited,
critiqued source here, which is the grounding a load-bearing claim needs under
this KB's own writing conventions (never invent precision; name the mechanism
and its scope). Second, MDA's own limitation is the one this workshop most
needs to keep in view: an inquiry-selection operation built by copying MDA's
split risks the same thing MDA has — a value-of-information procedure that
chooses well only among moves its supplied grammar already anticipates.
Open-endedness, as `theory-builder.md` already defines it (machinery
acquisition reach for theory families not anticipated in advance), is exactly
the condition a fixed decomposition violates.

## Proposed change

Add a sixth operation to the interface in `theory-refinement-interface.md`
(or wherever it settles once reconciled with the classical literature),
preceding Derive:

| Operation | Question it answers |
|---|---|
| **Inquire** | Among the cases available or constructible, which would most discriminate between the theory's currently live rivals, and how is it obtained? |

Naming and placement notes:

- **Inquire** folds selection and obtaining into one operation-level
  question, matching how the existing five operations are each one judgment,
  not sub-decomposed into search and execution. MDA's own split bundles
  computing value-of-information with executing the query for the same
  reason.
- Not "experiment": most of what Commonplace's own profile table
  (`theory-refinement-interface.md`, "Commonplace as the interpreted
  implementation") reviews a theory against is a criterion, not a lab
  intervention. Inquire needs to cover choosing which note to compare
  against or which validator to add, as much as choosing a physical
  experiment.
- Do not adopt ChatGPT's outer/inner ontology framing as a second container
  next to `theory-builder.md`'s existing development/refinement split or
  next to discovery-lifecycle's phases. Either would duplicate an existing
  distinction under a new name — the storage-without-consumption pattern
  the interface document's own open question 7 already warns against.

## What this does not settle

- Whether Inquire belongs inside theory refinement's definition or is a
  builder-level operation that surrounds refinement is still open. This is
  the interface document's open question 5 (where apply belongs) one
  operation over. Current lean: beside the interface, not inside it —
  `theory-refinement.md` already excludes application, and choosing which
  case produces a comparison looks like the same kind of exclusion.
- What "discriminate between rivals" requires when only one theory is live,
  not several, is untested by MDA (its benchmarks retain multiple candidates
  by construction) and not addressed by FALSIFYBENCH either.
- Whether Commonplace's own review pipeline already performs a degenerate
  form of Inquire — choosing which criterion or neighboring note to check a
  claim against — or whether that choice is currently fixed by task framing
  rather than by the theory, needs the same interpreted-implementation audit
  `theory-refinement-interface.md` already ran for the other five
  operations.

## What I would not import from ChatGPT's message

Its reflection definition — "a theory builder whose possible subjects include
its own theory-building organization" — drops the causal-connection
requirement `reflective-theory-builder.md` already carries: the self-theory
must be able to change the machinery, not merely describe it. That
requirement is load-bearing; it is what excludes a builder that holds a
description of itself and consults it without being able to act on it.
Nothing in the inquiry-selection gap bears on that requirement, so this
document does not propose changing it.

---

Relevant Notes:

- [Theory refinement as an interface](./theory-refinement-interface.md) —
  extends: the five-operation table this document proposes to extend, and
  the open questions this document resolves or narrows
- [Theory builder](./theory-builder.md) — grounds: the development/refinement
  split this document declines to duplicate with a second outer/inner nesting
- [Reflective theory builder](./reflective-theory-builder.md) — contrasts:
  the causal-connection requirement this document does not propose loosening
- [Discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) —
  grounds: the outer ontology already in place, and the phase whose internal
  decomposition this document supplies
- [Theory refinement may improve sample efficiency under structured
  shifts](../../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  — evidenced-by: already names "seeking discriminating evidence" as a
  required capability, independently of this conversation
- [Model Discovery Agent](../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md)
  — evidenced-by: a cited, critiqued instance of proposal/update/selection
  split, with its fixed-decomposition limit
- [FALSIFYBENCH](../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md)
  — evidenced-by: falsification-seeking probe choice predicts rule-discovery
  success
