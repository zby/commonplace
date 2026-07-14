---
description: "Curated head for the self-improving-systems tag — reflection is the machinery and the cheap part; the loop is the object, and autonomy is a separate gradient over it"
type: kb/types/tag-readme.md
index_source: tag
index_key: self-improving-systems
complete: true
---

# Self-improving systems

The object is the [**self-improving system**](./definitions/self-improving-system.md): an adaptation loop that runs on the system itself, through its own writable self-representation, against an improvement objective. Humans may sit inside the boundary; **autonomy** — how much of the loop runs without one — is a separate gradient over it. Most systems in [agent-memory-systems](../agent-memory-systems/README.md) are a bid at some version of it — mine the traces, write the lesson down, load it next time.

## Reflection is the machinery, not the property

A [reflective system](./definitions/reflective-system.md) holds a causally connected map of itself: kept true, and steering. Add **intercession** and the map is writable from inside. That is the whole machinery, and it delivers nothing on its own — a Smalltalk image has it maximally, classes as objects and a compiler that edits itself, and left alone it improves nothing for a decade. The programmer supplies what is missing. Remove the programmer and the loop is not weakened; it is absent.

The machinery is also nearly free: declare a maintainer inside the boundary and [reflection is cheap](./human-inclusive-boundaries-make-reflection-cheap.md), so *the system modifies itself* discriminates almost nothing. Where the map is prose rather than code an interpreter reads, the wire runs through search — so [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md), and a represented constraint no process can find is inert.

## The loop is where the work is

[An adaptation loop requires search, evaluation, and operative retention](./an-adaptation-loop-requires-search-evaluation-and-retention.md), and they fail in different ways. A system with the wire that stalls anyway is missing a *named* function: a reviewed note nothing loads has no consumer; a patch never merged has no channel; a validator nothing invokes has no force. In each, the work happened and the loop stayed open.

The two scarce functions are not alike. [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — evaluation is the terminal filter, so a rejected candidate costs effort while a bad acceptance is kept and can compound. And what the oracle returns is a claim, not a result: acceptance says the candidate met the criterion applied, not that the system improved.

## Three gradings over the same base

They answer different questions and move independently — a system can widen one without touching the others.

- **Coverage — what is represented.** [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md): a claim must name the form (prose, symbolic, distributed-parametric) and the operation depth.
- **Closure — what the methodology settles.** [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): whether each decision a change raises has a governed answer, or must be improvised.
- **Autonomy — who performs the functions.** [Human-inclusive boundaries make reflection cheap](./human-inclusive-boundaries-make-reflection-cheap.md): the axis that actually discriminates, and the one the rest of this page follows.

## Autonomy is bought, not chosen

Autonomy does not decide whether a system is self-improving; a human-inclusive loop still is one, and *autonomous* self-improving is reserved for a boundary with no human in it. More autonomy strengthens the autonomy attribution, but it is not automatically a better design. Hand a gate to a model with a rubric and the system is autonomous there tomorrow: the evaluator is fallible, but it still rejects things, so [the loop still closes](./definitions/self-improving-system.md) and the system stays self-improving while quietly getting worse. What is bounded by [mechanical verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) is *warranted* autonomy — running unattended and still deserving trust — and that is what predicts where a human remains necessary.

[Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md): the loop can run unattended only over candidates the available oracles can assess with the required confidence. Tightening an acceptance threshold can reduce reach, while improving an oracle's discrimination can expand it.

## Occupants

The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) makes all of its code rewritable — including the routine that searches for rewrites — and accepts one only under proof that it helps. It is the *autonomous* case, bought with the strongest available oracle and paid for in reach: every improvement it cannot prove is unreachable.

[Commonplace](../reference/commonplace-as-a-reflective-system.md) has the same skeleton and a looser gate: tests, validators, and a maintainer who notices what to change and judges whether it helped. Humans hold search and the judgment-heavy evaluation — the gates no adequate automatable oracle closes. That makes it human-inclusive rather than autonomous, and self-improving all the same.

## Consequence for agentic systems

[Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md): reliability gains move behavior between prose and code rather than staying in either, so coverage of a single form cannot carry them.

The external reviews are written in this vocabulary rather than as feature lists. The [agent-memory-system-review](../agent-memory-systems/types/agent-memory-system-review.md) type asks each system for its representational forms, its behavioral authority as *consumer, channel, and force*, and its **promotion path** — prose advice to symbolic validator to enforced gate — which it calls "often the most design-relevant question." The [comparison matrix](../agent-memory-systems/systems-table.md) is generated from those terms.

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this sits inside, including [actionable methodology](./definitions/actionable-methodology.md)
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
