# Workshop: gate-refactor

Goal: move reviews from monolithic bundle documents to individual gate files with gate-level staleness.

## Prior work

- Earlier selector-refactor analysis established the need for gate-local freshness and explored a more elaborate storage model that was later simplified away.
- [selector-loaded review gates](../../notes/selector-loaded-review-gates-could-let-review-revise-learn-from.md) — how review-revise discoveries become reusable gates

## Files in this workshop

- [design.md](./design.md) — the simplified gate system design
- [implementation-plan.md](./implementation-plan.md) — concrete steps to build it
- [current-bundles.md](./current-bundles.md) — prior analysis of bundle fate (superseded by design.md)
- [migration-plan.md](./migration-plan.md) — prior phased plan (superseded by design.md)

## Design decisions (2026-03-26)

### Review and application are separate stages

Review produces findings. Application (revision) decides what to do with them.

- **Reviewer** sees the note + gate instructions. Outputs findings.
- **Applicator** sees the note + all findings from all reviews. Decides priority, resolves conflicts, makes edits.

Reviewers stay focused on detection. The applicator holds the "what matters most" frame.

### Aspirational qualities belong in the applicator, not in gates

A gate is a **check** — it detects a specific quality failure. Aspirational directives like "prefer changes that increase generality over internal consistency" are **applicator directives** — they shape how the applicator prioritizes the pile of findings.

### No backward compatibility

This is experimental. No legacy adapters, no migration phases, no wrapper preservation. Delete the old bundle reviews and start fresh with gate files.
