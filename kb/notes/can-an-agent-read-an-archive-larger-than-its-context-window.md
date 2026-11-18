---
type: types/note.md
description: "Use this arithmetic example when someone estimates how much of a wiki an agent can use from the size of one context window."
---

# Can an agent read an archive larger than its context window?

Suppose a wiki has 1,000 documents. Each has a 20-token description, and a call has 2,000 tokens available for input after other costs. Reading just the descriptions takes **10 calls** if the agent scans them all. The archive need not fit in one call. A flat list still costs the agent time to search.

Now suppose the agent opens the relevant documents and keeps a 100-token summary of each. If 12 documents matter, their summaries fit together in one final call: 1,200 tokens. If 30 matter, they do not: 3,000 tokens. Combining them in batches helps only if each intermediate result preserves what the final answer needs. A summary that retains the majority view but drops the one dissenting source is no use for a question about disagreement.

When someone asks “Will the wiki fit?”, ask two questions instead: **What must the agent read to find the sources? What must it keep together to answer this question?**

## Scope

These are illustrative numbers, not measured retrieval costs. The calculation counts neither the calls to read full documents nor their output tokens. A searchable index changes the cost of finding documents; it does not guarantee that the agent finds the right ones.

---

Relevant Notes:

- [Bounded-context orchestration model](../theory/bounded-context-orchestration-model.md) — see-also: the fuller account of how work is divided across calls.
