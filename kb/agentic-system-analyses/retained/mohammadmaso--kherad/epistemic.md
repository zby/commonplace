---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Kherad epistemic routes: source acquisition, compilation, structural checking, human admission and downstream reliance."
run-id: AAS-2026-11-08-kherad-ac3e4da97ac6-01
reviewed-boundary: "2a8d6992b87a33760688e1f956653c21a6292294"
---

# Kherad epistemic report

## Source-and-claim boundary

The question is how organizational content becomes usable knowledge, what checks license reliance, and how withdrawal reaches later consumers. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). All direct reads below are SRC-1 implementation unless explicitly labelled doctrine/design. No execution, actual organizational corpus, model output, review decision or causal comparison was supplied. Thus implemented routes can be assessed, but exercised factual acceptance, model compliance and improvement cannot. Provider internals and actual MCP tools remain outside the frozen evidence.

The consequential grounding claim is [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat). Additional compilation and publication claims are [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) and [EPI-CLM-reviewed-publication](#epi-clm-reviewed-publication). The following coverage distinguishes direct inspection from supplied findings; it is not an exhaustive source audit.

| Entry point or operation | Source path, SRC-1 | Coverage and record | Remaining limit |
|---|---|---|---|
| HTTP registration and dispatch | `apps/api/src/index.ts` | Direct complete read; routes registered explicitly, not a hidden CLI loop | Handler bodies not all inspected |
| Compilation tools and guidance | `apps/api/src/agents/indexer/tools.ts`, `apps/api/src/agents/indexer/prompt.ts` | Direct complete reads; [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [EPI-RTE-structural-check](#epi-rte-structural-check) | No actual generated proposition |
| Compilation postprocessing, mirrored sources and deletion delta | `apps/api/src/agents/indexer/source-mirror.ts` | Direct complete read; [EPI-RTE-resource-rewrite](#epi-rte-resource-rewrite) | Orchestrator otherwise supplied through [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile) |
| Chat and search | `apps/api/src/agents/chat/prompt.ts`, `apps/api/src/agents/search-tools.ts` | Prompt complete; search lines 1–230 direct, covering semantic search and metadata query construction; [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat) | Metadata return tail not read; no system-complete retrieval correctness claim |
| Mention context and model/configuration | `apps/api/src/agents/page-mentions.ts`, `apps/api/src/agents/settings.ts` | Supplied [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) | Delivery is not compliance; mutable model identity |
| Review, rejection, conflicts | `apps/api/src/routes/merge-requests.ts` | Supplied [RT-RTE-review-merge](runtime.md#rt-rte-review-merge) | No evidence of review criterion or inspected human decisions |
| Specialist create/edit, section accept/reject, manual save and MCP | `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/agents/specialist/page-edit-prompt.ts` | Edit prompt direct complete read; remaining implementation supplied [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session), [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring) | Remote effects opaque; no observed criticism/revision episode |
| Conversion, OCR, STT, placement | `apps/api/src/routes/ingest.ts`, `apps/ingest/main.py` | Supplied [RT-RTE-ingest-document](runtime.md#rt-rte-ingest-document) | Fidelity and source warrant unknown |
| Remote raw/compiled admission | `apps/api/src/routes/bundle-remote.ts`, `apps/api/src/routes/document-remote.ts` | Supplied [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull) | Remote authorship/checking unavailable |
| Human compiled-document edits | `apps/api/src/routes/okf-docs.ts`, `apps/api/src/lib/okf-doc.ts` | Direct complete reads; [EPI-RTE-okf-edit](#epi-rte-okf-edit) | Semantic review not enforced at save |
| Version creation, restore, deletion | `apps/api/src/routes/wiki-versions.ts` | Direct complete read; [EPI-RTE-version-restore](#epi-rte-version-restore) | Core restore internals not inspected; caller route does not prove actual recovery |
| Page/folder withdrawal | `apps/api/src/routes/pages.ts` | Direct lines 368–522; [EPI-RTE-page-delete](#epi-rte-page-delete) | Other CRUD/rename bodies not directly read; no instantaneous global withdrawal conclusion |
| Skills, provider and capability administration | `apps/api/src/routes/skills.ts`, `apps/api/src/agents/mcp.ts` | Supplied [RT-RTE-admin-configuration](runtime.md#rt-rte-admin-configuration), [RT-BAP-session-skills](runtime.md#rt-bap-session-skills) | No trace-responsive configuration improvement evidence |
| Other registered handlers, UI, core search/Git tests | `apps/api/src/index.ts`, `packages/core/src/search/refresh.test.ts` | Registration direct; broader inventory in boundary, limited supplied runtime tracing | Not exhaustively assessed: prevents a system-complete negative about all evaluators or recovery routes. Tests are not observed passes |

The source register has no observed-run or causal-experiment layer. There is no source-supported candidate instance from which entailment or non-entailment of a generated organizational proposition can be decided. Model transformations are therefore classified as indeterminate, not automatically as conjecture or faithful reshaping. No supplied runtime fact requires supersession. Added restore and manual compiled-edit findings extend its selected routes rather than contradict its bounded account.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-pages](#epi-obj-source-pages) | Organizational claims in raw Markdown; specific propositions not supplied | Sources and mirrored evidence | see record | Import preserves text at some edges, not source truth |
| [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | Compiled organizational statements | Published knowledge | see record | Resource URL is not proof of derivation |
| [RT-OBJ-pending](runtime.md#rt-obj-pending) | See record; candidate Markdown plus symbolic path/deletion map | Staging | see record | No acceptance implied |
| [EPI-OBJ-session-draft](#epi-obj-session-draft) | Proposed document or section statements | Editable candidate | see record | No actual candidate or user rationale supplied |
| [EPI-OBJ-chat-answer](#epi-obj-chat-answer) | Answer assertions; actual content not determinable | Reader-facing answer | see record | Citation instructions are not a verifier |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) | None established in numerical parameters/vectors alone | Retrieval representation | see record | Similarity is not truth; proposition-level parameter content not determinable |
| [RT-BAP-session-skills](runtime.md#rt-bap-session-skills) | Method directions, potentially including claims; content unavailable | Working method | see record | Policy delivery distinct from truth assessment |

## Authority-route ledger

Fields owned by cited records are referenced rather than copied. Architectural statuses below concern inspected code, including implementation passages retained by supplied records; none establishes observed operation. Function-specific splits keep checking, disposition, retention and downstream use separate.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-ingest-document](runtime.md#rt-rte-ingest-document) | content transformation | implemented | [EPI-OBJ-source-pages](#epi-obj-source-pages) | truth-apt transformation: acquisition/import | Uploaded document into editable Markdown | see route | see route | see route | see route | External source warrant unknown; transcription accuracy unchecked | see route | see route | see route | none | none | OCR/STT may alter statements; no fidelity trace |
| [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring) | retention | implemented | [EPI-OBJ-source-pages](#epi-obj-source-pages) | no content change | Save/import candidate into raw Git content | see route | see route | see route | see route | Caller admission is not factual acceptance | see route | see route | see route | none | none | Explicit save need not mean semantic approval |
| [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile) | content transformation | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | truth-apt transformation: indeterminate | Source claims into concepts | see route | see route | see route | see route | Prompt asks for fidelity; neither entailment nor novelty established | see route | see route | see route | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | policy versus guarantee | No input/output pair or semantic checker |
| [EPI-RTE-structural-check](#epi-rte-structural-check) | check/evidence production | implemented | [RT-OBJ-pending](runtime.md#rt-obj-pending) | no content change | Path and frontmatter shape | see route | see route | see route | see route | Parseability/nonempty type only | see route | see route | see route | none | none | Not source truth or citation coverage |
| [EPI-RTE-structural-check](#epi-rte-structural-check) | disposition/acceptance | implemented | [RT-OBJ-pending](runtime.md#rt-obj-pending) | no content change | Tool write eligibility | see route | see route | see route | see route | Structural admission for staging, not epistemic acceptance | see route | see route | see route | none | none | Reserved documents exempt |
| [EPI-RTE-resource-rewrite](#epi-rte-resource-rewrite) | lineage/freshness/recovery | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | truth-apt transformation: indeterminate | Source URL association | see route | see route | see route | see route | Reachable source link only; no checked derivation | see route | see route | see route | [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | association versus support | Single-source fallback can create a link without semantic checking |
| [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile) | retention | implemented | [RT-OBJ-pending](runtime.md#rt-obj-pending) | no content change | Agent-branch commit and MR | see route | see route | see route | see route | Durable proposal, not accepted knowledge | see route | see route | see route | none | none | Successful run need not publish |
| [RT-RTE-review-merge](runtime.md#rt-rte-review-merge) | disposition/acceptance | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | no content change | Open MR/live branch tip | see route | see route | see route | see route | Permission and merge admissibility; actual factual criterion unspecified | see route | see route | see route | [EPI-CLM-reviewed-publication](#epi-clm-reviewed-publication) | human approval versus warrant | No recorded evidence-consuming acceptance against named truth criterion |
| [RT-RTE-review-merge](runtime.md#rt-rte-review-merge) | operational admission/selection/consumption | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | no content change | Published Git and searchable state | see route | see route | see route | see route | Publication licenses use operationally, not infallibility | see route | see route | see route | [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat) | none | No epistemic lifecycle integration established merely by publishing/indexing |
| [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat) | operational admission/selection/consumption | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | no content change | Tool/context selection | see route | see route | see route | see route | Relevance/metadata filtering, not factual validation | see route | see route | see route | [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat) | input-scope mismatch | Snippets truncated; full read is a separate model choice |
| [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat) | content transformation | implemented | [EPI-OBJ-chat-answer](#epi-obj-chat-answer) | truth-apt transformation: indeterminate | Answer from messages/tool results | see route | see route | see route | see route | Grounding/citations requested, no independent answer acceptance | see route | see route | see route | [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat) | policy versus guarantee | Answer content and compliance unobserved |
| [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session) | content transformation | implemented | [EPI-OBJ-session-draft](#epi-obj-session-draft) | truth-apt transformation: indeterminate | Research/questioning into draft or section proposal | see route | see route | see route | see route | Clarification and critical editing guidance, not a semantic proof | see route | see route | see route | none | none | May reshape or add claims; no candidate to classify |
| [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring) | disposition/acceptance | implemented | [EPI-OBJ-session-draft](#epi-obj-session-draft) | no content change | Section choice or save/import | see route | see route | see route | see route | Choice authorizes content use; truth criterion not recorded as a requirement | see route | see route | see route | none | none | Manual save bypasses accepted-overrides assembly |
| [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull) | operational admission/selection/consumption | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | truth-apt transformation: acquisition/import | Remote compiled/raw tree | see route | see route | see route | see route | Remote source warrant unknown; admin trigger not local document approval | see route | see route | see route | [EPI-CLM-reviewed-publication](#epi-clm-reviewed-publication) | alternate publication | Not universal MR enforcement |
| [EPI-RTE-okf-edit](#epi-rte-okf-edit) | retention | implemented | [EPI-OBJ-concept-docs](#epi-obj-concept-docs) | truth-apt transformation: acquisition/import | Caller-supplied compiled Markdown | see route | see route | see route | see route | Authorship outside compiler; warrant unknown | see route | see route | see route | none | none | Separate path from model compilation |
| [EPI-RTE-version-restore](#epi-rte-version-restore) | lineage/freshness/recovery | implemented | [EPI-OBJ-source-pages](#epi-obj-source-pages) | no content change | Select historical raw snapshot | see route | see route | see route | see route | Historical identity, not renewed truth endorsement | see route | see route | see route | [EPI-CLM-reviewed-publication](#epi-clm-reviewed-publication) | alternate raw admission | Compiled concepts not automatically re-derived |
| [EPI-RTE-page-delete](#epi-rte-page-delete) | disposition/acceptance | implemented | [EPI-OBJ-source-pages](#epi-obj-source-pages) | no content change | Caller withdrawal | see route | see route | see route | see route | No falsity judgment required | see route | see route | see route | none | none | Later compile deletion guidance is not synchronous revocation |
| [RT-RTE-admin-configuration](runtime.md#rt-rte-admin-configuration) | behavior/policy adaptation | implemented | [RT-BAP-session-skills](runtime.md#rt-bap-session-skills) | non-truth-apt policy/content update: method and capability configuration | Skill/provider/tool setup | see route | see route | see route | see route | Administrator authorization, not demonstrated method efficacy | see route | see route | see route | none | none | Live behavioral path exists; trace-responsive improvement not established |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat) | see record | see record | see record | [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull), [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages) | None supplied | No comparison; no observed answer | Model instructed to ground answers, tools select published OKF | Raw attachments broaden context; default branch does not certify local human review |
| [EPI-CLM-source-fidelity](#epi-clm-source-fidelity) | see record | see record | see record | [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [EPI-RTE-resource-rewrite](#epi-rte-resource-rewrite), [EPI-RTE-structural-check](#epi-rte-structural-check) | None supplied | No semantic input/output comparison | Source-grounded compilation is requested, with structural gating and source-link repair | Cannot establish semantic preservation, entailed derivation or actual ampliative acceptance |
| [EPI-CLM-reviewed-publication](#epi-clm-reviewed-publication) | see record | see record | see record | [RT-RTE-review-merge](runtime.md#rt-rte-review-merge), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull), [EPI-RTE-version-restore](#epi-rte-version-restore) | None supplied | No exercised reviewer or deployment evidence | MR route offers review/reject/conflict control | Universal wording exceeds alternate direct-admission paths |

## Bounded conclusion

Kherad wires candidate production and durable organizational-content use, not an evidenced factual oracle. Source import, human text entry and remote synchronization acquire claims with unknown external warrant. Model compilation and answering are semantically indeterminate on the accessible evidence: the source requests fidelity but supplies no generated candidate pair that establishes either non-ampliative reshaping or ampliative conjecture. No checked derivation from warranted premises is established. See [RT-RTE-ingest-document](runtime.md#rt-rte-ingest-document), [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat).

The deterministic check licenses staging on syntax, not truth. It can reject invalid paths/frontmatter and force correction through tool errors; it cannot establish that a resource supports a concept. The resource-rewrite example below is a positive countercase to interpreting citation presence as evidence-consuming acceptance. Human review can veto publication, and section decisions can exclude proposals, but implementation requires no named factual criterion or recorded supporting evidence for an intended use. Consequently epistemic acceptance and subsequent lifecycle integration are not established by merge status, retained files or search synchronization alone. See [EPI-RTE-structural-check](#epi-rte-structural-check), [EPI-RTE-resource-rewrite](#epi-rte-resource-rewrite), [RT-RTE-review-merge](runtime.md#rt-rte-review-merge), [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring).

Publication, attachment priority and skill loading have different authority paths. Published files become tool/wiki/search inputs; attached raw pages are explicitly preferred in model instructions; skills prescribe a working method on later turns. These are consequential delivery/selection paths, not evidence of correct downstream reliance. Remote pull and raw snapshot restore qualify universal review claims. Deletion removes raw candidates from future live-page inventories, but does not itself prove all published concepts, answers or prior thread copies have been withdrawn. See [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages), [RT-BAP-session-skills](runtime.md#rt-bap-session-skills), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull), [EPI-RTE-version-restore](#epi-rte-version-restore), [EPI-RTE-page-delete](#epi-rte-page-delete).

Critical-editing instructions afford asking questions and challenging contradictions, but no observed content-directed criticism/revision loop or formulated theory episode is supplied. Localized Markdown is inspectable and revisable; that fact alone establishes neither all theory-builder conditions nor improved future capacity. Learning remains unestablished independently of persistence. Skills/configuration can change later behavior-determining inputs, but evidence-responsive self-change and its subsequent exercise are not established. Reflection's two causal directions are likewise not established by storing methods or proposals. Computational proposal generation coexists with caller-controlled save/review/configuration and opaque remote effects; it supplies no autonomous-theory-builder conclusion. Provider weight mutation and exact versions remain bounded as in [RT-CMP-indexer-model](runtime.md#rt-cmp-indexer-model), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-ocr-model](runtime.md#rt-cmp-ocr-model), [RT-CMP-stt-model](runtime.md#rt-cmp-stt-model). No single system-wide epistemic score follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-pages
Label: Source pages and mirrors

Source-native identity: raw wiki page Markdown and copied `source/` Markdown. Form: natural-language organizational text with symbolic paths/frontmatter. Substrate: Git source branches and compiled-tree mirror files; database rows identify live pages. Distinct from the ephemeral [RT-OBJ-pending](runtime.md#rt-obj-pending); consumed by [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile) and attachment routes, not a duplicate route record. SRC-1 `apps/api/src/agents/indexer/tools.ts`, `apps/api/src/agents/indexer/source-mirror.ts` (implementation).

> return { content: decoder.decode(bytes) };
> --- `apps/api/src/agents/indexer/tools.ts:54-72`

> path: okfDocGitPath(bundleSlug, `source/${page.path}.md`),
>       content: decoder.decode(bytes),
> --- `apps/api/src/agents/indexer/source-mirror.ts`

#### EPI-OBJ-concept-docs
Label: Compiled concept documents

Source-native identity: nonreserved OKF concept Markdown, distinct from its source mirror and index/log. Natural-language bodies and symbolic frontmatter live in Git agent/user/default branches. The candidate is a material value part of [RT-OBJ-pending](runtime.md#rt-obj-pending) while staged, but this referent is the cross-stage document, not only that map part. No supplied object declares that persisted referent. Its checks and postprocessing are [EPI-RTE-structural-check](#epi-rte-structural-check) and [EPI-RTE-resource-rewrite](#epi-rte-resource-rewrite). SRC-1 `apps/api/src/agents/indexer/tools.ts` (implementation).

> pending.set(validPath, content);
>       return { written: validPath };
> --- `apps/api/src/agents/indexer/tools.ts`

#### EPI-OBJ-session-draft
Label: Specialist draft and section proposals

Source-native identity: session draft and proposed replacement sections, natural-language Markdown stored with symbolic session/proposal status in Postgres. Different checks/consumers from compiled concepts. No supplied object counterpart; producer/retention evidence and passages are [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session), with admission separated in [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring). These are a container; whole-draft import and section-override save remain separate consumption paths there. SRC-1 `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/agents/specialist/page-edit-tools.ts` (implementation). No concrete candidate supplied.

#### EPI-OBJ-chat-answer
Label: Chat answer

Source-native identity: streamed assistant response and optional persisted assistant message parts. Natural-language answer text plus symbolic UI/tool parts; stream and authenticated Postgres history are substrates, not knowledge-base publication. No supplied object counterpart; [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat) supplies implementation and passage for the producing call. SRC-1 `apps/api/src/routes/chat.ts`. Actual proposition content cannot be individuated from source alone.

### Routes

#### EPI-RTE-structural-check
Label: Concept write structural admission
Part of: [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile)

Endpoints: model path/content → `validateDocPath` and `requireFrontmatterType` → error or pending mutation. Owner: tool code. Target/domain: relative Markdown paths and parseable YAML with a nonempty string `type`, with reserved index/log exceptions. Check result and disposition are separate ledger functions implemented by one branch. Code can veto a model proposal, not assess organizational truth. Open compilation task; model proposes, program decides structural eligibility; human MR review remains later. No expected-answer oracle. Retry after tool error is available; no durable change precedes successful staging. SRC-1 `apps/api/src/agents/indexer/tools.ts`, `apps/api/src/lib/okf-doc.ts` (implementation).

- Immediate return: error object or written-path acknowledgment.
- Later read-back: successful map values can be read by `read_existing_doc` during the run; later persisted consumption is owned by the parent compile route.
- Delegated visibility: tool result goes to indexer model only; no additional worker.
- Selection predicate: each write call; path normalization and frontmatter check, reserved-name exemption.
- Invalidation or expiry: pending replacement/deletion or run termination; no truth expiry rule.
- Activation or effect: error prevents map mutation; success permits staging.
- Evidence limits: structural admission only; no generated sample or semantic checker.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (RESERVED_DOCS.has(docPath)) return null;
> --- `apps/api/src/lib/okf-doc.ts`

> if (typeof type !== "string" || !type.trim()) {
> --- `apps/api/src/lib/okf-doc.ts`

The staging branch and its quote are also retained in [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile). A concept with valid `type` but unsupported body has no body-truth rejection branch here; this is a source-level countercase, not a claim of an observed false document.

#### EPI-RTE-resource-rewrite
Label: Resource URL normalization and fallback
Part of: [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile)

Endpoints: pending concept content plus live source-path set → inferred page path → rewritten resource field in pending. Owner: deterministic source-mirror helper. This material subroute changes lineage assertions, not the body proposition or its proof. Distinct function within the supplied compile container. SRC-1 `apps/api/src/agents/indexer/source-mirror.ts` (implementation); invocation is supplied by the parent route.

- Immediate return: void; mutates pending entries when a live source can be selected.
- Later read-back: rewritten resource is retained with compiled files and can be used for answer source links.
- Delegated visibility: inapplicable — helper executes in orchestrator, no new context.
- Selection predicate: nonnull, nonreserved, nonsource pending document; existing recognized source URL or single-source fallback.
- Invalidation or expiry: later pending rewrite/compile replaces the field; no source-support revocation check.
- Activation or effect: mechanically changes the source URL association, without evidence-consuming factual judgment.
- Evidence limits: URL transformation is inspectable; actual model-generated association and downstream reliance unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> pagePath = sourcePages.length === 1 ? sourcePages[0]!.path : pagePath;
> --- `apps/api/src/agents/indexer/source-mirror.ts`

> const nextFm = /^resource:\s*.*$/m.test(fm)
>     ? fm.replace(/^resource:\s*.*$/m, `resource: ${resourceUrl}`)
>     : `${fm.replace(/\s*$/, "")}\nresource: ${resourceUrl}`;
> --- `apps/api/src/agents/indexer/source-mirror.ts`

Concrete deduction, not target execution: let the slug be `team`, the only live source path be `payroll`, and pending `concepts/example.md` contain `---\ntype: Guide\n---\nUnrelated body.`. `extractResourcePath` returns null because no resource field matches. The one-source branch chooses `payroll`; rewriting inserts `resource: /wiki/team/source/payroll` before the closing delimiter and leaves the body unchanged. The procedure never inspects whether “Unrelated body.” is supported. This establishes deterministic association, not an entailed factual derivation or a reliable provenance claim. Other documents can preserve their existing recognized associations, so the countercase does not imply every resource is invented.

#### EPI-RTE-okf-edit
Label: Human OKF document save

Endpoints: PUT compiled-doc content → mode/path/read-only/type/permission gates → user-branch Git commit. Owner: caller supplies replacement; software checks shape/access and commits. Distinct from raw save/import [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring) and model compile [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile); no supplied route counterpart for direct compiled editing. SRC-1 `apps/api/src/routes/okf-docs.ts` (implementation).

- Immediate return: commit OID, branch and updated timestamp or rejection error.
- Later read-back: content GET prefers the caller's branch if it carries the file; published consumers still use default branch.
- Delegated visibility: inapplicable — HTTP save, no model worker.
- Selection predicate: compiled bundle, valid doc path, not readonly log, valid frontmatter, edit permission.
- Invalidation or expiry: subsequent saves/branch merges change content; no semantic expiry.
- Activation or effect: writes replacement to caller branch, not immediate published chat knowledge.
- Evidence limits: no human rationale or actual save supplied; caller identity does not prove semantic review.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes and elects save; software can veto invalid/unauthorized input. Open manual editing, not scored experimentation; no reference oracle. Guidance shaping text is unspecified. History/later edits provide revision substrate, not demonstrated rollback or accepted truth. Publication still needs its own path.

> const branch = await git.createUserBranch(user.id);
>     const commitOid = await git.writeAndCommit(
>       branch,
>       [{ path: okfDocGitPath(bundle.slug, docPath), content }],
> --- `apps/api/src/routes/okf-docs.ts`

#### EPI-RTE-version-restore
Label: Raw wiki version restore

Endpoints: review-authorized snapshot/restore request → selected version via Git helper → raw/OKF search reconciliation when restored. Owner: caller selects historical raw state; API/Git helper execute. Distinct from remote pull [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull): local historical snapshot, no remote import. This supplements the runtime's forcing routes. SRC-1 `apps/api/src/routes/wiki-versions.ts` (implementation and explicitly labelled explanatory comment).

- Immediate return: restored flag and page counts, or permission/version error.
- Later read-back: reconciled raw state enters later page reads/compilation; version branches can be listed/deleted; compiled search reconciliation is not recompilation.
- Delegated visibility: inapplicable — authorized HTTP operation, no delegated worker.
- Selection predicate: bundle review permission and named snapshot; creation can select a full commit OID.
- Invalidation or expiry: subsequent restore/edit can replace live raw state; deleting a version removes that named recovery handle.
- Activation or effect: helper is invoked and, on restored result, raw metadata and searchable state are reconciled without an MR in this endpoint.
- Evidence limits: core helper internals and exercised restoration uninspected; no factual or temporal fitness criterion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: reviewer-authorized caller chooses snapshot and can decline to trigger restore; program validates names/permission/existence, not truth. Open maintenance mode, no answer oracle or criticism requirement. No semantic improvement objective specified. Historical text persists through Git; helper comment describes a new commit preserving prior state, but actual recovery is not observed.

> const allowed = await checkPermission(db, request.user, bundle, null, "review");
> --- `apps/api/src/routes/wiki-versions.ts:116-126`

> result = await git.restoreBundleWikiVersion(bundle.slug, request.params.name, {
>           name: user.displayName,
>           email: user.email,
>         });
> --- `apps/api/src/routes/wiki-versions.ts`

> await reconcileOkfSearchIndex(db, git, bundle, embedder);
> --- `apps/api/src/routes/wiki-versions.ts`

#### EPI-RTE-page-delete
Label: Raw page and folder withdrawal

Endpoints: page or folder DELETE → exact name confirmation and edit checks → null Git writes on user branch → soft-deleted raw rows. Owner: caller withdraws content; API executes. Distinct from proposal rejection [RT-RTE-review-merge](runtime.md#rt-rte-review-merge); targets existing raw sources. SRC-1 `apps/api/src/routes/pages.ts` lines 368–522 (implementation). The future compile consumer excludes deleted pages as directly inspected in `apps/api/src/agents/indexer/tools.ts`.

- Immediate return: updated deleted page or folder count, or input/permission error.
- Later read-back: live-source inventory excludes soft-deleted rows; subsequent delta calculation can identify missing source paths and the model is instructed to delete related concepts.
- Delegated visibility: inapplicable — user/API withdrawal operation.
- Selection predicate: exact page title or folder name confirmation; existing live raw pages and edit permission at affected paths.
- Invalidation or expiry: Git history remains; later remote pull/restore can change raw state. No automatic expiry of compiled claims or stored chat answers.
- Activation or effect: null branch writes and immediate database soft-delete; ordinary merge is separate from this operation.
- Evidence limits: no downstream execution; not a synchronous global revocation or proof that every derivative is removed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Disposition: caller selects removal, software can veto missing confirmation/access. No claim-falsity evaluator or answer oracle. Open content maintenance; reason for withdrawal is not required. Future compilation uses prompt-level guidance, not an inspected compulsory cascade. This is an operative rejection/withdrawal route even without epistemic criticism.

> .set({ isDeleted: true })
>       .where(eq(schema.pages.id, page.id))
> --- `apps/api/src/routes/pages.ts`

> eq(schema.pages.isDeleted, false),
>       isNull(schema.pages.redirectTo),
> --- `apps/api/src/agents/indexer/tools.ts`

### Claims

#### EPI-CLM-source-fidelity
Label: Source-faithful compilation policy

Claimed operation: compile raw source into traceable OKF without invented facts; keep ambiguity. Distinct from [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat): constrains compilation rather than answering. SRC-1 `apps/api/src/agents/indexer/prompt.ts` (doctrine/design delivered by implementation). This is a requested constraint, not evidence of semantic success.

> Do not invent facts that are not in the source pages. If a source page is ambiguous, represent the ambiguity rather than resolving it yourself.
> --- `apps/api/src/agents/indexer/prompt.ts`

#### EPI-CLM-reviewed-publication
Label: Every published change reviewed

Claimed operation: universal review-and-approve before publication. Broader than [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat), which concerns chat's knowledge input. SRC-1 `PRD.md` (doctrine/design; inspected search passage). Alternate remote and restore routes prevent treating this as an invariant over all shipped admission.

> Every edit is a git commit under the hood, every published change went through a review-and-approve step, and the entire history is preserved
> --- `PRD.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
