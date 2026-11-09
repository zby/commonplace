---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Project Wiki memory: canonical project records, provenance-only intake, resumable review and task-directed index routing."
run-id: AAS-2026-11-08-project-wiki-b055e5c71dc7-01
source-identity: "https://github.com/giodra96/project-wiki"
reviewed-boundary: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
---

# Project Wiki memory report

## Boundary and evidence

Project Wiki retains project knowledge in a consuming repository, not in a hosted memory service. This account includes initialization, notes, document intake, review resumption, canonical authoring, automatic coding-task consultation and updates, explicit synchronization, maintenance, configuration, source exclusions and instruction bootstrap. It uses SRC-1 at the boundary's frozen commit. The external host's model, context-window management, tool permissions and actual instruction loading remain outside the inspected implementation. No populated consuming wiki or execution trace was supplied. The retained objects below describe generated artifact contracts and their prescribed consumers, not observed instances.

Direct reads covered `SKILL.md`; `references/automatic-workflows.md`, `references/common-policies.md`, `references/update-workflows.md`, `references/document-ingestion.md`, `references/wiki-structure.md`, `references/maintenance-workflows.md`, `references/source-inbox.md`, `references/configuration.md`, `references/repository-scope.md`; root/index and registry templates in `assets/core-templates.md`; requirement/provenance and ADR template ranges in `assets/requirements-change-templates.md`; and snapshot loading and view selection/output in `scripts/review_progress.py`. These add doctrine/design and implementation depth under the existing SRC-1, not a new source. Other helper control-flow findings below are attributed to supplied runtime records rather than presented as fresh direct inspection.

