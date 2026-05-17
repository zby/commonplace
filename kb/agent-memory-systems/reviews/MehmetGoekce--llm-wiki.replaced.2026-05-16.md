---
description: "Promptware LLM Wiki bootstrap kit for Claude Code with L1/L2 memory split, Logseq/Obsidian schemas, setup script, and OpenSpec requirements"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation]
tags: []
status: outdated
last-checked: "2026-04-29"
---

# MehmetGoekce/llm-wiki

> Replaced 2026-05-16. See [MehmetGoekce/llm-wiki](./MehmetGoekce--llm-wiki.md) for the current review.

Mehmet Goekce's llm-wiki is a Claude Code-centered bootstrap kit for building Karpathy-style agent-maintained personal wikis in Logseq or Obsidian. It is neither the promptware-oriented [nvk/llm-wiki](./llm-wiki.md) nor the executable ingestion/UI stack in [kenhuangus/llm-wiki](./kenhuangus--llm-wiki.md). This repo sits between them: it has a real installer, templates, config, architecture docs, and OpenSpec requirements, but the ingest/query/lint behavior is still executed by Claude following `wiki.md` instructions rather than by a deterministic runtime. Its strongest design contribution is the explicit L1/L2 split: always-loaded Claude Memory for operational rules, identity, and secrets; on-demand wiki pages for project, workflow, research, and reference knowledge.

**Repository:** https://github.com/MehmetGoekce/llm-wiki

**Reviewed commit:** https://github.com/MehmetGoekce/llm-wiki/commit/96ce7ad1ccec75c9100a71c7472c46ac41eb2825

## Core Ideas

**The installer materializes a wiki scaffold, not the whole system.** `setup.sh` prompts for Logseq or Obsidian, wiki path, namespaces, memory path, optional git initialization, and optional Claude Code command installation. It then renders schema, dashboard, and hub templates with Python stdlib string substitution and writes `llm-wiki.yml`. That gives users a concrete starting graph, but after setup the operational behavior belongs mostly to the Claude command file rather than to shell or Python code ([setup.sh](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/setup.sh), [config.example.yml](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/config.example.yml)).

**`/wiki` is a prompt-level runtime.** `wiki.md` defines the acting role, config-reading contract, tool-specific format rules, and workflows for ingest, query, lint, status, and import. The ingest path tells Claude to analyze sources, scan the existing wiki, create or append pages, add cross-references, run a quality gate, and report touched pages. The query path tells Claude to grep/glob pages and synthesize from the top matches. There is no checked-in executable implementation of those operations beyond the prompt instructions, so success depends on agent compliance and host-tool capability ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md)).

**The L1/L2 boundary is the main architectural idea.** The repo frames memory as a cache hierarchy: L1 is Claude Code Memory, auto-loaded every session, for rules, gotchas, identity, and credentials; L2 is a Logseq or Obsidian wiki queried on demand for projects, workflows, research, and deeper context. The routing rule is consequence-based: knowledge whose absence would cause dangerous, embarrassing, or operationally costly mistakes belongs in L1; knowledge whose absence merely requires more context belongs in L2. This is a clearer activation model than a generic "put everything in the wiki" design ([README.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/README.md), [docs/l1-l2-architecture.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/l1-l2-architecture.md), [openspec/specs/l1-l2-routing.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/l1-l2-routing.md)).

**The schema contract is duplicated across Logseq and Obsidian formats.** Both template sets define the same page roles: entity, project, knowledge, feedback, and hub. The Logseq version encodes them as outliner blocks and `property:: value`; the Obsidian version encodes them as YAML frontmatter and nested folders. This is pragmatic for adoption because it lets the user keep their note app, but it also means every schema change has two concrete representations to keep aligned ([templates/logseq/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/logseq/Schema.md), [templates/obsidian/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/obsidian/Schema.md), [docs/schema-reference.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/schema-reference.md)).

**OpenSpec turns promptware behavior into acceptance criteria.** The `openspec/` directory specifies config loading, setup, schema, ingest, query, lint, and L1/L2 routing in SHALL/MUST language with BDD scenarios. That is stronger than README-only promptware because it gives contributors a reviewable contract. But the repo explicitly uses manual verification rather than a test framework, and many requirements describe intended Claude behavior rather than code that can be run and asserted automatically ([openspec/project.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/project.md), [openspec/AGENTS.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/AGENTS.md), [openspec/specs/ingest.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/ingest.md), [openspec/specs/query.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/query.md), [openspec/specs/lint.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/lint.md)).

## Comparison with Our System

| Dimension | MehmetGoekce/llm-wiki | Commonplace |
|---|---|---|
| Primary shape | Bootstrap kit: installer, Claude command, templates, docs, specs | Living methodology KB with typed notes, reference docs, instructions, skills, scripts, and reviews |
| Knowledge substrate | User's Logseq or Obsidian graph plus Claude Memory | Repo-native markdown under `kb/` with collection-local contracts |
| Runtime enforcement | Prompt instructions plus manual OpenSpec scenarios; setup script is concrete | Deterministic validators and indexers plus semantic review bundles |
| Activation model | L1 auto-loaded memory versus L2 queried wiki | Always-loaded repo instructions, skills, indexes, search, and collection contracts |
| Schema model | Five wiki page types shared across two editor formats | Type specs per collection, frontmatter validation, and register-specific writing conventions |
| Retrieval | Agent `glob`/`grep` over wiki pages, with 3-page JIT loading limit | `rg`, descriptions, curated indexes, generated indexes, semantic links, and skills |
| Governance | Prompt-level append-only rules, credential boundary, lint checklist, OpenSpec SHALLs | Explicit note statuses, deterministic validation, review gates, and stronger source/review lifecycle |

