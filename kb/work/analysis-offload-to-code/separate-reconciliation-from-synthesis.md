# Plan: separate reconciliation from synthesis, and make reconciliation a set member

- **Commissioned:** 2026-10-01, by the operator, after a discussion of how to reduce what each analysis worker reads and writes. The operator also decided that the retained sets are replaced by new runs under the changed method; the present sets are not migrated.
- **Status:** method implemented in `0ad34f5d`; both fresh Luna runs stopped at final record verification, before synthesis. Publication acceptance remains pending. See [trial observations](./split-luna-trials.md). The archive prerequisite landed in `b2b0fb04`, contracts in `5154fac6`, and job instructions in `0165fb18`.
- **Purpose:** the public synthesis is written once, on records that have already been reconciled and verified, by a job that reads only what a synthesis needs. Reconciliation becomes its own report, so each job reads and writes one type.
- **Not in scope:** field removal, conditional lenses, record indexes, the [contract packets plan](./role-specific-packets-and-code-owned-form.md), and any change to the runtime, memory and epistemic jobs beyond wording that names where amendments live.

## Evidence for the change

In run `AAS-2026-09-30-instinctual-memory-03` (run state on disk, not retained), reconciliation ran three times. Section sizes in bytes:

| Section | Round 0 | Round 1 | Round 2 |
|---|---:|---:|---:|
| Reconciliation | 3,314 | 4,073 | 6,406 |
| Bounded synthesis | 4,695 | 4,708 | 4,775 |
| Limitations | 3,087 | 2,719 | 2,766 |

Only the Reconciliation changed materially. The round 1 verification blockers that were read concerned records and the memory profile, not the synthesis. The public text was drafted before the memory correction and before any verification, then carried through two more rounds.

This is one run. It shows the pattern; it does not establish how often rounds repeat.

## Roles after the change

Reconciliation and verification read almost the same material, and differ in role:

- **Reconciliation is an author.** It resolves disagreements between the three members by writing amendments, supersessions and retained conflicts, and it may return findings to the memory analyst.
- **Verification is an independent judge.** It writes no correction. It lists blockers, and code uses that list to schedule another round or stop the run.

The split adds a third role and a second judge:

- **Synthesis is the public author.** It writes the Description, Bounded synthesis and Limitations from settled records.
- **Synthesis verification** judges that text against the records it cites.

## Target design

### Jobs and order

1. `reconcile-<n>` writes the reconciliation, and optionally the findings returned to the memory analyst. The return route and the round budget (`correction_rounds = 2`) stay as they are.
2. `verify-<n>` judges the records: the memory profile against the records of the whole set, amendments and supersessions against the records they name, scope agreement, and the structural check's failures. Its blockers start another reconcile round, as today.
3. `synthesize` runs once, after a `verify-<n>` reports no blockers. It writes Description, Bounded synthesis and Limitations.
4. `verify-synthesis` checks that each synthesis statement is supported by the records it cites, that the text reads without the members' context, and that every conflict the reconciliation left unresolved appears as a limitation. Its blockers return to `synthesize`, for one correction round.

A record fault found by `verify-synthesis` does not reopen reconciliation. The synthesizer states it as a limitation, as the method already does for faults in the runtime and epistemic members. If the last synthesis verification still names blockers, the run stops, as the last record verification does today.

### The set

A complete set has five members: `overview.md`, `runtime.md`, `memory.md`, `epistemic.md` and `reconciliation.md`.

- **`reconciliation.md`** has its own type. Its body is what the overview's Reconciliation section holds today. Code writes its frontmatter and renders the member from the accepted `reconcile-<n>` output, so a `Returned to the memory analyst` section never enters the set.
- **`overview.md`** keeps Boundary and evidence, Source register, Bounded synthesis, Limitations, and Verification and blockers. It loses the Reconciliation section. Under Verification it carries the record verification and the synthesis verification as separate subsections.
- **Amended records.** The overview carries a code-written line listing the IDs the reconciliation amends or supersedes, with a link to the member. A reader who resolves a record through the overview then sees that an amendment exists.
- **Blocked and out-of-scope runs** keep an overview-only set. The `Not reached` placeholder under Reconciliation goes away with the section.

The public review is unchanged: code renders it from the overview's description, synthesis and limitations.

### What each new job reads

| Job | Contracts | Run inputs |
|---|---|---|
| `reconcile-<n>` | Source and record contracts, the three member types, the reconciliation type | Boundary, three members, and prior round files as today |
| `verify-<n>` | Source and record contracts, the three member types, the reconciliation type | Boundary, three members, the round's reconciliation, the structural check |
| `synthesize` | Source and record contracts, the overview type | Boundary, three members, the reconciliation |
| `verify-synthesis` | Source and record contracts, the overview type | The synthesis, boundary, three members, the reconciliation |

Neither reconcile nor record verification receives the overview type. The two synthesis jobs do not receive the three member types (about 35,000 bytes). That second choice is a bet: the synthesizer reads the members for their findings, and the record contract supplies statuses and field meanings, but controlled values such as the memory axes are defined only in the member types. The trial tests it; see "Stop and escalate".

