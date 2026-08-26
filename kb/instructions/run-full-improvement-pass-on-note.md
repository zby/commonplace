---
description: Run the full improvement pipeline over one note, apply bounded edits that keep its claim, and require closing review to accept, repair once, or hand back the result.
type: kb/types/instruction.md
---

# Run a full improvement pass on one note

Sequence six method families — the compression bundle, `critique-note`, `composition-friction-gate` with its node-check companion `premise-decomposition-gate`, every catalog review bundle under `kb/instructions/review-gates/`, and `cp-skill-connect` — into one ordered pass over a single note. Reconcile their output into an editorial packet that identifies the note's warranted contribution and its disposition. Where the note keeps its claim, apply the packet's body edits, run a flow/coherence copyedit, and close review over the final text. Closing either accepts that text, permits one bounded recovery for defects the pass introduced, or restores the pass-start text and hands a claim-level or repeated failure back to the author. Where the initial findings require changing the note's claim, or removing or moving the note, stop after the packet and hand it back: the pass is a critique with a bounded repair, and a claim-level repair belongs to the author, who holds what the note is for. This instruction does not replace the individual methods; it orders them, settles their disagreements, and carries the result through to an accepted edited note or an explicit hand-back.

Catalog review bundles (always requested together in steps 5 and 10): `accessibility`, `complexity`, `frontmatter`, `prose`, `semantic`, `sentence`, `structural`. The selector skips gates that do not apply to the note's `type:` or `traits:`; do not treat a skipped gate as a passed gate.

`composition-friction-gate` and `premise-decomposition-gate` never resolve to a verdict: their product is routed attention for a human. This pass carries their output verbatim in the packet and uses it in exactly one way — as evidence in the decision table's objection question, which can only route the note to a pending hand-back, never to an applied edit. That is the boundary: a checker result may stop the pass and hand the note to a person; it may not change the note.

Inputs:

- `{note-path}` — repository-relative note path.
- `{model-partition}` — review model partition for the requested-mode selector calls, as `run-review-batches.md` requires. It has no default; record it in the packet.

Ownership precondition: from step 1 until the pass stops after step 7 or completes step 10, no other actor or process may edit `{note-path}`. The orchestrator's prescribed edits in steps 8 and 9 are the only exception. If step 7 inspects a proposed merge target, no other actor may edit that target until the packet is handed back. These are cooperative ownership rules, not filesystem locks; do not start the pass when they cannot be maintained.

Derive `<note-name>` once from the pass-start `{note-path}` as the filename without its extension. At the start of every invocation mint a unique `<pass-id>` (a UTC timestamp plus a short random suffix). Retain first-cycle reports under `kb/reports/full-pass/<note-name>/<pass-id>/{initial,closing}/`; a permitted recovery cycle writes `closing-recovery/`. Never reuse a pass ID or overwrite an initial or closing report. The `<note-name>` directory is historical packet identity: do not move or rename it if the note moves later.

## Execution roles and isolation

The parent agent running this instruction is the **orchestrator**. It alone creates jobs, dispatches workers, schedules around the harness concurrency limit, finalizes review output, copies retained artifacts, and edits the note. A dispatched worker performs the one review or copyedit task it receives and writes its result where told; it does not recursively start another sub-agent, and it never edits the note. After verifying the worker-owned output, the orchestrator releases that worker with the harness lifecycle operation before scheduling more work. Every worker is single-use.

A **fresh sub-agent** is a newly isolated execution context that has not participated in an earlier method or edit in this pass; a follow-up turn to an earlier worker is not fresh. When capacity is exhausted, queue work until a slot opens rather than nesting delegation or reusing a worker.

## Phases

The packet's `phase` field records where the pass is. It is distinct from `resolution`, which records the fate of a pending disposition. `closing_status` records whether closing is unreconciled (`null`), permits completion (`ready`), requires one bounded correction (`repair-needed`), or requires author action (`hand-back`). `closing_repair_attempted` records whether the one recovery allowance has been consumed.

