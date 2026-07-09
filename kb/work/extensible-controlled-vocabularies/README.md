# Extensible controlled vocabularies

Workshop for designing how a **code-enforced, closed enum field** becomes open-ended per installed KB while staying validator-checkable.

## Trigger

`kb/sources/types/ingest-report.schema.yaml`'s `source_type` is a JSON-schema `enum` — currently 11 values (`scientific-paper`, `practitioner-report`, `conceptual-essay`, `design-proposal`, `tool-announcement`, `github-issue`, `conversation-thread`, `code-repository`, `court-opinion`, `news-article`, `official-statement`). The last three were just added because casework in the sibling `epistack-casebooks` repo hit legal filings and press coverage that had no honest fit and were getting forced into `conceptual-essay`/`conversation-thread`, degrading retrieval. That's a PR against this repo's schema to unblock a downstream KB — the same "argue a new category into the closed set" pattern [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) retired for registers, recurring on a different field.

## Why this isn't just "do the register move again"

Register was a **prose** taxonomy — `COLLECTION.md` headers and a theory note, no code enforcement, so opening it up meant relaxing a claim and adding a catalogue doc. `source_type` is **schema-enforced**: a bare JSON-schema `enum` can't be open-ended without either breaking validation or ceasing to validate anything. "Default profiles, open per-KB" here needs a real mechanism, not just a rename — that mechanism is what this workshop is for.

## Extension points inventory (2026-07-09 survey)

A full pass over every `*.schema.yaml` under `kb/` for `enum:` constraints, filtered by the membership test from [first-principles are inherited constraints, not design choices](../../notes/first-principles-are-inherited-constraints-not-design-choices.md): does the set classify **what knowledge can be** (content taxonomy — demotes) or **what the machinery is** (may stay closed)? Tell: can you name a rival vocabulary that would also work under the same consumer/substrate/domain/machinery commitments?

**Content-taxonomy-shaped — real candidates:**

- `kb/sources/types/ingest-report.schema.yaml` → `source_type` (11 values) — the trigger case above.
- `kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml` → `source-tier` (`code-grounded` / `doc-grounded`) — classifies a review's evidentiary basis, the same shape as `source_type` (source-kind classification) just in a different collection. It's deliberately binary today ("the only authority discriminator," per `types/agent-memory-system-review.md`) and `scripts/build_systems_matrix.py` branches on its exact value when building the comparison matrix, so a third tier (e.g. trace-grounded, vendor-doc-grounded) would hit the same wall `source_type` just hit. Not under growth pressure yet — worth designing this workshop's mechanism generally enough to cover it later, not urgent to fix now.
- `kb/types/note.schema.yaml` → `status` (`seedling` / `current` / `speculative` / `outdated`) — already named in [a universal knowledge framework demotes content taxonomies to defaults](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) as the theory's "predicted fourth instance." A proposal already exists — [assertion force separate from lifecycle status](../../reference/proposals/assertion-force-separate-from-lifecycle-status.md) — but it answers a *different* half: the field fuses lifecycle with first-person assertion-force meaning, and that proposal's fix keeps lifecycle in the type with the four values unchanged ("validators keep checking the enum unchanged"). Its own adoption trigger (a non-endorsed collection needing to disambiguate what `current` means) technically exists now — the LHC casebook is live — but hasn't actually fired: every casebook note there is still `status: seedling` (checked directly in the sibling repo), so nobody has hit the ambiguity in practice. That proposal is adjacent, not overlapping: it never asks whether the four lifecycle values themselves should ever grow, which is this workshop's question.

**Machinery-shaped — probably stay closed:**

- `kb/reference/types/adr.schema.yaml` → `status` (`accepted` / `superseded` / `deprecated`) — a narrow, standard ADR-lifecycle vocabulary; hard to construct a plausible rival under this framework's own boundary commitments.
- `kb/types/index.schema.yaml` / `kb/types/tag-readme.schema.yaml` → `index_source` (`directory` / `tag` / `tag-indexes`) — names generation *mechanisms* Commonplace's own indexing code implements, not knowledge content.
- `kb/reports/types/connect-report.schema.yaml` → `depth` (`quick` / `standard` / `deep`) — an operational parameter of the connect skill, not a content classification.

## Candidate directions (unevaluated)

**A. Extensible vocabulary file.** The list lives as a **YAML file under `kb/`** — a symbolic artifact, not a schema literal — so an installed KB's own agents can edit it locally without a framework schema change. Rough shape, not yet designed: shipped defaults ship as one file; a consuming KB's local additions live in the same file or a sibling; the JSON schema's `enum` is either generated from that file at validation time or replaced by a lookup against it. Exact placement, file format, generation vs. runtime-lookup, and interaction with `commonplace-init`/upgrade are all open. Gives structured tracking (a real shared default list, promotion discipline) at the cost of new machinery.

