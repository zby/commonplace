---
description: "Conjecture that an automated software house capable of open-ended coherent change is reachable with 2026 LLMs while model weights stay fixed and the notes and code around them learn; the program-theory argument, training path, and witness obligations"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md
  - kb/notes/axes-of-artifact-analysis.md
  - kb/notes/code-complements-weight-prompt-with-symbolic-operations.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/opacity-is-a-scale-threshold.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/sources/goedel-machines-schmidhuber.ingest.md
  - kb/sources/programming-as-theory-building.ingest.md
---
# The reachability conjecture: the LLM stays fixed, the software house learns

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** We use *software house* for whatever keeps changing a piece of
software for its users, not only a company. It changes the software as users
ask for things and as the software is used. The conjecture is that such a
house can run with no human in a production role, on models that already
exist, and handle requests nobody listed in advance. **The models stay fixed;
learning happens in the software and project state around them:** code,
notes, and the machinery through which both shape later work. People write
the first versions. The house then revises them as requests and their
consequences arrive, and people correct it at first. **The bet** is that the
correction required shrinks as training goes on until the house keeps its own
state and software adequate without people. A separate, stronger hypothesis
says that the house does better when it writes its understanding down where
it can be found and revised as a unit than when it rebuilds it from raw
records. Agent harnesses with memory files and self-written rules are already
moving this way. The article gives that evolution a formal statement: what
the house is as a system, what counts as its learning rather than a person's,
what its endpoint without a person would be, and what a witness for that
endpoint would have to show.

## Claim

**The reachability conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) (below, *the house*) capable
of open-ended coherent software change is practically reachable with LLMs
available by 2026-09-02.

