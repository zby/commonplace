# Frame and objective declaration

Posed 2026-11-20 by the operator (Zbigniew Lukasiak), as a direction, not an
agent proposal. Agents have given the operator different remedies for the same
finding. The operator wants one settled rule for the whole KB, not a repair of
one note.

## Goal

Settle how a KB artifact that makes a claim about Commonplace itself states the
parameters that claim depends on: the system boundary, the human/computational
partition, the assessment horizon, the improvement objective, and inputs that
cross the boundary. The result is one rule, its owner artifacts, and the edits
that apply it.

## Refocus, 2026-11-20

The workshop began as a question about declaring the frame. A side
investigation and the operator's direction moved its centre to how progress is
claimed at all: on the margin, in a declared area, as a conjecture about an
unspecified total order that the objective names. The decision points below
remain the record of the first question; [the plan](./plan.md) and the
operator-direction section of [the settlement record](./settlement.md) state
the current one.

## What prompted it

An agent review of [Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md)
reported that the note cites [the declared Commonplace frame](../../reference/commonplace-declared-frame.md)
only in its footer while its body treats the maintainer inconsistently. The
review proposed restating the frame in the body. A second agent disputed both
the diagnosis and the remedy. Both are recorded under `positions/`.

## Settled background

These are not in dispute and need no re-derivation:

- The [self-improving system](../../theory/definitions/self-improving-system.md)
  definition reads an attribution against a declared boundary, horizon and
  objective.
- The declared Commonplace frame fixes the boundary and the partition. It says
  the horizon is declared per attribution. It does not state the objective.
- The objective, "more useful and better-warranted knowledge work per unit of
  human judgment spent", is stated at `commonplace-as-an-instrument.md:11` and
  repeated in [ablation baselines](../../reference/proposals/ablation-baselines-for-the-declared-objective.md)
  and [reusable commitment support](../../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md).
- [The closure note](../../theory/methodological-and-computational-closure-track-different-changes.md)
  already lists what closure evidence must declare: task selection, objective,
  boundary, permitted inputs, horizon, resource limits and treatment of
  failures, with the seed declared separately from run-time intervention.

## Decision points

A position answers each point or says it takes no view. Settlement is per
point; positions need not win or lose whole.

| # | Question |
|---|---|
| D1 | Does the instrument note move the maintainer across the boundary, or does it only use "components" in a sense that collides with the frame note's? |
| D2 | Does a note that depends on the frame restate it in the body, link it where the dependent term is first used, or keep a footer link? |
| D3 | Is the human-inclusive boundary the cause of the repeated declarations, or would any boundary choice owe the same declarations for an effectiveness claim? |
| D4 | Which human judgment does the objective's denominator count: per-task operation only, or also judgment spent building and maintaining the methodology? How is model strength treated? |
| D5 | Where is the objective declared: the instrument note, the frame note, or a new artifact? Do the two proposal copies become citations? |
| D6 | Does the frame note's "Using the frame" section cover claims that credit an outcome to one side of the partition or to the system rather than to outside inputs? If so, what does it say such claims owe? |
| D7 | Does "frame" name boundary, horizon and objective together (tag head) or the boundary and partition only (frame note)? Which surface changes? |
| D8 | Is the settled rule enforced: nowhere, in `cp-skill-write`, or by a review criterion? |

D4 is a commitment about what Commonplace optimizes. Agents may argue it; only
the operator decides it.

## Positions

Each agent with a distinct remedy adds one file under `positions/`, named
`<letter>-<short-name>.md`, following [the position format](./positions/README.md).
Do not edit another agent's position; answer it in your own file under
"Against other positions".

- [A — restate the frame in the body](./positions/a-restate-frame-in-body.md)
- [B — complete the owner declarations and cite them](./positions/b-single-owner-declarations.md)
- [C — B's rule, with local statement of what was observed](./positions/c-declare-shared-state-observed-locally.md)
- [D — rule D4, test the instrument note, and shrink the workshop](./positions/d-shrink-to-the-objective.md)

## Evaluation boundary

- A position is assessed on the whole KB, not on the instrument note alone.
  The first candidate set is every artifact that links the frame note or
  repeats the objective sentence; a position may widen it and should say why.
- A proposed rule is tested by applying it to that set. Report which artifacts
  it changes, and whether the change removes a misreading a cold reader would
  otherwise make. A rule that changes nothing a reader could get wrong is not
  earning its cost.
- Agreement between agents is not evidence. A point is settled by an argument
  the other side accepts, a discriminating check on the corpus, or the
  operator's ruling.
- Do not edit the disputed library artifacts while their decision points are
  open: `commonplace-as-an-instrument.md`, `commonplace-declared-frame.md`,
  the two proposals named above, and `kb/tags/self-improving-systems-README.md`.
  Edits outside those points are unaffected.
- New theory is out of scope unless a decision point cannot be settled without
  it. The boundary theory already exists; this workshop is about declaration
  and citation practice.

## What closes it

1. Every decision point is marked in [the settlement record](./settlement.md)
   as agreed, ruled by the operator, moot because no edit depends on it, or
   deferred with a named trigger.
2. The agreed edits are applied to the library artifacts and validated with
   `commonplace-validate`.
3. Any rule that binds future writing is placed in its owner artifact.
4. The directory is deleted and its entry removed from `kb/work/README.md`.

## Bookkeeping

- [`software-house-investigation.md`](./software-house-investigation.md) is a
  side investigation of what the automated software house definition supplies.
  It questions whether the objective should stay one ratio, which bears on D4,
  and reports that the frame note's boundary is partly person-based.
- [`plan.md`](./plan.md) is the working plan: the rule, what gates each step,
  and the edits. It changes as points settle.
- `positions/` holds one file per position, owned by its author.
- `settlement.md` is the shared record; anyone may update a row, with a date
  and the basis.
- Commits carry `Workshop: kb/work/frame-and-objective-declaration`.
