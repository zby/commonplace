---
description: "Commonplace as a human-inclusive seed and a bootstrap program that separately transfers production decisions and the machinery behind them"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/software-house.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
---
# Bootstrapping the First Automated Software House

*A research program from human-agent production to human-free internal operation*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** The [first article](./automated-software-houses-with-fixed-llms.md)
conjectures that an automated software house is reachable with fixed current
LLMs. The [second](./the-software-house-as-the-unit-of-training.md) says that
project-specific learning should run over the whole house, not only over the
model. This article gives a bootstrap program for reaching the first witness.

Commonplace is a useful starting point, but not yet a completed computational
learner. It has operative retained theory, computational proposal and revision,
symbolic checks, and durable retention. People still supply decisive judgments
about global fit, admission, delayed credit assignment, and authority over
consequential changes.

The program separates two transfers. **Operational transfer** moves a production
decision from a person to computation. **Learning transfer** moves production
and revision of the machinery behind that decision into the house's own
production-driven learning loop. A hand-written validator can complete the
first transfer without completing the second. The program tries bounded
transfers in an order discovered from production, declares each trial before it
runs, measures outcomes outside the transferred role, and records rescues,
failures, reversals, and reopened roles. The first article's witness requires
operational transfer across every internal production role in its declared
scope and horizon; it does not additionally require learning transfer. A house
trained as the second article prescribes needs learning transfer as well, and
the program aims at both.

## The starting point

A [software house](../notes/definitions/software-house.md) is whatever keeps
changing a piece of software for its users. The houses from which this program
proposes to bootstrap are human-agent systems. Coding agents may write and test
much of the code while people supply requirements from outside and still fill
internal roles such as: noticing that several failures share one cause,
deciding that a design assumption no longer holds, choosing among changes that
all pass the tests, approving new evaluators, and authorizing changes with
effects beyond the current job.

Commonplace, the knowledge base in which this series is written, is a house of
this kind. Agents produce notes, code, and reviews. Retained project theory is
loaded into later work. People still choose objectives, judge global fit,
assign blame for failures, approve evaluators, and authorize consequential
changes.

The first article draws the boundary that matters here. An *internal role* is
work the house depends on to produce the software, whoever performs it. A person
in such a role is inside the house. A person who supplies requirements, facts,
observed outcomes, or acceptance judgments about visible behaviour is a user
and stays outside. An automated house has no person in an internal role over
its declared scope and horizon.

The distance to that endpoint is not just a list of jobs to automate. It has two
parts. The house must stop depending on people for production decisions, and it
must stop depending on people to keep supplying the project-specific machinery
that makes those decisions possible.

## Commonplace as a seed instance

The second article says that a trained house needs retained components that
affect later production, a process by which production evidence changes them,
admission of accepted changes, credit assignment from later consequences, and
retention that makes accepted changes operative. Commonplace has a partial
implementation of this shape. It does not yet perform every part
computationally.

- **Retained theory is an update surface.** Notes state claims, scope, and
  evidence, and link to the claims they depend on. Agents can load them at the
  point of decision. A defeated note can be revised, superseded, or withdrawn,
  with its address redirected to its replacement.
- **Some recurring failures have produced machinery.** For example, evidence
  that bounded reviewers could pass material they had not read led to [a
  validator rule that limits unquoted source use on the
  artifact](../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md).
  Other repeated operator corrections have been retained as instructions for
  later passes.
- **Review supplies evaluation and provenance, not full admission or credit
  assignment.** The [review system](../reference/README-REVIEW-SYSTEM.md)
  records verdicts against pinned note and criterion snapshots. This shows
  which note and criterion formed the registered baseline and when either one
  changed. Review is opt-in, however, and a verdict does not itself decide which
  change is kept. Its [freshness
  model](../reference/review-architecture.md) also treats linked files as
  reading context rather than freshness inputs. Most importantly, staleness is
  not delayed credit assignment: it does not show that a later production
  outcome was caused by an earlier change.
- **Some episodes record who decided.** One revision records that [the model
  retrieved retained theory, searched over formulations, and produced edits,
  while the operator supplied the decisive judgments about global
  fit](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).
  This is the kind of accounting the bootstrap needs.

People still choose objectives, judge whether a claim fits the larger theory,
assign blame when a change fails, decide which review findings to accept,
approve new gates, and authorize changes whose effects reach beyond the current
job. Nothing here shows acquisition of project theory by computation alone, and
there has been no witness run in the first article's sense.

The useful claim is narrower. Commonplace already has several surfaces named by
the proposed learning process: retained theory, computational proposal and
revision, symbolic checks, review provenance, and durable retention. Its
remaining human roles can be named and measured. It is a seed implementation of
the program, not proof that the program already works.

