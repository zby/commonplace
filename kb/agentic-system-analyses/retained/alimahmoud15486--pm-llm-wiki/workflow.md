---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "pm-llm-wiki workflow: competitor-source ingestion, held approval, PRD delivery and later file-back in the fictional FitLoop pilot."
run-id: AAS-2026-11-09-pm-llm-wiki-4c3839e25928-01
reviewed-boundary: "64fb748ac9d187be4c51636aa56bfee1d9e5b116"
---

# pm-llm-wiki workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is the FitLoop pilot's July 2–3 competitor-intel ingest and Adaptive Plans PRD request, ending in a filed draft and refreshed catalog. It was selected because the journal explicitly connects new evidence, a reversal-condition check, two pending proposals, an intervening query, rejected second-hand approval, direct PM approval and durable file-back. This is one documented sequence, not an inferred orchestration assembled from unrelated capabilities. The reusable instructions explain its intended transitions; the fictional journal and retained pages illustrate the result (SRC-1, `template/SCHEMA.md`, `pilot/log.md`, `pilot/index.md`, `pilot/wiki/prd-adaptive-plans-v1.md`).

The [boundary](boundary.md) is doc-grounded. The journal supplies **reported operation**, while the schema supplies **doctrine/design**. Neither is a raw agent transcript. Dates, pending states and retained files support the account of the shipped example, not observed tool execution, authenticated PM approval, reliable model compliance or real-product success. The workflow reuses [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade) and [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback); it does not introduce duplicate route identities.

### 1. PM supplies the task; the agent interprets the source

