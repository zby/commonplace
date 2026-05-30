---
description: "ARIS review: markdown skill-pack for autonomous research with project state files, research wiki, review traces, and hook-log-driven skill optimization"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# ARIS

ARIS, from wanshuiyin's Auto-claude-code-research-in-sleep repository, is a markdown skill-pack and helper toolkit for autonomous ML research workflows. Its memory system is not a standalone database: behavior is shaped by installed `SKILL.md` instructions, project-local stage files, a lightweight research wiki, reviewer traces, hook logs, queue state, watchdog status files, and optional meta-optimization reports that propose changes back into the skill layer.

**Repository:** https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

**Reviewed commit:** [9a7846081ea1616a4ebde320b446ba738e3dd816](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/9a7846081ea1616a4ebde320b446ba738e3dd816)

**Last checked:** 2026-05-16

## Core Ideas

**The primary system-definition artifacts are markdown skills.** ARIS packages research workflows as `SKILL.md` files with trigger descriptions, argument hints, allowed tools, constants, and procedural phases. The agent-facing guide frames the repo as a "research harness" whose source of truth is each skill file, while the installer symlinks skills into project-local `.claude/skills/` or `.agents/skills/` directories and records managed entries in `.aris/installed-skills*.txt` manifests ([AGENT_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/AGENT_GUIDE.md), [skills/research-pipeline/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/research-pipeline/SKILL.md), [tools/install_aris.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/install_aris.sh), [tools/install_aris_codex.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/install_aris_codex.sh)). Storage substrate is filesystem symlinks and markdown; representational form is prose instructions plus symbolic frontmatter and shell blocks; behavioral authority is high because installed skills instruct the acting agent.

**Project state is split into stage-specific markdown and JSON files.** The project files guide defines `CLAUDE.md` Pipeline Status, `idea-stage/`, `refine-logs/`, `review-stage/`, `paper/`, `research-wiki/`, `findings.md`, `MANIFEST.md`, and recovery-state JSON files as the durable surfaces that survive compaction and new sessions. The session recovery guide makes `CLAUDE.md` plus `idea-stage/docs/research_contract.md` the first recovery reads, while `auto-review-loop` persists `review-stage/REVIEW_STATE.json` and `review-stage/AUTO_REVIEW.md` after each round ([docs/PROJECT_FILES_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/docs/PROJECT_FILES_GUIDE.md), [docs/SESSION_RECOVERY_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/docs/SESSION_RECOVERY_GUIDE.md), [templates/CLAUDE_MD_TEMPLATE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/templates/CLAUDE_MD_TEMPLATE.md), [skills/auto-review-loop/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/auto-review-loop/SKILL.md)). These artifacts are knowledge artifacts when read as evidence of project state, and system-definition artifacts when skills require future agents to resume from them.

**The research wiki is a small file-backed KB with a compiled query surface.** `/research-wiki` creates `research-wiki/{papers,ideas,experiments,claims,graph}/`, stores typed pages as markdown, stores relationships in `graph/edges.jsonl`, and regenerates `index.md` plus an 8000-character `query_pack.md` for idea generation. The helper code implements slug generation, arXiv metadata fetch, edge insertion, stats, and deterministic query-pack rebuilding; tests cover the helper resolution chain because downstream projects often have only `.aris/tools` rather than a copied `tools/` directory ([skills/research-wiki/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/research-wiki/SKILL.md), [tools/research_wiki.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/research_wiki.py), [tests/test_research_wiki_helper_resolution.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tests/test_research_wiki_helper_resolution.py)). The canonical knowledge artifacts are markdown pages and JSONL edges; `query_pack.md` is a derived view with prompt-time activation authority.

**Cross-model review is treated as an audit trail, not just a chat turn.** `auto-review-loop` sends research context to an external reviewer, parses score/verdict/action items, implements fixes, and repeats until a threshold or round cap. Hard and nightmare modes add `REVIEWER_MEMORY.md`, debate, and direct repo-reading by Codex. Separately, the review tracing protocol requires every reviewer MCP call to be saved under `.aris/traces/<skill>/<date>_runNN/` with request, response, and metadata files; `save_trace.sh` implements this and appends compact events to `.aris/meta/events.jsonl` when available ([skills/auto-review-loop/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/auto-review-loop/SKILL.md), [skills/shared-references/review-tracing.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/shared-references/review-tracing.md), [tools/save_trace.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/save_trace.sh)). Raw traces have evidence authority; reviewer memory and parsed action items gain system-definition authority inside later review rounds.

