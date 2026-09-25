---
description: "A Gödel machine admits self-rewrites through proof under its current formalization; this restricts admission without establishing how many useful changes are reachable or how reliably they are found"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# Gödel machines are a proof-governed case of reflective self-modification

Schmidhuber's Gödel machine permits rewriting its software, including the code
that searches for changes. Its initial admission route requires a proof that
switching to a proposed program has greater expected utility than continuing
the current search, under axioms describing the machine, environment, and
utility function ([Schmidhuber, §3.2 (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md)).

This is a proof-governed construction of reflective self-modification, not a
definition of reflection. Its admission rule offers rigor relative to a
formalization while excluding switches for which the required proof is not
obtained. That restriction alone says neither how large the reachable state
space is nor how well the machine operates within a practical budget.

## The change loop

The construction can be read as a [proposal-selection improvement
loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md):

| Function | Gödel-machine realization |
|---|---|
| Self-representation | Axioms describing the machine, its software, environment assumptions, and utility |
| Search | Proof techniques that can construct proposed replacements and proofs |
| Evaluation | A proof of the target theorem comparing switching with continued search |
| Authority and retention | The switching operation invokes the proved replacement, which can rewrite the subsequent software |

These functions are not independent components. Passing the switching check
and invoking the replacement are coupled. Environmental observations can enter
the proof process through the source's time-labelled `state2theorem` operation;
the machine is not limited to deductions about its initial state alone.

Self-modification can also change the proof searcher, axioms, or utility
representation where the predecessor formalization licenses that change.
The construction does not require every later policy choice to have been
listed in the seed, nor does it require an unchanged proof-search implementation
forever ([Schmidhuber, §3.2 and §6.1 (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md)).

## Three different limits

**Admission.** A useful switch cannot take effect through the proof-gated route
unless the required proof is obtained. The paper says the machine "must ignore
those self-improvements whose effectiveness it cannot prove"
([Schmidhuber, §2.4 (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md), verbatim).
Some claims may be unprovable under the axioms; others may be provable but not
found within the available resources. These are different limits.

**Adequacy of the formalization.** The Global Optimality Theorem compares a
switch with continuing the search, including the later switches that search
might find. Its guarantee is conditional on the encoded assumptions and
utility. A valid proof under an inadequate model or objective need not warrant
the outcome a user actually wanted. Formalization moves some judgment into the
choice of premises and objective; it does not remove that judgment.

**Practical continuation.** The existence of an admissible beneficial switch
says little about the cost of finding it or about sustained software-production
performance. A restrictive proof gate may allow many useful changes under one
formalization and few under another. No general size estimate follows from
proof-gated admission alone. Likewise, being allowed to emit arbitrary code
does not make a useful empirical successor likely.

## Comparison with empirical self-modification

An empirical loop can propose a change, test it, observe later consequences,
and recover without first proving improvement. Its characteristic risk is
accepting harmful changes. The proof route instead risks leaving a useful
change unavailable because its proof is absent or too expensive. Which costs
more depends on the objective, evidence, search process, and consequences of
error.

Consider the narrow case of a prompt-editing loop whose harness loads each edit
without an independent acceptance check. Its revision path is permissive and
its retention reliable, but neither property makes the edit good. Once a harmful
instruction is retained, it can affect later runs. This illustrates why
[false-positive acceptance becomes
operative](./false-positive-generation-is-filtered-before-retention.md).

That is a property of the chosen gate, not of natural-language representation.
A prompt-editing system can add tests, limited authority, independent criticism,
versioning, and rollback. Conversely, executable code can be admitted through a
weak gate. [Available checks](./warranted-autonomy-is-bounded-by-oracle-domain.md)
bound what the observed success warrants in either case. Proof is one way to
govern self-referential changes; it is not the only way to obtain bounded
empirical warrant.

## Acceptance and search pressure differ

The [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
uses viability to decide archive admission and benchmark performance to weight
later parent selection. It does not require each archived candidate to prove
or even demonstrate immediate improvement. The [Huxley-Gödel
Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
uses evidence about descendants to inform that selection. These are different
uses of evidence from a proof authorizing a switch.

[Incremental Self-Improvement](../sources/on-learning-how-to-learn-learning-strategies.ingest.md)
provides another contrast: a payoff-per-time criterion governs retained
modifications and restoration when they cease to qualify. These cases show why
admission, reproduction, and continued retention should not be collapsed into
one notion of evaluator strength.

The useful comparison has at least two dimensions: the rigor of inference from
stated premises, and how well those premises and observations cover the
objective. A strong answer on one dimension does not supply the other.

## Grounds for change: comparison with a theory builder

A [theory builder](./definitions/theory-builder.md) states tentative
theories, acts on them, criticizes what they say, and lets the result of
criticism shape the next conjecture. A
[reflective](./definitions/theory-builder.md#qualifiers) builder also holds and
criticizes theories of its own machinery. In neither case must a machinery
change first be proved beneficial under the current self-theory. The
distinction from the Gödel machine concerns the grounds required for a
change, not whether the system observes the world or can rewrite its
evaluators. Natural language, fixed model weights, and the mere
presence of self-modification do not define the difference.

| Question | Gödel machine's proof-governed route | Theory builder |
|---|---|---|
| What justifies a machinery change? | A proof of the switching claim under the formalization | Evidence supporting the change relative to a stated objective, with assurance bounded by the checks performed |
| How does evidence enter? | Observations enter through formalized operations and can support proofs | Cases and operating consequences can challenge the theory used to diagnose, propose, or evaluate a change |
| What if an empirical assumption is inadequate? | Proof does not establish the adequacy of the premises; formal revisions remain subject to the licensing route | The builder revises the implicated assumption and tests the resulting theory and machinery without proving the revision from that assumption |
| What remains uncertain? | Whether the formalization is adequate and useful proofs can be found within resources | Whether interpretation, diagnosis, evaluation, and later correction are reliable enough for the intended use |

Empirical acceptance permits acting where the required proof has not been
obtained, and it permits accepting harmful changes. A theory builder is
therefore not simply a more permissive admission route. The open question
about it is whether stated theories, including a self-theory that criticism
of the builder's own operation revises, make its machinery acquisition and
evaluation reliable enough for its work. Keep acquisition capability
separate from the warrant for using an extension: evaluator replacement
needs evidence of adequacy, not permission from the incumbent. Whether the
Gödel machine itself is a theory builder stays open. The construction does
not criticize the premises its proofs start from, but whether a deployment
criticizes them elsewhere is a question about that deployment, so this
comparison establishes no categorical exclusion.

## Scope

- A [reflective system](./definitions/reflective-system.md) needs a causally
  connected self-representation, not a proof of improvement. Proof-gated
  admission is an additional design choice.
- Deductive closure concerns derivable propositions. Transition closure
  concerns states reachable through permitted operations and inputs. Neither
  alone establishes practical reliability.
- The Gödel-machine paper presents a formal construction, not an implemented
  software house with measured continuation reliability. It supports the
  architectural comparison, not a performance ranking.
- Formal causal reasoning would require suitable assumptions and objectives
  inside the formalization. The host architecture alone does not supply them.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: separates the functions instantiated by the proof route
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: keeps admission evidence relative to what its premises and checks cover
- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection does not require proof-gated admission
- [Theory builder](./definitions/theory-builder.md) — contrasts: empirical grounds for a machinery change against the proof-governed route; the machine's own classification stays open
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: explains how a current policy can govern its own revision
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: identifies the risk of admitting a harmful retained change
- [Schmidhuber, Gödel Machines (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md) — abstracted-from: supplies the formal construction, theorem, and proof-search limits
