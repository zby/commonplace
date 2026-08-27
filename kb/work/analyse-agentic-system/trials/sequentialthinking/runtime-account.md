# Runtime baseline — RUN `AGS-20260821-sequentialthinking`

Logical record 5. Mandatory; run before lens applicability was decided. IDs are those
registered in `evidence-packet.md` §4.

---

## 5.1 Causal responsibilities, not module boundaries

Three causal responsibilities are traced: **scheduling**, **context assembly**, and
**external state/action**. In this system they do not map to three modules — two of them are
almost entirely absent from the boundary, and the third is concentrated in one method.

| Responsibility | Where it lives inside the boundary | Where it actually lives |
|---|---|---|
| Scheduling | **nowhere** (`ABS-7`) | entirely in the host + model, outside the boundary |
| Context assembly | `RTE-2` (descriptor out) and `RTE-9` (response out) — the server contributes two fixed-shape payloads and selects nothing | assembly proper is the host's; the server has no selection policy |
| External state / action | `RTE-6`, `RTE-7` (in-process writes) and `RTE-8` (stderr) only; no external effect (`ABS-2`) | — |

One facility, `CMP-8` `processThought`, spans validation dispatch, content update, both state
writes, the observability action, and response construction. It is a single method, ~45
lines, and is the whole material path.

---

## 5.2 Material loops

A loop is material when it alters the analysis question, a control path, evidence strength,
or a lens result. Three loops qualify; each is recorded against the full field set.

### Loop A — server lifecycle (`RTE-1`, `RTE-12`)

| Field | Record | Evidence |
|---|---|---|
| Trigger / input | host spawns the process (typically `npx -y @modelcontextprotocol/server-sequential-thinking`, `RTE-13`); no arguments are read (`ABS-1`) | `SRC-1:269-278`, `SRC-2:47-59` |
| Next-step owner | the SDK's stdio read loop (`SRC-6`, **uninspected**) — the server yields control at `await server.connect(transport)` and never regains a scheduling role | `SRC-1:270-271` |
| Decision policy and its form | none. No configuration branch, no mode selection | `ABS-1` |
| Context selection and framing | none | — |
| State reads and writes | constructs the `CMP-5` singleton at module scope, before `runServer()` is called; state is therefore process-global and shared by every request on the connection | `SRC-1:249` |
| Action executor and boundary | stderr readiness line; no other effect | `SRC-1:272` |
| Persistence | none across process restarts (`ABS-2`) | — |
| Coordination and return | single process, one transport, one server instance | `SRC-1:237-249` |
| Retry / cancellation / recovery | **none.** Any rejection from `connect` → log to stderr → `process.exit(1)`. No retry, no backoff, no graceful shutdown, no signal handler | `SRC-1:275-278` |
| Output | readiness log; then the process is a passive responder | `SRC-1:272` |

**Materiality:** establishes that all retained state is process-scoped and singleton, which
is the precondition for the memory lens's read-back question, and establishes that the server
holds no scheduling role at any point.

### Loop B — tool advertisement (`RTE-2`)

| Field | Record | Evidence |
|---|---|---|
| Trigger / input | host `tools/list` request | `SRC-1:251` |
| Next-step owner | the host, immediately | — |
| Decision policy and its form | none — an unconditional return of one static array literal. The handler ignores its request argument entirely | `SRC-1:251-253` |
| Context selection and framing | the server's **only** outbound framing act: it hands the host `OBJ-1` (54 lines of imperative natural-language instruction) and `OBJ-2` (a 9-property JSON Schema). Selection is degenerate — the same descriptor every time, regardless of request, session, or accumulated state | `SRC-1:133-235` |
| State reads and writes | none. `OBJ-4`/`OBJ-5` are not consulted; the descriptor does not vary with history | `ABS-3` |
| Action executor and boundary | response over stdio; boundary ends at the transport | — |
| Persistence | the descriptor is compiled into the shipped artifact (`RTE-13`); it is static shipped material, not accumulated | `CMP-9` |
| Coordination and return | synchronous single return | — |
| Retry / cancellation / recovery | none | — |
| Output | `{tools: [SEQUENTIAL_THINKING_TOOL]}` | `SRC-1:252` |

**Materiality:** this is the route carrying `BAP-1`, the system's only advisory-force
authority path toward the model, and it is where every knowledge-production claim
(`CLM-1`–`CLM-3`, `CLM-5`, `CLM-10`) physically resides. It is also the anti-conflation
boundary: a tool schema present in context is not tool execution.

### Loop C — thought recording (`RTE-3`–`RTE-11`) — the primary loop

