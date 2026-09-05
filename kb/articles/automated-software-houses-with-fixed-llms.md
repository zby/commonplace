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
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
  - kb/sources/goedel-machines-schmidhuber.ingest.md
  - kb/sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md
  - kb/sources/programming-as-theory-building.ingest.md
---
# The Automated Software House Conjecture

*Open-ended software development with fixed LLMs*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A *software house* is the complete persistent system that keeps
changing software for its users. We conjecture that, within at least one
declared product scope, it can sustain coherent change for relevant requests
not listed in advance while computation performs every production decision.
Its LLMs and other learned components stay fixed; its product, retained
knowledge, and production machinery may change. The house may begin from a
human-built seed.

The central test is whether the house can apply and revise its *program
theory*: its understanding of the software's purpose, organization, and how to
handle new demands. An *explicit project theory* is one possible written
carrier of that understanding.

## Claim

**The automated software house conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) capable of open-ended coherent
software change is practically reachable using only LLMs and other learned
components available by 2026-09-02 and held fixed during the run.

*Practically reachable* means that the house succeeds within a product scope,
request-generating process, operating horizon, and budget of compute, time,
and cost declared before the run. *Open-ended* means that the declared
process can produce relevant requests and consequences that were not listed
one by one in advance. It does not mean that one house must handle every
possible software product or request.

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

An automated software house has no human in an internal production role over
its declared scope and horizon.

## Why the claim is not trivial

Open-ended change brings questions that available checks do not settle. Say a
product built for one customer per deployment must now serve many tenants.
Several designs for representing tenant identity may pass the current tests,
while only some preserve the assumptions on which later changes depend.

Computer scientist Peter Naur called the understanding needed to choose and
revise such designs a program theory. Coherent modification across later
demands is its main behavioural test here. The proposed mechanism is that
project-specific commitments constrain changes, direct diagnosis, and identify
what recovery must preserve. Separating a person's identity from organizational
membership suggests where to revise the model; tenant isolation states what
must survive. These commitments could [keep search coherent until delayed
evidence arrives](../notes/program-theory-sustains-search-under-delayed-feedback.md).
Success tests the capacity; intervening on the commitments tests this proposed
explanation of how the house achieves it.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
reports that full code, annotations, extensive design discussion, and personal
advice did not give one successor team enough program theory. More documentation
of the same kind did not automatically transfer that understanding. But the
case tested [one historically bounded package and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md),
not linked rationale, semantic retrieval, or automatic loading of relevant
material at the decision point.

