# Integration Constraints

These constraints define what "adding Obsidian affordances" is allowed to mean in commonplace.

## Non-negotiable constraints

- **Links keep explicit relationship semantics.** Obsidian compatibility cannot justify dropping relation phrases.
- **Repo-native markdown remains the source of truth.** Any Obsidian-specific view, config, or cache is secondary.
- **Git reviewability stays intact.** Changes should remain inspectable as ordinary text diffs.
- **Library/workshop distinction stays visible.** Obsidian affordances should not flatten temporary workshop artifacts into the same behavioral class as durable notes.
- **Agent-facing structure must not become tool-fragile.** If an affordance only works inside Obsidian and weakens non-Obsidian traversal, it is a bad trade.

## Adaptable design choices

- **Canonical link syntax is open for evaluation.** Standard markdown links are the current house style, but the workshop may conclude that wiki links or dual-syntax support are better if the migration path and tooling changes are justified.
- **MkDocs and validator behavior are adaptable.** Current tooling assumptions are implementation details, not sacred boundaries.
- **Compatibility may be native or generated.** The workshop can consider changing canonical files, generating compatibility views, or supporting both.

## Preferred implementation shapes

- generated files over hand-maintained tool artifacts
- optional local configuration over required canonical metadata
- query and navigation layers over representation changes
- additive compatibility shims over syntax replacement

## Failure modes to avoid

- adding Obsidian-only fields with no retrieval or reasoning value
- introducing link-syntax churn without a clear canonical rule or migration plan
- optimizing for graph aesthetics over semantic clarity
- committing user-specific workspace state that does not represent shared workflow value
- rebuilding commonplace around a mainstream note-taking mental model instead of its current knowledge-system model
