# Workshop: offload analyse-agentic-system mechanics into code

- **Posed:** 2026-09-28, by the operator's direction after a review of the skill.
- **Start condition:** met on 2026-09-29, when the operator reported the batch finished.
- **Decision 2026-09-29 (operator):** fix all of the issues first, then rerun once. The rerun is therefore one bundled method change, not a sequence of separately comparable ones. The operator wants to compare its results with the batch 01 rerun, so the comparison will not isolate which change caused which difference. Freeze the method commit before opening the rerun.
- **Decision 2026-09-29 (operator), second:** build the code orchestrator first and hang the remaining items on it. The design is `kb/reference/proposals/code-scheduled-workflows.md`. This takes option A of that proposal's choice 3: the rerun tests the code orchestrator together with the backlog. See "Build on the code orchestrator" below.
- **Decision 2026-09-29 (operator), third:** the code orchestrator is a module separate from the analysis code, so that it can be tested on its own. This takes option A of the proposal's choice 2.
- **Decision 2026-09-29 (operator), fourth:** three points of the proposal are settled. Error recovery takes option B of choice 1: one retry by code that carries the validator's message, then a blocked outcome that the agent orchestrator repairs. The repair scope is conditions and removal of a bad output; the agent orchestrator does not write or edit the content of a job's output. The agent orchestrator reports listed events only: a failed launch, a repair, a stop.
- **Closes when:** each item below is implemented, or explicitly dropped, and one analysis run completes through the code orchestrator, with `kb/instructions/analyse-agentic-system/SKILL.md` reduced to what the workflow adds to the agent orchestrator's loop (`drive-a-code-scheduled-run.md` in the same directory, which the skill then loads) and the judgment content moved into job prompts. Then extract any durable decisions to `kb/reference/` and delete this workshop.

## Goal

The [worker information map](./worker-information-map.md) owns the
2026-10-01 reorganization of shared contracts and required worker reads.

Implemented: [separate reconciliation from synthesis](../../reference/adr/098-separate-analysis-reconciliation-from-synthesis.md)
(2026-10-01) writes public synthesis after record verification and makes
reconciliation a fifth set member. The two previous retained sets are archived.
Both fresh Luna trials stopped before synthesis; see
[trial observations](./split-luna-trials.md). Three subsequent Sol medium
runs reached verified synthesis and one published. Their
[results and trace audit](./three-run-audit-2026-10-01.md) retain the shared
publication collision and remaining semantic comparison defects.

Planned, not started: [role-specific contract packets and code-owned form](./role-specific-packets-and-code-owned-form.md)
(2026-10-01) delivers each job only the contract sections its role needs
and moves output form into a filled skeleton and validator messages. Its
skeleton step reopens the scaffold item under "Decided against" and waits
for the operator's confirmation.

Draft for review: [analyst intent paragraphs](./analyst-intent-paragraphs.md)
state each analyst's purpose and consequential errors. They are proposed
additions to the balanced compaction candidates; live instructions are unchanged.

Implemented: [Parameterized analyst instructions and direct launch delivery](./parameterized-analyst-invocations.md) (2026-09-30) removes forwarding layers, has code write every path a worker needs into its saved invocation, and has the orchestrator send that invocation as the worker's message. Its acceptance checks and two commissioned Luna trials are complete; the broader backlog below remains open.

`SKILL.md` is about 526 lines. Much of that length is protocol mechanics written as prose for the agent to carry out by hand (allocate IDs, record HEAD, map IDs, recompute hashes, check truncation, keep exit statuses) and prose guards for failure modes. Move the mechanical and checkable parts into `commonplace-*` commands, validators, and hooks. The agent keeps the judgment work: boundary and target classification, forcing-case selection, route and guarantee judgments, conclusion-status assignment, semantic verification, and synthesis.

## Not verified yet

The review that produced this list read only `SKILL.md`. Before building each item, read the relevant type spec, schema, and `src/commonplace/lib/agentic_publication.py` and `src/commonplace/cli/agentic_analysis_publication.py`, and check whether the code already does it. Some items may already exist in part.

## Items, in proposed order

Tier 1 — mechanical, low risk:

