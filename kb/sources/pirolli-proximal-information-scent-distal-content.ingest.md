---
description: "Information scent as a Brunswikian lens model — judging unseen content from proximal cues, with spreading activation and a random-utility rule fitted to Web protocols; grounds the KB's pointer-quality and stopping claims"
source: http://act-r.psy.cmu.edu/wordpress/wp-content/uploads/2012/12/515uir-2004-07-pirolli.pdf
captured: "2026-08-24"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: dcbc565308e0a9eab683087f729137d462f8b6f0d5a8808f989b10b3095e1da2
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [information-foraging, navigation, context-engineering, cognitive-modeling]
---

# Ingest: The Use of Proximal Information Scent to Forage for Distal Content on the World Wide Web

## Classification

A chapter for an edited academic volume (Kirlik, ed., *Working with Technology in Mind*), issued as PARC tech report UIR-2004-07. It states a theory, derives a mechanism from a Bayesian rational analysis, and reports an empirical fit against coded think-aloud protocols, so it carries a paper's evidential obligations rather than an essay's. It is a synthesis of already-published work (Pirolli & Card 1999; Card et al. 2001; Morrison et al. 2001; Pirolli & Fu 2003) rather than a first report of new results.

Author: Peter Pirolli, PARC — originator of Information Foraging Theory with Stuart Card. That is the strongest credibility signal available on this topic and also the main bias to hold: the chapter is the program's author summarising his own program, and it reports no result that disconfirms it.

## Summary

Pirolli frames Web navigation as a Brunswikian lens-model judgment problem: the forager never observes the distal content, only proximal cues (link summaries, search-result snippets, node labels, thumbnails), and must predict the one from the other in a probabilistically textured environment. He argues the cues have real ecological validity — Davison's elaborated anchor text correlates with the page it links to at r = .16 against roughly 0 for a random page, and page-to-page similarity falls sharply with link distance, so the Web has topical patches. He then derives the forager's prediction problem as Bayesian log-odds, maps it onto ACT-R spreading activation (`Ai = Bi + Σj Wj Sji`, with association strengths estimated from corpus co-occurrence and shown equal to PMI), and closes it with a Random Utility Model choice rule (multinomial logit) so that choice is stochastic rather than always-take-the-best. The resulting SNIF-ACT simulation is checked against 189 coded actions from four participants on two of six representative-design tasks: higher-scent links are the ones followed, and model-computed scent declines across a run of pages before the user abandons the site, with a high-scent start page predicting a longer run. Read it if you want the canonical mechanism account of judging an unseen target from its pointer, plus a stopping rule derived from the same quantity; skip the SNIF-ACT architecture sections if you only need the framing and the cue-validity measurements.

## Quotes

- **Source extract (verbatim):** scent refers to the cues used by information foragers to make judgments related
  - **Source location:** Introduction, PDF page 3.
- **Source extract (verbatim):** to the selection of information sources to pursue and consume. These cues
  - **Source location:** Introduction, PDF page 3.
- **Source extract (verbatim):** concise information about content that is not immediately available. The
  - **Source location:** Introduction, PDF page 3.
- **Source extract (verbatim):** assessments of proximal information scent cues in order to make action choices
  - **Source location:** Introduction, PDF page 4.
- **Source extract (verbatim):** that lead to distal information sources. This view is a variant of Brunswik’s Lens
  - **Source location:** Introduction, PDF page 4.

- **Source extract (verbatim):** Human-information interaction systems will tend to maximize the
  - **Source location:** Adaptation framework and Equation 1, PDF page 5.
- **Source extract (verbatim):** value of external knowledge gained relative to the cost of
  - **Source location:** Adaptation framework and Equation 1, PDF page 5.
- **Source extract (verbatim):** (the anchor plus additional surrounding text, having a mean of 11.02 terms) to a
  - **Source location:** Topical Patches and Diminishing Returns, PDF page 10.
- **Source extract (verbatim):** Linked r = .16 and Random r ≈ 0. Davison’s analysis of the correlation of
  - **Source location:** Topical Patches and Diminishing Returns, PDF page 10.
