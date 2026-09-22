---
description: "Survey: eighteen existing self-improving agent systems sorted by how what they retain is admitted; the parts of a conjectural learner have precedents, but in the reviewed evidence none tests its mechanism"
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

> **Draft, work in progress.** This survey is being realigned with the
> series that starts with
> [Conjectural Learning with Today's LLMs](./conjectural-learning-with-fixed-models.md).
> Which systems belong here and how each is placed may change. Comments,
> corrections, and additional candidates are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Existing self-improving agent systems supply the parts of a conjectural
learner: retained notes and code, scheduled revision, gates that can reject a
change, and rollback with failure evidence. In the evidence reviewed here,
none of eighteen systems tests its mechanism. The mechanism has two halves: a
retained explanation guides a later decision on a case it did not state, and
criticism of what the explanation says improves later decisions. What the
reviewed systems retain is admitted by a score, an oracle, a held-out gate, or
a critic, which judge an outcome, or by people, who supply the rationale
themselves. None of them tests the first half, so none tests the second.

Some systems were inspected in code; others are known only from papers or
practitioner reports, and no reported outcome was reproduced here. The finding
is about the reviewed evidence, not about what these systems could do.

## What the comparison asks

[Conjectural learning](../notes/definitions/conjectural-learning.md) needs
four things of a system. A formulated theory is
[operative](../notes/definitions/operative-change.md): a difference in what it
says changes a decision. Criticism addresses what the theory says, not only
whether an outcome passed. The result is retained and stays revisable. And,
for the automation bet, the loop continues with fixed model weights and no
person in an internal role.

The second condition is where most systems fall away. A gate that rejects a
change by its score has judged an outcome; it has not criticized an
explanation. Writing a note, a skill, or a patch after a failure does not by
itself show that the note did anything later, and
[a complete path from theory to use does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md).

## Where the reviewed systems stand

**People supply the rationale and settle revisions.** These are working
products, and their reports are the best evidence that retained knowledge
changes later work. They do not test automation, because the diagnosis is
human.

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

**A score, an oracle, a held-out gate, or a critic admits what is
retained.** These loops run without people inside and with weights mostly
fixed, so they are the nearest to the automation bet. What they retain is
selected by outcome, and no reviewed run isolates whether a retained item
guided a later decision.

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
- Memento-Skills learns skills mixing instructions and code under answer
  oracles, and also trains a router, so not all weights stay fixed. Its
  ablation leaves "no failure attribution, no skill rewriting, and no skill
  discovery"
  ([Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md),
  verbatim).
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
  skills on a critic's success report and overwrites a same-named program
  rather than revising it.
- Knowledge-Centric Self-Improvement holds software and solver fixed under a
  benchmark oracle: "The only object that changes is the curated knowledge
  base."
  ([Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md),
  verbatim)

**Changes are versioned or replayed without a content gate or a trigger.**
These supply the persistence and rollback machinery and show what it does
not guarantee.

- [HyperAgents](../agent-memory-systems/reviews/hyperagents.md) replays
  patch lineages into the next generation; its retained memory is executable
  and carries no explanation.
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

## What would change the picture

One reviewed run in which withholding or perturbing a retained explanation
changes a later decision on a case the explanation did not state, and in
which criticism of that explanation's content, not its score, improves the
decisions after it. Stronger still, a matched comparison of the retained
explanation against retained records of the same observations, so that the
explanation's contribution beyond the records is measured. The
[testing supplement](./testing-the-conjectural-learning-program.md) states
these as the first experiments. None of the systems here reports one, and
that, not any verdict on the systems, is the survey's finding.
