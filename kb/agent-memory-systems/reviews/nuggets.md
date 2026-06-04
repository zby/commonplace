---
description: "Nuggets review: HRR key-value memory with Pi tools, auto-captured facts, pre-turn prompt injection, and gateway-driven proactive chat"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Nuggets

Nuggets, from `NeoVertex1/nuggets`, is a local TypeScript memory and messaging assistant built around fixed-capacity Holographic Reduced Representation (HRR) key-value stores. The reviewed checkout contains the original TypeScript memory engine, Pi agent extensions, and Telegram/WhatsApp gateway; the README also advertises a newer `nuggets-memory-plugin` package, but the referenced `nuggets-memory/` workspace is not present in this commit, so this review treats the plugin as documented but not code-grounded here.

**Repository:** https://github.com/NeoVertex1/nuggets

**Reviewed commit:** [714cab8a3b1fb843aa98dfb51584d2c07a6739f3](https://github.com/NeoVertex1/nuggets/commit/714cab8a3b1fb843aa98dfb51584d2c07a6739f3)

**Last checked:** 2026-06-02

## Core Ideas

**Memory is a tiny associative cache, not a document store.** A `Nugget` stores short key-value facts, rebuilds deterministic complex-valued HRR vectors from those facts, and recalls values by resolving a query to a stored key and decoding the associated value ([src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts), [src/nuggets/core.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/core.ts)). The implementation keeps source facts in JSON and rebuilds the vector state; vectors are behavior-shaping runtime state, not the durable source of truth.

**Kinds provide coarse routing before recall.** `NuggetShelf` manages multiple named nuggets and supports kind-ordered recall over `user`, `project`, and `agent` memory ([src/nuggets/shelf.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/shelf.ts), [src/nuggets/kinds.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/kinds.ts)). The kind inference is heuristic: preference-looking keys become user memory, file/path/test/repo-looking keys become project memory, and the rest defaults to agent memory.

**The Pi extension is the implemented agent-memory surface.** `.pi/extensions/nuggets.ts` registers a `nuggets` tool for `remember`, `recall`, `forget`, and `list`, gives the agent prompt guidelines for using it, hydrates durable shelf facts at session start, and injects remembered facts into the system prompt before each agent turn ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)). This is the strongest implemented read-back path: memory can arrive before action without the agent first issuing a recall command.

**Trace capture is narrow but real.** The extension extracts preference-like user input, records file paths from `read`, `edit`, and `write` tool results, reconstructs in-memory state from prior `nuggets` tool results in the session branch, and stores a compact `_task` summary plus recent tool file paths before compaction ([.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)). It does not run a broad transcript-to-lessons miner; most durable memory is still explicit agent/user/tool-event capture.

**Promotion exists, but the wired path is weaker than the README implies.** `promoteFacts()` writes facts with `hits >= 3` into Claude Code `MEMORY.md` and is called after Pi session compaction ([src/nuggets/promote.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/promote.ts), [.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts)). The `Nugget.recall()` API increments hits only when a `sessionId` is passed, but the Pi extension's tool recall calls `shelfRecall(query, nuggetName)` without a session id. At this commit, promotion is implemented as an API-level mechanism, but the inspected Pi host path may not accumulate the cross-session hit counts needed to trigger it.

**The gateway makes memory proactive by prompting the agent, not by retrieving memories itself.** The Telegram/WhatsApp gateway maintains one Pi subprocess per user, serializes messages, sends prompts over JSONL RPC, and schedules heartbeat/cron/timer events ([src/gateway/pi-rpc.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/pi-rpc.ts), [src/gateway/router.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/router.ts), [src/gateway/cron.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/cron.ts)). Heartbeats ask Pi to check memory and respond `NOTHING` if there is no useful follow-up; the relevance judgment is delegated to the agent with remembered context, not implemented as a standalone memory selector ([src/gateway/heartbeat.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/heartbeat.ts)).

**Context efficiency is bounded by fact shape and formatting, not retrieval budgets.** Nuggets keeps values short, stores facts as compact JSON, caps `files` prompt injection to the last ten entries, and gives status warnings based on a rough capacity estimate ([src/nuggets/memory.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts), [.pi/extensions/nuggets.ts](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts), [NUGGETS_INSTRUCTIONS.md](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/NUGGETS_INSTRUCTIONS.md)). There is no token budget, embedding ranker, source provenance filter, or semantic deduplication layer around pre-turn injection.

## Artifact analysis

