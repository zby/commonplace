---
description: "Flywheel documents artifact-triggered workflows with separate admission, execution, and retry boundaries; a concrete case for KB automation design, without evidence of exactly-once effects."
source: https://docs.flywheel.paradigma.inc/concepts/hooks
captured: "2026-09-17"
capture: curl+trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 7efafdb13055c70c751d715e7dcb1fb4b83e2bb71324af69e6d61e2f19ee2ede
ingested: "2026-09-17"
type: ingest-report
domains: [workflow-automation, enforcement, observability]
---

# Ingest: Flywheel — Hooks And Automations

## Classification

Practitioner documentation specifying Flywheel's event-driven automation surface and operational failure categories. Author: Paradigma, the system's provider; authoritative for its stated contract, but not independent evidence of implementation correctness or production reliability.

## Summary

Flywheel hooks are persistent node-owned rules that match artifact finalization or eligible node-publication events, apply scope and deterministic filters, and launch observable asynchronous workflows. Artifact writes remain committed if a later hook fails. The documentation distinguishes one run per hook/event, suppression of unchanged-input reruns, and retries for selected execution failures. These rules do not establish exactly-once external effects. Organizer-owned hooks can process participant submissions using the organizer's authority while leaving attempt ownership unchanged. For KB automation design, the useful contribution is this separation of admission, ownership, execution, and recovery boundaries; the partial capture supplies a documented contract rather than tested implementation behavior.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a concrete documentation example for [Methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md): event selection, node scope, and filters govern activation, while workflow steps determine the response. The asynchronous boundary makes the distinction consequential. A reliably triggered hook does not itself block or reverse the artifact write that triggered it. This supports separating activation from response semantics without implying that every hook is an enforcement mechanism.

It also provides a bounded comparison with [Enforcement without structured recovery is incomplete](../notes/enforcement-without-structured-recovery-is-incomplete.md). Flywheel names terminal configuration failures and potentially retryable transport failures, making recovery policy distinct from event matching. The capture does not describe corrective, fallback, and escalation strategies as a complete recovery sequence, so it illustrates a narrower runtime distinction rather than validating the note's broader account.

## Extractable Value

1. **An event hook's placement determines what it can enforce.** Here, successful finalization precedes asynchronous execution, so a failed hook cannot serve as a precondition for that artifact's acceptance. This is a concrete example for the existing activation/response distinction, reusable when deciding where to place KB checks. [quick-win]
2. **Run deduplication and effect idempotency require separate guarantees.** The hook/event pair bounds enqueue cardinality, and the input-change policy suppresses some later runs. Neither specifies whether a retried HTTP step can repeat a remote side effect. This supplies a precise contract-reading distinction for future KB automations, not a demonstrated Flywheel defect. [just-a-reference]
3. **Ownership can separate participant work from organizer automation.** Root-owned subtree hooks can call evaluators or add review tags around participant submissions without transferring attempt ownership. This is a context-bound workflow reference for systems with shared contributions and centrally owned processing; it does not establish a general security property. [just-a-reference]

## Limitations (our opinion)

The retained capture is partial: several passages announce YAML examples whose code blocks are absent. It therefore cannot establish exact configuration syntax or executable examples. It also defers full runtime details to other contracts, leaving retry limits, backoff, crash recovery, and remote-effect idempotency unspecified here. No implementation was inspected or executed.

This is provider documentation, with no incident history, workload measurements, comparison, or evidence of performance under failure. Its run-state vocabulary and described behavior establish an intended operational contract, not achieved reliability. A simpler account of its contribution is ordinary event-driven workflow engineering; there is no evidence here that hooks improve knowledge quality or automate scientific judgment. In particular, the source explicitly leaves scoring and evaluator truth to each campaign's own contract. Organizer-owned credentials and participant event handling document authority placement, not resistance to hostile submissions.

## Recommended Next Action

Add Flywheel's post-finalization hook as a bounded example in [Methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md), showing why fixed activation alone does not make artifact acceptance conditional on automation success.
