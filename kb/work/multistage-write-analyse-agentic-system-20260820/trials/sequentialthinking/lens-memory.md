# Memory / context lens — RUN `AGS-20260821-sequentialthinking`

Logical record: step 6, embedded memory/context lens. IDs are those registered in
`evidence-packet.md` §4; new records are proposed under the lens-local `MEM-*` tag in §6 and
are **not** canonical until the orchestrator registers them.

Search boundary for every negative result in this lens is **B0** as defined in
`evidence-packet.md` §4e (the four files of `src/sequentialthinking` at `2ecb382`, each read in
full, plus targeted symbol reads), unless a narrower boundary is named inline.

`ABS-8` applies globally: there is no test, fixture, trace, log, or run artifact anywhere in the
boundary. **No finding in this lens can reach `observed` or `causally supported`.** Every status
below is `implemented`, `claimed`, `absent`, or `uninspected`, and the ceiling is restated at each
point where it bites.

---

## 1. Retained-part inventory

Parts are split wherever content, form, producer/consumer, checks, or authority path differ. The
nine required fields are carried across two tables (1a: identity, substrate, form, persistence,
producer, consumer; 1b: lineage, invalidation, regeneration, promotion) because a ten-column table
is unreadable; the rows are keyed identically.

**Classification** distinguishes three things the instruction's memory definition keeps apart:

- **accumulated** — material accumulated or changed through use, retained inside the boundary;
- **static-shipped** — retained material compiled into the artifact, not changed by use (documentation,
  tool specification): retained state, **not** memory;
- **emitted** — material that leaves the process and is not retained by the server at all.

### 1a. Identity, substrate, form, persistence, producer, consumer