| Phase | Meaning | Set when |
|---|---|---|
| *(no packet)* | reviewing: reports are being collected under `initial/` | pass directory created (step 1) |
| `packet` | the packet is written; a hand-back is complete here, and a `keep` stops here if its update is undetermined | step 7 |
| `editing` | the guard passed and body edits are being applied | step 8, before the first edit |
| `closing` | the copyedit is applied and captured; closing is running, needs its one recovery, or has handed back | step 9 onward |
| `complete` | closing status is `ready` and the packet validates | step 10 |

Transitions run forward only. Each phase or closing-status change is a frontmatter edit to the packet followed by `commonplace-validate <report-path>`. Packet and editing phases require `closing_status: null` and `closing_repair_attempted: false`; complete requires `closing_status: ready`.

## Re-entrancy preflight

Before minting a new pass ID, inspect `kb/reports/full-pass/<note-name>/` and every `kb/reports/full-pass/*/*/full-pass-report.md` whose `source` equals `{note-path}`. Match only this exact repository-relative path; do not use `properdocs.yml` redirects to infer identity, and never rewrite `source` or rename a packet directory.

- A pass directory with no `full-pass-report.md` is an orphan from an interrupted review phase. Stop; the operator deletes it or lets it be completed.
- A `keep` packet in phase `editing`, or in phase `closing` with `closing_status: null`, is an unfinished pass. Stop. Run `commonplace-guard-full-pass-report` on it: if the live note matches the packet's latest capture, the pass may be resumed from that phase; otherwise reconcile by hand before any new pass.
- A `keep` packet with `closing_status: repair-needed` may resume only through the bounded recovery below. A packet with `closing_status: hand-back` stops and is returned to the author; its guard must match the rolled-back pass-start text before any later work begins.
- A packet with `resolution: pending` (any of `revise`, `delete`, `merge`, `rehome`): run the guard. Exit 0 means the recommendation is still current — return it and stop. A `changed` input means the packet must be resolved to `superseded` under `resolve-full-pass-disposition.md` before a new pass starts. A `missing` or `corrupt-capture` input, or exit 2, blocks the pass until reconciled.
- A `rejected` packet: run the guard. Exit 0 keeps its rejection binding on step 7 — do not show it to review workers, and do not repeat the rejected disposition without materially new evidence. A `changed` input lifts the constraint and leaves the packet as history.
- `not-required` in phase `complete` with `closing_status: ready`, `accepted`, `alternative-applied`, and `superseded` packets do not block.

At most one pending packet may exist for a source path; more than one stops the pass for reconciliation.

## Why this order

- **Compression bundle first.** Across early validation cases it matched or exceeded standalone prune and split/rehome instructions and additionally covers core-claim-obscured and detail-overhang. It is the most reliable single source of edit-strategy signal and runs outside the review DB.
- **`critique-note` second.** An anchored, open-ended, report-kind assay targeting whether the retained central commitment is defensible, not whether the supporting material earns its space. Case 01 showed it flags overclaiming the compression criteria do not test for.
- **Friction and premise decomposition third**, adversarial, in separate fresh workers: friction checks the inferential joints, premise decomposition attacks the premises (routing each failure `LOCAL` or `GLOBAL`) and annotates each non-`HOLDS` premise's counterexample shape (`instance`, `prevalence`, `priced-exception`). An argument can carry valid inferences on a false premise — friction passes that, the premise gate catches it.
- **All catalog bundles fourth**, in one selector call. Case 02 showed `semantic` and compression diverge: a qualifier can be necessary for truth and still fail to earn its space. Keep complementary findings rather than letting one bundle veto another. Always run every applicable gate.
- **`cp-skill-connect` last of the report-only steps**, so its candidates reflect the same reading of the note that produced the earlier findings.
- **Contribution selection belongs in synthesis**, because it needs the artifact-supported intent, the warrant findings, compression's buried-versus-undetermined distinction, and connect's account of what the KB already supplies together. The packet's brief is a diagnostic reconstruction from the incumbent, not a record of the original commission — which is why a claim-level repair is handed back rather than made here.
- **Flow/coherence pass after body edits**, because compressing and cutting break the transitions the original prose relied on.
- **Several orthogonal checks, reconciled rather than voted.** Each method tests a structurally independent property; disagreement between them is signal to preserve.

