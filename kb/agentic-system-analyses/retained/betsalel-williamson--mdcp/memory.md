---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MDCP memory: authored source shards, derived publication and refs, selective host reads and maintainer feedback at the frozen commit."
run-id: AAS-2026-11-08-mdcp-1e4e8314c1e4-01
source-identity: https://github.com/betsalel-williamson/mdcp
reviewed-boundary: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
---

# MDCP memory report

## Boundary and evidence

MDCP retains repository documents, not a proprietary conversational memory. This account includes source-shard acquisition and editing, indexes, historical/rationale records, compiled documents, refs, host retrieval, maintenance, and the supplied maintainer-evaluation route. It excludes the enclosing host's opaque conversation storage and model internals from implementation attribution. Those dependencies prevent conclusions about actual window eviction, model updates or deployed cross-session recall. The source and evidence layers are SRC-1 in [boundary](boundary.md#source-register): implementation and doctrine/design, with no observed run or causal experiment.

Direct reads here covered `skills/mdcp/SKILL.md`, getting-started, doc-only, design-architecture and doc-review workflows, `skills/mdcp-arch-research/SKILL.md`, `packages/mdcp-cli/src/cli.ts` command dispatch from compile onward, core refs registry, section manifest and shard cache, and `.claude/hooks/session-start.sh`. Supplied runtime findings provide the separately labelled coverage below; their supporting passages are cited through records rather than represented as direct reads. All are SRC-1 at the frozen revision. HEAD was rechecked as 1a198715a4da72dd89bad93f84cf5d4b3ab56b01.

