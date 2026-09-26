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
theory*, the term Peter Naur, the computer scientist who argued that
programming is theory building, used for the understanding of a program's
purpose, organization, and how to handle new requests. Naur held that this
understanding is bound to people; an automated house that holds one would
show otherwise. Because software fails visibly, the house gives the
paradigm a stronger falsifier, a failure the system does not itself judge,
than a knowledge base does, at the price of a harder claim: that at least
one whole house meets four conditions together.

## Claim

**The automated software house conjecture.** At least one automated
[software house](../notes/definitions/software-house.md) capable of
open-ended coherent software change can operate practically using only
LLMs and other [distributed-parametric](../notes/definitions/representational-form.md)
models available by 2026-09-02, the cutoff chosen for this conjecture, and
held fixed during the run.

*Operates practically* means that the house, started from a declared seed
(the product and machinery built before the run), sustains adequate
performance over a stated horizon within a stated budget, reliably rather
than by chance. *Open-ended* means that it handles whatever reasonable
requests and consequences arise as development continues, without their
being listed in advance, including requests that change what it is
responsible for. Programs that cannot be produced at all, or not within
budget, do not count against the house. The working standard is comparative: given the same requests and resources, the
house should do at least as well as a *human-agent house*, one with people
in its internal production roles.

A *witness house* meets the four conditions below; a *witness run*
demonstrates them under a protocol declared in advance. A successful run is
evidence under its reported workload, horizon, and budget, not proof of the
open-ended claim, which covers requests no finite run exercises.

## The boundary

An *internal production role* is work the house depends on to develop and
evolve the software, whoever performs it: making implementation decisions,
diagnosing failures, comparing candidates, revising project state or
machinery, and choosing which revision takes effect. Users stay outside when they provide requirements, domain
facts, preferences, observed outcomes, or acceptance judgments about
visible behaviour. A user crosses inside when asked to diagnose an
implementation failure, choose among internal designs, or select the
retained successor. The role, not the person, decides the side.

An automated house performs every internal production role
computationally. People may build the seed, including its tests,
evaluators, workflows, and safety boundaries.
During a witness run every distributed-parametric model, including
adapters, embedding models, and parametric critics, is declared and
pinned. The house may change its natural-language and symbolic state,
including tests and update machinery, but every
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
behavioural test is coherent change: later requests are handled in ways
that fit the earlier design.

How would a house achieve that? The proposed mechanism is that retained
project-specific commitments rule out changes that break the design, point
diagnosis at the likely cause, and say what a recovery must preserve. In the tenant example, the commitment that
a person's identity is separate from their organizational membership shows
where the data model has to change, and the commitment to tenant isolation
says what every change must keep true. Commitments like these could [keep
the house's search for a design coherent while the consequences of a
choice are still unknown](../notes/program-theory-sustains-search-under-delayed-feedback.md).
Changing the commitments and observing what the house does next tests
whether this mechanism, rather than something else, explains its success.

Two parts of Naur's account bear on the conjecture: in his maintenance
cases, possessing documentation did not give successors the capacity to
use it, and he argues that program theory is bound to people.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
reports that full code, annotations, extensive design discussion, and
personal advice did not give a successor team enough program theory. But the
case tested [one historically bounded package and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md),
so it does not say why the transfer failed: the needed premises may have
been absent, present but never found, or found but not applied. Newer mechanisms, such as rationale linked to decisions and retrieval at
the point of decision, target the second and third causes; whether they
transfer more of the capacity is untested.

If program theory is bound to people, no automated house can hold one, and
the conjecture fails. [Our reading of Naur's
argument](../notes/naur-equates-machine-execution-with-formulated-criteria.md)
identifies a further premise: computation can make these judgments only by
executing explicitly formulated criteria. But formal execution does not
require designers to supply a complete project-specific rule for each
judgment. A fixed LLM may interpret an explanation of tenant isolation
without such a rule; whether it does so reliably is an empirical question.
A successful computational witness would show that program theory is not
bound to people, without settling whether the judgment's criteria can be
formulated.

## How the components could perform the program-theory function

The conjectured house combines three components: fixed LLMs that interpret
and propose, natural-language project state that retains purposes,
commitments, explanations, and decisions, and symbolic software (product,
tools, tests, context assembly, validation, rollback) that supplies exact
behaviour and continuity. No component holds the program theory alone. A note that is never loaded has
no effect; a model without enough project state must reconstruct or guess;
software executes a decision without supplying the judgment that selected
it. The house may retain an explicit project theory, reconstruct
understanding from records each time, or combine both. What matters is
explanatory use: project-specific state changes proposal, evaluation,
diagnosis, or recovery, including where the relevant implication is not
stated verbatim.

