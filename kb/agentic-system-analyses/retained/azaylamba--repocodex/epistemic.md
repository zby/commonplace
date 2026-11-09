---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "RepoCodex epistemic routes: imported and agent-authored explanations, mechanical attestation, semantic review and consequential consumers."
run-id: AAS-2026-11-08-repocodex-bf22ac3623d8-01
reviewed-boundary: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
---

# RepoCodex epistemic report

## Source-and-claim boundary

The question is whether RepoCodex's stored explanations acquire warrant through its pin checks and review loop, and what those results actually authorize. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and layers are in its [Source register](boundary.md#source-register). All source-dependent findings below use SRC-1 at the frozen revision. The checkout HEAD matched that revision and status was clean. Nothing here is a target execution result.

Assessed families: explanation import and authoring, anchor and literal checking, command admission, retrieval/ranking, diagnostic impact, semantic review requests, repair, supersession and retirement. External model internals, actual host compliance and consuming deployments remain outside the available implementation. No supplied execution trace establishes an actual candidate's generation, semantic evaluation, acceptance or later behavioral activation. No causal comparison establishes prevention of regressions. These missing layers prevent claims about exercised knowledge production and benefit, not reconstruction of implemented checks. Model state and mutability limits remain local to [RT-CMP-coding-agent](runtime.md#rt-cmp-coding-agent).

