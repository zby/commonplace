---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Arsumbris runtime baseline: documented typed-graph, host and agent routes plus the implemented device-config seeder at the frozen entry-repository boundary."
run-id: AAS-2026-10-15-arsumbris-a9be6bac297f-01
reviewed-boundary: "716bb14f2bf50e249d414525c8e07c50478fc786"
---

# Arsumbris runtime report

## Runtime account

### Evidence and claimed work

Arsumbris declares an IDE in which Markdown/YAML repositories become a typed live graph, consumed by UI projections and agent tools. Its entry repository contains descriptions of those consumers, not their implementations. This account follows the boundary's `complete artifact, partial loop` scope. All findings below use SRC-1 at the frozen revision. `README.md`, `INSTALL.md`, `au-engine.md`, `au-host.md`, `au-mcp.md`, `SAFETY.md`, `MIGRATION.md` and `VERSION.md` supply doctrine/design or attributed operation; only `scripts/seed-device-config.py` supplies executable implementation. No runtime, installer, test or example was run, and no supplied trace establishes activation or benefit. Source coverage here stays within the boundary's already registered textual scope.

The claimed consequential work is shared knowledge editing with structural diagnostics, agent-facing guidance and extensible tools, rather than model inference itself. SRC-1, `README.md` states:

> The engine reads them as one typed graph, checks fields and references and gives agents diagnostics they can act on.
> --- `README.md`

