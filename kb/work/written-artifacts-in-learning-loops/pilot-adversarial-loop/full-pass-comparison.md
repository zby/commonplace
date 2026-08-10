# Full-pass comparison

## Outcome

The 716-word full-pass revision beat its 1,054-word multistage input **3–0** under the pilot's fixed commission and rubric. Two judges received the multistage version first; one received the full-pass version first. All three preferred the full-pass version, found no hard-constraint failure, and judged its context cost justified.

The result is attached to the exact evaluated snapshot, [candidate-full-pass-v1.md](./candidate-full-pass-v1.md), not to the later live candidate. The source-grounded [full-pass acceptance review](./full-pass-acceptance-v1.md) passed that snapshot.

## Comparison chain

| Version | Words | SHA-256 | Pairwise result |
|---|---:|---|---|
| [Library incumbent capture](./original.md) | 765 | `fcdea461ebd3c498e06ad7d5bab9309599f4aaa647768ba29bf7e0e9e6d9193a` | Lost 0–3 to the multistage candidate in the [earlier comparison](./blind-comparison.md) |
| [Multistage candidate](./candidate-pre-full-pass.md) | 1,054 | `a04bb30d6c7fb2eb81a6ee2f9a58cfe974744c572ea17bc535eb210c4d9eef28` | Beat the incumbent 3–0; lost to full-pass v1 0–3 |
| [Full-pass v1](./candidate-full-pass-v1.md) | 716 | `932a44dce42b479559ce0697051edaec7229f1249cd1b8c2c0e53dfde0d6a0c6` | Beat the multistage candidate 3–0 |
| [Final targeted revision](./candidate.md) | 805 | `f77ff52bcdbfec18bd81e8c8db567aa2d9c034c5535e828f61c088316a6029b7` | Not re-balloted; preserves the winning claim while repairing closing-review findings |

This is a chain of two pairwise experiments, not proof of transitive preference. There was no direct incumbent-versus-full-pass ballot.

## Blind judgments

| Judge | Packet order | Decision | Mapped preference |
|---|---|---|---|
| [Judge 1](./full-pass-judge-1.md) | multistage, full pass | VERSION 2 | full pass |
| [Judge 2](./full-pass-judge-2.md) | full pass, multistage | VERSION 1 | full pass |
| [Judge 3](./full-pass-judge-3.md) | multistage, full pass | VERSION 2 | full pass |

The anonymous inputs are retained as [packet A](./full-pass-blind-packet-a.md) and [packet B](./full-pass-blind-packet-b.md).

All judges gave full-pass v1 its largest advantages in warranted contribution, reader usability, and context efficiency. All gave the multistage version an advantage in grounding/calibration or boundary handling. Their average scores make the trade-off visible, although the rubric treats scores as routed attention rather than a mechanical decision rule:

| Rubric dimension | Multistage | Full-pass v1 |
|---|---:|---:|
| Warranted contribution | 3.67 | 5.00 |
| Claim precision | 4.67 | 4.00 |
| Mechanism and inference | 4.33 | 4.33 |
| Grounding and calibration | 5.00 | 4.00 |
| Boundary handling | 5.00 | 4.00 |
| Reader usability | 3.33 | 5.00 |
| Context efficiency | 3.00 | 5.00 |

## What the full pass improved

- It replaced the over-defensive “auditable attempts only” center with a more useful distinction: one independently adjudicated local correction does not validate a method across cases.
- It removed 338 words while retaining the record contract, role allocation, critic evaluation conditions, outcome distinctions, and missing completeness criterion.
- It made the governing claim easier to retrieve and cite.

## What closing review found

The full pass's own closing critique and friction found that v1 required adjudication of the fault but did not explicitly require adjudication that a revision or narrowing resolved it. Prose review also found that the note moved from human writing practices to distributed handoffs without stating the analogy's limited basis.

The final targeted revision repairs those findings. It:

- requires adjudication of both the fault and the final response;
- defines independent adjudication as a separate role applying a stated criterion, not merely a different actor;
- limits the human-writing analogy to motivation for candidate recorded handoffs, not preservation of epistemic effects;
- narrows critic discrimination to critic reliability rather than making it necessary for every whole-loop reliability claim; and
- retains the three-stage taxonomy as explicitly candidate and unvalidated.

The final revision was not put through another blind ballot because it preserves the winning contribution and changes only conditions that the closing checks found under-specified. Its fresh semantic, friction, sentence, source-bridge, and acceptance results are recorded in [final review summary](./final-review-summary.md).

## Decision boundary

The experiment selects [candidate.md](./candidate.md) for human promotion consideration. It does not promote, replace, or rename the library note.
