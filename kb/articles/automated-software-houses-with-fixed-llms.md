---
description: "Conjecture that an automated software house can sustain open-ended coherent software change with LLMs available by 2026-09-02 and held fixed; system boundary, components that perform the program-theory function, and witness conditions"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/code-complements-weight-prompt-with-symbolic-operations.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
---
# The Automated Software House Conjecture

*Open-ended software development with fixed LLMs*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A *software house* is the complete persistent system that keeps
changing software for its users. We conjecture that an automated software
house is possible with today's LLM weights: a house in which computation
performs every production decision can sustain coherent change as
requirements and operating conditions develop, using only LLMs and other
distributed-parametric models available by 2026-09-02 and held fixed. The
house learns by revising its retained knowledge and production machinery,
not its models, and may begin from a human-built seed.

The central test is whether the house can apply and revise its *program
theory*: its understanding of the software's purpose, organization, and how to
handle new requests. An *explicit project theory* is one possible written
carrier of that understanding: an account of design commitments, causal
assumptions, and invariants. Possessing the account does not establish that the
house can use it.

## Claim

**The automated software house conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) capable of open-ended coherent
software change can operate practically using only LLMs and other
[distributed-parametric](../notes/definitions/representational-form.md) models
available by 2026-09-02, the cutoff chosen for this conjecture, and held fixed
during the run.

*Operates practically* means that the house, started from a declared seed,
sustains adequate performance over a stated horizon within a stated resource
budget, reliably rather than by chance. For an evaluation, adequate performance
means applying program theory, revising coherently, and continuing automatically
on the work being assessed. The four conditions below specify these capacities
and the evidence needed for their reliability. The seed may be human-built; how it is
reached from human-agent production is the bootstrap article's question.
Report the resources used to build the seed separately from the operating
budget.

*Open-ended* means that the house handles whatever reasonable requests and
consequences arise as development continues, without their being listed in
advance, including requests that change what the house is responsible for.
*Reasonable* is left informal. Some programs cannot be produced at all, and
others not within the available budget; those do not count against the house.
The working standard is comparative: given the same requests and resources,
the house should do at least as well as a *human-agent house*, one with
people in its internal production roles.

A *witness* is a concrete example that establishes an existence claim. Here a
**witness house** would establish the conjecture by meeting its four conditions.
A **witness run** is an attempt to demonstrate them; its **witness protocol**
specifies the conditions and evaluation procedure before testing.

## The boundary

An *internal production role* is work the house depends on to develop and
evolve the software, whoever performs it. Internal production roles include
interpreting project knowledge, making implementation decisions, diagnosing
failures, comparing candidates, revising project state or production
machinery, and choosing which revision takes effect.

Users remain outside the house when they provide product requirements, domain
facts, preferences, observed outcomes, or acceptance judgments about visible
behaviour. A user crosses into an internal production role when asked to
diagnose an implementation failure, choose among internal designs, supply a
missing project-specific design decision, or select the retained successor.
The role, not the person's identity, decides which side of the boundary an act
falls on.

An automated software house performs every internal production role
computationally. A witness run must maintain that boundary throughout the
observed operation; people may build the seed beforehand.

## Why the claim is not trivial

Open-ended change brings questions that available checks do not settle. Say a
product built for one customer per deployment must now serve many tenants.
Several designs for representing tenant identity may pass the current tests,
while only some preserve the assumptions on which later changes depend.

Computer scientist Peter Naur called the understanding needed to choose among
such designs, and to revise them later, a *program theory*. In this article its
main behavioural test is coherent modification: later requests are handled in
ways that fit the earlier design.

How would a house achieve that? The proposed mechanism is that retained
project-specific commitments do three jobs: they rule out changes that break
the design, they point diagnosis at the likely cause, and they say what a
recovery must preserve. In the tenant example, the commitment that a person's
identity is separate from their organizational membership shows where the data
model has to change; the commitment to tenant isolation says what every change
must keep true. Commitments like these could [keep the house's search for a
design coherent while the consequences of a choice are still
unknown](../notes/program-theory-sustains-search-under-delayed-feedback.md).
Passing the test shows that the house has the capacity. Changing the
commitments and observing what the house does next tests whether this
mechanism explains it.

Naur's thesis is that only people can hold a program theory. His evidence
for it is that documentation did not pass the theory to new programmers. Both
bear on the conjecture.

The evidence bears on the mechanism. [Naur's compiler
case](../sources/programming-as-theory-building.ingest.md) reports that full
code, annotations, extensive design discussion, and personal advice did not
give a successor team enough program theory, and that more documentation of
the same kind did not help. If that generalizes, the retained commitments
above would be inert. But the case tested [one historically bounded package
and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md),
not linked rationale, semantic retrieval, or automatic loading of relevant
material at the decision point. Whether those transfer more remains open.

