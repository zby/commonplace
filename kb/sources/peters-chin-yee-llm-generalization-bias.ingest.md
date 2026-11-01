---
description: "10 LLMs, 4,900 science summaries: models turn quantified, past-tense, descriptive results into generic, present-tense or action-guiding claims; accuracy prompts worsen it"
source: https://arxiv.org/abs/2504.00025
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: afe619f6e76a46df88f0186b7d2a52d53c5ec369f2356154c0bc669cfee44f60
ingested: "2026-11-01"
occasion: "the epistemic-relevance-and-conceptual-blending workshop (kb/work/epistemic-relevance-and-conceptual-blending/) screened this paper as evidence-register entry E16 from an operator-supplied external review; the workshop needs the paper's own account of how model summaries change what a source licenses a reader to conclude, and how the overgeneralization was coded and measured. Ingest it as a tracked source; do not edit the workshop."
type: types/ingest-report.md
domains: [generalization-bias, scientific-summarization, scope-qualifiers, summary-faithfulness]
tags: [llm-reliability]
---

# Ingest: Generalization Bias in LLM Summarization of Scientific Research

## Classification

This is a preregistered empirical study with human coding and mixed-effects
regression. It is a penultimate draft, dated 2025-03-28 and forthcoming in
Royal Society Open Science. The study varies models, prompts, temperature and
retests, and adds a human-written comparison set. Authors: Uwe Peters
(philosophy, Utrecht) and Benjamin Chin-Yee (pathology and medicine, Western
University; history and philosophy of science, Cambridge). Both have
published on generics and hasty generalization in medical research; the
coding scheme comes from that earlier work, which the paper cites.

## Summary

The study asked 10 LLMs, from GPT-3.5 Turbo to Claude 3.7 Sonnet and
DeepSeek, to summarize 200 abstracts from top science and medical journals
and 100 full-length clinical articles. It produced 4,900 summaries. Coders
labelled each original and each summary as containing a *restricted*
conclusion or a *generalized* one. Three moves count as generalizing. A
quantified claim becomes a generic one ("parental warmth is protective"). A
past-tense result about the sample becomes present tense. A descriptive
result becomes an action-guiding recommendation. Each move widens what a
reader is licensed to conclude: the population covered, the time covered, or
the step from finding to action. The norm is fidelity to the original text,
not whether the broader claim is warranted. Pooled LLM summaries were about
twice as likely as the originals to contain generalized conclusions. The
odds were about 9 times higher for ChatGPT-4o and 39 times for LLaMA 3.3
70B. Claude models and GPT-3.5 Turbo did not differ significantly from the
originals. Newer models were mostly worse than older ones. The most common
move was from a quantified claim to a generic. A prompt saying "do not
introduce any inaccuracies" roughly doubled the odds against a plain prompt
(OR 1.90); a "step by step" prompt had no significant effect. Temperature 0
cut the odds by 76% against temperature 0.7. On the full articles, NEJM
Journal Watch summaries written by experts did not differ from the articles.
Three LLMs taken together (GPT-4 Turbo, ChatGPT-4o and DeepSeek) were about
4.85 times as likely as those expert summaries to generalize. The authors
offer explanations — RLHF rewarding confident, broadly applicable answers,
an "ironic rebound" from the negative instruction, and bias inherited from
training text — but do not test any of them.

## Contribution assessment (our opinion)

The problem matters: lay readers and clinicians now read science through
LLM summaries, and scope errors are the kind a fluent reader cannot see. The
paper's main contribution is that it makes "faithful summary" measurable on
one specific axis, claim scope, not on factual content. It does so with an
explicit three-part coding scheme taken from linguistics (genericity, tense)
and from the philosophy of rules (descriptive versus action-guiding). That
operationalization, applied to many models with reported inter-rater
agreement, is probably the durable part. The direction of the effect (broader,
not narrower) and the quantified-to-generic pattern are well supported. The
model rankings, the "newer is worse" trend and the accuracy-prompt backfire
are weaker. Model generation is confounded with access mode (API or chat UI)
and collection date. The prompt result rests on one wording per prompt
class. The mechanistic explanations are conjectures the design cannot test.
Priority cannot be judged from background knowledge alone. The authors'
first-of-its-kind claim is plausible for LLM summaries specifically, since
earlier work on human science writing used similar codings.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the workshop's question, the source is the anchor case for scope
broadening under compression. It names the operators a summary can change —
quantifier, tense and modality — and reports how often models change them.
In the KB it serves as external evidence for several existing notes.

