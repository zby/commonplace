---
description: "Schmidhuber's reward-gated self-modification report as historical evidence for oracle-dependent behavior learning and reversible promotion"
source_snapshot: on-learning-how-to-learn-learning-strategies.md
ingested: "2026-04-29"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [learning-theory, self-improvement, oracle-theory, agent-memory]
---

# Ingest: On Learning How to Learn Learning Strategies

Source: on-learning-how-to-learn-learning-strategies.md
Captured: 2026-04-29
From: https://people.idsia.ch/~juergen/fki198-94.pdf

## Classification

Type: scientific-paper -- revised technical report with a formal learning paradigm, concrete implementation, toy experiments, citations, and explicit claims about reinforcement learning and meta-learning.
Domains: learning-theory, self-improvement, oracle-theory, agent-memory
Author: Jurgen Schmidhuber is a long-running machine-learning researcher in recurrent networks, self-referential learning, and self-improving systems; the source matters as historical lineage even though the implementation is not repo-inspectable here.

## Summary

Schmidhuber introduces "incremental self-improvement": a lifelong reinforcement-learning system whose action language includes ordinary environment actions and self-delimiting self-modification programs. Those programs can modify the probability distribution over future action sequences, including future self-modifications, so the system can shift its own inductive bias without a hard learning/meta-learning boundary. A fixed top-level credit-assignment strategy keeps only probability changes whose observed payoff-per-time exceeds the system or the previous useful self-modification, restoring older probability distributions from a stack when they stop qualifying. The report's durable contribution is not the toy-task performance itself but the architecture of reward-gated, reversible, whole-life behavior learning.

## Connections Found

`/connect` found that the strongest existing connection is the local source-only Incremental Self-Improvement coverage note, which already covers this exact report as related-system lineage but is not part of this commit. The source also supports [oracle strength spectrum](../notes/oracle-strength-spectrum.md), [automating KB learning is an open problem](../notes/automating-kb-learning-is-an-open-problem.md), and [memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md): Schmidhuber's system can automate promotion because payoff per time supplies a promotion oracle. It is evidence for [continual learning's open problem is behaviour, not knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md), because the learned state changes future behavior rather than accumulating retrievable facts. It also compares with [Huxley-Godel Machine](./huxley-godel-machine-human-level-coding-agent-development.ingest.md), which moves the same self-improvement lineage into benchmark-guided search over inspectable coding-agent scaffolds.

## Extractable Value

1. **Learning time belongs inside the objective** -- The highest-reach idea is that learning, evaluation, and rollback overhead are not free side channels; they must be charged to the same payoff/time budget as acting. This transfers directly to KB and harness loops where review, distillation, and search can look valuable while quietly consuming more capacity than they return. [quick-win]

2. **Automated promotion needs an oracle strong enough to carry retention decisions** -- The paper shows a clean automated gate because reward per time is numeric and immediate enough to compare self-modifications. That strengthens the KB's current diagnosis: our hard part is not generating candidate notes or links, but deciding whether they improve future reasoning without an equivalent payoff signal. [quick-win]

3. **Reversible promotion is a design primitive, not cleanup after failure** -- The stack of prior probability distributions lets the system keep a candidate modification while it appears useful and later restore old state if the evidence turns. This is a strong analogy for KB promotion: durable changes should preserve enough provenance and previous state to retire, supersede, or relax them without pretending the system never learned them. [experiment]

4. **Self-modification as ordinary action collapses the artificial learning/meta-learning split** -- The action language can express environment interaction and modifications to the future action distribution. For agent systems, the transferable pattern is to put policy edits, tool edits, and ordinary work in one inspectable workflow where possible, instead of treating "learning" as a separate magical subsystem. The source's own substrate is opaque, so the KB should borrow the framing rather than the implementation. [experiment]

5. **Primitive choice is prior bias** -- The report is explicit that the programmer's chosen primitives and payoff function encode prior knowledge. For Commonplace, type specs, validation commands, skills, and link labels play the same role: they make some learning trajectories cheap and others unlikely. This is useful as lineage, but already mostly captured in the source-only note. [just-a-reference]

6. **"Life is one-way" usefully attacks resettable-trial assumptions** -- The source treats every action as a singular event and refuses to hide trial boundaries or reset costs. That is a useful caution for applying benchmark-loop conclusions to deployed KB agents: repeatable evals are powerful, but they are not the same environment as one-way cumulative knowledge work. [deep-dive]

## Limitations (our opinion)

The experiments are illustrative toy tasks, not broad empirical evidence that the paradigm scales. The report says this directly: the goal is to show the mode of operation, not to compare initial biases or prove practical superiority. The simpler account for the empirical gains is "stochastic search with reward-rate rollback found useful biases in small environments," not "universal self-improvement is practically solved."

The central retention rule also depends on a strong reward oracle. Payoff per time can collapse validity and learning value only where reward is meaningful, observed at the right timescale, and hard enough to resist accidental correlations. The report itself acknowledges that apparent usefulness may be a fluke under single-experience induction. For KB methodology, this limits transfer: source fidelity, link usefulness, synthesis value, and future reasoning payoff do not reduce to a cheap scalar.

Finally, the learned state is not inspectable knowledge. Probability distributions over future instruction sequences can change behavior, but they cannot be searched, cited, linked, reviewed, or decomposed like notes, instructions, tests, and code. That makes the source valuable as lineage for oracle-gated behavior learning, not as an argument against the KB's readable-artifact strategy.

## Recommended Next Action

Update the local source-only Incremental Self-Improvement coverage note: cite this local snapshot as the captured source and add one short paragraph connecting payoff-per-time retention to the KB's separate validity and learning-value gates. No new note is needed; the existing source-only coverage already owns the core synthesis.
