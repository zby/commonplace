<!-- REVIEW-METADATA
note-path: kb/notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md
last-full-review-note-sha: 50a3c731a69f624a56bc656407bf2a971adf4257
last-full-review-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-full-review-at: 2026-03-24T12:00:00+01:00
last-accepted-note-sha: 50a3c731a69f624a56bc656407bf2a971adf4257
last-accepted-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-accepted-at: 2026-03-24T12:00:00+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md ===

Claims identified: 18

**Claims extracted:**

1. [The narrow framing] The KB learning loop note "frames KB value as 'question-answering capacity'"
2. [The narrow framing] A Claw is "an AI-assisted system that accumulates context and evolves with use"
3. [The narrow framing] A Claw "does more than look things up"
4. [What a Claw actually does] Five action modes enumerated: execution, classification, communication, planning, pattern recognition
5. [What a Claw actually does] "The common thread is contextual competence: the ability to act appropriately given accumulated knowledge about the domain, the user, and the project"
6. [What a Claw actually does] Framing each mode as answering a question "stretches the concept past usefulness"
7. [What changes — Knowledge types] A retrieval-oriented KB "stores facts and relationships"; an action-oriented KB also needs preferences, procedures, judgment precedents, voice and style, and domain models
8. [What changes — Knowledge types] The knowledge-types list "is illustrative, not exhaustive"
9. [What changes — Knowledge types] Koylanai's Personal Brain OS "appears to store several of these" knowledge types — "anecdotal evidence, but it suggests that practitioner-built Claws converge on action-oriented knowledge types even without a theoretical framework"
10. [What changes — Knowledge types] Current document classification "is oriented around structural properties of reference knowledge"
11. [What changes — Mutations] The boiling cauldron mutations are "mostly oriented around findability and structure, though synthesise is generative (creates new knowledge) and retire is maintenance"
12. [What changes — Mutations] Three new mutation types proposed: codify preference, capture procedure, consolidate precedents
13. [What changes — Evaluation] "Did it act appropriately?" is harder to measure than "Did it answer correctly?"
14. [What changes — Evaluation] "The usage that matters isn't just queries and failed retrievals — it's the full range of agentic actions"
15. [The retrieval frame isn't wrong, just partial] "retrieval learning is one layer of a larger system"
16. [The retrieval frame] The boiling cauldron loop structure transfers, but with different mutation types
17. [Open Questions] The three-space memory model may help: "Knowledge space maps to retrieval, operational space maps to procedures, self space maps to preferences and voice — suggesting each space might have its own learning dynamics"
18. [Open Questions] Predicted flat-memory failure modes "are exactly what you'd expect when action-oriented knowledge types are forced into a retrieval-oriented structure"

---

WARN:
- [Completeness — action modes] The five action modes (execution, classification, communication, planning, pattern recognition) are presented as "at least these modes" that benefit from accumulated context, acknowledging non-exhaustiveness. However, the note later treats them as the operative set when it says "the full range of agentic actions: classifications made, communications drafted, plans executed" — dropping pattern recognition and execution from the summary list. This partial recapitulation could lead readers to treat the later three-item list as the definitive set. More importantly, **monitoring/alerting** — observing ongoing state and raising signals when thresholds or conditions are met — is a common agentic action mode that does not cleanly reduce to any of the five. The KB could hold alert criteria, escalation policies, and baseline expectations. This is not pattern recognition (which surfaces precedent) but sustained observation against accumulated criteria.

- [Grounding — domain coverage] The note cites the constraining note in Open Questions: "Constraining frames system-level adaptation as artifact accumulation. The action layer's learning loop would need the same framework but applied to different artifact types." The constraining note defines constraining as "narrowing the interpretation space" that an underspecified spec admits — it is about reducing ambiguity, not about artifact accumulation per se. Artifact accumulation is an *effect* of constraining, but the constraining note's framework is about the interpretation-space dimension, not an inventory of artifact types. The note's reframing of constraining as "artifact accumulation" elides the core mechanism (interpretation-space narrowing) and substitutes an observable consequence.

- [Grounding — scope mismatch on mutations] The note characterizes the boiling cauldron mutations as "mostly oriented around findability and structure, though synthesise is generative (creates new knowledge) and retire is maintenance." The source note (automating-kb-learning-is-an-open-problem.md) explicitly categorizes mutations on two axes — generality and codifiability — and describes a range from narrow-scope individual improvements through medium-scope connection changes to wide-scope system restructuring. The source's own framing is not "findability and structure" but "scope of impact on the system's organizing principles." The note's characterization, while acknowledging exceptions, still flattens the source's richer taxonomy to draw a cleaner contrast with action-oriented mutations.

- [Completeness — knowledge types vs. action modes] The note lists five action modes and five knowledge types, but the mapping between them is left implicit. Execution is said to draw on "operational knowledge," classification on "criteria and precedents," communication on "style, stance, history," planning on "operational memory," and pattern recognition on "the case library." Yet the five knowledge types are preferences, procedures, judgment precedents, voice and style, and domain models. Where does "operational knowledge" (execution) land? It appears to be a composite of procedures and domain models. Where does "the case library" (pattern recognition) land? It is close to judgment precedents but not identical. The lack of explicit mapping means the reader cannot verify whether the knowledge types are sufficient to support all five action modes.

INFO:
- [Completeness — mutation asymmetry] The note proposes three action-oriented mutations (codify preference, capture procedure, consolidate precedents) as counterparts to the boiling cauldron's seven retrieval-oriented mutations. This asymmetry is not flagged in the note. Are there action-oriented analogues for extract, split, relink, reformulate, regroup, and retire? The note may intentionally be illustrative rather than exhaustive here, but it does not say so for the mutations the way it does for knowledge types.

- [Internal consistency — action vs. retrieval boundary] The note argues that framing each action mode as question-answering "stretches the concept past usefulness." But the Evaluation section acknowledges that broadening from retrieval to action makes evaluation "harder still" — implying a continuum rather than a categorical difference. If the difference is one of degree (harder evaluation), the question-answering framing might be partial but not useless. The note's rhetorical stance is stronger than its analytical stance, creating a mild tension.

- [Grounding — Claw definition] The note defines a Claw as "an AI-assisted system that accumulates context and evolves with use," citing simon-willison-karpathy-claws.md. The source defines Claws as "OpenClaw-like agent systems — AI agents that generally run on personal hardware, communicate via messaging protocols and can both act on direct instructions and schedule tasks." The note's definition abstracts away the infrastructure characteristics to an epistemological framing. This is a reasonable interpretive move but readers may assume the source directly supports the broader definition.

- [Internal consistency — three-space mapping] The Open Questions section maps "Knowledge space maps to retrieval, operational space maps to procedures, self space maps to preferences and voice." The three-space source note maps operational space to "friction observations, methodology, session artifacts" — high-churn working artifacts — not to durable procedures. Procedures would more naturally sit in the knowledge space (semantic memory). The note's mapping reinterprets the three-space model's categories to fit its own knowledge-type taxonomy.

PASS:
- [Internal consistency — core argument] The note's central claim — that a Claw's learning loop must target action capacity, not just retrieval — is maintained consistently from opening to closing. The progression from narrow framing to broader framing to implications for knowledge types, mutations, and evaluation is logically coherent.
- [Grounding — automating-kb-learning-is-an-open-problem.md] The attribution of the "question-answering capacity" framing is accurate. The source note explicitly states: "A knowledge base exists to answer questions about the project."
- [Grounding — Koylanai hedging] The current version appropriately hedges the Koylanai reference: "appears to store several of these," "This is anecdotal evidence," "suggests that practitioner-built Claws converge."
- [Grounding — document-classification.md] The claim that current document types are "oriented around structural properties of reference knowledge" aligns with the source, which defines types by structural tests rather than action-enablement properties.
- [Internal consistency — "not wrong, just partial"] The note explicitly positions the retrieval frame as partial rather than incorrect, and identifies specific elements that transfer vs. what does not. This is internally coherent and avoids overstating the critique.
- [Completeness — knowledge types] The note explicitly marks its knowledge-types list as "illustrative, not exhaustive," which is an appropriate hedge. The inclusion of domain models closes a significant completeness gap.

Overall: 4 warnings, 4 info
===
