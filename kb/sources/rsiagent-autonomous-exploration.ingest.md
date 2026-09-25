---
description: "RSIAgent reports gains from target-conditioned practice and frozen memory, with traceable rule revision and failure audits showing why task acceptance does not validate retained guidance."
source: https://arxiv.org/abs/2609.15364v1
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: cae39a84efcca85119f52141aa8519b7364fcbc6b1e05e0cf700241ce65a509f
type: kb/sources/types/ingest-report.md
domains: [agent-memory, recursive-self-improvement, learning-evaluation, computer-use]
learning_claims: true
---

# Ingest: RSIAgent — Autonomous Exploration for Recursive Self-improvement

## Classification

Scientific preprint by Sibo Zhu, Shicheng Fan, Xinyue Wang, Wenyi Wu, Kun Zhou, and Biwei Huang, affiliated with Aether AI, UC San Diego, and the University of Illinois Chicago. The builders report their architecture, prompts, benchmark results, historical run qualifications, and selected execution audits. This is first-party experimental and process evidence, without independent replication in the retained source. The observation is the complete v1 paper, including appendices.

## Summary

RSIAgent adapts fixed models to software environments by letting a curriculum agent propose practice, an actor execute programs and revise persistent memory, and a separate verifier judge task outcomes. Broad Recursive Self-exploration acquires diverse related experience; Deep Recursive Self-exploration includes attempts on the exact target and further practice; final execution reuses frozen memory. Within the shared actor–verifier harness, reported OSWorld partial score rises from 71.97% to 78.98% and ALE from 83.75% to 84.82%. These are mixed aggregates: 41 of 82 OSWorld entries and 19 of 67 ALE entries use reported RSI results, while the rest retain baseline scores. Historical run selection and differing budgets prevent reading them as uniform matched trials. The paper also reports improvements on 40 game-development tasks. Its strongest contribution for Commonplace is the detailed connection between failed interpretations, revised procedures, later retrieval, and artifact changes, alongside failure audits in which local acceptance lets unsupported assumptions become reusable memory rules.

## Quotes

No source quotes have been retained yet.

## Connections Found

The selected failure audits are evidence for [trace-extracted memory earning authority per operation](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). In the form-completion cases, the verifier accepts unsupported values, and the actor retains rules that substitute missing-data markers or negative answers for unavailable facts. Later attempts reuse those rules. Appendix A makes the authority boundary explicit: the verifier judges the candidate, while the actor distills and reconciles memory; neither the verifier nor the curriculum agent approves memory wording. These cases show how an accepted execution can become overgeneralized guidance, without establishing the frequency of that failure.

The presentation and railway cases compare with [retaining episode evidence for re-examination](../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md): failed interpretations remain available alongside revised procedures, and later actors read relevant records before acting. They also provide a concrete comparison for [connecting witnesses along one theory-mediated path](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md). Appendix E identifies particular revisions, reads, construction choices, and scored artifacts. This is stronger process evidence than memory growth alone, but historical baselines and target rehearsal do not isolate the benefit of retaining episodes, rules, or their combination.

[Machine Studying](machine-studying.ingest.md) supplies a useful contrasting preparation regime. It excludes downstream-task information during corpus study; RSIAgent supplies the exact target query to curriculum generation and practices the target during deep exploration. Freezing memory separates learning from final execution, but it does not make that final target unseen.

## Learning Claims (our opinion)

The source's learning mechanism changes files and subsequent experience selection while keeping model parameters fixed. After a grounded local PASS or FAIL, the same actor context receives the verifier report, distills lessons, and reconciles them with existing memory. Memory has no required schema or file count. During broad exploration, sibling projects start from identical memory; completed experiences are consolidated sequentially into the current canonical bank. During deep exploration, target outcomes and actor-authored diagnoses inform the curriculum's next practice choice. Final evaluation disables curriculum decisions and host memory writeback.

Several reported episodes fit the mechanism of [conjectural learning](../notes/definitions/conjectural-learning.md): a formulated interpretation guides action, criticism bears on its content, and the revised account appears in later action. T049's actor initially treats preservation requirements as forbidding box movement; its failure record identifies that interpretation, a synthetic repair tests a revised procedure, and a later target run consults the retained records. T085's audio practices expose a rendering discrepancy, prompt revision of resampling advice, and precede reuse of that setting. These records support content-directed criticism and recurrent use. The associated historical score gains support improved performance on the practiced targets, but do not isolate how much improvement was caused by the retained explanations rather than extra attempts, concrete solutions, or other retained procedures. Membership is therefore supported at the process level more strongly than causal attribution of the measured gains.

The procedures and episode records expose assumptions and scope conditions that can be revised separately, illustrating [addressable theory](../notes/definitions/addressable-theory.md) without requiring a formal claim schema. Not all memory contents are theories: exact source spans, coordinates, and completed solutions can serve as reusable answers. The T049 evaluation checks the same deck's identity before reusing its construction. That can improve future action on a known artifact without establishing transfer to a new task family. Frozen-memory execution exercises a learned state; it does not itself demonstrate continued criticism or learning.

