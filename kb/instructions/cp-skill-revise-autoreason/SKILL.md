---
name: cp-skill-revise-autoreason
description: "Experimental: revise a note with an AutoReason-style loop using fresh Codex sub-agents for critic, revision, synthesis, and blind judging. Keep the incumbent, generate a critique-driven revision and synthesis, then use blind Borda judging to decide whether to continue. Triggers on \"/cp-skill-revise-autoreason [note]\"."
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Write, Bash, Glob, Grep, Task
argument-hint: <note-filename>
context: fork
model: opus
---

## EXECUTE NOW

**Target: $ARGUMENTS** (exactly one note path or filename - if empty, ask which note)

**Experimental.** This is the conservative note-revision adaptation of AutoReason, based on `related-systems/autoreason/`. Use it when you want to test the tournament workflow; prefer `cp-skill-revise-iterative` for the established revision path.

This skill defaults to prose-preserving revision, but it may produce a separate substantive-revision sidecar when the revisions reveal that claim, evidence, source, or argument changes are actually needed. Keep that sidecar out of the B/AB blind tournament and never auto-apply it.

Each pass compares three versions:

- **A**: the unchanged incumbent for this pass.
- **B**: a revision motivated by a critic's identified problems.
- **AB**: a synthesis of A and B.

Three fresh judge agents rank blind candidate packets. Aggregate with Borda count. "Do nothing" is a first-class option: if A wins twice consecutively, stop.

## Step 0: Resolve The File

Resolve `$ARGUMENTS` to a full path. If it is a bare filename, search `kb/notes/` for a match. Read the file in full to confirm it exists and capture the original content.

Before running the loop, report the call budget: up to 5 passes. A normal pass uses 7 fresh Codex sub-agents (critic, revision author, synthesizer, post-candidate auditor, 3 judges). Early stops may use fewer, bounded reruns may use more, and the substantive-revision sidecar uses one additional sub-agent when triggered.

## Step 1: Initialize

Use a workshop directory so the original note remains untouched:

```bash
repo_root="$(pwd)"
run_dir="$repo_root/kb/work/revise-autoreason/$(basename "${source_file}").$(date +%Y%m%d-%H%M%S)"
mkdir -p "$run_dir"
cp "$source_file" "$run_dir/original.md"
cp "$source_file" "$run_dir/current_a.md"
```

The workflow makes substantive editorial changes. Remove `user-verified: true` from `$run_dir/current_a.md` if present and require every candidate to keep it absent. Applying a winning candidate therefore revokes the prior attestation; only a later explicit human action may restore it.

Set:

```text
pass=1
max_passes=5
incumbent_win_streak=0
last_good="$run_dir/current_a.md"
claim_revision_needed=false
claim_revision_file=""
claim_revision_artifact=""
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
- Wait for dependent actors in order: critic, B author, synthesizer, post-candidate auditor. Run parent-side hard-constraint checks before spawning downstream actors that depend on a generated candidate. Run the three judges in parallel when the harness supports it.
- After each actor returns and its handoff is verified, close, terminate, or release that sub-agent with the harness lifecycle operation. Actors are single-use: never retain one for another role, pass, rerun, or follow-up. Close all three judges after collecting their outputs and before aggregation.

### Claim-Revision Sidecar

Use this sidecar when the best next edit would need to change claims, evidence, caveats, qualifiers, source usage, or argumentative commitments. Do not let that change enter the AutoReason candidate tournament, but do produce a useful artifact for the user to review.

When triggered:

1. Write `$pass_dir/substantive/claim_revision_reason.md` with the exact reason, including before/after snippets if a candidate exposed the issue, and set `claim_revision_file="$pass_dir/substantive/claim_revision_reason.md"`.
2. Launch one fresh substantive-revision sub-agent with the prompt below.
3. Append a line to `$pass_dir/result.md`: `Escalation: claim revision needed`.
4. Set `claim_revision_needed=true`.
5. Stop the AutoReason loop and finalize with `last_good` unchanged.
6. In Step 3, report the sidecar artifact path and ask whether to keep the run bundle for review. Do not ask to apply `last_good` if it is identical to the original.

Substantive-revision prompt:

```text
Read $pass_dir/candidates/version_a.md, $claim_revision_file, and any existing candidate files in $pass_dir/author_b/ and $pass_dir/synthesizer/. Write either $pass_dir/substantive/version_claim_revision.md or $pass_dir/substantive/claim_revision_plan.md.

