---
description: "Nuggets review: TypeScript HRR fact memory, Pi prompt injection, trace capture, hit-count promotion to MEMORY.md, and Telegram/WhatsApp gateway"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Nuggets

Nuggets, by NeoVertex1, is a TypeScript project for a Pi-powered personal assistant with local holographic fact memory and a Telegram/WhatsApp gateway. At the reviewed commit the inspectable implementation is the original TypeScript app: topic/kind-scoped facts persist as JSON under `~/.nuggets`, Pi can call a `nuggets` tool to remember/recall/forget/list facts, selected traces are automatically written into memory, and high-recall facts can be promoted into Claude Code's `MEMORY.md`. The README advertises a newer `nuggets-memory-plugin` package and `nuggets-memory/` workspace, but that workspace is not present in the checked-out tree and the root package is still `nuggets` without a plugin binary ([README.md](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/README.md), [package.json](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/package.json), [root tree](https://github.com/NeoVertex1/nuggets/tree/714cab8a3b1fb843aa98dfb51584d2c07a6739f3)).

**Repository:** https://github.com/NeoVertex1/nuggets

**Reviewed commit:** [714cab8a3b1fb843aa98dfb51584d2c07a6739f3](https://github.com/NeoVertex1/nuggets/commit/714cab8a3b1fb843aa98dfb51584d2c07a6739f3)

**Last checked:** 2026-06-04

## Core Ideas

**The central memory is a tiny associative fact cache, not a document store.** `Nugget` stores short key/value facts with hit counters in JSON files such as `user.nugget.json`; the HRR vector itself is rebuilt deterministically from the facts and a seed derived from the nugget name, so the persisted artifact remains compact ([src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts)). The local instruction file frames it as "L1 cache for your agent" and warns against large documents, exact text retrieval, joins, and more than a few hundred facts per nugget ([NUGGETS_INSTRUCTIONS.md](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/NUGGETS_INSTRUCTIONS.md)).

**Recall is algebraic after symbolic key resolution.** A query first resolves to a stored key by exact match, substring match, token-overlap match, or a SequenceMatcher-like fuzzy score; only then does the implementation unbind the HRR memory and decode the stored value by softmax over vocabulary similarities ([src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts)). That makes the system fast and local, but also means semantic recall is limited by key wording and short value vocabulary rather than a full-text or embedding retriever.

**Memory is split into kind-scoped nuggets.** `NuggetShelf` loads all `.nugget.json` files, broadcasts recall across them, and provides ordered recall across `user`, `project`, and `agent` kinds; `inferMemoryKind()` routes preferences, file paths, commands, repository context, and agent self-knowledge by simple key/value heuristics ([src/nuggets/shelf.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/shelf.ts), [src/nuggets/kinds.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/kinds.ts)). This is a practical scoping layer, not a typed KB contract.

**The Pi extension is the real agent integration.** `.pi/extensions/nuggets.ts` registers the `nuggets` tool, reconstructs session-local facts from tool results, hydrates facts from the shelf on session start, appends all current facts to the system prompt before agent turns, auto-captures file paths from tool results, extracts simple preference phrases from user input, stores compacted task summaries, and runs promotion after compaction ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)). The gateway also starts Pi with an appended prompt telling it to use memory often, but that instruction is host scaffolding rather than retained memory content ([src/gateway/pi-rpc.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/pi-rpc.ts)).

**Context efficiency comes from small payloads and coarse prompt formatting.** Values are expected to be one-sentence facts, active file facts are capped to the last ten in the prompt formatter, and key/kind organization keeps lookup cheap ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts), [NUGGETS_INSTRUCTIONS.md](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/NUGGETS_INSTRUCTIONS.md)). There is no top-k budget for pushed non-file facts: preferences, learnings, and other facts are all formatted into the prompt when present, so context complexity is controlled mostly by social convention and small intended store size.

**Promotion bridges volatile prompt nudges into Claude memory.** `Nugget.recall()` can increment a fact's hit count once per session, and `promoteFacts()` copies facts with at least three hits into `~/.claude/projects/<cwd>/memory/MEMORY.md` if that Claude project memory directory exists ([src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts), [src/nuggets/promote.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/promote.ts)). That gives repeated recall stronger future authority, but only in Claude Code environments matching the directory convention.

## Artifact analysis

