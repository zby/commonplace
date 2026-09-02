# The reachability conjecture: train the house, not the LLM

**TL;DR.** A software house is whatever keeps developing and changing some
software for its users, over time, in response to what they ask for and what
happens in use. The conjecture is that such a house can be built to run with
no human in a production role, using only models that exist as of 2026-09-02,
and handling requests nobody listed in advance. Getting there does
not wait for a better model. The model stays fixed. People write the first
version of the code and notes around it; from then on the house changes them
itself, as it works, and the parts people wrote stop being what carries it.

## Claim

**The reachability conjecture.** At least one automated [software
house](../../notes/definitions/software-house.md) capable of open-ended coherent
software change is practically reachable with LLMs available by 2026-09-02.

The LLMs stay fixed: no new architecture, no further training, no waiting for
a more capable model. What gets trained is the software house, through
computationally produced and retained changes to two legible
[representational forms](../../notes/definitions/representational-form.md):
executable software and persistent natural-language notes.

A person may write the initial software and notes. Practical reachability
means that, within a declared product scope, operating horizon, and resource
envelope, computational training then discovers and maintains the decisive
project-specific structures, until no human is needed in an internal
production or theory-holding role. A system that people must keep redesigning
by hand has not reached that point.

## Why the substrate could suffice

Open-ended change brings demands nobody analysed in advance, and questions of
fit that the available checks do not settle. Say a product built for one
customer per deployment must now serve many tenants. The tenant identifier can
enter the data model in several ways; all of them pass the existing tests;
only some preserve the assumptions the rest of the code silently relies on.
Choosing among them needs what Naur called a program theory: the capacity to
relate the software to the activity it supports, to explain why it is
organized as it is, and to relate a new demand to that organization. [Holding
a program theory means sustaining coherent search under delayed
feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md):
the multi-tenant choice may not show its consequences until the next three
demands arrive.

Naur's evidence was a compiler whose original team could extend it cleanly
while a second team, working from the same code and documentation, produced
patches that fit badly. He concluded that the theory lives in people, because
its judgments cannot be reduced to a finite set of formulated criteria. An LLM
is still formal computation. What has changed is that a machine can now apply
informal project-specific state — a paragraph explaining why the retry logic
lives in the caller — without first translating it into a complete symbolic
decision procedure. A computational house could therefore pass Naur's
functional test while leaving intact his claim that the theory cannot be
written as rules. It would refute only his unproved step from "not rules" to
"only people". [The distinction is between formal execution and explicitly
formulated
criteria](../../notes/naur-equates-machine-execution-with-formulated-criteria.md).

The conjecture assigns each component a role:

- Fixed current LLMs supply the general linguistic, programming, and reasoning
  capacity that interprets project state and produces candidate changes.
- Natural-language notes supply the persistent project-specific state:
  purposes, commitments, explanations, evidence, and prior search. For
  example: "installs must be a single file, so the store is SQLite; do not add
  a server dependency."
- Executable software supplies exact behaviour and continuity: the product
  itself, tools, the script that assembles a prompt from the relevant notes,
  schedulers, validators and tests, rollback through version control, and the
  rules for what gets retained.

None of these holds the theory alone. A note nobody loads is inert. A fixed
LLM without enough project state reconstructs or guesses instead of carrying
understanding from one change to the next. Software executes a decision
without supplying the judgment that selected it. The composite has to exhibit
the theory-holding capacity.

## Training in legible forms

Legible means inspectable and directly revisable. It says nothing about how
easily the useful state can be designed: good notes and good tooling may have
to be found through search, criticism, trials, production consequences, and
retained correction, much as weights are found through gradient descent — and
they stay readable once found.

