# Multi-repository scope comparison

## Recommendation

**For the selected Ars Umbris cross-component question, prefer one fixed
repository bundle presented as one frozen source tree. Each repository occupies
a top-level directory. Reuse the current analysis roles, source IDs and path-only
quotation convention. Extend source preparation and verification, not the
analyst's quotation workflow.**

A kernel-only run answers a narrower question; it is not an adequate substitute
for tracing how overwrite policy reaches the actual write path. Separate full
component runs need additional composition assessment. A bundle lets the existing
roles inspect those seams within one boundary. Single-repository runs remain
appropriate when one repository supplies the needed evidence; that general rule
does not override the multi-repository requirement of this case.

For analysts, `au-mcp/src/daemon/broker.ts` is simply a path with one additional
directory. The frozen component manifest supplies repository identities and full
commits. Quotation attributions should not require repeated revisions or a second
source-selection field. Reuse quotation parsing and occurrence matching; test the
existing checks through component directories before deciding they need changes.
Source verification must still establish that the tree contains exactly the
approved revisions. Directory layout alone does not establish provenance.

The report recommends this design direction, not implementation or an analysis
run. Its engineering cost and effect on quotation repair remain unmeasured.
Quotation reliability is an adoption condition, particularly because the operator
reports recurrent quotation friction in the current workflow.

## Retention, inputs and method

Retained on 2026-10-11 to support evaluation of the multi-repository analysis
proposal. This is a living comparison: correct its recommendation and current
method assessment in place; the accompanying dated source extracts retain the
original inspection evidence. It is not an accepted external-system analysis.

Commission: the operator's `kb/work/analysis-lenses/multi-repository-scope-plan.md`
authorized bounded read-only scoping of local Ars Umbris Git objects and comparison
of single-component runs, separate runs and a fixed bundle. Subsequent operator
direction selected the simpler source-tree model, preservation of quotation syntax
and source IDs, durable retention, and a short proposal. No acquisition, target
execution, implementation or run was authorized.

Inputs: the exact component pins below; entry release documentation; manifests,
contracts and callers retained in the accompanying evidence; live boundary,
acquisition, quotation, validation and publication consumers named below; and the
[analysis design brief](../../../reference/agentic-system-analysis-design-brief.md).
The preservation premise is to keep roles, independent verification, correction
ownership, source isolation and exact-byte publication unless a specific mismatch
requires a change.

Method: inspect stored Git objects without materializing checkouts; resolve release
abbreviations and compare local tags; trace enough cross-component callers to
select a useful question; audit source-ID and single-pin consumers; probe path
normalization, object presence and existing attribution checks. This was not a
workflow trial or a cost measurement. Method state at retention was inspected in
Commonplace checkout `b38982da28b66bdbf0ccaf987cf8f9ae0edc6882`; working-tree changes
were present, so that commit alone does not identify every inspected byte.
LLM author: runtime-exposed model `gpt-6.1-sol`, reasoning level `medium`; no
independent worker judgment was produced.

## Selected question and evidence boundary

**How does a typed knowledge system separate agent overwrite policy from the
mechanism that performs writes, and under what conditions does that policy
actually reach the write path in its Claude Code adapter?**

Follow one closely related route: an overwrite of an existing knowledge file
through the shipped `write_file` tool. Inspect read-before-write mediation,
plugin discovery and broker grants, harness delivery, and the engine's optional
content-hash guard. This exposes a useful design alternative to embedding policy
in a runtime: load policy from typed plugin definitions while centralizing
mutation. It does not commission adoption advice for Commonplace.

Exclude full UI supervision, other adapters, all mutation verbs, general type
language correctness, skill/inject expansion, trace learning and the knowledge
capability ecosystem. This is an **agent overwrite subsystem**, not a
whole-system Ars Umbris analysis or an executed release test.

### Available component map

Each name below denotes the canonical repository
`https://github.com/arsumbris/<name>` and the local object repository
`related-systems/arsumbris--<name>`. These are proposed evidence members, not
an approved acquisition manifest. Membership includes access to the pinned
repository; the listed paths direct initial inspection, not a path allowlist.

