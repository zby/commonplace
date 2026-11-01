# Follow-up library changes

Changes outside the two definitions that this workshop has found necessary. Part of the [workshop](./README.md). None is authorized under this commission; each needs its own library revision. The definitions themselves are in [candidate definitions](./candidate-definitions.md).

## Vocabulary collision ledger

- **operational.** The row loses its codification sense when the fixed phrase is retired; see the ledger section of [candidate definitions](./candidate-definitions.md).
- **self-repair.** In the KB, an LLM regenerating code until a check passes. In the [repair ingest](../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md), repair by the speaker of the trouble source. Not recorded in the ledger.
- **semantic closure.** In the [Tarski thread](./tarski-thread.md), a language that contains its own semantic terms. In the KB's Pattee ingests, an unrelated biological sense. Not recorded in the ledger.
- **grounding.** In the KB, source support for claims (`cp-skill-ground`, the `claims-and-grounding` tag, ADRs 079 and 082). In Clark and Brennan, establishing mutual understanding in conversation. Not recorded in the ledger or in `AGENTS.md`. The [evidence ledger](./sources.md) qualifies the term at first use.

## The impossibility paragraph

[Agentic systems interpret underspecified instructions](../../theory/agentic-systems-interpret-underspecified-instructions.md) appeals to "Tarski/Gödel/halting-style impossibility results" in one sentence. The [Tarski ingest](../../sources/tarski-semantic-conception-of-truth.ingest.md) and the [Tarski thread](./tarski-thread.md) show what can be drawn: the hierarchy of languages and the absence of a general truth test. What cannot: a theorem about natural language as a whole, an impossibility independent of classical logic and full disquotation, or anything about execution. Rewrite the paragraph to the narrower claim and cite the three Tarski-related ingests, the [1969 article](../../sources/tarski-truth-and-proof.ingest.md) and the [encyclopedia entry](../../sources/iep-liar-paradox.ingest.md) included, with their passages grounded. [Traditional software can bracket executor conformance](../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) repeats the same wording and takes the same revision. The 1944 ingest should link the encyclopedia entry, since its Kripke and paraconsistency remarks are currently unsourced. The [institution-theory workshop](../institution-theory-import/import-assessment.md) asked for this audit.

## Links from theory notes to the ingests

The connection reports propose `evidenced-by` links, each worded as qualifying rather than corroborating:

- [meaning as coordination](../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) to the clarification and repair ingests, and to Clark and Brennan once ingested. The clarification paper limits the note's "other speakers as checker" claim to a minority of requests.
- [conversation vs prompt refinement](../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) to the repair ingest: most self-repair finishes inside the same turn, which qualifies "can only append corrections".
- The two new ingests on repair and clarification should link each other with `compares-with`.

## A possible new note

The connection passes suggest one claim the theory collection does not state: an agent handoff behaves like a delayed medium, so the cost of confirming understanding shifts to writing the prompt up front. Not written; revisit if the commitment account survives review.
