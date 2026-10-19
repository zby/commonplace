---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "sift-kg workflow: agent-directed graph construction, optional identity review and later grounded retrieval at the frozen commit."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
---

# sift-kg workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a user supplying documents to an external agent, the agent building the graph and optionally improving entity deduplication, and the agent later answering a domain question from selected graph neighborhoods. This sequence is selected because the bundled skill explicitly connects graph creation, resolve/review/apply and subsequent agent retrieval. It exposes the consequential boundary between model proposals, executable review statuses and returned knowledge. These are related stages of the shipped usage, not a claim that every invocation takes the optional review branch (SRC-1, `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/cli.py`; [RT-BAP-host-skill](runtime.md#rt-bap-host-skill)).

The evidence consists of implementation and source-native doctrine at the frozen revision in [boundary](boundary.md#source-register). This is a reconstructed workflow, not an observed successful session. The external agent's actual scheduling, user confirmation and final answer are not supplied. sift-kg owns the stage computations and filesystem effects; it does not own the enclosing conversational runtime. Model calls are bounded computations with constructed inputs, not delegated autonomous agents with their own tool loops.

Additional SRC-1 inspection for this member: the complete `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/resolve/reviewer.py` and `src/sift_kg/resolve/engine.py`, plus the resolve, apply-merges and review bodies in `src/sift_kg/cli.py`. The skill supplies doctrine/design; the Python bodies supply implementation evidence. No target code, tests, examples or services were executed. Other stage details below rely on the supplied runtime records.

### 1. Request, confirmation and initial graph delivery

The skill assigns the external agent the decision to build when the user provides documents or requests creation/update. It asks the agent to confirm paid extract and resolve calls with the user. That is a host instruction, not a CLI-enforced approval gate ([RT-BAP-host-skill](runtime.md#rt-bap-host-skill)). The initiating human's approval of a paid operation does not approve every extracted assertion.

The agent supplies a document directory and output directory to extraction. Stage code selects files, reads and chunks them, optionally discovers schema guidance, obtains a first-chunk summary, and delegates each chunk's extraction to the configured model. A chunk call sees its text, domain guidance and document summary, not the whole corpus. The model returns structured proposals; code parses them, combines chunks and writes document extraction JSON. A later build invocation reads those files and saves a graph with community assignments ([RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery), [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)).

This handoff is durable file exchange, not a continuing conversation between agents. The output directory connects successive commands. Cached extraction reuse is based on model/domain-name/chunk-size metadata, not a source-content hash; changing a document under the same stem can leave old content in the reconstructed graph. Force is an available caller recovery action, not automatic freshness detection ([RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction), [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)).

Initial delivery occurs when build saves queryable graph state. Relations can already be present before review flags are handled. Structural parsing, endpoint resolution and normalization are admission checks, not independent verification that the graph matches the documents ([RT-RTE-graph-build](runtime.md#rt-rte-graph-build)).

### 2. Optional identity proposal handoff

For better deduplication, the skill directs the agent through resolve, review and apply-merges. The CLI does not automatically run the next stage: it writes proposals and prints next-command guidance. The operator or external agent remains the next-step owner. Every command must address the same intended output directory; review accepts `-o` even though the skill's short example omits it (SRC-1, `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/cli.py`).

Resolve reloads the retained graph, constructs a model client and delegates identity comparison with type-batched IDs, names, aliases and selected attributes plus domain context. It does not give each comparison the complete document evidence. The model proposes merges and confidence/reasons; code also supplies deterministic same-name cross-type proposals on the supported path. Optional embeddings select comparison groups rather than act as another deliberating agent. Resolve writes merge proposals and appends nonduplicate variant suggestions to relation-review YAML. This returns candidate decisions, not a changed graph ([RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution)).

The CLI's own handoff is explicit:

> console.print("Next: [cyan]sift review[/cyan] to approve/reject merges and relations")
> console.print("  Then: [cyan]sift apply-merges[/cyan]")
> --- `src/sift_kg/cli.py`

### 3. Review, acceptance and rejection

Review loads the YAML files. At CLI defaults, code first auto-confirms merge drafts whose minimum member confidence reaches 0.85. The relation reviewer auto-confirms at 0.85 and rejects remaining drafts at confidence at or below 0.5. The display/help says “below,” but the inspected comparison is inclusive (SRC-1, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`; [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions)).

> if entry.confidence <= auto_reject_threshold:
>     entry.status = "REJECTED"
> --- `src/sift_kg/resolve/reviewer.py`

For the remaining manual merge drafts, the human receives canonical identity, member names/IDs/confidences and the proposal reason. For relation drafts, the human sees endpoints, relation type, confidence, source/flag information and available evidence. The human can approve, reject, skip or quit. The operation is open candidate review, not evaluation against a supplied reference-answer oracle. Confidence policies and reasons do not independently establish identity or factual validity ([RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions)).

The veto is therefore conditional: manual drafts can be rejected, and decision files can be edited before apply, but default automatic confirmations do not wait for individual human approval. Setting auto-approve to 1.0 disables that automatic path. The CLI persists review mutations after the reviewer returns (SRC-1, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`).

### 4. Apply and bounded recovery

Apply reloads graph and decision files, selects confirmed merges, checks member/canonical existence, merges node data and rewrites incident edges before removing members and merge-created self-loops. Rejected relations are removed by source/target/type keys, including reversed endpoints. The CLI saves the graph only if merges or removals occurred. It does not ask another model or human to validate the resulting graph. Confirmed variant suggestions are not insertion instructions in this engine ([RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions); SRC-1, `src/sift_kg/resolve/engine.py`, `src/sift_kg/cli.py`).

The inspected rejection path is operationally different for the two products: a rejected merge is excluded from application, while a rejected relation can cause deletion of already-admitted graph content. Skipping or quitting leaves unresolved drafts for later review; it does not undo automatic approvals or decisions already made in that review call. EOF and keyboard interruption are translated to quit:

> except (EOFError, KeyboardInterrupt):
>     return "q"
> --- `src/sift_kg/resolve/reviewer.py`

The CLI then writes the modified decision file. Recovery ownership stays with the caller: resume review, edit statuses before application, or supply corrected inputs. Missing graph state stops resolve/apply and directs the caller to build; missing nodes cause individual merge mappings to be skipped. There is no inverse-merge journal in the inspected engine/save path. Rebuild reconstructs from extraction files rather than restoring an exact pre-merge snapshot, and graph-only corrections can disappear. Apply also does not regenerate community assignments or descriptions, so later retrieval may combine updated graph data with older sidecars ([RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions), [RT-RTE-graph-build](runtime.md#rt-rte-graph-build); SRC-1, `src/sift_kg/resolve/engine.py`, `src/sift_kg/cli.py`).

### 5. Later question and final delivery boundary

In a later session the skill asks the external agent to run info and topology, then query relevant entities before answering a domain question. Query reloads retained graph state, selects an exact ID or degree-ranked name/alias match and returns a selected neighborhood. Ambiguity is exposed through other matches; the agent can re-query an exact ID. Empty results trigger the skill's suggested broader search or alias lookup, not model-generated graph completion ([RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval); SRC-1, `.agents/skills/sift-kg/SKILL.md`).

The code's delivery is CLI output to its caller. The skill assigns final response composition and non-invention to the external agent:

> Read the match info (community, bridge status, connections) and the subgraph. Base your answer on actual entities and relationships from the graph. If the entity isn't in the graph, say so — don't invent connections.
> --- `.agents/skills/sift-kg/SKILL.md`

Thus persisted graph, reviewed graph mutations and returned JSON are distinct delivery points. None proves that the final user answer was correct or even produced. No supplied execution evidence establishes host compliance, successful multi-stage completion or benefit from the review branch. The source supports coordinated stage handoffs and bounded rejection/recovery mechanisms, not an end-to-end reliability guarantee.

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

#### On [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions)

Workflow handoff: reviewer return is not graph delivery. The CLI writes the modified YAML and leaves apply as a separate caller-owned invocation. Quit, including EOF/keyboard interruption, preserves prior in-memory decisions for that write and leaves unresolved manual items as drafts. Auto-confirmation precedes that manual interruption point. Evidence: SRC-1, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`; passages and workflow consequences are given above.

#### On [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval)

Workflow terminal boundary: stdout delivers selected retained graph material, while the shipped skill assigns interpretation and user-facing response to the external agent. The prescribed response must distinguish no graph match from an invitation to invent a connection. Evidence: SRC-1, `.agents/skills/sift-kg/SKILL.md`; the quoted response instruction above supports this prescription, not observed adherence.
