---
description: "ATLAS review: logistics MCP server whose KnowledgeEngine enriches on-disk markdown files from document extractions, never overwriting — read-back only via its internal chat agent, not MCP"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-07-05"
---

# ATLAS

ATLAS (AI Transport Logistics Agent Standard), by Cargofy, is an open-source MCP server that indexes a logistics company's operational data — shipments, carriers, rates, tracking events, documents — inside the company's own perimeter and exposes it to external AI agents as read-only query tools. The stated deployment model is "questions only, no raw data out": an outside agent asks ATLAS about the company's logistics and gets answers, while the raw records stay local. Knowledge is one subsystem of this larger data server. The **KnowledgeEngine** maintains a small corpus of enterprise knowledge as markdown files on disk and automatically enriches it from the documents the extraction pipeline ingests. This review centers on that knowledge subsystem, not on ATLAS's full logistics query surface.

**Source:** https://github.com/cargofy/ATLAS

**Reviewed revision:** [65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988](https://github.com/cargofy/ATLAS/commit/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988)

## Core Ideas

**Knowledge is a folder of markdown files, not a database.** The KnowledgeEngine's substrate is a `knowledge/` directory rooted at `KB_ROOT` (`src/atlas.js` sets `const KB_ROOT = join(__dirname, '..', 'knowledge')`), addressed by relative `.md` paths. `getKnowledgeIndex()` walks the tree and returns sorted relative paths; `readKnowledgeFile`/`writeKnowledgeFile`/`deleteKnowledgeFile`/`getKnowledgeTree` are the CRUD surface, all guarded by `_resolveKbPath`, which normalizes the path and rejects anything escaping the root ([src/atlas.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/atlas.js)). This is the same file-first, editor-inspectable substrate as Basic Memory and DocMason, but far thinner: no parsed index, no frontmatter grammar, no search rows — just markdown text scored by string matching at read time.

**The write invariant is additive-only.** The enrichment system prompt forbids destructive edits: the engine may append a section, create a file, or mark a contradiction, but never rewrite.

> RULES:
> 1. NEVER delete or overwrite existing information — only ADD or MARK contradictions.
> --- [src/ai/knowledge-engine.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/knowledge-engine.js)

This is an intentional trust posture: the automatic path can grow the KB but cannot silently corrupt or drop a fact. Conflicts are surfaced, not resolved (below).

**Retrieval is substring scoring under a hard budget.** `loadRelevantKnowledge(topic, keywords, opts)` scores every KB file: +3 if the topic string appears in the path, +1 per keyword whose lowercased form is a substring of the file content; it sorts by score and takes the top `maxFiles` (default **5**) within a `maxChars` (default **30000**) character budget ([src/ai/knowledge-engine.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/knowledge-engine.js)). Keywords are pulled from structured entity records (identifier/name/code fields) or, for raw text, from capitalized words and code-shaped tokens. This is sense-blind lexical matching — it fires on a token whether or not the surrounding text negates it — with an explicit context-efficiency ceiling on the write-time read.

**Contradictions are annotated, not adjudicated.** On a conflict the engine does not supersede either value; it inserts a bilingual marker block naming both values and flagging it for a human:

> const block = `\n\n> **Суперечність** (джерело: ${src}, ${date}):\n> Поточне значення: ${contradiction.current_value}\n> Нове значення: ${contradiction.new_value}\n> Потребує перевірки.\n`;
> --- [src/ai/knowledge-engine.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/knowledge-engine.js)

Both the current and new values remain in the file; nothing is marked stale or superseded. Attribution lines (`> Джерело: …`) and the contradiction header are hardcoded Ukrainian ("Джерело" = source, "Суперечність" = contradiction), so the metadata scaffolding is language-fixed even though the prompt tells the model to keep body content in the file's existing language.

**Read-back is walled off from the external MCP surface.** The knowledge tools live only in the *internal* chat agent and the web UI — never in the MCP server that outside agents connect to. `src/index.js` registers the logistics query tools (`get_shipments`, `search_carriers`, `get_rate_history`, `get_sla_violations`, `query`, …) and no knowledge tool at all; a grep for `knowledge` in that file returns nothing. `read_knowledge` / `save_knowledge` / `list_knowledge` are defined only in `src/ai/chat.js`, the LLM tool-loop ATLAS runs itself. This matches the "no raw data out" boundary: the enterprise KB is company-private context for ATLAS's own reasoning, not something an external agent can pull.

## Artifact analysis

- **Storage substrate:** `files` — The retained knowledge is a directory of markdown files under `KB_ROOT` (`knowledge/`), addressed by relative path and CRUD'd through `atlas.js` helpers. There is no database mirror or index for the knowledge itself; the SQLite `ai_extract_log` table holds document-extraction *metadata* that drives enrichment, not the knowledge content ([src/atlas.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/atlas.js), [src/ai/extract-pipeline.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/extract-pipeline.js)).
- **Representational form:** `prose` — KB files are markdown prose (headers, tables, bold key-value), consumed by reading. The engine imposes light inline structure — Ukrainian attribution lines and contradiction blocks — but there is no separate symbolic index, frontmatter schema, or parsed graph over the knowledge; the JSON update protocol the LLM emits is transient and not retained. No parametric/embedding memory exists in the reviewed source.
- **Lineage:** `imported` `authored` — The automatic path is `imported`: enriched knowledge is derived by an LLM from document extractions, regenerable in principle by re-running enrichment over the source documents. The manual path is `authored`: ATLAS's chat agent (`save_knowledge`) and a human via the web UI CRUD write files directly. What invalidates the imported view is a change in the ingested documents; there is no propagation — a stale file simply persists until re-enriched or hand-edited.
- **Behavioral authority:** `knowledge` — The KB files are advisory context/reference. Their only consumer is ATLAS's own chat agent (and the human in the web UI); they instruct nothing, gate nothing, and route nothing in the external MCP path. The chat system prompt's injected file-path index is a lightweight recall/manifest aid, still knowledge-authority, not a routing table or validator.

**No promotion path.** Knowledge cannot move toward stronger form or authority. There is no step that turns a KB file into a validator, a schema, a route entry, or an enforced gate; a contradiction marker is the strongest signal the system emits, and it is a passive flag awaiting human review. Effective quality — whether the appended prose is accurate, whether the substring retrieval actually surfaces the right file — is *not verified from code*: the pipeline applies whatever the LLM returns after light structural validation (`action` + `path` present).

## Comparison with Our System

ATLAS shares Commonplace's file-first instinct — durable knowledge as inspectable markdown, not opaque service state — and its additive-only write invariant echoes Commonplace's preference for replacement history over silent overwrite. But the resemblance is shallow. ATLAS's KB has no type system, no collection contracts, no frontmatter, no validation, and no review gate; a file is whatever the enrichment LLM or a UI user wrote, attributed by a source line and a date. Retrieval is a single substring-scoring function, where Commonplace layers curated indexes, tags, typed routing, and `rg`.

The sharpest divergence is governance of contradictions. ATLAS's `mark_contradiction` retains both values inline and defers to a human, with no notion of supersession, `invalid_at`, or which value now holds — the opposite of a truth-maintenance discipline. Commonplace treats contradiction as a first-class lifecycle event (replacement, invalidation records, type-change review). ATLAS's approach is cheaper and never loses data, but the KB accretes unreconciled conflicts that only a human sweep resolves.

The most transferable design decision is the *access boundary*: ATLAS deliberately excludes its private KB from the external tool surface, exposing knowledge read-back only to its own in-perimeter agent. That is a clean articulation of "memory is for this system's reasoning, not for arbitrary callers."

### Borrowable Ideas

**Additive-only automatic enrichment with a hard char budget.** ATLAS's write path never overwrites and reads at most 5 files / 30000 chars before proposing changes. For any future Commonplace auto-write helper, "append or flag, never rewrite, under an explicit token ceiling" is a safe default. Ready now as a design constraint on a workshop-layer enrichment tool; durable promotion should still route through review.

**Contradiction-as-annotation as a cheap triage marker.** Inserting a "both values stand, needs verification" block is a low-cost way to surface conflicts without deciding them. Ready as a pattern for flagging conflicting claims during ingest — but only paired with a review queue, since ATLAS has no mechanism to ensure the flag is ever resolved.

**Access-boundary separation of the memory surface.** ATLAS keeps knowledge read/write off the externally-reachable MCP tools and only on the internal agent. If Commonplace ever exposes an MCP surface, the analogue is keeping curation/write tools separate from any outward-facing query surface. Needs a concrete MCP use case before it is actionable.

## Write side

**Write agency:** `manual` `automatic` — Automatic: the `knowledge-enricher` module polls `ai_extract_log` for extractions since its last watermark and calls `enrichFromText`; the extract pipeline also calls `enrichFromExtraction` inline after upserting records ([src/modules/knowledge-enricher/index.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/modules/knowledge-enricher/index.js), [src/ai/extract-pipeline.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/extract-pipeline.js)). Manual: the chat agent's `save_knowledge` tool and the web UI's `/api/kb/file` POST/DELETE and `/api/knowledge/enrich` endpoints let an agent or human write and edit files directly ([src/ai/chat.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/chat.js), [src/ui-server.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ui-server.js)).

**Curation operations:** `evolve` — The automatic path's three actions are `create_file` and `append_section` (both *acquisition*: placing newly-imported facts into a new or existing file — Lineage `imported`, not curation) and `mark_contradiction`, which is the one genuine operation over already-stored memory: triggered by a conflict with existing content, it modifies an existing file in place by inserting a "needs verification" annotation, retaining both values without merging or deleting — the weakest, annotation-only form of `evolve`. It is deliberately **not** `invalidate`: nothing is marked stale or superseded, no `valid_at`/`invalid_at` is recorded, and both values continue to stand pending a human. No `consolidate`, `dedup`, `synthesize`, `decay`, or `promote` occurs — the prompt's "skip if already present" is an LLM write-time guard, not a store operation reconciling existing entries. (A stricter reading that treats the contradiction annotation as still acquisition-side would report `none`; `evolve` is the honest floor because the operation reads existing content and writes back into that same entry in response to newly arriving data.)

## Read-back

**Read-back:** `both` — ATLAS's own chat agent receives a coarse always-load push (the KB file-path index injected into every system prompt) and then pulls file bodies on demand via the `read_knowledge` tool. External MCP agents get no knowledge read-back at all.

**Read-back signal:** `coarse` — `buildSystemPrompt(atlas)` unconditionally lists the entire KB index (paths only) in the chat agent's system prompt: `Knowledge Base files (${kbFiles.length}):` followed by every `- ${f}` path, with the instruction "Use read_knowledge to fetch content" ([src/ai/chat.js](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/chat.js)). This is an always-present listing keyed on session start, not on the current instance — coarse recall of *what exists*, leaving relevance to the agent's subsequent pull.

**Faithfulness tested:** `no` — Nothing in the reviewed source runs a with/without-knowledge ablation or post-answer audit proving the injected index or the pulled files change the chat agent's output; the presence of context is assumed to equal use.

**Direction edge cases.** The push is only the *index*, not the knowledge itself — a manifest of pointers. Actual knowledge content reaches the model only when the agent chooses to call `read_knowledge`, which is pull. So the coarse push carries near-zero payload; its role is to make the pull *possible* by advertising available paths. The enrichment write path (`loadRelevantKnowledge` scoring files, sending them to the enrichment LLM) reads KB files too, but that read serves a *write* decision (what to append/flag), not a read-back into an acting agent — it is write-side machinery, not a serve path.

**Targeting and signal.** The always-load index is `coarse`; there is no instance-targeted push of knowledge. When the agent does pull, `read_knowledge` takes an exact path (an `identifier` the agent already holds from the index), and the enrichment-time `loadRelevantKnowledge` uses `inferred / lexical` substring scoring — but both of those are internal reads, not pushes into the agent's context.

**Injection point.** Pre-invocation: the file-path index is assembled by `buildSystemPrompt` at the start of each chat turn, before the first model call, alongside live record counts from `getSyncStatus`.

**Selection, scope, and complexity.** The pushed index is **unbounded** — every KB path is listed, with no top-k or token cap on the manifest, so a large KB inflates every system prompt linearly. The counterpart write-time read *is* bounded (5 files / 30000 chars). This is an asymmetry worth naming: the serve-side manifest has no budget while the write-side context read does.

**Authority at consumption.** Advisory only. The chat agent is told the KB files hold "findings"; nothing makes a recalled file a gate or instruction.

**Other consumers.** The human operator reads and edits the same files through the web UI KB manager (`/api/kb/tree`, `/api/kb/file`), so the KB is simultaneously an agent-facing context store and a human-facing document manager.

## Curiosity Pass

- **The MCP boundary is the most interesting design choice, and it is easy to miss.** ATLAS is marketed as an MCP server, so the natural assumption is that its knowledge base is part of the MCP offering. It is not: the KB is reachable only by ATLAS's internal chat agent and the local web UI. An external agent connected over MCP can query logistics records but cannot see or write a single knowledge file. The "memory" of ATLAS is private to ATLAS.
- **"Knowledge enrichment" is thinner than the README implies.** The README describes AI that "automatically updates your knowledge base from extracted data, detecting contradictions." In code, the enricher module feeds the LLM only *extraction metadata* — filename, entity-group count, record count, timestamp (`buildSummaryForEntry`) — not the extracted records themselves, because it "does not query unrelated tables (no way to correlate log entries to specific DB records)." The richer inline path (`enrichFromExtraction`, called from the extract pipeline) does pass real record JSON. So enrichment quality depends heavily on *which* entry point fired.
- **Contradiction detection is only as good as substring recall.** A contradiction can only be marked if `loadRelevantKnowledge` surfaced the conflicting file into the 5-file / 30k-char window in the first place. If the relevant file scores below the cut (no path-topic match, no keyword substring hit), the new value is appended or filed as a fresh fact and the conflict is never seen. The additive-only invariant then guarantees both live on, unlinked.
- **The hardcoded Ukrainian metadata is a quiet coupling.** Attribution and contradiction scaffolding are fixed Ukrainian strings while body content follows the file's language. A KB authored in English accretes Ukrainian `> Джерело:` / `> Суперечність` annotations — cosmetically odd, and a sign the metadata layer was never generalized.

## What to Watch

- Whether ATLAS ever exposes knowledge read/write on the external MCP surface; that would flip the read-back verdict for outside agents from none to a pull tool and change the whole trust boundary.
- Whether the always-load KB index in the chat system prompt gains a budget; without one, a growing KB linearly inflates every chat turn's context.
- Whether contradiction markers ever gain resolution machinery (supersession, a review queue, `valid_at` semantics); today they are write-once flags with no lifecycle, so the classification would move from `evolve` toward `invalidate` only if that arrives.
- Whether the enricher starts consuming actual extracted records rather than extraction metadata; that would materially change enrichment fidelity and the imported-lineage story.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: ATLAS stores markdown knowledge but only its internal chat agent activates it, and only via a coarse index push plus agent pull; external MCP agents get storage with no read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: separates the markdown KB files (files/prose/imported+authored/knowledge) from the `ai_extract_log` extraction metadata that drives enrichment.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: ATLAS's KB files are advisory context to its chat agent, with no instruction, routing, or enforcement authority.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: with no typed identifiers on knowledge files, ATLAS falls back to substring scoring and a coarse path index rather than instance-targeted recall.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: the enrichment system prompt and MCP tool registrations are ATLAS's system-definition surface, while the KB files themselves are knowledge artifacts.
