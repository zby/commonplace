---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "From Agent Memory to Portable Skills: NAMS skill distillation and governance as documented in the frozen Neo4j article capture."
run-id: AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: subsystem-only
reviewed-boundary: neo4j-article-2026-10-18-99f91d4da959
analysis-cutoff: "2026-10-18"
evidence-tier: doc-grounded
source:
  kind: capture
  identity: https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills
  revision: neo4j-article-2026-10-18-99f91d4da959
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html
  sha256: 99f91d4da959125e4a24a1989523e8acd7f3daa28b72d11de635b0a880f4272c
---

# From Agent Memory to Portable Skills boundary

## Boundary and evidence

The target is the NAMS skill-distillation and governance subsystem described by William Lyon in the Neo4j article, not all of NAMS or an enclosing agent runtime. Its intended use is to turn scoped workspace memory into a portable skill for later agents. Classify it as a **builder or improvement plane**, with a **subsystem-only** boundary: the article describes a model-assisted artifact-building pipeline, admission gates, human review and subsequent maintenance. This qualifies as an agentic mechanism because it calls a model during synthesis and produces instructions for model-driven consumers (SRC-1, `article.html`, “Inside the Distillation Pipeline” and “How a Published Skill Reaches Your Agents”).

The article states:

> Distillation is a graph-backed, pollable job. A trigger enqueues a run on a Redis stream; the distiller runs a seven-stage pipeline:
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> For synthesis, the distiller calls out to a Python grounded-synthesis endpoint, and the LLM&rsquo;s role there is deliberately narrow.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

Included are the article's descriptions of workspace memory as input; HTTP, MCP and dashboard initiation; scope resolution, snapshot locking, consolidation, topology derivation, synthesis, gates and persistence; human review; drift detection and step repair; and publication to agent consumers. These are descriptions of responsibilities, not inspected executable paths (SRC-1, `article.html`, “Distilling a Skill from Memory” through “Inside the Distillation Pipeline”).

The consumer boundary is explicitly documented:

> Because the artifact is a standard SKILL.md package, the same skill loads into Claude Code, MCP clients, REST callers, or any other agent framework.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

External dependencies named in this account include Neo4j memory storage, Redis job delivery, a Python synthesis endpoint and its LLM, a human reviewer, and host agents that load the exported skill. The host agents' task execution and their production of memory remain outside this subsystem; their correctness is not attributed to the distiller. The article describes those interfaces but supplies neither client implementations nor end-to-end execution evidence (SRC-1, `article.html`, “Inside the Distillation Pipeline,” “Nothing Ships Unreviewed,” and “How a Published Skill Reaches Your Agents”).

### Evidence limits and exclusions

- **Frozen document, not a repository audit.** The source is the exact HTML response captured from the supplied URL on 2026-10-18, with the capture label and SHA-256 above. The inspected article body includes all substantive sections and resource links. No repository tree, shipped entry points or caller code is present in this capture. This prevents implementation-level verification of pipeline, maintenance and consumer behavior, and prevents a whole-system classification of NAMS.
- **Other NAMS responsibilities excluded.** General memory ingestion, ontology extraction and recall are considered only as the article's stated input context. Their implementations and operational guarantees cannot be inferred from this boundary.
- **Linked material not captured.** The live NAMS service, linked documentation, walkthrough, AIP paper, livestream, and remotely referenced images are outside the frozen evidence. HTML captions are included; image pixels, video contents and linked pages are not. This prevents verification of UI behavior, protocol conformance, evaluator setup or benchmark results against their underlying evidence. References to AIP evaluation in the article are secondhand reports, not causal experiments observed in this run.
- **No execution artifacts.** No actual memory graph, generated skill package, review record, tool trace or controlled experiment accompanies the article. Statements about deployed operation remain attributed reports. Neither successful skill execution nor measured improvement of NAMS is established.

The applicability cutoff is 2026-10-18, the supplied run date and capture date. The article is dated August 6, 2026; that publication date is not a software version pin. The overall evidence tier is **doc-grounded**. The capture supplies doctrine/design and reported operation only. Later changes to the live page or service do not enter this run.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | capture | `https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills` | neo4j-article-2026-10-18-99f91d4da959 | doctrine/design; reported operation | Frozen HTML at the absolute source.path above; article body from “Grounded skill distillation on a context graph” through “Resources.” Doctrine/design: memory model, skill graph, pipeline stages, gates, review and repair contracts. Reported operation: availability in NAMS, published-skill delivery and secondhand AIP evaluation. | `article.html`: “Distilling a Skill from Memory,” “What Distillation Produces,” “Nothing Ships Unreviewed,” “Keeping Skills Honest: Governance and Drift,” “Bounded, Node-Level Repair,” “How a Published Skill Reaches Your Agents,” “AIP Procedure Graphs in NAMS,” “Inside the Distillation Pipeline,” “Try It Today”; quotation attributions resolve to the registered absolute capture path. | No implementation, inspectable run or experimental artifacts in the capture. Linked resources and remote media are not frozen. Prevents code-grounded guarantees, whole-NAMS loop coverage, independent interoperability verification and causal performance claims about NAMS. |
