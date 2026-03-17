---
description: Source-code review of Napkin, Pi Self-Learning, and OpenViking session mining — compares triggers, consumed session formats, promotion logic, and single-session versus multi-tenant designs
type: note
traits: [has-comparison, has-implementation]
tags: [learning-theory, observability]
status: seedling
---

# Session-mining techniques in related systems

This is a source-code-grounded review of the related systems we have locally that mine CLI or agent sessions into longer-lived knowledge artifacts. I checked the implementation, not just the review notes.

Inspected code paths:

- **Napkin** — `related-systems/napkin/.pi/extensions/distill/index.ts`
- **Pi Self-Learning** — `kb/notes/related-systems/pi-self-learning/extensions/self-learning.ts`
- **OpenViking** — `related-systems/OpenViking/openviking/message/message.py`, `related-systems/OpenViking/openviking/session/session.py`, `related-systems/OpenViking/openviking/session/memory_extractor.py`, `related-systems/OpenViking/openviking/server/routers/sessions.py`

I did not include ClawVault in the concrete comparison below because its repo is not cloned in this workspace, so I could not inspect the extraction path directly.

## The recurring stages

Across the inspected systems, the same stages appear:

1. **Trigger** — when mining runs
2. **Source format** — what raw session representation is consumed
3. **Extraction schema** — what target shape the model or code writes
4. **Promotion/storage** — how extracted items persist or get ranked
5. **Reinjection** — how mined artifacts affect future sessions

What changes from system to system is not the existence of the loop, but how structured the input is and whether the system assumes one active agent session or a multi-session service backend.

## Napkin

Napkin keeps mining outside the core CLI. The actual mining lives in a `pi` extension, not in the `napkin` binary.

**Trigger.** Distillation starts on `session_start` by installing a timer. Every `intervalMinutes`, the extension checks whether the current session file grew since the last run. There is also a manual `/distill` command.

**Source format.** The extension does **not** parse messages itself. It asks `ctx.sessionManager.getSessionFile()` for the current pi session file, checks its byte size, forks it with `SessionManager.forkFrom(...)`, and passes the forked session file to a subprocess. So the consumed log format is "whatever pi stores as a session file"; Napkin treats it as an opaque runtime artifact rather than a schema it owns.

**Extraction technique.** The subprocess is another `pi` invocation with a fixed `DISTILL_PROMPT`. That prompt tells the model to:

- inspect the vault with `napkin overview`
- inspect note formats with `napkin template list` and `napkin template read`
- search before creating
- append to existing notes when possible
- create new notes with templates when needed

So Napkin's extraction is not "transcript -> JSON." It is "forked session -> agent subprocess -> tool-mediated note writes into the vault."

**Promotion/storage.** Promotion is mostly delegated to the vault itself. The extension writes directly into durable notes; it does not maintain a separate scored intermediate store.

**Multi-agent or single-agent?** The extension is effectively **single-session / single-agent**. It keeps one `activeProcess`, one `lastSessionSize`, and one timer loop for the current session. I did not find shared multi-agent coordination or a service API for many agents mining into one store concurrently.

## Pi Self-Learning

Pi Self-Learning is the cleanest example of direct transcript mining into a narrow schema.

**Trigger.** Reflection runs on `agent_end` when enabled. Reinjection runs on `before_agent_start`.

**Source format.** The extension reads the current branch via `ctx.sessionManager.getBranch()`. It filters entries with `type === "message"` and serializes them through `convertToLlm(...)` and `serializeConversation(...)`. It also separately scans recent branch entries for interruption signals, especially `toolResult` errors, permission denials, blocked commands, and aborted assistant turns.

So the consumed log format is not a plain text transcript file. It is pi's **branch event structure**: message entries plus tool-result events from the same session history.

**Extraction technique.** The reflection prompt is deliberately narrow:

- focus only on what went wrong and how it was fixed
- return strict JSON
- schema: `{"mistakes":["..."],"fixes":["..."]}`

Project/global mode changes the prompt scope. Project mode keeps repo-specific detail; global mode rewrites toward cross-project reusable rules.

**Promotion/storage.** The raw reflection appends to daily markdown. Durable promotion happens through a scored index with frequency bonus and recency decay, then renders into `CORE.md` and related memory files.

**Multi-agent or single-agent?** This is also **single-session / single-agent** in the code inspected. It operates on the current pi branch and current runtime hooks. It supports project-vs-global memory scope, but not a shared multi-agent memory service.

## OpenViking

OpenViking is structurally different from Napkin and Pi Self-Learning because it owns the session and message schema itself.

**Trigger.** Mining runs on `session.commit()` or the HTTP `POST /api/v1/sessions/{session_id}/commit` endpoint. The service also supports background commit with task tracking.