The closest alignment is the activation claim: stored knowledge is not enough if the agent cannot load the right rule before the mistake. llm-wiki names this as L1/L2 cache hierarchy; commonplace expresses it through always-loaded instructions, skills, navigation indexes, and typed artifacts. The difference is enforcement. llm-wiki mostly relies on Claude reading `wiki.md` and doing the right file operations. Commonplace has more machinery around validation, indexes, review runs, and collection contracts.

The repo is stronger than the `nvk` LLM Wiki review on installability because `setup.sh` creates an actual starting graph and command file. It is much weaker than `kenhuangus/llm-wiki` on executable autonomy because there are no ingestion scripts, query engine, monitor loops, API, UI, or deterministic lint implementation.

## Borrowable Ideas

**Use L1/L2 language when explaining activation, but adapt the security model.** The consequence-based routing rule is a useful way to explain why some instructions must load before retrieval. Ready to borrow for methodology docs. The credentials example needs adjustment: storing secret references in always-loaded memory may be useful, but loading raw credentials into every agent session is a different risk profile than merely keeping them out of git.

**Ship a scaffolded starter graph for methodology adoption.** `setup.sh` lowers adoption friction by creating schema, dashboard, hubs, config, and the command surface in one flow. Commonplace could borrow the "first usable KB in minutes" pattern for consuming projects, while keeping generated files explicitly tied to type specs and validators.

**Treat promptware as spec-worthy.** The OpenSpec files are useful because they make prompt-level behavior reviewable: ingest, query, lint, and setup all get requirements and scenarios. Ready to borrow for promoted skills whose behavior is important but not fully executable yet.

**Keep note-app adapters shallow until there is a real write engine.** The Logseq/Obsidian split is practical, but maintaining two template dialects by hand will drift. If commonplace ever supports editor-specific output, the better version is probably one semantic schema with generated renderers or validators, not parallel handwritten contracts.

## Curiosity Pass

**The system is more concrete than a README but less concrete than its command table suggests.** `/wiki lint`, `/wiki query`, and `/wiki ingest` read like commands, but the checked-in implementation is a Claude command prompt. That still matters in a Claude Code environment, but it should be evaluated as host-executed promptware, not as a CLI with independent behavior.

**The L1/L2 metaphor usefully separates activation from storage.** The simpler alternative is "rules in memory, context in wiki." The cache metaphor earns its keep because it names latency and consequence, not just file location. The failure mode is that L1 can become a dumping ground if "embarrassing mistake" is interpreted too broadly.

**The lint layer is currently a contract, not a checker.** The docs specify orphan detection, stale-page checks, broken references, credential patterns, hub completeness, and L1/L2 duplicate checks. Those are the right checks, but at this commit they are instructions for Claude to perform rather than a script with reproducible outputs. This is a good requirements list for a future validator.

**"5-15 page touches per ingest" is a provocative heuristic.** It pushes against underspecified one-page capture and encourages cross-reference creation. It can also incentivize unnecessary spread if the source is genuinely narrow. The safer reading is "consider affected context deliberately," not "touch at least five files."

**The initial commit path uses broad staging.** `setup.sh` runs `git add -A` inside the user's wiki when making the optional initial commit. That is convenient for a freshly created vault, but it is risky in a pre-existing graph. A production installer should stage only the files it created or at least show the pending diff first ([setup.sh](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/setup.sh)).

**This does not yet qualify as trace-derived learning.** The feedback page type and L1 promotion story can represent lessons from experience, and the docs mention promoting repeated mistakes into memory. But the repo does not implement a trace capture, extraction, judging, or promotion loop over agent sessions. It is a schema and workflow that a human or agent could use for such lessons, not a trace-derived learning system itself.

## What to Watch

- Whether `/wiki lint` becomes a deterministic script rather than a Claude checklist.
- Whether ingest/query grow reusable helpers for config parsing, page discovery, schema validation, and link normalization.
- Whether OpenSpec scenarios become executable tests while preserving the zero-dependency goal.
- Whether L1 memory gets size, age, and usage maintenance beyond prompt instructions.
- Whether the Logseq and Obsidian templates stay behaviorally equivalent as the schema evolves.
- Whether the system adds a safer installer commit path for existing vaults.

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: the L1/L2 split is primarily an activation strategy, not just a storage split
- [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) - aligns: high-consequence rules move into always-loaded memory while deeper context stays query-time
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) - exemplifies: `/wiki` is a command-shaped instruction artifact with routing and workflow policy
- [Agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) - aligns: query and ingest both depend on narrowing the wiki to a few relevant pages
- [Stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) - warns: hub pages and dashboards are useful only if ingest/lint keep them current
- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - aligns: durable knowledge remains readable markdown in an existing note tool
- [LLM Wiki](./llm-wiki.md) - compares: both package LLM Wiki as promptware, but MehmetGoekce adds a setup script, L1/L2 architecture, editor templates, and OpenSpec contracts
- [kenhuangus/llm-wiki](./kenhuangus--llm-wiki.md) - compares: same Karpathy-inspired wiki premise, but kenhuangus ships a Python/React runtime while MehmetGoekce ships a Claude Code scaffold and prompt/spec layer
