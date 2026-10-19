---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "sift-kg workflow: agent-directed document ingestion, optional identity review, and graph-grounded delivery at the frozen revision."
run-id: AAS-2026-10-15-sift-kg-dca68bc45a2c-01
reviewed-boundary: d786991c024f5401f113fc0cb70aee96dd1bd3bf
---

# sift-kg workflow report

## Workflow account

### Selection and evidence

The representative workflow is the bundled skill's create/update-and-answer procedure: a user supplies documents; the host agent obtains permission for paid extraction; extraction and build produce saved graph state; optional resolution/review/application cleans identities; the host retrieves graph context and explains the result. This procedure is selected because the shipped skill explicitly connects document production, maintenance and later agent use. It is not an invented autonomous coordinator joining unrelated APIs. The optional maintenance branch is expressly offered under “For better entity deduplication.” SRC-1: `.agents/skills/sift-kg/SKILL.md`; [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill).

> When the user provides new documents or wants to create/update the graph:
> --- `.agents/skills/sift-kg/SKILL.md`

> Base your answer on actual entities and relationships from the graph. If the entity isn't in the graph, say so — don't invent connections.
> --- `.agents/skills/sift-kg/SKILL.md`

This is a source-level workflow, not a supplied execution trace. Implementation conclusion status: wired for the CLI stages; operation conclusion status: uninspected. Host orchestration and final-answer compliance are requested by the skill, not established by executable sift-kg scheduling. No target commands, tests or providers were run. Added SRC-1 inspection covers the entire skill, CLI build/review/application/query bodies, merge-review interaction and the full surgery engine. These provide doctrine/design and implementation evidence at the boundary's revision, not a new source or observed run.

### Handoffs and next-step ownership

1. **User to host agent.** The request supplies documents and a desired update or answer. The skill asks the host to orient with `sift info --json` and `sift topology`, or build first when no graph exists. The host owns command selection, output-directory consistency and requesting permission before extract/resolve. The CLI does not enforce that permission exchange. In the skill's examples `review` omits `-o`; the CLI resolves its own configured output directory. A host using a nondefault directory must explicitly pass the same directory rather than assume all commands share session state. SRC-1: `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/cli.py`; [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill).

2. **Host to extraction, then code to completion model.** The host supplies document directory, output directory and optional model/domain settings. Python selects documents, cache entries and chunks, optionally discovers a schema, and supplies each extraction call with a domain-conditioned chunk and a first-chunk document summary. The delegated unit is a bounded completion request, not a worker with authority to choose later tools. Semaphore/gather coordinates chunk work; decoded entities/relations return to aggregation and per-document JSON. Extraction's terminal artifact is input to a separate build invocation, not an automatically advanced stage. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/llm_client.py`; [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery).

3. **Extraction files to build.** The host invokes build against the same output directory. Build reads retained extractions, constructs a fresh graph, normalizes/deduplicates, saves graph JSON, writes communities and then emits relation flags. It does not append reviewed surgery to the previous graph. The skill's “grows incrementally” description is therefore accumulation through retained extraction inputs, not preservation of arbitrary changes to the previous graph. The CLI's printed “Next” suggestions return control to the caller; they do not execute resolution. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/graph/builder.py`; [RT-RTE-graph-build](runtime.md#rt-rte-graph-build).

4. **Optional graph-to-proposal-to-decision branch.** With further user permission under the skill protocol, the host invokes resolve. The resolver model receives selected names/aliases/identity attributes in batches, not the complete document evidence or graph. Software filters proposals and persists DRAFT merge proposals and variant review entries. Review reloads these files, auto-confirms qualifying items and asks a human about remaining drafts. Thus semantic judgments pass between independent calls through YAML; neither the resolver nor the reviewer owns automatic progression to application. SRC-1: `src/sift_kg/resolve/resolver.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`; [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-review-application](runtime.md#rt-rte-review-application).

5. **Decision files to changed graph.** The host separately invokes apply-merges. The engine checks confirmed merges against current node existence, combines node data, rewrites incident edges and removes merged members/self-loops. It also removes rejected relation triples. The CLI saves only if changes occurred. A CONFIRMED proposed variant is not inserted as an edge. The result available for subsequent queries is the saved graph, not the review decision alone. SRC-1: `src/sift_kg/resolve/engine.py`, `src/sift_kg/cli.py`; [RT-RTE-review-application](runtime.md#rt-rte-review-application).

6. **Saved state to host to user.** The host queries a topic/name or exact ID; code reloads graph state, ranks ambiguous substring matches, selects a neighborhood and returns JSON with match information, subgraph and other matches. The host chooses further queries and authors the user-facing explanation. For an update, the skill additionally offers a before/after topology comparison: capture topology before extraction/build, inspect it afterwards and report new communities, bridges and count changes. That is an instructed host analysis, not an automatic diff or quality evaluator. Graph/query delivery is executable; a grounded final answer or accurate change attribution remains unobserved. Narration/view/export are optional presentation branches, not prerequisites for query or acceptance gates. SRC-1: `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/cli.py`; [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval), [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation), [RT-RTE-view-export](runtime.md#rt-rte-view-export).

### Verification, rejection and recovery

The workflow has different checks, not one end-to-end verifier. Extraction parsing validates shape; it does not verify source entailment. Resolver filters IDs/members; confidence is not a reference identity answer. Review admits statuses through thresholds or human choices, not universally through human approval. Build already saves flagged relations, so pending review does not quarantine them from retrieval. These limits follow [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-review-application](runtime.md#rt-rte-review-application) and [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval); SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`.