## Procedure

1. Mint `<pass-id>` and create its `initial/` and `closing/` directories. Read `{note-path}` once as UTF-8 text, write that exact character sequence to `kb/reports/full-pass/<note-name>/<pass-id>/source.txt`, and compute its SHA-256. Retain the logical `{note-path}` as the historical `source`, alongside packet-relative `source.txt` and its hash. Never rewrite any member of this triple. Assessment methods receive `{note-path}`, never `source.txt`.
2. Run the compression bundle per `run-compression-bundle-on-note.md`, passing `kb/reports/full-pass/<note-name>/<pass-id>/initial/compression-bundle-review.md` as its `{output-path}`.
3. Run `critique-note` through the requested-mode review pipeline in a fresh sub-agent:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} critique --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Delegate and finalize as in `run-review-batches.md`, then immediately copy the finalized pair result to `initial/critique.md`, before any later finalization can prune its job artifacts.
4. Run `composition-friction-gate` in a fresh sub-agent; copy its report to `initial/friction.md`. Then run `premise-decomposition-gate` in a separate fresh sub-agent; copy its report to `initial/premises.md`. Neither emits PASS/WARN/FAIL.
5. Run every catalog review bundle through the requested-mode, single-note flow in `run-review-batches.md`:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} \
     accessibility complexity frontmatter prose semantic sentence structural \
     --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Delegate, finalize, and verify as that instruction describes. Copy every finalized pair result to `initial/<bundle>/<gate>.md`.
6. Run `cp-skill-connect` against the note and copy its canonical report to `initial/connect.md`; the closing run will overwrite the canonical path, never this copy.
7. Synthesize the retained reports into one typed packet at `kb/reports/full-pass/<note-name>/<pass-id>/full-pass-report.md` by answering the decision table below, in order. Write every frontmatter field and the canonical `Resolution` section shown in the Output Contract, with `phase: packet`, `closing_status: null`, and `closing_repair_attempted: false`. A `keep` packet starts `resolution: not-required`; `revise`, `delete`, `merge`, and `rehome` start `pending`. Run `commonplace-validate <report-path>` and stop on any failure.

   If the disposition is anything but `keep`, or the `Update` is `UNDETERMINED`, the pass ends here: leave the note byte-identical, retain the pass directory, and hand back the packet. Executing a hand-back belongs to whoever reads it, under `resolve-full-pass-disposition.md`.
8. **`keep` only.** Run `commonplace-guard-full-pass-report <report-path>`. Continue only on exit 0 with every input `matching`. On `changed`, do not edit; render the packet `superseded` with `version-guard` authority and stop. On `missing`, `corrupt-capture`, or exit 2, reconcile and leave the packet unchanged. After a successful guard set `phase: editing`, then apply the packet's body edits directly to the note. Body-edit actions are `remove`, `compress`, `add` (an answer to an answerable objection, at the point of attack), and `keep`. Do not change the title, thesis, or any title-as-claim; do not rename the file; do not edit citers. Then reread each friction and premise report's "For the human" line against the edited text: not a rerun, only a check that the thing it pointed to is still accurately described or actually addressed; if not, record that in Open items rather than re-editing.
9. Dispatch a fresh sub-agent with only the current note text and exactly this prompt: `revise the note for flow, coherence, logic and readability`. The worker writes its result to `kb/reports/full-pass/<note-name>/<pass-id>/copyedit-candidate.md` and nothing else. The orchestrator diffs the candidate against the note: it may reflow, reorder within a section, and tighten wording; it may not add claims, reintroduce material step 8 removed, change the title or thesis, or replace the selected contribution with a more generic treatment. Apply the acceptable parts to the note and discard the rest. Run `commonplace-validate {note-path}`; a failure is fixed before proceeding. Then write the note's exact text to immutable packet-relative `final.txt`, record `final_capture: final.txt` and `final_sha256`, keep `closing_status: null`, set `phase: closing`, and validate the packet. **Do not start step 10 before this.**
10. Run and reconcile the closing cycle below against the current final capture. Set `phase: complete` only when reconciliation sets `closing_status: ready`; a schema or deterministic validation failure leaves the pass in phase `closing`. `repair-needed` permits the one bounded recovery below. `hand-back` restores the pass-start text and stops.

