# Instruction: split and rehome critique

Use this instruction when a note contains several plausible ideas, but only one is strong enough to carry the current note. The goal is to preserve intellectual value without letting weak branches bloat or weaken the strongest claim.

## Task

Given a note, write a restructuring report. Do not edit the note.

## Procedure

1. Identify the main note that should remain after revision:
   - its central claim;
   - the minimum argument needed to support it;
   - the material that must stay.
2. Identify branch ideas:
   - claims that are interesting but not necessary for the main note;
   - analogies or hypotheses that need different evidence;
   - predictions or mechanisms that overreach the current argument.
3. For each branch, choose a destination:
   - **delete** when it is weak and has no independent payoff;
   - **open question** when it should stay only as a prompt for later work;
   - **new note** when it has a distinct claim worth developing;
   - **source/workshop note** when it is a lead, not a library-ready claim.
4. For each proposed new note, write:
   - candidate title-as-claim;
   - what evidence or reasoning would be needed;
   - why it should not remain in the original note.

Prefer rehoming over deletion only when the branch has a real independent claim. Do not split merely to save every sentence.

## Output

Write a Markdown report with:

```markdown
# Split and Rehome Critique: <note title>

**Target:** <path>

## Main note to preserve
**Claim:** <one sentence>
**Minimum argument:** <bullets>

## Branch inventory
| Branch | Current location | Destination | Why |
|---|---|---|---|
| ... | ... | delete/open question/new note/workshop | ... |

## Rehoming candidates
- **<candidate title>** — <claim, required support, and relation to the original note>

## Deletion candidates
- <material to remove and why removal strengthens the main note>

## Revision target
<short prose description of the revised original note>
```