1. **`open` command.** Allocate the run ID, write run-state from the template, record HEAD. Run the publication worktree-clean and editable-install-equals-`inputs-commit` checks now, not at publication. Run `inspect-destination` and store `expected_incumbent_sha256` in run-state instead of in `## Run` prose. Optionally print the deterministic frontmatter block (type, run, source, `inputs-commit`, system name) for the agent to paste.
2. **`finalize-memory` command.** Applies the Reconciliation table to `memory-report.md`: exact-token ID mapping, `On <ID>` heading rewrites for shared records, removal of rejected proposals, `finalized-from`, and `## Amendments`. It refuses and returns the report to the specialist when a finding still depends on a rejected proposal.
3. **`manifest build`.** Write `ARTIFACT.yaml` from the files in `output/`, with type line and hashes.
4. **Register allocator and mapper.** `register alloc <PREFIX>` returns the next unused monotonic ID. `register map` replaces exact tokens and verifies every mapped target is declared and unique.
5. **Generated-review renderer.** The compact review is a projection of the validated set. Code fills the frontmatter (`analysis-run`, `source-identity`, `reviewed-revision`, artifact path and hash) and renders sections from overview fields. The agent writes at most a short summary. Largest single reduction in agent work; check the generated-review type first to see how much of the body is derivable.

Tier 2 — replace prose guards with code guards:

6. **Read command with quotes built in.** Commit-addressed read of a path and range; reports size and truncation as an exit status; emits the `commonplace-quote` block for the same selection; enforces a byte budget for batched reads.
7. **Probe runner.** `commonplace-probe run -- <cmd>` checks the execution preflight, captures status, stderr, stdout, and hashes, and emits a `SRC-*` probe capsule.
8. **Deny hook for prior-analysis exposure.** Block reads of `kb/agentic-systems/reviews/` and `kb/reports/retained/agentic-system-analysis/` for the coordinator and its workers, so the exposure rule and the "never inspect incumbent prose" paragraph become enforcement, not instruction.
9. **Schema-required completeness.** Require the RTE read-back fields and CMP fixity fields, each filled or marked `uninspected`/`inapplicable` with a reason, so most of the Verify list becomes `commonplace-validate --full`.
10. **Cross-member checks in `--full`.** The structural parts of the memory-comparison checks (scope agreement with canonical records, trace-fed writes including compaction, push-signal consumer and selector, amendments and annotations on the same IDs). Whether the scope is right stays with the agent.

10a. **Fail-fast command wrapper.** Run multi-step reads and edits so that any failed step fails the whole call: `check=True` semantics, pipefail, and a nonzero aggregate exit when a discovery loop skips a missing path. Motivating case: in the batch 01 rerun a Python excerpt-assembly step raised `ValueError` under an outer exit status of zero, and the shell went on to validate the old report (MM 160). Two more zero-status failures came from `git show ... | sed` without pipefail (B 142) and a read loop that printed stderr and continued (BM 99). The skill already states the rule; the prose did not prevent it. Belongs beside item 6.

Tier 3 — code proposes, the agent decides (lower priority):

11. **Seed scanners over the frozen commit.** Entry points, model and provider references (CMP seeds), alternate paths (subprocess, shell, provider-native tools, callbacks), prompt files, and a file-layer classification for the SRC register. Each emits candidates with quote blocks and a search-boundary receipt (patterns plus tree) that can support a load-bearing `ABS-*` claim. Output must say it is a seed list, not coverage, to limit anchoring.
12. **`memory-input.md` generator.** Assemble the frozen input from run-state and the overview draft, and hash it. The input is frozen, so the agent does not edit it.
13. **`publish` runs `prepare` internally; `status` command.** `status <run>` derives the phase and the next allowed action from files and hashes. It must not store a phase ledger, which the skill forbids.
14. **Comparison staleness in the handoff.** Compute which `kb/agentic-systems/comparisons/` outputs a changed review makes stale.

## Decided against

- **Scaffold command for the four members.** It would have to emit empty sections. Those either fail validation or need a placeholder convention, and a placeholder that passes validation records a section as present when nothing was analysed. The validator's missing-section errors already serve as the checklist. The useful part, deterministic frontmatter, is covered by item 1's printed block or a validator cross-check of member frontmatter against run-state.

## Contract decisions (2026-09-29, operator)

Read as: item 1 takes option A of its proposal (a run-state field for the incumbent digest, fixed when `open` runs; `prepare` and `publish` read it and the `--expected-incumbent-sha256` flag goes away). Item 9 takes option D of its proposal (a labelled-line presence rule in code plus an assay for adequacy). Proposals: `kb/reference/proposals/open-an-analysis-run-in-code.md` and `kb/reference/proposals/required-route-fields-as-labelled-record-lines.md`. The item 9 label vocabulary is still to be chosen and measured across the retained sets on the target branch before the rule ships. When each ships, the proposal becomes an ADR and archives.

