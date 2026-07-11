---
description: Run the full improvement pipeline over one note, apply its editorial packet, then close review over the resulting text with one assay cycle.
type: kb/types/instruction.md
---

# Run a full improvement pass on one note

Sequence five validated methods — the compression bundle, `critique-note`, `composition-friction-gate`, the production `semantic` review bundle, and `cp-skill-connect` — into one ordered pass over a single note, reconcile their output into one editorial packet, apply it, run a flow/coherence copyedit, and close review over the final text with one assay cycle. This instruction does not replace the individual methods; it orders them, settles the disagreements between them, and carries the result through to an edited and re-assayed note. Method fit varies by note shape — treat a note whose shape surprises you with extra scrutiny; the per-method rationale below (see "Why this order") states what each validation run actually found.

`composition-friction-gate` sits oddly here: its own hard rule is that it must never resolve to a verdict, because its output is meant for a human to judge, not to be graded by the same kind of agent that wrote or would edit the note. Running it inside an agent-driven synthesis step is in tension with that design — see the reconciliation rule below for how this instruction tries to avoid re-creating the false-confidence failure the gate exists to prevent. Five validation runs found real signal from this step every time, twice independently corroborating `critique-note` on the same sentence — but none has yet produced a genuine same-passage conflict between two methods; judge one on its own terms if it comes up.

Inputs:

- first and only argument: `{note-path}` — repository-relative note path.

Derive `<note-name>` from `{note-path}` as the filename without its extension (`kb/notes/linking-theory.md` → `linking-theory`). At the start of every invocation mint a unique `<pass-id>` (a UTC timestamp plus a short random suffix is sufficient). Retain reports under `kb/reports/full-pass/<note-name>/<pass-id>/{initial,closing,controls}/`; never reuse a pass ID or overwrite an initial report.

Steps 1 through 7 below only write reports; none of them edit the note. Steps 8 and 9 do — applying the packet and then a final flow pass. Step 10 closes review over those edits without starting another transformation round.

## Execution roles and isolation

The parent agent running this instruction is the **orchestrator**. It alone creates jobs, dispatches workers, schedules around the harness concurrency limit, finalizes review output, copies retained artifacts, edits the note, and writes the observation record. A dispatched worker performs the one review or copyedit task it receives; it does not recursively start another sub-agent merely because the invoked method requires a fresh reviewer. After verifying the worker-owned output, the orchestrator closes, terminates, or releases that worker with the harness lifecycle operation before scheduling more work. Every worker in this pass is single-use.

Here, **fresh sub-agent** means a newly isolated execution context that has not participated in an earlier method or edit in this pass. A follow-up turn to an earlier worker is not fresh. When capacity is exhausted, queue work until a slot opens rather than nesting delegation or reusing a worker. Step 9 has the strictest isolation: its worker must be new to the pass and receive only the current note text and the exact copyedit prompt.

## Why this order

- **Compression bundle first.** Across early validation cases, the compression bundle (`kb/instructions/compression-bundle/README.md`, run via `run-compression-bundle-on-note.md`) matched or exceeded earlier standalone prune and split/rehome instruction drafts and additionally covers core-claim-obscured and detail-overhang. It is the most reliable single source of edit-strategy signal (compress, fold, delete, rehome), and runs outside the review DB — no acceptance state written.
- **`critique-note` second.** This anchored, open-ended, report-kind assay targets whether the retained central commitment is actually defensible, not whether the supporting material earns its space. It writes a freshness baseline and completes with `REPORT`, not a decision. Case 01 showed it flags overclaiming the compression criteria do not test for, because compression assumes the material is already true and asks only whether it earns its place.
- **`composition-friction-gate` third.** A third orthogonal axis again: not context cost, not defensibility against an opponent, but whether the claim survives concretization at all and which inferential joints are least supported. Like `critique-note` it runs adversarially in a fresh sub-agent, so it sits next to it in the sequence. Unlike every other step here, it must not resolve to PASS/WARN or remove/compress/keep — see "Reconciling disagreement" for how its output is carried into the packet without collapsing that rule.
- **Production `semantic` bundle, always fourth.** These closed-ended, verdict-kind assays check truth, consistency, grounding, and load-bearing qualifiers — a fourth axis orthogonal to the three above. Case 02 showed the two can diverge sharply: `semantic/load-bearing-qualifiers` positively defended a section that the marginal-value-redundancy criterion correctly flagged, because the semantic gate asks whether qualifiers are necessary for truth, not whether a paragraph adds marginal value beyond what the argument already made. Like critique, this step writes a freshness baseline; unlike critique, each pair completes with a decision. It always runs rather than being left to a mid-pass judgment about whether the note looks like a promotion candidate.
- **`cp-skill-connect` last of the report-only steps.** Connect summarizes the note's current claim, mechanism, and tensions to prospect for links; running it last means the synthesis packet's connection candidates reflect the same reading of the note that produced the earlier findings, instead of being a disconnected report gathered at a different point in the reasoning.
- **Flow/coherence pass after body edits, not before.** Compressing, deleting, and rehoming material breaks transitions the original prose relied on. Running a readability pass before those edits land would polish sentences this instruction is about to cut; it belongs after the substantive content is settled.
- **Why several orthogonal checks at all, and why synthesis over voting.** Each of compression, critique-note, composition-friction-gate, semantic, and connect tests a different, structurally independent property, so their failures don't correlate the way repeated passes of the same check would. Step 7 reconciles by keeping complementary findings rather than voting one down — these methods answer different sub-problems, not the same question twice, so disagreement between them is signal to preserve, not noise to resolve by majority.

