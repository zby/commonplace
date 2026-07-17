---
description: "Quicky Wiki review: document-derived SQLite claim graph with confidence events, metabolism, generated wiki files, and MCP pull tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Quicky Wiki

Quicky Wiki, from `anzal1/quicky-wiki`, is a TypeScript CLI/library for turning user-supplied documents and URLs into a local confidence-scored wiki. At the reviewed commit, it stores source records, pages, claims, links, confidence state, full-text indexes, and epistemic events in SQLite; renders Markdown and other export formats; serves a dashboard; and exposes MCP tools for explicit agent access.

**Repository:** https://github.com/anzal1/quicky-wiki

**Reviewed commit:** [65ef29b9dcc76237aa797a0d16c50bc8fd89baf7](https://github.com/anzal1/quicky-wiki/commit/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7)

**Source directory:** related-systems/anzal1--quicky-wiki

## Core Ideas

**The canonical store is a SQLite claim graph.** A project keeps config under `.quicky/config.yaml`, durable graph state under `.quicky/graph.sqlite`, raw sources under `raw/`, and generated pages under `wiki/` ([README.md](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/README.md), [src/cli/context.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/context.ts)). The database schema stores sources, pages, claims, dependencies, contradictions, page links, epistemic events, and FTS5 tables; rendered files are projections over that store rather than the maintained source of truth ([src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts), [src/render/markdown.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/render/markdown.ts)).

**Document ingestion is LLM extraction plus graph resolution.** `ingestSource()` reads Markdown/text or fetched URL material, parses frontmatter, hashes content, infers source type and quality, asks the configured LLM for atomic claims, chunks long inputs, de-duplicates chunk outputs by normalized statement prefix, diffs the new claims against existing ones, resolves reinforcements/challenges/new claims, updates page summaries, and re-renders wiki pages ([src/compiler/ingest.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/ingest.ts), [src/compiler/diff.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/diff.ts), [src/compiler/resolve.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/resolve.ts), [src/cli/ingest.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/ingest.ts)).

**Confidence is visible but heuristic.** Initial confidence is scaled by source quality; reinforcement uses a diminishing-return merge; challenges reduce confidence to 60% of the prior value; dependency cascades propagate damped confidence changes to dependent claims ([src/compiler/confidence.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/confidence.ts), [src/compiler/diff.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/diff.ts), [src/compiler/resolve.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/resolve.ts), [src/graph/cascade.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/cascade.ts)). The code preserves confidence state and events; it does not prove confidence is calibrated.

**Context efficiency is bounded lexical retrieval for ordinary questions.** `queryKnowledge()` searches SQLite FTS for up to 50 matching pages/claims, groups claims by page, and sends only confidence-marked claim lines to the answering LLM ([src/graph/query.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/query.ts), [src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts)). The multi-model consensus path is less bounded: it assembles context from all pages and all claims before cross-model comparison ([src/compiler/consensus.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/consensus.ts)).

**Metabolism turns graph maintenance into explicit queues.** Health reports identify stale, low-confidence, contested, and cascade-risk claims; decay can down-weight old claims; resurface asks an LLM for review questions and suggestions; red-team asks an LLM to critique high-confidence claims ([src/metabolism/health.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/health.ts), [src/metabolism/decay.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/decay.ts), [src/metabolism/resurface.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/resurface.ts), [src/metabolism/redteam.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/redteam.ts)). Only decay and explicit graph edits mutate confidence/content directly; red-team and resurface are advisory.

**The MCP surface is an explicit pull interface.** Quicky Wiki exposes tools for `query_wiki`, `search_wiki`, `get_page`, listing pages/entities/claims, health reports, ingestion, and metadata updates, over stdio or HTTP JSON-RPC ([src/mcp/server.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/mcp/server.ts)). The tools make the wiki accessible to agents, but this repository does not implement a host hook that automatically injects memory into an agent before it acts.

## Artifact analysis

- **Storage substrate:** `sqlite` `files` `graph` `in-memory` — `.quicky/graph.sqlite` is the central durable store; raw sources and rendered/exported outputs persist as files; the page/claim/link/dependency structure is graph-shaped even though implemented relationally; query contexts and dashboard caches are transient ([src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts), [src/cli/context.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/context.ts), [src/cli/serve.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/serve.ts)).
- **Representational form:** `prose` `symbolic` — source text, claim statements, summaries, answers, critiques, and rendered pages are prose; schema rows, IDs, hashes, FTS tables, confidence numbers, timestamps, event types, frontmatter, metadata JSON, and tool schemas are symbolic.
- **Lineage:** `authored` `imported` — user files, dashboard edits, configuration, and saved answers are authored; fetched URLs and local source material are imported; source records, extracted claims, summaries, confidence events, FTS indexes, wiki pages, and exports are compiled from those authored/imported inputs. The reviewed code does not create durable memory from agent session/action traces.
- **Behavioral authority:** `knowledge` `routing` `validation` `ranking` `learning` — claims, pages, sources, answers, health reports, and exports advise users or agents; pages, links, FTS, MCP tools, and query assembly route context; health/lint/metabolism surfaces validate or audit the graph; confidence and FTS order rank what is seen first; reinforcements, challenges, decay, and saved-answer ingestion learn by changing future graph state.

**Raw sources and source records.** Raw files and fetched URL Markdown are source knowledge artifacts. SQLite source records add symbolic provenance: path, title, type, quality tier, content hash, ingestion time, and metadata. Source quality influences initial confidence, and content hashes suppress unchanged re-ingestion.

**Claims, pages, links, and events.** The claim graph is the behavior-shaping artifact: prose claims are attached to pages and source records, symbolic links/dependencies/contradictions structure navigation and health checks, and epistemic events retain confidence changes. The graph is both a knowledge artifact and a system-definition artifact because search, confidence, and page grouping decide what can enter answers.

**FTS indexes and query contexts.** FTS5 tables are derived access structures maintained by SQLite triggers. `queryKnowledge()` turns lexical matches into bounded prompt context; precision/recall is not verifiable from static code.

**Generated wiki and export files.** Markdown wiki pages, Obsidian-compatible pages, slides, Anki decks, graph HTML, and timelines are compiled views. They are adoption affordances for humans and external tools, but the mutation path remains the SQLite graph unless a user treats an exported file as a new source.

**Configuration, dashboard, and MCP tools.** The JSON-written `config.yaml` controls provider/model, paths, quality weights, metabolism thresholds, kind rules, and entity prompts. Dashboard and MCP code expose read/write interfaces; their authority is interface-level, not a separate memory substrate.

Promotion path: authored/imported source material becomes source rows and LLM-extracted claim candidates; resolution promotes them into claims, page summaries, links, confidence events, and FTS state; compile/export promotes the graph into browseable files; `query --save` can turn a generated answer into a new raw source that may later be ingested. The code does not promote claims into reviewed notes, validators, or enforced prompt rules.

## Comparison with Our System

| Dimension | Quicky Wiki | Commonplace |
|---|---|---|
| Primary purpose | Compile arbitrary documents into a confidence-scored personal wiki/graph | Maintain a typed methodology KB for agents and maintainers |
| Canonical substrate | SQLite claim graph plus generated files | Git-tracked Markdown collections, types, sources, reports, indexes, and validation |
| Unit of memory | Atomic extracted claim attached to sources and pages | Typed artifact with frontmatter, prose argument, links, and status |
| Trust model | Quality multipliers, confidence scores, events, health reports, red-team/resurface suggestions | Source grounding, collection contracts, deterministic validation, review gates, git history |
| Read-back | Explicit CLI/dashboard/MCP/search/query pull | Mostly explicit pull through `rg`, indexes, links, skills, commands, and reviews |
| Lifecycle | Reinforce, challenge, cascade, decay, edit/delete, render/export | Draft, connect, validate, review, replace/archive, promote from workshop to library |

Quicky Wiki is closest to Commonplace at the boundary where source material becomes maintained knowledge. The difference is granularity. Quicky Wiki decomposes sources into claims and lets a database coordinate provenance, confidence, search, and outputs. Commonplace keeps whole artifacts readable, typed, and reviewable as prose.

That makes Quicky Wiki better for broad ingestion, dashboard exploration, and confidence-oriented maintenance queues. Commonplace is slower but stronger when the artifact's argument, caveats, source grounding, and replacement history must remain directly inspectable by agents and maintainers.

The trust tradeoff is important. Quicky Wiki has richer first-class confidence and temporal machinery than ordinary Commonplace notes, but its central extraction, diffing, and page-assignment steps are LLM-mediated and heuristic. It does not retain exact source spans per claim, extraction prompt/model metadata per claim, or a reviewed acceptance state before claims become answer context.

### Borrowable Ideas

**Health reports that produce action candidates.** Ready as a report pattern. Stale, contested, low-confidence, and cascade-risk queues would be useful in Commonplace if they point to reviewable artifacts rather than silently altering library notes.

**Epistemic events for structured claims.** Needs a concrete structured-claim workflow. A Commonplace analogue could track when a claim was created, reinforced, challenged, or decayed, and which source or review caused the change.

**Confidence as visible metadata, not an automatic trust oracle.** Ready for candidate/review layers. Confidence can help prioritize work, but Commonplace should not let an LLM-derived number substitute for source grounding and review gates.

**MCP as a narrow pull surface.** Ready conceptually. Quicky's tools expose bounded operations instead of dumping the whole store; a Commonplace MCP layer should follow the same shape.

**Do not borrow automatic document-to-claim promotion without review.** Automatic extraction is useful for workshop intake and exploration. Durable methodology claims should still pass through typed authoring, source checks, and semantic review before entering the library.

## Write side

**Write agency:** `manual` `automatic` — Users can author files, run ingestion, save answers, edit/delete claims and pages through the dashboard, update entity metadata, and compile exports; the system automatically extracts claims, diffs them against existing claims, reinforces/challenges confidence, assigns pages, summarizes pages, maintains FTS, applies decay, and renders outputs.

**Curation operations:** `consolidate` `evolve` `invalidate` `decay` — page summary generation condenses stored claims into shorter page-level summaries; reinforcement, dashboard edits, and metadata updates evolve existing graph entries; challenges lower confidence and retain events; metabolism decay down-weights old claims. Chunk de-duplication and document-to-claim extraction are acquisition mechanics rather than curation operations over already-retained memory.

Quicky Wiki is not trace-learning under the survey rule. Its durable artifacts derive from user-authored/imported documents, fetched URLs, dashboard edits, and optionally saved generated answers, not from agent session logs, tool/action traces, event streams, repeated trajectories, or rollouts.

## Read-back

**Read-back:** `pull` — Retained memory reaches agents and users through deliberate CLI queries, dashboard API calls, FTS search, generated files, MCP tool calls, health reports, and explicit compile/export operations. I did not find a task-aware host hook, always-load memory injection, or event listener that pushes graph memory into an agent before it acts.

## Curiosity Pass

**The config file is YAML-named but JSON-parsed.** `CONFIG_FILE` is `config.yaml`, while `loadConfig()` uses `JSON.parse()` and `saveConfig()` writes `JSON.stringify()` ([src/cli/context.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/context.ts)). Valid JSON is valid YAML, but the implementation is narrower than the filename suggests.

**Contradiction edges exist, but ingestion challenges do not visibly populate them.** The schema and health report support `claim_contradictions`, yet the inspected diff/resolve path lowers challenged-claim confidence and records an event without adding contradiction rows ([src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts), [src/compiler/resolve.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/resolve.ts), [src/metabolism/health.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/health.ts)).

**Red-team and resurface are advisory, while decay mutates.** Red-team returns critiques and suggested confidence adjustments; resurface returns questions and suggestions. Decay actually writes updated confidence values.

**The saved-answer loop can compound weak lineage.** `query --save` writes an LLM answer as a `quality: blog` raw source, with cited claim text, and tells the user to ingest it later ([src/cli/query.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/query.ts), [src/cli/save-answer.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/save-answer.ts)). Useful personally; risky for a KB that needs source-span-level provenance.

**Dashboard edits bypass the event model.** Claim statement and confidence edits are direct updates; they do not appear to create epistemic events like created/reinforced/challenged.

## What to Watch

- Whether claim-level provenance gains source spans, extraction prompt/model metadata, and reviewed acceptance state; that would make the confidence graph more auditable.
- Whether contradiction detection starts writing explicit `claim_contradictions` rows during ingestion or resolution.
- Whether MCP adds host-side automatic context injection; that would change the read-back verdict from pull-only.
- Whether generated wiki files become editable inputs that reconcile back into SQLite; that would change the source-of-truth model.
- Whether metabolism/red-team outputs gain governed acceptance states before mutating confidence or claim text.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Quicky Wiki stores and searches memory, but its agent-facing effect is explicit pull through query/search/MCP/dashboard surfaces.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw sources, SQLite graph rows, events, FTS, generated files, config, dashboard, and MCP tools carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: sources, claims, generated pages, health reports, critiques, and query answers mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: config, quality weights, extraction prompts, FTS ranking, confidence formulas, decay, cascade propagation, and tool schemas shape future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Quicky Wiki's central agent-facing mechanism is selecting bounded claim context for explicit queries.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - compares: ordinary questions use bounded FTS retrieval, while consensus mode loads the whole graph.
- [Use trace extraction](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - contrasts: Quicky Wiki uses extraction, but from documents and saved answers rather than operational traces.
