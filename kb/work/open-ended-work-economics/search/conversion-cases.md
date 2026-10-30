# Search results: conversion cases for test 3

Raw material for the routine-conversion test (reconciliation.md,
"Discriminating tests", test 3). Facts only: no application of the account
and no judgment of the cases. Paths are KB-relative (`kb/...`). Quotes are
verbatim from the files named. Where a fact comes from a note that retells
an episode rather than the dated decision record, the note is named.

The six terms the parent's account will use are abbreviated in each
"What the record does not say" list: **recurrence**, **saving per use**,
**construction cost**, **invocation/checking/retrieval cost**,
**maintenance cost**, **stability**.

---

## Case 1. The tag-readme validator (conversion that held, then was revised)

**Records.**
`kb/reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md`
(accepted, 2026-06-10);
`kb/theory/evidence/tag-readme-trace-observed-causal-connection.md`
(timeline "verified 2026-07-30" from git history);
`kb/reference/tag-readme-trace-as-self-improving-loop.md`;
`kb/reference/adr/090-one-completeness-mark-reaches-members-in-one-hop.md`
(accepted, 2026-09-26, amends 026).

**Before conversion.** The `index` type did two jobs: "being an *index*
(complete enumeration) and being an *introduction to a tag*" (ADR 026,
Context). Completeness was a claim the reader had to re-check: "a careful
agent would re-run the by-tag `rg` sweep anyway, so an unenforced claim saves
no work." No size or completeness check existed: "no size validation exists
anywhere in the codebase yet" (trace, timeline 06-07); "no size or
completeness validator existed before ADR 026" (trace, "Verified timeline").

**The routine.** A committed `tag-readme` type with byte weight gates
("soft 8 KB warn / hard 16 KB fail, measured in **bytes**") and two
validator-enforced marks, `complete: true` and `covered_by: [children]`
(ADR 026, Decision 2-4). The trace records that one ADR became four forms in
commit `94769805`: "the natural-language spec (`kb/types/tag-readme.md`), the
JSON schema, the validator (`src/commonplace/lib/validation.py`), and the
build-time renderer", with tests in the same commit. Commit `dab163c6` made
validating one ordinary note also validate "every marked tag-README that
shares its tags".

**Recurrence.**
- Fifteen indexes migrated to the new type (trace, commit `9976a081`).
- The check fires reactively: "fire when the marked README is next validated
  (sweeps, fix runs)" (ADR 026, Decision 5), and after `dab163c6`, whenever a
  note sharing a marked tag is validated.
- The consumer that skips work: "When present, exhaustive consumers like
  `cp-skill-connect` skip the by-tag rg for that tag" (ADR 026, Decision 3).
  No count of connect runs is recorded.
