---
description: "Funes review: Git-native Librarian protocol for raw-source preservation, compiled Markdown wiki memory, outputs, and health-check governance"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Funes

Funes, from `ulyssestenn/funes`, is a repo-template knowledge-base system for an AI "Librarian." It gives an external coding/chat agent a protocol for preserving raw sources, compiling them into an interlinked Markdown wiki, answering questions from that wiki with citations, writing reusable outputs, and periodically auditing the library. At the reviewed commit, Funes is not an application, daemon, vector service, or MCP server; the behavior-shaping implementation is the repository scaffold plus Markdown operating instructions that a host agent follows.

**Repository:** https://github.com/ulyssestenn/funes

**Reviewed commit:** [872d82f65119306739a6c7a761df5add0736d0df](https://github.com/ulyssestenn/funes/commit/872d82f65119306739a6c7a761df5add0736d0df)

**Last checked:** 2026-06-04

## Core Ideas

**Funes is a protocolized repo template, not a memory runtime.** The root `README.md` presents Funes as a way to turn folders of raw sources into a durable cited Markdown knowledge base maintained by an AI Librarian, and the repository contains the shared `AGENTS.md`, `protocol.md`, `library.md`, and an empty `starter-library/` scaffold rather than executable ingestion or retrieval code ([README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/README.md), [AGENTS.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/AGENTS.md), [protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [library.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/library.md)).

**The central memory shape is raw source -> compiled wiki -> durable output.** The protocol preserves `raw/` as the verbatim record, compiles each source into `wiki/sources/`, extracts atomic `wiki/concepts/`, organizes them through `wiki/topics/`, and writes substantial generated work to `outputs/` before filing durable parts back into the wiki ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md)). The starter library seeds exactly those directories plus `raw/INDEX.md`, `wiki/INDEX.md`, `meta/CHANGELOG.md`, and health-report space ([starter-library/README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/README.md), [starter-library/raw/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/raw/INDEX.md), [starter-library/wiki/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/wiki/INDEX.md)).

**Source preservation and abstraction are separated by directory authority.** Funes instructs the Librarian to never edit raw source content and to place all summarization, concept extraction, linking, topic mapping, and reusable synthesis above it in the wiki and outputs layers ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/raw/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/raw/INDEX.md)). That makes lineage inspectable in ordinary files, but claim-level fidelity still depends on the acting agent because there is no deterministic citation or extraction checker in the reviewed repository.

**Context efficiency comes from compiled navigation and selective file reading.** Funes does not do top-k vector retrieval, learned ranking, token budgeting, or progressive source expansion in code. It controls future context by frontloading raw-source interpretation into summaries, concepts, topic maps, and indexes, then instructing Q&A to search the wiki first through `wiki/INDEX.md`, source notes, concepts, and citations instead of re-reading raw sources on every question ([README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/README.md), [protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/wiki/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/wiki/INDEX.md)).

**Governance is instruction-level and git-native.** The design leans on plain Markdown, relative links, bidirectional backlinks, source registries, a master wiki index, an append-only changelog, and dated health reports for broken links, duplicate concepts, stale indexes, contradictions, gaps, and possible new articles ([README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/README.md), [protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/AGENTS.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/AGENTS.md)). Those are adoption-friendly affordances, but the checkout has no schema validator, lint script, citation resolver, or review-state mechanism.

## Artifact analysis

