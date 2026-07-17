# Agent Memory Systems
A survey of external **agent memory systems** — how AI agents store, retrieve, and maintain knowledge across sessions and tasks. We track knowledge bases, context-engineering layers, structured note-taking tools, and trajectory-learning loops, reading their source code wherever it is available.

**Choosing or designing one?** Scan the [comparison table](./systems-table.md) — one
row per system, a plain-English description plus the handful of fields that
actually discriminate. Then read the [comparison](./agentic-memory-systems-comparative-review.md),
which synthesizes the current 148-row matrix, and
browse the repo-backed reviews under `reviews/` — each reads the actual
code and reports what a system _does_, not what its README claims.

We track these systems not just to borrow ideas but to watch how they evolve. Convergence across independent projects is a stronger signal than any single design argument.

## How we review

Every review classifies a system's retained behavior-shaping artifacts in **one
shared vocabulary**, so independent systems can be set side by side on the same
terms. The vocabulary, and the activation distinction the reviews turn on, come
from these theory notes:

- [designing-agent-memory-systems](../notes/designing-agent-memory-systems.md) — the design-pressure inventory the review contract distills into review-time sections.
- The **four-field artifact record** every review applies to each system's central artifacts:
  - [storage substrate](../notes/definitions/storage-substrate.md) — where retained state physically lives (files, repo, sqlite, rdbms, vector/graph, kv, in-memory, model-weights, service-object); locates access, versioning, deletion.
  - [representational form](../notes/definitions/representational-form.md) — prose / symbolic / parametric; sets the default inspection method (read / test / probe).
  - [lineage](../notes/definitions/lineage.md) — authored, imported, or trace-extracted, and what source change invalidates it.
  - [behavioral authority](../notes/definitions/behavioral-authority.md) — who consumes it, through which channel, with what force ([knowledge](../notes/definitions/knowledge-artifact.md) advice vs [system-definition](../notes/definitions/system-definition-artifact.md) instruction / enforcement / routing / validation / ranking / learning).
  - (the record applies at the [operative-part](../notes/definitions/operative-part.md) level of a [retained artifact](../notes/definitions/retained-artifact.md) — a bundled object is split when its parts carry different forms or authorities.)
