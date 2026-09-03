---
description: "Conjecture that an automated software house capable of open-ended coherent change is reachable with 2026 LLMs while distributed-parametric state stays fixed and localized natural-language and symbolic state learns; the program-theory argument, training path, and witness obligations"
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

**TL;DR.** A *software house* is whatever keeps changing a piece of software
for its users, as they ask for things and as the software is used. The
conjecture is that such a house can run with no human in a production role,
on models that already exist, and handle requests nobody listed in advance.
**The models stay fixed; learning happens in the software and project state
around them:** code, notes, and the machinery that makes both affect later
work. People write the first versions. The house then revises them as requests
and their consequences arrive, and people correct it at first. **The bet** is
that the correction required falls over training until the house keeps its own
state and software adequate without people. Whether it does better by writing
its understanding down as addressable theory than by rebuilding it from raw
records is a separate, stronger hypothesis.

## Claim

**The reachability conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) capable of open-ended coherent
software change is practically reachable with LLMs available by 2026-09-02.

The eligible model versions and other distributed-parametric internal state
stay fixed. What gets trained is the house, through computationally produced
and retained changes to localized [natural-language and symbolic
state](../notes/definitions/representational-form.md): notes, code, schemas,
tests, tools, and production policy. Derived indexes may be regenerated from
that canonical state under pinned machinery, but they are not independently
trained or treated as learned state. *Practically reachable* means success
within a declared product scope, operating horizon, and resource envelope of
compute, time, and cost. Within those bounds, training must discover and
maintain the decisive project-specific structures until no human is needed in
an internal production or theory-holding role.

## Why the substrate could suffice

Open-ended change brings demands nobody analysed in advance and questions of
fit that the available checks do not settle. Say a product built for one
customer per deployment must now serve many tenants. The tenant identifier can
enter the data model in several ways. All of them pass the existing tests, but
only some preserve the assumptions the rest of the code silently relies on.
Choosing among them needs what the computer scientist Peter Naur called a
program theory: the capacity to relate the software to the activity it
supports, explain why it is organized as it is, and relate a new demand to
that organization. [Holding a program theory means sustaining coherent search
under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md):
the multi-tenant choice may not show its consequences until the next three
demands arrive.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
showed that full code, annotations, extensive design discussion, and personal
advice did not give a successor team enough program-specific understanding;
more prose of the same kind is not an answer. But it tested [one historically
bounded documentation-and-consumption
system](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md),
not linked rationale, machine-maintained indexes, semantic retrieval,
dependency-aware context assembly, or decision-point activation. Whether a
newer representation-plus-consumption system transfers more of the required
capacity, to people or to an LLM-based composite, remains empirical.

