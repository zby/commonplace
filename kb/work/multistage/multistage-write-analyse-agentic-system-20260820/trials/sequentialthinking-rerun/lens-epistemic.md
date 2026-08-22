# Epistemic lens output — run `AGS-2026-08-21-SEQTHINK`

| field | value |
|---|---|
| run ID | `AGS-2026-08-21-SEQTHINK` |
| lens | epistemic architecture |
| method executed | `kb/instructions/analyse-external-system-epistemic-architecture.md`, all six output blocks, in order |
| depth | **full pass** (per `SCOPE-EPI`) |
| subquestion | Within the declared boundary (`sequentialthinking` at `2ecb382a`; MCP SDK, host client, and model declared external), what truth-apt content does the artifact acquire, transform, check, dispose, retain, or integrate; what epistemic and operational authority does any route grant; and how do the artifact's knowledge-production and warrant claims — especially `CLM-1` — compare with the routes actually found? |
| early branch taken | **Branch 2** (knowledge-production claim present, no implemented or observed route found), extended over implemented non-claimed routes. Resolution reasoning below. |
| ownership | executes inside the orchestrator's ownership; no boundary established, no publication decision, no system-wide epistemic grade |

## Early-branch resolution (step 3)

Both step-3 branches were tested against their stated conditions.

**Branch 1 is not satisfied**, and the apparent overlap dissolves on its own wording. Branch 1's condition is conjunctive: the inventory shows only storage/retrieval/serving/direct use, *with no relevant transformation* **and** *no knowledge-production claim*. The first conjunct is nearly met — the artifact is dominated by storage and serving. The second conjunct fails outright: `CLM-1` is an explicit knowledge-production and warrant claim ("Generates a solution hypothesis", "Verifies the hypothesis based on the Chain of Thought steps", "Provides a correct answer"). One failed conjunct excludes the branch. Separately, the first conjunct is also not strictly met: two implemented edges do transform truth-apt content (`RTE-7`'s derived state propositions; `RTE-8`'s request-conformance propositions).

