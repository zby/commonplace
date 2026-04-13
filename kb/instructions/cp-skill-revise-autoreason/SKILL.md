---
name: cp-skill-revise-autoreason
description: "Experimental: revise a note with an AutoReason-style loop using fresh Codex sub-agents for critic, revision, synthesis, and blind judging. Keep the incumbent, generate a critique-driven revision and synthesis, then use blind Borda judging to decide whether to continue. Triggers on \"/cp-skill-revise-autoreason [note]\"."
user-invocable: true
allowed-tools: Read, Edit, Write, Bash, Glob, Grep, Task
argument-hint: <note-filename>
context: fork
model: opus
---

## EXECUTE NOW

**Target: $ARGUMENTS** (exactly one note path or filename - if empty, ask which note)

**Experimental.** This is the conservative note-revision adaptation of AutoReason, based on `related-systems/autoreason/`. Use it when you want to test the tournament workflow; prefer `cp-skill-revise-iterative` for the established revision path.

Each pass compares three versions:

- **A**: the unchanged incumbent for this pass.
- **B**: a revision motivated by a critic's identified problems.
- **AB**: a synthesis of A and B.

Three fresh judge agents rank blind candidate packets. Aggregate with Borda count. "Do nothing" is a first-class option: if A wins twice consecutively, stop.

## Step 0: Resolve The File

Resolve `$ARGUMENTS` to a full path. If it is a bare filename, search `kb/notes/` for a match. Read the file in full to confirm it exists and capture the original content.

Before running the loop, report the call budget: up to 5 passes, 6 fresh Codex sub-agents per pass (critic, revision author, synthesizer, 3 judges).

## Step 1: Initialize

Use a workshop directory so the original note remains untouched:

```bash
repo_root="$(pwd)"
run_dir="$repo_root/kb/reports/revise-autoreason/$(basename "${source_file}").$(date +%Y%m%d-%H%M%S)"
mkdir -p "$run_dir"
cp "$source_file" "$run_dir/original.md"
cp "$source_file" "$run_dir/current_a.md"
```

Set:

```text
pass=1
max_passes=5
incumbent_win_streak=0
last_good="$run_dir/current_a.md"
```

## Step 2: Revision Loop

Run until `pass > max_passes` or `incumbent_win_streak >= 2`.

### Actor Execution Protocol

Use fresh Codex sub-agents for actor work. The parent agent is the orchestrator: it resolves files, creates directories, builds blind packets, verifies outputs, aggregates rankings, performs the outer semantic fidelity check, and decides whether to apply any candidate. Do not use `claude -p`.

For each actor prompt below:

- Launch a new sub-agent. Do not reuse an actor across roles or passes.
- Give the sub-agent only the files and instructions it needs. For judges, do not include `judge_mappings.md`, A/B/AB labels, or any provenance.
- Prefer an unforked/minimal-context sub-agent when the harness supports that. If the harness exposes only forked workspaces, the sub-agent may write in its fork, but the parent must ensure the requested artifact exists in the parent run directory before continuing. If writeback is not automatic, have the sub-agent return the full artifact content and write it yourself.
- In each actor prompt, keep the requested file path explicit. If the actor cannot write that path in the parent workspace, it must return the complete artifact content instead of a summary.
- After each actor returns, use this handoff rule before verification: if the requested file exists and is non-empty in the parent workspace, continue; if it is missing but the actor returned the complete artifact, write that exact content to the requested path; if it is missing and the actor returned only a path or summary, rerun that actor once with the same prompt plus `Do not write a file; return the complete artifact content in your final response.`
- Wait for dependent actors in order: critic, B author, synthesizer. Run the three judges in parallel when the harness supports it.
- Close finished sub-agents when the harness requires explicit cleanup.

### 2a. Prepare The Pass Directory

```bash
pass_dir="$run_dir/pass_$(printf '%02d' "$pass")"
mkdir -p "$pass_dir/candidates" "$pass_dir/critic" "$pass_dir/author_b" "$pass_dir/synthesizer" "$pass_dir/judges"
cp "$run_dir/current_a.md" "$pass_dir/candidates/version_a.md"
```

### 2b. Run A Fresh Critic

Launch one fresh critic sub-agent with this prompt:

```text
Read $pass_dir/candidates/version_a.md. Write $pass_dir/critic/output.md.

You are the critic in an AutoReason-style note revision loop.

Find real editorial problems in the note. Focus on flow, readability, cohesion, duplicated material, unsupported transitions, and places where the argument is harder to follow than necessary.

Constraints:
- Do not suggest fixes.
- Do not ask to add new claims, evidence, tags, sections, or sources.
- Do not complain about material merely because it is specialized or terse.
- Treat semantic preservation as mandatory: the next agent may rewrite prose but must preserve all claims, evidence, caveats, and structure unless a structure change improves flow without changing the argument.
- Write only to $pass_dir/critic/output.md. Do not create or modify files outside $pass_dir.

Final response: name only `$pass_dir/critic/output.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete critic report content instead, with no extra commentary.
```

Verify that `$pass_dir/critic/output.md` exists and is non-empty. If it is missing or empty, stop and finalize with the last good version.

### 2c. Run A Fresh Revision Author For B

Launch one fresh B-author sub-agent with this prompt:

```text
Read $pass_dir/candidates/version_a.md and $pass_dir/critic/output.md. Write $pass_dir/author_b/version_b.md.

