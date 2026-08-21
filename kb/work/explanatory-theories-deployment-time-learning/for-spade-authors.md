# An invitation to the SPADE authors

SPADE generates executable training environments. This invitation asks whether its separation of environment proposal, validation, and learning value could help generate acceptance tests for harness changes, and what extra evidence would make those tests decision-grade.

> **Status:** This is an exploratory response from the Commonplace project. It describes a possible extension inspired by SPADE, not a claim made or tested in the SPADE paper. We have not contacted the authors, and no response or endorsement is implied.

## Why SPADE matters to this workshop

Our [source analysis of SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md), a paper and implementation for self-play in adaptive synthetic executable environments, reads the system as a concrete separation of three jobs:

1. Corpus material broadens what environments are about; environment memory steers later generation using earlier environments annotated with difficulty and regret outcomes.
2. Structural and runtime checks—and, in the tool-use setting, a deterministic reset gate and an LLM feasibility screen—reject invalid environments.
3. Difficulty and the same-environment hint/no-hint return gap estimate whether a valid environment offers learning value to the current policy.

The released implementation supports this mechanism. The reported training and benchmark gains remain paper-only and unreproduced in this knowledge base. SPADE also updates shared model weights, while this workshop concerns changes to a separately versioned deployed harness. The bridge below therefore borrows SPADE's candidate-generation pattern, not its empirical results or its learning setting.

## The proposed bridge

[Harness Continual Learning (HCL)](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) develops a proposal–evaluation–commitment loop for persistent harness state in controlled task streams. A candidate is committed only after evidence of current-task improvement, sampled historical retention, and validity. Our target setting is different: evidence from real-world tasks would drive proposals and selection over retained system state without requiring an update to the base model's weights. We call that target **deployment-time learning** and borrow HCL's techniques for it; we do not treat HCL's experiments as a test of the transfer. Repeatedly running a growing historical evaluation surface can still become costly.

The proposed addition is an explicit working theory `tau_n` about relevant parts of the deployed system: causal mechanisms, dependency and authority paths, invariants, program structure, semantic contracts, learned action-conditioned predictions, or a mixture. It could diagnose a failure, guide search for candidate harness changes, prioritize those candidates, and derive evaluation obligations for them. A retained treatment would separately preserve and revise an addressable `T_n` across episodes.

SPADE does not supply this theory layer. Its current shared model generates executable environments on demand from corpus material and environment-memory context. The environment code embodies task dynamics, and a separately generated task-local hint states a solution insight, but neither is an explicit theory of the learner or harness; the hint is also produced after its environment rather than guiding that environment's generation. SPADE implements a proposal distribution whose later generations respond to learner outcomes through designer updates and regret-annotated environment memory; it does not show that an explicit theory with [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) mediates that search.

Our bridge asks whether an environment or test designer conditioned on `tau_n` could search for informative or corrective candidates, including procedures that discriminate rival theories or expose a predicted incumbent/candidate difference. That changes the generator's purpose. SPADE's hint/no-hint return contrast asks whether a privileged hint changes the current policy's return. The proposed acceptance contrast asks whether the incumbent and candidate differ on a specified obligation under the same procedure.

In this setting, SPADE's environment designer becomes a precedent for a **theory-conditioned, obligation-directed test synthesizer**, not the same role transplanted unchanged. The synthesizer would seek procedures likely to expose a relevant incumbent/candidate difference on an obligation named by the working theory's impact projection. A procedure could supply candidate-commitment evidence or act as a theory-discriminating audit where rival system theories predict different consequences; those roles should be recorded separately. Whether memory of earlier regressions, misses, unsuitable procedures, and theory revisions improves that search without narrowing it is a hypothesis for the experiment.

## Why acceptance needs stronger gates than curriculum generation

The bottleneck is independent observation validity, not executable generation. A generated procedure can run correctly and expose a real difference while measuring an incidental artifact rather than the intended obligation. A large difference is not automatically a regression. An authority independent of the procedure generator must establish what the obligation means and which outcomes count against it. Possible authorities include mechanically checked invariants, a human-authored obligation registry, or held-out seeded effects.