A bare memory file is weaker. It can affect later behaviour, but it may admit
entries without a settled rule, keep wrong entries without tracing later
failures back to them, omit their scope, and leave unclear whether a person or
the harness chose the rule. A harness can add the missing parts. The difference
is the process around the file, not the file's name.

## The bootstrap program

**The bootstrap program.** Starting from a human-agent house with operative
retained project state, try repeated, measured transfers of bounded production
decisions. For each decision class, or the smallest coupled bundle that cannot
be separated, build the missing premises, acceptance authority, independent
checks, and continuity machinery. Then test two claims separately: whether
computation now performs the production decisions, and whether production
evidence now causes computationally produced changes to the machinery that
performs them.

The global order is discovered from production. Each local trial is declared
before it runs. Its boundary, objective, horizon, workload, human contribution,
expected transfer, outcome measures, and rescue rules are fixed for that trial.
Failed, reversed, and reopened transfers remain part of the evidence.

The path is incremental, but it need not be smooth. One transfer may create a
new review role. Two roles may have to move together. A later demand may expose
that an earlier transfer covered only routine cases. The bootstrap can use
human rescues while learning from such failures. The human-free witness lineage
starts only when those rescues stop.

The quantity that should contract is the set of required human decisions, not
the number of people. One operator may stop doing one internal role while still
doing several others.

## The readiness conditions

A decision can move out of human hands with warrant when the automatic process
has the premises it needs, an acceptance rule or grant of authority settled
enough to apply, and a check independent enough to reject a plausible harmful
candidate. It also needs continuity when the decision or its evidence arrives
after the current run.

