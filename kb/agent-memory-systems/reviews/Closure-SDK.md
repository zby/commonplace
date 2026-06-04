---
description: "Closure-SDK review: geometric verification, Closure DNA database state, and experimental carrier-genome memory without agent prompt activation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# Closure-SDK

Closure-SDK, by Walter Henrique Alves da Silva, is a monorepo for composing ordered data on the unit 3-sphere. It includes a Python/Rust data-integrity SDK, stream comparison CLI, Closure DNA embedded database, and an experimental `closure_ea` runtime with genome-style associative memory. For this review it is best treated as an adjacent memory substrate rather than a conventional LLM agent memory system: it retains geometric summaries, rows, histories, genomes, and carrier traces, but it does not wire those artifacts into an agent prompt loop.

**Repository:** https://github.com/faltz009/Closure-SDK

**Reviewed commit:** [9a3d721e60a4f63f8d085d672b30e41c38844866](https://github.com/faltz009/Closure-SDK/commit/9a3d721e60a4f63f8d085d672b30e41c38844866)

**Last checked:** 2026-06-04

## Core Ideas

**The central retained object is a geometric product, not a text memory.** The SDK embeds byte records into S3 elements, composes them, inverts them, measures drift, and compares states; the Python package exports those primitives along with `Seer`, `Oracle`, `Witness`, `gilgamesh`, `Enkidu`, and Hopf/valence views ([closure_sdk/__init__.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/__init__.py), [closure_sdk/ops.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/ops.py)). The memory-like property is structural: the system keeps enough ordered-data identity to detect, compare, localize, and classify divergence without presenting remembered prose to an agent.

**The SDK separates observation depth.** `Seer` keeps a constant-memory running product, `Oracle` retains a full record/path trace for recovery and localization, and `Witness` builds a reference template for later checks ([closure_sdk/lenses.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/lenses.py)). This is the clearest context-efficiency pattern in the repo: keep a cheap summary hot, then escalate to retained evidence only when drift requires investigation.

**The stream CLI is monitor plus forensic escalation.** `closure observer` composes incoming records through `Seer`, stores recent raw records in bounded `RetentionWindow`s, and invokes `gilgamesh` only when drift crosses a threshold; `closure seeker` holds unmatched records with `Enkidu`, advances cycles, confirms missing records, and reclassifies late matches as reorders ([closure_cli/observer.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_cli/observer.py), [closure_cli/seeker.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_cli/seeker.py), [closure_sdk/canon.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_sdk/canon.py)). The retained window bounds volume, while the incident report bounds what later consumers need to inspect.

**Closure DNA is the durable database layer.** A Closure DNA database is a directory of `.cdna` table directories with typed column files, tombstones, identity headers, history logs, snapshots, SQL, audit/repair, resonance search, and a local web workbench ([closure_dna/README.md](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/README.md), [closure_dna/table.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/table.py), [closure_dna/database.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/database.py), [closure_dna/sql.py](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/sql.py), [closure_dna/rust/src/table.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/rust/src/table.rs)). It is a file-backed store with integrity and geometric retrieval rather than an agent memory policy.

**Resonance search is the closest analogue to retrieval.** Rust `resonance_scan` computes a gap between a query and each stored element, measures geodesic drift, decomposes the gap through Hopf channels, sorts by drift, and returns top-k matches; Closure DNA exposes row and composite search on top of this idea ([rust/src/resonance.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/rust/src/resonance.rs), [closure_dna/rust/src/table.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_dna/rust/src/table.rs)). This is query-gated pull retrieval over geometric state. It ranks rows or carriers, but it does not explain natural-language relevance.

**`closure_ea` implements the strongest agent-memory-adjacent runtime.** The `ThreeCell` runtime seeds permanent DNA anchors, ingests carrier sequences, reads `genome ∪ buffer` with ZREAD, collapses reads with RESONATE, records ZREAD coupling, writes epigenetic and response entries, consolidates non-DNA entries, and can serialize a full `BrainState` or just a `Genome` ([closure_ea/src/lib.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/lib.rs), [closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/three_cell.rs), [closure_ea/src/genome.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/genome.rs), [closure_ea/src/field.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/field.rs), [closure_ea/src/consolidation.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/consolidation.rs)). It is a carrier-level memory runtime, not a note, transcript, skill, or prompt-memory layer.

## Artifact analysis

- **Storage substrate:** `files` — The primary durable substrate is local files: `.cdb`/`.cdna` database directories, typed column binaries, quaternion sidecars, tombstones, headers, history JSONL, snapshots, JSON genome/brain-state saves, CLI report JSON, and source-controlled Rust/Python code. Secondary runtime substrates include in-memory `Seer`, `Oracle`, `Enkidu`, `Buffer`, `ThreeCell`, and composition-tree objects.
- **Representational form:** `symbolic` `prose` — The operative state is mostly symbolic/numeric: quaternions, running products, row schemas, SQL AST mappings, table histories, snapshots, tombstones, genome entries, edges, activation counters, coupling statistics, and closure events. Prose appears in docs, README theory, CLI formatted reports, and source comments, but the implemented memory mechanisms are not prose-native. I did not find distributed-parametric storage such as learned embeddings or model weights.
- **Lineage:** `authored` `imported` — Users and programs author database rows, schemas, snapshots, saved genomes, and reference witnesses; SDK/CLI inputs import external byte streams, CSV/JSON data, and carrier curricula into geometric state. Runtime-derived indexes, histories, table identities, closure reports, and genome updates are derived views of those inputs, but not trace-extracted from agent session/tool logs in the Commonplace sense.
- **Behavioral authority:** `knowledge` `enforcement` `routing` `validation` `ranking` `learning` — Reports and query results act as knowledge artifacts; schema constraints, SQL parsing, foreign-key checks, uniqueness, locks, tombstones, audit, repair, and integrity checks validate or enforce; resonance search, SQL filters, Hopf channels, ZREAD, and RESONATE route and rank reads; `closure_ea` ingest, evaluation, and consolidation update learned carrier memory.

**SDK lenses and incident reports.** Storage substrate: in-memory running products, full record traces, reference trees, bounded retention windows, and optional JSON reports. Representational form: symbolic numeric states plus incident records containing positions, payload bytes, checks, drift, and Hopf channels. Lineage: imported from compared byte streams. Behavioral authority: knowledge and validation; the SDK can report drift or incidents, but caller code decides what to do next.

**Closure DNA tables.** Storage substrate: one database directory containing `.cdna` table directories, column files, quaternion sidecars, `rows.tomb`, `header.bin`, `tree.q`, `genome.json`, `history/oplog.jsonl`, and snapshot state copies. Representational form: symbolic schemas, typed values, row/table quaternions, tree identities, tombstones, and history metadata. Lineage: authored/imported rows plus derived geometric indexes and histories. Behavioral authority: validation, routing, ranking, and knowledge for SQL/API/web users.

**Closure EA genomes and brain states.** Storage substrate: in-memory runtime by default, with JSON persistence through `Genome::save_to_file` and `ThreeCell::save_state_to_file`. Representational form: symbolic carriers, layers (`Dna`, `Epigenetic`, `Response`), addresses, values, edges, activation counts, ZREAD statistics, co-resonance, salience, coherence, pending predictions, and closure events. Lineage: DNA anchors are authored bootstrap state; epigenetic and response entries derive from carrier ingest and evaluation feedback. Behavioral authority: learning, ranking, and routing inside the experimental runtime.

**Curriculum traces and examples.** Storage substrate: in-memory traces and source-controlled example files. Representational form: symbolic carrier windows, labels, reports, and numeric outcomes. Lineage: authored deterministic experiments replayed through `ThreeCell`; reports derive from closures, genome growth, prediction error, self-free-energy, and consolidation counts ([closure_ea/src/teach.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/src/teach.rs), [closure_ea/examples/exp_associative_memory.rs](https://github.com/faltz009/Closure-SDK/blob/9a3d721e60a4f63f8d085d672b30e41c38844866/closure_ea/examples/exp_associative_memory.rs)). Behavioral authority: evaluation and learning input for experiments, not durable agent memory extracted from production traces.

Promotion path: Closure-SDK has strong intra-system promotion paths but weak LLM-agent adoption paths. Database rows can become indexed/snapshotted/audited state; carrier observations can become genome entries, response entries, co-resonance statistics, and promoted level-1 attractors; incident windows can become JSON reports. None of those paths promotes remembered material into reviewed prose, prompt instructions, or agent-facing policy without an external application layer.

## Comparison with Our System

| Dimension | Closure-SDK | Commonplace |
|---|---|---|
| Primary purpose | Geometric verification, embedded database, and experimental carrier memory | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | Quaternion product, table directory, genome entry, closure event | Typed Markdown artifact with frontmatter, links, and citations |
| Source of truth | Local files and Rust/Python runtime state | Repository Markdown plus generated indexes/reports |
| Write path | Data ingest, SQL/API writes, stream monitoring, genome ingest/evaluation/consolidation | Authored notes, snapshots, validation, semantic review, index refresh |
| Read path | API/CLI/SQL/resonance/ZREAD/RESONATE calls | `rg`, indexes, links, skills, instructions, review reports |
| Governance | Type/schema checks, table locks, audit/repair, tests, geometric invariants | Collection/type contracts, validation, git diffs, semantic gates, archives |

Closure-SDK shares Commonplace's local-first and inspectable bias, but the retained artifacts have different semantics. Commonplace stores behavior-shaping prose and symbolic contracts that an LLM can read directly. Closure-SDK stores algebraic summaries, tables, carriers, histories, and genome entries that require code-mediated interpretation before they can shape an agent's next action.

The main divergence is authority. In Commonplace, a note, instruction, or type spec can be inspected as behavior guidance. In Closure-SDK, retrieval returns a row, carrier, incident, or genome value. That may be a useful substrate for future agent systems, but this repository does not include the policy layer that turns retrieved geometric state into prompt advice, routing instructions, or enforced agent behavior.

### Borrowable Ideas

**Escalate from cheap summary to retained evidence.** Ready now as a design pattern. Commonplace workflows could keep lightweight fingerprints or cheap checks around generated artifacts, then load full evidence only when the summary changes or fails.

**Make integrity identity first-class.** Needs a concrete use case. Closure DNA's table identity, audit, repair, and snapshot model suggests a stronger way to treat generated indexes as checkable views rather than trusted files.

**Separate transient buffer from durable memory.** Ready now. `closure_ea` makes the working buffer and genome distinct; Commonplace workshop artifacts could benefit from the same clarity about what is temporary context and what has crossed into durable library state.

**Borrow resonance as an analogy, not as a retrieval replacement.** Not ready. Geometric top-k over carriers is interesting, but Commonplace's core artifacts are prose and citations; replacing lexical/link-based navigation would need a clear semantic bridge.

**Keep learned state below prompt authority until reviewed.** Ready as a constraint. Closure-SDK demonstrates rich automatic state change, but Commonplace should not let derived state become instruction or truth without review.

## Write side

**Write agency:** `manual` `automatic` — Manual writes include API/CLI/SQL database creation, row changes, imports, snapshots, saved genomes, and direct source-controlled examples. Automatic writes include column sidecars, identity headers, composition trees, tombstones, history entries, composite indexes, CLI reports, retention windows, genome ingest/correction, ZREAD statistics, co-resonance, consolidation, pruning, and promotion.

**Curation operations:** `consolidate` `evolve` `decay` `promote` — `closure_ea` consolidates non-DNA entries by merging nearby alive entries and pruning weak ones; genome `correct`, `learn_response`, `credit_response`, and `distribute_credit` evolve stored values in place; buffers age out and BKT-dead entries are pruned; response clusters can promote into a higher-level genome during consolidation. Database repair and index rebuilds are access/integrity upkeep rather than semantic curation.

The automatic writes are over rows, carriers, indexes, histories, and geometric memory, not agent transcripts. I did not find a qualifying raw-agent-trace to distilled-memory loop, so the review does not use the `trace-derived` tag or a `Trace-derived learning` subsection.

## Read-back

**Read-back:** `pull` — Closure-SDK exposes retrieval and diagnostic surfaces through deliberate API, CLI, SQL, resonance, ZREAD, RESONATE, web, and file reads. It has no implemented agent harness that pushes retained memory into an LLM prompt without the agent or caller invoking a read.

Read-back is query-gated and code-mediated. The SDK and database read paths answer explicit requests: compare two states, search a table, run SQL, inspect a row, audit a table, evaluate a carrier sequence, or RESONATE against a genome. Inside `ThreeCell::ingest`, ZREAD/RESONATE are automatic runtime reads, but they serve the runtime's own carrier loop; they are not memory activation into a receiving LLM agent.

Selection and scope vary by surface. `Seer` exposes only drift, `Oracle` keeps full path state, observer mode retains a bounded recent window, Closure DNA SQL narrows rows by schema/filter/order/limit, resonance search returns top-k by geodesic drift, and `closure_ea` filters reads by Hopf channel and coupling threshold. Actual usefulness of those retrieved objects for an LLM agent is not tested by the repository.

Authority at consumption is mostly advisory or validating. Incident reports, query rows, Hopf views, and genome reads are knowledge artifacts for the caller. Database constraints, audit, repair, and table integrity checks have validation/enforcement authority over the store. Faithfulness of read-back to later agent behavior is not applicable in-repo because there is no LLM action loop consuming the reads.

## Curiosity Pass

**The repo calls part of the system memory, but not in the prompt-memory sense.** `closure_ea` has a real genome/buffer/read/write runtime, and Closure DNA is a real persistent store. Neither stores natural-language lessons for an LLM agent.

**The strongest design idea is observation-depth separation.** Constant-memory monitoring, bounded evidence windows, full traces, table histories, and snapshots are distinct retained surfaces. That separation is more transferable to Commonplace than the S3 math itself.

**The implementation is much more concrete in Closure DNA than in the broader cognitive-architecture framing.** The database code has files, locks, history, SQL, audit, repair, and tests; the "geometric computer" layer is more experimental and carrier-centric.

**Ranking is precise but semantically foreign.** Drift-ranked resonance is inspectable and deterministic, but it does not give the natural-language relevance contract that agent memory systems usually need.

**The context-efficiency story is structural.** Closure-SDK minimizes retained evidence and escalates reads, but it does not manage prompt token budgets, progressive disclosure for LLMs, or memory injection policy.

## What to Watch

- Whether any downstream Closure application connects Closure DNA or `closure_ea` genomes to an LLM prompt loop; that would change the read-back classification from substrate-only to agent memory.
- Whether Closure DNA's `genome.json` and composite indexes become stable public APIs; that would make the database's derived retrieval state more comparable to Commonplace generated indexes.
- Whether resonance search gains text/document adapters with inspectable explanations; that would make it more relevant to prose KB retrieval.
- Whether `closure_ea` brain-state persistence is used outside examples; that would clarify whether its genome is a production retained artifact or an experimental model.
- Whether audit/repair history becomes semantically reviewable rather than purely structural; that would bridge integrity checking and KB governance.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Closure-SDK stores and retrieves retained state, but does not activate it into an LLM agent context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: running products, retention windows, DNA tables, resonance results, and genomes need separate substrate/form/lineage/authority classification.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: incident reports, query rows, Hopf views, histories, and genome reads advise callers as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: schemas, SQL parsing, table constraints, audit/repair logic, and runtime read/write policies shape behavior with stronger force.
