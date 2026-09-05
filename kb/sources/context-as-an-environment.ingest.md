---
description: "Scroll makes long-horizon context an executable environment over exact history, supporting bounded working views while exposing fixed harness choices"
source: https://arxiv.org/abs/2608.21690
captured: "2026-08-27"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 0dd117f22a91f911da2099773f362b2738651b16978d12532e6a6cb6886d6c9b
ingested: "2026-08-27"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, agent-memory, long-horizon-agents, evidence-preservation]
---

# Ingest: Context as an Environment

## Classification

An arXiv technical report that specifies an agent context-management architecture and evaluates it with controlled component ablations, cross-backbone runs, memory benchmarks, and a long-horizon acting benchmark.
Author: Yin Lin, Elaine Ang, Erkang Zhu, Bolin Ding, and Jingren Zhou are affiliated with Alibaba Group and Columbia University. As Scroll's designers, they have direct access to its architecture and runs but also an interest in favorable framing. The report names a public implementation branch, but this ingest is paper-grounded and does not inspect or execute it; the retained version does not report peer review.

## Summary

Scroll keeps accumulated agent history outside the prompt in a Session Environment comprising an append-only Event Log, externalized payloads, and a persistent sandboxed Python namespace. The model writes code to locate, materialize, and transform that state, while only explicit `print` output enters the next bounded working view; an address-anchored eviction index keeps removed spans navigable. With Qwen3.8-Max, the paper reports 94.8 on LongMemEvalS, 73.1 on BEAM10M, and 86.7 on LOCA256K. Its controlled BEAM10M ablations report 19.9 for lossily summarized history, a 7.3-point penalty without the persistent REPL, and a 1.8-point penalty without the eviction index. The report is therefore useful as design and empirical evidence for separating durable evidence from active context and making activation programmable, but not as proof that Scroll's fixed operation set is optimal or that its cross-system benchmark lead is controlled.

## Quotes

No source quotes have been retained yet.

## Connections Found

Scroll's primary role is a technical basis and empirical worked case for [preserving evidence without making history the next context](../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) and for the claim that [session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md). Its Event Log and payload handles retain addressable evidence, while model-written programs and explicit output projection determine what becomes active.

The paper also supplies end-to-end limitation evidence for distinguishing [access burden from transformation burden](../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) and evaluating [knowledge-access architecture beyond retrieval](../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md): its failure trajectories leave records reachable but miss them through bad query formulation or positional sampling. The lossy-history ablation is a bounded empirical case for why [an insufficient summary should precede rather than replace its source](../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md).

As a comparison source, Scroll broadens the operation vocabulary beyond [ACM's](./acm-agentic-context-management-for-long-horizon-tasks.ingest.md) fixed summarize/archive/query scheme and [Virtual Context's](../agent-memory-systems/reviews/virtual-context.md) proxy-selected layered retrieval. It shares [Fractal's](../agentic-systems/reviews/fractal.md) persistent Python and explicit projection pattern, then adds an event-sourced multi-session record and eviction landmarks. These are architecture-level paper comparisons, not code-grounded equivalence claims.

## Extractable Value

1. **Context-operation vocabulary is independent of retention policy** -- Systems can all retain raw history while offering a fixed summary/query pair, proxy-selected layers, or general model-written programs. Comparing the operations that make context policies expressible is a higher-reach design axis not yet isolated by the current KB notes. [deep-dive]

2. **Reachability does not guarantee successful activation** -- The appendix's failed preference and summarization trajectories had the needed records available, but query framing and positional sampling kept them out of the working view. This gives the KB concrete failure cases for separating storage, access, transformation, and exposure. [quick-win]

3. **Scroll learns or reasons only inside a fixed harness decomposition** -- Behavior can condition on typed event history, payloads, eviction landmarks, resident variables, and the namespace digest; it can compose search, expansion, SQL, Python transformations, permitted tools, and printing into expressive query-to-view mappings. Event schemas, lexical retrieval, sandbox capabilities, eviction and index rules, budgets, prompts, and evaluation partitions remain outside that effective update space, so model improvements do not validate those choices. [deep-dive]

4. **Keeping originals is specifically supported for exact-history tasks** -- Replacing original records with ingestion-time summaries is the most damaging BEAM10M ablation, especially for exact extraction, temporal reasoning, and updates. The result supports retained raw evidence in this benchmark regime; it does not compare every possible derived representation or hybrid store. [quick-win]

5. **Persistent computation helps when evidence must be composed** -- Removing the REPL while retaining ordinary search, expansion, and SQL tools costs 7.3 points overall, with larger differences on update and instruction-following categories and no reported difference on single lookups. A matched follow-up could separate namespace persistence, programmatic composition, and reduced serialization as candidate causes. [experiment]

6. **The eviction index is a targeted navigation aid** -- Removing it costs 1.8 points overall but more on scattered-evidence categories, which supports address-anchored landmarks over keyword search alone without showing that this roll-up algorithm is generally optimal. [just-a-reference]

## Limitations (our opinion)

The strongest headline comparison is not controlled. Table 2 selects each memory system's best public result under different backbones, reader models, retrieval budgets, and judges, and the authors explicitly do not reproduce those baselines. The within-harness LOCA and component comparisons are more informative, but the protocol generally evaluates each task once, reports no sampling uncertainty, and covers three benchmark families rather than deployed long-running work. Token counts do not establish latency, storage overhead, or dollar cost. The public implementation was not inspected or executed here, so the storage, sandbox, recoverability, and benchmark claims remain paper-only.

The fixed decomposition limits what the experiments establish. Under [the effective-update-space test](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), Scroll lets the model write broad programs over retained history, but the event representation, search substrate, capability surface, output boundary, index construction, and eviction policy are supplied rather than learned or compared as a set. The lossy-history ablation bears on replacing originals with its particular summaries; the no-REPL ablation bears on its persistent programmatic interface versus ordinary tool calls; and the no-index ablation bears on its index versus keyword search. Improvement within those contrasts does not establish that the surrounding decomposition is necessary, sufficient, or best.

Finally, the four appendix trajectories are selected explanatory cases, not causal experiments. They make query-formulation and sampling failures inspectable, but cannot estimate how often those mechanisms explain errors across tasks or whether a different model would fail for the same reasons.

## Recommended Next Action

Write a note tentatively titled **The context-operation alphabet constrains what a context policy can express**, using Scroll, ACM, and Virtual Context to separate retention guarantees from the operations available for locating, transforming, and exposing history while keeping Scroll's fixed-decomposition caveat explicit.
