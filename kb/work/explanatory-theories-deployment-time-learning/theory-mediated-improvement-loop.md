# A provisional theory-mediated improvement loop

> **Status:** This is an exploratory extension of the workshop. It distinguishes where a system theory can enter a proposal-selection loop and what an on-the-spot theory experiment can establish. It does not specify a settled theory representation, search algorithm, or retention gate.

Selective evaluation is only one use of a theory about the system. In a [proposal-selection improvement loop](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), a theory can help search bring better changes into consideration, help evaluation choose among those changes, and help decide which evidence is worth acquiring. Evidence from the resulting trials can then bear on both the system change and the theory that produced it.

This makes the theory a shared intermediate object across the loop rather than only an evaluation prior.

## Two coupled proposal-selection loops

Let `S_n` be the deployed system state and `Omega_n` the prediction boundary, including assumptions about the model, runtime, evaluator, environment, authority, and routing. Let `T_n` be a retained theory, if one exists, about relevant parts of the system's behavior-generating organization, and let `z_n` contain the current objective and deployment evidence. `tau_n` is the working theory active in the episode: it may be constructed from `S_n`, `Omega_n`, and `z_n` on the spot, or produced by retrieving and applying `T_n` to the present case. The system-change loop can use it in this path:

`tau_n + S_n + Omega_n + z_n -> candidate search -> Delta candidates -> benefit and impact projections -> evidence acquisition -> candidate decision -> S_{n+1} or S_n`

A second loop operates on the theory itself:

`T_n + tau_n + candidate outcomes + independent audits -> theory-revision search -> candidate T' -> reach-assessment -> theory decision -> T_{n+1} or T_n`

The loops interact. The active `tau_n` can guide search for `Delta`; tests of `Delta` can discriminate among candidate theories or reveal that retained `T_n` needs revision. They do not collapse into one decision. A candidate change may work for a reason the proposed theory gets wrong, so the system may accept `Delta` without accepting that theory. A failed candidate may still expose a useful counterexample, so the system may reject `Delta` while retaining a revised theory.

The theory therefore needs its own proposal, assessment, and retention path. Rejecting a system candidate preserves `S_n`, just as rejecting a proposed `T'` preserves `T_n`; acceptance produces `S_{n+1}` or `T_{n+1}` in the corresponding loop. HCL's harness commitment gate cannot be silently reused as a theory-acceptance gate: current-task improvement and sampled retention establish behavior on checked cases, not the explanatory-reach of the rationale offered for the change.

## Where theory can change the improvement loop

A theory can contribute at five distinct points:

1. **Problem diagnosis and search allocation.** It can explain which mechanism or constraint produced an observed failure, identify the intervention locus, rule out irrelevant components, and allocate candidate-generation effort.
2. **Candidate generation and pre-evidence prioritization.** It can derive changes expected to improve the objective, predict which premises each candidate relies on, and allocate execution budget among candidates. This is different from merely explaining a candidate after it has been written.
3. **Evidence selection.** For a fixed candidate, it can derive the candidate-specific impact projection `I_tau(S, Omega, Delta)` developed in the [selective-evaluation model](./selective-evaluation-model.md), then help select or generate procedures that discriminate benefits, regressions, and rival explanations.
4. **Post-evidence candidate decision.** Given the same candidates and observations, it can relate results to predicted mechanisms, estimate unresolved consequences, rank candidates, or recommend rejection. Theory-derived projections remain claims to test rather than empirical evidence, so the commitment gate must preserve that distinction.
5. **Evidence interpretation and theory revision.** It can explain why a result bears on a candidate or theory, update an applicability condition, and carry the revision into later search and evaluation.

These uses can fail independently. A theory may locate a promising intervention while underestimating its regressions, or select discriminating evidence while proposing no useful change. The experiment should therefore isolate search quality, candidate selection, evidence selection, and cross-episode retention before testing their joint effect.

## On-the-spot construction is an ephemeral-theory treatment

