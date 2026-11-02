# Tarski audit: result and limits for the import assessment

Received 2026-11-02 to discharge the primary-source audit requested by [candidate library correction 2](./import-assessment.md#candidate-library-corrections). The useful result is a narrower truth-language argument, not an impossibility theorem about ordinary-language interpretation or execution. This records the audit's delivered conclusion and the integrated library corrections; it does not adopt an institutional construction.

Provenance: the originating audit thread is retained in Git commit `c2da14dc120aef3d79309fa91e1a8513540adcc7`. The retained source quotes linked below are the support for this handoff; no live pointer to the originating workshop is needed.

## Result and library destinations

The blanket grouping of Tarski, Gödel and halting-style results cannot by itself establish a limit for natural language as a whole. The Tarski material supports distinguishing a language from the metalanguage used to define its truth predicate, under the assumptions of that truth treatment. It does not turn precise meaning into a general truth-decision procedure.

In [Tarski 1944](../../sources/tarski-semantic-conception-of-truth.ingest.md), sections 6 and 8, the precise truth-definition problem requires exactly specified structure. The antinomy uses a language containing names of its expressions and its own truth predicate, permitting all sentences determining that predicate's adequate use to be asserted, together with ordinary logic. A conclusion using this argument must carry those assumptions rather than attribute inconsistency to natural language without them.

[Tarski 1969](../../sources/tarski-truth-and-proof.ingest.md), page 69, explains the richer metalanguage as a way to block reconstruction of the liar in that truth-definition setting. The [encyclopedia entry on the liar](../../sources/iep-liar-paradox.ingest.md) explicitly reports disagreement over the relationship between formal-language and natural-language solutions, and presents truth-value gaps as outside the cited undefinability theorem's scope. These sources do not license an impossibility independent of the chosen logic and truth assumptions.

Library destinations for the narrowed paragraphs are:

- [Agentic systems interpret underspecified instructions](../../theory/agentic-systems-interpret-underspecified-instructions.md).
- [Traditional software can bracket executor conformance](../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md).

Both library paragraphs now carry the narrower argument. Parent integration checked them against the retained quotes and corrected an overbroad attribution about formalized-language fragments after independent review. Delivery does not establish any broader institutional construction.

## Two limits that must travel with the result

1. **The consistency claim about natural language stays hedged.** Tarski 1944, section 8, says the consistency question has no exact meaning for everyday language because its structure is not exactly specified. The encyclopedia entry says reflection on the liar suggests English is either not semantically closed or inconsistent, while explicitly questioning whether “inconsistent” applies to a language with vague structure. It raises, but does not resolve, whether English is semantically closed. Do not turn this into an established theorem that English is inconsistent or unformalizable.
2. **The audit establishes no execution restriction.** The quoted arguments concern truth predicates and the liar. They do not prohibit writing an interpreter in its own language, encoding semantic rules, or executing those rules. A governing reference can be external in authority without being expressed in a different language. No inference from truth-definition limits to an inability to interpret or execute instructions is delivered here.

## Disposition for continued work

The audit portion of correction 2 and its two library revisions are delivered. The broader import still needs its own worked examples and counterexamples. Keep semantic definition, decision procedures, interpreter conformance and contextual dependence separate, as the [import assessment](./import-assessment.md) already requires. If the institutional construction adds no diagnosis or permitted operation, the useful narrower correction can stand without it.
