---
description: "Job of an analyse-agentic-system run: check the assembled set semantically and write the overview's semantic verification and blockers"
type: types/instruction.md
---

# Verify the set

Read the assembled set: `overview-draft.md`, which is the overview without its verification, and the members in `output/`. Write `verification.md` with exactly these sections, which go into the overview's Verification and blockers:

```markdown
### Semantic verification

### Blockers
```

Check the whole set, not the separate lens returns, against the memory report type's Memory comparison fields: scope agreement with the canonical records across members, every scoped trace-fed write including compaction, each push signal's consumer and selector, and amendments and annotations on the same canonical IDs.

Record the checked routes and material dispositions, and the check of every source anchor, canonical ID, evidence status, boundary, member, limitation and blocker. A known assessment unsupported by its records is a blocker; properly scoped explicit uncertainty is not. Structural validation, which code runs, does not perform this check. Under Blockers write `none`, or each blocker with the member and IDs it affects. A blocker stops publication; code will not publish while this section names one.
