---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "claude-obsidian's claim assessment, mechanical evidence gates and later reliance at the frozen source boundary."
run-id: AAS-2026-10-13-claude-obsidian-c5e56e25c8bb-01
reviewed-boundary: "32ac5a02c4e082e4a5628ca810776375e134708e"
---

# claude-obsidian epistemic report

## Source-and-claim boundary

The question is how the shipped knowledge package acquires or changes truth-apt content, checks it, grants reliance and supplies it to later behavior. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); the evidence identity and layers are see [Source register](boundary.md#source-register), SRC-1. The host scheduler, provider weights, extraction services and Obsidian internals remain external. No live vault, host transcript, executed evaluation or causal comparison was supplied. Thus source inspection establishes mechanisms and requested judgment, not successful acceptance, model obedience or improved knowledge quality.

The consequential product promise is see [RT-CLM-product-promise](runtime.md#rt-clm-product-promise). This report distinguishes provenance eligibility from semantic support, and canonical filing from epistemic acceptance. It directly inspected additional SRC-1 paths at the frozen commit; these extend coverage, not the source register or evidence layer.

| Entry point or operation | Source path | Coverage and records; limitation |
|---|---|---|
| Save, Ingest and worker merge | `skills/save/SKILL.md`, `skills/wiki-ingest/SKILL.md`, `agents/wiki-ingest.md` | Skills directly read; worker supplied by runtime. See [RT-RTE-save-apply](runtime.md#rt-rte-save-apply), [RT-RTE-ingest-drafts](runtime.md#rt-rte-ingest-drafts), [EPI-RTE-evidence-assessment](#epi-rte-evidence-assessment). |
| Research dossier and separate merge | `skills/autoresearch/SKILL.md`, `skills/wiki/references/provenance.md` | Direct reads; see [EPI-RTE-evidence-assessment](#epi-rte-evidence-assessment), [EPI-RTE-canonical-integration](#epi-rte-canonical-integration). No operated research trace. |
| Query and optional retrieval tiers | `skills/wiki-query/SKILL.md`, `scripts/retrieve.py`, `scripts/rerank.py`, `scripts/contextual-prefix.py` | Query and synthetic-prefix implementation directly read; other executable paths supplied by runtime. See [RT-RTE-vault-query](runtime.md#rt-rte-vault-query), [RT-RTE-optional-rerank](runtime.md#rt-rte-optional-rerank), [RT-RTE-prefix-generation](runtime.md#rt-rte-prefix-generation), [EPI-RTE-synthetic-prefix](#epi-rte-synthetic-prefix). |
| Transaction inspect/apply/recover and direct capture | `claude_obsidian/transaction.py`, `claude_obsidian/capture.py` | Prospective ledger gate directly read; admission/recovery/capture supplied by runtime. See [EPI-RTE-ledger-check](#epi-rte-ledger-check), [EPI-RTE-ledger-disposition](#epi-rte-ledger-disposition), [RT-RTE-direct-capture](runtime.md#rt-rte-direct-capture). Capture queue and external runner implementations not traced here; extraction fidelity and queue-complete lineage conclusions are prevented. |
| CLI dispatch and hooks | `claude_obsidian/cli.py`, `hooks/hooks.json`, `claude_obsidian/hook_adapter.py` | CLI dispatch searched, lint handler directly read; hook bodies supplied by runtime. See [RT-RTE-session-context](runtime.md#rt-rte-session-context). No local registered model tool dispatcher was established; external host/tool grants remain uninspected. |
| Lint, repair and checkpoint | `claude_obsidian/lint_engine.py`, `claude_obsidian/checkpoint.py`, `skills/wiki-lint/SKILL.md` | Provenance lint binding, checkpoint blocker and opt-out directly read; other lint checks supplied by runtime. See [EPI-RTE-checkpoint-gate](#epi-rte-checkpoint-gate), [RT-RTE-review-machinery](runtime.md#rt-rte-review-machinery). |
| Fold and Think | `skills/wiki-fold/SKILL.md`, `skills/think/SKILL.md` | Direct reads; see [EPI-RTE-extractive-fold](#epi-rte-extractive-fold), [EPI-RTE-evidence-assessment](#epi-rte-evidence-assessment). Think is read-only; neither name establishes acceptance or improved reasoning. |
| Boundary score and semantic tiling | `scripts/boundary-score.py`, `scripts/tiling-check.py` | Graph/scoring/output and tiling embedding/cache/report bodies directly read; see [EPI-RTE-diagnostic-selection](#epi-rte-diagnostic-selection). Added material routes beyond runtime's fresh inspection. |
| Mode, setup, migration, adopt and extension seeds | `claude_obsidian/cli.py`, `claude_obsidian/ledgers.py`, `claude_obsidian/extensions.py` | Dispatch searched; provenance migration doctrine directly read, seed/config admission supplied by runtime. See [RT-RTE-mode-extension](runtime.md#rt-rte-mode-extension). Full migration and adopt bodies not assessed here; legacy semantic lineage not established. |
| Product contracts, verifier, release gates and archive | `claude_obsidian/contracts.py`, `claude_obsidian/gates.py`, `claude_obsidian/release.py`, `agents/verifier.md` | Supplied runtime [RT-RTE-review-machinery](runtime.md#rt-rte-review-machinery); no observed verification or publishing. |
| Other shipped skills, transports and supporting setup | `skills/wiki-cli/SKILL.md`, `skills/defuddle/SKILL.md`, `skills/canvas/SKILL.md`, `skills/obsidian-bases/SKILL.md`, `skills/obsidian-markdown/SKILL.md`, `scripts/detect-transport.sh` | CLI skill directly read: optional read transport, not mutation authority. Other skill/extraction/formatting bodies and transport detector not assessed afresh. Their semantic transformations and complete operational-selection coverage remain unestablished. |

Unassessed relevant operations prevent a system-complete negative about knowledge production, acceptance or behavior adaptation. Available source not read is not an access gap. Missing extraction implementations prevent judging fidelity of media imports; missing provider internals prevent judging internal parametric learning. Missing executions prevent identifying actual produced claims, evidence-consuming acceptance instances and later behavioral activation.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-claim-ledger](#epi-obj-claim-ledger) | Claim text scoped by note location, evidence and review fields | see record | SRC-1 `claude_obsidian/ledgers.py` | The program checks nonempty text, not falsifiability or source entailment. |
| [EPI-OBJ-source-ledger](#epi-obj-source-ledger) | Statements about source origin, payload identity and review/freshness | see record | SRC-1 `skills/wiki/references/provenance.md` | Metadata and matching bytes do not establish source truth. |
| [RT-OBJ-transaction-bundle](runtime.md#rt-obj-transaction-bundle) | Prose payloads may carry claims; symbolic plan carries byte/path assertions | see record | SRC-1 `claude_obsidian/transaction.py` | Mixed container; digest approval is not semantic acceptance. |
| [EPI-OBJ-derived-context](#epi-obj-derived-context) | Synthetic opening excerpts; model contextual sentences; diagnostic descriptions of graph/vector relationships | see record | SRC-1 `scripts/contextual-prefix.py`, `scripts/tiling-check.py` | Split consumption paths in ledger; numerical scores are not claim truth judgments. |
| [RT-OBJ-skills](runtime.md#rt-obj-skills) | Policies and requested reasoning; not acquired factual support | see record | SRC-1 `skills/think/SKILL.md` | The stage named ACCEPT means stating uncertainty, not the report's technical acceptance. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-CMP-haiku-prefix](runtime.md#rt-cmp-haiku-prefix), [RT-CMP-ollama-embedding](runtime.md#rt-cmp-ollama-embedding) | Internal truth-apt content not determinable from weights/API labels | see records | SRC-1 `agents/wiki-ingest.md`, `scripts/contextual-prefix.py`, `scripts/rerank.py` | External distributed-parametric internals; inference wiring does not expose training or prove no learning. |

Raw sources, page drafts, retained notes, hot context and fold children are endpoints of cited routes, not an asserted census of real artifacts. No supplied user artifact individuates an actually accepted claim.

## Authority-route ledger

Fields owned by declaring records are given by citation; architectural status and the content-edge classification are this report's overlay. Separate rows preserve checking, disposition, retention and integration.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-direct-capture](runtime.md#rt-rte-direct-capture) | content transformation | implemented | Raw payload | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Source warrant unknown; bytes are acquired, not established | see record | see record | SRC-1 `claude_obsidian/capture.py` | none | none | No semantic extraction evaluation supplied. |
| [RT-RTE-ingest-drafts](runtime.md#rt-rte-ingest-drafts) | content transformation | doctrine only | Draft pages | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Source statements are acquired; synthesis may reshape, derive or conjecture | see record | see record | SRC-1 `skills/wiki-ingest/SKILL.md` | [RT-CLM-product-promise](runtime.md#rt-clm-product-promise) | none | No input/output instance establishes entailment or non-entailment of synthesis. |
| [EPI-RTE-evidence-assessment](#epi-rte-evidence-assessment) | check/evidence production | doctrine only | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `skills/autoresearch/SKILL.md` | [RT-CLM-product-promise](runtime.md#rt-clm-product-promise) | none | Requested source reading and counter-position checks, not demonstrated checking. |
| [EPI-RTE-ledger-check](#epi-rte-ledger-check) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Contract violations follow from supplied fields within validator semantics | see record | see record | SRC-1 `claude_obsidian/ledgers.py` | none | none | No source truth or semantic entailment test. |
| [EPI-RTE-ledger-disposition](#epi-rte-ledger-disposition) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Mechanical eligibility only; not acceptance of claim truth | see record | see record | SRC-1 `claude_obsidian/transaction.py` | none | none | Gate runs when a ledger is written, not for every prose edit. |
| [RT-RTE-save-apply](runtime.md#rt-rte-save-apply) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | Retains submitted claims and metadata without adding warrant | see record | see record | SRC-1 `claude_obsidian/transaction.py` | [RT-CLM-product-promise](runtime.md#rt-clm-product-promise) | none | Successful persistence and actual review unobserved. |
| [EPI-RTE-canonical-integration](#epi-rte-canonical-integration) | lifecycle integration | doctrine only | Accepted claim candidate | no content change | see record | see record | see record | see record | see record | Intended integration after assessment; no accepted instance established | see record | see record | SRC-1 `skills/autoresearch/SKILL.md` | [RT-CLM-product-promise](runtime.md#rt-clm-product-promise) | none | Filing unsupported/provisional content is retention, not lifecycle integration. |
| [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) | operational admission/selection/consumption | implemented | Retained pages/ledgers | no content change | see record | see record | see record | see record | see record | BM25 supplies candidates; requested model uses current support for reliance | see record | see record | SRC-1 `skills/wiki-query/SKILL.md` | [RT-CLM-product-promise](runtime.md#rt-clm-product-promise) | none | Retrieval wiring implemented; semantic answer discipline doctrine only. |
| [RT-RTE-vault-query](runtime.md#rt-rte-vault-query) | content transformation | doctrine only | Cited answer | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Requested separation of evidence and inference; no answer instance | see record | see record | SRC-1 `skills/wiki-query/SKILL.md` | none | none | Neither produced accepted ampliation nor checked derivation established. |
| [EPI-RTE-synthetic-prefix](#epi-rte-synthetic-prefix) | content transformation | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Preserves selected opening text, not its factual warrant | see record | see record | SRC-1 `scripts/contextual-prefix.py` | none | none | 300-character truncation can omit qualification; title fidelity assumed from metadata. |
| [RT-RTE-prefix-generation](runtime.md#rt-rte-prefix-generation) | content transformation | implemented | Model prefix | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Unknown semantic preservation and source warrant | see record | see record | SRC-1 `scripts/contextual-prefix.py` | none | none | First-line extraction/fallback is not evidence-consuming acceptance. |
| [RT-RTE-optional-rerank](runtime.md#rt-rte-optional-rerank) | operational admission/selection/consumption | implemented | Embeddings/page candidates | no content change | see record | see record | see record | see record | see record | Similarity orders candidates, not truth | see record | see record | SRC-1 `scripts/rerank.py` | none | none | No ranked-result execution or benefit evidence. |
| [RT-RTE-session-context](runtime.md#rt-rte-session-context) | operational admission/selection/consumption | implemented | Hot context | no content change | see record | see record | see record | see record | see record | Orientation, not independent evidence | see record | see record | SRC-1 `claude_obsidian/hook_adapter.py` | none | none | Host delivery and influence unobserved. |
| [EPI-RTE-extractive-fold](#epi-rte-extractive-fold) | content transformation | doctrine only | Fold draft | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Intended extractive reshaping, no new evidence or upgrade | see record | see record | SRC-1 `skills/wiki-fold/SKILL.md` | none | none | Actual preservation depends on model drafting and verification. |
| [EPI-RTE-diagnostic-selection](#epi-rte-diagnostic-selection) | check/evidence production | implemented | Graph scores/vector pairs | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Numeric/report predicates within parsed graph or supplied vectors only | see record | see record | SRC-1 `scripts/tiling-check.py` | none | none | Semantic redundancy remains a heuristic interpretation. |
| [EPI-RTE-checkpoint-gate](#epi-rte-checkpoint-gate) | disposition/acceptance | implemented | Operation worktree | no content change | see record | see record | see record | see record | see record | Eligible for checkpoint under selected lint categories, not factual acceptance | see record | see record | SRC-1 `claude_obsidian/checkpoint.py` | none | none | Caller can skip lint; checkpoint is not mandatory for retention. |
| [RT-RTE-review-machinery](runtime.md#rt-rte-review-machinery) | check/evidence production | implemented | Product/capability candidate | no content change | see record | see record | see record | see record | see record | Covered executable verifier/test outcomes, not general knowledge correctness | see record | see record | SRC-1 `claude_obsidian/contracts.py` | none | none | Actual results unobserved; manual release gates remain separate. |
| [RT-RTE-mode-extension](runtime.md#rt-rte-mode-extension) | behavior/policy adaptation | implemented | Routing mode/seed thresholds | non-truth-apt policy/content update: explicit routing configuration | see record | see record | see record | see record | see record | No semantic calibration license from seed installation | see record | see record | SRC-1 `claude_obsidian/extensions.py` | none | none | Explicit configuration, not demonstrated evaluation-fed improvement. |

Retention of derived prefixes and embeddings, and stale filtering/rebuild invalidation, are see [RT-RTE-prefix-generation](runtime.md#rt-rte-prefix-generation), [RT-RTE-optional-rerank](runtime.md#rt-rte-optional-rerank) and [RT-RTE-vault-query](runtime.md#rt-rte-vault-query). They change availability and ranking, not endorsement. Transaction rollback and replay validation are see [RT-RTE-save-apply](runtime.md#rt-rte-save-apply): restoring bytes is recovery, not withdrawing a false claim. Source `superseded`/`rejected` states can withhold eligible support at the validator and Query consumer; no automatic semantic source adjudicator is established by those enumerations.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-product-promise](runtime.md#rt-clm-product-promise) | see record | SRC-1 `config/product-contract.json`; doctrine/design | Source/claim rules, bounded research, citations and separate merge | [RT-RTE-save-apply](runtime.md#rt-rte-save-apply), [RT-RTE-vault-query](runtime.md#rt-rte-vault-query), [EPI-RTE-ledger-disposition](#epi-rte-ledger-disposition) | None supplied | No quality or component intervention; source eligibility does not establish support semantics | Shipped source-cited construction and later consumption pathways, with mechanical provenance constraints | Compounding quality remains unestablished, not disproved. |

Acceptance requirements are operational policy, not a second unconditional correctness promise. The strongest countercase to treating admission as factual acceptance is the validator's fresh-contradiction branch: nonempty adjudication notes permit the accepted assessment to survive; the program does not evaluate whether the notes resolve the contradiction. Conversely, the implemented freshness and independence checks defeat a claim that provenance is only advisory. Both conclusions are localized to [EPI-RTE-ledger-check](#epi-rte-ledger-check) and [EPI-RTE-ledger-disposition](#epi-rte-ledger-disposition).

## Bounded conclusion

The package acquires raw material, requests source-grounded drafting and retains admitted notes and ledger records for later queries and optional lifecycle context. Raw capture preserves bytes; that alone leaves source warrant unknown. Save explicitly treats conversation assertions as synthetic or unsupported/provisional rather than independent corroboration. These are separate pathways, not a guarantee that every saved page is accepted knowledge. See [RT-RTE-direct-capture](runtime.md#rt-rte-direct-capture), [RT-RTE-save-apply](runtime.md#rt-rte-save-apply), [EPI-RTE-evidence-assessment](#epi-rte-evidence-assessment).

Claim eligibility has real computational force: fresh active non-synthetic support, review chronology, high-risk independent corroboration and contradiction handling are checked against declared metadata. Prospective ledger violations reject ledger-bearing transactions; lint also reports violations and can block an explicit checkpoint. No content comparison establishes that a cited source actually supports the claim. A valid ledger containing adjudication notes can therefore be mechanically eligible without a demonstrated justified adjudication. See [EPI-RTE-ledger-check](#epi-rte-ledger-check), [EPI-RTE-ledger-disposition](#epi-rte-ledger-disposition), [EPI-RTE-checkpoint-gate](#epi-rte-checkpoint-gate).

Research and query instructions name material criteria and intended use: grounded source-backed vault claims and answers, with contradictions preserved and insufficient support refused. High-risk claims require two independent sources. The foreground model assesses evidence, the parent resolves draft conflicts, and the user may reject or narrow filing and canonical merge. This is requested evidence-consuming acceptance and integration, not an observed accepted ampliative production instance. Hash approval binds planned effects; it authenticates neither human prose review nor semantic warrant. See [EPI-RTE-evidence-assessment](#epi-rte-evidence-assessment), [EPI-RTE-canonical-integration](#epi-rte-canonical-integration), [RT-RTE-save-apply](runtime.md#rt-rte-save-apply).

Synthetic prefixes demonstrably reshape selected text; model prefixes, fold themes, synthesis and answers remain semantically indeterminate without inspected input/output instances. Deterministic violations, graph scores and threshold bands are derivable within their formal input domain, not from warranted factual premises about the external world. Ranking changes selection; tiling diagnostics flag vector proximity, not falsehood, conceptual identity or warranted merging. See [EPI-RTE-synthetic-prefix](#epi-rte-synthetic-prefix), [EPI-RTE-extractive-fold](#epi-rte-extractive-fold), [EPI-RTE-diagnostic-selection](#epi-rte-diagnostic-selection).

Current source review/freshness can withhold reliance through Query's requested interpretation and the ledger gate; known stale retrieval candidates are filtered by code. The data envelope does not enforce model compliance. Explicit mode changes alter routing without a truth-apt acceptance route. External weights and mutable model endpoints remain bounded by the component findings in runtime. No single conclusion about learning, reflection, autonomous theory building or self-improvement follows from these mechanisms; improved capacity, actual content-directed criticism shaping later rounds, and causally exercised improvement are independently unestablished by this evidence. Uninspected supporting operations prevent universal negatives.

## Shared records

### Operative objects

#### EPI-OBJ-claim-ledger
Label: Claim ledger

Source-native identity: `wiki/meta/ledgers/claim-ledger.json`, schema `claude-obsidian.claim-ledger.v1`. Representational form: natural-language claim text and notes interpreted by models/humans, coupled to symbolic assessment/risk/review/evidence fields interpreted by validators. Storage substrate: vault JSON. Distinct from [RT-OBJ-transaction-bundle](runtime.md#rt-obj-transaction-bundle): the durable ledger is a payload/result, not the submitted operation or plan; runtime declares no ledger counterpart. SRC-1 `claude_obsidian/ledgers.py`, implementation; `skills/wiki/references/provenance.md`, doctrine/design.

> - `wiki/meta/ledgers/claim-ledger.json`: falsifiable claims, note locations,
>   support, contradictions, confidence, risk, and review state.
> --- `skills/wiki/references/provenance.md`

#### EPI-OBJ-source-ledger
Label: Source ledger

Source-native identity: `wiki/meta/ledgers/source-ledger.json`. Representational form: symbolic source status/identity/date/hash fields and textual metadata. Storage substrate: vault JSON. Distinct from [RT-OBJ-transaction-bundle](runtime.md#rt-obj-transaction-bundle), a plan that may carry this durable payload; no supplied ledger counterpart. SRC-1 `skills/wiki/references/provenance.md`, doctrine/design; `claude_obsidian/ledgers.py`, implementation.

> - `wiki/meta/ledgers/source-ledger.json`: stable source identities, authority,
>   SHA-256, retrieval/freshness, review state, and linked pages.
> --- `skills/wiki/references/provenance.md`

#### EPI-OBJ-derived-context
Label: Derived retrieval and diagnostic context

Source-native identity: contextual prefixes/chunk text and diagnostic graph/vector outputs. Representational form: natural-language prefixes/reports, symbolic graph/count/band data and distributed-parametric embedding vectors. Storage substrate: chunk/cache JSON and stdout reports. This is a container, split by checks and consumers in the routes below. No supplied operative-object counterpart after comparison with [RT-OBJ-skills](runtime.md#rt-obj-skills) and [RT-OBJ-transaction-bundle](runtime.md#rt-obj-transaction-bundle); it overlaps endpoints of [RT-RTE-prefix-generation](runtime.md#rt-rte-prefix-generation) and [RT-RTE-optional-rerank](runtime.md#rt-rte-optional-rerank), not their identities as routes. Model provenance/fixity remains see runtime components. SRC-1 `scripts/contextual-prefix.py`, `scripts/tiling-check.py`, implementation; passages in the corresponding new routes.

### Routes

#### EPI-RTE-evidence-assessment
Label: Evidence assessment requests

Part of: [RT-RTE-ingest-drafts](runtime.md#rt-rte-ingest-drafts)

This record owns the source-assessment phase of ingest; Research, Save and Think supply related doctrine, not asserted identity with the ingest route. Endpoints/progression: available source/selected material → foreground or worker interpretation → falsifiable claims, evidence, counter-positions, uncertainty and proposed assessments. Owner: model proposes/assesses, parent resolves worker conflicts, user can reject scope or filing. Open scoped requests or bounded research rounds, not comparative experiments. No answer oracle: source evidence is not an expected correct synthesis. Criterion/intended use: source-backed vault claims, current support, high-risk corroboration and grounded refusal; epistemic authority is requested and scoped to that evidence, not enforced semantic truth. Operational authority is advisory draft assessment passed by worker packet/chat to parent/user during the workflow. Theory-like hypotheses and counter-positions are requested, but no complete formulated theory or content-directed criticism instance is supplied; iteration of searches is doctrine, not demonstrated theory-builder iteration. No admission, rollback or retained change occurs in this phase.

- Immediate return: Proposed claims, assessments, contradictions and missing evidence.
- Later read-back: inapplicable — this assessment phase returns drafts; retention is separately admitted.
- Delegated visibility: Worker packet to parent; actual host isolation uninspected.
- Selection predicate: Scoped source and bounded relevant pages; plausible counter-position and gaps requested.
- Invalidation or expiry: Source changes or incomplete reads require revised/partial treatment by instruction.
- Activation or effect: Requested assessment and refusal behavior; no operated judgment supplied.
- Evidence limits: Doctrine/design only; neither claim entailment nor semantic acceptance established.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1 `skills/wiki-ingest/SKILL.md`, `skills/autoresearch/SKILL.md`, `skills/save/SKILL.md`, `skills/think/SKILL.md`.

> Conversation assertions are not
> independent evidence; classify them as synthetic or unsupported/provisional as
> appropriate. They cannot alone make a claim `accepted`.
> --- `skills/save/SKILL.md`

> 4. Extract falsifiable claims with precise evidence locators. Keep source
>    statements separate from inference.
> 5. Search the gaps and contradictions, not merely more examples of the leading
>    view. Deduplicate syndicated or dependent sources.
> --- `skills/autoresearch/SKILL.md`

#### EPI-RTE-ledger-check
Label: Ledger eligibility check

Distinct check subfunction of [RT-RTE-review-machinery](runtime.md#rt-rte-review-machinery), overlapping its lint endpoint but also used by transaction preparation; not part of exactly one supplied route. Endpoints: claim/source JSON, prospective page bytes and audit date → source/claim validators → sorted violations. Owner/evaluator: Python predicates over symbolic fields, file hashes/locations/anchors, review chronology, freshness and declared independence. Proposer of records is caller/model; code evaluates, no human semantic contribution inside validator. Mode: deterministic contract audit; no source-truth answer oracle. Claims marked accepted require fresh active non-synthetic support and review date; high risk requires two independent groups collapsed by origin/bytes/declared keys. Fresh contradicting evidence requires contested assessment or nonempty adjudication notes. These are necessary eligibility conditions, not semantic sufficiency. Returned errors themselves have no admission force until consumed. No change or rollback in this function.

- Immediate return: Sorted path/message violations.
- Later read-back: inapplicable — check produces current-call errors, not retained judgments.
- Delegated visibility: inapplicable — local function, no worker.
- Selection predicate: All supplied ledger records; fresh support evaluated at audit date.
- Invalidation or expiry: Recomputed from dates/current files; rejected/superseded sources fail active support predicate.
- Activation or effect: Derives violations within validator semantics; lint/transaction consume them separately.
- Evidence limits: Does not read source passages to test entailment; nonempty text is not a falsifiability analysis and nonempty notes are not evaluated adjudication.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `claude_obsidian/ledgers.py`, implementation.

> if assessment == "accepted" and not fresh_support:
>     _error(
>         errors,
>         f"{prefix}.assessment",
>         "accepted claims require fresh active support",
>     )
> --- `claude_obsidian/ledgers.py`

> if (
>     assessment == "accepted"
>     and risk == "high"
>     and _independent_group_count(fresh_support) < 2
> ):
>     _error(
>         errors,
>         f"{prefix}.evidence",
>         "high-risk acceptance requires two independent sources",
>     )
> --- `claude_obsidian/ledgers.py`

> if (
>     assessment == "accepted"
>     and fresh_contradictions
>     and not (
>         isinstance(notes, str)
>         and not _contains_non_scalar(notes)
>         and notes.strip()
>     )
> ):
>     _error(
>         errors,
>         f"{prefix}.assessment",
>         "accepted claims with fresh contradictory evidence require contested assessment or adjudication notes",
>     )
> --- `claude_obsidian/ledgers.py`

Concrete deduction: with an otherwise valid accepted low-risk record, one eligible support source and one eligible contradicting source, `notes=None` reaches the contradiction error; `notes="Reviewed"` skips that error. This follows from inspected code, was not executed, and warrants only that branch result, not overall ledger validity or truth.

#### EPI-RTE-ledger-disposition
Label: Prospective ledger disposition

Part of: [RT-RTE-save-apply](runtime.md#rt-rte-save-apply)

Endpoints/progression: prepared writes → complete prospective source/claim pair → validators → reject exception or continue preparation. Owner: transaction code; caller proposes bytes, user review is separate plan protocol, validators veto invalid ledger changes. Trigger/proposed change: writing either provenance ledger. Operating mode: deterministic admission; no semantic answer oracle. Guidance is the ledger contract; accepted assessments are supplied, not inferred by code. Consumer/channel/force/horizon: transaction preparation consumes validator errors as enforcing exceptions for current bundle; continued apply uses ordinary journal recovery. Passing checks allows persistence, not epistemic acceptance. Distinct from the validator's evidence-production function.

- Immediate return: None on success or INVALID_PROVENANCE_LEDGER error.
- Later read-back: Admitted ledger bytes later reach Query/lint; persistence and recovery are see parent route.
- Delegated visibility: inapplicable — local transaction code, not worker review.
- Selection predicate: Run only when SOURCE_PATH or CLAIM_PATH appears among prepared writes.
- Invalidation or expiry: Current/planned files and audit-date checks can reject prospective state; not automatic later withdrawal.
- Activation or effect: Exceptions block ledger-bearing prepared changes.
- Evidence limits: Prose-only edits bypass this ledger gate; external host writes are outside the transaction plane.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `claude_obsidian/transaction.py`, implementation.

> planned = {write.relative_path: write.content for write in prepared}
> if SOURCE_PATH not in planned and CLAIM_PATH not in planned:
>     return
> --- `claude_obsidian/transaction.py`

> if errors:
>     ordered = sorted(errors, key=lambda item: (item["path"], item["message"]))
>     detail = "; ".join(f"{item['path']}: {item['message']}" for item in ordered)
>     raise TransactionValidationError("INVALID_PROVENANCE_LEDGER", detail)
> --- `claude_obsidian/transaction.py`

#### EPI-RTE-canonical-integration
Label: Separately reviewed canonical integration

Distinct from [RT-RTE-save-apply](runtime.md#rt-rte-save-apply)'s byte retention and [RT-RTE-ingest-drafts](runtime.md#rt-rte-ingest-drafts)'s worker phase: owns Research's second-merge policy. Endpoints: filed dossier/evidence ledger → proposed canonical updates → separate review → transaction. Model proposes, user accepts/narrows/postpones/rejects, parent applies; core can veto stale/malformed plans and supplies journal rollback. Trigger: explicit desire to merge research, guided by provenance and cited dossier. Open reviewed operation; no answer oracle. Only claims accepted by evidence-consuming assessment qualify as lifecycle integration here; merely filing a dossier or provisional claim does not. Intended authority: evidence-linked canonical claims in their researched scope. Consumer/channel/force/horizon: later Query/Save reads canonical pages as evidence, interpreted by model subject to current support rules; user approval permits filing, not truth by fiat.

- Immediate return: Proposed second merge or separately applied paths.
- Later read-back: Canonical pages and citations available to later vault consumers if admitted.
- Delegated visibility: Workers supply drafts only; parent/user receives proposal.
- Selection predicate: Reviewed dossier/evidence and user-selected canonical scope.
- Invalidation or expiry: Current support and transaction preconditions; no automatic semantic withdrawal.
- Activation or effect: Requested reviewed integration; executable persistence uses shared core.
- Evidence limits: No accepted claim instance, user review or downstream use supplied; doctrine only for epistemic integration.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1 `skills/autoresearch/SKILL.md`, doctrine/design.

> After the dossier is filed, propose any updates to existing concept, entity,
> domain, overview, or decision pages as a second, separately inspected and
> explicitly approved transaction. Cite the dossier and evidence ledger. The user
> may accept, narrow, postpone, or reject that merge without losing the research
> artifact.
> --- `skills/autoresearch/SKILL.md`

#### EPI-RTE-synthetic-prefix
Label: Synthetic prefix reshaping

Part of: [RT-RTE-prefix-generation](runtime.md#rt-rte-prefix-generation)

Endpoints/progression: title metadata/page body → first sentence and 300-character slice → template prefix → parent chunk-processing/index route. Owner: deterministic function. No factual evaluator or acceptance decision; the code copies selected text. Domain: supplied strings, not external truth. Consumer/channel/force/horizon: prefix enters contextualized indexed text and ranking across rebuilds; force is selection context, not canonical authority. For `fm={"title":"Water"}`, body `Water freezes. Next topic.`, any chunk, the inspected implementation returns `This passage is from the wiki page "Water". The page opens: Water freezes.` This is a source-grounded deduction, not target execution; no novel substantive claim beyond supplied metadata/text is warranted.

- Immediate return: Template text containing title and sliced first sentence.
- Later read-back: Parent generation route stores derived chunk context for later retrieval.
- Delegated visibility: inapplicable — no provider/worker call in synthetic branch.
- Selection predicate: First sentence of page body, not necessarily the chunk; title or untitled fallback.
- Invalidation or expiry: Parent page/chunk hash rebuild rules, see parent route.
- Activation or effect: Changes lexical corpus/context; relevance benefit unobserved.
- Evidence limits: Truncation can drop qualifications; reshaping preserves copied text, not source truth or contextual sufficiency.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `scripts/contextual-prefix.py`, implementation.

> title = (fm.get("title") or "").strip() or "(untitled)"
> # First sentence of the body (not the chunk — gives the chunk a page-level frame)
> first_sentence = re.split(r"(?<=[.!?])\s+", body.strip(), maxsplit=1)
> first = first_sentence[0][:300] if first_sentence else ""
> return f'This passage is from the wiki page "{title}". The page opens: {first}'
> --- `scripts/contextual-prefix.py`

#### EPI-RTE-extractive-fold
Label: Extractive fold proposal

Distinct from [RT-RTE-save-apply](runtime.md#rt-rte-save-apply): manual log-rollup transformation with its own requested checks; shared core later retains bytes. Endpoints: selected complete log entries → extracts/themes/child table → count/bijection/numeric/citation checks → preview → optionally reviewed fold bundle. Model assembles and checks; user vetoes/apply authorization; core vetoes invalid/stale bundle and journals recovery. Mode: bounded explicit operation, no automatic fold-of-folds. Oracle: selected entries supply traceability references, not a correct synthesis oracle. Scope: the log is primary even when child pages disagree. No claim assessment upgrade; intended extractive reshaping remains unconfirmed without an artifact. Consumer/channel/force/horizon: index/catalog/log expose rollup to later readers, advisory history summary rather than new factual evidence.

- Immediate return: Complete draft/ID/range/budget, shortfall stop or existing-ID no-op.
- Later read-back: Reviewed fold can be reached through index/log in later invocations.
- Delegated visibility: Workers return extracts; parent assembles, no worker writes.
- Selection predicate: User range or batch 2^k, complete batch required.
- Invalidation or expiry: Existing deterministic ID no-op; force replacement separately reviewed, hashes rechecked.
- Activation or effect: Requested additive rollup; children preserved, hot context not updated.
- Evidence limits: Instructions do not establish faithful themes, counts or check compliance in practice.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

SRC-1 `skills/wiki-fold/SKILL.md`, doctrine/design.

> A fold adds no new factual evidence, so it does not upgrade claim assessments or
> create source records. Report discovered contradictions for later review instead
> of editing canonical claims.
> --- `skills/wiki-fold/SKILL.md`

#### EPI-RTE-diagnostic-selection
Label: Graph and tiling diagnostics

Distinct from [RT-RTE-review-machinery](runtime.md#rt-rte-review-machinery)'s lint/product checks and [RT-RTE-optional-rerank](runtime.md#rt-rte-optional-rerank)'s retrieval ranking. Two linked diagnostic consumers, not one truth evaluator. Boundary score: parsed known-page graph → (out-degree minus in-degree) times recency → sorted positive frontier report. Tiling: included page bodies → Ollama embeddings/cache → cosine pairs → configured review/error bands → stdout report. Owner/decider: code selects and scores, human/model can use report later; no automatic canonical merge or repair consumer was found in these inspected bodies. Domain/license: formal graph/count or vector/threshold relations; neither score establishes novelty, contradiction, redundancy or truth. No expected-answer oracle or semantic calibration supplied. Consumer/channel/force/horizon: sorted stdout/report is advisory current diagnosis; tiling cache is automatically retained for later checks, not accepted claims. Tiling uses an external caller-selected model/tag, body/model-name hashes, no immutable weight pin or client training; provider internals uninspected. Separate tiling model resolution is not inferred from rerank's installed-model choice.

- Immediate return: Frontier scores or similarity pairs/bands with calibration and skip diagnostics.
- Later read-back: Tiling stores embeddings in .vault-meta/tiling-cache.json for subsequent checks; graph report itself is stdout-only.
- Delegated visibility: Page bodies sent to selected Ollama inference endpoint; no host worker.
- Selection predicate: Scoreable included pages/known edges; tiling included readable bounded pages; positive/top frontier or cosine >= review band.
- Invalidation or expiry: Body/model-name hash mismatch recomputes embeddings; orphan cache entries pruned; same-tag weight replacement not detected by body_hash.
- Activation or effect: Selects diagnostic attention and persists derived cache; no automatic epistemic adjudication or canonical repair in inspected bodies.
- Evidence limits: Skips reduce coverage; uncalibrated thresholds do not authorize semantic merging; no executed diagnostic or intervention supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `scripts/boundary-score.py`, `scripts/tiling-check.py`, implementation. These added diagnostic routes do not supersede runtime's valid review container.

> score = (out_deg - in_deg) * rw
> --- `scripts/boundary-score.py`

> errors = [p for p in pairs if p[0] >= error_]
> reviews = [p for p in pairs if review <= p[0] < error_]
> --- `scripts/tiling-check.py`

> # Orphan GC: drop cache entries for paths that no longer exist.
> orphans = [k for k in cache["embeddings"] if k not in live_paths]
> for k in orphans:
>     del cache["embeddings"][k]
> --- `scripts/tiling-check.py`

#### EPI-RTE-checkpoint-gate
Label: Checkpoint lint disposition

Distinct from [RT-RTE-review-machinery](runtime.md#rt-rte-review-machinery)'s report/repair and [RT-RTE-save-apply](runtime.md#rt-rte-save-apply)'s persistence: a separately requested exact-operation Git checkpoint consumer. Endpoints: completed operation/current worktree → lint report when enabled → selected blockers → exception or pending checkpoint construction. Owner: Python code; caller requests checkpoint and can skip lint, user may decline checkpoint entirely. Target/domain: covered structural/provenance categories in current vault, not semantic truth. Trigger/proposed change: explicit checkpoint of completed paths, not canonical admission. Guidance: fixed blocking categories; no answer oracle for page prose. Consumer/channel/force/horizon: checkpoint construction consumes lint categories as enforcing gate for that invocation; no claim review-state change or retroactive rejection of retained note. Resumption/verification follows pending checkpoint metadata; full Git internals were not traced here.

- Immediate return: LINT_FAILED exception on selected findings or continued checkpoint flow.
- Later read-back: Checkpoint metadata supports later checkpoint resume/replay; no semantic assessment retained by this gate.
- Delegated visibility: inapplicable — local lint/Git pipeline, no worker.
- Selection predicate: Explicit operation, run_lint flag and fixed BLOCKING_LINT_CATEGORIES.
- Invalidation or expiry: Fresh audit/current worktree checks; durable audit date can be reused across pending/final state.
- Activation or effect: Can block a requested checkpoint without undoing prior retention.
- Evidence limits: skip-lint bypass and optional checkpoint mean no universal post-retention warrant gate; no successful checkpoint supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1 `claude_obsidian/checkpoint.py`, `claude_obsidian/cli.py`, implementation.

> if run_lint:
>     lint_root, _ = _descriptor_root_path(root)
>     report = lint_vault(lint_root, as_of=lint_as_of)
>     blockers = {
>         category: len(report.get(category, []))
>         for category in BLOCKING_LINT_CATEGORIES
>         if report.get(category)
>     }
>     if blockers:
>         raise CheckpointError(
>             "LINT_FAILED",
>             "vault lint has blocking findings: "
>             + ", ".join(
>                 f"{key}={value}"
>                 for key, value in sorted(blockers.items())
>             ),
>         )
> --- `claude_obsidian/checkpoint.py`

> checkpoint.add_argument("--skip-lint", action="store_true")
> --- `claude_obsidian/cli.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; paths are stated locally in route declarations and supplied [RT-BAP-skill-authority](runtime.md#rt-bap-skill-authority) and [RT-BAP-plan-enforcement](runtime.md#rt-bap-plan-enforcement).
