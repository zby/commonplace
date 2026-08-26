# Literature-disposition continuation plan

Date fixed: 2026-08-26

Start the next session here. The source corpus is complete for the current
cohort. Seven of fourteen candidates have dated artifact dispositions, and the
eighth target has a committed source-bounded repair whose multistage acceptance
run is still open. Complete that run first. Six further artifact judgments and
two workshop-level decisions then remain.

## State to inherit

- Source-corpus selection and its seven quote-backed cases landed in
  `18c6adf1`. Do not reopen corpus selection merely because a famous source was
  deferred. Reopen it only when comparison with a live target identifies an
  exact unsupported claim.
- The activation target and its disposition landed in `bcbde033` and
  `df158ebe`; read [activation-disposition.md](./activation-disposition.md)
  rather than reconstructing the 222-edge graph analysis.
- The Teevan, Tombros, Luhmann, and Milo target repairs landed in `ae1ce1dd`.
  Link-following/search and pointer design have dated decisions in
  [source-backed-dispositions.md](./source-backed-dispositions.md). All three
  edited targets validate, and their targeted grounding pairs are fresh with
  `pass` outcomes in the `codex` partition.
- The MOC repair is not yet a final disposition. Resume
  `kb/work/multistage/multistage-write-enforced-tag-readme-moc-20260826/`
  from its `README.md`. Its live checklist is authoritative because the run
  may continue after this plan is committed. Do not restart the run or treat
  the committed candidate as accepted until that checklist reaches acceptance,
  promotion, source-lineage validation, and workshop cleanup.
- The first four dated dispositions remain in [README.md](./README.md): Gödel
  machines, proposal selection, the Pirolli navigation premise, and end-to-end
  knowledge access.
- The working tree also contains
  `kb/work/multistage-skill-coherence-audit/`, which belongs to another task.
  Do not stage or edit it as part of this workshop. The current
  `kb/work/README.md` modification belongs to the active MOC run and should
  be reconciled by that run's eventual cleanup, not swept into an unrelated
  commit.

## Remaining candidate order

After the MOC run closes, the remaining six are the starting cohort minus the
starting-cohort notes already decided. Their proposed external traditions were explicitly deferred
in [the source selection](../source-grounding/corpus-selection.md#candidates-not-selected-for-the-current-live-claims)
because those traditions no longer establish a load-bearing live premise.
That means the next step is artifact judgment, not automatic source
acquisition.

| Order | Candidate | Current source-side finding | Decision work |
|---:|---|---|---|
| 1 | `index-completeness-does-not-determine-editorial-orientation` | LIS and PKM candidates were not selected for a surviving claim; the categorical generation claim was already scoped to deterministic membership generation | Compare the current note with the newly repaired MOC note and its ADR consumers; decide keep, merge, rewrite, or cohort removal |
| 2 | `indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more` | Automation-bias and materialized-view sources were deferred because the live claim is now a conditional control-flow mechanism | Decide whether the conditional mechanism remains an independent premise or should merge into the completeness cluster |
| 3 | `a-knowledge-base-should-support-fluid-resolution-switching` | Shneiderman was deferred as adjacent to, but not authoritative for, the live qualitative KB criterion | Decide whether the local mechanism inventory earns a note or belongs in a neighboring navigation synthesis |
| 4 | `design-for-the-first-time-human-except-on-access-cost` | DITA and single-source publishing were deferred because the live contribution is the access-mode transfer and per-consumer materialization | Test whether that transfer remains a distinct claim after the superseded navigation row was repaired |
| 5 | `addressability-grain-sets-a-matched-selective-read-floor` | Database cost-model and passage-retrieval sources were deferred; the live note uses a conditional matched-unit relation and local measurements | Decide whether the local relation and measurements earn the artifact without importing a database analogy as authority |
| 6 | `human-llm-differences-are-load-bearing-for-knowledge-system-design` | The claim inventory found almost no information-foraging content and the source selection found no missing authoritative source for its central claim | Re-test cohort membership explicitly; record either a keep disposition or removal from the settled cohort rather than silently dropping it |

## Per-candidate procedure

For each candidate:

1. Read the current note, its row in
   [claim-inventory.md](./claim-inventory.md), and the matching deferral in the
   source-corpus selection.
2. Re-measure inbound library references. Use the count as rewiring cost, not as
   the disposition signal.
3. Separate source-established units from the Commonplace remainder and apply
   the recovery test. Do not decide by resemblance or overlap count.
4. Record a dated disposition and execute it. A retirement must follow
   `kb/instructions/retire-artifact.md`, including the user-approval stop
   before inbound edits. A rename must use `commonplace-relocate-note` and a
   pure relocation commit.
5. Validate every edited artifact. Run `semantic/grounding-alignment` when a
   named source dependency changes. Broader graph discovery, if useful after
   the settled edit, belongs to `cp-skill-connect`.
6. Update the cohort count and this plan after each completed disposition.

## Final workshop decisions

After the six artifact judgments:

1. Promote a general disposition rule, or record the positive finding that
   literature disposition remains per-note. The worked cases currently favor a
   claim-level recovery test, but this is not yet a promoted rule.
2. Decide the write-time prior-art check. ADR 073 guards sources already named
   by a writer; the open question is whether authoring should also search for
   missing external prior art. Record either the new check and its home or the
   reason the existing intra-KB novelty tests should not grow one.
3. Promote durable conclusions to the appropriate library collection, remove
   this workshop from `kb/work/README.md`, and delete the workshop directory.
   Finished workshop files are not retained as a historical register.

## Closure checklist

- [ ] Active MOC multistage run is accepted and promoted or revised; its dated
      artifact disposition is recorded.
- [ ] Six remaining candidates have dated, executed dispositions.
- [ ] General rule or explicit no-general-rule finding is promoted.
- [ ] Write-time prior-art-check decision is recorded.
- [ ] Durable findings are promoted.
- [ ] Workshop entry and directory are removed.
