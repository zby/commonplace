---
description: "An RSI survey separates inherited improvement mechanisms from demonstrated improvement capacity, with bounded industrial evidence for persistent artifact adaptation."
source: https://arxiv.org/abs/2609.11873
captured: "2026-09-26"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: ec05b0134d9fa47a888aef7f46b88e2615c9c3ec2257aa677ab05136d1cba84d
ingested: "2026-09-26"
type: types/ingest-report.md
domains: [recursive-self-improvement, agent-memory, evaluation, learning-theory]
learning_claims: true
---

# Ingest: The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

## Classification

An arXiv v3 research survey and roadmap, combining a conceptual taxonomy, literature synthesis, a benchmark-trajectory analysis, and preliminary industrial comparisons. It is not one controlled demonstration of recursive self-improvement. Authors: Yi Duan and colleagues from Shanghai Jiao Tong University, Theseus Labs, Tsinghua University, and several industrial teams, including organizations whose systems appear in the industry chapter. This supplies operational access but makes those reports interested-party evidence.

## Summary

The [survey](https://arxiv.org/abs/2609.11873) organizes recursive self-improvement by which decisions a system controls: executing prescribed updates (L1), choosing improvement strategies (L2), acquiring learner-conditioned experience (L3), adapting persistently during deployment (L4), and revising mechanisms that govern subsequent improvement (L5). Within-task refinement without cross-task retention is its B0 reference case. Its most useful distinction separates structural L5—an inherited mechanism actually governs later improvement—from effective L5, where that mechanism produces better successors under comparable resources and independent assessment. The survey compares science, embodied intelligence, software, and healthcare, then reports industrial examples. Humanlaya reports fewer defective packages and less human handling after quality-system updates, holding the model, tools, and processing budget fixed; Frontis separately reports faster improvement on unseen internal tasks after accumulating cross-task experience. These bounded, company-reported results do not establish sustained compounding. The paper proposes evaluations that distinguish retention, use, task benefit, and later improvement capacity while accounting for external objectives, evaluators, and human effort.

## Contribution assessment (our opinion)

The problem is important because automation and rising task scores can obscure whether systems become better at improving. The survey's likely contribution is an operational comparison framework: identify what changes, what later rounds inherit, who retains authority, and which comparison supports a claimed gain. Its structural/effective distinction and proposed controls make several broad claims more testable. The industrial cases add potentially useful observations, but their incomplete experimental detail limits causal conclusions. The synthesis appears more valuable than the suggestion of a universal developmental ladder; neither priority over other surveys nor sustained recursive acceleration is established by the retained evidence.

## Quotes

No source quotes have been retained yet.

## Connections Found

The survey supplies an external comparison for [testing compounding in later improvement](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). Its L5 evaluation requires mechanism reuse and a successor-production comparison; its account of AIDE2 explicitly retains the inconclusive test of improvement efficiency. Frontis Horizon adds a company-reported later-improvement case, rather than another task-performance result. These accounts support keeping the questions separate, without establishing reliable acceleration across generations.

Humanlaya supplies bounded evidence for [persistent adaptation through retained system-definition artifacts](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md). Section 5.4 reports an entire quality-system revision evaluated with the same model, tools, and processing budget. It supports the existence of this adaptation pathway; it does not isolate a particular rule or establish the superiority of the fixed checker–refiner–delivery-checker decomposition.

Section 3.4.4 sharpens [validity versus learning value](../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) by separating correctness, learner-relative difficulty, and subsequent benefit, and proposing controls for adaptive acquisition. For [contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), the survey is a useful map with a qualification: the existing [Harness Updating Is Not Harness Benefit ingest](./harness-updating-is-not-harness-benefit.ingest.md) distinguishes observed loading and judged procedural match from a causal effect of skill content. The survey's stronger activation language should not erase that limit.

## Learning Claims (our opinion)

The source treats the whole improvement loop as the learning system. Experience informs candidate changes, an acceptance process selects changes, and retained state conditions later rounds. Its carriers include weights, memories, skills, code, evaluators, and research policies. This breadth exceeds Commonplace's [theory-builder](../notes/definitions/theory-builder.md) category. In particular, the source calls an accepted, inherited change an improvement; Commonplace's claim of learning still requires evidence of improved capacity for future action. An autonomy level supplies neither that evidence nor theory-builder membership.

Humanlaya is the clearest described case for comparing the four theory-builder conditions:

- **Localized content:** rules, prompts, examples, and skills state revisable content. The paper describes a concrete rule distinguishing extraction failure from unreadable source material, although it does not expose the complete versioned artifacts.
- **Consumption:** approved quality-system versions reportedly replace their predecessors in later batches. This establishes a described operational route; the version comparison does not isolate the behavioral effect of the example rule.
- **Content-directed criticism:** the extraction example identifies a mistaken inference and revises the decision rule that embodies it. That is stronger evidence for this condition than a score-only selection account, but remains a reported episode.
- **Iteration:** review and delivery feedback reportedly produce candidate revisions, held-out checks and human review select them, and later batches use the accepted versions. Four reported updates support iteration across batches; the paper does not supply a complete trace of every criticism and subsequent revision.

On this account, the human-inclusive Humanlaya process is consistent with a theory builder; humans supply ground truth and promotion decisions, so the described boundary is not autonomous. Persistence extends beyond individual task repairs into later production batches. Learning has separate, bounded outcome support: V0 and V4 differ on excluded packages under fixed model, tools, and budget. This result concerns the combined revised quality system. Following the [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), it does not compare alternative feedback representations, component boundaries, or model choices.

Two conceptual differences should remain explicit. B0 can include a theory builder whose criticism shapes another round within one task, even though the survey excludes it from persistent RSI. Conversely, weight adaptation or score-selected self-modification can meet source-side improvement criteria without establishing content-directed criticism. L5 likewise concerns inherited improvement machinery, not necessarily reflective criticism of stated methods. The source strengthens the need to test these properties separately; it does not require collapsing them into one classification.

## Extractable Value

1. **A concrete retained-artifact adaptation case.** Humanlaya reports that, after four updates, key defects remaining after automated repair fell from 9.0% to 3.7% and mean human handling from 48 to 27 minutes per task on 600 packages excluded from updating. Model, tools, and processing budget were unchanged. This adds outcome-bearing, company-reported evidence to the existing artifact-adaptation note, bounded to the complete revised quality system and retained human review. [quick-win]

2. **A test of adaptive acquisition that preserves its causal channel.** Section 3.4.4 proposes freezing the acquisition mechanism's learner-state input or using a learner-independent schedule while matching source access and total acquisition-and-learning budgets. Forcing both arms to acquire identical samples would remove the distributional adaptation being tested. This operationalizes the existing validity/value distinction; it is a proposed evaluation method, not a demonstrated benefit. [experiment]

3. **A candidate measurement of later improvement efficiency.** Frontis reports approximately 20% faster evolution on unseen internal tasks after experience from more than 100 improvement tasks, compared with a process without cross-task experience. The described protocol starts from identical agent versions and tracks iterations, time, tokens, and regressions. Shared evaluation infrastructure and human-controlled release remain in place. This is relevant to compounding measurement, but the survey lacks enough detail to assess uncertainty or identify the effect of particular retained lessons. Frontis-MA1's separate weight-training scores do not validate this Horizon result. [deep-dive]

4. **A boundary for environment-improvement claims.** Theseus reports gains of 18.65–39.67 percentage points in aggregate rubric scores when a Collection Map and Event Log enrich bare workspaces across five fixed model–harness pairings on 30 tasks. The treatment is the combined environment package, with some task regressions; it does not isolate either document's contribution or test the proposed environment–data–model co-evolution cycle. This is a bounded context-engineering reference. [just-a-reference]

## Limitations (our opinion)

The taxonomy compares responsibility transfers, not a demonstrated sequence every system must traverse. The survey itself says higher autonomy does not imply better quality or efficiency. Its broad definition of accepted improvement also permits inherited changes whose independent benefit remains unknown. Reclassifying Commonplace by this ladder would require a separate assessment of a declared system boundary.

Industrial results are supplied by organizations represented in the survey. Humanlaya's V0/V4 comparison is useful because it fixes several consequential components and uses excluded packages, but it does not isolate individual edits or report uncertainty and task-selection detail sufficient for independent reproduction. Frontis reports a relevant efficiency comparison without establishing repeated, causally attributable acceleration across generations. Theseus tests workspace interventions, not a completed recursive training cycle. No implementation was inspected or experiment reproduced for this ingest.

The benchmark-trajectory analysis normalizes heterogeneous bounded scores into headroom closed; it does not measure the effect of RSI. Its post-2026 extensions apply an illustrative formula, not a validated forecast. Similarly, the reviewed primary studies are not independent corroborations merely because this survey repeats them. For skill use, the narrower measurements retained in the primary-study ingest should constrain the survey's interpretation.

Finally, editable prompts or improvement policies do not make all consequential design choices revisable. Human-specified objectives, protected evaluators, task families, resource permissions, and fixed infrastructure remain material in the strongest examples. Better performance within those settings does not establish that their decompositions are necessary, optimal, or suitable for other KBs.

## Recommended Next Action

Update [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) with Humanlaya's bounded V0/V4 case, preserving its company-reported status, fixed model/tools/budget, whole-system attribution, and human approval boundary.
