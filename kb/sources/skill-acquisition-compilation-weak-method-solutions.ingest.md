---
description: "Anderson's ACT account compiles goal-organized problem solving into use-specific productions; human transfer studies bound its relevance to retained agent procedures."
source: https://files.eric.ed.gov/fulltext/ED264257.pdf
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 262bcb90b0791f53a37d316e630caa403391d5f36470e1f34b821891ba76f7c3
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [skill-acquisition, knowledge-compilation, learning-theory]
learning_claims: true
---

# Ingest: Skill Acquisition: Compilation of Weak-Method Problem Solutions

## Classification

A scientific technical report combining an ACT learning model, a technical account of its GRAPES implementation, and summaries of human experiments on programming, text editing, transfer, and instruction. The captured work is technical report ONR-85-1, dated August 12, 1985; it is not assumed identical to a later journal version. Author John R. Anderson, of Carnegie-Mellon's psychology department, presents research from his own cognitive-modeling and tutoring program, including revisions to his earlier theory. [Primary source](https://files.eric.ed.gov/fulltext/ED264257.pdf).

## Summary

Anderson proposes that novices use general problem-solving methods, such as analogy and means–ends analysis, to interpret declarative knowledge and solve unfamiliar problems. Knowledge compilation then creates domain-specific condition–action rules: proceduralization builds relevant declarative information into a rule, while composition combines rules that achieve a goal. Practice also strengthens successfully used rules. Human studies report faster performance on frequently practiced combinations and little transfer between evaluating LISP expressions and generating them, despite shared underlying knowledge. Within the proposed ACT architecture, these findings support skill tied to a particular use of knowledge; they do not compare the architecture's goal hierarchy, production representation, or supplied general methods against alternative learning architectures. The report also revises automatic syntactic induction into strategic problem solving informed by semantic knowledge. Its value for Commonplace is a concrete historical account of how usable procedures can emerge from problem solving, with boundaries on transferring that account to fixed-model agents.

## Quotes

No source quotes have been retained yet.

## Connections Found

The report is a historical comparison for [the two-layer execution account](../notes/theory-and-methodology-form-a-two-layer-execution-system.md): general methods interpret knowledge, and successful goal-organized solutions produce specialized rules that avoid repeating part of that interpretation. The appendix makes this transformation concrete. The human practice and transfer findings are consistent with the proposed production analysis, but do not test Commonplace's coverage recognition, recurrence-based promotion, fallback, or staleness policies. This is ACT/GRAPES, an earlier account than the ACT-R manual currently used by that note.

It also sharpens [the distinction between retaining theory and acquiring its missing application procedures](../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md). A single declarative relation can support different procedures for evaluation and generation; practice in one need not supply the other. The source supplies human task evidence and a computational explanation, not evidence that each new agent theory requires new code. [Human–LLM differences](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) remains the transfer boundary: human internalization, working-memory slips, and unconscious compilation cannot be presumed to describe an agent consuming skill files.

## Learning Claims (our opinion)

On the source's terms, learning changes the productions available for later problems and their strength. Its inputs include instructions, examples, and successes and failures retained as declarative knowledge. Supplied general methods produce a solution trace; goals identify which parts belong together for compilation. Proceduralization removes selected declarative lookups, and composition preserves the effect of a goal-achieving sequence in a shorter procedure. The simulation therefore specifies a persistent change that can cause later improvement. Human speed and transfer results support aspects of this explanation without uniquely identifying the mechanism.

For Commonplace, the key distinction is between improving execution of knowledge and criticizing that knowledge. Compilation and strengthening alone do not establish [conjectural learning](../notes/definitions/conjectural-learning.md): they can make a procedure more effective without a formulated criticism of what its guiding account says. The report's revised account of induction is closer to that question. It assigns generalization and discrimination to strategic problem solving using semantic knowledge, rather than to automatic comparison of rule syntax. Conscious rule formulation and correction provide relevant evidence, but the report does not establish every part of Commonplace's membership conditions for each learner. Missing evidence leaves that classification open.

