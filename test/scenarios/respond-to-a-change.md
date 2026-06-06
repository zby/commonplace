---
description: Fork decomposition of responding to a change — a content-heavy evidence-assembly fork (answer-style) followed, only for KB-note responses, by the write and connect forks
type: scenario
frequency: occasional
---

# Respond to a change

The user notices an upstream change (PR, RFC, API update) or floats a design idea and asks for a grounded response. The agent assembles evidence in the **main session** (like answer-a-question), then composes the response. If the response is a KB note it invokes `cp-skill-write` and `cp-skill-connect` (two more forks); if it is an external message or PR comment, it stops after the orchestrator fork.

## Forks

### Fork 1 — orchestrator (main session)
| load | kind | source | hops |
|---|---|---|---|
| routing + search patterns | overhead | `AGENTS.md` | 0 |
| the change (PR / RFC / idea) | content | variable | 0-1 |
| evidence notes (search + read) | content | variable | 3-5 |
| linked notes for grounding | content | variable | 1-3 |

Notes: the evidence-assembly phase runs in the main session — overhead is just AGENTS.md, the rest is content (quotable prior decisions, ADRs, source reviews). For an external output (PR comment / message) the agent composes here and stops: no skill forks, no overhead beyond AGENTS.md.

### Fork 2 — cp-skill-write (context: fork) — only if the response is a KB note
| load | kind | source | hops |
|---|---|---|---|
| drafting procedure | overhead | `kb/instructions/cp-skill-write/SKILL.md` | 0 |
| collection conventions | overhead | `kb/notes/COLLECTION.md` | 1 |
| type-spec | overhead | `kb/types/note.md` | 1 |
| destination dir-indexes | overhead | `kb/notes/dir-index.md` | 1-3 |
| candidate bodies NOT opened | spared | — | — |
| the assembled evidence | content | variable | 0-1 |
| targeted validation | overhead | `commonplace-validate` run | 1 |

Notes: identical to write-a-note Fork 2. The evidence assembled in Fork 1 is the content the write is about (carried into the fork). An ADR response uses `kb/reference/types/adr.md` and `kb/reference/COLLECTION.md` instead (one extra type hop).

### Fork 3 — cp-skill-connect (context: fork) — only if the response is a KB note
| load | kind | source | hops |
|---|---|---|---|
| connection procedure | overhead | `kb/instructions/cp-skill-connect/SKILL.md` | 0 |
| source-collection linking rules | overhead | `kb/notes/COLLECTION.md` | 1 |
| dir-index of every authorized destination | overhead | `kb/{notes,reference,agent-memory-systems,sources,instructions}/dir-index.md` | 5 |
| the new note + candidates | content | variable | 2-5 |

Notes: identical to write-a-note Fork 3 — full prospecting re-reads all five authorized dir-indexes (~137 KB), the second such read in the operation.

## Variants

**External output (PR comment / message):** only Fork 1 runs — the cheapest path, overhead ≈ AGENTS.md, no dir-index reads.

**KB-note output:** Forks 2-3 as in write-a-note; this is where the heavy navigation overhead (skill bodies + dir-indexes) is incurred.

**Escalation (installed projects):** extra `commonplace/kb/notes/` reads can occur in Fork 1 (thin evidence) or Fork 2 (response doesn't fit a standard type) — two escalation points.
