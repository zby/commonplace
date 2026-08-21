---
description: Proposes an offline selector comparison, a separate adaptive-procedure factor, independent audit labels, full cost accounting, and a trajectory-aware online phase.
type: kb/types/note.md
---

# Experiment design for causal selective evaluation

> **Status:** This is a proposed comparison, not a completed experiment or implementation plan. It does not establish that selective evaluation or generated procedures reduce total cost.

Selective evaluation means choosing which costly checks to run for each harness candidate instead of always running the full registered set. A credible test should separate selector policy from procedure source. First, it should compare selection policies over trusted registered procedures. Then it should test SPADE-inspired adaptive procedure generation as a separate factor. Every arm needs an independent audit surface and full cost accounting so that doing less evaluation is not mistaken for performing better.

## Offline comparison

The offline phase tests the [provisional selective-evaluation model](./selective-evaluation-model.md) on a fixed recorded candidate set. Every arm should see the same candidate interventions and have matched access to the obligation registry, procedure metadata, and available cost estimates. The comparison should include full registered-set evaluation, uniformly sampled anchors, deterministic dependency selection, diff-similarity selection, and causal selection. If selectors receive different structural information, that difference should be recorded explicitly as part of the treatment rather than hidden inside the method name.

The full registered set is a baseline, not complete ground truth. Before selector outputs are revealed, the study should build an independent reference surface from seeded known effects and held-out human-audited obligations. During scoring, it should also continue random audits of obligations that each selector would omit. A **harmful miss** is a material effect identified by this reference process that an arm fails to surface before its commitment decision. Discoveries outside the reference surface reveal limits in that surface and should inform later audits, but they do not retroactively turn the initial labels into a perfect oracle.

Coverage needs two separate measures. **Procedure availability coverage** asks whether the registry or generator can supply a procedure capable of observing a reference obligation. **End-to-end detection coverage** asks whether the selected or generated procedure actually detects the seeded or audited effect. Calibration compares predicted impact probabilities with independently audited effects. Together, these measures distinguish bad impact prediction from missing procedures, invalid observations, and selection failure.

Cost accounting should include model calls, tokens, latency, dollars, environment actions, retries, construction, technical and observational validation, sandboxing, execution, human adjudication, maintenance, and reuse. The protocol should predeclare its primary endpoints and advance rule. An arm supports an efficiency claim only if it reduces total cost while staying within prespecified harmful-miss and calibration bounds. Otherwise, the result is a measured tradeoff, not a success.

The first comparison should keep the procedure registry fixed so that it isolates selector quality. A second comparison can then cross qualifying selectors with two procedure-source conditions: selection from the fixed registry, and adaptive retrieval, adaptation, or generation. This ordering prevents failures in generated procedures from being attributed automatically to the selector.

## Online comparison

The fixed-candidate phase establishes only an offline contrast. Different commitment decisions change later harness states, operator responses, and candidate opportunities, so they also change adoption trajectories. A separate online comparison should therefore start repeated runs from common checkpoints, standardize candidate and operator inputs where possible, and record every branch that cannot be controlled. Delayed full audits should measure retained performance, newly discovered misses, cumulative evaluation cost, and reversals of earlier commitment decisions.

If candidate generation or operator behavior cannot be held fixed, the study should treat the resulting divergence as part of the end-to-end outcome. It should not claim to have isolated selector quality from every downstream effect. That is why the online phase cannot substitute for the fixed-candidate comparison, and why the offline result alone cannot establish deployment value.

## Adaptive procedure generation is a separate factor

[SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) generates executable Python environments and trains an agent to act inside them. Its released code supports environment generation, feasibility filtering, and a learning-value signal. Its reported training and benchmark gains, however, remain paper-only and unreproduced in this KB.

SPADE matters here as an architectural example, not as evidence for the causal selector. It shows that an evidence-acquisition policy could retrieve, adapt, or synthesize a procedure instead of mapping every obligation to a fixed registered evaluation. It does not show that an impact theory correctly identifies affected functions, that a generated procedure observes the intended obligation, or that generation protects a separately versioned harness against regression.

The generation condition therefore needs its own checks. **Technical validity** asks whether the procedure executes, remains contained, and satisfies its structural constraints. **Observational validity** asks whether its success criterion detects the intended obligation against the independent reference surface. **Decision value** asks whether constructing and running the procedure is worth its cost for the current commitment. A separate omitted-region audit should check effects that neither the selector nor the generated procedure chose to expose.

Generation may improve detection, increase cost, or both. The inspected SPADE loader executes generated Python, while feasibility and solvability checks do not by themselves establish containment or observational validity. Construction, validation, sandboxing, execution, and reuse should therefore be measured parts of the generation factor, not presumed savings.