The eligible model versions, meaning those available by the cutoff date, stay
fixed, and so do their weights and any other learned component, such as an
embedding model. Together these are the [distributed-parametric
state](../notes/definitions/representational-form.md). What gets trained is
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
tests, but only some preserve the assumptions the rest of the code silently
relies on. Choosing among them needs what the computer scientist Peter Naur
called a program theory. That is the capacity to relate the software to the
activity it supports, to explain why it is organized as it is, and to relate
a new demand to that organization. [Holding a program theory means sustaining
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

None of these holds the theory alone. A note nobody loads is inert. A fixed
LLM without enough project state reconstructs or guesses instead of carrying
understanding from one change to the next. Software executes a decision
without supplying the judgment that selected it. The house as a whole has to
hold the program theory.

## Training in legible forms

Legible means inspectable and directly revisable. It does not mean easy to
design. Finding good notes and tooling may require search, criticism, trials,
production consequences, and retained correction, much as finding useful
weights requires gradient descent. The artifacts remain readable once found.

This is compatible with the Bitter Lesson's preference for general methods
that scale with computation because [the lesson selects how behavior-shaping
structure is produced, not the form in which it is
retained](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Learned software and notes are not disqualified merely because they are
separate and readable. A hand-crafted seed is compatible only if [learning
outgrows the task-specific knowledge the seed
supplies](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
Those two points answer the objection in principle; whether training over
legible structures scales is what the project has to demonstrate.

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

Hand-crafted tools, stores, interfaces, safety boundaries, and provisional
notes may start the loop. They are seed engineering, not evidence of
acquisition. The training path must outgrow repeated human authorship of the
decisive project-specific theory, whatever its form. A hand-written check
that rejects every schema change carries the human's theory that the schema
is settled, just as a note saying so would. A wholly hand-built end state
would show that software and notes can carry theory, not that the house
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

## What this training route could buy

The alternative route is to train the model itself, by fine-tuning or
retraining its weights on project experience. Neither route makes the whole
system transparent. The fixed LLM's weights remain opaque, and enough
software and notes can [exceed practical
inspection](../notes/opacity-is-a-scale-threshold.md). The difference is
where the learned project-specific state lives. Fine-tuning spreads it across
weights, where a changed behaviour is hard to locate, inspect, or revert on
its own. Training the house keeps it in separate units that can be found and
revised on their own. The house can identify a changed claim or function,
inspect its history, revise it selectively, and roll it back without
retraining the model.

Learning can then happen in deployment. Production evidence can cause a
retained change to a note, test, tool, or policy, and that change can affect
the next round of work without a training run.

A further payoff is possible but not required by the conjecture. When
retained program theory captures structure that survives a change, the house
[may need fewer new observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can revise one premise and derive several consequences instead of
relearning them separately. This advantage depends on the theory being both
adequate and actually used in later decisions; otherwise one wrong premise
misleads many decisions at once. Fewer observations also need not mean lower
total cost once theory search, validation, retrieval, and maintenance are
counted.

## What a witness must show

One witness must eventually demonstrate the whole progression:

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
   false. The revision may touch explicit theory, records, software,
   production machinery, or a combination.
4. **Automated continuation.** The house sustains these capacities across the
   declared scope and horizon with no human in an internal role.

These obligations do not fix which form carries the theory. A complete
witness must show learning that responds to evidence in both notes and code
somewhere across the sequence, but no single learning step must change both
forms.

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

No reviewed system is an empirical witness. Factories with people in internal
roles, such as Fluent and the OpenAI agent-first account, come closest. They
have the shape of a user-facing house and supply project rationale, but
people keep the theory-building, generalization, or admission roles. Darwin
and Huxley Gödel Machines and HyperAgents train software around frozen
foundation models; Dynamic Cheatsheet and Voyager retain natural-language or
executable artifacts. None combines user-facing open-ended operation,
acquisition and revision of program theory, and continuation without a human
in an internal role. The harnesses among them are the practice the article
formalizes: memory files, self-written tests and tools, retained rules from
past failures. What their accounts do not say is whose learning an
improvement was. The person who noticed the recurring failure, diagnosed it,
and chose the rule did the credit assignment, and the accounts do not
separate that from what the harness did on its own. The internal-role
boundary and the obligations above are the instrument for that separation.
Commonplace, the knowledge base this article is written in, is the one
reviewed construction built to attack holding and acquisition directly,
through retained explanatory theory that later work loads and revises. It has
no witness run and is scored as a design target, not as evidence. The
[companion
map](./nearest-existing-constructions-to-a-reachability-witness.md) compares
twenty constructions and records the evidence behind each placement.

The broad conjecture does not require a theory stored as its own artifact: a
house may reliably reconstruct the understanding it needs from retained
records. The stronger hypothesis, call it the explicit-theory hypothesis, is
a prediction. Hold the model, source evidence, demand sequence, and inference
budget fixed. Then a rationale that can be found and revised on its own
improves coherent modification, diagnosis, or recovery, compared with raw
records or searching the artifacts directly. Both routes require retained
evidence to reach the relevant decision and actually change it. Only the
explicit route additionally requires selecting, retaining, and revising the
stored theory. That additional requirement tests the mechanism, not
reachability.

An [open-domain theory builder may itself become a software
house](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
when new domains require changes to its production machinery. That separate
conjecture is not needed for the reachability claim.

## Boundaries and epistemic status

The conjecture is existential: it says only that at least one such house
exists, for some eligible LLM, some arrangement of software and notes, some
product scope. The witness rules out, in advance, two ways of saving the
conjecture after a failure. The witness pins every eligible model and every
other learned component before testing, so that a newer model or another
newly trained component cannot quietly do the work. It also declares product
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

Practical usefulness, automated continuation, and learning by computation in
the way the Bitter Lesson favours are separate achievements. A house with
people in internal roles that substantially reduces programmer work is a
positive engineering and research result even if it never satisfies the full
conjecture. If decisive task-specific theory, decomposition, evaluation, or
selection remains repeatedly human-produced, however, the project has not
shown that its approach holds up under the Bitter Lesson. The system may
remain useful; what is missing is a reason to expect its durability and
scaling advantage, not a proof of failure.