---
description: Definition - lineage records the source dependencies needed to invalidate, regenerate, retire, or review retained behavior-shaping artifacts
type: kb/types/definition.md
tags: [learning-theory, artifact-analysis]
status: current
---

# Lineage

Lineage records a retained artifact's review-relevant source dependencies and derivation status. It answers whether an artifact is source material, canonical source, derived view, generated index, compiled artifact, assembled package, learned update, or archival evidence, and what must be invalidated, regenerated, or retired when a source changes.

## Scope

Use the term lineage when retained behavior can drift from its sources. Generated directory indexes, prompt summaries, skill bundles, compiled validators, route entries, retrieval indexes, and learned updates all have lineage concerns because their behavioral effect can survive after the apparent source has changed.

Lineage is deliberately narrower than full provenance. It records the dependency information needed for review, invalidation, regeneration, retirement, and rollback.

## Exclusions

Do not use lineage as a synonym for storage history. Git history can help reconstruct lineage, but the architectural field is about source dependencies and refresh obligations, not every edit event.

## Misuse Cases

- Treating generated views as harmless because they share a repository with their source notes. The lineage risk is stale derived behavior, not different storage.
- Calling a model checkpoint "current" without recording which traces, feedback, or source artifacts would invalidate the learned update.

---

Relevant Notes:

- [retained artifact](./retained-artifact.md) - scope: the state whose dependency obligations are being recorded
- [storage substrate](./storage-substrate.md) - contrast: a derived artifact can share a substrate with its source
- [behavioral authority](./behavioral-authority.md) - interaction: stale lineage matters most when a derived artifact has high authority
