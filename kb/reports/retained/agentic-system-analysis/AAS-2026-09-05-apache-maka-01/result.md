---
type: kb/types/agentic-system-analysis-result.md
description: "Apache Maka runtime and built-in memory routes at one frozen commit, distinguishing durable extraction from agent read-back"
run-id: AAS-2026-09-05-apache-maka-01
system: "Apache Maka (Incubating)"
run-date: "2026-09-05"
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "ece69ab3e7a1629a6073831005711d8aa7160ca4"
analysis-cutoff: "2026-09-05"
evidence-tier: code-grounded
memory-comparison:
  scope: "Built-in retained RuntimeEvents and compaction checkpoints, local MEMORY.md/PENDING.md, atomic MemoryItems and their keys/provenance/extraction bookkeeping. Excludes goal/skill control material, offloaded tool artifacts, arbitrary project files, external extensions and transient replay arrays."
  axes:
    storage_substrate:
      assessment: "known"
      basis: "wired"
      values: ["files", "sqlite"]
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4"]
      note: "Retained core memory and its access metadata use the file bundle and SQLite; transient replay arrays are excluded."
    representational_form:
      assessment: "not-determinable"
      basis: null
      values: []
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4"]
      note: "Natural-language and symbolic parts are established, but opaque provider checkpoint content prevents a complete set."
    lineage:
      assessment: "not-determinable"
      basis: null
      values: []
      records: ["OBJ-2", "OBJ-3", "OBJ-4"]
      note: "Authored entries and trace-derived transformations are established per route; opaque state and replacement/import provenance prevent a complete controlled set."
    behavioral_authority:
      assessment: "known"
      basis: "wired"
      values: ["knowledge", "validation", "routing", "enforcement"]
      records: ["BAP-2", "BAP-3", "BAP-4"]
      note: "Knowledge is advisory prompt consumption; checkpoint access metadata validates/routes replay, and extraction bookkeeping enforces writes. Atomic item content has no wired task-model consumer."
    write_agency:
      assessment: "known"
      basis: "wired"
      values: ["automatic", "manual"]
      records: ["RTE-7", "RTE-9", "RTE-12"]
      note: "Manual file-bundle operations coexist with automatic extraction and checkpoint generation, including human-triggered automatic transformations."
    curation_operations:
      assessment: "uninspected"
      basis: null
      values: []
      records: ["RTE-7", "RTE-11", "RTE-12"]
      note: "Approval, lifecycle withdrawal and summary replacement are described, but the complete controlled set across maintenance seams was not assessed."
    read_back_direction:
      assessment: "known"
      basis: "afforded"
      values: ["pull", "push"]
      records: ["RTE-8", "RTE-11", "RTE-13", "ABS-1"]
      note: "Local-memory and history/checkpoint push are wired. Atomic key/ID pull exists only as storage API affordance, without a production model caller; union retains the weaker basis."
    read_back_signal:
      assessment: "known"
      basis: "wired"
      values: ["coarse", "identifier"]
      records: ["RTE-8", "RTE-13"]
      note: "Wired push selects active entries by policy/session and checkpoints by session/coverage; no inferred relevance selection is asserted."
    trace_learning:
      assessment: "known"
      basis: "wired"
      values: ["yes"]
      records: ["RTE-12", "RTE-13"]
      note: "Automatic text checkpoints distill accumulated conversation for later task continuation; this does not establish cross-task use of atomic items or improved performance."
    trace_source:
      assessment: "known"
      basis: "wired"
      values: ["event-streams"]
      records: ["OBJ-1", "RTE-12"]
      note: "The established learning route consumes RuntimeEvent projections, including model/user/tool events, as one event-stream source."
    learning_scope:
      assessment: "known"
      basis: "wired"
      values: ["per-task"]
      records: ["RTE-12", "RTE-13"]
      note: "Session-bounded checkpoint continuation maps to per-task; no cross-task learned readback is established for atomic items."
    learning_timing:
      assessment: "known"
      basis: "wired"
      values: ["online"]
      records: ["RTE-12", "RTE-13"]
      note: "Checkpoint transformation occurs while continuing the task; later extraction retention alone adds no established learning loop."
    distilled_form:
      assessment: "not-determinable"
      basis: null
      values: []
      records: ["OBJ-4", "RTE-12", "RTE-13"]
      note: "Text checkpoints distill natural-language summaries; opaque provider compaction content prevents a complete form classification."
    faithfulness_tested:
      assessment: "uninspected"
      basis: null
      values: []
      records: ["RTE-8", "RTE-12", "RTE-13"]
      note: "No retained execution evidence testing dependence on recalled material was inspected or produced; structural checks do not substitute."
---

# Apache Maka agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/apache-maka.md`

**Legacy memory review:** not applicable

This run regenerates the analysis from the frozen source for a bounded comparison-consumer pilot. The destinations above are intended outputs; the run state establishes publication completion.

## Boundary and evidence

Maka is an enclosing agent runtime with desktop, terminal, command-line and evaluation clients. The analysis concerns its host-owned invocation, model/tool progression, durable history, built-in memory, compaction, goal judgment, and consequential alternate execution routes. The comparison scope is narrower: built-in retained conversational memory, its summaries, local MEMORY.md and atomic MemoryItems. Static shipped instructions, arbitrary tool-written project artifacts and independently maintained extensions are not part of that memory comparison.

The only evidence repository is `https://github.com/apache/maka`, frozen at `ece69ab3e7a1629a6073831005711d8aa7160ca4`. Source reads use commit-addressed Git access through `/home/zby/llm/commonplace/related-systems/apache--maka`. The checkout worktree, previous reviews and later revisions supply no findings. The cutoff is the inspection date, not a claim that this commit is the latest upstream revision.

