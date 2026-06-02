---
description: "Pi personal assistant with local HRR nugget files, prompt-time memory injection, chat scheduling, and partial promotion into Claude Code memory"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Nuggets

> Replaced 2026-06-02. See [nuggets](./nuggets.md) for the current review.

Nuggets, by NeoVertex1, is a TypeScript personal assistant stack that combines a local Holographic Reduced Representation key-value memory with a Pi extension and Telegram/WhatsApp gateway. The inspected commit implements a small file-backed memory engine, Pi lifecycle hooks that store and inject facts, a `MEMORY.md` promotion bridge for Claude Code, and proactive chat scheduling. It does not implement the newer README-advertised `nuggets-memory/` MCP plugin workspace at this commit; the review is therefore about the checked-in TypeScript/Pi assistant and gateway.

**Repository:** https://github.com/NeoVertex1/nuggets

**Reviewed commit:** [714cab8a3b1fb843aa98dfb51584d2c07a6739f3](https://github.com/NeoVertex1/nuggets/commit/714cab8a3b1fb843aa98dfb51584d2c07a6739f3)

**Last checked:** 2026-05-16

## Core Ideas

**The durable memory substrate is one JSON file per nugget kind.** A `Nugget` stores facts as `{ key, value, hits, last_hit_session }` records and writes them atomically to `${name}.nugget.json` under `~/.nuggets` by default ([src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts)). The vector memory is not serialized; it is rebuilt deterministically from the facts, nugget name, dimensions, banks, ensembles, and config. The practical source of truth is readable JSON facts, not opaque tensor files.

**HRR recall is keyed lookup with fuzzy key resolution, not general semantic retrieval.** The engine binds role, sentence, and vocabulary keys into superposed complex vectors, then unbinds by the resolved key position and decodes the nearest stored value by cosine-like similarity over reconstructed vocabulary vectors ([src/nuggets/core.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/core.ts), [src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts)). Natural-language convenience comes mostly from exact, substring, token-overlap, and sequence-ratio matching against stored keys before the HRR decode. That makes Nuggets best for small named facts, preferences, paths, commands, and task hints, not paragraph evidence or document search.

**The shelf layer separates user, project, and agent memory kinds.** `NuggetShelf` loads all `*.nugget.json` files, creates missing nuggets on demand, broadcasts recall across nuggets, and provides a priority-ordered `recallByKind` over `user`, `project`, and `agent` ([src/nuggets/shelf.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/shelf.ts)). `inferMemoryKind` classifies preference-like keys as user memory, file/path/repo/test/task keys as project memory, and everything else as agent memory ([src/nuggets/kinds.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/kinds.ts)). This is a simple authority split: facts differ by intended consumer context, but all three kinds share the same storage and review model.

**The Pi extension is the main behavior-shaping surface.** `.pi/extensions/nuggets.ts` registers a `nuggets` tool with `remember`, `recall`, `forget`, and `list`, reconstructs session-local fact state from prior tool results, hydrates it from the shelf on session start, and appends formatted preferences, learnings, active files, and other facts to the system prompt before agent turns ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)). Stored facts are knowledge artifacts while they sit in JSON; the injected prompt block becomes a temporary system-definition artifact because it conditions the next Pi run through an instruction-bearing channel.

**Capture is opportunistic and trace-derived.** The extension stores preferences from user text patterns such as "I prefer", "always use", "never", and "remember that"; captures read/edit/write file paths from tool results; and stores a compact `_task` fact from user messages before session compaction ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)). This is not a full transcript memory. It is a set of small extracted facts derived from chat/session/tool traces and consumed later by recall or prompt injection.

**Promotion to host memory is implemented but narrow.** `promoteFacts` scans shelf facts with at least three cross-session recall hits and writes them into Claude Code's project memory directory as `MEMORY.md`, grouped by nugget name and merged idempotently ([src/nuggets/promote.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/promote.ts)). Hit counting only increments when recall receives a non-empty session ID, while the Pi extension's direct `shelfRecall` calls do not pass one; the tests cover per-session hit deduplication in the core class, but the live extension path appears only partially wired for automatic promotion ([tests/memory.test.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/tests/memory.test.ts), [.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)).

