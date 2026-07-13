---
description: Run the full improvement pipeline over one note, apply its editorial packet, then close review over the resulting text with one assay cycle.
type: kb/types/instruction.md
---

# Run a full improvement pass on one note

Sequence five validated method families — the compression bundle, `critique-note`, `composition-friction-gate`, every catalog review bundle under `kb/instructions/review-gates/`, and `cp-skill-connect` — into one ordered pass over a single note, reconcile their output into one editorial packet, apply it, run a flow/coherence copyedit, and close review over the final text with one assay cycle. This instruction does not replace the individual methods; it orders them, settles the disagreements between them, and carries the result through to an edited and re-assayed note. Method fit varies by note shape — treat a note whose shape surprises you with extra scrutiny; the per-method rationale below (see "Why this order") states what each validation run actually found.

Catalog review bundles (always requested together in steps 5 and 10): `accessibility`, `complexity`, `frontmatter`, `prose`, `semantic`, `sentence`, `structural`. The selector skips gates that do not apply to the note's `type:` or `traits:`; do not treat a skipped gate as a passed gate.

`composition-friction-gate` sits oddly here: its own hard rule is that it must never resolve to a verdict, because its output is meant for a human to judge, not to be graded by the same kind of agent that wrote or would edit the note. Running it inside an agent-driven synthesis step is in tension with that design — see the reconciliation rule below for how this instruction tries to avoid re-creating the false-confidence failure the gate exists to prevent. Five validation runs found real signal from this step every time, twice independently corroborating `critique-note` on the same sentence — but none has yet produced a genuine same-passage conflict between two methods; judge one on its own terms if it comes up.

Inputs:

- first and only argument: `{note-path}` — repository-relative note path.

Concurrency precondition: from step 1 until the pass stops after step 8 or completes step 10, no other actor or process may edit `{note-path}`. The orchestrator's prescribed edits in steps 8 and 9 are the only exception. If step 7 inspects a proposed merge target, no other actor or process may edit that target until the packet is finalized and handed back. These are cooperative ownership rules, not filesystem locks; do not start the pass when they cannot be maintained.

Derive `<note-name>` from `{note-path}` as the filename without its extension (`kb/notes/linking-theory.md` → `linking-theory`). At the start of every invocation mint a unique `<pass-id>` (a UTC timestamp plus a short random suffix is sufficient). Retain reports under `kb/reports/full-pass/<note-name>/<pass-id>/{initial,closing}/`; never reuse a pass ID or overwrite an initial report.

Steps 1 through 7 below only write reports; none of them edit the note. For a `keep` Disposition, steps 8 and 9 apply the packet and run a final flow pass, and step 10 closes review over those edits without starting another transformation round. When step 7 concludes the note should not exist as a unit (Disposition `delete` or `merge`), leave the note byte-identical and stop after handing back the packet — see step 8.

## Execution roles and isolation

The parent agent running this instruction is the **orchestrator**. It alone creates jobs, dispatches workers, schedules around the harness concurrency limit, finalizes review output, copies retained artifacts, and edits the note. A dispatched worker performs the one review or copyedit task it receives; it does not recursively start another sub-agent merely because the invoked method requires a fresh reviewer. After verifying the worker-owned output, the orchestrator closes, terminates, or releases that worker with the harness lifecycle operation before scheduling more work. Every worker in this pass is single-use.

Here, **fresh sub-agent** means a newly isolated execution context that has not participated in an earlier method or edit in this pass. A follow-up turn to an earlier worker is not fresh. When capacity is exhausted, queue work until a slot opens rather than nesting delegation or reusing a worker. Step 9 has the strictest isolation: its worker must be new to the pass and receive only the current note text and the exact copyedit prompt.

## Re-entrancy preflight

Before minting a new pass ID, inspect existing `kb/reports/full-pass/*/*/full-pass-report.md` files whose `source` equals `{note-path}`:

