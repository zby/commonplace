---
name: review-related-system
description: Write a related-system review from a GitHub repository. Accepts `owner/repo` or a full `https://github.com/owner/repo` URL, clones into `./related-systems/`, writes the review in `kb/notes/related-systems/`, then runs semantic review and `/validate`.
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[owner/repo|github-url] — GitHub repository slug like `the-shift-dev/napkin` or full repo URL"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:

1. If target is empty, ask for a GitHub repo slug or URL.
2. If target matches `owner/repo`, normalize to `https://github.com/owner/repo`.
3. If target is a full GitHub repo URL, use it directly.
4. If target is not a GitHub repo slug or repo URL, stop and say this skill only accepts GitHub repositories.

**START NOW.**

---

## Goal

Produce a code-grounded related-system review for an open-source repo, stored in the KB's review collection, then run a semantic QA pass and final structural validation.

## Step 1: Normalize the Repository Target

Derive:

- `repo_url` — full GitHub URL
- `owner` — repo owner/org
- `repo_name` — final path segment
- `checkout_dir` — `related-systems/{repo_name}/`
- `note_path` — `kb/notes/related-systems/{repo_name}.md`

Use the repository name as the default review filename unless there is already an established house-style variant for the same system.

## Step 2: Check Existing State

Before cloning or writing:

- Check whether `checkout_dir` already exists.
- Check whether `note_path` already exists.
- Read `git status --short` so you know whether the worktree is dirty.

If the checkout already exists, reuse it. Do not delete or overwrite an existing repo checkout.

If the note already exists, treat the task as an update rather than a new review.

## Step 3: Load the Local Review Rules

Read these files before drafting:

- `kb/instructions/WRITING.md`
- `kb/notes/types/related-system.md`
- `kb/notes/related-systems/README.md`
- `kb/instructions/semantic-review.md`

Also read 1-2 existing reviews in `kb/notes/related-systems/` to match local style and comparison depth.

## Step 4: Clone the Repo

If `checkout_dir` does not exist, clone:

```bash
git clone "{repo_url}" "related-systems/{repo_name}"
```

Then gather quick orientation:

- top-level file listing
- most recent commit (`git log -1`)
- README
- package/manifest/build file(s)

## Step 5: Read for Mechanism, Not Marketing

Ground the review in primary repo sources. Prefer:

- `README.md`
- architecture/design docs
- `CLAUDE.md` / `AGENTS.md` if present
- package manifests and build metadata
- core source files that implement the repo's central claims

Do not rely only on the README if the implementation clarifies or contradicts it.

Focus on:

- storage model
- retrieval/navigation model
- learning/distillation/promotion model if any
- validation/governance model if any
- integration surface (CLI, MCP, API, editor plugin, etc.)
- what is genuinely implemented versus only proposed

## Step 6: Write or Update the Review

Create or update `note_path` using the `related-system` template.

Required properties:

- frontmatter with a discriminating `description`
- `type: note`
- `tags: [related-systems]`
- `status: current` unless clearly stale/outdated
- `last-checked: {today}`

Required sections:

- `## Core Ideas`
- `## Comparison with Our System`
- `## Borrowable Ideas`
- `## Curiosity Pass`
- `## What to Watch`

Write from the code outward:

- summarize what the system is
- identify 3-6 core mechanisms
- compare honestly with commonplace
- separate immediately borrowable ideas from ideas that need a use case
- use the Curiosity Pass to check for naming-vs-mechanism illusions

Every review should end with explicit `Relevant Notes:` links into the KB.

## Step 7: Update the Curated Index

If this is a new review, update `kb/notes/related-systems/related-systems-index.md`:

- add the system to the `## Systems` list
- update `## Patterns Across Systems` only if this repo adds a genuinely new cross-system pattern

Keep the edit minimal and specific.

## Step 8: Run Semantic Review as a QA Pass

Run the procedure from `kb/instructions/semantic-review.md` on the review note you just wrote.

Treat it as a read-only QA loop:

- extract the findings
- fix clearly valid issues in the review note
- if a finding is uncertain, prefer noting it in your final report rather than forcing a rewrite

Do not skip this step.

## Step 9: Run Final Validation

Run:

```text
/validate {note_path}
```

If validation reports structural or description-quality issues, fix them and validate once more.

## Output to the User

Report:

- repo cloned or reused
- review path
- whether the curated index changed
- semantic-review outcome (warnings/info if any)
- final `/validate` result

## Critical Constraints

**Always:**

- clone into `./related-systems/`
- write the review into `kb/notes/related-systems/`
- use the `related-system` template
- ground claims in repo code/docs, not just project marketing
- run semantic review before final validation
- finish with `/validate`

**Never:**

- put the checked-out repo under `kb/notes/related-systems/`
- skip reading the local writing/type guidance
- treat proposed docs as implemented behavior without checking the code
- leave the review unvalidated