An inference from Naur's argument to a human-only conclusion treats machine
execution as execution of explicitly formulated criteria. An LLM is formal
computation, yet can interpret an explanation of tenant isolation without
that judgment first being reduced to a complete rule. [Formal execution and
explicitly formulated criteria are different
things](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
A successful computational house would refute that inference to a human-only
conclusion. It would not settle Naur's separate claim that the relevant
judgment cannot be reduced to a finite set of formulated criteria.

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

The components must work together. An unloaded note has no effect; a model
without enough project state must reconstruct or guess missing understanding;
software executes a decision without supplying all the judgment that selected
it. The house may retain an explicit project theory, reconstruct understanding
from records, or combine both. What matters is causal use: project-specific
state changes proposal, evaluation, diagnosis, or recovery, including where
the relevant implication is not stated verbatim.

## The witness run

The human-built seed may include the product, purposes and rationale, tools,
tests, evaluators, workflows, context assembly, and safety boundaries. The
witness tests operation from that seed, not its discovery or outgrowth.

Declare and pin every eligible learned component before testing, including
model weights, adapters, embedding models, routers, and critics. A provider
endpoint that may change silently is insufficient unless its model lineage can
be audited. The cutoff applies to witness runs; ordinary development may use
newer models. During a witness, no newer model may supply trial-specific theory,
diagnosis, candidate comparison, successor selection, or another internal
production decision.

The product and natural-language and symbolic state may change, including the
house's tests, evaluators, workflows, and update machinery. Derived indexes may
be regenerated from mutable canonical state under pinned algorithms and
embedding models; this is not an independent learned update.

The loop can have this shape:

```text
request + operating evidence + current product and project state
  -> fixed learned components + current production machinery
  -> changed product and, where needed, changed project state or machinery
  -> later request
```

Every internal decision and successor must come from the current house,
its fixed learned components, and permitted external inputs. An internal human
intervention ends the witness. The [transition-closure
supplement](./reachability-as-closure-under-the-seed-gate.md) develops this
provenance requirement.

Pinning isolates whether the system around current models can perform every
software-house function. It is an experimental condition, not a recommendation
for mature houses or a claim that updates outside weights are generally better.

## What a witness house must show

One witness house must show all the following conditions together.

1. **Holding and application.** Across novel changes, the house uses
   program theory to guide proposal, evaluation, diagnosis,
   or recovery, including cases whose correct handling is not stated verbatim
   in its retained state. With everything else held equal, withholding or
   replacing the relevant state changes what the house does next in a
   predicted way.
2. **Coherent revision.** When a later request or operating consequence
   exposes an inadequacy in the current program theory, the house
   revises the product, retained project state, production machinery, or a
   combination, and the successor supports coherent later modification.
3. **Automated continuation.** The house sustains those capacities across the
   declared scope and horizon while satisfying the boundary above.
4. **Practical reliability.** The declared evaluation must show useful
   success within the resource budget and continued adequacy across the
   horizon. A single successful sequence may result from chance and establishes
   only possibility, not practical reachability.

## Future work: testing whether a house holds a program theory

A proposed experiment would follow one maintained product under a declared
process generating new requirements and operating consequences. A demanding
workload would require revising an architectural assumption, expose
consequences after intervening changes, and continue maintenance afterward.
These challenge choices preserve the existential claim while testing more than
unlisted parameter variations within an anticipated design.

In the tenant example, suppose each account initially belongs to one tenant.
A later request lets consultants work across customer organizations with one
login. The house must revise that assumption, change the product and relevant
project state, and preserve tenant isolation through subsequent changes.

At selected decisions, matched runs would vary retained project state while
holding models, code, tools, demands, and budget fixed. Predicted differences
in proposal, diagnosis, or recovery would test its causal contribution. An
[intervention on explicit retained
theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
is local to that component: other records may encode the same understanding,
and an effect alone need not distinguish explanatory guidance from extra
information or instruction following.

The [training article's component
experiment](./the-software-house-as-the-unit-of-training.md#testable-hypotheses)
addresses that distinction with theory, descriptive, raw-record, and
wrong-theory treatments across changes that preserve or break assumptions.
It can test a learning hypothesis before a fully automated house exists.
The full witness additionally requires coherent revision and reliable
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
is a formal construction that can rewrite its own code. Its embedded prover
admits a rewrite only after proving, from the current axioms and formal utility
function, that switching pays. The starting formalization is supplied in
advance, as the conjecture allows. Its limit is that it "must ignore those
self-improvements whose effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), §2.4, verbatim).

Both systems require each successor to arise through current machinery and
permitted inputs. Their update policies differ: the Gödel machine requires a
proof, while the proposed house can make a fallible change, observe its
consequences, and recover. External demands affect a Gödel-machine rewrite only
as its formalization gives them utility-relevant meaning. The house relies on
model interpretation, available checks, and later exposure. The Gödel-machine
paper does not demonstrate a software house meeting the witness conditions.

## Boundaries, evidence, and uncertainty

Declare the scope, request process, horizon, resource budget, and success
threshold before testing to prevent narrowing them after failure. Distinguish
the allowed histories, the history realized in a run, and the selection
procedure over histories. Fix the allowed set and selection procedure in
advance; use repeated runs or another justified estimate to assess success
across the horizon.

The need for program theory is a theoretical argument, not a proved theorem.
Whether current LLMs can participate in a practically reachable system that
performs this function remains conjectural. A working house establishes the
claim only over its declared regime; a failed architecture rules out only that
construction.

The [training article](./the-software-house-as-the-unit-of-training.md) asks
how such a house should improve. The [bootstrap
article](./bootstrapping-the-first-automated-software-house.md) asks how to
reach it from human-agent production, including how it might learn to build
machinery that its seed may inherit from people.