## Survey of existing code (2026-09-29)

A read-only survey by a subagent compared the backlog with the code. I have not re-checked its file:line evidence; verify each before building.

- **Item 1 (`open`): partial.** The worktree-clean, method-unchanged and running-package checks exist as functions in `src/commonplace/lib/agentic_publication.py` but run only at inspect, prepare and publish. Nothing allocates run IDs, writes run-state or records HEAD. `inspect-destination` prints JSON and stores nothing. Storing the incumbent digest needs a new run-state schema field, which is a contract change and needs a proposal; the alternative is for `prepare` and `publish` to re-run inspection themselves and drop the `--expected-incumbent-sha256` flag.
- **Items 2 and 3 (`finalize-memory`, `manifest build`): absent in `src/`, prototyped in tests.** `finalized_member_text` and `repin` in `tests/commonplace/lib/test_agentic_analysis.py` do the mapping, the `On <ID>` rewrite, `finalized-from`, `Amendments`, and hash pinning. Publication checks `finalized-from` by hash only, not by re-deriving. The Reconciliation table has a fixed parseable format that no code parses. Plan: promote the helpers into `lib`, merge item 3 into item 2's command family, and have item 2 parse the Reconciliation table instead of taking a separate mapping.
- **Item 4 (register alloc and map): mostly redundant.** Once item 2 parses the table, `register map` is not needed. `register alloc` is small enough to fold into `open` or drop.
- **Item 5 (review renderer): much smaller than assumed.** Only the frontmatter, the H1 and an Evidence-basis line are derivable. The generated-review type requires little beyond those, and the body is authored prose. Rescope to frontmatter plus an evidence-basis stub, unless the type is changed to a derivable body.
- **Item 6 (read command): partial.** `commonplace-quote` covers the quote half. The new work is the commit-addressed read with size, truncation status and byte budget. Keep together with 10a.
- **Item 9 (schema completeness): needs a contract change.** The RTE read-back and CMP fixity fields are prose inside record bodies with no structured form, so a JSON schema cannot require them. It needs a record-body line convention plus a Python rule, and a proposal.
- **Item 10 (cross-member checks): partial.** Identity, declaration uniqueness, reference resolution and comparison references are checked. Scope agreement, trace-fed writes, push consumer and selector, and same-ID amendments and annotations are not.
- **Item 13: `publish` already runs the full prepare check.** Drop that half. A `status` command is optional.
- **Item 14: dropped.** `kb/agentic-systems/comparisons/` holds only a README, and the matrix is rebuilt from all reviews, so any review change makes all of it stale. One sentence in the skill covers it.
- **Items 7, 8, 10a, 11, 12: absent.** Genuinely new; nothing to reuse except the existing hash check for item 12.

## Build on the code orchestrator (2026-09-29)

In the proposal's model a program runs the workflow, keeps run state on disk, and stops only where it needs a sub-agent. The agent orchestrator runs `step`, launches the jobs it names, and runs `step` again. A job is one delegation to a sub-agent; a mechanical step is executed by code inside `step`.

Where each remaining item lands:

| Item | Lands as | What changes |
|---|---|---|
| 1 `open` | The command that starts a run. The agent orchestrator runs it once with the invocation's arguments; `step` takes the run from there | Becomes the entry point of the workflow |
| 2, 3 finalize, manifest (shipped) | Mechanical steps the definition calls | The agent no longer calls them |
| 5 review renderer | Mechanical step for the frontmatter and evidence-basis stub; the body is a job | — |
| 6 read command, 7 probe runner, 10a fail-fast wrapper | Tools that workers use inside jobs, named in job prompts | Independent of the code orchestrator. 10a is not needed for mechanical steps, which run as Python and raise; it is still needed where a worker runs shell commands |
| 8 deny hook | Per-job tool scope, emitted by `step` as launch parameters and enforced by the hook | The agent orchestrator holds no analysis content, so the guard is needed for workers only |
| 9 route-field completeness, 10 cross-member checks | Validators that `step` runs when it accepts an output | A failed check becomes a retry that carries the validator's message, not a correction turn |
| 11 seed scanners | Mechanical steps whose outputs are declared inputs of jobs | Priority unchanged |
| 12 `memory-input.md` generator | Input assembly for the memory specialist job | Moves from tier 3 to required. Every judgment job needs the same: a generated prompt and declared inputs |
| 13 `status` | Subsumed: `step` derives the next action from files | Dropped as a separate item |

