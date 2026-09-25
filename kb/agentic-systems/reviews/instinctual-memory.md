---
type: kb/types/note.md
description: mem extracts sourced facts into Git and supplies host context, with separate
  publication, recall and withdrawal guarantees
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-instinctual-memory-01
source-identity: https://github.com/jasonkneen/instinctual-memory
reviewed-revision: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-instinctual-memory-01/result.md
analysis-result-sha256: 44ec3f5e0c84862f61ae28a54d4ca90bc1cb17ab671314da4ca1ddf8898723df
---

# mem: sourced facts and host context

mem is a Rust memory artifact that imports agent conversations and other records, derives lasting facts, publishes them on a Git memory branch, and supplies later context through explicit recall, hooks and generated project files. This review covers the complete artifact at the pinned commit, with the external agent loop, model internals and deployed stores excluded. Findings are code-grounded; no model, benchmark, erasure or host task was executed.

Raw journal records and curated facts remain separate. Rules or an optional LLM transform eligible source events into statements with provenance. Explicit caller changes have their own route. Publication validates structure and references, then uses Git compare-and-swap to reject a stale base. This is a bounded admission guarantee: an earlier operation-level receipt shortcut, task files and erasure phases have distinct semantics. [Publication source](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/repo.rs#L196-L329).

The extraction checks establish quoted-text occurrence and model-reported durability, not entailment or truth. The rules preference pattern omits the matched positive/negative operator from its resulting statement, although it retains the full match as evidence. Deduplication also drops several polarity words before measuring overlap. These are static transformation limits, not measured failure rates. Positional checkpoint advancement and old-file retirement likewise require care: a scoped pass can advance beyond excluded events, and retiring an old file version does not guarantee replacement facts were admitted. [Extraction source](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/consolidate.rs#L100-L476).

Automatic hooks select general preferences by identity and prompt-related facts by lexical overlap. Requested retrieval can instead rank facts and raw records with JEV or a local cross-encoder. Managed writeback supplies a retained project-file block for named external agents to load; actual loading priority and behavioral influence remain uninspected. Model names and cached assets do not establish fixed provider weights. [Hook source](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/hook.rs#L39-L212).

Withdrawal differs across these consumers. Suppressing a curated fact does not itself prevent raw transcript recall. Writeback has a different eligibility filter and an already-written block persists until rewritten. Erasure marks deletion Completed before later physical cleanup phases; interruption can leave a narrower recovery path than the status suggests. Its loop does not establish deletion of external source files, generated instruction files or all backups. [Read paths](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/ops.rs#L245-L332), [writeback](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/cli.rs#L1725-L1878), [erasure](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/erasure.rs#L52-L162).

The strongest supported contribution is reusable trace-derived knowledge with explicit admission, provenance and consumer routes. This satisfies the analysis's bounded trace-learning criterion; it does not establish conjectural learning or improved host capacity. Progress/control state supports narrow reflection on processing state. Self-improvement and faithful downstream use remain uninspected: the evaluation command scores retrieval against caller-provided IDs and text conditions, without a retained host dependence experiment.

The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-instinctual-memory-01/result.md) retains the canonical records, quotes, full memory comparison and epistemic assessment. Candidate-linked source audits, host recall interventions and fault/concurrency traces would change these limits.
