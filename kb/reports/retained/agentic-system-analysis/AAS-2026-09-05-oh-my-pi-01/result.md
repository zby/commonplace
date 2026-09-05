---
type: kb/types/agentic-system-analysis-result.md
description: "Code-grounded whole-system analysis of oh-my-pi, distinguishing runtime controls, optional memory, and route-specific warrant."
run-id: AAS-2026-09-05-oh-my-pi-01
system: oh-my-pi
run-date: "2026-09-05"
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: be6cb8217cd4c1dafcc86793ae5d809ea4d7396a
analysis-cutoff: "2026-09-05"
evidence-tier: code-grounded
memory-comparison:
  scope: >-
    Durable session branch/compaction memory, the local backend's extraction and
    consolidated files/SQLite access state, learned.md, and managed Auto-Learn
    skills with their write, maintenance, discovery and later-consumer routes.
    Excludes Mnemopi, Hindsight, Sharpshooter, autoresearch-specific playbooks,
    static instructions, ordinary current-turn state and arbitrary workspace files.
    Local backend and Auto-Learn are conditional/default-off; the union describes
    their inspected enabled routes, not an observed default deployment.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values: ["files", "sqlite"]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-9, OBJ-10, OBJ-11]
      note: "Session JSONL, local SQLite extraction/selection state and generated memory/skill files; transient process caches are excluded."
    representational_form:
      assessment: known
      basis: wired
      values: ["natural-language", "symbolic"]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-9, OBJ-11]
      note: "Prose summaries/procedures coexist with parsed session/selection metadata and optional generated scripts; no parametric learning is inferred."
    lineage:
      assessment: known
      basis: wired
      values: ["authored", "trace-extracted"]
      records: [RTE-3, RTE-5, RTE-7, RTE-10, RTE-11]
      note: "Retained messages and explicit lesson/skill edits are authored; extraction and capture distill use. Re-consolidation is not a separate compiled lineage."
    behavioral_authority:
      assessment: known
      basis: wired
      values: ["knowledge", "instruction", "routing"]
      records: [BAP-1, BAP-2, BAP-3]
      note: "Reconstructed history and local guidance supply context; learned skill metadata routes selection and loaded bodies prescribe work. Storage confinement is not consumer authority."
    write_agency:
      assessment: known
      basis: wired
      values: ["automatic", "manual"]
      records: [RTE-5, RTE-7, RTE-10, RTE-11]
      note: "Automatic extraction/capture and model tool writes coexist with explicitly retained lessons and manual edits of discovered memory files; a user-triggered extraction remains automatic."
    curation_operations:
      assessment: known
      basis: wired
      values: ["consolidate", "dedup", "evolve", "invalidate", "synthesize"]
      records: [RTE-5, RTE-7, RTE-11]
      note: "Cross-session synthesis/consolidation, exact lesson dedup, skill revision and removal are wired. Invalidate maps partly to deletion/replacement preventing read-back, not a tombstone or truth-status protocol."
    read_back_direction:
      assessment: known
      basis: wired
      values: ["pull", "push"]
      records: [RTE-3, RTE-6, RTE-12]
      note: "Chosen sessions and full memory/skill artifacts can be requested; scoped summaries and skill catalogs are automatically delivered."
    read_back_signal:
      assessment: known
      basis: wired
      values: ["coarse", "identifier"]
      records: [RTE-3, RTE-6, RTE-12]
      note: "Push selection uses project/cwd and budgets, the selected session/leaf identity, and enabled named-skill catalog entries. This does not assert semantic retrieval by the local backend."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-5, RTE-10]
      note: "Conditional automatic trace-fed extraction/capture produces durable summaries and reusable skills wired to later consumers; plain logging alone is excluded from this classification."
    trace_source:
      assessment: known
      basis: wired
      values: ["session-logs", "tool-traces", "trajectories"]
      records: [RTE-5, RTE-10]
      note: "Prior JSONL sessions include selected tool results; the private capture model receives a detached current-task message trajectory. An event trigger alone is not an event-stream learning source."
    learning_scope:
      assessment: known
      basis: wired
      values: ["per-project", "cross-task"]
      records: [RTE-5, RTE-10, RTE-12]
      note: "Local memory is scoped by project/cwd across sessions; managed procedures are reused across tasks from the agent directory. Compaction is counted as retention/reshaping, not separately as trace learning."
    learning_timing:
      assessment: known
      basis: wired
      values: ["offline", "online", "staged"]
      records: [RTE-5, RTE-7, RTE-10]
      note: "Idle prior-session extraction is offline relative to its source task; live learn/capture occurs online; local extraction then consolidation is staged."
    distilled_form:
      assessment: known
      basis: wired
      values: ["natural-language", "symbolic"]
      records: [OBJ-3, OBJ-10, OBJ-11, RTE-5]
      note: "Distillation can produce prose lessons/procedures and local consolidation can write script assets; their correctness or execution is not established."
    faithfulness_tested:
      assessment: uninspected
      basis: null
      values: []
      records: [RTE-5, RTE-6, RTE-10, RTE-12]
      note: "No retained executed recall-dependence experiment was inspected; test files and instruction policies cannot establish yes or global no."
---

# oh-my-pi agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/oh-my-pi.md`

**Legacy memory review:** not applicable

The result records analysis content. Only the run state declares completed publication. The retained projection preserves these exact bytes. No auxiliary comparison, transfer scan, or Git operation was commissioned.

## Boundary and evidence

Evidence basis: executable source and shipped documentation from `https://github.com/can1357/oh-my-pi`, frozen on 2026-09-05 at `be6cb8217cd4c1dafcc86793ae5d809ea4d7396a`; code-grounded, with no target execution.

The intended use is to explain which responsibilities oh-my-pi owns and what its context, checks, and retained artifacts allow a later consumer to rely on. The selected target is the enclosing coding runtime shipped by this monorepo, including its session/SDK layer, agent loop, tool registry, delegated sessions, context maintenance, optional memory adapters, and selected review and experiment workflows. It is a whole-system boundary with explicitly selective mechanism coverage, not an exhaustive security audit of every package.

The source allowlist contains only this repository and revision. Operational access is `/home/zby/llm/commonplace/related-systems/can1357--oh-my-pi`; the origin was verified, the checkout was created without materializing a worktree, and evidence reads use commit-addressed `git --no-replace-objects ... show`, `grep`, and `ls-tree`. The moving GitHub landing page was used only to resolve the supplied reference and is not evidence for any finding here.

