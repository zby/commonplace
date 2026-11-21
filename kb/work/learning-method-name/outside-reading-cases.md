# Cases for outside readings

Kept by Fable (claude-fable-5-2) since 2026-11-21 so that readings can be
repeated on the same cases. **A reader under test must not be shown this
file.** A case that [the draft](./draft-definition.md) discusses tests
lookup and not application, so it is retired here and replaced. Expected
placements are recorded before a reading and compared afterwards.

## Retired, because the draft now uses them as examples

- **D.** A support bot that decides whether to add an answer and rewrites
  one after three unhelpful marks. The draft's entry on triggers names it.
- **G.** A wiki that imports every page automatically, with editors deleting
  wrong ones. The draft uses it for the class of changes.
- **H.** A code-review bot that adds a rule after five reports. The draft's
  entry on triggers names it.
- **C.** A nightly job that ranks help articles by clicks. The draft's entry
  on direct updates names it. Its replacement is case L.

## Current set

| # | Case | Expected placement |
|---|---|---|
| A | A team adds a routing rule to its agents' written instructions after weighing searches saved against tasks misrouted. Later misrouted tasks can lead the team to revise or remove the rule. | Inside. Targeted correction. Kind undetermined. |
| B | A link repairer rewrites broken links in a documentation set and keeps a rewrite exactly when a fixed validator passes. Separately, the team that maintains it reviews where that validator is sufficient, changes the validator after bad repairs, and judges ambiguous repairs itself. Place the repairer alone and the team with the repairer. | Alone: depends on whether its own later work uses the documents; single-loop and no correction if inside. With the team: double-loop for link repairs. |
| E | A research team fine-tunes a model each week. It decides from held-out evaluations whether to deploy the new checkpoint, records the decision in a readable deployment file, and rolls back to an earlier checkpoint when production results get worse. Place the fine-tuning run and the team. | Run: outside on the store. Team: inside for deployment choices, targeted correction, kind undetermined. |
| F | An agent revises its written plan partway through a long task after a step fails. The plan governs the rest of that task and is discarded when the task ends. | Depends on the horizon. Outside for a horizon that spans tasks. |
| I | A mail service keeps a readable blocklist that its filter consults for every message. A script adds a sender when ten users have reported it. Each week a moderator reads the list and removes senders that were blocked wrongly. | Additions outside, as a trigger. Removals inside for that class. |
| J | An online shop's merchandising program proposes a new shelf category from sales patterns, runs it for one week beside the old layout, and keeps the category only if sales in it beat a fixed threshold. Kept categories are never reviewed again. The categories are a readable configuration the shop's own layout engine uses. | Inside, single-loop. Correction: none. |
| K | A translation team keeps a glossary that its translators use on every job. A translator proposes a term, and a second translator accepts or rejects it against written guidelines. When a client complains about a term, that entry is reopened. Twice a year the team rewrites the guidelines in the light of the complaints. | Inside, double-loop. Targeted correction. |
| L | A chess program keeps a readable opening book that it consults in every game. After each loss it marks the opening line it played as "avoid". | Outside. The loss fixes the update and nothing judges it. |
| M | A coding agent proposes edits to its own instruction file after each task. A second prompt to the same model is asked "is this edit an improvement?" before the edit is saved. In six months of logs the second prompt has never said no. | Depends on whether the check can in fact reject. The draft may not settle it. |
| N | A scientist keeps a lab notebook in which every result is written down as it comes. She also keeps a page of lessons that she consults when designing experiments. She adds a lesson when she judges that a result will matter for later designs, and crosses one out when later results contradict it. | Notebook entries outside. Lessons inside, targeted correction, kind undetermined. |
| O | A fleet of warehouse robots shares a readable list of no-go zones that every robot's route planner consults. A zone is added automatically whenever three robots have stalled at the same spot. Zones are never removed, and where two entries overlap the earlier one applies. | Outside as described: a count sets off the addition and nothing judges the zone. Replaces H. |
| P | A tutoring program keeps a readable set of worked examples that it shows to students. After each session it decides whether the session produced an example worth adding. When four students in a row fail the exercise that follows an example, the program regenerates that example. | Additions inside. Regenerations outside unless something judges the new example. The regeneration still acts on later evidence about one addition. Replaces D. |
| Q | A newsroom's style database receives every term from a wire service's feed automatically. Sub-editors consult the database while editing and strike terms they find misleading. | Imports outside. Strikes inside for that class. Replaces G. |

## Readings so far

- [Step 2](./positions/step-2-outside-reading.md): cases A to F, on the
  three-condition draft.
- [Step 3, Astra's reader](./positions/step-3-outside-reading.md) and
  [step 3, Opus](./positions/step-3-outside-reading-opus.md): on the
  two-condition draft. The Opus reading added D, G and H.
- [Step 4, Astra's reader](./positions/step-4-outside-reading.md) and
  [step 4, Opus](./positions/step-4-outside-reading-opus.md): on Neon's
  first revision.
- Step 5, Opus, on Neon's second revision: launched with A to H and the new
  I to N, before O, P and Q were written.
