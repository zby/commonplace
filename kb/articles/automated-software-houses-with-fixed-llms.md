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
theory*: its capacity to relate the software to its purpose, explain its
organization, and handle new demands. An *explicit project theory* is one
possible written carrier of that understanding.

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
The tenant identifier can enter the data model in several ways. More than one
choice may pass the current tests, while only some preserve the assumptions
on which later changes depend.

Computer scientist Peter Naur called the understanding needed to choose and
revise such designs a program theory. We use coherent modification across
later demands as its main behavioural test. [Holding a program theory means
sustaining coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md):
the first choice may be tentative, but the process must use program theory to
guide search, interpret failure, backtrack, and recover when
later consequences arrive.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
reports that full code, annotations, extensive design discussion, and personal
advice did not give one successor team enough program theory. The case
therefore rules out only a simple answer in which more documentation of the
same kind automatically transfers that program theory. It
tested [one historically bounded document package and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).
It did not test linked rationale, machine-maintained indexes, semantic
retrieval, dependency-aware context assembly, or automatic loading of the
relevant material at the decision point.

One inference from Naur's argument to a human-only conclusion depends on
treating machine execution as execution of explicitly formulated criteria.
An LLM is still formal computation, but it can interpret a paragraph about
why retry logic belongs in the caller without that judgment first being
reduced to a complete rule. [Formal execution and explicitly formulated
criteria are not the same
thing](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
A successful house would show that a system made of computational components
can perform the program-theory function defined here. It would refute that
inference to a human-only conclusion, but would not settle Naur's separate
claim that the relevant judgment cannot be reduced to a finite set of
formulated criteria.

## How the components could perform the program-theory function

The conjectured house combines three kinds of component:

- Fixed LLMs supply general linguistic, programming, and reasoning capacity.
  They interpret the current request and the project state and produce
  candidate judgments and changes.
- Natural-language project state supplies persistent purposes, commitments,
  explanations, evidence, and prior decisions. For example: "installs must
  remain a single file, so the store is SQLite; do not add a server
  dependency."
- Symbolic software supplies exact behaviour and continuity. This includes
  the product, tools, schemas, tests, context assembly, schedulers,
  validators, rollback, and retention rules.

None of these holds the program theory alone. A note nobody loads has no
effect. A fixed LLM without enough project state reconstructs or guesses the
program theory instead of preserving it from one change to the next. Software
executes a decision without supplying all the judgment that selected it. The
house as a whole has to perform the program-theory function.

The house may use an explicit project theory, reconstruct its understanding
from records, or combine both. What matters is causal use: the project-specific
state must change proposal, evaluation, diagnosis, or recovery, including
where the relevant implication is not stated verbatim.

## The witness run

The house may begin from a state constructed by people. That state may
include the product, project-specific purposes and rationale, tools, tests,
evaluators, workflows, context assembly, safety boundaries, and other
production machinery. The witness tests operation from that seed, not its
discovery or outgrowth.

For a witness run, every eligible model version and every other learned
component is declared and pinned before testing. This includes model weights,
adapters, embedding models, learned routers, learned critics, and similar
components. A provider endpoint that may change silently is not enough unless
its model lineage can be audited for the run.

The cutoff applies only to a run intended to establish the claim; ordinary
development may use newer models. In a witness run, however, a newer model
must not supply trial-specific program theory, diagnose internal failures,
compare candidates, select successors, or fill any other internal production
role.

The product and the house's natural-language and symbolic state may change.
The house may edit its explicit project theory, code, tests, tools, evaluators,
workflows, context assembly, or its own production machinery. Derived indexes
may be regenerated mechanically from that mutable canonical state under
algorithms pinned before the run; they are not an independent learned update.

The operational loop can therefore have this shape:

```text
request + operating evidence + current product and project state
  -> fixed learned components + current production machinery
  -> changed product and, where needed, changed project state or machinery
  -> later request
```

Once the witness run starts, every internal decision and successor state must
come from the house's current state, its fixed learned components, and the
permitted external inputs. A human intervention in an internal production role
ends that witness run. This provenance requirement is developed in the
[transition-closure supplement](./reachability-as-closure-under-the-seed-gate.md).

Pinning is an experimental condition, not a recommendation for a mature
software house or a claim that updates outside model weights are generally
better than weight updates. It isolates whether the system around current
models can perform every software-house function without help from a
newer or newly trained model.

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

Storing or citing a rationale is
insufficient if it does not govern a later decision. A gate that can reject is
insufficient if the accepted successor is not adequate. Passing tests on one
requested change is insufficient if the house cannot preserve coherence
across later demands.

## Support from existing constructions

Two reported constructions make parts of the conjecture concrete.
[OpenAI's agent-first product account](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
describes five months of product development with agent-generated code,
repository-local project knowledge, and automated checks and cleanup. People
still supplied internal design and production judgments. It supports the
possibility of sustained product development by agents within a human-agent
house. The [Darwin Gödel Machine paper](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
reports improved coding-benchmark performance through search over retained
agent code around frozen foundation models. It supports computational revision
of production machinery without model-weight updates, within a bounded
benchmark setting.

These reports give reasons to attempt the proposed composition. They do not
show autonomous program theory across later product changes. The
[comparison supplement](./nearest-existing-constructions-to-a-reachability-witness.md)
maps these and other constructions against the witness conditions, separating
code-inspected mechanisms from paper and practitioner reports. No reviewed
construction demonstrates all the conditions together. Whether the separate
capacities compose into a reliable automated house remains the conjecture.

## A formal contrast

The fully formal contrast is AI researcher Jürgen Schmidhuber's [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md),
a proof-governed construction that can rewrite its own code. The construction
allows interaction with an external environment, but the paper does not
demonstrate a software house meeting the witness conditions here.
An embedded prover admits a rewrite only after proving, from the current
axioms and formal utility function, that switching pays. Its starting
formalization is supplied in advance, which the conjecture stated here
allows. The limitation is that it "must ignore those self-improvements whose
effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), §2.4,
verbatim).

At the level of state-transition provenance, both systems obey the same
transition-closure condition: every next state must arise through the current
state's machinery and permitted inputs. Their system boundaries and successor
relations still differ. The Gödel machine admits only a
proof-licensed successor. The house can make a change that may be wrong,
observe later consequences, and recover. A novel demand can affect the Gödel
machine's rewrite only when and to the extent that its formalization gives that
demand utility-relevant meaning. The house instead relies on model
interpretation, available checks, and later exposure.

## Future work: testing whether a house holds a program theory

A proposed experiment would follow one maintained product under a predeclared
process that can generate new requirements and operating consequences. In the
multi-tenant example, the initial design could assume that each account
belongs to one tenant. A later request for consultants to work across customer
organizations with one login would test whether the house recognizes and
revises that assumption, changes the product and relevant project state, and
preserves tenant isolation across subsequent changes. The starting rationale
may be human-written; every internal production decision during the run must
be computational.

At selected decisions, matched runs would withhold or replace relevant retained
project state while holding models, product code, tools, demands, and budget
fixed. Predicted differences in proposal, diagnosis, or recovery would test
that state's causal contribution. An intervention on [explicit retained theory
tests that particular component](../notes/retained-theory-intervention-isolates-one-explicit-surface.md);
other records may encode the same understanding. The full experiment must also
show coherent revision and reliable continuation under the witness conditions.
It remains future work. Whether explicit project theory makes learning more
sample-efficient is a separate hypothesis in the
[training article](./the-software-house-as-the-unit-of-training.md#testable-hypotheses).

## Boundaries, evidence, and uncertainty

The scope, request process, horizon, resource budget, and success threshold
are declared before testing so they cannot be narrowed after a failure.

The request process's allowed histories, the history realized in one run, and
the probability or selection procedure over histories are distinct. Fix the
allowed set and selection procedure before the run. Repeated
runs or another justified estimate must show that adequate operation receives
usable probability and persists across the declared horizon.

The need for a program theory is a theoretical argument, not a proved
theorem. That current LLMs can participate in a system performing that
function, and that such a system is practically reachable, remain conjectures.
A working house establishes the claim only over its declared regime. Failure
of an architecture rules out only that architecture, not every possible
construction.

The [training article](./the-software-house-as-the-unit-of-training.md) asks
how such a house should improve once it exists. The [bootstrap
article](./bootstrapping-the-first-automated-software-house.md) asks how to
reach it from a house that still has people in internal production roles,
including how the house might learn to build the project-specific machinery
that its starting state may inherit from people.