- Marks in use: four heads carry `complete` (trace; ADR 090 Context: "Four
  heads carry `complete`; none carries `covered_by`").
- ADR 090 Context: "A survey of about 6,800 agent sessions found no use of
  the child list as a typed relation."

**Cost language.**
- Saving per use, as stated: "`rg` always recovers full membership at the
  cost of one tool call" (ADR 026, Decision 3). This is the work a `complete`
  mark lets a consumer skip.
- Maintenance, accepted: "Accepted cost: the entry and phrase are written
  cold at fix time rather than hot at write time — eventual correctness over
  write-path complexity" (ADR 026, Decision 5).
- Maintenance surface: "Operative through the `tag-readme` type spec and
  schema and the validator's weight, membership, and coverage checks"
  (ADR 026, Consequences, "Harder").
- Migration: "The hard fail lands only after every existing tag head is
  under the gate"; the calibration commit sequenced "soft warn first, hard
  fail only after the learning-theory split, 'otherwise validation is red on
  day one'" (trace, timeline 06-10 07:35).
- Construction effort is visible only as elapsed time: ADR at 09:20,
  implementation at 09:26, migration at 09:43 on 2026-06-10 (trace,
  timeline). Thresholds came from "a manual calibration pass: median curated
  tag index ≈ 3.5 KB".
- Reader-side cost of the marks' meaning: frontloaded "into AGENTS.md in two
  sentences" so "readers never load the spec — only maintenance work does"
  (ADR 026, Decision 6).

**Stability and risk.**
- Designed-for drift: "A `complete` README inevitably grows into the gate and
  must drop the mark; the design makes the drop *cheap*" (ADR 026, Risks).
- The mark is "an **accelerator, never a load-bearing wall**: no consumer's
  correctness may depend on it" (ADR 026, Decision 3).
- `covered_by` was built ahead of need: "adoption deferred to the first real
  case" (ADR 026, Decision 4).
- The trace's calibration: detection that triggered the change was human;
  "the completeness promise was never observed broken: no enforced
  `complete` mark existed to falsify" (trace, "Verified timeline").
- The self-improving reading: "the validator passing means the marks are
  consistent, not that the type split actually made the KB better"
  (`tag-readme-trace-as-self-improving-loop.md`).

**Outcome.** Still in use, revised. ADR 090 retired `covered_by` and
redefined `complete` as one-hop reach. Stated reason: "Practice did not fit
either alone. The one head that declared `covered_by` dropped it twice
because a few members fit no child and forcing a weak child tag was refused";
"nothing consumes the relation". The retired fan-out limit "was a guess and
nothing has shown the need" (ADR 090, Left open). One side benefit recorded
in the trace: adopting `covered_by` on learning-theory "caught a member the
natural-language `rg` recipe had missed" (block-style YAML tags).

**What the record does not say.**
- No count of how often connect or readers actually skip the by-tag search
  (recurrence of the saving is unmeasured).
- No measured invocation cost of the cross-artifact check (validator run
  time or added validation scope).
- No construction cost beyond elapsed timestamps; no line counts.
- No ongoing maintenance count (how many mark drops or fix-routed repairs
  occurred), apart from `covered_by` being dropped twice.
- Stability was not predicted in advance; ADR 026 states expected drift of
  `complete` but gives no expectation for `covered_by` other than deferral.

---

## Case 2. The artifact-run engine (ADR 113), retired by ADR 118

**Records.**
`kb/reference/proposals/archive/code-scheduled-workflows.md` (state "as of
2026-09-29");
`kb/reference/adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md`
(dated 2026-10-09, now superseded);
`kb/reference/adr/117-plans-derive-their-structural-jobs-from-the-type.md`
(2026-10-10);
`kb/reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md`
(accepted, 2026-10-19);
`kb/log.md` METHOD entries of 2026-10-09 and 2026-10-19;
`kb/work/conjecture-store/candidates.md`, candidate 2 (workshop).

**Before conversion.** "The analysis workflow's schedule was prose. The
coordinating agent read the skill, chose the next step, launched workers,
checked their outputs and carried values between steps in its own context"
(ADR 113, Context). The proposal: "The analysis skill is 518 lines. Its
schedule is prose" (code-scheduled-workflows, Current state).

**The routine (construction decision, ADR 113).** A generic engine,
`commonplace.artifactrun`, executing a plan file of jobs over a typed
directory artifact; "One command advances" (`commonplace-run advance`);
"Judgments are the one primitive"; "Coverage is engine-derived"; and a core
that "imports no consumer", so "A second consumer needs a plan, a type and
handlers, nothing in the engine." It replaced a first code scheduler of
2026-09-29 whose validator "read sibling members that were not declared
inputs".

**Construction reasons, as stated.** The batch 01 trace audit (2026-09-28)
"found what that costs: a step that failed under exit status zero followed by
validation of a stale report, workers guessing a contract filename, and
correction turns for a report that had already passed. When the conversation
ended, progress was recoverable only by reading files by hand" (ADR 113).
Also: "Harness-native code scheduling existed in one harness, inside a
sandbox that cannot run Commonplace commands."

**Recurrence.**
- One consumer: "The decision is tested with one consumer" (ADR 113).
- Runs: "76 engine runs were unfinished or unintegrated at retirement, 32 of
  them published in their worktree but not on `main`" (ADR 118, Considered
  alternatives). The total number of engine runs is not stated.
- Production evidence at adoption: "one production analysis: the Dynamic
  Cheatsheet run of 2026-10-09"; "one run does not establish production
  fitness" (ADR 113, Consequences).
- Life span: ADR 113 dated 2026-10-09; superseded 2026-10-19.

**Cost language.**
- Construction choice with cost stated: "**Core inside the analysis package,
  extracted later.** Cheaper up front and favoured by the expectation that
  harnesses will bring their own schedulers. Lost: a separate module can be
  tested without a model or the analysis package" (ADR 113).
- Bridge framing before construction: "Machinery that exists only because
  code cannot launch sub-agents should be as small as possible, because it is
  the part expected to be discarded" (code-scheduled-workflows, Expected end
  state).