## Decision table

Answer the four questions in order and record each answer in the packet. Derive every answer only from the artifact, the repository and collection contracts, the retained reports, explicit user direction, and retained intent that identifies its source, subject, scope, and role. Current user direction prevails. Do not add an ad hoc history search; do not treat model familiarity as evidence a contribution is old, or model surprise as evidence it matters.

**1. Warranted contribution.** Use an intended reader stated in the artifact when present; otherwise the consuming audience in the repository's KB purpose, narrowed by the collection contract. Answer: relative to that reader and the existing KB, what does this artifact warrant the reader to understand, infer, believe, or do that a generic treatment would not? Use connect to inform what the KB already supplies (it is candidate discovery, not an exhaustive ownership proof), critique and semantic findings to assess warrant, and compression to distinguish a buried contribution from an undetermined one. Set `Update` to one artifact-supported sentence, `UNDETERMINED`, or `NONE`. `UNDETERMINED` means materially different readings remain and no authorized input selects one; before finalizing it, ask the user one focused question presenting the choices, and record a live answer as the selecting input. `NONE` means no distinct contribution remains after excluding a distinct definition, record, reference, or audience-specific expository function; repairable warrant belongs in the Warrant field, not in `NONE`.

**2. Collection and type fit.** Read the target `COLLECTION.md` (including any "What does NOT belong here" list) and the note's `type:` spec. A note that describes one specific system fits `kb/notes/` when a substantive design-space claim remains after the local choices are scoped, as that contract allows; it fails when only procedure, description of one deployed system, or project-local operational voice remains. A misfit is `rehome` — whole, or a split when a separable transferable claim (identified in question 1) stands on its own once the local material is removed. Record the target collection and remedy.

**3. Strongest objection.** From critique, the premise and friction reports, and the grounding gate, name the strongest objection to the title-level claim and classify it:

- **answered** — the note already answers it, or the premise it targets returned `HOLDS` (an active counterexample hunt failed; a critique that re-asserts the objection does not lower warrant by itself).
- **answerable** — one passage the note could add, drawing on its own materials and the retained source, meets it. The passage is a body edit at the point of attack: an extension of warrant, not a hedge. The closing cycle then attacks the answer.
- **requires a claim change** — the objection defeats the claim as titled: a `DEFEATED` premise the commitment cannot survive without, a `semantic/grounding-alignment` FAIL on the passage carrying the claim, or an objection outside the decomposed premises that no such passage answers; or, independently of any objection, the warranted `Update` differs from the title in logical strength, direction, scope, modality, or category — including a title hedged *below* its warrant.

A `DOUBTFUL` premise or a critique that "partially lands" is at most answerable; the doubt routes to `## Scope` or Open items. Do not answer an objection by narrowing a definition: a definition that changes the claim's extension is a claim change. Whether a counterexample meets the note's antecedent as the note means it is the author's judgment, not the pass's — quote the counterexample and the passage it targets so the author can make it.

**4. Disposition.** Exactly one, note-level, from the answers above:

| Answer | Disposition | Handled |
|---|---|---|
| fit fails | `rehome` (whole or split) | pending hand-back |
| `Update` is `NONE` and another artifact owns the residue | `merge into <target>` | pending hand-back |
| `Update` is `NONE` and nothing owns it, or no passage earns its context cost, or the commitment is indefensible with no repair short of a different note | `delete` | pending hand-back |
| objection requires a claim change | `revise` | pending hand-back |
| `Update` is `UNDETERMINED` | `keep`, no body edits | stop at `packet` |
| otherwise | `keep` with body edits | steps 8–10 |

