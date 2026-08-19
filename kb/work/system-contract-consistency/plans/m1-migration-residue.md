# M1 plan — Finish the five representation migrations

**State:** open. All five audited contradictions remain, and a targeted recheck
found additional current-looking consumers. The table in the workshop is a
starting witness set, not a complete migration manifest.

## Resolution selected

Run one controlled sweep with five independently reviewable packets. The
governing ADRs and schemas already settle the representations, so no new design
ADR is needed. Each packet inventories current consumers, explicitly historical
occurrences, edits, validation, and a narrow guard against reintroducing the
retired executable form.

## Packets

1. **Global note status.** Correct `available-types.md`, `notes/README.md`, and
   `document-system-README.md`, then sweep current-present-tense consumers such
   as the workshop-layer and directory-scoped-type notes. Describe the actual
   base fields: required path-valued `type` and `description`, plus optional
   `traits`, `tags`, and `user-verified`. Preserve ADR and other type-local
   statuses; never ban the ordinary word `status` globally.
2. **Areas and Topics.** After T1 lands, rebuild and likely rename
   `areas-exist-because-useful-operations-require-reading-notes-together.md`
   around its surviving claim: comparative-reading operations need a
   purpose-built bounded scope rather than navigation tags. Rewrite
   `stale-indexes-are-worse-than-no-indexes.md` around tags, generated listings,
   scoped search, and enforced tag-README marks. Sweep the other current
   `areas:` and Topics instructions while preserving ADR 004 as history. Use
   `commonplace-relocate-note` if the title/path changes.
3. **Path-valued types.** Correct `storage-architecture.md` to direct lexical
   path resolution and update executable examples in
   `document-types-should-be-verifiable.md` and related type-ladder notes.
   Correct `type-loading.md`'s stale “collection-scoped lookup” description even
   though its body is current. Retain an old bare enum only when explicitly
   labelled historical.
4. **Snapshot type pointer.** Change the authoritative default in
   `kb/sources/types/snapshot.md` from `type: snapshot` to
   `type: kb/sources/types/snapshot.md`, while retaining the collection Types
   menu as the extension point. Coordinate wording with S1 and I3.
5. **Text promotion.** Change `kb/types/text.md` so promotion requires valid
   note frontmatter including `description` and `type: kb/types/note.md`, with
   no implicit human verification. Align conceptual conversion notes with the
   already-correct convert skill.

## Guard and verification

Create a migration manifest with columns for retired form, ground truth, live
consumers, allowed historical paths, chosen edit, validation, and closure.
Add focused lexical guards for load-bearing literals such as bare YAML
`type: note|spec|structured-claim|snapshot`, active `areas:`/Topics-footer
instructions, and global note maturity/status claims. Use explicit historical
allowlists; do not build a general semantic-contradiction engine.

Validate every changed artifact. If tests or relocation code are involved, run
the full test suite and lint. M1 closes when all current procedures and examples
match the schemas and every retained retired spelling is visibly historical.
