---
description: "Making retained state explicit makes it nameable, citable, and selectively revisable; credit assignment, coherence, retrieval, and admission are separate mechanisms explicitness enables but does not supply"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Explicit artifacts buy addressability, not credit assignment, coherence, retrieval, or admission

Making retained state explicit means encoding it in natural-language or symbolic artifacts rather than in parametric state. The move buys **addressability**: a retained commitment becomes an object the system can name, cite, inspect, and revise one piece at a time, since [reflection buys addressability](./reflection-buys-addressability.md) and [only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md). That is a real property, and it is worth paying for.

Addressability is what the move supplies on its own. Four further properties are often read into "explicit" and do not follow from it: assigning credit after a failure, keeping the store coherent, retrieving the right artifact at the right time, and deciding which proposed change is admitted. Each is a distinct mechanism. Explicitness makes each one buildable and supplies none of them.

## Credit assignment

A deployment failure does not say which of many artifacts, or which interaction among them, should change. Gradient descent has an answer inside a fixed differentiable graph: the chain rule propagates responsibility for the loss to every parameter, by construction and without a separate diagnosis step. An artifact corpus has no such construction, and [credit assignment without a chain rule is the hard core of learning over localized artifacts](./the-bitter-lesson-selects-production-methods-not-representational.md).

Explicitness supplies the units credit could be assigned *to*. Names, boundaries, and addresses are prerequisites for saying "this artifact was wrong", but they do not perform the attribution. The two regimes trade opposite gaps: a differentiable graph computes the attribution over opaque units, while an artifact corpus offers legible units with the attribution left open. The corpus boundaries also fix which units credit can name at all, and [learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — a correction no artifact boundary can express stays out of reach however clearly the artifacts are written.

## Coherence

Two artifacts can each be well-formed, individually plausible, and mutually contradictory. Being explicit does not run the comparison that would find the conflict. Detection is work that has to be scheduled, and its cost grows with the number of pairs that could conflict rather than with the number of artifacts. This is one reason [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md): a store can grow while contradictions accumulate inside it.

[Codification](./definitions/codification.md) buys a partial substitute. A schema, type, or validator makes some conflicts machine-detectable — those among the relations it declares. Commonplace's own case is narrow in exactly this way: an [enforced tag-README](./an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) has its declared membership relations checked while its editorial claims are not. Explicitness makes a contradiction expressible, and locatable once someone finds it. Locating is the cheaper half.

## Retrieval

An explicit artifact affects a task only along some path that surfaces it for that task. [A retrieval miss is a local reflective-path failure](./a-retrieval-miss-is-a-local-reflective-path-failure.md): the artifact stays written, may stay true, and changes nothing about the operation that needed it. Explicitness supplies handles a retrieval path can use — titles, descriptions, tags, links, indexes — and that is a genuine contribution, because material without such handles is harder to surface at all. But relevance-based discovery cannot enumerate in advance everything a task might need, so the wire stays best-effort however clean the artifacts are.

## Admission

Whether a proposed change enters the store is decided by a gate, not by the change being writable. [Continual learning requires governing behaviour-changing writes](./continual-learning-requires-governing-behaviour-changing-writes.md) — selecting a candidate, validating it, and deciding with what force it enters — and [a proposal-selection loop requires reject-capable evaluation](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md), because a loop that adopts every proposal has a write path where its evaluation function should be.

The sharpest witness that admission is separate is a system whose explicitness is total. In [the Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), the machine's own code, hardware, environment, and utility function are formally described and rewritable, and the acceptance rule still has to be stated on its own: a proof that switching now beats continuing. Its strictness then costs the machine the beneficial rewrites it cannot prove. Full explicitness made room for an admission rule and left the rule's design and price open.

## What explicitness buys is buildability

The four mechanisms are not out of reach for an artifact layer. Explicit dependencies make an impact closure computable, so validation after a change stays bounded when the change is [sparse in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md) — a partial substitute for credit assignment, since an artifact's dependents are a candidate blame set rather than a verdict. Retained episodes can carry attribution signals. Maintained checks price later candidates, so [oracle accumulation improves the selection environment](./oracle-accumulation-improves-the-selection-environment.md) for admission. A written gate can itself be audited and revised, because it is an artifact too.

None of these arrives with the decision to write things down. Each is a separate build with its own cost, coverage, and failure modes. The common error is to read "explicit" as "coherent and correct": the store is legible, so its contents feel like knowledge that has already been checked.

## Consequence for claims about learning outside weights

A governed artifact layer over a frozen interpreter is, on this argument, at most a candidate substrate for learning. Showing that it learns requires exhibiting each of the four mechanisms separately, with its own evidence. A comparison against weight updates that credits the artifact layer with coherence and correct retrieval because the artifacts are readable compares an idealization against an implementation.

## Scope

- This is not an argument against explicit retention. The positive half stands: addressability is what makes selective revision, criticism, and transfer possible at all.
- Four properties are named here because they are the ones this argument identified. The list is not claimed exhaustive; another property inherited by assumption would extend it rather than refute it.
- Partial substitutes exist for each — dependency closures, declared-relation validators, indexes and enforced membership marks, maintained checks. Whether any of them is adequate at a given corpus size is empirical and unresolved here.
- The claim is about what explicitness entails, not about what a particular system achieves. A system that has built all four mechanisms is an instance of the claim, not a counterexample to it.
- Explicitness is graded rather than binary, and codification buys automatic checking within the semantics it declares. The claim is that no currently available degree makes all four mechanisms free. A form of explicitness under which one of them came free would narrow the claim to the rest.

## Open Questions

- Whether any of the four admits a general method for a large, interdependent artifact corpus, or whether each stays a per-domain build.
- Whether the four are independent or are surface forms of one missing thing — a selection environment with a computable attribution path.
- Whether the credit-assignment gap is intrinsic to non-differentiable units or contingent on current methods, as the pre-backpropagation analogy for hand-crafted features suggests.

---

Relevant Notes:

- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: defines addressability and its comparative reading, which this note's positive half assumes
- [Only explicit retention is durable, writable, and addressable](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: the form-level comparison establishing explicit artifacts as the currently available addressable channel
- [The Bitter Lesson selects production methods, not representational form](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: credit assignment without a chain rule as the open problem for learned localized artifacts
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — grounds: a store growing while discoverability, composability, and trust degrade — the coherence clause's case
- [A retrieval miss is a local reflective-path failure](./a-retrieval-miss-is-a-local-reflective-path-failure.md) — grounds: why a written artifact reaches a task only through a best-effort discovery path
- [Continual learning requires governing behaviour-changing writes](./continual-learning-requires-governing-behaviour-changing-writes.md) — extends: develops admission into the full governance problem of selection, validation, authority, and coordination
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the reject-capable evaluation position that admission occupies in a change loop
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — evidenced-by: a fully formalized system whose acceptance rule still had to be designed and paid for separately
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md) — mechanism: how explicit dependencies become a bounded validation scope, the partial substitute for credit assignment
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — mechanism: how maintained checks build the admission gate explicitness leaves open
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — extends: why the artifact boundaries that make credit assignable also bound what any correction can express
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — contrasts: the case for automating the readable pair, which this note bounds by naming what its explicitness does not supply
