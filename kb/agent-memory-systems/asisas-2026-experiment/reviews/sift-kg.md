---
description: "sift-kg review: CLI document-to-knowledge-graph pipeline with LLM extraction, human-reviewed entity resolution, graph queries, and agent skill guidance"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# sift-kg

sift-kg, from Juan Ceresa's `juanceresa/sift-kg` repository, is a Python CLI and library that turns local document collections into a persistent NetworkX-backed knowledge graph. It extracts text from many document formats, uses LLMs to discover or apply a domain schema, extracts entities and relations, builds graph JSON, proposes duplicate merges for human review, generates narrative summaries, exports to analysis formats, and ships an agent skill that teaches agents to query the graph as an "AI second brain."

**Repository:** https://github.com/juanceresa/sift-kg

**Reviewed commit:** [d786991c024f5401f113fc0cb70aee96dd1bd3bf](https://github.com/juanceresa/sift-kg/commit/d786991c024f5401f113fc0cb70aee96dd1bd3bf)

**Last checked:** 2026-06-05

## Core Ideas

**The durable memory is a generated graph over imported documents.** The README's pipeline runs document extraction, schema discovery, entity/relation extraction, graph build, entity resolution, narrative generation, visualization, and export; the concrete project outputs are `output/extractions/*.json`, `discovered_domain.yaml`, `graph_data.json`, review YAML files, `communities.json`, `narrative.md`, `entity_descriptions.json`, rendered HTML, and exports ([README.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/README.md), [src/sift_kg/cli.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py)). There is no server database by default; the graph persists as files in the configured output directory.

**Schema-free means "discover a schema once, then reuse it."** In the default schema-free mode, extraction samples document text and asks the LLM to design entity and relation types, saves that schema as `discovered_domain.yaml`, and reuses the cached schema unless forced ([src/sift_kg/domains/discovery.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/domains/discovery.py), [src/sift_kg/extract/extractor.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/extractor.py)). Bundled `general`, `osint`, and `academic` domains provide fixed schemas, and custom YAML domains can enforce closed entity vocabularies and relation types ([src/sift_kg/domains/bundled/academic/domain.yaml](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/domains/bundled/academic/domain.yaml), [src/sift_kg/domains/models.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/domains/models.py)).

**The graph keeps provenance at node and edge level.** Extraction results carry document IDs, paths, chunk counts, model/domain metadata, entity contexts, relation evidence, confidence, and cost; graph building creates `DOCUMENT` nodes, `MENTIONED_IN` edges, source-document lists, support counts, relation evidence, and support documents ([src/sift_kg/extract/models.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/models.py), [src/sift_kg/graph/builder.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/builder.py), [src/sift_kg/graph/knowledge_graph.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/knowledge_graph.py)). That supports audit and export, though it does not make LLM-extracted claims fully verified.

**Deduplication is staged and reviewable.** `sift build` pre-deduplicates near-identical names with normalization, singularization, title stripping, and SemHash; `sift resolve` asks an LLM for merge proposals and variant relations; `sift review` marks drafts as confirmed or rejected, with confidence-based auto-approval/rejection defaults; `sift apply-merges` rewires graph edges and removes confirmed duplicate nodes ([src/sift_kg/graph/prededup.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/prededup.py), [src/sift_kg/resolve/resolver.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/resolver.py), [src/sift_kg/resolve/reviewer.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/reviewer.py), [src/sift_kg/resolve/engine.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/engine.py)).

**Context efficiency is graph-scoped pull retrieval, not bulk loading.** Agent-facing commands include `info --json`, `topology`, `query`, and `search --json`; the bundled skill explicitly warns that graphs under about 500 entities can be loaded directly, while larger graphs should be approached through topology and entity neighborhoods ([.agents/skills/sift-kg/SKILL.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md), [src/sift_kg/cli.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py)). There is no token budgeter or automatic prompt injector in the package; efficiency comes from explicit graph summaries, community/bridge views, entity lookup, and N-hop subgraphs.

**Adoption is CLI/library/skill based.** The package exposes a `sift` console command, Python pipeline functions for notebooks and applications, static graph viewers, exports to GraphML/GEXF/CSV/SQLite/JSON, and a bundled agent skill that instructs compliant agents to orient from and query the graph ([pyproject.toml](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/pyproject.toml), [src/sift_kg/pipeline.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/pipeline.py), [src/sift_kg/export.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/export.py), [.agents/skills/sift-kg/SKILL.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `files` `graph` `sqlite` — The main retained surfaces are local files under the output directory: extraction JSON, graph JSON, schema YAML, review YAML, communities JSON, narrative Markdown, viewer HTML, and exports. The active graph representation is NetworkX serialized to JSON; SQLite is an optional export format rather than the default live store ([README.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/README.md), [src/sift_kg/graph/knowledge_graph.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/knowledge_graph.py), [src/sift_kg/export.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/export.py)).
- **Representational form:** `prose` `symbolic` `parametric` — Narrative summaries, entity descriptions, document excerpts, relation evidence, domain descriptions, and the agent skill are prose; YAML schemas, JSON graph nodes/edges, review status files, CLI/API contracts, graph algorithms, and export tables are symbolic; optional sentence-transformer clustering, SemHash/model2vec similarity, LLM extraction, and LLM narration introduce parametric inference into derived artifacts and ranking/merge proposals ([src/sift_kg/narrate/generator.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/narrate/generator.py), [src/sift_kg/resolve/clustering.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/clustering.py), [src/sift_kg/graph/prededup.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/prededup.py)).
- **Lineage:** `authored` `imported` — Domain YAML, config, and the bundled skill are authored. The graph, schema discovery output, extractions, communities, merge proposals, narrative, descriptions, and exports are derived from imported documents and user review decisions. I did not find durable retained artifacts derived from agent session logs, tool traces, event streams, or trajectories, so this is not trace-derived learning under the current review contract.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Graph entities/relations, topology JSON, neighborhoods, search results, narrative, and exports advise agents and humans as knowledge; the bundled skill instructs agents how to use the graph; domains, CLI flags, entity IDs, source filters, query matching, and export formats route use; closed schemas, confidence thresholds, review statuses, API-key checks, cost caps, and tests validate or constrain operations; degree, communities, bridges, SemHash, optional embedding clustering, and candidate sorting rank attention; schema discovery, LLM extraction, merge proposal generation, community labeling, and narrative generation are learning-like derivation steps over imported source material.

**Imported documents and extraction records.** The source documents remain outside the retained graph, while `extract_document` reads them, writes per-document extraction JSON, tracks model/domain/chunk metadata, and caches non-stale extractions by model, domain, and chunk size ([src/sift_kg/extract/extractor.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/extractor.py)). Extraction records are knowledge artifacts with provenance and cost metadata, and they are also source material for graph construction.

**Graph data and topology.** `KnowledgeGraph` stores nodes and MultiDiGraph edges with confidence, evidence, source documents, support counts, canonical relation keys, mentions, and timestamps, then saves to JSON ([src/sift_kg/graph/knowledge_graph.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/knowledge_graph.py)). Community detection, bridge finding, isolated-node detection, and N-hop subgraph extraction turn the graph into agent-sized structural views ([src/sift_kg/graph/communities.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/communities.py)).

**Review YAML and merge application.** `merge_proposals.yaml` and `relation_review.yaml` are draft/confirmed/rejected decision files, not just reports. Once confirmed or rejected, `apply_merges` and `apply_relation_rejections` mutate the retained graph by merging nodes, rewriting edges, removing duplicate nodes, and removing rejected relations ([src/sift_kg/resolve/models.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/models.py), [src/sift_kg/resolve/engine.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/engine.py)).

**Narrative and descriptions.** `sift narrate` synthesizes an overview, relationship-chain prose, optional timeline narrative, community labels, and per-entity descriptions from graph structure and source contexts, then writes durable Markdown/JSON sidecars ([src/sift_kg/narrate/generator.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/narrate/generator.py)). These are more compact knowledge artifacts for humans, viewers, and agents, but their factual authority is only as strong as the graph and LLM generation.

**Agent skill.** `.agents/skills/sift-kg/SKILL.md` is a static system-definition artifact: it tells agents to orient with `sift info --json`, load `sift topology`, query entities, link knowledge islands, and avoid loading large graph JSON directly ([.agents/skills/sift-kg/SKILL.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md)). It changes behavior only for hosts that install and obey that skill.

**Promotion path.** Imported documents can become extraction records, graph nodes/edges, community assignments, reviewed merge decisions, narrative sections, entity descriptions, and export tables. The strongest promotion is from unstructured document text into symbolic graph structure with source/evidence fields, then into agent-readable topology/query surfaces. Human review can strengthen entity/relationship decisions, but there is no Commonplace-like type-validation or semantic review gate for the extracted claims themselves.

## Comparison with Our System

| Dimension | sift-kg | Commonplace |
|---|---|---|
| Primary purpose | Generate a local knowledge graph from arbitrary document corpora for exploration and agent lookup | Maintain a typed methodology KB for agents and maintainers |
| Canonical substrate | Output-directory files, especially extraction JSON and NetworkX graph JSON | Git-tracked Markdown artifacts, type specs, source snapshots, validators, and generated indexes |
| Knowledge structure | LLM-discovered or authored domain schemas plus graph nodes, edges, communities, narratives, and exports | Collection contracts, frontmatter schemas, authored links, indexes, reviews, notes, and instructions |
| Read path | Explicit CLI/library/viewer pull through `info`, `topology`, `query`, `search`, visual filters, and exports | Lexical search, curated/generated indexes, authored links, skills, review bundles, and validation reports |
| Write governance | Cost caps, closed schemas, confidence thresholds, merge/relation review YAML, tests, and user decisions | Collection/type contracts, deterministic validation, semantic review, git diffs, citation discipline, and artifact lifecycle |

The strongest alignment is that both systems make retained structure inspectable as ordinary files. SiftKG differs by letting the LLM derive much of the ontology and graph from raw documents, then presenting graph topology as the primary navigation surface. Commonplace starts from authored, typed artifacts and uses validation/review to preserve methodological authority.

SiftKG is better at making a heterogeneous document pile quickly navigable. It extracts entities and relations, computes communities and bridge entities, and gives agents a compact graph-shaped orientation without requiring a human to hand-build tags, backlinks, or indexes. Commonplace is better when the retained artifact itself is supposed to carry durable design authority: claims are authored, cited, typed, validated, and reviewed rather than merely extracted.

The main tradeoff is speed of structuring versus authority. SiftKG can transform a corpus in minutes, but LLM extraction and narration can create plausible graph structure whose claim-level correctness still needs domain review. Commonplace pays more authoring cost so the resulting artifact has clearer lineage, review state, and behavioral authority.

### Borrowable Ideas

**Topology as an agent orientation command.** Commonplace could expose a small JSON structural map for a collection or workshop: counts, hubs, bridges, isolated artifacts, stale review clusters, and cross-index gaps. Ready for review and navigation workflows.

**Graph neighborhoods as bounded context bundles.** SiftKG's `query` shape returns a matched entity plus an N-hop neighborhood rather than a full corpus. Commonplace could use a similar path-neighborhood command around notes, sources, reviews, and typed links, with explicit token or section budgets.

**Human-review YAML as a lightweight decision queue.** Merge and relation-review files are easy for agents and humans to inspect, edit, and apply. Commonplace already has review notes and gates, but a narrow YAML decision queue could help with batch link repairs, duplicate-note proposals, and source-ingest triage.

**Schema discovery should stay advisory.** The LLM-derived domain schema is useful for quick corpora, but Commonplace should not let generated schemas silently define durable methodology types. A comparable feature would need an explicit proposal file, validation, and human/semantic review before promotion.

**Do not borrow graph extraction as claim authority.** SiftKG's graph is excellent as exploratory structure; Commonplace should treat comparable extraction as candidate evidence or routing context until claims are promoted into sourced notes.

## Write side

**Write agency:** `manual` `automatic` — Users manually author configs/domains, provide source documents, edit review YAML, approve or reject proposals, and run CLI/library operations. Automatic paths read documents, discover schemas, extract entities and relations, build graph JSON, pre-deduplicate entity names, flag low-confidence or review-required relations, generate merge proposals, detect communities, generate narrative/descriptions, render views, and export formats.

**Curation operations:** `dedup` `synthesize` `promote` — Deterministic pre-dedup, LLM merge proposals, review auto-approval thresholds, and `apply_merges` remove or merge duplicate graph entries; narrative generation and relationship-chain/timeline/community-label steps synthesize prose views from the retained graph; community assignments, bridge detection, degree ranking, entity descriptions, and narrative sections promote selected graph structure into more salient agent/human-facing views. Index rebuilds, exports, and viewer rendering are access-structure upkeep rather than separate curation operations.

## Read-back

**Read-back:** `pull` — Retained graph memory reaches an agent only when the agent, user, or host explicitly calls `sift info`, `sift topology`, `sift query`, `sift search`, `sift view`, `sift export`, or library functions. The bundled skill instructs agents to use those commands proactively, but the repository does not include a deployed hook that automatically injects retained graph memory into future model invocations.

Pull paths are intentionally agent-shaped. `info --json` reports project/domain status, graph counts, review counts, and narrative presence; `topology` returns communities, bridges, isolated entities, and community connections; `query` resolves an entity name or ID and returns an N-hop subgraph; `search --json` returns entity matches and optional direct relations/descriptions ([src/sift_kg/cli.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py)).

Selection and scope are controlled by entity-name matching, exact IDs, type filters, graph degree, community assignments, source-document filters, confidence filters, neighborhood depth, top-N filtering, and export/view choices. The package tests mechanics of extraction, graph construction, review, export, and JSON output, but I did not find with/without tests proving that read-back changes a downstream agent's behavior.

The static agent skill is an edge case: it pushes instructions about when to query SiftKG, including session-start orientation and knowledge-island reasoning patterns, but that is shipped baseline documentation rather than retained memory accumulated from use. Under the review contract, it does not turn graph memory read-back into `push`.

## Curiosity Pass

**"Second brain" here mostly means structured corpus memory.** The graph persists across sessions and can orient an agent, but it does not remember agent conversations, tool traces, preferences, or decisions unless those are first supplied as documents and re-extracted.

**The graph is more auditable than ordinary RAG but less governed than a KB.** Nodes and edges carry source documents, support counts, evidence, and confidence, but the system still depends on LLM extraction and narration. Provenance helps users inspect claims; it is not the same as validated truth.

**The most interesting agent affordance is topology, not search.** `topology` exposes communities, bridges, isolated nodes, and inter-community connections as first-class JSON. That gives agents a way to reason about a corpus's shape before diving into specific entities.

**Human review is focused on identity and relation confidence, not all claims.** The review loop handles duplicate entities and flagged relations. It does not require every extracted entity, relation, narrative sentence, or community label to be confirmed before use.

**The package has no metered-service lock-in, but extraction can be metered.** Documents and outputs stay local, and Ollama is supported through LiteLLM, but default LLM extraction, resolution, and narration can spend API budget. The skill correctly tells agents to confirm before running cost-incurring `extract` or `resolve`.

## What to Watch

- Whether a future MCP/server integration adds automatic graph-memory injection into host model calls. That would change the read-back verdict from pull-only to push or both.
- Whether extracted claims gain per-claim review state beyond merge and low-confidence relation review. That would make SiftKG more useful as governed evidence rather than exploratory structure.
- Whether the bundled skill starts recording session observations or agent traces back into documents/graphs. That would change the trace-derived learning classification.
- Whether graph queries gain explicit token budgets or summarization budgets for very large corpora. The current guidance is scale-aware, but not tokenizer-aware.
- Whether schema discovery gets a stronger promotion workflow, such as generated-schema diffing, validation, and approval before reuse across extraction runs.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: SiftKG persists graph memory, but memory read-back is explicit CLI/library pull unless a host adds injection.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: SiftKG separates imported documents, extraction JSON, graph files, review decisions, narratives, exports, and skill instructions across different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: graph nodes, relations, topology, neighborhoods, narratives, and exports mainly advise as evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: domain schemas, review statuses, CLI commands, cost/config settings, graph algorithms, and the bundled skill define or constrain behavior.
- [Context engineering](../../../notes/definitions/context-engineering.md) - frames: SiftKG's agent-facing contribution is routing graph-shaped source knowledge into bounded lookup and topology surfaces.
