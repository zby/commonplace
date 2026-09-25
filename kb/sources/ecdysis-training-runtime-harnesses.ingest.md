---
description: "Ecdysis separates recurring-failure selection from harness-defect attribution; its ablation shows aggregation alone can increase model accommodation despite improving task scores."
source: https://arxiv.org/abs/2609.11677
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 882a0883d61df2ac3283da03faeb3e9b40a8e9fd9ac98daafe60bee5ab5aaa0f
type: kb/sources/types/ingest-report.md
domains: [agent-harnesses, learning-theory, failure-diagnosis]
learning_claims: true
---

# Ingest: Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents

## Classification

A scientific preprint, marked under review, by Ruiqing Yue, Yu Cui, and colleagues at Chinese research institutions and universities. The retained version is arXiv v2, dated September 20, 2026. It specifies an optimizer, baseline comparisons, a refinement ablation, and an author-conducted modification audit. The results are the developers' evaluation of their own method; the paper supplies no independent replication.

## Summary

[Ecdysis](https://arxiv.org/abs/2609.11677) trains a runtime harness by grouping failures across tasks, refining their interpretation through sequential Analyst, Critic, and Engineer roles, and handing one modification specification to a coding agent. The roles share an accumulated transcript; a Moderator consolidates their findings. Candidates survive only if they improve aggregate training score. With the same Life-Harness starting point, frozen task model, environment, and acceptance protocol, Ecdysis changes failure organization and candidate construction relative to serial per-failure editing. Harnesses evolved using Qwen3-8B are then frozen and reused across five models and three datasets: mean accuracy rises from 58.67% for serial evolution to 69.56% with Ecdysis, an 18.56% relative gain. The more useful methodological result is that aggregation without collaborative refinement improves accuracy but increases the authors' audited share of model-accommodating modifications from 60.00% to 75.61%; adding refinement lowers it to 45.45%. Recurrence can select evidence efficiently without establishing that the harness caused the recurring failure. These results compare treatments inside the supplied optimizer and harness boundary, not alternative definitions of that boundary.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies concrete evidence for [debugging that separates specification gaps, instruction violations, and run-to-run variation](../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md). Its appendix contrasts a global refund restriction that removes a policy-permitted gift-card option with a feedback correction that accurately reports an existing cancellation restriction. These cases show why a failed task and a successful patch do not by themselves identify what was wrong. The authors' model-accommodation versus harness-repair categories are not identical to the note's three relations, but their policy-and-behavior inspection supports its diagnostic discipline. The aggregation-only ablation further limits the inference from frequent failure to harness defect within the tested Life-Harness optimizer.

Ecdysis also provides a comparison for [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): it keeps candidate acceptance fixed while changing how failure evidence is grouped and interpreted. Adding refinement raises mean accuracy from 64.56% to 69.56%, but also adds reasoning calls; it does not isolate richer evidence from additional analysis. Compared with [HarnessEvolve](./harnessevolve-reference-trajectories.ingest.md), which supplies successful reference trajectories, Ecdysis uses recurring failures and role-based criticism as diagnostic inputs. This is a difference in evidence design, with no direct head-to-head evaluation in the paper.

## Learning Claims (our opinion)

The learning mechanism changes harness instructions and executable behavior while holding model weights fixed. Structured failure records retain task identity, termination reason, tool calls, and execution context. Groups spanning at least two distinct tasks receive priority; singleton groups remain auxiliary evidence. Refinement formulates and criticizes proposed repairs before implementation. Fresh executions on the training split decide acceptance, accepted harnesses guide subsequent rounds, and the final harness governs held-out execution. The score chooses what persists; the diagnoses influence what is proposed.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), the optimization system meets conditions 1 and 2: harness instructions and code are stated units whose content governs execution. Condition 3 is met as reported: the Critic role attacks the Analyst's stated repair claims, including their triggers and consequences, before anything is implemented. Condition 4 fails and decides the verdict. One run optimizes one harness for one task domain against its training split, and its rounds are one pass of error elimination. The frozen harness then governs held-out tasks and other models, but that is reuse of a handed-off product; nothing takes the harness or its record of criticism up as the starting point of later work on a different problem. A larger system that fed Ecdysis harnesses and failure records into later optimization could meet the condition; the paper does not test one. As a separate learning claim, the reported held-out aggregate supports improved task capacity for the compound procedure, more strongly than the correctness of each internal explanation. The policy/code witnesses make [addressability](../notes/definitions/theory-builder.md#addressability) concrete: a refund condition or feedback statement can be located and changed separately. They also show that a located edit can impose the wrong scope. Better average performance does not establish that every retained rule is a sound explanation of the failures.

