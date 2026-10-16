---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MemWiki epistemic routes: source synthesis, wiki reliance, health proposals and history condensation at the frozen commit."
run-id: AAS-2026-10-14-memwiki-79dcc4d04bcb-01
reviewed-boundary: "8034a3da991ac2639b87875172a9572903ecf1d5"
---

# MemWiki epistemic report

## Source-and-claim boundary

The question is how MemWiki turns project material into retained assertions, checks those assertions and licenses later reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identity and layers: see the [Source register](boundary.md#source-register), SRC-1. This report directly inspected the source paths below at the registered revision; runtime findings are supplied context, not substituted for those reads. No target execution occurred. No new source or evidence layer is introduced.

MemWiki's executable installs text; its continuing epistemic routes are instructions to an external agent. The relevant public claims are [EPI-CLM-project-memory](#epi-clm-project-memory), [EPI-CLM-primary-truth](#epi-clm-primary-truth), [EPI-CLM-health-fixes](#epi-clm-health-fixes) and [RT-CLM-safe-update](runtime.md#rt-clm-safe-update). The model component remains opaque: see [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent). Missing host implementation prevents conclusions about actual discovery, compliance, approvals or weight changes. Missing raw inputs and model traces prevent reconstruction of individual synthesis edges. Missing execution comparisons prevent benefit and causal attribution. Missing npm artifact prevents installed-byte equivalence.

| Entry point or operation | Source path directly read, SRC-1 | Covering records or bounded exclusion |
| --- | --- | --- |
| Declared CLI and build selection | `package.json`, `src/index.ts` | [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update); build configuration supplied through runtime, not directly reread |
| Alternate executable | `src/index.js` | [RT-RTE-legacy-init](runtime.md#rt-rte-legacy-init); init only, older protocol |
| Host hooks | `.cursorrules`, `CLAUDE.md`, `.github/copilot-instructions.md` | [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol), [EPI-CLM-primary-truth](#epi-clm-primary-truth) |
| Raw-source reading, discoveries, hot/log writes, page/index organization | `AGENTS.md`, `src/index.ts` | [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) |
| Repository ingestion | `AGENTS.md`, `README.md` | [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands) |
| Health checking and proposed fixes | `AGENTS.md`, `README.md` | [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) |
| History condensation | `AGENTS.md`, `README.md` | [EPI-RTE-log-fold](#epi-rte-log-fold) |
| Retained statements and routing | `.memory/wiki/hot.md`, `.memory/wiki/index.md`, `.memory/wiki/stack.md`, `.memory/wiki/patterns.md`, `.memory/wiki/bugs.md`, `.memory/wiki/decisions.md`, `.memory/wiki/log.md` | [EPI-OBJ-hot](#epi-obj-hot), [EPI-OBJ-domain-pages](#epi-obj-domain-pages), [EPI-OBJ-log](#epi-obj-log), [EPI-OBJ-index](#epi-obj-index) |
| External model/tool implementations and published distribution | Boundary exclusions | No claim about their evaluators or runtime behavior; prevents deployment-complete conclusions |

CLI dispatch admits only `init` and `update`; there is no registered executable slash-command tool in either inspected executable. Lint and fold are nevertheless material shipped operations because the installed protocol requests them. Available protocol and maintenance paths were assessed, including the strongest counterexample to a blanket “no checking” claim: lint explicitly requests a health evaluator. The absence conclusion below concerns an explicit acceptance decision, not all possible model checking.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files) | Mostly obligations, not truth-apt updates; project-memory assertions also occur | see record | SRC-1, `AGENTS.md`, `CLAUDE.md` | Instructions confer requested priority, not warranted truth |
| [EPI-OBJ-hot](#epi-obj-hot) | Project initialized; ingestion completed; next steps are policy/task content | see record | SRC-1, `.memory/wiki/hot.md` | Ingestion success is reported, not independently checked |
| [EPI-OBJ-domain-pages](#epi-obj-domain-pages) | Stack facts, CLI patterns, decisions and rationale; bugs page has no bug instance | see record | SRC-1, `.memory/wiki/stack.md`, `.memory/wiki/patterns.md`, `.memory/wiki/decisions.md`, `.memory/wiki/bugs.md` | Assertions are available; production and acceptance provenance unknown |
| [EPI-OBJ-log](#epi-obj-log) | Work and ingestion assertions | see record | SRC-1, `.memory/wiki/log.md` | Historical report is not an execution trace |
| [EPI-OBJ-index](#epi-obj-index) | Page descriptions and links | see record | SRC-1, `.memory/wiki/index.md` | Routing is not evidence validation |
| Raw documents | Potential external facts; concrete content not determinable | Source of truth in README | SRC-1, `README.md`, `AGENTS.md` | No tracked raw example; cannot assess source truth or a concrete import |
| [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent) | Parametric knowledge not individuated | see record | SRC-1, `README.md` | Model version, endpoint and parameter changes remain uninspected |

## Authority-route ledger

Fields owned by cited records say see; the local classifications below assess separate consequential functions, not replacement route identities. For natural-language routes, “doctrine only” means the requested action is present, not that the host reliably performs it.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), [RT-RTE-legacy-init](runtime.md#rt-rte-legacy-init) | content transformation | implemented | Protocol and starter pages | truth-apt transformation: acquisition/import | Fixed template to file | Destination existence, filesystem domain | see records | see records | Exact UTF-8 write or skip, not truth check | Source text preserved; source warrant unknown | Installs requested future instructions and starter assertions | see records and [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | SRC-1, `src/index.ts`, `src/index.js` | [EPI-CLM-project-memory](#epi-clm-project-memory) | none | Starter assertion can be false if files predate current invocation |
| [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update) | behavior/policy adaptation | implemented | [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files) | non-truth-apt policy/content update: fixed instruction replacement | Local hook/protocol replacement | Exact path predicate, not evidence evaluation | see record | see record | Unconditional four-path overwrite | No license to treat local wiki as correct | Can replace custom host guidance | see record and [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | SRC-1, `src/index.ts` | [RT-CLM-safe-update](runtime.md#rt-clm-safe-update) | Missing wiki paths still created | Downstream behavior unobserved |
| [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) | content transformation | doctrine only | Raw documents | truth-apt transformation: acquisition/import | New external material enters host context | Agent reading; source-specific domain unknown | see record | see record | Requested reading; no source authentication | Raw file preservation requested; source warrant unknown | Supplies potential premises for work/synthesis | see record and [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | SRC-1, `AGENTS.md`, `README.md` | [EPI-CLM-primary-truth](#epi-clm-primary-truth) | Preservation is not endorsement | No raw instance or read trace |
| [RT-RTE-agent-session](runtime.md#rt-rte-agent-session), [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands) | content transformation | doctrine only | [EPI-OBJ-domain-pages](#epi-obj-domain-pages), [EPI-OBJ-hot](#epi-obj-hot), [EPI-OBJ-log](#epi-obj-log) | truth-apt transformation: indeterminate | Raw/code/task findings become prose | Host model; project facts and selected rationale | see records | see records | Requested synthesis/write | No entailed derivation or accepted ampliative claim established | Model may author later context without per-sentence approval | see records and [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | SRC-1, `AGENTS.md` | [EPI-CLM-project-memory](#epi-clm-project-memory) | none | No paired inputs/outputs; reshaping, derivation and conjecture remain unresolved |
| [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) | retention | doctrine only | Hot, domain pages and log | no content change | Keep newly written content for later invocation | Host file tools; no acceptance criterion | see record | see record | Requested persistence | Retained candidate, not accepted knowledge | Makes authored content available later | see record and [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | SRC-1, `AGENTS.md` | [EPI-CLM-project-memory](#epi-clm-project-memory) | none | Existing pages show candidates available, not route activation |
| [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) | operational admission/selection/consumption | doctrine only | Hot, index and selected domain content | no content change | Use available wiki as project context | Host model judges whether hot is sufficient; not a truth evaluator | see record | see record | Requested primary-source priority and conditional reads | Operational reliance requested without explicit acceptance | Context may affect answers, changes and next steps | see [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) | SRC-1, `AGENTS.md`, `CLAUDE.md` | [EPI-CLM-primary-truth](#epi-clm-primary-truth) | Priority exceeds demonstrated warrant | No trace of which content reached or changed a decision |
| [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | check/evidence production | doctrine only | Wiki, especially hot and empty domain pages | no content change | Staleness, missing context, empty pages | see record | see record | see record | Requested diagnosis/proposal, not enforced invalidation | At most model diagnosis in project-health domain | Proposal can guide later edits; no automatic exclusion | see record | SRC-1, `AGENTS.md` | [EPI-CLM-health-fixes](#epi-clm-health-fixes) | README says fixing, protocol says propose | No diagnosis instance or accuracy evidence |
| [EPI-RTE-log-fold](#epi-rte-log-fold) | content transformation | doctrine only | [EPI-OBJ-log](#epi-obj-log) | truth-apt transformation: indeterminate | Older history to summary | see record | see record | see record | Requested replacement with crucial-history preservation | Intended compression; fidelity not checked | Shorter history can become later context | see record | SRC-1, `AGENTS.md` | [EPI-CLM-project-memory](#epi-clm-project-memory) | Append-only description versus condensation | No paired log/summary; cannot assign semantic preservation |

No disposition/acceptance or post-acceptance lifecycle-integration route was found within the inspected protocol/CLI boundary: see [EPI-ABS-acceptance-gate](#epi-abs-acceptance-gate). Linking a new page changes organization for later access, but does not establish lifecycle integration as defined here because acceptance has not been established. Lint's possible detection is not merged with an invented rejection mechanism.

Concrete deterministic trace, deduced from implementation without execution: take argv command `update`, an existing `CLAUDE.md` containing arbitrary custom text, and an existing `.memory/wiki/hot.md` containing a stale statement. The exact-path predicate makes the first destination a protocol file; its old content is replaced by the fixed hook template. Hot is not a protocol file and exists, so its stale text is skipped unchanged. Thus mechanical update neither validates nor refreshes that candidate. For command `lint`, dispatch exits 1 before any template loop. SRC-1, `src/index.ts`; supporting branches are retained in [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update) and [RT-RTE-cli-init](runtime.md#rt-rte-cli-init). This is an implementation deduction, not observed operation.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-project-memory](#epi-clm-project-memory) | see record | SRC-1, `README.md`, `AGENTS.md`; doctrine/design | see record | [RT-RTE-cli-init](runtime.md#rt-rte-cli-init); continuing loop [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) is doctrine only | None; log reports ingestion | No contrast; external compliance required | Files and requested cross-session reuse, not demonstrated compounding benefit | Retention does not establish learning or truth |
| [EPI-CLM-primary-truth](#epi-clm-primary-truth) | see record | SRC-1, `CLAUDE.md`, `README.md`; doctrine/design | see record | Hook installation; [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol) requests reliance | None | No evidence-consuming acceptance gate | Project-priority instruction exists | Domain facts can contradict metadata; source warrant unknown |
| [EPI-CLM-health-fixes](#epi-clm-health-fixes) | see record | SRC-1, `README.md`, `AGENTS.md`; doctrine/design | see record | [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) is doctrine only | None | No freshness oracle, validity criterion or enforced withdrawal | Requested health assessment and proposals | Automatic fixes stronger than protocol text |
| [RT-CLM-safe-update](runtime.md#rt-clm-safe-update) | see record | SRC-1, `README.md`, `src/index.ts`; doctrine/design and implementation | see record | [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update) | None | Ordinary filesystem assumptions; no concurrent-writer protection | Existing wiki files skipped | Missing starter pages created; old facts preserved regardless of truth |

## Bounded conclusion

MemWiki implements file installation and fixed protocol replacement. It requests acquisition of source material, synthesis, retention, selective reuse, health checking and history condensation. These are distinct from observed performance. Source files are intended to remain unchanged, but there is no demonstrated lineage from individual source assertions to wiki sentences. Import warrant remains unknown; untouched source bytes alone do not establish truth. Source-dependent claims: SRC-1, `src/index.ts`, `AGENTS.md`, `README.md`; see the ledger records.

The strongest evaluator is the requested lint pass over staleness, missing hot context and empty domain pages. Its result is a proposal, with advisory force through the external agent/user; no required consumer marks a candidate accepted or withdraws it from later reading. Retained wiki is requested as project truth before such checking. No warranted entailed derivation, evidence-consuming acceptance of an ampliative claim or subsequent lifecycle integration is established in this inspected boundary. This does not deny that a host can test code or critically inspect facts during ordinary work. Those external actions are not supplied evidence of MemWiki acceptance. SRC-1, `AGENTS.md`, `CLAUDE.md`; [EPI-RTE-wiki-lint](#epi-rte-wiki-lint), [EPI-ABS-acceptance-gate](#epi-abs-acceptance-gate).

A concrete contradiction qualifies the warrant claim: `stack.md` asserts no runtime dependencies, while `package.json` declares `memwiki`. This demonstrates a stale or mis-scoped candidate assertion at the frozen commit, not a known failure of lint execution. Similarly, the log reports links to `landscape.md` and `competitors.md`, while the retained index contains neither; the report cannot reconstruct when or why those references diverged. Neither inconsistency licenses a system-wide verdict. SRC-1, `.memory/wiki/stack.md`, `package.json`, `.memory/wiki/log.md`, `.memory/wiki/index.md`; [EPI-OBJ-domain-pages](#epi-obj-domain-pages), [EPI-OBJ-log](#epi-obj-log).

Instruction replacement can change future policy delivery without a truth-apt update. Retained work summaries and rationale could guide later action, but exercised learning, reflection, autonomous maintenance, self-improvement and a theory-criticism iteration remain independently unestablished. External model parameters and internal reasoning are uninspected; that opacity establishes neither those properties nor their absence. SRC-1, `src/index.ts`, `AGENTS.md`; [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent), [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).

## Shared records

### Operative objects

#### EPI-OBJ-hot
Label: Hot cache

Source-native identity: `.memory/wiki/hot.md`. Natural-language project state plus task checklist, stored in Markdown on disk. Distinct from [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files): this is retained context the hooks request, not the hooks themselves. SRC-1, `.memory/wiki/hot.md`, `AGENTS.md`. No supplied operative-object counterpart describes this page.

> - Successfully completed `/memwiki-ingest`, populating the wiki with stack details, coding patterns, and architectural decisions.
> --- `.memory/wiki/hot.md`

#### EPI-OBJ-domain-pages
Label: Domain pages

Source-native identity: `.memory/wiki/stack.md`, `.memory/wiki/patterns.md`, `.memory/wiki/decisions.md`, `.memory/wiki/bugs.md`. Natural-language facts, conventions, rationale and bug-record placeholder in Markdown files. These share the session write mechanism and task-dependent consumer, unlike the first-read hot cache and fold-targeted log. Distinct from [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files); no supplied counterpart describes these candidate pages. Source lineage and acceptance provenance are unknown. Some patterns accurately describe the inspected code; correctness of those instances does not establish correctness of the whole set. SRC-1, `.memory/wiki/patterns.md`, `.memory/wiki/stack.md`, `.memory/wiki/decisions.md`, `.memory/wiki/bugs.md`, `package.json`.

> - **Zero Dependencies**: The project explicitly avoids runtime dependencies (only `@types/node` and `typescript` as devDependencies) to ensure zero friction and high security/stability.
> --- `.memory/wiki/stack.md`

> "dependencies": {
>     "memwiki": "^1.0.0"
>   }
> --- `package.json`

> - **Decision:** Store the `.cursorrules`, `CLAUDE.md`, and default wiki files as string literals directly in `src/index.ts`.
> --- `.memory/wiki/decisions.md`

#### EPI-OBJ-log
Label: Work log

Source-native identity: `.memory/wiki/log.md`. Natural-language historical assertions in a Markdown file. Unlike [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files), this contains reported work and is the specific fold input; no supplied object counterpart. It is intended for later history access, but actual causal use is unobserved. The claimed ingestion supplies reported operation only, not authenticatable route execution. SRC-1, `.memory/wiki/log.md`, `AGENTS.md`.

> - Triggered `/memwiki-ingest`. Scanned `package.json`, `tsconfig.json`, `src/index.ts`, and `README.md`.
> - Populated `stack.md`, `patterns.md`, and `decisions.md` based on project findings.
> --- `.memory/wiki/log.md`

> - Updated `index.md` to link to the new `landscape.md` and `competitors.md` files.
> --- `.memory/wiki/log.md`

#### EPI-OBJ-index
Label: Project wiki index

Source-native identity: `.memory/wiki/index.md`. Natural-language labels and wiki-link notation in a Markdown file; links are interpreted by the external agent, with no shipped parser or checker. Distinct from [RT-OBJ-protocol-files](runtime.md#rt-obj-protocol-files): it supplies conditional context selection rather than detailed maintenance rules. No supplied object counterpart. Its registered links expose the default pages, not the two added pages asserted by the retained log. SRC-1, `.memory/wiki/index.md`, `.memory/wiki/log.md`, `AGENTS.md`.

> - [[hot.md]]: Immediate context and next steps.
> - [[log.md]]: Append-only changelog of agent sessions.
> - [[stack.md]]: Tech stack details and versions.
> - [[patterns.md]]: Established coding patterns and conventions.
> - [[bugs.md]]: Known issues, quirks, and workarounds.
> - [[decisions.md]]: Architecture Decision Records (ADRs).
> --- `.memory/wiki/index.md`

### Routes

#### EPI-RTE-wiki-lint
Label: Wiki health check
Part of: [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands)

This is the health-check part, separated from ingestion and fold by target, result and force. Endpoints/progression: user chat command → host interpretation → wiki diagnosis → proposed fixes. Owner: external agent; state/context: selected project/wiki content; action effects: requested diagnosis and proposal, not enforced rejection. Check target/domain: outdated wiki assertions, missing immediate context and empty pages. Evaluator: host model; no supplied expected-answer reference, independent oracle or truth metric. User proposes the launch; model decides findings and proposals; human veto is host-dependent and uninspected. Mode: open maintenance request. Trigger: `/memwiki-lint`; guidance names those three health conditions. Proposed fixes persist only if separately acted on; no rollback, required approval or exclusion marker is supplied. SRC-1, `AGENTS.md`, `README.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested health findings and proposed fixes.
- Later read-back: uninspected — protocol does not require persisting diagnosis or applying fixes for later sessions.
- Delegated visibility: uninspected — host delegation is unspecified.
- Selection predicate: Chat token `/memwiki-lint`; host selects wiki evidence for the stated health conditions.
- Invalidation or expiry: No enforced expiry or withdrawal; outdated information is a requested diagnosis target.
- Activation or effect: Advisory proposal through host response; any subsequent edit and changed reliance unobserved.
- Evidence limits: No lint transcript, result, accuracy evaluation or downstream consumer trace.

Behavioral-authority path: external agent/user consumes the response; channel is chat proposal; force advisory; horizon current maintenance request, potentially later file edits. No automatic truth-admission license follows.

> - `/memwiki-lint`: Perform a health check on the wiki. Look for outdated information, missing context in `hot.md`, or empty domain pages, and propose fixes.
> --- `AGENTS.md`

#### EPI-RTE-log-fold
Label: Work log condensation
Part of: [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands)

This is the older-log transformation part; unlike lint it requests a changed retained object. Endpoints/progression: user token → model selects older log entries → summary replaces detail → possible later reading. Owner/executor: host agent and its external tools. Context/state: log and host task context. Candidate target: historical assertions. Evaluator/condition: model decides crucial history and condensation; no prescribed fidelity comparison or acceptance criterion. Semantic preservation is indeterminate without paired input/output. User supplies launch, model proposes/admits text through file tools; human veto remains host-dependent. Mode: open maintenance request; improvement trigger is excess log length, without a threshold. Guidance: preserve crucial history. What persists is summarized history; no required backup, verification or rollback. SRC-1, `AGENTS.md`, `.memory/wiki/log.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested summarized paragraph replacing older log detail.
- Later read-back: Summary is intended to remain in `log.md` for subsequent history access; actual read-back unobserved.
- Delegated visibility: uninspected — no delegated worker or sharing protocol is specified.
- Selection predicate: `/memwiki-fold`, then model selection of older entries and crucial history.
- Invalidation or expiry: Older detail may be replaced; no explicit provenance or reversible expiry metadata.
- Activation or effect: Requested change to durable history; resulting behavior dependence unobserved.
- Evidence limits: No before/after log, source-linked summary or fidelity check supplied.

Behavioral-authority path: later coding agent, retained log read through conditional wiki access, contextual/advisory force, subsequent project sessions. This is retention before acceptance, not post-acceptance integration.

> - `/memwiki-fold`: Condense older entries in `log.md` into a summarized paragraph to keep the file from becoming too long, while preserving crucial history.
> --- `AGENTS.md`

### Claims

#### EPI-CLM-project-memory
Label: Persistent project memory

Claimed operation: persistent, compounding project knowledge across coding sessions. Distinct from [RT-CLM-safe-update](runtime.md#rt-clm-safe-update), which concerns file overwrite safety, not epistemic growth. SRC-1, `README.md`, `AGENTS.md`; doctrine/design. The metaphor is operationally interpreted as persistence and later reuse, not an assertion that the CLI itself contains model intelligence.

> `memwiki` gives your project a persistent brain. It leverages the fact that modern AI agents naturally read markdown files in your workspace, providing a standardized, vendor-agnostic memory system without requiring complex plugins or subscriptions.
> --- `README.md`

> This project uses **MemWiki** (inspired by the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)), a persistent compounding knowledge base for AI coding agents.
> --- `AGENTS.md`

#### EPI-CLM-primary-truth
Label: Primary project truth

Claimed warrant/operation: protocol and hot cache receive primary-source priority; raw originals are called a source of truth. Distinct from [RT-CLM-safe-update](runtime.md#rt-clm-safe-update); closely associated with the reliance channel [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol), but this record identifies its warrant language rather than another delivery path. SRC-1, `CLAUDE.md`, `README.md`; doctrine/design. Raw-file immutability does not independently validate content, and the protocol supplies no required claim-to-source citation.

> Please read `AGENTS.md` and `.memory/wiki/hot.md` as your primary source of truth for this project before answering any queries or making changes.
> --- `CLAUDE.md`

> - **How it works:** When you drop a file like `stripe-api.pdf` into `.raw/`, you simply tell your agent: *"Please process the new Stripe docs in the raw folder."* The agent will read the PDF and synthesize the important architectural details into a clean markdown file inside the `wiki/` folder, leaving the original PDF untouched as a source of truth.
> --- `README.md`

#### EPI-CLM-health-fixes
Label: Wiki health fixes

Claimed operation: agent fixes stale information and missing context on lint. No supplied claim counterpart; [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands) already notes the stronger README wording. This is the distinct public claim compared against [EPI-RTE-wiki-lint](#epi-rte-wiki-lint), not a duplicate command route. SRC-1, `README.md`, `AGENTS.md`; doctrine/design.

> - `/memwiki-lint`: The agent will perform a health check on the wiki, fixing outdated information or filling in missing context.
> --- `README.md`

### Evidenced absences

#### EPI-ABS-acceptance-gate
Label: Explicit acceptance gate

- implementation conclusion status: absent

Searched boundary: SRC-1 at `8034a3da991ac2639b87875172a9572903ecf1d5`, complete reads of `src/index.ts`, `src/index.js`, `AGENTS.md`, `README.md` and all three host hooks. Query/question: does any candidate assessment yield a recorded, evidence-consuming acceptance decision naming criterion, intended use and scope, consumed before reliance; or a mandatory rejection/withdrawal marker? Dispatch and write branches use command/path/existence predicates only. Protocol requests synthesis, reads, health proposals and condensation, with no acceptance record or mandatory validity gate. Strongest counterexample is lint, retained in [EPI-RTE-wiki-lint](#epi-rte-wiki-lint): it proposes fixes, rather than deciding explicit acceptance or preventing stale reuse. The closest supplied records [RT-RTE-agent-session](runtime.md#rt-rte-agent-session) and [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands) describe open model admission, not an acceptance record. This absence is a distinct assessment of those mechanisms, not a replacement route.

Conclusion: no explicit acceptance gate in these shipped paths; prevents promotion of retention/use to accepted knowledge or post-acceptance integration. It does not establish that external hosts never evaluate or that all wiki assertions are false. Load-bearing branches and requested command passages are supplied by [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), [RT-RTE-protocol-update](runtime.md#rt-rte-protocol-update), [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands), and the lint/fold records above.

> - Synthesize any raw knowledge from `.memory/.raw/` into the wiki pages.
> - Never delete knowledge from the wiki. Only append or refine.
> --- `AGENTS.md`
