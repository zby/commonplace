# Literature-disposition continuation plan

Date fixed: 2026-08-26

Start the next session here. The source corpus is complete for the settled
cohort. All fourteen candidates have dated resolutions: thirteen artifact
dispositions and one explicit removal from the cohort. Two workshop-level
decisions were adopted in ADR 081; only workshop closure remains.

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
- ADR 081 and the claim-grained literature-assessment instruction resolve the
  general-rule and write-time prior-art-check decisions. Ordinary writing does
  not search for missing prior art; an explicit retrospective question loads
  the bounded multistage assessment.
- The six post-MOC candidate resolutions are recorded in
  [remaining-dispositions.md](./remaining-dispositions.md): keep the independent
  membership/orientation premise after removing its stale five-note heuristic,
  and keep the conditional retrieval-suppression mechanism as a separate
  control-flow premise; then rewrite and keep fluid resolution-switching as the
  local qualitative criterion for transitions among KB views; then rewrite and
  keep the first-time-human heuristic as a conditional access-path comparison
  with one authority and consumer-specific interfaces; then keep addressability
  grain as an independent matched-unit relation after pinning its measured case
  and making its unmeasured helping case conditional; finally remove the
  human–LLM-differences candidate from this cohort after the claim inventory
  placed no central claim in an outside tradition and found its only
  navigation-adjacent unit already split out. The artifact itself remains
  unchanged.
- The working tree also contains
  `kb/work/multistage-skill-coherence-audit/`, which belongs to another task.
  Do not stage or edit it as part of this workshop.

## Candidate resolution complete

No candidate remains. The final candidate,
`human-llm-differences-are-load-bearing-for-knowledge-system-design`, was removed
from the settled cohort rather than silently dropped or mislabeled as a keep.
The claim inventory found almost no navigation content, and its one access row
had already been split into the first-time-human note. The target file remains
unchanged and valid.

Git commit `18c6adf1` retains the source-selection deferrals and their
disposition. They are not residual acquisition work for this workshop.

## Per-candidate procedure

For each candidate:

1. Read the current note, its row in
   [claim-inventory.md](./claim-inventory.md), and the matching source assignment
   retained by git commit `18c6adf1`.
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

## Resolved workshop decisions

With candidate resolution complete, ADR 081 selected both remaining decisions:

1. Explicit retrospective literature disposition uses the adopted
   claim-grained multistage instruction.
2. Ordinary writing does not search for missing external prior art. A bounded
   retrospective request, not every write, triggers the assessment.
3. Remove this workshop from `kb/work/README.md`, and delete the workshop
   directory.
   Finished workshop files are not retained as a historical register.

## Closure checklist

- [x] Active MOC multistage run is accepted and promoted; its dated
      artifact disposition is recorded.
- [x] All candidates have dated resolutions: thirteen artifact dispositions and
      one explicit cohort removal.
- [x] General rule or explicit no-general-rule finding is promoted.
- [x] Write-time prior-art-check decision is recorded.
- [x] Durable findings are promoted.
- [ ] Workshop entry and directory are removed.
