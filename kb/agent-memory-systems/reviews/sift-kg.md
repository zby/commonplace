---
description: "sift-kg review: document-to-knowledge-graph CLI with LLM extraction, source-grounded graph JSON, review YAML, topology queries, and an agent skill"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-02"
---

# sift-kg

sift-kg, by Juan Ceresa, is a local document-to-knowledge-graph CLI and Python library. At the reviewed commit it reads documents, discovers or loads a domain schema, extracts entities and relations with an LLM, compiles them into a NetworkX graph persisted as JSON, supports human review of proposed merges and low-confidence relations, and exposes graph topology through CLI commands plus a bundled agent skill.

**Repository:** https://github.com/juanceresa/sift-kg

**Reviewed commit:** [d786991c024f5401f113fc0cb70aee96dd1bd3bf](https://github.com/juanceresa/sift-kg/commit/d786991c024f5401f113fc0cb70aee96dd1bd3bf)

**Last checked:** 2026-06-02

## Core Ideas

**The central retained artifact is a source-grounded graph, not a note corpus.** `sift extract` writes per-document extraction JSON under `output/extractions/`, then `sift build` loads those files, creates `DOCUMENT` nodes, entity nodes, relation edges, `MENTIONED_IN` provenance edges, support counts, support documents, and confidence aggregation before saving `output/graph_data.json` ([extractor.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/extractor.py), [builder.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/builder.py), [knowledge_graph.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/knowledge_graph.py)).

**Schema-free mode is an LLM-generated symbolic contract.** When the selected domain is schema-free, extraction samples the first chunk, asks an LLM to design entity and relation types, and saves the result as `output/discovered_domain.yaml` for reuse unless forced ([discovery.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/domains/discovery.py), [extractor.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/extractor.py)). Fixed bundled domains and custom YAML domains give the opposite mode: authored entity/relation vocabularies, endpoint constraints, canonical names, and review-required relation types.

**Human review is focused on graph cleanup, not every extraction.** The build step flags low-confidence or review-required relations into `relation_review.yaml`; `sift resolve` proposes entity merges into `merge_proposals.yaml`; `sift review` can auto-approve high-confidence proposals, auto-reject low-confidence relations, or ask the operator to approve, reject, or skip items ([builder.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/builder.py), [resolver.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/resolver.py), [reviewer.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/resolve/reviewer.py)).

**Context efficiency is graph-scope selection.** The system does not put the whole graph into an agent context by default. It exposes `info`, `topology`, `search --json`, and `query` so an agent can first load counts, communities, bridges, isolated nodes, and targeted neighborhoods, with the bundled skill warning that large graphs should be approached through `topology` and `query` rather than by loading `graph_data.json` wholesale ([cli.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py), [communities.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/graph/communities.py), [SKILL.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md)).

**Read-back is explicit and tool-shaped.** The agent skill says to orient with `sift info --json` and `sift topology`, then use `sift query` or `sift search` for concrete questions. That makes the graph an inspectable memory substrate with a disciplined pull workflow, not an automatic prompt-injection service ([SKILL.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md), [cli.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py)).

**The adoption surface is deliberately local.** Configuration comes from CLI flags, environment variables, `.env`, and `sift.yaml`; output is JSON, YAML, Markdown, HTML, CSV, SQLite, GraphML, or GEXF; and the README emphasizes local document processing plus optional OCR and multiple LiteLLM providers ([config.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/config.py), [export.py](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/export.py), [README.md](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/README.md)).

## Artifact analysis

- **Storage substrate:** `files` — `output/extractions/*.json` on the local filesystem
- **Representational form:** `prose` `symbolic` — Symbolic JSON, YAML, graph structures, Markdown narratives, and CLI/skill instructions carry prose fields for entity context quotes, relation evidence, descriptions, reasons, and explanations.
- **Lineage:** `authored` `imported` — Source documents are imported, while extraction files, discovered schemas, graph JSON, review queues, communities, narratives, exports, and the skill are derived from source text, authored domain rules, LLM extraction, deterministic postprocessing, and operator review.
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `validation` — Extractions, graph artifacts, narratives, and exports advise users and agents, while schemas, review files, graph algorithms, query/topology tools, postprocessors, and the bundled skill constrain extraction, route lookup, rank visibility, or mutate reviewed graph state.

**Per-document extraction files.** Storage substrate: `output/extractions/*.json` on the local filesystem. Representational form: symbolic JSON with prose fields for entity context quotes and relation evidence. Lineage: derived from source documents through text extraction, chunking, optional schema discovery, document-context generation, and LLM JSON extraction; stale when model, domain, or chunk size changes. Behavioral authority: knowledge artifact as source evidence for graph construction; system-definition input to `sift build` because it determines nodes and edges.

**Discovered or authored domain schemas.** Storage substrate: bundled domain files, user domain YAML, `sift.yaml`, and generated `output/discovered_domain.yaml`. Representational form: symbolic YAML plus prose descriptions and extraction hints. Lineage: authored for fixed domains or LLM-derived from document samples for schema-free runs. Behavioral authority: system-definition artifact: it constrains extraction prompts, type normalization, relation endpoint direction, canonical vocabularies, and review-required relation types.

**Knowledge graph JSON.** Storage substrate: `output/graph_data.json` plus optional exports in GraphML, GEXF, CSV, SQLite, and native JSON. Representational form: mixed symbolic graph structure, prose names/evidence/context, numeric confidence/support metadata, and optional narrative descriptions. Lineage: compiled from extraction JSON, domain rules, deterministic pre-dedup, postprocessors, relation support aggregation, community detection, and reviewed merge/relation decisions. Behavioral authority: knowledge artifact when read by humans or agents; routing/ranking artifact when `query`, `topology`, viewer filters, exports, and graph algorithms select what becomes visible.

**Review files.** Storage substrate: `output/merge_proposals.yaml` and `output/relation_review.yaml`. Representational form: symbolic YAML with prose reasons, evidence, statuses, confidences, and flags. Lineage: LLM merge proposals, deterministic cross-type duplicate proposals, low-confidence relation flags, review-required relation flags, and operator decisions. Behavioral authority: system-definition artifact for graph mutation once `sift apply-merges` rewires confirmed entities or removes rejected relations.

**Communities, topology, and narrative artifacts.** Storage substrate: `output/communities.json`, `output/entity_descriptions.json`, and `output/narrative.md`. Representational form: symbolic community assignments, prose descriptions, and Markdown narrative. Lineage: Louvain community detection, LLM theme naming, LLM entity descriptions, relationship-chain selection, timeline extraction, and prose rewriting filters. Behavioral authority: knowledge artifact for orientation and explanation; soft routing authority when an agent uses communities, bridges, or top entities to decide where to look next.

**Bundled agent skill.** Storage substrate: `.agents/skills/sift-kg/SKILL.md` in the repo, copied or installed into an agent environment by the host. Representational form: prose instructions plus CLI command patterns. Lineage: authored instructions over the sift CLI surface; invalidated when CLI output shapes or graph semantics change. Behavioral authority: system-definition artifact for agents that load the skill: it instructs when to orient, query, avoid full graph loading, find knowledge islands, and ask before cost-incurring extraction or resolution.

Promotion path: sift-kg promotes source documents into extraction JSON, graph JSON, review queues, reviewed graph mutations, narrative summaries, and export formats. It does not promote findings into authored notes, tests, or validators; its strongest built-in authority is graph-structure mutation after review and agent instruction through the bundled skill.

## Comparison with Our System

Commonplace and sift-kg both prefer inspectable local artifacts over an opaque hosted memory service, but they choose different canonical forms. Commonplace stores typed Markdown artifacts with collection contracts, links, validation, generated indexes, and semantic review. sift-kg stores a derived graph whose canonical state is JSON plus YAML review files, with Markdown mostly reserved for generated narrative.

The systems also differ in where they spend governance. Commonplace reviews and validates artifacts before they enter higher-authority positions. sift-kg lets LLM extraction create the initial graph, then focuses human attention on entity merges and suspect relations. That is a pragmatic fit for high-volume document mapping, but it makes the graph's unflagged extracted relations more trusted than Commonplace would normally allow for methodological claims.

**Read-back:** `pull` — The graph reaches the agent through deliberate `info`, `topology`, `query`, `search`, viewer, export, or skill-guided lookup. I did not find an implemented host hook that automatically matches the user's current situation and injects graph memory into the agent context before action

The most relevant alignment is progressive disclosure. sift-kg's agent-facing topology command is a compact structural overview: communities, bridges, isolated nodes, and inter-community connections. Commonplace has indexes, descriptions, tags, links, and connect reports, but less explicit graph-topology output for "where are the knowledge islands?" style orientation.

### Borrowable Ideas

**Topology as first-class read-back.** Ready now as a review/reporting pattern. Commonplace could expose a lightweight structural summary of notes, tags, links, orphan clusters, bridge notes, and weakly connected collection areas without turning the KB into a graph database.

**Separate source provenance from substantive graph edges.** Ready now. sift-kg strips `DOCUMENT` nodes and `MENTIONED_IN` edges for topology analysis while retaining them for provenance. Commonplace could use the same distinction when computing navigation signals: source/evidence links should not always count like conceptual links.

**Review queues for uncertain derived structure.** Ready for derived indexes, not library notes. `merge_proposals.yaml` and `relation_review.yaml` are a useful middle layer for machine-proposed structure. In Commonplace this fits generated link suggestions, duplicate-note candidates, or type-normalization proposals better than direct note rewrites.

**Agent-facing graph commands with bounded output.** Needs a concrete query surface. `sift topology` and `sift query --depth` show how a CLI can be designed for agent context budgets: load the map, then load one neighborhood. Commonplace can borrow the output discipline even if the underlying substrate remains Markdown.

**Do not borrow schema-free extraction as authority.** The LLM-designed schema is useful for exploration, but Commonplace's methodology artifacts need authored contracts and validation. Schema-free extraction should create candidates or workshop artifacts, not directly define durable collection semantics.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The README's "AI second brain" claim is implemented as graph tooling plus a skill, not as an autonomous memory daemon.** That is a useful restraint: the system gives agents commands and instructions, but the host agent still has to choose to call them.

**The project metadata still points some package URLs at `civictable/sift-kg`.** The reviewed source and requested citation target are `juanceresa/sift-kg`, while `pyproject.toml` names `https://github.com/civictable/sift-kg` for homepage, documentation, repository, and issues ([pyproject.toml](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/pyproject.toml)). That does not change the implementation, but it is a source-identity wrinkle.

**The graph has better provenance than many vector-memory systems, but not full source-span replay.** Entity contexts and relation evidence are retained, along with source document ids and support counts. The source text chunks themselves are not preserved as a separate durable trace object in the graph format.

**The review layer is asymmetric.** Merges and low-confidence/review-required relations get explicit approval states; ordinary extracted entities and higher-confidence relations do not. That is sensible for cost and ergonomics, but it means "not in review queue" is not equivalent to "verified."

**Topology excludes provenance on purpose.** The clean graph strips document nodes and `MENTIONED_IN` edges before community and topology analysis. That is exactly right for structural sensemaking, but consumers need to remember that the graph's explanatory topology is not the same as its evidence topology.

## What to Watch

- Whether the agent skill is installed automatically by `sift init` or packaging hooks, or remains a repo-bundled file that host agents must discover and load manually; this determines whether read-back stays explicit pull or becomes stronger session-start activation.
- Whether extraction files begin retaining chunk text, prompt/model versions per chunk, and exact source spans; that would make graph lineage easier to audit and regenerate.
- Whether relation/entity review expands from cleanup queues to broader verification states on graph elements; that would make sift-kg more relevant to evidence-sensitive KB governance.
- Whether the package metadata converges on the same canonical repository URL as the reviewed GitHub source; divergent identity metadata complicates citation and update routing.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: sift-kg stores a durable graph, but agent effect depends on deliberate graph lookup through CLI commands or the skill.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: sift-kg's graph, schemas, review queues, narrative files, and agent skill need separate substrate/form/lineage/authority treatment.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: graph nodes, edges, topology, narrative, and exports mostly serve as evidence, context, or orientation.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: domain schemas, review statuses, graph mutation commands, CLI filters, and the bundled agent skill constrain later behavior.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - echoes: sift-kg uses topology and neighborhood queries to avoid loading the whole graph into context.
