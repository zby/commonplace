# Plan: role-specific contract packets and code-owned form

- **Commissioned:** 2026-10-01, by the operator, after a brainstorm on reducing what analysts and the orchestrator must read. The operator selected two of the brainstormed ideas for a plan: (1) deliver each worker only the contract sections its role needs; (2) let code own output form through a filled skeleton and validator messages.
- **Status:** plan, not started. One step reverses a recorded workshop decision and needs the operator's confirmation (see "Decision needed").
- **Purpose:** reduce each worker's fixed reading without removing an analytical requirement, an evidence distinction, or a field.
- **Not in scope:** the size of run inputs (members read by later jobs), the theory account's ownership, verification splitting, the orchestrator's reading, and harness-specific worker rules. The brainstorm listed these separately.

## Expected size of the gain

Measured from the current files by heading, in UTF-8 bytes. These are estimates of what a section-level selection can drop; step 1 replaces them with exact figures.

| Worker | Fixed reading now | Estimated drop | Share |
|---|---:|---:|---:|
| Reconciliation | 67,592 | ~9,500 | ~14% |
| Verification | 65,709 | ~9,500 | ~14% |
| Memory analyst | 39,016 | ~1,500–2,500 | ~4–6% |
| Epistemic analyst | 41,118 | ~1,500 | ~4% |
| Runtime analyst | 28,765 | ~500–800 | ~2–3% |
| Boundary | 15,371 | ~0 | — |

Where the drop for the two judging jobs comes from:

| File | Sections a judging job does not need | Bytes |
|---|---|---:|
| Overview type | Frontmatter table (code writes the frontmatter), Identity and completion, Template | ~3,000 |
| Memory type | Frontmatter table, Template, and the authoring descriptions of Core ideas, Write side, Read-back, Comparison rationale, Limitations and checks | ~3,800 |
| Epistemic type | Frontmatter table, Template, table and compact-record formatting rules | ~1,900 |
| Runtime type | Frontmatter table, Template | ~800 |

The gain is modest. The member types are mostly definitions, and the judging jobs need the definitions. The larger share of a judging job's context is its run inputs (about 117,000 bytes in run `AAS-2026-09-30-instinctual-memory-03`), which this plan does not touch. Two secondary benefits do not show in the byte counts: each worker reads one contract file instead of four to seven, and identity fields stop being hand-copied.

Step 1 is therefore a gate: if the exact measurement confirms a drop near these figures, the operator decides whether the plan is worth building before the input-side ideas.

## Design

### One packet per job, rendered by code

Code writes `<run>/packets/<job>.md` when it builds a job. The packet holds the worker rules and the contract sections selected for that job, each under a line naming its source file and heading. The job's invocation lists the packet as its single `read-first` file and as its only method input besides the job instruction.

Selection is by heading from the existing files. No second copy of a contract is authored: a digest written by hand would be a derived copy that nothing checks. The type specs stay whole in `kb/types/`, so generic type-conformance review and other readers are unaffected.

The selection table lives in `src/commonplace/lib/agentic_workflow.py`, next to the job constructors that now pass `extra=` file lists. For each job it names, per contract file, the headings included and the headings excluded.

Guards:

- **No silent drop.** A test fails when a contract file has a heading that some job's selection neither includes nor excludes. Adding a section to a contract forces a delivery decision for every job.
- **Freshness.** `step` renders packets deterministically before the engine compares input bytes, so a contract edit changes the packet and reopens the affected jobs, as a changed contract file does today.
- **Method pin.** Packets derive from files under `inputs-commit`; the publication check on an unchanged method already covers them.

Some authoring-only material now sits inside a mixed section and must move under its own heading before it can be excluded:

- Epistemic type: the table-row and compact-record formatting paragraphs inside `## Required blocks`.
- Memory type: the structural rules of the profile mapping inside `## Memory comparison fields` (exact field sets, empty `values` and `evidence` for non-positive assessments), as distinct from the axis definitions and assessment meanings.

These are moves under new headings, with wording preserved.

### Filled skeleton and validator-owned form

For each member-writing job, code extracts the `## Template` block of the member type, fills the fields it already knows (`type`, `run-id`, `reviewed-boundary`, `source-identity`), and writes the result to the job's `scratch` directory as `skeleton.md`. The packet then omits the type's Frontmatter table and Template. The type spec keeps both, so the type-spec contract is unchanged and the template still has one source.