## What a witness house must show

One house must show all four conditions together. Each needs positive
evidence: a run that never challenges an assumption cannot establish
coherent revision.

1. **Holding and application.** Across novel changes, the house uses
   program theory to guide proposal, evaluation, diagnosis, or recovery.
   The evidence must distinguish explanatory use from instruction-following,
   since a model that merely follows retained text also changes its
   behaviour when the text changes. It needs predicted changes in decisions
   on cases whose handling is not stated verbatim, variation of how
   commitments are reconstructed and consumed as well as of their text, and
   an account of equivalent reconstruction, since removing one written
   carrier proves nothing when other records supply the same understanding.
2. **Coherent revision.** Later requests or operating consequences expose
   an inadequacy in the current program theory. The house revises the
   product, retained project state, production machinery, or a
   combination, and the successor supports coherent later change.
3. **Automated continuation.** The house sustains those capacities through
   subsequent requests and consequences without internal human production
   decisions.
4. **Practical reliability.** The declared evaluation shows that the house
   sustains adequacy across the horizon within the budget, reliably enough
   to be useful, against a human-agent house given the same requests and
   resources. A single successful sequence may be chance and establishes
   only possibility.

The protocol declares in advance the starting system, boundary, workload,
failure counting, resources including seed-construction effort, and the
evaluation with its baseline, thresholds, and condition-1 interventions.

## A formal contrast and existing constructions

Schmidhuber's [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is the nearest formal construction. It rewrites its own code only after
proving that switching pays, so it
"must ignore those self-improvements whose effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), §2.4,
verbatim). Like the house, it requires every successor to arise through the current
machinery, but it admits a change by proof, while the house admits a
fallible change on empirical grounds and recovers from a wrong one.

Two reports make parts of the conjecture concrete. [OpenAI's agent-first
product account](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md)
describes months of agent-generated development, but people still supplied
internal design judgments. The [Darwin Gödel Machine
paper](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
reports improved coding-benchmark performance through search over retained
agent code around frozen models. Neither demonstrates autonomous program
theory across later product changes. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
maps eighteen systems against the four conditions; none shows all four
together.

## The comparison with the knowledge-base arrangement

The program's first arrangement is Commonplace producing a knowledge base
for consuming projects. Both arrangements test the same paradigm through an
externally assessed product. They differ on one point, where Naur's program
theory sits relative to the product, and the other differences in the table
follow from it.

| | Software house | Knowledge-base arrangement |
|---|---|---|
| Retained theory | A theory *about* the product: why the code is organized as it is and what a change must preserve | The theory *is* the product: consuming agents read it and act on it |
| Falsifier | Visible software failure (a failing test, an invalid release, a user who cannot complete a task), independent of how the theory was read | A judge rejecting an agent's work, which is evidence about task, consumer, and knowledge base together |
| Locating a fault | A broken release means the theory or its use failed | Separating the theory from its reading needs further interventions |
| Evidence per episode | Sharper | Less sharp |
| Claim form | Existence: one witness meeting four conditions; the open-ended claim lies beyond any finite run | Sufficiency across declared areas, with breadth from several areas and evidence about transfer |
| What a failed run refutes | Only that construction | Sufficiency for that area |
| Starting point | The seed must already be a working house performing every production role | An existing human-inclusive builder, moving roles to computation one class at a time |
| Program priority | Kept alongside, for stronger evidence if it can be obtained | Pursued first, because roles can move to computation gradually |

The two claim forms do not substitute for one another.

Whether a broadly capable knowledge-producing builder must eventually
become a software house, because new domains require it to revise its own
production software, is a separate [conditional
conjecture](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
that this supplement does not rely on.

## Relation to the program

The lead article tests a theory builder through what it receives from
outside: a falsifier, an objective, and an outcome level it does not judge
itself. A software house supplies all three through product operation and
users' judgments of visible behaviour. The software house is not the
program's paradigm case and not a special case of the knowledge-base
arrangement: it is a different product, with a stronger falsifier and a
harder claim.

## Where to go next

[Nearest existing constructions to a witness
house](./nearest-existing-constructions-to-a-witness-house.md) gives the
evidence behind the survey above. [Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every successor state come from the current house.
The [software house definition](../notes/definitions/software-house.md)
carries the boundary rule in its general form, and the [evidence
supplement](./testing-the-theory-refinement-program.md) states the
knowledge-base arrangement's protocol for the comparison above.
