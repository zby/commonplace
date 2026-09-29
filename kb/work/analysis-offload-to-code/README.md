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

10a. **Fail-fast command wrapper.** Run multi-step reads and edits so that any failed step fails the whole call: `check=True` semantics, pipefail, and a nonzero aggregate exit when a discovery loop skips a missing path. Motivating case: in the batch 01 rerun a Python excerpt-assembly step raised `ValueError` under an outer exit status of zero, and the shell went on to validate the old report (MM 160). Two more zero-status failures came from `git show ... | sed` without pipefail (B 142) and a read loop that printed stderr and continued (BM 99). The skill already states the rule; the prose did not prevent it. Belongs beside item 6.

Tier 3 — code proposes, the agent decides (lower priority):

11. **Seed scanners over the frozen commit.** Entry points, model and provider references (CMP seeds), alternate paths (subprocess, shell, provider-native tools, callbacks), prompt files, and a file-layer classification for the SRC register. Each emits candidates with quote blocks and a search-boundary receipt (patterns plus tree) that can support a load-bearing `ABS-*` claim. Output must say it is a seed list, not coverage, to limit anchoring.
12. **`memory-input.md` generator.** Assemble the frozen input from run-state and the overview draft, and hash it. The input is frozen, so the agent does not edit it.
13. **`publish` runs `prepare` internally; `status` command.** `status <run>` derives the phase and the next allowed action from files and hashes. It must not store a phase ledger, which the skill forbids.
14. **Comparison staleness in the handoff.** Compute which `kb/agentic-systems/comparisons/` outputs a changed review makes stale.

## Decided against

- **Scaffold command for the four members.** It would have to emit empty sections. Those either fail validation or need a placeholder convention, and a placeholder that passes validation records a section as present when nothing was analysed. The validator's missing-section errors already serve as the checklist. The useful part, deterministic frontmatter, is covered by item 1's printed block or a validator cross-check of member frontmatter against run-state.

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

- **Contract drift.** Tools that embed section headings or the `METHOD_PATHS` list can drift from the type specs. Generate from the schemas and the existing constant instead of copying them.
- **Method paths.** Every new command widens what must be committed before a run opens, because publication requires the package source to equal `inputs-commit`. Land these changes between batches, not during one.
- **YAGNI.** If an item turns out not to be needed, drop it here; write a design proposal in `kb/reference/proposals/` for any item that changes a shipped contract before implementing it.
- **Related workshops:** [agentic-analysis-output-documents](../agentic-analysis-output-documents/README.md) owns the current set and publication contracts; coordinate before changing them. [analyse-agentic-system](../analyse-agentic-system/README.md) holds the skill's construction history.
