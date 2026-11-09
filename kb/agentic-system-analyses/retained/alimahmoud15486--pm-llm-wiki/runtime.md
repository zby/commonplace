---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "pm-llm-wiki runtime baseline: prompt-directed ingestion, query/file-back, lint and PM-approved schema progression at the frozen revision."
run-id: AAS-2026-11-09-pm-llm-wiki-4c3839e25928-01
reviewed-boundary: "64fb748ac9d187be4c51636aa56bfee1d9e5b116"
---

# pm-llm-wiki runtime report

## Runtime account

### Boundary and entry

pm-llm-wiki ships instructions and Markdown state, not an executing agent host. Its consequential work is to turn PM-curated evidence into maintained product knowledge, then reuse that knowledge in answers and deliverables. The external coding agent performs interpretation and file I/O; the PM supplies sources, requests work and controls specified changes. This is a doc-grounded account at the [boundary](boundary.md). SRC-1 supplies doctrine/design and reported operation, not a raw execution trace or experiment. The fictional pilot illustrates requested behavior and reported steps; it does not demonstrate reliable compliance, activation in an actual agent session or benefit.

The shipped ordinary entry is: copy `template/SCHEMA.md` into a product folder as `CLAUDE.md`, add product context, create index/log and source/wiki directories, place a named source, and ask the agent to read the instructions and ingest it. Codex-style use renames the instruction file to `AGENTS.md`; query and weekly lint are separate PM requests. No repository CLI dispatches these operations (SRC-1, `README.md`, `template/SCHEMA.md`).

> **An agentic LLM tool that can read/write local files.** Claude Code is the reference tooling;
>   OpenAI Codex or similar coding agents work too (rename `CLAUDE.md` to `AGENTS.md`).
> --- `README.md`

> Read CLAUDE.md. Then ingest sources/2026-07-03_interview_jane.md.
> --- `README.md`

