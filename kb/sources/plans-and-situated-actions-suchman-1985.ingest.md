---
description: "Suchman's 1985 PARC thesis: plans are vague resources for situated action, not its controllers; a copier help system shows the user-machine situational asymmetry"
source: https://bitsavers.trailing-edge.com/pdf/xerox/parc/techReports/ISL-6_Plans_and_Situated_Actions.pdf
captured: "2026-11-02"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 955d5f3173984a286c8d0781da6bc85830136a9bb863d2759df4a3e5a8c4735b
ingested: "2026-11-02"
type: types/ingest-report.md
domains: [situated-action, plans-as-resources, human-machine-communication, communicative-breakdown]
tags: [method-guided-action]
---

# Ingest: Plans and Situated Actions (Suchman 1985 PARC thesis, ISL-6)

## Classification

This is Lucy Suchman's February 1985 doctoral thesis, issued as Xerox PARC technical report ISL-6. It combines a theoretical argument drawn from ethnomethodology, conversation analysis and Heideggerian philosophy with a qualitative empirical study: a conversation analysis of videotaped first-time users of a photocopier's "expert help system". Its methodology, data and citations make it a `scientific-paper` in the KB's vocabulary, though as a thesis it was not peer-reviewed as a journal article. It is the primary text behind the 1987 Cambridge book *Plans and Situated Actions*, but it is an earlier version. The 1987 book and the 2007 second edition are separate texts.
Author: Suchman was an anthropologist in PARC's Intelligent Systems Laboratory. Her thesis committee included Hubert Dreyfus and John Gumperz. The work became a founding text of situated-action research in HCI and CSCW.

The capture is a `pdftotext` extraction of a scanned PDF's OCR layer. It is full-source, but OCR errors such as "INTRODUCfION" and "hancl" appear throughout, and the transcript tables of Chapter 7 lose their column layout.

## Summary

Suchman contrasts two views of purposeful action. In the planning view of Cognitive Science, plans precede action and prescribe it, and mutual intelligibility rests on recognizing each other's plans. In the situated view, plans derive from situated action: they are projections before the fact and reconstructions after it. Action, while it runs smoothly, is transparent, and rules and procedures are explicated only when it breaks down, after which the action is "made accountable to them". Because language is indexical, mutual intelligibility must be achieved on each occasion from situation particulars rather than from a stable body of shared meanings. A plan is therefore a map rather than a model: it works because its user has the terrain at the time of use. Plans are vague by design, and that vagueness suits contingent circumstances rather than being a defect to remedy. The empirical chapters analyse first-time users, often working in pairs, with a copier help system built on plan recognition. The machine can see only a restricted set of the user's effects and maps them onto a prescribed template. The analysis identifies two breakdowns the system cannot detect: the false alarm, where the user sees an error that does not exist, and the garden path, where a faulted action satisfies the design under another interpretation and goes unnoticed. Suchman concludes that the designer's real task is to "engineer alternatives to interaction's situated properties", chiefly by substituting a description of the situation for access to it. She holds that the design problem is not the gap itself but designers' identification of plans with situated action.

## Contribution assessment (our opinion)

The problem is important and was badly framed at the time. AI planning and intelligent-interface research assumed that action follows plans and that a machine could interact by recognizing them. The thesis's main contribution is conceptual reframing rather than a tested model. It turns the plan-action relation from an assumption into a research question, and it imports conversation-analytic tools to study human-machine exchanges as interaction. The empirical support is one qualitative case: a single rule-following help system with a modest corpus of first-time users, analysed by close reading of transcripts. That is enough to show the asymmetry and to exhibit the two breakdown types with concrete episodes. It is not enough to establish how general they are, and it gives no rival design that does better. The central claims are partly framed as in-principle limits ("intractable"), which makes them harder to test. A stronger test would compare designs that give the machine more situational access. Judging from the later reception of the 1987 book, the thesis's significance was large. On the evidence in the text alone, its demonstrated value is a sharp, durable diagnosis and vocabulary, with the generality of the in-principle claims left open.

## Quotes

