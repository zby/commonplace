# Unified diff and ack: one freshness surface for all note assays

The minimal unification the MVP commits to: every note assay in the full pass — verdict-bearing (semantic gates) or not (compression bundle, critique-note, composition-friction-gate, connect) — gets the same version-anchored diff-and-ack treatment the review DB already gives gate reviews. An acceptance row pins the exact note and check text the evidence was computed against; the selector classifies fresh / note-changed / gate-changed by snapshot comparison; a stale record is either re-run or acked against the current bytes.

This is a build decision in the working-stance sense — the lightest representation that lets the MVP run — not a closed architecture question. What it deliberately does *not* decide: footprint machinery, edit-kind taxonomies in the system, trust-dial automation.

## Why the unification is nearly free

The staleness layer is already verdict-agnostic. Freshness classification compares snapshot hashes only (`src/commonplace/review/review-schema.sql`, selector query pattern at the bottom of the file); the decision column is consulted in exactly two consumer-side places — the `current_gate_acceptances` view's `rp.decision IS NOT NULL` filter and the warn-selector's fix queue. Admitting a verdict-free acceptance kind therefore touches the `decision` CHECK constraint and that one view filter; everything else falls out:

- **Gate-side staleness for free.** Each report-only assay's instruction file plays the gate role, exactly as type specs and COLLECTION.md contracts already do (ADR 038/041 pattern). Editing `critique-note.md` stales every anchored critique as `gate-changed`.
- **Warn queue untouched.** Verdict-free rows never enter the fix queue, which is the right behavior unprompted — routed reports are not findings to auto-fix.
- **Cumulative baseline by construction.** The accepted snapshot gives the S0→current diff, never the incremental one. Candidate constraint 2 in [carry-heuristics](./carry-heuristics.md) (preservation is not compositional; judge the cumulative diff) is enforced mechanically rather than left to agent discipline.

## What transformations stop needing to save

With every check anchored to content, transformations write nothing: any edit stales every anchored record unconditionally, and the closing review sees the change *in the diff* rather than in a transformation-side declaration. Two consequences for the carry-heuristics sketch:

- **No carry records on the transformation side.** Sketch item 2 ("every carry is a version-anchored record") collapses into an event written at ack time — but *not* into the acceptance row itself. See the residual requirement below: the ack advances current state; the carry judgment is history and needs an append-only record.
- **Footprints soften to stated intent.** The step-9 flow pass's "flow/coherence only" contract needs no enforcement machinery: if the copyedit leaks a claim change, the cumulative diff shows it to the closing review. Declared footprints become planning guidance the diff verifies — the softening carry-heuristics already anticipated, now with the verifying surface identified.

## Note assays: the category and its failure-mode split

Vocabulary adopted for this workshop: a **note assay** is any read-only procedure run against exact note bytes that produces anchored evidence about the note — the genus covering review gates, critique-note, composition-friction-gate, the compression bundle's gates, and connect. Distinct from deterministic validation (code checking recomputable facts): an assay is a judgment-valued measurement of a sample, and may be qualitative or quantitative.

Two species, named for the boundedness of the question they ask — deliberately not for their mechanism, because at run time both work the same way: directed model attention over the note, reporting what that attention found. Neither guarantees anything. A passing gate cannot certify that no failure exists, only that its directed attention detected none — the review-system doc already frames `pass` as an absence-of-detected-problem signal, never certification. The split is in the *question asked*, not the certainty of the answer:

- A **bounded assay** asks a closed question: is named pattern X present? Its verdict is a fallible answer to a fixed question. Re-running it against unchanged bytes re-samples the same detector — the expected yield is detector variance, not new coverage — so the cached answer has near-full replacement value, and its acceptance can carry a **skip license**: fresh means re-asking would be redundant, *not* that no failure exists.
- An **unbounded assay** asks an open question: what is wrong, thin, or connectable here? Its output is a sample of attention over an unbounded space. Re-running against unchanged bytes explores new regions and is *expected* to surface different material, so the cached report has no replacement value — its acceptance carries only an **evidence-currency license**: fresh means this sample still describes these bytes.

The verdict difference is downstream of the question difference. A closed question can be answered pass/warn/fail; forcing a verdict onto an open question would not close the space it samples — it would only manufacture false confidence (the exact failure the friction gate's hard rule exists to prevent). The same split sets the audit unit: for a bounded assay a "flip" is a verdict change, and the control arm's base rate measures detector variance; for an unbounded assay every re-run differs textually, so the audit question is whether the fresh sample *materially* diverges from the carried report — a judgment the MVP observes rather than pre-formalizes.

The axis cuts across the current DB boundary. Compression-bundle gates ask closed questions over named patterns (branch-bloat, detail-overhang, marginal-value-redundancy) — bounded assays that happen to run outside the DB today, so in principle their acceptances could carry skip semantics. Connect prospects an open link space — unbounded. So the acceptance kind must record the assay's *declared class*, and the license derives from the class — never from where the assay currently runs or whether a result line happens to exist.

**"Gate" keeps its name.** The assay vocabulary classifies; it does not rename. "Review gate" stays the operational term for the shipped unit — a catalog file executed through the batch mechanism (select → create-jobs → sub-agent → finalize) with verdict semantics — and it is load-bearing in CLI names, the schema's `gate_path`, and the ADRs. The layered statement: gates are the shipped bounded assays that run through the batch mechanism.

**The batch mechanism generalizes to unbounded assays — in class-homogeneous jobs.** Nothing in select / create-jobs / sub-agent execution / finalize depends on the verdict except the result-line parser and the `decision` column. Running critique through the pipeline as the first unbounded assay is therefore cheap — and it is also the *sound* registration surface. A record-after-the-fact command would accept the orchestrator's claim that a report was computed against these bytes: a self-reported anchor with a time-of-check gap (the note can change between assay run and recording). The pipeline pins snapshots itself as part of executing the assay, so the anchor is enforced by construction — the same enforced-or-omitted logic as marks. Batch execution also matches critique's own contract (fresh adversarial sub-agent) and gives unbounded assays model partitions for free.

The generalization has one structural constraint: **a job never mixes result-kind classes.** With `--grouping note` a job packs all of a note's pairs into one shared prompt and one sentinel-delimited output, so a mixed job would need per-pair parser expectations, would hand one sub-agent blended instructions (closed-question checking next to open-ended critique reading, degrading both — critique's contract wants a dedicated fresh agent), and under all-or-nothing finalization a malformed critique block would void the note's gate acceptances — coupled failure domains for no benefit. Separate bundles give homogeneity with no new machinery: the shipped packing already keys note-grouped jobs by `(note, bundle)` and gate-grouped jobs by gate, so a job never spans bundles — making critique its own bundle is sufficient. The selector already addresses bundles by name, and each job then carries exactly one output contract, keeping the parser change a job-level expected-result-kind rather than per-pair logic.

