---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "llm-wiki-newsroom's source attribution, editorial checks, publication reliance and instruction-change warrant."
run-id: AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01
reviewed-boundary: "8e209cab483da544852d7213f0e25291d06d8a88"
---

# llm-wiki-newsroom epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on the wiki's claims, rather than merely making them available. The functional boundary and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). All source anchors below are SRC-1 at the frozen revision. External host/model execution, QMD internals, private originals and private operational history are not inspected. Those gaps prevent claims of faithful extraction across the corpus, provider reliability or exercised end-to-end epistemic control.

The supplied runtime is a provisional route account. Direct reads add the citation check implementation, synthesis join surfacing and advisory exit behavior, contradiction classification/strength/re-adjudication, trail/timeline procedures, and a bounded sample of the judge experiment. They qualify rather than supersede runtime: specifically, a successful lint exit need not mean all required synthesis criteria passed, and a contradiction labeled superseded is not automatically withdrawn. Relevant claims are [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust), [EPI-CLM-evolving-guidelines](#epi-clm-evolving-guidelines), and [RT-CLM-human-supervision](runtime.md#rt-clm-human-supervision).

| Entry point or operation | Source path, SRC-1 | Coverage and records; limit |
|---|---|---|
| Natural language, nine slash commands | `.claude/commands/README.md` | Direct command roster read; runtime role dispatch see [RT-RTE-role-delegation](runtime.md#rt-rte-role-delegation). Host may expose non-command Markdown too; roster is not a closed tool registry. |
| Ingest, grades, links, cascade | `.claude/layers/source.md`, `.claude/skills/scholarly-citation/checks.py` | Direct guide and checker read; command flow supplied by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); [EPI-RTE-citation-check](#epi-rte-citation-check). Fetch/extraction implementations not independently inspected; no source-complete import-fidelity finding. |
| Query, save, no-QMD fallback | `.claude/commands/wiki-query.md`, `tools/query.py` | Direct procedure and CLI dispatch; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). No external search internals assessed. |
| Synthesis authoring/lint/Desk | `.claude/layers/synthesis.md`, `tools/_lint/synthesis.py`, `.claude/agents/desk.md` | Direct guide, evaluation/exit branches and full Desk read; correction reinspection distinguishes targeted excerpt output from corpus summaries; [EPI-RTE-join-surface](#epi-rte-join-surface), [EPI-RTE-desk-check](#epi-rte-desk-check), [EPI-RTE-editorial-disposition](#epi-rte-editorial-disposition). |
| Graph/build/lint and hooks | `tools/_build/graph.py`, `.claude/hooks/dispatch.py`, `.claude/hooks/lint_chain_guard.py` | Direct grade/relation parsers; remaining dispatch, hooks and alternate shell/CLI paths supplied by [RT-RTE-build-lint](runtime.md#rt-rte-build-lint), [RT-BAP-hook-feedback](runtime.md#rt-bap-hook-feedback). Not an independent audit of every lint branch. |
| Contradiction classification and re-adjudication | `tools/_build/contradictions.py`, `tools/_lint/contradiction.py` | Direct collection/classification/strength/write and reground-status function; [EPI-RTE-contradiction-derive](#epi-rte-contradiction-derive), [EPI-RTE-reground-surface](#epi-rte-reground-surface). Theme mapping/removal branches not fully inspected; no global withdrawal claim. |
| Trail create/follow/list, timeline | `.claude/commands/wiki-trail.md`, `.claude/commands/wiki-timeline.md` | Direct procedure reads; [EPI-RTE-narrative-authoring](#epi-rte-narrative-authoring). Their detailed layer/checker implementations remain uninspected; no chronology-completeness guarantee. |
| Export/browser/email | `tools/export.py`, `graph/graph.html`, `tools/send_briefing.py` | Export supplied by [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export); browser supplied by boundary coverage. Email not independently assessed: prevents a complete account of downstream factual delivery/omission. |
| News/discovery/ranking | `.claude/commands/wiki-news.md`, `tools/discover.py` | News stage separation supplied by runtime account; discovery implementation uninspected. Prevents complete ranking/selection assessment; recommendations are not established fact acceptance. |
| Guideline changes and alternate hosts | `.claude/agents/editor-in-chief.md`, `AGENTS.md`, `GEMINI.md` | Supplied [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change) and runtime control comparisons. No independent all-branch reinspection of measurement or feedback miners. |
| Judge experiment | `docs/experiments/judge-model-2026-09/README.md`, `docs/experiments/judge-model-2026-09/preregistration.md` | Direct plan, labeler prompt, ten A2 label rows and three score rows; [EPI-RTE-judge-measurement](#epi-rte-judge-measurement). No recomputation, complete ledger inspection or independent raw verification. |

No target was executed. Missing original documents prevent checking whether imported assertions are true or accurately paraphrased; model prompts establish requested checks, not performed acceptance. Available but uninspected routes above prevent a system-complete negative about acceptance, withdrawal or learning.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-claims](#epi-obj-source-claims) | see record | see record | SRC-1 `.claude/layers/source.md` | Import fidelity and truth not established by a grade. |
| [EPI-OBJ-claim-markers](#epi-obj-claim-markers) | see record | see record | SRC-1 `.claude/skills/scholarly-citation/checks.py` | Grammar and relation category do not verify the proposition. |
| [EPI-OBJ-narrative-pages](#epi-obj-narrative-pages) | see record | see record | SRC-1 `.claude/layers/synthesis.md` | No instance-to-production/check/acceptance provenance traced. |
| [EPI-OBJ-contradiction-db](#epi-obj-contradiction-db) | see record | see record | SRC-1 `tools/_build/contradictions.py` | Numeric metadata is a heuristic, not probability of truth. |
| [EPI-OBJ-experiment-ledger](#epi-obj-experiment-ledger) | see record | see record | SRC-1 `docs/experiments/judge-model-2026-09/scores.jsonl` | Opaque model tag, unpublished question/scorer, unavailable raw originals. |
| [RT-CMP-opus](runtime.md#rt-cmp-opus), [RT-CMP-fable](runtime.md#rt-cmp-fable), [RT-CMP-sonnet](runtime.md#rt-cmp-sonnet), [RT-CMP-session-model](runtime.md#rt-cmp-session-model), [RT-CMP-qmd](runtime.md#rt-cmp-qmd) | not determinable inside distributed parameters | see records | SRC-1 `.claude/agents/README.md`, `tools/_query/qmd.py` | Weights inaccessible; family aliases do not pin versions. No parameter-learning or internal fact-check conclusion follows. |

## Authority-route ledger

The following compact entries are this member's route-level epistemic overlay. Other owned fields are see the linked declarations. No observed activation is inferred from code or doctrine.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-source-claims](#epi-obj-source-claims)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: external document to attributed wiki claims; summarization can change nuance, so source warrant is unknown, not inherited automatically.
Evaluator/condition and domain: see route; source guide defines grade as source class, not truth certification.
Activation and timing: see route.
Possible or observed result: candidate claims and source/hub writes, not observed accepted propositions.
Implemented force: interpreted authoring protocol.
Epistemic authority and scope: attribution to a speaking source; no independent corroboration licensed.
Operational authority: written pages become available before final review.
Behavioral-authority path: later query and authors consume Markdown as evidence; permissive, across invocations.
Evidence: SRC-1 `.claude/layers/source.md`; see route passages.
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: retention precedes disposition.
Gap/limit: raw originals and production traces unavailable.

Route ID: [EPI-RTE-citation-check](#epi-rte-citation-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-claim-markers](#epi-obj-claim-markers)
Content/update relation: no content change
Transition or check target: textual grade/claimant/citation syntax, not truth of content or correctness of grade.
Evaluator/condition and domain: deterministic regex and injected page/section context; see record.
Activation and timing: author self-check or Copy Editor lint.
Possible or observed result: metrics and missing-line samples, not observed runs.
Implemented force: diagnostic, with selected required checks feeding source lint.
Epistemic authority and scope: conformance to matched schema only.
Operational authority: may return authoring work for correction through the supplied lint protocol.
Behavioral-authority path: author/Copy Editor via metrics, advisory or selected lint gate, current cycle.
Evidence: SRC-1 `.claude/skills/scholarly-citation/checks.py`
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: schema match is not epistemic endorsement.
Gap/limit: English composite claims need author/Desk judgment rather than the Korean composite regexes.

Route ID: [EPI-RTE-join-surface](#epi-rte-join-surface)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-narrative-pages](#epi-obj-narrative-pages)
Content/update relation: no content change
Transition or check target: lines with two distinct declared-source links before Connections.
Evaluator/condition and domain: code link-set membership; not entailment or substantive join validity.
Activation and timing: synthesis lint before Desk by protocol.
Possible or observed result: targeted invocation prints every detected entry as a stripped line excerpt clipped to 70 characters plus sorted source slugs; corpus invocation computes entries but prints no join entries.
Implemented force: advisory.
Epistemic authority and scope: locates a review target, does not prove or disprove its claim.
Operational authority: targeted diagnostics request span-by-span Desk comparison; corpus output does not supply join targets.
Behavioral-authority path: targeted stdout can supply excerpts and slugs to Desk through the review protocol; corpus stdout cannot supply the computed entries. The all-declared-source Desk read remains required by doctrine; actual delivery and compliance are unobserved.
Evidence: SRC-1 `tools/_lint/synthesis.py`
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: join count is not a verdict.
Gap/limit: missing declared links, cross-line joins and source selection can escape this surface. Clipping can omit the claim's decisive wording; the targeted excerpt is a locator requiring page/span reads, not full-line evidence. Corpus invocation supplies no join-entry channel.

Route ID: [EPI-RTE-desk-check](#epi-rte-desk-check)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-source-claims](#epi-obj-source-claims), [EPI-OBJ-narrative-pages](#epi-obj-narrative-pages)
Content/update relation: no content change
Transition or check target: framing, attribution, argument and readability; synthesis joins receive component-span comparison.
Evaluator/condition and domain: fresh model, six lenses/two personas, declared sources and raw on source sub-trigger; see record.
Activation and timing: after quantitative check; source threshold, mandatory/applied content cells differ.
Possible or observed result: defect list or reasoned zero-defect report.
Implemented force: specified qualitative gate, not software enforcement.
Epistemic authority and scope: evidence-consuming judgment about the named draft and read sources; not corroboration of outside-world truth.
Operational authority: defects can trigger ADAPT, escalation or operator decision.
Behavioral-authority path: see [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance); Desk report to author/main, protocol force, current publication cycle.
Evidence: SRC-1 `.claude/agents/desk.md`
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: fresh eyes requests independence of context, not statistical independence of errors.
Gap/limit: no production-review trace links a retained page to this check.

Route ID: [EPI-RTE-editorial-disposition](#epi-rte-editorial-disposition)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-narrative-pages](#epi-obj-narrative-pages)
Content/update relation: no content change
Transition or check target: publication eligibility, distinct from detecting defects.
Evaluator/condition and domain: quantitative completion criteria plus Desk findings, Editor-in-Chief routing and applicable operator gates.
Activation and timing: after checks/revisions; operator explicitly chooses synthesis save.
Possible or observed result: publish, revise, hold or decline; no observed acceptance instance established.
Implemented force: protocol.
Epistemic authority and scope: intended use is wiki publication; criterion is editorial/grounding conformance, not an independent universal truth test.
Operational authority: authorize publication or route back to author; filesystem writes can already exist.
Behavioral-authority path: Editor-in-Chief/operator via review reports, permissive protocol, publication cycle.
Evidence: SRC-1 `.claude/layers/synthesis.md`, `.claude/commands/wiki-query.md`; see record.
Claim IDs: [RT-CLM-human-supervision](runtime.md#rt-clm-human-supervision), [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: no software-wide veto; synthesis advisory lint can exit zero with structural failures.
Gap/limit: no evidence-consuming recorded acceptance of an ampliative claim traced here.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-claims](#epi-obj-source-claims), [EPI-OBJ-claim-markers](#epi-obj-claim-markers)
Content/update relation: no content change
Transition or check target: authored file and derived index persistence, not acceptance.
Evaluator/condition and domain: see records.
Activation and timing: writes/rebuild; candidate drafts can persist before gate completion.
Possible or observed result: retained Markdown and generated state.
Implemented force: software file effects for rebuild, instructed model writes for prose.
Epistemic authority and scope: availability only.
Operational authority: permits later lookup and authoring reuse.
Behavioral-authority path: query/author via retained files and indices, permissive across invocations.
Evidence: SRC-1 `tools/_build/graph.py`; supplied records.
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: retention is not lifecycle integration.
Gap/limit: linking/cascade can organize a candidate, but no instance's prior acceptance is established, so accepted lifecycle integration is not determinable.

Route ID: [EPI-RTE-narrative-authoring](#epi-rte-narrative-authoring), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-narrative-pages](#epi-obj-narrative-pages)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: selected source content to cross-source answer, commentary or chronology.
Evaluator/condition and domain: model authoring with source spans and dates; see records.
Activation and timing: query, save, trail create/follow or timeline request.
Possible or observed result: answer or retained narrative candidate.
Implemented force: interpreted instructions.
Epistemic authority and scope: attribution is requested; semantic preservation, entailment or ampliation must be decided per resulting proposition.
Operational authority: simple answers delivered without saving; approved saves enter publication chain.
Behavioral-authority path: reader or later wiki user via prose, advisory/permissive, current answer or later invocation.
Evidence: SRC-1 `.claude/commands/wiki-trail.md`, `.claude/commands/wiki-timeline.md`, `.claude/commands/wiki-query.md`
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: synthesis label alone does not establish new warranted knowledge.
Gap/limit: no traced candidate/premise pair establishes entailment or non-entailment. Reshaping, entailed derivation and ampliative conjecture remain live classifications.

Route ID: [EPI-RTE-contradiction-derive](#epi-rte-contradiction-derive)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction-db](#epi-obj-contradiction-db)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: source-authored contradiction assertions to extracted DB entries and metadata.
Evaluator/condition and domain: regex category cascade and weighted metadata rules, see record; derived scores are code-defined features.
Activation and timing: build contradictions.
Possible or observed result: open records with type, type_score and evidence_strength.
Implemented force: persistent symbolic derivation.
Epistemic authority and scope: preserves an asserted dispute and computes heuristic features; neither category nor strength adjudicates the dispute.
Operational authority: makes assertions available to contradiction maintenance and downstream readers.
Behavioral-authority path: lint reads DB and advises main/Desk; permissive/advisory, next maintenance invocation.
Evidence: SRC-1 `tools/_build/contradictions.py`
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: source assertion and program-derived label are not corroborating witnesses.
Gap/limit: source selection and grade accuracy unknown; no calibrated warrant claim supported.

Route ID: [EPI-RTE-reground-surface](#epi-rte-reground-surface)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction-db](#epi-obj-contradiction-db)
Content/update relation: no content change
Transition or check target: superseded type with open status.
Evaluator/condition and domain: exact metadata conjunction, not judgment that dispute really ended.
Activation and timing: contradiction lint.
Possible or observed result: advisory requesting re-adjudication.
Implemented force: advisory.
Epistemic authority and scope: potential stale reliance only.
Operational authority: asks Desk/operator to reconsider; does not close the claim or prevent query use.
Behavioral-authority path: foreground agent/Desk via stdout, advisory, maintenance cycle.
Evidence: SRC-1 `tools/_lint/contradiction.py`
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: cleanup/withdrawal not implemented by this surface.
Gap/limit: rebuild stamps open; this is a bounded finding, not a search-complete assertion that every other removal path is absent.

Route ID: [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-claims](#epi-obj-source-claims), [EPI-OBJ-narrative-pages](#epi-obj-narrative-pages)
Content/update relation: no content change
Transition or check target: stored state to CLI retrieval/export selection; answer behavior itself remains doctrine.
Evaluator/condition and domain: graph filters and export selection; host model instructed to fetch bodies before answering.
Activation and timing: see records.
Possible or observed result: selected graph facts or export context; no hosted answer trace.
Implemented force: selection/delivery, not truth validation.
Epistemic authority and scope: inherits uncertain source and synthesis warrant; export omits source/hub bodies.
Operational authority: permits answering and reader navigation without rerunning publication checks.
Behavioral-authority path: local model/hosted reader via pages or bundles, permissive, current query or later uploaded sessions.
Evidence: SRC-1 `tools/query.py`, `.claude/commands/wiki-query.md`; supplied export record.
Claim IDs: [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust)
Mismatch marker: retrieval and successful lookup do not renew endorsement.
Gap/limit: upload refresh manual; no per-answer expiry/withdrawal gate established.

Route ID: [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: role guidance, see [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance)
Content/update relation: non-truth-apt policy/content update: editing authoring/review rules, possibly accompanied by truth-apt diagnoses of defects.
Transition or check target: proposed instruction change against motivating and regression tasks.
Evaluator/condition and domain: software checks and blind model comparisons, with operator adoption and possible waivers; see record.
Activation and timing: recurrent defects/feedback.
Possible or observed result: accept/reject/defer, revised guidance and transition records by protocol.
Implemented force: operator-mediated policy, not automatic substantive acceptance from an accept log field.
Epistemic authority and scope: measured task comparisons, if performed, would not establish transfer or the proposed causal explanation by themselves.
Operational authority: revised instructions can govern later author/reviewer invocations.
Behavioral-authority path: see [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance); interpreted policy, subsequent cycles.
Evidence: SRC-1 `.claude/agents/editor-in-chief.md`; supplied route.
Claim IDs: [EPI-CLM-evolving-guidelines](#epi-clm-evolving-guidelines)
Mismatch marker: self-proposal is not autonomous adoption or demonstrated improvement.
Gap/limit: no live consumption and subsequent causal dependence traced.

Route ID: [EPI-RTE-judge-measurement](#epi-rte-judge-measurement)
Route function: check/evidence production
Architectural status: observed, implementation uninspected
Object/candidate ID: [EPI-OBJ-experiment-ledger](#epi-obj-experiment-ledger)
Content/update relation: no content change
Transition or check target: judge ranking of source-page defects relative to AI Desk labels.
Evaluator/condition and domain: two blind labelers, third on disagreement, critical/high endpoint; judge probabilities and AUC comparisons per plan.
Activation and timing: bounded September experiment, not ordinary publication.
Possible or observed result: sampled defect rows and judge score rows are supplied artifacts.
Implemented force: experiment/reporting, not a demonstrated production acceptance veto.
Epistemic authority and scope: assess agreement/ranking against this model-defined reference, not independent world truth.
Operational authority: plan selects expansion or directional report; implementation of that decision not inspected.
Behavioral-authority path: researcher/operator reads experiment outputs, advisory, experimental rounds.
Evidence: SRC-1 `docs/experiments/judge-model-2026-09/preregistration.md`
Claim IDs: none
Mismatch marker: reference labels are judgments, not infallible answer oracle.
Gap/limit: no scorer/question text, full replication or independent comparison performed here; no component-causal claim.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-newsroom-trust](#epi-clm-newsroom-trust) | see record | SRC-1 `README.md`, doctrine/design | Separate author/check/review roles; grounding and editorial standards | [EPI-RTE-citation-check](#epi-rte-citation-check), [EPI-RTE-join-surface](#epi-rte-join-surface), [EPI-RTE-contradiction-derive](#epi-rte-contradiction-derive) | Sampled experiment labels only; not a production gate trace | No independently varied reviewer/family or factual outcome comparison | A specified evidence-aware editorial process with deterministic structural support | Both gates are not universal enforced conditions: source trigger, advisory checks, alternate hosts and direct CLI qualify the rhetoric. |
| [EPI-CLM-evolving-guidelines](#epi-clm-evolving-guidelines) | see record | SRC-1 `README.md`, doctrine/design; private figures reported operation | [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change) | Schema/log and edit affordances, see supplied route | Private amendment totals attributed, not independently reconstructed | Waivers and mixed unmeasured changes prevent global improvement attribution | System can propose retained behavior-shaping rules under operator adoption | No autonomous adoption; no exercised self-improvement demonstrated in inspected evidence. |
| [RT-CLM-human-supervision](runtime.md#rt-clm-human-supervision) | see record | see record | [EPI-RTE-editorial-disposition](#epi-rte-editorial-disposition) | Gates are protocol, not universal file admission | No production acceptance trace | No proof human gate occurred on every page | Direction/acceptance remain human responsibilities by contract | Ingest initiation and save approval do not establish per-claim endorsement. |

## Bounded conclusion

The system acquires attributed claims, retains text and symbolic lineage, and asks later models to consume page bodies rather than retrieval snippets. Grades encode source categories; regex PASS licenses schema conformance, not truth. Cross-source narrative creation is specified, but no inspected claim/premise pair establishes an entailed derivation, ampliative conjecture or accepted ampliative product. See [EPI-OBJ-source-claims](#epi-obj-source-claims), [EPI-RTE-citation-check](#epi-rte-citation-check), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).

The substantive check is source-consuming editorial judgment, with unusually explicit synthesis join comparison and opened/unopened-source reporting. Its criteria and intended publication use are explicit, but its application is conditional and interpreted by the host. The deterministic detector supplies join excerpts and source slugs only through targeted synthesis lint; corpus summaries omit the computed entries. Even targeted excerpts are clipped to 70 characters, so they locate rather than reproduce full claims. The separate Desk protocol still requires reading every declared source and comparing surfaced joins span by span; actual checker-to-reviewer delivery is not established. A defect report can change author revision and publication behavior; it is not itself a recorded acceptance. No production candidate was traced through acceptance then integration, so organized retention cannot substitute for accepted lifecycle integration. See [EPI-RTE-desk-check](#epi-rte-desk-check), [EPI-RTE-editorial-disposition](#epi-rte-editorial-disposition).

Deterministic contradiction processing carries forward author assertions and adds heuristic metadata. A superseded/open hit asks for reconsideration; it does not remove operational reliance. The inspected build recreates open status. Downstream queries and exports can reuse content without a renewed substantive check, and export omits grounding bodies. These are distinct limits on withdrawal, freshness and accessible evidence, not evidence that all retained claims are wrong. See [EPI-RTE-contradiction-derive](#epi-rte-contradiction-derive), [EPI-RTE-reground-surface](#epi-rte-reground-surface), [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export).

The instruction-change pathway can alter later behavior through retained policy text without requiring a newly accepted factual theory. It is improvement-directed and operator-mediated. The missing links are observed installation/consumption and later behavior causally depending on the update; neither improved capacity nor successful self-improvement follows from proposal, retention or reported amendment counts. Reflection, autonomous adoption and content-directed theory criticism are not inferred from one another. The inspected account does not independently establish all theory-builder conditions, and uninspected feedback/measurement detail prevents a whole-system absence claim. The judge experiment supplies bounded evidence of review/score artifacts, not a general truth oracle or demonstrated component effect. See [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change), [EPI-RTE-judge-measurement](#epi-rte-judge-measurement).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-claims
Label: source-page claims

Source-native identity: Summary, Key Claims and Key Quotes in source pages. Natural-language propositions and attributed quotations in Markdown on disk; truth apt over each source's asserted topic, date and speaker. Distinct from the ingest route, which has no supplied object counterpart. Imported utterance truth and proposition truth differ. SRC-1 `.claude/layers/source.md`.

> A source page (`wiki/sources/<slug>.md`) enforces **three epistemic primitives** as its schema — claim atomization · citation type · evidence grade.
> --- `.claude/layers/source.md`

#### EPI-OBJ-claim-markers
Label: grade and citation markers

Source-native identity: fact/analysis/forecast tokens, claimant links, citation prefixes and anchors. Symbolic fields within source Markdown, later graph JSON, consumed by deterministic parsers; source claims remain a separate natural-language object. No supplied operative-object counterpart. SRC-1 `.claude/layers/source.md`, `tools/_build/graph.py`.

> - **When classification is ambiguous**: default to `[analysis]`. A conservative `[analysis]` classification is safer than over-claiming `[fact]`.
> --- `.claude/layers/source.md`

> m = GRADE_MARKER_RE.match(line)
>     if m:
>         return m.group(1)
>     return None
> --- `tools/_build/graph.py`

#### EPI-OBJ-narrative-pages
Label: synthesis and narrative pages

Source-native identity: synthesis analyses, trail commentary and timeline entries; natural-language claims plus symbolic links/dates/sources, stored as Markdown in the respective wiki folders. Their checks/consumers differ by route below. No supplied object counterpart; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) is a producer/consumer, not the object. SRC-1 `.claude/layers/synthesis.md`, `.claude/commands/wiki-trail.md`, `.claude/commands/wiki-timeline.md`.

> A synthesis page (`wiki/syntheses/<slug>.md`) is a **cross-source analytical answer to a standing question**
> --- `.claude/layers/synthesis.md`

#### EPI-OBJ-contradiction-db
Label: contradiction records

Source-native identity: extracted claim text, source locator, open status, classification and numeric strength in `wiki/contradictions/_contradictions.json`. Mixed natural-language claim string and symbolic metadata on disk; numerical scalars are localized program-defined features, not distributed-parametric representations. No supplied object counterpart. Evidence is in [EPI-RTE-contradiction-derive](#epi-rte-contradiction-derive).

#### EPI-OBJ-experiment-ledger
Label: judge experiment ledgers

Source-native identity: JSONL Desk defect/review records and judge p/model_version/state_hash/q_hash records in the shipped experiment. Natural-language defect arguments and symbolic fields on disk. Distinct from the runtime production routes; no supplied object counterpart. SRC-1 `docs/experiments/judge-model-2026-09/README.md`.

> Labels come from AI reviewers (the wiki's Desk role) working blind, two per page, with a third on disagreement.
> --- `docs/experiments/judge-model-2026-09/README.md`

### Routes

#### EPI-RTE-citation-check
Label: citation schema measurement
Part of: [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)

Owner: citation checker called by source lint; endpoints: source text plus injected page/section lookup → metric tuples. Code controls progression; no model oracle. Inspection deduction: the one-claim text `## Key Claims\n- [fact] Alice — the Moon is cheese` produces claim_total=1 and grade_count=1, hence G1 PASS regardless of whether its proposition is true. This is a concrete code deduction, not target execution. G2 and other metrics are separate; no whole-page PASS claimed. SRC-1 `.claude/skills/scholarly-citation/checks.py`.

> grade_count = len(GRADE_MARKER_RE.findall(claims_body))
>     g1_pass = (claim_total == 0) or (grade_count == claim_total)
> --- `.claude/skills/scholarly-citation/checks.py`

> G3_COMPOSITE_RE = re.compile(r"\[\[[^\]]+\]\][^\n]*\s(와|및)\s[^\n]*\[\[[^\]]+\]\]")
> --- `.claude/skills/scholarly-citation/checks.py`

- Immediate return: metric tuples and missing-line samples to lint.
- Later read-back: inapplicable — checker does not retain content.
- Delegated visibility: Copy Editor/main can consume lint metrics.
- Selection predicate: source lint invokes citation bundle for selected pages.
- Invalidation or expiry: recomputed from current body and injected context.
- Activation or effect: code produces metrics; acceptance use follows lint protocol.
- Evidence limits: regex conformance does not check truth, grade accuracy or actual speaker identity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-join-surface
Label: synthesis join surfacing
Part of: [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)

Owner: synthesis checker. Endpoints: stripped synthesis body and declared sources → internal entries for lines citing at least two distinct declared sources before Connections → invocation-specific stdout. Each entry holds only the first 70 characters of the stripped line and sorted matching source slugs. Targeted `run(target=...)` calls `_print_per_file`, printing every entry; corpus `run()` calls `_print_corpus_summary`, which prints no join entries. Does not edit the substantive claim. Source-native detector identity differs from Desk's semantic evaluator. SRC-1 `tools/_lint/synthesis.py`.

> if len(hits) >= 2:
>                 join_units.append((line.strip()[:70], sorted(hits)))
> --- `tools/_lint/synthesis.py`

> if ADVISORY_MODE or result["misfile"]:
>             return 0
> --- `tools/_lint/synthesis.py`

Branch and transformation evidence, SRC-1 `tools/_lint/synthesis.py` (implementation):

> for text, slugs in joins:
>             print(f"    {slugs} · {text}")
> --- `tools/_lint/synthesis.py`

> result = _evaluate(f"syntheses/{slug}.md", slug, content)
>         _print_per_file(result)
> --- `tools/_lint/synthesis.py`

> # Corpus scan.
>     results = []
>     for path, content in iter_md(SYNTHESES_DIR):
>         results.append(_evaluate(f"syntheses/{path.name}", path.name[:-3], content))
>     _print_corpus_summary(results)
> --- `tools/_lint/synthesis.py`

Reinspection of the complete `_print_corpus_summary` body finds no join-entry print. Static countercase: a detected line longer than 70 characters retains only its stripped prefix in the entry; targeted printing cannot restore the omitted suffix. The corpus branch computes the same entries but never prints them. Neither deduction requires target execution. Desk's independent all-source requirement remains doctrine:

> Spot check (1–2 items) that quoted attribution precisely matches the claim. **Synthesis is the exception** — open every declared source; the claims surfaced by lint `[Join]` are verified span by span, never sampled (`struct.join-grounded`, grounded in lens 4)
> --- `.claude/agents/desk.md`

Countercase to lint-as-substantive-veto: markup and type errors hard-fail, but advisory-mode structural failures can still return zero. No causal or operation inference follows.

- Immediate return: targeted invocation prints all detected join entries as clipped excerpts plus slugs and other per-file diagnostics; corpus invocation returns aggregate/selected failure diagnostics without join entries.
- Later read-back: inapplicable — detector output is current-run diagnostics, not retained memory.
- Delegated visibility: Desk is instructed to open every declared synthesis source and compare surfaced joins span by span; targeted stdout can deliver excerpt/slug locators, but corpus stdout omits the computed entries. No actual report delivery is observed.
- Selection predicate: non-misfiled synthesis, pre-Connections lines with at least two declared source hits.
- Invalidation or expiry: recalculated on lint invocation.
- Activation or effect: targeted diagnostics offer advisory location guidance, not join correctness judgment; corpus diagnostics do not expose join entries.
- Evidence limits: single-line declared-source detector cannot guarantee all semantic joins are surfaced; clipping loses wording beyond 70 characters, and internal computation does not establish consumer delivery. Full claims and component spans require direct reads.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-desk-check
Label: Desk evidence comparison
Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This record individuates the qualitative checking function within ingest, also reused for synthesis/narrative review. Owner: Desk model; inputs draft, guide and grounding; output specific defects/reasons, not edits. Source review triggers at seven fact claims and three citations; synthesis requires every declared source and component spans rather than 1–2 spot checks. Proposer is author; checker is separate Desk; publication veto/hold is owned by disposition, not this checking function. No expected-answer oracle; open authoring/review mode. SRC-1 `.claude/agents/desk.md`.

> - Fill the reply's **Sources compared**·**Sources not opened** fields on every review — a misattribution raised against a page whose support sits in an unopened source is a gap in the read, not a defect in the page
> --- `.claude/agents/desk.md`

> - **(synthesis) a claim fusing two sources fabricates, at the seam, a fact present in neither span (conflation)** — compare the lint `[Join]` surface point against each component span to verify the join is actually derived from the union.
> --- `.claude/agents/desk.md`

- Immediate return: structured defect list or reasoned zero-defect result.
- Later read-back: uninspected — no persisted review-instance provenance traced.
- Delegated visibility: author/main receive report; Desk independently reads files by protocol.
- Selection predicate: applicable layer cell and source sub-trigger; synthesis all-source exception.
- Invalidation or expiry: one pass per ADAPT cycle with bounded diverged re-adjudication.
- Activation or effect: requests evidence-consuming critique; production compliance not observed.
- Evidence limits: doctrine/design; fresh context does not prove accuracy or independent error distribution.
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### EPI-RTE-editorial-disposition
Label: editorial publication decision
Part of: [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Distinct function from checking: Editor-in-Chief uses Copy Editor/Desk results and applicable human decisions to route publish/revise/hold. Scope is saved synthesis publication; quantitative required criteria and grounding/manual join checks specify intended use and criterion. Model author proposes; operator can decline save or reject critical/high cases. No automatic recorded factual acceptance follows from a successful file write or lint code. SRC-1 `.claude/layers/synthesis.md`, `.claude/commands/wiki-query.md`.

> - All 9 required (roster `required`: struct.schema-sections·struct.source-coverage·struct.source-exists·struct.through-line·struct.join-grounded·enc.broken-link·jrn.lede·con.scr·cit.grounding) PASS
> --- `.claude/layers/synthesis.md`

> 5. Editor-in-Chief publish gate + `log.md` append
> --- `.claude/commands/wiki-query.md`

Recovery is author revision/recheck or holding publication, not transaction rollback. Retained proposals and drafts are not automatically accepted.

- Immediate return: prescribed publication/hold/revision outcome.
- Later read-back: approved saved content enters later wiki queries; no acceptance instance traced.
- Delegated visibility: main sees check reports; operator sees applicable gate decisions.
- Selection predicate: explicit save approval, applicable quantitative and qualitative criteria.
- Invalidation or expiry: uninspected — no instance-specific revocation history supplied.
- Activation or effect: protocol grants publication authority, not independently corroborated truth.
- Evidence limits: no inspected production trace joins criterion, evidence and acceptance decision.
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### EPI-RTE-narrative-authoring
Label: trail and timeline narrative

No exact supplied counterpart: overlaps query authoring but distinct entry points, source-pool selection and later follow behavior. Columnist selects trail pages or timeline source pool, writes narrative, then Copy Editor/Desk/main apply the stated cycle. Operator can reject applicable critical/high findings and out-of-range trails. In open-request mode, source pages/date evidence guide proposals; no answer oracle. Source truth is not entailed by chronological ordering. No instance establishes whether a proposed connection is merely reshaping or a new conjecture. SRC-1 `.claude/commands/wiki-trail.md`, `.claude/commands/wiki-timeline.md`.

> 2. Select a seed page + build a 5-12 page trail following the connections
> 3. Write the commentary on why each step connects
> --- `.claude/commands/wiki-trail.md`

> 3. Read each source → 1-2 lines of key facts. **entry-date guard**: the entry date must be directly backed by the source's `published` (or an occurrence date stated in the body) — it cannot be later than `scraped` (year typo), and when splitting one source across multiple points in time, each point must be stated in the body (otherwise demote to the hub `## Timeline`, no standalone timeline exposure).
> --- `.claude/commands/wiki-timeline.md`

- Immediate return: trail/timeline candidate and prescribed review/save report; follow mode explains existing trail.
- Later read-back: trail follow reads retained trail then pages in order; timelines persist for later wiki consumption.
- Delegated visibility: Columnist reads sources; separate reviewers read artifacts by procedure.
- Selection predicate: topic/target/year; timeline backlinks union hub sources; trail 5–12 linked pages.
- Invalidation or expiry: uninspected — detailed layer maintenance not inspected.
- Activation or effect: source-conditioned narrative production and reuse requested, not observed.
- Evidence limits: command doctrine; detailed checker/date enforcement uninspected.
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### EPI-RTE-contradiction-derive
Label: contradiction DB derivation
Part of: [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)

Owner: build code. Endpoints: source Connections contradicts lines → extracted text/ID/open status → category/score/strength → JSON. Category is first matching priority rule, not a semantic proof of incompatibility. Strength combines anchor, date, fact-grade ratio and hub type; those signals cannot certify source truth. Concrete static trace: any matching contradiction line whose captured text passes the length/skip filters is assigned open before classification, regardless of its source grade or whether the dispute is settled. The grade parser merely returns a matched token as inspected in `tools/_build/graph.py`. SRC-1 `tools/_build/contradictions.py`.

> items.append({
>                 "id": _claim_id(claim_text),
>                 "source": rel,
>                 "claim": claim_text,
>                 "status": "open",
>             })
> --- `tools/_build/contradictions.py`

> type_score = sum of matched pattern weights (capped at 1.0). Higher score
>     means more keyword density indicating the type. NOT a calibrated probability —
>     measures pattern-match strength, not classifier confidence.
> --- `tools/_build/contradictions.py`

> strength = (
>         EVIDENCE_WEIGHTS["anchor"] * anchor_score
>         + EVIDENCE_WEIGHTS["recency"] * recency_score
>         + EVIDENCE_WEIGHTS["primary"] * primary_score
>         + EVIDENCE_WEIGHTS["hub_type"] * hub_type_score
>     )
> --- `tools/_build/contradictions.py`

- Immediate return: derived JSON and build summary.
- Later read-back: contradiction lint reloads records, including reground-status comparison.
- Delegated visibility: model maintenance can inspect retained DB and diagnostics.
- Selection predicate: non-underscore source Markdown, Connections contradicts lines passing filters.
- Invalidation or expiry: rebuild regenerates records; content-based IDs change with claim text.
- Activation or effect: persistent availability of extracted assertions and heuristic metadata.
- Evidence limits: no dispute adjudication; metadata derivation is implementation, operation unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-reground-surface
Label: superseded-open re-adjudication
Part of: [RT-RTE-build-lint](runtime.md#rt-rte-build-lint)

Owner: contradiction lint. Endpoints: DB records → exact superseded/open filter → stdout advice to Desk/operator. Neither closes the claim nor withdraws it from retrieval. Distinct from build derivation: it changes maintenance attention, not the DB. SRC-1 `tools/_lint/contradiction.py`.

> means "worth re-adjudicating", not "provably settled". Hence **advisory
>     only**: deciding a dispute is actually settled is a Desk judgment ending at
>     the operator gate, never an automatic close.
> --- `tools/_lint/contradiction.py`

> stuck = [c for c in claims
>              if c.get("type") == "superseded" and c.get("status") == "open"]
> --- `tools/_lint/contradiction.py`

- Immediate return: potential stale-dispute advisory.
- Later read-back: inapplicable — no retained change produced by this function.
- Delegated visibility: foreground maintainer can request Desk/operator re-adjudication.
- Selection predicate: type superseded AND status open.
- Invalidation or expiry: repeated until underlying status/type differs; rebuild assigns open.
- Activation or effect: attention signal only, no implemented automatic closure here.
- Evidence limits: no adjudication instance or global withdrawal audit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-RTE-judge-measurement
Label: judge ranking experiment

No supplied route counterpart: this is experimental evaluation, not the production Desk gate. Owner: experiment authors; labels proposed by independent AI calls, third resolves endpoint disagreement; operator sets expansion rule. Reference outcome is AI-labeled page critical/high status, not external truth. Plan compares judge score, source sub-trigger and body length; cohort/amendment limits apply. Artifacts establish supplied results, not independently authenticated execution or causal component attribution. SRC-1 `docs/experiments/judge-model-2026-09/preregistration.md`.

> - **Primary endpoint:** a page is *defective* if it has ≥1 defect rated critical or high.
> - Agreement: if A and B agree on the endpoint, that is the label. If they disagree, a third labeller (C) reviews the page alone, and C decides.
> --- `docs/experiments/judge-model-2026-09/preregistration.md`

Sampled A2 rows explicitly criticize narrator interpretation absorbed into a fact line, conjunctive conditions dropped, and hedges lost. This is a source-supported countercase to assuming that attribution/schema alone preserves meaning. Their raw-evidence claims were not independently checked here.

> "issue":"The summary reduces a two-part conjunctive test to compute alone."
> --- `docs/experiments/judge-model-2026-09/labels/A2.jsonl`

> The judge's question wording is not included; the scorer stays unpublished.
> --- `docs/experiments/judge-model-2026-09/README.md`

- Immediate return: supplied defect/review records and judge criterion scores.
- Later read-back: analysis/reporting uses retained labels/scores; production integration uninspected.
- Delegated visibility: labelers restricted to pages/originals/needed hubs/SoTs, blinded to measurement by prompt.
- Selection predicate: frozen source populations and later topic/source-type expansion, per preregistration.
- Invalidation or expiry: round-two plan reuses unchanged labels and latest applicable score rows.
- Activation or effect: supplied sampled review/score artifacts; no demonstrated production admission change.
- Evidence limits: hidden scorer/questions and missing raw originals prevent full replication; model labels are fallible reference judgments.
- artifact conclusion status: observed
- implementation conclusion status: uninspected
- causal conclusion status: uninspected

### Claims

#### EPI-CLM-newsroom-trust
Label: newsroom loops produce trust

Public claim: separated author/reviewer roles, two publication gates, and grounding convert documents into a trustworthy persistent cross-referenced knowledge base. Distinct public trust claim relative to [RT-CLM-human-supervision](runtime.md#rt-clm-human-supervision), which concerns human/computational responsibility. SRC-1 `README.md`, doctrine/design.

> Four loops turn that division of labor into trust.
> --- `README.md`

> **Outer** | at publication | two gates — deterministic lint (Copy Editor), then a six-lens qualitative review (Desk) — and both must pass
> --- `README.md`

The bounded comparison concerns specified controls, not a universal verdict about trustworthiness.

#### EPI-CLM-evolving-guidelines
Label: authoring guidelines evolve

Claim: recurrent failures lead to edits of the system's own writing rules and those rules improve. Distinct from human-supervision claim; closest supplied mechanism is [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change). Public prose also qualifies the loop as experimental and private counts include waivers/unmeasured cases. SRC-1 `README.md`, doctrine/design and reported operation.

> When the same review failure keeps recurring, the system drafts a fix to its *own writing rules*.
> --- `README.md`

> The loop is still experimental; I'm measuring whether it earns its keep rather than claiming it's solved.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
