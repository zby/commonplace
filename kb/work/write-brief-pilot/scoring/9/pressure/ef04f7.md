---
description: "Supplement: the automated software house conjecture as an alternative test of theory refinement with fixed models; the 2026-09-02 claim, Naur's program theory, four witness conditions, and the knowledge-base comparison"
type: articles/types/article.md
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
possible with LLM weights held fixed: computation performs every production
decision, and the house learns by revising its retained knowledge and
machinery rather than its models. This is a second way to test the lead
article's paradigm, learning by theory refinement with fixed models, whose
first test is a knowledge base. The theory a house refines is *program
theory*, Peter Naur's term for the understanding of a program's purpose,
organization, and how to handle new requests. An automated house that
holds one would contradict Naur's view that it is bound to people.
Software fails visibly, so the house gives the paradigm a stronger
falsifier, a failure the system does not itself judge, than a knowledge
base does. It also demands a harder claim: that at least one
whole house exists that meets four conditions together.

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
being listed in advance, including requests that change what it is
responsible for. *Reasonable* is left informal; programs that cannot be
produced at all, or not within budget, do not count against the house. The
working standard is comparative: given the same requests and resources,
the house should do at least as well as a *human-agent house*, one with
people in its internal production roles.

A *witness house* is a concrete example meeting the four conditions below.
A *witness run* is an attempt to demonstrate them under a protocol declared
in advance. A successful run supplies evidence for the conjecture under its
reported workload, horizon, and budget. It does not establish the
open-ended claim, which covers requests no finite run exercises.

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
computationally. People may build the seed: the product, purposes and
rationale, tools, tests, evaluators, workflows, and safety boundaries.
During a witness run every distributed-parametric model is declared and
pinned, including adapters, embedding models, and parametric routers and
critics. The house may change its natural-language and symbolic state,
including tests, evaluators, workflows, and update machinery, but every
internal decision and successor must come from the current house, its
fixed models, and permitted external inputs. An internal human
intervention ends the run. The [transition-closure
supplement](./transition-closure-and-continuation-reliability.md) develops
that requirement.

## Why the claim is not trivial

Open-ended change raises questions that current checks do not settle.
Say a product built for one customer per deployment must now serve many
tenants. Several designs for representing tenant identity may pass the
current tests, while only some preserve the assumptions on which later
changes depend. Naur called the understanding needed to choose among such
designs, and to revise them later, a *program theory*. Its main
behavioural test here is coherent change: later requests are handled in
ways that fit the earlier design.

The proposed mechanism is that retained project-specific commitments rule
out changes that break the design, point diagnosis at the likely cause, and
say what a recovery must preserve. In the tenant example, the commitment
that a person's identity is separate from their organizational membership
shows where the data model has to change, and the commitment to tenant
isolation says what every change must keep true. Commitments like these
could [keep the house's search for a design coherent while the consequences
of a choice are still
unknown](../notes/program-theory-sustains-search-under-delayed-feedback.md).
Changing the commitments and observing what the house does next tests
whether this mechanism explains the capacity.

No single component would hold the theory: fixed LLMs propose,
natural-language project state retains commitments and decisions, and
symbolic software supplies exact behaviour, tests, and rollback. The
house may keep an explicit project theory, reconstruct understanding from
records each time, or combine both. What matters is explanatory use:
project-specific state changes proposal, evaluation, diagnosis, or
recovery, including where the relevant implication is not stated verbatim.

Naur's own work raises two objections. First, [Naur's compiler
case](../sources/programming-as-theory-building.ingest.md) reports that
full code, annotations, extensive design discussion, and personal advice
did not give a successor team enough program theory. But the case tested
[one historically bounded package and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md),
and it does not say why the transfer failed: the needed premises may have
been absent from the package, present but never found, or found but not
applied. Newer mechanisms target the second and third causes: rationale
linked to the decisions it affects, semantic retrieval, and loading the
relevant record where a decision is made. Whether they transfer more of the
capacity is untested.

Second, Naur argues that program theory is bound to people; if so, the
conjecture fails. [Our reading of Naur's
argument](../notes/naur-equates-machine-execution-with-formulated-criteria.md)
finds a further premise: computation can make these judgments only by
executing explicitly formulated criteria. Formal execution does not require
designers to supply a complete project-specific rule for each judgment. A
fixed LLM may interpret an explanation of tenant isolation without such a
rule; whether it does so reliably is an empirical question. A successful
witness would show that program theory is not bound to people, without
settling whether the judgment's criteria can be formulated.

## What a witness house must show

