---
name: revise-iterative
description: Iteratively revise a note for flow, readability, and cohesion using non-interactive Claude calls. Each pass produces a numbered copy; the outer agent reviews for semantic fidelity and significance before continuing. Triggers on "/revise-iterative [note]".
user-invocable: true
allowed-tools: Read, Edit, Bash, Glob, Grep
argument-hint: <note-filename>
context: fork
model: opus
---

## EXECUTE NOW

**Target: $ARGUMENTS** (exactly one note path or filename — if empty, ask which note)

### Step 0: Resolve the file

Resolve `$ARGUMENTS` to a full path. If it's a bare filename, search `kb/notes/` for a match. Read the file to confirm it exists and capture the original content.

### Step 1: Initialize

```
i=0
source_file=<resolved path>
```

Copy the original to `${source_file}.0` — this is the baseline for the first revision pass.

### Step 2: Revision loop

Run the following loop. **Max iterations: 5** (hard cap to prevent runaway).

#### 2a. Run non-interactive revision

```bash
claude -p "Revise $(basename ${source_file}).$i for flow, readability, and cohesion. Preserve all semantic content, claims, and structure. You MAY improve the title (# heading) and description frontmatter field if you see a clear improvement — but do not change tags, type, status, or traits. Focus on: sentence-level clarity, paragraph transitions, removing filler, tightening prose." \
  --allowedTools "Read,Edit,Write" \
  --max-turns 10
```

Run this from the directory containing the file so relative paths work.

#### 2b. Verify the revision happened

Read `${source_file}.$i` after the claude call. If the file is unchanged from before the call (content identical to pre-call state), the revision failed — report the failure and bail out. Do not increment or retry.

#### 2c. Semantic fidelity check

Compare `${source_file}.$i` (revised) against the previous version (`${source_file}.$((i-1))` for i>0, or the original `${source_file}` for i=0).

Check for:

1. **Semantic errors** — Did the revision change the meaning of any claim? Did it drop or add substantive content? Did it alter evidence, caveats, or qualifiers in ways that change the argument?
2. **Structural damage** — Did it remove sections, reorder arguments in ways that break logical flow, or merge distinct points?
3. **Frontmatter integrity** — Are tags, type, status, and traits unchanged? (Title and description MAY change — see 2e.)

If ANY semantic error or structural damage is found:
- Report exactly what went wrong (quote the before/after for the problematic passage)
- **Do not apply this revision** — the last good version is `${source_file}.$((i-1))` (or the original if i=0)
- Skip to Step 3 (finalize) using the last good version

#### 2d. Title and description change detection

Compare the `# Title` heading and `description:` frontmatter field between the current and previous version. If either changed, **flag it** — record the before/after values. These are not errors; they will be reported to the user in Step 3. Do not reject a revision solely because it changed the title or description.

#### 2e. Significance check

Assess whether the changes in this pass are **significant** — meaningful improvements to flow, readability, or cohesion beyond trivial whitespace or punctuation.

- If changes are significant: increment `i`, copy `${source_file}.$i` to `${source_file}.$((i+1))`, and loop back to 2a.
- If changes are minor or negligible: this version is good enough. Stop looping and proceed to Step 3.

**Note:** When copying to the next iteration file, always copy the current `${source_file}.$i` (not the original).

### Step 3: Finalize

The best version is the last file that passed the semantic fidelity check.

1. Show a **diff summary** between the original file and the best version — list the key changes made across all passes.
2. If the title or description changed, **report it explicitly** — show before/after for each.
3. Ask the user: "Apply these changes to `${source_file}`? (The intermediate files will be cleaned up either way.)"
4. If the user approves:
   - Copy the best version over the original file
   - **If the title changed** and the new title implies a different filename (per KB convention: lowercase, hyphens, derived from `# Title`):
     - Derive the new filename from the new title
     - Rename the file: `git mv ${source_file} ${new_filename}`
     - Find all markdown links pointing to the old filename across `kb/` and update them to the new filename
     - Report which files had links updated
   - Delete all intermediate files (`${source_file}.0`, `${source_file}.1`, etc.)
5. If the user declines:
   - Leave the original untouched
   - Delete all intermediate files

## Constraints

**Never:**
- Modify the original file until the user explicitly approves
- Let more than 5 iterations run
- Accept a revision that introduces semantic errors — always prefer the previous version
- Change tags, type, status, or traits frontmatter fields
- Skip the semantic fidelity check

**Always:**
- Show the user what changed before applying
- Clean up intermediate files regardless of outcome
- Report which iteration produced the final version
- Bail out early if a revision fails or introduces errors
