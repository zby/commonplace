---
description: "Meta-AQUA links explicit reasoning traces to failure diagnosis, learning goals, and planned sequences of knowledge-repair algorithms."
source: https://www.cc.gatech.edu/faculty/ashwin/papers/er-99-01.pdf
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
doi: "10.1016/S0004-3702(99)00047-8"
genre: scientific-paper
snapshot_sha256: 0e00c0814525619dc23399288a05814289a957ad30ca03af0aadba6a52aa5d10
ingested: "2026-09-17"
occasion: "What the failure-to-strategy loop requires of the self-representation; what the learning-goal ablation showed and under what conditions; whether the strategy library is fixed or extensible."
learning_claims: true
type: ingest-report
domains: [learning-theory, reflection, multistrategy-learning, failure-diagnosis]
---

# Ingest: Introspective multistrategy learning

## Classification

This is a scientific paper that defines a computational account, describes its implementation in Meta-AQUA, works through two examples, and evaluates it in repeated story-understanding trials.
Author: Michael T. Cox and Ashwin Ram, AI researchers then affiliated with Wright State University and the Georgia Institute of Technology, report an implemented system and a six-run controlled comparison in *Artificial Intelligence*.

## Summary

Meta-AQUA records selected decisions in its story-understanding process as explicit reasoning traces, diagnoses a detected failure by matching a stored introspective explanation to the trace, derives learning goals that specify desired changes to background knowledge, and uses nonlinear planning to sequence registered learning algorithms whose preconditions and effects are represented as operators. In six generated story sequences, the goal guided condition accumulated more question-answering points than both a condition that mapped diagnosed faults directly to randomly ordered repair calls and a no-learning condition. The result supports deliberate coordination when learning methods interact in this implementation, while the experimental contrast does not isolate explicit learning goals from nonlinear sequencing. The system revises its background knowledge and can change a learning goal during execution, but the reported strategy space itself is a designer-supplied toolbox of algorithms, operator schemas, failure categories, and introspective explanation patterns; the paper shows selection and composition within that library, not autonomous extension of it.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is an implemented historical anchor for [reflective system](../notes/definitions/reflective-system.md): its self-representation is not a generic narrative about the system, but a causal trace of selected reasoning decisions that is consumed by diagnosis and subsequent knowledge repair. It is also technical evidence for [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), because its failure-to-strategy path depends on traces that retain inputs, goals, decision bases, execution effects, expectations, and actual outcomes. The learning-goal comparison is best read through [a retained-theory intervention isolates one explicit surface, not the whole program theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md): the intervention changes the goal guided planning stage while leaving blame assignment and the hand-built representational decomposition in place, and also changes ordered planning to random ordering. Relative to [theory builder](../notes/definitions/theory-builder.md), Meta-AQUA offers a neighboring reflective repair case: failures identify addressable background-knowledge locations and selected operators revise them, but the paper does not establish that every repaired object meets Commonplace's narrower theory criteria.

## Learning Claims (our opinion)

On the source's terms, learning is a planned response to performance failure. A trace and a failure symptom support blame assignment; the resulting explanation posts explicit learning goals; a planner composes calls to learning algorithms; execution alters background knowledge. The self-representation must therefore preserve distinctions that diagnosis and planning can consume: what the system expected and observed, which goals and context enabled a reasoning step, the basis for strategy selection, and the effects of execution. It also requires a supplied vocabulary that maps trace patterns to possible causes and learning goals. Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the background knowledge is symbolic and localized (condition 1) and guides story understanding (condition 2). Blame assignment matches a stated introspective explanation to the trace and names the background-knowledge location at fault, which is criticism aimed at what a unit says (condition 3). Repairs are retained and used on later stories, which are different problems (condition 4). Meta-AQUA is therefore a partial theory builder: explanation-based generalization and memory reindexing can use or reorganize knowledge without revising a stated theory, so not every repair meets condition 3. The trace is a causally connected self-representation, but the failure taxonomy, explanation library, and operators it reasons with are fixed and never criticized, so the [reflective qualifier](../notes/definitions/theory-builder.md#qualifiers) is not shown. The coordination gain below is a separate learning claim.