- **Storage substrate:** `files` — The main retained memory persists as JSON fact files under `~/.nuggets`; promoted facts persist as `MEMORY.md` under Claude Code's project memory directory; gateway schedules persist separately under `.gateway/cron`.
- **Representational form:** `prose` `symbolic` — Fact values and promoted memory entries are prose, while keys, kinds, hit counts, session ids, HRR configuration, JSON envelopes, tool schemas, schedule requests, and prompt sectioning are symbolic. The HRR vector is behavior-shaping at runtime but is not persisted as a durable parametric artifact; it is regenerated from the symbolic/prose fact list.
- **Lineage:** `authored` `trace-extracted` — Facts can be manually authored through the tool or CLI-style instructions; the Pi extension also extracts file paths from tool results, preference-like phrases from user input, compacted task summaries from session history, and recall-hit signals from use.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — Recalled or injected facts advise the agent as knowledge; tool prompt snippets, gateway prompt text, and promoted `MEMORY.md` entries can instruct future behavior; recall confidence chooses among nuggets and decoded values; hit counts and trace captures feed later promotion and prompt memory.

**Nugget fact files.** Storage substrate: `~/.nuggets/<name>.nugget.json`, written atomically by `Nugget.save()`. Representational form: JSON metadata plus prose key/value facts, hit counts, and last-hit session ids. Lineage: authored by user/agent tool calls or trace-extracted by Pi extension hooks; vectors are derived views rebuilt from the fact list. Behavioral authority: knowledge when recalled, and prompt context when the extension injects the fact list.

**HRR runtime memory.** Storage substrate: in-memory `ComplexVector` banks rebuilt inside `Nugget._rebuild()`. Representational form: runtime numeric vectors derived from stored facts, not durable model weights. Lineage: compiled from JSON facts, nugget name seed, vocabulary keys, role keys, and configuration. Behavioral authority: ranking/selection inside recall, because the decoded value and confidence determine what the tool returns.

**Pi extension state and prompt injection.** Storage substrate: in-memory `facts` map during a Pi session, hydrated from shelf files and reconstructed from prior `nuggets` tool results. Representational form: prose facts formatted into symbolic prompt sections for preferences, learnings, active files, and other facts. Lineage: trace-extracted from session history plus imported shelf state. Behavioral authority: push read-back as advisory context and sometimes instruction-like preference guidance.

**Promoted `MEMORY.md`.** Storage substrate: Claude Code project memory files under `~/.claude/projects/<cwd>/memory/MEMORY.md` when the project memory directory exists. Representational form: Markdown prose grouped by nugget section. Lineage: derived from stored facts whose hit count reaches the threshold; invalidation is weak because promotion merges into `MEMORY.md` and does not remove or supersede source facts. Behavioral authority: stronger system-definition-like instruction/context in future Claude Code sessions.

**Gateway and schedule artifacts.** Storage substrate: gateway sessions, cron request/job files, and per-user Pi subprocess state. Representational form: JSONL/JSON requests and prompt strings. Lineage: authored by user messages, heartbeat timers, and the `schedule` tool. Behavioral authority: routing and orchestration for proactive messages, but not the core Nuggets memory substrate.

Promotion path: a fact can move from a manual or trace-extracted shelf entry, to prompt-injected memory, to hit-counted repeated recall, to `MEMORY.md` promotion. That is a real authority ladder, but it is frequency-based rather than semantically reviewed.

## Comparison with Our System

| Dimension | Nuggets | Commonplace |
|---|---|---|
| Primary purpose | Fast local fact cache and personal-assistant memory for Pi | Git-native methodology KB for agent-operated knowledge-base design |
| Canonical artifact | Short key/value fact in `.nugget.json` | Typed Markdown artifact governed by collection/type contracts |
| Storage substrate | User-local files plus optional Claude `MEMORY.md` | Repository files plus generated indexes and review artifacts |
| Write path | Tool calls, auto-captured traces, preference extraction, compaction summaries | Authored notes/reviews, source snapshots, validation, semantic review |
| Read-back | Tool recall plus always-load prompt injection of stored facts | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Unit tests, capacity conventions, simple kind heuristics, hit threshold | Type validation, collection contracts, source citations, semantic gates |

Nuggets is almost the opposite of Commonplace on artifact ambition. It intentionally keeps each memory small, local, and cheap to recall. Commonplace keeps larger typed artifacts whose value depends on source grounding, links, validation, and review history. Nuggets is stronger as a low-latency nudge layer; Commonplace is stronger as an inspectable knowledge substrate where a claim's source, type, and maintenance path matter.

