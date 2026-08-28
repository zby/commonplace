# Extraction candidates

Claims that the articles currently carry, or would have to carry, that could
instead be library notes the articles cite. Coverage verdicts come from a
scout pass over `kb/notes/` on 2026-08-28 (335 notes plus `definitions/` and
`evidence/`). All nine were written on 2026-08-28; each entry records its path under **Status**.

Titles are drafts in claim form. Each note, once written, gets a row in the
[ledger's transfer record](./incumbent-ledger.md#transfer-record) naming the
source claim IDs it discharges.

## Extract — absent from the library, load-bearing for a named article job

### E1. Each reason a decision stays human needs a different mechanism, so a self-improving architecture is mixed by necessity

- **Status.** Written 2026-08-28 as `kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md`.

- **Claim.** The residue classes — unrepresented premise, unsettled criterion,
  no independent check, horizon cut — each require a different mechanism
  (representation, settlement, verification, continuity), and no single part
  of the architecture covers another's class. Retained theory supplies
  representation and settlement; the interpreter applies settlements across
  unformalized cases; oracles supply verification; the symbolic runtime
  supplies horizon. Mixedness is derived, not stipulated.
- **Coverage.** Absent. Nearest:
  `kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md`
  (residue table names capacities, not parts);
  `kb/notes/bounded-context-orchestration-model.md` (scheduler + LLM motivated
  by context scarcity, not warrant classes);
  `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md`
  (argues one substrate for interpretation and retention — the opposite
  direction).
- **Unloads.** Hub (job 0), benchmark (job 2). Discharges the author-direction
  bullet "the target is not natural-language theory plus weights alone".
- **Premise-change test.** Drop a residue class and the corresponding part
  becomes optional; add a class with no part and the architecture is
  incomplete.
- **Ledger IDs.** T5 (formalization moves the theory problem), O8, R6.

### E2. A benchmark that holds the client fixed exports the least-warrantable decisions by design

- **Status.** Written 2026-08-28 as `kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md`.

- **Claim.** Any "as good as a competent remote X" comparison holds brief,
  feedback, and acceptance constant. Those are the unsettled-criterion and
  acceptance rows of the residue — the hardest to warrant. The benchmark
  therefore measures capability under a declared cut; it does not measure
  closure over the exported decisions, and presenting it as closure is
  boundary export.
- **Coverage.** Absent. Nearest in form:
  `kb/notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md`
  (benchmark shows less than it appears because ingredients are supplied);
  `kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`.
- **Unloads.** Benchmark (job 2); the separation rule on the client cut.
- **Ledger IDs.** O7, O9.

### E3. A theory-mediated loop closes only by causal co-indexing, not by co-occurrence inside one boundary

- **Status.** Written 2026-08-28 as `kb/notes/a-theory-mediated-loop-closes-only-by-causal-co-indexing.md`.

- **Claim.** The same theory must guide the change, the change's result must
  test that theory, and the revised theory must affect later operation on the
  same path. Theory mediation, reflection, and self-improvement each occurring
  somewhere inside one boundary (disconnected witnesses) do not establish the
  loop; a system with three disconnected paths is the counterexample.
- **Coverage.** Partial. `kb/notes/definitions/reflective-system.md` requires
  one named path with two-way causal connection;
  `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md`
  adds membership, interpretation, retention. Missing: the three-way
  co-indexing stated as a closure test and the explicit rejection of
  co-located disconnected witnesses.
  `kb/notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md`
  applies it case-wise without stating it.
- **Unloads.** Self-theories successor (jobs 2 and 5). This is the S2/S3/S4
  defeat stated positively; currently it exists only as a workshop constraint.
- **Ledger IDs.** S2, S3, S4 (defeated as stated / as sufficient).

### E4. A method's ceiling bounds the method, not the transfer it already made

- **Status.** Written 2026-08-28 as `kb/notes/a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md`.

- **Claim.** A bounded mechanism (formatter, compiler) makes real progress up
  to its ceiling; reaching the ceiling leaves the rest of the residue visible
  without making the transfer unreal. Performance inside an envelope (quality,
  reliability, coverage, cost) is a different kind of progress from envelope
  expansion; only expansion changes which decisions remain human.
- **Coverage.** Absent. Nearest:
  `kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md`,
  `kb/notes/constraining-and-extraction-both-trade-generality-for-reliability.md`,
  `kb/notes/improvements-can-accumulate-without-compounding.md` — all
  partition progress differently.
- **Unloads.** Bootstrap (job 3), hub. Carries the envelope/ceiling
  vocabulary the shared model uses without a citable home.
- **Ledger IDs.** O5, O6.

### E5. Tool usefulness, computational autonomy, warrant, and system power are separate dimensions

- **Status.** Written 2026-08-28 as `kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md`.

- **Claim.** Four dimensions move independently: how well the human–agent
  composite performs its function, how much of a path runs without a person,
  whether what runs unattended can be trusted, and how capable the system is.
  Autonomy does not entail power; the Bitter Lesson motivates a possible power
  gain as an empirical conjecture, not as a consequence of autonomy.
- **Coverage.** Absent as a four-way separation. Pairwise pieces:
  `kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md` (autonomy vs
  warrant), `kb/notes/increasing-computational-autonomy-relocates-human-effort.md`
  (autonomy vs effort),
  `kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md`.
- **Unloads.** Bitter Lesson (job 6), hub, and the separation rule "the plan
  must not become a power theorem".
- **Ledger IDs.** O3, O11, and the author-direction bullet on dimensions.

### E6. Citing retained theory at the decision point is a mediation trace

- **Status.** Written 2026-08-28 as `kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md`.

- **Claim.** When the theory that guided a decision is cited where the
  decision is made, the citation is the mediation trace: addressability makes
  tracing which theory guided a change cheap, and the trace is what separates
  theory-guided change from change that merely co-occurs with retained theory.
- **Coverage.** Absent. "Mediation trace" appears nowhere. Nearest:
  `kb/notes/reflection-buys-addressability.md` (readable, criticizable
  retention; does not treat a citation as evidence of mediation);
  `kb/notes/evidence/tag-readme-trace-observed-causal-connection.md` (one
  observed trace instance);
  `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`.
- **Unloads.** Bootstrap (job 3). Closure condition 9 rests on it.
- **Ledger IDs.** S4 (mediation trace requirement), O10, T2.

## Extract — partial in the library, worth consolidating

### E7. Programming-tool progress is a partial order on accepted outcomes per total human effort

- **Status.** Written 2026-08-28 as `kb/notes/programming-tool-progress-is-a-partial-order-not-a-scalar.md`.

- **Claim.** A change is forward when, at a fixed task class and acceptance
  threshold, it produces no worse outcomes with no more total human
  programming effort and strictly improves one term. Effort counts
  configuration, review, recovery, and repair. There is no unique scalar; the
  order is partial and does not imply convergence.
- **Coverage.** Partial.
  `kb/notes/increasing-computational-autonomy-relocates-human-effort.md`
  establishes "per human judgment, not human time"; the O8 note defines
  leverage in one line. Missing: the partial-order form, the explicit "no
  unique scalar", and the effort accounting.
- **Unloads.** Hub, bootstrap. The articles currently re-explain the
  accounting each time.
- **Ledger IDs.** O5, T3 (defeated scalar).

### E8. Explicit artifacts buy addressability, not credit assignment, coherence, retrieval, or admission

- **Status.** Written 2026-08-28 as `kb/notes/explicit-artifacts-buy-addressability-not-credit-assignment.md`.

- **Claim.** Making retained state explicit makes it inspectable and
  addressable. It does not by itself assign credit for outcomes, keep the
  store coherent, guarantee correct retrieval, or decide admission; each is a
  separate mechanism that explicitness makes possible but does not supply.
- **Coverage.** Partial. Positive half in
  `kb/notes/reflection-buys-addressability.md` and
  `kb/notes/only-explicit-retention-is-durable-writable-and-addressable.md`.
  The negative list is scattered
  (`kb/notes/a-retrieval-miss-is-a-local-reflective-path-failure.md`,
  `kb/notes/raw-accumulation-does-not-create-usable-memory.md`).
- **Unloads.** Continual-learning successor (job 5). Ledger row C4 is
  "defeated as stated" for exactly this reason.
- **Ledger IDs.** C4, C1.

### E9. Removing a human judgment can degrade the judgments that remain

- **Status.** Written and then retired 2026-08-28 as trivial: the parent note's one sentence plus its defeater carries it.

- **Claim.** A person left only with the decisions that cannot be checked,
  and with less contact with the routine cases that used to inform them, is
  worse placed to make those decisions. Transfer can therefore lower the
  quality of the remaining human judgments even while leverage rises. This is
  the mechanism behind requiring a warrant comparison and not only an
  autonomy record for each transfer.
- **Coverage.** Partial. One sentence in the O8 note; Bainbridge is cited in
  `kb/notes/increasing-computational-autonomy-relocates-human-effort.md` and
  `kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
  for the relocation/residue reading, not for degradation. Missing: the
  mechanism (loss of contact with routine cases) stated in its own right.
- **Unloads.** Bootstrap (job 3); grounds the goal's "or less useful" clause
  and O3's warrant comparison.
- **Ledger IDs.** O3, T6.

## Leave in place

| Candidate | Where it lives | Why not extracted now |
|---|---|---|
| Degenerate closure patterns are one move (apparent warrant at the least-warrantable decisions) | O8 note, "Consequences for closure" | Extracting would split that note's argument; cite the section. |
| Model-realization record: absent, unbound, untrusted, or unverified — four states, four repairs (R4) | Nowhere yet | Belongs to the transition article (job 4); closer to design than transferable theory. Write when job 4 is reconstructed, possibly as `kb/reference/` material. Structural analogues: `kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md`, `kb/notes/llm-output-deviation-requires-three-way-diagnosis.md`. |
| Admission needs a represented grant: holder, scope, conditions, binding (R3) | Nowhere yet | Same as above. Nearest: `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md`, `kb/notes/definitions/behavioral-authority.md`. |
| Learning unit vs concept formation must be declared (C2) | `kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md` covers most | Add a paragraph there rather than a new note. |
| Theory stated over decisions transfers across task types and reads as a build plan (O11) | Hub article thesis | A note now would be the article in miniature; see what generalizes once the hub is drafted. |

## Writing order

E1 and E3 carry real argument and should go first; E6 is small but condition
9 depends on it. E2, E4, E5 are half-page notes. E7–E9 are consolidations and
can follow. Seeds for each: the O8 note and the nearest-neighbour paths above.
