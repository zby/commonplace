---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Arsumbris epistemic routes: typed diagnostics, operational governance and unknown content warrant at the entry-repository boundary."
run-id: AAS-2026-10-15-arsumbris-a9be6bac297f-01
reviewed-boundary: "716bb14f2bf50e249d414525c8e07c50478fc786"
---

# Arsumbris epistemic report

## Source-and-claim boundary

The question is whether typed knowledge, diagnostics and agent governance establish truth-bearing knowledge or primarily organize content and control actions. The evidence boundary is the documented platform plus the implemented device seeder, not the sibling engine, host, agent kernel or knowledge packages. See the [boundary and exclusions](boundary.md#boundary-and-evidence) and [Source register](boundary.md#source-register). All source findings below refer to SRC-1 at the frozen commit. No execution evidence or causal comparison is supplied. Runtime findings are provisional; direct reads below check alternate operations and claims against the same frozen source.

The source's consequential claims concern a typed graph, actionable diagnostics, governance and reusable knowledge/capabilities: [EPI-CLM-typed-knowledge](#epi-clm-typed-knowledge), [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves), [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors), and [RT-CLM-user-privileges](runtime.md#rt-clm-user-privileges). The entry documentation does not itself supply substantive research claims to evaluate. Knowledge-package names are not evidence of their contents or evaluators.

| Entry point or operation | Source path directly read | Covering records / limits |
| --- | --- | --- |
| Install prompt, package acquisition, release claims and user launch handoff | `README.md`, `INSTALL.md`, `VERSION.md`, `MIGRATION.md` | [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding), [EPI-RTE-source-ingest](#epi-rte-source-ingest); release testing is reported operation only. |
| Sole tracked executable CLI: option dispatch, discovery, parse/merge/render, dry run/write | `scripts/seed-device-config.py`, read completely | [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding), [EPI-OBJ-registry-paths](#epi-obj-registry-paths); implementation supports producer semantics, not successful later launch. |
| Engine daemon start/status/stop, reads, mutations, subscriptions, dependency/workspace indexing | `au-engine.md`, `MIGRATION.md` | [EPI-RTE-graph-index](#epi-rte-graph-index), [EPI-RTE-type-diagnostics](#epi-rte-type-diagnostics); engine implementation unavailable in this boundary. |
| Host launch, file read/write, config save, selection, intents, focus/view state, preview/theme and unmount cleanup | `au-host.md` | [RT-RTE-host-edit](runtime.md#rt-rte-host-edit), [EPI-RTE-graph-index](#epi-rte-graph-index); layout/preview cleanup is not withdrawal of knowledge. Actual consumers remain uninspected. |
| MCP start, adapter launch, tools and hooks, profiles, skills/injects | `au-mcp.md` | [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action), [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance), [EPI-RTE-hook-lineage](#epi-rte-hook-lineage); direct reads confirm observer, stamper and session-start operations as well as mediator. |
| Executable plugin/projection discovery, rejection, rebuild/reload and arbitrary effects | `au-mcp.md`, `au-host.md`, `MIGRATION.md`, `SAFETY.md` | [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); no content-warrant evaluator follows from SDK compatibility. |
| File-to-source-note ingest and tree research, rules/governance/writing knowledge packages | `INSTALL.md` | [EPI-RTE-source-ingest](#epi-rte-source-ingest); only package descriptions accessible within scope. Missing transformations and acceptance consumers prevent a whole-platform negative about knowledge production. |
| Harness inference and provider state | `INSTALL.md` | [RT-CMP-agent-harness](runtime.md#rt-cmp-agent-harness); no model/version/parameter-update evidence, preventing model-learning or internal-reasoning conclusions. |

This is a material-operation coverage account, not a whole-system implementation audit. Direct source reads add no repository or source ID. The banner remains excluded; licensing is nonmaterial here. Actual knowledge bodies, provenance-preserving ingest, evaluator implementations, exact guidance delivery, acceptance records, rejection/withdrawal consumers and later reliance traces are missing. Respectively these gaps prevent semantic classification of knowledge updates, implemented warrant judgments, evidence of compliance, accepted-claim attribution and exercised lifecycle-integration conclusions. None is converted into evidence that the platform lacks those routes.

## Epistemic-object inventory

Fields owned by supplied records say `see`; the rows identify material distinctions rather than redefine those records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files) | Potential assertions in Markdown/YAML bodies; no concrete research proposition individuated | Typed knowledge substrate | SRC-1 `au-engine.md`; see record | File typing and storage do not warrant assertions. |
| [EPI-OBJ-type-definitions](#epi-obj-type-definitions) | Type constraints are symbolic policy; diagnostics can assert conformance/nonconformance in that formal domain | Define fields, references and body shape | SRC-1 `au-engine.md`; see record | Constraint validity is not source truth or encoding fidelity. |
| [EPI-OBJ-session-ledger](#epi-obj-session-ledger) | Events may assert that actions occurred; exact fields not determinable | Observation | SRC-1 `au-mcp.md`; see record | No event schema or downstream replay consumer. |
| [EPI-OBJ-write-metadata](#epi-obj-write-metadata) | Metadata assertions not individuated | Governed-write provenance | SRC-1 `au-mcp.md`; see record | No stamp schema or authenticity check. |
| [EPI-OBJ-registry-paths](#epi-obj-registry-paths) | Name/location associations usable as propositions about local installation; also symbolic launch configuration | Bootstrap resolution | SRC-1 `scripts/seed-device-config.py`; see record | Stale entries preserved; parser supports a subset, not arbitrary YAML. |
| [RT-OBJ-agent-profile](runtime.md#rt-obj-agent-profile) | Configuration, not a knowledge claim; see record | Session selection | SRC-1 `au-mcp.md`; see record | Guidance bodies separate and unavailable. |
| [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance) | Guidance/context may include claims, but actual content not determinable; see record | Natural-language instruction to harness | SRC-1 `au-mcp.md`; see record | Delivery neither establishes truth nor obedience. |
| [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | Executable definitions are capability policy, not accepted propositions; see record | Admit tools/views | SRC-1 `MIGRATION.md`, `SAFETY.md`; see record | Compatibility and privileges differ from knowledge authority. |
| [RT-CMP-agent-harness](runtime.md#rt-cmp-agent-harness) | Produced answer content and distributed-parametric state uninspected; see record | Optional inference | SRC-1 `INSTALL.md`; see record | No concrete generated proposition or provider-state evidence. |

## Authority-route ledger

Each function is separate even where it cites the same canonical container. All possible results below are source-supported capacities or declarations, not observed outcomes. `See` defers canonical route fields to the cited record; this ledger owns architectural status and the local epistemic assessment.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-graph-index](#epi-rte-graph-index) | content transformation | doctrine only | [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files) | truth-apt transformation: acquisition/import | Mounted files into graph | Parser/indexer, declared typed-file domain | Workspace start/file change; see record | Queryable graph; source warrant unknown | No inspected engine consumer | Access and representation, not endorsement | Supplies graph to UI/tools | Graph clients, versioned reads/subscriptions, informational, live workspace | SRC-1 `au-engine.md` | [EPI-CLM-typed-knowledge](#epi-clm-typed-knowledge) | none | Semantic fidelity and source lineage unverified. |
| [EPI-RTE-type-diagnostics](#epi-rte-type-diagnostics) | check/evidence production | doctrine only | [EPI-OBJ-type-definitions](#epi-obj-type-definitions) | no content change | Field/ref/body conformity, not truth of prose | Engine type rules, formal constraint domain | Index/read changes; exact schedule uninspected | Diagnostics on bad data | Declared informational feedback | Conditional structural conformance only | Makes errors available for response | Human/agent, diagnostics, advisory, current graph | SRC-1 `au-engine.md` | [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves) | none | No execution or evaluator implementation. |
| [RT-RTE-host-edit](runtime.md#rt-rte-host-edit), [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) | retention | doctrine only | [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files) | truth-apt transformation: indeterminate | Supplied content into persistent files | Writer/API; not an evidence-consuming truth decision | Save/tool invocation; see records | Retained edits despite diagnostics | Declared write path, not inspected | No semantic acceptance license established | Files may affect later graph consumers | Engine/UI/tools, file edits, operational, until later edit/delete | SRC-1 `au-host.md`, `au-engine.md`, `au-mcp.md` | [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves) | none | Human initiation does not prove per-claim approval. Relation could be reshaping, derivation or conjecture; actual input/output needed. |
| [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) | check/evidence production | doctrine only | [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files) | no content change | Prior read/tool prerequisite witness | `hasRead`/tool-precondition, action-history domain | Before governed action; see record | Allow/deny/inject/ask | Declared mediator decision | No truth license: reading is not validating | Produces pending-action decision | Mediator to kernel, decision channel, advisory until consumed, pending action | SRC-1 `au-mcp.md` | [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors) | none | Read history accuracy/lifetime uninspected. |
| [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) | operational admission/selection/consumption | doctrine only | [RT-OBJ-agent-profile](runtime.md#rt-obj-agent-profile) | no content change | Permit or prevent action | Kernel/adapter consume mediator decision | Mediate before act; unreachable daemon fails open | Action withheld or allowed by declaration | Intended enforcing policy only on covered path | Operational permission, not accepted knowledge | Allows/blocks governed write; no OS-wide control | Tool executor, mediation/redirect, enforcing conditionally, one action | SRC-1 `au-mcp.md`, `SAFETY.md` | [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors) | Fail-open countercase limits universal reading | Actual grants, human `ask` handling and bypass effects uninspected. |
| [EPI-RTE-hook-lineage](#epi-rte-hook-lineage) | lineage/freshness/recovery | doctrine only | [EPI-OBJ-write-metadata](#epi-obj-write-metadata) | truth-apt transformation: indeterminate | Metadata folded into governed write | Stamper described as trustworthy; trust derivation/domain not specified | Write-time hook; see record | Metadata on governed content | Declared write augmentation | Cannot establish authenticity or source warrant from adjective | Changes provenance received by later readers | Governed writer/readers, stamped file metadata, informational, retained-file horizon unspecified | SRC-1 `au-mcp.md` | none | none | No metadata schema or evaluator; cannot choose import/derivation/conjecture. |
| [EPI-RTE-hook-lineage](#epi-rte-hook-lineage) | retention | doctrine only | [EPI-OBJ-session-ledger](#epi-obj-session-ledger) | truth-apt transformation: acquisition/import | Pipeline events into ledger | Observer cannot deny; append stage | After act by declaration | Session events retained, source warrant unknown | Declared append, durability uninspected | Activity record, not acceptance record | No future policy update consumer established | Session ledger, event append, recording only, session horizon unspecified | SRC-1 `au-mcp.md` | none | none | Ledger replay/revision/withdrawal not established. |
| [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance) | operational admission/selection/consumption | doctrine only | [RT-OBJ-agent-profile](runtime.md#rt-obj-agent-profile) | no content change | Select guidance/context and visible tools | Profile/adapter, session configuration domain | Trigger/session start; see record | Materialized skills/injects/spawn command | Intended visibility control/instruction | No truth endorsement or compliance license | Changes available tools/context | Harness, materialized text/profile surfaces, advisory text and declared visibility control, session | SRC-1 `au-mcp.md` | [EPI-CLM-typed-knowledge](#epi-clm-typed-knowledge) | none | Graph-walk omission/transformation and model consumption uninspected. |
| [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | check/evidence production | doctrine only | [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | no content change | Runtime metadata/contract compatibility | Loader, SDK integer and concrete-type metadata domain | Discovery/start/load | Mismatch or missing/ambiguous declaration rejected | Declared compatibility result | Interface eligibility only; not code safety or content truth | Supplies load/refusal decision | Loader, metadata comparison, enforcing by declaration, current load | SRC-1 `MIGRATION.md` | [RT-CLM-user-privileges](runtime.md#rt-clm-user-privileges) | none | No loader implementation. |
| [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | operational admission/selection/consumption | doctrine only | [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | non-truth-apt policy/content update: executable capability admission | Install/load code | Loader consumes compatibility result; installer chooses source | Install/rebuild/reload | Tools/views gain execution privileges | Declared load/refusal | Not epistemic acceptance | Admitted code can run commands/read/write/network | Host/kernel, executable module, permissive, until unload/reload | SRC-1 `SAFETY.md`, `MIGRATION.md` | [RT-CLM-user-privileges](runtime.md#rt-clm-user-privileges) | none | Audit recommendation is not a supplied audit result. |
| [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding) | content transformation | implemented | [EPI-OBJ-registry-paths](#epi-obj-registry-paths) | truth-apt transformation: acquisition/import | Existing config/manifests into selected registry rows | Text parsers/discovery/merge, local path domain | CLI dispatch; see record | Associations selected/rendered; input warrant not upgraded | Producer code implemented | Local parser/discovery result only | Emits launch configuration for documented readers | Seeder then host/engine, YAML, permissive configuration, until manual change | SRC-1 `scripts/seed-device-config.py` | none | none | Concrete lossy parser counterexample in object record; downstream readers absent. |
| [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding) | retention | implemented | [RT-OBJ-device-config](runtime.md#rt-obj-device-config) | no content change | Rendered configuration to device files | Caller `--write`, deterministic file IO | After dry-run branch; see record | Sequential registry rewrite and paths create/append | Enforced write flag in inspected CLI | Persistence does not confirm locations still valid | Enables later configured resolution, not verified launch | Device config readers, filesystem, permissive by declared contract, across launches | SRC-1 `scripts/seed-device-config.py` | none | none | No stale eviction, transaction or automatic rollback. |
| [EPI-RTE-source-ingest](#epi-rte-source-ingest) | content transformation | doctrine only | [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files) | truth-apt transformation: indeterminate | Files to typed source notes | `au-ingest` implementation unavailable | Package use, timing unknown | Declared source notes | No inspected transformation | Source warrant preservation unknown | Potential later graph/guidance use uninspected | Knowledge-package consumers, typed files, force/horizon unknown | SRC-1 `INSTALL.md` | [EPI-CLM-typed-knowledge](#epi-clm-typed-knowledge) | none | Could import/reshape/derive/conjecture; source notes and transform needed. |

No separate acceptance or lifecycle-integration route is established by this inspected entry artifact. This is not a system-complete absence claim: opaque knowledge/governance packages could supply such routes. No invented evaluator is assigned to that gap. Unmount subscription disposal, source-file graph refresh, contract refusal and manual config correction have distinct targets; none by itself withdraws a previously accepted claim or its downstream uses.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-typed-knowledge](#epi-clm-typed-knowledge) | Reuse knowledge/capabilities; typed graph checks fields/references and supplies diagnostics | SRC-1 `README.md`, doctrine/design; see record | [EPI-RTE-graph-index](#epi-rte-graph-index), [EPI-RTE-type-diagnostics](#epi-rte-type-diagnostics), [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance) | None inspected for knowledge loop | None supplied | No comparison; typedness cannot establish empirical truth | A coherent declared organization/access architecture | Actual semantic production, warranted reliance and benefit unknown; do not inflate “knowledge” into a claim of proven truth. |
| [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves) | Bad data diagnosed without blocking save/read; see record | SRC-1 `au-engine.md`, doctrine/design | [EPI-RTE-type-diagnostics](#epi-rte-type-diagnostics), [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) | None inspected | None supplied | Structural scope only | Diagnostic feedback and retention are deliberately separate | Not evidence of failed truth acceptance; no such gate promised here. |
| [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors) | Always-on floors and fixed pipeline; see record | SRC-1 `au-mcp.md`, doctrine/design | [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) | None inspected | None supplied | Unreachable daemon, host writes and arbitrary code limit coverage | Conditional operational governance, not warrant | Fail-closed load and fail-open mediation coexist; universal enforcement unsupported. |
| [RT-CLM-user-privileges](runtime.md#rt-clm-user-privileges) | Installed code has user privileges, no sandbox; see record | SRC-1 `SAFETY.md`, doctrine/design | [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | None inspected | None supplied | Warning, not independent security test | Compatibility admission is not safe-code or true-content certification | Actual deployment envelope unobserved. |

## Bounded conclusion

Arsumbris declares retention of authored files, live graph retrieval and structural diagnostics, plus profile-selected context and operational action gates. Those are useful but different functions. Checks target field/reference/body conformity, prior-action prerequisites and SDK eligibility. No inspected check licenses the truth of natural-language knowledge. Diagnostics explicitly leave save/read possible; read-before-write licenses an action, not a proposition. The admission force and horizons are the separate paths in the ledger, not a shared truth oracle.

The only inspected executable route imports and persists local installation associations. It preserves existing selections even when discovery conflicts, warns rather than repairs them, and implements only a text subset of YAML. Thus the implementation licenses claims about its own selection/rendering, not freshness, source authenticity or successful downstream launch. The concrete parser deduction below supplies a source-supported countercase to general semantic-preservation claims.

Files entering the graph are acquired content with unknown source warrant. Graph indexing declares organization and access, not novel accepted propositions. File edits, stamped metadata and external source-note generation have indeterminate semantic relations at this boundary. No concrete warranted premises and checked derivation of a domain claim, non-entailed conjecture, evidence-consuming acceptance criterion for an intended knowledge use, or post-acceptance integration is established. The missing knowledge-package implementations and claim instances prevent stronger positives and whole-platform negatives alike. Operational use before such acceptance remains operational use.

The observer/ledger route records events; the stamper claims trustworthy metadata without exposing its warrant mechanism. Neither a trace-fed policy update nor later consumer reliance on a criticism is supplied. Guidance delivery and extension loading could change behavior, but do not establish reliable compliance, reflection, learning, autonomous theory construction or exercised self-improvement. These properties remain independently unestablished, not jointly disproved. The optional model dependency's mutability, exact version and endpoint behavior remain uninspected as recorded in [RT-CMP-agent-harness](runtime.md#rt-cmp-agent-harness); nothing about provider learning follows from static file or SDK inspection.

No runtime execution, accepted candidate trace or intervention comparison grounds exercised operation, benefit or causal attribution. This partial documentary loop supports the separate route conclusions above, not an unqualified epistemic verdict on the full platform.

## Shared records

### Operative objects

#### EPI-OBJ-knowledge-files
Label: Markdown and YAML knowledge files

Source-native Markdown/YAML repositories store authored content on disk; the engine declares an in-memory graph over mounted repositories. Natural-language bodies carry possible assertions; YAML/frontmatter and reference syntax are symbolic at graph consumers. Generic content does not establish a particular truth-apt proposition. The closest supplied [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) and [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) describe producers/consumers, not a separate declaration of the knowledge substrate. [RT-OBJ-device-config](runtime.md#rt-obj-device-config) is different: pre-graph launch configuration, not knowledge files. SRC-1 `au-engine.md`, doctrine/design:

> It indexes every mounted repo (deps) and holds them as one graph in memory.
> Change a file, and the graph updates.
> --- `au-engine.md`

> The engine will parse markdown and YAML,
> and the type system only applies on those filetypes for now.
> But media files or other assets are also be indexed as untyped members.
> --- `au-engine.md`

#### EPI-OBJ-type-definitions
Label: YAML type definitions and diagnostics

Source-native type definitions are symbolic YAML files with fixed intended constraints for fields, references, inheritance and required body sections. Diagnostic messages are claims about those constraints, not endorsements of file assertions. Their storage/output encoding is uninspected beyond the declarative examples. This separates the constraint/checking part from [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files). The closest supplied [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves) is the save contract, not this object. SRC-1 `au-engine.md`, doctrine/design:

>   myInteger: Number{integer} # must be whole number
>   myPositive: Number{>=0} # must be positive
> --- `au-engine.md`

> # that file must have the type "someOtherType" required by the field
> myReference: [[instance-of-someOtherType]]
> --- `au-engine.md`

The nonnegative check admits zero despite the comment “positive”; the explicit expression, not that informal adjective, bounds the documented domain. Even a correct structural result would need faithful encoding of an external claim before it could warrant anything about that claim.

#### EPI-OBJ-session-ledger
Label: Session ledger events

Part of: [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action)

This is the observation-output part of that route, not another mediated-action container. Ledger events are declared symbolic records, but schema, backing store, durability and attribution validation are not supplied. Event storage is session-specific. This differs from natural-language guidance in [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance) and from write metadata below. SRC-1 `au-mcp.md`, doctrine/design:

> - `observer` — watch the event stream, never deny.
> - `mediator` — intercept a pending action: allow / deny / inject / ask.
> - `stamper` — fold trustworthy metadata into a governed write.
> - `session-start` — compute context to inject in front of the agent at open.
> --- `au-mcp.md`

The pipeline passage retained in [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) supplies event append evidence, not evidence of acceptance or replay.

#### EPI-OBJ-write-metadata
Label: Governed write metadata

Part of: [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action)

This is the stamped-output part of the supplied action route, distinct from its session event log. The declared stamper folds symbolic metadata into a governed write, so later file readers rather than an identified ledger replay consumer could receive it. Actual keys, assertion content, storage encoding, authentication and later interpretation remain uninspected. SRC-1 `au-mcp.md`, doctrine/design; the hook-shape passage retained in [EPI-OBJ-session-ledger](#epi-obj-session-ledger) supplies the evidence. The adjective “trustworthy” is a declared property without a supplied verification mechanism. No inference of source authenticity or warranted premises follows.

#### EPI-OBJ-registry-paths
Label: Registry name and path associations

Part of: [RT-OBJ-device-config](runtime.md#rt-obj-device-config)

The name/location and template-path part of device configuration is symbolic YAML on disk. Its consumer uses paths to locate code/repositories; an association can also assert a local installation fact. It differs from the parent's tool-path map, while sharing its bootstrap producer [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding). SRC-1 `scripts/seed-device-config.py`, implementation, supplies the parse/serialization limits:

> def yaml_unquote(s):
>     """Inverse of yaml_scalar: unquote+unescape a quoted scalar, else strip an inline comment."""
>     s = s.strip()
>     if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
>         return _yaml_unescape(s[1:-1])
> --- `scripts/seed-device-config.py`

>     # a bare scalar never carries a space or '#' (we quote those), so a '#' here is a comment.
>     return s.split("#", 1)[0].strip()
> --- `scripts/seed-device-config.py`

>         if body[i] == "\\" and i + 1 < len(body):
>             out.append(body[i + 1]); i += 2
> --- `scripts/seed-device-config.py`

>     if unsafe:
>         return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'
>     return v
> --- `scripts/seed-device-config.py`

Concrete deduction without target execution: an existing registry entry with `name: demo` and `path: /tmp/a#b` is parsed as association `demo` → `/tmp/a`, since the bare scalar is split at `#`. Regeneration therefore writes the shortened path, not the original text. Within the script's own quoted subset, value `/tmp/a#b` is instead rendered as `"/tmp/a#b"` and unquoted back intact. This countercase rules out treating arbitrary imported config text as lossless reshaping; it does not claim that an actual installed config had either value. Similarly `_yaml_unescape` copies the character following each backslash, rather than implementing all YAML escapes. Existing selections survive merge without validating continued location, as the parent's retained `setdefault` passage shows. No endpoint beyond the producer was inspected.

### Routes

#### EPI-RTE-graph-index
Label: Mounted graph indexing

The engine is the declared owner: entry repository plus dependencies/workspace members → parser/indexer → live graph → versioned reads/subscriptions to UI and agent tools. This is acquisition and organization of file content, not an evidence-consuming acceptance decision. Closest supplied [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) and [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) are clients/writers, not the graph-index route; it is not wholly contained in either. The author supplies content, workspace declarations select mounting, and filesystem changes trigger updates; no per-claim approval is described. Type diagnostics do not veto this route. No answer oracle or improvement curriculum is established. SRC-1 `au-engine.md`, doctrine/design; supporting indexing passage is retained in [EPI-OBJ-knowledge-files](#epi-obj-knowledge-files).

- Immediate return: Declared graph reads observe a version and subscriptions stream changes.
- Later read-back: Changed files are declared to reach later graph reads; exact cache/reload implementation uninspected.
- Delegated visibility: Consumers see mounted graph content; session/sub-agent isolation uninspected.
- Selection predicate: Entry repo, dependencies and workspace `edit`/`discover` members; queries select graph material.
- Invalidation or expiry: File change updates graph by declaration; actual invalidation and stale snapshot semantics uninspected.
- Activation or effect: Declared graph availability to clients, with no supplied run.
- Evidence limits: Entry documentation only; engine and clients' actual transformations outside frozen source.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> - The daemon serves consumers over a Unix socket.
> - Reads observe a version.
> - Mutations go through one guarded write path.
> - Subscriptions stream changes.
> --- `au-engine.md`

#### EPI-RTE-type-diagnostics
Label: Typed content diagnostics

The engine evaluates file fields, references and body structure against [EPI-OBJ-type-definitions](#epi-obj-type-definitions), generating diagnostic feedback. This route is distinct from the supplied [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves): that claim establishes permissive saving, not a route declaration for evaluation. Content authors propose; type authors define criteria; engine judges formal conformity. A user or model may respond, but no mandatory revision or acceptance follows. There is no external truth oracle. Operating mode is open editing; reported diagnostics are a possible correction trigger, not an implemented improvement loop. The evaluator's license is limited to faithfully encoded constraints and references, not empirical truth. Supporting passages: [EPI-OBJ-type-definitions](#epi-obj-type-definitions) and [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves), SRC-1 `au-engine.md`, doctrine/design.

- Immediate return: Diagnostic feedback by declaration; exact message interface uninspected.
- Later read-back: uninspected — diagnostic persistence and later consumption are not specified; changed file graph reads belong to the separate indexing route.
- Delegated visibility: Agents and UI are intended consumers; actual delivery and omissions uninspected.
- Selection predicate: Mounted Markdown/YAML content and its declared type, fields and references.
- Invalidation or expiry: uninspected — no diagnostic clearing/withdrawal implementation supplied.
- Activation or effect: Feedback can inform editing; no enforced rejection or observed correction.
- Evidence limits: Examples and contract only, not an implementation or test result.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-hook-lineage
Label: Hook metadata and event recording

Part of: [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action)

This is the lineage/observation part of that route; checking prior reads and consuming mediation decisions remain in the supplied container. Hooks watch events or fold metadata into a governed write; the pipeline appends events to a session ledger. Kernel and hook code are declared owners, while metadata proposals, stamp vetoes and field interpretation are unavailable. Observer has explicitly no denial authority. It is an open-work recording route, without an answer oracle, acceptance criterion or improvement trigger. Provenance and replay safety cannot be inferred from recording. Supporting minimum passages are retained in [EPI-OBJ-session-ledger](#epi-obj-session-ledger) and [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action), SRC-1 `au-mcp.md`, doctrine/design.

- Immediate return: Governed write may receive metadata; events are declared appended after act.
- Later read-back: uninspected — no ledger replay consumer or later metadata-validation route supplied.
- Delegated visibility: uninspected — multi-session daemon does not specify cross-session ledger access.
- Selection predicate: Hook shapes and pipeline events; exact event/stamp filter uninspected.
- Invalidation or expiry: uninspected — no ledger retention, stamp expiry or provenance-withdrawal rule supplied.
- Activation or effect: Declared event retention and metadata augmentation; no observed activation or demonstrated reliance.
- Evidence limits: Kernel/hook implementations and event examples absent from this source boundary.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-source-ingest
Label: File source-note ingestion

The entry installation describes the sibling `au-ingest` package as converting files to typed source notes. No counterpart route is declared in the supplied runtime; this is distinct from [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding), which produces installation config rather than source notes. Input files → opaque package transform → typed source notes is the declared progression. The package owns the transformation; human/model proposal and veto roles, truth checks, recovery and guidance bodies are uninspected. No oracle or operating mode beyond a knowledge-work capability is established. No semantic-preservation, derivation, conjecture or acceptance classification can be resolved from the name. SRC-1 `INSTALL.md`, doctrine/design:

>   - `au-ingest` (files → typed source notes), and the `au-tree-research` feature package.
> --- `INSTALL.md`

- Immediate return: uninspected — source-note output is described but no invocation/result contract supplied.
- Later read-back: uninspected — knowledge-package writers and consumers are outside this entry source.
- Delegated visibility: uninspected — no worker or delivery boundary supplied.
- Selection predicate: uninspected — source file selection and filtering not specified.
- Invalidation or expiry: uninspected — source changes, note replacement and withdrawn-source handling unspecified.
- Activation or effect: Declared conversion capability only; no exercised candidate or checked result.
- Evidence limits: Package description does not expose evaluator, acceptance criterion, intended reliance scope or source lineage.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

### Claims

#### EPI-CLM-typed-knowledge
Label: Reusable typed knowledge

The source claims composable knowledge/capability repositories, a typed graph, field/reference checks and diagnostics for agents. This is a knowledge-organization and capability claim, not an explicit claim that every saved assertion is true. It is distinct from [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves), which describes the consequence of bad data, and [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors), which describes action governance. SRC-1 `README.md`, doctrine/design:

> Repos can depend on each other, letting you reuse knowledge and capabilities across projects.
>
> The engine reads them as one typed graph, checks fields and references and gives agents diagnostics they can act on.
> --- `README.md`