**The execution layer keeps operational state in simple files.** The experiment queue skill uses a manifest plus remote `queue_state.json`, per-job logs, and `run_meta.txt` to launch, monitor, retry, and resume large experiment batches. The Python scheduler writes job status atomically and detects OOM/stale-screen conditions. The watchdog daemon uses `tasks.json`, per-task status JSON, `alerts.log`, and `summary.txt` to preserve remote task health across low-frequency polling and session recovery ([skills/experiment-queue/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/experiment-queue/SKILL.md), [skills/experiment-queue/scripts/queue_manager.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/experiment-queue/scripts/queue_manager.py), [tools/watchdog.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/watchdog.py), [docs/WATCHDOG_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/docs/WATCHDOG_GUIDE.md)). This is not semantic memory, but it is retained state that changes future agent action by preventing lost jobs, repeated checks, and stale assumptions.

**Meta-optimization closes a cautious trace-to-skill loop.** `tools/meta_opt/log_event.sh` records Claude Code hook payloads into project and global `.aris/meta/events.jsonl`, classifying skill invocations, tool failures, Codex calls, slash commands, prompts, session starts, and session ends. `/meta-optimize` reads those logs, identifies usage/failure/convergence patterns, proposes minimal diffs to skill prompts or defaults, reviewer-gates the patch, and only applies changes after explicit user approval ([tools/meta_opt/log_event.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/meta_opt/log_event.sh), [tools/meta_opt/check_ready.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/tools/meta_opt/check_ready.sh), [skills/meta-optimize/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9a7846081ea1616a4ebde320b446ba738e3dd816/skills/meta-optimize/SKILL.md)). This is the clearest trace-derived learning mechanism: raw tool/session traces can become proposed edits to system-definition artifacts.

## Comparison with Our System

| Dimension | ARIS | Commonplace |
|---|---|---|
| Primary substrate | Markdown skills, project markdown/JSON files, `.aris/` manifests, logs, traces, helper scripts | Git-tracked markdown notes, sources, instructions, ADRs, type specs, generated indexes/reports |
| Main behavior-shaping artifact | Installed `SKILL.md` workflow instructions and project recovery files | Typed notes plus stronger instructions, validators, commands, and review artifacts |
| Knowledge substrate | Research wiki pages, JSONL edges, query pack, findings and experiment logs | Collections with frontmatter contracts, authored links, indexes, validation, review state |
| Trace-derived path | Hooks/reviewer traces -> meta-optimize report -> proposed skill diffs -> user-approved skill edits | Mostly review reports and human-mediated promotion; no general hook-log-to-instruction loop yet |
| Activation | Slash-command skill discovery, Pipeline Status recovery, `query_pack.md`, review state, queue/watchdog status | `rg`, indexes, descriptions, authored links, skills, validation and review commands |
| Lineage | Strong for some operational artifacts, weaker for wiki pages and compact state summaries unless the writing skill preserves evidence | Source snapshots, commit-pinned reviews, link contracts, archive/replacement status, validation outputs |
| Governance | Reviewer gates, human checkpoints, installer manifests, tests for helper resolution, user approval for meta patches | Type specs, schema validation, deterministic validation, semantic review gates, git history |

ARIS and commonplace converge on a filesystem-first belief: agents can operate better when the important state is inspectable files rather than opaque chat history. Both systems use markdown as a behavior-shaping medium, both keep generated indexes or compact views as derived activation surfaces, and both depend on local scripts to keep the convention layer from drifting.

The important difference is the unit of work. ARIS is a workflow harness for one research project at a time. Its artifacts are stage files that help an agent keep moving through idea discovery, implementation, experiments, review, and paper writing. Commonplace is a library-oriented KB methodology: its artifacts are intended to accumulate transferable knowledge and system documentation over time.

ARIS is stronger as an operational workshop. It has concrete queues, watchdogs, review loops, trace capture, notifications, and recovery protocols for long-running work. Commonplace has stronger artifact contracts and curation semantics: collection-local types, link vocabulary, status, validation, and review lifecycle are more explicit than ARIS's project file conventions.

The retained-artifact vocabulary helps avoid overclaiming ARIS. A `SKILL.md` file is a system-definition artifact with prose and symbolic operative parts. A research-wiki paper page is usually a knowledge artifact. `query_pack.md` is a derived knowledge artifact with prompt-time activation authority. `.aris/meta/events.jsonl` is raw trace evidence. A meta-optimize patch proposal is advice until accepted; once applied to a skill, it becomes a revised system-definition artifact.

