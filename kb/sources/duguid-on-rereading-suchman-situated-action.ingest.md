---
description: "Duguid 2012 rereads Suchman: plans are interpreted resources, not controllers of action; conformity pressure hides plan gaps; scale can disguise principled limits as practical ones"
source: https://lelibellio.polytechnique.fr/uploads/volume8_num2/articles/p3-9-on_rereading._suchman_and...1.pdf
captured: "2026-10-31"
capture: pdftotext
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 8a9548aa2ae053c679a710497239e0b30d8706579e21bf5283bb31f5e79d8466
ingested: "2026-10-31"
occasion: "workshop kb/work/operationalization-executability-automation asks how operationalizing knowledge for a defined task and executor relates to execution, function-level automation, and decision autonomy. This is Paul Duguid's 2012 essay \"On rereading. Suchman and Situated Action\" in Le Libellio d'AEGIS vol. 8 no. 2 pp. 3-9, a secondary source on Suchman's Plans and Situated Actions standing in for the book, which is too long to ingest."
type: types/ingest-report.md
domains: [situated-action, plans-as-resources, routinization, principled-vs-practical-limits]
tags: [method-guided-action]
---

# Ingest: On rereading. Suchman and Situated Action

## Classification

This is a short retrospective essay in a French management-research bulletin. It reports no study and makes no new empirical claim. It relays Suchman's 1987 argument and her 2007 second edition, places them in an intellectual lineage, and argues for their continuing relevance. That makes it a `conceptual-essay` and a secondary source on Suchman.

Author: Paul Duguid (UC Berkeley), co-author with John Seely Brown of *The Social Life of Information* (2000). He worked in the same Xerox PARC and Institute for Research on Learning circle as Suchman and Julian Orr, so he writes as an informed insider and sympathetic reader, not as a neutral critic.

## Summary

Duguid rereads Suchman's *Plans and Situated Actions* (1987; 2nd ed. 2007) on its 25th anniversary. He makes four claims that a reader of the book would want. First, Suchman did not offer situated action as an alternative to planning, as Simon and Vera read her. She treated plans as "discursive tools" that require interpretation through situated action: one resource among many, not a preordained means of controlling action. Second, this separates devices built to execute preordained plans accurately from humans who use plans in context and improvisationally. Xerox's response to unusable copiers illustrates the gap: more detailed instructions overwhelmed users, and "expert help systems" assumed a user could be reduced to a goal plus an executable plan. Third, drawing on Orr's ethnography of Xerox technicians, Duguid argues that a demand for conformity produces "surreptitious routinization": workers make the world appear to follow the plan. This hides both the plan's inadequacy and the insight gained by improvising. Fourth, he frames the whole critique around Moore's Law, which "often allowed principled objections to appear as merely practical ones". It is hard to tell whether a failing system lacks computing power or rests on a misconceived task. The essay also traces Suchman's debt to Heidegger through Dreyfus and Winograd and Flores. It notes the second edition's detour through Latour, and it ends by comparing design and use with writing and reading: neither designer nor author controls how the artifact is used.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the operationalization workshop, this ingest supplies the claim its sibling secondary reading could not establish. [Dittrich's rereading of Suchman](./jan-dittrich-rereading-suchman-plans-actions.ingest.md) gives the edition and page anchor, but by its own Limitations it cannot establish "plans as resources for action". Duguid states that claim directly and rejects the "alternative to planning" misreading. The two **compare with** each other on what the book claims about plans; together they still stand in for the uncaptured book.

On execution, the source is **evidence for** and a qualification of [the two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md). Departing from the plan is normal operation, which agrees with that note's expected fallback. Orr's case, as Duguid relays it, adds a condition: recurrence can drive promotion only if the fallback is visible. Conformity pressure hides both the gap and the improvised handling. The same case is a human instance of [a goal-holding interpreter failing soft](../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md). The technicians absorb an inadequate procedure through unrecorded workarounds while the record shows the procedure followed. The note's mechanism is about LLM runtimes; the transfer is analogy until a shared mechanism is shown.

On where the plan–action gap comes from, the source **compares with** [agentic systems interpret underspecified instructions](../theory/agentic-systems-interpret-underspecified-instructions.md). The note places the gap in the instruction's semantic underspecification. Suchman, as relayed here, places it in a changing material and social context that more specification cannot remove. The photocopier instruction regress illustrates that limit. The KB term for this relativity is [actionable methodology](../theory/definitions/actionable-methodology.md): whether a methodology can guide action depends on operator, operations, target and setting.

