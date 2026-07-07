# Run a full improvement pass on one note

Sequence every method this workshop has validated so far — the compression bundle, `critique-note`, the production `semantic` review bundle, and `cp-skill-connect` — into one ordered pass over a single note, reconcile their output into one editorial packet, apply it, and close with a flow/coherence copyedit pass. This instruction does not replace the individual methods; it orders them, settles the disagreements between them, and carries the result through to an edited note. Read the case comparisons in `case-01-llm-generation-relaxes-goals/README.md`, `case-02-prose-dereference/README.md`, and `case-03-adversarial-loop-writing-filter/README.md` before trusting a method's output on a note whose shape surprises you — fit varies by note.

Inputs:

- first argument: `{note-path}` — repository-relative note path.
- optional second argument: `{output-path}` — repository-relative Markdown path for the synthesis packet. If omitted, choose a workshop-local path near the relevant experiment case, or `kb/work/agent-note-improvement/<note-name>-full-pass.md` if this note is not already part of a case.

Steps 1 through 6 below only write reports; none of them edit the note. Steps 7 and 8 do — applying the packet and then a final flow pass.

## Why this order

- **Compression bundle first.** Across all three cases, the compression bundle (`compression/README.md`, run via `run-compression-bundle-on-note.md`) matched or exceeded the standalone `instruction-prune-weak-expansions.md` and `instruction-split-rehome-critique.md` findings and additionally covers core-claim-obscured and detail-overhang. It is the most reliable single source of edit-strategy signal (compress, fold, delete, rehome) and is workshop-local — no DB writes.
- **`critique-note` second.** It targets a different failure mode: whether the retained central commitment is actually defensible, not whether the supporting material earns its space. Case 01 showed it flags overclaiming the compression gates don't test for, because compression assumes the material is already true and asks only whether it earns its place.
- **Production `semantic` bundle, optional.** Checks truth, consistency, grounding, and load-bearing qualifiers — a third axis orthogonal to both of the above. Case 02 showed the two can diverge sharply: `semantic/load-bearing-qualifiers` positively defended a section that the marginal-value-redundancy gate correctly flagged, because the semantic gate asks whether qualifiers are necessary for truth, not whether a paragraph adds marginal value beyond what the argument already made. Run this step only when the note is a real promotion candidate — it writes durable review-DB acceptance state, unlike every other step here.
- **`cp-skill-connect` last of the report-only steps.** Connect summarizes the note's current claim, mechanism, and tensions to prospect for links; running it last means the synthesis packet's connection candidates reflect the same reading of the note that produced the compression and critique findings, instead of being a disconnected fifth report gathered at a different point in the reasoning.
- **Flow/coherence pass after body edits, not before.** Compressing, deleting, and rehoming material breaks transitions the original prose relied on. Running a readability pass before those edits land would polish sentences this instruction is about to cut; it belongs after the substantive content is settled.

## Procedure

1. Read the target note fully.
2. Run the compression bundle per `run-compression-bundle-on-note.md`. Workshop-local, no DB. Save its report near the note or case as that instruction directs.
3. Run `critique-note` (`kb/instructions/critique-note.md`) in a fresh sub-agent against the same note. It writes to `kb/reports/critique/<note-name>.critique.md`.
4. **Optional, promotion-candidate notes only.** Run the production `semantic` bundle through the requested-mode, single-note flow in `kb/instructions/run-review-batches.md`:

   ```bash
   commonplace-review-target-selector --mode requested --model {model-partition} semantic --note {note-path} --json \
     | commonplace-create-review-jobs --input - --grouping note
   ```

   Then delegate, finalize, and verify exactly as that instruction describes. Skip this step for an exploratory or draft pass — it mutates the shared review database, unlike the other three steps.
5. Run `cp-skill-connect` against the note. It writes a report to `kb/reports/connect/<collection>/<note-name>.connect.md` and touches nothing else.
6. Synthesize the reports (below) into one packet at `{output-path}`. This is the only step among 1–6 that reconciles disagreement; do not just concatenate the four reports.
7. Apply the packet's body edits directly to the note.
8. Run a final revise pass over the edited note with exactly this prompt: `revise the note for flow, coherence, logic and readability`. Give the sub-agent (or yourself, if editing directly) only the current note text and that prompt — not the packet or the underlying reports. This step is a copyedit pass, not a second chance to re-open the content decisions steps 1–7 already made; it should not reintroduce material step 7 removed or add new claims.

## Reconciling disagreement

- Default to the compression bundle's bias (compress, fold, delete, or rehome) when it and `critique-note` disagree about a passage. `critique-note`'s natural repair path tends to add qualification; only keep an addition it proposes when the addition is what makes the central claim defensible against the strongest attack, not merely a hedge against a possible objection.
- If the semantic bundle warns on a section the compression bundle passed (or vice versa), keep both findings in the packet rather than picking a winner — they test different properties (truth/grounding vs. context cost) and a note can fail one without failing the other.
- Treat connect's candidates as additive: they extend the note's outbound links and do not bear on whether body content should be cut, so list them separately from the body-edit recommendations.

## Output Contract

```markdown
# Full Improvement Pass: <note title>

**Target:** `<note-path>`
**Reports used:** compression bundle, critique-note[, semantic bundle], connect

## Strongest retained claim
<one sentence, reconciled from the compression bundle and critique-note>

## Body edits
| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| ... | compression/branch-bloat | ... | remove/compress/split/keep | ... |
| ... | critique-note | ... | ... | ... |

## Truth/grounding findings (if semantic bundle ran)
| Gate | Result | Finding |
|---|---|---|
| ... | ... | ... |

## Connection candidates
- <label> -> <target> — <reason, from connect report>

## Proposed revision shape
<short outline of the note after the body edits above>

## Open items
<branches or claims that need evidence before a rehoming or deletion decision can be made>
```

Omit the "Truth/grounding findings" section entirely when step 4 was skipped — do not write "not run" rows.

## Do not

- Do not edit the note before step 7. Steps 1–6 produce a plan; step 7 applies it.
- Do not run the production semantic bundle for a routine or exploratory pass — reserve it for notes actually being considered for promotion or re-acceptance.
- Do not hand back the four raw reports as the deliverable. The reconciled packet is the point of steps 1–6.
- Do not resolve a compression-vs-semantic disagreement by dropping one finding; record both and let the packet's reader judge, since they test different properties.
- Do not let the step 8 revise pass change claims, add material, or restore anything step 7 cut. If it does, that's a sign the packet's body edits left the note incoherent — fix the edit, not the prose around it.