**Read-back:** push — slash-command workflows and recovery protocols load skills, project state, and compiled query packs into context.

## Trace-derived learning placement

**Trace source.** ARIS qualifies as trace-derived learning. The strongest implemented source trace is `.aris/meta/events.jsonl`, produced from Claude Code hook payloads by `tools/meta_opt/log_event.sh`. It records skill invocations, tool failures, Codex reviewer calls, slash commands, user prompts, and session boundaries. Review tracing adds richer prompt/response traces under `.aris/traces/`, while workflow logs such as `AUTO_REVIEW.md`, `EXPERIMENT_LOG.md`, `findings.md`, `queue_state.json`, and watchdog status files preserve task-specific traces.

**Extraction.** Extraction is staged and mostly LLM-mediated. `/meta-optimize` reads event logs, computes usage, failure, convergence, and human-intervention patterns, then proposes diffs to skill prompts, defaults, convergence rules, workflow ordering, or cautious schema changes. The oracle is not the same acting agent alone: proposed patches are sent to a separate reviewer model and require user approval before application. Other workflow skills extract more local knowledge, such as experiment findings, claim verdicts, reviewer memory, and wiki edges, but the meta-optimize path is the trace-to-system-definition loop.

**Storage substrate.** Raw traces live in project-local files: `.aris/meta/events.jsonl`, `.aris/traces/`, review logs, experiment logs, queue state, watchdog status, and manifest files. Distilled or candidate outputs live as markdown reports, JSON state files, and proposed diffs. Accepted changes land back in `SKILL.md` files, which are then installed into `.claude/skills/` or `.agents/skills/`.

**Representational form.** Raw traces are symbolic JSONL plus prose prompt/response bodies. Distilled reports and skill patches are mixed prose and symbolic diff/code forms. The operative learned artifact, after approval, is prose instruction and shell/code snippets inside markdown skills. There is no learned model weight or embedding-based trace learner in the inspected meta-optimize path.

**Lineage.** The lineage is hook payload -> event record -> meta-optimize analysis -> proposed patch -> reviewer assessment -> user-approved skill edit. Review traces preserve fuller call lineage than the compact event log. The weakness is that accepted skill edits depend on disciplined reporting and backups rather than a built-in provenance field inside each changed `SKILL.md`.

**Behavioral authority.** Raw traces are knowledge artifacts: evidence about prior agent behavior. Meta-optimize reports are advisory knowledge artifacts until accepted. Applied patches to `SKILL.md` files become system-definition artifacts with instruction/configuration authority over future agents. Reviewer traces also feed audit authority, while `REVIEWER_MEMORY.md` can gain prompt-time system-definition authority over later reviewer rounds.

**Scope.** Scope is project-local for most traces, with a global `~/.aris/meta/events.jsonl` for cross-project trends. The learned behavior is harness-level, not domain-fact-level: it changes how ARIS skills run, when they stop, what they log, or how they route review.

**Timing.** Logging is online during normal usage. Optimization is offline and manually triggered or suggested by `check_ready.sh` after enough skill invocations. Application is explicitly user-approved.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), ARIS is a trace-to-instruction/artifact-learning system. It strengthens the survey's distinction between raw traces and distilled system-definition artifacts: the event log does not itself improve behavior until an approved patch changes a skill or a project state artifact is loaded by a later workflow.

## Borrowable Ideas

**Stage files with explicit recovery priority.** Ready to borrow for commonplace workshops. ARIS distinguishes dashboard state, active contract, tracker, full experiment log, findings log, review state, and manifest, then documents which files a fresh agent should read first. The commonplace analogue is not ML-specific stage names, but a stronger workshop recovery contract.

**Trace capture with promotion gates.** Ready as a governance pattern. ARIS logs hook events and reviewer traces, but the meta-optimize path turns them into proposed patches that require reviewer assessment and user approval before changing skills. That is the right authority gradient for moving from raw traces to system-definition artifacts.

**Hard-budgeted compiled context.** Ready for generated views. `query_pack.md` is regenerated from wiki state and capped for prompt loading, making it closer to an agent-facing compiled context than a human index. Commonplace can apply the same idea to review queues or workshop state.

**Operational memory as first-class memory.** Ready as a framing. Queue state, watchdog status, installer manifests, and recovery JSON are not semantic notes, but they prevent future agents from losing work or repeating checks. Commonplace should continue treating retained operational state as part of context engineering when it changes future action.

**Do not borrow the wiki schema wholesale.** The ARIS research wiki is useful for a project harness, but its pages and edges are thinner than commonplace's typed artifacts. It needs stronger provenance, status, validation, and link semantics before becoming a library-layer model.