**The gateway turns Pi into a persistent chat assistant.** `src/gateway` starts one Pi RPC subprocess per user, routes Telegram or WhatsApp text into `pi --mode rpc`, serializes messages by chat ID, reuses sessions until idle timeout, and sends assistant output back through the configured channel ([src/gateway/main.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/main.ts), [src/gateway/pi-rpc.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/pi-rpc.ts), [src/gateway/router.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/router.ts)). The gateway also appends a strong chat-persona/system prompt telling Pi to use nuggets often and use the schedule tool for reminders.

**Proactive behavior is file-bridged scheduling plus heartbeat prompts.** The `schedule` Pi extension appends JSONL requests to `.gateway/cron/requests.jsonl`; `CronScheduler` watches that file, persists jobs to `.gateway/cron/jobs.json`, evaluates five-field cron expressions each minute, and pushes events into the same router as incoming messages ([.pi/extensions/proactive.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/proactive.ts), [src/gateway/cron.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/cron.ts), [src/gateway/event-queue.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/event-queue.ts)). `HeartbeatManager` periodically prompts Pi to check memory for follow-ups while respecting quiet hours ([src/gateway/heartbeat.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/heartbeat.ts)).

**Tests cover the memory engine, not the assistant lifecycle.** Vitest tests exercise HRR primitives, save/load, upsert, forgetting, fuzzy matching, token-overlap lookup, max-fact eviction, and hit-count deduplication ([tests/core.test.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/tests/core.test.ts), [tests/memory.test.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/tests/memory.test.ts)). There are no comparable checked-in tests for Pi extension hooks, prompt injection, gateway routing, cron request processing, Telegram/WhatsApp integration, or the `MEMORY.md` promotion path.

## Comparison with Our System

| Dimension | Nuggets | Commonplace |
|---|---|---|
| Primary purpose | Personal Pi chat assistant with tiny durable facts and reminders | Agent-operated methodology KB with typed durable artifacts |
| Storage substrate | `~/.nuggets/*.nugget.json`, `.gateway/cron/*.json*`, Pi session dirs, optional Claude Code `MEMORY.md` | Git-tracked Markdown notes, sources, reviews, instructions, schemas, generated indexes |
| Representational form | Prose key/value facts, symbolic JSON fields and cron specs, HRR/vector reconstruction, injected prompt text | Typed prose, symbolic frontmatter/links/schemas/scripts, generated indexes and validation outputs |
| Lineage | Fact source usually implicit in hook or user phrasing; `_task` and file facts do not retain source message IDs | Source-pinned citations, review metadata, statuses, replacement archives, validation and review records |
| Activation | Pi tool recall, automatic system-prompt injection, heartbeat prompt, chat cron events | Search, indexes, authored links, skills, instructions, validation, review workflows |
| Behavioral authority | Stored facts advise; injected facts and gateway prompts instruct; schedule files route future prompts | Advice, instruction, routing, validation, and review authority split by artifact type |

Nuggets is much smaller and more operational than commonplace. Its design bet is that a personal assistant benefits from a few hundred durable facts that can be stored cheaply, recalled quickly, and injected into the next chat. Commonplace is a library and methodology system: it cares less about sub-millisecond lookup and more about source fidelity, review state, link semantics, lifecycle, and explicit authority.

The strongest overlap is artifact separation. Nuggets has raw chat/session signals, extracted stored facts, HRR reconstruction state, prompt-injected context, gateway prompts, schedule requests, cron job files, and promoted host-memory Markdown. Calling all of these "memory" hides the important differences. Stored nugget facts are knowledge artifacts when Pi uses them as context. The Pi extension's injected memory block, the gateway's appended system prompt, and scheduled prompts are system-definition artifacts because they instruct or route future behavior.

