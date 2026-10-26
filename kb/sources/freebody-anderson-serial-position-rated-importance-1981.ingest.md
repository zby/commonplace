---
description: "1981 study finding that both serial position and rated importance independently predict text recall, with a primacy effect stronger than recency."
source: https://scispace.com/pdf/serial-position-and-rated-importance-in-the-recall-of-text-4qw5q6il4r.pdf
captured: "2026-10-26"
capture: user-supplied-online-markdown-conversion
capture_scope: partial-source
genre: scientific-paper
snapshot_sha256: 83aaecfecbf1c345abcfcba4a7a2f7dff426219767624aafa336a2b17a8f2a20
ingested: "2026-02-28"
occasion: "What human-reader evidence can inform the planned Commonplace note about position, proportion, and what readers retain?"
type: types/ingest-report.md
domains: [text-recall, serial-position, memory, primacy-recency]
learning_claims: true
---

# Ingest: Serial Position and Rated Importance in the Recall of Text

## Classification

Scientific paper (technical report). Multiple regression analysis of free-recall protocols from controlled reading experiments. Author signal: Freebody and Anderson are established reading researchers at the Center for the Study of Reading, University of Illinois; the report is part of a series of related experiments on vocabulary, text cohesion, and comprehension.

## Summary

Freebody and Anderson (1981) examined whether serial position and rated importance of text propositions predict their appearance in free-recall protocols. Across 8 passages read by approximately 228 sixth-grade students, multiple regression showed that both rated importance (r = .191) and serial position (r = -.214) independently predict recall probability. The quadratic of serial position is also a significant predictor, indicating a recency effect. The study found a strong primacy effect and a moderate but significant recency effect, with importance and position contributing independently—no interaction between them. The authors argue the effects are stable and generalizable due to the large number of subjects, propositions, passages, and experimental conditions.

## Contribution assessment (our opinion)

This is a well-structured empirical study that directly tests and confirms two distinct predictors of text recall—position and importance—using a large, varied sample. The contribution to the problem of what determines what readers retain is clear and useful: it shows that position effects survive even when importance is controlled, and that importance operates independently of position. The recency finding (quadratic of position significant) adds nuance: late-appearing content gets a measurable boost, though weaker than primacy. The effect sizes are modest (position explains ~4.6% of variance, importance ~3.7%), but the authors make a reasonable case for stability given the design. The primary limitation is the specific population (sixth-graders, above-average achievement) and the partial-source capture with OCR artifacts in figures. The paper does not test competing accounts of why position matters—it confirms the effect exists but does not adjudicate between the "authors put important content at ends" hypothesis and a pure temporal-accountability account. Originality relative to the existing literature at the time appears genuine: the paper explicitly surveys discrepant prior findings (Deese & Kaufman 1957; Frase 1969; Meyer & McConkie 1973; Richardson & Voss 1960) and positions itself as resolving the inconsistency through a larger, more varied design.

## Quotes

> The results of the analysis are summarized in Table **1.** It can be seen that importance, position, and the quadratic of position predict significant portions of the variance. Simple correlations indicate that importance is positively related to probability of recall (r = .191), while position is negatively related (r = -.214). It is of note that these contribute independently to the prediction. In order to clarify the relationship between serial position and recall, the best-fitting equation was found for probability of recall regressed on position and then position-squared. The equation was then solved for 10-point intervals of the percentile position scale. The resulting relationship is presented in Figure 1. It can be seen that there is a strong predicted primacy effect and a moderate but significant recency effect. While the amount of variance accounted for is not great, the effect may be thought to be stable and generalizable due to the large number of subjects, propositions, passages, and experimental conditions in which they appeared.
> --- `kb/sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md` @ `sha256:83aaecfecbf1c345abcfcba4a7a2f7dff426219767624aafa336a2b17a8f2a20` — Results and Discussion, p. 8

> Only two of the analyses of individual passages showed significant effects for the quadratic component. Trends toward significance appeared in two other passages. The linear component was significant for five of the passages, with a trend in one other.
> --- `kb/sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md` @ `sha256:83aaecfecbf1c345abcfcba4a7a2f7dff426219767624aafa336a2b17a8f2a20` — Results and Discussion, p. 8

> The next-to-last paragraph in "Trade Laws" is a continuing description of the reasons for tariffs. The last paragraph is a one-sentence conclusion in figurative language. Thus, it might have mnemonic value due to its structural significance as a conclusion or encapsulation and to its possible imagery value, as well as its position.
> --- `kb/sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md` @ `sha256:83aaecfecbf1c345abcfcba4a7a2f7dff426219767624aafa336a2b17a8f2a20` — Results and Discussion, p. 11

> Various factors may be operating in the advantage of early and late appearing propositions in the overall analysis. It has been the function of this study to demonstrate, over a very large number of propositions, appearing in a variety of passages and textual conditions, that early and, to a lesser but significant extent, later propositions are better recalled. It has also been shown that the rated importance of a proposition predicts probability of recall independently of its serial position.
> --- `kb/sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md` @ `sha256:83aaecfecbf1c345abcfcba4a7a2f7dff426219767624aafa336a2b17a8f2a20` — Results and Discussion, p. 14

## Connections Found

