# Follow-up library changes

Changes outside the two definitions that this workshop has found necessary, and the migration of the retired phrase. Part of the [workshop](./README.md). None is authorized under this commission; each needs its own library revision. The definitions themselves are in [representational form](./representational-form-definition.md) and [codification](./codification-definition.md).

## Vocabulary collision ledger

- **operational.** The row loses its codification sense when the fixed phrase is retired. It keeps the lineage sense, the external senses, and the workshop-local sense. Its guidance changes from "write the fixed phrase whole" to "say that the artifact's language has a formal semantics or is close to one, and link symbolic form for the gloss".
- **self-repair.** In the KB, an LLM regenerating code until a check passes. In the [repair ingest](../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md), repair by the speaker of the trouble source. Not recorded in the ledger.
- **semantic closure.** In the [Tarski thread](./tarski-thread.md), a language that contains its own semantic terms. In the KB's Pattee ingests, an unrelated biological sense. Not recorded in the ledger.
- **grounding.** In the KB, source support for claims (`cp-skill-ground`, the `claims-and-grounding` tag, ADRs 079 and 082). In Clark and Brennan, establishing mutual understanding in conversation. Not recorded in the ledger or in `AGENTS.md`. The [evidence ledger](./sources.md) qualifies the term at first use.

## Migration of the retired phrase

"Unique operational semantics" is retired with the formalizability conjecture behind it. In [constraining](../../theory/definitions/constraining.md), "where the artifact has a unique operational semantics" becomes "where the artifact's language has a formal semantics or is close to one", in the misuse case and the footer label. Other library uses of the phrase migrate to the same wording, and each use should be checked for reliance on the conjecture rather than only replaced. The two source ingests that gloss the phrase keep it as a historical reference to the retired term. Promotion requires coordinated revisions of representational form, codification, constraining, the collision ledger, and the other library uses; this workshop authorizes none of them.

## Representational form beyond the two definitions

The [proposed form definition](./representational-form-definition.md) narrows the misuse case about a fixed prompt and model to repeatability, rewrites the inspection rule around the opaque modifier, and states the consequence that pinning and adopting a model codifies the instructions it reads. [Opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md) names one source of opacity, the artifact's scale; the workshop adds two more. The reference's form puts opacity at the smallest unit for a frozen model package. Deliberate obfuscation puts it at small scale by construction. The two obfuscation ingests, [Barak and co-authors](../../sources/on-the-impossibility-of-obfuscating-programs.ingest.md) and [Jain, Lin and Sahai](../../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md), give the note a definition of the goal, a proof that its strong form is impossible in general, with the reason that reading a program can strictly exceed running it, and the weaker provable notion that hides only which equivalent program was used. Both ingests propose qualifying links from the note, the form definition's misuse case and inspection rule, and the note on inspectable artifacts; the connection reports list them. The note's title claim, that opacity is a scale threshold, then narrows to one source among three, and its "practically opaque" reading becomes the definition: opaque relative to a behavior or change of interest and an acceptable inspection cost, with the reference's form stated as a gap between the path on which the reference is readable and the path on which the question is asked. The note should take the other two sources, and the form definition's misuse case against calling weights "opaque" as if opacity were the form stays as it is, since the modifier is an inspection property.

## The impossibility paragraph

[Agentic systems interpret underspecified instructions](../../theory/agentic-systems-interpret-underspecified-instructions.md) appeals to "Tarski/Gödel/halting-style impossibility results" in one sentence. The [Tarski ingest](../../sources/tarski-semantic-conception-of-truth.ingest.md) and the [Tarski thread](./tarski-thread.md) show what can be drawn: the hierarchy of languages and the absence of a general truth test. What cannot: a theorem about natural language as a whole, an impossibility independent of classical logic and full disquotation, or anything about execution. Rewrite the paragraph to the narrower claim and cite the three Tarski-related ingests, the [1969 article](../../sources/tarski-truth-and-proof.ingest.md) and the [encyclopedia entry](../../sources/iep-liar-paradox.ingest.md) included, with their passages grounded. [Traditional software can bracket executor conformance](../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) repeats the same wording and takes the same revision. The 1944 ingest should link the encyclopedia entry, since its Kripke and paraconsistency remarks are currently unsourced. The [institution-theory workshop](../institution-theory-import/import-assessment.md) asked for this audit.

## Links from theory notes to the ingests

The connection reports propose `evidenced-by` links, each worded as qualifying rather than corroborating:

- [meaning as coordination](../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) to the clarification and repair ingests, and to Clark and Brennan once ingested. The clarification paper limits the note's "other speakers as checker" claim to a minority of requests.
- [conversation vs prompt refinement](../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) to the repair ingest: most self-repair finishes inside the same turn, which qualifies "can only append corrections".
- The two new ingests on repair and clarification should link each other with `compares-with`.

## Routed from the probe answer

[Astra's answer](./probe-response-2026-11-01-astra.md) to the probe points at the C11 committee draft, WG14 N1570, sections 3.4.1 to 3.4.4, for the categories of unspecified, implementation-defined and undefined behavior. The account's section on what the reference leaves open uses those categories without a retained quote; an ingest of those sections would ground it, and the answer's split between permitted freedom, several actions satisfying one acceptance condition, and unresolved interpretation, uncertainty about which condition governs, is a cleaner wording for the section than the account's. The answer's six interpretation statuses, its ambiguity exception with the undecidability of task-relevant ambiguity for expressive acceptance conditions, and its assessment design belong to the [ideal-interpreter workshop](../ideal-interpreter/README.md), which owns the interpreter device; this workshop takes none of it.

## A possible new note

The connection passes suggest one claim the theory collection does not state: an agent handoff behaves like a delayed medium, so the cost of confirming understanding shifts to writing the prompt up front. Not written; revisit if the commitment account survives review.
