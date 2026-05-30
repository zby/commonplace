---
description: "Local agent control plane with routed execution, Claude hooks, Obsidian memory automation, receipts, provenance, and operational gates"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# LACP

LACP is a local agent control plane by 0xNyk for hardening Claude, Codex, Hermes, and similar CLI agents. At the reviewed commit it is less a single memory backend than an operations stack: shell commands route work through risk tiers and budgets, Claude hooks inject context and block unsafe behavior, Obsidian automation maintains a knowledge graph, and run receipts/provenance/manifests make agent activity auditable.

**Repository:** https://github.com/0xNyk/lacp

**Reviewed commit:** [7bdd7ab3655cf19876a9f7c95f6584725adc5e72](https://github.com/0xNyk/lacp/commit/7bdd7ab3655cf19876a9f7c95f6584725adc5e72)

## Core Ideas

**The command surface is a local control plane around existing agents.** The top-level `lacp` dispatcher launches the native REPL with no arguments, treats unknown first arguments as prompt text for `lacp-stream`, and otherwise dispatches to a large set of `lacp-*` subcommands for routing, doctors, hooks, harnesses, memory, provenance, release gates, worktrees, swarms, and Obsidian operations ([bin/lacp](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp)). The behavior-shaping surface is mixed: shell scripts are symbolic system-definition artifacts when they route and enforce, while the generated reports they read and write are usually knowledge artifacts unless a later command consumes them as a gate.

**Routing turns task text and risk flags into execution policy.** `config/sandbox-policy.json` defines three execution tiers, risk-tier mappings, cost ceilings, critical signals, keyword routing, and model-slot hints ([config/sandbox-policy.json](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/config/sandbox-policy.json)). `lacp-route` lowers the task string, matches remote/local/critical keywords, applies trust and sensitivity flags, selects a risk tier, cost ceiling, remote provider, and model hint, and emits JSON for downstream commands ([bin/lacp-route](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-route)). This is not memory retrieval; it is a system-definition artifact that shapes which execution channel an agent receives.

**Sandbox runs combine policy gates with durable receipts.** `lacp-sandbox-run` wraps command execution with critical-risk confirmation, budget confirmation, TTL approval for review-tier routes, optional input contracts, context contracts, and session fingerprints for mutating or remote-target commands ([bin/lacp-sandbox-run](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-sandbox-run)). Whether it executes directly, falls back from an unset local sandbox runner, or blocks, it writes a JSON receipt under `$LACP_KNOWLEDGE_ROOT/data/sandbox-runs` with route decision, command, exit code, contract validity, runner metadata, and provider metadata. Those receipts are raw operational traces and audit knowledge artifacts; they become behavior-shaping only when commands like `lacp-report`, `lacp-trace-triage`, canary gates, or manual operators use them to alter future routing or work.

**Claude hooks provide the strongest live behavior shaping.** The hook set includes `session_start.py`, `pretool_guard.py`, `stop_quality_gate.py`, eval checkpoints, telemetry, and contract exchange ([AGENTS.md](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/AGENTS.md)). `session_start.py` injects LACP identity, git context, test-command detection, focus brief, handoff artifacts, health snapshots, SMS memory, and context-mode instructions within a token budget ([hooks/session_start.py](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/hooks/session_start.py)). `pretool_guard.py` blocks command classes such as publish, pipe-to-interpreter, `git reset --hard`, `git clean -f`, privileged Docker, `rm -rf`, protected writes, selected exfiltration patterns, and public-repo push-to-main ([hooks/pretool_guard.py](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/hooks/pretool_guard.py)). These hooks are explicit system-definition artifacts: their authority is enforcement or instruction in the agent runtime, not advice.

**Stop gates convert session evidence into both blocking decisions and memory.** `stop_quality_gate.py` extracts the last assistant message and transcript path, checks for loop/circuit breakers, detects rationalization patterns, optionally verifies test-passing claims against an allowlisted test command, writes handoff artifacts, logs telemetry, records Self-Memory System episodes, and updates the self-model ([hooks/stop_quality_gate.py](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/hooks/stop_quality_gate.py)). The gate itself is a system-definition artifact because it can block stop. The handoff and SMS outputs are derived retained artifacts: handoffs advise future continuation, while the self-model can be injected at future session start and therefore gains instruction-like behavioral authority.

**The memory stack is file-first but multi-root.** LACP's advertised five-layer memory stack spans Claude project memory, an Obsidian vault, ingestion pipelines, GitNexus code intelligence, and persistent agent identity/provenance ([README](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/README.md)). The SMS module stores episodes, epochs, narrative, and self-model JSONL/JSON under `$LACP_SMS_ROOT` and builds a session-start memory block from the focus file, self-model, narrative, and recent significant episodes ([hooks/self_memory_system.py](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/hooks/self_memory_system.py)). Obsidian ingestion writes inbox notes with frontmatter fields such as `source_urls`, `source_sessions`, `confidence`, `last_verified`, and typed relation scaffolds ([bin/lacp-brain-ingest](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-brain-ingest)).

**Brain automation is an operations pipeline, not a single retriever.** `lacp-brain-expand` guards Obsidian config, promotes pending per-turn memory signals to inbox notes, syncs Claude/Codex sessions, materializes web research, syncs research/repo/agent-daily knowledge, runs consolidation/gap/wiki/review-queue steps, archives inbox notes, refreshes QMD, runs doctors, enforces memory index caps, and synthesizes SMS epochs ([bin/lacp-brain-expand](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-brain-expand)). Storage substrate is therefore split: raw session history, staging JSONL, Obsidian markdown, QMD indexes, workflow logs, and SMS JSON each have different lineage and authority.

**Receipts, manifests, and provenance are first-class operational artifacts.** `lacp-provenance` maintains a SHA-256 hash-chained session receipt log with agent ID, session fingerprint, project slug, memory hash, previous hash, and receipt hash ([bin/lacp-provenance](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-provenance)). `lacp-harness-run` executes dependency-ordered tasks through `lacp-sandbox-run`, validates expected inputs/outputs, runs verification checks, writes per-attempt hash-chained receipts, produces summaries and remediation plans, and can be replayed from receipts ([bin/lacp-harness-run](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-harness-run), [bin/lacp-harness-replay](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-harness-replay)). Browser/API/contract evidence manifests are similarly validated for freshness, entrypoint kind, artifacts, and assertions ([bin/lacp-e2e](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-e2e), [bin/lacp-browser-evidence-validate](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-browser-evidence-validate)).

**Doctors and KPIs make local operations measurable.** `lacp-doctor` checks commands, optional services, roots, recent artifacts, limits, Obsidian/brain health, and fix hints ([bin/lacp-doctor](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-doctor)). `lacp-report` summarizes recent sandbox receipts into success/block/intervention metrics and latest benchmark/snapshot pointers ([bin/lacp-report](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-report)). `lacp-memory-kpi` scans the Obsidian vault for canonical-note coverage, schema coverage, source backing, contradiction notes, and stale notes ([bin/lacp-memory-kpi](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-memory-kpi)). These surfaces mostly evaluate and advise; they become enforcement only where another command treats them as a gate.

## Comparison with Our System

| Dimension | LACP | Commonplace |
|---|---|---|
| Primary aim | Local agent operations control plane | Agent-operated knowledge-base methodology |
| Primary substrate | Shell/Python commands plus local JSON, JSONL, markdown, Obsidian, and receipts | Git-tracked typed Markdown collections plus generated indexes/reviews |
| Behavior shaping | CLI routing, policy gates, Claude hooks, context modes, contracts, stop gates | AGENTS.md, collection/type specs, skills, validation, semantic review, generated navigation |
| Memory creation | Hook-derived SMS episodes, per-turn staging, session sync, Obsidian ingest/expand, manual commands | Authored notes, source ingest, connect/revise workflows, review gates |
| Raw traces | Sandbox-run JSON, hook telemetry, transcripts, workflow logs, harness receipts | Git history, validation/review outputs, source snapshots, work artifacts |
| Derived artifacts | Handoffs, SMS self-model, inbox/graph notes, wiki compilations, review queues, reports | Notes, ADRs, indexes, review notes, connect reports, validation outputs |
| Lineage | Hash chains, timestamps, run dirs, manifest freshness, source URL/session fields | Frontmatter, source links, generated indexes, git history, type contracts, review lifecycle |
| Evaluation | Doctors, KPIs, stop quality gate, harness verification, evidence manifest validation | `commonplace-validate`, semantic review bundles, collection conventions |

LACP is strongest where commonplace is intentionally thinner: runtime governance around live agent execution. It has concrete pretool blockers, stop gates, route decisions, TTL approvals, budget ceilings, context contracts, session fingerprints, and replayable harness receipts. Commonplace has stronger library semantics: typed notes, link vocabulary, collection register, review workflows, and durable explanatory artifacts.

The closest alignment is the source/derived split. LACP keeps many raw operational traces as JSON/JSONL/logs, then derives reports, handoffs, SMS summaries, Obsidian notes, QMD indexes, and remediation plans. Commonplace has the same architectural instinct but uses typed markdown as the main durable substrate and generated indexes as transparent derived views.

The biggest divergence is authority. LACP often uses local commands as enforcement surfaces: a hook blocks, a route denies, a manifest fails, a harness task is blocked, a budget gate refuses execution. Commonplace mostly shapes behavior through instructions, type contracts, validation, and review, with fewer hard runtime gates.

## Borrowable Ideas

**Treat run receipts as a first-class artifact family.** LACP's sandbox and harness receipts are ready to borrow conceptually: capture command, route, contracts, exit code, verification, and lineage in one durable JSON object. Commonplace could use a similar receipt for review bundles or validation sweeps where provenance matters more than prose.

**Use session fingerprints for mutating work.** LACP's context-contract and session-fingerprint gates are a practical answer to "am I operating in the intended host/cwd/branch/worktree?" This is immediately relevant to commonplace commands that mutate many notes or generated indexes.

**Make stop gates write handoff artifacts.** The stop hook's handoff generation is a good workshop-layer mechanism. Commonplace already values workshop artifacts; a lightweight, typed handoff generated at context pressure or session end would fit without changing library notes.

**Separate audit traces from promoted memory.** LACP is useful precisely because many traces remain receipts/logs while only selected signals become SMS, inbox notes, wiki pages, or self-model entries. Commonplace should preserve the same discipline if it adds trace-derived capture: raw traces are evidence, not automatically knowledge.

**Add aggregate operational KPIs cautiously.** `lacp-memory-kpi` and `lacp-report` show small metrics that help operators notice drift. Commonplace could adopt analogous aggregate views for source-backed coverage, stale notes, validation warning trends, or review intervention rates, but only if they remain pointers to inspectable artifacts rather than scoreboard theater.

**Package context modes as named behavior contracts.** LACP's context-mode files are a useful middle layer between ambient AGENTS instructions and task-specific prompts. Commonplace skills already do this for procedures; a small mode concept could help with review, connect, revise, or ingest sessions when the same behavioral stance repeats.

## Trace-derived learning placement

LACP qualifies as trace-derived learning at this commit, but the qualification is specific. Raw traces and receipts are not themselves the learning mechanism. The qualifying loop is that session traces, hook observations, per-turn staging signals, and operational outcomes can be transformed into retained artifacts that future sessions consume through hooks, Obsidian memory, SMS context, reports, or gates.

**Trace source.** Source traces include Claude transcript paths passed to hooks, sandbox-run receipts under `$LACP_KNOWLEDGE_ROOT/data/sandbox-runs`, hook telemetry, staged per-turn memory JSONL, harness attempt receipts, browser/API/contract manifests, Obsidian Agent Daily notes, and local workflow logs. The stop hook explicitly reads transcript-derived file changes and assistant messages; brain-expand syncs sessions and promotes staged memory signals ([hooks/stop_quality_gate.py](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/hooks/stop_quality_gate.py), [bin/lacp-brain-expand](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-brain-expand)).

**Extraction.** Extraction is mostly deterministic plus heuristic, not model-trained. The stop hook extracts session summaries, files touched, test-failure state, and significance markers; SMS computes significance from content markers and context signals; brain-expand converts staging JSONL into inbox markdown and runs separate sync/consolidation/wiki/review-queue scripts ([hooks/self_memory_system.py](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/hooks/self_memory_system.py), [bin/lacp-brain-expand](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-brain-expand)). The oracle is therefore a mixture of hook rules, script schemas, thresholds, and later human/operator review, not a single learned judge.

**Storage substrate.** Raw operational receipts live in JSON/JSONL under `$LACP_KNOWLEDGE_ROOT`, provenance lives under `~/.lacp/provenance`, SMS lives under `~/.lacp/sms`, handoffs live under `~/.lacp/handoffs`, and promoted knowledge lives as Obsidian markdown notes with frontmatter and generated indexes. Runtime configuration lives in repo files under `config/`, `hooks/`, `plugin/`, and `bin/`.

**Representational form.** The raw traces are symbolic JSON plus log text. Derived memory is mixed: SMS episodes and self-models are JSON/JSONL with prose summaries and symbolic scores; Obsidian notes are prose plus frontmatter and relation scaffolds; route policies, contracts, schemas, and hook code are symbolic system-definition artifacts. There is no distributed-parametric learning in the reviewed code.

**Lineage.** LACP's lineage story is stronger for operational receipts than for promoted knowledge. Sandbox receipts record route decisions, contracts, timestamps, commands, and run files. Harness receipts are hash-chained per attempt. Provenance receipts are hash-chained across sessions and include memory hashes. Obsidian notes include source URLs and source sessions for ingest. The weaker point is that some brain-expand transformations call many scripts whose internal provenance quality varies; the top-level workflow records step status and log path but not always a complete derivation graph.

**Behavioral authority.** Raw traces, run receipts, logs, and reports are knowledge artifacts when used as audit evidence. Route policies, sandbox gates, hook code, context modes, contract schemas, stop gates, and manifest validators are system-definition artifacts because they route, block, validate, instruct, or enforce. SMS episodes are knowledge artifacts when merely listed; the self-model and selected SMS context become behavior-shaping system-definition artifacts when `session_start.py` injects them into the next agent session.

**Scope and timing.** The scope is local-machine and project/workspace oriented. Extraction happens online at stop hooks and during scheduled or manual brain-expand cycles. Harness and sandbox receipts are per-run; SMS and Obsidian memory are cross-session; provenance is cross-session continuity.

**Survey placement.** LACP strengthens the survey's "operations-derived memory" side: it shows a control plane where traces first serve audit/governance, then selected traces are promoted into behavior-shaping memory. It splits simple trace-derived labels into at least three surfaces: raw audit traces, derived knowledge artifacts, and enforced system-definition artifacts.

## Curiosity Pass

**The README's "5-layer memory" is real but heterogeneous.** It bundles session memory, Obsidian graph, ingestion, code intelligence, and identity/provenance. That is an accurate operations stack, but not one uniform memory model. A reader should not expect a single retrieval API or single canonical store.

**The strongest behavior is in gates, not retrieval.** LACP has many memory commands, but its clearest behavior-shaping mechanisms are route decisions, pretool blocks, stop gates, context modes, and harness validators. Memory improves future action partly by being injected, but governance improves action by refusing unsafe or under-evidenced work.

**Some "sandbox" paths fall back to direct execution.** `lacp-sandbox-run` can execute `local_sandbox` directly when `LACP_LOCAL_SANDBOX_RUNNER` is unset, while logging a warning ([bin/lacp-sandbox-run](https://github.com/0xNyk/lacp/blob/7bdd7ab3655cf19876a9f7c95f6584725adc5e72/bin/lacp-sandbox-run)). That is pragmatic for local adoption, but it means the route label and actual isolation level can diverge unless operators inspect receipts.

**The system has many doctors, but doctors are not guarantees.** Diagnostics and KPIs are useful knowledge artifacts. They become enforceable only when another command or operator treats their result as a gate. This distinction matters because LACP's CLI surface can make advisory and blocking outputs look equally official.

**The SMS layer is behaviorally powerful and epistemically thin.** It updates self-model patterns from simple markers such as test failures, blocked work, file counts, and terms like "test first" or "incremental." Because session_start may inject that self-model into future work, the self-model has more authority than its extraction oracle can always justify.

## What to Watch

- Whether `local_sandbox` grows a default real isolation runner, reducing the direct-fallback gap between policy label and execution substrate.
- Whether brain-expand artifacts gain uniform provenance records across every script, not just top-level workflow logs and selected note frontmatter.
- Whether SMS/self-model updates gain review, decay, or confidence gates before injection, since they can shape future agent behavior.
- Whether LACP consolidates its many command/report/doctor surfaces into a smaller typed artifact vocabulary.
- Whether run receipts become inputs to automatic policy changes, promotion rules, or learning loops beyond reporting and triage.

---

Relevant Notes:

- [behavioral authority](../../notes/definitions/behavioral-authority.md) - classifies: LACP's receipts advise, while hooks, policies, contracts, and validators enforce or instruct
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw logs, reports, manifests, receipts, and Obsidian notes when consumed as evidence/context
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: route policy, hook code, context modes, contract schemas, and stop gates
- [lineage](../../notes/definitions/lineage.md) - frames: hash-chained receipts and source-session metadata as invalidation and audit support
- [operative part](../../notes/definitions/operative-part.md) - sharpens: one stored JSON object can contain audit evidence, routing state, and future gating signal
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: LACP's handoffs, receipts, and workflow logs are a heavy workshop layer around agent operations
- [Memory management policy is learnable but oracle dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - explains: LACP's trace-derived memory depends on the quality of hook heuristics, staging rules, and operator review
