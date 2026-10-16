---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Sage-wiki workflow account: standard tier-3 source compilation through model handoffs, article publication, quality retry and resumable interruption."
run-id: AAS-2026-10-15-sage-wiki-cc43456fb833-01
reviewed-boundary: d3ef3a1346405c82eac01b4d7c493c94c1c59169
---

# Sage-wiki workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a caller-requested, standard tier-3 compile of new or changed source documents into retained wiki articles. It is selected because the shipped pipeline connects multiple model-dependent stages to persistent delivery and includes both rejection and recovery branches. It is not a reconstructed autonomous-agent conversation: Go code owns progression, while independent completions propose content. The canonical route is [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources); its configuration, prompt and queue inputs are [RT-OBJ-config](runtime.md#rt-obj-config), [RT-OBJ-prompts](runtime.md#rt-obj-prompts) and [RT-OBJ-compile-items](runtime.md#rt-obj-compile-items).

This account concerns implementation at the frozen boundary, not an observed execution. No target commands, tests or providers were run. Additional SRC-1 implementation inspection covers `internal/compiler/concepts.go`, `internal/compiler/confidence.go` and `internal/compiler/summarize.go`, plus selected ranges of `internal/compiler/fullpipeline.go`, `internal/compiler/write.go`, `internal/compiler/evidence_gate.go` and `internal/compiler/pipeline.go`. Comments quoted below describe contracts whose inspected branches are distinguished from successful operation. Batch submission, on-demand compilation and background workers are alternate routes retained in the runtime report, not assumed equivalent to this selected standard path.

### Request, scheduling and summarization

