# Handoff: measure what a review link budget would have to cover

Standalone task, no workshop. Implements the measurement half of
[Review link budget prices reviewer attention](../reference/proposals/review-link-budget-prices-reviewer-attention.md).
Delete this file when the measurement lands and the numbers are recorded.

## Two measurements, and only one is free

The phrase "measure what a review opens" hides two different things. They answer
different questions and cost differently. **Build the first. Do not build the
second without an explicit decision from the operator.**

### A. Available cost — deterministic, no behavior change

Size every resolved link at job-creation time and record what the review *could*
have opened. Nothing is asked of the reviewer, no prompt obligation changes, and
no verdict moves.

1. **A size column in the prompt's resolved-link table.** `resolved_links` in
   `src/commonplace/review/protocol/prompt.py` is already code-generated per
   target and already emitted into every prompt. Add the size of each resolved
   local target. V1 charges **whole files** — route-aware partial charging (a
   Quotes-route ingest reads one section; a `(snapshot required)` link opens the
   snapshot, not the ingest) is a known TODO whose mispricing is recorded in the
   proposal.

2. **Per-job available cost.** `review_jobs.telemetry_json` already exists for
   "opaque harness telemetry without making it review identity" — the right
   channel, and no schema change. Record the resolved link count, distinct
   artifact count, and total bytes available per pair.

This tells you the distribution of cost a budget would have to accommodate. It is
the whole of V1.

### B. Actual opens — needs a decision first, do not build unprompted

What a reviewer *actually* opened is known only to the reviewer. Capturing it
means adding to the gate or to the reviewer output contract, and **that is a
behavior change even though no verdict moves.** Today nothing asks for it: the
gate has no such instruction and the output contract has no such field. Review
job 8051 disclosed its four unopened links on its own initiative, not because
anything required it.

B is the measurement that actually yields α/β, because it says where reviewers
stop. A only says what they were offered. So B is the more valuable half and the
more invasive one, which is exactly why it is the operator's call and not the
implementer's.

**If you reach this point, stop and ask.** Do not extend the output contract to
get better numbers. Report what A shows and what B would add.

## What the numbers are for

The proposal's heuristic is `attention ≈ α · artifacts + β · bytes`. The ratio
α/β is the design question and is currently unmeasured; at β→0 it is today's
count, at α→0 it is a pure byte cap. Nothing in the corpus says where between
them the truth sits, so the measurement exists to supply it rather than to have
it chosen.

Under A, capture per pair: resolved links, distinct artifacts, and total bytes
available. Under B — only if authorized — distinct artifacts opened, bytes over
those, links left unopened, and whether the reviewer stopped for budget reasons
or because it had enough.

Note the limit honestly: **A alone cannot fix α/β.** It bounds the problem and
shows the shape of the corpus; it does not observe a stopping point. Say so in
whatever you report, rather than presenting available cost as if it were
consumed cost.

## Constraints

- **Scope of "no behavior change": verdicts and the gate.** Do not edit
  `semantic/grounding-alignment`, do not change any outcome, do not stale pairs.
  Adding a size column to a generated prompt is inside that boundary; adding an
  obligation on the reviewer is not.

- **Do not add rules splitting evidence into classes.** Operator decision
  2026-08-25: the budget stays global. An earlier sketch proposed ranking source
  links above internal ones; that is superseded and should not return.
- **Price, do not choose.** Sizing reports cost. Which links carry a target's
  load-bearing claims is judgment and stays in the gate; moving it into code
  reintroduces the classification rule just ruled out.
- **Dedupe in code.** Resolve links to targets and charge each distinct artifact
  once. 239 of 314 linked notes repeat a target, so this is the common case, not
  an edge one. Doing it in code is what removes the defect mechanically instead
  of describing it in an instruction.
- Report unavailable targets rather than erroring — a missing file, or a
  `(snapshot required)` link whose snapshot is absent. ADR 073 already makes the
  latter a gate FAIL; sizing should not duplicate that judgment.

## Two questions to answer with the data, not before it

- Would a derived budget be exceeded often, or rarely? That decides whether
  [enforcement](../reference/proposals/review-budget-enforcement-is-separable.md)
  needs machinery at all.
- Does artifact count or byte volume better explain where reviewers actually
  stopped? That is α/β, and it is the whole point.

## Background

The defect that started this is recorded in
[the link-budget note](./claim-grounding-rollout/grounding-alignment-link-budget.md):
the gate caps link occurrences where the resource is attention, and editing it
stales 775 pairs, so the counting rule, the number, and the ingest-scope question
should land in one later pass — not this one.