The tier is code-grounded. The hosted ordinary route and selected forcing paths were traced statically. Source comments and architectural claims remain distinct from executable branches. No target runtime was executed. Remote providers, operating-system isolation, third-party tools, user configuration, live credentials and benchmark environments are excluded; their exclusion prevents a deployed security, reliability, performance or memory-effect conclusion. Peer meshes, computer-use adapters, image-context projection, deep-research and daily-review features are not inspected end to end. Whole-system identifies the selected target; it does not claim exhaustive verification of every route family.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/apache/maka` | `ece69ab3e7a1629a6073831005711d8aa7160ca4` | implementation | Selected host, runtime, core, storage and eval files identified in the canonical records below | [RuntimeKernel](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/runtime-kernel.ts#L1143-L1279); all local path/range anchors below address this commit | No executed target run, deployed configuration or external service internals; wiring cannot establish activation or effect |
| SRC-2 | Git | `https://github.com/apache/maka` | `ece69ab3e7a1629a6073831005711d8aa7160ca4` | doctrine/design | Product claim and architectural ownership | [README](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/README.md#L24-L61), `ARCHITECTURE.md:24-75` | Design intent alone does not prove complete coverage or operation |
| SRC-3 | Git | `https://github.com/apache/maka` | `ece69ab3e7a1629a6073831005711d8aa7160ca4` | reported operation | Bounded benchmark report and its retained-evidence disclaimer | `docs/eval/terminal-bench-2.1-deepseek-v4-flash-four-arm.md:22-30,81-81` | Underlying prompts, traces and verifier output are not inspected; no observed-run or component-causal claim follows |

## Shared records

### Components

| ID | Source-native component and responsibility | Form and storage | Conclusion status | Evidence |
|---|---|---|---|---|
| CMP-1 | Runtime Host interactive/root admission; owns hosted session/turn identity and entry arbitration | Symbolic TypeScript; durable admission store accessed through interfaces | wired | SRC-1 `packages/runtime-host/src/server/interactive-turn-coordinator.ts:80-116`, `packages/runtime-host/src/server/root-turn-coordinator.ts:1462-1510` |
| CMP-2 | RuntimeKernel, AgentRun and AI SDK backend; own invocation lifecycle and repeated provider steps | Symbolic TypeScript; projected messages plus retained runtime events | wired | SRC-1 `packages/runtime/src/runtime-kernel.ts:1143-1279`, `packages/runtime/src/agent-run.ts:658-739`, `packages/runtime/src/ai-sdk-backend.ts:2022-2087` |
| CMP-3 | ToolRuntime; validates local tool calls and passes execution boundary to the executor | Symbolic TypeScript; per-turn state and durable tool-attempt interfaces | wired | SRC-1 `packages/runtime/src/tool-runtime.ts:1105-1157,1338-1390,1493-1558,1661-1677` |

