# I2 plan — Make the generated install a valid product shape

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. The pristine
projection produced 462 missing-link warnings in shipped notes, 55 in shipped
reference, 1 in shipped instructions, and 14 in shared types: 532 total across
181 files. The installed tag-semantic proposal also failed type resolution.
See the [witness ledger](../baseline-2026-08-27.md).

## Resolution selected

Treat installation as a non-identity build projection with an explicit source
to target map and dependency policy. The generated tree, not merely the source
checkout, becomes a release acceptance target.

The [installed-product decision](../installed-product-edition-decision.md)
compares the self-contained, thin, curated, and hybrid options and selects one
default hybrid evidence-local edition. It retains the complete methodology
core and the least fixed point of linked tracked source analyses, while
externalizing large review collections and other omitted first-party material
to immutable source-revision-pinned Commonplace publications. Raw snapshots
remain excluded. There is no edition flag in this program.

The decision also supplies pairwise-disjoint `kb-root`s, root-local type
semantics, ownership values, compiler boundary, and terminal upgrade transition
shared with I1, I3, and V1. The successor ADR remains a workshop draft during
dormant foundation and compiler work, then activates with the operative product
surfaces. The workshop recommendation is not system authority.

## Work

1. Consume V1's structured full-validation suite as the acceptance harness.
   Freeze a fixture from a built wheel plus `commonplace-init`. Resolve every
   local Markdown link and type pointer originating in the proposed projected
   set plus its root-local types, then apply one declared source-to-installed
   projection map. An edge without a mapped local target or explicit external
   replacement is an error.
2. Compile the hybrid evidence-local edition from source `kb/` into installed
   `commonplace-library/kb/`. Keep host `kb/` independent and reserve
   `commonplace/kb/` for the optional reader checkout. Promote the successor ADR
   only when the activation path becomes true. Extend `ScaffoldManifest` with
   the edition's source-analysis fixed-point rule and one declared
   source-to-target projection for every shipped entry. Do not duplicate the
   edition in init, packaging, tests, and documentation.
3. Inventory every link and `type:` dependency from the proposed shipped set
   and its type contracts. Give each edge one disposition:
   - target is shipped and the projected relative link is preserved or
     deterministically rewritten;
   - a raw captured source is omitted and can become its canonical source URL;
   - a Commonplace ingest is omitted but its analysis is load-bearing, so the
     edge becomes a stable release- or commit-pinned Commonplace publication;
   - omitted first-party theory or review material becomes a stable Commonplace
     publication link rather than the original evidence it interpreted;
   - target is intentionally omitted and the dependency is removed with its
     claim or navigation role dispositioned;
   - dependency reveals another collection that must be added to the bundle.
   When an internal target becomes an external URL, also preserve the edge as
   an authorized inline citation, reclassify its formal relation, or coordinate
   an explicit collection-contract change. URL validity alone does not make an
   externalized formal relation legal.
4. Implement one compiler-like projection operation using the existing
   fenced-code-safe relocation
   machinery (`TOKEN_PATTERN`, `format_relative_link`, and moved-file rebasing)
   rather than another Markdown regex. Resolve at the source location, map the
   target, then recompute the URL from the installed source location. Explicit
   overrides own external replacements for omitted sources and first-party
   artifacts. Wheel packaging and editable-source fallback must both call this
   operation; source mode must not continue identity-copying paths that the
   wheel rewrites.
5. Migrate or map the current source links. Add a source-authoring guard so a
   new local link from shipped content into an omitted snapshot or ingest cannot
   silently recreate the install breakage. Local ingests may remain
   supplementary in the source KB only when the shipped form has a valid
   primary citation.
6. Make projection-sensitive path handling explicit:
   - project source `kb/types/` into `commonplace-library/kb/types/`;
   - resolve `kb/...` pointers against the artifact's owning `kb-root` and keep
     that root-relative spelling when the target remains in the same root;
   - project selected Commonplace type contracts into host `kb/types/` as
     recorded replicas when host-root operations need them;
   - translate or make file-relative any collection-local type pointer such as
     the current semantic proposal's `kb/reference/types/design-proposal.md`;
   - compute any other rewritten relative URL from the source and target maps,
     never from hardcoded depth assumptions.
   Reject a pointer that falls through into another root and an absolute
   collection-local pointer that bypasses the declared projection map.
7. Add a projection audit that fails on an unresolved local target, an included
   file whose type/schema no longer resolves, or an undeclared dependency on an
   omitted collection. It should report the source edge and its disposition
   class rather than only a final warning count.
8. Build a wheel, install it into an isolated environment, initialize a fresh
   project, and invoke V1 over the installed artifact. Run an equivalent
   editable-source projection fixture through the same compiler and compare
   their product shape.

## Acceptance

- The proposed shipped source set plus root-local types retains zero missing-link
  warnings, and the clean installed tree has zero projection-introduced
  failures and zero missing-link warnings. V1's coverage guarantee and this
  stricter product severity policy remain separate.
- Every packaged tree is present in both wheel and sdist fixtures.
- Every omitted dependency is externally cited, removed, or rejected by the
  projection audit.
- Adding a synthetic dependency on an omitted unmapped target makes the product
  test fail. Because ordinary link warnings exit zero, the test inspects
  structured validation results or uses an explicit strict product-test mode.

I1 owns ownership-aware rerun and legacy-layout reconciliation for the
resulting installed set, I3 owns its topology and `kb-root` declaration, and V1
validates the whole result without a bespoke test loop.
