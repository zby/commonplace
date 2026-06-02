---
description: "LACP review: local agent control plane with Claude hooks, staged memory extraction, SMS read-back, Obsidian brain, and policy gates"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# LACP

LACP is 0xNyk's local-first agent control plane for Claude, Codex, Hermes, and related terminal agents. It combines shell/Python command wrappers, Claude Code hooks, policy contracts, evidence gates, Obsidian brain tooling, session provenance, and a psychology-inspired self-memory system. As an agent memory system, its distinctive feature is not a single vector store but a control plane that turns session events, local files, Obsidian notes, hook state, and evaluation artifacts into behavior-shaping context and gates.

**Repository:** https://github.com/0xNyk/lacp

**Reviewed commit:** [003eef16a583dbaa3fdd56e5efe393397f463f3f](https://github.com/0xNyk/lacp/commit/003eef16a583dbaa3fdd56e5efe393397f463f3f)

**Last checked:** 2026-06-02

## Core Ideas

**Memory is a layer in a broader control plane.** The README frames LACP as a harness with policy gates, context contracts, provenance, verification loops, and a "5-layer memory" stack rather than as a standalone memory database ([README.md](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/README.md), [CLAUDE.md](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/CLAUDE.md)). The layers include Claude project memory, topic files, Obsidian/MCP knowledge, offline synthesis, agent identity, and provenance. This makes retained artifacts operational: they are read at session start, consulted through brain commands, checked by doctors, and tied to policy/evidence loops.

**Claude hooks are the main online activation path.** `session_start.py` gathers identity, git context, test command, focus brief, previous handoff, health snapshot, SMS context, context modes, workflow brief, and memory-cap warnings, then emits a Claude hook `systemMessage` under a rough token budget ([hooks/session_start.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/session_start.py)). `stop_quality_gate.py` evaluates the last assistant message, verifies test-pass claims when a command is known, writes handoff artifacts, records SMS episodes, and can block or inject feedback ([hooks/stop_quality_gate.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/stop_quality_gate.py)). The memory system therefore lives inside lifecycle events, not only in an explicit query API.

**The Self-Memory System gives session-start memory relevance gates.** `self_memory_system.py` stores episodes, epochs, narrative, and self-model JSON/JSONL under `~/.lacp/sms`, reads a focus brief as the "working self," applies significance decay, and builds a session context from current focus, preferred approaches, known biases, failure patterns, narrative arc, and recent significant episodes ([hooks/self_memory_system.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/self_memory_system.py)). The relevance signal is simple but explicit: current-goal overlap, significance thresholds, recency decay, and bounded recent episodes.

**Trace extraction feeds an offline brain pipeline.** `extract_memories.py` is a Stop hook that scans the latest assistant message or transcript for decisions, lessons, architecture choices, workflow rules, and user corrections, then appends up to five signals to `~/.lacp/memory-staging/pending.jsonl` ([hooks/extract_memories.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/extract_memories.py)). `lacp-brain-expand` promotes staged signals into Obsidian inbox notes, syncs sessions and research, runs consolidation/gap/review/curation stages, and synthesizes SMS epochs when enough episodes exist ([bin/lacp-brain-expand](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-brain-expand)). This is a trace-derived loop with a raw staging layer and a later promotion/consolidation layer.

**Context efficiency is priority and budget based, not learned ranking.** The online hook path sorts candidate injections by priority and stops when a rough `LACP_SESSION_BUDGET_TOKENS` estimate is exhausted. It caps `MEMORY.md` structurally, limits handoff summaries and file lists, injects only the last few high-significance SMS episodes, and keeps hook state in compact contracts ([hooks/session_start.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/session_start.py), [hooks/hook_contracts.py](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/hooks/hook_contracts.py), [CLAUDE.md](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/CLAUDE.md)). The offline brain path is broader and more complex; it depends on Obsidian/QMD/smart-connections-style tooling, staging, sync, curation, and review queues rather than one bounded retrieval call.

**Governance artifacts are first-class memory.** `config/context-profiles.json` renders host/cwd/branch/worktree contracts, `config/risk-policy-contract.json` maps changed paths to required checks and evidence, `lacp-loop` routes a command through sandbox-run, verify/canary, and optional rollback, while `lacp-canary` evaluates benchmark artifacts for promotion readiness ([config/context-profiles.json](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/config/context-profiles.json), [config/risk-policy-contract.json](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/config/risk-policy-contract.json), [bin/lacp-loop](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-loop), [bin/lacp-canary](https://github.com/0xNyk/lacp/blob/003eef16a583dbaa3fdd56e5efe393397f463f3f/bin/lacp-canary)). These are system-definition artifacts whose authority is validation, routing, budget, and release gating.

## Artifact analysis

**Claude project memory and topic files.** Storage substrate: files under `~/.claude/projects/<slug>/memory/`, especially `MEMORY.md` plus topic files described in `CLAUDE.md`. Representational form: prose with implicit routing structure; the hard line cap is enforced by hook warning and optional guard scripts rather than a formal schema. Lineage: authored by agents/users or generated by memory tooling; source-of-truth status is local filesystem state, with weak provenance unless linked to session/provenance artifacts. Behavioral authority: knowledge-artifact context when loaded by Claude, and system-definition-like authority when `MEMORY.md` contains instructions the model treats as standing context.

**Session-start injection bundle.** Storage substrate: ephemeral Claude hook output plus persisted hook contracts under `~/.lacp/hooks/contracts/<session>/` and state under `~/.lacp/hooks/state/`. Representational form: assembled prose `systemMessage` with symbolic priority labels, token estimate, contract fields, and environment-variable controls. Lineage: derived at session start from current repo/git state, focus file, handoff JSON, health snapshots, SMS files, context mode files, and environment variables. Behavioral authority: push advisory/system context for the receiving model; context modes and workflow briefs have stronger instruction/routing force than git summaries or health lines.

**SMS episodes, epochs, narrative, and self-model.** Storage substrate: `~/.lacp/sms/episodes.jsonl`, `epochs.jsonl`, `narrative.json`, and `self-model.json`. Representational form: mixed symbolic/prose dataclasses serialized as JSON/JSONL: session id, project, files touched, summary, decisions, outcomes, significance, epoch id, preferred approaches, biases, success/failure patterns, and narrative arc. Lineage: episodes are generated from Stop-hook transcript summaries and session change scans; epochs can be synthesized from recent episodes; self-model updates are inferred from outcomes, test failures, file counts, blocked state, and summary text. Behavioral authority: knowledge artifacts when inspected through `lacp sms`; system-definition artifacts when `build_session_context()` selects them for pre-action hook injection.

**Per-turn memory staging and Obsidian brain artifacts.** Storage substrate: `~/.lacp/memory-staging/pending.jsonl`, Obsidian vault inbox/knowledge directories, and LACP knowledge/workflow directories such as `data/workflows/brain-expand`. Representational form: raw extracted JSONL signals, markdown notes with YAML frontmatter, wiki links, QMD indexes, benchmark/review JSON, and generated synthesis/queue artifacts. Lineage: raw signals come from assistant/session transcripts via heuristic regexes; `brain-expand` promotes them into inbox notes with `source: per-turn-extraction`, syncs other sessions/research/repo notes, then routes, archives, consolidates, probes, and curates. Behavioral authority: initially evidence/context; promotion and curation move notes toward stronger retrieval/ranking/review authority in the Obsidian graph.

**Handoff, provenance, and hook telemetry.** Storage substrate: `~/.lacp/handoffs/<cwd-hash>-latest.json`, `~/.lacp/provenance/chain.jsonl`, pending provenance receipts, hook logs/contracts, and generated reports. Representational form: symbolic JSON records with prose summaries, modified files, test status, git branch/diff summary, receipt hashes, previous hashes, memory hashes, and timestamps. Lineage: derived from session transcript scans, git state, session contracts, and `MEMORY.md` hashes. Behavioral authority: knowledge artifacts when used as resume evidence; system-definition artifacts when session-start injects a recent handoff or provenance checks gate auditability.

**Policy, context, and risk contracts.** Storage substrate: repo-tracked JSON config and shell/Python command implementations. Representational form: symbolic policies, glob rules, required checks, context constraints, risk tiers, budgets, and command-line flags. Lineage: authored configuration; command outputs such as canary reports and optimize-loop proposals are derived from benchmark and verification artifacts. Behavioral authority: system-definition artifacts with enforcement/routing/evaluation force because `lacp-loop`, `lacp-sandbox-run`, `lacp-pr-preflight`, `lacp-canary`, and hook profiles consume them to allow, block, route, or recommend.

**Skill-factory and lessons artifacts.** Storage substrate: external `~/.agents/skills/auto-skill-factory` ledger/scripts and repo command wrappers such as `lacp-skill-factory`, `lacp-skill-score`, and `lacp-lessons`. Representational form: workflow ledgers, generated skills, confidence scores, lesson markdown. Lineage: derived from recorded workflow executions, validation captures, recency, success/validation rates, and manually added lessons. Behavioral authority: potential system-definition artifacts when a generated skill or lesson is installed into an agent runtime; in this repo the wrapper code shows the lifecycle surface more than a complete in-repo skill corpus.

Promotion path: LACP has several promotion ladders. A live assistant message can become a staging signal, an Obsidian inbox note, a curated/promoted graph note, a review/queue item, a synthesis, or a session-start memory. A session can become a handoff, provenance receipt, SMS episode, SMS epoch, and self-model update. A repeated workflow can become a skill-factory ledger entry and later a skill. The promotion machinery is broad, but quality varies by path: some promotion is schema/gate driven, while per-turn extraction is heuristic and low-confidence.

## Comparison with Our System

| Dimension | LACP | Commonplace |
|---|---|---|
| Primary purpose | Local control plane for agent sessions, hooks, policy, evidence, and memory | Git-native methodology KB for agent-operated knowledge bases |
| Canonical substrate | Local home-directory state, Obsidian vault, hook contracts, JSON configs, shell/Python commands | Repo markdown collections, type specs, schemas, indexes, reports |
| Online read-back | Claude hook `systemMessage` injection at session start and stop/eval feedback | Mostly deliberate pull through `rg`, indexes, links, and skills |
| Learning loop | Trace extraction, SMS episode/self-model updates, brain-expand promotion/consolidation, workflow skill ledgers | Source snapshots, authored notes, review gates, validation, curated indexes |
| Governance | Runtime gates, risk contracts, canary thresholds, hook blockers, context profiles | Static schemas, collection contracts, semantic review bundles, git history |
| Reviewability | Mixed: repo config is reviewable; home/vault/runtime memory needs export/inspection | Strong: durable artifacts are versioned, typed, archived, and validated |

LACP is much more operational than Commonplace. It is built to shape live agent sessions: inject context, block bad stops, route risky commands, cache tests, keep handoff state, and use local scripts as control surfaces. Commonplace is built to make durable knowledge artifacts understandable and reviewable across agents.

The strongest alignment is the idea that memory authority is not just storage. LACP separates standing prose memory, hook injection, SMS-derived summaries, Obsidian notes, policies, canary outputs, and risk contracts. Commonplace has a similar distinction among notes, instructions, type specs, validation reports, indexes, and reviews, but Commonplace keeps more of that authority inside one git-reviewed substrate.

The biggest divergence is substrate discipline. LACP's behavior-shaping state is spread across the repo, `~/.lacp`, `~/.claude`, an Obsidian vault, optional automation roots, QMD indexes, benchmarks, and plugin installs. That is practical for a local operator control plane, but it weakens whole-system auditability unless export/report commands are kept current.

Read-back: both - operators and agents can pull via `lacp brain-*`, `lacp obsidian`, `lacp sms`, `lacp reflect`, and explicit search/read commands; Claude lifecycle hooks also push selected context, SMS memory, handoff state, mode rules, quality feedback, and eval failures into the receiving model's context.

### Borrowable Ideas

**Priority-labeled context assembly.** Commonplace could make any future session-start loader sort candidate context by explicit priority and stop at a token budget. Ready for a prototype because it mirrors existing index/link/search discipline without requiring embeddings.

**Memory cap as a structural warning.** LACP treats oversized `MEMORY.md` as a model-underparsing risk, not a style issue. Commonplace should borrow this for any always-loaded or high-priority instruction bundle.

**Hook contracts as typed runtime state.** `hook_contracts.py` is a useful pattern for short-lived, typed state exchange between lifecycle hooks. Commonplace could use a similar contract for review runs or multi-step skills when state should be machine-readable but not promoted to library artifacts.

**Trace staging before promotion.** The pending JSONL -> inbox note -> promoted graph note path is worth borrowing conceptually. Commonplace already has workshop and review layers; a low-authority staging lane for trace-extracted candidate lessons would fit, as long as promotion remains explicit and validated.

**Local canary gates for retrieval quality.** LACP's canary thresholds and optimize loop are a concrete way to ask whether memory retrieval is still working. Commonplace should consider a small canary corpus for navigation/retrieval changes before adding automatic activation.

**Do not borrow home-directory sprawl without export discipline.** LACP's local state layout is appropriate for a personal control plane. Commonplace should keep durable methodology knowledge in repo artifacts unless runtime state has a defined export, lineage, and review path.

## Trace-derived learning placement

**Trace source.** LACP qualifies as trace-derived learning. Sources include Claude JSONL transcripts, last assistant messages, hook inputs, session-start/stop contracts, changed-file scans, test checkpoint state, provenance receipts, benchmark artifacts, workflow captures, and Obsidian/agent-daily/research sync inputs. The code-grounded paths are `extract_memories.py`, `stop_quality_gate.py`, `detect_session_changes.py`, `self_memory_system.py`, `lacp-provenance`, `lacp-brain-expand`, `lacp-reflect`, `lacp-skill-factory`, and `lacp-skill-score`.

**Extraction.** There are several oracles. Per-turn memory extraction is heuristic regex matching over assistant text, capped and anti-pattern filtered. SMS extraction is procedural: Stop-hook code summarizes the session, counts changed files, incorporates test-failure signals, computes significance from markers/context, writes an episode, and updates the self-model. Reflection reads provenance entries and generates prompts; brain-expand promotes staging into inbox notes and delegates deeper sync/consolidation/curation to automation scripts when present. Skill scoring uses success rate, validation rate, recency, and observation count as a confidence oracle.

**Four-field placement.** Raw traces are transcript files, hook inputs, benchmark JSON, provenance chains, and workflow ledgers. Distilled artifacts are staging signals, Obsidian notes, SMS episodes/epochs/self-model fields, handoff summaries, canary reports, lesson rules, and generated skills. The raw artifacts are mostly knowledge artifacts; distilled outputs gain stronger authority when hooks inject them, gates consume them, route policies enforce them, or skills become installed runtime instructions.

**Scope and timing.** Scope is local machine, project/repo, session, Obsidian vault, and sometimes cross-project agent identity. Timing is mixed: per-turn Stop extraction is online and cheap; SMS episode recording happens at Stop; session-start read-back is pre-action; brain-expand is staged/offline; reflection is weekly; canary/optimize loops are periodic or invoked as gates.

**Survey placement.** LACP sits in the trace-to-control-plane family. It strengthens the survey claim that durable behavior change usually happens after a distillation boundary: transcript snippets and session facts do not directly become authority until they are staged, promoted, injected, converted into SMS context, or consumed by a gate/skill.

## Read-back placement

**Direction.** LACP is both pull and push. Pull surfaces include Obsidian read/search, brain commands, SMS CLI, reflection summaries, canary reports, lessons linting, and explicit `lacp` commands. Push surfaces include Claude `SessionStart` `systemMessage` injection, Stop/eval feedback `systemMessage`s, quality-gate blocking, and context modes loaded automatically when configured.

**Trigger and relevance signal.** The central push trigger is the Claude `SessionStart` hook. Relevance is engineered by priority labels, environment-selected context modes, current cwd/git state, recent handoff age, focus-file freshness, health snapshot recency, SMS goal/significance/recency filters, and a token budget. Stop-time feedback is triggered by assistant output, transcript scans, test-success claim patterns, cached test command, context pressure, and optional blind-spot/quality-gate settings.

**Timing relative to action.** Session-start injection happens before the model acts in a new session and can change the next plan. `UserPromptSubmit` thinking nudge can shape the next response before answering a user prompt. Stop hooks run after an answer and can only block completion, inject corrective feedback for the next pass, or write artifacts for future sessions.

**Selection, scope, and complexity.** Selection is intentionally simple: sorted priorities, rough token accounting, 24-hour handoff freshness, focus staleness warnings, last three high-significance episodes, line caps, bounded summaries, and env/config flags. Scope is current cwd/project slug, current session id, home-directory LACP state, and configured vault/automation roots. Complexity can still become high because the assembled context may mix policy, identity, git state, tests, focus, health, SMS memory, handoff state, and mode rules in one `systemMessage`.

**Authority at consumption.** Session-start memory is advisory-to-instructional context depending on the injected part. Context modes and workflow briefs instruct behavior; git/test/health/handoff/SMS items provide evidence and reminders. Quality gates have stronger authority because they can block Stop or inject required feedback. Risk policies and context contracts have enforcement/routing authority in command paths.

**Faithfulness.** The code verifies structural activation: hooks emit `systemMessage`, quality gates can block, and tests cover hook output. I did not find an ablation proving that injected SMS or handoff context changes model behavior. Effective precision and behavioral uptake are therefore not verified from code.

**Other consumers.** Human operators consume the same artifacts through TUI/CLI reports, Obsidian, status reports, doctors, canary summaries, incident drills, and release/preflight gates. Schedulers and automation consume them as JSON contracts, shell exit codes, and report files.

## Curiosity Pass

**The "5-layer memory" label hides multiple axes.** LACP's docs correctly separate access tiers from lifecycle layers, but the implementation still mixes always-loaded memory, retrieval stores, offline synthesis, identity, provenance, policy, and evidence under one memory umbrella.

**The strongest read-back path is not Obsidian.** Obsidian is the richer knowledge substrate, but `session_start.py` plus SMS is the code path that most clearly pushes memory into a receiving model before action.

**Trace-derived does not always mean high-quality extraction.** `extract_memories.py` is deliberately heuristic and low-latency. Its outputs should be treated as low-confidence candidates until brain-expand/curation promotes them.

**The control plane creates many system-definition artifacts.** Risk contracts, context profiles, hook profiles, quality thresholds, canary thresholds, and generated skills can all shape future behavior. Reviewing LACP as "memory" without those artifacts would miss most of its authority.

**Local-first is a strength and an audit burden.** The zero-dependency/local stance makes adoption easier for terminal agents, but memory is scattered across local directories. The export/report surfaces become part of the trust model.

**Autoresearch and skill factory are adjacent learning loops.** `autoresearch/` evaluates memory and optimization targets, while skill-factory commands score workflow ledgers and generated skills. They show the direction of travel toward self-improvement, even where the durable learned artifacts live outside this repo by default.

## What to Watch

- Whether per-turn extraction gains source spans, prompt/model versions, confidence calibration, and a review gate before promotion into durable brain notes.
- Whether SMS read-back adds retrieval-quality tests or with/without ablations for injected session context.
- Whether home-directory/vault state gets a canonical export format so LACP memory can be reviewed like repo artifacts.
- Whether context assembly evolves from priority heuristics to typed budgets by artifact family, with separate caps for instruction, evidence, health, and memory.
- Whether generated skills from workflow traces become common enough to need stronger lineage, validation, and retirement policy.
- Whether canary metrics become tied to specific activation paths, not only benchmark artifacts, so read-back quality and behavioral uptake are measured separately.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: LACP distinguishes stored Obsidian/SMS/provenance state from hook paths that actually inject or gate behavior.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - exemplifies: LACP's memory spans hooks, policy, evidence, provenance, Obsidian, CLI workflows, and skill generation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: LACP requires separate classification for prose memory, JSON contracts, Obsidian notes, hook outputs, policy config, and generated skills.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: staged signals, notes, provenance receipts, handoffs, and reports mostly begin as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: hook profiles, context modes, risk policies, canary thresholds, quality gates, and generated skills can instruct, route, validate, or enforce behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: LACP turns session traces into staging records, SMS episodes, handoffs, provenance, and potential skills.
