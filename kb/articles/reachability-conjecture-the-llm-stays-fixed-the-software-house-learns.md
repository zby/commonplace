---
description: "Conjecture that an automated software house capable of open-ended coherent change is reachable with fixed current LLMs by training the surrounding software and notes; the program-theory argument, training path, and witness obligations"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/axes-of-artifact-analysis.md
  - kb/notes/code-complements-weight-prompt-with-symbolic-operations.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
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

**TL;DR.** Call a software house whatever keeps developing and changing
software for its users, over time, in response to what they ask for and what
happens in use. The conjecture is that such a house can be built to run with
no human in a production role, using only models available by 2026-09-02,
and handling requests nobody listed in advance. The model stays fixed. What
changes is everything around it: the code the house runs on, and the notes
that record what the software is for, why it is built the way it is, and
what earlier changes taught. People write the first version of both, and the
house revises them as requests and their consequences arrive. People still
correct it at first. The bet is that each round needs less correction, until
keeping that understanding current no longer depends on people.

## Claim

**The reachability conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) capable of open-ended coherent
software change is practically reachable with LLMs available by 2026-09-02.

The LLMs stay fixed. What gets trained is the house, through computationally
produced and retained changes to two legible [representational
forms](../notes/definitions/representational-form.md): executable software
and persistent natural-language notes. *Practically reachable* means success
within a declared product scope, operating horizon, and resource envelope of
compute, time, and cost. Within those bounds, training must discover and
maintain the decisive project-specific structures until no human is needed
in an internal production or theory-holding role.

## Why the substrate could suffice

Open-ended change brings demands nobody analysed in advance and questions of
fit that the available checks do not settle. Say a product built for one
customer per deployment must now serve many tenants. The tenant identifier can
enter the data model in several ways. All of them pass the existing tests, but
only some preserve the assumptions the rest of the code silently relies on.
Choosing among them needs what the computer scientist Peter Naur called a
program theory: the capacity to relate the software to the activity it
supports, explain why it is organized as it is, and relate a new demand to
that organization. [Holding a program
theory means sustaining coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md):
the multi-tenant choice may not show its consequences until the next three
demands arrive.

