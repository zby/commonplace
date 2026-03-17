---
description: Pi extension with automatic task-end reflection, scored learnings index, temporal memory hierarchy (daily/monthly/core), and context injection — purest implementation of the automated mistake-extraction loop among reviewed systems, but the reflection pipeline relocates rather than transforms
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-16
---

# Pi Self-Learning

A [pi](https://github.com/badlogic/pi-mono) extension by Matteo Collina that keeps a git-backed memory of each coding session. After each completed agent task, it extracts what went wrong and how it was fixed, scores learnings by frequency and recency, and injects the highest-scoring patterns into future sessions. Single-file TypeScript extension (~2500 lines), MIT license, no test suite.

**Repository:** https://github.com/mcollina/pi-self-learning

## Core Ideas

**Automatic task-end reflection as the primary learning trigger.** On `agent_end`, the extension serialises the last N messages (default 8), sends them to an LLM with a prompt asking for `{"mistakes":["..."],"fixes":["..."]}`, and appends the result to a daily markdown file. The reflection prompt is framed as a "mistake-prevention reflection engine" — it explicitly excludes accomplishments and progress summaries. This is the tightest scope constraint among reviewed learning systems: the system only records what went wrong.

**Scored core index with frequency + recency ranking.** Learnings accumulate in `core/index.json` as records with `key`, `text`, `kind` (learning or antiPattern), `hits`, `score`, `firstSeen`, `lastSeen`. Each new occurrence increments score by `1 + min(1, hits * 0.08)` — a light repetition bonus. Effective score decays at 0.05 points per day since last seen. The top-ranked items render into `CORE.md` with balanced representation (learnings and watch-outs each get reserved slots). This is the system's only transformation mechanism: repeated observations float up, stale ones sink.

**Temporal memory hierarchy with git-backed persistence.** Four storage tiers:
- `daily/YYYY-MM-DD.md` — raw per-task reflections, append-only
- `monthly/YYYY-MM.md` — LLM-generated summaries of daily files
- `core/CORE.md` — top-ranked durable learnings, rendered from the scored index
- `long-term-memory.md` — complete learning history, also rendered from the index

Each tier lives in a dedicated git repository (separate from the project repo). Commits happen automatically after each memory update. The hierarchy looks like progressive distillation but the daily→core pathway is ranking, not synthesis — the same text surfaces or sinks, it doesn't get compressed or rewritten (except by the redistill command, discussed below).

**Context injection before agent start.** On `before_agent_start`, the extension injects: (1) recent in-memory runtime notes from the current session, (2) contents of `CORE.md` and optionally daily/monthly files up to a budget (default 12K chars), and (3) a system prompt appendix instructing the agent to consult memory files for historical questions. The injection is configurable with three instruction modes (off, advisory, strict) that range from no policy to "you MUST consult self-learning memory."

**Interruption signals as first-class learning inputs.** The extension scans recent tool results for blocked commands, permission denials, and user aborts (Esc/interrupt), treats these as intent-change signals, and includes them in the reflection prompt. The reflection prompt then requires at least one prevention-oriented mistake and fix for each interruption. This is a genuine design insight — user interruptions carry information about what the agent should not have done.

**Two-scope storage modes for portability.** Project mode keeps repository-specific details; global mode distills reflections into cross-project reusable rules. The `redistill` command rewrites existing index entries through an LLM to remove project-specific identifiers (file names, paths, class names), converting project-local learnings into portable action rules. This is the only place the system performs actual content transformation.

## Comparison with Our System

| Dimension | Pi Self-Learning | Commonplace |
|---|---|---|
| Learning trigger | Automatic post-task reflection via LLM | Human writes notes; agent navigates existing knowledge |
| What gets recorded | Mistakes and fixes only | Any knowledge: insights, claims, decisions, comparisons |
| Storage substrate | Git-backed markdown in a shadow repo | Git-backed markdown in the project repo |
| Ranking mechanism | Frequency + recency scoring with time decay | Human curation; status field (seedling → current → outdated) |
| Consolidation | Ranking (daily → core) + optional LLM redistill | Human-authored synthesis; `/connect` discovers relationships |
| Context loading | Inject scored learnings + system prompt policy | CLAUDE.md routing table + agent-driven progressive disclosure |
| Verification | None — LLM output accepted as-is with JSON schema enforcement | Type system + `/validate` + semantic review + link health |
| Inspectability | Readable markdown, but shadow repo is separate from project | Fully integrated — methodology IS the content |

**Where pi-self-learning is stronger.** Zero-effort learning — the user doesn't have to do anything. Reflections happen automatically after every task, learnings accumulate without conscious attention, and the scoring surface drives automatic curation. For a working developer who doesn't want to maintain a knowledge system, this is the right trade-off. The interruption-signal extraction is also genuinely novel — no other reviewed system treats user abort as a learning input.

**Where commonplace is stronger.** Knowledge scope and depth. Pi-self-learning can only learn from mistakes in the current session; it can't capture design insights, connect ideas across domains, or build structured arguments. The mistake-only frame excludes most of what a knowledge system needs to know. And the verification story is absent — extracted reflections are accepted without validation, so extraction errors compound silently.

**The fundamental trade-off.** Pi-self-learning optimises for automatic capture of operational patterns at the cost of knowledge depth and verification. Commonplace optimises for curated, deep knowledge at the cost of manual effort. Both are filesystem-first and git-backed, but they serve different knowledge needs — mistake prevention vs. understanding.

## Borrowable Ideas

**Interruption signals as learning inputs.** The pattern of scanning for blocked commands, permission denials, and user aborts to feed into reflection is simple, cheap, and carries real signal. Our `kb/log.md` append-during-traversal pattern could adopt this: if an agent encounters an error or the user interrupts, append a one-line observation about why. *Ready to borrow* — requires only a convention change, no infrastructure.

**Frequency + recency scoring for observation triage.** The `index.json` scoring model — increment on repetition, decay over time — is a concrete mechanism for the automated triage problem in [automating KB learning is an open problem](../automating-kb-learning-is-an-open-problem.md). If we ever build automated log triage, this scoring function is a reasonable starting heuristic. *Needs a use case first* — our log volume doesn't yet justify automated triage.

**Two-scope storage with redistill.** The global/project storage split and the redistill command that converts project-local learnings into portable rules is a clean pattern for knowledge portability. This maps to the distinction between project-specific notes and general methodology in our KB. *Interesting pattern but low priority* — our KB is currently single-project.

## Curiosity Pass

**What property does the reflection pipeline claim to produce?** It claims to produce "durable learnings" — persistent patterns extracted from ephemeral session data. The daily→core pathway is supposed to distill volatile session reflections into stable, reusable knowledge.

**Does the mechanism transform the data, or just relocate it?** Mostly relocate. The reflection step does transform: unstructured conversation → structured `{mistakes, fixes}` JSON. But from there, the pipeline is ranking, not transformation. Daily entries are appended verbatim. The core index tracks the same text strings with scores — no synthesis, no compression, no connection to other knowledge. `CORE.md` is a sorted subset of `index.json`. `long-term-memory.md` is a complete dump of `index.json`. The monthly summary is the only tier that performs genuine consolidation (LLM summarises daily files), and it's optional and rarely injected into context.

The redistill command is the exception — it genuinely transforms by rewriting entries to remove project-specific identifiers. But redistill is a manual, one-time operation (`/learning-redistill`), not part of the automatic pipeline.

**What's the simpler alternative that achieves the same result?** Append mistakes to a single file. Sort by recurrence count. Inject the top N into the system prompt. This achieves ~90% of what pi-self-learning does — the temporal hierarchy (daily/monthly), the dedicated git repo, the balanced kind representation, and the elaborate model resolution cascade add engineering complexity without proportionally more learning. The scored flat list IS the mechanism; the rest is presentation.

**What could this mechanism actually achieve, even if it works perfectly?** It can surface recurring operational mistakes. It cannot: discover design insights, connect ideas, build arguments, recognise when a learning is wrong, or learn anything the agent didn't make a mistake about in the current session. The mistake-only extraction frame is both the system's strength (focused, actionable) and its ceiling (no positive knowledge, no cross-domain synthesis).

**The repair-loop pattern is over-engineered for what it does.** Both reflection and redistill have a two-pass strategy: primary LLM call → parse → if parse fails → repair LLM call → parse. This handles models that wrap JSON in markdown fences or add commentary. But the underlying operation (extract mistakes from conversation text) is simple enough that a well-crafted prompt with a capable model shouldn't need repair. The repair loop is defensive engineering against model unreliability — legitimate for production, but a sign that the system is working against its tool rather than with it.

**The 12K context budget is the real constraint.** `maxChars: 12000` for all injected memory combined means the system is competing with the task for context space. With `CORE.md` potentially consuming most of that budget, the daily and monthly files rarely get injected in practice (both are disabled by default). The temporal hierarchy exists but the context injection barely uses it — the effective memory is just the top-ranked core learnings.

## What to Watch

- **Does the mistake-only frame limit adoption?** Users who want to learn positive patterns (what worked well, design decisions, architectural insights) have no mechanism for it. Will the system evolve toward broader knowledge capture, or stay focused on mistake prevention?
- **How does the scoring behave at scale?** With `maxCoreItems: 20` and unbounded `index.json`, the system will eventually have thousands of scored entries where only the top 20 are visible. Does the decay function cause useful-but-infrequent learnings to drop out prematurely?
- **Will the pi extension ecosystem produce competing memory systems?** Pi's extension model (hooks on `agent_end`, `before_agent_start`) makes this kind of system easy to build. Multiple memory extensions with different approaches could emerge.

---

Relevant Notes:

- [ClawVault](./clawvault.md) — also has scored observations with promotion, but richer taxonomy (decision/lesson/preference/commitment) vs. pi-self-learning's binary (learning/antiPattern)
- [Automating KB learning is an open problem](../automating-kb-learning-is-an-open-problem.md) — the pi-self-learning scoring mechanism is a concrete implementation of automated triage, though limited to mistake-pattern extraction
- [Distillation](../distillation.md) — the daily→core pathway claims distillation but primarily performs ranking; the redistill command is the only genuine content transformation
- [A functioning KB needs a workshop layer](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — pi-self-learning's daily files are ephemeral workshop artifacts that get promoted to core; the temporal hierarchy IS a workshop-to-library bridge
- [Inspectable substrate defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — pi-self-learning's shadow git repo maintains inspectability, though separation from the project repo reduces discoverability
- [Context engineering](../context-engineering.md) — the context injection system (`before_agent_start` with budget, instruction modes, and selective file inclusion) is a lightweight context engineering implementation
