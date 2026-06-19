---
description: "LLM Wiki review: Claude Code command package for a Logseq/Obsidian wiki with L1 auto-loaded memory, L2 pull queries, schema rules, and lint gates"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# LLM Wiki (MehmetGoekce)

LLM Wiki, from `MehmetGoekce/llm-wiki`, is a Claude Code command package and setup script for maintaining a personal or team wiki in Logseq or Obsidian. At the reviewed commit it does not ship a separate application server, database, retrieval service, or MCP tool; its behavior is encoded in `wiki.md`, setup templates, documentation, and OpenSpec requirements that instruct Claude Code to ingest sources, query wiki pages, lint structure, and route knowledge between always-loaded Claude memory and an on-demand wiki.

**Repository:** https://github.com/MehmetGoekce/llm-wiki

**Reviewed commit:** [96ce7ad1ccec75c9100a71c7472c46ac41eb2825](https://github.com/MehmetGoekce/llm-wiki/commit/96ce7ad1ccec75c9100a71c7472c46ac41eb2825)

**Last checked:** 2026-06-04

## Core Ideas

**The system is a Claude Code command, not a standalone memory runtime.** `setup.sh` creates wiki scaffolding, writes `llm-wiki.yml`, and optionally copies `wiki.md` into a project's `.claude/commands/wiki.md`; the command file then describes `/wiki ingest`, `/wiki query`, `/wiki lint`, `/wiki status`, and `/wiki import` workflows for Claude Code to execute with its normal file tools ([setup.sh](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/setup.sh), [wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md)). The repository's executable implementation is mostly setup; the memory operations themselves are prompt-governed agent work.

**L1/L2 is the main context-efficiency mechanism.** The docs and command split retained knowledge into L1 Claude Code memory for always-needed rules, identity, and credentials, and L2 wiki pages for project history, workflows, research, and deep knowledge queried on demand ([docs/l1-l2-architecture.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/docs/l1-l2-architecture.md), [openspec/specs/l1-l2-routing.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/l1-l2-routing.md)). L1 is deliberately small and pushed by Claude Code's memory mechanism; L2 is bounded by command instructions such as reading only the top 3-5 pages and at most 3 pages simultaneously.

**The schema is the operational contract.** The generated schema pages define page types, required properties, cross-reference rules, format rules, lint rules, and the L1/L2 boundary for either Logseq or Obsidian; the command tells Claude to read the schema before operations and enforce format-specific page creation ([templates/logseq/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/logseq/Schema.md), [templates/obsidian/Schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/templates/obsidian/Schema.md), [openspec/specs/schema.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/schema.md)). The schema gives prose instructions enough symbolic structure for linting and consistent page generation.

**Writes are append-only wiki maintenance with optional L1 recommendations.** `/wiki ingest` instructs Claude to analyze a URL, file, or text source, extract entities/facts/relationships/dates/decisions, scan existing pages, create or append pages, add cross-references, update hubs, and run a quality gate; the L1/L2 routing spec says L1 candidates should be recommended rather than silently written into the wiki ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md), [openspec/specs/ingest.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/ingest.md), [openspec/specs/l1-l2-routing.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/l1-l2-routing.md)).

**Read-back is simple file search plus synthesis.** `/wiki query` tells Claude to parse a question, glob by namespace, grep keywords, read the top 3-5 pages, optionally consult L1 memory, then synthesize an answer with source attribution and staleness/confidence warnings ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md), [openspec/specs/query.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/query.md)). There is no vector store or learned ranker in the inspected repository.

