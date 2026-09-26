---
description: "Supplement: the automated software house conjecture as an alternative test of theory refinement with fixed models; the 2026-09-02 claim, Naur's program theory, four witness conditions, and the knowledge-base comparison"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/software-house.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md
---
# An Automated Software House as an Alternative Test

*Program theory, the witness conditions, and why software gives a stronger falsifier*

> **Draft supplement.** This develops one alternative arrangement for
> testing the paradigm in [Learning by Theory Refinement with Fixed
> Models](./learning-by-theory-refinement-with-fixed-models.md). It may
> change. Comments and counterexamples are welcome on [the repository's
> GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A *software house* is the complete persistent system that keeps
changing software for its users. We conjecture that an automated one is
possible with LLM weights held fixed, learning by revising its retained
knowledge and machinery rather than its models. This is a second way to
test the lead article's paradigm, whose first test is a knowledge base. The
theory a house refines is what Peter Naur, who argued that programming is theory building, called *program
theory*: the understanding of a program's purpose, organization, and how to
handle new requests. Naur held that it is bound to people. Because software
fails visibly, the house gives a stronger falsifier than a knowledge base,
at the price of a harder claim.

## Claim

**The automated software house conjecture.** At least one automated
[software house](../notes/definitions/software-house.md) capable of
open-ended coherent software change can operate practically using only
LLMs and other [distributed-parametric](../notes/definitions/representational-form.md)
models available by 2026-09-02, the cutoff chosen for this conjecture, and
held fixed during the run.

*Operates practically* means that the house, started from a declared seed,
the product and machinery built before the run, sustains adequate
performance over a stated horizon within a stated budget, reliably rather
than by chance. *Open-ended* means that it handles whatever reasonable
requests and consequences arise as development continues, without their
being listed in advance; programs that cannot be produced within budget do
not count against the house. The working standard is
comparative: given the same requests and resources, the house should do at
least as well as a *human-agent house*, one with people in its internal
production roles.

A *witness house* is a concrete example meeting the four conditions below,
demonstrated in a *witness run* under a protocol declared in advance. A
successful run supplies evidence under its reported workload, horizon, and
budget, not for the open-ended claim, which covers requests no finite run
exercises.

## The boundary

An *internal production role* is work the house depends on to develop and
evolve the software, whoever performs it: interpreting project knowledge,
making implementation decisions, diagnosing failures, comparing candidates,
revising project state or production machinery, and choosing which revision
takes effect. Users stay outside when they provide requirements, domain
facts, preferences, observed outcomes, or acceptance judgments about
visible behaviour. A user crosses inside when asked to diagnose an
implementation failure, choose among internal designs, or select the
retained successor. The role, not the person, decides the side.

An automated house performs every internal production role
computationally. People may build the seed: the product, purposes, tools,
tests, evaluators, workflows, and safety boundaries. During a witness run
every distributed-parametric model, including adapters, embedding models,
and parametric routers, is declared and pinned. The house may change its
natural-language and symbolic state, including its update machinery. Every
internal decision and successor must come from the current house, its
fixed models, and permitted external inputs. An internal human
intervention ends the run. The [transition-closure
supplement](./transition-closure-and-continuation-reliability.md) develops
that requirement.

## Why the claim is not trivial

Open-ended change brings questions that available checks do not settle.
Say a product built for one customer per deployment must now serve many
tenants. Several designs for representing tenant identity may pass the
current tests, while only some preserve the assumptions on which later
changes depend.

Naur called the understanding needed to choose among such designs, and to
revise them later, a *program theory*. In this supplement its main
behavioural test is coherent change: later requests are handled in
ways that fit the earlier design.

How would a house achieve that? The proposed mechanism is that retained
project-specific commitments do three jobs: they rule out changes that
break the design, they point diagnosis at the likely cause, and they say
what a recovery must preserve. In the tenant example, the commitment that
a person's identity is separate from their organizational membership shows
where the data model has to change. The commitment to tenant isolation
says what every change must keep true. Commitments like these could [keep
the house's search for a design coherent while the consequences of a
choice are still unknown](../notes/program-theory-sustains-search-under-delayed-feedback.md).
Passing the test shows that the house has the capacity. Changing the
commitments and observing what the house does next tests whether this
mechanism explains it.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
reports that full code, annotations, extensive design discussion, and
personal advice did not give a successor team enough program theory:
possessing documentation did not give them the capacity to use it. The
case tested [one historically bounded package and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).
The successors had to find and apply the relevant material through their
own reading. So the case does not say why the transfer failed. The premises
the successors needed may have been absent from the package, present but
never found, or found but not applied. Newer mechanisms target the second
and third causes: rationale linked to the decisions it affects, semantic
retrieval, and loading the relevant record at the point where a decision
is made. Whether they transfer more of the capacity is untested.

Naur also argues that program theory is bound to people. If so, no
automated house can hold one, and the conjecture fails. [Our reading of Naur's
argument](../notes/naur-equates-machine-execution-with-formulated-criteria.md)
identifies a further premise: computation can make these judgments only by
executing explicitly formulated criteria. But formal execution does not
require designers to supply a complete project-specific rule for each
judgment. A fixed LLM may interpret an explanation of tenant isolation
without such a rule; whether it does so reliably is an empirical question.
A successful computational witness would show that program theory is not
bound to people, without settling whether the judgment's criteria can be
formulated.

## How the components could hold a program theory

Fixed LLMs interpret requests and project state and propose changes.
Natural-language project state retains purposes, commitments, and
decisions. Symbolic software supplies exact behaviour: the product, tools,
tests, validation, and rollback. No component holds the program theory
alone, and the house may retain an explicit theory or reconstruct one from
records each time. What matters is explanatory use: project-specific state
changes proposal, evaluation, diagnosis, or recovery, including where the
relevant implication is not stated verbatim.

## What a witness house must show

One house must show all four conditions together. Each needs positive
evidence: a run that never challenges an assumption cannot establish
coherent revision because nothing went wrong.

1. **Holding and application.** Across novel changes, the house uses
   program theory to guide proposal, evaluation, diagnosis, or recovery.
   The evidence must distinguish explanatory use from instruction-following,
   since a model that merely follows retained text as an instruction also
   changes its behaviour when the text changes. Three controls are part of
   the condition: predicted changes in the house's decisions on cases whose
   correct handling is not stated verbatim in its retained state; matched
   variation of the path by which commitments are reconstructed and
   consumed, not only of their text; and an account of equivalent
   reconstruction, since removing one written carrier without changing
   behaviour is inconclusive when other records supply the same
   understanding.
2. **Coherent revision.** Later requests or operating consequences expose
   an inadequacy in the current program theory. The house responds by
   revising the product, retained project state, production machinery, or
   a combination, and the successor supports coherent later change.
3. **Automated continuation.** The house sustains those capacities through
   subsequent requests and consequences without internal human production
   decisions.
4. **Practical reliability.** The declared evaluation shows that the house
   sustains adequacy across the horizon within the budget, reliably enough
   to be useful, against a human-agent house given the same requests and
   resources. A single successful sequence may be chance and establishes
   only possibility.

The witness protocol declares in advance the starting system, the boundary
and workload, how failures are counted, the resources including seed
construction, and the evaluation with its baseline, thresholds, and the
interventions that test condition 1.

## Existing constructions

Schmidhuber's [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is the nearest formal construction. It rewrites its own code, but an
embedded prover admits a rewrite only after proving that switching pays, so
it "must ignore those self-improvements whose effectiveness it cannot
prove" ([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md),
§2.4, verbatim). The house shares its requirement that every successor
arise through the current machinery, but admits a fallible change on
empirical grounds, observes its consequences, and recovers from a wrong one.

