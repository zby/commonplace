---
name: write-agent-memory-system-review
description: Write or update a local code-grounded agent memory system review from a GitHub repository reference, including checkout refresh, optional sub-agent drafting, semantic QA, and validation.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
argument-hint: "owner/repo | https://github.com/owner/repo"
---

# Write Agent Memory System Review

Use this local skill to write or update `type: kb/agent-memory-systems/types/agent-memory-system-review.md` notes for external systems under `kb/agent-memory-systems/reviews/`.

This is a local commonplace-repo workflow, not a promoted `cp-skill-*` framework skill. The parent agent owns GitHub handling, local source directory setup, artifact lifecycle, taxonomy/semantic QA, the closing validation pass, indexes, and the final report; the delegated worker validates and fixes its own draft's structure before returning, but owns nothing else. Delegate the code-grounded review drafting to a fresh worker context whenever the harness has a sub-agent mechanism.

Delegation means a harness-provided sub-agent/worker tool only. Never start a nested agent by running `codex`, `codex exec`, `claude`, or any other agent CLI from the shell. If the current agent cannot access the required harness sub-agent tool or an agent slot is unavailable, stop or wait and report the blocking condition; do not work around the limit with a command-line agent process.

## Prerequisites

- The topic is a GitHub repository reference: `owner/repo` or `https://github.com/owner/repo`.
- The repository is reachable.
- The checkout lives under `related-systems/`, outside `kb/`.

If the system has no reachable source code, stop and write a lightweight note instead.

## Steps

1. **Normalize the repository target.** Derive:
   - `repo_url` - canonical full GitHub repository URL for citations, `https://github.com/{owner}/{repo}` with no trailing slash or `.git`
   - `owner` - GitHub owner or organization
   - `repo_name` - final path segment
   - `repo_slug` - default review slug, usually `repo_name`
   - `checkout_slug` - owner-qualified checkout slug: `{owner}--{repo_name}`
   - `checkout_dir` - `related-systems/{checkout_slug}/`
   - `source_dir` - same path as `checkout_dir`; this is the directory passed to the review type contract
   - `note_path` - `kb/agent-memory-systems/reviews/{repo_slug}.md`

2. **Resolve same-name collisions.** Use the repository name as the default review filename unless there is already an established house-style variant. If `kb/agent-memory-systems/reviews/{repo_name}.md` already exists for a different GitHub repository with the same final path segment, use `kb/agent-memory-systems/reviews/{owner}--{repo_name}.md`. Do not overwrite or update a same-name review unless its `**Repository:**` line or frontmatter resolves to the same `owner/repo`.

3. **Choose the checkout path.** Use the owner-qualified checkout directory for new clones. Existing reviews may have legacy basename-only checkouts such as `related-systems/{repo_name}/`; use a legacy checkout only when its `origin` remote resolves to the same GitHub `owner/repo` you are reviewing. If a legacy checkout points to a different owner with the same repository name, do not pull it, delete it, or repurpose it; clone the requested repo into the owner-qualified `checkout_dir`.

4. **Check main repo state.** Run `git status --short` in the main repo before cloning or writing so you know whether unrelated changes already exist.

5. **Clone or refresh.** Run checkout-local git commands from `checkout_dir` using the Bash working directory, a subshell, or `cd` first. Do not spell checkout-local commands as `git -C "{checkout_dir}" ...`; permission rules match command prefixes such as `git fetch`, and `git -C ... fetch` can unnecessarily trigger approval prompts. After checkout git operations, return to the Commonplace root before metadata capture, archive moves, index refresh, QA, or validation.

   If `checkout_dir` does not exist:
   ```bash
   git clone "{repo_url}" "{checkout_dir}"
   ```
   If `checkout_dir` exists:
   ```bash
   (
     cd "{checkout_dir}"
     git fetch --all --prune
     git status --short
     git merge --ff-only @{upstream}
   )
   ```
   If using `cd` in the current shell instead of a subshell, save the Commonplace root first and `cd` back to it immediately after the checkout git commands.

   Use `git fetch` rather than `git pull` so the refresh uses the agent-approved fetch permission path. If the merge cannot fast-forward because of local commits or conflicts, stop and report the state. Do not force, delete, or overwrite an existing checkout.

