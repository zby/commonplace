---
description: "Claude Code promptware scaffold for an L1/L2 Logseq or Obsidian wiki, with setup templates, slash-command workflows, schema, lint, and OpenSpec contracts"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# MehmetGoekce/llm-wiki

> Replaced 2026-06-02. See [MehmetGoekce--llm-wiki](./MehmetGoekce--llm-wiki.md) for the current review.

Mehmet Goekce's `llm-wiki` is a Claude Code promptware scaffold for building a Karpathy-style LLM-maintained wiki in Logseq or Obsidian. The repository is not a Python package, vector store, MCP server, or autonomous ingest daemon. Its implemented core is a Bash installer, markdown templates, one Claude Code `/wiki` command prompt, OpenSpec requirements, and documentation for a two-layer memory architecture: L1 Claude Code memory for always-loaded rules, gotchas, identity, and credentials; L2 Logseq/Obsidian wiki pages for on-demand project, workflow, research, and reference knowledge.

**Repository:** https://github.com/MehmetGoekce/llm-wiki

**Reviewed commit:** [96ce7ad1ccec75c9100a71c7472c46ac41eb2825](https://github.com/MehmetGoekce/llm-wiki/commit/96ce7ad1ccec75c9100a71c7472c46ac41eb2825)

**Last checked:** 2026-05-16

## Core Ideas

**The central design is an explicit L1/L2 authority split.** The README and architecture doc argue that some knowledge must be available before a query because the agent would otherwise already have made the mistake. L1 is Claude Code memory: small, auto-loaded, git-excluded, and appropriate for operational guardrails, identity, preferences, and credentials. L2 is a larger Logseq or Obsidian wiki queried with `/wiki` when context is needed. The routing question is consequence-based: dangerous or embarrassing mistakes go to L1; merely inconvenient missing context goes to L2 ([README.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/README.md), [docs/l1-l2-architecture.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/l1-l2-architecture.md), [openspec/specs/l1-l2-routing.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/l1-l2-routing.md)).

**The behavior lives mostly in a Claude Code command prompt.** `wiki.md` defines `/wiki ingest`, `/wiki query`, `/wiki lint`, `/wiki status`, and `/wiki import` as agent workflows. It tells Claude to read `llm-wiki.yml`, respect Logseq versus Obsidian formatting, keep credentials out of the wiki, load at most three wiki pages at a time, append rather than overwrite, add cross-references, run quality gates, and commit after structural changes. This makes `wiki.md` a system-definition artifact with instruction and routing authority; the generated wiki pages it reads and writes are mostly knowledge artifacts ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md)).

**The installer materializes a file-first substrate.** `setup.sh` checks for `python3` and `git`, prompts for Logseq or Obsidian, chooses a wiki path, creates namespace hub pages, renders Schema and Dashboard templates, writes `llm-wiki.yml`, optionally copies `wiki.md` into `.claude/commands/wiki.md`, and creates a best-effort initial git commit. The durable storage substrate after setup is a local wiki directory, optional git history, a generated config file, and optional Claude Code command installation. There is no separate runtime database; the only Python is stdlib template rendering inside the setup script ([setup.sh](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/setup.sh), [config.example.yml](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/config.example.yml), [openspec/specs/setup.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/setup.md)).

**Schema templates give generated pages a lightweight artifact contract.** The Logseq and Obsidian templates define namespace conventions, page types, required properties, cross-reference rules, content-format rules, the L1/L2 boundary, ingest workflow, and lint rules. The representational form is prose plus symbolic frontmatter or Logseq properties. Schema and hub pages are system-definition artifacts when Claude consumes them as rules for later writes; entity, project, knowledge, and feedback pages are knowledge artifacts unless promoted into L1 memory or otherwise consumed as binding instructions ([templates/logseq/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/logseq/Schema.md), [templates/obsidian/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/obsidian/Schema.md), [docs/schema-reference.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/schema-reference.md)).

**OpenSpec is the strongest formal surface, but it is a contract rather than implementation.** The repository contains seven OpenSpec files with requirements and BDD scenarios for ingest, query, lint, schema, config, setup, and L1/L2 routing. These documents are useful system-definition artifacts: they specify how a future implementation or Claude Code workflow should behave. They should not be mistaken for executable validators. At this commit, lint, query, and ingest are prompt-defined behaviors performed by Claude Code, not deterministic local commands with tests ([openspec/project.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/project.md), [openspec/specs/ingest.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/ingest.md), [openspec/specs/query.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/query.md), [openspec/specs/lint.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/lint.md), [openspec/AGENTS.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/AGENTS.md)).