- Per-job cost after construction: "Every check job still needs a handler,
  mostly a wrapper naming its role and partners" (ADR 113). ADR 117: "the
  agentic-system analysis, then needed a package of handlers beside a plan
  of 498 lines. Ten of its twenty-five jobs were check or apply jobs that
  restated what the layout already said"; "Every copy was a place for the
  generic logic to drift". After 117: "The analysis plan is 219 lines
  against 498".
- Retirement cost comparison: "The engine survey (2026-10-18) counted about
  3,000 lines serving that model against about 1,000 of domain logic that
  already took plain values" (ADR 118).
- Mechanism of the overhead: with several attempts open, "the shared run
  state needs rules for which round an attempt belongs to, inputs that
  change while it runs, results reported late or twice"; "The engine's
  readiness rules, attempt closing, hand-out validation, run lock and reset
  machinery existed to enforce them, and the operator's checks of a harness
  had to cover nested coordination" (ADR 118, Context).
- Migration cost on retirement: migrating the 76 runs "would mean reading
  engine records into the new cache for runs whose worktrees already hold
  working engine code; declined" (ADR 118).
- Run-time cost of the replacement against the engine: "11 attempts, 0
  corrections, no failed launch, 39:56 wall against the engine's 39:40 to
  46:52 on the same system" (ADR 118, Evidence); "one run per route"
  (`kb/log.md`, 2026-10-19).

**Stability and risk.**
- The engine was designed as a bridge under an unobserved expectation: "The
  design assumes that harnesses will adopt code scheduling of their own ...
  This is the operator's expectation, not an observed fact"
  (code-scheduled-workflows).
- Untested scope at adoption: "not been exercised with concurrent
  coordinators on one run, with composite members, or with a plan whose code
  jobs are declared out of dependency order" (ADR 113).
- What changed: "Every harness now has a headless mode that takes a prompt,
  runs a worker to completion without interaction and returns: `claude -p`,
  `codex exec` and `pi -p`" (ADR 118, Context; phase 0 dated 2026-10-18).
- Refuter as recorded in the workshop: "consistency machinery for open
  attempts exceeding the domain logic it serves" — "refuter met"
  (conjecture-store candidate 2).

**Outcome.** Retired. ADR 118 supersedes "the engine, its plan model, the
advance command, hand-outs, judgments, engine-derived coverage, the run-state
layout and the core/consumer boundary". Kept: "Role-scoped draft validation
(`commonplace-validate <draft> --artifact <dir> --role <role>`)". Rejected
alternative "Keep the engine, drive it from a headless loop": "the
parallelism machinery stays because the engine's state model assumes it."
ADR 118 also records "Declined requirements" that it declines "bindingly, so
that later robustness work does not restore the machinery", including "a
general scheduler or coverage state in the workflow". A fallback was held:
"if the script exceeded about 600 lines of control flow ... It did not".

**What the record does not say.**
- No construction effort for the engine in time or lines at build time; the
  3,000/1,000 figure is a retirement-time survey.
- No total run count or per-run saving attributable to the engine versus the
  prose schedule; the one same-model comparison (log, 2026-10-09) reports
  quality differences, not cost.
- No stated expected life span or reuse forecast for the "second consumer";
  none arrived in the record.
- Construction-time maintenance cost was not estimated; it appears only as
  ADR 117's handler and plan-size complaint one day after adoption.

---

## Case 3. Source-claim grounding promoted to `cp-skill-ground` (ADR 073, ADR 076)

Chosen over other promotions because it has a dated cohort record of
repeated use before promotion. It is a promotion from an instruction to a
skill, not directly from methodology notes; the notes-to-instruction-to-skill
path it follows is stated in `kb/theory/capability-placement-should-follow-autonomy-readiness.md`.

**Records.**
`kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md`
(2026-08-24, revised 2026-08-25);
`kb/reports/retained/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md`;
`kb/reference/adr/076-source-claim-grounding-is-a-promoted-skill.md`
(accepted, 2026-08-25);
`kb/reference/adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md`
(2026-08-25);
`kb/theory/capability-placement-should-follow-autonomy-readiness.md`.

