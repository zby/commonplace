---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "claude-obsidian workflow: bounded delegated source ingestion, parent merge, reviewed transaction and recovery at the frozen commit."
run-id: AAS-2026-10-13-claude-obsidian-c5e56e25c8bb-01
reviewed-boundary: "32ac5a02c4e082e4a5628ca810776375e134708e"
---

# claude-obsidian workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects a bounded batch Ingest with one already-captured local source per delegated worker. It is representative because the shipped ingest skill connects source assessment, bounded delegation, evidence proposals, shared navigation and provenance changes, and one parent-owned transaction. Delegation is an available branch, not mandatory for every ingestion. This is a source-supported procedure with an executable persistence endpoint, not an observed successful run. No host transcript, actual worker packet, user review or recovered operation was supplied. The host owns worker scheduling and actual isolation, as [the boundary](boundary.md#boundary-and-evidence) establishes. SRC-1: `skills/wiki-ingest/SKILL.md`, `agents/wiki-ingest.md`.

The principal route already has identity in [RT-RTE-ingest-drafts](runtime.md#rt-rte-ingest-drafts). Its persistence endpoint shares the transaction mechanism of [RT-RTE-save-apply](runtime.md#rt-rte-save-apply); that citation does not relabel an Ingest operation as Save. The workflow fields below annotate those referents rather than declare duplicate routes.

### Request, capture readiness and delegation

The user supplies sources and intended scope. The foreground orchestrator resolves the installed product separately from the selected user vault. It agrees a budget for source count, bytes/pages, existing-page reads, generated pages and network requests. A large request starts with a bounded tranche. For this selected branch, sources are already local and in scope; workers do not fetch or capture them. A source outside the vault must first enter the skill's reviewed capture procedure, while URL capture needs separate destination consent and an available adapter. Unsupported extraction is reported, not synthesized as if read. These are entry conditions and alternatives, not evidence that a capture or extraction ran. SRC-1: `skills/wiki-ingest/SKILL.md`.

The orchestrator can assign independent sources to workers. Each assignment must supply the selected vault root, one local source path and stable identifier if assigned, requested emphasis/filing mode, and explicit pages or a bounded discovery scope. The worker stops rather than substitutes another source when the input is missing, outside the vault, uncaptured or ambiguous. The governing handoff is explicit:

> The parent orchestrator
> alone merges all worker drafts, inspects one
> `claude-obsidian.transaction.v1` bundle, and applies it once.
> --- `agents/wiki-ingest.md`

This divides synthesis from shared mutation. The skill forbids worker writes, address reservations, manifest edits and ledger updates; the parent resolves conflicts and merges once. That is a model-facing protocol, not a package-enforced read-only sandbox: the worker exposes Bash and the host controls effective permissions. [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-BAP-skill-authority](runtime.md#rt-bap-skill-authority) retain the tool/model and authority evidence. SRC-1: `agents/wiki-ingest.md`, `skills/wiki-ingest/SKILL.md`.

### Worker evidence and return boundary

Before drafting, the procedure hashes payloads and checks the legacy manifest and source ledger for unchanged input. It classifies each source and applies a compilation-value gate: source retention alone does not require a canonical paraphrase. A source can yield a source/ledger record or no-op when it adds no durable synthesis, navigation, decision or reusable connection. Workers read configuration, active methodology, hot/index orientation and relevant existing pages. The parent skill defaults to five existing pages per source and requires an explicit budget increase. Complete source reading is requested; an unread range makes the result partial. SRC-1: `skills/wiki-ingest/SKILL.md`, `agents/wiki-ingest.md`.

The worker returns YAML, not transaction success. The packet includes source identity/path/hash/title; create/replace proposals with purpose, expected target hash and content; claim evidence with real locator and exact excerpt when available; contradictions; open questions; and completed/remaining work with a concrete partial reason. Target hashes must come from current bytes; null is only for verified absence. These fields let the parent merge without guessing while retaining what was not established. They do not mechanically establish that an excerpt supports a claim. SRC-1: `agents/wiki-ingest.md`.

The turn-budget failure branch protects delivery of verified work:

> If the complete packet is at risk, stop new
> discovery and return a structured `partial` packet while there is still room;
> include only verified work, name every unread or unfinished item, and give the
> parent a resumable next step.
> --- `agents/wiki-ingest.md`

Thus source exploration can stay in a separate worker context while the structured result crosses back to the parent. The source does not establish actual host isolation or removal of the parent's old turns. Nor does it give a deterministic rescheduling algorithm for partial packets: the parent receives a resumable next step and retains responsibility for completion or reduced scope. Unrequested hot/index/log/address/manifest drafts are omitted from the packet. The parent owns these shared updates. SRC-1: `agents/wiki-ingest.md`.

### Parent synthesis, verification and review

The orchestrator resolves overlaps and contradictions across proposals, reuses existing canonical pages and stable addresses, and assembles one `operation_type: ingest` bundle for the agreed batch. As applicable it couples create-only raw captures, source summaries/canonical changes, separate source and claim ledgers, managed manifest/address requests, active indexes or MOCs, one batch log entry and refreshed hot context. Canonical creates/removals require active navigation updates; overview changes are conditional on a changed high-level picture. These coupling requirements are skill instructions, not evidence that every required relationship is checked by code. SRC-1: `skills/wiki-ingest/SKILL.md`, `skills/wiki/references/operation-transactions.md`.

Verification has distinct owners. The worker and parent are told to compare claims with source evidence and preserve contradictions. The provenance policy defines accepted claims as requiring fresh active non-synthetic support, with two independent sources for high risk; insufficient evidence should produce uncertainty or refusal. No supplied expected-answer oracle determines the correct synthesis. The human reviews the proposed scope and content. The core admits the submitted plan using hashes, operation scope and prospective ledger validation, not an authenticated human judgment or a factual proof of the prose. [RT-BAP-plan-enforcement](runtime.md#rt-bap-plan-enforcement) retains the enforcement witness. SRC-1: `skills/wiki-ingest/SKILL.md`, `skills/wiki/references/provenance.md`, `claude_obsidian/transaction.py`.

The transaction's provenance check runs when at least one ledger is among planned writes, and loads the prospective pair using planned content where available. Its checked scope is explicit:

> """Validate the complete prospective source/claim ledger pair."""
> --- `claude_obsidian/transaction.py`

This implementation supports a ledger admission mechanism; it does not establish that every source statement was read, that every claim was captured in a ledger, or that model interpretation is correct. The workflow separately requires a user-facing preview:

> Show the user the inputs, budget consumed, create/replace paths, raw captures,
> claim assessments, contradictions, and skipped items before apply. Canonical
> replacements or an expanded scope require explicit review.
> --- `skills/wiki-ingest/SKILL.md`

The parent runs transaction inspect, then supplies the returned `approval_sha256` to CLI apply after review. That digest binds the prepared plan and selected vault, but cannot prove who reviewed it. Direct callable capture can omit approval, as [RT-RTE-direct-capture](runtime.md#rt-rte-direct-capture) shows; it is not the selected reviewed Ingest CLI branch. SRC-1: `skills/wiki/references/operation-transactions.md`, `claude_obsidian/transaction.py`.

### Application, rejection and recovery

Local Python is the mutation executor. Under the mutation lock it recovers incomplete operations, expands managed metadata, prepares writes/backups and recomputes approval. It journals before applying, checks declared read preconditions and each target's original hash/mode, writes through confined atomic replacements, updates the journal, validates completed state, stores changed paths and marks completion. The lock coordinates cooperating writers; per-file atomic replacement is not simultaneous visibility of the whole batch. Only declared preconditions protect the non-write context that the agent previously read. SRC-1: `claude_obsidian/transaction.py`; [RT-RTE-save-apply](runtime.md#rt-rte-save-apply).

A concrete rejection branch is concurrent vault drift. The skill requires exit 75 to lead to rereading and rebuilding, rather than overwriting stale state:

> On exit 75,
> re-read and rebuild. Use `transaction recover` after interruption.
> --- `skills/wiki-ingest/SKILL.md`

The parent therefore owns proposal recovery: refresh affected inputs, resolve changed content, inspect a new plan and seek renewed review where needed. The core owns journal restoration on exceptions during writes or completed-state validation; explicit transaction recovery also handles interruption. Recovery does not authorize overwriting unrelated external changes, and can retain rollback failure. The supporting drift-refusal passage is already in [RT-RTE-save-apply](runtime.md#rt-rte-save-apply). Nothing here demonstrates that a real failure was recovered. SRC-1: `claude_obsidian/transaction.py`, `skills/wiki/references/operation-transactions.md`.

### Delivery and later consumption

A worker packet is not delivery of an ingested vault. Delivery requires the parent to obtain the apply result and report its operation ID and exact changed paths. Identical completed-ID replay returns the stored result only after result validation; a reused ID with different bundle content conflicts, and result drift blocks successful replay. Optional Git checkpointing is a separately requested action, not the definition of ingestion success. SRC-1: `skills/wiki-ingest/SKILL.md`, `claude_obsidian/transaction.py`.

The admitted pages and hot/navigation updates can later enter Query and opted-in lifecycle context through [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) and [RT-RTE-session-context](runtime.md#rt-rte-session-context). That closes the shipped persistence/read-back pathway, not a demonstrated improvement in answers. Unadmitted worker drafts have no established later-vault read-back route. The evidence does not show a successful batch, correct synthesis, user acceptance or downstream behavioral benefit.

Added source inspection under SRC-1: complete `skills/wiki-ingest/SKILL.md`, `agents/wiki-ingest.md`, `skills/wiki/references/provenance.md` and `skills/wiki/references/operation-transactions.md` for doctrine/design; `claude_obsidian/transaction.py` apply body and opening prospective-ledger validator for implementation. These extend the provisional runtime baseline without adding a source or observed-run evidence layer.

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

#### On [RT-RTE-ingest-drafts](runtime.md#rt-rte-ingest-drafts)

Workflow role: source-local draft production followed by one foreground merge. The parent supplies explicit source/root and bounded discovery; the worker returns evidence, target preconditions, contradictions and completion limits. Missing or ambiguous source inputs stop delegation; turn-budget pressure yields verified partial work with a resumable next step. Neither packet state permits the worker to claim shared mutation. The parent owns unresolved filing/merge decisions, shared navigation updates and admission. This is bounded requested orchestration, not a demonstrated scheduler or retry implementation.

Verification and delivery: evidence comparison and compilation value are model-facing judgments; human review applies to canonical replacements or expanded scope; deterministic persistence checks are a separate endpoint. No expected-answer oracle is supplied. The packet is an intermediate return, while operation ID and exact changed paths after apply define the requested final delivery.

#### On [RT-RTE-save-apply](runtime.md#rt-rte-save-apply)

Workflow role: the shared journaled executor is reached here by a single batch Ingest bundle rather than separate worker applies. The parent must couple source/provenance/navigation proposals before inspection. On stale-input conflict the parent rereads and rebuilds; the core handles journal restoration and explicit interruption recovery. Human prose review remains a protocol distinct from approval-hash comparison. These workflow responsibilities neither expand the core's validation coverage nor establish successful execution.
