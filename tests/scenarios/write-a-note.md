---
description: Framework loads for writing a KB note, with a separate cost for optional link discovery
type: scenario
frequency: common
---

# Write a note

The user asks the agent to capture an insight as a KB note. The orchestrator routes the request; `cp-skill-write` drafts and validates the note, then suggests `cp-skill-connect`. Count Forks 1 and 2 for writing alone. Include Fork 3 only if connect is invoked; it produces a candidate-link report, not an edit to the note.

## Forks

### Fork 1 — orchestrator (main session)
| load | kind | source | hops |
|---|---|---|---|
| routing table + active vocabulary | overhead | `AGENTS.md` | 0 |
| the insight to capture | content | variable | 0 |

Notes: AGENTS.md is always loaded in the main session (0 hops, bytes still count). The orchestrator picks the target collection from the routing table, then invokes `cp-skill-write`. The insight is already in the prompting session.

### Fork 2 — cp-skill-write (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| drafting procedure | overhead | `kb/instructions/cp-skill-write/SKILL.md` | 0 |
| collection conventions + outbound-linking rules | overhead | `kb/notes/COLLECTION.md` | 1 |
| type-spec (artifact shape) | overhead | `kb/types/note.md` | 1 |
| near-duplicate check (key-term search) | overhead | `rg` over `kb/notes/` | 1 |
| the insight + any user-named sources | content | variable | 0-2 |
| targeted validation | overhead | `commonplace-validate` run | 1 |

Notes: the writer searches for near duplicates rather than scanning a whole collection. Cross-collection link discovery is separate. Use the evaluator’s `agents_per_fork` setting to match whether the harness supplies root instructions to each fork.

### Fork 3 — cp-skill-connect (optional follow-up)
| load | kind | source | hops |
|---|---|---|---|
| connection procedure | overhead | `kb/instructions/cp-skill-connect/SKILL.md` | 0 |
| source-collection linking rules | overhead | `kb/notes/COLLECTION.md` | 1 |
| curated heads + scoped `rg` description listings per authorized destination | overhead | destination `README.md` / tag indexes + `rg` listings | 5 |
| the just-written note | content | variable | 1 |
| candidate notes (body search, tag traversal, reverse-edge) | content | variable | 2-5 |

Notes: if connect runs, it reads the source contract and uses its search guidance to prospect permitted local destinations. The number of destination reads depends on that contract; the table illustrates five.

## Variants

**Write only:** report total overhead and the heaviest fork using Forks 1–2. **Write followed by connect:** report both measures using Forks 1–3. Do not include the optional fork in the write-only total or feasibility check.

**Installed project:** measure the target project’s `AGENTS.md` and collection contract. Read global type specs and canonical skill bodies from the installed library identified by `.commonplace/library.md`, not from copies under the project’s `kb/`. For a collection-local type, use its spec under the project’s `kb/<collection>/types/`. If the task needs deeper methodology, count the additional library reads in the fork that makes them.