- If one has `resolution: pending`, run `commonplace-guard-full-pass-report <report-path>`. Exit 0 means the old recommendation is still current: return that report and stop. Exit 1 with a `changed` input means the old report must be resolved to `superseded` under `kb/instructions/resolve-full-pass-disposition.md` before a new pass starts. A `missing` or `corrupt-capture` result requires reconciliation and blocks a new pass. Exit 2 means the report is invalid and also blocks the pass.
- If a prior report is `rejected`, run the guard. Exit 0 retains its resolution for step 7 synthesis: do not show it to review workers, and do not repeat the rejected disposition without materially new evidence. Exit 1 with `changed` removes that constraint while preserving the old report as history. A `missing` or `corrupt-capture` result, or exit 2, requires reconciliation before a new pass.
- `not-required`, `accepted`, `alternative-applied`, and `superseded` reports do not block a new pass.

At most one matching pending report may exist for a source. If more than one exists, stop for reconciliation.

## Why this order

- **Compression bundle first.** Across early validation cases, the compression bundle (`kb/instructions/compression-bundle/README.md`, run via `run-compression-bundle-on-note.md`) matched or exceeded earlier standalone prune and split/rehome instruction drafts and additionally covers core-claim-obscured and detail-overhang. It is the most reliable single source of edit-strategy signal (compress, fold, delete, rehome), and runs outside the review DB — no freshness baseline state written.
- **`critique-note` second.** This anchored, open-ended, report-kind assay targets whether the retained central commitment is actually defensible, not whether the supporting material earns its space. It writes a freshness baseline and completes with `REPORT`, not an outcome. Case 01 showed it flags overclaiming the compression criteria do not test for, because compression assumes the material is already true and asks only whether it earns its place.
- **`composition-friction-gate` third.** A third orthogonal axis again: not context cost, not defensibility against an opponent, but whether the claim survives concretization at all and which inferential joints are least supported. Like `critique-note` it runs adversarially in a fresh sub-agent, so it sits next to it in the sequence. Unlike every other step here, it must not resolve to PASS/WARN or remove/compress/keep — see "Reconciling disagreement" for how its output is carried into the packet without collapsing that rule.
- **All catalog review bundles, always fourth.** Run every bundle under `kb/instructions/review-gates/` in one requested-mode selector call. Each bundle is an orthogonal lens; together they cover truth and grounding (`semantic`), metadata-as-claim (`frontmatter`), section shape and proportion (`complexity`), paragraph rhetoric and reference hygiene (`prose`), sentence clarity and attribution (`sentence`), presentation structure (`structural`), and reader load from opaque terms (`accessibility`). Case 02 showed `semantic` and compression can diverge sharply: `semantic/load-bearing-qualifiers` positively defended a section that marginal-value-redundancy correctly flagged, because semantic gates ask whether qualifiers are necessary for truth, not whether a paragraph adds marginal value. The same non-correlation applies across bundles — keep complementary findings rather than letting one bundle veto another. Like critique, this step writes freshness baselines; unlike critique, verdict-kind pairs complete with outcomes. It always runs every applicable gate rather than substituting judgment about whether the note looks mature enough to skip a lens.
- **`cp-skill-connect` last of the report-only steps.** Connect summarizes the note's current claim, mechanism, and tensions to prospect for links; running it last means the synthesis packet's connection candidates reflect the same reading of the note that produced the earlier findings, instead of being a disconnected report gathered at a different point in the reasoning.
- **Flow/coherence pass after body edits, not before.** Compressing, deleting, and rehoming material breaks transitions the original prose relied on. Running a readability pass before those edits land would polish sentences this instruction is about to cut; it belongs after the substantive content is settled.
- **Why several orthogonal checks at all, and why synthesis over voting.** Each of compression, critique-note, composition-friction-gate, the catalog bundles, and connect tests a different, structurally independent property, so their failures don't correlate the way repeated passes of the same check would. Step 7 reconciles by keeping complementary findings rather than voting one down — these methods answer different sub-problems, not the same question twice, so disagreement between them is signal to preserve, not noise to resolve by majority.

