---
description: "Dittrich's blog re-reading of Suchman's Plans and Situated Actions (2nd ed.): plans-as-executed-programs vs situated action, opportunistic method use, and the one-sided machine repair asymmetry"
source: https://www.fordes.de/posts/rerereading_suchman_plansActions.html
captured: "2026-10-31"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: c4a7caa08323163618131933e81e4518131151be1179be18477df4b6cb9f3d06
ingested: "2026-10-31"
occasion: "workshop kb/work/operationalization-executability-automation asks how operationalizing knowledge for a defined task and executor relates to execution, function-level automation, and decision autonomy. This is a secondary reading of Suchman's Plans and Situated Actions, standing in for the book itself, which is too long to ingest; record which edition the post reads."
type: types/ingest-report.md
domains: [situated-action, plans-and-practice, human-machine-interaction, interpretive-asymmetry]
tags: [method-guided-action]
---

# Ingest: Re-re-reading Lucy Suchman's Plans and Situated Actions

## Classification

This is a personal reflective blog post (dated 2023-06-30, with notes added 2025-09-08 and 2025-12-30) about reading a book three times. It reports no study and makes no formal argument of its own; it relays Suchman's position, two page-cited passages, and the author's reasons for distance from it. That makes it a `conceptual-essay` and a secondary source on Suchman.

Author: Jan Dittrich, a design researcher whose PhD work concerns instructions and tutorials people use to learn skills. He is a reader of the HCI and STS literature, not a Suchman specialist or her commentator of record.

**Edition read.** A footnote states that the author always read "the expanded second edition from 2006, titled 'Human Computer Reconfigurations'", and that some cited authors may be absent from the 1987 original. The page citations in the post (p70 for the definition of situated action, p.187 for the chapter "Plans, Scripts and Ordering Devices") are therefore second-edition pages, and the "Plans, Scripts" chapter exists only in that edition. From background knowledge, not from the source: Cambridge University Press published the second edition as *Human-Machine Reconfigurations: Plans and Situated Actions*, usually dated 2007 (copyright 2007, some listings 2006). Treat the blog's title wording and year as the author's recollection.

## Summary

Dittrich explains that Suchman's "plans" are not everyday plans but plans as conceived in cognitive science: to-be-executed future actions derived from an analysis of the situation, with deviations treated as special cases. Suchman's alternative, situated action, holds that "every course of action depends in essential ways on its material and social circumstances" (p70, 2nd ed.), building on Mead, Blumer and Garfinkel's ethnomethodology. Her empirical case is people using a photocopier with an expert help system; her four-column transcripts separate what the user did that was available to the machine, what was not, what the machine displayed, and the design rationale, showing the machine tracking the user "through a very small keyhole". Dittrich relates this to his own observation that design methods and instructions diverge from practice, are used opportunistically, and partly serve to claim rationality before peers. He keeps distance from Suchman's critique of cognitive-science plans and from her language-centred conversation-analysis method, and finds the second edition's "artifacts involved in social ordering" confusingly wide. Later notes add Wilf's and Adam's point of an "interpretative asymmetry": people repair what machines give them, while machines do not repair human input. Read it for a short orientation to the book and its second-edition additions, not as a substitute for the book.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the operationalization workshop, the source's role is a **secondary pointer** to Suchman's situated-action claim, with an identified edition and page, while the primary book remains uncaptured. It does not supply Suchman's argument in enough detail to carry claims about plans and execution on its own.

Within the theory layer it is a **counterpoint from an older tradition**. [Agentic systems interpret underspecified instructions](../theory/agentic-systems-interpret-underspecified-instructions.md) explains the gap between written instruction and action through semantic underspecification of the instruction; Suchman, as relayed here, locates the gap in the material and social circumstances of action, which no amount of specification removes. [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md) treats departure from method outside its coverage as normal operation; Dittrich's report of opportunistic method use agrees, and adds a function the note lacks: methods kept to display rationality rather than to cover cases. [Actionable methodology](../theory/definitions/actionable-methodology.md) makes a methodology's actionability relative to operator, operations, target and setting; Dittrich's target is "the assumption that there are right ways of doing something outside of a particular situation and value context", the same setting-relativity stated as critique.