**Lineage is mostly human/agent-maintained.** The `/wiki ingest` prompt requires source analysis, affected-page scanning, append-only updates, cross-references, updated dates, and a report; the examples show raw placeholder pages becoming synthesized wiki pages. That gives some lineage at page level through `source`, `created`, `updated`, git history, and source attribution in query output, but not source-span provenance, generated-page review state, or a deterministic regeneration path from original source to final page ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md), [examples/before-after.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/examples/before-after.md), [openspec/specs/ingest.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/ingest.md)).

## Comparison with Our System

| Dimension | MehmetGoekce/llm-wiki | Commonplace |
|---|---|---|
| Primary purpose | Claude Code scaffold for a personal/team Logseq or Obsidian wiki | Agent-operated methodology KB with typed collections, reviews, sources, ADRs, and instructions |
| Storage substrate | Claude memory files, wiki markdown files, `llm-wiki.yml`, git history, generated templates | Git-tracked markdown collections, type specs, source snapshots, generated indexes, validation/review reports |
| Representational form | Prose prompts, Logseq properties or YAML frontmatter, markdown pages, OpenSpec requirements | Prose plus structured frontmatter, authored links, type specs, CLI scripts, semantic review outputs |
| Lineage | Page-level dates/source fields, append-only convention, git commits, source attribution in query answers | Source snapshots, commit-pinned citations, status/lifecycle metadata, review replacement, validation and semantic gate reports |
| Activation | L1 auto-load, `/wiki query`, schema-guided Claude reads, Logseq/Obsidian backlinks | `rg`, generated indexes, authored links, skills, type contracts, validation and review workflows |
| Behavioral authority | Prompt instructions and schema/config guide Claude; L1 memory can directly constrain every session | Instructions, skills, type specs, validation, review findings, and notes carry differentiated authority |

The closest alignment is the belief that files and native tools are enough for a useful agent-operated KB. Both systems prefer inspectable markdown, git history, cheap lexical search, and agent-readable conventions over a hidden service. `llm-wiki` is more adoption-oriented: it meets users in Logseq or Obsidian and gives them a single `/wiki` command plus an installer.

Commonplace is stronger on artifact contracts and review lifecycle. `llm-wiki` distinguishes L1 and L2 well, but within L2 most behavior depends on Claude obeying prompt instructions and schema pages. Commonplace's path-valued type specs, validation scripts, review bundles, link vocabulary, and archive/replacement conventions create more friction, but they also make artifact authority easier to audit.

The most useful vocabulary split is knowledge artifact versus system-definition artifact. In `llm-wiki`, generated entity/project/knowledge pages are knowledge artifacts when queried as evidence or context. By contrast, `wiki.md`, `llm-wiki.yml`, OpenSpec requirements, Schema templates, lint rules, setup behavior, and L1 memory files are system-definition artifacts because Claude consumes them with instruction, routing, validation, or security-boundary force.

The system does not qualify as trace-derived learning at this commit. It can ingest URLs, files, inline text, or chat transcripts as sources, and the specs discuss promoting repeated gotchas from L2 to L1. But there is no implemented mechanism that mines agent session traces, tool trajectories, repeated task histories, or feedback logs into durable learned rules. The learning loop is an instructed human/Claude workflow, not a source-grounded trace-derived mechanism.

**Read-back:** both — L1 memory is always loaded, while L2 wiki pages are pulled through `/wiki query`.

## Borrowable Ideas

**Consequence-based hot/cold routing.** Ready to borrow as framing. The question "what happens if the agent does not know this before acting?" is a practical way to decide whether a retained artifact should be always-loaded instruction or on-demand context.

**Use the user's existing note substrate.** Ready as an adoption pattern. Logseq and Obsidian support backlinks, markdown, local files, and human editing. A scaffold that respects those conventions has lower setup cost than a custom KB UI.

**Generated Schema and Dashboard starter pages.** Useful for bootstrapping. Commonplace already has richer type specs, but new KBs could benefit from generated collection-local schema and dashboard pages that make first writes less ambiguous.

**Promptware plus OpenSpec as a lightweight product boundary.** Worth borrowing selectively. OpenSpec requirements make the intended behavior auditable even before every command is code. The risk is that requirements can drift from what the prompt and installer actually do.