Build order, depth-first:

1. The core: `step`, `report`, asynchronous `agent()` with wait, and input-matched acceptance. It is its own module and does not import analysis code. It is built and tested in its own workshop, [code-scheduled-workflows](../code-scheduled-workflows/README.md).
2. A coarse first analysis definition: `open`, one job per skill step that needs judgment, the shipped commands as mechanical steps, publication last. Each job prompt starts from the skill section it replaces. The definition must include the two lenses as parallel jobs, reconciliation, and a correction cycle, because those are the cases that show how much machinery the runner needs. The goal is one complete run through `step`. The core's interface stays open to change until this definition has used it.
3. Hang the items above on that run, in the order its failures suggest.
4. Split coarse jobs only where a run shows that a job's context is too large or its inputs are unclear.

### Job split of the first definition (2026-09-29)

The definition is `commonplace.lib.agentic_workflow:AnalyseAgenticSystem`. The run directory is the analysis run directory, `kb/reports/state/agentic-system-analysis/<run-id>/`; the core keeps its state in `workflow-state/` inside it, and the run ID is the directory's name. Each job's task is an instruction file in `kb/instructions/analyse-agentic-system/jobs/`, cut from the skill section it replaces; the file is a declared input, so a method change reopens the jobs that follow it. Every file below is relative to the run directory.

| Order | Name | Kind | Reads | Writes | Replaces |
|---|---|---|---|---|---|
| 1 | `open` | effect | parameters | `opening.json` (method commit, run date, review path, incumbent digest), `run-state.md` | step 1.1–1.3 |
| 2 | `boundary` | job | `opening.json` | `boundary.md`: disposition, target class, boundary kind, reviewed boundary, cutoff, evidence tier and source in frontmatter; the Boundary and evidence and Source register sections | steps 1.4–1.5, 2 |
| 3 | run-state source | mechanical | `boundary.md` | `run-state.md` | step 2.4 |
| 4 | `runtime` | job | `boundary.md` | `output/runtime.md` | steps 3, 4 |
| 5 | `scoping` | job | `boundary.md`, `output/runtime.md` | `scoping.md`: both lens scoping records | step 5, first paragraph |
| 6 | memory input | mechanical | the above | `memory-input.md` (item 12) | step 5, frozen input |
| 7 | `memory` and `epistemic` | two jobs in parallel | `memory-input.md`; boundary, runtime and scoping | `memory-report-0.md`; `epistemic-draft.md` | step 5 |
| 8 | `reconcile-<n>` | job | the lens results of round `n` | `reconcile-<n>.md`: Reconciliation, Bounded synthesis, Limitations, and any return to the specialist | step 6 |
| 9 | `memory-<n>` | job, only after a return | `memory-input.md`, the last report, the return | `memory-report-<n>.md` | step 6, correction |
| 10 | `epistemic-final` | job | `epistemic-draft.md`, the last reconciliation | `output/epistemic.md` with canonical IDs | step 5, remap |
| 11 | set assembly | mechanical | all of the above | `memory-report.md` (the last round), `output/overview.md` without semantic verification, `output/memory.md` (finalize) | step 7.1–7.4 |
| 12 | `verify` | job | the assembled set | `verification.md` | step 7, Semantic verification |
| 13 | final assembly | mechanical | `verification.md` | `output/overview.md`, `output/ARTIFACT.yaml`; `--full` validation | step 7 |
| 14 | `review` | job | the set | `review-body.md` | step 8.1, body |
| 15 | review candidate | mechanical | `review-body.md`, `ARTIFACT.yaml` | `review-candidate.md` with its frontmatter (item 5) | step 8.1, frontmatter |
| 16 | `publish` | effect | the candidate and the set | the public review, the retained set, the complete run state | step 8.2–8.3 |

