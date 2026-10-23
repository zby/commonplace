---
description: "Upgrade a consuming project when the Commonplace library changes from notes/ to theory/, preserving project-owned collections and reconciling library references and explicit command scopes"
type: types/instruction.md
---

# Upgrade the Theory library layout

Keep a consuming project's content intact while updating references to the
Commonplace library's Theory collection and the explicit command scopes.

Use this instruction when upgrading from a library exposing `notes/` to one
exposing `theory/`. The operator or the installation instructions load it
before reconciling an existing project. It authorizes reference reconciliation
within the commissioned project, not a collection rename, review-state rewrite
or change to captured evidence.

## Boundaries

- The installed Commonplace library now exposes `theory/` and
  `commonplace:theory/`. Its members still use the note type.
- Init still creates a project's own `kb/notes/`. Existing Notes or differently
  named collections and their customized contracts stay project-owned.
- Do not replace project `kb/notes/` paths merely because library `notes/`
  changed. There is no library alias from the old name.
- Do not edit installed library files, exact captures, source quotes or hash
  pins. Reconcile captured references through their owning workflow if needed.
- Old review/freshness records are not migrated by this upgrade. Whether a
  particular consumer needs continuity is its operator's decision; do not
  silently transfer or acknowledge reviews.

## Reconcile the upgrade

1. Checkpoint the project and identify its actual collections and customized
   control-plane files. Read `.commonplace/library.md` before upgrading and
   retain the old library root for the reference search. Stop on unrelated
   uncommitted changes that prevent attributing the intended edits.
2. Upgrade the user-level tool using the installation procedure. Do not switch
   a shared editable installation while an analysis using it is running.
3. Search the project for library references. These forms change:

   | Old library reference | New library reference |
   |---|---|
   | `commonplace:notes/<path>` | `commonplace:theory/<path>` |
   | `<library>/notes/<path>` | `<library>/theory/<path>` |
   | `<old absolute library root>/notes/<path>` | `<current absolute library root>/theory/<path>` |

   Use literal searches, including the old absolute root. For example:

   ```bash
   rg -n --hidden 'commonplace:notes/|<library>/notes/' .
   ```

   Search ignored local state separately if an active workflow uses it; do not
   rewrite a captured input, queued job or packet in bulk. Classify each hit as
   an authored library reference, a project-owned path, or historical evidence.
   Update only the authored library references and their displayed current
   paths. Keep source wording and observations of the former layout intact.
4. Reconcile the project's live `AGENTS.md` or `CLAUDE.md` library-routing rows.
   Do not replace its goals, local collection names, type pointers or tag
   participation with this KB's values. Existing divergent templates are
   preserved by init, so compare their library rows deliberately rather than
   assuming init upgrades them.
5. In the consuming project, refresh machine-specific pointers and check them:

   ```bash
   commonplace-init
   commonplace-init --check
   ```

   Verify the custom content and contracts remain unchanged, the pointer names
   the current library, and no `kb/theory/` was created. Never run this step in
   the Commonplace source checkout.
6. Update command recipes to supply their actual scope. Use the project's
   collection name or path, not the library's name:

   ```bash
   commonplace-validate recent --collection kb/notes
   commonplace-status --collection kb/notes
   commonplace-promotion-candidates kb/notes
   commonplace-review-target-selector --note kb/notes/<artifact>.md collection
   ```

   Here `kb/notes` is the scaffold example; substitute the project's actual
   collection. Date validation and status require `--collection`; promotion
   takes the collection as a positional argument. Review selection and trivial
   acknowledgement require explicit `--note` targets; `--user-verified` only
   filters that scope. The status JSON field remains `notes_validation`, with
   `scope`; it is not renamed to `theory_validation`. Check each command's
   `--help` when reconciling a script.
7. Validate changed artifacts explicitly and run `commonplace-validate landings`.
   Confirm the library's `theory/README.md` and any referenced local type specs
   exist at the new addresses. Rescan the authored reference set and account
   for remaining historical matches. Do not make review status green by
   rewriting state or acknowledging uncaptured evidence.

## Optional project-owned rename

A consumer can keep Notes indefinitely. If its operator separately chooses to
rename a collection, first decide that project's capture-preservation and
review-continuity requirements. Stop if the destination already exists; do not
merge collections or overwrite customized contracts. Dry-run
`commonplace-relocate-directory <source> <destination>`, review its complete
rewrite surface, and commit the authorized relocation alone. Reconcile local
types, schemas, routing, participation and publication separately. Init does
not perform this migration.

## Report

Name the project collections retained, the library references changed, custom
files preserved, validation results and any active workflow blocked by old
captured paths. Site redirects preserve published addresses, not filesystem or
GitHub blob paths. Report unresolved external references rather than claiming
this checkout can enumerate every consuming project.