## The license distinction

What a fresh record *licenses* differs by assay class, and the orchestrator prompt must keep this sharp:

- A fresh **bounded-assay acceptance** licenses skipping the re-run (the existing gate semantics).
- A fresh **unbounded-assay acceptance** licenses only reusing the report's content as current evidence — "this critique still describes these bytes." It is never an endorsement of the note, and in particular the friction gate's "For the human" routing is never satisfied or silenced by an ack.

A third record kind sits outside the assay genus: a **human attestation** (MVP phase 5) is not an assay at all — no procedure ran; a person recorded that they reviewed these bytes. The contract wording matters: "reviewed these bytes," not "accepts it" — accepting is already endorsement-shaped, a force smuggled into a supposedly force-free record. In the MVP it carries **no license**: an anchored, queryable fact that nothing consumes as permission to skip or suppress. Its force is the deliberately open part of workshop case 2 — decided by observed need, not up front. It is also not a cheap reuse of the acceptance store, which requires completed review-pair evidence; its representation is a separate probe (mvp-plan phase 5).

This distinction is why anchoring routed reports need not re-create certification semantics through the back door — but that is now a hypothesis the MVP observes rather than a rule it presumes. The workshop's case 3 flips accordingly: from "expected output is a documented do-not-anchor rule" to *anchor and watch* — does a current-critique signal in practice get read as "critiqued and handled"? If MVP use exhibits that failure, the do-not-anchor rule comes back located instead of assumed.

## Residual requirement: the carry judgment is history, not state

"Transformations don't need to save anything" holds for staleness but not for the carry judgment's *why*. The first draft of this file put a rationale column on acceptance; a codex review located the flaw against shipped code: acceptance is deliberately current-state storage with inline pruning ([ADR 036](../../reference/adr/036-review-acceptance-is-current-state-not-append-only-history.md)) — a superseding rerun deletes the prior pair, job, and artifacts in the same transaction. At 100% audit sampling the sequence *ack with rationale → audit rerun → rerun supersedes acceptance* destroys the rationale exactly when the audit result arrives.

So the two facts live in two stores with different semantics: the **ack advances current state** (the accepted baseline); the **carry judgment is an append-only event** — rationale required, edit-kind tag, and a capture of the prior evidence taken *before* pruning can remove it — because process history has one chance to become checkable ([history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md)). Acceptance may cache the latest rationale for convenience, but the event record is authoritative. At 100% sampling the event is a `would_ack` followed by the rerun, so acceptance moves once instead of being transiently advanced and immediately superseded.

A sibling distinction was located the same way: **verdict vs. completion**. A decision (pass/warn/fail/error) and a protocol completion marker are different facts — unbounded assays complete without deciding — so the pair carries a persisted `result_kind` written at creation, and finalization parses against that persisted contract rather than re-reading gate state at finalize time (which would reintroduce a time-of-check gap; `upsert_acceptance` also hard-rejects null-decision pairs today, so acceptance must key on completion, not decision). Both distinctions are operation-semantics findings of exactly the kind this workshop hunts — located by design review against shipped code before any run.

## Why one closing cycle suffices

The full pass has exactly two transformations — step 8 (apply the reconciled packet) and step 9 (flow-only copyedit) — already ordered content-before-form. Divergence danger is structurally low: form fixes can't reopen content decisions, and if step 9 leaks anyway the cumulative diff catches it by content, not by trusting the flow-only declaration. So the closing review is one cycle with the stopping rule from carry-heuristics constraint 4: for each anchored assay, the orchestrator reads the cumulative diff and either acks (with rationale) or re-runs; residual findings route to the packet's open items; no second transformation round.

---

Relevant material:

- [carry-heuristics.md](./carry-heuristics.md) — draws-on: the constraint list this design leans on and the trust-but-check sketch it refines
- [mvp-plan.md](./mvp-plan.md) — produces: the concrete build list this design implies
- [Review system](../../reference/README-REVIEW-SYSTEM.md) — depends-on: the freshness, acceptance, and ack machinery being extended
- [History has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — rationale: why the ack must carry rationale at decision time
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the checked-or-absent principle the sampled audit extends to judgment-valued caches
