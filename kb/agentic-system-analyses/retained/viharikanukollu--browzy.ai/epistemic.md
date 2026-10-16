---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "browzy.ai epistemic routes: source-to-wiki authority, answer grounding, health checks and interaction-derived candidates."
run-id: AAS-2026-10-15-browzy-ai-0a823a13a7b6-01
reviewed-boundary: "56c253042041ee2f483a5e9b824174d746891cf4"
---

# browzy.ai epistemic report

## Source-and-claim boundary

The question is what licenses reliance on imported sources, compiled articles, generated answers and interaction-derived material. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); source identity and layers: see [Source register](boundary.md#source-register). All additional inspection below is SRC-1 at that pin. Code supplies implementation evidence; prompts and README supply doctrine/design. No execution, provider weights, real user corpus or causal comparison was supplied. Consequently actual factual accuracy, successful correction, model compliance, benefit and exercised learning remain unestablished. Accessible service adapters do not reveal changes inside distributed-parametric state; see [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider).

Consequential claims are [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding), [EPI-CLM-source-compounding](#epi-clm-source-compounding), [EPI-CLM-compiler-preservation](#epi-clm-compiler-preservation) and [EPI-CLM-quality-auditor](#epi-clm-quality-auditor). No broader system-complete negative follows from this assessment.

| Entry point or operation | Source path, SRC-1 | Coverage and conclusion limit |
|---|---|---|
| Executable dispatch | `src/cli/entry.tsx` | Direct complete read confirms Ink default and registered init/ingest/compile/query/lint/status/search, consistent with runtime. No registered model tool dispatcher here. |
| Ingest and image description | `src/core/ingest/index.ts`, `src/core/ingest/image.ts` | Direct complete reads; [EPI-RTE-image-description](#epi-rte-image-description). Web/PDF/text processor bodies not directly assessed here; supplied source-compilation container covers their dispatch, not extraction fidelity. |
| Template/model compilation, parser, concepts, backlinks/index | `src/core/compile/compiler.ts`, `src/core/sanitization.ts` | Direct complete reads; [EPI-RTE-template-article](#epi-rte-template-article), [EPI-RTE-article-admission](#epi-rte-article-admission). Concept suggestions are returned slugs, not newly accepted concept articles. |
| Answering/cache/history/schema | `src/core/query/engine.ts`, `src/core/query/historyManager.ts`, `src/core/schema.ts`, `src/core/prompts.ts` | Supplied findings [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), [RT-RTE-library-query](runtime.md#rt-rte-library-query), [RT-RTE-schema-change](runtime.md#rt-rte-schema-change); prompt claim locations additionally searched. No independent provider compliance observation. |
| Retrieval and coverage diagnostics | `src/core/retrieval/contextBuilder.ts`, `src/core/discovery/gapResolver.ts` | Direct complete reads; [EPI-RTE-coverage-diagnostics](#epi-rte-coverage-diagnostics). Ranking internals, SQLite search implementation and section scorer not independently audited; semantic relevance and search completeness not proven. |
| Health checks and consumers | `src/core/lint/linter.ts`, `src/cli/commands/lint.ts`, `src/cli/app.tsx` | Linter/CLI complete reads; app health/rebuild range directly read. [EPI-RTE-wiki-checks](#epi-rte-wiki-checks), [EPI-RTE-issue-display](#epi-rte-issue-display). |
| Conversation compaction | `src/core/retrieval/compactor.ts`, `src/cli/app.tsx` | Direct complete compactor and app trigger reads; [EPI-RTE-conversation-compaction](#epi-rte-conversation-compaction). Shipped caller discards result, despite comment promising future context use. |
| Digest/crystallizer/session | `src/core/query/digest.ts`, `src/core/query/crystallizer.ts`, `src/cli/hooks/useSession.ts`, `src/cli/app.tsx` | Supplied [RT-RTE-session-digest](runtime.md#rt-rte-session-digest), [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft). Draft-to-live-wiki promotion remains unestablished, not inferred from filename. |
| Freshness/refresh/rebuild | `src/core/discovery/freshness.ts`, `src/cli/app.tsx` | Freshness complete direct read; supplied refresh and direct rebuild caller findings. HEAD metadata establishes a change signal, not a truth or endorsement check; compiler source-membership predicate can defeat recompilation. |
| Topic/clipboard/search/demo and static state | `src/cli/app.tsx`, `src/core/demo/seed.ts`, `src/core/discovery/webSearch.ts` | Supplied boundary coverage, app route search only for topic/gap consumers. Not independently traced end to end; no conclusion about source selection quality or demo provenance beyond boundary. |
| Test evaluators | `tests/e2e/retrieval-quality.test.ts` | Direct lines 1–210 only: fixture-based search assertions and token heuristics. Expected slug membership is an explicit test oracle for those searches, not factual-answer validation. Tests not run; remaining test bodies/fixtures not independently inspected. |
| Legacy/exported operations and dependency code | `src/cli/index.ts`, `src/cli/repl.ts`, `src/index.ts`, `package-lock.json` | Supplied classification and exports only. Full legacy/library operation enumeration and dependency internals not assessed; prevents universal no-evaluator/no-learning claim. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-content](#epi-obj-source-content) | Imported statements about user-selected topics | see record | SRC-1 `src/core/ingest/index.ts` | Imported truth warrant unknown; extraction fidelity varies by uninspected processor. |
| [EPI-OBJ-image-description](#epi-obj-image-description) | Model assertions about image contents | see record | SRC-1 `src/core/ingest/image.ts` | Not the original image's assertions or an independently checked transcription. |
| [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | Article bodies and summaries about source topics | see record | SRC-1 `src/core/compile/compiler.ts` | Short copy and model rewrite have different transformation guarantees. |
| [EPI-OBJ-lint-issue](#epi-obj-lint-issue) | Link/metadata diagnoses and model consistency allegations | see record | SRC-1 `src/core/lint/linter.ts` | Structural facts and semantic allegations have different evaluators. |
| [RT-OBJ-browzy-schema](runtime.md#rt-obj-browzy-schema) | Preferences, not necessarily truth-apt | see record | SRC-1 `src/core/schema.ts` | Instruction supply is not evidence about domain truth. |
| [RT-RTE-answer-question](runtime.md#rt-rte-answer-question) | Answer statements; human and assistant history | see record | SRC-1 `src/cli/app.tsx` | Route-owned output, not a newly declared duplicate object. Source use list is not an audited citation map. |
| [RT-RTE-session-digest](runtime.md#rt-rte-session-digest) | Claims about prior conversation and its conclusions | see record | SRC-1 `src/core/query/digest.ts` | Semantic preservation indeterminate; summary is not criticism or acceptance of the conversation's claims. |
| [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft) | Candidate connections extracted from answer | see record | SRC-1 `src/core/query/crystallizer.ts` | No concrete candidate instance supplied; entailment/non-entailment and actual novelty not determinable. |
| [EPI-RTE-coverage-diagnostics](#epi-rte-coverage-diagnostics) | Lexical match/coverage indicators | see record | SRC-1 `src/core/retrieval/contextBuilder.ts` | Coverage label is not confidence in factual truth. |

## Authority-route ledger

Fields owned by cited records are referenced with `see`; classifications and architectural status below are this overlay's assessments. Each row is one function even where a container implements several. All results are possible implementation results, not observed runs.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) | content transformation | implemented | [EPI-OBJ-source-content](#epi-obj-source-content) | truth-apt transformation: acquisition/import | External material to raw manifest | see route; source warrant unknown | see route | Imported source | see route | Acquisition, not independent confirmation | Raw input becomes compiler-eligible | Compiler/raw manifest/permissive/later compile | SRC-1 `src/core/ingest/index.ts` | none | none | Processor fidelity unassessed |
| [EPI-RTE-image-description](#epi-rte-image-description) | content transformation | implemented | [EPI-OBJ-image-description](#epi-obj-image-description) | truth-apt transformation: indeterminate | Image to model description | see record | see record | Description or pending placeholder | see record | Candidate image interpretation only | Description retained as raw material | see record | SRC-1 `src/core/ingest/image.ts` | none | none | No instance establishes semantic fidelity or non-entailment |
| [EPI-RTE-template-article](#epi-rte-template-article) | content transformation | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | truth-apt transformation: non-ampliative reshaping | Sanitized short source to article/body/summary | see record | see record | Body copied, prefix summary | see record | No new warrant for copied assertions | Eligible for article writes | see record | SRC-1 `src/core/compile/compiler.ts` | [EPI-CLM-compiler-preservation](#epi-clm-compiler-preservation) | short-source exception | General Unicode normalization may change source spelling |
| [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) | content transformation | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | truth-apt transformation: indeterminate | Long raw content to model article | see route | see route | Candidate article blocks | see route | Synthesis candidate; no checked entailment | Parser receives generated text | Parser/model response/permissive/current compile | SRC-1 `src/core/compile/compiler.ts` | [EPI-CLM-compiler-preservation](#epi-clm-compiler-preservation) | preservation not enforced | Titles only cannot support faithful merging of unseen old bodies |
| [EPI-RTE-article-admission](#epi-rte-article-admission) | disposition/acceptance | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | no content change | Marker/metadata admission to wiki | see record | see record | Parsed candidate admitted or skipped | see record | No evidence-consuming truth acceptance | Writes permitted without per-article human review | see record | SRC-1 `src/core/compile/compiler.ts` | [EPI-CLM-compiler-preservation](#epi-clm-compiler-preservation) | structural admission only | Empty body can pass; citations not validated |
| [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) | retention | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | no content change | Candidate to file and search record | see route | see route | Retained wiki/FTS/index | see route | Retention does not establish acceptance | Later retrieval permitted | Query/Markdown and FTS/permissive/future requests | SRC-1 `src/core/compile/compiler.ts` | none | none | Link/tag organization is not lifecycle integration after truth acceptance |
| [EPI-RTE-coverage-diagnostics](#epi-rte-coverage-diagnostics) | check/evidence production | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | no content change | Query coverage, not claim truth | see record | see record | Confidence/gaps | see record | Heuristic lexical scope only | UI and gap search receive diagnostics | see record | SRC-1 `src/core/retrieval/contextBuilder.ts` | [EPI-CLM-source-compounding](#epi-clm-source-compounding) | coverage versus correctness | Ranking evidence not a ground-truth answer oracle |
| [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), [RT-RTE-library-query](runtime.md#rt-rte-library-query) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | truth-apt transformation: non-ampliative reshaping | Wiki subset to model context | see routes | see routes | Selected article blocks, budget omissions | see routes | Source warrant remains unknown; omitted qualifications possible | Selected text presented as primary truth | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1 `src/core/retrieval/contextBuilder.ts` | [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding) | trust policy not verification | Model obedience unobserved |
| [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), [RT-RTE-library-query](runtime.md#rt-rte-library-query) | content transformation | implemented | Answer, see routes | truth-apt transformation: indeterminate | Context/question to answer | see routes | see routes | Generated answer | see routes | No post-answer truth license established | Display/cache/session consumption | see routes | SRC-1 `src/core/query/engine.ts` | [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding) | grounding requested | Neither entailment nor ampliation classifiable for an absent answer instance |
| [EPI-RTE-wiki-checks](#epi-rte-wiki-checks) | check/evidence production | implemented | [EPI-OBJ-lint-issue](#epi-obj-lint-issue) | no content change | Link structure, fields; summary consistency | see record | see record | Issues or empty result | see record | Structural deductions scoped to loaded files; model allegations unverified | Issues passed to display | see record | SRC-1 `src/core/lint/linter.ts` | [EPI-CLM-quality-auditor](#epi-clm-quality-auditor) | summaries not full claims | Parse failure can look like no semantic issues |
| [EPI-RTE-issue-display](#epi-rte-issue-display) | operational admission/selection/consumption | implemented | [EPI-OBJ-lint-issue](#epi-obj-lint-issue) | no content change | Issues to operator | see record | see record | Advisory messages/counts | see record | No acceptance/rejection of article truth | No automatic repair or retrieval veto in these consumers | see record | SRC-1 `src/cli/commands/lint.ts` | [EPI-CLM-quality-auditor](#epi-clm-quality-auditor) | advisory not enforcing | Later user response unobserved |
| [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft) | check/evidence production | implemented | Draft candidate, see route | no content change | Novelty relative to supplied articles | see route | see route | NONE or article proposal | see route | Model comparison only; neither truth nor corpus-wide novelty established | Enables draft parser | Model response/parser/permissive/current answer | SRC-1 `src/core/query/crystallizer.ts` | none | novelty versus truth | Comparison uses truncated source/answer text |
| [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft) | retention | implemented | Draft candidate, see route | truth-apt transformation: indeterminate | Answer connection to draft | see route | see route | Parsed draft file | see route | Candidate retention, not accepted ampliative knowledge | File write, not live wiki admission | see route | SRC-1 `src/core/query/crystallizer.ts` | none | none | No automatic later draft consumer established |
| [RT-RTE-session-digest](runtime.md#rt-rte-session-digest) | retention | implemented | Digest, see route | truth-apt transformation: indeterminate | Conversation to summary/banner/wiki attempt | see route | see route | Digest text and optional article | see route | Summary not validation of session assertions | Banner read and attempted wiki insertion | see route | SRC-1 `src/cli/app.tsx` | none | digest differs from draft gates | Runtime module resolution and retrieval remain unobserved |
| [RT-RTE-schema-change](runtime.md#rt-rte-schema-change) | behavior/policy adaptation | implemented | [RT-OBJ-browzy-schema](runtime.md#rt-obj-browzy-schema) | non-truth-apt policy/content update: owner preferences | Owner file to system instructions | see route | see route | New prompt supply | see route | No truth acceptance implied | Model asked to follow preferences | see [RT-BAP-schema-instruction](runtime.md#rt-bap-schema-instruction) | SRC-1 `src/core/schema.ts` | none | none | Human-directed customization, not evidence of self-improvement |

Route ID: [EPI-RTE-conversation-compaction](#epi-rte-conversation-compaction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: Returned conversation summary, see record.
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Older messages to summary plus recent tail.
Evaluator/condition and domain: see record; no fidelity evaluator.
Activation and timing: see record.
Possible or observed result: Summary returned; shipped terminal caller ignores it.
Implemented force: No downstream force in that caller.
Epistemic authority and scope: No checked preservation or truth license.
Operational authority: behavior permitted, blocked, or changed: Provider summarization request, no installed future context change.
Behavioral-authority path: consumer, channel, force, horizon: No consequential summary consumer in inspected caller; public function can return to an unspecified host whose use is uninspected.
Evidence source ID and local anchor: SRC-1 `src/core/retrieval/compactor.ts`, `src/cli/app.tsx`.
Claim IDs or none: none.
Mismatch marker or none: Comment promises future context use but result is discarded.
Gap/limit: Extends runtime coverage; no supersession needed for its valid bounded history-trimming account.

Freshness is a separate lineage/change signal, not a truth evaluator: direct SRC-1 `src/core/discovery/freshness.ts` inspects up to ten oldest eligible web sources using HEAD, compares Last-Modified or stored ETag, and silently skips network errors. Supplied [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) establishes why refresh/rebuild does not guarantee withdrawal or replacement of stale articles. No record here establishes evidence-consuming acceptance against a factual criterion, or lifecycle integration after such acceptance. This is a bounded finding about the inspected writes/checks, not an assertion about inaccessible model cognition or every uninspected operation.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding) | see record | SRC-1 `src/core/prompts.ts`, doctrine/design | see record | [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), [RT-RTE-library-query](runtime.md#rt-rte-library-query) | None supplied | No component intervention or answer audit | Context and provenance instructions delivered | Delivery is not enforced grounding; source warrant unknown |
| [EPI-CLM-source-compounding](#epi-clm-source-compounding) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation), [EPI-RTE-coverage-diagnostics](#epi-rte-coverage-diagnostics) | None supplied | No before/after comparison; finite selection and stale content qualify universal benefit | Sources can expand available content; questions can yield gap suggestions | Every-source/every-answer improvement unsupported |
| [EPI-CLM-compiler-preservation](#epi-clm-compiler-preservation) | see record | SRC-1 `src/core/prompts.ts`, `src/core/compile/compiler.ts`, doctrine/design | see record | [EPI-RTE-template-article](#epi-rte-template-article), [EPI-RTE-article-admission](#epi-rte-article-admission), [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) | None supplied | No merge-preservation or contradiction test output | Model receives preservation request; short route copies sanitized text | Existing bodies not supplied; collision rename and source metadata replacement do not enforce preservation |
| [EPI-CLM-quality-auditor](#epi-clm-quality-auditor) | see record | SRC-1 `src/core/prompts.ts`, doctrine/design | see record | [EPI-RTE-wiki-checks](#epi-rte-wiki-checks), [EPI-RTE-issue-display](#epi-rte-issue-display) | None supplied | No sensitivity/specificity measurement; summaries omit body details | Structural checks plus advisory model critique | No automatic correction, truth gate or reliable clean bill of health |

## Bounded conclusion

- Imported raw text and model-described images can become retained wiki content through software admission. Original source IDs remain useful lineage labels, but neither selection by a user nor membership in the wiki verifies source truth. The image route introduces a separate unchecked interpretation before compilation; see [EPI-RTE-image-description](#epi-rte-image-description).
- The short-source route copies its sanitized body and computes a prefix summary; this is a demonstrated implementation deduction, not novel knowledge production. Long-source compilation, answering, digesting and draft extraction cannot be classified as entailed derivation or ampliative conjecture without concrete content and checked interpretation. Fluent synthesis and a novelty instruction do not establish either class; see [EPI-RTE-template-article](#epi-rte-template-article) and [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft).
- Article markers/title/slug and draft shape/length gates are operational admission criteria. Their intended use is parseable persisted content, not acceptance of factual claims. Wiki admission has future answer-context authority; draft retention has no established automatic answer consumer. Digest insertion is a separate attempted route and defeats a blanket claim that all interaction-derived writes require human approval; see [EPI-RTE-article-admission](#epi-rte-article-admission), [RT-RTE-session-digest](runtime.md#rt-rte-session-digest).
- Structural lint results license narrow statements about loaded links/fields. Model consistency checks see summaries rather than full article propositions, and their outputs are advisory. Ranking confidence licenses no claim-truth probability; gap labels are lexical search signals. Neither result enforces revision, rejection, withdrawal or factual acceptance in the traced consumers; see [EPI-RTE-wiki-checks](#epi-rte-wiki-checks), [EPI-RTE-issue-display](#epi-rte-issue-display), [EPI-RTE-coverage-diagnostics](#epi-rte-coverage-diagnostics).
- Future model calls receive selected wiki text under a primary-truth policy, and owner schema preferences can change instructions. Those are live authority pathways at the implementation level, not observed compliance. Session/draft writes, schema editing and content accumulation do not alone demonstrate improved capacity, reflective criticism, autonomous theory building or exercised self-improvement. No theory instance or content-directed criticism/revision loop was supplied for those assessments. External model parameters remain opaque independently of these symbolic/textual routes; see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context), [RT-BAP-schema-instruction](runtime.md#rt-bap-schema-instruction), [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider).

## Shared records

### Operative objects

#### EPI-OBJ-source-content
Label: Raw source content

Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Object part of the route's raw-state output, not a duplicate of that end-to-end route. Source-native identity: source files named by RawSource.path and raw manifest entries. Representational form: natural-language source text plus symbolic source IDs/origin/type records. Storage substrate: local raw files/manifest and source SQLite rows. SRC-1 `src/core/ingest/index.ts`. Imported statements have unknown warrant; dispatch does not evaluate truth.

> fsStore.writeRawManifest(manifest);
> --- `src/core/ingest/index.ts`

#### EPI-OBJ-image-description
Label: Image description

Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Distinct intermediate object within ingestion: natural-language model description appended to a raw Markdown image reference; local raw file, with copied image in raw/images. Its factual claims concern visible image content. Unlike direct text import it is model-authored. SRC-1 `src/core/ingest/image.ts`; see [EPI-RTE-image-description](#epi-rte-image-description) for passage.

#### EPI-OBJ-wiki-article
Label: WikiArticle

Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Distinct retained output object, not a duplicate route. Source-native identity: WikiArticle.content and frontmatter. Representational form: natural-language body/summary and symbolic slug/source/tag/date fields. Storage substrate: Markdown, SQLite search rows and generated wiki index. Short-source body and model body have distinct producers; their admissions and consumers are traced separately. SRC-1 `src/core/compile/compiler.ts`; supplied write passage: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation).

#### EPI-OBJ-lint-issue
Label: LintIssue

No supplied counterpart after comparison with [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation): diagnosis output, not an article or compilation result. Representational form: natural-language message/suggestion with symbolic severity/article fields. Storage substrate: returned JS array, CLI display and terminal system messages; counts may enter activity log. SRC-1 `src/core/lint/linter.ts`, `src/cli/app.tsx`. Structural diagnoses differ from model-generated allegations; see check record.

### Routes

#### EPI-RTE-template-article
Label: Short-source template article

Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Code selects sanitized raw content shorter than 2,000 characters, constructs a WikiArticle without model interpretation, and returns it to the compiler writer. Deterministic witness: sanitized content `Rain falls.\nSnow melts.` becomes unchanged article body; summary becomes `Rain falls. Snow melts.` by prefix/newline/trim rules. This establishes non-ampliative reshaping for that concrete input, not preservation for every Unicode normalization or source format. Input source selection is user-initiated; code authors metadata and decides this branch, no per-article veto. Open ingestion mode, no expected-answer oracle; schema/guidance are bypassed. Recovery and subsequent persistence are owned by the parent route.

- Immediate return: Single candidate WikiArticle array.
- Later read-back: Future query can receive persisted body through parent route's wiki/search writes.
- Delegated visibility: inapplicable — this branch has no model call.
- Selection predicate: Sanitized rawContent.length < 2000.
- Invalidation or expiry: Parent source-membership skip and file replacement govern future reuse; no separate template expiry.
- Activation or effect: Supplies candidate without semantic evaluation; actual downstream reliance unobserved.
- Evidence limits: Implementation deduction only; no target execution or source truth check.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `src/core/compile/compiler.ts`, `src/core/sanitization.ts`.

> summary: content.slice(0, 150).replace(/\n/g, ' ').trim(),
> --- `src/core/compile/compiler.ts`

> content,
>       path: '',
> --- `src/core/compile/compiler.ts`

#### EPI-RTE-article-admission
Label: Parsed article admission

Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Model proposes article blocks; code splits markers, requires slug/title matches, sanitizes slug, and constructs frontmatter with only the current source ID. Compiler then collision-renames and writes/indexes accepted structures. This part owns structural disposition, not a truth check. Starting compile is not per-content human approval; code can skip malformed blocks, with no semantic veto or expected-answer oracle. Open requests. Guidance asks preservation and contradiction handling but does not supply existing article bodies. Rollback is not transactional across file/database writes; see parent recovery limits.

- Immediate return: Parsed article array, potentially empty; accepted entries reach parent writer.
- Later read-back: Persisted article files become later retrieval candidates under parent route.
- Delegated visibility: Model receives truncated raw source and slug/title index; parser receives response text, not an evidence audit.
- Selection predicate: Article marker blocks with slug/title and nonempty sanitized slug; no mandatory nonempty body.
- Invalidation or expiry: Parent source-membership filtering can retain stale represented-source articles; no truth-driven expiry here.
- Activation or effect: Permits wiki/search admission without factual verification or per-item human approval.
- Evidence limits: Does not establish acceptance of source propositions; no run evidence or observed successful persistence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `src/core/compile/compiler.ts`.

> if (!slugMatch || !titleMatch) continue;
> --- `src/core/compile/compiler.ts`

> sources: [sourceId],
> --- `src/core/compile/compiler.ts`

> content: bodyMatch?.[1]?.trim() || '',
> --- `src/core/compile/compiler.ts`

#### EPI-RTE-image-description
Label: Image description generation

Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Input image file → provider multimodal request → natural-language description → raw Markdown. A distinct pre-compilation transformation; caller supplies optional provider, code handles copying/writes, model authors description. File existence/size gates assess admissible input size, not image-description fidelity. No human per-description approval or reference oracle; open ingestion. Guidance is IMAGE_DESCRIPTION_PROMPT. Failure produces pending-description text; no semantic rejection, correction or rollback route is implemented in this function.

- Immediate return: RawSource pointing to persisted description/image reference.
- Later read-back: Parent compile reads the raw file; its resulting wiki article can reach future queries.
- Delegated visibility: Provider receives base64 image, MIME type, filename-derived title and description instructions.
- Selection predicate: Image type dispatch, existing file, size check; model path only with supplied llm.
- Invalidation or expiry: Re-ingest can regenerate raw description; no independent truth-review expiry.
- Activation or effect: Description becomes compiler input without independent fidelity check.
- Evidence limits: No image instance/description pair or run supplied; entailment versus hallucinated addition cannot be determined.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `src/core/ingest/image.ts`.

> description = `![${title}](images/${imgFilename})\n\n## Description\n\n${sanitizeUnicode(response.content)}`;
> --- `src/core/ingest/image.ts`

#### EPI-RTE-wiki-checks
Label: Wiki structural and consistency checks

No supplied counterpart after comparison with [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation): separate on-demand evaluator, not compiler admission. WikiLinter.lint loads articles and combines broken-link, orphan, missing-field and model-consistency checks. The structural evaluator's target is the loaded graph/metadata, not subject-matter truth. Example deduction: with only slug `a` present and body `[[missing]]`, checkBrokenLinks reports missing target. The model evaluator's target is contradiction/duplication/gaps/terminology among supplied titles and summaries, not full-body factual consistency. Human invokes health/lint; code decides structural findings; model proposes semantic allegations; parser accepts issue shape/severity. No reference answer for semantic critique, no automatic human approval, open diagnostic mode. Invalid JSON/shape produces empty semantic findings, not a recorded proof of consistency.

- Immediate return: LintIssue array combining deterministic diagnoses and parsed model allegations.
- Later read-back: inapplicable — this function does not retain diagnoses for another invocation.
- Delegated visibility: Model sees slug/title/summary list, not article bodies or underlying sources.
- Selection predicate: All loaded articles for structural checks; fewer than two bypasses semantic comparison; valid severity/string fields for model issue admission.
- Invalidation or expiry: Fresh invocation recomputes; no durable issue withdrawal protocol.
- Activation or effect: Results go to separate advisory consumers; no article repair or veto here.
- Evidence limits: Structural license bounded to code's matching rules and loaded state; model allegations lack independent evidence verification; no observed diagnoses.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `src/core/lint/linter.ts`.

> const summaries = articles
>       .map(a => `- ${a.slug}: ${a.frontmatter.title} — ${a.frontmatter.summary || '(no summary)'}`)
>       .join('\n');
> --- `src/core/lint/linter.ts`

> if (!slugs.has(target)) {
>           issues.push({
>             severity: 'warning',
>             article: article.slug,
>             message: `Broken wiki link: [[${target}]]`,
> --- `src/core/lint/linter.ts`

> if (!jsonMatch) return [];
> --- `src/core/lint/linter.ts`

#### EPI-RTE-issue-display
Label: Health issue display

No supplied counterpart after comparison with [RT-RTE-answer-question](runtime.md#rt-rte-answer-question): lint result consumption, not answer generation. CLI prints issues and suggestions or healthy status; terminal adds system notices and logs severity counts. Consumer: operator, via console/session messages. Force: advisory, no edit/retrieval veto in these callers. Horizon: present display and retained session notices; no programmatic issue-driven correction loop established. Users may act externally, but invocation is not evidence of such action. Open diagnostic mode; no admission proposal or reference-answer oracle in this display part.

- Immediate return: Console/session messages and severity counts.
- Later read-back: Terminal session notices can be saved, but supplied history/digest routes omit system messages from provider input; no automatic corrective reader established.
- Delegated visibility: inapplicable — display does not invoke a model.
- Selection predicate: Parsed issues displayed; zero issues produces healthy CLI message.
- Invalidation or expiry: Later lint can replace displayed assessment; no durable rejection/withdrawal semantics.
- Activation or effect: Changes operator-visible advice only; no automatic article correction or blocking.
- Evidence limits: User reliance and subsequent edits unobserved; healthy message can follow absent/failed semantic parsing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `src/cli/commands/lint.ts`, `src/cli/app.tsx`.

> success('Wiki is healthy — no issues found');
> --- `src/cli/commands/lint.ts`

> console.log(`${icon} [${issue.article}] ${issue.message}`);
> --- `src/cli/commands/lint.ts`

#### EPI-RTE-coverage-diagnostics
Label: Query coverage diagnostics

Part of: [RT-RTE-answer-question](runtime.md#rt-rte-answer-question)

Material check part of context preparation, also reused by [RT-RTE-library-query](runtime.md#rt-rte-library-query). Code turns rank scores/count into high/medium/low coverage; per-term FTS with punctuation/stop-word/length filters yields gaps. Target is lexical corpus coverage, not proposition truth. Human supplies question, software decides scores/gaps, no expected-answer oracle or per-diagnostic veto. Open query mode. Consumer is result/UI and terminal's first-gap suggestion path; code can request search through gapResolver with blacklist/length filtering. Force: advisory, not factual answer admission. Gap suggestions do not validate fetched sources.

- Immediate return: Coverage confidence and gaps bundled with context.
- Later read-back: Library cached query result can retain diagnostics; no diagnosis-driven method revision established.
- Delegated visibility: Model receives assembled context; diagnostic fields alone do not establish an independent model check.
- Selection predicate: Ranked candidate scores/count; search terms longer than four characters and not stop words; one FTS hit counts as coverage.
- Invalidation or expiry: Recompute on new context build; parent cache TTL/invalidation qualifies reuse.
- Activation or effect: Result can trigger source suggestions and UI labels; no semantic truth veto.
- Evidence limits: Ranking/search internals not independently verified here; threshold is not measured epistemic calibration; suggestions/benefit unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `src/core/retrieval/contextBuilder.ts`, `src/core/discovery/gapResolver.ts`; supplied terminal gap consumer: [RT-RTE-answer-question](runtime.md#rt-rte-answer-question).

> if (topScore > 15 && ranked.length >= 3 && avgScore > 5) return 'high';
> --- `src/core/retrieval/contextBuilder.ts`

> const results = this.db.search(term, 1);
>       if (results.length === 0) {
>         gaps.push(term);
> --- `src/core/retrieval/contextBuilder.ts`

#### EPI-RTE-conversation-compaction
Label: Conversation compaction

Distinct from [RT-RTE-answer-question](runtime.md#rt-rte-answer-question)'s ordinary history selection: a separate model summary call whose result is discarded by the shipped terminal caller. SRC-1 `src/core/retrieval/compactor.ts`, `src/cli/app.tsx`. After more than twenty session messages the terminal requests compaction retaining six recent messages. Code slices older messages, truncates each to 3,000 characters, asks a model for topic/findings/corrections/pending-thread summary and returns a system-summary message plus recent tail. The app awaits the call without assigning its result. This is candidate generation without a subsequent answer consumer in this path, despite the nearby comment. No factual fidelity check, reference oracle or human per-summary approval; open conversation mode. On repeated provider failure original messages are returned.

- Immediate return: Summary and keptMessages, or original messages after retry failure.
- Later read-back: inapplicable — inspected terminal call discards return; no persistence or future prompt installation occurs there.
- Delegated visibility: Summarizer receives older role-tagged messages with per-message truncation, not retained recent tail.
- Selection predicate: Terminal message count greater than twenty and provider available; function summarizes all but requested recent count.
- Invalidation or expiry: Returned candidate has no retained lifetime in this caller; original displayed/session messages remain.
- Activation or effect: Adds a provider call, not a demonstrated or wired replacement of later terminal answer context.
- Evidence limits: No run; unspecified library host could consume return, but that behavior is not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await compactConversation(
>             session.messages.map(m => ({ role: m.role, content: m.content })),
>             currentLlm,
>             6,
>           );
> --- `src/cli/app.tsx`

> // Compaction result is used internally for LLM context in future queries.
> --- `src/cli/app.tsx`

> const summaryMatch = response.content.match(/<summary>([\s\S]*?)<\/summary>/);
> --- `src/core/retrieval/compactor.ts`

### Claims

#### EPI-CLM-source-compounding
Label: Source addition compounds answer quality

No supplied counterpart after comparison with [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding): improvement claim rather than grounding policy. SRC-1 `README.md`, doctrine/design; universal future-answer benefit is not observed or causally supported.

> **The loop that compounds:** every source you add makes every future answer better. Every question you ask can surface gaps — browzy suggests sources to fill them.
> --- `README.md`

#### EPI-CLM-compiler-preservation
Label: Compiler source preservation

Distinct from answer provenance claim [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding): compiler instructions request preservation, merging and contradiction handling. SRC-1 `src/core/prompts.ts`, `src/core/compile/compiler.ts`, doctrine/design. Code input limitations prevent interpreting request as a guarantee.

> 1. If this source's content fits into an existing article, output an UPDATED version of that article with the new information merged in. Preserve all existing content and sources — add to them, don't replace.
> --- `src/core/compile/compiler.ts`

#### EPI-CLM-quality-auditor
Label: Wiki quality auditor

Distinct from [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding): diagnostic mandate rather than answer policy. SRC-1 `src/core/prompts.ts`, doctrine/design. Mandate does not establish reliable detection or corrective force.

> export const LINTER_SYSTEM_PROMPT = `You are browzy's browzy quality auditor. Your job is to find real problems in the knowledge base — not style preferences, not nitpicks, but issues that would cause a researcher to get wrong answers, miss connections, or waste time.
> --- `src/core/prompts.ts`
