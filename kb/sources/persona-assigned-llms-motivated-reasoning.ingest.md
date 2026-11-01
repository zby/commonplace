---
description: "8 LLMs given demographic or political personas: veracity discernment drops up to 9% and gun-control evidence is judged identity-congruently; CoT and accuracy prompts do not fix it"
source: https://arxiv.org/abs/2506.20020
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 3ffbf8dd58e68eaf1ad0185537c67fd4c4757325e9dd2bc8564b25c2e9611225
ingested: "2026-11-01"
occasion: "the epistemic-relevance-and-conceptual-blending workshop (kb/work/epistemic-relevance-and-conceptual-blending/) screened this paper as evidence-register entry E18 from an operator-supplied external review; the workshop needs the paper's own account of how an assigned persona changes the accuracy of evidence evaluation, what the tasks measured, and what debiasing was tried."
type: types/ingest-report.md
domains: [persona-prompting, motivated-reasoning, evidence-evaluation, prompt-debiasing]
tags: [llm-reliability]
---

# Ingest: Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning

## Classification

This is an empirical "machine psychology" study. It ports two human-subject
paradigms to LLMs, compares persona-prompted runs with a no-persona baseline,
and fits mixed-effects regressions. The capture is arXiv v2, dated
2026-04-16, and includes the appendix. Authors: Saloni Dash, Amélie Reymond,
Emma S. Spiro and Aylin Caliskan (University of Washington). Spiro works on
online information and misinformation. Caliskan is known for measuring social
bias in language models. The persona-prompting method follows Gupta et al.
(2023), "Bias runs deep".

## Summary

The study puts a persona in the system prompt, for example "Adopt the identity
of {persona}. Answer the questions while staying in strict accordance with the
nature of this identity", using three wordings. The 8 personas cover 4
attributes: Democrat/Republican, man/woman, atheist/religious, and
college/high-school educated. The 8 models are GPT-3.5, GPT-4, GPT-4o,
GPT-4o-mini, Llama2-7b, Llama3.1-8b, Mistral and WizardLM-2. Each was run at
temperature 0.7, 100 samples per persona wording. Task 1 is headline veracity
discernment on the 20-item MIST set (10 real, 10 synthetic fake). The model
rates accuracy on a 1–6 scale. Each rating is standardized to 0–1 and averaged
into veracity discernment ability (VDA). Mean VDA falls from 0.737 at baseline
to 0.673 for the High School persona (about 9% lower). The average fall is
about 3%. The Democrat persona instead rises to 0.773. The falls come mostly
from OpenAI models; Llama2 and WizardLM-2 improve under personas. Persona runs
also answer actively-open-minded-thinking (AOT) items and new cognitive
reflection test (CRT) items. In a mixed-effects model, AOT (taken as an
inverse proxy for myside bias) is a small significant predictor of VDA, and
CRT is not. The authors read this as motivated rather than analytical
reasoning, as in Roozenbeek et al. (2022). Task 2 replicates Kahan et al.'s
(2017) covariance-detection items with Democrat and Republican personas. A 2×2
contingency table is valid only when proportions are compared. It is framed
either as a skin-cream trial (the control) or as a concealed-handgun ban, and
the ground truth is either increase or decrease. The bias β is P(correct |
Republican) − P(correct | Democrat) for each ground truth. When banning guns
truly decreased crime, Democrat personas were far more often correct in
Llama2, Mistral, WizardLM-2 and GPT-3.5. The largest gap was GPT-3.5, 0.96
against 0.06, the paper's "up to 90%". When the ban truly increased crime,
Republican personas did better in Llama2 and Llama3.1, by up to 30%. Skin-cream
β stayed near zero. In 46% of open-source answers the persona states its
identity outright ("As a Republican, I must emphasize..."). Two prompt
debiasing methods were tried. "Think step by step" changed VDA by a
non-significant −0.39%. Adding "who has skeptical attitude and strives for
accuracy" to the persona lowered VDA by a significant 2.93%. On the evidence
task, neither "systematically" reduced β. They cut explicit identity
references to 8% (CoT) and 0% (accuracy), and the authors say the bias
persisted anyway. The authors say the "motivation" mechanism may be unlike the
human one and suspect training data or feedback tuning.

## Contribution assessment (our opinion)