**B. Per-constraint severity downgrade.** [ADR 024](../../reference/adr/024-schema-severity-is-per-constraint-fail-by-default.md) already ships per-constraint severity (`fail`/`warn`), read generically off `error.schema` for *any* schema keyword — confirmed in `src/commonplace/lib/validation.py` (`_schema_error_message`, ~line 291), not `enum`-specific. So `source_type: {enum: [...], severity: warn}` would make out-of-list values a warning, not a validation failure, **today, with a one-line schema annotation and zero new code**. Materially lighter than A. Trade-off: no shared, inspectable default-list growth or promotion tracking — an agent can type any string and it just warns, which may be too loose for a controlled vocabulary that wants "these are the known categories, extend deliberately," the same tension the register profile's worked-case guard exists to manage.

A and B are not mutually exclusive — B could be the enforcement floor while A (or something like the register profile catalogue) supplies the documented default list a KB extends against.

## Design Questions

- Where would an extensible-vocabulary file (direction A) live — `kb/types/` next to the schema, `kb/sources/` (collection-local, since `source_type` is currently sources-only), or a new global location now that `source-tier` is a second candidate?
- Generated enum (a build/validate-time step regenerates the schema's `enum` from the YAML) vs. runtime lookup (the validator reads the YAML directly, no `enum` in the schema at all)? Trade the `commonplace-validate` architecture cost against keeping the schema self-describing.
- Does severity downgrade (direction B) alone satisfy the need, or does an open-but-unchecked vocabulary proliferate the same way ADR 042's "guards and defaults" section warns open link/register sets would without a worked-case brake?
- Does an installed KB's local addition need the same worked-case-first promotion guard the register profiles got (ADR 019/042), or is that overkill for a controlled vocabulary that's cheaper to add and remove than a whole text contract?
- What's the shipped-defaults vs. local-additions split: does Commonplace ship a starter list and let each KB append freely, or does it ship categories plus a documented extension mechanism with no implied hierarchy?
- Do the per-`source_type` "Limitations Standards" lenses in `ingest-report.md`'s authoring instructions extend the same way (each new category needs its own lens paragraph), or is that a separate, harder problem — the schema field is data, the lens is prose guidance keyed to it?
- Should the mechanism be designed generally enough to also cover `source-tier` from day one, or is `source_type` alone enough to prove it out first (build-local-first, one field at a time)?
- Relationship to [vocabulary-governance](../vocabulary-governance/README.md): that workshop is about definitional *terms* (prose vocabulary like "register", collection/type scope for word meanings); this is about *enum values in a schema field*. Adjacent, not the same — check whether one mechanism could serve both before designing two.

## Closure

Close this workshop when there's a concrete mechanism proposal that answers: where the vocabulary file lives, how it's validated against, whether local additions need a promotion guard, and how the per-category prose guidance (the Limitations Standards lenses) is meant to extend alongside it. That becomes a proposal in `kb/reference/proposals/`, same as the register case, then an ADR once (if) it's exercised.

## Grounding

- [ADR 042: register becomes a default profile under open-ended text contracts](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — extends: the precedent this workshop generalizes to a code-enforced field
- [Text contract](../../notes/definitions/text-contract.md) / [Text contract profiles](../../reference/text-contract-profiles.md) — extends: the prose-side open-ended-list pattern; compare its worked-case-first guard against what a controlled-vocabulary guard should look like
- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — grounds: the demote-don't-delete theory (routing/growth-brake/interoperability) and the "predicted fourth instance" (status) the inventory found
- [First principles are inherited constraints, not design choices](../../notes/first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the membership test (content taxonomy vs. machinery) the inventory above applies to every schema enum
- [ADR 024: schema severity is per-constraint, fail by default](../../reference/adr/024-schema-severity-is-per-constraint-fail-by-default.md) — grounds: candidate direction B — existing, generic per-constraint severity machinery, not `enum`-specific
- [Assertion force separate from lifecycle status](../../reference/proposals/assertion-force-separate-from-lifecycle-status.md) — see-also: adjacent proposal on the same `status` field, fixing fused semantics rather than closed values — not overlapping, worth reading together
- [ingest-report type](../../sources/types/ingest-report.md) and [its schema](../../sources/types/ingest-report.schema.yaml) — operates-on: the concrete artifact with the closed `source_type` enum
- [agent-memory-system-review type](../../agent-memory-systems/types/agent-memory-system-review.md) and [its schema](../../agent-memory-systems/types/agent-memory-system-review.schema.yaml) — operates-on: the second content-taxonomy-shaped candidate (`source-tier`)
- [A richer `source` type](../epistack-framework-additions/richer-source-type.md) — see-also: adjacent casework candidate (capture metadata as first-class fields), not the same problem but same workshop-of-origin
- [Vocabulary governance](../vocabulary-governance/README.md) — see-also: adjacent workshop on definitional-term scope; check for a shared mechanism before designing two
