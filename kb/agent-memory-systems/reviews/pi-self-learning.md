---
description: Pi extension (v0.5.0) that auto-extracts mistake/fix learnings into a scored, git-backed-by-default memory and injects them back into the next run
type: agent-memory-system-review
traits: [has-comparison, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# Pi Self-Learning

A [pi](https://github.com/badlogic/pi-mono) extension by Matteo Collina that keeps a memory of each coding session, git-backed by default when git integration is enabled. At `agent_end` it extracts what went wrong and how it was fixed, scores learnings by frequency and recency, and injects the top-ranked patterns into future sessions. Single-file TypeScript extension (`extensions/self-learning.ts`, 2556 lines) at v0.5.0, MIT license, still no automated test suite — `AGENTS.md` lists manual validation via the extension's own `/learning-*` commands as the only test path.

**Repository:** https://github.com/mcollina/pi-self-learning

## Core Ideas

**Automatic task-end reflection as the sole automatic mistake-capture trigger.** The extension registers a `pi.on("agent_end", ...)` handler (extensions/self-learning.ts:2032). When enabled and `autoAfterTask` is true, it serializes the last `maxMessagesForReflection` branch messages (default 8), runs an LLM prompt that expects strict JSON `{mistakes: [...], fixes: [...]}`, and appends the result to `daily/YYYY-MM-DD.md`. The reflection prompt is explicitly framed as mistake-prevention — it excludes accomplishments and progress summaries. Across the reviewed trace-derived systems this remains the tightest scope constraint: the only thing the extension will ever record is what went wrong.

**Scored core index with frequency + recency ranking.** Durable entries live in `core/index.json` as records keyed by a normalized learning key, with `{kind: "learning" | "antiPattern", hits, score, firstSeen, lastSeen}`. Each new occurrence adds `1 + Math.min(1, existing.hits * 0.08)` to `score` (self-learning.ts:1309). `effectiveScore` then subtracts `0.05 * ageDays` from the stored score at ranking time (self-learning.ts:1177–1181). `CORE.md` is rendered from the top-ranked slice of the index with a balanced learning/anti-pattern split, and `long-term-memory.md` is rendered from the entire index. Both are derived files — the canonical store is `index.json`.

**Four-tier temporal memory hierarchy, git-backed when enabled.** The memory root (default `.pi/self-learning-memory` in project mode, `~/.pi/agent/self-learning-memory` in global mode) contains:
- `daily/YYYY-MM-DD.md` — raw per-task reflection entries, append-only
- `monthly/YYYY-MM.md` — optional manually generated summaries of daily files
- `core/CORE.md` + `core/index.json` — top-ranked scored learnings
- `long-term-memory.md` — complete rendered history from the index

The memory root is a git repo distinct from the project repo when git integration is enabled, and each update auto-commits when `git.autoCommit` is true. The daily→core pathway is not synthesis — it is sorting. Daily files are verbatim reflections; core and long-term-memory are sorted projections of the same `index.json` records. Only manual monthly summaries and the global/redistill rewrites transform text.

**Interruption signals as first-class learning inputs.** Before building the reflection prompt, `collectInterruptionSignals` scans recent tool results against three regexes: a blocked/refused pattern, a permission-denied pattern, and a user-cancelled pattern (self-learning.ts:131–134). It also detects `stopReason === "aborted"` assistant turns and treats them as intent-change signals (self-learning.ts:493). Collected signals are inserted into the prompt inside an `<interruption_signals>` block with an accompanying rule: "Treat interruption/blocked/permission signals as intentional user-boundary evidence" and "Do not frame user interruption as random failure." This is a genuine design insight — the user pressing Esc or denying a tool carries extractable signal most systems ignore.

**Context injection with three-mode instruction policy.** `pi.on("before_agent_start", ...)` (self-learning.ts:2052) injects up to `context.maxChars` of memory (default 12_000): recent in-session runtime notes, `CORE.md`, optionally the latest monthly file and last N daily files. The `context.instructionMode` setting controls the injected system-prompt appendix:
- `off` — no memory policy
- `advisory` — suggest consulting memory
- `strict` — explicit "consult `CORE.md` first, check `daily/` and `monthly/` for historical questions, prefer evidence over guessing, fall back to `long-term-memory.md`"

The injected headings reference the resolved absolute paths of memory files, so the agent can read them by path rather than relying only on the embedded content.

**Two storage scopes with an explicit migration path.** `storage.mode` is `project` or `global`. In global mode the reflection prompt is amended with extra rules: "Distill each item into a cross-project rule reusable in any repository. Remove project-specific details (file names, module names, internal identifiers, phase labels, ticket references)" (self-learning.ts:538–542). The `/learning-redistill` command re-runs this rewrite over an existing `index.json` in chunks of 8, with a primary-then-repair two-pass parse loop and a model-resolution cascade. These are the system's two real transformation points; the routine `agent_end` loop in project mode is selection-only.

## Comparison with Our System

| Dimension | Pi Self-Learning | Commonplace |
|---|---|---|
| Learning trigger | Automatic post-task LLM reflection | Human writes notes; agent navigates existing knowledge |
| What gets recorded | Mistakes and fixes only | Any knowledge: insights, claims, decisions, comparisons |
| Storage substrate | Git-backed markdown in a dedicated shadow repo | Git-backed markdown in the project repo |
| Canonical record | `core/index.json` (derived files rendered from it) | Markdown notes with YAML frontmatter (files are canonical) |
| Ranking | Frequency + recency scoring with time decay | Human curation; `status` field (seedling → current → outdated) |
| Consolidation | Sort the index; optional LLM redistill/monthly summary | Human synthesis; `/connect` surfaces relationships |
| Context loading | Pre-inject scored learnings + policy prompt | CLAUDE.md routing + agent-driven progressive disclosure |
| Verification | None — JSON shape checked, content accepted | Type system + `/validate` + semantic review + link health |
| Integration | Shadow repo adjacent to project | Methodology and content share a single repo |

**Where pi-self-learning is stronger.** Zero-effort capture. Reflections run automatically; the user does not have to write anything, and accumulation happens in the background. The interruption-signal channel is genuinely novel — no other reviewed system elevates user abort and permission denial to learning inputs. For a working developer who will not maintain a knowledge system, the tradeoff is defensible.

**Where commonplace is stronger.** Scope and depth. Pi-self-learning only records mistake/fix pairs from the current session. It cannot capture design insights, connect ideas across domains, build arguments, or recognise when a learning is wrong. Verification is absent — extracted reflections pass through a JSON shape check and enter the record, so extraction errors compound silently.

**The underlying tradeoff is unchanged from last review.** Pi-self-learning optimises for automatic capture of operational patterns at the cost of knowledge depth and verification. Commonplace optimises for curated, deep knowledge at the cost of manual effort. Both are filesystem-first and git-backed; they serve different knowledge needs — mistake prevention versus understanding.

## Borrowable Ideas

**Interruption signals as learning inputs.** The scan for blocked commands, permission denials, and user aborts is cheap, simple, and captures real signal. Our `kb/log.md` append-during-traversal pattern could adopt this: when an agent encounters an error or is interrupted, append a one-line observation about why. *Ready to borrow* — requires a convention change, not infrastructure.

**Frequency + recency scoring with time decay as triage heuristic.** The `score + 1 + min(1, hits * 0.08)` increment combined with `score - 0.05 * ageDays` at ranking time is a concrete, cheap mechanism for the automated triage problem in [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md). If we ever triage log entries automatically, this is a reasonable starting heuristic. *Needs a use case first* — our log volume does not yet justify it.

**Two-scope storage with explicit rewrite on migration.** The `storage.mode` split (project vs global) plus `/learning-redistill` to rewrite project-local entries into portable rules is a clean model for knowledge portability. It maps to our note-versus-methodology distinction. *Interesting but low priority* — our KB is single-project.

**Derived-files-from-a-canonical-index pattern.** Pi treats `index.json` as canonical and regenerates `CORE.md` and `long-term-memory.md` on every update. This separates storage from presentation cleanly. We already lean the other way (markdown is canonical) and should stay there, but the pattern is worth remembering for any subsystem where we need multiple views over the same data.

## Curiosity Pass

**What property does the reflection pipeline claim to produce?** It claims "durable learnings" — patterns extracted from ephemeral session data that remain useful across future sessions.

**Does the mechanism transform the data, or just relocate it?** Mostly relocate. The `agent_end` step does transform: conversation prose → structured `{mistakes, fixes}` JSON. In global mode it transforms further by rewriting entries into cross-project action rules. Outside those capture-time rewrites, the pipeline is ranking and routing — not synthesis. Daily entries are appended verbatim. `CORE.md` is a sorted top-slice of `index.json`. `long-term-memory.md` is the whole index, sorted. The monthly summary is the only tier that performs genuine consolidation, and it is off by default (`includeLatestMonthly: false`). `/learning-redistill` is the other exception but is a manual migration command, not part of the default loop.

**What is the simpler alternative that achieves the same result?** Append mistakes to a single file. Count recurrences. Inject the top N into the system prompt. That captures ~90% of what this extension delivers in routine use. The temporal hierarchy (daily/monthly), the dedicated git repo, the balanced kind representation, the model-resolution cascade — all add engineering surface without proportionally more learning value. The scored flat list IS the mechanism; the rest is presentation.

**What could this mechanism achieve even if it worked perfectly?** It can surface recurring operational mistakes. It cannot: discover design insights, connect ideas across domains, recognise when a learning itself is wrong, or learn anything the agent did not make a mistake about in the current session. The mistake-only frame is both the strength (focused, actionable) and the ceiling (no positive knowledge, no cross-domain synthesis).

**The 12K context budget is still the binding constraint.** `maxChars: 12000` covers all injected memory combined. With `CORE.md` typically consuming most of it — and `includeLatestMonthly` and `includeLastNDaily` disabled by default — the effective memory the agent sees is just the top 20 core entries. The four-tier hierarchy exists but injection barely uses it.

**The two-pass parse-then-repair pattern is defensive, not fundamental.** Both reflection and redistill wrap the LLM call in a primary-plus-repair loop that triggers if the first output fails to parse as JSON. This handles models that wrap output in markdown fences or add commentary. It is legitimate production engineering but signals a mismatch between the system and its tool — a capable model with a well-crafted prompt should not need the repair path, and the presence of the path encourages looser prompting.

**v0.5.0 is plumbing, not architecture.** The only substantive change since v0.3.0 is a model-auth refactor: `ctx.modelRegistry.getApiKey()` → `resolveModelRequestAuth()` with a fallback chain that first tries `getApiKeyAndHeaders()` (newer pi versions with provider-specific headers) and falls back to `getApiKey()` (legacy). This lets the extension work with hosts whose auth is not a bare API key. No change to storage, scoring, injection, or trigger semantics — the critique above still applies unchanged.

**Trace-derived learning placement.** Pi Self-Learning qualifies as trace-derived and sits firmly in the single-session-extension quadrant. *Trace source:* the current pi branch's message history (up to `maxMessagesForReflection` entries, default 8) plus tool-result interruption signals scanned from a slightly larger window (`maxMessagesForReflection * 4`, minimum 24). *Automatic capture:* per-task `agent_end`; manual maintenance commands include `/learning-now` and `/learning-month`. *Extraction:* a single LLM call produces `{mistakes: string[], fixes: string[]}` under strict JSON schema enforcement; global mode adds an in-prompt rewrite to cross-project rules; no oracle or judge validates the content. *Promotion target:* inspectable markdown and scored `index.json`, nothing compiled into weights. Memory is filesystem-local, git-versioned, in a dedicated repo separate from the project — service-adjacent storage, not hosted. *Scope:* per-branch/per-project in project mode; cross-project in global mode (rewrites at capture time and via redistill). *Timing:* online during deployment (the `agent_end` hook fires after every completed task) with optional manual monthly summaries and an on-demand redistill cycle. On the survey's axes: axis 1 (ingestion pattern) — single-session extension, same bucket as Napkin; axis 2 (artifact vs weights) — symbolic artifacts only, scored flat rules subclass. No claim in the survey needs to strengthen, weaken, or split; Pi Self-Learning remains a stable reference point for "the tightest-scoped automated mistake-extraction loop." No new subtype is warranted — the derived-files-from-canonical-index pattern is interesting but not yet mirrored by another reviewed system.

## What to Watch

- **Does the mistake-only frame widen?** Users who want positive patterns (what worked, design decisions, architectural insights) have no capture path. If adoption grows, pressure to record successes will too.
- **Does ranking behave at scale?** With `maxCoreItems: 20` and unbounded `index.json`, the system accumulates arbitrarily many scored entries with only the top 20 visible. Does the `0.05/day` decay drop useful-but-infrequent learnings prematurely, or retain too much noise? The decay constant has not changed since v0.3.0.
- **Can rare high-severity failures survive the recurrence bias?** Frequency-weighted scoring privileges routine mistakes. One-off catastrophic failures may matter more than their recurrence count suggests.
- **Will other pi extensions absorb or replicate this?** Pi's hook model (`agent_end`, `before_agent_start`) makes this kind of system easy to build. Competing memory extensions could emerge, or pi itself could absorb the pattern.
- **Will a test suite appear?** `AGENTS.md` at v0.5.0 still states there is no automated test suite and manual validation via `/learning-*` commands is the only path. A 2556-line single-file extension with no tests is a maintenance liability that will either force a refactor or an explicit decision to keep validation manual.

---

Relevant Notes:

- [ClawVault](./clawvault.md) — also has scored observations with promotion, but a richer taxonomy (decision/lesson/preference/commitment/etc.) versus pi-self-learning's binary learning/antiPattern split
- [Napkin](./napkin.md) — adjacent single-session extension on pi; treats the session file as opaque and delegates extraction to a subprocess, where pi-self-learning mines the branch's structured message/tool history directly
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — the frequency+recency+decay scoring is a concrete implementation of automated triage, though limited to mistake-pattern extraction
- [distillation](../../notes/definitions/distillation.md) — the daily→core pathway mainly distills by selection (ranking); only global-mode reflection, `/learning-redistill`, and monthly summarization perform genuine transformation
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — pi-self-learning's daily files are ephemeral workshop artifacts promoted (by ranking) into a core library; the temporal hierarchy is a workshop-to-library bridge
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — the shadow git repo keeps memory inspectable, though separation from the project repo reduces discoverability
- [context-engineering](../../notes/definitions/context-engineering.md) — the `before_agent_start` injection (budget, instruction modes, selective file inclusion) is a lightweight context-engineering implementation
