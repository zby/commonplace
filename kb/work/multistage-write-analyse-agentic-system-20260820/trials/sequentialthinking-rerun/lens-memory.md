# Lens output — memory/context — run `AGS-2026-08-21-SEQTHINK`

Depth: **brief**, per `SCOPE-MEM`. Brief means proportionate coverage of every numbered item, not silent omission. Inspected boundary for this lens: `SRC-1` (full file, 279 lines), `SRC-2` (full file, 63 lines), `SRC-3` (full file). Nothing outside the frozen boundary was read.

**Headline.** Retention is total and unmanaged; retrieval of retained *content* is nil. Two derived values return to a later consumer invocation — `thoughtHistoryLength` (a count) and `branches` (a key set). The `branches` array is the only accumulated caller-authored *text* that comes back, and it comes back as opaque labels with no content attached. There is no selection, no targeting, no budget, no curation, no invalidation, and no persistence past the process. Every artifact-side conclusion here is `implemented`; nothing in this run reaches `observed` or `causally supported`.

---

## 1. Inventory of retained operative parts

`OBJ-3` is a bundled artifact under the lens's splitting rule: its key set and its bucket contents differ in consumer, in checks, and in authority path. It is split below as parts P2 and P3, and that split is returned as amendment `MEM-AMD-1` rather than as a new inventory record.

| Part | Registered as | Storage substrate | Representational form | Persistence | Lineage | Producer | Consumer | Invalidation / regeneration | Promotion path |
|---|---|---|---|---|---|---|---|---|---|
| P1 `thoughtHistory` | `OBJ-2` | V8 heap, one module-level instance (`SRC-1:249`), no file, no DB, no network (`ABS-1`) | array of typed in-memory records | process lifetime; unbounded, no cap | `append` only (`RTE-5`, `SRC-1:94`) | `CMP-1` write path, over `EXT-3`-authored input | **only** `.length` (`SRC-1:114`) → `OBJ-4` | none — no clear, truncate, evict, decay, or TTL exists (`MEM-1`); regeneration impossible, nothing is derived from a source | none |
| P2 `branches` key set | part of `OBJ-3` | same heap object's own-property names | caller-authored opaque string labels | process lifetime; grows monotonically with distinct `branchId` values | `create-on-first-use` (`RTE-6`, `SRC-1:97–99`) | `EXT-3` authors the label; `CMP-1` admits it unvalidated (`SRC-1:53`) | `Object.keys` (`SRC-1:113`) → `OBJ-4` → `BAP-2` | none (`MEM-1`) | none — a label is never checked, normalized, deduplicated beyond object-key identity, or lifted into the schema |
| P3 `branches` bucket contents | part of `OBJ-3` | same heap; arrays of **references** to P4 objects already in P1 | array of typed in-memory records (aliases) | process lifetime | `append` (`SRC-1:100`) | `CMP-1` | **no consumer at all** — no route reads a bucket's elements | none (`MEM-1`) | none |
| P4 retained `ThoughtData` record | `OBJ-1` | heap object, single instance shared by P1 and P3 | typed record: one natural-language `thought` string plus eight control fields | process lifetime | `validate → mutate (RTE-4) → retain` | `EXT-3` authors `thought`; `CMP-1` validates four fields, casts five unchecked (`SRC-1:29–56`) | `CMP-5` render (`SRC-1:104`), then nothing | in-place mutation of `totalThoughts` before retention is the artifact's only write-over of acquired data (`MEM-AMD-4`); no versioning, no supersession (`ABS-6`) | none |
| P5 `OBJ-6` stderr render | `OBJ-6` | none — written to fd 2 and dropped | ANSI text box | **not retained** | `reshape-for-display` | `CMP-5` | no in-boundary consumer (`BAP-3`) | n/a | none |
| P6 `OBJ-5` / `OBJ-7` tool spec | `OBJ-5`, `OBJ-7` | shipped source constant | natural-language + JSON Schema | shipped, immutable at runtime | authored, not accumulated | package authors | `EXT-3` via `RTE-1` | n/a | n/a |

P5 and P6 are listed for completeness and are **out of scope as memory**: P6 is static shipped material, which the run's definition excludes from read-back; P5 is retained by nobody. P6 is nonetheless the artifact's strongest behavioral channel (`BAP-1`), which is a fact about instruction, not about memory.

**Checks on retained parts.** `RTE-3` checks four fields for JSON presence and type at the acquisition boundary and nothing thereafter. `branchId` and the four other optional fields are cast, not validated (`SRC-1:50–54`). No check of any kind runs against retained state after a write. Nothing inspects, scores, or compares a `thought` (`ABS-3`).

