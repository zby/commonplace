---
description: "Separates envelope expansion, where a responsibility leaves the residual human work, from performance gains inside a fixed envelope, so a bounded method reaching its ceiling does not retract the transfer it already made"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# A method's ceiling bounds the method, not the transfer it already made

Call a mechanism's **automation envelope** the set of responsibilities it can carry under stated conditions. A formatter's envelope holds formatting decisions. A compiler's holds the translation from source to machine code. A link validator's holds the check that a named target exists. Each envelope is narrow, and each is real: the responsibility inside it no longer has to be supplied by a person for the work to be accepted.

A bounded mechanism reaches a ceiling when improving it by its own method stops adding responsibilities to its envelope. A better formatter does not begin to design, debug, or maintain. At that point the rest of the residual human work becomes visible, because the transferred part no longer occupies attention. Visibility of the remainder is not evidence that the transfer was illusory. The ceiling is a fact about the method's reach, and it says nothing about whether the responsibilities already inside the envelope moved.

## Two kinds of progress, kept apart

The confusion this claim removes comes from scoring two different improvements on one scale.

**Envelope expansion.** A responsibility that a person had to supply is now carried by the mechanism under stated conditions. The set of decisions that remain human changes. Whether an expansion is warranted is a separate and harder question: it needs represented inputs, a settled criterion, and a check the candidate did not author, [since warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).

**Performance inside the envelope.** Output quality, reliability, input coverage, latency, or resource cost improves while the responsibility set is unchanged. Nothing moves across the boundary. This is still capacity change, [since learning is not only about generality](./learning-is-not-only-about-generality.md), and it is the trade [constraining and extraction make when they buy reliability, speed, or cost with generality](./constraining-and-extraction-both-trade-generality-for-reliability.md).

Under a fixed acceptance threshold, the two are disjoint by construction: expansion is defined by a change in the responsibility set, in-envelope performance by its constancy. So expansion is the kind of progress that changes which decisions remain human. The other kind still counts, on capability and yield — a formatter that stops corrupting files on unusual input has produced a real gain that no responsibility transfer explains.

## Two errors this rules out

The first error reads a ceiling backwards: because the method cannot reach further, the progress it made was not progress. This treats envelope expansion as the only currency and then denies even the expansion that happened, because what remains is larger than what moved. A responsibility that left the residual human work stays gone when the mechanism that took it stops improving.

The second error reads a ceiling as an end: because the method worked up to its ceiling, it is the way forward. This mistakes the envelope for the task. Improving the mechanism further will keep producing in-envelope gains and will not move the next responsibility.

Both errors are avoided by the same discipline. A progress record states what moved into the envelope and what stayed outside it, rather than reporting one number.

## Why ceilings are structural

The residual human work left after a round of transfer that prefers the decisions it can warrant is adversely selected: per decision it is harder to warrant than the work already transferred, because the mechanism took what it could warrant and stopped where warrant failed. The remaining decisions are missing a represented premise, a settled criterion, an independent check, or continuity past the declared horizon — different gaps, each needing a different capacity. That is why envelopes do not stack toward an empty human cut set, and why the ceiling is not an accident of the current implementation. Reaching the next responsibility usually requires a different mechanism, not a better version of this one, because the gap that blocks it is a gap this mechanism's method does not address. Where the gap is verification, the ceiling sits where checking does, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

This also explains why the second error is tempting. In-envelope improvement is cheap and legible; expanding to a responsibility whose warrant gap is unsolved is neither. A method that has just demonstrated a ceiling is exactly the method whose next increment is easiest to fund.

## Scope

- An envelope is relative to stated conditions — inputs, acceptance threshold, operating environment. A mechanism's envelope can shrink when conditions change: a formatter that carried its responsibility for one language does not carry it for a dialect it mishandles, and a checker can stop being trusted when its proxy is shown to be weak.
- Progress here is relative to a fixed task class and acceptance threshold. Comparing across task classes, or across a threshold change, mixes the two kinds again. Difficulty can also be reassigned upward, in which case an envelope that covered yesterday's task no longer covers today's, [as when scaling absorbs scaffolding at fixed difficulty but not at the deployment frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).
- The partition is clean only while the threshold is held fixed. A reliability gain can carry a responsibility across an acceptance threshold, and the same change then reads as expansion under the new threshold. The record should name which reading it is using rather than claim the change was one kind independent of the threshold.
- "The transfer is real" is a claim about the responsibility set, not about net benefit. A mechanism can take a responsibility and export more work into configuration, review, or repair than it removed. That is a bad trade with a real transfer in it, and it needs a separate accounting.
- Neither kind of progress is by itself evidence that later improvement got easier; that requires a traced feedback path, [as separated where improvements can accumulate without compounding](./improvements-can-accumulate-without-compounding.md).

## Open Questions

- Whether an envelope boundary can be measured rather than declared. The claim currently relies on the operator naming which responsibilities a mechanism carries; a test that reads the boundary off observed behaviour — the input classes where the mechanism's output is accepted without human repair — would make ceiling reports contestable.
- Whether the second error can be detected early from a progress record, for example by a run of consecutive improvements that report only in-envelope dimensions while the residual human work is unchanged.
- Whether the ceiling of a mechanism is better attributed to its method or to its warrant gap when the two disagree — a method could in principle be blocked by cost alone, which the residue classification treats as non-structural.

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the adverse selection that makes ceilings structural and explains why envelopes do not stack toward an empty human cut set
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: names where the ceiling sits when the blocking gap is verification
- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: the capacity dimensions along which in-envelope performance moves without any responsibility changing hands
- [Constraining and extraction can trade generality for reliability, speed, or cost](./constraining-and-extraction-both-trade-generality-for-reliability.md) — mechanism: how narrowing buys in-envelope gains while fixing the envelope's edge
- [Improvements can accumulate without compounding](./improvements-can-accumulate-without-compounding.md) — contrasts: partitions progress by whether an earlier benefit made later improvement more productive, where this note partitions it by whether the responsibility set changed
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — contrasts: the same fixed-task versus moving-frontier equivocation, read on scaffolding demand rather than on responsibility transfer
- [Codifying predictable choices leaves agents with less predictable work](./codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) — mechanism: the same selection effect one layer down, where the selector is predictability rather than warrant
