---
description: "Specification, checking, permitted interpretations, repeated-use cost, and the stake set against a pattern's stated odds and exposure inform which operations to codify; none alone makes code or model interpretation universally preferable"
type: types/note.md
traits: [synthesis]
tags: [learning-theory, constraining, computational-model]
---

# Codify-versus-LLM decision heuristics

The choice is between assigning an operation to a symbolic consumer and asking
a model to interpret it at use time. [Code and model-mediated
operations](./code-complements-weight-prompt-with-symbolic-operations.md) can
both participate in a learned procedure. A useful decision compares their
reliability, total cost, and ability to accommodate the changes that matter.

Four lenses help locate the tradeoff. They are questions to investigate, not
independent rules that determine one correct allocation.

## Specification: what does exact execution establish?

An explicit specification can make conformance checkable. It does not follow
that the specification captures the external objective. [Exact implementation
does not validate a requirement](./exact-implementation-does-not-validate-a-requirement.md).

A dependency traversal can execute exactly while its account of the build's
inputs is incomplete. Leaving that same account to a model does not repair the
missing dependency automatically. The house needs evidence against the account
and a revision to whichever component embodies it.

A theory-based operation is therefore not automatically unsuitable for code.
A fallible account can motivate a versioned validator, and later evidence can
revise both. The question is whether its specified portion is useful enough to
execute without fresh interpretation and whether errors remain detectable.

## Checking: what can reject a wrong result?

The [oracle-strength comparison](./oracle-strength-spectrum.md) asks what
evidence is available and what it costs. Schema checks can test specified
structural properties. Tests cover the cases or properties they actually
exercise; their existence does not establish complete semantic correctness.
Delayed consequences can expose failures that immediate checks miss.

Strong checks help assess both generated code and model outputs. Weak checks
do not make an LLM-plus-human path automatically reliable, and a precise
specification does not guarantee cheap verification. [The verification
boundary](./the-boundary-of-automation-is-the-boundary-of-verification.md)
concerns warranted acceptance, not an intrinsic inability to produce a correct
unchecked result.

## Interpretation: must one output be selected in advance?

An underspecified request can admit many valid results. That does not rule out
symbolic execution. An algorithm may return any result satisfying a relation,
search among alternatives, or use a declared random choice. Codification does
not require a unique output or a single permanently fixed answer.

What is assigned is the operation's behaviour under its implemented rules.
The risk is committing to an inadequate selection or search procedure. A model
may be useful where new cases require semantic judgments those rules do not
cover. It may also be called from an otherwise symbolic procedure. [Process
and output constraints](./process-structure-and-output-structure-are-independent-levers.md)
are separate: neither “codify what, not how” nor its reverse is a general rule.

## Repetition: is a reusable procedure worth its cost?

Repeated reconstruction creates an opportunity to retain a procedure.
[Spec mining](./spec-mining-as-codification.md) can identify recurring behaviour
and test whether a reusable implementation improves later work. But recurrence
can also preserve a repeated mistake. It is a cost signal and a source of
candidates, not a correctness criterion.

A sound operation can be worth implementing after one informative case.
Another may remain cheaper to interpret even after many cases because its
premises change frequently. Compare construction, invocation, checking,
retrieval, and maintenance costs under the same outcome requirements.

[Artifact lifetime](./ephemeral-computation-prevents-accumulation.md) is a
separate choice. Temporary code is symbolic while it runs. A persistent
natural-language procedure can retain learning despite repeated model
interpretation. Leaving an operation model-mediated does not mean the system
cannot learn across runs.

## Stake and odds: how much to build on an uncertain pattern

The repetition comparison above prices a conversion that is assumed to
hold. A conversion is also a bet that the extracted pattern is part of the
task rather than an accident of the observed cases
([codification is a bet](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)).
Two further terms follow from treating it as one, and the KB's own record
shows decisions that went wrong for lack of them.