## 2. Write side separated from read-back

**Write agency: automatic, unconditionally, on every accepted call.** There is no manual write, no opt-in, no opt-out, no caller-visible switch, and no configuration. A caller cannot suppress retention; the only way to not be recorded is to fail validation.

| Write-side function | Present? | Evidence / search boundary |
|---|---|---|
| Acquisition | yes — `RTE-3` boundary check, then `RTE-5` append (`SRC-1:29–56, 94`) | `SRC-1` full file |
| Index maintenance (distinct from acquisition) | yes — `RTE-6` maintains `branches` as a secondary index over the same P4 objects, keyed by caller-supplied label; bucket created on first use (`SRC-1:96–101`). This is the only structure-building write | `SRC-1` full file |
| Curation | **absent** — no selection, ranking, pruning, tagging, or editorial step of any kind | `SRC-1` full file: the only mutations of retained state are `SRC-1:94` and `SRC-1:97–100`, both unconditional-or-predicated appends |
| Consolidation | **absent** | same boundary |
| Deduplication | **absent** — identical thoughts append twice; object-key collision on `branchId` merges buckets but that is a hash-map property, not a dedup step | same boundary |
| Evolution / supersession | **absent** — `isRevision`/`revisesThought` are stored and used only to pick a stderr label (`SRC-1:64–66`); no prior entry is marked, replaced, or removed (`ABS-6`) | same boundary |
| Synthesis / distillation | **absent** (`ABS-9`) | same boundary |
| Invalidation | **absent** — no clear, reset, truncate, splice, pop, shift, reassignment, or `delete`; proposed as `MEM-1` | `SRC-1` full file; `SRC-2` full file; `OBJ-7` schema (no reset parameter) |
| Decay / TTL / size bound | **absent** — growth is unbounded for process lifetime (`RTE-5`) | same boundary |
| Promotion to stronger form or force | **absent** — nothing ever moves from in-memory to durable, from string to schema, or from informational to enforcing | `SRC-1` full file; `ABS-1` |

