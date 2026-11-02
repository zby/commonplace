---
description: "BNC corpus study of clarification requests: 3-4% of dialogue sentences, eight forms, four readings (clausal, constituent, lexical, correction), mostly targeting the previous sentence"
source: https://aclanthology.org/W01-1616.pdf
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce
ingested: "2026-11-01"
occasion: "Does this paper support the claim that clarification requests are frequent in ordinary dialogue and have classifiable forms and readings? What corpus figures and taxonomy does it provide, and do the readings concern expression meaning, speaker intent or what to do next? This 2001 SIGdial paper is the open stand-in for Ginzburg's The Interactive Stance (2012), which is not freely available."
type: types/ingest-report.md
domains: [clarification-requests, dialogue-repair, corpus-linguistics, formal-semantics]
---

# Ingest: On the Means for Clarification in Dialogue

## Classification

A short paper in the SIGdial 2001 proceedings combining a hand-annotated corpus study with a sketch of its consequences for an HPSG grammar and a dialogue-system implementation. The empirical part is descriptive frequency counting, not a controlled experiment.
Author: Matthew Purver and Jonathan Ginzburg (King's College London) and Patrick Healey (Queen Mary, London). Ginzburg is a principal author of the formal treatment of clarification and questions under discussion (QUD) that culminates in *The Interactive Stance* (2012); this paper is an early, openly available corpus basis for that line of work.

## Summary

The authors annotate every clarification request (CR) in a roughly 150,000-word sample of British National Corpus (BNC) dialogue: 200-turn sections from 59 transcripts. They classify each CR by form, reading and source sentence. The eight forms are non-reprise ("What do you mean?"), literal reprise sentence, wh-substituted reprise sentence, reprise sluice ("Who?"), reprise fragment ("Two people?"), gap, gap filler and conventional ("Eh?", "Pardon?"). The four readings are clausal (about the conversational move: "Are you asking/asserting that X?"), constituent (about what a part of the utterance refers to: "What/who do you mean by X?"), lexical (about the surface form: "Did you utter X?") and correction ("Did you intend to utter X instead of Y?"). CRs are just under 3% of sentences across all domains and just under 4% in casual conversation. Readings split roughly 46.5% clausal, 35% lexical, 14.5% constituent and 2.4% correction (all-domain table). Conventional and reprise-fragment forms each make up over a quarter of CRs. The scheme leaves only 0.5% of readings and about 1.5% of forms unclassified. Some forms, notably the reprise fragment, carry every reading, so the hearer must disambiguate. Annotators settled ambiguous readings from the other participants' responses and the initiator's acceptance of them. Most CRs target the immediately preceding sentence, over 96% target one within four sentences, and the maximum observed distance was 15. The authors conclude that a dialogue system needs a record of about ten utterances, including surface form, to handle most CRs. A single expert annotated everything, and reliability was not yet measured.

## Contribution assessment (our opinion)

The problem matters: a dialogue system that cannot recognise a CR misreads it as an answer, as in the paper's "Paris?" example, and formal analyses of CRs before this paper rested on constructed examples. The paper's main addition is an empirical form-by-reading distribution showing that a small taxonomy covers almost all CRs in a varied corpus. It also adds the distance measurement, which turns an open memory-retention question for the grammar into a bounded engineering parameter. The finding that lexical readings are frequent (about 35%) is the most consequential surprise, because the existing HPSG analysis did not cover them. The support is modest. One expert annotator, no agreement statistic, untested decision trees and sparse counts for the rarer forms make the headline proportions plausible but soft. The form-reading correlations for rare forms are explicitly tentative. The likely significance is as a seed corpus taxonomy for later clarification research. My guess is that later work refined the scheme rather than overturning it, but this capture cannot establish that.

## Quotes

> CRs were found to make up just under 4%
> of sentences when calculated over the demo
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §4.4.1, frequency in demographic portion (sentence continues after a footnote block)

> graphic portion, or just under 3% when calculated over all domains.
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §4.4.1, continuation: frequency over all domains

> The clausal reading takes as the basis for
> its content the content of the conversational
> move made by the utterance being clari ed.
> This reading corresponds roughly to \Are
> you asking/asserting that X?", or \For which
> X are you asking/asserting that X?".
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §3.1 clausal reading

> Another possible reading is a constituent
> reading whereby the content of a constituent
> of the previous utterance is being clari ed.
> This reading corresponds roughly to
> \What/who is X?" or \What/who do you
> mean by X?"
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §3.2 constituent reading

> Another possibility appears to be a lexical
> reading. This is closely related to the clausal
> reading, but is distinguished from it in that
> the surface form of the utterance is being clari ed, rather than the content of the conversational move.
> This reading therefore takes the form \Did
> you utter X?" or \What did you utter?".
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §3.3 lexical reading

> The correction reading appears be along the
> lines of \Did you intend to utter X (instead
> of Y)?".
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §3.4 correction reading

> Nearly 50% of CRs can be successfully
> interpreted as having a clausal reading, although both the lexical (about 35%) and constituent (about 15%) readings also make up a
> signi cant proportion.
> --- `kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md` @ `sha256:3b2b3893db8be52f4e0bb7fbf7275f17368f642ecf1c71721fa6fc911f96a6ce` — §4.4.1, reading proportions

## Connections Found

For the occasion, this paper is the anchor source for the claim that clarification requests are frequent and classifiable. It supports frequency and structure. It does not by itself support a broader claim about where meaning is settled, because most CRs concern hearing the words or identifying the move rather than what a term means.

In the KB, it is evidence for [Natural-language meaning is coordination among learned approximations](../theory/natural-language-meaning-is-coordination-among-learned-approximations.md). That note names other speakers as a weak, distributed checker of meaning. The corpus shows this checker operating in-band and often, at 3-4% of sentences. It also qualifies the note: only about 15% of CRs are constituent readings, which ask what an expression refers to. This is corroborating description, not a test the hypothesis could have failed.

It compares with [Silent disambiguation is the semantic analogue of tool fallback](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) on whether a wrong choice of reading becomes visible. In human dialogue a wrong pick is exposed by the initiator's next move: in the "spunyarn" exchange, a clausal answer is followed by "What's spunyarn?". The "Paris?" response (d) is the machine counterpart: an ambiguous move silently taken as an answer.

It compares with [Conversation vs prompt refinement in agent-to-agent coordination](../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) on in-band repair versus rewinding. The note asserts that humans can only append corrections. This paper measures how that append-only repair behaves: it is local and needs only about ten utterances of retained surface form.

The [Schegloff–Jefferson–Sacks repair study](./schegloff-jefferson-sacks-self-correction-repair.ingest.md) compares with this paper on repair organization: it explains ordered initiation opportunities and a structural preference for self-repair, whereas this paper measures clarification frequency and classifies forms and readings. Neither separates conventional expression meaning from speaker meaning.

Among sources, it gives the human side of the repair asymmetry discussed in [Dittrich's re-reading of Suchman](./jan-dittrich-rereading-suchman-plans-actions.ingest.md) and [the PD of HCI Suchman summary](./pd-of-hci-suchman-plans-situated-actions-summary.ingest.md). Those sources say humans repair breakdowns and classic machines do not detect them. This paper lists the means humans use.

## Extractable Value

1. **Frequency figures for clarification requests** -- CRs are just under 3% of sentences across all BNC dialogue domains and just under 4% in casual (demographic) conversation, in a sample of about 150,000 words from 59 transcripts. This is the citable support for "clarification requests are frequent in ordinary dialogue", with the single-annotator caveat beside it. [quick-win]
2. **Classifiable forms and readings** -- Eight forms and four readings cover nearly 99% of CRs. Only 0.5% of readings and about 1.5% of forms were "other", and the unclassified readings were expressions of surprise or outrage. This supports "classifiable forms and readings". It does not support finality: the authors say the form list may not be exhaustive, the scheme evolved during markup, and they suspect corrections may be subtypes of the other three readings. [quick-win]
3. **What a CR is about: mostly not expression meaning** -- The readings map onto the occasion's three-way question unevenly. The clausal reading (about 46.5%) concerns the speaker's conversational move, which is the speaker's intent at the level of the speech act. The lexical reading (about 35%) concerns which words were uttered, which is neither meaning nor intent. The constituent reading (about 14.5%) asks what a part of the utterance refers to. The correction reading (about 2.4%) asks which words the speaker intended. None of the four readings asks what to do next. The "Paris?" example shows that a reply can serve the task ("Paris is the quickest route"), but the paper does not classify that as a separate reading. A claim that repair settles meaning should therefore cite the roughly 15% constituent share, not the whole 3-4%. [quick-win]
4. **Expression meaning and speaker meaning are not separated** -- The constituent reading is modelled as a speaker-meaning relation between a sign, its speaker and the intended content: "What/who do you mean by X?". The "spunyarn" case, a request for the meaning of an unfamiliar word, falls under the same reading. The taxonomy therefore cannot establish whether a CR targets conventional expression meaning or one speaker's intended meaning. That distinction would need another source or the full book. [quick-win]
5. **Readings are ambiguous and settled by uptake** -- Ambiguity of reading is described as common, and the reprise fragment allows all readings. The annotators resolved readings from how other participants answered and whether the initiator accepted the answer. This makes the reading itself a coordinated outcome rather than a property fixed by form. It bears on the natural-language-meaning note's claim that meaning is held by checks. [experiment]
6. **Repair is local** -- Most CRs target the immediately preceding sentence, over 96% target one within four sentences, and the maximum observed distance was 15, in a crowded classroom. The authors draw a design rule: a record of about ten utterances, including syntax and phonology, suffices. For agent design, this suggests that in-band repair needs only short surface-form context. The figure is bounded by human spoken dialogue. [just-a-reference]

## Limitations (our opinion)

The proportions rest on one expert annotator, with no inter-annotator agreement measured and with decision trees not tested on naive users. The headline frequencies are plausible, but their second significant figure should not be trusted. The annotation scheme changed during annotation, so earlier and later decisions may not be consistent. The study counts CRs whose clarifying intent an annotator could recognise. That likely misses implicit repair, such as a puzzled pause or a reformulation without a request, so 3-4% is a floor on repair activity rather than a measure of all of it. Reading ambiguity was settled by uptake, and silence counted as acceptance. This method cannot detect misunderstandings that neither party noticed, which is the case that matters most for silent disambiguation. The corpus is British spoken English from casual, educational and business settings. It says nothing directly about written text, technical specifications or human-agent exchanges. Rare forms (gaps, fillers, corrections) have too few examples to support their claimed form-reading correlations, as the authors say. Finally, the paper is a stand-in for Ginzburg's later book. It predates *The Interactive Stance* by over a decade, so claims about that book's mature account cannot be grounded here.

## Recommended Next Action

Add the corpus findings as evidence in [Natural-language meaning is coordination among learned approximations](../theory/natural-language-meaning-is-coordination-among-learned-approximations.md), bounded to frequency and classifiability: only about 15% of CRs ask what an expression refers to, and the taxonomy does not separate conventional expression meaning from speaker meaning.

---

Relevant Notes:

- [On the Means for Clarification in Dialogue (ACL W01-1616)](https://aclanthology.org/W01-1616.pdf) — derived-from: the original paper
- [Natural-language meaning is coordination among learned approximations](../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) — is-evidence-for: corpus frequency of other-speaker checking, qualified by the small constituent-reading share
- [Silent disambiguation is the semantic analogue of tool fallback](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — compares-with: whether a wrong choice of reading becomes visible
- [Conversation vs prompt refinement in agent-to-agent coordination](../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — compares-with: measured locality of append-only human repair
- [Re-re-reading Lucy Suchman's Plans and Situated Actions](./jan-dittrich-rereading-suchman-plans-actions.ingest.md) — compares-with: who repairs a communication breakdown
- [PD of HCI - Plans and Situated Actions (summary of Suchman)](./pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) — compares-with: undetected breakdowns in human-machine exchange
