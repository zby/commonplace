---
description: "OKF Harness review: local file-first OKF wiki harness with source provenance, bounded CLI reads, generated agent guidance, lint, and graph reports"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-18"
---

# OKF Harness

OKF Harness, by pumblus, is a local, terminal-native harness for maintaining OKF-compatible LLM Wikis through Claude Code, Codex, and future coding agents. At the reviewed commit, it initializes local workspaces, installs agent guidance, registers source files or URL pointers, produces metadata-level ingest plans, searches and reads synthesized wiki concept documents with bounded JSON output, checks OKF conformance plus Harness lint, and generates a local graph report.

**Repository:** https://github.com/pumblus/okf-harness

**Reviewed commit:** [ea60b2d136fc157657ac8e966c27189ad66956e0](https://github.com/pumblus/okf-harness/commit/ea60b2d136fc157657ac8e966c27189ad66956e0)

**Last checked:** 2026-06-18

## Core Ideas

**The durable memory is an ordinary OKF workspace, not an app database.** `okfh init` creates a workspace with `wiki/` concept documents, `raw/sources/`, `.okfh/manifest.jsonl`, `.okfh/reports/`, `okfh.config.yaml`, and Claude/Codex guidance locations; the config fixes `wiki` as the OKF bundle root and records raw-source, manifest, and safety paths ([packages/core/src/workspace/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/workspace/index.ts)). The README explicitly frames the local folder as the center and keeps GUI, cloud sync, and vector retrieval out of the default path ([README.md](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/README.md)).

**The CLI prepares deterministic work, but the agent owns semantic synthesis.** `source add` copies local files or records URL metadata into `raw/sources/` and appends manifest rows; `ingest plan` recommends a reference path, candidate concepts, and a checklist from metadata token matches. It does not read source bodies, summarize content, extract claims, or rewrite wiki pages; generated agent guidance tells the agent to read the registered source and edit only affected wiki files ([packages/core/src/source/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/source/index.ts), [packages/agent-pack/src/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/agent-pack/src/index.ts), [packages/cli/test/ingest.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/cli/test/ingest.test.ts)).

**Agent guidance is a generated, layered system-definition artifact.** The agent pack renders a single `okf-harness` skill for Claude and Codex, with root `CLAUDE.md` or `AGENTS.md` managed blocks plus workflow references for setup, check, ingest, answer, and graph. It also preserves user root guidance outside the managed block and refuses to overwrite non-managed skill files unless forced ([packages/agent-pack/src/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/agent-pack/src/index.ts), [packages/agent-pack/test/index.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/agent-pack/test/index.test.ts)).

**Context efficiency is bounded lexical discovery plus bounded reads, not RAG.** `searchWorkspace()` returns thin candidate cards with scores, field matches, body-hit counts, and warnings, while explicitly omitting body snippets from result cards; `readWorkspaceDocument()` defaults to a 12,000-character preview, offers section/range reads, and caps full reads at 100,000 characters ([packages/core/src/search/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/search/index.ts), [packages/core/src/read/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/read/index.ts), [packages/core/test/search.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/test/search.test.ts)). The agent composes answers from `status`, `read index`, `search`, and bounded `read`; there is no `okfh query` command and no implemented vector or embedding path at this commit ([docs/WORKFLOWS.md](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/docs/WORKFLOWS.md), [docs/ROADMAP.md](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/docs/ROADMAP.md)).

**Trust comes from provenance and checks, not hidden retrieval quality.** File sources are copied under dated raw-source paths and hashed; duplicate file contents are reused by hash, URL sources are stored as metadata pointers, manifest rows are parsed and validated, source hash drift is a high-priority Harness finding, and broken links or missing citations remain Harness lint rather than OKF conformance failures ([packages/core/src/source/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/source/index.ts), [packages/core/src/lint/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/lint/index.ts), [packages/core/src/check/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/check/index.ts), [packages/cli/test/source.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/cli/test/source.test.ts)).

**The integration surface is intentionally narrow.** The implemented path is a Node CLI plus generated agent files; the MCP package only exposes scaffold metadata and tests that it has no MCP tools at this commit ([packages/cli/src/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/cli/src/index.ts), [packages/mcp/src/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/mcp/src/index.ts), [packages/mcp/test/index.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/mcp/test/index.test.ts)).

## Artifact analysis

- **Storage substrate:** `files` — The standing retained state is a local workspace file tree: OKF markdown under `wiki/`, raw source files or URL metadata under `raw/sources/`, source manifest JSONL, generated agent guidance files, config, graph/backlink reports, and optional local git state. No database, vector store, graph database, service object, prompt registry, or model-weight store is implemented in the reviewed code.
- **Representational form:** `prose` `symbolic` — Wiki concept bodies, reference documents, logs, generated skills, and workflow references are prose; YAML config, JSONL manifests, JSON CLI envelopes, source hashes, command routes, validators, search scoring, graph JSON, and TypeScript code are symbolic.
- **Lineage:** `authored` `imported` — Product templates, agent guidance, CLI code, and workspace scaffolds are authored; raw source records are imported from user files or URLs; wiki concept documents are agent- or human-authored synthesis from registered sources. I did not find durable retained artifacts derived from agent session traces, tool trajectories, or rollouts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — Wiki pages, reference documents, raw sources, graph reports, and search cards advise agents and humans; generated skills and root guidance instruct agent behavior; raw-source immutability rules, conflict checks, read caps, and lint/check exit behavior enforce boundaries; command dispatch, workflow references, workspace resolution, and concept ids route behavior; OKF conformance, manifest/hash checks, link/citation lint, and agent-pack tests validate artifacts; deterministic search scores and graph/backlink reports rank or orient candidate reads.

**OKF workspace.** The main memory artifact is the workspace created by `createWorkspacePlan()`: `wiki/` holds synthesized concept documents and reserved index/log pages, `raw/sources/` holds registered evidence records, `.okfh/manifest.jsonl` binds source IDs to provenance and hashes, and `okfh.config.yaml` defines paths and safety policy ([packages/core/src/workspace/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/workspace/index.ts)). Its wiki pages are knowledge artifacts; the config, manifest, and generated guidance become system-definition artifacts when CLI commands and agents consume them.

**Source manifest and raw source records.** `SourceManifestEntry` rows carry `id`, kind, original label, safe raw path, sha256, timestamp, status, optional mime/title/reference metadata, and parser-enforced shape. File sources are content-addressed for reuse, URL sources are URL-pointer markdown records rather than fetched page snapshots, and manifest append failures roll back copied raw files ([packages/core/src/source/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/source/index.ts), [packages/cli/test/source.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/cli/test/source.test.ts)). This is the clearest provenance surface.

**Agent adapter package.** The rendered skill is a prose instruction package with symbolic installation paths and managed-block markers. Its operative authority is instruction and routing: classify the request, run `okfh --json`, load only the needed workflow reference, preserve raw sources, run check after wiki edits, and report diffs ([packages/agent-pack/src/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/agent-pack/src/index.ts)).

**Search, read, and graph views.** Search cards, read envelopes, backlinks JSON, and graph HTML are derived access structures over the wiki. They are not canonical memory; they help an agent select and inspect canonical wiki concepts with bounded context volume ([packages/core/src/search/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/search/index.ts), [packages/core/src/read/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/read/index.ts), [packages/core/src/graph/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/graph/index.ts)).

**Check and lint outputs.** `checkWorkspace()` separates OKF conformance hard failures from Harness lint priorities. That gives validation authority to structural OKF readability and lower or higher maintenance authority to provenance, citation, index, and link findings without pretending every product preference is an OKF specification rule ([packages/core/src/check/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/check/index.ts), [packages/core/test/check.test.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/test/check.test.ts)).

Promotion path: imported source material becomes a registered raw source plus manifest row; an agent reads that source and writes a reference/topic/update in `wiki/`; `okfh check` can then promote or demote operational trust by reporting `ready`, `needs_attention`, or `blocked`. The content itself does not become a stronger representational form automatically: semantic synthesis remains prose authored by an agent or human, with symbolic checks around shape, links, citation presence, source integrity, and bounded access.

## Comparison with Our System

OKF Harness and Commonplace share the strongest local-first premise: agent-operated knowledge should remain inspectable as ordinary files, with deterministic tools for search, read, validation, and graph-like orientation. Both also separate raw source material from synthesized knowledge and make agents run checks after edits.

The major difference is type depth. Commonplace uses collection contracts, path-valued type specs, review workflows, and a richer internal vocabulary for semantic quality; OKF Harness targets portable OKF concept documents with a smaller set of conformance and maintainability checks. That makes OKF Harness easier to adopt for ordinary personal workspaces, while Commonplace is more opinionated about note kinds, linking semantics, and review gates.

OKF Harness has a sharper agent-adapter packaging story. It renders a single `okf-harness` skill with layered reference files into Claude and Codex layouts and preserves user guidance through managed blocks. Commonplace promotes skills into project adapters too, but the OKF Harness package treats generated agent guidance as a first-class product artifact.

The read-back tradeoff is also different. OKF Harness keeps the default retrieval stack deliberately simple: deterministic search candidates, bounded reads, and a graph report. Commonplace has broader KB navigation conventions and generated indexes, but much of its read-back is still agent-mediated search and link following. OKF Harness's restraint is useful: it avoids making vector recall look more authoritative than it is.

### Borrowable Ideas

**Managed guidance blocks.** Commonplace could use explicit managed sections when installing or upgrading root guidance in consuming projects, preserving user-authored instructions around framework-managed content. Ready for installer and skill-promotion work.

**One user-facing skill with layered workflow references.** OKF Harness avoids exposing setup/check/ingest/answer/graph as separate user-facing skills. Commonplace could apply that pattern where a family of promoted skills is better presented as one entrypoint with internal routing. Needs a concrete workflow family where the user-facing simplification outweighs direct skill invocation.

**Check status language that separates hard readability from quality lint.** `ready`, `needs_attention`, and `blocked` are a useful reporting layer. Commonplace validation already has severity and gates; borrowing this wording could make agent-facing final reports clearer. Ready for validation/reporting UX.

**Metadata-level ingest planning without pretending to understand sources.** OKF Harness returns candidate concepts and a checklist before the agent reads the source body. Commonplace snapshot and ingest workflows could make the same boundary more explicit when the deterministic part is only routing. Ready where current commands produce source metadata.

**Do not borrow the small type surface for methodology KBs.** OKF Harness is intentionally portable and lightweight. Commonplace's methodology KB needs stronger local type contracts, review gates, and linking vocabulary than generic OKF concept documents provide.

## Write side

**Write agency:** `manual` `automatic` — Humans or agents author synthesized wiki pages and decide semantic updates; the CLI automatically initializes workspace scaffolds, registers sources, appends manifests, reuses duplicate source records, writes generated agent guidance, writes graph/backlink reports, and emits check/search/read JSON.

**Curation operations:** `none` — Automatic writes are acquisition, scaffolding, validation, routing, and access-structure generation. The reviewed code does not automatically consolidate, evolve, synthesize, invalidate, decay, or promote existing stored memory content; semantic wiki maintenance is delegated to the agent following guidance.

## Read-back

**Read-back:** `pull` — Retained workspace knowledge reaches future action when an agent deliberately runs `okfh search`, `okfh read`, `source list`, `check`, or `graph`; I did not find an implemented path that automatically injects accumulated wiki/source memory into the agent's next invocation.

The main read-back consumer is the external coding agent. The generated root guidance and `okf-harness` skill are pushed baseline instructions, but they are installed system guidance rather than retained memory accumulated from workspace use. Those instructions tell the agent to call `okfh --json`, inspect returned JSON, and then decide what wiki content to edit or cite. The CLI gives it bounded selection surfaces rather than a final answer. That keeps context volume controlled, but it also means answer quality depends on the host agent choosing the right searches and reads.

Selection is identifier and lexical once the agent pulls. `read` targets concept ids, paths, section names, or section ids; `search` performs deterministic lexical and metadata scoring over title, path, tags, description, type filters, and bounded body matches. I did not find embedding retrieval or LLM-judgment retrieval in the implemented path.

The generated graph report is also a pull orientation surface. It writes `.okfh/backlinks.json` and `.okfh/reports/graph.html` from Markdown links and bare reference targets, then the user or agent must open or inspect it ([packages/core/src/graph/index.ts](https://github.com/pumblus/okf-harness/blob/ea60b2d136fc157657ac8e966c27189ad66956e0/packages/core/src/graph/index.ts)).

## Curiosity Pass

**The harness refuses to be an answer engine.** The docs and generated skill repeatedly say there is no `okfh query`; this is not just missing functionality, but a design line that prevents deterministic metadata search from being mistaken for semantic answering.

**URL sources are provenance pointers, not snapshots.** `source add` for a URL stores a markdown metadata record and hash of that metadata. That is safer than silently fetching web content, but a later answer cannot rely on the URL source body unless an agent or user separately saved the content and registered it as a file.

**The source manifest is append-friendly but not a full truth-maintenance model.** The code catches invalid rows, missing sources, hash drift, and missing reference source IDs, but it does not represent replacement, supersession, contradiction, or validity intervals for sources or concepts.

**The optional MCP package is not an integration yet.** The repo contains `@okf-harness/mcp`, but at this commit it only exports package metadata. Review claims about MCP tool behavior would be premature.

**Graph is an orientation artifact, not graph memory.** The graph report is rebuilt from Markdown links and citations. It does not store semantic relations beyond links, run graph algorithms for retrieval, or act as an agent router.

## What to Watch

- Whether the planned bounded evidence command appears; it would move OKF Harness from search-plus-read primitives toward a first-class evidence packaging layer, changing context-efficiency and read-back classifications.
- Whether optional vector or SQLite FTS caches become implemented; the roadmap keeps them optional, but they would add `vector` or possibly cache-backed symbolic access substrates beside files.
- Whether source replacement, contradiction, or review-queue features gain symbolic lifecycle state; that would add automatic curation or invalidation paths that are absent now.
- Whether new agent adapters preserve the same managed-block and layered-reference contract; adapter expansion is where instruction drift could appear.
- Whether the MCP scaffold grows real tools; that would add a second tool channel beside local shell `okfh --json`.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds: OKF Harness stores wiki and source artifacts, but activation depends on generated guidance, search/read calls, and agent behavior.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: OKF Harness bundles prose wiki content, symbolic manifests, generated instructions, validators, and derived graph/search views with different authorities.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - applies: OKF Harness read-back is strongest when a query string, concept id, path, section id, source id, or workflow symbol is already available.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki concepts, reference documents, raw source records, search cards, and graph reports advise future agents and humans.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated skills, root guidance, config, manifest validation, command routing, and check/lint rules carry instruction, routing, enforcement, and validation force.