The problem matters. Persona prompting is a cheap and widely used way to
personalize models, and an identity-congruent failure on evidence evaluation
would spread through any persona-conditioned assistant. The paper's main
contribution is to frame persona effects as identity-congruent reasoning and
to test that framing with validated human paradigms that come with controls.
The skin-cream control on the Kahan task is the strongest part of the design.
It makes the political-persona gap hard to explain as a general loss of
numeracy. The direction of the gap (Democrat personas more often right when a
gun ban works, Republican when it backfires) is a consequence the conjecture
predicts and a rival "personas just add noise" account does not. Support is
much weaker for the claim that this is *motivated* reasoning, as opposed to
role compliance. The instruction asks the model to answer "in strict
accordance" with the identity, and 46% of answers recite the identity's policy
view. Nothing separates the model inferring what a Republican would answer
from a reasoning process bent by identity. The AOT-predicts-VDA regression is
also a thin basis for the motivated-reasoning reading. AOT here is the model's
own questionnaire answer under the same persona, the coefficient is small, and
CONF is a larger predictor. The debiasing result is a credible negative for
two lightweight prompts and nothing more. The first-of-its-kind framing claim
is plausible from background knowledge, but this assessment cannot check
priority.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the workshop's question, this source is the anchor case for an
instruction about the *reasoner*, not about the item, changing the accuracy of
evidence evaluation. It also gives a second independent negative result for
prompt-level debiasing. In the KB it serves as evidence for several existing
notes, mostly as a bounding case.

It is evidence for [Context contamination operates below an agent's
compliance reasoning](../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md).
That note leaves open whether an explicit neutrality reminder can neutralize a
stance that is already in context. Here an accuracy-and-skepticism clause added
alongside a present persona removed the visible identity talk but did not
reduce identity-congruent errors, and it lowered veracity discernment. This
matches the note's distinction between suppressing a visible signal and
removing its influence. The caveat must travel with it: the persona was a
sanctioned standing instruction, not a contaminant the model was told to
ignore. The neutrality clause therefore competes with an instruction rather
than overriding stray content.

It is evidence for [Error correction works with above-chance oracles and
decorrelated checks](../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md).
That note names content bias as a measured source of correlated error. A
persona is a second source of the same kind. Repeated samples under one persona
lean the same way, so voting within a persona would amplify the lean.
"Think step by step" did not remove it. This qualifies the note's suggestion,
which rests on Lampinen, that process structure partly decorrelates
content-driven error. The suggestion is so far shown only for item-content
effects.

It is evidence for [Human writing structures transfer to LLMs because failure
modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md),
in two directions. It adds a shared failure mode, identity-congruent
evaluation of evidence, with the mechanism unknown. It also bounds the note's
claim that structured prompting "pushes toward content-independent reasoning".
Step-by-step prompting gave no significant mitigation against this bias
source. In the same way, it is a worked positive case for the per-principle
test in [Psychology-to-agent transfer needs per-principle failure-mode
testing](../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md).
The paper asks "does the agent exhibit this failure?" and answers yes at the
level of behavior. It does not answer at the level of mechanism.

It is evidence for [Systematic prompt variation serves verification and
diagnosis, not explanatory-reach testing](../theory/systematic-prompt-variation-serves-verification-and-diagnosis-not.md).
Identity personas are not semantics-preserving variants on politically loaded
evidence. They shift answers in a predictable direction there and leave the
neutral control roughly unchanged. For verification, persona variants
therefore give biased decorrelation, and the bias depends on the content. For
diagnosis, they cannot stand in for a surface-only paraphrase.