The Moore's Law frame **compares with** [codification and relaxing navigate the bitter lesson boundary](../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) and [the bitter lesson selects against unearned reach](../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md). The shared axis is whether a limitation can be identified as compute-curable before scale tests it. The first note says it cannot. Duguid poses the same identification problem from the critic's side, but in 2012 he asserted that natural-language failures were principled, and later LLM progress partly tests that example. The Heideggerian premise he relays ("implicit assumptions cannot all be made explicit") **compares with** [Naur's human-only conclusion](../theory/naur-equates-machine-execution-with-formulated-criteria.md). Both lines of thought need an extra premise to move from inexplicit practical understanding to human-only competence. Finally, the routinization case **compares with** [Argyris on organizational learning and MIS](./argyris-organizational-learning-and-mis-1977.ingest.md), where tighter control induces ritual compliance, and with [Norman's account of silent autopilot compensation](./norman-problem-of-automation-inappropriate-feedback.ingest.md). The shared axis is hidden compensation that corrupts the evidence of how work is done.

## Extractable Value

1. **Plans as interpreted resources, not controllers** -- for the workshop, this is the clearest available statement of Suchman's position. A device executes a preordained plan; a human uses the plan as one resource, interpreted in context. Operationalizing knowledge for an executor therefore has two targets: a plan to be executed, or a resource to be interpreted. Which one applies depends on whether the executor can interpret. This supports separating operationalization (fitting knowledge to a task and executor) from automation (removing the interpreting executor). It is secondhand: claims about Suchman's own wording still need the book. [quick-win]
2. **Conformity pressure hides fallback and its lessons** -- Orr's technicians appeared to follow repair instructions while improvising around their inadequacy. Duguid names two losses: the plan's inadequacy is concealed, and the improvisation's insight is never harvested. This qualifies the KB's recurrence-driven promotion in the two-layer execution note: an executor held to apparent conformity suppresses the signals that promotion needs. The KB states the LLM-runtime mechanism (fail-soft workarounds) but not this control-pressure cause. Orr's case reaches the KB third-hand here. [experiment]
3. **Taylor versus Babbage as two framings of function-level automation** -- Duguid contrasts Babbage's division of labour between people and machines (complementarity) with Taylor's decomposition of work into routines coordinated by a plan, with interpretation replaced by obedience. He traces AI's assumptions to Taylor. This gives the workshop a named historical contrast between automating functions alongside interpreting people and replacing interpretation inside the plan. The essay asserts the lineage without argument. [just-a-reference]
4. **Instruction regress** -- Xerox's first response to unusable machines was more detailed instructions, which overwhelmed users. Someone reportedly proposed a second set of instructions to explain the first. This is a compact case of added specification failing to close a context-driven gap. It suits the underspecification note as an illustration, not as evidence. [quick-win]
5. **Principled versus practical limits under scaling** -- "Moore's Law ... often allowed principled objections to appear as merely practical ones." This is the critic's side of the bitter-lesson identification problem. The useful part is the distinction, not Duguid's natural-language example, which later LLM progress has partly overtaken. [just-a-reference]
6. **Heideggerian lineage of the critique** -- Dreyfus, Winograd and Flores, and Suchman share premises such as "implicit assumptions cannot all be made explicit" and breakdown and repair as a way of surfacing unseen assumptions. The KB has no artifact on this lineage. Duguid points to Winograd and Flores (1986) as the primary statement if the workshop needs it. [deep-dive]

## Limitations (our opinion)

This is a secondary, sympathetic reading by a member of Suchman's own PARC circle. It relays her claims rather than quoting them at length. Only a few short phrases ("discursive tools", "durable dissymmetry among human and nonhuman actors", and the 2007 p. 270 passage) are attributed to her directly. Any claim that Suchman said X still needs the book; this essay establishes only that a well-placed reader reads her that way.

The routinization argument rests on Orr (1996) relayed in a few sentences. Duguid gives no frequency, no account of when conformity pressure does or does not suppress improvisation, and no counter-case. The parenthetical "All plans ... are inadequate, but some are more inadequate than others" admits degrees but gives no criterion for them. The reader cannot use it to tell when a plan is good enough to execute without interpretation. The case therefore supports a mechanism hypothesis, not a general law. The Haynes checklist ingest shows that rigid procedures sometimes improve outcomes.

The principled-versus-practical distinction is asserted, not operationalized. Duguid offers no test for telling the two apart in advance, and his own example (natural-language processing) has since moved substantially under scale. This does not refute the distinction, but it shows how easily a principled classification can be wrong. It should be read alongside the KB's claim that the boundary cannot be identified before scale tests it.

The human-versus-machine framing assumes 1980s rule-following machines. Suchman's contrast is between devices that execute preordained plans and humans who interpret them. LLM agents interpret natural-language plans in context, so they do not fall cleanly on either side. The essay cannot say which of Suchman's conclusions survive for such executors. The Taylor, Babbage and Heidegger lineage claims are brief intellectual-history assertions and need their own sources.

## Recommended Next Action

In the operationalization workshop, add a short entry pairing this ingest with Dittrich's on "plans as executed programs versus plans as interpreted resources". Use it to test one question: does operationalizing knowledge for an executor that can interpret (human or LLM) produce a resource rather than a program, so that automation, which removes the interpreter, is a separate step? Cite this ingest as secondary evidence and flag Orr's routinization case as the candidate condition under which interpreted fallback becomes invisible.
