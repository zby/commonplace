# Evidence packet — run `AGS-2026-08-21-SEQTHINK`

Canonical location for logical records 1–5 of the emitted result (identity; boundary/revision/tier; source register; shared records; runtime account). Frozen at step 2/4 of `analyse-agentic-system`. Lens workers consume this packet and the frozen read-only boundary; they must not reacquire, refresh, or widen sources.

---

## Record 1 — Run / staging identity

| field | value |
|---|---|
| run/result ID | `AGS-2026-08-21-SEQTHINK` |
| system identifier | `sequentialthinking` MCP server (`@modelcontextprotocol/server-sequential-thinking`), subtree `src/sequentialthinking` of github.com/modelcontextprotocol/servers |
| staging identity | `kb/work/multistage-write-analyse-agentic-system-20260820/trials/sequentialthinking-rerun/` |
| publication target | none authorized for this run — logical result retained under the staging identity (see record 11) |
| analysis cutoff | 2026-08-21, against frozen revision `2ecb382a02d7921511180dfbadcef24eb66a052f` |

## Record 2 — System boundary, revision, and overall evidence tier

### In-scope determination

The subject is an MCP server: a component whose deployed behavior depends on model calls it **serves** but never issues. Step 1.2's second route (narrower system, model call may live outside its own boundary, "such as an MCP server or tool") admits it. In scope.

### Boundary kind: **complete artifact, partial loop**

`src/sequentialthinking` is a complete, independently distributed artifact (npm package with its own `package.json`, `bin`, and build). But the loop its doctrine advertises — iterative, revisable, branching problem-solving — is produced jointly by the artifact, an MCP host client, and a model, only one of which is inside the boundary. Conclusions may be whole-artifact; they may not describe the behavior the crossing loop produces.

### Inclusions (by function)

Components whose scheduling, context selection, retained state, action execution, checking, acceptance, or authority decisions produce or constrain the behavior under review, and that ship inside the artifact:

- the request-handler registrations and their dispatch predicate (`index.ts:251–267`);
- the tool specification and its natural-language instruction text (`index.ts:133–235`), which is the artifact's only influence on the reasoning loop;
- the per-call validation, coercion, retention, formatting, and return logic (`index.ts:25–131`);
- process-local retained state (`thoughtHistory`, `branches`, `index.ts:26–27`);
- the stderr render path (`index.ts:58–84, 104, 272`);
- packaging and distribution contract (`package.json`, `tsconfig.json`);
- shipped doctrine (`src/sequentialthinking/README.md`; root `README.md:27`).

### Exclusions (external participants), each with the conclusion it prevents