The useful comparison is the promotion ladder. Nuggets turns repeated pull use into stronger future context by copying high-hit facts into `MEMORY.md`. Commonplace usually promotes by human/agent review, collection routing, and validation, not by frequency. A frequency signal could help prioritize Commonplace review candidates, but should not by itself grant authority.

### Borrowable Ideas

**A tiny fact-cache layer next to the KB.** Needs a concrete use case. Commonplace could use a scratch memory for ephemeral commands, locations, and active-work hints, but it should stay outside library notes and expire or promote through review.

**Hit-counts as review-priority signals.** Ready as a design principle, not an authority rule. Repeated lookup can indicate usefulness and route a candidate toward review; it should not make the fact more trusted without source grounding.

**Keep runtime vectors as derived artifacts.** Ready now. Nuggets persists the inspectable fact list and rebuilds HRR state deterministically; Commonplace retrieval indexes should preserve the same source-of-truth discipline.

**Prompt sectioning by memory kind.** Useful for small pushed context. Formatting preferences, learnings, active files, and other facts into separate sections is a simple way to make coarse recall more readable.

**Do not borrow broad always-load for durable KB content.** Nuggets can push all facts because it is designed for tiny values. Commonplace artifacts are too large and semantically dense; read-back should stay selected or explicitly scoped.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents can write facts through the `nuggets` tool or CLI-style workflows; automatic writes include preference extraction from user input, file-path capture from tool results, compacted task summaries before session compaction, per-session recall-hit updates, capacity eviction when `maxFacts` is configured, and promotion to `MEMORY.md`.

**Curation operations:** `promote` `decay` — Hit-counted facts are promoted into Claude `MEMORY.md` after the recall threshold, and configured `maxFacts` capacity evicts the oldest facts when a nugget exceeds its limit. Other automatic writes are acquisition from traces rather than curation of existing stored memory.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — The extension reconstructs state from session branch tool results, captures file paths from tool-result events, extracts preference phrases from user input events, stores recent user/task summaries before compaction, and updates recall hits from recall events.

**Learning scope:** `per-project` `cross-task` — The shelf under `~/.nuggets` is user-local and cross-session; project facts and promoted `MEMORY.md` entries can shape later tasks in the same project context.

**Learning timing:** `online` `staged` — Tool-result capture, preference extraction, remembers, recalls, and hit-count updates happen during normal sessions; compaction summaries and `MEMORY.md` promotion happen at compaction boundaries.

**Distilled form:** `prose` `symbolic` — Trace material becomes short prose facts with symbolic keys/kinds/hit metadata, and frequently recalled facts become Markdown memory entries.

**Trace source.** Nuggets qualifies as trace-derived because it writes durable retained artifacts from agent/user traces, not only from explicit memory commands. `tool_result` events store read/edit/write file paths, `input` events store simple preferences, `session_before_compact` stores a short `_task` summary and recent tool file paths, and `session_compact` runs promotion ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)).

**Extraction.** The extraction oracle is mostly rule-based: regexes for preferences, event field names for file paths, the last few user messages for task summaries, and a numeric hit threshold for promotion. Meaning-level judgment is limited; there is no LLM judge deciding whether a captured fact is true or should be retained.

**Scope and timing.** Most learning is online and local to the user's machine. Promotion is staged around compaction and depends on Claude Code project-memory path detection, so a high-hit fact may remain only a Nuggets fact outside that environment.

**Survey fit.** Nuggets is a trace-to-fact-cache system with frequency-based promotion. It strengthens the survey distinction between raw trace capture and stronger system-definition authority: file paths and preferences are easy to capture automatically, but moving them into durable prompt memory needs governance beyond a hit counter if correctness matters.

## Read-back

**Read-back:** `both` — Agents can deliberately pull memory through the `nuggets` recall/list tool, while the Pi extension also pushes stored facts into the system prompt before agent turns.

**Read-back signal:** `coarse` — The pushed memory path always formats the current fact map by category; it does not select facts for the current task by identifier, lexical match, embedding similarity, or LLM judgment. Instance-specific lookup remains pull through recall.