- A `blocked` or `out-of-scope` boundary skips 4 to 15: code assembles an overview-only set from `boundary.md`, with the sections that were not reached saying so, and completes the run state without publication.
- The correction cycle: a reconciliation that returns findings to the specialist hands out `memory-<n+1>` and then `reconcile-<n+1>`. After two returns the run goes on with the last report and the reconciliation records the unresolved conflict as uncertainty.
- Validators carry the checks that were prose: the member type's validation for each member, the finalization of the memory report against the reconciliation's table (a refusal is a retry of the reconciliation that carries the refusal), and the frontmatter values of `boundary.md` against the overview schema's enumerations.
- The judging norms of step 3 are one shared file, `jobs/judging-norms.md`, declared as an input of every job that judges evidence.
- Not in the definition: the transfer scan (step 9) and the handoff (step 10), which the skill runs after `done`.
- Revised after the first real run (2026-09-29). `runtime` writes `runtime-draft.md`. Each reconciliation round `r` that returns nothing closes with `runtime-final-r` (declares the records the reconciliation registered, retains their passages, applies amendments), a code-finalized `memory-final-r.md`, `epistemic-final-r`, a code set check (`set-check-r.md`: the members copied into `output/`, the manifest built, `--full` validation), and `verify-r`. A verification that names blockers, the set check's failures among them, starts reconciliation round `r+1` with the verification, the set check and round `r`'s members as inputs; the bound on rounds covers returns to the specialist and blockers together, and blockers in the last round stop the run. Each job has a private `scratch/<job>/` directory.

Main risk: today one coordinator context carries its reading of the sources from step 2 to step 7. Fresh workers do not share that reading. Each job either reads the sources again or receives what it needs as files, so token cost rises and analysis quality may change. The rerun comparison cannot separate this effect from the others.

The proposal's choices 1, 2 and 3 are decided above. Its free choices are left to the build.

## Evidence from real runs

The batch 01 rerun trace audit (2026-09-28) is in the `commonplace-refresh-batch-01-rerun` worktree at `kb/work/agentic-memory-refresh/batch-01-rerun-trace-audit-2026-09-28.md`; it is not on main yet, so cite it by path and date until it lands. It covers three published sets and six worker traces (476 tool outputs). What it shows for this backlog:

- **Item 2 (`finalize-memory`).** The audit rebuilt all three memory members from their local reports by exact-token mapping, merged-heading conversion, provenance hash and appended Amendments, with no substantive parent rewrite. Proposals mapped: 26, 19 and 34. Eight merged records exercised the `On <ID>` rule. No proposal was rejected, so the rejected-proposal refusal path has no real-run evidence yet.
- **Item 6 (read command).** 17 worker tool-output deliveries and 2 batch-coordinator deliveries were truncated. Raising the token budget on the nested shell call did not raise the outer wrapper's limit, although the skill already tells agents to check truncation at both levels.
- **Item 8 (deny and write guard).** The audit found no worker agent-listing call and no prior-review read, but only by scanning every tool output by hand. It also found one write outside the assigned worktree (`cat AGENTS.md >/tmp/...`), later deleted. A path-scoped guard would make both checks automatic.
- **Item 9 (schema-required completeness).** One specialist report passed validation and still needed two correction turns for heterogeneous objects, missing route read-back fields, and irregular kind headings and IDs.
- **Item 10a (fail-fast wrapper).** Three of six recovered worker command errors ran under an outer exit status of zero, so a grep for nonzero exits undercounts them.
- **Item 12 (input generator).** Specialists never loaded the runtime type whose route fields the final review applies, and two guessed a wrong contract filename. Embedding or linking the runtime-type route fields in the frozen input would remove the dependence on the specialist following links. The audit also proposes an instruction fix; the two are complementary.

The audit's other proposals (separating report content from execution accounting, keeping structural and semantic acceptance apart, stating that the runtime supplies doctrine and model identity, and allowing scratch selections inside the run) are instruction changes owned by that session's method follow-up, not part of this backlog.

## Constraints and risks

Further candidates are mapped in [Simplifications beyond mechanical offloading](./simplification-candidates.md), recorded at the operator's request on 2026-09-29. They are proposals for consideration, not adopted implementation work or additional closure requirements.

- **Contract drift.** Tools that embed section headings or the `METHOD_PATHS` list can drift from the type specs. Generate from the schemas and the existing constant instead of copying them.
- **Method paths.** Every new command widens what must be committed before a run opens, because publication requires the package source to equal `inputs-commit`. Land these changes between batches, not during one.
- **YAGNI.** If an item turns out not to be needed, drop it here; write a design proposal in `kb/reference/proposals/` for any item that changes a shipped contract before implementing it.
- **Output contracts:** the [analysis set type](../../agentic-systems/types/agentic-system-analysis-set.md) and collection-owned member types govern the current output. The output-documents workshop is closed; its [acceptance record](../../reports/retained/agentic-analysis-output-documents-20261002/README.md) retains the design trials and their limits. [analyse-agentic-system](../analyse-agentic-system/README.md) holds the skill's construction history.

## Log