**The promotion rule in the notes.** "1. Capture an operation in
notes/catalogues during exploration. 2. Turn the stable procedure into an
execution-oriented instruction in `kb/instructions/`. 3. Promote to skill
only after repeated successful autonomous execution"; "This sequence
prevents premature automation while avoiding AGENTS.md bloat"
(capability-placement note).

**Before conversion.** The grounding procedure "was a plain instruction
addressed by file path. Its only inbound routes were the stop-and-report
handoff inside `cp-skill-write` and `cp-skill-write-multistage`, ADR 073
itself, and the rollout workshop" (ADR 076, Context). Earlier, cohorts
01-10a used "a normalized claims ledger: each ingest entry held a
paraphrased claim, exact extracts, and authored scope, confidence, and
limitation fields" (retained report).

**The routine.** `cp-skill-ground`, "the single advertised entry for
deciding which quotes an ingest retains, and the only procedure that writes
an ingest's `## Quotes` section"; "Its body and result protocol ... are
unchanged from the instruction it replaces" (ADR 076). The independent check
is code: "`commonplace-validate` resolves every `Source extract (verbatim)`
against the name-paired snapshot".

**Recurrence.**
- Rollout cohorts 01-10b in 2026-08: 205 claim uses under the ledger and 59
  under quotes or snapshot (retained report, table).
- "In cohort 10b, six atomic recoveries appended 51 distinct verbatim source
  and location pairs"; a scan found "19 link occurrences carrying the
  `(snapshot required)` marker across seven of 68 frozen target notes"
  (retained report).
- ADR 076 cites this as readiness: "a bounded procedure that has already run
  repeatedly and autonomously — the rollout cohorts — is promotion-ready."
- Ongoing recurrence after ADR 078: writers invoke it whenever "a guarded
  source dependency's ingest exists and its Quotes are insufficient"
  (ADR 078). No count of later invocations was found.

**Trigger.** A misrouting on the promotion date: "an agent holding that
request matched the ingest skill, invoked it with a natural-language target,
and the skill selected quotes anchored to no claim. That happened on
2026-08-25 and forced the choice: one request had two advertised surfaces"
(ADR 076).

**Cost language.**
- Little explicit cost language in ADR 076. Promotion cost framed as
  footprint: "Promotion for explicit use carries no new mutation footprint,
  so it need not wait on that question."
- Retrieval/invocation: before promotion the writers' handoff "had to carry
  two literal routes, one for the source checkout and one for an installed
  project"; after, "a single route addressed by skill name".
- Per-use friction that motivated ADR 078: "A note whose source evidence was
  insufficient could not be finished in one run: the writer reported a skill
  call and the operator invoked it, then restarted the write."
- Checking cost is moved to code: "the agent that chose a passage never
  certifies its own transcription" (ADR 076).
- Note-level statement of why skills exist:
  "The skill exists because context is finite and expensive"
  (`kb/theory/skills-derive-from-methodology.md`).

**Stability and risk.**
- "promotion changes discovery and invocation, not the procedure itself"
  (ADR 076, citing the skills-are-instructions note).
- "Move retained evidence out of the ingest first ... Left open here: the
  skill's result protocol does not change if the append target later moves,
  so promoting now forecloses nothing" (ADR 076).
- Caveat on expected benefit: "on this harness a `context: fork` skill
  inherits the invoking conversation, so promotion does not by itself isolate
  source reading from target prose" (ADR 076).
- Cohort evidence is descriptive only: "The cohorts were successive and
  non-random ... The gap between 30.2% and 74.6% is descriptive, not a causal
  estimate" (retained report).

**Outcome.** Still in use and extended. ADR 078 (same day) made writers
invoke it automatically; ADR 081 lets a literature branch pass it a URL;
ADR 094 (2026-09-27) changed the quote form inside it. The skill is listed
as live (`kb/instructions/cp-skill-ground/SKILL.md`).

**What the record does not say.**
- No construction cost for the promotion (time, size of the skill change).
- No per-use saving measured for the skill surface versus the plain
  instruction; the cohort rates compare two grounding representations, not
  promotion.
- No maintenance cost of the skill as such; later amendments (078, 081, 094)
  are recorded as decisions without effort figures.
- No count of post-promotion invocations.
- Stability is asserted from repeated runs; no stated probability or
  condition for reversal.

---

## Case 4. Refusal to codify: `scripts/` cleanup and promotion stay judgment calls (ADR 040)

