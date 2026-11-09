---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Eva-brain epistemic routes: source-derived Markdown, structural checks, human admission and later reliance."
run-id: AAS-2026-11-09-eva-brain-de4240cd9e79-01
reviewed-boundary: "706fb91f4ee851cc355785f4e7c6eab37146938f"
---

# Eva-brain epistemic report

## Source-and-claim boundary

The question is how Eva turns source documents into durable claims, checks or admits them, and makes them available for later reliance. Scope, exclusions and evidence identity are see [boundary](boundary.md#boundary-and-evidence); the single frozen repository is SRC-1 in the [Source register](boundary.md#source-register). The desktop, its Rust caller, shipped prompts, MCP and structural evaluator are included. External model/runtime internals, real user sources and installed provider state are not inspected. This is an implementation/doctrine account, not an observed execution or effectiveness assessment.

Knowledge-production intent is [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge); the narrower review claim is [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate). Neither is treated as a blanket promise of truth. Semantic routes include ingestion, query, all seven profile tools and Health, not just the ordinary ingest path.

| Entry point or operation | SRC-1 source path | Coverage and supporting records |
| --- | --- | --- |
| Tauri command dispatch | `apps/desktop/src-tauri/src/main.rs` | Direct complete registry read; ingest, query/save/decision, health, profile, bootstrap/settings, import and setup agree with supplied runtime; no extra model-dependent command found in this registry. |
| Source acquisition, worktree proposal, gate and decision | `apps/desktop/src-tauri/src/ingest.rs` | Supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); direct gate and decision reads; content and checks separated below. |
| Query and all runtime dispatch alternatives | `apps/desktop/src-tauri/src/ingest.rs` | Supplied [RT-RTE-vault-query](runtime.md#rt-rte-vault-query); direct dispatcher/command reads confirm three adapters; adapter details are supplied findings, not independently reread in full. |
| Health and profile tools | `apps/desktop/src-tauri/src/ingest.rs` | Supplied [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools); direct profile guidance, seven-tool instruction map, shared prompt, validator and dispatch reads. Model criticism remains requested, not observed. |
| Save formatting, pending review, accept/reject | `apps/desktop/src-tauri/src/ingest.rs` | Direct formatting/preparation/query decision reads; [EPI-RTE-analysis-format](#epi-rte-analysis-format) and [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save). |
| Settings, bootstrap, create/import, setup | `apps/desktop/src-tauri/src/ingest.rs` | Supplied [RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings), [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup); no independent semantic-check inference from setup readiness. |
| Later desktop reload/display/tool save | `apps/desktop/src/main.ts` | Supplied runtime findings only: [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Not an independently inspected UI audit. |
| MCP search, read_page, neighbors, shortest_path | `packages/eva-mcp/server.mjs` | Direct complete read; [EPI-RTE-wiki-navigation](#epi-rte-wiki-navigation); all four registrations covered, none writes. |
| Wiki loading, parser, link resolution, graph | `packages/eva-mcp/vault-io.mjs`, `packages/wiki-lib/src/parse.ts`, `packages/wiki-lib/src/vault.ts`, `packages/wiki-lib/src/graph.ts` | Direct complete reads; selection/graph facts are about stored text and resolved links, not truth of page contents. |
| Structural lint | `packages/wiki-lib/src/lint.ts` | Direct complete read; [EPI-RTE-structural-check](#epi-rte-structural-check). |
| Shipped operating/format contract | `schema/EVA.md`, `docs/EVA_BRAIN_STANDARD.md` | Direct complete reads; epistemic discipline and portable format are doctrine, not evidence of compliance. |
| Product knowledge claim | `README.md` | Direct opening/product description read; [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge). Other promotional claims not assessed here. |

No independent trace identifies actual generated claims, the evidence a reviewer consumed, or changes in later answers. This prevents attributing exercised acceptance, learning or quality gain. Source truth and extraction fidelity are unknown without real source/claim pairs. External model opacity prevents assessment of internal derivation or parametric change, not of Eva's inspectable admission wiring. Remaining supplied implementation coverage is identified as such; this is not an exhaustive negative about all possible filesystem callers or external hooks.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-raw](#epi-obj-raw) | Imported source assertions; actual propositions depend on user documents | Original evidence | SRC-1 `schema/EVA.md`; see record | Acquisition is not endorsement; original source warrant unknown. |
| [EPI-OBJ-wiki](#epi-obj-wiki) | Entity/concept claims, summaries and saved syntheses | Durable linked knowledge | SRC-1 `schema/EVA.md`; see record | Editable prose and links do not prove source entailment. |
| [RT-OBJ-ingest-worktree](runtime.md#rt-obj-ingest-worktree) | see record | Ingest staging | see record | Proposal status differs from merged content. |
| [EPI-OBJ-query-answer](#epi-obj-query-answer) | Answer and page/source citations | Answer from wiki | SRC-1 `apps/desktop/src-tauri/src/ingest.rs`; see record | Nonempty/parseable does not mean supported. |
| [EPI-OBJ-health-report](#epi-obj-health-report) | Alleged contradictions, provenance/staleness problems and questions | Advisory diagnosis | SRC-1 `apps/desktop/src-tauri/src/ingest.rs`; see record | Questions/next steps need not be truth-apt; diagnoses can be. |
| [EPI-OBJ-profile-result](#epi-obj-profile-result) | Evidence maps, decision frames, reflections, threads, study answers | Read-only derived products | SRC-1 `apps/desktop/src-tauri/src/ingest.rs`; see record | Mixed claims and policy; no product instance examined. |
| [EPI-OBJ-lint-issues](#epi-obj-lint-issues) | Structural predicates about parsed pages | New-issue comparator input | SRC-1 `packages/wiki-lib/src/lint.ts`; see record | Does not judge substantive content. |
| [RT-BAP-vault-contract](runtime.md#rt-bap-vault-contract) | Operating guidance, not a source-truth oracle | Contract/profile to task behavior | see record | Settings are direct policy inputs; compliance unobserved. |
| [RT-CMP-codex](runtime.md#rt-cmp-codex), [RT-CMP-claude](runtime.md#rt-cmp-claude), [RT-CMP-eva-qwen](runtime.md#rt-cmp-eva-qwen) | Internal truth-apt content not determinable | External distributed-parametric reasoning | see records | Weight storage, version fixity and mutation limits remain local to each supplied component. |

## Authority-route ledger

The entries are function-specific overlays. Repeated citations name one implementation container, not multiple independent observations. Record-owned progression, activation, selection and limits are `see` the cited record; the fields below assess the epistemic edge and its force.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: User files to retained raw documents
Evaluator/condition and domain: Person chooses sources; filesystem copy, not a truth evaluator
Activation and timing: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Possible or observed result: Raw source available before wiki proposal
Implemented force: Permissive evidence supply
Epistemic authority and scope: Source warrant unknown; preservation of original document is not validation of its assertions
Operational authority: Allows source to be read for ingest
Behavioral-authority path: External model; raw filesystem; evidence supply; ingest and later source inspection
Evidence source ID and local anchor: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Claim IDs: [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge)
Mismatch marker: none; limits stated locally
Gap/limit: No observed execution; implemented request does not prove model compliance.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki](#epi-obj-wiki)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Raw plus existing wiki to proposed page edits
Evaluator/condition and domain: External model under source/provenance/profile guidance; semantic fidelity domain is requested, not independently checked
Activation and timing: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Possible or observed result: Model may summarize, acquire assertions, synthesize or revise
Implemented force: Candidate generation; not yet disposition
Epistemic authority and scope: No established warrant beyond whatever source support is actually preserved
Operational authority: Proposes durable content and links, cannot pass protected edits through this gate
Behavioral-authority path: Worktree/gate; Markdown diff; candidate; pending admission
Evidence source ID and local anchor: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Claim IDs: [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge)
Mismatch marker: none; limits stated locally
Gap/limit: No actual input/output semantic pair: import, reshaping, entailment and ampliative conjecture cannot be distinguished at the produced-claim edge. Non-entailment is not inferred from opacity.

Route ID: [EPI-RTE-structural-check](#epi-rte-structural-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-lint-issues](#epi-obj-lint-issues)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Parsed vault links, incoming edges, metadata and suspicious roots
Evaluator/condition and domain: Deterministic lint rules; domain is this parser's structural representation
Activation and timing: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Possible or observed result: Issue list; new-string difference computed separately by gate
Implemented force: Evidence production for admission
Epistemic authority and scope: Only the named structural predicates; no source truth or summary entailment license
Operational authority: Supplies issues consumed by gate or displayed reviewer
Behavioral-authority path: Rust gate/desktop; issue strings; enforcing hold predicate at gate; one proposal
Evidence source ID and local anchor: see [EPI-RTE-structural-check](#epi-rte-structural-check)
Claim IDs: [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate)
Mismatch marker: none; limits stated locally
Gap/limit: No observed execution; implemented request does not prove model compliance.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-ingest-worktree](runtime.md#rt-obj-ingest-worktree)
Content/update relation: no content change
Transition or check target: Ingest patch admissibility
Evaluator/condition and domain: Protected-path verifier; dirty-status condition; no deletions/no new issue strings, else UI accept/reject
Activation and timing: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Possible or observed result: Reject, auto-merge, or hold then merge/discard
Implemented force: Enforcing at this ingest gate; human overrides structural hold
Epistemic authority and scope: Operational admissibility, not evidence-consuming semantic acceptance of each claim
Operational authority: Allows merge or blocks pending decision; review resumes queue
Behavioral-authority path: Rust merge/worker; Git branch and boolean review; enforcing; current proposal
Evidence source ID and local anchor: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Claim IDs: [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate)
Mismatch marker: none; limits stated locally
Gap/limit: Countercases: inherited lint debt does not hold; human may accept new issues; a false but structurally clean claim can pass. These are limits, not demonstrated bad runs.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki](#epi-obj-wiki)
Content/update relation: no content change
Transition or check target: Admitted edits to main vault and history
Evaluator/condition and domain: Git merge after gate/decision
Activation and timing: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Possible or observed result: Persistent Markdown and operational log
Implemented force: Durable availability
Epistemic authority and scope: Retention does not establish semantic acceptance
Operational authority: Later tasks can read merged claims; rejection removes proposal, not existing claims
Behavioral-authority path: Desktop and later model tasks; files/search; permissive evidence; subsequent tasks
Evidence source ID and local anchor: see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Claim IDs: [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge)
Mismatch marker: none; limits stated locally
Gap/limit: No observed execution; implemented request does not prove model compliance.

Route ID: [EPI-RTE-wiki-navigation](#epi-rte-wiki-navigation)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki](#epi-obj-wiki)
Content/update relation: no content change
Transition or check target: Which stored material is returned
Evaluator/condition and domain: Lexical top-ten, exact/stem/title read, link graph neighbors and undirected BFS
Activation and timing: see [EPI-RTE-wiki-navigation](#epi-rte-wiki-navigation)
Possible or observed result: Excerpts, full body/metadata, neighboring IDs or shortest link path
Implemented force: Ranking for search; permissive delivery otherwise
Epistemic authority and scope: No endorsement of selected statements; graph connection is not evidential entailment
Operational authority: Places selected stored material in agent context
Behavioral-authority path: External runtime/model; MCP text result; ranking/permissive; task and later calls
Evidence source ID and local anchor: see [EPI-RTE-wiki-navigation](#epi-rte-wiki-navigation)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: Search excerpts can omit qualifications; full read is available. Selection is not an acceptance decision.

Route ID: [RT-RTE-vault-query](runtime.md#rt-rte-vault-query)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-query-answer](#epi-obj-query-answer)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Wiki plus question to answer
Evaluator/condition and domain: External model asked to cite supporting pages; Rust parse/nonempty checks operate on output format
Activation and timing: see [RT-RTE-vault-query](runtime.md#rt-rte-vault-query)
Possible or observed result: Displayed cited answer or error
Implemented force: Advisory answer; malformed/empty output rejected
Epistemic authority and scope: No independent verification that citations entail answer or match requested working set
Operational authority: User receives answer; saving requires another command/decision
Behavioral-authority path: UI/person; answer JSON/Markdown; advisory; current query
Evidence source ID and local anchor: see [RT-RTE-vault-query](runtime.md#rt-rte-vault-query)
Claim IDs: [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge)
Mismatch marker: none; limits stated locally
Gap/limit: No semantic pair or execution trace; cannot establish derivation, actual conjecture or scope compliance. Empty citations are allowed rather than proof of an evidence-backed answer.

Route ID: [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-health-report](#epi-obj-health-report)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Wiki contradictions, provenance, staleness, gaps
Evaluator/condition and domain: External model prompted for page IDs and explained local evidence, not general-world staleness judgments
Activation and timing: see [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools)
Possible or observed result: Advisory findings/next steps, possibly empty
Implemented force: Advisory only; no automatic repair or withdrawal consumer
Epistemic authority and scope: A requested evidence-backed diagnosis is a candidate, not established criticism
Operational authority: Can inform a person's next action; does not invalidate pages
Behavioral-authority path: Person; Health UI; advisory; current report
Evidence source ID and local anchor: see [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: No finding instance/trace; cannot credit actual content-directed criticism or a closed revision loop.

Route ID: [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-profile-result](#epi-obj-profile-result)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Wiki to seven profile-specific products
Evaluator/condition and domain: External model uses local record; format/nonempty validation not factual oracle
Activation and timing: see [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools)
Possible or observed result: Evidence map, reflection, threads map, brief, options review, flashcards or exam/key
Implemented force: Advisory/display; optional separate save
Epistemic authority and scope: No independent reference-answer acceptance; generated answer key is not an oracle for its own production
Operational authority: Supplies user-facing product; may be converted to saved answer
Behavioral-authority path: Person and optional save path; JSON/Markdown; advisory; current request or later saved page
Evidence source ID and local anchor: see [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: Domain differs per tool; shared lack of semantic validator does not establish all outputs false or conjectural.

Route ID: [EPI-RTE-analysis-format](#epi-rte-analysis-format)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-query-answer](#epi-obj-query-answer)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Supplied answer/citations to analysis Markdown
Evaluator/condition and domain: Rust string formatting and reference filtering
Activation and timing: see [EPI-RTE-analysis-format](#epi-rte-analysis-format)
Possible or observed result: Analysis prose plus formatted evidence and optional sources metadata
Implemented force: Candidate retention formatting
Epistemic authority and scope: Does not add warrant; reference filtering can degrade explicit lineage
Operational authority: Creates reviewable page/index/log, not immediate main-vault admission
Behavioral-authority path: Review preparer; Markdown diff; candidate; pending decision
Evidence source ID and local anchor: see [EPI-RTE-analysis-format](#epi-rte-analysis-format)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: Citation existence/entailment unchecked; unsafe references can disappear while answer prose remains. See concrete deduction in record.

Route ID: [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-query-answer](#epi-obj-query-answer)
Content/update relation: no content change
Transition or check target: Whether saved answer enters main vault
Evaluator/condition and domain: UI person requests save, then explicit accept/reject; command callers not authenticated humans
Activation and timing: see [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)
Possible or observed result: Merge/discard even when lint issues are displayed
Implemented force: Enforcing decision requirement
Epistemic authority and scope: Acceptance for retention; semantic criterion/evidence-consuming decision not recorded by command
Operational authority: Allows or blocks saved content entering later searches
Behavioral-authority path: query_decide/Git; review boolean; enforcing; this saved proposal
Evidence source ID and local anchor: see [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: A person could evaluate truth, but no trace or mandatory semantic criterion establishes that here.

Route ID: [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki](#epi-obj-wiki)
Content/update relation: no content change
Transition or check target: Approved saved analysis to later wiki consumers
Evaluator/condition and domain: Merge after decision
Activation and timing: see [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)
Possible or observed result: Persistent analysis/index/log
Implemented force: Durable availability
Epistemic authority and scope: Ordinary retained candidate claims, not automatically warranted claims
Operational authority: Later queries/profile tools can reuse them
Behavioral-authority path: Model/person; wiki files/MCP; permissive evidence; later tasks
Evidence source ID and local anchor: see [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: No observed execution; implemented request does not prove model compliance.

Route ID: [RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-BAP-vault-contract](runtime.md#rt-bap-vault-contract)
Content/update relation: non-truth-apt policy/content update: human-selected profile, purpose, language, runtime/model settings
Transition or check target: Direct configuration edit to future task guidance
Evaluator/condition and domain: Software validates settings and clean state; UI person chooses, not a model-evaluated improvement loop
Activation and timing: see [RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings)
Possible or observed result: Changed contract/manifest selection
Implemented force: Dispatch settings enforcing; natural-language guidance instructional
Epistemic authority and scope: No truth endorsement; an extraction lens is not evidence
Operational authority: Changes task framing/endpoint; protected from ingest edits
Behavioral-authority path: Rust and external model; settings and EVA.md; enforcing dispatch/instructional content; later tasks
Evidence source ID and local anchor: see [RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings)
Claim IDs: none
Mismatch marker: none; limits stated locally
Gap/limit: See record for admission and recovery; neither learning nor model-driven self-improvement follows.

No evidence-consuming semantic acceptance or post-acceptance lifecycle integration is established by these inspected consumers. Updating links/index and merging can be organization or retention before such acceptance; they are not relabelled lifecycle integration. Health may advise rejection or revision, and ingest can replace claims, but no automatic semantic withdrawal consumer links Health findings to those edits. The supplied local-runtime setup route is capability admission by readiness, not a truth-apt knowledge evaluator; see [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-durable-knowledge](#epi-clm-durable-knowledge) | see record | see record | see record | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-vault-query](runtime.md#rt-rte-vault-query), [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save), [EPI-RTE-wiki-navigation](#epi-rte-wiki-navigation) | none supplied | No source/claim accuracy comparison or later-answer intervention | Durable linked intermediary is wired; epistemic discipline is prompted | Knowledge label exceeds what structural validity alone licenses; actual quality unknown. |
| [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate) | see record | see record | see record | [EPI-RTE-structural-check](#epi-rte-structural-check), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | none supplied | No runtime evidence; gate predicate is inspectable | New structural issues/deletions force review on ingest; not semantic verification | Human override and inherited issue strings limit strength; not a universal write gate. |

## Bounded conclusion

Eva acquires raw evidence, asks external models to maintain source-linked Markdown, and retains admitted results for later querying. Source warrant is unknown; preserving originals and requesting provenance does not transfer truth to every summary or synthesis ([EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-wiki](#epi-obj-wiki), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)). Concrete generated content is unavailable, so the semantic edges remain indeterminate rather than being uniformly labelled conjecture.

The deterministic evaluator derives structural facts within its parser/link domain. A syntactically suitable but false summary can satisfy its source-prefix rule. New issues/deletions trigger a review channel; neither a clean gate nor review acceptance records a semantic test criterion, intended epistemic use and evidence-consuming warrant decision ([EPI-RTE-structural-check](#epi-rte-structural-check), [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate)). Rejection and cleanup prevent proposed content from entering the main vault; they do not retract already merged claims.

Retained claims gain operational availability through later search/read and answers, not an endorsement bit. Search ranking and short excerpts can affect what evidence reaches the model, while full reads remain available. Explicit graph routes derive connectivity, not explanatory or evidential relations ([EPI-RTE-wiki-navigation](#epi-rte-wiki-navigation)). Query/profile products and Health diagnoses are model candidates. Saving a query/profile product requires a separate review; Health next steps remain advice. Human truth assessment is possible but unobserved ([RT-RTE-vault-query](runtime.md#rt-rte-vault-query), [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools), [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)).

The research lens is an important counterexample to a claim that Eva requests only compression: it explicitly asks for competing-explanation revision and evidence maps. It does not establish that a formulated theory was actually criticized and its revision reused. For that requested research pathway, theory-builder condition 1 is afforded by localized Markdown thesis/competing explanations; condition 2 is afforded by instructions to use existing pages, not observed content-dependent reliance; condition 3 is claimed by profile guidance, not evidenced completed blame-assignment/revision; condition 4 is afforded by retaining updates for future ingest, not observed iteration. Addressability is page-level editable natural language; finer internal theory structure depends on actual content. Persistence across tasks is wired. Learning as improved future capacity is uninspected without performance/attribution evidence. Health's subject matter does not establish reflective self-representation of Eva's own operating machinery. End-to-end autonomous theory building is unestablished by opaque model reasoning and human-held admission paths. These are independent limits, not one negative verdict (SRC-1 `apps/desktop/src-tauri/src/ingest.rs`, profile passages in [EPI-OBJ-profile-result](#epi-obj-profile-result)).

Human configuration can change future behavior without a truth-apt route. The protected contract/settings path is not an inspected trace-fed self-revision loop; external endpoint changes are likewise not evidence of improved Eva performance ([RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings), [RT-BAP-vault-contract](runtime.md#rt-bap-vault-contract), supplied model component records). Implementation supports these bounded capacities without establishing exercised semantic acceptance, integrated accepted ampliative knowledge, reliable criticism, or causal benefit.

## Shared records

### Operative objects

#### EPI-OBJ-raw
Label: Raw source collection

SRC-1, `schema/EVA.md`; imported original documents in filesystem `raw/`, committed by the source-ingest route. Natural-language assertions may occur in text/PDF/etc.; exact input encodings depend on supplied files, not a frozen actual user corpus. Distinct from [RT-OBJ-ingest-worktree](runtime.md#rt-obj-ingest-worktree): original evidence is copied/committed before proposals, not the temporary proposal container. No other supplied object declares the original collection. Import preserves source material, not a truth certificate.

> `raw/` contains the original source documents. It is immutable: agents may
>   read it but must never edit, move, or delete anything in it.
> --- `schema/EVA.md`

#### EPI-OBJ-wiki
Label: Wiki pages

SRC-1, `schema/EVA.md`, `packages/wiki-lib/src/parse.ts`: durable filesystem Markdown. Natural-language body claims reach model/human interpretation; localized metadata and wiki links reach parser/graph rules. This is the retained corpus, distinct from the temporary [RT-OBJ-ingest-worktree](runtime.md#rt-obj-ingest-worktree) that can contain proposed edits to it. Metadata is separately tested by [EPI-OBJ-lint-issues](#epi-obj-lint-issues); it is not authority over body truth.

> The wiki is the generated Markdown outside `raw/`. Agents create and update
>   this layer as new sources and questions add knowledge.
> --- `schema/EVA.md`

> The profile is not a
> license to infer facts: preserve uncertainty, distinguish a source's claims
> from Eva's synthesis, and keep each durable claim close to its evidence.
> --- `schema/EVA.md`

#### EPI-OBJ-query-answer
Label: QueryAnswer

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: returned structured answer with natural-language Markdown and symbolic page/source strings; transient response/UI state until separately saved. Closest supplied [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) is its producer route, not an object counterpart; [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save) can also accept an arbitrary supplied answer. The output label does not attest source support.

> 4. Return a concise Markdown answer and cite every page that materially supports it. Cite exact brain-relative page ids. For each citation, include raw source paths named by that page when available. If there is no supporting evidence, return an empty citations array.
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### EPI-OBJ-health-report
Label: HealthReport

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: transient JSON findings, summary, page IDs and next-step prose; natural-language diagnoses interpreted by a person, symbolic shape parsed by Rust. Distinct product of [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools), not another declaration of that route. It has no inspected automatic edit consumer.

> 3. Be conservative: report a contradiction, stale claim, or provenance weakness only when you can name supporting page ids and explain the evidence. Do not use general-world knowledge to call a claim stale.
> --- `apps/desktop/src-tauri/src/ingest.rs`

> 5. Look for useful findings in: contradiction, provenance, stale-claim, coverage-gap, research-question. A finding must cite exact existing page ids when it relies on them. `nextStep` is only a suggested action. Return no more than 12 findings.
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### EPI-OBJ-profile-result
Label: ProfileToolResult

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`: title/content/citations JSON; Markdown is natural-language product, citation/options fields symbolic. Transient until separate analysis-save. Distinct from HealthReport and QueryAnswer by task and consumer wrapper; shares the supplied advisory route container [RT-RTE-advisory-tools](runtime.md#rt-rte-advisory-tools), not a duplicate route declaration. Personal/threads/decision/options tools mix assertions and suggestions; study tools request answers but supply no independent correctness oracle. Research content may include theories; none is instantiated in the inspected output evidence.

> Self::Research => "Separate claims from their evidence, attach provenance, and update competing explanations when the source challenges the current thesis.",
> --- `apps/desktop/src-tauri/src/ingest.rs`

> Self::ResearchEvidenceMap => "Map the central claims, the evidence for and against each, the confidence or limitations, and the most valuable next question. Keep claims distinct from interpretation.",
> --- `apps/desktop/src-tauri/src/ingest.rs`

> 2. Use only evidence in this brain. If the record is too thin, say exactly what is missing instead of filling gaps from general knowledge.
> --- `apps/desktop/src-tauri/src/ingest.rs`

> if result.title.trim().is_empty() {
>         return Err("agent returned a tool result without a title".into());
>     }
>     if result.content.trim().is_empty() {
>         return Err("agent returned an empty tool result".into());
>     }
> --- `apps/desktop/src-tauri/src/ingest.rs`

#### EPI-OBJ-lint-issues
Label: LintIssue

SRC-1, `packages/wiki-lib/src/lint.ts`: symbolic in-memory page/rule/message objects, rendered to strings for the supplied [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) comparator. Distinct from that route and from the wiki's substantive assertions; no supplied object counterpart. Predicates concern parsed structure, not agreement with source documents.

> export interface LintIssue {
>   /** Page id the issue belongs to. */
>   page: string;
>   rule: LintRule;
>   message: string;
> }
> --- `packages/wiki-lib/src/lint.ts`

### Routes

#### EPI-RTE-structural-check
Label: Structural lint evaluation
Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

The check is a material function inside the supplied combined ingest route; it is also reused for save-review/desktop diagnostics. Owner: deterministic wiki-lib/lint CLI, not a model. Parsed vault → graph/rules → issue list. Target is frontmatter, link resolution, incoming edges and misplaced path roots. The gate separately compares new strings and decides; no semantic answer oracle. No human judgment is needed to produce this list.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: array of structural issues, rendered by the lint CLI for Rust.
- Later read-back: inapplicable — this check does not itself persist material accumulated through use; gate consumes current/baseline lists.
- Delegated visibility: inapplicable — deterministic in-process computation/CLI, no separate reasoning worker.
- Selection predicate: all loaded wiki pages; summary-specific source checks only on type summary.
- Invalidation or expiry: recomputed from loaded state; baseline/post-state difference belongs to gate.
- Activation or effect: issues reach the ingest gate's hold predicate and review payload, not a factual-correction executor.
- Evidence limits: no target execution; predicate truth is about parsed representation only, not source existence/entailment.

SRC-1, `packages/wiki-lib/src/lint.ts`:

> } else if (!source.startsWith('raw/')) {
> --- `packages/wiki-lib/src/lint.ts`

> if (!hasIncoming.has(page.id) && page.type !== 'index') {
> --- `packages/wiki-lib/src/lint.ts`

Concrete implementation deduction, not a test run: a parsed summary with title, type summary and `source: raw/nonexistent.txt` does not trigger missing-source or invalid-source, because only presence and prefix are checked. Its prose could contradict the original without affecting those predicates. Likewise two mutually linked non-index pages each have an incoming edge without requiring an index path. These counterexamples constrain evaluator license; other checks may still report unrelated issues.

#### EPI-RTE-wiki-navigation
Label: MCP wiki navigation

Distinct from supplied [RT-RTE-vault-query](runtime.md#rt-rte-vault-query): reusable read service used by agents, not the query orchestration. No supplied standalone MCP route counterpart. Owner: Node MCP server and wiki-lib. Files → filtered vault → lexical search/page read/graph → JSON tool result. Search ranks lexical matches; neighbors and shortest_path derive explicit link connectivity under fixed resolution and an undirected traversal, not semantic support. The model decides when to request each tool.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked excerpts, full page, adjacency IDs or shortest undirected path/error.
- Later read-back: each call reloads retained wiki, including accepted earlier edits and accessible current worktree edits.
- Delegated visibility: tool caller receives selected JSON text; raw and infrastructure excluded by loader, though native filesystem tools are separate channels.
- Selection predicate: search scores title/alias/stem hit plus body term hits and returns ten; read accepts ID/stem/title; graph follows resolved explicit links.
- Invalidation or expiry: no persistent result cache in inspected service; next call rebuilds from files.
- Activation or effect: delivered text can supply model evidence; no proof it controls a later answer.
- Evidence limits: snippets may lack context; graph truth is bounded by parser/resolver, not relationship validity in the world.

SRC-1, `packages/eva-mcp/server.mjs`:

> const excerpt = at >= 0 ? page.body.slice(Math.max(0, at - 60), at + 120).replace(/\s+/g, ' ') : '';
> --- `packages/eva-mcp/server.mjs`

> return asText({ query, matches: results.slice(0, 10) });
> --- `packages/eva-mcp/server.mjs`

SRC-1, `packages/eva-mcp/vault-io.mjs`:

> .filter((p) => !p.startsWith('raw/'))
> --- `packages/eva-mcp/vault-io.mjs`

Concrete selection deduction: for body `Alpha is uncertain.` and query `alpha`, body match position is zero and the returned excerpt is the original-cased whole short body, not lowercased output or a new factual conclusion. Longer bodies can be cut at the fixed window. Full read returns body/frontmatter without that excerpt truncation. For graph operations, results concern resolved link paths only; there is no evidence-strength edge type.

#### EPI-RTE-analysis-format
Label: Analysis Markdown formatting
Part of: [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)

Distinct material transformation inside the supplied save route, not another admission mechanism. Owner: Rust `analysis_markdown`. Supplied answer/citations → trimmed answer prose, safe evidence links, selected source metadata, heading structure. Candidate file/index/log is prepared before review; admission/rejection remains see [RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save). This transformation does not independently authenticate caller provenance or inspect cited source truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted Markdown string, subsequently written to proposal worktree.
- Later read-back: after separate merge, page is loaded as wiki and can be used in future tasks.
- Delegated visibility: inapplicable — Rust formatting, not a model invocation; UI reviewer receives diff.
- Selection predicate: prose trimmed; citation references rejected if empty/control/bracket/pipe-containing; sources metadata selects raw paths, with summary-page fallback.
- Invalidation or expiry: rejected worktree removed by separate decision route; accepted file has no automatic semantic expiry.
- Activation or effect: preserves answer text while constructing evidence display and optional provenance metadata.
- Evidence limits: filtering may remove references but never establishes entailment; no observed saved instance.

SRC-1, `apps/desktop/src-tauri/src/ingest.rs`:

> let value = value.trim();
>     if value.is_empty()
>         || value.chars().any(char::is_control)
>         || value.contains(['[', ']', '|'])
> --- `apps/desktop/src-tauri/src/ingest.rs`

> .filter_map(|source| safe_reference(source))
>                 .filter(|source| source.starts_with("raw/"))
> --- `apps/desktop/src-tauri/src/ingest.rs`

> answer.answer.trim(),
> --- `apps/desktop/src-tauri/src/ingest.rs`

Concrete implementation deduction: input answer `  Claim A.  ` with citation page `concepts/a` and source `raw/a.txt` retains prose `Claim A.`, emits a wiki evidence link and sources metadata. If the source string instead contains a pipe, it is excluded by safe_reference while the answer prose survives; formatting is non-ampliative, but explicit lineage can be degraded. Neither example is executed or a claim that a real answer had those values.

### Claims

#### EPI-CLM-durable-knowledge
Label: Durable linked knowledge

SRC-1, `README.md`, `schema/EVA.md`: product/design claim of a durable Markdown intermediary and source-derived knowledge, not an explicit infallibility claim. Distinct from [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate), which concerns a narrower review predicate. Prompted provenance/uncertainty gives discipline; structural checks do not validate that discipline semantically.

> Eva helps an agent maintain a durable, linked
> Markdown brain between the sources and the user.
> --- `README.md`

> The purpose of the vault is to turn immutable source material into a
> durable, interlinked body of knowledge — not to act as a chat transcript or a
> temporary retrieval index.
> --- `schema/EVA.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