You are the substantive-revision sidecar in an AutoReason-style note revision loop. This artifact is outside the blind prose tournament.

Goal:
- If the needed claim/evidence/caveat/source/argument correction can be made using only information already present in the note, critic report, and candidate files, write a complete revised note to $pass_dir/substantive/version_claim_revision.md.
- If the correction would require new evidence, external source review, or a human decision about what the note should claim, write a concrete plan to $pass_dir/substantive/claim_revision_plan.md instead.

Constraints:
- Do not invent evidence or citations.
- Do not change tags, type, or traits frontmatter fields unless the plan explicitly says a metadata follow-up is needed.
- Preserve link targets unless the reason file identifies a target that must change.
- If writing a complete revised note, include full frontmatter and the complete body.
- If writing a plan, list the exact claim/evidence/source decisions needed and the passages they affect.
- Write only under $pass_dir/substantive/. Do not create or modify files outside $pass_dir.

Final response: name the artifact you wrote. If you cannot write into the parent workspace, return the complete artifact content and the intended target path, with no extra commentary.
```

After the sub-agent returns, use the normal handoff rule. Set `claim_revision_artifact` to whichever of `$pass_dir/substantive/version_claim_revision.md` or `$pass_dir/substantive/claim_revision_plan.md` exists and is non-empty. If neither exists and the returned artifact cannot be recovered, keep `claim_revision_artifact=""` and report only `$claim_revision_file`.

### 2a. Prepare The Pass Directory

```bash
pass_dir="$run_dir/pass_$(printf '%02d' "$pass")"
mkdir -p "$pass_dir/candidates" "$pass_dir/critic" "$pass_dir/author_b" "$pass_dir/synthesizer" "$pass_dir/auditor" "$pass_dir/substantive" "$pass_dir/judges"
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
- If you find a problem whose correct fix would require changing claims, evidence, caveats, qualifiers, source usage, or argumentative commitments, write a section titled `Claim revision needed` that states the problem and why prose-preserving revision is insufficient. Do not propose the replacement claim.
- Write only to $pass_dir/critic/output.md. Do not create or modify files outside $pass_dir.

Final response: name only `$pass_dir/critic/output.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete critic report content instead, with no extra commentary.
```

Verify that `$pass_dir/critic/output.md` exists and is non-empty. If it is missing or empty, stop and finalize with the last good version.

If `$pass_dir/critic/output.md` contains `Claim revision needed`, trigger the claim-revision sidecar immediately. Do not run B author, synthesizer, judge packets, judges, or aggregation.

Read `$pass_dir/critic/output.md`. If it identifies no concrete, actionable editorial problem, write `$pass_dir/result.md` with `Winner: A`, `Reason: critic found no actionable problem`, and `Borda: not run`, then skip B author, synthesizer, judge packets, judges, and aggregation. Leave `$run_dir/current_a.md` unchanged, increment `incumbent_win_streak`, and continue at title/description change detection.

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
- Do not change tags, type, or traits frontmatter fields.
- You may improve only the # heading and description frontmatter field if there is a clear improvement.
- Output the complete note, including frontmatter.
- Write only to $pass_dir/author_b/version_b.md. Do not create or modify files outside $pass_dir.

Write only $pass_dir/author_b/version_b.md. Do not modify $pass_dir/candidates/version_a.md or $pass_dir/critic/output.md.

Final response: name only `$pass_dir/author_b/version_b.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete revised note content instead, with no extra commentary.
```

Verify that `$pass_dir/author_b/version_b.md` exists and is non-empty. If it is missing or empty, stop and finalize with the last good version.

Before running the synthesizer, perform a parent-side hard-constraint check of B against `$pass_dir/candidates/version_a.md`. Reject B before synthesis if it:

- Changes `tags`, `type`, or `traits` frontmatter fields, or adds `user-verified`.
- Removes citations, source references, or link targets.
- Fails to output the complete note including frontmatter.
- Obviously adds or drops substantive claims, evidence, caveats, qualifiers, or sections.

If B fails this check, decide whether the violation is accidental semantic drift or a plausible sign that prose-preserving revision is insufficient:

- If it looks like accidental drift, record the exact problem in `$pass_dir/candidate_checks.md` and rerun the B-author sub-agent once with the same prompt plus the recorded problem and `Return a complete corrected note that fixes this violation without adding new content.` Replace `$pass_dir/author_b/version_b.md` with the rerun output and repeat this hard-constraint check. If B still fails from accidental drift, stop and finalize with the last good version.
- If the violation looks like a necessary claim, evidence, caveat, qualifier, source, or argument correction, trigger the claim-revision sidecar instead of rerunning B.

