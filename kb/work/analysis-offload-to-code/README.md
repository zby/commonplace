# Workshop: offload analyse-agentic-system mechanics into code

- **Posed:** 2026-09-28, by the operator's direction after a review of the skill.
- **Start condition:** implementation begins only after the current batch of agentic-analysis runs (batch 01 rerun and batch 02) is done. Until then this workshop holds design only; do not change commands, schemas, or the skill.
- **Closes when:** each item below is implemented, or explicitly dropped, and `kb/instructions/analyse-agentic-system/SKILL.md` has been trimmed to the judgment core plus command calls. Then extract any durable decisions to `kb/reference/` and delete this workshop.

## Goal

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

Tier 3 — code proposes, the agent decides (lower priority):

11. **Seed scanners over the frozen commit.** Entry points, model and provider references (CMP seeds), alternate paths (subprocess, shell, provider-native tools, callbacks), prompt files, and a file-layer classification for the SRC register. Each emits candidates with quote blocks and a search-boundary receipt (patterns plus tree) that can support a load-bearing `ABS-*` claim. Output must say it is a seed list, not coverage, to limit anchoring.
12. **`memory-input.md` generator.** Assemble the frozen input from run-state and the overview draft, and hash it. The input is frozen, so the agent does not edit it.
13. **`publish` runs `prepare` internally; `status` command.** `status <run>` derives the phase and the next allowed action from files and hashes. It must not store a phase ledger, which the skill forbids.
14. **Comparison staleness in the handoff.** Compute which `kb/agentic-systems/comparisons/` outputs a changed review makes stale.

## Decided against

- **Scaffold command for the four members.** It would have to emit empty sections. Those either fail validation or need a placeholder convention, and a placeholder that passes validation records a section as present when nothing was analysed. The validator's missing-section errors already serve as the checklist. The useful part, deterministic frontmatter, is covered by item 1's printed block or a validator cross-check of member frontmatter against run-state.

## Constraints and risks

- **Contract drift.** Tools that embed section headings or the `METHOD_PATHS` list can drift from the type specs. Generate from the schemas and the existing constant instead of copying them.
- **Method paths.** Every new command widens what must be committed before a run opens, because publication requires the package source to equal `inputs-commit`. Land these changes between batches, not during one.
- **YAGNI.** If an item turns out not to be needed, drop it here; write a design proposal in `kb/reference/proposals/` for any item that changes a shipped contract before implementing it.
- **Related workshops:** [agentic-analysis-output-documents](../agentic-analysis-output-documents/README.md) owns the current set and publication contracts; coordinate before changing them. [analyse-agentic-system](../analyse-agentic-system/README.md) holds the skill's construction history.
