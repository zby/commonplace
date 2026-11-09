---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OKF epistemic routes: source attribution, human review, structural checks, consequential trust metadata and consumer-side computation attestation."
run-id: AAS-2026-11-08-okf-8bc42addf404-01
reviewed-boundary: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
---

# OKF epistemic report

## Source-and-claim boundary

Question: what can license reliance on OKF's retained claims, and which results actually change admission or later use? The scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register), SRC-1. This is the shipped four-gem, skill, plugin and Pro ecosystem, not just the baseline library. External model reasoning, host enforcement, optional SQLite implementation and adopter computations remain outside inspected implementation.

The runtime is a supplied provisional account, not a source-inspection ceiling. Its principal route identities are retained below. Direct reads added the produce/curate procedures, authoring policy, SPEC §10, Concept trust derivation, Validator/Linter predicates, RowFilter, Pro reconciliation, attestation inventory, pairing, audit and Stop consumers. All direct findings below are SRC-1 implementation or doctrine/design; none is observed operation or causal evidence. No target code was executed.

| Entry point or operation | SRC-1 source path | Coverage and consequence |
|---|---|---|
| Baseline CLI registration; extension loading | `gems/okf/lib/okf/cli.rb` | Direct registration read; supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). Built-in readers/checks and installed extension seam distinguished. Arbitrary third-party code is not inspected. |
| Produce, maintain, curate, consume | `skills/okf/playbooks/produce.md`, `skills/okf/playbooks/maintain.md`, `skills/okf/playbooks/curate.md`, `skills/okf/reference/authoring.md` | Direct doctrine reads plus supplied [RT-RTE-skill-work](runtime.md#rt-rte-skill-work); [EPI-RTE-semantic-review](#epi-rte-semantic-review), [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition). No instantiated before/after semantic candidate or review trace. |
| Migration and structural/instruction restructuring | `skills/okf/reference/authoring.md`, `skills/okf/playbooks/refine.md`, `skills/okf-principles/SKILL.md` | Authoring migration doctrine directly read; refine/principles supplied [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal). Full migrate implementation procedure uninspected; prevents complete semantic-preservation account of migrations. |
| Parse/check/publish | `gems/okf/lib/okf/concept.rb`, `gems/okf/lib/okf/bundle/validator.rb`, `gems/okf/lib/okf/bundle/linter.rb` | Direct selected method reads; [EPI-RTE-structural-check](#epi-rte-structural-check), [EPI-RTE-trust-tier](#epi-rte-trust-tier); Reader/Writer supplied [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle). Not an exhaustive validator audit. |
| MCP registered tools, resources and filters | `gems/okf-mcp/lib/okf/mcp/server.rb`, `gems/okf/lib/okf/bundle/row_filter.rb` | Direct tool-list/search/read/catalog/RowFilter inspection; resources/cache/output cuts supplied [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve). Fourteen tools provide discovery, reads and structural reports, not an exposed per-run attester executor. |
| Browser/TUI and registry | `gems/okf/lib/okf/server/app.rb`, `gems/okf/lib/okf/server/hub.rb`, `gems/okf-tui/lib/okf/tui/workspace.rb` | Supplied runtime account and [RT-RTE-registry-manage](runtime.md#rt-rte-registry-manage); detailed rendering uninspected here. Prevents exhaustive UI trust-display assessment, not the supplied registry-selection conclusion. |
| Base post-edit feedback | `plugin/hooks/scripts/curate.rb` | Supplied [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback); post-edit advisory force, not rejection. |
| Pro check dispatch, pre-edit asks, post-edit, Stop, SessionStart, audit, records | `gems/okf-pro/lib/okf/pro/cli.rb`, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json`, `gems/okf-pro/lib/okf/pro/closing.rb`, `gems/okf-pro/lib/okf/pro/audit.rb`, `gems/okf-pro/lib/okf/pro/records.rb` | Direct selected dispatch and consumer reads; [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates), [EPI-RTE-read-pairing](#epi-rte-read-pairing), [EPI-RTE-reconcile-search](#epi-rte-reconcile-search). Wrapper/Git/CI wiring supplied runtime. |
| Pro deterministic writes and governance installation | `gems/okf-pro/lib/okf/pro/writes.rb`, `gems/okf-pro/lib/okf/pro/scaffold.rb` | Supplied [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes), [RT-RTE-governance-install](runtime.md#rt-rte-governance-install); structural conservation and installation are not semantic acceptance. |
| Attested computation contract and consumer lifecycle | `skills/okf/reference/SPEC.md` | Direct §10 read; [EPI-RTE-run-attestation](#epi-rte-run-attestation), [EPI-RTE-display-gate](#epi-rte-display-gate). Adopter executor, attester, authoritative service and receipts not supplied; no demonstrated attested output. |
| Tests, shipped example corpora, provider internals | boundary Source register | Available package tests/corpora not exhaustively inspected here; no source test counts as a passing run. No exhaustive negative over every example or full system is asserted. Provider parameters/version remain see [RT-CMP-agent](runtime.md#rt-cmp-agent). |

Consequential knowledge/warrant claims are [EPI-CLM-retain-reasoning](#epi-clm-retain-reasoning), [EPI-CLM-drift-build](#epi-clm-drift-build), [EPI-CLM-owner-attestation](#epi-clm-owner-attestation), [EPI-CLM-run-attestation](#epi-clm-run-attestation), and see [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies). Missing host traces prevent claims that instructions or asks were obeyed. Missing source-to-summary comparisons prevent claims that distilled content preserves source warrant. Missing evidence-consuming review decisions prevent identifying accepted ampliative products. Missing run receipts prevent attestation observations. Missing interventions and later-task outcomes prevent causal improvement attribution. These limits do not erase implemented structural checking or metadata-driven behavior.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-concept](#epi-obj-concept) | Project explanations, imported summaries, decisions and durable conclusions | see record | SRC-1, `skills/okf/playbooks/produce.md` | No particular candidate's generation, truth or acceptance follows from its presence. |
| [EPI-OBJ-provenance](#epi-obj-provenance) | Assertions of origin, confirmation, status and expiry | see record | SRC-1, `gems/okf/lib/okf/concept.rb` | Recorded declarations, not authenticated proof of source consultation. |
| [EPI-OBJ-findings](#epi-obj-findings) | Structural predicates and work-state/check results | see record | SRC-1, `gems/okf/lib/okf/bundle/linter.rb` | Their truth domain is parsed structure and configured rules, not project-world correctness. |
| [EPI-OBJ-computation](#epi-obj-computation) | Sanctioned definition and execution/check contract | see record | SRC-1, `skills/okf/reference/SPEC.md` | Runtime receipt/result is a declared external object, not a supplied operated instance. |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Policy guidance; some explanatory principles | see record | SRC-1, `skills/okf/SKILL.md` | Delivery does not establish interpretation or compliance. |
| [RT-OBJ-settings](runtime.md#rt-obj-settings) | None as project knowledge; symbolic operational policy | see record | SRC-1, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json` | Host protocol determines force. |
| [RT-CMP-agent](runtime.md#rt-cmp-agent) | Not determinable from accessible model internals | see record | SRC-1, `skills/okf/SKILL.md` | No accessible weights, pinned version or evidence of parameter updates. |

## Authority-route ledger

Fields owned by a cited declaration are `see` that declaration; this overlay assigns architectural status and content/update relation. Separate rows distinguish checking, disposition and retention even when a supplied container implements several functions.

Route ID: [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: External docs/wiki or manual knowledge enters the authoring context before distillation.
Evaluator/condition and domain: see [RT-RTE-skill-work](runtime.md#rt-rte-skill-work).
Activation and timing: Source choice during produce; see [EPI-OBJ-concept](#epi-obj-concept).
Possible or observed result: Imported source material, with source warrant unknown; no observed import supplied.
Implemented force: Requested authoring procedure, not an enforced source-truth check.
Epistemic authority and scope: Acquisition only; imported content is not produced knowledge.
Operational authority: Material can become the input to an agent-authored concept.
Behavioral-authority path: External agent through source text and the produce playbook, advisory, current authoring task; see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1, `skills/okf/playbooks/produce.md`.
Claim IDs: [EPI-CLM-retain-reasoning](#epi-clm-retain-reasoning).
Mismatch marker: none.
Gap/limit: Imported content is separated from the later semantic transformation below; neither source truth nor preservation by distillation is established.

Route ID: [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Acquired source/task material → authored concept
Evaluator/condition and domain: Agent interpretation; source warrant unknown
Activation and timing: Open task/changed project
Possible or observed result: Distillation or new durable conclusion requested
Implemented force: Advisory skill guidance
Epistemic authority and scope: Candidate only; no semantic preservation or non-entailment established
Operational authority: Agent may edit
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [RT-RTE-skill-work](runtime.md#rt-rte-skill-work).
Evidence source ID and local anchor: SRC-1, `skills/okf/playbooks/produce.md`.
Claim IDs: [EPI-CLM-retain-reasoning](#epi-clm-retain-reasoning).
Mismatch marker: none.
Gap/limit: No candidate pair or review trace.

Route ID: [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: no content change
Transition or check target: Authored files → later readers
Evaluator/condition and domain: Host filesystem edit or library writer
Activation and timing: After edits
Possible or observed result: Durable Markdown available
Implemented force: Readability, not truth approval
Epistemic authority and scope: No added epistemic license
Operational authority: Later task retrieval afforded
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [RT-RTE-skill-work](runtime.md#rt-rte-skill-work).
Evidence source ID and local anchor: SRC-1, `skills/okf/playbooks/maintain.md`.
Claim IDs: [EPI-CLM-retain-reasoning](#epi-clm-retain-reasoning).
Mismatch marker: none.
Gap/limit: Semantic write-back compliance unobserved.

Route ID: [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: no content change
Transition or check target: Claim → source/contradiction judgment
Evaluator/condition and domain: see [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Activation and timing: see [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Possible or observed result: see [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Implemented force: see [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Epistemic authority and scope: see [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Operational authority: see [EPI-RTE-semantic-review](#epi-rte-semantic-review)
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [EPI-RTE-semantic-review](#epi-rte-semantic-review).
Evidence source ID and local anchor: SRC-1, `skills/okf/reference/authoring.md`.
Claim IDs: [EPI-CLM-owner-attestation](#epi-clm-owner-attestation).
Mismatch marker: none.
Gap/limit: see [EPI-RTE-semantic-review](#epi-rte-semantic-review).

Route ID: [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: no content change
Transition or check target: Review/conflict → confirmation, correction or unresolved board line
Evaluator/condition and domain: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Activation and timing: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Possible or observed result: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Implemented force: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Epistemic authority and scope: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Operational authority: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`.
Claim IDs: [EPI-CLM-owner-attestation](#epi-clm-owner-attestation).
Mismatch marker: none.
Gap/limit: see [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition).

Route ID: [EPI-RTE-structural-check](#epi-rte-structural-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-findings](#epi-obj-findings)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Parsed structure → diagnostics
Evaluator/condition and domain: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Activation and timing: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Possible or observed result: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Implemented force: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Epistemic authority and scope: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Operational authority: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [EPI-RTE-structural-check](#epi-rte-structural-check).
Evidence source ID and local anchor: SRC-1, `gems/okf/lib/okf/bundle/linter.rb`.
Claim IDs: [EPI-CLM-drift-build](#epi-clm-drift-build).
Mismatch marker: Semantic drift is not this target.
Gap/limit: see [EPI-RTE-structural-check](#epi-rte-structural-check).

Route ID: [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: no content change
Transition or check target: Materialized tree → valid/refused publication
Evaluator/condition and domain: see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Activation and timing: see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Possible or observed result: see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Implemented force: Enforcing within Writer
Epistemic authority and scope: Structural conformance only
Operational authority: Promotion blocked on validator errors
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle).
Evidence source ID and local anchor: SRC-1, `gems/okf/lib/okf/bundle/writer.rb`.
Claim IDs: [EPI-CLM-drift-build](#epi-clm-drift-build).
Mismatch marker: Not every edit uses Writer.
Gap/limit: No semantic acceptance.

Route ID: [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: no content change
Transition or check target: Validated temporary tree → promoted directory
Evaluator/condition and domain: see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Activation and timing: see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Possible or observed result: see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle)
Implemented force: Filesystem rename
Epistemic authority and scope: No additional truth license
Operational authority: Future loads use promoted files
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle).
Evidence source ID and local anchor: SRC-1, `gems/okf/lib/okf/bundle/writer.rb`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Retention after structural check, not necessarily semantic acceptance.

Route ID: [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-findings](#epi-obj-findings)
Content/update relation: no content change
Transition or check target: Diagnostics → selected host feedback
Evaluator/condition and domain: see [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback)
Activation and timing: see [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback)
Possible or observed result: see [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback)
Implemented force: Advisory; exits zero
Epistemic authority and scope: Structural findings only
Operational authority: Repair requested; cannot undo edit
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback).
Evidence source ID and local anchor: SRC-1, `plugin/hooks/scripts/curate.rb`.
Claim IDs: [EPI-CLM-drift-build](#epi-clm-drift-build).
Mismatch marker: Post-edit feedback is not a gate.
Gap/limit: see [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback).

Route ID: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-provenance](#epi-obj-provenance)
Content/update relation: no content change
Transition or check target: Recognized attestation edit or checked state → ask/block/pass
Evaluator/condition and domain: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Activation and timing: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Possible or observed result: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Implemented force: Conditional host enforcement; distinct Git/CI doors
Epistemic authority and scope: Approval represents owner's review, not machine evidence of reading
Operational authority: May block tool/Stop/commit or prompt owner
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/guards.rb`.
Claim IDs: [EPI-CLM-owner-attestation](#epi-clm-owner-attestation).
Mismatch marker: No universal authentication.
Gap/limit: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates).

Route ID: [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-provenance](#epi-obj-provenance)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Verification mappings → tier label
Evaluator/condition and domain: see [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Activation and timing: see [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Possible or observed result: see [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Implemented force: see [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Epistemic authority and scope: see [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Operational authority: see [EPI-RTE-trust-tier](#epi-rte-trust-tier)
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [EPI-RTE-trust-tier](#epi-rte-trust-tier).
Evidence source ID and local anchor: SRC-1, `gems/okf/lib/okf/concept.rb`.
Claim IDs: [EPI-CLM-owner-attestation](#epi-clm-owner-attestation).
Mismatch marker: Tier denotes declarations, not demonstrated correctness.
Gap/limit: see [EPI-RTE-trust-tier](#epi-rte-trust-tier).

Route ID: [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-provenance](#epi-obj-provenance)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Tier + reference links → owed/stale-read findings
Evaluator/condition and domain: see [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Activation and timing: see [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Possible or observed result: see [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Implemented force: see [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Epistemic authority and scope: see [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Operational authority: see [EPI-RTE-read-pairing](#epi-rte-read-pairing)
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [EPI-RTE-read-pairing](#epi-rte-read-pairing).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/pairing.rb`.
Claim IDs: [EPI-CLM-owner-attestation](#epi-clm-owner-attestation).
Mismatch marker: No source truth test.
Gap/limit: see [EPI-RTE-read-pairing](#epi-rte-read-pairing).

Route ID: [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: no content change
Transition or check target: New Write filename terms → possible collisions + deprecation annotation
Evaluator/condition and domain: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Activation and timing: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Possible or observed result: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Implemented force: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Epistemic authority and scope: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Operational authority: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search)
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/reconcile.rb`.
Claim IDs: none.
Mismatch marker: Search suggestions are not contradiction detection.
Gap/limit: see [EPI-RTE-reconcile-search](#epi-rte-reconcile-search).

Route ID: [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-concept](#epi-obj-concept)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Stored bytes/rows → selected content
Evaluator/condition and domain: see [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve)
Activation and timing: see [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve)
Possible or observed result: see [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve)
Implemented force: Ranking and optional filters; full read by id
Epistemic authority and scope: Source attribution can travel; source truth not checked
Operational authority: External agent receives selected Markdown
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve).
Evidence source ID and local anchor: SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb`.
Claim IDs: [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies).
Mismatch marker: See runtime freshness qualification.
Gap/limit: No default human-review requirement for full read.

Route ID: [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-findings](#epi-obj-findings)
Content/update relation: non-truth-apt policy/content update: work-board placement and closure state
Transition or check target: Requested verb → constrained state mutation
Evaluator/condition and domain: see [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes)
Activation and timing: see [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes)
Possible or observed result: see [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes)
Implemented force: Conservation check and per-file writes
Epistemic authority and scope: No semantic truth license from line conservation
Operational authority: Changes task selection/state read by later agents
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/writes.rb`.
Claim IDs: none.
Mismatch marker: Mechanical closure does not prove completion.
Gap/limit: Count/check propositions are separate from commanded state change.

Route ID: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-findings](#epi-obj-findings)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Board/journal/log → snapshot agreement and record checks
Evaluator/condition and domain: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Activation and timing: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Possible or observed result: see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)
Implemented force: Host/Git/CI conditions differ
Epistemic authority and scope: Agreement with parsed files, not underlying event truth
Operational authority: Can demand snapshot/correction or refuse rewritten past record
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/closing.rb`.
Claim IDs: [EPI-CLM-drift-build](#epi-clm-drift-build).
Mismatch marker: Consistent records can encode false events.
Gap/limit: No authenticating measurement of work.

Route ID: [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-computation](#epi-obj-computation)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Receipt → sanctioned-artifact and displayed-value comparison
Evaluator/condition and domain: see [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Activation and timing: see [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Possible or observed result: see [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Implemented force: see [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Epistemic authority and scope: see [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Operational authority: see [EPI-RTE-run-attestation](#epi-rte-run-attestation)
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [EPI-RTE-run-attestation](#epi-rte-run-attestation).
Evidence source ID and local anchor: SRC-1, `skills/okf/reference/SPEC.md`.
Claim IDs: [EPI-CLM-run-attestation](#epi-clm-run-attestation).
Mismatch marker: No operated attester supplied.
Gap/limit: see [EPI-RTE-run-attestation](#epi-rte-run-attestation).

Route ID: [EPI-RTE-display-gate](#epi-rte-display-gate)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-computation](#epi-obj-computation)
Content/update relation: no content change
Transition or check target: Attestation verdict → display/refuse
Evaluator/condition and domain: see [EPI-RTE-display-gate](#epi-rte-display-gate)
Activation and timing: see [EPI-RTE-display-gate](#epi-rte-display-gate)
Possible or observed result: see [EPI-RTE-display-gate](#epi-rte-display-gate)
Implemented force: see [EPI-RTE-display-gate](#epi-rte-display-gate)
Epistemic authority and scope: see [EPI-RTE-display-gate](#epi-rte-display-gate)
Operational authority: see [EPI-RTE-display-gate](#epi-rte-display-gate)
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [EPI-RTE-display-gate](#epi-rte-display-gate).
Evidence source ID and local anchor: SRC-1, `skills/okf/reference/SPEC.md`.
Claim IDs: [EPI-CLM-run-attestation](#epi-clm-run-attestation).
Mismatch marker: Consumer responsibility, not MCP enforcement.
Gap/limit: see [EPI-RTE-display-gate](#epi-rte-display-gate).

Route ID: [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: [RT-OBJ-skill](runtime.md#rt-obj-skill)
Content/update relation: non-truth-apt policy/content update: reorganized retrieval or instruction arrangement
Transition or check target: Misfit evidence → proposal → approved restructuring
Evaluator/condition and domain: see [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal)
Activation and timing: see [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal)
Possible or observed result: see [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal)
Implemented force: Requested approval separation
Epistemic authority and scope: No improved factual warrant from smaller files
Operational authority: Later retrieval/instruction use can change
Behavioral-authority path: [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); route-specific consumer/channel/force/horizon see [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal).
Evidence source ID and local anchor: SRC-1, `skills/okf/playbooks/refine.md`.
Claim IDs: none.
Mismatch marker: Refine and principles have different approval policies.
Gap/limit: Independent theory/learning limits see supplied record.

Route ID: [RT-RTE-governance-install](runtime.md#rt-rte-governance-install)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-settings](runtime.md#rt-obj-settings)
Content/update relation: non-truth-apt policy/content update: installed governance templates
Transition or check target: Package templates → adopted instructions/hooks
Evaluator/condition and domain: see [RT-RTE-governance-install](runtime.md#rt-rte-governance-install)
Activation and timing: see [RT-RTE-governance-install](runtime.md#rt-rte-governance-install)
Possible or observed result: see [RT-RTE-governance-install](runtime.md#rt-rte-governance-install)
Implemented force: Per-file installation policy
Epistemic authority and scope: No semantic endorsement of adopter claims
Operational authority: Installed machinery can shape later behavior
Behavioral-authority path: [RT-BAP-hook-protocol](runtime.md#rt-bap-hook-protocol); route-specific consumer/channel/force/horizon see [RT-RTE-governance-install](runtime.md#rt-rte-governance-install).
Evidence source ID and local anchor: SRC-1, `gems/okf-pro/lib/okf/pro/scaffold.rb`.
Claim IDs: none.
Mismatch marker: Installation is not exercised improvement.
Gap/limit: No trace-responsive automatic policy revision established.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-retain-reasoning](#epi-clm-retain-reasoning) | see record | SRC-1, `README.md`; doctrine/design | see claim and [RT-RTE-skill-work](runtime.md#rt-rte-skill-work) | [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle), [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) | None supplied | No later-task comparison; file retention is not retention of inaccessible internal reasoning | A durable, readable place for agent-authored explanations | Correctness and keeping current depend on semantic work and actual write-back |
| [EPI-CLM-drift-build](#epi-clm-drift-build) | see record | SRC-1, `README.md`; doctrine/design | see [EPI-RTE-structural-check](#epi-rte-structural-check) | [EPI-RTE-structural-check](#epi-rte-structural-check), [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates) | None supplied | Configured thresholds/doors determine force; no effectiveness experiment | Structural problems can fail chosen gates | Semantic drift is not automatically detected; declared expiry is info, age cutoff is optional |
| [EPI-CLM-owner-attestation](#epi-clm-owner-attestation) | see record | SRC-1, `gems/okf-pro/lib/okf/pro/guards.rb`; doctrine/design with implementation | see [EPI-RTE-semantic-review](#epi-rte-semantic-review) | [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates), [EPI-RTE-trust-tier](#epi-rte-trust-tier), [EPI-RTE-read-pairing](#epi-rte-read-pairing) | None supplied | No evidence that approver read sources or that every path asked | Recognized added attestation text can trigger explicit owner permission; tier affects attention obligations | Review declaration and permission are not a semantic truth oracle or authenticated history |
| [EPI-CLM-run-attestation](#epi-clm-run-attestation) | see record | SRC-1, `skills/okf/reference/SPEC.md`; doctrine/design | see [EPI-RTE-run-attestation](#epi-rte-run-attestation), [EPI-RTE-display-gate](#epi-rte-display-gate) | Contract accessors/checks: [EPI-RTE-structural-check](#epi-rte-structural-check); no attester execution in inspected dispatch | None supplied | Depends on particular executor, independent binding, receipt and authoritative reread | A bounded consumer-side computation-fidelity protocol is specified | Not implemented or observed as an end-to-end gate on the inspected CLI/MCP surfaces |
| [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies) | see record | SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb`; doctrine/design | see record | [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) | None supplied | No stale-run observation; implementation countercases suffice to limit guarantee | Live body reads preserve original file bytes at resolved ids | Fresh bytes do not imply fresh selection metadata or endorsed content |

## Bounded conclusion

**OKF separates semantic responsibility from mechanical checking.** It can retain prose and provenance declarations and deliver them to later agents. The source-to-concept route includes acquisition of external material with unknown source warrant; its subsequent agent distillation is semantically indeterminate without paired inputs/outputs. Code-derived explanations and cross-cutting conclusions are requested, but no individual novel proposition, its non-entailment, or evidence-consuming acceptance is established here. An available concept is not proof that a particular production or review route operated. See [RT-RTE-skill-work](runtime.md#rt-rte-skill-work), [EPI-OBJ-concept](#epi-obj-concept), [EPI-RTE-semantic-review](#epi-rte-semantic-review).

**Mechanical deductions are real but narrowly licensed.** Trust tier follows verification mappings; keyed-footnote checks follow label membership; expiry follows dates; snapshot checks follow the parsed work state. These support propositions in those formal domains, conditional on parser/encoding fidelity and input declarations. They do not certify what a service does, whether a cited document supports a summary, whether work really occurred, or whether a computation's definition matches policy. The concrete tier/footnote deductions in [EPI-RTE-trust-tier](#epi-rte-trust-tier) and [EPI-RTE-structural-check](#epi-rte-structural-check) use inspected code, not target execution.

**Authority differs by consumer.** Structural conformance can veto Writer publication. Base curation supplies advisory evidence after edits. Pro can request owner permission before recognized attestation edits and conditionally block subsequent host/commit/CI phases. Human-reviewed metadata changes which briefings still owe a board line; explicit trust/status filters change retrieval membership. Full concept reads do not demand that a concept be human-reviewed. No review authenticity or general filesystem exclusion follows. See [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle), [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback), [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates), [EPI-RTE-read-pairing](#epi-rte-read-pairing), [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve).

**Semantic disposition is prescribed, not evidenced as an operated acceptance chain.** Review is against sources and consistency; intended use is reliable later bundle consultation within the concept's own scope. The Pro profile reserves human confirmation to an owner who actually reads. A collision is to be corrected/deprecated now or retained as an unresolved linked board obligation. Those are meaningful requested changes of reliance, not automated resolution. Neither a verification entry nor structural acceptance alone records the proposition, consumed evidence, criterion and intended scope needed to establish an accepted ampliative claim. Linking/indexing and retention are performed before or independently of that acceptance; no distinct acceptance-conditioned lifecycle-integration route is established in the assessed procedures. See [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition), [EPI-RTE-reconcile-search](#epi-rte-reconcile-search).

**Run attestation has a different target.** Its specified criterion is equality of the executed artifact to the sanctioned binding and displayed value to authoritative receipt data. Intended use is displaying that run's result, within the named computation/runtime/parameters. A consumer-side gate is requested for that call, not retrospective proof of the definition's truth. Its attester and gate remain doctrine only here; contract-shape linting is not their execution. See [EPI-RTE-run-attestation](#epi-rte-run-attestation), [EPI-RTE-display-gate](#epi-rte-display-gate).

**Direct policy change remains independent of knowledge warrant.** Pro writers alter task state under construction constraints; installation changes instruction/hook files; refinement requests retrieval/instruction restructuring using before/after evidence. These pathways can influence future action without producing an accepted truth-apt claim. Localized principles, requested consumption, criticism/iteration limits and independent learning, reflection, autonomy and self-improvement assessments are see [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal). No improved later-task capacity, causal benefit, exercised self-improvement or provider-parameter update is established by this evidence. The missing model internals do not negate the implemented file-based authority paths. Uninspected migrations, UI details, examples and external attesters also prevent a system-complete negative about all possible epistemic routes.

## Shared records

### Operative objects

#### EPI-OBJ-concept
Label: Bundle concept prose

Natural-language descriptions, explanations, summaries, decisions and findings in Markdown bodies, stored on disk and parsed into Ruby Concept instances; later consumers are agents/humans through direct files or retrieval surfaces. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill): project knowledge is the product, not the procedure telling an agent how to author it. No supplied operative-object counterpart names these bodies. SRC-1, `skills/okf/playbooks/produce.md`, `skills/okf/reference/authoring.md`.

> Pick the source(s): **code** (derive concepts from source, READMEs, docstrings,
>    config), **docs/wiki** (distill pages into concepts; record the originals in
>    `sources:` and key claims with `[^id]` footnotes), **manual** (decisions,
>    playbooks, metrics that live only in people's heads).
> --- `skills/okf/playbooks/produce.md`

External content is acquired, not newly discovered merely because summarized. The instruction to capture explanations beyond one file makes useful synthesis a goal, but does not establish which actual output is entailed or ampliative.

> Capture what you **cannot** derive by
> reading one source file: the *why* behind a design, cross-cutting relationships,
> decisions and their tradeoffs, operational tribal knowledge, the metric that
> actually matters.
> --- `skills/okf/reference/authoring.md`

#### EPI-OBJ-provenance
Label: Concept provenance and lifecycle fields

Symbolic YAML mappings/lists/scalars in concept frontmatter: generated, verified, sources, status and stale_after. Stored beside concept prose; Ruby computes trust and status for downstream consumers. This is a distinct operative part of [EPI-OBJ-concept](#epi-obj-concept), split because its checks and fixed consumers differ from prose interpretation. No supplied runtime object names this metadata; [RT-OBJ-settings](runtime.md#rt-obj-settings) instead names hook machinery. SRC-1, `gems/okf/lib/okf/concept.rb`; doctrine in `skills/okf/reference/authoring.md`.

> `generated` records how the current content was produced (`by` REQUIRED within;
> `at` an ISO 8601 datetime); `verified` lists who confirmed it against its
> sources — they stay separate because who *wrote* a concept need not be who
> *checked* it.
> --- `skills/okf/reference/authoring.md`

The prose fields embedded in source metadata remain declarations interpreted by readers, not a formal proof of support. Status absent defaults to stable; stable is not evidence of a verification event.

> text = declared_status.nil? ? "" : declared_status.to_s.strip
>       text.empty? ? DEFAULT_STATUS : text
> --- `gems/okf/lib/okf/concept.rb`

#### EPI-OBJ-findings
Label: Structural and operational findings

Symbolic Ruby result structures rendered as JSON/text: validation errors/warnings, lint warnings/infos, trust counts, pairing obligations and computed work-state evidence. These are ephemeral returns unless an agent writes them into the log; snapshot text can persist and be rechecked. They describe parsed files under fixed rules, not semantic correctness. No supplied runtime operative object names these results; they are outputs used by [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates) and [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback). SRC-1, `gems/okf/lib/okf/bundle/linter.rb`.

> structured data (OKF::Bundle::Linter::Report) for a human or agent to act on. Contradictions
>    # and semantic staleness are NOT detected here — they need meaning, not structure;
>    # the JSON report is the substrate an agent consumes for those passes.
> --- `gems/okf/lib/okf/bundle/linter.rb`

#### EPI-OBJ-computation
Label: Attested Computation contract

Symbolic frontmatter type/runtime/parameter declarations and executor/attester pointers, plus an inline symbolic computation or file reference, retained as Markdown/YAML and referenced assets. Natural-language explanation of the definition is concept prose, see [EPI-OBJ-concept](#epi-obj-concept); this record owns the contract consumed under fixed binding/check rules. Actual executable semantics and any numerical model inside a pointed asset are not determined by the format alone. No supplied runtime object declares this contract; it is distinct from generic skill guidance.

SRC-1, `skills/okf/reference/SPEC.md`:

> OKF records the computation
> and the means to check it; it does not execute anything itself.
> --- `skills/okf/reference/SPEC.md`

> - `attester`: The deterministic check. `resource` names code (no LLM) that
>   takes a receipt and returns a verdict. It is meant to run consumer-side.
> --- `skills/okf/reference/SPEC.md`

Runtime artifacts are not the retained contract:

> This subsection is informative, not normative. The runtime artifacts below
> are **not** stored in the bundle.
> --- `skills/okf/reference/SPEC.md`

### Routes

#### EPI-RTE-structural-check
Label: Validator and lint evidence

Distinct check/evidence-production referent shared across the supplied consumer containers [RT-RTE-publish-bundle](runtime.md#rt-rte-publish-bundle), [RT-RTE-curation-feedback](runtime.md#rt-rte-curation-feedback) and [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates). Those records own admission/feedback; this record owns the predicates, not another publication or gate.

Parsed bundle → Validator/Linter result, owned by deterministic Ruby analyzers. Target/domain: conformance grammar, existence/attribution joins, declared expiry and selected curation predicates over the parsed tree. Criterion is the named predicate, not agreement between a summary and external facts. Output errors/warnings/infos are separate from consumers deciding to reject. No semantic answer oracle is supplied. Callers configure check sets, clocks and thresholds; humans supply/adopt content and configuration, software evaluates.

- Immediate return: Result object, optionally rendered JSON/text findings.
- Later read-back: A snapshot written into log.md can be checked later, but these pure analyzers do not retain their returned reports themselves.
- Delegated visibility: uninspected — host sharing of tool/check results is external.
- Selection predicate: Selected checks; Validator visits parsed concepts/reserved/unparseable entries; keyed attribution activates only if sources have ids.
- Invalidation or expiry: Each call recomputes over its supplied bundle snapshot. Expired needs today; stale needs an age cutoff. Pro explicitly excludes stale while supplying today.
- Activation or effect: Wired evidence generation; Writer consumes validity, base hook returns selected findings, Pro gates consume structural results. No semantic truth license.
- Evidence limits: No target execution. Parser/input fidelity and check coverage bound deductions; URL truth and semantic entailment are not these predicates.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf/lib/okf/bundle/validator.rb`, `gems/okf/lib/okf/bundle/linter.rb`, `gems/okf-pro/lib/okf/pro/conformance.rb`, `gems/okf-pro/lib/okf/pro/audit.rb`.

> @result.add_error(concept.path, "frontmatter must include a non-empty type") if OKF.blank?(concept.type)
> --- `gems/okf/lib/okf/bundle/validator.rb`

> ids = source_ids(concept).map(&:downcase)
>           next if ids.empty?
> --- `gems/okf/lib/okf/bundle/linter.rb`

> next if ids.include?(label.downcase)
> --- `gems/okf/lib/okf/bundle/linter.rb`

> next if defined.include?(label.downcase)
> --- `gems/okf/lib/okf/bundle/linter.rb`

> report = ::OKF::Bundle::Linter.call(bundle, today: Date.today, except: [ :stale ])
> --- `gems/okf-pro/lib/okf/pro/conformance.rb`

Concrete input deduction, not execution: a concept with source id `s`, body marker `[^s]`, and no separate footnote definition passes this membership check even if its sentence misquotes the source. A marker `[^x]` with the same sole source id and no definition yields an unattributed-claim warning. Removing all source ids skips the check. Thus “attributed” here licenses a keyed join, not evidence support. Expired is info; selected stale is warn, see the severity map in `gems/okf/lib/okf/bundle/linter.rb`. Pro audit returns findings for validator warnings as well as errors; per-edit Conformance instead distinguishes soft warnings and defers set-scoped checks. Passing one door does not entail passing all doors.

#### EPI-RTE-trust-tier
Label: Verification mappings to trust tier

No counterpart after comparison with supplied records: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates) controls attempted edits, whereas this route classifies already parsed declarations and feeds multiple consumers.

Concept.verified → trust_tier → wire tier, owned by Concept Ruby code. Target/domain: the shapes and actor-prefix membership of recorded verification events, not the body proposition. A mapping becomes a one-element list; non-mapping entries drop. No entries means unverified; any trimmed human: prefix means human-reviewed; other mappings mean machine-confirmed. This is an entailed classification under the code's interpretation of metadata, not newly warranted project knowledge.

- Immediate return: Tier symbol and hyphenated string.
- Later read-back: Stored verification mappings are reclassified on later concept loads; derived tier need not itself be stored.
- Delegated visibility: inapplicable — pure local classification, no delegation.
- Selection predicate: All accepted verification mappings; any human: verifier takes precedence.
- Invalidation or expiry: Neither date freshness nor body/source equality participates in this tier predicate. Reload can change the result if metadata changes.
- Activation or effect: Trust can filter catalog/search; Pro attention pairing treats human-reviewed as read discharged. These consumers confer selection/attention consequences, not demonstrated truth.
- Evidence limits: No authentication of by, no independent evidence of reading, no model evaluator; tier computation alone cannot license claim truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf/lib/okf/concept.rb`, `gems/okf/lib/okf/bundle/row_filter.rb`, `gems/okf-mcp/lib/okf/mcp/server.rb`.

> raw = frontmatter["verified"]
>       entries = raw.is_a?(Hash) ? [ raw ] : Array(raw)
>       entries.grep(Hash).map { |entry| Markdown::Frontmatter.stringify_keys(entry) }
> --- `gems/okf/lib/okf/concept.rb`

> events = verified
>       return :unverified if events.empty?
> --- `gems/okf/lib/okf/concept.rb`

> return :human_reviewed if events.any? { |event| event["by"].to_s.strip.start_with?(HUMAN_ACTOR) }
>
>       :machine_confirmed
> --- `gems/okf/lib/okf/concept.rb`

> (trust.nil? || fold(row[:trust]) == Concept.fold_tier(trust))
> --- `gems/okf/lib/okf/bundle/row_filter.rb`

Concrete deterministic trace: `verified: {by: process:nightly}` normalizes to one mapping and yields machine-confirmed; substituting `human:owner` yields human-reviewed. Leaving that mapping unchanged while changing the body leaves the tier predicate unchanged. An empty mapping also survives shape filtering and yields machine-confirmed, though Validator warns about missing by; a scalar human actor yields no verification mappings, hence unverified. These are deductions from implementation, not executed fixtures or allegations about an actual host event. No timestamp/body binding is checked by this classifier. Full read_concept accepts bundle/id and reads text without a trust precondition; trust filtering is opt-in on search/catalog, not universal admission.

#### EPI-RTE-read-pairing
Label: Human review to attention obligation

Part of: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)

This is its trust-sensitive pairing/checking part, split from edit permission and unrelated snapshot/budget checks; it owns no replacement of that container.

Concept tier plus board targets → Pairing failures and Attestation rows → Stop/audit or owner-visible inventory, owned by Ruby Pairing and its consumers. Target/domain: whether generated reference briefings still have a read-owed line and whether already human-reviewed references retain obsolete To-read lines. For owner-read semantics, computation uses declarations; the owner is the intended semantic reviewer. No semantic answer oracle. Missing required links and stale read lines can become blocking findings in configured consumers, not proof that source reading occurred.

- Immediate return: Pairing findings; unverified listing gives id, producer, date and tier.
- Later read-back: Later inventory/Stop/audit reads the same persisted fields and board links; later sessions can see updated attention state.
- Delegated visibility: uninspected — host/worker propagation not specified.
- Selection predicate: Read owed if declared_generated? and not human-reviewed; briefing-specific board pairing scopes to reference/ ids. Attestation inventory is corpus-wide.
- Invalidation or expiry: Recomputed when state is read; human-reviewed field declaration changes obligation. No expiry date reverses this predicate.
- Activation or effect: Stop includes pairing failures; audit includes pairing; unverified listing is informational. Force is conditional host refusal/commit-CI failure for findings and advisory owner attention for listing, across later project operation.
- Evidence limits: Software can veto inconsistent board pairing, not false human authorship or source truth. Process verification deliberately does not discharge human read.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf-pro/lib/okf/pro/pairing.rb`, `gems/okf-pro/lib/okf/pro/attestation.rb`, `gems/okf-pro/lib/okf/pro/closing.rb`, `gems/okf-pro/lib/okf/pro/audit.rb`.

> def awaiting_read?(concept)
>         concept.declared_generated? && concept.trust_tier != :human_reviewed
>       end
> --- `gems/okf-pro/lib/okf/pro/pairing.rb`

> def owner_read?(concept)
>         concept.trust_tier == :human_reviewed
>       end
> --- `gems/okf-pro/lib/okf/pro/pairing.rb`

> next unless awaiting_read?(concept)
> --- `gems/okf-pro/lib/okf/pro/pairing.rb`

> next unless owner_read?(concept)
> --- `gems/okf-pro/lib/okf/pro/pairing.rb`

> msgs.concat(Pairing.failures(root, board: board, concepts: concepts))
> --- `gems/okf-pro/lib/okf/pro/closing.rb`

Countercase to “any verification discharges reading”: process:nightly remains machine-confirmed and therefore owed. Human-reviewed does not automatically delete the line; a stale-read finding asks the actor to remove it. Admission/recovery: software rejects unresolved pairing at configured doors; agent/owner corrects the board or metadata and reruns, not automatic rollback.

#### EPI-RTE-reconcile-search
Label: Filename collision feedback

Part of: [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates)

Distinct post-edit selection/feedback part: it offers possible semantic collisions, not verification-edit admission.

Write event → target filename terms → bundle search hits → deprecation annotation and instruction to compare, owned by Reconcile Ruby code then interpreted by agent. Decider of actual contradiction, duplicate or supersession is the agent/owner under Pro Rule 1. Search is no semantic oracle. It selects already retained claims; it neither generates a new truth-apt proposition about their disagreement nor settles one.

- Immediate return: Possible collision blocks containing id, type, title, snippet and settled-status annotation.
- Later read-back: Existing concept bodies/status are searched again on later writes; this check itself writes no reconciliation result.
- Delegated visibility: uninspected — post-edit host context propagation external.
- Selection predicate: Write only, excluding journal and structural filenames; first four non-stopword filename terms, at most five matching concepts per term; own id excluded.
- Invalidation or expiry: Current parsed targets/status supply annotations; deprecated hits remain visible rather than being erased.
- Activation or effect: CLI post-edit consumes messages and emits refusal-style feedback after mutation, conditional on host protocol. Consumer agent is told to read/settle or file a board conflict; no pre-write veto or semantic resolution is implemented by this search.
- Evidence limits: Vocabulary bounds recall; snippets omit bodies. Post-edit demand is not evidence of actual body reading, accepted supersession or rollback.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf-pro/lib/okf/pro/reconcile.rb`, `gems/okf-pro/lib/okf/pro/cli.rb`.

> return [] unless event.tool_name == "Write"
> --- `gems/okf-pro/lib/okf/pro/reconcile.rb`

> File.basename(target.rel, ".md").split("-")
>             .reject { |t| t.empty? || STOP_WORDS.include?(t.downcase) }
>             .first(4)
> --- `gems/okf-pro/lib/okf/pro/reconcile.rb`

> status == "deprecated" ? "  [deprecated — this collision was already settled]" : ""
> --- `gems/okf-pro/lib/okf/pro/reconcile.rb`

> Conformance.check(target, scope: :edit) + Budget.cap_check(target) + Reconcile.search(target, event)
> --- `gems/okf-pro/lib/okf/pro/cli.rb`

Trigger and veto: code may return no hits; the semantic proposal/decision is left to the reader. If unresolved, requested persistent result is a linked conflict line. Correction/deprecation is manual, not an automatic search-result rewrite.

#### EPI-RTE-semantic-review
Label: Source and contradiction review

Part of: [RT-RTE-skill-work](runtime.md#rt-rte-skill-work)

The generic semantic checking part of the supplied skill workflow, supplemented by Pro's explicit owner-review policy. Pro's human confirmation is a stricter policy than ordinary maintain; no universal human approval is inferred.

Concept/source material → requested judgment whether meaning remains true and claims match sources, owned by external agent for maintenance and by the owner for Pro human verification. Target/domain: the concept's propositions within their source/project scope. Criterion is confirmation against sources plus semantic consistency/current relevance; intended use is later project consultation. Neither an evidence packet nor an actual acceptance decision naming a specific claim/scope is supplied. No expected-answer oracle is provided; source references are evidence inputs, not guaranteed correct reference answers.

- Immediate return: Requested judgments, proposed repairs and owner confirmation; no observed review output.
- Later read-back: Review can result in durable corrections or verified mappings; judgment not separately retained unless the actor writes it.
- Delegated visibility: uninspected — external host reasoning and delegation are not specified.
- Selection predicate: Project changes/affected assets, observed disagreement, loose-file/tag judgment, or owner choosing material to read.
- Invalidation or expiry: Maintenance reruns on changed reality; declared date/age hints do not decide semantic staleness.
- Activation or effect: Advisory procedural guidance through installed Markdown; current and later sessions may follow it. Implementation supplies evidence access and targeted approval asks, not semantic compliance.
- Evidence limits: Doctrine/design only for review itself. No demonstrated source comparison, evidence-consuming acceptance, reliable model criticism or actual owner reading.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1, `skills/okf/playbooks/maintain.md`, `skills/okf/reference/authoring.md`, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/frontmatter.md`; generic judgment evidence is also supplied in [RT-CMP-agent](runtime.md#rt-cmp-agent) and the boundary.

> Reach for this when the project changed and the bundle's *content* must catch
> up.
> --- `skills/okf/playbooks/maintain.md`

> `verified:` (a list) | **The owner's decision** — the agent may hold the pen | Only after actually reading | Who confirmed this, and when.
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/guides/frontmatter.md`

Proposer/decider/veto: the agent proposes content and maintenance; owner can deny matched attestation asks, but general unverified concept edits do not require human per-content approval. Review guidance does not prove the reviewed content is true. Rejection/recovery is to leave unverified, revise, or escalate a conflict, not to fabricate provenance.

#### EPI-RTE-semantic-disposition
Label: Correct, deprecate or retain a conflict

Distinct from the checking part [EPI-RTE-semantic-review](#epi-rte-semantic-review) and from mechanical [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates). It spans maintenance and Pro reconciliation rather than being part of exactly one supplied route: it owns the requested semantic disposition, not event detection, persistence mechanics or actual human permission.

Source/contradiction judgment → requested confirmation/correction, supersession or unresolved work. Agent/owner judges propositions; owner decides Pro human confirmation. Intended use is a current, navigable project corpus. Criterion is agreement with sources/current reality and resolved contradiction, but no run provides a particular decision with consumed evidence and intended scope. Ordinary filing can precede checking. No formal semantic oracle or universal human acceptance gate is established.

- Immediate return: Requested corrected/deprecated concept or linked board conflict; recorded verification if confirmation occurs.
- Later read-back: Corrected bodies, deprecation markers and conflict lines are later searchable; code annotates deprecated collisions, while humans/agents interpret superseded reasoning.
- Delegated visibility: uninspected — external sharing of review and acceptance decisions not specified.
- Selection predicate: Changed or colliding claims; unresolved conflicts remain work rather than forcibly selecting a winner.
- Invalidation or expiry: Subsequent source/project change or conflict may reopen reliance; code does not authenticate whether a verification remains applicable to revised prose.
- Activation or effect: Policy guidance to author/correct now and preserve conflict. Operational effect through subsequent retrieval and board attention, not enforced semantic agreement.
- Evidence limits: No observed semantic acceptance or post-acceptance integration. Linking/index updates alone remain retention/organization, not evidence of acceptance.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1, `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`, `skills/okf/playbooks/maintain.md`.

> It supersedes
> something: correct the loser **now** — title and `description:` first,
> `status: deprecated` on its frontmatter, superseded reasoning into
> `<details>` — because ingestion is the only moment both claims are in
> front of someone and the cost of noticing is at its minimum.
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`

> Or the conflict cannot be settled on the spot: **file it, do not resolve
> it** — one dated line on the board, both sides linked:
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/skills/okf-pro/SKILL.md`

> mark retired assets with a `**Deprecation**` note rather than
>    silently deleting the context that explains them.
> --- `skills/okf/playbooks/maintain.md`

Admission/rejection/recovery: actor can withhold confirmation, correct a loser, or defer resolution with an explicit conflict obligation. No executable semantic rollback or compulsory evidence ledger is shown. Human/agent execution and actual later changed reliance remain unobserved.

#### EPI-RTE-run-attestation
Label: Receipt fidelity checking

No counterpart after comparison with [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) and [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates). Those supply content/structure or owner-permission checks, not §10's per-call execution comparison. This is also separate from definition-level verified events.

Sanctioned contract + parameters + executor receipt → independent attester verdict. Owner is the consumer's deterministic attester; external agent supplies only parameter values. Check target/domain is the particular executed artifact and displayed value, relative to the sanctioned binding and authoritative execution result. Criterion is equality/fidelity, not whether the sanctioned definition captures the right real-world concept. Intended use is this call's displayed value. The authoritative outcome is meant to be reread by job id; no actual oracle implementation/provider is supplied here.

- Immediate return: Specified per-call verdict and supporting job/log evidence.
- Later read-back: inapplicable — SPEC says runtime artifacts are not stored in the bundle; no retained receipt-to-later-call route supplied.
- Delegated visibility: uninspected — executor/attester packaging and remote visibility are adopter-specific.
- Selection predicate: Discover Attested Computation, load one computation, bind declared parameters only, execute, then attest.
- Invalidation or expiry: Per-run check; definition verification/expiry is separate and does not replace it.
- Activation or effect: Verdict intended for a consumer-side display gate, see [EPI-RTE-display-gate](#epi-rte-display-gate). No inspected registered CLI/MCP attester executor establishes enforcing force.
- Evidence limits: Doctrine only. Missing executor, authoritative service, attester implementation and trace prevent implementation, observed-run or causal conclusions for a concrete computation.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1, `skills/okf/reference/SPEC.md`, especially §10.3–10.6. Fourteen tool registration names in `gems/okf-mcp/lib/okf/mcp/server.rb` and built-in requires in `gems/okf/lib/okf/cli.rb` were checked; references inventory/lint are not execution.

> the attester independently re-derives that same binding to compare against
> what actually ran.
> --- `skills/okf/reference/SPEC.md`

> confirms provenance (the computation that ran equals `computation` bound
>    with the claimed parameters, not agent-authored SQL) and fidelity (the
>    displayed value matches the receipt's authoritative source, re-read by
>    job id rather than taken from the agent's text).
> --- `skills/okf/reference/SPEC.md`

> A concept with a stale definition can still attest cleanly, and a
> freshly-verified definition still requires attestation on each run, which
> is why both are needed.
> --- `skills/okf/reference/SPEC.md`

Countercase limits scope: even a correct equality verdict licenses only artifact/value fidelity under the receipt/source contract. It does not warrant revenue-policy correctness, omitted premises, data truth or transfer to another runtime.

#### EPI-RTE-display-gate
Label: Consumer verdict disposition

Distinct from [EPI-RTE-run-attestation](#epi-rte-run-attestation): that route evaluates evidence; this one consumes its verdict to decide whether to display. No supplied runtime gate has this target.

Attester verdict + declared expiry → consumer display/refusal/warning. Consumer owns disposition; agent proposes parameters, not a replacement computation. Criterion for intended display use is a passing per-call attestation; expired definitions are to warn or refuse according to consumer policy. Software is intended to veto a failed attestation; no human decision is prescribed per call. No new oracle: it consumes the preceding check's verdict.

- Immediate return: Specified refusal, warning, or displayed value with visible verdict evidence.
- Later read-back: inapplicable — no retained runtime artifact is specified; this disposition is per call.
- Delegated visibility: uninspected — consumer packaging/protocol is outside supplied implementation.
- Selection predicate: Each checked Attested Computation call; failing verdict must not be displayed under the informative procedure.
- Invalidation or expiry: today >= stale_after requests warning/refusal; definition freshness is separate from successful per-run attestation.
- Activation or effect: Doctrine requests enforcing refusal of failing display, for this result/call, with visible success evidence. No end-to-end gate is implemented in the inspected registered retrieval/checking surfaces.
- Evidence limits: No observed refusal/display, concrete consumer or rejection recovery protocol. Refusing a display is not automatic rollback of execution or removal of retained definition.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1, `skills/okf/reference/SPEC.md`.

> 6. **Gate**: refuse to display a failing attestation; warn or refuse when
>    `today >= stale_after`. On success, surface the verdict (for example a
>    link to the job log) so trust is visible.
> --- `skills/okf/reference/SPEC.md`

Admission/recovery: passing verdict is the specified operational admission to display; failed check is not to be repaired by an agent silently changing the sanctioned computation. Authoring policy says to tell a human when the computation is wrong. No executable rollback or evidence of a corrected retry was inspected.

### Claims

#### EPI-CLM-retain-reasoning
Label: Reasoning retained between sessions

No counterpart after comparison with [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies): this is the broader durable-project-explanation claim, not live-read freshness. SRC-1, `README.md`, doctrine/design.

> **okf gives that reasoning somewhere to live.** Plain Markdown files in your
> repo, next to the code they explain, written and kept current by the agent
> itself rather than by you.
> --- `README.md`

[RT-RTE-skill-work](runtime.md#rt-rte-skill-work) and [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) provide instruction and access paths. Neither establishes that every internal reasoning step was written, that authored explanations are true, or that later tasks improved.

#### EPI-CLM-drift-build
Label: Drift as failing build

Distinct from [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies): CI-visible drift rather than file freshness. SRC-1, `README.md`, doctrine/design.

> - **Drift is a failing build.** `okf validate` and `okf lint` return exit codes,
>   so a stale or malformed bundle breaks CI the same way a broken test does.
> --- `README.md`

Supported for selected structural findings with configured failure thresholds and invoked CI. [EPI-RTE-structural-check](#epi-rte-structural-check) limits stale to cutoff comparisons and explicitly separates semantic staleness; Pro excludes the age check and reports expiry as info. No universal semantic-drift guarantee follows.

#### EPI-CLM-owner-attestation
Label: Owner approval means review

Distinct from [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies); closest supplied route is [RT-RTE-pro-gates](runtime.md#rt-rte-pro-gates), whose ask/host limits remain unchanged. SRC-1, `gems/okf-pro/lib/okf/pro/guards.rb`: doctrine/design embodied in the ask message.

> "your approval is the attestation. Approve ONLY if you have actually reviewed " \
>                    "this content yourself. If you have not, deny — unverified is the truth."
> --- `gems/okf-pro/lib/okf/pro/guards.rb`

Approval has intended semantic significance, but the code requests honesty rather than measuring source reading. [EPI-RTE-trust-tier](#epi-rte-trust-tier) and [EPI-RTE-read-pairing](#epi-rte-read-pairing) show why the declaration matters downstream. A scalar verified value is a countercase to approval alone producing a human-reviewed tier; an unchanged valid human mapping after a body edit is a countercase to tier alone proving current review.

#### EPI-CLM-run-attestation
Label: Sanctioned computation fidelity

No supplied claim counterpart: unlike [RT-CLM-live-bodies](runtime.md#rt-clm-live-bodies), this is provenance/fidelity of a computed value. SRC-1, `skills/okf/reference/SPEC.md`, doctrine/design.

> An Attested Computation concept carries not just what a value *means* but a
> sanctioned way to *compute* it, so a consumer can confirm the agent ran the
> blessed computation instead of improvising its own.
> --- `skills/okf/reference/SPEC.md`

The specified comparison and gate are [EPI-RTE-run-attestation](#epi-rte-run-attestation) and [EPI-RTE-display-gate](#epi-rte-display-gate). The format explicitly does not execute computations itself; present contract accessors and lint checks establish neither a run nor a successful verdict.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
