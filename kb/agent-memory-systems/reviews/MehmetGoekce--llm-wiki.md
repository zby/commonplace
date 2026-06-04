---
description: "Claude Code slash-command wiki scaffold with Logseq/Obsidian schemas, L1/L2 routing doctrine, setup templates, and prompt-governed lint/query workflows"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# LLM Wiki (MehmetGoekce)

LLM Wiki, by Mehmet Goekce, is a Claude Code-oriented implementation scaffold for Karpathy's LLM Wiki idea. At the reviewed commit it is not a Python service or vector memory system; its operative implementation is a `/wiki` slash-command prompt, an interactive `setup.sh` installer, Logseq/Obsidian schema templates, config, examples, docs, and OpenSpec requirements that tell Claude how to ingest sources, query wiki pages, lint structure, and maintain a two-layer L1/L2 memory boundary.

**Repository:** https://github.com/MehmetGoekce/llm-wiki

**Reviewed commit:** [96ce7ad1ccec75c9100a71c7472c46ac41eb2825](https://github.com/MehmetGoekce/llm-wiki/commit/96ce7ad1ccec75c9100a71c7472c46ac41eb2825)

**Last checked:** 2026-06-02

## Core Ideas

**The system is a prompt-installed wiki maintainer, not a standalone runtime.** `setup.sh` asks for Logseq or Obsidian, wiki path, namespaces, optional Claude memory path, and optional project path; then it creates schema, dashboard, hub pages, `llm-wiki.yml`, and copies `wiki.md` into `.claude/commands/wiki.md` ([setup.sh](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/setup.sh), [wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md)). There is no separate query engine, indexer, or deterministic linter implementation beyond this shell installer and Claude command specification.

**L1/L2 is the central context-efficiency doctrine.** L1 is Claude Code memory: small, auto-loaded rules, gotchas, identity, and credentials. L2 is the Logseq/Obsidian wiki: larger project, workflow, research, and reference knowledge loaded on demand by `/wiki query`. The design aims to keep always-loaded context under roughly 10-20 concise memory files while limiting query-time wiki reads to the top 3-5 relevant pages, with at most three pages loaded simultaneously ([docs/l1-l2-architecture.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/l1-l2-architecture.md), [openspec/specs/query.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/query.md)).

**The wiki schema is the behavior contract.** Setup installs different templates for Logseq and Obsidian, but both encode the same page types, required properties, namespace rules, cross-reference rules, L1/L2 boundary, ingest workflow, and lint rules. Logseq uses `property:: value` outliner blocks and flat `Wiki___...md` filenames; Obsidian uses YAML frontmatter and folder hierarchy under `Wiki/` ([templates/logseq/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/logseq/Schema.md), [templates/obsidian/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/obsidian/Schema.md), [docs/schema-reference.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/schema-reference.md)).

**Ingest is append-only, cross-linking, and quality-gated by instruction.** `/wiki ingest` tells Claude to analyze a URL/file/text source, extract entities and decisions, route quick rules to L1 recommendations, scan the wiki, create or append to 5-15 pages, update hubs, add cross-references, check credentials, and report changes ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md), [openspec/specs/ingest.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/ingest.md)). The append-only rule is strong in the prompt and specs, but enforcement depends on the agent following the command text.

**Query is deliberate pull over files, not retrieval middleware.** `/wiki query` parses the question, glob/grep searches namespace pages, reads the top matching pages in small batches, optionally reads L1 memory when operational gotchas may apply, and synthesizes an attributed answer. There is no implemented event hook that pushes selected wiki pages into a receiving agent context before arbitrary actions ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md), [openspec/specs/query.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/query.md)).

**Governance is mostly prose-plus-template, with setup-time shell automation.** The README and OpenSpec files describe nine lint rules, including orphan detection, staleness, missing properties, broken references, hub completeness, credential leaks, empty pages, cross-reference minimums, and L1/L2 duplicates. In the reviewed source these are expressed in `wiki.md`, schema templates, and specs; there is no checked-in deterministic `llm-wiki lint` executable that independently enforces them ([openspec/specs/lint.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/lint.md), [README.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/README.md)).

## Artifact analysis

