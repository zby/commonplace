---
description: "Cordis formalizes reversible component effects and reactive dependency lifecycles, supplying a missing deployment substrate for dynamically changing agent harnesses"
source: https://github.com/cordiverse/paper/blob/main/paper.pdf
captured: "2026-08-14"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: eabef28217793ee9ee52a6bbba50234b31beac294222058f9df402b9f2b54919
ingested: "2026-08-14"
type: kb/sources/types/ingest-report.md
domains: [runtime-composition, harness-engineering, effect-systems, self-improving-systems]
---

# Ingest: A Programming Paradigm for Spatiotemporal Composability

## Classification

An 88-page preprint with a formal calculus, metatheory, TypeScript implementation, and an observational production case.
Author: Yifan Shi, Wei Zhang, and Tianyi Cui are affiliated with Peking University and DeepSeek-AI. Their authorship gives first-hand access to Cordis and Koishi, but the paper has no stated peer-review status and its implementation or production claims have not been independently reproduced in this KB.

## Summary

The paper splits dynamic software composition into two obligations: temporal composability, in which removing a component restores the effects it introduced, and spatial composability, in which components declare dependencies and react to their availability. It models the first with state-specific inverse witnesses accumulated for later recovery, the second with reactive coeffect specifications and notifications, and combines both in a unified context and component calculus. Under explicit assumptions, the authors prove preservation, recovery, dependency ordering, progress, and confluence properties. Cordis implements the model with effect tracking, dependency isolation and interception, component lifecycle management, declarative configuration reconciliation, and transactional hot module replacement. Koishi's four-year, 4,000-plus-plugin history supplies existence-and-adoption evidence for an earlier Cordis version; self-evolving agent harnesses remain a proposed application rather than an evaluated one.

## Connections Found

The paper is a formal technical basis for [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md): component registries and shared contexts become reliable only when their composition mode carries recovery, visibility, ordering, and isolation guarantees. It also bears on [Runtime structure determines the control surfaces available to governance](../notes/runtime-structure-determines-governance-control-surfaces.md), because Cordis obtains interception, dependency notification, local withdrawal, and rollback by forcing relevant operations through a mediated context.

The closest system comparison is [Autogenesis](../agentic-systems/autogenesis.md). Autogenesis supplies proposal, evaluation, versioning, and commit machinery for mutable harness resources but has relatively weak semantic gates; Cordis supplies a much stronger model of change application and dependency-coherent recovery but no optimizer or benefit oracle. The Koishi case must be read through [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): operating successfully inside Cordis does not validate the component seams, effect/coeffect partition, dependency representation, or system boundary that the case never varies.

## Extractable Value

1. **Dynamic harness composition has two independent correctness obligations** -- A component must cleanly relinquish what it changed, and its dependents must react coherently when its provisions appear or disappear. Versioning and rollback address only part of this lifecycle unless dependency activation and withdrawal are also specified. This distinction sharpens current harness-runtime analysis. [quick-win]
2. **Local rollback requires state-specific inverse witnesses and mediated mutation** -- Cordis records the inverse appropriate to the state at effect time, composes recovery in reverse order, and requires independent interleaved effects for arbitrary component withdrawal. This is a stronger design target than storing a previous file version, but it works only for resources whose mutations pass through the context and can be exclusively restored. [experiment]
3. **Change selection and change application are separate harness layers** -- Self-improvement systems need search and reject-capable evaluation to decide which change deserves adoption; they also need a substrate that can install, coordinate, and reverse the accepted change without resetting unrelated state. Cordis and Autogenesis expose these complementary responsibilities more clearly together than either does alone. [deep-dive]
4. **A target/committed split prevents lifecycle transitions from observing half-applied dependency state** -- Cordis computes intended availability separately from the committed view exposed during activation and retirement, then advances fibers through explicit states. This is a reusable transaction pattern for configuration reconciliation and hot replacement. [experiment]
5. **The theorem boundary is the mediated system boundary** -- Effects outside the context, non-exclusive external resources, and malicious component behavior are not made reversible by the calculus. Withholding or compensation may be possible, while hostile code still needs an external sandbox. The boundary should be declared before a runtime promises rollback. [quick-win]
6. **Koishi demonstrates sustained use, not comparative superiority** -- Thousands of plugins over four years show that the shared Cordis model can support a large ecosystem, but the paper reports no controlled baseline, overhead measurement, productivity comparison, or v4 production deployment. [just-a-reference]

## Limitations (our opinion)

The formal results depend on strong assumptions whose violations are common in agent harnesses. Relevant mutations must be mediated through the context and reversible; inverse witnesses are supplied by component authors rather than verified by the runtime; arbitrary withdrawal requires effect independence; and progress or confluence additionally relies on conditions such as acyclic dependencies, finite iteration, total provisions, or absence of failures. External emissions can at best be withheld or compensated, and malicious code remains outside the safety case.

The empirical evidence is observational and version-misaligned. Koishi is one TypeScript ecosystem with no controlled comparison, and its production deployment uses Cordis v3 while the paper presents refined v4 semantics and a redesigned loader. The authors do not measure runtime overhead, authoring cost, failure rates, or productivity, so adoption cannot identify which mechanism caused the ecosystem to work.

There is no learner in the Koishi case, so the fixed-decomposition lens applies to the design inference rather than to learned behavior. Available signals and histories are component declarations, mediated effects, dependency availability, lifecycle/configuration changes, hot-module dependencies, and failures. The runtime can compose activation, deactivation, reload, withdrawal, isolation, interception, configuration reconciliation, and recorded inverses. Its effective mapping is from declared provisions, requirements, and target/committed state to those lifecycle responses. Fixed outside that space are the component/fiber split, effect/coeffect partition, key-based dependency representation, component granularity, context-mediated boundary, and the assumptions used by the theorems. Koishi shows that this compound configuration can operate at scale; it does not show that those fixed choices are necessary or best. The proposed self-evolving-agent use case is not evaluated at all.

## Recommended Next Action

Write a new theoretical note under `kb/notes/` titled **Self-modifying harnesses need a recovery and dependency-coordination substrate, not only an optimizer**. Use Cordis to define the change-application layer and Autogenesis plus the proposal-selection loop to distinguish it from search, evaluation, and operative retention; preserve the system-boundary and fixed-decomposition limits above.