The evaluation supports a bounded coordination claim. Across six Tale-Spin story sequences, the learning-goal condition outscored random learning in every run; the reported average cumulative question-point scores were 93.67 for learning goals, 76.00 for random learning, and 46.67 for no learning. In run four, random learning attempted 26 learning episodes against 8 in the learning-goal condition while scoring lower, and on one story it performed worse than no learning. But the treatment jointly replaces explicit goal formation and nonlinear plan construction with direct fault-to-repair assignment and random ordering. It therefore shows that the complete goal guided planning treatment improved this system under interactions among its learning algorithms; it does not separately establish that explicit goals, rather than planned ordering or another coupled difference, caused the gain.

The effective update space is narrower than the paper's broad language about autonomous strategy construction. Available signals and histories include the designed trace fields, foreground and background knowledge, detected expectation/actual-outcome relations, and later story input. Available responses are compositions of algorithms already encoded in a toolbox as planning operators. The planner can express mappings from represented learning goals and context to partially ordered plans over those operators, and execution can alter background knowledge, indexes, and even replace a tentative learning goal when new information appears. Fixed outside that update space are the performance task, trace ontology, failure and goal taxonomies, introspective explanation library, planner, operator descriptions, scoring rule, and algorithm toolbox. The paper demonstrates dynamic selection, sequencing, and goal transformation inside this decomposition, but no mechanism that adds a new learning algorithm or operator representation to the strategy library.

## Extractable Value

1. **Specify the minimum self-representation for a failure-to-strategy loop.** A useful trace records expected and actual outcomes plus the goals, context, decision basis, and execution effects needed to move from a symptom to candidate causes and repairs; a raw failure score alone cannot support this path. [quick-win]
2. **Bound the learning-goal result to the treatment actually compared.** The six-run result favors goal guided nonlinear planning over direct fault-to-repair mapping with random ordering, not explicit goal representation in isolation. [quick-win]
3. **Distinguish dynamic composition from strategy-library extension.** Meta-AQUA changes goals and composes registered learning operators, while the operator toolbox and the representations that make planning possible remain designer supplied. [quick-win]
4. **Use negative algorithm interactions as a trigger for deliberate coordination.** The run-four reversal, where random learning was worse than no learning on one story, is a context-bound demonstration that executing individually plausible repairs in arbitrary order can damage performance. [just-a-reference]
5. **Treat the trace schema as part of the fixed learning decomposition.** Meta-AQUA improves within a space determined by hand-built trace fields, failure causes, IMXPs, learning-goal types, and operators; the experiment does not compare alternative decompositions or test omitted signals, repairs, or mappings. [deep-dive]

## Limitations (our opinion)

The experiment uses one implementation, one synthetic story-understanding domain, six generated sequences comprising 166 stories, and a researcher-defined partial-credit measure for posing, answering, and correctly answering questions. It reports aggregate scores and variability but no inferential test, and the same architecture and hand-built knowledge structures define both the treatment and the tasks on which it is judged. The learning-goal treatment is not factorial: goal formation and nonlinear ordering vary together against random ordering, so the source cannot assign the effect to either component alone. Blame assignment covers only part of the proposed failure taxonomy, verification of learned changes is explicitly unimplemented, and computational cost is discussed rather than measured. Following [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within the supplied trace, taxonomy, planner, and operator library does not validate those fixed choices or show that the learner could repair omissions outside them.

## Recommended Next Action

Update [reflective system](../notes/definitions/reflective-system.md) with a compact Meta-AQUA example that names the trace fields consumed by diagnosis and explicitly limits the reflective claim to the designer-supplied failure and repair decomposition.