## Procedure

1. Mint `<pass-id>` and create its `initial/` and `closing/` directories. Read `{note-path}` once as UTF-8 text, write that exact Unicode character sequence as UTF-8 to `kb/reports/full-pass/<note-name>/<pass-id>/source.txt`, and compute the SHA-256 of the capture's UTF-8 text. Retain the logical `{note-path}`, packet-relative `source.txt`, and hash as three separate values. Never rewrite the capture. Then read the target note normally for the pass; assessment methods continue to receive `{note-path}`, never `source.txt`.
2. Run the compression bundle per `run-compression-bundle-on-note.md` (`kb/instructions/run-compression-bundle-on-note.md`), passing `kb/reports/full-pass/<note-name>/<pass-id>/initial/compression-bundle-review.md` as its `{output-path}` argument. No DB writes.
3. Run `critique-note` through the requested-mode review pipeline in a fresh sub-agent:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} critique --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Delegate and finalize as in `run-review-batches.md`, then immediately copy the finalized pair result to `kb/reports/full-pass/<note-name>/<pass-id>/initial/critique.md`. Do this before any later finalization can prune its job artifacts.
4. Run `composition-friction-gate` (`kb/instructions/composition-friction-gate.md`) in a fresh sub-agent against the same note. Copy its report to `kb/reports/full-pass/<note-name>/<pass-id>/initial/friction.md`. It will not, and must not, emit a PASS/WARN/FAIL verdict — only a filter result (SURVIVES/DISSOLVES) and a ranked list of the thinnest inferential joints.
5. Run every catalog review bundle through the requested-mode, single-note flow in `kb/instructions/run-review-batches.md`:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} \
     accessibility complexity frontmatter prose semantic sentence structural \
     --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Then delegate, finalize, and verify exactly as that instruction describes.
   Immediately copy every finalized pair result to `kb/reports/full-pass/<note-name>/<pass-id>/initial/<bundle>/<gate>.md`, preserving one file per gate under its bundle subdirectory (`semantic/completeness-boundary-cases.md`, `prose/source-residue.md`, and so on).
6. Run `cp-skill-connect` against the note and immediately copy its canonical report to `kb/reports/full-pass/<note-name>/<pass-id>/initial/connect.md`. The closing connect run writes the same canonical report path and will overwrite it; the pass-scoped copy is the retained initial evidence.
7. Synthesize the retained reports (below) into one typed packet at `kb/reports/full-pass/<note-name>/<pass-id>/full-pass-report.md`, including the note-level Disposition (`keep`, `delete`, or `merge into <target>` — see "Reconciling disagreement"). This is the only step among 1–7 that reconciles disagreement; do not just concatenate the reports.

   If the disposition is `merge`, treat the target as provisional until you read it fully, confirm that the rationale still applies, write its exact UTF-8 text to packet-relative `merge-target.txt`, and record its logical path, H1 title, and text SHA-256. From that capture until the report is finalized, no other actor may edit the target. If the rationale fails against the captured target, choose `keep` or `delete` instead; do not retain provisional merge fields.

   Write every frontmatter field and the canonical `Resolution` section shown in the Output Contract. A `keep` report starts `not-required`; `delete` and `merge` start `pending`. Run `commonplace-validate <report-path>` and stop on any failure.