- 2026-09-29: the first definition is built: `src/commonplace/lib/agentic_workflow.py`, eleven job instructions in `kb/instructions/analyse-agentic-system/jobs/` cut from the skill's steps, and `SKILL.md` reduced to opening the run, the loop instruction, and the report. Item 12 (memory input generator) and the frontmatter half of item 5 are mechanical steps of the definition; items 2 and 3 run as mechanical steps; the finalization check is the reconciliation's validator. Scripted-worker tests (`tests/commonplace/lib/test_agentic_workflow.py`) take a complete run through publication, the out-of-scope branch, the correction cycle, validator refusals, and a verification blocker; they found two defects (the repository root was one level short, and the boundary validator accepted unquoted dates), both fixed. Not yet shown: any run with real workers. Dropped from the skill without a replacement: the rule to commission a fresh specialist when a correctable `blocked` report comes back; a blocked report now stops the run at set validation. Next: one real run through `step`, then hang the remaining items on what it shows.
- 2026-09-29: the first real run (`AAS-2026-09-29-instinctual-memory-01`, Claude Code) stopped at set validation: 10 records the epistemic lens proposed were declared nowhere. A trace audit found the stop hid four verify blockers, one a content error in a reconciliation amendment, and smaller gaps: dangling "see Returns" anchors, a member job that had to check a file written after it, no home for last-round passages, absence records without a searched boundary, a missing previous-round input, undefined lens-depth triggers, a shared scratch directory, `commonplace-quote` refusing absolute run-state paths, and three prior-analysis folders missing from the forbidden list. All are fixed; blockers now start a reconciliation round (operator decision). Cost of the run: about 28.7M input tokens, mostly cache reads, 37 minutes; runtime, memory-0 and verify each re-read the same core files. The run is marked failed. Next: a second real run.
- 2026-09-29: ADR 096 removes the failure class behind the first run's stop: each pass declares its own records under a canonical lens prefix (`MEM-`, `EPI-`), no step renames IDs, and amendments live in the overview's Reconciliation. Memory finalization, the mapping table, `runtime-final` and `epistemic-final` are gone; the memory member is the specialist's report byte for byte. The one old-grammar retained set (pageindex) and its generated review were deleted rather than migrated. Next: a second real run, which is also ADR 096's adoption test.
- 2026-09-29: ADR 097 lands the operator's selection from the simplification candidates (Decisions 1, 2, 3, 5 and 6): no scoping job, no memory handoff or its three frontmatter fields, the public review rendered by code from the verified overview with a reconciliation-authored description, one normalized source identity, and Blockers as exactly `none` or a list. Correction routing (Decision 7) waits for the second real run, which now tests ADR 096 and ADR 097 together.
- 2026-09-30: fact checks of the PageIndex and instinctual-memory reviews found no claim the source contradicts, but dropped route scope, caller workflow written as code, a whole route (`mem tidy`) missing from one run, and set-internal references in the public text. The planned fixes (an entry-point inventory, a Bounded synthesis template, and verify checks on the public text) are in [Review accuracy fixes](./review-accuracy-fixes.md), to land after run `AAS-2026-09-30-instinctual-memory-03` finishes.
- 2026-09-30: analyst trials (runtime analyst on frozen inputs, by model) and fresh-eyes audits of what each analyst can understand from the files it is given are recorded in [Analyst instruction audit](./analyst-instruction-audit.md). Part of the runtime findings is fixed (`ae70fe59`); the rest is parked until the command-redirection work lands.

- 2026-09-30: parameterized analyst invocations are implemented in `eeeb60af`–`4e4f4013`, including the generic delivery rule, complete-message engine flag, all six jobs, merged memory and epistemic methods, and dependency-based trial hashing. All 1,181 Python tests passed. Two fresh Luna trials on copied inputs from `AAS-2026-09-30-instinctual-memory-02` produced memory and epistemic reports accepted on their first final submission by the workflow validators; all seven output quotations verified, and input hashes stayed unchanged. Full details and the limits of these checks are in the [implementation record](./parameterized-analyst-invocations.md#implementation-and-verification-2026-09-30).

- 2026-09-30: the operator commissioned a [trace audit of the Luna trials](./parameterized-luna-trace-audit.md). It found six truncated tool deliveries with incomplete recovery, inner command/status loss, an internally repaired quote-selection failure and 15 schema failures, a stale validation line, unflagged record overlaps, missing tidy evaluation coverage, and epistemic ledger defects. No forbidden prior-analysis read or out-of-scope write was observed. The earlier structural and quotation passes remain valid, but do not establish clean execution or semantic completeness. Reports were preserved.
