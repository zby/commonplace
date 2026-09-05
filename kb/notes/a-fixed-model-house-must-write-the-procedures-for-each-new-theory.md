---
description: "Retained theory is inert without operations that select, apply, check, and revise it; when weights are pinned those operations cannot be practised into the model, so they have to be retained outside it, and code is where one runs the same way twice"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, self-improving-systems]
---

# A fixed-model house must write the procedures for manipulating each new theory

A retained theory states what is the case: design commitments, causal
assumptions, invariants. Using it is a set of operations the text does not
contain: selecting the fragment that bears on the decision at hand, deriving
this case's consequence, checking a candidate change against it, noticing an
observation that contradicts an assumption, and rewriting the theory when one
does.

Acquiring the theory and acquiring those operations are two different
acquisitions. A [software house](./definitions/software-house.md) that gains
the first without the second holds a text that changes nothing later — and a
text it cannot test, since checking a theory by attempted falsification is
itself an application: deriving what the theory predicts and confronting the
prediction with observations. The derive-and-test steps of the [discovery
lifecycle](./definitions/discovery-lifecycle.md) run on the same operations
as production use.

This split is the one the familiar knowing-that / knowing-how distinction
names, and
this KB already records its cognitive-science version in the [three-space memory
taxonomy](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md),
where procedural content sits in a space of its own. The analogy is doing one
job here: it names a function and a failure mode — knowledge acquired but inert
because the skill for applying it was not acquired alongside it. It does not
argue that the house needs a component called procedural memory, since [human
analogies can motivate functions without determining component
boundaries](./human-analogies-suggest-functions-not-component-boundaries.md).

## Pinning the weights closes the usual path

In a system whose weights can change, the second acquisition can happen without
any artifact naming it. Practice writes into the same substrate that runs the
operations, so a new operation for a new kind of theory can be consolidated
where nothing points at it. Under a fixed-model premise that route is closed by
construction: the pinned model supplies whatever it already does with text on
the spot, and no amount of production adds an operation to it.

What remains are the localized [representational
forms](./definitions/representational-form.md) — natural language and symbolic
artifacts. A procedure the house needs and the model does not already perform
has to be written into one of them and retained, because [the deployed system,
not the model alone, is the unit of
learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md):
retrieval, scheduling, schemas, validators, tests, and tools each perform a step
of theory use, and each is revisable while the weights are not. It cannot be
optimized into place from inside the existing arrangement either, since
[learning inside a fixed decomposition inherits its
mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): an
operation absent from the supplied structure is not reachable by tuning that
structure.

## Where the demand starts

The claim is not that every retained theory obliges new machinery. A fixed
model's generic competence with text covers a wide band of theory use for free:
read a short account, apply it to the case in front of it, spot a plain
contradiction. While a theory's operations stay inside that band, retaining the
text is the whole of the acquisition.

The demand appears where an operation scales with what the theory governs.
Selecting the relevant commitment out of hundreds is a retrieval problem, not a
reading problem. Enumerating every file an invariant reaches is a traversal
problem. Deciding whether a candidate change respects the invariant, on every
change rather than when someone thinks to ask, is a checking problem. Watching
for the observation that would refute an assumption is a monitoring problem.
These are the operations a growing project keeps asking for, and they are the
ones a pinned model will not acquire. A house that can revise its theories but
not its machinery should therefore improve for a while and then stop, at roughly
the scale where its theories outgrow what the model can do with them in one
pass.

## Why the procedure tends toward code

Both localized forms can carry a procedure, and the difference between them is
not whether the procedure is retained but how it executes. A procedure written
as instructions is re-interpreted at each use: the model reconstructs the
operation from the text every time, paying the cost and taking the variance
again, which is [ephemeral computation](./ephemeral-computation-prevents-accumulation.md)
of the operation itself even though the instructions persist. A procedure
written as code is executed by a defined consumer, because [code complements the
weight–prompt pair with independently executed symbolic
operations](./code-complements-weight-prompt-with-symbolic-operations.md): once
installed it runs the same way twice, can be tested against cases, and can be
revised one step at a time.

