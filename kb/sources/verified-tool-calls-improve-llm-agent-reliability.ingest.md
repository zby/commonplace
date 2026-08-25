---
description: "Controlled simulation finds that effect verification before retry cuts duplicate tool actions, while a fixed simulator and bundled treatment limit attribution"
source: https://arxiv.org/abs/2608.02645
captured: "2026-08-22"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: bfaa8426ac9b4d79d6f45164deaa35cbd48d93833785800865bb0ea1530c5d2d
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [agent-reliability, tool-use, distributed-systems, runtime-verification]
---

# Ingest: Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures

## Classification

A v1 scientific preprint with a formal wrapper algorithm, controlled fault injection, fixed-seed comparisons, an ablation, and reported confidence intervals. Its evidence is simulator-based rather than production-based.
Author: Isham Kalappurackal Mansoor and Pratip Rana are affiliated with Old Dominion University, and Abhishek Phadke with Christopher Newport University. The paper exposes its model, tasks, fault probabilities, retry budget, run counts, and principal outcomes, but no implementation was inspected or executed for this ingest.

## Summary

The paper separates a tool's response channel from its effect on world state: a timeout, stale read, or incomplete response may coexist with an already-applied action. It wraps a ReAct-style Gemini Flash-Lite agent with task-specific postcondition checks, three-valued verification (`true`, `false`, or `unknown`), verify-before-retry control, and idempotency keys. In 300 main-comparison runs over two simulated workflows and three injected-fault levels, the wrapper sharply lowers duplicate messages and writes while keeping or improving final task success. The strongest result is execution safety rather than retry itself: in a separate one-task ablation, verify-only outperforms the full verify-before-retry method, so another retry can add faults even after verification.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a bounded empirical anchor for [Final task success does not establish intended-path health](../notes/final-task-success-does-not-establish-intended-path-health.md): successful terminal state and safe execution diverge when retries duplicate effects. It gives [structured recovery](../notes/enforcement-without-structured-recovery-is-incomplete.md) a concrete tool-boundary branch over verified effect state. Its closest technical comparison is [ToolGate](./toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md), which validates returned results before trusted-state commit; this paper instead verifies external effects after an ambiguous response and before retry. [GBrain](../agentic-systems/gbrain.md) provides the closest inspected runtime comparison through durable tool-execution journaling and replay of only pending idempotent tools. The paper's evidence remains bounded by [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): it improves recovery inside a supplied task, verifier, action, and simulator design without testing whether those fixed choices are the right decomposition.

## Extractable Value

1. **Tool response and tool effect are separate evidence channels** -- relative to the KB's pre-commit ToolGate case, this identifies the distinct post-dispatch acknowledgement gap: transport failure does not show effect absence, so blindly retrying a non-idempotent action is unsafe. This is the highest-reach contribution. [quick-win]
2. **Path-sensitive metrics expose reliability that terminal success hides** -- the paper reports duplicate side effects separately from task success; in the high-fault invoice condition, the baseline still succeeds in 96% of runs while duplicating effects in 76%. This directly strengthens the KB's outcome-versus-path distinction. [quick-win]
3. **Recovery needs a three-valued effect oracle plus a deduplication boundary** -- `unknown` distinguishes stale or incomplete observation from verified absence, while a stable idempotency key limits the race between a verification read and a retry. The combination is a reusable runtime pattern, but it still needs real-API testing. [experiment]
4. **Retry is not the source of the reported gain** -- in the separate medium-fault `activate_customer` ablation, verify-only reports about 80% success and 20% duplicates, compared with about 72% and 28% for the full method. Recovery policies should preserve wait, stop, or escalation choices instead of treating verified retry as automatically beneficial. [experiment]
5. **The four fault classes form a compact test-fixture vocabulary** -- timeout after dispatch, delayed visibility, partial success, and stale conflict cover distinct response/effect disagreements that an agent tool harness can inject independently before testing its recovery policy. [deep-dive]

## Limitations (our opinion)

The experiment tests two hand-built simulated workflows, one model, one ReAct loop, manually authored postconditions, at most one retry, chosen fault probabilities, and 25 episodes per main configuration. The learner can condition on tool responses, verifier reads, and a retry counter; it can compose only the supplied task actions, read-only verification, backoff, and retry. Task representation, tool schemas, verifier completeness, fault semantics, idempotency support, prompts, and metrics remain fixed outside that effective space. The gains therefore show improvement within this design, not that the design generalizes to production APIs or that its fixed decomposition is preferable.

The main baseline-versus-wrapper contrast changes postcondition verification, retry policy, idempotency use, and prompt/wrapper behavior together. The separate ablation runs only one task at medium fault under a different configuration. Under [the actual-contrast rule](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), it supports that local comparison but cannot assign every main-run gain to verification, idempotency, or retry individually. Outcomes are aggregated by fault level rather than reported per injected failure class, so the experiment also does not establish equal effectiveness against all four classes.

The decisive verifier is supplied by the experimenter. Real systems must define complete postconditions, distinguish stale reads from absent effects, and obtain server-side idempotency or accept a remaining race window. No source code was inspected, the simulator was not reproduced, and the paper's reported performance remains paper-only outcome evidence.

## Recommended Next Action

Write `kb/notes/safe-retries-after-ambiguous-tool-failure-require-effect-verification-or-idempotency.md`, using this paper as bounded empirical evidence and ToolGate and GBrain as adjacent boundary cases; state explicitly that the simulation supports the tested wrapper contrasts, not the fixed task or verifier decomposition.
