# Agent-memory-system-review instructions

Use this type for a **code-grounded** review of an external agent memory, knowledge, or context-engineering system, comparing it against commonplace.

**A reachable GitHub repository is required.** This type exists to capture what the reviewed system actually does, not what it claims. If the system is only documented via paper, README, or blog post without accessible source code, use the article-based review type instead — do not use this type. Abandoned repos are acceptable if the code is still readable.

**Topic argument.** The topic is a GitHub repository — either `owner/repo` or a full `https://github.com/owner/repo` URL.

- **New review (no existing note):** if no repo is given, ask. If the topic is not a GitHub repo reference, stop.
- **Update (note already exists):** resolve the repo URL from the existing review's frontmatter, the `**Repository:**` line, or the `[name](https://github.com/...)` link in the opening. If no repo URL is findable, stop and tell the user — this review may have been written against an article and belongs in a different type.

If the repo is unreachable (404, gone from GitHub), stop and report. Do not write or update a review of a system whose code you cannot read.

## Workflow

### 1. Normalize the repository target

Derive:

- `repo_url` — full GitHub URL
- `repo_name` — final path segment
- `checkout_dir` — `related-systems/{repo_name}/`
- `note_path` — `kb/agent-memory-systems/reviews/{repo_name}.md`

Use the repository name as the default review filename unless there is already an established house-style variant for the same system.

### 2. Check existing state

Before cloning or writing:

- Check whether `checkout_dir` already exists
- Check whether `note_path` already exists — if so, this is an **update**, not a new review (see update-mode notes below)
- Read `git status --short` in the main repo so you know whether the worktree is dirty

### 3. Read existing reviews for style

Read 1-2 existing reviews in `kb/agent-memory-systems/reviews/` to match local style and comparison depth. Also read `kb/agent-memory-systems/README.md`.

### 4. Clone or refresh the repo

If `checkout_dir` does not exist:

```bash
git clone "{repo_url}" "related-systems/{repo_name}"
```

If `checkout_dir` already exists, refresh it before reading so the review reflects current code:

```bash
cd "related-systems/{repo_name}"
git fetch --all --prune
git status --short
git pull --ff-only
```

If the pull cannot fast-forward (local commits or conflicts), do not force — report the state and ask the user. Do not delete or overwrite an existing checkout.

Gather orientation: top-level listing, most recent commit (`git log -1`), README, package/manifest files. Capture the reviewed commit SHA for citations:

```bash
git -C "related-systems/{repo_name}" rev-parse HEAD
```

When adding Markdown links to source files or directories, link to the reviewed GitHub commit, not the local checkout under `related-systems/`. Use `https://github.com/{owner}/{repo}/blob/{commit}/{path}` for files and `https://github.com/{owner}/{repo}/tree/{commit}/{path}` for directories. Local checkout paths are fine for your own inspection notes or final report, but review notes must remain readable on GitHub Pages.

### 5. Read for mechanism, not marketing

Ground the review in primary repo sources:

- `README.md`
- architecture/design docs
- `CLAUDE.md` / `AGENTS.md` if present
- package manifests and build metadata
- core source files implementing the repo's central claims

Do not rely only on the README if the implementation clarifies or contradicts it.

Focus on:

- storage model
- retrieval/navigation model
- learning/distillation/promotion model if any
- validation/governance model if any
- integration surface (CLI, MCP, API, editor plugin, etc.)
- what is genuinely implemented versus only proposed

### 6. Fill the template (new reviews)

Write from the code outward:

- **Opening paragraph:** what the system is, what it is for, who built it. Include the repository URL.
- **Repository metadata:** include `**Repository:** {URL}` and `**Reviewed commit:** {commit URL}` before the section headings.
- **Core Ideas:** 3-6 mechanisms and design choices, not feature lists. Use bolded lead phrases for scanning.
- **Comparison with Our System:** concrete alignments, divergences, and tradeoffs vs commonplace.
- **Borrowable Ideas:** the most important section. For each idea, say what it would look like in our system and whether it is ready now or needs a use case first.
- **Source citations:** when linking to repo code/docs, use commit-pinned GitHub links. Do not link to `../../../related-systems/...` or other local checkout paths.
- **Curiosity Pass:** second-pass review. Re-read the draft and look for surprising claims, simpler alternatives, and mechanisms that sound more powerful than they really are. For each strong claim in Core Ideas, ask:
  - what property does this produce?
  - does the mechanism transform the data, or just relocate it?
  - what simpler alternative might achieve the same result?
  - what could this mechanism actually achieve, even if it worked perfectly?
- **What to Watch:** future changes in the reviewed system that might affect our design.

Every review should end with explicit `Relevant Notes:` links into the KB.

### 6b. Update mode — replacing an existing review

When `note_path` already exists, archive the old review and write a fresh one. Do NOT diff or merge.

**Archive the existing review:**

```bash
git mv "{note_path}" "{note_path%.md}.replaced.{YYYY-MM-DD}.md"
```

