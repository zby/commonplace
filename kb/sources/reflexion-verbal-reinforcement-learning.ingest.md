---
description: "Reflexion improves retries with bounded verbal memory; self-test errors and uneven diagnosis fidelity limit its evidence for learning through retained explanations."
source: https://arxiv.org/abs/2303.11366
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 13e7359dff27f467a4bf4e83ae55afa30701180471095118b50ee7a6d57cf4b7
type: kb/sources/types/ingest-report.md
domains: [agent-memory, learning-theory, evaluation]
learning_claims: true
---

# Ingest: Reflexion: Language Agents with Verbal Reinforcement Learning

## Classification

An experimental research paper proposing a language-agent feedback loop and evaluating it on sequential decisions, question answering, and programming. The captured observation is arXiv v4, dated 10 October 2023. Authors Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao report their own system's experiments, with affiliations at Northeastern, MIT, and Princeton. The paper provides methods, ablations, and selected trajectories; its authorship is methodological access, not independent replication.

## Summary

Reflexion keeps model weights fixed and improves later attempts on a task by supplying generated verbal reflections alongside task context. An actor produces actions or code, an evaluator supplies feedback, and a reflection model turns the trajectory and feedback into advice retained in a recent buffer of one to three experiences. Within this fixed division of responsibilities, the paper reports cumulative success on 130 of 134 ALFWorld tasks over twelve trials and HumanEval Python accuracy of 91% versus 80.1% for the GPT-4 baseline. The coding result evaluates one final submission after internal tests and revisions; it is not one model call. A HotPotQA ablation finds an approximately eight-percentage-point gain from adding reflection to prior-trajectory memory, without isolating diagnosis accuracy from the additional generation step. MBPP Python instead falls from 80.1% to 77.1%, accompanied by more incorrect solutions accepted by generated tests. The useful contribution is evidence that retained linguistic feedback can improve bounded retries, with explicit failures that constrain stronger claims about reliable self-diagnosis or durable transfer across tasks.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies a concrete case for [warranted autonomy being bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): a programming agent stops revising when its own tests accept a solution, even when hidden evaluation later rejects it. The reported probability of an incorrect solution conditional on passing internal tests is 16.3% on MBPP Python versus 1.4% on HumanEval Python. This supports an acceptance-boundary warning for this particular test-generation and stopping procedure, rather than a verdict on self-generated tests generally.

It also sharpens the distinction in [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). In the HotPotQA setting with supplied supporting context, reflection plus prior trajectory outperforms prior trajectory alone. That tests an additional interpretation step within the supplied actor, feedback, and memory arrangement; it does not compare alternative memory architectures or establish that the interpretation accurately explains failure. The appendix makes [the need to connect causal witnesses](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md) concrete: in the ALFWorld example, the retained advice recommends changing the order of finding a lamp and mug, but the successful attempt retains the original goal order while using remembered location information. The episode supports useful retained context more directly than the particular causal explanation the caption offers.

## Learning Claims (our opinion)

The source calls its mechanism verbal reinforcement learning: feedback changes the text on which an otherwise fixed model conditions its next attempt. The learner receives trajectories and evaluator signals; in coding it also receives generated-test results and compiler or interpreter feedback. It can revise an answer, a program, a search query, or an action sequence. Reflections summarize failures and propose changes, with only the most recent one to three retained. The source's long-term memory therefore means persistence across these trials, not demonstrated accumulation across an open-ended working life.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), Reflexion as evaluated is outside, and condition 4 (retention) decides it. Reflections are stated explanations of failure with proposed plans (condition 1). Condition 2 (consumption) is unestablished: the ablations show that adding a reflection step can help, not that a reflection's content caused the next decision, and the ALFWorld example succeeds without following its advice. Condition 3 (criticism) is unestablished: later feedback tests answers and programs, not what a retained reflection says, and newly generated advice can replace old advice without confronting its claims. Condition 4 fails: the one-to-three-reflection buffer is carried across retries of the same task, and retries on one task are one pass of error elimination on one problem, however many trials run. Learning is a separate claim. The ablations give evidence that including reflection improves task-solving in some configurations; imperfect diagnoses do not rule that out, since remembered locations or altered search may still help.

