# ADR 089 change packet

Per [change a contract that several consumers read](../../instructions/change-a-contract-that-several-consumers-read.md). Opened 2026-09-25. Fields are marked **done** as each consumer class is updated; the rescan (step 6) closes the packet.

## 1. Authoritative declaration

[ADR 089](../../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md). Derived declarations: `kb/types/tag-readme.md` and its schema; the code constants in `src/commonplace/lib/index_generated.py` (tag space, participating collections, head path); the scaffold manifest.

## 2. Declared scope and its enforcement

- "Every tag in use within the tag space has a head" — enforced by the base validator check on every artifact in a participating collection that carries `tags:`.
- "Membership ranges over the participating collections" — enforced by one collector (`collect_tag_space`) that the validator's marks, the impacted-head lookup, and the site tail all read. The participating set is declared once in `kb/tags/COLLECTION.md` frontmatter (`participating:`), never inferred.
- "Every head lives in `kb/tags/`" — enforced by the tag-readme type rule failing a head outside that collection, and by the head lookup reading only that path.
- Out of scope, not read: `work`, `sources`, `reports`, `types`, `reference/proposals/archive`.

## 3. Consumer classes

| Class | Search | Members | Status |
|---|---|---|---|
| resolvers and validators | `rg -n "index_source|index_key|collection_index|impacted_marked_tag_readmes|TAG_PAGE_TYPES|tag-indexes|-README.md" src/` | `lib/index_generated.py`, `lib/validation.py`, `docs/properdocs_hooks.py` | pending |
| schemas and derived copies | `rg -n "index_source|index_key|tag-indexes" kb/types/` | `tag-readme.schema.yaml`, `generated-index.md`, `generated-index.schema.yaml` | pending |
| emitters | none: no command writes a head | — | n/a |
| migration in `commonplace-init` | `scaffold_manifest.py`, templates | add `kb/tags/` dir, `user-tags-COLLECTION.md`, `user-tags-README.md` | pending |
| promoted skills and procedures | `rg -n "README.md|tag" kb/instructions/cp-skill-*/SKILL.md kb/instructions/maintain-curated-indexes.md` | connect, write, maintain-curated-indexes | pending |
| collection contracts and type specs | `rg -n "tag" kb/*/COLLECTION.md kb/types/tag-readme.md` | notes contract, tag-readme spec, new tags contract | pending |
| control-plane templates and root AGENTS.md | `rg -n "tags-README|-README.md|kb/notes/ --glob" AGENTS.md src/commonplace/_data/ src/commonplace/lib/library.py` | AGENTS.md (vocabulary, navigation, rg recipes), `AGENTS.md.template`, routing file entry points | pending |
| reference pages and accepted ADRs in present tense | `rg -n "tags-README|index_source|index_key|<tag>-README" kb/reference/` | navigation.md, commands.md, storage-architecture.md, collections-and-types.md, README-REVIEW-SYSTEM? ADR 025/026 (historical: annotate 026) | pending |
| tests and fixtures | `rg -l "tag-readme|index_source|tags-README|covered_by" tests/` | test_validation_tag_readme, test_properdocs_hooks, test_validate_notes, test_type_resolver, test_init_project | pending |
| published views | site hooks, `properdocs.yml` redirects | tag routing, tails, 22 redirects from relocation | pending |
| the heads themselves | `ls kb/notes/*-README.md` | 21 heads + hub | relocation, pure commit |

## 4. Byte-pinned consumers

Freshness baselines key review pairs by note path. `commonplace-freshness-status` lists 31 review pairs on `kb/notes/agent-memory-README.md`, all already stale; no other head carries one. Relocation does not re-key the store. Decision: retire those 31 targets with `commonplace-freshness-retire` in the relocation step and record the count in the commit; a future review re-registers at the new path. Verification: status shows no pair on either path afterwards.

## 5. Spellings of the old value

- `index_source: tag`, `index_source: tag-indexes`, `index_key: <tag>` (unquoted; no quoted instances found).
- Paths: `kb/notes/<tag>-README.md`, `./<tag>-README.md` (from notes), `../notes/<tag>-README.md` (from other collections), `notes/<tag>-README.md` (site paths in properdocs.yml), `tags-README.md`.
- Prose: "tag-README", "tag README", "`<tag>-README.md`", "tags-README".

## 6. Generated and projected forms

Site build: tag tails and tag links (hooks). Installed library: the package ships `kb/` as data, so `kb/tags/` ships with it; no separate projection. Init-written routing file lists entry points (check `library.py`).

## 7. Fresh install

`commonplace-init` on an empty directory creates `kb/tags/COLLECTION.md` (with `participating: [notes, reference, instructions]`) and `kb/tags/README.md`; `commonplace-validate landings` passes; validating a note with a tag and no head fails with the head path named.

## 8. Existing installs and clones

Init on an existing project adds `kb/tags/` if absent and leaves it alone if present. Second run changes nothing. Clones of this checkout receive the relocation through git.

## 9. Diagnostic promises

- "Validator reports a tag without a head": base check on the artifact; probe: a note tagged `x` in a fresh project.
- "Head outside `kb/tags/` fails": type rule; probe: a tag-readme file left in `kb/notes/`.
- "Undeclared participation means no members": probe: `kb/tags/COLLECTION.md` without the field validates with a warning naming the field.

## 10. Acceptance probe

```
tmp=$(mktemp -d); commonplace-init --root $tmp
(cd $tmp && commonplace-validate landings && commonplace-validate kb/tags)
# write kb/notes/a.md tagged [x]; validate -> fails naming kb/tags/x-README.md
# write kb/tags/x-README.md; validate -> passes
```

## 11. Drift guard

Test: the set of directories `collect_tag_space` scans equals the `participating:` declaration in the fixture's `kb/tags/COLLECTION.md`; and every top-level collection in this checkout is either declared participating or named in the ADR's outside list (test reads the ADR-independent constant `NON_PARTICIPATING_NOTE` in the tags contract?). Keep the second as a repository test that lists undeclared collections rather than counting.

## 12. Historical witnesses

ADR 025 and ADR 026 describe `tags-README.md` and `index_source` as current; 026 gets a one-line forward annotation to ADR 089, 025 is left (its decision, build-time-only listings, is unchanged). Archived proposals carrying tags stay untouched and outside the tag space. Ingest reports under `kb/sources/` link to head paths; relocation rewrites those links.

## Rescan (step 6)

pending
