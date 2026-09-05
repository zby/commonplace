---
description: "Pond review: Lance-backed cross-client session archive with canonical codecs, scheduled trace acquisition, pull-only recall, read-only analytics, and restore"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-09-04"
---

# Pond

Pond, built by tenequm, is a durable archive and interchange layer for agent
sessions. It converts session formats from agent clients into one canonical
`Session`/`Message`/`Part` representation, persists them in Lance, and exposes
search, transcript reads, SQL analytics, and restore-to-client operations. It
retains interaction traces for later use but does not run the agent loop that
decides when retrieved material enters a model context.

**Repository:** https://github.com/tenequm/pond

**Reviewed commit:** [`bb4f791ba1be6d4a70cf007e1bee9eb8008d9334`](https://github.com/tenequm/pond/commit/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334)

**Last checked:** 2026-09-04

## Core Ideas

**The canonical session model is the durable record and interchange boundary.**
Adapters parse client-specific traces into typed sessions, messages, and parts;
the same adapters serialize canonical sessions back to native or foreign client
formats. Canonical rows retain source agent, project, timestamps, structured
tool and file parts, source-specific options, injected-versus-conversational
provenance, and an ingest-host stamp
([canonical model](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/docs/spec.md#L268-L433),
[validator](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/sessions.rs#L3962-L4185)).
This is an exact mapping to trace-extracted retained memory: Pond transforms an
external execution trace without trying to derive a lesson from it.

**Fidelity is protected structurally, not semantically.** The adapter seam uses
sealed extracted values so adapter code cannot fill missing source fields with
ordinary literals; canonical validation checks ordering, identity, lineage,
provenance, and Pond-owned metadata. Append writes leave matching composite
keys unchanged. These mechanisms protect record shape and source attribution.
They do not check whether a human, model, or tool statement in the trace is
true.

> An adapter MUST NOT substitute a sentinel, default, or placeholder for source data it could not find.
> --- [docs/spec.md](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/docs/spec.md)

**Recall is explicit and progressively disclosed.** An agent or human first
searches with BM25 FTS or optional vector similarity, receives bounded excerpts
grouped by session, then expands a selected session or message. Filters, limits,
IDs, scope counts, pagination, and integration-level output caps control volume
and complexity. This is context engineering by pull and staged expansion, not
automatic recall
([search](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/handlers.rs#L1049-L1375),
[get](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/handlers.rs#L820-L1043)).
Actual precision, context dilution, model receipt, and behavioral effect were
not verified from static code.

**Searchable memory excludes low-signal scaffolding without deleting it.**
`search_text` includes user/assistant conversational text and selected file
metadata, while system, reasoning, tool, and injected content remain available
through full session/message reads and restore. Pond therefore uses different
projections for discovery and preservation instead of compacting the source
record into a summary
([search projection](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/sessions.rs#L4440-L4520)).

**Host integrations add routing and policy, not autonomous memory use.** Pi,
OpenClaw, and Hermes register four read-only recall tools. Static server
instructions, tool descriptions, a bundled skill, and Pi prompt guidelines tell
the model when and how to search; these are authored system-definition
artifacts, not accumulated memory. OpenClaw also translates host session
visibility into a project clamp and restricts whole-corpus SQL, but direct core,
Pi, and Hermes access are alternate paths. The wrapper policy is not core
authorization
([Pi tools and guidance](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pi-pond/src/tools.ts#L73-L229),
[OpenClaw tools](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/openclaw-pond/src/tools.ts#L131-L317),
[Hermes tools](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/hermes-pond/tools.py#L175-L246),
[MCP instructions](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/transport.rs#L1202-L1260),
[bundled skill](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/SKILL.md#L1-L57),
[OpenClaw scope](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/openclaw-pond/src/scope.ts#L71-L180)).

**Adoption is local-first but the trust envelope remains operator-owned.** Pond
ships as one binary with local or object-store Lance storage, explicit adapters,
HTTP/MCP surfaces, and first-party host plugins. Operators can inspect and move
the canonical data and restore sessions to client files. Hosted identity,
authorization, encryption, tenant routing, and object-store IAM are assigned to
the integrator, so this source review does not establish a deployment-level
privacy boundary
([deployment scope](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/docs/spec.md#L83-L108)).

## Artifact analysis

- **Storage substrate:** `files` `vector` — Canonical rows, full-text structures, and optional vectors persist in local or object-store-backed Lance datasets; restored sessions and SQL exports are ordinary destination files.
- **Representational form:** `natural-language` `symbolic` `parametric` — Conversation and transcript text are natural-language; canonical schemas, IDs, metadata, indexes, filters, and tool contracts are symbolic; optional embeddings provide parametric similarity signals.
- **Lineage:** `authored` `trace-extracted` `other-compiled` — Routing instructions and integration policy are authored; the canonical corpus is transformed from agent-session traces; search text, indexes, and embeddings are compiled from canonical rows.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — Retrieved sessions advise as knowledge; server/skill/tool text instructs and routes; OpenClaw scope code enforces within its wrapper; ingest validators admit rows; FTS/vector scores rank excerpts. No corpus artifact is promoted to an accepted rule or learned policy.

**Canonical session corpus.** The operative retained memory is a set of Lance
rows for sessions, messages, and typed parts. Natural-language and symbolic
content is trace-extracted through an adapter rather than copied byte-for-byte.
The validator and no-synthesis seam give it structural validation authority;
when later retrieved, it remains a knowledge artifact with advisory force.

**Search access structures.** `search_text`, FTS indexes, and optional embeddings
are other-compiled from the corpus. They carry routing and ranking authority for
a query, not authority over the truth of the selected content. A source-row
change or embedding-model mismatch invalidates or regenerates the corresponding
access structure
([embedding writes](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/sessions.rs#L1000-L1050)).

**Routing and scope artifacts.** MCP server instructions, the bundled
`SKILL.md`, integration tool descriptions, and OpenClaw scope code are authored
system-definition artifacts. They can route a host agent toward search and, in
OpenClaw, block or narrow tool calls. Their effective authority depends on the
external host loading and honoring them; that behavior was not verified from
Pond's code.

**Restored client files.** `pond resume` non-ampliatively reshapes a stored
session into a target adapter's filesystem format. Destination containment,
collision refusal, and rollback protect the write. Native restore is labelled
value-complete and foreign restore best effort, but no adapter-by-adapter
round-trip instance was observed
([restore](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/main.rs#L1924-L2165)).

**Promotion path.** Pond has no route that promotes an archived statement from
advisory session evidence to an instruction, validator, accepted claim, or
learned policy. A model may act on a retrieved transcript, but that host-owned
action is not a retained authority transition inside Pond.

## Write side

**Write agency:** `automatic` — Manual, scheduled, and host-lifecycle triggers
run deterministic ingestion that discovers source traces, converts them to
canonical events, validates them, appends new rows, computes optional
embeddings, and maintains search indexes. The operator chooses sources and can
trigger sync, but Pond does not expose a manual memory-authoring or editing
surface.

**Curation operations:** `none` — Pond acquires traces and maintains access
structures. It does not consolidate, evolve, synthesize, invalidate, decay, or
promote already-stored session content. Composite-key insertion prevents
duplicate rows; it is not semantic near-duplicate merging. At the reviewed
commit, no implemented session-erasure path supplies the only planned deletion
exception.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Enabled
adapters consume client session files and event records containing messages,
tool calls/results, reasoning, approvals, and harness-injected parts.

**Learning scope:** `per-project` `cross-task` — Project and source-agent
metadata remain filterable, while one Pond corpus can retain sessions across
projects, machines, clients, and later tasks.

**Learning timing:** `offline` `staged` — Sync runs manually, periodically, or
at host lifecycle boundaries after clients have written source traces; index
maintenance can run after row commits.

**Distilled form:** `natural-language` `symbolic` `parametric` — Trace content
becomes canonical natural-language and symbolic rows plus optional embeddings.
“Distilled” is only the controlled field name here: Pond preserves and indexes
the trace rather than summarizing or extracting higher-level lessons.

Pond belongs at the archival-acquisition end of the trace-learning survey. It
strengthens the distinction between retaining raw interaction evidence and
learning a higher-authority rule from it. Its adapters perform structured,
loss-aware conversion, but there is no judge, semantic distillation step, or
promotion policy. The raw-to-distilled loop therefore stops at canonicalization
and access-structure compilation.

## Read-back

**Read-back:** `pull` — Retained session memory reaches an agent only after the
agent or user deliberately invokes search, get, SQL, or resume. Pi, OpenClaw,
and Hermes do not register a hook that automatically selects and injects past
session content. Search is followed by bounded expansion, and weak results do
not prove that the archive lacks an answer. Authored server instructions and
tool descriptions may be loaded automatically, but static routing guidance is
not retained-memory read-back. The external host owns actual context insertion
and model use, so read-back faithfulness and behavioral effect are not verified
from code.

## Curiosity Pass

**“Lossless” is a contract with two different evidence levels.** The adapter
seam, canonical validator, source options, and native/foreign restore branch are
implemented. The stronger statement that every registered adapter preserves
every source value through a native round trip remains unobserved without the
adapter conformance fixtures and live outputs.

**“No prompt injection” is accurate only when narrowed to recalled content.**
The integrations do not push past-session memory, but Pond does load or register
server instructions and tool descriptions, and Pi adds prompt guidelines about
when to use the tools. This does not change the pull-only memory verdict; it
does expose a terminology boundary between memory injection and routing
instruction.

**Read-only has an object boundary.** MCP has no canonical ingest or delete
tool, and the SQL parser rejects mutations of the Lance corpus. SQL formatting
can write an export artifact, restore writes client files, and local-store
self-heal may rename damaged storage. “Read-only” is therefore precise for the
MCP corpus surface, not for every filesystem effect a Pond command can have.

**The specification and implementation disagree about erasure.** The design
specifies an operator-only true purge and resurrection denylist, while the
README still places `pond erase` next on the roadmap. The inspected
implementation is explicit:

> erase pending; pond erase is not yet implemented
> --- [packages/pond/src/main.rs](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/main.rs)

No implemented expiry, pruning, contradiction invalidation, or true-purge route
was found in the inspected boundary. At this commit, the stored corpus is
append-only in practice unless an operator changes the storage outside Pond.

**Provenance is not truth warrant.** Injected/conversational markers,
source-agent metadata, timestamps, options, and ingest-host stamps help a
reader reconstruct origin. Pond does not test propositions, record acceptance,
or prevent a later model from treating a plausible but false archived statement
as advice.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - rests-on: Pond retains and serves sessions, while the external host owns actual model activation.
- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: Pond converts session and tool traces into durable canonical records without a semantic distillation or promotion loop.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: separates Pond's canonical corpus, search structures, routing instructions, wrapper policy, and restored files by substrate, form, lineage, and authority.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - grounds: distinguishes advisory transcripts, routing instructions, relevance ranking, validation, and OpenClaw wrapper enforcement.
- [Representational form](../../notes/definitions/representational-form.md) - grounds: separates natural-language trace content, symbolic schemas and indexes, and optional parametric embeddings.
- [Pond whole-system analysis](../../agentic-systems/reviews/pond.md) - part-of: traces the same frozen source through core runtime, host-integration, security-boundary, and epistemic routes.
