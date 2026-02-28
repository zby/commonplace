---
description: Every traversal is a read-write opportunity — agents should log improvement opportunities during reading, then process them separately to avoid context-switching
type: note
traits: []
areas: [claw-design]
status: seedling
---

# Traversal improves the graph

Every time an agent traverses a note — following a link, searching for context, reading during `/connect` — it may notice something worth improving: a weak description, a missing link, a title that's a topic instead of a claim, a stale reference. The insight from arscontexta's [incremental formalization](https://raw.githubusercontent.com/agenticnotetaking/arscontexta/refs/heads/main/methodology/incremental%20formalization%20happens%20through%20repeated%20touching%20of%20old%20notes.md) is that these traversals are not just reads — they're opportunities for the graph to improve through use.

But fixing things on the spot is wrong for our system. The agent is mid-task — answering a question, writing a note, connecting documents. Context-switching to improve a traversed note means loading WRITING.md, reading the type template, understanding what "good" looks like for that specific document. The improvement costs more attention than the original task.

## The log as deferred improvement

The solution is to separate noticing from fixing. The agent appends one line to `kb/log.md` and stays on task. A separate pass — manual review, a future skill, or a recurring task — processes the log entries.

This matches the [wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md): capture with zero friction, refine later. The log entry is the lowest-friction capture possible — one line, no frontmatter, no filename to choose, no methodology to consult.

## What the agent notices during traversal

- **Weak descriptions** — topic summaries instead of retrieval filters
- **Missing links** — "this note should reference X but doesn't"
- **Topic-as-title** — titles that label a subject instead of making a claim
- **Stale references** — paths that don't exist, outdated directory names
- **Missing index membership** — a note that belongs in an area index but isn't listed

These are all things the agent can recognise without deep analysis — pattern-matching during normal reading.

## Co-evolution

The arscontexta note describes a bidirectional relationship: "The agent gets better at navigating the graph. And the graph gets better at being navigated." In our system this co-evolution is mediated by the log. The agent's traversal experience generates improvement signals; processing those signals improves the graph; the improved graph makes future traversals more productive.

The key difference from Luhmann's Zettelkasten (and arscontexta's model) is that we explicitly defer the improvement rather than doing it in-place. Luhmann could scribble a correction on a card in seconds. An LLM agent improving a note requires loading writing methodology, which is expensive. The log is the mechanism that preserves the co-evolution pattern while respecting the cost structure of LLM agents.

---

Relevant Notes:
- [wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — foundation: the log is zero-friction capture; processing is progressive refinement
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — constrains: the agent shouldn't load writing methodology during traversal, which is why we defer
- [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — the log catches staleness that defensive creation-time checks miss
- [Ars Contexta](./related-systems/arscontexta.md) — source: the incremental formalization insight that motivated this design

Topics:
- [claw-design](./claw-design.md)
