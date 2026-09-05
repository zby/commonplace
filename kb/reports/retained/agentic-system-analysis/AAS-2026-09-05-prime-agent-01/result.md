---
type: kb/types/agentic-system-analysis-result.md
description: "Prime Agent runtime, retained-context and refinement analysis at commit 5146337; complete code-grounded disposition"
run-id: AAS-2026-09-05-prime-agent-01
system: "Prime Agent"
run-date: "2026-09-05"
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "514633727bf26d74f39f3119c2b0e31a5ceb2a9d"
analysis-cutoff: "2026-09-05"
evidence-tier: code-grounded
memory-comparison:
  scope: Built-in accumulated session history, compaction and branch summaries, session/global supplemental harness
    entries and audit history, kernel namespace snapshots and their manifests, and retained child continuation.
    Includes separately authored skills at the documented authoring and loading boundary. Excludes shipped static
    instructions, arbitrary extension implementations, provider internals, task work products outside these stores,
    dashboard recaps without an established model consumer, and operational goal/heartbeat/schedule/admission control
    state. Opaque kernel payloads remain included.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - files
      - in-memory
      records:
      - OBJ-1
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - OBJ-10
      - OBJ-11
      - OBJ-12
      - OBJ-13
      note: JSONL history and audits, JSON harness state and manifests, dill payloads, skill files, and live session/kernel
        maps; the history tree is a logical organization in files, not a graph database.
    representational_form:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - OBJ-9
      - OBJ-10
      - OBJ-13
      note: Readable summaries are natural language and addressing/skill contracts are symbolic, but restored arbitrary
        dill values are not classified by their JSON name manifest; no complete aggregate form set follows.
    lineage:
      assessment: known
      basis: afforded
      values:
      - authored
      - imported
      - other-compiled
      - trace-extracted
      records:
      - OBJ-1
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - OBJ-10
      - OBJ-13
      - RTE-12
      note: Authored user/agent entries and skills, acquired messages/data, mechanically constructed addressing/manifests/snapshots,
        and automatic trace-derived summaries/refinement coexist. Authored skill creation is documented and loading
        is wired. Payload-specific semantic provenance is not certified.
    behavioral_authority:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - OBJ-10
      - OBJ-13
      note: Established consumers use knowledge, supplemental instruction, and routing hints. Arbitrary restored
        helpers and generated skill implementations have unspecified executable effects, preventing a complete aggregate
        authority set.
    write_agency:
      assessment: known
      basis: afforded
      values:
      - automatic
      - manual
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-12
      - RTE-14
      note: Automatic recording, summaries, refinement and snapshotting coexist with explicit human/agent authorship.
        A human-triggered model extraction is automatic; direct authorship is a separate afforded surface.
    curation_operations:
      assessment: known
      basis: afforded
      values:
      - consolidate
      - decay
      - evolve
      - invalidate
      - synthesize
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      note: Summaries consolidate; updates evolve; audited deletes withdraw reliance while preserving before images;
        oversized kernel values can be forgotten; refiner prompts afford synthesis of reusable policies from trajectories.
        No semantic dedup or tier-promotion mechanism is established by ID collisions or choosing the global store.
    read_back_direction:
      assessment: known
      basis: afforded
      values:
      - pull
      - push
      records:
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-12
      - RTE-13
      - RTE-14
      note: Model context assembly and namespace revival automatically supply retained state; kernel-agent requests
        can retrieve complete harness entries, skill bodies, and existing values. Documented authored-skill consumption
        is afforded, with its loader wired.
    read_back_signal:
      assessment: known
      basis: wired
      values:
      - coarse
      - identifier
      records:
      - RTE-7
      - RTE-10
      - RTE-11
      - RTE-13
      - RTE-14
      note: Branch leaf/parent/first-kept matching selects actual delivered history; selected session artifact paths
        choose namespace payloads. Harness and skill catalogs use scope/availability and bounded listing, not semantic
        matching. Refiner judgment selects writes, not a separate semantic retrieval push.
    trace_learning:
      assessment: known
      basis: wired
      values:
      - 'yes'
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      note: Automatic trace-fed summaries and refinement persist material subsequently supplied to model consumers.
        Raw history, ordinary namespace copying and authored skill packaging alone are not the qualifying transformation.
    trace_source:
      assessment: known
      basis: wired
      values:
      - session-logs
      - tool-traces
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      note: Qualifying built-in transformations serialize retained conversation messages, including tool calls/results
        and mechanically extracted file operations. The source calls this a trajectory; there is no additional independent
        trajectory store in these routes.
    learning_scope:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      note: Global refinement affords cross-task reuse and explicitly project-qualified lessons; local stores and
        continuation summaries follow session/branch boundaries. The compaction prompt explicitly permits multiple
        tasks, and a branch has no enforced task horizon. A complete per-task/per-project/cross-task union would
        overstate those boundaries.
    learning_timing:
      assessment: known
      basis: wired
      values:
      - online
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      note: 'The qualifying transformations occur in the ongoing session: compaction, branch navigation, explicit
        refine, or automatic turn/compaction checkpoints; refiner background planning is applied between turns.
        Planning/apply phases do not establish a separate offline learning or reviewed deployment stage.'
    distilled_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - symbolic
      records:
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - RTE-10
      note: Qualifying routes retain natural-language summaries and supplemental entries, plus structured skill
        reference/argument contracts and summary access metadata. No parameter update is implemented by these transformations;
        opaque namespace copying is outside the qualifying trace-learning subset.
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - CLM-4
      note: The commission excludes target execution and retained deployed evidence. Static wiring and expected-outcome
        strings do not test dependence on recalled content; neither yes nor a system-wide empirical no is established.
---

# Prime Agent agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/prime-agent.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/memory-report.md`
**Memory analysis report SHA-256:** 97627341457b6cbcc2b89252946e2f2e763353be64aac074a75d7911cc2a4a39

Run AAS-2026-09-05-prime-agent-01 opened on 2026-09-05. These are intended destinations; the run state separately establishes publication completion.

## Boundary and evidence

Evidence basis: static inspection of Prime Agent source code and its shipped documentation at `514633727bf26d74f39f3119c2b0e31a5ceb2a9d`, cutoff 2026-09-05. No target execution or performance experiment was run. The existing checkout supplied this revision; upstream freshness was not checked.

This analysis explains how the coding and research runtime executes work, maintains continuity, and admits changes to its supplemental harness. Prime Agent is an enclosing runtime: it owns model/tool iteration, child sessions, queues, retained session state and background execution. Its Recursive Language Model (RLM) interface expresses tool use and delegation through persistent Python. Its Continual Harness supplies mutable supplemental state. These are source-native mechanisms; the memory and epistemic classifications below annotate them.

