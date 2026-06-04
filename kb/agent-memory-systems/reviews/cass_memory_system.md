---
description: "CASS Memory review: trace-derived playbook rules over cass session logs, pull context scoring, MCP tools, outcome feedback, and trauma guard hooks"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# cass_memory_system

`cass-memory` is Jeffrey Emanuel's Bun/TypeScript procedural-memory layer for AI coding agents. It wraps the separate `cass` session-search engine with a `cm` CLI and MCP-style HTTP server that turn agent session logs into diary entries, playbook bullets, feedback events, outcome records, semantic embeddings, and safety "trauma" entries. The project is ambitious in its README language; the code-grounded system at this revision is strongest as a file-backed rule and warning layer over searchable session history, not as a self-contained autonomous learning agent.

**Repository:** https://github.com/Dicklesworthstone/cass_memory_system

**Reviewed commit:** [ff49fbd94339880f3b7bac0759026db6368f9bba](https://github.com/Dicklesworthstone/cass_memory_system/commit/ff49fbd94339880f3b7bac0759026db6368f9bba)

**Last checked:** 2026-06-01

## Core Ideas

**The canonical memory is a playbook, not the raw session index.** `src/types.ts` defines `PlaybookBullet` as the behavior-shaping unit: content, category, scope, maturity, feedback counters, source sessions, source agents, reasoning, tags, optional embeddings, and deprecation fields. `PlaybookSchema` persists these bullets in YAML through `src/playbook.ts`, while `cass` remains the external episodic search substrate rather than the durable procedural store ([src/types.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/types.ts), [src/playbook.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/playbook.ts), [src/cass.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/cass.ts)).

**Reflection is a staged trace-to-rule pipeline.** `orchestrateReflection` discovers unprocessed sessions through `cass`, exports and sanitizes each session, writes a diary entry, asks the reflector LLM for playbook deltas, validates those deltas, deterministically curates them into global or repo playbooks, and only then marks sessions processed ([src/orchestrator.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/orchestrator.ts), [src/diary.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/diary.ts), [src/reflect.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/reflect.ts), [src/curate.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/curate.ts)).

**Curation keeps the LLM away from final state mutation.** The reflector emits typed deltas, but `curatePlaybook` owns duplicate checks, conflict warnings, reinforcement, replacement, deprecation, merge handling, harmful-rule inversion, maturity promotion, demotion, and auto-deprecation. That is the main reliability boundary in the ACE story: LLMs propose; deterministic code applies or skips ([src/reflect.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/reflect.ts), [src/curate.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/curate.ts), [src/scoring.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/scoring.ts)).

**Read-back is mostly explicit context retrieval.** `cm context "<task>"` loads the merged playbook, filters active bullets by workspace scope, scores relevance with keywords plus optional embeddings, multiplies by effective confidence, searches `cass` history, checks deprecated patterns, and returns rules, anti-patterns, history snippets, and suggested searches ([src/commands/context.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/commands/context.ts), [src/semantic.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/semantic.ts)). The MCP server exposes the same `cm_context` tool, plus feedback, outcome, search, and reflection tools; these are still deliberate calls by the host or agent ([src/commands/serve.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/commands/serve.ts)).

**Feedback and outcomes are first-class maintenance signals.** Manual marks append helpful/harmful events; outcome logs can infer helpful or harmful feedback from success/failure, duration, errors, retries, sentiment, and context logs. Scoring decays old feedback by half-life, weights harmful feedback more heavily, and moves bullets through candidate, established, proven, or deprecated maturity states ([src/outcome.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/outcome.ts), [src/scoring.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/scoring.ts), [src/commands/why.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/commands/why.ts)).

**The trauma guard is a separate push/enforcement surface.** Trauma entries are regex patterns with severity, scope, status, trigger event, and provenance. `cm guard --install` writes a Claude Code `PreToolUse` hook that reads active trauma entries and denies matching Bash commands; `cm guard --git` installs a pre-commit hook that scans staged added lines. This is narrower than the playbook, but it is the clearest engineered push activation path in the code ([src/trauma.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/trauma.ts), [src/commands/guard.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/commands/guard.ts), [src/trauma_guard_script.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/trauma_guard_script.ts)).

## Artifact analysis

- **Storage substrate:** `files` — External agent session files indexed by the separate `cass` binary, with local and optional SSH remote searches
- **Representational form:** `prose` `symbolic` — Structured/prose transcripts are normalized into `CassSearchHit` objects and exported markdown/text
- **Lineage:** `authored` `imported` `trace-extracted` — Manual rules/configuration, starter or batch imports, external session stores, and reflected session traces all feed retained artifacts
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Context snippets and diaries inform; playbook bullets instruct; trauma hooks enforce; query/scoping paths route; schemas and validators check deltas; scoring/embeddings rank; feedback and outcomes update future rules

**Raw sessions and `cass` hits.** Storage substrate: external agent session files indexed by the separate `cass` binary, with local and optional SSH remote searches. Representational form: mixed structured/prose transcripts, normalized into `CassSearchHit` objects and exported markdown/text. Lineage: source evidence from Claude, Codex, Cursor, Aider, PI, and similar agent sessions; `cm` does not own the canonical session store. Behavioral authority: knowledge artifacts when returned as context snippets or used as reflection evidence; ranking authority lives in `cass` search results and `cm` query construction rather than in the raw traces themselves.

**Diary entries.** Storage substrate: JSON files under `config.diaryDir`, defaulting to `~/.cass-memory/diary`. Representational form: symbolic JSON with prose arrays for accomplishments, decisions, challenges, preferences, and key learnings. Lineage: derived from sanitized session exports by either LLM extraction or deterministic fast extraction; diary ids are content-derived, but generated entries do not retain a full prompt/version provenance bundle. Behavioral authority: knowledge artifacts for `why`, reflection, and related-session enrichment; they become part of system-definition lineage only when reflection consumes them to propose playbook deltas.

**Playbook bullets.** Storage substrate: YAML playbook files, default global `~/.cass-memory/playbook.yaml` plus optional repo `playbook.yaml`, merged at read time. Representational form: symbolic metadata wrapped around prose rules and anti-patterns, with optional distributed-parametric embeddings cached separately. Lineage: manual addition, starter import, batch import, LLM reflection from sessions, harmful-rule inversion, merge, replacement, and feedback/outcome reinforcement. Behavioral authority: system-definition artifacts when selected into `cm context` or MCP `cm_context` as task guidance; knowledge artifacts when inspected through `cm why`, export, or stats.

**Feedback, outcome, context, and processed logs.** Storage substrate: JSONL logs such as `outcomes.jsonl`, `context-log.jsonl`, processed reflection logs, privacy audit logs, and feedback arrays embedded in bullets. Representational form: symbolic event records with some prose context. Lineage: manual marks, context-use logs, session outcome calls, inline transcript feedback, and automatic outcome classification. Behavioral authority: learning input and evaluation/ranking influence; they do not instruct an agent directly, but they change future bullet scores, maturity, deprecation, and trace-processing idempotency.

**Embedding cache.** Storage substrate: `~/.cass-memory/embeddings/bullets.json`, guarded by a lock. Representational form: distributed-parametric vectors keyed by bullet id and content hash, with Xenova or Ollama backends. Lineage: derived from current bullet content and embedding model/version; content hash invalidates stale entries. Behavioral authority: ranking influence in context selection and similar-rule detection, not standalone advice ([src/semantic.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/semantic.ts)).

**Trauma entries and installed hooks.** Storage substrate: global `~/.cass-memory/traumas.jsonl`, project `.cass/traumas.jsonl`, and generated hook scripts under `.claude/hooks` or `.git/hooks`. Representational form: symbolic regex entries plus generated Python enforcement scripts. Lineage: manual `cm trauma add/import`, status changes through heal/remove, and potential audit-derived candidates; the stored trigger event records the source session path, timestamp, and human message. Behavioral authority: system-definition artifacts with enforcement force when a hook denies a Bash tool call or commit; knowledge artifacts when listed for human review.

**Configuration and agent-facing docs.** Storage substrate: global config, restricted repo config under `.cass/`, the package `SKILL.md`, and README/AGENTS guidance. Representational form: symbolic config plus prose instructions. Lineage: authored project files and user config edits. Behavioral authority: configuration, routing, and onboarding instruction. The README's "scientific validation" language is broader than the implementation guarantee: the code has LLM validation, semantic similarity checks, scoring, and outcome feedback, but not a controlled scientific proof that accepted rules causally improve future agents.

The promotion path is raw agent trace -> diary summary -> reflector delta -> validator/curator decision -> scored playbook bullet -> selected context or enforced guard. The system can strengthen prose advice into anti-pattern warnings and, in the trauma subsystem, into hook-level denial. It does not compile general playbook rules into validators or tests.

## Comparison with Our System

| Dimension | cass-memory | Commonplace |
|---|---|---|
| Primary purpose | Procedural memory for coding agents across session histories | Typed methodology KB for agents and maintainers |
| Canonical substrate | YAML playbooks, JSON diaries/logs, embedding cache, trauma JSONL | Git-tracked markdown notes, instructions, reviews, schemas, reports, indexes |
| Raw evidence | External `cass` session index and exported transcripts | Source snapshots, review outputs, logs, reports, git history |
| Learning loop | Session trace -> diary -> LLM deltas -> deterministic curation -> scored rules | Source/workshop artifacts -> reviewed notes/instructions -> validation/review gates |
| Read-back | Pull via CLI/MCP context; narrow push via trauma hooks | Mostly pull via search/indexes/links and explicit instruction loading |
| Governance | Zod schemas, locks, scoring decay, curation, validation heuristics, hooks | Type specs, collection contracts, deterministic validation, review gates, git lifecycle |

cass-memory is closer to an operational agent assistant than Commonplace. It assumes the user wants compact task guidance immediately before work and gives agents a single command to call. Commonplace assumes agents are navigating a durable knowledge base whose artifacts have explicit collection contracts and review state. That makes Commonplace heavier, but it also gives stronger provenance and replacement discipline for durable knowledge.

The strongest alignment is the retained-artifact split. cass-memory distinguishes raw traces, summaries, rules, feedback, embeddings, and guards, even though the README often presents them as one cognitive architecture. Commonplace should read this as evidence that agent memory systems need multiple authority levels: evidence, advice, ranking, learning input, instruction, and enforcement should not be collapsed just because all are "memory".

The main divergence is source preservation and auditability. cass-memory keeps source session paths and can show `why`, but playbook bullets do not carry a complete derivation record: reflector prompt version, validator result, exact diary excerpt, curation decision, embedding model, and outcome feedback path are scattered. Commonplace's artifact model is slower but better suited to inspectable lineage.

**Read-back:** `both` — Ordinary playbook and history memory reach the agent by explicit pull through `cm context`, `cm_context`, `memory_search`, or similar calls; retained trauma entries can reach and block the agent by before-action hooks without a deliberate memory query

### Borrowable Ideas

**Separate rule confidence from retrieval relevance.** cass-memory's context scoring combines task relevance with effective confidence. Commonplace could adopt that split for generated context packets or review recommendations: relevance says "about this task"; confidence says "still trusted." Ready when we have enough feedback signals.

**Use outcome logs as weak feedback, not truth.** The outcome pipeline converts success/failure, retries, and sentiment into decayed feedback. Commonplace could record similar signals for skills and instructions, but only as triage hints until reviewed. Needs a concrete consumer before adding.

**Keep LLM extraction outside deterministic curation.** The reflector/curator boundary is worth borrowing directly. For Commonplace, subagents can propose note edits, rule candidates, or warning acknowledgments, while deterministic validators and human/agent review decide durable authority. Already aligned; worth making explicit in future workflows.

**Treat harmful lessons as promotable warnings.** Inverting repeatedly harmful rules into anti-patterns is a useful lifecycle move. Commonplace could promote repeated review failures into warning notes, checklist items, or validation gates. Ready for review-system failure patterns.

**Installable hook enforcement should stay narrow.** The trauma guard shows how a small class of high-risk memories can become pre-action enforcement. Commonplace should not push every note this way, but narrow hooks for irreversible commands or known project hazards are plausible. Needs strict governance and bypass policy.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `tool-traces` `event-streams` — The review describes external `cass` session traces, exported transcripts, inline feedback markers, context logs, and outcome records as learning inputs.

**Learning scope:** `per-project` `cross-task` — Learning is global plus optional repo/workspace layering, with cross-agent related-session enrichment when enabled.

**Learning timing:** `staged` — Reflection runs after sessions exist through `cm reflect` or MCP `memory_reflect`, then updates playbooks.

**Distilled form:** `prose` `symbolic` `parametric` — Session traces become prose diary/playbook guidance, symbolic metadata/regex guards/scoring state, and optional embedding-backed ranking features.

**Trace source.** cass-memory qualifies as trace-derived learning. It consumes agent/session traces through the external `cass` index, exported session transcripts, inline feedback markers, context logs, outcome records, and optional cross-agent related-session searches. Reflection boundaries are sessions selected by processed-log state, lookback windows, workspace, agent filters, or an explicit session path.

**Extraction.** Extraction runs in several stages. `generateDiary` turns sanitized session exports into diary records using LLM extraction or deterministic fast extraction. `reflectOnSession` asks an LLM for typed deltas against the existing playbook and related history. `validateDelta` and rule validation apply quality, similarity, and evidence checks. `curatePlaybook` then applies deterministic deduplication, conflict detection, reinforcement, deprecation, inversion, promotion, and demotion.

**Scope and timing.** Scope is global plus optional repo/workspace layering. Timing is staged after sessions exist: `cm reflect` or MCP `memory_reflect` discovers unprocessed sessions and updates playbooks. The read-back loop is pre-task but pull-oriented: the agent or host calls `cm context` with the current task after learning has already been distilled.

**Authority transition.** Raw traces and diaries are knowledge artifacts. Reflector deltas are proposals. Curated playbook bullets become system-definition artifacts when selected into future task context. Feedback and outcome logs are learning inputs that change ranking and maturity over time. Trauma entries are the strongest promoted form because installed hooks enforce them before action.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), cass-memory belongs in the trace-to-prose-rule family with an unusually explicit maintenance layer: scored rules, maturity, harmful inversion, outcome feedback, optional embeddings, and hook-level escalation for hazardous patterns. It strengthens the survey's claim that trace-derived learning is not one mechanism: the same source traces can produce evidence snippets, summaries, advisory rules, ranking features, and hard guards.

