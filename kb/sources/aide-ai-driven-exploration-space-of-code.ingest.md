---
description: "AIDE searches task-code trees with retained plans, scores and debugging feedback; its fixed controller separates within-run improvement from reflective harness revision."
source: https://arxiv.org/abs/2502.13138v1
captured: "2026-09-27"
ingested: "2026-09-27"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 4379b864609c81b2de1b88a0b47d66a088bf6a91a1e51a2139b9306c17072fcb
type: types/ingest-report.md
domains: [self-improving-systems, agent-evaluation, context-engineering]
learning_claims: true
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
---

# Ingest: AIDE: AI-Driven Exploration in the Space of Code

## Classification

An empirical research preprint specifying an agent algorithm and reporting machine-learning engineering benchmarks. Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxiang Wu present work associated with Weco AI; Schmidt lists Runway ML with the work done at Weco. The authors provide their own Kaggle evaluation and summarize independent OpenAI and METR evaluations. That mixture offers engineering detail and outside comparison, while the latter results remain this paper's account of other studies.

## Summary

[AIDE](https://arxiv.org/abs/2502.13138v1) treats machine-learning engineering as search over executable solutions scored by an evaluator. It retains scripts in a tree, selects parents through a fixed drafting/debugging/improvement policy, and supplies summarized prior attempts to an LLM that proposes the next script. Debugging consumes execution errors; improvement requests one change to make its performance effect easier to assess. With this bundled architecture, AIDE with GPT-4 Turbo reportedly exceeds 51.38% of human competitors on average across 16 tabular Kaggle tasks and beats the median in half, outperforming the tested H2O, AutoGPT, and human-with-ChatGPT baselines. The paper also reports MLE-Bench gains and RE-Bench results that vary by task and time budget, with failures on larger codebases and multistep changes. These comparisons support the complete task-solving arrangement; they do not isolate tree search, summarization, or atomic edits, and the controller remains outside the code being optimized.

## Contribution assessment (our opinion)

The work makes a useful engineering contribution to repeated experimentation: explicit candidate storage and standalone evaluation let an LLM reuse partial solutions without extending one conversation indefinitely. The formal decomposition is clear enough to support alternative implementations and stronger component tests. Comparisons across Kaggle engineering and research tasks suggest practical value beyond one dataset, although the evidence is stronger for the compound system than for the authors' causal explanations of its advantages. Likely significance lies in making sustained code search operational and inspectable; the available comparisons do not establish the necessity or originality of each component.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source supplies the original task-code search mechanism needed to interpret the later [AIDE2 paper analysis](./aide2-recursive-self-improvement-research-agents.ingest.md). The useful comparison is the object of revision: here the retained nodes are task solutions and the search controller is fixed; in the later analysis, an outer process searches inner-agent harnesses. This distinction prevents gains under AIDE's bundled controller from becoming evidence that the controller improves itself. The [theory-builder definition](../notes/definitions/theory-builder.md) provides the relevant classification boundary: localized code and retained feedback are present, but a performance ranking alone does not establish criticism of what the code says. Debugging is the more concrete candidate pathway for that criticism.

## Learning Claims (our opinion)

AIDE's adaptation resides in the solution tree and the context assembled from it. The coding model receives a selected script, summarized performance and debugging information, and a static data preview. It can propose new models, preprocessing, optimizers, and other code changes. The paper does not describe updating the coding LLM's weights during search; training models inside generated task solutions is a different operation. Our interpretation is that fixed-model orchestration can improve the solutions available for later steps through retained external state.

Against the theory-builder conditions, the evidence has different strengths:

1. **Localized content:** Section 3 explicitly describes brief solution plans and executable scripts. These supply identifiable candidate content, though the paper does not show that every plan states a testable explanatory conjecture.
2. **Consumption:** The selected script is executed for evaluation and supplied to the coding operator for revision. This is a specified consumption path for code; the influence of particular prose rationales is not separately demonstrated.
3. **Content-directed criticism:** Debugging inspects errors and traces to repair imports, tensor dimensions, and similar defects. This supplies a plausible and specifically described pathway from a failure to an identified part of code. However, the paper supplies no worked trace establishing the full chain from stated diagnosis to revision and retest. For non-buggy improvements, scalar scores and requests for one change do not by themselves show a stated reason bearing on what a candidate says. The criticism condition remains supported by method description more strongly than by inspected episodes.
4. **Iteration:** The algorithm retains scripts and scores and passes summarized history into later proposals. The method also describes passing debugging hints forward. Reuse across rounds is explicit; reuse of substantive criticism is supported to the extent that these hints contain diagnoses, rather than merely failure indicators.

Persistence is established across rounds of a task run, not as a reusable theory library across independent problems. The source therefore provides evidence for some necessary mechanisms of a theory builder without settling membership for the whole optimization process. In particular, code's [addressability](../notes/definitions/addressable-theory.md) makes selective repair possible but does not prove that the system diagnoses the responsible commitment.

Learning remains a separate empirical claim. The task comparisons support improved problem-solving capacity from the complete arrangement; additional independent attempts increasing pass@k also admit the simpler explanation of more sampling. Neither result establishes that later improvement becomes more effective because earlier improvements changed the improver. The fixed controller, evaluator interface, summary scheme, and drafting/debugging/improvement split remain outside the update space in this account. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), successful search shows that these choices suffice in tested settings, not that they are preferable to alternative decompositions. The paper does not demonstrate reflective revision of AIDE's own method or compounding of its improvement process.