At least four questions therefore remain separate:

- **Execution validity:** Does the procedure parse, run, terminate, and stay within an independently enforced containment boundary?
- **Observation validity:** Does an independent check establish that success or failure measures the intended obligation rather than an incidental behavior or exploitable artifact?
- **Decision value:** Is the expected information worth generation, validation, sandboxing, and execution cost for this candidate?
- **Evidence-selection validity:** Does the generator expose harmful effects rather than co-adapt with the candidate, teach to the gate, or search only where the theory and impact projection that scoped its search already expect success?

SPADE is useful here because it keeps proposal breadth, validity, and value distinct. It does not answer these acceptance questions or provide evidence that a system theory has explanatory-reach. Its use of generated Python with functional checks is also not, by itself, an execution-containment argument.

## A minimal joint experiment

A first experiment should isolate the theory layer before testing adaptive procedure generation. With a fixed full evaluator, compare direct harness-candidate search, search after an on-the-spot working theory, and search after instantiating a working theory from a retained theory. With fixed harness candidates, compare evidence selection with and without theory-derived impact projections. Only theory and selector conditions that qualify on independent audits should enter the SPADE-inspired phase.

A second phase would cross qualifying selectors with three procedure-source conditions:

1. Selection from the fixed registered set.
2. Obligation-directed procedure synthesis without adaptive memory.
3. SPADE-inspired adaptive generation conditioned on earlier procedure outcomes.

The synthesizer would receive the candidate change, the `I_tau`-derived obligation, and the relevant stated scope and premises, but not the final acceptance label. A held-out audit surface would test whether each arm detects seeded effects, effects outside `I_tau`, and cases on which rival theories disagree. Designing that audit so it does not reproduce the working theory's blind spots remains part of the problem.

The analysis should separate theory error, impact-derivation error, obligation mapping, procedure synthesis, observation-validity certification, containment, and cost amortization. Primary measurements would include harmful misses, detection coverage, projection calibration or deductive soundness, total evidence cost, procedure reuse, held-out retention, and rival-theory discrimination. Agent return alone would not establish useful acceptance evidence. Adaptive generation should outperform the non-adaptive synthesis baseline before its memory or curriculum machinery receives credit.

The experiment does not yet specify the synthesizer's objective, choose an independent observation-validity authority, or define what approval means when possible effects were not tested.

## Questions for the SPADE authors

Your view would be especially useful on these questions:

- Could SPADE's hint/no-hint rollout machinery be adapted from learning-value estimation to incumbent/candidate discrimination without rewarding arbitrary behavioral difference?
- Could the Environment Designer be conditioned on an explicit theory of the learner's failure or missing capability, and what intervention would show that the theory rather than extra context redirected its search?
- Could designer generation target a consequence on which rival system theories disagree, rather than merely maximize incumbent/candidate behavioral difference?
- What designer objective could target an explicit behavioral obligation while resisting reward hacking and candidate–evaluator co-adaptation?
- Which parts of SPADE's environment validation could transfer to generated evaluations, and what additional checks would be required before treating an environment as acceptance evidence?
- Could environment memory retain discovered regressions, false negatives, and redundant procedures without collapsing generation onto a narrow historical surface?
- When would adaptive generation amortize its construction and validation cost better than selecting from a fixed procedure registry?
- What experiment would most strongly falsify the claim that adaptive executable-procedure generation improves this selective-evaluation loop?

The [full explanatory-theories and deployment-time-learning workshop](./README.md) develops the proposed transfer from controlled HCL techniques to deployment-time learning, theory-guided candidate and evidence search, the on-the-spot versus retained-theory distinction, changed acceptance semantics, and the reach-assessment and audit problems created by correlated blind spots. We would welcome criticism of the bridge above, especially where this use misreads what SPADE's mechanisms can support.