| Entry or memory operation | Source path in SRC-1 | Coverage and limit |
| --- | --- | --- |
| Bootstrap initial docs/config and migrate legacy material | `skills/mdcp/references/workflows/getting-started.md` | Direct; [MEM-RTE-shard-authoring](#mem-rte-shard-authoring). Initial content is agent-authored from intake/repo; no per-shard human approval established. |
| Feature docs-first, UX and tutorial workflow selection | `skills/mdcp/SKILL.md`; `skills/mdcp/references/workflows/feature-level.md` | Direct parent routing plus supplied [RT-RTE-feature-work](runtime.md#rt-rte-feature-work). UX/tutorial bodies not inspected here; specific UX artifact admission and phase-return details remain uninspected, preventing a claim of identical detailed behavior across workflows. |
| Doc-only/design, current-state editing, historical exceptions | `skills/mdcp/references/workflows/doc-only.md`, `skills/mdcp/references/workflows/design-architecture.md`, `skills/mdcp-arch-research/SKILL.md` | Direct; [MEM-OBJ-shards](#mem-obj-shards), [MEM-OBJ-research](#mem-obj-research), [MEM-RTE-shard-authoring](#mem-rte-shard-authoring). |
| Search/index selective reads; optional host fork | `skills/mdcp/SKILL.md` | Direct; annotations on [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), [RT-BAP-skill-host](runtime.md#rt-bap-skill-host). No enforced numeric token budget or host compaction implementation established. |
| Compile, refs-gen/check/list, lint, links, check | `packages/mdcp-cli/src/cli.ts`; `packages/mdcp-core/src/refs/registry.ts`, `packages/mdcp-core/src/compile/section-manifest.ts` | Direct dispatch/selection/registry; supplied assembly in [RT-RTE-compile-check](runtime.md#rt-rte-compile-check). [MEM-OBJ-compiled](#mem-obj-compiled), [MEM-OBJ-refs](#mem-obj-refs). |
| In-process raw/derived shard snapshots | `packages/mdcp-core/src/compile/shard-cache.ts` | Direct; [MEM-OBJ-shard-cache](#mem-obj-shard-cache); not itself cross-invocation memory. |
| Peer formatting mutation | `packages/mdcp-cli/src/cli.ts` | Direct; [MEM-RTE-peer-fix](#mem-rte-peer-fix). External formatter semantics not frozen. |
| Mechanical import and programmable compile hooks | `packages/mdcp-core/src/shard/orchestrator.ts`, `packages/mdcp-core/src/compile/hooks.ts` | Supplied [RT-RTE-shard-import](runtime.md#rt-rte-shard-import), [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension); separate admission from semantic authoring. |
| Sprawl review, deletion, recurrence into rules | `skills/mdcp/references/workflows/doc-review.md`; `packages/mdcp-core/src/validate/review.ts` | Direct workflow, supplied implementation [RT-RTE-doc-review](runtime.md#rt-rte-doc-review). No completed semantic criticism or durable diagnostic history observed. |
| Site publication and output backup | `packages/mdcp-site/scripts/sync-content.mjs`, `packages/mdcp-core/src/compile/write-output.ts` | Supplied [RT-RTE-compile-check](runtime.md#rt-rte-compile-check). Not independently reread here; exact page sanitization and backup retention policy remain uninspected, preventing stronger safety/expiry conclusions. |
| Session hook skill installation | `.claude/hooks/session-start.sh` | Direct; builds and installs skill, not a push of task-relevant accumulated shards. |
| Maintainer tests, evaluation, proposal history, admission/release | `.agents/skills/skill-creator/scripts/run_loop.py`, `.agents/skills/skill-creator/scripts/improve_description.py`, `.github/workflows/ci.yml` | Supplied [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation), [RT-RTE-release-admission](runtime.md#rt-rte-release-admission). Detailed grading artifacts, feedback viewer, benchmark result persistence and release rollback not inspected here; no claim of exhaustive feedback uptake or deployed skill replacement. |
| Other complementary archetype policies | `skills/mdcp-arch-product-docs-site/SKILL.md`, `skills/mdcp-arch-gtm/SKILL.md`, `skills/mdcp-arch-oss-library/SKILL.md` | Included but uninspected here; parent explicitly affords complementary skills. Their particular retained parts, trust rules and later consumers remain unresolved; research overlay findings are not generalized to them. |

## Core ideas

1. Durable content is current intent and contracts, selectively reloaded by the host agent. The selection key is the task interpreted against search results or indexes, not an embedding or a compiler-selected prompt bundle. The installed skill is static guidance; changed shards are memory when later tasks reload them. See [MEM-OBJ-shards](#mem-obj-shards) and [RT-CLM-context-discipline](runtime.md#rt-clm-context-discipline).
2. Natural-language authority and mechanical authority differ. An agent interprets shard contracts; the compiler deterministically follows config/index links, rewrites text and produces output. The refs registry is access metadata derived from headings, not the semantic content or evidence for those headings. See [MEM-OBJ-refs](#mem-obj-refs), [MEM-OBJ-compiled](#mem-obj-compiled) and [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).
3. Withdrawal normally edits current shards, while Git, ADRs and research records preserve different kinds of history. The research overlay is a counterexample to an unrestricted claim that MDCP deletes all old claims. It prescribes immutable observations and visible links from evidence to positions to clauses, not treating observations as instructions. See [MEM-OBJ-research](#mem-obj-research) and [MEM-RTE-shard-authoring](#mem-rte-shard-authoring).
4. Feedback can change durable guidance, but diagnosis is not automatic adoption. Review asks an agent to decide; formatter/import paths can write mechanically without that decision; the optimizer feeds descriptions and scores to later proposal calls but stops short of production installation. See [RT-RTE-doc-review](runtime.md#rt-rte-doc-review), [MEM-RTE-peer-fix](#mem-rte-peer-fix), [RT-RTE-shard-import](runtime.md#rt-rte-shard-import) and [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-shards
Label: Source shards and guide indexes

Source-native identity: topic `.md` shards and guide `index.md`/`shards.md` in caller repositories. Storage: filesystem files, normally Git-versioned. Form: natural-language intent, contracts, definitions and explanations for human/agent interpretation; Markdown links and ordering have an additional symbolic compiler consumption path. The content and access-order roles differ even in the same file. Initial lineage is request/repository intake and agent or human authorship, not a captured conversation transcript. Subsequent lineage includes as-built reconciliation and semantic maintenance; mechanical import is an alternative producer. Human control of each admitted sentence is unresolved: user initiation is not per-content approval.

Distinct from supplied [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp): that is vendor skill/workflow policy; these are the caller's mutable project documents. Closest routes are [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) and [RT-RTE-shard-import](runtime.md#rt-rte-shard-import). Later agent tasks are instructed to load relevant shards as contracts/current intent, while compilers use links/order. The consumer interprets what a shard says; delivery alone establishes neither compliance nor truth. Source authority is asserted by policy, not authenticated per-file provenance. Reasons for surviving constraints are shortened in the current shard and can link to an ADR; incident details and temporary planning are deliberately not retained there. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/doc-only.md`.

> - Shards under `docs/**/` are the source of truth.
> --- `skills/mdcp/SKILL.md`

> Update each guide's `index.md` for compile order.
> --- `skills/mdcp/references/workflows/doc-only.md`

> Move the history behind a rule or constraint that still holds, such as an erratum or how things worked before the rule, to an ADR and link it from the shard or standalone guide. The shard or standalone guide states today's reason in one present-tense sentence and does not link the incident log or ticket behind the change, which stays in the issue tracker.
> --- `skills/mdcp/references/workflows/doc-only.md`

#### MEM-OBJ-research
Label: Research records and derived positions

Source-native identity: `research/` dated observation records, `design-constraints/` durable positions and normative clauses prescribed by the research archetype. Storage: separate Markdown files with linked data CSV/JSON alongside where used. Form: natural-language evidence and recommendations; data encoding is symbolic and its specific semantics depend on the cited method, not inferred here. These are material content parts distinct from generic current-state shards in [MEM-OBJ-shards](#mem-obj-shards); closest supplied counterpart is [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp), the guidance that an overlay extends, not these authored results. No separate supplied record names these retained observation/position parts.

Lineage is observations/measurements → authored record → position → normative clause, with source-native confidence/method/caveat requirements. This is prescribed curation, not an automatic trace extractor or observed derivation. Authors decide what enters the record; computation producing a number is not itself human admission of a claim. Later readers can follow links to reasons, but no automatic host selector guarantees it will read underlying records before obeying a clause. Records have evidence authority, positions and clauses can guide later design; those forces are not identical. SRC-1, `skills/mdcp-arch-research/SKILL.md`.

> - **Separate observation from recommendation.** A record names the durable position it feeds and links to it. The record does not become the rule.
> - **Supersede, never overwrite.** A later measurement is a new file that links back to the one it replaces.
> --- `skills/mdcp-arch-research/SKILL.md`

> 1. The record states what was observed and what it cannot support.
> 2. The durable position cites the record by link.
> 3. The normative clause cites the position.
> --- `skills/mdcp-arch-research/SKILL.md`

#### MEM-OBJ-compiled
Label: Compiled guide and monolith documents

Source-native identity: per-guide, publish-target and monolith Markdown generated by compile. Storage: output files; optional backup of overwritten outputs. Form: natural-language prose plus symbolic Markdown headings, rewritten links and optional provenance tags. Lineage: selected shards, assembly/hook transformations and output-location-specific link rewriting. Not a model summary of raw conversational traces. Distinct from source shards and [RT-OBJ-config](runtime.md#rt-obj-config); closest supplied [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) supplies implementation and supporting passages, not an object declaration. Content reasons survive only insofar as selected source text and transformations carry them; compilation does not independently establish evidence quality.

Consumers: deterministic site generation and human published readers; broader host-agent reads are a last resort under the skill. Regeneration supersedes derived text; manual editing is forbidden by doctrine, not a write guard. Failed late checks do not withdraw already-written outputs. SRC-1, `packages/mdcp-cli/src/cli.ts`; assembly and site details supplied in [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

> const written = writeCompiledFromWorkspace(config, docsRoot, workspace);
> logWritten(written);
> const refsPath = resolveRefsPath(docsRoot, config.outputDir, config.refs.registryFile);
> genRefs(workspace, refsPath);
> if (runBuiltInLinkLint(config, docsRoot, opts, workspace)) process.exit(1);
> --- `packages/mdcp-cli/src/cli.ts`

#### MEM-OBJ-refs
Label: Refs heading registry

Source-native identity: `refs.json` (`RefsRegistry`). Storage: persisted JSON. Form: symbolic headings/slugs, output file identity and line metadata, with natural-language title display strings. It is an access/index artifact, not an opaque semantic payload, vector index or store of supporting arguments. Derivation uses compiled text and optional output-specific texts; per-output headings are slugged independently. Later CLI `refs-list` parses the saved registry and emits headings, adding output file names when available. Older top-level-only registries produce a warning and still return their headings. Site use is supplied by [RT-RTE-compile-check](runtime.md#rt-rte-compile-check). Distinct object, no supplied counterpart beyond that route.

Admission: software derives/writes it on compile, refs-gen and check; no per-heading human approval. `refs-check` compares exact serialization against fresh computed data; a check command regenerating refs first does not authenticate previously saved metadata. It cannot certify prose truth. Consumers' authority is symbolic link/discovery resolution, not normative policy adoption. SRC-1, `packages/mdcp-core/src/refs/registry.ts`, `packages/mdcp-cli/src/cli.ts`.

> export function readRefsRegistry(path: string): RefsRegistry {
>   return JSON.parse(readFileSync(path, 'utf-8')) as RefsRegistry;
> }
> --- `packages/mdcp-core/src/refs/registry.ts`

> const headings: (HeadingEntry & { file?: string })[] = registry.outputs
>   ? registry.outputs.flatMap((o) => o.headings.map((h) => ({ file: o.file, ...h })))
>   : registry.headings;
> --- `packages/mdcp-cli/src/cli.ts`

#### MEM-OBJ-shard-cache
Label: Shard snapshots

Source-native identity: `ShardCache`, absolute path → `ShardSnapshot`. Storage: process-local Map, not a persisted conversational store. Form: raw/processed natural-language text plus symbolic link provenance, slugs and anchor sets. Lineage: source file read/trim, body processing and extracted links; assembly and lint reuse derived fields. It is working computational state, not later-invocation read-back merely because its name is cache. Different persistence/consumer from [MEM-OBJ-shards](#mem-obj-shards), closest supplied [RT-RTE-compile-check](runtime.md#rt-rte-compile-check). No opaque learned payload is exposed here. Cache updates are software-controlled, not semantic approval. SRC-1, `packages/mdcp-core/src/compile/shard-cache.ts`.

> const existing = cache.get(absPath);
> if (existing) return existing;
> --- `packages/mdcp-core/src/compile/shard-cache.ts`

> export function createShardCache(): ShardCache {
>   return new Map();
> }
> --- `packages/mdcp-core/src/compile/shard-cache.ts`

### Routes

#### MEM-RTE-shard-authoring
Label: Bootstrap and document authoring

Endpoints: request/existing repository → host agent's bootstrap, doc-only or architecture workflow → source docs/indexes/config or ADRs → validation/review → future shard reads. Host agent owns content decisions; host filesystem/Git tools effect writes. This groups the shared agent-mediated admission mechanism, not all detailed workflow steps. It is distinct from [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), which includes product implementation, and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review), which begins from whole-set diagnosis. SRC-1, `skills/mdcp/references/workflows/getting-started.md`, `skills/mdcp/references/workflows/doc-only.md`, `skills/mdcp/references/workflows/design-architecture.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Plan, edited docs and review submission are requested, not an implemented MDCP response object.
- Later read-back: Later tasks discover current shards/indexes; ADR links afford rationale access, not mandatory rationale loading.
- Delegated visibility: Host-dependent isolated workflow is permitted by the parent skill; selected inputs and return schema are not specified.
- Selection predicate: Task selects workflow; intake/repo supplies scope, audience and glossary inclusion; the agent pulls needed shards and as-built code.
- Invalidation or expiry: Current-state text is replaced/deleted; superseded ADRs retain replacement links. Brownfield bootstrap preserves legacy files pending review rather than auto-deleting them.
- Activation or effect: Requested edits produce durable intent available to later consumers; actual writing, reload and behavioral change are unobserved.
- Evidence limits: These are authored workflow instructions. They do not establish universal human approval, host enforcement or successful semantic reconciliation.

Trigger: bootstrap/docs/design request. Proposed change: new or revised current shards, indexes/config, glossary and design/decision records. Proposer/decider: host agent using request/repository and as-built inspection; human can review/reject when available, while parent headless defaults permit continuation. Physical I/O is not admission judgment. Rejection includes scope deferral and retiring a superseded unbuilt design; review can withhold acceptance. Recovery is external branch/Git revision, not automatic rollback. Mode: open work requests, not oracle-scored experiments. Answer oracle: no universal prose answer; as-built code and task acceptance constrain content. Guidance is audience/job separation, current-state truth, small batches and validation; resulting content persists, with ADRs preserving reasons where prescribed.

> - Do **not** delete or overwrite legacy files.
> - Scaffold the four-tier MDCP layout **alongside** them.
> - Pull useful content into new shards.
> --- `skills/mdcp/references/workflows/getting-started.md`

> Mark a superseded ADR as superseded and link its replacement instead of deleting it, because a shard may link it for a rule's history.
> --- `skills/mdcp/references/workflows/design-architecture.md`

#### MEM-RTE-peer-fix
Label: Peer formatter mutation

Endpoints: caller invokes fix → CLI resolves Prettier/markdownlint peers → peer processes rewrite docs. CLI owns dispatch, peers own detailed transformation. Distinct from [RT-RTE-compile-check](runtime.md#rt-rte-compile-check), which derives outputs/checks rather than requesting in-place formatting, and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review), which asks for semantic decisions. SRC-1, `packages/mdcp-cli/src/cli.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Peer process effects/output; no semantic approval report or automatic compile is present in this action.
- Later read-back: Changed files can be read by future compile/check and host tasks; particular changes depend on external peers/config.
- Delegated visibility: Peers receive docs-root cwd and arguments with the process's filesystem authority, not a model context frame.
- Selection predicate: Prettier gets `--write .`; markdownlint gets `--fix` under docs root.
- Invalidation or expiry: Direct rewrites; no expiry/rollback protocol in this action.
- Activation or effect: Automatic formatting mutation is wired; successful execution and meaning preservation are unobserved.
- Evidence limits: Dependency code/results not frozen; cannot infer exact fixes or semantic safety from command names.

Admission trigger is caller invocation, not approval of each changed passage. Software admits mutations with no visible per-content veto in this action; human identity of caller remains unresolved. Mode: deterministic maintenance; answer oracle: inapplicable, no expected semantic answer is supplied. Proposed change: formatting/lint fixes; guidance is peer/config rules, not task interpretation. Recovery requires external Git/filesystem repair. This can alter retained docs but is not established trace-fed learning.

> runPeer(prettier, { cwd: getDocsRoot(opts), args: ['--write', '.'] });
> --- `packages/mdcp-cli/src/cli.ts`

> runPeer(mdlint, { cwd: getDocsRoot(opts), args: ['--fix'] });
> --- `packages/mdcp-cli/src/cli.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp)

Write agency and storage: vendor-managed Markdown policy is installed for later host discovery; project-specific guidance is directed to complementary skills/extensions/normative shards instead of vendor hand-edits. The separate mutable content is [MEM-OBJ-shards](#mem-obj-shards). Direct inspection of SRC-1, `.claude/hooks/session-start.sh` shows a remote-only session initialization path that builds and installs the checkout skill, not a retained-task summarizer. Its authority is policy delivery to the host; source text supplies neither successful installation nor compliance.

> # --- Agent Skill: install this checkout's mdcp skill, so agents use the latest ---
> pnpm run skill:dev
> --- `.claude/hooks/session-start.sh`

#### On [RT-RTE-feature-work](runtime.md#rt-rte-feature-work)

Read-back and context control: SRC-1, `skills/mdcp/SKILL.md`, directly inspected, requests discovery by task-relevant host search or guide index, then one shard. This is pull selection controlled by the foreground agent, not an unsolicited relevance push from the compiler. Budget is qualitative, one shard/workflow at a time; neither cumulative token accounting nor preferential eviction is wired by MDCP. Old turns/tool results remain host-controlled. The optional isolated workflow resembles a task frame only at the host: MDCP names no return payload, retained summary, pointer or automatic reload handle. Repository shards remain addressable through ordinary file reads. An index link is not a live reference in the model window; following it requires another tool read. No observed activation or reduced cost follows.

> Discover the relevant shard with host search (`rg`, IDE search) or the guide
> `index.md`, then open **one** `.md` shard. Broader reads of compiled output are
> last resort.
> --- `skills/mdcp/SKILL.md`

#### On [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)

Selected retained parts are source shards → output prose and heading metadata, not conversation traces → learned summaries. Direct SRC-1, `packages/mdcp-core/src/compile/section-manifest.ts` shows index Markdown links and same-guide slug-to-file matches first, then sorted directory fallback if no paths resolve. Transitive Markdown links expand within the configured scope. This compiler predicate differs from the agent's task-relevance judgment. No token budget is applied at this selection layer; output scope is not a model-window limit. Persisted refs-list reload establishes a concrete later deterministic consumer of metadata, and supplied site wiring establishes another publication consumer. No hypothetical library caller is needed for those paths. Unknown host readership is not upgraded to an observed agent recall route.

> const resolved = resolveManifestPaths(guideDir, scopedText, {});
> if (resolved.length > 0) return resolved;
> --- `packages/mdcp-core/src/compile/section-manifest.ts`

> /** Manifest sections plus shards reachable via transitive `.md` links within the guide tree. */
> --- `packages/mdcp-core/src/compile/section-manifest.ts`

#### On [RT-RTE-doc-review](runtime.md#rt-rte-doc-review)

Curation: direct SRC-1, `skills/mdcp/references/workflows/doc-review.md` confirms index-first then signal-targeted reads and sampling. A finding is input to a semantic decision, not itself accepted knowledge. Changed current shards are read later; recurring findings can shape durable thresholds, glossary and Vale rules consumed by future checks/agents. This is a prescribed experience-responsive guidance update path, not inspected automatic raw-trace extraction. The workflow requests one-line decision reasons, but does not identify a fixed durable reason store or guarantee later readers receive each reason. Distinguish reasons retained in ADRs from transient review replies. It permits leaving correct content and narrowing faulty rules; curation is not invariably deletion or increased restriction. No improvement benefit is demonstrated.

> Pick one action per finding and record why in one line:
> --- `skills/mdcp/references/workflows/doc-review.md`

#### On [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation)

Memory-specific findings supplied by runtime: raw query outcomes and labels produce scores/history, and the proposer receives current description, skill text, failures and history stripped of test-prefixed fields. This is trace-fed candidate-description revision with later proposal/evaluation consumers inside bounded iterations, not merely retained raw logs. Description prose has interpreted policy authority at the next skill-trigger consumer; scores have fixed selection authority. Optional prompt/response logs preserve more raw material than the compact history. No automatic extraction of warranted general rules or stable rationale store follows. The runtime's quoted best-description instruction requires author-applied frontmatter editing to cross into durable production policy. Human control at production installation is a further decision, not established by the optimizer's score selection. Actual exercise and generalized learning remain uninspected. Model weights and provider state remain opaque as specified in [RT-CMP-claude](runtime.md#rt-cmp-claude).

#### On [RT-RTE-shard-import](runtime.md#rt-rte-shard-import)

Alternative admission: supplied implementation mechanically imports/explodes/copies content to durable source shards and deletes destinations before rebuilding; caller source/mappings govern intake, not the interpretive content review of [MEM-RTE-shard-authoring](#mem-rte-shard-authoring). Origin is imported documents/directories, not necessarily agent experience. Future compile/host reads consume the result, but no successful read is observed. Temporary-directory cleanup is not withdrawal or rollback of partially rewritten guides.

#### On [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension)

Transformation and authority: supplied callback wiring can replace compiled bodies before publication. Registration is process-local executable symbolic state; only output text becomes durable by writing. Arbitrary callbacks mean default compilation's exact content preservation cannot be generalized to every exposed core call. No callback trace-learning algorithm, admission semantics or provenance guarantee can be inferred without its supplied implementation.

## Write side

The durable write mechanisms have different controls. Agent authoring uses intake, repository/code inspection and task acceptance; host tools perform the I/O, and human review is conditional, not universal. Bootstrap seeds structure and chosen glossary terms while preserving legacy material pending review. Doc-only/design paths and feature work admit natural-language contracts before later checks; these are not runtime-enforced semantic gates. See [MEM-RTE-shard-authoring](#mem-rte-shard-authoring) and [RT-RTE-feature-work](runtime.md#rt-rte-feature-work).

Mechanical import admits source-derived shards from mappings. Formatting admits peer-selected changes without per-content review in its action. Compiler hooks can transform derived output; compile and check persist outputs/refs before later failures, so diagnostic rejection is not transactional withdrawal. Source updates, regenerated derivatives, old backups and saved registry freshness are separate states. See [RT-RTE-shard-import](runtime.md#rt-rte-shard-import), [MEM-RTE-peer-fix](#mem-rte-peer-fix), [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension) and [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

Semantic maintenance makes deletions, splits, moves and canonical links, then repeats checks. Superseded current text leaves the primary read path; Git can retain old wording, ADRs retain live-rule history, and research records preserve dated observations instead of being edited into today's claim. No automatic expiry clock or guarantee that future agents consult old reasons is established. The research overlay's evidence → position → clause chain is deliberately different from dumping raw logs into durable docs. See [MEM-OBJ-shards](#mem-obj-shards), [MEM-OBJ-research](#mem-obj-research) and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review).

Trace-derived behavior-shaping state is clearest in the supplied optimizer: trigger outcomes → score/history/failure inputs → candidate description → next evaluation/proposal. That bounded loop has an actual next consumer in code, unlike mere archival of a report. Its final result still needs separate production editing/admission. Review recurrence → thresholds/glossary/Vale is a prescribed analogous path, not evidence of executed improvement. Neither route establishes model-weight learning. No MDCP conversational compaction/checkpoint substitution is established by the inspected mechanisms; opaque host storage remains a limit, not an evidenced absence. See [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) and [RT-RTE-doc-review](runtime.md#rt-rte-doc-review).

## Read-back

| Later consumer | Trigger, selection, delivery and authority | Status and limits |
| --- | --- | --- |
| Foreground or optional isolated host agent | Task interpretation → host search/index → selected shard/workflow file reads; interpreted current contracts/instructions. Qualitative smallest-context guidance, no numeric budget. | Claimed protocol; actual delivery/activation unobserved. [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), [RT-BAP-skill-host](runtime.md#rt-bap-skill-host). |
| Compile/check invocation | Caller command → configured guides, index-linked and reachable shards/directory fallback → full text plus deterministic metadata/rewrites. | Wired implementation, operation uninspected. [RT-RTE-compile-check](runtime.md#rt-rte-compile-check), [MEM-OBJ-shard-cache](#mem-obj-shard-cache). |
| Refs-list | Caller command → stored registry → per-output heading JSON/table or old-format top-level headings. No task-targeted content retrieval or prose reasoning. | Wired implementation, operation uninspected. [MEM-OBJ-refs](#mem-obj-refs). |
| Site generator and published readers | Site preparation → refs/compiled/source files → derived pages/navigation. Reader selection and actual agent readership unknown. | Supplied wired consumer, not observed publication/behavior. [RT-RTE-compile-check](runtime.md#rt-rte-compile-check). |
| Reviewer / later check | Explicit/sprawl/external weekly trigger → indexes, signal-targeted shards, sample rest; edited docs and tuned rules can reach future readers/checks. Evidence record for weekly runs is prescribed, not assumed present. | Afforded workflow; semantic decisions unobserved. [RT-RTE-doc-review](runtime.md#rt-rte-doc-review). |
| Next optimizer proposal/evaluation; later installed host skill | Bounded iteration selects current description and train failures/history; test fields blinded from proposer; output candidate requires further author editing to install. | Wired bounded feedback, not observed production self-change. [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation). |

The session-start installer is automatic policy setup, not an automatic selector pushing accumulated task material. Available files and public read/write APIs alone do not establish additional deployed consumers. Host compaction, window trimming and child-return visibility remain external and uninspected. The memory-management analogy therefore fits optional host frames only loosely: source documents are addressable outside context, but MDCP neither tracks their window liveness nor provides dereference/eviction machinery. SRC-1, `skills/mdcp/SKILL.md`, `.claude/hooks/session-start.sh`; [RT-RTE-feature-work](runtime.md#rt-rte-feature-work).

## Integration issues

- No supplied fact is corrected. In particular, current-doc withdrawal is scoped: the supplied runtime's deletion account is compatible with preserved Git history; direct research/design reads add explicit immutable-record and superseded-ADR exceptions, not a contradiction. [MEM-OBJ-research](#mem-obj-research), [MEM-RTE-shard-authoring](#mem-rte-shard-authoring), [RT-RTE-feature-work](runtime.md#rt-rte-feature-work).
- No proposed duplicate declarations. New source/derived/index/cache objects describe concrete parts not separately declared by runtime. Authoring excludes feature implementation and whole-set review; peer fix is separate direct mutation. Policy remains [RT-OBJ-mdcp](runtime.md#rt-obj-mdcp); existing compile/import/review/evaluation/hook referents receive annotations rather than replacement records.
- Other archetype policies, detailed UX/tutorial admissions, evaluator grading/viewer/benchmark persistence and precise site/backup policy remain included inspection limits as named in the coverage table. They prevent exhaustive claims across all complementary rules and feedback products, not the positive routes established here.
- Host-specific skill discovery, fork inputs/return, conversational storage/compaction and permission grants remain uninspected dependencies. Thus the protocol cannot be promoted to an enforced window-budget, reliable recall, trust-boundary or autonomous semantic maintenance guarantee. [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), [RT-BAP-skill-host](runtime.md#rt-bap-skill-host).
- Actual per-content human approval, rationale consultation, optimizer installation, improved future capacity and successful withdrawal from deployed publication are not established without run evidence. A later route exists where code or documentation identifies one; activation and benefit remain distinct. [MEM-RTE-shard-authoring](#mem-rte-shard-authoring), [RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation), [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

## Limitations and checks

This is source analysis, not a target execution. No target, tests, examples, dependency installation, evaluator or provider call was run. The source pin and supplied run identity were rechecked against boundary/runtime; source identity is unchanged. The worker procedure, member types and complete record contract were read; truncated continuations of mandatory input reads were recovered. Newly inspected source paths stay within SRC-1; the evidence layer is implementation or doctrine/design as specified above, never observed operation. Unknown initial content control and opaque external model state are retained locally rather than converted into system-wide negatives.

Deterministic validation: passed with the assigned role/artifact command. This establishes content/quotation form, not semantic completeness, exercised behavior or benefit.