The experiments also illustrate [improvement within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). The retry loop can change candidate behavior and textual advice, but does not learn a replacement for the actor/evaluator/reflection division, the available environment interface, or the recent-buffer retention policy. Coding tests can be generated and questioned, yet the experimental procedure still treats passing that internally generated suite as its stopping condition. Gains establish usefulness within these choices, not their superiority to other choices. Nothing here requires revising the theory-builder definition; the source chiefly supplies bounded positive results and examples where improvement through an explanation remains unestablished despite a successful retry.

## Extractable Value

1. **False acceptance can terminate an otherwise useful improvement loop.** Section 4.3 distinguishes failing tests on correct code from passing tests on incorrect code. The latter can end the run before correction; the former can still prompt the agent to question a test. Add this asymmetric stopping consequence to the KB's existing oracle-domain account, retaining the task-specific conditional error rates and the distinction between parseable tests and adequate tests. [quick-win]
2. **Separate the effect of adding reflection from the truth of its diagnosis.** The HotPotQA prior-trajectory ablation reports an approximately eight-point gain from reflection in the ground-truth-context setting. In the hardest-50 HumanEval Rust ablation, the baseline and tests-without-reflection score 60%, reflection-without-tests scores 52%, and the full treatment scores 68%. These comparisons support the tested combinations within fixed interfaces; removing tests also removes early stopping, and neither comparison isolates explanation fidelity or equal-cost superiority. They are useful design evidence for a controlled reflection experiment, not a general requirement to create a separate critic. [experiment]
3. **Selected successful trajectories can expose unsupported causal interpretations.** Appendix B's lamp-and-mug example succeeds without the recommended reversal of goal order. Appendix D.1 recommends searching Gorden Kaye, already tried unsuccessfully, whereas the successful retry searches Sam Kelly. These cases can strengthen the existing warning about disconnected witnesses by separating retained context, diagnosis, actual behavior, and final outcome. [quick-win]

## Limitations (our opinion)

The evaluations mainly retry the same task. ALFWorld reports cumulative solved environments, HotPotQA uses 100 questions and binary exact-match feedback between attempts, and coding submits a final candidate after internal work. These protocols do not establish cross-task transfer, indefinite memory growth, or equal-inference-budget superiority. HotPotQA's supplied-context and Wikipedia-search settings also expose different information; their scores should not be pooled as a single reasoning result.

The paper's positive results are uneven. MBPP Python deteriorates; StarChat-beta remains at 26% on HumanEval Python; and a 100-request WebShop run is stopped after four trials without improvement. The latter bounds the tested configuration but does not establish the authors' broad claim that Reflexion cannot handle tasks requiring substantial diversity and exploration. Likewise, the different test false-acceptance rates offer a plausible explanation for MBPP's weakness without isolating the cause of every benchmark difference.

The reflection stage adds computation and changes the supplied context. Better retry results can therefore reflect additional inference, remembered task facts, or altered search as well as sound diagnosis. The Rust test-removal ablation changes both information and stopping behavior, so its lower score cannot be attributed solely to lack of evaluation information. Alternative retention schemes and actor/evaluator boundaries are not compared under matched conditions.

No implementation was inspected or executed for this ingest; all outcome evidence remains the paper's reports. Algorithm 1 uses a disjunction in its loop condition that conflicts with the prose account of stopping on success or at the trial limit. Appendix ablation templates also retain fields that their labels say are omitted. These inconsistencies leave exact runtime behavior unresolved and preclude treating the printed pseudocode or templates as a verified implementation specification.

## Recommended Next Action

Update [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) with the Section 4.3 case of incorrect code passing generated tests and ending retries, preserving the HumanEval/MBPP scope and distinguishing syntactic test validity from evidence of functional correctness.