The revised induction account also limits what apparent learning from one example means. Generalizing an example may depend on understanding why it works and which features matter; the example is not the learner's entire evidential or conceptual starting point. This supports separating newly observed evidence from the knowledge and methods already available to interpret it.

The [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) applies to the model's learning machinery. Domain-specific productions and strengths change, while the production formalism, compilation operations, and availability of general methods are presupposed. Goal structures organize each solution, but their role as the basis for compilation is not itself learned in the account. The experiments vary practice, task use, editor interfaces, or instruction; none isolates whether an alternative representation or compiler would learn better. This bounds architectural inference without demonstrating that the supplied architecture cannot express some particular skill. Finally, ACT's declarative/procedural distinction concerns how information is used; it is not identical to Commonplace's natural-language/symbolic distinction. Declarative information in a symbolic simulation is already formally represented.

## Extractable Value

1. **A concrete mechanism for learning a cheaper execution path.** The appendix separates removal of declarative lookups from composition of goal-achieving rule sequences. This adds technical substance to the two-layer note's cognitive-architecture illustration. Its fixed production-and-goal machinery and human task evidence do not validate that note's promotion or maintenance regime. [quick-win]
2. **Transfer should be tested by operation, not shared content alone.** In the reported LISP study, evaluation practice reduced average evaluation time from 18.2 to 10.0 seconds and raised accuracy from 58% to 85%; accuracy on isomorphic generation problems changed only from 71% to 74%. Another manipulation held individual-function frequency fixed while varying pair frequency: frequent pairs averaged 6.55 seconds versus 8.61 seconds. These bounded human comparisons motivate agent tests that distinguish knowing a relation, composing familiar operations, and using the relation for a different task. They do not show that LLM agents will have the same transfer pattern. [experiment]
3. **Feedback timing depends on the operation being learned.** The proposed mechanism requires preserving decision-point information until corrective feedback arrives. The reported game study favors immediate error signals for successful moves, while discovery practice improves recognition of error states. Supplying an answer can instead train copying. This suggests testing whether agent learning records preserve the relevant decision state and whether feedback exercises the intended operation; it is not a universal preference for immediate feedback. [experiment]
4. **Single-example generalization can reuse prior understanding.** The replacement of syntactic induction by semantically informed problem solving gives a historical counterpoint to accounts that attribute a general rule to the new example alone. Retain this as a distinction between the observed example and the learner's prior resources, rather than evidence for a general one-shot learning guarantee. [just-a-reference]

## Limitations (our opinion)

Several studies are summarized without full sample sizes, uncertainty estimates, or methods. The opening LISP account combines a detailed individual protocol and fitted simulation with tutor observations from 38 subjects. Reproducing that protocol is not a unique identification of the learner's mechanism. The editor-transfer studies improve the evidential position by using independently motivated production analyses, but the report does not compare complete alternative cognitive architectures. Faster frequently practiced combinations could also fit other accounts of practice; the frequency control rules out differing exposure to the individual functions, not every rival learning mechanism.

The source's broad ambition to explain cognitive skill acquisition exceeds the mainly adult technical-skill evidence. Its account of procedural transfer also distinguishes intact execution of a transferred procedure from harm caused by choosing that procedure in the wrong situation. Substantial transfer after changing editor key bindings does not establish that procedural learning is universally free of interference or harmful transfer. Likewise, the tutor comparisons evaluate instructional packages; they do not isolate compilation as the sole cause of better outcomes.

The full-source capture contains noisy OCR, damaged formulas and LISP punctuation, and poorly preserved figures. The prose and appendix support the qualitative mechanism, but exact executable rules should not be reconstructed from this text. No implementation was inspected or executed, and no experiment was reproduced. Application to Commonplace requires evidence about an agent's actual consumer, retention mechanism, and tasks, rather than identifying a natural-language skill file with an ACT production.

## Recommended Next Action

Update the cognitive-architecture illustration in [the two-layer execution note](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) with this earlier ACT/GRAPES account of proceduralization and goal-bounded composition, retaining its status as an illustration rather than evidence for Commonplace's promotion and maintenance policies.
