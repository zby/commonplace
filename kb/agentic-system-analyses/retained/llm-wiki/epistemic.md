---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LLM Wiki epistemic routes: source compilation, structural checks, delegated criticism and later reliance at the frozen commit."
run-id: AAS-2026-10-14-llm-wiki-b437987c5802-01
reviewed-boundary: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
---

# llm-wiki epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on LLM Wiki's compiled pages and later answers. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). SRC-1 is the sole frozen source. Toolkit behavior is implementation evidence; model maintenance is doctrine/design. The example contradiction ledger is available candidate state, not evidence of the route that produced or accepted it.

The consequential knowledge claim is [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge); the operational allocation is see [RT-CLM-agent-bookkeeping](runtime.md#rt-clm-agent-bookkeeping). Assessed families include source import, semantic writing, contradiction review, retention, search/expansion, structural diagnosis, status notification, scaffold replacement and instruction propagation. No host/model execution, verified acceptance history or causal experiment is supplied. Those missing items prevent findings about actual compliance, source fidelity, accepted ampliative knowledge, benefit and exercised improvement. The external qmd index and model parameters remain uninspected; this prevents conclusions about their provenance, freshness and adaptation. No new source or revised boundary is needed.

Coverage distinguishes direct source inspection here from supplied runtime findings. Every path below is SRC-1 at the frozen revision. No target execution was performed.

| Entry point or operation | Source path | Coverage and records | Limit |
|---|---|---|---|
| Ingest, query, lint and convention co-evolution instructions | `src/llm_wiki/scaffold/AGENTS.md` | Direct full read; see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync) | Requests, not model execution or acceptance trace. |
| Entire CLI dispatch: init, search, lint, list, stats, log, expand, ingest-status, backlinks, graph, new, watch, init-check | `src/llm_wiki/cli.py` | Direct full read; runtime records above plus [EPI-RTE-catalog-inspection](#epi-rte-catalog-inspection), [EPI-RTE-log-inspection](#epi-rte-log-inspection), [EPI-RTE-project-readiness](#epi-rte-project-readiness) | No hidden semantic ingest or automatic repair in this dispatch. |
| All ten registered MCP tools and stdio server | `src/llm_wiki/mcp_server.py` | Direct full read; same helpers as CLI; new records below cover omitted read operations | MCP lint reports filtered data; it has no CLI exit threshold. |
| Lint, frontmatter parsing and source coverage | `src/llm_wiki/lint.py`; `src/llm_wiki/ingest.py` | Direct full reads; [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-source-coverage](#epi-rte-source-coverage), runtime lint | No semantic source endorsement or proposition-level contradiction test. |
| BM25, qmd adapter, section extraction, links and statistics | `src/llm_wiki/search.py`; `src/llm_wiki/expand.py`; `src/llm_wiki/links.py`; `src/llm_wiki/stats.py` | Direct full reads; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search), new inspection records | Partial text and lexical scores do not establish truth. |
| Init/new force paths, pending poller and prompt sync | `src/llm_wiki/bootstrap.py`; `src/llm_wiki/new_page.py`; `src/llm_wiki/watch.py`; `scripts/sync_agents.py` | Supplied findings, not direct reads: [RT-RTE-project-init](runtime.md#rt-rte-project-init), [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch), [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync) | No independent implementation extension or observed operation asserted. |
| Checklist/demo callers, CI and development hooks | `scripts/ingest-checklist.sh`; `scripts/demo-walkthrough-fast.sh`; `.github/workflows/ci.yml`; `.pre-commit-config.yaml` | Supplied caller account plus scoped source search for hooks/checks; developer hook deliberately excluded by boundary | No deployed automatic maintenance or verified CI result inferred. Developer hook enforcement remains excluded. |
| Public compiled-knowledge claim and illustrative conflict | `README.md`; `examples/demo/wiki/contradictions.md` | Direct README opening and full contradiction page; [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge), [EPI-OBJ-contradictions](#epi-obj-contradictions) | Remaining examples/tests unassessed for semantic quality; no system-complete corpus-quality negative. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw](#epi-obj-raw) | External source assertions, whatever their truth | Human-curated import input | see record | Source truth and warrant not evaluated here. |
| [EPI-OBJ-source-pages](#epi-obj-source-pages) | Summaries of imported assertions | Source attribution and compiled source memory | see record | Summary fidelity cannot be established from prescribed reading. |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Entity/concept claims, evolving synthesis and filed answers | Persistent account and later answer context | see record | Semantic transformations and acceptance history are unknown. |
| [EPI-OBJ-contradictions](#epi-obj-contradictions) | Paired conflicting claims and proposed disposition | Conflict ledger | see record | An open conflict is not resolved knowledge or a rejection decision. |
| [EPI-OBJ-source-metadata](#epi-obj-source-metadata) | File/path association, not source truth | Symbolic coverage and lineage pointer | see record | Reference existence does not establish support for claims. |
| [RT-CMP-agent](runtime.md#rt-cmp-agent) | Not determinable at parameter level | Semantic interpretation | see record | Exact parameters, version and endpoint mutability uninspected independently. |

Instructions, templates and operation logs additionally affect guidance or inspection; their identities and routes are see [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions), [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync) and [EPI-RTE-log-inspection](#epi-rte-log-inspection). A search response is transient selected content from the page objects, not a separately accepted knowledge object.

## Authority-route ledger

Record-owned fields are cited rather than reproduced. Each compact row below separates the consequential functions even where one source route supplies several functions. Architectural status is assessed here; activation, timing, predicates, result and consumers are see the cited record unless a narrower license is stated.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-source-pages](#epi-obj-source-pages)
Content/update relation: truth-apt transformation: acquisition/import — external assertions enter the intended wiki; source warrant unknown.
Transition or check target: Raw assertions to source summary.
Evaluator/condition and domain: see route; reading/discussion is not an explicit source-truth evaluator.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: Protocol only, not an implemented semantic writer.
Epistemic authority and scope: Imported attribution, not verified truth; interpretation fidelity remains unknown.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions).
Evidence source ID and local anchor: see route.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: none; import is not knowledge production.
Gap/limit: No imported source's warranted premises or acceptance are established.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: truth-apt transformation: indeterminate — summary, synthesis and answer instructions permit reshaping, derivation or conjecture; no paired input/output with verified interpretation establishes which.
Transition or check target: Source/page assertions to entity, concept, synthesis and answer claims.
Evaluator/condition and domain: see routes; external model interpretation, not a formal entailment check.
Activation and timing: see routes.
Possible or observed result: see routes.
Implemented force: Requested model writing and synthesis.
Epistemic authority and scope: Candidate claims only; novelty or citations confer no acceptance.
Operational authority: behavior permitted, blocked, or changed: see routes.
Behavioral-authority path: consumer, channel, force, horizon: see routes and [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions).
Evidence source ID and local anchor: see routes.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: Knowledge wording exceeds established warrant if taken as verified knowledge.
Gap/limit: Missing semantic correspondence prevents an entailed/ampliative classification; inability to prove entailment alone is not non-entailment evidence.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-source-pages](#epi-obj-source-pages), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-contradictions](#epi-obj-contradictions).
Content/update relation: no content change — persistence of separately authored candidates.
Transition or check target: Edited/filed Markdown to later project sessions.
Evaluator/condition and domain: see routes; human discussion is bypassable in batch mode; filing is offered, not an enforced evidence-consuming approval.
Activation and timing: see routes.
Possible or observed result: see routes; example files show availability only.
Implemented force: Semantic retention requested; toolkit read-back exists separately.
Epistemic authority and scope: Retention records no named criterion accepting a claim for reliance.
Operational authority: behavior permitted, blocked, or changed: see routes.
Behavioral-authority path: consumer, channel, force, horizon: see routes.
Evidence source ID and local anchor: see routes.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: Persistent cross-linking is not lifecycle integration after acceptance.
Gap/limit: No separately established lifecycle-integration or acceptance route for these claims; this does not prohibit an external human from accepting them.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-contradictions](#epi-obj-contradictions), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change — semantic review, separate from proposed revision.
Transition or check target: New-source conflicts with prior claims; stale conflicts in the ledger.
Evaluator/condition and domain: see routes; agent interprets assertions and human emphasis.
Activation and timing: see routes.
Possible or observed result: Requested flagging/review; see routes.
Implemented force: Advisory protocol, no automatic claim withdrawal.
Epistemic authority and scope: Potential criticism only; no evidenced test result, blame assignment or resulting changed reliance.
Operational authority: behavior permitted, blocked, or changed: see routes.
Behavioral-authority path: consumer, channel, force, horizon: see routes.
Evidence source ID and local anchor: see routes.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: none.
Gap/limit: Review and revision instructions do not supply a recorded acceptance or rejection criterion. Open ledger state is a countercase to assuming every conflict is resolved.

Route ID: [EPI-RTE-contradiction-check](#epi-rte-contradiction-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradictions](#epi-obj-contradictions), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change.
Transition or check target: Marker-bearing prose and lexical ledger references, not compatibility of propositions.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: Advisory lint diagnostic; see record.
Epistemic authority and scope: Licenses only the lexical condition, not truth, contradiction resolution or endorsement.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint).
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: A semantic reading of the check would exceed its domain.
Gap/limit: Silent checks can coexist with false claims or unresolved contradictions.

Route ID: [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [EPI-RTE-source-coverage](#epi-rte-source-coverage), [EPI-RTE-project-readiness](#epi-rte-project-readiness)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-metadata](#epi-obj-source-metadata); page/file structure.
Content/update relation: no content change.
Transition or check target: File existence, frontmatter fields, resolvable links, discoverability and raw/source mapping; split targets and evaluators are see records.
Evaluator/condition and domain: see records; deterministic filesystem/syntax conditions, no expected answer for substantive claims.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: Reports and readiness error; lint exit is separated below.
Epistemic authority and scope: Structural evidence only, not semantic fidelity, completeness of maintenance or source truth.
Operational authority: behavior permitted, blocked, or changed: see records.
Behavioral-authority path: consumer, channel, force, horizon: see records.
Evidence source ID and local anchor: see records.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: Labels “ingested” and “ready” are structurally bounded.
Gap/limit: No blanket inference that the maintained corpus is healthy or warranted.

Route ID: [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: Structural lint issue report, not a substantive candidate claim.
Content/update relation: no content change.
Transition or check target: CLI process success under configured fail-on severity.
Evaluator/condition and domain: see record; deterministic threshold over unfiltered issues.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: Enforcing exit status within this invocation; no page-write admission gate. MCP reports without this exit policy.
Epistemic authority and scope: No claim acceptance; successful continuation means threshold not triggered.
Operational authority: behavior permitted, blocked, or changed: see record; downstream shell continuation can depend on status if caller uses it.
Behavioral-authority path: consumer, channel, force, horizon: see record; actual automated downstream consumer unobserved.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Display filters and fail-on none defeat any inference from “no issues” display to universal health.

Route ID: [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-source-pages](#epi-obj-source-pages).
Content/update relation: truth-apt transformation: non-ampliative reshaping — lexical ranking, snippet and section selection; qmd's internal content relation remains unknown.
Transition or check target: Query to selected page content available to caller/model.
Evaluator/condition and domain: see records; relevance score or heading match, not a truth evaluator.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: Ranking and selected delivery; agent consumption remains doctrinal.
Epistemic authority and scope: None added. Omitted context can remove qualifications; full page remains reachable.
Operational authority: behavior permitted, blocked, or changed: see records.
Behavioral-authority path: consumer, channel, force, horizon: see records.
Evidence source ID and local anchor: see records.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: Retrieval does not certify retained content.
Gap/limit: External qmd lineage/freshness uninspected; no observed model benefit.

Route ID: [EPI-RTE-catalog-inspection](#epi-rte-catalog-inspection), [EPI-RTE-log-inspection](#epi-rte-log-inspection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: Corpus paths, wikilinks and operation headings.
Content/update relation: truth-apt transformation: non-ampliative reshaping — returned claims concern encoded files/links/log matches, not truth of their prose.
Transition or check target: Catalog/graph/backlinks and recent operation selection.
Evaluator/condition and domain: see records.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: Advisory inspection and selected delivery.
Epistemic authority and scope: Graph presence and parseable log headings only; no authentication or acceptance warrant.
Operational authority: behavior permitted, blocked, or changed: see records.
Behavioral-authority path: consumer, channel, force, horizon: see records.
Evidence source ID and local anchor: see records.
Claim IDs or none: none.
Mismatch marker or none: Log omission can hide hyphenated declared operations.
Gap/limit: Inspection counts and missing links are not a causal maintenance trace.

Route ID: [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-project-init](runtime.md#rt-rte-project-init)
Route function: retention
Architectural status: implemented
Object/candidate ID: Rendered templates/scaffold instructions and pages.
Content/update relation: non-truth-apt policy/content update: scaffold and placeholder substitution; no substantive knowledge inference.
Transition or check target: Caller-selected template/project files to disk.
Evaluator/condition and domain: see records; existing destination rejection is overridable with force.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: Direct filesystem write or rejection; no semantic check.
Epistemic authority and scope: None added; forced replacement can remove formerly useful candidate text without withdrawal assessment.
Operational authority: behavior permitted, blocked, or changed: see records.
Behavioral-authority path: consumer, channel, force, horizon: see records.
Evidence source ID and local anchor: see records.
Claim IDs or none: none.
Mismatch marker or none: Countercase to treating protocol as enforced on every write.
Gap/limit: No multi-page rollback or acceptance mechanism established.

Route ID: [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: Maintainer instructions, not a truth-apt accepted claim.
Content/update relation: non-truth-apt policy/content update: propagate canonical conventions to scaffold/examples.
Transition or check target: Canonical text to future instruction readers.
Evaluator/condition and domain: see record; copying checks no improvement objective.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: File-copy propagation; behavior effects require host loading and compliance.
Epistemic authority and scope: No empirical warrant added to a convention.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions).
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Policy propagation is not demonstrated evidence-responsive self-improvement.

Route ID: [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-metadata](#epi-obj-source-metadata).
Content/update relation: no content change.
Transition or check target: Newly pending names to notification.
Evaluator/condition and domain: see record and [EPI-RTE-source-coverage](#epi-rte-source-coverage).
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: Notification only in shipped CLI consumer.
Epistemic authority and scope: Pending coverage, not semantic staleness or endorsement.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge).
Mismatch marker or none: Watch does not keep knowledge current itself.
Gap/limit: No same-name content-change notification or automatic semantic refresh established.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | see record | see record | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | see [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch) | None supplied; example state does not authenticate the loop | No experiment; manual/model semantic updates depend on excluded host; force and batch paths bypass possible discussions | Persistence and retrieval capacity plus compilation/maintenance protocol | Truth, currentness and compounding benefit not established. “Compiled” is a workflow metaphor, not checked entailment. |
| [RT-CLM-agent-bookkeeping](runtime.md#rt-clm-agent-bookkeeping) | see record | see record | see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) | see [EPI-RTE-source-coverage](#epi-rte-source-coverage), [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) for supporting diagnostics, not semantic execution | None supplied | No compliance/quality attribution | Clear allocation of human curation and agent bookkeeping | Toolkit support does not implement the external agent's semantic role. |

## Bounded conclusion

LLM Wiki can persist scaffold pages and return selected existing text. It asks an external agent to import source assertions, author summaries and synthesis, file answers and revise conflicts. Import acquires assertions; source warrant remains unknown. No inspected formal domain or accepted premise set establishes novel entailed claims. Instructions alone do not distinguish non-ampliative semantic rewriting from conjecture. See the separate transformation and retention ledger entries for [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).

Structural evaluators have real but narrow targets. They check references, fields and existence, rank lexical relevance and identify marker language. They do not decide the truth of wiki assertions. CLI lint can enforce a process-status threshold, not knowledge admission. Neither that threshold, a source-page mapping, citation, cross-link nor optional answer filing supplies an evidence-consuming acceptance decision naming criterion, intended use and scope. Consequently no produced accepted ampliative claim or subsequent lifecycle integration is established by this evidence. This is a bounded finding about the shipped protocol and toolkit, not a prohibition on external human judgment. See [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [EPI-RTE-source-coverage](#epi-rte-source-coverage) and [EPI-RTE-contradiction-check](#epi-rte-contradiction-check).

The contrary witnesses matter: the protocol does require complete source reading, human discussion outside batch mode, conflict review and source citations. These are potential error-control affordances, not absent criticism. The example retains an explicitly open conflict, and lexical lint can miss genuine conflicts. Forced page creation can replace content without semantic withdrawal. No observed criticism-to-revision-to-next-round trace closes the theory-builder conditions left uninspected in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Addressability is at page/heading level; retained knowledge and method text have intended session horizons, while exercised consumption and improved future capacity remain unobserved independently.

Instruction co-evolution and synchronization form a distinct non-truth-apt policy route. The changed text can reach later agents through natural-language instructions; host loading and compliance are not established. Learning, reflection, autonomy and exercised self-improvement do not follow from copying conventions or retaining pages. Parameter change, version pinning and endpoint replacement remain independently uninspected in [RT-CMP-agent](runtime.md#rt-cmp-agent). No single epistemic verdict or measured compounding benefit follows.

## Shared records

### Operative objects

#### EPI-OBJ-raw
Label: Raw sources

Source-native identity: `raw/` documents. Representational form: natural-language source content, with possible images requiring separate reading. Storage substrate: project filesystem. No object counterpart is declared in the supplied runtime; this is the input object of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not that route itself. SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, doctrine/design.

> 1. **Read** the raw source completely (text first; view images separately if present).
> --- `src/llm_wiki/scaffold/AGENTS.md`

#### EPI-OBJ-source-pages
Label: Source pages

Source-native identity: `wiki/sources/` summaries, distinct from raw source documents and reusable synthesis/answer pages. Representational form: natural-language compiled assertions; source pointer metadata is assessed separately. Storage substrate: Markdown files. No supplied operative-object counterpart; intended output of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, doctrine/design.

> | Source | `wiki/sources/` | One summary per ingested raw document |
> --- `src/llm_wiki/scaffold/AGENTS.md`

#### EPI-OBJ-wiki-pages
Label: Entity concept synthesis and answer pages

Source-native identity: entity/concept pages, `wiki/synthesis.md` and filed `wiki/answers/` pages. Representational form: natural-language claims for agent/human interpretation. Storage substrate: Markdown files. These share semantic-writing admission and later retrieval but differ from source summaries and conflict ledger. No supplied object counterpart; these are candidate outputs/inputs of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, doctrine/design.

> 4. **Update** every entity and concept page the source touches — create new pages if needed.
> 5. **Revise** `wiki/synthesis.md` if the source shifts the overall picture.
> --- `src/llm_wiki/scaffold/AGENTS.md`

> 5. **Offer** to file the answer: valuable analyses should become `wiki/answers/<slug>.md`.
> --- `src/llm_wiki/scaffold/AGENTS.md`

#### EPI-OBJ-contradictions
Label: Contradictions ledger

Source-native identity: `wiki/contradictions.md`, paired conflicting claims and status prose. Representational form: natural-language claims even when displayed in a Markdown table. Storage substrate: project file. Distinct from synthesis and source metadata because its consumer is conflict review and its role is to preserve unresolved disagreement. No supplied object counterpart; linked to [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint). SRC-1: `src/llm_wiki/scaffold/AGENTS.md`, doctrine/design; `examples/demo/wiki/contradictions.md`, illustrative available state. The example gives two different claimed search thresholds and keeps the disagreement open. This is not provenance for a model's judgment or evidence of acceptance.

> 6. **Flag** contradictions in `wiki/contradictions.md` when new data conflicts with existing claims.
> --- `src/llm_wiki/scaffold/AGENTS.md`

> | Index + lexical search works to ~100 sources without embedding infrastructure | [[sources/karpathy-llm-wiki-gist]] | Hybrid search improves recall before ~100 pages when cross-links are sparse | [[sources/qmd-hybrid-search]] | **open** — adopt qmd when query quality drops, not at a fixed page count |
> --- `examples/demo/wiki/contradictions.md`

#### EPI-OBJ-source-metadata
Label: Source raw-file and source-reference metadata

Source-native identity: YAML `raw_file` and `sources` fields. Representational form: symbolic values when consumed by coverage/lint, rather than natural-language truth assertions. Storage substrate: frontmatter in Markdown files. Distinct operative part from source prose and a metadata part spanning source and other page files; no single supplied object counterpart. Related supplied route is [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch). SRC-1: `src/llm_wiki/ingest.py`, `src/llm_wiki/lint.py`, implementation.

> raw_file = meta.get("raw_file") if meta else None
> --- `src/llm_wiki/ingest.py`

> if resolve_link(normalized, slug_index) is None:
> --- `src/llm_wiki/lint.py`

### Routes

#### EPI-RTE-contradiction-check
Label: Contradiction marker and ledger check
Part of: [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)

Endpoints/progression: page prose after wikilink removal → regex marker check → lexical page-name presence in ledger → warning/info issue → CLI/MCP caller. Owner: Python rules; external maintainer owns subsequent judgment and fixes. Context/state/action effects: reads page/ledger; appends transient issues, does not revise claims. SRC-1: `src/llm_wiki/lint.py`, implementation. This is a material diagnostic part, not a second identity for whole lint.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Warning `contradiction-unfiled` for eligible marker-bearing page absent from ledger; separate info hint on other eligible pages.
- Later read-back: inapplicable — issue report is not automatically retained.
- Delegated visibility: CLI/MCP receive issues subject to display filters; instructed maintainer can review them.
- Selection predicate: Regex markers plus stem/prefix exemptions; unfiled check needs an existing ledger and page name not present by substring.
- Invalidation or expiry: Recomputed on current files; no persistent issue state.
- Activation or effect: Produces diagnostic; human/model correction unobserved.
- Evidence limits: Lexical predicates do not compare claims or evaluate truth; no run trace.

Diagnosis mode is an open lint request. Code proposes the diagnostic and decides lexical eligibility; caller can filter or ignore it. Agent/human decides semantic correction and can decline a proposed fix. Reference outcome is the string condition, not an answer oracle for propositions. A concrete deduction from implementation: an eligible source page containing “These claims do not conflict” triggers the marker test; with a present ledger lacking its name it receives the warning despite asserting no conflict. Conversely a real pair “X occurs”/“X never occurs” can lack all marker words and produce no such warning. Adding the page stem anywhere in ledger prose suppresses the unfiled issue without requiring a conflict entry. These countercases bound the license; they are not target executions.

> if not CONTRADICTION_MARKERS.search(prose):
>     return
> if _page_in_contradictions_ledger(page, contradictions_text):
>     return
> --- `src/llm_wiki/lint.py`

> return any(token in lowered for token in checks)
> --- `src/llm_wiki/lint.py`

#### EPI-RTE-source-coverage
Label: Raw source coverage classification
Part of: [RT-RTE-pending-watch](runtime.md#rt-rte-pending-watch)

Endpoints/progression: raw file enumeration and source frontmatter → filename mapping → ingested/pending/incomplete/orphan records → status CLI/MCP or watcher. Owner: deterministic software. Context/state/action effects: filesystem reads and transient classifications, no semantic ingest or write. This part is the classifier used inside pending-watch and exposed separately by ingest-status; it is not a duplicate of the notification loop. SRC-1: `src/llm_wiki/ingest.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Raw/source association statuses and paths.
- Later read-back: Reads current retained source metadata on later requests/polls; results themselves are not persisted.
- Delegated visibility: CLI/MCP caller sees labels; watch consumes pending names.
- Selection predicate: Enumerated raw files excluding README/.gitkeep; source pages with truthy raw_file populate map; absent field marks incomplete, absent raw filename marks orphan.
- Invalidation or expiry: Recomputed per call; same-name content changes do not invalidate mapped status.
- Activation or effect: Classifies coverage and supplies watch selection; semantic completion unobserved.
- Evidence limits: Filename relation is the entire license; duplicate mapping can replace earlier page association, and no source/body comparison occurs.

Open inspection mode. Software decides statuses; human chooses raw files and author/model supplies metadata. No substantive expected-answer oracle or admission veto exists in this reader. Concrete implementation deduction: with raw `a.txt` and a source page whose frontmatter says `raw_file: a.txt`, even an empty summary body yields “ingested.” This is coverage, not source fidelity or completed maintenance.

> status="ingested" if source_page else "pending",
> --- `src/llm_wiki/ingest.py`

> mapping[str(raw_file)] = page.rel_path
> --- `src/llm_wiki/ingest.py`

#### EPI-RTE-catalog-inspection
Label: Catalog statistics and link graph inspection

Endpoints/progression: CLI/MCP list/stats/backlinks/graph → page enumeration, prefix counts or unique wikilink resolution → caller. Owner: software; caller selects operation/type/page. Context/state/action effects: current retained file corpus and link index; no write. Distinct from [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query): these return paths/counts/edges, not BM25 snippets or expanded prose. No supplied route counterpart covers these exposed operations. SRC-1: `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/links.py`, `src/llm_wiki/stats.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Paths, counts, inbound page references or graph nodes/edges; invalid explicit backlink page returns error.
- Later read-back: Current accumulated wiki files supply later inspection requests; reports are not automatically persisted.
- Delegated visibility: CLI/MCP caller receives derived structure, not whole page assertions.
- Selection predicate: List/type and stats use path prefixes; backlinks selects a resolved requested page; graph includes uniquely resolved extracted links and deduplicates edges.
- Invalidation or expiry: Recomputed from current files; edits/deletions change subsequent reports.
- Activation or effect: Advisory navigation and structural evidence; no truth validation or cleanup.
- Evidence limits: Ambiguous/unresolved links produce no graph edge; graph does not preserve fragment/alias distinctions or attest claim support.

Force/horizon: caller inspection within request; later human/model can choose navigation but actual consumption is unobserved. No content admission or answer oracle applies. A concrete derivation: two occurrences of `[[concepts/x]]` from a page to one uniquely resolving target yield one graph edge, because extraction is a set and edges are deduplicated. That deduction warrants encoded link structure only.

> for target in extract_wikilinks(text):
>     resolved = resolve_link(target, slug_index)
>     if not resolved:
>         continue
>     key = (page.rel_path, resolved.rel_path)
>     if key in seen_edges:
>         continue
> --- `src/llm_wiki/links.py`

#### EPI-RTE-log-inspection
Label: Recent operation log inspection

Endpoints/progression: CLI log/MCP recent-log or stats → read log → regex matching headings → selected entries/count → caller. Owner: deterministic parser. Context/state/action effects: retained operation text; no authentication or write. Distinct from [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query): parser returns operation headings rather than search hits/answers. No counterpart after comparison with supplied routes. SRC-1: `src/llm_wiki/stats.py`, implementation; prescribed operations in `src/llm_wiki/scaffold/AGENTS.md`, doctrine/design.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Last limit matching heading records in file order; stats counts matches.
- Later read-back: Human/model-appended log headings can reach a later inspection request; stored narrative below heading is not returned by parser.
- Delegated visibility: CLI/MCP caller receives date, operation and detail only.
- Selection predicate: Regex requires word-only operation followed by separator; Python final-list slice selects returned records.
- Invalidation or expiry: Reparsed each invocation; edits/removal affect future inspection; no tamper protection.
- Activation or effect: Advisory reported-operation display/count, not semantic acceptance or automatic adaptation.
- Evidence limits: Parseable headings do not authenticate action; hyphenated declared operations are omitted.

Concrete deduction: `## [2026-10-14] ingest | a` matches; `## [2026-10-14] answer-filed | a` does not, because operation `\w+` cannot consume the hyphen and then match the required space. Thus declared `answer-filed` and `synthesis-update` headings can remain in raw log while absent from recent-log/stats output. This corrects the possible completeness inference, not the supplied runtime record's identity.

> LOG_ENTRY_RE = re.compile(r"^## \[([^\]]+)\] (\w+) \| (.+)$", re.MULTILINE)
> --- `src/llm_wiki/stats.py`

#### EPI-RTE-project-readiness
Label: Project structure readiness check

Endpoints/progression: CLI init-check → required path existence → display marks → success text or ClickException. Owner: software; human/caller invokes. Context/state/action effects: project filesystem, no semantic content read or write. Distinct from [RT-RTE-project-init](runtime.md#rt-rte-project-init): this verifies existing paths rather than producing scaffold. No supplied record counterpart for this exposed command. SRC-1: `src/llm_wiki/cli.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Existence indicators and success, or project-incomplete exception.
- Later read-back: inapplicable — no accumulated content read; current path existence only.
- Delegated visibility: CLI caller receives marks and startup guidance.
- Selection predicate: AGENTS.md, index.md, log.md, synthesis.md, raw and templates paths must exist.
- Invalidation or expiry: Recomputed each invocation.
- Activation or effect: Current CLI continuation or failure; no gate on subsequent independent writes.
- Evidence limits: Does not require correct file kind, schema, source fidelity or answer quality; no execution trace.

Diagnosis mode: open request. Program decides existence; caller can ignore failure or repair and retry. Reference outcome is all named paths existing, not an answer oracle for substantive claims. Missing paths reject this readiness request only. No claim proposal, acceptance or rollback occurs.

> exists = path.exists()
> --- `src/llm_wiki/cli.py`

> raise click.ClickException("Project structure is incomplete.")
> --- `src/llm_wiki/cli.py`

### Claims

#### EPI-CLM-compiled-knowledge
Label: Compiled current and compounding knowledge

Claimed operation: ingest integrates extracted source content, entity updates, synthesis and contradictions into persistent knowledge, described as compiled once/kept current and compounding. Distinct from [RT-CLM-agent-bookkeeping](runtime.md#rt-clm-agent-bookkeeping), which allocates work between human and agent; this is the stronger product/warrant and benefit framing. SRC-1: `README.md`, doctrine/design, not evidence of actual truth or comparative performance.

> **LLM Wiki is different.** When you add a source, the agent reads it, extracts key information, and integrates it into a persistent wiki — updating entity pages, revising synthesis, flagging contradictions. Knowledge is **compiled once and kept current**.
> --- `README.md`

> A **reference implementation** of [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — a compounding personal knowledge base where the LLM maintains structured, interlinked markdown instead of re-deriving everything from raw chunks on every question.
> --- `README.md`