**Do not borrow the prompt-only lint surface as sufficient governance.** `llm-wiki` specifies strong lint checks, but they are not deterministic local validators in the inspected repo. Commonplace should keep executable validation for structural guarantees and reserve LLM/agent review for semantic checks.

## Takeaways

**The L1/L2 split is the repo's real contribution.** The cache metaphor is more actionable than the LLM-wiki branding: behavior-changing guardrails need zero-query activation, while project history and research can stay in on-demand pages.

**Promptware can create behavioral authority.** Even without a package or service, `wiki.md` is a system-definition artifact. If Claude Code obeys it, it controls what is read, written, linked, linted, committed, and excluded from storage.

**Generated wiki pages need clearer lineage than the scaffold currently provides.** Dates, source fields, and git commits are useful, but they do not preserve enough derivation detail to regenerate or audit synthesized claims without rereading the original source.

**The security boundary is crisp and worth keeping.** Credentials are explicitly L1-only because the wiki is assumed git-tracked. That is a stronger, simpler rule than trying to classify secret wiki pages.

**The repo should be reviewed as scaffold plus doctrine, not as an autonomous memory engine.** Its authority comes from templates, prompts, and specs; many advertised behaviors depend on Claude's execution inside an installed project.

## Curiosity Pass

The installer contains a small drift signal: it patches a `<CONFIG_PATH>` placeholder into the copied command file, and troubleshooting tells users to verify that replacement, but the inspected `wiki.md` does not contain that placeholder. The command still tells Claude to read `llm-wiki.yml`, so this is not necessarily fatal, but it shows how promptware, docs, and installer scripts can diverge.

The docs mention migration automation between Logseq and Obsidian, but the inspected file list does not include a `migrate.sh` implementation. That is another example of promise-surface drift rather than core architectural failure ([docs/logseq-vs-obsidian.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/logseq-vs-obsidian.md)).

The strongest implemented code is `setup.sh`, not the ingest/query/lint loop. That matters for trust: setup page generation can be inspected line by line, while ingest/query/lint correctness depends on the live Claude session following the prompt and user confirmations.

## Open Questions

- Should `/wiki lint` become a deterministic local command so orphan, stale, missing-property, broken-link, credential, and L1/L2 duplicate checks are not left to prompt execution?
- How should generated wiki pages cite source spans, transcript excerpts, or file paths so a later agent can audit a synthesized claim?
- Should L1 memory promotion/demotion produce explicit review records, or is user confirmation inside Claude Code enough?
- How should concurrent Claude sessions coordinate writes beyond the README warning that parallel agents can conflict?
- Should schema pages distinguish knowledge artifacts from system-definition artifacts explicitly, especially for feedback pages that may become L1 rules?
- How should the scaffold handle drift between README claims, OpenSpec requirements, `wiki.md`, setup behavior, and troubleshooting docs?

## What to Watch

- Whether ingest, query, lint, and status become executable scripts with tests, or remain Claude Code prompt workflows.
- Whether the setup command gains non-interactive mode and safer git staging for team or CI use.
- Whether generated pages gain stronger source lineage, review status, and regeneration/invalidation rules.
- Whether L1/L2 duplicate and promotion signals are backed by actual usage traces rather than manual judgment.
- Whether Logseq/Obsidian migration support is implemented in code rather than only described in docs.

## Bottom Line

MehmetGoekce/llm-wiki is a useful Claude Code scaffold for turning Logseq or Obsidian into a two-layer agent memory surface. Its best idea is not retrieval technology but authority placement: keep always-needed, mistake-preventing rules in L1 and put deeper knowledge in an on-demand wiki. For commonplace, the main lesson is to preserve that activation distinction while adding stronger lineage, deterministic validation, and lifecycle controls before generated knowledge becomes trusted memory.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: `llm-wiki` needs separate treatment for L1 memory files, L2 wiki pages, schema templates, config, prompt commands, and OpenSpec requirements.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: generated entity, project, knowledge, and feedback pages primarily serve as evidence, context, or reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: `wiki.md`, Schema templates, lint rules, config, setup behavior, and L1 memory carry instruction, routing, validation, or security-boundary authority.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - aligns: the L1/L2 split is explicitly about loading critical guardrails before the agent acts.
- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - aligns: the scaffold keeps durable knowledge in markdown files and git rather than a service database.
