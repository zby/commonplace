---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AI Research OS Workshop: source attribution, synthesized wiki claims, maintenance checks and the limits of downstream reliance."
run-id: AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01
reviewed-boundary: dc6660555266239cd36483cf51b5ab39febacf02
---

# AI Research OS Workshop epistemic report

## Source-and-claim boundary

The question is what licenses reliance on this plugin's acquired source material and generated research claims, and how those claims or their criticism affect later work. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). The shipped plugin is a host-mediated research-memory workflow, not the host model or source services. SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments.

Direct inspection here adds complete source-writer, comparison-writer, summary-writer, lint-driver/judge, four mechanical lint scripts and `_lintlib.py`, dedup helper, render driver and both manifests. The rest of the trace relies on the supplied runtime records as explicitly indicated below. No target code was executed. Available files left unread are not inaccessible. No example output was used to establish production, checking or acceptance provenance.

| Entry point or operation | Source path, SRC-1 | Record coverage and inspection basis | Limit and prevented conclusion |
|---|---|---|---|
| Registration | `.claude-plugin/marketplace.json`; `plugins/ai-research-os/.claude-plugin/plugin.json` | Direct complete reads; see [RT-OBJ-skill-instructions](runtime.md#rt-obj-skill-instructions) | These manifests register the plugin; they do not establish host grants or automatic evaluators. No deployed host hook coverage asserted. |
| Init/append, web/PDF/YouTube/local/connector acquisition | `plugins/ai-research-os/skills/research/SKILL.md`; `plugins/ai-research-os/skills/research/agents/builder.md` | Supplied [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest); driver targeted search here | PDF/transcript extraction internals and source CLI references remain uninspected here. Prevents extraction-fidelity and complete source-warrant conclusions. |
| Deep discovery, relevance selection and next queries | `plugins/ai-research-os/skills/research/agents/researcher.md`; `plugins/ai-research-os/skills/research/agents/gap_analyzer.md`; `plugins/ai-research-os/skills/research/scripts/dedup_findings.py` | Supplied [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery); dedup directly read | External search/model responses unobserved; no exhaustive discovery conclusion. |
| GitHub curated specs and clone recovery | `plugins/ai-research-os/skills/research/agents/github_spec_writer.md`; `plugins/ai-research-os/skills/research/scripts/github_clone.py` | Supplied [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest) | Parser internals uninspected; provider-independent code reading is not verification of the generated architecture account. |
| Source-page construction | `plugins/ai-research-os/skills/research/agents/source_writer.md` | Direct [EPI-OBJ-source-pages](#epi-obj-source-pages); supplied [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) | No summary-fidelity or quote-verification execution evidence. |
| Entity/concept and overview/thesis construction | `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`; `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md` | Entity writer supplied by [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest); summary writer directly read, [EPI-OBJ-synthesis](#epi-obj-synthesis) | No exercised criticism/revision or accepted thesis established. |
| Comparison generation/refusal | `plugins/ai-research-os/skills/research/agents/comparison_writer.md` | Direct [EPI-RTE-comparison-write](#epi-rte-comparison-write) | Agent artifact exists; driver dispatch to it is not established by the inspected steps. Lint's suggested render command has no matching format. |
| Canonical catalog/navigation | `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research/scripts/build_index_md.py` | Supplied [RT-RTE-index-build](runtime.md#rt-rte-index-build) | Metadata projection and ordering do not verify source truth or pointer fidelity. |
| Query/load/filter/compose and save-back | `plugins/ai-research-os/skills/research/SKILL.md`; `plugins/ai-research-os/skills/research/CONVENTIONS.md` | Supplied [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); driver targeted search | Conflicting save scopes retained; no conclusion that a two-source answer becomes accepted knowledge. |
| Four mechanical lint operations | `plugins/ai-research-os/skills/research-lint/scripts/lint_orphans.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_comparisons.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`; `plugins/ai-research-os/skills/research-lint/scripts/_lintlib.py` | Direct complete reads, [EPI-RTE-lint-mechanical](#epi-rte-lint-mechanical) | Implemented structural checks, not factual adjudication. Resolves the runtime's imported-resolver inspection limit without changing its supplied record. |
| Semantic lint, flags, append and cleanup | `plugins/ai-research-os/skills/research-lint/SKILL.md`; `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md` | Direct reads and [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance) | Wiki-only eight-page cap; older findings stay. No system-wide withdrawal or complete semantic audit established. |
| Distill matching/export | `plugins/ai-research-os/skills/research-distill/SKILL.md` | Supplied [RT-RTE-distill-export](runtime.md#rt-rte-distill-export) | No exact quote/match accuracy or later writer-use observation. |
| Four render formats, chart execution, retry/noop | `plugins/ai-research-os/skills/research-render/SKILL.md`; `plugins/ai-research-os/skills/research-render/agents/chart_writer.md` | Driver directly read; chart supplied by [RT-RTE-render-output](runtime.md#rt-rte-render-output) | Marp/canvas/brief agent bodies remain uninspected here; prevents complete classification of their content changes and checks. Chart success would not establish truth of hard-coded data. |
| Connector usage and opaque numerical state | `plugins/ai-research-os/skills/obsidian-cli/SKILL.md`; `plugins/ai-research-os/skills/readwise-cli/SKILL.md`; `plugins/ai-research-os/skills/nlm-skill/SKILL.md` | Supplied [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-CMP-notebooklm-model](runtime.md#rt-cmp-notebooklm-model), boundary | External implementations excluded; exact version, parameter updates and endpoint substitution remain uninspected. |

Consequential attribution/confidence claims are [EPI-CLM-source-attribution](#epi-clm-source-attribution) and [EPI-CLM-synthesis-confidence](#epi-clm-synthesis-confidence). A maintenance recommendation with a missing dispatch is [EPI-CLM-comparison-repair](#epi-clm-comparison-repair). Operational policies remain the supplied [RT-CLM-query-safety](runtime.md#rt-clm-query-safety), [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy) and [RT-CLM-index-contract](runtime.md#rt-clm-index-contract). Uninspected extraction/render/connector branches prevent a system-complete negative about all epistemic routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-skill-instructions](runtime.md#rt-obj-skill-instructions) | Policy text, not research evidence | see record | SRC-1 `plugins/ai-research-os/skills/research/CONVENTIONS.md` | Instructed compliance differs from checked compliance. |
| [RT-OBJ-python-helpers](runtime.md#rt-obj-python-helpers) | Code predicates; not evidence for external-topic claims | see record | SRC-1 `plugins/ai-research-os/skills/research/scripts/dedup_findings.py` | Fixed rules can justify only their encoded output relation. |
| [EPI-OBJ-source-pages](#epi-obj-source-pages) | Attributed source claims, quotes, and model interpretations | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/source_writer.md` | Incomplete raw reads permitted; fidelity unverified. |
| [EPI-OBJ-synthesis](#epi-obj-synthesis) | Thesis, supporting moves, dependencies and counter-evidence | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md` | Confidence is a requested heuristic, not calibrated warrant. |
| [EPI-OBJ-comparison](#epi-obj-comparison) | Contrasts and context-relative recommendations | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/comparison_writer.md` | Source-page proxies; no exercised generator trace. |
| [EPI-OBJ-lint-findings](#epi-obj-lint-findings) | Structural propositions, opposing claims, stale flags; questions are not assertions | see record | SRC-1 `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md` | Structural JSON and semantic judgment have different licenses. |
| [EPI-OBJ-raw](#epi-obj-raw) | External source claims/captions/highlights and assets | see record | SRC-1 `plugins/ai-research-os/skills/research/CONVENTIONS.md` | Imported warrant unknown; extraction/rewriting may change fidelity. |
| [EPI-OBJ-index](#epi-obj-index) | Source metadata, summaries, pointers; scores are selection policy | see record | SRC-1 `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py` | No fact or pointer validation. |
| [EPI-OBJ-topic-pages](#epi-obj-topic-pages) | Entity/concept claims and tensions; overview groupings | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md` | Different argumentative and navigation outputs remain separate content edges in ledger. |
| [EPI-OBJ-repo-specs](#epi-obj-repo-specs) | Repository mechanism explanations | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/github_spec_writer.md` | Bounded reading and unresolved destination. |
| [EPI-OBJ-query-content](#epi-obj-query-content) | Answer assertions and intended saved knowledge; question pointers | see record | SRC-1 `plugins/ai-research-os/skills/research/SKILL.md` | Save permission conflicts; question itself is not an assertion. |
| [EPI-OBJ-research-appendix](#epi-obj-research-appendix) | Matched claims and quote fragments | see record | SRC-1 `plugins/ai-research-os/skills/research-distill/SKILL.md` | Match/fidelity unobserved. |
| [EPI-OBJ-render-content](#epi-obj-render-content) | Prose/graph claims and chart snapshot data | see record | SRC-1 `plugins/ai-research-os/skills/research-render/SKILL.md` | Format bodies partly uninspected; snapshot reproduction not truth. |
| [EPI-OBJ-chart-program](#epi-obj-chart-program) | Embedded data may be truth-apt; execution instructions are not | see record | SRC-1 `plugins/ai-research-os/skills/research-render/agents/chart_writer.md` | Code execution has a separate force from claim interpretation. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | not determinable within opaque parameter state | see record | SRC-1 `plugins/ai-research-os/skills/research/SKILL.md` | No individuated stored propositions, update or exact-version evidence. |
| [RT-CMP-notebooklm-model](runtime.md#rt-cmp-notebooklm-model) | not determinable within opaque parameter state | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/researcher.md` | Returned answers acquire candidate content; provider state is unassessed. |

Imported source warrant is unknown: copying and citation do not establish the imported proposition's truth. The inventory separates accumulated outputs from the supplied static instruction/tool objects; component records cover opaque numerical alternatives.

## Authority-route ledger

Each route below is separated by consequential function. Fields owned by supplied records say `see`; this overlay adds the epistemic distinction, not a second declaration of their referents. All operation remains unobserved.

Route ID: [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: acquired raw text and [EPI-OBJ-source-pages](#epi-obj-source-pages).
Content/update relation: truth-apt transformation: acquisition/import for fetched/copied content; source warrant unknown. The source-page edge is truth-apt transformation: indeterminate: intended attribution/compression, with interpretation or unsupported additions possible; actual paired input/output needed to distinguish preservation, entailment or ampliation.
Transition or check target: sources into raw, then raw into summary/claims/quotes.
Evaluator/condition and domain: model source writer selects source substance; no independently checked semantic-preservation decision.
Activation and timing / possible or observed result / implemented force: see route; instructions afford direct writes, not observed production.
Epistemic authority and scope: candidate attributed accounts, not accepted external-topic truths.
Operational authority / behavioral-authority path: downstream wiki writers receive source pages instead of raw; current ingest and later queries, advisory evidence through model interpretation. See route and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/source_writer.md`.
Claim IDs: [EPI-CLM-source-attribution](#epi-clm-source-attribution).
Mismatch marker / gap/limit: links and synthesis markers request lineage; they do not verify fidelity. Long-file read policy can omit later content.

Route ID: [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: entity/concept, overview and [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: truth-apt transformation: indeterminate. The thesis/assumptions template requests argumentation; non-entailment of a specific produced proposition cannot be established without its source premises and result. Navigation grouping may merely reshape; argumentative synthesis may conjecture.
Transition or check target / evaluator/condition and domain: source-page material into topic-level argument under model selection, citation and counter-evidence guidance; see route.
Activation and timing / possible or observed result / implemented force: see route; no inspected automatic external-topic truth checker.
Epistemic authority and scope: candidates with explicit uncertainty and cited lineage; no evidence-consuming acceptance decision demonstrated.
Operational authority / behavioral-authority path: retained wiki may guide query/export/article work through model interpretation across sessions; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.
Claim IDs: [EPI-CLM-synthesis-confidence](#epi-clm-synthesis-confidence).
Mismatch marker / gap/limit: source counts/agreement do not establish independence, encoding fidelity or thesis truth. Five-full-read cap and pre-refresh catalog seam limit available premises.

Route ID: [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: raw/wiki claims, including [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: no content change at persistence itself.
Transition or check target / evaluator/condition and domain: file landing after writer output; not a truth-acceptance check.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: persistence preserves candidates; no additional warrant.
Operational authority / behavioral-authority path: later query/lint/distill/render consumption through files; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/SKILL.md`.
Claim IDs: [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy).
Mismatch marker / gap/limit: retention and source links are not lifecycle integration after acceptance. KEEP blocks preserve human text, not adjudicated truth.

Route ID: [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: external hits, NotebookLM answers/notes and source metadata.
Content/update relation: truth-apt transformation: acquisition/import for selected external content, warrant unknown; no content change for relevance selection itself.
Transition or check target / evaluator/condition and domain: topical relevance and coverage, not factual correctness; researchers and gap analyzer, see route.
Activation and timing / possible or observed result / implemented force: see route; preset rounds, capped admission, optional successor queries.
Epistemic authority and scope: source candidates, not reference answers or verified complete coverage.
Operational authority / behavioral-authority path: model relevance/top-K determines retained sources; metadata gaps guide next searches within the preset horizon, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/researcher.md`.
Claim IDs: none.
Mismatch marker / gap/limit: more relevant or richer metadata is not more truthful; opaque external answers may omit sources.

Route ID: [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: findings JSON.
Content/update relation: truth-apt transformation: non-ampliative reshaping for winner-record retention; non-truth-apt policy/content update: fixed relevance-tag score mapping.
Transition or check target: equal `original_path`, summary length and supplied relevance tag.
Evaluator/condition and domain: fixed `dedup`/`score_from_relevance`, not source truth.
Activation and timing / possible or observed result: invocation with JSON; longest-summary winner and optional scores, see route.
Implemented force: enforcing winner selection and score assignment in helper execution.
Epistemic authority and scope: only the mechanically derived identity/length/mapping relation, conditional on supplied records.
Operational authority / behavioral-authority path: JSON to catalog builder and later score-based selectors, ranking force; see route and [RT-BAP-helper-execution](runtime.md#rt-bap-helper-execution).
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`.
Claim IDs: none.
Mismatch marker / gap/limit: a longer false summary defeats a shorter accurate summary; this is not an accuracy evaluator. Concrete deduction from inspected code: two rows with the same original_path and summaries `true` then `incorrect` select the latter (length nine exceeds four), preserving its other fields; with relevance high it receives 0.8 under --as-results. This uses code as implementation evidence, not a target execution or semantic endorsement.

> if existing is None or len(f.get("summary", "") or "") > len(existing.get("summary", "") or ""):
>     by_path[key] = f
> --- `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`

Route ID: [RT-RTE-index-build](runtime.md#rt-rte-index-build)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: catalog/navigation metadata.
Content/update relation: truth-apt transformation: non-ampliative reshaping for projected source metadata; non-truth-apt policy/content update: seed score 1.0 and ranking.
Transition or check target / evaluator/condition and domain: schema projection, seed precedence and filesystem navigation, see route.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: no fact-checking or source endorsement; timestamps license freshness-of-write only.
Operational authority / behavioral-authority path: canonical YAML and live-tree navigation feed later selection, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`.
Claim IDs: [RT-CLM-index-contract](runtime.md#rt-clm-index-contract).
Mismatch marker / gap/limit: seed priority is origin policy; pointers may be null, preservation requires prior-index input.

Route ID: [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: curated repository specs.
Content/update relation: truth-apt transformation: indeterminate. Source-supported summaries are intended; code-to-prose explanation needs checked interpretation to count as entailed derivation.
Transition or check target / evaluator/condition and domain: model reads bounded repository material and writes topical explanations, see route.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: commit-linked candidate explanations, not demonstrated behavior of the reviewed repository.
Operational authority / behavioral-authority path: architecture hub/module docs into later queries, advisory force, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/github_spec_writer.md`.
Claim IDs: none.
Mismatch marker / gap/limit: conflicting copy destination may break delivery; commit citation does not freeze concurrent cache reads.

Route ID: [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: clone cache/commit metadata.
Content/update relation: truth-apt transformation: acquisition/import for changed repository contents; source warrant unknown.
Transition or check target / evaluator/condition and domain: fetch/reset/reclone subprocess success, see route.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: cached revision identity, not correctness of generated specs.
Operational authority / behavioral-authority path: mutable clone supplied to writers; executable replacement force in current/subsequent ingestion, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/scripts/github_clone.py`.
Claim IDs: none.
Mismatch marker / gap/limit: recovery replaces cache, not withdrawal of accepted research; no concurrency lock established.

Route ID: [EPI-RTE-comparison-write](#epi-rte-comparison-write)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-comparison](#epi-obj-comparison).
Content/update relation: truth-apt transformation: indeterminate; source aggregation and context-relative recommendation can preserve, derive or extend input claims; produced edge unobserved.
Transition or check target / evaluator/condition and domain / activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: candidate comparison with linked supporting pages; not accepted when-to-use knowledge.
Operational authority / behavioral-authority path: recommendation may guide user choice or later wiki consumption, advisory, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/comparison_writer.md`.
Claim IDs: [EPI-CLM-comparison-repair](#epi-clm-comparison-repair).
Mismatch marker / gap/limit: routine dispatch unestablished; guideline quality is not observed result quality.

Route ID: [EPI-RTE-comparison-write](#epi-rte-comparison-write)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: proposed [EPI-OBJ-comparison](#epi-obj-comparison).
Content/update relation: no content change.
Transition or check target: subject existence and backing-page sufficiency for a proposed comparison.
Evaluator/condition and domain: see route; model checks missing pages/shared and exclusive source counts. Scope is available wiki support, not true comparative outcome.
Activation and timing / possible or observed result / implemented force: see route; refusal judgment before write.
Epistemic authority and scope: at most insufficient/available proxy material, no calibrated comparison validity.
Operational authority / behavioral-authority path: judgment supplied to same writer, permissive/blocking instruction for this write; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/comparison_writer.md`.
Claim IDs: none.
Mismatch marker / gap/limit: copied source pages need not be independent or faithful.

Route ID: [EPI-RTE-comparison-write](#epi-rte-comparison-write)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: proposed [EPI-OBJ-comparison](#epi-obj-comparison).
Content/update relation: no content change.
Transition or check target / evaluator/condition and domain: see route; refusal/noop/write decision by writer under availability/thinness/body-identity policy.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: operational permission to write only; not an evidence-consuming acceptance decision certifying the recommendation for a named use.
Operational authority / behavioral-authority path: writer refusal blocks landing under compliance; user/orchestrator may ingest more and retry; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/agents/comparison_writer.md`.
Claim IDs: none.
Mismatch marker / gap/limit: generated verdict is judgment, not an answer oracle; no independent acceptance record.

Route ID: [EPI-RTE-lint-mechanical](#epi-rte-lint-mechanical)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: structural part of [EPI-OBJ-lint-findings](#epi-obj-lint-findings), broken-links result.
Content/update relation: truth-apt transformation: entailed derivation, conditional on parsed body links and filesystem state.
Transition or check target: file existence for recognized wikilink targets.
Evaluator/condition and domain: Python resolver after normalization/external exclusions; see route.
Activation and timing / possible or observed result / implemented force: see route; executable JSON flags.
Epistemic authority and scope: recognized target-file existence only, not heading existence or citation support.
Operational authority / behavioral-authority path: JSON to orchestrator/user, advisory for current repair; see route. No automatic claim rejection.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`; `plugins/ai-research-os/skills/research-lint/scripts/_lintlib.py`.
Claim IDs: none.
Mismatch marker / gap/limit: resolves supplied resolver-inspection limit; no supersession needed. Anchor stripping prevents heading-validity conclusions.

Route ID: [EPI-RTE-lint-mechanical](#epi-rte-lint-mechanical)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: structural part of [EPI-OBJ-lint-findings](#epi-obj-lint-findings), orphan result.
Content/update relation: truth-apt transformation: entailed derivation, conditional on catalog pointers and parsed body targets.
Transition or check target: whether any uri_full/uri_highlights/uri_source_page pointer is wikilinked by a wiki body.
Evaluator/condition and domain: fixed set-membership predicate; see route.
Activation and timing / possible or observed result / implemented force: see route; executable JSON flags sorted by relevance score.
Epistemic authority and scope: encoded pointer-reference absence, not unused source or semantic integration.
Operational authority / behavioral-authority path: current report/user deletion-or-citation choice, advisory; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/scripts/lint_orphans.py`.
Claim IDs: none.
Mismatch marker / gap/limit: pointerless entries skipped; frontmatter-only/ordinary Markdown citations do not enter target set.

Route ID: [EPI-RTE-lint-mechanical](#epi-rte-lint-mechanical)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: structural part of [EPI-OBJ-lint-findings](#epi-obj-lint-findings), missing-hubs result.
Content/update relation: truth-apt transformation: entailed derivation, conditional on parsed source-page links and configured threshold.
Transition or check target: absent entity/concept file with enough distinct referring source pages.
Evaluator/condition and domain: fixed distinct-page count plus file resolver; default threshold three, see route.
Activation and timing / possible or observed result / implemented force: see route; executable JSON flags.
Epistemic authority and scope: encoded link frequency and file absence, not substantive or independent evidence count.
Operational authority / behavioral-authority path: current report/user ingest-or-accept-absence choice, advisory; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`.
Claim IDs: none.
Mismatch marker / gap/limit: source writer forbids links to nonexistent new hubs, so compliant suggestions can remain invisible to this link-only predicate.

Route ID: [EPI-RTE-lint-mechanical](#epi-rte-lint-mechanical)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: structural part of [EPI-OBJ-lint-findings](#epi-obj-lint-findings), missing-comparisons result.
Content/update relation: truth-apt transformation: entailed derivation, conditional on parsed hub mutual references and expected filename absence.
Transition or check target: mutual hub links and absent alphabetized comparison path.
Evaluator/condition and domain: fixed pair/set/resolver rule; see route.
Activation and timing / possible or observed result / implemented force: see route; executable JSON flags.
Epistemic authority and scope: comparison-file candidate only, not supported rivalry or recommendation.
Operational authority / behavioral-authority path: current report/user comparison request, advisory; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_comparisons.py`.
Claim IDs: [EPI-CLM-comparison-repair](#epi-clm-comparison-repair).
Mismatch marker / gap/limit: suggested repair format has no matching render dispatch; existing comparison file need not contain valid comparison.

Route ID: [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: semantic portion of [EPI-OBJ-lint-findings](#epi-obj-lint-findings).
Content/update relation: truth-apt transformation: indeterminate for model interpretations of opposition/supersession; no actual claim-pair/result to classify.
Transition or check target: opposing source claims already represented in qualifying entity/concept tensions.
Evaluator/condition and domain: wiki-only model judge; see route. Opposition detection does not decide which source is true.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: candidate criticism, not automatic correction or accepted truth.
Operational authority / behavioral-authority path: stale flags to user for judgment; contradiction judgments to append route; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`.
Claim IDs: none.
Mismatch marker / gap/limit: scoped to qualifying entity/concept pages, eight full reads; source-level contradiction dispatch wording is broader than judge scope.

Route ID: [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: stale flags in [EPI-OBJ-lint-findings](#epi-obj-lint-findings).
Content/update relation: truth-apt transformation: indeterminate for model judgments of newer contradiction/supersession; no actual input/result pair supplied.
Transition or check target: unqualified older claims on entity/concept pages with at least three backing sources and a broad publication-date spread.
Evaluator/condition and domain: wiki-only model judge, using dates and newer contradictory/superseding content, not age alone; see route.
Activation and timing / possible or observed result / implemented force: see route; no source-page correction requested.
Epistemic authority and scope: candidate stale-claim flag, not a decision that newer source is true.
Operational authority / behavioral-authority path: current report to user, advisory; user decides revision, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`.
Claim IDs: none.
Mismatch marker / gap/limit: publication chronology is not endorsement; no automated withdrawal or changed reliance established.

Route ID: [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: contradictions/questions in [EPI-OBJ-lint-findings](#epi-obj-lint-findings).
Content/update relation: no content change at append; question generation is non-truth-apt policy/content update: candidate search prompts.
Transition or check target / evaluator/condition and domain: model duplicate decision and additive admission; see route.
Activation and timing / possible or observed result / implemented force: see route; additive writes requested without individual user approval.
Epistemic authority and scope: retained criticism, not acceptance or withdrawal of the challenged claim.
Operational authority / behavioral-authority path: next synthesis writer/query can read rolling files; current report advises user actions, see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`.
Claim IDs: none.
Mismatch marker / gap/limit: old entries remain even when obsolete; append-only policy supplies no cleanup of withdrawn criticism. Scratch deletion removes diagnostics, not wiki claims.

Route ID: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: catalog/source/wiki content, including [EPI-OBJ-synthesis](#epi-obj-synthesis).
Content/update relation: no content change for retrieval; truth-apt transformation: indeterminate for synthesized answer.
Transition or check target / evaluator/condition and domain: progressive relevance/depth selection and answer generation; see route.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: attributed answer candidate; citations do not verify inference or represent complete evidence.
Operational authority / behavioral-authority path: user or another skill receives selected layers and answer metadata, advisory for current decision; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/SKILL.md`.
Claim IDs: [RT-CLM-query-safety](runtime.md#rt-clm-query-safety).
Mismatch marker / gap/limit: summary-only reads may inherit losses; source-layer drilldown is a counterexample to an absolute no-raw-read claim.

Route ID: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: answer-derived content/question pointer.
Content/update relation: no content change at save decision.
Transition or check target / evaluator/condition and domain: explicit bookmark or at least two cited sources triggers save; see route.
Activation and timing / possible or observed result / implemented force: see route; fallback blocks all writes.
Epistemic authority and scope: operational admission for recall, not demonstrated acceptance against a correctness criterion.
Operational authority / behavioral-authority path: model lands content/pointer for later wiki consumption under conflicting permissions; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research/SKILL.md`.
Claim IDs: [RT-CLM-query-safety](runtime.md#rt-clm-query-safety).
Mismatch marker / gap/limit: Q.5 landing conflicts with authoritative question-page-only map. No licensed conclusion that saved synthesis was epistemically accepted or lifecycle-integrated.

Route ID: [RT-RTE-distill-export](runtime.md#rt-rte-distill-export)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: corpus-relative research appendix.
Content/update relation: truth-apt transformation: indeterminate; intended faithful selection/condensation and quote retention require paired evidence to verify non-ampliative reshaping.
Transition or check target / evaluator/condition and domain: match source use in supplied writing corpus, not source truth; see route.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: candidate matched appendix; no reference match set or observed exactness.
Operational authority / behavioral-authority path: future writing-agent context by exported file, advisory; see route.
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-distill/SKILL.md`.
Claim IDs: none.
Mismatch marker / gap/limit: seed scores do not force inclusion; matching an idea does not prove historical source use.

Route ID: [RT-RTE-render-output](runtime.md#rt-rte-render-output)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: rendered prose/graph and hard-coded chart data/program.
Content/update relation: truth-apt transformation: indeterminate for model render semantics; non-truth-apt policy/content update: generated chart program admitted for execution.
Transition or check target / evaluator/condition and domain: format writer extracts/reframes selected wiki content; script execution success targets executable/renderability, not numerical truth; see route.
Activation and timing / possible or observed result / implemented force: see route.
Epistemic authority and scope: no new source warrant; chart reproducibility concerns embedded snapshot, not valid measurement or mechanism.
Operational authority / behavioral-authority path: user artifacts/navigation, plus Python execution under host permissions; see route and [RT-BAP-helper-execution](runtime.md#rt-bap-helper-execution).
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-render/SKILL.md`.
Claim IDs: none.
Mismatch marker / gap/limit: prompt/path noop ignores changed source bodies; needs_guidance retries scope, execution failure retains script, neither verifies claims.

Route ID: [RT-RTE-render-output](runtime.md#rt-rte-render-output)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-chart-program](#epi-obj-chart-program).
Content/update relation: no content change at execution admission.
Transition or check target: writer-generated script admitted to Python execution, then success/failure handled as render completion.
Evaluator/condition and domain: orchestrator requests uv execution; process success targets executable artifact/render production, not source truth. See route.
Activation and timing / possible or observed result / implemented force: see route; requested executable authority under host permissions, actual run unobserved.
Epistemic authority and scope: none for the selected numbers or causal chart interpretation from program success alone.
Operational authority / behavioral-authority path: generated file to Python/matplotlib, executable force for current render and possible reruns; see route and [RT-BAP-helper-execution](runtime.md#rt-bap-helper-execution).
Evidence source ID and local anchor: SRC-1 `plugins/ai-research-os/skills/research-render/SKILL.md`.
Claim IDs: none.
Mismatch marker / gap/limit: no separate program-content approval; failure retains script for user recovery, not claim rejection.

No lifecycle-integration route after evidenced acceptance was established in these inspected routes. That is a bounded distinction, not a declaration of system-complete absence. Citation-linked retention and operational consumption are present as doctrine; neither substitutes for acceptance.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-source-attribution](#epi-clm-source-attribution) | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/source_writer.md`, doctrine/design | Attribution and judgment markers requested | [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), doctrine for model content | None supplied | No fidelity experiment | Inspectable lineage policy | Wikilink existence does not establish support or source truth |
| [EPI-CLM-synthesis-confidence](#epi-clm-synthesis-confidence) | see record | SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`, doctrine/design | Counter-evidence, assumptions and confidence heuristics | [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), doctrine | None supplied | No independent outcome/precision calibration | Candidate thesis and criticism protocol | Counts and majority do not establish independence or truth |
| [EPI-CLM-comparison-repair](#epi-clm-comparison-repair) | see record | SRC-1 `plugins/ai-research-os/skills/research-lint/SKILL.md`, doctrine/design | Lint recommends comparison repair command | [EPI-RTE-comparison-write](#epi-rte-comparison-write), doctrine; [RT-RTE-render-output](runtime.md#rt-rte-render-output), no matching format | None supplied | No observed fallback | Comparison writer available, repair dispatch not established | Render only supports marp/chart/canvas/brief |
| [RT-CLM-query-safety](runtime.md#rt-clm-query-safety) | see record | SRC-1 `plugins/ai-research-os/skills/research/SKILL.md`, doctrine/design | see record | [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | None supplied | Host compliance unobserved | Policy bounds normal/fallback writes | Save-content conflict, not an invariant |
| [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy) | see record | SRC-1 `plugins/ai-research-os/skills/research/CONVENTIONS.md`, doctrine/design | see record | [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) | None supplied | No immutability deployment evidence | Post-ingest preservation request | Asset rewrite/overwrite alternates retained; not byte-preservation guarantee |
| [RT-CLM-index-contract](runtime.md#rt-clm-index-contract) | see record | SRC-1 `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, implementation | see record | [RT-RTE-index-build](runtime.md#rt-rte-index-build) | None supplied | No quality comparison | Narrow fixed projection/priority rules | Not source endorsement, complete dedup or pointer verification |

## Bounded conclusion

The plugin acquires external content and asks models to turn it into source pages, topic pages, theses, answers and exports. Imported content is acquired rather than produced knowledge; its warrant remains unknown. Source-page citations and explicit synthesis markers make intended lineage inspectable but do not check semantic fidelity. Summary-only downstream writers inherit omissions; query drilldown can revisit deeper content. GitHub pinning licenses source identity, not the explanation generated from that source. See [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest) and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).

The deterministic deductions here are narrow. Dedup is length/identity selection and tag-to-score mapping; catalog construction projects metadata and assigns seed priority. Mechanical lint derives claims about parsed links, pointers, thresholds and existing files. Those predicates carry implementation warrant in their encoded domain, not external research truth. Concrete counterexamples below show why a clean lint result cannot license intact citation support. See [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery), [RT-RTE-index-build](runtime.md#rt-rte-index-build) and [EPI-RTE-lint-mechanical](#epi-rte-lint-mechanical).

Models are instructed to formulate potentially substantive thesis/recommendation candidates and criticize source opposition. No supplied run individuates a produced ampliative proposition with its premises, check result and evidence-consuming acceptance decision. Failure to prove entailment is not a conjecture classification. Confidence and source-count thresholds are writer/admission heuristics, not demonstrated acceptance criteria for external-topic truth. Comparison refusal is a support-availability gate for a write; query bookmarks/two-source counts admit recall artifacts. Neither is shown accepting a proposition for a named intended use against a checked criterion. Citation connection before such acceptance is not lifecycle integration. See [EPI-RTE-comparison-write](#epi-rte-comparison-write), [EPI-CLM-synthesis-confidence](#epi-clm-synthesis-confidence) and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).

Lint criticism can persist and later reach synthesis/query consumers. Its force is additive/advisory; stale flags require user resolution, structural flags do not delete claims, and obsolete contradiction entries remain. A retained critic report does not prove changed reliance or revision. The summary writer's counter-evidence guidance affords weakening/splitting a thesis, but no exercised result closes that loop here. See [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance) and [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest).

Separate behavioral routes matter without truth acceptance: coverage gaps propose next discovery queries; score mappings rank candidates; chart scripts receive executable authority; noop gates can preserve old render snapshots. Retained research reaches later model context through files, while helpers act through fixed symbolic rules. Neither delivery nor successful execution demonstrates benefit. Provider parameters remain opaque under [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-CMP-notebooklm-model](runtime.md#rt-cmp-notebooklm-model); no weight-change, exact-version or endpoint-fixity conclusion follows.

Theory formulation, requested consumption, criticism and iteration retain the separate afforded conclusions in [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) and [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance). Improved future capacity, own-method reflection, a fully autonomous exercised theory cycle and exercised self-improvement are not established by those content routes. These independent evidence limits do not negate implemented structural checking or the afforded external-topic thesis process. Missing run/causal evidence, unread extraction/format details and the missing comparison dispatch prevent a single system-wide epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-source-pages
Label: Source pages

Natural-language `wiki/sources/<slug>.md` on the research-directory filesystem holds model summaries, key claims, quotes and marked synthesis. Metadata frontmatter has symbolic parsing uses; the content assessed here is prose interpreted by downstream model writers/query readers. Distinct from static [RT-OBJ-skill-instructions](runtime.md#rt-obj-skill-instructions) and executable [RT-OBJ-python-helpers](runtime.md#rt-obj-python-helpers). It is retained output carried by [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), not an alias for that route. No supplied operative-object counterpart declares accumulated source-page prose. SRC-1 `plugins/ai-research-os/skills/research/agents/source_writer.md`.

> This page is what every downstream wiki page (entities, concepts, comparisons, overview, synthesis) reads from.
> --- `plugins/ai-research-os/skills/research/agents/source_writer.md`

> If the file is very long (>2000 lines), read in chunks — start with the first 2000 lines and only read further if your draft is missing critical content from later sections.
> --- `plugins/ai-research-os/skills/research/agents/source_writer.md`

#### EPI-OBJ-synthesis
Label: Synthesis page

Natural-language thesis, assumptions, supporting moves, counter-evidence and revision conditions in `wiki/synthesis.md`, with confidence metadata on disk. This is generated research content, not static plugin instructions or numerical model state. Its closest supplied route is [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), which carries production/retention; no supplied object declares this retained thesis. The summary writer's five-full-read cap and requested no-raw reads limit premises without proving any particular thesis false. SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

> **synthesis** — "What does it all mean?" The thesis. Argumentative, opinionated, ≤ 1000 words. This is the page that compounds into article drafts.
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

> <What the wiki contains that pushes against the thesis. Be honest — if there's strong contradiction, the thesis should weaken or split. Wikilink contradictions.md.>
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

#### EPI-OBJ-comparison
Label: Comparison page

Natural-language comparison tables and when-to-use recommendations in `wiki/comparisons/<slug>.md` on disk; frontmatter points at subject/backing pages. Human/model interpretation gives recommendations force. Distinct from entity/concept and thesis pages because the writer has subject-existence and thinness refusal rules. Closest supplied containers are [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); neither declares a comparison object or this dedicated writer route. SRC-1 `plugins/ai-research-os/skills/research/agents/comparison_writer.md`.

> A comparison surfaces alignment, contrast, and when-to-use guidance between two entities OR two concepts (or one of each). It is its own synthesis artifact, distinct from the entity/concept pages it sits across.
> --- `plugins/ai-research-os/skills/research/agents/comparison_writer.md`

#### EPI-OBJ-lint-findings
Label: Lint findings

Structural part: symbolic JSON diagnostics on stdout/scratch, fixed-key consumers for counts and sorted flags. Semantic part: natural-language contradiction/stale-claim judgments and questions in stdout reports or rolling Markdown files, consumed by user/model interpretation. These parts have different checking domains and retention, kept separate in the ledger. They are outputs of [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance), not duplicate declarations of that route or its static tooling. No accumulated-diagnostic object counterpart occurs in the supplied runtime. SRC-1 `plugins/ai-research-os/skills/research-lint/SKILL.md`; `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`.

> The orchestrator aggregates flags into the final report.
> --- `plugins/ai-research-os/skills/research-lint/SKILL.md`

> Be conservative — these are flags for the user, not auto-fixes. False positives waste user attention. Prefer to miss borderline cases.
> --- `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`

#### EPI-OBJ-raw
Label: Raw source layer

Natural-language source copies/captions/highlights in `raw/`, with binary source/image assets on the filesystem. Model/human interpretation consumes text and images; paths are symbolic pointers rather than truth checks. Imported provenance and rewriting limits are those of [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) and [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy), whose retained passages support the finding. Distinct from source-page/model-generated prose and from static instructions; no supplied object counterpart. SRC-1 `plugins/ai-research-os/skills/research/CONVENTIONS.md`.

#### EPI-OBJ-index
Label: Research index

Canonical `index.yaml` on disk contains symbolic fields/pointers and natural-language summaries; Python projects fields, models interpret summaries for relevance. `index.md` is a separately regenerated human/model navigation view using both YAML and the live wiki tree. These operative parts have distinct freshness inputs and no factual evaluator. See [RT-RTE-index-build](runtime.md#rt-rte-index-build) and its passages for production/consumption. Different referent from shipped helper source or instructions; no supplied accumulated-catalog object. SRC-1 `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; `plugins/ai-research-os/skills/research/scripts/build_index_md.py`.

#### EPI-OBJ-topic-pages
Label: Entity concept and overview pages

Natural-language entity/concept definitions, grounded claims, tensions and questions in filesystem wiki pages; model producers and later query/writer consumers. Overview prose instead groups/navigates available topics. These are distinct operative parts: overview does not supply the argumentative thesis, and entity/concept writers aggregate assigned source pages while overview has discovery/read caps. See [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) and its writer passages. Distinct from source pages and thesis; no supplied object counterpart. SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`; `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

#### EPI-OBJ-repo-specs
Label: Repository specifications

Natural-language curated architecture/module Markdown with code permalinks, intended filesystem substrate `wiki/repos/`. Models produce explanations and later interpret them via the architecture hub; commit/path metadata is symbolic lineage. Closest [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest) carries the production/pointer conflict and evidence passages, not an object declaration. Distinct from retained raw copies and source-page summaries; no supplied object counterpart. SRC-1 `plugins/ai-research-os/skills/research/agents/github_spec_writer.md`.

#### EPI-OBJ-query-content
Label: Query answer and saved content

Natural-language immediate answers and intended knowledge-doc content; question Markdown is separately a slim pointer with question/motivation/link rather than answer body. Filesystem landing is subject to the unresolved permission conflict. Models select/generate answers; user or skill caller interprets them; later consumers may follow saved pointers. See [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) for evidence and distinct save rules. This object spans new answer material and modifications of existing topic/repo/comparison objects, so it is not a part of exactly one supplied object and not a duplicate route. No supplied answer object counterpart. SRC-1 `plugins/ai-research-os/skills/research/SKILL.md`.

#### EPI-OBJ-research-appendix
Label: Research appendix

Natural-language matched claims/quote fragments and symbolic metadata/pointers in exported `research.md` beside the supplied writing corpus. The matching model selects material for a later writer, not for universal source ranking. See [RT-RTE-distill-export](runtime.md#rt-rte-distill-export) and its retained selection passage. Distinct substrate/location/consumer from canonical catalog and topic wiki; no supplied object counterpart. SRC-1 `plugins/ai-research-os/skills/research-distill/SKILL.md`.

#### EPI-OBJ-render-content
Label: Rendered wiki content

Natural-language Marp/brief prose, spatial Canvas relationships in symbolic JSON consumed by a viewer and human/model interpretation, and image chart data presentation under `wiki/renders/`. These parts share selected wiki provenance but not encoding or viewer rules. Writer-body uncertainty remains for Marp/Canvas/brief; no invented semantic-preservation classification. See [RT-RTE-render-output](runtime.md#rt-rte-render-output) for chart snapshot and requested persistence passages. Distinct from its companion executable program and from source wiki; no supplied render object counterpart. SRC-1 `plugins/ai-research-os/skills/research-render/SKILL.md`.

#### EPI-OBJ-chart-program
Label: Chart program

Symbolic generated Python with hard-coded snapshot data on disk next to the chart PNG. Python executes instructions; embedded quantities and labels separately express claims about selected wiki data. Its effect boundary is host permissions, not the epistemic authority of those claims. See [RT-RTE-render-output](runtime.md#rt-rte-render-output) and its quoted execution/snapshot instructions. Unlike [RT-OBJ-python-helpers](runtime.md#rt-obj-python-helpers), it is generated retained output, not fixed shipped helper source. No supplied generated-program object counterpart. SRC-1 `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`.

### Routes

#### EPI-RTE-lint-mechanical
Label: Mechanical lint predicates
Part of: [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance)

This is the executable structural-check part of the supplied maintenance container, not a supersession of its model judges or driver. Endpoints: research-directory Markdown/YAML/files → shared parser and four Python predicates → stdout JSON → prompted report/user repair choices. Python owns evaluation; host/orchestrator owns invocation/reporting. Direct source inspection adds the previously uninspected shared resolver and three other scripts. SRC-1 `plugins/ai-research-os/skills/research-lint/scripts/_lintlib.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_orphans.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`; `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_comparisons.py`; `plugins/ai-research-os/skills/research-lint/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Each script prints JSON with counts and diagnostic rows; it does not edit claims.
- Later read-back: Scratch diagnostic files may remain for user review until deleted; no automatic later knowledge-reader injection is specified. Log counts can persist but no content-dependent successor is established from those counts alone.
- Delegated visibility: inapplicable — helpers are Python subprocesses reading filesystem input, not dispatched model agents.
- Selection predicate: Broken-links checks parsed body wikilinks after excluding external targets; orphans checks catalog uri_full/uri_highlights/uri_source_page against all body targets, skipping rows without pointers; missing-hubs counts distinct source-page links at default threshold three; missing-comparisons finds mutual links between hub paths and absent alphabetized comparison filename.
- Invalidation or expiry: Findings are regenerated per invocation; driver permits scratch JSON deletion after review. They do not automatically invalidate wiki claims.
- Activation or effect: Executable JSON generation is wired; driver requests aggregate report and user choices, not automatic structural repair. Later human action is unobserved.
- Evidence limits: Parsing excludes frontmatter links, labels and anchors; only recognized wikilinks count. Normal Markdown citations are outside predicates. No execution trace supplied.

The user requests audit/scope; code proposes structural flags, the orchestrator reports them, and the user decides repairs/deletion or accepts absence. No expected-answer oracle is supplied. Operating mode is open-request structural audit, not an experiment. Threshold and filesystem predicates determine diagnostic truth only within their encoding. There is no knowledge-admission change, rollback or research rejection in these scripts.

Concrete implementation deductions, not executed fixtures: `[[wiki/concepts/foo#missing]]` yields target `wiki/concepts/foo`; if that file exists, the missing heading is not a broken-link finding. A source row lacking all three pointers is skipped by the orphan checker, so no orphan flag does not prove source integration. Three source pages linking a missing hub satisfy the default hub threshold even if their claims merely repeat one source. Hub A linking B and B linking A with no expected comparison file produces a candidate; the predicate does not establish useful or evidence-supported rivalry. These cases falsify broad interpretations of a clean structural audit without falsifying its narrow predicates. A second coverage limit follows from the source-writer rule below: new entity/concept suggestions returned only in stdout cannot count toward a checker that sees only body wikilinks.

> Do NOT create new wikilinks for entities/concepts that don't have pages yet — those go in your stdout JSON as suggestions, not as broken links in the body.
> --- `plugins/ai-research-os/skills/research/agents/source_writer.md`

> target = match.group(1).strip()
> out.append(target)
> --- `plugins/ai-research-os/skills/research-lint/scripts/_lintlib.py`

> if not candidates:
>     continue  # No file => can't be orphan in the wiki sense; skip.
> --- `plugins/ai-research-os/skills/research-lint/scripts/lint_orphans.py`

> if len(source_pages) < args.threshold:
>     continue
> --- `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`

> if a_key in refs.get(b_key, set()):
> --- `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_comparisons.py`

#### EPI-RTE-comparison-write
Label: Comparison support gate and write

Dedicated writer protocol: two subject pages → shared/exclusive source-page selection → model contrast/recommendation draft → refuse/noop/write → JSON verdict. The host-dispatched model owns selection, judgment and physical write requests. This differs from the supplied [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) container's generic topic propagation and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)'s answer landing: the dedicated agent has distinct required inputs and refusal rules. It is not declared part of one container because routine dispatch is unresolved. SRC-1 `plugins/ai-research-os/skills/research/agents/comparison_writer.md`; `plugins/ai-research-os/skills/research-render/SKILL.md`; `plugins/ai-research-os/skills/research-lint/SKILL.md`.

- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Requested JSON contains created/updated/noop or refusal; generated verdict labels favors_a, favors_b, context_dependent or orthogonal.
- Later read-back: Comparison page is eligible for later wiki/query/render consumption; actual activation is unobserved.
- Delegated visibility: Two subject pages, shared source pages in full, exclusive source-page distinctive/connections sections; raw files are forbidden.
- Selection predicate: Subject existence; shared source sets; refuse when shared_sources is empty and exclusive total is below four. Citation and no-fabrication guidance bound content, not proven fidelity.
- Invalidation or expiry: Identical body excluding last_updated requests noop; otherwise rewrite with created/KEEP preservation. No TTL or automatic withdrawal of false comparison is specified.
- Activation or effect: Writer protocol affords retained comparison and advisory recommendation. Dedicated dispatch from current inspected drivers is not established.
- Evidence limits: No produced comparison, exercised refusal or expected reference outcome supplied. Support count is a proxy, not truth validation.

Proposer and decider are the writer model; user framing and KEEP blocks shape content but are not routine per-proposition approval. No answer oracle exists in this protocol. Mode is open comparative research. Missing subject files or thin material request rejection; more ingest permits retry, not a transaction rollback. Guidance requests mechanism/tradeoff/citation context and preserves existing human blocks; recommendation prose and JSON verdict persist/return. Local recommendations do not by themselves establish a whole formulated theory, so no new independent theory-cycle claim is made; any consumed thesis remains under the supplied synthesis theory account.

> If either page does not exist, **abort**: print `{"action": "refused", "reason": "subject_b.page_path does not exist"}` and exit. Do not write a comparison page.
> --- `plugins/ai-research-os/skills/research/agents/comparison_writer.md`

> **Refuse rather than fabricate.** If `shared_sources` is empty AND `a_only_sources + b_only_sources < 4`, refuse: the wiki is too thin for this comparison. The orchestrator will retry after more sources are ingested.
> --- `plugins/ai-research-os/skills/research/agents/comparison_writer.md`

### Claims

#### EPI-CLM-source-attribution
Label: Source attribution and marked judgment

Claim: source-derived assertions are linked to raw, while model synthesis is marked for distinguishability. This is an authorship/lineage policy, not an implemented truth guarantee. Closest [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy) governs preserved copies rather than claim attribution; [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) describes writer production without declaring this claim. SRC-1 `plugins/ai-research-os/skills/research/agents/source_writer.md`, doctrine/design.

> **No floating claims.** Every claim is either backed by a wikilink to the raw file or marked `> Synthesis:`.
> --- `plugins/ai-research-os/skills/research/agents/source_writer.md`

#### EPI-CLM-synthesis-confidence
Label: Thesis confidence guidance

Claim: current research supports a thesis whose declared confidence tracks source-page counts and agreement/contradiction. This differs from catalog priority in [RT-CLM-index-contract](runtime.md#rt-clm-index-contract); the closest production container [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest) does not declare this confidence claim. No independent calibration or acceptance decision is supplied. SRC-1 `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`, doctrine/design.

> `high` — ≥ 5 source pages, multiple aligned, low/no contradictions
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

> `medium` — 3–4 source pages OR contradictions exist but a clear majority view
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

> `low` — < 3 source pages OR strong contradictions and no majority
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

These criteria do not check whether copied/derived sources are independent, true or correctly encoded. That is a limitation of the stated target/domain, not a measured failure rate.

#### EPI-CLM-comparison-repair
Label: Missing comparison repair command

Claim: lint offers `/research-render comparison` to resolve missing comparison flags. This overlaps [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance)'s repair advice and [RT-RTE-render-output](runtime.md#rt-rte-render-output)'s dispatch, but neither declares this mismatch. Direct inspection shows the render format dispatch has only four formats and no comparison agent row. Thus the literal command is not supported as a matching shipped format; unobserved model reinterpretation remains possible. SRC-1 `plugins/ai-research-os/skills/research-lint/SKILL.md`; `plugins/ai-research-os/skills/research-render/SKILL.md`, doctrine/design.

> For missing comparisons: run /research-render comparison <a> <b>
> --- `plugins/ai-research-os/skills/research-lint/SKILL.md`

> **format(s)** — one or more of `marp` | `chart` | `canvas` | `brief`. Resolve as follows:
> --- `plugins/ai-research-os/skills/research-render/SKILL.md`

### Behavioral-authority paths

none declared in this member; the supplied [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) and [RT-BAP-helper-execution](runtime.md#rt-bap-helper-execution) cover the two channels. The ledger separates their actual content consumers, force and horizons rather than asserting delivery establishes compliance.
