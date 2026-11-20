# Cold-reader check: a decision to keep the tag check is not a finding of net improvement

**Result:** Both questions passed at commit `88bd13490`. No repair to the instrument note or its link is indicated by this reading. This was one agent, not a test of agreement across readers or of the framework's effectiveness.

A fresh, read-only `commonplace-worker` session (`01a1fa93-4152-725f-886a-3b834ac88e47`) received [Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md) as its only starting document, with permission to follow its links. The prompt included the two questions below, not the plan, expected distinctions, or scoring criteria.

## 1. What does this note claim the tag-readme trace shows about Commonplace?

> **The trace shows a local gain from using the pieces together.** A tag index had grown too large to support its claim of completeness. Commonplace introduced the `tag-readme` type and gave its `complete` mark a meaning shared by the instructions, schema, validator, and renderer. The validator then found a tagged member that the documented `rg` search had missed. That finding prompted a correction to the search instructions. The evidence is not just that a new check ran: it caught a real omission and changed how the KB was maintained.

**Assessment:** Pass. The reader identified the observed difference from the old search and the resulting correction. The answer did not claim that a previously enforced completeness promise had failed, that the machinery did the design work unaided, or that this trace established system-wide effectiveness.

## 2. The maintainer must choose whether to keep this change. What can they reasonably decide now, and what can they still not claim?

> **The maintainer can reasonably keep the change here without claiming it has proved its worth overall.** Readers who rely on a complete index to know when they can stop searching have a concrete reason to prefer the check. The maintainer can weigh that benefit against the work of keeping marked indexes and the check current. If plausible upkeep costs would reverse the choice, those costs are worth investigating; otherwise the maintainer can act now and revisit the choice if usage or upkeep changes.
>
> The missed member establishes a detection gain in this case. It does **not** establish that Commonplace produces better-warranted work for the same human judgment, or comparable work for less. That would require a broader comparison with the previous practice, including losses as well as gains. Nor does success here show that another operator or a different kind of KB would benefit from the same rule.

**Assessment:** Pass. The reader gave a reason to keep the check and a condition for reopening the choice. They did not turn that decision into evidence that the benefit repaid the maintenance cost or transferred to another KB.