## Read-back placement

**Direction.** cass-memory is both, but asymmetrically. The ordinary memory product is pull: an agent, human, or MCP host asks for context or search results. The trauma subsystem is push/enforcement: installed hooks receive a tool or commit event, load active retained trauma entries, match them against the pending command or staged diff, and return a denial/warning without the agent asking for memory.

**Read-back signal:** `coarse` `inferred / lexical` — Trauma hooks fire on coarse before-action hook events, then match retained trauma regexes against the pending command or staged diff lines.

**Faithfulness tested:** `no` — The review found context-use/outcome logging and mechanical hook enforcement, but no WITH/WITHOUT test proving selected memories changed agent behavior.

**Targeting and signal.** `cm context` uses an explicit task string, keyword extraction, workspace filters, optional embeddings, minimum relevance thresholds, decayed confidence, cass search, and deprecated-pattern checks. That pull selector is instance-targeted and inferred: lexical by default, with embedding ranking when semantic search is enabled. MCP `cm_context` wraps the same call. The trauma guard's hook entry is action-type keyed (`PreToolUse` for Bash commands or git pre-commit for staged diffs), but the retained-memory selection is instance-targeted: active trauma regexes are matched against the pending command or added diff lines, so the signal is inferred / lexical rather than an identifier match.

**Injection point.** Context retrieval happens before work only if the agent or host calls it. Trauma guard hooks fire before the risky Bash command or commit proceeds, so they can change the next action by denying it and showing the stored reason/reference.