| Proposed member | Exact available commit | Responsibility, supporting claim and loss if excluded |
|---|---|---|
| `arsumbris` | `a9f6cceedb191b8504443222d55d3106f9f36ba9` | Entry documentation and release map: what composition is claimed to ship. Without it, component pins lack this release's documented composition. Inspect `README.md`, `INSTALL.md`, `VERSION.md`, `au-engine.md`, `au-host.md`, `au-mcp.md`. |
| `au-mcp` | `3ddc3b62ed0b339a89a57f11026676df18d3b2eb` | Kernel discovery, mediation, invocation and broker wiring. Without it, policy definitions do not establish registration, scheduling or delivery to a callable. Start at `src/daemon/{discovery,daemon,broker}.ts`. |
| `au-mcp-sdk` | `91209bb00cebde36e6454207a89e257f20573577` | Plugin, mediation and wire contracts. Without it, shared handles, contract versions and separation of mediation from invocation remain assumptions. Start at `src/{plugin,wire,client}.ts` and `type/`. |
| `au-mcp-core` | `25e0625e553c237671bba9a3a8c173a889dddf02` | Shipped read guard and write tool, with typed metadata. Without it, actual overwrite policy and the tool's forwarding behavior are external. Start at `src/{read-guard,file-tools,tool-write-file}.ts` and their type definitions. |
| `au-mcp-adapter-cc` | `333b2117f338cd4815eeeb9ab7b3932b29fa7d62` | Claude Code hooks and MCP server shim. Without it, translating mediation decisions into harness behavior and handling an unreachable daemon are unknown. Start at `hooks/pre-tool-use.ts`, `hooks/hooks.json`, `src/{bridge,mcp-server,surface}.ts`. |
| `au-engine-sdk` | `ffeca7a745af6f8069d5d2151fc96bae964825dd` | Broker's typed engine client. Without it, mapping write arguments and revision-compatible wire dispatch are unverified. Start at `src/{client,wire}.ts`. |
| `au-engine` | `46f12389d4d4833fed51640a48cf938516433106` | Engine mutation handling. Without it, optional hash checking, path admission and the actual disk-write seam remain client claims. Start at `crates/au-engine/src/{serve,mutate}.rs`; follow the named target-resolution helpers rather than reviewing the full graph engine. |
| `au-defaults` | `0879c5ef432b468b9fa0e4a3e52d2fb58d2ec504` | Default aggregation and profile configuration. Without it, shipped membership and profile selection cannot be distinguished from a possible custom installation. Start at `mcp-bundle/.arsumbris/repo.yaml`, `studio/profiles/Claude.yaml` and the associated workspace declaration. |

Eight repository roots are the proposed minimum for **this formulation**, which
includes release composition and a default profile. A question restricted to the
kernel's extension mechanism needs fewer. An evidence bundle is not an executable
dependency closure: ordinary dependencies may remain external if the affected
claim is limited explicitly.

| Candidate not admitted | Exact available release commit | Why outside this question; conclusion prevented |
|---|---|---|
| `au-mcp-adapter-codex` | `3b0e3a3cf67b3143819c61c590efc85d36c23bc5` | Alternative harness path; no cross-adapter equivalence claim. It appears in the default aggregator but that does not compel implementation inspection. |
| `au-host` | `0e85fb1731fdef2d6196618aff5a2a567e621866` | Shipped UI/launcher, not an ordinary library dependency. Exclusion prevents claims about actual host-created sessions, environment delivery or GUI bypass paths. Selected route assumes a correctly configured adapter launch. |
| `au-type-codegen` | `e3c63da4afc77c2979ea06763c8c1045bcd93644` | Actual runtime dependency of kernel discovery (`buildIR`, `emitJsonSchema`), not merely a build tool. Exclusion prevents proving schema generation correct. The question assesses overwrite mediation and forwarding, conditional on successful discovery/input validation; expand only if schema behavior becomes load-bearing. |
| `au-type-system` | `066fd06b224bc46358273ebfbc82b6b8863e9885` | Specification reference; no general type-language correctness claim. |

