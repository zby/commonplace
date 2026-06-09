---
description: "Ingest of the 3D-8Q LLM-memory survey: how object/form/time taxonomy fits our memory-axes and cognitive-analogy-skepticism notes"
source_snapshot: "from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.md"
ingested: "2026-06-09"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [agent-memory, learning-theory, memory-taxonomy]
---

# Ingest: From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs

Source: from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.md
Captured: 2026-06-09
From: https://arxiv.org/html/2504.15965v2

## Classification

Type: scientific-paper -- arXiv survey (2504.15965v2) with a formal taxonomy, a structured literature map, and dozens of cited systems; no original experiment, but methodology and citation density place it firmly in the scientific-paper class rather than essay.
Domains: agent-memory, learning-theory, memory-taxonomy
Author: Huawei Noah's Ark Lab (Wu, Liang, Zhang, et al.). Industrial research lab with a track record in retrieval and recommendation; credible as a landscape survey, with the usual survey caveat that it organizes rather than tests.

## Summary

The survey maps human memory onto LLM-driven AI memory and proposes a 3D-8Q taxonomy: three orthogonal dimensions — object (personal vs system), form (parametric vs non-parametric), time (short- vs long-term) — crossed into eight quadrants, each tagged with a human-memory analogue (sensory, working, episodic, semantic, procedural). It walks the human side (Multi-Store Model, encoding/storage/retrieval, consolidation, reconsolidation, reflection, forgetting), then catalogues AI systems by quadrant: multi-turn dialogue and memory-RAG (mem0, MemoryBank, A-MEM, HippoRAG) for personal non-parametric memory; prompt/KV caching and PEFT/knowledge-editing (Character-LLM, WISE, MemoryLLM) for parametric memory; ReAct/Reflexion/Voyager/ExpeL/Agent Workflow Memory for system reflection-and-refinement; vLLM/ChunkKV for KV management. It closes with six future directions (multimodal, stream, comprehensive, shared memory, collective privacy, automated evolution). Read it for a broad, well-organized field map and a shared vocabulary, not for novel mechanisms or evidence.

## Connections Found

The companion [connect report](../reports/connect/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.connect.md) found no existing note that cites this snapshot and frames the load-bearing signal as reverse-edge `evidence` candidates. The strongest fit is the cognitive-analogy-skepticism cluster: [three-space-agent-memory-echoes-tulvings-taxonomy](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) (the note currently cites only a single tweet for the human-taxonomy-to-agent move; this is a paper-grade second instance, and the survey's own admission that its quadrants reduce to object/form/time policy dimensions supports the note's "the analogy may be decorative" hedge) and [psychology-to-agent-transfer-needs-per-principle-failure-mode-testing](../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) (the survey is a large worked example of the wholesale-mapping move that note warns against). The second cluster is artifact/operational axes: the survey's *form* dimension (parametric/non-parametric) is an independent external parallel to our [representational-form](../notes/definitions/representational-form.md) axis and its substrate-vs-form distinction in [axes-of-artifact-analysis](../notes/axes-of-artifact-analysis.md); the four memory-processing stages (construction, management, retrieval, usage) map onto the operational axes in [memory-design-adds-operational-axes-to-artifact-analysis](../notes/memory-design-adds-operational-axes-to-artifact-analysis.md). The survey's quadrant-VI (Reflexion, Voyager, ExpeL) and quadrant-VIII (WISE, MemoryLLM) populate the two behaviour-change mechanisms in [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md). Connect also flagged that [agentic-memory-systems-comparative-review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) reaches a compatible "storage form under-determines design" conclusion from a different taxonomy (substrate/lineage/authority/activation). What the source adds beyond existing connections: a third independent top-level memory taxonomy that, like ours, concludes storage form is not the consequential fork; and a survey-level catalogue of named systems per quadrant. As context only (not actionable here), connect noted a coverage gap — the survey's "shared memory / collective privacy" future direction has no corresponding KB note.

