---
description: "A caution when removing human approval stops: repeated acceptance can conceal an exceptional-case check that has not been exercised or has been omitted"
type: types/note.md
traits: [title-as-claim]
tags: []
---

# Routine approvals do not show that human judgment is dispensable

Repeated approval does not show that a human check is unnecessary. The operator may not have encountered the case that needs judgment, or may have approved it without checking. For example, an agent's KB link updates might mostly correct paths, but occasionally replace the source supporting a claim. An operator who routinely approves path corrections can miss the source replacement that requires checking support. This is a hypothetical failure, not an observed frequency claim.

Removing the approval stop while preserving its intended protection requires accounting for those exceptional cases. Automating routine cases and routing exceptions to a person reduces interruptions, but does not fully automate the original scope. Full automation requires automating the exceptional check too, or reliably excluding those cases from the permitted work. Keeping the approval button alone does not ensure that the check happens.
