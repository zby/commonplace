---
description: "Conjecture that an automated software house capable of open-ended coherent change is practically reachable with 2026 LLMs kept fixed while computation trains the notes and code around them; program theory, learning loop, seed, witness obligations"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md
  - kb/notes/axes-of-artifact-analysis.md
  - kb/notes/code-complements-weight-prompt-with-symbolic-operations.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md
  - kb/sources/goedel-machines-schmidhuber.ingest.md
  - kb/sources/programming-as-theory-building.ingest.md
---
# The Automated Software House Conjecture

*Open-ended software development with fixed LLMs*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** We use *software house* for whatever keeps changing a piece of
software for its users, not only a company. It changes the software as users
ask for things and as the software is used. The conjecture is that such a
house can run with nobody inside it in a production role, on LLMs available
by 2026-09-02, and handle requests nobody listed in advance. Users stay
outside; asking for things and judging what they see is not a production
role. The computer scientist Peter Naur argued that the understanding that
relates a program to what it is for, which he called a program theory,
can be held only by people; the conjecture denies that. The models stay
fixed. Learning happens in the project state around them: code, notes, and
the machinery that loads both into later work and decides which changes are
kept. People write the first versions. The house then revises them as
requests and their consequences arrive, and people correct it at first. The
conjecture includes that the correction required shrinks as the house's
training goes on, until the house keeps its own state and software adequate
without people. Agent harnesses with memory files and self-written rules are
already moving this way. The article gives that practice a formal statement:
what the house is as a system, what counts as its learning rather than a
person's, what its endpoint without a person would be, and what one working
house would have to show to establish the conjecture. It does not argue that
a fixed model is the best way to train such a house; a [companion
article](./the-software-house-as-the-unit-of-training.md) takes that up.

## Claim

**The automated software house conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) (below, *the house*) capable
of open-ended coherent software change is practically reachable with LLMs
available by 2026-09-02.

The eligible model versions, meaning those available by the cutoff date, stay
fixed, and so do their weights and any other learned component, such as an
embedding model. Together these are the [learned
parameters](../notes/definitions/representational-form.md). What gets trained is
the house, through changes that computation produces and the house retains in
its [notes and code](../notes/definitions/representational-form.md). *Notes
and code* here means everything the house holds in natural language or in
symbolic form: notes, code, schemas, tests, tools, and rules for how
production is done. Derived indexes may be regenerated from those notes and
code under pinned machinery, but they are not independently trained or
treated as learned state. *Practically reachable* means success within a
declared product scope, operating horizon (how long the house must keep
running), and budget of compute, time, and cost. Within those bounds,
training must discover and maintain the decisive project-specific notes and
code until no human is needed in an internal role.

