---
description: Write or update a code-grounded agent memory system review from a GitHub repository checkout.
type: note
---

# Write an Agent Memory System Review

Use this procedure to write or update `type: agent-memory-system-review` notes for external GitHub repositories under `kb/agent-memory-systems/reviews/`.

## Prerequisites

- The topic is a GitHub repository reference: `owner/repo` or `https://github.com/owner/repo`.
- The repository is reachable.
- The checkout lives under `related-systems/`, outside `kb/`.

If the system has no reachable source code, stop and write a source-only note instead.

## Steps

1. **Normalize the repository target.** Derive:
   - `repo_url` — canonical full GitHub repository URL for citations, `https://github.com/{owner}/{repo}` with no trailing slash or `.git`
   - `owner` — GitHub owner or organization
   - `repo_name` — final path segment
   - `repo_slug` — default review slug, usually `repo_name`
   - `checkout_slug` — owner-qualified checkout slug: `{owner}--{repo_name}`
   - `checkout_dir` — `related-systems/{checkout_slug}/`
   - `note_path` — `kb/agent-memory-systems/reviews/{repo_slug}.md`

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

6. **Capture orientation.** Record the top-level listing, most recent commit, README, and package/manifest files for the writer's context. The writer establishes `reviewed_commit` and checkout freshness from `checkout_dir` at the start of the artifact contract.
   Write the refresh marker immediately after a successful clone/fetch/pull:
   ```bash
   git_dir="$(git -C "{checkout_dir}" rev-parse --absolute-git-dir)"
   date -Iseconds > "$git_dir/commonplace-checkout-refreshed-at"
   ```

7. **Archive an existing review before writing.** If `note_path` exists, archive it before drafting or delegating:
   ```bash
   git mv "{note_path}" "{note_path%.md}.replaced.{YYYY-MM-DD}.md"
   ```
   Then mark the archived file:
   - Set `status: outdated` in frontmatter.
   - Change `tags: [related-systems, trace-derived]` to `tags: []`.
   - Add after the title: `> Replaced {YYYY-MM-DD}. See [{name}](./{name}.md) for the current review.`
   Do not read the archived `.replaced.*.md` file while writing the replacement.

8. **Write or delegate the review.** Use the artifact contract in `kb/agent-memory-systems/types/agent-memory-system-review.instructions.md` as the writing prompt. Pass the writer these inputs: `repo_url`, `checkout_dir`, and `note_path`.

9. **If delegating, keep ownership narrow.** The worker may read the checkout and write the review note or draft path only. The runner owns checkout, archive moves, curated index edits, semantic QA, validation, and final report. The worker must decide trace-derived status from implementation evidence and either include both the placement section and `trace-derived` tag, or omit both.

10. **Update the curated index.** If this is a new review, update `kb/agent-memory-systems/README.md`:
    - add the system to the `## Systems` list
    - update `## Patterns Across Systems` only if this repo adds a genuinely new cross-system pattern
    Keep the edit minimal and specific.

11. **Update the trace-derived survey if needed.** If the review's trace-derived placement adds meaningfully to the survey, update `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`.

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
- whether the curated index changed
- whether `trace-derived-learning-techniques-in-related-systems.md` changed
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
