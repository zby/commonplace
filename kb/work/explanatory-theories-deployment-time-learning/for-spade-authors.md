# Invitation: generate procedures for theory-derived questions with SPADE

> **Status:** Exploratory note from the Commonplace project. We have not contacted the SPADE authors, and no response or endorsement is implied. The proposed use is ours; SPADE does not claim or test it.

SPADE gives an Environment Designer a concrete executable output: Python environments that must pass structural and runtime checks before their learning value is estimated. Corpus material broadens generation, while environment memory lets later designs respond to earlier difficulty and regret outcomes. The same model learns through shared-weight updates. Our [source analysis](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) grounds those mechanisms; its reported training gains remain unreproduced here.

We are interested in a different use of the generator. Could it produce an evaluation procedure for a question derived from an explicit theory of a system change?

## The proposed change in purpose

SPADE's hint/no-hint return gap asks whether privileged information improves the current policy's return in a generated environment. An acceptance procedure would ask a different question: does a fixed incumbent/candidate pair differ on a specified behavioral obligation?

The obligation could be derived from a working theory's prediction about the candidate. For example, the theory might predict that a routing change preserves tool selection outside one task family. The designer would receive that obligation, the relevant scope and premises, and the incumbent/candidate interfaces, then generate a procedure capable of exposing a violation. Alternatively, two rival theories could supply incompatible predictions, and the designer could seek a procedure whose outcome discriminates between them.

This proposal does not reclassify SPADE's current artifacts. Its environment code represents task dynamics, environment memory records curriculum examples and outcomes, and the task-local hint states a solution insight. None is thereby a system theory. The hint is also generated after its environment rather than used to derive the environment's question.

A generated procedure would need stronger evidence than executability. Independent checks must establish:

- **execution validity:** the procedure runs, terminates, and remains contained;
- **observation validity:** its result bears on the named obligation rather than an incidental difference; and
- **decision value:** the evidence justifies the cost of generation, validation, and execution.

SPADE's validators contribute to the first question and parts of feasibility. They do not by themselves establish containment or make the resulting behavior difference relevant to candidate acceptance.

## One discriminating experiment

Hold the model, incumbent/candidate pairs, procedure budget, validation pipeline, and hidden audit set fixed. Disable adaptive environment memory at first. Compare the same designer under three inputs:

1. the task and candidate change, with no explicit theory-derived question;
2. the same context plus one pre-recorded theory-derived obligation; and
3. the same context plus rival theories and their predicted disagreement.

Before generation, seed some candidate pairs with hidden effects whose detection requires probing the named obligation, including cases that separate the rival predictions. Keep the effects and final acceptance labels hidden from the designer. An independent authority should certify whether each executable procedure measures its claimed obligation.

Measure valid detections per total cost, harmful misses, invalid or incidental discriminators, and coverage outside the generator's expected surface. The second and third arms qualify only if they outperform the generic arm without weakening observation validity. If they qualify, add SPADE-style memory as a later factor and test whether prior successes and failures improve procedure search beyond non-adaptive synthesis. This ordering keeps theory conditioning separate from adaptive memory.

The workshop's [selective-evaluation model](./selective-evaluation-model.md) defines obligations and bounded acceptance; the [experiment design](./experiment-design.md) explains why procedure generation comes only after the selector itself qualifies.

## Questions for the SPADE authors

- Could the Environment Designer target a supplied behavioral obligation without collapsing onto superficial incumbent/candidate differences?
- What reward could favor valid discrimination while resisting reward hacking and candidate–evaluator co-adaptation?
- Which current environment checks would transfer, and what independent authority could certify observation validity?
- Could the designer search specifically for an outcome on which rival theories disagree? What representation would make that conditioning usable?
- What should environment memory retain—successful procedures, misses, invalid discriminators, or all three—without narrowing generation to old blind spots?
- What result would convince you that theory-derived conditioning adds no value over ordinary environment generation?

We would welcome corrections to this reading of SPADE and criticism of the proposed change in purpose.