The first-party capability repositories listed in `INSTALL.md` supply content,
skills and governance extensions. They are not all needed to understand this
baseline overwrite route. Their customization effects remain outside the slice.
Node/pnpm/Rust and third-party packages are ordinary execution dependencies, not
automatic evidence members. Examples and linked references likewise do not enter
merely by being linked. This pass deliberately did not pin or inventory the entire
ecosystem.

### Release coherence and what was actually established

The entry's `VERSION.md` calls the release `0.0.1-alpha` and records abbreviated
commits. All twelve inspected abbreviations resolved to full local commits; each
local tag of that name resolves to the corresponding pin. No selected revision
was substituted with a branch tip. There is no missing-object gap for this map.

`INSTALL.md` documents sibling layout and JS `link:../...` dependencies. Inspected
package manifests support those links: kernel to both SDKs and type-codegen, core
to both SDKs, adapter to kernel and MCP SDK. The default MCP aggregator names
kernel, SDK, core and both adapters. Engine/engine-client wire constants agree at
29; inspected MCP wire and plugin constants are 0, and the core metadata uses 0.
Kernel discovery checks plugin contract equality. These are composition and
interface-consistency observations, **not proof of complete release compatibility**.

No source was executed, installed or materialized. Release testing is a claim in
the entry documentation, not an observed run here. Remaining gaps include actual
harness hook delivery, host launch configuration, complete discovery/schema
correctness, and whether mediated read freshness remains enforced at the eventual
write under all failure/race conditions. They prevent an unconditional claim that
all agent writes are safe or governed. They do not prevent this option comparison.

The [retained local evidence](./measurements/ars-umbris-multi-repository-scope-evidence.md)
contains full pins, blob digests, discriminating extracts and the namespace probe.
For example, core's read guard allows creates and an explicit hash, and allows
when the current hash cannot be obtained; the adapter's mediation bridge defaults
to allow on failure; the engine checks a hash only if one is supplied. These
condition-sensitive seams explain why reading only the kernel cannot settle the
selected question. This is scoping evidence, not a completed safety assessment.

## Options: coverage and total work

| Option | Can establish | Cannot establish | Expected work |
|---|---|---|---|
| One `au-mcp` run with external limits | Kernel extension/discovery mechanism, session state, mediation ordering and broker grants. It fits a narrower model-serving mechanism boundary. | Implemented floor policy, real adapter behavior or engine write guarantees; only attributed contracts for external components. Cannot answer the selected composition question fully. | One existing workflow and one operator-facing set; lowest new engineering burden. Strong value if kernel architecture is the actual priority. |
| Separate component runs | Independently bounded accounts where each component qualifies; existing source and publication guarantees remain usable. Kernel, core tool mechanism, adapter host integration and engine knowledge system are plausible targets. | Integration does not follow from accepting each account. SDKs and default configuration may be supporting contracts rather than standalone qualifying targets. | For `k` commissioned qualifying component runs: `k` boundary decisions and deterministic check/correction cycles, `k` report verifications, `k` profile stages, `k` synthesis stages and their verification, and `k` overview/publication sets to read. Analytical depth varies; no assumption that all eight roots warrant full runs. |
| One explicitly frozen bundle | A coherent static account across the admitted route; one runtime map, two lenses, reconciliation, report verification, profile and synthesis sequence. | Other adapters/host routes, excluded capabilities and observed execution. Bundle membership does not establish exhaustive coverage or compatibility. | One wider boundary plus manifest preparation; analysts/verifier must still trace each consequential seam. Avoids repeated workflow packaging and later composition reconstruction, but pays an implementation and testing cost before its first run. |