If a house first transfers decisions that meet these conditions, the decisions
left with people should become enriched for missing premises, unsettled
criteria, weak checks, and delayed consequences. This is a prediction about the
transfer policy, not a claim that every real automation path already follows
it. The
[residue analysis](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
turns the remaining work into a list of missing functions:

| Why a decision stays human | What the program must build |
|---|---|
| A needed premise is unavailable | Representation, retrieval, or acquisition of that premise |
| No objective, criterion, commitment, or grant of authority settles acceptance | A settled rule or represented grant of authority within declared limits |
| No independent check can defeat a wrong candidate | Verification, criticism with different failure modes, delayed exposure, or an accepted error tolerance |
| The decision arises after the automatic path stops | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | No new capacity; wait for the cost to fall |

The table says what is ready; it does not give a full schedule. Among several
ready transfers, value, cost, risk, and dependencies decide which one to try
next. A role whose only missing premise is already recorded may be cheap to
move. A role with an unsettled criterion must wait for more decided cases. A
role with no usable check must wait for a stronger check or a declared tolerance
for error.

Different residue classes require different
[functions](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md):
representation, interpretation of settled guidance, verification, and
continuity. Commonplace currently realizes these through natural-language
notes, LLM interpretation, symbolic checks and scheduling, and retained
evidence. The final house need not keep those forms separate. The program
requires the functions, not a permanent split among notes, models, and code.

## What is fixed for each trial

The program does not declare a universal sequence of stages. Production decides
which transfer is ready next. But adaptive global order does not license a
story written after the result. Before each attempted transfer, the program
records:

- the decision class or coupled bundle;
- the declared workload, boundary, objective, and horizon;
- which decisions people currently supply;
- which premise, rule, check, or continuity mechanism is thought to be missing;
- the separate operational-transfer and learning-transfer claims;
- external outcome, cost, rescue, and reopening measures.

The result is then kept whether the transfer succeeds or fails. This prevents
the discovered order from becoming only a list of successful cases.

Operative retained state is a prerequisite for a claim that the house learns
from what it retains. It need not be the first operational transfer. A narrow
hand-written rule may move a routine decision before retained theory has shown a
causal effect. That is real automation, but not yet evidence of learning by the
house.

Admission can also move in parts before the endpoint. A deterministic formatter
or a well-tested dependency update may already be admitted automatically. At
the training endpoint, project-specific successors must become operative over
the declared scope without a person choosing them, and production evidence must
be able to revise the update machinery when it fails. In an architecture with
an explicit admission gate, this includes computational admission and revision
of its machinery. That is an endpoint obligation, not a claim about the literal
last chronological move.

Requirements, facts, outcomes, and acceptance judgments about visible behaviour
remain with users throughout. Those are outside inputs, not internal roles.

## Two kinds of transfer

A single statement that a role "moved" hides two different claims.

| Claim | What must be shown |
|---|---|
| **Operational transfer** | Computation now makes the declared production decisions, including hard cases, without a person supplying them. External outcome and cost measures remain acceptable. |
| **Learning transfer** | Production evidence causes the house's own process to produce or revise the project-specific machinery that makes those decisions, and the retained change affects later work. |

A hand-written validator can complete operational transfer. It makes the
declared production decision inside the house without a person being present at
each case. But its criterion still came from a person. It does not complete
learning transfer until the house can produce or revise that criterion and its
machinery from production evidence.

The first article's witness does not require learning transfer, but operational
transfer alone is not the full witness. A wholly hand-built starting house can
be a witness if, with nobody inside, it also satisfies the program-theory,
coherent-revision, and practical-reliability conditions. It is not a trained
house in the second article's sense if none of its project-specific machinery
was produced from production evidence by the house's own process. The program
aims at both transfers, since the point of reaching the witness is to train it.

Operational transfer can look complete while a person still handles the cases
that matter. A person who fixes the three hard failures each month still holds
the diagnosis role. The accounting must record who made each decision class,
on which demands, and when. After the declared start of a human-free witness
lineage, any internal diagnosis, successor selection, or state edit by a person
is a rescue and breaks that lineage. During the bootstrap, the same rescue is
allowed but must remain visible.

Transfers may also reopen. A new demand can show that a rule covered only the
old workload, or that moving one role created another human review role. A
reopened role returns to the human set until the missing function is built. The
program measures contraction over declared windows; it does not assume every
step is permanent.

Quality can fall when the metric that would have caught the drop moves with the
role. A path can be computationally closed while its evaluator is captured. A
no-op loop, bad objective, or self-approving evaluator can run without people.
[Usefulness, autonomy, warrant, and power are separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).
Each transfer claim must say which one moved. The program therefore keeps an
outcome measure outside the transferred role: user-visible success on later
demands, escaped failures, and total cost.

The wrong benchmark can hide the remaining human roles. A test that compares an
agent with a remote programmer while holding the same brief, tools, feedback,
and client fixed measures the worker role under that division of labour. It
[does not test the client decisions it holds
fixed](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md),
such as task choice, missing premises, feedback, and final acceptance.

## What the house's training must produce

The operational path could be built entirely by hand: one validator for every
recurring judgment, one diagnosis procedure for every failure class, and one
fixed admission policy. That could produce an automated house in the first
article's sense, and a witness for its conjecture. It would not produce a
house that trains as the second article prescribes, because the
project-specific machinery would still come from people rather than from the
house's own process.

The seed is legitimate. People may write the first notes, tools, checks, and
safety boundaries. Later transfers must increasingly depend on machinery that
the house produces and retains from production evidence. The seed is outgrown
when [learning displaces repeated human construction of the task-specific
knowledge it supplied](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
over the claimed scope. New theories, checks, decompositions, and evaluators
then come from the house's own process rather than another round of human
design.

This does not require every component to change. General machinery such as the
version-control system, test runner, or model client may [stay fixed when its
scope is warranted](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
It becomes a revision target only when the declared scope needs a change it
cannot supply. The burden is on project-specific specialization, not on changing
every inherited tool.

In the current explicit-artifact path, machinery is usually produced
through a [proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md):
produce candidates, evaluate them with a real chance of rejection, and make an
accepted change operative. Early in the bootstrap a person may supply the final
rejection. Later, more of that gate moves into the house. Other update forms are
also allowed. Reward-, error-, viability-, or gradient-driven updates may change
the house without a separate candidate-admission event. The doctrine requires
an evidence-caused operative change, not one permanent update architecture.

## Stop or redirect conditions

The program is a bet. The following patterns, observed in a declared regime,
are reasons to stop or change the route rather than attempt the next transfer.

- **Retained state makes no causal difference.** Repeatedly withholding or
  replacing project state does not change later decisions in the predicted
  way.
- **The human set does not contract.** Interventions per demand stay flat or
  rise, transferred roles repeatedly reopen, or each transfer creates equal or
  harder human work elsewhere.
- **Each new demand class needs new human design.** A person must supply a new
  ontology, evaluator, or decomposition whenever the scope expands.
- **Evaluation becomes self-confirming.** The house's approval is the only
  evidence of quality, while external outcomes stop tracking it.
- **A more direct method wins at comparable total cost.** Reconstruction from
  raw records, direct search, or model adaptation reaches the same result more
  cheaply or reliably.

These results do not refute the existential conjecture by themselves. They show
that this path, in the tested regime, is not working or is not the best use of
resources. The same production history that supports a transfer must also be
able to reveal these failures.

## Where this leaves the series

The first article asks whether an automated software house can exist and states
what a witness must show. The second asks how a software house should learn and
puts governed behaviour-changing writes at the center.

This article supplies the construction program. Commonplace is not already the
finished trained house. It is a seed with operative retained state,
computational search, partial evaluation machinery, durable retention, and
named human residuals. The path from that seed has two coupled contractions:
fewer production decisions supplied by people, and less project-specific
production machinery supplied by people. Measuring both keeps ordinary
automation from being mistaken for learning. It also keeps a learning loop that
still needs human approval from being called a human-free house.
