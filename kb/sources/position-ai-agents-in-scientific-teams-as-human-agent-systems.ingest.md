---
description: "Position paper restates human-inclusive evaluation for scientific AI, but the captured page neither resolves contribution attribution nor exposes enough evidence to advance KB methodology"
source: https://huggingface.co/papers/2608.14667
captured: "2026-08-20"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 1230de7b14abcd6d7e701adfcabf585220d87e52952e2efd0af9c358f79bd977
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [human-agent-systems, scientific-discovery, agent-evaluation, function-allocation]
---

# Ingest: Position: AI Agents in Scientific Teams Should Be Studied as Human-Agent Systems

## Classification

An arXiv position paper whose abstract reports literature and empirical analysis plus real-world case studies in support of a research agenda for human-agent scientific teams.
Author: a 14-author team; the captured page identifies the National Laboratory of the Rockies, but does not expose individual affiliations, author credentials, or review status, so authority rests on the argument and evidence rather than the page metadata.

## Summary

The authors argue that evaluating autonomous “AI Scientists” in isolation misses the social system that produces scientific work. They propose the human-agent pair as the unit of analysis, identify reduced inquiry diversity as a near-term risk, and call for models of collaboration benefit and coordination cost. This is a useful scientific-team application of human-inclusive evaluation, but the current KB already states the broader system-boundary and actor-allocation claims. The captured Hugging Face page contains the abstract and community descriptions, not the paper's full methods, evidence, or proposed framework.

## Connections Found

This source is primarily a domain-specific restatement of [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): causally consequential human participants and interaction protocols belong inside the evaluated system boundary. [Methodological and computational closure track different changes](../notes/methodological-and-computational-closure-track-different-changes.md) already supplies the more discriminating human, computational, and joint actor profile that the captured page does not.

The paper's measurement agenda encounters the unresolved problem in [Measuring autonomy well enough to see it improve is an open problem](../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md). Coordination cost measures burden, not who supplied the decision content that produced an outcome. Any scalar synergy or work-share score would still need a commensurable per-function decomposition, and the captured page does not show whether the proposed framework provides one. [CRUX's autonomous-research shadow evaluation](./can-ai-agents-conduct-open-ended-ai-research.ingest.md) remains the closest empirical comparison, but this source adds only the proposal to study interactive configurations rather than autonomous ones.

## Extractable Value

1. **Inquiry diversity is a candidate system-level outcome.** The paper foregrounds reduced diversity of scientific inquiry as a near-term risk that single-answer accuracy and final-paper quality cannot reveal. The claim is a useful experimental lead, but the captured page provides no measure, baseline, or effect size. [experiment]

2. **The proposed synergy framework is a targeted full-paper retrieval question.** Its value would depend on whether it distinguishes coordination burden from causal contribution and compares matched role, initiative, feedback, and authority allocations. Nothing in the current capture establishes that it does. [deep-dive]

3. **The scientific-team framing is an independent domain example.** It corroborates the need to evaluate causally consequential humans and agents together, but does not extend the KB's existing general account of system boundaries or actor allocation. [just-a-reference]

## Limitations (our opinion)

The durable source is a Hugging Face abstract-page capture, not the 15-page paper. The abstract supports the position, the reduced-diversity concern, and the existence of literature, empirical, and case-study analysis. Details about de-skilling, two named case studies, and a benefit-versus-coordination-cost framework come from the page's submitter-authored community description. The capture does not expose literature selection, case protocols, equations, measures, results, citations, or counterevidence. Those details should not become load-bearing empirical claims until the PDF is captured and read.

The source does not currently advance the KB's methodology. Human hours, coordination costs, output volume, and final-artifact quality measure different things; none by itself attributes the decision-bearing contribution of the human and agent. Per-function actor allocation avoids a scalar work-share claim for one system, but comparisons still require commensurable decompositions. The captured page does not show whether the paper acknowledges or resolves that problem.

The fixed-decomposition limit is substantial. The page does not establish which signals and interaction histories conditioned the agents, which scientific operations the humans and agents could compose, or which mappings the selected models and experts could express. The scientists, models, tasks, dyadic pair boundary, interfaces, role allocation, timing, source access, and outcome measures appear fixed outside the reported cases, but the capture does not disclose enough detail to audit them. Reported augmentation therefore shows at most that particular arrangements were useful in their contexts; it does not show that the human-agent pair is the best decomposition or that adjacent fixed choices caused the result. No ablation visible in the capture varies those choices.

The proposed pair can itself be too narrow for the paper's “scientific teams” subject. Multiple researchers, multiple agents, institutions, publication incentives, shared tools, literature, and reviewers can all affect the outcome. A dyadic analysis may improve on model-only evaluation while still excluding consequential organization-level causes. Likewise, the page gives no effect size or baseline for reduced inquiry diversity, so that risk is a hypothesis and retrieval lead here, not established population evidence.

Finally, this is an advocacy paper. Its central claim is useful because it redirects measurement, but favorable cases of complementarity cannot by themselves show when collaboration helps, when it merely shifts hidden work to experts, or when agent advice homogenizes rather than expands inquiry.

## Recommended Next Action

Keep this paper as a source-only reference. Do not promote its claims into a theory note from this snapshot; reconsider only if a full-paper capture supplies inspectable inquiry-diversity evidence or a contribution-attribution method that addresses per-function commensurability.
