# Workshop: Connect Refactoring

## Question

How should `/connect` be restructured? Currently it couples discovery (finding connections) with mutation (editing files). This creates awkwardness with sources (working copies needed) and makes debugging opaque (no saved artifacts).

## Context

Started from a mechanical refactoring — splitting SKILL.md (688 lines) into a procedural core + reference files. That's done. But reviewing the simplified skill surfaced deeper questions about what `/connect` should actually do.

The ingestion-and-deep-search workshop already discovered the key pattern: **instructions notes** as frontloaded work packets for sub-agents. Experiment 2 concluded that "/connect is a caller-side tool (helps the caller discover connections to frontload), not a sub-agent-side tool." That insight applies here.

## Design: Split connect into discovery + directed writing

### The problem with coupling

`/connect` currently does four things in one pass:
1. **Discovery** — find candidate connections (index exploration, semantic search, keyword search)
2. **Evaluation** — articulation test, relationship typing, agent traversal check
3. **File mutation** — add inline links to prose, add Relevant Notes footer, add reverse links to other notes
4. **Index mutation** — update area indexes with the note

Steps 1-2 are judgment. Steps 3-4 are editing. Coupling them creates problems:
- **Sources can't be edited** (they're snapshots), so you need an awkward working copy
- **No saved artifacts** — the discovery trace and evaluation exist only in conversation output, lost after the session
- **Multi-note connecting** is all-or-nothing — you can't review connections across a batch before committing edits
- **Debugging is hard** — if a connection is wrong, you can't see why it was made

### The proposed split

**`/connect [note]` becomes discovery-only.** It reads the target note, runs dual discovery, evaluates candidates, and outputs a structured connection report to the workshop. No file mutations.

**Directed reading handles all writing.** It takes a document + a goal (the connection report) + a direction, and produces output:
- **Direction = "add links"** → rewrites the note with connections woven into prose, overwrites in place
- **Direction = "write analysis"** → writes a new report file (for sources, or any case where you want a separate artifact)
- **Direction = "update indexes"** → edits the relevant area indexes

This solves the sources problem naturally — you never edit a snapshot. `/connect` discovers what relates to it, then directed reading writes a new report or weaves connections into an existing ingest analysis.

For regular notes, "add links" is just the common case where the direction is "edit this file in place."

### Single-note is sufficient

`/connect` always targets exactly one note. Multi-note connection finding is a caller-level workflow:
- The caller iterates over multiple notes, running `/connect` on each
- Connection reports accumulate in the workshop
- The caller reviews the full picture before triggering edits
- Synthesis opportunities (flagged by individual `/connect` runs) can be addressed with cross-note context

The case where loading A+B+C together reveals connections invisible to individual runs is real but rare — and it's a synthesis task, not a connection task.

### Workshop as artifact home

Every `/connect` run saves its connection report to the active workshop directory. This means:
- **Debuggable** — you can see exactly what was discovered, what was evaluated, what was rejected
- **Reviewable** — a batch of connection reports can be reviewed before any edits happen
- **Reusable** — a connection report is an instructions note for directed reading

**Convention:** Skills check for an active workshop in the global context. If none is set, the skill fails. This forces intentionality about where artifacts go — no silent loss to conversation ephemera.

**Parallel agents:** The caller passes the workshop name to sub-agents in their prompt. All agents working on the same task write to the same workshop directory. No global mutable state.

## What we want to discover

- What does a connection report actually look like as a saved artifact? (The current output format is a starting point)
- Does directed reading need to be a separate skill, or is it a mode of an existing skill?
- How does the workshop name flow through skill invocations — CLAUDE.md, frontmatter, parameter?
- What's the lifecycle of workshop artifacts — persist forever, clean up per session, archive when done?

## Completed steps

### File structure refactoring (2026-03-03)

Split SKILL.md from 688 → 207 lines. Six reference files extracted:
- `discovery.md` — dual discovery methodology
- `evaluation.md` — articulation test, relationship types
- `linking.md` — inline link patterns, bidirectional rules
- `index-updates.md` — index structure, update rules
- `quality-gates.md` — gates 1-6 + edge cases
- `output-format.md` — report template

Also simplified to single-note target: removed multi-invocation patterns, narrowed description.
