---
description: "Controlled authorization histories show memory writers creating false permissions, with exact-state repair isolating their effect and provenance defenses exposing safety–utility costs."
source: https://arxiv.org/abs/2609.01836
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: f51e7a14e3a299e7901dca11c7cabda23c2e95ed890f568341469e6d9dd6d0be
type: kb/sources/types/ingest-report.md
domains: [agent-memory, authorization, evaluation]
learning_claims: true
---

# Ingest: Agent Memory Is a Surface for Endogenous Authorization Laundering

## Classification

Scientific paper: an arXiv preprint by Tommaso Cerruti, Mika Okamoto, and Ansel Kaplan Erol, affiliated with ETH Zurich and Georgia Institute of Technology. It reports a controlled benchmark, memory interventions, and mitigation comparisons. The work was conducted through EleutherAI's SOAR program; Baseten sponsored part of the inference. The authors report releasing code and artifacts, but this ingest assesses the paper without inspecting or executing that implementation.

## Summary

[EAL-Bench](https://arxiv.org/abs/2609.01836) tests whether authentic, non-malicious histories become false permissions when agents maintain persistent memory. Five writers build free-text or typed profiles, either from complete history or incrementally from prior memory plus a new block; two executors receive only the resulting memory and a request. A hidden deterministic ledger supplies authorization truth for synthetic procurement, cybersecurity, and finance cases. Typed incremental memory grants false authority for 28.3%, 10.4%, and 50.2% of unauthorized requests respectively. In selected naturally erroneous typed-memory trials, executors perform unauthorized actions in 98.6% of replays; replacing only memory with exact state reduces this to zero. Within the shared typed-incremental comparison, source-authority gating and bounded event sourcing reduce unauthorized submissions but also block substantial legitimate use. These results locate an authorization failure in the maintained state under this writer–memory–executor separation; they neither estimate deployment prevalence nor establish a universally preferable memory architecture.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies controlled evidence for [a consumption channel delivering force without the authorizing history](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). Memory-only replacement removes unauthorized actions behind executors that pass faithful-memory controls. This supports the note's non-adversarial case: an authorized writer can still produce content whose operative permission exceeds its grounds. The source-authority gate checks cited principals and visibility, not whether the messages entail the stored scope or preserve current validity; residual errors support the note's distinction between provenance and the authorization decision.

It also gives [memory lifecycle operations](../notes/agent-memory-requirements/retire-redact-supersede-relax.md) a behavioral evaluation: retaining revoked or inactive grants can cause unauthorized action, while conservative filtering can discard valid grants. This is evidence for testing lifecycle semantics, not evidence that lifecycle fields alone suffice. Compared with [The Memory Trust Gap](./the-memory-trust-gap.ingest.md), which varies evidence already supplied to a consumer, EAL-Bench additionally measures writer formation against known authorization state and transfers frozen memories between calibrated executors. Both use oracle-correct input to isolate harmful reliance, without establishing a deployed repair process.

## Learning Claims (our opinion)

The mechanism is fixed-model adaptation through persistent state: a writer updates its account of permissions as new history arrives, and that account changes later action. The exact-state intervention establishes that the account is operative. It does not by itself establish [conjectural learning](../notes/definitions/conjectural-learning.md): replacing state with an experimenter's oracle is not the agent criticizing its own account, and ordinary permission updates need not be formulated tentative theories. The paper primarily measures fidelity loss during adaptation.

Typed records make scopes and lifecycle states individually inspectable, a structural parallel to [addressable theory](../notes/definitions/addressable-theory.md). Their higher failure rates in incremental conditions show that inspectability alone does not preserve correctness. The procurement candidate-selection experiment improves downstream behavior as candidate pools grow, but reviewers often miss available exact memories and the tested incremental typed trajectories show no self-repair. This is evidence for a limited selection process, not demonstrated autonomous correction of retained errors.

The [effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) is consequential here. Incremental writers cannot revisit earlier raw blocks, and executors cannot consult the underlying history. Expanding the advertised capacity largely leaves profile size unchanged; that ablation varies a limit inside profile rewriting, not access to immutable history. Event sourcing does compare another architecture, but jointly changes extraction, accumulation, and reduction. Its improvement cannot identify which component deserves the credit. The source therefore strengthens the need to assess what information an updater can recover while leaving comparisons with raw-history retrieval open.

## Extractable Value

- **Separate false-authority formation from action propagation.** [experiment] Freeze memory before observing behavior, score typed permissions against known state, and replay matched authorized and unauthorized requests behind faithful-memory-calibrated executors. In the source's selected erroneous-memory trials, 205 of 208 replays submit the unauthorized action and none do after exact replacement. This method localizes a memory-mediated failure without treating its conditional propagation rate as its overall incidence.
- **Test authorization semantics beyond provenance.** [quick-win] A valid citation to an authorization-capable principal can coexist with a revoked, inactive, or incorrectly scoped permission. Retain this as bounded evidence for the consumption-channel note: the tested gate intentionally omits entailment and lifecycle checks, so its residual failures reveal what source filtering leaves unchecked.
- **Measure legitimate use alongside blocked violations.** [experiment] On the same typed-incremental population, gating reduces unauthorized submissions from 25.3% to 7.3% while authorized use falls from 93.3% to 53.8%; event sourcing reaches 9.0% and 64.7% respectively. The latter uses model-extracted changes, an external immutable log, and a deterministic reducer. These are three observed operating points, not a complete safety–utility frontier or an isolated test of deterministic reduction.
- **Distinguish capacity from recoverable history.** [just-a-reference] The procurement capacity intervention weakens the explanation that the explicit token cap alone causes errors. Writers still receive only prior memory and the new block, rarely consume the additional allowance, and show inconclusive safety changes. It supplies no general result against larger memories, raw-history access, or retrieval-based correction.

## Limitations (our opinion)

The 36 cases use synthetic, ordered, complete histories with explicit authority classes and deterministic ground truth. Requests differ in one controlled field, and tool calls are simulated. Real policy conflicts, missing records, concurrent writers, multiple profiles, service failures, and side-effect recovery are outside the experiment. The headline percentages characterize these constructed cases, not operational prevalence or inherent differences between industries.

The strongest causal result is that replacing erroneous memory changes action while other inputs remain fixed. It does not show that executor safeguards generally cannot help: history verification, external policy enforcement, or refusal under uncertainty would alter the tested interface. Exact repair assumes access to truth unavailable to the agents. Deterministic formation labels apply only to typed memory; free-text outcomes cannot be assigned the same representation-level denominator.

The source-authority gate assumes known authorization-capable principals and deliberately permits unrelated messages from them. Its large reduction does not validate a full authorization checker. Event sourcing retains an extraction bottleneck, and its whole-architecture comparison cannot isolate the log, reducer, or prompt as the cause of improvement. Domain-specific utility losses are substantial: event sourcing reduces finance authorized use from 98.3% to 13.3%. Pooled improvements obscure that deployment constraint.

Three seeds support descriptive replication over fixed cases. Pressure and some diagnostic comparisons use one seed; pressure effects also differ between executors. The procurement-only capacity and candidate-selection studies cannot establish general scaling laws. All experimental outcomes here remain author-reported, without independent reproduction.

## Recommended Next Action

Update [A consumption channel delivers force without the history that earned it](../notes/a-consumption-channel-delivers-force-without-the-history-that.md) with EAL-Bench as a controlled non-adversarial example, preserving the memory-only repair comparison and the distinction between source-authority checks and current permission semantics.