## Extractable Value

1. **Separate task-code improvement from improvement of the agent's method.** The original AIDE supplies the fixed-controller case for a Weco/AIDE² comparison: subsequent scores shape which task solution is revised, while the mechanism producing those revisions stays fixed. This supports a more precise account of inner and outer loops without treating the family name as a classification verdict. [quick-win]

2. **Use debugging as the concrete criticism question.** Plans and performance histories establish less than a connected episode in which a named code assumption fails, the diagnosis targets it, and a revision responds. AIDE specifies enough of this pathway to guide trace inspection; it does not furnish that full episode itself. [deep-dive]

3. **Test selective history against a full-history baseline.** AIDE retains candidate scripts while giving the coding operator selected metrics, settings, and error hints. This is a reusable context-management design, but benchmark gains under the bundled controller do not isolate summary quality or prove that the retained categories preserve every useful distinction. [experiment]

## Limitations (our opinion)

The strongest numerical results compare complete systems or model-plus-harness combinations. No component ablation here identifies the separate contribution of the tree, summary operator, or one-change prompt. Likewise, asking for one change improves interpretability only if the generated change is actually isolated and evaluation noise is controlled; the instruction itself does not establish either condition.

The Weco protocol acknowledges that locally constructed holdouts differ from Kaggle's private test sets, complicating percentile comparisons, and that training contamination remains possible. The 16-task subset emphasizes relatively inexpensive tabular problems. Table 2's Above Median flags also appear inconsistent with its reported ranks and percentages, so per-task binary judgments need checking before reuse. The summarized MLE-Bench and RE-Bench results should be checked against their primary studies for precise outcome claims. Reported advantages over humans depend on time limits and task; larger codebases and changes needing several interacting steps expose a stated weakness of the local improvement policy.

The report is grounded in the paper, not an inspected implementation or reproduced experiment. Mechanism descriptions establish the intended loop, while its treatment of diagnoses, selection effects, and retained reasoning in actual runs remains less certain. No cross-problem retention test or experiment changing AIDE's own controller establishes reflective learning or compounding.

## Recommended Next Action

Update `which-existing-self-improving-systems-are-theory-builders.md` with a Weco/AIDE² case that uses this source for the original fixed-controller task-search mechanism and the existing AIDE2 ingest for harness revision, keeping the evidence for content-directed criticism separate from score-based improvement and from better improvement production.
