# General plan: full rename of `kb/notes/` to `kb/theory/`

Drafted 2026-10-22 after the operator leaned towards the full rename. The
per-file inventory is a separate agent's work in this directory
(`inventory-summary.json`, `moves.tsv`, `relocation-updates.tsv`,
`residual-*.tsv`); this plan names phases and the decisions each needs, not
file lists. Counts below are from that inventory at `073eca55f`.

## Runtime independence (operator direction)

The separate [hardwired-collections removal plan](./hardwired-collections-plan.md)
records runtime implementation, including the completed collection-spec typing
boundary and the selected semantic-policy exceptions. This general plan retains the rename's
sequencing and layout/migration decisions; its runtime phase depends on that
workstream rather than commissioning a second implementation.

The operator directed that code should be collection-independent and approved
this plan revision. Runtime operations must accept explicit collections or use
an approved discovery/eligibility policy, not exchange `notes` hardcoding for
`theory` hardcoding. Build/scaffold manifests and this KB's authored routing
legitimately declare the shipped Theory layout. Consumers may retain their
own collection names.

The [detailed implementation plan](./implementation-plan.md#1-runtime-and-build-changes)
lists the runtime files and remaining layout changes. The runtime choices are
settled: commit `43a98d836` requires explicit scopes, and `daed61d59` makes the
source bound collection-owned under ADR 122. Gate 6 is resolved, not a request
to redesign these APIs. Discovery alone does not make every collection eligible.
The TSVs are the pre-sort audit baseline, not instructions to mechanically
rename identifiers. Another agent owns the evidence split; do not refresh those
inventories or move content until that agent's handoff.

## Couplings beyond links

These were not in the framing's starting evidence and change the plan.

- **Shipped library.** `hatch_build.py` ships `notes` with instructions,
  reference, tags and types (`SHIPPED`); installed KBs read it under
  `<environment>/share/commonplace/` and address it as `commonplace:notes/...`.
  Renaming changes the library's public layout, so anything in a consuming KB
  that points into `commonplace:notes/` breaks on upgrade.
- **Review and freshness store.** `kb/reports/state/commonplace-store.sqlite`
  keys records by path: 15,450 review pairs and 7,850 freshness inputs name
  `kb/notes/...`. Without identity migration, moved artifacts appear new to
  current selection; historical records still retain old identities. Decide
  whether that is acceptable or continuity requires migration. No database
  rewrite is authorized merely by this plan.
- **Byte-pinned artifacts.** Source ingests and snapshots carry checksums;
  retained reports and analysis sets carry manifest hashes. The relocation
  baseline touches 517 source files and 59 retained-evidence/archive paths
  under the final inventory categories; rewriting pinned bytes breaks pins.
  Inspect actual protection boundaries, not the broad category alone.
- **Site URLs.** Published note paths change from `notes/x.md` to
  `theory/x.md`. The baseline map has 215 old Notes source keys to preserve
  and 164 target values to retarget; the directory command can add only one
  explicit redirect. Use `redirect-changes.tsv`, refreshed after evidence moves.
- **Residual references.** The final audit separates 1,263 candidate lines in
  203 live/code/test files from historical and workshop references. Use
  `residual-live.tsv` and its preservation rules. Runtime hits require the
  generic refactor below, not a global word replacement.

## Phases

0. **Evidence split** (prerequisite, operator 2026-10-22): sort
   `kb/notes/evidence/` by scope of inference, state the rule in the
   reports, reference and notes contracts, and relocate the local cases to
   `kb/reports/retained/`, each move committed alone. This shrinks the rename and settles README question 2.
1. **Decide** (this workshop, then an ADR). Answer the questions below; write
   the ADR that amends the collection layout and the shipped library.
2. **Prepare tooling** (code commits, tests first).
   - State policy: back up the store; decide whether to preserve historical
     identities and establish new baselines, migrate current keys, or track
     rename identity. Scope/test any required migration before relocation.
   - Generic runtime: done in `43a98d836`. Status and date validation require
     `--collection`; promotion takes an explicit collection and emits scoped
     reports with path-derived links. Review requires explicit `--note` targets;
     `--user-verified` filters them. Keep these interfaces and the generic
     `notes_validation` field with its reported scope. No Theory-specific helper,
     root or status field is needed.
   - Type applicability: done. The unquoted-source bound is set by the
     collection contract's `unquoted-source-limit` field, in Notes and
     Articles ([ADR 122](../../reference/adr/122-collections-set-the-unquoted-source-limit.md)); it moves with `COLLECTION.md`, so the
     rename needs no validator change. Verify the relocated contract still binds.
   - Layout declarations: change `hatch_build.SHIPPED`, scaffold/templates,
     repository-specific scripts and CI to the shipped Theory layout.
     Address init refresh for consumers keeping their original collection names.
   - Preserve the arbitrary/namespaced-collection regressions added with Track 1.
     Re-run integration checks after the layout change; do not remove non-Theory
     fixtures merely to make the test tree match the shipped default.
   - Redirect generation: one redirect per moved page, with existing
     `notes/` redirect targets retargeted rather than chained.
   - Shims only with a named consumer need, marked `# BACKCOMPAT:`.
3. **Freeze window.** Announce in the agent mailbox; no other session edits
   `kb/notes/` or files linking into it between the relocation dry run and
   its commit.
4. **Relocate** with `commonplace-relocate-directory kb/notes kb/theory`
   (dry run, review `relocation-updates.tsv` against it, then `--apply`).
   Commit the result alone so `git log --follow` survives.
5. **Follow-up edits** in separate commits: scaffold/layout switch-over,
   adopted state handling, residual prose mentions, declarations (`AGENTS.md`,
   content routing, tags `participating`, `kb/index.md`), redirects.
6. **Verify.** Full suite (`uv run pytest -m ''`), relevant validation targets,
   store checks against the adopted state policy, site build/redirects and an
   installed-KB rehearsal ([orchestrator instruction](../../instructions/test-installed-commonplace.md)).
   Exercise status, promotion, review and validation with arbitrary collection
   names, including a project with neither Notes nor Theory. Confirm ignored
   or protected data is not pulled in by broader discovery.
7. **Release and consumer upgrade**: communicate the shipped-library address
   change and command/status API changes. A consumer may retain its own
   collection names; document optional directory migration separately.

## Questions to answer before phase 2

In addition to the six in the [README](./README.md):

7. **Name.** `kb/theory/` (singular, mass noun like `reference`) or
   `kb/theories/`; menu label "Theory".
8. **Term collision.** The KB already registers *tentative theory*,
   *addressable theory* and *theory builder*. Is the collection "the theory"
   (the KB's one body of theory) or a register of theory? Is a note a theory,
   or part of one? The answer goes in the collection contract and must not
   contradict the registered definitions.
9. **Library address.** Does `commonplace:notes/...` change to
   `commonplace:theory/...` for installed KBs, and how are their existing
   references found and rewritten?
10. **Existing consumers and init refresh.** Consumers may keep `notes/` or
    another name; runtime support must not require renaming it. Decide how
    init refresh avoids creating an unwanted empty Theory twin while refreshing
    library pointers and skills. Any consumer-owned rename remains optional.
11. **Review store.** Migrate keys in place, or record rename events that
    target identity follows? Does a renamed note keep its freshness, or must
    its reviews be redone?
12. **Pinned bytes.** Exclude checksum- and manifest-pinned files (sources,
    snapshots, retained reports and sets) from the link rewrite and rely on
    redirects, or rewrite and re-pin under a recorded migration as ADR 087
    did for snapshot retyping?
13. **Local state.** Rewrite the 997 untracked files under `kb/reports/state`
    and `cache`, or leave local state to regenerate?
14. **Proposals pairing.** `kb/notes/proposals/` ("unadopted theory") beside
    `kb/reference/proposals/` (system designs): keep as `theory/proposals/`?
15. **Runtime scope/API: resolved.** Keep the explicit-scope interfaces from
    `43a98d836` and the collection-owned source bound from ADR 122. Generic
    target resolution accepts any existing collection, including `theory`.
    The rename needs no unquoted-source registration change. Generic
    `validate_notes`, `relocate-note` and note-typed fields keep their names.
16. **External links.** GitHub URLs into `kb/notes/` in published articles,
    sources and outside sites break; are site redirects enough, or do
    articles get rewritten?
17. **Sequencing with other workshops.** Workshops that edit notes in bulk
    (tagging, navigation, improvement passes) either finish first or pause
    for the freeze window.

## Out of scope

Renaming the note type, its schema or `type: types/note.md` values; splitting
or reorganising the collection beyond the decisions on `evidence/` and
`definitions/`.
