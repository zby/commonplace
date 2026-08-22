# M1 plan — Finish the representation migrations

**State:** open. Three packets remain. Text promotion and the snapshot type
pointer were resolved and guarded on 2026-08-19; the other witness sets still
need complete consumer inventories.

## Resolution selected

Run one controlled sweep with five independently reviewable packets. The
governing ADRs and schemas already settle the representations, so no new design
ADR is needed. Each packet inventories current consumers, explicitly historical
occurrences, edits, validation, and a narrow guard against reintroducing the
retired executable form.

## Packets

1. **Global note status.** The type-reference exposition sweep retired
   `available-types.md` and corrected `notes/README.md`,
   `document-system-README.md`, and the workshop-layer opening. Sweep remaining
   current-present-tense consumers such as the directory-scoped-type note.
   Describe the actual base fields: required path-valued `type` and
   `description`, plus optional
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
3. **Path-valued types.** The type-reference exposition sweep corrected
   `storage-architecture.md`, absorbed the useful `type-loading.md` mechanics
   into `collections-and-types.md`, and retired the former page. Update
   executable examples in `document-types-should-be-verifiable.md` and related
   type-ladder notes. Retain an old bare enum only when explicitly labelled
   historical.
4. **Snapshot type pointer — resolved 2026-08-19.** The authoritative default
   in `kb/sources/types/snapshot.md` now matches the schema's required
   `type: kb/sources/types/snapshot.md`. The collection Types menu remains the
   extension point. A schema-derived docs test guards the type spec, menu, and
   snapshot skill defaults; existing CLI tests cover the X and GitHub emitters.
   The repair does not constrain S1's mutation boundary or I3's installed
   sources contract.
5. **Text promotion — resolved 2026-08-19.** `kb/types/text.md` now requires
   valid note frontmatter including `description` and
   `type: kb/types/note.md`, with no implicit human verification. The root and
   reference guides plus the text-promotion passages in five conceptual notes
   match the already-correct convert skill. A focused docs test derives the
   schema's required fields, checks the authoritative text contract and
   converter template against them, and rejects retired shortcuts across those
   eight live consumers.

## Migration manifest

| Packet | Retired form | Ground truth | Live consumers | Allowed history | Chosen edit | Verification | State |
|---|---|---|---|---|---|---|---|
| Global note status | Global maturity/status on base notes | ADR 044 and `note.schema.yaml` | Starting witnesses corrected by the type-reference exposition sweep; directory-scoped-type note and full sweep pending | Inventory pending; preserve type-local lifecycle fields and dated decisions | Partial cleanup landed; packet remains open | Pending | Open |
| Areas and Topics | `areas:` plus Topics footers as current grouping | ADR 004 and current tag contracts | Starting witnesses: areas note and stale-indexes note; full sweep after T1 | ADR 004 retains the migration history | Pending T1 | Pending | Open |
| Path-valued types | Bare type names and collection/global lookup fallback | `collections-and-types.md`, resolver, and schemas | Storage summary and canonical exposition corrected; document-types note and related type-ladder notes remain | Inventory pending | Partial cleanup landed; packet remains open | Pending | Open |
| Snapshot type pointer | `type: snapshot` | `snapshot.schema.yaml` | Snapshot type spec; sources Types menu; snapshot-web default and template; X and GitHub emitters | None | Replace the bare default with the schema's path-valued constant while retaining the Types-menu extension point; S1 and I3 do not alter the pointer | All 4 edited Markdown artifacts validate cleanly; schema-derived spec/menu/skill parity and existing emitter tests pass; 492-test suite and focused Ruff pass | **Resolved 2026-08-19** |
| Text promotion | Description-only or arbitrary-frontmatter promotion; bare `type: note`; implicit verification | `note-base.schema.yaml`, `note.md`, and `cp-skill-convert` | Root README, reference README, `text.md`, convert-description, metadata-enforcement, why-types, directory-scoped-types, and wikiwiki notes | Dated ADR/workshop experiment copies may retain their historical wording | Require `description` plus `type: kb/types/note.md`; leave `user-verified` absent; preserve the logical artifact while allowing backlink-safe rename | All 11 edited Markdown artifacts validate cleanly; schema-derived text-contract/converter checks and the scoped retired-wording scan pass; 491-test suite and focused Ruff pass | **Resolved 2026-08-19** |

## Guard and verification

Maintain the migration manifest above as each packet inventories consumers and
settles its allowed history, edits, verification, and closure. Add focused
lexical guards for load-bearing literals such as bare YAML
`type: note|spec|structured-claim|snapshot`, active `areas:`/Topics-footer
instructions, and global note maturity/status claims. Use explicit historical
allowlists; do not build a general semantic-contradiction engine.

Validate every changed artifact. If tests or relocation code are involved, run
the full test suite and lint. M1 closes when all current procedures and examples
match the schemas and every retained retired spelling is visibly historical.
