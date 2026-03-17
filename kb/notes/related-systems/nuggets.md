---
description: Pi-coupled personal memory assistant with local HRR nugget files and chat-channel scheduling - strongest reference for file-backed scratch memory, though its promotion loop is only partially wired
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-17
---

# Nuggets

Nuggets is a TypeScript personal-assistant stack built around two layers: a tiny local memory library (`src/nuggets/`) and a Pi-powered chat gateway (`src/gateway/` plus `.pi/extensions/`). It stores facts as JSON files under `~/.nuggets/`, rebuilds HRR vectors on demand for recall, injects selected facts into Pi's system prompt, and can message the user through Telegram or WhatsApp. The repo's strongest idea is not "AI memory" in the abstract but a practical bridge between ephemeral chat interaction, lightweight local persistence, and host-specific memory files.

**Repository:** https://github.com/NeoVertex1/nuggets

## Core Ideas

**Keyed HRR storage keeps the runtime substrate tiny.** `Nugget` stores only raw facts plus hyperparameters in `{name}.nugget.json`; vectors are rebuilt deterministically from the nugget name via a seeded PRNG in `src/nuggets/memory.ts` and `src/nuggets/core.ts`. Recall is cheap because the system never reaches for a vector database or embedding API. The important constraint is that recall is still key-driven: it first resolves the query against stored keys, then decodes one of the stored values.

**The Pi extension is the real product surface.** The system becomes useful through `.pi/extensions/nuggets.ts`, not through the HRR library alone. That extension registers a `nuggets` tool, injects remembered facts into `before_agent_start`, auto-captures file paths from tool results, extracts preferences from user input, and snapshots volatile task state before session compaction. In practice this is what turns the library into "persistent memory."

**Promotion is a bridge into host memory files rather than a separate knowledge layer.** `src/nuggets/promote.ts` scans facts with `hits >= 3` and writes them into a project-scoped `MEMORY.md` under `~/.claude/projects/.../memory/`. That is a useful interoperability move: repeated facts can escape the nugget store and become part of the host agent's default context. The mechanism is pragmatic, but it is promotion by thresholded reuse, not synthesis.

**The gateway wraps long-lived Pi sessions in chat-native orchestration.** `src/gateway/` provides a per-user Pi process pool, serialized message queues, JSONL RPC over stdin/stdout, heartbeat prompts, and a file-backed cron scheduler. This is the part of Nuggets that feels most product-shaped: memory is not just stored, it is surfaced through the same channel where the user already talks to the agent.

**The proactive layer is implemented as filesystem operations, not a service backend.** Scheduled jobs live in `.gateway/cron/jobs.json`; the Pi extension appends requests to `.gateway/cron/requests.jsonl`; heartbeat state is kept in memory and event delivery goes through a local queue. This keeps the system inspectable and easy to debug, at the cost of weaker coordination guarantees than a real broker or database would provide.

## Comparison with Our System

| Dimension | Nuggets | Commonplace |
|---|---|---|
| Primary concern | Runtime personal memory for a chat assistant | Curated knowledge for agent navigation and reasoning |
| Storage | JSON fact files in `~/.nuggets/`, plus gateway JSON files | Markdown notes in git |
| Knowledge unit | Key-value fact with optional recall count | Note with prose, frontmatter, and explicit links |
| Retrieval | Fuzzy key match, then HRR decode among stored values | Search + descriptions + indexes + semantic links |
| Learning model | Accumulate facts, optionally promote repeated ones to `MEMORY.md` | Human/agent curation, connection, maturation, validation |
| Integration surface | Pi extension + Telegram/WhatsApp gateway | CLAUDE.md, instructions, skills, direct file editing |
| Proactivity | Heartbeats, cron jobs, reminders in the same chat channel | External operations triggered by users, skills, or maintenance workflows |
| Validation | Unit tests for the memory math and core operations; little semantic governance | `/validate`, semantic review, type templates, link semantics |

**Where Nuggets is stronger.** It solves a real runtime problem we mostly ignore: how to keep cheap, low-stakes personal facts available across sessions without turning the whole KB into a scratchpad. The per-user process pool and same-channel reminder path also make the assistant feel continuous in a way a library-style KB does not.

**Where commonplace is stronger.** Knowledge has explicit structure, scope, and maturation. A Nuggets fact is an untyped assertion with no evidence, no relationship semantics, and no path from "raw capture" to "developed argument." Our system also makes retrieval legible to the agent through descriptions and curated indexes rather than burying everything behind one memory tool.

