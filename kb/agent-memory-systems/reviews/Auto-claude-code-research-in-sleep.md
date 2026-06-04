---
description: "ARIS review: Markdown skill harness for autonomous research with project research-wiki memory, review traces, and gated trace-derived skill optimization"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Auto-claude-code-research-in-sleep

Auto-claude-code-research-in-sleep, also called ARIS, is a research workflow harness built around Markdown skill packages, helper scripts, MCP reviewer bridges, and project-local artifacts. It is not primarily a memory database. Its memory behavior comes from the skill corpus that instructs future agents, the optional `research-wiki/` project knowledge base, reviewer/run traces under `.aris/`, and a meta-optimization loop that reads usage traces to propose changes to the skill corpus.

**Repository:** https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

**Reviewed commit:** [f0dde3eee942e6630f2f62d78daafcd8c52ed033](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/f0dde3eee942e6630f2f62d78daafcd8c52ed033)

**Last checked:** 2026-06-04

## Core Ideas

**The main retained unit is a portable Markdown skill.** ARIS distributes workflows as `skills/<name>/SKILL.md` files, with mirrors for Codex and overlays for alternate reviewer backends. The agent guide says behavior lives in each `SKILL.md`, while installers symlink those packages into host-specific skill roots and record managed manifests in `.aris/installed-skills*.txt` ([AGENT_GUIDE.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/AGENT_GUIDE.md), [tools/install_aris.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/install_aris.sh), [tools/install_aris_codex.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/install_aris_codex.sh), [skills/](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills)).

**Research memory is project-local and file-based.** The `/research-wiki` skill creates a `research-wiki/` tree with paper, idea, experiment, claim, graph, log, index, gap-map, and query-pack files. The helper implements initialization, paper ingest, edge addition, index rebuilds, query-pack rebuilds, stats, and arXiv sync in a single stdlib Python script ([skills/research-wiki/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/research-wiki/SKILL.md), [tools/research_wiki.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/research_wiki.py)).

**Context efficiency is mostly compressed-file read-back, not learned retrieval.** The wiki helper builds `query_pack.md` from project direction, open gaps, failed ideas, key papers, and recent graph edges, capped at a default 8000 characters. `/idea-creator` loads that pack when present and still runs fresh literature search for recent work. This bounds volume more than loading the whole wiki, but it is a coarse pack rather than top-k semantic retrieval ([tools/research_wiki.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/research_wiki.py), [skills/idea-creator/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/idea-creator/SKILL.md)).

**Cross-model review is the governing pattern.** Several skills require a reviewer from a different model family, save review traces, and distinguish executor completion from acceptance. `run_state.py` makes this explicit by separating `done` from `accepted`, and `meta-apply` refuses producer-written verdicts in favor of a fresh cross-model jury at landing time ([tools/run_state.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/run_state.py), [skills/shared-references/review-tracing.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/shared-references/review-tracing.md), [skills/meta-apply/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/meta-apply/SKILL.md)).

**Trace-derived self-improvement is proposed, staged, and gated.** Hook logging appends skill, prompt, tool, session, and reviewer-call events to project and global `.aris/meta/events.jsonl` logs. `/meta-optimize` reads those logs to propose SKILL.md/default/workflow patches, and `/meta-apply` is the privileged human-invoked landing gate ([tools/meta_opt/log_event.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/meta_opt/log_event.sh), [tools/meta_opt/check_ready.sh](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/meta_opt/check_ready.sh), [skills/meta-optimize/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/meta-optimize/SKILL.md), [skills/meta-apply/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/meta-apply/SKILL.md)).

