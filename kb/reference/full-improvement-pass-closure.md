---
description: "How the shipped full-improvement workflow reassays final note bytes, routes residual findings, and stops without claiming convergence"
type: types/note.md
tags: [evaluation, kb-maintenance, review-system]
---

# Full improvement pass closure

The full-improvement workflow evaluates a note, transforms it, and then runs a closing assay cycle against the final bytes. The closing cycle exists because the initial reports describe the pre-edit note: once the editor and the copyeditor change that note, the earlier evidence cannot by itself describe the result.

Closure here means that the workflow has reassessed its output and preserved any remaining findings. It does not mean every assay passes, every finding is fixed, or the note has converged to a fixed point.

## Shipped behavior

`commonplace-review run full-pass`, operated under the [full-improvement-pass instruction](../instructions/run-full-improvement-pass-on-note.md), has three phases:

1. Run the compression bundle, critique, composition friction, premise decomposition, every catalog gate bundle and connection discovery against the initial note, and reconcile their reports into one packet.
2. For a `keep` with a determined update, an editor applies the packet's body edits and a separate copyeditor fixes flow and coherence; code checks the text and keeps it in the run.
3. Run the same methods against the edited text, then choose a closing status: `ready` ends the pass and writes the final text to the note, `repair-needed` permits one repair and a new closing cycle, and `hand-back` ends the pass with the note at its start text. Each closing decision is appended to the packet.

Every method, including the catalog gates and critique, is asked over each text. When the pass ends, code writes review result files once, for the text the note then holds: the final text's closing verdicts after an applied edit, the initial verdicts otherwise.

The closing cycle starts at most one further edit-and-review round, and only for defects the pass introduced. A second `repair-needed` ends the pass like a `hand-back`, with the note untouched. This is a stopping rule: it prevents an unbounded loop in which one repair reopens a different concern while still leaving the final state inspected.

## Calibration evidence

The closing behavior was calibrated on five substantive full-improvement passes on 2026-07-11:

| Observation | Result |
|---|---:|
| Anchored carry judgments | 28 `would_rerun`, 0 `would_ack` |
| Semantic verdict changes after editing | 14 of 23 |
| Materially changed critiques after editing | 5 of 5 |
| Materially changed compression, friction, and connection reports | 15 of 15 |
| Same-byte verdict controls that changed | 1 of 5 |
| Same-byte critiques that materially changed | 0 of 5 |
| Passes ending with residual Open items | 5 of 5 |

These observations justify the closing cycle for this workflow's substantive edits. They do not estimate behavior for arbitrary small edits: the tested passes made multidimensional changes, every carry judgment favored rerunning, and rerun cost was not measured. The same-byte controls also show that a changed verdict is not automatically caused by the edit; reviewer variance is non-zero.

## Resulting system policy

- Keep a closing cycle in the full-improvement workflow, with at most one repair.
- Treat closing reports as evidence about the final note, not certification that it is complete or correct.
- Preserve residual findings as Open items instead of reopening transformation.
- Do not build carry-event commands, trust-dial automation, reduced audit sampling, or general edit-preservation heuristics from this calibration.
- Do not infer that every transforming workflow needs this exact assay set. The evidence is local to the shipped full-improvement pass.
- Human review attestation remains deferred. The closure calibration neither selected a representation nor gave an attestation any freshness or skip semantics.

The review system's distinction between freshness and endorsement remains intact: a current review says its evidence matches the current inputs. The closing-cycle rule adds a workflow-level obligation to obtain that current evidence after the workflow changes its target.

---

Relevant Notes:

- [Review system](./README-REVIEW-SYSTEM.md) — part-of: the snapshot-anchored assay and freshness system used by the closing semantic and critique runs
- [Run a full improvement pass on one note](../instructions/run-full-improvement-pass-on-note.md) — procedure: the operative transformation and one-cycle closure workflow
