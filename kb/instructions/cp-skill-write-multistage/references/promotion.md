# Promote an accepted multistage candidate

Load this reference only after `candidate.md` has an independent `accept` for
its current SHA-256. The parent executes every mutation and recovery step.

## Preflight and drift

Require no blocker, completed grounding, candidate bytes matching the accepted
digest, and destination-relative frontmatter, required sections, and links
passing preflight. For an edit, require the live target to remain byte-identical
to `original.md`; for a new artifact, require the destination to remain absent.
Never overwrite or rebase automatically. Compare and write in one
parent-controlled sequence; a digest is not a lock.

## Retitle only with explicit authority

An edit retitle is an address change separate from substantive replacement.
Dry-run:

```bash
commonplace-relocate-note <old-path> --to <final-path>
```

Require the destination absent. Inspect every reported move, Markdown rewrite,
and ProperDocs change. Stop if the report touches `original.md`, `candidate.md`,
frozen reconstruction/disposition, or immutable reviews.

Before adding `--apply`, require explicit mutation and separate-commit authority
plus a concrete recovery plan covering the move, destination absence, every
reported Markdown file, and ProperDocs. If complete recovery is unavailable,
report the retitle blocker without mutating anything.

Run the exact command with `--apply`. It is non-transactional. On error, stop,
inventory actual state, execute only the preauthorized recovery, and verify all
affected paths before any other edit. On success:

- require the old path absent and destination present;
- require only the reported address-preserving diff;
- verify candidate and accepting-review hashes did not change;
- validate the relocated target, every changed Markdown file, and the redirect
  map when ProperDocs changed;
- keep the successful relocation pure and separate under repository commit
  policy.

Capture byte-exact `relocated-original.md` as the new drift and rollback
baseline. Candidate title, frontmatter, and links must already fit the new
destination. Relocation does not preserve review freshness.

## Write, validate, and recover

Recheck the applicable drift baseline immediately before replacement. Write
only the accepted candidate bytes, then run:

```bash
commonplace-validate <target>
```

On failure, restore `original.md` or `relocated-original.md` byte for byte; for
a new artifact, remove only the newly created target. Verify recovery, retain
the workshop, and report the validation failure. Never patch live bytes after
acceptance. A repair can return to the main workflow only if its one
post-review allowance remains unused.

## Add authorized lineage

After target validation, add only source-to-target lineage that the user
authorized and each source collection permits. Prevalidate and preserve every
source. Do not add a reverse edge merely for symmetry. Validate every changed
source.

If lineage mutation fails, restore all changed sources and the target to their
pre-promotion substantive bytes and verify them. A prior address relocation is
separate and remains in place; do not claim that substantive rollback reversed
it.

## Account and clean up

Before cleanup, record in the final report:

- the commission and user-owned decisions;
- replacement, fold, merge, retirement, retitle, and artifact-set choices;
- grounding results, including exact text returned as `quotes added`;
- final candidate and review paths and digests;
- validation, promotion, relocation, lineage, and recovery outcomes;
- removed or retained paths, unresolved blockers, and bounded handoffs.

Extra artifacts or sibling changes converge only through explicit decline,
user acceptance, or separate completion. A composition mismatch blocks
promotion.

Remove only this exact workshop and its exact `kb/work/README.md` line after the
target and lineage validate, the closing account is complete, no authorized
decision remains unexecuted, and no retention reason remains. Retain blocked,
failed, inspection, and experiment runs and report the pending state.