Reconciliation's reading does not shrink much. The gain there is a smaller output and one task.

## Shipped contracts this changes

The workshop requires a design proposal for a change to a shipped contract. This change touches:

- the set type and schema (`kb/reports/types/agentic-system-analysis-set.md`): five members for a complete outcome;
- the overview type and schema: section removed, verification subsections changed;
- a new reconciliation type and schema in `kb/types/`;
- the record contract's rule that only the overview's Reconciliation amends records, and the mentions of that location in the source contract, the three member types, the generated-review type, `kb/agentic-systems/COLLECTION.md`, `kb/reference/commands.md` and `kb/reference/validation-contract.md`;
- the one-line descriptions of the overview in `scan-agentic-system-transfer` and `synthesize-agent-memory-landscape`.

## Steps

Commit each step separately. Steps 2–5 are one method change and land before any new run, because a run pins the method commit when it opens.

1. **Design proposal.** Write the proposal in `kb/reference/proposals/` under the design-proposal type: the problem, this design and the alternatives discussed (reconciliation kept as an overview section; record faults at synthesis verification reopening reconciliation; verification moved into the reconciliation member). The operator's selection is this plan. The proposal becomes an ADR when step 5 ships.
2. **Archive the present sets.** Move `AAS-2026-09-29-pageindex-02` and `AAS-2026-09-30-instinctual-memory-02` to `kb/reports/retained/agentic-system-analysis-archive/` and their two generated reviews to `kb/agentic-systems/reviews-archive/`, following commits `255c9645` and `e57af861`: pins rewritten to the archive path, hashes still verifying. Confirm first that the archive directories are outside set validation, as that precedent implies. Do this before the contract change so no retained set fails validation in between.
3. **Types and schemas.** Add the reconciliation type and schema. Change the overview and set types and schemas. Reword the contracts and documents listed above. Add `reconciliation.md` to the member names in `src/commonplace/lib/agentic_set.py`, and extend the set check so references and amendments resolve through the new member.
4. **Job instructions.** Narrow `jobs/reconcile.md` to the reconciliation and the return route, with a rule for marking a conflict it leaves unresolved. Narrow `jobs/verify.md` to the records. Add `jobs/synthesize.md` and `jobs/verify-synthesis.md`. Update the mention of the overview draft in `jobs/worker-rules.md` and of amendments in `jobs/memory.md`.
5. **Workflow.** In `src/commonplace/lib/agentic_workflow.py`: the reconcile validator requires only its own sections; the round renders the reconciliation member and runs the structural check without a synthesis; the two new jobs and the synthesis correction round follow the record loop; the overview is rendered once from the boundary, the synthesis and both verifications, with the amended-records line. Update the tests that build sets and rounds. `uv run pytest` passes; the contracts and instructions validate.
6. **New runs.** With the method committed, run PageIndex and Instinctual Memory again. These produce the retained sets and the regenerated reviews.
7. **Close.** Convert the proposal to an ADR, and record the trial observations below in the workshop.

## Acceptance

- Both new runs publish a five-member set that passes `commonplace-validate --full`, with a review rendered from the overview.
- In each run, `synthesize` is handed out once, plus at most one correction.
- The reconcile and record-verification jobs do not load the overview type; the synthesis jobs do not load the member types.
- No retained set or review under the live directories fails validation at any commit.

## Observations to record from the new runs

- Rounds of reconcile and record verification, and whether any record blocker was about synthesis text.
- Whether `verify-synthesis` named a blocker that traces to a term defined only in a member type.
- Whether `verify-synthesis` found record faults, and how the synthesizer stated them.
- Jobs handed out in total, against run 03's count for Instinctual Memory.

## Stop and escalate

- The structural check cannot run on a set without a synthesis: return the choice between a provisional overview and a record-only check to the operator if neither is a small change.
- A synthesis blocker in the new runs traces to a member-type definition the synthesizer lacked: add that member type to the synthesis jobs' contracts, and record which definition was needed.
- A record fault found at synthesis verification cannot be stated as a limitation without making the synthesis misleading: stop the run and report; this is the evidence for reopening reconciliation from that stage.

## Open choices left to execution

- The reconciliation member's internal headings, beyond holding what the overview section holds today.
- The marker reconcile uses for an unresolved conflict, provided `verify-synthesis` can find each one.
- Whether the round's structural check uses a provisional overview or checks the members and reconciliation directly.
- File names of the round files in the run directory.

## Deferred

- **Cited-record extracts for `verify-synthesis`.** Code could extract only the records the synthesis cites, so the verifier does not read three whole members. Build it only if the new runs show this job's context is a problem.
- **Overlap between reconciliation and record verification.** Both check the memory profile against the records. Run 03's blockers were defects the reconcile instruction already asked it to check. Whether the reconcile job should keep that check, or leave it to verification, is a separate question; the workshop's standing rule is to preserve independent verification.