- **Storage substrate:** `files` — Local JSON files under `~/.nuggets/`, one per nugget or kind
- **Representational form:** `symbolic` — Symbolic JSON records containing fact key, value, hit count, last-hit session, dimensions, bank count, and HRR configuration
- **Lineage:** `authored` `trace-extracted` — facts are written explicitly through the tool or derived from Pi user, tool-result, and compaction events
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — facts advise through recall and injection; extension code instructs capture/use; kinds and gateway state route; HRR/key matching ranks; trace capture learns short facts

**`.nugget.json` fact files.** Storage substrate: local JSON files under `~/.nuggets/`, one per nugget or kind. Representational form: symbolic JSON records containing fact key, value, hit count, last-hit session, dimensions, bank count, and HRR configuration. Lineage: authored by the agent/user through the `nuggets` tool or derived from Pi events such as preference input, file-tool results, and compaction summaries. Behavioral authority: knowledge artifacts when recalled explicitly; system-definition-adjacent context when the Pi extension injects them before an agent turn.

**HRR runtime vectors and key maps.** Storage substrate: in-memory TypeScript objects rebuilt from JSON facts, not serialized as the durable source. Representational form: distributed numeric complex vectors plus symbolic maps from tags to positions. Lineage: compiled deterministically from the nugget name, stored facts, dimension, bank count, and hyperparameters. Behavioral authority: ranking/selection influence during recall because the vector decode and token/key matching decide which value is returned.

**Pi extension memory state.** Storage substrate: process-local `Map<string,string>` plus the persistent `NuggetShelf`. Representational form: symbolic key-value facts rendered as prose prompt sections: Preferences, Learnings, Active Files, and Facts. Lineage: hydrated from durable shelf files at `session_start`, reconstructed from session-branch `nuggets` tool results, and updated from new tool calls/user inputs. Behavioral authority: push context before each agent turn through `before_agent_start`; the same facts also support the `/nuggets` UI and explicit tool recall.

**Claude `MEMORY.md` promoted facts.** Storage substrate: `~/.claude/projects/<cwd-safe>/memory/MEMORY.md` when the Claude project directory exists. Representational form: prose Markdown sections with bullet facts. Lineage: derived from nugget facts whose hit count reaches the promotion threshold. Behavioral authority: stronger always-loaded Claude project context once written. The promotion path is implemented, but its effective use in the Pi extension is not verified because the extension recall path does not pass a session id for hit tracking.

**Gateway session, cron, and heartbeat state.** Storage substrate: `.gateway/` directories for Pi session dirs, cron jobs, and schedule requests, plus live process-pool state. Representational form: symbolic JSON jobs/requests and JSONL RPC events, with prose prompts sent to Pi. Lineage: authored by user messages, schedule tool calls, cron evaluation, timers, heartbeat intervals, and gateway routing. Behavioral authority: orchestration authority over when Pi is prompted and which chat receives the response; memory relevance remains delegated to Pi and the injected/tool-accessible Nuggets facts.

**Pi extension command/tool definitions.** Storage substrate: `.pi/extensions/nuggets.ts` and `.pi/extensions/proactive.ts`. Representational form: executable TypeScript plus prose prompt snippets and tool guidelines. Lineage: authored integration code. Behavioral authority: system-definition artifacts because they define available tools, agent instructions for memory use, event hooks, extraction triggers, prompt injection, and scheduled-message behavior.

Promotion path: user input, tool result, explicit `remember`, or compaction state can become a local fact, then an injected prompt line, and possibly a Claude `MEMORY.md` bullet if hit tracking reaches the threshold. This is a real prose/symbolic promotion ladder, but it lacks review state, source spans, confidence, deduplication beyond key overwrite, and a verified recall-hit path through the inspected Pi extension.

## Comparison with Our System

| Dimension | Nuggets | Commonplace |
|---|---|---|
| Primary purpose | Fast local short-fact memory for Pi/chat agents | Git-native methodology KB for future agents and maintainers |
| Canonical substrate | Home-directory JSON fact files plus runtime HRR vectors | Typed Markdown artifacts, schemas, indexes, and review reports |
| Capture loop | Explicit `remember`, preference regexes, file-tool events, compaction summaries | Source snapshots, authored notes, skills, validation, semantic review |
| Read-back | Tool recall plus pre-turn prompt injection | Mostly deliberate pull through search, indexes, links, and skills |
| Governance | Key overwrite, capacity warnings, tests for core math and memory API | Collection contracts, type specs, deterministic validation, review bundles, git history |
| Context economy | Short values, approximate associative recall, grouped injection, last-ten file cap | Routing contracts, indexes, type-specific loading, explicit source/review lifecycle |

