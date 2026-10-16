---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "CocoIndex epistemic routes: source context, typed extraction, entity decisions, operational checks and the limits of freshness as warrant."
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
reviewed-boundary: "1639793b3602408a9cb220728fb30e306d433473"
---

# CocoIndex epistemic report

## Source-and-claim boundary

The question is whether CocoIndex's context-indexing and shipped consumer routes establish truth, or instead transport and operationally admit content. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register), SRC-1. This is the same whole-system target, but the assessment below is a bounded route analysis, not a complete negative audit. All new reads are implementation or doctrine/design at the frozen revision. No run trace, provider output or causal comparison was supplied, and no target was executed.

Missing execution evidence prevents conclusions about actual extraction accuracy, successful withdrawals, freshness latency, retrieval benefit and exercised learning. External provider/dependency internals and model weights are outside SRC-1; they prevent exact semantic or parameter-update conclusions. Available but uninspected examples, connectors, benchmarks and tests prevent a system-complete claim that no factual evaluator, adaptation or acceptance route exists. These are inspection limits, not access failures. The manual and entity routes below are positive counterexamples to an embedding-only account; the entity retry loop is a counterexample to a schema-only account of every check.

| Entry point or operation | Source path | Coverage and records, or limit |
|---|---|---|
| CLI update, preview, reset, drop | SRC-1 `python/cocoindex/cli.py` | Direct dispatch read for update/drop; source search finds ls/show/init as other commands. See [RT-RTE-index-update](runtime.md#rt-rte-index-update), [RT-RTE-preview-update](runtime.md#rt-rte-preview-update), [RT-RTE-drop-app](runtime.md#rt-rte-drop-app). ls/show/init bodies not audited here; no exhaustive display/scaffold warrant conclusion. |
| Python/Rust APIs, live maintenance, memo reuse and retirement | SRC-1 `rust/core/src/engine/app.rs`, `rust/core/src/engine/execution.rs`, `python/cocoindex/connectors/localfs/_source.py` | Supplied runtime findings, not new direct reads: [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance), [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), [RT-RTE-drop-app](runtime.md#rt-rte-drop-app). |
| Chunk production and text search | SRC-1 `python/cocoindex/ops/text.py`, `examples/text_embedding/main.py` | Direct full text wrapper read; supplied runtime producer/query: [EPI-RTE-chunk-slice](#epi-rte-chunk-slice), [RT-RTE-query-index](runtime.md#rt-rte-query-index). Rust boundary selection and other retrieval applications not newly audited. |
| Manual extraction, validation, row declaration | SRC-1 `examples/manuals_llm_extraction/main.py` | Direct full read; [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), [EPI-RTE-module-check](#epi-rte-module-check), [EPI-RTE-module-count](#epi-rte-module-count). |
| Entity resolver generation, repair, contract check, canonical selection | SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py`, `python/cocoindex/ops/entity_resolution/__init__.py` | Resolver read fully; engine decision validation/application and resolve_entities orchestration inspected. [EPI-RTE-pair-proposal](#epi-rte-pair-proposal), [EPI-RTE-pair-check](#epi-rte-pair-check), [EPI-RTE-pair-disposition](#epi-rte-pair-disposition). Candidate-index and partition implementation only partially inspected; no completeness or parallel-equivalence proof. |
| DSPy patient extraction | SRC-1 `examples/patient_intake_extraction_dspy/main.py` | Direct full read: image conversion, ChainOfThought request, returned Patient serialized to declared local file. No optimizer/train call in this file; model compliance and dependency internals uninspected. Distinct modality/output route remains unassessed in detail; prevents exhaustive extraction conclusions. |
| Contributor registered hooks | SRC-1 `.claude/settings.json`, `.claude/hooks/py-typecheck-flag.sh`, `.claude/hooks/py-typecheck-run.sh`, `.claude/hooks/docs-build-check.sh`, `.claude/hooks/docs-build-run.sh`, `dev/agent-checks/py-typecheck-run.sh`, `dev/agent-checks/docs-build-run.sh` | All read fully: [EPI-RTE-contributor-check](#epi-rte-contributor-check), [EPI-RTE-hook-result](#epi-rte-hook-result). Host interpretation of exit codes uninspected. |
| Other ops, examples, tools and evaluation | SRC-1 `python/cocoindex/ops/litellm.py`, `examples/conversation_to_knowledge/conv_knowledge/app.py`, `benchmarks/`, `python/tests/` | Bounded source searches locate embedding/transcription operations and shipped entity-resolver call site. Remaining bodies, provider-native tool registrations, graph consumers, tests and benchmarks not inspected in this member. No source-wide absence of factual checks, tools, training or adaptation follows. Separate CocoIndex-code MCP product remains excluded by boundary. |

Consequential design claims are [EPI-CLM-fresh-context](#epi-clm-fresh-context) and [EPI-CLM-supported-extraction](#epi-clm-supported-extraction). They have different scopes: maintained context versus requested source fidelity.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-chunk-text](#epi-obj-chunk-text) | Source assertions, if any; source-dependent | see record | SRC-1 `python/cocoindex/ops/text.py` | Literal substring provenance is not source truth or complete context. |
| [EPI-OBJ-module-info](#epi-obj-module-info) | Manual-derived descriptions, API membership and arguments | see record | SRC-1 `examples/manuals_llm_extraction/main.py` | No actual returned instance supplied; conversion fidelity and assertion support unknown. |
| [EPI-OBJ-module-counts](#epi-obj-module-counts) | Sizes of extracted class/function lists | see record | SRC-1 `examples/manuals_llm_extraction/main.py` | Not independently the actual manual's counts; methods count is top-level info.methods only. |
| [EPI-OBJ-pair-decision](#epi-obj-pair-decision) | Two names refer to the same entity; canonical name preference is policy | see record | SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py` | Model receives names, scope and guidance, not independently authenticated identity evidence. |
| [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization) | No independent truth claim from serialization | see record | SRC-1 `rust/core/src/engine/execution.rs` | Reuse dependencies do not entail semantic validity. |
| [RT-CMP-sentence-transformer-embedder](runtime.md#rt-cmp-sentence-transformer-embedder) | Vectors have no separately individuated truth-apt proposition here | see record | SRC-1 `examples/text_embedding/main.py` | Relevance is operationally ranked, not verified truth. |
| [EPI-OBJ-check-exit](#epi-obj-check-exit) | Check process reported success/failure for current workspace | see record | SRC-1 `.claude/hooks/py-typecheck-run.sh` | Not a proof of application behavior, factual prose, or release admission. |

## Authority-route ledger

Fields owned by cited shared records are referenced with `see`; the ledger adds the epistemic classification and separates checking, disposition and retention. `implemented` below is an architectural finding, not observed operation.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-index-update](runtime.md#rt-rte-index-update) | content transformation | implemented | [EPI-OBJ-chunk-text](#epi-obj-chunk-text) | truth-apt transformation: acquisition/import | Source file to processing | File filter, not factual evaluator | see [RT-RTE-index-update](runtime.md#rt-rte-index-update) | Source text imported | Processing input | Source warrant unknown; no endorsement | Selected files enter processing | Processor; file data; permissive; current update | SRC-1 `examples/text_embedding/main.py` | [EPI-CLM-fresh-context](#epi-clm-fresh-context) | none | Imported source truth not checked. |
| [EPI-RTE-chunk-slice](#epi-rte-chunk-slice) | content transformation | implemented | [EPI-OBJ-chunk-text](#epi-obj-chunk-text) | truth-apt transformation: non-ampliative reshaping | Source span to chunk | Python slicing over supplied offsets | see [EPI-RTE-chunk-slice](#epi-rte-chunk-slice) | Substring | Literal slicing | Preserves selected characters, not independent-context meaning | Selected spans become downstream inputs | Chunk consumer; return value; permissive; current processing | SRC-1 `python/cocoindex/ops/text.py` | none | none | Rust offset selection not proved here. |
| [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction) | content transformation | implemented | [EPI-OBJ-module-info](#epi-obj-module-info) | truth-apt transformation: indeterminate | Converted manual to ModuleInfo | Provider interpretation of prompt; semantic domain opaque | see [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction) | Structured extraction candidate | Requested source support only | No checked entailment or factual license | Candidate proceeds to validation | Validator; response object; permissive; extraction request | SRC-1 `examples/manuals_llm_extraction/main.py` | [EPI-CLM-supported-extraction](#epi-clm-supported-extraction) | unknown: requested fidelity not independently checked | Could reshape, derive or add unsupported claims; need paired input/output and semantic assessment. |
| [EPI-RTE-module-check](#epi-rte-module-check) | check/evidence production | implemented | [EPI-OBJ-module-info](#epi-obj-module-info) | no content change | ModuleInfo shape | Pydantic fields/types, not source entailment | see [EPI-RTE-module-check](#epi-rte-module-check) | Validated object or exception | Enforcing shape gate | Schema conformity only | Invalid validation prevents row declaration through this call | process_file; return/exception; enforcing; current call | SRC-1 `examples/manuals_llm_extraction/main.py` | [EPI-CLM-supported-extraction](#epi-clm-supported-extraction) | factual interpretation exceeds checked domain | Instructor validation internals not frozen. |
| [EPI-RTE-module-count](#epi-rte-module-count) | content transformation | implemented | [EPI-OBJ-module-counts](#epi-obj-module-counts) | truth-apt transformation: entailed derivation | Extracted list cardinalities | Python len on extracted lists | see [EPI-RTE-module-count](#epi-rte-module-count) | Integer class/function counts | Row construction | Exact cardinality of supplied lists, conditional on inputs | Counts enter declared record | ModuleRecord constructor; integer fields; permissive; row lifetime | SRC-1 `examples/manuals_llm_extraction/main.py` | none | none | Does not establish actual API coverage. |
| [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction) | disposition/acceptance | implemented | [EPI-OBJ-module-info](#epi-obj-module-info) | no content change | Schema-valid extraction to row declaration | Application code after validation; operational criterion | see [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction) | Declared row candidate | Automatic admission | Operational eligibility, not evidence-consuming factual acceptance | No human per-result gate; provider/validation error can interrupt | table target; declare_row; permissive; reconciled target lifetime | SRC-1 `examples/manuals_llm_extraction/main.py` | [EPI-CLM-supported-extraction](#epi-clm-supported-extraction) | retention is not acceptance | Prompt criterion is not independently checked against manual. |
| [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction) | retention | implemented | [EPI-OBJ-module-info](#epi-obj-module-info) | no content change | Result to memo/PostgreSQL | Memo/reconciliation machinery | see [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction) | Reusable result and indexed JSON | Persistence wiring | No additional semantic warrant | Later update may reuse result; downstream retrieval uninspected | Update processor; memo; permissive; subsequent updates | SRC-1 `examples/manuals_llm_extraction/main.py` | none | none | No lifecycle integration after epistemic acceptance established. |
| [EPI-RTE-pair-proposal](#epi-rte-pair-proposal) | content transformation | implemented | [EPI-OBJ-pair-decision](#epi-obj-pair-decision) | truth-apt transformation: indeterminate | Names to identity judgment | LLM with scope/guidance and candidate list | see [EPI-RTE-pair-proposal](#epi-rte-pair-proposal) | Match/null and canonical preference | Proposal only | Identity correctness not established | Proposal reaches contract check | Resolver checker; response object; permissive; pair attempt | SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py` | none | none | Names may support identity inference but entailment/non-entailment not decidable without instance. |
| [EPI-RTE-pair-check](#epi-rte-pair-check) | check/evidence production | implemented | [EPI-OBJ-pair-decision](#epi-obj-pair-decision) | no content change | Matched identifier belongs to candidates and is not entity itself | Exact membership and equality; finite string domain | see [EPI-RTE-pair-check](#epi-rte-pair-check) | Valid match/null, retry feedback or ValueError | Enforcing interface contract | Candidate-list membership, not real-world identity | Invalid model output retried; generic invalid decision raises | Retry loop / caller; feedback or exception; enforcing; current pair | SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py` | none | none | Valid but factually wrong matches pass. |
| [EPI-RTE-pair-check](#epi-rte-pair-check) | behavior/policy adaptation | implemented | [EPI-OBJ-pair-decision](#epi-obj-pair-decision) | non-truth-apt policy/content update: corrective request context | Invalid identifier to next attempt's messages | Exact membership failure; retry budget/deadline | see [EPI-RTE-pair-check](#epi-rte-pair-check) | Assistant response plus corrective user message appended | Current-call context change | No new factual authority | Changes next provider request; cap falls back to empty decision | Provider; messages; advisory; remaining pair retries | SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py` | none | none | Feedback targets format/reference contract, not identity error. |
| [EPI-RTE-pair-proposal](#epi-rte-pair-proposal) | retention | implemented | [EPI-OBJ-pair-decision](#epi-obj-pair-decision) | no content change | Returned decision to memoized reuse | Decorated fn memo machinery | see [EPI-RTE-pair-proposal](#epi-rte-pair-proposal) | Decision reusable across calls/runs | Memo reuse | No factual acceptance added | Later identical tracked request may bypass provider inference | Resolver caller; memo return; permissive; subsequent runs | SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py` | none | none | Internal persistence follows supplied [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization); no observed replay. |
| [EPI-RTE-pair-disposition](#epi-rte-pair-disposition) | disposition/acceptance | implemented | [EPI-OBJ-pair-decision](#epi-obj-pair-decision) | no content change | Checked decision to canonical map | PINNED/PREFERRED rules plus model preference | see [EPI-RTE-pair-disposition](#epi-rte-pair-disposition) | New canonical, alias or repoint | Operational map mutation | Policy-consistent canonicalization, not factual acceptance | Existing-canonical policy can override model preference | resolve_entities caller; returned dedup map; enforcing selection; current result | SRC-1 `python/cocoindex/ops/entity_resolution/__init__.py` | none | none | Downstream graph storage/use not traced. |
| [EPI-RTE-contributor-check](#epi-rte-contributor-check) | check/evidence production | implemented | [EPI-OBJ-check-exit](#epi-obj-check-exit) | no content change | Edited Python types or docs build | mypy or npm build; workspace-dependent check domain | see [EPI-RTE-contributor-check](#epi-rte-contributor-check) | Exit status and diagnostics | Check execution wired | Only check-specific reported success/failure | Results reach Stop hook, not production row gate | Hook; process exit; advisory to this source analysis; current editing turn | SRC-1 `dev/agent-checks/py-typecheck-run.sh` | none | none | No run or dependency semantics inspected. |
| [EPI-RTE-hook-result](#epi-rte-hook-result) | operational admission/selection/consumption | implemented | [EPI-OBJ-check-exit](#epi-obj-check-exit) | no content change | Check exit to host signal | Shell nonzero branch | see [EPI-RTE-hook-result](#epi-rte-hook-result) | Exit 2 on failure, 0 otherwise | Signal emitted; host force uninspected | No factual license | Communicates failure to host; flag already removed | Claude hook host; stderr/status; advisory unless host contract enforces; Stop invocation | SRC-1 `.claude/hooks/py-typecheck-run.sh` | none | none | Not a durable acceptance decision or guaranteed veto. |
| [RT-RTE-query-index](runtime.md#rt-rte-query-index) | operational admission/selection/consumption | implemented | [EPI-OBJ-chunk-text](#epi-obj-chunk-text) | no content change | Retained rows to displayed top-k | Vector-distance SQL order | see [RT-RTE-query-index](runtime.md#rt-rte-query-index) | Printed selected text | Ranking then delivery | Similarity, not endorsement or truth | Determines search output, not a generated answer | query_once/human; SQL rows/stdout; ranking; query invocation | SRC-1 `examples/text_embedding/main.py` | [EPI-CLM-fresh-context](#epi-clm-fresh-context) | none | No downstream answering-agent evidence. |
| [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance) | lineage/freshness/recovery | implemented | [EPI-OBJ-chunk-text](#epi-obj-chunk-text) | no content change | Source changes to reconciliation | Watcher, scan and tracked dependencies | see [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance) | Updated/deleted target rows | Maintenance protocol | Freshness is not endorsement | Refreshes or retires operational context | Update engine/target; events and actions; enforcing; subsequent index state | SRC-1 `python/cocoindex/connectors/localfs/_source.py` | [EPI-CLM-fresh-context](#epi-clm-fresh-context) | none | External delivery/writes unobserved. |
| [RT-RTE-drop-app](runtime.md#rt-rte-drop-app) | lineage/freshness/recovery | implemented | [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization) | no content change | App-owned state retirement | Explicit caller; core delete handler | see [RT-RTE-drop-app](runtime.md#rt-rte-drop-app) | Removal or surfaced error | Destructive maintenance | No criticism or epistemic withdrawal decision | Successful removal prevents future reuse; partial failure possible | Core/connector; delete actions; enforcing; future app use | SRC-1 `rust/core/src/engine/app.rs` | none | none | Ordinary orphan cleanup has different error handling; see record. |
| [RT-RTE-preview-update](runtime.md#rt-rte-preview-update) | operational admission/selection/consumption | implemented | [EPI-OBJ-module-info](#epi-obj-module-info) | no content change | Planned target actions versus apply | Core preview branch | see [RT-RTE-preview-update](runtime.md#rt-rte-preview-update) | Actions returned without normal submit | Target-action withholding | No content acceptance criterion | Caller can inspect plan; model calls/direct I/O may still happen | Caller; action list; advisory; planning invocation | SRC-1 `rust/core/src/engine/execution.rs` | none | none | Not a universal sandbox or automatic approval workflow. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-fresh-context](#epi-clm-fresh-context) | see record | SRC-1 `README.md`, doctrine/design | Incremental context-maintenance intent | [RT-RTE-index-update](runtime.md#rt-rte-index-update), [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance), [RT-RTE-query-index](runtime.md#rt-rte-query-index) | None supplied | No controlled comparison or measured freshness; source delivery and external stores matter | Maintenance and retrieval wiring exists | “reliable” and “no context gap” not established as unconditional outcomes or factual warrant. |
| [EPI-CLM-supported-extraction](#epi-clm-supported-extraction) | see record | SRC-1 `examples/manuals_llm_extraction/main.py`, doctrine/design prompt | Source-only extraction requested | [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), [EPI-RTE-module-check](#epi-rte-module-check), [EPI-RTE-module-count](#epi-rte-module-count) | None supplied | No manual/output comparison or independent semantic evaluator | Typed model proposals become operational records; list cardinalities are derived exactly | Shape and persistence do not enforce prompt's source-support criterion. |

## Bounded conclusion

CocoIndex's inspected indexing path imports content whose source warrant is unknown, reshapes selected text and makes it retrievable. Character-preserving slicing supplies lineage for selected spans; it does not preserve every contextual qualification or certify their truth. See [EPI-RTE-chunk-slice](#epi-rte-chunk-slice) and [RT-RTE-query-index](runtime.md#rt-rte-query-index). Embeddings control ranking; their proposition-level content is not determinable from these sources. The supplied embedder record identifies a model name, not exact weights, and inference calls, not inspected training.

The manual route requests source-supported extraction but checks schema. Passing that check licenses construction and declaration of rows, not acceptance of a new factual claim against evidence. Persistence in memoization and PostgreSQL is operational retention before any established epistemic acceptance; no post-acceptance lifecycle integration is demonstrated. The counts are entailed only as cardinalities of extracted lists, not as verified facts about the original manual. See [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), [EPI-RTE-module-check](#epi-rte-module-check), [EPI-RTE-module-count](#epi-rte-module-count). Semantic relations remain indeterminate without actual input/output and support checks; neither novelty nor failure to prove entailment licenses labeling all outputs ampliative conjectures.

The entity route has an additional, operative evaluator: candidate-membership checking generates corrective feedback, retries invalid outputs, and falls back to no match at the retry cap. The generic resolver also rejects a self-match or out-of-list identifier. These checks constrain referential interface validity, not identity truth. Valid decisions change the canonical map, with explicit existing-canonical policy able to override model preferences. See [EPI-RTE-pair-check](#epi-rte-pair-check) and [EPI-RTE-pair-disposition](#epi-rte-pair-disposition). No supplied expected-answer oracle or independently verified identity criterion is consumed here. Model alias/endpoint uncertainty remains local to [EPI-CMP-llm-pair-resolver](#epi-cmp-llm-pair-resolver).

Maintenance, deletion and preview alter operational availability, not epistemic endorsement. Dependency-checked memo reuse is not factual revalidation. Explicit drop and ordinary orphan cleanup have different failure semantics, so successful universal withdrawal cannot be inferred. Preview withholds planned target application, not arbitrary provider or host effects. See [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), [RT-RTE-drop-app](runtime.md#rt-rte-drop-app), [RT-RTE-preview-update](runtime.md#rt-rte-preview-update).

Contributor hooks check type/build properties and return failure signals to their host. They are not factual evaluators of indexed content and do not mediate every SDK call or production write. See [EPI-RTE-contributor-check](#epi-rte-contributor-check) and [EPI-RTE-hook-result](#epi-rte-hook-result). Their removal of pending flags before checking is not acceptance or durable criticism retention.

The retry loop adapts the next request's context to an invalid identifier within one pair call. This supports a local feedback mechanism, not demonstrated improvement of future capacity, weight learning, reflective self-representation, autonomous theory construction or self-improvement. None of those properties is inferred from another. Unassessed shipped routes prevent system-wide negatives; absent execution and comparison evidence prevents benefit and causal attribution. This report assigns no single epistemic status to CocoIndex.

## Shared records

### Components

#### EPI-CMP-llm-pair-resolver
Label: LlmPairResolver

Source-native wrapper configuration is symbolic Python state; provider inference is distributed-parametric and outside the repository's storage substrate. The resolver keeps a lazy Instructor client and memo fingerprint; returned decisions can enter CocoIndex memo storage. No counterpart after comparison with supplied runtime components: this endpoint is independently configured, not [RT-CMP-llm-model](runtime.md#rt-cmp-llm-model) or [RT-CMP-sentence-transformer-embedder](runtime.md#rt-cmp-sentence-transformer-embedder). SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py`.

Parameters change during operation: caller performs inference, not training; provider internals uninspected. Exact version pinned: no, arbitrary model string is supplied. Mutable endpoint can resolve to another model: permitted by model-string/provider configuration; actual resolution unobserved. The key includes model/entity_type/extra_guidance, not a weights digest (nor retries), so changed provider behavior behind an unchanged alias is not independently detected by this key.

> self._memo_key = _coco.memo_fingerprint((model, entity_type, extra_guidance))
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

> @_coco.fn(memo=True, logic_tracking="self")
> async def __call__(
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

### Operative objects

#### EPI-OBJ-chunk-text
Label: Chunk text

Part of: [RT-RTE-index-update](runtime.md#rt-rte-index-update)

Material natural-language data part of the supplied production route, not a duplicate route. Stored as Python Chunk text in processing and as text fields in the supplied PostgreSQL index route; symbolic offsets preserve selected-span lineage. Truth aptitude depends on source contents, not the string type. SRC-1 `python/cocoindex/ops/text.py`; closest supplied consumer is [RT-RTE-query-index](runtime.md#rt-rte-query-index).

> chunk_text = text[raw.start_char_offset : raw.end_char_offset]
> --- `python/cocoindex/ops/text.py`

#### EPI-OBJ-module-info
Label: ModuleInfo

Part of: [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction)

Material output object within that supplied route, not a second extraction route. Natural-language title/descriptions and symbolic API names/lists are held in a typed Python object; the candidate is serialized to JSON and fields in a PostgreSQL ModuleRecord, with memoized extraction reuse. These parts share a schema gate but no inspected independent source-support check. SRC-1 `examples/manuals_llm_extraction/main.py`.

> class ModuleInfo(pydantic.BaseModel):
>     title: str
>     description: str
>     classes: list[ClassInfo] = pydantic.Field(default_factory=list)
>     methods: list[MethodInfo] = pydantic.Field(default_factory=list)
> --- `examples/manuals_llm_extraction/main.py`

#### EPI-OBJ-module-counts
Label: ModuleRecord counts

Part of: [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction)

Separate symbolic integer fields in Python row construction and PostgreSQL storage. Unlike the extracted descriptions, their relation to their immediate input lists is checked by inspection of len calls; they do not independently certify manual completeness. This object is not the ModuleInfo lists themselves. SRC-1 `examples/manuals_llm_extraction/main.py`.

> num_classes=len(info.classes),
> num_methods=len(info.methods),
> --- `examples/manuals_llm_extraction/main.py`

#### EPI-OBJ-pair-decision
Label: PairDecision

Symbolic matched identifier/null and canonical-side enum in Python, interpreted as entity-identity assertion plus naming policy. Model response is converted to PairDecision, memoized per pair and consumed by canonical-map construction; transient events can expose the raw decision. Empty PairDecision after exhausted invalid-output retries is a conservative operational fallback, not evidence that no candidate denotes the same entity. No counterpart after comparison with [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction): its ModuleInfo is a different candidate/domain. SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py`, `python/cocoindex/ops/entity_resolution/__init__.py`.

> return _PairDecision(matched=result.matched, canonical=result.canonical)
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

#### EPI-OBJ-check-exit
Label: MYPY_EXIT and BUILD_EXIT

Symbolic process-status integers and associated diagnostic text held transiently in shell/stdio, not retained epistemic records. Both have the same shell disposition, but distinct check domains described in the routes. No counterpart after comparison with [RT-RTE-index-update](runtime.md#rt-rte-index-update): these are contributor checks, not update/target results. SRC-1 `.claude/hooks/py-typecheck-run.sh`, `.claude/hooks/docs-build-run.sh`.

> MYPY_EXIT=$?
> if [ $MYPY_EXIT -ne 0 ]; then
>   echo "mypy typecheck failed" >&2
>   exit 2
> fi
> --- `.claude/hooks/py-typecheck-run.sh`

### Routes

#### EPI-RTE-chunk-slice
Label: Chunk text slicing

Part of: [RT-RTE-index-update](runtime.md#rt-rte-index-update)

Python _convert_chunk owns conversion from a core span and source text into Chunk. This is the slicing part of the index-production route. Implementation deduction, not execution: given text `A is B.\nC is D.` and raw character offsets 0 and 7, Python slicing yields `A is B.`. It neither generates a new assertion nor checks whether A is B. For a span crossing sentence boundaries, source-context warrant can degrade despite exact characters. Offset choice is an upstream condition, not proved by this example. SRC-1 `python/cocoindex/ops/text.py`.

- Immediate return: Chunk containing the source slice plus positional metadata.
- Later read-back: The text example retains chunk text in PostgreSQL for later query; see [RT-RTE-index-update](runtime.md#rt-rte-index-update).
- Delegated visibility: Conversion receives source text and raw byte/character/line offsets.
- Selection predicate: Core-supplied start/end character offsets.
- Invalidation or expiry: inapplicable — this conversion has no independent expiry; upstream processing determines replacement.
- Activation or effect: Sliced text is returned to split consumers; downstream index delivery is wired, not observed.
- Evidence limits: No Rust splitter correctness proof, actual chunk trace or truth assessment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return [_convert_chunk(c, source_text) for c in raw_chunks]
> --- `python/cocoindex/ops/text.py`

#### EPI-RTE-module-check
Label: ModuleInfo validation

Part of: [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction)

The schema-checking subroute within the supplied extraction route passes result.model_dump() through ModuleInfo.model_validate. Pydantic is the evaluator of typed structure; the manual is not an argument to this final check. Invalid shape can stop progression; valid shape is returned to process_file. The model proposes, code decides operational continuation, and no per-content human veto or expected-answer oracle is present at this call. This is open extraction, not an improvement experiment. Caller can change source/prompt/model and rerun; no semantic rollback is implemented here. SRC-1 `examples/manuals_llm_extraction/main.py`.

- Immediate return: Validated ModuleInfo, or validation exception.
- Later read-back: Returned result participates in memoized extract_module and later row persistence through the parent route.
- Delegated visibility: Validator receives dumped fields, not the original manual as evidence.
- Selection predicate: Every successful completion result reaching the return statement.
- Invalidation or expiry: Parent memo/change tracking; no semantic expiry in this check.
- Activation or effect: Shape-valid objects return for row construction; exceptions interrupt this path.
- Evidence limits: Pydantic/Instructor internals uninspected; no factual support checked by this statement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return ModuleInfo.model_validate(result.model_dump())
> --- `examples/manuals_llm_extraction/main.py`

#### EPI-RTE-module-count
Label: ModuleRecord list counting

Part of: [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction)

process_file derives cardinalities from returned lists, then constructs a ModuleRecord. This is the deterministic counting part, not the model-extraction proposal or its admission gate. For input classes=[one class] and methods=[], the two len calls yield 1 and 0. No execution is required for this implementation deduction. The premise is the extracted lists, not a warranted assertion that they exhaust the source manual; class methods are not added to num_methods. SRC-1 `examples/manuals_llm_extraction/main.py`.

- Immediate return: Integer fields inside ModuleRecord.
- Later read-back: Declared counts persist with the PostgreSQL row; downstream consumer for this example uninspected.
- Delegated visibility: Counter receives info.classes and info.methods.
- Selection predicate: All returned extraction objects passing to row construction.
- Invalidation or expiry: Parent process_file memo/reprocessing, not an independent count expiry.
- Activation or effect: Counts enter table.declare_row automatically with the other fields.
- Evidence limits: Only list-size derivation established; external writes and manual completeness unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> module_info=json.dumps(info.model_dump()),
> --- `examples/manuals_llm_extraction/main.py`

#### EPI-RTE-pair-proposal
Label: Pair resolution proposal

LlmPairResolver builds system/user messages from entity name, candidates, entity-type scope and extra guidance, then requests structured inference. Code owns progression; the provider proposes identity and canonical preference. Distinct from the closest supplied route, [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), which has different inputs, outputs and consumer. The fixed prompt guides identity resolution and asks uncertainty to favor null. The operator configures model/guidance, not per-pair approval. Open resolution requests have no independently supplied expected-answer oracle. SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py`; model limits are see [EPI-CMP-llm-pair-resolver](#epi-cmp-llm-pair-resolver).

- Immediate return: Proposed structured match/null and canonical side passed into validation.
- Later read-back: The decorated resolver memoizes returned PairDecision across runs, not proof that a call occurred.
- Delegated visibility: Provider receives entity/candidate names, system scope/guidance and retry messages, not authenticated entity records.
- Selection predicate: Invocation by caller with entity and candidate list.
- Invalidation or expiry: Memo key tracks model/scope/guidance; alias drift not independently tracked.
- Activation or effect: Proposal is consumed by contract checking, then map policy if valid.
- Evidence limits: No provider trace, semantic identity oracle or measured accuracy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> If you are unsure whether two names refer to the same thing, err on the side \
> of `matched` being null.
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

#### EPI-RTE-pair-check
Label: Pair decision contract

Distinct from the closest supplied route, [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction): this operation checks entity-resolution responses, not manual schema. There are two linked contract guards: the built-in LLM wrapper checks membership and retries invalid identifiers with specific feedback; the generic entity engine additionally rejects matching the entity to itself. These are finite-string checks. The evaluator is code; it can veto invalid identifiers but cannot veto a factually false identity match that satisfies the interface. The retry loop appends the invalid assistant response and corrective user message to the current request, adapting context within this call; no revised method is retained. At exhaustion of this particular invalid-output exception, wrapper code returns empty PairDecision, not a propagated invalid match. Provider failures have other semantics. The source names retries=2 by default; an active deadline can stop sooner. No independent answer oracle or improvement experiment. SRC-1 `python/cocoindex/ops/entity_resolution/llm_resolver.py`, `python/cocoindex/ops/entity_resolution/__init__.py`.

- Immediate return: Valid PairDecision, empty decision on exhausted invalid-output retries, or error including generic ValueError.
- Later read-back: Accepted resolver return may be memoized; current retry messages are not shown retained for future prompts.
- Delegated visibility: Checker receives matched value, candidates and, in generic guard, entity name.
- Selection predicate: Each proposed decision; only invalid-output exception selects this wrapper retry.
- Invalidation or expiry: Current-call message accumulation ends with call; memo invalidation follows wrapper fingerprint.
- Activation or effect: Invalid choices alter retry prompt; generic contract failure blocks map application.
- Evidence limits: Membership and self-exclusion do not establish identity truth; no observed retry or success.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if result.matched is None or result.matched in candidates:
>                 return _PairDecision(matched=result.matched, canonical=result.canonical)
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

> messages.append({"role": "assistant", "content": result.model_dump_json()})
> messages.append({"role": "user", "content": feedback})
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

> except _InvalidModelOutput:
>             # Exhausted the cap without a valid answer: keep the public
>             # contract of returning an empty decision instead of raising.
>             return _PairDecision()
> --- `python/cocoindex/ops/entity_resolution/llm_resolver.py`

> decision.matched not in candidates or decision.matched == entity
> --- `python/cocoindex/ops/entity_resolution/__init__.py`

#### EPI-RTE-pair-disposition
Label: Canonical decision application

Distinct from the closest supplied route, [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction): _apply_pair_decision and _new_wins dispose a checked identity proposal under canonical policy, not a manual record. resolve_entities calls validation before application, inserts/repoints names and returns ordered ResolvedEntities. PINNED seeds existing canonicals without consulting resolver; PREFERRED favors an existing name when only one side is existing. Thus operational naming authority is not entirely the model's. This is not evidence-consuming acceptance of identity truth: model judgment plus contract validity permits map mutation. Caller authors policy and can replace resolver or rerun, but no human per-pair gate is implemented here. No expected-answer oracle, bounded improvement objective or demonstrated rollback; exceptions cancel pending sibling tasks and completed events may still be delivered. SRC-1 `python/cocoindex/ops/entity_resolution/__init__.py`.

- Immediate return: Canonical-map mutation; outer resolve_entities returns ResolvedEntities.
- Later read-back: inapplicable — map is returned in current invocation; downstream persistence is not inspected here.
- Delegated visibility: Application receives entity info, checked PairDecision, current map and existing-canonical policy.
- Selection predicate: Policy and decision.matched/canonical determine new canonical, alias or repoint.
- Invalidation or expiry: inapplicable — current returned map has no independent expiry in this function.
- Activation or effect: Canonical map and events change; returned identities can govern caller behavior, but later graph consumer uninspected.
- Evidence limits: Policy application inspected, not real-world identity correctness, full candidate coverage or observed use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> dedup[info.name] = matched
>     return _DecisionApplication(canonical=matched)
> --- `python/cocoindex/ops/entity_resolution/__init__.py`

> if existing_policy == ExistingCanonicalPolicy.PINNED:
>         if matched_info.is_existing:
>             return False
>         return decision.canonical == CanonicalSide.NEW
> --- `python/cocoindex/ops/entity_resolution/__init__.py`

#### EPI-RTE-contributor-check
Label: Contributor type and docs checks

Registered PostToolUse Edit/Write hooks flag Python/pyi or docs changes. Stop hooks consume those flags and invoke portable scripts: uv run mypy for Python, npm dependency preparation and npm run build for docs. Check target is current workspace type/build compatibility, not truth of indexed assertions. Distinct from the closest supplied route, [RT-RTE-index-update](runtime.md#rt-rte-index-update): these contributor checks do not mediate the indexing API. Human/agent proposes edits, configured check code judges, and host/caller retains recovery through editing and rerunning; no production rollback or answer oracle is provided. Dependency tools' own semantics are outside this inspection. SRC-1 `.claude/settings.json`, `.claude/hooks/py-typecheck-flag.sh`, `.claude/hooks/docs-build-check.sh`, `dev/agent-checks/py-typecheck-run.sh`, `dev/agent-checks/docs-build-run.sh`.

- Immediate return: Process exit and diagnostic output.
- Later read-back: inapplicable — scripts do not retain a checked claim for later epistemic reliance.
- Delegated visibility: Checkers receive current workspace source/config and installed dependencies, not production row evidence.
- Selection predicate: Hook registration plus matching edit path and pending flag; portable scripts are also independently callable.
- Invalidation or expiry: Flags removed by Stop wrapper before checks; dependency lock timestamps govern docs installation.
- Activation or effect: Check processes return results to wrappers; no actual check run supplied.
- Evidence limits: Host/dependency internals and success not inspected; docs dependency setup can fail before build.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> uv run mypy 2>&1
> --- `dev/agent-checks/py-typecheck-run.sh`

> npm run build 2>&1
> --- `dev/agent-checks/docs-build-run.sh`

#### EPI-RTE-hook-result
Label: Contributor hook result signal

Distinct disposition from executing checks: shell wrappers translate nonzero check status into stderr and exit 2; zero status returns 0. Distinct from the closest supplied disposition, [RT-RTE-preview-update](runtime.md#rt-rte-preview-update): hook signaling neither plans nor applies index target actions. The flag is removed before the check runs, so consuming it is not a persisted acceptance record and does not guarantee automatic recheck after failure without another flag trigger. Host receives the signal; host retry/blocking semantics are uninspected, so no enforced host veto is asserted. Neither successful build nor types grant factual authority to indexed content. SRC-1 `.claude/hooks/py-typecheck-run.sh`, `.claude/hooks/docs-build-run.sh`.

- Immediate return: Hook exit 2 with failure message or exit 0.
- Later read-back: inapplicable — flag deletion and ephemeral status are not a durable evidence-consuming acceptance ledger.
- Delegated visibility: Host receives hook status/stderr; wrapper sees underlying check exit.
- Selection predicate: Pending flag selects check; nonzero status selects failure signal.
- Invalidation or expiry: Pending flag removed before check; later matching edit must set it again for hook-triggered recheck.
- Activation or effect: Failure signal reaches configured hook channel; host operational enforcement uninspected.
- Evidence limits: No observed host continuation, rejection, release gate or semantic content evaluation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> rm -f "$FLAG"
> 
> "$CLAUDE_PROJECT_DIR/dev/agent-checks/docs-build-run.sh"
> BUILD_EXIT=$?
> if [ $BUILD_EXIT -ne 0 ]; then
>   echo "docs build failed" >&2
>   exit 2
> fi
> --- `.claude/hooks/docs-build-run.sh`

### Claims

#### EPI-CLM-fresh-context
Label: Fresh context

Public claim that context is continuously fresh and reliable for agents. No counterpart after comparison: supplied runtime Claims declares none; the closest supplied mechanism is [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance). SRC-1 `README.md`, doctrine/design, not observed operation or an independently established truth guarantee. The relevant maintenance/retrieval routes are [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance) and [RT-RTE-query-index](runtime.md#rt-rte-query-index); no quantified reliability conclusion follows.

> Get your production AI agent ready in 10 minutes with reliable, continuously fresh data — no stale batches, no context gap
> --- `README.md`

#### EPI-CLM-supported-extraction
Label: Source-supported extraction

Part of: [RT-BAP-extraction-prompt](runtime.md#rt-bap-extraction-prompt)

The specific fidelity criterion inside the supplied behavioral-authority path, not a new prompt or duplicate path. Source-native extraction instruction requests content support by the manual, alongside specified summary/API fields. SRC-1 `examples/manuals_llm_extraction/main.py`, doctrine/design. Its existence licenses a claim about what is asked, not compliance; the route checks typed shape as [EPI-RTE-module-check](#epi-rte-module-check).

> "module-level functions (with their arguments). Use only what the text supports."
> --- `examples/manuals_llm_extraction/main.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
