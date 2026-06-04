---
description: "Closure-SDK review: geometric S3 verification, database, and experimental brain runtime with file-backed state and query-gated recall but no agent prompt memory"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-01"
---

# Closure-SDK

Closure-SDK, by Walter Henrique Alves da Silva, is a monorepo for composing ordered data on the unit 3-sphere: a Python/Rust data-integrity SDK, a Closure DNA database layer, a CLI for stream comparison, and an experimental `closure_ea` "geometric computer" runtime with genome-style associative memory. For this review, it is best treated as an adjacent memory substrate rather than a conventional agent memory system: it retains and retrieves geometric summaries, database tables, genomes, and histories, but it does not wire those artifacts into an LLM agent's prompt context.

**Repository:** https://github.com/faltz009/Closure-SDK

**Reviewed commit:** [9a3d721e60a4f63f8d085d672b30e41c38844866](https://github.com/faltz009/Closure-SDK/commit/9a3d721e60a4f63f8d085d672b30e41c38844866)

**Last checked:** 2026-06-01

## Core Ideas

**The central retained object is a running geometric product, not a text memory.** The public SDK turns bytes into `ClosureState` values, composes them, inverts them, measures drift, and compares two states; the Python surface exports those primitives plus `Seer`, `Oracle`, `Witness`, `gilgamesh`, `Enkidu`, and Hopf/valence views ([closure_sdk/__init__.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/__init__.py), [closure_sdk/ops.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/ops.py)). The memory-like claim is structural: the system remembers enough ordered-data identity to detect and localize divergence without replaying full records every time.

**The SDK separates three observation depths.** `Seer` is a constant-memory stream monitor that keeps only the current running product. `Oracle` retains every raw record and path state so it can recover records, check ranges, and localize divergence. `Witness` builds a reference template and checks later test data against it ([closure_sdk/lenses.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/lenses.py)). This is a useful context-efficiency pattern: keep the cheap summary hot, escalate to retained evidence only when the summary reports drift.

**The stream tooling is a monitor plus forensic escalation pipeline.** `closure observer` ingests two streams through `Seer`, stores recent raw records in bounded `RetentionWindow`s, and calls `gilgamesh` only when drift crosses a threshold ([closure_cli/observer.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_cli/observer.py), [closure_sdk/canon.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/canon.py)). `closure seeker` uses `Enkidu` to hold unmatched records, advance cycles, confirm missing records, and reclassify late matches as reorders ([closure_cli/seeker.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_cli/seeker.py)). The system is efficient about context volume because it retains a window, not full stream history, in the online monitor.

**Closure DNA is the durable database layer.** A database is a directory of `.cdna` table directories; tables are typed, columnar, local, and file-backed, with typed columns, row operations, search, snapshots, history, identity checks, audit, repair, SQL, CLI, and a web workbench ([closure_dna/CLOSURE_DNA.md](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/CLOSURE_DNA.md), [closure_dna/table.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/table.py), [closure_dna/database.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/database.py), [closure_dna/sql.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/sql.py), [closure_dna/cli.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/cli.py)). It is a storage substrate with integrity and geometric retrieval, not an agent memory policy.

**Resonance search is the closest analogue to semantic retrieval.** Rust `resonance_scan` recovers each stored element, composes it with the inverse query, measures geodesic distance, decomposes the gap through Hopf channels, sorts by drift, and returns top-k matches ([rust/src/resonance.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/rust/src/resonance.rs), [closure_dna/table.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/table.py)). This is query-gated pull retrieval over geometric state. It has ranking authority over which row or genome entry is returned, but no natural-language relevance explanation.

**`closure_ea` implements a richer experimental memory runtime.** The `ThreeCell` runtime seeds permanent DNA anchors, ingests carrier sequences, reads over `genome union buffer` with ZREAD, collapses reads with RESONATE, writes epigenetic and response entries, records edges and coupling statistics, consolidates/prunes/merges non-DNA entries, and can serialize full runtime state or just the genome ([closure_ea/README.md](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/README.md), [closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/three_cell.rs), [closure_ea/src/genome.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/genome.rs), [closure_ea/src/field.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/field.rs), [closure_ea/src/consolidation.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/consolidation.rs)). This is the repository's strongest agent-memory-adjacent mechanism, but it operates on carriers, not notes, transcripts, or promptable lessons.

## Artifact analysis

- **Storage substrate:** `in-memory` — In-process Rust/Python objects, with `Seer` retaining only the current stream monitor state and `Oracle` retaining raw records plus a geometric path
- **Representational form:** `symbolic` — Symbolic/distributed-geometric numeric state, especially 4-float S3 elements
- **Lineage:** `authored` `imported` — authored docs, examples, schemas, thresholds, deterministic runtime logic, and curriculum windows combine with imported byte records, table rows, CLI inputs, and caller-supplied query carriers
- **Behavioral authority:** `knowledge` `enforcement` `routing` `validation` `ranking` `learning` — incidents, reports, rows, and states act as evidence; identity/audit/repair/transaction logic validates and gates accepted state; resonance and ZREAD route/rank reads; curriculum and response paths provide learning input

**SDK running products and closure states.** Storage substrate: in-process Rust/Python objects, with `Seer` retaining only the current stream monitor state and `Oracle` retaining raw records plus a geometric path. Representational form: symbolic/distributed-geometric numeric state, especially 4-float S3 elements. Lineage: derived deterministically from ordered byte records through hashing and quaternion composition. Behavioral authority: system-definition artifact authority for detection, comparison, and localization decisions; knowledge artifact authority when the returned `ClosureState`, `CompareResult`, or `LocalizationResult` is inspected as evidence. The promotion path is summary to escalation: a cheap state can trigger use of retained records and detailed incident reports.

**Retention windows and incident reports.** Storage substrate: in-memory deques of `RetainedBlock`s during monitoring, plus optional CLI JSON reports written by `identity`, `observer`, or `seeker`. Representational form: raw byte-record evidence plus symbolic incident fields such as `incident_type`, source/target positions, payload, checks, drift, channels, and axis. Lineage: raw stream/file records are buffered directly; incident reports are derived by `gilgamesh`, `Enkidu`, and Hopf/valence decomposition. Behavioral authority: knowledge artifacts for forensic evidence and operator review; system-definition artifacts when a CLI exit code, monitor escalation, or downstream automation treats drift or incident type as an operational gate.

**Closure DNA tables and database directories.** Storage substrate: local `.cdb` and `.cdna` directories, typed column files managed through the Rust table engine, plus schema metadata and transaction journals/backups in the Python database wrapper. Representational form: mixed symbolic table schemas, typed row values, geometric sidecars/identities, append-only history, and named snapshots. Lineage: authored or imported rows, SQL/CLI mutations, table snapshots, rollback journals, and repairable derived geometric state. Behavioral authority: knowledge artifact authority when rows are queried as data; system-definition authority when identity, audit, repair, uniqueness, primary-key, foreign-key, or transaction logic controls whether database state is accepted.

**Resonance indexes and query results.** Storage substrate: table paths and Rust in-memory scan state; the inspected implementation exposes brute-force and flat-array resonance scans, with table search returning `ResonanceHit` records. Representational form: distributed-geometric carriers plus symbolic result tuples containing position, drift, base, and phase. Lineage: generated from stored row elements and a caller-supplied query carrier or typed row query. Behavioral authority: ranking and routing authority because top-k drift order decides which retained item is returned. Effective semantic relevance is not verified from code; the mechanism can rank geometric proximity, but a host application must define what that means for its domain.

**`closure_ea` genomes, buffers, and response entries.** Storage substrate: Rust structs in memory, optional JSON files through `Genome::save_to_file` and `ThreeCell::save_state_to_file`. Representational form: mixed symbolic/geometric state: DNA, Epigenetic, and Response layers; S3 address/value carriers; sequential edges; support, activation, zread, salience, coherence, and co-resonance statistics. Lineage: DNA anchors are boot-seeded and protected; epigenetic entries are created, reinforced, or corrected from carrier ingest and closure events; response entries are learned from delayed prediction feedback; consolidation merges/prunes based on geometric and coupling criteria. Behavioral authority: system-definition artifacts inside the runtime because they determine future ZREAD/RESONATE reads, prediction, generation, consolidation, and credit assignment.

**`closure_ea` curriculum traces and reports.** Storage substrate: in-memory `CurriculumTrace`, `CurriculumWindow`, and report structs. Representational form: symbolic ordered windows with carrier arrays and numeric outcome metrics. Lineage: authored deterministic carrier windows are replayed through a `ThreeCell` runtime; reports are derived from the resulting closures, genome growth, prediction error, self-free-energy, and consolidation counts ([closure_ea/src/teach.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/teach.rs)). Behavioral authority: evaluation and learning-input authority for experiments, but not trace-derived agent memory in the Commonplace taxonomy because the source traces are curriculum/data carriers rather than agent/session/tool transcripts.

**Docs, experiments, and benchmark outputs.** Storage substrate: Markdown docs, Rust examples, Python examples, demo data, generated documentation assets, and checked-in benchmark output files. Representational form: prose claims, executable examples, and sample outputs. Lineage: authored documentation and experiment code, with benchmark outputs retained as evidence snapshots. Behavioral authority: knowledge artifact authority for understanding and adoption; system-definition authority only where tests/examples are executed by maintainers or CI.

## Comparison with Our System

| Dimension | Closure-SDK | Commonplace |
|---|---|---|
| Primary purpose | Geometric verification, database/storage, and experimental carrier-based cognition | Agent-operated methodology KB with typed prose artifacts |
| Main retained substrate | S3 running products, `.cdna` tables, JSON genomes, stream windows | Git-tracked Markdown notes, type specs, indexes, review artifacts |
| Retrieval/read path | API/CLI pull, resonance nearest-neighbor, internal ZREAD/RESONATE | Agent pull through search/indexes/links, plus explicit instructions and validators |
| Context efficiency | O(1) summaries, bounded retention windows, top-k geometric scans, escalation on drift | Lexical routing, indexes, links, schemas, scoped skills, validation/review bundles |
| Governance | Deterministic algebra, tests, audit/repair, transactions, snapshots | Collection contracts, frontmatter schemas, semantic review, validation, git history |
| Human interpretability | Incident tables, Hopf channels, docs, examples; many geometric states are opaque | Prose-first artifacts with explicit type and link semantics |

Closure-SDK shares Commonplace's local-first and inspectable bias, but the retained artifacts are very different. Commonplace stores behavior-shaping prose and symbolic contracts that an LLM can read directly. Closure-SDK stores algebraic summaries, table state, carriers, and genome entries that need code-mediated interpretation before they can shape an agent's next action.

The strongest alignment is escalation discipline. A `Seer` keeps a tiny running product hot, `RetentionWindow` preserves a bounded evidence slice, and `gilgamesh` produces detailed incident reports only when the cheap monitor detects drift. Commonplace could use the same shape for review and validation: hold small invariant summaries continuously, then expand to source-grounded evidence only on anomaly.

The main divergence is semantic authority. In Commonplace, a note, instruction, or type spec can be read and challenged as natural-language behavior guidance. In Closure-SDK, retrieval returns a row, carrier, incident, or genome value. That may be a powerful substrate for a future agent, but the repository itself does not include the policy layer that translates a retrieved geometric object into prompt advice, instruction, or a validator.

**Read-back:** `pull` — For agents. Closure-SDK exposes CLI/API/database/geometric retrieval that a caller deliberately invokes; `closure_ea` performs query-gated internal reads during ingest, but the repo does not implement relevance-gated push of memory into an LLM agent context

### Borrowable Ideas

**Escalation from invariant summary to retained evidence.** Commonplace could borrow the `Seer`/`RetentionWindow` split for review runs: keep cheap summaries of current state, but retain enough local evidence to explain a detected drift. Ready for validation/reporting workflows.

**Typed incident reports as first-class review artifacts.** `IncidentReport` is narrow but useful: type, source/target positions, payload, and checks. A Commonplace analogue would emit small structured discrepancy records for index drift, link rot, schema violations, or review-bundle disagreements. Ready where deterministic checks already exist.

**Snapshots and repair as database affordances.** Closure DNA's snapshot, history, audit, repair, and transaction recovery surfaces are a good reminder that durable knowledge substrates need rollback and repair verbs, not just writes. Commonplace has git history and validation; a borrowable version would expose higher-level "repair derived state" and "restore generated view" commands. Needs a concrete failing workflow before implementation.

**Separate geometric/ranking authority from semantic authority.** Resonance search ranks by a mathematically explicit distance, then leaves interpretation to the application. Commonplace should preserve this separation if it adds embeddings or learned ranking: rankers can select candidates, but prose/type contracts should remain the place where authority is assigned. Ready as a design constraint.

**Internal memory layers can be useful without prompt injection.** `closure_ea` shows a memory-bearing runtime where reads and writes happen inside the substrate itself. Commonplace should not assume every memory system is a prompt-context system; some retained artifacts shape future behavior through validators, stores, route tables, or model state. Ready as taxonomy discipline.

## Curiosity Pass

The repository's claims are broader than its agent-memory integration. The docs position the primitive as a replacement for many infrastructure layers, and `closure_ea` describes a cognitive architecture, but the code-grounded agent-memory takeaway is narrower: retained geometric state, database persistence, query-gated recall, and integrity/audit machinery.

`closure_ea` is the most memory-like part, yet it is not a trace-derived LLM memory system. It learns from carriers, closure events, prediction feedback, and curriculum windows; those are durable behavior-shaping inputs, but they are not agent/session/tool traces being distilled into notes, rules, or promptable lessons.

The system has two very different notions of "memory." Closure DNA is a database and integrity layer with snapshots and SQL. `closure_ea` is an experimental runtime with genomes and response entries. Treating them as one memory design hides important differences in substrate, form, lineage, and authority.

The Hopf/channel language is useful for incident explanation, but it is not a substitute for semantic review. A system can report W/RGB/base/phase values precisely while still requiring an application-level policy to decide what the result means operationally.

The context-efficiency lesson is stronger than the math claims need to be. Even if one ignores the universal-primitive framing, the monitor/escalate design is a concrete engineering pattern: constant-memory detection, bounded raw retention, detailed diagnosis on demand.

## What to Watch

- Whether an agent or LLM integration appears that turns resonance hits, incidents, DNA rows, or genome entries into prompt context; that would change the read-back classification and could create a real push-activation path.
- Whether Closure DNA's `build_genome`, resonance search, snapshots, and history gain clearer persisted file contracts in docs; that would make the storage substrate easier to compare with KB systems.
- Whether `closure_ea` state serialization becomes a promoted user-facing workflow rather than experiment support; that would strengthen the case for reviewing it as an autonomous memory runtime.
- Whether the repository adds ablations or benchmarks for retrieval quality, not just integrity/performance; that would help distinguish geometric proximity from useful semantic recall.
- Whether incident reports gain source-lineage fields beyond positions and payloads, such as input file hashes or stream segment ids; that would make them more borrowable as audit artifacts.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Closure-SDK is easiest to compare when running products, retention windows, DNA tables, resonance results, and genomes are separated by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: reports, docs, benchmark outputs, incidents, and query results are evidence unless a caller gives them operational force.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: comparison thresholds, audit/repair logic, resonance ranking, database constraints, and genome read/write rules directly shape later behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Closure-SDK stores and retrieves retained state, but does not activate it into an LLM agent context.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: `closure_ea` learns from carrier/curriculum streams, but the reviewed code does not distill agent/session/tool traces into durable prompt-facing behavior.
