---
description: Controlled prompt variation either decorrelates checks or measures brittleness under fixed task semantics; Deutsch's variation test instead changes the explanation to test mechanism and reach
type: note
traits: [has-external-sources]
tags: [evaluation, llm-interpretation-errors, learning-theory]
status: seedling
---

# Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing

"Vary something and observe what changes" appears across multiple methodological contexts, but the underlying operations are distinct. This note groups the two main uses of **controlled prompt variation as analysis**:

- **verification** — vary the prompt to create less-correlated checks or judges
- **diagnosis** — vary the prompt while holding task semantics fixed to measure brittleness

Both vary what the model sees. Deutsch's explanatory-reach test does something different: it varies the **explanation itself** — change a premise and ask whether the conclusion changes predictably. That tests whether an idea captures causal structure. Prompt variation tests the behavior of the interpreter under alternative framings.

## Verification: prompt variation as decorrelation machinery

In [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md), "vary the prompt" is a way to manufacture independent signal from a soft oracle. A single model with a single framing shares the same bias across repetitions — naive voting just amplifies it. Rephrasing the question, changing framing, or applying metamorphic transformations breaks some of that correlation and makes aggregation more meaningful.

The primary success criterion here is **not invariance** but less-correlated signal. Disagreement across variants can be useful — the point is to avoid shared failure modes. Some verification methods, especially metamorphic checks, also use invariance as part of the signal ("if the answer changes under an equivalent transformation, something is wrong"). But the distinctive role of prompt variation in this section is that it creates multiple probes that do not all fail for the same reason.

## Diagnosis: prompt variation as brittleness measurement

In [operational signals that a component is a relaxing candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md), paraphrase and reordering tests are not trying to create independent judges. They ask whether a component is stable under semantically equivalent surface changes. The [PromptSE ingest](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) makes this concrete: emotion and personality prompt variants preserve the task while changing expression style, so performance shifts are interpreted as prompt sensitivity, not as evidence from multiple judges.

The success criterion here **is invariance**. If the task is unchanged, large output swings indicate the system is tracking surface cues instead of underlying structure — a diagnostic signal that a component is overfit to prompt format rather than task specification.

## Deutsch's reach test varies the explanation, not the prompt

The [reach note](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) uses "can you vary it?" in a different sense. Deutsch's test asks: Can you change a premise in the explanation? Can you predict what changes in the conclusion? Does that reveal causal structure that transfers beyond the original case?

This is a quality test for **ideas**, not for model behavior. The desired result is **structured sensitivity**: if the explanation captures mechanism, changing one premise should change downstream predictions in an intelligible way. Neither stability under paraphrase nor decorrelated disagreement is the goal.

The three operations separate cleanly:

| Operation | What is varied | What is held fixed | What counts as success |
|---|---|---|---|
| Verification via prompt variation | framing of the check | the candidate answer and evaluation target | less-correlated signal |
| Diagnosis via prompt variation | surface form of the task | task semantics | stable behavior under equivalent variants |
| Reach testing | premises in the explanation | the standards of criticism | predictable downstream changes |

All three use controlled variation to learn something invisible from a single run, but the interpretation logic differs. Treating them as one method obscures what each result means.

## Prompt ablation is adjacent but distinct

[Prompt ablation converts human insight into deployable agent framing](./prompt-ablation-converts-human-insight-to-deployable-framing.md) is a fourth nearby use: vary prompt framing against a known target to find which framing reliably elicits the desired reasoning. This is closest to **optimization/search**. It uses a hard target like verification, but the goal is not decorrelation. It measures behavioral robustness like diagnosis, but only relative to one human-verified finding. Prompt ablation selects a framing — it is not testing reach or classifying brittleness.

## Why the distinction matters

Without this separation, the results of prompt variation are easy to misread:

- A diagnostic test could be mistaken for evidence aggregation, when disagreement actually signals brittleness.
- A verification setup could be misjudged as instability, when disagreement is exactly what creates independent signal.
- A reach test could be reduced to paraphrase robustness, when the point is to vary the mechanism and predict the consequences.

The common meta-pattern is **controlled variation as an epistemic tool**. The object of variation determines the epistemic role:

- vary the **prompt** → learn about model robustness or judge correlation
- vary the **explanation** → learn whether the idea has mechanistic reach

---

Relevant Notes:

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — foundation: prompt variation as a way to decorrelate weak oracles for verification
- [operational-signals-that-a-component-is-a-relaxing-candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — foundation: prompt variation as a diagnostic for paraphrase brittleness and theory-like components
- [Prompt Stability in Code LLMs](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — evidence: controlled emotion/personality variants operationalize diagnostic prompt variation at scale
- [first-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — contrasts: Deutsch's "vary" test changes the explanation to test mechanism and reach, not the prompt to test model behavior
- [prompt ablation converts human insight into deployable agent framing](./prompt-ablation-converts-human-insight-to-deployable-framing.md) — adjacent method: controlled prompt variation used for framing selection rather than diagnosis or decorrelation
