# Worked case: `architecture.md`

Executed 2026-08-24. The sixth artifact taken through the full disposition
procedure.

## Result

**Minimized around orientation and boundaries.** The installed topology remains
as an explicitly approximate discovery map. The durable content is now the
library/user/shared ownership split, the user-level command runtime, canonical
skills versus runtime projections, and path invariance across source and
installed positions. Exact scaffold membership and materialization behavior
route to the live manifest and init implementation.

The edit reduced the page from 11,067 bytes and 128 lines to 5,793 bytes and
115 lines. Most of the line-count persistence comes from readable wrapping;
authored bytes fell by 48 percent.

## Consumption events and dispositions

| Unit | Consumer question | Required reliability | Recovery result | Source grain | Document grain | Maintenance form | Disposition | Retrieval path |
|---|---|---|---|---|---|---|---|---|
| Detailed installed tree | Where does an unfamiliar kind of content live? | orientation | recoverable only after choosing what to inspect | manifest or installed filesystem | 38-line tree | approximate authored routing map | keep and compress | installed-topology diagram; manifest for exactness |
| Surface-by-role table | What does each path mean? | orientation | duplicates tree and prose | manifest plus collection contracts | 11-row table | no independent saving | merge | topology and ownership section |
| Library, user, and shared-type boundary | Who owns and may edit each surface? | architectural | distributed across manifest, resolver, and decisions | several source units and ADR 021 | three bullets plus examples | authored synthesis | keep and compress | ownership section |
| User-level command installation | Where does executable behavior come from? | architectural placement; exact operation elsewhere | mixed | package metadata and environment behavior | three operational paragraphs | retain placement; route procedure | split | runtime paragraph; commands and ADR 064 |
| Four-step init manual | What files and projections does init create? | exact | direct single-unit recovery | `scaffold_manifest.py` and `init_project.py` | numbered list | executable manifest | omit | `commonplace-source`; manifest and init source |
| Wheel versus editable scaffold lookup | How is one authored library packaged in both modes? | architectural invariant; exact mappings elsewhere | mixed | build metadata plus resolver | two paragraphs | one boundary sentence plus live implementation | compress | materialization section; ADR 027 |
| Skill names and runtime directories | Which skills are promoted, and what is canonical? | exact list; architectural authority | mixed | `MANIFEST.promoted_skills` plus copy loop | list embedded in topology and prose | list in manifest; relation in architecture | split | manifest for list; projection section for relation |
| Re-run and upgrade behavior | Will init overwrite or synchronize existing files? | operational exactness with ownership consequence | duplicate | `_record_existing()`, command guide, install guide | two claims | exact behavior in code; preservation boundary retained | split | init source and commands; materialization section |
| User extension and cross-library citation examples | How might a user copy a type or link a note? | procedural | recoverable and uncommon | type contract and ordinary link grammar | one paragraph | no architecture saving | omit | collections/types and link guidance |
| Path invariance | Why do the same library files resolve in source and installed positions? | architectural | requires relation across manifest, links, and resolver | multiple units plus ADR 021 | three rules | authored synthesis | keep and compress | path-invariance section |
| Why reference ships | Why is system reference inside the library? | rationale already implied by selected boundary | duplicate | ADR 021 and library manifest | two paragraphs | stronger decision home | omit | ADR 021 |

## Recovery and discovery experiment

The live `ScaffoldManifest` groups exact directories, copied trees, individual
files, templates, skill destinations, and promoted skill names in one small
data object. `init_project()` consumes those groups directly. A consumer asking
what init creates or which skills it projects gets a more complete answer from
that pair than from the old prose, and an installed consumer can locate the
executing copy with `commonplace-source`.

That does not eliminate the topology's routing value. A reader who does not
yet know whether a thing belongs to the library, user KB, command package, or
runtime skill surface lacks the source symbol needed to begin. The compact
diagram supplies that first distinction, then explicitly sends exact inventory
questions to the manifest. This is the same shape as the retained command-name
catalogue, but with approximate categories instead of checked set parity.

## Drift exposed by comparison

Two statements had crossed from orientation into incorrect exactness:

- The old tree showed `AGENTS.md` as part of init output. The manifest and tests
  show that init creates only `AGENTS.md.template`; the practitioner chooses how
  to integrate it into a runtime control plane.
- The ownership section said `commonplace-init` could re-sync shipped library
  files on upgrade. `_record_existing()` preserves every existing file,
  including a differing library file. Upgrades are a reported, manual
  diff-and-merge operation rather than synchronization.

Both claims were plausible summaries that had lost an important operator
choice. The rewrite keeps template integration and overwrite authority as
boundaries while leaving exact output and classification to the implementation.

## Why the document survives

The manifest cannot explain why `kb/commonplace/` is read-only while peer
collections are writable, why commands live outside the project, why copied
skills are projections rather than canonical instructions, or why wrapping the
library does not break its internal links and type identities. Those relations
span filesystem layout, packaging, runtime discovery, and type resolution.

The page now closes those architecture questions without trying to close exact
installer questions. Its maintenance triggers are semantic boundary changes;
new directories, templates, promoted skills, build mappings, steps, and
commands remain implementation-owned.

## Next

[The `freshness-architecture.md` worked case](./worked-case-freshness-architecture.md)
completed the original scope. It retained target identity and transition
boundaries, removed schema, package, command, and serialization inventories,
and added the missing generation guard for retire/recreate concurrency.