6. **Capture source metadata.** Record the top-level listing, most recent commit, README, and package/manifest files for the writer's context. The parent establishes GitHub-specific metadata before delegation:
   - `source_dir`: `checkout_dir`
   - `source_url`: `repo_url`
   - `reviewed_commit`: output of `git rev-parse HEAD` run from `checkout_dir`
   - `commit_url`: `{repo_url}/commit/{reviewed_commit}`
   - citation format:
     - files: `{repo_url}/blob/{reviewed_commit}/{path}`
     - directories: `{repo_url}/tree/{reviewed_commit}/{path}`

   Write the refresh marker immediately after a successful clone or fetch-and-fast-forward:
   ```bash
   (
     cd "{checkout_dir}"
     git_dir="$(git rev-parse --absolute-git-dir)"
     date -Iseconds > "$git_dir/commonplace-checkout-refreshed-at"
   )
   ```
   If the marker is more than 1 hour old by the time drafting starts, carry a checkout freshness warning into the final report. If it is more than 24 hours old, refresh again before drafting.

7. **Archive an existing review before writing.** If `note_path` exists, archive it before drafting or delegating:
   ```bash
   git mv "{note_path}" "{note_path%.md}.replaced.{YYYY-MM-DD}.md"
   ```
   If that target path already exists (a same-day rerun already archived one), do not overwrite it: append a numeric suffix starting at `2` and increment until the path is free — `{note_path%.md}.replaced.{YYYY-MM-DD}.2.md`, then `.3.md`, and so on.

   Then mark the archived file:
   - Set `status: outdated` in frontmatter.
   - Set `tags: []` (clearing any `trace-derived` tag).
   - Add after the title: `> Replaced {YYYY-MM-DD}. See [{name}](./{name}.md) for the current review.`
   Do not read the archived `.replaced.*.md` file while writing the replacement.

8. **Draft the review by delegation.** Use `kb/agent-memory-systems/types/agent-memory-system-review.md` as the worker's artifact contract for required sections and fields. Do not ask the worker to load the full [designing-agent-memory-systems](../../notes/designing-agent-memory-systems.md) note during ordinary review writing — its comparison lens is already distilled into the contract.

   Before delegating: if the harness cannot launch a sub-agent or worker, stop after setup and report that delegated drafting is unavailable. Do not draft locally unless the user explicitly authorizes a local fallback for this run; if authorized, report `drafting was local, not delegated` as a workflow exception. This is a parent-only decision, made before any worker exists — a worker that has actually been launched is, by construction, the delegated drafting worker and never needs to reason about fallback authorization itself.

   Launch one fresh sub-agent or worker with a minimal task-local context. Do not fork the parent's full context when the harness offers a clean-context option. Use only the harness sub-agent mechanism for this delegation; do not launch an agent CLI from Bash. Give the worker exactly this task, with the bracketed values filled in — this task text is the worker's complete brief; do not also hand it this skill file:

   ```text
   Draft review content for {note_path}.

   You are a delegated drafting worker; this task text is your complete and only brief. Your environment may surface `write-agent-memory-system-review` or another skill as available or auto-loaded because this task resembles its trigger — if so, do not invoke or follow it. Its steps (checkout, archiving, indexes, QA, final validation) are written for the parent that dispatched you, not for you. Ignore it entirely and follow only the instructions below.

   Read, in this order:
   - kb/agent-memory-systems/COLLECTION.md
   - kb/agent-memory-systems/types/agent-memory-system-review.md — the artifact contract; authoritative for required sections and fields. Use its current retained-artifact vocabulary, including `knowledge-artifact` and `system-definition-artifact` as behavioral-authority families.
   - 1-2 current reviews in kb/agent-memory-systems/reviews/ and kb/agent-memory-systems/README.md, for style

   Your inputs:
   - source_dir: {source_dir} (already prepared; do not mutate it)
   - note_path: {note_path}
   - reviewed_revision / source identity: {reviewed_revision}
   - source_url: {source_url}
   - reviewed_commit: {reviewed_commit}
   - commit_url: {commit_url}
   - citation format — files: {repo_url}/blob/{reviewed_commit}/{path}; directories: {repo_url}/tree/{reviewed_commit}/{path} (unless the caller supplies a different format)

   If any input above is missing, stop and report which. Verify source_dir is readable (e.g. test -d); if it isn't, stop and report. Never update last-checked without actually reading source_dir.

   Ground the review in primary sources in source_dir — README, architecture/design docs, CLAUDE.md/AGENTS.md, package manifests, and the core source files implementing the central claims. Where the implementation clarifies or contradicts the README, report what the code does and note the divergence. Decide trace-derived status from implementation evidence and either include both the placement section and the trace-derived tag, or omit both.

   Write note_path from the code outward.

   Then run: commonplace-validate {note_path}
   Fix any structural or description-quality issues it reports and re-run until clean — you own this file, so fix it directly rather than reporting it back.

   Do not edit indexes, archived reviews, the trace-derived survey, checkout state, or any file other than note_path. Do not run any commonplace-* command other than commonplace-validate on note_path. Do not spawn further agents unless a proper sub-agent/worker tool is available to you; if you need one and none is available, pause and report the blocker — never run codex, codex exec, claude, or another agent CLI as a substitute.

   Report: your commonplace-validate result and whether trace-derived learning applies.
   ```

   The parent owns checkout, archive moves, curated index edits, taxonomy QA, semantic QA, and the final report — none of that is the worker's concern.

