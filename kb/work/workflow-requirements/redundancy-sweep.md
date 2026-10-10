# Redundancy sweep of the files changed on 2026-10-09 and 10

Four read-only scouts went over the 105 files the engine, compact-plan,
prompt-section, citation and naming work changed, each with its area, and
reported what is stated twice, dead, stale or contradictory. This page
keeps the findings with a home proposed for each; nothing is applied. The
engine scout confirmed every dead-code claim with a search over `src/` and
`tests/`.

The pattern across all four areas is the same: each change added its rule
in the new place and left the old statement standing. The fix is the same
everywhere too: one home per rule, named below, and the other copies cut.

## 1. Instructions and types (the heaviest)

Homes, applied to every row: the record grammar and answers grammar in the
records contract; execution obligations in the worker rules; the check
command and the return line in the prompt section; shape and materiality
in the member types; a job instruction keeps only what is stage-specific.
PS is `jobs-engine/prompt-section.md`, FWR is `follow-worker-rules.md`, RC
is `agentic-analysis-records.md`, T is `types/`.

| Where | Repeated | Home |
|---|---|---|
| PS:26-34, FWR:120-146, RC:79-83 | the answers protocol, one entry per blocker in order, empty file without refusal | grammar in RC, obligations in FWR, PS keeps the slot sentence |
| FWR:143-146, RC:82-83 | an identical output passes only when every answer is declined | RC |
| FWR:134-135, RC:74-77 | a corrected report keeps every declared record ID | RC |
| FWR:122-125, PS `[output-answers]`, plan `outputs` | which roles write answers; FWR says "record verification" | the plan; delete from FWR |
| PS:27-28, FWR:88-91, FWR:148-151 | repair findings against frozen evidence with the previous output as baseline | FWR |
| PS:36-40, FWR:177-186 | run the check and repair until it passes; a pass is form, not acceptance | command in PS, meaning in FWR |
| PS:41, FWR:152, FWR:225-226 | return one line naming the files, or problem | PS |
| PS:23-24, T verification:62-67, verify-reports:39-42 | blocker addressing, a defect in two reports is two blockers | verification type; PS points |
| FWR:19-35 against the engine's frame | read the instruction first, then batches, oversized files in ranges | the engine prints it; FWR keeps truncation guidance only |
| FWR:95-101 against the frame | worker-identity JSON rules | the engine prints it; FWR keeps the per-harness subsections |
| FWR:37-41, FWR:179-182, drive:25-29 | exit codes | FWR for workers, driver for coordinators, once each |
| declare-boundary:46, FWR:52, FWR:74-77 | the capture directory survives cleanup | FWR |
| declare-boundary:35-36, FWR:163-165, T boundary:82-84 | a Git source is the repository at the commit; inspected paths are coverage not an allowlist | boundary type |
| declare-boundary:26-30, T boundary:43-57 | what to trace for a memory system; exclusions name prevented conclusions | boundary type |
| declare-boundary:13-14, 49-50, T boundary:33 | source identity equals the line | type plus layout; one job mention |
| declare-boundary:39-45, T boundary:28-33 | frontmatter shape for reviewed-boundary and capture | boundary type |
| reconcile-records:18-32, T reconciliation:29-50, RC:62-77, 105-109 | supersession rules, stated three times | RC for rules, type for shape, job keeps "connect afresh" |
| analyse-memory:28-32, T memory-report:114-122 | integration issues, verbatim including "side-channel messages do not substitute" | memory type |
| map-memory-profile:17-26, verify-memory-profile:19-25, T memory-profile:77-99, RC:203 | what `known` needs; a positive witness is not completeness | profile type |
| map-memory-profile:29-32, verify-memory-profile:41-43, T memory-profile:240-241 | source reads only for a named ambiguity, logged | FWR as a non-analyst inspection rule |
| verify-memory-profile:38-40, T verification:73-76 | when a profile-value limit is admissible | verification type |
| verify-reports:31-37, verify-memory-profile:27-36, verify-synthesis:31-38, T verification:55-90, RC:234 | the materiality threshold, four times | verification type; jobs keep stage examples |
| verify-reports:12-13, verify-memory-profile:14-15, verify-synthesis:15-16, T verification:29-38 | "code has already checked what the type assigns to it", four times | verification type |
| verify-reports:15-20, verify-memory-profile:11-13, verify-synthesis:12-14 | judge answers and refusals afresh | FWR verifier paragraph |
| synthesize-analysis:16-25, verify-synthesis:22-29, T synthesis:38-51 | synthesis stance rules, near verbatim | synthesis type |
| synthesize-analysis:27-30, verify-synthesis:22-24, T synthesis:65-70 | Limitations carries every limit and unresolved conflict | synthesis type |
| synthesize-analysis:34-37, verify-synthesis:40-42, T synthesis:66 | a record fault becomes a limitation or problem | synthesis type; problem path in FWR |
| SKILL:127-138, drive:50-56; SKILL:166-169, drive:115-117 | inherited profile rule; old run directories rejected | the driver |