| Field | Record | Evidence |
|---|---|---|
| Trigger / input | host `tools/call` with `name` and an `arguments` object authored by the model | `SRC-1:255-257` |
| Next-step owner | **the host and model, unconditionally.** The server returns and yields. Nothing schedules, requests, or requires a subsequent call. `nextThoughtNeeded` is copied input→output unchanged and is never branched on (`ABS-7`) | `SRC-1:49`, `111` |
| Decision policy and its form | exactly three, all deterministic, all in imperative TypeScript: (a) **name equality** `request.params.name === "sequentialthinking"` (`RTE-3`); (b) **envelope validation** — four presence-and-type predicates, throwing `Error` on failure (`RTE-4`); (c) **branch routing** — `branchFromThought && branchId` both truthy (`RTE-7`). Nothing else decides anything |
| | Note on (b): `!data.thought` and `!data.thoughtNumber` are falsy-checks, so `thought: ""` and `thoughtNumber: 0` are rejected with type-shaped messages. `revisesThought`, `branchFromThought`, `branchId`, `needsMoreThoughts` are **cast, not checked** (`as` assertions at `SRC-1:50-54`) — a caller can put any type in them and the server will store and render it | `SRC-1:32-43`, `50-54`, `96` |
| Context selection and framing | **no selection.** The outbound payload `OBJ-6` is a fixed 5-field shape. Framing toward the model is minimal metadata. Framing toward the human is `OBJ-8`, a chalk-colored unicode box carrying the full thought text — the richest framing in the system, and it goes to stderr, not to any agent | `SRC-1:58-84`, `106-117` |
| State reads and writes | **writes:** `OBJ-4.push(validated)` on every valid call, unconditional, append-only, never pruned or bounded (`RTE-6`); `OBJ-5[branchId].push(validated)` when both branch fields are truthy, with lazy bucket creation (`RTE-7`) — a branch thought is therefore stored **twice**, once in each structure, as the same object reference. **In-place mutation:** `RTE-5` writes `validatedInput.totalThoughts = thoughtNumber` *before* the push, so the clamped value is what gets stored. **reads:** exactly two, both at `SRC-1:113-114` — `Object.keys(OBJ-5)` and `OBJ-4.length`. Content is never read (`ABS-3`) | `SRC-1:90-101`, `113-114` |
| Action executor and boundary | `console.error` (stderr) and the MCP response. No filesystem, network, or subprocess (`ABS-2`). The action boundary is the process's own two output streams |
| Persistence | process memory only, for the process lifetime. No serialization, no eviction, no size bound, no TTL. Unbounded growth is possible in a long-lived session; nothing in the boundary addresses it | `ABS-2` |
| Coordination and return | one singleton, no locking, no request identity, no session partitioning. If a host multiplexes several conversations onto one server process, their thoughts interleave in one `OBJ-4` with no separator — the code affords this; whether hosts do it is outside the boundary | `SRC-1:249` |
| Retry / cancellation / recovery | **validation failure:** `throw` inside `try` → caught at `SRC-1:118` → `OBJ-7` returned with `isError: true`. Crucially the throw happens *before* `SRC-1:94`, so a rejected call is **not** appended — state and history stay clean. **unknown tool name:** `RTE-11`, separate error payload, no state touched. **no retry, no cancellation handling, no compensating action** anywhere | `SRC-1:88-94`, `118-129`, `260-266` |
| Output | `OBJ-6` JSON text block to the host; `OBJ-8` box to stderr. `thoughtHistoryLength` and `branches` are the only outputs derived from accumulated state | `SRC-1:106-117` |

**Materiality:** this is the loop that determines both lens dispositions.

---

## 5.3 Anti-conflation checks

| Rule | Application here |
|---|---|
| A filesystem is not a scheduler | No filesystem exists (`ABS-2`); and the in-memory store is likewise not a scheduler — `ABS-7` records that nothing in the boundary schedules |
| Retaining material is not selecting it into context | `RTE-6`/`RTE-7` retain full thought records; `RTE-9` selects **none** of that content into any outbound payload. This is the sharpest instance of the rule in this system: retention is total, selection is nil (`ABS-3`) |
| A tool schema present in context is not tool execution | `OBJ-1`/`OBJ-2` reaching model context via `RTE-2`/`BAP-1` establishes an affordance only. Whether any call follows, and whether the model's behavior changes, is outside the boundary and uninspected |

---

## 5.4 Conditional surface inventory

Surfaces are inspected only where they materially alter the analysis question, a control
path, evidence strength, or a lens result. Materiality is stated for each included surface.
This is not a taxonomy, template, ladder, ranking, or adoption advice; surfaces not listed
below were judged immaterial and are omitted deliberately.

| Surface | Included? | Materiality statement | Finding |
|---|---|---|---|
| Observability | **yes** | It is the system's only rich output and the only place thought content leaves the process, so it changes the memory lens's read-back answer and owns `BAP-3` | `RTE-8` writes the full thought, chalk-colored and boxed, to stderr on every valid call, unconditionally and untunably (`ABS-1`). Content that never returns to the model does reach a human log reader. It is a display path with no consumer inside the boundary |
| Permissions / governance | **yes** | Determines whether any control surface exists for governance to attach to — a null result that bounds several conclusions | No permission, auth, rate-limit, quota, or gating mechanism of any kind. The only enforcing surface in the whole boundary is `BAP-4`, an envelope-shape schema check. Governance has essentially no attachment point here |
| Packaging / deployment | **yes** | `RTE-13` determines what artifact actually runs, and the README's recommended `npx -y` launch makes the deployed revision non-pinned, which bounds every claim tied to `2ecb382` | `tsc` → `dist/index.js`, `files: ["dist"]`, `bin` entry. README recommends `npx -y @modelcontextprotocol/server-sequential-thinking` with no version pin, so an operator following the README runs **whatever is latest**, not this revision. Combined with the ~20-month boundary age, this prevents any claim that a deployment following the documented configuration runs the analysed code |
| Providers / model access | **yes (as a null result)** | Bears on the scope route in §2 and on `ABS-10` | The server makes no model call and declares no `sampling` capability (`ABS-10`). It is model-adjacent machinery only: the model that gives it meaning runs entirely on the other side of the transport |
| Performance | **partial** | Only the unbounded-growth property is material, because it is a property of the retained store the memory lens analyses | `OBJ-4` is append-only with no bound, no eviction, no compaction. Per-call cost is O(1) except `formatThought`'s `'─'.repeat(...)`, which is O(len(thought)) |
| User interface | no | Immaterial — there is none; the stderr render is covered under Observability | — |
| Concurrency / isolation | **yes** | Determines whether `OBJ-4` is one shared store or many, which changes what the memory lens's read-back finding is about | Singleton with no session key or request partitioning (`SRC-1:249`); see Loop C "coordination and return" |
