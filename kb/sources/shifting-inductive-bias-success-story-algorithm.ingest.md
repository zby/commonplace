---
description: "SSA retains reversible policy changes by lifetime reward-rate comparisons; maze and program-learning cases bound its value as evidence for reject-capable retention."
type: kb/sources/types/ingest-report.md
source: https://link.springer.com/content/pdf/10.1023/A:1007383707642.pdf
captured: "2026-09-20"
ingested: "2026-09-21"
capture: pdftotext
capture_scope: full-source
doi: "10.1023/A:1007383707642"
genre: scientific-paper
snapshot_sha256: 77afd17c663e6069b79136bbb4c7853d1b054361dc5d7c2e35c843d65ed7cae2
domains: [metalearning, reinforcement-learning, self-improvement]
learning_claims: true
---

# Ingest: Shifting Inductive Bias with Success-Story Algorithm

## Classification

Scientific paper by Jürgen Schmidhuber, Jieyu Zhao, and Marco Wiering, published in *Machine Learning* 28 (1997), pp. 105–130. It supplies an algorithm, a retrospective invariant, and experimental case studies. The authors developed the methods being evaluated; the paper is primary evidence for their mechanisms and reported results, not independent replication.

## Summary

The success-story algorithm (SSA) evaluates policy changes by reward per elapsed time since saved points in a learner's single lifetime, including time spent learning and testing. It restores saved policy components until the surviving history satisfies a reward-acceleration criterion; earlier changes can survive because later learning benefited, but none is permanently protected. The paper instantiates this wrapper with adaptive Levin search (ALS), which adjusts probabilities of program instructions, and incremental self-improvement (IS), whose generated instructions can modify their own generating policy. In a designed maze-task sequence, SSA improves ALS search costs and learning-rate robustness within a fixed program language, probability representation, and reward scheme. A separate arithmetic curriculum demonstrates IS learning increasingly complex functions within supplied arithmetic and self-modification operations. These results support reversible, long-horizon evaluation of learning changes, without establishing their causal contribution individually, optimality, or transfer to unrestricted knowledge-base work.

## Quotes

No source quotes have been retained yet.

## Connections Found

SSA is a concrete technical basis for [the proposal-selection loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): a learning action generates and actualizes a change, SSA can separately reject it by restoring saved components, and surviving policy probabilities govern future execution. It particularly clarifies evaluation *after* a change becomes operative. The maze comparison supports adding this rejection mechanism to ALS under the supplied program representation and task sequence; it does not test the general adequacy of that representation.

The paper also supports [objective-relative self-improvement](../notes/self-improvement-is-relative-to-a-declared-objective.md). Reward rate is specified before modifications occur, and elapsed learning time counts against it. The enforced property concerns surviving historical intervals measured at an evaluation time. It should not be read as an ordering of all possible policies or a guarantee of future improvement.

## Learning Claims (our opinion)

ALS raises the probability of instructions in successful programs, thereby changing which later programs search reaches cheaply. SSA wraps these updates in reversible retention: it stores old components with time and cumulative-reward records and rolls changes back when subsequent reward rates fail its comparison. IS broadens what the policy generates to include instructions that change policy probabilities themselves. Thus a retained change can alter both subsequent task behavior and subsequent modification behavior. Evaluation timing can also depend on generated instructions in the general IS construction; the function-learning experiment instead fixes evaluation after five nonzero rewards following a self-modification sequence.

In Commonplace terms, the policy is an operative retained result, and SSA supplies reject-capable evaluation. The evidence supports adaptation of search bias and, in IS, an implemented path for adapting the modification process. It does not by itself establish [conjectural learning](../notes/definitions/conjectural-learning.md). Individually editable policy probabilities provide repair locations, but the reported learning signal scores behavior rather than contradicting consequences derived from an explicit domain theory and using that contradiction to repair the theory. The success history is a retention record, not demonstrated explanatory knowledge about why each change worked.

