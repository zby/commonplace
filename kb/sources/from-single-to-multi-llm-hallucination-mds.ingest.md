---
description: "MDS hallucination benchmark: asked for shared insights, LLMs pass off unshared ones; on absent subtopics they rarely abstain; most errors are off-instruction or generic, not fabrication"
source: https://aclanthology.org/2025.findings-naacl.293/
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
doi: "10.18653/v1/2025.findings-naacl.293"
genre: scientific-paper
snapshot_sha256: 711c6938c4cd79316873ad997269366feb07e40b3d30becb69f2dfd6b2c3f435
ingested: "2026-11-01"
occasion: "the epistemic-relevance-and-conceptual-blending workshop (kb/work/epistemic-relevance-and-conceptual-blending/) screened this paper as evidence-register entry E17 from an operator-supplied external review; the workshop needs the paper's own account of what models produce when asked for information shared across documents and that shared information is absent or thin, and how the hallucination categories were defined and counted."
type: types/ingest-report.md
domains: [multi-document-summarization, hallucination-taxonomy, abstention, shared-information]
tags: [llm-reliability]
---

# Ingest: From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization

## Classification

This is an empirical research paper (Findings of NAACL 2025). It builds two
benchmarks from existing data, runs controlled prompting experiments on five
LLMs, adds a human error annotation, and tests post-hoc filters. It reports
no new model or training method.
Author: Catarina G. Belem (UC Irvine, intern at Megagon Labs) with five Megagon
Labs researchers; an industry NLP lab with prior summarization-evaluation
work. Code and data are released at
https://github.com/megagonlabs/Hallucination_MDS.

## Summary

The paper studies topic-focused multi-document summarization (MDS). It regroups
the synthetic SummHay news and conversation corpora into combinations of
N = 2, 3, 4, 5 or 10 documents (about 750 words each), 500 combinations per N
and domain. Each combination has at least two subtopic insights shared across
two or more documents. Five models (GPT-3.5-Turbo, GPT-4o, Gemini 1.5 Flash,
Llama 3.1 70B, Qwen 2 72B) write bullet-point summaries under a "subtopic"
prompt and a "subtopic+trustworthy" prompt that asks only for insights
mentioned in at least two documents. Every prompt says to answer "No insights
found" when nothing relevant exists. A gpt-4o-mini judge checks coverage in
both directions against the reference insights. "Hallucination rate" is
macro-FDR: the share of predicted bullets that match no reference insight. It
therefore counts off-topic, redundant, unshared and uninformative bullets as
well as invented content. Under the optimistic mapping (PARTIAL counts as
correct), average hallucination rates are at least 20% (news) and 52%
(conversation), up to 45% and 75%. From 2 to 10 documents the rate moves only
about ±5% (Gemini Flash rises by under 10%), while recall falls by up to 33%.
The shared-only instruction shortens summaries but raises hallucination
(news +10.47%, conversation +4.20%). On 250 samples paired with a related but
undiscussed subtopic, models abstain 20.65%-71.08% of the time. Abstention
falls as N grows; GPT-3.5 and GPT-4o still summarize up to 79.35% and 44% of
the time. Two authors coded 700+ predicted insights at N = 2 into four
inductively derived, non-exclusive types: pedantic, instruction inconsistency,
context inconsistency and fabrication. Frequencies are tabulated for news
only. Context inconsistency is 9%-37% of errors and fabrication 0%-9%. In the
shared-only setting, instruction inconsistency exceeds 70% of errors, and
58.54%-67.24% of all errors are insights not shared across documents. Simple
post-hoc filters change F1 by about ±3%. The authors suggest, without testing,
summarizing each document before merging.

## Contribution assessment (our opinion)

The problem matters: MDS is a common LLM deployment, and aggregate faithfulness
scores hide what kind of wrong content appears. The main contribution is
measurement, not explanation. The paper turns SummHay's insight annotations
into a controlled document-count and task-focus manipulation. It also gives
an error breakdown showing that most counted "hallucinations" are instruction
violations or uninformative bullets, not invented facts. That is a useful
corrective to reading hallucination rates as fabrication rates. The abstention
probe and the shared-only setting are the most informative results: models
respond to the conditions (shorter outputs) but do not reliably enforce them.
The evidence is narrower than the headline numbers suggest. The documents are
GPT-4o-generated, with no contradictions. The metric counts any unmatched
bullet as hallucinated, and its conversation-domain level shifts by about
30 points with the label mapping. The taxonomy rests on two coding authors, N = 2 and a few
dozen errors per model and setting. The mechanism hypotheses (count mismatch
for flat FDR, recency from instruction proximity or positional encoding,
discourse habits for openers and closers) are offered, not tested. I cannot
judge originality against the wider literature from this capture. The
authors' claim to be first in MDS hallucination analysis is plausible but
unverified. Likely significance: a reusable benchmark protocol and a
well-grounded warning, rather than a settled account of why MDS outputs
deviate.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, the paper is a measured case of condition non-enforcement
under thin shared information. The shared-only setting always contains some
shared material: at least two shared subtopic insights per combination. So it
tests thin shared information, not absent shared information. The only
absence test is the non-existent-subtopic probe, which removes the topic
entirely, not just the overlap. Within those bounds, the dominant output when
asked for cross-document overlap is real, single-document content presented as
shared. Invention is not the dominant output.

