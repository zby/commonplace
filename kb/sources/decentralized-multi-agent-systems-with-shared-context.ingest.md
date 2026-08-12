---
description: "DeLM's verified shared-state experiments support coordination guarantees and hierarchical context scheduling while leaving the fixed decomposition untested"
source_snapshot: "decentralized-multi-agent-systems-with-shared-context.md"
ingested: "2026-08-12"
type: kb/sources/types/ingest-report.md
domains: [multi-agent-systems, agent-orchestration, context-engineering, test-time-scaling]
---

# Ingest: Decentralized Multi-Agent Systems with Shared Context

Source: [decentralized-multi-agent-systems-with-shared-context.md](./decentralized-multi-agent-systems-with-shared-context.md)
Captured: 2026-08-12
From: https://arxiv.org/abs/2606.10662

## Classification

Genre: scientific-paper -- an arXiv preprint with a specified architecture, benchmark comparisons, modular ablations, robustness checks, and trace-level mechanism examples.
Domains: multi-agent-systems, agent-orchestration, context-engineering, test-time-scaling
Author: Yuzhen Mao and Azalia Mirhoseini are Stanford researchers; the paper gives enough implementation and experimental detail to inspect its design claims, but this captured `v1` is a first-party preprint rather than independent replication.

## Summary

The paper presents Decentralized Language Models (DeLM), a multi-agent framework in which workers asynchronously claim tasks, read compact verified updates from a shared context, and publish new gists after compression and evidence checking. Long source units remain recoverable through a `gist -> reference-grounded summary -> raw evidence` hierarchy, while a dependency-aware queue controls ready work and lets the last finishing worker propose more tasks or finalize. On SWE-bench Verified, DeLM reports the best Avg.@1, Pass@2, and Pass@4 results for Gemini 3 Flash and Claude Opus 4.6, including 65.7% Avg.@1 and 77.4% Pass@4 at $0.12 per task with Gemini. On LongBench-v2 Multi-Doc QA it reports the highest average accuracy across four model families; with GPT-5.4, removing admission verification lowers accuracy from 60.1% to 55.2% and removing the intermediate summary layer lowers it to 57.7%. On aggregation-heavy OOLONG, natural-language DeLM trails code-mediated RLM, but a hybrid of decentralized coordination and RLM workers outperforms either alone.

## Connections Found

This paper is an empirical anchor for [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md): its shared channel is paired with evidence-grounded admission, write-before-publish atomicity, and snapshot visibility, and its no-verification ablation measures one missing guarantee. It is also a worked implementation of [Decomposition heuristics for bounded-context scheduling](../notes/decomposition-heuristics-for-bounded-context-scheduling.md), especially representation choice, reusable intermediate state, selective co-loading, and verifiable boundaries.

DeLM is a boundary case for [Topology, isolation, and verification form a causal chain for reliable agent scaling](../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md): workers have local task contexts but share verification-gated mutable state, so shared state is not equivalent to an ungoverned scratchpad. The experiments do not isolate local scoping, admission verification, compact representation, and atomic visibility, however. Interpreting the gains therefore rests on [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): the ablations support the verifier and hierarchy choices they vary, not the entire fixed queue-and-context decomposition.

## Extractable Value

1. **Verification-gated shared state is a distinct coordination regime.** DeLM combines locally bounded workers with globally reusable state whose write path is checked and atomically published. This sharpens the KB's current isolated-branches-versus-shared-scratchpad contrast: the governing variable may be the admission and visibility contract, not sharedness alone. Establishing that higher-reach claim requires an experiment that independently varies local isolation, admission verification, and publication discipline. [deep-dive]

2. **The LongBench ablation separates an admission guarantee from a representation layer.** Removing verification changes GPT-5.4 average accuracy from 60.1% to 55.2%; separately removing the reference-grounded summary layer changes it to 57.7%. Relative to the existing orchestration notes, this is unusually direct evidence that grounding before reuse and coarse-to-fine recoverability contribute independently within the tested configuration. [quick-win]