8. Read the packet's Disposition first. If it is `delete` or `merge`, do not edit the note or apply the packet's body edits. Leave the note byte-identical, retain the pass directory, hand back `kb/reports/full-pass/<note-name>/<pass-id>/full-pass-report.md`, and stop the pass — skip steps 9 and 10. The packet is the sole handoff until the disposition is accepted, rejected, or superseded; executing the deletion or merge belongs to whoever reads it, not to this instruction.

   Otherwise (Disposition `keep`), run `commonplace-guard-full-pass-report <report-path>` immediately before the first edit. Continue only on exit 0 with every input `matching`. On exit 1 with `changed`, do not edit the note; render the report as `superseded` with `version-guard` authority and stop. A `missing` or `corrupt-capture` result, or exit 2, requires reconciliation and leaves the report unchanged.

   After a successful guard, apply the packet's body edits directly to the note. If `composition-friction-gate` ran, reread its report's "For the human" line against the edited text before moving on. This is not a re-run of the gate — just a check that the one thing it pointed to is still accurate, or has actually been addressed, now that the edit has changed the prose around it. If it looks wrong given the edit, note that in the packet's Open items rather than silently re-editing.
9. Run a final revise pass over the edited note with exactly this prompt: `revise the note for flow, coherence, logic and readability`. Give a newly isolated sub-agent that performed no earlier work in this pass (or yourself, if editing directly) only the current note text and that prompt — not the packet or the underlying reports. Do not use a follow-up turn to a reviewer from steps 2–6. This step is a copyedit pass, not a second chance to re-open the content decisions steps 1–8 already made; it should not reintroduce material step 8 removed or add new claims. **Do not start step 10 until this step completes and `{note-path}` is stable on disk.**
10. Run one closing cycle over all five method families, as specified in "Closing cycle" below — **only after step 9 has finished**. Append its summary to `full-pass-report.md`; route residual findings to Open items and stop after this one cycle.

### Synchronization: steps 8–10

Steps 8, 9, and 10 are a **strict pipeline**, not a parallel batch. The note has one authoritative "final" version for the closing cycle; every closing assay must read that same version.

| Barrier | Rule |
|---|---|
| 8 → 9 | Start step 9 only after step 8 body edits (and any friction reread) are committed. |
| 9 → 10 | **Hard stop:** do not create closing review jobs, dispatch closing workers, or rerun any closing method until step 9's copyedit is complete and verified on disk. |
| Within 10 | Closing methods may run concurrently with each other **only after** the step-9 barrier clears. Every closing run — including critique and catalog-bundle review jobs — must target the post-step-9 bytes. |

Review jobs snapshot `{note-path}` at **pair create**, not at finalize. A closing `critique-note` or catalog-bundle job queued while step 9 is still running will pin freshness to pre-copyedit text even if finalization happens later. Wait for step 9, then record the final note SHA-256, then begin step 10.

## Closing cycle

**Prerequisite:** step 9 complete; `{note-path}` byte-stable. Record the final note SHA-256 **now** — before creating any closing review job or dispatching any closing worker. Retain every closing report under `closing/` and leave `initial/` byte-identical. Rerun every catalog review bundle through the step-5 flow against the final note:

```bash
commonplace-review-target-selector --mode requested --model-partition {model-partition} \
  accessibility complexity frontmatter prose semantic sentence structural \
  --note {note-path} --json \
  | commonplace-create-review-jobs --input - --grouping note
```

Rerun critique through the step-3 flow. Immediately copy finalized catalog-bundle results into `closing/<bundle>/<gate>.md` and copy critique into `closing/critique.md`.

Rerun the compression bundle, composition-friction-gate, and connect directly against the final text. Retain them under `closing/`. Copy connect's canonical report into `closing/connect.md` immediately after the skill returns; this closing run overwrites the canonical report used in step 6 but never the retained `initial/connect.md`.

Read every closing report against the edited note. Add any remaining actionable finding to the packet's Open items; do not start another edit-and-review round. The friction report's "For the human" line remains routed attention and must not be collapsed into an automatic verdict.

Append this section to the packet:

