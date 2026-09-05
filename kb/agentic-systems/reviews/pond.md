---
description: "Whole-system analysis of Pond as a durable cross-client session archive, separating its canonical ingest, retrieval, restore, and host policy boundaries"
type: kb/types/note.md
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-04-pond-01
source-identity: https://github.com/tenequm/pond
reviewed-revision: bb4f791ba1be6d4a70cf007e1bee9eb8008d9334
---

# Pond

**Evidence basis:** first-hand source and design reading on 2026-09-04 of
`tenequm/pond` at commit
[`bb4f791`](https://github.com/tenequm/pond/commit/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334),
covering the Rust core, canonical model, adapter seam, Lance persistence,
HTTP/MCP transports, restore path, bundled skill, and the Pi, OpenClaw, and
Hermes integrations. I did not run Pond against a live corpus or host agent.

Pond is a durable archive and interchange layer for agent sessions. It reads
session formats from clients such as Claude Code and Codex, converts them into
one canonical `Session`/`Message`/`Part` model, stores them in Lance, and serves
search, transcript retrieval, read-only SQL, and restore-to-client operations.
It is not an agent runtime: the specification explicitly excludes executing
tools, running an agent loop, compacting context, and rendering the host's
response ([scope](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/docs/spec.md#L83-L108)).

That boundary controls every stronger claim about Pond. The core can make past
sessions durable and available. The enclosing agent host decides whether to
call a Pond tool, where to place its result, which model sees it, and what action
follows.

## Runtime progression

The ordinary write path starts with an enabled adapter. Manual or scheduled
sync discovers source sessions, parses them into typed canonical events, and
passes them through a validator that checks event order, identities, parent
coherence, part provenance, and Pond-owned ingest metadata. Composite primary
keys make matching rows no-ops; new rows append. Search text is compiled from
eligible conversational content, and embeddings are added only when semantic
search is enabled ([sync handlers](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/handlers.rs#L60-L473),
[store writes](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/sessions.rs#L1200-L1325)).

A trusted caller can bypass source discovery and submit canonical batches over
the HTTP/CLI ingest surface. This alternate still uses core validation, but its
values do not inherit an adapter's extraction guarantees. MCP exposes no ingest
or delete tool.

The ordinary read path is explicit. A caller chooses FTS or optional vector
search, applies filters and a limit, receives ranked excerpts grouped by
session, then may fetch a whole session or one message with bounded neighbors.
The MCP and HTTP transports dispatch to shared handlers
([search implementation](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/handlers.rs#L1049-L1375),
[get implementation](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/handlers.rs#L820-L1043)).
The separate SQL route accepts one DataFusion query or explain statement and
rejects write statements. Formatting modes can create an export file, so the
guarantee is precisely that SQL does not mutate the canonical corpus, not that
every invocation is side-effect free
([SQL gate](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/sql.rs#L304-L375),
[SQL tool](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/transport.rs#L1086-L1198)).

Restore runs the canonical record in the opposite direction. An operator
selects a stored session and target adapter. Pond includes child sessions,
labels each source as native or foreign, serializes it, refuses occupied or
escaping destinations, writes the full batch, and removes partial output on
failure. Native restore is intended to be value-complete; foreign restore is
best effort. The structure is implemented, but this analysis did not execute
adapter-by-adapter round trips
([resume path](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/main.rs#L1924-L2165),
[safe writes](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/adapter/mod.rs#L722-L864)).

## Canonical fidelity and context selection

The canonical schema is Pond's central product. Adapters must preserve each
ingested source value in a typed field, part, or source-specific options. They
must not invent missing values. Parts distinguish conversational content from
harness-injected scaffolding, so search can exclude injected text while restore
retains it. Source agent, project, timestamps, source options, and an ingest-host
stamp retain lineage needed to interpret a result
([model honesty](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/docs/spec.md#L411-L433)).

These checks establish schema honesty and attribution, not truth. Pond archives
whatever people, models, and tools said. It has no evaluator, evidence-consuming
acceptance decision, or semantic-review state for propositions in a session.
FTS and embeddings rank relevance. They do not decide whether retrieved content
is correct. SQL can derive counts or aggregates entailed by stored rows and the
query, but the caller owns the premises, query meaning, and interpretation.

Context efficiency is progressive disclosure. Search returns bounded excerpts,
IDs, grouping, and scope counts; get expands a chosen session or message;
plugin relays cap rendered text. No first-party integration automatically
selects retained session content for a model. The agent or user pulls it through
a tool. Static MCP instructions, tool descriptions, the bundled skill, and Pi
guidelines do provide routing advice about when to search, but shipped baseline
instructions are not recalled memory
([MCP instructions](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/transport.rs#L1202-L1260),
[Pi tool guidance](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pi-pond/src/tools.ts#L73-L105)).

## Host integrations and authority

Pi, OpenClaw, and Hermes project the same core operations into different host
envelopes. Pi exposes the operator's archive. Hermes exposes an
operator-selected corpus without adding per-caller scope. OpenClaw adds the
strongest policy: it hides Pond tools from subagents, translates host session
visibility into a project clamp, fails closed when required identity is absent,
and exposes cross-session SQL only at effective visibility `all`
([scope resolver](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/openclaw-pond/src/scope.ts#L71-L180),
[tool gates](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/openclaw-pond/src/tools.ts#L170-L317)).

The OpenClaw clamp is enforcement inside that wrapper, not core authorization.
Direct MCP/HTTP access, Pi, and Hermes are alternate paths. Search sends a
project clamp to Pond, while OpenClaw get operations repeat the caller-context
gate but deliberately do not reverify the target session server-side. The core
specification assigns identity, authorization, tenancy, gateway routing, and
object-store IAM to the integrator. A deployment-level security conclusion
therefore needs evidence outside this repository.

Retrieved transcripts have advisory behavioral authority. They reach the host
through a tool-result channel, after which the host or model may ignore them.
Search ranking decides which excerpts appear first, and OpenClaw scope policy
can block a call, but Pond does not observe or record whether recalled content
changes the later response. No behavioral-effect claim is observed or causally
supported by this source-only analysis.

## Documented erasure is not implemented

The specification describes `pond erase` as the sole append-only exception: an
operator-only purge that deletes a session and children, compacts history,
purges blobs, and prevents re-ingest
([erasure contract](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/docs/spec.md#L494-L506)).
The inspected implementation says the opposite at this revision: reconciliation
reports label erase as pending and state that `pond erase` is not yet
implemented
([implementation](https://github.com/tenequm/pond/blob/bb4f791ba1be6d4a70cf007e1bee9eb8008d9334/packages/pond/src/main.rs#L4356-L4365)).
No implemented expiry, automatic pruning, contradiction invalidation, or true
purge route was found in the inspected boundary. The archival path is therefore
append-only in practice at this commit, while the stronger right-to-erasure
contract remains doctrine only.

## Architectural assessment

Pond's design is coherent for an operator who wants a local-first or
object-store-backed record of complete agent sessions that can be searched and
moved across clients. Canonical provenance and explicit progressive disclosure
are the discriminating mechanisms: the archive tries to preserve what happened,
then lets a later caller decide how much of it to retrieve. The system keeps the
agent loop, truth judgment, and model-context decision outside its own authority.

That separation also sets the limits. Static source supports the ingest,
storage, retrieval, SQL, restore, and wrapper-policy wiring, but not live
durability, universal adapter fidelity, retrieval quality, actual model
activation, behavioral improvement, or deployed tenant isolation. Stronger
evidence would require reproducible corpus runs, adapter round-trip fixtures,
host traces joining tool results to model calls, retrieval judgments, causal
with/without-recall tests, and a deployment security review. Implementing and
testing the documented erase route would remove the clearest current
design/implementation mismatch.

---

Relevant Notes:

- [Pond memory-system review](../../agent-memory-systems/reviews/pond.md) — contains: applies the shared memory-system ontology to the same frozen source boundary
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: distinguishes Pond's durable corpus and host tool delivery from actual model use
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rests-on: separates ranking, wrapper enforcement, routing instructions, and advisory transcript context by consumer and force
- [Representational form](../../notes/definitions/representational-form.md) — rests-on: distinguishes natural-language sessions, symbolic schemas and indexes, and optional parametric embeddings