So the two forms are not interchangeable for this purpose. Written instructions
are the cheap first carrier for a procedure still being worked out; the crossing
into code — [codification](./definitions/codification.md) — is what makes a
theory-manipulation step repeatable and checkable. The pressure to cross grows
with how often the step runs and how much a wrong execution costs. At
sufficient volume the crossing stops being an optimization and becomes the
condition of application: having a model re-interpret the theory for every
change to a large product exceeds any practical budget, so at that scale the
theory is applied only as software.

This is a different argument from the neighbouring [two-layer
arrangement](./theory-and-methodology-form-a-two-layer-execution-system.md),
where a derived methodology is a cheaper fast path for derivations the theory
could still supply the slow way. There the case for building the procedure is
a cost case; here, past the band the model covers for free, the procedure is
what lets the theory reach the decision at all. That is the concrete reason a
house under the pin must be able to write and revise programs, not only
retain text: a text can hold the theory, but it holds a procedure only as a
recipe the model must re-derive at each use.

## What would show this is wrong

The prediction is a signature in the record of retained changes: in a house
whose models stay pinned, theory revisions should be accompanied by revisions to
retrieval, schemas, checks, tools, or scheduling, at a rate that rises as the
theories govern more. A lineage of theory-only revisions that keeps improving
later work while the project grows would refute the claim, and would show
instead that the model's generic competence absorbs the procedure demand at the
scales tested. A single stretch of theory-only improvement does not refute it;
the claim is about what happens as the governed scope grows.

## Scope

- The second half of the claim is conditional on the pin. Where weights can be
  updated, the procedural substrate may be parametric and the argument for
  writing procedures down loses its force; the first half — that using a theory
  takes operations the theory does not contain — does not depend on the pin.
- *Procedure* here covers anything that performs a step of theory use: a
  retrieval path, a schema, a validator, a test, a tool, a scheduling rule, or a
  written instruction. It is not restricted to callable functions.
- Code is not claimed to be the sole carrier. Natural-language instructions
  carry procedures too, and the claim about code is comparative: it is the
  carrier whose consequences are assigned rather than re-interpreted.
- A procedure held only in a context window or a prompt cache is not retained
  state under this argument. It expires, and the next episode starts without it.
- The human knowing-that / knowing-how split motivates the distinction and
  supplies a failure mode to look for. It is not evidence that a fixed-model
  house behaves this way.

## Open Questions

- Which theory-manipulation operations actually exceed a current fixed model's
  in-context competence, and at what project scale? The answer fixes where the
  procedure demand starts, and it moves with model capability.
- Does the demand per theory fall over time? If procedures written for earlier
  theories are general enough to be reused — one retrieval path, one checking
  harness, many theories — the plateau this note predicts is pushed back rather
  than removed, and the interesting quantity becomes the reuse rate.

---

Relevant Notes:

- [Code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) — grounds: supplies the distinction between an operation re-instantiated from a prompt at each use and one whose consequences a runtime assigns
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: establishes that retrieval, tools, and runtime policy are behaviour-determining parts, which is what lets a written procedure count as an acquisition
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: an operation missing from the supplied structure cannot be recovered by optimizing within it, so the procedure must be written rather than tuned into existence
- [An open-domain theory builder becomes a software house when new domains require production-machinery changes](./an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md) — extends: applies the same coupling to a boundary question, concluding that a builder facing new manipulation requirements must bring software development inside its own boundary
- [Treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) — extends: names the coupling this note supplies one mechanism for — why the natural-language and symbolic loops cannot be optimized independently once the parametric one is pinned
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — contrasts: there a derived procedure is a cheaper path to an effect the theory can still produce slowly; here the procedure is what gives the theory any effect on the decision
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — mechanism: explains what a house pays when the operation is rebuilt from instructions at each use instead of installed once
- [Codification](./definitions/codification.md) — defined-in: names the natural-language-to-symbolic crossing a procedure makes when it becomes code
- [Discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: names the derive-and-test path that checking a theory runs on, which this note ties to the same operations as production use
- [Representational form](./definitions/representational-form.md) — defined-in: supplies the three-form classification and the localized pair the pin leaves writable
- [Software house](./definitions/software-house.md) — defined-in: the persistent producer whose retained theory and machinery this claim is about