| CMP-4 | HostMemoryCoordinator and MemoryExtractionEngine/coordinator; separate file-bundle and atomic extraction owners | Symbolic TypeScript; file bundle and SQLite commit ports | wired | SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts:162-191,345-467`, `packages/runtime-host/src/server/memory-extraction-coordinator.ts:77-96,123-184` |
| CMP-5 | Runtime store and checkpoint machinery; durable event storage and history projection | Symbolic TypeScript; SQLite and text/provider checkpoint payloads | wired | SRC-1 `packages/storage/src/sqlite-runtime-store.ts:325-328,381-410`, `packages/runtime/src/agent-run.ts:546-569`, `packages/runtime/src/history-compact-checkpoint.ts:87-138` |
| CMP-6 | Goal evaluator and continuation controller | Symbolic control, model judgment and retained goal authority | wired | SRC-1 `packages/runtime/src/goal-evaluator.ts:37-64,122-173`, `packages/runtime/src/goal-continuation.ts:699-741`, `packages/storage/src/goal-authority.ts:171-225` |
| CMP-7 | Eval runner and attempt selector, outside interactive storage authority | Symbolic execution/verifier interfaces and structured results | wired | SRC-1 `packages/eval/src/runner.ts:284-328`, `packages/eval/src/result.ts:31-94` |

### Operative objects

OBJ-1 — RuntimeEvents and their projected conversation history. Structured event identities and control facts coexist with natural-language messages and tool content. AgentRun appends initial user/run facts and reconstructs prior context; subsequent local tool execution requires readable current-run facts. Conclusion status: wired. SRC-1 `packages/runtime/src/agent-run.ts:658-739,948-1013`; `packages/runtime/src/ai-sdk-backend.ts:2022-2033,2815-2825`.

OBJ-2 — Atomic MemoryItem. Natural-language content is coupled to kind, fact/plan/prediction classification, temporal and global/workspace scope, version and lifecycle metadata, keys, hashes, and session/run/turn/event provenance. This contract alone establishes the shape; its executable write and read routes are assessed separately below. Conclusion status: afforded. SRC-1 `packages/core/src/long-term-memory.ts:28-59,75-128`.

OBJ-3 — Local MEMORY.md bundle. Markdown entries carry manual/extracted/imported origin, active/draft/review/archived states, source and optional session scope. Content and symbolic selection metadata must remain distinguishable from OBJ-2. Conclusion status: afforded. SRC-1 `packages/core/src/local-memory.ts:33-79,105-120`.

OBJ-4 — HistoryCompactCheckpoint. Session identity, covered event range/digest and predecessor accompany either v2 summary text or v3 encrypted provider state. Text is natural-language with symbolic access metadata; encrypted provider content does not establish a representational form or model-weight update. Checkpoints enter durable runtime events. Conclusion status: wired. SRC-1 `packages/runtime/src/history-compact-checkpoint.ts:39-56,87-138`; `packages/runtime/src/agent-run.ts:546-569`; `packages/storage/src/sqlite-runtime-store.ts:381-410`.

OBJ-5 — GoalEvaluation and retained goal authority. A model returns completion/impossibility/progress/waiting judgments and a reason; persisted condition, counters and control state support subsequent goal work. The judgment and control metadata are symbolic, with natural-language condition/reason. Conclusion status: wired. SRC-1 `packages/runtime/src/goal-evaluator.ts:37-64,122-173`; `packages/runtime/src/goal-state.ts:25-35,150-199`; `packages/storage/src/goal-authority.ts:171-225`.

OBJ-6 — Task reminder. Pending/in-progress task keys select a one-time natural-language advisory reminder for the goal; this object does not independently verify completion. Conclusion status: wired. SRC-1 `packages/runtime/src/goal-task-gate-policy.ts:35-88`.

OBJ-7 — Benchmark attempt result. Structured score, status, usage, cost, duration and artifact references come from subject execution and configured verification. A selected result is not necessarily a successful task outcome. Conclusion status: wired. SRC-1 `packages/eval/src/runner.ts:284-328`; `packages/eval/src/result.ts:31-94`.

OBJ-8 — Extraction evidence slice. Stable user-authored text, normalized/bounded with event references, supplies evidence to the model and deterministic citation checks. It is an intermediate natural-language/symbolic view of OBJ-1, not an additional durable memory store. Conclusion status: wired. SRC-1 `packages/runtime/src/memory-extraction-evidence.ts:94-117`.

OBJ-9 — Mutable skill catalog and skill files, adjacent to the comparison scope. Install/update/delete/enable/pin and starter creation are wired catalog mutations; SkillSearch serves metadata and Skill loads full user-provided instructions. External skill contents and dependencies remain outside inspection. Conclusion status: wired. SRC-1 `packages/runtime-host/src/server/skill-catalog-repository.ts:478-529`; `packages/runtime/src/skills-agent-tools.ts:143-185,212-249`; `packages/runtime/src/skills-context.ts:183-205`.

OBJ-1 storage annotation: the inspected SQLite runtime store writes and queries runtime events; transient replay arrays are access views, not an extra retained substrate. SRC-1 `packages/storage/src/sqlite-runtime-store.ts:325-328,381-410`.

OBJ-2 storage annotation: items, keys, provenance, receipts and extraction cursors live in SQLite; transaction and cursor conditions protect commitment identity. Storage conclusion status: wired. Source-defined object shape remains an affordance independently of this write route. SRC-1 `packages/storage/src/sqlite-long-term-memory-schema.ts:38-154,216-223`; `packages/storage/src/sqlite-long-term-memory-store.ts:292-402`.

OBJ-3 storage annotation: file-backed MEMORY.md, PENDING.md and backups contain the local bundle. Storage conclusion status: wired. SRC-1 `packages/storage/src/memory-bundle-io.ts:53-65,96-112,147-189`.

### Routes

| ID | Trigger, owner, progression and return | Context, effects and persistence | Conclusion status | Evidence |
|---|---|---|---|---|
| RTE-1 | A client starts a turn with session/turn IDs; Host arbitrates admission, Kernel opens AgentRun, backend issues provider steps, and mapped events return to the client | Current input and prior event projections; Host binds interaction/message ownership, provider identity and cancellation; events and terminal facts retained through store | wired | SRC-1 `packages/runtime-host/src/server/interactive-turn-coordinator.ts:80-116`, `packages/runtime-host/src/server/root-turn-coordinator.ts:1462-1510`, `packages/runtime/src/runtime-kernel.ts:1169-1254`, `packages/runtime/src/model-adapter.ts:281-314,328-339` |
| RTE-2 | Returned local tool call enters ToolRuntime; schema and availability checks can refuse it before dispatch; accepted calls receive executor context and return a settlement to the next provider step | Snapshot arguments, run/turn/tool IDs, current execution boundary and permission mode; durable current-run read is required before local effects | wired | SRC-1 `packages/runtime/src/ai-sdk-backend.ts:2815-2878`, `packages/runtime/src/tool-runtime.ts:1105-1157,1338-1390,1493-1558,1661-1677` |
| RTE-3 | A provider-owned tool starts within the provider step; backend records its call/result rather than executing it through RTE-2 | Provider owns external effects; reported activity enters runtime events; local tool admission cannot be assumed to cover it | wired | SRC-1 `packages/runtime/src/ai-sdk-backend.ts:2506-2557,2827-2833` |
| RTE-4 | Agent Graph supervisor wake passes freshness and identity checks, waits when hosted admission conflicts, then calls the same runtime sendMessage route | Graph/wake/attempt identity, durable run identity, cancellation and terminal classification; graph observer interfaces are presentation-only | wired | SRC-1 `packages/runtime-host/src/server/agent-graph-execution-coordinator.ts:74-143`, `packages/runtime/src/stream-graph-dispatch.ts:38-68` |
| RTE-5 | Scheduled agent work rechecks its connection and enters hosted admission; scheduled notification instead calls a native workspace service | Stored task intent, execution fingerprint and origin identify agent runs; native notifications wait for a service and have separate effect settlement | wired | SRC-1 `packages/runtime-host/src/server/scheduled-task-coordinator.ts:560-605,733-776` |
| RTE-6 | Recovery classifies an unfinished run from its own retained events; a continuation requires a current authoritative safety inspection | Missing terminal history yields a failed recovery classification; terminal commit has a durable barrier; replay safety is conditional, not an assertion that effects never repeat | wired | SRC-1 `packages/runtime/src/agent-run-recovery.ts:49-82`, `packages/runtime/src/runtime-kernel.ts:1475-1486`, `packages/runtime/src/agent-run.ts:1334-1394` |

RTE-7 — Local memory mutation. User/proposal operations create pending material, remember user-authored entries, approve into active memory, reject, change status, reset or restore. Host commits memory/pending documents against expected revision, with backup. Owner: HostMemoryCoordinator; immediate return: operation outcome; future visibility: active entries through RTE-8; expiry/withdrawal: archive/status and policy gates. Conclusion status: wired. SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts:345-467`; `packages/core/src/local-memory.ts:489-535`.

