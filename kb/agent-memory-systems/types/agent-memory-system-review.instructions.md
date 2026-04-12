# Agent-memory-system-review instructions

Use this type for a code-grounded review of an external agent memory, knowledge, or context-engineering system, comparing it against commonplace.

**Topic argument.** The topic for this type is a GitHub repository — either `owner/repo` or a full `https://github.com/owner/repo` URL. If no repo is given, ask for one. If the topic is not a GitHub repo reference, stop and say this type only accepts GitHub repositories.

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

- Check whether `checkout_dir` already exists — reuse if so, never delete or overwrite
- Check whether `note_path` already exists — if so, treat this as an update
- Read `git status --short` so you know whether the worktree is dirty

### 3. Read existing reviews for style

Read 1-2 existing reviews in `kb/agent-memory-systems/reviews/` to match local style and comparison depth. Also read `kb/agent-memory-systems/README.md`.

### 4. Clone the repo

If `checkout_dir` does not exist:

```bash
git clone "{repo_url}" "related-systems/{repo_name}"
```

Gather quick orientation: top-level listing, most recent commit (`git log -1`), README, package/manifest files.

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

### 6. Fill the template

Write from the code outward:

- **Opening paragraph:** what the system is, what it is for, who built it. Include the repository URL.
- **Core Ideas:** 3-6 mechanisms and design choices, not feature lists. Use bolded lead phrases for scanning.
- **Comparison with Our System:** concrete alignments, divergences, and tradeoffs vs commonplace.
- **Borrowable Ideas:** the most important section. For each idea, say what it would look like in our system and whether it is ready now or needs a use case first.
- **Curiosity Pass:** second-pass review. Re-read the draft and look for surprising claims, simpler alternatives, and mechanisms that sound more powerful than they really are. For each strong claim in Core Ideas, ask:
  - what property does this produce?
  - does the mechanism transform the data, or just relocate it?
  - what simpler alternative might achieve the same result?
  - what could this mechanism actually achieve, even if it worked perfectly?
- **What to Watch:** future changes in the reviewed system that might affect our design.

Every review should end with explicit `Relevant Notes:` links into the KB.

### 7. Required frontmatter

- `description` — discriminating retrieval filter (50-200 chars, double-quoted)
- `type: agent-memory-system-review`
- `tags: [related-systems]` — add `trace-derived` if the system learns from agent traces (see step 9)
- `status: current` unless clearly stale/outdated
- `last-checked: "{today}"`

### 8. Update the curated index

If this is a new review, update `kb/agent-memory-systems/related-systems-index.md`:

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
- run semantic gate bundle before final validation

**Never:**

- put the checked-out repo under `kb/agent-memory-systems/reviews/`
- treat proposed docs as implemented behavior without checking the code
- leave the review unvalidated
- update `last-checked` without actually re-reading the system

## Maintenance

Update `last-checked` when you substantially re-review the system. Reviews become stale when:

- the reviewed system has had a major release or architectural change since `last-checked`
- our own system has evolved enough that the comparison section no longer reflects reality
- more than 3 months have passed without re-checking

Stale reviews should be updated or demoted to `status: outdated`. Don't delete — the comparison history has value even when details drift.