The thesis, if true, rules out the conjecture: computation could not
fill every production role. Naur's argument reaches it only by treating
machine execution as executing explicitly formulated criteria. [Formal
execution and explicitly formulated criteria are different
things](../notes/naur-equates-machine-execution-with-formulated-criteria.md):
an LLM is formal computation, yet it can act on an explanation of tenant
isolation without that judgment first being reduced to a complete rule. A
working computational house would show that a program can make this judgment,
refuting the human-only thesis. It would not show that the judgment can be
written as rules. An LLM's judgment has no formulated criteria either, so
Naur's claim that the criteria cannot be formulated would stand.

## How the components could perform the program-theory function

The conjectured house combines three kinds of component:

- **Fixed LLMs** interpret requests and project state, then propose judgments
  and changes using general linguistic, programming, and reasoning capacity.
- **Natural-language project state** retains purposes, commitments,
  explanations, evidence, and decisions. For example: "tenant isolation protects
  each customer's data; every query must respect the active tenant."
- **Symbolic software** supplies exact behaviour and continuity through the
  product, tools, schemas, tests, context assembly, scheduling, validation,
  rollback, and retention rules.

No component holds the program theory alone. A note that is never loaded has
no effect. A model without enough project state must reconstruct or guess the
missing understanding. Software executes a decision without supplying all the
judgment that selected it.

Nor does the conjecture fix which form carries the theory. The house may
retain an explicit project theory, reconstruct understanding from records
each time, or combine both. What matters is causal use: project-specific
state changes proposal, evaluation, diagnosis, or recovery, including where
the relevant implication is not stated verbatim.

## The witness run

The human-built seed may include the product, purposes and rationale, tools,
tests, evaluators, workflows, context assembly, and safety boundaries. The
witness run tests operation from that seed. Learning to construct machinery
that the seed may inherit is the separate question of the training article.

Declare every eligible distributed-parametric model and pin its parameters,
including adapters, before testing. This covers LLMs, embedding models, and
parametric routers and critics. A provider endpoint that may change silently
is insufficient unless its model lineage can be audited. The cutoff binds only
witness runs; ordinary development may use newer models. During a witness run,
no newer model may supply run-specific theory, diagnosis, candidate
comparison, successor selection, or another internal production decision.

The house may learn by changing its natural-language and symbolic state,
including tests, evaluators, workflows, and update machinery. Its product may
also change. Derived indexes may
be regenerated from mutable canonical state under pinned algorithms and
embedding models; this is not an independent learned update.

The loop can have this shape:

```text
request + operating evidence + current product and project state
  -> fixed distributed-parametric models + current production machinery
  -> changed product and, where needed, changed project state or machinery
  -> later request
```

Every internal decision and successor must come from the current house,
its fixed distributed-parametric models, and permitted external inputs. An internal human
intervention ends the witness run. The [transition-closure
supplement](./transition-closure-and-continuation-reliability.md) develops this
provenance requirement.

Pinning rules out model-parameter updates as the source of improvement during
the run. It isolates one variable and proves nothing on its own: whether the
house performs every software-house function is what the rest of the
evaluation must show. Pinning is an experimental condition, not a
recommendation for mature houses or a claim that updates outside weights are
generally better.

## What a witness house must show

One witness house must show all the following conditions together. Each needs
positive evidence: a run that never challenges an assumption cannot establish
coherent revision merely because nothing went wrong.

1. **Holding and application.** Across novel changes, the house uses
   program theory to guide proposal, evaluation, diagnosis, or recovery,
   including cases whose correct handling is not stated verbatim in its
   retained state. Test causal use through matched interventions on retained
   commitments or on the paths used to reconstruct and consume them: a
   changed commitment or access path must produce a predicted change in the
   house's decisions. Removing one written carrier without changing behaviour
   is inconclusive when other records supply the same understanding; call
   that equivalent reconstruction, and the test must account for it.
2. **Coherent revision.** Later requests or operating consequences expose
   an inadequacy in the current program theory. The house responds by revising
   the product, retained project state, production machinery, or a combination,
   and the successor supports coherent later modification.
3. **Automated continuation.** The house sustains those capacities through
   subsequent requests and consequences without internal human production decisions.
4. **Practical reliability.** The declared evaluation must show that the
   house sustains adequacy across the horizon within the resource budget,
   reliably enough to be useful, with a human-agent house given the same
   requests and resources as the baseline. A single successful sequence may
   result from chance and establishes only possibility, not practical
   operability.

## Future work: testing whether a house holds a program theory