The model-backed component is [RT-CMP-llm-agent](#rt-cmp-llm-agent); its prompt authority enters through [RT-BAP-schema-agent](#rt-bap-schema-agent). The actual instruction-loading policy, provider, context window, tool permissions, shell access, approval machinery and isolation envelope belong to the unspecified external host. File access is a required capability, not evidence of a particular grant set or sandbox. Optional Git history and Obsidian are user tooling, not necessary orchestration components (SRC-1, `README.md`).

### Ordinary invocation and material routes

An ordinary ingest, [RT-RTE-source-ingest](#rt-rte-source-ingest), starts when the PM places/selects a source. The agent reads the catalog and source, returns 3–5 takeaways, updates problem evidence and mention counts, checks assumptions and decision reversal conditions, queues questions, refreshes the overview when warranted, and updates index/log. The next-step policy is natural-language instruction interpreted by the model, not a programmatic transition system. Durable state is the local Markdown wiki; transient conversation and tool results are external-host state. The PM becomes next-step owner when a gated edit needs approval; otherwise the agent is instructed to continue filing. A source with no consequential change takes the log-only skip branch. High-volume exports take a distinct source-admission path: draft a digest and obtain PM approval, or consume a PM-provided digest, rather than ingest a raw dump (SRC-1, `template/SCHEMA.md`).

[RT-RTE-query-fileback](#rt-rte-query-fileback) selects pages through `index.md`, synthesizes a cited answer and offers durable file-back. Its immediate output may remain only in the conversation. [RT-RTE-wiki-lint](#rt-rte-wiki-lint) is a PM-triggered weekly review, not a shipped scheduled process; it sends findings to open questions or approval proposals. [RT-RTE-stage-upgrade](#rt-rte-stage-upgrade) changes the governing instructions and available entity structure after a need trigger and PM approval. These routes have different admission endpoints even though the same external agent executes them (SRC-1, `template/SCHEMA.md`, `pilot/log.md`).

### Guarantees and forcing cases

The source claims evidence traceability and PM control, but explicitly locates their enforcement in the agent's conduct:

> These five rules are what separate this from "AI notes." They're encoded in the schema; the
> agent enforces them on itself.
> --- `README.md`

The guarantee owner is the PM for approval decisions and the external agent for recognizing protected edits, waiting and performing compliant I/O. The enforcement point supplied by this repository is the schema instruction before a write, not a filesystem permission check or verified authorization token. Guarantee strength: **policy**. Design conclusion status: **claimed**. Operation conclusion status: **uninspected**. External contract: the host must deliver the instructions and conversation, and the model must correctly interpret edit categories, speaker identity and evidence requirements. There is no basis here for calling these controls an invariant or deployment guarantee (SRC-1, `template/SCHEMA.md`, `README.md`).

Three forcing cases delimit that policy:

1. **Relayed approval versus direct PM reply.** A meeting note or coordinator message saying approval was given is explicitly insufficient. The pilot journal says a coordinator relayed approval, both proposals remained pending, then direct PM approval was applied the next day. This is reported operation consistent with the policy, not an authenticated conversation or proof that a host verifies the PM's identity (SRC-1, `template/SCHEMA.md`, `pilot/log.md`; [RT-RTE-stage-upgrade](#rt-rte-stage-upgrade)).
2. **Unchanged assumption status.** The specific write-gate clause permits adding evidence to existing assumptions without a status change, while its final blanket prohibition says not to write to Assumptions without approval. A universal claim that *every* assumption edit requires PM approval would ignore the explicit exception. The pilot sought approval for A4's status-unchanged additions anyway; it demonstrates a conservative example, not removal of the exception. New assumption registration is not explicitly classified by the detailed gate; the pilot reports approvals for A1/A2 and other registrations. Approval treatment of a new entry must not be inferred from the status-change rule alone (SRC-1, `template/SCHEMA.md`, `pilot/log.md`, `pilot/wiki/assumptions.md`).
3. **Query without persistence and evidence without reopening.** A deliverable can return in-message before file-back; it is not automatically a new source or an admitted decision. Likewise a competitor launch does not by itself meet a reversal condition requiring an early **and demonstrably strong** launch. The pilot describes Coach as shallow, records the reversal as not triggered, and leaves the decision active. Neither selected evidence nor a generated proposal automatically reopens the roadmap decision (SRC-1, `pilot/log.md`, `pilot/sources/2026-07-02_intel_gymjoy-coach-launch.md`, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`).

The covered paths are compliant ingest, query/file-back, lint and progression through the loaded schema. Alternate physical paths include PM/manual file edits, an external agent with direct write tools, and repository contribution PRs. The repository does not mediate those through executable controls. Provider-native tools, shell callbacks, delegated workers and concurrent editors cannot be exhaustively traced because no external host implementation is frozen; their availability is not a demonstrated bypass. The coordinator mentioned in the journal establishes a reported relayed message, not a shipped delegation runtime. Atomic writes, locking, crash recovery and tool-error retries are likewise not established. Logical recovery is specified through pending proposals, preserved decisions and supersession; Git is optional, not an automatic rollback mechanism (SRC-1, `README.md`, `template/SCHEMA.md`, `pilot/log.md`, `CONTRIBUTING.md`).

Evidence chains, immutable sources, append-only logs and retained decisions are also agent policies. Their scope includes generated deliverables, but a citation requirement is not verification of source truth or inference validity. Reversal checks and contradiction handling prescribe questions rather than automatic resolution. Later analysts can rely on the existence and contents of those instructions, not on guaranteed compliance ([RT-CLM-evidence-control](#rt-clm-evidence-control)).

### Coverage and evidential limits

Runtime inspection used SRC-1 at the frozen commit: `README.md`, `template/SCHEMA.md`, `pilot/CLAUDE.md`, `pilot/log.md`, `pilot/index.md`, `pilot/sources/2026-07-02_intel_gymjoy-coach-launch.md`, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`, `pilot/wiki/assumptions.md`, `pilot/wiki/prd-adaptive-plans-v1.md`, and `CONTRIBUTING.md`. These supply doctrine/design; the journal and PRD preamble also supply reported operation. The tracked-tree listing corroborates the prompt-and-Markdown packaging already established by the boundary. No new source or execution evidence was added. Runtime scheduling, model activation and benefits remain unobserved. Memory revisions and the detailed epistemic treatment of individual product assumptions remain the specialists' work.

## Shared records

### Components

#### RT-CMP-llm-agent
Label: External LLM agent

Source-native identity: the agentic LLM tool named in SRC-1, `README.md`, and addressed by `template/SCHEMA.md`. Natural-language instruction interpretation is performed by an external distributed-parametric model; file operations are supplied by its host. Parameters and provider storage are outside the repository. Whether parameters change during operation is uninspected; no exact model version is pinned, and endpoint mutability/resolution to another model is uninspected because no endpoint is specified. The explicit allowance for different coding agents precludes attributing one fixed model to this system. No embedding or vector-store component is required by the shipped setup.

> **A folder.** That's the whole infrastructure. No database, no vector store, no plugin.
> --- `README.md`

### Operative objects

#### RT-OBJ-schema
Label: Maintainer schema

Source-native identity: `template/SCHEMA.md`, copied to `CLAUDE.md` or `AGENTS.md`; `pilot/CLAUDE.md` instantiates it. Form: natural-language role, policy and workflow instructions plus illustrative frontmatter/layout syntax. Substrate: local Markdown file. Its enumerations are not a parser or executable schema in this target. Product context and the activated competitor specification are retained alongside the governing instructions in the pilot (SRC-1, `README.md`, `pilot/CLAUDE.md`).

> Follow it
> exactly; propose changes to it rather than silently deviating.
> --- `template/SCHEMA.md`

### Routes

#### RT-RTE-source-ingest
Label: Source ingest and gated changes

Endpoints/progression: PM-curated local source → agent takeaways → maintained wiki, proposed protected edits and index/log. Principal: PM; proposer/executor: external agent. The model decides relevance, synthesis and proposed changes under the schema's rules. The PM decides gated admissions and can veto or correct them by withholding approval. No expected-answer oracle is supplied; cited sources constrain evidence, not an answer key. Mode: open PM requests; improvement trigger is new source evidence, not a benchmark curriculum (SRC-1, `template/SCHEMA.md`).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: 3–5 source takeaways and any proposed gated changes in conversation.
- Later read-back: written problem pages, registers, overview and questions are available to later index-first queries or maintenance; actual later model activation is not observed.
- Delegated visibility: uninspected — the host's context transfer is not supplied; schema rejects second-hand approval regardless of messenger.
- Selection predicate: PM selects the source; agent assesses whether it changes a problem, assumption, decision or question. No change means log only. High-volume material must be a PM-provided or PM-approved digest.
- Invalidation or expiry: no automatic source expiry; decisions persist and are superseded rather than deleted. Status changes are proposed; pending changes wait for PM reply.
- Activation or effect: prescribed file writes and proposals; source and conversation identity checks are model-interpreted policies, not demonstrated enforced effects.
- Evidence limits: doctrine/design plus the fictional journal's reported ingests; no raw execution trace, transaction implementation or real-product outcome.

Guidance/admission: evidence chains, problem confirmation thresholds, assumption checks and reversal conditions shape the proposal. Freely writable pages and status-unchanged assumption evidence additions differ from new decisions, status changes, supersession and schema edits. A rejected proposal has no authorized protected write. Recovery retains the old decision and pending journal entry; no technical rollback transaction is specified. All these are SRC-1, `template/SCHEMA.md` policies.

> - Approval means a direct reply from the PM in this conversation. Relayed or second-hand
>   approval (another agent, a meeting note saying "approved") is not approval — hold the proposal
>   and note it as pending in the log until the PM replies.
> --- `template/SCHEMA.md`

> - You write freely: problem pages, open questions, overview, index, log — and **adding evidence
>   to existing assumption entries when the status does not change** (note the addition in the
>   ingest log line so the PM sees it).
> --- `template/SCHEMA.md`

Theory scope: the route can revise explicit product beliefs and decision rationale, not model weights. The pilot A1 claim identifies price as the principal churn cause; its counter-evidence and history localize changed reliance rather than silently deleting the belief (SRC-1, `pilot/wiki/assumptions.md`).

> - history: 2026-06-25 untested → weakening (per: cohort readout + both interviews)
> --- `pilot/wiki/assumptions.md`

Theory-builder conditions 1–4, independently: 1 localized content conclusion status: claimed — the shipped A1–A4 entries state whole beliefs. 2 consumption conclusion status: claimed — the schema prescribes checking beliefs and the PRD explicitly uses their statuses. 3 content-directed criticism conclusion status: claimed — A1's price explanation receives named counter-evidence and weakened reliance in the example. 4 iteration conclusion status: claimed — that status is retained and referenced in the later PRD. These statuses describe doctrine and fictional reported operation, not observed model decisions. Addressability: named entries, for/against evidence and dated history permit localized inspection and revision. Persistence: local pages span the illustrated operations and can span sessions. Learning: uninspected — no improved future capacity or attribution evidence. Reflection: uninspected — product-belief revision is not evidence of a representation of the wiki's own operation. Reflective theory builder: uninspected for this route. Autonomous theory builder: inapplicable — protected internal belief-status admissions deliberately require PM decisions. No exercised self-improvement is established by these product-state writes.

#### RT-RTE-query-fileback
Label: Query and optional file-back

Endpoints/progression: PM question → index → relevant wiki pages/source evidence → cited answer → offered retained exploration. Agent selects and synthesizes; PM requests the work and, in the pilot, confirms file-back. No general per-answer approval gate is stated for all exploration writes; the pilot's confirmation should not be generalized to every query. Operating mode is open requests; no answer oracle, scoring selector or benchmark is supplied (SRC-1, `template/SCHEMA.md`, `pilot/log.md`).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: source-chained answer or deliverable in-message; persistence is optional.
- Later read-back: if filed, the answer becomes a wiki page listed in the index; pilot PRD is cataloged as an exploration. No later agent read of that PRD is supplied.
- Delegated visibility: uninspected — no shipped worker/context-transfer implementation; the pilot names Dana and Omar as intended readers, not observed consumers.
- Selection predicate: read index first, then only pages judged relevant to the question; pilot PRD also reports use of raw sources.
- Invalidation or expiry: no automatic expiry; page dates and later lint provide review cues. No special generated-answer revocation mechanism is specified.
- Activation or effect: prescribed synthesis, optional durable page, index update and exploration log; proposed product features are not executed by this route.
- Evidence limits: instructions and fictional PRD/journal; delivery and filing do not prove source correctness, actual decision influence or improved PM outcomes.

> - Drafted from problem/decision/assumption pages + raw sources; delivered to PM in-message,
>   evidence-chained per schema. Not yet filed as a wiki page — offered to file as `exploration`
>   on PM confirmation.
> --- `pilot/log.md`

Admission trigger is a valuable answer; guidance is evidence chaining, with unsupported claims marked. Agent authors; pilot PM confirms filing; protected changes embedded in an answer would still fall under the schema's write gate. Rejection leaves the in-message answer unfiled. Recovery/rollback beyond ordinary editing and optional Git is unspecified (SRC-1, `template/SCHEMA.md`, `README.md`). The selection rule reduces requested reading by catalog/page relevance; it is not host context compaction, isolation or deterministic retrieval. No prescribed trimming of accumulated turns, automatic summary or eviction policy is supplied by these files.

The PRD derives a rollout proposal under A2's stated causal uncertainty; this is not itself criticism revising A2. Theory-builder conditions 1–4: 1 localized content conclusion status: claimed — explicit assumptions and scope are present; 2 consumption conclusion status: claimed — rollout text depends on A2; 3 content-directed criticism conclusion status: uninspected — no revision outcome caused by this PRD is supplied; 4 iteration conclusion status: uninspected — no subsequent round consuming PRD criticism is supplied. Addressability: explicit goals, scope, risks and source-linked assumptions. Persistence: filed Markdown across potential sessions. Learning and reflection conclusion status: uninspected — no outcome comparison or self-representation feedback loop is supplied. Reflective and autonomous theory builder conclusion status: uninspected — a generated plan and retained page do not establish either property.

> Holdout-controlled rollout, not a full launch: adaptivity→retention is validated only
> correlationally (swap-feature users retain 2.3×, self-selected — A2), so the rollout doubles as
> the Q1 causality experiment (source: 2026-06-25_analytics_cohort-retention-readout.md;
> [Q1](open-questions.md)).
> --- `pilot/wiki/prd-adaptive-plans-v1.md`

#### RT-RTE-wiki-lint
Label: Weekly product truth check

Endpoints/progression: PM weekly request → agent page/evidence review → findings → questions or proposed assumption changes → operation journal. The agent diagnoses; PM triages discovery and approves protected status changes. Sources and reversal thresholds are reference criteria, not a general expected-answer oracle. Operating mode: open maintenance review. Triggers include counter-evidence, contradictions, stale pages, orphan links, unaddressed rising problems and evidence gaps (SRC-1, `template/SCHEMA.md`, `README.md`).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: lint findings and proposals.
- Later read-back: questions and any approved register changes persist for later discovery-plan queries and review.
- Delegated visibility: uninspected — no separate lint worker or context boundary is specified.
- Selection predicate: sweep relevant wiki evidence, including each active decision's reversal conditions and pages over 30 days untouched in an active area.
- Invalidation or expiry: stale-page finding requests review, not deletion. A triggered reversal produces a question, not automatic reopening.
- Activation or effect: prescribed question writes and gated proposals; pilot journal reports Q2/Q5 creation and no triggered reversal.
- Evidence limits: fictional journal reports a lint pass, not a reproducible evaluator run or proof of complete detection.

> Rules: decision pages are NEVER deleted or rewritten after the fact. New decision on the same
> question → new page, old page gets `status: superseded` and a `superseded-by:` link. During lint,
> check each active decision's reversal conditions against new evidence — if one has triggered,
> add an open question; do not reopen the decision yourself.
> --- `template/SCHEMA.md`

Admission/recovery: open questions are freely writable; assumption status changes remain proposals the PM can reject. Old decisions persist. The route's guidance is the lint checklist and existing claims/reversal conditions. Theory-builder conditions 1–4: 1 localized content conclusion status: claimed — explicit decision rationale and assumptions are review targets; 2 consumption conclusion status: claimed — review is instructed to depend on those contents; 3 content-directed criticism conclusion status: claimed — the protocol directs named counter-evidence into questions or status proposals, without proving a revision occurred; 4 iteration conclusion status: claimed — persistent queue/status outputs are designated inputs to later discovery. Actual performed criticism and later activation remain uninspected. Addressability: individual assumptions and decision conditions are inspectable; persistence: wiki across sessions. Learning, reflection, reflective theory builder and autonomous theory builder conclusion status: uninspected — a checklist and reported questions establish neither improved capacity, a self-model feedback loop nor completion of every theory-building role by computation.

#### RT-RTE-stage-upgrade
Label: Triggered schema progression

Endpoints/progression: observed need threshold → agent proposal → direct PM approval → schema/entity addition and log. Pilot trigger: second competitor-intel ingest; retained result: competitor specification in `pilot/CLAUDE.md`, competitor page and index section. Agent proposes and performs I/O; PM decides and can veto. Mode: need-driven open maintenance, not experimental candidate selection; no answer oracle is supplied (SRC-1, `template/SCHEMA.md`, `pilot/CLAUDE.md`, `pilot/log.md`).

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: upgrade proposal; pending status until direct PM confirmation.
- Later read-back: changed schema is intended to govern subsequent maintenance; index exposes the competitor page. No post-upgrade agent session trace is supplied.
- Delegated visibility: relayed approval is disallowed; pilot journal reports coordinator relay held pending, not an implementation of delegated identity verification.
- Selection predicate: Stage-2 entity-specific pressure, or Stage-3 scale/ritual maturity; pilot competitor threshold is second intel ingest.
- Invalidation or expiry: no automatic expiry or downgrade; further schema edits require approval. No built-in rollback is described.
- Activation or effect: prescribed expansion of instructions and filing structure; pilot retained files display the addition, not observed later compliance.
- Evidence limits: fictional recorded approval and instantiated text; automated tooling remains a proposed later stage, not installed machinery.

> Stage upgrades are triggered by observed pressure, not ambition. When a trigger fires, tell the
> PM and propose the upgrade; on approval, update this schema file and log the change.
> --- `template/SCHEMA.md`

> - Note: coordinator relayed approval for the two pending proposals; per session rules that is
>   not PM confirmation — both remain PENDING PM APPROVAL.
> --- `pilot/log.md`

Guidance: minimal stages and need thresholds shape expansion; schema and operation record persist. Rejection withholds the edit; technical rollback is unspecified. Repository-level product change follows a different admission context: contributions by PR, honesty-rule constraints and manual fresh-agent testing. `CONTRIBUTING.md` asks contributors to report observations but supplies no automated selection gate or test result.

This route revises operating instructions, but addition of an entity upon its predeclared trigger is not demonstrated criticism of a theory. Theory-builder conditions 1–4: 1 localized content conclusion status: claimed — schema has inspectable workflow units; 2 consumption conclusion status: claimed — maintenance is instructed to follow them; 3 content-directed criticism conclusion status: uninspected — pilot upgrade does not identify and blame a failed methodological claim; 4 iteration conclusion status: uninspected — no subsequent round shaped by such criticism is supplied. Addressability: named schema sections can be proposed for editing. Persistence: schema and log across sessions. Learning conclusion status: uninspected — no comparative capacity evidence. Reflection conclusion status: claimed — the progression plan represents the system's entity/tool stage, need pressure can change that representation, and the changed schema is intended to govern later behavior; exercised feedback is unobserved. Reflective theory builder conclusion status: uninspected — methodological criticism against operation records is not established. Autonomous theory builder: inapplicable — schema admission deliberately belongs to the PM. A dormant authority path for changed instructions is present in the design, but exercised self-improvement is not established: later operation causally dependent on the upgrade and objective-responsive improvement evidence are not supplied.

### Claims

#### RT-CLM-evidence-control
Label: Evidence-chain policy

Claimed operation: every factual wiki/deliverable claim is source-traceable or flagged unsupported; sources remain unedited. Owner and enforcement point: external agent interpreting the schema before writing. Guarantee strength: policy. Covered paths: ingest and query/file-back, with lint supporting review; no proof covers arbitrary external writes. Design conclusion status: claimed. Operation conclusion status: uninspected. Source: SRC-1, `template/SCHEMA.md`; README rhetoric is not measured reliability.

> Every factual claim on any wiki page cites its source inline: `(source: <filename>)`. Verbatim
> user quotes stay verbatim, in quotation marks, attributed. A claim you cannot chain to a source
> is labeled `[unsupported]` — never silently asserted. Generated deliverables (PRDs, briefs)
> inherit this rule: every claim traceable or flagged.
> --- `template/SCHEMA.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-schema-agent
Label: Schema to maintainer behavior

Consumer: external coding agent/model. Channel: local `CLAUDE.md`/`AGENTS.md` read in the task context. Force: natural-language operating policy, not executable authorization. Horizon: current task when read, and later tasks if reloaded. It prescribes selection, filing, approvals and changes to its own instruction file. Host instruction priority and actual compliance remain uninspected. Its object is [RT-OBJ-schema](#rt-obj-schema); admission of changed contents is [RT-RTE-stage-upgrade](#rt-rte-stage-upgrade). SRC-1, `README.md`, `template/SCHEMA.md`.

> **Step 2 — Add product context** at the top of `CLAUDE.md`: what the product is, the current
> top-level goal, who the key people are. Five lines is enough — see the
> [pilot's version](pilot/CLAUDE.md) for the shape.
> --- `README.md`

## Annotations

none
