---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Quicky Wiki workflow: a local document passes through extraction, graph admission, page assignment, summarization and CLI Markdown delivery."
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
---

# Quicky Wiki workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is a single local-file `qw ingest` invocation, from a user's document request to retained graph changes and generated wiki pages. It is selected because one shipped caller connects extraction, semantic comparison, mutation, page assignment, summarization and rendering; it does not require joining unrelated capabilities. It is a code-directed sequence of model computations, not an autonomous agent delegating to independently planning workers. The supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) establishes the route, while [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff) identifies its intermediate handoff object (SRC-1, `src/cli/ingest.ts`, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`).

Evidence is implementation and shipped prompt/design at the boundary's frozen commit. This member inspected the complete CLI ingestion, compiler ingestion, comparison, resolver and Markdown renderer implementations under SRC-1. These are within the existing source register, not additional sources. No execution trace, generated wiki, database or provider response was supplied or produced. Consequently, the following is implemented progression and failure handling, not a successful observed run or a reliability result. See [boundary](boundary.md#boundary-and-evidence).

### Request, extraction and semantic handoff

The user supplies a path and optional source type/quality. The CLI requires initialization, opens the store, loads project configuration, creates the model adapter and resolves the path before calling the compiler. Code owns every next step. The user chooses the source, not the individual claims subsequently admitted. Configuration can add entity-kind instructions to extraction; this is a preexisting instruction channel, not a learned worker policy ([RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup); SRC-1, `src/cli/ingest.ts`, `src/compiler/ingest.ts`).

The compiler reads and hashes complete file bytes, separates Markdown frontmatter from body, resolves title/kind/metadata and checks the registered path/hash. Identical bytes return an empty diff after synchronizing primary-page kind/metadata. For new or changed bytes, it writes the source registration/hash **before** extraction. Thus the registered hash denotes bytes encountered, not proof that all following stages completed. This ordering is important to recovery, below ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/compiler/ingest.ts`).

The host delegates extraction to the configured chat endpoint with a fresh system/user pair. The model receives source title, type, quality and body or one chunk, plus instructions for atomic claims, confidence, tags, concepts and dependencies. Bodies longer than 12,000 characters use sequential 8,000-character chunks with 500-character overlap. Code combines returned claims and deduplicates normalized 80-character statement prefixes. Only extracted arrays cross this call boundary; there is no retained conversation or sub-agent workspace. Confidence is quality-weighted before comparison. Model compliance and extraction completeness are unobserved ([RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/compiler/ingest.ts`).

Comparison receives all existing statements and the extracted statements, indexed separately. Its model proposes reinforcement, challenge or new admission, plus knowledge gaps. Code resolves indices into the in-process diff and computes confidence changes. With no existing claims it skips this model call and treats extracted claims as new. In the comparison branch, invalid referenced indices are skipped; an omitted match need not become a new claim. This is semantic model judgment, not verification against an expected answer or original independent evidence. There is no human per-claim veto between comparison and writes ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff); SRC-1, `src/compiler/diff.ts`).

### Admission, assignment and summary

