---
description: "Uncredited 1997 HCI course summary of Suchman's Plans and Situated Actions (1987): plans as resources not controlling structures, copier breakdown types, three design problems"
source: https://uni-koeln.de/hf/konstrukt/didaktik/situierteslernen/PD%20of%20HCI%20-%20Suchman.htm
captured: "2026-10-31"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 5831665794ea06ed1527c3c1c2645912f5e4da01af1f5b5d56ae14bcb4442e85
ingested: "2026-10-31"
occasion: "workshop kb/work/operationalization-executability-automation asks how operationalizing knowledge for a defined task and executor relates to execution, function-level automation, and decision autonomy. This is a 1997 course reading summary of Suchman's Plans and Situated Actions (1987 edition) from an HCI course, a secondary source standing in for the book, which is too long to ingest; record that it is an uncredited student-style summary."
type: types/ingest-report.md
domains: [situated-action, plans-and-practice, human-machine-interaction, interactional-breakdown]
tags: [method-guided-action]
---

# Ingest: PD of HCI - Plans and Situated Actions (summary of Suchman)

## Classification

This is a chapter-by-chapter summary of a book, written as a course reading page for a Participatory Design of HCI course and last updated 7 April 1997. It reports no study and adds almost no argument of its own; it paraphrases Suchman's position, her copier study and her design conclusions. It is therefore a `conceptual-essay` in genre and a secondary source on Suchman. It reads the 1987 first edition, the only one that existed in 1997, and it cites that edition in its reference list.

Author: uncredited. The page names Mikael Jakobsson (Umeå University informatics) as the responsible maintainer, but does not say who wrote the summary. Its register — first-person-plural framing, loose terminology ("adjacent pairs" for adjacency pairs), and grammatical slips — reads as a student-style course summary, not a specialist commentary. The captured copy is a mirror on a University of Cologne didactics site; the page gives its original location as an informatik.umu.se course page.

## Summary

The summary presents Suchman's argument that plans do not precede and determine action: actions are tied to particular situations, and people fit them into a plan mainly when they must account for them. It reports her critique of the "planning model" in AI, where intentions are uncompleted parts of an already executing plan, and her objections: the model cannot handle unrealized intentions or unplanned intentional action, world models cannot hold common-sense background knowledge, and background assumptions are generated during interaction rather than held beforehand. Her alternative, situated action, is presented as a research programme grounded in ethnomethodology: plans are representations that arise when "otherwise transparent activity becomes in some way problematic", language is indexical, and mutual intelligibility is achieved on each occasion. The empirical core is a study of first-time users of a copier with an expert help system that inferred the user's plan from detectable actions. The system misread requests for help, could not detect "false alarms" (the user wrongly believes an error occurred) or "garden paths" (an error the user does not notice), and users misread the machine by applying conventions of human interaction. Suchman draws three design problems: extend the machine's access to the user's actions and circumstances, make clear the limits of that access, and compensate for what it lacks. The summary also reports strategies of real-time user modelling (differential modelling against expert use, local and global interpretation, turning non-constructive trouble into constructive trouble) and the conclusion that design should "engineer alternatives to the situated properties of interaction" rather than simulate human communication. Read it for the outline of the 1987 argument; it is not a substitute for the book.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the operationalization workshop, this source's role is a **second secondary pointer** to Suchman, complementing the [Dittrich re-reading](./jan-dittrich-rereading-suchman-plans-actions.ingest.md) on a named axis: edition and coverage. Dittrich reads the second edition and gives a page anchor but little of the argument; this summary reads the first edition and gives its argument structure — plans as resources, plans as after-the-fact accounts, the breakdown typology and the three design problems — which the Dittrich ingest explicitly could not establish. Neither replaces the book.

In the theory layer the source is a **counterpoint from situated-action theory**. [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md) runs the method by default and falls back to theory outside its coverage; Suchman, as summarized, inverts the default: situated activity runs by default and the plan is consulted when activity becomes problematic. [Agentic systems interpret underspecified instructions](../theory/agentic-systems-interpret-underspecified-instructions.md) locates the instruction-action gap in semantic underspecification; the summary locates it in indexicality, where meaning is conditional on the situation of use, which more specification does not remove. [Actionable methodology](../theory/definitions/actionable-methodology.md) already makes guidance relative to operator, operations, target and setting; the summary's "event driven resources for action rather than controlling structures" is the strong form of that setting-relativity.