Nuggets and Commonplace both reject "raw transcript as memory" as the main durable substrate. Nuggets compresses working facts into a tiny associative cache; Commonplace promotes source-grounded claims into typed Markdown artifacts. Nuggets is better suited to immediate operational recall: "where is the auth handler?", "what command worked?", "what preference did the user state?" Commonplace is better suited to inspectable methodology: claims need provenance, routing, review state, and links.

The central tradeoff is authority without governance. Nuggets can inject remembered facts before every Pi turn, which gives small facts immediate behavioral force. But the fact record has no source pointer, author/reviewer, expiration, confidence, or semantic type beyond the key and inferred kind. Commonplace moves more slowly because durable artifacts carry more contract.

**Read-back:** `both` — Explicit `nuggets` tool recall is pull, while Pi `before_agent_start` injection pushes current remembered facts into the agent before action; gateway heartbeats and cron jobs push prompts to Pi, but the retained-memory push still comes from Pi's injected or tool-accessible Nuggets facts rather than a gateway-side memory selector

### Borrowable Ideas

**Treat short facts as an L1 cache, not a competing KB.** Commonplace could use a tiny, scoped fact cache for repeated file locations, commands, and user preferences during workshop work. Ready only if the cache has explicit expiry and never bypasses promoted artifact review.

**Separate durable facts from compiled recall state.** Nuggets stores inspectable JSON facts and rebuilds numeric vectors. Commonplace should preserve this principle for any future embedding or ranking layer: generated indexes can accelerate recall, but authored artifacts remain canonical.

**Use event capture for low-risk operational facts.** Auto-capturing read/edit file paths is a pragmatic source of future navigation hints. Commonplace could capture similar hints in temporary workshop state, but promotion into notes should require review.

**Pre-turn memory injection should carry a budget and provenance.** Nuggets shows the usefulness of push activation, but also its risk: all grouped facts can become prompt context without source framing. Commonplace should not borrow this without token budgets, source pointers, and authority labels.