You are the B author in an AutoReason-style note revision loop.

Revise the note to address only valid problems identified in $pass_dir/critic/output.md.

Hard constraints:
- Preserve all semantic content, claims, evidence, caveats, qualifiers, and link targets.
- Preserve the note's overall argumentative structure unless a local reorder improves flow without changing the argument.
- Do not add new claims, examples, evidence, citations, or sources.
- Do not remove citations or source references.
- Do not change tags, type, status, or traits frontmatter fields.
- You may improve only the # heading and description frontmatter field if there is a clear improvement.
- Output the complete note, including frontmatter.
- Write only to $pass_dir/author_b/version_b.md. Do not create or modify files outside $pass_dir.

Write only $pass_dir/author_b/version_b.md. Do not modify $pass_dir/candidates/version_a.md or $pass_dir/critic/output.md.

Final response: name only `$pass_dir/author_b/version_b.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete revised note content instead, with no extra commentary.
```

Verify that `$pass_dir/author_b/version_b.md` exists and is non-empty. If it is missing or empty, stop and finalize with the last good version.

### 2d. Run A Fresh Synthesizer For AB

Launch one fresh synthesizer sub-agent with this prompt:

```text
Read $pass_dir/candidates/version_a.md and $pass_dir/author_b/version_b.md. Write $pass_dir/synthesizer/version_ab.md.

You are the AB synthesizer in an AutoReason-style note revision loop.

Treat A and B as equal inputs. Produce one coherent note that keeps the strongest wording and organization from each. This is not a compromise: choose the better version per passage or section.

Hard constraints:
- Preserve all semantic content, claims, evidence, caveats, qualifiers, and link targets from the incumbent A.
- Do not add new claims, examples, evidence, citations, or sources.
- Do not remove citations or source references.
- Do not change tags, type, status, or traits frontmatter fields.
- You may improve only the # heading and description frontmatter field if there is a clear improvement.
- Output the complete note, including frontmatter.
- Write only to $pass_dir/synthesizer/version_ab.md. Do not create or modify files outside $pass_dir.

Write only $pass_dir/synthesizer/version_ab.md. Do not modify $pass_dir/candidates/version_a.md or $pass_dir/author_b/version_b.md.

Final response: name only `$pass_dir/synthesizer/version_ab.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete synthesized note content instead, with no extra commentary.
```

Verify that `$pass_dir/synthesizer/version_ab.md` exists and is non-empty. If it is missing or empty, stop and finalize with the last good version.

### 2e. Build Blind Judge Packets

Create three judge packets with balanced label order. Do not expose A/B/AB names to the judges.

Use these default mappings unless you deliberately randomize and record an equivalent mapping:

```text
judge_1: 1=A,  2=B,  3=AB
judge_2: 1=AB, 2=A,  3=B
judge_3: 1=B,  2=AB, 3=A
```

Copy candidate files into `$pass_dir/judges/judge_<n>_candidate_<m>.md` according to the mapping, and write the mapping to `$pass_dir/judges/judge_mappings.md`.

```bash
cp "$pass_dir/candidates/version_a.md"      "$pass_dir/judges/judge_1_candidate_1.md"
cp "$pass_dir/author_b/version_b.md"        "$pass_dir/judges/judge_1_candidate_2.md"
cp "$pass_dir/synthesizer/version_ab.md"    "$pass_dir/judges/judge_1_candidate_3.md"

cp "$pass_dir/synthesizer/version_ab.md"    "$pass_dir/judges/judge_2_candidate_1.md"
cp "$pass_dir/candidates/version_a.md"      "$pass_dir/judges/judge_2_candidate_2.md"
cp "$pass_dir/author_b/version_b.md"        "$pass_dir/judges/judge_2_candidate_3.md"

cp "$pass_dir/author_b/version_b.md"        "$pass_dir/judges/judge_3_candidate_1.md"
cp "$pass_dir/synthesizer/version_ab.md"    "$pass_dir/judges/judge_3_candidate_2.md"
cp "$pass_dir/candidates/version_a.md"      "$pass_dir/judges/judge_3_candidate_3.md"