| Entry point or operation | Source paths, SRC-1 | Coverage and conclusion limits |
| --- | --- | --- |
| Explicit modes and automatic triggers | `SKILL.md` | Direct dispatch-table read; [RT-OBJ-skill](runtime.md#rt-obj-skill). Host-interpreted routing, not a central executable or inspected host hook. |
| Init/scan and instruction bootstrap | `references/wiki-structure.md`, `assets/core-templates.md`; runtime's `scripts/wiki_scaffold.py`, `references/initialization-workflows.md` | Direct structure/template reads plus supplied [RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki) and [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol). Structural placeholders are not acquired project knowledge. |
| Notes, answers and chat-derived knowledge | `references/update-workflows.md`, `references/common-policies.md` | Direct; [RT-RTE-note-update](runtime.md#rt-rte-note-update), [MEM-OBJ-canonical-records](#mem-obj-canonical-records). No complete conversation archive is implied by filing a synthesis. |
| Inbox admission, hash/history and quarantine | `references/source-inbox.md`; runtime's `scripts/check_inbox.py`, `scripts/ingest_document.py` | Direct protocol plus [RT-RTE-source-intake](runtime.md#rt-rte-source-intake); [MEM-OBJ-source-registry](#mem-obj-source-registry). Direct explicit document ingestion is an alternative admission path, not proof of inbox deduplication. |
| Extraction and optional copied source | `references/document-ingestion.md`; runtime's `scripts/ingest_document.py` | Direct artifact contract plus supplied helper findings; [MEM-OBJ-intake-provenance](#mem-obj-intake-provenance). OCR, images and legacy DOC are unsupported by declared format scope. |
| Inspect/view/apply/audit, status and audit-skips | `references/document-ingestion.md`, `scripts/review_progress.py` | Direct documentation and load/view implementation; supplied runtime apply/audit findings. [MEM-OBJ-review-progress](#mem-obj-review-progress) and intake-route annotation. Diagnostics do not admit canonical meaning. |
| Canonical integration and blocking review | `references/document-ingestion.md`, `assets/requirements-change-templates.md` | Direct; [MEM-OBJ-canonical-records](#mem-obj-canonical-records), [MEM-OBJ-requirement-evidence](#mem-obj-requirement-evidence). Human authority decisions are conditional; ordinary integration is agent-admitted. |
| Future-task read-back and source access | `references/automatic-workflows.md`, `references/repository-scope.md`, `assets/core-templates.md` | Direct; [MEM-OBJ-wiki-routing](#mem-obj-wiki-routing), coding-cycle annotation. Runtime supplies `scripts/wiki_scope.py` implementation account. No token-bound delivery guarantee. |
| Automatic writes and configuration CLI | `references/configuration.md`, `references/automatic-workflows.md` | Direct policies plus runtime configuration implementation account; [MEM-OBJ-project-controls](#mem-obj-project-controls). Config changes are not semantic synchronization. |
| Sync, migration, lint, validation and contract checks | `references/maintenance-workflows.md`, `references/common-policies.md`; runtime's `references/synchronization-workflow.md`, `scripts/validate_wiki.py`, `.github/workflows/tests.yml` | Direct maintenance policies plus [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile). Validator structural result and model semantic judgment have different authority. Contract checks/CI do not establish semantic benefit. |
| Help | `SKILL.md`; runtime's `scripts/wiki_help.py` | Direct dispatch policy plus supplied runtime account: bundled static guide, read-only early return, not retained-memory read-back. |
| External host, provider state and consumption | `SKILL.md`; [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent) | Supplied host boundary; model parameters, native compaction, subagent contexts, actual scheduling/loading and deployments uninspected. Prevents claims of enforcement, activation or effective learning. |

No additional registered service or library consumer is established by the shipped entry table. The helper CLIs and generated instruction blocks are the material exposed paths covered here. This is not an absence claim about external host integrations.

## Core ideas

1. **Canonical knowledge is separated from source retention.** Extracted text, raw sources and pending decisions remain provenance or workflow state. Canonical integration changes where later ordinary work is supposed to read. Terminal intake is deliberately excluded from routine coding consultation ([MEM-OBJ-intake-provenance](#mem-obj-intake-provenance)). A source's presence or completed ledger does not itself grant it canonical authority.
2. **Routing controls acquisition before context entry.** The foreground agent selects root index, section index and task-relevant pages, falling back to catalog/traceability. Review uses source-defined sections or complete text, not relevance-scored chunk retrieval. These are instructions and deterministic view selectors, not host-window eviction ([MEM-OBJ-wiki-routing](#mem-obj-wiki-routing); intake-route annotation).
3. **Admission is semantic and distributed.** Helpers bind bytes, check structure and record dispositions. The host compares source meaning with existing records and normally integrates conservatively without per-claim human approval. A human resolves blocking authority/baseline/binding decisions and high-impact maintenance changes. Disabling automatic writes does not revoke explicit update or maintenance ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake), [MEM-OBJ-project-controls](#mem-obj-project-controls)).
4. **History is retained without making it all active context.** Stable IDs, rationale, evidence edges, resolved questions, closed alerts and audit entries preserve revision context. Index compaction moves detail to pages; it does not compact the agent's conversational window. Preserved reasons are available to selected later reads, not guaranteed to be read on every task ([MEM-OBJ-canonical-records](#mem-obj-canonical-records), [MEM-OBJ-audit-history](#mem-obj-audit-history)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-canonical-records
Label: Canonical project records and durable analysis

Identity: project-local Markdown under `requirements/`, `changes/`, `technical/`, `implementation/`, plus `PROJECT.md`, `GLOSSARY.md`, `STATUS.md`, durable `analysis/`, questions and alerts. These are accumulated project content, distinct from the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki) and driver [RT-OBJ-skill](runtime.md#rt-obj-skill); neither supplied object denotes the generated content. Different record families share file-based natural-language consumption and host semantic admission, but retain different authority: requirements express confirmed intent, technical pages express observed implementation, and analysis is non-canonical synthesis. Symbolic IDs/status/confidence/frontmatter provide catalog and validation handles, not executable guarantees that prose is true.

Storage and form: repository Markdown; natural-language statements, explanations and decisions interpreted by later agents, with symbolic metadata checked by helpers. Lineage includes explicit user/stakeholder notes, reviewed source chunks, source-code findings, agent analysis and durable chat answers. Scans may be inferred/unknown; code-derived behavior is not promoted to confirmed intent merely because it looks like a requirement. Initial scaffold placeholders are non-authoritative until project-specific semantic work occurs ([RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki)).

Write agency/admission: host authors and edits content under explicit workflow authorization or automatic impact rules. Human initiation does not approve each content unit. Blocking document decisions and high-impact maintenance changes have conditional human veto. Curation includes classification, comparison, topic decomposition, synthesis, question reconciliation, revision and status withdrawal. Consumers are future coding/planning agents and maintenance/sync agents selecting pages; force is task evidence or project-intent guidance interpreted by that consumer, not host instruction priority. Horizon is later tasks/sessions when files persist and are loaded. No observed behavior change is supplied.

Reasons and evidence are intended to persist: requirements have rationale and acceptance notes; ADRs preserve context, alternatives and consequences; questions retain resolution evidence. Later page selection can deliver those sections, but there is no separate guaranteed reason-reader. Exact document-derived source edges reside outside the readable requirement body in [MEM-OBJ-requirement-evidence](#mem-obj-requirement-evidence).

Evidence: SRC-1, `references/wiki-structure.md`, `references/update-workflows.md`, `assets/requirements-change-templates.md`.

> Product intent comes from explicit business, user, stakeholder, meeting, issue, ticket, chat, or imported requirements sources. Implemented behavior discovered in code belongs in `technical/` unless an explicit source confirms it as a requirement.
> --- `references/wiki-structure.md`

> Open questions are durable records. Do not delete them when answered. Close, narrow, supersede, dismiss, or merge them with evidence.
> --- `references/wiki-structure.md`

#### MEM-OBJ-wiki-routing
Label: INDEX and REGISTRY access metadata

Identity: generated root/section `INDEX.md`, `REGISTRY.yml` and traceability routing maps. Distinct from the schema that defines their shapes [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki), and from content pages [MEM-OBJ-canonical-records](#mem-obj-canonical-records). Storage: repository Markdown/YAML. Form: natural-language task-routing labels and summaries interpreted by the host; symbolic paths, IDs, relationships and anchors checked by the validator. These are access metadata rather than substitutes for full retained claims.

Lineage: scaffold/template routing followed by host edits when catalog or routing changes; human control of each edit is not established. Later coding preflight selects the smallest relevant section from the root table, then linked documents. Registry and traceability are fallback when context is missing, not a vector search or fixed ranking function. Task description and already-read/current context drive host selection. No numerical token/page budget is specified. Routing changes and date/catalog consistency are maintenance concerns; stale routing can prevent useful delivery even when content survives. Evidence: SRC-1, `references/automatic-workflows.md`, `references/common-policies.md`, `assets/core-templates.md`.

> 4. If the needed context is missing, read `REGISTRY.yml` and traceability maps before broad code search.
> --- `references/automatic-workflows.md`

#### MEM-OBJ-intake-provenance
Label: Intake extraction provenance

Identity: `intake/documents/DOCIN-*/` source-info, extraction index, manifest, chunk files, optional copied source and extraction report. Distinct from the shipped contract [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki); the closest supplied route is [RT-RTE-source-intake](runtime.md#rt-rte-source-intake), not an object declaration. Storage: repository YAML/JSON/Markdown and optionally original binary/text file. Form: natural-language extracted content, symbolic hashes/counts/paths/section metadata, and opaque original payloads such as PDF/DOCX. Readable extraction is not complete understanding of those payloads: image/diagram interpretation and OCR are outside the declared extractor scope.

Lineage: helper snapshot of local source bytes, SHA-256, format extraction, heading-aware chunking, full text in separate chunk files; optional source copy only when requested or needed to retain a temporary original. `extracted.md` and `intake-report.md` are compact displays/routing, not the text store; manifest previews/hints are metadata, not canonical semantic classifications. Source trust remains a separate host/human authority decision.

Admission: helper publishes byte/structure-validated extraction, not canonical project truth. Host admits semantic results separately. Immutable provenance is a policy; review state is separately mutable. Before integration, materially bad extraction is rejected/superseded and regenerated; after integration, affected canonical records require correction and a new audit entry. Minor usable issues receive warnings. A legacy overflow-producing extraction may be superseded or removed and regenerated under the documented exception.

Consumers: review helper reloads text, host reviews returned source sections/all, and later provenance/audit/conflict investigation may reread it. Ordinary coding should not consult terminal intake. This is a retained-source read-back path, not automatic supply to every task; lifecycle metadata restricts intended use without proving filesystem denial. Evidence: SRC-1, `references/document-ingestion.md`, `scripts/review_progress.py`.

> `extracted.md` is a compact extraction index. It records extraction counts and routes agents to `review_progress.py`; it never stores full text or enumerates chunks.
> --- `references/document-ingestion.md`

> 16. Do not consult `integrated`, `archived`, `superseded`, or `rejected` intake documents during normal coding tasks unless the user asks for provenance, audit, or conflict investigation.
> --- `references/document-ingestion.md`

#### MEM-OBJ-review-progress
Label: Review progress ledger and blocking review

Identity: mutable `review-progress.yml` and conditional agent-authored `review.md` within intake. Separate parts: the ledger is symbolic per-chunk state with classifications, target IDs, counts and natural-language skip notes; blocking review is natural-language decision/evidence/options, not canonical knowledge. Storage: repository YAML/Markdown. Both are workflow state for [RT-RTE-source-intake](runtime.md#rt-rte-source-intake), not a duplicate of that route or the immutable extraction object.

Lineage/admission: extraction initializes pending entries; the host supplies JSON dispositions to `apply`, whose structural checks/atomic write are reported in runtime. Reviewed is incomplete; classified/skipped are final. The helper does not prove prior reading or semantic accuracy. `audit` records a digest of ledger bytes, not a score of canonical meaning. Decision-focused `review.md` exists only when human resolution is needed; after resolution the agent resumes integration once. Pending approval is not approved knowledge.

Later consumers: resumed review uses inspection and view markers with ledger statuses; audit/validator use final coverage and target edges; the agent/human reads a blocking review to settle authority or scope. Ledger checkpoints support task interruption without requiring the old conversation window. They retain dispositions and skip reasons, not necessarily the full reasoning behind every classification. No observation of successful resumption is supplied. Evidence: SRC-1, `references/document-ingestion.md`; [RT-RTE-source-intake](runtime.md#rt-rte-source-intake).

> `review-progress.yml` is mutable workflow state. It contains one entry for every manifest chunk, aggregate counts, classifications, target wiki IDs, and skip reasons.
> --- `references/document-ingestion.md`

#### MEM-OBJ-requirement-evidence
Label: Requirement evidence sidecar

Identity: generated `traceability/requirement-evidence.yml`. This is provenance metadata distinct from requirement prose and the generic schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki). Storage/form: repository YAML with symbolic record-to-full-chunk-ID edges. Lineage: host records exact edges after source review and atomic requirement decomposition. Human authorization of source integration does not imply human approval of every edge.

Consumers and force: validator checks edge consistency with integrated ledger targets; human requirement map is derived from this sidecar. A later agent investigating provenance must follow these edges to intake text; a plain readable requirement intentionally omits chunk IDs. Structural equality of edges does not establish entailment. Canonical content can reach ordinary coding without its complete provenance entering the same context. Recovery requires correcting affected records/edges and auditing, not just relabeling a bad source. Evidence: SRC-1, `assets/requirements-change-templates.md`, `references/document-ingestion.md`; supplied [RT-RTE-source-intake](runtime.md#rt-rte-source-intake).

> Use full chunk IDs, one explicit entry per edge, with no ranges or duplicates. Keep chunk IDs and paths out of readable REQ/NFR/CON bodies; non-intake source paths remain valid elsewhere. The human requirement map is derived from this sidecar, and integrated ledger targets must match it bidirectionally.
> --- `assets/requirements-change-templates.md`

#### MEM-OBJ-source-registry
Label: Raw source archive and SOURCE_REGISTRY

Identity: `sources/inbox/`, `processed/`, `rejected/`, `ignored/`, `sources/INDEX.md` and `SOURCE_REGISTRY.yml`. Distinct from [MEM-OBJ-intake-provenance](#mem-obj-intake-provenance), the downstream extracted snapshot, and from [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki), the defining schema. Storage/form: local raw files including opaque document binaries; symbolic YAML source IDs, hashes, paths, statuses, intake IDs and dates; readable index summaries/notes.

Lineage/control: users supply files; preflight determines process/skip/review using validated history and byte hashes. Software quarantine can move skip files without canonical semantic admission; the host maintains lifecycle entries and archives successful sources. Historical path/new bytes and ambiguous histories require resolution before ingestion; explicit reprocessing can override skip while preserving history. This deduplicates bytes and process history, not meanings. Later preflight and validator consume retained hashes and archival bytes; update consumes pending sources. Raw retained content is not ordinary canonical project guidance. Source exclusions can suppress refresh without deleting already extracted history. Evidence: SRC-1, `references/source-inbox.md`, `references/wiki-structure.md`; [RT-RTE-source-intake](runtime.md#rt-rte-source-intake).

> The preflight cross-checks registry entries with complete intake history, so stale source status does not silently authorize reingestion.
> --- `references/wiki-structure.md`

#### MEM-OBJ-audit-history
Label: Wiki audit and maintenance history

Identity: weekly `logs/wiki-log-YYYY-Www.md`, project `changes/CHANGELOG.md`, maintenance lint/migration reports, scan records and closed alerts/questions. They preserve different histories: wiki edits versus project change versus findings/recovery. These histories are distinct from supplied [RT-OBJ-skill](runtime.md#rt-obj-skill); they are generated retained results. Closed record content remains part of [MEM-OBJ-canonical-records](#mem-obj-canonical-records), while this record concerns its historical/audit consumption path, not a second identity for each closed record.

Storage/form: Markdown natural-language summaries/findings/reasons plus symbolic IDs, links, status and ledger digests. Lineage: host curates meaningful updates and helper structural results into compact logs/reports; raw coding chats/tool traces are not implied. Audit logging alone is not automatic trace learning. Later maintenance, explicit history/provenance investigation and sync baseline selection can consume retained results; routine tasks receive only selected linked context. Logs are not automatically injected or a demonstrated optimizer.

Curation: extend only the latest entry for the same ongoing activity; preserve prior information; separate mandatory intake/migration events; use corrective entries for historical meaning. Semantic lint can generate follow-up questions/alerts and revisions, with user confirmation for high-impact meaning changes. Index compaction moves detail into pages, leaving linked content reachable. Evidence: SRC-1, `references/common-policies.md`, `references/maintenance-workflows.md`, `references/wiki-structure.md`; [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile).

> Earlier entries may only receive formatting/link repairs; clarify historical meaning with a new corrective entry.
> --- `references/common-policies.md`

#### MEM-OBJ-project-controls
Label: Project configuration and source exclusions

Identity: project-retained `.project-wiki/config.yml` and `.wikiignore`, not the shipped schema [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki). Distinct operative parts with different consumers: symbolic YAML preference controls automatic-write policy via helper output and host interpretation; symbolic ignore patterns control helper source filtering. Storage: repository files outside the document registry. Lineage: scaffold defaults, deliberate user edits/configuration requests, and preservation during migration. Configuration may be edited directly; the generic filesystem writer alone would not prove human per-content approval, while the config workflow explicitly routes a requested preference change.

Later consumption: preflight reads effective config; potentially changed settings are refreshed before automatic processing. False/invalid suspends automatic assessment and writes, not preflight or explicit work; absent config defaults enabled. Re-enabling does not repair skipped updates. Source ignore rules are reused by source helpers, not a host filesystem sandbox. Exclusion suppresses new source reads/refresh but preserves consultation of previous wiki/intake history. These settings change selection/admission authority, not semantic truth or deletion. Evidence: SRC-1, `references/configuration.md`, `references/repository-scope.md`; runtime load-bearing controls.

> The generated blocks reference the configuration dynamically; never embed the current boolean value.
> --- `references/configuration.md`

> Existing wiki documentation, traceability, intake artifacts, and audit history remain consultable; they are not refreshed from excluded sources.
> --- `references/repository-scope.md`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle)

Memory consumer: a later foreground coding/planning invocation, conditional on host loading the generated protocol. Direction: automatic preflight is prescribed by task trigger; the agent then actively requests selected files. The selector is the host interpreting the task against root and section routing, not an independent retrieval service. Inputs are task, current indexes, already-read/current pages and fallback metadata. Selected parts are task-relevant canonical pages; only affecting facts should be summarized. Budget is qualitative, smallest relevant set; no token cap or enforced window accounting.

Working-context control: reuse still-current pages rather than reload after every edit. This limits new acquisition; it does not remove prior turns or guarantee that the host retains them. Static workflow selection similarly loads one relevant procedure, not accumulated memory. No child frame or return-only subagent boundary is specified here. The stack-frame analogy does not establish host isolation: helper calls return selected text by value into the same foreground context; links on disk remain reload routes, not live references tracked by the context manager. Evidence: SRC-1, `SKILL.md`, `references/automatic-workflows.md`.

> Reuse context already read in the same ongoing task while it remains current; do not reload unchanged pages after each small edit.
> --- `references/automatic-workflows.md`

#### On [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

Read-back consumer: same or later review invocation using persisted extraction and ledger, then later ordinary tasks consuming admitted canonical results. `inspect` loads validated intake data but delivers compact structure/aggregate state rather than all text. Direct implementation inspection shows `load_intake_snapshot` loads all chunk files before view selection; context reduction concerns returned output, not lazy disk loading.

> chunks = [load_chunk(document_root, entry, intake_id, contract) for entry in manifest["chunks"]]
> --- `scripts/review_progress.py`

`view --section` selects membership in source-defined section chunk IDs; `--chunks` selects explicit IDs and emits in source order; `--all` returns everything. This is identifier/structural selection, not task-targeted relevance ranking. Default markdown returns full selected text plus provenance/status markers; JSON includes the same selected text. No summary replaces the source text.

> selected_ids = set(section["_chunk_ids"])
> chunks = [chunk for chunk in chunks if chunk["id"] in selected_ids]
> --- `scripts/review_progress.py`

> print(chunk["text"])
> --- `scripts/review_progress.py`

The extraction `--max-words` default is 350 words per chunk, not a bound on a section/all response or the model window. Policy requires all reliable sections including unsectioned content, or all text when full-document context matters. Explicit chunk selection is reserved for rereading after complete review; the CLI selector itself does not prove completion or enforce the semantic reading order. `status --limit` provides diagnostic ledger display, not full-source review. `audit-skips` exposes excluded runs/notes/lexical signals for investigation, explicitly not a semantic verdict. Alternative legacy full-text formats are superseded/regenerated rather than loaded into context by migration policy (SRC-1, `references/document-ingestion.md`, `references/maintenance-workflows.md`).

> Progressive review manages context; it never permits truncating findings.
> --- `references/document-ingestion.md`

Retained reasons: skip notes and conditional blocking-review reasons survive; classification does not require a full rationale. Requirements/ADRs preserve downstream rationale fields, while sidecar edges preserve provenance separately. Digest/coverage delivery does not prove semantic activation or truthful canonical claims.

#### On [RT-RTE-note-update](runtime.md#rt-rte-note-update)

Memory transformation: user notes and durable agent answers become classified canonical revisions or linked non-canonical synthesis. In automatic filing the foreground agent decides lasting value and representation under the write gate; the human is not a mandatory per-answer approver. This is a prescribed trace-fed write pathway when a chat answer/task outcome is transformed into durable knowledge and a later preflight selects it. It does not entail saving raw conversation, training parameters or improved future capacity. Explicit update bypasses the automatic preference gate but not intent/uncertainty rules. Reasons survive where included in target record fields; no universal reasoning-transcript retention is specified (SRC-1, `references/update-workflows.md`, `references/automatic-workflows.md`).

#### On [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile)

Curation/read-back: sync reads retained claims against current included source and a reliable baseline; maintain reads structure, content and findings, revises selected records, preserves history and refreshes stale protocol blocks. Low-risk structural repairs are distinct from semantic withdrawal requiring confirmation. Moving verbose index detail to linked documents reduces future routing loads, not the current model window. Terminal legacy ledger skip reasons preserve the fact of migration without asserting retrospective semantic review (SRC-1, `references/maintenance-workflows.md`).

> For terminal legacy intakes, create a complete ledger with explicit legacy skip reasons rather than claiming retrospective semantic coverage.
> --- `references/maintenance-workflows.md`

#### On [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol)

Memory authority: the marked block is generated behavioral instruction, not merely project-fact memory. It is installed/refreshed from shipped guidance, with dynamic preference reads; project knowledge reaches later tasks through the consultation it requests. The source supports an instruction-level path across sessions, not reliable loading/compliance. Ordinary canonical pages supply task knowledge; they are not all automatically promoted to the host's top-level instruction force. No new behavioral-authority record is needed for this same generated block (SRC-1, `references/wiki-structure.md`, `references/configuration.md`; supplied record's bootstrap/template evidence).

## Write side

Acquisition has several independent admission paths. Init/scan starts from structural placeholders and project evidence; explicit pasted notes enter classification without document chunk review; document intake acquires byte-bound snapshots with coverage state; automatic post-code updates derive durable changes from task-scoped diffs; durable answer filing derives selected synthesis from chat work. These share target authoring policies but not identical provenance guarantees ([RT-RTE-initialize-wiki](runtime.md#rt-rte-initialize-wiki), [RT-RTE-note-update](runtime.md#rt-rte-note-update), [RT-RTE-source-intake](runtime.md#rt-rte-source-intake), [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle)).

Authorship, physical persistence and admission differ. A helper writes extraction or ledger bytes; the host supplies semantic dispositions and canonical edits; a human may supply sources or authorize a blocking choice. Inbox hash decisions, structural validation and atomic ledger replacement do not approve the meaning of the resulting requirement. Explicit update normally permits direct conservative integration. Conversely, a source whose authority cannot be represented conservatively needs a focused human decision, not merely another software checkpoint. These distinctions are local to the artifacts above, not a single system-wide human-control classification.

The trace-fed chain is task/chat answer or agent-made source change → host impact/lasting-value judgment → affected canonical record or durable synthesis with links/history → later index-selected coding/planning context. This is an afforded retained-text update path, conditional on the automatic gate for automatic writes. Raw logs alone are not the transformed result, and no supplied run establishes successful repeated use or improved action. There is no source basis here for attributing provider-weight updates to the skill ([RT-CMP-host-agent](runtime.md#rt-cmp-host-agent)).

Withdrawal preserves evidence: reject/supersede materially wrong extraction, regenerate, correct already integrated claims, and append audit history. Stale canonical pages receive revision/status changes, not silent historical deletion. Questions and alerts retain resolution evidence. Migration preserves project-authored content, resets active legacy review honestly to pending, and requests confirmation before risky moves/deletions/meaning changes. Cleanup of failed helper publication is not rollback of all semantic edits. Review rejection remains workflow state until canonical consequences and catalogs are reconciled ([MEM-OBJ-intake-provenance](#mem-obj-intake-provenance), [MEM-OBJ-review-progress](#mem-obj-review-progress), [RT-RTE-explicit-reconcile](runtime.md#rt-rte-explicit-reconcile)).

## Read-back

The ordinary later consumer is explicitly shipped: a future coding agent is instructed to read the index and linked current knowledge before work. This exceeds a storage-only API with an imaginary caller, but remains afforded operation rather than observed execution. Persistence is repository-local across tasks/sessions, not an expiring cache. Task relevance, status and routing affect intended access; no general TTL is specified. Stale/excluded evidence may remain physically available while no longer refreshed.

The review consumer is distinct. It requests structural views of retained source text and sees current disposition markers. A later review invocation can reconstruct progress from ledger state without the original chat. Complete review is a semantic protocol; all-text output and application of final dispositions do not prove careful reading. Terminal source text is deliberately not normal coding context. Explicit provenance/conflict investigation remains a reload path ([MEM-OBJ-review-progress](#mem-obj-review-progress), [MEM-OBJ-intake-provenance](#mem-obj-intake-provenance)).

Maintenance, inbox preflight and validation also consume retained state, but with different authority. Hash/history controls source processing; structural checks control acceptance of artifact shape; semantic maintenance interprets claims and current evidence. Metadata read-back is not equivalent to model consumption of all source reasons. Requirement sidecar provenance and source text may be omitted from an ordinary canonical page read. Nothing in these prescribed paths proves that delivered facts changed an agent's decision or benefited a task.

## Integration issues

- No supplied generic identity requires correction. The memory objects are generated project artifacts or their access paths, not duplicates of [RT-OBJ-project-wiki](runtime.md#rt-obj-project-wiki), which explicitly denotes the shipped machine schema. Route and instruction-block identities are reused through annotations rather than redeclared.
- Clarification for [RT-RTE-source-intake](runtime.md#rt-rte-source-intake): compact section output does not mean lazy storage reads or a bounded context window. The directly inspected loader reads all chunks before `print_view` selects output (SRC-1, `scripts/review_progress.py`). Section/all output has no token bound; complete source review remains required. This qualifies any inference from the label progressive review, not the supplied route's explicit no-budget limit.
- Unresolved host activation: [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol) and [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle) prescribe later consultation, but host loading, context eviction and compliance are not supplied evidence. Prevented conclusion: exercised cross-session recall or reliable automatic maintenance.
- Unresolved content-instance quality: [MEM-OBJ-canonical-records](#mem-obj-canonical-records), [MEM-OBJ-requirement-evidence](#mem-obj-requirement-evidence) and [MEM-OBJ-review-progress](#mem-obj-review-progress) have inspectable contracts, not populated project results. Prevented conclusions: actual rationale completeness, accurate provenance entailment, successful resumption, or improved future capacity. Structural passes cannot settle them.
- No additional possible duplicate declarations were identified against supplied runtime records. No epistemic/workflow member was supplied; reconciliation should compare any later declarations of these same generated artifacts without treating differing prefixes as distinct identities.

## Limitations and checks

The source HEAD recheck returned `3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41`, matching the supplied boundary. The invocation's job, member types, collection, worker rules and complete records-contract ranges were read, with continuation reads recovered before source work. Inputs were used as supplied; no other run or prior characterization was read. Source inspection was read-only. Target scripts, tests, fixtures, examples, providers and services were not executed.

Evidence is implementation for directly inspected review loading/selection and supplied runtime helper findings; workflow content and generated artifact contracts are doctrine/design. No observed run or causal experiment is registered. Automatic text updates and cross-session storage support an architectural retained-memory pathway, not demonstrated learning, reflection or self-improvement. No universal absence of those properties is inferred from missing execution evidence. External host compaction/isolation and opaque provider state prevent claims about total context management or weight mutability.

Deterministic validation: passed using the invocation's prepared `commonplace-validate` command with this output, artifact and role memory. The check establishes format, references and quote occurrence, not semantic correctness or job acceptance.
