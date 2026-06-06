---
description: Fork-by-fork decomposition of writing a KB note — orchestrator routes, cp-skill-write drafts, cp-skill-connect links; the most fork-rich common operation
type: scenario
frequency: common
---

# Write a note

The user asks the agent to capture an insight as a KB note. The work runs as three clean-context forks: the orchestrator routes the request, `cp-skill-write` (context: fork) drafts and validates the note, and the write skill then calls `cp-skill-connect` (context: fork) to wire it into the graph. Each fork pays its framework overhead from scratch.

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
| dir-index of every authorized outbound destination | overhead | `kb/{notes,reference,agent-memory-systems,sources,instructions}/dir-index.md` | 5 |
| candidate note bodies NOT opened | spared | — | — |
| the insight + any user-named sources | content | variable | 0-2 |
| targeted validation | overhead | `commonplace-validate` run | 1 |

Notes: the skill body is injected (0 hops; bytes count). Step 4 reads the dir-index of *each destination collection the source COLLECTION.md authorizes outbound links to* — for `kb/notes/` that is five (notes, reference, agent-memory-systems, sources, instructions), ~137 KB total, dominated by the notes (~66 KB) and sources (~60 KB) indexes. It deliberately does *not* open candidate bodies — that is the spared credit. This makes Fork 2 one of the heaviest forks in the eval (~150 KB net), on par with the connect fork. Directory-local types (adr, index) add one hop to a `kb/*/types/` spec. Whether AGENTS.md is re-injected into the fork is the main open assumption — set it in the harness config.

### Fork 3 — cp-skill-connect (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| connection procedure | overhead | `kb/instructions/cp-skill-connect/SKILL.md` | 0 |
| source-collection linking rules | overhead | `kb/notes/COLLECTION.md` | 1 |
| dir-index of every authorized destination | overhead | `kb/{notes,reference,agent-memory-systems,sources,instructions}/dir-index.md` | 5 |
| the just-written note | content | variable | 1 |
| candidate notes (body search, tag traversal, reverse-edge) | content | variable | 2-5 |

Notes: cp-skill-write suggests cp-skill-connect as a non-optional next step, so a normal write incurs this fork. Connect runs the *full* prospecting procedure on every authorized destination, so it re-reads the same ~137 KB of dir-indexes Fork 2 already read — **the operation pays for them twice** — plus tag indexes, `rg` body search, and candidate bodies (content). This is the heaviest fork; the repeated dir-index reads dominate it.

## Variants

**Commonplace repo vs installed project (common path):** identical forks — installed projects copy COLLECTION.md and the type-specs, so the overhead files and paths match.

**Selective link discovery:** most links land in `kb/notes/`, so an agent may read only the notes dir-index instead of all five authorized destinations — dropping Fork 2's index overhead from ~137 KB to ~66 KB. The skill instructs reading each authorized destination's dir-index, so all five is the worst case and the notes-only read is the optimistic one.

**Escalation to methodology (installed projects, ~10%):** when a convention is unclear, an extra search + 1-2 body reads into `commonplace/kb/notes/` are added to Fork 2. In the Commonplace repo this does not occur — the methodology notes are already the content in scope.

**Directory-local types:** for adr / index / agent-memory-system-review, Fork 2 adds one hop to the target collection's `kb/*/types/` spec.

**Write without connect:** if the user declines the suggested connect step, Fork 3 does not run — removing the largest single overhead body and the heaviest content-prospecting fork.