For example: `kb/agent-memory-systems/reviews/ace.md` → `kb/agent-memory-systems/reviews/ace.replaced.2026-04-12.md`. Use today's ISO date.

Then mark the archived file so it isn't mistaken for a current review:
- Set `status: outdated` in the frontmatter
- Drop `tags: [related-systems, trace-derived]` to `tags: []` (removes it from indexes)
- Add a one-line note at the top of the body, right after the title: `> Replaced {YYYY-MM-DD}. See [{name}](./{name}.md) for the current review.`

**Then write a brand-new review at the original path** following the same workflow as a new review (steps 5-9). Do NOT read the archived `.replaced.*.md` file — the current code is the source of truth, and reading the prior review risks dragging stale claims or framing forward. The new review must be grounded in code, not in the prior reviewer's language.

The `.replaced.*.md` archive is not curated content — it's a frozen prior version that lets the operator inspect the change with `git diff` and recover any borrowable insights manually if they want to.

### 7. Required frontmatter

- `description` — discriminating retrieval filter (50-200 chars, double-quoted)
- `type: agent-memory-system-review`
- `tags: [related-systems]` — add `trace-derived` if the system learns from agent traces (see step 9)
- `status: current` unless clearly stale/outdated
- `last-checked: "{today}"`

### 8. Update the curated index

If this is a new review, update `kb/agent-memory-systems/index.md`:

- add the system to the `## Systems` list
- update `## Patterns Across Systems` only if this repo adds a genuinely new cross-system pattern

Keep the edit minimal and specific.

### 9. Trace-derived learning placement (when relevant)

Check whether the reviewed system learns from traces. Qualifying source traces: agent/assistant session logs, conversation transcripts, tool/action traces, event streams, repeated task trajectories, rollouts. Qualifying promotion targets: durable notes/rules/playbooks/lessons/memories or similar symbolic artifacts; model weights or other compiled runtime state derived from those traces.

If the system qualifies, add `trace-derived` to the frontmatter `tags` and include a `**Trace-derived learning placement.**` paragraph (bolded lead, not a heading) that addresses these questions:

1. **Trace source** — what raw signal is consumed (conversation logs, execution telemetry, task outcomes, environment feedback, trajectories)? With what trigger boundaries (per turn, per run, per tournament, per benchmark)?
2. **Extraction** — what gets pulled out (freeform reflections, episodic memories, playbooks, skills, code, lessons)? What oracle or judge decides what becomes signal?
3. **Promotion target** — does the system stop at inspectable artifacts, or promote into weights? Service-owned memory, or ephemeral?
4. **Scope** — per-task, per-benchmark, or cross-task generalizable?
5. **Timing** — online during deployment, offline from collected traces, or staged in cycles?

Then position the system on the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md): axis 1 (ingestion pattern) and axis 2 (artifact vs weights). State whether the system strengthens, weakens, or splits any claim in the survey, and whether it warrants a new subtype.

If the placement adds meaningfully to the survey (not a stub), update [`trace-derived-learning-techniques-in-related-systems.md`](../trace-derived-learning-techniques-in-related-systems.md) with the finding.

### 10. Run semantic review as a QA pass

Run the procedure from `kb/instructions/run-review-bundle-on-note.md` on the review note you just wrote, using the `semantic` bundle. Treat it as a read-only QA loop:

- extract the findings
- fix clearly valid issues in the review note
- if a finding is uncertain, prefer noting it in your final report rather than forcing a rewrite

Do not skip this step.

### 11. Final validation

Run `commonplace-validate-notes {note_path}`. If validation reports structural or description-quality issues, fix them and validate once more.

## Report

After finishing, tell the user:

- repo cloned or reused
- review path
- whether the curated index changed
- whether `trace-derived-learning-techniques-in-related-systems.md` was updated (if trace-derived placement applied)
- semantic gate bundle outcome (warnings/info if any)
- final `commonplace-validate-notes` result

## Constraints

**Always:**

- clone into `./related-systems/` (outside `kb/`)
- write the review into `kb/agent-memory-systems/reviews/`
- ground claims in repo code/docs, not just project marketing
- cite source files and directories with GitHub URLs pinned to the reviewed commit
- run semantic gate bundle before final validation

**Never:**

- put the checked-out repo under `kb/agent-memory-systems/reviews/`
- write Markdown links from review notes into `../../../related-systems/...` or other local checkout paths
- treat proposed docs as implemented behavior without checking the code
- leave the review unvalidated
- update `last-checked` without actually re-reading the system

## Maintenance

Update `last-checked` when you substantially re-review the system. Reviews become stale when:

- the reviewed system has had a major release or architectural change since `last-checked`
- our own system has evolved enough that the comparison section no longer reflects reality
- more than 3 months have passed without re-checking

Stale reviews should be updated or demoted to `status: outdated`. Don't delete — the comparison history has value even when details drift.
