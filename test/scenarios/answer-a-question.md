---
description: Fork decomposition of answering a question — a single read-only fork, content-dominated; the low-overhead contrast case where the framework costs little beyond AGENTS.md
type: scenario
frequency: common
---

# Answer a question

The user asks something the KB should know. The agent searches, reads the relevant notes, follows links, and synthesises — all in the **main session**. No `cp-skill-*` is invoked, so there is **one fork**. This is the contrast case: cost is dominated by *content* (the notes that answer the question, which any reader would load), and framework overhead is little more than AGENTS.md.

## Forks

### Fork 1 — orchestrator (main session) — the only fork
| load | kind | source | hops |
|---|---|---|---|
| routing + search patterns | overhead | `AGENTS.md` | 0 |
| navigation surface (only if scanned in full) | overhead | `kb/notes/dir-index.md` | 0-1 |
| matching notes | content | variable | 3-5 |
| linked notes followed | content | variable | 1-3 |

Notes: read-only, no skill fork. AGENTS.md is the only guaranteed overhead. The agent navigates by `rg` (search results are small content, ~0 overhead) **or** by scanning a dir-index; a *full* dir-index read is the expensive path (~66 KB) and is usually avoidable with `rg`, so it is listed at 0-1 hops. Everything else is content the reader would load regardless of any framework.

## Variants

**Depth:** a simple factual question needs only the matching notes (2-4 hops, content-only); a synthesis question exercises link-following (5-9 hops).

**Methodology question (installed project):** the search shifts from `kb/` to `commonplace/kb/notes/`, but the shape stays a single content-dominated fork.

**Commonplace repo:** no content/methodology split — everything is in `kb/notes/`.