| ID | External participant | Evidence status | Conclusion it prevents |
|---|---|---|---|
| `EXT-1` | `@modelcontextprotocol/sdk` 0.5.0 — `Server`, `StdioServerTransport`, request schemas. Pinned at `package-lock.json:808–817`; **no `node_modules` present in the checkout**, so its source was not inspected. | uninspected | Any claim about how JSON-RPC framing, method routing, protocol error handling, cancellation, or connection lifecycle actually behave. The artifact's dispatch loop is described only at the registration surface it exposes. |
| `EXT-2` | MCP host client (README's worked example is Claude Desktop, `README.md:43–59`). Owns process launch, tool-list injection, the decision to call the tool, and the conversation transcript. | uninspected | Any claim about whether or how the tool description reaches a model, how often it is called, or what the caller does with the returned status object. |
| `EXT-3` | The model that issues the tool calls and authors every `thought` string. | uninspected | Any claim that the advertised reasoning discipline (revision, branching, hypothesis generation and verification) actually occurs; any claim about the *quality* or *effect* of the loop. |
| `EXT-4` | Sibling servers in the same monorepo (`src/*` workspaces). | out of boundary by declaration | Nothing relevant — no code path in the subtree references them. |

### Revision

`2ecb382a02d7921511180dfbadcef24eb66a052f` (committed 2024-12-06), clean working tree, at `/home/zby/llm/servers`. This is a **stable but old** boundary: roughly 20 months before the analysis cutoff. Published limitation — every conclusion is pinned to this revision and says nothing about the current upstream state.

### Overall evidence tier: **`code-grounded`**

Every material loop the boundary *includes* rests on inspected TypeScript source (`index.ts`, read in full). `EXT-1`'s dispatch machinery is a declared external dependency, which per the tier rule neither raises nor lowers the tier; it is carried as the limitation named above. No observed run and no causal experiment exist anywhere in the register, which bounds conclusion statuses at `implemented` for everything the artifact does.

## Record 3 — Source register

| ID | Kind | Identity / location | Revision / capture | Evidence layer | Inspected scope | Citation anchors | Access gaps |
|---|---|---|---|---|---|---|---|
| `SRC-1` | existing checkout, file | `/home/zby/llm/servers/src/sequentialthinking/index.ts` | `2ecb382a`, clean | implementation | whole file, 279 lines, read in full | `SRC-1:<line>` | none |
| `SRC-2` | existing checkout, file | `/home/zby/llm/servers/src/sequentialthinking/README.md` | `2ecb382a` | doctrine/design | whole file, 63 lines | `SRC-2:<line>` | none |
| `SRC-3` | existing checkout, file | `/home/zby/llm/servers/src/sequentialthinking/package.json` | `2ecb382a` | implementation (packaging/distribution contract); the `description` field is doctrine/design | whole file | `SRC-3:<line>` | built `dist/` not present |
| `SRC-4` | existing checkout, file | `/home/zby/llm/servers/src/sequentialthinking/tsconfig.json` | `2ecb382a` | implementation (build config) | whole file | `SRC-4:<line>` | none |
| `SRC-5` | existing checkout, files | `/home/zby/llm/servers/package.json`, `/home/zby/llm/servers/tsconfig.json`, `/home/zby/llm/servers/package-lock.json` | `2ecb382a` | implementation (workspace + dependency pinning) | root manifests read; lockfile inspected only at the `@modelcontextprotocol/sdk` entry | `SRC-5:package-lock.json:808–817` | lockfile not read in full |
| `SRC-6` | existing checkout, file | `/home/zby/llm/servers/README.md` | `2ecb382a` | doctrine/design | lines 25–29 (the one-line catalogue entry for this server at `:27`, plus adjacent entries for other servers) | `SRC-6:27` | rest of file not material to boundary |

Register-wide access gaps, each with the conclusion prevented:

- **No `node_modules`, no `dist/`** → SDK behavior and the built artifact are uninspected; prevents any claim about runtime protocol behavior or about what the published package actually contains beyond the declared `files: ["dist"]` (`SRC-3:13–15`).
- **No tests, no fixtures, no logs, no run traces anywhere in the subtree** → prevents any `observed` or `causally supported` status for any finding in this run.
- **No published-npm-tarball inspection, no host configuration inspected** → prevents claims about deployed configuration in the field.

**Targeted reads added centrally after the freeze.** All read-only, all inside the frozen boundary; nothing was fetched, refreshed, or mutated.

| Read | Source | Effect on the register | Downstream invalidation |
|---|---|---|---|
| Memory lens: `index.ts` full, `src/sequentialthinking/README.md` full, `package.json` full | `SRC-1`, `SRC-2`, `SRC-3` | none — all already registered at whole-file scope | none |
| Epistemic lens: same three files, full | `SRC-1`, `SRC-2`, `SRC-3` | none — confirmatory re-reads at registered scope | none |
| Epistemic lens: root `README.md:25–29` | `SRC-6` | **inspected scope widened** from line 27 to lines 25–29; row updated above | none — lines 25–26 and 28–29 are catalogue entries for unrelated servers, and no finding in the run uses them |
| Orchestrator verification: `index.ts:148–157`, `:177–188`, `:192–195` | `SRC-1` | none — already registered at whole-file scope | none |

No targeted read invalidated a downstream finding, so no lens work was redone on this account.

## Record 4 — Shared component, object, route, claim, absence, and authority records

Ownership per the instruction's canonical-records table. Amendments are listed under the record they attach to.

### Components (`CMP-*`)

| ID | Component | Form / substrate | Evidence |
|---|---|---|---|
| `CMP-1` | `SequentialThinkingServer` class — the stateful thought recorder | TypeScript class, process-local instance | `SRC-1:25–131`, instantiated `SRC-1:249` |
| `CMP-2` | `SEQUENTIAL_THINKING_TOOL` — tool spec: name, ~54-line natural-language description, JSON Schema | symbolic (JSON Schema) + natural-language (description) | `SRC-1:133–235` |
| `CMP-3` | MCP `Server` instance and its two handler registrations | TypeScript, delegating to `EXT-1` | `SRC-1:237–267` |
| `CMP-4` | `StdioServerTransport` binding and `runServer` entrypoint | TypeScript, delegating to `EXT-1` | `SRC-1:269–278` |
| `CMP-5` | `formatThought` stderr renderer (chalk-coloured box drawing) | TypeScript + ANSI text | `SRC-1:58–84`, invoked `SRC-1:104` |
| `CMP-6` | packaging/distribution contract: `bin` name, `files: ["dist"]`, build scripts, pinned deps | npm manifest + tsconfig | `SRC-3`, `SRC-4`, `SRC-5` |
| `CMP-7` | shipped doctrine: feature list, tool description, usage guidance, host config example | Markdown | `SRC-2`, `SRC-6:27` |

**Amendment `CMP-2/a1` (doctrine–implementation name mismatch).** `SRC-2:16` documents the tool as `sequential_thinking`; the implementation registers and dispatches on `sequentialthinking` (`SRC-1:134`, `SRC-1:256`), and the package name is `server-sequential-thinking` (`SRC-3:2`). A host wiring itself from the README's tool name would not match the dispatch predicate. Evidence anchor: `SRC-1:134,256` vs `SRC-2:16`. Superseded value: none — the record is amended, not replaced.

**Amendment `CMP-3/a1` (version disagreement).** The MCP server identity advertised over the protocol declares `version: "0.2.0"` (`SRC-1:240`); the package it ships in declares `0.6.2` (`SRC-3:3`). A client reading server capabilities is told a different version than the registry. Evidence anchor: `SRC-1:237–241` vs `SRC-3:3`.

**Amendment `CMP-6/a1` (declared, unused dependency).** `yargs` and `@types/yargs` are declared dependencies (`SRC-3:24,28`) but no source file in the boundary imports them (search boundary: all four subtree files, full-text). No argument parsing exists; the binary takes no options.

### Operative objects (`OBJ-*`)

| ID | Object | Form | Producer | Consumer | Persistence |
|---|---|---|---|---|---|
| `OBJ-1` | `ThoughtData` record — one validated thought plus its control flags | in-memory object (`SRC-1:13–23`, built `SRC-1:45–55`) | `EXT-3` authors `thought`; `CMP-1` validates and shapes | `OBJ-2`, `OBJ-3`, `CMP-5` | process lifetime |
| `OBJ-2` | `thoughtHistory` — append-only array of every accepted `OBJ-1` | in-memory array (`SRC-1:26`, written `SRC-1:94`) | `CMP-1` | read **only** for `.length` (`SRC-1:114`) | process lifetime |
| `OBJ-3` | `branches` — map from caller-authored `branchId` to array of `OBJ-1` | in-memory record (`SRC-1:27`, written `SRC-1:96–101`) | `CMP-1` | read for content by nothing; read on the **write side** at `SRC-1:97,100` for bucket existence and resolution; read for **derivation** at `SRC-1:113` (`Object.keys`) | process lifetime |
| `OBJ-4` | tool result status object — `{thoughtNumber, totalThoughts, nextThoughtNeeded, branches[], thoughtHistoryLength}` | JSON string in an MCP text content block (`SRC-1:106–117`) | `CMP-1` | `EXT-2` → `EXT-3` | single response |
| `OBJ-5` | tool description text, 54 lines (`SRC-1:135–188`) — **container record; corrected by `OBJ-5/c1` and split into `OBJ-11` (assertive) and `OBJ-12` (directive)**. It is *not* uniformly second-person instruction: `:135–146` is third-person description, `:148–157` is a "Key features" list that switches grammatical subject mid-list (items 1–5 grant capability in the second person, items 6–9 drop the subject and assert what the tool does), `:159–175` is parameter documentation, and only `:177–188` is the numbered second-person block. | natural-language, static shipped material | authors of `CMP-2` | `EXT-3`, via `EXT-2`'s tool list | shipped, immutable at runtime |
| `OBJ-6` | rendered thought box on stderr | ANSI-coloured text (`SRC-1:78–83`, emitted `SRC-1:104`) | `CMP-5` | no in-boundary consumer; whatever captures the process's stderr | not retained by the artifact |
| `OBJ-7` | tool `inputSchema` — JSON Schema, 9 properties, 4 required | symbolic (`SRC-1:189–234`) | authors of `CMP-2` | `EXT-2` (client-side arg shaping), and mirrored by `RTE-3` server-side | shipped |
| `OBJ-8` | error result object — `{error, status:'failed'}` with `isError: true` | JSON in MCP content block (`SRC-1:118–129`) | `CMP-1` catch block | `EXT-2` → `EXT-3` | single response |

### Routes (`RTE-*`)

| ID | Route | Endpoints | Progression | Evidence |
|---|---|---|---|---|
| `RTE-1` | tool discovery — ListTools returns `CMP-2` verbatim | `EXT-2` → `CMP-3` → `EXT-2` | pull, once per client tool-list refresh (timing owned by `EXT-2`) | `SRC-1:251–253` |
| `RTE-2` | tool invocation dispatch — name equality check, delegate or return unknown-tool error | `EXT-2` → `CMP-3` → `CMP-1` | one hop; unmatched names return an `isError` text block, not a protocol error | `SRC-1:255–267` |
| `RTE-3` | validation — four presence/type checks on `thought`, `thoughtNumber`, `totalThoughts`, `nextThoughtNeeded`; five optional fields cast without validation | `CMP-1` internal | throw → `RTE-8` | `SRC-1:29–56` |
| `RTE-4` | totalThoughts coercion — if `thoughtNumber > totalThoughts`, raise `totalThoughts` to `thoughtNumber` on the record before retention | `CMP-1` internal, mutates `OBJ-1` | one-way, upward only | `SRC-1:90–92` |
| `RTE-5` | history retention — unconditional append of `OBJ-1` to `OBJ-2` | `CMP-1` → `OBJ-2` | append-only; no eviction, dedup, ordering, or size bound | `SRC-1:94` |
| `RTE-6` | branch retention — append `OBJ-1` to `OBJ-3[branchId]`, creating the bucket on first use; **requires both** `branchFromThought` and `branchId` | `CMP-1` → `OBJ-3` | append-only; the same object reference is in `OBJ-2` too | `SRC-1:96–101` |
| `RTE-7` | status return — assemble and return `OBJ-4` | `CMP-1` → `EXT-2` | echoes three caller-supplied fields (post-`RTE-4`), plus two values derived from retained state | `SRC-1:106–117` |
| `RTE-8` | error return — catch anything thrown, return `OBJ-8` with `isError` | `CMP-1` → `EXT-2` | no retry, no state rollback needed (nothing was written before validation) | `SRC-1:118–129` |
| `RTE-9` | stderr render — format `OBJ-1` into `OBJ-6`, write to `console.error` | `CMP-5` → process stderr | fire-and-forget; not part of the protocol response | `SRC-1:58–84, 104` |
| `RTE-10` | process lifecycle — connect transport, log a banner, `process.exit(1)` on fatal | `CMP-4` → `EXT-1` | no retry, no reconnect, no graceful shutdown, no signal handling | `SRC-1:269–278` |

### Objects registered from lens returns (splits and claimed-only objects)

Registered after the lenses returned; the lens-local proposal tags are discarded and the mapping is recorded in `result.md` §8. Splits do not delete the parent record — the parent stays as the container, and route rows citing the parent remain valid where the split is not load-bearing.

| ID | Object | Split of | Form | Truth-apt? | Evidence |
|---|---|---|---|---|---|
| `OBJ-9` | the `thought` payload — the single content-bearing field, one caller-authored natural-language string | `OBJ-1` | natural-language string | **yes**, per instance and caller-determined | `SRC-1:14, 32–34, 46, 59, 82, 94` |
| `OBJ-10` | the control-flag envelope — the other eight `ThoughtData` fields | `OBJ-1` | numeric/boolean/string control fields; four validated, five `as`-cast and erased at runtime | no (see `RTE-4/a1`) | `SRC-1:15–22, 35–43, 47–54` |
| `OBJ-11` | **assertive block** of the tool description — "When to use this tool" and "Key features" | `OBJ-5` | natural-language assertion, shipped static | **yes** — assertions about what the artifact does, with truth values over the artifact's own behavior | `SRC-1:139–157` |
| `OBJ-12` | **directive block** of the tool description — parameter guidance and "You should: 1–11" | `OBJ-5` | natural-language directive, shipped static | no — directives have no truth value | `SRC-1:159–188` |
| `OBJ-13` | the **claimed** "solution hypothesis" — the object `CLM-1` says the tool generates and verifies. **No in-boundary representation**: absent from `ThoughtData` and from `inputSchema` | — (claimed only) | claimed only; no implemented form | **yes by claim**; ampliation established by the claim evidence, since pairing generation with verification presupposes non-entailment | named `SRC-1:154–155`, `SRC-2:12`; absence anchored `SRC-1:13–23, 189–234` |
| `OBJ-14` | echoed control fields of the tool result — `thoughtNumber`, `nextThoughtNeeded`, `totalThoughts` post-`RTE-4` | `OBJ-4` | JSON numbers/booleans | no — caller-sourced, no independent warrant | `SRC-1:110–112` |
| `OBJ-15` | derived state propositions of the tool result — `branches` and `thoughtHistoryLength` | `OBJ-4` | JSON array / number | **yes** — each asserts a fact about the artifact's own retained state | `SRC-1:113–114` |

### Claims (`CLM-*`) — orchestrator namespace; truth/scope/warrant fields owned by the epistemic lens

| ID | Claim | Source anchor | Evidence layer |
|---|---|---|---|
| `CLM-1` | "Generate and verify solution hypotheses" / "Generates a solution hypothesis · Verifies the hypothesis based on the Chain of Thought steps · Repeats the process until satisfied · Provides a correct answer" — stated in a list headed "Key features" of the tool. **Split by `CLM-1/a1` into two channel instances below; `CLM-1` is retained as the shared propositional content, so existing citations stay valid.** | `SRC-2:12`; `SRC-1:154–157` | doctrine/design |
| `CLM-1a` | the **README-channel** instance of `CLM-1`: "Generate and verify solution hypotheses". Consumer: a human operator deciding whether to install. Channel: repository/package documentation. Horizon: the installation decision. | `SRC-2:12` | doctrine/design |
| `CLM-1b` | the **prompt-channel** instance of `CLM-1`, delivered into the model's context with the tool list. Consumer: `EXT-3`. Channel: `OBJ-11` via `RTE-1`, path `BAP-6`. Horizon: the session. **This is the consequential instance — the only one that can induce in-session reliance on a verification that does not occur.** | `SRC-1:154–157`, delivery route `SRC-1:251–253` | doctrine/design |
| `CLM-2` | "Revise and refine thoughts as understanding deepens"; "You can question or revise previous thoughts" | `SRC-2:9`; `SRC-1:150` | doctrine/design |
| `CLM-3` | "Branch into alternative paths of reasoning"; "you can branch or backtrack" | `SRC-2:10`; `SRC-1:153` | doctrine/design |
| `CLM-4` | "Adjust the total number of thoughts dynamically"; "You can adjust total_thoughts up or down as you progress" | `SRC-2:11`; `SRC-1:149` | doctrine/design |
| `CLM-5` | Suited to "Tasks that need to maintain context over multiple steps" | `SRC-2:38`; `SRC-1:146` | doctrine/design |
| `CLM-6` | Suited to "Situations where irrelevant information needs to be filtered out" | `SRC-2:39`; `SRC-1:146` | doctrine/design |
| `CLM-7` | "provides a tool for dynamic and reflective problem-solving through a structured thinking process" | `SRC-2:4`; `SRC-6:27` | doctrine/design |

### Evidenced absences (`ABS-*`) — status `absent`, each with its recorded search boundary

| ID | Absence | Recorded search boundary | Conclusion it prevents / supports |
|---|---|---|---|
| `ABS-1` | No durable persistence. No filesystem, database, or network write of any kind; the only dependencies are `@modelcontextprotocol/sdk`, `chalk`, `yargs` (unused). | all four subtree files, full text; `SRC-3:21–25` | Prevents any claim of cross-process or cross-session memory. Supports: retained state dies with the process. |
| `ABS-2` | No retrieval of retained thought *content*. No route returns a stored `thought` string. **[amended `ABS-2/a1`]** Retained state is read for content by nothing; on the write side at `SRC-1:97,100` (bucket existence check and reference resolution); for derivation at `SRC-1:113–114` (`Object.keys`, `.length`). | `SRC-1`, full file; every read of `thoughtHistory` (26, 94, 114) and `branches` (27, 97, 98, 100, 113) enumerated | Prevents any claim that the server supplies prior thoughts back into a caller's context. |
| `ABS-3` | No evaluator of thought content. `RTE-3` checks JSON types only; nothing inspects, scores, compares, or verifies what a thought says. | `SRC-1`, full file | Prevents any claim that the artifact checks, verifies, or disposes a hypothesis. Directly bounds `CLM-1`. |
| `ABS-4` | No tests, fixtures, run logs, or execution traces. | subtree file listing (4 files) and repo root listing | Prevents every `observed` and `causally supported` status in this run. |
| `ABS-5` | No per-connection or per-session state isolation. One module-level `thinkingServer` instance (`SRC-1:249`) holds all state for the process lifetime. | `SRC-1`, full file | Prevents any claim of multi-session separation. Supports: state is process-global. In the shipped stdio deployment one process serves one client, so the practical exposure is bounded — but that bound comes from `EXT-2`'s launch model, not from the artifact. |
| `ABS-6` | No revision operation. `isRevision`/`revisesThought` are stored on `OBJ-1` and used only to choose a stderr label and caption (`SRC-1:64–66`). No prior entry is superseded, marked, replaced, or removed. | `SRC-1`, full file; all uses of both fields enumerated | Prevents any claim that the artifact applies a revision to retained history. Bounds `CLM-2`. |
| `ABS-7` | `needsMoreThoughts` is accepted by `OBJ-7`, validated nowhere, stored on `OBJ-1`, and never read. | `SRC-1`, full file; all occurrences enumerated (lines 21, 54, 228) | Prevents any claim that this parameter affects any behavior. |
| `ABS-8` | No downward adjustment of `totalThoughts` by the artifact. `RTE-4` only raises it. | `SRC-1:90–92`, full file | Bounds `CLM-4`: "up or down" is a caller capability (the caller may send a smaller number next call), not an artifact behavior. |
| `ABS-9` | No filtering, summarization, compression, or relevance selection of any content. | `SRC-1`, full file | Bounds `CLM-6`. |
| `ABS-12` | No referential integrity on revision/branch pointers. `revisesThought` and `branchFromThought` are stored and never checked against `thoughtHistory`; a revision may point at a thought number that does not exist. *(Registered from epistemic-lens proposal `EPI-3`.)* | `SRC-1` full file; all occurrences of both identifiers enumerated (`:18–19, :52, :59, :66, :69, :96`) | Prevents any claim that the retained revision/branch structure is a well-formed graph over retained thoughts. Distinct from `ABS-6`, which addresses revision *application* rather than pointer validity. |
| `ABS-11` | No invalidation, reset, or clear operation for retained state. Every occurrence of `thoughtHistory` (26, 94, 114) and `branches` (27, 97, 98, 100, 113) is an initializer, an append, a bucket create, or a derived read. No `delete`, `splice`, `pop`, `shift`, `length = 0`, or reassignment. No reset parameter in `OBJ-7`; no documented reset in `SRC-2`. *(Registered from memory-lens proposal `MEM-1`.)* | `SRC-1` full file, both symbols fully enumerated; `SRC-2` full file; `OBJ-7` (`SRC-1:189–234`) | Prevents any claim that a caller, a session boundary, or the artifact itself can bound, scope, or expire what has accumulated. Supports: the only way to drop retained state is process termination, so retention duration is `EXT-2`'s launch decision, not the artifact's. Distinct from `ABS-1`, `ABS-5`, `ABS-6`, none of which state the absence of a discard path. |
| `ABS-10` | No scheduler. Nothing in the artifact decides when the next thought happens: no timer, no loop, no callback registration, no continuation. `nextThoughtNeeded` is received and echoed unchanged (`SRC-1:112`). | `SRC-1`, full file | Prevents any claim that the artifact drives, paces, or terminates the thinking loop. |

### Behavioral-authority paths (`BAP-*`) — `{consumer, channel, force, horizon}`

| ID | Path |
|---|---|
| `BAP-1` | `{consumer: EXT-3, the model in the host session; channel: OBJ-12, the directive block of the tool description carried in the host's tool list; force: strong directive instruction — eleven numbered "You should" rules (SRC-1:177–188) plus parameter guidance, but nothing in the artifact can oblige compliance; horizon: for as long as the server is configured in the host and its tool list is in context}` **[amended `BAP-1/a1`: scope narrowed from `OBJ-5` to `OBJ-12`; the assertive half of the same channel is now `BAP-6`. Superseded value: channel `OBJ-5`, the whole 54-line description.]** |
| `BAP-6` | `{consumer: EXT-3, and any human reading the README; channel: OBJ-11, the assertive block, carried in the host's tool list via RTE-1, plus SRC-2:6–12; force: belief-forming/assertive — it tells the consumer what the tool does, and four of its assertions have no implemented route; horizon: as BAP-1}`. **Registered because `BAP-1` recorded only directive force. Without this path the `CLM-1` mismatch reads as documentation drift rather than as an unsupported assertion delivered into a consumer's context.** |
| `BAP-2` | `{consumer: EXT-2, and through it EXT-3; channel: OBJ-4, the JSON status object in the tool result; force: informational — three echoed control fields and two derived state values, with no directive content and no enforcement; horizon: the single tool call that produced it, plus whatever transcript retention EXT-2 applies}` |
| `BAP-3` | `{consumer: none inside the boundary — a human operator or log collector attached to the process's stderr; channel: OBJ-6 on file descriptor 2; force: none implemented, no consequential consumer exists within the boundary; horizon: process lifetime}` |
| `BAP-4` | `{consumer: EXT-2's argument construction, then RTE-3 server-side; channel: OBJ-7, the JSON Schema in the tool spec; force: enforcing on argument shape — RTE-3 rejects a call missing any of four required fields; horizon: same as BAP-1}` |
| `BAP-5` | `{consumer: EXT-2's process supervisor; channel: process exit code 1 on fatal transport error (SRC-1:275–278); force: terminating — the artifact removes itself rather than degrading; horizon: one process lifetime}` |

### Amendments registered from lens returns

Each is a finding *about* a registered record, carrying its evidence anchor and any superseded value, cited through the ID of the record it annotates. Lens-local proposal tags are discarded at registration and do not appear in the emitted result; the mapping is recorded in `result.md` §8.

| Amendment | Annotates | Finding | Evidence anchor | Superseded value |
|---|---|---|---|---|
| `OBJ-3/a1` | `OBJ-3` | `branches` bundles two parts with different consumers, checks, and authority paths: the **key set** is consumed by `RTE-7` and travels `BAP-2` to `EXT-3`; the **bucket contents** have no consumer anywhere in the boundary — no route ever reads a bucket's elements. | `SRC-1:113` (keys read) vs `SRC-1:96–101` (buckets written, never read for elements) | none — the single-row description is amended, not replaced |
| `OBJ-4/a1` | `OBJ-4` | The `branches` field is **verbatim accumulated caller text**, not a derived summary: the derivation is in selection only (keys, not values), and the returned tokens are the exact strings `EXT-3` supplied on earlier calls, admitted without validation. It is therefore the only accumulated caller-authored text that ever returns to a consumer. It has no cap and no discard path (`ABS-11`), so it grows monotonically with distinct `branchId` values and never shrinks. | `SRC-1:53`, `SRC-1:113` | the "two values derived from retained state" characterization in the `RTE-7` progression field |
| `OBJ-4/a2` | `OBJ-4` | `thoughtHistoryLength` is a **process-lifetime counter of accepted calls**, not a measure of the current thinking sequence. It counts revision and branch thoughts alike, never resets (`ABS-11`), and with one module-level instance (`ABS-5`) spans every thinking episode the process handles. It can diverge arbitrarily from the `thoughtNumber` echoed two fields above it in the same JSON object, and a second episode starting at `thoughtNumber: 1` receives a count carrying the first episode's calls. Bounds `CLM-5`. | `SRC-1:94, 110, 114, 249` | none |
| `OBJ-1/a1` | `OBJ-1`, and by reference `RTE-4`, `RTE-5`, `RTE-6` | Retention is **by shared reference, and the retained record is the mutated one**. `RTE-4` mutates `totalThoughts` in place *before* both retention writes; the same object reference then enters `thoughtHistory` and, when eligible, a `branches` bucket. Consequences: exactly one copy, so the two containers cannot diverge and carry no provenance separation; retained history preserves the coerced value, not what the caller sent; `formatThought` renders the post-coercion value too, so not even the stderr trace preserves the original. The artifact's single write-over of acquired data is silent and unrecorded. | `SRC-1:88–104` | none |
| `RTE-6/a1` | `RTE-6` | The branch-eligibility predicate `branchFromThought && branchId` (`SRC-1:96`) is a **truthiness test on two unvalidated fields** (`SRC-1:52–53`). A call supplying `branchId` but omitting `branchFromThought`, or sending a falsy value for either, produces no bucket, no error, and no signal: the thought lands in `thoughtHistory` and the label vanishes. Because the key set is the only accumulated authored text that returns (`OBJ-4/a1`), a silent write-side drop is a silent read-back loss, visible to the caller only as a label that never appears. **Both lenses reached this independently; the epistemic lens adds that `branchFromThought: 0` is falsy here while the schema's `minimum: 1` would have excluded it, so the bypass is reachable only from a caller that skips `EXT-2`'s validation.** | `SRC-1:52–53, 96–101, 113` | none |
| `RTE-3/a1` | `RTE-3` | "Four presence/type checks" is imprecise in a load-bearing way: three of the four use a **falsy guard**, not a presence guard (`!data.thought`, `!data.thoughtNumber`, `!data.totalThoughts`); only `nextThoughtNeeded` uses `typeof` alone. Consequence: the entire set of content constraints the artifact applies to the truth-apt payload is *not the empty string*, and it arrives accidentally through falsy coercion rather than by declaration — `OBJ-7` declares no `minLength`. | `SRC-1:32–43` vs `SRC-1:192–195` | none; record amended |
| `RTE-4/a1` | `RTE-4` | Determination on the direct-adaptation hand-off, returned as requested by `SCOPE-EPI`: **`non-truth-apt policy/content update`** — concurrence, not correction. `totalThoughts` as a *field* is arguably truth-apt (documented as an "estimate of thoughts needed"), but the *update* applies no evaluator to the estimate's subject matter, consults nothing but the two integers in the current request, and repairs the invariant `totalThoughts >= thoughtNumber` so the stderr header never reads `9/5`. The artifact holds no criterion of "needed"; that criterion lives at `SRC-1:188`, in `EXT-3`'s self-assessment. Scope was not expanded. | `SRC-1:90–92, :75, :170, :188` | none |
| `RTE-9/a1` | `RTE-9`, `OBJ-6` | Fidelity bound on the reshaping. Content is preserved verbatim (`padEnd` pads, never truncates; the border is sized to the payload). But the renderer assumes a **single-line** payload, and multi-line chain-of-thought text — the normal shape — produces a border sized to the whole string and a broken box. The render also drops `nextThoughtNeeded` and `needsMoreThoughts`, and computes its revision/branch caption from unvalidated fields, so `isRevision: "banana"` renders as a revision. Content lineage is preserved; presentational structure and caption reliability are not. | `SRC-1:58–84` with `SRC-1:50` | none |
| `RTE-8/a1` | `RTE-8` | The registered parenthetical "no state rollback needed (nothing was written before validation)" is true about validation but does not support the conclusion. The writes at `SRC-1:94` and `:96–101` precede two further operations **inside the same `try`**: `formatThought` (`:103`) and `JSON.stringify` (`:109`). A throw from either returns `isError: true` with `OBJ-2` and `OBJ-3` already mutated. Practical exposure over stdio is negligible (it needs a pathologically large `thought` to raise `RangeError` from `'─'.repeat(n)`), and the record is filed at that weight. The epistemic consequence is what matters: **an `isError` response does not warrant the proposition "nothing was retained".** *(The lens proposed this as a possible third correction and declined on practical weight; the orchestrator concurs — the parenthetical is imprecise rather than misleading at the scope stated, so it is amended, not corrected.)* | `SRC-1:87–129`, ordering at `:94, :96–101, :103, :109` | the parenthetical's implied scope |
| `OBJ-8/a1` | `OBJ-8` | The artifact's diagnostic propositions are **not uniformly true**. `thought: ""` conforms fully to `OBJ-7` (`{type: "string"}`, no `minLength`) yet fails the falsy guard and is returned `"Invalid thought: must be a string"` — which is false of the input, since `""` is a string. The same pattern makes `"Invalid thoughtNumber: must be a number"` false for `0`, though `0` is excluded by the schema's `minimum: 1` and so reaches `RTE-3` only from a caller bypassing `EXT-2`. Consequence: `RTE-8` warrants reliance on *the fact of rejection* but not on the *stated reason*. **Verified independently by the orchestrator against `SRC-1:32` and `SRC-1:192–195`.** | `SRC-1:32–43` vs `SRC-1:192–209` | none |
| `ABS-3/a1` | `ABS-3` | The absence is accurate and can be **sharpened one stage earlier**: the artifact has no *representable check target* for `CLM-1`'s verification claim. `OBJ-7`'s nine properties contain no hypothesis marker and `ThoughtData` has no such field — while the schema *does* individuate other thought kinds (`isRevision`, `revisesThought`, `branchFromThought`, `branchId`), so the omission is not a general refusal to type thought kinds; hypotheses specifically are unrepresentable. The verification claim therefore fails not merely for want of an evaluator but for want of anything to evaluate, and could not be implemented against the current protocol without a schema change. | `SRC-1:189–234`, `SRC-1:13–23` | none |
| `BAP-4/a1` | `BAP-4` | The registered force "enforcing on argument shape" holds only for the **four required properties**. Server-side, nothing enforces `OBJ-7`'s `minimum: 1` constraints on `thoughtNumber`, `totalThoughts`, `revisesThought`, `branchFromThought`, nor the declared types of the five optional properties, which are `as`-cast and erased at runtime. Those constraints live only in `EXT-2`, which is uninspected. For a caller speaking JSON-RPC directly, `BAP-4`'s enforcing force covers 4 of 9 properties and no value ranges. | `SRC-1:29–56` vs `SRC-1:189–234` | the unqualified "enforcing on argument shape" |
| `CMP-2/a2` | `CMP-2` | Companion to `CMP-2/a1` (tool-name mismatch): a parallel **parameter-name mismatch** inside the same object. The in-prompt parameter documentation names eight of nine parameters in snake_case (`next_thought_needed`, `thought_number`, `total_thoughts`, …) while `OBJ-7` declares and `RTE-3` requires camelCase. `SRC-2:21–29` uses camelCase, so the README agrees with the schema and the in-prompt text does not. Bearing: `CLM-4`'s in-prompt instance ("You can adjust `total_thoughts` up or down") names a parameter the schema will not accept. Force is weak — a capable consumer follows the schema — and it is recorded at that weight. | `SRC-1:149, 168–175` vs `SRC-1:189–234` | none |
| `CLM-1/a1` | `CLM-1` | `CLM-1` conflated two claim instances with the same propositional content but different consumer, channel, and horizon. Split into `CLM-1a` (README channel, human operator, installation decision) and `CLM-1b` (prompt channel, `EXT-3`, session). Only `CLM-1b` can induce in-session reliance on a verification that does not occur. `CLM-1` is retained as the shared propositional content so existing citations remain valid. | `SRC-2:12` vs `SRC-1:154–157`, delivery at `SRC-1:251–253` | the single-instance framing |
| `OBJ-5/c1` | `OBJ-5` | **Correction, not amendment.** `OBJ-5` was registered as "54 lines of instruction addressed to the model in the second person" — misclassified by the very criterion the record states. `SRC-1:135–146` is third-person description; `:148–157` switches subject mid-list, items 6–9 dropping the subject to assert what the tool does; only `:177–188` is the numbered second-person block. Classifying the whole object as directive would have made its assertive content invisible, and licensed the conclusion that `OBJ-5` cannot mislead because instructions have no truth value. It can. Remedy: split into `OBJ-11`/`OBJ-12`, narrow `BAP-1`, register `BAP-6`. | `SRC-1:135–188`, contrast `:154–157` with `:184–187` | "54 lines of instruction … in the second person" |

## Record 5 — Runtime account

Scheduling, context assembly, and external state/action are treated as causal responsibilities, not module boundaries. In this artifact one of the three is almost entirely absent, and saying where it went is the main runtime finding.

### Material loops

A loop is material when it alters the analysis question, a control path, evidence strength, or a lens result.

#### `LOOP-A` — protocol serve loop (partly external)

| field | value |
|---|---|
| trigger/input | process launch by `EXT-2` (`npx -y @modelcontextprotocol/server-sequential-thinking`, `SRC-2:47–58`), then JSON-RPC messages on stdin |
| next-step owner | `EXT-1`'s transport and dispatcher — **uninspected** |
| decision policy and form | method-schema → handler map, populated by two `setRequestHandler` calls (`SRC-1:251,255`); symbolic, static, exhaustive at two entries |
| context selection and framing | none; `RTE-1` returns the single tool spec verbatim with no filtering or parameterization |
| state reads and writes | none at this level |
| action executor and boundary | process-local only: stdout for protocol, stderr for `OBJ-6` and the startup banner (`SRC-1:272`). No filesystem, network, or subprocess access anywhere (`ABS-1`) |
| persistence | none |
| coordination and return | single-process, single-transport, request/response; no concurrency control, no queue |
| retry / cancellation / recovery | **none implemented in the boundary.** No cancellation handling, no reconnect, no signal handler, no graceful shutdown. A fatal transport error exits the process (`RTE-10`, `BAP-5`). Any retry lives in `EXT-2`. |
| output | tool list, or a tool result |
| evidence | `SRC-1:237–278`; `EXT-1` internals uninspected |

#### `LOOP-B` — per-call thought-processing loop (fully inside the boundary)

| field | value |
|---|---|
| trigger/input | a `CallTool` request whose `params.name === "sequentialthinking"` (`SRC-1:256`) |
| next-step owner | `CMP-1.processThought`; returns synchronously, owns nothing after return |
| decision policy and form | straight-line procedure with three conditionals — validity (`RTE-3`), overflow coercion (`RTE-4`), branch-bucket eligibility (`RTE-6`). Symbolic, fully determined by the request; no model call, no configuration, no randomness |
| context selection and framing | **none.** The artifact selects nothing into anyone's context. It emits `OBJ-4`, a fixed five-field shape computed the same way on every call |
| state reads and writes | writes: `OBJ-2` always (`RTE-5`), `OBJ-3` conditionally (`RTE-6`), and a mutation of the incoming `OBJ-1` (`RTE-4`). Reads: `OBJ-2.length` and `Object.keys(OBJ-3)` only (`ABS-2`) |
| action executor and boundary | no external action. `RTE-9` writes to stderr; that is the only side effect leaving the process besides the protocol response |
| persistence | in-memory, process lifetime, unbounded growth, no eviction (`ABS-1`, `RTE-5`) |
| coordination and return | one JSON text block; `nextThoughtNeeded` is passed through unchanged — the artifact expresses no opinion about continuation (`ABS-10`) |
| retry / cancellation / recovery | one try/catch converting any throw into `OBJ-8` with `isError: true` (`RTE-8`). No retry, no compensation. Failure is total for the call and invisible to retained state |
| output | `OBJ-4` on success, `OBJ-8` on failure, plus `OBJ-6` on stderr on success only |
| evidence | `SRC-1:86–130` |

#### `LOOP-C` — the advertised thinking loop (crossing loop; declared partial)

| field | value |
|---|---|
| trigger/input | `EXT-3` decides a problem warrants structured thinking |
| next-step owner | **`EXT-3`, outside the boundary.** This is the finding: the artifact holds no scheduling responsibility for the loop it is named after (`ABS-10`) |
| decision policy and form | `OBJ-5` — 54 lines of natural language, delivered once through `BAP-1`. Representational form is natural-language instruction; its force is directive in tone and unenforceable in fact |
| context selection and framing | `EXT-2`'s transcript carries the prior `thought` strings, because the model wrote them into its own turns. The artifact contributes only `OBJ-4` (`BAP-2`) |
| state reads and writes | the artifact's writes (`OBJ-2`, `OBJ-3`) are invisible to this loop except through the two derived values in `OBJ-4` |
| action executor and boundary | `EXT-3`/`EXT-2` |
| persistence | the host transcript, outside the boundary |
| coordination and return | iteration is the caller repeating `LOOP-B`; the artifact neither counts down nor terminates it |
| retry / cancellation / recovery | entirely `EXT-2`'s |
| output | whatever answer `EXT-3` produces |
| evidence | doctrine only for the loop's existence (`CLM-1`–`CLM-7`); the artifact-side half is implementation-grounded |
| limitation | Boundary kind `complete artifact, partial loop`: no conclusion in this run describes the behavior `LOOP-C` produces. |

### Anti-conflation checks (step 4.3)

- **A filesystem is not a scheduler** — and here neither exists. `OBJ-2` is an in-memory array; the absence of a scheduler is recorded as `ABS-10`, not inferred from the presence of storage.
- **Retaining material is not selecting it into context** — `RTE-5`/`RTE-6` retain; nothing selects. The gap between them is `ABS-2` and is the central runtime fact about this artifact.
- **A tool schema present in context is not tool execution** — `RTE-1` places `OBJ-5`/`OBJ-7` in a host's tool list. That is presence. Execution is `RTE-2`, and no evidence in this register shows either occurring in a real session (`ABS-4`).

### Conditional surface inspection (step 4.4)

Included only where materially altering the analysis question, a control path, evidence strength, or a lens result:

- **Observability** (material: it is the only consumer-facing output besides the protocol response, and it is the *only* place a retained thought's content ever leaves the process). `RTE-9`/`OBJ-6` renders each thought to stderr with a revision/branch label. It has no in-boundary consumer (`BAP-3`). Consequence for the lenses: content leaves via a channel the model never reads, which sharpens the read-back finding rather than softening it.
- **Packaging/distribution** (material: it fixes what "the system" is, and it carries two defects that bear on doctrine–implementation agreement). `CMP-6`, with amendments `CMP-3/a1` (version disagreement) and `CMP-6/a1` (unused `yargs`).
- **Permissions and governance** — inspected and found to have no surface: the artifact requests no capabilities beyond `tools: {}` (`SRC-1:243–245`), touches no resource outside its process, and applies no authorization to callers. Recorded because a reader would otherwise wonder; not developed further, as it alters no lens result beyond confirming `ABS-1`.
- Providers, user interface, and performance were **not** inspected: no provider integration exists, there is no UI, and no performance evidence exists in the register (`ABS-4`). Their omission prevents no conclusion this run makes.

---

## Notes for lens workers

- Cite by the IDs above. Do **not** rename or re-inventory a registered object or route.
- Propose new records under a lens-local tag (`MEM-n`, `EPI-n`) and state each proposal's identity (file path, symbol, route endpoints) so the orchestrator can register it canonically.
- If you find a registered record defective — false, misclassified by its own stated criterion, or accurate but misleading at the scope stated — return the correction with its evidence anchor instead of re-inventorying.
- You may make targeted reads inside the frozen boundary (the four files under `/home/zby/llm/servers/src/sequentialthinking/` plus the root manifests named in `SRC-5`/`SRC-6`), read-only. Report any read you made so it can be added centrally. Do not fetch, pull, refresh, or widen sources.
- Do not decide publication. Do not assign a system-wide grade.
