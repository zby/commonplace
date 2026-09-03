---
description: "Holding a program's theory is tested by whether a partial, fallible account of what the program is for keeps modification search, backtracking, and recovery coherent until delayed evidence arrives, not by whether the first change is right"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Holding a program theory means sustaining coherent search under delayed feedback

Peter Naur's essay *Programming as Theory Building* asks what someone who holds
a program's theory must be able to do. His hardest test of that holding is
coherent modification: change the program for a new demand without destroying
the structure and purpose that make the program work. A separate argument,
about which decisions automation leaves behind, reaches the same decision from
the other side. Decisions whose premises are written down, whose criteria are
settled, and whose results are cheap to check move to machines first. What
stays with people is the residue: decisions no complete rule, settled local
criterion, or cheap independent check already determines. On an open-ended
modification path, the least-warrantable decision in that residue is which
change preserves the program's structure and purpose. Naur's test names the
capacity a theory-holder needs; the transfer argument explains why the same
decision stays with people.

Meeting that test does not require a theory strong enough to deduce the right
change in one step. A working program theory may be partial, imprecise, and
fallible. It counts because it keeps modification search coherent: it shapes
which changes are considered, what must be preserved, how failures are
interpreted, when to backtrack, and what should be revised. Searching, failing,
and backtracking are therefore not signs that the theory was missing.

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

Two differences separate theory-guided search from mutation with
backtracking, once both are granted the same budget. The first is update
bandwidth. Backtracking needs an address: which earlier commitment is at fault
for a late failure, and what replaces it? An accept-or-reject result on an
undirected candidate says little about which earlier commitment is at fault,
while the space of revert-point and alternative pairs grows combinatorially
with sequence length. One surprising consequence read against a theory can
single out a specific commitment as at fault and revise a whole region of that
space at once. Where trials are few, slow, and expensive, that asymmetry is the
regime argument for theory.

The second difference is the failure signature. Undirected search fails in no
consistent direction: its errors differ from one episode to the next. A wrong
theory fails coherently, bending successive changes the same wrong way, as
[broad negative transfer from a broad wrong
theory](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
predicts. If that prediction holds, a test that replaces the theory with a
plausible wrong one discriminates better than one that withholds it:
directional failure would show the theory was steering. The prediction has not
been tested here; how large the effect must be is an open question below.

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
open-ended modification path, the residue concentrates at the question Naur's
modification test poses: which change fits the program's world, purpose, and
organization when no finite rubric settles the case?

The two descriptions coincide:

- **Bearer side:** the actor holds the theory well enough to modify coherently
  across new demands.
- **Boundary side:** the actor carries the least-warrantable modification
  decision through search, delayed evaluation, recovery, and retained revision
  without passing the decisive judgment to another actor.

The identity holds for this decision, not across every residue class. An absent premise,
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
- How large must the wrong-theory effect be, and over how many episodes, to
  separate directional failure from ordinary variance when both arms
  eventually find an acceptable change?
- How should delayed evidence receive credit when several changes and theory
  revisions intervene before the consequence appears?

---

Relevant Notes:

- [Naur binds program theory to humans by equating machine execution with formulated criteria](./naur-equates-machine-execution-with-formulated-criteria.md) — grounds: supplies Naur's bearer tests and leaves their satisfaction by a composite empirical
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the selection effect and least-warrantable residual identified with coherent modification here
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: supplies the functions through which a fallible theory guides modification
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: requires the same theory to guide change, receive outcome read-back, be revised, and affect later operation
- [Citing retained theory at the decision point is a mediation trace](./citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — enables: records which theory was consumed while leaving load-bearing use open
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — grounds: identifies program-specific premises generic search cannot reliably reconstruct
- [A repeatable operative path keeps a redesign class open to revision](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — extends: supplies continuity and executable recovery across later episodes
- [Open-ended improvement must allocate search before decisive evaluation is available](./open-ended-improvement-allocates-search-before-evaluation.md) — grounds: establishes the prior allocation problem that makes program theory useful before the strongest evidence exists
- [A failure explanation becomes search control only when it changes a later branch decision](./failure-explanation-changes-later-branch-decisions.md) — mechanism: makes outcome read-back operative by requiring retained failure interpretation to change a later branch choice
- [A search controller is tested by what it brings to stronger evaluation](./a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — extends: supplies a matched downstream evaluation design for separating theory-guided routing from generic search without assuming exhaustive counterfactual search
- [Theory-mediated learning may improve sample efficiency under shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: predicts the directional negative transfer that makes a wrong-theory arm the discriminating test
- [The 2026-08-30 Commonplace revision used retained theory to guide computational search](./evidence/commonplace-revision-used-theory-guided-computational-search.md) — evidenced-by: records one human-inclusive case while preserving the missing ablation and longitudinal-track-record limits