- **Storage substrate:** `files` — `wiki.md` in the source repository and the copied `.claude/commands/wiki.md` in a target project
- **Representational form:** `prose` `symbolic` — prescriptive prose in prompts, specs, schemas, and examples, plus symbolic YAML, frontmatter/properties, shell, links, namespaces, and command/config structure
- **Lineage:** `authored` `imported` — authored prompts, specs, templates, and setup code are installed into a target wiki; L2 wiki pages may be manually imported, setup-created, or generated/appended from source material by `/wiki` workflows
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` — L2 pages advise query answers; command prompts, schemas, config, namespaces, links, and lint expectations instruct Claude, route artifacts, validate structure, and rank/query candidate pages

**`/wiki` command prompt.** Storage substrate: `wiki.md` in the source repository and the copied `.claude/commands/wiki.md` in a target project. Representational form: prescriptive prose with command syntax, workflow phases, constraints, and tool-format rules. Lineage: authored in the repo, copied by `setup.sh`, and patched only for config path substitution. Behavioral authority: system-definition artifact with instruction and routing force for Claude Code when the slash command is invoked.

**Installed wiki config and templates.** Storage substrate: `llm-wiki.yml` in the wiki root and generated Schema/Dashboard/Hub files in the Logseq graph or Obsidian vault. Representational form: symbolic YAML plus prose/symbolic Markdown schema. Lineage: generated from `config.example.yml`, selected setup answers, and `templates/logseq/` or `templates/obsidian/`; invalidated by namespace, tool-mode, or path changes. Behavioral authority: system-definition artifacts because they route file format, namespace discovery, required properties, lint expectations, and L1/L2 boundaries.

**L2 wiki pages.** Storage substrate: Logseq `pages/Wiki___*.md` files or Obsidian `Wiki/**/*.md` files, usually git-tracked. Representational form: mixed prose plus symbolic properties/frontmatter and `[[Wiki/...]]` links. Lineage: imported manually, created by setup, or generated/appended by `/wiki ingest`, `/wiki import`, `/wiki lint --fix`, and query write-back when the user confirms. Behavioral authority: primarily knowledge artifacts when read during query, ingest, status, and lint; their frontmatter and links also have routing/ranking/evaluation force for command workflows.

**L1 Claude memory files.** Storage substrate: an external Claude Code memory directory referenced by `memory_path` in config; examples live only as sample files in `examples/l1-memory-examples.md`. Representational form: concise prose rules, gotchas, identity notes, and credential references. Lineage: authored or manually promoted from discovered operational lessons; the repo recommends L1 storage but does not itself create, update, or inject these files except by recording the path. Behavioral authority: system-definition or high-authority advisory context when Claude Code auto-loads them, but that activation is provided by Claude Code's host memory mechanism rather than implemented by this repo.

**OpenSpec files.** Storage substrate: `openspec/project.md` and `openspec/specs/*.md`. Representational form: prescriptive prose with `SHALL`/`MUST` requirements, BDD scenarios, and acceptance criteria. Lineage: authored design and implementation contract for future development. Behavioral authority: system-definition artifacts for contributors and agents extending the repo, but not runtime enforcement for installed users unless an agent reads and follows them.

**Setup script.** Storage substrate: `setup.sh`. Representational form: symbolic shell plus embedded Python and template substitution. Lineage: authored installer. Behavioral authority: one-time scaffolding and packaging authority: it creates directories, config, schema/dashboard/hub pages, optionally initializes git, optionally installs the slash command, and optionally commits the initial wiki state.

The main promotion path is source material -> agent extraction -> L2 wiki page append/update -> later query synthesis. A separate recommended path routes dangerous or embarrassing operational facts to L1 memory, but the repository leaves actual L1 write/promotion to the user or host Claude memory workflow. This means the architecture is clear, but the strongest behavioral authority sits outside the repo's own implementation.

## Comparison with Our System

| Dimension | LLM Wiki (MehmetGoekce) | Commonplace |
|---|---|---|
| Primary purpose | Personal/team Claude Code wiki scaffold for Logseq or Obsidian | Agent-operated methodology KB with typed collections, source capture, validation, and review gates |
| Main retained artifacts | Claude slash-command prompt, generated schemas, L1 memory recommendations, L2 wiki pages | Typed Markdown notes, source snapshots, skills, type specs, reports, generated indexes |
| Runtime surface | Claude Code `/wiki` command plus setup-created files | `commonplace-*` commands, local skills, schemas, collection contracts |
| Context efficiency | L1/L2 split, JIT query, max three pages at a time, 3-5 page reads | Collection routing, indexes, lexical search, source snapshots, semantic review, explicit artifact lifecycle |
| Governance | Prompt/spec/schema lint rules and credential warnings | Deterministic validation, type specs, review runs, archived replacements, link conventions |
| UI substrate | Logseq or Obsidian as human-facing graph/vault | Git-native Markdown KB with generated indexes and reports |

The strongest alignment is file-native knowledge. Both systems prefer inspectable Markdown, explicit schemas, links, and git history over opaque vector-only memory. The strongest divergence is enforcement. Commonplace treats validation scripts, type specs, generated indexes, review runs, and archives as first-class machinery. LLM Wiki describes similar governance intentions, but most checks live in Claude prompt instructions and OpenSpec requirements rather than executable validators.

LLM Wiki's L1/L2 split is more concrete than Commonplace's current phrasing around always-loaded context versus library retrieval. It distinguishes operational guardrails that must be present before action from contextual knowledge that should stay out of the base prompt until queried. The repo also makes the adoption surface unusually practical: it meets users where their notes already live, with Logseq/Obsidian serialization and Claude Code memory.

**Read-back:** `both` — L1 memory is a coarse host-provided always-load path at session start, while L2 wiki pages and query-time L1 supplements enter through explicit `/wiki query` or command workflows using namespace/entity/keyword matching. The repo records the memory path and recommends L1/L2 routing, but it does not implement a relevance-gated memory push hook into a receiving agent/model context, so this does not warrant `push-activation`

**Read-back signal:** `coarse` — the only push path described in the review is host-provided always-load L1 memory at session start; L2 pages and query-time L1 supplements are explicit pull workflows.

**Read-back timing:** `pre-action` — host-loaded L1 memory is present at session start before the receiving Claude Code session acts.

**Faithfulness tested:** `no` — the review records no with/without ablation or post-action audit showing that loaded L1 memory changes downstream behavior.

This review does not mark the system `trace-derived`. A user may ingest chat transcripts or manually promote gotchas into L1, and the docs call feedback/gotchas first-class page types, but the source does not implement durable artifact derivation from session/tool/evaluation traces. Ordinary source ingestion and manual L1/L2 promotion advice are not enough for the trace-derived tag.

### Borrowable Ideas

**Explicit L1/L2 routing as a user-facing doctrine.** Ready now. Commonplace could sharpen its own distinction between always-loaded operational rules and query-time library knowledge, including explicit "dangerous or embarrassing without it" routing language for promotion decisions.

**Host-native wiki export targets.** Needs a concrete audience. Logseq/Obsidian support is not necessary for Commonplace's methodology repo, but a consuming-project template could borrow the dual serializer idea when human editing in an external graph tool matters.

**Schema as the first generated artifact.** Ready now. Setup creates schema, dashboard, and hub pages before any ingest. Commonplace already has type specs and collection contracts; the borrowable piece is making initial scaffold generation visibly establish the behavior contract before content growth.

**L1/L2 duplicate lint concept.** Worth borrowing with deterministic implementation. Commonplace could inspect overlaps between always-loaded instructions/skills and library notes to find stale duplicated rules, but it should do that as a report first rather than an automatic mutation.

**Append-only ingest target.** Borrow selectively. Append-only page updates reduce accidental deletion in personal wikis; Commonplace should retain replacement/review workflows for durable notes where synthesis quality matters more than preserving every incremental block.

**Do not borrow prompt-only governance as final enforcement.** LLM Wiki's specs are useful, but Commonplace should keep converting high-value checks into executable validators or review gates when artifacts carry system-definition authority.

## Curiosity Pass

**The advertised linter is mostly a command contract.** The README says `/wiki lint` finds orphans, stale content, broken references, and credential leaks, but the repository has no separate linter program. The lint behavior is an instruction set for Claude plus OpenSpec requirements.

**L1 is architecturally central but externally implemented.** The repo's most important memory claim depends on Claude Code memory loading. `setup.sh` asks for `memory_path`, schemas mention L1, and query may read L1 files, but the repo does not create or maintain those files.

**The installer uses git strongly but locally.** Setup can initialize git in the wiki and commit the initial scaffold, which fits the "wiki as durable artifact" story. Later command workflows only recommend commits or tell Claude to commit; they are not wrapped in a transaction.

**The Logseq/Obsidian split is more than display.** It changes file paths, property syntax, and append ergonomics, so the command prompt must keep format rules in context. This is adoption-friendly but adds a correctness burden to every agent run.

**OpenSpec raises the bar for future implementation.** The `SHALL`/`MUST` scenarios are clearer than most README roadmaps, and could become tests if the repo later adds deterministic tooling.

## What to Watch

- Whether `/wiki lint` becomes a real executable validator. That would move governance from prose authority toward symbolic enforcement and make the comparison with Commonplace materially stronger.
- Whether L1 promotion/demotion gains an implemented write path or review queue instead of recommendations only. That would change the system's artifact lifecycle and possibly its activation classification.
- Whether setup or the command layer starts instrumenting query frequency, page reads, or session events. That would reopen the `trace-derived` decision if those traces produce durable behavior-shaping artifacts.
- Whether Claude Code memory support changes its loading semantics. This repo's L1 model depends on host behavior outside the repository.
- Whether generated Logseq/Obsidian schemas diverge. The current promise is tool-agnostic behavior with serialization differences only; drift would make reviews of installed wikis harder.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: L2 wiki pages are stored knowledge until a query or command reads them.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - applies: the L1/L2 split is explicitly a context-budget mechanism.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: slash commands, schemas, L1 memory files, L2 pages, and OpenSpec specs have different substrates, forms, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: L2 wiki pages advise later agents when queried.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `wiki.md`, setup templates, schemas, and OpenSpec files instruct or constrain future agent behavior.