Two reports make parts of the conjecture concrete without demonstrating it:
in [OpenAI's agent-first product
account](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
people still supplied internal design judgments, and the [Darwin Gödel
Machine
paper](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
improves benchmark scores by searching over agent code around frozen
models, with no product changing over time. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
maps eighteen systems against the four conditions; none shows all four
together.

## The comparison with the knowledge-base arrangement

The program's first arrangement is Commonplace, a framework for knowledge
bases operated by agents, producing a knowledge base for consuming projects, whose agents use it on their tasks. Both
arrangements test the same paradigm through an externally assessed
product. They differ on Naur's program theory; the other rows follow.

| | Automated software house | Knowledge-base arrangement |
|---|---|---|
| Retained theory | A theory *of* the product: why the code is organized as it is and what a change must preserve | The theory *is* the product: consuming agents read it and act on it |
| Falsifier | A failing test, an invalid release, a user who cannot complete a task, whatever the model took the theory to mean | A judge rejecting an agent's work: evidence about task, consumer, and knowledge base together |
| Locating a fault in the theory | Direct: a broken release means the theory or its use failed | Needs extra interventions to separate the theory from its reading |
| Claim form | Existence: one witness meeting four conditions; the open-ended claim lies beyond any finite run | Sufficiency across declared areas, with breadth from several areas and evidence about transfer |
| What a failed run refutes | Only that construction | Sufficiency for that area |
| Required machinery | Every production role of a working development organization; the seed must already be a working house | Can start from an existing human-inclusive builder and move roles to computation one class at a time |
| Place in the program | Kept beside the knowledge base: its evidence would be stronger if obtainable | Pursued first, because it can start from what exists |

The first row is the hinge. Because the software is a separate artifact
that works or does not, the house gets sharper evidence per episode; the
knowledge base has no second artifact that tests the theory independently
of how it was read. Since the claims differ in form, neither arrangement
substitutes for the other.

Whether a broadly capable knowledge-producing builder must eventually
become a software house, because new domains require it to revise the
software that performs its own production, is a separate [conditional
conjecture](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md).
This supplement does not rely on it in either direction.

## Relation to the program

The lead article tests a theory builder through what it receives from
outside: a falsifier, an objective, and an outcome level it does not judge
itself. A software house supplies these through product operation and
users' judgments. It is neither the program's paradigm case nor a special
case of the knowledge-base arrangement, and its conjecture keeps its own
model cutoff.

## Where to go next

The [software house definition](../notes/definitions/software-house.md)
states the boundary rule in its general form. [Transition closure and
continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every successor come from the current house, and the
[evidence supplement](./testing-the-theory-refinement-program.md) gives the
knowledge-base arrangement's protocol.