9. **Update the README only if needed.** Only edit `kb/agent-memory-systems/README.md` when:
   - the system was named in the `## Coverage` "Review backlog" callout — remove it there, or
   - the repo adds a genuinely new cross-system pattern worth a line in `## Patterns Across Systems`.
   Keep the edit minimal and specific.

10. **Update the trace-derived survey if needed.** If the review's trace-derived placement adds meaningfully to the survey, update `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`.

11. **Run taxonomy QA.** Re-read the drafted review and check whether it makes the artifact contract clear where relevant. Work from the type contract's artifact-analysis field list (plus its trace-derived split, when the system learns from traces) — the contract is authoritative for which fields exist and what each means; do not QA against a remembered list. For each contract field, ask: does the review make that mechanism clear where it affects the comparison? Do not force a rigid section into every review; add or revise prose only when the existing text leaves a mechanism ambiguous.

   If a field is absent because the reviewed system has no distinctive mechanism there, leave it absent. If the absence hides an important tradeoff, fix the review before semantic QA.

12. **Run semantic QA.** Run the live-agent procedure from `kb/instructions/run-review-batches.md` on the new review note using requested mode with the `semantic` bundle: select target pairs with `commonplace-review-target-selector --mode requested`, create jobs from selector JSON with `commonplace-create-review-jobs --input -`, delegate each job to a sub-agent, then finalize each sentinel-bracketed output with `commonplace-finalize-review-job` and the runner/model provenance flags. Treat it as a read-only QA loop: extract findings, fix clearly valid issues, and leave uncertain findings for the final report rather than forcing a rewrite.

   If semantic QA cannot be completed through the current harness, report it as a blocked QA step rather than substituting a shell-launched agent.

13. **Validate.** Run:
    ```bash
    commonplace-validate "{note_path}"
    ```
    If validation reports structural or description-quality issues, fix them and validate once more.

## Report

Report:

- repo cloned or reused
- checkout freshness warning, if any
- review path
- whether drafting was delegated
- whether the curated index changed
- whether `trace-derived-learning-techniques-in-related-systems.md` changed
- taxonomy QA outcome
- semantic gate bundle outcome
- final `commonplace-validate` result

## Constraints

**Always:**

- keep checkouts under `related-systems/`
- use owner-qualified checkout directories for new clones
- write reviews under `kb/agent-memory-systems/reviews/`
- cite repo source files with GitHub URLs pinned to the commit derived from the checkout
- run semantic QA before final validation

**Never:**

- put checked-out repos under `kb/`
- overwrite or repurpose an existing checkout whose remote points to a different owner/repo
- force-pull, delete, or reset a checkout to handle conflicts
- update `last-checked` without actually re-reading the reviewed system
- run `codex`, `codex exec`, `claude`, or another agent CLI from the shell to bypass delegation or worker limits
- leave the review unvalidated
