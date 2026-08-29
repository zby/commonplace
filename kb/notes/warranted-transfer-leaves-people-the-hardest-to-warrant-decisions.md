---
description: "Transfers the codification selection effect to the human cut: preferring warrantable decisions for computational supply leaves people a residue that is harder to warrant per decision"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions

Call a decision **warrantable** for computational supply when three conditions hold: its inputs are represented where the deciding process can read them, its criterion is settled enough to apply, and its result can be checked by an oracle the candidate did not author. These are the three parts of the conversion that lets a recurring human decision move to a computational actor, [since methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md), and the third is the binding one, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

The claim is conditional. When a system preferentially moves warrantable decisions out of its human cut set — the human participants whose decisions the improvement path cannot complete without, [as defined where computationally directed self-improvement is a fixed-boundary reallocation](./computationally-directed-self-improvement-is-a-reallocation.md) — the decisions that remain with people are, per decision, harder to warrant than the ones that left. The residue concentrates unrepresented premises, unsettled criteria, and results no available oracle can check.

This is the same selection effect that operates one layer down, where [codifying predictable choices leaves agents with less predictable work](./codifying-predictable-choices-leaves-agents-with-less-predictable-work.md). There the selector is predictability: a state-to-action mapping that can be fixed and verified cheaply enough to move from open-ended judgment into a symbolic control. At the human cut the selector is different, because the receiving actor is different. A language model with a verifier can take work that no schema could take. It cannot, with warrant, take work whose acceptance nothing independent can check. So the property that gets selected out of the human cut is warrant, not predictability, and the residue is defined by what current oracles, representations, and settled criteria cannot reach.

## Why the residue is a selection effect, not a capacity claim

The list of what people still supply in a human-inclusive system — choosing demands, supplying unrecorded premises, interpreting ambiguous results, authorizing changes, repairing failures beyond the represented path — reads like a catalogue of essentially human work. Under this claim it is a residue: the decisions that resisted the last round of warranted transfer. Each entry names a warrant gap, not a human faculty. That reading stays consistent with the observation that a program-specific theory has to be held by *something* for coherent modification; it denies that the current shape of the human cut is evidence about what that something must be.

The consequence for how the residue looks over time: warranted transfer does not merely shrink the human cut set. It changes its composition toward the decisions that are most expensive to warrant. Moving the next decision out therefore costs more than moving the last one, even with a fixed incoming workload. This is a different mechanism from the elastic backlog that [relocates human attention to the frontier](./increasing-computational-autonomy-relocates-human-effort.md): that mechanism needs new work to arrive; this one operates on the work already present.

## Consequences for closure

Stacking bounded automation mechanisms does not approach an empty human cut set asymptotically. Each mechanism takes the warrantable slice within its reach and stops at the point where warrant fails, and the slices it leaves are, by construction, the ones no similar mechanism will take. Closure over a declared path is therefore decided at the least-warrantable decisions on that path, which is to say at the evaluator: the automatic system can take those decisions only when an oracle independent of the candidate can check them.

This makes several ways of faking closure legible as one move. A captured evaluator, a viability-only gate, and a boundary that quietly exports a hard decision to a person outside the declared system all supply *apparent* warrant at exactly the decisions where real warrant is missing. They are not separate mistakes; they are the selection effect being hidden rather than paid for.

The same reasoning bounds the tool-usefulness payoff of transfer. Leverage — accepted outcomes per unit of human effort — can rise while the human's remaining decisions become harder, less routine, and less connected to the day-to-day operation of the system. A person left with only the decisions that cannot be checked, and less contact with the routine cases that used to inform them, is in a worse position to make those decisions well. Removing a human judgment can therefore lower the quality of the judgments that remain, which is one mechanism behind the rule that a transfer needs a warrant comparison and not only an autonomy record; evidence that reviewers who see only escalated cases judge them as well as reviewers who also see the routine ones would defeat it.