**Selection, scope, and complexity.** Context read-back controls volume with `maxBulletsInContext`, `maxHistoryInContext`, `--limit`, `--history`, lookback days, workspace scope, history snippet truncation, and semantic/keyword scoring. Trauma read-back is narrow: one matching active trauma entry is enough to block. Precision is not established from code; regexes can false-positive or false-negative, and context relevance depends on task wording, embedding availability, and playbook quality.

**Authority at consumption.** Context output is advisory system-definition material: it can guide the agent but is not enforced. Deprecated warnings and anti-patterns are stronger advice. Trauma hooks are hard enforcement in the local environment because the Claude hook returns a denial decision and the git hook exits nonzero.

**Faithfulness.** The code records context use and outcomes and can feed those back into bullet scores, but I did not find a WITH/WITHOUT faithfulness test proving that specific selected bullets changed agent behavior. The hook path verifies enforcement mechanically, not downstream task quality.

**Other consumers.** Humans consume `cm why`, `cm stats`, `cm top`, `cm stale`, `cm trauma list`, exported playbooks, and onboarding samples. MCP clients consume tool responses. The same retained artifacts therefore serve agent context, human review, ranking, learning, and local safety governance.

## Curiosity Pass

**The scientific-validation claim outruns the code.** There are real validation mechanisms: Zod schemas, strict LLM output schemas, similarity checks, curation logs, feedback decay, outcome application, and tests. But "scientific validation" in the README should be read as an aspiration or product framing, not as a code-grounded experimental guarantee.