- **Source extract (verbatim):** proximal cues to distal content confirms our intuition that the cues have
  - **Source location:** Topical Patches and Diminishing Returns, PDF page 10.
- **Source extract (verbatim):** The stronger the associations (reflecting greater predictive strength)
  - **Source location:** Mapping the Bayesian Rational Analysis to Spreading Activation, PDF page 14.

## Connections Found

The source is prior art, in close to canonical form, for the KB's navigation cluster: it is the anchor the cluster currently lacks. [Agents navigate by deciding what to read next](../notes/agents-navigate-by-deciding-what-to-read-next.md) states the follow/skip model with no citation; this chapter states it as the proximal-cue/distal-content lens and measures it. Its strongest role, though, is as technical basis for [linking theory](../notes/linking-theory.md), whose candidate theory — link quality as navigation-uncertainty reduction per token consumed — is offered without formalism or data, and which the chapter supplies with a value-per-cost maximization schema, an activation-plus-logit operationalization, and a protocol fit. It also sharpens two nearby notes rather than merely agreeing with them: it gives [link-following and search](../notes/link-following-and-search-impose-different-metadata-requirements.md) a causal direction its two-mode split lacks, and it supplies [charting the knowledge-access problem beyond RAG](../notes/charting-the-knowledge-access-problem-beyond-rag.md) with a protocol-validated navigation-mode decomposition where that note is openly guessing. Two notes gain captured prior work in place of recalled prior work: [information value is observer-relative](../notes/information-value-is-observer-relative.md), whose utility term is goal-conditioned by construction here, and [soft-bound traditions](../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md), whose twelve-row table omits the tradition that fits its own (processor, bound, mechanism) schema most directly. The countervailing role is a limitation: the population is 14 human students on the 1998–2003 Web paying wall-clock time, so every edge into an LLM-agent claim needs the transfer argument that [human-LLM differences are load-bearing](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) demands, and this source cannot supply it.

## Extractable Value

1. **A name and a measure for cue-to-content validity.** The KB has vocabulary for a pointer "carrying context" but none for *how well a cue predicts what it points at*; ecological validity is that term, and Davison's anchor-text correlations make it a measurable property of a description rather than a stylistic preference. This is the concept a description-quality gate would need to state its own criterion. [quick-win]

2. **Pointer quality and stopping are one quantity, not two design problems.** The same scent estimate both ranks the next move and sets the threshold for abandoning a patch. The KB reasons about pointer form and about when discovery stops in separate tags; the chapter's rate model (expected value of knowledge gained over cost of interaction) is the thing that would join them. [deep-dive]

3. **Cue quality causes mode switching.** Weak-scent tasks pushed participants out of link-following and into search (about 3.25 versus 1.25 result sets per participant), and higher-rated links were the ones actually followed. Our two-mode split treats link-following and search as parallel regimes with different metadata needs; this says search is the fallback that fires when link cues fail, which makes description quality the lever on how often the expensive mode runs. [quick-win]

4. **A transferable measurement method.** Web Behavior Graphs — a state-transition graph over a coded session, shaded by independently rated scent — plus the link/keyword/URL problem-space partition were produced from logged sessions with 91% and 93% inter-coder agreement. The same construction over logged agent sessions would let us measure our own navigation instead of reasoning about it analytically. [experiment]

5. **A thirteenth row for the soft-bound traditions table.** Processor: information seeker. Bound: time and attention in a probabilistically textured environment. Adaptation mechanism: scent-guided patch selection plus a patch-leaving threshold. It is closer to that note's subject than several rows already present. [quick-win]

6. **A goal-conditioned utility that is observer-relative by construction.** `U_{J|G}` is defined relative to the forager's goal and to association strengths learned from that forager's own history, so the same cue has different value for different observers by derivation rather than by assertion. That is a captured prior-work entry for a note whose survey is currently flagged as recalled. [just-a-reference]

## Limitations (our opinion)

Our reading, not the author's.

**The empirical baseline is a floor, not a comparison.** Link choice is tested against random selection. Nothing in the chapter pits the spreading-activation-plus-RUM scent measure against a simpler rival, even though the obvious rival — cosine similarity over anchor text — is computed a few pages earlier for Davison's validity numbers, and an LSA-based alternative (Blackmon et al. 2002) is cited in the discussion. The fit therefore supports "some cue-similarity measure predicts navigation choice," not "this derivation is the right account of it."