## Procedure

1. Mint `<pass-id>`, create its `initial/`, `closing/`, and `controls/` directories, record the initial note SHA-256, then read the target note fully.
2. Run the compression bundle per `run-compression-bundle-on-note.md` (`kb/instructions/run-compression-bundle-on-note.md`), passing `kb/reports/full-pass/<note-name>/<pass-id>/initial/compression-bundle-review.md` as its `{output-path}` argument. No DB writes.
3. Run `critique-note` through the requested-mode review pipeline in a fresh sub-agent:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} critique --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Delegate and finalize as in `run-review-batches.md`, then immediately copy the finalized pair result to `kb/reports/full-pass/<note-name>/<pass-id>/initial/critique.md`. Do this before any later finalization can prune its job artifacts.
4. Run `composition-friction-gate` (`kb/instructions/composition-friction-gate.md`) in a fresh sub-agent against the same note. Copy its report to `kb/reports/full-pass/<note-name>/<pass-id>/initial/friction.md`. It will not, and must not, emit a PASS/WARN/FAIL verdict — only a filter result (SURVIVES/DISSOLVES) and a ranked list of the thinnest inferential joints.
5. Run the production `semantic` bundle through the requested-mode, single-note flow in `kb/instructions/run-review-batches.md`:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} semantic --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Then delegate, finalize, and verify exactly as that instruction describes.
   Immediately copy every finalized semantic pair result to `kb/reports/full-pass/<note-name>/<pass-id>/initial/semantic/`, preserving one file per gate.
6. Run `cp-skill-connect` against the note and immediately copy its canonical report to `kb/reports/full-pass/<note-name>/<pass-id>/initial/connect.md`. The closing connect run writes the same canonical report path and will overwrite it; the pass-scoped copy is the retained initial evidence.
7. Synthesize the retained reports (below) into one packet at `kb/reports/full-pass/<note-name>/<pass-id>/full-pass-report.md`. This is the only step among 1–7 that reconciles disagreement; do not just concatenate the reports.
8. Apply the packet's body edits directly to the note. If `composition-friction-gate` ran, reread its report's "For the human" line against the edited text before moving on. This is not a re-run of the gate — just a check that the one thing it pointed to is still accurate, or has actually been addressed, now that the edit has changed the prose around it. If it looks wrong given the edit, note that in the packet's Open items rather than silently re-editing.
9. Run a final revise pass over the edited note with exactly this prompt: `revise the note for flow, coherence, logic and readability`. Give a newly isolated sub-agent that performed no earlier work in this pass (or yourself, if editing directly) only the current note text and that prompt — not the packet or the underlying reports. Do not use a follow-up turn to a reviewer from steps 2–6. This step is a copyedit pass, not a second chance to re-open the content decisions steps 1–8 already made; it should not reintroduce material step 8 removed or add new claims.
10. Run one closing cycle over all five methods, as specified in "Closing cycle" below. Append its summary to `full-pass-report.md`; route residual findings to Open items and stop after this one cycle.

## Closing cycle

Record the final note SHA-256 before any closing run. Retain every closing report under `closing/` and leave `initial/` byte-identical.

For each anchored semantic pair and critique, first run the stale selector with `--json` and inspect its cumulative accepted-snapshot-to-final-text `diff`:

```bash
commonplace-review-target-selector --model-partition {model-partition} {assay} --note {note-path} --json
```

Before rerunning, record `would_ack` or `would_rerun`, a rationale, and rough free-text edit kinds. Then rerun regardless: this MVP uses 100% counterfactual sampling and performs no real ack. Run each semantic gate as its own job:

```bash
commonplace-review-target-selector --mode requested --model-partition {model-partition} {semantic-gate} --note {note-path} --json \
  | commonplace-create-review-jobs --input - --grouping gate --batch-size 1
```