**The memory store is file-native but not repo-native by default.** Global state lives under `~/.cass-memory`, while repo rules can live in project files. That is convenient for cross-project agent use, but less reviewable than Commonplace's git-first artifacts unless the user deliberately exports or commits state.

**The strongest push mechanism is not the main memory mechanism.** The trauma guard qualifies for push activation, but it is a special safety lane, not general task-context injection. The ordinary procedural-memory path still relies on the agent remembering or being instructed to call `cm context`.

**Cross-agent learning is consent-gated in code.** Related-session enrichment only runs when cross-agent config is enabled and consent is given, and it can write a privacy audit log. That is more careful than the README's broad "all agents benefit" phrasing suggests ([src/diary.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/diary.ts), [src/types.ts](https://github.com/Dicklesworthstone/cass_memory_system/blob/ff49fbd94339880f3b7bac0759026db6368f9bba/src/types.ts)).

**Embeddings are optional and degraded visibly.** Semantic search is off by default in config, can use Xenova or Ollama, and falls back to keyword scoring with warnings when unavailable. That is a practical choice for an agent CLI, but it means semantic read-back quality is a deployment property, not a guaranteed system feature.

## What to Watch

- Whether playbook bullets gain compact derivation records: diary id, source excerpts, reflector prompt version, validator result, curation decision, and outcome evidence. That would move the system closer to auditable procedural knowledge.
- Whether `autoReflect` becomes an implemented post-session hook rather than a config field and command workflow. That would make trace-derived updates more continuous and would raise new consent and quality-gate questions.
- Whether context retrieval gains a host-side automatic pre-task integration. If MCP clients call `cm_context` before every task, the playbook path would become engineered push rather than pull.
- Whether general playbook rules can promote into validators, hooks, or tests. That would turn some prose rules into stronger system-definition artifacts, but it would need stricter review than current curation.
- Whether trauma scanning moves from heuristic audit candidates to a reviewed promotion pipeline. Hard-denial memories need better provenance and false-positive controls than ordinary advice.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: cass-memory distills agent/session traces into scored prose rules and, separately, enforceable trauma guards.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: ordinary playbook storage is pull-only unless a host calls `cm context`; trauma hooks are the activation exception.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: reflection turns past session behavior into future task guidance.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: context output loads compact rules and snippets instead of replaying full sessions.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: playbook bullets, scoring, embeddings, and hooks carry different kinds of behavior-shaping force.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - defined-in: cass-memory is useful mainly because it separates advice, ranking influence, learning input, and hard enforcement.
