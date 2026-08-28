---
description: "Why preferential transfer of the checkable decisions lowers the quality of the human decisions left behind: the routine cases carried the calibration and the premises those decisions needed"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Removing a human judgment can degrade the judgments that remain

Moving a decision out of the human cut set is normally scored as a gain, because the same person then supplies fewer judgments per completed unit of work. That score assumes the judgments the person still makes are as good as they were before the transfer. Under one identifiable transfer policy the assumption fails.

The policy is preferential transfer of the checkable decisions: the system moves out the decisions whose results an independent oracle can check, and keeps the rest, [since warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md). That parent claim is about composition — the residue is harder to warrant per decision. This note adds a second effect on the same residue: those decisions are now made under worse conditions than before, because the cases that left were supplying part of the conditions.

## Two mechanisms

**Loss of calibration.** The routine cases were the sample from which the person learned what a normal case looks like. Judging an exception means judging a distance from normal, and that distance is read against a base rate the person holds from having seen the ordinary run of cases. When the routine cases stop reaching the person, the base rate stops being refreshed. It then ages as the incoming population drifts, and the person keeps applying an old sense of normal without a signal that normal has moved.

**Loss of context.** A hard decision usually needs premises that are not in the case record: which upstream step tends to produce this shape of input, what was already tried on similar cases this week, which part of the system was recently changed. When the person also handled the surrounding routine work, those premises arrived as a by-product of doing it. After the transfer the escalation delivers the case but not the work that carried its premises, so the decision is encountered cold. The person can reconstruct some of the missing context on demand, but reconstruction costs effort and reaches only the premises the person knows to ask for.

Both mechanisms operate with the incoming workload held fixed. Neither needs new work to arrive.

## Leverage and judgment quality can move in opposite directions

Leverage — accepted outcomes per unit of human effort — counts outcomes and human effort. It does not read the quality of the judgments the human still supplies. Under the two mechanisms above, a transfer can raise leverage and lower that quality at the same time, so leverage alone cannot tell the two apart. The same holds for an autonomy record that reports how far the automatic path ran unattended and how many human judgments each completed outcome required.

This is why a transfer needs a warrant comparison and not only an autonomy record. The comparison has to state, before and after, which decisions were made by whom, on what evidence, and checked against what — and it has to include the human's remaining decisions on both sides. A comparison that scores only the transferred decisions will show the automatic path checked and the leverage improved while the degradation sits entirely outside what was measured.

This is a different mechanism from the elastic backlog by which [increasing computational autonomy relocates human effort to the frontier](./increasing-computational-autonomy-relocates-human-effort.md), and it is the second half of the monitoring irony that note cites. The relocation mechanism needs new work to arrive: attention freed from routine work moves to harder work that was previously going unattempted, and the person's total hours stay put. The mechanism here needs no new work at all. Hold the incoming workload fixed and the degradation still follows, because it comes from what the person stopped seeing rather than from what the person started doing.

## What would defeat this

The claim predicts a difference between two reviewers facing the same escalated case: one who also handles the routine cases from the same stream should judge it better than one who sees escalations alone. Evidence that the two judge escalated cases equally well, over a case population where the routine and exceptional cases share a generating process, would defeat the mechanism rather than merely bound it. Evidence that the gap exists but closes quickly once the escalation carries a summary of recent routine cases would leave the mechanism intact and reduce it to a solved design problem.

## Scope

- The claim is conditional on preferential transfer of the checkable decisions. A system that transfers on some other basis — cost alone, or whatever an unattended model will attempt — does not satisfy the condition, and the residue it leaves has a different shape, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).
- The claim is about the default, not the mitigated case. Sampling routine cases back to the person, attaching the relevant recent history to each escalation, and rotating people through the routine stream each attack one of the two mechanisms. Each also spends part of the leverage the transfer was made for, so the mitigated case is a priced choice rather than a free repair.
- The calibration mechanism assumes the routine cases were informative about the exceptions. Where the exceptional cases are generated by a process the routine cases say little about, removing the routine cases costs little calibration and the context mechanism has to carry the claim alone.
- Degradation is measured against the same person's judgment on the same decisions before the transfer. The note does not claim that the remaining human judgment is worse than what the automatic path would produce on those decisions; by the selection condition, the automatic path has no warranted way to take them.
- The mechanism does not establish how often deployed transfers degrade the residue in practice. Evidence that they usually do not would defeat a prevalence claim built on this note, not the conditional.

## Open Questions

- The small-scale test named in the parent note: does a reviewer who sees only the escalated cases judge them worse than one who also sees the routine ones? A review queue with a recorded split of routine and escalated cases could supply a first answer cheaply.
- How much routine contact is enough. If a small sampled share restores calibration, the mitigation is cheap; if the requirement scales with the drift rate of the input population, it is not.
- Whether the two mechanisms separate empirically. Attaching recent context to escalations should repair the context mechanism without repairing calibration, which would make them independently testable.

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the selection condition and the residue composition this note's degradation claim is stated over
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — contrasts: the elastic-backlog mechanism needs new work to arrive, while this one operates with the workload held fixed
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why checkability is the property that selects which decisions leave the human cut
- [Preferential codification concentrates less predictable work at the agent boundary](./codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) — contrasts: the same selection shape one layer down changes which work is retained, without claiming anything about how well the retained work is then done
