# What to do with the current gate bundles

The current bundled review instructions should survive, but their role should change.

## Decision

Keep the current bundle names as stable user-facing entry points. Stop treating the bundle documents as the canonical place where checks live.

In practice:

- `frontmatter-review`, `prose-review`, `semantic-review`, and `complexity-review` remain valid bundle names
- their check lists move into individual gate files
- the bundle document becomes a wrapper containing shared framing, prerequisites, cautions, and output contract

This preserves the interface without preserving the wrong storage primitive.

## What stays in a bundle wrapper

- what the bundle is for
- shared prerequisites
- bundle-level do-not rules
- output format
- optional execution guidance such as target budget or ordering

These are genuinely bundle-level concerns. They should not be duplicated across every gate.

## What moves out of the bundle wrapper

- individual check definitions
- canonical bundle membership
- stale policy
- anything the selector needs to compute freshness

Those belong in gate files and derived indexes.

## Why not delete the bundles outright

Deleting the bundles would create unnecessary UX churn.

- users already think in terms of named review passes
- execution may still want bundle-sized packets even after freshness becomes gate-local
- shared output and prompting constraints are real bundle-level concerns

So the right move is to thin them, not remove them.

## Why not keep them canonical

Keeping the current bundle documents canonical would preserve the main problem:

- checks remain trapped inside monoliths
- selector logic keeps inferring semantics from bundle names
- the same check cannot cleanly appear in multiple bundles
- review-revise extracted gates have nowhere first-class to land

That would recreate the current coupling under a new label.

## Specific recommendation for review-revise experiments

The workshop-only `accessibility-review` and `sentence-review` documents should not be promoted wholesale as new canonical bundles just because they surfaced useful checks.

Recommended treatment:

- harvest stable checks from them into individual gate files
- mark those gates `candidate` or `active` based on confidence
- then decide whether they belong inside existing bundles or justify a new named bundle

This matters because the review-revise experiment mixed two things:

- discovery of useful individual checks
- experimentation with review-pass packaging

We should preserve the first result without prematurely freezing the second.

## Practical migration stance

Near term:

- keep current bundle files working
- decompose their checks into gates
- let selector freshness become gate-local behind the scenes

Later:

- make bundle files thin wrappers
- let execution regroup stale gates by bundle when useful
- retire duplicate monolithic check prose

That is the least disruptive path that still gets us to the right architecture.
