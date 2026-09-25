---
description: "Supplement: the automated software house conjecture (2026-09-02 fixed models) as a second test of a theory builder; Naur's program theory against the stated-content condition, software's stronger falsifier and harder claim, four witness conditions"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/software-house.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md
  - kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md
---

# An Automated Software House as a Second Test of a Theory Builder

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

[The lead article](./building-a-theory-builder-from-todays-llms.md) bets
that a fully automated theory builder can be made from today's fixed-weight
LLMs, and tests the bet first with a knowledge base, whose failures are slow
and partly judged by people. This supplement states a second arrangement: an
automated software house. Software gives the program a stronger falsifier
than a knowledge base does, at the price of a harder claim. The arrangement
is kept as a companion to the knowledge-base test, not a replacement for it.

## The conjecture

A [software house](../notes/definitions/software-house.md) is the complete
persistent system responsible for developing and evolving software for
external users. It is automated when computation performs every internal
production role: interpreting project knowledge, making implementation
decisions, diagnosing failures, and choosing which revision takes effect.
Users who only supply requirements, feedback, and acceptance judgments stay
outside.

> **The automated software house conjecture.** At least one automated
> software house capable of open-ended coherent software change can operate
> practically using only LLMs and other
> [distributed-parametric](../notes/definitions/representational-form.md)
> models available by 2026-09-02, the cutoff chosen for this conjecture, and
> held fixed during the run.

*Operates practically* means that the house, started from a declared seed
(the product and machinery built before the run), sustains adequate
performance over a stated horizon within a stated budget, reliably rather
than by chance. *Open-ended* means that it handles whatever reasonable
requests arise as development continues, without their being listed in
advance. The working standard is comparative: given the same requests and
resources, the automated house should do at least as well as a house with
people in its internal production roles.

## Why an automated house is a theory builder

Peter Naur, in
[Programming as Theory Building](https://doi.org/10.1016/0165-6074(85)90032-8),
called the understanding a maintainer needs a *program theory*: an account
of what the program is for, why its parts are as they are, and how a new
demand fits the existing structure. Suppose a product built for one customer
per deployment must now serve many tenants. Several designs pass the current
tests; only some preserve what later changes depend on. A commitment
such as "a person's identity is separate from their membership in an
organization" shows where the data model must change, and "tenants never see
each other's data" says what every change must keep true. Commitments like
these [keep the search for a design coherent while the consequences of a
choice are still unknown](../notes/program-theory-sustains-search-under-delayed-feedback.md).

The knowledge base [defines a theory builder](../notes/definitions/theory-builder.md)
by four conditions: its theories are stated, so identifiable units say
something; they guide what it does; it criticizes what they say and revises
or replaces those that fail; and the result of criticism shapes the next
conjecture. An automated house meets them when its program theory is written
down as commitments like the two above, later changes consult them, a broken
release or a rejected change is traced to a commitment that was wrong, and the
revised commitment governs the next request. Software failures then do the
error-elimination step of the lead's cycle.

Naur's account is in tension with the first condition. He held that program theory cannot
be expressed as rules or criteria, and that it is bound to the people who
hold it. The knowledge base
[reads his human-only conclusion](../notes/naur-equates-machine-execution-with-formulated-criteria.md)
as needing a further premise: that a computer can make a judgment only by
executing criteria formulated in advance. A fixed LLM runs by defined operations,
but nobody supplied it a rule for each judgment; it can apply a stated
commitment to a case the commitment does not mention. How well is an
empirical question. His
[compiler case](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md),
in which program text, annotations, design notes, and personal advice did not
transfer the theory to a successor team, tested one historically bounded way
of writing and reading documentation, not every possible one.

This does not dispute that the theory cannot be fully written down, and the
house need not write all of it down. It must state what
it holds, because only stated units can be criticized; the fixed model
supplies the judgment that applies them. A text of commitments does not apply
itself, and with the models pinned, any procedure the house learns for using
its theory [must be retained outside the weights](../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md),
as instructions or code. Naur's human-only thesis predicts that such a house
will fail to change its product coherently. One that succeeds would show that
program theory is not bound to people, without settling whether its criteria
can be fully formulated.

## Why the falsifier is stronger, and the price

A knowledge base is tested when a consuming project's agents use it and a
judge accepts or rejects their work. The knowledge is the product, and the
rejection is evidence about the task, the consumer, and the knowledge base
together. A house's program theory is about a separate artifact that either
works or does not. A failing test, a broken build, or a rejected release
arrives quickly and is judged outside the house.

Users who judge the software supply all three items of full
[external assessment](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
an external falsifier, an external objective, and an outcome level
independent of the builder's own evaluators. The knowledge base needs a
consuming project to supply them. An outside signal still does not locate
the fault. A broken release shows that
the theory or its use failed, and blaming a particular commitment needs a
further probe.

The price is the claim. The knowledge-base claim is sufficiency in declared
areas, each testable on its own. Open-ended coherent change covers requests no finite run exercises, so a run
supports a version of the conjecture bounded to its workload, horizon, and
budget, and does not establish the open-ended claim.

## What a witness must show

A *witness run* is an attempt, under a protocol declared in advance, to show
one house meeting four conditions together.

1. **Holding and application.** The house's program theory guides its
   proposals, diagnoses, and recoveries on novel changes. It fails if
   [altering a retained commitment](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
   changes decisions only where the text states the answer verbatim, which
   is instruction-following, or changes nothing.
2. **Coherent revision.** A later request or operating consequence exposes a
   wrong commitment, and the house revises the product, the theory, or its
   machinery so that later changes still fit. It fails if the house patches
   around the problem and later changes break the design, or if the run
   never challenges a commitment, since then nothing was shown.
3. **Automated continuation.** The house keeps both capacities through
   later requests with no person in an internal production role. It fails
   the moment a person diagnoses a failure, chooses between designs, or
   selects the next version; that ends the run.
4. **Practical reliability.** Across the horizon and within the budget, the
   house does at least as well as a human-staffed house on the same requests
   and resources. It fails if it does worse, or if success comes from one
   lucky sequence that repetition does not reproduce.

The conditions test the conjecture, not the theory-builder definition, which
has no success condition. A house that met all four through outcome-scored
repair, with no stated reason aimed at what a commitment says, would confirm
the conjecture without being a theory builder.

Five of the eighteen systems in the
[survey of existing self-improving systems](./which-existing-self-improving-systems-are-theory-builders.md)
meet the theory-builder conditions, three of them staffed by people; none is
shown there to be an automated software house.

## A companion, not the main path

A house must perform every production role of a working development
organization, so its seed must already be a working house. The knowledge-base
arrangement can start from an existing builder staffed by people and agents
and [move its roles to computation one class at a
time](./bootstrapping-an-autonomous-theory-builder.md). That is why the
knowledge base comes first. The software house is kept beside it because its
evidence would be stronger if it could be obtained.

## Where to go next

The [testing supplement](./testing-whether-a-theory-builder-learns.md)
states the knowledge-base protocol and how evidence reaches a builder. The
[software-house definition](../notes/definitions/software-house.md) gives the
role boundary in its general form. Whether an automated theory builder
working across open domains must itself
[become a software house](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
is a separate, conditional conjecture this article does not rely on.
