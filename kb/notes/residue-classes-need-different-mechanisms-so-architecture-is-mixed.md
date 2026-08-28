---
description: "Derives architectural mixedness from the residue classes: unrepresented premise, unsettled criterion, uncheckable result, and horizon cut each name a capacity that no other part of the architecture supplies"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Each residue class needs a different mechanism, so a self-improving architecture must be mixed

A system that moves decisions out of its human cut set keeps a residue, and the residue is adversely selected, [since warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md). Each residual decision stayed human for a reason. The reasons identified so far form a short list. A premise the decision needs is not represented anywhere the deciding process can read. The criterion is unsettled, so the method names a decider instead of determining a result. No oracle independent of the candidate can check the result. The decision falls after the declared automatic horizon ends. Call these the **residue classes**.

Each class names one capacity that has to grow before its decisions can move: representation, settlement, verification, continuity. This note takes the next step. Each capacity is supplied by a different part of the architecture, and none of those parts supplies another's capacity. A system built to shrink a residue that is nonempty in more than one class therefore has to contain more than one kind of part. Mixedness is derived from the residue classes, not stipulated as a design preference.

"Mixed" here means mixed in [representational form](./definitions/representational-form.md): retained natural-language artifacts, a parametric interpreter over them, and symbolic code all appear, because the capacities they supply are not interchangeable.

## Which part supplies which capacity

**Representation is supplied by retained explicit artifacts.** The premise has to be externalized somewhere the deciding process can read it and later revise it, [since only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md). One alternative exists: the deciding process reconstructs the premise from what it already sees. That works where the premise is recoverable from available material, and it leaves nothing addressable behind, so the reconstruction is repeated rather than criticized or rescoped.

**Settlement is supplied by retained theory together with an interpreter that applies it.** The criterion's content has to exist as a retained statement, [since a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). A stated criterion still underdetermines many cases. Something must apply it to a case the statement does not fully fix. Pre-LLM automation could take delivery only of a [codified](./definitions/codification.md) criterion, so semantic criteria stayed human; a language model can take delivery of an explicit natural-language one, [as methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) records. This is the pairing that [theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) argues for on independent grounds.

**Verification is supplied by evidence and oracles independent of the candidate.** Mechanical validators sit at the cheap end, tests and decorrelated checks above them, and accumulated evidence above that. What makes them a distinct part is the independence requirement rather than their machinery, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

**Continuity is supplied by a symbolic runtime that holds state and keeps executing.** A decision after the horizon can only move if the executor is still running when the decision arises. That takes state kept outside any one bounded call and transitions applied faithfully over a long path, which is the [bounded-context orchestration model](./bounded-context-orchestration-model.md)'s scheduler role. Hosting that role in a model instead is expensive rather than impossible, [because scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).

## No part covers another's class

The derivation depends on four non-substitutions, one per class.

**Code cannot settle a criterion.** A symbolic artifact executes the criterion it was given, and executes a wrong one as faithfully as a right one. Where the method says "use judgment", there is nothing to compile. Codification presupposes a settled criterion rather than producing one, so moving an unsettled decision into code either fixes an arbitrary reading or fails.

**An interpreter cannot warrant its own output.** Warrant needs a check the candidate did not author. A model judging its own proposal draws the check from the same distribution that produced the proposal, so the check's errors correlate with the errors it is meant to catch — [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md), and self-checking supplies neither guarantee. What the interpreter lacks here is independence, not capability, so a more capable interpreter does not close this class.

**Retained theory cannot execute.** A written criterion changes nothing until some process runs it, and a written artifact holds no position in a long path. Retention makes a claim available; it does not make anything happen at the moment the decision arises.

**Verification cannot supply an absent premise.** An oracle rejects candidates; it does not author the input nobody recorded. A check applied to a decision whose premise is unrepresented has nothing to check against. Verification can reveal that a premise is missing, which locates the gap without filling it.

## The premise-change test

The derivation predicts what happens when the residue changes shape.

Drop a class and the corresponding part becomes optional. Where every criterion in a domain is already formal — type checking, lexical analysis — no residual decision stays human for want of settlement, and the natural-language interpreter is not needed. What remains is a wholly symbolic compiler, which is what that domain actually built. Where a whole path fits inside one bounded call, nothing stays human for want of continuity, and a one-shot transformation with a check needs no scheduler.

Add a class with no corresponding part and the architecture is incomplete for it. A candidate: a decision stays human because the system holds no represented authority to commit the change, so no one has granted it scope. None of the four capacities above closes that by itself. Whether this is a fifth class or a subcase of representation — recording who holds the grant, under what conditions — is unresolved, and the test says what turns on the answer.

## Scope

- The claim inherits the parent note's condition: transfer is *preferential*, favouring warrantable decisions. Under transfer on some other basis — cost alone, or whatever an unattended model will attempt — the residue has a different composition, and which parts a system needs follows that composition instead.
- The four classes are the ones identified so far. Nothing here shows the list is exhaustive, and the derivation gives the architecture only as many kinds of part as there are classes in play.
- The parent table's last row, where transfer is possible but priced out, is not a class in this sense. No capacity has to grow, so no part corresponds to it. Making an existing part cheaper changes the price without adding a capacity.
- The mapping between classes and parts is not one-to-one. Retained artifacts carry both the represented premise and the criterion's content; settlement additionally needs the interpreter. The claim is that the capacities do not substitute for one another, not that parts and classes are in bijection.
- The parts are functional roles, not processes. One process can host two roles — a model can interpret a criterion and drive its own loop. Hosting two roles is not one capacity covering another: the roles still fail separately, and the error-correction asymmetry prices what hosting the runtime role in a model costs.
- The claim says what an architecture must contain. It says nothing about how the parts are wired, how many processes implement them, or which of them a given system should build first.

## Open Questions

- Whether the class list can be derived systematically from the warrantability conditions rather than collected. Continuity is the suspicious member: it may be a representation problem about state across a path rather than a class of its own.
- How independent an oracle has to be for the second non-substitution to hold. A second model call under a perturbed prompt is not the candidate's own author, yet shares training. If prompt perturbation decorrelates well enough for a class of cases, the interpreter-cannot-warrant-itself boundary is a gradient in those cases rather than a wall, and the verification part is partly reachable from the interpreter.
- Whether an architecture can be shown incomplete in practice by exhibiting a residual decision whose class no part addresses, which is the falsifying observation this claim invites.

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — extends: supplies the residue classes and the selection effect this note converts into an architectural requirement
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: the representation–settlement–warranted-execution conversion the four capacities are read off
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why verification is a separate part rather than a property of a capable decider
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — grounds: the retention-plus-interpretation pairing that supplies representation and settlement here, argued from sample efficiency instead of from residue classes
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: why the continuity role stays symbolic, priced as a cost gradient rather than a hard line
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — contrasts: motivates the scheduler-plus-model split from context scarcity and bookkeeping reliability, where this note reaches a similar split from warrant classes
- [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: the decorrelation condition behind the claim that an interpreter cannot warrant its own output
- [Only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: why the representation capacity needs an externalized artifact rather than a better decider
- [Representational form](./definitions/representational-form.md) — defined-in: the axis along which the resulting architecture is mixed
