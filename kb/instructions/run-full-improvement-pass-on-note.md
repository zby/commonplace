---
description: Run the full improvement pass over one note with commonplace-review run full-pass; the packet, editor and closing workers read this page as their instruction.
type: types/instruction.md
---

# Run a full improvement pass on one note

The pass runs six method families over one note: the compression bundle, `critique-note`, `composition-friction-gate` with its node-check companion `premise-decomposition-gate`, every catalog review bundle under [review-gates/](./review-gates/), and `cp-skill-connect`. A packet reconciles their output into the note's warranted contribution and its disposition. Where the note keeps its claim, an editor applies the packet's body edits, a copyeditor fixes flow and coherence, and a closing cycle reviews the final text. Closing either accepts that text, permits one bounded repair of defects the pass introduced, or leaves the note at its pass-start text and hands the result back to the author. Where the findings require changing the note's claim, or removing or moving the note, the pass stops after the packet and hands it back: a claim-level repair belongs to the author, who holds what the note is for. The pass does not replace the individual methods; it orders them, settles their disagreements, and carries the result to an accepted edited note or an explicit hand-back.

`composition-friction-gate` and `premise-decomposition-gate` never resolve to a verdict: their product is routed attention for a human. The packet carries their output verbatim and uses it in exactly one way — as evidence in the decision table's objection question, which can only route the note to a pending hand-back, never to an applied edit. That is the boundary: a checker result may stop the pass and hand the note to a person; it may not change the note.

## Running the pass

```bash
commonplace-review run full-pass <note-path> [--direction TEXT] [--profile NAME]
```

The command runs the pass as a workflow in the run directory `kb/reports/state/review/runs/full-pass/<note path without .md>/<first 12 hex of the note's SHA-256>/`. Each method, the packet, the editor, the copyeditor and each closing status is one headless worker ask. Workers write only their output files. Every worker receives the text under review as an input: the start text, or the edited text the pass carries forward. The note's file in the checkout may hold an older text. The command alone writes the note, once, at the end of the pass.

- **Methods.** The compression bundle, friction, premises and connect each write one report. The catalog bundles and `critique-note` are asked over the text under review, one worker per bundle; a stored result does not replace the ask. The selector skips gates that do not apply to the `type:` or `traits:` of the text under review; a skipped gate is not a passed gate. When the pass ends, the command writes review result files once, for the text the note then holds: the last closing cycle's verdicts after an applied edit, the initial verdicts otherwise. A stop or a conflict writes none.
- **Packet.** One worker answers the decision table below from the method reports and writes the packet.
- **Edit.** For `keep` with a determined update, an editor writes the edited note and a copyeditor copyedits it. The command rejects a text that changes the frontmatter `title` or `type` or the H1, keeps `user-verified` after a body change, or adds a validation failure; the worker writes it again with those problems.
- **Closing.** The methods run again over the edited text, and one worker chooses the closing status. The command applies it: `ready` ends the pass, `repair-needed` allows one repair and a new closing cycle over the repaired text, and `hand-back` ends the pass with the note untouched.

On `ready`, the command writes the packet and then the final text to the note. It writes the note only when the file still holds the start text. If the note changed during the pass, the command writes nothing and reports a conflict that names the run file holding the proposed text. Each accepted edited text stays in the run's `artifact/texts/`.

The note's current packet is kept at `kb/reports/state/review/packets/<note-path>`, with a copy in the run's `artifact/packet.md`. A pass does not start while the note's current packet is `pending` and still matches the note; the command returns that packet instead. Resolve it under [resolve a full-pass disposition](./resolve-full-pass-disposition.md), or change the note.

The command prints a JSON report: run directory, disposition, closing status, the run file holding the proposed text, whether the note was written, the packet path, and a checkout guard that ignores the pass's own write. It exits 0 for an accepted edit or a hand-back packet, 1 for a stop or a conflict, and 2 when the command failed.

- After a launch failure or usage limit, repeat the same command. While the note is unchanged, the run continues and answered calls replay. An edited note opens a new run.
- After a worker problem, read it in the report, then `commonplace-review retry RUN JOB` and repeat the command.
- When the packet's update is `UNDETERMINED`, the packet lists the competing readings. Answer by repeating the command with `--direction "<the chosen reading>"`; the pending packet does not block it, and the packet is decided again over the same method reports. The run records the direction, so a later repeat without `--direction` keeps it.

## Why this order