The consequential boundary is the [fixed decomposition outside harness search](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Harness editing does not revise the benchmark score, failure threshold, recurrence priority, supplied role sequence, or strict aggregate-score acceptance rule. The experiments vary aggregation and refinement inside that arrangement. They support learning within it, without establishing that those fixed choices are necessary, optimal, or erroneous. Cross-model evaluation reuses the learned artifact; it is not further learning by the frozen harness. The evidence adds a useful warning to our account: selecting recurring evidence and criticizing its interpretation are separate operations, and improvement in task capacity can coexist with more accommodation of model errors. No revision of the theory-builder definition follows from these results.

## Extractable Value

1. **Frequency selects diagnostic candidates, not proven defects.** Within the shared Life-Harness and acceptance setup, aggregation alone raises accuracy while increasing the author-audited accommodation share. The refund and cancellation cases explain why inspection of policy, observed action, and changed behavior is still needed. This is a concrete empirical companion to the debugging note's warning against choosing a remedy from frequency alone. [quick-win]
2. **Separate the cost of gathering failures from the cost of attributing them.** Round-level aggregation replaces one coding-agent call per failure with one per nonempty round. Collaborative refinement adds analysis before that call. In the reported Airline run, aggregation without refinement is 3.23 times faster than serial evolution; with refinement it is 1.84 times faster. These are actual execution-path results under the supplied optimizer, including stopping and call-completion differences, rather than fixed-budget comparisons of reasoning quality. [experiment]
3. **Audit behavioral decisions against the runtime contract.** The paper counts one substantive modification by its purpose and direct behavioral change, merges related edits across functions, and checks permitted actions before and after the change. Prompt edits can repair feedback; code edits can wrongly prohibit valid actions. This method offers a reusable way to inspect persistent KB or harness rules without equating representation with correctness. The KB application is a proposed transfer. [experiment]
4. **Curate diagnostic coverage as well as sample count.** A five-task set selected for new interaction structures and failure mechanisms achieves 71.67% accuracy, versus 65.00% for five random tasks and 75.00% for the full set, when evolution uses Qwen3-8B and evaluation uses Qwen3-32B. This single reported setting suggests a candidate experiment on repair-example selection; it does not establish a general sample-efficiency law or equivalence to full-data training. [experiment]

## Limitations (our opinion)

The baseline is Life-Harness's serial evolution, not a direct run of every related harness optimizer. All evolved variants start from the same human-augmented harness, use Qwen3-8B during evolution, and allow at most three candidate-generation rounds. Results on the five-model matrix support transfer of those frozen harnesses across tested models and tasks, not repeated successful evolution with every model or transfer to new domains. Three held-out trials measure execution variation; they are not independent replications of the evolution process. The overall averages also hide regressions: for MiniMax-M2.7 on Retail, accuracy falls from 100.00% without refinement to 96.67% with it.

The refinement ablation changes reasoning effort and organization together. All roles use DeepSeek-V4-Pro and read an accumulated sequential transcript; role names do not supply independent evidence. A simpler explanation for some benefit is more careful proposal analysis, rather than the specific role decomposition. Aggregation also changes editing granularity and repeated-call failure exposure. Actual-path training cost and latency therefore do not isolate a single mechanism, and service latency limits portability of the timing claims.

The accommodation audit includes saved candidates later rolled back, so its ratios do not describe only deployed changes. Five authors independently annotate decisions and majority voting assigns labels, but no agreement statistic is reported. The classification rests on their interpretation of policy and execution evidence. Accommodation is explicitly allowed to be useful and reusable; a lower ratio is not itself a measure of generalization or proof that it caused the accuracy gain. The aggregate acceptance test permits individual-task regressions and does not enforce preservation of every policy-permitted action.

The five-task curation result lacks repeated subset-selection trials and gives mixed metrics: its Pass@3 exceeds full-data training, while its all-three-trials success rate is lower. It supports further testing rather than an established replacement for larger training sets. No implementation was inspected or executed for this ingest; the reported code witnesses, costs, and task outcomes remain paper evidence.

## Recommended Next Action

Update [the debugging note](../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md) with the refund-versus-cancellation cases and the aggregation-only ablation, preserving the distinction between author-audited accommodation, demonstrated policy conflict, and improved task score.
