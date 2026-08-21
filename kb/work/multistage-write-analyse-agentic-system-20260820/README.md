# Workshop: analyse an agentic system

- **Immutable run key:** `kb/instructions/analyse-agentic-system/SKILL.md`
- **Current intended target:** `kb/instructions/analyse-agentic-system/SKILL.md`
- **Mode:** new write
- **Collection:** `kb/instructions/`
- **Type:** `kb/types/instruction.md`
- **Acceptance review:** required — the eventual instruction will route several analyses and replace a functioning review workflow. **Complete 2026-08-21: PROMOTE WITH NAMED CHANGES**, twelve required changes in `acceptance.md` §5, not yet applied.

## Goal

Design one public procedure for analysing an external agentic system as a whole. The procedure should establish one source and evidence boundary, analyse the runtime, invoke memory/context analysis when retained material can shape a later invocation, invoke epistemic analysis when a material route handles truth-apt content or makes a knowledge-production claim, and synthesize the findings without collapsing the lenses.

Memory is an internal lens of agentic-system analysis. Its current separate collection is historical: it was the first external-system review methodology to mature. This workshop does not treat memory as a peer system category.

## Current state

The initial assembly is complete: operative precedents are preserved, modular source/runtime/memory baselines are written, and independent reconstruction, disposition, and instruction-skeleton passes agree on the ownership split. A fresh-context writer has realized the skeleton as `draft.md` (skill-shaped, zero `NEW COMMITMENT FOR AUDIT` markers). A fresh-context auditor has written `audit.md`: 27 anchored findings, all `Status: open` — 14 keep, 12 clarify, 1 ground, 0 remove, 0 ask-user. The audit confirmed the writer's zero-new-commitments claim except one strengthened run-ID citation rule (finding 1.1), checked that the footer link *targets* exist and that their annotations match the notes (it did **not** verify link resolution from the promotion path — its finding 6.2 wrongly resolved "keep" on root-style markdown links, corrected at acceptance), verified the epistemic-invocation consistency, and disposed the four writer-flagged ambiguities (WF-a relocate topology rules to run level; WF-b keep; WF-c ground — add the packaging-theory `rests-on` entries per disposition D; WF-d add `user-invocable: true`, defer `allowed-tools`/`context`/`model` explicitly).

The audit ran before the lens-routing trials by design: the skeleton classifies integrated cold trials as blocking promotion, not drafting, and they must run on the exact candidate. Reconciliation is complete: all 27 findings are `Status: resolved` in `audit.md` with named resolutions, and `candidate.md` realizes them — run-ID rule scoped to the skeleton's commitment (1.1), worker topology moved to a run-level subsection at the end of step 3 (WF-a), evidence-packet contents specified (4.4), tier rule tied to the step-4 baseline (4.1), loop materiality test added (4.2), recorded-search-boundary wording for `absent` (4.3), invoked method's "observed candidate state" vocabulary (3.3), horizon marked as a run-level extension (3.4), orchestrator introduced in the opening (5.1), inline `invokes` grammar fixed (6.1), footer titles corrected and the three packaging-theory `rests-on` entries added per disposition D (6.4, WF-c), and frontmatter extended with `user-invocable: true` and an `argument-hint` (WF-d). No finding required a user decision; reconciliation changed ordering, expression, and disposition-authorized grounding only — no new evidence and no change to the central contribution, so no stage rebuild was triggered. Next stage: cold-run the exact candidate across the four lens combinations (trial-system selection is a pending user decision), then acceptance review (required) before any promotion or collection migration.

Deliberate deferral (per audit finding WF-d): `allowed-tools`, `context`, and `model` frontmatter values are unfixed by workshop inputs and are deferred; promotion must resolve this deferral explicitly because operativity is blocking at promotion.

## Known instruction inputs

The `known-instructions/` directory preserves or extracts procedures whose behavior is already understood well enough to use as workshop baselines:

