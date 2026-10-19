---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Supermemory epistemic routes: public context transformations and withdrawal controls, with inferred-fact review and graph maintenance bounded by an opaque engine."
run-id: AAS-2026-10-19-supermemory-1cc18c778c48-01
reviewed-boundary: f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe
---

# Supermemory epistemic report

## Source-and-claim boundary

The question is what licenses reliance on submitted, inferred and retrieved content, and what results can change later behavior. The [boundary and Source register](boundary.md#source-register) establish SRC-1: the public artifact is complete, but the product loop is partial. The non-public extraction, embedding, graph, ranking and maintenance engine prevents an implementation-grounded account of its truth checks. Provider weights and their updates are also inaccessible; see [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-local-embeddings](runtime.md#rt-cmp-local-embeddings) and [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model). No observed run or causal experiment is registered. Source deductions below are implementation evidence, not target executions.

The consequential warrant claims are [EPI-CLM-graph-truth](#epi-clm-graph-truth), [EPI-CLM-review-facts](#epi-clm-review-facts), [EPI-CLM-benchmark-judge](#epi-clm-benchmark-judge) and the engine boundary in [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary). The review endpoints are a material alternative omitted from the provisional runtime account, not a correction to its selected middleware trace. They defeat an unqualified claim that the product declares no confirmation or rejection route. Their existence in documentation does not establish a working human gate on every read or write.

| Entry point or operation | Source path, SRC-1 | Coverage and evidence basis | Remaining limit |
|---|---|---|---|
| Automatic Vercel and OpenAI context/save | `packages/tools/src/vercel/index.ts`; `packages/tools/src/openai/middleware.ts`; `packages/tools/src/conversations-client.ts`; `packages/tools/src/vercel/middleware.ts` | Supplied [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call), [RT-RTE-openai-call](runtime.md#rt-rte-openai-call); direct reads of OpenAI preparation, Vercel conversion and conversation serialization | Provider compliance and remote admission unobserved; OpenAI prepared context is not the Vercel LRU |
| Shared retrieval, deduplication and prompt construction | `packages/tools/src/shared/memory-client.ts`; `packages/tools/src/tools-shared.ts`; `packages/tools/src/shared/prompt-builder.ts`; `packages/tools/src/shared/memory-context.ts` | Direct implementation reads; [EPI-RTE-memory-format](#epi-rte-memory-format) | Custom templates can differ; no universal semantic preservation guarantee |
| MCP dispatch, save form and search | `apps/mcp/src/server/tools/index.ts`; `apps/mcp/src/server/tools/guided-save.ts`; `apps/mcp/src/server/tools/search-memory.ts`; `apps/mcp/src/server/client/index.ts` | Direct registry, form and search reads; client mapping section; [EPI-RTE-search-projection](#epi-rte-search-projection). Supplied [RT-RTE-mcp-save](runtime.md#rt-rte-mcp-save) | Form affords review, not mandatory approval; graph/list/profile/document handlers not independently audited here |
| MCP forget, context and upload | `apps/mcp/src/server/tools/forget-memory.ts`; `apps/mcp/src/server/prompts/context.ts`; `apps/mcp/src/server/space-state.ts` | Supplied [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget), [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context), [RT-RTE-upload-session](runtime.md#rt-rte-upload-session) | Backend withdrawal and host-history eviction unverified |
| Framework tools, deletion and forget helpers | `packages/tools/src/ai-sdk.ts`; `packages/tools/src/tools-shared.ts` | Supplied [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop); direct helper read; [EPI-RTE-mutation-checks](#epi-rte-mutation-checks) | Request checks are not content-truth checks |
| Claude memory command dispatch and all file operations | `packages/tools/src/claude-memory.ts` | Direct complete implementation read; [EPI-RTE-claude-files](#epi-rte-claude-files) | Remote replacement, concurrent writes and rename atomicity unverified |
| Inference review queue/actions | `apps/docs/recall/memory-review.mdx`; `packages/lib/api.ts` | Direct documentation and schema-section reads; [EPI-RTE-inference-review](#epi-rte-inference-review) | No inspected endpoint implementation or exercised review |
| Extraction, derives, updates and forgetting | `apps/docs/concepts/graph-memory.mdx` | Direct doctrine read; [EPI-RTE-graph-dreaming](#epi-rte-graph-dreaming) | Non-public engine prevents implementation judgment |
| Agent Framework lifecycle, LiveKit and release gate | `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py`; `packages/livekit-sdk-python/src/supermemory_livekit/agent.py`; `.github/workflows/publish-tools.yml` | Supplied [RT-RTE-python-context](runtime.md#rt-rte-python-context), [RT-RTE-publish-tools](runtime.md#rt-rte-publish-tools) | Other Python, Mastra and Voltagent internals uninspected; no adapter-wide negative |
| Benchmark evaluator | `apps/docs/memorybench/memscore.mdx` | Direct doctrine read; [EPI-CLM-benchmark-judge](#epi-clm-benchmark-judge) | External benchmark implementation, runs and comparisons unavailable |
| Other shipped relevant paths | `packages/memory-graph/`; `apps/memory-graph-playground/`; `apps/docs/connectors/overview.mdx`; `skills/supermemory/SKILL.md` | Available but not independently traced here beyond supplied boundary coverage | No system-complete negative about evaluation, lineage or maintenance; visualization and connector behavior not assessed |

## Epistemic-object inventory

Fields owned by records are referenced rather than restated.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-facts](#epi-obj-memory-facts) | Personal facts, preferences and inferred propositions | see record | SRC-1, `apps/docs/concepts/graph-memory.mdx` | Actual provenance and warrant unknown |
| [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache) | Formatted retrieved assertions | see record | SRC-1, `packages/tools/src/shared/cache.ts` | Vercel-local retention is not acceptance |
| [EPI-OBJ-openai-context](#epi-obj-openai-context) | Prepared retrieved assertions | see record | SRC-1, `packages/tools/src/openai/middleware.ts` | Transient preparation, not a retained-cache path |
| [MEM-OBJ-document-content](memory.md#mem-obj-document-content) | Submitted conversation assertions | see record | SRC-1, `packages/tools/src/conversations-client.ts` | Raw input, not derived graph facts |
| [EPI-OBJ-search-results](#epi-obj-search-results) | Selected assertions or document chunks | see record | SRC-1, `apps/mcp/src/server/tools/search-memory.ts` | Inference distinction lost on this search path |
| [EPI-OBJ-claude-files](#epi-obj-claude-files) | Arbitrary file text; truth-aptness not determinable without an instance | see record | SRC-1, `packages/tools/src/claude-memory.ts` | File mutations can change claims without assessing them |
| [RT-OBJ-space-state](runtime.md#rt-obj-space-state) | None: routing/capability state | see record | SRC-1, `apps/mcp/src/server/space-state.ts` | Operational scope selection, not warrant |

## Authority-route ledger

The architectural status assesses each route, separately from operation evidence. Every implementation route below remains unobserved. References in cells delegate the detailed field to its declaring record.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call) | content transformation | implemented | [MEM-OBJ-document-content](memory.md#mem-obj-document-content) | truth-apt transformation: acquisition/import | Serialized conversation enters document-ingestion interface | see route | see route | see route | API submission request | Imported conversation assertions; source warrant unknown | Save eligible text, including generated text | see route | SRC-1, `packages/tools/src/conversations-client.ts` | none | none | Conversion omits system text and selected payloads; acquisition does not classify remote document-to-fact derivation |
| [RT-RTE-openai-call](runtime.md#rt-rte-openai-call) | operational admission/selection/consumption | implemented | [EPI-OBJ-openai-context](#epi-obj-openai-context) | no content change | Prepared context delivered in Chat messages or Responses instructions | see route | see route | see route | Model-input preparation | No new factual warrant | see route | see [RT-BAP-memory-context](runtime.md#rt-bap-memory-context) | SRC-1, `packages/tools/src/openai/middleware.ts` | none | none | Fail-open continuation is not endorsement; no Vercel LRU association |
| [EPI-RTE-memory-format](#epi-rte-memory-format) | content transformation | implemented | [EPI-OBJ-memory-facts](#epi-obj-memory-facts) | truth-apt transformation: non-ampliative reshaping | Default textual projection | see route | see route | see route | Formatting/selection | No truth license; epistemic annotations can be lost | see route | see route | SRC-1, `packages/tools/src/shared/memory-client.ts` | none | none | Arbitrary custom template relation indeterminate |
| [EPI-RTE-search-projection](#epi-rte-search-projection) | operational admission/selection/consumption | implemented | [EPI-OBJ-search-results](#epi-obj-search-results) | truth-apt transformation: non-ampliative reshaping | API results to tool output | see route | see route | see route | Tool-result delivery | Similarity is not confidence in truth | see route | see route | SRC-1, `apps/mcp/src/server/tools/search-memory.ts` | [EPI-CLM-review-facts](#epi-clm-review-facts) | qualification | Search output does not expose inferred status |
| [EPI-RTE-mutation-checks](#epi-rte-mutation-checks) | check/evidence production | implemented | [EPI-OBJ-memory-facts](#epi-obj-memory-facts) | no content change | Mutation target/status and response count | see route | see route | see route | Protocol gates | Equality/status/count only | see route | see route | SRC-1, `packages/tools/src/tools-shared.ts` | none | none | Cannot establish truth or remote deletion correctness |
| [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget) | disposition/acceptance | implemented | [EPI-OBJ-memory-facts](#epi-obj-memory-facts) | no content change | Withdrawal selection, not factual acceptance | see route | see route | see route | Dispatch or return candidates | No falsehood judgment follows from forget | see route | see route | SRC-1, `apps/mcp/src/server/tools/forget-memory.ts` | none | none | No mandatory human gate or local cache eviction |
| [EPI-RTE-claude-files](#epi-rte-claude-files) | retention | implemented | [EPI-OBJ-claude-files](#epi-obj-claude-files) | truth-apt transformation: indeterminate | Caller-selected text changes | see route | see route | see route | Remote write/read requests | No acceptance criterion | see route | see route | SRC-1, `packages/tools/src/claude-memory.ts` | none | none | Instances may instead be non-truth-apt instructions |
| [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call) | retention | implemented | [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache) | no content change | Continuation cache | see route | see route | see route | Cache reuse | Neither freshness nor endorsement | see route | see route | SRC-1, `packages/tools/src/shared/cache.ts` | none | none | No backend-mutation invalidation |
| [EPI-RTE-graph-dreaming](#epi-rte-graph-dreaming) | content transformation | doctrine only | [EPI-OBJ-memory-facts](#epi-obj-memory-facts) | truth-apt transformation: ampliative conjecture | Derives example | see route | see route | see route | No inspected engine force | Candidate inference, not verified consequence | see route | see route | SRC-1, `apps/docs/concepts/graph-memory.mdx` | [EPI-CLM-graph-truth](#epi-clm-graph-truth) | implementation unknown | Classification is of documented example, not all extraction |
| [EPI-RTE-inference-review](#epi-rte-inference-review) | disposition/acceptance | doctrine only | [EPI-OBJ-memory-facts](#epi-obj-memory-facts) | no content change | Confirm/decline/undo one inferred fact | see route | see route | see route | Declared status/search changes; no inspected enforcement | Confirmation label without supplied evidence criterion | see route | see route | SRC-1, `apps/docs/recall/memory-review.mdx` | [EPI-CLM-review-facts](#epi-clm-review-facts) | acceptance limit | No evidence-consuming acceptance or lifecycle integration established |
| [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context) | operational admission/selection/consumption | implemented | [RT-OBJ-space-state](runtime.md#rt-obj-space-state) | no content change | Namespace and fact selection | see route | see route | see route | Routing and bounded prompt construction | Namespace access is not factual warrant | see route | see [RT-BAP-space-selection](runtime.md#rt-bap-space-selection), [RT-BAP-memory-context](runtime.md#rt-bap-memory-context) | SRC-1, `apps/mcp/src/server/prompts/context.ts` | none | none | Host placement and compliance unknown |
| [RT-RTE-upload-session](runtime.md#rt-rte-upload-session) | disposition/acceptance | implemented | [RT-OBJ-space-state](runtime.md#rt-obj-space-state) | no content change | Upload capability admission | see route | see route | see route | Request authorization | No content-quality license | see route | see route | SRC-1, `apps/mcp/src/server/space-state.ts` | none | none | Single consumption not exactly-once ingestion |
| [RT-RTE-publish-tools](runtime.md#rt-rte-publish-tools) | disposition/acceptance | implemented | none | non-truth-apt policy/content update: package publication | Version/build/compatibility gate | see route | see route | see route | Ordered CI publication gate | Compatibility only, not knowledge truth | see route | see route | SRC-1, `.github/workflows/publish-tools.yml` | none | none | No executed CI evidence |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-graph-truth](#epi-clm-graph-truth) | see record | SRC-1, `apps/docs/concepts/graph-memory.mdx`; doctrine/design | see record | No inspected engine route; [EPI-RTE-graph-dreaming](#epi-rte-graph-dreaming) is doctrine only | none supplied | No comparison or engine execution | Declared extraction and conjecture; correctness unknown | “Stays true” exceeds public implementation evidence |
| [EPI-CLM-review-facts](#epi-clm-review-facts) | see record | SRC-1, `apps/docs/recall/memory-review.mdx`; doctrine/design | see record | Schema support, not endpoint enforcement; [EPI-RTE-search-projection](#epi-rte-search-projection) shows a consumer | none supplied | Review procedure and factual evidence unknown | Declared reversible disposition; not demonstrated acceptance | Unreviewed suggestions already searchable; inference marker not carried on this MCP search path |
| [EPI-CLM-benchmark-judge](#epi-clm-benchmark-judge) | see record | SRC-1, `apps/docs/memorybench/memscore.mdx`; doctrine/design | see record | none inspected in registered artifact | none supplied | External implementation/run; judge choice, prompts and excluded failures limit interpretation | A described answer evaluator, not a live graph-admission oracle | No supported component-effect or general truth guarantee |
| [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary) | see record | SRC-1, `apps/docs/self-hosting/overview.mdx`; doctrine/design | see record | Public routes delegate remotely | none supplied | No engine code | Partial loop remains the right boundary | Implementation questions remain open, not negative findings |

## Bounded conclusion

**Public routes acquire and reuse assertions without establishing their truth.** Automatic conversation submission can feed user and generated assistant text into later remote profile/search results; source warrant is unknown. See [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call), [RT-RTE-openai-call](runtime.md#rt-rte-openai-call) and [RT-RTE-python-context](runtime.md#rt-rte-python-context). The acquired input is document content, not already-derived graph assertions; see [MEM-OBJ-document-content](memory.md#mem-obj-document-content). The intervening document-to-fact processing is separately declared in [MEM-RTE-engine-dreaming](memory.md#mem-rte-engine-dreaming), not established by submission code. Vercel cache retention and OpenAI transient preparation are separate paths; see [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache) and [EPI-OBJ-openai-context](#epi-obj-openai-context). Neither retention nor repeated delivery licenses acceptance. The backend extraction relation remains indeterminate; no inspected route establishes an entailed new factual proposition from warranted premises.

**The default text consumers can weaken epistemic distinctions.** [EPI-RTE-memory-format](#epi-rte-memory-format) drops metadata and merges normalized variants. [EPI-RTE-search-projection](#epi-rte-search-projection) drops inference status, although the client separately preserves it for memory-list entries. Similarity and profile categories govern supply, not a truth decision. These are consumer-specific findings, not claims that the API never offers lineage. Model-facing text is advisory/interpretive through [RT-BAP-memory-context](runtime.md#rt-bap-memory-context); code enforces replacement of owned blocks, not compliance with their content.

**Conjecture and review are declared, but acceptance is not demonstrated.** The specific graph example is ampliative because the stated premises also fit work on another product; see [EPI-RTE-graph-dreaming](#epi-rte-graph-dreaming). Review declares confirmation, rejection and undo and directly affects future search, yet supplies no required evidence criterion, intended-use test or inspectable implementation. No accepted ampliative claim or post-acceptance lifecycle integration is established by [EPI-RTE-inference-review](#epi-rte-inference-review). Unreviewed content may have operational use first. This does not establish that server checks are absent.

**Withdrawal and editing have narrower, real protocol targets.** Equality/status/count checks in [EPI-RTE-mutation-checks](#epi-rte-mutation-checks) and candidate gating in [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget) constrain requests, not factual warrant. Remote forgetting does not evict already injected prompts or local caches. [EPI-RTE-claude-files](#epi-rte-claude-files) provides inspectable text revision and later exact-file reads without content-quality judgment; rename is write-then-delete, not an atomic epistemic revision. Guided save affords human editing, but direct add remains available.

**Evaluation does not transfer beyond its target.** The documented external benchmark judge checks answers against reference answers; it does not establish extraction correctness, graph mechanism, replay safety or component effect. The release workflow gates publication, not memory truth. Neither supplies observed benefit here. Retained trace-fed content can reach later behavior, but that alone does not establish improved capacity, reflection, autonomous theory-building or exercised self-improvement. These properties remain separately unestablished, not bundled into a system-wide verdict. Available uninspected adapters, graph consumers and connector paths also prevent a system-complete negative.

## Shared records

### Operative objects

#### EPI-OBJ-openai-context
Label: OpenAI prepared memory context

Part of: [RT-RTE-openai-call](runtime.md#rt-rte-openai-call)

This object is the transient context payload within the supplied route, not another route. Identity: retrieved/formatted memories inserted into Chat messages or Responses instructions during request preparation. Form: natural-language assertions inside symbolic message/instruction fields and owned delimiters. Substrate: in-process request values, then external provider input; host history retention is uninspected. Distinct from [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache), the Vercel-only LRU: the OpenAI preparation retrieves/formats and forwards request values, without that cache. SRC-1 implementation, `packages/tools/src/openai/middleware.ts`. Its provider consumer and interpretive force are described in [RT-BAP-memory-context](runtime.md#rt-bap-memory-context); no factual acceptance follows. No-text branches skip search and caught retrieval failures clear owned context rather than proving current memories were delivered.

> enhancedInstructions = replaceMemoryContext(
> params.instructions || "",
> typeof memories === "string" ? memories : "",
> )
> --- `packages/tools/src/openai/middleware.ts`

> messages: enhancedMessages,
> --- `packages/tools/src/openai/middleware.ts`

#### EPI-OBJ-memory-facts
Label: Graph memories and profile facts

Identity: remote graph facts and API profile/search assertions, including inferred facts. Form: natural-language assertions with symbolic IDs, inference/review/latest/forgotten flags and relationships; backend graph storage uninspected. These are remote contents, distinct from the local formatted-string container [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache); no supplied record names this remote factual population. Source lineage is declared but actual claim-to-evidence links and extraction fidelity remain unknown. SRC-1, `apps/docs/concepts/graph-memory.mdx`, `apps/docs/recall/memory-review.mdx`.

> | **What** | Raw input you send | Facts Supermemory extracts |
> --- `apps/docs/concepts/graph-memory.mdx`

#### EPI-OBJ-search-results
Label: MCP matching memories

Identity: `search_memory` result projection: natural-language memory/chunk text with symbolic IDs, document ID when present, similarity, totals and timing; transient tool response, potentially retained by external host history. Distinct from [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache): different producer, output and consumer, no wrapper-local LRU. SRC-1, `apps/mcp/src/server/tools/search-memory.ts`, `apps/mcp/src/server/client/index.ts`. The latter's `mapMemoryEntry` preserves `isInference` on the memory-list path, counterevidence to any API-wide claim of marker removal.

> const results = searchResult.results.map((result) => ({
> id: result.id,
> text: getMemoryText(result),
> similarity: result.similarity,
> ...(result.documentId && { documentId: result.documentId }),
> }))
> --- `apps/mcp/src/server/tools/search-memory.ts`

#### EPI-OBJ-claude-files
Label: Claude memory file documents

Identity: namespace-scoped remote documents with `source: claude-memory`, file paths and reversible IDs. Text is natural-language or arbitrary caller content, with symbolic path/metadata; storage is remote service, not a local filesystem. No counterpart in supplied objects: [RT-OBJ-space-state](runtime.md#rt-obj-space-state) is namespace/capability routing state, not these documents. SRC-1, `packages/tools/src/claude-memory.ts`.

> interface ClaudeFileDocument {
> documentId: string
> content: string
> metadata: ClaudeFileMetadata
> }
> --- `packages/tools/src/claude-memory.ts`

### Routes

#### EPI-RTE-memory-format
Label: Default memory text formatting

Part of: [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call)

This is the shared-helper content-transformation stage of that call, not a replacement for its invocation/persistence account. Code fetches profile/search, extracts strings, deduplicates by normalized text with static-before-dynamic-before-search precedence, then passes Markdown strings and selected raw results to a template. The default template uses only the strings. SRC-1 implementation: `packages/tools/src/tools-shared.ts`, `packages/tools/src/shared/memory-client.ts`, `packages/tools/src/shared/prompt-builder.ts`, `packages/tools/src/shared/memory-context.ts`.

Concrete source deduction, not execution: in full mode static `Alex works at Stripe` and search `[2026-10-19] Alex works at Stripe` have the same normalization key; the static string survives and the dated search result is omitted. The default result contains `## Static Profile` and the surviving bullet, without the search entry's date or metadata. This is non-ampliative textual selection, but not guaranteed preservation of temporal scope or warrant. In query mode the profile is excluded before deduplication, so the search result survives: counterexample to an unconditional profile-precedence claim. A custom template can consume raw result metadata or produce arbitrary text; its semantic relation is indeterminate without its implementation.

- Immediate return: Formatted memory string, or empty string.
- Later read-back: Wrapper can cache the string for a continuation; see parent route for cache policy.
- Delegated visibility: Default model context gets fact strings, not original result metadata, review flags or a proof.
- Selection predicate: Mode, nonempty memory/chunk, normalized text uniqueness and source priority; no truth evaluator or answer oracle.
- Invalidation or expiry: Owned marked blocks replaced on later preparation; cache invalidation is parent-owned, not remote fact revision tracking.
- Activation or effect: Code determines supplied context; downstream model reliance unobserved.
- Evidence limits: No execution; custom templates and remote semantic fidelity uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .replace(/^\[recent\]\s*/i, "")
> .replace(/^\[\d{4}-\d{2}-\d{2}\]\s*/, "")
> --- `packages/tools/src/tools-shared.ts`

> return `User Supermemories: \n${data.userMemories}\n${data.generalSearchMemories}`.trim()
> --- `packages/tools/src/shared/prompt-builder.ts`

#### EPI-RTE-search-projection
Label: MCP search result projection

Distinct from supplied routes: [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop) is the framework executor; [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context) is the MCP profile prompt, not this registered search operation. SRC-1 implementation: `apps/mcp/src/server/client/index.ts` mapping section and `apps/mcp/src/server/tools/search-memory.ts`. Backend results become text/chunks, IDs, similarity and optional source-document ID. Neither projection checks truth nor carries inference status. Document IDs preserve a possible lookup path but not a demonstrated warrant chain.

- Immediate return: Text and structured matching memories, totals and timing, or tool error.
- Later read-back: uninspected — host can retain tool history; this handler makes no durable write.
- Delegated visibility: MCP caller receives projected text/IDs/similarity, not inferred/review status.
- Selection predicate: Caller query and resolved namespace; remote search plus client projection, no truth oracle.
- Invalidation or expiry: inapplicable — transient output; no local eviction of previous host messages.
- Activation or effect: Supplies tool context, advisory to host/model; model use unobserved.
- Evidence limits: No service execution; other routes such as memory listing preserve more metadata.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const similarity = (result.similarity * 100).toFixed(0)
> --- `apps/mcp/src/server/tools/search-memory.ts`

The load-bearing output-field passage is in [EPI-OBJ-search-results](#epi-obj-search-results).

#### EPI-RTE-mutation-checks
Label: Framework mutation target checks

Part of: [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop)

This record owns the inspected shared-helper check stage, not the model's disposition or the remote mutation implementation. In open requests the caller/model proposes a document ID or memory ID/content; code may veto, and the service may reject. `deleteDocument` fetches the document, rejects a known nonterminal status, requests deletion and checks count one. Missing status is not rejected by that predicate. `forgetMemory` with content requests a dry-run semantic preview and selects normalized exact matches; direct ID bypasses preview. Post-request nonzero count is treated as success. The MCP forget handler has a different exact-text rule; see [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget). SRC-1 implementation, `packages/tools/src/tools-shared.ts`.

- Immediate return: Count/void on checked protocol success, otherwise error.
- Later read-back: Service mutation can affect later retrieval; visibility and durability uninspected.
- Delegated visibility: Service receives IDs; caller gets success/error, not a factual evaluation.
- Selection predicate: Document existence/status, normalized memory equality or explicit ID, then returned deletion/forget count. No answer oracle, improvement trigger or per-content human approval.
- Invalidation or expiry: Remote withdrawal requested; no local restoration or cache eviction wired by helper.
- Activation or effect: Blocks certain target mismatches/nonterminal deletes and rejects reported zero-success results; not proof of remote effect.
- Evidence limits: Status omission and direct-ID branches limit gates; no truth criterion or rollback.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (status !== undefined && !TERMINAL_DOCUMENT_STATUSES.has(status)) {
> --- `packages/tools/src/tools-shared.ts`

> .filter((match) => normalizeMemoryFact(match.memory) === target)
> .map((match) => match.id)
> --- `packages/tools/src/tools-shared.ts`

#### EPI-RTE-claude-files
Label: Claude document file editing

No counterpart in supplied routes: this dispatches file commands, unlike conversation submission or generic framework fact tools in [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop). Caller supplies command and text; code validates path/required arguments and resolves the exact stored document using source/path metadata rather than ranked chunks. Create overwrites; replace changes the first literal match; insert modifies a line position; rename writes destination then deletes source; delete checks returned count. `writeFile` tries update, falling back to add only on not-found. These are operational file admissions, not evidence-consuming claim acceptance. Guidance is the shipped command schema and path rules; operating mode is open requests, with no answer oracle. Caller can abstain or later edit/delete, code and service can veto, but no per-content human approval or transactional rollback is established. SRC-1 implementation: `packages/tools/src/claude-memory.ts`.

- Immediate return: Success/content/error or formatted tool-result with is_error.
- Later read-back: View resolves complete remote file and numbers selected lines; directory view paginates all results then filters paths. A later caller can receive retained edits.
- Delegated visibility: API receives file content and metadata; host gets command outcome or numbered content.
- Selection predicate: Namespace, reversible/legacy IDs, source/path match and command-specific literal/line checks; caller chooses content.
- Invalidation or expiry: Replacement/deletion requests change remote documents; rename is non-atomic write then delete; no local cache or host-context clearing.
- Activation or effect: Retention/read requests wired; actual later behavior depends on external caller interpretation.
- Evidence limits: No concrete file instance or execution; truth-aptness and semantic classification indeterminate, service consistency/concurrency unverified.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const newContent = originalContent.replace(oldStr, () => newStr)
> --- `packages/tools/src/claude-memory.ts`

Concrete source deduction: old content `A A`, old string `A`, replacement `$&` becomes literal `$& A`, not `A A`. This establishes only the fixed string transformation and literal replacement behavior, not a factual derivation.

> if (!isNotFoundError(error)) throw error
> await this.client.add(this.namespace, { content, id, metadata })
> --- `packages/tools/src/claude-memory.ts`

#### EPI-RTE-graph-dreaming
Label: Dreaming inferred facts

No supplied route describes this remote internal transformation; [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model) names a component, not an inspected route. Documentation says dreaming extracts, links, resolves updates and derives propositions from groups of documents. In the specific example, being a PM and frequently discussing payment APIs/fraud does not entail working on the core payments product: those premises also fit a PM on another product. Thus this example is ampliative conjecture. Other extraction could reshape, derive or conjecture; inaccessible implementation leaves that classification indeterminate. SRC-1 doctrine/design: `apps/docs/concepts/graph-memory.mdx`.

- Immediate return: uninspected — documentation describes asynchronous/dynamic or instant processing, not an inspected execution.
- Later read-back: Declared graph facts and relations enter search/profile; actual effects unobserved.
- Delegated visibility: Remote engine's model prompts, evidence and intermediate judgments unavailable.
- Selection predicate: Declared related-document grouping and configured dreaming mode; caller supplies documents, remote process decides extraction/relationships. No supplied answer oracle or mandatory human gate.
- Invalidation or expiry: Documentation declares updates, time expiry, contradiction resolution and noise filtering; exact conditions/rollback uninspected.
- Activation or effect: Declared production of retained inferred content, not inspected or observed engine operation.
- Evidence limits: Truth tests, evaluator domain and error calibration unknown; novelty or coherence cannot substitute for acceptance.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> Memory 1: "Alex is a PM at Stripe"
> Memory 2: "Alex frequently discusses payment APIs and fraud detection"
>          → Derived: "Alex likely works on Stripe's core payments product"
> --- `apps/docs/concepts/graph-memory.mdx`

#### EPI-RTE-inference-review
Label: Inferred memory review actions

No counterpart in supplied runtime routes: [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget) selects forgetting targets; these declared endpoints operate on an inferred-memory queue and review stamps. SRC-1 doctrine/design: `apps/docs/recall/memory-review.mdx`; interface schema in `packages/lib/api.ts`, not endpoint implementation. Target is one namespace-scoped inferred proposition. The client proposes approve/decline/undo and the declared server transition decides status. Human UI review is intended but generic HTTP calls do not prove human authorship. No required evidence input, reference truth, intended-use criterion or recorded reasoning is specified. Consequently approval licenses the product's confirmation label, not established evidence-consuming acceptance under this analysis.

- Immediate return: Declared ID/inference/forgotten/review status, or authentication/permission/not-reviewable error.
- Later read-back: Declared approval clears inference marker; decline removes from search and queue; undo restores unreviewed state and can un-forget.
- Delegated visibility: Client gets candidate text, parent count and metadata; no required premise passages or proof supplied by the queue contract.
- Selection predicate: Declared unreviewed, nonforgotten, nonexpired inferred facts; up to 50 ordered by parent count then creation time. Client chooses action; no answer oracle or improvement trigger.
- Invalidation or expiry: Undo reverses prior disposition; decline withdraws remote search availability by contract, not existing host contexts/caches.
- Activation or effect: Declared search eligibility and inference-flag changes; typed action interface exists, but service and consumer execution unobserved.
- Evidence limits: Parent count is not independent corroboration or a truth probability; implementation, human judgment and evidence-consuming acceptance uninspected.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> | **Approve** | `isInference` cleared | Stays in search, no longer flagged as inferred |
> | **Decline** | `isForgotten` set | Removed from search entirely — a rejected guess is forgotten |
> | **Undo** | back to unreviewed | Returns to the queue, flagged as inferred again |
> --- `apps/docs/recall/memory-review.mdx`

### Claims

#### EPI-CLM-graph-truth
Label: Graph stays true

Claimed operation: living graph extraction, updates, extensions, derives, expiry and contradiction handling keep understanding current. Distinct from [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary), which locates unavailable implementation, not the asserted knowledge mechanism. SRC-1 doctrine/design, `apps/docs/concepts/graph-memory.mdx`.

> **How understanding is stored and stays true over time.**
> --- `apps/docs/concepts/graph-memory.mdx`

> - **Contradiction** — updates win for “what’s true now.”
> --- `apps/docs/concepts/graph-memory.mdx`

#### EPI-CLM-review-facts
Label: Review confirms inferred facts

Claimed operation: approve promotes an inferred memory to confirmed fact, decline forgets it and undo restores unreviewed status. Distinct from [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary): this is a disposition claim with declared consumers. SRC-1 doctrine/design, `apps/docs/recall/memory-review.mdx`; schema existence in `packages/lib/api.ts` does not establish enforcement.

> - **`approve`** — Promote the memory: clears `isInference`, so it's treated as a
>   confirmed fact. Stamps `reviewStatus: "approved"`.
> --- `apps/docs/recall/memory-review.mdx`

#### EPI-CLM-benchmark-judge
Label: MemoryBench answer correctness

Claimed operation: an external judge LLM compares benchmark provider answers to ground truth and reports verdicts, with latency and context cost separately reported. No supplied claim counterpart after comparison with [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary). SRC-1 doctrine/design, `apps/docs/memorybench/memscore.mdx`. Target/domain: answers to selected benchmark questions under selected judging prompts, not all retained memories. Evaluator choices include GPT-4o, Claude Sonnet and Gemini Flash; their exact versions, weights, update behavior and endpoint resolution are uninspected because no benchmark implementation or execution is registered. No causal experiment or wired product-consumer path is established.

> Correctness isn't decided by string matching — a **judge LLM** (GPT-4o, Claude Sonnet, or Gemini Flash, your choice) compares the provider's answer against ground truth and returns a verdict:
> --- `apps/docs/memorybench/memscore.mdx`

> | **Success rate** | Percentage of questions that completed without erroring (failures are excluded from accuracy, not counted against it) |
> --- `apps/docs/memorybench/memscore.mdx`