## Reading the residue as a work list

Because each residual decision names a warrant gap, the human cut set can be classified by the reason each decision resisted transfer, and the reason names the mechanism that has to grow before it can move:

| Why the decision stayed human | What has to grow before it can move |
|---|---|
| A premise it needs is not represented anywhere the system can read | Representation: the premise has to be externalized and made addressable |
| The criterion is unsettled; the method says "use judgment" or names an approver | Settlement: methodology or objective has to supply the criterion, not the decider |
| No oracle independent of the candidate can check the result | Verification: oracle construction, decorrelated checks, or error-cost tolerance |
| The decision falls after the declared automatic horizon ends | Horizon: path continuity, so the executor is still running when the decision arises |
| Transfer is possible but costs more than continued human judgment | Nothing structural; the transfer is available and has been priced out |

The last two rows are not warrant gaps in the strict sense. A decision that falls outside the horizon may be fully warrantable within a longer one; the horizon trick is calling a path closed by cutting it just before such a decision. A decision that is merely uneconomic marks a claim that could be moved for evidence, if the experiment were worth its price.

## Scope

- The claim compares the human cut set before and after selective transfer under a fixed boundary, objective, horizon, and incoming workload. New work, or a policy that deliberately keeps routine decisions with people, can offset or reverse the shift.
- Warrantability is relative to the available representations, oracles, and settled criteria. The same decision can be warrantable in one system and not in another, and a transfer can regress when an oracle proves to be a weak proxy.
- The selection condition is *preferential* transfer of warrantable decisions. A system that moves decisions on some other basis — cost alone, or whatever an unattended model will attempt — does not satisfy the condition and the residue prediction does not follow; bare autonomy of that kind is free and produces a differently shaped residue.
- The claim predicts enrichment, not purity. Warrantable decisions can remain with people because moving them is uneconomic, and residual human decisions can contain checkable substeps.
- The mechanism does not establish how often real systems satisfy the selection condition. Evidence that deployed systems usually transfer without favoring warrantable decisions would defeat a prevalence claim built from it, not the conditional.

## Open Questions

- Whether the classification table can be applied to a recorded human cut set from repository history, giving a cheap first test of the composition shift.
- Whether the tool-usefulness consequence is observable at small scale: does a reviewer who sees only the escalated cases judge them worse than one who also sees the routine ones?

---

Relevant Notes:

- [Codifying predictable choices leaves agents with less predictable work](./codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) — mechanism: the selection effect this note transfers from the agent–code boundary to the human cut, with the selector changed from predictability to warrant
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: supplies the representation–settlement–warranted-execution conversion whose three parts define warrantability here
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why verification is the binding condition and why bare autonomy does not satisfy the selection condition
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: defines the human cut set and the contraction endpoint this note says gets harder to reach per decision
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — contrasts: the elastic-backlog mechanism needs new work to arrive; the selection effect changes the residue's composition with the workload held fixed
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: the structural reason the residue concentrates where oracles are weakest
- [Each residue class needs a different mechanism, so a self-improving architecture must be mixed](./residue-classes-need-different-mechanisms-so-architecture-is-mixed.md) — extends: develops the residue table into an architectural requirement: each class names a capacity supplied by a different part
- [A method's ceiling bounds the method, not the transfer it already made](./a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md) — extends: a bounded mechanism's ceiling bounds its method, not the responsibilities it already took
- [A benchmark that holds the client fixed exports the least-warrantable decisions by design](./holding-the-client-fixed-exports-the-least-warrantable-decisions.md) — extends: applies the residue classes to benchmark construction: a fixed client exports the unsettled-criterion and no-check rows
- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](./usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) — extends: generalizes the tool-usefulness consequence into a four-way separation of progress dimensions
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md#compatibility-is-assessed-per-portion-of-a-path) — extends: reads the residue on the production axis — the portion of a path an independent oracle reaches is the portion search can govern, so the residue is where nothing can yet select
