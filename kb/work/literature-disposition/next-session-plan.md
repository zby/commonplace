# Literature-disposition continuation plan

Date fixed: 2026-08-26

Start the next session here. The source corpus is complete for the current
cohort. Thirteen of fourteen candidates have dated, executed artifact dispositions.
One further artifact judgment and two workshop-level decisions
remain.

## State to inherit

- Source-corpus selection and its seven quote-backed cases landed in
  `18c6adf1`. Do not reopen corpus selection merely because a famous source was
  deferred. Reopen it only when comparison with a live target identifies an
  exact unsupported claim.
- The activation target and its disposition landed in `bcbde033` and
  `df158ebe`; read [activation-disposition.md](./activation-disposition.md)
  rather than reconstructing the 222-edge graph analysis.
- The Teevan, Tombros, Luhmann, and Milo target repairs landed in `ae1ce1dd`.
  Link-following/search, pointer design, and the enforced tag-README have dated
  decisions in
  [source-backed-dispositions.md](./source-backed-dispositions.md). The MOC
  target's source-first multistage rewrite subsequently passed acceptance,
  deterministic validation, and review job `8462`; all three targets' targeted
  grounding pairs are fresh with `pass` outcomes in the `codex` partition.
- The first four dated dispositions remain in [README.md](./README.md): Gödel
  machines, proposal selection, the Pirolli navigation premise, and end-to-end
  knowledge access.
- The first five post-MOC judgments are recorded in
  [remaining-dispositions.md](./remaining-dispositions.md): keep the independent
  membership/orientation premise after removing its stale five-note heuristic,
  and keep the conditional retrieval-suppression mechanism as a separate
  control-flow premise; then rewrite and keep fluid resolution-switching as the
  local qualitative criterion for transitions among KB views; then rewrite and
  keep the first-time-human heuristic as a conditional access-path comparison
  with one authority and consumer-specific interfaces; then keep addressability
  grain as an independent matched-unit relation after pinning its measured case
  and making its unmeasured helping case conditional.
- The working tree also contains
  `kb/work/multistage-skill-coherence-audit/`, which belongs to another task.
  Do not stage or edit it as part of this workshop.

## Remaining candidate order

The remaining candidate is from the starting cohort and has not yet received a
dated disposition. Its proposed external tradition was explicitly deferred
in [the source selection](../source-grounding/corpus-selection.md#candidates-not-selected-for-the-current-live-claims)
because it no longer establishes a load-bearing live premise.
That means the next step is artifact judgment, not automatic source
acquisition.

| Order | Candidate | Current source-side finding | Decision work |
|---:|---|---|---|
| 1 | `human-llm-differences-are-load-bearing-for-knowledge-system-design` | The claim inventory found almost no information-foraging content and the source selection found no missing authoritative source for its central claim | Re-test cohort membership explicitly; record either a keep disposition or removal from the settled cohort rather than silently dropping it |

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

After the remaining artifact judgment:

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

- [x] Active MOC multistage run is accepted and promoted; its dated
      artifact disposition is recorded.
- [ ] One remaining candidate has a dated, executed disposition.
- [ ] General rule or explicit no-general-rule finding is promoted.
- [ ] Write-time prior-art-check decision is recorded.
- [ ] Durable findings are promoted.
- [ ] Workshop entry and directory are removed.
