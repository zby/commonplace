# Change packet: write-brief sidecars

Procedure: [change a contract that several consumers read](../../instructions/change-a-contract-that-several-consumers-read.md). The consumer map comes from a code survey on 2026-09-26 plus the searches recorded below.

## The contract

- A document may declare `brief: <own-stem>.brief.md`. The value is a bare filename, resolved relative to the document's own directory.
- The named sibling must exist and declare `type: types/write-brief.md`, a new global type.
- A write brief:
  - is named `<target-stem>.brief.md`;
  - is referenced by exactly that sibling's `brief:`;
  - carries no `brief:` and no `tags:`.
- The one predicate "is this a write brief" is the `.brief.md` filename suffix, answered by one function. The validator enforces that the suffix and the type always agree.
- `cp-skill-write` loads a target's brief as retained intent. It may write a brief when commissioning a write.

## Scope change (2026-09-26, operator)

No artifact scanner excludes briefs. Commands stay simple, and a brief found by a search, listing, site build or review sweep is acceptable. The site, the directory index, the review selector, the orphan check and the `cp-skill-connect` globs are therefore unchanged. The predicate function serves only the validator and relocation. The operator's reason and this alternative are recorded in the ADR.

## Packet fields

1. **Authoritative declaration.** The ADR, which states the decision, and `kb/types/write-brief.md`, which states the authoring contract. The schema and the predicate function hold the machine-checked part.
2. **Declared scope and its enforcement.** "Any typed document may have a brief" is enforced by the `brief:` validator rule. "Every `.brief.md` is a brief of its sibling" is enforced by the pairing rule. "A brief has no brief" is enforced by the brief schema and the pairing rule.
3. **Consumer classes.** Each class lists its members; the status line records what was done.
   - **Resolvers and validators.**
     - Pointer, pairing and suffix⇔type rules: a new rule in `validation.py`.
     - Slug limit (`validation.py` ~448–477): exempt `write-brief`, because the name is derived.
     - Orphan INFO (`validation.py` ~383–393): skip briefs.
     - Type eligibility: a global type is admitted everywhere (`type_resolver.py:243`), so no change is needed.
     - *Status:* pending.
   - **Schemas.** New `kb/types/write-brief.schema.yaml`: `type` const; `tags` and `brief` forbidden. *Status:* pending.
   - **Emitters.** `cp-skill-write` writes briefs and pointers; no code emits them. `relocation.relocate_note` must move the sidecar with its document, rename it to the new stem, and rewrite `brief:`. It must refuse to relocate a brief directly. `relocate_directory` moves siblings together and the pointer is directory-relative, so it needs no change; a test confirms this. *Status:* pending.
   - **Migration code in `commonplace-init`.** None. The type ships through the `types` glob (`init_project.py:382`, `hatch_build.py:30`), and there is no old form to migrate. *Status:* not applicable.
   - **Promoted skills and procedures.** (Missed in the first inventory and added in review: `retire-artifact.md` must delete a document's brief with it — done.)
     - `cp-skill-write` (Steps 1 and 4; commissioning a brief).
     - `cp-skill-connect`: exclude `*.brief.md` from destination scans (its rg calls, ~:64–81).
     - The retire and relocation instructions, if they name sibling handling.
     - *Status:* pending.
   - **Collection contracts, type specs, templates.** New type spec `kb/types/write-brief.md`. No COLLECTION.md lists types (ADR 068), so none changes. *Status:* pending.
   - **Control plane (`AGENTS.md`, `AGENTS.md.template`).** No vocabulary entry: "write brief" is defined in its type spec, and the root instructions do not route to it. *Status:* not applicable.
   - **Reference pages and accepted ADRs.**
     - `collections-and-types.md:101-111`: the statement "composes three files" and "no third file joins this composition" becomes false.
     - `validation-contract.md` ~83–91: new base rules; slug-limit exemptions.
     - `commands.md`: relocate-note (126–128), relocate-directory (131–133), review-target-selector (226–228).
     - `deterministic-write-context-assembly.md` anchor bullet about briefs.
     - *Status:* pending.
   - **Tests and fixtures.** `test_validate_notes.py`, `test_relocate_note.py`, `test_relocate_directory.py`, `test_project_paths.py` / `test_validation_exclusions.py`, `test_index_directory.py`, `test_properdocs_hooks.py` / `test_site_publication_boundaries.py`, `test_review_target_selector.py`, `test_type_schemas.py` / `test_type_contract_integrity.py`. *Status:* pending.
   - **Published views.**
     - `properdocs.yml`: `exclude_docs` gets `**/*.brief.md`.
     - `index_directory` (`_has_indexable_content`, `generate`): skip briefs.
     - Redirects: briefs are unpublished, so none.
     - *Status:* pending.
   - **Other scanners.** `review_target_selector._expand_note_filter` and `list_reviewable_notes` skip briefs. Tag-space scan: briefs carry no tags by schema, so no change. `promotion.py` reads only `kb/notes` and parses briefs harmlessly, so no change. `quote_verification`, `extraction/*` and `link_audit` are audit scans and briefs are ordinary markdown, so no change. *Status:* pending.
4. **Byte-pinned consumers.** None. No existing artifact's bytes change. A target gains a `brief:` line only when a brief is first written for it, and that is an ordinary edit.
5. **Spellings of the old value.** No old value exists. New spellings accepted: `brief: x.brief.md` and `brief: "x.brief.md"`. Paths with `/`, `./` or `../` are rejected.
6. **Generated and projected forms.** The type spec and schema ship in the installed library through the `types` glob. The site excludes briefs. Generated indexes skip them.
7. **Fresh install.** `commonplace-init` creates no brief. The global type is available, and a project that adds a brief validates.
8. **Existing installs and clones.** Nothing to rewrite, and a second init changes nothing. Clones receive the type through the package.
9. **Diagnostic promises.** `commonplace-validate` reports all of the following. The probes are in tests and the acceptance probe.
   - a `brief:` value that is not the document's own `<stem>.brief.md`;
   - a missing brief file;
   - a brief file of the wrong type;
   - a `.brief.md` file whose sibling does not point to it, or that has no sibling;
   - a brief carrying `brief:` or `tags:`.
10. **Acceptance probe.** Run `commonplace-init --root <tmp>`. Add a note with `brief:` and a valid sidecar, then run `commonplace-validate` on the note and on the collection: expected clean. Break each rule in turn: expected a failure naming the rule. Then `commonplace-relocate-note` the note: expected the sidecar to move and the pointer to update.
11. **Drift guard.** A test that walks the repository KB and asserts that every `*.brief.md` is paired and every `brief:` resolves. It passes trivially at zero briefs and does not hardcode a count.
12. **Historical witnesses.** The archived proposal keeps "no third file" as a dated current-state fact. The pilot records live in git history only.
13. **Identity by convention.** Before the change: 0 files named `*.brief.md` and 0 frontmatter `brief:` fields (search below). After it, the suffix is the identity, and the validator keeps the type in agreement with it.
14. **Shared exclusions of a derived predicate.** One predicate function, e.g. `naming.is_write_brief_path`. Consumers: the orphan check, the slug exemption, the dir-index, the review selector, the relocation refusal, the connect skill (by glob), and the site build (by glob).
15. **Side effects of relocation on gated or pinned artifacts.** A brief moves with its document. Briefs are unpublished, so they need no redirect. Their review pins do not exist, because briefs are not review targets.

## Searches (step 2)

| Pattern | Hits / files | Use |
|---|---|---|
| `no third file` | 2 / 2 | reference statement + proposal quote |
| `composes three files` | 1 / 1 | `collections-and-types.md` |
| `\.brief\.md` | 1 / 1 | workshop only; no existing files |
| `brief:` | 5 / 5 | all prose; no frontmatter field |
| `glob("*.md")` / `rglob("*.md")` | 27 / 18, 7 / 7 | scanners; triaged in field 3 |
| `endswith(".ingest.md")` | 6 / 3 | precedent for suffix checks |
| `Rename or move one note` | 1 / 1 | `commands.md` |
| `retained intent` | 18 / 12 | `cp-skill-write` consumer slot and proposals |

## Rescan (step 6)

On 2026-09-26, `rg -i "no third file|composes three files|third file joins"` was run over live `kb/`, excluding the workshop. Results:

- `collections-and-types.md` now reads "composes three files" followed by the optional brief. This is correct.
- The assembler proposal's current-state bullet stated the old rule. It is fixed.
- The per-artifact proposal keeps its dated statement. It is a historical witness and is archived with the proposal.

Missed consumer found in review: `retire-artifact.md` did not delete a document's brief. It is added under Promoted skills and procedures.