In the general KB, the paper is outside evidence for
[out-of-spec output is a failure of the interpreter, not the spec](../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md).
That note's archetypal case is "summarise this document → facts not in the
document". Here the measured deviations mostly violate explicit prompt
conditions (subtopic, conciseness, shared-only) rather than inventing content.
The weak post-hoc filters show how hard repair is at the detection surface.
It bounds
[soft degradation can bind before the hard cap even when required evidence fits](../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md).
The 2-10 document inputs fit easily in the models' windows, yet recall and
abstention fall as documents are added. The error share in output stays nearly
flat, so the degradation appears as lost coverage and lost abstention, not as
rising fabrication. The "pedantic" class (correct bullets that paraphrase the
subtopic, opening remarks, takeaway closers) is a human-coded instance of
[reverse compression](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md).
The authors' untested per-document-then-merge suggestion is weak outside
support for the "separate selection from joint reasoning" advice in
[decomposition heuristics for bounded-context scheduling](../theory/decomposition-heuristics-for-bounded-context-scheduling.md).

Among sources, it compares with
[Peters and Chin-Yee on generalization bias](./peters-chin-yee-llm-generalization-bias.ingest.md)
on scope distortion in summaries. Overgeneralization appears here only as one
sub-case of context inconsistency, a minority error class (9%-37% of news
errors) with no separate count. It compares with
[Paulsen's maximum effective context window](./paulsen-maximum-effective-context-window-mecw.ingest.md)
and [GSM-DC](./gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md)
on how error scales with input volume. Paulsen reports hallucination
approaching 100% beyond the effective window, and GSM-DC reports power-law
error growth with distractor count. This paper's near-flat output error share
measures a different quantity at a much smaller scale; neither should be cited
as the general rule without the contrast. It compares with
[LongMemEval](./longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md)
on abstention when the requested information is absent. Both treat abstention
as a separately failing ability. This paper adds that it decays with document
count.

## Extractable Value

1. **Asked for shared information, models output unshared single-document content as if it were shared** -- in the news "subtopic+trustworthy" annotations at N = 2, instruction-inconsistency errors exceed 70% of hallucinations. Of these, 80%-95.45% are insights not shared across documents, 58.54%-67.24% of all errors. Fabrication is 0%-2.4% in that setting. Summaries get shorter, yet hallucination rises by 10.47% (news) and 4.20% (conversation). Models register the condition but do not verify it. Shared information was thin, not absent: every combination had at least two shared subtopic insights. This answers the occasion's "thin" case directly. The "absent" case for sharedness was not tested. [quick-win]
2. **When the requested topic is absent, many models summarize anyway, and more so with more documents** -- with an explicit "No insights found" instruction, abstention on a related but undiscussed subtopic ranges from 20.65% (GPT-3.5, conversation) to 71.08% (Llama 3.1, news), and it falls as N grows, most sharply in conversation. This is the nearest the paper comes to "absent shared information". It removes the topic, not just the overlap, and the main text does not say which prompt setting the 250 probe samples used. Llama 3.1 is the robust outlier (under 8% drop). The paper does not code what content the non-abstaining summaries contain. [quick-win]
3. **How the categories were defined and counted** -- "hallucination" in every rate is operational: a predicted bullet with no matching reference insight under a two-way gpt-4o-mini coverage judge, with PARTIAL counted as correct. The four types were derived inductively. Two authors described errors in 700+ insights from 150+ summaries at N = 2, roughly uniform across models, focus and domains. They then agreed a taxonomy and recoded. Labels are non-exclusive, so Table 2 percentages per model sum above 100%. Two more authors relabeled 50 examples per category, and 80.71% of insights got the same label from at least three annotators. Frequencies are reported for news only, over 25-60 errors per model and setting. The taxonomy is a small-sample, author-coded instrument, and its percentages are shares of errors, not of output. [quick-win]
4. **Most measured "hallucination" in MDS is condition violation or uninformative output, not invention** -- this bounds the default reading of hallucination rates in the out-of-spec and soft-degradation notes. A headline like "up to 75% hallucinated" mostly measures off-topic, redundant, unshared and generic bullets. The paper's own limitations add that some "false hallucinations" come from merging two reference ideas into one bullet. [quick-win]
5. **Volume degradation splits into separately moving quantities** -- here recall and abstention fall with document count while output error share stays near-flat. Paulsen and GSM-DC measure rising error. A claim that "more context degrades performance" should name which quantity degrades. This is a candidate refinement for the soft-degradation note, and a synthesis that needs more than this source. [deep-dive]
6. **Position effects in output and input** -- bullet accuracy declines with output position, apart from low-accuracy generic openers and "takeaway" closers (GPT-4o, Gemini). Copied hallucinations lean slightly toward later input documents for 3 of 5 models. The input-side analysis uses 50-character string matching, so it covers only copied errors, not paraphrased or invented ones. Context-bound. [just-a-reference]
7. **Judge-mapping sensitivity as a calibration data point** -- switching PARTIAL between correct and incorrect moves conversation-domain recall by up to 30 points, and news by under 5%. The judge was validated mainly against gpt-4o, with Cohen's kappa 0.84 and 91% label agreement on matched pairs. Any reuse of the conversation-domain magnitudes should carry this. [just-a-reference]

## Limitations (our opinion)

The corpus is synthetic. SummHay documents were generated by GPT-4o from the
reference insights, contain no contradictions, and repeat each insight across
6+ documents. Real document sets with unplanned overlap, contradiction or
genuinely absent common ground were not tested. That matters for the
occasion: "shared information is thin" here means at least two planted shared
insights, and no condition has zero shared insights under the shared-only
prompt. The metric treats any bullet without a reference match as
hallucinated. That builds "not in the reference list" into the definition and
cannot separate a correct but unlisted merge from a real error, a weakness the
authors acknowledge. The headline rates use the optimistic mapping. In
conversation the level is uncertain by about 30 points, so only within-domain
comparisons and directions are safe there. The human taxonomy is the paper's
most interpretive evidence and its thinnest. It has two primary coders who
also authored the paper, N = 2 only, news-only frequencies, a few dozen errors
per cell, and multi-label categories without per-category agreement statistics.
The conclusion that "most errors are pedantic or instruction inconsistency" is
plausible, but the exact shares should not be generalized to N > 2 or to
conversation. Pedantic and instruction-inconsistency errors are partly
artifacts of this decomposition. A bullet-per-insight format with no target
count invites over-generation, and the authors link flat FDR to the
predicted-to-reference ratio. A count-informed or extract-then-verify pipeline
might shift the error mix, and the paper compares no alternative pipeline
designs. Generation used temperature 1 with one sample per input, so
run-to-run variation is not separated from systematic behavior. The
mitigation study covers only post-hoc filters at N = 2. The weak results may
reflect weak LLM classifiers rather than the limits of filtering, as the
authors note. The hierarchical alternative they recommend is untested. The
model set is from mid-2024.

## Recommended Next Action

Update evidence-register entry E17 in
`kb/work/epistemic-relevance-and-conceptual-blending/evidence-register.md` to
record the scope of what the paper shows. Asked for cross-document shared
insights with thin overlap (at least two planted shared insights), models
mostly output real but unshared single-document insights as shared: 58.54%-67.24% of
news errors at N = 2, with fabrication at most 2.4%. The absent case is only
tested as an undiscussed subtopic (abstention 20.65%-71.08%, falling with N).
The category shares come from author-coded, multi-label, news-only annotations
at N = 2.

---

Relevant Notes:

- [From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization](https://aclanthology.org/2025.findings-naacl.293/) — derived-from: the original paper
- [Out-of-spec output is a failure of the interpreter, not the spec](../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — is-evidence-for: measured MDS deviations are mostly explicit-condition violations, with fabrication rare
- [Soft degradation can bind before the hard cap even when required evidence fits](../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — is-evidence-for: recall and abstention fall with document count well inside the window; bounds the note because error share stays flat
- [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) — is-evidence-for: the human-coded "pedantic" class
- [Decomposition heuristics for bounded-context scheduling](../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — is-evidence-for: weak; the authors propose, untested, per-document summarization before merging
- [Generalization Bias in LLM Summarization of Scientific Research](./peters-chin-yee-llm-generalization-bias.ingest.md) — compares-with: scope distortion in summaries; overgeneralization is a minority error class here
- [Maximum Effective Context Window](./paulsen-maximum-effective-context-window-mecw.ingest.md) — compares-with: error scaling with input volume; flat output error share here vs rising hallucination there
- [GSM-DC](./gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) — compares-with: controlled growth of non-target input, different dose-response shapes
- [LongMemEval](./longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) — compares-with: abstention when requested information is absent
