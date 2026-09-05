---
description: "Exo review: file-backed long-running agent with append-only traces, coarse-pushed memory, progressive skills, and reversible self-modification"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-07-26"
---

# Exo

Exo is an MIT-licensed long-running personal agent and agent-harness framework built by Ankur Goyal and contributors under the exoharness organization. Its central design separates a durable, trusted `exoharness` substrate from a replaceable executor that owns prompt assembly, model calls, tool policy, memory, and compaction. The canonical agent exposes its own prompts, tools, scheduler, and source tree for modification while preserving conversation events, versioned artifacts, secrets, and sandbox records outside the rewound sandbox ([README.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/README.md), [docs/spec.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/docs/spec.md), [LICENSE](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/LICENSE)).

**Source:** https://github.com/exoharness/exo

**Reviewed revision:** [main at baa07f6785547080d99bd2a7d3eab6d76b984e35](https://github.com/exoharness/exo/commit/baa07f6785547080d99bd2a7d3eab6d76b984e35)

## Core Ideas

**A protected substrate keeps policy mutable.** The Rust exoharness owns identity, ordered events, versioned artifacts, bindings, secrets, and sandbox lifecycle; the TypeScript executor decides which retained state becomes context and which tools are available. This boundary is the enabling mechanism for self-modification: Exo can edit prompts, TypeScript tools, and harness policy, rebuild, and restart without placing canonical history inside the layer being changed ([docs/EXOREADME.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/docs/EXOREADME.md), [examples/exo/harness.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/harness.ts)). What remembered material can change therefore ranges from an answer in one conversation to the tools and instructions used in future conversations.

**Canonical history survives experiments.** Every message, tool request/result, lifecycle change, artifact write, and selected host event becomes a UUIDv7-ordered event file. Sandbox rewind restores filesystem state but deliberately leaves this history and agent artifacts intact; conversation fork copies the prefix through a selected event and records the fork. This lets a repaired agent inspect what happened before retrying, although the implementation's append-only property is an API/storage discipline rather than a cryptographic tamper proof ([crates/exoharness/src/basic.rs](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/crates/exoharness/src/basic.rs), [website/docs-src/concepts/time-travel.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/website/docs-src/concepts/time-travel.md)).

**Memory is small, global, and deliberately non-semantic.** `remember(text)` appends a short agent-scoped fact to a versioned JSON artifact; `forget(id)` removes it from the current version. Prompt assembly injects every retained fact as a developer message in every model round and labels it authoritative context. There are no embeddings, relevance scores, links, provenance fields beyond id/time, or per-entry review state. Entries are capped at 600 characters and the store at 200 entries; overflow drops the oldest facts ([examples/exo/memory-tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/memory-tools.ts)).

**Skills use progressive disclosure; tools cross into execution.** Installed agentskills-format packages are stored as versioned agent artifacts. Every round receives all skill names and descriptions; `use_skill(name)` returns one `SKILL.md`, and `read_skill_file` opens one bundled text file. Separately, `install_agent_tool` writes and loads a TypeScript module that becomes callable in the next model round. These are two promotion targets for reusable understanding: natural-language instruction and executable capability ([typescript/harness/skill-tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/skill-tools.ts), [typescript/harness/built-in-tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/built-in-tools.ts)). Installation validates shape and loadability, not whether the procedure or behavior is correct.

**Context efficiency is uneven by retained surface.** Large individual tool results are preserved as artifacts while only an 8,000-character-or-smaller value and a 4,000-character preview stay inline. Skills disclose bodies and supporting files on demand. Memory and todos have hard count/length caps. But the canonical Exo turn loop materializes all message, tool-request, and tool-result events in ascending order on every model round, with no history window, token budget, retrieval, or implemented compaction; the cumulative count and complexity of prior exchanges are unbounded ([typescript/harness/tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/tools.ts), [typescript/harness/index.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/index.ts)).

> return [
>   ...instructions,
>   ...(await materializeConversationMessages(conversation)),
> ];
> --- [typescript/harness/index.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/index.ts)

**Adoption is local and inspectable, with two histories.** Default state lives as JSON and binary files under git-ignored `.exo`; prompts and harness code live in the git repository; both survive service restart. Memory, skills, tasks, and events can be inspected through structured tools or the files, and no hosted memory API is required. Artifact versions and git history support rollback, but local operational state is not itself committed, and concurrent read-modify-write updates to global memory and the skills index can lose an update ([examples/exo/docs/SELF-CONTROL.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/docs/SELF-CONTROL.md), [docs/design/skills-arch.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/docs/design/skills-arch.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — Default operational state is a filesystem object store under `.exo`: one JSON file per event, version metadata plus binary contents for artifacts, and JSON task/run records. Checked-in prompts, tools, tests, and harness policy persist in the git repository ([crates/exoharness/src/basic.rs](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/crates/exoharness/src/basic.rs), [crates/executor/src/scheduler_store.rs](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/crates/executor/src/scheduler_store.rs)).
- **Representational form:** `natural-language` `symbolic` — Messages, remembered facts, profiles, and skill bodies are natural-language; event envelopes, artifact metadata, task/todo state, skill indexes, tool schemas, TypeScript modules, and harness code are symbolic. A skill bundle deliberately combines natural-language instructions with symbolic frontmatter and may include scripts.
- **Lineage:** `authored` `imported` `trace-extracted` `other-compiled` — Humans and the model directly author memory, todos, skills, tasks, profiles, prompts, and tools. Published skills may be imported without changing their `SKILL.md` content, though Exo serializes the package into JSON artifacts. Conversation events and tool-result artifacts are automatically retained from live interaction traces. Skill catalogs and inline tool-result previews are compiled access/context views over retained skill records and full results; a skill install/uninstall or new tool result invalidates the corresponding view.
- **Behavioral authority:** `knowledge` `instruction` `routing` `enforcement` — Event history and remembered facts return as knowledge context. Profiles and skill bodies instruct; skill descriptions and tool schemas route the model toward procedures and actions; executable tool modules, scheduler records, and harness code enforce behavior by determining what runs. Effective authority, retrieval quality, and whether a loaded fact or skill actually changes behavior are not verified from code.

**Canonical event log and tool-result artifacts.** `files`, `natural-language` `symbolic`, `trace-extracted`, `knowledge`. The log preserves raw messages, tool traffic, errors, usage, and lifecycle events. The default prompt path automatically replays only message/tool traffic, while `list_conversation_events` offers filtered, paginated pull access to lifecycle and host records. Each tool result is also written in full as a versioned turn artifact; its event carries a bounded preview and artifact reference ([examples/exo/introspection-tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/introspection-tools.ts), [typescript/harness/tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/tools.ts)).

**Durable memory and conversation todos.** `files`, `natural-language` `symbolic`, `authored`, `knowledge` `instruction`. Agent-global memory facts are coarse-pushed across conversations as asserted knowledge. Conversation-local todos are replacement-written symbolic status plus natural-language steps and coarse-pushed while any item remains open, instructing continuation of the plan ([examples/exo/memory-tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/memory-tools.ts), [examples/exo/todo-tools.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/todo-tools.ts)).

**Installed skills.** `files`, `natural-language` `symbolic`, `authored` `imported` `other-compiled`, `instruction` `routing`. Content artifacts retain full packages; a separate catalog compiles name/description pointers for every-round routing. The model deliberately pulls a selected body and supporting file. Prior versions survive update and uninstall, but only catalogued current entries are activated.

**Prompts, tools, and harness code.** `repo` `files`, `natural-language` `symbolic`, `authored`, `instruction` `routing` `enforcement`. Git-tracked identity/developer prompts and executor code assemble each model request. A local profile adds uncommitted user-specific instructions. Agent-created TypeScript tools live under `.exo/agent-tools`, are dynamically registered every round, and execute after structural validation; broken modules are skipped so the agent can still boot and repair them ([examples/exo/harness.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/examples/exo/harness.ts), [typescript/harness/tool-modules.ts](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/typescript/harness/tool-modules.ts)).

**Promotion path.** Exo exposes an unusually broad but agent-mediated path: an observation can remain in conversation history, be copied into global memory, be authored as a reusable skill, become executable TypeScript, or motivate edits to the prompts and harness itself. The path crosses from knowledge artifact to system-definition artifact and from natural language to symbolic execution, but Exo records no explicit source relation between stages and supplies no semantic judge, canary, or mandatory review gate. Git commits, artifact versions, tests, builds, snapshots, and restart observation make changes reversible and inspectable; they do not prove improvement.

## Comparison with Our System

| Dimension | Exo | Commonplace |
|---|---|---|
| Primary retained state | Raw conversation events, versioned artifacts, memory facts, skills, tasks, code | Typed Markdown library artifacts plus an operational SQLite review/freshness store |
| Context policy | Full conversation/tool replay; all memory facts and skill descriptions pushed; skill bodies pulled | Scoped lexical search, curated indexes, authored links, and explicit loading |
| Behavioral authority | Same agent can move from facts to skills, executable tools, prompts, and harness code | Knowledge artifacts are separated from system-definition artifacts and promoted through explicit contracts |
| Trust and rollback | Append-only API, artifact versions, git, sandbox snapshots, rebuild/restart | Git history, schemas, deterministic validation, semantic review, freshness baselines |
| Organization | Flat short-fact store, per-conversation trace, named skill catalog | Collections, types, links, descriptions, attribution, and generated navigation |
| Maintenance | Capacity eviction for memory; otherwise model/human-directed | Deterministic validators and explicit maintenance/review workflows |

Both systems keep durable knowledge inspectable in local files, treat code and instructions as retained behavior-shaping state, and use progressive disclosure for skills. Exo is the more operational system: it preserves execution traces and lets the live agent modify its own runtime surfaces. Commonplace is the more governed knowledge system: it carries typed claims, lineage links, collection contracts, validation, and semantic review, but does not make every knowledge writer a live code-deployment authority. Exo's protected-substrate/mutable-policy split gives self-modification a recovery boundary; Commonplace's knowledge/system-definition distinction gives promotion an epistemic boundary.

### Borrowable Ideas

**Fail closed on writes, degrade loudly on reads.** Corrupt Exo memory or skill indexes do not brick prompt assembly, but the write path refuses to overwrite the corrupt artifact and the model receives an explicit unavailable-state message. Commonplace could apply this to optional generated navigation or cached marks while preserving ground truth. Ready now as a failure-policy pattern.

**Keep full tool output as evidence, serve a bounded preview.** Exo writes the complete result to a versioned artifact and retains a compact preview plus reference in the trace. Commonplace's review pipeline could use the same shape for voluminous assay/tool output: preserved evidence without repeatedly loading it. Ready for a concrete review-output case now.

**Default introspection to lifecycle signal, not traffic.** `list_conversation_events` excludes messages and tool traffic unless requested, then offers kind filters, cursors, ordering, and a hard result cap. A comparable Commonplace operator surface could default to review/freshness transitions and require explicit opt-in for verbose execution detail. Ready as a CLI/API design principle.

**Protect history below mutable policy.** Exo keeps canonical events outside the resettable sandbox and executor. For Commonplace, the analogous move would be keeping source snapshots and accepted review evidence outside any experimental agent-authored projection that may be replaced. This needs a concrete self-modifying workflow before adding infrastructure.

## Write side

**Write agency:** `manual` `automatic` — Humans and the model deliberately author facts, todos, skills, tasks, profiles, prompts, and tools through explicit edit/tool interfaces. The runtime automatically captures messages, tool calls/results, artifact-write events, lifecycle events, and scheduled-task runs; it also versions artifacts and updates task lease/run metadata ([crates/exoharness/src/basic.rs](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/crates/exoharness/src/basic.rs), [crates/executor/src/scheduler_store.rs](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/crates/executor/src/scheduler_store.rs)).

**Curation operations:** `decay` — On acquisition of a 201st memory fact, `remember` drops the oldest entry and keeps the newest 200. This is deterministic capacity eviction over already-stored memory. Other automatic writes are acquisition or operational bookkeeping: Exo does not deduplicate, consolidate, enrich, synthesize, invalidate, or promote stored memory automatically. `forget`, skill uninstall, task cancellation, and code edits are deliberate authoring actions, not automatic curation.

Exo does **not** qualify as trace-learning at this revision. It durably retains raw session messages, tool/action traces, and host events and gives the agent tools to inspect them, but no implementation extracts lessons, skills, rules, validators, code, or parametric updates from those traces. Skills, tools, memory, and self-code changes are authored through deliberate model or human actions. The README's autonomous self-maintenance loop is explicitly ongoing work, so the implemented system is a trace-preserving substrate for possible learning, not a trace-learning loop ([README.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/README.md)).

> Exo should periodically inspect its context,
> memories, tools, scheduled tasks, and running processes; identify stale or
> conflicting state; propose or perform safe cleanup; and record what changed.
> --- [README.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/README.md)

## Read-back

**Read-back:** `both` — Push dominates the canonical agent: each model round receives all retained conversation messages/tool traffic, all current global memory facts, every open todo list, and the complete skill name/description catalog without an agent lookup. Pull remains available through `use_skill`, `read_skill_file`, `list_conversation_events`, artifact APIs, and shell/git inspection of prompts and code.

**Read-back signal:** `coarse` — Implemented push is always-load within its scope: all current-conversation history, all agent memory, all installed-skill descriptions, and the current conversation's todo list. No lexical, embedding, or LLM-judged relevance selector targets retained memory for the current instance. Identifier-based skill/event lookup exists only on the pull path.

**Faithfulness tested:** `no` — Unit tests verify that remembered facts, todos, and skill descriptions appear in assembled messages and that full skill bodies can be loaded. The system does not run WITH/WITHOUT ablations, perturb recalled content, or audit whether a pushed fact or selected skill changed the action.

The injection point is prompt assembly immediately before each model call, including every tool-loop round. Memory and catalogs arrive as developer messages; conversation history and prior normalized tool results follow as ordinary replayed messages. At consumption, memory is labelled authoritative context, skills are instructions the standing prompt tells the model to follow, and registered tool definitions constrain available action schemas. Actual obedience and context dilution are not verified from code.

Selection is bounded per item but not globally. Memory is at most 200 entries of 600 characters; todos at most 50 entries of 300 characters; one skill body is capped at 100,000 characters and each supporting text file at 200,000, but bodies are pulled. Tool results preserve full artifacts while replaying at most a compact wrapper and 4,000-character preview per call. Conversation history and the skill catalog have no total token budget or count cap, so a long-lived conversation's volume and interaction complexity grow monotonically. The general spec says an executor *could* compact millions of raw events; the canonical Exo executor does not implement that policy ([docs/spec.md](https://github.com/exoharness/exo/blob/baa07f6785547080d99bd2a7d3eab6d76b984e35/docs/spec.md)).

Other consumers include the human through CLI/ExoChat history and diagnostics, the scheduler through task records, adapters through conversation wakeups, and operators through `.exo`, logs, and git. These consumers share retained state without changing the `both` verdict.

## Curiosity Pass

- **"Recursive self improvement" currently means broad self-modifiability plus recovery primitives, not an automatic improvement algorithm.** Exo supplies access to code, logs, builds, restarts, snapshots, and version history, but no implemented trigger/objective/judge automatically turns traces into accepted changes. The claim is architectural capability; improvement quality remains model- and operator-dependent.
- **The trusted log is append-only, not tamper-evident.** The public API only appends UUIDv7 event files and preserves them across sandbox rewind, but the default filesystem backend has no hash chain, signature, or integrity digest. "Immutable" describes the intended authority boundary and API behavior, not cryptographic immutability.
- **The durable conversation/prompt distinction exists in the substrate but collapses in the canonical executor.** The architecture explicitly allows summaries and compacted views over millions of events; `materializePromptMessages` simply prepends instructions to every message/tool event. Exo has built the escape hatch before implementing the escape.
- **Skill portability is semantic rather than physical.** Exo accepts a standard `SKILL.md` and files, then stores them in JSON artifact records rather than an agentskills directory. Content survives, but ordinary filesystem discovery and direct editor workflows require export or tool access.
- **The strongest promotion has the lightest epistemic gate.** Memory facts have length/schema checks; skills have frontmatter/path checks; agent tools are loaded to validate their module shape. None requires provenance, task-outcome evidence, semantic review, or a canary before gaining instruction or execution authority.
- **Cross-conversation memory has a lost-update race.** `remember` and skill installation both read the latest whole artifact, modify it, and write a new version without compare-and-swap. Two concurrent conversations can each publish a valid successor while one silently omits the other's change; the source records this as a storage-rework TODO.

## What to Watch

- Whether canonical-executor compaction or retrieval lands. A bounded derived view would change Exo from unbounded coarse replay to a materially different context-efficiency and read-back design.
- Whether autonomous self-maintenance gains a concrete trace source, trigger, judge, and durable output. That would change the trace-learning verdict and raise the need for promotion gates.
- Whether the artifact storage rework adds compare-and-swap or append-entry operations for agent-global memory and skill indexes. This determines whether multi-channel use can preserve all concurrent writes.
- Whether a cloned-sandbox canary and comparison step becomes mandatory before adopting self-modifications. That would turn recovery-after-failure into evidence-before-promotion.

Relevant Notes:

- [Exo as an agentic system](../../agentic-systems/reviews/exo.md) - part-of: the whole-system analysis this memory subsystem sits inside, covering the self-modification loop, host control surfaces, and where the acceptance gate stops.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supplies the storage, form, lineage, and authority record used to separate Exo's traces, facts, skills, and executable policy.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - defines why Exo's always-replayed history and memory are push while event/skill tools are pull.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames Exo's bounded entries and progressive skills against its unbounded full-history replay.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - contrasts Exo's useful canonical evidence retention with the canonical executor's decision to load the trace by default.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - explains why Exo's promotion from memory fact to skill, tool, prompt, or harness code changes behavioral authority.
- [The chat-history model trades context efficiency for implementation simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) - describes the tradeoff instantiated by Exo's direct event-to-prompt materialization.
