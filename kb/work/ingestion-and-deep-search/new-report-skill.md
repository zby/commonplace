# Source Report Procedure

**Parameters:**
- `URL` — URL to snapshot and analyse (or path to existing snapshot)
- `GOAL` — what you're looking for, either inline text or a path to a file with instructions

## Step 1: Snapshot

If URL starts with `http`, invoke `/snapshot-web <URL>`. Parse the output for the saved file path.

If URL is a file path, use it directly.

## Step 2: Connect

Run `/connect <snapshot-path>` to discover how this source relates to existing knowledge.

Read the connected snapshot and note what was found.

## Step 3: Goal-directed analysis

Read the GOAL (inline text or file contents).

Read the snapshot. With both the goal and the connections from Step 2 in mind, write a report that answers the goal. No fixed template — the goal determines the structure.

Guidelines:
- Start with a one-paragraph summary of the source
- Then address the goal directly — extract what the caller asked for
- Note connections found by /connect that are relevant to the goal
- Flag anything surprising that the goal didn't ask about but seems important
- End with a concrete next action

## Step 4: Save

Save the report as `{snapshot-basename}.report-{short-goal-slug}.md` next to the snapshot in `kb/sources/`.

The slug should be 2-3 words derived from the goal (e.g. `report-crystallization-patterns.md`, `report-type-system-comparison.md`).

Tell the user where the report was saved and what the recommended next action is.
