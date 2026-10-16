---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of Auto-claude-code-research-in-sleep: empirical support, proof judgment, local checks and later reliance."
run-id: AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01
reviewed-boundary: 26b95cfa0d8747078e9e43b42e20952709e561b8
---

# Auto-claude-code-research-in-sleep epistemic report

## Source-and-claim boundary

The question is how ARIS converts research inputs into claims that affect later research or writing. The [boundary and Source register](boundary.md#source-register) fix SRC-1 and the partial-loop scope. ARIS supplies host-followed procedures and executable helpers, not the external agent host, model service or experiment environment. No execution trace, target execution or causal experiment was supplied or performed. Implementation findings do not establish that a host followed the procedures.

Assessed route families are empirical support judgment, proof acceptance criteria, local evidence checking, wiki claim retention and selective reuse, plus supplied review-stop, resume and harness-patch routes. Warrant claims are [EPI-CLM-result-support](#epi-clm-result-support), [EPI-CLM-proof-verification](#epi-clm-proof-verification) and [RT-CLM-review-independence](runtime.md#rt-clm-review-independence). No supplied record needs supersession; new records identify distinct mechanisms, not alternate names for existing referents.

| Entry point or operation | Source path | Coverage or prevented conclusion |
|---|---|---|
| Plugin/setup, MCP dispatch and direct nightmare CLI | `.claude-plugin/plugin.json`, `commands/setup.md`, `mcp-servers/codex-exec/server.py`, `skills/auto-review-loop/SKILL.md` | Supplied findings only: [RT-RTE-codex-call](runtime.md#rt-rte-codex-call). Arbitrary prompts/direct CLI prevent a universal enforced independent-input claim. |
| Pipeline and experiment sanity/deployment | `skills/research-pipeline/SKILL.md`, `skills/experiment-bridge/SKILL.md` | Supplied [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline); queue implementation uninspected, preventing end-to-end experiment assurance. |
| Review stop and phase acceptance/resume | `tools/review_gate.py`, `tools/run_state.py`, `tools/provenance.py` | Supplied [RT-RTE-review-transition](runtime.md#rt-rte-review-transition), [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume); not semantic evidence verifiers. Native Copilot evidence-helper internals uninspected. |
| Result-to-claim and evidence CLI | `skills/result-to-claim/SKILL.md`, `tools/evidence_check.py` | Direct complete reads: [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-result-judgment](#epi-rte-result-judgment), [EPI-RTE-result-disposition](#epi-rte-result-disposition). |
| Proof acceptance/closure/recovery/wiki mapping | `skills/proof-checker/SKILL.md` | Direct acceptance-gate and Phases 3–5.5 reads: [EPI-RTE-proof-check](#epi-rte-proof-check), [EPI-RTE-proof-disposition](#epi-rte-proof-disposition). Earlier obligation construction and optional formalization unassessed; no comprehensive formal-verification verdict. |
| Wiki claim writes, edges and query pack | `tools/research_wiki.py` | Direct imports, claim rendering/add_claim, add_edge and complete rebuild_query_pack reads; CLI operation names inventoried. [EPI-RTE-wiki-retention](#epi-rte-wiki-retention), [EPI-RTE-query-pack](#epi-rte-query-pack). Paper ingest/experiment-upsert internals and full maintenance not inspected. |
| Capture screen and quarantine | `tools/capture_filter.py`, `tools/threat_scan.py` | Complete capture-filter read; scan/quarantine function reads. [EPI-RTE-wiki-retention](#epi-rte-wiki-retention). Pattern definitions/accuracy not audited; universal capture-filter invocation not established. |
| Wiki context admission into ideation | `skills/idea-creator/SKILL.md` | Read-side gate and landscape opening directly read: [EPI-RTE-query-consumption](#epi-rte-query-consumption). Full generation/selection uninspected. |
| Harness patches and corpus hook | `skills/meta-optimize/SKILL.md`, `skills/meta-apply/SKILL.md`, `templates/claude-hooks/corpus_write_guard.py` | Supplied [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing), [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions). No actual landing/later-use evidence. |
| Other admission and withdrawal operations | `tools/verify_papers.py`, `tools/idea_discovery_gate.py`, `tools/forensics_gate.py`, `tools/verify_paper_audits.sh`, `skills/research-review/SKILL.md` | File/operation inventory only. Bibliographic, submission and unresolved-obligation checks may add local force; not assessed, preventing system-complete negatives about knowledge production, acceptance or withdrawal. |
| Other host variants, patents, installation, updates and monitoring | `skills/`, `tools/`, `aris-monitor/` | Boundary inclusions remain uninspected, not inaccessible. No parity/deployment conclusion; presentation/community exclusions remain unchanged. |

Actual source-linked reviewer inputs/outputs are missing, preventing identification of a particular accepted proposition. Authentic measurements and comparators are missing, preventing empirical warrant and causal improvement attribution. A proof with premises and checked interpretation is missing, preventing a warranted entailed theorem. Host traces are missing, preventing observed disposition/integration/reuse conclusions. These gaps do not establish that behavior never occurs.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-result-claim](#epi-obj-result-claim) | Intended claim, metrics, support/limits and revisions | Empirical candidate | see record | No concrete evaluated instance supplied. |
| [EPI-OBJ-proof-claim](#epi-obj-proof-claim) | Theorem, hypotheses and proof obligations | Mathematical candidate | see record | No warranted premises or completed proof supplied. |
| [EPI-OBJ-wiki-claim](#epi-obj-wiki-claim) | Statement/scope/evidence, symbolic status and graph relations | Retained claim ledger | see record | Status caller-supplied; empirical and proof axes differ. |
| [EPI-OBJ-query-pack](#epi-obj-query-pack) | Excerpts of brief, failures, paper theses and relations | Later ideation context | see record | Full scopes/evidence omitted. |
| [RT-OBJ-run-state](runtime.md#rt-obj-run-state) | Reported completion/acceptance, not research truth | Resume control | see record | Verdict handles/model labels do not attest correctness. |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Method assumptions and non-truth-apt procedural direction | Later host policy | see record | No specific landed update supplied. |

## Authority-route ledger

Record-owned fields say see; architectural status is assessed here. It concerns local implementation or declared procedure, not actual activation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-evidence-check](#epi-rte-evidence-check) | check/evidence production | implemented | [EPI-OBJ-result-claim](#epi-obj-result-claim) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-result-support](#epi-clm-result-support) | occurrence not support | Narrow text-domain deduction. |
| [EPI-RTE-result-judgment](#epi-rte-result-judgment) | check/evidence production | doctrine only | [EPI-OBJ-result-claim](#epi-obj-result-claim) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-result-support](#epi-clm-result-support) | selected evidence | No observed judgment. |
| [EPI-RTE-result-disposition](#epi-rte-result-disposition) | disposition/acceptance | doctrine only | [EPI-OBJ-result-claim](#epi-obj-result-claim) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-result-support](#epi-clm-result-support) | integrity nonblocking | Judgment is distinct from admission. |
| [EPI-RTE-result-integration](#epi-rte-result-integration) | lifecycle integration | doctrine only | [EPI-OBJ-result-claim](#epi-obj-result-claim) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-result-support](#epi-clm-result-support) | partial/no also retained | Only accepted branch is post-acceptance integration. |
| [EPI-RTE-proof-check](#epi-rte-proof-check) | check/evidence production | doctrine only | [EPI-OBJ-proof-claim](#epi-obj-proof-claim) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-proof-verification](#epi-clm-proof-verification) | formal warrant unestablished | No proof certificate supplied. |
| [EPI-RTE-proof-disposition](#epi-rte-proof-disposition) | disposition/acceptance | doctrine only | [EPI-OBJ-proof-claim](#epi-obj-proof-claim) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-proof-verification](#epi-clm-proof-verification) | restatement exception | PASS can coexist with advisory drift. |
| [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) | retention | implemented | [EPI-OBJ-wiki-claim](#epi-obj-wiki-claim) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | storage not acceptance | Clean rendering versus quarantine replacement. |
| [EPI-RTE-query-pack](#epi-rte-query-pack) | content transformation | implemented | [EPI-OBJ-query-pack](#epi-obj-query-pack) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | warrant degraded | Excerpts omit evidence and qualifiers. |
| [EPI-RTE-query-consumption](#epi-rte-query-consumption) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-query-pack](#epi-obj-query-pack) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | no scientific reacceptance | Host-followed read-side guard. |
| [RT-RTE-review-transition](runtime.md#rt-rte-review-transition) | disposition/acceptance | implemented | see route | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | path-specific assurance | Stop permission, not scientific truth. |
| [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume) | operational admission/selection/consumption | implemented | [RT-OBJ-run-state](runtime.md#rt-obj-run-state) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | provisional/skipped advance | Helper does not inspect verdict evidence. |
| [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing) | behavior/policy adaptation | doctrine only | [RT-OBJ-skill](runtime.md#rt-obj-skill) | non-truth-apt policy/content update: skill procedure changes; semantic claims unresolved | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | receipt not correctness | Receipt/hash subpath implemented; landing/later effect unobserved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-result-support](#epi-clm-result-support) | see claim | see claim | see claim | [EPI-RTE-evidence-check](#epi-rte-evidence-check); judgment/disposition procedural | None supplied | No error-rate comparison; selected summaries and baseline validity bound judgment | Evidence-consuming support criterion and intended writing use specified | No particular accepted ampliative claim established. |
| [EPI-CLM-proof-verification](#epi-clm-proof-verification) | see claim | see claim | see claim | [EPI-RTE-wiki-retention](#epi-rte-wiki-retention) stores statuses; checking/disposition procedural | None supplied | Model review is not a supplied formal certificate or source-truth guarantee | Explicit hypotheses, counterexample and scope requirements | Restatement drift may survive PASS; status helper does not enforce honest mapping. |
| [RT-CLM-review-independence](runtime.md#rt-clm-review-independence) | see claim | see claim | see claim | [RT-RTE-codex-call](runtime.md#rt-rte-codex-call) | None supplied | Model/thread difference does not identify causal error reduction | Primary-artifact independence is requested | Result gate explicitly pastes selected numbers/caveats; no universal unfiltered-input invariant. |

## Bounded conclusion

ARIS specifies an evidence-consuming empirical acceptance process, not merely retrieval. Codex judges intended claims against results, baselines and caveats; no/partial/yes directs pivot, revision/new tests or confirmation for writing. The deterministic precheck contributes only occurrence evidence, not measurement authenticity, scientific support or transfer. No observed input/output establishes a produced accepted ampliative claim. See [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-result-judgment](#epi-rte-result-judgment), [EPI-RTE-result-disposition](#epi-rte-result-disposition).

Proof judgment has different targets and criteria: hypotheses, obligations, uniformity, counterexamples and blind rechecking. A gap is not falsity; imports retain conditional status. No supplied proof with warranted premises and checked interpretation establishes an actually derived theorem. A persisted verified label cannot supply that warrant; optional restatement checking remains advisory. See [EPI-RTE-proof-check](#epi-rte-proof-check), [EPI-RTE-proof-disposition](#epi-rte-proof-disposition).

Retention, integration and reliance differ. Helper writes can store caller-selected proof statuses without executing an audit. Empirical support edges do not change the proof axis. Query-pack excerpts omit full evidence/scopes and can be used as banlists/prior-work context after injection scanning rather than scientific reacceptance. Import warrant is unknown; selective pack transport degrades warrant because omitted qualifications cannot be recovered from the pack alone. No complete withdrawal propagation is established in inspected paths. See [EPI-RTE-result-integration](#epi-rte-result-integration), [EPI-RTE-wiki-retention](#epi-rte-wiki-retention), [EPI-RTE-query-pack](#epi-rte-query-pack), [EPI-RTE-query-consumption](#epi-rte-query-consumption).

Local stop/resume and patch controls do not provide a universal oracle. Family assurance is path-specific, provisional/skipped phases can advance recovery and patch receipts do not prove improvement. Distributed-parametric inference is external: [RT-CMP-claude](runtime.md#rt-cmp-claude) and [RT-CMP-codex](runtime.md#rt-cmp-codex) establish neither pinned weights nor observed parameter updates. Harness adaptation supports a human-mediated improvement-directed capacity; learning, exercised reflection, autonomous theory building and successful self-improvement remain independently unestablished within the evidence limits of [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing). The empirical partial-result loop requests claim-directed criticism and iteration but supplies no witnessed criticism/revision/reuse episode. Uninspected literature, forensics and paper paths prevent a system-complete negative.

## Shared records

### Operative objects

#### EPI-OBJ-result-claim
Label: Intended empirical claim and support judgment

Source-native identity: intended claim, collected results and normalized claim_supported fields in /result-to-claim. Natural-language claims/interpretations and symbolic yes/partial/no are distinct consumption surfaces in project result files, findings and claim reports. Distinct from the orchestration container [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline): this standalone gate's claim/evidence bundle is not that route. Source: SRC-1, `skills/result-to-claim/SKILL.md`.

> Experiments produce numbers; this gate decides what those numbers *mean*. Collect results from available sources, get a Codex judgment, then auto-route based on the verdict.
> --- `skills/result-to-claim/SKILL.md`

#### EPI-OBJ-proof-claim
Label: Theorem and proof obligations

Source-native identity: theorem/lemma, hypotheses, proof and obligation ledger in /proof-checker; natural-language/mathematical notation in LaTeX/Markdown files and symbolic JSON audit status. No supplied counterpart denotes this proof-specific object. Source: SRC-1, `skills/proof-checker/SKILL.md`; acceptance passage in [EPI-RTE-proof-check](#epi-rte-proof-check). Scope is theorem under explicit hypotheses, not imported source truth.

#### EPI-OBJ-wiki-claim
Label: Wiki claim page and proof status

Source-native identity: claims/<slug>.md, statement, honest scope and evidence chain; symbolic status and typed graph/edges.jsonl relations. Natural-language body and symbolic metadata on disk have separate consumers. Unlike [RT-OBJ-run-state](runtime.md#rt-obj-run-state), it stores research statements, not phase acceptance. Source: SRC-1, `tools/research_wiki.py`, _render_claim_page/add_claim/add_edge.

> lines.append("## Honest scope")
> --- `tools/research_wiki.py`

> lines.append("## Evidence chain")
> --- `tools/research_wiki.py`

#### EPI-OBJ-query-pack
Label: Compressed wiki context

Source-native identity: research-wiki/query_pack.md, natural-language excerpts and relation identifiers on disk, intended for later idea-creator invocation. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill): accumulated research context, not static procedural text. Source: SRC-1, `tools/research_wiki.py`, rebuild_query_pack; `skills/idea-creator/SKILL.md`. Supporting passages below.

### Routes

#### EPI-RTE-evidence-check
Label: Cited evidence occurrence check

Distinct identity: no supplied counterpart; [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume) checks status labels, not result bytes. Endpoints: value/source/glob and root → readable matching files → numeric/literal matching → JSON status. Owner: Python helper. Domain/target: occurrence in local text, not empirical support or file authenticity. Result is symbolic JSON persisted by caller at .aris/evidence_precheck.json.

- Immediate return: verified, path_missing, value_not_found, or batch unparseable, details and counts; failed checked citations cause CLI nonzero.
- Later read-back: caller persists JSON and supplies selected statuses to later reviewer prompt; unobserved in operation.
- Delegated visibility: per-claim status table; deterministic negatives withheld from relitigation by skill instruction.
- Selection predicate: usable value/source; any readable matching file with matching value suffices.
- Invalidation or expiry: files reread on each check; no hash binding of persisted result established.
- Activation or effect: fixed-rule occurrence result; host consumes negative status in separate disposition route.
- Evidence limits: implementation/caller fully read; no execution or source-measurement validation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction without execution: value 73.2 and readable file text `score = 73.2` produce Decimal 73.2/no-percent; safe boundaries permit token matching; equality yields verified. Text 73.2% does not match that no-percent citation. The newly derived proposition is only that bytes contain the cited value under this matching domain. An unrelated baseline value in the same file can also pass: a source-supported countercase to treating verification as claim support. Non-numeric mixed strings use literal substring matching after source whitespace normalization. Behavioral path: helper JSON → host/current audit and selected jury table; advisory at helper boundary, procedural rejection/permissive checking in the skill. No scientific answer oracle; readable file is only an occurrence reference. Source: SRC-1, `tools/evidence_check.py`, `skills/result-to-claim/SKILL.md`.

> if tnum == dval and bool(m.group(2)) == want_pct:
>                 return True
> --- `tools/evidence_check.py`

> `verified` means only that the cited evidence EXISTS — not that the claim holds.
> --- `tools/evidence_check.py`

#### EPI-RTE-result-judgment
Label: Experimental support jury

Distinct from [RT-RTE-review-transition](runtime.md#rt-rte-review-transition): evaluates empirical support, not loop stopping. Endpoints: intended claim, experiments, metrics, baselines/caveats/precheck → Codex → support, limits, revision and confidence. Host selects evidence; reviewer judges. Target is named claim in tested conditions; open research, no universal expected-answer oracle.

- Immediate return: requested yes/partial/no, supported/unsupported scope, missing evidence, revision, next experiments and confidence.
- Later read-back: findings and later experiments can reach another reviewer invocation.
- Delegated visibility: selected numbers, comparisons and caveats are pasted, not automatically complete primary data.
- Selection predicate: missing-evidence claims terminally rejected; unparseable/ambiguous eligible claims go to jury; unresolved precheck warns/skips rather than blocking jury.
- Invalidation or expiry: new results justify rerun; no clock-only repetition; input snapshot integrity not established.
- Activation or effect: requests evidence-consuming judgment; disposition remains separate.
- Evidence limits: doctrine only; no actual model response/source trace or measured reviewer accuracy.
- design conclusion status: claimed
- operation conclusion status: uninspected

Epistemic license sought is tested-domain support with limitations, not universal generalization. Relation remains indeterminate without inputs/outputs: interpretation/revision might reshape, derive or conjecture; failure to establish entailment does not establish ampliation. Consumer/channel/force/horizon: host parser receives judgment, advisory until disposition in current/later project rounds. Source: SRC-1, `skills/result-to-claim/SKILL.md`.

> [paste key numbers, comparison deltas, significance]
> --- `skills/result-to-claim/SKILL.md`

> A single positive result on one dataset does not support a general claim.
> --- `skills/result-to-claim/SKILL.md:148-158`

#### EPI-RTE-result-disposition
Label: Empirical claim disposition

Distinct from [RT-RTE-review-transition](runtime.md#rt-rte-review-transition): decides research support use, not score-based stopping. Endpoints: precheck/jury → host branch → pivot, revised claim/new experiments or confirmation/writing. Researcher proposes; Codex judges; deterministic missing-evidence screen can reject; host follows branch. No mandatory per-content human approval or general answer oracle.

- Immediate return: no/postmortem, partial/supplement, yes/confirmation; reviewer unavailability requires REVIEW_UNAVAILABLE and stop after allowed fallbacks.
- Later read-back: findings, revised claim and project notes guide later experiments/review.
- Delegated visibility: normalized verdict/why; supportive/ambiguous outcomes without reviewer must not flow downstream.
- Selection predicate: no/partial/yes; low confidence means inconclusive/add experiments; precheck missing evidence can reject without reviewer.
- Invalidation or expiry: new experiments or narrowed claim lead to rejudgment; repeated partial can pivot; product rollback not specified here.
- Activation or effect: host protocol permits pivot, further experiments, ablations or writing; no encompassing executable controller inspected.
- Evidence limits: no observed acceptance; absent integrity audit does not block, integrity failure lowers confidence rather than automatically reversing verdict.
- design conclusion status: claimed
- operation conclusion status: uninspected

Acceptance criterion/intended use/scope: evidence-consuming positive reviewer judgment for the intended empirical claim in tested settings, subject to low-confidence inconclusiveness, for project confirmation/paper preparation. This specifies a process, not an observed accepted ampliative proposition. Behavioral authority: parsed verdict → host branch instruction, permissive/advisory force over current project and later rounds. Rejected material can persist without acceptance. Source: SRC-1, `skills/result-to-claim/SKILL.md`.

> 1. Update the working claim to reflect what IS supported
> 2. Record the gap in findings.md
> 3. Design and run supplementary experiments to fill evidence gaps
> 4. Re-run result-to-claim after supplementary experiments complete
> --- `skills/result-to-claim/SKILL.md`

> verdict is labeled "provisional — no integrity audit run"
>     (this does NOT block anything — pipeline continues normally)
> --- `skills/result-to-claim/SKILL.md`

#### EPI-RTE-result-integration
Label: Empirical verdict integration

Distinct from [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline): connects specific judged results to project/wiki evidence, rather than stage handoffs. Endpoints: judgment/disposition → project notes, optional experiment node → support/invalidation edges, idea outcome and query-pack rebuild. Host owns instruction-following; helpers own selected writes. Yes branch integrates accepted claim with evidence; partial/no retention is a separate nonaccepting branch, not acceptance by storage.

- Immediate return: notes, optional experiment update/edges/outcome edits, or warning/skip on helper failure.
- Later read-back: outcomes/lessons can enter later query packs and ideation.
- Delegated visibility: node has metrics/reasoning/provenance; pack does not retain full audit evidence.
- Selection predicate: active wiki and successful experiment-node birth before edges; yes/partial supports, no invalidates.
- Invalidation or expiry: rejudgment updates experiment and outcome; edge removal/reversal not specified, distinct edge types can coexist.
- Activation or effect: changes evidence connections and future ideation input after judgment, not proof-status promotion.
- Evidence limits: doctrine only; experiment-upsert internals not fully inspected; no observed integration or global withdrawal propagation.
- design conclusion status: claimed
- operation conclusion status: uninspected

Admission inherits result disposition; helper does not independently accept scientific content. Future idea model receives outcome-based pack with advisory/ranking force across project invocations. Localized claim content afforded; content-directed criticism, consumption and iteration requested, not observed. Claims/fields are addressable and notes persist across intended rounds; improved future capacity and exercised reflection are unestablished. This revises external research products, not demonstrated ARIS self-improvement. Source: SRC-1, `skills/result-to-claim/SKILL.md`, `tools/research_wiki.py`.

> This skill never edits a claim's
> `status` field and never creates a claim node
> --- `skills/result-to-claim/SKILL.md:229-233`

#### EPI-RTE-proof-check
Label: Proof closure and independent review

No supplied proof-specific counterpart; unlike [RT-RTE-review-transition](runtime.md#rt-rte-review-transition), checks theorem obligations rather than stop scores. Endpoints: proof/issues → fixes/re-review → global closure/blind severe-fix review/regression → audit judgment. Executor constructs fixes; selected Codex/manual reviewer criticizes. Domain is explicit hypotheses and mathematical statement, not truth of imported literature.

- Immediate return: issues, closure/counterexample findings, or unresolved-proof report after budget.
- Later read-back: same-invocation review uses prior issues; audit/state and optional claim ledger persist results.
- Delegated visibility: follow-up has fixes/prior issues; FATAL/CRITICAL fixes require fresh blind section-only review.
- Selection predicate: all theorem obligations/key lemmas, severe fixes trigger fresh review; optional restatement scan separate.
- Invalidation or expiry: blind-review issues reenter fixes; regression retests downstream lemmas after changes.
- Activation or effect: requested criticism/evidence for proof disposition; not an inspected formal kernel.
- Evidence limits: specified skill ranges only; no actual proof, checked derivation, warranted imports or formal certificate.
- design conclusion status: claimed
- operation conclusion status: uninspected

Semantic relation indeterminate for actual produced content; intended proof does not establish entailment. No fixed answer oracle; model review/counterexample search evaluate an open proof. Guidance is obligation accounting; consumer is executor via reviewer messages, revisory procedural force during current invocation. Theory-builder conditions 1–4 separately: localized statement afforded; semantic consumption, blame-directed criticism/revision and iteration claimed, not observed. Assumptions/parts are inspectable; retention intended across rounds. Learning, exercised reflection and autonomous operation are not inferred. Source: SRC-1, `skills/proof-checker/SKILL.md`.

> The proof passes when ALL of the following hold:
> 1. Zero open FATAL or CRITICAL issues
> 2. Every theorem/lemma has: (i) explicit hypotheses, (ii) proof with all interchanges justified, (iii) every application discharges hypotheses in the ledger
> 3. All big-O/Θ/o statements have declared parameter dependence and uniformity scope
> 4. Counterexample pass executed on all key lemmas (log candidates even if none found)
> --- `skills/proof-checker/SKILL.md`

#### EPI-RTE-proof-disposition
Label: Proof acceptance and status mapping

Distinct from [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume), which records acceptance metadata without proof judgment. Endpoints: reviewed obligations → accept/unrecoverable → audit/state → optional mapped claim status. Executor proposes/fixes, reviewer reopens issues, host records; no mandatory human approval in these passages.

- Immediate return: audit/state and optional claim write; severe unresolved issues require unrecoverable report.
- Later read-back: audit/status/scope available to future project readers; actual use unobserved.
- Delegated visibility: canonical statement, scope, audit/counterexample/obligation pointers and trace path, not a machine-checked certificate.
- Selection predicate: proof gate; PASS/no imports verified, flagged imports sound-modulo-imports, false statement/counterexample refuted, gap unproven.
- Invalidation or expiry: re-audit update-on-exist; salvage by weakened claim, stronger assumptions or restructured proof; no automatic dependency revocation established.
- Activation or effect: procedural acceptance for theorem reliance and scope recording; optional ledger cannot change/block audit verdict.
- Evidence limits: instruction only; advisory restatement drift can coexist with PASS.
- design conclusion status: claimed
- operation conclusion status: uninspected

Acceptance criterion is explicit obligation gate, intended use theory-paper theorem reliance, scope stated hypotheses/import limits. Model acceptance is not infallibility or source truth. Host consumes report through procedural permissive direction; later ledger reader gets advisory status across project invocations. Recovery is revision/re-audit, not automatic rollback. Source: SRC-1, `skills/proof-checker/SKILL.md`.

> Never invent a status: a plain proof gap is `unproven` — never `refuted` (which
> asserts falsity) and never `verified`/`drafted`.
> --- `skills/proof-checker/SKILL.md`

> A paper with non-empty `restatement_drift` may still emit `PASS` if all proof obligations are otherwise discharged; the drift is independent of proof correctness.
> --- `skills/proof-checker/SKILL.md`

#### EPI-RTE-wiki-retention
Label: Claim and edge write paths

Distinct from [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume): stores scientific statements/relations, not phase metadata. Endpoints: caller fields → enum/structure checks and optional quarantine → claim Markdown/edge JSONL → derived context rebuild. Helper owns I/O; caller owns scientific verdict. `verified` is accepted as an enum without executing audit or requiring nonempty provenance.

- Immediate return: page write/update or existing-slug skip; edge duplicate skip; dangling-node warning; invalid claim enum raises.
- Later read-back: claim writes rebuild index/query pack; full page retained for later readers, actual reuse unobserved.
- Delegated visibility: flagged statement/scope/evidence can become placeholders; raw content retained in quarantine.log.
- Selection predicate: initialized claims directory/valid status/slug; update-on-exist overwrites; edge dedup from/to/type ignores changed evidence.
- Invalidation or expiry: caller may overwrite as retracted/refuted; no scientific review or automatic propagation; differing edge types coexist.
- Activation or effect: durable storage of caller assertions, including rejected/provisional content; not evidence-consuming acceptance.
- Evidence limits: claim/edge paths inspected, not all maintenance; threat definitions/accuracy unassessed, import failure allows unscanned writes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Clean rendering is non-ampliative; quarantine replaces propositions with policy placeholders, leaving whole-route semantic preservation indeterminate. Content proposer/decider is caller; helper veto is structural. Future readers receive status/relations via disk, advisory authority across sessions. Complete capture_filter.py read establishes a separate regex CLI rejection screen for operational noise, not its universal invocation by add_claim and not positive correctness. No new scientific warrant from storage. Source: SRC-1, `tools/research_wiki.py`, `tools/threat_scan.py`, `tools/capture_filter.py`.

> if status not in _CLAIM_STATUSES:
>         raise RuntimeError(f"unknown claim status '{status}'. "
>                            f"Valid: {sorted(_CLAIM_STATUSES)}")
> --- `tools/research_wiki.py`

> if not findings:
>         return content, []
> --- `tools/threat_scan.py`

#### EPI-RTE-query-pack
Label: Selective wiki context construction

No supplied extractor counterpart; [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline) describes different summaries. Endpoints: brief/gaps/ideas/papers/graph → selected/truncated sections → query_pack.md. Deterministic helper owns excerpting, not acceptance.

- Immediate return: overwritten pack and character count.
- Later read-back: intended later idea-creator reads accumulated outcomes after scan.
- Delegated visibility: title/thesis and failure excerpts; graph from/type/to only, not edge evidence or full claim scope.
- Selection predicate: recognized brief sections, sliced gaps, negative/mixed frontmatter outcomes, sorted first twelve papers, last twenty edges and character caps.
- Invalidation or expiry: rebuilt on request; seven-day freshness handled by consumer instruction, not scientific reacceptance.
- Activation or effect: constructs future context; threat findings prepend banner rather than blanking pack.
- Evidence limits: complete function inspected, page ingestion lineage partly uninspected; no actual pack/consumer trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete text-transformation deduction: an idea page with outcome negative, title Trial A and a failure heading contributes title plus up to 200 characters from the selected three-line failure/lesson excerpt. Changing only outcome to pending excludes it even if body discusses negative outcomes. Graph projection drops evidence qualifier while preserving from/type/to: this degrades warrant, not necessarily selected text's truth. Paper order is sorted filenames, not implemented semantic relevance ranking despite its comment. Consumer is later idea model via file Read; advisory/ranking horizon across project invocations. Source: SRC-1, `tools/research_wiki.py`.

> if meta.get("outcome") in ("negative", "mixed"):
> --- `tools/research_wiki.py`

> chains.append(f"  {e['from']} --{e['type']}--> {e['to']}")
> --- `tools/research_wiki.py`

#### EPI-RTE-query-consumption
Label: Scan-gated ideation reliance

Distinct from [RT-RTE-codex-call](runtime.md#rt-rte-codex-call): retained wiki context admission, not reviewer transport. Endpoints: cached/rebuilt raw pack → strict scan → immediate Read or skip → ideation. Host follows embedded Bash guard; scanner decides syntactic admission, not scientific acceptance.

- Immediate return: clean/blocked-or-error/scanner-unavailable; clean permits immediate Read, failure skips context while ideation continues.
- Later read-back: accumulated outcomes reach later ideation when scan succeeds; activation unobserved.
- Delegated visibility: raw selected pack, not full source nodes; rejected pack remains on disk but must not be read in this invocation.
- Selection predicate: cached pack younger than seven days or one rebuild, successful scan immediately before Read.
- Invalidation or expiry: stale/missing rebuild once if helper exists; scanner missing/error/hit skips all wiki context.
- Activation or effect: assigns gaps search-seed, failed ideas banlist and papers known-prior-work roles.
- Evidence limits: guard source inspected; deployment/compliance unobserved; scan cleanliness is not scientific warrant.
- design conclusion status: claimed
- operation conclusion status: uninspected

No fresh evidence-consuming acceptance. Behavioral path: future idea model receives file context, directive banlist/advisory ranking force over current ranking and later project invocations. Prior producers propose retained content; scanner can veto delivery, not primary ideation. Human per-content admission unresolved. Source: SRC-1, `skills/idea-creator/SKILL.md`.

> Treat its gaps as search seeds, failed ideas
>    as a banlist, and top papers as known prior work; still run Phase 1 for the
>    last 3–6 months.
> --- `skills/idea-creator/SKILL.md`

### Claims

#### EPI-CLM-result-support
Label: Experimental support assessment

Claimed operation: external reviewer judges whether results support intended claims and directs next action. Source: SRC-1, `skills/result-to-claim/SKILL.md`, doctrine/design; minimum passage in [EPI-OBJ-result-claim](#epi-obj-result-claim). Distinct from [RT-CLM-review-independence](runtime.md#rt-clm-review-independence): support evaluation, not input independence. Criterion and intended use described by result routes, no observed accepted proposition.

#### EPI-CLM-proof-verification
Label: Mathematical proof verification

Claimed operation: adversarial proof checking, fixing and repeated review with obligation accounting. Source: SRC-1, `skills/proof-checker/SKILL.md`, doctrine/design. Distinct from [RT-CLM-review-independence](runtime.md#rt-clm-review-independence): mathematical correctness claim, not general reviewer separation.

> Systematically verify a mathematical proof via cross-model adversarial review, fix identified gaps, re-review until convergence, and generate a detailed audit report with proof-obligation accounting.
> --- `skills/proof-checker/SKILL.md`