This is compatible with the Bitter Lesson because [the lesson selects how
behavior-shaping structure is produced, not the form in which it is
retained](../../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Learned software and notes do not lose merely because they are localized and
legible. A hand-crafted seed is compatible only if [learning outgrows the
task-specific knowledge the seed
supplies](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
Those two points answer the categorical objection; whether training over
legible structures scales is what the program has to demonstrate.

Current LLMs can produce both forms, and software can decide whether a
proposed change becomes operative and feed later consequences into the next
update. The conjectured training path:

```text
production evidence + fixed LLMs + present software and notes
  -> computational update of software and/or notes
  -> retained successor software and notes
  -> later production
```

The update mechanism is open. It may produce the successor directly or
separate proposal, evaluation, and selection. A successor theory may come from
editing the prior notes, from discarding them and rebuilding from the
evidence, or both.

Not every retained change is learning. A transition counts as learning when
experience causes a retained change that affects later production. Fixing a
bug changes the product. Adding a validator because that bug class recurred,
so that the validator later blocks the same class, changes production — that
is learning. A note written and never loaded by any context assembly changes
neither.

Hand-crafted tools, stores, interfaces, safety boundaries, and provisional
notes may start the loop. They are seed engineering, not evidence that the
house acquired anything. The training path must outgrow repeated human
authorship of the decisive project-specific theory, in whichever form a person
put it: a hand-written check that rejects every schema change encodes the
human's theory that the schema is settled, just as a note saying so would.
Machinery that implements a general production method — git, the test runner,
the model client — may stay fixed for as long as the declared scope stays
within what it handles. A house that is wholly hand-built at the end would
show that software and notes can carry the theory; it would not show the
training path.

Whether the production machinery must itself change within the declared scope
is an empirical question the theory does not decide. If it must — say the
relevant notes stop fitting the context window and the house needs a tag
index to select them — then the automation obligation below already requires
the house to make that change, and the forward argument applies to the
machinery as it does to the product: coherent open-ended change to it needs a
program theory of it. Self-application is a possible consequence of
automation, not a separate requirement.

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
3. **Successor acquisition.** When experience exposes an inadequacy — a
   dependency change makes a recorded design reason false — it comes to hold an
   adequate successor, by editing, rebuilding, or both.
4. **Automated continuation.** It sustains these capacities across the declared
   scope and horizon with no human in an internal role. Users may still supply
   requirements, feedback, domain knowledge, and acceptance judgments.

Computational training of the legible state is a condition on obligations 2
and 3, not a further stage.

## A consequence for general theory builders

The same components appear when the target is a persistent automated system
that builds, tests, and revises natural-language theories for external users
across domains not fixed in advance — a knowledge base like this one, operated
without its maintainers. At present an LLM is the only generally available
computational interpreter for semantic operations over theories of that
breadth. The corpus, exact state transitions, scheduling, checks, and rollback
need software outside model interpretation: [code complements the
weight–prompt pair with independently executed symbolic
operations](../../notes/code-complements-weight-prompt-with-symbolic-operations.md),
and [symbolic scheduling avoids using an LLM for unreliable
bookkeeping](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).

New domains bring new manipulation requirements as well as new content. A
domain whose claims must be compared across versions of a source needs
snapshot pins in the note schema and a validator for them, which the earlier
domains never needed. If no fixed harness anticipates all such requirements,
the builder must revise its own supporting software. Whoever repeatedly
supplies those demand-specific changes fills an internal role in the complete
builder, so an automated builder brings that role inside. It then persistently
develops and evolves software in the service of its external users and meets
the software-house [definition](../../notes/definitions/software-house.md).

The reachability claim does not depend on this link. It is a conjecture; a
fixed harness that sustained a general theory builder across genuinely new
domains would break it without touching the forward argument.

## Boundaries and epistemic status

The conjecture is existential: some current LLM, some arrangement of software
and notes, some product scope. Two rescues are ruled out in advance. The
witness pins the model versions it admits before testing, so that a newer
model cannot quietly do the work. And it declares product scope, horizon, and
resource envelope before testing, so that the scope cannot shrink until fixed
machinery suffices. Open-ended means the declared demand stream admits
relevant novelty: one web application whose users keep asking for things
nobody listed qualifies; a fixed set of fifty tasks does not.

Software and notes delimit the house's trainable internal state. Products,
user demands, tool outputs, and operating consequences are its work and
evidence.

The software-house definition requires none of holding, acquisition, training,
learning, or automation. Those are properties of the target this program
constructs.

The need for a program-theory function is a theoretical argument, not a
proved theorem. Current-LLM sufficiency and the practical training path are
conjectures. The program is constructive: a working system establishes
reachability over its declared scope, horizon, and envelope. Failure of one
architecture eliminates that path; it cannot refute the existential claim
unless the search has first been bounded.
