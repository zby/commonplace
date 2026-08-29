---
description: Fork-by-fork decomposition of ingesting a source — orchestrator routes, cp-skill-ingest coordinates capture and connection forks, then delegates analysis to a fresh drafting worker; five clean contexts
type: scenario
frequency: occasional
---

# Ingest a source

The user provides one URL-backed document to capture and analyse.
`cp-skill-ingest` (context: fork) drives a pipeline that invokes
`cp-skill-snapshot-web` to create a local reading copy and `cp-skill-connect`
to discover links. It then gives the snapshot and connect report to a fresh
worker that writes the tracked `.ingest.md` analysis. Five clean contexts, each
paying overhead from scratch.

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
| snapshot frontmatter and checksum | content | variable | 1 |
| final ingest validation | overhead | `commonplace-validate` | 1 |

Notes: the driving fork injects its skill body (0 hops), invokes Forks 3 and 4,
then dispatches Fork 5 with exact input paths and verifies its handoff. It does
not classify the source or draft the analysis.

### Fork 3 — cp-skill-snapshot-web (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| capture procedure (URL routing) | overhead | `kb/instructions/cp-skill-snapshot-web/SKILL.md` | 0 |
| the fetched source | content | variable | 1 |

Notes: invoked by ingest for URL capture; writes the snapshot under ignored `kb/sources/.snapshots/`. The fetched page is external content and is not a tracked artifact.

### Fork 4 — cp-skill-connect (context: fork)
| load | kind | source | hops |
|---|---|---|---|
| connection procedure | overhead | `kb/instructions/cp-skill-connect/SKILL.md` | 0 |
| sources linking rules | overhead | `kb/sources/COLLECTION.md` | 1 |
| curated heads + scoped `rg` description listings per authorized destination | overhead | destination `README.md` / tag indexes + `rg` listings | 2-5 |
| the snapshot + candidate notes | content | variable | 2-5 |

Notes: connect runs the full prospecting procedure on every destination `kb/sources/COLLECTION.md` authorizes. As of ADR 025 there are no complete `dir-index.md` reads — before that change the notes (~66 KB) and sources (~60 KB) dir-indexes dominated this fork (~126 KB), the heaviest in the eval; the scoped listings grow with the matching slice instead. (Exact destination set = read it from the sources outbound section.)

### Fork 5 — ingest-report drafting worker
| load | kind | source | hops |
|---|---|---|---|
| drafting procedure | overhead | `kb/instructions/draft-ingest-report.md` | 1 |
| ingest-report type-spec | overhead | `kb/sources/types/ingest-report.md` | 2 |
| sources collection conventions | overhead | `kb/sources/COLLECTION.md` | 2 |
| the captured snapshot | content | variable | 1 |
| generated connection findings | content | variable | 1 |
| connected artifacts selected for verification | content | variable | 2 |
| worker-side ingest validation | overhead | `commonplace-validate` | 2 |

Notes: this is a fresh worker with no parent conversation history. Its complete
task input is the standalone drafting instruction plus exact paths for the
snapshot, connect report, and output, the expected snapshot checksum, any
prepared code-grounding context, and the optional occasion (the caller's
pre-reading question, which governs only the report's selection sections). It
writes and validates only the ingest report.

## Variants

**Snapshot already on disk:** Fork 3 is skipped. Fork 2 passes the existing
snapshot to Forks 4 and 5.

**Source type variation:** ordinary academic papers, blogs, GitHub, and X
change only Fork 3's capture method; Forks 2, 4, and 5 keep the same roles.

**Paper with code:** a Papers with Code URL, or an arXiv paper explicitly
requested with code grounding, makes Fork 2 read
`kb/instructions/ingest-paper-with-code.md`. Fork 3 captures the version-pinned
arXiv paper. Fork 2 also inspects commit-pinned checkouts under
`related-systems/`, then passes the prepared grounding context to Fork 5. This
adds evidence without adding another skill fork.

**Experiment-bearing source:** Fork 5 additionally reads
`kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` in
the source checkout or its installed `kb/commonplace/notes/` counterpart.
