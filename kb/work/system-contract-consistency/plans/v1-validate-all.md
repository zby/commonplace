# V1 plan — Make `validate all` mean every declared collection

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. The promoted
skill's one-level `kb/*/COLLECTION.md` loop sees five of eight pristine-install
contracts and misses all three shipped library collections. The command
reference no longer publishes a second hardcoded enumeration. See the [witness
ledger](../baseline-2026-08-27.md).

## Resolution selected

Make `commonplace-validate all` the sole implementation of full deterministic
validation. The Python command should discover scopes recursively, validate
each collection separately, cover type specs outside collections exactly once,
continue after failures, run repository-level checks once, return a stable
`ValidationSuiteResult` (or equivalent), render an aggregate summary, and
return nonzero after the complete sweep if any phase failed. Optional JSON may
render that result, but console text is not the programmatic interface.

Land V1 after the minimal I3 role/root model and before I2. A truthful `all`
command may report that the current installed product is broken; I2 then uses
the same suite as its acceptance harness. Coverage and severity remain
separate: `all` guarantees every declared scope was examined, ordinary warnings
stay warnings, and the packaged-product test may require zero missing-link
warnings.

The [installed-product decision](../installed-product-edition-decision.md)
selects explicit, pairwise-disjoint roots. V1 selects each declared root first,
then performs recursive contract-based collection discovery inside it. Each
root's `types/` remains a collection even when artifact-oriented consumers
exclude type specs explicitly.

## Work

1. Resolve I3's root and collection definitions. Refactor
   `collection_dirs()` or add a validation-specific wrapper so enumeration:
   - operates inside one explicit root and includes its type collections;
   - prunes subtrees beneath `.commonplace-validation-ignore`;
   - schedules only a visible collection root with no collection ancestor,
     leaving an ancestor's structure check to report a non-ignored nested
     `COLLECTION.md`;
   - returns deterministic root-aware paths.
2. Add an internal all-runner to `validate_notes.py`. Pass root identity plus
   root-relative collection paths, never basenames that collide across roots.
   Preserve each collection as its own `ValidationRun` so collection-local tag,
   type, and structure rules retain the correct boundary.
3. Do not fail fast. Accumulate collection results, ignored scopes, warnings,
   failures, and execution errors in one stable Python result, then render one
   final scope ledger showing every discovered collection exactly once. Add an
   optional JSON renderer only after the result contract is tested.
4. After collection runs, validate type specs not already covered by a
   scheduled collection exactly once. `kb/reports/types/` is covered by its
   reports collection; preserve the current `types` coverage of uncontracted
   support directories such as `kb/tasks/types/`. Report this phase separately
   so broader collection discovery cannot create duplicates.
5. Run the landing check once per declared root under its stated scope; do not
   silently broaden it to arbitrary nested collections. Decide and
   document whether redirects are part of `all`; the recommended behavior is to
   run them once when `properdocs.yml` exists and record “not applicable” when
   it does not.
6. Replace the shell programs in `cp-skill-validate` and `commands.md` with the
   single portable invocation. Remove the CLI's explicit rejection of `all` and
   update help and failure text.

## Tests

- Source layout and pristine installed layout.
- User and shipped collections with the same basename.
- Host and Commonplace collections with the same root-relative path, plus a
  validation-ignored nested fixture.
- The I3 disposition of root-local `types/` and collection-local type specs.
- Report/task type specs outside collections, with exact-once coverage.
- Exact-once execution and deterministic order.
- A failing early collection followed by a later collection that is still run.
- Landing and conditional redirect phases.

The current fixture's eight contracts are a regression witness, not the future
hardcoded answer: I2 and I3 may add collections. V1 closes when the invoked set
always equals the discovered declared set and the promoted skill is a
shell-neutral one-command wrapper.
