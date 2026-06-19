---
description: "TheKnowledge review: file-first LLM wiki gateway with citation-grounded Markdown, NotebookLM synthesis, MCP tools, and policy distillation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-05"
---

# TheKnowledge

TheKnowledge, from `badwally/TheKnowledge`, is a personal research knowledge base and gateway for an LLM Wiki-style local vault. At the reviewed commit it keeps canonical source material in `raw/`, writes cited knowledge pages in `wiki/`, mediates NotebookLM and Obsidian use, exposes CLI/MCP/web operations, and constrains agents through a gateway, validator, skills, hooks, pollers, and scheduled jobs.

**Repository:** https://github.com/badwally/TheKnowledge

**Reviewed commit:** [c573953baf79695a0fd065e0309689803b3f2e86](https://github.com/badwally/TheKnowledge/commit/c573953baf79695a0fd065e0309689803b3f2e86)

**Last checked:** 2026-06-05

## Core Ideas

**The filesystem is the system of record.** Raw sources are normalized Markdown files with YAML frontmatter, wiki pages are Markdown files with page-type schemas, NotebookLM state is bookkeeping under `nlm/`, and runtime policies/events live under `.knowledge/`; the architecture document explicitly rejects a standing database for core reads ([README.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/README.md), [ARCHITECTURE.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/ARCHITECTURE.md), [WIKI.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/WIKI.md)).

**The gateway is the write boundary.** `wiki` CLI commands, MCP tools, and web routes delegate into `src/gateway/ops/`; `apply_plan` validates all planned wiki updates before atomic writes, holds a `wiki-author` lock, records backlinks, and logs the write ([src/gateway/ops/apply_plan.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/apply_plan.py), [src/gateway/mcp_server.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/mcp_server.py), [src/gateway/web/app.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/web/app.py)). Agents can read files, but sanctioned mutation is narrow and auditable.

**Citation grounding is enforced at the page level.** The validator checks source shape, content hashes, immutable source bodies, page frontmatter, required sections, timestamps, slug rules, citation verbs, and uncited claims; draft mode downgrades citation failures but final pages must carry inline source links ([src/gateway/validator.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/validator.py), [src/gateway/citations.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/citations.py), [src/gateway/ops/finalize.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/finalize.py)).

**Context efficiency is mostly routing, caps, and progressive loading.** The system avoids dumping the vault into context: `wiki search` is bounded lexical search, `wiki context` resolves one page and N-hop wikilink neighbors, authorship prompts cap source and existing-page snippets, and evaluation context has per-domain and per-source character caps ([src/gateway/ops/search.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/search.py), [src/gateway/ops/context_op.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/context_op.py), [src/gateway/ops/ingest.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/ingest.py), [src/gateway/evaluate/wiki_context.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/evaluate/wiki_context.py)). There is no local vector index in the inspected implementation; NotebookLM supplies the heavier corpus query path.

**NotebookLM is treated as a mediated synthesis engine, not the source of truth.** `wiki query` requires a persistent domain notebook, sends the question through `NlmClient`, resolves NotebookLM citation ids through a source map, rewrites `[N]` markers to wiki source links, and files the answer as a synthesis page through the gateway ([src/gateway/ops/query.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/query.py), [src/gateway/nlm_client.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/nlm_client.py), [src/gateway/research/source_map.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/research/source_map.py)). External synthesis must come back into the filesystem with citations.

**Curation traces feed candidate policy learning.** Filter decisions and user corrections accumulate as per-domain examples; later filter calls select those examples for calibration, and `finetune.distill_prompt` can distill the example bank into a candidate policy version without overwriting the live policy ([src/gateway/filter/examples.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/filter/examples.py), [src/gateway/filter/semantic.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/filter/semantic.py), [src/gateway/ops/filter_correct.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/filter_correct.py), [src/gateway/ops/finetune.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/finetune.py)). This is a staged trace-derived loop, with review/promotion left outside the automatic path.

## Artifact analysis

- **Storage substrate:** `files` `repo` `service-object` - The central retained artifacts are local Markdown/YAML files in `raw/`, `wiki/`, `nlm/`, `.knowledge/`, `index.md`, and `log.md`, normally under git; NotebookLM notebooks and generated artifacts are external service objects accessed only through the gateway wrapper ([README.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/README.md), [ARCHITECTURE.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/ARCHITECTURE.md), [src/gateway/nlm_client.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/nlm_client.py)).
- **Representational form:** `prose` `symbolic` - Source bodies, wiki claims, plans, synthesis pages, skills, policies, logs, digests, and NotebookLM answers are prose; YAML frontmatter, page types, source ids, wikilinks, domain policies, source maps, lock names, MCP schemas, validator rules, and schedule/event records are symbolic. I found no durable local parametric memory store at this commit.
- **Lineage:** `authored` `imported` `trace-extracted` - Wiki conventions, policies, skills, schemas, and code are authored; raw source files are imported through converters, pollers, watchers, research adapters, or manual ingest; filter examples, event logs, agent digests, evaluation trends, and candidate policy versions derive from operational traces and prior decisions.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Raw sources and wiki pages advise as knowledge; CLAUDE/skill text instructs agents; the gateway, locks, direct-write rules, and CLI-only exclusions enforce mutation boundaries; page types, domains, source maps, wikilinks, and MCP operation schemas route work; validator and lint checks validate; lexical scores, filter scores, domain inference, query plans, and NotebookLM source maps rank or select context; example-bank distillation and evaluation trends support learning.

**Raw sources.** `raw/<type>/<id>.md` files preserve imported evidence with stable ids, content hashes, and mutable frontmatter fields for pipeline state. Their authority is mostly knowledge evidence; their ids become citation anchors for every downstream wiki claim ([src/gateway/ops/ingest.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/ingest.py), [src/gateway/validator.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/validator.py)).

**Wiki pages.** Entity, concept, source, synthesis, MOC, and artifact pages are authored or generated prose plus symbolic frontmatter and wikilinks. They are knowledge artifacts for readers and agents, but their frontmatter, citations, `synthesizes` lists, draft fields, and backlink records also route validation, context assembly, NotebookLM sync, and evaluation ([WIKI.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/WIKI.md), [src/gateway/wiki_pages.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/wiki_pages.py), [src/gateway/ops/apply_plan.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/apply_plan.py)).

**Domain policies, examples, and candidate policies.** Live `policy.yaml` files instruct filters; examples capture prior decisions and rationales; candidate `policy_versions` are distilled but not automatically promoted. This is the most important authority split: traces become calibration knowledge first, and only a reviewed policy can become a stronger system-definition artifact ([src/gateway/filter/policy.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/filter/policy.py), [src/gateway/filter/examples.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/filter/examples.py), [src/gateway/ops/finetune.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/finetune.py)).

**Gateway operations and validators.** CLI/MCP/web operation definitions, validation functions, direct-write lint, and sanctioned citation operations are system-definition artifacts. They decide which writes can land, which NotebookLM calls are allowed, and how incomplete citations can be repaired ([src/gateway/mcp_server.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/mcp_server.py), [src/gateway/validator.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/validator.py), [src/gateway/ops/cite.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/cite.py)).

**Events, logs, schedules, and hooks.** `log.md`, `.knowledge/events`, `.knowledge/schedule.yaml`, agent subscription YAML, and Claude hooks retain operational state. Most of it is audit or routing state, but the agent digest and session reanchor hooks can put selected retained state back in front of a future agent ([src/gateway/events.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/events.py), [src/gateway/ops/agent_log.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/agent_log.py), [src/gateway/scheduler.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/scheduler.py), [.claude/hooks/session-start-reanchor.sh](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/.claude/hooks/session-start-reanchor.sh)).

**Promotion path.** TheKnowledge has several explicit ladders: imported source -> wiki source page -> cited synthesis/entity/concept page -> finalized page; filter decision -> example -> candidate policy -> manually promoted policy; research candidate -> filtered raw source -> NotebookLM session -> cited synthesis -> persistent notebook promotion. The implementation favors visible promotion steps over silent memory authority upgrades.

## Comparison with Our System

| Dimension | TheKnowledge | Commonplace |
|---|---|---|
| Primary purpose | Personal research capture, synthesis, and operation | Methodology KB and framework for agent-operated knowledge bases |
| Canonical substrate | Local Markdown/YAML vault plus gateway state | Git-tracked Markdown artifacts plus generated indexes and validators |
| Write path | Gateway ops, converters, pollers, NotebookLM mediation, plan application | Authored notes/reviews/instructions, snapshots, indexes, validation, review gates |
| Read-back | Explicit search/context/query plus session hooks and MCP/skill affordances | Mostly explicit pull through files, `rg`, indexes, links, and loaded instructions |
| Governance | Citation grounding, immutable source bodies, write gateway, draft/finalize lifecycle, source maps | Collection contracts, type specs, citations, deterministic validation, semantic review |

The closest alignment is architectural: both systems treat prose files as operational artifacts and use symbolic contracts to decide what those files mean. TheKnowledge is more productized around ingestion, NotebookLM, web forms, pollers, and agent-facing MCP tools. Commonplace is narrower but more explicit about collection-local type contracts, cross-system comparison vocabulary, and review workflow.

The strongest divergence is read-back. Commonplace expects agents to search and load relevant material deliberately. TheKnowledge has the same explicit pull surface, but it also installs Claude hooks and skills that remind or reanchor host agents at session boundaries. That is useful but weaker than a deployed pre-call memory injector: the hook output instructs the host agent to act, but faithfulness still depends on the host agent following it.

### Borrowable Ideas

**Candidate policies from curation traces.** Ready for Commonplace review workflows. We could retain accepted/rejected review findings as examples and distill candidate review rubrics without automatically replacing the live instruction.

**Service mediation with source-map reconciliation.** Ready when Commonplace uses external synthesis services. The important pattern is not NotebookLM specifically; it is forcing service output through a source map and then back into a cited local artifact.

**Session reanchor hooks with explicit authority labels.** Needs a concrete serving surface. A Commonplace hook could remind an agent to reload a workshop state file, but it should name whether the loaded state is advice, instruction, or a blocker.

**Draft-finalize as an authority transition.** Ready now as vocabulary. TheKnowledge's draft citation downgrade and finalization gate are a clean way to keep useful generated prose visible without pretending it has full claim authority.

**Do not borrow unrestricted scheduler command execution.** The scheduler is pragmatic for a personal system, but Commonplace should avoid arbitrary scheduled shell commands unless each job has a typed contract, write boundary, and review path.

## Write side

**Write agency:** `manual` `automatic` - Humans and agents can write through explicit gateway commands, MCP tools, and file-drop workflows; automatic writes come from watchers, pollers, scheduled jobs, filter scoring, research materialization, NotebookLM-mediated synthesis filing, event emission, daily digests, evaluation trend writes, and candidate policy distillation.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` - NotebookLM and daily-domain digest paths consolidate selected sources into shorter synthesis pages; ingest and research materialization use content hashes, URLs, source ids, and source maps to avoid duplicate source/citation state; research analysis, query filing, and policy distillation synthesize new retained pages or candidate policies; finalization/abandon/supersedence/retraction/stale checks invalidate or downgrade artifacts; source-to-wiki, draft-to-final, session-to-persistent-notebook, and example-to-candidate-policy paths promote artifacts to stronger roles.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` `tool-traces` - Qualifying traces include gateway logs, filesystem event bus records, watcher/poller events, filter decisions and corrections, evaluation runs, scheduler job outcomes, and agent activity events. These are operational traces, not user conversation transcripts as the primary substrate.

**Learning scope:** `per-project` `cross-task` - Examples and policy versions are per-domain inside one vault, then reused across later filter calls, research runs, and ingestion decisions; evaluation trends are per-domain and cross-run.

**Learning timing:** `offline` `staged` - Filter examples are accumulated online as operations run, but distillation into a candidate policy is a separate `wiki finetune --distill` step and live promotion is not automatic.

**Distilled form:** `prose` `symbolic` - The distilled policy candidate is YAML containing prose inclusion/exclusion criteria plus symbolic version/calibration metadata; agent digests and daily digests are draft prose pages.

**Extraction.** The main oracle is not a hidden autonomous learner. `filter_correct` records user corrections as high-signal examples; filter scoring records model rationales; `finetune.distill_prompt` samples examples and asks an LLM for revised criteria; optional calibration scores the candidate against held-out labels ([src/gateway/ops/filter_correct.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/filter_correct.py), [src/gateway/ops/calibration.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/calibration.py), [src/gateway/ops/finetune.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/finetune.py)).

**Survey placement.** TheKnowledge fits the curation-trace-to-policy family. It strengthens the distinction between trace storage and authority promotion: operational traces are retained as knowledge/calibration artifacts, while the distilled policy remains a candidate until a human or later procedure promotes it.

## Read-back

**Read-back:** `both` - Agents and humans can explicitly pull memory through file reads, `wiki search`, `wiki context`, `wiki query`, MCP tools, and the web UI; retained state can also be pushed at session start or before compaction by Claude hooks, and scheduled/agent digest paths can create draft pages from retained event state.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / judgment` - Hook output is coarse session-level reminder text; `wiki context` and citations use page/source identifiers and wikilinks; `wiki search` uses lexical matching; NotebookLM queries, filter scoring, query planning, domain inference, and evaluation use LLM or service judgment over selected context.

**Faithfulness tested:** `no` - The repository has tests for search, MCP parity, validation, event routing, evaluation plumbing, query filing, citation handling, and policy calibration, but I did not find a with/without read-back ablation or post-action audit proving that pushed hook/digest memory changes agent behavior correctly.

**Direction edge cases.** Static skill files are baseline instruction, not retained memory read-back. The retained push cases are narrower: SessionStart and PreCompact hooks print instructions based on the presence of session state, event digests convert retained event records into draft synthesis pages, and MCP operation responses return selected retained content to a host agent ([.claude/settings.json](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/.claude/settings.json), [.claude/hooks/precompact-snapshot.sh](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/.claude/hooks/precompact-snapshot.sh), [.claude/hooks/session-start-reanchor.sh](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/.claude/hooks/session-start-reanchor.sh), [src/gateway/ops/agent_log.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/agent_log.py)).

**Targeting and signal.** Pull paths are identifier-heavy: source ids, page slugs, domain slugs, notebook ids, and wikilinks do most of the routing. Lexical search is simple substring matching over file title, slug, and body. Judgment-based paths happen when external services or LLM clients choose domain, filter relevance, query plan, research taxonomy, or evaluation score.

**Injection point.** Read-back happens before the consumer acts: a session hook writes text into the host agent's startup context, `wiki context` assembles pages before returning the operation result, `wiki query`/research assemble NotebookLM answers before filing or presenting them, and evaluation assembles wiki context before the judge call. Post-operation logs, event writes, source-map updates, and digests are write-side maintenance for later consumers.

**Selection, scope, and complexity.** Context scope is explicit but uneven. `wiki context` follows N-hop links, `wiki search` caps result count, authorship prompts cap source and existing-page snippets, and evaluation skips oversized source bodies. NotebookLM query selection is service-mediated, so source inclusion and ranking quality are not fully inspectable from this repo.

**Authority at consumption.** Search/context/query results are advisory context; source citations carry evidence authority; hooks and skills are instruction to a compliant host agent; validators and gateway operations enforce write rules; policy files steer filter decisions but candidate policies remain non-live until promoted.

**Other consumers.** Humans consume the Obsidian vault, web UI, CLI output, lint reports, daily reviews, and drafts. Gateway jobs, validators, NotebookLM wrappers, pollers, schedulers, and MCP clients consume the same retained artifacts through narrower operational APIs.

## Curiosity Pass

**The system is less a memory retriever than a write-governance layer.** Its most mature design is not recall quality; it is the path by which imported evidence becomes cited claims and candidate policies without bypassing visible authority transitions.

**The "no database" claim is true for the canonical layer but not for all retained state.** There is no standing DB, but `.knowledge/`, `nlm/`, logs, source maps, evaluation CSVs, schedules, and built web artifacts are all behavior-shaping retained files that must be included in backup and review thinking.

**NotebookLM is both powerful and partly opaque.** The gateway gives it provenance boundaries, but relevance/ranking inside NotebookLM is not inspectable from code. Treat filed synthesis pages as service-derived artifacts with local citation repair, not as locally reproducible derivations.

**Trace-derived learning is conservative.** The policy loop stops at candidate YAML and optional calibration metrics; this is weaker than autonomous skill mutation but better aligned with reviewable KB operation.

**Some automatic paths bypass the full plan validator shape.** Daily digests and some agent/triage helpers write files or frontmatter directly with locks or plain writes. They are still gateway code, but not every path gets the same `apply_plan` validation and reporting surface.

## What to Watch

- Whether a local BM25/vector index or `wiki index --rebuild` becomes real; that would change read-back from mostly identifier/lexical pull to ranked retrieval.
- Whether candidate policy promotion becomes automated; that would upgrade trace-derived examples from calibration evidence into direct system-definition authority.
- Whether hook-assisted session reanchoring gains behavior tests; that would turn the faithfulness verdict from plumbing-only to behavior-grounded.
- Whether NotebookLM source maps cover all artifact and query paths reliably; unresolved `[[nlm:<uuid>]]` citations weaken the local provenance story.
- Whether all automatic write paths are routed through the same validation/reporting contract as `apply_plan`; divergence there is the main governance risk.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: TheKnowledge stores evidence carefully, while most activation is still explicit pull plus coarse hooks.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: TheKnowledge's files, policies, examples, validators, hooks, source maps, and service notebooks carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, wiki pages, filter examples, logs, and source maps usually advise or provide evidence.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: gateway ops, validators, policies, skills, hooks, and scheduler definitions constrain later behavior.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: filter decisions and operational events can be distilled into candidate policies and digest pages.