The repair point gives an **HCI baseline** for [silent disambiguation](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md). The Wilf/Adam asymmetry says the human repairs and the machine does not; LLM agents now repair underspecified human input, and the note's concern is that this repair is invisible. Among sources, [Norman's "Problem" of Automation](./norman-problem-of-automation-inappropriate-feedback.ingest.md) is the closest peer: both are 1980s accounts of interactional resources a machine lacks relative to a human partner. Suchman's photocopier cannot interpret the user; Norman's automation cannot report its own state.

## Extractable Value

1. **Edition and page anchor for the workshop's Suchman citation** -- the post read the second edition (cited by the blogger as 2006, "Human Computer Reconfigurations"; published as *Human-Machine Reconfigurations*), and its situated-action definition sits at p70 of that edition. The workshop can cite a specific edition and page when it eventually captures the book, and must not treat this paraphrase as the 1987 argument. [just-a-reference]
2. **"Plan" names an executable representation, not an intention** -- Suchman's target is plans-in-cognitive-science: a situation analysis yields a plan that is then executed, with deviations as special cases. That is close to what the workshop calls operationalized knowledge handed to an executor. The occasion's question (operationalization versus execution) inherits Suchman's challenge: if every course of action depends on circumstances, an operationalized artifact constrains execution without determining it. This sharpens rather than answers the workshop question, and it is a paraphrase of a paraphrase. [quick-win]
3. **Interpretive asymmetry as a decision-autonomy axis** -- whether the executor repairs breakdowns in the instruction (humans do; classic machines do not; LLM agents now do) is a candidate dimension for the workshop's distinction between function-level automation and decision autonomy. It also supports the synthesis that LLM agents invert the classic HCI repair asymmetry, moving the design problem from the machine's narrow keyhole to the visibility of its repairs, as in [silent disambiguation](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md). The claim needs primary grounding in Suchman, Wilf or Adam before it becomes a note. [deep-dive]
4. **Four-column availability analysis** -- Suchman's transcripts split each step into user actions available to the machine, actions not available, machine display, and design rationale. The same split could audit an agent's observation channel: what of the operator's situation the agent receives, what it does not, what it shows, and why. This is a method suggestion inferred from the post's description, not a tested practice. [experiment]
5. **Methods as display of rationality** -- the post reports that design methods are used opportunistically and partly to claim rationality before peers. The KB has no landing site for a legitimacy function of methods; one blog mention is below the quality bar for a note. [just-a-reference]
6. **Second-edition pointer to scripts and ordering devices** -- the added chapter "Plans, Scripts and Ordering Devices" engages Woolgar's "configuring the user" and Akrich's "de-scription" of technical objects. These are leads if the workshop needs the STS account of artifacts that prescribe users' actions. [just-a-reference]

## Limitations (our opinion)

The post is a secondary, selective reading by an author who says he had trouble thinking along with the book's notion of plans. Its account of Suchman is a few sentences plus two page citations, so it cannot establish what Suchman argues about plans as resources for action, the role of plans after the fact, or her second-edition revisions; any KB claim attributed to Suchman needs the book itself, which this capture does not contain. The interpretive-asymmetry point is reported thirdhand from Wilf and Adam in two short dated notes, without their arguments. Nothing in the post is tested: the opportunistic-use claim rests on literature the author points to but does not summarize, and the "claim rationality" function is a suggestion ("It is also unclear how much…"). The edition title as given ("Human Computer Reconfigurations", 2006) differs from the published title, so the footnote is reliable for which edition but not for bibliographic detail. The photocopier study is a pre-LLM system with no capacity to repair input; transferring its keyhole analysis to agents that do interpret and repair is the reader's analogy, not the source's.

## Recommended Next Action

Add this ingest to the source table in `kb/work/operationalization-executability-automation/exploration.md` as a secondary pointer to Suchman's second edition (*Human-Machine Reconfigurations*, situated-action definition at p70), keeping the primary Suchman source marked as still blocked rather than retained.