Nuggets is weaker on lineage and governance. It can remember a preference, a path, or a task summary, but the resulting fact does not record which message, tool call, file version, or extraction rule produced it. `MEMORY.md` promotion increases behavioral authority but does not add review, contradiction handling, retirement, or provenance. For a personal assistant this may be acceptable; for a methodological KB it would be too much authority for an unreviewed extracted fact.

**Read-back:** both — Pi can recall nugget facts explicitly, while hooks and the gateway inject remembered facts or scheduled prompts into later turns.

## Borrowable Ideas

**Use tiny file-backed facts as a scratch layer.** Ready to borrow for workshop-local convenience, not for library claims. A commonplace analogue would be a small, inspectable fact cache for active work: file paths, commands, current task labels, and user preferences that help a later agent resume cheaply.

**Separate scratch memory from promoted host memory.** Worth borrowing with stronger gates. Nuggets distinguishes nugget JSON from Claude Code `MEMORY.md`; commonplace should similarly distinguish provisional trace-derived facts from instructions, skills, ADRs, or other stronger surfaces.

**Make activation explicit in the assistant host.** Nuggets is useful because the Pi extension loads facts before agent turns and gives the model a recall tool. Commonplace could benefit from host-specific activation surfaces, but they should respect collection type contracts and authority boundaries.

**Use chat scheduling as a runtime surface, not a KB primitive.** The cron/request bridge is a practical personal-assistant mechanism. In commonplace it would belong in an operational workshop or reminder tool, not in the durable library layer.

**Do not borrow HRR as a general KB retrieval substrate yet.** The implementation is interesting for fixed-capacity keyed facts, but the surrounding system still depends on readable JSON keys, prompt injection, and manual/tool-driven capture. It does not solve evidence retrieval, provenance, contradiction, or large-document navigation.

**Do not promote trace-derived facts without review when authority rises.** Nuggets' promotion bridge is the right shape to study and the wrong default for methodology knowledge. A fact crossing from scratch memory into a persistent host memory file should gain source links, review state, and a retirement path.

## Trace-derived learning placement

**Trace source.** Nuggets qualifies as trace-derived learning at this commit. The qualifying traces are user chat inputs, Pi tool-result events, session-compaction message windows, and recall events. It does not retain full conversation transcripts as the primary memory artifact; it extracts small facts, file paths, preferences, and task summaries from those traces.

**Extraction.** Extraction is mostly heuristic. Regex patterns capture preferences and "remember that" statements from user input; tool-result hooks capture file paths from read/edit/write calls; compaction hooks join the last few user messages into `_task`; recall calls may increment per-session hit counts when a session ID is supplied ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts), [src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts)). The oracle is code and the acting model's tool use, not a reviewer or evaluator.

**Storage substrate.** Extracted facts persist in `~/.nuggets/*.nugget.json`. Session-local reconstructed facts live in the Pi extension process. Gateway sessions persist under `.gateway/sessions`, schedule requests and jobs persist under `.gateway/cron`, and promoted high-hit facts can be written to Claude Code's project `MEMORY.md` if the expected host directory exists ([src/nuggets/promote.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/promote.ts), [src/gateway/config.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/config.ts)).

**Representational form.** Raw traces are chat/tool/session events managed by Pi. Distilled nugget facts are short prose key/value pairs inside symbolic JSON. The HRR memory is distributed-parametric working state rebuilt from those facts for recall. Schedule jobs are symbolic cron records plus prose prompts. `MEMORY.md` is prose Markdown grouped by nugget section. The operative behavior-shaping path is mixed: symbolic hooks select or write prose facts, HRR/fuzzy matching retrieves them, and prompt formatting turns them into instruction-channel text.

**Lineage.** Lineage is weak. A stored fact can often be recognized by key convention (`pref:`, `file:`, `edited:`, `_task`, `learn`), but it does not carry source message IDs, tool-call IDs, timestamps, extraction rule version, confidence, or source file revision. Promotion to `MEMORY.md` preserves nugget name, key, and value, but not the recall sessions that justified the hit count.

