---
description: "Job of an analyse-agentic-system run: check the assembled set semantically and write the overview's semantic verification and blockers"
type: types/instruction.md
---

# Verify the set

Read the round's assembled set, as your prompt's inputs name it: the overview draft (the overview without its verification), the runtime member, the memory report that is the round's memory member byte for byte, the epistemic member, and the set check, which lists what structural validation of the set found. Write the output your prompt names with exactly these sections, which go into the overview's Verification and blockers:

```markdown
### Semantic verification

### Blockers
```

Both sections become overview text, so the overview type's source-anchor rules apply to them: cite a source path without a line range, or quote the passage. Your output is refused while the overview with your verification adds a validation failure to those the set check lists.

Check the whole set, not the separate lens returns, against the memory report type's Memory comparison fields: scope agreement with the canonical records across members, every scoped trace-fed write including compaction, each push signal's consumer and selector, and the Reconciliation's amendments and supersessions against the records they name.

Record the checked routes and material dispositions, and the check of every source anchor, canonical ID, evidence status, boundary, member, limitation and blocker. A known assessment unsupported by its records is a blocker; properly scoped explicit uncertainty is not. Structural validation does not perform this check, but every failure the set check lists is a blocker too. Under Blockers write exactly `none`, or a Markdown list with one `- ` entry per blocker, giving the member and IDs it affects and what would resolve it; indent any continuation line. Anything else is refused, including `None.` or `none found`. Code continues only on `none`: a blocker list starts another reconciliation round, which gets your verification, and in the last round it stops the run.
