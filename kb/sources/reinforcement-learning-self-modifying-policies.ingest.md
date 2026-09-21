---
type: kb/sources/types/ingest-report.md
description: "Self-modifying policies retain changes by lifelong reward rate; their checkpoint guarantee bounds claims about learned learning rules and compounding."
source: https://nic.schraudolph.org/pubs/SchZhaSch98.pdf
captured: "2026-09-20"
ingested: "2026-09-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 0a51cb77615dea3bf1b25881c34dd881e64e2379e44094c2d0013a16ff0e4532
domains: [reinforcement-learning, self-modification, metalearning]
learning_claims: true
---

# Ingest: Reinforcement Learning with Self-Modifying Policies

## Classification

Scientific paper by Jürgen Schmidhuber, Jieyu Zhao, and Nicol N. Schraudolph, affiliated with IDSIA. The captured author manuscript identifies a chapter in *Learning to Learn* and prints 1997. It supplies an algorithm, a concrete implementation, and a small simulation study. The authors describe their own construction; implementation and results were not independently reproduced for this ingest.

## Summary

The paper puts modifiable parts of the learning algorithm inside a stochastic policy, allowing policy changes to alter subsequent learning. Its success-story algorithm (SSA) retrospectively undoes changes until the surviving checkpoint history satisfies an increasing long-term reward-rate condition. The policy influences when evaluation happens, but the reward channel, SSA criterion, and available instructions remain supplied machinery. In a constructed two-agent, partially observable navigation task, the implementation reduces average trial length from 330,000 cycles without effective self-modification to 5,500 cycles after training, a roughly sixtyfold improvement averaged over four simulations. This tests adaptation within a fixed instruction and memory architecture; comparisons with tabular Q-learning also change the representation and control structure. The reusable contribution is a precise mechanism for retaining earlier changes through their later consequences, with a guarantee about the surviving empirical history rather than optimality or independently established causal compounding.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies a concrete empirical-retention counterpart to [the Gödel-machine account](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md). Here changes operate before SSA can reject them; a Gödel-machine switch requires a proof under the current formalization. The important distinction is both the ground for retention and the time at which a change becomes operative. Restoring the earlier policy does not restore elapsed time or environmental consequences.

It also sharpens the boundary in [compounding is tested in later improvement](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). Earlier modifications affect the generation of later ones and are assessed over the intervening lifetime. That is an explicit mechanism for crediting later consequences. A favorable reward trend on one lived trajectory, however, does not isolate the contribution of learned update rules to later improvement productivity. The reported navigation gain remains evidence for the tested SMP/SSA configuration within its supplied instruction and state representation.

## Learning Claims (our opinion)

An SMP is a self-modifying policy: the distributions that select instructions also select policy-changing instructions and their arguments. A stack records previous policy values and checkpoint reward totals. SSA compares average reward rates from surviving checkpoints to the present and pops modifications that fail its criterion. Evaluation timing is partly learned: the `PrepareEvaluation` instruction suspends further policy modifications until a selected number of positive rewards arrives. This gives a modification time to affect behavior before judgment, while retaining a fixed evaluation rule.

The substantive meta-learning mechanism is that an earlier distribution change can alter where, when, and how often subsequent distribution changes occur. The paper reports changes in self-modification frequency and concentration, alongside task improvement. These observations support adaptation of the implemented update process. They do not separately establish that learning the update process caused the task gain: the study lacks a matched condition retaining ordinary policy learning while freezing those meta-learning choices.

This maps only partially to [conjectural learning](../notes/definitions/conjectural-learning.md). The policy has editable components and a causal role in future learning, but the described procedure formulates no theory in language and directs no criticism at what one says. It changes action-generating probabilities and selects surviving histories by reward. It therefore supplies a route to learned learning behavior without demonstrating the KB's conjectural-learning process; calling every editable policy a theory would erase that distinction.

The effective update space is consequential. In the experiment, the instruction pointer provides internal state, task-specific perception and movement primitives provide the action basis, and probability updates alter their selection. The learner can compose these primitives, including its update and evaluation-timing instructions, but cannot replace the supplied primitives, reward definition, SSA rule, or memory architecture. As [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, success demonstrates useful adaptation within this space, not superiority of its fixed boundaries. The paper itself distinguishes this restricted implementation from more general programming-language possibilities.

## Extractable Value

- **[quick-win] Separate becoming operative from continued retention.** SSA lets a change act and later removes it when accumulated outcomes cease to justify it. This is a precise comparison case for the Gödel-machine note's distinction between proof-authorized switching and empirical retention. Its scope is reversible policy state; lived consequences remain.
- **[quick-win] State what a recursive credit rule guarantees.** SSA retains a history satisfying a reward-rate condition at evaluation points, possibly an empty history. It measures later outcomes after earlier changes, but this does not establish their counterfactual contribution to later learning or guarantee future improvement. This distinction improves how Commonplace reads claims of compounding.
- **[experiment] Treat evaluation timing as a learnable variable.** The source provides an implemented way to delay judgment while collecting rewards. A KB experiment could compare fixed evaluation windows with bounded adaptive windows for retained procedural changes. The paper motivates this comparison, but its fixed navigation architecture and bundled result do not establish that adaptive timing would improve KB review.

## Limitations (our opinion)

The empirical scope is one constructed environment and a few simulations. Disabling the probability-changing instruction compares the full adaptive configuration with random behavior; it does not isolate SSA, learned evaluation timing, or learned modification schedules. Q-learning uses different action and observation arrangements, and the SMP instruction pointer supplies memory. Its weak performance cannot establish a general advantage over learning systems with comparable memory and representations. Adding Q-learning as an SMP instruction reportedly improves late performance slightly, which supports composability in this setup rather than superiority of the overall decomposition.

SSA's retention evidence comes from a single irreversible history. Environmental changes, delayed consequences, and chance can affect measured reward rates; rollback cannot provide the counterfactual trajectory without a modification. The source acknowledges that no optimality or improvement-speed guarantee follows and that environments with persistently decreasing reward may leave only the trivial empty success history. Repeated re-evaluation is useful correction machinery, not proof that surviving changes caused progress.

Task-specific direction and perception instructions encode substantial prior structure. Neither the state-space size nor the reported improvement shows that the same architecture would handle arbitrary tasks or open-ended knowledge work. No released implementation was inspected or executed here. PDF extraction also flattens some mathematical notation and figure references, so exact formula transcription needs checking against the external manuscript.

## Recommended Next Action

Update [the Gödel-machine note](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) with this primary-source case distinguishing retrospective reward-based retention from proof required before a switch, including the fact that policy rollback does not undo lived consequences.

---

Relevant Notes:

- [Original author manuscript](https://nic.schraudolph.org/pubs/SchZhaSch98.pdf) — derived-from: algorithm, implementation, and reported navigation experiment