Rerun critique through the step-3 flow. Immediately copy finalized results into `closing/semantic/<gate>.md` and `closing/critique.md`. For verdict pairs record whether the verdict flipped; for critique record whether the new report materially diverged enough that it would have changed steps 8–9. A carried report would only be reused evidence: it endorses nothing and has no skip semantics.

Rerun the compression bundle, composition-friction-gate, and connect directly against the final text. Retain them under `closing/`, compare initial to closing (compression at bundle level with per-gate detail nested), and record divergence. Copy connect's canonical report into `closing/connect.md` immediately after the skill returns; this closing run overwrites the canonical report used in step 6 but never the retained `initial/connect.md`. The friction report's "For the human" line is never satisfied by a carry judgment.

Write the observation record directly; the MVP has no owning event command. Append one JSON object per event to `kb/work/transformation-closure/observations/<pass-id>.jsonl`, at this granularity:

- one `carry_audit` for each anchored pair — critique and every selected semantic gate each get their own line;
- one `closing_comparison` for each unanchored method family — compression bundle, composition-friction-gate, and connect;
- one `control_comparison` for each control run.

Every new line uses `schema_version: 2` and has `record_kind`, `pass_id`, `note_path`, `assay_id`, `initial_note_sha256`, `final_note_sha256`, and `adjudicator`. `adjudicator` records the agent that made the counterfactual or comparison judgment. Every report reference records the execution provenance of the run that produced that report; a single event-level runner cannot represent two independent executions. Existing schema-less observation files are legacy v1 evidence; do not rewrite them after the fact.

Use an execution object of `{"runner":"...","model":null,"effort":null}`. Record a concrete value only when the harness or worker explicitly supplied it; use JSON `null` when unavailable, never the string `"unknown"`. A report reference is `{"path":"...","sha256":"...","execution":{...}}`.

The record-kind fields are:

- `carry_audit`: `judgment` (`would_ack` or `would_rerun`), `rationale`, `edit_kinds`, `initial_report`, `closing_report`, and either `flip` (verdict) or `material_divergence` (report).
- `closing_comparison`: `initial_report`, `closing_report`, and the applicable divergence outcome; there is no carry judgment.
- `control_comparison`: `source_report`, `control_report`, `gate_snapshot_sha256`, `source_prompt_sha256`, `control_prompt_sha256`, and either `flip` or `material_divergence`.

Use these shapes literally; `edit_kinds` is an array of free-text strings:

```json
{"schema_version":2,"record_kind":"carry_audit","pass_id":"...","note_path":"...","assay_id":"...","initial_note_sha256":"...","final_note_sha256":"...","adjudicator":{"runner":"codex","model":null,"effort":null},"judgment":"would_ack","rationale":"...","edit_kinds":["flow-only"],"initial_report":{"path":"...","sha256":"...","execution":{"runner":"codex-subagent","model":null,"effort":null}},"closing_report":{"path":"...","sha256":"...","execution":{"runner":"codex-subagent","model":null,"effort":null}},"flip":false}
{"schema_version":2,"record_kind":"closing_comparison","pass_id":"...","note_path":"...","assay_id":"...","initial_note_sha256":"...","final_note_sha256":"...","adjudicator":{"runner":"codex","model":null,"effort":null},"initial_report":{"path":"...","sha256":"...","execution":{"runner":"codex-subagent","model":null,"effort":null}},"closing_report":{"path":"...","sha256":"...","execution":{"runner":"codex-subagent","model":null,"effort":null}},"material_divergence":false}
{"schema_version":2,"record_kind":"control_comparison","pass_id":"...","note_path":"...","assay_id":"...","initial_note_sha256":"...","final_note_sha256":"...","adjudicator":{"runner":"codex","model":null,"effort":null},"source_report":{"path":"...-source-output.md","sha256":"...","execution":{"runner":"codex-subagent","model":null,"effort":null}},"control_report":{"path":"...-control-output.md","sha256":"...","execution":{"runner":"codex-subagent","model":null,"effort":null}},"gate_snapshot_sha256":"...","source_prompt_sha256":"...","control_prompt_sha256":"...","flip":false}
```

Manually run two controls in fresh sub-agents: critique and one verdict gate, rotating the verdict gate across `semantic/internal-consistency`, `semantic/load-bearing-qualifiers`, `semantic/explanatory-reach`, and `semantic/explication-quality`. For each control:

