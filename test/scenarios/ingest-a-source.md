---
description: Fork-by-fork decomposition of ingesting a source — orchestrator routes, cp-skill-ingest drives a pipeline that forks cp-skill-snapshot-web (capture) and cp-skill-connect (link); four clean contexts
type: scenario
frequency: occasional
---

# Ingest a source

The user provides a URL or document to capture and analyse. `cp-skill-ingest` (context: fork) drives a pipeline that itself invokes two further forked skills — `cp-skill-snapshot-web` to capture, `cp-skill-connect` to link — before writing the `.ingest.md` analysis. Four clean contexts, each paying overhead from scratch.

## Forks

### Fork 1 — orchestrator (main session)
| load | kind | source | hops |
|---|---|---|---|
| skill table + routing | overhead | `AGENTS.md` | 0 |
| the URL or document | content | variable | 0 |

Notes: AGENTS.md is always loaded; the orchestrator routes "source analysis" to `cp-skill-ingest` and invokes it.

### Fork 2 — cp-skill-ingest (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| ingest orchestration procedure | overhead | `kb/instructions/cp-skill-ingest/SKILL.md` | 0 |
| source-review type-spec | overhead | `kb/sources/types/source-review.md` | 1 |
| sources collection conventions | overhead | `kb/sources/COLLECTION.md` | 1 |
| the captured snapshot | content | variable | 1 |
| related notes for extraction | content | variable | 2-3 |

Notes: the driving fork — injects its skill body (0 hops), invokes Forks 3 and 4, then writes the `.ingest.md`. The source-review type-spec is tiny (~1 KB).

### Fork 3 — cp-skill-snapshot-web (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| capture procedure (URL routing) | overhead | `kb/instructions/cp-skill-snapshot-web/SKILL.md` | 0 |
| the fetched source | content | variable | 1 |

Notes: invoked by ingest for URL capture; writes the snapshot under `kb/sources/`. The fetched page is external content.

### Fork 4 — cp-skill-connect (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| connection procedure | overhead | `kb/instructions/cp-skill-connect/SKILL.md` | 0 |
| sources linking rules | overhead | `kb/sources/COLLECTION.md` | 1 |
| dir-index of every destination authorized by sources | overhead | `kb/notes/dir-index.md`, `kb/sources/dir-index.md` (+ any others in the sources outbound section) | 2-5 |
| the snapshot + candidate notes | content | variable | 2-5 |

Notes: connect runs the full prospecting procedure on every destination `kb/sources/COLLECTION.md` authorizes — the notes (~66 KB) and sources (~60 KB) dir-indexes dominate (~126 KB), the heaviest single fork in the eval. (Exact destination set = read it from the sources outbound section.)

## Variants

**Snapshot already on disk:** Fork 3 is skipped — the path is passed straight to Fork 2/4.

**Source type variation:** academic paper / blog / GitHub / X each change only Fork 3's capture method; Forks 2 and 4 are identical.

**Escalation (installed projects, rare):** an unusual source format adds a search + 1-2 reads into `commonplace/kb/notes/` in Fork 2.