It compares with [Generalization Bias in LLM Summarization of Scientific
Research](./peters-chin-yee-llm-generalization-bias.ingest.md) on the axis of
prompt-level mitigation of a systematic bias. In both studies an accuracy
instruction made the measured bias worse, and "step by step" had no
significant effect. The two wordings differ (a negative "do not introduce
inaccuracies" there, a persona attribute "strives for accuracy" here), and so
do the bias sources. So this is a replicated pattern across two designs, not
one controlled effect.

It compares with [Language models don't always say what they
think](./language-models-dont-always-say-what-they-think.ingest.md) on whether
a biasing input is verbalized. Turpin et al.'s models almost never mention the
biasing feature. Here half the open-source answers state the identity, and the
mitigations remove the statement without removing the bias. The two together
show that the biasing input being named in the output is neither necessary nor
sufficient for the bias.

It compares with [Language Models, Like Humans, Show Content Effects on
Reasoning Tasks](./language-models-like-humans-show-content-effects-on-reasoning.ingest.md)
on human-like bias in human-subject reasoning tasks and on whether CoT helps.
Lampinen et al. find belief-congruent content effects that CoT partly reduces.
This source finds persona-induced effects that CoT does not reduce. The bias
sources differ, item content against an instruction about the reasoner, so
the two results are not in direct conflict.

It compares with [Many AI analysts, one
dataset](./many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md)
on prompt-assigned personas steering conclusions drawn from fixed evidence.
That study uses framing personas in long autonomous analyses. This one uses
socio-demographic identities on short items.

## Extractable Value

1. **How a persona changes the accuracy of evidence evaluation, in the paper's own account** -- the effect has two forms that should not be merged. On veracity discernment it is a small, model-dependent level shift. The average fall is about 3%, the High School persona falls about 9%, the Democrat persona rises 4%, and two open models improve. On covariance-detection evidence the effect is *conditional on congruence*: political personas are more often right when the true answer matches the identity's policy stance, and the neutral skin-cream control is unaffected. For the workshop, the second form is the one that bears on relevance. A feature of the reasoner that is irrelevant to the evidence changes which valid inference is drawn, and only on topics where the feature has a stance. The result is bound to an instruction that requests identity fidelity, so it may be role compliance rather than a distorted inference process. [quick-win]
2. **What the tasks measured** -- VDA is mean standardized accuracy rating over 20 MIST headlines. It measures discernment of real from fake as a whole, not identity-congruent rating of individual headlines, which the paper never analyzes. β is a difference in correct-answer rates between Republican and Democrat personas on one contingency table per ground truth. The tables use the same four numbers with labels swapped, and correctness needs a ratio comparison (223/75 against 107/21). The "motivated versus analytical" contrast comes from the model's own AOT and CRT questionnaire answers under the persona, entered as predictors of VDA. So the measured quantities are task accuracy and a between-persona accuracy gap, not a direct measure of motivation. [quick-win]
3. **What debiasing was tried, and its result** -- two prompt additions were tried: "Think step by step" appended to the task, and "who has skeptical attitude and strives for accuracy" inserted into the persona description. CoT gave a non-significant −0.39% VDA. The accuracy clause gave a significant −2.93%. Neither systematically reduced β on the evidence task, and those figures are not in the text capture. Both removed explicit identity references (46% to 8% and 0%) without removing the effect. Self-consistency, tree-of-thought, removing the persona, and fine-tuning were not tested. [quick-win]
4. **Verbalization is not a reliable indicator of persona bias** -- suppressing the identity statement leaves the identity-congruent answer. A reviewer or checker that looks for explicit stance markers in a trace would pass these outputs after mitigation. This strengthens the context-contamination note's distinction between suppressing a signal and removing its influence. [experiment]
5. **Accuracy exhortation as a non-control, second instance** -- with Peters and Chin-Yee, this is a second study where an accuracy-emphasis prompt worsened a measured bias and step-by-step prompting did nothing. It is a candidate log observation toward "exhortation is not a debiasing control". The mechanism is unexplained in both, so under the quality bar it is not yet a note. [just-a-reference]
6. **Persona prompts are a correlated-error source for multi-sample or multi-agent checks** -- persona-differentiated reviewers or voters do not supply independent errors on stance-bearing content, and one persona's samples share its lean. This is a concrete caution for the error-correction note's decorrelation levers. The reach is limited because only demographic and political identities were tested, not expertise or role personas. [experiment]

## Limitations (our opinion)

The central confound is instruction compliance. The persona prompts explicitly
ask for answers "in strict accordance with the nature of this identity". An
identity-congruent answer on gun-control evidence may therefore be the model
correctly inferring what the persona would say, not reasoning that the persona
distorts. The paper has no condition that separates the two, such as a persona
told to report its own beliefs and then judge the data neutrally, or a third
party asked what the persona would conclude. The authors' own caveat that the
mechanism may differ from the human one leaves "motivated reasoning" as a
behavioral analogy, not an established mechanism.

The motivated-versus-analytical regression is weak support. AOT and CRT are
the model's own answers to questionnaire items under the persona. Personas
move both scores (CRT rises for every persona). So the regression relates
three outputs that the same prompt shapes jointly. The AOT coefficient is
0.0021 VDA per standard deviation. That is significant, but it is small beside
CONF and the open-source indicator. The human finding being replicated is
about AOT as a trait of a person, and a model endorsing AOT statements may not
measure the same construct.

The evidence task is narrow. There is one numeric table per ground truth, and
300 samples per persona are repeated draws on the same item, so item-level
generalization is untested. Effects are concentrated in a few small open
models and GPT-3.5. Several OpenAI models score near 0% on the gun items and
are dropped from the figure. Strong base-rate preferences (Llama2 toward
"crime decrease", Llama3.1 toward "increase") interact with β. No significance
tests for β appear in the text. Figures 2–4 and 18–22 are images that are not
in the text capture, so the per-model β values, the mitigation results on the
evidence task, and the non-political-persona results cannot be checked from
the snapshot. The extracted VDA formula is also garbled, so the exact
standardization for real headlines cannot be confirmed from the capture.

The model set is 2023–2024 vintage: 7–8B open models and pre-reasoning OpenAI
models. The authors note that reasoning-trained models were not tested. On the
veracity task, VDA's overall drop does not show identity-congruence. The MIST
items include politically valenced fakes, but no per-headline congruence
analysis is reported, and the Democrat persona's improvement is left
unexplained. Mitigation covers two short prompts, one wording each.

## Recommended Next Action

In the epistemic-relevance-and-conceptual-blending workshop, update
evidence-register entry E18 to cite this ingest. Record three things: the
congruence-conditional accuracy effect on the gun-control evidence task, with
the skin-cream control, as the paper's account; the measured quantities (VDA
over MIST, the between-persona β on single contingency tables); and the null
or negative CoT and accuracy-prompt results. Mark the instruction-compliance
confound as the reason not to treat E18 as evidence of a distorted inference
mechanism.
