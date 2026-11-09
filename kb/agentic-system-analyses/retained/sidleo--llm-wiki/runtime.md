---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "llm-wiki runtime baseline: five host entry paths, bundle retrieval, write admission, rule delivery and synchronization at the frozen revision."
run-id: AAS-2026-11-08-llm-wiki-97b740596442-01
reviewed-boundary: f70e680d852a78d48504425d87252531e68c5624
---

# llm-wiki runtime report

## Runtime account

### What performs the work

llm-wiki is a file-backed knowledge service plus host-facing guidance, not an enclosing model runner. Its shipped work is to expose a Markdown bundle for listing, keyword search, concept retrieval with backlinks, creation and revision, rule delivery, diagnostics and synchronization. The external agent decides when to invoke these operations and what to write; Node code handles parsing, selection, filesystem changes and transport. The skill explicitly limits its own control over the host (SRC-1, `packages/skill/SKILL.md`):

> 本 skill 只在宿主加载它时才生效，
> 宿主是否加载、加载后会不会真去查库，不由我们决定。
> --- `packages/skill/SKILL.md`

The decision policy combines executable JavaScript and natural-language guidance. The latter requests rules→list→search→get→create use and active recording after discovering missing knowledge or pitfalls. It does not enforce that ordering. See [RT-RTE-bundle-read](#rt-rte-bundle-read), [RT-RTE-concept-create](#rt-rte-concept-create) and [RT-BAP-rule-delivery](#rt-bap-rule-delivery). No target-selected model or provider version is established by these paths. Model parameters, endpoint mutability, grants and execution isolation belong to the excluded hosts; their values are uninspected, not fixed by llm-wiki. The inspected core performs these operations without a model call; semantic synthesis is assigned to its caller (SRC-1, `packages/core/index.mjs`, `packages/core/lib/ingest.mjs`). No distributed-parametric component is declared as an internal executor of these routes.

All findings below concern implementation or doctrine/design under SRC-1. No target execution, test run, supplied operational trace or experiment was used. Wired delivery does not establish activation, compliance, retrieval quality or benefit.

### Shipped entry paths and identity scopes

| Form | Entry and next-step owner | State, delivery and return |
|---|---|---|
| Skill/CLI | The host loads `packages/skill/SKILL.md` and invokes `packages/skill/bin/wiki.mjs`; `main` dispatches subcommands. | Each command resolves a bundle using arguments/environment/registry. CLI stdout is data for the shell caller; explicit usage/not-found/confirmation failures exit nonzero. Rules can be requested explicitly and are appended to get/create/update output. |
| DSH | `packages/dsh/wiki.mjs` exports `apply`, registers tools, prompt assembly, management HTTP routes and autosync lifecycle callbacks. | A WeakMap stores bundle overrides per agent; a no-agent path uses shared plain state. Global bundle resolution and context snapshots have TTL caches. The host owns tool scheduling and consumption of returned text. |
| pi | `packages/pi/extensions/index.ts` default export registers tools and `before_agent_start`. | Tool calls resolve a bundle; each prompt hook reads APPEND files afresh and appends their text to the provided system prompt. Failures quietly leave that turn without this addition. |
| MCP | `packages/mcp/lib/server.mjs` builds the server and tools; `packages/mcp/lib/core.mjs` loads core. | Tools use a process-level bundle override, not a per-user authentication identity. Initialize instructions are assembled once; subsequent tool calls can obtain current context/rules. Tools return text content. |
| Codex | `packages/codex/bin/wiki-mcp.mjs` implements stdio JSON-RPC using its own local tools; `packages/codex/hooks/inject-context.mjs` adds context. | The transport serializes incoming lines through a promise chain. The hook hashes rendered context per session ID, emits additionalContext on SessionStart or changed text, and suppresses unchanged submissions. Hook failures exit successfully without context. |

Evidence: SRC-1, `packages/skill/bin/wiki.mjs`, `packages/dsh/wiki.mjs`, `packages/pi/extensions/index.ts`, `packages/mcp/lib/server.mjs`, `packages/mcp/lib/tools.mjs`, `packages/codex/bin/wiki-mcp.mjs`, `packages/codex/hooks/inject-context.mjs`.

The actual load paths matter. DSH, pi, MCP and Codex prefer package-local vendor-core, with repository core fallbacks; CLI tries bundled wiki-core, repository core and then an npm import. A read-only byte comparison at the frozen checkout found the four vendor copies equal to core for `index.mjs` and `lib/write.mjs`, `lib/rules.mjs`, `lib/bundle.mjs`, `lib/search.mjs`, `lib/ingest.mjs`, `lib/git.mjs`, `lib/feishu.mjs`. Codex's `lib/tools.mjs` and `lib/instructions.mjs` equal MCP's copies. This supports the specific shared-core traces below, not installed npm parity or universal adapter equivalence. Adapter differences remain material; see [RT-CLM-form-equivalence](#rt-clm-form-equivalence).

### Ordinary invocation, end to end

An ordinary skill-assisted retrieval starts when the user asks a domain question. The external host interprets the skill and chooses commands. `wiki rules` loads behavior rules, `wiki list` exposes directory overviews, `wiki search QUERY` builds a graph from disk and returns scored matches, and `wiki get ID` resolves an ID/title/prefix and returns body plus backlinks. The host interprets that output and answers or acts with its own tools; llm-wiki does not execute the domain task (SRC-1, `packages/skill/SKILL.md`, `packages/skill/bin/wiki.mjs`, `packages/core/lib/search.mjs`). This is an inspectable path, not an observed session.

The principal is the invoking host/user; concept identity is the bundle-relative Markdown path. The CLI resolves the root before dispatch. Core recursively scans nonhidden Markdown files except reserved names, parses frontmatter and links, and derives forward/back indexes. Search selects by textual matching and scores, with type/tag filters and a result limit; no embedding or model ranking is required by this implementation. Get prefers exact ID, ID without .md, unique exact title, then unique prefix. Ambiguous exact titles return candidates; missing or ambiguous CLI get terminates with an error rather than fabricating a concept. Graphs are rebuilt from files, so later invocations can read changes without a separate ingestion index service. Details and retained-content boundaries are in [RT-RTE-bundle-read](#rt-rte-bundle-read).

If the agent discovers missing knowledge, it supplies a proposed ID/type/body to create. The caller checks directory gates, then core checks the create ID/type/existence, serializes frontmatter/body, writes the file, and updates log/index. Confirmation is a caller-supplied flag, not an authenticated approval exchange. A successful local write may be followed by an unsuccessful online flush; the returned status distinguishes them. Existing concepts use a separate update route. Memory revisions and semantic curation are left to the memory member; this report establishes the admission and effect boundaries (SRC-1, `packages/skill/bin/wiki.mjs`, `packages/core/lib/write.mjs`).

### Four forcing cases and what they delimit

1. **Create with and without confirmation.** The nearest AGENTS.md gate section replaces the parent's type list; no section means automatic recording. A named type match and missing confirmation block the adapter's create call. Supplied `--confirmed`/`confirmed:true` allows it and requests verified metadata. The software does not inspect a human consent record. This is a protocol between host and user, not proof of approval. See [RT-RTE-concept-create](#rt-rte-concept-create).
2. **Update or ingest instead of gated create.** Supported update inputs include type/body changes. CLI, DSH, pi and MCP update bodies reach core without consulting gateForType; the core does not impose that gate. Ingest calls core create directly for a Reference. Therefore a create gate is not a universal per-content write gate. This conclusion does not require malformed arguments or a hypothetical shell bypass. See [RT-RTE-concept-update](#rt-rte-concept-update) and [RT-RTE-source-ingest](#rt-rte-source-ingest).
3. **Fresh rules versus static/truncated context.** pi rereads APPEND on the hook; DSH may reuse a TTL snapshot; MCP initialize instructions do not refresh automatically; Codex's hook emits only changed text except SessionStart. DSH/MCP/Codex context builders cap text and may omit trailing rule material; CLI compact appendices omit AGENTS text outside the gate section. Thus delivery is not identical or complete under all forms. Direct wiki_rules reload is an alternate path, not evidence it is used. See [RT-RTE-context-delivery](#rt-rte-context-delivery).
4. **Local mutation versus remote conflict and explicit deletion.** MCP/DSH/CLI updates consult the Feishu write guard, but their wrapper catches guard exceptions and permits local writing; pi update does not call that guard. Flush can subsequently report conflict and leave a changed local cache. The ordinary no-deletion synchronization policy does not cover the explicit Feishu delete operation, whose `apply:true` branch performs irreversible deletes. See [RT-RTE-remote-sync](#rt-rte-remote-sync).

These cases challenge the broad readings of human approval, form equivalence, complete rule delivery and safe synchronization. Provider-native tools, shell access outside CLI, arbitrary host extensions and remote model workers remain host capabilities, not llm-wiki-enforced alternate model paths. Direct file editing and migration are genuine alternate bundle producers, however. The exported core is also callable without adapters. These paths are not covered by adapter confirmation checks (SRC-1, `packages/core/index.mjs`, `packages/core/lib/write.mjs`, `scripts/migrate.mjs`).

### Guarantees, grants and recovery

The **create confirmation check** is owned by adapter code; implementation conclusion status: wired; operation conclusion status: uninspected; guarantee strength: protocol. It covers configured type matches through those create handlers. It requires a host that truthfully associates the flag with user approval. It does not cover core callers, update, source registration, migration or direct filesystem edits. A human can veto through the cooperating host before invocation, but the flag itself is supplied by the caller.

The **rule channel** is owned jointly by target-side hooks/builders and the external host. Implementation conclusion status: wired; operation conclusion status: uninspected; guarantee strength: best effort. It covers emitted text, subject to cache, truncation and error fallback. Prompt precedence, receipt by a particular model and obedience require external host/model contracts not frozen here. Natural-language instructions cannot establish their own enforcement.

The **online write/sync controls** are owned by core and adapter wrappers. Implementation conclusion status: wired; operation conclusion status: uninspected; guarantee strength: best effort. Feishu conflict classification gates selected writes/syncs, but caller differences and exception fallback prevent a universal prewrite exclusion. Git synchronization retains local commits before fetch/merge and uses ordinary push arguments. Feishu deletion is a separate, explicitly admitted effect, not covered by ordinary sync's no-delete claim. Neither backend supplies a demonstrated distributed transaction or successful remote operation here (SRC-1, `packages/core/lib/git.mjs`, `packages/core/lib/feishu.mjs`).

The capability surface includes filesystem read/write, Git subprocesses, lark-cli remote operations, registry changes and DSH management endpoints/timers. That is distinct from actual grants: available paths, credentials, host approvals and deployed network/isolation settings are not supplied. The code relies on the Node process and external Git/lark identities, not a demonstrated sandbox. Producer names and human strings are provenance labels, not authorization identities. Core writes occur before log/index maintenance and are not wrapped in a transaction; later failure can leave a durable file despite incomplete derived maintenance. Index refresh, retry and remote conflict guidance are recovery affordances, not observed recovery outcomes (SRC-1, `packages/core/lib/write.mjs`, `packages/core/lib/git.mjs`, `packages/core/lib/feishu.mjs`).

### Additional inspected coverage and limits

Beyond the boundary's initial reads, this member inspected complete core rules/search/ingest modules, MCP server/instructions/core loader, Codex core loader/context hook and stdio dispatch; selected full handler regions in CLI/DSH/pi/MCP; Git sync; Feishu sync, write guard, flush and delete; DSH autosync scheduling; and source searches over migration/smoke files. These supply implementation and attributed design only. Vendor comparison was limited to the files named above. Remaining validation, migrations, packaging/UI details, exhaustive Feishu push/pull/adopt branches and evaluations are not certified by this runtime account. No statement of universal sync safety, schema conformance, successful migration, model correctness or theory-building follows from these reads. The shipped migration file writes and evaluation assertions establish alternate producers/test expectations, not successful runs (SRC-1, `scripts/migrate.mjs`, `scripts/migrate-to-feishu.mjs`, `scripts/smoke-test.mjs`).

## Shared records

### Components

#### RT-CMP-core
Label: llm-wiki core

Source-native identity: `packages/core/index.mjs` and its imported modules. Representational form: symbolic JavaScript; storage substrate: package files, including adapter vendor-core copies. It exports deterministic bundle operations, rules, diagnostics, registry and online backends. The host's model, if any, is outside this component; no internal weights/version mutation is attributed. SRC-1, `packages/core/index.mjs`:

> export { createConcept, updateConcept, deprecateDir, nowIso, checkId } from './lib/write.mjs'
> export { ingestSource } from './lib/ingest.mjs'
> --- `packages/core/index.mjs`

### Operative objects

#### RT-OBJ-agents
Label: AGENTS.md gate declaration

Source-native identity: per-directory AGENTS.md. The parsed gate section is natural-language source consumed through a symbolic extractor/type-list comparison; filesystem Markdown is the substrate. Other prose in the file remains host-interpreted guidance, not an executable veto. Nearest ancestor with a gate declaration wins. SRC-1, `packages/core/lib/rules.mjs`:

> if (decl) {
>       return { needConfirm: decl.needConfirm.includes(type), via: rules[i].path }
>     }
> --- `packages/core/lib/rules.mjs`

#### RT-OBJ-append-system-prompt
Label: APPEND_SYSTEM_PROMPT.md

Source-native identity: reserved per-directory APPEND_SYSTEM_PROMPT.md files, distinct from concepts. Representational form: natural-language behavior instructions; substrate: Markdown files. Consumers are context builders and host/model prompt interpretation. Root plus all nonhidden subdirectories are collected for broad injection; directory-specific retrieval uses an ancestor chain. Text delivery alone proves no behavior change. SRC-1, `packages/core/lib/bundle.mjs`, `packages/core/lib/rules.mjs`:

> out.sort((a, b) => (a.dir === b.dir ? 0 : a.dir === '' ? -1 : b.dir === '' ? 1 : a.dir < b.dir ? -1 : 1))
> --- `packages/core/lib/bundle.mjs`

### Routes

#### RT-RTE-bundle-read
Label: Bundle list search get

Endpoints/progression: external host or CLI caller → bundle resolution → graph reconstruction → list/search/get → text response → external host. Owner: caller selects commands; code performs lexical selection and link derivation. State: Markdown files, in-memory graph and per-adapter bundle choice. Action effects: read-only retrieval, not domain-task execution. Guidance requests overview first, but get is independently callable. Operating mode: open requests, not a bounded experiment. The search score is a retrieval heuristic, not an answer oracle; no expected-answer provider governs ordinary calls. SRC-1, `packages/core/lib/bundle.mjs`, `packages/core/lib/search.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: concept summaries for search/list; get returns parsed concept body, metadata and graph-derived backlinks/outlinks before adapter formatting.
- Later read-back: changes persisted in bundle files can enter a later graph build and retrieval; static shipped examples alone are not evidence of accumulation.
- Delegated visibility: inapplicable — no target-side subagent frame is created; the requesting host receives text.
- Selection predicate: nonhidden nonreserved .md scan; search matches token alternatives with type/tag filters and score limit; get resolves exact ID, stripped extension, unique title or unique prefix.
- Invalidation or expiry: graph reconstructed per call; this code does not remove deprecated concepts from unfiltered results.
- Activation or effect: wired delivery to caller; use in the eventual answer is unobserved.
- Evidence limits: no retrieval benchmark or observed domain answer; selected metadata fields are indexed, not arbitrary frontmatter despite the broad module comment.

> if (graph.nodes.has(want)) return compose(graph, want)
> --- `packages/core/lib/search.mjs`

> const top = results.slice(0, limit)
> --- `packages/core/lib/search.mjs`

#### RT-RTE-concept-create
Label: Gated concept creation

Endpoints/progression: caller proposes path/type/body → adapter parses nearest gate → refusal or core create → local file → log/index → optional flush → response. Owner: computational caller proposes and supplies confirmation; code tests the flag/type list; a human veto is mediated by the external caller, not directly authenticated. Mode: open knowledge recording. No answer oracle checks truth. Guidance: directory gate specifies types requiring human confirmation; skill asks agents to display proposals first. Admission: core checks create ID/type/existence, then writes; no mandatory validate/lint pass is called. Rollback: no transactional undo in create; retry can encounter an already-existing concept. SRC-1, `packages/skill/bin/wiki.mjs`, `packages/mcp/lib/tools.mjs`, `packages/dsh/wiki.mjs`, `packages/pi/extensions/index.ts`, `packages/core/lib/write.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: created ID/path text, or confirmation/error text; CLI confirmation rejection exits 2.
- Later read-back: created Markdown enters subsequent graph scans; generated and optional verified labels persist in frontmatter.
- Delegated visibility: inapplicable — caller-mediated proposal, no internal delegated worker.
- Selection predicate: nearest AGENTS gate section's exact type membership; otherwise automatic recording; confirmation supplied by caller.
- Invalidation or expiry: existing-file check rejects another creation at that path; no automatic content expiry or approval expiry enforced here.
- Activation or effect: local file write plus navigation/log maintenance; successful remote publication and later model use unobserved.
- Evidence limits: a supplied confirmation flag is not proof that a human approved content; core exports permit callers without this adapter gate.

> if (gate.needConfirm && !has(rest, '--confirmed')) {
> --- `packages/skill/bin/wiki.mjs`

> await writeFile(file, text)
>
>   if (p.opts?.logAction !== false) {
> --- `packages/core/lib/write.mjs`

#### RT-RTE-concept-update
Label: Existing concept mutation

Endpoints/progression: supported update request → core read/parse/merge/write → log/index → adapter flush/return. Caller proposes and selects all changed values; core rejects missing files or missing frontmatter but does not consult directory confirmation rules. CLI/DSH/MCP may reject a Feishu conflict before calling core; pi's inspected update handler calls core directly. Mode: open revision requests, no truth oracle. Human control over content is not established by invocation alone. Admission is executable field merge with optional confirmation metadata, not mandatory human approval. Recovery: no atomic file-plus-log transaction; deprecated status is reversible by later editing. SRC-1, `packages/core/lib/write.mjs`, `packages/skill/bin/wiki.mjs`, `packages/dsh/wiki.mjs`, `packages/pi/extensions/index.ts`, `packages/mcp/lib/tools.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: update status and optional remote flush status; errors become caller-visible text or CLI failures.
- Later read-back: merged metadata/body persists and can be read by later invocations.
- Delegated visibility: inapplicable — host calls this route directly.
- Selection predicate: caller-supplied existing ID and supplied fields; type changes are a supported input, not merely a core-private possibility.
- Invalidation or expiry: omitted fields retained; generated metadata refreshed; unconfirmed updates do not automatically remove prior verified entries.
- Activation or effect: local concept overwrite; downstream behavioral dependence unobserved.
- Evidence limits: write admission is not correctness validation; retained verification labels must not be interpreted as fresh approval of every revision.

> const next = { ...oldMeta }
> --- `packages/core/lib/write.mjs`

> const body = p.body !== undefined ? p.body : oldBody
>   const outText = serializeDoc({ meta: next, body })
>   await writeFile(file, outText)
> --- `packages/core/lib/write.mjs`

#### RT-RTE-source-ingest
Label: Raw source registration

Endpoints/progression: explicit caller source path → copy into references (or supplied refDir) if absent → optional Reference concept → log/index → return. Owner: caller selects source; core registers deterministically. Mode: open registration; no answer oracle. Core creates the Reference without calling gateForType or receiving a confirmed option; a configured Reference create gate is therefore not universal across source registration. This is distinct from later agent synthesis. Proposed change is source copy and minimal derived Reference description/first line; no content approval exchange occurs inside ingest. Existing destination is retained; no transactional rollback of copy and concept/log writes. SRC-1, `packages/core/lib/ingest.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reference path, existed flag and source concept ID in core; CLI formats registration status.
- Later read-back: copied source and generated Reference remain on disk; later model interpretation or synthesis requires a caller read.
- Delegated visibility: inapplicable — semantic synthesis is assigned to the caller, not an internal worker.
- Selection predicate: explicit source; basename sanitization, default references directory, existing concept/destination checks.
- Invalidation or expiry: existing destination not recopied; no freshness reconciliation of changed source implemented in this routine.
- Activation or effect: copy and Reference write; not automatic extraction of validated domain knowledge.
- Evidence limits: no observed successful ingest or downstream synthesis; binary fallback and first-line excerpt are not semantic validation.

> await copyFile(p.source, dest)
> --- `packages/core/lib/ingest.mjs`

> opts: { producer: ingestOpts?.producer || 'llm-wiki', version: ingestOpts?.version || '0.1.0', logAction: false },
> --- `packages/core/lib/ingest.mjs`

#### RT-RTE-context-delivery
Label: Rules into host context

Endpoints/progression: host lifecycle/initialize request or explicit rules command → bundle resolution → APPEND collection/rule-chain read → formatted text → host channel. Owner: target code chooses what to send; external host determines prompt placement and model invocation. Context/state: static skill guidance, retained bundle rule text, optional snapshot/TTL or session-hash state. Decision policy is symbolic triggering and natural-language instruction interpretation. DSH supplies a constant assembly section and runtime context with interpolation disabled; pi returns an amended systemPrompt; MCP provides initialize instructions; Codex hook emits additionalContext. CLI carries full APPEND chain plus only AGENTS gate sections on get/create/update. SRC-1, `packages/dsh/wiki.mjs`, `packages/pi/extensions/index.ts`, `packages/mcp/lib/instructions.mjs`, `packages/codex/hooks/inject-context.mjs`, `packages/core/lib/rules.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook/context/instructions text or CLI rules/appendix text; errors can silently omit it.
- Later read-back: edited retained APPEND files can reach a later prompt assembly, reconnection, changed Codex submission or explicit rules call; reload cadence differs by adapter.
- Delegated visibility: inapplicable — no target-side isolated model frame or subagent return channel.
- Selection predicate: broad injection collects root and all nonhidden directory APPEND files; scoped rule calls select root-to-directory ancestors; compact CLI appendix selects only gate sections from AGENTS.
- Invalidation or expiry: pi rereads per hook; DSH TTL/epoch cache; MCP instructions static after construction; Codex digest suppresses unchanged text except SessionStart; direct rules calls provide reload.
- Activation or effect: delivery-capable channel, not demonstrated model adherence; no context trimming or summarization of host turns is implemented by these inspected hooks.
- Evidence limits: context builders may truncate; errors can suppress delivery; external host compaction, precedence and subsequent model choices uninspected.

> if (text.length > maxChars) text = text.slice(0, maxChars) + '\n…（instructions 超限截断）'
> --- `packages/mcp/lib/instructions.mjs`

> const force = eventName === 'SessionStart'
> --- `packages/codex/hooks/inject-context.mjs`

> if ((await readFile(stateFile, 'utf8')).trim() === digest) return
> --- `packages/codex/hooks/inject-context.mjs`

These controls select external knowledge and suppress repeated injections; they do not establish removal of prior messages from the host's window. The frame analogy is inapplicable to these hooks because they create no separate model context. Reload works by new file reads and by-value text delivery, not dereferencing a live pointer inside model context.

#### RT-RTE-remote-sync
Label: Remote bundle maintenance

Endpoints/progression: explicit sync request or enabled DSH timer → selected Git/Feishu backend → external process/service → local/remote file changes → status. DSH HTTP management routes and CLI also admit bundle registration, clone/init and explicit Feishu delete; these are not necessarily foreground-model choices. Owner: caller/configuration chooses backend, identity and options; software classifies changes and executes operations; external credentials and services decide actual remote access. Mode: open maintenance plus configured periodic synchronization, not an experimental improvement curriculum. No answer oracle judges knowledge truth. Admission compares filesystem/history/ledger changes, not semantic quality. Guidance describes no-force Git and no-delete ordinary sync, but explicit deletion is separately available. SRC-1, `packages/core/lib/git.mjs`, `packages/core/lib/feishu.mjs`, `packages/dsh/wiki.mjs`, `packages/mcp/lib/tools.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: structured core status/steps/conflicts then adapter text; successful local mutation can coexist with publication failure.
- Later read-back: remote changes pulled into bundle files become eligible for later graph/context reads; registry changes alter later bundle resolution.
- Delegated visibility: external git/lark-cli subprocesses receive operation arguments; no model-worker delegation is implemented here.
- Selection predicate: backend by resolved bundle kind; Git history/merge status; Feishu local/remote/ledger differences; explicit delete paths and apply flag; DSH autosync selects enabled due Feishu bundles.
- Invalidation or expiry: autosync running markers, due interval and last-tick map coordinate scheduling; successful DSH sync invalidates context caches; no universal distributed lock or transaction established.
- Activation or effect: local and remote mutations, index reconstruction, log merge and possible explicit deletion; live successful service effects unobserved.
- Evidence limits: exhaustive push/pull/adopt option coverage not established; status snapshots do not prove race freedom; host and remote credentials/deployments absent.

Git commits local changes before fetch, fast-forwards or merges remote history, aborts its attempted merge on concept/config conflicts, regenerates index, then pushes normally. Rejected push returns retry guidance, not force. External Git hooks can affect command success. Feishu sync rejects nonderived conflicts, treats index as derived and unions logs when readable; unreadable remote log conflict falls back to local push. Manual repair, retry or external backup/Git history provides recovery; explicit delete stops at first irreversible failure and does not undo earlier deletions.

> const add = await run(root, ['add', '-A', '.'], opts)
> --- `packages/core/lib/git.mjs:234-234`

> const conceptConflicts = before.conflict.filter((c) => !derived(c.rel))
> --- `packages/core/lib/feishu.mjs`

> steps.push('log.md 为两侧改动但远端内容不可读：以本地为准推送')
> --- `packages/core/lib/feishu.mjs`

> if (opts.apply !== true) {
> --- `packages/core/lib/feishu.mjs`

> const r = unwrap(await runLark(['drive', '+delete', '--file-token', p.fileToken, '--type', 'file', '--yes', '--format', 'json', ...id.as], opts))
> --- `packages/core/lib/feishu.mjs`

Automatic sync is evidence-responsive file reconciliation, not demonstrated improvement of model capacity or knowledge truth. The timer records outcomes for scheduling/status; that alone is not trace-fed semantic revision or self-improvement.

### Claims

#### RT-CLM-form-equivalence
Label: Common bundle equivalence claim

Claimed operation: all five forms share the same bundle and behavior. Source: SRC-1, `README.md`.

> All five forms read and write **the same bundle** with identical behavior — they reuse `packages/core`, no duplicated implementation.
> --- `README.md`

The selected vendor files are byte-identical, supporting common core semantics. Complete behavior equivalence is not established: prompt cadence/channels differ, CLI appends rules differently, and pi's inspected update omits the prewrite Feishu guard found in other adapters. The claim is doctrine/design, not an observed equivalence result.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-rule-delivery
Label: Retained rules to host behavior

Consumer: external host/model and, for parsed AGENTS gate sections, adapter create code. Channel: systemPrompt/runtime context/initialize instructions/additionalContext, explicit rules text or CLI appendix; symbolic gateForType result for create. Force: natural-language guidance for model behavior; executable conditional refusal for configured create types. Horizon: later host turns/sessions while files and bundle selection persist, subject to each reload cadence. Route links: [RT-RTE-context-delivery](#rt-rte-context-delivery), [RT-RTE-concept-create](#rt-rte-concept-create).

SRC-1, `packages/pi/extensions/index.ts`, provides a concrete retained-text channel:

> return { systemPrompt: `${base}\n\n${text}` };
> --- `packages/pi/extensions/index.ts`

This establishes a target-side authority channel, not exercised compliance or a self-improvement result. Rule edits can change subsequently delivered instructions; what caused an edit and whether later behavior depends on it are unobserved. No product-weight update or autonomous theory-builder conclusion is inferred from editable instructions.

## Annotations

none