Chosen for the clearest stated reason with a count. It declines two
codifications: a scheduled cleanup sweep with expiry machinery, and a
mechanical promotion trigger.

**Record.**
`kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md`
(accepted, 2026-07-07); the norms as carried today in `scripts/README.md`
("Cleanup norm", "Promotion signal").

**The work and what stays interpreted.**
- Cleanup: "A script whose docstring says 'one-off' or 'temporary' is
  deleted by whoever finishes using it, in the same session or commit
  series" (ADR 040, Decision).
- Promotion: "A script graduates to a `commonplace-*` command when it has
  been invoked, unmodified in its core logic, across multiple unrelated
  sessions or triage passes — repetition with a stable interface ... This is
  a judgment call exercised periodically (e.g., at monthly triage), not a
  mechanical trigger."
- Declined routine: "No scheduled sweep or expiry-timestamp machinery is
  adopted".

**Stated reason.** "one stale file in six, over 15 months, is thin evidence
for anything heavier than an informal norm" (ADR 040, Decision). Context:
"one script self-described as 'one-off' sat unused and undeleted for months
— the only genuine evidence of drift, but real."

**Recurrence.** One observed drift instance in six scripts over 15 months
(Decision, above). The promotion signal itself is recurrence-based:
"repetition with a stable interface, the same signal spec mining uses
generally". One precedent promotion: ADR 014 "documents the one precedent
for a promotion out of `scripts/`, at subsystem scale".

**Cost language.**
- Accepted cost of not codifying: "The cleanup norm is informal and relies
  on the finishing agent remembering; if drift turns out to be worse than the
  one observed instance, a scheduled sweep is the escalation path, not
  adopted now" (ADR 040, Consequences, "Harder / accepted costs").
- "The promotion signal is a judgment call, not a mechanical trigger, so it
  depends on someone noticing recurrence rather than firing automatically."
- Retrieval surface chosen: "a one-line pointer in `AGENTS.md` (visible to
  every agent immediately) and the fuller norm/signal detail in
  `scripts/README.md`". (The current AGENTS.md pointer reads "Save reusable
  tooling in `scripts/` (see `scripts/README.md`)".)

**Stability and risk.** "A script whose interface is still changing hasn't
stabilized enough to promote, no matter how many times it's been touched."
Rests on `kb/theory/progressive-constraining-commits-only-after-patterns-stabilize.md`
as the reason the signal is "stabilization-across-uses rather than a
first-use or fixed-count trigger" (ADR 040, Relevant Notes).

**Outcome.** Still in force, unchanged: `scripts/README.md` carries both
norms in the ADR's wording. `scripts/` now holds 18 entries (17 files or
directories plus README, by directory listing on 2026-10-30). No record
found of the escalation (a scheduled sweep) being adopted, nor of a
promotion made under the signal.

**What the record does not say.**
- No construction or maintenance cost estimate for the declined sweep; the
  reason given is weak evidence of need, not cost of the machinery.
- No saving per use for either norm.
- No count of later stale scripts or of triage passes held, so whether the
  "monthly triage" occurred is unrecorded.
- No invocation cost of the judgment call (who notices, how often).

---

## Other candidates not developed

- **ADR 092, coded write-context assembler declined**
  (`kb/reference/adr/092-write-briefs-are-optional-sidecars-named-by-a-validated-pointer.md`):
  "It lost for now. There is one consumer"; brief lookup stays in skill
  prose; same ADR rejects brief-staleness tracking "under YAGNI. No evidence
  yet shows briefs drifting".
- **Claim identifiers and quote deduplication not earned**
  (`kb/reports/retained/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md`,
  ADR 073 V1): 264 claim uses with "no case that needed a stable claim
  identifier"; a refusal backed by a cohort count.
- **`covered_by` as its own case** (ADR 026 to ADR 090): a mark built ahead
  of its first case, adopted by one head, dropped twice, retired because
  "nothing consumes the relation" after a 6,800-session survey.
- **Cohort-scoped review ack deferred**
  (`kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md`,
  `kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md`):
  "deliberately deferred until a real type edit makes per-note acking
  painful" (038); "it stays deferred until a real edit makes per-note acking
  painful" (041).
- **ADR 014, scripts become the `llm-commonplace` package**
  (`kb/reference/adr/014-scripts-as-python-package-one-tree-model.md`,
  2026-04-08): the one recorded promotion out of `scripts/`; "The review
  system ... was the forcing function."
