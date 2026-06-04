---
description: "Napkin review: local-first Markdown/Obsidian vault memory with NAPKIN.md, TF-IDF overview, BM25 search/read, templates, and pull-only CLI/SDK read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-02"
---

# napkin

napkin, from Michaelliv's `Michaelliv/napkin` repository, is a local-first TypeScript CLI and SDK for using a Markdown/Obsidian-style vault as agent memory. At the reviewed commit, its core memory mechanism is not embeddings, a graph database, or an autonomous learning loop. It is a filesystem vault with `NAPKIN.md` project context, generated folder overviews, BM25-style search over Markdown files, wikilink/backlink navigation, templates, tasks, properties, bases, canvases, and structured CLI/SDK outputs for agents.

**Repository:** https://github.com/Michaelliv/napkin

**Reviewed commit:** [ffd2b04c628e0ccf946002909dbe36a5c751a473](https://github.com/Michaelliv/napkin/commit/ffd2b04c628e0ccf946002909dbe36a5c751a473)

**Last checked:** 2026-06-02

## Core Ideas

**Markdown files are the memory substrate.** Napkin discovers or creates a vault by walking up to `.napkin/`, keeps content in the project directory, stores config under `.napkin/config.json`, syncs selected settings into `.obsidian/`, and treats ordinary Markdown notes as the durable knowledge store ([src/utils/vault.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/vault.ts), [src/utils/config.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/config.ts), [README.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/README.md)). The memory is inspectable and editable without Napkin running.

**Progressive disclosure is the central context-efficiency design.** The README describes four levels: `NAPKIN.md`, `napkin overview`, `napkin search <query>`, and `napkin read <file>` ([README.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/README.md)). The implementation matches that shape: overview returns the trimmed `NAPKIN.md` context plus a folder map, search returns ranked snippets, and read returns full file content ([src/core/overview.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/overview.ts), [src/core/search.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/search.ts), [src/sdk.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/sdk.ts)). Context volume is bounded by command choice, configured limits, folder depth, keyword count, snippet lines, and search result count. Context complexity is kept low by forcing the agent through overview/search/read rather than dumping the vault.

**The overview is a generated lexical map, not a semantic graph.** `getOverview()` groups Markdown files by folder, skips internal/template files, extracts tags and headings, weights filenames/frontmatter/body text, computes folder-level TF-IDF keywords, and appends warnings for malformed frontmatter ([src/core/overview.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/overview.ts)). The design doc explains the weighting pipeline and bigram suppression ([docs/overview-keyword-extraction.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/docs/overview-keyword-extraction.md)).

**Search is local lexical retrieval with small ranking extras.** `searchVault()` builds or loads a MiniSearch index over Markdown basename and content, then combines MiniSearch score, inbound wikilink count, and file recency before returning snippets ([src/core/search.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/search.ts)). The search cache stores a fingerprint, serialized index, file metadata, and backlink counts in `.napkin/search-cache.json`, invalidated by path/mtime changes ([src/utils/search-cache.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/search-cache.ts)).

**The CLI is explicitly agent-shaped.** Commands expose human, JSON, and quiet output surfaces, and the SDK exposes typed data-returning methods without `console.log` or `process.exit` ([src/main.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/main.ts), [src/sdk.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/sdk.ts)). The overview and search command outputs include hints that steer the next pull step, while hiding scores by default to reduce LLM anchoring ([src/commands/overview.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/commands/overview.ts), [src/commands/search.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/commands/search.ts), [docs/designing-cli-for-agents.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/docs/designing-cli-for-agents.md)).

**Templates provide adoption affordances rather than governance.** `napkin init --template` can scaffold domain-specific folders, `_about.md` files, note templates, and a `NAPKIN.md` skeleton for coding, personal, research, company, and product vaults ([src/core/init.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/init.ts), [src/templates/index.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/templates/index.ts), [src/templates/coding.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/templates/coding.ts)). This is a light structure layer: it gives agents familiar directories and starter formats, but does not enforce schemas or review states.

**Distillation is adjacent, not implemented in core Napkin.** The docs describe Pi extensions for context injection and automatic conversation distillation, and the README points users to `pi-napkin` for vault context injection, `kb_search`/`kb_read` tools, and automatic distillation ([docs/distill.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/docs/distill.md), [README.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/README.md)). In this checkout, I found no `src/commands/distill.ts`, no registered `napkin distill` command, and no included `.pi/extensions/` implementation. The review therefore treats trace distillation as a documented companion design, not as implemented Napkin behavior.

## Artifact analysis

- **Storage substrate:** `files` — Project filesystem under the vault content root, excluding hidden/system directories such as `.napkin/`, `.obsidian/`, `.git/`, `.trash/`, and `node_modules` during listing ([src/utils/files.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/files.ts))
- **Representational form:** `prose` `symbolic` — Prose Markdown plus YAML frontmatter, headings, tasks, tags, wikilinks, JSON config/cache records, command contracts, and Obsidian-compatible structures
- **Lineage:** `authored` `imported` — Authored or imported through file edits, CLI/SDK operations, templates, daily-note commands, external Obsidian editing, and generated views derived from the current vault files/config
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` — Notes and reads provide advisory knowledge; templates, command hints, config, and SDK/CLI contracts instruct and route access; MiniSearch/backlinks/recency rank returned snippets

**Vault Markdown notes.** Storage substrate: project filesystem under the vault content root, excluding hidden/system directories such as `.napkin/`, `.obsidian/`, `.git/`, `.trash/`, and `node_modules` during listing ([src/utils/files.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/files.ts)). Representational form: prose Markdown with optional YAML frontmatter, headings, tasks, tags, wikilinks, and Obsidian-compatible structures. Lineage: authored or imported by users and agents through file edits, CLI CRUD commands, templates, daily-note commands, or external Obsidian editing; Napkin itself preserves files rather than canonicalizing them into another store. Behavioral authority: knowledge artifacts when searched/read as evidence or context; weak system-definition artifacts when a host treats a note as instruction.

**`NAPKIN.md`.** Storage substrate: a top-level Markdown file created as an empty file for bare vaults or from template skeletons during scaffold/init ([src/utils/vault.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/vault.ts), [src/core/init.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/init.ts)). Representational form: prose. Lineage: authored by the user/agent or seeded by a template; invalidated by ordinary file edits. Behavioral authority: from Napkin's implementation it is context returned by `overview`; from a host agent's perspective it can become always-loaded advisory instruction if the host injects the overview or file. Napkin core does not itself run an agent or force that load.

**Generated overview output.** Storage substrate: transient CLI/SDK output, generated from current files and config each time `overview()` runs. Representational form: structured JSON or human text containing folder paths, note counts, tags, keywords, warnings, and optional `NAPKIN.md` context. Lineage: derived from Markdown filenames, frontmatter fields, headings, body text, tags, config values, and the keyword extraction algorithm. Behavioral authority: routing and navigation advice for the next agent action; it tells the agent where to search or read, but it is not durable unless captured elsewhere.

**Search index and cache.** Storage substrate: in-memory MiniSearch index plus `.napkin/search-cache.json`. Representational form: distributed-parametric-ish lexical index state serialized as JSON, plus symbolic doc metadata and backlink counts. Lineage: derived from Markdown file paths, mtimes, basenames, content, and wikilinks; regenerated when the fingerprint changes. Behavioral authority: ranking and retrieval system-definition artifact because it decides which files and snippets appear first in response to a query. Precision and recall are not verified by static code, though the benchmark harness measures retrieval effects externally.

**Config and Obsidian sync files.** Storage substrate: `.napkin/config.json` as Napkin source of truth, with generated `.obsidian/daily-notes.json`, `templates.json`, and `app.json` derived by `saveConfig()` ([src/utils/config.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/config.ts)). Representational form: symbolic JSON. Lineage: authored or updated through CLI/SDK config operations, merged with hardcoded defaults. Behavioral authority: configuration authority over overview depth/keyword count, search limits/snippets, daily note paths, templates folder, graph renderer, and Obsidian compatibility settings.

**Templates and scaffolded vault shape.** Storage substrate: TypeScript template definitions in the package and generated Markdown files/folders in the target vault. Representational form: mixed symbolic directory/file maps plus prose Markdown templates. Lineage: authored package definitions copied into a user vault by init/scaffold. Behavioral authority: weak system-definition authority over initial organization and expected note forms; after creation, the files become ordinary authored vault content with no enforcement beyond convention.

**CLI/SDK command surfaces.** Storage substrate: TypeScript modules in `src/main.ts`, `src/commands/`, `src/core/`, and `src/sdk.ts`. Representational form: symbolic API definitions, command options, output contracts, and prose hints in human output. Lineage: authored code. Behavioral authority: system-definition artifacts for agent interaction: commands route access, decide output volume, expose JSON/quiet modes, and teach follow-up actions. The hints are advisory prompt content, not a hard gate.

There is no implemented promotion ladder from note to rule to validator. A note can become more behavior-shaping if a host or human decides to load it as instruction, but Napkin core does not type, review, validate, or automatically promote memory artifacts into stronger authority.

## Comparison with Our System

| Dimension | napkin | Commonplace |
|---|---|---|
| Primary purpose | Local Markdown/Obsidian vault memory for agents and humans | Git-native methodology KB with typed artifacts, validation, review, and generated indexes |
| Main retained artifact | Markdown notes and vault config | Typed Markdown notes, instructions, ADRs, reviews, source snapshots, reports, indexes |
| Context strategy | Progressive disclosure: `NAPKIN.md` -> overview -> search -> read | Search, indexes, links, collection contracts, skills, validation/review commands |
| Retrieval | MiniSearch lexical search plus backlinks and recency | `rg`, authored links/indexes, generated indexes, review reports, optional command workflows |
| Governance | Templates, config, Obsidian conventions, CLI output contracts | Collection contracts, type specs, schemas, deterministic validation, semantic review, git history |
| Learning loop | Core Napkin has no implemented trace distillation loop | Workshop/library promotion, source-grounded note writing, review, validation, and explicit skill workflows |

Napkin is a close cousin to Commonplace at the storage and ergonomics layer. Both systems prefer plain files, cheap lexical search, readable source artifacts, and agent-operable command surfaces over opaque databases. Napkin's strongest contribution is product discipline: it makes the basic memory workflow small, installable, Obsidian-compatible, and easy for an arbitrary agent to operate without learning a large methodology.

The main divergence is authority and lifecycle. Napkin optimizes for capture and retrieval: if a Markdown file exists, overview/search/read can expose it. Commonplace optimizes for governed reuse: collection contracts, type specs, validation, replacement archives, and review gates decide how an artifact should be interpreted and when it is safe to shape future work. Napkin's simplicity is useful, but it leaves stale notes, contradictory notes, and high-authority instructions to host convention.

Napkin's read path also keeps activation deliberately manual. The system can make knowledge discoverable and cheap to inspect, but it does not decide that a given memory is relevant before an action or inject it into an agent loop. That makes Napkin easy to trust operationally, but it preserves the classic second-brain problem: stored knowledge affects behavior only when the agent asks the right thing or the host separately injects context.

**Read-back:** `pull` — In the implemented core, memory reaches the agent through explicit CLI/SDK calls such as `overview`, `search`, `read`, links, tasks, tags, properties, bases, and file commands; `NAPKIN.md` is included when overview is called, not automatically pushed by Napkin itself

### Borrowable Ideas

**Treat progressive disclosure as the default UX, not an advanced mode.** Commonplace already uses indexes/search/links, but Napkin's explicit level model is cleaner for new agents. A Commonplace analogue would document and expose a smallest-to-largest context ladder for each collection. Ready now as documentation and command-output convention.

**Design command output for LLM behavior, not human dashboards.** Napkin's score hiding, match-only snippets, JSON/quiet modes, and output hints are directly borrowable for Commonplace commands that agents consume. Ready now for command UX review.

**Keep a top-level project context note small and visible.** `NAPKIN.md` is a simple adoption surface: one short file tells an agent what the vault is about before it searches. Commonplace has richer `AGENTS.md` and indexes, but a deliberately small "KB context card" could help external agents. Needs a specific loading path so it does not duplicate existing instructions.

**Use template scaffolds as adoption affordances without pretending they enforce quality.** Napkin's templates make a new vault usable quickly. Commonplace could borrow that for consuming projects: scaffold folders, type examples, and minimal indexes, while keeping validation/review as the actual governance layer. Ready for init/template workflows.

**Cache lexical search state with inspectable invalidation metadata.** Napkin's path/mtime fingerprint and JSON cache are simple enough to debug. Commonplace could use similarly transparent caches if expensive indexes are introduced. Needs a concrete performance bottleneck first.

**Do not borrow ungoverned note authority.** Napkin intentionally lets any note be retrieved as context. Commonplace should preserve a stronger distinction between ordinary knowledge artifacts and instructions/validators with system-definition authority.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The README's "no summaries" benchmark claim is true for core retrieval, but not a general memory philosophy.** The benchmark harness converts chat sessions into per-round Markdown notes and relies on BM25/search/read rather than embeddings or summaries ([bench/README.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/bench/README.md), [bench/longmemeval-eval.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/bench/longmemeval-eval.ts)). That supports the progressive-disclosure argument, but the generated benchmark vaults are temporary evaluation artifacts, not a standing trace-derived learning mechanism in Napkin core.

**The docs mention two incompatible distillation shapes.** `docs/agent-memory-progressive-disclosure.md` describes a `napkin distill` command, while `docs/distill.md` says distillation is a Pi extension, not a Napkin command ([docs/agent-memory-progressive-disclosure.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/docs/agent-memory-progressive-disclosure.md), [docs/distill.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/docs/distill.md)). The code I inspected supports the latter for this repository: distillation is outside core Napkin.

**`NAPKIN.md` is called Level 0 always-loaded context, but the core implementation returns it through overview.** That is a useful distinction. Always-loaded behavior belongs to the host integration, while Napkin core provides the file and the overview field.

**The search cache is both a performance artifact and a hidden authority artifact.** It is not just an implementation detail: if corrupted or stale, it can change which memories an agent sees first. The fingerprint makes this fairly auditable.

**Bases, canvases, tasks, bookmarks, tags, properties, and links widen the memory surface without adding much agent policy.** Napkin covers many Obsidian-adjacent artifacts, but most are exposed as pull commands. The policy question remains in the host: which surface should matter for the next action?

## What to Watch

- Whether core Napkin adds a real `distill` command or vendors the Pi distill extension; that would change the trace-derived learning decision.
- Whether `pi-napkin` becomes part of this repository or a stable integration contract; that would change the read-back review from core pull-only to host-mediated context injection.
- Whether overview/search gain typed budgets, source freshness metadata, or confidence thresholds; that would make context assembly more governable than today's lexical ranking.
- Whether templates grow schema validation or required frontmatter; that would move Napkin from scaffolded convention toward enforceable artifact governance.
- Whether benchmark access traces feed back into vault promotion or overview weighting; that would turn evaluation telemetry into behavior-shaping memory.

## Bottom Line

Napkin is a real agent memory system in the file-first, progressive-disclosure family. Its strength is not automatic learning; it is a small, local, inspectable interface that lets agents find and read Markdown memory without paying the cost of full-context loading. For Commonplace, the borrowable lesson is the UX discipline around agent-facing retrieval, while the non-borrowable part is treating retrievable notes as sufficiently governed just because they are easy to load.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Napkin stores and retrieves memory well, but core Napkin does not automatically activate relevant notes before action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Napkin separates vault files, `NAPKIN.md`, overview output, search cache, config, templates, and CLI/SDK surfaces across substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: ordinary vault notes and search/read results mostly advise future work as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: config, command output contracts, templates, and search ranking code shape agent behavior through routing and instruction surfaces.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Napkin's main mechanism is routing and loading the right Markdown into bounded context.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - compares: Napkin is strong on discoverability and inspectable composition, weaker on trust/governance.
