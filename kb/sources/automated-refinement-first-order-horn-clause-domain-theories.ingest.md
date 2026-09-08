---
description: "FORTE revises executable Horn-clause theories from examples, separating proof-guided repair from theory-guided software modification and exposing language and evaluation limits."
source: https://www.cs.utexas.edu/~ml/papers/forte-mlj-94.pdf
captured: "2026-09-08"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 97e363997cf37e7fe662022c038b3236ac5155a5cb7e6fbe9988748015f5603e
ingested: "2026-09-08"
occasion: "What objects, operations, evaluation criteria, and representation choices define theory refinement? Which are essential to the concept, which belong to particular algorithms, and how does its application to program debugging compare with refinement of theories used to guide software modification?"
type: kb/sources/types/ingest-report.md
domains: [theory-refinement, inductive-logic-programming, program-debugging, knowledge-representation]
---

# Ingest: Automated Refinement of First-Order Horn-Clause Domain Theories

## Classification

A scientific paper presenting an implemented learning algorithm, its operators, comparative experiments, and applications to program debugging and qualitative modelling. Bradley L. Richards and Raymond J. Mooney report this work in *Machine Learning* 19, 95–131 (1995); the captured manuscript identifies affiliations at EPFL and the University of Texas at Austin. Algorithm descriptions and experimental conditions provide the main author signal.

## Summary

[Richards and Mooney](https://www.cs.utexas.edu/~ml/papers/forte-mlj-94.pdf) present FORTE, which revises an imperfect function-free first-order Horn-clause theory using labelled instances and associated facts. Failed proofs of positive instances and successful proofs of negative instances identify possible repair locations. Generalization and specialization operators propose changes; a hill-climbing loop selects the largest training-accuracy improvement, preferring smaller theories on ties. Relational path finding adds connected groups of antecedents to escape plateaus that defeat single-literal search. Family-domain experiments compare revision with induction, vary initial corruption, and ablate path finding. Applications include repairing all 23 collected incorrect student programs across three simple Prolog tasks, repairing limited faults in a decision-tree learner, and inducing or revising qualitative physical models. The paper is useful for understanding how executable theories can be repaired automatically and where recursion, representation, and supplied background knowledge constrain that achievement.

## Quotes

No source quotes have been retained yet.

## Connections Found

FORTE is a technical basis for the classical refinement mechanism in [the theory-refinement lineage note](../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md): explicit fallible rules shape proof diagnosis and are themselves revised against examples. It also provides a concrete comparison for [theory-mediated learning](../notes/definitions/theory-mediated-learning.md). In its debugging application the revised theory is the program; this differs from revising a theory of purposes and organization that guides edits to a distinct program. Program repair therefore broadens the lineage beyond external classification without establishing reflective self-modification. The [fixed-decomposition analysis](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) limits the experimental reading: FORTE varies clauses and, in its path-finding ablation, an operator capability; it does not learn its representation, verifier, or protected background predicates.

## Extractable Value

1. **Separate the refinement task from FORTE's realization.** Sections 1–2 identify the organizing task as improving an existing fallible theory from empirical cases, preserving useful prior knowledge while correcting errors. FORTE realizes it with function-free definite clauses, positive and negative predicate instances, instance-specific facts, and SLD-resolution. Horn clauses, greedy search, and this exact label format should not become universal requirements in the KB's definition of theory refinement. [quick-win]

2. **Specify both semantic direction and concrete operations.** Specialization excludes erroneous consequences; generalization admits missing correct ones. FORTE composes rule addition/deletion and antecedent addition/deletion into richer proposals, including inverse-resolution operations and relational path finding. The primitive edit basis describes the symbolic search space; the richer operators address how useful changes become reachable under limited search. Their necessity is algorithm-relative. [quick-win]

3. **Keep three evaluation questions distinct.** Correctness on supplied instances means deriving every positive and no negative from the theory plus each instance's facts. Search ranks actual training-accuracy improvement, with smaller theories breaking ties; small edits and few operations approximate minimal revision without guaranteeing it. Held-out accuracy tests generalization in the family experiments, whereas the programming application seeks completely correct programs. None of these criteria alone establishes that a theory explains software responsibilities or supports coherent future modification. [quick-win]

4. **Use debugging as a precise comparison, not an identity of theory objects.** FORTE directly changes executable clauses to repair behavior. A retained theory used to guide software modification instead needs a demonstrated path from its claims through diagnosis or proposals into separate software changes, followed by evidence that can revise those claims. FORTE's preservation of an unusual student recursion scheme shows structural preservation in one repair; it does not test understanding of why that organization fits new requirements. [deep-dive]

5. **Distinguish diagnostic evidence from selection scores.** Proof annotations expose failing antecedents and antecedents that supplied problematic variable bindings; successful negative proofs expose clauses to specialize. These traces localize candidate changes before a whole-training-set score selects among them. This is a reusable mechanism for addressing knowledge defects, but the experiments do not isolate the contribution of diagnostic richness. [just-a-reference]

6. **Record where a successful repair can change a component's meaning.** In Section 6.3, repairing list reversal produces an append predicate adequate for the calls that reversal makes, but not a general-purpose append. Top-level behavioral success can therefore conceal loss of an intended reusable contract. A KB drawing lessons for software modification should distinguish fitting observed callers from preserving a component's wider responsibility. [quick-win]

## Limitations (our opinion)

The family experiments start with a designed relational domain and random corruptions of a known correct theory. They support benefits from retained approximate knowledge in that setting, not an unrestricted preference for repair: with 100 training examples and eight introduced errors, induction performs better. The reported student programs cover three simple tasks that FORTE could already synthesize. The larger debugging example exposes only 31 lines to revision while protecting much of its supporting program. No implementation was inspected or executed for this ingest.

The effective update space is explicit. The learner receives examples, associated facts, current clauses, and proof traces; recursive repair additionally uses positive examples as temporary extensional definitions. Its operators can compose relational and recursive clauses over available predicates, including new variables and multi-antecedent paths. However, predicate invention, negation as failure, and probabilistic theories are unavailable. Translators, language bias, the operator library, resource limits, optional consistency verifier, and protected fundamental domain theory remain supplied. Introducing a missing qualitative-model variable is thus possible without inventing a new predicate vocabulary. Following the [fixed-decomposition distinction](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within these conditions does not validate the fixed choices against alternatives. The path-finding ablation identifies the contribution of that operator capability in the tested domains.

Recursive repair depends on sufficiently complete small examples. Deriving examples for lower-level predicates can fail or distort their meanings when callers are incorrect, insufficiently instantiated, or narrow in their use. Hill climbing can stop at a local maximum; consistency with training instances and global minimality are not guaranteed. The positive-only qualitative-model mode adds a supplied preference for a maximally constrained single-clause theory, so its results should not be read as evidence that positive observations alone identify arbitrary physical theories.

## Recommended Next Action

Revise [the theory-refinement lineage note](../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) to add a bounded comparison of executable-theory repair and refinement of a theory guiding separate software changes, using FORTE's debugging results and component-contract failure to state what transfers and what remains untested.
