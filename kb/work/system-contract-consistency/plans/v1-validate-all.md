# V1 plan — Make `validate all` mean every declared collection

**State:** open. The skill and command reference now agree, but both use the
same one-level `kb/*/COLLECTION.md` loop. A current clean install contains seven
contracts and that glob sees four; it misses all three shipped library
collections.

## Resolution selected

Make `commonplace-validate all` the sole implementation of full deterministic
validation. The Python command should discover scopes recursively, validate
each collection separately, cover type specs outside collections exactly once,
continue after failures, run repository-level checks once, print an aggregate
summary, and return nonzero after the complete sweep if any phase failed.

## Work

1. Resolve I3's collection definition. Refactor `collection_dirs()` or add a
   validation-specific wrapper so enumeration:
   - includes namespace-nested and global-type collections;
   - prunes subtrees beneath `.commonplace-validation-ignore`;
   - schedules only a visible collection root with no collection ancestor,
     leaving an ancestor's structure check to report a non-ignored nested
     `COLLECTION.md`;
   - returns deterministic repository-relative paths.
2. Add an internal all-runner to `validate_notes.py`. Pass full paths such as
   `kb/commonplace/notes`, never basenames that collide with user collections.
   Preserve each collection as its own `ValidationRun` so collection-local tag,
   type, and structure rules retain the correct boundary.
3. Do not fail fast. Accumulate collection results, ignored scopes, warnings,
   failures, and execution errors, then render one final scope ledger showing
   every discovered collection exactly once.
4. After collection runs, validate type specs not already covered by a
   scheduled collection exactly once. Preserve the current `types` coverage of
   support roots such as `kb/reports/types/` and `kb/tasks/types/`; report this
   phase separately so broader collection discovery cannot create duplicates.
5. Run the existing top-level landing check once; do not silently broaden its
   direct-child-of-`kb/` contract to nested library collections. Decide and
   document whether redirects are part of `all`; the recommended behavior is to
   run them once when `properdocs.yml` exists and record “not applicable” when
   it does not.
6. Replace the shell programs in `cp-skill-validate` and `commands.md` with the
   single portable invocation. Remove the CLI's explicit rejection of `all` and
   update help and failure text.

## Tests

- Source layout and pristine installed layout.
- User and shipped collections with the same basename.
- A namespace-nested collection and a validation-ignored nested fixture.
- The I3 disposition of `kb/types/` and collection-local type specs.
- Report/task type specs outside collections, with exact-once coverage.
- Exact-once execution and deterministic order.
- A failing early collection followed by a later collection that is still run.
- Landing and conditional redirect phases.

The current fixture's seven contracts are a regression witness, not the future
hardcoded answer: I2 and I3 may add collections. V1 closes when the invoked set
always equals the discovered declared set and the promoted skill is a
shell-neutral one-command wrapper.