RTE-8 — Local memory prompt projection. Host run composition requests the file bundle; policy enablement, read enablement, privacy and active/session scope determine inclusion. Content is redacted, bounded and framed as untrusted lower-priority context. Consumer: task model in a later composed run; direction: push; effect: context delivery, with behavioral activation uninspected. SQLite OBJ-2 is not its input. Conclusion status: wired. SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts:162-191`; `packages/core/src/local-memory.ts:291-312`; `packages/runtime-host/src/server/interactive-run-composer.ts:588-624`.

RTE-9 — Atomic extraction transformation. Foreground remember, background extraction and automatic compaction triggers enter a per-session lane. Policy/privacy/archive/subagent conditions gate entry. Stable user text supplies OBJ-8 evidence; model proposals and isolated canonicalization produce candidate OBJ-2 content. Assistant context may help interpretation; tool output is not admitted user evidence here. Conclusion status: wired. SRC-1 `packages/runtime-host/src/server/memory-extraction-coordinator.ts:101-184`; `packages/runtime/src/memory-extraction-evidence.ts:94-117`; `packages/runtime/src/memory-extraction.ts:1019-1055`.

RTE-10 — Atomic candidate checking and disposition. Deterministic checks establish content/temporal/key shape, source-reference membership and quote occurrence. A separate model acceptance judgment claims supported durable rewriting. Runtime checks result identity/cardinality, handles requested and incidental rejection differently, then reruns deterministic admission. These are distinct check and disposition functions within this implementation route. Conclusion status: wired. SRC-1 `packages/runtime/src/memory-extraction-proposal.ts:308-365`; `packages/runtime/src/memory-extraction.ts:1061-1112`; SRC-2 `packages/runtime/src/memory-extraction-proposal.ts:201-220`.

RTE-11 — Atomic retention and storage retrieval surface. Accepted items and source coverage commit under policy/cursor conditions; provenance survives as event references. Storage API offers item-ID and key-prefix lookup with scope/lifecycle filters. Write conclusion status: wired. Later retrieval conclusion status: afforded. No production task-model caller was found (ABS-1), so returned storage data must not be represented as established contextual delivery. SRC-1 `packages/runtime/src/memory-extraction.ts:1120-1139,1861-1892`; `packages/storage/src/sqlite-long-term-memory-store.ts:292-402,842-889`; `packages/storage/src/long-term-memory-store.ts:155-159`.

RTE-12 — Text compaction transformation and admission. A model summarizes folded conversation events and can update a previous summary. Ordered sections, substantive content, truncation signals and applicable size limits are checked; bounded repair follows, and persistent failure withholds the replacement. Structural eligibility is not semantic faithfulness. Conclusion status: wired. SRC-1 `packages/runtime/src/history-compact-summarizer.ts:117-214`; `packages/runtime/src/history-compact-summary-validation.ts:63-130,144-159`; `packages/runtime/src/history-compaction.ts:363-417`.

RTE-13 — Durable history/checkpoint read-back. AgentRun retains checkpoints; the loader reads and validates them; replay matches session/event coverage and replaces the covered prefix with checkpoint context plus successor events. Prior session history is loaded for later invocations. Trigger: new/continued model request; owner: runtime projection; direction: push; framing: conversation context; invalidation: coverage/digest mismatch refuses projection. Provider checkpoint internals are opaque (OBJ-4). Delivery is wired; behavioral activation is uninspected. SRC-1 `packages/runtime/src/agent-run.ts:546-569`; `packages/runtime/src/history-compact-ledger.ts:57-139`; `packages/runtime/src/prior-run-context.ts:26-74`; `packages/runtime/src/ai-sdk-backend.ts:1872-1916,5066-5100`.

RTE-14 — Goal check. A separate tool-free call to the session's model judges the goal using recent conversation. Consumer: goal controller; result: OBJ-5 with judgment flags and rationale. Parser coerces fields with Boolean(), so parse success alone does not establish boolean-schema compliance. Conclusion status: wired. SRC-1 `packages/runtime/src/goal-evaluator.ts:57-64,122-173`.

RTE-15 — Goal disposition and steering. Matching active-goal state permits terminal achieved/impossible settlement or further work/waiting. Evaluation reason enters later continuation text. Pending-task reminders are advisory and occur after terminal evaluator settlement, so cannot veto it. Persistence horizon: this goal/session, not demonstrated cross-task learning. Conclusion status: wired. SRC-1 `packages/runtime/src/goal-continuation.ts:699-741,958-970`; `packages/runtime/src/goal-task-gate-policy.ts:35-88`.

RTE-16 — Benchmark verification and cell selection. Executor verification supplies an acquired score/result after eligible subject execution; shape/error handling is separate from substantive verifier warrant. Earliest non-infrastructure/non-indeterminate attempt becomes authoritative for the cell, including scored failure. Consumer: experiment result, not an evidenced automatic runtime-policy update. Conclusion status: wired. SRC-1 `packages/eval/src/runner.ts:284-328`; `packages/eval/src/result.ts:87-94`.

RTE-17 — Skill mutation and pull consumption. Host catalog operations can change retained instruction material; model tools separately search metadata and load full instructions. Force: lower-priority user-provided instructions in invoking context. No trace-fed skill writer is established by this bounded catalog/tool inspection; general learning from arbitrary skill updates remains uninspected. Conclusion status: wired. SRC-1 `packages/runtime-host/src/server/skill-catalog-repository.ts:478-529`; `packages/runtime/src/skills-agent-tools.ts:143-185,212-249`; `packages/runtime/src/skills-context.ts:183-205`.

### Claims

CLM-1 — Maka presents itself as a task-finishing workspace with a complete execution record and one Runtime Host serving thin clients. Conclusion status: claimed. SRC-2 `README.md:24-61`; `ARCHITECTURE.md:24-48`. RTE-1 through RTE-6 support specific ownership and record paths; provider-side internals and uninspected adapters limit completeness.

CLM-2 — Maka describes benchmark comparison with shared models/verifiers and published per-task records. Conclusion status: claimed. SRC-2 `README.md:48-54`; `ARCHITECTURE.md:50-63`. SRC-3's report does not supply inspected raw traces or verifier output, so this run makes no benchmark-score or component-effect inference.

CLM-3 — Atomic canonicalization should preserve a durable assertion fully supported by user evidence without adding facts. Conclusion status: claimed. SRC-2 `packages/runtime/src/memory-extraction-proposal.ts:201-220`. RTE-9 through RTE-11 implement a source-support admission procedure; no execution measures its fidelity.

CLM-4 — Text checkpoints should retain the context needed to continue the work. Conclusion status: claimed. SRC-2 `packages/runtime/src/history-compact-summary-validation.ts:38-60`. RTE-12/RTE-13 establish generation, structural admission and use, not proposition-level preservation.

CLM-5 — Separate goal judgment is intended to prevent premature self-declared completion. Conclusion status: claimed. SRC-2 `packages/runtime/src/goal-evaluator.ts:20-30`. RTE-14/RTE-15 separate invocations, but use the same session model and supplied conversation rather than independent environmental checks.

### Evidenced absences

ABS-1 — No production caller of atomic item recall was found within the inspected composition. Conclusion status: absent. Search boundary: commit `ece69ab3e7a1629a6073831005711d8aa7160ca4`, roots `packages/` and `apps/`, query `\.readItem\(|\.searchByKeys\(`, excluding `**/__tests__/**` and `**/*.test.ts`. Only the storage facade forwards these calls. Cross-checks: extractor ports lack a recall consumer, and prompt projection reads the local file bundle. SRC-1 `packages/storage/src/long-term-memory-store.ts:155-159`; `packages/runtime-host/src/server/memory-extraction-coordinator.ts:77-96`; `packages/runtime-host/src/server/memory-coordinator.ts:162-191`. This prevents a claim that new SQLite item content affects later task-model work. It does not preclude an external embedder calling the public storage API.

### Behavioral-authority paths

BAP-1 — RTE-1/RTE-2 consumer: RuntimeKernel and ToolRuntime; channel: typed execution and admission state; force: enforcement of the inspected identity, schema and dispatch conditions; horizon: hosted invocation and local tool attempt. This is operational authority, not warrant for model-produced claims. SRC-1 `packages/runtime/src/runtime-kernel.ts:1169-1232`; `packages/runtime/src/tool-runtime.ts:1338-1390,1493-1558`.

BAP-2 — RTE-8 consumer: task model; channel: composed local-memory prompt text; force: advisory knowledge explicitly subordinated to system/developer/permission rules; horizon: a composed run while policy/scope admit the entry. Presence is wired; changed behavior is uninspected. SRC-1 `packages/runtime-host/src/server/interactive-run-composer.ts:588-624`.

BAP-3 — RTE-13 has two consumers: model receives summary/history as advisory conversation knowledge; runtime uses coverage/digest as symbolic validation and routing authority over which history is replayed. Horizon: matching session checkpoint and later continuation. SRC-1 `packages/runtime/src/ai-sdk-backend.ts:1890-1916`; `packages/runtime/src/history-compact-checkpoint.ts:39-56`.

BAP-4 — RTE-10/RTE-11 consumer: extractor/store; channel: admission results, source IDs, cursor and receipts; force: permission or enforcement over a memory write; horizon: this operation and its coverage/replay identity. No task-model authority is established for atomic item content. SRC-1 `packages/runtime/src/memory-extraction.ts:1061-1139`; `packages/storage/src/sqlite-long-term-memory-store.ts:292-402`.

BAP-5 — RTE-14/RTE-15 consumer: goal controller and next task invocation; channel: judgment flags and continuation text; force: terminal/continuation control for flags, advisory steering for rationale; horizon: current goal/session. This operational authority exceeds what was independently verified about task completion. SRC-1 `packages/runtime/src/goal-continuation.ts:699-741,958-970`.

BAP-6 — RTE-16 consumer: experiment selector/report; channel: typed attempt outcomes; force: authoritative cell selection; horizon: this experiment cell. Verifier-domain warrant does not extend to explanations or component effects. SRC-1 `packages/eval/src/runner.ts:284-328`; `packages/eval/src/result.ts:87-94`.

BAP-7 — RTE-17 consumer: model; channel: explicitly loaded skill instructions; force: lower-priority user-provided instruction; horizon: invocation context and enabled catalog version. Source content truth and automatic learning remain uninspected. SRC-1 `packages/runtime/src/skills-agent-tools.ts:212-249`; `packages/runtime/src/skills-context.ts:183-205`.

## Runtime account

The ordinary principal is the connected client acting through Host. Its request supplies session and turn identity, while Host reserves admission and rejects an existing identity with a different execution payload. AgentRun opens the invocation and retains the initial event before constructing prior context. Kernel binds provider, message and interaction ownership, then streams mapped events back through the run's persistence path (RTE-1, OBJ-1).

The AI SDK adapter issues one provider step with the chosen model, projected messages, instructions and active tool schema. Its own retries are disabled; continuation belongs to the outer runtime loop. That loop refreshes durable history, incorporates steering and can reserve the last child-agent step for a tool-free summary. Model output chooses content and proposed tool calls; symbolic runtime control decides admission, repetition and termination. Tool settlement occurs between model requests (SRC-1 `packages/runtime/src/model-adapter.ts:281-314,328-339`; `packages/runtime/src/ai-sdk-backend.ts:2022-2087,2815-2878`; `packages/runtime/src/tool-runtime.ts:1649-1657`).

The capability surface, current grants and deployed isolation are separate. A named tool schema exposes a capability; availability checks and execution boundary determine whether the inspected local route may dispatch. Client-capability tools have a separate preparation contract and can fail before dispatch. The code passes the boundary and permission mode onward; this inspection does not probe the OS or every executor. Provider-owned tools (RTE-3) and scheduled native effects (RTE-5) demonstrate why local ToolRuntime checks cannot establish a universal effects guarantee.

The bounded static forcing cases are:

| Case | Owner and enforcement point | Strength and covered path | Result and limit |
|---|---|---|---|
| Reuse a turn identity with a different payload | Host admission compares durable execution and request identity, RTE-1 | Protocol enforced on inspected root admission | Conflict is returned; external callers bypassing that hosted interface are not covered |
| Lose readable current-run history before local tool continuation | Backend reads durable turn events before settlement, RTE-2 | Enforced precondition on local tool continuation | Unreadable ledger prevents dispatch; provider-owned work may already have occurred in RTE-3 |
| Crash without a terminal event, then request continuation | Recovery classification and authoritative continuation safety check, RTE-6 | Recovery protocol, dependent on store and safety-inspector contracts | Failed closure and revalidated continuation are wired; no crash experiment establishes replay or filesystem guarantees |
| Scheduled work when a dependency is unavailable | Separate agent admission and native service branches, RTE-5 | Conditional protocol | Connection is rechecked for agent work; missing notification service leaves a waiting state; no delivery outcome was observed |

No dynamic check planned. A fake-provider turn, crash injection and memory recall intervention were considered. Static inspection suffices for the wiring conclusions sought here. A dynamic target run would require a prepared Node dependency environment, isolated persistent stores and either a fake provider or configured provider access; none was prepared or executed. Actual activation, recovery under failure and dependence on recalled content remain uninspected.

All material routes receive their read-back and authority dispositions in the lens outputs. RTE-3 reports provider activity without local executor ownership. RTE-4 yields a graph terminal outcome and may reuse the session context; its child/supervisor visibility is bounded by the selected interfaces, not assumed to be a full shared transcript. RTE-5's notification return is a service settlement, not a model-memory read. RTE-6 changes future admissibility and history; it supplies no new source warrant.


## Lens scoping

### Memory/context scope

Depth: full. Trigger evidence: OBJ-1 through OBJ-4, RTE-7 through RTE-13. The inspected core covers retained history/checkpoints, local bundles, atomic item writing, maintenance and access, plus source and coverage metadata. Goal and skill state (OBJ-5/OBJ-9) were checked as adjacent retained control/instruction surfaces, kept outside the scoped comparison. Tool-result offload, arbitrary project files, external skill content and plugins are outside that comparison; no total inventory of every form of agent memory is claimed.

The depth is warranted because several distinct stores and consumers could otherwise be conflated. Full means route analysis within this boundary, not empirical activation or exhaustive deployment inspection.

### Epistemic scope

Depth: full. Trigger evidence: CLM-3 through CLM-5; OBJ-2 through OBJ-8; RTE-9 through RTE-16. The question is what transformations and checks occur, what their results authorize and what warrant survives. The assessed families are memory extraction/admission, local approval/selection, text compaction, goal judgment and settlement, and benchmark verifier/result selection. Independent semantic checks inside tool/provider implementations, opaque provider compaction, task-specific verifiers, other benchmark reports and arbitrary user workflows are unassessed. This prevents a system-complete account of knowledge production.

## Lens outputs

### Memory/context lens

The core inventory comprises accumulated event history (OBJ-1), atomic items and access metadata (OBJ-2), the local file bundle (OBJ-3), and checkpoints (OBJ-4). Their retained substrates are files and SQLite. Transient model-message arrays do not add an in-memory retained store to the profile.

The write paths differ. Local memory accepts user operations and proposal approval; atomic memory transforms eligible user evidence through model calls and deterministic checks; text compaction transforms accumulated conversation into a durable continuation summary. Source event IDs preserve attribution, not source truth. Atomic extraction's evidence restriction excludes tool output as support, whereas the compactor consumes conversation projections containing tool calls/results (RTE-9/RTE-12).

The later consumers differ too. RTE-8 pushes local memory into a composed prompt; RTE-13 pushes selected history/checkpoints into a later request. Both use session/status/coverage predicates rather than demonstrated inferred relevance. RTE-11 exposes key/ID pull at the storage API only; ABS-1 bounds the missing production recall integration. The profile therefore records the combined push/pull surface at afforded basis, while the records preserve wired push and merely afforded pull. It must not be counted as implemented agent pull recall.

For each core route: RTE-7 immediately returns a mutation outcome, and later visibility depends on RTE-8 active/scope/policy selection. RTE-9/RTE-10 return extraction/admission outcomes to their owner; RTE-11 retains content and bookkeeping, with no inspected delegated/task-model recall. RTE-12 returns a candidate checkpoint; RTE-13 validates coverage and supplies it to continuation. Withdrawal is governed by archive/status for local memory, lifecycle filters for atomic access, and coverage/replacement for checkpoints. Delivered text has no retained activation or causal-effect evidence.

The trace-learning classification is bounded to the wired text-checkpoint route: automatic trace-fed transformation creates durable text used for continued task behavior. This is online per-task adaptation in context, with session continuation mapped to the controlled per-task value. It is not a demonstrated reusable skill, improved performance or distributed-parametric update. Atomic extraction alone does not establish cross-task learning because its later agent consumer was not found. Encrypted provider checkpoint content prevents a complete distilled-form or representational-form classification. Known text/symbolic parts remain named without guessing the opaque part.

The manual/automatic write union is supported; curation mapping remains uninspected as a complete controlled set. Approval, withdrawal and summary replacement exist, but this pass does not assert every curation token or equate idempotency with semantic deduplication. Lineage across opaque provider state and general bundle replacement also remains not determinable. Faithfulness tested is uninspected: no retained execution tests dependence on recalled material.

Legacy review detection: not applicable to this selected target. Maka's primary offered work is executing tasks through an enclosing runtime (CLM-1), rather than offering a memory system as the selected product boundary. Memory presence warrants this full lens but does not itself trigger the legacy writer. Invocation disposition: not invoked; memory-review-required is false.

### Epistemic lens

#### Source-and-claim boundary

The sparse overlay uses SRC-1 implementation, SRC-2 doctrine/design and SRC-3 reported operation at the shared commit. It assesses CLM-2 through CLM-5 across the families in the scoping record. No production candidate instance, raw execution trace or intervention was inspected. A committed benchmark report is an attributed report, not a candidate-linked observation of these runtime routes.

#### Object annotations

| Canonical object | Truth-apt part and transformation | Warrant and limit |
|---|---|---|
| OBJ-1/OBJ-8 | Acquired utterances and tool/model content; eligible user evidence is normalized and bounded | Event attribution can survive; user authorship and recorded tool output do not independently establish external truth |
| OBJ-2 | Memory assertion, plan or prediction; model proposal/canonical rewrite is indeterminate between preservation, derivation and ampliation | Candidate-linked evidence is needed to decide semantic relation; source-reference checks alone do not decide it |
| OBJ-3 | Direct user content is acquired; extracted proposals have an indeterminate semantic relation | Human authorization and active state can permit use without a truth-directed acceptance criterion |
| OBJ-4 | Text summary contains statements about work, decisions and next steps; relation to source is indeterminate | Structural acceptance does not decide omission or unsupported inference; encrypted provider payload is unassessed |
| OBJ-5 | Goal-state judgment and reason can be truth-apt; relation to supplied evidence is indeterminate | Recent conversation and the session model supply judgment, not a separate environmental verifier |
| OBJ-6 | Operational reminder selected by task keys | No independently checked candidate proposition; list state is not a task-completion oracle |
| OBJ-7 | Configured verifier score is acquired; selected outcome preserves its recorded status | Substantive warrant depends on the excluded verifier/task domain |
| OBJ-9 | Third-party instruction content, beyond the inspected catalog operation | No inspected content instance establishes truth aptness or its derivation |

#### Authority-route ledger

Architectural status in every implementation row below: implemented. Observed candidate state: no instance observed. These fields do not assert that a condition activated. Record-local anchors are inherited from the cited canonical route; no identity is redefined here.

| Route and function | Content/update relation | Target, evaluator and timing | Result, force and warrant |
|---|---|---|---|
| RTE-9 — content transformation | acquisition/import for OBJ-8; indeterminate for candidate OBJ-2 | Stable user-event selection, then model extraction/canonicalization during admitted extraction | Evidence domain and proposed rewrite; attributable utterance support, not external truth; BAP-4 |
| RTE-10 — check/evidence production | no content change | Candidate content/keys/temporal shape and cited quote checked by deterministic predicates | Rejects predicate violations; quote membership is not entailment; BAP-4 |
| RTE-10 — disposition/acceptance | no content change | Canonicalization model judges one durable assertion against supplied user evidence; runtime checks IDs and reruns screening | Conditional write permission under a stated support criterion; acceptance reliability unmeasured; BAP-4 |
| RTE-11 — retention | no content change | Policy recheck, transaction and cursor/replay conditions before commit | Durable items and event provenance, not established future reliance; BAP-4 |
| RTE-11 — operational admission/selection/consumption | no content change | Storage key/ID/scope/lifecycle predicates when API is called | Afforded data retrieval; production agent use not found (ABS-1), no content warrant granted |
| RTE-7 — disposition/acceptance | no content change | Human approval operation with ID/state/content/document constraints | Authorizes local active entry; no truth-directed criterion in inspected operation; BAP-2 bounds later use |
| RTE-7 — retention | no content change | Expected bundle revision and backup on mutation | Persists authorized documents; consistency is not truth |
| RTE-8 — operational admission/selection/consumption | no content change | Policy, active/session scope, redaction and size at prompt build | Supplies lower-priority context; no endorsement or demonstrated activation; BAP-2 |
| RTE-12 — content transformation | indeterminate | Model folds event projections and prior summary into OBJ-4 | Candidate continuation summary; actual preservation/derivation/ampliation unresolved |
| RTE-12 — check/evidence production | no content change | Ordered-section, content, truncation and applicable size predicates | Shape eligibility; no semantic correspondence judgment established |
| RTE-12 — disposition/acceptance | no content change | Repair budget and final structural gate | Accepts checkpoint format or withholds replacement; not proposition truth |
| RTE-13 — operational admission/selection/consumption | no content change | Coverage/digest matching and replay selection during continuation | Replaces detailed prompt history with admitted checkpoint plus tail; BAP-3 |
| RTE-14 — check/evidence production | indeterminate judgment | Separate tool-free call assesses named goal from recent context | Model judgment, with loose boolean coercion at parse; no direct task/environment check |
| RTE-15 — disposition/acceptance | no content change | Matching active goal and parsed met/impossible/waiting/progress flags | Terminal settlement or continued work; operational authority, not demonstrated task correctness; BAP-5 |
| RTE-15 — behavior/policy adaptation | non-truth-apt policy/content update: continuation steering | Reason and no-progress/task state enter next prompt | Advisory direction within this goal; no reusable general claim accepted; BAP-5 |
| RTE-16 — check/evidence production | acquisition/import | Executor verify after eligible subject execution, then result-shape check | Acquired task-domain result; verifier internals uninspected; BAP-6 |
| RTE-16 — disposition/acceptance | no content change | Earliest attempt excluding infrastructure/indeterminate outcomes | Authoritative cell selection, including scored failure; no automatic runtime adaptation established; BAP-6 |
| RTE-1/RTE-2/RTE-4/RTE-5/RTE-6 — operational admission and recovery | no content change in control checks | Host identity, local call schema, graph freshness, scheduled dependency and continuation predicates | Limits admission on inspected paths; does not accept generated propositions; BAP-1 |
| RTE-3 — acquisition/import of provider results | indeterminate source warrant | Provider-owned tool output enters runtime events | Reported content without local executor control; internal verifier and remote provenance uninspected |
| RTE-17 — operational admission/selection/consumption | no content change in catalog selection | Model searches/loads catalog entries under availability | Supplies instruction force; catalog availability is not truth or learned efficacy; BAP-7 |

The task reminder (OBJ-6 within RTE-15) grants only advisory force once per goal. Terminal judge settlement happens first. An achieved state therefore cannot be read as a guarantee that every pending task was independently checked.

#### Per-object lifecycle disposition

No ampliative transformation is established for a specific observed candidate, so no fabricated discovery-lifecycle phases are assigned. OBJ-2, extracted OBJ-3, text OBJ-4 and OBJ-5 remain indeterminate: preservation, loss, derivation or ampliation require paired source/candidate/check evidence. Their architectural routes are implemented and observed candidate state is no instance observed. Runtime retention, prompt inclusion and continuation steering are not inferred to be post-acceptance lifecycle integration.

OBJ-1/OBJ-8 and direct user-authored OBJ-3 have acquisition/import dispositions; discovery lifecycle is not applicable to that acquisition. OBJ-7 has acquisition/import from configured verifier output; discovery lifecycle is not applicable to result selection. Attribution, bounded projection and verifier-domain limits remain as above. Provider content in OBJ-4 and external content in OBJ-9 remain uninspected, preventing a lifecycle classification.

No lifecycle record for OBJ-6: no candidate truth-apt output independently assessed by the reminder; relevant operational route: RTE-15.

#### Claim versus route comparison

| Claim | Doctrine and implemented support | Observed/causal support and conclusion |
|---|---|---|
| CLM-1 | Host entry/lifecycle and event projection paths RTE-1 through RTE-6 | No target run inspected; supports bounded wiring, not universal logging/isolation/performance |
| CLM-2 | Configured verification and outcome selection RTE-16; SRC-3 describes one experiment | Reported operation only; raw traces/verifier output and comparable method identity are uninspected; no reproduced score or component effect |
| CLM-3 | Source-domain and citation checks plus model canonicalization RTE-9 through RTE-11 | No paired candidate evidence or fidelity measurement; support-admission procedure is implemented, truth/reliability unmeasured |
| CLM-4 | Summary generation, shape repair/admission and later replay RTE-12/RTE-13 | No semantic faithfulness or recall intervention inspected; schema compliance does not validate summary propositions |
| CLM-5 | Separate goal-judgment invocation and consumed flags RTE-14/RTE-15 | No prevention-effect comparison; same model and supplied text remain the judgment boundary |

#### Bounded conclusion

Maka retains and uses material through different authorities. Citation predicates establish eligible-source membership; model canonicalization judges asserted support; local approval authorizes inclusion; summary checks admit format; goal judgment controls continuation; verifier results authorize a benchmark cell outcome. None transfers its license to all the others. Strong operational influence can coexist with unmeasured semantic fidelity.

## Reconciliation

The parent integrated two independently scoped lens returns and rechecked their source identity and consequential anchors. Memory-local proposals were registered as CMP-4/CMP-5, OBJ-4, RTE-7 through RTE-13, ABS-1 and BAP-2 through BAP-4. Epistemic proposals for evidence, goal, reminder and eval objects became OBJ-8/OBJ-5/OBJ-6/OBJ-7; their routes became RTE-9 through RTE-16, with distinct functions retained in the overlay. Adjacent skill material became OBJ-9/RTE-17/BAP-7. No local proposal tags remain as record identities.

The memory worker proposed positive legacy detection from memory presence. That proposal was rejected: the producer's rule concerns the primary offered work of the selected target. CLM-1 and SRC-2 establish Maka as an enclosing task runtime. The canonical disposition is memory-review-required false; memory remains a mandatory full lens. The worker's recommendation did not alter source identity or publication scope.

Both lenses independently separated local memory approval from atomic extraction. The parent reran the readItem/searchByKeys search and confirmed only storage-facade hits. The resulting ABS-1 is scoped to production composition rather than a claim that lookup APIs do not exist. Afforded pull and wired push stay separate in RTE-11/RTE-8/RTE-13, with the comparison union at the weaker basis.

The opaque provider checkpoint was retained as an uncertainty, not silently mapped to natural language or distributed-parametric learning. All observed-candidate states remain no instance observed, and no wiring status was upgraded to activation, measured faithfulness or causality. No other anchored conflict remains unresolved.

## Bounded synthesis

Maka's distinguishing architecture is the separation between durable execution facts and the context projected for the next model request. Host admission and runtime ownership constrain the inspected ordinary path, while graph wakes and scheduled agent work re-enter that ownership. Provider-owned tools and scheduled native effects have different effect boundaries. A local dispatch precondition therefore cannot stand for universal control over everything a model or schedule may cause.

Its built-in memory is likewise several mechanisms. File-backed local memory is user-authorized, filtered and injected as lower-priority context. Atomic extraction admits attributed user assertions into a structured SQLite store, but this commit's inspected production composition does not recall those items into the task model. Conversation history and compaction checkpoints form a separate later-use route, including online, session-bounded text transformation. A single claim that Maka learns from all stored memories would erase the missing consumer and the different horizons.

For a scenario requiring later access to accumulated conversation, the history/checkpoint route supplies implementation evidence. For a scenario requiring a newly extracted global/workspace item to guide a later task, the current evidence stops at writing and storage lookup affordance. For a scenario requiring independently verified completion, the separate goal judge supplies an additional model judgment over recent context, with control authority but no inspected environmental verification. Benchmark result selection is a separate task-verifier domain, not evidence that memory caused an improvement.

The assessment would change with an integrated atomic recall consumer, candidate-linked source/summary checks, stricter goal-result admission, inspected deployed isolation, or retained interventions measuring dependence on recalled content. None is inferred from a passing schema, active entry, terminal goal state or reported benchmark score.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Static inspection only | SRC-1, all implementation routes | Frozen selected source paths | Successful operation, behavioral activation, reliability and causal benefit | Retained target executions or controlled interventions |
| Missing atomic production recall integration | OBJ-2, RTE-11, ABS-1 | Production call search plus extraction/prompt composition | New atomic content influences later task work | Source-wired consumer and, for activation, retained behavioral evidence |
| Opaque provider checkpoint | OBJ-4, RTE-13 | Type and replay interfaces | Complete form, lineage, distilled content or weight-update classification | Inspectable provider-state contract or content-specific probes |
| Summary truth not checked by structural predicates | OBJ-4, RTE-12 | Summarizer, summary validator and planner | Semantic preservation and warranted summary propositions | Paired events/summary, semantic checks and retained outcomes |
| Goal judge uses supplied conversation and loose boolean coercion | OBJ-5, RTE-14/RTE-15 | Judge/parser and continuation settlement | Independent task verification or strict typed-JSON admission | Environmental verifier route and stricter admission, tested with retained cases |
| External effect and isolation envelopes uninspected | RTE-2/RTE-3/RTE-5 | Local admission and adapter boundaries | Universal permissions, replay or containment guarantee | Per-executor/provider contracts and deployed probes |
| Benchmark raw evidence unavailable to this pass | SRC-3, CLM-2, OBJ-7 | One report and general eval interfaces | Reproduced outcome, score or component-level causal attribution | Exact tasks, methods, attempts and verifier outputs |
| Adjacent route families not traced end to end | OBJ-9, RTE-4/RTE-17 | Selected graph and skill interfaces; excluded peer/image/offload/research families | Exhaustive whole-system epistemic or memory classification | Bounded follow-on route inspection and source regeneration |
| Incomplete aggregate lineage and curation mapping | OBJ-1 through OBJ-4 | Core memory boundary with opaque/replacement seams | Complete controlled-value sets for those axes | Additional inspected provenance and maintenance semantics |

## Verification and blockers

### Semantic verification

Source-first baseline and both mandatory lenses completed at the same commit. Independent lens workers returned sparse records; parent reconciled IDs, source layers, primary-work legacy detection, scoped absence and evidence strength. Parent re-read local-memory injection, checkpoint projection, atomic admission, goal parser, ordinary/tool/alternate entry and terminal paths. No prior review or legacy CSV supplied a finding. Local final review checked that known comparison unions retain weaker bases, unknowns do not imply negatives, and memory presence does not imply activation. This is analytical verification, not an executed target test.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/result.md`. Full deterministic validation passed with no failures or warnings. Publication additionally verifies all source anchors before completing the run.

### Blockers

None. Analytical limitations above withhold stronger conclusions; they do not prevent the bounded result from completing.