No source quotes have been retained yet.

## Connections Found

This is the first primary Suchman text in the KB. Three secondary ingests already relay her argument: [Duguid, On rereading Suchman](./duguid-on-rereading-suchman-situated-action.ingest.md), [Dittrich, Re-re-reading Suchman](./jan-dittrich-rereading-suchman-plans-actions.ingest.md) and the [PD of HCI summary](./pd-of-hci-suchman-plans-situated-actions-summary.ingest.md). Each says in its limitations that Suchman's own claims need the book. This thesis compares with all three as their primary anchor, with one edition caveat. It contains the plans-as-resources argument, the map metaphor, the false-alarm and garden-path typology and the "engineer alternatives" conclusion. It does not contain the PD-of-HCI summary's list of three design problems (extend access, make limits clear, compensate), which may come from the 1987 book or from the summarizer.

The source's main role in theory is as a counterpoint and pre-LLM baseline for notes on how instructions guide execution:

- It compares with [agentic systems interpret underspecified instructions](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) on where the instruction-action gap originates. The note locates it in semantic underspecification that constraining can narrow. Suchman locates it in indexicality: an instruction's significance depends on circumstances it cannot carry, which she calls "an intractable problem" for providing in advance for the significance of instructions (§4.6). The two positions should be kept side by side rather than reconciled.
- It compares with [the two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md) on which layer runs by default. In §4.2 situated action is the default and rules appear only at breakdown, which inverts the note's method-first fast path for human operators.
- It compares with [fix what the executor can't determine](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) through the map metaphor. A map need not represent all the terrain because the traveller has the terrain at the time of use. Suchman gives no rule for what the plan must fix, which the note supplies.
- It compares with [silent disambiguation](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) on who detects and repairs breakdowns. The copier could detect neither false alarms nor garden paths; an LLM agent repairs ambiguity, but silently.
- It compares with [natural-language meaning as coordination among learned approximations](../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) through proposition (v): mutual intelligibility is achieved on each occasion rather than "discharged once and for all by a stable body of shared meanings". That is an ethnomethodological precedent for the note's hypothesis, with a different mechanism: situated repair rather than learned approximations held by checks.
- It compares with [intent-framed delegation](../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) and [MCDP 1](./marine-corps-mcdp-1-warfighting-1997.ingest.md) through the preface's Trukese navigator, who "begins with an objective rather than a plan". Suchman supplies no control regime of bounds, reporting or authority, which shows what intent-framing adds beyond situatedness.
- It compares with [human analogies suggest functions, not component boundaries](../theory/human-analogies-suggest-functions-not-component-boundaries.md): the designer should engineer alternatives to situated interaction rather than simulate it.
- It compares with [Naur's human-only conclusion](../theory/naur-equates-machine-execution-with-formulated-criteria.md) and the [Naur ingest](./programming-as-theory-building.ingest.md). Suchman infers a fundamental machine limitation from a 1980s rule-following system, and that inference needs an extra premise to reach other system classes, as Naur's does.
- It compares with [actionable methodology](../theory/definitions/actionable-methodology.md) on the setting-relativity of guidance. Plans-as-resources is a strong form of that relativity.

On the conversation-analysis side, Chapter 5 builds directly on the repair tradition in [Schegloff, Jefferson and Sacks](./schegloff-jefferson-sacks-self-correction-repair.ingest.md). [Purver, Ginzburg and Healey](./purver-ginzburg-healey-clarification-dialogue.ingest.md) give human-side clarification rates, where Suchman gives a machine that can neither issue nor recognize clarification. [Norman on automation feedback](./norman-problem-of-automation-inappropriate-feedback.ingest.md) diagnoses the same asymmetry from the other side: Suchman's machine cannot see the user's situation, and Norman's automation cannot report its own state.

## Extractable Value

1. **Context as a substituted situation description** -- Suchman's conclusion names the designer's move as substituting "a description of the situation of action, for access to the actual situation". An LLM agent likewise receives a constructed description of the operator's situation, but unlike the copier it can gather situational evidence through tools. No theory note states this framing, and it would connect context engineering, silent disambiguation and fix-what-the-executor-can't-determine. Its mechanism needs to be worked out before it meets the quality bar, and the transfer from a 1980s help system to LLM agents is analogy until it is. [deep-dive]
2. **Primary grounding for the Suchman cluster, with edition boundaries** -- Claims the secondary ingests attribute to Suchman can now be checked against her 1985 wording. These include plans as resources, the map metaphor, breakdown-triggered explication of rules and the false alarm and garden path. The "three design problems" list cannot be grounded in this text. Notes citing Suchman should cite this ingest for the 1985 claims and name the edition. [quick-win]
3. **Breakdown-default inversion** -- In §4.2, rules are explicated only when transparent activity breaks down, and action is then made accountable to them. This is a principled counter-case to method-first execution and qualifies the two-layer execution note. It is human-operator evidence and needs separate argument before it applies to agents. [experiment]
4. **False alarm and garden path as named breakdown types** -- These are observed, pre-LLM cases of breakdowns invisible to the executing system. The garden path is especially useful: a faulted action satisfies the design under a compatible interpretation, so the fault surfaces only later, when its source is hard to reconstruct. That is the structure of silent disambiguation and of out-of-spec success. [quick-win]
5. **Vagueness of plans as a design property** -- Ch. 8 argues that plans are vague because the detail of intent and action must depend on circumstances. This supports leaving execution-time choices open in directives, and it bounds the underspecified-instructions note's implication that more constraint always narrows the gap. [just-a-reference]

## Limitations (our opinion)

The empirical base is one qualitative case: a single plan-recognizing copier help system, a corpus of videotaped first-time users, and analysis by close reading of selected episodes. The thesis reports no comparison with a design that gives the machine more access to the situation. It therefore shows that this system class fails in these ways, but it cannot show that the failures are in-principle limits of machines. Its claims of intractability are stated at the level of the argument, not tested. That is the same gap the KB already identifies in [Naur's human-only conclusion](../theory/naur-equates-machine-execution-with-formulated-criteria.md). Any transfer to LLM agents is the reader's analogy. Modern agents interpret natural language, can ask clarifying questions and can gather evidence through tools, so the copier's specific blindness does not carry over directly. What may carry over is the narrower point that an agent's view of the operator's situation is a description, not shared access.

The theoretical chapters lean on authorities (Mead, Garfinkel, Heidegger via Dreyfus) more than on argument that would discriminate between the situated and planning views. A planning theorist could absorb much of it as a claim about plan granularity and replanning. This is the 1985 thesis, not the 1987 book, so book-only material must not be attributed to it. The OCR text has scattered character errors and the Chapter 7 transcript tables lost their layout, so quotations from that chapter need checking against the scanned PDF.

## Recommended Next Action

Update [agentic systems interpret underspecified instructions](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) with a short counterpoint citing this ingest: Suchman's §4.6 claim that an instruction's significance depends on circumstances it cannot carry, so part of the instruction-action gap is situational and cannot be closed by constraining. Keep the two positions side by side and mark the transfer from the copier study to LLM agents as analogy.

---

Relevant Notes:

- [Plans and Situated Actions, ISL-6 (PDF)](https://bitsavers.trailing-edge.com/pdf/xerox/parc/techReports/ISL-6_Plans_and_Situated_Actions.pdf) — derived-from: this analysis is worked out from Suchman's 1985 thesis
- [Agentic systems interpret underspecified instructions](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — compares-with: where the instruction-action gap originates, semantic underspecification versus indexicality
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md) — compares-with: which layer runs by default, with rules explicated only at breakdown
- [Silent disambiguation is the semantic analogue of tool fallback](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — compares-with: who detects and repairs breakdowns, and whether repair is visible
- [Duguid, On rereading Suchman](./duguid-on-rereading-suchman-situated-action.ingest.md) — compares-with: secondary reading checked against the 1985 primary text
- [PD of HCI Suchman summary](./pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) — compares-with: argument structure, with the three design problems absent from the thesis