The fixed layer matters as described in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Maze agents compose a restricted language of movement and jump instructions; program execution state supplies memory despite ambiguous current observations. This makes a purely observation-based impossibility claim inappropriate, but neither the primitives nor their probability-matrix representation are learned. The arithmetic experiment fixes work and program storage, arithmetic operations, the reward test, and an externally arranged progression through related functions. Self-modification changes probabilities inside this setup, not the meaning of its primitives or its reward objective. Reported improvement therefore establishes useful learning within those choices, not evidence that the choices are preferable to alternative decompositions.

The substantive addition to our account is temporal: an early change may earn continued retention through later changes it enabled, while remaining retractable. However, a single accumulated trajectory cannot identify that enabling contribution causally. The invariant and the useful experimental outcomes warrant different strengths of claim.

## Extractable Value

- **Reject-capable evaluation after actualization** `[quick-win]`: SSA gives the proposal-selection note a precise example where rejection restores saved state rather than merely generating a successor. Retention remains provisional throughout the learner's life.
- **Evaluate learning costs and downstream effects together** `[deep-dive]`: reward-rate accounting includes later learning and its cost, allowing an earlier change to be assessed beyond its immediate task. A KB analogue would need an independently defensible outcome measure and horizon; the paper does not supply them.
- **Rollback can counter harmful transfer within a fixed search space** `[just-a-reference]`: the maze comparison reports better search costs and robustness for SSA+ALS than ALS within the same supplied instruction and probability framework. Its explanation of over-biasing toward an earlier solution is useful evidence for reversible retention, not a demonstrated general policy for KB edits.

## Limitations (our opinion)

SSA enforces a retrospective inequality on the history left after rollback. An empty history can satisfy the requirement. Survival does not prove a modification caused the subsequent acceleration, distinguish improvement from favorable environmental change, or guarantee maximal reward or monotonic gains in future intervals. The paper explicitly denies general improvement-speed and optimality guarantees and requires environments in which useful regularities and reward accelerations are available. [Reinforcement Learning with Self-Modifying Policies](./reinforcement-learning-self-modifying-policies.ingest.md) uses the same SSA machinery with overlapping authors, so the two papers are not independent confirmations of one result: this one concerns assessing continued retention, that one learning the modification procedure.

The strongest direct comparison for the wrapper is ALS with versus without SSA on a constructed maze sequence. Learning rates were searched over, and the reported best settings differ; added noise also differs between successful configurations. This supports performance of the tested configurations and a separate robustness claim, rather than isolating every detail of the treatment. The earlier comparison against Q-learning also changes available memory, instructions, or observability between variants. It cannot attribute the whole performance difference to search alone, and it is not an SSA ablation.

The function-learning result uses a curriculum of strongly related arithmetic tasks with performance-dependent progression. Its large claimed advantage uses an estimated infeasible random-search baseline, not a completed matched run. The evolving self-modification frequency is suggestive, but the paper itself notes the difficulty of determining how much the system learned to use self-modification. It does not isolate that mechanism from curriculum benefits and ordinary policy learning.

No implementation was inspected or executed for this ingest. The PDF text extraction disrupts equation and table layout, so this report does not rely on precise table-cell comparisons or transcribe the extracted inequalities. Open-domain KB work adds semantic evaluation, changing tasks, and edits whose external effects cannot necessarily be undone by restoring a policy component; none is tested here.

## Recommended Next Action

Add SSA as an example of evaluation after actualization to [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), explicitly separating rollback's historical acceptance criterion from causal proof of improvement.

---

Relevant Notes:

- [Original paper](https://link.springer.com/content/pdf/10.1023/A:1007383707642.pdf) — derived-from: primary algorithm and experimental account
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — is-evidence-for: separately rejectable modifications followed by operative retention
- [Self-improvement is relative to a declared objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) — is-evidence-for: antecedent lifetime reward-rate objective with a bounded retrospective guarantee