1. Copy the closing single-pair job's `prompt.md` and raw sentinel-bracketed `bundle-output.md` into `controls/` as `<assay>-source-prompt.md` and `<assay>-source-output.md`. These retained copies are the control's source artifacts.
2. Duplicate `<assay>-source-prompt.md` as `<assay>-control-prompt.md`, changing only its output destination to `<assay>-control-output.md`.
3. Run the control prompt in a newly isolated sub-agent. Do not finalize it.
4. Compare the two raw sentinel-bracketed outputs. Record the retained source output as `source_report` and the control output as `control_report`; do not compare a finalized pair result with a raw control bundle.
5. Read `gate_snapshot_sha256` from the completed source pair's reviewed gate snapshot, not from the live criterion file. Given its `review_pair_id`, query the active review DB:

   ```bash
   sqlite3 "${COMMONPLACE_REVIEW_DB:-kb/reports/review-store.sqlite}" "SELECT s.content_sha256 FROM review_pairs p JOIN review_file_snapshots s ON s.snapshot_id = p.reviewed_gate_snapshot_id WHERE p.review_pair_id = <source-review-pair-id>;"
   ```

6. Hash both retained prompts and outputs, record the `control_comparison`, and verify that the original source job output hash and review DB state remain unchanged.

Append this section to the packet:

```markdown
## Closing cycle
**Pass ID:** <pass-id>

| Assay | Counterfactual judgment | Closing outcome |
|---|---|---|
| ... | would_ack/would_rerun/not applicable | flip/material divergence/unchanged |
```

## Reconciling disagreement

- Default to the compression bundle's bias (compress, fold, delete, or rehome) when it and `critique-note` disagree about a passage. `critique-note`'s natural repair path tends to add qualification; only keep an addition it proposes when the addition is what makes the central claim defensible against the strongest attack, not merely a hedge against a possible objection. Before calling a finding a hedge, state what the note's claim would need to look like if the objection were fully valid — if that changes the claim's scope, completeness, or a load-bearing precondition, it is not a hedge, no matter how easy the label is to reach for.
- If the semantic bundle warns on a section the compression bundle passed (or vice versa), keep both findings in the packet rather than picking a winner — they test different properties (truth/grounding vs. context cost) and a note can fail one without failing the other.
- Treat connect's candidates as additive: they extend the note's outbound links and do not bear on whether body content should be cut, so list them separately from the body-edit recommendations.
- **Carry `composition-friction-gate`'s findings unresolved.** Do not convert its filter verdict or its ranked joints into a remove/compress/keep action the way the other methods' findings are converted. Put them in the packet's dedicated "Routed attention" section verbatim, out of scope for step 8's automatic application — the same status as the "Open items" section, not a body edit. This is the one deliberate exception to "reconcile, don't concatenate" — reconciling this gate's output the way the others are reconciled would recreate the self-graded verdict its own hard rule forbids. If a thin joint turns out, on the editor's judgment, to need a real fix, that judgment call belongs to whoever reads the packet, not to this instruction.

## Output Contract

```markdown
# Full Improvement Pass: <note title>

**Target:** `<note-path>`
**Reports used:** compression bundle, critique-note, composition-friction-gate, semantic bundle, connect

## Strongest retained claim
<one sentence, reconciled from the compression bundle and critique-note>

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

## Truth/grounding findings
| Gate | Result | Finding |
|---|---|---|
| ... | ... | ... |

## Connection candidates
- <label> -> <target> — <reason, from connect report>

## Proposed revision shape
<short outline of the note after the body edits above>

## Open items
<branches or claims that need evidence before a rehoming or deletion decision can be made, plus any routed-attention item above that the editor judges worth acting on>
```

Never omit "Routed attention" — even a clean SURVIVES with no thin joints below THIN is worth one line, since silently dropping the section would make the friction gate's absence indistinguishable from a clean result.

`kb/reports/full-pass/*`, `kb/reports/critique/*`, `kb/reports/friction/*`, and `kb/reports/connect/*` are gitignored, but reports used by this experiment are retained through workshop closure: a hash verifies bytes but does not preserve them. The observation JSONL is committed workshop evidence because judgments are not regenerable. Quote or restate enough of each source report's substance directly into the packet that it stands alone.

## Do not

- Do not edit the note before step 8. Steps 1–7 produce a plan; step 8 applies it.
- Do not skip the production semantic bundle (step 5). It always runs — do not substitute your own judgment about whether the note's apparent maturity makes it a promotion candidate.
- Do not hand back the raw reports as the deliverable. The reconciled packet is the point of steps 1–7.
- Do not resolve a compression-vs-semantic disagreement by dropping one finding; record both and let the packet's reader judge, since they test different properties.
- Do not convert `composition-friction-gate`'s filter verdict or thinnest-joints ranking into a remove/compress/keep action. Its hard rule against self-graded verdicts is why this instruction carries its findings unresolved instead of reconciling them like the others.
- Do not let the step 9 revise pass change claims, add material, or restore anything step 8 cut. If it does, that's a sign the packet's body edits left the note incoherent — fix the edit, not the prose around it.

---

Relevant Notes:

- [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — why running compression, critique-note, composition-friction-gate, semantic, and connect side by side catches more than repeating one check.
- [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md) — why step 7 reconciles complementary findings instead of voting one down.