- **Compression bundle first.** Across early validation cases it matched or exceeded standalone prune and split/rehome instructions and additionally covers core-claim-obscured and detail-overhang. It is the most reliable single source of edit-strategy signal.
- **`critique-note` beside it.** An anchored, open-ended, report-kind assay targeting whether the retained central commitment is defensible, not whether the supporting material earns its space. Case 01 showed it flags overclaiming the compression criteria do not test for.
- **Friction and premise decomposition**, adversarial, in separate workers: friction checks the inferential joints, premise decomposition attacks the premises (routing each failure `LOCAL` or `GLOBAL`) and annotates each non-`HOLDS` premise's counterexample shape (`instance`, `prevalence`, `priced-exception`). An argument can carry valid inferences on a false premise — friction passes that, the premise gate catches it.
- **All catalog bundles.** Case 02 showed `semantic` and compression diverge: a qualifier can be necessary for truth and still fail to earn its space. Keep complementary findings rather than letting one bundle veto another.
- **`cp-skill-connect` over the same text**, so its candidates reflect the same reading of the note that produced the other findings.
- **Contribution selection belongs in the packet**, because it needs the artifact-supported intent, the warrant findings, compression's buried-versus-undetermined distinction, and connect's account of what the KB already supplies together. The packet's brief is a diagnostic reconstruction from the incumbent, not a record of the original commission — which is why a claim-level repair is handed back rather than made here.
- **Copyedit after body edits**, because compressing and cutting break the transitions the original prose relied on.
- **Several orthogonal checks, reconciled rather than voted.** Each method tests a structurally independent property; disagreement between them is signal to preserve.

## Decision table

Answer the four questions in order and record each answer in the packet. Derive every answer only from the artifact, the repository and collection contracts, the method reports, explicit operator direction, and retained intent that identifies its source, subject, scope, and role. Operator direction given to the packet prevails. Do not add an ad hoc history search; do not treat model familiarity as evidence a contribution is old, or model surprise as evidence it matters.

**1. Warranted contribution.** Use an intended reader stated in the artifact when present; otherwise the consuming audience in the repository's KB purpose, narrowed by the collection contract. Answer: relative to that reader and the existing KB, what does this artifact warrant the reader to understand, infer, believe, or do that a generic treatment would not? Use connect to inform what the KB already supplies (it is candidate discovery, not an exhaustive ownership proof), critique and semantic findings to assess warrant, and compression to distinguish a buried contribution from an undetermined one. Set `Update` to one artifact-supported sentence, `UNDETERMINED`, or `NONE`. `UNDETERMINED` means materially different readings remain and no authorized input selects one; state the competing readings as one focused question for the operator in Open items. `NONE` means no distinct contribution remains after excluding a distinct definition, record, reference, or audience-specific expository function; repairable warrant belongs in the Warrant field, not in `NONE`.

**2. Collection and type fit.** Read the target `COLLECTION.md` (including any "What does NOT belong here" list) and the note's `type:` spec. A note that describes one specific system fits `kb/theory/` when a substantive design-space claim remains after the local choices are scoped, as that contract allows; it fails when only procedure, description of one deployed system, or project-local operational voice remains. A misfit is `rehome` — whole, or a split when a separable transferable claim (identified in question 1) stands on its own once the local material is removed. Record the target collection and remedy.

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
| `Update` is `UNDETERMINED` | `keep`, no body edits | pending hand-back at the packet |
| otherwise | `keep` with body edits | edit, copyedit, closing |

A `revise` packet records, without applying any of it: the objection and the evidence that decides it; one or more candidate replacement claims, each with the mode it would assert under `kb/theory/COLLECTION.md`'s claim-modality rules and the guard that mode carries (a statistical claim states what prevalence would refute it; an ideal-type claim needs its adequacy record); and the citer scope — every inbound link whose visible text or summary states the current claim. A near-duplicate surfaced by connect informs `merge`; it never justifies a passage-level cut. Do not reach a non-`keep` disposition by summing passage-level cuts.

For `merge`, treat the target as provisional until you read it fully and confirm the rationale still applies. If the rationale fails against the target, choose another disposition. The command records the target's hash when it writes the packet.

## Reconciling passage-level findings

These rules govern body edits inside a `keep`; the decision table governs the note-level disposition.

- Default to the compression bundle's bias (compress, fold, delete) when it and `critique-note` disagree about a passage. Keep an addition critique proposes only when it answers an answerable objection. Before calling a proposed addition a hedge, state what the claim would need to look like if the objection were fully valid — if that changes the claim's scope, completeness, or a load-bearing precondition, it is a claim change, and the disposition is `revise`.
- Keep both a catalog-bundle finding and a compression finding on the same section; they test different properties. Keep overlapping `prose`/`sentence` and `semantic` findings when their tests differ; compress to one row only when finding and action are identical.
- Route `frontmatter` findings that need description changes into body edits; a finding that needs a title change is a claim change.
- Treat connect's candidates as additive outbound links, listed separately from body edits.
- Keep a body edit only when its rationale states how it surfaces or sharpens the selected update, strengthens or protects its warrant, or removes material that does none of those jobs.
- Carry friction and premise findings verbatim in "Routed attention". They are never converted into a passage action, and a passage that states a held premise is not removed on warrant grounds.

## Packet

The packet's frontmatter holds the decision fields the command asks for: `disposition` (`keep`, `revise`, `delete`, `merge` or `rehome`), `update` (`determined` for one artifact-supported sentence, `undetermined` or `none`), and `merge-target` (the target's repository path for `merge`, otherwise null). The command adds the note path, hashes, run and resolution fields. The body has these sections; never omit "Warranted contribution", "Disposition" or "Routed attention". Quote or restate enough of each method report's substance that the packet stands alone: the reports live only in the run directory.