- **Storage substrate:** `repo` - The behavior-shaping state lives in a Git-tracked Markdown repository: root protocols, per-library `AGENTS.md`, raw sources, wiki pages, outputs, indexes, changelogs, and health reports. Files are the material representation, but Git versioning, portability, diffs, and library folders are part of the system's explicit storage model.
- **Representational form:** `prose` `symbolic` - The Librarian protocol, source summaries, concept articles, topic maps, outputs, changelogs, and health reports are prose; directory roles, frontmatter fields, status values, index tables, slugs, link conventions, and the raw/wiki/output/meta layout are symbolic. I found no retained vector index, database schema, or model-weight adaptation.
- **Lineage:** `authored` `imported` - Protocol files, library instructions, indexes, topic/concept/source pages, and outputs are authored by humans or the Librarian; raw files and pasted/linked materials are imported source material. The reviewed repo does not implement durable extraction from session logs, tool traces, or trajectories.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` - Raw sources, source notes, concepts, topics, outputs, and health reports advise later work as knowledge; `AGENTS.md` and `protocol.md` instruct the Librarian; indexes, folders, backlinks, and topic maps route lookup; health-check reports and source registries provide audit/validation authority at the protocol level.

**Root protocol artifacts.** The root `AGENTS.md` tells agents what the repository is and points them to `protocol.md` and `library.md`; `protocol.md` specifies ingest, compile, Q&A, output, health-check, naming, linking, frontmatter, and template conventions; `library.md` specifies how new top-level libraries are created. These are authored prose and symbolic layout contracts with instruction and routing authority over future agents ([AGENTS.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/AGENTS.md), [protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [library.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/library.md)).

**Library scaffold.** A library is a top-level folder with its own `AGENTS.md`, `README.md`, `raw/`, `wiki/`, `outputs/`, and `meta/` subtrees. The scaffold is symbolic routing plus prose orientation: it tells the acting Librarian which store is immutable, where compiled memory belongs, where substantial outputs go, and where health/changelog state is retained ([starter-library/AGENTS.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/AGENTS.md), [starter-library/README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/README.md)).

**Raw source registry.** `raw/INDEX.md` is an imported-source ledger with ids, title, type, added date, status, and description. Its authority is source governance: it records what has entered the library and whether it is raw or compiled, but it does not itself retrieve or rank content ([starter-library/raw/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/raw/INDEX.md)).

**Compiled wiki pages.** Source notes, concept articles, topic maps, and `wiki/INDEX.md` are the standing retained memory. They are prose knowledge artifacts with symbolic frontmatter, filenames, tags, relative links, and section templates. Their lineage is imported raw source or Librarian-authored synthesis over wiki material; their behavioral authority is advisory context and navigation for later Q&A, outputs, and health checks ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/wiki/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/wiki/INDEX.md)).

**Outputs and maintenance reports.** `outputs/` holds generated reports, analyses, routines, reading plans, and answers, while `meta/CHANGELOG.md` and `meta/health/` record changes and audits. These are knowledge artifacts until durable findings are filed into the wiki; the health reports carry weak validation authority by surfacing broken links, duplicates, contradictions, gaps, and stale indexes for follow-up ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/outputs/README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/outputs/README.md), [starter-library/meta/CHANGELOG.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/meta/CHANGELOG.md), [starter-library/meta/health/README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/meta/health/README.md)).

Promotion path: imported raw source becomes a source note, extracted concepts, topic maps, and possibly durable outputs. That is a promotion from source evidence to compiled knowledge and navigation, but not to executable enforcement. Funes has no implemented path from wiki claim to symbolic validator, hard gate, or model training artifact.

## Comparison with Our System

| Dimension | Funes | Commonplace |
|---|---|---|
| Primary purpose | Template for AI-maintained personal or research libraries | Methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Git-tracked Markdown libraries with raw/wiki/outputs/meta folders | Typed Markdown artifacts, source snapshots, indexes, schemas, reviews, and Python commands |
| Write path | Librarian follows protocol to ingest, compile, link, answer, output, and health-check | Agent/human writes governed by collection contracts, type specs, validators, review workflows, and generated indexes |
| Read-back | Acting Librarian pulls wiki pages, concepts, topics, and outputs when answering or producing work | Mostly explicit pull through `rg`, indexes, links, skills, commands, and loaded instructions |
| Governance | Raw immutability, indexes, backlinks, changelog, health reports, Git diffs | Stronger schema validation, citation/source review, semantic gates, replacement lifecycle, generated navigation |

Funes and Commonplace share the strongest architectural instinct: durable Markdown beats repeatedly asking an LLM to rediscover structure from raw material. Both systems treat files, links, indexes, and Git history as part of the memory machinery rather than incidental storage.

The divergence is contract strength. Funes is intentionally light: it can be adopted by cloning a template and pointing an agent at it. Commonplace is heavier because it makes collection routing, type contracts, validation, review status, source snapshots, and replacement history explicit. Funes is easier to start; Commonplace is more inspectable when the library itself must support repeated agent work under a quality bar.

The second divergence is automation evidence. Funes describes an agent-operated workflow but ships no code that ingests, validates, searches, ranks, or checks citations. Commonplace's commands and validators make more of the workflow reproducible outside a single agent's compliance with prose instructions.

### Borrowable Ideas

**Make the raw -> compiled -> output loop obvious to new users.** Ready now as documentation influence. Funes' three-layer diagram is a compact onboarding shape for explaining why raw sources, compiled notes, and generated outputs should not collapse into one folder.

**Keep starter libraries nearly empty.** Ready when Commonplace supports downstream project templates. Funes avoids over-seeding a user's library with methodology content, which lowers adoption friction for non-framework users.

**Use per-library `AGENTS.md` as a small scope contract.** Ready for downstream KBs. The starter library's `AGENTS.md` keeps local scope and deviations close to the library while referring to the shared protocol for behavior.

**Do not borrow prose-only health checks as the final governance layer.** Funes' health-check categories are useful, but Commonplace should keep deterministic validation and semantic review artifacts wherever maintenance reports can cause durable changes.

## Write side

**Write agency:** `manual` `automatic` - Humans add sources and ask questions; the Librarian agent writes raw captures, registry rows, source notes, concepts, topics, indexes, outputs, changelog entries, and health reports by following the protocol. The automatic side is protocol-driven agent operation after invocation, not a resident daemon, deterministic script, or scheduled learner.

**Curation operations:** `consolidate` `dedup` `synthesize` - At the protocol level, Funes instructs the Librarian to consolidate sources and concepts into summaries/topic maps, merge duplicate concepts rather than duplicate them, and generate syntheses and durable outputs from the wiki. Health checks can surface contradictions and stale material, but the reviewed checkout does not implement retained-history invalidation.

Funes does not qualify as trace-derived learning under the current review contract. It can preserve pasted text, links, and source material, and the Librarian may write outputs from a work session, but I found no implemented durable derivation from session logs, tool traces, event streams, repeated trajectories, rollouts, model feedback, or usage telemetry. Its learning path is source import and agent-authored compilation, not trace-derived memory.

## Read-back

**Read-back:** `pull` - Retained library memory reaches the acting Librarian when it deliberately reads `wiki/INDEX.md`, source notes, concept pages, topic maps, or outputs while answering a question, compiling a report, or running a health check. The root protocol is baseline instruction; it does not automatically inject accumulated wiki memory into a future model call.

Selection is file- and index-shaped. The Q&A workflow tells the Librarian to search the wiki first, follow the index/source/concept structure, answer with relative-link citations, and say plainly when the library does not cover the question ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md)). There is no embedding index, keyword ranker, top-k budget, always-load memory bundle, situation trigger, or identifier-based push path in the reviewed repository.

Authority at consumption is advisory unless the loaded page is a protocol or local `AGENTS.md`. A concept page can inform an answer; a source note can provide evidence; a topic map can route navigation; the shared protocol and library instruction file tell the Librarian how to behave. Effective faithfulness is not tested by the system: there is no with/without-memory ablation, post-answer audit, or citation-resolution check proving the agent used the loaded memory correctly.

Other consumers are first-class. Funes is deliberately readable from GitHub or any editor, so humans can browse raw sources, wiki notes, outputs, changelog entries, and health reports without a special app ([README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/README.md)).

## Curiosity Pass

**The most important implementation is social, not technical.** Funes makes the agent "own the wiki" and asks the human to supply sources and questions. That can work well with a capable coding agent, but it means correctness depends on host-agent behavior rather than a local executable pipeline.

**The raw layer is stronger than the compiled layer.** The instruction not to edit raw material is crisp and easy to audit in Git. The compiled wiki's summaries, concepts, links, and topic maps have weaker protection because no checker verifies source support, duplicate detection, or backlink completeness.

**The name's design claim is apt.** Funes explicitly separates remembering everything from abstracting it into usable concepts. The repo implements that distinction structurally through directories and templates rather than through a retrieval model.

**Many-library support is cheap because each library is isolated.** Top-level folders can share one protocol while keeping scope and links self-contained. That avoids accidental cross-domain sprawl, but it also means cross-library synthesis requires explicit human instruction.

## What to Watch

- Whether Funes adds deterministic helpers for ingest, link checking, source-registry updates, backlink checks, or citation validation; that would move governance beyond prose compliance.
- Whether the example library becomes rich enough to inspect actual Librarian outputs against the protocol; this review only covers the template and instructions.
- Whether health reports gain machine-readable status fields or a review lifecycle; that would make audits easier to compare across libraries.
- Whether Funes adds retrieval tooling, MCP surfaces, or automatic context assembly; that would change the read-back verdict and require push-specific faithfulness analysis.
- Whether source-to-concept compilation gains preserved source spans or claim ids; without them, the raw layer is preserved but individual compiled claims remain hard to audit.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Funes stores wiki memory, but accumulated memory acts only when the Librarian reads it.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - aligns: Funes frontloads source interpretation into compiled source notes, concepts, topics, and outputs.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw files, wiki pages, indexes, protocols, outputs, changelogs, and health reports carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, source notes, concepts, topics, outputs, and health reports advise future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `AGENTS.md`, `protocol.md`, folder contracts, index conventions, templates, and health-check rules shape agent behavior.
