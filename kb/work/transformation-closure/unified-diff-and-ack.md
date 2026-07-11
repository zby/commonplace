# Unified diff and ack: one freshness surface for all checks

The minimal unification the MVP commits to: every check in the full pass — verdict-bearing (semantic gates) or not (compression bundle, critique-note, composition-friction-gate, connect) — gets the same version-anchored diff-and-ack treatment the review DB already gives gate reviews. An acceptance row pins the exact note and check text the evidence was computed against; the selector classifies fresh / note-changed / gate-changed by snapshot comparison; a stale record is either re-run or acked against the current bytes.

This is a build decision in the working-stance sense — the lightest representation that lets the MVP run — not a closed architecture question. What it deliberately does *not* decide: footprint machinery, edit-kind taxonomies in the system, trust-dial automation.

## Why the unification is nearly free

The staleness layer is already verdict-agnostic. Freshness classification compares snapshot hashes only (`src/commonplace/review/review-schema.sql`, selector query pattern at the bottom of the file); the decision column is consulted in exactly two consumer-side places — the `current_gate_acceptances` view's `rp.decision IS NOT NULL` filter and the warn-selector's fix queue. Admitting a verdict-free acceptance kind therefore touches the `decision` CHECK constraint and that one view filter; everything else falls out:

- **Gate-side staleness for free.** Each report-only check's instruction file plays the gate role, exactly as type specs and COLLECTION.md contracts already do (ADR 038/041 pattern). Editing `critique-note.md` stales every anchored critique as `gate-changed`.
- **Warn queue untouched.** Verdict-free rows never enter the fix queue, which is the right behavior unprompted — routed reports are not findings to auto-fix.
- **Cumulative baseline by construction.** The accepted snapshot gives the S0→current diff, never the incremental one. Candidate constraint 2 in [carry-heuristics](./carry-heuristics.md) (preservation is not compositional; judge the cumulative diff) is enforced mechanically rather than left to agent discipline.

## What transformations stop needing to save

With every check anchored to content, transformations write nothing: any edit stales every anchored record unconditionally, and the closing review sees the change *in the diff* rather than in a transformation-side declaration. Two consequences for the carry-heuristics sketch:

- **No carry records on the transformation side.** Sketch item 2 ("every carry is a version-anchored record") collapses into the ack itself — the ack *is* the carry record. See the residual requirement below.
- **Footprints soften to stated intent.** The step-9 flow pass's "flow/coherence only" contract needs no enforcement machinery: if the copyedit leaks a claim change, the cumulative diff shows it to the closing review. Declared footprints become planning guidance the diff verifies — the softening carry-heuristics already anticipated, now with the verifying surface identified.

## The license distinction

What a fresh record *licenses* differs by check kind, and the orchestrator prompt must keep this sharp:

- A fresh **gate acceptance** licenses skipping the review (the existing semantics).
- A fresh **verdict-free record** licenses only reusing the report's content as current evidence — "this critique still describes these bytes." It is never an endorsement of the note, and in particular the friction gate's "For the human" routing is never satisfied or silenced by an ack.

This distinction is why anchoring routed reports need not re-create certification semantics through the back door — but that is now a hypothesis the MVP observes rather than a rule it presumes. The workshop's case 3 flips accordingly: from "expected output is a documented do-not-anchor rule" to *anchor and watch* — does a current-critique signal in practice get read as "critiqued and handled"? If MVP use exhibits that failure, the do-not-anchor rule comes back located instead of assumed.

## Residual requirement: rationale on ack

"Transformations don't need to save anything" holds for staleness but not for rationale. `commonplace-ack-gate-review` currently records only the pointer to the reused review pair plus fresh snapshots — no rationale field anywhere in `acknowledgement.py` or the `acceptance` table. If the ack is the carry record, it must capture the carry judgment's *why* (and a rough edit-kind tag) at decision time — process history has one chance to become checkable ([history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md)). Without it, the observation log has no attribution substrate when an audit re-run flips a carried assessment. A rationale column on ack is the one schema addition the MVP needs beyond the verdict-free acceptance kind.

## Why one closing cycle suffices

The full pass has exactly two transformations — step 8 (apply the reconciled packet) and step 9 (flow-only copyedit) — already ordered content-before-form. Divergence danger is structurally low: form fixes can't reopen content decisions, and if step 9 leaks anyway the cumulative diff catches it by content, not by trusting the flow-only declaration. So the closing review is one cycle with the stopping rule from carry-heuristics constraint 4: for each anchored check, the orchestrator reads the cumulative diff and either acks (with rationale) or re-runs; residual findings route to the packet's open items; no second transformation round.

---

Relevant material:

- [carry-heuristics.md](./carry-heuristics.md) — draws-on: the constraint list this design leans on and the trust-but-check sketch it refines
- [mvp-plan.md](./mvp-plan.md) — produces: the concrete build list this design implies
- [Review system](../../reference/README-REVIEW-SYSTEM.md) — depends-on: the freshness, acceptance, and ack machinery being extended
- [History has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — rationale: why the ack must carry rationale at decision time
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the checked-or-absent principle the sampled audit extends to judgment-valued caches