The resolver consumes the diff in a fixed order: reinforce retained claims; challenge claims and invoke cascade; create concept pages; assign and insert new claims; link pages sharing the source; summarize touched or summary-less pages. Source/claim/page IDs are host store identities, whereas the models use transient indices and titles. The diff gains resolved IDs and returns to the caller; it is neither a durable approval record nor a transaction covering the invocation. Extracted dependency statements are not carried into dependency-edge construction on this path, so cascade invocation must not be read as evidence that this ingestion created a dependency graph ([RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/compiler/diff.ts`, `src/compiler/resolve.ts`).

Page assignment is another delegated model decision, not a review of factual truth. Batches contain at most eight new statements and all existing page titles; single-statement prompts have separate branches. The host accepts returned titles, creates missing pages and inserts claims with the current source ID. Missing or unparsable structured assignments fall back to the first existing page or `General`. The single-claim/no-existing-page branch instead consumes plain title text. These are availability-oriented routing defaults, not correctness gates (SRC-1, `src/compiler/resolve.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

Summarization supplies one page title and that page's statements/confidences to a fresh call. Up to three host workers drain a shared queue; these workers are code-level concurrency, not autonomous agents. A trimmed response longer than five characters can replace the stored summary. Failure is noncritical, and the CLI makes a further attempt for pages still lacking summaries. Neither the requested 30-word limit nor summary fidelity is independently checked. The graph holds the result for later readers; this establishes a retention path, not demonstrated influence or improved answers (SRC-1, `src/compiler/resolve.ts`, `src/cli/ingest.ts`; [RT-BAP-retained-context](runtime.md#rt-bap-retained-context)).

### What counts as delivered

There are two delivery boundaries. The compiler returns a resolved diff after mutation, summaries and primary-page entity synchronization. The CLI then prints the diff, attempts missing summaries, renders wiki pages and prints database totals. Its early `Ingested` message precedes rendering, so that message alone cannot establish completed file delivery (SRC-1, `src/compiler/ingest.ts`, `src/cli/ingest.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

For this CLI workflow, the final view is Markdown written to the configured wiki directory. Each nonempty page includes metadata, summary or placeholder, confidence-marked claims, related pages and source titles/quality. Empty pages are skipped; the renderer does not perform a truth check. File writes are sequential and are not atomic with graph admission (SRC-1, `src/render/markdown.ts`):

> const outPath = join(wikiDir, page.path);
> await mkdir(dirname(outPath), { recursive: true });
> await writeFile(outPath, content, "utf-8");
> return outPath;
> --- `src/render/markdown.ts`

The SQLite graph, not generated Markdown, is the later query input. A subsequent answer request is a separate invocation that reconstructs context from the graph, rather than resuming ingestion's messages. Library and dashboard callers can have different rendering tails, so the CLI's file-delivery boundary is not a universal compiler guarantee ([RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store), [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-client-access](runtime.md#rt-rte-client-access); SRC-1, `src/cli/ingest.ts`, `src/render/markdown.ts`).

### Failure, rejection and recovery responsibility

Two malformed-output paths have opposite admission consequences. Extraction's parse/mapping catch returns no claims and permits the remaining workflow to continue. Comparison's parse/processing catch instead appends extracted claims as new. Neither is a factual rejection decision, and provider call errors occur outside these parsing catches. Parseable output also receives no independent factual acceptance test. The closest supplied route records these policies and their minimum passages; this member does not relabel them as verification ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`).

The compiler has no encompassing rollback or retry coordinator. An extraction or later assignment request can throw after source/hash registration; a later stage can throw after earlier graph writes. Summary failure is swallowed, but rendering failure reaches the CLI's outer error handler after graph mutations and possibly some wiki-file writes. A directory invocation catches each file's exception and continues to the next file; that is batch continuation, not repair of the failed file. The operator owns any subsequent recovery outside these automatic fallbacks (SRC-1, `src/cli/ingest.ts`, `src/compiler/ingest.ts`, `src/compiler/resolve.ts`, `src/render/markdown.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

A consequential forcing case is an unchanged retry after a failed first attempt. Since source/hash admission happens first, the retry can take the identical-hash shortcut and never repeat failed extraction or resolution. The source therefore supports neither automatic recovery by rerunning the same file nor completion semantics for the stored hash. The compiler's implemented terminal progress label also cannot distinguish an empty extraction caused by parsing failure from a genuinely claim-free source (SRC-1, `src/compiler/ingest.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)). No observed failure/recovery trace establishes how an operator actually restored consistency.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow role: the selected end-to-end local-file CLI route. Host code delegates bounded text computations while retaining scheduling and effect authority. Semantic comparison, page assignment and summarization are distinct decisions, not successive independent factual approval gates. Compiler return, early CLI success text and final Markdown delivery are separate milestones. Recovery defaults preserve progression at the cost of silent omission or permissive admission; they do not constitute a retry/rollback protocol. These workflow conclusions remain implementation-grounded, with successful execution and operational recovery unobserved.