**Size the stake to the stated odds.** Recurrence and saving per use decide
what is won if the pattern holds; construction cost, carrying cost (the
maintenance and later removal that [entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md)
adds) and exposure decide what is lost if it does not. When a record states
at decision time that the pattern's stability is low, the construction
should be small. The artifact-run engine was adopted as a bridge under an
expectation its own proposal called "not an observed fact", with the intent
to keep it "as small as possible, because it is the part expected to be
discarded"; it was built at about 3,000 lines serving its state model
against 1,000 of domain logic and retired ten days later on the condition
the proposal had named
([ADR 113](../reference/adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md),
[ADR 118](../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md)).
The repetition comparison alone does not catch this, because the costs it
compares are all conditional on the routine holding.

**Exposure is a term the designer controls.** Exposure is what a wrong
routine costs before its failure is noticed, beyond the cost of removing it.
It is bounded by what depends on the routine, and that bound can be set
independently of stability. That is how a low-stability conversion can
still pay: the `complete` mark of
[ADR 026](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md)
was expected to drift and was made "an accelerator, never a load-bearing
wall", so no consumer's correctness depended on it. Its exposure was
bounded rather than zero: a stale mark suppresses the by-tag search in
consumers that skip it until someone drops the mark. The same ADR's
`covered_by` mark had no consumer and was built with "adoption deferred to
the first real case"; it was dropped twice by its one adopter and retired.
Both decisions were assessable from the ADR's own text. Before recurrence is
observed, bound construction cost and downstream loss against the
anticipated benefit; this is the rule
[ADR 040](../reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md)
applies to scripts, stated so that it covers types and engines. The cases
do not show that zero exposure is necessary; an anticipated benefit can
justify a bounded, nonzero exposure.

Every term here is a forecast. Stability is the one about the pattern
itself rather than a quantity, and the one that
[observing across runs](./progressive-constraining-commits-only-after-patterns-stabilize.md)
or an explanation of why the pattern holds improves; which of those two does
more is not settled here.

## Mixed implementations and revision

A check selector can combine symbolic dependency traversal with model judgment
about a new kind of consumer. The traversal avoids repeated bookkeeping;
the judgment handles a case the current procedure does not settle. Either part
can be revised when evidence exposes an inadequacy.

The [deterministic-validation note](./deterministic-validation-should-be-a-script.md)
gives a bounded example: structural frontmatter and link checks have defined
consumers, while judgments about a description's usefulness require a different
assessment. This does not establish that every semantic judgment must remain
model-mediated forever.

A codified operation is a [relaxation
candidate](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)
when its assumptions repeatedly fail or its maintenance cost exceeds an
adequate alternative. Growing exceptions and integration failures are prompts
to diagnose the cause, not proof that code is the wrong carrier. The repair may
be a better symbolic procedure, more flexible interpretation, or a revised
representation shared by both.

## Scope

These heuristics guide a comparative design decision; they do not prove a
universal preference for code or models. A [fixed-model house](./a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md)
needs new machinery when its current operations are inadequate under the
required reliability and budget. Existing general machinery may already
supply what a new theory needs.

A useful comparison must allow both alternatives competent implementations.
If the model path retains instructions, examples, and tests, count their costs
and benefits. If the code path uses configurable rules or model calls, assess
those actual operations rather than treating code as an inflexible baseline.

---

Relevant Notes:

- [Code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) — grounds: defines the operation-level comparison
- [Exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md) — grounds: distinguishes conformance from objective fit
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — grounds: compares available checking evidence
- [Codification](./definitions/codification.md) — defined-in: names the crossing to symbolic consumption
- [Discarding all experience-dependent state prevents cross-run accumulation](./ephemeral-computation-prevents-accumulation.md) — contrasts: execution form does not decide whether learning persists
- [A fixed-model house must retain missing procedures for theory use](./a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md) — extends: connects the allocation decision to learning new theory-use capacity
- [Current-task fit alone does not warrant costly entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — grounds: supplies the carrying-cost side of the stake, where adoption raises later removal cost
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: observation across runs as the way the stability forecast is improved before construction
- [ADR 026: tag-readme type with completeness and coverage marks](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidenced-by: a bounded-exposure conversion that held under expected drift, and a built-ahead-of-need mark that was retired
- [ADR 118: analyses run as a workflow over headless harnesses](../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md) — evidenced-by: a conversion whose construction exceeded its stated odds and was retired on the condition its proposal named