The general entry contract makes the PM the source curator and task principal and the external agent the filing/synthesis executor. The operative instructions are [RT-OBJ-schema](runtime.md#rt-obj-schema), consumed through [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent). A source handoff supplies a local immutable file, the product context, the catalog and existing wiki state. The schema instructs the agent to read the catalog first, read the source, return 3–5 takeaways and evaluate effects on problems, assumptions, decisions and questions. These are model-interpreted instructions, not executable stage transitions ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `template/SCHEMA.md`).

For this episode, the supplied evidence is the fictional July 2 GymJoy launch note. It says Coach launched July 1 at €9.99 in Premium, but lacks progression logic; it also gives an August 1 end date for the €5.99 base-tier promotion. The note itself labels its provenance as fictional, so the workflow can demonstrate source handling but cannot establish actual competitor facts (SRC-1, `pilot/sources/2026-07-02_intel_gymjoy-coach-launch.md`).

> No progression logic —
> suggested weights/reps do not respond to performance.
> --- `pilot/sources/2026-07-02_intel_gymjoy-coach-launch.md`

### 2. Ingest separates new information from authorization to change a decision

The journal reports that the agent checked the active Q3 decision, answered Q4, opened Q6/Q7, updated problem pages and overview, and proposed the competitor entity upgrade and A4 evidence additions. Thus the immediate result is not merely a summary: it includes maintained state and proposals with different admission requirements (SRC-1, `pilot/log.md`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

The consequential check is conjunctive. The decision requires an early **and demonstrably strong** GymJoy release before that reversal condition is met. The source describes an early but shallow launch, and the journal explicitly records the condition as not triggered. Arrival of new evidence therefore does not itself authorize reversal. Even a triggered condition would produce an open question under the schema rather than permit the agent to reopen the decision itself (SRC-1, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`, `pilot/log.md`, `template/SCHEMA.md`; [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)).

> - GymJoy Coach ships early AND demonstrably strong, making fast-follow pointless and
>   differentiation-elsewhere (e.g. social) more attractive.
> --- `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`

This is evidence-relative model judgment, not an expected-answer oracle or verified test. The PM retains decision authority. The inspected materials do not show a software evaluator checking whether “strong” was interpreted correctly.

### 3. Protected proposals stop at the PM boundary

The second competitor-intel ingest meets the schema's predeclared Stage-2 trigger. The agent may propose a competitor entity, but changing the governing schema requires a direct PM reply before writing. The journal marks both that upgrade and A4 evidence additions pending. Its more conservative treatment of status-unchanged A4 evidence must not be generalized into a universal approval requirement: the detailed schema gate expressly allows that category of addition, while its final blanket prohibition is broader. The runtime baseline retains this tension ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `template/SCHEMA.md`, `pilot/log.md`).

The rejection path is actually documented: a coordinator relays approval, but the proposals remain pending. The coordinator is not established as a spawned worker, and there is no shipped inter-agent scheduling or context-transfer implementation. What the journal establishes is a reported message and a prescribed refusal to treat it as authorization ([RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade)). The rejection preserves the pending state instead of treating relayed information as equivalent to the PM's direct reply. This is a policy-strength gate owned by the interpreting agent, not a host-enforced identity check.

### 4. The query returns a useful draft without admitting the pending edits

While proposals are pending, a PM-requested PRD is drafted for Dana and Omar's Q3 kickoff. The query handoff supplies an audience and deliverable request; the query policy supplies index-first reading, relevant-page selection and evidence-chain synthesis. The journal says the draft drew from problem, decision and assumption pages plus raw sources and was delivered in-message, with a file-back offer. Pending schema approval is therefore not reported as blocking an otherwise authorized query ([RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback); SRC-1, `pilot/log.md`, `template/SCHEMA.md`).

Verification here is chiefly an authoring obligation: trace factual claims to sources, flag unsupported claims, and distinguish inference from evidence. The PRD retains A2's correlational limitation and proposes a holdout rollout rather than asserting causality. It also explicitly labels its timing inference. Such markings show inspectable qualification in the shipped artifact, not that every claim or inference passed independent review ([RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control); SRC-1, `pilot/wiki/prd-adaptive-plans-v1.md`).

> To fit two cohort cycles of measurement before the end-Q4 churn gate, ship by ~mid-Q3
> [inference from the measurement window — not sourced].
> --- `pilot/wiki/prd-adaptive-plans-v1.md`

The immediate delivery boundary is the PM's conversation. Dana and Omar are named intended readers, not observed recipients. Nothing supplied shows product implementation, rollout results or their acceptance of the draft. Selection through the catalog limits requested reading, but the external host's actual context composition, compaction and isolation remain uninspected; no subagent frame is established.

### 5. Direct approval resumes writes; file-back completes the retained result

The July 3 journal reports direct PM approval, followed by the competitor specification being added to the instruction file, creation of the competitor page, A4/A1 evidence updates, PRD file-back and catalog changes. The final PRD and index corroborate the existence and discoverability of the filed artifact. They do not authenticate the approval conversation or prove an atomic write sequence (SRC-1, `pilot/log.md`, `pilot/index.md`, `pilot/wiki/prd-adaptive-plans-v1.md`).

> - PRD one-pager (Adaptive Plans v1) filed back as `wiki/prd-adaptive-plans-v1.md` per the query
>   workflow file-back offer. Index updated (new Competitors + Explorations sections).
> --- `pilot/log.md`

Delivery consequently has two endpoints: an in-message draft first, then a retained exploration cataloged for later index-first retrieval. The file remains `draft-v0.1`; filing is not promotion to an approved product decision. The page's new competitor link is visible in final state, but without intermediate snapshots one cannot establish when that link entered the draft. No later invocation consuming this PRD is supplied ([RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)).

Recovery in the supported rejection case is human-controlled resumption: hold the proposal, preserve its pending journal state, wait for the correct reply, then apply the admitted edit. Protected changes can be vetoed by withholding approval. Existing decisions remain retained and are superseded rather than erased. Tool-error retries, crash recovery, locking and transactional rollback are not established within this prompt-and-Markdown boundary. Optional external Git cannot be treated as an automatic recovery implementation ([RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

### Inspection coverage

Direct source inspection for this account covered SRC-1 at the frozen revision: `template/SCHEMA.md`, `pilot/log.md`, `pilot/index.md`, `pilot/sources/2026-07-02_intel_gymjoy-coach-launch.md`, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md` and `pilot/wiki/prd-adaptive-plans-v1.md`. These paths were already inside the registered coverage. No source, implementation layer, execution trace or experiment was added. The selected sequence establishes a coherent prescribed and fictionally reported workflow, with a bounded approval-rejection path; it does not establish measured reliability or successful downstream product delivery.

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

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow role: supplies maintained product context to the intervening PRD query while distinguishing a non-triggered reversal from a pending approval. The selected episode does not require all ingest effects to wait for approval; only the held proposals are reported pending.

#### On [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade)

Workflow role: the documented rejection/resumption checkpoint. A coordinator relay does not advance the pending proposal; the reported direct PM reply resumes schema and entity writes. This is not evidence of a delegated-worker runtime or host-authenticated authorization.

#### On [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)

Workflow role: delivery is split between the July 2 in-message draft and July 3 durable exploration/catalog entry. Neither endpoint establishes downstream reader acceptance, product execution or a subsequent agent's use of the filed PRD.