A proposed experiment could start with one maintained product and follow new
requirements and operating consequences. One way to exercise the witness
conditions is to build in an architectural assumption whose consequences
surface only after later changes, then continue maintenance after the house
revises it. The evidence must demonstrate application and revision of program
theory. A stream of requests that vary within the anticipated design, even if
none was listed in advance, does not establish those capacities by itself.

In the tenant example, suppose each account initially belongs to one tenant.
A later request lets consultants work across customer organizations with one
login. The house must revise that assumption, change the product and relevant
project state, and preserve tenant isolation through subsequent changes.

At selected decisions, matched runs would vary retained project state while
holding models, code, tools, requests, and budget fixed. Predicted differences
in proposal, diagnosis, or recovery would test its causal contribution. Such an
[intervention on explicit retained
theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
has two limits. If removing the retained theory changes nothing, that may be
because other records carry the same understanding. If it changes the house's
decisions, that shows the note mattered, but not how: the house may have used
it as an explanation, as extra facts, or as an instruction to follow.

The [training article's component
experiment](./the-software-house-as-the-unit-of-training.md#testable-hypotheses)
addresses that distinction with theory, descriptive, raw-record, and
wrong-theory treatments across changes that preserve or break assumptions.
It can test a learning hypothesis before a fully automated house exists.
The full witness run additionally requires coherent revision and reliable
continuation across all internal roles. Both experiments remain future work.

## Support from existing constructions

Two reports make parts of the conjecture concrete. [OpenAI's agent-first
product account](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
describes five months of development with agent-generated code, repository-local
knowledge, and automated checks and cleanup. People still supplied internal
design and production judgments. It supports sustained agent production within
a human-agent house.

The [Darwin Gödel Machine
paper](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
reports improved coding-benchmark performance through search over retained
agent code around frozen foundation models. It supports computational revision
of production machinery within that benchmark setting.

Neither report demonstrates autonomous program theory across later product
changes. The [comparison
supplement](./nearest-existing-constructions-to-a-reachability-witness.md)
maps eighteen constructions against the witness conditions, separating
code-inspected mechanisms from paper and practitioner reports. None demonstrates
all four conditions together; their reliable composition remains conjectural.

## A formal contrast

Jürgen Schmidhuber's [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is the nearest formal construction that changes itself under the same
provenance requirement as the conjectured house, and the contrast shows what
proof-gated admission costs. The machine can rewrite its own code. Its
embedded prover admits a rewrite only after proving, from the current axioms
and formal utility function, that switching pays. Its starting axioms and
utility function are written by people in advance, as the conjecture's seed
may be. Its limit is that it "must ignore those self-improvements whose
effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), §2.4, verbatim).

Both systems require each successor to arise through current machinery and
permitted inputs. Their update policies differ: the Gödel machine requires a
proof, while the proposed house can make a fallible change, observe its
consequences, and recover. They also differ in how the outside world reaches
an update. A request can influence a Gödel-machine rewrite only if its
formalization already assigns that request a utility; the house instead
interprets the request with its models, checks what it can, and learns the
rest from later consequences. The Gödel-machine paper does not demonstrate a
software house meeting the witness conditions.

## Boundaries, evidence, and uncertainty

The witness protocol must declare the following before testing:

- **Starting system:** seed, mutable state, pinned distributed-parametric models, and
  update procedure, including what that procedure may revise.
- **Boundary and workload:** starting products, permitted external inputs,
  how requests and consequences are selected or generated, and any restrictions
  on their histories. Record how failures, refusals, and excluded cases are counted.
- **Resources:** seed-construction effort, the budget for sustaining
  adequacy, and the operating horizon.
- **Evaluation:** the human-agent baseline and success thresholds for
  sustained adequacy, repetitions or another justified estimation method, and
  the interventions used to test program-theory application.

These declarations govern the evaluation. The input process may respond to the
house's actions and introduce new kinds of work; it need not fix a product
family or enumerate future requests. Keep the selection rules distinct from
the history realized in a run, and retain failures rather than removing them
afterward. The [transition-closure supplement](./transition-closure-and-continuation-reliability.md)
explains how the input process affects possible paths and their probabilities.

The need for program theory is a theoretical argument, not a proved theorem.
Whether current LLMs can participate in a practically operable house that
performs this function remains conjectural. A successful run supplies evidence
for the capacities it exercises under the reported conditions; extending that
conclusion to untested work needs further support. A failed architecture rules
out only that construction.

The [training article](./the-software-house-as-the-unit-of-training.md) asks
how such a house should improve. The [bootstrap
article](./bootstrapping-the-first-automated-software-house.md) asks how to
reach it from human-agent production, including how it might learn to build
machinery that its seed may inherit from people.
