---
description: "PRODIGY derives different control rules by explaining the winning or losing branch of the same search and separates proof of applicability from the cost of keeping a rule active."
source: https://www.ijcai.org/proceedings/1987/0046.pdf
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 334ed825f4b6eab788c61fe628e0eb78206a2b1e0d2aceb29a6cf1c433076e11
ingested: "2026-11-21"
occasion: "Which parts of deliberative learning, if any, have precedents in symbolic learning and its retention judgments?"
type: types/ingest-report.md
domains: [explanation-based-specialization, search-control-rules, prodigy]
tags: [improvement-loop, learning-theory, self-improving-systems]
learning_claims: true
---

# Ingest: Strategies for Learning Search Control Rules: An Explanation-based Approach

## Classification

Steven Minton and Jaime G. Carbonell of Carnegie Mellon describe their PRODIGY implementation in an IJCAI 1987 paper. The evidence consists chiefly of worked derivations from blocks-world search trees.

## Summary

PRODIGY learns how to search by explaining a choice in its own search trace. The learner starts with a question about the choice: did it succeed, fail, have no viable rival, or cause one goal to interfere with another? The trace guides a proof from axioms about both the domain and the solver. The conditions needed for that proof become the conditions of a rule that later selects, rejects, or prefers a candidate. In the worked example, explaining how UNSTACK succeeded ties the rule to a particular arrangement of blocks; explaining why PICKUP failed justifies choosing UNSTACK across more arrangements under the same operators. The authors distinguish deriving such a rule from keeping it active: later search time saved must justify the time spent checking whether the rule applies.

## Contribution assessment (our opinion)

The strongest contribution is a comparison within one decision: the winning branch and its failed rival justify the same choice for different reasons, and those reasons predict different scope. This exposes a design choice that simply generalizing a successful plan would hide: what should the learner try to explain? The worked proofs establish that the distinction matters even with the solver held fixed. They do not establish which explanation strategy pays more often or whether using several is faster overall.

## Quotes

No source quotes have been retained yet.

## Connections Found

PRODIGY gives [the account of failure explanations changing later branch decisions](../theory/failure-explanation-changes-later-branch-decisions.md) a symbolic precedent: the retained item is not a failed episode but a condition the solver can check before choosing the same operator again. This paper supplies the derivation and states the criterion for keeping a rule active. [Minton’s 1988 utility study](./minton-utility-of-ebl-aaai88.ingest.md) supplies the separate experimental evidence about what retaining rules cost.

## Learning Claims (our opinion)

A training trace is evidence for choosing steps in a proof, not itself the explanation. PRODIGY starts with a supplied target concept and specializes it top down, using the trace to choose among proof schemas until primitive conditions remain. A template turns those conditions into a control rule. For instance, if the goal is to hold a block that is not on the table, trying PICKUP requires putting the block on the table first, which requires holding it already. The solver’s goal-stack cycle explains the rejection; the number of blocks above the target plays no part. With PICKUP eliminated, UNSTACK is the sole remaining candidate, not a guarantee of success.

Against the [theory builder](../theory/definitions/theory-builder.md) conditions, localized content and consumption are clear: each rule states a condition and a decision, and the solver applies matching rules at that decision. Criticism is narrower. The failure proof identifies why a proposed move cannot work under the axioms. The utility test judges whether an individual rule earns its matching time, not whether its premises are wrong. Iteration is described for search: interleaved learning can redirect backtracking, and the active rule set and its utility estimates carry into later problems. No worked sequence shows an adverse utility judgment prompting a revised explanation. Persistence across separate sessions is not established.

The paper therefore supports learning in a specific sense: on a later matching problem the solver can avoid a branch it previously had to explore. It does not measure net improvement across problems. Its domain theory is an input to deduction, not a conjecture revised by this learner. The target concepts, proof schemas, and permitted control decisions illustrate [the boundary of learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): a designer can extend them, but the worked learner does not invent a new question or a new standard for retaining its answer.

## Extractable Value

1. **Separate the reason to act from the reason to retain.** The proof says when a choice is justified. The retention judgment compares cumulative search time saved with cumulative matching time, including checks that do not pay off. This is a precedent for judging future use separately from the quality of the original explanation, not for measuring every kind of knowledge by time. [quick-win]
2. **Ask why the rival failed.** In the fixed blocks-world example, the success proof depends on how the solver cleared the block; the rival’s failure depends only on the holding goal and the block not being on the table. The useful question for a later decision may concern the rejected alternative rather than the successful sequence. [quick-win]
3. **Match the strength of the instruction to the explanation.** A proof of failure licenses rejection. A proof that one goal ordering forces rework licenses a preference, since rework can be unavoidable. Retaining the latter as a prohibition could exclude a solution. [quick-win]

## Limitations (our opinion)

The paper states what rule utility compares but does not show how PRODIGY estimates the search it would have performed without a rule, or report a retention experiment. The authors report testing the system in scheduling and robotics, but present no corresponding performance comparison here. The worked proofs assume explicit operator effects and a model of the solver. A failed attempt without those premises does not establish that every alternative continuation would fail. The examples support neither autonomous repair of incorrect premises nor the same reliability for explanations of open-ended agent work.

## Recommended Next Action

Add the PICKUP/UNSTACK comparison to [the failure-explanation note](../theory/failure-explanation-changes-later-branch-decisions.md) as a symbolic precedent, distinguishing the proof that changes a later choice from the utility judgment that keeps the rule active.
