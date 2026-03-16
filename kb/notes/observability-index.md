---
description: Index of notes about making hidden state, hidden failure, and quality drift visible — runtime inspectability, degraded-execution signals, and maintenance-oriented detection mechanisms
type: index
status: current
---

# Observability

Observability is about recovering signals that would otherwise stay hidden: execution paths that differ from the intended one, quality drift that has not yet become a visible failure, and system state that operators need in order to debug, maintain, and improve the runtime.

## Runtime visibility

- [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — inspectable orchestration is a precondition for seeing how a run actually progressed rather than inferring from the final artifact
- [Apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — successful outcomes can hide broken helpers and degraded execution paths, so final success alone is not a trustworthy operational signal
- [Silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — extends the same observability problem to underspecified specs: a useful artifact can hide that the contract did not determine the path and the runtime repaired it locally
- [Traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) — explains why programmers over-trust successful outcomes when semantic recovery hides the broken mechanism

## Detection & Signals

- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — catalog of weak signals that can make hidden quality changes visible enough to drive maintenance or learning loops
- [Notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — compresses many weak signals into ranked note quality so curation effort goes where it matters
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — dependency-aware staleness detection turns silent drift into an explicit review queue
- [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation-cannot.md) — adversarial reading supplies visibility into content failures that deterministic validation never surfaces

## Inspectable Substrate

- [Inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — the substrate choice determines whether failures and drift can be inspected, diffed, tested, and verified at all

## Related Tags

- [KB maintenance](./kb-maintenance-index.md) — maintenance consumes the signals observability exposes
- [Computational model](./computational-model-index.md) — runtime architecture determines which state transitions are inspectable
- [Learning theory](./learning-theory-index.md) — soft signals, oracle strength, and inspectable artifacts explain what observability can reliably support
- [LLM interpretation errors](./llm-interpretation-errors-index.md) — error correction and verification theory explain how visible signals can become actionable

## Other tagged notes <!-- generated -->