The [effective update-space boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) is also consequential. The actor can rewrite procedures, scripts, retrieval organization, and explanatory claims; the curriculum can vary practice using outcomes and diagnoses. The role division, program-action interface, checkpoint lifecycle, and distinction between local verification and official grading remain fixed in the reported setup. Neither stage ablation compares those architectural choices with alternatives. The paper supports adaptation within that arrangement, not the necessity of three agents or superiority of an actor-owned memory authority policy. Its failure cases strengthen Commonplace's warning that criticism can itself be mistaken and that preserving a rule does not establish its validity.

## Extractable Value

- **Task acceptance and memory-rule acceptance require different evidence.** [quick-win] Section 4.6 and Appendix A jointly provide a bounded example: unsupported missing-information assumptions pass local verification, become reusable guidance, and affect later attempts, while no separate role approves memory wording. This supports the existing authority note with an observed failure mechanism rather than a proposed checklist.
- **Revision histories can connect learning claims to concrete output changes.** [quick-win] Appendix E follows memory reads into construction choices and scoring consequences. In the selected T049 historical comparison, correcting one arrow endpoint accounts for the 0.40-to-0.80 gain; another slide remains uncredited despite verifier acceptance. The retained path is useful evidence practice, with the historical comparison and target rehearsal kept explicit. It does not isolate an advantage of linked episode-and-rule memory over other representations.
- **Freezing and task disclosure are separate evaluation boundaries.** [just-a-reference] The reference lifecycle records a memory hash, resets the environment, and prevents evaluation writeback. These controls establish a stable retained input for final execution. Because the target was already available and attempted during learning, they cannot establish unseen-task generalization or corpus-only study.
- **Broad-then-deep exploration is a candidate experiment, not a settled curriculum rule.** [experiment] The four-task ablation reports a 74.54% mean for both stages, versus 65.52% for broad-only and 56.50% for deep-only, inside the same actor–verifier design. The cohort was selected for improvements, the baselines are historical, and deep-only practice has a two-project cap. A comparison with comparable budgets and declared stopping rules is needed before importing the sequence as a Commonplace default.

## Limitations (our opinion)

**Reported gains are narrower than the headline.** The main-table RSI rows combine new results with retained baselines. Retries, selected checkpoints, corrected grades, an ALE variant without broad exploration, and ECG results qualified by public-label transfer remain part of the reporting set. Regressions are retained, which matters, but the aggregate is still not a uniformly repeated experiment. Cross-system leaderboard comparisons use different harnesses and budgets. ALE binary accuracy is 50.75%, below the reported GPT-6 value of 52.24%, even though RSI has higher partial credit.

**The stage ablation changes more than a clean ordering choice.** Its four tasks come from an improvement-selected cohort. Full RSI averages two historical evaluations; single-stage conditions use their recorded scores. Deep-only practice is capped, and its checkpoint records do not give the curriculum direct memory access. These differences leave extra compute, practice coverage, stopping policy, and interfaces as alternative explanations for the observed advantage. The experiment does not identify the optimal division between broad and deep practice or validate the fixed actor–verifier–curriculum decomposition.

**Known-target repair is not an estimate of general transfer.** Appendix E uses historical memory-free baselines rather than matched-seed memory ablations. T065 also changes the date information supplied to the final run. T044's score gain depends partly on native project structure: both outputs remove the watermark, but only the memory run uses the accepted native crop settings. T085's score uses acoustic proxies for sentence boundaries. These details help explain the measured changes while limiting claims about general task correctness or causal discovery. Target-specific solutions are a simpler explanation for some gains than broadly reusable causal knowledge.

**Verification independence is limited.** Separate contexts and checkpoint restoration protect information and artifact boundaries. They cannot ensure that a verifier correctly interprets the task or that the actor's abstraction follows from its verdict. The failure percentages describe selected audits, with overlapping cases, rather than prevalence across the benchmark. A preserved uncertainty is also ineffective if later execution ignores it.

**Outcome and cost evidence remains incomplete.** The game experiment uses the same base game and development backbone within each generator group and reports gains under a capped development procedure, but relies on model-based quality judgments and does not isolate the memory mechanism. The desktop reference's ten-hour target watchdog does not bound the complete exploration lineage. More efficient final execution on one target does not establish a net saving after practice costs. This ingest analyzes the paper; it does not inspect the released implementation or reproduce any reported run.

## Recommended Next Action

Update [Trace-extracted memory earns authority per operation, not at capture](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) with the selected missing-information failure cases as bounded evidence that a task verdict does not validate an actor-authored reusable rule, retaining the distinction between observed mechanism and failure prevalence.
