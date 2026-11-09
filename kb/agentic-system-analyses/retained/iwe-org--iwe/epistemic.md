---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "IWE epistemic routes: conversation evidence, selected memory, structural checks and later reliance."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
---

# IWE epistemic report

## Source-and-claim boundary

IWE's shipped system acquires caller-written documents and supplies them to later human or external-model consumers. This report asks what licenses reliance at each transition: transcript to proposal, proposal to stored document, structural report to write permission, and retained content to later context. The frozen scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); the evidence identity is SRC-1 in its [Source register](boundary.md#source-register). No external host, plugin repository, model service, user store or execution trace is added.

The important contrast is not knowledge versus no knowledge. The store can contain truth-apt facts and user decisions, and its programs can establish bounded structural facts. Whether a captured factual claim is true is separate from whether a user selected it, a schema permits it, or a later agent receives it. The public continuity claim is [EPI-CLM-shared-context](#epi-clm-shared-context). The stronger selected-write claim is [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity).

### Material-route coverage

Direct reads below add SRC-1 implementation or doctrine/design coverage at the registered revision. Supplied findings are distinguished from direct inspection; neither is observed operation.

| Entry point or operation | Source path | Coverage and records; remaining limit |
| --- | --- | --- |
| CLI dispatch, internal commands and hook dispatch | `crates/iwe/src/main.rs` | Direct command/handler search; direct schema validation/gate read. Supplied create/update/retrieval account: [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval). |
| Capture, dedup, selection, recording | `crates/iwe/templates/claude/prompts/distill.md`; `crates/iwe/src/internal/claude/session.rs` | Complete prompt, direct proposal parser and completion read; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [EPI-OBJ-proposal](#epi-obj-proposal). Transcript extraction implementation otherwise supplied, not independently retraced. |
| Maintenance, rejection feedback, pruning, tombstones | `crates/iwe/templates/claude/prompts/reflect.md` | Complete direct prompt read; [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance). No trace of actual policy criticism, adoption or improvement. |
| Default and typed policy, typed schema | `crates/iwe/templates/claude/enable/starter.md`; `crates/iwe/templates/claude/enable/typed.md`; `crates/iwe/templates/claude/enable/schemas/learning.yaml` | Complete direct reads; [EPI-OBJ-policy-body](#epi-obj-policy-body), [EPI-OBJ-injection](#epi-obj-injection), [EPI-OBJ-learning-schema](#epi-obj-learning-schema). Other schema variants and initialization prompt not independently inspected; cannot generalize this sample's predicates to all initialized stores. |
| MCP tool registry and mutation routes | `crates/iwec/src/lib.rs` | Direct handler/registration search; direct delete, query, rename, normalize, attach. Supplied create/update: [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document). Extract/inline handlers inventoried but not fully read; no complete semantic-preservation or all-tools admission guarantee. |
| MCP explore/review/refactor prompts and resources | `crates/iwec/src/lib.rs` | Direct complete prompt/resource-handler reads; [EPI-RTE-review-prompts](#epi-rte-review-prompts). Tools find/retrieve/tree/stats/squash inventoried; supplied retrieval findings are not an exhaustive renderer audit. |
| Schema evidence and write disposition | `crates/diwe/src/schema.rs`; `crates/iwe/src/main.rs`; `crates/iwec/src/lib.rs` | Direct validation loop and pending conversion, CLI validation/gate, MCP checked call sites. [EPI-RTE-schema-check](#epi-rte-schema-check); [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission). External schema engine internals uninspected: encoding fidelity and complete validator correctness not established. |
| Post-tool correction and similarity | `crates/iwe/src/internal/claude/hook/post_tool.rs`; `crates/diwe/src/stats.rs` | Complete hook read and direct similarity/graph/mutation findings read; [EPI-RTE-post-tool](#epi-rte-post-tool). Other stats reporting consumers not exhaustively traced; no global automatic repair claim. |
| Delete and inbound link cleanup | `crates/liwe/src/operations/delete.rs`; `crates/iwec/src/lib.rs` | Complete direct operation and MCP consumer read; [EPI-RTE-link-cleanup](#epi-rte-link-cleanup). CLI guards supplied, not independently retraced for every refactoring operation. |
| Later index and editor reload | `crates/iwe/src/internal/claude/hook/index.rs`; `crates/iwes/src/router/server.rs` | Supplied [RT-RTE-session-index](runtime.md#rt-rte-session-index), [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload), not fresh direct reads. Actual host delivery/compliance remains unobserved. |
| Distribution, initialization variants, exports and tests/benchmarks | `npm/iwe/lib/run.js`; `crates/iwe/src/init/agents.rs`; `crates/iwe/src/main.rs`; `crates/iwe/tests/internal_test.rs`; `crates/iwe/benches/load.rs` | Boundary/runtime responsibility findings only, except CLI dispatch search. No independent exhaustive init/export transformation or test assertion audit; cannot conclude system-complete absence of evaluators or establish measured quality. |

Accessible but uninspected operations above are not absences. The report's negative findings concern the named checks and admission paths, not every line of IWE. Missing user documents prevent individuating actual captured propositions or deciding their entailment. Missing host traces prevent establishing that policy was delivered, selection was genuine, retrieval altered an answer, or maintenance changed later behavior. Missing interventions prevent causal benefit or component attribution. No source-supported execution evidence permits assessment of host weight updates or exact model identity; the model-free boundary declaration prevents attributing model training to IWE's Rust handlers.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-graph](runtime.md#rt-obj-graph) | See record: document payload may contain facts; graph relations encode parsed structure | See record | SRC-1, `crates/iwec/src/lib.rs` | A container, not a particular warranted proposition; body consumers interpret text. |
| [EPI-OBJ-proposal](#epi-obj-proposal) | See record | See record | SRC-1, `crates/iwe/src/internal/claude/session.rs` | Nonempty evidence text is not verified evidence. |
| [RT-OBJ-session-record](runtime.md#rt-obj-session-record) | See record: bookkeeping plus evidence/rejection payloads | See record | SRC-1, `crates/iwe/src/internal/claude/session.rs` | Written/rejected status does not authenticate user selection or claim truth. |
| [EPI-OBJ-policy-body](#epi-obj-policy-body) | See record | See record | SRC-1, `crates/iwe/templates/claude/enable/typed.md` | Static shipped guidance, not an observed accepted theory from a user store. |
| [EPI-OBJ-injection](#epi-obj-injection) | See record | See record | SRC-1, `crates/iwe/templates/claude/prompts/reflect.md` | Symbolic operational policy rather than factual endorsement. |
| [EPI-OBJ-learning-schema](#epi-obj-learning-schema) | See record | See record | SRC-1, `crates/iwe/templates/claude/enable/schemas/learning.yaml` | A `learning` label and shape do not establish learning or true contents. |

## Authority-route ledger

These are function-specific views of linked records. Architectural status describes each row, not a system-wide score. For common endpoints, ownership and source passages, see each cited declaration. Source warrant of imported caller/transcript claims is unknown unless independently supplied; no such instantiated warrant was supplied here.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-cli-document](runtime.md#rt-rte-cli-document) | content transformation | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | truth-apt transformation: acquisition/import | Caller content enters a document | See record | See record | See record | Write preparation | Source warrant unknown; does not create warrant | Caller can admit supplied content, optionally checked | CLI caller → arguments/stdin → permissive filesystem write → later loads | SRC-1, `crates/iwe/src/main.rs` | none | none | Normalization is not proof that every input's semantics survives. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | content transformation | doctrine only | [EPI-OBJ-proposal](#epi-obj-proposal) | truth-apt transformation: indeterminate | Transcript claims become proposed fact/decision bodies | External agent using capture policy and quotes | After session reading, before selection | Requested evidence-bearing candidates | Procedural authorship guidance | Could be acquisition or non-ampliative summary; entailed derivation or conjecture requires actual input/output | Agent is asked to stage, not yet publish | Host agent → distill text → advisory → capture episode | SRC-1, `crates/iwe/templates/claude/prompts/distill.md` | [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity) | unknown compliance | Code implements staging, not the model's semantic transformation. No paired candidate/transcript supplied. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | disposition/acceptance | doctrine only | [EPI-OBJ-proposal](#epi-obj-proposal) | no content change | Candidate worth keeping, with evidence shown | User remember/skip/edit; named instruction also selects; policy defines intended future repository use | Before requested strict writes | Requested retain/reject/revise | Human-mediated protocol, not a storage invariant | Selection licenses remembering under policy, not factual truth outside the conversation/project scope | Host should write selected items and skip others | User → question response/instruction → permissive under protocol → pending batch | SRC-1, `crates/iwe/templates/claude/prompts/distill.md` | [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity) | exclusivity bounded | No observed evidence-consuming acceptance decision, criterion application or true proposition established. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | retention | implemented | [RT-OBJ-session-record](runtime.md#rt-obj-session-record), [EPI-OBJ-proposal](#epi-obj-proposal) | no content change | Stage and settle supplied entries | See record; parser and completion are software bookkeeping | See record | See record | Durable progress/inbox status, outside graph | Retains candidates and reports without certifying them | Supports resumption; drops pending entries when instructed | Completion/staging caller → YAML record → enforcing state update → later inbox/brief | SRC-1, `crates/iwe/src/internal/claude/session.rs` | none | none | Settling by key/title does not verify how the user answered. |
| [EPI-RTE-schema-check](#epi-rte-schema-check) | check/evidence production | implemented | [EPI-OBJ-learning-schema](#epi-obj-learning-schema), [RT-OBJ-graph](runtime.md#rt-obj-graph) | truth-apt transformation: entailed derivation | Parsed document satisfies bound predicates, or has violations | See record | See record | See record | Report computation; separate consumers decide consequences | Bounded to configured schemas over parsed document representation; no external fact oracle | Produces evidence for gate or diagnostic | Validator → KeyReport/ValidationRun → evidence → current check | SRC-1, `crates/diwe/src/schema.rs` | none | none | Unbound keys are skipped; schema engine and parsing fidelity are not independently proved. |
| [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document) | disposition/acceptance | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | no content change | Proposed writes structurally admissible | See [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission) | CLI conditional strict; inspected MCP checked branches before persistence | Reject on reports/config error, otherwise permit | Enforcing at checked call sites | Structural admissibility only, not accepted ampliative knowledge | Blocks checked write or allows persistence | Pending-write handlers → validation result → enforcing → that write | SRC-1, `crates/iwe/src/main.rs`; `crates/iwec/src/lib.rs` | none | none | Empty reports can mean no binding. Normalize is a separate MCP persistence path without this check. |
| [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document) | retention | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | no content change | Persist caller-authored document | See record | See record | See record | Filesystem write and graph update | Retention does not upgrade truth or provenance | Later readers may consume document | MCP handler → disk/shared graph → permissive reuse → later requests | SRC-1, `crates/iwec/src/lib.rs` | [EPI-CLM-shared-context](#epi-clm-shared-context) | none | Recovery reloads disk rather than restoring all prior content. |
| [EPI-RTE-post-tool](#epi-rte-post-tool) | check/evidence production | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | truth-apt transformation: entailed derivation | Bound schema violations; lexical similarity and graph defects in selected paths | See record | After writes, if host invokes hook | See record | Diagnostic, no veto | Program-relative shape/graph/lexical properties, not same-fact identity or truth | Requests fix; possible downstream merge remains host judgment | Hook → notice/additional context → advisory → next host action | SRC-1, `crates/iwe/src/internal/claude/hook/post_tool.rs`; `crates/diwe/src/stats.rs` | none | none | Similarity does not establish duplication; no repair activation trace. |
| [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) | content transformation | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph) | truth-apt transformation: indeterminate | Remove selected document and incoming parsed links | See record | Explicit delete, preview or persist | See record | Structural withdrawal from graph/files | No decision that removed claim is false; removing links may remove lineage | Later graph readers lose target/link access after persistence | Delete caller → Changes → enforcing file/graph update → later loads | SRC-1, `crates/liwe/src/operations/delete.rs`; `crates/iwec/src/lib.rs` | none | none | Domain includes natural-language links: semantic preservation is not universal. Tombstone filtering is separately requested by reflect. |
| [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval), [RT-RTE-session-index](runtime.md#rt-rte-session-index) | operational admission/selection/consumption | implemented | [RT-OBJ-graph](runtime.md#rt-obj-graph), [EPI-OBJ-injection](#epi-obj-injection) | no content change | Select stored material for current context | See records | Explicit retrieval or invoked session-start helper | See records | Ranking/projection; stdout/tool delivery | Selection conveys availability, not endorsement; projection is not full proof context | Can expose previously retained facts/instructions to host | Reader/index → rendered output → advisory/ranking → later session/invocation | SRC-1, `crates/diwe/src/retrieve.rs`; `crates/iwe/src/internal/claude/hook/index.rs` | [EPI-CLM-shared-context](#epi-clm-shared-context) | unknown activation | Missing bodies/evidence can require explicit retrieval; host delivery remains external. |
| [EPI-RTE-review-prompts](#epi-rte-review-prompts) | check/evidence production | doctrine only | [RT-OBJ-graph](runtime.md#rt-obj-graph) | no content change | Placement, clarity, size and missing connections | External agent prompted to review/refactor | Client requests prompt, then host may act | Requested critique/proposal, not server-computed verdict | Advisory questions only | No accepted factual claim or reliable evaluation established | Host may propose operations | MCP prompt → user-role text → advisory → current host task | SRC-1, `crates/iwec/src/lib.rs` | none | none | Prompt construction is implemented; actual evaluation is not. |
| [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance) | behavior/policy adaptation | doctrine only | [EPI-OBJ-policy-body](#epi-obj-policy-body), [EPI-OBJ-injection](#epi-obj-injection) | non-truth-apt policy/content update: revise capture guidance, taxonomy or context selection | Rejection/acceptance patterns and user requests | See record | User-assisted proposal/confirmation, then edit | See record | Procedural confirmation; general tools perform writes | A policy choice, not proof of better knowledge or method | Future capture advice and symbolic context selection can change | User/host → MEMORY edit → advisory body or enforcing selector → later runs | SRC-1, `crates/iwe/templates/claude/prompts/reflect.md`; `crates/iwe/templates/claude/prompts/distill.md` | none | unknown operation | Next helper can consume injection settings; exercised evidence-shaped improvement is unestablished. |
| [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance) | lifecycle integration | doctrine only | [RT-OBJ-graph](runtime.md#rt-obj-graph) | truth-apt transformation: indeterminate | Selected merge/promote/reorganize and connect retained content | User plus policy-guided host; query/schema checks test organization | Only after requested user choice under curation permissions | Requested survivor/topic/links, proof queries | Procedural curation, implemented document tools | Organization checks do not supply factual acceptance | Later queries and retrieval can use changed links/fields | Host → curation commands → permissive storage changes → subsequent reads | SRC-1, `crates/iwe/templates/claude/prompts/reflect.md` | none | acceptance prerequisite unobserved | Lifecycle integration in the technical post-acceptance sense is not established without an accepted claim instance. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-shared-context](#epi-clm-shared-context) | See record | SRC-1, `README.md`, doctrine/design | Shared local documents and requested capture/reuse | [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document), [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval), [RT-RTE-session-index](runtime.md#rt-rte-session-index) | None supplied | No comparative quality or attribution study | Mechanisms support shared retained context and later access | Knowledge gain and useful future action remain unmeasured; README need not mean automatic scientific validation. |
| [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity) | See record | SRC-1, `crates/iwe/templates/claude/prompts/distill.md`, doctrine/design | Named instruction or explicit selection; unattended staging rule | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture); alternatives [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document), [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload) | None supplied | No deployed compliance evidence | Coherent host protocol, not exclusive enforced admission | Literal all-write guarantee contradicted by alternate handlers; no actual unselected write inferred. |

## Bounded conclusion

**IWE supports durable, user-directed project memory without making storage a truth certificate.** Caller document acquisition, persistence and later retrieval are implemented; their shared source warrant is unknown. Session capture asks for quotable transcript evidence, distinguishes user-confirmed decisions from assistant suggestions, and requests policy-relative remember/skip/edit choices. That is more selective than unfiltered conversation dumping. It is not an observed evidence-consuming acceptance of a novel factual claim: actual propositions, premises, user answers and criterion applications are absent from the supplied evidence. The strongest supported semantic classification of the requested transcript-to-body transformation is indeterminate, not automatically ampliative conjecture. See [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [EPI-OBJ-proposal](#epi-obj-proposal), [EPI-OBJ-policy-body](#epi-obj-policy-body).

**Structural evidence has real but narrow force.** Schema reports test configured predicates over parsed documents; strict CLI and checked MCP handlers can reject before persistence. Successful structural admission licenses that write under those constraints, not the truth of a `learning` body. Unbound keys are skipped. Post-write schema/similarity notices request correction but cannot veto an already completed write. Lexical similarity selects review candidates; the subsequent same-fact judgment belongs to the human/host procedure. The concrete cleanup deduction in [EPI-RTE-link-cleanup](#epi-rte-link-cleanup) is warranted within parsed graph semantics, not as a claim that all surrounding prose remains semantically intact. See [EPI-RTE-schema-check](#epi-rte-schema-check), [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission), [EPI-RTE-post-tool](#epi-rte-post-tool).

**Later authority has two distinct paths.** Documents reach readers through selection, expansion and budgets; the session index supplies metadata and an optional policy section, not every fact's body/evidence. Natural-language policies and retrieved facts influence an external interpreter only if delivered and followed. Symbolic injection settings directly determine helper selection when invoked. Neither path establishes downstream factual reliance or benefit in a run. Delete can remove access and incoming links; reflect's tombstone option requires later passes to exclude superseded entries rather than implementing a universal withdrawal gate. Retention and curation are not automatically post-acceptance lifecycle integration. See [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval), [RT-RTE-session-index](runtime.md#rt-rte-session-index), [RT-BAP-session-policy](runtime.md#rt-bap-session-policy), [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance).

**Policy adaptation is separable from learning and theory building.** Shipped method sections are localized and revisable. Rejection records can feed proposed policy edits; user confirmation is part of the requested internal process. Symbolic settings have code consumers, while natural-language compliance is host-owned. The independent theory-builder, reflection, learning and autonomy limits remain those of [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance): localized guidance and a reread path do not establish actual content-directed criticism, iterative improvement or autonomous completion. No retained empirical causal explanation, accepted ampliative theory or exercised self-improvement chain is established by the inspected prompts and handlers. This is a limit on those sources, not a negative about opaque host reasoning or every available uninspected operation.

## Shared records

### Operative objects

#### EPI-OBJ-proposal
Label: Staged proposal
Part of: [RT-OBJ-session-record](runtime.md#rt-obj-session-record)

Source-native identity: `Proposal`, the candidate portion of the session record, distinct from the record's progress counters and capture/rejection history. Representational form: natural-language title/body/evidence with symbolic key, classification, updates and status fields. Storage substrate: serialized session record outside the document graph. Candidate content can be a fact, a project decision or a proposed rule; no actual instance was supplied. Claimed role: hold evidence-bearing candidates before selection. The parser checks YAML, nonempty fields, normalized key and existing update target; it does not check quotation occurrence or factual entailment. SRC-1, `crates/iwe/src/internal/claude/session.rs`; doctrine/design, `crates/iwe/templates/claude/prompts/distill.md`.

> for (name, value) in [
>     ("title", &proposal.title),
>     ("key", &proposal.key),
>     ("body", &proposal.body),
>     ("evidence", &proposal.evidence),
> ] {
>     if value.is_empty() {
>         return Err(format!("--content: {} is empty", name));
>     }
> }
> --- `crates/iwe/src/internal/claude/session.rs`

> No quotable evidence, no candidate: an idea you raised and argued well is a suggestion, not a decision.
> --- `crates/iwe/templates/claude/prompts/distill.md`

#### EPI-OBJ-policy-body
Label: Memory policy body
Part of: [RT-OBJ-graph](runtime.md#rt-obj-graph)

Source-native identity: the natural-language body of the `MEMORY` document, a material payload part of the loaded graph rather than the whole graph. Storage substrate: workspace Markdown/configured document, loaded into graph memory. Representational form: named natural-language sections interpreted by external humans/models. Claimed role: govern capture, writing, dedup, provenance, curation and session-start advice. Content includes normative instructions and criteria about durable project facts; a normative rule is not by itself a factual discovery. Distinct from [EPI-OBJ-injection](#epi-obj-injection), whose consumer follows fixed symbolic rules. Closest supplied route: [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance), not another declaration of this body. SRC-1 doctrine/design, `crates/iwe/templates/claude/enable/starter.md`, `crates/iwe/templates/claude/enable/typed.md`.

> **A `decision` is recorded only when the user requested or confirmed it, in their own words.** An assistant recommendation, however well argued, is not a decision, nor is a proposal that went unanswered — drop it, or write it as a `learning` about the open question, never as a settled `decision`.
> --- `crates/iwe/templates/claude/enable/typed.md`

> Keep an item only when it stays true after the session ends, is not obvious from the code, the README, `CLAUDE.md`, the history or a document already here, and would make a future session act differently.
> --- `crates/iwe/templates/claude/enable/typed.md`

#### EPI-OBJ-injection
Label: Injection slices
Part of: [RT-OBJ-graph](runtime.md#rt-obj-graph)

Source-native identity: `injection` frontmatter in the loaded `MEMORY` document, split from its natural-language body because the consumers and force differ. Representational form: symbolic filter/sort/heading/limit/max_tokens settings. Storage substrate: document frontmatter and loaded graph structures. Claimed role: choose the session-start index, not certify any chosen fact. SRC-1 doctrine/design, `crates/iwe/templates/claude/prompts/reflect.md`; implemented consumer and limits supplied by [RT-RTE-session-index](runtime.md#rt-rte-session-index). No duplicate of the delivery route or [RT-BAP-session-policy](runtime.md#rt-bap-session-policy).

> A document listed by one slice is not repeated by a later one, and a slice with neither `limit` nor `max_tokens` lists everything it matches.
> --- `crates/iwe/templates/claude/prompts/reflect.md`

#### EPI-OBJ-learning-schema
Label: Learning schema

Source-native identity: typed `learning.yaml`, one sample schema installed with the typed policy. Representational form: symbolic document-schema predicates. Storage substrate: shipped YAML, installable into workspace schema configuration; this is configuration rather than a document graph payload, so not a part of [RT-OBJ-graph](runtime.md#rt-obj-graph). No counterpart object was declared in supplied runtime; [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission) describes its class of consumer authority. Claimed role: constrain learning-document shape. Candidate truth-apt content: none in the schema itself; its name describes a document class. SRC-1 implementation/configuration, `crates/iwe/templates/claude/enable/schemas/learning.yaml`.

> required: [type, created]
> properties:
>   type: { const: learning }
>   created: { type: string }
>   session: { type: string }
> additionalProperties: true
> maxTokens: 400
> maxDepth: 2
> --- `crates/iwe/templates/claude/enable/schemas/learning.yaml`

### Routes

#### EPI-RTE-schema-check
Label: Schema report computation

Distinct identity: evidence-producing validation shared by the CLI, MCP and hook consumers, not their admission decision. It overlaps [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document) and [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload), but is not part of exactly one supplied route. Endpoints: pending key/content or loaded selected documents → configured bindings/compiled schemas → `ValidationRun` and `KeyReport`. Owner: deterministic validator adapter. It builds a graph from pending Markdown, resolves schemas per key, builds a document representation and obtains violations from the compiled schema. It changes no source document itself. Target/domain: predicate satisfaction over this parsed representation, not external truth. The derivation is conditional on faithful parsing and validator implementation; neither schema intent nor external source accuracy is proved. SRC-1 implementation, `crates/diwe/src/schema.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reports, bound-document/schema counts, or configuration errors.
- Later read-back: inapplicable — this computation persists no report; caller may separately use output or change documents.
- Delegated visibility: inapplicable — no delegation is implemented by the validator.
- Selection predicate: caller-supplied keys and configured key-to-schema bindings; unbound keys skipped.
- Invalidation or expiry: a fresh invocation recomputes against current supplied content/configuration.
- Activation or effect: evidence for a separate gate, command report or hook; no observed result supplied.
- Evidence limits: external compiled-schema internals and all document encoding paths were not audited; shape is not factual correctness.

> let names = bindings.schemas_for(&key.to_string());
> if names.is_empty() {
>     continue;
> }
> --- `crates/diwe/src/schema.rs`

> let document = build_document(graph, key, count_tokens);
> for name in names {
>     schemas_used.insert(name);
>     let violations = compiled[name].validate(&document);
> --- `crates/diwe/src/schema.rs`

The separate disposition has enforcing force at [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission). The CLI's standalone validation exits on reports rather than rewriting documents. A clean report is possible with no bindings and cannot be read as universal schema coverage.

#### EPI-RTE-post-tool
Label: Post-tool corrective report
Part of: [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload)

This is the material diagnostic part of the supplied combined editor/reload/post-tool route, not the LSP reload itself. Endpoints: selected host tool payload and already-written files → schema or lexical/graph diagnostics → notice/context text. Owner: Rust hook helper; external host owns invocation and any response. Context effect: advisory correction prompt, not rollback. Check targets differ: schema violations over bound parsed content, graph orphan/dangling properties, and symmetric normalized BM25 similarity with token/length gates. `editor_report` emits schema findings; `command_report` handles selected unchecked IWE writes and creates, and takes only similar-page findings from mutation diagnostics for create advice. These are not semantic sameness tests. SRC-1 implementation, `crates/iwe/src/internal/claude/hook/post_tool.rs`, `crates/diwe/src/stats.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: optional notice plus additional corrective context through the supplied hook dispatch.
- Later read-back: inapplicable — the report does not itself retain or edit a document; host correction is separate.
- Delegated visibility: uninspected — host/plugin wiring and delivery to any agent are not supplied.
- Selection predicate: Write/Edit/MultiEdit file paths/extensions; Bash text heuristics for IWE verbs, strict flag and create, with resolvable written keys; MEMORY excluded.
- Invalidation or expiry: recomputed from selected current files; report is post-write and does not restore old content.
- Activation or effect: asks host to fix schema or read a similar page, merge/delete only if same fact; no observed repair.
- Evidence limits: selected tool/command heuristics are not universal monitoring; model/human semantic comparison is not performed by BM25.

> (reverse_ratio >= threshold).then(|| SimilarPage {
>     key: other,
>     score: forward_ratio.min(reverse_ratio),
> })
> --- `crates/diwe/src/stats.rs`

> "That write ran without `--strict`, which would have refused it before anything landed. Fix the document and put the flag on every write.".to_string(),
> --- `crates/iwe/src/internal/claude/hook/post_tool.rs`

Candidate comparison and correction roles: code proposes lexical neighbors; host reads and decides semantic sameness under dedup policy; user can control the host procedurally, not by a hook-enforced selection token. Mode: post-write open requests, not a curriculum. Answer oracle: inapplicable — no reference correct fact is provided. Rejection/rollback: no write veto; later merge/delete would be new general document operations. Guidance is current dedup policy plus diagnostic text; persistent output would be a later host-authored document, not the report itself.

#### EPI-RTE-link-cleanup
Label: Delete link cleanup

Distinct identity: explicit delete tool and shared `delete` operation, extending supplied [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document)'s create/update/query account. The operation is also reachable inside generic query deletion, but this record owns the cleanup transformation, not the query parser or guard. Endpoints: target graph key → affected incoming-link documents and removal → `Changes` → MCP validation/preview or persistence. Owner: deterministic operation and MCP handler. Action effects: remove incoming inclusion edges and inline link targets, render changed referrers, remove target. SRC-1 implementation, `crates/liwe/src/operations/delete.rs`, `crates/iwec/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: error if target missing, otherwise changes or persisted changes with post-delete warnings in MCP.
- Later read-back: persisted referrer changes and removal reach future graph consumers and disk loads.
- Delegated visibility: uninspected — MCP host chooses delivery and subsequent actions.
- Selection predicate: explicit target key, then incoming inclusion/reference edges in parsed graph.
- Invalidation or expiry: removal withdraws target from future loads; a caller can recreate it separately.
- Activation or effect: graph/file deletion and referrer rewriting when not dry-run; no executed cleanup supplied.
- Evidence limits: no factual rejection judgment, immutable retraction history or automatic epistemic rollback is implemented by this operation.

> let updated = tree
>     .remove_inclusion_edges_to(&links_to)
>     .remove_inline_links_to(&links_to);
> let markdown = updated.iter().to_text(&affected_key.parent(), &format);
> result.add_update(affected_key.clone(), markdown);
> --- `crates/liwe/src/operations/delete.rs`

> result.add_remove(target_key.clone());
> --- `crates/liwe/src/operations/delete.rs`

Concrete static deduction: suppose parsed document `a` includes target `b` and `b` exists. Deleting `b` collects `a` through the inclusion edges, applies the predicate `graph.target_key(target) == b`, removes the inclusion to `b`, emits an update for `a` and a removal for `b`. This follows from inspected implementation, not target execution. For an inline link to `b`, the inline-link removal is also applied; this report does not infer that linked wording or all prose meaning is preserved. MCP checks pending rewritten documents before persisting; validation failure can reject the deletion, and dry-run returns changes without persistence. A successful write changes later reachable structure, not the truth value of the deleted document.

Decision roles: caller proposes and requests deletion; server can veto missing target, schema failures or I/O errors. Human identity is unresolved from an MCP call. Mode: open tool request. Answer oracle: inapplicable — target existence and schemas are not factual reference answers. Guidance: caller's intent, optional reflect curation policy. Recovery follows [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document); no transaction-wide restoration is established.

#### EPI-RTE-review-prompts
Label: MCP review prompts

Distinct identity: server-generated explore/review/refactor prompt and document-resource delivery, absent as separate routes from supplied runtime; closest overlap is [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval)'s document context. Endpoints: client prompt/resource request → statistics, retrieved context or graph-rendered document → client/host. Owner: MCP handlers construct messages; external model/human owns any actual diagnosis. Representational form: symbolic selection plus natural-language questions/document payloads. `review` retrieves includes/included_by depth two with backlinks; `refactor` uses includes three/included_by one and requests a restructuring sequence. No server-side model evaluator or acceptance of its critique is in these handlers. SRC-1 implementation and requested behavior, `crates/iwec/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: user-role prompt text containing serialized context, or resource content; missing document yields error.
- Later read-back: documents already retained can be delivered; inapplicable to retaining critique — these handlers persist none.
- Delegated visibility: uninspected — client decides which model/human sees returned messages.
- Selection predicate: requested key, fixed context expansion per prompt, or resource URI; listing caps document resources at 100, document URI read is separate.
- Invalidation or expiry: each request uses current server graph; no critique state to invalidate.
- Activation or effect: implemented context delivery and requested review; critique, adoption and changes remain unobserved.
- Evidence limits: output questions are not evaluation results; resource document rendering is not an independent source-truth check.

> "Review this document and its context in the knowledge graph:\n\n```json\n{}\n```\n\nConsider: Is it well-placed in the graph? Are there missing links? Is the content clear and well-structured? What sections might be extracted into separate documents?",
> --- `crates/iwec/src/lib.rs`

Conditional diagnosis fields: external host proposes critiques and operation sequences; user/client decides whether to act, while general mutation handlers can reject structural failures. Mode: open request. Answer oracle: inapplicable — no expected correct document or reference outcome. Guidance is the prompt and supplied context; only preexisting documents persist unless another tool writes. A returned critique alone has advisory force for the current task, no automatic promotion or accepted knowledge status.

### Claims

#### EPI-CLM-shared-context
Label: Shared growing context

Claimed operation: users and agents share connected documents, save what they learn together and return to that context as work grows. SRC-1 doctrine/design, `README.md`. Distinct from [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity): this is continuity/access, not exclusive user-selected admission. The prose does not specify a factual acceptance algorithm or claim formal truth guarantees.

- claim conclusion status: claimed

> IWE gives you and your AI agents **one shared place to work, right inside your project**: a folder of connected Markdown documents — specs, plans, decisions, and more. Keep your own ideas there, ask your agent to save what you learn together, and return to that context as your work grows. You can read, edit, and organize those documents yourself — and they stay yours.
> --- `README.md`
