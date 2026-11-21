---
description: "When the same expected gain justifies an internal trial but not a public commitment, check which losses correction can stop and which survive it."
type: types/note.md
traits: [title-as-claim]
tags: [evaluation]
---

# Reversibility can favor a change by limiting future loss

Suppose a team can try an interface internally or publish it for other projects to use. The same expected gain may justify the internal change but not publication. Internally, a failing check could reveal a mistake and let the team revert before the next use. After publication, reverting could break programs written against the new interface. Trying the change with a way back is a different alternative from committing to keep it. An [on-balance judgment](./on-balance-judgments-can-guide-improvement-without-a-global-measure.md) can favor the trial without counting harm during the trial any less.

To bound the downside of a trial without listing every possible failure, ask three questions:

- **How soon could the team detect and correct a mistake?** A routing instruction takes seconds to delete, but an agent sent to the wrong note may never report why. The time to edit the instruction does not bound the time it will remain in use.
- **Which losses stop at correction?** Removing the instruction prevents further misrouting through it. It does not recover time already spent or repair a document written from the wrong instructions.
- **What will have come to depend on the change?** Callers can start using a published interface before the team discovers a fault. The cost of backing out then includes repairing those callers or supporting them during migration.

If losses accrue at most at rate `r`, correction stops them within time `t`, and reverting and repairing downstream damage costs at most `c`, the total loss is at most `r × t + c`. Each bound needs grounds. If the team cannot detect a silent failure or trace its downstream effects, the existence of a revert command supplies no such guarantee.

Can the team get the evidence it needs before making the commitment that is hard to undo? Under the [Commonplace article lifecycle](../articles/COLLECTION.md), readers can challenge a circulating draft while the author can still rewrite it. Once published, the article is a fixed record: a correction must remain visible rather than silently replacing what readers cited. A limited rollout offers a different protection: fewer people encounter a mistake, but the smaller audience does not make harm to those people reversible.

A team that keeps the internal change on these terms is judging that doing so will improve future work. Its ability to correct a mistake is a reason for that judgment today. Whether the retained change actually improved later work is a different question; rollback capability is not evidence of that gain.