Jobs restating the type or the layout, now printed as lines: cites lists in
trace-runtime:32-33, analyse-memory:35-37, trace-epistemic:31-32,
reconcile-records:33; record prefixes in the three analyst jobs; input
lists in five jobs; the Blockers/Limits grammar in verify-reports:47-49;
the epistemic blocks in trace-epistemic:15-17; "the boundary type gives
its sections" in declare-boundary:54-55. All delete.

Procedure inside types: memory-profile:107-113 copies the verification
type's materiality rule; memory-report:28-31 and 124-133 carry the problem
path and the self-check meaning; epistemic:148-150 and memory-profile:97-99
say what deterministic checks establish. All move to FWR or the
verification type, or go.

Stale: "record verification" FWR:124; "the record verifier" T
reconciliation:13; RC:48-49 says the citing member's type names what it
may cite (the layout does); "hand-out" for prompt in FWR:2, 13, 16, 52, 76
and six job descriptions; "new-engine" in FWR:10 and three jobs; the
plan.yaml:12-15 comment omits the two new parameter lines; plan.yaml lists
the records contract both in `criteria.contracts` and under `files:` on
nine entries; history paragraphs in memory-profile:31-36 and
reconciliation:34-36; overview:31 and synthesis:67 describe the old order.
Within-file repeats: SKILL:17, 57-59, 99; FWR:63-68 and 208.

## 2. Engine code

| Where | Issue | Action |
|---|---|---|
| plan.py:26-29, handouts.py:80-81, 154-162 | prompt line names listed three times | build `prompt_line_names` from `HANDOUT_FIELDS` |
| handouts.py:149-213, engine.py:394, 413 | hand-out directory paths rebuilt in three places | `_close` takes them from `handout_for` |
| handouts.py:127, engine.py:221, 528 | attempt-id format three times | one helper in store.py |
| handouts.py:158 | literal `"absent"` beside `ABSENT_LINE` | use the constant |
| plan.py:34, run.py:587, store.py:195, cli/run.py:67 | `("accepted", "refused")` four times | import `OUTCOMES` |
| run.py:466, store.py:172 | two `ATTEMPT_FIELDS` with different meanings | rename one |
| compact.py:79-83, run.py:475-479 | type parsed into a layout twice with the same error | one public function |
| plan.py:93-98, handlers.py:128-130 | dotted-path import twice | one helper |
| handlers.py:202-208, checks.py:95, note_parser.section | `## Title` section regex three times | use `note_parser.section` |
| checks.py:128, cli/analysis.py:221 | raw sha256 beside `store.digest` | use `digest` |
| checks.py:38-40, engine.py:470 | manifest bytes built twice | one helper |
| eight sites | relation names split and joined ad hoc | two helpers in plan.py |
| engine.py:262-268 | refusal looked up again after `run.resolve` did | one Run method |
| engine.py:275-277, 570 | exhaustion check twice | `Run.exhausted` |
| engine.py five sites, `current_outputs` lacking it | "holds no run" guard | one helper |
| handlers.py:97, 305-306; engine.py:105, 119 | small repeats | one-liners |
| handlers.py:275-277, checks.py:133-144 | refusal body built twice | one builder |
| compact.py:71, 147, 154-155 against plan.py | invariants checked in the loader and again at load | `load_plan` is the authority |
| run.py:449-462 `Run.covered` | called only by tests | move to a test helper |
| engine.py:5, `__init__.py`:19, handlers.py:110, 134-136, plan.py:29, 211, 244, handouts.py:3, 120 | stale words: state.py, report, option, reasons, "hand-out field" against "frame line" | one-line each |

## 3. Analysis consumer code