[Naur's evidence](../sources/programming-as-theory-building.ingest.md) was a
compiler whose original team could extend it cleanly while a second team,
working from the same code and documentation, produced patches that fit
badly. He concluded that the theory lives in people because its judgments
cannot be reduced to a finite set of formulated criteria. An LLM is still
formal computation. What has changed is that a machine can now apply informal
project-specific state, such as a paragraph explaining why the retry logic
lives in the caller, without first translating it into a complete symbolic
decision procedure. A computational house could therefore pass Naur's
functional test while leaving intact his claim that the theory cannot be
written as rules. It would refute only his unproved step from "not rules" to
"only people". [The distinction is between formal execution and explicitly
formulated criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

AI researcher Jürgen Schmidhuber's [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is a proof-governed construction that rewrites its own code. It is not a
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

The conjecture assigns each component a role:

- Fixed current LLMs supply the general linguistic, programming, and reasoning
  capacity that interprets project state and produces candidate changes.
- Natural-language notes supply the persistent project-specific state:
  purposes, commitments, explanations, evidence, and prior search. For
  example: "installs must be a single file, so the store is SQLite; do not add
  a server dependency." Architecture decision records are the existing
  practice closest to this. The notes generalize them, and Naur's theory is
  what a decision record tries to write down.
- Executable software supplies exact behaviour and continuity. This includes
  the product, tools, context assembly, schedulers, validators and tests,
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
localized and legible. A hand-crafted seed is compatible only if [learning outgrows the
task-specific knowledge the seed
supplies](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
Those two points answer the categorical objection; whether training over
legible structures scales is what the program has to demonstrate.

Current LLMs can produce both forms. Software can make a proposed change
operative and feed later consequences into another update. The process is a
schematic loop, not a formal model:

```text
production evidence + fixed LLMs + present software and notes
  -> computational update of software and/or notes
  -> retained successor software and notes
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
or separate proposal, evaluation, and selection. It may edit the prior notes,
rebuild them from the evidence, or combine both methods.

A retained change counts as learning only when experience causes it and it
affects later production. Adding a validator because a bug class recurred, so
that the validator later blocks that class, qualifies. A note never loaded by
context assembly does not.

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
system transparent. The fixed LLM remains distributed-parametric, and enough software
and notes can [exceed practical
inspection](../notes/opacity-is-a-scale-threshold.md). The difference is where
the learned project-specific state lives. Fine-tuning spreads it across
weights, where a changed behaviour is hard to locate, inspect, or revert on
its own. Training the house keeps it in localized units. The house can
identify a changed claim or function, inspect its history, revise it
selectively, and roll it back without retraining the model.

Learning can then happen in deployment. Production evidence can cause a
retained change to a note, test, tool, or policy, and that change can affect
the next round of work without a training run.

A further payoff is possible but not required by the conjecture. When retained program theory captures structure that survives a
change, the house [may need fewer new observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can revise one premise and derive several consequences instead of
relearning them separately. This advantage depends on the theory being both
adequate and faithfully connected to later decisions; otherwise its breadth
creates negative transfer. Fewer observations also need not mean lower total
cost once theory search, validation, retrieval, and maintenance are counted.

## Obligations of a constructive witness

One construction must eventually demonstrate the whole progression:

1. **Holding and application.** Given adequate project-specific state, the
   composite uses a program theory across novel changes. The test is a change
   that violates a recorded rationale without violating any stated rule: a
   house that holds the theory adapts or declines; one that only paraphrases
   makes the change and cites the note.
2. **Initial acquisition.** From permitted records, interaction, and
   participation in the work, it builds an adequate theory instead of receiving
   the decisive theory from a human.
3. **Successor acquisition.** When experience exposes an inadequacy, such as a
   dependency change that makes a recorded design reason false, it comes to
   hold an adequate successor, by editing, rebuilding, or both.
4. **Automated continuation.** It sustains these capacities across the declared
   scope and horizon with no human in an internal role. Users may still supply
   requirements, feedback, domain knowledge, and acceptance judgments.

Computational training of the legible state is a condition on obligations 2
and 3, not a further stage.

## Nearest existing constructions

No existing system is a witness, but several hold one piece, and placing
them shows what the obligations exclude. The [Darwin Gödel
Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
and the [Huxley-Gödel
Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
rewrite coding agents around frozen foundation models and admit a child on
viability or on estimated lineage productivity.
[HyperAgents](../agent-memory-systems/reviews/hyperagents.md) replays
benchmark-selected patches into the code its next generation edits. All
three train software with the model fixed. What they retain is code, not the
reasons a later change must respect. [Dynamic
Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md) retains
the other form: a natural-language cheatsheet curated from solver traces and
read back into later prompts, with no gate beyond the curator and no change
to software. [Voyager](../agent-memory-systems/reviews/voyager.md) admits an
executable skill when a critic reports success and replaces a skill rather
than revising it. None of the five serves users. Their demand streams are
benchmarks or a game environment, which the open-endedness rule excludes.
Each answers part of obligation 1's question about the substrate. Obligations
2 and 3 concern acquiring and revising a program theory, and none of the five
is set up to test that: what they retain and revise is judged by score or
viability, not by whether it explains why the software is organized as it
is.

Many builders of such systems expect obligations 2 and 3 to follow without
further machinery. The simplest version of that expectation is that an LLM
given a record of its failures will generate the theory. The conjecture
predicts otherwise. A record influences later behaviour only through a
consumption path: something must load it into the context of the right
call, with enough force to change the decision, at the moment the decision
is made. A failure log left in a directory is advice nobody reads. Turning
it into a theory that later changes respect requires the admission and
credit-assignment decisions above, retention in a form later calls consume,
and enough authority over those calls to matter. Which machinery is missing
in a given system can be stated precisely by recording how each retained
artifact acts, by [its storage, representational form, lineage, and
behavioural authority](../notes/axes-of-artifact-analysis.md). That record
is how the placements above were made, and it is the instrument this
program uses to say what a witness needs.

## A consequence for general theory builders

The same components appear when the target is a persistent automated system
that builds, tests, and revises natural-language theories for external users
across domains not fixed in advance, such as this knowledge base operated
without its maintainers. At present an LLM is the only generally available
computational interpreter for semantic operations over theories of that
breadth. Symbolic systems perform such operations only over domains someone
has already formalized. The corpus, exact state transitions,
scheduling, checks, and rollback need software outside model interpretation:
[code complements the weight–prompt pair with independently executed symbolic
operations](../notes/code-complements-weight-prompt-with-symbolic-operations.md),
and [symbolic scheduling avoids using an LLM for unreliable
bookkeeping](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).

We conjecture that such a builder is itself a software house. New domains
bring new manipulation requirements as well as new content. A domain whose
claims must be compared across versions of a source needs snapshot pins in the
note schema and a validator for them, which the earlier domains never needed.
A harness fixed in advance can anticipate only requirements someone has
already formulated, and a genuinely new domain brings some that nobody has.
So either the builder revises its own supporting software or a person does.
Whoever repeatedly supplies those demand-specific changes fills an internal
role in the complete builder, so an automated builder brings that role
inside. It then keeps developing software for its external users, which is
the software-house [definition](../notes/definitions/software-house.md).

This link is a conjecture, and the reachability conjecture does not depend on
it. A fixed harness that sustained a general theory builder across genuinely
new domains would refute the link without affecting the forward argument. [The
decisions that stay human, and what would move
them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops
this boundary.

## Boundaries and epistemic status

The conjecture is existential: some current LLM, some arrangement of software
and notes, some product scope. Two ways of saving the conjecture after a
failure are ruled out in advance. The witness pins the model versions it
admits before testing, so that a newer model cannot quietly do the work. And it declares product scope, horizon, and
resource envelope before testing, so that the scope cannot shrink until fixed
machinery suffices. Open-ended means the declared demand stream admits
relevant novelty: one web application whose users keep asking for things
nobody listed qualifies; a fixed set of fifty tasks does not. The stream also
bounds what is reachable, since the closure is taken under the demands the
house receives as well as its gate. Bare reachability is cheap: a gate that
admits anything makes every state reachable. The claim is that adequate
states are reached with usable probability inside the declared envelope.

Software and notes are the trainable internal state. Products, demands, tool
outputs, and operating consequences are its evidence. Holding, acquisition,
training, learning, and automation are requirements of this witness, not of
the base software-house definition.

The need for a program-theory function is a theoretical argument, not a
proved theorem. Current-LLM sufficiency and the practical training path are
conjectures. The program is constructive: a working system establishes
reachability over its declared scope, horizon, and envelope. Failure of one
architecture eliminates that path; it cannot refute the existential claim
unless the search has first been bounded.