**Source format.** OpenViking stores session messages as **structured messages with parts**. A message is `role + parts`, serialized to JSONL. Supported parts include:

- `text`
- `context`
- `tool`

The session API accepts either a simple `content` string or a full `parts` array. Tests show assistant messages can carry multiple text parts, context parts, and tool parts. The extractor formats the archived messages into lines like `[user]: ...` and `[assistant]: ...`, and serializes tool calls into JSON objects embedded as `[ToolCall] ...`.

So unlike Napkin and Pi Self-Learning, OpenViking consumes a **first-class typed session log** rather than borrowing an opaque runtime file or in-memory branch structure.

**Extraction technique.** `Session.commit()` archives the current messages, then calls `extract_long_term_memories(...)`. The extractor sends formatted recent messages to an LLM prompt and expects a parsed payload containing memory candidates. The categories are explicit in code:

- user memory: `profile`, `preferences`, `entities`, `events`
- agent memory: `cases`, `patterns`
- tool/skill memory: `tools`, `skills`

There is also explicit handling for tool-call statistics and skill names, so tool execution data is part of the mined trace, not just the natural-language conversation.

**Promotion/storage.** Extraction writes into typed memory directories and runs deduplication/merge logic. The important point is that OpenViking persists the mined items into a service-managed memory substrate, not directly into human-authored notes.

**Multi-agent or single-agent?** OpenViking is the only inspected system here that is clearly **multi-session and multi-tenant**. The server has multi-tenant auth, session isolation tests, user-space and agent-space directory initialization, and background task tracking keyed by `session_id`. That does not automatically mean sophisticated multi-agent reasoning, but the backend is built as a shared service rather than a single-agent extension.

## What the comparison makes concrete

The systems fall into two technique families.

**Single-session extension pattern.**

- Run inside an existing agent runtime
- Mine the current conversation only
- Reuse the runtime's session representation instead of defining a new one
- Usually write back into markdown artifacts directly

Napkin and Pi Self-Learning fit here, though Napkin is even looser because it treats the session as an opaque file and reuses a subprocess agent to do the actual extraction.

**Service-owned session pattern.**

- Own the message schema
- Accept structured session events over an API
- Separate archive, extraction, and deduplication
- Support concurrent sessions and tenant isolation

OpenViking fits here.

## Log formats matter more than the prompts

The biggest difference is not the wording of the extraction prompt. It is the **shape of the source trace**:

- **Napkin** consumes an opaque pi session file and delegates interpretation to a subprocess agent
- **Pi Self-Learning** consumes pi branch events and explicitly mines both message text and tool-result interruptions
- **OpenViking** consumes its own typed message schema with text/context/tool parts and JSONL serialization

That affects what can be learned. If the log format carries tool calls, statuses, and context references, the system can mine operational patterns that a plain transcript cannot. If the format is opaque, the miner has to trust the upstream runtime to preserve the right details.

## What looks borrowable

- **Explicit boundary triggers.** `agent_end`, `session.commit()`, and periodic distill checks are all concrete extraction clocks.
- **Narrow extraction schemas.** Pi Self-Learning's `mistakes/fixes` pair is the cleanest example; OpenViking's fixed memory categories are the broader version.
- **Tool-result mining.** Pi Self-Learning and OpenViking both mine more than user/assistant prose. They use blocked commands, permission denials, tool inputs, outputs, and statuses as learning material.
- **Separate trigger from promotion.** Extraction is one problem; ranking, deduplication, or durable promotion is another. The systems that keep those separate are easier to reason about.

## What remains open

None of the inspected systems closes the harder KB-learning mutations. They extract and persist candidates well, but that is still different from:

- deciding whether two notes should be linked
- synthesizing a better abstraction from several sessions
- retiring a stale learning for principled reasons
- judging whether a mined pattern has explanatory reach or is just a recurring local patch

The concrete update to [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) is narrower: **session-derived candidate generation is now a solved enough pattern to copy; oracle-backed evaluation is not.**

---

Relevant Notes:

- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — sharpens: source-inspected systems now give concrete extraction and promotion loops for workshop artifacts; the remaining bottleneck is still evaluation of higher-order mutations
- [a functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — grounds: all three systems operationalize workshop-to-library bridges from session traces
- [Napkin](./related-systems/napkin.md) — source-inspected instance: forked-session distill via a subprocess agent and vault templates
- [Pi Self-Learning](./related-systems/pi-self-learning.md) — source-inspected instance: branch-event mining into strict `mistakes`/`fixes` JSON plus scored promotion
- [OpenViking](./related-systems/openviking.md) — source-inspected instance: typed session messages, commit-triggered extraction, and multi-tenant user/agent memory spaces
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: these systems learn or curate policy only as far as their available promotion oracle allows