An *internal role* is what the
[definition](../notes/definitions/software-house.md#scope) calls an internal
production role: work the house depends on to produce the software, whoever
performs it. For this conjecture the decisive internal roles are diagnosing
implementation failures, comparing internal candidates, editing the theory,
and choosing which revision is kept. Users stay outside the house when they
supply product-level requirements, facts, observed outcomes, or acceptance
judgments about visible behaviour. The role, not the person, decides which
side of the boundary an act falls on.

## Why the components could suffice

Open-ended change brings demands nobody analysed in advance and questions of
fit that the available checks do not settle. Say a product built for one
customer per deployment must now serve many tenants. The tenant identifier
can enter the data model in several ways. All of them pass the existing
tests, but only some preserve the assumptions the rest of the code relies on
without stating them. Choosing among them needs what the computer scientist
Peter Naur called a program theory. That is the capacity to relate the
software to the activity it supports, to explain why it is organized as it
is, and to relate a new demand to that organization. [Holding a program theory means sustaining
coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md):
the multi-tenant choice may not show its consequences until the next three
demands arrive.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
showed that full code, annotations, extensive design discussion, and personal
advice did not give a successor team enough program-specific understanding.
More prose of the same kind is not an answer. But it tested [one set of
documents and one way of reading them, bounded to its
time](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).
It did not test linked rationale, machine-maintained indexes, semantic
retrieval, context assembled by following dependencies, or a note surfaced at
the point of decision. A newer way of representing and consuming project
knowledge may transfer more of the required capacity, to people or to a house
built from an LLM. That is an open empirical question.

Naur's conclusion that only people can hold a program theory also relied on
treating machine execution as the same thing as executing formulated
criteria. An LLM is still formal computation, but it can interpret a
paragraph explaining why retry logic belongs in the caller without that
judgment first being written out as a complete, explicit rule. A successful
house would falsify Naur's human-only conclusion while leaving intact his
claim that the relevant judgment cannot be reduced to a finite set of
formulated criteria. [The distinction is between formal execution and
explicitly formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
Naur's criterion is judged by what the house can do, and that can be seen
only over many changes. Its project-specific state must guide how it
proposes, evaluates, diagnoses, or recovers, on implications not stated
verbatim in that state. And changing that state must change what the house
does next.

The conjecture implements the house from three components, each with a role:

- Fixed current LLMs supply the general linguistic, programming, and
  reasoning capacity that interprets project state and produces candidate
  changes.
- Natural-language notes supply persistent project-specific purposes,
  commitments, explanations, evidence, and prior search. For example:
  "installs must be a single file, so the store is SQLite; do not add a
  server dependency." Architecture decision records already carry part of
  this rationale.
- Symbolic software supplies exact behaviour and continuity. This includes
  the product, tools, schemas, context assembly (choosing what the model
  reads), schedulers, validators and tests, version-control rollback, and
  retention rules.

None of these holds the theory alone. A note nobody loads has no effect. A
fixed LLM without enough project state reconstructs or guesses instead of
carrying understanding from one change to the next. Software executes a
decision without supplying the judgment that selected it. The house as a
whole has to hold the program theory.

## How the house learns while the model stays fixed

Pinning the model does two things. It isolates one question: whether learning
in the state around a model can suffice, with no help from a changed model.
And it matches the regime of a project that uses a hosted model whose
weights its provider does not let it change. Such a project cannot retrain
the model it uses. If it is to keep what it learns about its own product,
that learning has to be kept in state outside the model. Pinning is a
condition of the experiment, not a recommendation for how a mature house
should be trained.

Training here means search. Finding notes and code that work may require
criticism, trials, production consequences, and retained correction, much as
finding useful weights requires gradient descent. That the artifacts are
readable once found does not make them easy to find.

Current LLMs can produce both notes and code. Software can put a proposed
change into effect and feed later consequences into another update. The
process is a schematic loop, not a formal model:

```text
production evidence + fixed LLMs + present notes and code
  -> computational update of notes and/or code
  -> retained successor state
  -> later production
```

The first arrow hides two hard decisions. Admission is deciding which changes
of meaning may enter retained state. Credit assignment is deciding which
earlier code, note, way of loading context, test, objective boundary, or
selection policy a later consequence counts for or against. [Governing a
behaviour-changing write therefore requires selection, validation,
authorization, and
coordination](../notes/continual-learning-requires-governing-behaviour-changing-writes.md).
This article supplies no general solution to that problem. A *witness* is one
working house that makes the existential claim true, in the logician's sense
of the word. It must show that its credit assignment and admission work well
enough to satisfy the acquisition and continuation obligations below. A user
who supplies requirements, feedback, domain knowledge, or an acceptance
judgment stays external. A person who repeatedly diagnoses the theory failure
or chooses the successor is doing the house's credit assignment and fills the
excluded internal role.

The update mechanism is otherwise open. It may produce a successor directly
or separate proposal, evaluation, and selection, and it may edit prior notes,
rebuild working understanding from retained records, revise software, or
combine these operations. A retained change counts as learning by the house
only when experience causes it and it changes how the house handles a later
job it has not yet been given. Carrying forward the product state an earlier
request asked for is not enough, since the next job starts from the changed
product either way. Adding a validator because a bug class recurred
qualifies, since the validator later blocks that class. So does a product
abstraction, invariant, or test that demonstrably shapes later changes beyond
merely being part of the changed product. A note never loaded by context
assembly does not.

Hand-built tools, stores, interfaces, safety boundaries, and provisional
notes may start the loop. They are seed engineering, not evidence of
acquisition. The training path must outgrow repeated human authorship of the
decisive project-specific theory, whatever its form. A hand-built check
that rejects every schema change carries the human's theory that the schema
is settled, just as a note saying so would. A wholly hand-built end state
would show that notes and code can carry theory, not that the house
learned it. Once no human is inside, every successor must arise through the
predecessor state's own update machinery and the external inputs the witness
permits. The states the house can reach are therefore those its own update
machinery and permitted inputs can produce from the seed, step by step. The
companion article names this set the [transition closure of the
seed](./reachability-as-closure-under-the-seed-gate.md). The step from one
state to the next may be probabilistic, and it may revise the house's own
machinery through permitted transitions. Outgrowing the seed means that
adequate human-free states are reached with usable probability and sustain
coherent later work, not merely that one such state lies on a possible path.

General production machinery such as git, the test runner, or the model
client may stay fixed while it handles the declared scope. If the scope
requires a machinery change, such as a tag index once relevant notes stop
fitting the context window, the automation obligation below requires the
house to make it. Changing its own machinery is then a consequence of
automation, not a separate requirement.

## What a witness must show

One witness must eventually show the whole progression:

1. **Holding and application.** Given adequate project-specific state, the
   house sustains theory-guided proposal, evaluation, diagnosis, or recovery
   across novel changes, including cases whose correct handling is not stated
   verbatim in that state. With everything else held equal, withholding or
   replacing the relevant state changes what the house does next in a
   predicted way.
2. **Initial acquisition.** From permitted records, interaction, and
   participation in the work, the house acquires the capacity an adequate
   program theory provides instead of receiving the decisive project-specific
   understanding from a human. The theory may be written down, reliably
   reconstructed from records each time, or a mix.
3. **Successor acquisition.** When experience exposes an inadequacy, the
   house reaches a successor state that supports coherent later modification.
   An example is a dependency change that makes an earlier design reason
   false. The revision may change explicit theory, records, software,
   production machinery, or a combination.
4. **Automated continuation.** The house sustains these capacities across the
   declared scope and horizon with no human in an internal role.

These obligations do not fix which form carries the theory or which form
learns. Notes and code are both eligible surfaces. A witness may meet the
obligations by changing either, or a mix, so long as experience causes the
change, computation produces it, and the retained result does the work the
obligation names.

Obligations 2 and 3 must be met by computation. That is a condition on them,
not a fifth step. A partial mechanism for one of them is not partial
completion of it: storing or paraphrasing a rationale does not show that it
governed a decision, and a gate that can reject does not show that the
admitted successor was adequate.

## Nearest existing constructions

The fully formal case is AI researcher Jürgen Schmidhuber's [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md),
a proof-governed construction that rewrites its own code. It is not a
software house: it has no users, and the only software it changes is itself.
It shows what automation costs when formulated criteria buy it. An embedded
prover admits a rewrite only after proving, from the machine's axioms and
formal statement of utility, that the rewrite pays. Everything the conjecture
asks the house to acquire is supplied there in advance, as the formal basis
for accepting a rewrite. The theory of the system is the axioms, the
objective is the utility function, and the test is proof. Any of them may be
rewritten, but only under a proof from the formalization then in force. So
the initial formalization governs every successor by descent, and a demand
nobody formalized cannot enter the test. The paper states the price: the
machine "must ignore those self-improvements whose effectiveness it cannot
prove" ([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md),
§2.4, verbatim).

Once no human is inside, both the Gödel machine and the conjectured house are
self-modifying systems. Every next state must arise through the current
state's own machinery and permitted inputs. The Gödel machine admits a next
state only under proof from its current formalization. The house's next state
may be wrong and corrected later, because operating consequences can defeat
part of its current theory and alter later updates. They share the descent
structure, not the justification. The Gödel machine's theorems are closed
under deduction; its states are closed under proof-gated transitions. The
house's states are closed under fallible ones.

The obligations above are also an instrument for reading existing systems.
Agent harnesses that keep memory files, write their own tests and tools, and
retain rules from past failures are the practice this article formalizes.
What their accounts usually leave open is whose learning an improvement
was: the person who noticed a recurring failure, diagnosed it, and chose the
rule did the credit assignment, and an account that does not separate that
from what the harness did on its own cannot show acquisition by the house.
The internal-role boundary and the obligations make that separation
explicit. A [companion
map](./nearest-existing-constructions-to-a-reachability-witness.md) applies
them to twenty reviewed constructions and records the evidence behind each
placement. The [third
article](./bootstrapping-the-first-automated-software-house.md) in this
series sets out a program for getting from a house that still has people in
internal roles to a witness.

The conjecture does not require a theory stored as its own artifact: a house
may reliably reconstruct the understanding it needs from retained records.
Whether a rationale that can be found and revised on its own does better
than reconstruction from records is a question about the mechanism, not
about reachability. The [companion
article](./the-software-house-as-the-unit-of-training.md#testable-consequences)
states it as a hypothesis with its own test.

An [open-domain theory builder may itself become a software
house](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
when new domains require changes to its production machinery. That separate
conjecture is not needed for the claim made here.

## Boundaries and epistemic status

The conjecture is existential: it says only that at least one such house
exists, for some eligible LLM, some arrangement of notes and code, some
product scope. The witness rules out, in advance, two ways of saving the
conjecture after a failure. The witness pins every eligible model and every
other learned component before testing, so that a newer model or another
newly trained component cannot do the work. It also declares product
scope, horizon, and budget before testing, so that the scope cannot shrink
until fixed machinery suffices. Open-ended means that the process generating
requests and their consequences is declared in advance and can produce
relevant novelty; it is not a fixed list of benchmark tasks. Three things
about that process are distinct and fixed before the run: which request
sequences it may produce, the one it actually produced, and how likely each
was. None may be changed after a failure is seen. Bare reachability is cheap:
one lucky path establishes only possibility. The claim is that training
reaches adequate states with usable probability inside the declared budget
and that they remain adequate across the declared horizon.

The cutoff and pinning apply only to a run meant to establish the claim, not
to ordinary development. The project may build and deploy with newer models,
and doing so can show that accumulated state and machinery let a prepared
project exploit a newer model better than an unprepared one. That is evidence
about the state's value, not of reachability with models available by
2026-09-02. In a run meant to establish the claim, a newer model must not
supply trial-specific theory, diagnose the trial's internal failures, select
successors, or fill any other excluded internal role. Derived indexes may
change only as mechanical views of the notes and code under the pinned
algorithms declared by the witness.

Notes and code are the trainable internal state. Products, demands, tool
outputs, and operating consequences are its evidence. Holding, acquisition,
training, learning, and automation are requirements of this witness, not of
the base software-house definition.

The need for a program theory is a theoretical argument, not a proved
theorem. That current LLMs suffice, and that the training path is practical,
are conjectures. The project is constructive: a working system establishes
reachability over its declared scope, horizon, and budget. Failure of one
architecture eliminates that path; it cannot refute the existential claim
unless the search has first been bounded.

Pinning the model isolates the question whether the house is reachable. This article does not
claim that explicit project theory is the best carrier of acquired
understanding, that updates outside the weights are better than training the
model, or that weights should stay fixed in a mature system. It asks only
whether an automated house can acquire and sustain the required capacity
under that restriction. A house with people in internal roles that
substantially reduces programmer work is a positive engineering result even
if it never satisfies the conjecture. The [companion
article](./the-software-house-as-the-unit-of-training.md) takes up the
training regime that becomes available once such a house exists.
