---
description: "Survey of eighteen self-improving systems placed against the four theory-builder conditions, with reported learning gains judged separately: five builders, one outside, twelve unsettled mostly on criticism; next experiments"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md
  - kb/notes/definitions/system-definition-artifact.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
---

# Which Existing Self-Improving Systems Are Theory Builders

> **Draft.** The claims, system selection, and comparisons may change.
> Comments, corrections, and additional candidates are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Existing self-improving systems already report gains from retained knowledge
and revised skills. They also supply mechanisms for diagnosis, criticism,
revision, and reuse. [Our program](./building-a-theory-builder-from-todays-llms.md)
asks two separate questions of each system. Is it a theory builder, a system
that states its theories, acts on them, criticizes what they say, and lets
the result of criticism shape its next conjecture? And does holding and criticizing those
theories improve its later decisions? A third question is whether the whole
process can run without people performing its internal roles.

This survey compares eighteen systems through retained code reviews, papers,
and practitioner reports. No reported outcome was reproduced here. It places
each system against the theory-builder conditions on the evidence cited, says
where that evidence does not settle the placement, and identifies which
experiments would resolve the remaining questions.

## Two precedents already test improvement

**Knowledge-Centric Self-Improvement** keeps the solver machinery fixed while
agents contribute experience to a shared knowledge base: "The only object that
changes is the curated knowledge base."
([Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
verbatim). Agents formulate claims in task forums, support or challenge them
with evidence, discuss which observations generalize across tasks, and distill
the results for later agents. Its protocol therefore includes criticism of
claims as well as benchmark evaluation.

The paper freezes a learned knowledge bundle and transfers it to unseen tasks;
a task-conditioned adapter "converts the shared donor asset into a short
memo" for the task at hand before the solver acts
([Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
verbatim). It reports
improved zero-shot performance on Polyglot and ARC-AGI-1. This tests
the value of the retained bundle beyond the tasks that produced it. A further
comparison would isolate what the criticism contributed to that bundle's
value.

**Memento-Skills** retains skills containing instructions and code. Its
comparison removes several parts of skill improvement together: "no failure
attribution, no skill rewriting, and no skill discovery"
([Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md),
verbatim). The full system reports 66.0% accuracy on the unseen GAIA test set,
against 52.3% for this ablation. That is evidence for the combined improvement
pipeline; separating failure attribution from rewriting and discovery would
test the contribution of diagnosis. The system also trains a skill router,
so its fixed solver weights do not make every component fixed-weight.

Both precedents address parts of the program's first testing goal: retained
changes improving later performance. Their remaining mechanism questions
call for narrower comparisons within the successful pipelines. Both are also
theory builders on this evidence, as the next section explains: their
retained units are stated, consumed on later tasks, and revised after
criticism aimed at a particular claim or skill.

## What the comparison asks

A system is a [theory builder](../notes/definitions/theory-builder.md) when
it meets four conditions:

1. **Localized content.** Its theories are stated in natural or formal
   language, so identifiable units, such as a claim, a skill file, or a
   ruling, carry their content.
2. **Consumption.** The theories guide what the system does through what
   they say. A difference in a theory's content that matters to a decision
   changes the decision; such a change is
   [operative](../notes/definitions/operative-change.md).
3. **Criticism.** A working process of attempted refutation aims at what
   identified units say, and a theory that fails is revised or replaced.
   Generating variants and keeping those with the best outcome score, with no
   stated reason bearing on what a variant says, is trial and error and does
   not meet this condition.
4. **Iteration.** The result of criticism, a revised theory or the record
   of criticism, is kept and shapes the next conjecture. Rounds of revision
   within one run meet this condition. How far results persist, within a
   run, across runs, or across problems, is graded, like addressability,
   and is not a condition. A critic whose report no next conjecture takes up
   does not meet it, and a run that freezes its result for another system to
   deploy ends the builder at the freeze.

The builder is the whole system that performs these operations, so people
who propose, criticize, or select theories are inside it. A human-staffed
system can therefore be a theory builder. The knowledge base calls a builder
in which computation performs every internal operation
[autonomous](../notes/definitions/theory-builder.md#qualifiers).

Membership is not a claim of success. Whether holding and criticizing a
builder's theories improves its capacity for future action is a separate
learning claim, and it needs an outcome comparison:
[observing the whole theory-to-use path does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md).
A system can be a theory builder without any shown gain.

We distinguish how a revision is produced from how it is accepted. A system
may diagnose a mistaken assumption, revise the theory, and use an outcome
gate to accept the revision. Testing a stated consequence can itself be
criticism. The gate alone tells us little about whether the preceding
process criticized a theory or simply generated another variant, so a gate
does not settle condition 3.

The program adds distinct questions to this learning test. Can all internal
roles run computationally with fixed model weights? Does the learned revision
transfer to new cases? Does retaining the assembled theory save work compared
with reconstructing it from the same evidence? A human-assisted system may
provide evidence of learning before it provides evidence of autonomy, as the
[bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
proposes for Commonplace.

## Where the reviewed systems stand

The placements below use only the evidence this survey cites. Where that
evidence does not show a condition, the placement is marked unsettled rather
than inferred from the neighbouring conditions. On that basis:

- **Theory builders (5):** Knowledge-Centric Self-Improvement and
  Memento-Skills, which also report gains, and three human-staffed systems
  without a measured gain: OpenAI's agent-first product, Warp's skill
  improver, and Commonplace.
- **Outside (1):** Rainbow, whose supplied model is never criticized.
- **Unsettled (12):** Fluent, Wheelhouse, the Darwin Gödel Machine, the
  Huxley-Gödel Machine, Recuris, Harness Continual Learning, Dynamic
  Cheatsheet, Voyager, HyperAgents, Autogenesis, Exo, and Prime Agent. Most
  are unsettled on condition 3: the evidence shows an outcome gate or a
  success report, not criticism aimed at what a retained unit says. No
  placement turns on persistence.

**Knowledge and skill pipelines with reported gains.** Knowledge-Centric
Self-Improvement meets the four conditions: its claims are stated,
challenged with evidence, distilled, and consumed through a memo on unseen
tasks. Memento-Skills meets them as well: failure attribution names one
responsible skill, rewriting changes what that skill says, and the retained
skills are used on the unseen test set.

**Human-assisted learning and machinery development.** These systems show
how people and agents retain knowledge and change their working machinery.
Because the builder includes whoever performs its internal operations, the
people in them are part of the system under assessment, not outside help.
Their reports also identify internal roles that remain human.

- [Fluent](../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
  retains product code, expertise, scheduling, rejection, and reuse; people
  and the system jointly settle the brief, the behaviour specification, and
  the approach. Practitioner-reported. Unsettled: the report shows review of
  work items, but not criticism aimed at the retained expertise.
- Wheelhouse, in Steve Yegge's report, moves human rulings from custom to
  warnings, written doctrine, and programs that refuse actions. The corpus
  retained "old rulings that were obsolete or had changed"
  ([Wheelhouse](../sources/steve-yegge-fences-not-sandboxes.ingest.md),
  verbatim), which is the maintenance cost of retention made visible.
  Unsettled: rulings are stated, enforced, and later changed, but the report
  cited here does not say whether a change answered criticism of what a
  ruling said.
- OpenAI's agent-first product keeps repository documents that explain the
  business domain and repairs them recurrently. People generalize: when
  agents struggle, engineers ask "what capability is missing? What
  constraint is unenforced?" and build the tool, linter, or test
  ([agent-first product](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md),
  verbatim). A human-staffed theory builder: the documents are stated,
  consumed by later agent work, and repaired when what they say is found
  wrong. No gain from them is measured.
- [Warp's scheduled skill improver](../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
  admits skill updates through human feedback and review. A human-staffed
  theory builder: an improver proposes an edit to what the skill says,
  people review the edit, and later runs use the updated skill. The account
  does not show that accepted edits improve later outcomes.
- Commonplace retains explanatory notes with scope and evidence and revises
  them under review; its
  [system-definition artifacts](../notes/definitions/system-definition-artifact.md)
  describe the machinery. One
  [recorded episode](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
  shows retained theory guiding computational search with the operator
  selecting what fit, without ablation. Models are not reliably pinned.
  Commonplace is a reflective, human-staffed theory builder whose learning is
  not yet shown.

**Automated revision, selection, and reuse.** These systems automate parts of
the path from experience to later behavior. The entries distinguish the
retained change from the mechanism that selects or consumes it. Placing them
requires tracing a formulated theory and its criticism through that path, and
the evidence cited here does not complete the trace for any of them.

- The Darwin Gödel Machine evolves coding agents around frozen models; a
  fixed diagnostician suggests improvements from the parent's logs, and
  admission is viability: "Only agents that compile successfully and retain
  the ability to edit a given codebase are added to the DGM archive"
  ([Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md),
  verbatim). Diagnostic rationale is not shown to persist across
  generations. Unsettled on condition 3, since admission is by viability and
  score. Later generations build on archived agents, so results persist
  across the run; the evidence cited does not show the archive taken up on a
  problem other than the one it evolved on, which bears on its persistence
  grade, not on membership.
- The [Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
  replaces score with descendant productivity for parent selection, and
  reports that immediate score predicts it poorly. Unsettled on condition 3
  for the same reason as the Darwin Gödel Machine, with the same run-level
  persistence.
- Recuris proposes memory patches from traces and decides each through a
  deterministic paired held-out gate, with the memory coordinates supplied
  in advance: "The memory only grows, and it can afford to."
  ([Recuris](../sources/recursive-experiential-working-memory-evolution.ingest.md),
  verbatim). Unsettled on condition 3: patches are proposed from traces, but
  a memory that only grows shows no retained entry revised or rejected.
- [Harness Continual Learning](../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
  retains edits that improve the current task, respect sampled anchors, and
  pass validity checks; held-out forgetting persists even at zero loss on
  the anchors. Unsettled on condition 3: acceptance is by outcome and
  constraint checks, and the evidence cited does not show whether a proposed
  edit states what was wrong with the component it changes.
- [Dynamic Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md)
  curates notes from solver traces into later prompts; the curator prompt is
  the only gate. Unsettled on condition 3: the curator rewrites notes, but
  whether it criticizes what a note says is not shown.
- [Voyager](../agent-memory-systems/reviews/voyager.md) admits executable
  skills on a critic's success report. Retained skills supply both prompt
  context and executable code for later tasks. Unsettled on condition 3: the
  critic reports task success, and criticism of a skill after admission is
  not shown.
- [HyperAgents](../agent-memory-systems/reviews/hyperagents.md) evaluates
  generated patches and replays selected parent lineages into later
  generations. The replayed code changes future execution; the reviewed
  patches do not carry an explanation of why they worked. Unsettled on
  condition 3, closest to selection by outcome score.

**Machinery for self-modification and recovery.** These systems make changes
persistent and recoverable, with different limits on what starts or selects
an improvement.

- [Autogenesis](../agentic-systems/reviews/autogenesis.md) can write to many
  forms, but its selection is weaker than its versioning, and public
  implementations are incomplete. Unsettled on condition 3.
- [Exo](../agentic-systems/reviews/exo.md) supports self-inspection,
  revision, restart, rollback, and preserved failure evidence, with no
  automatic trigger from experience to improvement. Exo is machinery that a
  builder could use; whether a system built on it criticizes its theories
  and builds on the result is unsettled.
- Prime Agent retains versioned prompts, memories, skills, and subagent
  specifications without weight updates; one case found a specification
  exploit and "preserved it as a reusable skill"
  ([Prime Agent](../sources/prime-agent-a-self-improving-rlm-harness.ingest.md),
  verbatim). Persistence does not ensure sound admission. Unsettled on
  condition 3: the preserved exploit shows a harmful skill admitted, and the
  evidence cited does not show how admission judges what a skill says.

**A supplied model guides adaptation.**
[Rainbow](../sources/rainbow-architecture-based-self-adaptation.ingest.md)
selects adaptation strategies from a causal model of a running system whose
vocabulary, goals, and strategies are fixed and supplied. It is a mechanism
comparison for retained causal models, not a case of learning one. It is
outside: its model is a fixed theory that the system never criticizes, so it
fails condition 3.

## The next comparisons

For most unsettled systems, the deciding evidence is whether a stated reason
bears on what a retained unit says. Recording the proposer's diagnosis next to
each accepted change, and checking whether it names what the changed unit
said, would settle condition 3. For the Gödel machines, running a retained
archive on a problem it did not evolve on would measure how far their results
persist.

For the knowledge and skill pipelines, vary the formulated criticism while
keeping the underlying observations and evaluation conditions comparable.
Then withhold or perturb a retained theory to test how its content affects
later decisions. This connects two questions that a pipeline-level ablation
leaves together: what produced the useful revision, and how the revision
contributed to later improvement.

For the human-assisted systems, record which internal roles people perform
and test computational replacements under matched demands. For the
self-modification systems, follow one proposed improvement from its diagnosis
through selection to later use and measured benefit. These comparisons serve
the same program at different stages of automation.

Finally, compare retaining an assembled theory with reconstructing it from
the same episode evidence, counting both cost and decision quality. This
tests the program's persistence conjecture; either arrangement may learn. The
[testing supplement](./testing-whether-a-theory-builder-learns.md) develops
these comparisons into controlled task-family experiments.