- `current-memory-review-skill.md` — byte-for-byte snapshot of the functioning local review skill.
- `current-memory-analysis-contract.md` — byte-for-byte snapshot of the functioning memory review type contract, which currently carries much of the analysis procedure.
- `current-epistemic-analysis.md` — byte-for-byte snapshot of the accepted and cold-trialled epistemic instruction.
- `current-agentic-comparison-instruction.md` — byte-for-byte snapshot of a bounded whole-system comparison instruction that produced a substantive review, retained as precedent rather than a general contract.
- `prepare-code-grounded-source-baseline.md` — a new modular extraction of the functioning GitHub checkout, revision-pinning, and citation preparation steps.
- `analyse-agent-runtime-baseline.md` — a new, deliberately narrow baseline built from the established scheduler/context/external-state distinction and repeated agentic-system review practice. It is understood but not yet independently trialled as a general instruction.
- `analyse-memory-context-baseline.md` — a new modular extraction of the stable memory/context parts of the current review contract. It preserves current distinctions while removing collection placement, comparison-with-Commonplace, and publication concerns.

Exact snapshots are inputs, not proposed final structure. The three extracted baselines are executable workshop artifacts, not promoted instructions.

## Design boundary

Fixed for this workshop:

- one public entry point;
- one `kb/agentic-systems/` collection for whole-system analyses and their lenses;
- one shared source/revision/evidence pass per reviewed system;
- runtime analysis for every in-scope agentic system;
- **both lenses run on every in-scope system, at a depth proportionate to what the evidence supports** (user decision, 2026-08-21). This supersedes the original boundary item, "explicit applicability dispositions for memory/context and epistemic lenses." Five trials returned `applicable` for both lenses — the fifth deliberately targeted a trigger-poor subject and still triggered both — so the gate never fired and its `inapplicable`/`uncertain` branches were never exercised. Step 5 becomes a scoping step that names trigger evidence and sets depth; `uncertain` becomes an evidence limitation inside a lens output, never an exit, preserving the property the gate existed to protect: "we could not tell" must never read as "there is nothing there";
- memory/context analysis on every run, scoped by whether retained material accumulated or changed through use can shape later behavior;
- epistemic analysis on every run, scoped by whether a route produces, transforms, checks, accepts, or authorizes truth-apt content, or the system makes a knowledge-production or warrant claim;
- evaluation-driven behavior or policy adaptation with no evidenced truth-apt object and no knowledge/warrant claim remains a runtime finding; under the 2026-08-21 decision this exception no longer gates the epistemic lens but scopes its objects — the route stays in the runtime account and is named for the orchestrator rather than analysed as an epistemic route;
- synthesis preserves lens-specific findings and evidence limits.

Not fixed yet:

- whether a published system analysis is one file or a per-system package;
- whether lens instructions remain internal sections of one skill or become separately invocable instructions;
- the final output schema and which controlled values deserve parser support;
- the migration sequence for the existing memory corpus and comparison matrix.

These are design questions, not permission to mechanically relocate or patch the current corpus.

## Inputs