A CLI or embedded compile request supplies workspace/options; code loads configuration, prompts and manifest, computes changed work and selects tiers. Sources assigned tier 3 enter the full pipeline under queue claims. This entry and lease protocol are supplied by [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources) and [RT-OBJ-compile-items](runtime.md#rt-obj-compile-items). The caller need not be human, and initiation is not per-article approval.

The first handoff supplies source identities, configured model/token/concurrency settings and the prompt registry to summarization. For a normal single-chunk text source, extraction produces text and the provider receives summary guidance plus wrapped source text. Large inputs take chunk summarization followed by hierarchical synthesis. A reusable on-disk summary can bypass another model call when its body is at least 100 bytes and its retained source hash matches. The output is summary prose and a path, not a delegated agent's continuing context. Code persists successful summaries and attempts indexing/embedding before advancing. SRC-1: `internal/compiler/summarize.go`, `internal/compiler/fullpipeline.go`.

> if len(body) >= 100 && storedHash != "" && storedHash == info.Hash {
> --- `internal/compiler/summarize.go`

Cancelled or timed-out source work is not promoted to a successful summary by the full pipeline. Other summary errors increment error accounting. If no summaries survive, later extraction/writing does not proceed. These are local control decisions, not evidence of source understanding or correct compression. SRC-1: `internal/compiler/fullpipeline.go`.

### Summaries to concepts to article inputs

Concept extraction receives successful summaries and a sorted snapshot of existing concept names. The batch builder truncates each summary to 1,000 bytes before constructing the extraction prompt. Thus a generated full summary is not necessarily wholly visible to the extraction model. Independent batches share the existing-name snapshot rather than each other's evolving results. Code requests structured JSON, decodes concepts, combines results and filters/deduplicates candidates. Partial batch failure retains surviving concepts with an error; total extraction failure ends this pipeline invocation. SRC-1: `internal/compiler/concepts.go`, `internal/compiler/fullpipeline.go`.

> if len(summary) > 1000 {
> summary = summary[:1000] + "\n..."
> }
> --- `internal/compiler/concepts.go`

Before article generation, the full pipeline can merge embedding-similar concepts into existing manifest entries. Its source-count gate then suppresses candidates below the configured minimum; a nonpositive minimum disables that gate. This checks declared source-list length, not the truth or independence of source evidence. Optional model curation follows this seam; its failure is advisory and compilation proceeds uncurated. Selected concepts enter the manifest and become article-writing tasks. SRC-1: `internal/compiler/evidence_gate.go`, `internal/compiler/fullpipeline.go`.

> if len(c.Sources) >= minSources {
> kept = append(kept, c)
> } else {
> skipped = append(skipped, c)
> }
> --- `internal/compiler/evidence_gate.go`

The article handoff does not simply pass the extraction transcript forward. Code rereads source files, selects sections using concept names/aliases, falls back to the first section when none match, and truncates included text parts to 4,000 bytes. It ranks parts and accumulates them against an estimated token budget, always retaining the first part even if over budget. It also reads an existing article, if present, and supplies related concepts and metadata to the write template. Source files remain outside the completion and reachable through later reads; omitted content is not restored automatically within this call. SRC-1: `internal/compiler/write.go`.

This resembles isolated task frames only in the limited sense that each completion receives selected inputs and returns content. There is no inspected sub-agent delegation or shared agent transcript here. Persistent summaries, files and manifest state escape these calls and may be reselected later; provider-private context remains outside the source boundary. The model-component limits are in [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client).

### Preparation, publication and verification

Article preparation runs concurrently under configured backpressure or a semaphore. It performs completion and pure postprocessing, including rejecting empty content, stripping generated frontmatter, normalizing wikilinks and constructing code-owned metadata. The write request asks for comprehensive, precise wiki prose; it does not give the provider tool-selection authority. Once preparations finish, code applies their effects sequentially in input order. SRC-1: `internal/compiler/write.go`.

> // applyArticlePayload performs every store mutation and the file write for
> // one prepared article. Called sequentially in input order from WriteArticles
> --- `internal/compiler/write.go`

Application atomically writes the article file before index/ontology updates; the manifest save occurs later. File-write failure fails that article, but store-mutation failures can log and continue. Consequently an article result is not proof that every derived retrieval or graph artifact exists. The runtime's retained passage and persistence limits in [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources) also apply. SRC-1: `internal/compiler/write.go`.

Verification after writing is conditional: an item store must be supplied and the article must be readable. Code calculates a weighted score for format, source-phrase overlap, relative article length, known-concept wikilink resolution and filler avoidance. It does not consult an expected correct answer. These are software heuristics, not human review or a factual-answer oracle. SRC-1: `internal/compiler/confidence.go`, `internal/compiler/fullpipeline.go`.

> Grounding   float64 // fraction of source key phrases present in the article
> Coverage    float64 // article length adequacy vs. source size
> --- `internal/compiler/confidence.go`

### Failure, recovery and delivered result

A sub-threshold score can trigger one fresh rewrite when quality retry is enabled. Code, not the writer model, selects that action. The caller removes the article first so the next preparation cannot seed itself with the rejected text. The retry receives the concept's name, aliases and sources with ordinary writing options; this branch does not pass a detailed critique or score breakdown into the rewrite. A successful retry is rescored. A still-low article remains published with an error counted rather than undergoing an indefinite correction loop. SRC-1: `internal/compiler/fullpipeline.go`, `internal/compiler/write.go`; the shipped keep-and-count policy is quoted in [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources).

Removal failure keeps the original. Rewrite failure after successful removal can leave the article absent, even though its previous indexing effects were not transactionally rolled back. The branch increments errors and skips final score persistence for that failed rewrite. Thus recovery owns a bounded second attempt, not restoration of the prior article. SRC-1: `internal/compiler/fullpipeline.go`.

> // the original file is gone; the failed retry is an error
> result.Errors++
> belowThreshold++
> continue
> --- `internal/compiler/fullpipeline.go`

Interrupted or totally failed extraction has a different recovery path. The full pipeline withholds its pass-completed flag; the caller avoids advancing pass checkpoints and skips manifest save. A later compile can rediscover work, and matching persisted summaries can be reused. Already-written files and database effects are not undone. Conversely, reaching the end sets completion even when individual article errors occurred; for successfully summarized sources the caller can advance all three pass flags. Completion must therefore not be read as a guarantee that every article succeeded or that a failed quality rewrite will automatically be repaired next time. SRC-1: `internal/compiler/fullpipeline.go`, `internal/compiler/pipeline.go`.

Delivery on this route means retained summary/article files, attempted derived indexes and graph updates, a completed-run manifest merge, and returned compile counts/errors/cost metadata. Finalization can itself fail at manifest merge; diagnostic/changelog failures can be advisory. It is possible to return a compile result with content errors, and low quality is not a universal publication veto. SRC-1: `internal/compiler/pipeline.go`.

> } else if err := manifest.MergeSave(orBackground(run.opts.Ctx), run.mfPath, run.base, run.mf); err != nil {
> return nil, fmt.Errorf("compile: save manifest: %w", err)
> }
> --- `internal/compiler/pipeline.go`

Later use is a separate consumer boundary: [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki) can return retained content, and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) can select it for answer synthesis. Compilation does not establish that a later question retrieves a particular article or that a host acts on it. Its article publication is also distinct from the answer-output trust route [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); that route is not a mandatory human approval stage for compiled concepts.

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

#### On [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

Workflow-specific progression: the selected standard tier-3 path delegates summarization, batched concept extraction and article preparation to independent completions; Go owns the transitions, source-count suppression, publication and optional single quality rewrite. Preparation can run in parallel, while article application is sequential. Quality scoring follows file publication rather than guarding every write. Checkpoint completion and per-article success are separate: end-of-pass completion can coexist with errors, including a failed rewrite whose original file has already been removed. The workflow account above supplies the selected-path handoffs, delivery contract and evidence limits without declaring a second identity for this route.