Knowledge/warrant claims: [RT-CLM-executable-memory](runtime.md#rt-clm-executable-memory), [EPI-CLM-pin-match](#epi-clm-pin-match), and [EPI-CLM-loop-protection](#epi-clm-loop-protection). No single claim licenses a system-wide epistemic verdict.

### Coverage

“Direct” means this analyst read the source; “supplied” means reliance on the runtime record and its retained passage. Source paths in this table are SRC-1 implementation except Markdown skills and product documentation, which are doctrine/design. Supporting internals not directly inspected are not access failures. This is material-route coverage, not an exhaustive correctness audit.

| Entry point or operation | Source path | Coverage records and inspection basis | Remaining limit |
| --- | --- | --- | --- |
| CLI dispatch, including apply-patches, bootstrap, audit, advisory and repair | `src/repocodex/cli.py` | Direct; [RT-CMP-command-engine](runtime.md#rt-cmp-command-engine) | No command execution |
| All six registered MCP tools | `src/repocodex/mcp_server.py` | Direct; [RT-RTE-context-read](runtime.md#rt-rte-context-read), [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-validate-change](runtime.md#rt-rte-validate-change), [EPI-RTE-impact-read](#epi-rte-impact-read) | Host handling of returned dictionaries unobserved |
| Author/read/edit/revalidate procedure | `src/repocodex/data/skills/repocodex-coding/SKILL.md` | Direct; [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop) | Requests do not prove compliance |
| Semantic PR review and advisory wrapper | `src/repocodex/data/skills/repocodex-review/SKILL.md`, `src/repocodex/commands/advisory.py` | Direct; [EPI-RTE-semantic-review](#epi-rte-semantic-review), [RT-RTE-review-audit](runtime.md#rt-rte-review-audit) | CLI supplies no semantic judgments |
| Write, gate, matching and claim owner resolution | `src/repocodex/commands/write.py`, `src/repocodex/engine/gate.py`, `src/repocodex/engine/match.py` | Direct; [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [EPI-RTE-claim-check](#epi-rte-claim-check) | Mechanical attachment is not narrative validation |
| Validation, contradictions, dilution, liveness and relocation candidate search | `src/repocodex/commands/validate.py`, `src/repocodex/engine/contradiction.py`, `src/repocodex/engine/dilution.py`, `src/repocodex/engine/liveness.py`, `src/repocodex/engine/relocate.py` | Direct; [RT-RTE-validate-change](runtime.md#rt-rte-validate-change), [EPI-RTE-relocation-check](#epi-rte-relocation-check), [EPI-RTE-claim-check](#epi-rte-claim-check) | Ratchet and index synchronization helper correctness supplied, not independently audited |
| Bootstrap source mining | `src/repocodex/commands/bootstrap.py` | Direct; [EPI-RTE-bootstrap-import](#epi-rte-bootstrap-import), [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts) | Evidencing commit need not be origin of the explanation |
| Retrieval, store, links and impact | `src/repocodex/retrieval.py`, `src/repocodex/store/bundle.py`, `src/repocodex/engine/impact.py` | Direct; [RT-RTE-context-read](runtime.md#rt-rte-context-read), [EPI-RTE-impact-read](#epi-rte-impact-read) | Reverse-index implementation supplied; semantic relevance and completeness unestablished |
| Reconcile patch and identity relocation | `src/repocodex/commands/reconcile.py`, `src/repocodex/commands/relocate.py` | Direct patch source; supplied relocation [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch), [RT-RTE-relocate-identity](runtime.md#rt-rte-relocate-identity) | No universal gate or atomic rollback |
| Audit screening, findings import and GC | `src/repocodex/commands/audit.py` | Direct; [RT-RTE-review-audit](runtime.md#rt-rte-review-audit), [EPI-RTE-audit-gc](#epi-rte-audit-gc) | Out-of-band reviewer operation unavailable |
| Hook, required Action and advisory Action | `src/repocodex/data/hooks/pre-commit`, `src/repocodex/data/action/repocodex.yml` | Direct; [RT-BAP-check-enforcement](runtime.md#rt-bap-check-enforcement) | Actual installation and branch protection unobserved |
| Installer, external repair driver and plugin adapters | `src/repocodex/commands/install.py`, `src/repocodex/commands/repair.py`, `src/repocodex/data/plugin/hooks/claude-pre-commit`, `src/repocodex/data/plugin/hooks/cursor-pre-commit` | Supplied; [RT-RTE-install-wiring](runtime.md#rt-rte-install-wiring), [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair) | Host policy/provider and child-produced repairs uninspected |
| Product warrant and benefit assertions | `README.md`, `docs/architecture.md` | Direct doctrine/design; [EPI-CLM-pin-match](#epi-clm-pin-match), [EPI-CLM-loop-protection](#epi-clm-loop-protection) | No run or causal layer |

The direct reads include additional internals under the already registered Git source, not a new evidence boundary. Source-defined tests and contributor workflows are covered by the boundary, not taken here as successful evaluations. Uninspected supporting helpers and external interpretation prevent an exhaustive negative about every possible acceptance process. The narrower negative below concerns automatic semantic acceptance in the inspected command consumers.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) | Explanations of constructs, constraints and cross-package flows; directives themselves need not be truth-apt | See record | SRC-1; see record | Agent-authored meaning/update relation is indeterminate without a candidate and premises; no retained production instance supplied |
| [EPI-OBJ-bootstrap-body](#epi-obj-bootstrap-body) | Existing comment or commit-subject explanation copied into a draft | See record | SRC-1 `src/repocodex/commands/bootstrap.py` | Imported, not a newly inferred explanation; provenance is narrower than proof of authorship or truth |
| [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | Paths, status, sources, anchors and frozen literals; a literal's declared subject can denote a contract proposition | See record | SRC-1; see record | Symbolic selectors and token checks do not verify the prose's causal account |
| [RT-OBJ-coding-skill](runtime.md#rt-obj-coding-skill) | Mostly behavioral instructions, with operational assumptions about types, checks and workflow | See record | SRC-1; see record | Natural-language host interpretation, not engine-executed proof obligations |
| [RT-CMP-coding-agent](runtime.md#rt-cmp-coding-agent) | Not determinable within distributed parameters; externally produced prose may be truth-apt | See record | SRC-1; see record | Exact version, parameter updates and provider state not inspectable here |

## Authority-route ledger

Fields owned by a cited record are referenced with “see”; the classifications and epistemic licenses below are this report's assessments. One container route can appear in separate rows for its distinct functions. “Implemented” for a model-facing route means the delivery/request is wired, not that the requested judgment occurred. All possible results are source deductions, not observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop) | content transformation | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) | truth-apt transformation: indeterminate | Agent produces explanation/update | See route | See route | Proposed prose; no observed instance | See route | Candidate generation; semantic preservation, entailment and novelty unresolved | See route | See [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | SRC-1; see route | [EPI-CLM-loop-protection](#epi-clm-loop-protection) | none | Failure to establish entailment is not evidence of ampliation |
| [EPI-RTE-bootstrap-import](#epi-rte-bootstrap-import) | content transformation | implemented | [EPI-OBJ-bootstrap-body](#epi-obj-bootstrap-body) | truth-apt transformation: acquisition/import | Existing comment/subject becomes draft body | See route | See route | Copied note with wrapper | See route | Source warrant unknown; copied assertion, not checked explanation | See route | See route | SRC-1 `src/repocodex/commands/bootstrap.py` | none | none | File-touch commit is not necessarily originating evidence |
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | check/evidence production | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | no content change | Anchor locality/distinctiveness, claim literals, type/prefix and revision metadata | See route; gate's local text domain | See route | Gate result and tighten reasons | See route | Evidence of attachment under implemented matcher/configuration; not explanation truth | See route | See route | SRC-1 `src/repocodex/engine/gate.py`; see route | [EPI-CLM-pin-match](#epi-clm-pin-match) | anchorless exception | Gate does not consume narrative semantics |
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | disposition/acceptance | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | no content change | Command admission of supplied concept | See route | See route | Accepted or rejected envelope | See route | Acceptance for storage/attachment, not an evidence-consuming decision that an ampliative explanation is true | See route | See route | SRC-1; see route | [RT-CLM-executable-memory](runtime.md#rt-clm-executable-memory) | all-writes guarantee unsupported | Anchorless branch accepts without anchor evaluator; bootstrap and patch paths differ |
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts) | retention | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [EPI-OBJ-bootstrap-body](#epi-obj-bootstrap-body) | no content change | Store serialized candidate and lookup material | See routes | See routes | Files, catalogs/logs and generated index | See routes | Retention alone supplies no additional warrant | See routes | See [RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption) | SRC-1 `src/repocodex/store/bundle.py`; see routes | [RT-CLM-executable-memory](runtime.md#rt-clm-executable-memory) | none | Not classified as lifecycle integration of accepted knowledge |
| [RT-RTE-context-read](runtime.md#rt-rte-context-read) | operational admission/selection/consumption | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | truth-apt transformation: non-ampliative reshaping | Select/order stored bodies and related titles | See route | See route | Body JSON or direct identity read | See route | Sources/verified/status/churn affect ranking, not truth adjudication | See route | See [RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption) | SRC-1 `src/repocodex/retrieval.py`; see route | [EPI-CLM-loop-protection](#epi-clm-loop-protection) | freshness is not endorsement | Related titles are not complete bodies; direct read can expose deprecated material |
| [RT-RTE-validate-change](runtime.md#rt-rte-validate-change) | check/evidence production | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | truth-apt transformation: entailed derivation | Counts/regions imply LIVE, WEAK or miss under code-defined predicates; contradiction and maintenance diagnostics | See route | See route | Symbolic classifications and diagnostics | See route | Derived properties of parsed metadata/text/diff, not program correctness or explanation validity | See route | See route | SRC-1 `src/repocodex/engine/liveness.py`, `src/repocodex/engine/contradiction.py`; see route | [EPI-CLM-pin-match](#epi-clm-pin-match) | none | No warranted natural-language premise set supplied; derivation license is only the matcher domain |
| [EPI-RTE-claim-check](#epi-rte-claim-check) | check/evidence production | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | truth-apt transformation: entailed derivation | Frozen literal absent from owning region | See route | See route | CLAIM_BROKEN even if anchor LIVE | See route | Token absence in selected region; not proof that behavior violated a contract | See route | See route | SRC-1 `src/repocodex/engine/liveness.py` | [EPI-CLM-pin-match](#epi-clm-pin-match) | none | Subject semantics and causal role of token remain unchecked |
| [EPI-RTE-relocation-check](#epi-rte-relocation-check) | check/evidence production | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | truth-apt transformation: entailed derivation | Missed pin has relocation candidate | See route | See route | REANCHOR patch or DRIFT candidates | See route | Algorithmic candidate, not semantic continuity of explanation | See route | See route | SRC-1 `src/repocodex/engine/relocate.py` | [EPI-CLM-pin-match](#epi-clm-pin-match) | rename partial-match case | Rename path accepts any region; search path requires all terms |
| [RT-RTE-validate-change](runtime.md#rt-rte-validate-change) | disposition/acceptance | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | no content change | Whether change blocks in configured caller/posture | See route | See route | Blocking true/false; possible acknowledged exemption | See route | Permission to continue is not endorsement of explanation or repair | See route | See [RT-BAP-check-enforcement](runtime.md#rt-bap-check-enforcement) | SRC-1; see route | [EPI-CLM-loop-protection](#epi-clm-loop-protection) | default shadow and override limits | Plain CLI/MCP do not deny solely by returning a blocking verdict |
| [EPI-RTE-impact-read](#epi-rte-impact-read) | operational admission/selection/consumption | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter), [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) | truth-apt transformation: non-ampliative reshaping | Changed files mapped through stored links/pins | See route | See route | Advisory impacted identities | See route | Potential relevance by registered edges, not completeness or regression prediction | See route | See route | SRC-1 `src/repocodex/mcp_server.py`, `src/repocodex/engine/impact.py` | none | none | No recursive causal code graph follows |
| [EPI-RTE-semantic-review](#epi-rte-semantic-review) | check/evidence production | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) | truth-apt transformation: indeterminate | New narrative versus originating diff; weakening/duplicate why | See route | See route | Requested advisory judgment; CLI categories not_evaluated unless supplied | See route | Comparison request could expose defects; no observed judgment or acceptance warrant | See route | See route | SRC-1 `src/repocodex/data/skills/repocodex-review/SKILL.md` | [EPI-CLM-loop-protection](#epi-clm-loop-protection) | advisory Action is not agent review | Uninspected model inference cannot be classified as absent or reliable |
| [RT-RTE-review-audit](runtime.md#rt-rte-review-audit) | check/evidence production | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | truth-apt transformation: non-ampliative reshaping | Audit sample/body-region screening and imported findings | See route | See route | Screening payload and contradiction proposals | See route | Review inputs/proposals, not accepted semantic corrections | See route | See route | SRC-1 `src/repocodex/commands/audit.py`; see route | none | none | Imported judgments are not authenticated or automatically applied |
| [EPI-RTE-audit-gc](#epi-rte-audit-gc) | disposition/acceptance | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | non-truth-apt policy/content update: deprecated status | Orphan/no-hit or expired draft retirement | See route | See route | Deprecated status persists | See route | Withdrawal from default selection, not refutation of content | See route | See route | SRC-1 `src/repocodex/commands/audit.py` | none | none | Partial anchor hit can prevent orphan retirement; direct reads remain possible |
| [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | disposition/acceptance | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | non-truth-apt policy/content update: superseded predecessor deprecated | Supplied supersedes/rationale retires predecessor | See route | See route | Predecessor can be deprecated before replacement rejection | See route | Author's revision relationship, not validated criticism or truth decision | See route | See [RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption) | SRC-1; see route | none | nontransactional withdrawal | Stable-body comparison enforces revision metadata, not correctness of rationale |
| [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch), [RT-RTE-relocate-identity](runtime.md#rt-rte-relocate-identity) | lineage/freshness/recovery | implemented | [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter), [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body) | non-truth-apt policy/content update: path/term/address mutation | Apply replacement pin or move identity | See routes | See routes | Changed anchor/index or identical body at new identity | See routes | No new semantic warrant; body-preserving identity move differs from changed evidence pointer | See routes | See routes | SRC-1; see routes | [EPI-CLM-pin-match](#epi-clm-pin-match) | patch admission is separate | Caller JSON need not be an emitted checked patch |
| [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair) | behavior/policy adaptation | implemented | [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) | truth-apt transformation: indeterminate | Invoke repair harness after validation | See route | See route | Process outcome, not certified repaired state | See route | No acceptance license from zero process exit | See route | See route | SRC-1; see route | [EPI-CLM-loop-protection](#epi-clm-loop-protection) | no post-child validation | No actual durable child update supplied |
| [RT-RTE-install-wiring](runtime.md#rt-rte-install-wiring) | behavior/policy adaptation | implemented | [RT-OBJ-coding-skill](runtime.md#rt-obj-coding-skill) | non-truth-apt policy/content update: install rules, skills and controls | Setup/upgrade behavior-shaping files | See route | See route | Installed machinery | See route | No content-validation license from copying instructions | See route | See [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption), [RT-BAP-check-enforcement](runtime.md#rt-bap-check-enforcement) | SRC-1; see route | none | none | Not an evidence-fed method-improvement loop |

No automatic **lifecycle integration after semantic acceptance** was found in the inspected write, bootstrap, audit, advisory, validate, retrieval and reconcile consumers. The concrete positive is indexing, linkage, retention and operational use of mechanically admitted content, as recorded above. The semantic-review protocol is a counterexample to “no semantic checking is requested”; it is not an implemented acceptance-and-integration protocol. Opaque host decisions could add one, so no system-complete negative is inferred.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-executable-memory](runtime.md#rt-clm-executable-memory) | See record | SRC-1; see record; doctrine/design | See record | [RT-RTE-context-read](runtime.md#rt-rte-context-read), [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-validate-change](runtime.md#rt-rte-validate-change), [EPI-RTE-impact-read](#epi-rte-impact-read) | None supplied | No intervention/comparison | Executable routes attach and serve explanations and diagnose metadata/text relations | “Executable” does not make explanation semantics executable |
| [EPI-CLM-pin-match](#epi-clm-pin-match) | See record | SRC-1 `README.md`, `docs/architecture.md`; doctrine/design | See record | [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [EPI-RTE-claim-check](#epi-rte-claim-check), [EPI-RTE-relocation-check](#epi-rte-relocation-check) | None supplied | Mechanical predicates only; no source-truth or encoding-fidelity evaluation | Attachment check supported in the checked branch/domain | Unqualified “proves it still matches” exceeds semantic license; anchorless admission and relocation qualify universality |
| [EPI-CLM-loop-protection](#epi-clm-loop-protection) | See record | SRC-1 `README.md`; doctrine/design | See record | [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop), [RT-RTE-validate-change](runtime.md#rt-rte-validate-change), [EPI-RTE-semantic-review](#epi-rte-semantic-review), [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair) | None supplied | No regression comparison; host compliance and branch protection external | Shipped workflow requests preservation and can deny selected mechanical defects | General why/code divergence can survive token presence; default shadow and exemptions qualify denial |

## Bounded conclusion

RepoCodex retains explanations and metadata in repository Markdown and serves selected bodies to later coding agents. This establishes a persistent behavioral-authority opportunity, not demonstrated reliance or benefit: see [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-context-read](runtime.md#rt-rte-context-read) and [RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption). Retrieval reshapes existing content. Sources and verified/status/churn signals reorder it but do not authenticate its claims. Direct identity reads and default filtered retrieval grant different visibility.

Bootstrap **acquires** existing explanations. Its commit pointer and extraction retain a route back to a file/history entry, but source warrant is unknown; the latest file-touch commit is not proof of the note's origin or truth. It does not produce an accepted ampliative explanation merely by wrapping a note as a TechnicalDecision: see [EPI-RTE-bootstrap-import](#epi-rte-bootstrap-import). Agent authoring and repair can produce truth-apt prose, but without concrete candidate inputs/outputs this report cannot decide whether any particular update is reshaping, entailed derivation or ampliative conjecture. No accepted ampliative candidate instance is evidenced.

The code derives narrow diagnostic propositions from parsed symbolic input and current file text: term/region matches, literal absence, shared-subject literal inequality, competing supersession and graph-based potential impact. These are source-code deductions, not independently warranted conclusions about causal explanations or program behavior. In particular, [EPI-RTE-claim-check](#epi-rte-claim-check) can reject a frozen literal while the anchor stays LIVE, and [EPI-RTE-relocation-check](#epi-rte-relocation-check) admits a rename candidate on weaker evidence than its search alternative. Those cases defeat treating all LIVE/REANCHOR results as equivalent evidence of complete semantic attachment.

Material admission criteria are mechanical suitability for stored attachment, configured change-maintenance compliance and deterministic retirement, not an automatic semantic truth decision. Their actual authority is storage permission, selection/ranking, deprecated-status withdrawal or conditional hook/check denial. Acceptance for those uses is real but scoped; it does not establish acceptance of an explanation as knowledge. Checks, admission and retention remain separate functions. [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) can withdraw a predecessor before rejecting its replacement. [EPI-RTE-audit-gc](#epi-rte-audit-gc) withdraws unlinked/no-hit concepts or expired drafts without refuting their meaning. There is no implemented automatic semantic acceptance followed by lifecycle integration in the inspected consumers; a host could perform additional decisions outside this evidence.

Semantic criticism is explicitly requested against the originating diff, not absent by design. Its force is advisory, and audit imports proposals rather than automatically correcting bodies. The shipped advisory Action does not execute that agent judgment: see [EPI-RTE-semantic-review](#epi-rte-semantic-review) and [RT-RTE-review-audit](runtime.md#rt-rte-review-audit). No accepted criticism/revision sequence is observed. Consequently these routes do not independently establish learning, theory-builder criticism/iteration or reliable autonomous acceptance. Retained explanations could express theories, but no actual formulated theory and its use/criticism is supplied; the opaque model is not evidence for or against those conditions.

Installation directly changes later behavior-shaping instructions and check machinery; it is not a trace-fed update or evidence-responsive self-improvement demonstration. Model parameter adaptation remains uninspected. Repair's process success does not close the causal chain to repaired state or later improved behavior. Preservation, reflection, learning, autonomy and self-improvement therefore cannot be bundled into one result. The supported conclusions are the separate implemented routes and bounded licenses above, with operation, acceptance instances and causal benefit still unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-bootstrap-body
Label: Bootstrap note body

Part of: [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body)

The material subset generated by the deterministic bootstrap producer, rather than externally authored concepts in general. Natural-language copied explanation plus a file-path wrapper, serialized as Markdown under a discovered `.context` shard. Different provenance and draft filtering distinguish this part; [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter) separately covers its symbolic metadata. SRC-1 implementation: `src/repocodex/commands/bootstrap.py`. No actual generated instance supplied.

> body=f"Bootstrapped from `{rel}`.\n\n{note}\n",
> --- `src/repocodex/commands/bootstrap.py`

### Routes

#### EPI-RTE-bootstrap-import
Label: Bootstrap note import

Part of: [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts)

The extraction/transformation part, separate from the parent's gate and persistence. Code owns tracked-file/comment and history-subject selection, then constructs [EPI-OBJ-bootstrap-body](#epi-obj-bootstrap-body). No model inference or per-item human judgment occurs here. Caller starts an open mining pass; code proposes the extracted note; the subsequent gate can reject. No semantic reference answer. SRC-1 implementation: `src/repocodex/commands/bootstrap.py`.

Concrete deduction, without execution: a tracked `a.py` containing `# why: preserve stable ordering` yields note `preserve stable ordering` and terms `preserve`, `stable`, `ordering`; `_commit_for` asks for the latest commit touching `a.py`. With a nonempty commit result, the body becomes `Bootstrapped from ` followed by the backticked path, a blank line and the unchanged note. The later gate determines whether it persists. This is import with non-ampliative wrapping, not production of the explanation or acceptance of its truth. The history branch similarly copies an existing subject and associates the first changed path. A latest-touch commit pointer can be less specific than note provenance.

- Immediate return: Candidate tuples, then a draft document for the gate; outer command returns kept/rejected identities.
- Later read-back: Only after the parent's persistence step; drafts require draft-enabled context or direct read.
- Delegated visibility: No internal model; external reader may receive stored draft later.
- Selection predicate: Supported suffixes and why-patterns, first three sufficiently long identifier words; history last 100 subjects matching selected phrases; source commit required before admission.
- Invalidation or expiry: Parent sets stale_after and draft status; audit later applies expiry.
- Activation or effect: Supplies a copied note for possible retention, not demonstrated behavior change.
- Evidence limits: No actual source-note instance or operation supplied; copying preserves wording but does not warrant the source assertion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> note = match.group(1).strip()
> terms = [part for part in re.findall(r"[A-Za-z_][A-Za-z0-9_]{3,}", note)][:3]
> if terms:
>     found.append((rel, note, terms, _commit_for(repo, rel)))
> --- `src/repocodex/commands/bootstrap.py:64-67`

> result = run_git(["log", "-n", "1", "--pretty=%H", "--", rel], cwd=repo)
> sha = result.stdout.strip()
> return sha or None
> --- `src/repocodex/commands/bootstrap.py`

#### EPI-RTE-claim-check
Label: Owning-region literal check

Part of: [RT-RTE-validate-change](runtime.md#rt-rte-validate-change)

The `evaluate_claims` diagnostic part of validation; unlike admission in [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), it rechecks already stable claims at use/maintenance time. Code owns evaluation. Target/domain: a declared literal's token presence in the best matched region of its resolved owning anchor, not the proposition named by the subject or behavior of the software. Missing/ambiguous owner, missing file, absent region or literal produces a finding. No human/model decides the diagnostic, and no semantic answer oracle is supplied. The parent validator owns blocking disposition, with caller posture/exemption veto of its force. SRC-1 implementation: `src/repocodex/engine/liveness.py`, `src/repocodex/engine/match.py`, `src/repocodex/commands/validate.py`.

Concrete counterexample to anchor sufficiency: source text `ENTERPRISE grace = 4` with anchor terms `ENTERPRISE`, `grace`, `= 3`, min_match 2 has two hits and therefore LIVE. A claim with literal `3` and that sole owning anchor fails `literal_as_token` in the best region and yields CLAIM_BROKEN. This deduction assumes a stable loaded concept and selection for validation; it is not a test run. Conversely, keeping all three anchor terms while changing surrounding behavior need not break either check. Token presence does not validate a causal account.

- Immediate return: ClaimFinding objects converted to claim_findings JSON by validator.
- Later read-back: inapplicable — this evaluator writes no retained claim or approval; the parent may append diagnostic metrics.
- Delegated visibility: Findings reach CLI/MCP caller and configured hook/Action through parent envelope.
- Selection predicate: Stable documents with claims selected by parent validation; owner resolution then selects one anchor.
- Invalidation or expiry: Recomputed against current pinned file; no cached semantic approval.
- Activation or effect: Findings add claim_broken to parent's potential blocking reasons; hook/check denial depends on posture and exemption.
- Evidence limits: Working-tree token/region evidence only; no execution of contract behavior or semantic truth check.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if doc.status != ConceptStatus.stable or not doc.frontmatter.claims:
>     return []
> --- `src/repocodex/engine/liveness.py`

> region_text = matched.best.source(text.splitlines()) if matched.best else None
> if region_text is None or not literal_as_token(claim.literal, region_text):
> --- `src/repocodex/engine/liveness.py`

> if hits >= required:
> --- `src/repocodex/engine/liveness.py`

#### EPI-RTE-relocation-check
Label: Relocation candidate check

Part of: [RT-RTE-validate-change](runtime.md#rt-rte-validate-change)

This is candidate generation/checking for a missed anchor, not application of a patch; [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch) owns the latter distinct function. Code owns next-step selection. Domain: current text matches at a Git rename target, or all-term regions in searched files/history-derived paths. Parent liveness consumes `unique` to emit REANCHOR; otherwise DRIFT. The caller can withhold applying the patch; there is no per-candidate human approval inside the check. Local source text is comparison evidence, not a semantic expected answer. Maintenance mode, triggered only after zero pinned-path term hits. SRC-1 implementation: `src/repocodex/engine/relocate.py`, `src/repocodex/engine/liveness.py`.

Counterexample to a universal full-term reanchor check: anchor `all_of=["alpha", "beta"]` fully misses its old path; Git reports that path renamed to one containing only `alpha`. `evaluate_file` produces a nonempty region, so the rename branch returns unique even without `beta`. Liveness then emits a replacement-path patch. The search branch instead requires every term in a region. This source deduction qualifies the meaning of REANCHOR without contradicting runtime's narrower account that a unique candidate is returned. No supplied runtime record needs supersession; the strengthened full-match reading is not asserted there.

- Immediate return: Relocation(unique, via, candidates), then parent patch/classification.
- Later read-back: inapplicable — checking alone persists no anchor; applied patches later feed validation/retrieval through the separate patch route.
- Delegated visibility: Candidate paths and patch delivered to caller, not an internal model evaluator.
- Selection predicate: Git rename first; otherwise least-frequent-term search and full-term regions, then history-derived path fallback.
- Invalidation or expiry: Current calculation; no enduring proof of semantic continuity.
- Activation or effect: Can change DRIFT to REANCHOR and offer caller a repair; does not mutate concept itself.
- Evidence limits: Rename requires only a nonempty region; uniqueness is algorithmic, not independent identity or explanation verification.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> matched = evaluate_file(relocated, config.root, default_scope=config.scope_lines)
> if matched.regions:
>     return Relocation(
>         unique=True,
>         via="rename",
>         candidates=[{"path": new_path, "via": "git diff -M", "terms": list(anchor.all_of)}],
>     )
> --- `src/repocodex/engine/relocate.py`

> if any(len(region.terms_hit) >= len(anchor.all_of) for region in matched.regions):
>     candidates.append({"path": rel, "via": f"pickaxe:{term}", "terms": list(anchor.all_of)})
> --- `src/repocodex/engine/relocate.py`

#### EPI-RTE-semantic-review
Label: New-concept prose review

Part of: [RT-RTE-review-audit](runtime.md#rt-rte-review-audit)

The semantic comparison request is separate from deterministic screening, imported-findings packaging and GC. Producer/evaluator: external review agent interpreting the shipped review skill. Target/domain: new concept narrative versus originating PR diff, plus requested weakening and duplication review. No reference correct answer is supplied. The reviewer proposes findings, not automatic concept edits; coding author/caller must decide a revision and route it through write or other allowed machinery. Human contribution and approval policy remain external. The Action invokes the advisory command without agent judgments, so its output alone establishes no semantic review. SRC-1 doctrine/design: `src/repocodex/data/skills/repocodex-review/SKILL.md`; implementation: `src/repocodex/commands/advisory.py`, `src/repocodex/cli.py`, `src/repocodex/data/action/repocodex.yml`.

- Immediate return: Requested advisory findings; command wrapper marks missing categories not_evaluated and supplied categories evaluated.
- Later read-back: inapplicable — no automatic retained semantic correction or acceptance record in this request/wrapper; host could retain one externally.
- Delegated visibility: Agent must have originating diff and new concept bodies; delivery/compliance is unobserved. CLI itself does not call the reviewer.
- Selection predicate: Every PR/new concepts under skill; caller-provided judgments by category in Python advisory API.
- Invalidation or expiry: Per-diff comparison request; no durable semantic certificate.
- Activation or effect: Advisory to reviewer/coding host, never itself fails required verdict; host response unobserved.
- Evidence limits: Implemented skill delivery and envelope support only; actual judgment, validity, criticism-induced revision and acceptance unobserved.
- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> **New concepts:** while the originating diff is in context, verify each new `.context/**/*.md` body's narrative against the diff. Flag mismatches as advisory findings.
> --- `src/repocodex/data/skills/repocodex-review/SKILL.md`

> Findings from this skill post to the **advisory** check only. Never fail the required deterministic check.
> --- `src/repocodex/data/skills/repocodex-review/SKILL.md`

#### EPI-RTE-audit-gc
Label: Audit deterministic retirement

Part of: [RT-RTE-review-audit](runtime.md#rt-rte-review-audit)

The GC disposition differs from its parent's advisory semantic review. Code loads all concepts, builds inbound-link identities and checks whether any anchor has any term hit; it deprecates if orphaned without a hit, or if draft stale_after is past. `deprecate_concept` persists status/log; ordinary retrieval suppresses deprecated selections but direct MCP reads do not. Trigger: audit/GC invocation, not semantic criticism. Code proposes and admits retirement without per-item human approval or semantic answer oracle. Caller can avoid invoking, restore repository files or revise later; no automatic rollback. SRC-1 implementation: `src/repocodex/commands/audit.py`, `src/repocodex/store/bundle.py`, `src/repocodex/retrieval.py`, `src/repocodex/mcp_server.py`.

- Immediate return: Retired identities in gc_deprecated.
- Later read-back: Persisted deprecated status changes default path retrieval across invocations; direct identity read can still expose body.
- Delegated visibility: Caller receives retirement list; no model judges or authorizes retirement internally.
- Selection predicate: Every loaded concept, not merely stable sample; no inbound links and no partial anchor hit, or expired draft.
- Invalidation or expiry: Date expiry applies to drafts; any partial hit defeats orphan criterion even without full liveness.
- Activation or effect: Writes deprecated status and log; withdrawal from default selection is enforced by retrieval, not epistemic refutation.
- Evidence limits: Current links/hits/date only; no judgment that unlinked narrative is false or useless. Actual retirements unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if matched.hits_for_best() > 0:
>     live_anchor = True
>     break
> orphan = doc.identity not in inbound and not live_anchor
> expired_draft = doc.status == ConceptStatus.draft and _expired(doc.frontmatter.stale_after)
> if orphan or expired_draft:
>     deprecate_concept(repo, doc.identity, reason="gc")
>     retired.append(doc.identity)
> --- `src/repocodex/commands/audit.py`

#### EPI-RTE-impact-read
Label: MCP impact selection

Distinct from [RT-RTE-context-read](runtime.md#rt-rte-context-read): overlapping loaded concepts, but this exposed operation returns impacted identities from a changed-file/link/pin walk rather than ranked bodies. The runtime names impact output under validation but has no separate record for the MCP get_impact consumer. Code calls validate to obtain changed_files, reloads concepts and index, walks seeds, Markdown links and linked-document pins. It returns advisory identities, not checks of the linked claims. Owner/next-step policy is deterministic code; caller chooses base and later interprets relevance. SRC-1 implementation: `src/repocodex/mcp_server.py`, `src/repocodex/engine/impact.py`.

- Immediate return: impacted_scenarios, engine_version and advisory true; validation's full blocking envelope is not forwarded by this tool.
- Later read-back: Uses stored concept links and pins at each call; this route writes no memory, though its internal validate call can append metrics.
- Delegated visibility: MCP host receives identities, not full bodies or full validation findings; further retrieval is separate.
- Selection predicate: Changed-file reverse-index seeds, seed body links, then other concepts sharing linked documents' pins; no unbounded recursive walk.
- Invalidation or expiry: Recomputed current mapping; no semantic approval or expiry decision.
- Activation or effect: Advisory relevance signal to requesting host; no denial or automatic revision; behavioral response unobserved.
- Evidence limits: Stored-edge completeness and semantic relevance unestablished; does not certify all affected behavior was found.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> files = verdict.get("changed_files") or []
> return {
>     "engine_version": verdict["engine_version"],
>     "impacted_scenarios": intent_impact(files, concepts, index),
>     "advisory": True,
> }
> --- `src/repocodex/mcp_server.py`

### Claims

#### EPI-CLM-pin-match
Label: Pin match proof claim

Distinct from [RT-CLM-executable-memory](runtime.md#rt-clm-executable-memory), which names the operation bundle rather than this proof license. SRC-1 doctrine/design: `README.md`, `docs/architecture.md`. The public assertion is proof that stored why matches live text. Supported scope: mechanical attachment according to selected terms, region algorithm and current source; not proof of prose truth, actual behavior, encoding fidelity or historical explanation. Gate/validation implementations, anchorless-write branch, direct patch route and weaker rename check constrain the literal universal reading. Operation and semantic soundness unobserved.

> **Git-native why next to code — with a pin check that proves it still matches.**
> --- `README.md`

> Prove every pinning memory record is about live code text (anchors + write gate) for any grep-able file.
> --- `docs/architecture.md`

#### EPI-CLM-loop-protection
Label: Loop protection claim

Distinct from [RT-CLM-executable-memory](runtime.md#rt-clm-executable-memory) and [EPI-CLM-pin-match](#epi-clm-pin-match): this claims an operational denial and protective consequence, not merely availability of operations or attachment proof. SRC-1 doctrine/design: `README.md`. The shipped coding/review requests and conditional checks support an intended protective loop. The executable consumer denies configured mechanical outcomes, not every divergence between prose and code; default shadow posture, acknowledged exemptions, plain CLI returns and bypassable integration qualify denial. No supplied trace or intervention establishes preservation of behavior, agent compliance or anti-regression benefit.

> The product is that loop: agents retrieve stored why before they edit, so they do not silently break existing behavior; the pin check fails the turn when why and code diverge, and a first substantive edit of an uncovered file is denied until a pinning concept is written.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

