---
description: "Survey of eighteen systems: reported gains from retained knowledge and revised skills, evidence of formulated criticism, human-assisted bootstraps, and the experiments needed to establish autonomous conjectural learning"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/conjectural-learning.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/notes/definitions/system-definition-artifact.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
---

# How existing self-improving systems relate to conjectural learning

> **Draft.** The claims, system selection, and comparisons may change.
> Comments, corrections, and additional candidates are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Existing self-improving systems already report gains from retained knowledge
and revised skills. They also supply mechanisms for diagnosis, criticism,
revision, and reuse. The question for
[our conjectural-learning program](./conjectural-learning-with-fixed-models.md)
is how these mechanisms contribute to the gains: does criticism of a
formulated theory improve later decisions, and can the whole process run
without people performing its internal roles?

This survey compares eighteen systems through retained code reviews, papers,
and practitioner reports. No reported outcome was reproduced here. The
comparisons identify what each precedent contributes and which experiments
would resolve the remaining questions.

## Two precedents already test improvement

**Knowledge-Centric Self-Improvement** keeps the solver machinery fixed while
agents contribute experience to a shared knowledge base: "The only object that
changes is the curated knowledge base."
([Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
verbatim). Agents formulate claims in task forums, support or challenge them
with evidence, discuss which observations generalize across tasks, and distill
the results for later agents. Its protocol therefore includes criticism of
claims as well as benchmark evaluation.

The paper freezes a learned knowledge bundle and transfers it to unseen tasks,
using a task-conditioned adapter to prepare a memo for each recipient. It
reports improved zero-shot performance on Polyglot and ARC-AGI-1. This tests
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
call for narrower comparisons within the successful pipelines.

## What the comparison asks

[Conjectural learning](../notes/definitions/conjectural-learning.md) requires
a formulated theory to be
[operative](../notes/definitions/operative-change.md): a difference in what it
says changes a decision. Criticism of what the theory says must improve the
system's capacity for future action. The effect can persist in a retained
theory or in criticisms from which the theory is reconstructed.

We therefore distinguish how a revision is produced from how it is accepted.
A system may diagnose a mistaken assumption, revise the theory, and use an
outcome gate to accept the revision. Testing a stated consequence can itself
be criticism. The gate alone tells us little about whether the preceding
process criticized a theory or simply generated another variant. Conversely,
[observing the whole theory-to-use path does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md);
that needs an outcome comparison.

The program adds distinct questions to this learning test. Can all internal
roles run computationally with fixed model weights? Does the learned revision
transfer to new cases? Does retaining the assembled theory save work compared
with reconstructing it from the same evidence? A human-assisted system may
provide evidence of learning before it provides evidence of autonomy, as the
[bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
proposes for Commonplace.

## Where the reviewed systems stand

**Human-assisted learning and machinery development.** These systems show
how people and agents retain knowledge and change their working machinery.
They are precedents for a bootstrap whose learning system includes the
operator. Their reports also identify internal roles that remain human.

- [Fluent](../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md)
  retains product code, expertise, scheduling, rejection, and reuse; people
  and the system jointly settle the brief, the behaviour specification, and
  the approach. Practitioner-reported.
- Wheelhouse, in Steve Yegge's report, moves human rulings from custom to
  warnings, written doctrine, and programs that refuse actions. The corpus
  retained "old rulings that were obsolete or had changed"
  ([Wheelhouse](../sources/steve-yegge-fences-not-sandboxes.ingest.md),
  verbatim), which is the maintenance cost of retention made visible.
- OpenAI's agent-first product keeps repository documents that explain the
  business domain and repairs them recurrently. People generalize: when
  agents struggle, engineers ask "what capability is missing? What
  constraint is unenforced?" and build the tool, linter, or test
  ([agent-first product](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md),
  verbatim).
- [Warp's scheduled skill improver](../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md)
  admits skill updates through human feedback and review.
- Commonplace retains explanatory notes with scope and evidence and revises
  them under review; its
  [system-definition artifacts](../notes/definitions/system-definition-artifact.md)
  describe the machinery. One
  [recorded episode](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
  shows retained theory guiding computational search with the operator
  selecting what fit, without ablation. Models are not reliably pinned.

**Automated revision, selection, and reuse.** These systems automate parts of
the path from experience to later behavior. The entries distinguish the
retained change from the mechanism that selects or consumes it. Establishing
conjectural learning additionally requires tracing a formulated theory and
its criticism through that path.

- The Darwin Gödel Machine evolves coding agents around frozen models; a
  fixed diagnostician suggests improvements from the parent's logs, and
  admission is viability: "Only agents that compile successfully and retain
  the ability to edit a given codebase are added to the DGM archive"
  ([Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md),
  verbatim). Diagnostic rationale is not shown to persist across
  generations.
- The [Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
  replaces score with descendant productivity for parent selection, and
  reports that immediate score predicts it poorly.
- Recuris proposes memory patches from traces and decides each through a
  deterministic paired held-out gate, with the memory coordinates supplied
  in advance: "The memory only grows, and it can afford to."
  ([Recuris](../sources/recursive-experiential-working-memory-evolution.ingest.md),
  verbatim)
- [Harness Continual Learning](../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md)
  retains edits that improve the current task, respect sampled anchors, and
  pass validity checks; held-out forgetting persists even at zero loss on
  the anchors.
- [Dynamic Cheatsheet](../agent-memory-systems/reviews/dynamic-cheatsheet.md)
  curates notes from solver traces into later prompts; the curator prompt is
  the only gate.
- [Voyager](../agent-memory-systems/reviews/voyager.md) admits executable
  skills on a critic's success report. Retained skills supply both prompt
  context and executable code for later tasks.
- [HyperAgents](../agent-memory-systems/reviews/hyperagents.md) evaluates
  generated patches and replays selected parent lineages into later
  generations. The replayed code changes future execution; the reviewed
  patches do not carry an explanation of why they worked.

**Machinery for self-modification and recovery.** These systems make changes
persistent and recoverable, with different limits on what starts or selects
an improvement.

- [Autogenesis](../agentic-systems/reviews/autogenesis.md) can write to many
  forms, but its selection is weaker than its versioning, and public
  implementations are incomplete.
- [Exo](../agentic-systems/reviews/exo.md) supports self-inspection,
  revision, restart, rollback, and preserved failure evidence, with no
  automatic trigger from experience to improvement.
- Prime Agent retains versioned prompts, memories, skills, and subagent
  specifications without weight updates; one case found a specification
  exploit and "preserved it as a reusable skill"
  ([Prime Agent](../sources/prime-agent-a-self-improving-rlm-harness.ingest.md),
  verbatim). Persistence does not ensure sound admission.

**A supplied model guides adaptation.**
[Rainbow](../sources/rainbow-architecture-based-self-adaptation.ingest.md)
selects adaptation strategies from a causal model of a running system whose
vocabulary, goals, and strategies are fixed and supplied. It is a mechanism
comparison for retained causal models, not a case of learning one.

## The next comparisons

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
tests the program's retention advantage; either arrangement may learn. The
[testing supplement](./testing-the-conjectural-learning-program.md) develops
these comparisons into controlled task-family experiments.