```markdown
## Closing cycle
**Pass ID:** <pass-id>

| Assay | Closing result | Residual routed to Open items |
|---|---|---|
| compression bundle | ... | yes/no |
| critique-note | report summary | yes/no |
| composition-friction-gate | SURVIVES/DISSOLVES summary | yes/no |
| accessibility / complexity / frontmatter / prose / semantic / sentence / structural | per-bundle pass/warn/fail summary | yes/no |
| connect | candidate summary | yes/no |
```

## Reconciling disagreement

- Default to the compression bundle's bias (compress, fold, delete, or rehome) when it and `critique-note` disagree about a passage. `critique-note`'s natural repair path tends to add qualification; only keep an addition it proposes when the addition is what makes the central claim defensible against the strongest attack, not merely a hedge against a possible objection. Before calling a finding a hedge, state what the note's claim would need to look like if the objection were fully valid — if that changes the claim's scope, completeness, or a load-bearing precondition, it is not a hedge, no matter how easy the label is to reach for.
- If any catalog bundle warns on a section the compression bundle passed (or vice versa), keep both findings in the packet rather than picking a winner — they test different properties (truth, grounding, clarity, shape, metadata, accessibility vs. context cost) and a note can fail one without failing the other.
- If `prose` or `sentence` findings overlap with `semantic` findings on the same passage, keep both when the underlying tests differ (for example grounding alignment vs. parsing ambiguity); compress to one row only when the finding and recommended action are identical.
- Route `frontmatter` findings that require title or description changes into Body edits with explicit actions; do not leave metadata fixes only in Open items when the packet already commits to substantive edits.
- Treat connect's candidates as additive: they extend the note's outbound links and do not bear on whether body content should be cut, so list them separately from the body-edit recommendations. One exception: a near-duplicate connect surfaces may inform the packet's Disposition (next bullet) — it still never justifies a passage-level cut.
- **Disposition is a note-level judgment, made once in step 7.** Set `delete` or `merge into <target>` only when a finding is about the note as a unit, not about a passage: connect surfaces an existing note that already carries the same claim and mechanism (merge); the compression bundle finds no passage that earns its context cost (delete); or `critique-note` shows the central commitment indefensible with no repair short of a different note (delete, with the packet recording what a replacement would need). Do not reach a non-`keep` disposition by summing passage-level cuts — a note every section of which got compressed can still deserve to exist.
- **Carry `composition-friction-gate`'s findings unresolved.** Do not convert its filter verdict or its ranked joints into a remove/compress/keep action the way the other methods' findings are converted. Put them in the packet's dedicated "Routed attention" section verbatim, out of scope for step 8's automatic application — the same status as the "Open items" section, not a body edit. This is the one deliberate exception to "reconcile, don't concatenate" — reconciling this gate's output the way the others are reconciled would recreate the self-graded verdict its own hard rule forbids. If a thin joint turns out, on the editor's judgment, to need a real fix, that judgment call belongs to whoever reads the packet, not to this instruction.

## Output Contract

