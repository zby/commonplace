# An invitation to the SPADE authors

SPADE generates executable training environments. This invitation asks whether its separation of environment proposal, validation, and learning value could help generate acceptance tests for harness changes, and what extra evidence would make those tests decision-grade.

> **Status:** This is an exploratory response from the Commonplace project. It describes a possible extension inspired by SPADE, not a claim made or tested in the SPADE paper. We have not contacted the authors, and no response or endorsement is implied.

## Why SPADE matters to this workshop

Our [source analysis of SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md), a paper and implementation for self-play in adaptive synthetic executable environments, reads the system as a concrete separation of three jobs:

1. Corpus material and memory broaden and steer environment generation.
2. Structural, runtime, and semantic checks reject invalid environments.
3. Difficulty and the paired hint/no-hint return gap estimate whether a valid environment offers learning value to the current policy.

The released implementation supports this mechanism. The reported training and benchmark gains remain paper-only and unreproduced in this knowledge base. SPADE also updates shared model weights, while this workshop concerns changes to a separately versioned deployed harness. The bridge below therefore borrows SPADE's candidate-generation pattern, not its empirical results or its learning setting.

## The proposed bridge

[Harness Continual Learning (HCL)](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) treats a deployed harness around frozen model weights as revisable state. A candidate harness change is committed only after evidence of current-task improvement, sampled historical retention, and validity. Our workshop calls this deployment-time learning: deployment evidence changes retained harness state without updating the base model's weights. Repeatedly running a growing historical evaluation surface can become costly.

The proposed addition is a revisable **impact theory**. Given the current system and a candidate change, it predicts which behavioral functions or obligations may materially change. An evidence-acquisition policy then decides which evidence is worth buying. It would derive evaluation obligations from the predicted effects, select or generate procedures capable of observing them, validate those procedures, compare incumbent and candidate behavior, and feed the result into the commit decision.

SPADE suggests expanding that policy from selecting stored benchmarks or historical anchors to synthesizing an executable procedure for the particular change. That changes the generator's purpose. SPADE's matched contrast asks whether a privileged hint changes the current policy's return. The proposed acceptance contrast asks whether the incumbent and candidate differ on a specified obligation under the same procedure.

In this setting, SPADE's environment designer becomes a precedent for an **obligation-directed test synthesizer**, not the same role transplanted unchanged. The synthesizer would seek procedures likely to expose a relevant incumbent/candidate difference on the predicted impact surface. Whether memory of earlier regressions, misses, and unsuitable procedures improves that search without narrowing it is a hypothesis for the experiment.

## Why acceptance needs stronger gates than curriculum generation

The bottleneck is independent observation validity, not executable generation. A generated procedure can run correctly and expose a real difference while measuring an incidental artifact rather than the intended obligation. A large difference is not automatically a regression. An authority independent of the procedure generator must establish what the obligation means and which outcomes count against it. Possible authorities include mechanically checked invariants, a human-authored obligation registry, or held-out seeded effects.

At least four questions therefore remain separate:

- **Execution validity:** Does the procedure parse, run, terminate, and stay within an independently enforced containment boundary?
- **Observation validity:** Does an independent check establish that success or failure measures the intended obligation rather than an incidental behavior or exploitable artifact?
- **Decision value:** Is the expected information worth generation, validation, sandboxing, and execution cost for this candidate?
- **Selection validity:** Does the generator expose harmful effects rather than co-adapt with the candidate, teach to the gate, or search only where its own impact theory already expects success?

SPADE is useful here because it keeps proposal breadth, validity, and value distinct. It does not answer these acceptance questions. Its use of generated Python with functional checks is also not, by itself, an execution-containment argument.

## A minimal joint experiment

A first experiment could use a fixed collection of recorded harness candidates and known behavioral obligations. For each incumbent–candidate pair, compare four arms:

1. The full registered evaluation set.
2. Impact-guided selection from that set.
3. Obligation-directed procedure synthesis without adaptive memory.
4. SPADE-inspired adaptive generation conditioned on earlier procedure outcomes.

The synthesizer would receive the candidate change, predicted affected functions, and the obligation to observe, but not the final acceptance label. A held-out audit surface would test whether each arm detects seeded effects and misses effects outside its predicted surface. Designing that audit so it does not reproduce the impact theory's blind spots remains part of the problem.

The analysis should separate failures of impact prediction, procedure synthesis, observation-validity certification, containment, and cost amortization. Primary measurements would include harmful misses, detection coverage, calibration, total evidence cost, procedure reuse, and held-out retention. Agent return alone would not establish useful acceptance evidence. Adaptive generation should outperform the non-adaptive synthesis baseline before its memory or curriculum machinery receives credit.

The experiment does not yet specify the synthesizer's objective, choose an independent observation-validity authority, or define what approval means when possible effects were not tested.

## Questions for the SPADE authors

Your view would be especially useful on these questions:

- Could SPADE's paired-play machinery be adapted from hint/no-hint learning value to incumbent/candidate discrimination without rewarding arbitrary behavioral difference?
- What designer objective could target an explicit behavioral obligation while resisting reward hacking and candidate–evaluator co-adaptation?
- Which parts of SPADE's environment validation could transfer to generated evaluations, and what additional checks would be required before treating an environment as acceptance evidence?
- Could environment memory retain discovered regressions, false negatives, and redundant procedures without collapsing generation onto a narrow historical surface?
- When would adaptive generation amortize its construction and validation cost better than selecting from a fixed procedure registry?
- What experiment would most strongly falsify the claim that adaptive executable-procedure generation improves this selective-evaluation loop?

The [full causal-impact and selective-evaluation workshop](./README.md) develops the impact model, its relation to deployment-time learning and HCL, the changed acceptance semantics, and the audit problem created by selectively unobserved effects. We would welcome criticism of the bridge above, especially where this evaluation use misreads what SPADE's mechanisms can support.
