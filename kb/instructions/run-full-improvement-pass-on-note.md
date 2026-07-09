---
description: Run the full validated improvement pipeline over one note (compression, critique, friction gate, semantic review, connect), reconcile into an editorial packet, apply it, and copyedit for flow.
type: kb/types/instruction.md
---

# Run a full improvement pass on one note

Sequence five validated methods — the compression bundle, `critique-note`, `composition-friction-gate`, the production `semantic` review bundle, and `cp-skill-connect` — into one ordered pass over a single note, reconcile their output into one editorial packet, apply it, and close with a flow/coherence copyedit pass. This instruction does not replace the individual methods; it orders them, settles the disagreements between them, and carries the result through to an edited note. Method fit varies by note shape — treat a note whose shape surprises you with extra scrutiny; the per-method rationale below (see "Why this order") states what each validation run actually found.

`composition-friction-gate` sits oddly here: its own hard rule is that it must never resolve to a verdict, because its output is meant for a human to judge, not to be graded by the same kind of agent that wrote or would edit the note. Running it inside an agent-driven synthesis step is in tension with that design — see the reconciliation rule below for how this instruction tries to avoid re-creating the false-confidence failure the gate exists to prevent. Five validation runs found real signal from this step every time, twice independently corroborating `critique-note` on the same sentence — but none has yet produced a genuine same-passage conflict between two methods; judge one on its own terms if it comes up.

Inputs:

- first and only argument: `{note-path}` — repository-relative note path.

Derive `<note-name>` from `{note-path}` as the filename without its extension (`kb/notes/linking-theory.md` → `linking-theory`). Every report and the synthesis packet this pass produces goes under `kb/reports/full-pass/<note-name>/` — see the per-step paths below and the Output Contract.

Steps 1 through 7 below only write reports; none of them edit the note. Steps 8 and 9 do — applying the packet and then a final flow pass.

## Why this order

- **Compression bundle first.** Across early validation cases, the compression bundle (`kb/instructions/compression-bundle/README.md`, run via `run-compression-bundle-on-note.md`) matched or exceeded earlier standalone prune and split/rehome instruction drafts and additionally covers core-claim-obscured and detail-overhang. It is the most reliable single source of edit-strategy signal (compress, fold, delete, rehome), and runs outside the review DB — no acceptance state written.
- **`critique-note` second.** It targets a different failure mode: whether the retained central commitment is actually defensible, not whether the supporting material earns its space. Case 01 showed it flags overclaiming the compression gates don't test for, because compression assumes the material is already true and asks only whether it earns its place.
- **`composition-friction-gate` third.** A third orthogonal axis again: not context cost, not defensibility against an opponent, but whether the claim survives concretization at all and which inferential joints are least supported. Like `critique-note` it runs adversarially in a fresh sub-agent, so it sits next to it in the sequence. Unlike every other step here, it must not resolve to PASS/WARN or remove/compress/keep — see "Reconciling disagreement" for how its output is carried into the packet without collapsing that rule.
- **Production `semantic` bundle, always fourth.** Checks truth, consistency, grounding, and load-bearing qualifiers — a fourth axis orthogonal to the three above. Case 02 showed the two can diverge sharply: `semantic/load-bearing-qualifiers` positively defended a section that the marginal-value-redundancy gate correctly flagged, because the semantic gate asks whether qualifiers are necessary for truth, not whether a paragraph adds marginal value beyond what the argument already made. This step writes durable review-DB acceptance state, unlike every other step here, which is why it always runs rather than being left to a mid-pass judgment about whether the note looks like a promotion candidate.
- **`cp-skill-connect` last of the report-only steps.** Connect summarizes the note's current claim, mechanism, and tensions to prospect for links; running it last means the synthesis packet's connection candidates reflect the same reading of the note that produced the earlier findings, instead of being a disconnected report gathered at a different point in the reasoning.
- **Flow/coherence pass after body edits, not before.** Compressing, deleting, and rehoming material breaks transitions the original prose relied on. Running a readability pass before those edits land would polish sentences this instruction is about to cut; it belongs after the substantive content is settled.
- **Why several orthogonal checks at all, and why synthesis over voting.** Each of compression, critique-note, composition-friction-gate, semantic, and connect tests a different, structurally independent property, so their failures don't correlate the way repeated passes of the same check would. Step 7 reconciles by keeping complementary findings rather than voting one down — these methods answer different sub-problems, not the same question twice, so disagreement between them is signal to preserve, not noise to resolve by majority.

## Procedure

1. Read the target note fully.
2. Run the compression bundle per `run-compression-bundle-on-note.md` (`kb/instructions/run-compression-bundle-on-note.md`), passing `kb/reports/full-pass/<note-name>/compression-bundle-review.md` as its `{output-path}` argument. No DB writes.
3. Run `critique-note` (`kb/instructions/critique-note.md`) in a fresh sub-agent against the same note. It writes to `kb/reports/critique/<note-name>.critique.md`.
4. Run `composition-friction-gate` (`kb/instructions/composition-friction-gate.md`) in a fresh sub-agent against the same note. It writes to `kb/reports/friction/<note-name>.friction.md`. It will not, and must not, emit a PASS/WARN/FAIL verdict — only a filter result (SURVIVES/DISSOLVES) and a ranked list of the thinnest inferential joints.
5. Run the production `semantic` bundle through the requested-mode, single-note flow in `kb/instructions/run-review-batches.md`:

   ```bash
   commonplace-review-target-selector --mode requested --model-partition {model-partition} semantic --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Then delegate, finalize, and verify exactly as that instruction describes.
6. Run `cp-skill-connect` against the note. It writes a report to `kb/reports/connect/<collection>/<note-name>.connect.md` and touches nothing else.
7. Synthesize the reports (below) into one packet at `kb/reports/full-pass/<note-name>/full-pass-report.md`. This is the only step among 1–7 that reconciles disagreement; do not just concatenate the reports.
8. Apply the packet's body edits directly to the note. If `composition-friction-gate` ran, reread its report's "For the human" line against the edited text before moving on. This is not a re-run of the gate — just a check that the one thing it pointed to is still accurate, or has actually been addressed, now that the edit has changed the prose around it. If it looks wrong given the edit, note that in the packet's Open items rather than silently re-editing.
9. Run a final revise pass over the edited note with exactly this prompt: `revise the note for flow, coherence, logic and readability`. Give the sub-agent (or yourself, if editing directly) only the current note text and that prompt — not the packet or the underlying reports. This step is a copyedit pass, not a second chance to re-open the content decisions steps 1–8 already made; it should not reintroduce material step 8 removed or add new claims.

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

`kb/reports/full-pass/*`, `kb/reports/critique/*`, `kb/reports/friction/*`, and `kb/reports/connect/*` are gitignored — regenerable working artifacts, not durable state. The note itself, edited in steps 8–9, is the only durable output of this pass. Quote or restate enough of each source report's substance directly into the packet at step 7 that the packet stands alone for steps 8–9, even though the packet does not persist afterward.

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
