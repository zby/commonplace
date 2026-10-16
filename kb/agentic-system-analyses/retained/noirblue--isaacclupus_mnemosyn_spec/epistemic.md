---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of IsaacCLupus_mnemosyn_spec: proposed audit and governance versus legacy publication and delegated backend authority."
run-id: AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01
reviewed-boundary: "0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92"
---

# IsaacCLupus_mnemosyn_spec epistemic report

## Source-and-claim boundary

The question is which routes turn source or conversational assertions into content licensed for later reliance, and which checks actually control that reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identity/layers: see [Source register](boundary.md#source-register), SRC-1. This remains a complete specification artifact with a partial implemented loop, not a completed knowledge OS. No target execution was performed. No observed-run or causal-experiment evidence was supplied.

Direct inspection covers the canonical architecture/specification, agent lifecycle guidance, complete heavy-compilation study, complete v0.2 draft, initial DDL, and complete legacy CLI, gateway and publisher. These extend the supplied runtime coverage with claim governance, profile promotion and optional proof export. Supplied runtime findings remain provisional; source checks confirm the consequential dispatch and publication asymmetries. No supplied finding requires supersession. The new route records are material parts or distinct future proposals, not relabelings of their containers.

| Entry point or operation | Source path, SRC-1 | Coverage and records / limit |
|---|---|---|
| CLI init/status/publish/serve-mcp/serve-proxy | `prior-art/v0-glue/jarvis_kb/cli.py` | Direct dispatch read; init/status are directory/tool-availability operations, not factual approval; publication and MCP routes below. Proxy internals supplied by runtime. |
| kb_ingest, kb_compile | `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | Direct complete handler read; see [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools). auto_approve forwards a flag, not verified approval. |
| kb_audit | `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | Direct read; see [EPI-RTE-audit-dispatch](#epi-rte-audit-dispatch). |
| kb_remember | `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | Direct read; see [RT-RTE-link-remember](runtime.md#rt-rte-link-remember). Backend admission opaque. |
| kb_search, kb_ask | `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | Direct read; see [RT-RTE-client-query](runtime.md#rt-rte-client-query). Source/budget labels do not enforce controls. |
| Publication, normalization, reload | `prior-art/v0-glue/jarvis_kb/vault_sync.py` | Direct read; see [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish), [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping). |
| Model generate/chat routing | `prior-art/v0-glue/jarvis_kb/ollama_proxy.py` | Supplied [RT-RTE-model-proxy](runtime.md#rt-rte-model-proxy); no direct provider inspection. Semantic generation and compliance remain opaque. |
| Extract/compile/audit/finalize study | `python_thoughts/05-heavy-llm-compilation.md` | Direct complete read; separated generation, checking, disposition and integration below. Markdown normalization can change links, not just typography. |
| Approve, memory commit/archive, write guards | `ARCHITECTURE.md`, `AGENTS.md`, `SPECIFICATION.md` | Direct reads; design only. See [RT-CLM-write-guards](runtime.md#rt-clm-write-guards) and integration record. |
| SQLite views, constraints, cascade and timestamp trigger | `schema/001-init.sql` | Direct complete read; structural constraints and stage views, not factual checks or approval enforcement. No populated runtime DB supplied. |
| Phase 2–4 profiles, governance hooks/verdicts, proof export | `MNEMOSYNE_SPEC_v0.2.md` | Direct complete read; draft proposals separately assessed below. Receipts/logging report operations, not epistemic acceptance. |
| Watcher/incremental compile and unified API sketches | `rust_thoughts/04-file-watcher-incremental-compile.md`, `rust_thoughts/03-axum-mcp-rest.md` | Scoped search only, not full inspection. Rejection/unblock and further API proposals remain unassessed; prevents a system-complete negative about proposed adaptation/admission. |
| Other extraction/graph/pack studies and historical spec | `python_thoughts/`, `rust_thoughts/`, `MNEMOSYNE_SPEC_v0.1.md` | Not fully inspected; prevents complete enumeration of proposed transformations and controls. No inference of absence. |

External Synto, Synthadoc, LLM-WIKI, Link, Ollama weights/providers and live agents are excluded frozen dependencies, not inspected evaluators. Their missing code prevents knowing semantic preservation, source warrant, remote approval and retrieval behavior. Missing candidates/traces prevent identifying an actual conjecture, acceptance, activated authority or successful withdrawal. Missing interventions/comparisons prevent causal attribution, calibration and quality-benefit claims. Distributed-parametric limits: see [RT-CMP-fast-model](runtime.md#rt-cmp-fast-model), [RT-CMP-heavy-model](runtime.md#rt-cmp-heavy-model), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model); no claim of fixed weights or online learning is licensed by configuration alone.

Knowledge/warrant claims: see [EPI-CLM-audit-quality](#epi-clm-audit-quality), [EPI-CLM-memory-commit](#epi-clm-memory-commit), [EPI-CLM-governance-proof](#epi-clm-governance-proof), [RT-CLM-publish-atomicity](runtime.md#rt-clm-publish-atomicity), [RT-CLM-write-guards](runtime.md#rt-clm-write-guards).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-article-output](#epi-obj-article-output) | see record | see record | SRC-1, `python_thoughts/05-heavy-llm-compilation.md` | No candidate output; semantics not determinable. |
| [EPI-OBJ-audit-result](#epi-obj-audit-result) | see record | see record | SRC-1, `python_thoughts/05-heavy-llm-compilation.md` | Schema does not verify assertions. |
| [EPI-OBJ-unified-pages](#epi-obj-unified-pages) | see record | see record | SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py` | Producer approval lineage not preserved in full. |
| [EPI-OBJ-governance-state](#epi-obj-governance-state) | see record | see record | SRC-1, `MNEMOSYNE_SPEC_v0.2.md` | Draft tables, no populated verdict. |
| [EPI-OBJ-user-profiles](#epi-obj-user-profiles) | see record | see record | SRC-1, `SPECIFICATION.md` | No concrete fact or verification algorithm. |
| [RT-OBJ-compile-template](runtime.md#rt-obj-compile-template) | see record | see record | SRC-1, `python_thoughts/05-heavy-llm-compilation.md` | Prompt is instruction, not factual guarantee. |
| [RT-RTE-link-remember](runtime.md#rt-rte-link-remember) | see route for opaque caller memory | see route | SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | Link state/form beyond payload uninspected. |
| [RT-RTE-client-query](runtime.md#rt-rte-client-query) | see route for opaque answers/retrieved pages | see route | SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | No actual answer or full retrieval context. |

## Authority-route ledger

Each row names a consequential function. The linked declaration owns endpoints, target/evaluator, result, force, scope, consumer/channel/horizon and activation limits; those fields are not re-declared here. Architectural status is local to this overlay. Multiple functions of a supplied container remain separate rows, not a claim that retention equals integration.

Route ID: [EPI-RTE-article-generation](#epi-rte-article-generation)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-article-generation](#epi-rte-article-generation).
Content/update relation: truth-apt transformation: indeterminate.
Evidence source ID and local anchor: SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-article-audit](#epi-rte-article-audit)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-article-audit](#epi-rte-article-audit).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-article-disposition](#epi-rte-article-disposition)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-article-disposition](#epi-rte-article-disposition).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-article-integration](#epi-rte-article-integration)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-article-integration](#epi-rte-article-integration).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `ARCHITECTURE.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping).
Content/update relation: non-truth-apt policy/content update: confidence/status mapped to maturity.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping).
Content/update relation: truth-apt transformation: acquisition/import.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-audit-dispatch](#epi-rte-audit-dispatch)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-audit-dispatch](#epi-rte-audit-dispatch).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-claim-governance](#epi-rte-claim-governance)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-claim-governance](#epi-rte-claim-governance).
Content/update relation: truth-apt transformation: indeterminate.
Evidence source ID and local anchor: SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-claim-governance](#epi-rte-claim-governance)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-claim-governance](#epi-rte-claim-governance).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-profile-promotion](#epi-rte-profile-promotion)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-profile-promotion](#epi-rte-profile-promotion).
Content/update relation: truth-apt transformation: indeterminate.
Evidence source ID and local anchor: SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-profile-promotion](#epi-rte-profile-promotion)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-profile-promotion](#epi-rte-profile-promotion).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-profile-promotion](#epi-rte-profile-promotion)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-profile-promotion](#epi-rte-profile-promotion).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-proof-export](#epi-rte-proof-export)
Route function: lineage/freshness/recovery
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-proof-export](#epi-rte-proof-export).
Content/update relation: truth-apt transformation: indeterminate.
Evidence source ID and local anchor: SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [EPI-RTE-markdown-normalization](#epi-rte-markdown-normalization)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [EPI-RTE-markdown-normalization](#epi-rte-markdown-normalization).
Content/update relation: truth-apt transformation: indeterminate.
Evidence source ID and local anchor: SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools).
Content/update relation: truth-apt transformation: acquisition/import.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-link-remember](runtime.md#rt-rte-link-remember)
Route function: retention
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-link-remember](runtime.md#rt-rte-link-remember).
Content/update relation: truth-apt transformation: acquisition/import.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)
Route function: retention
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish).
Content/update relation: truth-apt transformation: acquisition/import.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-client-query](runtime.md#rt-rte-client-query)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-client-query](runtime.md#rt-rte-client-query).
Content/update relation: no content change.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

Route ID: [RT-RTE-client-query](runtime.md#rt-rte-client-query)
Route function: content transformation
Architectural status: not determinable
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path: see [RT-RTE-client-query](runtime.md#rt-rte-client-query).
Content/update relation: truth-apt transformation: indeterminate.
Evidence source ID and local anchor: SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.
Claim IDs: see comparison below. Mismatch marker: design versus legacy where applicable. Gap/limit: no observed operation; delegated semantics remain uninspected.

For delegated ingest/remember and legacy publication, source assertions enter but their original warrant is unknown; normalization demonstrably degrades governance metadata. For query synthesis, the adapter only requests and returns an external answer: it does not individuate the produced propositions or their semantic relation to premises. These distinctions do not classify arbitrary opaque backend generation as ampliative conjecture. Legacy selection grants operational exposure to later queries, not epistemic acceptance. The gateway audit result is advisory to its caller; the design threshold result is intended to enforce promotion. No implemented result-to-policy-update route is established by the inspected gateway/publisher; the uninspected incremental studies prevent a repository-wide absence claim.

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant and source layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|
| [EPI-CLM-audit-quality](#epi-clm-audit-quality) | see record | see record | [EPI-RTE-audit-dispatch](#epi-rte-audit-dispatch), [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping) | none supplied | No comparative truth or quality evaluation | Proposed checking and threshold admission are separate | Reporting checks and labeling maturity are not validated knowledge production. |
| [EPI-CLM-memory-commit](#epi-clm-memory-commit) | see record | see record | [RT-RTE-link-remember](runtime.md#rt-rte-link-remember) | none supplied | Link admission semantics external | Proposed audited/human lifecycle | Direct remember adapter does not locally implement inbox/audit/approval. |
| [EPI-CLM-governance-proof](#epi-clm-governance-proof) | see record | see record | none established for draft claim verdict/proof routes | none supplied | Merkle integrity is not truth; reversibility open | Governance and proof proposals only | Evidence references/trust labels do not demonstrate acceptance. |
| [RT-CLM-publish-atomicity](runtime.md#rt-clm-publish-atomicity) | see record | see record | [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish) | none supplied | Sequential files/subprocesses, no shared rollback | Best-effort legacy exposure | Not the claimed unified atomic publication. |
| [RT-CLM-write-guards](runtime.md#rt-clm-write-guards) | see record | see record | [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish) | none supplied | Guard fields/DDL are not authenticated enforcement | Policy declared | Copier overwrites without checking guards. |

## Bounded conclusion

**Implemented bridge authority is operational, not a demonstrated acceptance of new knowledge.** It delegates import, compilation, memory and checking; copies selected pages; removes governance metadata; requests index/reload; and returns retrieved material or generated backend text. See [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools), [RT-RTE-link-remember](runtime.md#rt-rte-link-remember), [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish), [RT-RTE-client-query](runtime.md#rt-rte-client-query). The downstream path is page files → requested backend index/load → client query result, with permissive exposure across invocations and interpretive influence thereafter. Successful reload, client reliance and factual benefit remain unobserved. Synto draft-path exclusion is a limited admission rule; Synthadoc and direct remember routes prevent treating it as universal human approval. Audit calls do not locally veto publication. Stale destinations can survive source removal; no inspected bridge retraction propagates a contrary audit result.

**The proposed architecture separates checks and admission, but its epistemic license is bounded.** See [EPI-RTE-article-audit](#epi-rte-article-audit), [EPI-RTE-article-disposition](#epi-rte-article-disposition), [EPI-RTE-article-integration](#epi-rte-article-integration). Structural validity licenses structure; consistency checks license only their comparison domain; model review remains fallible candidate criticism. A score threshold and optional human veto license intended wiki use operationally, not demonstrated source truth, accepted ampliative claims or successful lifecycle integration. Imported assertions are acquired, not produced. No inspected candidate plus warranted premises supports a specific entailed derivation. No supplied source/output pair establishes non-entailment for a concrete ampliative conjecture. These are local evidence limits, not assertions that models never conjecture.

**Policy labels can outrun evidence.** [EPI-RTE-maturity-mapping](#epi-rte-maturity-mapping) establishes by inspected branches that contradicted content with numeric confidence 0.9 is labeled established. That changes a persisted label and strips approval/audit detail; downstream ranking force is unknown. The body is preserved, so this is not evidence of a novel factual proposition being generated or validated.

**Future routes remain separate.** [EPI-RTE-claim-governance](#epi-rte-claim-governance) adds proposed claim-scoped verdicts and dissent, but no executed evidence-consuming verdict or withdrawal consumer. [EPI-RTE-profile-promotion](#epi-rte-profile-promotion) separates inferred user facts, relevance selection and human commitment; heat/freshness is not endorsement. [EPI-RTE-proof-export](#epi-rte-proof-export) concerns integrity/provenance of serialization, not truth. Profile visibility, verdict reversibility and semantic fidelity remain open or unimplemented in inspected evidence.

Learning, reflection, autonomy and theory building do not follow from retention or audit labels. The independent design-level theory condition limits and proposed rejection-feedback iteration remain as stated in [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle). Improved future capacity, two-way machinery self-representation and exercised self-improvement remain unestablished independently; no system-wide negative is inferred from missing traces or partial study coverage. There is no single epistemic score or system-wide verdict here.

## Shared records

### Operative objects

#### EPI-OBJ-article-output
Label: ArticleOutput
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Material article object within that route, not a duplicate of its workflow container or the supplied template. Source-native ArticleOutput contains natural-language title/summary/sections/citation quotes plus symbolic confidence and lists; proposed files/SQLite pages/links store it. Candidate assertions concern the ingested subject domain; no instance is supplied. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

>     sections: List[Section] = Field(description='Article sections')
>     cross_links: List[str] = Field(description='Wikilink targets to related pages')
>     confidence: float = Field(ge=0.0, le=1.0, description='Overall confidence')
> --- `python_thoughts/05-heavy-llm-compilation.md`

#### EPI-OBJ-audit-result
Label: AuditResult and ContradictionReport
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Material check-result part, distinct from the article/template. Natural-language conflicting claim descriptions and recommendations sit in symbolic structured artifacts intended for audit_log/contradictions and audit JSON. A contradiction assertion is truth-apt over specified claim pairs; score alone is an evaluation signal. No result supplied. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

>     claim_a: str = Field(description='First conflicting claim')
>     claim_b: str = Field(description='Second conflicting claim')
>     severity: str = Field(description='low | medium | high | critical')
>     resolution: str = Field(description='Suggested resolution or note')
> --- `python_thoughts/05-heavy-llm-compilation.md`

#### EPI-OBJ-unified-pages
Label: Unified vault pages
Part of: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)

Material retained output part of publication. Markdown natural-language assertions and selected symbolic frontmatter reside in unified-vault files and are supplied to external indexers. Body provenance originates with external producer pages; local source_tool/synced_at report copying, not approval. Distinct from runtime's publication route, not a new alias for it. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

>         post.metadata = clean
>         dst.parent.mkdir(parents=True, exist_ok=True)
>         dst.write_text(frontmatter.dumps(post), encoding="utf-8")
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

#### EPI-OBJ-governance-state
Label: Claims verdicts dissents

No supplied counterpart after comparison: draft Phase 3 per-claim governance is not the current page-level design lifecycle. Natural-language claim/rationale/counter-evidence and symbolic statuses/references are proposed SQLite rows and versioned pack state. Claim truth is domain-specific; endorsement is a disposition, not infallibility. SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.

>     verdict_type TEXT CHECK (verdict_type IN ('endorse', 'reject', 'downgrade', 'supersede')),
>     rationale TEXT,
>     verdict_by TEXT, -- user_id or agent_id
>     verdict_at TEXT,
>     evidence_refs TEXT -- JSON: [claim_id, page_id, etc.]
> --- `MNEMOSYNE_SPEC_v0.2.md`

#### EPI-OBJ-user-profiles
Label: user_profiles

No supplied object counterpart: the Phase 2 implicit profile table differs from opaque direct Link memory. Natural-language key/value facts in symbolic SQLite fields carry confidence and conversation provenance. Intended user/time-scoped facts, not supplied factual instances. The canonical specification adopts fields, not a working verification route. SRC-1, `SPECIFICATION.md`.

> Implicit facts extracted from conversations by the fast model:
> --- `SPECIFICATION.md`

### Routes

#### EPI-RTE-article-generation
Label: Article generation
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Raw source and extracted concepts → proposed fast/heavy models → typed article, claims, citations and confidence. Owner: proposed OS and Python satellite. Natural-language claims are represented inside symbolic typed containers, intended for files and SQLite pages/links. Model versions and mutability: see the supplied fast/heavy component records. No concrete output was supplied. Extraction acquires source assertions; generated article semantics are indeterminate between faithful reshaping, entailed elaboration and ampliative conjecture. The instruction to generate an article does not prove any one relation. Source reliability and confidence are model judgments, not independently checked warrant. Open ingestion requests, not a curriculum. Guidance is the compilation template; sources and related summaries enter model input. Neither delivery nor citations establish compliance or source truth. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

This isolates a material function within [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle); the parent remains a valid container.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed ConceptExtraction and ArticleOutput.
- Later read-back: Proposed article files/pages feed later audit, compilation and query; no artifact or consumption trace supplied.
- Delegated visibility: Source text, concepts, related-page summaries and flagged conflicts are proposed model inputs.
- Selection predicate: Source type, maturity, namespace and template version select guidance.
- Invalidation or expiry: uninspected — deployed incremental invalidation is not present in the inspected bridge.
- Activation or effect: Requests extraction, article writing, citations and confidence, without demonstrated semantic preservation.
- Evidence limits: Design example, not wired unified runtime; no candidate instance, model trace or factual oracle.

>     - Extract concepts, entities, key claims
>     - Identify link opportunities
>     - Score source reliability
> --- `python_thoughts/05-heavy-llm-compilation.md`

#### EPI-RTE-article-audit
Label: Article audit
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Draft article and existing pages → proposed structural lint, heavy-model contradiction detection and adversarial review → AuditResult. Owner: proposed audit engine. Targets differ: markdown/link syntax is a structural domain; pairs of article/existing-page claims are the consistency domain; factual error is the intended adversarial domain. Agreement with existing pages cannot establish their truth or adjudicate which conflicting source is wrong. Pydantic type/range checking licenses shape and numeric bounds, not citation occurrence or factual correctness. The risk table proposes source-ID validation but the illustrated Citation schema merely describes a quote. Model judgment supplies no expected-answer oracle. Audit reporting is separate from admission below. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

This isolates a material function within [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle); the parent remains a valid container.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed audit score, issues and recommendations or contradiction report.
- Later read-back: Proposed audit artifacts persist for finalize/rejection feedback; actual use unobserved.
- Delegated visibility: New article and existing page text reach the proposed contradiction model.
- Selection predicate: Stage 3 after generation; model checks requested by audit template.
- Invalidation or expiry: uninspected — no deployed re-audit/withdrawal protocol supplied.
- Activation or effect: Intended advisory evidence for the separate threshold/human disposition.
- Evidence limits: No ground-truth comparison, calibration, citation verifier implementation or observed audit supplied.

> Compare the following new article against existing pages in the knowledge base.
> Identify any contradictions, conflicts, or inconsistencies.
> --- `python_thoughts/05-heavy-llm-compilation.md`

#### EPI-RTE-article-disposition
Label: Publish or reject
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

AuditResult → proposed threshold comparison and optional human gate → promotion or draft with feedback. Owner: proposed finalizer/core. Models propose the article and audit; code compares a score with an unspecified threshold; a human may veto if configured. Intended use is admission to wiki for later knowledge queries and compilation. Criterion is audit score plus configured approval, not a demonstrated evidence-consuming truth decision over individually scoped propositions. Rejection feedback is retained to guide another compilation; coordinated rollback is unspecified. This is open-request knowledge admission, not an evaluated learning experiment. Proposed guidance is the audit/compile templates. Publication could operationally grant reliance without establishing accepted ampliative knowledge under this analysis contract. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

This isolates a material function within [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle); the parent remains a valid container.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed published article or rejected draft with feedback.
- Later read-back: Proposed rejection_feedback guides recompilation; approved wiki pages feed query/compile.
- Delegated visibility: Finalizer receives article and audit files; human review visibility not fully specified.
- Selection predicate: Score >= threshold versus score < threshold, with human approval if configured.
- Invalidation or expiry: uninspected — complete retraction and multi-store rollback semantics not supplied.
- Activation or effect: Intended enforcing publish/reject choice, not observed acceptance.
- Evidence limits: Threshold, factual criterion, actual human decisions and artifacts unavailable.

>     - Score >= threshold: promote to wiki/
>     - Score < threshold: return to drafts/ with feedback
>     - Human approval gate (if configured)
> --- `python_thoughts/05-heavy-llm-compilation.md`

#### EPI-RTE-article-integration
Label: Approved graph integration
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Proposed approved pages/memories → publish/graph engine → linked searchable wiki or committed memory. Owner: proposed OS, conditional on approval. This is a distinct post-admission function, not evidence that acceptance occurred. Semantic license is inherited from the preceding content-specific decision, whose factual warrant remains unestablished. Operational path: published pages and graph links → query or compilation context → interpretive influence on later model/client decisions across sessions. Index/graph/pack updates are declared transactional; the legacy publisher does not implement that shared transaction. SRC-1, `ARCHITECTURE.md`.

This isolates a material function within [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle); the parent remains a valid container.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed published pages, rebuilt graph/index/packs.
- Later read-back: Later query and compile requests select approved material; no observed read-back.
- Delegated visibility: Proposed engines receive accepted article and graph relationships.
- Selection predicate: Approved lifecycle stage, not merely storage.
- Invalidation or expiry: uninspected — withdrawal propagation across graph/packs is unspecified in inspected design.
- Activation or effect: Intended post-approval organization and later use.
- Evidence limits: No acceptance artifact or successful lifecycle integration trace; cannot infer it from retention.

> ├── memory/
> │   ├── inbox/               # proposed memories
> │   └── committed/           # approved, linked to graph
> --- `ARCHITECTURE.md`

#### EPI-RTE-maturity-mapping
Label: Confidence to maturity
Part of: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)

Producer frontmatter → _normalize_frontmatter → selected metadata on disk. Owner/evaluator: deterministic Python branch. Target: producer metadata, not article truth. Concrete static deduction: confidence=0.9 and status=contradicted selects established, because the numeric branch runs before the contradicted branch. confidence=0.8 selects refining, not established; without numeric confidence, contradicted selects disputed. The body remains intact. clean retains selected title, maturity, source_tool, timestamp, provenance/source and optional citations, dropping approval/audit/hash fields. Thus article assertions are imported with degraded governance lineage, while maturity is a policy label rather than an entailed epistemic assessment. No execution was performed. This disproves a reading that contradicted always yields disputed; it does not show a deployed false answer. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

This isolates a material function within [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish); the parent remains a valid container.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized markdown written to self/ or world/.
- Later read-back: Written page metadata/body enters requested indexing and later backend query; downstream maturity weighting is unknown.
- Delegated visibility: Indexer receives normalized markdown, not all producer metadata.
- Selection predicate: Numeric thresholds take precedence over status; Synto path filter is a separate admission step.
- Invalidation or expiry: Publication rewrites selected destinations; no source-deletion reconciliation in inspected loops.
- Activation or effect: Writes maturity and removes governance metadata without checking content truth.
- Evidence limits: Implementation deduction only; real inputs, backend ranking and answer effects unobserved.

>         if isinstance(confidence, (int, float)):
>             maturity = "established" if confidence > 0.8 else "refining" if confidence > 0.5 else "seed"
>         elif status == "contradicted":
>             maturity = "disputed"
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

#### EPI-RTE-audit-dispatch
Label: Gateway audit dispatch
Part of: [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools)

kb_audit → Synto eval / Synthadoc lint / Link validate → caller result. Owner: gateway selects services; external tools evaluate. Check target is the selected backend KB, but exact predicates, factual domain and algorithms are unavailable. Scope self selects Synto, world selects Synthadoc, all selects both; Link is always attempted. The handler returns output without consuming it to gate compile, remember, publish or queries. This adapter therefore implements check requests and advisory reporting, not a local evidence-consuming acceptance or withdrawal policy. Human/software caller identity remains unresolved; caller may act outside this boundary. No expected answers supplied. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

This isolates a material function within [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools); the parent remains a valid container.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Backend-labeled output or Link error inside MCP text.
- Later read-back: inapplicable — gateway audit results are not retained or reloaded by this handler; backend retention is uninspected.
- Delegated visibility: Selected backend receives eval/lint command or validate HTTP request, not a locally selected proposition.
- Selection predicate: Tool dispatch plus scope; always attempt Link validation.
- Invalidation or expiry: inapplicable — no gateway audit state to expire; backend lifecycle unknown.
- Activation or effect: Returns advisory diagnostics; no local consequential gate consumes their content.
- Evidence limits: Backend evaluation meaning, results and caller consequences unavailable; not evidence that checks passed.

>         return {"scope": scope, "results": results}
> --- `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`

#### EPI-RTE-claim-governance
Label: Claim verdict governance

Draft Phase 3 design: article → claim extraction → governance queue → human endorse/reject/downgrade → publish or return to draft. This is distinct from the current lifecycle container: it adds claim-level state, evidence_refs, rationale, dissent/counter-evidence and superseded_by. Closest supplied record is the broader current design lifecycle, not an existing claim-governance implementation. Claim text and rationale are natural language inside symbolic SQLite rows. Human verdict is the declared decision maker; extraction proposer is model-driven in the audit context. Intended use is governed publication/reliance on particular claims. The draft stores evidence references but specifies neither a sufficient truth criterion nor how a human must consume evidence. Verdict reversibility is explicitly open. Proposed statuses alone do not implement withdrawal from existing query results, graph context or exported packs. No observed accepted claim follows. SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed verdict and claim status, publication or draft return.
- Later read-back: Versioned claim state proposed for packs; consumers of supersession/dissent not implemented in inspected bridge.
- Delegated visibility: Human governance queue is proposed to receive extracted claims; evidence_refs fields can hold claim/page references.
- Selection predicate: Governance pass after adversarial review, Phase 3 only.
- Invalidation or expiry: uninspected — reversibility and withdrawal propagation are open design questions.
- Activation or effect: Intended human veto and scoped claim reliance; not deployed authority.
- Evidence limits: Draft only; no criterion-specific verdict, consumer or executed revocation evidence.

>   4. [NEW] Claim extraction → propose claims to governance queue
>   5. [NEW] Human verdict (endorse/reject/downgrade)
>   6. Publish or return to draft
> --- `MNEMOSYNE_SPEC_v0.2.md`

#### EPI-RTE-profile-promotion
Label: Conversation profile promotion

Proposed conversation log → fast-model key-fact extraction → user_profiles/proposed memories → heat/decay selection → inbox → human approval → committed memory, with cold memories archived. Distinct from supplied Link remember dispatch: automatic extraction and relevance-based promotion are future design, not that direct adapter. Closest overlap is the current memory lifecycle in the design container. Targets include user job/location/interests, truth-apt within a user/time scope, but no concrete extraction or source utterance supplied. Relation remains indeterminate between acquisition/reshaping and inference; implied profiles need not be entailed by conversation. Heat is reference frequency/decay relevance, not verification. Human approval is separate from heat selection, with no named factual criterion. Profile visibility is explicitly open; do not infer user-profile injection into agent prompts. Caller/agent operation is open conversation use, not a curriculum. SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed extracted profile values, proposed or committed memories, archived cold records.
- Later read-back: Committed memories are intended for later retrieval; direct profile visibility remains open.
- Delegated visibility: Fast model receives conversations; approval queue receives proposed memories.
- Selection predicate: References update heat, daily decay selects hot/cold material, human approves commitment.
- Invalidation or expiry: Cold material archived for provenance; last_verified_at/status fields do not define a verification algorithm.
- Activation or effect: Intended retention and human-controlled commitment; heat changes selection, not truth.
- Evidence limits: No runtime wiring, extracted fact, acceptance decision or later behavioral trace supplied.

>   2. Fast model extracts key facts → `user_profiles` + proposed memories
>   3. Heat score updated on reference
>   4. Decay job runs daily (background)
>   5. Hot mid-term memories promoted to `memory/inbox/`
>   6. Human approves → `memory/committed/`
>   7. Cold memories archived (retained for provenance)
> --- `MNEMOSYNE_SPEC_v0.2.md`

#### EPI-RTE-proof-export
Label: Optional proof export

Approved article → pack/RDF → optional Merkle root/anchor → packs/latest and optional DKG submission. Owner: proposed publish engine, Phase 4 draft. Distinct from current atomic-publish claim: optional external proof and trust-tier labels are an additional proposal. Target/domain for hashing is identity/integrity of serialized bytes relative to a root, not truth of claims, RDF encoding fidelity or source reliability. No verifier algorithm, verification result or warranted consensus is supplied. Serialization may reshape claims but fidelity is indeterminate without an encoding contract. Approval precedes proof export; an anchor is not a new factual acceptance decision. No rollback or proof-based veto implementation inspected. SRC-1, `MNEMOSYNE_SPEC_v0.2.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed serialized pack, root and optional transaction/network submission.
- Later read-back: Export intended for later external consumption; verifier behavior unavailable.
- Delegated visibility: Optional external system receives pack/proof; this is not new source evidence about that system.
- Selection predicate: Optional DKG mode after article approval.
- Invalidation or expiry: uninspected — proof invalidation and retraction protocols unspecified.
- Activation or effect: Intended provenance/integrity checking affordance, not truth warrant.
- Evidence limits: Draft only; no proof, verifier execution, external consensus or successful export supplied.

>   3. [OPTIONAL] Serialize to RDF
>   4. [OPTIONAL] Compute Merkle root
>   5. [OPTIONAL] Anchor to blockchain
>   6. Publish pack to `packs/latest/`
>   7. [OPTIONAL] Submit to DKG network
> --- `MNEMOSYNE_SPEC_v0.2.md`

#### EPI-RTE-markdown-normalization
Label: Markdown normalization
Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

Illustrative normalize_markdown receives model text and rewrites headings, links, citation markers and blank lines. Owner: proposed satellite postprocessor; not an installed module. Concrete static deduction from the displayed regex: [Report](https://example.org/evidence) becomes [[Report]], discarding the original URL. The same rule maps [Report](https://other.example/contrary) to that identical wikilink. This is not guaranteed non-ampliative semantic preservation: external evidence addresses collapse to a title-based resolver. Article sentences need not change, but provenance and reference meaning can. Relation is indeterminate between faithful reshaping and changed reference/content; the missing fact is whether resolved titles identify the same evidence. This is a source-code deduction about an illustrative study function, not executed target behavior or a wired runtime. It is a counterexample to treating every normalization in the repository as typography only. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

This isolates a material function within [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle); the parent remains a valid container.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Proposed normalized markdown string.
- Later read-back: Normalized articles are intended for persistence and graph extraction; actual calls and downstream resolution are unobserved.
- Delegated visibility: Postprocessor receives generated markdown; later wikilink extraction receives rewritten targets.
- Selection predicate: Regex match on ordinary Markdown links, regardless of URL identity.
- Invalidation or expiry: uninspected — no preserved URL map or deployed undo mechanism supplied.
- Activation or effect: Would replace explicit evidence addresses with local title references if used.
- Evidence limits: Design snippet only; no invocation or fidelity test supplied.

>     # Ensure wikilinks use [[Page Name]] format
>     text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[[\1]]', text)
> --- `python_thoughts/05-heavy-llm-compilation.md`

### Claims

#### EPI-CLM-audit-quality
Label: Three-pass quality gate

Claimed operation: structural lint, contradiction detection and adversarial review gate knowledge publication. Distinct from [RT-CLM-publish-atomicity](runtime.md#rt-clm-publish-atomicity): this claim concerns content quality, not transactionality. Support is doctrine/design, SRC-1, `ARCHITECTURE.md`; proposed checks and admission are separated in the article routes above. No observed quality or causal effect supplied.

> Three-pass quality gate (Synthadoc-style):
> 1. Structural lint (orphans, missing targets)
> 2. Contradiction detection (blocking vs. warning)
> 3. Adversarial review (devil's advocate critique)
> --- `ARCHITECTURE.md`

#### EPI-CLM-memory-commit
Label: Audited memory commitment

Claimed operation: agent proposal is reviewed and approved before graph commitment, with configurable automatic approval. Distinct from supplied publication/write-guard claims; closest route is [RT-RTE-link-remember](runtime.md#rt-rte-link-remember), whose local implementation forwards directly to an excluded backend. Doctrine/design only for the unified lifecycle. SRC-1, `AGENTS.md`.

> The agent proposes → OS stores in `memory/inbox/` → Audit engine checks → Human approves → Committed to graph.
> --- `AGENTS.md`

#### EPI-CLM-governance-proof
Label: Future governance and provenance

Claimed operations: draft additions of claim/verdict/dissent governance and optional cryptographic provenance/external verification. These are two distinct future warrants, not one truth oracle. No counterpart among supplied current atomicity or write-guard claims. SRC-1, `MNEMOSYNE_SPEC_v0.2.md`, doctrine/design. Claim-governance and proof-export route records bound their separate meanings; no observed support.

> 1. **Epistemic governance** (aminglab/knowledge-os) — claim/verdict/dissent lifecycle
> --- `MNEMOSYNE_SPEC_v0.2.md`

> The publish engine (Layer 5) gains an optional **external verification** step:
> --- `MNEMOSYNE_SPEC_v0.2.md`
