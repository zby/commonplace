---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Hippocampus epistemic routes: source import, model consolidation, structural checks, contradiction decisions and later reliance."
run-id: AAS-2026-11-08-hippocampus-30a5ab9b2a87-01
reviewed-boundary: "99531951ae60a9814ac7d27a32dd00f0c81a5008"
---

# Hippocampus epistemic report

## Source-and-claim boundary

The question is how the personal vault obtains claims, checks them, authorizes reliance and carries results into later sessions. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). The shipped host contracts and executable utilities are included; external host/model internals and actual private vaults are not. All source anchors below refer to SRC-1 at the reviewed commit. No target execution was performed. Architectural wiring, requested model behavior and observed operation are kept separate.

The consequential warrant claims are [EPI-CLM-structural-checks](#epi-clm-structural-checks), [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge), and the freshness claim [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh). These concern inspectability, meaningful links and available recent context, not a formal proof engine. The primary stated objective is transparency and minimal infrastructure rather than superior recall; the source itself acknowledges wording and scale limits (see [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge)).

### Coverage

Direct reads here supplement, rather than merely repeat, the supplied runtime account. Available but not independently reread material is explicitly marked.

| Entry point or operation | Source path (SRC-1) | Coverage / records | Limit and conclusion prevented |
|---|---|---|---|
| Local, outside-file, pasted and URL ingest; batch/re-ingest | `.claude/skills/ingest/SKILL.md`, `_templates/source.md` | Direct complete reads; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [EPI-OBJ-source](#epi-obj-source), [EPI-OBJ-archive](#epi-obj-archive) | No source-specific extraction trace: semantic preservation and exercised rejection unobserved. |
| Conversation save | `.claude/skills/save/SKILL.md`, `_templates/note.md` | Direct complete reads; [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) | No saved-conversation pair: relation between input and saved propositions remains indeterminate. |
| Query and cross-project read | `CLAUDE.md` | Direct complete read; [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) | No query/reference-answer set: recall, correctness and transfer unmeasured. |
| Mechanical lint CLI, both text and JSON output | `scripts/vault_lint.py` | Direct complete read, including argparse and final return; [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint), [EPI-OBJ-findings](#epi-obj-findings) | Checks structures, not propositions about the world. |
| Editorial lint, stale claims, deletion/merge/resolution | `.claude/skills/lint/SKILL.md`, `CLAUDE.md` | Direct complete reads; [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) | Sampling allowed; human criteria for which conflicting claim is true unspecified. |
| SessionStart and Stop, both hosts | `.claude/settings.json`, `.codex/hooks.json`, `scripts/on-stop.sh` | Direct complete reads; [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) | Host execution and interpretation unobserved; timestamp ordering is not summary fidelity. |
| Host entry/skill adapters | `AGENTS.md`, `.agents/skills/ingest/SKILL.md`, `.agents/skills/save/SKILL.md`, `.agents/skills/lint/SKILL.md` | Supplied runtime findings; [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance) | No independent adapter reread here; runtime establishes redirects, not loading. |
| Framework update/diff/export | `scripts/sync_framework.sh` | Supplied runtime findings; [RT-RTE-framework-update](runtime.md#rt-rte-framework-update), [RT-RTE-framework-export](runtime.md#rt-rte-framework-export) | Source-level pathname/copy admission only; neither semantics of future revisions nor activation is established. |
| Public warrant and walkthrough | `README.md`, `docs/why-no-vector-db.md`, `docs/what-happens-when-you-ingest.md` | Direct complete reads; epistemic claims below | Comparisons are design arguments, not causal experiments. |
| Initial retained surfaces | `wiki/hot.md`, `wiki/index.md`, `wiki/log.md` | Direct complete reads; [EPI-OBJ-hot](#epi-obj-hot), [EPI-OBJ-index](#epi-obj-index) | Scaffold only: no provenance-linked production/check/acceptance instance. |
| Other templates, Obsidian/configuration and non-operative roots | `_templates/entity.md`, `_templates/concept.md`, `_templates/project.md`, `.obsidian/`, other roots listed by boundary | Supplied boundary coverage, not direct reads here | No independent assessment of other template fields or browsing behavior. Images remain excluded. |

There is no separately registered tool server or model executor in the supplied runtime account: tools are host-native and skills are instructions. This report assesses all material route families identified above, but does not promote supplied coverage or uninspected external behavior into a system-complete negative about all possible host-mediated checks. Missing provider internals prevent a conclusion about internal model learning or hidden reasoning; missing observations prevent claims of successful memory activation or benefit. These limits do not make the inspected structural evaluator unknowable.

## Epistemic-object inventory

Object fields owned by declarations are referenced rather than duplicated.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-archive](#epi-obj-archive) | Imported source assertions, if present; arbitrary input may contain none | see record | SRC-1 `.claude/skills/ingest/SKILL.md` | see record |
| [EPI-OBJ-source](#epi-obj-source) | Attributed source summary and key claims | see record | SRC-1 `_templates/source.md` | see record |
| [EPI-OBJ-pages](#epi-obj-pages) | Concepts, entity facts, saved findings, decisions/rationale | see record | SRC-1 `.claude/skills/save/SKILL.md` | see record |
| [EPI-OBJ-hot](#epi-obj-hot) | Recent facts and active-thread descriptions | see record | SRC-1 `wiki/hot.md` | see record |
| [EPI-OBJ-index](#epi-obj-index) | Claims describing what a page covers; journal claims about operations | see record | SRC-1 `wiki/index.md`, `wiki/log.md` | see record |
| [EPI-OBJ-findings](#epi-obj-findings) | Container of the two separately assessed output parts below | see record | SRC-1 `scripts/vault_lint.py`, `.claude/skills/lint/SKILL.md` | see record |
| [EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings) | Program-derived predicates about current file structures | see record | SRC-1 `scripts/vault_lint.py` | see record |
| [EPI-OBJ-editorial-findings](#epi-obj-editorial-findings) | Model allegations of staleness/conflict and proposed repairs | see record | SRC-1 `.claude/skills/lint/SKILL.md` | see record |
| [RT-OBJ-project-contract](runtime.md#rt-obj-project-contract) | Policies, not newly established factual knowledge | see record | see record | see record |
| [RT-OBJ-hook-config](runtime.md#rt-obj-hook-config) | None in event-dispatch rules | see record | see record | see record |
| [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) | Not determinable at the parameter-content level | see record | see record | see record |

## Authority-route ledger

Repeated route citations below identify different consequential functions of the same supplied route, not new record identities. For endpoints, owner, state effects, read-back, activation and other generic route fields, **see the cited declaration**. This overlay adds epistemic classification and distinguishes checking, disposition, retention and consumption. “Doctrine only” describes the semantic route prescribed to a host model; “implemented” describes executable checks/transport, not model compliance.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) / acquire | content transformation | doctrine only | [EPI-OBJ-archive](#epi-obj-archive) | truth-apt transformation: acquisition/import | External content enters archive | Host read/fetch/copy under model protocol | On user ingest | Original or fetched extraction retained | Requested source handling | Source warrant unknown; provenance is not endorsement | Source supplies data, not instructions | Foreground model, source text, advisory evidence, current ingest | SRC-1 `.claude/skills/ingest/SKILL.md` | none | none | URL stores extracted text, not necessarily original bytes; see archive record. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) / duplicate check | check/evidence production | doctrine only | [EPI-OBJ-source](#epi-obj-source) | no content change | Hash equals an existing content_hash | SHA-256 plus model-directed search; byte identity domain | Before extraction | Duplicate candidate reported | Requested check | Content identity only, no truth license | Supplies evidence for stopping | Foreground model, hash/search result, advisory, current request | SRC-1 `.claude/skills/ingest/SKILL.md` | none | none | Tool algorithm requested, no supplied execution. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) / duplicate stop | disposition/acceptance | doctrine only | [EPI-OBJ-source](#epi-obj-source) | no content change | Whether to process again | Model follows duplicate rule; user can override | After duplicate result | Stop or explicit re-ingest | Requested admission policy | No epistemic acceptance | Blocks repeated processing unless user asks | Model, skill rule, permissive/enforcing by compliance, request | SRC-1 `.claude/skills/ingest/SKILL.md` | none | none | Not per-claim verification. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) / consolidate | content transformation | doctrine only | [EPI-OBJ-source](#epi-obj-source), [EPI-OBJ-pages](#epi-obj-pages) | truth-apt transformation: indeterminate | Source to English summaries, selected claims and linked concepts | Model interpretation; likely future reference is page-worthiness criterion | After source/context/template reads | Seed pages, revisions and source links | Requested model transformation | Attributed candidates; confidence/status fields do not establish evidence-consuming acceptance | May write retained claims without universal per-content approval | Foreground model then later readers, Markdown, advisory knowledge, later sessions | SRC-1 `.claude/skills/ingest/SKILL.md`, `_templates/source.md` | [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | unknown | Intended extraction/translation may reshape; no input/output pair establishes preservation, entailment or non-entailment. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) / conflict check | check/evidence production | doctrine only | [EPI-OBJ-source](#epi-obj-source), [EPI-OBJ-pages](#epi-obj-pages) | no content change | Competing claims in new and existing pages | Model compares propositions; no explicit truth oracle | During ingest | Conflict noticed or missed | Requested semantic check | A tension allegation, not adjudication | Makes conflict available for later resolution | Model, source/pages, advisory, ingest and future maintenance | SRC-1 `CLAUDE.md`, `.claude/skills/ingest/SKILL.md` | [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | none | No guarantee that all competing pages are read. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) / flag conflict | retention | doctrine only | [EPI-OBJ-pages](#epi-obj-pages) | truth-apt transformation: indeterminate | Record conflict on both pages without silent overwrite | Model writes callouts; user reserves resolution | On detected conflict | Both candidate assertions remain with warning | Requested preservation protocol | Withholds automatic adjudication, not automatic downstream use | Later readers may see warning; neither side auto-withdrawn | Model/user, warning callouts, advisory, until resolution | SRC-1 `CLAUDE.md` | [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | none | No forced query abstention on warned pages. |
| [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) / synthesize | content transformation | doctrine only | [EPI-OBJ-pages](#epi-obj-pages) | truth-apt transformation: indeterminate | Conversation to durable conclusions and rationale | Model chooses what is worth keeping; ambiguous content prompts user | On save request | Declarative cited note or page update | Requested synthesis | Candidate conclusions; citation does not certify source truth | Can write without general per-content approval | Model, save skill and conversation, advisory content, later sessions | SRC-1 `.claude/skills/save/SKILL.md` | none | none | Some outputs may be compression, others new inference; no pair individuates these alternatives. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) / file | retention | doctrine only | [EPI-OBJ-source](#epi-obj-source), [EPI-OBJ-pages](#epi-obj-pages), [EPI-OBJ-index](#epi-obj-index) | no content change | Candidate persistence and graph/catalog connection | Model/host writes; page-worthiness, not warranted truth, selects | On ingest/save completion | Pages, links, index/log entries and archive | Requested retention | Retained candidates, not established accepted ampliative claims | Makes content available to future selection | Future agent and human, files/catalog, advisory/ranking, sessions | SRC-1 `.claude/skills/ingest/SKILL.md`, `.claude/skills/save/SKILL.md` | [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | none | Cross-linking before epistemic acceptance is retention/organization, not lifecycle integration after acceptance. |
| [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) / scan | check/evidence production | implemented | [EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings) | truth-apt transformation: entailed derivation | Parsed fields, names, links, counts and index membership | Python fixed predicates over current snapshot | Explicit CLI; requested after large batch and fixes | JSON/text findings and counts | Reports, does not block writes | Narrow claims about scanner-defined structures | Supplies fix candidates, no automatic admission | Foreground model/user, stdout, advisory, scan/maintenance | SRC-1 `scripts/vault_lint.py` | [EPI-CLM-structural-checks](#epi-clm-structural-checks) | scope limit | See concrete deduction below; parser and resolver boundaries limit license. |
| [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) / editorial check | check/evidence production | doctrine only | [EPI-OBJ-editorial-findings](#epi-obj-editorial-findings) | truth-apt transformation: indeterminate | Stale contradictory claims, missing links/pages, old seeds | Model search/judgment, possibly sampled; 3+ mentions and 30+ days are editorial triggers | After scan | Proposed repairs, development, merges or deletion | Requested judgment | Allegations/proposals; age does not establish falsity | Can nominate content for revision | Foreground model, maintenance findings, advisory, current maintenance | SRC-1 `.claude/skills/lint/SKILL.md` | none | none | Sampling prevents full semantic coverage. |
| [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) / approve fixes | disposition/acceptance | doctrine only | [EPI-OBJ-pages](#epi-obj-pages), [EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings), [EPI-OBJ-editorial-findings](#epi-obj-editorial-findings) | no content change | Which fixes and conflicting claims to retain | Human bulk approval for safe edits, individual approval for merge/delete/contradiction; model proposes | Before model edits | Approve, reject or defer | Model-mediated user veto policy | User decides truth in contradiction cases; criterion/evidence protocol unspecified | Permits approved revisions, not a universal write gate | User → foreground model, approval response, permissive, current maintenance and persisted edits | SRC-1 `.claude/skills/lint/SKILL.md` | [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | unknown | A possible human acceptance decision is afforded, not evidenced as a performed, criterion-bound decision. |
| [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) / apply repair | content transformation | doctrine only | [EPI-OBJ-pages](#epi-obj-pages) | truth-apt transformation: indeterminate | Approved changes replace/remove page content; rerun checks structures | Model/host executes approved edits; user can reject proposals | After approval | Content revision, deletion, merges, updated log/hot | Requested repair | Rescanning licenses structures only, not truth of a resolved claim | Changes later available content; recovery manual | Future readers, edited files, advisory knowledge, sessions | SRC-1 `.claude/skills/lint/SKILL.md` | none | none | No explicit dependency invalidation propagates withdrawn claims to every derivative. |
| [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) / timestamp | check/evidence production | implemented | [EPI-OBJ-hot](#epi-obj-hot) | truth-apt transformation: entailed derivation | Whether any non-hot Markdown file has newer mtime | Shell find and guarded test, filesystem timestamps | Eligible first Stop | Refresh request or no request | Hook stdout; host must honor block | Temporal ordering, not semantic freshness or session causation | Can request another model turn before stopping | Host/model, JSON reason, enforcing only through host, current stopping turn | SRC-1 `scripts/on-stop.sh` | [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh) | bounded guard | Missing hot, recursive stop, markers and equal/older timestamps bypass. |
| [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) / refresh | content transformation | doctrine only | [EPI-OBJ-hot](#epi-obj-hot) | truth-apt transformation: indeterminate | Wiki/session content to <=500-word summary | Model instructed to overwrite four sections | After writes or hook request | Replacement summary | Requested rewrite | No established semantic fidelity or claim endorsement | Narrows recent context later injected | Foreground model → later model, hot text, advisory, sessions | SRC-1 `scripts/on-stop.sh`, `CLAUDE.md` | [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh) | unknown | Summary may compress or introduce interpretation; no traced pair. |
| [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) / persist | retention | implemented | [EPI-OBJ-hot](#epi-obj-hot), [EPI-OBJ-pages](#epi-obj-pages), [EPI-OBJ-archive](#epi-obj-archive) | no content change | Working-tree content to Git history | Shell stages content roots and commits existing index | Eligible stop after guard or bypass | Commit or logged failure | Local Git side effects | Versioning is not epistemic acceptance | History can aid manual recovery | Human/Git, local repository, recovery affordance, future sessions | SRC-1 `scripts/on-stop.sh` | none | none | Failure returns zero; prestaged files also enter commit; see runtime. |
| [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) / reload | operational admission/selection/consumption | implemented | [EPI-OBJ-hot](#epi-obj-hot) | no content change | File to model-visible context | Host startup/resume/clear/compact callback runs cat | SessionStart events | Hot text printed if present | Wired supply, host delivery external | Delivered summary without added warrant | Recent facts may influence later answers/actions before new checking | Host/model, hook context, advisory knowledge, invocation | SRC-1 `.claude/settings.json`, `.codex/hooks.json` | [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh) | unknown | Delivery/compliance/activation not observed; Codex context limit is external semantics. |
| [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) / read-answer | operational admission/selection/consumption | doctrine only | [EPI-OBJ-hot](#epi-obj-hot), [EPI-OBJ-index](#epi-obj-index), [EPI-OBJ-pages](#epi-obj-pages) | truth-apt transformation: indeterminate | Relevant pages to cited answer or scoped abstention | Model relevance/confidence, search fallback, no reference answer | On question | Cited synthesis, or not-in-vault plus research offer | Requested read/abstain protocol | Source-relative answer; not independently verified world knowledge | Limits training-data substitution; no hard gate enforces it | Foreground/cross-project agent, file reads and citations, advisory/ranking, answer/current task | SRC-1 `CLAUDE.md` | [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | unknown | Selection and confidence can miss or misread; not-in-vault is not exhaustive absence. |
| [RT-RTE-framework-update](runtime.md#rt-rte-framework-update), [RT-RTE-framework-export](runtime.md#rt-rte-framework-export) / replace policy | behavior/policy adaptation | implemented | [RT-OBJ-project-contract](runtime.md#rt-obj-project-contract), [RT-OBJ-hook-config](runtime.md#rt-obj-hook-config) | non-truth-apt policy/content update: copy framework instructions and executable rules | Path-eligible incoming/local framework differences | see supplied records | see supplied records | see supplied records | see supplied records | No semantic quality or knowledge acceptance established | Future loading can alter guidance, templates and checks | see supplied records and [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance) | see supplied records, SRC-1 `scripts/sync_framework.sh` | [RT-CLM-local-edit-protection](runtime.md#rt-clm-local-edit-protection) | see supplied claim | No evidence-responsive improvement criterion or exercised successor evaluation. |

### Deterministic deduction and attempted counterexamples

For the lint row, the target is link resolution in the scanner's filename map, **not** the truth of the linked page or whether a heading exists. From inspected implementation, input text `[[Plan#Missing]]` produces target `Plan`: `link_targets` removes the heading portion. With a scanned file whose stem is `Plan`, the resolver gets a nonempty list and does not emit a dead-link finding for a missing heading. This is a static deduction, not a target run. Conversely an absent stem produces a dead-link finding. It refutes an unqualified reading of “all link correctness” while supporting basename-resolution checks. The scanner's fixed parsing rules warrant the derived predicates only for its actual input snapshot and interpretation, not omitted fields or real-world claims. See [EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings) for the implementation passages.

Other stronger interpretations were checked against adverse cases. Ingest's complete-read requirement explicitly allows sectional extraction for very large sources, and URL archival saves extracted content; neither implies lossless raw-byte provenance. The query fallback can find unindexed pages, so “unindexed means invisible” is too strong. Contradiction callouts preserve rather than reject conflicting candidates. Lint approval is not required by ordinary ingest/save or Stop. Stop's recursive/missing-file branches prevent an invariant semantic-refresh claim. These limits follow the supplied routes and the direct source reads above; none establishes that the intended protocol failed in a real run.

No ledger row establishes lifecycle integration **after epistemic acceptance**: graph connection occurs during candidate filing, and human resolution has no supplied decision trace identifying evidence, criterion and intended scope. This does not deny operational organization or possible human acceptance. Nor does it infer the absence of internal model reasoning from opacity. There is no source-supported input/output pair here that individuates an accepted ampliative proposition; the indeterminate transformations retain non-ampliative reshaping, entailed inference and ampliative conjecture as alternatives pending such evidence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-structural-checks](#epi-clm-structural-checks) | see record | see record | see record | [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) | None supplied | No comparison; fixed predicates support only their specified structures | Inspectable deterministic defect reporting, not semantic validation | “Duplicate under slightly different names” exceeds basename equality; missing headings are not checked. |
| [EPI-CLM-graph-knowledge](#epi-clm-graph-knowledge) | see record | see record | see record | No executable semantic-link evaluator; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) are model protocols | None supplied | No component intervention or comparative retrieval benchmark | Links can carry written intent and point to retained claims; explicit conflicts can be preserved for judgment | Link existence does not establish that causal intent is true or that one-hop retrieval beats similarity. |
| [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh) | see record | see record | see record | [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) | None supplied | No semantic-fidelity check; guarded timestamps | Wired reload and bounded refresh reminder | see supplied claim; fresh mtime is not endorsement. |
| [RT-CLM-local-edit-protection](runtime.md#rt-clm-local-edit-protection) | see record | see record | see record | [RT-RTE-framework-update](runtime.md#rt-rte-framework-update), [RT-RTE-framework-export](runtime.md#rt-rte-framework-export) | None supplied | No exercised successor comparison | Path-based framework change admission only | see supplied claim; not evidence of improved method. |

## Bounded conclusion

Hippocampus affords acquisition and durable organization of imported source claims and conversation conclusions. The archive/hash/origin protocol can preserve lineage, but source truth is unassessed, fetched extraction may omit original content, and neither a `confidence` field nor `seed`/`mature` status records an evidence-consuming acceptance decision. Source and saved-page transformations remain indeterminate without concrete input/output pairs; novelty or summary labels cannot establish either ampliation or entailment ([EPI-OBJ-archive](#epi-obj-archive), [EPI-OBJ-source](#epi-obj-source), [EPI-OBJ-pages](#epi-obj-pages)).

The inspected program produces narrow, truth-apt structural findings by deterministic derivation from file contents and names. Its findings advise the foreground model/user; they do not prevent writes or certify page truth. Editorial contradiction checks are model prescriptions. Contradiction handling withholds automatic adjudication and preserves warnings; maintenance reserves individual resolution, merging and deletion to user judgment. That is a real decision path, but the source specifies neither a truth criterion nor a performed acceptance with evidence and scope. Rechecking after repairs checks structure, not the truth of the repair ([EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings), [EPI-OBJ-editorial-findings](#epi-obj-editorial-findings), [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint)).

Retained pages, catalog descriptions and hot summaries receive operational reliance through model selection, hook injection and cited answers. Their force is advisory knowledge or relevance ranking; policies against training-data substitution and source instructions depend on host/model compliance. No check prevents a still-conflicted page or a faulty summary from influencing a later answer. Versioning is recovery, not validation; recency is not endorsement. The horizon is later invocations/sessions, but neither activation nor benefit is observed ([RT-RTE-vault-query](runtime.md#rt-rte-vault-query), [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks)).

The ordinary write paths are model-directed, not universally human-approved. Maintenance decisions and framework synchronization are distinct: one applies a user approval policy to fixes, the other copies behavior-shaping files by pathname/difference rules. Neither establishes autonomous evidence-responsive method improvement. Provider parameter changes remain uninspected, independently of Markdown adaptation. Implemented memory affordances, reflection, learning, autonomy and exercised self-improvement must not be collapsed into one verdict; this evidence establishes no causal benefit or exercised self-improvement claim ([RT-CMP-agent-model](runtime.md#rt-cmp-agent-model), [RT-RTE-framework-update](runtime.md#rt-rte-framework-update), [RT-RTE-framework-export](runtime.md#rt-rte-framework-export)).

The supported architecture is therefore a source-relative, inspectable retention and retrieval workflow with localized structural evaluation and human-reserved contradiction resolution. It does not, on the supplied evidence, establish produced accepted ampliative knowledge or comparative retrieval superiority. This is a bounded conclusion about those claims, not a negative score for a deliberately personal, low-infrastructure vault.

## Shared records

### Operative objects

#### EPI-OBJ-archive
Label: Archived originals

Source-native identity: `inbox/_done/` and original input files. Form: natural-language source text when textual; other input/attachment encodings depend on the source and are uninspected in the empty scaffold. Substrate: local files and, conditionally, Git history. Claimed role: original provenance, not a truth oracle. Closest supplied record is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), a process rather than this object; no supplied operative-object counterpart. Local files are to be moved/copied without editing; pasted material is saved verbatim; URL material is fetched extraction. Hash/origin identifiers are symbolic lineage metadata, not proof that the attributed proposition is true. No real archive/source pair is supplied. SRC-1 `.claude/skills/ingest/SKILL.md`.

> - **A URL** — fetch it with the available web tool, save the extracted content to `inbox/_done/<slug>-<YYYY-MM-DD>.md` with `source_url` and `fetched` in frontmatter, then ingest.
> --- `.claude/skills/ingest/SKILL.md`

> 4. **Decide the archive path now**: `inbox/_done/<original-name>`; if that name is already taken, suffix with date-time (`report.md` → `report-20260711-1030.md`). Never overwrite an archived original.
> --- `.claude/skills/ingest/SKILL.md`

#### EPI-OBJ-source
Label: Source pages

Source-native identity: `wiki/sources/` pages using `_templates/source.md`. Natural-language summary, key claims, caveats and entity/concept descriptions coexist with symbolic type/date/hash/path/link fields in local Markdown. Claimed role: attributable source account and provenance bridge. Closest supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) is its producer route, not the retained object; no supplied object counterpart. The `confidence: medium` default and `status: seed` do not name an evaluator, criterion, evidence consumption or accepted intended use. A claim may be attributed without being accepted. No populated source pages are supplied. SRC-1 `_templates/source.md`, `.claude/skills/ingest/SKILL.md`.

> confidence: medium       # high | medium | low
> content_hash: "<sha256 of the original file>"
> origin: "inbox/_done/<original-filename>"
> --- `_templates/source.md`

> ## Key Claims
>
> - <claim>
> --- `_templates/source.md`

#### EPI-OBJ-pages
Label: Derived and saved pages

Source-native identity: entity/concept/project pages and `wiki/notes/` synthesis/decision/session pages. Natural-language propositions, explanations, rationale and warnings; symbolic YAML metadata and wikilinks; local Markdown substrate. Claimed role: reusable durable knowledge, later read by foreground/cross-project agents and humans. Different from [EPI-OBJ-source](#epi-obj-source): this is derived or conversation-saved content rather than the source account. Closest supplied [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) describe production, not an object counterpart. Citation and cross-link requirements provide intended attribution, not guaranteed semantic preservation. Contradiction warnings remain claims awaiting user resolution; not automatic retractions. SRC-1 `.claude/skills/save/SKILL.md`, `.claude/skills/ingest/SKILL.md`, `CLAUDE.md`.

> 4. **Write the page** from the matching `_templates/` skeleton: declarative present tense, in the language set in the vault `CLAUDE.md` → Conventions, self-contained (readable cold in 6 months), every mentioned entity/concept wikilinked, claims cited as `(Source: [[Page]])`. If it answers a specific question, put the question verbatim in the `question:` field.
> --- `.claude/skills/save/SKILL.md`

> 8. **Check for contradictions** with existing pages. Flag both sides with `> [!warning] Contradiction with [[Page]]` callouts — never silently overwrite.
> --- `.claude/skills/ingest/SKILL.md`

#### EPI-OBJ-hot
Label: Hot cache

Source-native identity: `wiki/hot.md`. Natural-language recent facts/change/thread summary with symbolic YAML fields, stored as overwriteable Markdown. Claimed role: recent context supplied before later questions. Closest supplied [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) is its delivery/persistence route, not an object counterpart. Different from the static [RT-OBJ-project-contract](runtime.md#rt-obj-project-contract): accumulated cache is instance state, not the operating contract. Scaffold text establishes an available initial candidate, not execution of summary production. Summary warrant/fidelity remains unknown; source references can be lost in condensation. SRC-1 `wiki/hot.md`, `CLAUDE.md`, `scripts/on-stop.sh`.

> Day zero — vault scaffolded, nothing ingested yet. (This cache refreshes automatically after the first session that changes the wiki.)
> --- `wiki/hot.md`

#### EPI-OBJ-index
Label: Catalog and operations journal

Source-native identity: `wiki/index.md` and `wiki/log.md`. Natural-language page descriptions and operation/insight statements with symbolic wikilinks/date/action headings; local Markdown. Claimed roles: relevance selection versus operation lineage, respectively. Grouped only as navigation/lineage support here; their consumers differ: queries choose from catalog, humans/maintenance can consult history. No runtime object counterpart; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) are their update routes. No full audit invariant follows: journaling is requested in workflows, while hooks commit without checking a log entry. Fallback search counters absolute invisibility of unindexed content. SRC-1 `wiki/index.md`, `wiki/log.md`, `CLAUDE.md`, `scripts/on-stop.sh`.

> Master catalog. One line per page: wikilink + one-sentence description. Newest entries first within each section.
> --- `wiki/index.md`

> Append-only journal. New entries at the TOP. Never edit past entries.
> --- `wiki/log.md`

#### EPI-OBJ-findings
Label: Mechanical and editorial findings

Source-native identity: the two-pass lint findings presented by the foreground agent, optionally retained as `wiki/meta/lint-report-YYYY-MM-DD.md`. This is a mixed-output container, not one evaluator or one warrant class. Its symbolic mechanical part is [EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings); its natural-language editorial part is [EPI-OBJ-editorial-findings](#epi-obj-editorial-findings). Substrate: scanner stdout, foreground context, and optional Markdown report. Closest supplied [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) is the producing/consuming workflow rather than an object counterpart. The parts below own form, warrant and consumer findings separately. Retaining this container does not merge their epistemic authority or imply observed operation. SRC-1 `scripts/vault_lint.py`, `.claude/skills/lint/SKILL.md`.

> Present findings grouped by severity, each with a one-line suggested fix. If the user wants a record (or there are many findings), write it to `wiki/meta/lint-report-YYYY-MM-DD.md` (`type: meta`).
> --- `.claude/skills/lint/SKILL.md`

#### EPI-OBJ-mechanical-findings
Label: Mechanical findings

Part of: [EPI-OBJ-findings](#epi-obj-findings)

Source-native identity: `scripts/vault_lint.py` output findings and summary. Representational form: symbolic severity/check/file/message dictionaries and aggregate counts, rendered as JSON or fixed text messages; substrate: stdout, then foreground context and optionally the combined Markdown report. The Python scanner produces predicates about its decoded file snapshot, parsed fields, filenames and link maps. These warrant scanner-defined structural conclusions, not world-claim truth, heading existence or semantic duplicate detection. The foreground agent is explicitly instructed to trust this output rather than re-derive it; findings then inform proposed fixes presented to the user. Force is advisory evidence for maintenance, not automatic write rejection or epistemic acceptance of page claims. Scope/horizon: the scanned snapshot and maintenance episode; a retained report may outlast that snapshot, with no automatic freshness guarantee. The completed scanner returns zero even with findings. No actual scan output or successful repair is supplied. Unlike [EPI-OBJ-editorial-findings](#epi-obj-editorial-findings), this part is program-derived rather than model editorial judgment. The closest supplied [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) is the containing workflow, not an output counterpart. SRC-1 `scripts/vault_lint.py`, `.claude/skills/lint/SKILL.md`; implementation and doctrine/design respectively.

> findings.append({
>     "severity": severity, "check": check,
>     "file": str(path.relative_to(root)) if isinstance(path, Path) else path,
>     "message": message,
> })
> --- `scripts/vault_lint.py`

> print(json.dumps({"summary": summary, "findings": findings}, indent=2, ensure_ascii=False))
> --- `scripts/vault_lint.py`

> Trust its output; don't re-derive these by reading pages.
> --- `.claude/skills/lint/SKILL.md`

> t = m.group(1).split("|")[0].split("#")[0].strip()
> --- `scripts/vault_lint.py`

> stem = Path(target).stem
> resolved = by_name.get(stem, [])
> if not resolved:
>     check = "index_drift" if p.name == "index.md" else "dead_links"
>     add("error", check, p, f"dead link: [[{target}]]")
> --- `scripts/vault_lint.py`

#### EPI-OBJ-editorial-findings
Label: Editorial findings

Part of: [EPI-OBJ-findings](#epi-obj-findings)

Source-native identity: the lint skill's editorial findings and suggested fixes. Representational form: natural-language allegations and proposals interpreted by the foreground model and user; substrate: foreground report/context, optionally `wiki/meta/lint-report-YYYY-MM-DD.md`. The model proposes unlinked mentions, missing pages, stale claims and aging seeds through search and judgment; sampling recent pages is permitted for large vaults. These are candidate diagnoses, not deterministic structural evidence or established truths. The user receives grouped findings and suggestions, approves bulk safe fixes or individually decides deletion, merging and contradictions; the model consumes that approval to edit. Force is advisory proposal followed by model-mediated user permission, not a software write gate. Scope/horizon: current maintenance decisions and, if approved edits occur, later page consumers; report retention alone does not establish acceptance or benefit. No performed editorial check or criterion-bound truth decision is supplied. Unlike [EPI-OBJ-mechanical-findings](#epi-obj-mechanical-findings), this part is requested model judgment with user-facing proposals. The closest supplied [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) is the workflow, not a duplicate object. SRC-1 `.claude/skills/lint/SKILL.md`, doctrine/design.

> Scale to vault size — sample recent pages if the vault is large:
> --- `.claude/skills/lint/SKILL.md`

> - **One-by-one approval**: deleting orphans (isolation may be intentional), merging duplicates, resolving contradictions (needs the user's judgment on which side is true).
> --- `.claude/skills/lint/SKILL.md`

> - **Stale claims**: pages whose claims newer pages contradict, without a contradiction callout.
> --- `.claude/skills/lint/SKILL.md`

### Claims

#### EPI-CLM-structural-checks
Label: Structural correctness through text checks

Claimed operation/warrant: inspectable text permits deterministic verification of the retrieval substrate and diagnosis of what is broken. Distinct from [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh), which concerns hook refresh; no supplied claim counterpart. SRC-1 `docs/why-no-vector-db.md`, `docs/what-happens-when-you-ingest.md`, doctrine/design. The implementation of `scripts/vault_lint.py` supports a narrower structural reading: case-insensitive duplicate **basenames**, not semantic duplicates under arbitrary different names; link targets without heading validation; lenient flat frontmatter parsing. It does not check the truth of page claims or whether an index description is sufficient for recall. Comparisons with vector systems lack experimental support.

> Because the entire retrieval substrate is text, a script can verify it: `vault_lint.py`
> deterministically checks dead wikilinks, orphan pages, duplicate filenames, alias collisions,
> frontmatter gaps, index drift and cache size, and tells you exactly what is broken. No tokens,
> no model judgment.
> --- `docs/why-no-vector-db.md`

> | `duplicates` | The same page created twice under slightly different names |
> --- `docs/what-happens-when-you-ingest.md`

> lower_names[p.stem.lower()].append(p)
> --- `scripts/vault_lint.py`

#### EPI-CLM-graph-knowledge
Label: Deliberate links carry knowledge

Claimed warrant: ingest-time links encode meaningful intent/causal relationships and make one-hop reading better than similarity-radius expansion. No supplied claim counterpart; distinct from [RT-CLM-cache-refresh](runtime.md#rt-clm-cache-refresh) and [EPI-CLM-structural-checks](#epi-clm-structural-checks). SRC-1 `docs/why-no-vector-db.md`, doctrine/design. Source-native objective is visible operation and minimal installation, with explicit scale/wording caveats. [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) requests deliberate linking and conflict flags, while [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) requests bounded read/search/citation. Neither establishes link semantics are true or that retrieval comparisons hold. A `sources` relation can carry attribution; it cannot itself show the cited evidence supports a causal proposition.

> So the goal was not better retrieval. It was a system I could always see inside of, that asks
> you to install as little as possible.
> --- `docs/why-no-vector-db.md`

> A hand-placed link carries intent that a similarity score cannot reconstruct. "These two pages
> are 0.83 similar" and "this decision was made because of that constraint" are not the same
> claim. The first is a measurement; the second is knowledge. Following one hop of real links
> beats expanding a similarity radius, because the links encode why.
> --- `docs/why-no-vector-db.md`

> **Wording you did not anticipate.** If the index line and your question share no vocabulary and
> no concepts, the read path can miss where semantic search would hit. That is what the grep
> fallback is for, and grep is a weaker net than embeddings.
> --- `docs/why-no-vector-db.md`