A concrete rejection path is a remaining DRAFT merge that the human rejects. The reviewer changes its status to REJECTED, the CLI writes the proposal file, and later application selects only confirmed proposals. Rejection therefore prevents that proposal's surgery; it does not undo build's earlier automatic pre-deduplication. Skip/quit leave pending drafts; EOF or interrupt is interpreted as quit. Auto-confirmation occurs before this interaction, so quitting is not a blanket cancellation of earlier automatic decisions. SRC-1: `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`; [RT-RTE-review-application](runtime.md#rt-rte-review-application).

> elif choice == "r":
>     proposal.status = "REJECTED"
>     stats["rejected"] += 1
> --- `src/sift_kg/resolve/reviewer.py`

> except (EOFError, KeyboardInterrupt):
>     return "q"
> --- `src/sift_kg/resolve/reviewer.py`

A confirmed proposal can still fail node-existence validation. The engine skips missing members or canonicals and can return zero changes; confirmation does not guarantee application to a later rebuilt graph. The caller must inspect the result, edit/rerun as appropriate, or reconstruct from inputs. Exact undo requires an external saved copy rather than merely re-running build, which can lose prior surgery. SRC-1: `src/sift_kg/resolve/engine.py`; [RT-RTE-review-application](runtime.md#rt-rte-review-application).

> if not kg.graph.has_node(canonical_id):
>     logger.warning(f"Canonical {canonical_id} not in graph, skipping merge")
>     continue
> --- `src/sift_kg/resolve/engine.py`

Earlier failures can be less visible: exhausted chunk calls may persist empty results, and a changed document can hit cache because source contents are not part of invalidation. The host owns force/re-extraction and inspection; build success is not evidence that all new facts arrived. See [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), SRC-1: `src/sift_kg/extract/extractor.py`. At delivery, no match returns a null match and empty subgraph. The skill directs broader search/alias checks rather than invented connections; the host must decide whether this resolves the user's request. SRC-1: `src/sift_kg/cli.py`, `.agents/skills/sift-kg/SKILL.md`; [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval).

Delivery consequently has two boundaries: sift-kg writes usable artifacts or returns selected graph data; the external host interprets those returns and responds to the user. No inspected execution demonstrates successful completion across both boundaries, and no source-supported acceptance test proves factual completeness or improved answers.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

Workflow role: the first paid semantic handoff. Its return is an intermediate artifact, not final delivery. The host must invoke build and must not equate successful document counts with complete extraction.

#### On [RT-RTE-review-application](runtime.md#rt-rte-review-application)

Workflow role: optional identity-maintenance branch with two distinct caller-controlled boundaries: persist decisions, then apply them to the current graph. A rejected merge blocks surgery for that proposal; it is not rollback. Quitting review can coexist with persisted automatic confirmations.

#### On [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval)

Workflow role: machine-readable delivery to the host. Ambiguity can require another exact-ID query. The host, not this route, decides when it has enough evidence and produces the final user-facing answer.
