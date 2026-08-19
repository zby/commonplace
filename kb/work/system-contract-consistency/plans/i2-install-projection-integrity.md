# I2 plan — Make the generated install a valid product shape

**State:** open. A clean install rechecked on 2026-08-19 produced 468 missing
links in shipped notes, 33 in shipped reference, 1 in shipped instructions, and
14 in shared types: 516 total. `text-contract-profiles.md` also failed because
its file-relative global type pointer resolved under `kb/commonplace/types/`.

## Resolution direction and open bundle decision

Treat installation as a non-identity build projection with an explicit source
to target map and dependency policy. The generated tree, not merely the source
checkout, becomes a release acceptance target.

The bundle choice is the one blocking decision. The current-system
recommendation is to retain the three collections already promised by
`INSTALL.md` and its tests, project links to omitted first-party analyses onto
stable public Commonplace pages, and project captured-source links onto their
canonical external URLs. Expanding the offline bundle to include
`agent-memory-systems` and `agentic-systems` is also coherent, but must be chosen
explicitly after measuring its current size and its own omitted-source closure.
Either branch must be recorded before I1's successor ADR; silently dropping
links is not an option.

## Work

1. Freeze a fixture from a built wheel plus `commonplace-init`. Resolve every
   local Markdown link and type pointer originating in the proposed projected
   set plus shared types, then apply one declared source-to-installed projection
   map. An edge without a mapped local target or explicit external replacement
   is an error.
2. Decide the bundle and extend the scaffold/package manifests with one
   declared projection map for every shipped tree. Do not duplicate the bundle
   list in init, packaging, tests, and documentation.
3. Inventory every link and `type:` dependency from the proposed shipped set
   and shared types. Give each edge one disposition:
   - target is shipped and the projected relative link is preserved or
     deterministically rewritten;
   - target is an omitted source and the durable artifact is revised to use the
     canonical external URL as its primary citation;
   - target is intentionally omitted and the dependency is removed;
   - dependency reveals another collection that must be added to the bundle.
   When an internal target becomes an external URL, also preserve the edge as
   an authorized inline citation, reclassify its formal relation, or coordinate
   an explicit collection-contract change. URL validity alone does not make an
   externalized formal relation legal.
4. Implement one link rewriter using the existing fenced-code-safe relocation
   machinery (`TOKEN_PATTERN`, `format_relative_link`, and moved-file rebasing)
   rather than another Markdown regex. Resolve at the source location, map the
   target, then recompute the URL from the installed source location. Explicit
   overrides own external replacements for omitted sources and first-party
   artifacts.
5. Migrate or map the current source links. Add a source-authoring guard so a
   new local link from shipped content into an omitted snapshot or ingest cannot
   silently recreate the install breakage. Local ingests may remain
   supplementary in the source KB only when the shipped form has a valid
   primary citation.
6. Make projection-sensitive path handling explicit:
   - translate Markdown links from shared `kb/types/` into the shipped library
     namespace when their targets move;
   - keep pointers to global type specs repository-relative (`kb/types/...`),
     including the `text-contract-profiles.md` witness;
   - compute any other rewritten relative URL from the source and target maps,
     never from hardcoded depth assumptions.
   Fix `text-contract-profiles.md` directly to the repository-relative
   `type: kb/types/note.md`, and reject a file-relative pointer that only reaches
   shared global types in the source layout.
7. Add a projection audit that fails on an unresolved local target, an included
   file whose type/schema no longer resolves, or an undeclared dependency on an
   omitted collection. It should report the source edge and its disposition
   class rather than only a final warning count.
8. Build a wheel, install it into an isolated environment, initialize a fresh
   project, and validate every collection and the shared type collection. This
   release test must use packaged data, not fall through to source-checkout
   paths.

## Acceptance

- The proposed shipped source set plus shared types retains zero missing-link
  warnings, and the clean installed tree has zero projection-introduced
  failures and zero missing-link warnings.
- Every packaged tree is present in both wheel and sdist fixtures.
- Every omitted dependency is externally cited, removed, or rejected by the
  projection audit.
- Adding a synthetic dependency on an omitted unmapped target makes the product
  test fail. Because ordinary link warnings exit zero, the test inspects
  structured validation results or uses an explicit strict product-test mode.

I1 owns preserve-only rerun semantics and the manual reconciliation procedure
for the resulting installed set, I3 owns its collection topology, and V1 must
validate the whole result without a bespoke test loop.
