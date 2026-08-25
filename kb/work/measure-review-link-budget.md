# Handoff: measure what a review actually opens

Standalone task, no workshop. Implements the measurement half of
[Review link budget prices reviewer attention](../reference/proposals/review-link-budget-prices-reviewer-attention.md).
Delete this file when the measurement lands and the numbers are recorded.

## What to build

**Measurement only. Change no review behavior, edit no gate, stale no pairs.**
The point is to learn what reviews cost before any cap moves.

Two surfaces, both reusing what exists:

1. **A size column in the prompt's resolved-link table.** `resolved_links` in
   `src/commonplace/review/protocol/prompt.py` is already code-generated per
   target and already emitted into every prompt. Add the size of each resolved
   local target. V1 charges **whole files** — route-aware partial charging (a
   Quotes-route ingest reads one section; a `(snapshot required)` link opens the
   snapshot, not the ingest) is a known TODO, and its mispricing is recorded in
   the proposal.

2. **Recorded cost per completed job.** `review_jobs.telemetry_json` already
   exists for "opaque harness telemetry without making it review identity" — the
   right channel, and no schema change. Record what the reviewer reports opening:
   distinct artifacts and total bytes.

## What the numbers are for

The proposal's heuristic is `attention ≈ α · artifacts + β · bytes`. The ratio
α/β is the design question and is currently unmeasured; at β→0 it is today's
count, at α→0 it is a pure byte cap. Nothing in the corpus says where between
them the truth sits, so the measurement exists to supply it rather than to have
it chosen.

Useful to capture per pair: distinct artifacts opened, bytes over those
artifacts, how many resolved links went unopened, and whether the reviewer said
it stopped for budget reasons or because it had enough.

## Constraints

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