Naur's human-only conclusion also relied on identifying machine execution with
execution of formulated criteria. An LLM is still formal computation, but it
can interpret a paragraph explaining why retry logic belongs in the caller
without that judgment first being translated into a complete symbolic decision
procedure. A successful house would falsify Naur's human-only conclusion while
leaving intact his claim that the relevant judgment cannot be reduced to a
finite formulable rubric. [The distinction is between formal execution and
explicitly formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
Whether a composite meets his functional criterion is a longitudinal question:
project-specific state must shape proposal, evaluation, diagnosis, or recovery
on implications not stated verbatim, and interventions on that state must
change the modification path.

The conjecture assigns each component a role:

- Fixed current LLMs supply the general linguistic, programming, and reasoning
  capacity that interprets project state and produces candidate changes.
- Natural-language notes supply persistent project-specific purposes,
  commitments, explanations, evidence, and prior search. For example:
  "installs must be a single file, so the store is SQLite; do not add a server
  dependency." Architecture decision records are a familiar partial carrier
  of such rationale.
- Symbolic software supplies exact behaviour and continuity. This includes the
  product, tools, schemas, context assembly, schedulers, validators and tests,
  version-control rollback, and retention rules.

None of these holds the theory alone. A note nobody loads is inert. A fixed
LLM without enough project state reconstructs or guesses instead of carrying
understanding from one change to the next. Software executes a decision
without supplying the judgment that selected it. The composite has to exhibit
the theory-holding capacity.

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
localized and legible. A hand-crafted seed is compatible only if [learning
outgrows the task-specific knowledge the seed
supplies](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
Those two points answer the categorical objection; whether training over
legible structures scales is what the program has to demonstrate.

Current LLMs can produce both localized forms. Software can make a proposed
change operative and feed later consequences into another update. The process
is a schematic loop, not a formal model:

```text
production evidence + fixed LLMs + present localized state
  -> computational update of natural-language and/or symbolic state
  -> retained successor state
  -> later production
```

The first arrow hides two hard decisions. Semantic admission is deciding which
meaning-bearing changes may enter retained state. Credit assignment is
deciding which earlier code, note, context route, test, objective boundary, or
selection policy a later consequence counts for or against. [Governing a
behaviour-changing write therefore requires selection, validation,
authorization, and
coordination](../notes/continual-learning-requires-governing-behaviour-changing-writes.md).
This article supplies no general solution to that problem. A witness must show
that its update process attributes evidence and admits successors well enough
to satisfy the acquisition and continuation obligations below. A user who
supplies requirements, feedback, domain knowledge, or an acceptance judgment
stays external. A person who repeatedly diagnoses the theory failure or
chooses the successor is doing the house's credit assignment and fills the
excluded internal role.

The update mechanism is otherwise open. It may produce a successor directly
or separate proposal, evaluation, and selection, and it may edit prior notes,
rebuild working understanding from retained records, revise software, or
combine these operations. A retained change counts as learning by the house
only when experience causes it and it changes how a later,
not-yet-specified production episode is conducted. Carrying forward the
product state an earlier request asked for is not enough, since the next
episode starts from the changed product either way. Adding a validator because
a bug class recurred, so that the validator later blocks that class, qualifies;
so does a product abstraction, invariant, or test that demonstrably shapes
later changes beyond that continuity. A note never loaded by context assembly
does not.

Hand-crafted tools, stores, interfaces, safety boundaries, and provisional
notes may start the loop. They are seed engineering, not evidence of
acquisition. The training path must outgrow repeated human authorship of the
decisive project-specific theory, whatever its form. A hand-written check that
rejects every schema change carries the human's theory that the schema is
settled, just as a note saying so would. A wholly hand-built end state would
show that software and notes can carry theory, not that the house learned it.
Because each successor is admitted by the prior state's gate, the house can
only occupy states reachable from the seed by admitted steps: the closure of
the seed under that gate and the demand stream. The gate is fallible and the
LLM samples, so the steps are nondeterministic, but the set of reachable
states is still fixed by the seed, the gate, and the demands. Outgrowing the
seed then means that this set contains states holding an adequate theory and
that the house reaches one of them.

General production machinery such as git, the test runner, or the model client
may stay fixed while it handles the declared scope. If the scope requires a
machinery change, such as a tag index once relevant notes stop fitting the
context window, the automation obligation below requires the house to make
it. Self-application is then a consequence of automation, not a separate
requirement.

## What this training route could buy

The alternative route is to train the model itself, by fine-tuning or
retraining its weights on project experience. Neither route makes the whole
system transparent. The fixed LLM remains distributed-parametric, and enough
software and notes can [exceed practical
inspection](../notes/opacity-is-a-scale-threshold.md). The difference is where
the learned project-specific state lives. Fine-tuning spreads it across
weights, where a changed behaviour is hard to locate, inspect, or revert on
its own. Training the house keeps it in localized units. The house can
identify a changed claim or function, inspect its history, revise it
selectively, and roll it back without retraining the model.

Learning can then happen in deployment. Production evidence can cause a
retained change to a note, test, tool, or policy, and that change can affect
the next round of work without a training run.

A further payoff is possible but not required by the conjecture. When
retained program theory captures structure that survives a change, the house
[may need fewer new observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can revise one premise and derive several consequences instead of
relearning them separately. This advantage depends on the theory being both
adequate and faithfully connected to later decisions; otherwise its breadth
creates negative transfer. Fewer observations also need not mean lower total
cost once theory search, validation, retrieval, and maintenance are counted.

## Obligations of a constructive witness

One construction must eventually demonstrate the whole progression:

1. **Holding and application.** Given adequate project-specific state, the
   composite sustains theory-guided proposal, evaluation, diagnosis, or
   recovery across novel changes, including cases whose correct handling is
   not stated verbatim in that state. Under matched conditions, withholding
   or replacing the relevant state changes the modification path in a
   predicted way.
2. **Initial acquisition.** From permitted records, interaction, and
   participation in the work, it acquires an adequate project-theory function
   instead of receiving the decisive project-specific understanding from a
   human. The function may be carried by explicit theory, reliable
   reconstruction from records, or mixed state.
3. **Successor acquisition.** When experience exposes an inadequacy, such as a
   dependency change that makes an earlier design reason false, it reaches a
   successor state that supports coherent later modification, by revising
   explicit theory, records, software, production machinery, or a combination.
4. **Automated continuation.** It sustains these capacities across the declared
   scope and horizon with no human in an internal role.

These obligations are carrier-neutral. A complete witness must demonstrate
evidence-responsive learning in both natural-language and symbolic state
somewhere across the sequence, but no single acquisition episode must change
both forms. Users may supply product-level requirements, facts, observed
outcomes, and acceptance judgments about visible behaviour. Implementation
diagnosis, internal candidate comparison, theory editing, or successor
selection counts as an internal role regardless of who supplies it.

Computational training of localized state is a condition on obligations 2 and
3, not a further stage. A partial mechanism for one of them is not partial
completion of it: storing or paraphrasing a rationale does not show that it
governed a decision, and a gate that can reject does not show that the
admitted successor was adequate. The [companion
map](./nearest-existing-constructions-to-a-reachability-witness.md) separates
what a carrier-neutral witness must demonstrate from the stronger test of
explicit retained theory.

## Nearest existing constructions

The formal corner is AI researcher Jürgen Schmidhuber's [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md),
a proof-governed construction that rewrites its own code. It is not a
software house: it has no users, and the only software it changes is itself.
It shows what automation costs when formulated criteria buy it. An embedded
prover admits a rewrite only after proving, from the machine's axioms and
utility formalization, that the rewrite pays. Everything the conjecture asks
the house to acquire is supplied there in advance as the formal acceptance
basis: the theory of the system is the axioms, the objective is the utility
function, the test is proof. Any of them may be rewritten, but only under a
proof from the formalization then in force. So the initial formalization
governs every successor by descent, and a demand nobody formalized cannot
enter the test. The paper states the price: the machine "must ignore those
self-improvements whose effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), verbatim).

Once no human is inside, the conjectured house is closed in the same way.
Every successor is admitted by the notes, software, and fixed LLM the prior
state supplies, so the seed governs the lineage by descent. The difference is
the admission relation. The Gödel machine admits only what its current axioms
derive. The house admits what a fallible gate accepts on production
consequences, and a consequence can contradict the current theory where a
proof cannot contradict its axioms. The house pays with fallibility instead.

No reviewed system is an empirical witness. Human-inclusive factories such as
Fluent and the OpenAI agent-first account are closest to the user-facing house
topology and supplied project rationale, but people retain theory-building,
generalization, or admission roles. Darwin and Huxley Gödel Machines and
HyperAgents train software around frozen foundation models; Dynamic Cheatsheet
and Voyager retain natural-language or executable artifacts. None combines
user-facing open-ended operation, acquisition and revision of program theory,
and continuation without an internal human. The [companion
map](./nearest-existing-constructions-to-a-reachability-witness.md) compares
nineteen constructions and records the evidence behind each placement.

The broad conjecture does not require a separately retained theory object: a
house may reliably reconstruct the understanding it needs from retained
records. The stronger explicit-theory hypothesis predicts that, with model,
source evidence, demand sequence, and inference budget held fixed, an
addressable rationale improves coherent modification, diagnosis, or recovery
relative to raw records or direct artifact search. Both routes require retained
evidence to reach the relevant decision with enough behavioural force. Only
the explicit route additionally requires selecting, retaining, and revising
the synthesized theory object. The companion map treats that as a mechanism
test rather than a condition of reachability.

An [open-domain theory builder may itself become a software
house](../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
when new domains require changes to its production machinery. That separate
conjecture is not needed for the reachability claim.

## Boundaries and epistemic status

The conjecture is existential: some eligible LLM, some arrangement of software
and notes, some product scope. Two ways of saving the conjecture after a
failure are ruled out in advance. The witness pins every eligible model and
other distributed-parametric component before testing, so that a newer model
or learned auxiliary component cannot quietly do the work. It also declares
product scope, horizon, and resource envelope before testing, so that the scope
cannot shrink until fixed machinery suffices. Open-ended means the declared
demand stream admits relevant novelty: one web application whose users keep
asking for things nobody listed qualifies; a fixed set of fifty tasks does not.
The declared stream is part of what the claim is about, since the reachable
states depend on the demands received. Bare reachability is cheap: a gate that
admits anything makes every state reachable. The claim is that adequate states
are reached with usable probability inside the declared envelope.

The cutoff and pinning bind a claim-establishing witness run, not ordinary
development. The project may build and deploy with newer models, and doing so
can show that accumulated state and machinery let a prepared project exploit a
newer model better than an unprepared one. That is evidence about the state's
value, not of reachability with models available by 2026-09-02. In a
claim-establishing run, a newer model must not supply trial-specific theory,
diagnose the trial's internal failures, select successors, or fill any other
excluded internal role. Derived indexes may change only as mechanical views of
localized canonical state under the pinned algorithms declared by the witness.

Localized natural-language and symbolic artifacts are the trainable internal
state. Products, demands, tool outputs, and operating consequences are its
evidence. Holding, acquisition, training, learning, and automation are
requirements of this witness, not of the base software-house definition.

The need for a program-theory function is a theoretical argument, not a proved
theorem. Current-LLM sufficiency and the practical training path are
conjectures. The program is constructive: a working system establishes
reachability over its declared scope, horizon, and envelope. Failure of one
architecture eliminates that path; it cannot refute the existential claim
unless the search has first been bounded.

Practical usefulness, automated continuation, and Bitter-Lesson-compatible
computational acquisition are separate achievements. A human-inclusive house
that materially reduces programmer work is a positive engineering and research
result even if it never satisfies the full conjecture. If decisive
task-specific theory, decomposition, evaluation, or selection remains
repeatedly human-produced, however, the project has not established its Bitter
Lesson durability argument. The system may remain useful; what is missing is a
warrant for its durability and scaling advantage, not a proof of failure.
