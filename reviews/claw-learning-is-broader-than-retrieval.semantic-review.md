=== SEMANTIC REVIEW: claw-learning-is-broader-than-retrieval.md ===

Claims identified: 14

**Claims extracted:**

1. [The narrow framing] The KB learning loop note "frames the KB's value as 'question-answering capacity'"
2. [The narrow framing] Commonplace is a Claw: "an AI-assisted system that accumulates context and evolves with use"
3. [What a Claw actually does] Four concrete action modes enumerated: classification, communication, planning, pattern recognition
4. [What a Claw actually does] "The common thread isn't question-answering — it's contextual competence"
5. [What a Claw actually does] You *can* frame all four as answering a question "but that stretches the concept past usefulness"
6. [What counts as knowledge] Four action-oriented knowledge types: preferences, procedures, judgment precedents, voice and style
7. [What counts as knowledge] Koylanai's Personal Brain OS "already stores all four" knowledge types
8. [Document types] Current document classification "is oriented around structural properties of reference knowledge"
9. [Document types] "Preferences, procedures, and judgment precedents don't fit neatly into these categories"
10. [Mutation types] Boiling cauldron mutations are "all oriented around making knowledge more findable and better structured"
11. [Mutation types] Three new mutation types proposed: codify preference, capture procedure, consolidate precedents
12. [The retrieval frame isn't wrong] "retrieval learning is one layer of a larger system"
13. [Open Questions] The three-space memory model maps: "Knowledge space maps to retrieval, operational space maps to procedures, self space maps to preferences and voice"
14. [Open Questions] Predicted flat-memory failure modes "are exactly what you'd expect when action-oriented knowledge types are forced into a retrieval-oriented structure"

---

WARN:
- [Completeness] The four action modes (classification, communication, planning, pattern recognition) are presented as the concrete instances of "what a Claw actually does," but **execution/implementation** — actually carrying out multi-step tasks (writing code, editing files, running scripts) — is arguably the most common agentic action and does not map cleanly to any of the four. Classification is routing, communication is drafting, planning is decomposition, pattern recognition is matching — but none covers "do the thing." The note's own framing ("A Claw acts on behalf of the user") implies execution as the central activity, yet the enumeration lists only cognitive pre-stages of execution. This omission is significant because execution capacity is also learnable (tool selection strategies, error recovery patterns) and would need its own knowledge types.

- [Completeness] The four action-oriented knowledge types (preferences, procedures, judgment precedents, voice and style) omit **domain models / ontologies** — structured representations of entities and relationships specific to the user's domain. These are not retrieval-oriented facts and not preferences; they are action-enabling because they let the agent reason about domain structure (e.g., knowing that "a PR belongs to a branch belongs to a repo" enables correct git operations). The note frames the gap as "retrieval-oriented KB stores facts and relationships" vs. "action-oriented KB also needs [four types]," but domain models sit uncomfortably between these categories — they are structural knowledge that enables action without being preferences, procedures, precedents, or voice.

- [Grounding — scope mismatch] The note claims Koylanai's Personal Brain OS "already stores all four" action-oriented knowledge types: "voice guides and brand files for style, AGENT.md decision tables for procedures, decisions.jsonl and failures.jsonl for judgment precedents, and values/goals YAML for preferences." The ingest file (koylanai-personal-brain-os.ingest.md) classifies itself as a "practitioner-report" with "self-report only" evidence, notes that "every architectural detail in this report is filtered through the author's own description," and recommends treating it as "anecdotal practitioner evidence." The note here presents the mapping as straightforwardly established fact ("already stores all four") without hedging, which overstates what the source supports. The ingest note specifically warns against promoting this source beyond anecdotal evidence.

- [Grounding — domain coverage] The note claims the boiling cauldron mutations are "all oriented around making knowledge more findable and better structured." The source note (automating-kb-learning-is-an-open-problem.md) lists seven mutations: extract, split, synthesise, relink, reformulate, regroup, retire. Of these, "synthesise" creates new knowledge that neither source note contains alone — this is generative, not findability-oriented. "Retire" removes artifacts that have outlived usefulness — this is maintenance, not structure improvement. Characterizing the full set as findability/structure-oriented flattens real variation among the mutations, which weakens the contrast the note is trying to draw between retrieval-oriented and action-oriented mutation types.

INFO:
- [Completeness] The note proposes three new mutation types (codify preference, capture procedure, consolidate precedents) as the action-oriented counterparts to the boiling cauldron's retrieval-oriented mutations. But the boiling cauldron has seven mutations while only three action-oriented ones are proposed. Are there action-oriented analogues for split, relink, reformulate, regroup, and retire? For example: "split a preference that covers two domains," "relink procedures that share steps," "retire a precedent superseded by a policy change." The asymmetry may be intentional (these are examples, not an exhaustive list) but the note doesn't signal this — readers could mistake it for a complete proposed set.

- [Internal consistency] The note defines the broader learning target as "contextual competence: the ability to act appropriately given accumulated knowledge about the domain, the user, and the project." But the Open Questions section maps the three-space memory model as "Knowledge space maps to retrieval, operational space maps to procedures, self space maps to preferences and voice." This mapping omits "the domain" and "the project" from the contextual competence definition — domain knowledge would sit in the knowledge space (which the note has characterized as retrieval-oriented), and project knowledge cuts across all three spaces. The mapping is suggestive rather than rigorous, which the question-mark framing ("Does the three-space model help here?") appropriately signals, but the subsequent sentence ("Maybe each space has its own learning dynamics") treats the mapping as more settled than the question suggests.

- [Grounding — vocabulary] The note's definition of Claw as "an AI-assisted system that accumulates context and evolves with use" is a broader interpretation than the source (simon-willison-karpathy-claws.md), which defines Claws as "OpenClaw-like agent systems — AI agents that generally run on personal hardware, communicate via messaging protocols and can both act on direct instructions and schedule tasks." The source emphasizes infrastructure characteristics (personal hardware, messaging protocols, scheduling) while the note abstracts to an epistemological framing (accumulates context, evolves). This is a reasonable inference given the note's purpose, but readers may assume the source directly supports the broader definition.

- [Internal consistency] The note says "The retrieval frame isn't wrong, just partial" and "This note doesn't invalidate [the KB learning loop note]." But the opening section's claim that question-answering "stretches the concept past usefulness" as a framing for Claw action modes is a stronger dismissal than "partial." If all four modes can technically be framed as question-answering (as the note concedes), then the retrieval frame is not just partial but a differently-granulated lens — the note's argument is about usefulness of framing, not logical inadequacy. The tension between "you can do it but it's useless" and "it's not wrong, just partial" could be sharpened.

PASS:
- [Internal consistency] The note's core argument — that retrieval is a subset of action capacity — is internally consistent throughout. The progression from narrow framing to broader framing to implications to open questions follows without contradictions.
- [Grounding — automating-kb-learning-is-an-open-problem.md] The attribution of the "question-answering capacity" framing to the KB learning loop note is accurate. That note explicitly states: "A knowledge base exists to answer questions about the project. This defines value for every artifact."
- [Grounding — document-classification.md] The claim that current document types are "oriented around structural properties of reference knowledge" aligns with the source, which defines types by structural tests (frontmatter presence, section requirements, link density) rather than by action-enablement properties.
- [Grounding — constraining.md] The claim that constraining "frames system-level adaptation as artifact accumulation" is a reasonable reading of the constraining note, which describes a constrain/relax cycle where each step produces or modifies artifacts. The note correctly identifies that action-oriented artifacts would be different types (preference codifications, procedure captures) rather than the note/link mutations constraining currently covers.
- [Completeness — knowledge types vs. Koylanai] Setting aside the hedging issue (reported as WARN above), the four-way mapping to Koylanai's system (voice guides = style, AGENT.md = procedures, decisions/failures logs = precedents, values/goals YAML = preferences) is structurally sound — each claimed type does have a plausible corresponding artifact in the described system.

Overall: 4 warnings, 4 info
===