- [LLM context is composed without scoping](../theory/llm-context-is-composed-without-scoping.md) — **is-evidence-for**: The theory note states that ordering conventions in LLM context assembly "exploit primacy/recency effects but provide no isolation." This paper is the classic empirical demonstration that primacy and recency effects operate in human text recall specifically—both predict recall independently, with primacy stronger than recency. The human cognitive science evidence base for the phenomenon the note invokes.
- [Knowledge storage does not imply contextual activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: The theory note draws on human memory research (Tulving & Pearlstone's availability vs. accessibility distinction) to argue that storage does not guarantee retrieval or use. This paper provides complementary evidence about what factors affect recall probability—specifically that both proposition importance and serial position independently predict whether content is recalled. Relevant to the broader argument that what is stored is not what is accessed.
- [Psychology-to-agent-transfer needs per-principle failure-mode testing](../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — **see-also**: This note establishes a methodology for evaluating whether cognitive science findings transfer to agents. The Freebody & Anderson paper is an instance of the type of human cognitive psychology research this methodology would evaluate—a controlled study of serial position and importance effects on text recall. Citing it in discussions of agent memory design would require per-principle failure-mode analysis before assuming the findings apply to LLM agents.

## Learning Claims (our opinion)

The source's mechanism on its own terms: the paper studies what determines whether propositions from read text appear in free recall. The mechanism is not a learning process in the theory-builder sense (conjecture, criticism, iteration); it is an empirical characterization of correlates of recall probability. The paper finds that two factors—where a proposition appears in the text (serial position) and how important readers rate it—each independently predict recall.

Mapping onto Commonplace concepts: the paper is evidence about *what is retained from reading*, which relates to the KB's interest in context composition and what readers (human or agent) retain from input. The primacy/recency finding is directly relevant to [LLM context is composed without scoping](../theory/llm-context-is-composed-without-scoping.md), which invokes primacy/recency effects as a phenomenon that ordering conventions exploit. The independence of importance from position is relevant to [Knowledge storage does not imply contextual activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md): rated importance—a property of the content, not its position—also predicts recall, supporting the idea that not all retained content is equally accessible or useful.

Theory-builder conditions: the paper does not itself constitute a theory builder. It has localized content (the regression results and their interpretation), and it applies a form of empirical criticism (significance testing, effect-size analysis). But it does not iterate—this is a single study reporting a snapshot of findings, not a system that revises its theories in response to criticism. The paper contributes evidence to our account; it does not model a learning system.

What the source adds to, supports, or puts in question: it strengthens the empirical basis for the claim that position effects in recall are real and operate alongside content-based factors. It does not put our current account in question, because our notes invoke primacy/recency as a known phenomenon rather than claiming it is exclusive or sufficient. The paper's finding that importance and position are uncorrelated (r = .006) is useful: it means the two effects are separable, which matters for any design that wants to weight content by importance rather than rely solely on position.

## Extractable Value

1. **Empirical confirmation that primacy and recency effects operate in text recall, with primacy stronger than recency.** The paper's regression results (position linear F = 20.66, quadratic F = 7.87, both p < .01) and the figure showing the predicted recall curve give a concrete, quantified basis for the primacy/recency claims used in [LLM context is composed without scoping](../theory/llm-context-is-composed-without-scoping.md). This is the human-reader evidence the occasion asked for. [{quick-win}]

2. **Importance and position are independent predictors of recall.** The near-zero correlation between importance ratings and serial position (r = .006) means the two effects are separable. For any system that wants to weight retained content by thematic importance rather than just position, this paper provides evidence that importance-weighted selection can add value beyond position-based selection. [{deep-dive}]

3. **The paper addresses position and what readers retain, but not proportion.** The occasion asked about "position, proportion, and what readers retain." The paper addresses position and what readers retain, but not proportion—the relationship between how much content is presented and how much is retained, or how proportion of important content affects recall. That gap is a limitation of using this paper for the occasion's full question. [{just-a-reference}]

## Limitations (our opinion)

- **Population and materials constraint.** The subjects were sixth-grade students in a small central Illinois city, approximately half a standard deviation above mean achievement. The eight passages were 250–300 words, four adapted from a Grade 6 social studies program and four written to match. Whether the same primacy/recency pattern holds for adult readers, longer texts, or more complex discourse structures is not established by this study. Generalization beyond the tested population and text type is an open question.

- **Partial-source capture with OCR artifacts.** The snapshot is a user-supplied online Markdown conversion with OCR limitations. Figure captions and some passages contain garbled characters; the figures themselves (especially Figures 1, 2, and 3, which show the predicted recall curves) are represented only as garbled text. The abstract and main text are readable, but the capture quality limits confidence in any quotes drawn from the figures or from passages near OCR-corrupted regions.

- **No competing-account test.** The paper confirms that position and importance predict recall and that they are independent. It does not test why position matters—whether because authors cluster important content at text boundaries (the Meyer & McConkie hypothesis) or because of a pure temporal primacy/recency mechanism. The "why" is relevant if our KB's use of the finding depends on a particular account of the mechanism.

- **Effect sizes are modest.** Position explains 4.57% of variance and importance 3.70% in the combined analysis. The paper argues the effects are stable and generalizable given the design, but the modest variance explained means position and importance are not the whole story; other factors (background knowledge, perspective, text structure, genre) also matter and are not controlled here.

- **Capture scope is partial-source.** The retained boundary prevents the ingest from establishing whether the full paper contains additional analyses, caveats, or qualifications not present in the captured text.

## Recommended Next Action

Update [LLM context is composed without scoping](../theory/llm-context-is-composed-without-scoping.md) to cite this paper as the empirical basis for the primacy/recency claim currently stated without a source. The paper's finding that both primacy and recency operate in text recall, with primacy stronger than recency, is exactly the human-reader evidence the note invokes. Add a citation in the paragraph that states ordering conventions "exploit primacy/recency effects but provide no isolation," with a note that the source is Freebody & Anderson (1981), Technical Report No. 219, Center for the Study of Reading.
