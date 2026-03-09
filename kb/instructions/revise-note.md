---
description: Editorial revision of a single KB note — rewrites for logic, flow, and cohesion. Reads linked notes for context. Edits the file in place and reports changes.
---

# Revise Note

**Target: $NOTE_PATH**

## What this is

A content-level editorial pass on a single note. You may rewrite sentences, reorder paragraphs, cut redundant material, tighten arguments, and fix logical gaps. The goal is a note that reads as a coherent, well-structured argument — not a draft with bolt-on additions.

## Scope

- **In scope:** everything between the frontmatter block and the `---` separator before Sources/Relevant Notes/Topics. This includes headings, prose, lists, code blocks, and inline citations.
- **Out of scope:** frontmatter fields, the Sources list, the Relevant Notes list, and the Topics list. Do not add, remove, or reorder entries in these sections. You may fix broken markdown links if you encounter them.

## Steps

1. **Read the target note in full.**

2. **Read linked notes for context.** Follow links in the body and Relevant Notes section. Read enough to understand what the target note is building on and what it commits to. Cap at 8 linked notes — prioritise notes the target depends on (marked "foundation," "grounds," "mechanism") over notes that depend on it.

3. **Assess.** Before editing, identify:
   - Logical gaps: claims that don't follow from what precedes them.
   - Redundancy: the same point made twice in different words.
   - Flow breaks: sections that don't connect to their neighbours.
   - Cohesion failures: terms used inconsistently, or framing that shifts mid-note.
   - Unsupported transitions: "therefore" or "this means" without the intermediate step.

4. **Revise.** Edit the file in place. You may:
   - Rewrite sentences and paragraphs.
   - Reorder sections if the argument flows better.
   - Cut material that is redundant or doesn't serve the note's claim.
   - Add bridging sentences where logical gaps exist.
   - Sharpen vague language into precise claims.
   - Merge or split sections.

   Do NOT:
   - Change the note's central claim (the title).
   - Add new claims or evidence not already present or implied by the existing text.
   - Remove citations or source references from the body.
   - Touch frontmatter, Sources, Relevant Notes, or Topics sections.

5. **Report.** After editing, output a short report for the user:

```
=== REVISION: {note-filename} ===

Changes:
- {what you changed and why, 1 line each}

Flagged:
- {anything you noticed but didn't fix — e.g. a claim that may be wrong,
  a link that doesn't match its context phrase, a section that needs
  evidence you don't have}

===
```

Keep the report concise — aim for 3-8 change lines. Group small fixes (typos, tightening) into one line rather than listing each individually.