Whole-system is the selected product boundary, not a claim of exhaustive source coverage. Inspected families are ordinary session dispatch, provider-call assembly, IPython and tool hooks, recursive child admission/return, daemon recovery, scheduling, extension/provider registration, package admission, refinement, and the specialist's retained-context routes. TUI rendering, installer/release-update internals, every provider adapter and every third-party extension or executable skill were not exhaustively inspected. Those gaps prevent complete UI, distribution, provider-native tool and arbitrary extension guarantees. The external OS, Python/Node dependencies, credential services, remote models and MCP services are dependencies, not implementations supplied by this repository. Their internals, deployment permissions and availability remain uninspected. The linked RLM/Continual Harness papers and Verifiers/PRIME-RL projects are outside the source allowlist; research efficacy and training-loop claims cannot be imported from their names or links.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/PrimeIntellect-ai/prime-agent`; local access root `/home/zby/llm/commonplace/related-systems/PrimeIntellect-ai--prime-agent` | `514633727bf26d74f39f3119c2b0e31a5ceb2a9d` | implementation | Bounded ranges cited in the shared records: agent loop; coding-agent session, SDK, tools, extensions, registry, package manager, daemon, cron, refinement, compaction and persistence; Python RLM and harness runtime | [Agent loop](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/agent/src/agent-loop.ts#L305-L499); all SRC-1 path:line spans below refer to this commit | Static implementation only; no execution, provider internals, arbitrary installed payloads or external evaluator data |
| SRC-2 | Git | `https://github.com/PrimeIntellect-ai/prime-agent` | `514633727bf26d74f39f3119c2b0e31a5ceb2a9d` | doctrine/design | README claimed work and trust boundary; shipped architecture documentation and lens-specific documentation anchors | [README](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/README.md#L39-L96); `README.md:39-52,71-74,88-96`; `packages/coding-agent/docs/architecture.md:3-86` | No reported-operation, observed-run or causal-experiment source admitted; documentation cannot establish benefit |

All source inspection used full-commit-addressed Git blobs. No worktree contents or prior system analyses supplied evidence. Wide discovery output that was truncated was not cited; load-bearing ranges were subsequently read in bounded deliveries.

## Shared records

### Components

CMP-1 — AgentSession and agent-core loop. Symbolic TypeScript implementation; transient in-memory queues and messages with file-backed session persistence. Owns preparation, continuation, tool dispatch and terminal events. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/agent-session.ts:5913-6035`; `packages/agent/src/agent-loop.ts:305-499`.

CMP-2 — Persistent IPython and RLM host bridge. Symbolic Python/TypeScript execution machinery; in-memory kernel state plus serialized state treated separately below. Model-visible Python cells can perform file, shell and host operations. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/tools/ipython.ts:627-704`; `prime-agent-runtime/src/rlm/__init__.py:148-158`.

CMP-3 — Provider language models used for ordinary responses, child work and the lens-identified summary/refinement roles. Distributed-parametric component accessed through provider/model selectors. Identity-resolution conclusion status: wired: restored or configured provider/model IDs resolve through the registry, whose URLs and implementations may be overridden; an exact selector is not a retained weight digest. Parameter-change conclusion status: uninspected for provider internals; inspected call sites request inference, not a weight update. Exact weight fixity is uninspected, and no selected deployed model is known. Refinement changes external harness state, so parameter fixity would not settle trace learning. SRC-1 `packages/coding-agent/src/core/sdk.ts:176-209,277-299`; `packages/coding-agent/src/core/model-registry.ts:517-562,1015-1019,1435-1460`; `packages/coding-agent/src/core/agent-session.ts:9358-9378`.

CMP-4 — Daemon supervisor, session worker and scheduler. Symbolic TypeScript control plane; local sockets, detached processes, file-backed recovery records and scheduled jobs. Conclusion status: wired. SRC-1 `packages/coding-agent/src/modes/daemon/daemon-supervisor.ts:2430-2485,3170-3248`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:566-591`; `packages/coding-agent/src/core/cron-jobs.ts:932-1044`. Declared role separation: SRC-2 `packages/coding-agent/docs/architecture.md:43-49`.

CMP-5 — Dashboard recap model. Separate distributed-parametric role, resolved to provider `prime-inference` and model `qwen/qwen3-30b-a3b-instruct-2507` with configured authentication. Selector wiring is wired; exact deployed weights and parameter change during operation are uninspected. It produces OBJ-14 for display; no later model consumer was established at the inspected endpoints. SRC-1 `packages/coding-agent/src/modes/daemon/daemon-session-summarizer.ts:8-46,150-176,318-371`.

### Operative objects

OBJ-1 — Session messages/history entries. Canonical seed retained without splitting its referent: user, assistant and tool-result history; compaction entries, harness state and kernel blobs have separate IDs below. Message content carries natural language and possible structured/code/multimodal parts in JSONL; history is neither inherently warranted nor guaranteed to preserve every opaque provider payload. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/sdk.ts:176-188,332-344`; memory records supply detailed write/read-back anchors.

OBJ-2 — Model-generated IPython code and its output. Python is symbolic executable content; stdout/result/traceback may contain truth-apt natural-language or structured data. Kernel execution changes process and external project state; recorded tool results enter OBJ-1. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/tools/ipython.ts:637-704`.

OBJ-3 — Extension/skill/package source and registration. Executable modules plus declarative configuration on local/project/user files; user or model-authored file contents can supply new capabilities. Installed artifacts are not automatically source-reviewed by their loader. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/extensions/loader.ts:328-439`; `packages/coding-agent/src/core/package-manager.ts:946-995`. Detailed executable Python skill implementation remains uninspected; it is not conflated with a stored skill description.

OBJ-4 — Cron and heartbeat job instructions and dispatch state. Symbolic schedule/identity/state plus natural-language prompts retained in the job store, selected for a named session. Operational control state, with memory-profile inclusion/exclusion stated by the integrated scope. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/cron-jobs.ts:932-1044`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:574-591,1777-1847`.

OBJ-5 — Command/worker recovery records. Symbolic file-backed identity, pending/complete response or busy-operation records. Their consumer may refuse replay or hold interrupted work. Conclusion status: wired. SRC-1 `packages/coding-agent/src/modes/daemon/worker-recovery-journal.ts:14-55,66-103`; `packages/coding-agent/src/modes/daemon/daemon-supervisor.ts:1411-1431,3198-3248`.

OBJ-6 — Provider/model registry and active tool grant configuration. Symbolic objects resolved from settings, built-in definitions and dynamic extension registration; this identifies execution choices, not model weights. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/model-registry.ts:517-562,1435-1460`; `packages/coding-agent/src/core/agent-session.ts:4190-4208,8835-8853,8890-8929`.

OBJ-7 — compaction entry. A derived natural-language continuation summary plus `firstKeptEntryId`, token count, optional file-operation details and origin/custom-instruction fields in the session log. It replaces older messages in selected model context, while their log entries remain available in history. Summary text has knowledge/instruction force as continuation context; its IDs have selection force in the assembler. SRC-1 `packages/coding-agent/src/core/session-manager.ts:124-132,490-522,1443-1464`. Conclusion status: wired.

OBJ-8 — branch summary. A derived exploration summary saved as a new entry attached to the destination branch. It preserves information from the branch being left for future model context. `fromId` is assigned the branch insertion point by `branchWithSummary`; it is not a complete list of source entries. SRC-1 `packages/coding-agent/src/core/session-manager.ts:134-140,478-486,1839-1855`; `packages/coding-agent/src/core/agent-session.ts:11290-11309,11349-11424`. Conclusion status: wired.

OBJ-9 — supplemental continual harness. Four entry kinds, `prompt`, `memory`, `skill`, and `subagent`, share JSON state with textual content, IDs, paths, scope, reference/argument/metadata records, timestamps and versions. The local file lives under the session artifact directory; global state lives under the agent directory's `harness/`. These are supplemental instructions, advisory knowledge and routing hints when formatted into model prompts. Skill entries describe Python call contracts; subagent entries describe delegation roles. Neither entry kind itself installs code or instantiates a named-agent registry. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:30-63,134-148,269-278,326-358,465-519`; `packages/coding-agent/src/core/system-prompt.ts:108-109,147-148`. Conclusion status: wired.

OBJ-10 — kernel namespace and snapshot pair. Live arbitrary user values are independently dill-serialized into `kernel-state.dill`; `kernel-state.json` records names, skipped/pruned values, size, Python version and time. The manifest is access/status metadata, not a readable rendering of values. Restored functions, data and other objects are consumed by subsequent Python execution. Form and authority of arbitrary payloads cannot be inferred from serialization or names. SRC-1 `packages/coding-agent/src/core/kernel/state-snapshot.ts:1-48,84-163,203-243`. Conclusion status: wired.

OBJ-11 — refinement audit and before/after images. Applied edit records retain before/after entries and errors. The session log stores results; global changes additionally append to `refinements.jsonl`. Audit entries feed future refinement and rollback. Rationale and expected outcome are model assertions, and direct Python CRUD does not automatically create equivalent before/after audits. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:24-25,85-101,716-844,548-561`; `packages/coding-agent/src/core/agent-session.ts:8215-8238`; `prime-agent-runtime/src/rlm/harness.py:345-401,690-703`. Conclusion status: wired.

OBJ-12 — retained child continuation and access records. Each child has its own session manager/artifact directory. Parent-held IDs, session paths and lifecycle state permit roster recovery and reopening completed children. This reuses OBJ-1 and OBJ-7 through OBJ-11 per child rather than creating another kind of memory content. SRC-1 `packages/coding-agent/src/core/agent-session.ts:9346-9401,9470-9529`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:2574-2595,2991-3023,3050-3075`. Conclusion status: wired.

OBJ-13 — separately authored installed skill. A project or personal skill directory contains a Markdown body and optional scripts/reference/assets or Python package. A metadata catalog routes the model; the body is loaded through a requested file read or explicit skill invocation. An authored Python implementation can execute, but its effects are not determined by the package label. This object is separate from a supplemental harness skill description. SRC-2 `packages/coding-agent/skills/skill-creator/SKILL.md:8-27,31-39,73-81`; SRC-1 `packages/coding-agent/src/core/skills.ts:391-424,443-473`; `packages/coding-agent/src/core/agent-session.ts:5034-5056`. Creation/use conclusion status: afforded. Loader conclusion status: wired.

OBJ-14 — Outside-profile operative object: daemon dashboard recap/status. A specialized model summarizes recent messages for dashboard display, with an eight-message, 600-character-per-message input limit and 400 output tokens. Idle verdicts persist as agent status; live recaps also label child updates. This is a trace-derived display summary, but the inspected roster returns IDs/status rather than recap text, and no later model consumer of the recap was established. It therefore does not add a qualifying learning route here. SRC-1 `packages/coding-agent/src/modes/daemon/daemon-session-summarizer.ts:8-46,150-176,318-371`; `packages/coding-agent/src/core/agent-session.ts:9285-9288,9470-9529,10286`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:552`. Conclusion status: wired for production/display; model read-back remains uninspected beyond these endpoints.

OBJ-15 — declarative memory edits — Proposed or applied `kind: memory` entry content, natural language Model emits from OBJ-1, entry overview, and prior refinement overview; CMP-1 persists and exposes it in supplemental prompt. Facts, preferences, decisions, failures, and outcomes; may preserve known information or conjecture a reusable lesson. SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:134-151`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:637-806`, `packages/coding-agent/src/core/refinement/refinement.ts:904-948`. No actual candidate instance; transformation of a particular entry is indeterminate. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-16 — expected improvement — `RefinementProposal.expectedOutcome`, natural-language prediction Model emits expected improvement/validation suggestion; history and prompt rendering consume it. Prediction that proposed edits will improve future behavior. This is ampliative, since trajectory alone does not entail future improvement. SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:157-158`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-805`, `packages/coding-agent/src/core/refinement/refinement.ts:508-512`. No measured observation is substituted for this prediction. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-17 — supplemental prompt edits — `kind: prompt` instruction content, natural language Refiner or extension proposes; CMP-1 admits; model consumes prompt overview. Narrow behavioral policy. No necessary truth-apt output for this part. SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:135`, `packages/coding-agent/src/core/refinement/refinement.ts:146-147`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:673-806`. Reserved base-prompt ID is blocked; policy usefulness is not mechanically validated. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-18 — subagent specification edits — `kind: subagent` delegation instruction, natural language Refiner proposes reusable purpose/instructions/when-to-invoke; caller model uses routing hint to compose task. Delegation policy. No necessary truth-apt output for this part. SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:138`, `packages/coding-agent/src/core/refinement/refinement.ts:146-147`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:454-487`. No subagent performance test in examined refinement route. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-19 — skill interface description edits — `kind: skill` content plus Python reference/arguments objects, mixed natural language and structured descriptors Refiner proposes a description of an installed Python callable; structural validator admits reference fields; future model consults description. Claim about what callable exists and how to invoke it; reusable procedure description. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:693-711`; SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:137`; `README.md:91`. Validation does not import or execute the referenced function. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-20 — automatic review result — `shouldRefine` control bit plus distinct natural-language rationale/instructions Selected session model, or configured injected reviewer, receives checkpoint/context; scheduler consumes result. Bit is a decision to spend effort refining; rationale may assess future usefulness. Neither is a completed-edit verdict. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:951-1011`; `packages/coding-agent/src/core/agent-session.ts:7871-7891`. Rationale content is indeterminate without candidate instance; decision itself is non-truth-apt. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-21 — application receipt — Per-edit `applied`, error, `before`/`after`; refinement ID/scope and audit result, structured data Application code produces from validations and mutations; history, UI, and rollback consume. Whether a particular edit was applied in this invocation, and prior/next entry content. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:716-808`; `packages/coding-agent/src/core/agent-session.ts:8221-8236`. Receipt licenses mutation provenance, not truth or usefulness of entry content. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-22 — quality-gate command configuration — User-supplied shell command list, retry and timeout settings, executable/structured policy Configuration supplies commands; host process runner executes them in task cwd. Criterion for continuing/stopping the current autonomous run. No necessary truth-apt candidate output in the command configuration itself. SRC-1 `packages/coding-agent/src/core/autonomous.ts:57-61`, `packages/coding-agent/src/core/autonomous.ts:106-132`, `packages/coding-agent/src/core/autonomous.ts:284-319`. Gate internals and task-specific coverage unavailable. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-23 — quality-gate result and failure snapshot — Process exit/error/timeout/output plus command/attempt and workspace snapshot, structured data with text output Host program execution produces signals; aggregate gate decision and continuation builder consume. Recorded command success/failure in the actual process environment. Any broader task claim depends on what command checks. SRC-1 `packages/coding-agent/src/core/autonomous.ts:284-370`, `packages/coding-agent/src/core/autonomous.ts:374-424`, `packages/coding-agent/src/core/autonomous.ts:481-569`. Process output is externally acquired; return-code-to-status mapping is domain-limited derivation. No observed run available. Implementation conclusion status: wired; no candidate instance observed. Storage is the parent harness/audit container for entry and receipt parts, or in-memory/configuration state for review/gate parts.

OBJ-24 — Raw stdout/stderr/error text within OBJ-23. Acquired from the configured gate process, consumed by repair context; natural-language or arbitrary structured text, held in memory and propagated into session history. Conclusion status: wired. Truth of printed claims is uninspected. SRC-1 `packages/coding-agent/src/core/autonomous.ts:312-340,350-367`.

OBJ-25 — Program-derived gate disposition within OBJ-23. Symbolic exit/error/timeout classification and retry outcome in runtime state; enforcing consumer RTE-27. Conclusion status: wired. Predicate scope is process status, not general task success. SRC-1 `packages/coding-agent/src/core/autonomous.ts:322-347`.

OBJ-26 — Failure workspace snapshot within OBJ-23. Symbolic Git status/diff/untracked content fingerprint in runtime state; RTE-29 uses it to suppress a repeated check. Conclusion status: wired. Its equality domain excludes configured paths and external environment. SRC-1 `packages/coding-agent/src/core/autonomous.ts:294-310,370-424`.

OBJ-27 — shouldRefine boolean within OBJ-20. Symbolic model-produced decision, transient control input to RTE-17; no candidate truth-apt content in the bit. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:951-1011`.

OBJ-28 — Review rationale/instructions within OBJ-20. Model-generated natural-language assessment, transient input for planning; its truth-apt content and transformation are indeterminate without an instance. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:951-1011`.

OBJ-29 — Serialized arbitrary values within OBJ-10. File-backed dill payloads restored into the kernel namespace. Conclusion status: wired. Payload representational form, semantic provenance and potential behavioral authority remain not-determinable; a serialization format does not decide its contents. SRC-1 `packages/coding-agent/src/core/kernel/state-snapshot.ts:84-163,203-243`.

OBJ-30 — Namespace manifest and restore name/status lists within OBJ-10. Symbolic JSON metadata distinct from the arbitrary values; used for inspection and notices, not a complete substitute for payload contents. Conclusion status: wired. SRC-1 `packages/coding-agent/src/core/kernel/state-snapshot.ts:1-48,203-243`.

### Routes

Each route's implementation conclusion status is wired unless stated otherwise. Operation and activation remain uninspected: reading implementation did not execute these routes. The audit distinguishes immediate return, later read-back, delegated visibility, selection, invalidation, effect and evidence limits. Persistence of ordinary runtime state does not by itself enter the memory-comparison scope.

RTE-1 — Ordinary prompt to model/tool continuation. User/client supplies text and optional images to CMP-1; prepared actions acquire a commit fence, run configured extension preparation, assemble context and call the model. The model proposes text/tool calls; symbolic loop code owns scheduling, tool-result insertion, steering/follow-up priority and terminal emission. Context is selected history, current system prompt, tools and extension transformations. Executor effects occur through RTE-4. Immediate return differs by caller: the session can wait for completion or accept a queued request; model output streams to clients and OBJ-1. Later read-back is the separate memory history route; child visibility is RTE-3, not automatic inheritance of the whole parent chat. Selection uses queued action eligibility and current context; abort/error/stop policy ends the loop, while follow-up and continuation can re-enter it. Recovery may requeue not-yet-delivered input; no arbitrary external effect rollback is implied. SRC-1 `packages/coding-agent/src/core/agent-session.ts:4514-4555,5913-6035`; `packages/agent/src/agent-loop.ts:305-499`.

RTE-2 — Daemon command admission and uncertain-operation recovery. Client/session/command identities route the user's request to a worker. Supervisor symbolically returns recorded complete responses and refuses to replay already pending identified mutations; prompt acknowledgments can precede completion. A detached worker owns execution and journal writes. Recovery selects busy operation records, marks interrupted session state, resets records to recovery_hold and does not replay uncertain work. Immediate return is acknowledgment, saved response or explicit uncertainty; later read-back consumes OBJ-5 to control recovery. Descendant sessions may be included in the worker journal, not given a security boundary. Selection is by command identity or busy record; completed/held state invalidates pending status. Effect is controlled admission and recovery hold, not transactional reversal of Python/file/network effects. Guarantee owner: supervisor; enforcement point: duplicate command admission and recovery loop; strength: protocol; covered paths: identified daemon mutations/journaled workers. Alternate SDK calls and arbitrary subprocess effects do not inherit that protocol. Required contract: usable durable records and OS process identity/termination. SRC-1 `packages/coding-agent/src/modes/daemon/daemon-supervisor.ts:1411-1460,2430-2485,3170-3248`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:4082-4179,4299-4302`.

RTE-3 — Recursive RLM child admission, run and reply. Model code requests rlm.run with prompt/name/model/thinking; the host rejects unsupported arguments, excess recursion depth, invalid selections or disposed parents. Accepted work receives its own child ID/session directory and inherits allowed/active tools and runtime configuration. The parent owns admission, tracking and cancellation; a child AgentSession owns its model loop. Immediate return is a spawn handle at admission, not the child's completed answer. The detached task publishes child state, waits for its turn and descendants to settle, and registers the child for later access. Replies travel separately through agent messages; terminal notices cover completion without a reply and failures. Selection is explicit child identity/model selector; retention/revisit details are in the specialist records. No automatic shared parent chat is demonstrated by constructing a fresh child session. Invalidation is cancellation/deletion/disposal; no rollback of child external effects is implied. Guarantee owner: session host; enforcement: _startRlmChildRun depth/argument checks; strength: invariant for that API, not a limit on arbitrary Python subprocesses or direct provider calls. SRC-1 `prime-agent-runtime/src/rlm/__init__.py:148-158`; `packages/coding-agent/src/core/agent-session.ts:9305-9401,10198-10323,10355-10488,10596-10601`.

RTE-4 — Tool admission and Python/project mutation. Model selects a registered active tool; schema validation and optional beforeToolCall extension results can reject it before execution. IPython serializes its model-facing cells within a tool batch, executes Python or bash magic, and returns output/errors/images and effect details. Proposal is the model's code; admission owner is tool dispatcher plus installed hook; human can abort or configure hooks/grants, but no mandatory human approval exists in the inspected default dispatch. Project changes are admitted by executing code with OS authority, not by a subsequent semantic acceptance gate. Immediate return is tool output; later read-back occurs through OBJ-1 or explicit retained artifacts; child visibility follows inherited grants and accessible filesystem, not isolation. Selector is exact registered tool name; removal/reload changes future selection, abort does not establish external rollback. Guarantee strength: protocol for argument/hook admission, best effort for interruption and kernel revival. Current grants are uninspected; SDK default active tool is ipython, but allowedToolNames and extensions can alter the set. Capability surface includes arbitrary Python, shell, imports, direct APIs and subprocesses inside that admitted cell. OS isolation is an external deployment responsibility; worker processes are expressly not security sandboxes. SRC-1 `packages/agent/src/agent-loop.ts:772-855`; `packages/coding-agent/src/core/agent-session.ts:1423-1472,8835-8853,8890-8929`; `packages/coding-agent/src/core/sdk.ts:235-238`; `packages/coding-agent/src/core/tools/ipython.ts:627-704`; SRC-2 `README.md:71-74`.

RTE-5 — Capability and provider revision through packages/extensions. User/SDK chooses project/user package source or module; package installation admits supported npm/Git/local sources and persists configuration after installation. The loader imports code and calls its factory; an invalid factory or thrown error rejects registration, but module side effects may already have occurred. Extensions can transform context/provider payloads, register tools/providers and change active selections. Proposed change is executable/configuration content; code checks structure and availability, not correctness or trust. Immediate return is installed/loaded state or error; later invocations consume registrations and configuration, including child routes inheriting the resource/runtime host. Selection is configured source/path/provider/name, invalidation is removal/reload/unregistration. Unregistering a provider refreshes original definitions; removing a package does not prove reversal of prior external effects. Human adoption and package managers own acquisition; arbitrary executable skill behavior and binary update admission are uninspected. SRC-1 `packages/coding-agent/src/core/package-manager.ts:946-995`; `packages/coding-agent/src/core/extensions/loader.ts:328-439`; `packages/coding-agent/src/core/sdk.ts:301-324`; `packages/coding-agent/src/core/model-registry.ts:1435-1460`; `packages/coding-agent/src/core/agent-session.ts:8786-8829`.

RTE-6 — Scheduled re-entry. Stored once/cron/interval/heartbeat jobs become due; scheduler claims dispatches and serializes them by active session ID. Worker rechecks runnable state and chooses ordinary follow-up or heartbeat steer/follow-up. Busy compaction/retry/bash/pending work can defer heartbeat delivery. Next-step owner is symbolic scheduler, then CMP-1/model. Immediate return is dispatched/skipped/error state, not task success; later read-back automatically consumes the selected stored prompt, while the resulting work uses ordinary session memory. Child visibility is limited to the job's target session and any delegation it initiates. Selector inputs are due time, job identity and active session, plus busy-state predicates; current job existence/runnable checks invalidate stale dispatches. Effect is another model turn; scheduler stop and job edits govern future work, not rollback of already executed cells. Guarantee strength: protocol within scheduler lane/store contract; exact timing and deployed liveness uninspected. SRC-1 `packages/coding-agent/src/core/cron-jobs.ts:932-1044,1347-1370`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:1777-1847`.

RTE-7 — branch-selected history replay. Trigger: creation/resumption of a session or branch navigation. The host chooses leaf ID, traverses parent IDs, locates the latest compaction and matches `firstKeptEntryId`; it supplies the selected summary and retained messages to the session model. SDK restoration assigns assembled messages to agent state. This is automatic push to the model with identifier selection, even when the operator chose the session/branch upstream. SRC-1 `packages/coding-agent/src/core/session-manager.ts:422-529`; `packages/coding-agent/src/core/sdk.ts:176-189,332-334`. Conclusion status: wired.

RTE-8 — compaction continuation learning. `/compact`, automatic compaction and the compact skill share preparation/generation/application. Raw selected branch messages, previous summary and file-operation traces produce a durable checkpoint; a split turn can use separate history and turn-prefix summaries. The host appends OBJ-7 and immediately rebuilds future model messages. Extensions may cancel/replace before persistence, and abort is checked before append. SRC-1 `packages/coding-agent/src/core/compaction/compaction.ts:579-638,673-745`; `packages/coding-agent/src/core/agent-session.ts:7393-7474`. Conclusion status: wired.

RTE-9 — branch-summary continuation learning. Navigation with `summarize` collects abandoned-branch entries, asks the current model to summarize, saves OBJ-8 at the destination, and rebuilds later context. Extensions can cancel, supply a summary, or change instructions; failed/aborted generation prevents normal application. The selected consumer is the destination session model, not a hypothetical retrieval caller. SRC-1 `packages/coding-agent/src/core/compaction/branch-summarization.ts:151-206,248-285`; `packages/coding-agent/src/core/agent-session.ts:11290-11424`. Conclusion status: wired.

RTE-10 — trace-fed harness refinement and prompt read-back. Explicit `/refine`, the kernel refine skill, or an automatic turn-interval/compaction review initiates model planning from conversation and existing state/history. Valid edits persist to the requested store and a prompt rebuild supplies the bounded catalog to later session turns. The automatic reviewer decides whether to run extraction; this is distinct from admission of each resulting edit. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:880-944,963-1011`; `packages/coding-agent/src/core/agent-session.ts:7771-7890,8091-8132,8215-8238,4340-4379`; SRC-2 `packages/coding-agent/skills/refine/SKILL.md:8-40`. Conclusion status: wired.

RTE-11 — namespace acquisition, checkpoint and revival. Successful Python execution schedules a snapshot; explicit compaction prunes oversized values and reports remaining names; graceful disposal attempts a final snapshot. A later session kernel restores the selected artifact's dill values before bootstrap reinstalls live handles. The model receives a restore notice and can request values through Python. The namespace is automatically supplied to the execution consumer; model inspection of a chosen value is pull. SRC-1 `packages/coding-agent/src/core/kernel/index.ts:956-963,1691-1754,1777-1809`; `packages/coding-agent/src/core/tools/ipython.ts:485-523`; `packages/coding-agent/src/core/agent-session.ts:7222-7296,9018-9025`. Conclusion status: wired.

RTE-12 — explicit kernel harness authoring and lookup. The kernel agent can call `rlm.harness` CRUD/get/list interfaces, with local default and explicit global target. Reads resynchronize on disk modification, and return complete entries by kind/ID or sorted lists. This names a documented in-runtime consumer and supported interface, not just a standalone storage API. The host subsequently loads the same paths when it rebuilds its prompt. Direct CRUD is available without the model-refinement gate; a prompt rebuild is not shown as a mandatory immediate callback of each Python write. SRC-1 `prime-agent-runtime/src/rlm/harness.py:1-7,187-197,303-436,531-558,722-735`; `packages/coding-agent/src/core/agent-session.ts:7893-7899,9196-9210`; `packages/coding-agent/src/core/kernel/bootstrap.ts:54`. Conclusion status: afforded for explicit authored uses; interface wiring status: wired.

RTE-13 — retained child reuse and harness visibility. New children receive a fresh session manager and their own local artifact directory; they share global harness addressing. Parent local harness entries are not automatically merged into a new child's local store in the inspected inline or daemon construction. A completed daemon child can be rehydrated by reopening its saved session and reconstructing its runtime/model, thereby reusing the same replay and namespace routes. Roster lookup gives the parent identifiers for addressing follow-up work. SRC-1 `packages/coding-agent/src/core/agent-session.ts:9196-9210,9346-9401,9470-9529`; `packages/coding-agent/src/modes/daemon/daemon-mode.ts:2574-2595,2991-3023,3050-3075`. Conclusion status: wired. Exact follow-up-message scheduling is parent-owned runtime analysis.

RTE-14 — authored skill retention and later loading. The shipped skill-creator procedure tells the agent to turn a requested workflow into a project/personal skill and verify reload. The installed-resource interface reads its metadata; visible descriptions are automatically cataloged and instruct the model to inspect a matching file through IPython. Explicit `/skill:name` matches the selected identifier and inserts the full body. Thus authored material has an afforded later consumer and wired delivery interfaces, while no automatic trajectory-extraction pipeline is established merely by packaging a skill. SRC-2 `packages/coding-agent/skills/skill-creator/SKILL.md:8-27,62-81`; SRC-1 `packages/coding-agent/src/core/skills.ts:391-424,443-473`; `packages/coding-agent/src/core/agent-session.ts:5034-5056,4360-4379`. Conclusion status: afforded.

RTE-15 — refinement input selection. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Conversation/context passed through conversion, serialization and suffix slicing; when review/planning starts; bounded text/overviews. Context/objects: OBJ-1 → refinement input; truth-apt transformation: non-ampliative reshaping Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:522-565`, `packages/coding-agent/src/core/refinement/refinement.ts:906-919`, `packages/coding-agent/src/core/refinement/refinement.ts:974-989`; CLM-2; no fidelity proof.

RTE-16 — automatic opportunity judgment. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Whether checkpoint contains material useful for future turns; selected model instructed to reject noise/unsupported hypotheses or injected reviewer; before automatic planning; boolean plus rationale/instructions, error. Context/objects: OBJ-20; truth-apt transformation: indeterminate for rationale; non-truth-apt decision output Implementation conclusion status: wired. SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:175-187`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:963-1011`; `packages/coding-agent/src/core/agent-session.ts:7871-7891`; CLM-2; no independence from source model/trajectory established.

RTE-17 — automatic review admission. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Whether automatic refinement may run; controller consumes shouldRefine, settings, cooldown, root/persistence eligibility, branch generation and activity; approve, skip, defer, invalidate. Context/objects: OBJ-20; no content change Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/agent-session.ts:7496-7498`, `packages/coding-agent/src/core/agent-session.ts:7740-7868`, `packages/coding-agent/src/core/agent-session.ts:2256-2329`, `packages/coding-agent/src/core/agent-session.ts:2365-2440`; `packages/coding-agent/src/core/settings-manager.ts:883-899`; CLM-2; opportunity approval is not candidate acceptance.

RTE-18 — refinement proposal generation. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Proposed edits to permitted harness entries; selected session model given trajectory, state and history, optional user instructions; manual/agent request or RTE-17 approval; JSON proposal, empty edit list, error. Context/objects: OBJ-15/OBJ-16/OBJ-17/OBJ-18/OBJ-19; OBJ-15/OBJ-19 truth-apt transformation: indeterminate; OBJ-16: ampliative conjecture; OBJ-17/OBJ-18: non-truth-apt policy/content update: reusable instructions Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:880-948`; `packages/coding-agent/src/core/agent-session.ts:8046-8133`; SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:123-172`; CLM-2; no measurement.

RTE-19 — extension pre-refine veto or replacement. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Conditional extension. Pending non-rollback plan; extension handler can skip or supply normalized proposal before default model planner; skip, supplied proposal, default model call. Context/objects: Proposed refinement round; no content change for skip, otherwise replacement proposal content with transformation indeterminate Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/agent-session.ts:8091-8117`; CLM-2; hook can replace proposer, no inspected extension evaluator.

RTE-20 — per-edit structural and baseline checking. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Action/kind, immutable reserved ID, required fields, Python reference strings, existence and planning baseline; deterministic validation immediately before each mutation; error or admissible edit. Context/objects: OBJ-15/OBJ-17/OBJ-18/OBJ-19 edit envelope; no content change Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:637-789`; CLM-2; checks establish structure/freshness, not semantic truth or callable behavior.

RTE-21 — per-edit operational disposition. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Operational disposition. Each proposed edit; application consumes RTE-20 result; invalid/conflicting edits skipped, eligible edits applied independently. Context/objects: OBJ-21 and edits; no content change in disposition itself Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:716-789`; CLM-2; no epistemic acceptance of memory/prediction.

RTE-22 — scope-state and audit retention. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Applied state and receipt; save current scope state, append global history for global edits, append session audit/outcome; after application. Context/objects: OBJ-15/OBJ-16/OBJ-17/OBJ-18/OBJ-19/OBJ-21; no content change beyond structured recording Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:345-399`, `packages/coding-agent/src/core/refinement/refinement.ts:791-808`; `packages/coding-agent/src/core/agent-session.ts:8221-8236`; CLM-2; retained prediction remains prediction.

RTE-23 — supplemental prompt consumption. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Future model context; prompt builder formats scoped entry overviews, CMP-1 rebuilds prompt after application; changed available instructions/routing. Context/objects: OBJ-15/OBJ-17/OBJ-18/OBJ-19 consumed; non-truth-apt policy/content update: changed supplemental context/instructions Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:429-499`; `packages/coding-agent/src/core/system-prompt.ts:108-109`, `packages/coding-agent/src/core/system-prompt.ts:147-148`; `packages/coding-agent/src/core/agent-session.ts:8237-8238`; CLM-2; behavioral influence does not establish adherence or benefit.

RTE-24 — predicted-outcome presentation. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Expected future improvement; event constructor maps expectedOutcome to outcome and overview renders 'outcome'; subsequent prompt construction. Context/objects: OBJ-16 displayed in history; no content change to prediction's proposition Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-800`, `packages/coding-agent/src/core/refinement/refinement.ts:508-512`; CLM-5; prediction label can look like observation.

RTE-25 — inverse-edit rollback. Stages within RTE-10/RTE-12 memory refinement; generic scope and persistence are owned there. Trigger, owner and progression: Named earlier applied refinement; rollback reconstructs inverse edits from before/after snapshots, reuses application checks; restore/delete entries or reject unsupported inverse edit. Context/objects: OBJ-21 prior snapshots → inverse edits; truth-apt transformation: non-ampliative reshaping of prior recorded content Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:813-845`, `packages/coding-agent/src/core/refinement/refinement.ts:892-904`; `packages/coding-agent/src/core/agent-session.ts:8171-8220`; CLM-2; recovery is not retesting.

RTE-26 — configured quality-gate execution. Autonomous control stage after ordinary RTE-1 work; current run configuration/state governs it. Trigger, owner and progression: Conditional configuration. Configured command against current task cwd; host shell/process runner, sequential commands until first failure; zero exit without error/timeout passes a command, other result fails. Context/objects: OBJ-22 → OBJ-23; acquired process outputs plus entailed result classification in exit-code domain Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/autonomous.ts:273-348`, `packages/coding-agent/src/core/autonomous.ts:481-569`; CLM-3; gate internals/expected answer unknown.

RTE-27 — quality-gate stop/continue disposition. Autonomous control stage after ordinary RTE-1 work; current run configuration/state governs it. Trigger, owner and progression: Run-control decision. Current autonomous run's configured command criteria; code consumes command results; all passed stops continuation, failure requests retry while budget remains, exhausted retries/limits stops without success. Context/objects: OBJ-23 aggregate; no content change Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/autonomous.ts:227-251`, `packages/coding-agent/src/core/autonomous.ts:284-348`; CLM-3; epistemic license limited to named commands' scope.

RTE-28 — failure-feedback continuation. Autonomous control stage after ordinary RTE-1 work; current run configuration/state governs it. Trigger, owner and progression: Next ordinary model turn; continuation builder embeds failed command, attempt, output and repair instruction in user-role message; model receives new repair request. Context/objects: OBJ-23 failure → next-turn instruction; non-truth-apt policy/content update: repair/continue instruction Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/autonomous.ts:196-223`, `packages/coding-agent/src/core/autonomous.ts:350-367`; `packages/coding-agent/src/core/agent-session.ts:3331-3347`; CLM-3; repair success not guaranteed.

RTE-29 — unchanged-workspace rerun suppression. Autonomous control stage after ordinary RTE-1 work; current run configuration/state governs it. Trigger, owner and progression: Whether same failed command should be rerun; equality of scoped Git status, diff and untracked hash; unchanged snapshot suppresses process rerun and increments attempt. Context/objects: OBJ-23 prior failed snapshot; no content change Implementation conclusion status: wired. SRC-1 `packages/coding-agent/src/core/autonomous.ts:294-310`, `packages/coding-agent/src/core/autonomous.ts:370-424`; CLM-3; source changes outside snapshot scope and environmental changes not modeled.

### Claims

CLM-1 — Broad source claim: a coding/research RLM harness with persistent Python, recursive subagents, durable supplemental state/refinement and long-running continuity. Conclusion status: claimed. SRC-2 `README.md:39-52,88-96`. Supported wiring is route-specific; this record does not assert measured improvement or uninterrupted recovery.

CLM-2 — Refine never rewrites the immutable base system prompt and records rollback snapshots. Conclusion status: claimed. SRC-2 `README.md:48,91`. Its applicable implementation scope is the refine edit schema, not all executable Python/extensions with filesystem access.

CLM-3 — Bounded autonomous mode can execute user-defined quality gates; gate passes check only their own targets and limits do not imply success. Conclusion status: claimed. SRC-2 `README.md:96`. The epistemic overlay below relates gate implementation to this deliberately bounded claim.

CLM-4 — memory continuity and reversible supplemental refinement are implemented; improvement and evidence-backed truth remain claims. The source's stored event `outcome` is assigned `proposal.expectedOutcome`. The refiner never receives an implemented before/after task-performance comparison in the inspected planning/application route. SRC-2 `README.md:41-52,88-96`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-809,880-944`. Mechanism conclusion status: wired. Improvement conclusion status: claimed.

CLM-5 — Internal prediction-label mismatch. Conclusion status: wired. A proposal's expectedOutcome is recorded as a refinement event's outcome and displayed with that label in later harness context. This is a retained prediction, not a measurement; whether a model misconstrues it is uninspected. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-800,508-512`; the planner history separately labels it expected outcome at `packages/coding-agent/src/core/refinement/refinement.ts:548-562`.

### Evidenced absences

No canonical absence is inferred from a casual search miss. Provider training, omitted adapters and unexecuted behavior are limitations rather than ABS records.

No additional memory ABS record is asserted; the profile preserves empirical and opaque-payload uncertainty.

ABS-1 — No built-in post-proposal semantic test and evidence-consuming acceptance of an individual refinement prediction/lesson found within the inspected refine path. Conclusion status: absent. Search boundary: SRC-1 at `514633727bf26d74f39f3119c2b0e31a5ceb2a9d`, `packages/coding-agent/src/core/refinement/refinement.ts:637-806,880-948` and `packages/coding-agent/src/core/agent-session.ts:8046-8133,8158-8266`. Search method/query: exhaustive control-flow reading from plan/normalize through per-edit validation, apply, save, audit and prompt rebuild, looking for an evaluator of factual correctness, callable behavior or realized improvement whose result is required before admission/use. Only structural/current-baseline checks are required. An extension may veto/supply a proposal, but no installed checker is evidenced. This bounds the absence to built-in admission; it does not rule out arbitrary external user tests. Without such acceptance, later storage and prompt use are not post-acceptance lifecycle integration.

### Behavioral-authority paths

BAP-1 — User/current system prompt and history to CMP-3, model request channel, instruction and advisory/evidential force, current and subsequent assembled turns. Delivered content is wired; behavioral activation is uninspected. SRC-1 `packages/agent/src/agent-loop.ts:472-499`.

BAP-2 — Validated tool name/arguments and optional hook decision to the tool executor, dispatch channel, enforcing admission force, one call. This licenses execution under the host's authority, not truth of tool output or confinement of nested Python actions. SRC-1 `packages/agent/src/agent-loop.ts:779-817`.

BAP-3 — Parent task message to a child model, custom parent message in the child's session, instruction force, admitted task and later visible history. Child results/notices to parent model carry advisory/evidential and lifecycle information, not truth acceptance. SRC-1 `packages/coding-agent/src/core/agent-session.ts:10433-10477`.

BAP-4 — Recovery journal to supervisor, identity/status lookup, enforcing replay refusal or recovery hold, duplicate request/recovery interval. Operational authority only. SRC-1 `packages/coding-agent/src/modes/daemon/daemon-supervisor.ts:1411-1431,3198-3248`.

BAP-5 — Retained schedule prompt to target session/model, due-job dispatch through follow-up/steering, instruction and routing force, scheduled invocation. SRC-1 `packages/coding-agent/src/modes/daemon/daemon-mode.ts:1777-1843`.

BAP-6 — mutable supplemental state admission. Proposer: current session model, or configured pre-refine extension. Decider: optional model auto-review for whether to run, followed by deterministic per-edit validation and conflict check. Veto: extension `skip`, cancellation/disposal, invalid edit fields, reserved base prompt ID, missing/duplicate target, changed baseline. Destination: scoped JSON state, audit append, then model system-prompt supplement. Rollback creates reverse edits from prior before/after images and reuses application checks; it is not automatic measured-regression recovery. Direct kernel CRUD is a separate admission path. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:673-844,892-903`; `packages/coding-agent/src/core/agent-session.ts:8091-8132,8170-8238`; `prime-agent-runtime/src/rlm/harness.py:345-424`. Conclusion status: wired.

For BAP-6, consumer/channel/force/horizon clarification: the per-edit controller consumes validation and baseline results with enforcing force for that mutation; later model consumers receive retained supplemental entries through the system prompt as instructions, evidence and routing hints across the chosen local/global horizon. Actual behavioral activation is uninspected.

BAP-7 — Automatic review decision to refinement controller, shouldRefine result channel, enforcing opportunity/admission force, one eligible checkpoint. Planner's review invocation is not an independent answer oracle. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:963-1011`; `packages/coding-agent/src/core/agent-session.ts:7871-7891`.

BAP-8 — Quality-gate command outcome to autonomous controller, process status channel, enforcing stop/retry force, current bounded run. Failure text then reaches the model in a generated user-role continuation with instruction and evidential force for repair. This does not establish a correct diagnosis or complete criterion. SRC-1 `packages/coding-agent/src/core/autonomous.ts:196-251,284-367`.

BAP-9 — Expected improvement and retained entry fragments to later session model, supplemental system-prompt channel, advisory/instruction/routing force, local session or future global consumers. A prediction's label grants no epistemic authority. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:429-519,791-800`; `packages/coding-agent/src/core/agent-session.ts:8237-8238`.

## Runtime account

A normal interactive client attaches through the local daemon to a session worker. The client owns presentation; the worker/session continues independently of that connection. Session identity selects retained history and configuration, credentials resolve the selected model, and ipython is the default active tool in the SDK. A prepared user action commits messages and extension-adjusted context, the loop streams a provider response, validates requested tools, runs cells and returns tool output to the next model call. Steering is drained at turn boundaries, follow-up after pending tool/steering work, and continuation after follow-up. A model error, abort or configured stopping rule emits a terminal event; a final response can still trigger configured continuation. Session retention and read-back are distinct routes below. SRC-2 `packages/coding-agent/docs/architecture.md:3-86`; SRC-1 `packages/coding-agent/src/core/sdk.ts:145-209,235-238,277-344`; RTE-1 through RTE-4.

Material alternatives are direct SDK/in-process sessions, RPC/print clients, scheduled and other-agent input, recursive child sessions, extension/custom tools, and Python imports/shell/subprocess/direct-service calls. Inspected daemon and child controls apply where those paths enter their enforcement points. A single exposed Python tool is a broad effect surface, not a narrow filesystem grant. Provider-native tools and arbitrary third-party extensions were not traced; they cannot inherit a blanket guarantee from the ordinary tool dispatcher.

Four forcing cases were traced statically:

1. **Disconnect or ambiguous command after a worker failure:** RTE-2 distinguishes a recorded response from pending uncertainty. It refuses blind replay and leaves interrupted work on hold; effects that occurred before failure may remain.
2. **Child task exceeds recursion depth or completes without replying:** RTE-3 rejects excess depth at the host and distinguishes spawn acknowledgment, child completion and an explicit result message. A fallback terminal notice does not certify successful task execution.
3. **New instruction/refinement would change later work:** the integrated refinement route checks edit structure and records state changes/rollback, while keeping the model's proposed benefit separate from observed effect.
4. **Autonomous model stops while an objective is unfinished or its gate fails:** the integrated gate/continuation routes decide whether another turn, stop, or failure state follows. A configured command supplies only its own test domain.

For product changes, the model proposes Python/file actions and the tool/OS executes them; no generic semantic veto precedes every admitted external effect. For capability changes, users or executable code propose packages/registrations and RTE-5 admits supported structure. For retained memory changes, the specialist's records below distinguish proposal, admission, deletion and rollback. Binary distribution updates are outside inspected implementation coverage. These are separate admission mechanisms; the refine guarantee does not cover unrestricted project/source edits.

Operating mode is open coding/research requests, with optional persistent goals, schedules and bounded autonomous continuation. User-defined verification commands can support bounded tasks or evaluations, but an inspectable curriculum or supplied expected-answer corpus is not established merely by the repository's research positioning. Oracle access is recorded on the gate/refinement routes: the model's own judgment is not independent reference-answer access. No actual run supplied an expected answer, candidate outcome or intervention comparison.

The memory-route audit below supplements the shared records without redefining them. All actual activation/benefit remains uninspected; successful delivery is the strongest supported implementation inference.

| Routes | Immediate return and later consumer | Delegated visibility and selector | Invalidation/recovery and effect limit |
|---|---|---|---|
| RTE-7 | Assembled context to caller; automatic history push to next model invocation | Same mechanism per child; branch leaf/parent and first-kept entry matching selects delivered parts | Branch changes/latest compaction change context; persistence-disabled/buffered history limits later recovery; no semantic endorsement |
| RTE-8, RTE-9 | Summary result then append/rebuild supplies later model context | Each session/branch owns summary; configured token cut/branch destination selects input and output placement | Extension veto/replacement, cancellation or generation failure precede normal append; summaries can lose qualifications; raw log differs from active context |
| RTE-10 | Per-edit result and bounded rebuilt prompt; later model catalog consumption | Scoped local/global stores, first six sorted entries per kind, five recent events; local parent entries do not automatically become child-local state | Invalid/changed targets reject per edit; inverse edits recover stored content; audit failure after save may prevent normal refresh; modeled benefit untested |
| RTE-11 | Execution/snapshot status and restore notice; later kernel automatically receives serialized values; model can request inspection | Chosen session artifact path selects payload; child has separate artifact path; name manifest is not complete value delivery to model | Failed/skipped/corrupt values and pruning may lose state; best effort revival, trusted local deserialization; no behavioral activation proof |
| RTE-12 | Requested complete entry/list returns to kernel agent; host prompt reuse follows rebuild | Exact kind/ID for requested pull; explicit local/global addressing; rebuild catalog is separate coarse push | Modification-time refresh; direct CRUD differs from audited refiner and has no demonstrated mandatory immediate prompt-refresh callback |
| RTE-13 | Roster returns child identifiers; reopening a saved child reuses its own history/kernel/harness | Child ID/session path; shared global store, distinct local state | Deleted/disposed or unavailable child state limits reopening; no merge or guarantee of correct continued work |
| RTE-14 | Requested skill body or command invocation; metadata catalog supplies automatic routing hints | Scope/availability-based catalog push; explicit skill invocation/file request is requested read, not additional identifier-based push | File edits/reload change future availability; package authorship/review afforded, arbitrary implementation behavior uninspected |

For RTE-15 through RTE-25, the stage audit inherits the named local/global store and model consumer of RTE-10: selection/auto-review/proposal stages return transient input or JSON to the controller; structural check and disposition return per-edit permission/results; retention returns persisted state/audit; prompt stages supply a bounded view for future turns; rollback returns inverse edits and receipts. Only the retained outputs have later read-back. Rejection, cancellation, stale branch/baseline, audit failure and changed-entry conflicts limit the corresponding stages; no stage establishes external-effect rollback. Delegation sees global state and its own local store as in RTE-13. Automatic review selects whether to plan, not retained memories by semantic relevance.

For RTE-26 through RTE-29, the gate runner returns command status/output to the controller, which stops or supplies a user-role repair continuation within configured budgets. Failure state is selected by command and compared workspace snapshot; it is cleared on pass or replaced by a new failure, and affects later attempts in this autonomous run. No separate durable memory-learning route is inferred from that ordinary control state. Children are not given a distinct criterion or expected-answer store by these functions. Stop, abort, timeout and retry limits govern execution; repair remains model-chosen, and no rollback or complete task verdict follows from a command result alone. See BAP-8.

Execution preflight disposition: **no dynamic check planned**. Considered provider-backed prompt/refine runs, IPython/subagent execution, daemon crash injection and autonomous gate execution. Static inspection resolves the route/enforcement questions asked here; dynamic checks would require target packages, runtime configuration, services/credentials and a controlled fixture without establishing general efficacy. None was attempted, so there is no observed-run capsule and no negative finding from non-execution.

## Lens scoping

### Memory/context scope

Full depth. Trigger: SRC-2 `README.md:41-52,91-95`, CLM-1 and CLM-2. Inspected memory objects and write/read-back routes are the accepted specialist records below, at the same full commit. Persistent variables, compaction, session branches, mutable harness entries and retained child state make a brief inventory insufficient. The profile's explicit memory boundary controls aggregate classifications; ordinary control-plane persistence and static shipped instructions are not silently equated with accumulated memory.

### Epistemic scope

Full depth. Trigger: CLM-1 through CLM-3 and the implemented refinement, summary and quality-gate families. Assessed question: what content is proposed, checked, admitted, retained and consumed, and what those transitions warrant. Runtime/tool/context routes RTE-1 through RTE-6 are classify-only where they do not check truth. The lens covers refinement and gate evidence in depth; arbitrary user programs, external references, provider internals and unobserved research evaluations remain outside its warrant.

## Lens outputs

### Memory/context lens

Prime Agent maintains several distinct continuities. Conversation history is a parent-linked append log; later model context is assembled from a selected branch, its latest summary and retained messages. The IPython kernel preserves another working context that can survive conversational compaction, with best-effort serialization for later process revival. Supplemental harness entries form a third store: they survive outside token history, can be rewritten by a refiner, and enter future prompts through a compact catalog. These are wired mechanisms, not evidence that retained content helps. See OBJ-1 and RTE-7 through RTE-11.

Selection is largely structural. History assembly follows exact entry identities. Harness prompt assembly sorts entries by path/title/ID and includes only the first six of each kind, truncating content to 180 characters, plus five recent refinement events. Full entries remain explicitly accessible through the kernel API. Consequently an entry can be durably available without its full instructions reaching the model, and a newly created entry may fall beyond the catalog cutoff. The refiner itself sees another bounded view: up to 40 entries per kind, 240-character content fragments, 20 audit records, and an 80,000-character conversation suffix; the automatic review uses 40,000 characters. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:26-28,429-442,465-519,522-561,906-919,963-999`.

The strongest admission checks protect shape and concurrency, not truth. Refinement validates operation kinds, IDs and skill contracts, forbids its reserved base-prompt target, and rejects edits whose target changed since planning. Extensions can skip the refiner or supply its proposal. No required human approval or executed usefulness/faithfulness test appears between the built-in proposal and save. Moreover, the Python CRUD path uses a different, weaker validation surface. The label `outcome` in a refinement event stores the model's expected outcome, not a measured result. See BAP-6 and CLM-4.

Acquisition precedes learning. OBJ-1 records the conversation and tool results; OBJ-10 keeps values created or loaded by code. Neither raw recording nor value serialization alone is trace learning. RTE-8 and RTE-9 transform those conversation records into retained continuation guidance and have proven static links to later model context. Both therefore qualify independently of RTE-10. The compaction prompt explicitly allows a session goal containing multiple tasks, so local persistence cannot be normalized to per-task merely from a session ID. SRC-1 `packages/coding-agent/src/core/compaction/compaction.ts:417-448`.

Compaction preserves a recent message suffix, defaulting to 20,000 estimated tokens and reserving 16,384 tokens at the context boundary. Its main summary output budget is 80% of the reserve; the split-turn alternative also generates a separate prefix summary. Branch summarization budgets input against the selected model's context window minus its reserve, walks newest-first, and allows 2,048 output tokens. These are selection and compression policies, not semantic completeness guarantees. SRC-1 `packages/coding-agent/src/core/compaction/compaction.ts:106-113,206-209,352-386,508-519,673-745`; `packages/coding-agent/src/core/compaction/branch-summarization.ts:151-206,248-285`.

Refinement is online adaptation: it reads the ongoing trajectory, plans without changing the store, waits for the session's apply boundary, saves entries and rebuilds the prompt. Local scope is enforced through the target store; global scope is explicit. The instruction that globally retained facts must name their project is a model policy, not a project-matching retrieval filter. Automatic approval invokes local refinement without setting the global option. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:140-148,906-919`; `packages/coding-agent/src/core/agent-session.ts:7842-7846,8041-8090,8170-8224`.

Maintenance varies by entry route. Refiner updates increment versions; deletes preserve before images in the audit, allowing inverse edits. Those support evolve and invalidate. Summary generation supports consolidate, and prompts to derive reusable policies from failures afford synthesize; no observed successful synthesis is claimed. ID collision handling is not semantic deduplication. Choosing a global file is not a tier-promotion operation. Kernel compaction can remove values above the per-variable cap, supporting decay as forgetting; ordinary snapshot skips do not necessarily remove the live value. The default caps are 16 MiB per value and 256 MiB aggregate. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:125-152,716-844`; `packages/coding-agent/src/core/kernel/state-snapshot.ts:10-13,108-187`.

Rollback is corrective writing, not restoration of a whole immutable state snapshot. Reverse edits can fail individually if current entries no longer permit their operation, and before/after content is applied through normal versioned edits. State saving occurs before audit append and prompt rebuild; an audit append failure can therefore leave persisted edits without a completed normal refresh/report sequence. Python writes resynchronize using modification time but write JSON directly, whereas the TypeScript save uses a temporary file and rename. Neither mechanism by itself proves a transaction spanning concurrent processes, state and audit. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:345-358,716-844`; `packages/coding-agent/src/core/agent-session.ts:8194-8238`; `prime-agent-runtime/src/rlm/harness.py:187-197,285-301`.

History replay is push into the model: branch identity actually selects delivered parts. Summary generation is an earlier write; semantic judgment about what to put in that summary does not make later branch assembly semantic retrieval. The operative IDs and preserved source log make inspection possible, but generated statements do not receive per-claim evidence bindings. RTE-7 through RTE-9 establish delivery rather than faithful use.

Harness prompt supply is coarse push. Local/global scope selects stores; catalog sort and entry limits choose visible fragments. The refiner receives a larger but still bounded catalog and recent history. A kernel agent can explicitly request a whole harness entry through RTE-12, which is pull. Upstream operator scope selection does not turn every downstream automatic catalog load into pull. Refiner model judgment is about proposed writes; no query-dependent semantic selector is implemented by the formatter. SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:429-561`; `prime-agent-runtime/src/rlm/harness.py:403-436`.

The kernel receives restored values, while the model receives names and failure notices. A successful revival does not establish that the model inspected or used a value. Skipped values, missing libraries, corrupt snapshots and changed module environments can prevent complete revival. The loader calls dill on the outer payload and each value without a content-trust classifier or integrity signature in the inspected route. This is a trust in the local snapshot file, not a guarantee about arbitrary imported objects. SRC-1 `packages/coding-agent/src/core/kernel/state-snapshot.ts:118-130,203-243`; `packages/coding-agent/src/core/agent-session.ts:7271-7296`.

A retained child supplies later work through its own history, local harness and namespace. The parent roster is access metadata; it is not a merged transcript or automatic transfer of all local lessons. Shared global entries can influence children through ordinary prompt assembly, while local entries require explicit communication or other explicit access. Exact delivery of follow-up messages is left to the parent's recursive runtime account; no benefit is inferred from rehydration alone. See RTE-13.

Human editing and adoption have two concrete surfaces: focused refine instructions/rollback requests, and separately authored installed skill files with reload. Harness files are ordinary JSON and direct Python CRUD is exposed to the kernel agent, but such writes should not be mistaken for a human-reviewed promotion workflow. The skill creator's manual verification instructions establish an afforded review practice; they are not an automatic clearance gate on all memory. See RTE-12 and RTE-14.

The fourteen-axis profile is an aggregate of the explicitly selected memory subset, not a classification of every persistent runtime file. Files plus in-memory state describe its storage. Parent pointers and maps do not add graph or KV service substrates. Imported content, authored entries and skills, trace-derived summaries/refinements, and mechanically generated manifests/addressing structures explain the lineage union. The weakest evidence basis is afforded where the union includes documented explicit authoring or use.

Representational form and behavioral authority remain not-determinable because OBJ-10 retains arbitrary executable/data payloads. Known natural-language and symbolic portions do not justify silently dropping that part. Model weights used by CMP-3 are outside memory storage: these paths call an existing provider model and do not update it. Conversely, it would also be unsupported to rule out arbitrary payload forms merely because the snapshot filename ends in dill. These uncertainties do not block a complete source-bounded report.

The qualifying trace-learning routes are precisely RTE-8, RTE-9 and RTE-10. They use conversation/tool traces, operate online, and retain text plus structured contracts/access metadata; copying kernel state and independent skill authorship do not extend that qualifying set. Their scope cannot be reduced to per-task: compaction explicitly tolerates multiple tasks, branch navigation has no task boundary, and global refinement is meant to carry reusable lessons across future sessions. The source establishes intended reuse horizons, but not a complete enforced taxonomy across every included continuation branch. Hence learning_scope is not-determinable rather than an invented complete union.

No retained execution evidence establishes whether recalled content changes behavior correctly. Faithfulness is therefore not-determinable in this source-only commission. Expected-outcome prose, model review gates and structural tests would not independently support a yes. Curation and read-back values denote implemented or afforded operations, never observed quality.

### Epistemic lens

#### Source-and-claim boundary

See SRC-1/SRC-2, the frozen Boundary and evidence and Epistemic scope sections. This pass assesses refinement and configured autonomous gates, annotating CLM-2 and CLM-3. Ordinary tool execution, history, scheduling and recovery are classify-only: they can transport statements or enforce operations without granting general truth authority. Compaction/branch transformation is addressed below with the integrated memory evidence. No actual candidate, task gate, independent expected answer or interventional comparison was supplied. Excluded arbitrary programs, provider internals and external verifiers prevent system-complete epistemic conclusions.

#### Epistemic-object inventory

Generic identities, forms, lineage and consumers remain in the canonical object records; this table records the epistemic parts.

| Canonical part | Candidate truth-apt content and limit | Evidence |
|---|---|---|
| OBJ-15 | Facts, preferences, decisions, failures, and outcomes; may preserve known information or conjecture a reusable lesson. | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:134-151`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:637-806`, `packages/coding-agent/src/core/refinement/refinement.ts:904-948`. No actual candidate instance; transformation of a particular entry is indeterminate. |
| OBJ-16 | Prediction that proposed edits will improve future behavior. This is ampliative, since trajectory alone does not entail future improvement. | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:157-158`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-805`, `packages/coding-agent/src/core/refinement/refinement.ts:508-512`. No measured observation is substituted for this prediction. |
| OBJ-17 | Narrow behavioral policy. No necessary truth-apt output for this part. | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:135`, `packages/coding-agent/src/core/refinement/refinement.ts:146-147`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:673-806`. Reserved base-prompt ID is blocked; policy usefulness is not mechanically validated. |
| OBJ-18 | Delegation policy. No necessary truth-apt output for this part. | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:138`, `packages/coding-agent/src/core/refinement/refinement.ts:146-147`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:454-487`. No subagent performance test in examined refinement route. |
| OBJ-19 | Claim about what callable exists and how to invoke it; reusable procedure description. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:693-711`; SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:137`; `README.md:91`. Validation does not import or execute the referenced function. |
| OBJ-20 | Bit is a decision to spend effort refining; rationale may assess future usefulness. Neither is a completed-edit verdict. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:951-1011`; `packages/coding-agent/src/core/agent-session.ts:7871-7891`. Rationale content is indeterminate without candidate instance; decision itself is non-truth-apt. |
| OBJ-21 | Whether a particular edit was applied in this invocation, and prior/next entry content. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:716-808`; `packages/coding-agent/src/core/agent-session.ts:8221-8236`. Receipt licenses mutation provenance, not truth or usefulness of entry content. |
| OBJ-22 | Criterion for continuing/stopping the current autonomous run. No necessary truth-apt candidate output in the command configuration itself. | SRC-1 `packages/coding-agent/src/core/autonomous.ts:57-61`, `packages/coding-agent/src/core/autonomous.ts:106-132`, `packages/coding-agent/src/core/autonomous.ts:284-319`. Gate internals and task-specific coverage unavailable. |
| OBJ-23 | Recorded command success/failure in the actual process environment. Any broader task claim depends on what command checks. | SRC-1 `packages/coding-agent/src/core/autonomous.ts:284-370`, `packages/coding-agent/src/core/autonomous.ts:374-424`, `packages/coding-agent/src/core/autonomous.ts:481-569`. Process output is externally acquired; return-code-to-status mapping is domain-limited derivation. No observed run available. |

#### Authority-route ledger

| Route | Function | Architectural status | Object; content/update relation | Target before evaluator; activation/timing; possible result | Evidence; claim; mismatch |
|---|---|---|---|---|---|
| RTE-15 | content transformation | implemented | OBJ-1 → refinement input; truth-apt transformation: non-ampliative reshaping | Conversation/context passed through conversion, serialization and suffix slicing; when review/planning starts; bounded text/overviews. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:522-565`, `packages/coding-agent/src/core/refinement/refinement.ts:906-919`, `packages/coding-agent/src/core/refinement/refinement.ts:974-989`; CLM-2; no fidelity proof. |
| RTE-16 | check/evidence production | implemented | OBJ-20; truth-apt transformation: indeterminate for rationale; non-truth-apt decision output | Whether checkpoint contains material useful for future turns; selected model instructed to reject noise/unsupported hypotheses or injected reviewer; before automatic planning; boolean plus rationale/instructions, error. | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:175-187`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:963-1011`; `packages/coding-agent/src/core/agent-session.ts:7871-7891`; CLM-2; no independence from source model/trajectory established. |
| RTE-17 | operational admission/selection/consumption | implemented | OBJ-20; no content change | Whether automatic refinement may run; controller consumes shouldRefine, settings, cooldown, root/persistence eligibility, branch generation and activity; approve, skip, defer, invalidate. | SRC-1 `packages/coding-agent/src/core/agent-session.ts:7496-7498`, `packages/coding-agent/src/core/agent-session.ts:7740-7868`, `packages/coding-agent/src/core/agent-session.ts:2256-2329`, `packages/coding-agent/src/core/agent-session.ts:2365-2440`; `packages/coding-agent/src/core/settings-manager.ts:883-899`; CLM-2; opportunity approval is not candidate acceptance. |
| RTE-18 | content transformation | implemented | OBJ-15/OBJ-16/OBJ-17/OBJ-18/OBJ-19; OBJ-15/OBJ-19 truth-apt transformation: indeterminate; OBJ-16: ampliative conjecture; OBJ-17/OBJ-18: non-truth-apt policy/content update: reusable instructions | Proposed edits to permitted harness entries; selected session model given trajectory, state and history, optional user instructions; manual/agent request or RTE-17 approval; JSON proposal, empty edit list, error. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:880-948`; `packages/coding-agent/src/core/agent-session.ts:8046-8133`; SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:123-172`; CLM-2; no measurement. |
| RTE-19 | operational admission/selection/consumption | implemented | Proposed refinement round; no content change for skip, otherwise replacement proposal content with transformation indeterminate | Conditional extension. Pending non-rollback plan; extension handler can skip or supply normalized proposal before default model planner; skip, supplied proposal, default model call. | SRC-1 `packages/coding-agent/src/core/agent-session.ts:8091-8117`; CLM-2; hook can replace proposer, no inspected extension evaluator. |
| RTE-20 | check/evidence production | implemented | OBJ-15/OBJ-17/OBJ-18/OBJ-19 edit envelope; no content change | Action/kind, immutable reserved ID, required fields, Python reference strings, existence and planning baseline; deterministic validation immediately before each mutation; error or admissible edit. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:637-789`; CLM-2; checks establish structure/freshness, not semantic truth or callable behavior. |
| RTE-21 | disposition/acceptance | implemented | OBJ-21 and edits; no content change in disposition itself | Operational disposition. Each proposed edit; application consumes RTE-20 result; invalid/conflicting edits skipped, eligible edits applied independently. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:716-789`; CLM-2; no epistemic acceptance of memory/prediction. |
| RTE-22 | retention | implemented | OBJ-15/OBJ-16/OBJ-17/OBJ-18/OBJ-19/OBJ-21; no content change beyond structured recording | Applied state and receipt; save current scope state, append global history for global edits, append session audit/outcome; after application. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:345-399`, `packages/coding-agent/src/core/refinement/refinement.ts:791-808`; `packages/coding-agent/src/core/agent-session.ts:8221-8236`; CLM-2; retained prediction remains prediction. |
| RTE-23 | behavior/policy adaptation | implemented | OBJ-15/OBJ-17/OBJ-18/OBJ-19 consumed; non-truth-apt policy/content update: changed supplemental context/instructions | Future model context; prompt builder formats scoped entry overviews, CMP-1 rebuilds prompt after application; changed available instructions/routing. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:429-499`; `packages/coding-agent/src/core/system-prompt.ts:108-109`, `packages/coding-agent/src/core/system-prompt.ts:147-148`; `packages/coding-agent/src/core/agent-session.ts:8237-8238`; CLM-2; behavioral influence does not establish adherence or benefit. |
| RTE-24 | operational admission/selection/consumption | implemented | OBJ-16 displayed in history; no content change to prediction's proposition | Expected future improvement; event constructor maps expectedOutcome to outcome and overview renders 'outcome'; subsequent prompt construction. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-800`, `packages/coding-agent/src/core/refinement/refinement.ts:508-512`; CLM-5; prediction label can look like observation. |
| RTE-25 | lineage/freshness/recovery | implemented | OBJ-21 prior snapshots → inverse edits; truth-apt transformation: non-ampliative reshaping of prior recorded content | Named earlier applied refinement; rollback reconstructs inverse edits from before/after snapshots, reuses application checks; restore/delete entries or reject unsupported inverse edit. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:813-845`, `packages/coding-agent/src/core/refinement/refinement.ts:892-904`; `packages/coding-agent/src/core/agent-session.ts:8171-8220`; CLM-2; recovery is not retesting. |
| ABS-1 | check/evidence production | no route found within boundary | Truth of OBJ-15/OBJ-19 or realized OBJ-16; no content change | Post-proposal factual accuracy, callable behavior, or measured improvement; no distinct evaluator/criterion-consuming test found between planning and applying in inspected functions. | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:637-806`, `packages/coding-agent/src/core/refinement/refinement.ts:880-948`; `packages/coding-agent/src/core/agent-session.ts:8046-8133`, `packages/coding-agent/src/core/agent-session.ts:8158-8266`; CLM-2; scoped absence only. |
| ABS-1 | lifecycle integration | no route found within boundary | Accepted ampliative OBJ-16, or any established ampliative OBJ-15 lesson; no content change | Connection/use after evidence-consuming epistemic acceptance; retention and prompt use exist, but no such prior acceptance found in inspected refinement path. | Same boundary as ABS-1, plus RTE-22, RTE-23; CLM-2; do not rename retention integration. |
| RTE-26 | check/evidence production | implemented | OBJ-22 → OBJ-23; acquired process outputs plus entailed result classification in exit-code domain | Conditional configuration. Configured command against current task cwd; host shell/process runner, sequential commands until first failure; zero exit without error/timeout passes a command, other result fails. | SRC-1 `packages/coding-agent/src/core/autonomous.ts:273-348`, `packages/coding-agent/src/core/autonomous.ts:481-569`; CLM-3; gate internals/expected answer unknown. |
| RTE-27 | disposition/acceptance | implemented | OBJ-23 aggregate; no content change | Run-control decision. Current autonomous run's configured command criteria; code consumes command results; all passed stops continuation, failure requests retry while budget remains, exhausted retries/limits stops without success. | SRC-1 `packages/coding-agent/src/core/autonomous.ts:227-251`, `packages/coding-agent/src/core/autonomous.ts:284-348`; CLM-3; epistemic license limited to named commands' scope. |
| RTE-28 | behavior/policy adaptation | implemented | OBJ-23 failure → next-turn instruction; non-truth-apt policy/content update: repair/continue instruction | Next ordinary model turn; continuation builder embeds failed command, attempt, output and repair instruction in user-role message; model receives new repair request. | SRC-1 `packages/coding-agent/src/core/autonomous.ts:196-223`, `packages/coding-agent/src/core/autonomous.ts:350-367`; `packages/coding-agent/src/core/agent-session.ts:3331-3347`; CLM-3; repair success not guaranteed. |
| RTE-29 | lineage/freshness/recovery | implemented | OBJ-23 prior failed snapshot; no content change | Whether same failed command should be rerun; equality of scoped Git status, diff and untracked hash; unchanged snapshot suppresses process rerun and increments attempt. | SRC-1 `packages/coding-agent/src/core/autonomous.ts:294-310`, `packages/coding-agent/src/core/autonomous.ts:370-424`; CLM-3; source changes outside snapshot scope and environmental changes not modeled. |

Authority details (fields: implemented force; epistemic authority and scope; operational authority; behavioral-authority path; gap/limit):

- **RTE-15:** Supplies evidence context without truth approval. Warrant from original user/tool/model statements is unknown, and selection drops material. Reviewer/planner consume text through a user-role model input, informational force for that call. Overviews cap current entries at 40 per kind and content at 240 characters; history supplies the last 20 refinements and expected outcomes. Neither original evidence completeness nor semantic preservation of omitted context is guaranteed.
- **RTE-16:** Produces review judgment; RTE-17 supplies consequential force. Same configured model as session is the default, a distinct invocation rather than an independent oracle. No separate expected answer or external test access is supplied to this call. It can recognize recorded failure/correction evidence, but can also reason from the model's own trajectory. Its rationale warrants only an attributed model assessment.
- **RTE-17:** Enforcing scheduler decision for this checkpoint. Default auto-refine settings enable review every 25 assistant turns and after compaction with a 20-minute cooldown; automatic eligibility requires root RLM depth and a local persisted artifact directory. Disabling, cooldown, active work, branch invalidation, or negative review can prevent/defer a round. In serialized/headless mode a checkpoint consumes the exact background plan; stale branch generation is discarded. Public/explicit refine calls bypass this automatic opportunity review (SRC-1 `packages/coding-agent/src/core/agent-session.ts:7917-7963`, `packages/coding-agent/src/core/agent-session.ts:2603-2605`). No human approval or post-proposal vote is required by this path.
- **RTE-18:** The proposer is the selected model, except RTE-19 replacement or deterministic rollback. The prompt asks for small evidence-backed changes and describes validation in expectedOutcome; those are natural-language instructions. JSON normalization permits empty rationale and expectedOutcome. Planner has no tool loop or oracle call in the inspected function. Outputs are candidate declarations, predictions or instructions. They become consequential through RTE-20 through RTE-23, not through this generation alone.
- **RTE-19:** Extension is a conditional veto/replacement authority for this round, before normal planning. Supplied proposals still go through normalization/application. No invoked extension implementation was supplied, so there is no basis to credit independent checking or human oversight. Rollback skips this before-refine hook.
- **RTE-20:** Enforcing per-edit checks. The code blocks reserved `base_system_prompt`, malformed action/kind, absent required title/content, invalid skill reference fields, create collisions, missing update/delete targets, and an entry changed since planning. These results license only admissibility in the edit schema and a narrow concurrency condition. It does not establish referenced import existence, procedure correctness, relevance, or accuracy of a fact. Application also rereads state and waits for session quiescence (`packages/coding-agent/src/core/agent-session.ts:7984-8016`, `packages/coding-agent/src/core/agent-session.ts:8194-8220`). Freshness is not endorsement.
- **RTE-21:** Controller decides immediately, per edit; a proposal can partly apply. `applied: true` means mutation executed, not epistemic acceptance. There is no approval-stage candidate store requiring a human or independent reviewer before use. The operational scope is selected local/global target state. Local runs treat global entries as planning context and mutate the local store; global scope is an explicit option. The model is instructed to restrict global lessons, but cross-session generality is not a semantic validator criterion.
- **RTE-22:** State write uses temp-file rename; global refinement history and session audit are separate writes. The audit carries snapshots, scope, ID, rationale and prediction, not measurements. The outcome-message helper separately attempts session persistence and then appends the message in memory (SRC-1 `packages/coding-agent/src/core/agent-session.ts:8135-8151`). Save precedes later audit writes, so a later append failure need not mean no state changed. Consumer horizon is current local session or future global sessions as selected. Retention is operationally consequential through prompt reuse and rollback; it is not acceptance.
- **RTE-23:** CMP-1 adds compact harness descriptions through system-prompt assembly; text directs model to use relevant entries, inspect details as needed, and treat base prompt as immutable. This supplies advisory/routing instructions through a high-priority prompt channel; semantic compliance and actual improvement remain model-dependent. Prompt-policy edits directly adapt behavior without requiring a truth-apt lesson. Subagent specifications still require model composition/invocation; skill descriptions do not install or verify code. Local versus global state determines intended horizon; active-session cross-process refresh timing is outside this overlay.
- **RTE-24:** Same text prediction, changed label: `proposal.expectedOutcome` becomes `state.refinements[].outcome`, then renders as `outcome`. The future model consumes it in supplemental context. No measured result is inserted, and the separate planner history correctly labels it `Expected outcome`. This label discrepancy can obscure evidential status; no run evidence establishes that a model was misled.
- **RTE-25:** Caller names a refinement ID; code reverses applied edits and reconstructs earlier content, retaining rollback lineage. This permits undoing selected harness changes. It does not undo previous external actions, test restored policies, or infer that the old content is true. Baseline checks protect changes made during the current rollback plan; they do not prove that undoing an older edit preserves all later intentional edits.
- **ABS-1/ABS-1:** No enforcing check/acceptance/integration authority found for semantic quality in the named refinement implementation. Existing structural admission, recording, and prompt use must not be given that authority. External tests or later informal user judgment could supply evidence in a real deployment; none was supplied or inspected here.
- **RTE-26:** Host executes configured commands independently of the model's declaration of success. Warrant is zero-exit/error/timeout behavior of that command, in that environment, on that invocation. Whether it tests the intended task, accesses a hidden oracle, protects expected answers, or is writable by the working agent is not established by this runner. No read-only expected-answer boundary, holdout separation, or verifier independence should be inferred. Commands default to empty; autonomous mode defaults disabled (``packages/coding-agent/src/core/autonomous.ts:106-132``).
- **RTE-27:** Enforcing stop/continue authority, not certification of broad task success. A pass licenses completion only relative to configured command predicates if their meaning is warranted externally; their semantics are unavailable here. Failures permit another model continuation within budgets, while exceeding retry or resource bounds ends automatic continuation without truth approval. Retry exhaustion is `attempt > maxRetries`, so the initial attempt plus configured retries is allowed. There is no identified connection making a task gate an independent test of an individual harness refinement.
- **RTE-28:** Failure command, attempt and output (6,000-character prefix plus a truncation marker when needed; SRC-1 `packages/coding-agent/src/core/autonomous.ts:63`, `packages/coding-agent/src/core/autonomous.ts:581-586`) reach the model as a generated user-role continuation. This is directive repair feedback, not a verified diagnosis. The model chooses repairs; no runtime check here distinguishes fixing production behavior from changing tests or producing a blocker artifact. Parent retains full RTE-1 continuation arbitration; session code can suppress a stale continuation after intervening input.
- **RTE-29:** Enforcing rerun suppression with informational freshness scope, not new failure measurement. Equality excludes `verification`, `target`, `.vf-prime-agent`, `Cargo.lock`, `submission.tar.gz`, and `runner_args.log`; environment/time/service changes are also outside the comparison. If snapshot capture cannot establish equality, the optimization does not apply. Therefore “unchanged” is relative to this snapshot, not all inputs to the gate.

#### Per-object lifecycle disposition

**OBJ-16 — predicted improvement.** Relevant routes: RTE-15, RTE-18, RTE-22, RTE-24, ABS-1, ABS-1. Transformation: **ampliative conjecture**. Every observed candidate state below is **no instance observed**; prompt examples and type declarations are not candidate instances.

| Phase | Routes | Architectural status | Observed candidate state | Evidence and scope |
|---|---|---|---|---|
| Observation/anomaly | RTE-15, RTE-16 | implemented | no instance observed | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:906-919`, `packages/coding-agent/src/core/refinement/refinement.ts:974-989`. Trajectory selection and opportunity assessment; no actual anomaly evidenced. |
| Conjecture | RTE-18 | implemented | no instance observed | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:157-158`; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:927-948`. Future improvement prediction. |
| Derived consequence: validation suggestion | RTE-18 instruction | doctrine only | no instance observed | SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:158`. Asks for how to validate. |
| Derived consequence: checked derivation | ABS-1 boundary | no route found within boundary | no instance observed | SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:637-806`, `packages/coding-agent/src/core/agent-session.ts:8046-8133`, `packages/coding-agent/src/core/agent-session.ts:8158-8266`. Free-text suggestion is not an entailed consequence. |
| Test/evidence | ABS-1 | no route found within boundary | no instance observed | Same bounded implementation anchors. Structure checks do not test improvement; task gates lack individual-refinement linkage. |
| Acceptance | ABS-1 | no route found within boundary | no instance observed | Same bounded implementation anchors. Evaluator/criterion for measured improvement absent; intended use later behavior; accepted epistemic scope none established. RTE-21 only disposes edits operationally. |
| Lifecycle integration | ABS-1 | no route found within boundary | no instance observed | RTE-22 retention and RTE-24 exposure lack preceding epistemic acceptance. |

Missing phase/evidence: a candidate-specific predicted effect and test criterion; realized measurements; acceptance decision consuming them; post-acceptance integration; independent contrast if attributing improvement to the refinement.

**OBJ-15 — declarative memories.** Relevant RTE-15, RTE-18, RTE-20 through RTE-23, RTE-25 and ABS-1. Transformation **indeterminate**: possible preservation/reshaping of a stated fact, entailed derivation from premises, or ampliative generalization from observed failures. Provenance records model rationale and before/after state, not a compulsory claim-to-message evidence link. Implemented checks cover structure, identity and planning freshness; retention and use occur without a semantic acceptance stage. Current warrant: a generated/edited entry whose truth is not established by this implementation. Decide classification from an actual input/output pair plus warranted premises or source evidence. No instance observed; do not fabricate a discovery lifecycle for all memories from their type label.

**OBJ-19 — skill interface description.** Relevant RTE-18, RTE-20 through RTE-23, RTE-25 and ABS-1. Transformation **indeterminate**: can copy installed documentation, derive an invocation description, or invent a callable/behavior claim. Source lineage is trajectory/state and proposal rationale. Python-shaped fields are checked but existence and behavior are not tested. Warrant requires actual candidate and installed module/docs/execution evidence; none supplied. No instance observed.

**OBJ-20 — automatic review rationale.** Relevant RTE-16, RTE-17. Transformation **indeterminate** for the rationale's truth-apt parts: a rationale may restate a correction or conjecture future reuse. The boolean disposition itself is non-truth-apt. Actual input/output and the asserted proposition are required to classify. Implemented model review and controller consumption establish operation scheduling, not accepted knowledge. No instance observed.

**OBJ-1 input slices.** Relevant RTE-15; transformation **non-ampliative reshaping** by selecting/formatting retained context; discovery lifecycle **not applicable**. Warrant of original messages is neither created nor checked, and truncation can remove qualifications or contrary evidence. Source lineage remains conversation input at the interface level, with no inspected mandatory proposition-level evidence binding.

**OBJ-21 application receipt.** Relevant RTE-20, RTE-21, RTE-22, RTE-25; transformation **entailed derivation** within program state accounting: status and snapshots are generated from checks and mutations. Discovery lifecycle **not applicable**. Warrant covers program's branch/mutation bookkeeping, not content truth, disk/audit all-or-nothing semantics, or later effects. Implementation inspection alone does not establish that a receipt was produced in a real run.

**OBJ-23 quality-gate output/result.** Relevant RTE-26, RTE-27, RTE-28, RTE-29. Process stdout/stderr are **acquisition/import**, with source identity the configured command; truth of arbitrary output is unknown. Result classification is **entailed derivation** within the inspected exit/error/timeout predicates. Discovery lifecycle **not applicable** to those signals. No task artifact was supplied whose broader claim could be accepted under a known gate. Result authority is predicate scope only; retry suppression is a policy decision from a scoped snapshot, not acquisition of a new execution result.

No lifecycle record for OBJ-17: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-18, RTE-21, RTE-23, RTE-25.

No lifecycle record for OBJ-18: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-18, RTE-21, RTE-23, RTE-25.

No lifecycle record for OBJ-22: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-26, RTE-27.

The typed parts OBJ-24 through OBJ-30 make heterogeneous envelopes explicit without changing their parent identities: OBJ-23 is gate-result state, OBJ-20 is the review-result envelope, and OBJ-10 is the namespace/snapshot pair. Acquired gate output OBJ-24 has unknown source truth; derived status OBJ-25 is entailed only within exit/error/timeout predicates; snapshot OBJ-26 is mechanically compiled freshness evidence, with limited equality scope. OBJ-28's rationale is indeterminate, while OBJ-27 is a non-truth-apt operational decision. OBJ-29 remains opaque; OBJ-30's symbolic names/status do not resolve its content. These distinctions constrain the aggregate profile and the ledger's authority claims.

For the classify-only runtime/memory inventory: OBJ-1 transports acquired user/tool claims and generated assistant candidates whose individual truth is not established. OBJ-2's executed code is a program/policy, while its returned stdout/results are acquired evidence whose meaning depends on the executed computation. This permits external tests and potential derivations but does not establish a general answer oracle. OBJ-7/OBJ-8 summaries are intended non-ampliative reshaping; actual preservation versus omitted qualifications or invented claims is indeterminate without source/output instances. OBJ-9/OBJ-11 are containers whose content parts are separately disposed above; OBJ-12 is addressing metadata; OBJ-13 is authored procedural/code material with opaque behavior; OBJ-14 is a displayed model summary without established later model use. No observed candidate lifecycle is inferred from any of these type declarations. Relevant evidence and uncertainty remain on their shared records.

No lifecycle record for OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-12, OBJ-22, OBJ-26, OBJ-27 or OBJ-30 as operational configuration/addressing/control parts: no candidate ampliative truth-apt output is established for those parts. Their relevant direct-control, recovery or adaptation routes are RTE-2, RTE-3, RTE-5, RTE-6, RTE-13, RTE-17, RTE-26 and RTE-29. OBJ-5 records derive operation status within their journal domain; they do not license truth of an underlying task. Static contents and opaque programs do not warrant a fabricated discovery lifecycle.

#### System-claim versus route comparison

| Claim | Claim identity/source layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limit | Supported conclusion; mismatch/unknown |
|---|---|---|---|---|---|---|
| CLM-2 | See CLM-2; SRC-2 `README.md:42`, `README.md:48`, `README.md:91` | Planner instructions require focused evidence-backed edits and name expected validation; immutable base prompt and local default are stated. | RTE-15 through RTE-25 and ABS-1 for refinement slice only | None supplied | No before/after comparison, controlled intervention, candidate-linked measurement, or independent verifier of proposed lesson. | Implemented trajectory-based model proposal, structural/freshness admission, durable scoped edits, and snapshot-based undo. This supports capacity to revise reusable context; actual improvement and evidence-backed truth of an admitted lesson are unestablished. Parent owns remaining continuity/subagent claims. |
| CLM-3 | See CLM-3; SRC-2 `README.md:96` | README explicitly limits pass to the gate and distinguishes budget exhaustion from success. | RTE-26 through RTE-29 | None supplied | No task gate definitions/expected answers, gate-protection boundary, or task outcomes. An independent process is not necessarily an independent semantic oracle. | Implemented exit-code-gated continuation and repair feedback support the narrow public claim. Gate criteria and their completeness remain configuration-dependent. |
| CLM-5 | Internal label: expectedOutcome stored/rendered as outcome; SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:791-800`, `packages/coding-agent/src/core/refinement/refinement.ts:508-512` | Planner explicitly requests expected improvement, SRC-2 `packages/coding-agent/src/core/refinement/refinement.ts:158`; planner history separately says Expected outcome, SRC-1 `packages/coding-agent/src/core/refinement/refinement.ts:548-562`. | RTE-18, RTE-22, RTE-24 | None supplied | No evidence that this wording caused later false reliance. | Definite representational mismatch: retained/rendered 'outcome' is a prediction, not an observed evaluation. Report actual mutation receipt separately. |

#### Bounded conclusion

Refinement performs a model judgment and direct adaptation loop. It reads bounded trajectory and history, proposes reusable facts or instructions, applies edits that meet structural and narrow freshness criteria, and exposes them in subsequent supplemental context. This is implemented operational admission and reuse. It is not evidence of accepted knowledge or realized improvement. Automatic review determines whether a checkpoint deserves refinement; it runs before a concrete proposal and normally uses the same selected model and trajectory. User/agent requests can enter planning without that review. Extensions can veto or replace the plan, but no independent extension checker was supplied.

The implemented authority boundaries are concrete: local state is the default, automatic refinement is root-session/persistence-limited, global mutation requires the global option, the reserved base prompt cannot be edited through this route, conflicting edits can be skipped, and recorded snapshots enable inverse edits. These protect edit scope and recoverability. They do not verify facts, code-call correctness, future utility, or safe transfer of lessons to another session. Failed later audit writes also should not be interpreted as proof that state stayed unchanged.

Quality gates are a distinct route: the host runs configured commands and consumes their outcomes to stop autonomous continuation or request repair. A passed command warrants only its own checked predicate. No configured oracle, expected answer, hidden holdout, protection of verifier inputs, or measured task outcome was available, and the gate implementation does not by itself establish those properties. Failure feedback affects the next model turn directly. Rerun suppression compares a limited workspace snapshot, so it can reuse failure despite changes in excluded paths or external conditions. Default autonomous mode is disabled and default gate commands are empty; deployed activation cannot be inferred from the code alone.

No inspected route connects an individual refinement prediction to an independent expected result, measured test, evidence-consuming acceptance decision, and post-acceptance integration. The expected improvement can instead reappear labeled as an outcome. Retention, prompt influence, and rollback are supported; produced accepted ampliative knowledge, successful long-run improvement, and causal benefit remain unestablished within this boundary.

## Reconciliation

Memory input identity matched run/source/boundary and SHA-256 `9206ed1fd5d94a4f17dff0abf716710ae3c2f1d8f2fbf6dbb87b8ca4ccf4e4f8`; report status was complete and report bytes matched the Run identity digest. The specialist's full comparison profile is adopted without stronger classifications.

Memory mappings: MEM-OBJ-1 through MEM-OBJ-8 map in order to OBJ-7 through OBJ-14; MEM-RTE-1 through MEM-RTE-8 to RTE-7 through RTE-14; MEM-BAP-1 to BAP-6; MEM-CLM-1 to CLM-4. OBJ-1 and CMP-1/CMP-2/CMP-3 retain their original referents. OBJ-12 is child access metadata reusing existing content kinds; OBJ-14/CMP-5 are included in the runtime inventory but excluded from the memory profile because model read-back was not established.

All nine memory integration issues are disposed: records registered; raw history kept separate; opaque payload uncertainty preserved; compaction/branch summaries counted as trace learning; refine authority/rollback narrowed to its actual route; global versus child-local visibility distinguished; dashboard model kept separate from configurable session model; recap read-back left uninspected; operational-control and arbitrary-extension exclusions kept explicit. No new memory comparison was independently drafted by the parent. The additional content-part IDs OBJ-29/OBJ-30 expose the already reported payload/manifest distinction; they do not change the profile scope or assessments.

Epistemic mappings: EPI-OBJ-15 through EPI-OBJ-23 map in order to OBJ-15 through OBJ-23, typed parts of the harness/audit or review/gate state. EPI-R1 through EPI-R11 map to RTE-15 through RTE-25; EPI-R12/EPI-R13 become the two absence functions of ABS-1; EPI-R14 through EPI-R17 map to RTE-26 through RTE-29. EPI-C2 maps to CLM-5. Refinement stage records specialize RTE-10; their epistemic judgments annotate its same source-native admission path, not a second memory mechanism.

The parent challenged EPI-R9's original `packages/coding-agent/src/core/agent-session.ts:8259-8261` citation: it identifies abort-controller cleanup, not prompt rebuilding. The epistemic specialist reread numbered pinned blobs, withdrew erroneous narrow anchors, corrected save/audit to `packages/coding-agent/src/core/agent-session.ts:8221-8236` and rebuild to `packages/coding-agent/src/core/agent-session.ts:8237-8238`, and rechecked other anchors. These were local line-assignment errors, not a changed source pin; findings remained supported. The corrected lens was integrated. The parent also independently checked the per-edit admission, expected-outcome assignment, history selector, catalog formatter and namespace restore mechanism. Structural anchor existence alone would not have caught this semantic mismatch.

The memory and epistemic specialists independently identified structural rather than semantic refinement admission and the expected-outcome label mismatch before seeing one another's findings. Their convergence concerns those mechanisms only. No convergence is claimed for omitted routes, actual behavior or measured benefit. There is no remaining material source conflict or unresolved specialist blocker.

## Bounded synthesis

Prime Agent centers work on a persistent Python environment controlled by a TypeScript session loop. This makes programming the execution and delegation interface: Python can hold large working objects and call real child sessions, while daemon workers preserve execution across client detachment. The mechanisms distinguish accepting a command, completing a model turn, replying to a parent and meeting an objective. Those events are not interchangeable.

Continuity is distributed across history, summaries, kernel snapshots, harness state and retained child metadata. Each has its own loss and selection boundary. Recovery deliberately avoids replaying uncertain worker operations; this favors explicit interruption over pretending external effects were rolled back. For long-running work the distinction matters more than a generic persistence label.

The Continual Harness implements adaptation of supplemental prompts, memories and descriptions. It can reshape traces into later context and record focused changes with rollback. Its code-backed admission establishes permissible stored changes; it does not itself establish that the proposed lesson is true or that the change improves performance. User quality gates are a different mechanism with a separately configured evaluator and operational stop/continue authority. A stored prediction named outcome must not be read as a measured result.

The assessment would change with candidate-linked execution traces showing actual read-back, experiments that vary retained content while holding task/model conditions fixed, external gate fixtures with documented reference authority, deployed permission configuration, or implementation changes that add a post-proposal improvement check or cover presently opaque branches. This analysis establishes wiring and its limits, not a product ranking or adoption recommendation.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Static source only | SRC-1, SRC-2; all routes | Pinned repository implementation/docs | Actual execution, activation, reliability or causal improvement | Retained executions and controlled comparisons |
| Existing checkout revision, not verified latest upstream | SRC-1, SRC-2 | Exact recorded commit | Claim to cover subsequent upstream changes | Separately pinned rerun |
| Provider internals/configuration excluded | CMP-3, OBJ-6, RTE-1, RTE-3, RTE-5 | Registry and inference call sites | Exact deployed weights, parameter updates, remote isolation and provider-native tools | Provider contracts, model/version provenance and deployed configuration |
| Arbitrary executable code and external services | OBJ-2, OBJ-3, RTE-4, RTE-5 | Tool admission and module registration | Universal effect confinement, semantic correctness or complete rollback | Bounded installed artifacts and external enforcement inspection |
| UI, installer/release update and all adapters not exhaustive | CLM-1, RTE-2, RTE-5 | Selected runtime routes | Exhaustive whole-repository behavior and distribution trust | Targeted additional source analysis |
| Opaque kernel values and authored skill implementations | OBJ-10, OBJ-13, RTE-11, RTE-14 | Serialization/loading interfaces | Complete aggregate representational form and behavioral authority | Actual retained payloads and bounded consumer inspection |
| Session/branch horizon is not task identity | RTE-8, RTE-9, RTE-10 | Compaction, branch and refine paths | Complete learning-scope union | Explicit task-to-session/branch mapping for all included paths |
| Dashboard recap has no established later model consumer | CMP-5, OBJ-14 | Summary production/display and child roster | Counting recap generation as durable trace learning | Source-anchored consumer route and retention trace |
| No candidate-specific semantic evaluator or reference answer supplied | ABS-1, OBJ-15 through OBJ-23, RTE-15 through RTE-29 | Built-in refinement and autonomous command runner | Accepted factual lessons, correct skill descriptions, predicted improvement or exhaustive task correctness | Candidate-linked tests, named acceptance criteria, reference provenance and actual outcomes |

## Verification and blockers

### Semantic verification

Checked canonical identity and stable referents, scope alignment, source layers and all adopted lens findings. RTE-7 through RTE-14 match the memory profile's objects and alternatives; static shipped instructions, arbitrary extensions, control state and unestablished recap consumers remain excluded. RTE-8, RTE-9 and RTE-10 each qualify independently as automatic trace-fed retained guidance; their online timing and text/structured forms are preserved, while the complete task-horizon union remains not-determinable. RTE-11 namespace copying and RTE-14 independent skill authorship do not inflate that learning subset.

Checked push selectors: RTE-7's branch/entry matching selects delivered history; RTE-11's session artifact identity selects restored payloads; RTE-10/RTE-14 catalogs are coarse scope/availability selection. Requested full-entry/value/skill reads remain pull. Opaque payloads remain part of both form and authority aggregates, preventing false known sets. General authored-skill acquisition/use stays afforded where documented consumers, rather than observed deployment, carry the claim.

RTE-1 through RTE-6 and RTE-15 through RTE-29 were checked for alternate-path coverage, admission versus terminal result, proposer/decider/veto roles, recovery and oracle scope. Refinement admission is operational, autonomous gate outcomes are predicate-relative, and predicted improvement is not observed outcome. Architectural status is separate from observed candidate state; no instance was observed and no causal support is claimed. The corrected epistemic source anchors were rechecked before integration. All material limitations have prevented conclusions and resolving evidence. Source-independent formatting validation is reported separately below.

### Deterministic validation

Validation target: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/result.md`. PASS (clean).

### Blockers

none