The copier study gives a **pre-LLM baseline** for [silent disambiguation](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md). Suchman's machine could detect neither false alarms nor garden paths; LLM agents now repair underspecified input, and the note's concern is that the repair is invisible. Her second design problem, making clear to the user the limits of the machine's access, sits beside [Norman's "Problem" of Automation](./norman-problem-of-automation-inappropriate-feedback.ingest.md): both are late-1980s diagnoses of interactional resources the machine lacks. Suchman's conclusion that design gains more from understanding human-machine differences than from assuming similarity bears on [human analogies can motivate functions without determining component boundaries](../theory/human-analogies-suggest-functions-not-component-boundaries.md) as an early HCI instance of keeping the function while refusing the human form; it does not test that note.

## Extractable Value

1. **Plans as resources, not controlling structures, for the workshop's operationalization question** -- the summary gives the 1987 position the Dittrich ingest lacked: plans are representations used when activity becomes problematic, and they also serve as after-the-fact accounts of action. If operationalized knowledge is a plan in this sense, an operationalized artifact is a resource the executor consults at breakdowns, and its executability depends on the executor's situated work around it. This sharpens the workshop's section on a plan constraining action without determining it, but it is still a paraphrase; any claim attributed to Suchman needs the book by edition and page. [quick-win]
2. **The three design problems as an executor-access checklist** -- extend the machine's access to the user's actions and circumstances, make the limits of that access clear, and compensate for what it lacks. For the workshop's function-level automation versus decision autonomy question, these name what an executor must have before it can be trusted with a decision rather than a function. The mapping to LLM agents is our inference; the source concerns a copier help system. [experiment]
3. **False alarm and garden path as breakdown types** -- the two communicative breakdowns the copier could not detect give vocabulary for a pre-LLM baseline in the repair-locus synthesis already flagged in the Dittrich ingest: classic machines detected no breakdown, LLM agents repair but silently. The typology adds a distinction between errors the user perceives but did not make and errors the user made but does not perceive. [deep-dive]
4. **Situated default with plan fallback** -- the inversion of the two-layer execution system's default is a candidate qualification for that note: for some operators and settings the situated layer, not the method, is the fast path. Holding it at the strength of a secondary summary, it is a prompt for review, not evidence. [just-a-reference]
5. **"Engineer alternatives, do not simulate"** -- a pre-LLM HCI precedent for the KB's position on human analogies. Useful as a historical citation once grounded in the book. [just-a-reference]

## Limitations (our opinion)

The source is an uncredited course summary of a book, captured from a mirror; its author's understanding of Suchman cannot be checked from the page. It compresses a book-length argument into under two thousand words, sometimes loosely: it writes "adjacent pairs" for adjacency pairs, garbles the Cohen and Perrault point about speaker and hearer models, and does not separate Suchman's own proposals from the systems she discusses. In particular, the differential-modelling strategy it presents as a design recommendation resembles the WEST coach's strategies (Burton and Brown), which the summary mentions earlier; from background knowledge, not the source, Suchman draws on those coaching strategies rather than originating them, so the attribution should not be trusted. Quotation marks in the summary do not establish Suchman's wording, and there are no page numbers. The argument itself is conceptual and rests on one qualitative video study of first-time users of one expert help system, so the summary cannot show how far its conclusions generalize. Transferring the copier analysis to LLM agents, which do interpret and repair input, is the reader's analogy, not the source's.

## Recommended Next Action

Add this ingest to the source table in `kb/work/operationalization-executability-automation/exploration.md` as a second secondary pointer to Suchman, recorded as an uncredited 1997 course summary of the 1987 first edition, and extend section 6.6 with its plans-as-resources and three-design-problems points, marked as secondhand and still requiring the book by edition and page.
