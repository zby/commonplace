---
description: "ai-modules review: deployable multi-vendor skill/plugin bundle with Markdown wiki, session wrapup, task backlog, and linted file memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# ai-modules

`theafh/ai-modules` is Andreas F. Hoffmann's meta-repository for AI skills, agents, commands, hooks, and deployment glue. Its memory-relevant surface is the `knowledge_management` plugin: a plain-Markdown LLM wiki, session/source import front ends, an audit-and-repair agent, deterministic wiki scripts, and text-distillation skills. The same repository also ships `ai_dev` skills for project-local task backlogs, changelog generation, git commits, and AI-instruction writing; those are retained behavior-shaping artifacts too, but the agent-memory center is the wiki workflow.

**Repository:** https://github.com/theafh/ai-modules

**Reviewed commit:** [14f42f58a898f6ae335920d2fb462b39cf61e71b](https://github.com/theafh/ai-modules/commit/14f42f58a898f6ae335920d2fb462b39cf61e71b)

**Last checked:** 2026-06-04

## Core Ideas

**The product is a deployable skill/plugin corpus.** The root README presents `ai-modules` as a collection of professional AI skills, agents, commands, and hooks that can be installed through the bundled Claude marketplace, symlinked globally into vendor config directories, symlinked into a single project, or used in-place from the checkout ([README.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/README.md)). The plugin manifests declare `knowledge_management` and `ai_dev` for Claude and Codex, while `deployment/deployment.sh` discovers artifacts by `plugins/<plugin>/<asset-folder>/` layout and installs them for Claude Code, Codex, Cursor, VS Code Copilot, Gemini CLI, and Antigravity ([.claude-plugin/marketplace.json](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/.claude-plugin/marketplace.json), [deployment/deployment.sh](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/deployment/deployment.sh), [deployment/README.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/deployment/README.md)).

**The wiki is a compiled Markdown memory, not a vector retrieval service.** The `wiki` skill defines a three-layer system: immutable raw sources, agent-owned wiki pages, and `SCHEMA.md` as the governing schema. It explicitly contrasts this with RAG: sources are compiled once into durable pages with cross-links, contradictions, and synthesis rather than re-derived from raw chunks per query ([plugins/knowledge_management/skills/wiki/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki/SKILL.md), [plugins/knowledge_management/README.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/README.md)).

**Schema and scripts make the file memory inspectable.** The wiki scaffold carries `SCHEMA.md`, `index.md`, `log.md`, `raw/`, typed page directories, and a linter that reads the page-type enum and tag taxonomy from the schema. Raw sources carry body-only `sha256` drift hashes, wiki pages carry `sources:` frontmatter and inline claim links, and lint reports frontmatter, links, taxonomy, stale raw content, oversized pages, index drift, and other health checks ([plugins/knowledge_management/skills/wiki/references/template_schema.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki/references/template_schema.md), [plugins/knowledge_management/skills/wiki/scripts/lint.py](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki/scripts/lint.py), [plugins/knowledge_management/skills/wiki/scripts/compute_sha256.py](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki/scripts/compute_sha256.py)).

**Trace-derived learning exists through session wrapup.** `wiki_wrapup` mines the visible chat session for durable claims, decisions, definitions, conventions, comparisons, workflows, and named entities; diffs them against the existing wiki; surfaces new pages, extensions, and contradictions; and only writes approved candidates through the base `wiki` skill ([plugins/knowledge_management/skills/wiki_wrapup/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki_wrapup/SKILL.md)). This is not autonomous online reinforcement learning, but it is durable extraction from agent-human session traces into retained prose and procedural memory.

**Context efficiency is orientation and routing, not embedding search.** Every wiki operation first resolves the wiki path, reads `SCHEMA.md`, `index.md`, and recent `log.md`, then reads selected pages or searches the tree for large wikis. Queries read the index, optionally run recursive search for 100+ page wikis, then read relevant pages and file only valuable syntheses back ([plugins/knowledge_management/skills/wiki/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki/SKILL.md)). Complexity control comes from page types, flat type folders, index summaries, page-size guidance, and deterministic lint; there is no top-k vector budget.

**The repository separates prose authority from deterministic helpers.** Skill prose tells the agent when and how to act; bundled scripts perform discovery, scaffold initialization, hash computation, linting, task validation, git-commit context capture, and changelog day preparation. The README names the intended effect: mechanical work is offloaded to programs so the model does not re-derive it each session ([README.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/README.md), [plugins/ai_dev/skills/task/scripts/lint.py](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/task/scripts/lint.py), [plugins/ai_dev/skills/git_commit/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/git_commit/SKILL.md), [plugins/ai_dev/skills/update_changelog/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/update_changelog/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `files` — The behavior-shaping state is a file tree: plugin manifests, `SKILL.md` files, agent definitions, bundled scripts, templates, deployment config, generated target symlinks/copies, and downstream wiki/task/changelog Markdown files. Git/versioned repo state and deployment paths are important governance surfaces, but the primary retained substrate remains files.
- **Representational form:** `prose` `symbolic` — Skill and agent instructions, wiki pages, task files, changelog entries, summaries, and SPRs are prose; plugin manifests, YAML frontmatter, schema enums, lint scripts, deployment rules, hashes, and generated target configs are symbolic. I did not find a retained vector index or model-weight adaptation path in the reviewed checkout.
- **Lineage:** `authored` `imported` `trace-extracted` — Plugin definitions and procedures are authored; wiki raw sources and task source material can be imported; `wiki_wrapup` derives candidate wiki memory from the active chat session, and changelog generation derives prose from git history.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — Wiki pages, tasks, raw sources, summaries, and changelogs provide knowledge context; loaded skills and agents instruct future actions; deployment manifests and scripts route artifacts into host tools; lints and format scripts validate file memory; `wiki_wrapup`, import, SPR, and changelog flows learn or distill new retained prose from traces or source material.

**Plugin and skill artifacts.** Storage substrate is repo files under `plugins/`, `.claude-plugin/`, and `.codex-plugin/`. Representational form is prose instructions with YAML frontmatter and JSON metadata. Lineage is authored and versioned in the repository. Behavioral authority is instruction and routing when a host loads a skill or plugin manifest; the same source can be deployed into several vendor-specific locations by the deployment script.

**Wiki memory.** Storage substrate is a downstream `wiki/` directory containing `SCHEMA.md`, `index.md`, `log.md`, `raw/`, and typed page folders. Representational form is prose pages plus symbolic frontmatter, type directories, tag taxonomy, source paths, hashes, and links. Lineage is imported raw source -> distilled wiki page, or trace-extracted session content -> proposed page/update -> approved wiki write. Behavioral authority is knowledge, instruction, routing, validation, and learning: pages answer future queries, procedure pages guide action, `index.md` routes lookup, lint validates structure, and wrapup/import workflows turn new material into retained pages.

**`wiki_auto_shaper` agent.** Storage substrate is a Markdown agent definition. Representational form is prose protocol. Lineage is authored. Behavioral authority is repair instruction plus validation governance: it runs lint, audits prose beyond the linter's reach, fixes structure/content issues, surfaces contradictions through the contested-page protocol, re-lints until clean, and appends an audit entry ([plugins/knowledge_management/agents/wiki_auto_shaper.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/agents/wiki_auto_shaper.md)).

**Task backlog.** Storage substrate is project-local `tasks/` and `tasks/archive/` Markdown files. Representational form is prose briefs plus symbolic frontmatter, filenames, links, and lint rules. Lineage can be authored or derived from source material, including chat sessions, pasted notes, specs, PDFs, meeting transcripts, or files on disk. Behavioral authority is knowledge and instruction for future implementers, with validation from `task/scripts/lint.py` enforcing filename, status/location, frontmatter, link, and size rules ([plugins/ai_dev/skills/task/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/task/SKILL.md), [plugins/ai_dev/skills/task/scripts/lint.py](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/task/scripts/lint.py)).

**Changelog and commit helpers.** Storage substrate is `CHANGELOG.md`, temporary commit-context files, and git history. Representational form is prose entries plus symbolic day sections, status markers, and script-produced context blocks. Lineage is imported from git commits/diffs and authored summarization. Behavioral authority is knowledge for future readers and instruction/validation for commit and changelog workflows ([plugins/ai_dev/skills/update_changelog/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/update_changelog/SKILL.md), [plugins/ai_dev/skills/git_commit/scripts/prepare_commit_context.sh](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/ai_dev/skills/git_commit/scripts/prepare_commit_context.sh)).

Promotion path: raw source or session content can become proposed wiki changes, approved pages, index entries, and procedures; operational rules can then be promoted further into a `SKILL.md`, agent definition, linter check, or deployable plugin artifact. That is a form-and-authority escalation from prose evidence to prose instruction to symbolic validation/enforcement, but the reviewed code leaves promotion under human/agent workflow control rather than automatic tier promotion.

## Comparison with Our System

| Dimension | ai-modules | Commonplace |
|---|---|---|
| Primary purpose | Ship reusable AI skills/plugins and a Markdown wiki/task/changelog toolkit | Maintain a typed methodology KB and its validation/review framework |
| Main memory substrate | Plain files deployed into host tool config dirs and downstream wiki/task trees | Typed Markdown artifacts, sources, indexes, review notes, schemas, and Python commands |
| Write path | Skill-driven source ingest, session wrapup, wiki repair, task creation, changelog generation | Agent/human-authored artifacts governed by collection contracts, type specs, validators, review bundles |
| Read-back | Host loads selected skills; the acting agent pulls wiki/task/changelog files via orientation, index, search, and file reads | Mostly explicit pull through `rg`, indexes, links, skills, and reference docs, with validation/review as governance |
| Governance | Markdown schemas, frontmatter, deterministic helper scripts, drift hashes, lints, contested-page protocol | Stronger type specs, source snapshots, deterministic validation, generated indexes, semantic gates, replacement lifecycle |
| Adoption surface | Multi-vendor plugin deployment and ordinary local Markdown | Repo-local framework and installed `commonplace-*` commands |

The strongest alignment is the compiled wiki pattern. Both systems prefer durable, inspectable Markdown artifacts over opaque chat memory or raw-chunk RAG, and both make type/schema/index files do routing work that would otherwise be re-decided by an agent each session.

The main divergence is authority granularity. Commonplace's collection/type/review machinery makes each artifact's role explicit and validates the whole KB against a stable contract. `ai-modules` keeps the model lighter and more portable: a user can deploy the skills into several tools, start a wiki, and rely on local scripts, but the downstream wiki pages do not carry Commonplace-style review status, replacement archives, or collection-local type specs.

`ai-modules` is stronger on host adoption. Commonplace's commands are more integrated with this repo's methodology, while `ai-modules` treats multi-vendor installation as a first-class product surface. That deployment layer is borrowable even where the memory model itself overlaps.

### Borrowable Ideas

**Multi-vendor artifact discovery by plugin layout.** Ready if Commonplace starts distributing skills outside this repo. A `plugins/<plugin>/skills/<skill>/SKILL.md` layout plus generated target formats would make installation more uniform than hand-maintained per-tool copies.

**Body-only raw-source hashes.** Ready now. Commonplace has source snapshots and validation, but the `sha256` convention for raw source bodies is a simple drift-detection mechanism worth considering for re-ingest workflows.

**Triage-first session wrapup.** Ready for workshop contexts. Commonplace could mine a completed agent session into proposed notes/tasks/contradictions, then require explicit approval before library writes land.

**Schema-owned extensible type enums.** Needs a concrete use case. The wiki linter reads page types from `SCHEMA.md`, which is flexible for user wikis. Commonplace's stricter type specs are better for framework consistency, but project-local workshop layers might benefit from schema-defined temporary types.

**Do not borrow broad auto-repair without review-state boundaries.** `wiki_auto_shaper` is useful, but Commonplace should keep large autonomous repairs tied to review runs, explicit artifacts changed, and semantic QA so validation does not become silent rewrite authority.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents author and edit skill files, wiki pages, task files, and changelogs manually through workflows; automatic or semi-automatic writes come from scaffold/init scripts, lint/repair loops, import/wrapup distillation, task linting/archiving, changelog generation, and deployment output generation.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` — `wiki_import` and `wiki_wrapup` consolidate raw/session material into candidate wiki pages, classify candidates as NEW/EXTEND/CONFIRM/CONFLICT to avoid duplicate writes, synthesize new pages and query answers, and mark contradictions with contested frontmatter rather than silently resolving them. The task skill also supports source-to-task conversion with a coverage pass, while changelog generation synthesizes commit history into day-grouped prose. I did not find automatic decay or salience promotion.

### Trace-derived learning

**Trace source:** `session-logs` — `wiki_wrapup` treats the visible chat session as the source and mines it for durable claims, decisions, definitions, conventions, comparisons, workflows, and named entities.

**Learning scope:** `per-project` `cross-task` — The retained output lands in the discovered wiki for a project or user context and can guide later unrelated tasks in that scope.

**Learning timing:** `staged` — The trace is mined at session close/wrapup time, diffed against existing wiki state, presented as a proposal, and only written after user approval.

**Distilled form:** `prose` `symbolic` — The distilled output is prose wiki content with symbolic frontmatter, paths, page types, tags, links, source references, contradiction markers, index entries, and log entries.

**Trace source.** The qualifying trace is the active chat transcript visible to the agent. `wiki_wrapup` is deliberately session-only: it skips claims the session did not establish and ignores transient back-and-forth or private ephemera ([plugins/knowledge_management/skills/wiki_wrapup/SKILL.md](https://github.com/theafh/ai-modules/blob/14f42f58a898f6ae335920d2fb462b39cf61e71b/plugins/knowledge_management/skills/wiki_wrapup/SKILL.md)).

**Extraction.** Extraction is model-mediated and schema-constrained. The skill instructs the agent to orient on `SCHEMA.md`, `index.md`, and recent `log.md`, classify each candidate as NEW, EXTEND, CONFIRM, or CONFLICT, and include source-message references. The oracle is a combination of the acting model's judgment, the existing wiki's schema/index/search results, and user approval before writes.

**Scope and timing.** Learning is staged, not continuous. No code observes every tool call or action trajectory online. Instead, a user invokes wrapup near the end of a conversation, reviews the triage proposal, and approved writes route through the base wiki ingest/update flow, lint, and log entry.

**Survey relation.** `ai-modules` strengthens the survey category where trace-derived learning is not an autonomous memory daemon: a human-visible session transcript is mined into proposed durable prose, then governance gates decide what survives. It also splits raw trace retention from distilled behavior authority; the visible session is evidence, while approved wiki pages or procedures are the retained artifacts that later change behavior.

## Read-back

**Read-back:** `pull` — Retained wiki/task/changelog memory reaches the acting agent when a loaded skill instructs it to resolve paths, read `SCHEMA.md`, `index.md`, recent `log.md`, search files, and open selected pages. Host skill activation pushes the baseline procedure, but selected retained memory is not automatically injected by a memory service.

The main edge case is the plugin host. A deployed `SKILL.md` can be auto-selected by Claude, Codex, or another tool according to its trigger description, which is push-like for the instruction artifact itself. For this review's memory read-back verdict, that static skill instruction is the operating interface, not accumulated retained memory. The accumulated memory is the downstream wiki/task/changelog content, and the code-visible path to it is explicit file navigation.

Selection is index-first and file-search based. The wiki query flow reads `index.md`, runs recursive search for large wikis, reads relevant pages, synthesizes an answer with citations, and may file valuable answers back. The task query flow lists or searches `tasks/` and `tasks/archive/`. The changelog skill reads git-derived context and existing day sections. None of these paths exposes an embedding index, semantic top-k service, or situation-triggered memory injection.

Authority at consumption depends on the file read. A wiki concept page is advisory knowledge; a procedure page can become instruction; `SCHEMA.md`, `SKILL.md`, and lint scripts carry stronger system-definition and validation authority. Effective faithfulness is not tested in the repo: the code validates file shape and source drift, not whether a model actually obeyed the wiki page it read.

## Curiosity Pass

**The memory system is portable partly because it avoids a memory runtime.** There is no daemon, database, or model-side persistent state. That makes deployment easy and inspection strong, but every host still needs an agent capable of reading files and following the skill's procedure.

**The trigger descriptions are broad.** The `wiki` skill activates whenever the user mentions the wiki, knowledge base, or research notes in many ways. That improves adoption, but it can load a large procedural surface for ordinary questions before the actual retained wiki content is even selected.

**Session wrapup is trace-derived but approval-gated.** This is a useful middle ground: it avoids silently training on every conversation, but it also means learning depends on the user remembering to invoke wrapup and approve the proposal.

**Validation is mostly structural.** The wiki linter is substantial, and `wiki_auto_shaper` adds semantic audit instructions, but there is no retained per-claim review state comparable to Commonplace review gates. Contradictions are surfaced rather than resolved, which is the right direction but still leaves quality dependent on later human review.

**Deployment creates multiple consumption surfaces from one source.** Symlinked targets update with repo changes; copied/generated targets require redeploy. That split matters for memory authority because two host tools can be running different effective versions of the same skill after one edit.

## What to Watch

- Whether `wiki_wrapup` starts persisting a raw session snapshot or source-message ids alongside approved pages; that would make trace-derived lineage auditable after the chat disappears.
- Whether the wiki linter gains source-span or citation-resolution checks for generated pages; that would move wiki claims closer to Commonplace's code-grounded review discipline.
- Whether deployment metadata records which host has which plugin version installed; without that, multi-vendor adoption can drift from the repo source of truth.
- Whether `wiki_auto_shaper` grows a machine-readable review report; that would let autonomous repairs remain inspectable without reading every changed page.
- Whether any future retrieval layer is added to the wiki. Embedding or judgment-based push would change the read-back verdict from explicit pull toward targeted push, and would need faithfulness testing.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: stored wiki files affect behavior only when the skill's orientation/search path brings them into context.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: `wiki_wrapup` distills session traces into durable wiki candidates.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: `ai-modules` is an approval-gated session-to-wiki trace extraction system.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - aligns: wiki pages and changelog entries precompute source understanding so future sessions do not re-derive it from raw material.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: skills, manifests, wiki pages, raw sources, lints, logs, and deployment outputs carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, tasks, raw sources, summaries, and changelogs can advise future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `SKILL.md`, agent definitions, plugin manifests, schemas, deployment scripts, and lints shape or validate agent behavior.