It is evidence for [Abstract an experience into a lesson only when you can
state where the lesson stops](../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md).
That note's mechanism is that over-generalization drops the condition
clause. The paper measures exactly that drop when an LLM compresses
scientific claims. It qualifies the note more than it corroborates it,
because the setting is summarization of another author's text, not lesson
formation from one's own episodes.

It is evidence for [A citation cannot assert more fidelity than its capture
preserved](../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).
That note treats a paraphrase-layer passage as unverifiable. The paper adds
that LLM paraphrase of scoped claims is also *biased*, in a predictable
direction toward broader scope. This argues for verbatim retention of
scope-bearing qualifiers. In the same way, it is evidence for [An insufficient
summary precedes the source rather than replacing
it](../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md).
For a question about population, time or recommendation strength, an LLM
summary often fails the note's sufficiency condition, so the source must stay
in the reading path.

It is evidence for [LLM output deviation requires three-way
diagnosis](../theory/llm-output-deviation-requires-three-way-diagnosis.md),
qualified by the decomposition the study holds fixed. In one study, two
remedies from different classes act on the same deviation. A
prompt-narrowing remedy (the accuracy instruction) made it worse; a
sampling-control remedy (temperature 0) reduced it without removing it.
This matches the note's claim that a remedy's class does not settle whether
it reaches the defective relation, and its remark that lower temperature
"can suppress a bad tail". The study cannot tell suppression from masking.
The temperature-0 condition covered only some API-accessed older models.

It also bears on [Out-of-spec output is a failure of the interpreter, not
the spec](../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md),
but the classification is unsettled. The paper treats any change of scope
under "summarize this" as an error. Whether a generic restatement falls
outside the public meaning of "summarize" (interpreter failure), or is a
valid but unwanted reading (underspecification), needs arguing. The case is
clearest under the explicit accuracy instruction. If the interpreter-failure
reading holds, the temperature result is in tension with that note's claim
that sampling control is "irrelevant" to interpreter failure. It is also in
tension with [Execution indeterminism is a property of the sampling
process](../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md),
which says sampling control leaves interpreter failure "untouched".

It compares with [How Language Models Conflate Logical Validity with
Plausibility](./llm-validity-plausibility-conflation-content-effects.ingest.md).
The shared axis is a pressure toward what is plausible or broadly applicable
displacing fidelity to what the input licenses. That paper shows the pressure
mechanistically for syllogism validity. This one shows it behaviourally, on
a real task, for claim scope, with only an untested explanation for the
mechanism.

## Extractable Value