**Branch 2 is satisfied and is the governing branch.** A knowledge-production claim exists (`CLM-1`); no implemented or observed route performing the claimed functions was found within the recorded search boundary (`ABS-3`, plus this lens's `EPI-AMD-4`). Branch 2's prescribed shape is executed in full: the claimed object is inventoried (`EPI-6`), its claimed transformation is classified first, ampliation is established *by the claim evidence*, the lifecycle schema is used with declared phases marked `doctrine only` and every unobserved candidate phase marked `no instance observed`, ledger rows are added for the claimed functions (`RC1`–`RC8`), and the claims are compared against the absent implementation.

**How I extended Branch 2.** Branch 2 ends with "Then stop." I did not treat that as authority to omit implemented material routes that step 2's material-route rule had already admitted. Branch 2 instructs what to do *about the claim*; it does not retract the inventory. `SCOPE-EPI` warrants a full pass, and dropping `RTE-3`, `RTE-7`, `RTE-8`, and `RTE-9` would have discarded the artifact's only real truth-apt edges — including the two places it does produce warranted content. So: Branch 2's claim-side shape, plus the step 4–7 classification and ledger over the implemented routes.

Had I instead taken Branch 1, the output would have contained an "explicit no-claim comparison" — which would have been false, and would have omitted the `CLM-1` comparison that is the decision-relevant part of this analysis. Branch 1 would have been the wrong resolution even before its condition failed.

---

## Block 1 — Source-and-claim boundary

| field | value |
|---|---|
| system | `sequentialthinking` MCP server (`@modelcontextprotocol/server-sequential-thinking`), subtree `src/sequentialthinking` of github.com/modelcontextprotocol/servers |
| reviewed revision | `2ecb382a02d7921511180dfbadcef24eb66a052f` (committed 2024-12-06), clean tree at `/home/zby/llm/servers` |
| declared scope | as fixed by the orchestrator in evidence-packet record 2: boundary kind **complete artifact, partial loop**; inclusions per record 2 |
| excluded components | `EXT-1` MCP SDK 0.5.0 (uninspected); `EXT-2` host client (uninspected); `EXT-3` the model authoring every `thought` (uninspected); `EXT-4` sibling servers (out by declaration) |
| analysis question | the bounded epistemic subquestion above |
| assessed route families | acquisition/import at the request boundary; content reshaping for display; entailed derivation from retained state; retention; diagnostic production; tool-spec serving and dispatch; process lifecycle; the claimed hypothesis-generation/verification/iteration/answer family |
| unassessed route families | JSON-RPC framing, method routing, protocol error handling, cancellation, connection lifecycle — all inside `EXT-1`, uninspected. Conclusion prevented: any claim about how the request actually reaches `RTE-2`, or whether a malformed frame is rejected before `RTE-3` ever runs. Also unassessed: everything downstream of `OBJ-4` in `EXT-2`/`EXT-3`. |

### Source register (reusing the packet's canonical IDs; no parallel namespace minted)

| ID | identity / revision | evidence layer |
|---|---|---|
| `SRC-1` | `/home/zby/llm/servers/src/sequentialthinking/index.ts` @ `2ecb382a`, 279 lines | implementation |
| `SRC-2` | `.../sequentialthinking/README.md` @ `2ecb382a`, 63 lines | doctrine/design |
| `SRC-3` | `.../sequentialthinking/package.json` @ `2ecb382a` | implementation (packaging); `description` field is doctrine/design |
| `SRC-4` | `.../sequentialthinking/tsconfig.json` @ `2ecb382a` | implementation (build config) |
| `SRC-5` | repo-root `package.json`, `tsconfig.json`, `package-lock.json` @ `2ecb382a` | implementation (workspace + pinning) |
| `SRC-6` | repo-root `README.md:27` @ `2ecb382a` | doctrine/design |

No source was reacquired, refreshed, fetched, or widened. Targeted reads made are listed in the "Targeted reads" section.

### Missing evidence → conclusion prevented

| missing evidence | conclusion it prevents | wrapper conclusion status of the affected finding |
|---|---|---|
| No run traces, tests, fixtures, or logs anywhere in the subtree (`ABS-4`) | Every `observed` and `causally supported` status. **No observed candidate exists anywhere in this run**, so every observed-candidate-state cell in block 4 is `no instance observed`. This is an evidence limit, not a finding that candidates fail to occur. | bounded at `implemented` |
| `EXT-3` uninspected | Whether any `thought` payload is in fact a hypothesis, a conjecture, a restatement, or a question; therefore whether the acquired content is ampliative. Forces `EPI-1` into the *indeterminate* disposition rather than the ampliative one. | `uninspected` |
| `EXT-2` uninspected | Whether `OBJ-5` reaches a model at all; whether the JSON Schema's `minimum: 1` and optional-field types are enforced anywhere; what a caller does with `OBJ-4`. | `uninspected` |
| `EXT-1` uninspected | Whether `RTE-3` is the first check a request meets. | `uninspected` |
| No `node_modules`, no `dist/` | Whether the published artifact's behavior matches `SRC-1`. All findings are about the source at `2ecb382a`. | `uninspected` |

### System knowledge-production / warrant claims

Claims are cited by the packet's canonical IDs. `CLM-1` is the consequential knowledge-production and warrant claim; `CLM-2`, `CLM-3`, `CLM-6`, `CLM-7` are secondary epistemic-shaped claims; `CLM-4`, `CLM-5` are capability claims with epistemic bearing.

| claim ID | source anchor | evidence layer | knowledge-production / warrant content |
|---|---|---|---|
| `CLM-1` | `SRC-2:12`; `SRC-1:154–157` | doctrine/design | **yes** — generation, *verification*, iteration to satisfaction, and a *correct answer* |
| `CLM-2` | `SRC-2:9`; `SRC-1:150` | doctrine/design | revision of prior content |
| `CLM-3` | `SRC-2:10`; `SRC-1:153` | doctrine/design | alternative-path exploration |
| `CLM-4` | `SRC-2:11`; `SRC-1:149` | doctrine/design | dynamic adjustment of a control estimate |
| `CLM-5` | `SRC-2:38`; `SRC-1:146` | doctrine/design | context maintenance across steps |
| `CLM-6` | `SRC-2:39`; `SRC-1:146` | doctrine/design | relevance filtering |
| `CLM-7` | `SRC-2:4`; `SRC-6:27` | doctrine/design | "dynamic and reflective problem-solving through a structured thinking process" |

A further doctrine string not previously registered as a claim: `SRC-3:4`, `"description": "MCP server for sequential thinking and problem solving"`. It is weaker than `CLM-7` and adds nothing `CLM-7` does not already carry; recorded here for completeness, not proposed as a new claim record.

---

## Block 2 — Epistemic-object inventory

Canonical `OBJ-*` IDs are reused. Where the method's split rule (split parts differing in content, form, checks, producers/consumers, or authority paths) requires a part the packet does not register, a lens-local `EPI-n` proposal is used and its identity is stated so the orchestrator can rewrite it to a canonical ID.

| object ID | system name and description | representational form | source/input and lineage | producer → consumer | candidate truth-apt content | claimed role | evidence | gap/limit |
|---|---|---|---|---|---|---|---|---|
| `EPI-1` (proposed; split of `OBJ-1`) | the `thought` payload — one caller-authored natural-language string, the only content-bearing field of `ThoughtData` | natural-language string | authored by `EXT-3`; crosses boundary as `params.arguments.thought`; stored verbatim, never rewritten | `EXT-3` → `RTE-3` → `OBJ-2`/`OBJ-3`, `CMP-5` | **yes** — may assert propositions; the tool description itself says it may contain "Hypothesis generation" and "Hypothesis verification" (`SRC-1:166–167`) | the substance the whole tool exists to carry | `SRC-1:14`, `32–34`, `46`, `59`, `82`, `94` | Truth-aptness is caller-determined and per-instance. The artifact's own type for it is `string` — it individuates no proposition inside it. `EXT-3` uninspected, so no instance is observed. |
| `EPI-2` (proposed; split of `OBJ-1`) | the control-flag envelope — `thoughtNumber`, `totalThoughts`, `nextThoughtNeeded`, `isRevision`, `revisesThought`, `branchFromThought`, `branchId`, `needsMoreThoughts` | numeric/boolean/string control fields | authored by `EXT-3`; four validated, five cast without runtime validation | `EXT-3` → `RTE-3`/`RTE-4`/`RTE-6`/`RTE-7`/`CMP-5` | **no** (see `EPI-AMD-3` for the `totalThoughts` determination) | control of sequencing, revision labelling, branch bucketing | `SRC-1:15–22`, `35–43`, `47–54` | Split from `EPI-1` because form, checks, consumers, and truth-aptness all differ. Five fields are `as`-cast, which TypeScript erases at runtime (`SRC-1:50–54`). |
| `OBJ-2` | `thoughtHistory` — append-only array of every accepted `ThoughtData` | in-memory array | `RTE-5` | `CMP-1` → read only as `.length` (`SRC-1:114`) | contains `EPI-1` instances; the container itself yields one derived proposition | retained record of the thinking sequence | `SRC-1:26`, `94`, `114` | No content read path (`ABS-2`). Unbounded, no eviction. |
| `OBJ-3` | `branches` — map from caller-authored `branchId` to arrays of `ThoughtData` | in-memory record | `RTE-6` | `CMP-1` → read only as `Object.keys` (`SRC-1:113`) | retained record of alternative paths | `SRC-1:27`, `96–101`, `113` | Same object references as in `OBJ-2`; no content read path. Bucket creation requires both `branchFromThought` and `branchId` truthy. |
| `EPI-10` (proposed; split of `OBJ-4`) | echoed control fields in the tool result — `thoughtNumber`, `nextThoughtNeeded`, and `totalThoughts` post-`RTE-4` | JSON numbers/booleans in an MCP text block | caller-supplied; `totalThoughts` possibly raised by `RTE-4` | `RTE-7` → `EXT-2` → `EXT-3` | no | echo/acknowledgement | `SRC-1:110–112` | Split from `EPI-11` because lineage and warrant differ: caller-sourced vs artifact-derived. |
| `EPI-11` (proposed; split of `OBJ-4`) | derived state propositions in the tool result — `branches: Object.keys(this.branches)` and `thoughtHistoryLength: this.thoughtHistory.length` | JSON array / number | mechanically computed from `OBJ-2`, `OBJ-3` at response time | `RTE-7` → `EXT-2` → `EXT-3` | **yes** — each asserts a fact about the artifact's own retained state, truth-apt over the scope "this process's `thoughtHistory`/`branches` at this response" | tells the caller how much has accumulated | `SRC-1:113–114` | The *only* truth-apt content the artifact itself produces about anything other than the current request. Scope is self-referential bookkeeping, not the problem domain. |
| `OBJ-8` | error result object — `{error: <message>, status: 'failed'}` with `isError: true` | JSON in an MCP text block | produced by the `catch` at `SRC-1:118` | `CMP-1` → `EXT-2` → `EXT-3` | **yes** — the `error` string asserts a proposition about the request ("Invalid thought: must be a string") | diagnostic | `SRC-1:118–129`, messages at `33`, `36`, `39`, `42` | At least one message is **false** for a schema-conforming input; see `EPI-AMD-8`. |
| `OBJ-6` | rendered thought box on stderr | ANSI-coloured text | non-ampliative reshaping of `EPI-1` + two `EPI-2` fields | `CMP-5` → fd 2; **no in-boundary consumer** (`BAP-3`) | inherits `EPI-1`'s truth-aptness verbatim | human/log observability | `SRC-1:58–84`, emitted `104` | Payload preserved verbatim (`padEnd` never truncates); structure degrades for multi-line payloads — `EPI-AMD-2`. |
| `EPI-4` (proposed; split of `OBJ-5`) | **assertive block** of the tool description: "When to use this tool" (`SRC-1:139–146`) and "Key features" (`SRC-1:148–157`) | natural-language assertion, shipped static | authored by `CMP-2`'s authors | `CMP-2` → `RTE-1` → `EXT-2`'s tool list → `EXT-3` | **yes** — these are assertions about what the artifact does; they have truth values over the artifact's behavior | states the tool's capabilities | `SRC-1:139–157` | Carries `CLM-1`, `CLM-4`, `CLM-5`, `CLM-6` **into the model's context**. This is the channel that makes the `CLM-1` mismatch operationally consequential rather than merely documentary. |
| `EPI-5` (proposed; split of `OBJ-5`) | **directive block** of the tool description: parameter guidance (`SRC-1:159–175`) and "You should: 1–11" (`SRC-1:177–188`) | natural-language directive, shipped static | same authors | same channel | **no** — directives are not truth-apt | instructs the model how to use the tool | `SRC-1:159–188` | Items 7–10 instruct `EXT-3` to perform exactly the four operations `CLM-1` attributes to the tool. See `EPI-CORR-1`. |
| `OBJ-7` | tool `inputSchema` — JSON Schema, 9 properties, 4 required | symbolic | authored, shipped | `EXT-2` client-side; partially mirrored by `RTE-3` | no (a constraint artifact, not a content assertion) | declares the accepted argument shape | `SRC-1:189–234` | Contains **no field for a hypothesis**, though it does mark revisions and branches. This is why the `CLM-1` verification claim has no representable target — `EPI-AMD-4`. Its `minimum: 1` constraints are enforced only in `EXT-2` (uninspected). |
| `EPI-6` (proposed) | **the claimed "solution hypothesis"** — the object `CLM-1` says the tool generates and verifies. Identity: named at `SRC-1:154–155` and `SRC-2:12`; **no in-boundary representation** — no schema property, no interface field, no variable, no type | claimed only; no implemented form | claimed to be produced by the tool | claimed producer `CMP-1`; claimed consumer the verification step | **yes by claim** — a hypothesis is truth-apt, and pairing generation with verification presupposes non-entailment, so **ampliation is established by the claim evidence** | the centre of `CLM-1` | `SRC-1:154–157`; `SRC-2:12`; absence anchored at `SRC-1:13–23` (interface), `189–234` (schema), full `SRC-1` | Architectural status `doctrine only`; wrapper conclusion status `claimed`. No instance observed. |
| `CMP-*` components | `CMP-1`…`CMP-7` per the packet | — | — | — | — | — | packet record 4 | Components are not epistemic objects; they appear here only as producers/consumers. |

### Omitted route families and what the omission prevents

- Protocol transport internals (`EXT-1`) — prevents any claim about pre-`RTE-3` checking.
- Build and packaging (`SRC-3`, `SRC-4`, `SRC-5`) — no truth-apt content edge; omission prevents nothing this lens concludes.
- Host-side and model-side reasoning (`EXT-2`, `EXT-3`) — prevents every conclusion about `LOOP-C`, which is exactly the loop `CLM-1`–`CLM-7` describe. This is the single largest omission and it is a declared boundary property, not an oversight.

---

## Block 3 — Authority-route ledger

Row labels `R1`–`R10` (implemented) and `RC1`–`RC8` (claimed) are **row labels only**; each names the canonical `RTE-*`/`OBJ-*`/`CLM-*` it concerns. Two status vocabularies are kept in separate fields throughout: **architectural status** (method) and **wrapper conclusion status** (run).

### Implemented routes

**`R1` — concerns `RTE-1`, `EPI-4`/`EPI-5`/`OBJ-7`, `CLM-1`–`CLM-7`**
- route function: `operational admission/selection/consumption` (serving the tool spec)
- architectural status: `implemented` · wrapper conclusion status: `implemented`
- object/candidate: `EPI-4`, `EPI-5`, `OBJ-7` (returned verbatim as `CMP-2`)
- content/update relation: `no content change` — the handler returns the module constant unfiltered and unparameterized
- check target: none · evaluator/condition and domain: **none — evidenced absence**; no filtering, no capability negotiation, no per-caller selection
- activation and timing: on every `ListTools` request; timing owned entirely by `EXT-2`
- possible/observed result: the single tool spec · observed: `no instance observed` (`ABS-4`)
- implemented force: none at this route; force arrives downstream through `BAP-1`/`EPI-7`
- epistemic authority: **none granted.** Serving a description asserts nothing and licenses no reliance. Guard applied: *a tool schema present in context is not tool execution*, and serving an assertion is not evidence for it.
- operational authority: makes the tool callable at all — permits `R2`
- behavioral-authority path: `BAP-1` (directive half, `EPI-5`) and `EPI-7` (assertive half, `EPI-4`); see `EPI-AMD-5`
- evidence: `SRC-1:251–253` · claim IDs: all seven, since this is the route by which every in-prompt claim reaches a consumer
- mismatch marker: none at this route · gap/limit: whether `EXT-2` forwards the description to a model is uninspected

**`R2` — concerns `RTE-2`**
- route function: `operational admission/selection/consumption` (dispatch)
- architectural status: `implemented` · wrapper: `implemented`
- object/candidate: the incoming `CallTool` request
- content/update relation: `no content change`
- check target: `request.params.name` — a string identity, **not truth-apt** · evaluator: string equality against the literal `"sequentialthinking"` (`SRC-1:256`); domain: exact match only
- activation and timing: every `CallTool` request
- possible result: dispatch to `CMP-1`, or `{text: "Unknown tool: …", isError: true}` · observed: `no instance observed`
- implemented force: enforcing on admission
- epistemic authority: none
- operational authority: permits or blocks entry to `R3`; an unmatched name yields a tool-level error, not a protocol error, so `EXT-2` sees a normal result envelope
- behavioral-authority path: `{consumer: EXT-2; channel: the result envelope's isError flag; force: informational; horizon: this call}`
- evidence: `SRC-1:255–267` · claims: none
- mismatch marker: **yes, inherited** — `SRC-2:16` documents the tool as `sequential_thinking`; the dispatch predicate matches `sequentialthinking` (`CMP-2/a1`). A host wired from the README name is rejected here.
- gap/limit: uninspected whether `EXT-1` routes the request here at all

**`R3` — concerns `RTE-3`, `EPI-1`, `EPI-2`, `ABS-3`**
- route function: `check/evidence production` (this is the artifact's **only** check-shaped route)
- architectural status: `implemented` · wrapper: `implemented`
- object/candidate: `EPI-1` and `EPI-2` as fields of an untyped request object
- content/update relation: `truth-apt transformation: acquisition/import` for `EPI-1` — external content enters the system. **Source warrant: unknown.** `EXT-3` is uninspected; the artifact neither inherits, attests, nor degrades the payload's warrant, and applies nothing that could establish it. Content is preserved byte-identically (`SRC-1:46`).
- transition/check target: **the request object's shape**, not any proposition. Four predicates: `!data.thought || typeof !== 'string'`; `!data.thoughtNumber || typeof !== 'number'`; `!data.totalThoughts || typeof !== 'number'`; `typeof data.nextThoughtNeeded !== 'boolean'` (`SRC-1:32–43`).
- evaluator/condition and domain: an inline procedural predicate; **domain is JSON type and presence only.** It has no access to meaning, no comparison corpus, no reference state, and no model call. The one content-sensitive effect is accidental non-emptiness via falsy coercion — see `EPI-AMD-1`.
- activation and timing: first operation inside `processThought`, before any write
- possible result: return a shaped `ThoughtData`, or `throw` → `R8` · observed: `no instance observed`
- implemented force: enforcing, but only over 4 of the 9 declared properties; the other five are `as`-cast and reach retention unvalidated (`SRC-1:50–54`)
- **epistemic authority: none over content.** Passing `R3` warrants exactly one proposition: *this argument object has a non-empty string at `thought` and numbers/boolean at three control fields.* It licenses **no** reliance on what the thought says. Guard applied: do not transfer an outcome pass to the producing process or to content warrant.
- operational authority: passing permits `R4`, `R5`, `R6`, `R9`, `R7`; failing blocks all of them and routes to `R8`
- behavioral-authority path: `BAP-4`, with `EPI-AMD-7` narrowing its stated force
- evidence: `SRC-1:29–56` · claims: bounds `CLM-1` (this is the only route that could have been a verifier, and its target is not truth-apt)
- mismatch marker: **yes** — `CLM-1` claims verification; the only check in the artifact checks argument shape
- gap/limit: no referential-integrity check on `revisesThought`/`branchFromThought` (`EPI-3`); schema minima unenforced server-side

**`R4` — concerns `RTE-4`, `EPI-2`**
- route function: `behavior/policy adaptation` (per the scoping record's direct-adaptation hand-off)
- architectural status: `implemented` · wrapper: `implemented`
- object/candidate: `EPI-2.totalThoughts`
- content/update relation: **`non-truth-apt policy/content update: raise a control field to restore the invariant `totalThoughts >= thoughtNumber`.**` I concur with `SCOPE-EPI`'s classification and return the determination as `EPI-AMD-3` rather than a correction. Reasoning: the field is documented as an *estimate* of thoughts "needed" (`SRC-1:170`), and an estimate can carry a truth value — but only relative to a criterion of "needed" that lives entirely in `EXT-3`'s future self-assessment (`SRC-1:188`). The artifact holds no such criterion. And the update is not a re-estimation: it applies no evaluator to the estimate's subject matter and consults nothing but the two numbers in the current request. It is arithmetic invariant repair whose only downstream effects are the stderr header `N/M` (`SRC-1:75`) and the echo in `EPI-10`. So the *update* is non-truth-apt within the boundary, which is what the classification field records.
- check target: the numeric relation `thoughtNumber > totalThoughts` · evaluator: inline comparison; domain: two integers from one request
- activation and timing: post-validation, pre-retention, every successful call
- possible result: mutate `validatedInput.totalThoughts` upward, or no-op · observed: `no instance observed`
- implemented force: enforcing on the record about to be retained; one-way, upward only (`ABS-8`)
- epistemic authority: none
- operational authority: changes what `R5`/`R6` retain and what `R7`/`R9` emit; changes nothing outside the process
- behavioral-authority path: `BAP-2` (the mutated value returns to the caller inside `EPI-10`) — force informational
- evidence: `SRC-1:90–92` · claims: bounds `CLM-4`
- mismatch marker: **yes** — `CLM-4` says "up or down"; the artifact only raises. Downward movement is a caller capability, not an artifact behavior (`ABS-8`).
- gap/limit: mutation is applied to the same object reference later shared by `OBJ-2` and `OBJ-3`

**`R5` — concerns `RTE-5`, `EPI-1`, `EPI-2`, `OBJ-2`**
- route function: `retention` (explicitly **not** lifecycle integration — no acceptance precedes it)
- architectural status: `implemented` · wrapper: `implemented`
- object/candidate: the validated `ThoughtData` carrying `EPI-1`
- content/update relation: `no content change` — a reference is appended; the payload is not transformed
- check target: none · evaluator/condition: **none — unconditional.** Every request that survives `R3` is retained. There is no acceptance criterion, no scoring, no dedup, no ordering, no size bound, no eviction.
- activation and timing: every successful call, before render and before return
- possible result: array grows by one · observed: `no instance observed`
- implemented force: none — retention is inert
- **epistemic authority: none, and unusually so.** Retention normally licenses at least "this can be retrieved later". Here it does not even license that: no route ever reads a retained payload (`ABS-2`). Retained content is epistemically inaccessible from the moment it is stored. Guard applied: do not infer acceptance or knowledge production from retention.
- operational authority: increments the count that `R7` reports; nothing else
- behavioral-authority path: reaches a consumer only as the integer in `EPI-11`, i.e. `BAP-2`
- evidence: `SRC-1:94` · claims: bears on `CLM-5` (context maintenance)
- mismatch marker: **yes** — `CLM-5` ("maintain context over multiple steps") is satisfied by `EXT-2`'s transcript, not by this route, since nothing retained here returns
- gap/limit: unbounded growth; no instance observed

**`R6` — concerns `RTE-6`, `OBJ-3`**
- route function: `retention` (linked to `R5`; separate row because the target container, the activation condition, and the read path all differ)
- architectural status: `implemented` · wrapper: `implemented`
- content/update relation: `no content change`
- check target: bucket eligibility · evaluator: `validatedInput.branchFromThought && validatedInput.branchId` — a truthiness conjunction, domain = presence of two request fields, neither runtime-type-validated
- activation and timing: every successful call where both fields are truthy
- possible result: create bucket and append, or skip · observed: `no instance observed`
- implemented force: enforcing on bucket membership
- epistemic authority: none over content; the accumulated key set becomes the one proposition in `EPI-11.branches`
- operational authority: determines what `Object.keys` will report
- behavioral-authority path: `BAP-2`
- evidence: `SRC-1:96–101` · claims: bears on `CLM-3`
- mismatch marker: **yes** — `CLM-3` says "branch into alternative paths of reasoning". The route records a caller-supplied label and stores a duplicate reference; it does not fork, compare, prune, merge, or resolve anything. Branching is done by `EXT-3`; the artifact bookkeeps labels.
- gap/limit: `branchFromThought: 0` is falsy and silently skips bucketing while bypassing the schema's `minimum: 1` if `EXT-2` does not enforce it; no referential integrity (`EPI-3`)

**`R7a` — concerns `RTE-7`, `EPI-10`**
- route function: `content transformation` (echo/return)
- architectural status: `implemented` · wrapper: `implemented`
- content/update relation: `non-ampliative reshaping` — three caller-supplied control values re-emitted as JSON, one of them post-`R4`
- check target: none · evaluator: none
- activation/timing: end of every successful call
- possible result: the three fields · observed: `no instance observed`
- implemented force: informational
- epistemic authority: none beyond restating what the caller sent; `totalThoughts` may differ from what was sent, and nothing flags that it was changed
- operational authority: none — `nextThoughtNeeded` is passed through unaltered, so the artifact expresses no opinion about continuation (`ABS-10`)
- behavioral-authority path: `BAP-2` · evidence: `SRC-1:110–112` · claims: `CLM-4`
- mismatch marker: none · gap/limit: silent mutation of `totalThoughts` is not signalled

**`R7b` — concerns `RTE-7`, `EPI-11`, `OBJ-2`, `OBJ-3`**
- route function: `content transformation` (derivation)
- architectural status: `implemented` · wrapper: `implemented`
- content/update relation: **`truth-apt transformation: entailed derivation`.** `Object.keys(this.branches)` and `this.thoughtHistory.length` follow mechanically from the retained state. Premises (the arrays' own contents) are warranted within the domain "this process's memory"; the derivation is a total function of them; warrant transfers cleanly inside that domain and **not one step outside it**.
- check target: none · evaluator: none — derivation, not checking
- activation/timing: end of every successful call
- possible result: a label array and an integer · observed: `no instance observed`
- implemented force: informational
- **epistemic authority: real but tiny and self-referential.** It licenses reliance on exactly two propositions: *this process has retained N thoughts* and *these branch labels have been used*. It licenses nothing about the problem domain, nothing about the thoughts' content, and nothing about the count's meaning as progress. `thoughtHistoryLength` counts accepted requests, not distinct thoughts — a repeated call with identical arguments increments it.
- operational authority: none; no route consumes these values inside the boundary
- behavioral-authority path: `BAP-2` · evidence: `SRC-1:113–114` · claims: bears loosely on `CLM-5`
- mismatch marker: none · gap/limit: the count's semantics are undocumented; a caller could over-read it as "distinct reasoning steps"

**`R8` — concerns `RTE-8`, `OBJ-8`**
- route function: `check/evidence production` (diagnostic emission consequent on `R3`) — linked to `R3`
- architectural status: `implemented` · wrapper: `implemented`
- content/update relation: **`truth-apt transformation: entailed derivation`** — the message asserts which predicate failed, derived from the throw site
- check target: the failed request · evaluator: whichever `R3` predicate threw; domain = argument shape
- activation/timing: any throw inside the `try` (`SRC-1:87–129`), not only validation throws
- possible result: `{error: <message>, status: 'failed'}`, `isError: true` · observed: `no instance observed`
- implemented force: informational to `EXT-2`/`EXT-3`
- epistemic authority: licenses reliance on "this request was rejected", scoped to this call. **It does not license "nothing was retained"** — see `EPI-AMD-9`. And at least one message is false for a schema-conforming input — `EPI-AMD-8`, which bounds the reliance a caller may place on the message's *content* as opposed to the fact of failure.
- operational authority: blocks retention, render, and status return for this call
- behavioral-authority path: `{consumer: EXT-2 → EXT-3; channel: OBJ-8 with isError; force: informational; horizon: this call}`
- evidence: `SRC-1:118–129` · claims: none · mismatch marker: none
- gap/limit: no retry, no compensation, no distinction between validation failure and any other in-`try` throw

**`R9` — concerns `RTE-9`, `OBJ-6`, `BAP-3`**
- route function: `content transformation` (reshaping for display)
- architectural status: `implemented` · wrapper: `implemented`
- content/update relation: **`truth-apt transformation: non-ampliative reshaping`** — `EPI-1` is embedded verbatim in a box with a header and a revision/branch caption; no truncation occurs (`padEnd` only pads)
- check target: none · evaluator: none · activation: every successful call, after retention (`SRC-1:103–104`)
- possible result: an ANSI block on fd 2 · observed: `no instance observed`
- **implemented force: none.** `BAP-3` records no consequential consumer inside the boundary.
- epistemic authority: none — no in-boundary consumer can rely on it
- operational authority: none
- behavioral-authority path: `BAP-3` · evidence: `SRC-1:58–84`, `104` · claims: bears on `CLM-2` and `CLM-3`
- mismatch marker: **yes, and this is the sharpest one for `CLM-2`.** `isRevision` and `revisesThought` change *only a coloured label and a caption* (`SRC-1:64–66`). No retained entry is superseded, marked, replaced, or removed (`ABS-6`). The artifact's entire implementation of "revise and refine thoughts" is a yellow 🔄 emoji on a stream nothing in the boundary reads.
- gap/limit: `EPI-AMD-2` — multi-line payloads garble the box; the caption is computed from unvalidated fields, so `isRevision: "banana"` renders as a revision

**`R10` — concerns `RTE-10`, `BAP-5`**
- route function: `lineage/freshness/recovery`
- architectural status: `implemented` · wrapper: `implemented`
- content/update relation: `no content change`
- check target: transport connection health · evaluator: the rejected promise from `server.connect` · domain: process startup and transport faults
- activation/timing: startup, and any unhandled rejection from `runServer`
- possible result: banner on stderr, or `process.exit(1)` · observed: `no instance observed`
- implemented force: terminating
- epistemic authority: none
- operational authority: removes the artifact rather than degrading it; destroys all retained state (`ABS-1`)
- behavioral-authority path: `BAP-5` · evidence: `SRC-1:269–278` · claims: none
- mismatch marker: none · gap/limit: no reconnect, no signal handling, no graceful shutdown; whether the exit is observed depends on `EXT-2`'s supervisor (uninspected)

### Claimed routes (Branch 2 rows)

Each row's architectural status is `doctrine only`; each row's wrapper conclusion status is `claimed`. Recorded search boundary for every "no implemented route" finding: **`SRC-1` in full (279 lines), `SRC-2` in full, `SRC-3` in full, plus the four-file subtree listing.** None of these is `absent` in the sense of "the operation does not occur" — they are absent *from the artifact*; `EXT-3` is uninspected and may well perform them.

| row | claim | claimed function | architectural status | wrapper status | implemented route found | evaluator claimed vs found | epistemic authority the claim would grant | mismatch marker |
|---|---|---|---|---|---|---|---|---|
| `RC1` | `CLM-1` | produce a solution hypothesis (`EPI-6`) — `ampliative conjecture` by claim | `doctrine only` | `claimed` | **none.** No route produces any content; every output field is either echoed or counted. | claimed: the tool. found: `EXT-3`, named by the artifact's own `SRC-1:184` "Generate a solution hypothesis when appropriate" | would license treating tool output as a candidate hypothesis | **relabelled instruction** — the same operation appears as a tool feature at `SRC-1:154` and as a model instruction at `SRC-1:184` |
| `RC2` | `CLM-1` | **verify** the hypothesis against the Chain of Thought steps | `doctrine only` | `claimed` | **none** (`ABS-3`). Sharpened: there is not even a representable check target — `OBJ-7` marks revisions and branches but has no hypothesis field (`EPI-AMD-4`). | claimed: the tool. found: `EXT-3`, `SRC-1:185` | would license reliance on tool-attested verification — the strongest epistemic license in the whole doctrine | **most consequential mismatch in the run.** A verification claim with no evaluator, no target, and no comparison corpus, delivered into the consumer's context via `EPI-7` |
| `RC3` | `CLM-1` | repeat the process until satisfied | `doctrine only` | `claimed` | **none** (`ABS-10`). No scheduler, timer, loop, callback, or continuation; `nextThoughtNeeded` is echoed unchanged. | claimed: the tool. found: `EXT-3`, `SRC-1:186` | would license reliance on the tool to terminate the loop | mismatch: iteration is the caller re-invoking `R3`–`R7`; the artifact neither drives nor terminates it |
| `RC4` | `CLM-1` | **provide a correct answer** | `doctrine only` | `claimed` | **none — and contradicted under the artifact reading.** `R7` returns a fixed five-field status object with no answer slot; `R8` returns error+status. No route returns anything derived from thought content (`ABS-2`). | claimed: the tool. found: `EXT-3`, `SRC-1:187` | would license reliance on tool output as an answer, and on its correctness | **double mismatch: contradicted by the implemented return shape, and hedge-stripped.** `SRC-1:187` instructs the model to "Provide a single, **ideally** correct answer"; `SRC-1:157` states as a tool feature "Provides a **correct** answer". The hedge is present in the instruction and absent from the claim. |
| `RC5` | `CLM-2` | revise and refine thoughts | `doctrine only` | `claimed` | **none as a state operation** (`ABS-6`). The nearest implemented behavior is `R9`'s stderr label. | claimed: the tool. found: `EXT-3`, `SRC-1:182` | would license reliance on retained history being corrected | mismatch: label-only; nothing supersedes, marks, replaces, or removes a retained entry |
| `RC6` | `CLM-3` | branch into alternative reasoning paths | `doctrine only` | `claimed` | **partial and bookkeeping-only** — `R6` records caller labels; no fork, compare, prune, merge, or resolve exists | claimed: the tool. found: `EXT-3`, `SRC-1:182` | would license reliance on the tool managing alternatives | mismatch: the tool accumulates labels; the caller does the branching |
| `RC7` | `CLM-6` | filter out irrelevant information | `doctrine only` | `claimed` | **none** (`ABS-9`). No filtering, summarization, compression, or relevance selection anywhere. | claimed: the tool (listed under "When to use this tool"). found: `EXT-3`, `SRC-1:183` "Ignore information that is irrelevant to the current step" | would license reliance on the tool reducing context noise | mismatch: a suitability claim readable as a tool capability; the implementation contributes nothing |
| `RC8` | `CLM-5` | maintain context over multiple steps | `doctrine only` | `claimed` | **none that returns.** `R5`/`R6` retain; `ABS-2` means no retained content ever returns. The context is maintained by `EXT-2`'s transcript. | claimed: the tool. found: `EXT-2` | would license reliance on the tool as a context store | mismatch: retention without read-back is not context maintenance for the consumer |

### `no relevant route found` declarations

- **Checking of truth-apt content: `no route found within boundary`** (architectural) / `absent` (wrapper). Search boundary: `SRC-1` in full; every conditional in the file enumerated (`SRC-1:32`, `35`, `38`, `41`, `64`, `67`, `90`, `96`, `97`, `256`). None takes thought content as its subject.
- **Acceptance / disposition of any candidate: `no route found within boundary`** / `absent`. No evidence-consuming decision against a named criterion exists anywhere. Retention (`R5`) is unconditional and therefore cannot be acceptance.
- **Lifecycle integration: `no route found within boundary`** / `absent`. Nothing is connected to evidence, reorganized, or promoted post-acceptance, because there is no acceptance.
- **Epistemic authority over the problem domain: `no route found within boundary`** / `absent`. The artifact grants epistemic authority over exactly two classes of proposition, both self-referential (`R7b`, `R8`).

---

## Block 4 — Per-object lifecycle disposition

**Global note.** `ABS-4` records no run traces, tests, fixtures, or logs anywhere in the register. Therefore **no observed candidate exists in this run**, and every observed-candidate-state cell below is `no instance observed`. This is an evidence limitation, not a finding that candidates fail to traverse phases. Implementation and doctrine alone never establish an observed candidate state, and none is claimed below.

The global no-candidate statement is **not** applicable: the inventory does contain candidate truth-apt output (`EPI-11`, `OBJ-8`, and the acquired `EPI-1`).

### `EPI-6` — the claimed "solution hypothesis" (ampliative; Branch 2 schema)

- **candidate object ID:** `EPI-6` (proposed; identity: the object named at `SRC-1:154–155` and `SRC-2:12`; no in-boundary representation)
- **relevant route IDs:** `RC1`, `RC2`, `RC3`, `RC4`
- **transformation: ampliative conjecture** — established *by the claim evidence*, not by implementation. A hypothesis does not follow from its inputs, and `CLM-1` pairs generation with verification, which presupposes non-entailment.
- **observation/anomaly:** routes — none declared and none found. architectural status `no route found within boundary`. observed candidate state `no instance observed`. evidence: `SRC-1` full file; `SRC-2` full file — neither declares an observation or anomaly-detection step.
- **conjecture:** routes `RC1`. architectural status **`doctrine only`** (`SRC-1:154`; `SRC-2:12`). observed candidate state `no instance observed`. evidence layer: doctrine/design via `SRC-2`, `SRC-1`. No implemented route produces content of any kind.
- **derived consequence:** routes — none. architectural status `no route found within boundary`. observed candidate state `no instance observed`. Neither doctrine nor implementation describes deriving testable consequences from the hypothesis; `SRC-1:185` jumps straight from generation to verification "based on the Chain of Thought steps".
- **test/evidence:** routes `RC2`. architectural status **`doctrine only`**. observed candidate state `no instance observed`. evidence: `SRC-1:155`, `SRC-1:185`; `SRC-2:12`. Implementation status is `absent` with search boundary `SRC-1` full file (`ABS-3`, sharpened by `EPI-AMD-4`: no representable target exists, so the phase could not be implemented against the current schema without adding one).
- **acceptance:** routes `RC3` (the "until satisfied" condition is the nearest thing doctrine offers to an acceptance criterion). evaluator: **`EXT-3`, outside the boundary** — `SRC-1:188` names the criterion holder explicitly: "Only set next_thought_needed to false when truly done and a satisfactory answer is reached". criterion: *the model's own satisfaction*, stated in exactly those words and not operationalized further. intended use: terminate the loop and emit an answer. architectural status **`doctrine only`**. observed candidate state `no instance observed`. accepted scope: **undeterminable** — a self-assessed satisfaction criterion held by an uninspected evaluator has no statable scope from inside this boundary. evidence: `SRC-1:186–188`.
- **lifecycle integration:** routes — none. architectural status `no route found within boundary`. observed candidate state `no instance observed`. Nothing post-acceptance changes any organization or use inside the artifact; `nextThoughtNeeded: false` is echoed and nothing else happens (`R7a`, `ABS-10`). Per the method's rule, retention and pre-acceptance use are kept in `R5`/`R6` and are **not** counted as integration.
- **missing phase/evidence:** observation, consequence derivation, and integration are absent from doctrine as well as implementation. The acceptance evaluator is external and uninspected. No candidate instance is available anywhere. Conclusions prevented: whether any hypothesis is ever generated; whether it is ever checked against anything; whether "satisfied" tracks correctness.

### `EPI-1` — the acquired `thought` payload (indeterminate schema)

- **candidate object ID:** `EPI-1` · **relevant route IDs:** `R3` (acquisition), `R5`/`R6` (retention), `R9` (reshaping)
- **transformation: indeterminate.** Within the boundary the edge is `acquisition/import`. Whether the *content* is ampliative cannot be decided here: the artifact never inspects it, and `EXT-3`, where any ampliation would have occurred, is uninspected. Nothing in the register distinguishes a conjecture from a restatement, a question, or a plan step — and the tool description says the payload may be any of these (`SRC-1:160–167`).
- **classifications still possible:** `ampliative conjecture` (if the payload asserts a hypothesis, as `SRC-1:166` anticipates); `non-ampliative reshaping` or `entailed derivation` (if it restates or follows from the transcript); `no truth-apt content` (if it is a question or a bare plan step, both explicitly anticipated at `SRC-1:163–165`). All four remain open per instance.
- **preserved lineage:** strong within the artifact. The string is stored byte-identically (`SRC-1:46`), retained by reference (`SRC-1:94`), and rendered verbatim (`SRC-1:82`). No rewriting, truncation, summarization, or merging occurs anywhere. Lineage *outside* the artifact is not preserved in any structured form: the artifact records no author, no timestamp, no session ID, no provenance field.
- **implemented checks, retention, or use:** check — `R3`, shape and non-emptiness only, no content evaluation. retention — `R5` unconditional, `R6` conditional; both inert, since no read path exists (`ABS-2`). use — `R9` render to a stream with no in-boundary consumer.
- **current warrant limit:** **whatever warrant the payload carries is entirely `EXT-3`'s and is neither checked, attested, nor recorded by the artifact.** Passing `R3` adds nothing. Being retained adds nothing. Being counted in `EPI-11` adds nothing about content. The artifact is warrant-transparent: it neither preserves nor degrades source warrant, because it never engages with it.
- **evidence needed to decide preservation, entailment, or ampliation:** observed `thought` instances paired with the transcript that produced them — i.e. inspection of `EXT-2`'s conversation state and `EXT-3`'s inputs. Both are outside the declared boundary; acquiring them would widen it and is not authorized in this run.

### `EPI-11` — derived state propositions in the tool result (non-ampliative schema)

- **candidate object ID:** `EPI-11` · **relevant route IDs:** `R7b`, upstream `R5`, `R6`
- **transformation:** `entailed derivation`
- **discovery lifecycle:** not applicable
- **applicable derivation route and warrant:** `R7b` computes `Object.keys(this.branches)` and `this.thoughtHistory.length` as total functions of the retained containers. Premises are the containers' own state, which is warranted within the domain "this process's memory at this response". The derivation is mechanical and the interpretation is checked by the language's semantics. **Warrant transfers cleanly inside that domain and stops at its edge.** Specifically: the count warrants *N calls were retained*, not *N distinct reasoning steps occurred*, not *the reasoning progressed*, and nothing about any payload's truth.
- **missing evidence/limit:** no observed instance (`ABS-4`). The count's semantics are undocumented in `SRC-2`, leaving a caller free to over-read it. `Object.keys` order is insertion order for string keys, which is stable but not documented as a guarantee to the caller.

### `OBJ-8` — the error diagnostic (non-ampliative schema)

- **candidate object ID:** `OBJ-8` · **relevant route IDs:** `R8`, upstream `R3`
- **transformation:** `entailed derivation` (from the throw site to the message)
- **discovery lifecycle:** not applicable
- **applicable derivation route and warrant:** the message is selected by whichever predicate threw. Warrant is limited to "this request failed a shape predicate", scoped to this call. **The message's specific content is not fully warranted**: see `EPI-AMD-8` — `"Invalid thought: must be a string"` fires for `thought: ""`, which *is* a string and *is* conforming to `OBJ-7` (no `minLength` is declared). The artifact's one diagnostic proposition class contains at least one member that is false for a schema-conforming input.
- **missing evidence/limit:** no observed instance. Whether `EXT-2` surfaces the message to `EXT-3` is uninspected. The `catch` is not restricted to validation throws, so a non-validation error produces a message with no relation to argument shape.

### `OBJ-6` — the stderr render (non-ampliative schema)

- **candidate object ID:** `OBJ-6` · **relevant route IDs:** `R9`
- **transformation:** `non-ampliative reshaping` of `EPI-1`
- **discovery lifecycle:** not applicable
- **applicable route and warrant:** `R9` embeds the payload verbatim; the reshaping preserves content, so it preserves whatever warrant `EPI-1` had — which, per `EPI-1`'s record, is unknown and unattested. The added header and caption are derived from `EPI-2` fields, two of which (`isRevision`, `revisesThought`) are unvalidated, so the caption itself is not warranted.
- **missing evidence/limit:** no in-boundary consumer, so the object grants nothing to anyone inside the boundary (`BAP-3`); `EPI-AMD-2` records the structural fidelity limit.

### `EPI-4` — the assertive block of the tool description (non-ampliative schema)

- **candidate object ID:** `EPI-4` · **relevant route IDs:** `R1`, and behaviorally `EPI-7`
- **transformation:** `no content change` within the boundary — static shipped material, authored outside runtime and never transformed by any route
- **discovery lifecycle:** not applicable (no in-boundary production route)
- **applicable route and warrant:** the only in-boundary route is `R1`, which serves it verbatim. **Its warrant is authorial assertion and nothing else.** No route inside the artifact checks it, and this analysis finds four of its assertions unsupported (`RC1`–`RC4`) and one contradicted by an implemented route (`RC4`).
- **missing evidence/limit:** whether `EXT-2` delivers it to a model is uninspected, which prevents any conclusion about whether the unsupported assertions actually induce reliance. That they *would* if delivered is a property of the channel (`EPI-7`), not an observed effect.

### Per-object no-candidate lines

- No lifecycle record for `EPI-2`: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: `R4`, `R6`, `R7a`.
- No lifecycle record for `EPI-5`: no candidate truth-apt output for this object — directives have no truth value; relevant direct-adaptation or update routes: none. Its consequence is behavioral, via `BAP-1`.
- No lifecycle record for `EPI-10`: no candidate truth-apt output originating in this object; it re-emits caller-supplied control values. Relevant update route: `R4` (which may alter `totalThoughts` before echo).
- No lifecycle record for `OBJ-7`: no candidate truth-apt output for this object — it is a symbolic constraint artifact, not a content assertion; relevant routes: `R1` (serving), `R3` (partial server-side mirror).
- `OBJ-2` and `OBJ-3` are containers. They hold `EPI-1` instances, whose disposition is recorded above; the containers themselves yield only `EPI-11`, recorded above. Relevant retention routes: `R5`, `R6`.
- No lifecycle record for `CMP-1`–`CMP-7`: components are not epistemic objects in this method; they appear only as producers and consumers.

---

## Block 5 — System-claim versus route comparison

| claim ID | claimed operation or warrant | source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| `CLM-1` (a) | "Generates a solution hypothesis" | `SRC-2:12`; `SRC-1:154` — doctrine/design | full: stated as a feature in two places | **none** | none — `ABS-4` | none; no experiment exists in the register | The artifact produces no content of any kind. It receives, stores, counts, and echoes. Hypothesis generation, if it occurs, occurs in `EXT-3`, which the artifact's own instruction text tells to do it (`SRC-1:184`). | **mismatch: relabelled instruction.** The same operation appears as a tool feature and as a model instruction in the same file. |
| `CLM-1` (b) | "**Verifies** the hypothesis based on the Chain of Thought steps" | `SRC-2:12`; `SRC-1:155` — doctrine/design | full | **none** (`ABS-3`; `EPI-AMD-4`) | none | none | **The artifact contains no evaluator of any truth-apt content, and no representable target for one.** Its only check (`R3`) takes argument shape as its target. `OBJ-7` marks revisions and branches but has no hypothesis field, so the object the claim says is verified cannot even be named in the protocol. | **mismatch — the run's headline.** A verification-and-warrant claim with zero implementation, delivered into the consumer's context via `EPI-7`. |
| `CLM-1` (c) | "Repeats the process until satisfied" | `SRC-2:12`; `SRC-1:156` — doctrine/design | full | **none** (`ABS-10`) | none | none | The artifact holds no scheduling responsibility. `nextThoughtNeeded` is received and echoed unchanged; there is no timer, loop, callback, or continuation. Iteration is the caller re-invoking the tool. | mismatch: the loop the tool is named after is owned entirely by `EXT-3`. |
| `CLM-1` (d) | "**Provides a correct answer**" | `SRC-2:12`; `SRC-1:157` — doctrine/design | full, **unhedged** | **none; contradicted under the artifact reading** by `R7a`/`R7b` | none | none | Two readings, and the evidence discriminates. **Artifact reading** (the "tool" is the server): contradicted — every success response is the same five-field status object with no answer slot, and no route returns anything derived from thought content (`ABS-2`). **Assembly reading** (the "tool" is server+host+model): out of boundary; `EXT-3` uninspected, so undecidable here. The artifact's own `SRC-1:187` supports the assembly reading by instructing the model to provide the answer — which is also what makes the feature-list phrasing an attribution error. | **double mismatch: contradicted by the implemented return shape, and hedge-stripped.** `SRC-1:187` says "ideally correct"; `SRC-1:157` says "correct". |
| `CLM-2` | "Revise and refine thoughts as understanding deepens" | `SRC-2:9`; `SRC-1:150` — doctrine/design | full | `R9` only (label and caption) | none | none | The artifact implements revision as a coloured stderr label. No retained entry is superseded, marked, replaced, or removed (`ABS-6`), and `isRevision` is not runtime-validated, so the label is not even reliable. | mismatch: label-only, on a stream with no in-boundary consumer. |
| `CLM-3` | "Branch into alternative paths of reasoning" | `SRC-2:10`; `SRC-1:153` — doctrine/design | full | `R6` (bookkeeping only) | none | none | The artifact accumulates caller-authored branch labels and duplicates references into buckets. It never forks, compares, prunes, merges, resolves, or returns a branch. The label set is the one branch-related fact it can report. | mismatch: the caller branches; the artifact bookkeeps. |
| `CLM-4` | "Adjust the total number of thoughts dynamically" / "adjust total_thoughts up or down" | `SRC-2:11`; `SRC-1:149` — doctrine/design | full | `R4` (upward only) | none | none | The artifact raises `totalThoughts` to `thoughtNumber` on overshoot and never lowers it (`ABS-8`). Downward movement is a caller capability. The update is non-truth-apt invariant repair (`EPI-AMD-3`). | mismatch: "or down" is not an artifact behavior. Secondary: the claim text names `total_thoughts`, a parameter the schema does not accept (`EPI-AMD-6`). |
| `CLM-5` | "Tasks that need to maintain context over multiple steps" | `SRC-2:38`; `SRC-1:146` — doctrine/design | full, phrased as suitability | `R5`, `R6` retain; **no read-back** | none | none | Context is maintained by `EXT-2`'s transcript, because the model wrote the thoughts into its own turns. The artifact retains material it never returns (`ABS-2`), so its retention contributes nothing to the consumer's context. | mismatch at the scope a reader would take it: retention without read-back is not context maintenance. |
| `CLM-6` | "Situations where irrelevant information needs to be filtered out" | `SRC-2:39`; `SRC-1:146` — doctrine/design | full, phrased as suitability | **none** (`ABS-9`) | none | none | No filtering, summarization, compression, or relevance selection exists. The corresponding capability is delegated in `SRC-1:183` ("Ignore information that is irrelevant"). | mismatch: a suitability claim readable as a tool capability, with zero implementation contribution. |
| `CLM-7` | "provides a tool for dynamic and reflective problem-solving through a structured thinking process" | `SRC-2:4`; `SRC-6:27` — doctrine/design | full | `R1`, `R2`, `R3`, `R5`, `R6`, `R7`, `R9` | none | none | **Supported in its literal reading and only there.** The artifact does provide a tool; the *structure* it supplies is a JSON Schema plus a 54-line instruction, and the "thinking" is `EXT-3`'s. Read as "the artifact performs dynamic and reflective problem-solving", unsupported. | partially supported; scope ambiguity between "provides a tool for X" and "performs X". Recorded per the method's rule on deliberately operational scope: providing a structured surface is a legitimate scope and is **not** a product failure — the mismatch is only with the broader knowledge-production claim `CLM-1` layers on top of it. |

**Cross-claim finding.** Six of seven claims (`CLM-1`–`CLM-6`) name an operation that the artifact's own directive block (`EPI-5`, `SRC-1:177–188`) separately instructs `EXT-3` to perform. The mapping is one-to-one and explicit: features at `SRC-1:149–157` ↔ instructions at `SRC-1:178–188`. The doctrine describes as tool behavior the very operations the prompt delegates to the model. This is not seven independent overclaims; it is one systematic attribution error applied across a feature list.

---

## Block 6 — Bounded conclusion

Route-level findings only. No system-wide epistemic grade is given, and none should be inferred from the concentration of negative findings: several of them are bounded by `EXT-2`/`EXT-3` being uninspected.

**What the artifact retains, retrieves, reshapes, and uses.** It retains every validated request unconditionally in `OBJ-2` (`R5`) and, when two caller fields are truthy, a duplicate reference in `OBJ-3` (`R6`). It **retrieves no retained content at all** (`ABS-2`) — `OBJ-2` is read only for `.length`, `OBJ-3` only for `Object.keys`. It reshapes one payload per call into an ANSI box on stderr (`R9`), verbatim and with no in-boundary consumer (`BAP-3`). It uses retained state for exactly two derived integers/arrays (`R7b`). Retention here does not even license later retrieval, because no read path exists; that is a stronger negative than "no retrieval was observed" and it rests on a full-file enumeration of every read.

**What it acquires, and what happens to source warrant.** One truth-apt object crosses the boundary: the `thought` payload (`EPI-1`, via `R3`). Source warrant is **unknown** — `EXT-3` is uninspected — and the artifact neither preserves nor degrades it, because it never engages with it. Content is preserved byte-identically end to end. The artifact records no provenance: no author, timestamp, session, or lineage field exists on `ThoughtData`. The acquisition is warrant-transparent.

**What it derives, from which premises, in what domain.** Exactly two derivation routes, both entailed and both self-referential. `R7b` derives the retained count and the branch-label set from its own memory; warrant is clean inside the domain "this process's state at this response" and transfers nowhere beyond it — in particular, `thoughtHistoryLength` counts accepted calls, not distinct reasoning steps or progress. `R8` derives a diagnostic proposition from the failed predicate; its warrant covers "this request was rejected" but not the message's specific content, since `"Invalid thought: must be a string"` is false for the schema-conforming input `thought: ""` (`EPI-AMD-8`).

**What it conjectures, tests, accepts, and integrates.** **Nothing, on all four counts, within the boundary.** No route produces a proposition that does not follow from its inputs. No route evaluates any truth-apt content — the only check-shaped route takes argument shape as its target. No evidence-consuming acceptance decision against a named criterion exists anywhere; retention is unconditional and therefore cannot be acceptance. With no acceptance there is no post-acceptance integration, and retention is explicitly not counted as one. Each of these is scoped to `SRC-1` read in full at `2ecb382a`; none says anything about whether `EXT-3` conjectures, tests, or accepts — it is uninspected, and `uninspected` is not `absent`.

**Acceptance criterion, intended use, scope, authority.** The one acceptance criterion anywhere in the register is stated in doctrine and held externally: `SRC-1:188` conditions termination on the model judging itself "truly done and a satisfactory answer is reached". Evaluator `EXT-3`; criterion self-assessed satisfaction; intended use terminate and answer; architectural status `doctrine only`; observed candidate state `no instance observed`; **accepted scope undeterminable from inside this boundary.** The artifact's role in that decision is to echo the boolean unchanged (`R7a`, `ABS-10`).

**The three authorities, kept separate.**
- *Epistemic authority.* The artifact grants it over two proposition classes only: its own retained-state counts (`R7b`) and its own request-rejection diagnostics (`R8`). It grants **none** over any thought's content, any hypothesis, or any problem domain. Passing `R3` licenses no reliance on what a thought says.
- *Operational authority.* Confined to the process. `R3` admits or blocks the rest of the call; `R6`'s predicate gates bucket membership; `R8` blocks retention, render, and status return; `R10` terminates the process on a fatal transport error. The artifact permits, blocks, or changes **no external behavior** — it holds no capability beyond `tools: {}`, touches nothing outside its process, and authorizes no caller.
- *Behavioral-authority paths.* `BAP-1` (directive text → model, unenforceable, horizon = while configured); `EPI-7` (**assertive** text → model, belief-forming, same horizon — proposed, see `EPI-CORR-1`/`EPI-AMD-5`); `BAP-2` (status object → host → model, informational, one call); `BAP-3` (stderr, no in-boundary consumer, therefore **no implemented force**); `BAP-4` (schema, enforcing over 4 of 9 properties server-side, narrowed by `EPI-AMD-7`); `BAP-5` (exit code, terminating).

**Direct behavior/policy adaptation with no truth-apt route.** One: `R4`/`RTE-4` raises `totalThoughts` to `thoughtNumber` on overshoot. I concur with `SCOPE-EPI`'s hand-off classification and return no correction: the update is invariant repair, not re-estimation, and the artifact holds no criterion of "needed" against which the field could be true or false (`EPI-AMD-3`). Its only effects are the stderr header and the echoed value.

**Which claims remain unsupported, and why.** `CLM-1`'s four conjuncts have **no implemented route**, and its fourth is additionally contradicted by the implemented return shape under the artifact reading. `CLM-6` has none. `CLM-2`, `CLM-3`, `CLM-5` have implemented routes that do materially less than the claim states — a label, a label set, and a write with no read path. `CLM-4` is half-implemented. `CLM-7` is supported in its literal "provides a tool" reading. None of these is unsupported *because run evidence is missing*; they are unsupported against inspected source read in full. What the missing run and causal evidence prevents is different and should not be conflated with it: no finding in this lens can rise above `implemented`, no claim about `LOOP-C`'s actual behavior can be made at all, and no statement about whether the unsupported assertions in `EPI-4` in fact induce reliance is available — only that the channel exists to carry them.

**The decision-relevant asymmetry.** The `CLM-1` gap is not merely documentary. The same file that fails to implement verification also ships that verification claim into the consumer's context: `EPI-4` travels with the tool spec through `R1` into the host's tool list, where the model that would rely on it reads it (`EPI-7`). The mismatch is delivered on the same channel as the instruction that reveals who actually performs the work. That co-location — feature claim at `SRC-1:154–157`, matching instruction at `SRC-1:184–187`, hedge present in the second and stripped from the first — is the finding most likely to change what a reviewer does with this artifact.

---

## Proposals (`EPI-n`)

Each states its identity so the orchestrator can rewrite it to a canonical ID. No canonical ID is minted here.

| ID | proposed record | identity | rationale |
|---|---|---|---|
| `EPI-1` | epistemic object — the `thought` payload | field `thought` of `ThoughtData`, `/home/zby/llm/servers/src/sequentialthinking/index.ts:14`; assigned at `:46`; read at `:59`, `:82` | Split from `OBJ-1`, which bundles the truth-apt payload with non-truth-apt control flags. Method output 2 requires splitting parts differing in content, form, checks, and consumers; here truth-aptness itself differs, which is the epistemically load-bearing difference. |
| `EPI-2` | epistemic object — the control-flag envelope | the other eight fields of `ThoughtData`, `index.ts:15–22` | Counterpart of `EPI-1`. Different form, different checks (four validated, five `as`-cast at `:50–54`), different consumers (`RTE-4`, `RTE-6`, `RTE-7`, `CMP-5`). |
| `EPI-3` | evidenced absence — no referential integrity on revision/branch pointers | `revisesThought` and `branchFromThought` are stored (`index.ts:51–52`) and never checked against `thoughtHistory`; search boundary `index.ts` full file, all occurrences of both identifiers enumerated (`:18–19`, `:52`, `:59`, `:66`, `:69`, `:96`) | Not covered by `ABS-6`, which addresses revision *application*. Prevents any claim that the retained revision/branch structure is a well-formed graph over retained thoughts. |
| `EPI-4` | epistemic object — assertive block of the tool description | `index.ts:139–157` ("When to use this tool", "Key features") | Speech act is assertion; content is truth-apt about the artifact; it is the channel carrying `CLM-1` into the model's context. Split required by output 2 and by `EPI-CORR-1`. |
| `EPI-5` | epistemic object — directive block of the tool description | `index.ts:159–188` (parameter guidance, "You should: 1–11") | Speech act is directive; not truth-apt; its force is `BAP-1`'s. Counterpart of `EPI-4`. |
| `EPI-6` | epistemic object — the **claimed** "solution hypothesis" | named at `index.ts:154–155` and `README.md:12`; **no in-boundary representation** — absent from `ThoughtData` (`index.ts:13–23`) and from `inputSchema` (`index.ts:189–234`) | Branch 2 requires inventorying the claimed object. It is the subject of `CLM-1`'s verification claim and the key to `EPI-AMD-4`. |
| `EPI-7` | behavioral-authority path for the assertive channel | `{consumer: EXT-3 (and any human reading the README); channel: EPI-4, carried in the host's tool list via RTE-1, and SRC-2:6–12; force: belief-forming/assertive — it tells the consumer what the tool does, and four of its assertions are unsupported by any implemented route; horizon: for as long as the server is configured and its tool list is in context}` | `BAP-1` records only the directive force. Without this path the `CLM-1` mismatch reads as documentation drift rather than as content delivered into a consumer's context. |
| `EPI-8` | claim record — the README-channel instance of `CLM-1` | `README.md:12`, "Generate and verify solution hypotheses"; consumer = human operator choosing to install; channel = repository/package documentation | See `EPI-CORR-2`. Different consumer, channel, and horizon from `EPI-9`. |
| `EPI-9` | claim record — the prompt-channel instance of `CLM-1` | `index.ts:154–157`; consumer = `EXT-3`; channel = `EPI-4` via `RTE-1`/`EPI-7`; horizon = in-context for the session | See `EPI-CORR-2`. This is the consequential instance. |
| `EPI-10` | epistemic object — echoed control fields of the tool result | `index.ts:110–112` | Split from `OBJ-4`: caller-sourced lineage, no independent warrant. |
| `EPI-11` | epistemic object — derived state propositions of the tool result | `index.ts:113–114` | Split from `OBJ-4`: artifact-derived lineage, entailed warrant within a self-referential domain. The artifact's only produced truth-apt content besides diagnostics. |

## Corrections (`EPI-CORR-n`)

**`EPI-CORR-1` — `OBJ-5` is misclassified by its own stated criterion.**
Registered value: *"tool description text — 54 lines of instruction addressed to the model in the second person ('You should: 1…11')"*.
Correction: the 54 lines (`SRC-1:135–188`) are not uniformly second-person instruction. `SRC-1:135–146` is third-person description of the tool; `SRC-1:148–157` is a "Key features" list that switches grammatical subject mid-list — items 1–5 are second-person capability grants ("You can adjust…", "You can question or revise…"), items 6–9 drop the subject and read as assertions about the tool ("Generates a solution hypothesis", "Verifies the hypothesis…", "Provides a correct answer"); `SRC-1:159–175` is parameter documentation; only `SRC-1:177–188` is the numbered second-person block.
Evidence anchor: `SRC-1:135–188`, contrast `SRC-1:154–157` with `SRC-1:184–187`.
Why it is a correction and not merely an amendment: classifying the whole object as directive makes its assertive content invisible, and the assertive content is precisely what carries `CLM-1` to the consumer. The registered description, applied at the scope it states, would license the conclusion that `OBJ-5` cannot mislead because instructions have no truth value. It can, and that is the run's headline finding.
Proposed remedy: split into `EPI-4` (assertive) and `EPI-5` (directive); amend `BAP-1` per `EPI-AMD-5`; register `EPI-7`.

**`EPI-CORR-2` — `CLM-1` conflates two claim instances with different consumers and channels.**
Registered value: `CLM-1` bundles `SRC-2:12` and `SRC-1:154–157` under one ID with one evidence layer.
Correction: the propositional content is the same, but the two instances differ in every field the method's split rule names. `SRC-2:12` is read by a human operator deciding to install; its channel is repository documentation and its horizon is the installation decision. `SRC-1:154–157` is delivered into the model's context with the tool list; its channel is `EPI-4` via `RTE-1`, its consumer is `EXT-3`, and its horizon is the session. Only the second can induce in-session reliance on a verification that does not occur.
Evidence anchor: `SRC-2:12` vs `SRC-1:154–157`, with `SRC-1:251–253` establishing the second's delivery route.
Proposed remedy: split into `EPI-8` and `EPI-9`; the orchestrator assigns canonical IDs. All comparison rows in block 5 that cite `CLM-1` apply to both instances unless they name `EPI-7`, which applies only to `EPI-9`.

*Considered and declined as corrections:* `ABS-2`, `ABS-6`, `ABS-7`, `ABS-8`, `ABS-9`, `ABS-10`, `RTE-3`, `RTE-4`, `RTE-7`, `OBJ-4`, `CMP-2/a1`, `CMP-3/a1`, `CMP-6/a1` were each re-verified against the source and found accurate as stated. `RTE-8`'s stated justification is unsound (see `EPI-AMD-9`) but its practical exposure is negligible, so it is filed as an amendment rather than a correction; that judgement is recorded here so the orchestrator can overrule it.

## Amendments (`EPI-AMD-n`)

**`EPI-AMD-1` — on `RTE-3`.** The registered description says "four presence/type checks". Three of the four use a falsy guard rather than a presence guard: `!data.thought`, `!data.thoughtNumber`, `!data.totalThoughts` (`SRC-1:32`, `35`, `38`); only `nextThoughtNeeded` uses `typeof` alone (`SRC-1:41`). Consequence for this lens: the **entire** set of content constraints the artifact applies to the truth-apt payload is *not the empty string*, and it arrives accidentally through falsy coercion rather than by declaration — `OBJ-7` declares no `minLength` (`SRC-1:192–195`). Evidence anchor: `SRC-1:32–43` vs `SRC-1:192–195`. Superseded value: none; the record is amended.

**`EPI-AMD-2` — on `RTE-9`/`OBJ-6`.** Fidelity bound on the reshaping. The payload is preserved verbatim: `thought.padEnd(border.length - 2)` pads and never truncates (`SRC-1:82`), and `border` is sized to `Math.max(header.length, thought.length) + 4` (`SRC-1:76`). But the renderer assumes a single-line payload; a multi-line `thought` — the normal shape for chain-of-thought text — produces a border sized to the full multi-line length and a broken box. The render also drops `nextThoughtNeeded` and `needsMoreThoughts` entirely, and computes its revision/branch caption from fields `RTE-3` does not validate, so `isRevision: "banana"` renders as a revision (`SRC-1:64–66` with `SRC-1:50`). Consequence: content lineage is preserved; presentational structure and caption reliability are not. Evidence anchor: `SRC-1:58–84`.

**`EPI-AMD-3` — on `RTE-4` (the `SCOPE-EPI` direct-adaptation hand-off).** Determination returned as requested. `totalThoughts` as an *object* is arguably truth-apt over a caller-indexed scope — it is documented as an "estimate of thoughts needed" (`SRC-1:170`, `SRC-2:24`), and an estimate can be right or wrong. What settles the classification is the *update*, not the field: `RTE-4` applies no evaluator to the estimate's subject matter, consults nothing but the two integers in the current request, and repairs the invariant `totalThoughts >= thoughtNumber` so the stderr header never reads `9/5` (`SRC-1:75`). The artifact holds no criterion of "needed" — that criterion lives at `SRC-1:188` in `EXT-3`'s self-assessment. **Concurrence with the scoping record: `non-truth-apt policy/content update`. No correction is returned, and scope was not expanded.** Evidence anchor: `SRC-1:90–92`, `:75`, `:170`, `:188`.

**`EPI-AMD-4` — on `ABS-3`.** The registered absence ("No evaluator of thought content") is accurate and can be sharpened one stage earlier. The artifact also has **no representable check target** for `CLM-1`'s verification claim: `OBJ-7`'s nine properties contain no hypothesis marker (`SRC-1:189–234`), and `ThoughtData` has no such field (`SRC-1:13–23`). The schema *does* individuate other thought kinds — `isRevision`, `revisesThought`, `branchFromThought`, `branchId` — so the omission is not a general refusal to type thought kinds; hypotheses specifically are unrepresentable. Consequence: the verification claim fails not merely for want of an evaluator but for want of anything to evaluate, and could not be implemented against the current protocol without a schema change. Search boundary: `SRC-1` full file, all nine schema properties enumerated. Evidence anchor: `SRC-1:189–234`, `SRC-1:13–23`.

**`EPI-AMD-5` — on `BAP-1`.** The registered path's `force` field describes only the imperative block. Amended scope: `BAP-1` as written covers the directive block (`EPI-5`, `SRC-1:159–188`). The same channel also carries the assertive block (`EPI-4`, `SRC-1:139–157`), whose force is belief-forming rather than directive — it tells the consumer what the tool does, and four of its assertions have no implemented route. Proposed as a separate path, `EPI-7`. Superseded value: none; `BAP-1`'s stated content stays correct at its narrowed scope. Evidence anchor: `SRC-1:139–188`, delivery route `SRC-1:251–253`.

**`EPI-AMD-6` — on `CMP-2` (companion to `CMP-2/a1`).** `CMP-2/a1` records the *tool-name* mismatch. A parallel *parameter-name* mismatch exists inside the same object: `EPI-5`'s parameter documentation names eight of nine parameters in snake_case — `next_thought_needed`, `thought_number`, `total_thoughts`, `is_revision`, `revises_thought`, `branch_from_thought`, `branch_id`, `needs_more_thoughts` (`SRC-1:168–175`) — while `OBJ-7` declares and `RTE-3` requires camelCase (`SRC-1:189–234`). `SRC-2:21–29` uses camelCase, so the README agrees with the schema and the in-prompt text does not. Epistemic bearing: `CLM-4`'s in-prompt instance (`SRC-1:149`, "You can adjust total_thoughts up or down") names a parameter the schema will not accept. Force is weak — a capable consumer would follow the schema — and it is recorded at that weight. Evidence anchor: `SRC-1:149`, `168–175` vs `SRC-1:189–234`.

**`EPI-AMD-7` — on `BAP-4`.** The registered force, "enforcing on argument shape", holds only for the four required properties. Server-side (`RTE-3`) nothing enforces `OBJ-7`'s `minimum: 1` constraints on `thoughtNumber`, `totalThoughts`, `revisesThought`, `branchFromThought`, nor the declared types of the five optional properties, which are `as`-cast and erased at runtime (`SRC-1:50–54`). Those constraints are enforced only in `EXT-2`, which is uninspected. Consequence: for a caller that speaks JSON-RPC directly, `BAP-4`'s enforcing force covers 4 of 9 properties and no value ranges. Evidence anchor: `SRC-1:29–56` vs `SRC-1:189–234`.

**`EPI-AMD-8` — on `OBJ-8`.** The artifact's diagnostic propositions are not uniformly true. `thought: ""` is fully conforming to `OBJ-7` (`{type: "string"}`, no `minLength`) yet fails `!data.thought` (`SRC-1:32`) and is returned the message `"Invalid thought: must be a string"` — which is false of the input, since `""` is a string. The same falsy pattern makes `"Invalid thoughtNumber: must be a number"` false for the input `0`, though `0` is excluded by the schema's `minimum: 1` and so reaches `RTE-3` only from a caller that bypasses `EXT-2`'s validation. Epistemic consequence: `RTE-8` warrants reliance on *the fact of rejection* but not on the *stated reason*. Evidence anchor: `SRC-1:32–43` vs `SRC-1:192–209`.

**`EPI-AMD-9` — on `RTE-8`.** The registered parenthetical, "no state rollback needed (nothing was written before validation)", is true about validation but does not support the conclusion. Writes at `SRC-1:94` and `SRC-1:96–101` precede two further operations inside the same `try`: `formatThought` (`SRC-1:103`) and `JSON.stringify` (`SRC-1:109`). A throw from either — `'─'.repeat(n)` raises `RangeError` above V8's maximum string length, reachable only with a pathologically large `thought` — returns `isError: true` with `OBJ-2` and `OBJ-3` already mutated. Practical exposure over stdio is negligible and is recorded at that weight; the epistemic consequence is the part that matters: **an `isError` response does not warrant the proposition "nothing was retained".** Evidence anchor: `SRC-1:87–129`, ordering at `:94`, `:96–101`, `:103`, `:109`. I considered filing this as `EPI-CORR-3` and declined on grounds of practical weight; the orchestrator may overrule.

## Targeted reads made (for central registration)

All reads were read-only, inside the frozen boundary. No fetch, pull, refresh, checkout, widening, or mutation occurred.

| # | path | scope read | maps to | tool |
|---|---|---|---|---|
| 1 | `/home/zby/llm/servers/src/sequentialthinking/index.ts` | whole file, lines 1–279 | `SRC-1` (already registered as read in full; this is an independent re-read) | Read |
| 2 | `/home/zby/llm/servers/src/sequentialthinking/README.md` | whole file, lines 1–63 | `SRC-2` (already registered) | Read |
| 3 | `/home/zby/llm/servers/src/sequentialthinking/package.json` | whole file, lines 1–32 | `SRC-3` — **new inspected scope**: previously registered as "whole file"; this read is confirmatory. Used only to check the `description` field for an unregistered doctrine claim (found: `SRC-3:4`, subsumed by `CLM-7`) and to re-verify `CMP-3/a1` and `CMP-6/a1`. | Read |
| 4 | `/home/zby/llm/servers/README.md` | lines 25–29 | `SRC-6` — **slightly wider than registered** (`SRC-6:27` only). Lines 25–26 and 28–29 were read as adjacent catalogue entries for other servers and are not material; nothing from them is used. Reported so the register can record the actual read. | Bash (`sed -n '25,29p'`) |

Not read: `tsconfig.json` (`SRC-4`), root `package.json`/`tsconfig.json`/`package-lock.json` (`SRC-5`). Their omission prevents no conclusion in this lens; build configuration and dependency pinning carry no truth-apt content edge.

## Evidence limitations, each paired with the conclusion it prevents

| limitation | conclusion it prevents |
|---|---|
| `ABS-4` — no run traces, tests, fixtures, or logs anywhere in the register | Every observed-candidate-state in block 4 is `no instance observed`. Prevents any `observed` or `causally supported` wrapper status for any finding in this lens. Prevents any statement that a candidate hypothesis fails to traverse a phase — only that no evidence of traversal exists. |
| `EXT-3` uninspected | Whether any `thought` payload is a hypothesis, a conjecture, a restatement, or a question; therefore whether the acquired content is ampliative. Forces `EPI-1` into the indeterminate disposition. Also prevents any conclusion about whether hypothesis generation, verification, revision, branching, or filtering occurs *at all* in the deployed assembly — the artifact's non-implementation of `CLM-1`–`CLM-6` says nothing about `EXT-3`. |
| `EXT-2` uninspected | Whether `EPI-4` and `EPI-5` reach a model; therefore whether `BAP-1` and `EPI-7` are live paths rather than latent ones. Prevents any conclusion that the `CLM-1` mismatch has induced reliance — only that the channel to do so exists. Also prevents any conclusion about whether `OBJ-7`'s `minimum: 1` and optional-field types are enforced anywhere (`EPI-AMD-7`). |
| `EXT-1` uninspected | Whether `RTE-3` is the first check a request meets, and whether malformed frames are rejected earlier. Prevents any claim that `RTE-3` is the artifact's complete input-validation surface as deployed. |
| No `node_modules`, no `dist/` | Whether the published package behaves as `SRC-1` does. Every finding is scoped to source at `2ecb382a`. |
| Revision is ~20 months before the analysis cutoff | Every finding, including the `CLM-1` mismatch, is pinned to `2ecb382a` and says nothing about current upstream state. |
| Boundary kind `complete artifact, partial loop` | No finding in this lens describes the behavior `LOOP-C` produces. `CLM-1`'s assembly reading (`RC4`) is undecidable from inside this boundary; deciding it would require widening, which this run does not authorize. |
| No published-npm-tarball or host-configuration inspection | Whether any deployed host is wired with the README's `sequential_thinking` name (`CMP-2/a1`), and therefore whether that mismatch has any field consequence. |

---

*This lens informs a review. It does not accept the system's claims, does not assign a system-wide epistemic grade, and makes no publication decision.*