External model services supply inference and provider-specific replay behavior; their internals and credentials are excluded, preventing inference-quality and provider-isolation conclusions. Host operating systems, actual deployed extension code, editors, MCP servers, language servers, and debuggers are external effect or evidence producers; their exclusion prevents a deployment-wide containment or correctness guarantee. Hindsight server internals are excluded: an HTTP adapter establishes requests and framing, not the server's storage, retrieval, or learning mechanism. Unassessed route families include detailed security-scanner/remediation, cleanse, commit planning, collaboration relay cryptography, individual web scrapers, browser/computer execution, all provider codecs, and native platform isolation implementations. No system-complete warrant or performance conclusion covers them.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/can1357/oh-my-pi`; operational root above | `be6cb8217cd4c1dafcc86793ae5d809ea4d7396a` | implementation | Selected `packages/agent/src/`, coding-agent SDK/session/task/tools/memory/autolearn/advisor/autoresearch paths, and `crates/pi-edit/` paths cited in shared records | [Session construction](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/coding-agent/src/sdk.ts#L1305-L1339), [model boundary](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/packages/agent/src/agent-loop.ts#L1593-L1639); every additional full-path anchor is specified below | Static inspection establishes wiring under conditions, not operation, activation, causal gains, or the excluded external contracts |
| SRC-2 | Git | `https://github.com/can1357/oh-my-pi` | `be6cb8217cd4c1dafcc86793ae5d809ea4d7396a` | doctrine/design | README claims, memory documentation, and shipped instruction templates cited below; README benchmark statements are attributed claims, not inspected experiments | [Offered work](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/README.md#L155-L219), [memory contract](https://github.com/can1357/oh-my-pi/blob/be6cb8217cd4c1dafcc86793ae5d809ea4d7396a/docs/memory.md#L1-L28) | No linked video, benchmark dataset, live report, or external blog entered the boundary; claimed gains and shown behavior remain unverified |

## Shared records

### Components

| ID | Source-native component and responsibility | Form/storage | Evidence |
|---|---|---|---|
| CMP-1 | coding-agent SDK, AgentSession, SessionManager and client modes own configuration, prompt assembly, persistence and client lifetime | symbolic TypeScript in repository; runtime state in memory/files | SRC-1 `packages/coding-agent/src/sdk.ts:1312-1339,1435-1498,3531-3568` |
| CMP-2 | agent-core loop owns request/tool progression and callback boundaries | symbolic TypeScript; in-memory message state | SRC-1 `packages/agent/src/agent-loop.ts:1196-1270,1437-1479,1593-1639` |
| CMP-3 | MemoryBackend selector and local/Mnemopi/Hindsight/Sharpshooter adapters | symbolic code; backend-specific stores, not one common memory database | SRC-1 `packages/coding-agent/src/memory-backend/resolve.ts:20-26` |
| CMP-4 | task executor, output validation and isolation runner own delegated session lifetime and return | symbolic code; session files, artifacts and optional checkout copies | SRC-1 `packages/coding-agent/src/task/executor.ts:668-812,3318-3437` |
| CMP-5 | tool registry, extension wrapper, Hashline engine, LSP writethrough and TTSR coordinator mediate selected effects and feedback | symbolic TypeScript/Rust and natural-language rules; process state plus workspace files | SRC-1 `packages/coding-agent/src/sdk.ts:2918-2923`; `crates/pi-edit/src/modes/hashline/patcher.rs:185-250` |
| CMP-6 | reviewer command and advisor runtime generate and deliver model judgments | symbolic orchestration plus natural-language templates; session/task artifacts | SRC-1 `packages/coding-agent/src/extensibility/custom-commands/bundled/review/index.ts:180-267`; `packages/coding-agent/src/advisor/runtime.ts:1113-1201` |
| CMP-7 | Auto-Learn controller and managed-skill tools generate, mutate and rediscover reusable procedures | symbolic orchestration and natural-language skill files | SRC-1 `packages/coding-agent/src/autolearn/controller.ts:73-150`; `packages/coding-agent/src/autolearn/managed-skills.ts:16-26,174-255` |
| CMP-8 | autoresearch owns experiment execution, model-directed keep/discard, records and next-iteration context | symbolic tools plus natural-language protocol; Git, logs and stored session state | SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:124-217`; `packages/coding-agent/src/autoresearch/index.ts:294-316,378-404` |

### Operative objects

Each row identifies an operative part rather than treating all retained text as knowledge. Status of the producing/consuming implementation is wired; existence or quality of any real generated instance is uninspected.

| ID | Source-native object/part | Form and substrate; lineage and consumers | Evidence |
|---|---|---|---|
| OBJ-1 | Session entries and branch metadata | natural-language messages plus symbolic JSONL IDs/settings; user/model/tool history written by session manager and selected on resume | SRC-1 `packages/coding-agent/src/session/session-manager.ts:2281-2292,2913-2938`; `packages/coding-agent/src/session/session-context.ts:226-285` |
| OBJ-2 | Local compaction/branch summary and kept-entry boundary | natural-language summary with symbolic metadata in session files; model reshapes history; later context reconstruction consumes it | SRC-1 `packages/agent/src/compaction/compaction.ts:1792-1873`; `packages/coding-agent/src/session/session-context.ts:424-499` |
| OBJ-3 | Consolidated local MEMORY.md, memory_summary.md and generated memory skill bundles | natural-language summaries/procedures and optional symbolic scripts, stored as project memory files; produced from extracted sessions, read by model | SRC-1 `packages/coding-agent/src/memories/index.ts:872-1009` |
| OBJ-4 | Mnemopi working/episodic/fact records exposed by adapter | text plus symbolic metadata and bank/row identity; local SQLite backend contract; adapter retains transcript-derived material and retrieves it | SRC-1 `packages/coding-agent/src/mnemopi/backend.ts:54-64,87-150`; `packages/coding-agent/src/mnemopi/state.ts:472-589`; core storage/ranking internals uninspected |
| OBJ-5 | Tool-call request and arguments | symbolic schema instance proposed by model, held in message state and dispatched to a granted tool | SRC-1 `packages/agent/src/agent-loop.ts:2282-2362` |
| OBJ-6 | Worker final yield/data | natural-language findings or symbolic structured output; task-dependent production, parent consumption, optional artifact retention | SRC-1 `packages/coding-agent/src/task/executor.ts:668-812` |
| OBJ-7 | Active configuration, instruction templates and TTSR predicate/reminder policy | symbolic settings/predicates and natural-language prescriptions; files loaded into system/tool channels; static shipped material is excluded from memory read-back | SRC-1 `packages/coding-agent/src/sdk.ts:3171-3215`; `packages/coding-agent/src/session/ttsr-coordinator.ts:82-105,328-386` |
| OBJ-8 | Model-visible tool result payload and outcome | text/data imported from executor, possibly revised by extensions; memory/JSONL retention and model consumption | SRC-1 `packages/coding-agent/src/extensibility/extensions/wrapper.ts:349-415` |
| OBJ-9 | Local stage1_outputs, raw memories and rollout summaries | natural-language extraction plus symbolic source/update/lease metadata in SQLite and files; bounded traces feed extraction, consolidation consumes outputs | SRC-1 `packages/coding-agent/src/memories/storage.ts:47-88,137-217,493-521`; `packages/coding-agent/src/memories/index.ts:643-806` |
| OBJ-10 | learned.md lesson entries | natural-language observation/process advice in project files; explicit learn or manual editing; later bounded prompt snapshot | SRC-1 `packages/coding-agent/src/memories/index.ts:1280-1419` |
| OBJ-11 | Managed SKILL.md procedure body and discovery metadata | natural-language instructions plus symbolic frontmatter/name; agent-directory files generated/edited by learn/manage_skill; model selects and reads them | SRC-1 `packages/coding-agent/src/autolearn/managed-skills.ts:16-26,174-255`; `packages/coding-agent/src/extensibility/skills.ts:345-408,499-538` |
| OBJ-12 | Hindsight remote retained bank material | text and structured request metadata sent to external service; future recall/mental-model responses return to adapter | SRC-1 `packages/coding-agent/src/hindsight/backend.ts:41-83,198-265`; server substrate and completed materialization uninspected |
| OBJ-13 | Cached Hindsight recall/mental-model context | natural-language/data response cached in adapter state; imported from server, passed to driving model and compaction | SRC-1 `packages/coding-agent/src/hindsight/state.ts:332-456,502-523` |
| OBJ-14 | Sharpshooter decision statement and evidence/rationale delta | natural-language plus symbolic kind/friction/session fields; model extracts from user turn and persists pending delta | SRC-1 `packages/coding-agent/src/sharpshooter/extract.ts:171-310` |
| OBJ-15 | Consolidated Sharpshooter architecture/product/style prescriptions | natural-language project files; model consolidates deltas/current decisions, later prompt carries instruction force | SRC-1 `packages/coding-agent/src/sharpshooter/consolidate.ts:81-108,123-198,218-226`; `packages/coding-agent/src/sharpshooter/backend.ts:78-125` |
| OBJ-16 | Proposed source-code mutation | symbolic code/patch targeting workspace file; model proposes, edit engine applies; no necessary truth-apt assertion in code itself | SRC-1 `crates/pi-edit/src/modes/hashline/patcher.rs:185-250` |
| OBJ-17 | Hashline tag/anchor compatibility result | symbolic relation among stored snapshot, supplied tag, current bytes and anchor neighbors; patch engine consumes applicability result | SRC-1 `crates/pi-edit/src/modes/hashline/patcher.rs:185-250`; `crates/pi-edit/src/modes/hashline/recovery.rs:123-186` |
| OBJ-18 | LSP/linter diagnostics | text plus symbolic location/version/status from external analyzer; tool feedback to agent after write | SRC-1 `packages/coding-agent/src/lsp/writethrough.ts:347-422,449-472` |
| OBJ-19 | Reviewer bug findings and patch verdict | natural-language explanations with symbolic priorities/confidence/locations; model-generated judgment returned to parent/operator | SRC-2 `packages/coding-agent/src/prompts/agents/reviewer.md:1-54,57-84,111-134` |
| OBJ-20 | Advisor risk/correctness claim | natural-language candidate judgment and severity; separate model consumes primary trace, primary receives note | SRC-1 `packages/coding-agent/src/advisor/advise-tool.ts:34-64`; SRC-2 `packages/coding-agent/src/prompts/advisor/system.md:13-16,29-54` |
| OBJ-21 | Advisor suggestion/instruction part | natural-language proposed action, no necessary truth claim; same envelope as OBJ-20, separate authority interpretation | SRC-1 `packages/coding-agent/src/advisor/advise-tool.ts:45-64,119-134` |
| OBJ-22 | Autoresearch raw run and parsed measurements | symbolic command/exit/timing/metric fields and natural-language log; imported from fixed harness into pending run | SRC-1 `packages/coding-agent/src/autoresearch/tools/run-experiment.ts:81-136,143-195` |
| OBJ-23 | Autoresearch supplied metric/status/description and retained run interpretation | symbolic judgment fields with text, commit, deviation/flag and log lineage; model supplies, logger acts/stores | SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:124-217` |
| OBJ-24 | Autoresearch confidence scalar | symbolic arithmetic result over retained positive/unflagged metrics; metadata/display consumer | SRC-1 `packages/coding-agent/src/autoresearch/state.ts:144-169` |
| OBJ-25 | Autoresearch playbook hypothesis/explanation part | natural-language candidate explanation from model; retained session notes, later model context | SRC-1 `packages/coding-agent/src/autoresearch/tools/update-notes.ts:24-69`; SRC-2 `packages/coding-agent/src/autoresearch/prompt.md:28-39` |
| OBJ-26 | Autoresearch playbook goals/scope/next-action part | natural-language policy in same notes container; model-authored, stored and later inserted as instructions | SRC-1 `packages/coding-agent/src/autoresearch/index.ts:294-316,378-404` |

### Routes

All records below have **implementation conclusion status: wired**. This means the described conditional control path is connected. **Operation conclusion status: uninspected** and **activation conclusion status: uninspected** apply to every route: no target run or content-dependent behavioral comparison was retained. Evidence status does not state a guarantee. The runtime account and read-back audit extend these canonical records; the epistemic ledger splits their functions into linked rows without creating a second identity inventory.

| ID | Trigger, next-step owner and policy/form | Context/state → executor/effect → return, persistence and recovery | Evidence |
|---|---|---|---|
| RTE-1 | prompt/continuation; AgentSession and agent loop, model choice within symbolic scheduling | assembled messages/settings → provider stream → assistant content/calls; RTE-3 retains, deadline/abort/hooks stop or continue | SRC-1 `packages/agent/src/agent-loop.ts:1029-1075,1196-1270,1593-1639,1660-1708` |
| RTE-2 | assistant tool calls; loop resolves/validates and schedules selected executor | OBJ-5 plus current tool registry → effect and OBJ-8 → next model request; errors/skips paired with calls, retention through RTE-3 | SRC-1 `packages/agent/src/agent-loop.ts:1437-1479,2282-2362,2586-2653` |
| RTE-3 | message append or session open/branch selection; SessionManager/SessionContext | OBJ-1 entries and leaf → file retention or branch reconstruction → later model context; cyclic traversal bounded, in-memory variant loses file durability | SRC-1 `packages/coding-agent/src/session/session-manager.ts:2281-2292,2913-2938,3102-3109`; `packages/coding-agent/src/session/session-context.ts:226-285,410-499` |
| RTE-4 | compact request or token threshold; maintenance chooses compaction method/model | selected history → local summary or external replay/archive → OBJ-2/retained entry and rebuilt messages; later reset/compaction supersedes selection | SRC-1 `packages/agent/src/compaction/compaction.ts:1792-1873`; `packages/coding-agent/src/session/session-maintenance.ts:1487-1541,1622-1638` |
| RTE-5 | local-backend startup on durable top-level session; lease/age/idle/cwd filters then extractor/consolidator models | prior bounded transcripts → OBJ-9 → OBJ-3 files/bundles; source watermark/retry/lease state in SQLite, empty/malformed output handled before file application | SRC-1 `packages/coding-agent/src/memories/index.ts:334-451,477-603,643-806,872-1009`; `packages/coding-agent/src/memories/storage.ts:137-217,493-521` |
| RTE-6 | local prompt build or memory:// read; cache/budget/root selection | OBJ-3/OBJ-10 → bounded system append or requested full artifact → model; cache reused per session, explicit clear/startup-summary refresh changes it | SRC-1 `packages/coding-agent/src/memories/index.ts:182-293`; `packages/coding-agent/src/internal-urls/memory-protocol.ts:117-198` |
| RTE-7 | explicit learn call; enabled tool/backend and bounded lesson formatter | lesson text → backend retain/queue or local OBJ-10; optional OBJ-11 write follows; lesson can survive later skill-write failure; local writes serialize/deduplicate/cap | SRC-1 `packages/coding-agent/src/tools/learn.ts:22-48,51-138`; `packages/coding-agent/src/memories/index.ts:1292-1419` |
| RTE-8 | task/eval worker launch, follow-up or revival; task policy and executor | prompt/agent definition + selected parent resources → separate AgentSession, own tools/IDs and optional isolated cwd → OBJ-6/artifacts; schema disposition RTE-16, cleanup/revival/merge recovery | SRC-1 `packages/coding-agent/src/task/executor.ts:941-984,3234-3240,3318-3437,3697-3727`; `packages/coding-agent/src/task/isolation-runner.ts:197-285,340-409` |
| RTE-9 | tool dispatch; extension callback and approval wrapper | original/revised args + grant mode/policies → block, prompt or execute; result hooks can change returned evidence; explicit deny or unavailable required UI produces error | SRC-1 `packages/coding-agent/src/extensibility/extensions/wrapper.ts:180-250,245-345,349-415` |
| RTE-10 | qualifying completed primary turn with automatic Auto-Learn enabled; controller/model | detached trajectory and private provider session → capture model invokes learn/manage_skill or stores nothing; abort/plan/goal/tool-count conditions restrict triggering | SRC-1 `packages/coding-agent/src/autolearn/controller.ts:73-150`; `packages/coding-agent/src/sdk.ts:1203-1255,4191-4215` |
| RTE-11 | manage_skill or learn skill payload; managed-store validation | named procedure → confined create/update/delete → persistent OBJ-11; manage_skill refreshes current catalog, learn's optional branch only writes; invalid paths/size/link cases reject | SRC-1 `packages/coding-agent/src/autolearn/managed-skills.ts:54-108,174-255`; `packages/coding-agent/src/tools/manage-skill.ts:34-99`; `packages/coding-agent/src/tools/learn.ts:98-133` |
| RTE-12 | skills discovery/refresh or explicit named invocation; filters/name priority then model/human selection | managed description → system catalog; selected full body → instruction-bearing model input; persists after capture disabled, deleted/shadowed/filtered skills stop discovery | SRC-1 `packages/coding-agent/src/discovery/builtin.ts:309-336`; `packages/coding-agent/src/extensibility/skills.ts:345-408,499-538`; `packages/coding-agent/src/session/session-tools.ts:1266-1286` |
| RTE-13 | Mnemopi selected; primary first-turn/compaction/end lifecycle and explicit tools | prompt/history → recall context; unretained transcript → backend writes with provenance/cursor; children alias parent state; extraction/flush/promotion are adapter requests, shutdown bounded | SRC-1 `packages/coding-agent/src/mnemopi/backend.ts:87-150,177-193,251-318`; `packages/coding-agent/src/mnemopi/state.ts:280-431,472-624,645-700,736-780` |
| RTE-14 | Hindsight selected; bank scope, first-turn recall and retain cadence | transcript → async server retain; prompt/history → recalled/mental-model context → model/compaction; cache clear is local, errors/timeouts bounded, parent owns automatic work | SRC-1 `packages/coding-agent/src/hindsight/backend.ts:41-147,198-265`; `packages/coding-agent/src/hindsight/state.ts:332-456,502-523` |
| RTE-15 | Sharpshooter selected and qualifying top-level user message; model extraction, shape/quote admission, background consolidation | current user/context → OBJ-14 queued deltas → OBJ-15 project files → bounded instruction append or lexical search; concurrent extraction skipped and consolidated deltas consumed | SRC-1 `packages/coding-agent/src/sharpshooter/backend.ts:78-125,225-240`; `packages/coding-agent/src/sharpshooter/extract.ts:98-148,171-310`; `packages/coding-agent/src/sharpshooter/consolidate.ts:123-198,218-226` |
| RTE-16 | worker yield/finalization; JSON validator then mode/override-aware finalizer | OBJ-6 and output schema → valid/invalid/unavailable plus success/failure/warning → parent/job return; strict rejects; ordinary valid-schema mismatches also reject in permissive mode, exceptions permit warning success | SRC-1 `packages/coding-agent/src/tools/output-schema-validator.ts:56-106`; `packages/coding-agent/src/task/executor.ts:668-812` |
| RTE-17 | Hashline edit; symbolic snapshot/anchor compatibility and recovery | OBJ-16 plus stored/current bytes → OBJ-17 predicate → applied/recovered patch or mismatch error; head/tail drift may warn and apply | SRC-1 `crates/pi-edit/src/modes/hashline/patcher.rs:185-250`; `crates/pi-edit/src/modes/hashline/recovery.rs:123-186` |
| RTE-18 | LSP writethrough; configured analyzers and feedback timing | file mutation → OBJ-18 diagnostics → inline/deferred tool feedback; write precedes diagnostic fetch and timeout path still commits | SRC-1 `packages/coding-agent/src/lsp/writethrough.ts:241-288,347-472` |
| RTE-19 | /review; command prepares diff/distribution instructions, model chooses reviewer tasks | diff/source context → reviewer-model OBJ-19 → parent/operator verdict/findings; review work uses task persistence/return; no inspected release gate consumes verdict | SRC-1 `packages/coding-agent/src/extensibility/custom-commands/bundled/review/index.ts:180-267`; SRC-2 `packages/coding-agent/src/prompts/review-request.md:24-41` |
| RTE-20 | enabled advisor and primary updates; reviewer model then noise/dedup/rate guard and severity scheduler | incremental trace → OBJ-20/OBJ-21 or silence → aside/card/steering; blocker can interrupt/reopen, plan/ACP/user-interrupt/terminal conditions qualify delivery | SRC-1 `packages/coding-agent/src/advisor/runtime.ts:1113-1201`; `packages/coding-agent/src/advisor/emission-guard.ts:103-175`; `packages/coding-agent/src/session/session-advisors.ts:1206-1290` |
| RTE-21 | configured regex/AST match on selected streamed content; TTSR coordinator | OBJ-7 predicate → reminder/abort/retry/follow-up by mode → primary context, persisted injection state; matching does not certify corrected behavior | SRC-1 `packages/coding-agent/src/session/ttsr-coordinator.ts:82-141,251-297,328-459`; `packages/coding-agent/src/session/session-manager.ts:2504-2522` |
| RTE-22 | active autoresearch run; tool executes fixed harness | working code → bash autoresearch.sh/log/exit/parsed measurements OBJ-22 → model and pending run; process failure/kill is reported | SRC-1 `packages/coding-agent/src/autoresearch/tools/run-experiment.ts:81-136,143-195,227-235` |
| RTE-23 | log_experiment on pending run; model status/metric then logger/Git executor | OBJ-22 plus supplied OBJ-23 → keep commit on dedicated branch or revert, warnings and retained record; supplied/parsed metric mismatch is warning, Git failures return errors | SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:64-83,124-217` |
| RTE-24 | enough eligible retained measurements; arithmetic state calculation | positive/unflagged segment metrics → absolute best-kept change divided by MAD → OBJ-24 or null; informational output, not keep gate | SRC-1 `packages/coding-agent/src/autoresearch/state.ts:144-169`; `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:204-217,259-279` |
| RTE-25 | update_notes and later active autoresearch start; model text then storage/prompt renderer | OBJ-25/OBJ-26 replace/append → retained session notes → next iteration system context with recent results; acceptance not prerequisite, updates replace prior guidance | SRC-1 `packages/coding-agent/src/autoresearch/tools/update-notes.ts:24-69`; `packages/coding-agent/src/autoresearch/index.ts:294-316,378-404` |

### Claims

| ID | Claimed operation | Conclusion status | Evidence |
|---|---|---|---|
| CLM-1 | Coding agent with integrated IDE/tool surface | claimed | SRC-2 `README.md:6-27,133-151` |
| CLM-2 | Time-traveling stream rules interrupt, inject, retry and persist corrections | claimed | SRC-2 `README.md:155-157` |
| CLM-3 | Subagents return schema-validated results from isolated worktrees, without merge conflicts/orphaned edits | claimed | SRC-2 `README.md:163-165` |
| CLM-4 | Agent curates facts/lessons and recalls cross-session project memory | claimed | SRC-2 `README.md:213-215` |
| CLM-5 | Code review returns prioritized findings/confidence and ship verdict | claimed | SRC-2 `README.md:201-203` |
| CLM-6 | Hashline rejects stale patches and improves editing/token efficiency | claimed | SRC-2 `README.md:205-207,113-120` |
| CLM-7 | Separate advisor catches issues and injects notes including blockers | claimed | SRC-2 `README.md:173-175` |
| CLM-8 | Autoresearch retains improved experiments while preserving correctness and learns across iterations | claimed | SRC-2 `packages/coding-agent/src/autoresearch/prompt.md:28-45,99-103` |

### Evidenced absences

None registered within the selected boundary. Uninspected mechanisms and missing run evidence are limitations, not evidenced absences.

### Behavioral-authority paths

The force below describes how a consumer receives a result. Epistemic license is separate; none of these paths has observed activation evidence.

| ID | Objects/routes | Consumer, channel, force, horizon | Epistemic license and evidence |
|---|---|---|---|
| BAP-1 | OBJ-1/OBJ-2; RTE-1/RTE-3/RTE-4 | driving model, reconstructed conversation/summary, contextual knowledge and retained role instructions, later calls on selected branch | History presence is not source truth or summary fidelity; SRC-1 `packages/coding-agent/src/session/session-context.ts:226-285,424-499` |
| BAP-2 | OBJ-3/OBJ-10; RTE-6 | driving model, system append or memory:// tool return, advisory memory knowledge/process guidance, cached current or later project session | Wrapper explicitly defers factual decisions to current files/runtime/user instruction; SRC-2 `packages/coding-agent/src/prompts/memories/read-path.md:1-17` |
| BAP-3 | OBJ-11; RTE-12 | driving model/worker, skill-list metadata then full selected body, routing then instruction, current invocation and later sessions until filtered/shadowed/updated/deleted | Availability and prescribed use, not verified procedure; SRC-1 `packages/coding-agent/src/extensibility/skills.ts:345-408,499-538`; SRC-2 `packages/coding-agent/src/prompts/skills/user-invocation.md:1-8` |
| BAP-4 | OBJ-4/OBJ-13; RTE-13/RTE-14 | driving model, advisor or summarizer, backend recall/tool/system/compaction context, background knowledge, scoped bank and invocation | Recalled context is not instruction precedence or completed learning proof; SRC-1 `packages/coding-agent/src/mnemopi/backend.ts:54-64,138-150`; `packages/coding-agent/src/hindsight/backend.ts:21-29,86-101`; SRC-2 `packages/coding-agent/src/prompts/advisor/memory-context.md:1-4` |
| BAP-5 | OBJ-15; RTE-15 | driving model, appended project decisions, instruction to follow unless user overrides, later project work | Quoted evidence occurrence and model curation do not warrant every decision; SRC-1 `packages/coding-agent/src/sharpshooter/backend.ts:78-125`; `packages/coding-agent/src/sharpshooter/extract.ts:252-310` |
| BAP-6 | OBJ-5/OBJ-7; RTE-9 | tool executor, resolved symbolic grant/extension result, enforcing allow/prompt/deny, one wrapped call | Operational authorization only; SRC-1 `packages/coding-agent/src/extensibility/extensions/wrapper.ts:180-345` |
| BAP-7 | OBJ-6/OBJ-17; RTE-16/RTE-17 | worker finalizer or edit engine, schema/applicability predicate, enforcing within selected mode/path, one return/edit | Schema shape or anchor compatibility only; SRC-1 `packages/coding-agent/src/task/executor.ts:668-812`; `crates/pi-edit/src/modes/hashline/patcher.rs:185-250` |
| BAP-8 | OBJ-18/OBJ-19; RTE-18/RTE-19 | agent/operator, diagnostics or reviewer task output, advisory evidence/judgment, current revision work | Analyzer-specific result or model finding, not universal correctness; SRC-1 `packages/coding-agent/src/lsp/writethrough.ts:347-472`; SRC-2 `packages/coding-agent/src/prompts/agents/reviewer.md:57-84,111-134` |
| BAP-9 | OBJ-20/OBJ-21; RTE-20 | primary model and scheduler, aside/card/steering note, advisory content plus enforcing interruption/continuation, current/next permitted turn | Delivery acceptance is noise/dedup/rate policy, not truth acceptance; SRC-1 `packages/coding-agent/src/advisor/emission-guard.ts:103-175`; `packages/coding-agent/src/session/session-advisors.ts:1220-1290` |
| BAP-10 | OBJ-7; RTE-21 | primary model/loop, reminder plus abort/retry/follow-up, instruction and enforced scheduling, continued turn and persisted injection horizon | Policy match, not proof of correction; SRC-1 `packages/coding-agent/src/session/ttsr-coordinator.ts:251-297,389-459` |
| BAP-11 | OBJ-23; RTE-23 | Git executor, model-supplied keep/discard tool args, enforcing commit/revert under branch preconditions, working experiment | Intended improvement criterion remains model policy; SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:124-202` |
| BAP-12 | OBJ-25/OBJ-26; RTE-25 | next experimenting model, system-prompt notes, hypothesis context and procedural instruction, later active iteration | Retention/use does not require explanatory claim acceptance; SRC-1 `packages/coding-agent/src/autoresearch/index.ts:294-316,378-404` |

## Runtime account

### Ordinary invocation and responsibility horizon

An operator starts `omp` with a prompt, working directory, configuration, and model selection. `main` constructs the SDK session, then chooses an interactive, RPC, ACP, or print surface (SRC-1 `packages/coding-agent/src/main.ts:1856-1873,2045-2050,2099-2116`). A simple print invocation provides a concrete end-to-end path: the frontend calls `session.prompt`, emits the final assistant text or error, waits for stdout to drain, and disposes the session (SRC-1 `packages/coding-agent/src/modes/print-mode.ts:169-246`). Interactive and RPC operation reuse the session machinery but keep the client available for further input.

The session derives the project/agent directories, loads settings and provider registry, creates or accepts a SessionManager, and assigns a provider session identity. On resume it reconstructs a selected message branch and marks a previously interrupted nonterminal tail as aborted (SRC-1 `packages/coding-agent/src/sdk.ts:1312-1339,1435-1498`). Prompt assembly combines workspace roots, loaded context files, skills, rules, current tools, optional memory instructions, and model-specific configuration. The Agent receives the resulting system prompt, active model and tools, conversion callbacks, steering/follow-up policy, credential resolver, and deadline (SRC-1 `packages/coding-agent/src/sdk.ts:3171-3215,3531-3568`). This establishes delivered context, not obedience.

The model chooses content and calls within the current tool surface; symbolic loop policy owns sequencing, gates, cancellation, and continuation. Before each request the loop applies context transformations, message conversion, provider normalization, and optional in-band tool encoding. It calls the selected stream function with the resolved model, context, credentials, and request controls (SRC-1 `packages/agent/src/agent-loop.ts:1196-1270,1593-1639,1660-1708,1750-1760`). Local argument validation and before-tool hooks precede execution. Tool outputs are appended and may trigger another model turn; stopped, denied, truncated, or aborted calls receive explicit outcomes (SRC-1 `packages/agent/src/agent-loop.ts:1437-1479,2282-2362,2586-2653`). A terminal assistant response or explicit stop ends that run, while the enclosing session may continue.

Effects belong to the dispatched tool and its host contract. Files, shell state, subprocesses, and remote actions can outlive a model turn. Session entries retain messages and settings for reconstruction; they are not a transaction over external effects. An in-memory SessionManager explicitly omits file persistence (SRC-1 `packages/coding-agent/src/session/session-manager.ts:2281-2292,2913-2938,3102-3109`). No exactly-once external-effect claim follows from a recoverable transcript.

### Material alternate paths and controls

The SDK and lower-level Agent can be embedded independently of CLI surfaces. `streamFn` can replace the default provider call, and provider-specific tool delivery can differ from normal local dispatch (SRC-1 `packages/agent/src/agent-loop.ts:1660-1708,2288-2294`). The session tool registry is always wrapped for approval. Extensions may revise arguments before the wrapper resolves the actual executing input, and may replace result content or its error flag afterward (SRC-1 `packages/coding-agent/src/sdk.ts:2795-2808,2918-2923`; `packages/coding-agent/src/extensibility/extensions/wrapper.ts:180-250,349-415`). A wrapper result therefore represents the installed extension chain's account of execution. Same-tool native delegation through `ctx.invokeTool` intentionally inherits the caller's existing grant (SRC-1 `packages/coding-agent/src/sdk.ts:2840-2846,2881-2887`). A registry gate is not a boundary around arbitrary loaded code or shell effects.

The capability surface includes read/write/exec tiers, custom and MCP tools, code execution, and worker launch. The current grant is the runtime-selected tools plus effective per-tool policies and approval mode. The shipped mode defaults to `yolo`; `always-ask` still automatically allows read-tier tools. Explicit deny policies remain operative. Pending provider computer-safety checks require an interactive approval even in yolo mode, and a required prompt without UI fails the tool call (SRC-1 `packages/coding-agent/src/config/settings-schema.ts:4100-4123`; `packages/coding-agent/src/tools/approval.ts:120-218`; `packages/coding-agent/src/extensibility/extensions/wrapper.ts:245-345`). Actual operator settings and the OS isolation envelope were not supplied.

Subagents are session instances with separate IDs, model/context, selected tools, depth/spawn policy, and optional retained session file. Despite its name, the inspected `runSubprocess` path constructs `createAgentSession` directly. Children may share the parent's credential resolver, MCP connections, artifact manager, and selected memory state (SRC-1 `packages/coding-agent/src/task/executor.ts:3234-3240,3318-3437`). Headless children use yolo mode; explicit policies still apply, and the parent task grant is the declared authorization boundary (SRC-1 `packages/coding-agent/src/task/executor.ts:941-984`). Spawn frontmatter can select allowed agent names or disable spawning (SRC-1 `packages/coding-agent/src/task/spawn-policy.ts:18-57`).

Checkout isolation is optional and defaults off. When enabled, the runtime runs the child with an isolated cwd, waits for successful deferred cleanup before capturing changes, then returns patches or branches for optional application. Apply defaults true; patch is the default merge strategy. Failed integration can retain a patch or rescue branch with an error; source code explicitly represents merge conflicts (SRC-1 `packages/coding-agent/src/config/settings-schema.ts:4852-4859,4922-4946`; `packages/coding-agent/src/task/isolation-runner.ts:197-285,340-409`). This is workspace-change isolation and recovery, not evidence of process or network containment. Non-isolated workers may remain parked and later revive; owner jobs are reaped during finalization (SRC-1 `packages/coding-agent/src/task/executor.ts:3697-3727`).

### Forcing cases and guarantee limits

1. **Headless call requiring approval.** The wrapper rejects execution when a prompt is required but there is no UI. Its owner is ExtensionToolWrapper; enforcement point is before `tool.execute`; strength is an invariant of the inspected wrapped path; implementation conclusion status: wired. Covered: wrapped registry execution and its shown nested dispatch rules. Alternate: yolo grants ordinary tiers, native same-tool delegation inherits approval, arbitrary extension/provider effects require their own contracts. This establishes scoped operational admission, not truth or universal containment.
2. **Restart after compaction or interruption.** SDK reconstruction appends an interrupted-tail marker and SessionContext walks the chosen leaf-to-root branch. It emits the latest summary plus kept/post-compaction messages, honors a later reset boundary, and can reattach provider replay payload or snapcompact archive. The owner is session/context maintenance; strength is a reconstruction protocol; implementation conclusion status: wired. Persisted summaries affect a later invocation, but an abort marker does not undo prior effects or certify summary fidelity (SRC-1 `packages/coding-agent/src/sdk.ts:1486-1498`; `packages/coding-agent/src/session/session-context.ts:226-285,410-499`).
3. **Worker result or isolated integration fails.** Output handling can distinguish schema, abort, and merge outcomes; optional strictness and explicit failure artifacts limit the README's unconditional-sounding typed/no-conflict promise. The owner is task execution and isolation handling; strength is a conditional protocol; implementation conclusion status: wired. It depends on chosen output enforcement, cleanup completion, filesystem and Git behavior. Successful operational return is not semantic correctness of the worker's findings.
4. **Edit targets drift or reported experiment metrics disagree.** Hashline recovery and autoresearch warning/keep logic expose the difference between a check and a hard admission gate. The exact checks, consumers, and limitations are recorded by route below. Neither a stale-file recovery nor a model-supplied keep decision establishes a correct program or transferable improvement.

**Execution preflight disposition:** no dynamic check planned. Considered checks were a mocked provider/tool turn, persisted-session compaction/resume fixture, stale Hashline fixture, and a controlled memory-recall intervention. Static inspection resolves the present wiring and policy questions. A mocked turn would not establish live provider or OS behavior; a memory activation claim would require retained contrasting executions. No target package installation, configured credential availability, live backend service, or deployed tool grant was assumed. No target test ran, so there is no probe capsule or negative result from execution.

### Read-back and visibility audit

This table extends every canonical route. “Via RTE-3” means delivery only if the relevant messages were retained and that branch is later selected; it does not turn ordinary current-run state into memory. All described effects are wired; actual activation and deployed success remain uninspected. Persistence is specified in the canonical route, so the audit names the later consumer and selection/expiry separately.

| Route | Immediate return; later read-back | Delegated visibility | Selection predicate; invalidation/expiry | Activation/effect and evidence limit |
|---|---|---|---|---|
| RTE-1 | assistant/calls; retained branch via RTE-3 | only context explicitly delivered to workers | active prompt/model/context transforms; branch reset/compaction | inference request wired, correctness and obedience unobserved |
| RTE-2 | tool result; via RTE-3/local extraction when selected | worker's tools/results or parent-supplied context | granted tool/name/args; current results may be pruned/summarized | external effects not rolled back by transcript operations |
| RTE-3 | entry ID/reconstructed messages; selected later invocation | separate child session or explicit context sharing | session file and leaf ancestry; reset/latest compaction changes visible path | reconstructable context, not transactional replay; in-memory variant has no durable read-back |
| RTE-4 | summary/rebuilt context; retained compaction on resume | only delivered context/worker's own compaction | threshold/manual method, kept-entry ID; later reset/summary supersedes | content transformation and replay assembly, not verified preservation |
| RTE-5 | background extraction/consolidation output; RTE-6 or memory file reads | extraction skips children; local roots can differ by cwd | top-level durable session, age/idle/watermark/cwd/leases; reprocessing and omitted-skill removal | automatic durable distillation, not tested learning benefit |
| RTE-6 | injected bounded summary/lessons or full requested file; later session snapshot | caller-cwd root; no automatic parent-bank alias on local path | root/session cache and budget; clear/startup summary refresh/new session | summary gets budget before lessons; same-session lesson write may remain undelivered |
| RTE-7 | retain/lesson status, optional partial skill result; RTE-6/RTE-12 | backend-dependent shared state, never inferred from write alone | enabled learn/backend, bounded text, exact dedup/cap; editing/clear/replace | persistence may precede failed skill write; no immediate lesson-injection guarantee |
| RTE-8 | worker report/artifacts; optional saved-worker revival | per-child context, tools and selected shared resources | spawn policy/ID, model, optional isolation; timeout/cleanup/park expiry | delegated execution/return, not independent process containment or content trust |
| RTE-9 | allow/deny/error/revised tool result; via RTE-3 | children have their own effective mode; explicit policies inherited | actual executing args/tier/policy/UI; settings or extension change | scoped gate; arbitrary extension effects and raw SDK calls require separate contracts |
| RTE-10 | capture finishes or no write; later RTE-6/RTE-12 | capture has private message/provider state; originating turn top-level | enabled automatic mode, substantive stop/tool count/abort/plan/goal guards; disabling stops capture | detached trace-fed call, not successful reusable lesson observation |
| RTE-11 | skill path/status; current refresh from manage_skill and later discovery | workers may discover same agent-directory skills subject to filters | managed name/path/size/link checks; update/delete/name shadowing | dedicated writes confined; broad shell/extension changes outside that guarantee |
| RTE-12 | catalog metadata or requested body; future sessions rediscover | same discovery contract subject to worker config | master switch/filters/name priority/selected identifier; capture-off alone does not invalidate | routing/instruction delivery, not actual matching or execution quality |
| RTE-13 | backend tools/recall; later primary/compaction recall | children alias parent's backend resources, no own automatic listeners | selected backend/bank/query/cursor; edit/invalidate/clear/shutdown contracts | adapter calls wired; core retrieval/extraction and completed promotion uninspected |
| RTE-14 | HTTP/tool result or cached context; later recall/mental model | child aliases parent's bank/scope | bank/tag/query/cadence/cache deadline; local clear does not delete server bank | async acceptance of request does not prove durable retrievable materialization |
| RTE-15 | admitted delta/search/file context; future project prompts | automatic extraction top-level; file visibility follows project | nonshort nonslash user turn, literal quote/shape, budget; consolidated queue consumption/files replacement | model-selected decisions gain instruction force; boolean shape does not enforce any friction flag true |
| RTE-16 | validity/outcome metadata plus worker return; via RTE-8/RTE-3 | parent sees final output/status | declared schema/mode/override/fallback; per-return scope | schema licenses representation only |
| RTE-17 | applied/recovered edit or mismatch; file bytes and via RTE-3 | shared or isolated workspace; own snapshot store | tag/anchor/context matching; new file bytes invalidate older assumptions | selected edit admission only; no proof of program behavior |
| RTE-18 | inline/deferred diagnostics; via RTE-3 if retained | worker's configured analyzer and feedback path | write/version/analyzer/feedback timing; new write changes freshness | imported analyzer judgment after effects, not universal pre-write check |
| RTE-19 | prioritized findings/verdict; task/session history | reviewer receives selected diff/context | requested diff and prompt-directed distribution; later revision can stale findings | candidate judgment, downstream release decision uninspected |
| RTE-20 | note or suppressed emission; retained card/next permitted turn | separate advisor context; not automatic sibling sharing | enabled model, transcript update, guard/severity/runtime state; duplicate/terminal/user-interrupt handling | schedule can change while note remains advisory; no observed correctness gain |
| RTE-21 | reminder/interrupt/retry; persisted injected-rule state | worker's own configured rules | selected regex/AST sources and interrupt mode; session-rule state changes | enforced stream control, model compliance unobserved |
| RTE-22 | log/exit/metrics; pending/retained experiment through RTE-23 | no independent worker visibility established in inspected path | active experiment and fixed harness; pending run consumed on log | process/harness evidence only |
| RTE-23 | keep/discard outcome and retained run; subsequent active experiment | code/records only if delegated explicitly or workspace shared | model status, pending run, dedicated-branch condition; flags/revisions affect later selection | commit/revert force, faithful improvement/correctness judgment not enforced by metric comparison |
| RTE-24 | derived scalar/null; logged/displayed result | no special delegated consumer inspected | positive unflagged current-segment metrics; fewer than 3, zero MAD or unchanged best yields null | descriptive arithmetic, not causal confidence |
| RTE-25 | saved notes; next active iteration prompt | only context explicitly supplied | active experiment/branch and stored notes; replace/append changes next guidance | hypotheses and policy may be used before acceptance |

## Lens scoping

### Memory/context scope

**Depth: full.** Trigger evidence: CLM-4; SRC-1 backend selection, extraction/retention, named skill discovery and session reconstruction. Inspected boundary: CMP-1/CMP-3/CMP-4/CMP-7; OBJ-1–OBJ-4 and OBJ-9–OBJ-15, plus role-bearing OBJ-7 as a classify-only static contrast; RTE-3–RTE-8 and RTE-10–RTE-15. RTE-25 is separately inventoried as experiment-specific retained context. Substantive write, maintenance, read-back, worker visibility and authority paths warrant full depth. Backend core algorithms/external servers and real generated instances remain outside the established evidence.

The fourteen normalized axes intentionally describe session branch/local-summary memory, local extraction, lessons and managed Auto-Learn skills. Alternatives remain in this whole-system lens but outside that comparison population. This prevents an uninspected remote store from becoming a supposed property of local memory.

### Epistemic scope

**Depth: full.** Invoked `kb/instructions/analyse-external-system-epistemic-architecture.md` as a sparse overlay on SRC-1/SRC-2 and the canonical register. Triggers: CLM-2–CLM-8, which attach consequences to checking, remembered guidance, review and experiment selection. Assessed: RTE-9 and RTE-15–RTE-25, plus memory shape/publication checks in RTE-5/RTE-7/RTE-11. RTE-1–RTE-4, RTE-6/RTE-8 and backend request plumbing RTE-13/RTE-14 are classify-only where their epistemic contribution is generation, acquisition, retention or use.

The question is which content a route checks, what its result licenses, and how that result changes use or execution. External provider reasoning, arbitrary test workloads, debugger interpretations, deployed extension evaluators, remote-memory core semantics, and security/cleanse/commit pipelines remain unassessed. Full depth applies to the listed routes; it is not a claim of exhaustive whole-product warrant.

## Lens outputs

### Memory/context lens

The inventory distinguishes accumulated session history, model-made summaries, explicit lessons, generated procedures, remote/backend memory, and static instructions. Session branch reconstruction and persisted compaction are read-back when a later invocation consumes them. Current-turn state alone is not. Local extraction and Auto-Learn additionally transform traces into durable later-use artifacts, so their enabled paths qualify as trace learning in the comparison's architectural sense.

**Local memory.** Backend selection is exclusive and defaults to off; Auto-Learn is separately off by default (SRC-1 `packages/coding-agent/src/memory-backend/resolve.ts:20-26`; `packages/coding-agent/src/config/settings-schema.ts:2987-3013,3027-3054`). With local enabled, RTE-5 scans prior persisted sessions, excludes current/ephemeral/child work, and applies cwd, age, idle, source watermark, concurrency and lease predicates. The extractor receives bounded messages and selected bash/eval/read/grep results. It writes structured per-session outputs; the consolidator creates project summaries and optional procedure bundles. SQLite bookkeeping ties extraction to source session/update state. It supports incremental maintenance and retries, not a verified truth lineage (SRC-1 `packages/coding-agent/src/memories/index.ts:334-451,477-603,643-806,872-1009`; `packages/coding-agent/src/memories/storage.ts:137-217,493-521`).

The later model receives a bounded summary/lesson block, or pulls a full artifact through memory://. Local search is not a semantic-retrieval service: the local backend declares structured search unavailable (SRC-1 `packages/coding-agent/src/memory-backend/local-backend.ts:34-45`). RTE-6 spends the shared injection budget on the summary first. Lessons may get no remaining space. Its per-session cache intentionally keeps a lesson written during startup for the next session; background startup can refresh the summary without refreshing those lessons (SRC-1 `packages/coding-agent/src/memories/index.ts:210-293`). Thus stored, selected, delivered and behaviorally used remain distinct states.

RTE-7 writes lessons before optional skill creation. Local lesson maintenance normalizes text, redacts common secret patterns, strips selected delimiters, deduplicates exact lines, caps entries, and serializes same-process writes; it does not semantically prove safe or correct content. Failure in the optional skill branch can leave the lesson durable (SRC-1 `packages/coding-agent/src/tools/learn.ts:51-138`; `packages/coding-agent/src/memories/index.ts:1292-1419`). Local summaries are explicitly heuristic guidance to check against current repository evidence (BAP-2). Parse/schema/nonempty checks in RTE-5 do not perform that downstream verification.

**Managed procedures.** Automatic Auto-Learn runs a private capture model over a detached completed-turn trajectory subject to trigger guards; the model can choose learn/manage_skill or decline to store anything. Passive mode supplies guidance without that automatic capture. Managed SKILL.md lives under the agent directory, separately from local consolidation's project skill bundles (RTE-10/RTE-11; SRC-1 `packages/coding-agent/src/autolearn/controller.ts:73-150`; `packages/coding-agent/src/sdk.ts:1203-1255,4191-4215`). Manage_skill refreshes discovery after mutations; learn's optional skill branch only writes. Dedicated managed-store checks constrain names, paths, sizes and link cases, not arbitrary shell or extension behavior.

RTE-12 still discovers retained managed skills after capture is disabled. The master skills switch, filters and authored/custom name precedence control actual visibility. Descriptions enter a routing catalog; a selected body is framed as instructions. This supports BAP-3 instruction authority without evidence that a model selected the right procedure or that its use improved work (SRC-1 `packages/coding-agent/src/discovery/builtin.ts:309-336`; `packages/coding-agent/src/extensibility/skills.ts:345-408,499-538`; SRC-2 `packages/coding-agent/src/prompts/skills/user-invocation.md:1-8`).

**Alternative backends.** RTE-13 exposes Mnemopi working/episodic/fact stores, scoped recall, transcript retention cursors and consolidation requests. Factual extraction input is separated from transcript episodes marked with unknown veracity. Children alias parent resources; top-level lifecycle owns automatic recall/retention. The adapter distinguishes row editing, episodic invalidation and read-only facts. Underlying in-repo Mnemopi algorithms were not inspected, so adapter wiring does not establish ranking, decay, embedding or extraction quality (SRC-1 `packages/coding-agent/src/mnemopi/state.ts:472-624,645-700,736-780`).

RTE-14 sends Hindsight bank-scoped retention/recall requests and supplies cached mental models or recall as background context. Its asynchronous retention and bounded startup/shutdown do not prove server materialization. Clear resets local cache/state, not the server bank. Children share parent bank/tool access without running their own automatic lifecycle (SRC-1 `packages/coding-agent/src/hindsight/backend.ts:41-147,198-265`). BAP-4 keeps this content advisory, including separate advisor framing.

RTE-15 extracts Sharpshooter decision deltas from user turns and consolidates them into project architecture/product/style files. Literal evidence-substring and shape checks occur before admission. The friction fields must be booleans, but no branch requires one to be true. Therefore friction-based selection remains a model policy, and the quote check establishes occurrence rather than support for the decision. Later read-back instructs the model to follow those decisions unless the user overrides: BAP-5 is stronger than local heuristic framing (SRC-1 `packages/coding-agent/src/sharpshooter/extract.ts:252-310`; `packages/coding-agent/src/sharpshooter/backend.ts:78-125`). Worker visibility consequently depends on backend: shared parent banks for Mnemopi/Hindsight, cwd-relative roots for local files, and explicit context/tool grants for advisors.

**Legacy review detection:** false. The selected whole target's primary offered work is coding-agent execution (CLM-1). Embedded memory capabilities do not turn the selected product into a primary memory/knowledge/context-engineering system. Invocation disposition: legacy review not applicable; the legacy publication workflow was not invoked.

No route establishes contextual activation or causal improvement. Read-back, procedure authority and automatic writes are supported as wiring; faithfulness remains uninspected. The comparison uses these established findings without inferring properties from missing tags or a legacy review.

### Epistemic lens

#### 1. Source-and-claim boundary

This overlay uses SRC-1 implementation and SRC-2 doctrine at the frontmatter revision. It asks what each material check permits a consumer to rely on. Assessed and classify-only families are fixed in Epistemic scope; excluded external services and unassessed security/cleanse/commit/debugger/provider families cannot supply warrant by implication. CLM-2–CLM-8 attach consequential promises to these routes. No inspected observed-run or causal-experiment source supports a candidate state.

#### 2. Epistemic-object annotations

Generic identity, form, substrate and producer/consumer remain in the indicated canonical object. The evidence column points to its canonical source account; no lens-local identity is introduced.

| Object | Truth-apt content or non-truth-apt part; lineage/warrant annotation | Evidence/limit |
|---|---|---|
| OBJ-1 | heterogeneous claims imported from user/model/tool messages, with role/branch metadata; retention preserves an account, not its truth | see OBJ-1, SRC-1; no actual session instance inspected |
| OBJ-2 | intended compressed history; semantic preservation vs omitted/invented content indeterminate | see OBJ-2, SRC-1; no summary-to-source comparison |
| OBJ-3 | distilled factual/process claims and procedure bundles; indeterminate preservation/generalization | see OBJ-3, SRC-1; parser checks are not semantic checks |
| OBJ-4 | backend facts/episodes can be truth-apt; scope/veracity metadata does not independently warrant facts | see OBJ-4, SRC-1; core algorithms and instances uninspected |
| OBJ-5 | action request, no necessary candidate truth proposition | see OBJ-5, SRC-1; schema validates shape |
| OBJ-6 | task-dependent findings; acquisition, reshaping, derivation or conjecture remain possible | see OBJ-6, SRC-1; schema conformance is separate |
| OBJ-7 | instructions/configuration and policy predicates, no required truth-apt candidate | see OBJ-7, SRC-1; content presence does not establish obedience |
| OBJ-8 | imported executor account, possibly extension-transformed | see OBJ-8, SRC-1; source warrant can change with installed hooks |
| OBJ-9 | model extraction from bounded traces, possibly lossy reshaping/generalization | see OBJ-9, SRC-1; provenance identifies source/update, not entailment |
| OBJ-10 | lesson observations and process recommendations; semantic relation indeterminate without content | see OBJ-10, SRC-1; dedup/normalization is not acceptance |
| OBJ-11 | procedural instruction and selection metadata; any embedded factual assertion needs separate evaluation | see OBJ-11, SRC-1; dedicated path checks do not verify skill utility |
| OBJ-12 | acquired/retained remote content | see OBJ-12, SRC-1; request success not server materialization |
| OBJ-13 | imported recalled context/mental model | see OBJ-13, SRC-1; remote transformation and warrant unknown |
| OBJ-14 | proposed decision statement with quoted user evidence and rationale | see OBJ-14, SRC-1; occurrence check cannot decide whether statement is entailed or generalized |
| OBJ-15 | project behavioral prescriptions | see OBJ-15, SRC-1; instruction force does not confer truth |
| OBJ-16 | proposed program update, no necessary claim in the patch itself | see OBJ-16, SRC-1; applicability differs from correctness |
| OBJ-17 | byte/anchor compatibility predicate within a symbolic domain | see OBJ-17, SRC-1; no license for intended program semantics |
| OBJ-18 | acquired analyzer judgments | see OBJ-18, SRC-1; valid only within analyzer configuration/domain |
| OBJ-19 | candidate patch-introduced bug/impact claims, ampliative conjecture | see OBJ-19, SRC-2; output schema cannot verify reasoning |
| OBJ-20 | candidate risk/correctness judgments, ampliative conjecture | see OBJ-20, SRC-1/SRC-2; no independently checked instance |
| OBJ-21 | suggestion part of advice, non-truth-apt policy/content | see OBJ-21, SRC-1 |
| OBJ-22 | imported harness output, process status and parsed measurement | see OBJ-22, SRC-1; benchmark validity external |
| OBJ-23 | model interpretation, supplied metric and keep/discard judgment over measurement | see OBJ-23, SRC-1; supplied values can differ from parsed evidence |
| OBJ-24 | arithmetic derivation over selected metrics | see OBJ-24, SRC-1; descriptive ratio, not probability/causality |
| OBJ-25 | proposed causal/improvement explanation or hypothesis, ampliative where it goes beyond measurements | see OBJ-25, SRC-1/SRC-2; no concrete instance |
| OBJ-26 | goals, constraints and next actions in playbook | see OBJ-26, SRC-1; may be used before truth-apt content is accepted |

#### 3. Authority-route ledger

Architectural status is **implemented** for every row below. This is the epistemic procedure's architectural vocabulary, separate from the enclosing result's wired conclusion status. Activation is conditional on each canonical trigger/configuration, and no candidate execution was observed. Rows sharing a canonical route describe distinct linked functions; checking, disposition, retention and use are never treated as one epistemic act. “No content change” refers to the checked/consumed object even when a scheduling or filesystem consequence follows. Generic endpoints, timing and recovery are in the canonical route and audit.

| Route/function | Content/update relation; object and target before evaluator | Operative result, epistemic license, operational/behavioral force | Claim/evidence and limit |
|---|---|---|---|
| RTE-1 — content transformation | indeterminate; requested output and OBJ-5/OBJ-6-like content, evaluated/generated by selected model | candidate response/call; no general truth license; model output drives RTE-2 and BAP-1 | CLM-1; SRC-1 `packages/agent/src/agent-loop.ts:1593-1639,1750-1760`; task-specific semantics unknown |
| RTE-2 — check/evidence production | acquisition/import; OBJ-8 executor result, tool/environment produces evidence | result/error can guide next action; license limited to actual executor and installed hook chain, BAP-1/BAP-8 | CLM-1; SRC-1 `packages/agent/src/agent-loop.ts:1437-1479`; arbitrary tool validity excluded |
| RTE-3 — retention | no content change; OBJ-1 account, SessionManager append | entry identity/durable history for later selection; no acceptance transition | SRC-1 `packages/coding-agent/src/session/session-manager.ts:2281-2292` |
| RTE-3 — operational admission/selection/consumption | no content change; selected branch, SessionContext ancestry/reset rules | messages admitted to later context, BAP-1; lineage selection only | SRC-1 `packages/coding-agent/src/session/session-context.ts:226-285,410-499` |
| RTE-4 — content transformation | indeterminate; OBJ-2 history summary, summarizer model or chosen external compaction route | compressed/replacement history; intended reshaping, preservation not demonstrated | SRC-1 `packages/agent/src/compaction/compaction.ts:1792-1873` |
| RTE-4 — retention | no content change to completed summary; maintenance stores boundary and rebuilds | later BAP-1 use; storage does not verify summary | SRC-1 `packages/coding-agent/src/session/session-maintenance.ts:1487-1541` |
| RTE-5 — content transformation | indeterminate; OBJ-9/OBJ-3, extraction then consolidation models over bounded trace lineage | raw memory/summary/procedures; reshaping or ampliation possible, no semantic truth grant | CLM-4; SRC-1 `packages/coding-agent/src/memories/index.ts:643-806,872-954` |
| RTE-5 — check/evidence production | no content change; proposed consolidated output, JSON/schema/nonempty validator | well-shaped/nonempty or reject; syntax/shape license only | SRC-1 `packages/coding-agent/src/memories/index.ts:921-954` |
| RTE-5 — retention | no content change; parsed/sanitized OBJ-3, file application | replaces memory files/assets for later BAP-2 use; no repository check at this transition | SRC-1 `packages/coding-agent/src/memories/index.ts:957-1009` |
| RTE-6/RTE-12 — operational admission/selection/consumption | no content change except bounded presentation; OBJ-3/OBJ-10/OBJ-11, scope/cache/filter/name selection | BAP-2 advisory context; BAP-3 routing and instruction; selection/freshness do not endorse content | CLM-4; SRC-1 `packages/coding-agent/src/memories/index.ts:210-293`; `packages/coding-agent/src/extensibility/skills.ts:345-408,499-538` |
| RTE-7/RTE-11 — retention | authored lesson/procedure update; OBJ-10/OBJ-11, bounded formatter/path checks | stored or rejected/partial outcome; format/path license, not truth; later BAP-2/BAP-3 | SRC-1 `packages/coding-agent/src/tools/learn.ts:51-138`; `packages/coding-agent/src/tools/manage-skill.ts:34-99` |
| RTE-10 — content transformation | indeterminate truth-apt extraction or non-truth-apt procedure creation; capture model over detached trajectory | invokes write tools or no output; reusable-content selection remains model judgment | SRC-1 `packages/coding-agent/src/autolearn/controller.ts:73-150`; `packages/coding-agent/src/sdk.ts:1203-1255` |
| RTE-9 — operational admission/selection/consumption | no content change or callback argument revision; OBJ-5 under tool/user/mode/UI policy | BAP-6 permits/blocks execution; user authorization is not epistemic acceptance | SRC-1 `packages/coding-agent/src/extensibility/extensions/wrapper.ts:180-345` |
| RTE-9 — content transformation | indeterminate; OBJ-8 original tool account, optional result callback | content/details/error may change before model consumption; license depends on hook behavior | SRC-1 `packages/coding-agent/src/extensibility/extensions/wrapper.ts:371-415` |
| RTE-13/RTE-14 — retention | acquisition/import; transcript/explicit retain content, backend adapter request | server/core request and local cursors/cache; external materialization not established | CLM-4; SRC-1 `packages/coding-agent/src/mnemopi/state.ts:472-589`; `packages/coding-agent/src/hindsight/backend.ts:198-265` |
| RTE-13/RTE-14 — operational admission/selection/consumption | acquisition/import at response, then no content change in delivery; returned recall, scope/query/wrapper | BAP-4 background knowledge; imported authority bounded by uninspected core/server | SRC-1 `packages/coding-agent/src/mnemopi/backend.ts:54-64,138-150`; `packages/coding-agent/src/hindsight/backend.ts:21-29,86-101` |
| RTE-15 — content transformation | indeterminate decision extraction; OBJ-14 user evidence, model | candidate delta; occurrence does not establish entailment, generalization or authority | SRC-1 `packages/coding-agent/src/sharpshooter/extract.ts:171-249` |
| RTE-15 — check/evidence production | no content change; OBJ-14 candidate, literal evidence substring plus shape/enum/boolean predicates | accept/reject for storage eligibility; proves quote occurrence, not decision warrant or true friction flag | SRC-1 `packages/coding-agent/src/sharpshooter/extract.ts:252-310` |
| RTE-15 — retention | model-consolidated policy/content update; OBJ-14/OBJ-15, background consolidator | replaces files/consumes deltas; storage, not epistemic integration | SRC-1 `packages/coding-agent/src/sharpshooter/consolidate.ts:123-198,218-226` |
| RTE-15 — operational admission/selection/consumption | no content change; OBJ-15, project/budget selector | BAP-5 instruction force unless user overrides; no semantic check prerequisite | SRC-1 `packages/coding-agent/src/sharpshooter/backend.ts:78-125` |
| RTE-16 — check/evidence production | no content change; OBJ-6 vs declared schema, JSON validator | valid/invalid/unavailable; licenses schema conformance only | CLM-3; SRC-1 `packages/coding-agent/src/tools/output-schema-validator.ts:56-106` |
| RTE-16 — operational admission/selection/consumption | no content change; validator result, mode/override/abort/fallback finalizer | BAP-7 success/failure/warning controls parent return; permissive exceptions are explicit, not blanket bypass | CLM-3 qualification; SRC-1 `packages/coding-agent/src/task/executor.ts:668-812` |
| RTE-17 — lineage/freshness/recovery | no content change to candidate patch; OBJ-17 current/snapshot/anchors, symbolic check/remapping | match/recover/mismatch; applicability only, BAP-7 | CLM-6; SRC-1 `crates/pi-edit/src/modes/hashline/patcher.rs:185-250`; `crates/pi-edit/src/modes/hashline/recovery.rs:123-186` |
| RTE-17 — operational admission/selection/consumption | non-truth-apt program update; OBJ-16, patch engine after applicability decision | apply/reject; head/tail drift can warn/apply; no semantic correctness license | CLM-6 literal-stale-rejection mismatch; SRC-1 `crates/pi-edit/src/modes/hashline/patcher.rs:210-250` |
| RTE-18 — check/evidence production | acquisition/import; written file, configured external analyzers | OBJ-18 diagnostics/version/status; analyzer-domain evidence after mutation | CLM-1; SRC-1 `packages/coding-agent/src/lsp/writethrough.ts:347-472` |
| RTE-18 — operational admission/selection/consumption | no content change; diagnostics, inline/deferred budget | BAP-8 feedback can inform revision; no inspected pre-write rejection or automatic rollback in this path | SRC-1 `packages/coding-agent/src/lsp/writethrough.ts:241-288,449-472` |
| RTE-19 — content transformation | ampliative conjecture; OBJ-19 possible bug/impact, reviewer model under patch criteria | prioritized findings/verdict, BAP-8 advice to parent/operator; no inspected release blocker | CLM-5; SRC-1 `packages/coding-agent/src/extensibility/custom-commands/bundled/review/index.ts:180-267`; SRC-2 `packages/coding-agent/src/prompts/agents/reviewer.md:57-84,111-134` |
| RTE-20 — content transformation | ampliative conjecture for OBJ-20; non-truth-apt suggestions for OBJ-21; advisor model evaluates primary trace | note/severity/silence; model risk judgment, not independent confirmation | CLM-7; SRC-1 `packages/coding-agent/src/advisor/runtime.ts:1113-1201`; SRC-2 `packages/coding-agent/src/prompts/advisor/system.md:13-16,29-54,79-91` |
| RTE-20 — operational admission/selection/consumption (emission) | no content change; note, noise/dedup/rate guard | suppress/deliver; internal acceptance means channel eligibility | SRC-1 `packages/coding-agent/src/advisor/emission-guard.ts:103-175` |
| RTE-20 — operational admission/selection/consumption (primary delivery) | no content change; admitted note/severity, primary-state scheduler | BAP-9 aside/preserved card/steer; content explicitly advisory while blocker can interrupt/reopen | CLM-7 qualification; SRC-1 `packages/coding-agent/src/advisor/advise-tool.ts:45-64,119-134`; `packages/coding-agent/src/session/session-advisors.ts:1220-1290` |
| RTE-21 — check/evidence production | no content change; selected stream/tool content, regex/AST predicate | policy match; neither truth judgment nor observed model violation in this run | CLM-2; SRC-1 `packages/coding-agent/src/session/ttsr-coordinator.ts:82-105,328-386` |
| RTE-21 — behavior/policy adaptation | non-truth-apt policy-content update; matched rule/interrupt mode, coordinator | BAP-10 reminder/abort/retry/follow-up with optional context discard; scheduling enforced, compliance model-dependent | CLM-2; SRC-1 `packages/coding-agent/src/session/ttsr-coordinator.ts:125-141,251-297,389-459` |
| RTE-22 — check/evidence production | acquisition/import; candidate code, fixed benchmark harness | OBJ-22 log/process/parsed metric; license limited to harness measured outcome | CLM-8; SRC-1 `packages/coding-agent/src/autoresearch/tools/run-experiment.ts:81-136,143-195,227-235` |
| RTE-23 — disposition/acceptance | no content change to evidence; pending run plus model-supplied status/metric, logger/Git | BAP-11 keep commits on dedicated branch, other outcomes invoke revert; intended correctness/improvement application belongs to model | CLM-8; SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:64-83,124-202`; criterion fidelity not a code invariant |
| RTE-23 — retention | no content change; supplied interpretation plus parsed evidence, logger | durable record/flags/commit lineage; retaining a keep does not independently accept its explanation | SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:174-217` |
| RTE-24 — content transformation | entailed derivation within arithmetic domain; selected OBJ-23 metrics, median/MAD calculation | OBJ-24 or null; describes best change relative to variation, not probability or causal effect | SRC-1 `packages/coding-agent/src/autoresearch/state.ts:144-169` |
| RTE-25 — retention | indeterminate truth-apt text update for OBJ-25, non-truth-apt policy update for OBJ-26; model text setter | replace/append notes; no semantic evaluation in setter | SRC-1 `packages/coding-agent/src/autoresearch/tools/update-notes.ts:24-69` |
| RTE-25 — operational admission/selection/consumption | no content change; active session/branch and notes renderer | BAP-12 next-iteration system context; speculative guidance can enter without acceptance | SRC-1 `packages/coding-agent/src/autoresearch/index.ts:294-316,378-404` |

RTE-8 supplies task execution/return; its candidate generation shares RTE-1's indeterminate content classification and its output check/disposition is separately annotated as RTE-16. No standalone lifecycle-integration row is asserted merely because a result is retained or consumed.

#### 4. Per-object lifecycle dispositions

**Observed candidate state is no instance observed for every phase below.** Implementation and doctrine alone do not establish that an actual candidate was accepted, rejected, revised, failed, suspended or integrated.

| Ampliative object | Observation/anomaly | Conjecture | Derived consequence | Test/evidence | Acceptance: evaluator, criterion, intended use/scope | Lifecycle integration and missing evidence |
|---|---|---|---|---|---|---|
| OBJ-19 | RTE-19 diff/context acquisition: architectural status implemented | RTE-19 reviewer-model production: implemented | concrete impacted paths required by reviewer template: doctrine only | reading consumers/grounding bug evidence prescribed: doctrine only for candidate-linked testing, with generic tools implemented | reviewer model judges patch-introduced correctness under SRC-2 template; evaluative protocol doctrine only, output admission RTE-16 implemented; accepted scope unestablished | downstream release/merge acceptance and post-acceptance change: not determinable; no candidate, validated reasoning or consumer decision. SRC-2 `packages/coding-agent/src/prompts/agents/reviewer.md:57-84,111-134` |
| OBJ-20 | RTE-20 primary-trace acquisition: implemented | separate advisor model: implemented | concrete risk/impact instruction: doctrine only | personally verify before raising concerns: doctrine only as candidate evidence; investigation tools afforded by runtime | primary model is eventual evaluator of advice for current work; acceptance criterion application not determinable; emission guard implemented but checks delivery only | RTE-20 delivery is pre-acceptance operational use; post-acceptance integration not determinable. Need note-linked evidence and primary response. SRC-2 `packages/coding-agent/src/prompts/advisor/system.md:29-54,79-91`; SRC-1 `packages/coding-agent/src/advisor/emission-guard.ts:103-175` |
| OBJ-25, when causal/improvement hypothesis exceeds measurements | RTE-22 measurement: implemented | model proposal and RTE-25 storage/delivery: implemented, particular semantic content unobserved | improvement/correctness implication: doctrine only as explicit hypothesis-derived consequence | RTE-22 harness execution: implemented; hypothesis-to-run linkage not determinable | experimenting model judges primary metric improvement while preserving correctness for continuing optimization; intended criterion SRC-2, doctrine only as faithful epistemic application; RTE-23 operational disposition implemented; accepted explanatory scope unestablished | kept code can change next working state, but accepted explanatory claim and evidence-linked post-acceptance integration not determinable. RTE-25 use can precede acceptance. SRC-2 `packages/coding-agent/src/autoresearch/prompt.md:28-45`; SRC-1 `packages/coding-agent/src/autoresearch/tools/log-experiment.ts:124-202` |

The remaining objects receive these dispositions:

- **Indeterminate transformation:** OBJ-1/OBJ-2/OBJ-3/OBJ-4/OBJ-6/OBJ-9/OBJ-10/OBJ-14/OBJ-23. Their canonical source lineage and implemented shape checks, retention and use remain explicit. Acquisition, lossy or faithful reshaping, entailed derivation and ampliative conjecture remain possible according to concrete content. A particular source/output pair, candidate-linked checks, and disposition evidence would be needed to decide. Neither compaction nor consolidation is presumed semantically preserving merely because that is its purpose.
- **Acquisition/import; discovery lifecycle not applicable:** OBJ-8/OBJ-12/OBJ-13/OBJ-18/OBJ-22. Executor/server/analyzer/harness output is acquired, not produced knowledge. Exact source linkage is wired in the named route, but external validity is uninspected; extension result rewriting can make preservation indeterminate for a particular OBJ-8 instance.
- **Entailed derivation; discovery lifecycle not applicable:** OBJ-17/OBJ-24. Their domains are checked byte/anchor relations and arithmetic over selected reported numbers. The licenses exclude source truth, encoding fidelity outside those predicates, program correctness, benchmark generality, and causal attribution.
- **No lifecycle record for OBJ-5:** no candidate truth-apt output is required by the action request; relevant update/dispatch routes RTE-1/RTE-2/RTE-9.
- **No lifecycle record for OBJ-7:** configured policy is consumed through RTE-1/RTE-9/RTE-21; its authority does not require a candidate truth claim.
- **No lifecycle record for OBJ-11:** the operative procedure/routing part is non-truth-apt; RTE-10/RTE-11/RTE-12 create, retain and consume it. Any concrete embedded factual claim would need separate candidate evidence.
- **No lifecycle record for OBJ-15:** project prescriptions are retained and used through RTE-15; decision-evidence content is separately OBJ-14.
- **No lifecycle record for OBJ-16:** program update is not itself a required truth-apt claim; RTE-17 applies it.
- **No lifecycle record for OBJ-21:** advice's suggestion part follows RTE-20.
- **No lifecycle record for OBJ-26:** playbook policy follows RTE-25. Retention and later instruction use do not constitute epistemic acceptance.

#### 5. System claims versus routes

Every row has **observed-run support: uninspected** and **causal support: uninspected**. README screenshots, linked clips and benchmark statements are doctrine/attributed claims here; none is an inspected intervention.

| Claim | Doctrine/design support | Implemented routes | Supported conclusion and mismatch/unknown |
|---|---|---|---|
| CLM-1 | SRC-2 `README.md:6-27,133-151` | RTE-1/RTE-2/RTE-9/RTE-18 | integrated coding runtime is wired; analyzer/provider/OS performance and full breadth unassessed |
| CLM-2 | SRC-2 `README.md:155-157` | RTE-21/RTE-3 | conditional matching, interruption/reminder, retry and injection retention wired; noninterrupting modes exist; behavioral correction unobserved |
| CLM-3 | SRC-2 `README.md:163-165` | RTE-8/RTE-16 | schema checks are real; strict/permissive/override/no-schema paths differ. Isolation defaults off and enabled integration can conflict. Literal unconditional typed/no-conflict reading exceeds implementation |
| CLM-4 | SRC-2 `README.md:213-215`, `docs/memory.md:1-28` | RTE-5–RTE-7/RTE-10–RTE-15 | optional cross-session retention/distillation/read-back wired. Backend/capture defaults off; curation/injection does not establish verified knowledge or activation |
| CLM-5 | SRC-2 `README.md:201-203` | RTE-19/RTE-16 | criterion-shaped model review and structured reporting; command gives orchestration guidance to model; no inspected release-blocking consumer |
| CLM-6 | SRC-2 `README.md:113-120,205-207` | RTE-17 | unrecoverable stale anchors reject; recovery or head/tail warning permits other edits. Correctness/perfect-edit wording and token-saving magnitude unverified |
| CLM-7 | SRC-2 `README.md:173-175` | RTE-20 | separate model notes, filtered emission and severity-driven scheduling wired; finding missed issues is an unmeasured outcome; blocker force does not make note authoritative truth |
| CLM-8 | SRC-2 `packages/coding-agent/src/autoresearch/prompt.md:28-45,99-103` | RTE-22–RTE-25 | measurement → model selection → keep/revert/record → later iteration wired. Parsed/supplied metrics and scope deviations may warn without rejection; correctness and general improvement remain policy/evidence questions |

#### 6. Route-bounded conclusion

The strongest code checks here license a narrow domain: schema representation, edit applicability, permission policy, quote occurrence, or arithmetic. Language-server evidence is imported after effects. Reviewers/advisors produce candidate judgments; their output and delivery checks do not independently warrant content.

Autoresearch connects measurement, an intended improvement/correctness criterion, model disposition, retained records and later work. That is a substantive testing-and-selection architecture. Its logger acts on supplied status/metric and can retain discrepancies with parsed evidence. It therefore does not make honest metric reporting or faithful criterion application an invariant, and its confidence scalar does not establish component causality.

Memory and playbooks preserve or transform material for later reliance. Local heuristic guidance, managed procedure instructions, and Sharpshooter project prescriptions have different behavioral authority. TTSR and advisor blockers can enforce scheduling while leaving content compliance to the model. None of these findings supports a system-wide epistemic grade.

## Reconciliation

The runtime baseline and two bounded worker lenses used the same full commit and SRC-1/SRC-2 identities. All worker references resolved to those supplied sources; proposed objects/routes were registered into the single shared inventory. Memory proposals became OBJ-9–OBJ-15, RTE-10–RTE-15 and BAP-2–BAP-5. Epistemic proposals became OBJ-16–OBJ-26, RTE-16–RTE-25 and BAP-7–BAP-12. Generic session/tool/worker identity remains with CMP-1–CMP-5 and RTE-1–RTE-9. No worker-local tags survive as alternate canonical identities.

Initial combined claim seeds were split before finalization: stream correction stays CLM-2, worker guarantees become CLM-3, code review becomes CLM-5, and Hashline becomes CLM-6. Each final ID has one meaning. The shared backend object was narrowed to Mnemopi OBJ-4; Hindsight and Sharpshooter received distinct records because their storage, framing and authority differ. No accepted record ID was reused after rejection or merge.

The parent re-read the consequential spans for schema finalization, local cache/parse transitions, Sharpshooter admission, Hashline drift/recovery, and autoresearch keep handling. A preliminary shorthand that permissive worker validation could generally ignore schema failure was rejected: RTE-16 now states that ordinary valid-schema mismatches reject even in permissive mode, while explicit overrides, unusable schema and other documented branches can remain warning successes. Evidence: SRC-1 `packages/coding-agent/src/task/executor.ts:668-812`. This correction affects CLM-3, BAP-7 and the worker forcing case.

The README's broad stale-edit and isolated-worker wording remains anchored as claims, while implementation qualifications stay attached to RTE-8/RTE-16/RTE-17: isolation defaults off, merge failures are represented, and stale anchors can recover. Neither layer is silently preferred as a stronger conclusion. Local guidance and Sharpshooter instruction framing were not collapsed into one memory-authority value; only the explicitly narrower comparison boundary contributes its axes.

Both lenses separately found retained text used without a demonstrated acceptance prerequisite: the memory worker in local/managed memory and the epistemic worker in autoresearch notes. This is limited convergence across different routes, not independent replication of one same-route finding. Parent-shared observations about local semantic checks and Sharpshooter friction are not reported as independently rediscovered by the epistemic worker.

Cross-route ownership is explicit: RTE-3 owns transcript retention/reconstruction; RTE-4 owns summarization/boundaries; RTE-5/RTE-10 own extraction/capture; RTE-6/RTE-12 own later memory delivery; RTE-16 owns worker output admission within RTE-8; RTE-9 owns wrapped tool policy, not arbitrary host code. Final legacy detection remains false for the enclosing coding runtime. No legacy projection or its QA state is required.

## Bounded synthesis

At this pinned code boundary, oh-my-pi is an enclosing coding runtime with client modes around a common session/agent loop. Its distinguishing work is to assemble project/tool context, run model/tool turns, retain reconstructable session branches, delegate to separately configured worker sessions, and add optional memory and review workflows around those turns. Provider inference and host execution remain external contracts.

Three mechanisms change the operational reading. First, the session substrate reconstructs chosen history rather than merely replaying every stored event. Compaction, resets, branch ancestry and provider replay/archive payloads determine what reaches the next invocation. The persisted account and the external effects can therefore diverge; recovering a conversation does not roll back a shell or filesystem action.

Second, automatic durable memory has multiple enabled paths and different consumer authority. Local memory extracts idle prior sessions into bounded heuristic guidance; explicit lessons have a deliberate later-session cache horizon. Auto-Learn can capture reusable procedures whose discovery outlives the capture switch. Alternative banks and Sharpshooter project decisions have distinct visibility and invalidation rules. These mechanisms afford continued work across sessions, while the inspected code supports only wiring, not faithful recall, correct generalization, or beneficial activation.

Third, control outcomes are route-specific. A schema can constrain a worker's return shape; a Hashline predicate can check whether an edit still applies; LSP can supply diagnostics after a write; a blocker can interrupt the primary agent; a model's experiment disposition can commit or revert code. Those results do not share a single epistemic license. Autoresearch is the most explicit selected measurement-and-disposition loop, yet its code permits supplied metrics and scope deviations to survive as recorded warnings.

For a long coding task, the branch/compaction and memory paths explain how work can resume with selected context; actual retention fidelity requires execution evidence. For delegated workspace edits, optional isolation and explicit patch/branch recovery explain how results can be integrated; default shared working state and configurable schema handling limit unconditional isolation/typed-return claims. For review and optimization, judgments and metrics can become operationally consequential; current code does not establish that the judgment is correct or that any measured gain transfers beyond its harness.

The assessment would change with candidate-linked executions showing memory selection and behavior under recall interventions; strict-schema and drift/merge forcing runs at a declared deployed configuration; substantive bug/advisor findings linked to verified outcomes; or autoresearch records showing justified criteria and independent measurements. Source changes that move semantic criteria into actual admission consumers, alter default grants/isolation, or change memory read-back/invalidation would also require a new analysis pin. No product ranking, adoption prescription or Commonplace transfer conclusion follows.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| Static-only inspection | SRC-1/SRC-2 and all routes | commit-addressed source and shipped text, no target execution | observed reliability, activation, quality and causal improvement | retained runs/probes with declared inputs/environment and controlled comparisons where causal |
| Selected whole-runtime coverage | CMP-1–CMP-8 | entry/core/session/memory/task and selected checks; security/cleanse/commit/collaboration/browser/provider internals not exhaustively traced | system-complete security or epistemic guarantee | separately bounded traces of the omitted route families |
| Deployment configuration not supplied | RTE-1/RTE-8/RTE-9 | schema defaults and configurable paths | actual granted tools, active memory, strict schema, isolation or deployed provider behavior | exact sanitized effective settings, installed extensions and host configuration |
| Host effects outside transcript transaction | RTE-2/RTE-3/RTE-8/RTE-9 | inspected scheduling, persistence and cleanup/capture paths | exactly-once effects, rollback completeness, process/network containment | effect-linked fault/restart tests and OS/remote isolation contracts |
| Model summary/lesson fidelity | OBJ-2/OBJ-3/OBJ-9/OBJ-10; RTE-4–RTE-7 | bounded input, parse/shape checks, retention and prompt wrapper | preserved meaning, fact correctness, useful transfer or resistance to all injected instructions | retained source/output pairs, semantic checks and later-consumer interventions |
| Procedure correctness and selection | OBJ-11; RTE-10–RTE-12 | capture guards, confined mutation, catalog/body delivery | correct reusable code, appropriate skill matching or actual compliance | generated skill instances plus task-linked execution/evaluation |
| Backend internals/remote completion uninspected | OBJ-4/OBJ-12/OBJ-13; RTE-13/RTE-14 | adapter/state methods only | Mnemopi core extraction/ranking/decay or Hindsight storage/durable processing and deletion | pinned core/server analysis and completion/recall traces |
| Selective normalized comparison | memory-comparison; RTE-3–RTE-7/RTE-10–RTE-12 | explicitly local session/summary/lesson/managed-skill scope | treating axes as a union over all backend alternatives and experiment playbooks | separate expanded evidence and explicitly revised comparison scope in a new run |
| Candidate-linked acceptance missing | OBJ-19/OBJ-20/OBJ-25; RTE-19/RTE-20/RTE-23/RTE-25 | templates and implemented generation/disposition/use | verified bug/risk claims, accepted explanations or post-acceptance integration | candidate-linked evidence, evaluator decision/criterion and consequential later consumer |
| Applicability/check-domain limits | OBJ-6/OBJ-17/OBJ-18; RTE-16–RTE-18 | JSON schema, Hashline byte/anchor checks and analyzer feedback | semantic task correctness or universal edit correctness | task-specific evidence and analyzer/configuration coverage |
| Benchmark and component causality unassessed | CLM-6/CLM-8; RTE-22–RTE-24 | README metrics as claims; harness/logging arithmetic code | claimed speed/token gains, general optimization benefit or individual-component effects | pinned datasets, exact repeated measurements and appropriate independent interventions |

## Verification and blockers

### Semantic verification

Checked that the final register has one identity per ID; lens annotations resolve to it; each source-dependent record has a full commit-relative anchor; claims remain separate from code-supported wiring; and no implementation/doctrine evidence is upgraded to observation or causality. Parent targeted rereads confirmed the materially consequential corrections listed in Reconciliation. Every RTE-1–RTE-25 has explicit return, later-read, delegated-visibility, selection, invalidation and effect/evidence dispositions. Every operative object has an epistemic disposition, with separate architectural and observed-candidate vocabulary.

Checked primary-work detection and the narrower memory-comparison scope against the actual selected product. Checked that declared limits cover external inference/effects/backend cores, unassessed mechanism families, default-off memory/capture, conditional grants and unobserved activation. No unresolved semantic blocker remains.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-01/result.md`, using `commonplace-validate --full`. Result: PASS, with no warnings or failures. Frontmatter, ordered sections, type schema, link health, and all memory-comparison assessments/canonical references pass. Source-anchor existence and workflow identity are additionally checked before publication against the frozen commit.

### Blockers

None.