1. **A three-operator account of how a summary changes what a source licenses** -- quantified → generic widens the population, past → present widens the time and sample, and descriptive → action-guiding moves from finding to recommendation. Each is a change in a separate scope-bearing feature, so a checker can compare original and summary feature by feature instead of judging "faithfulness" as a whole. This answers the workshop's first question directly and has reach beyond science summaries: any agent-written compression of a scoped claim, including KB distillation, has the same three features to lose. [quick-win]
2. **How the overgeneralization was coded and measured** -- each text gets one binary label (restricted or generalized) from preregistered criteria. Two expert coders labelled everything; a third coder, blind to source, re-labelled 100 texts (κ 0.79–0.95). GLMMs use a random intercept per original text. "Overall algorithmic overgeneralization" (OAO) is a count difference between summaries and originals, so it nets out narrowing in other items. "Specific" overgeneralization is a per-pair transition the original lacked. Hedged broadened claims ("suggests", "may") still count as generalized. For the workshop, the measured quantity is relative scope change against the original, not warrant. [quick-win]
3. **LLM compression is directionally biased, not just lossy** -- overgeneralizations far outnumbered undergeneralizations in every model. A paraphrase-layer passage made by an LLM should therefore be presumed broader than its source until checked, and scope qualifiers deserve priority in quote retention. This strengthens the citation-fidelity and insufficient-summary notes from "unverified" to "predictably skewed". It needs more than one study before becoming a general claim. [experiment]
4. **A negative accuracy instruction backfired on scope** -- "do not introduce any inaccuracies" roughly doubled the odds of generalized conclusions (OR 1.90, 95% CI [1.11, 3.26]); "step by step" did nothing. It is a data point for the three-way-diagnosis note: narrowing in the prompt can increase the deviation it targets. It rests on one wording per prompt class. [just-a-reference]
5. **Temperature reduced but did not remove the deviation** -- temperature 0 against 0.7 lowered the odds of generalized conclusions by 76%. This is evidence in the tension between the sampling-control notes, which call it irrelevant to interpreter failure, and the three-way-diagnosis note, which allows tail suppression. Resolving it needs a run that holds model and access mode fixed. [deep-dive]
6. **Human expert baseline** -- on the same 100 clinical articles, NEJM Journal Watch summaries did not differ from the articles, while three pooled LLMs were about 4.85 times as likely to generalize. Expert summarization of this kind can preserve scope, so the broadening is not forced by compression itself. The comparison covers one expert-for-expert venue and three models. [just-a-reference]

## Limitations (our opinion)

The normative standard is fidelity to the original, so the study measures
change of scope, not unwarranted inference. When an abstract already
generalizes (54% of the 200 abstracts did), a summary that matches it scores
as faithful, even if the generalization outruns the evidence.

The coding treats the three operators as markers of broader scope. A simpler
rival account fits part of the result: summary-genre conventions. Present
tense and "key takeaway" framing are normal in summaries. On that account,
some coded "generalization" is a register shift that readers may discount,
not an epistemic overreach. The Claude example in Table 3 ("shedding is
common initially…") shows how thin the line can be. The paper offers no
reader study showing that coded summaries change what readers conclude, so
the claim that summaries change what a reader is licensed to conclude rests
on the semantics of the coded features, not on observed misreading.

The comparison between models is not clean. Older models were run through
the API at temperature 0.7 and in early 2024. Newer models were mostly run
through chat UIs with undisclosed settings in March 2025. So generation,
access mode, system prompts and date are confounded, and "newer is worse"
is an association across that mix. The temperature-0 condition appears to
cover only some older API models. Figure 1, which gives the full condition
layout, is an image and is not in the text capture, so the exact layout
cannot be checked from the snapshot.

Several tables in the capture look internally inconsistent. In Table 4, each
"SA overgeneralizations" row equals the "past to present tense" row exactly.
Each "SA undergeneralizations" row equals the "present to past tense" row.
The asterisk labels for action-guiding transitions swap between prompts.
Table 2 contains negative OAO values. Take the per-operator breakdowns as
unreliable until checked against the published version or the OSF data. The
headline ORs from the GLMMs are not affected.

Prompt effects rest on one wording per class. The accuracy prompt is a
negative instruction, so the backfire may be about negation, about the word
"inaccuracies", or about accuracy instructions in general; the design cannot
separate these. The "ironic rebound", RLHF and catastrophic-forgetting
explanations are all untested. The ChatGPT-4.5 "research preview"
confirmation of the RLHF account is one data point.

The human comparison uses one expert venue, and its LLM article prompt was
adapted to require a title. Most analyses use medical texts. The models are
2024–2025 releases, so rankings may not hold for later versions.

## Recommended Next Action

In the epistemic-relevance-and-conceptual-blending workshop, update evidence-register entry E16 to cite this ingest. Record the three-operator account (quantifier, tense, modality) as the paper's answer to how a summary changes what a source licenses. Record the measurement as a binary per-text coding of relative scope against the original, not of warrant, and note the Table 4 inconsistency as a reason not to rely on the per-operator counts.