- `kb/agentic-systems/COLLECTION.md`
- `kb/agentic-systems/README.md`
- representative whole-system analyses under `kb/agentic-systems/`
- `kb/agent-memory-systems/COLLECTION.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml`
- `kb/instructions/write-agent-memory-system-review/SKILL.md`
- `kb/agent-memory-systems/review-framework-design.md`
- `kb/instructions/analyse-external-system-epistemic-architecture.md`
- `kb/work/multistage-write-analyse-epistemic-architecture-20260820/`
- `kb/work/pi-agent-zerostack-comparison/review-instruction.md`
- `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`
- `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`
- `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md`
- `kb/notes/runtime-structure-determines-governance-control-surfaces.md`
- `kb/notes/definitions/behavioral-authority.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `kb/instructions/COLLECTION.md`
- `kb/types/instruction.md`

## Checklist

- [x] `brief.md`
- [x] `reconstruction.md`
- [x] `claim-disposition.md`
- [x] `claim-skeleton.md`
- [x] `draft.md`
- [x] `audit.md`
- [x] `candidate.md`
- [x] lens-routing trials — four cold runs executed; see `trial-evaluation.md`. **Coverage incomplete:** all four returned both lenses `applicable`, so no early exit was exercised.
- [x] post-trial candidate revision — twelve fixes applied to `candidate.md`; dispositions recorded in `trial-evaluation.md` ("Post-trial revision pass")
- [x] fifth trial (`sequentialthinking`, run against the revised candidate) and its four repairs R1–R4; dispositions in `trial-evaluation.md` ("Fifth trial")
- [x] early-exit trial or recorded limitation — resolved by design change, not by testing. **Five trials, five double-`applicable` results**; the fifth deliberately targeted a trigger-poor subject and still triggered both lenses. Escalated to the user, who chose to make both lenses mandatory with proportionate depth (2026-08-21), removing the untested branch by removing the branch
- [x] sixth trial — `sequentialthinking` re-run against the post-amendment candidate, validating proportionate depth: memory judged **brief**, epistemic **full**, on the same subject. Three follow-ups applied (classify-only seam, `implemented`→`afforded` rename, reading-order note); dispositions in `trial-evaluation.md` ("Sixth trial" and "Validation re-run")
- [x] `acceptance.md` — **Verdict: PROMOTE WITH NAMED CHANGES** (fresh reviewer, 2026-08-21). Twelve required changes in its §5, all text-local (~10 lines added, 3 removed); no design decision reopened, nothing the trials validated disturbed. Frontmatter resolved with named values (§6). Nine known limits routed to a `kb/reference/proposals/` design proposal so they survive workshop deletion (§8).
- [x] apply the twelve required changes from `acceptance.md` §5 to `candidate.md` — all applied 2026-08-21, plus a full self-narration sweep and the two record corrections (this file's audit-link claim; `brief.md`'s superseded four-combination criterion). Link resolution from the promotion path verified: 9 markdown links resolve, the one code-span pointer exists. **`candidate.md` is ready for promotion; the coordinator writes the target.**
- [x] promotion — `kb/instructions/analyse-agentic-system/SKILL.md` written from `candidate.md` (200 lines, byte-identical), 2026-08-21. `commonplace-validate`: **PASS (clean)**, zero warnings, all local relative links resolve. Projected as committed relative symlinks into `.claude/skills/` and `.agents/skills/`, and confirmed discoverable by the harness. Collection navigation deliberately not touched: `kb/reference/README.md:52` still describes the memory-review workflow this skill will eventually subsume, and rewriting it belongs to the corpus migration below, not to promotion
- [ ] collection/type/schema migration design
- [ ] corpus regeneration plan

## Lens-routing trial design

Trial pool (user decision, 2026-08-20): systems already reviewed in the KB, so prior analyses serve as ground-truth baselines for judging trial output — withheld from the trial workers, never given as input. Trial workers run cold: candidate + frozen sources only, no expected-combination hints, on `claude-opus-5` (user decision). Existing checkouts are inspected as-is at the commits the prior reviews pinned (no refresh), preserving comparability.

Slate (per-slot expectations are trial-design hypotheses; the candidate's own step 5 makes the actual dispositions, which is part of what is being tested):

| Trial dir | System | Frozen source | Expected combination | Known tension the trial probes |
|---|---|---|---|---|
| `trials/fractal/` | Fractal | `related-systems/Trampoline-AI--fractal` @ `5954a07d` | runtime only | epistemically clean, but disk-persisted session continuity may fire the memory trigger under a strict reading — informative about trigger breadth either way |
| `trials/swamp/` | Swamp | `related-systems/swamp-club--swamp` @ `cf38c4ec` | runtime + memory | CEL `data.latest` read-back over versioned observations is memory without trace-learning; epistemic expected negative (no check/accept route) |
| `trials/cc-dynamic-workflows/` | Claude Code dynamic workflows | docs snapshot `kb/sources/claude-code-dynamic-workflows-docs.md` (2026-06-03), optionally + captured in-session tool contract | runtime + epistemic | doc-grounded (no repo) — also exercises the non-repository source branch; session-local journal vs the save-as-command retention channel |
| `trials/gbrain/` | GBrain | `related-systems/gbrain` @ `9a0bae8d` | runtime + both | the clean double-positive (facts/takes with confidence/supersession; dream-cycle consolidation) |

**Trial outcome (2026-08-21).** Three runs produced the complete eleven-record result, held one register and one revision, upgraded no status, and reported the publication blocker rather than improvising a target; the fourth (GBrain) finished after a usage-limit interruption and logged fifteen friction points. All four returned **both lenses `applicable`**, so the runtime-only and epistemic-without-memory combinations were never exercised and no early-exit record was produced. The convergence is itself a finding — for systems interesting enough to review, both triggers fire nearly always — but it leaves the `inapplicable`/`uncertain` branches untrialled. Full assessment, the twelve pre-promotion fixes and their dispositions, and the validated features are in `trial-evaluation.md`.

Slate provenance: two scouting passes over the reviewed pool found no clean runtime-only or epistemic-without-memory system — retention is near-ubiquitous in systems selected for orchestration/self-improvement interest. The original slate guesses (Swamp runtime-only, Voyager memory-only) were corrected by review evidence: Swamp has real memory read-back, and Voyager's curriculum QA cache plus critic verdicts make it epistemic-positive (duplicating GBrain's combination). The user chose Fractal and CC dynamic workflows for the contested slots, accepting the boundary arguments as part of the trial.

## Human decisions and blockers

- The user fixed the collection relationship: memory belongs inside agentic systems; its separate collection is historical, not conceptual.
- The user authorized this workshop and asked it to contain instructions already understood or already functioning.
- No blocker prevents reconstructing the unified instruction. Publication shape and corpus migration remain downstream decisions and must not be silently chosen by an early draft.

## Pending handoffs

- Revise `kb/agentic-systems/COLLECTION.md` only after the instruction and output shape survive representative trials.
- Replace or retire the current memory review type, schema, skill, matrix discovery, and separate collection only through a source-regeneration migration; do not mechanically retrofit semantic classifications.
- Reconcile the current memory type/schema trace-learning drift (`trace-learning`/`### Trace-learning` in the type versus legacy `trace-derived`/`### Trace-derived learning` in the schema) before treating the schema as the durable lens contract.
- Decide durable paths for any independently invocable lens instructions after routing trials show whether separate operativity is useful.
- **Repair Branch 2's "Then stop" in `kb/instructions/analyse-external-system-epistemic-architecture.md`** — separate work, not this workshop's, because that instruction is promoted and accepted. Found by the sequentialthinking re-run (`trials/sequentialthinking-rerun/trial-notes.md` F11) and the only place in five-plus trials where a worker had to override an instruction's literal text to reach the right answer. Two linked problems in its step 3. First, the two branches overlap: a system whose inventory is dominated by storage and serving (Branch 1's first condition) can simultaneously make an explicit knowledge-production claim, which defeats Branch 1's second condition and triggers Branch 2; the worker resolved it on Branch 1's conjunctive wording. Second and more serious, Branch 2 closes with "Then stop", which read literally discards the implemented routes the material-route rule has already admitted — in this run, the artifact's only real truth-apt edges, which carried its headline finding. The worker reasoned past it on the grounds that Branch 2 prescribes what to do about the *claim* and does not retract the inventory. That reading is right and should become the text: Branch 2 should stop the *claim assessment*, not the route analysis. Evidence and the worker's reasoning are in the re-run's `lens-epistemic.md`.

## What closes this workshop

The unified instruction has passed cold trials on systems that exercise different lens combinations; the target agentic-systems collection/type design is explicit; and the memory corpus has a source-regeneration migration plan. Promotion and migration may occur in separate atomic runs, but their decisions must no longer be implicit.
