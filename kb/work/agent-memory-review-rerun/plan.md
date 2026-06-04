# Plan: Rerun Remaining Agent-Memory Reviews

## Current State

- `systems.csv` has 129 system rows.
- Rows 1-6 have already been rerun in the current worktree: A-mem, ACE, Agent Skills for Context Engineering, Agent Workflow Memory, Agent-R, and Agent-S.
- Remaining rows after those six: 123.
- Remaining rows with `public_repo`: 95.
- Remaining rows without `public_repo`: 28.
- Current review workflow uses the local `write-agent-memory-system-review` skill: parent owns checkout refresh, archive lifecycle, index refresh, taxonomy QA, semantic QA, validation, and final reporting; subagents own only bounded draft replacement notes.

## Assumptions

- "The rest" means rows 7-129 in `kb/agent-memory-systems/systems.csv`, in CSV order unless a row is blocked.
- Rows with `public_repo` should use the normal code-grounded GitHub checkout workflow.
- Rows without `public_repo` should not be forced through that workflow. They need a separate source-resolution pass: find an existing checkout/source pointer, confirm the old review has enough local source evidence, or mark the row blocked for a later manual/source-recovery run.
- Existing uncommitted first-six changes should be committed before starting the large sweep, so later batches have a clean baseline and failures are easier to isolate.

## Execution Shape

1. **Close and commit the first-six batch.**
   - Review `git diff`.
   - Stage explicit paths only: six current reviews, six `.replaced.2026-06-04.md` archives, `reviews/dir-index.md`, and `systems.csv`.
   - Commit as one artifact batch if the diff is coherent.

2. **Preflight the remaining queue.**
   - Generate a queue file from `systems.csv` with row number, system name, review path, `public_repo`, clone path, and lane.
   - Lane A: `public_repo` present.
   - Lane B: `public_repo` missing/source resolution needed.
   - For Lane A, check whether clone paths exist and whether their remotes match the CSV repo. Do not repair conflicts destructively.

3. **Run Lane A in waves of four.**
   - Use four worker subagents per wave, matching the currently available parallelism.
   - Each worker gets one system, one checkout, one target review file, source metadata, and strict ownership of only the replacement review file.
   - Parent does checkout refresh, archival `git mv`, archive frontmatter/pointer edits, worker spawning, taxonomy QA, semantic QA, index refresh, validation, and final integration.

4. **Commit every two waves, not every wave.**
   - Two waves is usually eight reviews. That is small enough to inspect and revert with ordinary commits, but large enough to avoid 24 tiny commits for the 95 public repos.
   - If a wave contains unusually large or risky systems, commit that wave alone.
   - Each commit should include only the refreshed reviews, their archives, generated review index changes, and any intentional `systems.csv` corrections from that batch.

5. **QA loop per wave.**
   - Refresh indexes once after all four workers finish.
   - Run taxonomy QA locally over the four notes, especially read-back direction, `push-activation`, `trace-derived`, and artifact-axis language.
   - Run semantic QA with `commonplace-create-review-run --with-prompt ... semantic`; write and ingest bundle outputs in the current harness.
   - Validate each changed review.
   - Validate `agent-memory-systems` before committing a two-wave batch.

6. **Lane B source-resolution pass.**
   - Do not rewrite these 28 as if they had fresh GitHub source.
   - For each row, check whether the old review names a repository, local checkout, source snapshot, or internal project path.
   - If a source is recoverable, convert it into a normal rerun task and add/fix `public_repo` or source metadata in `systems.csv` only when code-grounded evidence justifies it.
   - If a source is not recoverable, leave the current review untouched and record it in a blocked/source-needed report.

## First Lane A Waves

Start with the first public-repo rows after Agent-S, skipping no-repo rows into Lane B:

Wave 1:

- AgentFly
- Agentic Harness Engineering
- Archie
- AriGraph

Wave 2:

- ARIS / Auto-claude-code-research-in-sleep
- Ars Contexta
- Atomic
- auto-harness

Wave 3:

- Autocontext
- Awesome Agent Memory
- Binder
- browzy.ai

Wave 4:

- byterover-cli
- cass_memory_system
- Claude Context Guard
- clawvault

## Lane B Rows

Rows without `public_repo` after the first six:

- Agentic Local Brain
- AI Context OS
- ai-memex-cli
- ai-modules
- Basic Memory
- beever-atlas
- claude-obsidian
- Continuity
- Cortex
- dense-mem
- Echel
- Funes
- interview-doc-agent
- Kompl
- llm-context-base
- llm-project-wiki
- llm-wiki-coordination
- Memex
- OpenClerk
- Origin
- Quicky Wiki
- sage-wiki
- Secure LLM-Wiki
- Sparks
- Synthadoc
- TheKnowledge
- VLM-wiki
- WeKnora

## Stop Conditions

- Checkout has local commits, dirty state, remote mismatch, or non-fast-forward update.
- Repository is unreachable after one escalated fetch/clone attempt.
- Worker cannot produce a code-grounded review from the checkout.
- Semantic QA produces a real WARN/FAIL that needs source rereading or revision.
- Collection validation reports warnings/failures after a batch.

## Reporting

For each committed batch, report:

- rows covered and skipped
- repos cloned/reused/refreshed
- checkout freshness warnings
- whether drafting was delegated
- index/CSV/survey changes
- taxonomy QA summary
- semantic gate result counts
- validation result
- commit hash