**Raw traces versus distilled artifacts.** P1 is a pure raw trace: every accepted call, in arrival order, verbatim. There is no distilled retained artifact anywhere — the only distillation in the system (`OBJ-4`'s two derived values) is computed at read time and never stored. P3 is a raw trace re-partitioned by label, not a distillation.

**Read-back, stated exactly.** Under the run's definition, read-back exists and is real: `thoughtHistoryLength` and `branches` are computed from material accumulated in earlier consumer invocations and are delivered into a later one. That a long-lived process holds them does not make them current-run state. But no retained *content* returns: `OBJ-2` is read only for `.length`, `OBJ-3` only for its keys, and no route returns a stored `thought` string (`ABS-2`). The content of every retained thought leaves the process exactly once, on stderr, through a channel the consuming model never reads (`RTE-9`, `BAP-3`) — which sharpens the finding rather than softening it.

**Lineage labels carry no epistemic weight.** `append` (`RTE-5`), `create-on-first-use` (`RTE-6`), and `derive` (`Object.keys`, `.length`) are lineage descriptions only. None establishes that a retained thought is true, accepted, warranted, or semantically preserved. A `branchId` returned in `OBJ-4` is an opaque token: its reappearance says a label was used before, not that the branch it names still means anything.

## 3. The runtime-owned context route

There is exactly one read-back route: `RTE-7` → `OBJ-4`, on path `BAP-2`.

| Dimension | Value | Evidence |
|---|---|---|
| Read-back direction (receiving agent's perspective) | **pull, and only pull.** Delivery is the return value of a call the consumer itself made. No push channel exists: the artifact cannot initiate, has no timer, callback, notification, or continuation (`ABS-10`), and `RTE-9`'s stderr write goes to a party outside the consumer path (`BAP-3`) | `SRC-1:106–117`, `SRC-1:255–267`, `ABS-10` |
| Selection signal | **none.** The same five fields are computed the same way on every call. No query, no relevance score, no recency, no similarity, no caller-supplied selector. `branchId` in the request does not filter the returned key set | `SRC-1:109–115` |
| Targeting | **none.** Not addressed to a task, topic, branch, or thought range. `thoughtNumber` and `branchId` arrive in the request and steer only the write side | `SRC-1:106–117` |
| Selection scope | whole retained state, but only its cardinality and its key names — never its elements | `SRC-1:113–114`, `ABS-2` |
| Budget | **none implemented.** No token cap, item cap, or truncation. The `branches` array is caller-controlled and monotone: distinct `branchId` values accumulate without limit, so read-back payload size grows with use and never shrinks (`MEM-AMD-2`) | `SRC-1:113`; `MEM-1` (no invalidation) |
| Delivery point | one MCP text content block, `JSON.stringify(..., null, 2)`, in the tool result | `SRC-1:106–116` |
| Consumption point | owned by `EXT-2` — where and whether the tool-result block lands in a model's context is outside the boundary | `EXT-2`, `BAP-2` |
| Behavioral-faithfulness test | **absent.** Nothing checks that the returned count or key set corresponds to anything the consumer believes; nothing verifies the consumer used them (`ABS-3`) | `SRC-1` full file |
| Post-turn capture / consolidation | `RTE-5`/`RTE-6` are write-side maintenance on the same synchronous call, not a second read-back point. There is no second read-back point | `SRC-1:86–130` |

Two read-back defects follow, returned as amendments: the `branches` field is verbatim accumulated caller text rather than a summary and is unbounded (`MEM-AMD-2`); `thoughtHistoryLength` is a process-lifetime counter of accepted calls, not a measure of the current thinking sequence (`MEM-AMD-3`).

## 4. Presence, wiring, activation, causal effect — four separate findings

| Finding | Status | Evidence | Boundary and the conclusion it prevents |
|---|---|---|---|
| **Context presence (artifact side).** `RTE-7` assembles `OBJ-4` into an MCP content block on every successful call; `RTE-1` returns `OBJ-5`/`OBJ-7` verbatim to a tool-list request | **implemented** | `SRC-1:106–117`, `SRC-1:251–253` | `SRC-1` full file. Prevents nothing about the artifact; establishes only that the material is emitted, not that it enters any context |
| **Context presence (consumer side).** Whether `OBJ-4` or `OBJ-5` reaches a model's context window | **uninspected** | — | `EXT-2` is uninspected and owns tool-list injection and transcript assembly. Prevents any claim that read-back material is present to a model |
| **Deployed wiring.** A `claude_desktop_config.json` entry launching the server via `npx` | **claimed** — doctrine only | `SRC-2:43–59` | Register gap: no host configuration inspected, no npm tarball inspected. Prevents any claim that this server is deployed anywhere in the field |
| **Activation.** Evidence that delivered material changed `EXT-3`'s behavior | **uninspected** (explicitly *not* `absent`) | — | No tests, fixtures, logs, or traces exist in the subtree or repo root (`ABS-4`). Prevents any `observed` status. The artifact affords no activation evidence either: it records nothing about what the caller did with `OBJ-4` |
| **Causal effect.** That read-back caused a behavior change | **uninspected** | — | `ABS-4`, plus absence of any experiment in the register. Prevents every `causally supported` status this run could otherwise reach |

No upgrade is made anywhere: emission is not presence, presence is not activation, `implemented` is not `observed`, and the doctrine's configuration example is not deployment.

## 5. Behavioral authority for the memory paths

Authority is reported in four parts; the family label is not a substitute for them.

| Path | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|
| `BAP-2` (the read-back path) | `EXT-2`, and through it `EXT-3` | `OBJ-4` in the tool result | **informational** — no directive content, no enforcement, no consequence for ignoring it | the single call that produced it, plus whatever transcript retention `EXT-2` applies |
| `BAP-3` (the content-egress path) | none inside the boundary | `OBJ-6` on fd 2 | none implemented | process lifetime |
| `BAP-4` (the acquisition gate) | `EXT-2`'s argument construction, then `RTE-3` | `OBJ-7` JSON Schema | **enforcing on argument shape** for four required fields; silent on the other five | as `BAP-1` |

Note on horizons, which differ and must not be collapsed: the *delivery* horizon of `BAP-2` is one call, while the *material's* accumulation horizon is the whole process lifetime (`ABS-1`, `ABS-5`). A consumer reading `OBJ-4` at call *n* is being handed a value shaped by every call since process start, including calls from earlier, unrelated thinking episodes.

Epistemic and operational authority stay separate here and both are weak on the memory paths. `BAP-2` licenses no content (it returns a count and a label list, neither asserting anything about the world) and permits or blocks no behavior (`ABS-10` — the artifact does not pace or terminate the loop; `nextThoughtNeeded` is echoed unchanged). The artifact's only strong authority is `BAP-1`, an instruction channel, which is not memory.

---

## Proposals (`MEM-n`)

**`MEM-1` — evidenced absence: no invalidation, reset, or clear operation for retained state.**
Identity: an absence over the state mutators of `SequentialThinkingServer` in `/home/zby/llm/servers/src/sequentialthinking/index.ts`, symbols `thoughtHistory` (declared `SRC-1:26`) and `branches` (declared `SRC-1:27`).
Recorded search boundary: `SRC-1` full file — every occurrence of both symbols enumerated (`thoughtHistory`: 26, 94, 114; `branches`: 27, 97, 98, 100, 113); every one is an initializer, an append, a bucket create, or a derived read. No `delete`, `splice`, `pop`, `shift`, `length = 0`, or reassignment exists. Plus `SRC-2` full file (no documented reset) and `OBJ-7` (`SRC-1:189–234`, no reset or session parameter).
Status: `absent`.
Conclusion it supports: the only way to drop retained state is process termination, so retention duration is entirely `EXT-2`'s launch decision, not the artifact's.
Conclusion it prevents: any claim that a caller, a session boundary, or the artifact itself can bound, scope, or expire what has accumulated.
Distinct from `ABS-1` (no durable persistence), `ABS-5` (no per-session isolation), and `ABS-6` (no revision applied to history), none of which state the absence of a discard path.

## Corrections (`MEM-CORR-n`)

**`MEM-CORR-1` — `ABS-2`'s recorded search boundary is misstated at the scope given; the absence itself stands.**
`ABS-2` states its boundary as "every read of `thoughtHistory`/`branches` enumerated (`SRC-1:113–114`)", and the `OBJ-3` row says it is "read **only** for `Object.keys` (`SRC-1:113`)". `branches` is in fact also read on the write side, twice: `SRC-1:97` (`if (!this.branches[validatedInput.branchId])`, an existence check that decides whether to create a bucket) and `SRC-1:100` (`this.branches[validatedInput.branchId].push(...)`, resolving the bucket reference to append into).
Evidence anchor: `SRC-1:96–101`.
What survives: the absence claim is true — neither read retrieves a stored `thought`, and no route returns retained content. What is defective: the enumeration is incomplete and the word "only" overstates it, which matters because it hides the artifact's single instance of retained state feeding a control decision (index maintenance, item 2 above). Correction, not re-inventory: `ABS-2` and the `OBJ-3` row should read "read for content by nothing; read on the write side at `SRC-1:97,100` for bucket existence and resolution; read for derivation at `SRC-1:113–114`."

## Amendments (`MEM-AMD-n`)

**`MEM-AMD-1` — `OBJ-3` bundles two parts with different consumers, checks, and authority paths.** The key set of `branches` is consumed by `RTE-7` and travels `BAP-2` to `EXT-3`; the bucket contents have no consumer anywhere in the boundary. Under the lens's splitting criterion (consumer and authority path differ) they are separate retained parts, inventoried above as P2 and P3. Evidence anchor: `SRC-1:113` (keys read) versus `SRC-1:96–101` (buckets written, never read for elements). Superseded value: none — `OBJ-3`'s single-row description is amended, not replaced.

**`MEM-AMD-2` — the `branches` field of `OBJ-4` is verbatim accumulated caller text, not a derived summary, and is unbounded.** `RTE-7` describes `branches` as one of "two values derived from retained state". The derivation is in *selection* only (keys, not values); the tokens returned are the exact strings `EXT-3` supplied on earlier calls, admitted without validation (`SRC-1:53`). This makes it the **only** accumulated caller-authored text that ever returns to a consumer, which is the memory lens's central positive finding. Second part: the array has no cap and no discard path (`MEM-1`), so it grows monotonically with the number of distinct `branchId` values used in the process and never shrinks. Evidence anchor: `SRC-1:53`, `SRC-1:113`. Superseded value: the "derived" characterization in the `RTE-7` progression field.

**`MEM-AMD-3` — `thoughtHistoryLength` is a process-lifetime counter of accepted calls, not a measure of the current thinking sequence.** It is `this.thoughtHistory.length` (`SRC-1:114`) over an array that receives an unconditional append per accepted call (`SRC-1:94`), including revision thoughts and branch thoughts. It never resets (`MEM-1`) and, with one module-level instance serving the whole process (`ABS-5`), it spans every thinking episode that process handles. Consequences: it can diverge arbitrarily from the caller's `thoughtNumber` echoed two fields above it in the same JSON object; and a second episode starting at `thoughtNumber: 1` receives a count carrying the first episode's calls. Evidence anchor: `SRC-1:94, 110, 114`, `SRC-1:249`. This bounds `CLM-5` ("maintain context over multiple steps") on the memory side: the artifact maintains an accumulation, and the one number it reports about that accumulation does not describe the step sequence the claim is about.

**`MEM-AMD-4` — retention is by shared reference, and the retained record is the mutated one.** `RTE-4` mutates `validatedInput.totalThoughts` in place at `SRC-1:90–92`, *before* both retention writes; the same object reference is then pushed into `thoughtHistory` (`SRC-1:94`) and, when eligible, into a `branches` bucket (`SRC-1:100`). Three consequences for the memory model: there is exactly one copy, so the two containers cannot diverge and there is no versioning or provenance separation between them; retained history preserves the coerced `totalThoughts`, not the value the caller sent, so the artifact's single write-over of acquired data is silent and unrecorded; and `formatThought` (`SRC-1:103`) likewise renders the post-coercion value, so even the stderr trace does not preserve the original. Evidence anchor: `SRC-1:88–104`. Attaches to `OBJ-1`, `RTE-4`, `RTE-5`, `RTE-6`.

**`MEM-AMD-5` — `RTE-6`'s eligibility predicate fails silently, and it gates the only content channel that returns.** The predicate is `validatedInput.branchFromThought && validatedInput.branchId` (`SRC-1:96`) — a truthiness test on two fields neither of which is validated (`SRC-1:52–53`). A call supplying `branchId` but omitting `branchFromThought`, or sending a falsy value for either, produces no bucket, no error, and no signal: the thought lands in `thoughtHistory` and the label vanishes. Because the key set is the only accumulated authored text that returns (`MEM-AMD-2`), a silent write-side drop here is a silent read-back loss, and the caller's next `OBJ-4` shows the omission only as a label that never appears. Evidence anchor: `SRC-1:52–53, 96–101, 113`. Attaches to `RTE-6`; related to but distinct from `ABS-7` (`needsMoreThoughts` is never read at all; `branchId` is read, conditionally).

## Targeted reads made

All within the frozen boundary, read-only. No scope expansion beyond what the register already records.

| File | Scope read | Already in register at this scope? |
|---|---|---|
| `/home/zby/llm/servers/src/sequentialthinking/index.ts` | whole file, 279 lines | yes — `SRC-1` |
| `/home/zby/llm/servers/src/sequentialthinking/README.md` | whole file, 63 lines | yes — `SRC-2` |
| `/home/zby/llm/servers/src/sequentialthinking/package.json` | whole file | yes — `SRC-3` |

Not read by this lens: `tsconfig.json` (`SRC-4`), the root manifests (`SRC-5`), the root README (`SRC-6`). Nothing was fetched, refreshed, or mutated.

## Evidence limitations, each paired with the conclusion it prevents

| Limitation | Conclusion it prevents |
|---|---|
| No run traces, tests, fixtures, or logs anywhere in the subtree or repo root (`ABS-4`) | Prevents every `observed` and `causally supported` status in this lens. Every artifact-side finding above is capped at `implemented`. In particular: no claim that read-back ever occurred, that a `branches` array was ever non-empty in a real session, or that any consumer read either derived value |
| `EXT-2` uninspected — it owns process launch, tool-list injection, and transcript assembly | Prevents any claim about whether `OBJ-4` enters a model's context, how long the process lives (and therefore the real duration of the read-back window), or whether one process serves one client. `ABS-5`'s practical bound on state sharing rests on `EXT-2`'s launch model, which is `claimed` from `SRC-2:47–58` and not verified |
| `EXT-3` uninspected | Prevents any activation finding: no evidence exists that the returned count or label set changed a model's behavior, and none could be produced from within this boundary |
| `EXT-1` (`@modelcontextprotocol/sdk` 0.5.0) uninspected; no `node_modules` in the checkout | Prevents any claim about whether the tool result is delivered intact, whether cancellation could interrupt a call between validation and retention, or whether concurrent requests could interleave the write path. The single-threaded, synchronous shape of `processThought` (`SRC-1:86–130`) makes interleaving within one call implausible, but that is an inference from the artifact, not an inspected property of the dispatcher |
| No `dist/`, no published tarball inspected | Prevents any claim that the shipped package's retention behavior matches this source |
| Revision `2ecb382a` is roughly 20 months before the analysis cutoff | Prevents any claim about current upstream memory behavior. Every finding here is pinned to this revision |

None of these is recorded as `absent`. `uninspected` is not `absent`, and no negative finding above rests on one of them.
