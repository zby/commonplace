# Related Systems

Reviews of external systems doing similar work — knowledge management for AI agents, context engineering, structured note-taking.

## Why we track these

Convergence across independent projects is a stronger signal than any single design argument. When three unrelated systems arrive at filesystem-over-databases, that's evidence. When one system makes a bet we haven't considered, that's a prompt to think harder.

## How to write a review

Use the template: `kb/notes/types/related-system.md`

The recurring structure: **what it is → core ideas → how it compares → what to borrow → what to watch.**

The "Borrowable Ideas" section is the most important deliverable. Each review should produce concrete candidates for adoption — not just "interesting" observations but things shaped enough to act on. For each borrowable idea, say what it would look like in our system and whether it's ready now or needs a use case first.

## Staleness

Reviews have a `last-checked` field in frontmatter. A review is stale when:

- The reviewed system has had a major release or architectural change since `last-checked`
- Our own system has evolved enough that the comparison section no longer reflects reality
- More than 3 months have passed without re-checking

Stale reviews should be updated or demoted to `status: outdated`. Don't delete — the comparison history has value even when the details drift.

## Spin-off notes

A review may produce spin-off notes (like `thalo-type-comparison.md`) when a specific comparison deserves deeper treatment. These live in this directory alongside the main review and link back to it.

## Index

The `related-systems-index.md` is a curated index with a "Patterns Across Systems" section. Update it when adding a new review — the cross-system patterns are as valuable as individual reviews.