Separate runs need a **separately commissioned composition assessment** if the
operator still wants the cross-component answer. It must bind exact component
revisions, trace callers/contracts across the seams and verify those new claims.
Independent accepted reports can guide it; they are not substitutes for source
inspection or authority to acquire anything. That assessment adds reconciliation
and operator reading, even if it is much smaller than another full run.

No timing or token savings were measured. A bundle may reduce repeated fixed
workflow work while increasing each analyst's search space and verifier load.
Separate runs win when component accounts have independent reuse value, when
questions are separable, or when only one component matters now. The present case
supports one bundle **for the selected composition question**. Choosing a
single-repository run instead requires explicitly narrowing that question.

## Fixed-bundle policy and preservation conditions

The operator approves the question, stable public target and finite membership
before opening a run. Code binds names to canonical repository identities and
full commits; workers cannot add entries. A discovered repository produces a
local limit naming the conclusion prevented. If the question cannot be answered
within that limit, the worker returns `problem`; the coordinator asks the operator
to revise the boundary in a separately opened run. It never silently fetches or
adds a repository, and never edits an already frozen boundary to continue.

A future implementation must satisfy these conditions:

1. **Intake and identity:** accept one explicit component manifest, not recursive
   URL traversal. Require unique normalized component names/identities, full
   commits, and a declared system/slice identity. Reject ambiguous membership.
2. **Source preparation:** verify each origin, exact commit and canonical access
   root. Preserve existing dirty or foreign checkouts; do not repair them silently.
   Journal each preparation and bind aggregate completion to the complete manifest.
   Publish the acquisition result only after every required member verifies.
   Partial or uncertain preparation stops before workers; retries recognize the
   same pins, not new remote tips. Retain partial state for operator recovery.
   Physical checkout renaming to sibling plain names is unnecessary for static
   reading; preserve runtime-relative links as evidence, not as instructions to
   reproduce an installation.
3. **Worker access:** present the approved repositories as top-level directories
   of one frozen source tree, with provenance supplied through the existing boundary
   input. The physical layout or source-read adapter remains an implementation
   choice. Search only approved components, read-only. Keep existing roles,
   correction ownership and later record-based consumption. Report verification
   searches that tree under its existing materiality/stopping rules, not all local
   repositories.
4. **Validation and provenance:** bind every member's reviewed boundary to a digest
   of the canonical identity/revision manifest, not to one arbitrarily selected
   component commit. Do not include machine-specific access paths in this digest.
   Verify all source pins on live checks and before assembly/publication. Keep
   exact-byte member and criterion manifests, worker provenance, refusal handling,
   acceptance and publication journaling unchanged in purpose.
5. **Public identity:** approve a stable system identity independent of the
   component revision manifest. For an Ars Umbris system account, the entry
   repository's canonical URL is the natural candidate; do not identify the system
   with one implementation component. Name partial scope in the boundary rather
   than invent a new identity for every question. If multiple current slices must
   coexist, resolve that actual publication need separately: current slug generation
   ignores URL fragments, so adding a fragment is not sufficient. Preserve stable
   refresh, duplicate detection and archival behavior.

Do not install dependencies or execute the target as part of bundle support. Do
not package repository code into today's non-Git capture to evade these changes:
its single-file capture contract does not preserve component Git anchoring.

## Citations and source-register decision

**Keep the existing path-only quotation convention and `SRC-*` source register.
For a bundle, paths start with the repository directory; the pinned manifest
supplies identity and revision. Do not add per-quotation source IDs or repeated
commits. Source-ID removal is not part of this recommendation.**

A citation such as `au-mcp/src/daemon/broker.ts` identifies a component and a
commit-relative path. The manifest supplies its repository and revision. A
component name is a physical repository locator, not an evidence layer, scope
label or analyst record ID. Implementation, doctrine/design, reported operation,
observed run and causal experiment remain separate evidence-layer information.
Keep one source-register row per repository, with its existing `SRC-*` ID,
identity, full commit, evidence layers, inspected scope, anchors and access gaps.
Bind each row to its manifest component. The component directory locates a file;
the source ID continues to support finding references and scope accounting.

