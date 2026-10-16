---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of OpenClerk's retained-state, admission, epistemic and session-planning routes at the frozen Git boundary."
run-id: AAS-2026-10-16-openclerk-ec0e00c2bb0a-01
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
---

# OpenClerk report verification

## Verification

The runtime, memory, epistemic, workflow and reconciliation members support publication of a bounded implementation account. No material correction is required. The remaining inventory limit is stated below; this is not a complete audit of every report or maintenance route.

### Evidence and verification method

I read all supplied members, their types and the records contract. The correction-answer files are empty. The supplied structural report says `none`, so there is no structural finding to route. I independently inspected source rather than accepting the analysts' validation statements as semantic verification.

SRC-1 remains the repository registered in the [Source register](boundary.md#source-register). `git rev-parse HEAD` returned `092fb98d243c2d9d95867ad04618ebce88983552`; `git status --short` was empty. The tracked top-level tree agrees with the boundary's coverage table. Source reads supplied implementation and doctrine/design evidence only. No target execution, tests, provider invocation, installation or new experiment occurred. Bundled evaluation filenames were inventoried but their outcomes were not adopted as observations.

Independent source inspection covered the relevant bodies of SRC-1 `internal/chronicler/chronicler.go`, `internal/runner/document.go`, `internal/runner/autonomy.go`, `internal/runner/retrieval.go`, `internal/runner/artifact_candidate_plan.go`, `internal/runner/compile_synthesis.go`, `internal/runner/audit_contradictions.go`, `internal/runner/source_audit_report.go`, `internal/runner/memory_router_recall.go`, `internal/runner/retrieval_eval.go`, and `internal/runner/semantic_search.go`. Storage witnesses were checked in `internal/infra/sqlite/documents.go`, `internal/infra/sqlite/store.go`, `internal/infra/sqlite/sync.go`, `internal/infra/sqlite/synthesis.go`, `internal/infra/sqlite/document_moves.go`, `internal/infra/sqlite/records.go`, `internal/infra/sqlite/services.go`, `internal/infra/sqlite/decisions.go`, `internal/infra/sqlite/ingest_source.go` and `internal/infra/sqlite/ingest_video.go`. Module binding and cache/provider branches were checked in `internal/runclient/local.go`, `internal/runclient/modules.go` and `modules/semantic-retrieval-adapter/main.go`. Evaluation setup, continuation and the stated substring oracle were checked in `scripts/agent-eval/ockp/codex_runner.go`, `scripts/agent-eval/ockp/constants.go` and `scripts/agent-eval/ockp/verify_helpers.go`. Doctrine and example checks used `README.md`, `docs/agent-contract.md`, `skills/openclerk/SKILL.md` and the session-to-docs example's command and handoff files. The two additional maintenance paths inspected for omissions are identified below.

### Runtime, permissions and host responsibilities

[RT-OBJ-agent-contract](runtime.md#rt-obj-agent-contract), [RT-BAP-skill-routing](runtime.md#rt-bap-skill-routing) and [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary) correctly distinguish instructions to an external host from enforced permissions. The shipped instruction asks for approval, but normalization defaults an omitted mode to `approve_write`. The document gate vetoes explicit `propose_only`; it does not authenticate a separate human decision. [RT-RTE-document-write](runtime.md#rt-rte-document-write) appropriately limits its detailed witness to creation/replacement and does not claim identical control across every branch. The lock coordinates cooperating runner writers, not arbitrary filesystem editors. Canonical creation precedes synchronization; replacement receipts supply another request for compensation, not automatic rollback.

[RT-RTE-context-pack](runtime.md#rt-rte-context-pack) and [RT-RTE-session-plan](runtime.md#rt-rte-session-plan) match the inspected orchestration. Query precedes task text in selection. Search snippets and decision summaries, not the complete vault, reach context packs. Explicit inbox artifacts reach deterministic planning, and the returned candidate does not itself become durable knowledge. Host scheduling, reasoning, actual compliance and accumulated-window management are not attributed to OpenClerk.

[RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search) and [RT-RTE-module-install](runtime.md#rt-rte-module-install) preserve the important alternate-path distinctions: enabled installed bindings are verified on configured use; local hashes do not certify executable safety or pin remote weights; the runner omits the adapter's fallback field; direct adapter execution can use that fallback after corpus-embedding failure. Canonical read-only access coexists with writable derived caches. Buffered subprocess output precedes the decoder's byte limit. The report does not turn that decoder limit into process isolation or a whole-process memory bound.

[RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) and [RT-CMP-codex-model](runtime.md#rt-cmp-codex-model) correctly leave parameter mutability and immutable weight identity uninspected. [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn) traces a shipped caller, not an excluded hypothetical application: setup and seeding precede model-driven turns; a session ID is reused for multi-turn scenarios; single-turn invocation requests ephemeral context. The requested host flags are not evidence of sandbox enforcement. The cited document verifier checks required/forbidden strings, which licenses bounded predicates rather than task correctness or causal benefit.

### Retained objects and their consumers

[MEM-OBJ-documents](memory.md#mem-obj-documents), [MEM-OBJ-chunks](memory.md#mem-obj-chunks), [MEM-RTE-vault-sync](memory.md#mem-rte-vault-sync) and [MEM-RTE-projection-read](memory.md#mem-rte-projection-read) correctly separate canonical-file authority from the database actually read by ID lookup and lexical retrieval. Synchronization imports selected nonsymlink Markdown, prunes missing rows, writes chunks/FTS and rebuilds projections. Ordinary initialized read-only opens do not perform that full synchronization. Uninitialized read-only opening can initialize storage, so the reports correctly withhold a universal zero-physical-write claim.

[MEM-OBJ-record-entities](memory.md#mem-obj-record-entities), [MEM-OBJ-service-records](memory.md#mem-obj-service-records) and [MEM-OBJ-decision-records](memory.md#mem-obj-decision-records) have distinct stored/query identities. The record and service extraction witnesses support parser-relative projection, not truth acceptance. The decision SQL supports the listed retained fields, not complete rationale preservation. [MEM-OBJ-graph](memory.md#mem-obj-graph) is supported as a rebuilt and exposed derived view; its explicit extraction/completeness limits prevent treating the rebuild witness as a full graph audit.

[MEM-OBJ-source-assets](memory.md#mem-obj-source-assets) correctly distinguishes PDF bytes, extracted notes, supplied transcripts and optional video metadata. The inspected video creation path writes metadata rather than acquiring media. Source-update impact reporting explicitly leaves synthesis unrepaired. The report makes no unsupported claim that original payloads automatically reach the ordinary answer model.

[MEM-OBJ-projection-states](memory.md#mem-obj-projection-states) separates current derivation metadata from transition events and historical full bodies. [MEM-OBJ-semantic-cache](memory.md#mem-obj-semantic-cache) accurately describes retained numerical vectors and symbolic cache identity: provider/model/filter/corpus keys and per-chunk checks govern reuse, not provider training. [MEM-OBJ-retrieval-cases](memory.md#mem-obj-retrieval-cases) identifies reduced retrieval traces, not a learned policy or correct-answer dataset. [MEM-BAP-retained-evidence](memory.md#mem-bap-retained-evidence) is a distinct payload/authority path from shipped instruction routing; its delivery does not establish interpretive activation.

[MEM-RTE-document-move](memory.md#mem-rte-document-move) is supported as sequential structural maintenance with partial-failure exposure. [MEM-RTE-policy-recall](memory.md#mem-rte-policy-recall) correctly identifies fixed paths, token-presence tests and largely code-authored summaries rather than a general autonomous memory router. [MEM-RTE-regression-replay](memory.md#mem-rte-regression-replay) preserves capture and later comparison without implying automatic ranker adoption.

### Epistemic checks, content transformations and force

[MEM-RTE-synthesis-compile](memory.md#mem-rte-synthesis-compile), [EPI-OBJ-synthesis](epistemic.md#epi-obj-synthesis), [EPI-RTE-synthesis-build](epistemic.md#epi-rte-synthesis-build) and [EPI-RTE-synthesis-write](epistemic.md#epi-rte-synthesis-write) match the compiler's actual source-evidence lookup, body assembly and target selection. Missing source lookup can continue with a path-only citation. Supplied body/facts are not checked against source assertions. Source-role labels and the specially prefixed summary transformation are real deterministic additions, not general model synthesis. Duplicate-target admission, persistence and substantive acceptance remain separate.

[EPI-RTE-synthesis-freshness](epistemic.md#epi-rte-synthesis-freshness) correctly bounds its derivation to stored paths, timestamps and supersession declarations. Generated `freshness: fresh` text is not the computed projection verdict. The check's output has actual consumers in reports and repair, but it neither endorses the body nor automatically withdraws it.

[MEM-RTE-synthesis-repair](memory.md#mem-rte-synthesis-repair) and [EPI-RTE-audit-repair](epistemic.md#epi-rte-audit-repair) correctly describe copying the first sorted current source's nonempty Summary when an existing target and current/superseded classes permit repair. [EPI-OBJ-audit-report](epistemic.md#epi-obj-audit-report) and [EPI-RTE-audit-conflicts](epistemic.md#epi-rte-audit-conflicts) preserve the finite day-value heuristic, snippet-based evidence and advisory force. The conflict check follows possible replacement; it is not a pre-write semantic veto. Distinct subjects can produce a numerical discrepancy, and unsupported quantities can be missed. These limitations materially qualify the source-native claim without denying the implemented check.

[EPI-OBJ-source-note](epistemic.md#epi-obj-source-note) and [EPI-RTE-web-import](epistemic.md#epi-rte-web-import) correctly classify acquisition rather than accepted novel production. Markdown normalization and HTML tag removal support the stated fidelity distinction. [EPI-OBJ-artifact-plan](epistemic.md#epi-obj-artifact-plan) and [EPI-RTE-artifact-ocr](epistemic.md#epi-rte-artifact-ocr) distinguish extracted candidate content from configuration/file/process checks and an unexercised review request. Neither module verification nor nonempty text licenses transcription accuracy.

[EPI-OBJ-retrieval-eval](epistemic.md#epi-obj-retrieval-eval), [EPI-RTE-eval-capture](epistemic.md#epi-rte-eval-capture) and [EPI-RTE-eval-replay](epistemic.md#epi-rte-eval-replay) match the captured selector/result-reference chain and later Jaccard/top1 comparison. Two empty sets can score perfect agreement. The emitted metrics do not implement acceptance of factual claims, relevance judgments or successor machinery. [EPI-CLM-markdown-authority](epistemic.md#epi-clm-markdown-authority) and [EPI-CLM-source-repair](epistemic.md#epi-clm-source-repair) accurately retain doctrine as doctrine and compare it with narrower implemented mechanisms. The bounded conclusion does not make a system-complete negative about acceptance, adaptation, learning or theory-building from these selected witnesses.

### Workflow, relations and reconciliation

[WF-RTE-artifact-plan](workflow.md#wf-rte-artifact-plan) supports the selected workflow without inventing a successful run. Inspection confirms the first-hit duplicate heuristic, title-plus-bounded-body query, candidate-directory default, confidence gating and suppression of a convenient create request. Those are proposal controls, not a universal veto against another caller's write. Chronicler returns a compact summary and selected fields; serialized next-create content can carry the full body. Per-file rejection continues while a returned Go error aborts. Inbox processing precedes the accompanying context request. The report correctly keeps the example's contrary high-level expectation separate from implementation and the contract's pre-work context step.

I checked every declared `Part of:` relation. Move and compilation are branches of the document-family container; the epistemic compiler build/write parts also fit that container; workflow artifact planning is inside explicit-session orchestration. Their distinct effects and owned statuses survive containment. The [reconciliation](reconciliation.md#reconciliation) correctly retains valid containers rather than replacing them merely because finer parts exist.

The repair supersession is justified: both declarations identify the same retrieval-family mechanism, target, projection classes, summary selection and persistent effect. Capture-plus-replay is instead a valid container over separate capture and replay routes. The broader source-asset, document and evaluation objects are not identical to their narrower or request-local overlaps. Instruction and evolving-evidence authority paths remain distinct. No evidenced-absence records are declared. All declared route operation statuses remain uninspected; none silently promotes implementation, an example fixture or source-authored advice to an observed result. No unresolved cross-report contradiction or missing conflict disposition was found. The reconciliation's read-only, ordering, approval and freshness qualifications preserve the reports' actual differences in scope rather than selecting stronger statuses.

### Consequential omission questions and stopping decision

The frozen tree, shipped skill action index, retrieval dispatch and producer/consumer dependencies guided omission checks beyond the listed evidence passages. Three questions mattered:

1. Could a shipped alternate entry point invalidate the approval or no-write account? Retrieval-family repair and opt-in capture were traced independently, including writable opening/locking; adapter caching and storage initialization were checked separately. Their dispositions are already present in the records. No universal no-write or human-authenticated gate is emitted.
2. Could another maintenance surface turn the bounded account into a materially false passive-storage or no-transformation characterization? The reports already positively establish compilation, repair and candidate construction. Additional inspection of SRC-1 `internal/runner/graph_relationship_maintenance_plan.go` confirms another candidate-content surface, with a separately executed document request rather than automatic adoption. Its omission from individual records limits the inventory, not those positive conclusions.

> CandidateSectionContent:   content,
> NextReplaceSectionRequest: nextReplace,
> NextAppendDocumentRequest: nextAppend,
> WriteStatus:               "planned_no_write",
> --- `internal/runner/graph_relationship_maintenance_plan.go`

3. Could storage history be mistaken for absent retention or automatic host-context recovery? Inspection of SRC-1 `internal/runner/git_lifecycle_report.go` confirms explicitly enabled, caller-path-scoped Git checkpoint creation. The reports already name Git lifecycle as incompletely inspected and withhold complete recovery/history conclusions. This does not establish an automatic compaction or semantic restoration chain.

> if !gitLifecycleCheckpointsEnabled(config) {
>     return GitLifecycleReport{
>         CheckpointStatus: "disabled",
>         WriteStatus:      "rejected",
>     }, nil
> }
> --- `internal/runner/git_lifecycle_report.go`

Further optional expansion stopped because these selected challenges have supported dispositions, and the records do not claim exhaustive maintenance coverage, global absence of adaptation, observed instruction compliance or causal improvement. More report converters, demo details, release machinery and bundled result analyses could add inventory detail, but no identified challenge remains that would invalidate the emitted bounded conclusions. Their uninspected behavior is not evidenced absence.

## Blockers

none

## Limits

- The route inventory remains partial for relationship-maintenance candidate construction and Git storage history. The coverage limits beside [MEM-RTE-projection-read](memory.md#mem-rte-projection-read), [MEM-RTE-document-move](memory.md#mem-rte-document-move), [RT-RTE-document-write](runtime.md#rt-rte-document-write) and the [epistemic bounded conclusion](epistemic.md#bounded-conclusion) must be preserved: additional source inspection above confirms a relationship-section proposal with serialized write requests and explicitly enabled Git checkpoints, but the analyst records do not individually characterize their full selection, persistence and later-consumer chains. Readers can rely on the recorded request-driven retrieval, candidate planning, compilation and source-sensitive repair mechanisms. They should withhold exhaustive route comparisons, complete version-recovery claims and system-wide negatives about maintenance or adaptation.
