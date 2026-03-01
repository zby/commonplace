# Directed Reading Procedure

Read a document through the lens of a goal. The goal shapes what you extract and how you structure the output.

**Parameters:**
- `DOCUMENT` — path to a markdown file (source snapshot, note, or any markdown)
- `GOAL` — what you're looking for: inline text, or a path to a note/file whose content defines the purpose

## Step 1: Working copy

Copy the DOCUMENT to a working copy next to where the report will be saved. This keeps `/connect` from modifying the original.

## Step 2: Connect

Run `/connect <working-copy>` to discover how this document relates to existing knowledge. Connections are written into the copy, not the original.

## Step 3: Read with purpose

Read the DOCUMENT and the GOAL (if it's a file path, read that file).

With both the goal and the connections from Step 1 in mind, write a report. No fixed template — the goal determines the structure.

Guidelines:
- Start with a one-paragraph summary of the document
- Address the goal directly — extract what's relevant
- Note connections found by /connect that bear on the goal
- Flag anything surprising that the goal didn't ask about but seems important
- End with a concrete next action

## Step 4: Save

Save the report as `{document-basename}.report-{short-goal-slug}.md` next to the document.

The slug should be 2-3 words derived from the goal (e.g. `report-crystallization-patterns.md`, `report-type-system-comparison.md`).

Delete the working copy created in Step 1.

Tell the user where the report was saved and what the recommended next action is.