One house must show all four conditions together. Each needs positive
evidence: a run that never challenges an assumption cannot establish
coherent revision.

1. **Holding and application.** Across novel changes, the house uses
   program theory to guide proposal, evaluation, diagnosis, or recovery.
   The evidence must separate explanatory use from instruction-following,
   since a model that merely obeys retained text also changes its behaviour
   when the text changes. Three controls are part of the condition:
   predicted changes in the house's decisions on cases whose correct
   handling is not stated verbatim in its retained state; matched variation
   of the path by which commitments are reconstructed and consumed, not
   only of their text; and an account of equivalent reconstruction, since
   removing one written carrier without changing behaviour is inconclusive
   when other records supply the same understanding.
2. **Coherent revision.** Later requests or operating consequences expose
   an inadequacy in the current program theory. The house revises the
   product, retained project state, production machinery, or a combination,
   and the successor supports coherent later change.
3. **Automated continuation.** The house sustains those capacities through
   subsequent requests and consequences without internal human production
   decisions.
4. **Practical reliability.** The declared evaluation shows that the house
   sustains adequacy across the horizon within the budget, reliably enough
   to be useful, against a human-agent house given the same requests and
   resources. A single successful sequence may be chance and establishes
   only possibility.

The witness protocol declares in advance the starting system, workload,
failure counting, resources including seed-construction effort, baseline,
thresholds, and the interventions used to test condition 1.

## A formal contrast and existing constructions

Schmidhuber's [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is the nearest formal construction. It can rewrite its own code, and its
embedded prover admits a rewrite only after proving, from the current
axioms and utility function, that switching pays. So it "must ignore those
self-improvements whose effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), §2.4,
verbatim). It differs from the house in the admission route: the
Gödel machine admits a change by proof under its formalization, while the
house admits a fallible change on empirical grounds, observes its
consequences, and recovers from a wrong one.

Existing systems show parts of the conjecture. [OpenAI's agent-first
product account](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
describes months of agent-generated development, while people still
supplied internal design judgments. The [Darwin Gödel Machine
paper](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
reports coding-benchmark gains from search over retained agent code around
frozen models. Neither demonstrates autonomous program theory across later
product changes. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md) maps
eighteen systems against the four conditions; none shows all four.

## The comparison with the knowledge-base arrangement

The program's first arrangement is Commonplace producing a knowledge base
for consuming projects. Both arrangements test the same paradigm through an
externally assessed product. They differ on where the retained theory sits,
and the other differences follow from that.

| | Software house | Knowledge-base arrangement |
|---|---|---|
| Retained theory | A theory *about* the product: why the code is organized as it is and what a change must preserve. The software is a separate artifact. | The theory *is* the product: consuming agents read it and act on it. No second artifact tests it independently of how it was read. |
| Falsifier | A failing test, an invalid release, a user who cannot complete a task, whatever the model understood the theory to say. | A judge rejecting an agent's work: evidence about task, consumer, and knowledge base together. Locating the fault in the theory needs extra interventions. |
| Evidence per episode | Sharper | Weaker |
| Claim form | Existence: one witness meeting four conditions; the open-ended claim lies beyond any finite run. | Sufficiency across declared areas, with breadth from several areas and evidence about transfer. |
| A failure refutes | Only that construction | Sufficiency for that area |
| Required machinery | Every production role of a working development organization; the seed must already be a working house. | Can start from an existing human-inclusive builder and move roles to computation one class at a time. |

The two claims do not substitute for one another. The lower machinery
requirement is why the program pursues the knowledge base first; the
software house stays beside it as the arrangement whose evidence would be
stronger if obtained: a stronger falsifier, at the price of a harder claim.

Whether a broadly capable knowledge-producing builder must eventually
become a software house, because new domains require it to revise the
software that performs its own production, is a separate [conditional
conjecture](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md).
This supplement does not rely on it in either direction.

## Relation to the program

The lead article tests a theory builder through what it receives from
outside: a falsifier, an objective, and an outcome level it does not judge
itself. A software house supplies all three through product operation and
users' judgments of visible behaviour. Its conjecture, boundary, and
conditions predate that framing and keep their own model cutoff. The
software house is not the program's paradigm case and not a special case
of the knowledge-base arrangement; it is a different product.

## Where to go next

[Nearest existing constructions to a witness
house](./nearest-existing-constructions-to-a-witness-house.md) surveys
existing systems. [Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every successor state come from the current house.
The [software house definition](../notes/definitions/software-house.md)
carries the boundary rule in its general form, and the [evidence
supplement](./testing-the-theory-refinement-program.md) states the
knowledge-base arrangement's protocol.
