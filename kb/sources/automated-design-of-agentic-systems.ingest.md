---
description: "Meta Agent Search feeds an archive of agent code and scores into iterative design, with evidence for agent transfer but fixed outer-loop machinery."
source: https://arxiv.org/abs/2408.08435
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: a848e5eb3f2a988749433e666b6c5295942f89f2569813bf73357bd0c01ad57b
ingested: "2026-09-17"
occasion: "How the meta-agent's archive is consumed; whether discovered agents transfer across domains; where people intervene."
learning_claims: true
type: types/ingest-report.md
domains: [agentic-system-design, meta-learning, transfer]
---

# Ingest: Automated Design of Agentic Systems

## Classification

This is a full scientific paper presenting an optimization method, benchmark experiments, transfer tests, and an initialization ablation for automated agent design.
Author: Shengran Hu, Cong Lu, and Jeff Clune are academic researchers affiliated with the University of British Columbia and Vector Institute; the paper was published at ICLR 2025.

## Summary

The paper defines Automated Design of Agentic Systems as search over an agent representation against an evaluation function, then instantiates it as Meta Agent Search. A foundation-model meta-agent receives an archive initialized with baseline agents and updated with discovered agent programs and evaluation metrics; it proposes a new code-defined agent, performs prompted self-reflection, repairs runtime errors, and adds the evaluated result to the archive. On ARC and four question-answering benchmarks, the discovered agents outperform the authors' hand-designed baselines. Selected agents searched on MGSM also outperform or match those baselines on held-out math and non-math benchmarks, and selected ARC agents transfer across several foundation models. These experiments support transfer of particular agent programs within the tested settings, while leaving the transfer of the search procedure and its human-designed outer loop untested.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical case for treating the deployed agentic system, rather than model weights alone, as the behavior-changing unit: search changes executable workflows and prompts around fixed foundation models, as described in [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). It also supplies a useful boundary case for [Factory construction does not establish knowledge acquisition](../notes/factory-construction-does-not-establish-knowledge-acquisition.md): the archive is consumed as in-context examples and stepping stones for constructing further programs, but the experiment does not identify a reusable production theory acquired by the system. The reported cross-domain result transfers discovered task agents, not an improvement procedure that demonstrably improves later improvement, which bears on [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). Finally, the experiments expose the fixed layer described by [An omitted improvement-loop function and a frozen one need different repairs](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md): people supply the meta-agent prompt, framework, task descriptions, validation objective, iteration budget, baselines, and safety inspections, while the search updates only the generated agent's `forward` program.

## Learning Claims (our opinion)

On the paper's terms, Meta Agent Search performs iterative optimization in program space: archive-conditioned proposal and self-reflection generate an agent program, validation performance evaluates it, and the program plus its metric is retained for later proposals. This is not theory refinement in Commonplace's sense because the retained archive entries are candidate designs and scores, not an explicit tentative theory whose consequences and parts are diagnosed and revised. The archive nevertheless has a direct consumption path: its contents enter the next design prompt, and the search trace suggests that later agents recombine earlier design patterns. That trace is evidence consistent with archive-mediated cumulative search, but it does not isolate the archive's causal contribution.

The effective update space is broad within the generated `forward` function: task information can condition behavior; the program can compose foundation-model calls, prompts, roles, feedback, refinement, and ensembling; and a coding model can express many mappings among them. The experiment fixes the basic framework and APIs, archive protocol, proposal and reflection prompts, error-repair procedure, evaluation metric and validation data, task partition, and outer iteration. Improvement inside this space therefore does not validate those fixed choices, as [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts. The empty-initialization ablation varies only the initial baseline agents: it supports a claim about initialization in these runs, not about the remaining decomposition or the archive's later consumption.

## Extractable Value

1. **Archive consumption is concrete prompt conditioning.** Each iteration exposes the discovered-agent archive to the meta-agent, asks it to compare prior implementations, and retains the next program with its evaluation metric. This specifies a consumption path rather than treating retention alone as learning. [quick-win]
2. **Transfer attaches to the discovered agent artifact.** The authors run top MGSM agents unchanged on held-out math and non-math benchmarks, and top ARC agents with other foundation models; they do not transfer Meta Agent Search itself and show that it improves a new domain. This distinction prevents task-agent transfer from being counted as compounding improvement. [quick-win]
3. **People remain responsible for consequential outer-loop choices.** Human work supplies the framework, prompts, notion of interestingness, domain descriptions, datasets, objectives, baselines, budgets, and manual safety inspection. The meta-agent searches within those choices rather than revising them. [quick-win]
4. **The cross-domain evidence is positive but bounded.** Math-searched agents beat or match hand-designed baselines on reading comprehension, multi-task, and science evaluations, yet generally trail agents searched directly for the target domain. This supports partial reuse of agent design patterns, not domain-independent optimality. [just-a-reference]
5. **The initialization ablation identifies a narrow human-input effect.** Removing hand-designed seeds still produces agents above the selected baselines, while seeded search usually performs better and math is the exception. This varies initial archive contents without removing human-designed prompts, framework, benchmarks, or evaluation. [just-a-reference]

## Limitations (our opinion)

The benchmarks are mostly single-step question answering, so they do not establish performance in long-running agents, tool-rich environments, or real deployment. Search uses small validation subsets, a single performance objective, fixed model versions, and at most 25 or 30 iterations; repeated adaptive evaluation can favor the validation regime even when final tests are held out. The baselines cover prominent hand-designed patterns but do not establish superiority over every competing automated search method. Cross-domain transfer is tested from one math search domain to a limited set of benchmark domains, and cross-model transfer is tested on ARC, so the paper does not establish general transfer across tasks and models. The archive's causal role is not ablated, and its entries bundle code with metrics, preventing attribution to particular retained information. The authors' empty-initialization ablation tests baseline seeding only. Manual inspection addresses harmful generated code in the reported setup but is an external intervention, not an automated safety property. No implementation was inspected or experiment reproduced for this ingest, so outcome claims remain paper-reported.

## Recommended Next Action

Update [Factory construction does not establish knowledge acquisition](../notes/factory-construction-does-not-establish-knowledge-acquisition.md) with Meta Agent Search as a compact case distinguishing archive-conditioned program construction, transferred task-agent artifacts, and the human-fixed outer search loop.
