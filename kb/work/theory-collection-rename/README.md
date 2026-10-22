# Rename the notes collection to Theory

Posed by the operator on 2026-10-22, after the site menu was trimmed to
Agentic Systems, Reference and the other collections.

## Goal

Rename the collection now at `kb/notes/` to **Theory**, so its name states its
role beside Reference (Commonplace's selections and their state) and
Instructions (procedures). Its README already calls it "the theory collection",
and [content routing](../../reference/content-routing.md) already routes
"theory: the reader reasons with it" there. The `note` type keeps its name:
the collection is the theory, its members are notes.

## Operator decisions

- Rename the collection to Theory (2026-10-22). Depth (label only or the
  directory too) is decided here, not yet.

## Constraint

[ADR 116](../../reference/adr/116-one-word-per-concept-across-prose-and-code.md)
gives one concept one word on every surface and renames code first when
surfaces disagree. A "Theory" label over a `kb/notes/` path is therefore
allowed only as a recorded, temporary step of a full rename, not as an end
state.

## Starting evidence (2026-10-22)

- **Contents:** 429 Markdown files; 366 at the root. Subdirectories:
  `definitions/` (27, vocabulary), `evidence/` (17, episode records that
  support or test claims), `agent-memory-requirements/` (13), `proposals/` (3,
  "finished but unadopted theory"), `types/` (2), `research/` (1).
- **Live inbound links:** about 200 files across `kb/notes`, `kb/tags`,
  `kb/reference`, `kb/instructions`, `kb/index.md` and `AGENTS.md`.
- **Frozen inbound links:** the Agent Memory Systems reviews (159 files),
  ADRs (49), retained reports (52), reference proposals (37) and several
  workshops. Local `kb/reports/state` and `cache` hold about 18,600 more; they
  are not published.
- **Code naming the path:** `lib/project_status.py`, `lib/project_paths.py`,
  `lib/promotion.py` and `cli/promotion_candidates.py`, `cli/validate_notes.py`
  (the `notes` target), `review/review_target_selector.py` (`NOTES_ROOT`),
  `review/collection_conformance.py`; relocate command examples.
- **Scaffold:** `scaffold_manifest.py` creates `kb/notes/` and
  `kb/notes/types/` in every new KB, from `templates/user-notes-COLLECTION.md`
  and `user-notes-README.md`; other user templates mention `notes/`.
- **Declarations:** `kb/tags/COLLECTION.md` lists `notes` as a participating
  collection; `AGENTS.md`, content routing and `CLAUDE.md`'s collection table
  name `kb/notes/`; `properdocs.yml` holds 215 redirect entries from
  `notes/` paths.

## Open questions

1. **Depth.** Label only (menu and README heading), or rename the directory to
   `kb/theory/` with code, scaffold and declarations. ADR 116 favours the full
   rename.
2. **`evidence/`.** Records of episodes are evidence for theory, not theory.
   Keep them as a declared part of the collection, or move them elsewhere.
3. **`definitions/`.** Vocabulary as theory's terms: state it in the contract,
   or leave as is.
4. **Installed projects.** New KBs get the new name from the scaffold;
   existing consuming KBs migrate (a relocation they run), keep `notes/` with
   the code accepting both (a `# BACKCOMPAT:` shim needs a consumer need), or
   are left to diverge.
5. **Frozen history.** Rewrite links in frozen collections and retained
   reports through relocation, or leave them and rely on site redirects.
6. **Decision record.** A full rename changes what ships to consuming KBs and
   needs an ADR.

## Boundaries

- Commit any `commonplace-relocate-*` result alone, without content edits.
- Do not edit retained analysis sets or frozen collections except through the
  relocation command's backlink rewrite, if question 5 chooses that.
- The note type, its schema and `type: types/note.md` values stay unchanged
  unless a separate decision renames them.

## What closes this workshop

The collection has one name on every surface, or a recorded decision keeps
`notes`; the ADR (if any) is accepted; the scaffold, code, declarations and
site agree; installed-project handling is decided and documented. Then remove
this directory and its Active Workshops entry.
