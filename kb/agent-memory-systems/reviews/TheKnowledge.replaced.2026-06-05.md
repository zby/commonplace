---
description: "TheKnowledge review: filesystem wiki gateway with citation-grounded Markdown, NotebookLM-mediated synthesis, policy distillation, MCP tools, and hook-assisted read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
last-checked: "2026-06-03"
tags: []
---

# TheKnowledge

> Replaced 2026-06-05. See [TheKnowledge](./TheKnowledge.md) for the current review.

TheKnowledge, from `badwally/TheKnowledge`, is a personal research knowledge base and gateway for an LLM Wiki-style filesystem vault. At the reviewed commit it stores canonical source material in `raw/`, writes LLM-authored pages in `wiki/`, routes all mutation through a Python `wiki` gateway, enforces citation grounding and source immutability, mediates NotebookLM corpus and artifact operations, exposes CLI/MCP/web surfaces, and includes Claude Code hooks and skills for agent operation.

**Repository:** https://github.com/badwally/TheKnowledge

**Reviewed commit:** [c573953baf79695a0fd065e0309689803b3f2e86](https://github.com/badwally/TheKnowledge/commit/c573953baf79695a0fd065e0309689803b3f2e86)

**Last checked:** 2026-06-03

## Core Ideas

**The filesystem is the canonical database.** The top-level README and architecture doc describe one substrate: immutable source Markdown under `raw/`, authored wiki Markdown under `wiki/`, NotebookLM bookkeeping under `nlm/`, runtime policy/state under `.knowledge/`, and no standing database for core reads ([README.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/README.md), [ARCHITECTURE.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/ARCHITECTURE.md), [src/gateway/paths.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/paths.py)). The design is inspectable and git-friendly: source bodies remain files, page bodies remain files, and derived indexes or services sit beside that substrate rather than replacing it.

**The gateway is the single mutator.** CLI, MCP, and web routes delegate to `src/gateway/ops/`; writes use `OperationResult`, file locks, atomic writes, validation, backlink updates, and `log.md` entries ([src/gateway/core.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/core.py), [src/gateway/ops/apply_plan.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/apply_plan.py), [src/gateway/mcp_server.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/mcp_server.py)). This makes the gateway a system-definition artifact: agents can read files directly, but sanctioned mutation has a narrow path.

**Citation grounding is a hard governance rule, not a style preference.** The validator checks source frontmatter, content hashes, source immutability, mutable-source-field allowlists, page schemas, timestamps, slug rules, wikilinks, and citation grounding ([src/gateway/validator.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/validator.py), [docs/adr/ADR-005-citation-grounding-mandatory.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/docs/adr/ADR-005-citation-grounding-mandatory.md)). Draft pages can temporarily downgrade unresolved claims, but final wiki pages must carry inline `[[sources/<id>]]` support.

**Context efficiency is explicit but mostly symbolic.** The system avoids full-context loading through path routing, source/page type boundaries, `wiki context` N-hop wikilink walks, prompt guards for unbounded `log.md` and `index.md`, domain-scoped evaluation context with character caps, filter prompts with truncated source bodies, and authorship prompts that cap existing-page snippets before calling the planner ([src/gateway/ops/context_op.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/context_op.py), [src/gateway/evaluate/wiki_context.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/evaluate/wiki_context.py), [src/gateway/paths.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/paths.py), [src/gateway/ops/ingest.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/ingest.py)). The deferred `wiki search` stub means general local retrieval is still file/search-tool oriented; NotebookLM supplies corpus query for domains with persistent notebooks.

**NotebookLM is mediated as a heavy synthesis service.** `wiki query` requires a domain notebook, resolves NotebookLM citations through cached source maps, rewrites numeric citations into wiki source links, and files a synthesis page through the normal plan/apply path ([src/gateway/ops/query.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/query.py), [src/gateway/research/source_map.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/research/source_map.py), [docs/MCP_API.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/docs/MCP_API.md)). The important design point is not NotebookLM itself; it is that external synthesis returns to the canonical vault with provenance.

**The filter policy learns from curation traces.** Each domain has a policy file; filter calls can include selected examples; `wiki filter-correct` writes user corrections into source frontmatter and pins examples under `.knowledge/policies/<domain>/examples/`; `wiki finetune --distill` feeds accumulated examples to an LLM and writes a candidate policy version, never overwriting the live policy ([src/gateway/filter/policy.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/filter/policy.py), [src/gateway/filter/examples.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/filter/examples.py), [src/gateway/ops/filter_correct.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/filter_correct.py), [src/gateway/ops/finetune.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/finetune.py)). This is the strongest trace-derived learning loop in the code.

**Agent adoption is through native surfaces.** The repo ships Claude Code skills, MCP tools, session hooks, watcher/scheduler daemons, and a local web UI ([.claude/skills/wiki-research/SKILL.md](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/.claude/skills/wiki-research/SKILL.md), [.claude/settings.json](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/.claude/settings.json), [src/gateway/scheduler.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/scheduler.py), [src/gateway/web/app.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/web/app.py)). The system does not require a hidden memory service for agents to use it; it makes the filesystem and gateway operations legible to existing agent hosts.

## Artifact analysis

- **Storage substrate:** `files` — Central durable state is Markdown, YAML, and JSON files under `raw/`, `wiki/`, `nlm/`, `.knowledge/`, `.claude/`, `index.md`, and `log.md`, with Python gateway code enforcing how those files are written.
- **Representational form:** `prose` `symbolic` — Prose Markdown carries source, synthesis, policy criteria, rationales, skills, and session-state content; YAML/JSON frontmatter, policies, examples, schedules, events, source maps, Python validators, ops, MCP wrappers, hooks, and scripts carry symbolic state and executable system definitions.
- **Lineage:** `authored` `imported` `trace-extracted` — Raw sources are imported through ingest and capture paths; wiki pages, policies, gateway code, hooks, and skills are authored or generated through controlled operations; filter examples, logs, event records, and candidate policies derive from retained curation and operation traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — Sources, wiki pages, logs, and examples act as knowledge; skills and hooks instruct; validators and policies enforce; gateway operations, NotebookLM maps, and MCP surfaces route; citation and schema checks validate; filter examples and candidate policies carry learning authority.

**Raw source files.** Storage substrate: `raw/<type>/<id>.md` files. Representational form: mixed Markdown body plus YAML frontmatter. Lineage: imported through converters, pollers, watcher, or explicit `wiki ingest`; source bodies are immutable after ingest while only allowlisted frontmatter fields may change ([src/gateway/ops/ingest.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/ops/ingest.py), [src/gateway/validator.py](https://github.com/badwally/TheKnowledge/blob/c573953baf79695a0fd065e0309689803b3f2e86/src/gateway/validator.py)). Behavioral authority: knowledge artifacts as preserved evidence; they become learning inputs for filtering and source material for wiki pages, NotebookLM corpora, and evaluation context.

**Wiki pages.** Storage substrate: `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/synthesis/`, `wiki/mocs/`, `wiki/artifacts/`, and related page directories. Representational form: mixed Markdown prose plus symbolic frontmatter and wikilinks. Lineage: source pages are generated from raw frontmatter; entity/concept/synthesis pages are authored through plans, queries, NotebookLM artifacts, or controlled ops; draft/final state records citation maturity. Behavioral authority: knowledge artifacts when read as evidence/context, and weak system-definition artifacts when an agent treats a page as a task guide or domain map.

**Gateway operations and validators.** Storage substrate: Python modules under `src/gateway/`. Representational form: symbolic/executable code plus prompt templates. Lineage: authored implementation. Behavioral authority: system-definition artifacts with enforcement force: they route operations, reject invalid writes, apply locks, select prompt context, call LLMs, mediate NotebookLM, expose MCP tools, and log mutations.

**Domain policies and example banks.** Storage substrate: `.knowledge/policies/<domain>/policy.yaml`, `examples/*.yaml`, `policy_versions/*.yaml`, calibration data, and generated domain skills. Representational form: symbolic YAML with prose criteria and rationales. Lineage: policies are authored or generated from domain bootstrapping; examples are retained from filter decisions and user corrections; candidate policies are distilled from examples and current policy. Behavioral authority: filter policies and selected examples shape future inclusion/exclusion decisions; candidate versions have reviewable advice authority until promoted.

**NotebookLM registries, query plans, and source maps.** Storage substrate: `nlm/notebooks.yaml`, `nlm/query_plans/*.yaml`, `nlm/source_maps/*.json`, and filed artifacts in `wiki/artifacts/`. Representational form: symbolic mappings plus generated prose/media artifact records. Lineage: derived from gateway-mediated NotebookLM calls and citation resolution. Behavioral authority: routing and provenance authority for corpus synthesis; the source map decides whether external citations can become `[[sources/...]]` wiki citations.

**Read-back and agent control surfaces.** Storage substrate: `.claude/skills/*/SKILL.md`, `.claude/settings.json`, `.claude/hooks/*.sh`, generated `.claude/skills/wiki-<domain>/SKILL.md`, MCP server definitions, and CLI command registry. Representational form: mixed prose instructions, JSON hook config, shell scripts, and Python tool wrappers. Lineage: authored static skills/hooks plus generated domain skills from policy/MOC/recent synthesis. Behavioral authority: system-definition artifacts that instruct agents how to call the gateway and, in the SessionStart hook, push a re-anchor instruction based on retained `docs/session-state.md`.

**Operational traces and event logs.** Storage substrate: `log.md`, `.knowledge/events/<date>/*.json`, `.knowledge/schedule.yaml`, `.knowledge/agents/*.yaml`, lint reports, evaluation results, and session-state docs. Representational form: mixed event records, Markdown summaries, YAML configs, and JSON results. Lineage: generated by gateway operations, watcher events, schedules, evaluations, and session hooks. Behavioral authority: mostly knowledge artifacts for status, audit, and operator review; some become system-definition inputs when schedulers, subscribers, status displays, or fine-tune readiness checks act on them.

**Promotion path.** TheKnowledge has several promotion ladders: source file -> wiki source page -> cited entity/concept/synthesis page -> finalized page; filter decision -> pinned example -> distilled candidate policy -> manually promoted policy; domain policy/MOC/recent synthesis -> generated Claude skill; NotebookLM citation -> source map resolution -> wiki citation. The strongest governance idea is that higher authority generally passes through an explicit gateway operation rather than an implicit retrieval side effect.

## Comparison with Our System

| Dimension | TheKnowledge | Commonplace |
|---|---|---|
| Primary purpose | Personal research wiki and LLM/NotebookLM gateway | Methodology KB for building agent-operated knowledge bases |
| Main substrate | Local Markdown/YAML files under `raw/`, `wiki/`, `.knowledge/`, `nlm/` | Git-tracked Markdown collections, type specs, instructions, sources, reports, indexes |
| Write control | Single gateway with validators, locks, plans, logs, MCP/CLI/web surfaces | Collection contracts, type specs, deterministic validation, skills, review gates, git workflow |
| Context strategy | Explicit pulls (`context`, `query`, MCP tools), domain-scoped context caps, prompt guards, NotebookLM corpora | `rg`, indexes, links, collection contracts, type specs, review bundles, skills |
| Learning loop | Curation trace -> example bank -> candidate filter policy; generated domain skills | Human/agent review -> durable notes/instructions; semantic QA and validation; limited automatic learning |
| Read-back | Pull by default, plus hook-assisted session-state re-anchor and generated skills | Mostly pull through search/index/link/skill paths; shell instructions can push static guidance |

TheKnowledge is close to Commonplace in philosophy: file-first, gateway-mediated, source-grounded, validator-backed, and built for agents reading and writing under constraints. Its most relevant difference is domain: TheKnowledge is a personal research production system, while Commonplace is a methodology library and framework. That makes TheKnowledge more operationally integrated with external capture, NotebookLM, web UI tasks, pollers, and Claude Code hooks; Commonplace is more explicit about artifact typing, review workflow, collection boundaries, and cross-system comparison.

TheKnowledge also separates provenance and authority more strongly than many research wikis. Raw sources are not the same as wiki claims; drafts are not the same as finalized pages; candidate policies are not live policies; NotebookLM citations are not accepted until source-map resolution. That is directly aligned with Commonplace's artifact-authority vocabulary.

The main tradeoff is complexity. TheKnowledge accumulates many operational paths: pollers, watcher, scheduler, web tasks, NotebookLM, filters, plans, lint, evaluation, skills, hooks, and source maps. The gateway keeps mutation coherent, but the context model is still spread across several surfaces. Commonplace should borrow the authority discipline without importing the whole operations stack unless it needs equivalent capture throughput.

**Read-back:** `both` — The dominant memory path is explicit pull through `wiki context`, `wiki query`, MCP tools, source/page reads, and NotebookLM-mediated synthesis; the Claude Code SessionStart hook also pushes a pre-action re-anchor instruction that tells agents to consult retained `docs/session-state.md` when fresh enough.

### Borrowable Ideas

**Keep candidate policy distillation reviewable.** The filter fine-tune loop writes a candidate policy version instead of mutating the live policy. A Commonplace analogue would let repeated review/validation decisions produce candidate instruction or validation updates, with human or gate review before promotion. Ready as a workshop experiment, not as automatic instruction promotion.

**Make external synthesis prove its citations before entering the KB.** NotebookLM output is not trusted merely because it came from a corpus; source maps resolve citations back into local source ids. Commonplace could borrow this for any external summarizer or research service. Ready whenever an external synthesis path is introduced.

**Expose every write operation through one typed result shape.** `OperationResult` makes CLI/MCP/web behavior easier to compare and test. Commonplace already has command conventions, but a uniform result envelope for mutating commands would improve agent ergonomics. Ready for command UX cleanup.

**Use prompt guards for known unbounded files.** `assert_safe_for_prompt()` blocks `log.md` and `index.md` from accidental wholesale prompt inclusion. Commonplace has similar risk around generated indexes and review logs; a small guard layer could prevent expensive or behaviorally noisy loads. Ready now where commands assemble prompt context.

**Generate domain skills from policy and navigation state.** TheKnowledge's `skill-emit` compiles policy, MOC links, and recent threads into a bounded Claude skill. Commonplace could generate collection or project skills from `COLLECTION.md`, type specs, and curated indexes. Useful, but only after deciding which generated instructions have authority and freshness guarantees.

**Do not borrow arbitrary scheduled shell execution as an agent surface.** The scheduler is intentionally CLI-only in MCP because it can run arbitrary commands. Commonplace should preserve that boundary if it adds scheduled jobs.

## Write-side placement

**Write agency:** `manual` `automatic` — humans and agents author raw/wiki/policy artifacts through gateway operations, while ingest, NotebookLM filing, source-map resolution, filter correction, candidate policy distillation, generated skills, hooks, watcher/scheduler paths, and validators also mutate retained files and metadata.

**Curation operations:** `consolidate` `synthesize` — source/wiki/query paths consolidate imported material into pages and filed artifacts, while NotebookLM queries, candidate policy distillation, and generated domain skills synthesize new retained artifacts without replacing the live policy automatically.

### Trace-derived learning

**Trace source.** The qualifying traces are curation and filtering events rather than full chat transcripts: automatic filter decisions, user corrections, rationales, scores, source frontmatter snapshots, and content excerpts retained as examples under `.knowledge/policies/<domain>/examples/`. Gateway logs, event files, and evaluation results are additional operational traces, but the implemented learning loop uses the filter example bank.

**Trace source:** `event-streams` — The implemented learning loop consumes retained curation/filtering events, user corrections, rationales, scores, source snapshots, and example records rather than chat transcripts or full tool trajectories.

**Extraction.** Extraction is partly deterministic and partly LLM-mediated. `filter-correct` pins a corrected include/exclude decision with rationale and source snapshot; high-confidence and legacy examples can also populate the bank. Future filter calls select representative examples and include them in the filter prompt. When a domain reaches the threshold, `distill_prompt()` asks an LLM to produce tightened inclusion and exclusion criteria from the accumulated examples and current policy, parses JSON, writes a candidate YAML policy version, and optionally scores calibration metrics.

**Scope and timing.** Scope is per-domain. Timing is staged: decisions accumulate during ingest/filter workflows; readiness is surfaced by `wiki status`; distillation is an explicit `wiki finetune --distill` operation gated by example count unless forced. The live policy is not replaced automatically.

**Learning scope:** `cross-task` — The retained examples and candidate policy are scoped by domain, but they accumulate across filter/ingest decisions and shape later decisions beyond a single task.

**Learning timing:** `staged` — Examples accumulate during workflows, while distillation is an explicit readiness-gated `wiki finetune --distill` stage that writes a candidate rather than replacing the live policy.

**Distilled form:** `prose` `symbolic` — The distilled candidate policy is YAML carrying symbolic include/exclude structure plus prose criteria and rationale.

**Survey placement.** On the trace-derived learning survey, TheKnowledge belongs in the curation-trace-to-policy family. It strengthens the survey claim that the most important authority jump is not trace storage itself but promotion from observed decisions into a system-definition artifact. Here, examples are knowledge artifacts and calibration inputs; a distilled policy candidate is a system-definition artifact only after review/promotion.

## Read-back placement

**Direction.** Both. Agents and humans pull retained memory through file reads, `wiki context`, `wiki query`, `wiki status`, MCP tools, skills, and NotebookLM-mediated synthesis. Separately, the Claude Code `SessionStart` hook pushes an instruction into the agent session telling it to re-read retained `docs/session-state.md` before plan/write actions when the snapshot is newer than the session start.

**Read-back signal:** `coarse` — The push path is the Claude Code `SessionStart` hook, which fires on session start and relies on freshness of retained session state rather than semantic relevance to the current request.

**Targeting and signal.** Pull targeting is usually `identifier`: page slug/path, domain slug, source id, NotebookLM notebook/domain, MCP tool name, or wikilink. The hook push is `coarse`: it fires at SessionStart and relies on the retained file's mtime/session-start comparison, not semantic relevance to the user's current request.

**Selection, scope, and complexity.** `wiki context` bounds expansion by N-hop wikilink depth and returns either Markdown or JSON. Evaluation context caps total and per-source characters. Authorship prompts cap source body and existing-page snippets. The hook path is intentionally tiny: it pushes a short rule, not the full session state.

**Authority at consumption.** Retrieved wiki/source content is advisory context unless a host or agent treats a page as instruction. Gateway validators and policies carry enforcement authority at write/filter time. The session hook carries instruction authority because Claude Code injects hook stdout into context before the agent acts.

**Faithfulness.** The read-back path does not appear to test whether `wiki context`, generated skills, or the session-state hook actually change agent behavior. Evaluation modules judge wiki answer quality and trends, not read-back uptake.

**Faithfulness tested:** `no` — The review finds evaluation of wiki answer quality and trends, but no with/without test that read-back changes agent behavior.

**Other consumers.** The same retained memory is consumed by Obsidian, the FastAPI/React UI, scheduled jobs, lint/status reports, NotebookLM corpus workflows, and humans reviewing drafts, contradictions, or research plans.

## Curiosity Pass

**The "no database" claim has a useful boundary.** Core knowledge remains files, but NotebookLM, MCP, web tasks, and optional external APIs are active services around it. The system stays inspectable because service outputs are filed back into the vault, not because services are absent.

**`wiki search` is still a stub while `wiki context` is real.** That makes current read-back more identifier/link driven than retrieval driven. Agents need a slug, page title, domain, or NotebookLM-backed query path rather than a general local semantic index.

**The citation-grounding rule is stronger for wiki pages than for generated policy or skill text.** Policies and generated skills can shape future behavior, but their claims do not carry the same per-claim source citation discipline as finalized wiki pages. That is reasonable for operational instructions, but it is the boundary to watch.

**The filter-learning loop is conservative in exactly the right place.** It learns a candidate policy from examples but stops before live replacement. That preserves reviewability while still using repeated decisions as signal.

**The hook-based session-state mechanism is a small but real push-memory design.** It does not flood context with old session notes. It pushes a rule that can cause targeted pull of a retained snapshot only when the snapshot is temporally relevant.

## What to Watch

- Whether `wiki search --rebuild` or a BM25/vector layer becomes implemented. That would change TheKnowledge's read-back from mostly identifier/link pull to relevance-ranked retrieval.
- Whether candidate policies gain promotion metadata, reviewer identity, or rollback links. That would make trace-derived policy learning safer as system-definition authority.
- Whether generated domain skills include freshness stamps and source pointers for policy/MOC inputs. That would make skill read-back more auditable.
- Whether the SessionStart hook evolves from a coarse session-state re-anchor into instance-targeted retrieval. That would strengthen the push-activation placement.
- Whether NotebookLM artifacts and query answers get stricter citation-chain lint before finalization. That would close the main provenance gap in external heavy synthesis.

## Bottom Line

TheKnowledge is a mature file-first research gateway with unusually strong mutation governance. Its main memory design is not autonomous recall; it is a controlled path from captured sources to cited wiki claims, from curation decisions to candidate policies, and from retained session state to hook-assisted agent re-anchoring. For Commonplace, the strongest borrow is the promotion discipline around trace-derived policy learning and external synthesis, not the entire operational surface.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - compares: TheKnowledge stores and governs sources well, while explicit `wiki context`/`query` remain the dominant activation paths.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: TheKnowledge's raw files, wiki pages, policies, examples, validators, source maps, hooks, and logs differ by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: gateway validators, policies, MCP wrappers, hooks, scheduler boundaries, and generated skills configure or constrain future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, wiki pages, logs, event records, examples before promotion, and context outputs serve as evidence or reference.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: curation decisions can become candidate policy updates without immediate automatic promotion.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: raw sources and session-state records remain available while higher-level pages or hook instructions carry compact behavior-shaping context.
