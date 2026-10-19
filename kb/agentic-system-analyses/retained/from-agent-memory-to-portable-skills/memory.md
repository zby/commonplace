---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory mechanisms of From Agent Memory to Portable Skills: scoped trace distillation, provenance, published read-back and bounded repair in the frozen article."
run-id: AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01
source-identity: https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills
reviewed-boundary: neo4j-article-2026-10-18-99f91d4da959
---

# From Agent Memory to Portable Skills memory report

## Boundary and evidence

This report covers the documented NAMS skill-building subsystem, not the upstream memory service or host agent runtime. The frozen source is SRC-1, `article.html`, capture neo4j-article-2026-10-18-99f91d4da959, registered in [boundary](boundary.md#source-register). Direct reading covered the substantive article body and captions, including memory types, scope, pipeline, review, drift, repair, delivery, graph/prose alternatives and future work. Supplied runtime findings were checked against that text. Evidence is doctrine/design and reported operation, not implementation or observed execution.

Included memory surfaces are the scoped input memories, derived topology, synthesized claims and annotations, packaged skill, grounding metadata, review state and maintenance/version relations. Upstream ingestion and ontology extraction are input context only. Host-side skill matching, context lifecycle and task execution are outside the subsystem. Linked pages, code, remote image pixels and video are not captured. These exclusions prevent verification of admission enforcement, actual consumer loading and beneficial behavior. Frozen CLI dispatch, hooks, registered tool handlers and service implementations cannot be checked: the capture names HTTP, MCP, REST and repairStep responsibilities but contains no executable implementation.

| Entry point or memory operation | Source path and evidence | Covering records or unresolved limit |
|---|---|---|
| HTTP, MCP, dashboard scope request; Redis job; snapshot | SRC-1, `article.html`, scope and pipeline sections; direct read | [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation); caller identity, scope schemas and lock enforcement uninspected |
| Messages, decisions, reasoning, observations, reflections | SRC-1, `article.html`, memory types and raw-input paragraph; direct read | [MEM-OBJ-memory-text](#mem-obj-memory-text); original authorship and complete upstream admission unknown |
| Tool-call fields and ontology entities/relations | SRC-1, `article.html`, raw inputs and memory types; direct read | [MEM-OBJ-tool-call](#mem-obj-tool-call), [MEM-OBJ-memory-graph](#mem-obj-memory-graph); status update provenance unknown |
| Outcome-separated consolidation and topology | SRC-1, `article.html`, graph and pipeline sections; direct read plus supplied runtime | [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation), [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph); intermediate cluster persistence unspecified |
| Bounded synthesis, redaction and source checks | SRC-1, `article.html`, synthesis paragraph; direct read | [RT-CMP-llm](runtime.md#rt-cmp-llm), [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation); snippet ranking and model lifecycle opaque |
| Gates, graph/prose fallback and pending persistence | SRC-1, `article.html`, graph and gates paragraphs; direct read | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls), [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package); fallback validation shape unknown |
| Review approval/rejection and published delivery | SRC-1, `article.html`, review and delivery sections; direct read | [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery), [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption); rejection record, task selector and downstream loading uninspected |
| Drift comparison, merged/deleted source cleanup, patch/refusal | SRC-1, `article.html`, governance and repair sections; direct read | [RT-RTE-drift-check](runtime.md#rt-rte-drift-check), [RT-RTE-step-repair](runtime.md#rt-rte-step-repair); flag persistence and consumer invalidation unspecified |
| Other admission/edit/read-back paths | SRC-1, `article.html`, future-work and interface descriptions; direct read | Raw pending reads, manual replacement, direct synthesis access and patch release policy are not specified; universal review enforcement cannot be concluded |

## Core ideas

The distinguishing transformation is not mere trace retention. Scoped conversations feed outcome-separated pattern consolidation, deterministic graph derivation and bounded model synthesis; the retained skill becomes guidance for a later agent. Raw records and derived instructions have different consumers and authority. The update worker uses graph identities and recorded outcomes; a later host interprets procedure text. Neither source existence nor successful schema validation proves that the procedure is true or successful. See [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) and [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption).

Grounding remains an independently maintainable relation rather than a one-time citation. Tool-status contradiction can challenge a still-linked step, while merged/deleted sources can be followed or dropped during repair. These are different failure classes: repairing provenance does not by itself restore a failing tool. The supplied [RT-RTE-drift-check](runtime.md#rt-rte-drift-check) and [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) retain the source passages.

Context control is explicit only at the synthesis boundary: requested scope, settled snapshot, up to 400 interleaved redacted snippets, and a restricted return of claims/annotations. This resembles a separate work frame with selected input and a narrow return, not evidence of foreground compaction or a general sub-agent stack. Truncation preference, any discarded content, surviving window tail and reload pointers are unspecified. Published package loading is a separate external-context supply path, with host selection and eviction unknown (SRC-1, `article.html`, synthesis and delivery; [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

A countercase limits any universal graph claim: fewer than three recorded steps produces prose. A second countercase limits automatic maintenance: no surviving grounding causes repair refusal and a full re-distill flag. Neither alternative may be hidden by the primary graph/patch route (SRC-1, `article.html`; passages in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) and [RT-RTE-step-repair](runtime.md#rt-rte-step-repair)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-text
Label: Conversation and reasoning text

Source-native identity: messages, conversations, recorded reasoning/action/result text on AgentStep nodes, observations and reflections selected as distillation inputs. Their readable content is natural language; node identities and links are separate symbolic access/grounding metadata. Substrate: the workspace's graph-based memory in Neo4j, as described, without an inspected schema or stored instance. Lineage includes agent interactions and reasoning/execution traces; original human versus agent authorship and any prior summarization are unspecified. These inputs are raw relative to this distillation, not necessarily untouched original events. Evidence: SRC-1, `article.html`, memory-types and pipeline input paragraphs.

Consumers are the distiller and, after snippet selection/redaction, the synthesis model. Their role is evidence for candidate instructions, not already-approved skill authority. Reviewers can follow grounding back to supporting work, but which text is displayed or retained verbatim is unspecified. Upstream acquisition/admission is outside this subsystem. Subsequent transformations and software admission are described by [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation). Distinct identity: this is retained input text, not the derived [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package) or [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph); no supplied input-object counterpart after comparison.

> Its raw inputs come from all three memory types: recorded decisions (:AgentStep nodes with reasoning, action, and result), the tool calls each decision made (:ToolCall nodes with tool name, input, output, and recorded status), the entities those conversations touched, and the surrounding messages, observations, and reflections.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### MEM-OBJ-tool-call
Label: Recorded tool-call structure

Source-native identity: ToolCall node identity, tool name, recorded input/output bindings, status and decision relationships. Storage is workspace Neo4j memory. The fixed-role fields and relationships are symbolic at consolidation, topology and status-comparison consumers. Actual input/output payload encoding is uninspected: arbitrary tool results must not all be classified as symbolic just because they occupy graph properties. Readable payloads may reach synthesis as selected snippets, but exact serialization and payload selection are unknown. Evidence: SRC-1, `article.html`, raw-input paragraph quoted in [MEM-OBJ-memory-text](#mem-obj-memory-text), graph derivation and governance paragraphs.

Lineage is recorded agent tool execution, not model-invented code according to the article; actual recording fidelity and how current status is updated are uninspected. Outcome values separate patterns from anti-patterns, determine script-backed bindings and provide the governance comparison input. They are evidence and structured checks, not permission to execute a tool or a task-level correctness oracle. Consumers are [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) and [RT-RTE-drift-check](runtime.md#rt-rte-drift-check). Distinct identity: these are backing records, not their derived bindings in [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph); no supplied counterpart after comparison. Raw-call retention duration and initial admission control are unknown.

#### MEM-OBJ-memory-graph
Label: Ontology entities and grounding identities

Source-native identity: domain-ontology entities and relationships extracted from conversations, including entities those conversations touched. Storage: Neo4j workspace context graph. Form: symbolic nodes/relations for querying and reference existence; names or descriptions, where present, are not thereby fixed-rule knowledge. Exact properties and extraction representations are uninspected. Lineage: the article attributes extraction to a domain-specific ontology; extractor identity, initial admission and historical source completeness are unspecified. Evidence: SRC-1, `article.html`, memory-types discussion and raw-input paragraph in [MEM-OBJ-memory-text](#mem-obj-memory-text).

The distiller uses selected entities as evidence; the reference-checking worker uses graph identity as the authority on what exists. Repair follows merged sources and drops deleted ones. These consumers do not establish semantic entailment of synthesized claims or warrant for all ontology assertions. Distinct identity: upstream extracted knowledge differs from skill topology in [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph); no supplied counterpart after comparison. Reasoning traces and messages are not reduced to this extracted ontology object.

> The ontology is the load-bearing part: it decides that a conversation contains an incident and the service it touched, not a paragraph that mentions both.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph)

Memory lineage is trace → recurring-action clusters separated by outcome → deterministic topology and recorded-call bindings → retained Neo4j skill subgraph. Clusters are derived working material; their separate persistence is not specified. GROUNDED_IN links carry symbolic lineage/access information, not the reasoning content they reference. Graph validation consumes structural parts before persistence; repair traverses grounding at a later maintenance invocation. Downstream interpretation of the graph is not established for every host. The supporting passages are in this record and [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) (SRC-1, `article.html`, output, graph and repair sections).

#### On [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package)

The durable behavior-shaping result is procedure text plus claims, annotations and reference material, stored alongside the graph. Source metadata, scores and package identity are access/admission metadata; they must not be mistaken for the procedure's meaning or for full retained deliberation. Reference links permit reviewer access to backing reasoning, but the article does not establish that every procedure retains an explanation of why it works or that later agents read the complete reasoning. Exact exported bytes and fallback packaging are opaque. This is not an opaque embedding payload with a display summary: the described exported content is a readable skill, though no specimen is supplied (SRC-1, `article.html`, output and synthesis paragraphs; source passages in the supplied record and [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).

#### On [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)

Automatic trace-fed transformation is described from all three input classes above into retained instructions and graph structure. Source scope is a caller request, not evidence of human approval of each generated claim. Software consolidates, derives structure, filters source-less claims, checks references and applies gates; the model authors names, descriptions, completion criteria and claims. Physical persistence is the final software stage, distinct from authorship and admission. Raw-input origin includes agent decisions/tool executions and surrounding conversations/ontology extraction; labels alone do not resolve every source's original authorship.

The selector resolves scope to conversations; model-visible delivery is at most 400 interleaved PII-redacted snippets through the Python endpoint. Detailed ranking, preferential omission and any later reload of omitted snippets are unknown. The package, not an observed complete synthesis transcript, is the retained result for subsequent review and host loading. This supports a claimed trace-fed instruction-update mechanism, not measured improved future capacity (SRC-1, `article.html`, pipeline and synthesis; passages retained in the supplied route).

#### On [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery)

The reviewer is an explicit human admission authority for publication, not merely the initial caller. Review consumes steps and grounding evidence; rejection is possible, but rejection rationale, rejected-artifact retention and direct human editing/replacement are unspecified. Published SKILL.md delivery names later consumer roles and therefore goes beyond a hypothetical storage getter, without proving deployed wiring or actual use. Claude Code loading, MCP fetching and REST consumption are documented alternatives. No automatic task-matching policy or independent unsolicited push selector is described. The document lists agent-driven skill selection and deeper editing as exploration areas; that does not prove either behavior absent from every implementation (SRC-1, `article.html`, review, delivery and future-work sections).

#### On [RT-RTE-drift-check](runtime.md#rt-rte-drift-check)

The later maintenance invocation reads retained expected status and current ToolCall status. The result is a contradiction flag, distinct from revised instruction content. The UI is said to show governance issues; durable flag schema, scheduling and whether delivery consults flags are unspecified. Thus evaluation has an identified comparison consumer and a described display, but no established chain from flag to changed agent behavior. Retained grounding alone does not immunize a step from contradiction (SRC-1, `article.html`, governance and caption; passage retained in supplied route).

#### On [RT-RTE-step-repair](runtime.md#rt-rte-step-repair)

Cleanup changes the grounding of one step by survivor traversal/deletion removal, followed by graph revalidation and a superseding patch. The derived durable result is a revised skill version, not a claim that historical traces are rewritten or obsolete versions physically deleted. Software admits salvageable grounding changes and refuses when none survives; the reviewer sees a one-step diff, but mandatory human patch approval is unresolved. Supersession identifies the intended later review/use product, not an inspected consumer version selector. Retention of repair rationale beyond provenance/diff, automatic re-distillation after refusal, rollback and installed-copy withdrawal are unspecified (SRC-1, `article.html`, repair; both branches quoted in supplied route).

## Write side

Input acquisition is upstream: the article describes conversation retention, ontology extraction and reasoning/tool traces but does not establish their initial human/software admission controls. This unknown does not suppress known later transformations. The chain is [MEM-OBJ-memory-text](#mem-obj-memory-text), [MEM-OBJ-tool-call](#mem-obj-tool-call) and [MEM-OBJ-memory-graph](#mem-obj-memory-graph) → scoped settled snapshot → outcome-weighted consolidation → graph or thin-scope prose → sourced textual synthesis → software gates → pending Neo4j package → human publication decision. The detailed admissions and veto owners are in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation), [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) and [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery).

The gate thresholds, PII checks, dropped unsourced claims and split suggestion are documented controls. They do not establish semantic truth, absence of sensitive content or equal enforcement on alternate writers. Human starting of a job is not per-content approval. Human publication approval is explicit; human curation of repaired content is not equally specified. Manual edits, replacements and permission boundaries remain unresolved.

Maintenance separates detection, repair and withdrawal. Status comparison can flag a contradiction without changing content. Repair can retain a patch with new grounding, or decline and flag full re-distillation. Neither event proves removal of a published skill, deletion of a prior version or invalidation of a host's cached package. References preserve a path to supporting work; no supplied skill shows whether explanatory reasons survive selection, synthesis and export or are consulted in later execution (SRC-1, `article.html`; [RT-RTE-drift-check](runtime.md#rt-rte-drift-check), [RT-RTE-step-repair](runtime.md#rt-rte-step-repair)).

## Read-back

There are distinct later consumers, not one universal recall route:

- The scope-requested distiller reads retained conversations, traces and entities; it bounds model input through snippet selection/redaction. This is requested evidence selection, not unsolicited context push. The 400-snippet bound is not a token budget or a completeness guarantee ([RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)).
- The reviewer reads persisted steps and follows evidence links to backing work. The selected skill/step is the target; exact UI evidence serialization and display budget are unspecified ([RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery)).
- Later agents receive published packages via host loading, MCP or REST. Publication state is the documented condition; task relevance ranking, version matching, load budget and eviction/reload policy are unknown. The force is interpreted procedural guidance, not a verified executor contract or tool permission grant ([RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption)).
- Governance and repair consume retained status expectations and grounding respectively. They provide comparison/maintenance authority, not proof of downstream task success. A flag can reach a governance display; a patch supersedes a prior version, but downstream automatic update/revocation remains unresolved ([RT-RTE-drift-check](runtime.md#rt-rte-drift-check), [RT-RTE-step-repair](runtime.md#rt-rte-step-repair)).

All are article claims, with no observed activation or beneficial effect. A generic Neo4j storage capability is not counted as an additional read-back route. No foreground conversation compaction, summary checkpoint, verbatim-tail retention or reload stub is specified within this subsystem; the inspected article cannot determine host implementations.

## Integration issues

1. No correction to a supplied runtime fact is required. Existing graph/package/routes are annotated rather than duplicated. The three new input objects are distinct backing material, with comparisons in their declarations; no possible duplicate with a supplied record was found.
2. [MEM-OBJ-tool-call](#mem-obj-tool-call) leaves tool payload forms and current-status update provenance unresolved. This prevents a universal symbolic classification and limits interpretation of contradiction detection in [RT-RTE-drift-check](runtime.md#rt-rte-drift-check).
3. Upstream admission/authorship and extraction fidelity remain unknown for [MEM-OBJ-memory-text](#mem-obj-memory-text) and [MEM-OBJ-memory-graph](#mem-obj-memory-graph). Referenced graph existence cannot substitute for source trust or entailment in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation).
4. Fallback shape, intermediate cluster retention, snippet omission policy and complete rationale delivery remain unspecified in [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package) and [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation). This prevents complete-context, all-graph and preserved-explanation conclusions.
5. Direct reads/writers, reviewer editing authority, rejection persistence, patch re-review and publication rules are not exposed. [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls), [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery) and [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) cannot establish universal human control over all revisions.
6. Drift schedule, flag persistence, consumer flag checks, version selection, rollback, withdrawal and installed-copy invalidation remain unresolved. The governance/patch routes above cannot prove that a detected issue changes a later agent's instructions. Source basis for these limits is SRC-1, `article.html`, governance, repair and delivery sections; the capture gives no implementation or execution artifact resolving them.

## Limitations and checks

Identity recheck: frontmatter repeats the supplied run ID, capture label and source identity exactly. Direct source reads were restricted to the registered capture; no linked resources, target services, prior analyses or executable target examples were used. Method checks used the supplied job, member types, worker rules, collection contract and records contract.

The source supports described trace-fed instruction construction and maintenance, not exercised learning, verified host compliance, universal graph execution or causal benefit. Parameter lifecycle remains uninspected as recorded in [RT-CMP-llm](runtime.md#rt-cmp-llm); persistence outside weights does not imply changed model parameters. No actual skill content or consumer decision trace supports an additional theory-builder assessment. Keeping reasons reachable through provenance does not establish criticism of an explanation or autonomous improvement of this subsystem.

Deterministic validation: validate-output passed for this invocation. This checks structure, identity and quotation occurrence, not analytical truth, consumer activation or job acceptance.
