# M1 plan — Finish the representation migrations

**State:** open; rebaselined at commit `6660bd2a` on 2026-08-27. Only the
Areas/Topics packet remains. Global note status and path-valued types were
resolved and guarded on 2026-08-27; text promotion and the snapshot type
pointer were resolved and guarded on 2026-08-19. See the [witness
ledger](../baseline-2026-08-27.md).

## Resolution selected

Run five independently reviewable packets rather than one correlated sweep. The
governing ADRs and schemas already settle the representations, so no new design
ADR is needed. Each packet inventories current consumers, explicitly historical
occurrences, edits, validation, and a narrow guard against reintroducing the
retired executable form.

Areas/Topics waits for the tag-contract workshop. Completed packets remain
recorded outcomes until this workshop closes.

## Packets

1. **Global note status — resolved 2026-08-27.** Current guidance now describes
   required path-valued `type` and `description`, plus optional `traits`,
   `tags`, and `user-verified`, without a global maturity ladder. The sweep
   preserved ADR and article-local lifecycle fields and removed the final live
   `seedling` navigation label. A schema-derived guard checks the shared note
   fields, scans active frontmatter for unauthorized `status`, and rejects the
   retired contract only in its inventoried current guidance surfaces.
2. **Areas and Topics.** After the tag-contract workshop lands, rebuild and likely rename
   `areas-exist-because-useful-operations-require-reading-notes-together.md`
   around its surviving claim: comparative-reading operations need a
   purpose-built bounded scope rather than navigation tags. Rewrite
   `stale-indexes-are-worse-than-no-indexes.md` around tags, generated listings,
   scoped search, and enforced tag-README marks. Sweep the other current
   `areas:` and Topics instructions while preserving ADR 004 as history. Use
   `commonplace-relocate-note` if the title/path changes.
3. **Path-valued types — resolved 2026-08-27.** Current examples now use
   resolvable path values with their source location made explicit where that
   changes resolution. A guard parses every visible active artifact's
   frontmatter, validates each type path, checks executable examples in the
   inventoried guidance, and allows the old bare enum only in ADR 012's dated
   history.
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
| Global note status | Global maturity/status on base notes | ADR 044, `note-base.schema.yaml`, `note.schema.yaml`, and `note.md` | Every visible active artifact's frontmatter plus the inventoried current guidance that taught maturity or status | ADR lifecycle values and article-local publication status remain type-local; dated decisions remain history | Replace maturity/status guidance with the actual shared fields and remove the final `seedling` navigation label | All 19 changed KB artifacts validate cleanly; schema-derived tests constrain shared fields, authorized local status values, and retired current guidance; full suite and focused Ruff pass | **Resolved 2026-08-27** |
| Areas and Topics | `areas:` plus Topics footers as current grouping | ADR 004 and current tag contracts | Starting witnesses: areas note and stale-indexes note; full sweep after tag-contract adoption | ADR 004 retains the migration history | Pending tag-contract adoption | Pending | Open |
| Path-valued types | Bare type names and collection/global lookup fallback | `collections-and-types.md`, resolver, and schemas | Every visible active artifact's frontmatter plus executable examples in the canonical type guidance and related notes | ADR 012 retains the pre-path enum in dated context | Replace live bare values with paths that resolve from the artifact or explicitly illustrated source context | Parsed frontmatter and executable-example guards resolve every current type path; the bare-value scan permits only ADR 012; all changed artifacts, the full suite, and focused Ruff pass | **Resolved 2026-08-27** |
| Snapshot type pointer | `type: snapshot` | `snapshot.schema.yaml` | Snapshot type spec; sources Types menu; snapshot-web default and template; X and GitHub emitters | None | Replace the bare default with the schema's path-valued constant while retaining the Types-menu extension point; S1 and I3 do not alter the pointer | All 4 edited Markdown artifacts validate cleanly; schema-derived spec/menu/skill parity and existing emitter tests pass; 492-test suite and focused Ruff pass | **Resolved 2026-08-19** |
| Text promotion | Description-only or arbitrary-frontmatter promotion; bare `type: note`; implicit verification | `note-base.schema.yaml`, `note.md`, and `cp-skill-convert` | Root README, reference README, `text.md`, convert-description, metadata-enforcement, why-types, directory-scoped-types, and wikiwiki notes | Dated ADR/workshop experiment copies may retain their historical wording | Require `description` plus `type: kb/types/note.md`; leave `user-verified` absent; preserve the logical artifact while allowing backlink-safe rename | All 11 edited Markdown artifacts validate cleanly; schema-derived text-contract/converter checks and the scoped retired-wording scan pass; 491-test suite and focused Ruff pass | **Resolved 2026-08-19** |

## Guard and verification

Maintain the migration manifest above as each packet inventories consumers and
settles its allowed history, edits, verification, and closure. Add focused
guards for load-bearing literals such as bare YAML
`type: note|spec|structured-claim|snapshot`, active `areas:`/Topics-footer
instructions, and global note maturity/status claims. Parse YAML fields and
executable examples where possible so ordinary prose occurrences do not fail.
Use explicit historical allowlists; do not build a general
semantic-contradiction engine.

Validate every changed artifact. If tests or relocation code are involved, run
the full test suite and lint. M1 closes when all current procedures and examples
match the schemas and every retained retired spelling is visibly historical.
