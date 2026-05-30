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

This is a local commonplace-repo workflow, not a promoted `cp-skill-*` framework skill. The parent agent owns GitHub handling, local source directory setup, artifact lifecycle, QA, validation, indexes, and the final report. Delegate the code-grounded review drafting to a fresh worker context whenever the harness has a sub-agent mechanism.

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

5. **Clone or refresh.** If `checkout_dir` does not exist:
   ```bash
   git clone "{repo_url}" "{checkout_dir}"
   ```
   If `checkout_dir` exists:
   ```bash
   cd "{checkout_dir}"
   git fetch --all --prune
   git status --short
   git pull --ff-only
   ```
   If the pull cannot fast-forward because of local commits or conflicts, stop and report the state. Do not force, delete, or overwrite an existing checkout.

6. **Capture source metadata.** Record the top-level listing, most recent commit, README, and package/manifest files for the writer's context. The parent establishes GitHub-specific metadata before delegation:
   - `source_dir`: `checkout_dir`
   - `source_url`: `repo_url`
   - `reviewed_commit`: output of `git -C "{checkout_dir}" rev-parse HEAD`
   - `commit_url`: `{repo_url}/commit/{reviewed_commit}`
   - citation format:
     - files: `{repo_url}/blob/{reviewed_commit}/{path}`
     - directories: `{repo_url}/tree/{reviewed_commit}/{path}`

   Write the refresh marker immediately after a successful clone/fetch/pull:
   ```bash
   git_dir="$(git -C "{checkout_dir}" rev-parse --absolute-git-dir)"
   date -Iseconds > "$git_dir/commonplace-checkout-refreshed-at"
   ```
   If the marker is more than 1 hour old by the time drafting starts, carry a checkout freshness warning into the final report. If it is more than 24 hours old, refresh again before drafting.

7. **Archive an existing review before writing.** If `note_path` exists, archive it before drafting or delegating:
   ```bash
   git mv "{note_path}" "{note_path%.md}.replaced.{YYYY-MM-DD}.md"
   ```
   Then mark the archived file:
   - Set `status: outdated` in frontmatter.
   - Set `tags: []` (clearing any `trace-derived` tag).
   - Add after the title: `> Replaced {YYYY-MM-DD}. See [{name}](./{name}.md) for the current review.`
   Do not read the archived `.replaced.*.md` file while writing the replacement.

8. **Draft the review by delegation.** Use `kb/agent-memory-systems/types/agent-memory-system-review.md` as the worker's artifact contract. Its embedded comparison lens is the review-time distillation of the memory-system design; do not ask the worker to load the full design note during ordinary review writing. The worker should follow the type contract's current retained-artifact vocabulary, including knowledge-artifact and system-definition-artifact use as behavioral-authority families.

   Launch one fresh sub-agent or worker with a minimal task-local context. Do not fork the parent's full context when the harness offers a clean-context option. Give the worker only the local skill handoff, the type contract path, the source directory, the target note path, and the source metadata listed below.

   The worker has only this ownership:
   - read `kb/agent-memory-systems/COLLECTION.md`
   - read `kb/agent-memory-systems/types/agent-memory-system-review.md`
   - read 1-2 current reviews for style
   - inspect `source_dir`
   - write `note_path`
   - decide trace-derived status from implementation evidence and either include both the placement section and `trace-derived` tag, or omit both

   Pass the worker these type-contract inputs:
   - `source_dir`
   - `note_path`

   Also pass this parent-supplied source metadata for the review note:
   - `source_url`
   - `reviewed_commit`
   - `commit_url`
   - citation format for files and directories

   The worker must not edit indexes, archived reviews, the trace-derived survey, checkout state, or unrelated files. The parent owns checkout, archive moves, curated index edits, taxonomy QA, semantic QA, validation, and final report.

   If the harness cannot launch a sub-agent or worker, stop after setup and report that delegated drafting is unavailable. Do not draft locally unless the user explicitly authorizes a local fallback for this run. If the user authorizes that fallback, report `drafting was local, not delegated` as a workflow exception.

9. **Refresh indexes; update the README only if needed.** A new review appears automatically in `reviews/dir-index.md` after `commonplace-refresh-indexes`, so the README no longer carries a per-system list. Only edit `kb/agent-memory-systems/README.md` when:
   - the system was named in the `## Coverage` "Review backlog" callout — remove it there, or
   - the repo adds a genuinely new cross-system pattern worth a line in `## Patterns Across Systems`.
   Keep the edit minimal and specific.

10. **Update the trace-derived survey if needed.** If the review's trace-derived placement adds meaningfully to the survey, update `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`.

11. **Run taxonomy QA.** Re-read the drafted review and check whether it makes the artifact contract clear where relevant. Do not force a rigid four-field section into every review; add or revise prose only when the existing text leaves a mechanism ambiguous.

   Check:
   - **Storage substrate:** does the review identify where retained state persists when storage is architecturally relevant?
   - **Representational form:** does it classify behavior-shaping operative parts as prose, symbolic, distributed-parametric, or mixed when that affects the comparison?
   - **Lineage:** does it explain source traces, derivation, invalidation, regeneration, or source-of-truth status for generated or distilled artifacts?
   - **Behavioral authority:** does it distinguish knowledge-artifact use from system-definition-artifact use by naming the consumer, channel, and force?
   - **Trace-derived split:** if the system learns from traces, does the review distinguish raw trace artifacts from distilled behavior-shaping artifacts?

   If a field is absent because the reviewed system has no distinctive mechanism there, leave it absent. If the absence hides an important tradeoff, fix the review before semantic QA.

12. **Run semantic QA.** Run the procedure from `kb/instructions/run-review-bundle-on-note.md` on the new review note using the `semantic` bundle. Treat it as a read-only QA loop: extract findings, fix clearly valid issues, and leave uncertain findings for the final report rather than forcing a rewrite.

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
- leave the review unvalidated