The declared architecture separates facts (engine), interaction (host), and agent governance (MCP layer). It does not identify a deployed model, provider call, inference configuration or model version. [RT-CMP-agent-harness](#rt-cmp-agent-harness) preserves that unresolved distributed-parametric dependency; the harness owns next-step model decisions, not the graph daemon.

### Ordinary documented invocation and shipped entry paths

The concrete shipped entry is the README's installation prompt followed by `INSTALL.md`: acquire sibling repositories, build the engine, install JS dependencies, build host/projections, seed local configuration, then hand GUI launch to the user. The installer agent is explicitly told not to launch the long-running desktop app. Bootstrap is recorded in [RT-RTE-device-seeding](#rt-rte-device-seeding). It produces device registries, not a knowledge graph or an agent answer. The subsequent launcher reads configuration before an engine exists, offers a template, materializes a workspace and starts its engine. The host supervises that daemon and opens a composition; the separate agent adapter connects the optional harness. These later steps are documentary contracts, not verified consumers of the seeder's files (SRC-1, `INSTALL.md`, `au-host.md`).

A representative ordinary agent request is a file overwrite after a read. This is a reconstruction from the documented tool/hook examples, not an observed run. A user supplies work through a harness; the harness's foreground agent selects a typed tool. The adapter maps harness lifecycle hooks to the workspace's MCP daemon. An agent-profile resolves daemon-side tools, native-tool allowlist, hooks, skills and injects. A plugin's tool type defines symbolic input fields such as `file_path` and `content`; the content can itself be natural-language knowledge. Mediators choose allow/deny/inject/ask, the tool acts through the governed broker/engine seam, and events enter the session ledger. The example tool returns `wrote ${file_path}`. The harness then owns continuation or the final user response; neither its decision policy nor its terminal answer is supplied here. See [RT-RTE-mediated-action](#rt-rte-mediated-action) and [RT-BAP-profile-guidance](#rt-bap-profile-guidance).

The graph's context is the entry repository plus mounted dependencies/workspace members, with `edit` members live and `discover` members pinned for discovery. Repository identities come from `.arsumbris/repo.yaml`; workspace membership comes from `.arsumbris/workspace.yaml`. Cross-repository references use repository-qualified links. The declared engine holds the graph in memory, updates it on file changes, provides versioned reads and subscriptions, and reports diagnostics. The persistent substrate remains files. No transaction, concurrent-writer conflict, ledger replay or crash-recovery implementation is available here (SRC-1, `au-engine.md`, `au-mcp.md`). Memory revisions and selection semantics beyond these runtime interfaces are left to the memory analysis.

### Three forcing cases and guarantee boundaries

**1. Unread overwrite versus unreachable mediation.** The read-guard example denies an unread overwrite; floors are described as fail-closed at load. But the same source says mediation fails open when the daemon is unreachable. These are distinct failure points, not a single universal fail-closed property. The profile and adapter determine the declared native-tool routing, while actual grant configuration and lifecycle coverage are unavailable. The strongest warranted conclusion is a documented policy on the mediated path, conditional on reachable mediation and functioning adapter/plugin contracts, not an invariant over all file effects. See [RT-CLM-mediation-floors](#rt-clm-mediation-floors).

**2. Invalid typed content versus file admission.** The engine explicitly permits saves and reads despite bad data. Thus a guarded write seam does not imply semantic validity or even structural-validity admission. The projection route also exposes `host.files.write`, while external file changes update the graph. Neither path is shown passing through MCP's read-guard. Direct engine access is documented via `au daemon start .`; the MCP statement that plugins do not open sockets describes that plugin contract, not exclusive platform access. See [RT-RTE-host-edit](#rt-rte-host-edit) and [RT-CLM-diagnostic-saves](#rt-clm-diagnostic-saves).

**3. Discovered executable extension versus isolation.** A type query discovers plugin/projection code, and runtime metadata names its entry and contract version. Compatibility refusal is declared, but accepted code runs with the user's privileges and no sandbox. Shell commands, network and filesystem access by installed code are therefore part of the warned capability surface, not proven broker-confined effects. This challenges any reading of “Every agent action” as an OS-level containment claim. See [RT-RTE-extension-load](#rt-rte-extension-load) and [RT-CLM-user-privileges](#rt-clm-user-privileges).

Together these cases cover the material alternate paths visible in this documentary boundary: mediated tools; redirected native tools; unreachable-daemon mediation; host callbacks and projection code; direct engine clients; external file editing; installed code's arbitrary commands. No remote-worker, sub-agent, manual graph execution or durable resume implementation is supplied. Their omission is not evidence of absence. The current profile's grant set and the actual deployment envelope are unobserved; the declared envelope is explicitly unsandboxed. The source does not establish an approval UI's handling of `ask`, denial bypass behavior, durable continuation semantics or reliable context injection.

### Change admission and context control

Knowledge changes can come from agents through tools, humans through views, or ordinary filesystem writers. Type diagnostics inform rather than veto those saves. Executable capability/UI changes are authored as repositories with type definitions and code, discovered through the type graph, and loaded under SDK contract declarations. Projection edits require rebuild/reload. Public release adoption is a human/installer operation over sibling repository tags and builds; release testing remains attributed operation, not an answer oracle or causal experiment (SRC-1, `INSTALL.md`, `MIGRATION.md`, `VERSION.md`). [RT-RTE-extension-load](#rt-rte-extension-load) separates this admission from model-proposed file content.

Working-context controls visible here are static triggered skills, always-on injects seeded by graph walks, and session-start computed injects. A profile selects what a session sees and an adapter materializes guidance. The profile/graph-walk bodies, exact delivery transforms, harness context retention and compaction rules are outside the captured implementation. No selective trimming or sub-agent frame boundary can be inferred. These are declared delivery mechanisms, not evidence that guidance changed a model's answer. [RT-BAP-profile-guidance](#rt-bap-profile-guidance) records their intended force. No theory criticism/revision or self-improvement conclusion is drawn from extensibility alone.

## Shared records

### Components

#### RT-CMP-agent-harness
Label: Optional agent harness and model dependency

The source-native identities are Claude Code and Codex, connected through their adapters. Harness process/configuration is symbolic software; model inference is an unresolved distributed-parametric dependency, not an inspected component implementation. Model parameter substrate and provider internals are uninspected outside SRC-1's entry artifact. Parameters changing during operation: uninspected. Exact model version pinned: uninspected; this source pins no inference model. Mutable endpoint resolving to another model: uninspected; no endpoint contract is supplied. The source names harness compatibility, not model identity or weight fixity (SRC-1, `INSTALL.md`).

> **An agent harness** *(optional — only for the agent layer)* — **Claude Code** or **Codex** work out of the box (via `au-mcp-adapter-cc` / `au-mcp-adapter-codex`). Any other model or harness needs an adapter. The engine and host run without one; you just won't get agent capabilities until a harness is connected.
> --- `INSTALL.md`

### Operative objects

#### RT-OBJ-device-config
Label: Pre-graph device configuration

Source-native objects are engine `repos.yaml`, host `workspace-template-repos.yaml` and host `paths.yaml`, under the user's `.arsumbris` directory. They are symbolic YAML filesystem configuration: repository name/path rows, ordered template paths and tool executable paths. Engine/host readers are documented, not inspected. The implemented producer is [RT-RTE-device-seeding](#rt-rte-device-seeding). These device-local files are not inferred knowledge memory or model parameters (SRC-1, `scripts/seed-device-config.py`, `INSTALL.md`).

> merged.setdefault(name, path)              # do not relocate an already-registered repo
> --- `scripts/seed-device-config.py`

#### RT-OBJ-agent-profile
Label: Session agent-profile

An `agent-profile` is symbolic session selection/configuration over skills, injects, tools, a native-tool allowlist and hooks. It selects natural-language guidance separately from executable plugins; guidance is interpreted by the agent while profile/tool fields are intended to be consumed by daemon/adapter rules. Repository graph storage and launch materialization are declared, but the exact profile serialization, default grant set and generated harness files are not supplied. This is the configuration referent, not the guidance bodies or ledger (SRC-1, `au-mcp.md`).

> An **agent-profile** bundles what one session sees: its `skills`, `inject`, `tools`,
> `nativeToolAllowlist`, and `hooks`. Tool visibility is the profile's, resolved daemon-side.
> --- `au-mcp.md`

### Routes

#### RT-RTE-device-seeding
Label: Device configuration bootstrap

The initiating principal is a user or installing agent running the shipped Python script. Code owns discovery, pruning, parsing and merge selection; the caller selects root/device-root/engine override and explicitly opts into writes. The ordinary install mode is an open setup task, not an experiment. There is no answer oracle. Filesystem manifests and existing configuration are inputs, not expected-answer references. Admission trigger: `--write`; proposed change: missing registry/template/tool-path entries. Caller veto: omit that flag. Software retains existing repository locations and top-level path keys, warns on conflicts/missing binaries, and does not authenticate discovered code. Existing `binaries` prevents adding even a missing nested Claude entry. Guidance is `INSTALL.md`; generated YAML persists, not installer reasoning. This route admits production launch configuration, not knowledge claims.

- Immediate return: stdout lists discovered repositories, merges, warnings and would-write or wrote messages; unknown options or a missing root terminate through `sys.exit`.
- Later read-back: documented host pre-graph setup consumes template/tool configuration and engine resolution consumes repository locations; actual readers are outside this source.
- Delegated visibility: no subprocess delegation in the inspected script; subsequent host/engine access is a documented separate invocation.
- Selection predicate: walk for `.arsumbris/repo.yaml`, prune named build/test/scratch/template directories, require a name scalar, keep first name collision, preserve existing locations; find binaries by override, PATH then known directories.
- Invalidation or expiry: no automatic stale-entry eviction; existing entries win and the script advises manual edit or re-registration for relocation.
- Activation or effect: implementation writes two rendered registries and creates/appends tool-path keys only in write mode; successful host launch is unobserved.
- Evidence limits: only producer logic inspected; no installed files, fixture execution or end-to-end bootstrap trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery is warning/manual correction and rerun, not an inspected transaction or rollback protocol. Two registries are rewritten sequentially with `open(..., "w")`; tool paths are created or appended afterward. No backup/atomic replacement is implemented in this script, so the dry-run safeguard is not all-or-nothing application. Idempotent merge intent does not imply stale path repair or comment preservation (SRC-1, `scripts/seed-device-config.py`).

> if not write:
>         print("\n--- would write (engine repos.yaml) ---")
> --- `scripts/seed-device-config.py`

> for path, text in ((engine_cfg, engine_text), (host_cfg, host_text)):
>         os.makedirs(os.path.dirname(path), exist_ok=True)
>         with open(path, "w", encoding="utf-8") as f:
>             f.write(text)
> --- `scripts/seed-device-config.py`

#### RT-RTE-mediated-action
Label: Profile-mediated agent file action

Endpoints are harness adapter, workspace MCP daemon, mediator hooks, plugin tool and engine broker, then tool result/event ledger. A workspace daemon serves many sessions, paired 1:1 with its engine over one socket; the ledger is session-specific. The foreground model proposes a tool/action and content; deterministic mediator/plugin contracts supply admission decisions. A human contribution is possible through `ask`, but who presents/answers it and any approval persistence are uninspected. Mode is open agent work, not a specified curriculum; answer oracle: none established. A prior read is a precondition witness, not a truth oracle. Proposed file changes can be denied by mediators; no content-quality improvement trigger or automatic rollback is supplied. Profile guidance may shape the model proposal, but bodies are unavailable. Written files and ledger events persist by declaration; the exact storage/durability contract of the ledger is not supplied.

- Immediate return: documented example tool returns a content string reporting the written path; mediation can allow, deny, inject or ask before execution.
- Later read-back: graph reads can consume changed files; the source supplies no ledger-to-future-model replay or trace-fed revision contract.
- Delegated visibility: adapter conveys harness lifecycle; daemon can serve many sessions, but per-session cross-visibility and delegation isolation are uninspected.
- Selection predicate: profile resolves visible tools/hooks; type-defined tool inputs select path/content; mediators inspect pending action and session context such as `hasRead`.
- Invalidation or expiry: uninspected — read tracking lifetime, grants, ledger retention and mid-session profile reload are not defined here.
- Activation or effect: declared pipeline mediates, runs a tool through the broker, then appends events; no exercised overwrite or reliable compliance is observed.
- Evidence limits: examples and architectural prose only; daemon, plugins and adapters are separate repositories.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

SRC-1, `au-mcp.md` provides the pipeline and denial example:

> - `mediate` — the mediators decide (allow / deny / inject / ask).
> - `act` — the tool runs against the governed engine seam.
> - `observe` — every event is appended to the session's ledger.
> --- `au-mcp.md`

> if (action.tool === 'write_file' && !ctx.hasRead(action.input.file_path))
>     return { kind: 'deny', reason: 'read the file before overwriting it' }
> --- `au-mcp.md`

#### RT-RTE-host-edit
Label: Host projection file edit

Endpoints are a human/UI event, mounted projection, `MountHost` file/config callbacks, engine-backed graph and files. A composition's pool/reference graph selects configured projection instances. Symbolic code owns callbacks and coordination via selection, focus and intents; the user chooses UI actions, while arbitrary projection code can initiate effects too. The host supervises the engine daemon. Open editing is the operating mode; no answer oracle or improvement trigger is established. For file admission the proposal is supplied text, and for pane configuration it is changed instance configuration. Diagnostic errors do not veto saves. Human initiation is not evidence of per-content approval for projection-generated content. Rollback semantics are uninspected; projection unmount cleanup disposes subscriptions but is not data rollback.

- Immediate return: file read resolves content; selection/intent callbacks coordinate UI, and `saveConfig` requests persisted pane configuration. Exact write acknowledgments are unspecified.
- Later read-back: saved files feed the live graph and persisted pane configuration is intended for later host use; reload implementation is outside this repository.
- Delegated visibility: projections follow/publish selection; intent routes to a handler or broadcast. No model sub-agent result boundary is described.
- Selection predicate: type queries discover projection kinds; composition references select instances; file path and workspace entry select file operations.
- Invalidation or expiry: unmount disposer stops subscriptions; edited code requires rebuild/reload. Data and viewer-state expiry are uninspected.
- Activation or effect: declared engine-backed file edits and persistent config can change graph/UI state, without evidence that MCP floors cover them.
- Evidence limits: illustrative callbacks and contracts, not host implementation or a supplied UI trace.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

SRC-1, `au-host.md`:

> host.files.write('notes/today.md', text)                    // ...and write it back
> --- `au-host.md`

> host.saveConfig({ note: 'edited' })                               // persist this pane's config
> --- `au-host.md`

#### RT-RTE-extension-load
Label: Executable extension admission

Endpoints are a human/agent author, a repository/type definition, type-query discovery and a plugin/projection loader, then executable module. Symbolic metadata declares code entry and contract version; executable JS/TS supplies behavior. Open extension development and release upgrades are documented operating modes; no bounded optimization curriculum or answer oracle is supplied. Human and agent authors may propose tools/views/app changes; loader contract checks can reject incompatible projections. Who approves source code before installation is not enforced here: safety guidance recommends reading/auditing it. Guidance includes SDK examples, build/reload instructions, migration notes and optional build-a-plugin skills whose full body is absent. Code, type definitions and dependency changes persist; no trace-based update algorithm is supplied. Recovery is rebuild/reload or coordinated checkout/rebuild of versions, not demonstrated rollback.

- Immediate return: declared discovery/load accepts an eligible extension or reports compatibility/discovery refusal; installed modules then expose tool or view behavior.
- Later read-back: later discovery/mount/plugin use consumes installed definitions and modules; source-changing agent logs are not shown being consumed for revisions.
- Delegated visibility: mounted code receives host callbacks or plugin context; no sandbox boundary separates installed third-party code from first-party user privileges.
- Selection predicate: plugin/projection subtype query and runtime metadata; projection migration requires each concrete type to declare its own runtime meta and matching mount contract.
- Invalidation or expiry: projection edits require rebuild/reload; internal version mismatches are declared startup/load refusal. Mid-session plugin invalidation is uninspected.
- Activation or effect: declared loading admits code that can affect files, network, commands or UI; no installed extension execution was observed.
- Evidence limits: loaders and SDKs are outside this source; compatibility testing claims remain reported operation.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

SRC-1, `au-mcp.md`, `au-host.md`, `MIGRATION.md`, `INSTALL.md`, `SAFETY.md` support these separate admission and effect boundaries:

> A plugin is its own tiny engine repo, discovered by type-query. No manifest, no registry.
> --- `au-mcp.md`

> A projection built against contract 7 is refused at load with `contract version mismatch`.
> --- `MIGRATION.md`

> - **Discovery loads only code a type declares itself.** A concrete projection that only inherits its parent's `projection-runtime-meta`, declares several, or lacks a required one is rejected, with the reason. Give every concrete projection its own runtime meta.
> --- `MIGRATION.md`

### Claims

#### RT-CLM-mediation-floors
Label: Conditional governance floors

Claimed operation: read-before-write, tool preconditions and native-tool redirect are always-on floors, with fail-closed loading. Owner: au-mcp-core policies, kernel mediation and harness adapter routing. Enforcement point: plugin load and pending-action mediation; guarantee strength: policy. Covered path: declared mediated/redirected actions. Alternate paths: unreachable daemon, projection/host writes, direct filesystem code and engine clients. Required external contract: functioning daemon, loaded floor plugins, accurate adapter lifecycle/native-tool declarations and actual profile grants. It is not an OS-wide effect invariant. SRC-1, `au-mcp.md`:

> A few floors are always on
> (shipped in au-mcp-core, fail-closed at load):
> --- `au-mcp.md`

> Mediation fails OPEN if the daemon is unreachable (it never wedges the editor), and says so loudly.
> --- `au-mcp.md`

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### RT-CLM-diagnostic-saves
Label: Diagnostics do not veto saves

Claimed operation: typed-field/reference checks report bad data but leave save/read available. Owner: engine; enforcement point: diagnostics versus save/read contract; guarantee strength: protocol. Covered path: documented engine operations and graph indexing, not every external filesystem mutation. Required external contract: actual engine behavior at its separate release revision. The guarded seam does not support a stronger guarantee of valid admitted content. SRC-1, `au-engine.md`:

> Bad data surfaces as diagnostics.
> It never blocks a save or a read.
> --- `au-engine.md`

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### RT-CLM-user-privileges
Label: Installed code has user privileges

Declared execution envelope, not an isolation guarantee. Owner: installing user and runtime processes; enforcement point: no sandbox is declared; guarantee strength: no claimed guarantee. The documented capability surface includes filesystem, network and commands for installed code, across first- and third-party plugins/projections. Current profile grants are separate and unobserved. Required external contract for narrower containment would be an additional sandbox/deployment control not supplied by this boundary. SRC-1, `SAFETY.md`:

> This is an early alpha. There is **no security hardening or sandboxing** in place.
> - Code you install runs with **your** user privileges.
> - It can read and write your files, reach the network, and run commands, like any program you run.
> --- `SAFETY.md`

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-profile-guidance
Label: Profile-scoped launch guidance

Consumer: harness agent; channel: adapter-materialized skills/injects and computed session-start context selected by [RT-OBJ-agent-profile](#rt-obj-agent-profile). Force: intended natural-language instruction/context, not mechanically guaranteed model obedience; symbolic profile rules govern visibility separately. Horizon: declared launch/session, with recomputation at session start; cross-session persistence of changed guidance and actual model delivery are uninspected. Triggered skills, always-on graph-walk injects and computed hooks differ in timing; their full bodies and graph selection transforms are unavailable. This path establishes intended guidance delivery, not learning, formulated criticism or exercised self-improvement. SRC-1, `au-mcp.md`:

> - **skills** — triggered guidance, a `mcp.skill` instance (front-matter + a markdown body).
> - **injects** — always-on context, a `mcp.inject` instance that seeds a graph walk.
> - a `session-start` hook is the COMPUTED inject, recomputed per session.
> --- `au-mcp.md`

## Annotations

none
