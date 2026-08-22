# Decide the home of text-contract and profile vocabulary

## Status

Open. The previously proposed relocation was deliberately stopped before editing library artifacts so it could be decided under the workshop's general content model.

## Question

Should Commonplace retain a standalone definition of **text contract** and **profile**, and if so, which reference artifact should own it?

The answer must start from the user's correction: these terms describe chosen Commonplace machinery. They are not definitions required to state a theory merely because their meanings are stable.

## Current ownership

- [The theory-collection definition](../../../notes/definitions/text-contract.md) defines the terms, lists default profiles, maps them to collections, explains promotion and maintenance, and restates link-grammar policy.
- [The reference profile catalogue](../../../reference/text-contract-profiles.md) already repeats the canonical gloss and owns the shipped profile set.
- [ADR 042](../../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) owns the historical decision to retire the closed `register` taxonomy and adopt open, worked-case-gated profiles.
- Each live `COLLECTION.md` owns the binding contract actually applied to its subtree.
- `AGENTS.md` carries an always-loaded vocabulary gloss for operators.

The present definition has 30 direct Markdown backlinks from 22 files, including six live collection contracts. That is migration cost and evidence of a shared term; it does not establish theoretical placement or the need for a separate file.

## History

- Commit `7eb616d584d86bbc3a5f6198a888a3c8aa2189d2` (2026-04-12) added `kb/notes/definitions/register.md` while stripping universal mechanics out of collection contracts.
- Commit `1ac2171dd38d2cc0e661e348ae546cfc2d8fbd31` (2026-07-09) replaced it with `text-contract.md`, added ADR 042 and the profile catalogue, and demoted theoretical/descriptive/prescriptive from an exhaustive taxonomy to default profiles.
- ADR 042 says invariant “theory” should remain in the definition while changing system state belongs in the catalogue. The workshop now contests the word *theory*: invariant system vocabulary and mutable system state can both belong in reference while still benefiting from separate maintenance surfaces.

## Live options

### A. Retire the standalone definition

Make `kb/reference/text-contract-profiles.md` the canonical surface. Fold in any missing boundary language, retarget backlinks, and delete the theory definition.

This is the most economical option. It is attractive because the catalogue's opening already defines both terms, while the classifier owns the separation from content kind, lineage, and authority.

### B. Keep a small reference definition

Create `kb/reference/definitions/text-contract.md` containing only the canonical distinction:

- text contract: the binding local declaration;
- profile: a reusable, non-authoritative bundle of contract features;
- the collection contract remains authoritative;
- profile is not type, content kind, lineage, or behavioral authority.

Keep current profile entries and promotion state in the catalogue. This preserves a cheap glossary target but costs another synchronized surface.

### C. Recast the catalogue around both concepts

Rename or reshape the catalogue as a broader `text contracts and profiles` reference page. This makes one canonical current-system document but requires a larger backlink and navigation migration than option A.

## Decision tests

- Does a consumer need the definition without loading the profile catalogue?
- Is the residual definition materially cheaper than the catalogue's opening and limits sections?
- Can invariant vocabulary and changing catalogue state be reviewed independently without duplicating their content?
- Which surface should six live collection contracts cite when declaring their adopted profile?
- Would a standalone file carry any proposition not already owned by the classifier, ADR 042, catalogue, or live collection contracts?

## Required migration work after selection

- Retarget all direct backlinks and the `AGENTS.md` vocabulary entry.
- Repair stale consumers that still call the target `register` or describe exactly three exhaustive content modes.
- Correct the profile catalogue's maintenance rows so profile membership does not itself impose theory → prescription → description propagation; actual lineage, dependencies, and consumption paths do.
- Update ADR 042 without falsifying its historical decision: record the later documentation-placement change rather than rewriting what the ADR originally decided.
- Reconcile link labels with each source collection's authorized vocabulary.
- Update collection headings, reference navigation, and any generated definition index.
- Validate every touched artifact and run a broken-link search confirming the retired path has no remaining consumers.

## Completion condition

One option is selected under the workshop's general collection-placement rule, all migration targets are enumerated, and the implementation can be executed atomically without leaving a theory artifact as canonical machinery documentation.