**Safety is implemented as cheap deterministic screens plus review gates.** Wiki edge evidence and query packs are scanned or quarantined for injection patterns; capture filtering rejects transient operational noise before it hardens into durable research memory; evidence pre-checks mechanically verify cited values before Codex judges claim support ([tools/threat_scan.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/threat_scan.py), [tools/capture_filter.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/tools/capture_filter.py), [skills/result-to-claim/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/skills/result-to-claim/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `files` — ARIS stores its behavior-shaping state in repository files, symlinked skill directories, project-local `.aris/` artifacts, and optional `research-wiki/` files; MCP bridges may keep transient process state, but the central retained surfaces are filesystem artifacts.
- **Representational form:** `prose` `symbolic` — SKILL.md instructions, reviewer prompts, wiki pages, reports, and query packs are prose; manifests, JSONL edges/events/traces, run-state JSON, helper scripts, installers, tests, and MCP server code are symbolic.
- **Lineage:** `authored` `imported` `trace-extracted` — Maintainers author the skill corpus and helper contracts, wiki ingest imports external paper metadata and user-declared claims, and meta-optimization/review-tracing derives retained artifacts from session, tool, and reviewer traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Wiki artifacts inform future research; skills instruct agents; installers, run state, evidence checks, and threat scans enforce or validate; reviewer routing and helper resolution route work; idea ranking and review scoring influence choices; meta-optimization learns proposed harness changes.

**Skill packages and shared references.** Storage substrate: the `skills/` tree and host-specific installed symlinks. Representational form: prose instructions plus symbolic frontmatter, allowed-tool declarations, resolver blocks, shell snippets, and helper paths. Lineage: authored and versioned in the repository, then installed into project-local skill roots. Behavioral authority: system-definition artifacts; when invoked as slash commands, they instruct future agents, route model calls, define artifact contracts, and sometimes require validation gates.

**Research wiki.** Storage substrate: a project `research-wiki/` directory containing Markdown entity pages, `graph/edges.jsonl`, `index.md`, `log.md`, `gap_map.md`, and `query_pack.md`. Representational form: prose pages with symbolic frontmatter and JSONL graph edges. Lineage: imported paper metadata, user/agent-authored idea and claim notes, experiment outcomes, and generated indexes/query packs. Behavioral authority: mostly knowledge and ranking; the query pack influences later idea generation, failed ideas become anti-repetition memory, and claim status can steer paper-writing or follow-up experiments.

**Review and run traces.** Storage substrate: `.aris/traces/<skill>/<date>_runNN/`, `.aris/meta/events.jsonl`, and `.aris/runs/<run_id>.json`. Representational form: symbolic JSON and JSONL plus full prose prompts/responses. Lineage: trace-extracted from reviewer MCP calls, Claude hook events, and workflow phase transitions. Behavioral authority: knowledge and validation evidence during audit/replay, plus learning input for meta-optimization. Run state has stronger validation authority because resume skips only phases that are accepted or skipped, not merely executor-marked done.

**Meta-optimization patches.** Storage substrate: `.aris/meta/` logs, reports, pending patch files, manifests, backups, provenance sidecars, and optimization logs. Representational form: prose reports plus symbolic diffs, JSONL manifests, and provenance hashes. Lineage: trace-extracted proposals from usage logs, then human-selected and cross-model-reviewed before landing. Behavioral authority: learning and instruction after promotion; before `/meta-apply`, a proposal is only advisory evidence.

**Helper scripts and deterministic gates.** Storage substrate: `tools/` and installed `.aris/tools` links. Representational form: symbolic shell/Python with some embedded prose diagnostics. Lineage: authored repository utilities. Behavioral authority: enforcement, validation, and routing: examples include installer safety rules, helper resolution, capture filtering, threat scanning, evidence pre-checks, run-state acceptance rules, and trace saving.

**Promotion path.** ARIS has several promotions, all file-mediated. Literature or experiment material can move into wiki pages, then into query-pack context. Session traces can move into meta-optimization reports, then staged diffs, then landed skill changes through `/meta-apply`. Executor work can move from `done` to `accepted` only with a recorded reviewer or deterministic verifier. The design pattern is "drive automatically, acquit separately."

## Comparison with Our System

| Dimension | ARIS | Commonplace |
|---|---|---|
| Primary purpose | Autonomous research workflows and cross-model review | Agent-operated KB methodology and reviewable knowledge artifacts |
| Main substrate | Plain files: skills, wiki pages, JSONL traces, helper scripts | Plain files: notes, sources, reviews, indexes, schemas, instructions |
| Main retained unit | SKILL.md workflow package plus project artifacts | Typed Markdown artifact under collection/type contracts |
| Memory read-back | Query-pack loading, skill invocation, trace/meta reminders, explicit wiki commands | Search, links, indexes, skills, validation/review workflows |
| Trace-derived learning | Usage logs and reviewer traces propose harness patches | Review reports and work logs can inform authored KB artifacts, but less automated |
| Governance | Cross-model jury, helper gates, installers, provenance, run state | Schema validation, collection contracts, source-grounded review, generated indexes |

ARIS and Commonplace share the file-first adoption story: a user can inspect, diff, copy, and patch the retained artifacts without adopting a service. They diverge in the unit of authority. Commonplace uses typed knowledge artifacts as the durable substrate and lets instructions/validators govern how agents consume them. ARIS starts from executable workflow instructions: the skill package is the thing that tells future agents what to do, while the wiki and traces feed those workflows.

The strongest design overlap is review discipline. Both systems distrust context presence as proof of correctness. ARIS makes this operational with cross-model reviewer roles, trace files, run-state acceptance, and a separate meta-apply landing gate. Commonplace's review bundles and validation are more KB-native; ARIS's gates are workflow-native.

The main tradeoff is semantic locality. ARIS's skill packages are portable and immediately operational, but many relationships live inside long SKILL.md procedures and shell snippets. Commonplace pays more schema and collection overhead so claims, links, status, and lineage are first-class artifacts rather than instructions embedded in a workflow.

### Borrowable Ideas

**Separate executor completion from acceptance.** Ready now. Commonplace already distinguishes validation and review, but `run_state.py`'s `done` versus `accepted` split is a clean reusable pattern for long review workflows.

**Trace every reviewer call as forensic evidence.** Ready now for high-stakes reviews. ARIS's trace directory layout would map well to Commonplace review runs when a later agent must inspect whether the reviewer saw raw evidence or only executor framing.

**Use a compact query pack as a pragmatic read-back layer.** Needs a specific Commonplace workflow. ARIS shows that a generated, bounded pack can be more useful than asking agents to search a whole project at every step, but the pack needs freshness and injection controls.

**Keep self-improvement proposals unprivileged until landing.** Ready as governance vocabulary. The producer/applier split in `/meta-optimize` and `/meta-apply` is a strong pattern for any future Commonplace skill that proposes edits to instructions or validators.

**Do not borrow coarse context packs as the only retrieval mechanism.** ARIS's query pack is useful, but it is not a precise instance-level selector. Commonplace should preserve lexical search, typed indexes, and explicit links rather than flattening everything into one recurring context blob.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents author/edit skills, wiki notes, reports, claims, and experiments; automatic helper paths initialize wiki structures, ingest paper metadata, add graph edges, rebuild indexes/query packs, append trace/event logs, update run state, screen captures, and stage meta-optimization proposals.

**Curation operations:** `consolidate` `synthesize` `invalidate` `promote` — `rebuild_query_pack` consolidates wiki material into a bounded context pack; `/meta-optimize` synthesizes patch proposals from usage logs; `/result-to-claim` can mark claims invalidated and add invalidating edges; `/meta-apply` promotes a staged proposal into the skill corpus only after human invocation and a fresh cross-model jury.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — ARIS logs Claude hook events, slash commands, skill invocations, tool failures, reviewer calls, and full reviewer prompt/response traces.

**Learning scope:** `per-project` `cross-task` — Project-level `.aris/meta/events.jsonl` supports project-specific harness optimization, while the global `~/.aris/meta/events.jsonl` records cross-project trends.

**Learning timing:** `offline` `staged` — Logging happens during normal operation, but `/meta-optimize` analyzes accumulated traces after the fact; landing is staged through pending patches and `/meta-apply`.

**Distilled form:** `prose` `symbolic` — Trace analysis produces prose reports and symbolic diffs/manifests; accepted changes become modified SKILL.md prose, helper contracts, defaults, or workflow rules.

**Trace source.** The trace-derived loop is implemented around `.aris/meta/events.jsonl`, `.aris/traces/`, and hook helpers. `log_event.sh` records hook payloads into project and global JSONL files; `save_trace.sh` writes reviewer request/response artifacts and appends summary events; `check_ready.sh` injects a reminder after enough skill invocations accumulate.

**Extraction.** `/meta-optimize` asks the agent to compute frequency, failure, convergence, and human-intervention patterns from the event log, then generate patch proposals. It explicitly screens rationales with `capture_filter.py` to avoid hardening transient operational failures into durable rules. The cross-model review inside `/meta-optimize` is advisory; `/meta-apply` reruns a fresh landing jury and records provenance before corpus mutation.

**Scope and timing.** Scope is harness behavior, not paper content. The loop is offline and staged: traces accumulate during ordinary runs, a human or reminder triggers analysis, patches are staged under `.aris/meta/pending/`, and a separate human-invoked applier lands only jury-passed survivors.

**Survey position.** ARIS belongs in the trace-to-instruction-artifact family. It strengthens the claim that trace-derived learning is safer when the learner can propose but not acquit its own changes. Its distinctive split is that the trace-derived artifact is initially advisory and only becomes system-definition material after a separate landing gate.

## Read-back

**Read-back:** `both` — ARIS supports explicit pull through `/research-wiki` commands and ordinary skill invocation, while several workflows automatically load retained project state, such as `query_pack.md` into `/idea-creator` and meta-optimization reminders from `.aris/meta/events.jsonl`.

**Read-back signal:** `coarse` — The implemented push paths are broad project/session signals: a `research-wiki/` directory exists, a query pack is stale or fresh, a skill starts, or enough skill invocations have accumulated. I did not find an embedding, lexical, identifier, or judgment-based memory selector in the active wiki read-back path.

**Faithfulness tested:** `no` — The repository tests helper behavior and enforces many gates, but I did not find a WITH/WITHOUT ablation showing that pushed wiki packs, meta reminders, or retained review traces improve future agent decisions.

**Direction.** ARIS has both pull and push read-back for retained memory. Pull is explicit: a user or agent can invoke `/research-wiki query`, rebuild indexes, inspect traces, or read wiki pages. Push appears when a workflow reads project-local retained state before acting, especially `/idea-creator` Phase 0 and the SessionEnd meta-optimize readiness reminder.

**Targeting and signal.** The push is coarse, not instance-targeted. `/idea-creator` loads the same project query pack for the current research direction when the wiki exists; `check_ready.sh` keys on a count of skill invocations since the last meta-optimization. These are useful operational triggers, but not content-specific retrieval over the current user prompt.

**Selection, scope, and complexity.** The main selection budget is `query_pack.md`'s max-character cap. It selects high-level sections by fixed priority: project direction, gaps, failed ideas, paper summaries, and recent relationships. This controls volume, but complexity can still be high because many unrelated wiki facts are compressed into one pack.

**Authority at consumption.** Wiki read-back is advisory context for research ideation and anti-repetition. Skill read-back is stronger because the invoked SKILL.md instructs the agent's workflow. Meta-optimization reminders are advisory, while `/meta-apply` has privileged authority only after explicit user invocation and jury approval.

**Other consumers.** Human researchers consume wiki pages, HTML renders, review reports, traces, and ARIS-Monitor views. Deterministic helpers consume the same retained artifacts as validation inputs. ARIS-Monitor is read-only triage over Claude session registry/transcripts, not a memory-write mechanism ([aris-monitor/scanner.py](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/f0dde3eee942e6630f2f62d78daafcd8c52ed033/aris-monitor/scanner.py)).

## Curiosity Pass

**ARIS is closer to a workflow operating system than a memory engine.** The durable memory pieces matter because skills repeatedly consume them, but most intelligence lives in workflow contracts, model-role separation, and gates.

**The query pack is a deliberately blunt retrieval primitive.** It is cheap, inspectable, and robust across agents, but it cannot express precise relevance. That is a reasonable first layer for research projects where missing a stale failed idea may matter more than perfect top-k recall.

**The strongest memory governance is around self-modification, not the research wiki.** `/meta-apply` is stricter than ordinary wiki update paths: it requires human invocation and a fresh cross-model jury before modifying the corpus. Wiki writes have useful screens, but many page edits remain instruction-level procedures.

**The read-only monitor is adoption infrastructure, not retained knowledge.** ARIS-Monitor helps users manage many Claude sessions and approval prompts, but it intentionally does not write memory or infer long-term state.

**The repository contains far more documented workflow than reusable runtime code.** This is a feature for portability, but it makes code-grounding uneven: some mechanisms are directly implemented in helpers, while others are procedural contracts executed by the host agent.

## What to Watch

- Whether `research-wiki` adds instance-level retrieval beyond the coarse query pack; that would change ARIS from broad project-memory push to targeted memory read-back.
- Whether meta-optimization gains an integrity verifier for landed provenance stamps; the current docs identify content-hash/provenance checks as not fully built.
- Whether wiki claim/idea/experiment page updates move from procedural SKILL.md instructions into helper-enforced schemas; that would strengthen lineage and validation.
- Whether ARIS-Code releases expose the same memory surfaces in a packaged CLI runtime; this checkout mostly shows the skill/harness side plus docs about the CLI.
- Whether WITH/WITHOUT evaluations are added for query-pack loading or meta-optimized skill changes; that would test faithfulness rather than assuming context and patches help.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames why ARIS's stored wiki only becomes memory read-back when workflows load `query_pack.md` or agents query it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies to ARIS's split between skills, wiki pages, traces, helper scripts, and staged patches.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies ARIS's usage-log-to-skill-patch loop.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies SKILL.md packages, helper gates, run-state rules, and meta-apply as behavior-shaping artifacts.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies research-wiki pages, traces, reports, and imported paper metadata before they gain instruction or validation force.
