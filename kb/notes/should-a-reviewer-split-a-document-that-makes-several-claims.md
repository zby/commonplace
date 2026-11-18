---
type: types/note.md
description: "Use the decision-record example when an editorial review recommends splitting a document solely because it contains several checkable assertions."
---

# Should a reviewer split a document that makes several claims?

Take an [architecture decision record](../reference/types/adr.md). It says what the team chose, why the alternative was rejected, and what the choice costs. A reviewer can dispute any of those statements. But a maintainer asking “Why did we choose this?” needs them together. Splitting the rationale from the decision because both contain claims would make the record worse.

Change the example: halfway through, the record also adopts an unrelated publication policy. A future maintainer could reverse that policy without reopening the first decision. Now there is a reason for a separate record: **someone needs to find or change the second decision independently**.

Check each assertion on its merits. Decide whether to split by asking what the reader needs to retrieve or revise as a unit, not by counting assertions.