**Quality checks are mostly specified agent behavior.** The lint spec names nine checks: orphans, stale high-confidence pages, missing properties, broken references, hub completeness, credential leaks, empty pages, cross-reference minimum, and L1/L2 duplicates. `wiki.md` tells Claude how to perform them and which fixes are allowed, but the repo does not contain a separate deterministic lint executable for those checks ([wiki.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/wiki.md), [openspec/specs/lint.md](https://github.com/MehmetGoekce/llm-wiki/blob/96ce7ad1ccec75c9100a71c7472c46ac41eb2825/openspec/specs/lint.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — L1 memory persists as Claude Code memory files at `memory_path`; L2 persists as Logseq or Obsidian Markdown files under the configured wiki path; setup can initialize git and commit the initial wiki state, but there is no database, vector store, or service object in the inspected repository.
- **Representational form:** `prose` `symbolic` — Wiki pages, command instructions, docs, examples, and source-derived notes are prose; page properties, YAML/frontmatter, Logseq property blocks, `llm-wiki.yml`, namespace conventions, lint rules, and OpenSpec requirements are symbolic constraints. I found no parametric representation such as embeddings or model weights.
- **Lineage:** `authored` `imported` — The command, specs, schema templates, and setup script are authored; wiki pages are created from imported URLs, files, inline text, existing notes, and manual edits. The repo does not show a durable agent-trace mining loop, so I am not marking it `trace-extracted`.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — L2 pages advise as knowledge; L1 memory and the `/wiki` command instruct Claude Code; credential boundaries, append-only rules, schema requirements, and lint checks enforce or validate; namespaces, page types, hubs, and the L1/L2 rule route writes and reads; grep/namespace matching plus top-page selection rank read-back; ingest and optional query write-back accumulate imported knowledge.

**Claude command file.** `wiki.md` is a system-definition artifact: it defines the role, context, workflows, constraints, and command modes that future Claude Code sessions follow. Its operative content is prose instruction plus symbolic command names, phases, limits, and file-format rules.

**L1 memory files.** L1 files are outside the git-tracked wiki, configured through `memory_path`, and are meant to be auto-loaded by Claude Code every session. Their content is usually concise prose with high prompt authority: rules, gotchas, identity, and credentials that should affect action before any query.

**L2 wiki pages.** L2 pages are Logseq or Obsidian Markdown with required properties and cross-references. They are knowledge artifacts during query, and become stronger system-definition artifacts when their properties, links, hub membership, or confidence/staleness fields drive search, lint, routing, or update decisions.

**Schema and lint rules.** The schema pages and OpenSpec files are durable constraints over the wiki surface. They do not execute independently, but they shape Claude Code's future writes and validations by defining valid types, required fields, namespace depth, cross-reference minimums, credential patterns, and auto-fix boundaries.

**Promotion path.** LLM Wiki has an explicit L2-to-L1 conceptual promotion path: repeated or high-consequence gotchas should become L1 memory; stale or historical L1 content can be demoted to L2. The inspected implementation records this as command/spec guidance and lint suggestions, not as an independently implemented promotion engine.

## Comparison with Our System

LLM Wiki and Commonplace both use Markdown files, schema-like conventions, links, and validation language to make a knowledge base agent-operable. The difference is where authority sits. Commonplace encodes type contracts, validation, indexes, review workflows, and generated artifacts inside a repository with deterministic Python commands. LLM Wiki mostly delegates operation to Claude Code following a command prompt and wiki schema, with `setup.sh` as the only substantial executable surface.

The L1/L2 split is sharper than Commonplace's ordinary navigation model. LLM Wiki explicitly says some retained memory should be pushed into every session because missing it would be dangerous or embarrassing, while broader context stays behind `/wiki query`. Commonplace usually relies on the active agent to search indexes, links, and notes, plus whatever instructions are loaded by the harness.

The tradeoff is verification. LLM Wiki is easy to adopt because it fits existing Claude Code, Logseq, Obsidian, and git habits; its memory behavior is also harder to test because the key operations depend on a live LLM faithfully following prose instructions. Commonplace is heavier, but deterministic validation and review gates give its artifacts more inspectable authority.

### Borrowable Ideas

**Explicit hot/cold memory routing.** Ready now as vocabulary. Commonplace could name "always-loaded" versus "pull-only" artifacts more explicitly when deciding which instructions, workshop notes, or warnings belong in session context.

**Credential boundary as a first-class lint rule.** Ready now if Commonplace ever stores operational project knowledge. LLM Wiki's rule that secrets belong only in git-excluded L1 memory is a crisp security boundary.

**Schema page as agent-facing writing contract.** Already aligned with Commonplace's `COLLECTION.md` and type specs, but LLM Wiki's generated in-wiki schema is a useful adoption pattern for small KBs that do not need a Python validator yet.

**Do not borrow prompt-only lint for durable governance.** Commonplace should keep deterministic validation for required metadata, link health, and generated indexes; prose-only lint is useful as guidance but too weak as a repository gate.

## Write side

**Write agency:** `manual` `automatic` — Users choose sources, invoke commands, approve optional write-back, and can edit wiki pages manually; Claude Code is instructed to perform automatic source extraction, page creation, append-only updates, hub updates, cross-reference insertion, lint scanning, selected lint auto-fixes, and git commits within those user-triggered commands.

**Curation operations:** `evolve` `synthesize` `invalidate` — Ingest appends new facts to existing pages and updates hubs/cross-references; query can synthesize a useful answer from multiple pages and offer to save it as a new page; lint can downgrade stale high-confidence pages and flag L1/L2 duplicates or credential leaks. Source acquisition and index/search scans are not counted as curation operations.

The automatic side is agent-executed rather than service-executed: I found instructions and specs for these operations, but not a separate implementation that deterministically parses pages and applies the rules without Claude Code.

## Read-back

**Read-back:** `both` — L1 Claude Code memory is designed as push memory that is present every session, while L2 wiki knowledge is retrieved through explicit `/wiki query` and file reads.

**Read-back signal:** `coarse` — The push path is coarse always-load of L1 memory. Namespace, keyword, confidence, and staleness signals are used after the agent invokes L2 query, so they classify the pull path rather than targeted push.

**Faithfulness tested:** `no` — The repository contains specs and examples for desired behavior, but I did not find tests or evaluations showing with/without memory effects on Claude Code behavior.

**Direction edge cases.** Static `wiki.md` command instructions are shipped baseline behavior, not accumulated memory read-back. L1 memory files count because they are retained user/project memory intended to be auto-loaded. L2 wiki pages are pull-only because Claude Code must decide to glob, grep, and read them during `/wiki query` or related workflows.

**Selection, scope, and complexity.** L2 query is bounded by simple symbolic and lexical heuristics: parse the question, select candidate namespaces/entities, grep keywords, read the top 3-5 pages, and batch at most 3 pages simultaneously. Actual precision and context dilution are not verifiable from the repository alone.

**Authority at consumption.** L1 has high prompt authority because it is present before action. L2 query results have advisory authority as cited source pages. Schema and lint outputs can become stronger when the agent treats them as blocking rules, especially for credentials and missing required properties.

**Other consumers.** Humans read and edit the Logseq or Obsidian graph, dashboard, hubs, and backlinks. Git history, setup-generated files, and optional commits make the wiki inspectable outside Claude Code.

## Curiosity Pass

**The strongest design idea is not the wiki.** The L1/L2 routing rule is the distinctive part: it treats context loading as a consequence-management problem rather than a generic retrieval problem.

**The repo's claims are more operational than executable.** The README says `/wiki lint` finds stale pages and credential leaks, but the inspected files implement that as Claude Code command guidance and OpenSpec requirements, not as a standalone lint binary.

**Append-only updates reduce overwrite risk but can accumulate contradiction.** Existing content is never overwritten, which is safer for LLM editing, but stale or contradicted claims need lint/review discipline to avoid becoming a long page of unmerged history.

**Logseq is a good fit for agent writes.** Its block structure makes appending and addressing smaller units easier than free-form Markdown, while Obsidian improves manual editing ergonomics.

**L1 credential handling is pragmatic but high risk.** Putting credentials in auto-loaded memory avoids git leaks, but it also gives them prompt-level exposure in every session that loads that memory.

## What to Watch

- Whether `/wiki lint` becomes a deterministic executable; that would materially strengthen schema and security enforcement beyond prompt-following.
- Whether query gains a real retrieval layer or remains glob/grep plus model judgment; this determines how well L2 scales past the stated 50-200 page target.
- Whether L1 promotion/demotion gets an auditable workflow with provenance, not just recommendation text.
- Whether optional query write-back gains a review state before creating durable pages from synthesized answers.
- Whether tests are added for setup, template generation, and representative command workflows; currently the OpenSpec files are stronger than the executable verification surface.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: LLM Wiki's L1 memory is pushed into sessions, while L2 wiki pages require explicit query/read work.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: L1 memory files, L2 wiki pages, schema pages, command instructions, and lint rules differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: L2 wiki pages mainly serve as evidence and reference during query.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: `wiki.md`, schemas, routing rules, lint rules, and setup templates shape future agent behavior.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: LLM Wiki's retrieval depends on namespaces, page names, properties, links, and keywords being available as symbols.
