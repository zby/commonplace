---
description: "Objective change is improvement only against a level outside both objectives; proxy revision, re-indexing, and surfaced under-specification subtract most apparent cases"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Revising an improvement objective is licensed from outside it or is not improvement

[Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md), so when a pathway changes the objective it is directed at, the natural question is whether that change was itself an improvement. The natural answer fails. A successor objective's own approval establishes nothing, because every objective approves of itself; if that counted, every objective change would be an improvement and the word would stop discriminating. Nor can evidence close the gap: [evidence bears on an objective](./definitions/evidence-bearing-on-an-improvement-objective.md) by carrying information about how the system stands relative to it, never about whether that objective is the one to have. The restriction is to the *terminal* objective, and it is narrower than it first looks. Evidence tests a stand-in against the thing it stands in for all the time — a benchmark that predicts held-out performance poorly, a rubric that keeps disagreeing with later judgment, a validator that misses a defect class are all empirical findings about a proxy, made against an objective that has not moved. What evidence cannot do is establish that the terminal objective is itself the right one to hold, because there is nothing left for it to be measured against.

So an objective change is an improvement only relative to a level outside both objectives. That much is nearly forced. What makes it a useful claim rather than a bare impossibility result is the second half: most changes that look like objective revision are not objective revision, and subtracting them leaves a residue small enough to say something definite about.

## Three subtractions

**Proxy revision.** Most revision of what a system steers on revises a *check*, not the objective. [Oracle strength is how reliably a check discriminates relative to the objective](./warranted-autonomy-is-bounded-by-oracle-domain.md), which means an oracle is already a stand-in for something it is not — a relation the [oracle-strength gradient](./oracle-strength-spectrum.md) treats as continuous rather than as a threshold. Replacing a gate, tightening a validator, swapping a benchmark is therefore assessed by whether the replacement discriminates better *relative to the same unchanged objective*. That is an ordinary empirical question with a determinate answer, no meta-criterion required and no regress. Commonplace's own criterion history is almost entirely this: review criteria get rewritten because they misfire, and the rewrite is judged against what the criterion was already for.

**Re-indexing.** An objective can change because the analysis changed — a different task, different users, a boundary moved. Since the objective is a declared parameter, this is the same operation as redeclaring the boundary or the horizon: it yields a different attribution, not a better one. Nobody asks whether widening a declared boundary was an improvement. Nothing was revised by the system; something was redeclared about it, and no license is needed because no improvement is claimed.

**Under-specification surfacing.** A pathway that begins minimizing latency and comes to minimize latency subject to correctness looks like it revised its objective. Usually the declared objective was an incomplete statement of a wider one that was operative throughout, and the correctness failures were evidence bearing on that wider objective rather than on the narrow one's adequacy. The revision is licensed at the wider level, and the earlier declaration is revealed to have been a proxy. This folds into the first subtraction instead of adding a case: what changed was the stand-in, not what it stood for.

## The residue

What survives all three: a pathway changes its terminal objective, the change is caused by the pathway rather than by the world, and no wider objective was operative for it to answer to. Here self-ratification is the only license available, and it is not a license.

The honest report is that the objective changed. That is still operative, evidence-responsive [self-change](./definitions/self-improving-system.md) — membership is untouched — but its improvement status is not determinable from inside. If no outside level is available, the improvement claim is unavailable rather than merely unproven.

## What counts as an outside level

Four forms, and they are not equally mysterious.

- **The prior objective licenses the transition.** Reduces to the first or third subtraction.
- **A retained higher criterion ranks objectives.** A genuine meta-objective. It pushes the question up one level and terminates wherever that criterion is itself declared rather than derived.
- **An external judgment.** A person, an institution, a declared purpose.
- **An epistemic standard on how each objective stands to the evidence.** The successor better systematizes what the predecessor organized.

The fourth resolves a question the parent note left open — whether it is a real alternative to a meta-criterion or a disguised instance of one. It is a meta-criterion, and the useful distinction is what kind. Licensing the successor because it better systematizes the evidence does induce a comparison over objectives, so the third form's structure is not escaped; what differs is the species. A retained higher criterion ranks objectives by *preference* — this one is worth more than that one. An epistemic standard ranks them by how each stands to the evidence, which is [explanatory-reach applied to criteria](./first-principles-reasoning-selects-for-explanatory-reach-over.md). The comparison it yields is also usually partial rather than total.

The species difference carries a scope restriction. An epistemic standard can adjudicate between empirical claims — competing models, competing proxies, competing accounts of what a system's failures mean. It cannot settle whether autonomy should be valued above safety, or whether one terminal purpose is preferable to another. Where the objectives differ in what they value rather than in what they claim about the world, the fourth form has nothing to say and the third or the external judgment has to carry it.

**Why the regress does not need terminating.** The apparent regress — every level requiring a level above it — is an artifact of expecting the system to supply its own objective. Because the objective is declared, the chain ends at a declaration. [The Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) is the limiting case with that terminus made formal: rewrites are licensed only by proof under its own formalization, and the formalization is given rather than derived. But declaration settles indexing, not improvement. An analyst who records that the objective changed has not thereby established that the change was good.

## Scope

- The claim concerns whether an objective *change* is an improvement, not whether an objective is any good. A mis-specified objective faithfully pursued is a different failure, and one membership already declines to rule out.
- The subtractions are claims about what observed pathways actually do, not about what is possible. Nothing here shows terminal objective revision cannot occur.
- Commonplace exhibits no instance of the residue: its criterion changes are proxy revision against unchanged quality objectives. The residue is presently unexemplified here, which is a reason to hold this analysis lightly.

## Open Questions

- Whether the fourth form can run computationally rather than only in an analyst's judgment — a system applying an epistemic standard to its own objectives would be the first instance of the residue that carries a license.
- Whether "a wider objective was operative all along" is always available as a redescription. If it is, the residue collapses and the claim goes vacuous from the other direction — the mirror of the [post-hoc objective problem](./self-improvement-is-relative-to-a-declared-objective.md), and unresolved for the same reason: independent specifiability is not mechanically checkable.

---

Relevant Notes:

- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: the declared-parameter framing this develops, and the open question it closes
- [Evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md) — defined-in: why evidence cannot bear on its own criterion's correctness
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: oracles discriminate relative to an objective, the stand-in relation the first subtraction rests on
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — extends: the proxy relation as a gradient rather than a threshold; exploratory
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the membership the residue still satisfies while its improvement status stays undetermined
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the epistemic standard the fourth outside level applies
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — grounds: a formal, declared terminus for the licensing chain
