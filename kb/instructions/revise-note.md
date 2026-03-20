---
description: Editorial revision of a single KB note — rewrites for logic, flow, and cohesion. Reads linked notes for context. Edits the file in place and reports changes.
---

# Revise Note

**Target: $NOTE_PATH**

## What this is

A content-level editorial pass on a single note. You may rewrite sentences, reorder paragraphs, cut redundant material, tighten arguments, and fix logical gaps. The goal is a note that reads as a coherent, well-structured argument — not a draft with bolt-on additions.

## Scope

- **In scope:** everything about the target note itself. This includes the full file contents, all frontmatter fields, the title, footer sections such as Sources and Relevant Notes, and the filename.
- **Out of scope:** changes outside the target note during the main revision pass. Do not edit other notes, indexes, instructions, or generated listings until the revision step is complete. If revising the note exposes needed follow-up changes elsewhere, handle them only in the separate follow-up step below.

## Steps

1. **Read the target note in full.**

2. **Read linked notes for context.** Follow links in the body and Relevant Notes section. Read enough to understand what the target note is building on and what it commits to. Cap at 8 linked notes — prioritise notes the target depends on (marked "foundation," "grounds," "mechanism") over notes that depend on it.

3. **Assess.** Before editing, identify:
   - Logical gaps: claims that don't follow from what precedes them.
   - Redundancy: the same point made twice in different words.
   - Flow breaks: sections that don't connect to their neighbours.
   - Cohesion failures: terms used inconsistently, or framing that shifts mid-note.
   - Unsupported transitions: "therefore" or "this means" without the intermediate step.
   - Throat-clearing: sentences that concede an obvious point just to set up a contrast ("Nobody doubts X. But Y…"). Cut them — the reader already accepts X; go straight to Y.

4. **Revise.** Edit the file in place. You may:
   - Rewrite sentences and paragraphs.
   - Reorder sections if the argument flows better.
   - Cut material that is redundant or doesn't serve the note's claim.
   - Add bridging sentences where logical gaps exist.
   - Sharpen vague language into precise claims.
   - Merge or split sections.
   - Revise frontmatter, title, footer sections, and filename when needed to improve the note as a whole.

   Do NOT:
   - Change the note into a substantively different note than the one you started with.
   - Add new claims or evidence not already present or implied by the existing text.
   - Remove citations or source references from the body.
   - Edit files outside the target note as part of the main revision pass.

5. **Handle tag changes as a separate follow-up.** If you changed `tags`, spawn a sub-agent after the main revision is complete. The sub-agent should inspect nearby notes, indexes, and workflows affected by the tag change, make the minimal external edits needed to keep those connections accurate, and then report what it changed. Keep the write scope narrow: only files directly impacted by the tag change. Do not use this step for broad taxonomy cleanup or unrelated refactors.

6. **Report.** After editing, output a short report for the user:

```
=== REVISION: {note-filename} ===

Changes:
- {what you changed and why, 1 line each}

Flagged:
- {anything you noticed but didn't fix — e.g. a claim that may be wrong,
  a link that doesn't match its context phrase, a section that needs
  evidence you don't have, or external follow-up beyond the narrow tag-update pass}

===
```

Keep the report concise — aim for 3-8 change lines. Group small fixes (typos, tightening) into one line rather than listing each individually.
