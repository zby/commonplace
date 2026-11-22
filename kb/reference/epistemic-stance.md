---
description: "The philosophical tradition Commonplace's assertions assume — Popperian: fallibilism, methodological rules as conventions, anti-essentialism, intersubjective testability — and what it does not inherit"
type: types/note.md
tags: []
---

# Epistemic stance

Commonplace adopts four commitments from the Popperian tradition. They shape
how the KB tests claims, chooses rules, defines terms and interprets instructions.

1. **Fallibilism.** Claims are conjectures. Observations never establish a
   universal statement. Corroboration is a survived attempt at refutation
   ([Popper, *Logic of Scientific Discovery*](../sources/popper-logic-of-scientific-discovery.ingest.md)).
   Applied in the [theory contract](../theory/COLLECTION.md) and
   [claim modality](./adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md).

2. **Methodological rules are conventions** (*Logic of Scientific Discovery*,
   §11). Commonplace adopts rules through ADRs, contracts, type specs and
   definitions. A counterexample can overturn a claim about what a rule
   achieves. It does not repeal the rule. To change the rule, propose an
   alternative and explain why its consequences would be preferable.

3. **Anti-essentialism** (*Open Society*, ch. 11; *Poverty of Historicism*,
   §10). A Commonplace definition assigns a name to what the definition
   describes; it does not claim to discover the term’s true meaning. See
   [verifiable document types](../theory/document-types-should-be-verifiable.md)
   and [taxonomies as defaults](../theory/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md).
   Commonplace takes the meaning of an instruction to be the reading that a
   designated reference set of interpreters converges on, under a stated rule
   for when two outputs count as the same answer; see
   [prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md).

4. **Objectivity is intersubjective testability** (*Logic of Scientific
   Discovery*, §8), and knowledge lives in artifacts
   ([Popper 1968](../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md)).
   Applied in the [theory builder](../theory/definitions/theory-builder.md).
   This commitment keeps point 3 from relativism. The reference set is
   chosen, but choosing it does not make its interpreters converge. Whether
   they converge is a fact, and a test can find that they do not.

## Judgment under uncertainty

A test can show what a rule achieved. Deciding whether to keep the rule
still calls for an [on-balance judgment](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md).
A validator may catch an omission the old search missed. That is a reason to
keep it, but it does not settle the choice. How often would readers otherwise
miss an entry? How much upkeep will maintainers face? Experience can narrow
those uncertainties. It cannot decide how much maintenance work a benefit to
readers is worth.

For the decision at hand, investigate an unknown when a plausible answer
could change the choice. A maintainer can give reasons to keep the validator
without claiming that its benefits have been shown to outweigh its costs.

## Limits of the declaration

Commonplace does not inherit the propensity interpretation of probability,
verisimilitude measures, or Popper's political writings beyond their
anti-essentialist argument.

*Open Society* and *Poverty of Historicism* are not ingested. Cite them
without quotes until they are.
