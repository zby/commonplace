---
description: "SoL-Pi discovers reusable harness changes that lower full-task cost with some capability loss; recoverable observations and interface revision inform context economics and bounded learning claims."
source: https://arxiv.org/abs/2609.20519
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 7fc142fbc559ad54f634dc1faba557b633b5c06924e7372557fdde6b3e21dc6f
type: kb/sources/types/ingest-report.md
domains: [agent-harnesses, context-engineering, automated-research, learning]
learning_claims: true
---

# Ingest: SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

## Classification

An empirical research paper describing automated harness development, benchmark comparisons, component evaluations, and one development lineage. Haozhe Liu and coauthors report their own system and experiments; the captured paper identifies NVIDIA affiliation. The [paper](https://arxiv.org/abs/2609.20519) supplies research evidence rather than independent replication.

## Summary

SoL-Pi searches for reusable efficiency improvements to the Pi coding-agent harness without changing model weights. Development covers 152 proposed directions, 535 executable environments, more than 3,000 runs, and more than 60,000 interactions. Four retained mechanisms combine edits with known follow-up commands, compact context according to estimated future savings, replace repeated large observations with retrievable handles, and reduce selected logs through checked evidence receipts. On the reported 51-task EdgeBench aggregate, the fixed four-component stack reduces token traffic by 49.0% with GPT-5.6 Sol and 44.7% with Opus 5, and API cost by about one third relative to Pi, while average scores fall from 44.833 to 42.003 and 44.756 to 42.224. These are outcomes for the integrated Pi extensions and reported task setup, not evidence that this component arrangement is optimal. Eleven tasks serve frozen-candidate acceptance and 40 serve final generalization evaluation. The paper's separate performance configuration selects the highest-scoring single component per backend. Reusing the improved harness to make successor discovery cheaper remains future work.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies bounded empirical support for the aggregate-cost side of [context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md). In the GPT-5.6 Sol full-stack comparison, cache reads fall from 2.1326 billion to 1.0605 billion tokens while cache writes rise from 0.0141 billion to 0.0316 billion; reported cost falls from $1,339 to $894, alongside the score decline above. This establishes a useful cost–quality tradeoff in the tested configuration, without testing the note's claim that per-window feasibility is the binding concern.

ObservationPack and the Evidence-Preserving Reducer provide a concrete comparison for [summary sufficiency and source fallback](../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md). Exact archived outputs remain available, and receipts undergo deterministic checks. Those checks establish properties of selected evidence, not that omitted material is irrelevant to every later diagnostic question. Finally, the component evaluation illustrates [the limit imposed by an experiment's actual contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): adding each mechanism separately to Pi tests standalone additions; comparing different configurations on their own triggered-task subsets does not isolate interactions among mechanisms.

## Learning Claims (our opinion)

The source's learner is a research process that reads execution trajectories, proposes explanations of overhead, implements changes, receives independent review and development feedback, and retains candidates and evidence. Capability metrics, tolerances, and efficiency metrics remain outside optimizer control. Passing candidates must satisfy capability tolerances and improve an efficiency metric; nondominated candidates survive. Search lineages use disposable copies of a shared skill template, and their modified orchestration code is discarded. Retained harness changes are therefore the demonstrated persistent update; persistent improvement of the research machinery is not established.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), at the whole development-system boundary, conditions 1 and 2 are met: proposed explanations of overhead and harness changes are stated, and they guide experiments and agent behavior. Condition 3 is met as reported. In the Action Fusion lineage, a proposed explanation of avoidable round trips guides experiments, and unreliable prompt-only triggering, a finding against the prompt's content, motivates an explicit tool-schema change. That is stronger than outcome-only variant selection. Condition 4 fails and decides the verdict. The development campaign addresses one problem, making the Pi harness cheaper within capability tolerances, and its many directions and runs are one pass of error elimination on it. The four retained mechanisms are then used unchanged on evaluation tasks, which reuses the product. Search-lineage code is discarded, and taking the improved harness up as the starting point of successor discovery remains future work. As a separate learning claim, the reported cost improvements support increased efficiency capacity, subject to the observed capability losses. The paper does not isolate the benefit of retaining explanations or criticism separately from retaining executable changes.

The lineage also demonstrates why [the effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters. Prompts and tool schemas can change; the six proposal families organize search without fixing implementation boundaries. The research process can therefore revise an interface rather than merely optimize behavior behind it. Fixed model weights, development environments, final capability criteria, and the overall search/validation arrangement still bound the evidence. A locally introduced trigger-rate metric guides development alongside task score; it should not be confused with authority to rewrite the fixed end-task acceptance criteria. No comparison establishes the optimality of the search arrangement, a breadth/depth scaling law, or compounded improvement across successor research cycles.

## Extractable Value

1. **A measured case for full-task context accounting.** The tested full stack pays extra cache-write cost to reduce repeated reads, lowering cost despite lower scores. This strengthens the existing context-economics discussion while requiring capability and expense to remain separate outcomes. Historical prices and the Pi-based configuration limit numerical reuse. [quick-win]
2. **Recoverable observation reduction with explicit checks.** ObservationPack sends outputs above 10 KiB in full for two provider requests, then substitutes handles and excerpts. The reducer first processes selected build/test logs of at least 4 KiB, checks schema, hash, status, exact quotations, and size reduction, and falls back on failure or suspected credentials. Reads and searches bypass it; its receipts bypass ObservationPack. This is a concrete candidate design for testing which source reads a projection can safely replace, without treating exact quotation as proof of completeness. [experiment]
3. **A documented move from prompt revision to interface revision.** Action Fusion's 27-iteration lineage makes a mechanism directly expressible through the tool schema after prompt-only triggering proved unreliable. It gives the KB a specific case of an outer learner changing its agent's action interface, with observed outcomes bounded by the reported development and evaluation setup. It does not show that recursive improvement of the optimizer itself occurred. [just-a-reference]

## Limitations (our opinion)

The strongest numerical claims concern an efficiency–capability tradeoff. On 63 CPU-only Terminal-Bench 4 tasks, SoL-Pi solves 15 against Pi's 18 despite reducing total cost from $286.45 to $211.12. On IMO 2026 it matches Pi at three of six verified problems; Codex solves five. Lower cost per score or solved task does not establish equal capability. The 51-task EdgeBench tables combine acceptance and final-evaluation tasks, so the entire aggregate should not be described as an untouched final-only evaluation.

The performance configuration is selected separately from the reported single-component scores: ObservationPack for GPT-5.6 Sol and Action Fusion for Opus 5. Its gains are not those of one configuration transferred unchanged. The fixed full-stack transfer is a distinct result. Component comparisons vary additions to Pi, while triggered-subset comparisons leave interactions unidentified. They do not compare all alternative decompositions or establish that every component is necessary.

The study supplies no independent search replication or uncertainty estimates. The swarm comparison has one two-hour run per condition: SoL-Pi workers achieve 1,127 cycles at $60.11 versus Pi workers' 1,366 at $82.12, while a single Codex agent achieves 1,333 at $39.20. These observations do not establish general swarm superiority. API costs use August 17, 2026 prices. The compaction gate does not separately price its summarization call, limiting its local cost estimate. No implementation was inspected or executed for this ingest; mechanism descriptions and outcomes remain paper-reported. Broader search coverage, multi-backend development, and recursive reinvestment of savings remain proposed experiments.

## Recommended Next Action

Update [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) with the bounded cache-read/cache-write cost comparison, retaining the accompanying score loss and limiting its evidential role to aggregate economics.