**Nothing was ablated, and the model's update space is narrow.** The only thing estimated from data is the association strengths, taken once from Tipster plus AltaVista counts. Fixed outside that space: cues are bags of words, the goal is a fixed word set, utility is summed activation, the choice rule is Gumbel, the link/keyword/URL partition came from analyst hand-coding, and the scent ground truth behind the patch-leaving figures is human judges' ordinal ratings. There is no within-session learning at all — the chapter concedes that different foraging histories should yield different category structures and files that under future work. So the reported fit exercises choices inside a decomposition it cannot itself test, and none of it attributes the result to the Bayesian derivation over any other scoring function ([learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)).

**The numbers are small where the claims are strongest.** Fourteen participants were run, four protocols on two of six tasks were analysed, 189 actions were coded, and the site-leaving curve averages twelve site-leaving actions. The related figure of judge-rated scent before departure is explicitly ordinal, with the author warning against reading it quantitatively. The patch-leaving threshold is the chapter's most reusable claim and rests on its thinnest data.

**Scope conditions are dated and human.** Stanford students, the 1998–2003 Web, hint scaffolding at ten and fifteen minutes, and cost measured in wall-clock time. The part most likely to transfer to an agent is the structural one — judge the target from its pointer and never load it — because that is what makes navigation cheap for any bounded reader. The part least likely to transfer is the learned-strengths mechanism: our reader pays linear context per byte with no skim, and starts each session with no association strengths at all. Treat any edge from this source into an LLM-agent claim as owing that argument rather than inheriting it.

**Self-report on a research program.** Roughly every supporting result is the author's own, and the failure cases discussed (non-text cues, learning) are framed as open problems rather than as evidence against the framework.

## Recommended Next Action

Update [linking theory](../notes/linking-theory.md) to cite this ingest as external grounding for its candidate theory, and to state which of its five predictions the foraging results actually bear on — prediction 4 (link density has diminishing returns) is the patch model under another name. Keep the edit to grounding and prediction status; whether nearby notes are rediscoveries of this tradition is a separate disposition question this ingest does not settle.

---

- [The Use of Proximal Information Scent to Forage for Distal Content on the World Wide Web](http://act-r.psy.cmu.edu/wordpress/wp-content/uploads/2012/12/515uir-2004-07-pirolli.pdf) — derived-from: Pirolli, PARC tech report UIR-2004-07
- [Agents navigate by deciding what to read next](../notes/agents-navigate-by-deciding-what-to-read-next.md) — is-evidence-for: states and measures the follow/skip decision the note models without citation
- [Linking theory](../notes/linking-theory.md) — is-evidence-for: supplies the formalism and data behind the note's value-per-cost candidate theory
- [Link-following and search impose different metadata requirements](../notes/link-following-and-search-impose-different-metadata-requirements.md) — is-evidence-for: weak cues drove participants from link-following into search
- [Pointer design tradeoffs in progressive disclosure](../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — is-evidence-for: a prior taxonomy of pointer forms with measured task performance across them
- [Charting the knowledge-access problem beyond RAG](../notes/charting-the-knowledge-access-problem-beyond-rag.md) — is-evidence-for: a navigation-mode decomposition validated against coded protocols
- [Information value is observer-relative](../notes/information-value-is-observer-relative.md) — is-evidence-for: utility defined relative to the forager's goal and learned history
- [Soft-bound traditions as sources for context engineering strategies](../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — is-evidence-for: information foraging fits the note's schema and is absent from its table
- [Human-LLM differences are load-bearing for knowledge system design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — is-evidence-for: a worked instance of inherited human-oriented research with testable scope conditions
- [Navigation](../reference/navigation.md) — see-also: the shipped cost-ordered navigation stack is this tradition instantiated under other names
- [Ingest: Agentic Note-Taking 23: Notes Without Reasons](./agentic-note-taking-23-notes-without-reasons-202689418851669643.ingest.md) — compares-with: measured cue validity against reported cue absence, on what a pointer must carry for pre-load relevance judgment
