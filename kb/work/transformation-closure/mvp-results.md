# MVP results: closure reruns paid; carrying did not reach its build gate

## Result

The MVP shipped and ran on five real full-improvement passes. It established a useful local result: after the substantive edits produced by this workflow, closing review is not redundant. It did **not** establish that carrying review evidence is worth building, nor did it locate the proposed general carry heuristics.

Part 4's instrumentation gate is therefore **no for now**. Do not build carry-event commands, ack integration, reduced audit sampling, or a trust dial from this evidence. Reopen that decision only after a workflow produces plausible `would_ack` cases and records enough cost data to show that avoiding reruns would matter.

## Evidence base

Five passes produced 53 observation events:

| Pass target | Semantic pairs | Semantic flips | Critique changed after edit | Same-byte verdict control | Same-byte critique control |
|---|---:|---:|---|---|---|
| `directory-placement-is-total-frontmatter-classification-is-partial.md` | 5 | 4 | yes | flipped | materially stable |
| `a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` | 5 | 2 | yes | stable | materially stable |
| `a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md` | 5 | 4 | yes | stable | materially stable |
| transformation-closure `README.md` | 3 | 3 | yes | stable | materially stable |
| `claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md` | 5 | 1 | yes | stable | materially stable |

Aggregate:

- 28 anchored counterfactual decisions: **28 `would_rerun`, 0 `would_ack`**.
- Semantic verdicts flipped on 14 of 23 edited-note reruns.
- Critique materially diverged on 5 of 5 edited-note reruns.
- Compression, friction, and connect materially diverged on all 15 initial-to-closing comparisons.
- Same-byte controls: 1 verdict flip in 5 runs; 0 materially divergent critiques in 5 runs.
- Every pass ended with residual Open items; the one-cycle rule terminated the workflow by routing them rather than claiming the artifact had no remaining problems.

The full test suite passes after the MVP implementation: 377 passed, 1 skipped on 2026-07-11.

## What the observations support

### Closing review is warranted after this workflow's substantive edits

All five editors judged every anchored pair unsafe to carry. The reruns often changed the result, far above the small same-byte control sample: 14/23 semantic flips after edits versus 1/5 under identical inputs, and 5/5 materially changed critiques after edits versus 0/5 under identical inputs. These passes were selected for substantive improvement, so this is a workflow-local result, not a general estimate over arbitrary edits.

The closing cycle also caught useful residuals after the edits: unsupported universality, grounding that still exceeded evidence, new weakest inferential joints, and new connection candidates. Step 10 earns its place for the full-improvement workflow.

### One closing cycle is a stopping rule, not convergence

Every pass retained residual findings. The protocol still terminated cleanly because it routes those findings to Open items instead of reopening transformation. The observed semantics are therefore: *re-assay the final bytes once, preserve residual evidence, and stop*. “Closure” does not mean that all assays pass or that the note has converged to a fixed point.

### Version anchoring helped open-ended critique, but its license remains empirical

Critique changed materially after every edited note, so anchoring it to exact bytes was useful. But all five same-byte critique controls were materially stable at the operational threshold (“would this have changed steps 8–9?”). That contradicts the categorical planning claim that an open-ended report has no replacement value on unchanged bytes.

The conservative shipped license may remain evidence-currency-only while evidence is sparse, but it is a policy choice, not a located semantic necessity. Question shape alone does not determine skip value; repeated-run material stability, cost, and downstream use also matter.

### Reviewer variance is non-zero

One of five same-byte verdict controls flipped. The sample is small, but it validates the control arm's premise: an edited-note flip is not automatically an edit-caused failure. The observations support retaining identical-input controls in any future calibration experiment.

## What the observations do not support

| Candidate | Status after five passes | Why |
|---|---|---|
| Edit direction predicts preservation better than size | unidentified | Edits were substantive, multidimensional, and labeled after the fact; diff size and matched directional contrasts were not recorded. |
| Preservation is not compositional | untested | No pass carried a sequence of individually accepted edits; every judgment was `would_rerun`. |
| Ex-ante transformation footprints beat ex-post classification | untested | The record contains only the cumulative step-5-to-final diff, not a separately anchored step-8-to-step-9 copyedit diff. |
| Convergence needs structure, not judgment | locally supported only as a stopping policy | Residuals occurred in every pass, but no unstructured rerun-and-fix loop was run for comparison. |
| Current critique is mistaken for “handled” | untested | The workflow consumed critique deliberately; it did not instrument a downstream reader or define misuse behavior. |
| Real carrying would pay | unsupported | There were no `would_ack` cases and no usable rerun-cost measurement. |

These are not negative findings about the candidate mechanisms. They are limits of the probe. Do not promote or discharge them from this dataset.

## Implementation findings that did survive

Two distinctions were located by building against shipped state rather than by the five-pass comparison:

- **Completion is not decision.** A report-kind pair completes without a verdict; persisted `result_kind` and per-kind completion rules are required.
- **Current state is not process history.** Acceptance owns the current freshness baseline; counterfactual carry rationale and comparisons belong in a separate history surface.

Both are now represented in the review implementation and reference documentation. They need no additional theory note unless a later case shows transfer beyond review storage.

## Next decision

The closure MVP needs no more carry-calibration runs of the same shape: substantive full passes will predictably produce `would_rerun` and cannot exercise the carry gate. Meaningful next work must change the probe, not add volume:

1. If carrying remains interesting, target deliberately small or constrained edits and record a separate pre/post copyedit snapshot, rerun cost, preregistered rival explanations, and independent materiality judgment.
2. If trajectory-aware evaluation remains interesting, run the proposed trajectory-versus-final-output comparison on retained pass histories; the earlier trace audit was suggestive but had no blinded control.
3. Keep the human-attestation probe independent. Nothing in these passes selects its representation or licenses building it.

Until one of those probes is deliberately chosen, the correct operational state is: keep step 10, keep critique anchored, keep other methods as direct reruns, and build no carry machinery.