## Takeaways

**Borrow the stage-file discipline for workshops.** ARIS is clearest where it treats long-running research as a set of durable stage files with different audiences: dashboard, active contract, tracker, full log, findings, review state, and manifest. Commonplace's workshop layer could use the same explicit recovery priority without importing the research-specific workflow.

**Borrow trace capture only with a promotion gate.** The meta-optimize loop is useful because it does not let hook logs rewrite the harness directly. It turns traces into proposals, reviewer-gates them, and requires approval before changing skills. That matches commonplace's preference for reviewable promotion from raw evidence to stronger authority.

**Treat compiled context as a first-class derived view.** `query_pack.md` is simple, hard-budgeted, and regenerated from wiki state. Commonplace already has generated indexes; ARIS is a useful reminder that some generated views should be optimized for agent context loading rather than human browsing.

**Do not borrow ARIS's loose wiki schema as-is.** The research wiki is practical, but its page schemas and edges are much thinner than commonplace's type/link system. It is enough for research-project continuity, not enough for a long-lived methodology KB without stronger status, source, validation, and link semantics.

**Operational memory matters.** Queue state, watchdog summaries, installer manifests, and recovery JSON are not "knowledge" in the narrow semantic sense, but they materially prevent future agent mistakes. Commonplace should keep treating retained operational state as part of the memory design surface when it changes future action.

## Curiosity Pass

The repository is mostly promptware, but the promptware is not inert documentation. Installed skills have real system-definition authority because Claude Code and Codex discover and execute them as slash-command workflows. That makes ARIS a useful counterexample to treating "implementation" as only Python or TypeScript code.

The research wiki is less central than the README framing might imply. It exists and has a real helper, but most of the durable behavior-changing state in ARIS is in workflow files, review logs, project dashboards, traces, queues, and skills rather than in the wiki itself.

The meta-optimize loop is intentionally conservative. It is trace-derived, but not autonomously self-modifying: hook data produces proposed skill edits, and those edits still require review and user approval. That makes it weaker as automatic learning and stronger as inspectable governance.

The Codex and Claude skill variants are a maintenance risk. The installers and tests help, but parallel skill trees and overlay packages can drift in subtle behavior-shaping ways if updates are not mirrored carefully.

## Open Questions

- Does ARIS's hook-log meta-optimization work on enough real runs to produce patches that survive beyond anecdotal improvements?
- Will accepted meta-optimize patches carry durable provenance inside the changed skill files, or only in external reports/backups?
- Can the research wiki grow without stronger deduplication, stale-claim handling, source citations, and relationship validation?
- Will project-local trace files become too sensitive or bulky for routine retention, especially full reviewer prompt/response traces?
- Can ARIS's cross-model review protocol distinguish failures in idea quality, experiment implementation, reviewer judgment, and skill instructions, or do those signals collapse into generic "fix the workflow" patches?
- Will the Codex/Claude/Gemini skill variants stay behaviorally equivalent as the base skill pack evolves?

## What to Watch

- Whether `/meta-optimize` gains examples of accepted patches with durable provenance back to event logs and reviewer traces.
- Whether `research-wiki/` becomes a stronger typed project KB or remains a compact sidecar for idea generation.
- Whether review traces stay local/private by default as users run ARIS on sensitive unpublished work.
- Whether queue and watchdog state become integrated into `/monitor-experiment` rather than remaining adjacent status files.
- Whether the skill installers and mirror tests are enough to keep Claude, Codex, and Gemini skill packs behaviorally aligned.

## Bottom Line

ARIS is best understood as an agent-operated research workshop, not a general knowledge library. Its strongest memory ideas are durable project-state files, compiled wiki context, forensic review traces, and a cautious trace-to-skill optimization loop. It is less mature than commonplace on artifact contracts, lineage, and long-term curation, but stronger as a practical harness for keeping autonomous research work alive across sessions, reviewers, experiments, and overnight execution.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: ARIS turns hook and reviewer traces into proposed skill edits, with reviewer and user gates before system-definition authority changes.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - exemplifies: ARIS is mostly a workshop-state system, with stage files optimized for active work rather than accumulated theory.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: ARIS requires separating skill files, wiki pages, query packs, event logs, review traces, and queue state by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: ARIS makes activation explicit through slash-command skills, Pipeline Status recovery, and `query_pack.md`.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - qualifies: ARIS logs deploy-time usage but makes harness learning staged and approval-gated rather than fully online.