3. **Negative findings and binding constraints are first-class handoff artifacts.** The SWE-bench traces show workers reusing a failed printer hypothesis, a multi-valued-relation safety constraint, and a compact patch summary. The examples give the KB a more precise boundary-return vocabulary than generic “agent output,” although trace anecdotes do not establish how often each mechanism causes benchmark gains. [experiment]

4. **Semantic admission and concurrent consistency are separate guarantees.** DeLM verifies whether a gist is supported, writes detailed backing content before publishing its label, exposes lock-free snapshots to readers, and serializes only the queue-empty decision. This decomposes “verified shared context” into grounding, publication order, read visibility, and work ownership; it does not solve semantic conflict between two individually supported updates. [just-a-reference]

5. **Coordination and local reasoning substrate can be composed independently.** Vanilla DeLM is weak on exact OOLONG aggregation, while RLM supplies code-mediated inspection and computation; the DeLM+RLM hybrid reports the best accuracy and lowest cost on both OOLONG and the paper's GPT-5 LongBench-v2 comparison. This supports treating shared coordination and the worker's natural-language-versus-symbolic operation set as separate design axes rather than rival whole-system packages. [experiment]

6. **Context efficiency has workload-dependent costs.** Compact shared discoveries cut repeated SWE-bench work and halve cost in the Gemini comparison, while hierarchical summarization and verification add upfront LongBench cost. The stable shared-context prefix also creates a claimed KV-cache opportunity. This is evidence for measuring both per-worker context feasibility and aggregate traffic, not for a universal claim that decentralized coordination is cheaper. [just-a-reference]

## Limitations (our opinion)

The strongest causal language exceeds what the comparisons isolate. On SWE-bench, DeLM differs from centralized and independent baselines in shared-state representation, admission verification, task scheduling, information visibility, and merge policy together. The LongBench modular ablations are cleaner, but they test verification and hierarchical summarization only in the fixed DeLM pipeline with GPT-5.4; they do not show that decentralization, the task queue, or the full three-level representation is optimal. The 125 LongBench samples are split into small domain subsets, and the reported three-run averages do not replace replication on other long-context workloads.

The admission verifier checks support against supplied trajectories, summaries, or raw spans. That is narrower than correctness: two conflicting claims may each be textually supported, and generator and verifier may share model-induced errors. The paper does not report verifier discrimination, correlated-error tests, adversarial writes, semantic conflict resolution, stale-entry behavior, or failures under many concurrent writers. Its atomic publication and snapshot reads address systems consistency, not all semantic consistency identified in [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md).

Under the fixed-decomposition lens, workers can condition on the task, queue and dependency state, admitted gists, local tool/reasoning history, and unfolded summaries or raw evidence. They can claim work, inspect or execute, compress, verify, publish, unfold, enqueue follow-up tasks, and finalize; the selected base models and prompts determine which mappings over those inputs are expressible. The shared gist schema, summary hierarchy, global-context partition, task-queue protocol, decomposition and finalization prompts, verifier design, concurrency limits, model assignments, benchmarks, and baseline implementations remain fixed outside that effective update space. Improvements within it show that the compound design worked on these evaluations. They do not establish that adjacent fixed choices, or the decomposition as a whole, caused the gains.

Finally, the trace examples are mechanism illustrations selected by the authors, not a systematic mediation analysis. A simpler account for part of the SWE-bench result is that compact cross-attempt hints increase useful token allocation regardless of decentralization; a controlled comparison would hold the summaries and information content constant while changing only who schedules, admits, and broadcasts them.

## Recommended Next Action

Update [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) with DeLM as a measured verification-gated shared-state case: record the 60.1% to 55.2% no-verification ablation, distinguish evidential admission from atomic visibility and unresolved semantic conflict, and retain the fixed-decomposition limit on what the experiment supports.
