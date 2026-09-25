---
description: "SKILL.state tests structured current-state prompts against transcript and compression baselines, supporting selective loading while exposing schema sufficiency and evidence-retention limits."
source: https://arxiv.org/abs/2608.26263
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: cdcabbf1cf31570202db6e138059fb205521cc13ad9ea0da447f501579856230
ingested: "2026-09-25"
type: types/ingest-report.md
domains: [context-engineering, agent-runtime, execution-state]
---

# Ingest: SKILL.state: Scalable Long-Horizon Agent Skills

## Classification

An empirical runtime paper combining controlled procedural benchmarks, public interactive tasks, prompt templates, and a complexity argument. The captured text is arXiv version 3, dated September 2, 2026; it does not establish peer-review status. Authors: Sanket Badhe and Jonghyun Chung, affiliated with Google, and Priyanka Tiwari, affiliated with Purdue University. Results are author-reported; no implementation was inspected or executed for this ingest.

## Summary

[SKILL.state](https://arxiv.org/abs/2608.26263) replaces accumulated conversational context with an immutable procedure, a domain-authored structured state, and the latest observation. The model proposes dictionary mutations and an action; the runtime validates and applies the mutations, discards intermediate reasoning, and executes the action. With those supplied procedures and schemas, the reported benchmarks generally improve accuracy and reduce cumulative tokens against transcript, summary, and state-plus-transcript prompts. On Warehouse at 100 steps with Gemini-3-Flash, accuracy is 0.94 versus 0.91 for the state-plus-transcript baseline, using 65,408 versus 1,062,387 reported tokens. Capped compression controls also perform worse, but inconsistent character/token units limit claims of exact budget matching. The useful contribution is evidence for maintaining selected current state instead of repeatedly reconstructing it from history. It does not establish that fixed schemas are sufficient for arbitrary tasks, that all histories can be safely destroyed, or that state-only execution always improves accuracy. Constant prompt size additionally requires state contents and observations to remain bounded, not merely a fixed number of fields.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is empirical support for [Session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md): in the tested domains, supplied schemas let current-state prompts outperform several forms of historical replay or compression. The comparison concerns these runtime representations and prompts, not every implementation of a named framework. The paper's LangGraph-style baseline includes the full transcript; it does not characterize LangGraph as a whole.

It also supplies a useful boundary case for [Preserve evidence without making history the next context](../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md). Discarding reasoning permanently is a separate decision from excluding it from the acting prompt. The experiments do not compare permanent disposal against retaining an unloaded evidence archive. The paper itself identifies auditing, debugging provenance, and unforeseen later relevance as limits of history disposal.

Its mutable schemas compare with [Active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md): current facts must change or disappear as execution proceeds. However, its environment-state examples do not establish the note's richer lifecycle of evidence gates, closure, and extraction into durable knowledge.

## Extractable Value

1. **A controlled example for selecting current state at execution boundaries.** Warehouse comparisons include both unconstrained history and capped summary, window, and LLMLingua controls. At 100 steps with Gemini-3-Flash, the reported scores are 0.94 for SKILL.state, 0.52 for capped summary, 0.18 for the window, and 0.22 for LLMLingua. Within the supplied procedure and domain schema, these results suggest that what compression preserves matters beyond prompt length alone. They do not isolate JSON syntax from domain-aware content selection or test alternative schema designs. [quick-win]

2. **A precise condition on bounded-context claims.** The prompt contains procedure, serialized state, and latest observation. Its size is independent of execution length only when all three remain bounded independently of that length. A five-field schema containing growing hypothesis or discovered-item lists does not ensure this. This condition transfers more broadly than the benchmark scores and helps evaluate other state-based runtimes. [quick-win]

3. **Semantic state loss as an execution failure.** The paper attributes 68% of the examined small-model failures to premature overwrite or deletion, compared with 20% to schema/type confusion and 12% to JSON syntax. This makes destructive updates and omitted facts concrete evaluation targets. A focused experiment could distinguish syntactically valid but incorrect patches from malformed patches and test reconciliation after failed actions. The taxonomy alone does not show that constrained decoding would recover lost meaning. [experiment]

## Limitations (our opinion)

**The decomposition supplies much of the solution.** Procedures and domain schemas are fixed before execution; the model fills and revises state within that design. The paper compares runtime context strategies under those interfaces. It does not test discovering an adequate schema, revising the procedure, or selecting between alternative state decompositions. The claimed sufficient statistic is a substantive assumption: earlier evidence may acquire relevance only after it has been discarded. Task-state maintenance is not evidence of cross-task learning or self-improvement.

**Validation is not truth checking.** The runtime rejects malformed patches, but a well-formed patch can omit a necessary fact or assert an incorrect one. Algorithm 1 applies the patch before executing the action. The paper does not fully specify reconciliation when the action fails after a valid patch has been applied. Immediate recovery in successful scenarios follows a corrective alert; the canceled-order and closed-PR scenarios fail for every runtime. These results do not establish autonomous detection and repair of all state divergence.

**Reported gains have narrower scope than the strongest prose.** Synthetic results cover five generator seeds and selected horizons. SKILL.state scores 0.88 against the Stateful baseline's 0.94 on Software Repository at 25 steps; Gemma at 100 Warehouse steps ties Stateful at 0.42. Public results favor SKILL.state on success and cumulative tokens, but Retail's average prompt is larger than the baselines'. Fractional CTF percentages over a described 100-task suite lack a clear repetition explanation. The paper also alternates characters and tokens when describing the approximately 1,800 budget. These reporting gaps prevent precise independent interpretation of budget equivalence and aggregation.

**Noise resistance is not adversarial robustness.** Appendix C restricts injected noise to random, irrelevant, non-state-changing telemetry, despite broader main-text wording about rule overrides. The experiment supports filtering that noise under the supplied schema; it does not establish resistance to malicious instructions, relevant ambiguity, or deceptive state changes. Nor do reduced inference tokens establish that destroying an external evidence archive adds value: the KB's capture/loading distinction remains untested by this comparison.

## Recommended Next Action

Update [Session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md) with one bounded empirical example from SKILL.state, keeping the supplied-schema condition beside the result and preserving the distinction between excluding history from prompts and deleting evidence.