## Extractable Value

1. **Third independent taxonomy that converges on "form is not the fork."** -- The survey explicitly states parametric short-term personal and system memory "overlap technically" and differ only by *focus* (individual-input processing vs task-execution reuse). This is external corroboration, from a different axis set, of our recurring claim that storage form/substrate under-determines design — strengthening [axes-of-artifact-analysis](../notes/axes-of-artifact-analysis.md), [representational-form](../notes/definitions/representational-form.md), and the [comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md). [just-a-reference]

2. **Paper-grade second instance for the Tulving-mapping note.** -- [three-space-agent-memory-echoes-tulvings-taxonomy](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) currently rests on a single tweet. The survey makes the same human-taxonomy-to-agent move at scale, and its self-reduction to object/form/time is direct support for the "decorative analogy" hedge. Upgrades the note's evidence base from one informal source to one informal plus one paper. [quick-win]

3. **A worked example of unguarded wholesale cognitive transfer.** -- The survey maps consolidation, reconsolidation, reflection, and forgetting onto AI mechanisms with no per-principle failure-mode testing — exactly the move [psychology-to-agent-transfer-needs-per-principle-failure-mode-testing](../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) cautions against. Useful as a citable specimen of the failure pattern, not as evidence the analogies hold. [just-a-reference]

4. **Per-quadrant system catalogue for the two continual-learning mechanisms.** -- Quadrant-VI (non-parametric reflection: Reflexion, Voyager, ExpeL, Buffer of Thoughts, Agent Workflow Memory) and quadrant-VIII (parametric editing: WISE, MemoryLLM) give [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) a ready list of instances of its readable-artifact vs distributed-parametric behaviour-change split. [just-a-reference]

5. **Vocabulary: the four memory-processing stages (construction, management, retrieval, usage).** -- A clean external naming of the long-term-memory lifecycle that parallels the operational axes (capture, derivation, activation, lifecycle) in [memory-design-adds-operational-axes-to-artifact-analysis](../notes/memory-design-adds-operational-axes-to-artifact-analysis.md). Improves retrieval and gives an external label set to cite when discussing memory operations. [just-a-reference]

6. **Named coverage gap: shared memory and collective privacy.** -- The survey's cross-agent / cross-domain memory-sharing and group-level-privacy future directions have no KB note; nearest hits are about coordination and authority, not aggregated-data privacy. A candidate topic if cross-agent memory becomes in-scope for our methodology. [deep-dive]

## Limitations (our opinion)

This is editorial judgment. As a survey it organizes the field but tests nothing, so it cannot tell us *which* of its eight quadrants matter or *when* a human-memory analogy actually predicts agent behavior — the central weakness our own [psychology-to-agent-transfer](../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) note identifies. The 3D-8Q framing is also partly decorative: by the authors' own admission several quadrants collapse (parametric short-term personal vs system "overlap technically"), and the human-memory labels (sensory/episodic/procedural) are attached to quadrants by analogy rather than derived from any functional difference, so naming a quadrant "procedural memory" explains nothing the object/form/time coordinates did not already fix. The mapping is hard to vary — almost any AI memory mechanism can be slotted into some quadrant and given a human-memory name, which makes the taxonomy more a filing scheme than a predictive theory. Treat the system citations as a discovery index, not as validated comparisons: the survey reports what each system claims, not head-to-head results, and gives no baselines. The future-directions section is aspirational and should not be read as evidence those directions are tractable.

## Recommended Next Action

Add a reverse-edge `evidence` link from [three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) to this snapshot (its strongest, lowest-effort fit: the note currently cites only one tweet and this is a paper-grade second instance plus support for its "decorative analogy" hedge). Authoring that edit is a separate explicit step — run `cp-skill-write`/`cp-skill-connect` follow-through on that note rather than treating it as done here. Do not pursue the cross-taxonomy synthesis note flagged by connect unless a writer judges it adds beyond the existing operational-axes and four-field notes.
