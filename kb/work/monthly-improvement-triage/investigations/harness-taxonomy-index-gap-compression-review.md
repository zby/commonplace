# Compression Bundle Review: Runtime structure determines the control surfaces available to governance

**Target:** `kb/notes/runtime-structure-determines-governance-control-surfaces.md`
**Bundle:** `kb/work/agent-note-improvement/compression/`
**Reviewer:** fresh sub-agent, blind (no prior context beyond the note text and gate definitions), run against the merged note before the fixes below were applied.

## Overall Result

WARN

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | PASS | Title and first paragraph state the claim plainly and prominently; everything after clearly serves it until the matrix section. |
| compression/branch-bloat | WARN | The "general pattern" bullets closing the matrix section introduced new, loosely-argued side-claims that competed with the note's stated thesis rather than supporting it. |
| compression/detail-overhang | WARN | The commonplace matrix section carried implementation-level detail (specific instruction/tool names) disproportionate to a theory-register note; it roughly doubled the note's length for one worked example. |
| compression/marginal-value-redundancy | WARN | The four closing bullets restated/extended the table's content without clearly returning value to the main claim; one bullet was self-contradictory about its own generality. |

## Findings

### compression/branch-bloat

- WARN: The four "general pattern" bullets at the end of the matrix section ("Governance density tracks authorship control," "Inform is the most uniformly populated operation," "Validate and correct are layered by cost and confidence," "Drift detection is content-addressed, not timestamp-based") each asserted a new, independent claim about commonplace specifically — none of which were set up or needed by the note's actual thesis (structure affords/constrains governance; governance hardens into structure). The reviewer flagged this as the clearest evidence that the merge produced "two documents stapled together": the theory section (through "Consequence for runtime comparison") is a complete, self-closing argument; the matrix section restarted with its own scope and conclusions that didn't fold back into the asymmetric-dependence framing above.
- INFO: The matrix table itself was judged a legitimate formalization of the "structural affordances for governance" section — defensible; the discursive bullets after the table were the actual problem.

### compression/detail-overhang

- WARN: The table cells and the "scheduler row is mostly empty" paragraph named commonplace-specific artifacts in more detail than needed to illustrate the abstract claim (e.g. specific instruction and command names, DB mentions) — a fully populated 3×4 grid plus follow-up prose where two or three representative cells would do the same job.
- INFO: Given this is `kb/notes/` (theoretical register) and the project routes "describing the shipped Commonplace system" to `kb/reference/` (descriptive register), the matrix's implementation specificity sat closer to reference-collection content than to a transferable theory claim.

### compression/marginal-value-redundancy

- WARN: "Drift detection is content-addressed, not timestamp-based" was introduced as "a general pattern beyond this one system," but its own justification ("This fell out of using git as the versioning layer...") was explicitly about commonplace's implementation choice — the bullet contradicted its own framing.
- WARN: "Governance density tracks authorship control" duplicated, at lower argumentative quality, ground already covered by the theory section's account of why the substrate is "the strongest governance surface."
- INFO: "Inform is the most uniformly populated operation" and "Validate and correct are layered by cost and confidence" were true but were asides about commonplace's specific governance economy, not about the structure-governance relationship the note is named for.

## Suggested Revision (as given by the reviewer)

Keep the theory sections through "Consequence for runtime comparison" as-is. For the matrix section: trim cell content to short labels and move implementation-heavy detail out; cut the four closing bullets to at most one, generalizing the drift-detection observation properly and folding it into the existing "Execution substrate" paragraph where hash-diffing is already discussed; cut the authorship-control and inform/validate-cost bullets or demote them to a future workshop lead; re-read the matrix's opening sentence afterward to confirm it reads as one continuous argument rather than an appended second essay.

## Fixes applied

All four suggested changes were applied directly to `kb/notes/runtime-structure-determines-governance-control-surfaces.md`:

1. The corrected, generalized drift-detection claim ("content-addressed comparison is a stronger drift oracle than timestamps...") was folded into the "Execution substrate" paragraph in the theory section, replacing the earlier "compare SHAs" phrasing with the fuller argument.
2. The matrix table cells were trimmed to short labels (e.g. "routing/skill descriptions" instead of naming specific instruction files and command names); the "SQLite DB" / `note-changed`/`gate-changed` implementation detail was removed.
3. All four closing "general pattern" bullets were deleted. The scheduler-row explanation was kept and tightened into one paragraph that explicitly ties the empty row back to the note's own claim ("the empty row is itself evidence for this note's claim rather than an exception to it") instead of trailing into unrelated observations.
4. Re-read after editing: the matrix section now opens with "Crossing the two axes for commonplace itself is one worked example of the general claim" and closes by referring back to the theory claim, reading as one continuous note.

`commonplace-validate` was re-run after the edits: PASS (clean, no WARN/FAIL/INFO).
