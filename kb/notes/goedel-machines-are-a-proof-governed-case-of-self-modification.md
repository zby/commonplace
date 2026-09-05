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
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: explains how a current policy can govern its own revision
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: identifies the risk of admitting a harmful retained change
- [Schmidhuber, Gödel Machines (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md) — abstracted-from: supplies the formal construction, theorem, and proof-search limits