printf "judge_1: 1=A, 2=B, 3=AB\njudge_2: 1=AB, 2=A, 3=B\njudge_3: 1=B, 2=AB, 3=A\n" > "$pass_dir/judges/judge_mappings.md"
```

### 2f. Run Three Fresh Judges

For each judge `n` in `1 2 3`, launch a separate fresh judge sub-agent. Run the three judge sub-agents in parallel when the harness supports it.

Use this prompt for judge `${n}`:

```text
Read $pass_dir/judges/judge_${n}_candidate_1.md, $pass_dir/judges/judge_${n}_candidate_2.md, and $pass_dir/judges/judge_${n}_candidate_3.md. Write $pass_dir/judges/judge_${n}.md.

You are an independent judge. You have no authorship stake in any version. You are evaluating three anonymized revisions of the same KB note.

Rank the candidates by:
1. Apparent semantic safety: no internal contradictions, invented-looking evidence, broken links, suspicious frontmatter changes, or signs that caveats/qualifiers were flattened. You do not have the original baseline, so do not try to infer which candidate is the incumbent.
2. Editorial quality: flow, readability, cohesion, precision, and absence of filler.
3. Conservative restraint: do not reward changes merely because they are more extensive.

For each candidate, briefly state what it gets right and what it gets wrong. Then end with exactly:

RANKING: [best], [second], [worst]

Where each slot is 1, 2, or 3.

Write only $pass_dir/judges/judge_${n}.md. Do not create or modify files outside $pass_dir.

Final response: name only `$pass_dir/judges/judge_${n}.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete judge report content instead, with no extra commentary.
```

If a judge output is missing, empty, or lacks a parseable `RANKING:` line containing all of `1`, `2`, and `3` exactly once, rerun that judge once. If fewer than two judges are valid after the rerun, stop and finalize with the last good version.

### 2g. Aggregate With Borda Count

Map judge labels back to A, B, and AB with `$pass_dir/judges/judge_mappings.md`.

Score each valid ranking:

```text
first: 3 points
second: 2 points
third: 1 point
```

Break ties conservatively:

```text
A > AB > B
```

Write `$pass_dir/result.md` with:

- Valid judge count
- Each parsed ranking after remapping
- Borda scores for A, B, and AB
- Winner
- Tie-break, if used

### 2h. Outer Semantic Fidelity Check

If the winner is B or AB, compare the winning file against `$run_dir/current_a.md`.

Reject the winner and stop if it:

- Changes the meaning of any claim
- Drops or adds substantive content
- Alters evidence, caveats, qualifiers, or link targets in a meaning-changing way
- Removes sections or merges distinct points in a damaging way
- Changes tags, type, status, or traits frontmatter fields

If rejected:

- Record the exact before/after problem in `$pass_dir/result.md`.
- Do not apply the rejected candidate.
- Finalize with `last_good`.

If accepted, copy the winning file (`$pass_dir/author_b/version_b.md` for B, `$pass_dir/synthesizer/version_ab.md` for AB) to `$run_dir/current_a.md`, set `last_good="$run_dir/current_a.md"`, and reset `incumbent_win_streak=0`.

If the winner is A, leave `$run_dir/current_a.md` unchanged and increment `incumbent_win_streak`.

### 2i. Title And Description Change Detection

Compare the `# Title` heading and `description:` frontmatter field between the original note and `$run_dir/current_a.md`. If either changed, record the before/after values in `$run_dir/summary.md`. These are not errors.

### 2j. Continue Or Stop

If `incumbent_win_streak >= 2`, stop: the incumbent survived two consecutive challenges.

Otherwise increment `pass` and repeat Step 2.

## Step 3: Finalize

The best version is `last_good`.

1. Show a diff summary between the original file and `last_good`; list the key changes across all accepted passes.
2. Report the AutoReason trajectory: pass winners, Borda scores, and final pass count.
3. If the title or description changed, report it explicitly with before/after values.
4. Ask the user: "Apply these changes to `${source_file}`? (The AutoReason run bundle will be cleaned up unless you ask to keep it.)"
5. If the user approves:
   - Copy `last_good` over the original file.
   - If the title changed and the new title implies a different filename, derive the new filename using the KB convention (lowercase, hyphens, derived from `# Title`), rename with `git mv`, and update markdown links across `kb/`.
   - Delete the run bundle unless the user asked to keep it.
6. If the user declines:
   - Leave the original untouched.
   - Delete the run bundle unless the user asked to keep it.

## Constraints

**Never:**

- Modify the original file until the user explicitly approves.
- Let more than 5 passes run.
- Accept a candidate that introduces semantic errors.
- Change tags, type, status, or traits frontmatter fields.
- Let judge preference replace the outer semantic fidelity check.
- Expose A/B/AB provenance to judges.

**Always:**

- Keep A as a first-class candidate.
- Use fresh sub-agents for critic, B author, synthesizer, and each judge.
- Aggregate valid judge rankings with Borda count and conservative tie-breaks.
- Report the trajectory and final pass count.
- Bail out early if required candidate or judge outputs fail.
