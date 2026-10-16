---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AutoSci epistemic routes: source acquisition, hypothesis verdicts, wiki consistency and bounded Hiera evaluation."
run-id: AAS-2026-10-15-autosci-430df584df8f-01
reviewed-boundary: f5c2fe009c6683b6aa5b668de759a0610c938aaf
---

# AutoSci epistemic report

## Source-and-claim boundary

The question is how AutoSci turns imported papers, proposed hypotheses and experiment outputs into later reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identity/layers: see [Source register](boundary.md#source-register), SRC-1. The only frozen source is implementation and doctrine/design, not an observed research run. This report distinguishes scientific evidence assessment from schema checks, retention and score-directed execution.

The runtime is provisional. Its containers remain valid; the records below split consequential checking, disposition and integration parts rather than superseding them. One additional implementation qualification matters: Hiera `loop` re-evaluates selected existing candidates, whereas `tune` creates config variants; reporting an experience revision does not establish that revision drives scheduling. See [EPI-RTE-hiera-select](#epi-rte-hiera-select) and [EPI-RTE-hiera-summary](#epi-rte-hiera-summary). No supplied runtime fact requires supersession.

### Material coverage

“Direct” means source bodies read in this attempt; “supplied” means the runtime finding, not a new source inspection. All paths below are SRC-1 at the frozen commit. Available but uninspected operations prevent a system-complete negative.

| Entry point or operation | Source path | Coverage and records / limit |
|---|---|---|
| Paper import, matching and writing | `.claude/skills/ingest/SKILL.md` | Direct source-resolution through rebuild body; [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) |
| Ask, crystallization, init fan-in, CI intake | `.claude/skills/ask/SKILL.md`, `.claude/skills/init/references/parallel-ingest.md`, `.github/workflows/daily-arxiv.yml` | Supplied: [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle), [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest), [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake) |
| Wiki compiler, lifecycle transition, cleanup | `tools/research_wiki.py` | Direct compiler, transition, edge/citation dedup bodies and complete CLI operation-name search; [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief), [EPI-RTE-edge-dedup](#epi-rte-edge-dedup) |
| Browser metadata/edge mutation | `tools/serve.py` | Supplied: [RT-RTE-browser-write](runtime.md#rt-rte-browser-write); counterpath to enforced scientific acceptance |
| Automated lint and repair; semantic maintenance | `tools/lint.py`, `.claude/skills/check/SKILL.md` | Direct check collector, quality heuristics, fix dispatch and fix bodies; semantic checklist/constraints; [EPI-RTE-wiki-check](#epi-rte-wiki-check), [EPI-RTE-wiki-repair](#epi-rte-wiki-repair) |
| Ideation filtering and refinement | `.claude/skills/ideate/SKILL.md`, `.claude/skills/refine/SKILL.md` | Direct filter/deep-validation and refinement-loop bodies; [EPI-CLM-validated-ideas](#epi-clm-validated-ideas) |
| Experiment hypothesis evaluation/update | `.claude/skills/exp-eval/SKILL.md` | Direct load/check/synthesis/disposition/integration bodies; [EPI-RTE-verdict-check](#epi-rte-verdict-check), [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition), [EPI-RTE-verdict-integrate](#epi-rte-verdict-integrate) |
| Experiment execution/research gates | `.claude/skills/exp-run/SKILL.md`, `.claude/skills/research/SKILL.md` | Supplied: [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict) |
| MCP chat, reply and native search | `mcp-servers/llm-review/server.py`, `.mcp.json` | Direct registration-name search confirms three exposed tools; supplied dispatch/retry/thread evidence: [RT-RTE-review-call](runtime.md#rt-rte-review-call); no extra evaluator inferred |
| Hiera evaluation, status, finalize, tune, loop | `tools/hiera/evaluator.py`, `tools/hiera/cli.py`, `tools/hiera/experience.py`, `tools/hiera/scheduler.py`, `tools/hiera/tuner.py`, `tools/hiera/acquisition.py` | Direct named bodies; [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search), [EPI-RTE-hiera-summary](#epi-rte-hiera-summary), [EPI-RTE-hiera-select](#epi-rte-hiera-select) |
| Hiera remote worker, recovery, admission, contract | `tools/hiera/remote_worker.py`, `tools/hiera/remote_adapter.py`, `tools/hiera/contract.py` | Supplied: [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search); no claim of independent remote measurement authentication |
| Setup activation, writer policy | `setup.sh`, `runtime/policy/writers.yaml` | Supplied: [RT-RTE-setup-skills](runtime.md#rt-rte-setup-skills), [RT-CLM-writer-contract](runtime.md#rt-clm-writer-contract) |
| Other CLI functions / prompt paths | `tools/research_wiki.py`, `.claude/skills/novelty/SKILL.md`, `.claude/skills/exp-pilot-eval/SKILL.md`, `.claude/skills/paper-plan/SKILL.md`, `.claude/skills/review/SKILL.md` | CLI names inventoried; query/projection/maturity/backfill bodies and standalone novelty/pilot/review/writing procedures not fully inspected. Their exact evaluator criteria and all downstream publication checks remain unassessed; no system-wide absence of acceptance, derivation or withdrawal is claimed. |
| Translation and activation alternatives | `i18n/` | Setup supplied, language equivalence unassessed; conclusions about active English bodies do not prove all language surfaces equivalent. |

Missing evidence and prevented conclusions: no populated, provenance-linked research instance establishes produced/checked/accepted claims; no run trace establishes activation or model obedience; no comparison establishes causal benefit, reviewer component effect or transfer. External provider weights, parameter updates, endpoint resolution and search quality are uninspected; see [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) and [RT-CMP-review-llm](runtime.md#rt-cmp-review-llm). Experiment raw data, reference outcomes and instantiated Hiera contracts are not supplied, preventing scientific-validity assessment. These limits do not erase inspectable compiler, integrity and continuation capacity.

Consequential warrant claims: [EPI-CLM-verdict-certainty](#epi-clm-verdict-certainty), [EPI-CLM-validated-ideas](#epi-clm-validated-ideas), [RT-CLM-sidecar-confirmation](runtime.md#rt-clm-sidecar-confirmation) and [RT-CLM-writer-contract](runtime.md#rt-clm-writer-contract). README branch claims outside this pin remain excluded as in boundary; no single knowledge-production claim is substituted for these heterogeneous routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | Paper identity, reported methods/results, summary and commentary | see record | SRC-1 `.claude/skills/ingest/SKILL.md` | Imported warrant unknown; summary fidelity unobserved |
| [EPI-OBJ-idea-hypothesis](#epi-obj-idea-hypothesis) | Proposed hypothesis, novelty/risk/failure statements | see record | SRC-1 `.claude/skills/exp-eval/SKILL.md` | No candidate instance; proposed is not accepted |
| [EPI-OBJ-experiment-results](#epi-obj-experiment-results) | Measured effects/setup and result interpretation | see record | SRC-1 `.claude/skills/exp-eval/SKILL.md` | Raw measurements and provenance unprovided |
| [EPI-OBJ-evaluation-receipt](#epi-obj-evaluation-receipt) | Execution/result/status claims and numeric score | see record | SRC-1 `tools/hiera/evaluator.py` | Status success is not scientific success |
| [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) | Selected retained summaries/relation labels; no new warrant | see record | SRC-1 `tools/research_wiki.py` | Truncation can omit reasons and qualifications |
| [RT-OBJ-task-contract](runtime.md#rt-obj-task-contract) | Mostly non-truth-apt execution policy; snapshot/digest assertions | see record | SRC-1 `tools/hiera/contract.py` | Objective and evaluator validity remain external |
| [RT-OBJ-writers](runtime.md#rt-obj-writers) | None as authorization commands; declarative policy | see record | SRC-1 `runtime/policy/writers.yaml` | Not a scientific evaluator or runtime permission gate |

## Authority-route ledger

Each row is a consequential function, not an inferred successful episode. Repeated mechanism fields refer to the owning record. No observed operation is asserted. Textual scientific transformations remain indeterminate unless their inputs and relation are established; an unobserved model proposal is not automatically classified as ampliative merely because entailment is unproved.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) | content transformation | doctrine only | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | truth-apt transformation: acquisition/import | External papers/metadata into wiki | Source interpretation and enrichment; see record | Requested ingest | Imported source claims plus interpretation | Prompt-mediated writing | Source warrant unknown, not validated by import | Allows later use of retained claims | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `.claude/skills/ingest/SKILL.md` | none | none | Import is distinct from new commentary; interpretation fidelity unobserved. |
| [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) | content transformation | doctrine only | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | truth-apt transformation: indeterminate | Summary/My take and later answer | Foreground model; see record | Ingest or ask synthesis | Candidate summaries/answers | Advisory answer; optional authorized write | Neither source truth nor entailment checked by storage | Can answer before crystallization approval | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `.claude/skills/ingest/SKILL.md` | none | none | Need concrete inputs/outputs to separate faithful reshaping, inference and conjecture. |
| [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) | retention | implemented | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | no content change | Persisted pages/edges | Filesystem/helper shape checks; see record | During writes | Available later candidates | Persistence, not acceptance | None added by retention | Retained candidates become readable | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `tools/research_wiki.py` | none | none | Direct writes and browser route can bypass skill gates. |
| [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) | content transformation | implemented | [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) | truth-apt transformation: non-ampliative reshaping | Selected metadata/context to brief | Fixed budgets, connectivity, field extraction | Rebuild/compile | Selected/truncated pack | Selection/omission only | No added endorsement; lossy carrier | Changes available short context | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `tools/research_wiki.py` | none | none | Semantic completeness not guaranteed, original pages still reachable. |
| [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) | operational admission/selection/consumption | doctrine only | [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) | no content change | Relevant full pages for ask | Model relevance; top K <=15 | Later ask | Selected pages and cited answer | Advisory knowledge use | Source warrant remains unknown | Permits synthesis; crystallize separately gated | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `.claude/skills/ask/SKILL.md` | none | none | No observed operation. |
| [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake) | operational admission/selection/consumption | implemented | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | no content change | Paper intake selection | Model high-confidence instruction; CI branch | Scheduled/manual auto-ingest | Possible committed wiki/raw changes | CI writeback wired; per-paper judgment prompted | Selection not truth acceptance | Can ingest without per-paper human approval | CI/action -> retained wiki -> future agent; permissive, later sessions | SRC-1 `.github/workflows/daily-arxiv.yml` | none | none | Provider-compatible alternative is inform-only; model compliance unobserved. |
| [EPI-RTE-wiki-check](#epi-rte-wiki-check) | check/evidence production | implemented | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | no content change | Representation consistency/quality heuristics | see record | Requested lint | Issue list | Advisory diagnostics | Only checked structural predicates | No universal rejection of wiki use | Caller via issues; advisory, maintenance call | SRC-1 `tools/lint.py` | none | none | No observed operation. |
| [EPI-RTE-wiki-repair](#epi-rte-wiki-repair) | content transformation | implemented | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | truth-apt transformation: indeterminate | Defaults and reverse links | see record | Fixer call without dry-run | Changed fields/links | Filesystem mutation | Schema consistency, not scientific truth | Can change later metadata and relation use | Future readers via pages; permissive, until edited | SRC-1 `tools/lint.py` | none | none | Reverse completion may be entailed under schema assumptions; default values need not be true. |
| [EPI-RTE-edge-dedup](#epi-rte-edge-dedup) | lineage/freshness/recovery | implemented | [EPI-OBJ-paper-pages](#epi-obj-paper-pages) | truth-apt transformation: non-ampliative reshaping | Duplicate relation rows | First canonical triple; see record | Explicit cleanup | Later duplicate evidence removed | Enforcing within cleanup | No adjudication of conflicting evidence | Changes surviving graph evidence | Graph readers via JSONL; enforcing survival, persistent | SRC-1 `tools/research_wiki.py` | none | none | Warrant may degrade when later evidence differs; see deduction below. |
| [EPI-RTE-verdict-check](#epi-rte-verdict-check) | check/evidence production | doctrine only | [EPI-OBJ-idea-hypothesis](#epi-obj-idea-hypothesis) | truth-apt transformation: indeterminate | Hypothesis versus result portfolio | see record | After experiment collection | Verdict/concerns | Advisory until disposition | Conditional judgment, not an oracle | Proposes changed reliance/next tests | Foreground via reviewer text; advisory, current verdict | SRC-1 `.claude/skills/exp-eval/SKILL.md` | [EPI-CLM-verdict-certainty](#epi-clm-verdict-certainty) | Agreement does not establish calibrated certainty | No actual evidence-consuming check instance supplied. |
| [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition) | disposition/acceptance | doctrine only | [EPI-OBJ-idea-hypothesis](#epi-obj-idea-hypothesis) | no content change | Acceptance/rejection for linked hypothesis use | see record | After verdict; confirmation unless auto | Validated/failed/unchanged | Prompt-level permission; lifecycle shape code | Acceptance specified for supported main single-hypothesis case only | May unlock paper planning or avoid failed idea | Foreground via verdict/status; permissive, later research | SRC-1 `.claude/skills/exp-eval/SKILL.md` | [EPI-CLM-verdict-certainty](#epi-clm-verdict-certainty) | none | Status transition cannot prove evidence was consumed; direct metadata path bypasses it. |
| [EPI-RTE-verdict-integrate](#epi-rte-verdict-integrate) | lifecycle integration | doctrine only | [EPI-OBJ-idea-hypothesis](#epi-obj-idea-hypothesis) | no content change | Accepted supported claim into evidence graph/context | see record | After supported disposition | Supports edge and Idea updates | Requested connection and rebuild | No additional license beyond disposition | Can guide later paper/research | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `.claude/skills/exp-eval/SKILL.md` | none | none | Rejected/partial branches retain evidence separately; they are not acceptance. |
| [EPI-RTE-verdict-integrate](#epi-rte-verdict-integrate) | retention | doctrine only | [EPI-OBJ-experiment-results](#epi-obj-experiment-results) | no content change | Verdicts, rejection reasons and inconclusive evidence | see record | All verdict branches | Persisted outcome metadata | Requested write | Retention alone no acceptance | Allows failure anti-repetition and next tests | see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | SRC-1 `.claude/skills/exp-eval/SKILL.md` | none | none | No observed operation. |
| [RT-RTE-browser-write](runtime.md#rt-rte-browser-write) | operational admission/selection/consumption | implemented | [EPI-OBJ-idea-hypothesis](#epi-obj-idea-hypothesis) | truth-apt transformation: indeterminate | Caller-selected metadata replacement | see record | HTTP PATCH/direct CLI | Changed metadata | Enforcing shape/existence, not review | No truth license | Can change status without experiment acceptance | Browser/CLI -> page -> compiler/model; permissive, persistent | SRC-1 `tools/serve.py` | [RT-CLM-writer-contract](runtime.md#rt-clm-writer-contract) | none | Caller identity does not authenticate human scientific review. |
| [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search) | check/evidence production | implemented | [EPI-OBJ-evaluation-receipt](#epi-obj-evaluation-receipt) | truth-apt transformation: acquisition/import | Candidate execution and result-file score | Command evaluator, contract score path and finite-number gate | Admitted/frozen run; local or remote | Failed/success receipt | Process execution and receipt recording | License only for recorded execution/result conditions; metric validity external | Can make candidate score-eligible | Ledger -> scheduler; ranking/permissive, sidecar horizon | SRC-1 `tools/hiera/evaluator.py` | [RT-CLM-sidecar-confirmation](runtime.md#rt-clm-sidecar-confirmation) | none | Success requires zero exit/no timeout/result file/finite score, not hypothesis confirmation. |
| [EPI-RTE-hiera-summary](#epi-rte-hiera-summary) | content transformation | implemented | [EPI-OBJ-evaluation-receipt](#epi-obj-evaluation-receipt) | truth-apt transformation: entailed derivation | Counts of ledger statuses per point | see record | Status/finalize call | Counts/revision and report | Reporting only | Entailed from ledger premises; no source-truth upgrade | No direct scheduler use of experience digest | CLI/report consumer; advisory, run/report horizon | SRC-1 `tools/hiera/experience.py` | [RT-CLM-sidecar-confirmation](runtime.md#rt-clm-sidecar-confirmation) | none | Revision includes current timestamp; not a stable outcome-only identity. |
| [EPI-RTE-hiera-select](#epi-rte-hiera-select) | behavior/policy adaptation | implemented | [EPI-OBJ-evaluation-receipt](#epi-obj-evaluation-receipt) | non-truth-apt policy/content update: select next evaluation/config | Existing score/bout/config state | see record | Loop/tune call | Repeated evaluation or child variants | Code-enforced selection within these paths | Ranking has no broader scientific license | Changes next work based on results/tried configs | Scheduler -> evaluator via candidate ID; enforcing, run budget | SRC-1 `tools/hiera/scheduler.py` | none | none | No hypothesis criticism, benefit or transfer follows from numeric optimization. |

Concrete deductions from inspected implementation (not target runs):

- Given two valid edge rows with identical endpoints/type but evidence `E1` then `E2`, `dedup_edges` keeps the first canonical key and drops the second without comparing evidence. Semantic relation count is reshaped non-ampliatively, but the surviving evidence lineage loses `E2`. Malformed lines survive. See [EPI-RTE-edge-dedup](#epi-rte-edge-dedup).
- Given ledger receipts for a point with statuses `success`, `failed`, `success`, the counter increments yield attempts=3, successes=2, failures=1. This is entailed only relative to those recorded statuses; it does not entail two scientifically successful trials. See [EPI-RTE-hiera-summary](#epi-rte-hiera-summary).
- Given a failed idea with title `X` and failure_reason `R`, compiler extraction forms `- X — R`, applies the failed-section character budget and may omit/truncate it again at the pack budget. The brief's “avoid repeating” guidance therefore does not guarantee the model receives the whole failure rationale. See [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) (SRC-1 `tools/research_wiki.py`).

Additional prompt-only functions: ideation screening/ranking and refinement specify operational selection and revision, not scientific acceptance; see [EPI-CLM-validated-ideas](#epi-clm-validated-ideas). Their checks, dispositions and writes are distinct in that record. No uninspected standalone novelty or pilot criterion is inferred from these callers.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-verdict-certainty](#epi-clm-verdict-certainty) | see record | SRC-1 `.claude/skills/exp-eval/SKILL.md`, doctrine/design | see record | [RT-RTE-review-call](runtime.md#rt-rte-review-call), [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict) helper affordances; check/disposition remain doctrine | None registered | No independent reviewer comparison, calibration or experimental outcomes | Evidence-consuming acceptance procedure is specified with fatal-methodology priority and inconclusive withholding | Agreement is not sufficient evidence of high certainty; foreground reads reviewer verdict first |
| [EPI-CLM-validated-ideas](#epi-clm-validated-ideas) | see record | SRC-1 `.claude/skills/ideate/SKILL.md`, `.claude/skills/refine/SKILL.md`, doctrine/design | see record | [RT-RTE-review-call](runtime.md#rt-rte-review-call) transports model advice; wiki helpers afford writes | None registered | No novelty ground truth, exhaustive search, reviewer reliability or benefit comparison | Ranking/filtering/revision requested; no claim of accepted new science follows | Deep validation can be skipped, retained ideas are proposed, review score is not a truth oracle |
| [RT-CLM-writer-contract](runtime.md#rt-clm-writer-contract) | see record | SRC-1 `runtime/policy/writers.yaml`, doctrine/design and implementation counterpath | see record | [RT-RTE-browser-write](runtime.md#rt-rte-browser-write) | None registered | No deployed grants supplied | Writer policy does not enforce scientific acceptance | Direct metadata writes make a universal approval invariant false |
| [RT-CLM-sidecar-confirmation](runtime.md#rt-clm-sidecar-confirmation) | see record | SRC-1 `.claude/skills/hiera-experiment/SKILL.md`, `tools/hiera/cli.py`, doctrine/design and implementation | see record | [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search), [EPI-RTE-hiera-summary](#epi-rte-hiera-summary), [EPI-RTE-hiera-select](#epi-rte-hiera-select) | None registered | No evaluator validity, formal-confirmation instance or secure confinement evidence | Exploratory evaluation and report-only finalization are supported | Finite-score success is narrower than confirmation; arbitrary code is not sandboxed by cwd |

## Bounded conclusion

AutoSci specifies acquisition of literature claims and model-authored interpretation, then retains pages for later question answering, proposal generation and experiment planning. Source warrant is unknown rather than upgraded by ingestion. Compiler and cleanup routes demonstrably reshape retained carriers; they do not evaluate scientific truth and can remove qualifications or later evidence. See [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle), [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) and [EPI-RTE-edge-dedup](#epi-rte-edge-dedup).

Its strongest inspected scientific-acceptance design is hypothesis evaluation against experiment/sibling results, with methodological criticism, conservative disagreement handling, interactive veto (omitted in auto), and withholding on inconclusive evidence. Supported main single-hypothesis results may license validated status and paper planning; rejected results license failed status plus concrete anti-repetition memory. Accepted supported claims are then meant to acquire evidence edges and derived-context connections. Those phases are separately specified, not observed accepted ampliative knowledge. No supplied instance establishes what new proposition was conjectured, whether it followed from its premises, or whether a check accepted it. See [EPI-RTE-verdict-check](#epi-rte-verdict-check), [EPI-RTE-verdict-disposition](#epi-rte-verdict-disposition) and [EPI-RTE-verdict-integrate](#epi-rte-verdict-integrate).

Automated integrity checks license representation-level conclusions only; deterministic repairs do not accept the truth of filled defaults or reverse relations. Direct/browser metadata writes also permit operational status changes without the experimental procedure. Consequently status alone cannot authenticate acceptance history. See [EPI-RTE-wiki-check](#epi-rte-wiki-check), [EPI-RTE-wiki-repair](#epi-rte-wiki-repair) and [RT-RTE-browser-write](runtime.md#rt-rte-browser-write).

Hiera implements contract-bound execution, finite-score receipts, reporting and result-directed continuation. Receipt counts are entailed within the recorded ledger domain, not from independently warranted scientific premises. Scores and tried-config history can change what runs next without producing a truth-apt explanatory theory. Report-only finalization explicitly withholds formal wiki promotion. The experience revision itself is not the inspected loop's selection signal. See [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search), [EPI-RTE-hiera-summary](#epi-rte-hiera-summary) and [EPI-RTE-hiera-select](#epi-rte-hiera-select).

Localized scientific hypothesis criticism/iteration is specified separately from learning benefit or reflection on AutoSci itself; see [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict) and [EPI-RTE-verdict-check](#epi-rte-verdict-check). Implementation supports independent narrower capacities, but no observed activation, causal improvement, calibrated certainty or system-wide verdict follows. Uninspected novelty/pilot/publication paths prevent a complete negative about other acceptance routes. External distributed-parametric state remains independently unresolved, not proof of either weight learning or fixity; see [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) and [RT-CMP-review-llm](runtime.md#rt-cmp-review-llm).

## Shared records

### Operative objects

#### EPI-OBJ-paper-pages
Label: Paper pages

Natural-language paper claims, method/result summaries and My take, with symbolic identity/importance/link metadata in Markdown under wiki/papers. The paper import interpretation is distinct from [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) (derived selected carrier), not a duplicate. SRC-1 `.claude/skills/ingest/SKILL.md`, doctrine/design. No populated page instance or provenance-linked acceptance supplied.

> **Experiment & Results** — setup, primary metrics, and results in one place. Do not stop at "they beat the baseline"; cite the numbers and their conditions.
> --- `.claude/skills/ingest/SKILL.md`

#### EPI-OBJ-idea-hypothesis
Label: Idea hypothesis

Natural-language Hypothesis, Approach sketch, Risks and Novelty argument in wiki/ideas Markdown, plus symbolically consumed lifecycle metadata. Scope is the scientific candidate and changed reliance, not the [RT-OBJ-task-contract](runtime.md#rt-obj-task-contract) execution policy or [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) copy. No counterpart among supplied object records. Source: SRC-1 `.claude/skills/exp-eval/SKILL.md`, doctrine/design.

> - `## Hypothesis`, `## Approach sketch`, `## Risks`, `## Novelty argument`
> --- `.claude/skills/exp-eval/SKILL.md`

#### EPI-OBJ-experiment-results
Label: Experiment results

Natural-language setup/results/interpretation and numerical metric claims retained in experiment Markdown. Numerical values are symbolic measurements when consumed as metrics; prose interpretation remains natural language. They feed hypothesis judgment, distinct from idea hypotheses and sidecar receipts; no supplied object counterpart. SRC-1 `.claude/skills/exp-eval/SKILL.md`, doctrine/design; no measurement instance supplied.

> - `metrics` and full `## Results` section
> --- `.claude/skills/exp-eval/SKILL.md`

#### EPI-OBJ-evaluation-receipt
Label: Evaluation receipt

Symbolic JSON ledger receipt: execution status, score/direction, result digest and result-file data. Sidecar filesystem/ledger substrate; arbitrary result payload semantics are evaluator-defined, not automatically natural-language knowledge. Distinct from [RT-OBJ-task-contract](runtime.md#rt-obj-task-contract) (instructions and frozen policy) and [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) (wiki text). SRC-1 `tools/hiera/evaluator.py`, implementation. Available receipt schema is not an observed receipt instance.

> self.ledger.set_status(candidate_id, "evaluated", last_attempt_id=attempt_id, last_depth=depth)
> --- `tools/hiera/evaluator.py`

### Routes

#### EPI-RTE-wiki-check
Label: Wiki integrity and quality checks

No identical supplied route referent: the [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) container describes ingest/use, not this maintenance function.

The lint function collects missing-field, broken-link, orphan, field-value, conditional-required-field, target, reverse-reference, edge, citation and content-quality issues. This checks representation consistency and selected heuristics, not whether scientific assertions are true.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Issue objects/report to caller.
- Later read-back: inapplicable — checks alone do not retain or reload candidates; a separate fixer consumes issues.
- Delegated visibility: Local caller sees issue category and structured data; no provider is required for these checks.
- Selection predicate: All discovered pages and declared schema rules; content-quality checks use importance, maturity, references and empty sections.
- Invalidation or expiry: Issues are recomputed from current files; no semantic endorsement expiry exists.
- Activation or effect: Issues can guide the separate repair route or a person; no automatic rejection of all wiki use is established.
- Evidence limits: No lint run was supplied; regex/parser correctness and scientific truth are not established by collection of checks.

SRC-1 `tools/lint.py`; implementation.

> issues.extend(check_content_quality(wiki_dir, pages))
> --- `tools/lint.py`

#### EPI-RTE-wiki-repair
Label: Deterministic issue repair

No identical supplied route referent: the [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) container describes ingest/use, not this maintenance function.

fix_issues selects fixable issues in two categories. It adds reverse links or declared defaults, using structured issue data. This mutates representations without evaluating the underlying scientific claim. It is distinct from the preceding checker and from experiment acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: FixResult list and possibly changed Markdown.
- Later read-back: Changed fields/links can reach later page reads, compilation and subsequent lint.
- Delegated visibility: Local fixer receives structured issue data and schema-provided defaults/templates, not a review verdict.
- Selection predicate: Explicit fixer call; fixable xref-asymmetry or missing-field only; dry_run suppresses writes.
- Invalidation or expiry: Subsequent edits or repository restoration can replace changes; no automatic semantic rollback is established.
- Activation or effect: Writes are implemented when not dry-run; downstream scientific reliance is unobserved.
- Evidence limits: A reverse link/default can encode an unwarranted relation when its premise or schema is wrong; consistency is not acceptance.

Caller chooses repair/dry-run and can withhold it. Guidance is the schema and the checker issue, not an answer oracle. Trigger is requested maintenance, not a measured scientific-improvement objective. /check asks for user approval for non-deterministic suggestions; generic direct writes remain separate.

SRC-1 `tools/lint.py`; implementation.

> elif issue.category == "missing-field":
> --- `tools/lint.py`

#### EPI-RTE-edge-dedup
Label: First-occurrence edge cleanup

No identical supplied route referent: the [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) container describes ingest/use, not this maintenance function.

dedup_edges canonicalizes symmetric endpoints and keeps the first row per canonical endpoint/type triple. Later duplicate evidence is discarded even if its text differs. Malformed JSON is preserved. This is a material lineage operation, not a semantic conflict adjudicator.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts plus overwritten edges.jsonl.
- Later read-back: Later load_edges/context rebuilds read the surviving rows.
- Delegated visibility: Local filesystem caller; no model evaluator.
- Selection predicate: First canonical triple wins; duplicate evidence text does not participate in the key.
- Invalidation or expiry: Overwrites current graph; recovery requires retained repository/file history.
- Activation or effect: Changes which evidence survives for later readers; no check chooses the better evidence.
- Evidence limits: Deduction from implementation, not a target execution; bibliography cleanup uses a separate endpoint-pair key.

Caller requests cleanup and can decline it. Code decides survival; no human per-row veto or reference answer is wired. Existing add-edge admission is in [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle); cleanup is a distinct post-admission operation.

SRC-1 `tools/research_wiki.py`; implementation.

> kept.append(stripped)  # preserve malformed lines
> --- `tools/research_wiki.py`

#### EPI-RTE-verdict-check
Label: Hypothesis evidence assessment

Part of: [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict)

The foreground agent loads the idea hypothesis, current experiment results/setup and sibling outcomes. It requests a reviewer verdict on statistical significance, effect size, validity, confounds and generalization, then synthesizes a final verdict. Fatal methodology findings take priority. This is an evidence-consuming check specification, not proof it was executed.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Supported/partially_supported/not_supported/inconclusive verdict, strength, concerns and proposed status.
- Later read-back: Recorded verdict is requested in the experiment Idea updates section; retained results can enter later rounds.
- Delegated visibility: Review provider gets hypothesis, setup, full Results, key_result and sibling summary, not all source data or the whole wiki.
- Selection predicate: Named linked idea required; aggregate experiments and method concerns guide judgment.
- Invalidation or expiry: New results can lead to another verdict; no formal statistical acceptance threshold is fixed.
- Activation or effect: Advisory verdict feeds separate disposition; the adapter itself cannot update the wiki.
- Evidence limits: No supplied results, review trace or reference-answer oracle. Foreground reads the review before its own supposedly independent verdict; actual independence is unestablished.

The model proposes and synthesizes; interactive user can veto subsequent writes, auto mode omits that veto. This is open research judgment, not a benchmark oracle. Theory-builder conditions 1–4: condition 1 conclusion status: afforded (localized hypothesis sections); condition 2 conclusion status: claimed (verdict requested against their content); condition 3 conclusion status: claimed (methodological criticism and changed reliance requested); condition 4 conclusion status: claimed (sibling results and further experiments requested). Addressability is page/section-level; persistence is requested across experiment rounds/sessions. Learning benefit, reflection on AutoSci method, autonomous theory building and exercised self-improvement are uninspected independently.

SRC-1 `.claude/skills/exp-eval/SKILL.md`; doctrine/design.

> **Fatal findings take priority**: if either party finds a methodological issue (data leakage, unfair comparison), that finding takes precedence
> --- `.claude/skills/exp-eval/SKILL.md`

#### EPI-RTE-verdict-disposition
Label: Verdict-dependent reliance decision

Part of: [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict)

After the check, user confirmation is requested unless auto. Supported may advance a single-hypothesis idea whose main experiment this is to validated; partial leaves lifecycle unchanged; not_supported requests failed with concrete failure_reason; inconclusive leaves status unchanged. The intended use is subsequent research and possible paper planning, scoped to the linked hypothesis/evidence portfolio. No software proof of scientific validity follows from the status.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Planned/authorized status and relation changes, terminal report.
- Later read-back: Retained status and failure_reason can affect later ideation and paper planning.
- Delegated visibility: Foreground agent consumes final verdict; user sees planned changes unless auto.
- Selection predicate: Verdict branch and main-experiment/single-hypothesis qualification; user may withhold confirmation.
- Invalidation or expiry: Later edits/results can change reliance; transition helper restricts some transitions but direct set-meta bypasses it.
- Activation or effect: Prompt-level permissive decision to change reliance; transition code only checks lifecycle/preconditions.
- Evidence limits: No accepted claim instance is supplied. The word validated names a requested status, not demonstrated generalization.

Model proposes/decides branch; human veto exists only on interactive path. Proposal guidance is the verdict and methodological concerns. Rejection leaves status unchanged or marks failed; recovery is further experiments/manual edits, not a transactional multi-file rollback. No expected-answer oracle is supplied.

SRC-1 `.claude/skills/exp-eval/SKILL.md`; doctrine/design.

> 1. **Do not modify idea status**: insufficient evidence to make a judgment
> --- `.claude/skills/exp-eval/SKILL.md`

#### EPI-RTE-verdict-integrate
Label: Post-verdict wiki connection

Part of: [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict)

Following disposition, supported/partial branches request supports edges, rejected hypotheses request invalidates edges and concrete failure reasons; all paths record Idea updates and rebuild derived context. This is intended post-acceptance integration for supported cases, and retained rejection/evidence bookkeeping for other branches. It does not retroactively turn every retained idea into accepted knowledge.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Updated experiment/idea pages, evidence edges, rebuilt context and log.
- Later read-back: Later ask, ideate, research and paper-plan reads can consume status/edges/reasons.
- Delegated visibility: Foreground writer receives the verdict; downstream compiler exposes selected fields, often omitting the full reasoning.
- Selection predicate: Disposition branch determines supports/invalidates; all paths record verdict metadata.
- Invalidation or expiry: Derived brief is overwritten; source pages persist until edited; no automatic withdrawal propagation to every prose claim is established.
- Activation or effect: Connects disposition to retrievable pages and relationship summaries; actual behavioral dependence unobserved.
- Evidence limits: Integration is doctrine; helper availability supports only physical write capacity. Partial and rejected retention must not be classified as acceptance.

Admission owner and veto are those of disposition; graph helper rejects some malformed edges, not false evidence. Guidance and persisted content are branch-specific verdict, key_result and failure_reason. Recovery is subsequent explicit edits/rebuilds.

SRC-1 `.claude/skills/exp-eval/SKILL.md`; doctrine/design.

> **Fill in the `## Idea updates` section of the experiment page** (records changes to the linked idea, not a separate claim entity):
> --- `.claude/skills/exp-eval/SKILL.md`

#### EPI-RTE-hiera-summary
Label: Receipt counts and report derivation

Part of: [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search)

build_snapshot groups ledger evaluations by candidate point_id and counts attempts plus success versus other statuses. It derives timestamped/digested symbolic summaries. Success here is an evaluator status, not confirmation of the scientific hypothesis. CLI status/finalize consume the revision digest, not the full per-point counts; coverage_scores is separately printed as advisory coverage.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Point counts and revision; status/finalize expose revision and coverage, finalizer writes FINAL_REPORT.json.
- Later read-back: Later status/finalize recompute from persisted ledger; final report can be read by caller.
- Delegated visibility: Local CLI sees counts/digest; no model receives a scientific explanation automatically.
- Selection predicate: Evaluation receipts with a string point_id; status equal to success selects successes, everything else failures.
- Invalidation or expiry: Recomputed with updated_at, so revision can change without changed outcomes; ledger remains the source.
- Activation or effect: Implemented reporting, not an automatic wiki acceptance or policy gate.
- Evidence limits: No observed receipts. Counts are entailed only relative to ledger statuses, not evidence that commands or benchmarks were honest.

SRC-1 `tools/hiera/experience.py`; implementation.

> row["successes" if receipt.get("status") == "success" else "failures"] += 1
> --- `tools/hiera/experience.py`

#### EPI-RTE-hiera-select
Label: Score-directed continuation and config search

Part of: [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search)

choose_deep_candidate requires finite best_score and fewer than max bouts, orders by objective direction, bouts and ID, records a TUNE decision or returns STOP. cmd_loop consumes that decision and calls evaluate on the same candidate at deep depth. Unlike cmd_tune, loop does not materialize config variants. cmd_tune separately proposes bounded Cartesian configs excluding tried digests and evaluates immutable children.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: TUNE/STOP decision, subsequent evaluation receipts or tuned children.
- Later read-back: Ledger scores/bouts and tried configs are loaded by later loop/tune invocations.
- Delegated visibility: Executor receives selected candidate ID/config; no explanation-bearing theory criticism is required.
- Selection predicate: Finite best score, bout/budget limits and objective direction; tuning uses schema and deterministic enumeration.
- Invalidation or expiry: Changed receipts affect eligibility/order; exhausted budget or STOP ends continuation.
- Activation or effect: Enforcing code selection within loop; best score ranks operational priority, not scientific warrant.
- Evidence limits: No run or benchmark contract instance. Coverage priority and experience revision are reported but not the inspected loop selector.

Author/user supplies candidate/contract; admission and approval controls are in [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search). Code chooses continuation, caller can stop or change permitted run arguments. No oracle is supplied by finite scores. Config changes persist as children; source/contract integrity failures reject evaluation. Theory content of candidate code is not determinable without an instance; scores alone establish neither content-directed criticism nor improved future capacity.

SRC-1 `tools/hiera/scheduler.py`; implementation.

> if not finite_number(record.get("best_score")):
> --- `tools/hiera/scheduler.py`

The Hiera evaluator's success gate and consequence, supplementary implementation evidence for [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search) and [EPI-RTE-hiera-select](#epi-rte-hiera-select):

> if execution.get("returncode") == 0 and not execution.get("timed_out") and result_file.is_file():
> --- `tools/hiera/evaluator.py`

> "status": "success",
> "score": float(score),
> "result": data,
> "result_digest": sha256_file(result_file),
> --- `tools/hiera/evaluator.py`

The scheduling consumer and variant generator are different operations:

> receipt = evaluator.evaluate(decision["candidate_id"], "deep")
> --- `tools/hiera/cli.py`

> configs = propose_configs(schema, parent.get("config", {}), tried, args.limit)
> --- `tools/hiera/cli.py`

> if canonical_digest(config) in tried:
>     continue
> --- `tools/hiera/tuner.py`

Reporting does not imply experience counts are the selection policy:

> summary["experience_revision"] = build_snapshot(ledger)["revision"]
> --- `tools/hiera/cli.py`

### Claims

#### EPI-CLM-verdict-certainty
Label: Agreement and hypothesis support

Part of: [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict)

This claim is a doctrine part of the research route (cross-kind containment): exp-eval specifies high certainty on reviewer agreement and supported main single-hypothesis transition to validated. Distinct from [RT-CLM-sidecar-confirmation](runtime.md#rt-clm-sidecar-confirmation), which concerns exploratory versus confirmatory paths. SRC-1 `.claude/skills/exp-eval/SKILL.md`, doctrine/design. The claim's target is support for a named idea from a portfolio, not universal benchmark correctness. The procedure asks for evidence consumption but supplies no executed verdict or calibration evidence. Agreement alone does not warrant high certainty, especially when the foreground reads the other verdict before forming its own.

> **Both agree** (same verdict): use that verdict, high certainty
> --- `.claude/skills/exp-eval/SKILL.md`

> If the idea covers a single hypothesis and this experiment is the main experiment block, transition the idea to `validated`:
> --- `.claude/skills/exp-eval/SKILL.md`

#### EPI-CLM-validated-ideas
Label: Validated ideas and review-driven refinement

No counterpart among supplied claim records: this is candidate novelty/feasibility/ranking and artifact refinement, not writer ownership or formal sidecar confirmation. SRC-1 `.claude/skills/ideate/SKILL.md` and `.claude/skills/refine/SKILL.md`, doctrine/design. The caller claims filter/deep validation and writing of validated ideas, but outputs proposed status and permits skip-validation/default priority. It specifies first-pass feasibility/search/banlist checks; disposition eliminates low-feasibility similar work or known-failure-correlated ideas, then ranks survivors using novelty and review scores. Interactive user can adjust/veto; auto delegates. These are proposal-selection criteria, not acceptance of hypothesis truth. Expected-answer oracle: none supplied; web similarity and reviewer advice are not an exhaustive novelty oracle. Full standalone novelty procedure uninspected.

> Write the validated ideas to the wiki (including eliminated ideas, with their elimination reasons recorded).
> --- `.claude/skills/ideate/SKILL.md`

> (Skip if `--skip-validation`: proceed directly to Phase 4: Write to Wiki with default priority = 3 for all survivors.)
> --- `.claude/skills/ideate/SKILL.md`

> **Write top ideas** (status: proposed):
> --- `.claude/skills/ideate/SKILL.md`

Refinement separately specifies reviewer checking, score/verdict termination, direct artifact fixes and wiki relation changes, while experimental-data/domain-expert requirements remain unresolved. Author model interprets advice; artifact/wiki edits persist and rebuilds expose them to future readers. This is policy/content adaptation requested in prompts, not an implemented scientific verifier or an observed improvement. Guidance is reviewer weaknesses; no automatic rollback of incorrect edits is established. It is not evidence of revising AutoSci's own methodology: selected artifacts may be external work products.

> **Category D — Out of scope (skip):**
> - Requires new experimental data → cannot resolve in refine loop
> - Requires domain expert judgment → mark as unresolved
> - → Record in `unresolved_issues`
> --- `.claude/skills/refine/SKILL.md`

> **Target score reached**: `score >= target-score` → terminate, output final report
> --- `.claude/skills/refine/SKILL.md`