| Where | Issue | Action |
|---|---|---|
| worktree.py:83-94 | `_frontmatter` defined twice | delete one |
| analyses.py:67-69, plan.py:18-21, records.py:452-457 | no caller in src | delete or move to tests |
| opening.py:59-60, 113-114, 130-135 | guards a retired parameter; writes command-path and capture-directory the plan already prints; re-validates what it just wrote | delete |
| systems_matrix.py v1 path | BACKCOMPAT for bare-ID profiles; the only v1 profile is archived under a dead type path; a third copy of the ID grammar | remove, condition met |
| publication.py:48-61, 174, 263, 322; worktree.py:133-149 | identity fields, producers and member paths hardcoded though the layout declares them | read the layout |
| boundary.py:14-32, publication.py:210-216 | run-id checked twice, plus draft validation | keep one |
| publication.py:203-205, declared_checks.py:29-31, 36-40 | acquisition-result check twice; source field parsed beside `handlers._source_field` | one helper each |
| opening.py:79-95, publication.py:84-104 | the same environment guards | one guard function |
| opening.py, worktree.py, publication.py | the 40-hex regex four times, the run-ID grammar six times | one module |
| rules.py:133, records.py:292-296, 386, 409-426 | syntax errors reported twice, duplicate declarations twice, duplicate SRC rows three times, out-of-artifact citations twice | member-local syntax in the member rule, resolution in the artifact rule |
| rules.py:318-354, handlers.py:211-233 | Blockers/Limits grammar and addressee check in both; roles and addressees hardcoded though `verifies` declares them | one grammar, addressees from the layout |
| verification.py:44 | prefix table repeats the types' `record-prefix` | use declarations over the snapshot |
| systems_matrix.py:400-449, rules.py:297-305 | profile citation scope computed twice, slightly differently | one function |
| directory_layout.py:69-86 | the phrase-to-repair map misfires on "duplicate field" and holds consumer phrases in a generic module | pass `repair=` at origin, delete the map |
| checks.py:72, engine.py:344-349 | run values built twice | one source |
| profile.py:1, 18, opening.py:82, rules.py:3-5, directory_layout.py:3-9 | stale "new-engine"; a garbled docstring; a docstring without `verifies` | one-line each |

## 4. Reference and workshop documents

The proposal `plans-without-structural-wrapper-code.md` is the worst file:
its Current state still describes the hand-written plan; it claims a
type with no rule validates as schema-only, which the code still refuses;
it says the verdict keeps its `verifies` field, which ADR 114 dropped; two
bullets are both titled Extensions; the criteria text says the records
contract is in the set type while the ordering says it is not; the plan's
length is 237 in one place and 219 in another; the key is `handout:` where
it is `prompt-section`; the Ordering bullet repeats step 5; and each step's
done note appears in both the sequence and the criteria, with the toy-prompt
criterion contradicting itself. All of this is one rewrite, best done as
the conversion to an ADR.

Three statements live in three or four places: the directory-artifact
definition against the validation contract against ADR 111 (home: the
definition; the contract keeps checks); the verification protocol in the
workshop write-up, the proposal and ADR 114 (home: the proposal now, the
ADR later; ADR 114 keeps the invariant); `verifies` semantics and the
layout rendering in the workshop against the type and ADR 114 (home: the
type and the ADR).

Amendment lines missing: ADR 111 for `required: when`, the `[set]` marker
and "verifications are not members"; ADR 113 for `inspect`, the compact
plan and the deleted check handlers; ADR 114 for the role rename and the
loader built. The glossary still says "set", uses *invocation*, omits
`verifies` from its relation kinds and defines coverage against ADR 114;
`reads` is a retired word the compact plan reintroduced and should be
recorded as the exception. commands.md says "published set" and
"handouts". The conformance proposal's current state is dated 2026-10-01
and names the deleted sources contract.

Workshop files that can close with nothing lost: the implementation
review, the job-set mapping, the verification write-up (its one-cycle
walk-through is illustrative), the layout rendering, the naming review
once the drift-test decisions are in the test's docstring, and the API
design with its sketch. Keep: consumer-surface (its measurements are
nowhere else), the notes sweep (open opportunities), scenarios (until
encoded as tests), requirements (decisions ADR 113 lacks), and the
glossary, which becomes the reference page.

## Order

1. The proposal's rewrite, as its conversion to an ADR, and the amendment
   lines; one session, one day.
2. The instructions and types, under the homes above; this is the one
   workers read, so it goes before the production run.
3. The consumer code, starting with the duplicated findings and the v1
   path.
4. The engine code, all small.
5. Workshop closure, after the ADR.
