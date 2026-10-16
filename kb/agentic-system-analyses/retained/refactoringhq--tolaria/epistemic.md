---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Tolaria's note-content, operational checks and reliance routes at the frozen revision; retention is distinguished from epistemic acceptance."
run-id: AAS-2026-10-14-tolaria-42ddaf2ee8cd-01
reviewed-boundary: "48f2a70844c1e8005a7aa5f1499c66f7678360de"
---

# Tolaria epistemic report

## Source-and-claim boundary

The question is what Tolaria acquires or produces, what checks license reliance, and which results affect later behavior. Scope, external exclusions and evidence identity: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). This is a complete artifact with partial loop inspection, not a whole-system negative assessment. SRC-1 supplies implementation and doctrine/design; there are no supplied observed runs or causal experiments.

Truth-apt content can occur in note bodies, metadata and chat responses. Actual user propositions and their provenance are not supplied. Tool success, modification time, types and an organized flag are not truth judgments about those propositions. The consequential public claim already identified is [RT-CLM-direct-chat](runtime.md#rt-clm-direct-chat). The additional type/navigation claim is [EPI-CLM-types-lenses](#epi-clm-types-lenses). No broader correctness guarantee is established by the inspected guidance or write paths.

| Entry point or operation | Source path | Coverage and limit |
|---|---|---|
| Workspace send, history filtering, CLI dispatch, event completion and Stop | SRC-1, `src/lib/aiAgentSession.ts`, `src/lib/aiAgentConversation.ts`, `src/lib/aiAgentStreamCallbacks.ts`, `src-tauri/src/ai_agents.rs` | Supplied findings: [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send). CLI-model internals excluded; prevents claims about model checking or compliance. |
| Native AI commands, guidance status/restore | SRC-1, `src-tauri/src/commands/ai.rs` | Direct read of command definitions and shared/cancellable stream scaffolding; native simple Claude chat remains untraced end to end. Prevents all-entry-point admission conclusion. |
| OpenAI-compatible create-note result and content fallback | SRC-1, `src-tauri/src/ai_model_tools.rs` | Direct read plus [RT-RTE-provider-create](runtime.md#rt-rte-provider-create). Local tool result is a filesystem outcome, not truth evaluation. |
| All registered MCP tools and handler dispatch | SRC-1, `mcp-server/index.js`, `mcp-server/tool-service.js` | Direct read of registry, handlers and service. Read/search/context and attach/clone extend runtime coverage: [EPI-RTE-note-read](#epi-rte-note-read), [EPI-RTE-note-search](#epi-rte-note-search), [EPI-RTE-vault-register](#epi-rte-vault-register). UI open/highlight/refresh carry operational messages, not semantic endorsement. Deployed bridge delivery uninspected. |
| MCP update check, replacement cleanup, append and create | SRC-1, `mcp-server/vault.js` | Direct read of relevant functions plus [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write). [EPI-RTE-mtime-check](#epi-rte-mtime-check) splits the optional check from write admission. |
| Managed guidance and bundled-doc recommendations | SRC-1, `src-tauri/src/vault/config_seed.rs`, `src-tauri/src/vault/getting_started.rs`, `src/utils/ai-agent.ts`, `mcp-server/agent-instructions.js` | Direct read of replacement predicates, current AGENTS template, prompt construction and instruction delivery; see [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync). Full migration and docs corpus not assessed; prevents complete guidance correctness assessment. |
| Organize/unorganize and inbox auto-advance | SRC-1, `src/hooks/useEntryActions.ts`, `src/hooks/useInboxOrganizeAdvance.ts` | Direct reads: [EPI-RTE-organized-toggle](#epi-rte-organized-toggle). Persistence dependency below the hook remains uninspected; the flag is not a content-check result. |
| Other CLI permission modes, Pi extensions, native tools | SRC-1, `src-tauri/src/pi_config.rs` | Supplied [RT-RTE-pi-extension](runtime.md#rt-rte-pi-extension); other adapters and external packages not fully inspected. Prevents app-wide enforcing-policy conclusion. |
| Editor serialization, watcher/Git reconciliation, web/server collaboration and remaining evaluators/tests | SRC-1, `src/App.tsx`, `apps/web/README.md`, `apps/server/src/main.ts`, `package.json` | Supplied boundary identifies included but uninspected loops. No tests executed. Prevents exhaustive semantic-acceptance, rollback or consistency conclusion. |

Search for an omitted evaluator or cleanup route covered `src-tauri/src/commands/ai.rs`, `src/utils/ai-agent.ts`, `src/lib/aiAgentStreamCallbacks.ts` using review/verify/hook/cleanup/organize terms, then source discovery for organized-state consumers. This exposed the organize hook, which is assessed separately rather than treated as an epistemic approval. The MCP registry also exposed attach/clone, extending available read/write scope. These are countercases to reducing the target to chat plus three write tools; they do not invalidate the runtime's selected-route account. Relevant uninspected operations prevent a system-complete absence claim.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-note-content](#epi-obj-note-content) | Possible assertions in body and frontmatter | Retained knowledge and context | SRC-1, `mcp-server/vault.js` | Actual propositions, initial authorship and evidence lineage unknown. |
| [EPI-OBJ-read-result](#epi-obj-read-result) | Parsed body, frontmatter and current file metadata | MCP caller's note context | SRC-1, `mcp-server/vault.js` | Trimming/parsing changes representation; source truth not tested. |
| [EPI-OBJ-search-result](#epi-obj-search-result) | Partial excerpts and path/title information | Discovery context | SRC-1, `mcp-server/vault.js` | Truncation may omit necessary qualification; not a complete proposition/evidence package. |
| [RT-OBJ-agent-prompt](runtime.md#rt-obj-agent-prompt) | Product/convention assertions plus instructions | see record | SRC-1, `src/utils/ai-agent.ts` | Policy delivery is not reliable obedience or independent product verification. |
| [EPI-OBJ-organized-flag](#epi-obj-organized-flag) | None about note truth; workflow state | Mark as Organized | SRC-1, `src/hooks/useEntryActions.ts` | Does not encode acceptance criterion or evidence. |
| [RT-OBJ-stream-request](runtime.md#rt-obj-stream-request) | None in dispatch fields; text payload may be truth-apt | see record | SRC-1, `src-tauri/src/ai_agents.rs` | Opaque external model processing. |

Chat histories and provider-generated responses are carried by [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send) and [RT-RTE-provider-create](runtime.md#rt-rte-provider-create). Individual candidate propositions are not determinable without request/result instances. Distributed-parametric parts remain separately bounded by [RT-CMP-cli-model](runtime.md#rt-cmp-cli-model) and [RT-CMP-api-model](runtime.md#rt-cmp-api-model): no inspected application weight update, no immutable model-version pin, and provider resolution remains opaque.

## Authority-route ledger

Each entry is one function. Where a declaring record owns identity or implementation details, see that record. Architectural status below is independently assessed. Results described here are possible implementation outcomes, not observed operation.

Route ID: [EPI-RTE-note-read](#epi-rte-note-read)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content) → [EPI-OBJ-read-result](#epi-obj-read-result)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: selected existing note enters caller context.
Evaluator/condition and domain: path/root and ambiguity rules, not a truth evaluator.
Activation and timing: caller invokes get_note; before tool return.
Possible or observed result: parsed frontmatter, trimmed body, path and mtime; errors on failed/ambiguous read.
Implemented force: supplies context.
Epistemic authority and scope: no endorsement; external source warrant unknown, no independent source/evidence validation.
Operational authority: permits caller to use returned text in the current request.
Behavioral-authority path: MCP client/model, JSON text tool return, advisory, current invocation; later behavior unobserved.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: parsing preserves many ordinary body assertions, but does not establish source truth or general semantic preservation for malformed frontmatter.

Route ID: [EPI-RTE-note-search](#epi-rte-note-search)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-result](#epi-obj-search-result)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: substring-selected text is excerpted and formatted.
Evaluator/condition and domain: deterministic lowercase substring matching and result limit, not factual relevance evaluation.
Activation and timing: search_notes invocation.
Possible or observed result: ordered limited snippets or no-match message.
Implemented force: selection/context supply, not acceptance.
Epistemic authority and scope: evidence only of matching stored text; excerpt can omit warrant or negation context.
Operational authority: makes selected notes easier to inspect/use; does not prevent relying on an excerpt alone.
Behavioral-authority path: MCP client/model, formatted text, advisory selection, current tool invocation.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no global relevance ranking; vault order and scan order affect coverage.

Route ID: [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: completed user/assistant history; see route.
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: history filtering and newest-fitting suffix selection.
Evaluator/condition and domain: code budget estimate and completed/nonmarker message predicate; no truth judgment.
Activation and timing: before each send.
Possible or observed result: selected text delivered; old turns and tool/reasoning objects omitted.
Implemented force: enforcing context construction.
Epistemic authority and scope: no added warrant; omission can remove evidence lineage.
Operational authority: controls what the external model sees; does not erase stored turns or roll back files.
Behavioral-authority path: see route and [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy).
Evidence source ID and local anchor: SRC-1, `src/lib/aiAgentConversation.ts`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no observed downstream reliance or benefit; incomplete native transcript lifecycle.

Route ID: [RT-RTE-provider-create](runtime.md#rt-rte-provider-create)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: provider response/tool content; see route.
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: model maps request context to response/content; fixed fallback can format title/type without adding factual claims.
Evaluator/condition and domain: external model inference; no supplied candidate-level comparison.
Activation and timing: API-target request and provider return.
Possible or observed result: text, note proposal, fallback Markdown or error.
Implemented force: candidate generation.
Epistemic authority and scope: novelty or fluent text adds no warrant. Entailment, preservation and non-entailment are not distinguishable without instances.
Operational authority: tool proposal can reach local write executor before any semantic check.
Behavioral-authority path: see [RT-BAP-tool-executor](runtime.md#rt-bap-tool-executor).
Evidence source ID and local anchor: SRC-1, `src-tauri/src/ai_model_tools.rs`.
Claim IDs or none: [RT-CLM-direct-chat](runtime.md#rt-clm-direct-chat).
Mismatch marker or none: documentation's universal no-write-tools claim is too broad.
Gap/limit: no evidence-consuming acceptance of a produced ampliative claim established by this executor.

Route ID: [EPI-RTE-mtime-check](#epi-rte-mtime-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: stored note modification time.
Content/update relation: no content change
Transition or check target: equality of supplied expectedMtime and current file stat.
Evaluator/condition and domain: deterministic numerical equality, only when expectedMtime supplied.
Activation and timing: before MCP full replacement.
Possible or observed result: return or error recommending re-read/retry.
Implemented force: return continues update; exception blocks it.
Epistemic authority and scope: licenses only that the sampled mtime matches expectation, not unchanged meaning, current source truth or exclusive access through write completion.
Operational authority: gates the current replacement; omitted expectation skips gate.
Behavioral-authority path: updateNote, return/exception, enforcing conditional gate, one operation.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no compare-and-swap; later concurrent edits can intervene.

Route ID: [RT-RTE-provider-create](runtime.md#rt-rte-provider-create)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: provider tool name, arguments and proposed Markdown; see route.
Content/update relation: no content change
Transition or check target: create-note request admission, not acceptance of propositions.
Evaluator/condition and domain: supported function, arguments, active vault and native path/exclusive-create constraints; see route.
Activation and timing: after provider completion, before local create.
Possible or observed result: create proceeds or error; earlier calls can already have written.
Implemented force: local executable admission.
Epistemic authority and scope: none for truth; successful write is not evidence-consuming acceptance.
Operational authority: permits create without an inspected per-content confirmation branch.
Behavioral-authority path: native create-note executor, provider tool-call arguments, enforcing admission, current call with lasting file effects; see [RT-BAP-tool-executor](runtime.md#rt-bap-tool-executor).
Evidence source ID and local anchor: SRC-1, `src-tauri/src/ai_model_tools.rs`.
Claim IDs or none: [RT-CLM-direct-chat](runtime.md#rt-clm-direct-chat).
Mismatch marker or none: universal direct-model no-write claim contradicted.
Gap/limit: no semantic approval or multi-call rollback established.

Route ID: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: MCP create request; see route.
Content/update relation: no content change
Transition or check target: new-file operational admission.
Evaluator/condition and domain: active root, path/content/default rules and exclusive create; see route.
Activation and timing: create_note invocation, before new file write.
Possible or observed result: creation or error, including existing destination.
Implemented force: enforcing local gate.
Epistemic authority and scope: none about note truth.
Operational authority: allows a new note without an inspected per-content human veto.
Behavioral-authority path: Node filesystem service, MCP create arguments, enforcing, current call with lasting file effects.
Evidence source ID and local anchor: SRC-1, `mcp-server/tool-service.js`.
Claim IDs or none: [EPI-CLM-types-lenses](#epi-clm-types-lenses).
Mismatch marker or none: none.
Gap/limit: create permission is not factual acceptance.

Route ID: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: MCP replacement request; see route.
Content/update relation: no content change
Transition or check target: full existing-note replacement admission.
Evaluator/condition and domain: active root/path/content and optional mtime gate; see [EPI-RTE-mtime-check](#epi-rte-mtime-check).
Activation and timing: update_note invocation, before temporary-file replacement.
Possible or observed result: replacement or path/conflict/I/O error.
Implemented force: enforcing local gate.
Epistemic authority and scope: none about replacement truth; mtime license is separately bounded.
Operational authority: allows full replacement, with caller-selectable conflict check.
Behavioral-authority path: Node updateNote, MCP update arguments and check return/exception, enforcing, current call with lasting replacement.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: [EPI-CLM-types-lenses](#epi-clm-types-lenses).
Mismatch marker or none: none.
Gap/limit: no semantic approval; conflict sample is not atomic with replacement.

Route ID: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: MCP append request; see route.
Content/update relation: no content change
Transition or check target: existing-file append admission.
Evaluator/condition and domain: active root/path and nonempty content; no expectedMtime gate in this operation.
Activation and timing: append_to_note invocation before append.
Possible or observed result: appended bytes or error.
Implemented force: enforcing local gate.
Epistemic authority and scope: none about appended assertions.
Operational authority: permits extension, not full replacement, without semantic review.
Behavioral-authority path: Node appendToNote, MCP append arguments, enforcing, current operation with persistent extension.
Evidence source ID and local anchor: SRC-1, `mcp-server/tool-service.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: lower-risk documentation is not proof of semantic correctness or transactional append.

Route ID: [RT-RTE-provider-create](runtime.md#rt-rte-provider-create)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: no content change
Transition or check target: provider candidate becomes a new Markdown file.
Evaluator/condition and domain: exclusive create and I/O success, not truth.
Activation and timing: after provider-call admission.
Possible or observed result: new file or error; previous batch creations can remain.
Implemented force: physical persistence.
Epistemic authority and scope: retained candidate, source warrant unknown.
Operational authority: future vault readers can consume file content without an added approval stage.
Behavioral-authority path: native file create → vault reader/MCP → later caller, permissive availability across requests.
Evidence source ID and local anchor: SRC-1, `src-tauri/src/vault/file.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no demonstrated acceptance-followed integration or actual later activation.

Route ID: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: no content change
Transition or check target: MCP candidate becomes a new file.
Evaluator/condition and domain: Node exclusive create/write result, not truth.
Activation and timing: after MCP create admission.
Possible or observed result: new Markdown file or I/O error.
Implemented force: physical persistence.
Epistemic authority and scope: retained candidate only.
Operational authority: future readers can retrieve new file.
Behavioral-authority path: Node new-file write → vault/MCP read → later caller, permissive availability across requests.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: not evidence of acceptance, lifecycle integration or crash durability.

Route ID: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: no content change
Transition or check target: replacement content supplants existing note.
Evaluator/condition and domain: temporary-file write and rename result, not truth.
Activation and timing: after update admission and optional mtime check.
Possible or observed result: replaced file or error with temporary-file cleanup.
Implemented force: physical replacement; cleanup is not semantic withdrawal.
Epistemic authority and scope: new retained candidate; no content judgment.
Operational authority: subsequent readers see replaced content.
Behavioral-authority path: Node temp-file/rename → later file readers, permissive availability across requests.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: old claim loss/replacement is not evidence-directed retraction; no compare-and-swap or fsync guarantee established.

Route ID: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: no content change
Transition or check target: candidate bytes extend existing note.
Evaluator/condition and domain: append handle/write/stat result, not truth.
Activation and timing: after append admission.
Possible or observed result: appended content/mtime or error.
Implemented force: physical extension.
Epistemic authority and scope: retained candidate extension only.
Operational authority: later readers can use old and appended material together.
Behavioral-authority path: Node append → later file/MCP readers, permissive availability across requests.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no semantic reconciliation of contradictory old/new text or transactional append established.

Route ID: [EPI-RTE-vault-register](#epi-rte-vault-register)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: vault path/registry, imported files on clone.
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: attach/clone makes a root available to subsequent MCP operations.
Evaluator/condition and domain: directory/access/nesting checks, clone exit status and registry I/O; not source accuracy.
Activation and timing: explicit attach_vault or clone_vault request.
Possible or observed result: registered root and widened session roots; clone error cleans temporary tree.
Implemented force: registry and session-root admission.
Epistemic authority and scope: imported source warrant unknown; Git success is not endorsement.
Operational authority: read/write tool scope expands to admitted root; active vault selection need not change.
Behavioral-authority path: activeVaultPaths, registry/session path list, permissive tool availability, later calls and persisted registry use.
Evidence source ID and local anchor: SRC-1, `mcp-server/vault-lifecycle.js`, `mcp-server/tool-service.js`.
Claim IDs or none: none.
Mismatch marker or none: runtime omitted this additional root-admission route, not a false supplied fact.
Gap/limit: no remote snapshot supplied, no semantic provenance/authenticity check; registry failure after rename does not show rollback of final clone.

Route ID: [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: retained root guidance; see route.
Content/update relation: non-truth-apt policy/content update: code-selected managed instructions
Transition or check target: template recognition/empty/legacy stub determines replacement.
Evaluator/condition and domain: deterministic recognizer, not an evaluator of guidance truth or improved future decisions.
Activation and timing: seed/restore maintenance.
Possible or observed result: template/shim writes, preservation of custom content, errors.
Implemented force: code-owned replacement; future prompt requests file reading.
Epistemic authority and scope: default conventions only, no evidence-responsive acceptance established.
Operational authority: changes available later instructions; interpretive rather than physical isolation.
Behavioral-authority path: see route and [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy).
Evidence source ID and local anchor: SRC-1, `src-tauri/src/vault/config_seed.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no exercised improvement, theory criticism or actual instruction-mediated behavior demonstrated.

Route ID: [EPI-RTE-organized-toggle](#epi-rte-organized-toggle)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-organized-flag](#epi-obj-organized-flag)
Content/update relation: non-truth-apt policy/content update: inbox workflow flag
Transition or check target: mark/unmark organized and optionally advance inbox focus.
Evaluator/condition and domain: user action plus deterministic state/persistence/focus checks; not a semantic evaluator.
Activation and timing: toggle action; auto-advance after successful callback while focus remains unchanged.
Possible or observed result: flag change, undo history and next note selection, or state rollback/toast.
Implemented force: workflow control.
Epistemic authority and scope: none about correctness or accepted knowledge.
Operational authority: changes organization state and operator's selected next note.
Behavioral-authority path: entry UI and inbox hook, boolean state/callback, enforcing selection, current UI session with requested persistence.
Evidence source ID and local anchor: SRC-1, `src/hooks/useEntryActions.ts`, `src/hooks/useInboxOrganizeAdvance.ts`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: persisted flag does not establish evidence-consuming acceptance or lifecycle integration; lower storage dependency uninspected.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-direct-chat](runtime.md#rt-clm-direct-chat) | see record | SRC-1, `site/concepts/ai.md`, doctrine/design | see record | [RT-RTE-provider-create](runtime.md#rt-rte-provider-create) | none supplied | No intervention or quality comparison | Direct calls can create notes under provider/vault conditions; no shell follows from this | Universal no-write-tools part contradicted; not evidence of all-provider write access |
| [EPI-CLM-types-lenses](#epi-clm-types-lenses) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), [RT-RTE-provider-create](runtime.md#rt-rte-provider-create) | none supplied | Operational path constraints remain; not an exhaustive validation audit | Types provide conventions, not epistemic approval; inspected write paths agree with non-schema role | Other editor/server validation uninspected; scoped intentional design is not product failure |

## Bounded conclusion

Tolaria wires acquisition and operational reuse of note text. Parsed reads and excerpt search carry stored claims to models without establishing their truth. History suffix selection and omitted tool/reasoning entries can separate retained responses from their original evidential context. These are distinct limits on lineage, not proof that all imported warrant is lost: full note bodies can still contain citations and evidence ([EPI-RTE-note-read](#epi-rte-note-read), [EPI-RTE-note-search](#epi-rte-note-search), [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)).

The direct model and selected CLI can generate candidate responses and changes. Without candidate instances and premise comparisons, preservation, entailed derivation and ampliative conjecture remain indeterminate at the model edge. Deterministic Markdown fallback and substring excerpting do not themselves add a warranted factual claim. Model state and any internal checking stay opaque independently of the inspected application wiring ([RT-CMP-cli-model](runtime.md#rt-cmp-cli-model), [RT-CMP-api-model](runtime.md#rt-cmp-api-model), [RT-RTE-provider-create](runtime.md#rt-rte-provider-create)).

The material checks assessed here license operation, not epistemic acceptance. An mtime match gates a replacement over a sampled file stat; supported-tool, path, active-root and exclusive-create checks permit file effects. The local executors can retain candidates before any content approval. Later file readers make those candidates available for reliance. No evidence-consuming acceptance criterion, intended factual use and scope is established in these inspected executors; therefore retention is not classified as lifecycle integration ([EPI-RTE-mtime-check](#epi-rte-mtime-check), [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), [RT-RTE-provider-create](runtime.md#rt-rte-provider-create)).

Attach/clone widens tool authority without source-truth assessment. Guidance restore changes later available policy; organized-state changes control the workflow without certifying content. Each has a consequential consumer but no supplied evidence that changed content improved later capacity. Learning benefit, evidence-responsive theory criticism/iteration, reflection and exercised self-improvement are not established by these paths; external model opacity and uninspected application loops prevent broader negatives ([EPI-RTE-vault-register](#epi-rte-vault-register), [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync), [EPI-RTE-organized-toggle](#epi-rte-organized-toggle)). No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-note-content
Label: Markdown note content

Source-native identity: filesystem Markdown content supplied to createNote/updateNote/appendToNote. Representational form: natural-language body and values interpreted by humans/models; YAML fields also have symbolic application consumers. Storage substrate: vault files. This separates retained content from [RT-OBJ-agent-prompt](runtime.md#rt-obj-agent-prompt) and [RT-OBJ-stream-request](runtime.md#rt-obj-stream-request); no supplied operative object represents the same file-content referent. Actual knowledge assertions and origin are not supplied. Evidence: SRC-1, `mcp-server/tool-service.js`, `mcp-server/vault.js`.

> const note = await createVaultNote(vaultPath, notePath, createNoteContent(args))
> --- `mcp-server/tool-service.js`

#### EPI-OBJ-read-result
Label: Parsed note result

Source-native identity: getNote return. Representational form: symbolic path/frontmatter/mtime fields carrying natural-language body to a model. Storage substrate: transient object serialized as MCP text. Distinct from [EPI-OBJ-note-content](#epi-obj-note-content): a derived read result with different consumer and omitted formatting; no supplied runtime object counterpart. Evidence: SRC-1, `mcp-server/vault.js`.

> frontmatter: parsed.data,
>     content: parsed.content.trim(),
>     mtimeMs: stats.mtimeMs,
> --- `mcp-server/vault.js`

#### EPI-OBJ-search-result
Label: Search snippet result

Source-native identity: searchNotes path/title/snippet results. Representational form: symbolic result fields rendered into natural-language tool text. Storage substrate: transient result array, not a persisted summary. Distinct from [EPI-OBJ-read-result](#epi-obj-read-result), since substring selection and truncation replace full body delivery. No supplied runtime object counterpart. Evidence: SRC-1, `mcp-server/vault.js`, `mcp-server/index.js`; supporting transformation passage in [EPI-RTE-note-search](#epi-rte-note-search).

#### EPI-OBJ-organized-flag
Label: Organized workflow flag

Source-native identity: entry.organized and `_organized` property. Representational form: symbolic boolean. Storage substrate: frontend entry state and requested frontmatter persistence. Distinct from runtime request/prompt objects; no supplied counterpart. Evidence: SRC-1, `src/hooks/useEntryActions.ts`; minimum passage in [EPI-RTE-organized-toggle](#epi-rte-organized-toggle).

### Routes

#### EPI-RTE-note-read
Label: MCP note read

Caller get_note → service active-vault/disambiguation → getNote → parsing/trimming → JSON tool text. Code owns selection/delivery. Distinct from [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write): consuming retained content rather than changing it; same files can link the routes. Evidence: SRC-1 implementation, `mcp-server/index.js`, `mcp-server/tool-service.js`, `mcp-server/vault.js`, `mcp-server/agent-instructions.js`.

- Immediate return: parsed note object or MCP error.
- Later read-back: note files retained by writers reach this later caller; this route retains no new material.
- Delegated visibility: selected body/frontmatter/path/mtime, vault metadata; get_vault_context separately includes root instructions.
- Selection predicate: requested path and optional active root; ambiguous cross-root matches rejected.
- Invalidation or expiry: each read samples current file; no retained result cache in this service method.
- Activation or effect: delivery wired; changed model behavior unobserved.
- Evidence limits: actual propositions and source warrant unknown; fallback parser not a semantic verifier.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const resolvedNote = await resolveVaultNotePath(vaultPath, notePath)
>   const raw = await readUtf8File(resolvedNote.noteRealPath)
>   const parsed = parseMarkdownNote(raw)
> --- `mcp-server/vault.js`

The parser calls gray-matter, chooses a fallback when parsed metadata is empty but fallback metadata is not, and also falls back on parsing error. This is acquisition with representation changes, not proof that malformed YAML had a unique intended meaning.

> } catch {
>     return parseFrontmatterFallback(raw)
>   }
> --- `mcp-server/vault.js`

#### EPI-RTE-note-search
Label: MCP note search

Query → per-root Markdown scan → lowercase substring match → limited excerpt results → formatted MCP text. Code owns matching and limit. Distinct from [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write) and the read result route: selection/truncation, not retained-content mutation. Evidence: SRC-1 implementation, `mcp-server/vault.js`, `mcp-server/tool-service.js`, `mcp-server/index.js`.

- Immediate return: formatted matching snippets or no-match text.
- Later read-back: accumulated file content can be selected by later searches; result itself is not retained here.
- Delegated visibility: partial body text, title and root/path label, not complete evidence context.
- Selection predicate: lowercase title/content substring; positive limit, active-root order and scan order; scan skips dot entries and selected system directories.
- Invalidation or expiry: next invocation reads files again; no semantic freshness/endorsement state.
- Activation or effect: context-selection wiring; actual reliance unobserved.
- Evidence limits: excerpt removal may alter interpretation; no relevance oracle or outcome evaluation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const body = content.replace(/^---[\s\S]*?---\n?/, '').trim()
>   const idx = body.toLowerCase().indexOf(query)
>   if (idx === -1) return body.slice(0, 120)
>   const start = Math.max(0, idx - 40)
>   const end = Math.min(body.length, idx + query.length + 80)
>   return (start > 0 ? '...' : '') + body.slice(start, end) + (end < body.length ? '...' : '')
> --- `mcp-server/vault.js`

Concrete deduction from inspected code, not execution: input `---\ntype: Note\n---\n\n# Example\nWater freezes at 0 C.\n` and query `water` yield body `# Example\nWater freezes at 0 C.`, index 10, start 0 and end equal to body length. The snippet is that body, with no ellipses. No new freezing proposition is derived, and its domain qualifications are not verified. A long body can instead lose prefix/suffix content. Across roots, the service breaks after accumulating the requested limit and slices results; it does not globally rank relevance.

#### EPI-RTE-mtime-check
Label: MCP modification check
Part of: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)

Material subroute of update admission: updateNote → stat → optional equality comparison → continuation or exception. Node code decides; caller proposes expectedMtime and can omit it. Open request, no improvement trigger or expected-answer oracle about note truth. Rejection blocks current replacement and advises re-read; no content rollback because the check precedes write. Distinct check part, not a duplicate write mechanism. Evidence: SRC-1 implementation, `mcp-server/vault.js`.

- Immediate return: no value on allowed continuation or a stale-note error.
- Later read-back: inapplicable — check result is not retained by this function.
- Delegated visibility: error text reaches caller through MCP error handling; success is consumed internally.
- Selection predicate: existing target note and supplied expectedMtime; null/undefined skips equality gate.
- Invalidation or expiry: stat result is a point-in-time sample, not a lock.
- Activation or effect: exception aborts update; return permits replacement to proceed.
- Evidence limits: sampled mtime equality neither authenticates content nor guarantees no race.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const stat = await statFile(noteRealPath)
>   if (expectedMtime === undefined || expectedMtime === null) return
>   if (stat.mtimeMs === expectedMtime) return
> --- `mcp-server/vault.js`

> await assertNoteMatchesExpectedMtime(noteRealPath, options.expectedMtime)
>   const mtimeMs = await writeExistingUtf8File(noteRealPath, content)
> --- `mcp-server/vault.js`

#### EPI-RTE-vault-register
Label: MCP vault registration

Caller attach/clone → filesystem/clone checks → registry update → session root list → later MCP operations. Distinct from [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write): root admission and possible imported tree rather than an existing-root note write. Caller proposes path/URL; code decides access/destination/nesting/registry admission; no local per-content human approval, source-truth oracle or improvement objective. Clone failure removes the temporary directory. Registry failure after successful rename has no inspected compensating final-tree deletion. Evidence: SRC-1 implementation, `mcp-server/vault-lifecycle.js`, `mcp-server/tool-service.js`, `mcp-server/index.js`.

- Immediate return: registry entry or error and vault_registry_changed action on service success.
- Later read-back: registry entry persists; sessionVaultPaths widens later service reads/writes, including imported files.
- Delegated visibility: admitted root entry; later content/instructions require reads/context calls.
- Selection predicate: explicit accessible absolute local directory or remote URL/new absolute destination; registered nesting rejected.
- Invalidation or expiry: no automatic root expiry implemented in these operations; active roots recomputed from base and session lists.
- Activation or effect: registry and tool-root expansion wired, no observed clone or downstream reliance.
- Evidence limits: external Git/remote contents unknown; source accuracy not evaluated; persistence consumers outside the service untraced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const entry = await operation(args)
>     if (!sessionVaultPaths.includes(entry.path)) sessionVaultPaths.push(entry.path)
>     emitUiAction('vault_registry_changed', { path: entry.path, registrationType })
> --- `mcp-server/tool-service.js`

> await cloneRepository(remoteUrl, temporaryPath)
>     await rename(temporaryPath, destinationPath)
> --- `mcp-server/vault-lifecycle.js`

#### EPI-RTE-organized-toggle
Label: Organized state transition

Toggle → optimistic entry state → frontmatter persistence/history → success or rollback → optional next inbox note. Code owns state transition and focus gate; user initiates workflow marking, not an inspected evidence-consuming content verdict. No supplied runtime counterpart: distinct UI workflow surface rather than [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send). Human semantic review before clicking is unknown. Open workflow action, no expected-answer oracle/improvement criterion. Flag/history persists through requested dependencies; undo history and error rollback address workflow state, not factual withdrawal. Evidence: SRC-1 implementation, `src/hooks/useEntryActions.ts`, `src/hooks/useInboxOrganizeAdvance.ts`.

- Immediate return: boolean persistence outcome; rollback and toast on failure.
- Later read-back: requested `_organized` frontmatter persistence; complete native storage/reload uninspected.
- Delegated visibility: operator sees state and selected next note; no model evaluation request in inspected hooks.
- Selection predicate: current entry; auto-advance requires enabled setting, previously unorganized active note in inbox, available next entry and unchanged focus.
- Invalidation or expiry: reverse toggle/undo or rollback changes state; no content freshness condition.
- Activation or effect: workflow state and next-note selection wired; actual user operation unobserved.
- Evidence limits: persistence callbacks below hook uninspected; no content evidence/criterion consumed by this transition.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> deps.updateEntry(transition.path, { organized: transition.after })
>   trackEvent(action.eventName)
>   const persistPromise = persistBooleanProperty(deps, transition.path, '_organized', transition.after)
> --- `src/hooks/useEntryActions.ts`

> const organized = await onToggleOrganized(path)
>     if (!organized || !nextEntry) return
>     if (!isStillFocusedOnPath(path, activeTabPathRef, requestedActiveTabPathRef)) return
>
>     void onSelectNote(nextEntry)
> --- `src/hooks/useInboxOrganizeAdvance.ts`

### Claims

#### EPI-CLM-types-lenses
Label: Types as navigation lenses

Claimed operation: note types are navigation aids rather than required-field schemas/validation. Distinct from [RT-CLM-direct-chat](runtime.md#rt-clm-direct-chat), which concerns provider capability rather than note warrant. SRC-1 doctrine/design, `README.md`. The inspected provider/MCP writes constrain paths/arguments and I/O rather than validating factual content or an epistemic type contract. This is intentional operational scope, not a failure to implement a universal knowledge evaluator.

> Types in Tolaria are navigation aids, not enforcement mechanisms. There's no required fields, no validation, just helpful categories for finding notes.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
