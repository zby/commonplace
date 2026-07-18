---
description: "kgai review: local-first Go CLI storing engineering decisions as an append-only content-addressed event log projected into an embedded Kuzu graph, with Claude Code auto-capture"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-07-18"
---

# kgai

kgai (`kg`) is a local-first Go CLI, packaged as a Claude Code plugin, that records engineering **decisions** — what structural choice was made, *why*, and what it superseded — as an append-only, content-addressed event log, and projects that log into an embedded property graph of domain **elements** (features, services, business objects) an AI reads before and writes after changing code. It is aimed primarily at an AI consumer: every command prints JSON, and a bundled skill plus a `Stop` hook drive capture without an explicit user request. Built by kgaidev (kgai.dev); MIT-licensed; bundles the Kuzu/LadybugDB embedded graph engine.

**Source:** https://github.com/kgaidev/kgai

**Reviewed revision:** [aee513e109a2f903ccabb67238b35b7dfc384904](https://github.com/kgaidev/kgai/commit/aee513e109a2f903ccabb67238b35b7dfc384904) (release v0.1.9)

## Core Ideas

**Two planes, one log.** The append-only decision log is the source of truth; the graph is a throwaway projection. Writes go to per-install NDJSON shards (`log/<installId>.ndjson`), and a deterministic replay projects them into an embedded Kuzu property graph holding a **live element graph** (current shape) plus a **decision plane** (immutable history via `SHAPES`/`SUPERSEDES`) ([docs/ARCHITECTURE.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/docs/ARCHITECTURE.md), [src/internal/graph/graph.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/graph/graph.go)). The graph can be dropped and rebuilt from the log at any time (`kg rebuild`), so sync is log-merging, not database-merging.

**Elements are few and stable; decisions are the history.** A decision is an immutable event carrying who/why/when plus a list of structural mutations — `upsert_element`, `add_link`, `retire_link`, `set_prop` — applied atomically and idempotently ([src/internal/event/event.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/event/event.go)). `retire_link` deletes the live edge but the decision that retired it is permanent, so `kg as-of <date>` reconstructs any past shape by replaying events up to a cut ([src/internal/engine/reads.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/reads.go)).

**Deterministic identity gives coordination-free convergence.** `ElementID = "el_" + hash(normalize(kind), normalize(name))` and `DecisionID` is a content hash of the decision's intent (title, rationale, author, mutations) excluding supersession ([event.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/event/event.go)). Two recorders naming `feature:Invoice` mint the same id and `MERGE` onto one node; re-recording identical content is a no-op. This is exact-identity convergence, not similarity dedup — normalization only lowercases and collapses whitespace, so diacritics and synonyms fork the node.

> But **diacritics and distinct words still fork the node**: `Ceník` ≠ `Cenik`, `Invoice` ≠ `Faktura`. Pick one canonical name per element and reuse it.
> --- [skills/knowledge-graph/SKILL.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/skills/knowledge-graph/SKILL.md)

**Context efficiency: bounded head-only recall, history on demand.** `kg context` loads the *whole* live element graph into process (small by design) and ranks in-process, returning the top `--max` (default 15) elements, each with its current links and up to 4 **head** decisions (the current "why") — superseded decisions are deliberately excluded and served only by `kg history` on demand ([reads.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/reads.go)). So what lands in the agent's context is capped and current, with the full evolution reachable but not pinned. `kg search` ranks free text over elements and decisions with an in-process IDF-weighted fuzzy token overlap (camelCase splitting, stopwords, prefix/edit-distance matching) — lexical, not embedding-based ([src/internal/engine/search.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/search.go)).

**Trust rests on content-addressing and replay determinism.** Every event's hash is the sha256 of its canonical JSON; per-install shards form a hash chain; replay refuses to project any event whose content doesn't match its hash or whose decision id doesn't match its content, and `kg doctor` reports chain breaks ([engine.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/engine.go), [reads.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/reads.go)). `kg export --canonical` emits a sorted digest so two stores that replayed the same events can be proven byte-identical.

**Adoption affordances are strong but not zero-dependency.** Local-first, MIT, per-project store gitignored from the host repo, sync to a git repo or S3 bucket you own, no metered API. The log degrades to human-readable NDJSON files. Reads, however, require the native Kuzu/LadybugDB engine (CGO over `libkuzu`), downloaded as a prebuilt binary to `~/.kgai` — so the *projection* is not inspectable without that engine, even though the log is ([docs/ARCHITECTURE.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/docs/ARCHITECTURE.md)).

## Artifact analysis

- **Storage substrate:** `files` `graph` — The source of truth is per-install append-only NDJSON shards under `log/` (`files`; the store dir is also a git repo for the optional sync transport), and the derived read-model is an embedded Kuzu property graph, `graph.kuzu`, gitignored as a rebuildable cache ([store.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/store/store.go), [graph.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/graph/graph.go)).
- **Representational form:** `prose` `symbolic` — Each decision carries a natural-language `title`/`rationale` (the "why", prose) plus a structured mutation list — ops, element ids, link kinds — that is machine-applied to the graph (symbolic). The projected graph is symbolic structure (Element/LINK/Decision/SHAPES/SUPERSEDES) that also stores the prose rationale on Decision nodes.
- **Lineage:** `authored` `other-compiled` — Decisions in the log are **authored** through `kg ingest` (by a human or, via the plugin, by the agent composing the JSON); the Kuzu graph is **other-compiled** by deterministic replay of the log, regenerated by `kg rebuild` and invalidated by any newly appended or out-of-order pulled event ([engine.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/engine.go)). It is *not* trace-extracted — see Write side.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` — Decisions are consumed as advisory **knowledge**: the skill says "if a decision constrains what you're about to do, respect it," but nothing in the engine enforces that — it is context, not a gate ([SKILL.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/skills/knowledge-graph/SKILL.md)). The bundled `knowledge-graph` skill is a system-definition **instruction**/routing artifact directing when to read and record; the `Stop` hook is a deterministic **enforcement** trigger that blocks turn-end to inject a record-now instruction when code was edited.

The two central *memory* artifacts are the decision log and its projection; the skill and hook are the system-definition machinery behind the "automatic capture" claim and are classified below.

**Decision log (source of truth).** `files`, `prose` `symbolic`, `authored`, `knowledge`. Immutable, content-addressed, Lamport-stamped NDJSON, one writer per shard. Holds the durable memory; everything else is derived from it.

**Projected property graph (read-model).** `graph`, `symbolic` `prose`, `other-compiled`, `knowledge`. Kuzu tables: `Element`, `Decision`, `LINK`, `SHAPES` (with an `authority` flag marking the subset a decision structurally changed), `SUPERSEDES`, plus an `_Applied(hash)` watermark for idempotent replay ([graph.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/graph/graph.go)). Serves `context`/`search`/`history`/`conflicts`.

**`knowledge-graph` skill.** `files`, `prose`, `authored`, `instruction` `routing`. Its description instructs the model to invoke it "AUTOMATICALLY, WITHOUT WAITING TO BE ASKED" on a structural choice, and to read prior decisions before a non-trivial change — the DO/DON'T rules route what counts as a recordable decision ([SKILL.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/skills/knowledge-graph/SKILL.md)).

**`Stop` hook (auto-capture).** `files`, `symbolic`, `authored`, `enforcement`. A bash+python script that fires at end of turn and, if the turn edited code and no `kg ingest` ran, returns `{"decision":"block",...}` to force a record-now instruction ([hooks/auto-capture-stop.sh](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/hooks/auto-capture-stop.sh)).

**Promotion path.** kgai codifies *eagerly at acquisition*: a single authored decision fuses prose rationale with symbolic graph mutations, so the prose→symbolic crossing happens at write time, not through a later promotion. But behavioral authority never climbs past advisory knowledge — a decision cannot become an enforced gate on code; its force depends entirely on the agent choosing to read and honor it (the Stop hook enforces *recording*, never *compliance*). Effective authority and recall quality are *not verified from code*: whether a respected-by-convention rationale actually changes the next action is untested here.

## Comparison with Our System

| Dimension | kgai | Commonplace |
|---|---|---|
| Unit of memory | An immutable decision (who/why/when) mutating a small element graph | Typed artifacts (notes, ADRs, reviews) under collection contracts |
| Substrate | NDJSON log (truth) + rebuildable Kuzu graph (read-model) | Git-tracked Markdown `kb/` collections + SQLite freshness/review store |
| Identity | Deterministic content/name hashes; coordination-free convergence | Human-authored paths, titles, links; validated by code |
| History | Append-only; supersession chains; `as-of` replay | Git history; archive lifecycle; review baselines |
| Retrieval | In-process lexical fuzzy rank; bounded head-only context | Lexical `rg`, curated indexes, authored links, review gates |
| Authority | Advisory knowledge; no enforcement on code | Type schemas, validation gates, semantic review before durable authority |

kgai and Commonplace agree that provenance and immutable history matter, and both prefer inspectable local files over a service. They diverge on where authority lives: kgai's decisions are pure advisory context with a deterministic *capture* gate but no *compliance* gate, whereas Commonplace makes typing, validation, and review the gates a claim must pass before it carries durable weight. kgai's live graph is deliberately tiny (few stable elements), which makes "load everything and rank in-process" viable — a bound Commonplace approximates with curated indexes rather than an in-memory whole-corpus scan.

### Borrowable Ideas

**Head-only recall with history on demand.** Serving only the current head decision(s) per element into context, with the superseded chain reachable via a separate `history` call, is a clean context-efficiency pattern. In Commonplace terms it maps onto surfacing the current claim while keeping the ADR/supersession trail one hop away. Ready now as a read-shaping principle for review and navigation surfaces.

**Deterministic content-addressed identity for convergence.** Hashing normalized identity so independent recorders converge on one node, with a content hash making re-records idempotent, is an elegant way to avoid duplicate islands without coordination. For Commonplace this needs a concrete use case first — repo paths and links already give stable, git-visible identity, so the payoff would only appear in a multi-writer, machine-authored setting.

**Replay-determinism digest as a trust check.** `kg export --canonical` proving two stores replayed to a byte-identical state is a strong integrity affordance. Commonplace could borrow the idea of a canonical digest over a derived index to detect drift between the index and its ground truth. Ready as an experimental validator concept.

**A capture gate that forces recording, not compliance.** The `Stop` hook's "you edited code — record the decision now or explicitly record nothing" is a deterministic nudge that separates *capturing* a decision from *obeying* it. Worth watching as a model for Commonplace write-discipline hooks, but needs a use case before adoption.

## Write side

**Write agency:** `manual` `automatic` — Decisions are **authored** through the `kg ingest` write interface, whether a human types the JSON or the plugin-driven agent composes it ([main.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/main.go), [engine.go](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/engine.go)). The **automatic** side is engine-computed supersession: on each authoritative ingest the engine finds the current head decision(s) of every element the decision structurally changes and records `SUPERSEDES` edges to them — the author does not set supersession by hand.

**Curation operations:** `invalidate` — Supersession is truth maintenance over already-stored decisions: a new authoritative decision marks the prior head(s) stale (no longer authoritative for that element) while **retaining** them in the log and decision plane, so `history`/`as-of` still serve them and two unsuperseded heads surface as a conflict branch ([engine.go `headDecisions`/`buildDecisionEvent`](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/engine.go), [reads.go `Conflicts`](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/src/internal/engine/reads.go)). Deterministic element convergence (`MERGE` on the identity hash) is acquisition-time identity, not a `dedup` operation over stored entries; index rebuilds after sync are access-structure upkeep. No `consolidate`, `synthesize`, `decay`, or `promote` path exists.

**No trace-learning.** The plugin's "automatic, without you asking" capture is *not* distillation from agent traces. The `Stop` hook reads the transcript only to compute two booleans — did this turn use an edit tool, and did it already run `kg ingest` — and, if code was edited and nothing recorded, injects a record-now instruction; it never parses the transcript into a decision.

> IF the turn edited code, forces the model to record any structural decision NOW (or record nothing for trivial work). [...] it just injects one focused instruction at exactly the right moment.
> --- [hooks/auto-capture-stop.sh](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/hooks/auto-capture-stop.sh)

The decision content is authored by the LLM in-context and passed to `kg ingest`; the store never ingests session logs, tool traces, or transcripts as raw material. Lineage is therefore `authored`, so no `trace-learning` tag and no raw→distilled sub-section apply.

## Read-back

**Read-back:** `pull` — Retained decisions re-enter a future action only through the agent's own deliberate lookups. The skill directs the model to run `kg search`/`kg context` *before* a non-trivial change, and the `/kgai:kg-review` command's phase 1 pulls `kg context`/`kg conflicts` to ground the work ([SKILL.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/skills/knowledge-graph/SKILL.md), [commands/kg-review.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/commands/kg-review.md)). No hook or always-load path injects stored decisions into context: the `SessionStart` hook only installs the engine, and the `Stop` hook injects a *write* instruction, not retained memory ([hooks/hooks.json](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/hooks/hooks.json)). The recall discipline is entirely instruction-driven pull — a decision reaches context only if the agent honors the skill's "READ before you change code" step and issues the query. The skill description is shipped baseline instruction, not retained memory, so it does not lift the verdict above `pull`.

## Curiosity Pass

- **"Automatic dedup" is exact-identity convergence, not similarity merge.** It collapses only byte-normalized-identical `kind:name` pairs; near-duplicates, diacritic variants, and synonyms each mint a distinct node, and the burden of picking one canonical name falls on the caller (`kg resolve` is offered as a pre-check).
- **Team sync is implemented but marketing runs ahead of exposure.** The README front page sells parallel team memory ("8-way concurrent syncs against production S3", "1,000,000 decisions"), yet the architecture doc and CLI both mark sync experimental and unsupported. The `internal/remote` git/S3 transports and `kg sync` exist in code, but no slash command ships for it.

  > the sync mechanisms below are implemented in the engine (`kg sync`) but team sharing is **not yet exposed as a supported feature** — no slash command ships for it and the docs don't advertise it.
  > --- [docs/ARCHITECTURE.md](https://github.com/kgaidev/kgai/blob/aee513e109a2f903ccabb67238b35b7dfc384904/docs/ARCHITECTURE.md)

- **"Contextual search" is lexical, not semantic.** `kg search` is IDF-weighted fuzzy token overlap over the small live graph; there are no embeddings. The roadmap's "contextual-search index for stores beyond ~100k decisions" concedes the current approach is a whole-corpus in-process scan that only stays fast because the live graph is intended to be small.
- **The auto-capture reliability claim is about the hook, not the model.** The hook exists precisely because the model alone records only ~50–75% of the time; the deterministic block is what makes capture reliable. Whether the *recorded* decision is then *respected* on the next turn is neither enforced nor measured.

## What to Watch

- Whether team sync graduates from experimental to a shipped, slash-command-exposed feature — that would move sync from "designed" to deployed behavior and change how much of the README front page is verifiable.
- Whether the promised "kgai cloud" MCP endpoint lands; an MCP surface could add a push or host-mediated read-back path that this pull-only verdict does not currently cover.
- Whether a contextual-search index (embeddings) replaces the lexical scan for large stores — that would change the read-back signal character from lexical toward inferred/embedding selection.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: kgai stores a rich decision history, but read-back is instruction-driven pull; nothing activates a decision unless the agent queries for it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the log, its projection, the skill, and the hook differ across substrate, form, lineage, and authority.
- [Codification](../../notes/definitions/codification.md) - relates: kgai codifies a prose decision into symbolic graph mutations at write time rather than as a later promotion.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: decisions are consumed as advisory context, with no enforcement of compliance.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: the knowledge-graph skill and Stop hook instruct and enforce capture behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: deterministic element ids depend on a canonical name already being reused; diacritic/synonym forks are the symbol-availability limit.