| Part | Class | Storage substrate | Representational form | Persistence | Producer | Consumer |
|---|---|---|---|---|---|---|
| `OBJ-3` — validated `ThoughtData` record, one per accepted call (`index.ts:45-55`) | accumulated | process heap (a fresh object literal, not the caller's argument object) | structured record, 9 fields | process lifetime; no serialization (`ABS-2`) | `CMP-6` `validateThoughtData`, from model-authored `request.params.arguments` | `RTE-6` (append), `RTE-7` (conditional index), `CMP-7` `formatThought` (`index.ts:103`, current record only). Per-field consumer split below |
| `OBJ-4`-content — the `ThoughtData` elements held in `thoughtHistory` (`index.ts:26`, `:94`) | accumulated | process heap, append-only array | structured record array | process lifetime; unbounded, never pruned | `RTE-6`, unconditional on every valid call | **none inside the boundary** (`ABS-3`). No operation reads any element |
| `MEM-1` — history cardinality, the accumulated scalar view of `OBJ-4` (`index.ts:114`) | accumulated | derived on read from `OBJ-4.length`; not separately stored | integer | recomputed per read; lives as long as `OBJ-4` | implicitly by every `RTE-6` append | `RTE-9` → `OBJ-6.thoughtHistoryLength` → host LLM (`BAP-2`) |
| `OBJ-5`-content — the `ThoughtData` elements held in branch buckets (`index.ts:27`, `:96-101`) | accumulated | process heap, keyed buckets; elements are **the same object references** as the corresponding `OBJ-4` entries (see `MEM-4`) | keyed structured records | process lifetime; never pruned | `RTE-7`, only when `branchFromThought && branchId` are both truthy | **none inside the boundary** (`ABS-3`) |
| `MEM-2` — branch-key set, the accumulated key view of `OBJ-5` (created `index.ts:97-99`, read `:113`) | accumulated | property keys of the `branches` object | set of caller-authored strings | process lifetime; monotonic — a key is never removed | `RTE-7` lazy bucket creation, keyed by the model-supplied `branchId` | `RTE-9` → `OBJ-6.branches` → host LLM (`BAP-2`) |
| `OBJ-1` — tool description prose, 54 lines (`SRC-1a:135-188`) | static-shipped | string literal compiled into `dist/index.js` (`CMP-9`) | natural-language | shipped-artifact lifetime; invariant under use | authors, at build time | host LLM via `RTE-2`/`BAP-1`; placement into model context is host-owned and **uninspected** |
| `OBJ-2` — tool input JSON Schema, 9 properties (`SRC-1:189-234`) | static-shipped | object literal compiled into `dist/index.js` | symbolic | shipped-artifact lifetime; invariant under use | authors, at build time | host/model at call time via `RTE-2`; independently re-checked in-process by `RTE-4` (`BAP-4`) |
| `OBJ-9` — README doctrine (`SRC-2`) | static-shipped | repo file; **not** in `files: ["dist"]` (`SRC-3:13-15`), so not in the npm artifact | natural-language | repo lifetime | authors | human operator (`BAP-5`) |
| `OBJ-10` — distribution manifest (`SRC-3`) | static-shipped | repo file | symbolic config | repo lifetime | authors | npm / host launcher (`RTE-13`) |
| `OBJ-8` — rendered thought box, full `thought` text (`index.ts:58-84`, `:104`) | emitted | process stderr; the receiving sink is host-owned and **excluded from the boundary** | natural-language display | not retained by the server; downstream retention **uninspected** | `RTE-8`, per call, from the current record only — it never reads the store | human operator / log reader (`BAP-3`); **no consumer inside the boundary** |
| `OBJ-6` — success payload, 5 fields (`index.ts:106-117`) | emitted | MCP response over stdio | structured record → JSON text in one `text` content block | one response; server keeps no copy | `RTE-9` | host LLM (`BAP-2`) |
| `OBJ-7` — error payload (`index.ts:118-129`) | emitted | MCP response over stdio | structured record → JSON text | one response | `RTE-10` / `RTE-11` | host LLM. Carries **no** accumulated state at all — not even `thoughtHistoryLength` |

**Per-field consumer split inside `OBJ-3`.** The bundled record's fields differ by consumer, which
matters because it determines what the store could ever return:

| Field | Consumer(s) | Anchor |
|---|---|---|
| `thought` | `formatThought` → stderr only (`BAP-3`) | `index.ts:59`, `:76`, `:82` |
| `thoughtNumber`, `totalThoughts`, `nextThoughtNeeded` | stderr render, and echoed into `OBJ-6` **from the current record**, not from the store | `index.ts:110-112` |
| `isRevision`, `revisesThought` | stderr render only; no state operation (`ABS-6`) | `index.ts:64-66` |
| `branchFromThought`, `branchId` | index routing (`RTE-7`) + stderr render | `index.ts:67-69`, `:96-100` |
| `needsMoreThoughts` | **none anywhere** (`ABS-4`) — retained but unconsumed | `index.ts:54` |

This is the precise sense in which `OBJ-6`'s first three fields are **echo, not read-back**: they are
read off `validatedInput`, the current call's record (`index.ts:110-112`), never off `OBJ-4` or
`OBJ-5`. Only `branches` and `thoughtHistoryLength` are functions of accumulated state.

### 1b. Lineage, invalidation, regeneration, promotion

| Part | Lineage | Invalidation conditions | Regeneration conditions | Promotion path toward stronger form or force |
|---|---|---|---|---|
| `OBJ-3` | model-authored call arguments → **lossy 9-field whitelist projection** (`MEM-3`, `index.ts:45-55`: any key outside the whitelist is dropped) → **in-place field overwrite** by the `RTE-5` clamp at `index.ts:90-92`, applied *before* the push. The retained record therefore diverges from what the model submitted in the `totalThoughts` field, silently and without record of the original value | none post-store | none | **absent** (B0). No code path converts a record into any other form. `JSON.stringify` (`:109`) and `formatThought` (`:78-83`) are lossy renderings toward output, not promotions |
| `OBJ-4`-content | one append per accepted call, in acceptance order, no separators, no session key (singleton at `index.ts:249`). Rejected calls are **not** appended (`RTE-10`), so the array records accepted calls, not attempts | **absent** post-store (B0): no entry is removed, overwritten, marked, superseded, or expired. Whole store is discarded on process exit, including the `process.exit(1)` path at `index.ts:277` | **absent**: a restarted process starts empty; nothing rebuilds it (`ABS-2`) | **absent** (B0) |
| `MEM-1` | derived from `OBJ-4` length; monotonically increasing, one per accepted call | recomputed on each read | recomputed on each read | **absent** |
| `OBJ-5`-content | the record is stored **twice by reference**, once in `OBJ-4` and once in the bucket (`MEM-4`). This is an index over `OBJ-4`, not a second copy | **absent** post-store | **absent** | **absent** |
| `MEM-2` | keys are model-authored `branchId` strings, cast without type check (`index.ts:53`) and used directly as object keys, so a non-string value is coerced by JS property access. Lazy creation only; no key normalization, validation, or namespacing | **absent**: monotonic, a branch cannot be closed or removed | **absent** | **absent** |
| `OBJ-1`, `OBJ-2` | authored at build time; compiled into `dist/index.js` by `tsc` (`CMP-9`) | invalidated only by a new build and publish (`RTE-13`) | regenerated by rebuild | not applicable — already the shipped form. `OBJ-2` already carries the strongest force in the boundary (`BAP-4`, enforcing) |
| `OBJ-9`, `OBJ-10` | authored; `OBJ-9` is not shipped in the npm artifact | new commit | rewrite | not applicable |
| `OBJ-8` | current record → chalk/unicode render; the render reads the record, never the store (`index.ts:103`) | not retained by the server | re-emitted only if the same call recurs | **absent** inside the boundary. Whether the host's stderr sink turns it into durable material is **uninspected** |
| `OBJ-6`, `OBJ-7` | constructed per call and returned | — | — | **absent** |

**Nothing in the boundary carries a `consolidate`, `import`, `merge`, or `distil` label**, so there is
no lineage or curation label available to be mistaken for semantic preservation. The append at
`index.ts:94` asserts no transformation and warrants none: it is raw retention of a normalized
record.

---

## 2. Write side vs read-back

### 2.1 Write agency

**Automatic within the server; agent-triggered at its boundary.** Every valid `tools/call` writes
(`index.ts:94`, unconditional). There is no manual write path, no operator write API, no
configuration that could disable, filter, or throttle writing (`ABS-1`, `ABS-2`). The *content* is
authored entirely by an external agent, the host LLM, which is excluded from the boundary; the
*decision to write* is not the server's at any point.

There is exactly one gate between an agent's utterance and the store: `RTE-4` / `BAP-4`, four
presence-and-type predicates over the envelope (`index.ts:32-43`). It checks nothing about the
substance of a thought (`ABS-5`). Status: `implemented`.

### 2.2 Acquisition, index maintenance, curation — separated

| Function | Present? | Mechanism / evidence |
|---|---|---|
| Acquisition | `implemented` | `RTE-4` envelope gate → `RTE-6` unconditional append (`index.ts:88-94`). No relevance, novelty, or quality condition (`ABS-9`) |
| Normalization | `implemented` | `MEM-3`: the whitelist projection at `index.ts:45-55` plus the pre-push clamp `RTE-5`. Lossy in two directions — unknown keys dropped, `totalThoughts` overwritten |
| Index maintenance | `implemented`, thin | `RTE-7` only. A single flat keyed index over caller-supplied `branchId`, lazy bucket creation, no key hygiene. The gate is `branchFromThought && branchId` **truthiness** (`index.ts:96`), so `branchId: ""` or `branchFromThought: 0` silently skips indexing while the thought still lands in `OBJ-4` — a silent index miss with no error and no signal to the caller |
| Curation | **absent** (B0) | See breakdown below |

**Curation breakdown.** Each is `absent` within B0, and each names what it prevents:

| Operation | Status | Evidence | Conclusion prevented |
|---|---|---|---|
| Consolidation | `absent` | No operation reads any stored element (`ABS-3`; only reads are `index.ts:113-114`) | Prevents any claim that stored thoughts are merged, summarized, or compacted |
| Deduplication | `absent` | `index.ts:94` pushes with no comparison to any prior entry | Prevents any claim that repeated or near-identical thoughts are collapsed |
| Evolution / revision effect | `absent` | `ABS-6`: `isRevision` and `revisesThought` are stored and rendered, but no state operation links, supersedes, marks, or removes a target entry; the revising thought is appended like any other | Prevents any claim of a revision graph, supersession, or corrected history. Revision is **labelled, not effected** |
| Synthesis | `absent` | No read of content exists to synthesize from (`ABS-3`) | Prevents any claim that the server produces a derived or distilled artifact from the store |
| Invalidation | `absent` | No entry is removed, overwritten, or marked after the push. The only field write, `RTE-5`, happens *before* storage | Prevents any claim of post-hoc correction or retraction |
| Decay / eviction / bounding | `absent` | No TTL, cap, compaction, or eviction; array is append-only and unbounded (runtime §5.4, Performance) | Prevents any claim that the store is bounded or self-limiting in a long session |
| Promotion | `absent` | No serialization, file, or export path (`ABS-2`) | Prevents any claim of a path from in-memory record toward a stronger form or force |

### 2.3 Raw traces vs distilled artifacts

There is **no distilled tier**. The store holds normalized raw records (`MEM-3`); the only
non-raw accumulated artifacts are `MEM-1` and `MEM-2`, which are a cardinality and a key set —
aggregate projections, not content distillations. Whether the raw records are traces or working
material is not settled inside the boundary, because nothing consumes them.

### 2.4 Read-back — does the derived return count?

**Definition applied as given:** memory read-back is material accumulated or changed through use
returning to a later invocation or action.

**Yes, the derived return at `index.ts:113-114` is read-back, and it is the only read-back in the
system.** Both values are functions of state accumulated across prior invocations, and both are
returned into a later invocation's response. Three precisions bound what that means:

1. **It is fused with a same-turn increment.** The write (`:94`) precedes the read (`:113-114`)
   inside a single `processThought` call. The returned `thoughtHistoryLength` therefore equals
   *(accepted calls before this one) + 1*, and a newly created branch key appears in the very
   response that created it. The accumulated component is real, but it never arrives alone.
2. **What it can carry.** `thoughtHistoryLength`: a count of accepted calls on this process since
   start — scoped to the process, not the conversation, because the singleton at `index.ts:249`
   has no session key or request partition. `branches`: the set of distinct caller-authored branch
   labels ever opened. Note carefully — **`branches` is the one place accumulated, model-authored
   *text* returns to the model.** This does not contradict `ABS-3`, which is scoped to stored
   thought *content*; branch labels are identifiers stored as keys, and they do come back.
3. **What it cannot carry.** No thought text, no thought metadata, no per-entry addressing, no
   ordering, no branch membership (the response gives the key set only, never which thoughts are in
   a branch), and no indication that any prior call was rejected other than through the counter.

**What a receiving agent could actually do with it** (`implemented`-level reasoning about
affordance; `ABS-8` prevents any claim that an agent does any of this):

- confirm the call was accepted at all — an error payload (`OBJ-7`) omits the counters entirely;
- recover branch labels it opened earlier and has since lost from its own context — the only
  genuine recall the channel offers;
- detect a divergence between its own expected count and `thoughtHistoryLength`, which would
  indicate either rejected calls (`RTE-10` does not append) or another conversation multiplexed
  onto the same process.

It **cannot** retrieve, review, resume, re-read, verify, or reason over any prior thought.

The sharp asymmetry: in the ordinary single-conversation case the model authored every thought in
the store, so the projection is largely redundant with the model's own context — the server returns
a count of what the caller itself sent. The store's function inside the boundary is therefore
closer to a write-only ledger with a receipt than to a memory the agent reads.

### 2.5 The stderr path, stated exactly (`RTE-8`, `OBJ-8`, `BAP-3`)

Full thought content **does** leave the process here, on every valid call, unconditionally and
untunably (`ABS-1`). It is the richest output in the system and the only place the `thought` string
exits. Under this lens's definitions:

- It is **not read-back.** It is push-emitted at write time toward a human log reader (`BAP-3`),
  not returned to a later invocation or action of any agent. Nothing in the boundary consumes it.
- It is **not a store read.** `formatThought` is called on `validatedInput` (`index.ts:103`) and
  reads only the current record (`index.ts:59`). Even the rich channel performs no read of `OBJ-4`
  or `OBJ-5`.
- It is **not retained by the server.** Whether it accumulates depends on the host's stderr
  handling, which the boundary excludes and this lens did not inspect.

The system's richest content channel points away from the agent that produced the material and
carries display-only force.

---

## 3. Context-route annotation

`RTE-9` is the read-back route. `RTE-2` is annotated as well, because it is the system's other
outbound context route and its annotation is load-bearing as a negative: it is where the memory
mechanism is *not*.

### `RTE-9` — success response construction (`index.ts:106-117`)

| Field | Annotation |
|---|---|
| **Read-back direction** (receiving agent's perspective) | **Pull**, at the transport level: the host LLM's own `tools/call` elicits the response, and the server never initiates (no `sampling` capability, `ABS-10`; passive responder after `connect`, Loop A). At the content level the projection is **unrequested** — there is no query parameter, filter, or state argument in `OBJ-2` (`index.ts:189-234`), so the agent cannot ask for state, cannot ask for more, and cannot ask for less. It gets the same five fields for calling the tool |
| **Selection signal** | **None.** The payload is a fixed five-field shape computed unconditionally at `index.ts:106-117`. No relevance, recency, similarity, query, or budget signal exists (`ABS-9`, `ABS-3`). Selection is degenerate — constant shape, aggregate values |
| **Targeting** | **None.** `Object.keys()` and `.length` are whole-store aggregates. No per-entry addressing exists anywhere in the boundary; there is no retrieval primitive to target with |
| **Selection scope and budget** | Scope: the entire process-global store since process start — not conversation-scoped, because `thinkingServer` is a module-scope singleton (`index.ts:249`) with no session partition. Budget: unmanaged. `thoughtHistoryLength` is O(1) in payload size regardless of store size; `branches` grows linearly with the number of distinct caller-supplied labels and is never truncated, capped, or token-budgeted. The one unbounded payload component is thus under the caller's own control |
| **Delivery and consumption point** | Delivered as a single MCP `text` content block holding `JSON.stringify(..., null, 2)` (`index.ts:109-115`), returned from the `CallToolRequestSchema` handler (`index.ts:255-258`) over stdio. Framing over the wire is the SDK's (`SRC-6`, **uninspected**). The consumption point — whether and where the host places tool results in model context — is **host-owned and excluded from the boundary**. Status is affordance only: the server delivers to the transport; `BAP-2`'s horizon is one turn "unless the host retains it" |
| **Behavioral-faithfulness test** | **Absent** (B0). No test, fixture, assertion, trace, or run artifact exists (`ABS-8`), and no in-code check compares the returned counters against anything. Prevents any conclusion that delivery, parsing, or interpretation of the projection is faithful, and prevents any conclusion that the counters are correct in the presence of concurrency |

### `RTE-2` — tool advertisement (`index.ts:251-253`), annotated as a negative

| Field | Annotation |
|---|---|
| **Read-back direction** | Pull (host-elicited `tools/list`) — but what is delivered is **static shipped material** (`OBJ-1`, `OBJ-2`), which under the given definition is retained state, **not** memory read-back |
| **Selection signal** | None. Unconditional return of one static array literal; the handler ignores its request argument entirely (`index.ts:251-253`) |
| **Targeting** | None |
| **Selection scope and budget** | Fixed: 54 lines of prose plus a 9-property schema, byte-identical on every call. Does not grow, shrink, or vary with use, session, or accumulated state |
| **Delivery and consumption point** | `tools/list` response over stdio; placement into model context is host-owned and **uninspected** (`BAP-1`: "the server affords, the host disposes") |
| **Behavioral-faithfulness test** | **Absent** (B0, `ABS-8`) |

**The load-bearing annotation:** `RTE-2` never consults `OBJ-4` or `OBJ-5` (`ABS-3`; runtime §5.2
Loop B records "state reads and writes: none"). There is no mechanism by which accumulated use
changes what is advertised to the model — no adaptive description, no learned schema, no
history-conditioned instruction. The system's one authority-bearing channel toward the model
(`BAP-1`) is fixed at build time.

---

## 4. Four separate findings

Presence, wiring, activation, and causal effect are recorded separately with separate evidence.
None may be upgraded into the next.

### 4.1 Context presence

| Sub-claim | Status | Evidence | Ceiling / prevented conclusion |
|---|---|---|---|
| Accumulated material (`MEM-1`, `MEM-2`) is placed onto a route directed at the receiving agent | `implemented` | `index.ts:113-114` read the store; `:106-117` place the values into the returned content block | Cannot be raised: whether the block enters model context is host-owned and **uninspected** (host excluded, `evidence-packet.md` §2). Presence in *context* is therefore not established — only presence on the *wire* |
| Stored thought **content** is placed onto any route toward the model | **`absent`** (B0) | `ABS-3`: `rg 'thoughtHistory\|branches'` yields 8 hits, all enumerated in `RTE-6`/`RTE-7`/`RTE-9`; the only reads are `Object.keys()` and `.length` at `index.ts:113-114` | Prevents any claim that the server retrieves, returns, summarizes, or re-serves prior thoughts |
| Stored thought content reaches a **human** | `implemented` | `RTE-8`, `index.ts:103-104`, full `thought` text to stderr on every valid call | Not read-back (see §2.5). Whether any human reads the stream is outside the boundary |
| Static shipped instruction (`OBJ-1`) is placed onto a route toward the model | `implemented` | `RTE-2`, `index.ts:251-253` | Static material, not memory. Presence in model context host-owned, **uninspected** |

### 4.2 Deployed wiring

| Sub-claim | Status | Evidence | Prevented conclusion |
|---|---|---|---|
| The read-back route is wired end-to-end inside the inspected artifact | `implemented` | Handler registered at `index.ts:255-267`; `processThought` reached by name equality at `:256`; singleton constructed at module scope `:249` before `runServer()` | Dispatch into the handler is the SDK's (`SRC-6`, **uninspected**). Prevents any claim about request ordering or concurrency, and therefore about whether `OBJ-4` order corresponds to call order under load |
| The wiring inspected is the wiring that runs in a deployment | **not established** | `CMP-9`/`RTE-13`: `tsc` → `dist/index.js`, `files: ["dist"]` (`SRC-3:10-20`); the README's configuration (`SRC-2:47-59`) launches `npx -y @modelcontextprotocol/server-sequential-thinking` with **no version pin** | Combined with the ~20-month boundary age, this prevents any claim that a deployment following the documented configuration runs the analysed memory code |
| A store exists per conversation | **not established**; the code affords the opposite | Singleton at `index.ts:249`, no session key, no request identity, no partitioning | Prevents any claim that `thoughtHistoryLength` counts one conversation's thoughts. If a host multiplexes conversations onto one process, they interleave in one array with no separator. Whether hosts do this is outside the boundary |

### 4.3 Activation

**Status: `uninspected`.** Not `absent` — an absence would require a search boundary in which
activation could have appeared, and no such boundary exists here.

Evidence for the status: the behaving agent (the host LLM) is excluded from the boundary
(`evidence-packet.md` §2), and `ABS-8` records that no run artifact, trace, or log exists anywhere
in the boundary that could show a behavior change. There is no intervention, ablation, or
comparison available.

Prevented conclusions: any claim that delivered material changed model behavior; any claim that
the tool descriptor (`OBJ-1`, `BAP-1`) changes what the model does; any claim that the returned
counters are read, parsed, or acted on.

The strongest statement available is a bound on what activation *could* be: the read-back channel
carries only an accepted-call count and a set of branch labels (§2.4), so any behavior change
attributable to *memory* in this system would have to be one that a count and a label list can
support. It could not be a change grounded in the content of a prior thought, because that content
never returns (`ABS-3`).

### 4.4 Causal effect

**Status: `uninspected`.** No intervention, no comparison, no A/B, no with/without run exists
inside the boundary (`ABS-8`), and both halves of the loop that would have to show the effect — host
and model — are excluded.

Prevented conclusions: any claim that the retained store improves, structures, lengthens, or
otherwise changes reasoning; any claim that branching or revision labelling has an effect on
outcomes; any claim about the difference between calling this tool and not calling it.

Doctrine in `OBJ-1`/`OBJ-9` asserts reasoning outcomes (`CLM-1`–`CLM-3`, `CLM-5`, `CLM-10`), and
that doctrine is `claimed`, at advisory force (`BAP-1`), addressed to the model. It supplies no
evidence at any status about effect, and it is not upgraded here. Its truth, scope, and warrant are
the epistemic lens's to record.

---

## 5. Authority references

Referenced by ID; consumer, channel, force, and horizon are read off the register rather than
inferred from the family label.

| Path | Bearing on this lens |
|---|---|
| `BAP-1` | Consumer host LLM, channel `RTE-2`, force advisory, horizon host-determined. The material it carries is **static shipped**, not accumulated. So the system's only instruction-force path toward the model is fixed at build time and is not a memory path |
| `BAP-2` | Consumer host LLM, channel `RTE-9`, force **informational only — obliges nothing**, horizon one turn unless the host retains it. This is the read-back path. Its authority horizon (one turn) is shorter than the retention horizon of the material it reports on (process lifetime), which is in turn shorter than the conversation that produced it |
| `BAP-3` | Consumer human log reader, channel `RTE-8` stderr, force display only, **no consumer inside the boundary**. The richest content channel carries no behavioral force here |
| `BAP-4` | Consumer host/model at call time, channel `OBJ-2` plus in-process re-validation `RTE-4`, force **enforcing**, horizon every call for the process lifetime. This is the only gate on what enters the store — and it enforces envelope shape, not content (`ABS-5`). Four fields are checked; `revisesThought`, `branchFromThought`, `branchId`, `needsMoreThoughts` are cast without check (`index.ts:50-54`), so caller-supplied values of any type enter the store and, for `branchId`, become index keys |
| `BAP-5` | Consumer human operator, advisory setup. No memory bearing beyond `RTE-13`'s unpinned launch, recorded in §4.2 |

**No path in the register has a memory-derived consumer with binding force.** The one enforcing
path (`BAP-4`) constrains input into the store; nothing constrains, or is constrained by, what comes
out of it.

Lineage and curation labels are kept independent of transformation, acceptance, and warrant
throughout: the append at `index.ts:94` is retention, and retention establishes nothing about
semantic preservation, correctness, or acceptance of what was retained.

---

## 6. `MEM-*` proposals and corrections to registered records

### Proposals (lens-local until the orchestrator registers them)

| Tag | Proposed record | Concrete identity | Why it needs its own ID |
|---|---|---|---|
| `MEM-1` | History cardinality — the accumulated scalar view of `OBJ-4` | `index.ts:114` (`this.thoughtHistory.length`), written implicitly by the append at `index.ts:94` | It is one of exactly two accumulated parts with a consumer. `OBJ-4` as registered bundles a content array with a cardinality projection whose consumer, form, and authority path all differ (`BAP-2` vs no consumer at all) |
| `MEM-2` | Branch-key set — the accumulated key view of `OBJ-5`; monotonic, model-authored strings | created `index.ts:97-99`, read `index.ts:113` (`Object.keys(this.branches)`) | Same split as above for `OBJ-5`, and it is the **only** accumulated caller-authored text that returns to the caller. Bundling it with bucket content would hide that |
| `MEM-3` | Normalized-record projection — the lossy 9-field whitelist that determines what actually enters the store | `index.ts:45-55`, the object literal returned by `validateThoughtData` | It bounds what the store could ever hold or return: keys outside the whitelist are dropped, and the retained object is a fresh copy, not the caller's argument object. This is a lineage transform distinct from the `RTE-4` gate it sits inside |
| `MEM-4` | Reference aliasing between `OBJ-4` and `OBJ-5` — branch buckets hold the *same* object references as history entries | `index.ts:94` (`push(validatedInput)`) and `index.ts:100` (`push(validatedInput)`) | Determines that `OBJ-5` is an **index over** `OBJ-4`, not a second copy — the correct reading of the "stored twice" fact. Recorded in the runtime account's Loop C prose but carries no ID |

Two facts are cited against existing IDs rather than proposed as new records, since they are already
covered: the pre-store `totalThoughts` overwrite is `RTE-5` (`index.ts:90-92`), and its memory-lens
consequence is that the retained record diverges from the submitted value in one field with no trace
of the original; the silent branch-index miss on falsy `branchId`/`branchFromThought` is a property
of `RTE-7` (`index.ts:96`).

### Corrections to registered records

**None.** Every registered record this lens depended on (`OBJ-3`–`OBJ-8`, `RTE-2`, `RTE-5`–`RTE-10`,
`ABS-2`–`ABS-9`, `BAP-1`–`BAP-4`) was checked against `index.ts` and found accurate, including
`ABS-3`'s claim of exactly two read sites and `ABS-4`'s claim that `needsMoreThoughts` has no
consumer (verified: declared `:21`, copied `:54`, documented `:175`, schema'd `:228`, read nowhere).
All contributions above are extensions by ID, not re-inventories.

One scoping note, not a correction: `ABS-3` is scoped to stored thought **content**, and this lens
relies on that scoping. `MEM-2` shows that accumulated caller-authored *identifiers* do return via
`Object.keys` at `index.ts:113`. Reading `ABS-3` as "nothing accumulated ever returns" would be
wrong; as written it is correct.

---

## 7. Limitations, each with the conclusion it prevents

| Limitation | Conclusion it prevents |
|---|---|
| `ABS-8` — no test, fixture, trace, log, or run artifact anywhere in the boundary | Prevents **every** `observed` and `causally supported` status in this lens. Caps §4.1 and §4.2 at `implemented` and leaves §4.3 and §4.4 at `uninspected` |
| The host is excluded from the boundary (`evidence-packet.md` §2) | Prevents any claim that the read-back projection or the tool descriptor enters model context. Context presence is established on the wire only |
| The host LLM is excluded from the boundary | Prevents any claim of activation or causal effect, and any claim about what a model does with the counters |
| `SRC-6` — `@modelcontextprotocol/sdk` 0.5.0 uninspected, `node_modules/` absent | Prevents any claim about wire framing of `OBJ-6`, about pre-handler validation, and about request ordering or concurrency — and therefore prevents any claim that `OBJ-4`'s order corresponds to call order, or that `thoughtHistoryLength` is race-free |
| Host stderr handling is uninspected | Prevents the stronger reading of `ABS-2`. `ABS-2` licenses "the **server** performs no persistence"; it does **not** license "thought content is never durably retained anywhere", because `RTE-8` writes full thought text to a host-owned sink |
| Boundary age (~20 months) plus the README's unpinned `npx -y` launch (`RTE-13`, `SRC-2:47-59`) | Prevents any claim that a deployment following the documented configuration runs the memory behavior analysed here, and any claim about the current upstream state of this server |
| Multiplexing behavior of hosts is outside the boundary | Prevents any claim that the store is conversation-scoped, and therefore prevents interpreting `thoughtHistoryLength` as a count of one conversation's thoughts. The code affords sharing; whether hosts share is not established |
