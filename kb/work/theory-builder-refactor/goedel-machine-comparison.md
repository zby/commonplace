# How the proposed theory builder differs from the Gödel machine

> **Status:** Working comparison, 2026-09-14. The operator asked to
> differentiate the research approach from the Gödel machine. This comparison
> characterizes the proposed approach; it does not add restrictions to the
> general theory-builder definitions or establish a novelty claim.

## The distinction

The proposed builder develops and revises explicit, fallible theories of
external subjects and of its own theory-building machinery. Those theories
guide changes whose justification can be empirical and whose continued use
remains open to correction by later evidence. A machinery change need not
first be proved beneficial under the current self-theory.

The Gödel machine's proof-governed switching route requires a proof that
switching to a candidate program has higher expected utility than continuing
the current search, under its formalization. Its software, proof searcher,
axioms, and utility representation can change when that formalization licenses
the change. Observations can enter the proof process. The distinction therefore
concerns the grounds required for a switch, not whether the system observes
the world or can rewrite its evaluators.
([Gödel-machine note](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md);
[Schmidhuber, §§3.2, 4.1, and 6.1](https://arxiv.org/html/cs/0309048v5))

| Question | Gödel machine's proof-governed route | Proposed theory builder |
|---|---|---|
| What justifies a machinery change? | A proof of the switching claim under the formalization. | Evidence supporting the change relative to a stated objective, with assurance bounded by the checks performed. |
| How does evidence enter? | Observations enter through formalized operations and can support proofs. | Cases and operating consequences can challenge the theory used to diagnose, propose, or evaluate a change. |
| What if an empirical assumption is inadequate? | Proof alone does not establish the adequacy of the premises; formal revisions remain subject to the licensing route. | The builder can revise the implicated assumption and test the resulting theory and machinery without proving the revision from that assumption. |
| What remains uncertain? | Whether the formalization is adequate and useful proofs can be found within resources. | Whether interpretation, diagnosis, evaluation, and later correction are reliable enough for the intended use. |

This is a distinction between grounds for change. A symbolic theory can be
revised empirically, and the proposed builder can use proofs and validators
where they apply. Natural language, fixed model weights, and the mere presence
of self-modification do not define the difference.

## What this commits the research program to

Empirical acceptance permits acting where the required proof has not been
obtained. It also permits accepting harmful changes. The research target is
therefore not simply a more permissive admission route. It is a builder whose
explicit theories help it acquire machinery and evaluate changes reliably
enough for its work, including changes to its evaluators.

The distinctive proposed mechanism is the return from external theory work
to a theory of the machinery that performed it: an external failure can expose
a machinery limitation, prompt revision of the self-theory, and lead to a
machinery change tested in subsequent external work. A retained self-theory
must contribute to those decisions; a description added after a change is
not evidence for this mechanism.

The research question is whether that use of explicit theories improves later
theory-building competence and machinery acquisition compared with empirical
search that does not retain and use such theories. The
[experiment workshop](../explanatory-theories-deployment-time-learning/README.md)
owns the comparison designs. Neither empirical self-modification nor explicit
fallible theories alone are claimed as new here, and this comparison does not
establish that their proposed combination is absent from prior systems.

## Consequence for the definitions

The current drafts define the builder using fallible theories, keep reflection
and autonomy as its two conditions, and assess machinery extension under a
budget. The interpreter now has a
[separate definition](./resource-bounded-ideal-interpreter.md). This comparison
supports distinguishing the grounds for accepting changes; it does not yet
establish the drafts' stronger claims excluding the Gödel machine. Those
boundary cases require the
[reconciliation listed in the README](./README.md#next-review-reconcile-the-definitions).

Keep acquisition capability separate from the warrant for using an extension.
Evaluator replacement needs evidence of adequacy, not merely permission from
the incumbent. A claim that all future warrant is the closure of the seed
objective and evidence rules requires a separate argument; it is not needed
for this comparison. The
[objective-revision note](../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md)
limits what licenses an improvement claim, rather than establishing that an
autonomous builder's objective cannot change.