Rules that the schema or validator already enforces leave the delivered text. `kb/types/type-spec.md` already says a type body must not restate a schema rule. For each such sentence, the audit in step 4 records the validator message that replaces it; where the message does not tell the author how to repair the defect, the message is improved before the sentence is cut. A sentence with no enforcing check stays.

Every member-writing job instruction tells the worker to run `commonplace-validate --full <output>` and repair before finishing. The memory and epistemic jobs say this today; the runtime job does not. This matters because code retries a refused output once and then blocks the job: format repairs must happen inside the worker's own attempt, not consume the retry.

## Decision needed

The workshop README records, under "Decided against", a scaffold command for the four members. Its reason: a scaffold emits empty sections, and a placeholder that passes validation would record a section as present when nothing was analysed. It kept only deterministic frontmatter as useful.

The skeleton here differs in two ways, and the plan depends on both holding:

1. It is written to `scratch`, not to `output`. A worker that submits nothing has written no output.
2. An unfilled required section must fail acceptance. Step 3 verifies this for each member type and adds the rule where it is missing. No placeholder convention is introduced.

If the operator keeps the earlier decision, the plan drops the skeleton's body and keeps only code-filled frontmatter, delivered as a block in the invocation. The packet then keeps each type's Template. The cost is about 300–800 bytes per analyst.

## Steps

Each step ends with `uv run pytest` passing and `commonplace-validate` clean on the edited contracts and instructions. Commit each step separately.

1. **Measure and fix the selection table (no behavior change).** Write the per-job include and exclude lists against the current headings, and compute exact fixed bytes per job from them. Record the table and figures in this file. Settle the uncertain rows: whether a judging job needs the memory type's section descriptions for Core ideas, Write side, Read-back and Comparison rationale. The test for each row: name the check in `jobs/reconcile.md` or `jobs/verify.md` that would use the section; if none does, exclude it. **Gate:** report the figures to the operator before step 2.
2. **Move mixed authoring material under its own headings.** The two moves listed under Design, with wording preserved. Markdown only.
3. **Verify empty-section refusal.** For the runtime, memory and epistemic types, check that a member whose required section is empty, or still holds a template placeholder such as `{System}`, fails `commonplace-validate --full`. Add the missing rule and a test for each gap.
4. **Audit restated rules.** For each member type, list every body sentence that a schema or registered validator rule enforces, with the rule and its message. Improve messages that do not state the repair. Record the list here. Do not delete yet.
5. **Render packets.** Implement packet rendering, the selection table, the no-silent-drop test and the freshness behavior. Switch every job from `extra=` file lists to its packet. At this step each packet still includes every section, so the delivered content is unchanged and only the delivery path is tested.
6. **Apply the selections.** Turn on the excludes from step 1. Record before and after bytes per job.
7. **Deliver the skeleton** (after the decision above). Write `skeleton.md` per member-writing job, name it in the invocation, exclude Frontmatter and Template from analyst packets, and add the validate-before-finishing instruction to `jobs/runtime.md`.
8. **Cut the audited sentences.** Remove from the type bodies the sentences step 4 listed whose messages are adequate. This changes the type specs themselves, so run the type-conformance checks on the four types afterward.
9. **Trial.** One full run on a previously analysed target. Compare with its earlier run: refusals and retries per job, blocked jobs, verification blockers, and whether any blocker traces to a section a packet excluded.

Steps 1–4 are independent of each other after step 1 and change no delivery. Steps 5–8 each depend on the one before.

## Acceptance

- Every job's fixed reading is at or below its step 1 target, measured from the rendered packet plus the job instruction.
- The no-silent-drop test passes, and a contract edit reopens the jobs whose packets include the edited section.
- The trial run completes with no blocker or refusal attributable to an excluded section or a cut sentence, and with no more blocked jobs than the comparison run.
- No field, controlled value, evidence distinction or correction rule is removed from any contract; step 8 removes only sentences an enforcing check replaces.

## Stop and escalate

- Step 1 shows a drop well below the estimates: stop and report; the input-side ideas may be the better investment.
- Step 3 finds that empty-section refusal cannot be added without a placeholder convention: return the skeleton decision to the operator.
- The trial shows a blocker caused by an excluded section: restore that section to the packet and record which check needed it, before any further exclusion.

## Open choices left to execution

- The packet's internal layout and the exact form of its source labels.
- Whether worker rules sit inside the packet or stay a second `read-first` file; either serves, provided the bootstrap rule in each job instruction still names what to read first.
- The order of steps 2, 3 and 4.
