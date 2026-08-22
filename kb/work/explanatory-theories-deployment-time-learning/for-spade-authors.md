# Invitation: generate procedures for theory-derived questions with SPADE

> **Status:** Exploratory note from the Commonplace project. We have not contacted the SPADE authors, and no response or endorsement is implied. The proposed use is ours; SPADE does not claim or test it.

SPADE's Environment Designer produces concrete, executable outputs: Python environments that must pass structural and runtime checks before SPADE estimates their learning value. Corpus material broadens generation, while environment memory allows later designs to respond to earlier difficulty and regret outcomes. The same model learns through shared-weight updates. Our [source analysis](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) grounds these mechanisms; we have not reproduced the reported training gains.

We propose using the generator for a different purpose: producing an evaluation procedure for a question derived from an explicit theory of a system change.

## The proposed change in purpose

SPADE's hint/no-hint return gap asks whether privileged information improves the current policy's return in a generated environment. The proposed acceptance procedure asks a different question: does a fixed incumbent/candidate pair differ on a specified behavioral obligation?

The obligation could be derived from a working theory's prediction about the candidate. For example, the theory might predict that a routing change preserves tool selection outside one task family. The designer would receive that obligation, the relevant scope and premises, and the incumbent/candidate interfaces, then generate a procedure capable of exposing a violation. Alternatively, two rival theories could supply incompatible predictions, and the designer could seek a procedure whose outcome discriminates between them.

This proposal does not reclassify SPADE's current artifacts. Its environment code represents task dynamics, environment memory records curriculum examples and outcomes, and the task-local hint states a solution insight. Those functions do not make any artifact a system theory. SPADE also generates the hint after its environment rather than using the hint to derive the environment's question.

A generated procedure requires evidence beyond successful execution. Independent checks must establish three properties:

- **execution validity:** the procedure runs, terminates, and remains contained;
- **observation validity:** its result bears on the named obligation rather than an incidental difference; and
- **decision value:** the evidence justifies the cost of generation, validation, and execution.

SPADE's validators contribute to the first property and to parts of feasibility. By themselves, they neither establish containment nor make the resulting behavior difference relevant to candidate acceptance.

## One discriminating experiment

First, hold the model, incumbent/candidate pairs, procedure budget, validation pipeline, and hidden audit set fixed. Disable adaptive environment memory. Then compare the same designer under three inputs:

1. the task and candidate change, with no explicit theory-derived question;
2. the same context plus one prerecorded theory-derived obligation; and
3. the same context plus rival theories and their predicted disagreement.

Before generation, researchers should seed some candidate pairs with hidden effects whose detection requires probing the named obligation. The set should include cases that separate the rival predictions. Researchers must hide the effects and final acceptance labels from the designer. An independent authority should certify whether each executable procedure measures its claimed obligation.

Measure valid detections per total cost, harmful misses, invalid or incidental discriminators, and coverage outside the generator's expected surface. The second and third arms qualify only if they outperform the generic arm without weakening observation validity. If the theory-conditioned arms qualify, a later experiment can add SPADE-style memory and test whether prior successes and failures improve procedure search beyond nonadaptive synthesis. This sequence separates theory conditioning from adaptive memory.

The workshop's [selective-evaluation model](./selective-evaluation-model.md) defines obligations and bounded acceptance; the [experiment design](./experiment-design.md) explains why procedure generation comes only after the selector itself qualifies.

## Questions for the SPADE authors

- Could the Environment Designer target a supplied behavioral obligation without collapsing onto superficial incumbent/candidate differences?
- What reward could favor valid discrimination while resisting reward hacking and candidate–evaluator co-adaptation?
- Which current environment checks would transfer, and what independent authority could certify observation validity?
- Could the designer search specifically for an outcome on which rival theories disagree? What representation would make that conditioning usable?
- What should environment memory retain—successful procedures, misses, invalid discriminators, or all three—without narrowing generation to old blind spots?
- What result would convince you that theory-derived conditioning adds no value over ordinary environment generation?

We welcome corrections to this reading of SPADE and criticism of the proposed change in purpose.