```markdown
---
description: "Full improvement pass over <note title>"
type: kb/reports/types/full-pass-report.md
source: <note-path>
source_capture: source.txt
source_sha256: <SHA-256 of source.txt as UTF-8 text>
pass_id: <pass-id>
disposition: keep | delete | merge
merge_target: null | <target-path>
merge_target_capture: null | merge-target.txt
merge_target_title: null | <captured target H1>
merge_target_sha256: null | <SHA-256 of merge-target.txt as UTF-8 text>
resolution: not-required | pending
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []
---

# Full Improvement Pass: <note title>

**Target:** `<note-path>`
**Reports used:** compression bundle, critique-note, composition-friction-gate, catalog review bundles (`accessibility`, `complexity`, `frontmatter`, `prose`, `semantic`, `sentence`, `structural`), connect

## Strongest retained claim
<one sentence, reconciled from the compression bundle and critique-note>

## Disposition
**keep | delete | merge into `<target-path>`** — <for delete/merge: one-line rationale naming the source finding; for keep: "no note-level finding" suffices>

## Body edits
| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| ... | compression/branch-bloat | ... | remove/compress/split/keep | ... |
| ... | critique-note | ... | ... | ... |

## Routed attention (composition-friction-gate — not auto-resolved)
**Filter verdict:** SURVIVES | DISSOLVES
<if DISSOLVES: the contradiction, verbatim from the friction report>

**Thinnest joints:**
1. <joint, quoted> — <UNSUPPORTED|THIN|HOLDS> — <what it fails to establish>
...

## Gate findings

Repeat this subsection for every bundle that produced at least one applicable gate. Omit bundles with no applicable gates; record skipped bundles in Open items only when their absence is surprising for the note's type or traits.

### Semantic
| Gate | Result | Finding |
|---|---|---|
| ... | ... | ... |

### Prose
| Gate | Result | Finding |
|---|---|---|
| ... | ... | ... |

Add matching subsections for any other bundle with findings (`accessibility`, `complexity`, `frontmatter`, `sentence`, `structural`).

## Connection candidates
- <label> -> <target> — <reason, from connect report>

## Proposed revision shape
<short outline of the note after the body edits above>

## Open items
<branches or claims that need evidence before a rehoming or deletion decision can be made, plus any routed-attention item above that the editor judges worth acting on>

## Resolution

**Status:** <not-required for keep | pending for delete/merge>
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
```

Never omit "Routed attention" — even a clean SURVIVES with no thin joints below THIN is worth one line, since silently dropping the section would make the friction gate's absence indistinguishable from a clean result. Never omit "Disposition" either: an explicit `keep` distinguishes "considered and kept" from "never considered".

`kb/reports/full-pass/*`, `kb/reports/critique/*`, `kb/reports/friction/*`, and `kb/reports/connect/*` are gitignored inspection artifacts. Quote or restate enough of each source report's substance directly into the packet that it stands alone. Retain the pass directory while its packet or residual findings are still in use; delete it after those outputs have been consumed. An unactioned `delete`/`merge` Disposition counts as still in use, so retain its packet until someone accepts, rejects, or supersedes it.

## Do not

- Do not edit the note before step 8. Steps 1–7 produce a plan; step 8 applies it.
- Do not skip any catalog review bundle in step 5 or the closing cycle. Request all seven bundles every time; let the selector skip non-applicable gates, not the orchestrator.
- Do not hand back the raw reports as the deliverable. The reconciled packet is the point of steps 1–7.
- Do not resolve a compression-vs-catalog-bundle disagreement by dropping one finding; record both and let the packet's reader judge, since they test different properties.
- Do not convert `composition-friction-gate`'s filter verdict or thinnest-joints ranking into a remove/compress/keep action. Its hard rule against self-graded verdicts is why this instruction carries its findings unresolved instead of reconciling them like the others.
- Do not let the step 9 revise pass change claims, add material, or restore anything step 8 cut. If it does, that's a sign the packet's body edits left the note incoherent — fix the edit, not the prose around it.
- Do not start step 10 — including creating closing review jobs — while step 9 is still running or before its edits are on disk. Parallelizing copyedit with closing critique or catalog-bundle jobs pins review snapshots to the wrong text.
- Do not delete, merge, mark, or otherwise edit the note within the pass when its Disposition is `delete` or `merge`. The retained packet is the pass's entire output in that case; executing the disposition is the packet reader's call.
- Do not begin any packet-driven edit, deletion, merge, rejection, or alternative operation without a successful `commonplace-guard-full-pass-report` result over the complete guarded-input set.

---

Relevant Notes:

- [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — why running compression, critique-note, composition-friction-gate, the catalog bundles, and connect side by side catches more than repeating one check.
- [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md) — why step 7 reconciles complementary findings instead of voting one down.
- [Resolve a full-pass disposition](./resolve-full-pass-disposition.md) — applies-when: a retained delete or merge report needs inspection or resolution