**Promotion by observed reuse is promising but needs a working counter path.** Hit-count promotion to `MEMORY.md` is a useful design sketch. Commonplace could treat repeated successful recall as a candidate-promotion signal, but only after verifying that the recall path records sessions and that promoted facts keep lineage.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` `event-streams` — Pi session messages, user input, tool results, compaction windows, and extension event hooks feed capture

**Learning scope:** `per-task` `per-project` `cross-task` — compaction summaries are task-shaped, file/project facts are project-shaped, and durable user/agent facts can cross tasks

**Learning timing:** `online` `staged` — user and tool-result capture happens during the session, while compaction capture and promotion are staged around session compaction

**Distilled form:** `prose` `symbolic` `parametric` — trace signals become short JSON facts, rendered prompt or `MEMORY.md` prose, and rebuilt HRR vector state

**Trace source.** Nuggets qualifies as trace-derived learning through the Pi extension, not through the HRR math alone. Raw signals include user input text, `read`/`edit`/`write` tool-result file paths, prior `nuggets` tool results in the session branch, messages selected for compaction, and assistant tool-use blocks in the compaction window.

**Extraction.** Extraction is deterministic and narrow. Preference capture uses regexes over user input. File capture reads `file_path` or `path` from tool inputs/results and stores `file:<basename>` or `edited:<basename>`. Compaction capture stores a short `_task` summary from recent user messages and recent file paths from tool-use blocks. Explicit `remember` remains the highest-confidence extraction path because the agent chooses the key and value.

**Four-field placement.** Raw traces are Pi session messages, tool events, and user inputs. Distilled artifacts are short JSON facts and, potentially, promoted `MEMORY.md` bullets. The raw traces are evidence; the distilled facts become behavior-shaping artifacts when injected into the system prompt, recalled by the tool, or promoted into Claude project memory.

**Scope and timing.** Scope is local-user/local-project in practice: `~/.nuggets/` is shared by the host process, while gateway sessions and cron state are per chat/JID. Timing is mixed: input/tool-result capture happens online; compaction capture happens before session compaction; promotion happens after session compaction if the hit threshold is met.

**Survey placement.** Nuggets sits in the trace-to-short-fact branch. It strengthens the distinction between trace-derived capture and trace-derived reasoning: the system extracts operational facts from traces, but it does not synthesize lessons, procedures, validators, or model updates from trajectories.

## Read-back placement

**Direction.** Nuggets is both pull and push. Pull is the `nuggets` tool's `recall` action and the `/nuggets` inspection command. Push is the Pi extension's `before_agent_start` hook, which appends remembered facts to the system prompt before the agent acts.

**Read-back signal:** `coarse` — the push path fires for every Pi agent turn after facts are loaded or captured, without identifier or inferred relevance matching for the current turn

**Read-back timing:** `pre-action` — prompt injection happens before the receiving agent turn acts; capture and promotion affect later turns rather than returning memory to the completed action

**Faithfulness tested:** `no` — the review found structural activation but no with/without behavioral test for injected facts

**Targeting and signal.** The push path is `coarse`: the `before_agent_start` hook fires on every Pi agent turn after facts are loaded or captured and injects remembered facts from the current session map. There is no instance-level `identifier` or `inferred` signal for the push; grouping by key prefix and the last-ten file cap are scope controls, not relevance matching for this turn. Explicit pull recall uses key resolution, token-overlap fallback, and HRR decoding.

**Timing relative to action.** Prompt injection happens before the agent turn and can affect the next action. Preference and file captures happen during input/tool events and become available for later turns. Compaction capture and promotion happen around session compaction and affect future turns/sessions.

**Selection, scope, and complexity.** Selection is broad for preferences, learnings, and other facts, bounded only by what has been remembered in the current map; active files are capped. Scope comes from the shelf kind, current session reconstruction, and local home-directory storage. Complexity stays low because values are expected to be short facts, but context dilution can still grow if many facts accumulate.

**Authority at consumption.** Injected facts are advisory context with system-prompt placement. Promoted `MEMORY.md` facts would have stronger always-loaded Claude project-memory authority. Tool recall returns a value with confidence/source metadata, but using it remains up to the agent.

**Faithfulness.** The code proves structural activation: the hook appends prompt text and the gateway can prompt Pi proactively. I did not find with/without ablations or behavioral tests showing that injected facts improve decisions or that false memories are ignored.

**Other consumers.** Human users can inspect facts through the Pi UI command and chat with the gateway. The gateway consumes cron/heartbeat state as scheduler input, but it does not directly consume memory facts except through Pi.

## Curiosity Pass

**The advertised plugin is outside the reviewed code.** The README says to use `nuggets-memory-plugin` and references `nuggets-memory/`, but that workspace is absent from this commit. The implemented evidence is the original app/gateway/Pi extension.

**The HRR layer may be less important than the integration layer.** For the reviewed agent-memory behavior, the important mechanisms are capture, injection, and promotion. HRR makes recall fast and compact, but pre-turn injection uses the fact list directly.

**Promotion is an attractive idea with an integration gap.** The threshold logic exists, and tests cover hit counts in the core API, but the Pi extension's recall path does not pass a session id. That makes the README's "3+ recalls across sessions" claim weaker for the inspected host path.

**Trace-derived does not mean transcript understanding here.** Nuggets extracts preferences, file paths, and task summaries. It does not infer durable methodology, causal lessons, or verified procedures from completed work.

**Proactivity is scheduler-mediated.** Heartbeats and cron jobs can wake Pi and ask it to check memory. The gateway does not itself perform relevance-gated memory retrieval; Pi has to follow the prompt and use its injected/tool-accessible memory.

## What to Watch

- Whether the repository adds the advertised `nuggets-memory-plugin` source, because MCP tools such as `guide`, `nudges`, and `status` could change both read-back and governance.
- Whether Pi recall starts passing a stable session id, making hit-count promotion to `MEMORY.md` operational rather than mostly API-level.
- Whether injected facts gain source metadata, timestamps, expiry, or confidence so pre-turn push activation can be audited.
- Whether trace extraction expands beyond regex/file-path capture into reviewed candidate lessons, and whether those lessons get a promotion gate before prompt authority.
- Whether prompt injection gains token budgets, per-kind caps, or query-conditioned selection to prevent the fact cache from becoming ambient clutter.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Nuggets extracts short operational facts from Pi user/tool/session traces rather than learning weights or broad procedures.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: facts matter only when recalled by the tool, injected by the hook, or promoted to Claude memory.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Nuggets separates JSON facts, HRR runtime vectors, prompt injections, gateway scheduler state, and promoted Markdown by substrate, form, lineage, and authority.
- [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) - compares: Nuggets uses pre-turn system-prompt injection and optional Claude `MEMORY.md` promotion as harness-level activation paths.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - qualifies: Nuggets performs low-complexity trace extraction from user inputs, tool paths, and compaction summaries.
- [Activate Behavior-Changing Memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - supports: the Pi `before_agent_start` hook is the behavior-changing activation surface, while stored facts alone are inert.
