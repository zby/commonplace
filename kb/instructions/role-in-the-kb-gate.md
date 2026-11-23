---
description: Report method that states a note's role in the KB from the passages that link to it, and reports what its dependents need, what it duplicates, which recommendations it has not taken up, and whom a change would reach
type: types/instruction.md
depth: 1
---

# Report a note's role in the KB

A note's text does not show what the KB uses it for. Other notes cite it for a term, a premise or a distinction. Source ingests recommend changes to it. A local repair that looks right inside the note can break a dependent, or miss that a dependent already states the claim better. This method reads the note together with the passages that link to it and reports the note's role. "Gate" is its file name only: it is **not a catalog gate** and gives no verdict. It is a report criterion, and its result is the **role report**. Write the report; do not touch the note.

## Inputs

- The note.
- `inbound`: the note's inbound contexts. For each file under `kb/` that links to the note, outside `kb/reports/`, `kb/workflow-state/` and `kb/work/`, it gives the file's repository path, title and description, and each passage that holds a link to the note. The text says when a cap cut files or passages. When nothing links to the note, it says so.

Judge only from these inputs. Do not open the linking files, and do not search for other links. A file or passage the caps cut is unseen: name the cut where it limits a finding.

It runs alone, with no other criterion:

```bash
commonplace-review NOTE --criteria role
commonplace-review NOTE --criteria role --input inbound=PATH
```

Without `--input`, the command collects the inbound contexts itself. The run keeps its result as a retained observation and writes no current result, because no freshness hash covers the inbound contexts. The full improvement procedure (`commonplace-revise NOTE --full`) runs it after its review sweep and hands the report to the assessor.

## The hard rule

Propose nothing about how to edit the note or its dependents. Do not rank edits, draft replacement text or recommend a pass. The product is a description of the note's role and of the dependencies a change would meet. Whoever plans the edit decides what to do with it.

## What to report

1. **Role.** In two or three sentences, state what the note is for in the KB as its dependents use it. Examples: it supplies a vocabulary pair that three notes cite; it is a premise other notes argue from; only tag heads cite it, and no dependent argues from it; nothing links to it. Then write one line that names the note's terms and claims that dependents rely on, and the ones no dependent uses.
2. **Dependents.** For each linking file, say what it needs from the note: a term, a claim, a distinction, a premise, or only a citation. Say whether the note supplies it: `SUPPLIED`, `PARTLY SUPPLIED` or `NOT SUPPLIED`. A dependent that uses a term in another sense than the note's does not get what it needs.
3. **Duplication.** Report where the note restates what a dependent's passage already states, or where a dependent restates the note. Say which states it better for the dependents' use, and why, when the passages show it.
4. **Untaken recommendations.** A linking source can recommend a change to the note: an ingest's "recommended next action", a "revise" or "add this citation" passage. Compare each with the note's text. Report each recommendation the note has not taken up. Report one the note has taken up only when it is partly taken up.
5. **Reach.** Name the claims and terms whose change would reach dependents, and name those dependents. A change to a claim or term that no dependent uses reaches no one; say so. Do not recommend cutting content because no dependent uses it. The report says who uses the note, not whether its claims are good theory; a sound claim can precede its dependents.

## Output

The caller names the output file. Write only that file; mutate nothing else. The output is a [review result](../types/review-result.md) fragment with `outcome: report` and no `attack-outcome`.

Each dependent need, each duplication and each untaken recommendation is one finding. Begin its `reason` with `SUPPLIED`, `PARTLY SUPPLIED`, `NOT SUPPLIED`, `DUPLICATED` or `UNTAKEN`, then name the linking file's repository path and state the need, overlap or recommendation. Give `scope: passage` with a quote from the note when one span of the note carries what the dependent relies on; otherwise give `scope: document` with no quotes. A note that nothing links to has no findings.

Keep `## Role` first and self-contained: a later reader may receive that section alone.

```markdown
---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["<the span of the note the dependent relies on>"]
    reason: "PARTLY SUPPLIED — <linking file path> — <what it needs and what is missing>"
outcome: report
---

# Role in the KB: <note title>

## Role
<two or three sentences: what the note is for, as its dependents use it>
Relied on: <terms and claims>. Unused: <terms and claims no dependent uses>.

## Dependents
<one line per linking file: its path and what it needs; the needs themselves are the findings>

## Duplication
<the overlaps, or "None">

## Untaken recommendations
<the recommendations not taken up, or "None">

## Reach
<the claims and terms a change would carry to dependents, with the dependents named, or "No dependent relies on the note's claims or terms">
```