- [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) — separates stored memory, memory loaded into context (**read-back**: pull / push / both), and memory that actually changes behavior; the reason a review states a read-back direction and asks whether faithfulness is tested.
- [symbolic context engineering is bounded by symbol availability](../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) — why a targeted push needs an identifier already on the table or a content inference; grounds the read-back **signal** (coarse vs identifier vs inferred).
- [agent memory is a crosscutting concern, not a separable niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — why these axes span storage, retrieval, and learning at once rather than being one "memory" box.

The [review type spec](./types/agent-memory-system-review.md) is the operational
contract that turns these notes into the fixed review sections and the
backticked lead tokens the [matrix](./systems.csv) is parsed from.
## Coverage
**Two coverage tiers.** Systems with inspectable implementations get the deep path: clone the repo, read the code, write a review note here. Systems known only from a README, paper, spec, or non-implementation repo get the lightweight path: snapshot the source into `kb/sources/`, run `/ingest`, and optionally add a standard note under `lightweight/` when the system needs a stable place in this collection.

Browse the roster:

- Repo-backed reviews (`reviews/`) — systems with open-source repos, reviewed from the code; the [comparison table](./systems-table.md) is the curated entry point
  
- [Lightweight coverage](./lightweight/README.md) — paper- or README-grounded systems with no inspectable repo
  

Cross-cutting reads:

- [Comparison table](./systems-table.md) — one scannable row per code-reviewed system
  
- [Comparison](./agentic-memory-systems-comparative-review.md) — the current synthesis across 148 code-reviewed systems
  
- [Trace-learning techniques in related systems](./trace-learning-techniques-in-related-systems.md) — broadens the comparison to artifact-learning and weight-learning systems fed by live traces
  
- [Thalo type comparison](./thalo-type-comparison.md) — detailed type mapping against the Commonplace document types
  
## Comparison matrix

[`systems.csv`](./systems.csv) is the machine-generated comparison matrix — one row per **code-grounded** review (`source-tier: code-grounded`, in `reviews/`), one column per comparison axis. It is **rebuilt from source artifacts, not hand-maintained**:

- Generated by [`scripts/build_systems_matrix.py`](../../scripts/build_systems_matrix.py): scans `reviews/` and extracts each review's comparison data (doc-grounded reviews under `lightweight/` are excluded). Re-run after reviews or triage artifacts change — `python3 scripts/build_systems_matrix.py`.
- Analysed by [`scripts/analyze_matrix.py`](../../scripts/analyze_matrix.py): reports per-column fill, value entropy, and redundancy to decide which columns earn a place in a human-readable table.

**Extractable columns** come straight from each review, so the matrix stays in sync with the prose:

- Backticked **lead tokens** written in the review body where the finding is reached — `storage_substrate` (`files`/`repo`/`sqlite`/`rdbms`/`vector`/`graph`/`kv`/`in-memory`/`prompt-registry`/`model-weights`/`service-object`), `representational_form` (`prose`/`symbolic`/`parametric`), `read_back_direction` (`pull`/`push`/`both`), `Read-back signal`, write agency, curation operations, and trace-learning sub-fields. The token leads its own justifying sentence, so value and reasoning can't drift. The convention lives in the [review type spec](./types/agent-memory-system-review.md).
- `lin_trace_extracted` from the authored `Lineage` tokens: at least one retained artifact comes from traces, such as session logs, execution histories, child-agent reports, request/response history, trajectories, recovery state, or stored interaction history.
- `trace_learning` from the review's `trace-learning` frontmatter tag: a stricter learning field for automatic writes fed by agent traces that produce durable behavior-shaping memory. `trace_learning` is a subset of `lin_trace_extracted`; systems can retain traces for evidence, recovery, continuity, or debugging without distilling them into lessons, rules, skills, validators, embeddings, adapters, rankers, or other learned memory.

The ASISAS-2026 paper's frozen corpus and Karpathy-gist sample split are deposited separately at DOI `10.5281/zenodo.20759081`, pinned to Commonplace `v0.1.0` (`e957a7b`). This living survey keeps growing and does not maintain that historical sample-origin column.

Remaining columns are hand-classified candidates the script lists but leaves empty; the analyzer flags them as too-sparse until filled. When populating a compound axis (e.g. the trace-learning sub-fields), record the raw observed value first and normalise it into a harness-agnostic vocabulary — the normalisation step is itself the test of whether the category generalises across systems.

**Consumption rule:** a human comparison table is for *choosing* a system, so it covers **code-based reviews only**. Lightweight reviews (doc-only or spec-only, lower authority) stay outside the generated code-grounded matrix and table until promoted to an inspected implementation review.

Current mature chooser fields are `storage_substrate`, `representational_form`, `trace_learning`, `read_back_direction`, and the `Read-back signal` one-hots. Pushing shipped static documentation is baseline context, not memory read-back. For system choice, the useful distinction is whether retained memory is pull-only, coarse-pushed, identifier-targeted, or inferred from the current content.

## Patterns Across Systems
Most systems here (ours, Ars Contexta, Thalo, ClawVault, Agent-Skills) independently converge on:

- **Filesystem over databases** — plain text, version-controlled, no lock-in
  
- **Progressive disclosure** — load descriptions at startup, full content on demand
  
- **Start simple** — architectural reduction outperforms over-engineering
  
- **Trace-learning** — [trace-learning techniques in related systems](./trace-learning-techniques-in-related-systems.md) broadens the comparison beyond pi-adjacent session mining to include artifact-learning and weight-learning systems fed by live traces and trajectories
  

The divergences are more revealing:

- **Storage model** — Cognee uses a poly-store (graph + vector + relational with pluggable backends), Siftly uses SQLite, CrewAI uses LanceDB by default with optional Qdrant Edge, Hindsight uses PostgreSQL+pgvector, Zikkaron uses SQLite with FTS5+sqlite-vec, and SAGE uses SQLite+BadgerDB (personal) or PostgreSQL+pgvector (multi-node) as operational substrates, while the others keep files as the primary storage interface. OpenViking occupies a novel middle position: it presents a filesystem interface (`viking://` URIs, `ls`/`read`/`find` operations) but the substrate is AGFS + vector index — filesystem as metaphor, not mechanism. Cludebot uses Supabase (PostgreSQL+pgvector) for its full mode but also offers a local JSON file store that is the closest a database-first system gets to filesystem-first. Cognee, Hindsight, CrewAI, Zikkaron, Cludebot, and SAGE are the furthest from filesystem-first: memories are opaque database records, not readable files
  
- **System boundary** — CocoIndex sits one layer below most systems here: it is an incremental engine for maintaining derived vector/graph/relational projections, not a primary knowledge medium. That makes it more relevant to our "operational layer beneath the KB" question than to the note/link semantics question directly
  
- **Agent-facing UX** — Napkin is the clearest example of treating CLI output itself as part of the memory architecture: hidden scores, match-only snippets, and next-step hints are all tuned for model behavior rather than human browsing. Most other systems focus on storage and retrieval internals but leave the interaction layer human-shaped
  
- **Packaging unit** — most systems distribute concerns across multiple files (notes, configs, scripts, indexes), but o-o pushes the opposite extreme: each document is a self-contained polyglot file carrying rendering, update contract, shell dispatch, source cache, and changelog. That maximizes portability and local inspectability at the cost of modularity and inter-document structure
  
- **Grounding discipline** — cognitive psychology (arscontexta) vs programming theory (Commonplace, thalo) vs empirical operational patterns (Agent-Skills)
  
- **Formalization level** — custom DSL (thalo) vs YAML conventions (Commonplace) vs prose instructions (Agent-Skills)
  
- **Governance stance** — most systems treat governance as advisory (instructions the agent should follow); Decapod enforces governance with hard gates (validation must pass, VERIFIED requires proof-plan); SAGE enforces with cryptographic gates (signed transactions, validator quorum, RBAC clearance levels) — two very different enforcement models, both structurally enforced rather than instructed
  
- **Access control** — SAGE has structured multi-agent RBAC (clearance levels, domain-scoped permissions, on-chain agent identity); Cognee has relational ACLs with tenant isolation and per-dataset permissions; most other systems either have no access control or rely on filesystem permissions
  
- **Cross-agent knowledge transfer** — most systems are single-agent or agent-agnostic; cass-memory is the first reviewed system to make cross-agent session mining a first-class feature, indexing logs from Claude Code, Cursor, Codex, Aider, and others into a shared playbook
  
- **Runtime self-modification** — most frameworks have fixed agent topology defined at build time; OpenSage is the first reviewed system where agents can create subagents and scaffold new tools at runtime, though without quality gates on the created artifacts
  
- **Self-referentiality** — only our KB is simultaneously a knowledge system and a knowledge base about knowledge systems
  
## Open Questions
- Does convergence on filesystem-first indicate a durable pattern, or a phase that will be outgrown?
  
- Should high-volume ingestion in a file-first KB adopt a small operational database layer for stage state and indexing?
  
- Will the programming-theory grounding produce better systems than the psychology grounding, or will they converge?
  
- Are there systems we're missing that take a fundamentally different approach?
