---
description: "ScaleMAS tests bounded, citation-ranked retrieval of shared agent work; useful evidence for attention allocation, not durable knowledge acceptance."
source: https://arxiv.org/abs/2610.16120v1
captured: "2026-10-18"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 3783f1bf1f838a0a4bb42d8c4ef5687577c2f84d55e4de00a5e0923e2eb1d747
ingested: "2026-10-18"
type: types/ingest-report.md
learning_claims: true
domains: [multi-agent-coordination, retrieval, context-engineering, curation]
---

# Ingest: Scaling Multi-Agent Intelligence with Substrate-Centric Coordination

## Classification

An empirical research preprint proposing ScaleMAS and evaluating coordination, scaling, retrieval ranking, and failure tolerance through benchmarks and ablations. Authors: Zhenting Qi and collaborators affiliated with Meta, Harvard, and the Kempner Institute. The source reports its own experiments; this ingest does not independently reproduce them.

## Summary

ScaleMAS moves coordination into a task-local, append-only datastore of linked messages. Identically prompted asynchronous agents publish completed work, search by content, and visit messages by address rather than assigning work to peers. Search and visits return at most eight messages per call; ranking adds a decaying citation weight to normalized BM25 relevance. Across four tasks and two model backbones, the paper reports better performance at matched input-plus-output token counts than independent agents, debate, a coordinator, and a shared-context baseline. Scaling extends to 128 agents on two tasks, but theorem proving plateaus while contradiction-audit recall continues improving. Within this fixed message schema, read interface, and agent harness, removing citation weight lowers eight-agent BrowseComp-Plus accuracy from 60.0% to 40.8%; this isolates ranking's contribution, not the superiority of the entire decomposition. Third-party task scores use Pass@N rather than selection of one committed answer, and contradiction-audit scoring measures relaxed recall without penalizing extra reports. The datastore is discarded after each task.

## Contribution assessment (our opinion)

The paper appears to make a useful contribution to the important problem of turning additional agents into useful work rather than additional reading. Its strongest contribution is a concrete, inspectable coordination design with ranking and shared-versus-private-store ablations, plus traces showing peer evidence entering correct answers. These tests discriminate against independent sampling and relevance-only retrieval as complete explanations of the gains. The wider claim that substrate-centric coordination generally scales better remains tentative: the comparisons bundle multiple design choices, answer commitment is excluded, and the strongest continued scaling result uses a forgiving audit metric. The Web analogy explains the design motivation but does not establish originality; the retained comparisons support the tested combination rather than priority over all retrieval-based coordination systems.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source provides bounded empirical support for the inbound-link ranking hypothesis in [Notes need quality scores to scale curation](../notes/notes-need-quality-scores-to-scale-curation.md). Within ScaleMAS's fixed structured-message store and capped read interface, citation-weighted ranking improves BrowseComp-Plus performance over BM25 alone. That supports testing dependency reuse as an attention-allocation signal, not adopting citation count as a truth measure or validating the note's full composite score. The note's reserved exploration slice remains important: ScaleMAS does not test protection for low-degree material or sustained curation of a durable library.

## Learning Claims (our opinion)

ScaleMAS adapts during inference through two distinct mechanisms: agents append results and corrections that later agents consume, and deterministic citation updates change which lexically relevant messages search prioritizes. Neither mechanism updates model weights. The latter is a reuse signal, not content-directed criticism by itself.

Against the [theory builder](../notes/definitions/theory-builder.md) conditions, localized content is directly specified by identifiable messages containing claims, artifacts, rationales, and references. Consumption has stronger evidence than storage alone: the paper traces correct answers using peer-discovered evidence that the submitting agent never opened. Content-directed criticism is illustrated, rather than measured systematically, by cases where agents challenge a wrong candidate or answer an objection with new evidence. Iteration is illustrated separately by later agents taking up those retained corrections and changing their answers. Together these cases support within-run theory building by the whole agent-tool-datastore system; they do not establish how reliably every run performs criticism. Persistence ends with the task, despite messages surviving individual agents' departures.

Improved task performance is a separate finding from those conditions. Shared-versus-private-store and ranking ablations support benefits from peer access and adaptive prioritization in the tested configurations, but do not establish improved capacity across future tasks. As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) cautions, the available adaptations leave the message fields, append-only policy, retrieval eligibility, ranking rule, and supplied tool interfaces fixed. Agents can compose searches, visits, publications, and task-tool calls; the study does not test learning alternative storage or access schemes. This is not evidence that those fixed choices are mistaken, only that the reported adaptation does not compare their alternatives.

## Extractable Value

1. **Reuse can rank attention without licensing acceptance.** Within the fixed message schema and bounded retrieval interface, the citation-weight ablation supplies evidence beyond a popularity analogy: at eight agents BrowseComp-Plus accuracy is 60.0% with citation weight versus 40.8% without it. This narrows a useful test of the existing quality-score proposal to ranking already-relevant candidates, not judging their truth. [experiment]
2. **Bound the read operation, not merely the storage medium.** Search and visit caps make intake per call independent of agent count. This is a reusable interface principle, but not a bound on total run context or all displayed tokens: repeated reads, rationales, reference displays, and history management still matter. [quick-win]
3. **Separate shared discovery from durable learning.** The private-store ablation distinguishes access to peer work from private external memory; selected correction traces show criticism influencing later work within a task. Neither establishes accumulation across tasks because the shared store is discarded. [just-a-reference]

## Limitations (our opinion)

The main comparisons change bundles of coordination mechanisms. The citation ablation varies ranking inside ScaleMAS; the private-store ablation varies peer visibility. Neither isolates the necessity of append-only storage, the four message fields, reverse-link display, or the particular read cap. Common history summarization for non-SWE tasks also contributes to context management. Shared-context baseline results should not be generalized to all blackboard or filesystem designs.

Pass@N on the three third-party benchmarks measures whether any agent succeeds, not whether the group can identify and commit to that answer. Those experiments use the first 100 examples of each selected benchmark or split. Contradiction Audit credits any reported pair containing the edited snippet and ignores extra reports, so rising recall does not establish precise contradiction detection. Token counts are an inference-cost proxy, not a measurement of latency, datastore overhead, or deployment cost.

Citation-based answer-chain membership is partly circular because citations define the chain. Gold-document association is a more independent check, and the ranking ablation tests downstream utility, but neither excludes self-reinforcing errors or adversarial citation. Self-citations can raise weight. Reference-existence and rationale-coverage checks do not verify claim truth; Case 6 also records verbatim reuse without a complete citation trail. Selected success traces establish possible mechanisms rather than their prevalence.

Failure tests cover injected errors and intermittent absence, not agents publishing plausible misinformation or corrupting shared state. Persistence after producer failure is within-task availability, not durable knowledge retention. No implementation was inspected or executed for this ingest; benchmark results remain first-party paper evidence.

## Recommended Next Action

Design a bounded retrieval-ranking experiment for [Notes need quality scores to scale curation](../notes/notes-need-quality-scores-to-scale-curation.md), comparing relevance-only ranking with relevance plus dependency-reuse signals while holding the candidate pool and read budget fixed and reserving exploration for low-degree artifacts.