A `revise` packet records, without applying any of it: the objection and the evidence that decides it; one or more candidate replacement claims, each with the mode it would assert under `kb/notes/COLLECTION.md`'s claim-modality rules and the guard that mode carries (a statistical claim states what prevalence would refute it; an ideal-type claim needs its adequacy record); and the citer scope — every inbound link whose visible text or summary states the current claim. A near-duplicate surfaced by connect informs `merge`; it never justifies a passage-level cut. Do not reach a non-`keep` disposition by summing passage-level cuts.

For `merge`, treat the target as provisional until you read it fully, confirm the rationale still applies, write its exact UTF-8 text to packet-relative `merge-target.txt`, and record its logical path, H1, and hash. If the rationale fails against the captured target, choose another disposition; never retain provisional merge fields.

## Closing cycle

**Prerequisite:** phase `closing`, `closing_status: null` — the current final capture is written and `{note-path}` matches it. On the first cycle retain every report under `closing/`; after the one permitted recovery retain them under `closing-recovery/`. Leave `initial/` and every earlier closing directory byte-identical. Rerun every catalog bundle through the step-5 flow and critique through the step-3 flow against `{note-path}`; copy results to `<closing-dir>/<bundle>/<gate>.md` and `<closing-dir>/critique.md`. Rerun the compression bundle, both adversarial gates, and connect directly against the final text; retain them under `<closing-dir>/` (the premise report as `premises.md`; connect's canonical report copied as `connect.md`).

Review jobs snapshot `{note-path}` at pair creation, so every closing job is created after the final capture and no closing method reads any other version. Closing methods may run concurrently with each other.

Read every closing report against the current final note. Repeat question 1 against the same reader and KB baseline and record whether the final text strengthened, preserved, weakened, changed, or made the selected update undetermined. The friction and premise "For the human" lines remain routed attention. Then choose exactly one closing status:

- **`ready`** — the selected update is strengthened or preserved; closing finds no title-, thesis-, scope-, modality-, or category-level mismatch; and no defect introduced by steps 8 or 9 remains. Pre-existing residuals and non-blocking new attention go to Open items. Set `closing_status: ready`, set `phase: complete`, and validate the packet.
- **`repair-needed`** — the selected update remains strengthened or preserved and every pass-introduced defect is local: it can be corrected without changing the title, thesis, selected update, evidence, or another author-owned decision. This route is available only while `closing_repair_attempted: false`. Record the exact defects and their closing evidence, set `closing_status: repair-needed`, and validate the packet. Then run the guard against the current final capture, apply only those corrections, validate the note, write the new exact text to immutable `final-recovery.txt`, update `final_capture` and `final_sha256`, set `closing_repair_attempted: true` and `closing_status: null`, validate the packet, and rerun the complete closing suite under `closing-recovery/`. A changed final text invalidates every first-cycle closing result as completion evidence; rerun all methods, not only the ones that found the defect.
- **`hand-back`** — the selected update is weakened, changed, or undetermined; closing requires a title, thesis, scope, modality, category, or evidential decision; a newly introduced angle appears; or any pass-introduced defect remains after the one recovery. Record the exact author decision or exhausted defect. Run the guard against the current final capture, restore `{note-path}` from immutable `source.txt` byte-for-byte, point `final_capture` and `final_sha256` to `source.txt` and `source_sha256`, set `closing_status: hand-back`, validate the note and packet, and stop. This rollback removes the pass's edits from the live library while retaining every attempted final capture and closing report as evidence.

When a closing cycle finds both a local introduced defect and a claim-level failure, `hand-back` takes precedence. Do not spend the bounded recovery allowance making local prose cleaner around an author-owned decision. A finding is pass-introduced only when the source/final diff or the closing evidence locates it in steps 8 or 9; a merely stochastic disagreement with an initial reviewer is not enough. Do not start any further edit-and-review round.

Append:

```markdown
## Closing cycle
**Pass ID:** <pass-id>
**Assessed capture:** `<final_capture>` — `<final_sha256>`
**Cycle:** initial | recovery

| Method | Closing result | Residual routed to Open items |
|---|---|---|
| compression bundle | ... | yes/no |
| critique-note | report summary | yes/no |
| composition-friction-gate | SURVIVES/DISSOLVES summary | yes/no |
| premise-decomposition-gate | premise verdicts; any GLOBAL defeat | yes/no |
| accessibility / complexity / frontmatter / prose / semantic / sentence / structural | per-bundle pass/warn/fail summary | yes/no |
| connect | candidate summary | yes/no |
| warranted contribution | strengthened / preserved / weakened / changed / undetermined | yes/no |

**Closing status:** ready | repair-needed | hand-back
**Status basis:** <introduced defects, claim-level hand-back, or why remaining items are non-blocking>
```

## Reconciling passage-level findings

These rules govern body edits inside a `keep`; the decision table governs the note-level disposition.

- Default to the compression bundle's bias (compress, fold, delete) when it and `critique-note` disagree about a passage. Keep an addition critique proposes only when it answers an answerable objection. Before calling a proposed addition a hedge, state what the claim would need to look like if the objection were fully valid — if that changes the claim's scope, completeness, or a load-bearing precondition, it is a claim change, and the disposition is `revise`.
- Keep both a catalog-bundle finding and a compression finding on the same section; they test different properties. Keep overlapping `prose`/`sentence` and `semantic` findings when their tests differ; compress to one row only when finding and action are identical.
- Route `frontmatter` findings that need description changes into body edits; a finding that needs a title change is a claim change.
- Treat connect's candidates as additive outbound links, listed separately from body edits.
- Keep a body edit only when its rationale states how it surfaces or sharpens the selected update, strengthens or protects its warrant, or removes material that does none of those jobs.
- Carry friction and premise findings verbatim in "Routed attention". They are never converted into a passage action, and a passage that states a held premise is not removed on warrant grounds.

## Output Contract

`source` is the pass-start `{note-path}` whose text was copied into `source.txt`; set it once. The frontmatter description, report H1, displayed Target, and `<note-name>` directory likewise use the pass-start title or path and are never realigned. Each capture is immutable. `final_capture` points to the text the pass currently leaves: `final.txt` after the first edit, `final-recovery.txt` after the one recovery, or `source.txt` after a closing hand-back. The guard compares the live note against that latest capture.

```markdown
---
description: "Full improvement pass over <pass-start note title>"
type: kb/reports/types/full-pass-report.md
source: <pass-start note path>
source_capture: source.txt
source_sha256: <SHA-256 of source.txt as UTF-8 text>
pass_id: <pass-id>
phase: packet | editing | closing | complete
closing_status: null | ready | repair-needed | hand-back
closing_repair_attempted: false | true
disposition: keep | revise | delete | merge | rehome
merge_target: null | <target-path>
merge_target_capture: null | merge-target.txt
merge_target_title: null | <captured target H1>
merge_target_sha256: null | <SHA-256 of merge-target.txt>
final_capture: null | final.txt | final-recovery.txt | source.txt
final_sha256: null | <SHA-256 of final_capture>
resolution: not-required | pending
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []
---

# Full Improvement Pass: <pass-start note title>

**Target:** `<pass-start note path>`
**Model partition:** `<model-partition>`
**Reports used:** compression bundle, critique-note, composition-friction-gate, premise-decomposition-gate, catalog review bundles (`accessibility`, `complexity`, `frontmatter`, `prose`, `semantic`, `sentence`, `structural`), connect

## Warranted contribution
**Reader and prior:** <intended reader or use, the input that determines it, and the existing-KB baseline>
**Update:** <one artifact-supported sentence | UNDETERMINED | NONE>
**Why a generic treatment would not supply it:** <the specific delta, the competing choices when undetermined, or why no delta remains>
**Warrant:** <the evidence and reasoning route, preserving differences in epistemic status and naming repairable limits>
**Collection/type fit:** <FITS | MISPLACED — the failed requirement and the fitting collection>
**Strongest objection:** <answered | answerable | requires a claim change — the objection, and the premise verdict, passage, or grounding result that decides it>

## Disposition
**keep | revise | delete | merge into `<target-path>` | rehome** — <one line naming the deciding answer; for rehome: target collection and whole | split; for revise: the objection>

## Body edits
| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| ... | compression/branch-bloat | ... | remove/compress/add/keep | <how this affects the update or its warrant> |

## Revision brief
<`revise` only: the objection and its evidence; candidate replacement claims, each with its mode and that mode's guard; citer scope. For other dispositions: "—">

## Routed attention (composition-friction-gate and premise-decomposition-gate — not auto-resolved)
**Composition friction — filter verdict:** SURVIVES | DISSOLVES
<if DISSOLVES: the contradiction, verbatim>

**Composition friction — thinnest joints:**
1. <joint, quoted> — <UNSUPPORTED|THIN|HOLDS> — <what it fails to establish>

**Premise decomposition — premises:**
1. <premise, quoted> — <HOLDS|DOUBTFUL|DEFEATED> — <counterexample or reason> — <LOCAL|GLOBAL if not HOLDS> — <instance|prevalence|priced-exception if not HOLDS>

## Gate findings

### <Bundle>
| Gate | Result | Finding |
|---|---|---|

(one subsection per bundle that produced at least one applicable gate)

## Connection candidates
- <label> -> <target> — <reason, from connect report>

## Proposed revision shape
<outline of the note after the body edits, or "—" for a hand-back or undetermined update>

## Open items
<residual findings; routed-attention items the editor judges worth acting on; competing choices when undetermined>

## Resolution

**Status:** <not-required for keep | pending for revise, delete, merge, rehome>
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
```

Never omit "Warranted contribution", "Routed attention", or "Disposition". Quote or restate enough of each source report's substance that the packet stands alone; `kb/reports/full-pass/*` and the per-method report trees are gitignored inspection artifacts. Retain the pass directory while its packet or residual findings are in use; a pending packet is always in use.

## Do not

- Do not edit the note before step 8, and never for a disposition other than `keep`.
- Do not change a title, thesis, or title-as-claim inside the pass. A claim change is `revise`, handed back with the objection and candidate claims recorded.
- Do not skip a catalog bundle; let the selector skip non-applicable gates, not the orchestrator.
- Do not hand back raw reports as the deliverable; the packet is the point of steps 1–7.
- Do not convert a friction or premise finding into a passage action, and do not reach a disposition by summing passage-level cuts.
- Do not let the step-9 copyedit change claims, add material, or restore anything step 8 cut; if it does, the body edits left the note incoherent — fix the edit.
- Do not create closing jobs before the final capture exists.
- Do not set phase `complete` before closing status is `ready`, and do not use more than one bounded closing recovery.
- Do not begin any packet-driven edit, resolution, or follow-up without a successful `commonplace-guard-full-pass-report` result over every guarded input.

---

Relevant Notes:

- [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — why running compression, critique-note, the adversarial gates, the catalog bundles, and connect side by side catches more than repeating one check.
- [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md) — why step 7 reconciles complementary findings instead of voting one down.
- [Warranted reader update is the objective of substantive writing](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — rests-on: why the packet compares a specific reader update and its warrant with generic and existing-KB alternatives.
- [Narrowing bought to survive review is paid for in content](../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: why a claim change is handed back rather than applied — repair that optimizes defensibility drifts toward the untouchable claim.
- [Domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) — rests-on: the ideal-type mode guard a revision brief must carry.
- [Resolve a full-pass disposition](./resolve-full-pass-disposition.md) — applies-when: a pending revise, delete, merge, or rehome packet needs inspection or resolution.
