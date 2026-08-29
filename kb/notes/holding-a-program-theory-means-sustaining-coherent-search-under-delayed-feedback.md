---
description: "At the least-warrantable point of open-ended program modification, Naur's coherent-modification test asks whether a fallible program-specific theory can keep search, backtracking, and revision coherent until delayed evidence arrives"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Holding a program theory means sustaining coherent search under delayed feedback

At the decisive point of an open-ended programming path, Naur's
**coherent-modification test** and the residue model's
**least-warrantable modification decision** are the same problem viewed from
opposite sides. Naur asks what capacity a theory-holder must have: can it change
the program for a new demand without destroying the structure and purpose that
make the program work? The residue model asks why that decision remains human:
no complete rule, settled local criterion, or cheap independent oracle already
determines which change preserves that structure and purpose.

This does not require a strong theory that deduces the right change in one
step. A working program theory may be partial, imprecise, and fallible. It
counts because it keeps modification search coherent: it shapes which changes
are considered, what must be preserved, how failures are interpreted, when to
backtrack, and what should be revised.

## Theory guides search rather than replacing it

A theory-holder may inspect the system, construct alternatives, test
assumptions, make a tentative change, encounter a conflict, reverse course, or
revise its account of what the program is for. Backtracking is not evidence
that the theory was absent. It is one way a fallible theory is used under
incomplete information.

The theory supplies program-specific control over search:

- it narrows candidate changes and identifies commitments a local fix must not
  silently destroy;
- it gives unexpected results an interpretation;
- it helps distinguish evidence against a candidate from evidence against the
  theory; and
- it tells recovery what to restore or revise.

Generic search can also generate and test changes. The difference is causal:
the program theory must shape proposal, evaluation, recovery, or revision. A
retained theory that affects none of them is inert. The relevant architecture
is therefore a
[proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
in which theory guides search and interpretation rather than serving as a
complete generator of answers.

## Warrant belongs to the path, not the first proposal

For the decision at issue, decisive evidence is often delayed: a later demand,
a failed extension, an operational problem, or consequences visible only after
use. At the moment of commitment, neither a human nor a computational actor
necessarily has an independent proof that the change is coherent.

The human standard is therefore longitudinal:

    partial program theory
      -> theory-guided search
      -> provisional evaluation
      -> tentative change
      -> delayed or external consequences
      -> retain, backtrack, repair, or revise
      -> updated theory and later modification

A failed first candidate can belong to coherent modification when the process
recognizes the failure, recovers, and revises in response to the evidence. A
successful first candidate can fail the test when it passes a narrow check
while damaging the program's organization in a way the process cannot detect.

The initial decision may be weakly warranted. The modification process earns
warrant through a track record under refuting exposure, including its capacity
to detect mistakes and recover from them. Outcomes must be read back against
the theory and affect later operation, as required by a
[causally co-indexed theory-mediated path](./theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## The bearer test and the hardest residual coincide

[Warranted transfer leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
because represented, settled, cheaply checkable decisions move first. On an
open-ended modification path, the residue concentrates at the question Naur
uses as his third bearer test: which change fits the program's world, purpose,
and organization when no finite rubric settles the case?

The two descriptions coincide:

- **Bearer side:** the actor holds the theory well enough to modify coherently
  across new demands.
- **Boundary side:** the actor carries the least-warrantable modification
  decision through search, delayed evaluation, recovery, and retained revision
  without exporting the decisive judgment.

The identity is at this crux, not across every residue class. An absent premise,
missing authority, or truncated horizon may block the path before coherent
modification is attempted. Nor does the identity make coherent modification an
essentially human capacity. It says that a computational composite must carry
the same functions by which the human process is warranted, not imitate a
human's first answer.

## What a computational test should require

A theory-possession test should cover novel modification demands and recovery,
not one accepted edit. For a declared program, boundary, and horizon, it should
show:

1. program-specific theory and otherwise-unregenerable premises available to
   the modifying process;
2. search or recovery that changes when that theory is withheld or replaced;
3. provisional checks capable of rejecting some candidates;
4. executable realization, rollback, and backtracking paths;
5. consequences not authored solely by the candidate process; and
6. outcome read-back that revises theory or machinery and changes a later
   modification episode.

A contemporaneous
[mediation trace](./citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
records which theory the process claims to have used. Withholding or replacing
the theory is stronger evidence that its use was load-bearing.

Self-evaluation is not automatically captured evaluation: a theory-holder may
make provisional judgments about its own candidates. Evaluation becomes
captured when no outside consequence can overturn the candidate, trigger
recovery, or revise the theory.

## Scope

- The claim concerns open-ended modification where no complete specification
  and cheap oracle settle the result. Where both exist, the problem has moved
  into a narrower, more warrantable automation envelope.
- A program theory may be distributed across retained artifacts, learned
  competence, tools, and participants; it need not be a complete proposition
  set or one document.
- Search and backtracking are not sufficient evidence of theory possession.
  Random mutation does both. The program-specific theory must shape the path.
- One successful modification does not establish the disposition. The test is
  a track record across later demands, including cases that expose an error.
- The equivalence is relative to task selection, objective, boundary, and
  horizon; changing them can change which decision is the hardest residual.

## Open Questions

- What task distribution and horizon distinguish coherent modification from
  luck, memorization, or a permissive evaluator?
- How can theory-guided search be separated empirically from generic search
  when both eventually find an acceptable change?
- How should delayed evidence receive credit when several changes and theory
  revisions intervene before the consequence appears?

---

Relevant Notes:

- [Naur binds program theory to humans by equating machine execution with formulated criteria](./naur-equates-machine-execution-with-formulated-criteria.md) — grounds: supplies Naur's bearer tests and leaves their satisfaction by a composite empirical
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the selection effect and least-warrantable residual identified with coherent modification here
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: supplies the functions through which a fallible theory guides modification
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: requires the same theory to guide change, receive outcome read-back, be revised, and affect later operation
- [Citing retained theory at the decision point is a mediation trace](./citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — enables: records which theory was consumed while leaving load-bearing use open
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — grounds: identifies program-specific premises generic search cannot reliably reconstruct
- [A repeatable operative path keeps a redesign class open to revision](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — extends: supplies continuity and executable recovery across later episodes