If B passes, continue.

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
- Do not change tags, type, or traits frontmatter fields.
- You may improve only the # heading and description frontmatter field if there is a clear improvement.
- Output the complete note, including frontmatter.
- Write only to $pass_dir/synthesizer/version_ab.md. Do not create or modify files outside $pass_dir.

Write only $pass_dir/synthesizer/version_ab.md. Do not modify $pass_dir/candidates/version_a.md or $pass_dir/author_b/version_b.md.

Final response: name only `$pass_dir/synthesizer/version_ab.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete synthesized note content instead, with no extra commentary.
```

Verify that `$pass_dir/synthesizer/version_ab.md` exists and is non-empty. If it is missing or empty, stop and finalize with the last good version.

Before building blind judge packets, perform a parent-side hard-constraint check of AB against `$pass_dir/candidates/version_a.md` using the same criteria as the B check. If AB fails, decide whether the violation is accidental semantic drift or a plausible sign that prose-preserving revision is insufficient:

- If it looks like accidental drift, record the exact problem in `$pass_dir/candidate_checks.md` and rerun the synthesizer sub-agent once with the same prompt plus the recorded problem and `Return a complete corrected note that fixes this violation without adding new content.` Replace `$pass_dir/synthesizer/version_ab.md` with the rerun output and repeat this hard-constraint check. If AB still fails from accidental drift, stop and finalize with the last good version.
- If the violation looks like a necessary claim, evidence, caveat, qualifier, source, or argument correction, trigger the claim-revision sidecar instead of rerunning AB.

If AB passes, continue.

### 2e. Run A Post-Candidate Auditor

Launch one fresh auditor sub-agent with this prompt:

```text
Read $pass_dir/candidates/version_a.md, $pass_dir/critic/output.md, $pass_dir/author_b/version_b.md, and $pass_dir/synthesizer/version_ab.md. Write $pass_dir/auditor/output.md.

You are the post-candidate auditor in an AutoReason-style note revision loop. You are not a judge. Do not rank A, B, or AB.

You now have more evidence than the initial critic: the incumbent A, the critic's concerns, the B revision, and the AB synthesis. Decide whether the tournament should proceed to blind judging.

Check for:
- Hard-constraint violations in B or AB: changed tags/type/traits, missing frontmatter, removed citations or link targets, added or dropped substantive claims, flattened caveats or qualifiers, changed evidence, or damaged section structure.
- Evidence that prose-preserving revision is the wrong task because the note appears to need claim, evidence, caveat, qualifier, source, or argument correction.

Write exactly one decision line:

DECISION: PASS
DECISION: RERUN_B
DECISION: RERUN_AB
DECISION: CLAIM_REVISION_NEEDED
DECISION: REJECT

Use PASS only if B and AB are viable for blind judging.
Use RERUN_B only for accidental semantic drift in B; if B is rerun, AB must be regenerated from the corrected B.
Use RERUN_AB only for accidental semantic drift in AB while B remains viable.
Use CLAIM_REVISION_NEEDED when the hard rule itself appears to be the wrong task boundary.
Use REJECT only when a candidate is invalid but the problem is not worth a rerun and does not suggest claim revision.

After the decision line, briefly state the exact evidence. If citing a violation, include before/after snippets where practical.

Write only $pass_dir/auditor/output.md. Do not create or modify files outside $pass_dir.

Final response: name only `$pass_dir/auditor/output.md` if you wrote it successfully. If you cannot write that file in the parent workspace, return the complete auditor report content instead, with no extra commentary.
```

Verify that `$pass_dir/auditor/output.md` exists, is non-empty, and has exactly one parseable `DECISION:` line. If it is missing, empty, or unparseable, rerun the auditor once. If it still fails, stop and finalize with the last good version.

Handle the auditor decision before building judge packets:

- `PASS`: continue.
- `CLAIM_REVISION_NEEDED`: trigger the claim-revision sidecar.
- `REJECT`: stop and finalize with the last good version.
- `RERUN_B`: rerun the B-author sub-agent once using the original B prompt plus the auditor's exact evidence and `Return a complete corrected note that fixes this violation without adding new content.` Replace `$pass_dir/author_b/version_b.md` with the rerun output. Then rerun the synthesizer once from the corrected B, replace `$pass_dir/synthesizer/version_ab.md`, rerun the parent-side B and AB checks, and rerun this post-candidate auditor once. If the auditor does not return `PASS`, stop with either the claim-revision sidecar for `CLAIM_REVISION_NEEDED` or `last_good` for any other decision.
- `RERUN_AB`: rerun the synthesizer sub-agent once using the original synthesizer prompt plus the auditor's exact evidence and `Return a complete corrected note that fixes this violation without adding new content.` Replace `$pass_dir/synthesizer/version_ab.md` with the rerun output. Then rerun the parent-side AB check and rerun this post-candidate auditor once. If the auditor does not return `PASS`, stop with either the claim-revision sidecar for `CLAIM_REVISION_NEEDED` or `last_good` for any other decision.

### 2f. Build Blind Judge Packets

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

### 2g. Run Three Fresh Judges

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

### 2h. Aggregate With Borda Count

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

### 2i. Outer Semantic Fidelity Check

If the winner is B or AB, compare the winning file against `$run_dir/current_a.md`.

Reject the winner and stop if it:

- Changes the meaning of any claim
- Drops or adds substantive content
- Alters evidence, caveats, qualifiers, or link targets in a meaning-changing way
- Removes sections or merges distinct points in a damaging way
- Changes tags, type, or traits frontmatter fields

If rejected:

- Record the exact before/after problem in `$pass_dir/result.md`.
- Do not apply the rejected candidate.
- If the semantic change looks like a necessary claim, evidence, caveat, qualifier, source, or argument correction, trigger the claim-revision sidecar.
- Otherwise finalize with `last_good`.

If accepted, copy the winning file (`$pass_dir/author_b/version_b.md` for B, `$pass_dir/synthesizer/version_ab.md` for AB) to `$run_dir/current_a.md`, set `last_good="$run_dir/current_a.md"`, and reset `incumbent_win_streak=0`.

If the winner is A, leave `$run_dir/current_a.md` unchanged and increment `incumbent_win_streak`.

### 2j. Title And Description Change Detection

Compare the `# Title` heading and `description:` frontmatter field between the original note and `$run_dir/current_a.md`. If either changed, record the before/after values in `$run_dir/summary.md`. These are not errors.

### 2k. Continue Or Stop

If `incumbent_win_streak >= 2`, stop: the incumbent survived two consecutive challenges.

Otherwise increment `pass` and repeat Step 2.

## Step 3: Finalize

The best version is `last_good`.

1. Show a diff summary between the original file and `last_good`; list the key changes across all accepted passes.
2. Report the AutoReason trajectory: pass winners, Borda scores or skip reasons, and final pass count.
3. If `claim_revision_needed=true`, report the reason from `$claim_revision_file` and the sidecar artifact path from `$claim_revision_artifact` if present. Leave the original untouched and ask whether to keep the run bundle for substantive-revision review. Do not apply AutoReason changes automatically. Skip the remaining apply/decline steps.
4. If the title or description changed, report it explicitly with before/after values.
5. Ask the user: "Apply these changes to `${source_file}`? (The AutoReason run bundle will be cleaned up unless you ask to keep it.)"
6. If the user approves:
   - Copy `last_good` over the original file.
   - If the title changed and the new title implies a different filename, derive the new filename using the KB convention (lowercase, hyphens, derived from `# Title`), rename with `git mv`, and update markdown links across `kb/`.
   - Delete the run bundle unless the user asked to keep it.
7. If the user declines:
   - Leave the original untouched.
   - Delete the run bundle unless the user asked to keep it.

## Constraints

**Never:**

- Modify the original file until the user explicitly approves.
- Let more than 5 passes run.
- Accept a candidate that introduces semantic errors.
- Force a claim-level correction through the prose-preserving tournament path.
- Change tags, type, or traits frontmatter fields.
- Let judge preference replace the outer semantic fidelity check.
- Expose A/B/AB provenance to judges.

**Always:**

- Keep A as a first-class candidate.
- Use fresh sub-agents for critic, B author, synthesizer, post-candidate auditor, each judge, and any rerun.
- Run hard-constraint checks before blind judging so judges only rank viable candidates.
- Trigger the claim-revision sidecar when the hard rule itself is the wrong task boundary.
- Aggregate valid judge rankings with Borda count and conservative tie-breaks when judges run.
- Report the trajectory and final pass count.
- Bail out early if required candidate or judge outputs fail.