```markdown
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

## Open items
<residual findings; routed-attention items worth acting on; the focused question when the update is undetermined>
```

## Body edits

For `keep` with a determined update, apply the packet's body edits to the note text you are given. Body-edit actions are `remove`, `compress`, `add` (an answer to an answerable objection, at the point of attack), and `keep`. Do not change the title, thesis, or any title-as-claim; do not edit other files. If any body edit was applied and the note carries `user-verified`, remove that field: an applied body edit is substantive, and only a human may restore verification (see the [note type](../types/note.md)). Description changes routed from `frontmatter` findings are allowed.

A **repair** applies only the corrections of the closing defects it is given, under the same bounds.

## Copyedit

Copyedit the note text you are given for flow, coherence, logic, and readability. You may reflow, reorder within a section, and tighten wording. Preserve the title, the thesis, every claim, the evidence, the sources, the frontmatter exactly, and every cut the text already reflects; add no material and restore nothing. If a useful change would be substantive, leave that passage as it is.

## Closing cycle

The closing worker reads every closing report against the final text. Repeat question 1 against the same reader and KB baseline and record whether the final text strengthened, preserved, weakened, changed, or made the selected update undetermined. The friction and premise "For the human" lines remain routed attention. Then choose exactly one closing status:

- **`ready`** — the selected update is strengthened or preserved; closing finds no title-, thesis-, scope-, modality-, or category-level mismatch; and no defect introduced by the edit or copyedit remains. Pre-existing residuals and non-blocking new attention go to the record's residual column.
- **`repair-needed`** — the selected update remains strengthened or preserved and every pass-introduced defect is local: it can be corrected without changing the title, thesis, selected update, evidence, or another author-owned decision. List the exact defects and their closing evidence. Only the initial closing cycle may choose it; after the repair, the recovery cycle reruns every method, because a changed final text invalidates every earlier closing result.
- **`hand-back`** — the selected update is weakened, changed, or undetermined; closing requires a title, thesis, scope, modality, category, or evidential decision; a newly introduced angle appears; or any pass-introduced defect remains after the one repair. Record the exact author decision or exhausted defect. The command leaves the note at its pass-start text and keeps every closing record in the packet as evidence.

When a closing cycle finds both a local introduced defect and a claim-level failure, `hand-back` takes precedence. Do not spend the repair making local prose cleaner around an author-owned decision. A finding is pass-introduced only when the difference between the start and final texts or the closing evidence locates it in the edit or copyedit; a merely stochastic disagreement with an initial reviewer is not enough.

The closing record, written after the decision fields:

```markdown
| Method | Closing result | Residual routed to Open items |
|---|---|---|
| compression bundle | ... | yes/no |
| critique-note | report summary | yes/no |
| composition-friction-gate | SURVIVES/DISSOLVES summary | yes/no |
| premise-decomposition-gate | premise verdicts; any GLOBAL defeat | yes/no |
| catalog review gates | per-bundle pass/warn/fail summary | yes/no |
| connect | candidate summary | yes/no |
| warranted contribution | strengthened / preserved / weakened / changed / undetermined | yes/no |

**Status basis:** <introduced defects, claim-level hand-back, or why remaining items are non-blocking>
```

## Do not

- Do not change a title, thesis, or title-as-claim inside the pass. A claim change is `revise`, handed back with the objection and candidate claims recorded.
- Do not hand back raw reports as the deliverable; the packet is the point of the method reports.
- Do not convert a friction or premise finding into a passage action, and do not reach a disposition by summing passage-level cuts.
- Do not let the copyedit change claims, add material, or restore anything the body edits cut; if the body edits left the note incoherent, that is a closing defect.
- Do not act on a pending packet without `commonplace-review packet` reporting that its recorded hashes still match.

---

Relevant Notes:

- [Error correction works with above-chance oracles and decorrelated checks](../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — why running compression, critique-note, the adversarial gates, the catalog bundles, and connect side by side catches more than repeating one check.
- [Synthesis is not error correction](../theory/synthesis-is-not-error-correction.md) — why the packet reconciles complementary findings instead of voting one down.
- [Warranted reader update is the objective of substantive writing](../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) — rests-on: why the packet compares a specific reader update and its warrant with generic and existing-KB alternatives.
- [Narrowing bought to survive review is paid for in content](../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: why a claim change is handed back rather than applied — repair that optimizes defensibility drifts toward the untouchable claim.
- [Domain pricing routes an exception to idealization assessment but does not decide it](../theory/domain-pricing-routes-an-exception-to-idealization-assessment.md) — rests-on: the ideal-type mode guard a revision brief must carry.
- [Resolve a full-pass disposition](./resolve-full-pass-disposition.md) — applies-when: a pending revise, delete, merge, rehome, undetermined or hand-back packet needs inspection or resolution.