The [namespace probe](./measurements/ars-umbris-multi-repository-scope-evidence.md#namespaced-path-probe)
found distinct committed `README.md` blobs under three component pins; prefixes
remove that basename ambiguity. Normalized path checks reject absolute paths,
`..`, redundant separators and dot segments. An undeclared component must be an
error, not a fallback search. An absent path in an available component is a bad
anchor; unavailable approved evidence is unverified and prevents live acceptance.
Explicit wrong repository/revision attribution must fail even if text matches.
Symlinks must not allow filesystem escape. Duplicate/case-colliding component
names must be rejected at intake. These are dispatch requirements, not evidence
that today's resolver implements bundle support: a prefixed path is currently
looked up inside the one pinned repository and does not resolve. The missing piece
is source-tree lookup and pin verification, not a richer quotation grammar.
Existing quotation parsing and occurrence matching can remain the basis; reuse
has not yet been demonstrated end to end.

### Actual consumers of `SRC-*` and source pins

| Consumer | Current invariant | Implication |
|---|---|---|
| Boundary type, `declare-boundary.md`, shared record contract and worker rules | Eight-column register; one row per stable source with labelled layers; every source-dependent finding cites a declared `SRC-*` and anchor; later workers cannot add IDs | Preserve declaration/visibility and scope limits; bind registered repositories to approved component directories. |
| `records.py`: source parsing, `artifact_declarations`, `artifact_record_findings`, range checks | Bare `SRC-*` references resolve only against the boundary available in the member's citation scope; unresolved IDs and numbered ranges are refused | Keep these source-reference checks and semantic `RT-*`, `MEM-*`, `EPI-*` and behavioral-authority record IDs unchanged. |
| `rules.py`: `_agentic_boundary_register_rule` | Row shape, unique IDs and a row matching the boundary's frozen kind/identity/revision | Keep shape and label checks; extend agreement checking to every approved component. |
| Boundary schema, `boundary.py`, opening/acquisition, generic frozen-source checks | One exact frozen Git/capture object, reviewed boundary equal to its revision, authorized source inspection | These are not `SRC-*` consumers. Deleting labels does not make them bundle-aware. |
| `quote_grounding.py`, `_artifact_quotation_findings` in `rules.py` | Quotations resolve against one authorized pin; explicit wrong repository/revision, escaping/nonexistent paths and unavailable bytes are distinguished | Keep quotation grammar and matching. Resolve the extra directory through the approved source tree without weakening attribution checks. |
| Publication, analysis enumeration, profile/comparison consumers | Exact-byte artifact/provenance plus one stable source identity, directory and duplicate detection | Also not numbered-label consumers. Bundle/slice identity affects them separately. |

The audit searched analysis instructions/types, analysis code, generic frozen
source/validation code and tests. Tests exercising register grammar and visibility
include `test_records.py` and `test_validation_draft_in_role.py`; comparative
profile tests exclude source IDs from analyst-record citation slots. Numbered
labels are **not the durable provenance identity** and do not route quotations.

The source register is useful existing infrastructure for several repositories,
but it does not currently authorize or route reads: those consumers bind one
frozen source object. Extend that binding to the finite manifest while retaining
source-reference declaration and visibility checks. Do not remove source IDs or
redesign generic evidence handling to support hypothetical future source kinds.

Historical retained analyses remain byte-for-byte unchanged. Readers and
validators must continue to understand their Source registers and single-pin
quotations. The new source-tree representation needs old and new boundary fixtures,
not a mass rewrite or new quotation dialect. Supporting the old format serves an
actual consumer: existing published sets.

## Change footprint for source-tree support

No files in this table were changed by this comparison. Follow
[method maintenance](../../../agentic-system-analyses/instructions/maintain-analysis-method.md)
before an implementation commission; update each consumer through its actual
loading path.

| Layer | Minimum affected surfaces | Needed verification |
|---|---|---|
| Instructions/types | Boundary type/schema and source-tree contract; boundary and worker missions; source identity and reviewed-boundary descriptions; overview/profile contracts where boundary identity semantics change. Keep record IDs and quotation grammar. | `test_member_types.py`, `test_instruction_composition.py`, `test_records.py`, `test_profile.py`; old retained register/quotation fixtures plus new bundle coverage and excluded-loop cases. |
| Plan/layout | Opening/acquisition input for the approved manifest; existing `boundary` dependency supplies component map; same roles and correction relations; reviewed-boundary identity propagation | `test_compact_plan.py`, `test_opening.py`, `test_pinned_drafts.py`; ensure all jobs receive identical pins, corrections cannot change membership, and no extra analyst jobs are derived. |
| Analysis-specific code | `opening.py`, `boundary.py`, `rules.py`, `publication.py`; source-tree preparation and lookup; inspect `worktree.py`, `run_ids.py`, `analyses.py`, `guards.py` and comparison identity consumers for system-level identity compatibility rather than assume all need edits | `test_boundary.py`, `test_acquisition.py`, `test_publication.py`, `test_publication_locking.py`, `test_retained_analyses.py`, `test_pinned_validation_contracts.py`, comparison `test_systems_matrix.py`; manifest mutation, missing member, wrong origin/commit, directory collision/escape, wrong explicit revision, exact-byte publication, stable system refresh and archive compatibility. |
| Generic engine/shared libraries | `artifactrun/sources.py` exposes one-pin freezing and refusal checks; `handlers.py`/`checks.py` carry one source mapping into validation; validation's `frozen_source` authorization and quote pin dispatch are shared seams | Existing artifactrun and validation consumer suites plus source quote suites. Preserve single Git/capture behavior and interrupted-acquisition recognition; test partial aggregate preparation and no default-tip reselection. |

The generic plan/layout machinery already carries a boundary mapping and compares
identity field values; it need not learn recursive repository acquisition or new
analytical roles. Some shared source-check dispatch may be unavoidable if a
bundle is represented as a new frozen-source kind. First compare a narrow
analysis-owned adapter using the existing one-repository primitives with that
small shared dispatch change. Do not decide the generic extension merely to keep
a hypothetical capability. Any shared implementation requires general tests and
affected consumer suites under the repository's test-selection rules.

## Risks, counterevidence and return

- **Bundle scope creep:** this question already proposes eight roots. Codegen and
  host exclusions could become load-bearing. The remedy is claim limits and an
  operator decision, not recursive acquisition. If the question cannot stay
  useful with these limits, shrink it before opening a run.
- **Cost counterevidence:** the kernel alone can reveal mechanism/policy separation
  for a narrower question; source-tree support has no measured cost benefit yet.
  Independent component reviews may have greater reuse value. Neither observation
  makes a kernel-only run sufficient for the selected cross-component question.
- **Quotation friction:** the operator reports recurrent problems today. A component
  directory should add no new authoring rule beyond the path itself. If supporting
  it requires extra attribution fields or substantial new repair work, the proposed
  implementation has failed its simplicity condition.
- **False coherence:** matching release pins and inspected constants do not show
  hook execution, schema correctness, full compatibility or race-free writes.
  Preserve those qualifications beside every affected claim.
- **Operator cost:** one bundled report may be harder to consume than a focused
  component account. Keep the question and untraced seams prominent; do not
  substitute a multi-repository inventory for explanation.
- **Historical validation:** extending frozen-source structure must not break old
  boundary validation. Keep existing source IDs and quotation syntax; preserve
  previous accepted sets unchanged.

The next adoption decision is whether to commission bounded source-tree support
with offline fixture verification. Test manifest identity, all-or-nothing pin
availability, the existing quotation format through component directories,
unchanged single-source behavior and stable system publication identity. The
physical layout and minimal shared-code changes remain open. The overwrite slice
is a discriminating fixture, not the scope of a future whole-system Ars Umbris
analysis. Full-system coverage would need its own approved component boundary.
This report authorizes neither implementation nor acquisition nor an analysis run.
