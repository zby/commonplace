---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "QwenPaw epistemic routes: imported evidence, memory maintenance, relevance checks and the limits of reliance at the frozen revision."
run-id: AAS-2026-10-15-qwenpaw-e41495d47fc0-01
reviewed-boundary: "16b2e712d198166c9359e77055b13bf2668bf5ae"
---

# QwenPaw epistemic report

## Source-and-claim boundary

This report asks how QwenPaw acquires potential facts, transforms and retains them, checks candidates and permits later reliance. The frozen whole-system scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All direct reads below are SRC-1 implementation evidence unless marked doctrine/design. No target execution, supplied run trace or causal comparison is available. A route being wired establishes neither a particular candidate nor successful use.

The material routes include answers and tool evidence; memory search and relevance ranking; automatic/manual conversation extraction; dream and Daily Paper jobs; caller-authored memory and instructions; context compression; execution permission; installation; and destructive cleanup. Opaque alternatives stay in scope, with limits below. The principal knowledge claim is [EPI-CLM-never-forgets](#epi-clm-never-forgets). The memory-writing instruction is [EPI-CLM-preserve-valid](#epi-clm-preserve-valid). Wider product/security claims remain [RT-CLM-assistant-work](runtime.md#rt-clm-assistant-work) and [RT-CLM-security-built](runtime.md#rt-clm-security-built).

### Coverage

| Entry point or operation | Source path, SRC-1 | Coverage and records, or limit |
|---|---|---|
| CLI dispatch and destructive clean | `src/qwenpaw/cli/main.py`; `src/qwenpaw/cli/clean_cmd.py` | Direct reads of lazy-command registration and complete clean implementation: [EPI-RTE-clean-workspace](#epi-rte-clean-workspace). This is outside the normal turn lifecycle. |
| Native request, session load/save and answer | `src/qwenpaw/runtime/runtime.py`; `src/qwenpaw/hooks/session/session_hook.py`; `src/qwenpaw/runtime/builder.py` | Supplied findings: [RT-RTE-native-turn](runtime.md#rt-rte-native-turn), [RT-OBJ-session-state](runtime.md#rt-obj-session-state). AgentScope inner inference and correctness of generated answers remain uninspected. |
| Memory middleware, reply/compression flush and query injection | `src/qwenpaw/agents/middlewares.py` | Direct read of model-call/reply/compression paths and batch flush: [EPI-RTE-memory-search](#epi-rte-memory-search), [EPI-RTE-auto-memory](#epi-rte-auto-memory). Complete cache-helper and retry algorithms not audited. |
| Registered tools | `src/qwenpaw/agents/tools/__init__.py`; `src/qwenpaw/agents/memory/reme_light_memory_manager.py` | Direct import registry and ReMe memory-tool registration inspected. Web tools directly read: [EPI-RTE-web-acquisition](#epi-rte-web-acquisition). File/shell, visual/browser, AST, mail, external delegation and driver tool internals are not all inspected; this prevents a complete inventory of their domain-specific evaluators. |
| Memory search and optional reranker | `src/qwenpaw/agents/memory/reme_light_memory_manager.py` | Direct public search, automatic search, reorder/cap and API code: [EPI-RTE-rerank-check](#epi-rte-rerank-check), [EPI-RTE-rerank-selection](#epi-rte-rerank-selection). Answer-section reconstruction helpers not fully inspected; complete lineage preservation after fallback reconstruction remains unresolved. |
| `/memorize`, `/dream` and maintenance crons | `src/qwenpaw/runtime/builtin_commands.py`; `src/qwenpaw/agents/command_handler.py`; `src/qwenpaw/agents/memory/reme_light_memory_manager.py`; `src/qwenpaw/agents/memory/reme_config.py` | Direct conversation-command registration, handlers, adapter dispatch and configured jobs: [EPI-RTE-auto-memory](#epi-rte-auto-memory), [EPI-RTE-dream-dispatch](#epi-rte-dream-dispatch), [EPI-RTE-paper-dispatch](#epi-rte-paper-dispatch). ReMe backend steps are external; configured step names are not inspected implementations. |
| Synthetic search removal before extraction | `src/qwenpaw/agents/memory/base_memory_manager.py`; `src/qwenpaw/agents/memory/reme_light_memory_manager.py` | Direct: [EPI-RTE-search-exclusion](#epi-rte-search-exclusion). This narrows any claim that memory extraction simply consumes all prior context. |
| Workspace memory API | `src/qwenpaw/app/routers/workspace.py`; `src/qwenpaw/agents/memory/agent_md_manager.py` | Direct memory PUT and writer: [EPI-RTE-memory-file](#epi-rte-memory-file). Generic callers do not establish human content review. |
| Prompt transformation and later consumption | `src/qwenpaw/runtime/prompt_contributors.py` | Direct helper reads; supplied write/consumer findings: [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction), [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt). Marked memory sections can be replaced, not simply passed through verbatim. |
| Checkpoint restoration and GC/reset commands | `src/qwenpaw/runtime/commands/control/checkpoint_handler.py` | Direct targeted handler reads/search: [EPI-RTE-checkpoint-restore](#epi-rte-checkpoint-restore). Restore engine internals not inspected; prevents a complete rollback-atomicity or revived-content lineage account. GC is checkpoint cleanup, not proof of semantic withdrawal. |
| Governance, plugin admission, harness turns and forked work | `src/qwenpaw/governance/tool_adapter.py`; `src/qwenpaw/plugins/loader.py`; `src/qwenpaw/harnesses/runtime.py`; `src/qwenpaw/agents/tools/agent_management.py` | Supplied [RT-RTE-tool-governance](runtime.md#rt-rte-tool-governance), [RT-RTE-plugin-install](runtime.md#rt-rte-plugin-install), [RT-RTE-harness-turn](runtime.md#rt-rte-harness-turn), [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker). Inner harness evaluation and all merge gates remain unresolved. |
| Working-window compression/recovery | `src/qwenpaw/agents/context/scroll/manager.py`; `src/qwenpaw/agents/react_agent.py` | Supplied [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery). Summary semantics, all recall transformations and native dependency compaction remain uninspected. |
| Other included paths | Boundary coverage table; alternative `src/qwenpaw/agents/memory/adbpg_memory_manager.py`, skills/scanners, MCP, plugins, backup and tests | Available but uninspected in this member beyond cited supplied findings. Prevents system-complete absence of factual checking, criticism, acceptance or withdrawal. External dependency internals and live/model/user artifacts are unavailable, not merely unread files. |

## Epistemic-object inventory

These are candidate classes, not observed candidate instances. The object records own form, storage and provenance; rows here do not re-declare them.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-search-results](#epi-obj-search-results) | see record | memory results | see record | see record |
| [EPI-OBJ-rerank-order](#epi-obj-rerank-order) | none; selection indices | relevance order | see record | see record |
| [EPI-OBJ-daily-notes](#epi-obj-daily-notes) | see record | conversation memory | see record | see record |
| [EPI-OBJ-dream-units](#epi-obj-dream-units) | see record | merged digest units | see record | see record |
| [EPI-OBJ-paper-brief](#epi-obj-paper-brief) | see record | paper readings and brief | see record | see record |
| [EPI-OBJ-web-results](#epi-obj-web-results) | see record | external text | see record | see record |
| [RT-OBJ-session-state](runtime.md#rt-obj-session-state) | see record | saved context | see record | see record |
| [RT-OBJ-prompt-files](runtime.md#rt-obj-prompt-files) | see record | selected prompt bodies | see record | see record |

The active inference and alternative-harness parameters are separate from these text and symbolic objects: see [RT-CMP-active-model](runtime.md#rt-cmp-active-model), [RT-CMP-harness-model](runtime.md#rt-cmp-harness-model). The optional relevance endpoint is [EPI-CMP-reranker-api](#epi-cmp-reranker-api). Neither endpoint configuration nor a model name establishes exact weights or an in-operation parameter update.

## Authority-route ledger

Each compact entry gives this member's architectural judgment. Other fields are owned by the cited record; `see` imports its bounded account, not a new declaration. Checked results, their disposition, retention and use are separate functions even when implemented by one method.

Route ID: [RT-RTE-native-turn](runtime.md#rt-rte-native-turn)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see record and [RT-OBJ-session-state](runtime.md#rt-obj-session-state).
Content/update relation: truth-apt transformation: indeterminate. Without actual outputs, factual acquisition, entailed reformulation and non-entailed generation cannot be separated for a particular answer.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record. Open-request completion is not a truth verdict.

Route ID: [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs or none; mismatch marker or none; gap/limit: see record.

Route ID: [EPI-RTE-memory-search](#epi-rte-memory-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [EPI-RTE-rerank-check](#epi-rte-rerank-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [EPI-RTE-rerank-selection](#epi-rte-rerank-selection)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record. Disposition here admits an ordering, not the truth of selected text.

Route ID: [EPI-RTE-search-exclusion](#epi-rte-search-exclusion)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [EPI-RTE-auto-memory](#epi-rte-auto-memory)
Route function: retention
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record. The implemented portion is dispatch to extraction, not independently inspected semantic acceptance or every external write.

Route ID: [EPI-RTE-dream-dispatch](#epi-rte-dream-dispatch)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record. Implemented dispatch is narrower than the declared integration backend.

Route ID: [EPI-RTE-paper-dispatch](#epi-rte-paper-dispatch)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [EPI-RTE-memory-file](#epi-rte-memory-file)
Route function: retention
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see record and [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt).
Content/update relation: non-truth-apt policy/content update: caller changes instructions; factual material may coexist, but its truth is not checked by the write acknowledgement. Epistemic authority: no factual license established. Claim IDs: [EPI-CLM-preserve-valid](#epi-clm-preserve-valid). Mismatch marker: none for the bounded write claim.

Route ID: [RT-RTE-tool-governance](runtime.md#rt-rte-tool-governance)
Route function: check/evidence production
Architectural status: implemented
Transition or check target: proposed tool call against configured permission policy, not truth of a proposed answer. Evaluator/condition and domain; activation and timing; possible result; evidence source ID and local anchor; gaps: see record.
Content/update relation: no content change. Object/candidate: proposed tool call, see record. Implemented force; operational authority and behavioral-authority path: see record; decision is consumed by permission machinery. Epistemic authority: policy eligibility only, not factual validity. Claim IDs: [RT-CLM-security-built](runtime.md#rt-clm-security-built). Mismatch marker: conditional coverage, see record.

Route ID: [RT-RTE-tool-governance](runtime.md#rt-rte-tool-governance)
Route function: disposition/acceptance
Architectural status: implemented
Transition or check target: permission result to execute, deny or ask. Evaluator/condition and domain; timing; result; force; operational authority; behavioral-authority path; evidence and limits: see record. Content/update relation: no content change. Object/candidate: see record. Epistemic authority: permission is not content acceptance. Claim IDs: [RT-CLM-security-built](runtime.md#rt-clm-security-built). Mismatch marker: OFF, unsandboxed fallback and external enforcement limits, see record.

Route ID: [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID; activation and timing; possible result; implemented force; operational authority; behavioral-authority path; evidence and gap/limit: see record.
Content/update relation: truth-apt transformation: indeterminate for model summaries; symbolic pointer/retry changes do not establish semantic preservation. Transition/check target: working-context fit and durability, not factual truth. Evaluator/condition and domain: see record. Epistemic authority: recoverability/fit does not license summary accuracy. Claim IDs: [EPI-CLM-never-forgets](#epi-clm-never-forgets). Mismatch marker: losslessness unestablished.

Route ID: [EPI-RTE-checkpoint-restore](#epi-rte-checkpoint-restore)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [EPI-RTE-clean-workspace](#epi-rte-clean-workspace)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID; content/update relation; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; claim IDs; mismatch marker; gap/limit: see record.

Route ID: [RT-RTE-plugin-install](runtime.md#rt-rte-plugin-install)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; timing; results; force; operational authority; behavioral-authority path; evidence and limits: see record and [RT-BAP-plugin-backend](runtime.md#rt-bap-plugin-backend).
Content/update relation: non-truth-apt policy/content update: executable capabilities and application registrations. Epistemic authority: structural/compatibility checks do not establish behavioral quality. Claim IDs: [RT-CLM-assistant-work](runtime.md#rt-clm-assistant-work). Mismatch marker: none for extensibility; no evidence-responsive improvement or content-truth acceptance inferred.

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant and source layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|
| [EPI-CLM-never-forgets](#epi-clm-never-forgets) | see record | see record | [EPI-RTE-auto-memory](#epi-rte-auto-memory), [EPI-RTE-dream-dispatch](#epi-rte-dream-dispatch), [EPI-RTE-memory-search](#epi-rte-memory-search), [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery), [EPI-RTE-clean-workspace](#epi-rte-clean-workspace) | see record | see record | see record | see record |
| [EPI-CLM-preserve-valid](#epi-clm-preserve-valid) | see record | see record | [EPI-RTE-memory-file](#epi-rte-memory-file), [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction) | see record | see record | see record | see record |
| [RT-CLM-assistant-work](runtime.md#rt-clm-assistant-work) | see record | see record | [RT-RTE-native-turn](runtime.md#rt-rte-native-turn), [RT-RTE-plugin-install](runtime.md#rt-rte-plugin-install) | see record | see record | see record | see record |
| [RT-CLM-security-built](runtime.md#rt-clm-security-built) | see record | see record | [RT-RTE-tool-governance](runtime.md#rt-rte-tool-governance), [RT-RTE-harness-turn](runtime.md#rt-rte-harness-turn) | see record | see record | see record | see record |

## Bounded conclusion

QwenPaw supplies several distinct routes to later reliance, not one epistemic gate. Saved conversations and configured instruction files can reach later inference; neither serialization nor instruction delivery accepts their factual contents ([RT-OBJ-session-state](runtime.md#rt-obj-session-state), [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt)). Web tools import external text, and memory search supplies selected retained text; source truth is unknown rather than newly warranted by retrieval ([EPI-RTE-web-acquisition](#epi-rte-web-acquisition), [EPI-RTE-memory-search](#epi-rte-memory-search)).

The optional reranker evaluates query relevance from truncated snippet text. A permutation check accepts an ordering for retrieval, not propositions for belief. A concrete code deduction shows that dropping a result is selection, not refutation ([EPI-RTE-rerank-check](#epi-rte-rerank-check), [EPI-RTE-rerank-selection](#epi-rte-rerank-selection)). Governance separately evaluates action permission. Its denial can stop an action but says nothing about whether the proposed answer is true ([RT-RTE-tool-governance](runtime.md#rt-rte-tool-governance)). These checks have implemented force in their own domains without furnishing an answer oracle.

Automatic and manual extraction submit conversation batches to ReMe. Synthetic recall is deliberately removed first, which protects one provenance boundary but does not validate the remaining user/model/tool claims ([EPI-RTE-search-exclusion](#epi-rte-search-exclusion)). Dream and paper workflows configure extraction, merging, ranking, analysis and digest stages. QwenPaw dispatch and inbox reporting are implemented; opaque backend labels and successful completion do not establish factual acceptance or lifecycle integration after acceptance ([EPI-RTE-auto-memory](#epi-rte-auto-memory), [EPI-RTE-dream-dispatch](#epi-rte-dream-dispatch), [EPI-RTE-paper-dispatch](#epi-rte-paper-dispatch)). Particular outputs, premise warrant, entailment, non-entailment and criticism remain unestablished without backend/instance evidence. There is no evidenced accepted ampliative claim in the inspected routes; this is not a system-complete architectural absence.

Memory PUT permits caller-authored replacement before any demonstrated semantic review. Cleanup can destroy retained state without testing its validity; checkpoint selection can request earlier state without endorsing its truth ([EPI-RTE-memory-file](#epi-rte-memory-file), [EPI-RTE-clean-workspace](#epi-rte-clean-workspace), [EPI-RTE-checkpoint-restore](#epi-rte-checkpoint-restore)). “Never forgets” therefore supports a layered retention design, not invariant preservation or truth-maintaining self-evolution ([EPI-CLM-never-forgets](#epi-clm-never-forgets)).

Parameter learning is unresolved at external endpoints. Retained context can shape later action without parameter updates. Improved capacity, content-directed theory criticism, reflective feedback, autonomous theory construction and exercised self-improvement require independent evidence; neither model opacity nor the absence of supplied runs proves those properties absent. The supplied plugin/instruction routes establish behavior-changing affordances, not evidence-responsive improvement or successful benefit. Uninspected skills, domain tools, alternative backends and dependency evaluators prevent a universal negative. No system-wide score follows.

## Shared records

### Components

#### EPI-CMP-reranker-api
Label: Optional reranker API

Source-native identity: `RerankerConfig`, `config.model_name`, `config.base_url`. Representational form: opaque external relevance model behind symbolic HTTP configuration; any distributed-parametric weights are not supplied. Storage substrate: external service. Parameters changing during operation: uninspected; API requests expose no weight updates. Exact version pinned: not established by the configured model name. Mutable endpoint resolving to another model: not excluded; endpoint and model are configuration values. Distinct from [RT-CMP-active-model](runtime.md#rt-cmp-active-model) and [RT-CMP-harness-model](runtime.md#rt-cmp-harness-model): it returns relevance indices, not native/harness replies. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation).

> payload: dict[str, Any] = {
>     "model": config.model_name,
>     "query": query,
>     "documents": documents,
> }
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

### Operative objects

#### EPI-OBJ-search-results
Label: Memory search results

Source-native identity: search `response.answer`, `response.metadata["results"]`. Natural-language snippets and answer sections, with symbolic result locations/scores; substrate is the returned ReMe response and current model input. Candidate factual contents concern past work, decisions, dates, people, preferences and todos, as the tool contract specifies. No concrete truth-valued instance supplied. Imported retained content has unknown original warrant; paths and line numbers can identify locations without validating contents. Distinct from [RT-OBJ-session-state](runtime.md#rt-obj-session-state): search reads the memory corpus rather than restoring the whole agent snapshot. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation and tool doctrine).

> Use this tool before answering questions about prior work,
> decisions, dates, people, preferences, or todos. Returns top
> relevant snippets with file paths and line numbers.
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

#### EPI-OBJ-rerank-order
Label: Reranker result ordering

Source-native identity: `new_order`, `ordered`. Symbolic index list in transient Python/HTTP response state, not truth-apt factual content. Used to permute result objects. Distinct from search snippets and from all supplied runtime objects: ordering metadata is not an answer or saved session. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation); evidence in [EPI-RTE-rerank-check](#epi-rte-rerank-check) and [EPI-RTE-rerank-selection](#epi-rte-rerank-selection).

#### EPI-OBJ-daily-notes
Label: Conversation-derived daily notes

Source-native identity: `auto_memory`, daily note output. Intended natural-language conversation facts in Markdown daily storage under configured ReMe local files. Symbolic session identity accompanies dispatch. Actual note text, write success, premise lineage and changes of meaning are not supplied. Claimed facts could include factual user reports and model assertions, not automatically warranted premises. Distinct from [RT-OBJ-session-state](runtime.md#rt-obj-session-state): extracted daily notes are not the serialized context container. SRC-1, `src/qwenpaw/agents/memory/reme_config.py` (doctrine/design of external job), `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation dispatch).

> "Auto-memory: record conversation facts into a daily "
> "note"
> --- `src/qwenpaw/agents/memory/reme_config.py`

#### EPI-OBJ-dream-units
Label: Dream digest units and interests

Source-native identity: `auto_dream`, digest units, `interests.yaml`, dream catalog. Intended natural-language merged units/topics plus symbolic YAML/catalog metadata in configured local ReMe storage. Whether topics state propositions or only preference labels is not determinable without instances; factual digest units can be truth-apt. This is not the daily-note extraction output or any supplied runtime object. SRC-1, `src/qwenpaw/agents/memory/reme_config.py` (doctrine/design); external step internals uninspected.

> "Auto-dream: scan today's day-index and daily notes, "
> "globally extract merged units/topics, integrate digest "
> "units, write interests.yaml, and persist the dream "
> "catalog."
> --- `src/qwenpaw/agents/memory/reme_config.py`

#### EPI-OBJ-paper-brief
Label: Daily Paper readings and brief

Source-native identity: `daily_paper`, `digest_path`, `note_paths`, `pdf_paths`, `selected_arxiv_ids`. Intended natural-language paper readings/brief with symbolic artifact/source identifiers, in backend files and an inbox event. Potential paper claims are truth-apt; no paper, generated text or acceptance trace supplied. Distinct from daily conversation notes and all supplied runtime objects: resource-fed scheduled output with separate consumers and source lineage. SRC-1, `src/qwenpaw/agents/memory/reme_config.py` (doctrine/design), `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation dispatch/reporting).

> "Build detailed readings and a five-minute brief from "
> "Hugging Face weekly/monthly papers."
> --- `src/qwenpaw/agents/memory/reme_config.py`

#### EPI-OBJ-web-results
Label: Web search and fetched text

Source-native identity: web-search `results`, fetched `raw_html`, returned `text`. Natural-language imported snippets/page text in transient ToolChunk content; URLs and tool state are symbolic metadata. Potential external facts, not a witnessed candidate instance. Distinct from saved-session and prompt objects: fresh external acquisition. SRC-1, `src/qwenpaw/agents/tools/web_search.py` (implementation); passages in [EPI-RTE-web-acquisition](#epi-rte-web-acquisition).

### Routes

#### EPI-RTE-web-acquisition
Label: Web evidence acquisition

Part of: [RT-RTE-native-turn](runtime.md#rt-rte-native-turn)

A tool-mediated part of the native-turn route, not a duplicate whole request. Endpoints: proposed search/fetch → configured search provider or HTTP HTML fetch → formatted snippets or converted readable text → ToolChunk → agent. Owner: tool implementation plus external provider/HTML converter. SRC-1, `src/qwenpaw/agents/tools/web_search.py` (implementation). Content/update relation: truth-apt transformation: acquisition/import, source warrant unknown. Neither syntactically valid URL nor SUCCESS assesses factual truth; no target-specific evidence-consuming content acceptance in this wrapper. Search and fetch are separate acquisition branches with the same immediate advisory consumer; search formatting/provider details remain uninspected. Behavior path: agent tool-result channel, advisory evidence for current/subsequent inference if retained. Claim IDs: none; mismatch marker: none.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted search snippets or converted page text; ERROR for empty/invalid input and caught fetch/provider exceptions.
- Later read-back: uninspected — tool wrappers do not themselves persist content; native session retention may include resulting messages.
- Delegated visibility: uninspected — no direct child handoff in these wrappers.
- Selection predicate: tool invocation; nonempty query; HTTP/HTTPS URL with hostname for fetch; search limits provider results to five.
- Invalidation or expiry: inapplicable — no durable object managed by the wrappers; freshness is the remote retrieval time, not endorsement.
- Activation or effect: tool text can enter current model input; factual reliance/compliance unobserved.
- Evidence limits: provider result quality, HTML conversion fidelity, source truth and successful execution not established.

> results = await provider.search(
>     query,
>     max_results=5,
> )
> text = format_search_results(results)
> --- `src/qwenpaw/agents/tools/web_search.py`

> raw_html = await _fetch_html(target)
> text = _html_to_text(raw_html)
> --- `src/qwenpaw/agents/tools/web_search.py`

#### EPI-RTE-memory-search
Label: Retrieved memory consumption

Distinct from [RT-RTE-native-turn](runtime.md#rt-rte-native-turn): includes separately callable memory tool and middleware-initiated acquisition from retained memory, rather than the whole native lifecycle. Endpoints: explicit query or latest external user query → ReMe search → optional reorder/cap → answer → tool result or injected completed interaction → model call. Owner: ReMe adapter and MemoryMiddleware. Object: [EPI-OBJ-search-results](#epi-obj-search-results). Content/update relation: truth-apt transformation: acquisition/import, original warrant unknown. Selection is query relevance, not factual acceptance. Operational authority: admit selected memory as advisory model evidence for the current user turn, not permission to execute a tool. Explicit call is foreground-requested; automatic search is independently initiated by middleware from the user query. Claim: [EPI-CLM-never-forgets](#epi-clm-never-forgets); mismatch marker: retrieval is neither completeness nor truth maintenance. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/middlewares.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: memory tool answer with response success, or automatic query/text/message structure used for injection; blank/unavailable/failed auto search can yield none.
- Later read-back: selected retained corpus content enters a later model invocation through search; source corpus extraction is separately bounded.
- Delegated visibility: uninspected — projections to every child/backend not traced.
- Selection predicate: explicit memory tool when enabled, or automatic search enabled and a new external-user turn; automation bypass in middleware; min-score/limit and optional reranker constrain delivery.
- Invalidation or expiry: middleware replaces cached search at a new user-turn marker; failures can retry; corpus expiry uninspected.
- Activation or effect: input messages are injected before next model handler; actual answer reliance unobserved.
- Evidence limits: opaque ReMe search, reconstruction helpers, recall quality and original source endorsement not established.

> if memory_msgs:
>     input_kwargs["messages"] = self._inject_search_messages(
>         list(input_kwargs.get("messages") or []),
>         memory_msgs=memory_msgs,
>         turn_marker=turn_marker,
>     )
> return await next_handler(**input_kwargs)
> --- `src/qwenpaw/agents/middlewares.py`

#### EPI-RTE-rerank-check
Label: Relevance and index checks

Distinct from [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery): checks memory-result ordering, not working-window fit. Endpoints: query and snippets → optional reranker endpoint → descending relevance index proposal → length/permutation condition. Owner: adapter; external model provides relevance, Python checks structural validity. Objects: [EPI-OBJ-search-results](#epi-obj-search-results), [EPI-OBJ-rerank-order](#epi-obj-rerank-order). Content/update relation: no content change. Check target/domain: relevance of first 500 characters per result to query; structural domain: permutation of `0..n-1`. A passing index check licenses only safe reordering without duplicate/missing indices at this stage. No factual license over full snippets. Result consumed by [EPI-RTE-rerank-selection](#epi-rte-rerank-selection), enforcing structural rejection before reorder; horizon one retrieval. No human decision, answer oracle or bounded improvement experiment. Claim IDs: none; mismatch marker: none. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposed indices or none; invalid count/permutation returns without replacement.
- Later read-back: inapplicable — transient check result has no independent persistence/reload route here.
- Delegated visibility: external reranker receives query and truncated snippets, not the full session.
- Selection predicate: configured reranker and more than one result; endpoint/query/documents must be present.
- Invalidation or expiry: inapplicable — one search evaluation, discarded after use.
- Activation or effect: valid ordering can pass to selection; invalid ordering leaves original order.
- Evidence limits: relevance model accuracy and full-document relevance unobserved; truth not a check target.

> texts: list[str] = [r.get("text", "")[:500] for r in results]
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> if set(new_order) != set(range(len(results))):
>     logger.warning(
>         "[rerank] API returned invalid indices (not a permutation): "
>         "%s for %d results — using original order",
>         new_order,
>         len(results),
>     )
>     return
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

#### EPI-RTE-rerank-selection
Label: Ranked result disposition

Distinct from supplied context-selection route [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery): consumes relevance ordering for retrieval delivery. Endpoints: checked ordering → reordered metadata → cap → reconstructed answer → explicit/automatic search consumer. Owner: adapter. Objects as in [EPI-RTE-rerank-check](#epi-rte-rerank-check). Content/update relation: truth-apt transformation: non-ampliative reshaping for reorder/cap of existing snippets; completeness is reduced by selection. Full reconstruction fidelity remains unresolved, not asserted. Criterion is structural validity for an ordering and configured count for delivery, not acceptance of facts. API proposes; Python can reject; no mandatory human approval. Open retrieval operation, no expected-answer oracle. Force: enforcing selection upstream of advisory model delivery. Epistemic authority: relevance preference only. Claim IDs: none; mismatch marker: none. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reordered/capped response, with answer rebuilt if order/count changes; original ordering on caught rerank failure.
- Later read-back: inapplicable — this does not itself retain an updated corpus or persistent relevance policy.
- Delegated visibility: inapplicable — disposition is local, not a worker handoff.
- Selection predicate: admitted ordering and cap; reconstruction uses parsed sections when available, raw metadata fallback otherwise.
- Invalidation or expiry: inapplicable — per-query result selection, not content expiry.
- Activation or effect: determines which snippets the downstream model can see in this retrieval.
- Evidence limits: no observed response, calibrated relevance benefit or factual acceptance; fallback answer fidelity unresolved.

Concrete implementation deduction, not execution: let result list be `[A,B,C]`, endpoint order `[2,0,1]`, cap `2`. The permutation check passes; indexing yields `[C,A,B]`; slicing delivers metadata `[C,A]`, after which the answer is reconstructed. `[2,2,0]` fails the set check and leaves original ordering before ordinary capping. Neither case evaluates the truth of A, B or C. A non-delivered B is not refuted or deleted from memory.

> reordered = [results[idx] for idx in new_order]
>
> response.metadata["results"] = reordered
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> truncated = len(results) > cap
> if truncated:
>     results = results[:cap]
>     response.metadata["results"] = results
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

#### EPI-RTE-search-exclusion
Label: Synthetic recall exclusion

Distinct from [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery): sanitizes extraction inputs, not a general live-context compactor. Endpoints: conversation messages → metadata-identified synthetic blocks removed → remaining messages → auto-memory queue. Owner: base memory helper and ReMe adapter. Content/update relation: truth-apt transformation: non-ampliative reshaping, removal rather than inference. Object: input messages that may contain [EPI-OBJ-search-results](#epi-obj-search-results). Criterion: symbolic block-ID membership, not truth or user endorsement. Operational authority: enforcing omission upstream of extraction; epistemic authority: avoids re-importing specifically tagged recall, not all circular provenance. No semantic acceptance. Claim IDs: none; mismatch marker: none. SRC-1, `src/qwenpaw/agents/memory/base_memory_manager.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: original message if no IDs; copied message with remaining blocks or none if all removed.
- Later read-back: surviving batch can feed extracted daily notes and later search; removed synthetic blocks do not enter through this batch.
- Delegated visibility: external extraction receives the sanitized messages, conditional on metadata tags being present.
- Selection predicate: message metadata synthetic-search block IDs; ReMe auto-memory applies the helper before enqueueing.
- Invalidation or expiry: copied message removes the synthetic-search metadata key; no source-corpus deletion.
- Activation or effect: determines extraction input; absence of tags does not prove content was never retrieved elsewhere.
- Evidence limits: only marked synthetic recall removed; no universal provenance de-duplication or factual check.

> kept_blocks = [
>     block
>     for block in msg.get_content_blocks()
>     if getattr(block, "id", "") not in block_ids
> ]
> if not kept_blocks:
>     return None
> --- `src/qwenpaw/agents/memory/base_memory_manager.py`

> all_messages = self._messages_without_auto_memory_search(all_messages)
> if not all_messages:
>     return
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

#### EPI-RTE-auto-memory
Label: Conversation extraction dispatch

Distinct from [RT-RTE-native-turn](runtime.md#rt-rte-native-turn): also manually callable via `/memorize`, crosses from conversation batches into external knowledge maintenance, and runs asynchronously. Endpoints: middleware reply-count/compression batch or manual selected reply groups → sanitized messages → serial summary queue → `auto_memory` job → declared daily notes. Owner: middleware/command handler, base worker and ReMe adapter; external ReMe owns extraction/write semantics. Object: [EPI-OBJ-daily-notes](#epi-obj-daily-notes). Content/update relation: truth-apt transformation: indeterminate; whether particular output preserves input meaning, entails a new proposition or conjectures needs actual input/output and backend inspection. Claim: [EPI-CLM-never-forgets](#epi-clm-never-forgets). SRC-1, `src/qwenpaw/agents/middlewares.py`, `src/qwenpaw/agents/command_handler.py`, `src/qwenpaw/agents/memory/base_memory_manager.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/memory/reme_config.py`.

Admission: middleware/handler select batches; generic command caller chooses count, not per-note approval. Model-backed external extraction is requested, not verified. Empty messages/session guard submission; interval can disable automatic batching; automation is skipped. Guidance includes memory hint and declared recording of conversation facts. No expected-answer oracle or content acceptance criterion established; open maintenance mode. Stored notes are intended for later search, but this report does not equate retention with post-acceptance integration. Job/worker completion indicates control flow, not acceptance of truth. Failure/retry state and inbox notifications are operational; full rollback of backend writes is uninspected. Mismatch marker: acknowledged/queued versus semantically accepted.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: manual command says started/messages submitted; summary worker records returned string/completed or failure; adapter may return empty when unavailable.
- Later read-back: declared daily notes are search inputs; actual backend persistence and note provenance are unobserved.
- Delegated visibility: ReMe gets serialized selected messages, session ID and hint; synthetic recall blocks are filtered separately.
- Selection predicate: valid session, nonempty messages; configured reply interval or compression flush; manual positive count and available reply groups.
- Invalidation or expiry: backend note revision/expiry uninspected; local pending markers/snapshots manage batching, not semantic withdrawal.
- Activation or effect: enqueues and dispatches extraction; produced notes, warranted facts and later behavioral use unobserved.
- Evidence limits: external extraction prompts/checks/writes and actual candidates not available; no inference of absent external evaluator.

> response = await self._run_reme_job(
>     "auto_memory",
>     needs_llm=True,
>     messages=[message.model_dump(mode="json") for message in messages],
>     session_id=_to_reme_session_id(session_id),
>     memory_hint=str(kwargs.get("memory_hint") or ""),
> )
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> result = await self.summarize(messages=messages, **kwargs)
> info["status"] = "completed"
> info["result"] = result
> --- `src/qwenpaw/agents/memory/base_memory_manager.py`

#### EPI-RTE-dream-dispatch
Label: Dream maintenance dispatch

Distinct from supplied native turn and context recovery: operates over day-index/daily notes for corpus maintenance rather than just the current window. Endpoints: enabled cron or `/dream` hint → adapter `auto_dream` → configured extract/integrate/topics/finish external steps → response/inbox. Owner: adapter and external ReMe. Object: [EPI-OBJ-dream-units](#epi-obj-dream-units). Content/update relation: truth-apt transformation: indeterminate; declarations of merging/integration do not settle semantics. Operational authority: request maintenance and expose result; declared changed/deleted paths can affect future corpus, but backend enforcement uninspected. Epistemic authority: no named evidence-consuming factual acceptance established. Claim: [EPI-CLM-never-forgets](#epi-clm-never-forgets). SRC-1, `src/qwenpaw/agents/command_handler.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/memory/reme_config.py`.

Trigger/proposal/admission: caller hint or configured schedule starts model-backed work; backend chooses units/topics. No demonstrated per-unit human veto, oracle or experimental successor contest. Guidance is configured source window/limits and hint. Persisted products are declared digest units/interests/catalog, not proof of accepted theory. Rejection of unsuccessful response raises; command catches errors. Backend rollback and content-retraction propagation remain unresolved. Important counterexample to treating completion as successful maintenance: adapter only raises when response is non-null and unsuccessful; a null response can return without raising, and handler then says complete. Mismatch marker: completion message exceeds demonstrated job execution, much less epistemic success.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: no result from adapter; command success/failure text; optional configured inbox event from returned response.
- Later read-back: declared digest/interests intended for later search/proactive work; exact external reader and update semantics uninspected.
- Delegated visibility: date and hint reach ReMe; external steps read their configured day-index/note sources.
- Selection predicate: enabled cron settings or command with memory manager; external extraction limits and topic settings.
- Invalidation or expiry: backend merge/deletion policy uninspected; inbox payload is not a semantic withdrawal protocol.
- Activation or effect: dispatch and result reporting implemented; no observed merged unit, criticism, acceptance or later reliance.
- Evidence limits: external steps not frozen; “integrate” in backend name is not lifecycle integration after evidenced acceptance.

> response = await self._run_reme_job(
>     "auto_dream",
>     needs_llm=True,
>     date=str(kwargs.get("date") or ""),
>     hint=str(kwargs.get("hint") or ""),
> )
> if response is not None and not response.success:
>     raise RuntimeError(str(response.answer))
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> return await self._make_system_msg(
>     "**Auto-dream Complete**\n\n"
>     "- Ran one auto-dream memory optimization pass",
> )
> --- `src/qwenpaw/agents/command_handler.py`

#### EPI-RTE-paper-dispatch
Label: Daily Paper job dispatch

Distinct from dream and supplied runtime routes: resource-fed paper selection/readings with an operator inbox output, not conversation extraction. Endpoints: configured maintenance callback → job with date/force/mirror/topics → configured collect/rank/select/analyze/digest steps → response and inbox. Owner: adapter/notification code plus external backend. Object: [EPI-OBJ-paper-brief](#epi-obj-paper-brief). Content/update relation: truth-apt transformation: indeterminate for generated brief; declared external paper acquisition has unknown source warrant and uninspected extraction fidelity. Check target/domain: adapter checks job availability and success, not truth of paper claims or faithfulness of readings. Epistemic authority: none established beyond attributed resource-derived candidate. Force/path: operational error propagation and informational inbox delivery to operator, horizon retained inbox; subsequent agent use uninspected. Claim IDs: none beyond job doctrine; mismatch marker: no inference from success status to knowledge. SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/memory/reme_config.py`.

Trigger/proposal: scheduled or direct adapter call requests topics/date; external backend ranks/selects papers. No per-claim human acceptance, expected-answer oracle or critique loop established. Force may regenerate existing brief; rollback not inspected. Guidance includes weekly/monthly sources, candidate/history limits and topics; configured stages persist readings/brief according to external backend. Notification truncates long answer text and carries artifact identifiers, so inbox body is not necessarily the complete candidate or its evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: no adapter result; exceptions for unavailable or unsuccessful job; optional inbox answer/status/payload.
- Later read-back: inbox event persists returned body and artifact paths; external note reload and later agent consumption uninspected.
- Delegated visibility: backend receives date, force, mirror and topics; detailed paper acquisition lives in dependency steps.
- Selection predicate: schedule configuration or invocation; backend selection settings; notification enable and duplicate/no-op gates.
- Invalidation or expiry: force can request regeneration; backend expiry/retraction propagation uninspected.
- Activation or effect: job request, failure signalling and inbox report wired; actual brief, source checking or downstream use unobserved.
- Evidence limits: missing paper/output instances and backend evaluators prevent conclusions about accepted ampliative claims or faithful summary.

> if response is None:
>     raise RuntimeError("ReMe is not started; Daily Paper did not run")
> if not response.success:
>     raise RuntimeError(str(response.answer))
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> answer = str(getattr(response, "answer", "") or "").strip()
> if len(answer) > MAX_INBOX_BODY_CHARS:
>     answer = f"{answer[:MAX_INBOX_BODY_CHARS].rstrip()}\n..."
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

#### EPI-RTE-memory-file
Label: Caller memory-file replacement

Distinct from [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction): memory-directory daily/digest files, not selected working instruction files. Endpoints: memory PUT body → AgentMdManager memory path → Markdown write → acknowledgement; later search is separately wired. Owner: router/file manager. Object: caller-supplied daily/digest Markdown, potentially replacing [EPI-OBJ-daily-notes](#epi-obj-daily-notes) or [EPI-OBJ-dream-units](#epi-obj-dream-units); replacement capacity does not make this route part of either producing route. Content/update relation: truth-apt transformation: acquisition/import for factual caller text, warrant unknown. Policy/non-propositional text may coexist. Trigger/proposal: caller chooses path, section and content; code resolves path and writes; human authorship/per-content review unresolved. No semantic oracle, model judgment or criterion for truth acceptance. Operational authority: file replacement before later read; enforcing I/O, advisory factual influence at later model retrieval. Retention is not lifecycle integration. Rewriting affords replacement, not versioned rollback. Claim: [EPI-CLM-preserve-valid](#epi-clm-preserve-valid); mismatch: exhortation not writer enforcement. SRC-1, `src/qwenpaw/app/routers/workspace.py`, `src/qwenpaw/agents/memory/agent_md_manager.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: written acknowledgement or HTTP error.
- Later read-back: memory corpus is available to separately configured search; exact reindex timing uninspected.
- Delegated visibility: uninspected — no automatic child publication traced.
- Selection predicate: request workspace, memory path and optional daily/digest section; path-helper safety not fully audited here.
- Invalidation or expiry: later write replaces bytes; automatic expiry and semantic withdrawal consumers uninspected.
- Activation or effect: supplied content becomes file content; no observed factual endorsement or changed answer.
- Evidence limits: caller identity, review and actual write absent; filesystem admission is not factual acceptance.

> file_path = self._memory_path_for_read_write(md_name, section)
> file_path.parent.mkdir(parents=True, exist_ok=True)
> file_path.write_text(content, encoding="utf-8")
> --- `src/qwenpaw/agents/memory/agent_md_manager.py`

#### EPI-RTE-checkpoint-restore
Label: Requested memory restoration

Distinct from [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery): caller-selected prior workspace/session/memory state, not provider overflow retry. Endpoints: checkpoint command target/flags → confirmation/preview guard → restore engine method → rendered result. Owner: command handler; engine internals uninspected. Object: selected prior state, potentially [RT-OBJ-session-state](runtime.md#rt-obj-session-state) and memory files. Content/update relation: truth-apt transformation: acquisition/import when earlier factual content is restored; historical warrant unknown, not newly accepted. Check domain: requested scope/confirmation, not truth or continued applicability. Proposer/controller: command caller; no required per-content human review established by generic caller. No answer oracle; open recovery operation. Force/path: enforcing dispatch gate, then engine changes requested files/state for later consumers, exact atomicity uninspected. Claimed safety checkpoint in handler text is not independently verified engine implementation. Claim IDs: none; mismatch marker: restoration does not endorse revived content. SRC-1, `src/qwenpaw/runtime/commands/control/checkpoint_handler.py` (implementation of handler).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: confirmation/preview guidance or rendered engine result.
- Later read-back: requested restored memory/session is intended for later consumers; engine effect and coherence not inspected.
- Delegated visibility: inapplicable — local restoration dispatch, not worker handoff.
- Selection predicate: target plus explicit include-memory flag; absent dry-run/confirm returns confirmation instructions.
- Invalidation or expiry: requests replacement by older state; downstream invalidation and reindex semantics uninspected.
- Activation or effect: selects restore_with_memory versus ordinary restore; actual mutation unobserved.
- Evidence limits: complete rollback, evidence links, concurrent state and removed-content cache behavior unresolved.

> elif include_memory:
>     result = await engine.restore_with_memory(
>         target=target,
>         session_id=context.session_id,
>         user_id=context.user_id,
>         channel=chan,
>         dry_run=dry_run,
>     )
> --- `src/qwenpaw/runtime/commands/control/checkpoint_handler.py`

#### EPI-RTE-clean-workspace
Label: Destructive workspace cleanup

Distinct from all supplied routes: top-level CLI destructive operation, not a tool permission decision or conversational clear. Endpoints: registered clean subcommand → enumerate WORKING_DIR children excluding telemetry marker → dry-run/confirmation decision → remove directories/files → Done. Owner: Click command. Content/update relation: non-truth-apt policy/content update: removes stored artifacts without evaluating their contents. Object scope: all selected working-directory children, which can contain retained memory/config/session material; actual deployed layout not supplied. Check target/domain: caller consent and selected filesystem entries, not validity of retained claims. No answer oracle or semantic proposal. Human can decline prompt; `--yes` skips it; no per-content human review required. Force/path: enforcing deletion at filesystem, indefinite until external recovery; active-process cache invalidation not established. Epistemic authority: none; removal is not refutation or propagated epistemic withdrawal. Claim: [EPI-CLM-never-forgets](#epi-clm-never-forgets); mismatch marker: counterexample to unconditional preservation. SRC-1, `src/qwenpaw/cli/main.py`, `src/qwenpaw/cli/clean_cmd.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: preview, cancellation, absence message or Done; FileNotFoundError tolerated during removal.
- Later read-back: deleted files no longer available at those paths; external backups and already loaded state are not handled here.
- Delegated visibility: inapplicable — direct CLI operation, not a model/worker exchange.
- Selection predicate: WORKING_DIR children except telemetry marker; no deletion on dry-run or declined confirmation.
- Invalidation or expiry: physical deletion; not a content-dependent expiry or truth-maintenance decision.
- Activation or effect: recursive directory removal/unlink; observed deletion not supplied.
- Evidence limits: no restoration implemented in this function; crash/permission errors and active-reader coherence not guaranteed.

> if dry_run:
>     click.echo("dry-run: nothing deleted.")
>     return
> --- `src/qwenpaw/cli/clean_cmd.py`

> if not yes:
>     ok = click.confirm(f"Delete ALL contents under {wd}?", default=False)
>     if not ok:
>         click.echo("Cancelled.")
>         return
> --- `src/qwenpaw/cli/clean_cmd.py`

> if c.is_dir() and not c.is_symlink():
>     shutil.rmtree(c)
> else:
>     c.unlink()
> --- `src/qwenpaw/cli/clean_cmd.py`

### Claims

#### EPI-CLM-never-forgets
Label: Layered self-evolving memory

Claimed operation: live working context, verbatim history and a self-evolving personal KB continuously turning conversations/resources into linked Markdown. SRC-1, `README.md` (doctrine/design). Distinct from broader [RT-CLM-assistant-work](runtime.md#rt-clm-assistant-work): specifically retention and knowledge-maintenance warrant. Design and dispatch/search routes support a layered architecture and maintenance requests, not invariant recall or factual correctness. No observed-run or causal support supplied. Cleanup, conditional persistence, search caps, transformed summaries and unavailable backend semantics bound the claim. Self-evolving is not evidence of improved capacity or accepted new knowledge.

> | **Never forgets**                       | Three-layer memory — live working context, full verbatim history, and a self-evolving personal knowledge base powered by [ReMe](https://github.com/agentscope-ai/ReMe). Conversations and resources continuously become readable, editable, searchable, and linked Markdown memory. |
> --- `README.md`

#### EPI-CLM-preserve-valid
Label: Preserve valid memory guidance

Claimed operation: user/agent retain durable information, read before update, preserve valid user/other-session information and merge without duplication. SRC-1, `src/qwenpaw/agents/md_files/en/MEMORY.md` (doctrine/design). Distinct from supplied assistant/security claims: semantic memory maintenance instruction. Direct memory writer does not enforce reading existing content, validity or merging. Model/human compliance unobserved; no causal comparison. The guidance is evidence of intended preservation, not a configured factual evaluator or actual acceptance record.

> Do not copy daily activity logs or complete conversations here; those belong in the personal knowledge base's daily notes. Unless the user explicitly asks, do not store passwords, tokens, or other sensitive information. Read the existing content before updating it, preserve valid information written by the user or other sessions, and merge without duplication.
> --- `src/qwenpaw/agents/md_files/en/MEMORY.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
