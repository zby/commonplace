---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MemWiki memory: model-maintained Markdown, hot-first read-back, raw-source synthesis and chat maintenance at the frozen source boundary."
run-id: AAS-2026-10-14-memwiki-79dcc4d04bcb-01
source-identity: "https://github.com/hereisSwapnil/memwiki"
reviewed-boundary: "8034a3da991ac2639b87875172a9572903ecf1d5"
---

# MemWiki memory report

## Boundary and evidence

MemWiki persists project context in local files and instructs an external coding agent to maintain and reload it. This report includes both scaffold executables, all three host hooks, the installed protocol, seven retained wiki pages, raw-source admission instructions and ingest/lint/fold maintenance. SRC-1 is the frozen Git source registered in [boundary](boundary.md#source-register). Direct reads covered `src/index.ts`, `src/index.js`, `AGENTS.md`, `README.md`, `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`, `package.json` and every tracked `.memory/wiki/` page. HEAD was rechecked against the full reviewed revision; the checkout was clean and read-only. Tree enumeration checked alternative shipped paths.

Implementation evidence establishes deterministic scaffolding, not a model-run memory service. Protocol and read-back conclusions are doctrine/design evidence; the ingestion log is reported operation. No observed host execution or causal experiment is supplied. External host parameters, instruction precedence, compaction, file-tool approvals, deployed npm bytes and dependency implementation are outside the supplied boundary. These exclusions prevent conclusions about actual consumption, enforceable raw immutability, model-window eviction or improved performance. Ancillary maps and build metadata remain covered by the supplied boundary/runtime account rather than fresh inspection here.

| Included operation or part | Source path | Coverage and evidence basis | Limit |
| --- | --- | --- | --- |
| Init and protocol replacement | `src/index.ts`, `package.json` | Direct reads; [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update) | Existing wiki is skipped; missing wiki files can be seeded. Published artifact unverified. |
| Alternate generated scaffold | `src/index.js` | Direct read; [RT-RTE-legacy-init](runtime.md#rt-rte-legacy-init) | Older instructions omit scaling and maintenance commands; not the declared package bin. |
| Host delivery | `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md` | Direct reads; [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | Discovery/compliance remains external. |
| Hot-first and domain read-back | `AGENTS.md`, `.memory/wiki/hot.md`, `.memory/wiki/index.md` | Direct reads; [RT-RTE-agent-session](runtime.md#rt-rte-agent-session), [MEM-OBJ-hot](#mem-obj-hot), [MEM-OBJ-index](#mem-obj-index) | Model judges insufficiency; no enforced budget. |
| Domain content and rationale | `.memory/wiki/stack.md`, `.memory/wiki/patterns.md`, `.memory/wiki/bugs.md`, `.memory/wiki/decisions.md` | Direct reads; [MEM-OBJ-domain-pages](#mem-obj-domain-pages), [MEM-OBJ-decisions](#mem-obj-decisions) | Bugs is a starter page; populated prose is not verified knowledge. |
| Raw acquisition and synthesis | `AGENTS.md`, `README.md`, `src/index.ts` | Direct reads; [MEM-OBJ-raw](#mem-obj-raw), session annotation | No tracked raw input bundle; actual synthesis lineage unknown. |
| Work summaries and task-end checkpoint | `AGENTS.md`, `.memory/wiki/log.md`, `.memory/wiki/hot.md` | Direct reads; [MEM-OBJ-log](#mem-obj-log), session annotation | No verbatim transcript or alternate machine checkpoint specified. |
| Repository ingestion | `AGENTS.md`, `.memory/wiki/log.md` | Direct reads; [MEM-RTE-repository-ingest](#mem-rte-repository-ingest) | Claimed scan differs from complete-tree evidence. |
| Health evaluation and fixes | `AGENTS.md`, `README.md` | Direct reads; [MEM-RTE-wiki-lint](#mem-rte-wiki-lint) | Protocol asks proposals; README promises fixing. No evaluator result supplied. |
| History condensation | `AGENTS.md`, `.memory/wiki/log.md` | Direct reads; [MEM-RTE-log-fold](#mem-rte-log-fold) | No before/after summary or preservation audit. |
| Provider context/parameters | `README.md`, `AGENTS.md` | Supplied [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent) plus direct instruction reads | Opaque host state; MemWiki does not specify selection inside that state. |

## Core ideas

The two-tier read policy is hot first, then a directory and relevant domain pages when the foreground agent finds hot context insufficient. This is requested model-directed file selection, not an executable retrieval ranker or automatic push service. The approximately 500-word description is guidance, not a truncation rule. SRC-1, `AGENTS.md`, `README.md`; [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol).

> 1. **The Hot Cache (`hot.md`)**: Agents read this file *first*. It contains immediate, short-term context (~500 words). It tells the agent exactly what was being worked on and the immediate next steps.
> --- `README.md`

The substantive memory is derived prose. Work discoveries and source documents are synthesized into domain content; current work becomes a hot checkpoint and a timestamped summary. Later agents are asked to use these files, but no supplied execution proves that delivered content changed a decision. Neither accumulation nor refinement establishes improved capacity. SRC-1, `AGENTS.md`; [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).

Maintenance is likewise a model-interpreted workflow. Ingest adds knowledge; lint diagnoses and proposes; fold replaces older history with a summary. “Append-only” and “never delete knowledge” therefore express semantic preservation intent, not byte preservation. The retained repository exposes stale/inconsistent claims, so curation cannot be treated as validation. SRC-1, `AGENTS.md`, `.memory/wiki/log.md`, `.memory/wiki/stack.md`, `package.json`.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-hot
Label: Hot cache

Source-native identity: `.memory/wiki/hot.md`. Storage: project-local UTF-8 Markdown; form: natural-language state and task guidance, with checklist notation interpreted by the model rather than enforced by MemWiki. Lineage: seeded by the CLI; later refresh requested at session/task end or impending context loss. The frozen page reports ingestion completion but still lists initial scope/stack setup tasks. It is derived context, not a raw transcript or opaque checkpoint. Its later consumer is the foreground coding agent, requested to read it first. Authority is project context/next-step guidance, subject to host precedence. No TTL, provenance schema or hard size cap is specified. Distinct from [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files): this is mutable project content, not the installed workflow. SRC-1, `.memory/wiki/hot.md`, `src/index.ts`, `AGENTS.md`.

> - Successfully completed `/memwiki-ingest`, populating the wiki with stack details, coding patterns, and architectural decisions.
> --- `.memory/wiki/hot.md`

#### MEM-OBJ-index
Label: Wiki directory

Source-native identity: `.memory/wiki/index.md`. Storage: local Markdown. Form: natural-language directory labels and wiki-style path links; MemWiki supplies no link resolver executable. Lineage: fixed initial directory, requested agent additions when new pages are created. This is access/routing metadata, not the domain knowledge it references. Consumer: agent needing more than hot context; authority: candidate navigation, not content approval. Different from [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files), which requests navigation, and from hot, which supplies initial task context. SRC-1, `.memory/wiki/index.md`, `AGENTS.md`.

> - If you create a new file, you MUST add a link to it in `.memory/wiki/index.md`.
> --- `AGENTS.md`

The frozen index enumerates the six other starter pages. It does not contain the landscape/competitor links claimed in the work log. That mismatch prevents trusting the log as an inventory of reachable retained material. SRC-1, `.memory/wiki/index.md`, `.memory/wiki/log.md`.

#### MEM-OBJ-domain-pages
Label: Stack, patterns and bugs pages

Source-native identities: `.memory/wiki/stack.md`, `.memory/wiki/patterns.md`, `.memory/wiki/bugs.md`. Storage: project-local Markdown; form: human/model-readable natural-language claims and code-name examples, not a machine-enforced configuration. These pages share requested agent synthesis/refinement admission and index-mediated consumers. They are kept distinct here from the rationale-bearing decisions page and from routing metadata. No supplied runtime object denotes these contents; closest counterpart [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) is their producer/consumer route, not their identity. SRC-1, the three page paths above, `AGENTS.md`.

Stack and patterns contain concrete tool/convention descriptions; bugs contains only a heading and authoring instruction. The log attributes population to repository ingestion, but original model processing and input-to-sentence lineage are unavailable. Later consumers are agents consulting relevant domains; authority is project knowledge and convention guidance. The stack's zero-dependencies assertion conflicts with package metadata, so neither maintained prose nor a domain label establishes truth. SRC-1, `.memory/wiki/stack.md`, `.memory/wiki/patterns.md`, `.memory/wiki/bugs.md`, `.memory/wiki/log.md`, `package.json`.

> - **Zero Dependencies**: The project explicitly avoids runtime dependencies (only `@types/node` and `typescript` as devDependencies) to ensure zero friction and high security/stability.
> --- `.memory/wiki/stack.md`

#### MEM-OBJ-decisions
Label: Architectural decisions

Source-native identity: `.memory/wiki/decisions.md`. Storage: local Markdown; form: natural-language decisions plus explicit rationale. Lineage: starter authoring guidance, later populated text attributed to ingestion in log. Four ADRs cover dependencies, synchronous I/O, hardcoded templates and safe updates. Different from [RT-CLM-safe-update](runtime.md#rt-clm-safe-update): that record assesses a particular README claim; this object is the retained decision/rationale page, including three other decisions. Not part of the protocol-file object. SRC-1, `.memory/wiki/decisions.md`, `.memory/wiki/log.md`, `src/index.ts`.

> - **Rationale:** It simplifies the build process. If we used external template files, the TypeScript build step would also need to copy those non-TS files to the `dist/` directory before publishing to NPM. Hardcoding them avoids complex build scripts.
> --- `.memory/wiki/decisions.md`

Reasons thus survive for some domain guidance and can reach an index-selected later agent. No instruction guarantees that a later decision consults those reasons, or that all synthesized claims retain rationale, alternatives or source references. Consumer authority is advisory architectural knowledge, not CLI enforcement. Actual dependence and correctness remain unobserved. SRC-1, `AGENTS.md`, `.memory/wiki/index.md`, `.memory/wiki/decisions.md`.

#### MEM-OBJ-log
Label: Work log

Source-native identity: `.memory/wiki/log.md`. Storage: local Markdown; form: natural-language work summaries with textual dates. Lineage: CLI setup entry, then requested agent-authored session summaries; frozen ingestion entry is reported operation. This is already derived history, not a raw tool trace. Fold may derive a further summary from it. Later consumers: fold's summarizing agent, and potentially task agents selecting it through index. Unlike hot, direct reading at every session is not required. No supplied runtime object names the retained history itself; [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands) is its maintenance route. SRC-1, `.memory/wiki/log.md`, `.memory/wiki/index.md`, `AGENTS.md`.

> - Updated `index.md` to link to the new `landscape.md` and `competitors.md` files.
> --- `.memory/wiki/log.md`

Those files are not tracked at the frozen revision and the frozen index has no such links. The record supports an attributed report, not verified production history. No raw transcript, immutable event ID, fold revision or prior-version pointer is retained in this page. SRC-1, `.memory/wiki/log.md`, `.memory/wiki/index.md`; frozen tracked-tree enumeration.

#### MEM-OBJ-raw
Label: Raw source documents

Source-native identity: `.memory/.raw/`. Storage: project filesystem directory created by CLI; document encoding is input-specific (README examples include PDFs, gists and meeting notes). No actual raw file is tracked here, so representational form and provenance of a deployed payload are unresolved, not assumed Markdown or natural language throughout. Consumer-visible derived display is wiki prose; that does not establish complete coverage of an input's opaque or binary contents. Human-supplied documents are distinguished from agent-authored wiki output. Closest supplied [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) describes the route, not the retained input object. SRC-1, `src/index.ts`, `README.md`, `AGENTS.md`.

> 3. If the user drops new API docs, PDF specs, or gists into `.memory/.raw/`, read them to understand the new information, but **never modify the files in `.raw/`**.
> --- `AGENTS.md`

Admission of source files is assigned to the human; synthesis admission is assigned to the agent, without sentence-level approval. Raw originals have declared source-of-truth status and requested immutability, not enforced permissions. No automatic watcher, raw-file expiry, provenance index or invalidation propagation is specified by the inspected CLI/protocol. Initial content, extraction completeness and deployed host access remain unknown. SRC-1, `README.md`, `AGENTS.md`, `src/index.ts`.

### Routes

#### MEM-RTE-repository-ingest
Label: Repository ingestion
Part of: [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands)

This is the ingest branch of the supplied combined chat-maintenance route, not another dispatch mechanism. User chat request → foreground model interprets protocol → scans repository → selects findings → writes stack/patterns/decisions. Owner/executor: external agent using host file tools; context/state: repository and available task context. Effect: derived retained project knowledge. SRC-1, `AGENTS.md`, `.memory/wiki/log.md`.

- implementation conclusion status: claimed
- operation conclusion status: claimed
- Immediate return: Requested page population and host response; no result schema.
- Later read-back: Written domains may reach later tasks through hot/index navigation; actual reads are unobserved.
- Delegated visibility: uninspected — host delegation is not specified.
- Selection predicate: User enters `/memwiki-ingest`; model chooses findings from the requested entire-repository scan.
- Invalidation or expiry: Subsequent refinement/lint is requested; no automatic invalidation or expiry.
- Activation or effect: The log reports ingestion and populated pages exist; no trace shows resulting behavioral dependence.
- Evidence limits: Reported operation does not prove scan completeness or accurate transformation.

Admission: human initiates request, model proposes/selects and physically writes; initiation is not per-content approval. Operating mode: open maintenance request. Guidance is the repository findings and protocol's target pages. No independent answer oracle, required approval gate, content rejection criterion or rollback procedure is supplied; human veto remains host-dependent. Existing file preservation in CLI does not constrain this writer. SRC-1, `AGENTS.md`; the passage supporting this branch is retained in [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands).

#### MEM-RTE-wiki-lint
Label: Wiki health check
Part of: [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands)

User chat request → agent reads wiki → judges outdated information, missing hot context and empty domains → proposes fixes. Owner/executor: foreground host agent; context: retained wiki and whatever comparison evidence the host gathers. This branch evaluates/proposes, unlike ingest's direct population and fold's requested replacement. SRC-1, `AGENTS.md`, `README.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Health findings and proposed fixes under the protocol; README describes fixing instead.
- Later read-back: Proposals alone have no required retained consumer; if admitted as edits, revised pages can enter the ordinary session route.
- Delegated visibility: uninspected — no delegated evaluator specified.
- Selection predicate: `/memwiki-lint` triggers model selection of the named health issues.
- Invalidation or expiry: Outdated content is to be diagnosed; no rule automatically expires or quarantines it.
- Activation or effect: Requested evaluation is present; no inspected result demonstrates correction or withdrawal.
- Evidence limits: No evaluation trace, scoring rule, expected answers or mandated fix-acceptance step.

Admission: user chooses diagnosis; model chooses criticisms/proposals. Protocol does not explicitly admit all proposals as edits. README's stronger fixing language leaves that transition unresolved. Mode: open health request, not controlled experiment. No reference-answer provider or independent oracle; human decision/veto after proposal is unspecified. Guidance persists as protocol; any accepted edits persist only if host writes them. No rollback, audit or content-level rejection mechanism is supplied. SRC-1, `AGENTS.md`, `README.md`; [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands).

#### MEM-RTE-log-fold
Label: Work history condensation
Part of: [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands)

User chat request → foreground agent selects older log entries → synthesizes a paragraph → condenses retained history. Owner/executor: host agent/file tools; context/state: existing log and protocol's crucial-history criterion. The trace-fed chain is work → initial work summary → folded summary → potential future index-selected reader. It starts from already summarized history, not a demonstrated raw transcript. SRC-1, `AGENTS.md`, `.memory/wiki/log.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested condensed log/history and host response.
- Later read-back: Folded log remains reachable through index, but no next session is required to read it.
- Delegated visibility: uninspected — host worker contexts are unspecified.
- Selection predicate: `/memwiki-fold`; model selects older log entries and crucial history.
- Invalidation or expiry: Old detail is condensed without defined age cutoff or mandatory backup.
- Activation or effect: Replacement is requested, not demonstrated; preserved meaning and changed later behavior are unobserved.
- Evidence limits: No before/after fold artifact, preservation test or downstream read trace.

Admission: user initiates; model determines content and replacement, without required human approval. Mode: open maintenance request. Guidance: limit log growth while preserving crucial history; no independent oracle evaluates that preservation. User/host veto and recovery depend on external facilities; protocol mandates neither version backup nor rollback. Reasons may be dropped unless selected as crucial; retention of rationale is not guaranteed. Fold modifies external durable history, not already loaded host turns. SRC-1, `AGENTS.md`; exact command passage is in [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands).

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files)

Write control is operator launch plus fixed-template software admission for initialization/replacement, not model curation of project memory. Existing hooks can survive init without routing to the wiki; update overwrites local protocol customizations. These retained instructions direct memory consumption but static installation alone is not read-back of accumulated experience. SRC-1, `src/index.ts`; supporting passages in [RT-RTE-cli-init](runtime.md#rt-rte-cli-init) and [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update).

#### On [RT-RTE-agent-session](runtime.md#rt-rte-agent-session)

Memory read-back is requested pull: foreground agent reads hot based on session/task entry; uses its current task/context and judgment of insufficiency to read index and relevant domains. Hot supplies state/next steps, index supplies locations, selected domains supply content and sometimes rationale. Delivery is host file reading into the model-visible context. Hook discovery initiates the obligation but is not itself independent push selection of retained content. Persistence is project files between tasks/sessions; host prompt retention is opaque. SRC-1, `AGENTS.md`, `CLAUDE.md`, `.memory/wiki/index.md`; [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol).

Write agency is agent synthesis/refinement after work discoveries or user-supplied raw documents. Physical writes require host file tools; no per-content human approval is stated. The source of work-derived memory includes coding experience and repository observations; raw synthesis instead begins with human-supplied documents of unresolved payload form. Initial setup supplies starter text rather than experience. No automatic transcript-to-memory model call is wired by MemWiki; the foreground model is instructed to perform the transformation. Task-end hot refresh and log append are alternative derived retained outputs, not resumable model checkpoints. SRC-1, `AGENTS.md`, `src/index.ts`.

> - Synthesize any raw knowledge from `.memory/.raw/` into the wiki pages.
> - Never delete knowledge from the wiki. Only append or refine.
> --- `AGENTS.md`

Selection budget: README suggests approximately 500 words for hot; protocol gives no quantitative domain/file limit. No context frame isolation, eviction or selective host-turn compaction is specified by these inspected sources. Impending context loss is a write trigger, not an enforced interception. After host context disappears, external hot/index/domain files remain potentially reloadable; prior turns and tool results have no MemWiki reload guarantee. The file pointers permit later explicit reading, not live references inside a model window. SRC-1, `README.md`, `AGENTS.md`, `src/index.ts`.

#### On [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol)

Hot and protocol are presented as primary project truth by the Claude hook; domain pages gain context authority through conditional navigation. That priority remains natural-language guidance at an external consumer, not a permission or correctness boundary. Reasons retained in decisions can be delivered along with claims, whereas log summaries and hot state need not retain reasons or source provenance. Update modifies the instruction-delivery side; agent wiki edits modify selected context. No observed decision establishes activation of either change. SRC-1, `CLAUDE.md`, `AGENTS.md`, `.memory/wiki/decisions.md`; supplied hook passage in [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).

## Write side

The CLI seeds absent pages from authored templates and mechanically replaces only protocol files on update. Human launch chooses the project and installation; it does not review individual contents. Existing files reject init replacement by existence alone, even if stale or unrelated. Missing knowledge pages are recreated as starters, not restored from a prior checkpoint. The alternate generated CLI uses the same basic seeding approach with older instructions. SRC-1, `src/index.ts`, `src/index.js`; [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update), [RT-RTE-legacy-init](runtime.md#rt-rte-legacy-init).

Thereafter admission is chiefly foreground-model selection. User-supplied raw originals → agent interpretation → domain prose; work discoveries → patterns/bugs/decisions; task state → refreshed hot; work history → timestamped log summary. All results persist locally; the protocol does not require source anchors, reasons for every claim or an independent acceptance decision. Decisions explicitly retain some rationale, but the lineage of their authored sentences is reported rather than traced. SRC-1, `AGENTS.md`, `.memory/wiki/decisions.md`, `.memory/wiki/log.md`; session annotation and operative-object records above.

Ingest, lint and fold are separate maintenance branches with different effects and admission boundaries. Lint may leave only proposals. Fold explicitly permits textual replacement despite append-only labels. No inspected protocol supplies a rejected-content ledger, automated quarantine, source-withdrawal propagation or semantic preservation check. This bounded observation concerns the included CLI/protocol, not unknown host/version-control facilities. It prevents treating raw immutability, append-only logs or refinement as enforced guarantees. SRC-1, `AGENTS.md`, `src/index.ts`; [MEM-RTE-repository-ingest](#mem-rte-repository-ingest), [MEM-RTE-wiki-lint](#mem-rte-wiki-lint), [MEM-RTE-log-fold](#mem-rte-log-fold).

## Read-back

The evidenced later-consumer role is the external project coding agent, not an unspecified storage API caller. The protocol affords a cross-session route: changed hot is requested first; changed index can route to changed domain content when context is insufficient. Raw sources may also be reread after user delivery, but unchanged raw originals are not derived work memory. The log is reachable through index and explicitly consumed by fold; it has no universal session-start read mandate. SRC-1, `AGENTS.md`, `.memory/wiki/index.md`, `README.md`; [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).

Selection uses task context and foreground judgment; MemWiki implements neither ranking, embeddings, automatic relevant-part injection nor enforced maximum file size in the inspected CLI/protocol. Calling root hooks automatic front doors is a discovery claim, not evidence of unsolicited context supply by a MemWiki selector. Folding can reduce future file reads, but does not remove already loaded material from host context. Opaque host selection, compaction and worker isolation remain unresolved. No execution establishes that any retained artifact affected the later agent's work or improved capacity. SRC-1, `src/index.ts`, `AGENTS.md`, `README.md`; [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent).

## Integration issues

- No correction to the supplied runtime's mechanism account is needed. New branch records are explicit parts of its combined maintenance route, not competing declarations. All new operative objects have no supplied object counterpart; comparisons are retained in each declaration.
- The log says landscape/competitor pages were created and indexed, but neither pages nor links exist in the frozen tracked tree/index. This is a discrepancy in reported production history, not missing available source material. It prevents interpreting the log as proof of full retained coverage. SRC-1, `.memory/wiki/log.md`, `.memory/wiki/index.md`; [MEM-OBJ-log](#mem-obj-log), [MEM-OBJ-index](#mem-obj-index).
- Stack/decisions/log assert dependency-free operation; package metadata declares a runtime dependency. Runtime already identifies the package conflict; this report localizes its retention in future context. It is unknown whether a later agent would correct or propagate it. SRC-1, `.memory/wiki/stack.md`, `.memory/wiki/decisions.md`, `package.json`; [MEM-OBJ-domain-pages](#mem-obj-domain-pages), [MEM-OBJ-decisions](#mem-obj-decisions).
- Lint's proposal-versus-fix transition is unresolved between protocol and README. No supplied result settles whether proposed corrections are retained. This prevents promoting diagnosis into admitted corrected knowledge. SRC-1, `AGENTS.md`, `README.md`; [MEM-RTE-wiki-lint](#mem-rte-wiki-lint), [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands).
- The frozen hot page combines completed ingestion with initial setup next steps. Source alone does not settle whether those tasks are intentionally outstanding or stale. This prevents asserting successful hot freshness. SRC-1, `.memory/wiki/hot.md`; [MEM-OBJ-hot](#mem-obj-hot).
- Host discovery, approval controls, context retention, model version/parameter mutability and actual reading remain unresolved external responsibilities, not alternative internal stores silently omitted. Missing raw examples and original traces prevent detailed lineage and transformation-completeness claims. SRC-1, `AGENTS.md`, `README.md`; [MEM-OBJ-raw](#mem-obj-raw), [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent).

## Limitations and checks

The source identity and frozen HEAD matched the supplied boundary; no new source ID or evidence layer was added. Scope followed runtime routes and was checked against executable dispatch, all hooks, maintenance instructions and tracked wiki inventory. Strong claims were challenged using the generated CLI variant, conditional read policy, missing reported pages, package dependency contradiction, fold replacement and lint proposal wording. No target execution, installation, test or provider call was performed.

Observed activation, cross-session improvement, complete ingestion, rationale-preserving fold and reliable compliance remain unestablished. Deterministic validation is run on this candidate through the supplied invocation; a successful result checks form, identities, citations and quotation occurrence, not factual truth or acceptance.

Validation: passed with the supplied validate-output command.