**Faithfulness tested:** `no` — The test suite checks HRR math, remember/recall/forget behavior, persistence, hit counting, fuzzy matching, and false-positive avoidance, but I did not find an ablation or behavioral test proving that pushed facts or promoted memories change agent decisions ([tests/memory.test.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/tests/memory.test.ts), [tests/core.test.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/tests/core.test.ts)).

**Targeting and signal.** Pull recall is query-driven and can search a named nugget or the ordered `user`, `project`, `agent` kinds. Push recall is coarse: `before_agent_start` builds prompt sections from all current facts, with only active files sliced to the last ten. There is no implemented pre-prompt top-k memory retrieval over the current user message.

**Injection point.** The extension appends memory before the Pi agent turn. Gateway prompt text is also appended at Pi process startup, but that is a static instruction to use memory rather than read-back of retained memory content. Heartbeats are proactive triggers that tell Pi to check memory; the memory still reaches the model through the prompt-injected facts or an explicit recall call ([src/gateway/heartbeat.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/heartbeat.ts), [src/gateway/router.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/router.ts)).

**Selection, scope, and complexity.** Pull selection is simple and cheap: exact/substr/token/fuzzy key resolution, then HRR decode, with shelf-level best-confidence selection. Push selection has weak complexity control because most facts are included if present; this is acceptable only while the cache remains small. Actual prompt dilution and obedience are not proven from code.

**Authority at consumption.** Tool recall returns advisory knowledge with a confidence and source kind. Prompt-injected preferences and learnings can behave like soft instructions if the agent follows them. Promoted `MEMORY.md` entries have stronger host-level memory authority in Claude Code, but Nuggets does not test whether agents obey them.

**Faithfulness.** The repository validates local mechanics, not agent-level memory use. Tests prove that a fact can be recalled, hit counts increment once per session, and unrelated natural-language queries can return not-found; they do not measure whether Pi checks memory before searching or follows injected preferences.

**Other consumers.** Humans can inspect facts through the `/nuggets` Pi command or the underlying JSON files, and chat users consume the gateway's proactive reminders and replies. The system is designed for a chat assistant, so the human-facing Telegram/WhatsApp path is part of the memory loop rather than a side display.

## Curiosity Pass

**The advertised plugin path is ahead of the checked-out source.** The README points to `nuggets-memory-plugin` and `nuggets-memory/`, but the reviewed tree only exposes the original TypeScript app/gateway and Pi extensions. A review should not infer MCP plugin behavior from that README section.

**The "holographic" mechanism is less important than the trace hooks.** HRR makes recall cheap, but the distinctive memory-system behavior comes from when facts are written and when they re-enter the prompt.

**Promotion can launder noisy facts into stronger memory.** Hit frequency is a useful salience signal, but a false or stale fact can become more authoritative if repeatedly recalled. There is no contradiction check, source citation, or review gate before `MEMORY.md` insertion.

**Always-load is viable only because the intended unit is tiny.** Nuggets' prompt injection would be risky for larger notes, source summaries, or code excerpts. Its design depends on short facts and local conventions about what not to store.

**The gateway makes memory proactive without making recall targeted.** Heartbeat and schedule events can initiate a conversation, but they prompt Pi to check memory rather than automatically selecting relevant facts for the event instance.

## What to Watch

- Whether the advertised `nuggets-memory-plugin` source appears in the repository; an MCP implementation with `guide`, `nudges`, and `recall` tools could change both the integration surface and read-back classification.
- Whether prompt injection gains relevance selection over the current user message; that would move pushed memory from coarse always-load to instance-targeted read-back.
- Whether `MEMORY.md` promotion gains source, freshness, contradiction, or user-approval checks; without that, frequency is doing too much governance work.
- Whether hit counts begin to affect recall ranking directly; today they mainly drive promotion, not query-time ranking.
- Whether tests add behavioral with/without memory checks for Pi or Claude Code sessions; that would distinguish context presence from faithful use.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Nuggets both stores facts and pushes them into Pi prompts, while explicit recall remains a pull path.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: JSON facts, HRR runtime vectors, prompt injection, gateway schedules, and promoted `MEMORY.md` entries have different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: recalled facts and prompt-injected nuggets mostly advise as evidence, context, or preference knowledge.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: promoted `MEMORY.md`, tool guidelines, and gateway prompt instructions can shape future behavior with instruction-like force.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Nuggets turns tool results, user inputs, compaction summaries, and recall events into retained memory and promotion signals.