**The deepest difference** is what counts as improvement. Nuggets treats repeated recall as the proxy for importance. Commonplace treats improved explanation, connection quality, and composability as the proxy. Nuggets optimizes for convenience and continuity; commonplace optimizes for reasoning quality.

## Borrowable Ideas

**A tiny scratch-memory layer for low-value facts.** Nuggets cleanly separates "remember this command/path/preference" from the main knowledge system. For commonplace, that suggests a small workshop-adjacent scratch layer for volatile operational facts that are too useful to lose but too weak to deserve a note. *Needs a use case first.*

**Compaction hooks that preserve volatile context before it disappears.** The Pi extension stores a short task summary and recent file activity before session compaction. That pattern would transfer well to a workshop layer: capture active task state before summarization erases it, then decide later whether anything deserves promotion. *Ready to borrow.*

**Promotion into the host agent's native memory file.** Writing repeated facts into `MEMORY.md` is a practical interoperability move. For commonplace, a similar bridge could promote stable workshop learnings into whichever host memory file the runtime already loads. The idea is good; the trigger needs a stronger oracle than raw recall count. *Interesting pattern, but not ready as-is.*

**Chat-channel maintenance triggers.** Nuggets uses heartbeat and cron to run follow-up behavior through the same interface the user already inhabits. For commonplace, the analogous move would be externally triggered maintenance passes that arrive as explicit tasks rather than hidden background mutation. *Needs a use case first.*

## Curiosity Pass

**"Holographic memory" names the representation more than the retrieval behavior.** The repo frames recall as algebraic memory, and the HRR implementation is real. But the retrieval path first resolves the user's query against stored keys using exact, substring, and SequenceMatcher-style matching, then decodes among known values. That means the system is closer to a compact keyed associative store than to open-ended semantic memory.

**The self-improving loop is only partially wired.** Promotion depends on `hits`, and `hits` only increment when `recall()` receives a `sessionId`. The tests exercise this path, but the Pi extension calls `shelfRecall(query)` without a session ID, so normal memory lookups do not advance promotion counters. The repo has the mechanism pieces, but the main product path does not fully connect them.

**Topic-scoped nuggets mostly collapse into one default memory bucket.** The library supports multiple nuggets and the README presents topic-scoped memories as a major idea. In the actual Pi extension, most operations read and write the single `"memory"` nugget. The multi-nugget substrate exists, but the user-facing path barely exploits it.

**The proactive architecture is more single-user than the gateway framing suggests.** The scheduler request bridge writes `add/remove/list` requests without a JID, and the cron layer falls back to `defaultJid`. That works cleanly in single-user deployments, but it is a ceiling on the otherwise per-user gateway design.

**The best part of Nuggets is not the math; it is the inspectable ergonomic packaging.** Files instead of infrastructure, prompt injection instead of a separate retrieval server, and reminders delivered in the same chat where the user already talks to the agent are all strong design choices. Even if the HRR layer were replaced with a simpler keyed store, much of the product value would remain.

## What to Watch

- Whether recall-session wiring is fixed so promotion actually reflects real usage rather than test-only behavior.
- Whether the system grows a genuine multi-nugget strategy instead of routing almost everything through one `"memory"` shelf.
- Whether proactive scheduling becomes properly per-user; that would make the gateway architecture more than a single-user assistant shell.
- Whether Nuggets stays Pi-coupled or becomes a runtime-agnostic memory layer with multiple agent frontends.

---

Relevant Notes:

- [Pi Self-Learning](./pi-self-learning.md) - contrasts: both are Pi extensions that inject memory across sessions, but Nuggets optimizes for persistent personal facts and reminders rather than mistake extraction
- [files-not-database](../files-not-database.md) - exemplifies: Nuggets keeps both memory and scheduling state in readable local files instead of introducing operational databases
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: Nuggets tries to keep always-loaded context small by storing most facts externally and injecting only selected items
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - extends: the nugget store plus promotion bridge is a concrete ephemeral-to-durable pattern, even though the durable target is a host memory file rather than a curated note
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) - exemplifies: Nuggets picks an easy-looking oracle for learning (recall frequency), but the gap between having the metric and wiring it into real improvement remains
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](../periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) - parallels: Nuggets' heartbeat and cron features show the value of externally triggered follow-up work rather than hiding maintenance inside every routing decision
