# Agent memory systems

Reviews of external systems doing similar work — memory, knowledge management, and context engineering for AI agents.

## Why we track these

Convergence across independent projects is a stronger signal than any single design argument. When three unrelated systems arrive at filesystem-over-databases, that's evidence. When one system makes a bet we haven't considered, that's a prompt to think harder.

## What's here

- **`reviews/`** — one file per reviewed system. Each review is grounded in the system's code (not marketing), compares it with commonplace, and surfaces borrowable ideas.
- **`source-only/`** — standard-note coverage for systems known from a paper, README, or article when the repo-backed review type would overclaim implementation evidence.
- **`index.md`** — auto-generated directory index. Rebuild with `commonplace-generate-notes-index kb/agent-memory-systems`.
- **`landscape.md`** — curated navigation with a "Patterns Across Systems" section.
- **`agentic-memory-systems-comparative-review.md`** — cross-system synthesis.
- **`thalo-type-comparison.md`** — focused comparison that outgrew a single review section.

## For contributors

Writing conventions and the review workflow live in [COLLECTION.md](./COLLECTION.md). New repo-backed reviews use the `agent-memory-system-review` type — see `types/agent-memory-system-review.instructions.md` for the end-to-end workflow. If there is no reachable repository to inspect, use a standard note under `source-only/` instead.
