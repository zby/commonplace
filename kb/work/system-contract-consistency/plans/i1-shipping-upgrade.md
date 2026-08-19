# I1 plan — Make preserve-only upgrade semantics explicit

**State:** open; witnesses rechecked 2026-08-19.

## Resolution selected

Keep ADR 021's `kb/commonplace/` namespacing, but supersede its unimplemented
marker and automatic-refresh clauses. Make the current preserve-only behavior
the deliberate contract: init creates missing paths, classifies existing files
as identical or different, and never replaces or deletes an existing path.
Package upgrades therefore require an explicit manual diff/merge or a clean
regeneration when existing library or projected-skill files must change.

This is the smaller coherent resolution because ADR 014, ADR 037, `INSTALL.md`,
the initializer, and its tests already agree on preservation. Accepted ADR 021
still carries the marker-backed replacement contract; architecture separately
retains a broader claim that init can re-sync on upgrade.

## Work

1. Resolve I3's collection roles, S1's installed-sources mutation boundary, and
   I2's bundle decision first. The successor must name the exact topology and
   shipped collections rather than inherit ADR 021's obsolete list.
2. Write a successor ADR that restates the surviving namespacing decision and
   replaces ADR 021's bundle, `.commonplace` marker, drift detection, and
   clean-tree overwrite clauses. Mark ADR 021 `status: superseded` and link its
   status/body to the successor so its old Decision is no longer operative.
   Reconcile ADR 014's loosely worded “upgrade + rerun” consequence with its
   explicit no-automatic-sync rule.
3. Define the rerun transition for every scaffold class:
   - missing library, template, type, and projected-skill files are created;
   - byte-identical files are reported as matching;
   - every differing existing file is preserved and reported without guessing
     whether the cause is a user edit or an older package version;
   - upstream deletion or rename never deletes an installed path.
4. Document the manual upgrade procedure. Generate the new scaffold in a clean
   comparison directory or inspect packaged canonical content, review the diff,
   and deliberately reconcile existing library and runtime copies. Do not imply
   that reinstalling the Python package alone updates project-local content.
5. Update `architecture.md` (especially its re-sync claim), `INSTALL.md`, the
   init command reference, ADR 037 links, and the ADR 021 path-audit context to
   one vocabulary: rerun acquires newly introduced paths but does not refresh an
   existing path.
6. Derive and test the selected bundle from the scaffold/package manifest. Do
   not add a `.commonplace` marker whose presence would imply unimplemented
   refresh semantics.

## Verification

- The selected bundle is identical in scaffold, wheel, sdist, tests, and docs.
- A fresh init creates no `kb/commonplace/.commonplace` marker.
- A same-version rerun reports all scaffold files as identical.
- In both the old-upstream and practitioner-edited cases, the installed file
  retains exactly its own pre-rerun local bytes and appears in
  `preserved_different`.
- New upstream paths are added; removed upstream paths are preserved locally.
- User collection content and projected-skill edits are never overwritten.
- A lexical/reference check finds no live claim that plain init “re-syncs” or
  automatically updates existing project-local files.

I3's roles/discovery decision, S1's sources boundary, and I2's bundle choice are
inputs to this successor. I1 is complete only when the ADR chain, reference,
installer, and tests describe the same preserve-only transition and upgrade
expectation.
