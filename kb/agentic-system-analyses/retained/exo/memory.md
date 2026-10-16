---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Exo memory: versioned events, agent facts and skills, conversation plans, result previews and native context recovery."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
source-identity: "https://github.com/exoharness/exo"
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
---

# Exo memory report

## Boundary and evidence

The subject is the shipped Exo runtime, including the older persistent-agent experiment, at the boundary's frozen commit. Memory scope follows the managed Basic, Responses, native-agent, RLM, background-wakeup and maintenance routes. It includes conversation events, artifacts, managed instructions, installed capabilities, local profile text, durable facts, todos, skills, native thread recovery and sandbox checkpoints. Credentials and network policy are configuration dependencies, not treated here as knowledge stores. External model weights, native-agent algorithms and deployed data remain outside inspectable implementation. This prevents claims about their internal summarization, deployed retention or empirical memory quality.

All new findings use SRC-1, implementation unless explicitly called guidance/design. The supplied runtime is evidence of its author's static inspection, not an observed execution. Direct reads added the paths in the table; paths supporting supplied findings are identified as such. There is no execution or causal-experiment evidence. The checkout has no known access gap. Available but unread branches remain inspection limits.

| Entry point / operation | Source paths and inspection basis | Records / limit |
|---|---|---|
| CLI definition synchronization and managed turn | Supplied runtime: `crates/cli/src/main.rs`, `crates/cli/src/managed_agents.rs`, `crates/executor/src/managed_agents.rs`, `crates/executor/src/turn_queue.rs` | [RT-RTE-definition-admission](runtime.md#rt-rte-definition-admission), [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn); not re-audited branch by branch |
| Basic history and artifact versions | Direct: artifact helpers in `crates/exoharness/src/basic.rs`; scoped search of `crates/executor/src/basic.rs`; runtime supplies loop/recovery excerpts | [MEM-OBJ-artifact-versions](#mem-obj-artifact-versions), annotation on managed turn; no general semantic context-budget guarantee |
| Responses history and instruction construction | Direct: `exoharness/typescript/harness/index.ts`, `exo/harness.ts`; supplied runtime: `exoharness/typescript/model-runtime/turn-loop.ts` | Annotation on [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop); remaining event-conversion branches not exhaustively audited |
| remember / forget / automatic injection | Direct: `exo/tools/memory-tools.ts`, `exo/profiles/practical.ts` | [MEM-OBJ-exo-memory](#mem-obj-exo-memory), [MEM-RTE-fact-revision](#mem-rte-fact-revision) |
| todowrite / automatic plan injection | Direct: `exo/tools/todo-tools.ts`, `exo/harness.ts`, `exo/profiles/practical.ts` | [MEM-OBJ-exo-todos](#mem-obj-exo-todos), [MEM-RTE-plan-replacement](#mem-rte-plan-replacement) |
| install/list/use/read/uninstall skills | Direct: complete `exoharness/typescript/harness/skill-tools.ts`, profile registration | Separate catalog and payload records; [MEM-RTE-skill-lifecycle](#mem-rte-skill-lifecycle); alternate file-read path survives catalog removal |
| Tool-result offload and preview | Direct: compaction helpers in `exoharness/typescript/harness/tools.ts` | [MEM-RTE-result-offload](#mem-rte-result-offload); generic artifact APIs alone do not establish model-directed full reload |
| Codex native reuse / resume / replay / compaction | Direct: recovery/replay branch of `exoharness/typescript/codex/harness.ts`, complete `exoharness/typescript/codex/replay.ts` | [MEM-RTE-codex-compaction](#mem-rte-codex-compaction); native summary payload and algorithm opaque |
| Pi history; Claude and Cursor alternatives | Supplied [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge), `exoharness/examples/typescript/pi-harness.ts`; Claude/Cursor internals not inspected here | Pi transcript transformation supported provisionally; no parity or complete native-memory account |
| RLM selected-context subquery | Supplied `crates/executor/src/native/rlm.rs` | Annotation on [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery); turn-local isolation, not proven retained JS memory |
| Snapshot / rewind | Direct: snapshot, rewind and registry helpers in `crates/executor/src/native/harness_tool.rs` | [MEM-OBJ-sandbox-snapshots](#mem-obj-sandbox-snapshots), [MEM-RTE-sandbox-rewind](#mem-rte-sandbox-rewind); backend bytes/coverage not audited |
| Background results and pending delivery | Supplied `crates/executor/src/native/scheduler_runtime.rs`, `crates/executor/src/native/conversation_wakeup.rs` | Annotation on [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup); adapter-specific filtering, acknowledgement and deletion semantics unresolved |
| History/telemetry introspection | Direct registration in `exo/tools/introspection-tools.ts` | [MEM-CLM-history-inspection](#mem-clm-history-inspection); host-side filter implementation not rechecked |
| Installed tools / source rebuild | Supplied registry and guardian findings; direct Exo registration and guidance | Annotations on [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), [RT-OBJ-guardian-update](runtime.md#rt-obj-guardian-update); not duplicates of text skills |
| Local profile and identity | Direct `exo/harness.ts` | Annotation on [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions); initial authorship and external file-edit control unresolved |
| Cloudflare, UI and Harbor consumers | Supplied boundary/runtime paths: `exoharness/cloudflare/src/provider.ts`, `website/src/chat.jsx`, `eval/harbor/src/exo_harbor/agent.py` | Hosted recovery and trajectory export retained as supplied facts; not a separate verified learning/adoption loop; host-specific retention, UI selection and evaluator outcome gates uninspected |

## Core ideas

Exo separates persistence from context policy. Managed configuration, events and artifacts can survive invocations; the selected harness chooses what reaches the model. This is not one universal memory algorithm. Basic recovery uses journal structure; Responses reconstructs messages; Codex may keep a native thread or replay Exo history through native compaction. See the route annotations and [MEM-RTE-codex-compaction](#mem-rte-codex-compaction).

The persistent-agent profile has three distinct textual stores. Facts are agent-wide and automatically pushed in full; todos are conversation-local and shown only while work remains open; skills push catalog metadata and require a foreground tool request for the body. Their consumers have different withdrawal rules. In particular, uninstalling a skill removes its catalog membership, not its payload or every read route. See [MEM-RTE-skill-lifecycle](#mem-rte-skill-lifecycle).

“Authoritative context” is a prompt instruction attached to saved facts, not a truth-verification rule. The store records text, ID and time, not evidence or reasons. The tool can also save facts about the agent itself; the narrower harness instruction about user preferences does not restrict the handler to that origin. There is no independent answer oracle in these inspected write paths. See [MEM-RTE-fact-revision](#mem-rte-fact-revision).

Tool-result “compaction” is deterministic offload plus truncation, not a semantic summary. Codex replay compaction is a separate host request whose actual representation is opaque. Neither the preview nor an opaque native checkpoint should be mistaken for a complete readable account of retained reasons. See [MEM-RTE-result-offload](#mem-rte-result-offload) and [MEM-RTE-codex-compaction](#mem-rte-codex-compaction).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-artifact-versions
Label: Artifact versions

Source-native identity: Basic `ArtifactVersion` metadata and corresponding stored contents. Form: symbolic IDs, paths, version/time/size metadata; contents are opaque bytes until decoded by an actual consumer. Substrate: Basic object store, with version-numbered `.json` metadata and `.bin` bytes under an artifact-ID directory. Lineage: caller-supplied bytes, not automatically derived knowledge. Same-path writes choose the highest existing version and increment it. Agent, conversation and turn scopes are distinct handles. SRC-1: `crates/exoharness/src/basic.rs`.

> let version = existing.map(|artifact| artifact.version + 1).unwrap_or(1);
> --- `crates/exoharness/src/basic.rs`

> artifact_dir.join(format!("{version}.bin")),
> --- `crates/exoharness/src/basic.rs`

Consumers below select versions through list/read operations. Metadata locates payload; it is not the payload's meaning. The inspected writer stores metadata and bytes separately, so versioning alone proves neither atomicity nor compare-and-swap. Old versions are reachable storage capability, not automatic rollback or automatic model recall. Closest supplied referents are [RT-OBJ-turn-work](runtime.md#rt-obj-turn-work) and [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), neither the same store/referent. Specific artifacts below are distinct logical parts, not duplicates of those records.

#### MEM-OBJ-exo-memory
Label: Exo memory

Source-native identity: agent artifact `memory/exo-memory.json`, entries containing `id`, `text`, `createdAt`. Form: natural-language facts plus symbolic IDs/timestamps and JSON envelope. Substrate: versioned agent artifact, shared across conversations. Lineage: text supplied by a tool caller/model; user, agent-self and potentially other task-derived origins are possible, actual deployed provenance unknown. It does not retain a structured source/reason field. Later consumers are the memory reader/editor and the model receiving developer-message entries. SRC-1: `exo/tools/memory-tools.ts`.

> const MEMORY_ARTIFACT_PATH = "memory/exo-memory.json";
> --- `exo/tools/memory-tools.ts`

This is retained content feeding [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions), not that authority path itself. No counterpart object is declared in the supplied runtime. Revision and authority are established by [MEM-RTE-fact-revision](#mem-rte-fact-revision).

#### MEM-OBJ-exo-todos
Label: Exo todos

Source-native identity: conversation artifact `todos/exo-todos.json`. Form: natural-language task text plus symbolic status (`pending`, `in_progress`, `completed`, `cancelled`). Substrate: versioned conversation artifact. Lineage: full-list tool proposals, not an automatic extraction from the transcript. Model receives all items only while at least one remains open. Completion is caller assertion; verification is requested in prose, not encoded as evidence. SRC-1: `exo/tools/todo-tools.ts`.

> const TODO_ARTIFACT_PATH = "todos/exo-todos.json";
> --- `exo/tools/todo-tools.ts`

Distinct from agent-wide facts and from [RT-OBJ-turn-work](runtime.md#rt-obj-turn-work), which stores queued execution rather than the model's task list. No supplied object counterpart; [MEM-RTE-plan-replacement](#mem-rte-plan-replacement) owns the lifecycle.

#### MEM-OBJ-skills-index
Label: Skills index

Source-native identity: agent artifact `skills/index.json`, with name, description and installed/updated times. Form: symbolic membership/names/times plus natural-language retrieval descriptions. Substrate: agent artifact versions. Lineage: installation frontmatter plus software timestamps; not semantic model summarization. Consumer: automatic developer-message catalog and membership check in `use_skill`. Metadata selects access; it is not the full skill. SRC-1: `exoharness/typescript/harness/skill-tools.ts`.

> const SKILLS_INDEX_ARTIFACT_PATH = "skills/index.json";
> --- `exoharness/typescript/harness/skill-tools.ts`

No supplied object counterpart: unlike [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), these entries advertise textual procedures, not initialized executable handlers.

#### MEM-OBJ-skill-record
Label: Skill record

Source-native identity: `SkillRecord` at `skills/${name}.json`, holding name, description, full `skillMd` and supporting files. Form: natural-language procedure and arbitrary supporting text; code text remains text at this reader, not automatically executed. JSON and file names are symbolic access structure. Substrate: versioned agent artifact. Lineage: submitted skill text and files, possibly fetched externally by a foreground agent; no authenticated origin imposed by this handler. Consumer: foreground model via `use_skill` / `read_skill_file` tool output, subject to generic result offload. SRC-1: `exoharness/typescript/harness/skill-tools.ts`.

> return `skills/${name}.json`;
> --- `exoharness/typescript/harness/skill-tools.ts`

Distinct from its catalog and executable [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry). It may contain rationale if submitted text includes it; no mandatory reasons schema exists. Later body reads preserve that supplied text before generic result truncation, not necessarily within the model window.

#### MEM-OBJ-sandbox-snapshots
Label: Sandbox snapshots

Source-native identity: backend snapshot IDs and `SandboxSnapshotRegistry` entries/current references. Form: symbolic scope, sandbox/owner/snapshot IDs and registry; checkpoint bytes are opaque backend state, not a readable summary. Substrate: backend snapshot plus agent-artifact registry. Lineage: actual sandbox state at requested capture; exact file coverage depends on backend, not inspected here. Consumers: list tool, rewind handler and backend `start_sandbox`, then later commands using restored filesystem. SRC-1: `crates/executor/src/native/harness_tool.rs`.

> .start_sandbox(StartSandboxRequest {
>                     id: handle.sandbox_id.clone(),
>                     snapshot_id: Some(snapshot_id),
> --- `crates/executor/src/native/harness_tool.rs`

No supplied object counterpart. This is not the native conversation snapshot in [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge) and does not rewind agent artifacts, event history or provider model state in the inspected handler. Its route is [MEM-RTE-sandbox-rewind](#mem-rte-sandbox-rewind).

### Routes

#### MEM-RTE-fact-revision
Label: Fact revision

Model/tool caller → `remember` or `forget` → validated read-modify-write of agent memory → instruction assembly → later model request. Owner: handler for structural changes; foreground model for proposed fact and stale-item selection. This is a distinct content-maintenance route feeding [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop), not a replacement for its execution loop. SRC-1: `exo/tools/memory-tools.ts`, `exo/harness.ts`, `exo/profiles/practical.ts`.

- Immediate return: added ID, total and dropped count, or removal count / validation error.
- Later read-back: every Exo instruction assembly selects the latest artifact version by path and injects all saved entries as developer text; across conversations of the same agent.
- Delegated visibility: model sees entry IDs and text, not `createdAt` or structured provenance.
- Selection predicate: current agent handle, exact artifact path, maximum version; no query relevance filter; `forget` matches exact supplied ID.
- Invalidation or expiry: explicit forgetting; addition beyond 200 entries keeps the newest 200; corrupt store blocks writes and produces an unavailable warning on reads.
- Activation or effect: changes future instruction content; actual model reliance and improvement unobserved.
- Evidence limits: no compare-and-swap; concurrent channels can lose updates. Structural validation does not verify fact truth or source trust.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: open task/user or self-fact proposals; trim text, reject empty or over 600 characters; handler checks JSON shape and refuses corrupt prior state. Generic tool permission policy can veto invocation, not certify truth. There is no mandatory per-entry human approval. Authorship and initial deployment contents are unknown. Guidance requests standalone facts and removal of stale entries. No automatic transcript summarizer produces this store: a model may use prior experience when selecting text, but that trace-to-fact transformation is not observed. Reasons need not persist. Old artifact versions are storage, not an implemented restore button in these tools.

> const MAX_ENTRIES = 200;
> const MAX_TEXT_CHARS = 600;
> --- `exo/tools/memory-tools.ts`

> content: `Durable memory you saved earlier with the remember tool. Treat these as authoritative context. Add new facts with remember and drop stale ones with forget(id).\n\n${lines.join("\n")}`,
> --- `exo/tools/memory-tools.ts`

The latter is requested model-interpreted authority. It is not independently warranted knowledge.

#### MEM-RTE-plan-replacement
Label: Plan replacement

Foreground tool proposal → full validated list → conversation artifact → conditional developer-message replay. Owner: model proposes tasks/status; software validates and selects replay. Distinct from the execution queue [RT-OBJ-turn-work](runtime.md#rt-obj-turn-work). SRC-1: `exo/tools/todo-tools.ts`, `exo/harness.ts`.

- Immediate return: total/remaining counts or error.
- Later read-back: latest list reaches later model rounds and turns of this conversation while at least one item is pending/in_progress.
- Delegated visibility: all item content and statuses, including completed/cancelled items when another item remains open.
- Selection predicate: exact conversation artifact path/latest version, then presence of open items; not a topical query.
- Invalidation or expiry: full replacement or empty list; all-closed suppresses injection without deleting retained artifact. Corrupt/unreadable list is treated as empty.
- Activation or effect: plan can guide later work through developer text; verification/compliance unobserved.
- Evidence limits: source description asks for one in-progress item and verified completion; handler does not enforce either as semantic predicates.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: open planning requests; software rejects malformed status/shape, over 50 items, empty text or content over 300 characters. Model/caller can replace any item; per-item human approval is not required by this handler. Generic invocation authorization remains separate. Full-list rewriting can change meaning and reliance, but no compulsory criticism or outcome-based comparison exists. No answer oracle. Prior versions persist physically; no automatic rollback is wired here.

> if (open.length === 0) {
>     return null;
>   }
> --- `exo/tools/todo-tools.ts`

#### MEM-RTE-skill-lifecycle
Label: Skill lifecycle

Submitted skill/files → frontmatter/path/size checks → payload version → index publication → automatic catalog → foreground `use_skill` and optional file reads. Owner: model/caller proposes; handler admits structure; model chooses applicability and subsequent procedure use. This adds textual instructions, distinct from [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission). SRC-1: `exoharness/typescript/harness/skill-tools.ts`, `exo/harness.ts`, `exo/profiles/practical.ts`.

- Immediate return: install/update metadata, listing, requested body/file, uninstall count, or error.
- Later read-back: latest agent-wide catalog is pushed at instruction assembly; requested skill body and file contents reach later model invocations through tool results.
- Delegated visibility: push gives name/description only; `use_skill` gives full SKILL.md and bundled path names; `read_skill_file` gives exact selected file content, each before result offload/truncation.
- Selection predicate: agent + latest exact-path artifact; foreground name selection and, for files, exact path. `use_skill` requires catalog membership; `read_skill_file` reads payload directly without that membership check.
- Invalidation or expiry: same-name install writes new payload/index metadata; uninstall removes index entry only. Old payload survives and direct file reads can still succeed by known name/path.
- Activation or effect: procedure is delivered as tool output with an instruction to follow it; executable file text is not automatically run. Actual reliance unobserved.
- Evidence limits: index and payload are separate writes; no compare-and-swap. Catalog withdrawal is not full revocation and does not erase earlier conversation copies.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: open requests, not a controlled improvement curriculum. Structural gate rejects invalid/reserved names, missing/oversized descriptions, malformed frontmatter, unsafe relative file paths, duplicates and size/count violations. Limits: 100,000 characters SKILL.md, 200,000 per file, 64 files, 1,024-character description; no aggregate catalog count cap in this handler. Generic invocation policy can veto; no mandatory human content approval, origin authentication or semantic correctness oracle. User-provided, externally fetched and model-authored content are possible; deployed lineage unknown. Guidance requests reuse for matching tasks, not source verification. Supporting text may retain explanations but no required criticism/revision rationale is stored. Corrupt index blocks install/uninstall and causes a prompt warning; unreadable body can be reinstalled. Reinstallation is repair, not automatic rollback.

> await handle.writeArtifactJson({
>           path: skillArtifactPath(name),
>           value: record as unknown as JsonValue,
>         });
> --- `exoharness/typescript/harness/skill-tools.ts`

> const record = await readSkill(skillsHandle(execution.context), name);
> --- `exoharness/typescript/harness/skill-tools.ts`

The second passage is the direct file-read branch, unlike the catalog check in `use_skill`; this is the counterexample to complete withdrawal.

#### MEM-RTE-result-offload
Label: Result offload

Part of: [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop)

Registered tool output → code-rule artifact write and preview → normalized result journal → later model history. Owner: registry normalization, not a summarizing model. SRC-1: `exoharness/typescript/harness/tools.ts`; closest supplied account is the parent route's large-result paragraph.

- Immediate return: normalized tool result containing success, source/name/call ID, artifact metadata, preview, truncation flag and optional full inline value.
- Later read-back: normalized results enter later materialized conversation history; full result bytes remain in turn artifacts for explicit readers.
- Delegated visibility: value retained inline only at or below 8,000 serialized characters; preview capped at 4,000 characters. Full JSON always offloaded; nonempty stdout/stderr additionally get text artifacts.
- Selection predicate: serialized length, not relevance, truth or importance; preview is string prefix.
- Invalidation or expiry: no expiry implemented by these helpers; later event/turn retention policy uninspected.
- Activation or effect: reduces model-visible large result contents and preserves a pointer; actual follow-up reload unobserved.
- Evidence limits: generic artifact read APIs afford access but this helper does not automatically fetch omitted bytes into a later request. A precise model-facing arbitrary-result reload route was not established in the inspected practical profile.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is an automatic trace-fed transformation: raw output → full raw artifact plus derived normalized envelope → later prompt. It preserves original reasons in the raw bytes if present, but the prefix may omit them. It does not derive new semantic knowledge. The symbolic pointer does not itself make the model window dereferenceable or liveness-managed.

> const fullResultArtifact = await writeToolResultArtifact(
>     context,
>     args,
>     "result.json",
>     `${JSON.stringify(args.result, null, 2)}\n`,
>     "application/json",
>   );
> --- `exoharness/typescript/harness/tools.ts`

#### MEM-RTE-codex-compaction
Label: Codex compaction

Part of: [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge)

Exo materialized prior history → Responses-input replay items → tool-pair-aware chunks → native injection, interleaved native compaction → later native turn. Owner: bridge selects replay/chunks; Codex owns compacted representation. SRC-1: `exoharness/typescript/codex/replay.ts`, `exoharness/typescript/codex/harness.ts`.

- Immediate return: replay completes, or timeout/native compaction error; no readable summary returned by these functions.
- Later read-back: the native thread, after compaction, supplies context to subsequent native turn; alternatively warm reuse/resume can avoid replay. Persistent representation inside native state is opaque.
- Delegated visibility: replay excludes system/developer messages; other messages convert to Responses items. Native compaction receives injected thread state, not all host artifacts.
- Selection predicate: replay only when thread is not reused; chunks default to 256,000 JSON characters, preserving call/output units. A single oversized unit can exceed that budget.
- Invalidation or expiry: resume failure is recorded and can fall back to a new thread/replay. Between replay chunks the bridge requests compaction and waits up to 600,000 ms; native checkpoint retention/expiry uninspected.
- Activation or effect: next injected chunk and subsequent turn consume native state produced after compaction; actual selected content, rationale survival and model behavior are unobserved.
- Evidence limits: no semantic summary payload, retained verbatim tail or alternative checkpoint algorithm is inspectable here. Warm thread/resumed snapshot and replay are different recovery paths, not interchangeable claims of complete context preservation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is a wired trace-fed host transformation, but raw-to-derived lineage is only known up to the opaque native state. It cannot be scored as inspected semantic curation or evidence-responsive learning. The trigger and delivery are automatic bridge decisions, not foreground memory retrieval.

> if (index + 1 < chunks.length) await compactThread(server, threadId);
> --- `exoharness/typescript/codex/replay.ts`

> await server.request("thread/compact/start", { threadId });
> --- `exoharness/typescript/codex/replay.ts`

#### MEM-RTE-sandbox-rewind
Label: Sandbox rewind

Snapshot tool request → backend checkpoint plus symbolic registry → later rewind request → start sandbox at checkpoint → later filesystem consumer. Owner: caller/model selects capture/rewind; handler resolves scope and backend executes. Distinct from conversational recovery [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge). SRC-1: `crates/executor/src/native/harness_tool.rs`.

- Immediate return: scope, sandbox/owner/snapshot IDs and success/rewound flag, or backend error.
- Later read-back: later shell/tool operations use the sandbox started from selected snapshot; registry list operations expose IDs, not file contents.
- Delegated visibility: backend receives snapshot ID; model receives metadata unless it separately reads restored files.
- Selection predicate: requested snapshot ID plus resolved agent/conversation scope and active sandbox; registry listing filters scope, owner and sandbox.
- Invalidation or expiry: rewind updates current registry reference; snapshot garbage collection and backend expiry uninspected.
- Activation or effect: can restore filesystem-dependent behavior; does not restore conversation memory artifacts through this handler.
- Evidence limits: backend snapshot fidelity and successful restore unobserved; registry metadata is not proof of available checkpoint bytes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is an open restoration request under tool authorization, not semantic knowledge approval. Software parses snapshot identity and resolves scope; no answer oracle or per-file quality gate. Caller authorship is unresolved. Guidance in `exo/harness.ts` advertises checkpoints; source-maintenance advice does not establish a validated prior checkpoint. Recovery remains backend-specific. The checkpoint retains state, not an obligatory reason for restoring it.

### Claims

#### MEM-CLM-history-inspection
Label: History inspection

Claimed operation: the practical profile registers read-only `list_adapter_events` and `list_conversation_events` tools for inspecting retained history. The exposed contract accepts adapter ID/type/time/limit and conversation kinds/cursor/direction/limit. Descriptions specify default 50/cap 200 and lifecycle/host kinds by default; requesting `messages` permits model usage/cost investigation. Source layer: registration implementation and description contract, not a re-audit of host-side filtering. SRC-1: `exo/tools/introspection-tools.ts`, `exo/profiles/practical.ts`.

> name: "list_conversation_events",
> --- `exo/tools/introspection-tools.ts`

This is a model-requested read-back affordance over raw telemetry, not automatic analysis, admitted lessons or proof of improvement. It is distinct from the automatic delivery route [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup), though both may expose events from the same history. Actual retrieved records and later adoption remain unobserved.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn)

Memory-specific reading: Basic event history is retained interaction evidence; cache/cursor is access metadata, not a learned summary. The scoped search of SRC-1 `crates/executor/src/basic.rs` found `limit: None` in history fetching and instructions followed by extended event messages. The supplied record supports recovery from committed rounds. This supports accumulation/reconstruction, not a semantic bounded-window algorithm. Full cache invalidation branches were not re-audited; no universal absence of context control is asserted.

#### On [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop)

SRC-1 `exoharness/typescript/harness/index.ts` directly shows prompt construction as current instructions followed by materialized conversation messages. The inspected event conversion repairs unmatched calls with a synthetic failure and recognizes duplicate representations of tool requests rather than blindly concatenating every event. Thus the event journal and provider message list are not identical raw representations. New result-offload details are in [MEM-RTE-result-offload](#mem-rte-result-offload).

> ...instructions,
>     ...(await materializeConversationMessages(conversation)),
> --- `exoharness/typescript/harness/index.ts`

#### On [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions)

Direct SRC-1 `exo/harness.ts` reads shipped identity once at module initialization, while `readLocalPrompt` rereads `EXO_LOCAL_PROMPT_FILE` or `.exo/exo-profile.md` during assembly. Local content is developer text, not a hard permission gate. External edits can change later instruction supply; initial content authorship, editing grants and per-change human control are unknown. The default practical profile registers memory/todo/skill tools, while instruction assembly itself always attempts these readers. No global guarantee that every profile exposes the corresponding write tools follows.

> const contents = readFileSync(path, "utf8").trim();
> --- `exo/harness.ts`

Saved facts and plans have model-interpreted instructional force. Catalog text asks for body retrieval, and skill bodies enter as tool outputs; catalog delivery does not prove skill adoption. The fact store's “authoritative” wording does not authenticate original sources.

#### On [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery)

Supplied source finding, SRC-1 `crates/executor/src/native/rlm.rs`: foreground root chooses question and selected text/variable; the separate no-tool request excludes full foreground history. Only answer preview and optional JS value escape. This is turn-local frame isolation and value return, not evidence of cross-turn restoration. Full transcript remains accessible in foreground JS working state. A variable name is not a model-window pointer with automatic dereferencing or garbage collection.

#### On [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup)

Supplied SRC-1 `crates/executor/src/native/scheduler_runtime.rs` and `crates/executor/src/native/conversation_wakeup.rs` establish raw command result → artifact/pending fire → formatted user-message preview/report instructions → later agent turn. Delivery is a host-selected push, keyed by owner conversation/task/pending state. It is not a relevance search or proof that results become reusable conclusions. Original command output may include heterogeneous external evidence; its source trust is not established by scheduler origin. Task-specific adapter filter and delete semantics remain uninspected here; exact preview budget was not independently checked.

#### On [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry)

The supplied record and [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) establish source/initialization persistence, next-round reread and remove/replace behavior. Executable modules change host loader/handler behavior, whereas model-visible definitions guide selection. Structural validation is curation of capability shape, not verification of semantic correctness. Import-time effects can precede successful installation. Reasons need not be retained with installed source; no automatic reversal of import-time effects follows from failed-install cleanup. SRC-1 `exoharness/typescript/harness/tool-registry.ts`, `exoharness/typescript/harness/tool-modules.ts` as supplied findings.

#### On [RT-OBJ-guardian-update](runtime.md#rt-obj-guardian-update)

The supplied record retains reason/status/outcome separately from executable source. Later inspection through files and attempted conversation event is not the same as later service execution of rebuilt code. A queued/completed label is deployment telemetry, not a correctness verdict. The self-update route's lack of observed evidence-responsive determination or later causal dependence remains intact. SRC-1 `exo/tools/guardian-tools.ts`, `exo/scripts/deferred-rebuild-and-restart` as supplied findings.

## Write side

Fact revision, plan replacement and skill installation have separate structural gates, explicit withdrawal mechanisms and different corruption behavior. Their write agency is foreground tool proposal plus software validation; a user's request to remember or install is not proof of human approval of each resulting byte. Generic authorization can constrain invocation but does not establish truth, trustworthy provenance or semantic evaluation. See [MEM-RTE-fact-revision](#mem-rte-fact-revision), [MEM-RTE-plan-replacement](#mem-rte-plan-replacement), [MEM-RTE-skill-lifecycle](#mem-rte-skill-lifecycle).

Automatic trace processing is narrower: normalized result envelopes preserve raw bytes outside the window; Codex requests opaque compaction between replay chunks; scheduler results become retained artifacts and formatted wakeups. These have known later consumers but no observed improvement. Native warm-state snapshots, resumed thread state and fresh replay are alternative representations; one cannot substitute their retention guarantees for another. See [MEM-RTE-result-offload](#mem-rte-result-offload), [MEM-RTE-codex-compaction](#mem-rte-codex-compaction) and the background annotation.

Cleanup does not necessarily revoke prior content. Memory forgetting changes latest-version injection while history remains versioned. Completed todos disappear from the prompt without deletion. Skill uninstall removes catalog membership but leaves a direct file-read route. Tool registry removal has different executable-store semantics, and cannot undo prior effects. Filesystem rewind restores another state plane rather than undoing agent artifacts or journaled events. These are distinct rejection, withdrawal and recovery boundaries, not one global forgetting operation.

No installed lesson store or automatic semantic extraction is inferred merely from keeping raw telemetry. Dynamic facts and procedures may contain theories, but no specific inspected content-directed criticism/revision cycle is established by their generic APIs. Consequently this report does not assert a theory builder, learning benefit or exercised self-improvement from persistence alone.

## Read-back

The main automatic routes are instruction-time fact push, conditional plan push, catalog push, conversation materialization, host wakeup and native replay/reuse. Their selectors are IDs, paths, statuses and code rules. They do not establish semantic retrieval ranking. Budgets vary: fact/todo per-entry and count limits, skill per-payload limits without a catalog-wide cap, result prefix limits, and Codex chunk heuristics rather than a hard total context bound. Loaded bodies may exceed inline result limits and become previews with artifact references.

Requested routes are `use_skill`, `read_skill_file` and history introspection; foreground model chooses name/path or event filters. The caller selecting a known path is not itself an automatic task-relevance selector. Generic artifact read methods establish storage access, not a deployed model consumer that reliably reloads any omitted result. Backend checkpoint restoration is read-back to executable filesystem consumers rather than necessarily model text. Native summarization and external SDK context internals remain opaque.

The frame analogy applies narrowly to RLM's selected-input/no-tool subqueries: only a return value crosses back. It does not imply heap-style reachability, reference counting or automatic reload of text from any pointer. Offloaded results and skill catalogs supply addresses that require further explicit operations; native compaction supplies an opaque replacement state rather than an inspected live-reference scheme.

## Integration issues

1. Qualification of supplied native account: [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge) describes replay, but [MEM-RTE-codex-compaction](#mem-rte-codex-compaction) establishes bridge-controlled compaction between replay chunks (SRC-1 `exoharness/typescript/codex/replay.ts`). The statement that native compaction internals are uninspected remains true; bridge trigger/wiring is inspectable. Reconciliation should preserve that distinction, not flatten it into wholly unknown compaction.
2. Fact and skill catalog corruption differs from plan corruption. Known transformations must not be generalized into a universal silent-empty or fail-closed policy. The three lifecycle records preserve this distinction.
3. Skill withdrawal is partial: [MEM-RTE-skill-lifecycle](#mem-rte-skill-lifecycle), SRC-1 `exoharness/typescript/harness/skill-tools.ts`, shows `read_skill_file` bypassing index membership. This prevents classifying uninstall as complete behavioral revocation. Earlier conversation copies also remain distinct from current catalog membership.
4. Potential overlap: [MEM-RTE-result-offload](#mem-rte-result-offload) is a declared part of [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop); [MEM-RTE-codex-compaction](#mem-rte-codex-compaction) is a part of [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge). These are not replacement referents. Other new objects have no supplied object counterparts, as compared in their declarations. No other possible duplicate identified after comparison.
5. Unresolved full-result reload: artifact pointer/storage capability is supported, but a general model-facing full-result read route in the practical profile was not established. This prevents claiming universal on-demand recovery of omitted evidence. Concerns [MEM-RTE-result-offload](#mem-rte-result-offload) and [MEM-OBJ-artifact-versions](#mem-obj-artifact-versions).
6. Included opaque/remaining work: native derived payloads and expiry; Claude/Cursor memory policy; host-specific Cloudflare retention; evaluator/UI selection; adapter admission/filter/delete/acknowledgement; backend snapshot fidelity; and external local-profile initialization control remain unresolved at the table's named boundaries. These limit completeness/parity/quality claims, not the established fact, plan, skill, result or replay mechanisms. No unavailable evidence is mislabeled absent.

## Limitations and checks

This is static implementation plus target-authored guidance, not observed operation. Actual content authorship, invocation grants, model compliance, recovery reliability and improvement remain unestablished. There is no new source ID or changed target boundary. Direct `git rev-parse HEAD` matched `423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e`; `git status --short` was empty. Supplied contracts and input members were read completely, including bounded continuation reads. Worker identity was taken from PI environment variables. Target code, tests and examples were not executed. Scope and method remained the supplied memory job and contracts.

Deterministic validation: `commonplace-run validate-output` passed for this invocation after expanding one ambiguous snapshot quotation. No finding was narrowed or withdrawn. A form/quotation pass does not establish analytical correctness or job acceptance.
