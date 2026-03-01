# Writing Directed Reading Instructions

How to write an instructions note that a sub-agent can execute with clean context. Directed reading — "read document X through the lens of goal Y" — is the first case, but the principles apply to any delegatable work.

## Core principle: frontload everything

The caller has context the sub-agent won't. The caller's job is to do the thinking — resolve references, select what's relevant, make decisions — and write it all down. The sub-agent's job is to execute, not to figure out what you meant.

A good instructions note is self-contained. A bad one has parameters to fill in.

## What to include

**The document(s) to read.** Full paths. If there are multiple, say why each is included and what to look for in each one.

**The goal, fully articulated.** Not "analyze this" — say what you're looking for. If the goal comes from another note, don't just point to it — extract the relevant parts and include them. The sub-agent shouldn't have to read a whole note to find the one paragraph that matters.

**Relevant context from connected notes.** Run `/connect` or search yourself before writing instructions. Include the connections that bear on the goal — a sentence each, with paths. Don't make the sub-agent discover what you already know.

**Where to focus.** If you know the relevant sections, say so. "Pay attention to sections 3.1-3.3 and the prompt templates in Appendix B" saves the sub-agent from reading the whole document with equal attention.

**Output location and format.** Where to save the report, what to name it. If you want a specific structure, say so. If you don't, say "the goal determines the structure."

**Working copy instructions.** If the sub-agent will run `/connect`, tell it to work on a copy and delete it after. Don't leave this to the sub-agent's judgment.

## Example

```markdown
# Instructions: A-MEM learning operations analysis

Read kb/sources/a-mem-agentic-memory-for-llm-agents.md

The question: how does A-MEM learn? What are the concrete operations
it performs, and are they all automatic? Focus on sections 3.1-3.3
(note construction, link generation, memory evolution) and the prompt
templates in Appendix B — the action vocabulary in B.3 is especially
relevant.

Connected notes that bear on this:
- kb/notes/automating-kb-learning-is-an-open-problem.md — frames
  automated re-organization as "boiling cauldron mutations." A-MEM's
  memory evolution is an empirical instance of this.
- kb/notes/claw-learning-is-broader-than-retrieval.md — argues that
  retrieval-only benchmarks miss most of what learning means. A-MEM's
  evaluations are retrieval-only.

Write a report that inventories the operations and assesses what's
missing. The goal determines the structure — no fixed template.

Save as: kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-learning-operations.md
```

## What NOT to include

- The search history that led you to these documents. The sub-agent doesn't need to know what you rejected.
- Hedging about whether the documents are relevant. You decided they are — commit to it.
- Instructions to "search for more sources." That's a different task; don't mix gathering and analysis.