The first practical experiments can ask an LLM to construct `tau_n` from `S_n`, `Omega_n`, and `z_n` inside the current run. Making the working theory explicit before it is used gives the experiment an inspectable intermediate artifact: stated mechanisms or invariants, assumptions, scope, and predictions. That can test whether explicit theory construction improves this episode's search or selection compared with asking the same model to propose or choose directly.

It does not yet test cumulative theory-mediated learning. If `tau_n` is discarded after the decision, the next episode must reconstruct it. The LLM supplies interpretation but the pathway lacks the retained, separately revisable object required by [theory-mediated self-improvement](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). Performance gains would show immediate reasoning value, not that theories accumulate or make later improvement cheaper.

The retained treatment instead begins episode `n` with an addressable `T_n`, records whether the system actually retrieves and consumes it, and permits a separately gated update to `T_{n+1}`. Its advantage must be measured against the cost of storage, retrieval, applicability checking, maintenance, and correction. Retention can also entrench a broad false theory, so it is not presumed to dominate reconstruction.

## Object theories and improvement-process theories

The Exo case exposes two theory targets that should not be collapsed. The working `tau_n` above is an **object-level system theory**: it explains behavior-generating relations relevant to the current problem and candidate change. A **promotion and revision theory** is meta-level: it says what observations warrant promotion, which retained form and authority a result should receive, how it should be routed into later work, and what should revise, rescope, codify, supersede, or retire it.

The meta-level theory can alter candidate formation and retention in both loops, and it can itself become an operative part of `S_n`. It still does not replace an object-level account of why a proposed change should work or what else it may affect. A useful promotion rule is not evidence that `tau_n` is true; a sound object theory does not decide whether retaining it is worth its lifecycle cost. Experiments should identify which theory type a treatment supplies and gate changes to the improvement process independently of the candidates that process judges.

## Ordering and independence controls

An on-the-spot rationale written after seeing a candidate cannot establish that theory guided candidate search. For a search claim, the experiment must record the provisional theory before candidate generation and vary access to it. For an evidence-selection claim, it must record the candidate-specific projection before evaluation outcomes are revealed. Post-hoc explanations remain useful diagnostic artifacts, but they are a different treatment.

Using one LLM for theory, candidate, and evaluation roles also creates correlated error. A theory can narrow search to candidates that confirm it, select only evaluations inside its predicted surface, and then appear well calibrated on the evidence it chose. Fixed full-evaluation phases, held-out change families, rival-theory cases, randomized omitted-region audits, and role or information separation are ways to expose this feedback loop. None is a complete theory oracle.

## Application and source boundary

The three external systems motivate different parts of this architecture:

| System | Contribution used here | Boundary |
|---|---|---|
| [HCL](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) | A governed proposal-evaluation-commitment protocol for isolated harness candidates | Its frozen model analyzes evidence and proposes edits, but it does not expose a separately versioned theory with premises, predictions, and a revision history. |
| [SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) | Adaptive generation, filtering, and valuation of executable procedures | Its shared model generates environments and task-local hints, but it does not retain an explicit theory of the learner or harness that guides those proposals. |
| [Exo](../../agentic-systems/exo.md) | A protected substrate, mutable executor, durable events, and retained artifact surfaces on which an accepted change can remain operative | Those source-pinned affordances establish a possible application substrate, not beneficial self-improvement, an explicit theory lifecycle, or a compounding pathway. |

Exo supplies an architecture in which the end-to-end distinction can be tested. An accepted `Delta` can become operative `S_{n+1}` through a durable rewrite or retained artifact. That would instantiate deployment-time learning if the change arose from task evidence and later behavior used it. It would not by itself show compounding. The stronger test asks whether an earlier retained theory, evaluator, promotion rule, or other benefit changes the cost, reliability, breadth, or human dependence of producing a later improvement, with a causal trace between episodes.

This workshop's on-the-spot theory artifact is a proposed experimental intervention. The retained-and-revised theory path is the stronger cumulative theory-mediated self-improvement hypothesis. Deployment-time learning can still occur through retained harness changes without retaining a theory.