**Behavioral authority.** Raw chat and tool traces are source signals. Nugget JSON facts are knowledge artifacts when used as remembered context or recall answers. HRR confidence has ranking influence over which answer becomes active. Prompt-injected preferences, learnings, active files, and facts become temporary system-definition artifacts for Pi's next turn. `MEMORY.md` facts become stronger host-memory artifacts because Claude Code can load them as persistent context outside the Nuggets extension. Cron jobs and heartbeat prompts have routing authority: they decide that Pi should run at a later time with a particular prompt.

**Scope and timing.** Scope is personal-assistant and project-local. Capture occurs online during Pi sessions and tool use; prompt activation occurs before agent turns; heartbeat and cron activation occur later through the gateway. Promotion is staged at session compaction, but at this commit the live extension does not appear to pass session IDs into ordinary recall calls, so recall-count promotion may require paths outside the inspected default tool flow.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Nuggets belongs in the lightweight trace-to-fact and trace-to-host-memory family, adjacent to Pi-oriented personal memory systems rather than benchmark trajectory learners. It strengthens the survey distinction between raw trace evidence and behavior-shaping artifacts: chat text, extracted nugget fact, injected prompt block, schedule job, and promoted `MEMORY.md` entry each carry different authority.

## Curiosity Pass

**The HRR story is less important operationally than the key discipline.** The algebraic memory is real and tested, but the system's usefulness depends on short, stable keys that fuzzy matching can resolve. Bad keys or overpacked nuggets will fail in ways a user may experience as "the assistant forgot."

**The README is ahead of the checkout.** It advertises a plugin-first `nuggets-memory/` workspace and MCP package, but that directory is absent at the reviewed commit ([README.md](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/README.md)). The implemented source is the original Pi assistant/gateway path.

**Prompt injection is the main authority jump.** A preference stored as a JSON fact is relatively harmless; appending it under "Persistent Memory" to every agent turn gives it instruction-channel force. The code does not distinguish reviewed preferences from accidental regex captures.

**The scheduling bridge is intentionally simple but brittle.** Appending shell-escaped JSON into `.gateway/cron/requests.jsonl` makes Pi-to-gateway scheduling easy, but there is no validation beyond required fields and cron syntax matching during evaluation. The bridge is operationally useful, not a governed task system.

**Promotion is conceptually strong but implementation-coupled.** Writing frequently recalled facts into host memory is exactly the kind of authority gradient memory systems need. The current path depends on Claude Code's directory convention and on recall hit accounting that is not clearly fed by the default Pi tool recall path.

## What to Watch

- Whether the advertised `nuggets-memory-plugin` source appears in this repository or moves to a separate package with MCP tools.
- Whether Pi recall calls begin passing stable session IDs so the three-hit promotion rule works in ordinary use.
- Whether nugget facts gain source metadata, timestamps, confidence, or extraction-rule provenance.
- Whether `MEMORY.md` promotion adds review, deduplication by authority, contradiction handling, or retirement.
- Whether gateway cron jobs gain validation, per-user audit, and tests.
- Whether tests expand from HRR/memory primitives into Pi extension hooks, prompt injection, scheduling, and gateway behavior.

## Bottom Line

Nuggets is best read as a compact personal-assistant memory runtime: local keyed facts, HRR-backed recall, Pi prompt injection, chat reminders, and a partial bridge into Claude Code memory. Its strongest lesson for commonplace is not the HRR substrate itself, but the layered authority path from trace-derived scratch fact to prompt-visible context to host memory. Commonplace should borrow the authority-gradient framing and the tiny scratch-layer ergonomics, while requiring source lineage and review before any extracted fact becomes durable instruction.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - situates: Nuggets extracts preferences, file paths, task summaries, and recall-hit signals from Pi traces into later-consumed artifacts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: nugget JSON, HRR reconstruction state, prompt injections, cron jobs, and `MEMORY.md` entries need separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: stored nugget facts advise later recall and prompt construction.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: injected memory blocks, gateway prompts, cron prompts, and promoted host memory can instruct or route behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Nuggets explicitly activates stored facts through Pi hooks and gateway prompts.
