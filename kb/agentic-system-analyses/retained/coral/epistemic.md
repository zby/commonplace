---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "CORAL epistemic routes: task grading, shared research, grounding checks and the limits of score- and note-based reliance."
run-id: AAS-2026-10-15-coral-25e5fdab9dc4-01
reviewed-boundary: "0123dfb939b35228cf2c1fde224cd0561e727408"
---

# CORAL epistemic report

## Source-and-claim boundary

This report asks which CORAL routes supply truth-apt task or research content, check it, license reliance and affect subsequent work. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). All new inspections use SRC-1 at the frozen revision. Implementation establishes possible routes, not observed activation. No target execution, supplied run trace or causal experiment supports this report.

The public continuous-improvement claim is see [RT-CLM-agent-organizations](runtime.md#rt-clm-agent-organizations). A narrower research-grounding claim is see [EPI-CLM-grounding-check](#epi-clm-grounding-check). External source authority, actual model output, provider parameter changes, source-capture fidelity and independent reproduction are unestablished. These gaps prevent claims of reliable discovery, accepted novel knowledge or realized improvement, not the architectural positives below.

| Entry point or operation | Source path | Coverage and records / prevented conclusion |
|---|---|---|
| CLI dispatch, including hidden aliases | `coral/cli/__init__.py` | Direct read of dispatch; start/resume/eval/wait/heartbeat/validate/query routes map to supplied runtime records below. |
| Launch, tools, custom runtimes, grader imports and sandbox extensions | `coral/agent/registry.py`, `coral/agent/manager.py` | Supplied findings: [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch), [RT-RTE-machinery-admission](runtime.md#rt-rte-machinery-admission). External harness tools and parameter state remain uninspected; no universal mediation or fixed-weight conclusion. |
| Session-start hook | `plugin/hooks/session-start.py` | Direct complete read: detects installation/version and supplies skill pointers; no research-claim adjudication. Closest record: [RT-RTE-machinery-admission](runtime.md#rt-rte-machinery-admission). |
| Eval, checkpoint, daemon, feedback, migration, steering | `coral/hooks/post_commit.py`, `coral/grader/daemon.py`, `coral/agent/manager.py` | Supplied runtime plus direct daemon status/finalization read. [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission), [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution), [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback), [RT-RTE-island-migration](runtime.md#rt-rte-island-migration), [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering). |
| Revert, checkout, export | `coral/cli/eval.py` | Direct function reads; [EPI-RTE-code-selection](#epi-rte-code-selection). These alternate paths do not require a passing score. |
| Research, review, synthesis, withdrawal guidance | `coral/template/skills/deep-research/SKILL.md`, `coral/template/skills/deep-research/agents/synthesis-reviewer.md`, `coral/hub/prompts/consolidate.md` | Direct complete reads; [EPI-RTE-research-writing](#epi-rte-research-writing), [EPI-RTE-synthesis-review](#epi-rte-synthesis-review), [EPI-RTE-confidence-disposition](#epi-rte-confidence-disposition). |
| Offline grounding and note lint | `coral/template/skills/deep-research/scripts/check_grounding.py`, `coral/template/skills/create-notes/scripts/lint.py` | Direct complete reads; [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-note-lint](#epi-rte-note-lint). |
| Status filtering and graph | `coral/hub/notes.py` | Direct function reads; [EPI-RTE-note-selection](#epi-rte-note-selection). |
| Other graders, skill-creator evaluations, deduplication, link rewriting, frontend and full maintenance transformations | `examples/`, `coral/template/skills/skill-creator/`, `coral/template/skills/organize-files/`, `web/` | Available but unassessed here. These prevent a system-complete negative about all evaluation, curation or acceptance routes. Circle-packing evidence cannot stand for these evaluators. |
| Note body generation and actual reliance | External coding harness and authored run files | No observed content/provenance supplied. Concrete novel claims and their acceptance are not determinable; prompt compliance is not inferred. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw-sources](#epi-obj-raw-sources) | Imported source assertions | Saved evidence | see record | Capture fidelity and source truth unknown |
| [EPI-OBJ-research-notes](#epi-obj-research-notes) | Research claims, mechanisms, experiment interpretations | Reusable findings and planning guidance | see record | No authored instance supplied; assertion vs warranted synthesis unresolved |
| [EPI-OBJ-review-json](#epi-obj-review-json) | Per-claim support verdicts against saved text | Grounding review | see record | Template, not an observed review |
| [EPI-OBJ-attempt-score](#epi-obj-attempt-score) | Numeric task result and relative-performance classification | Machine scheduling/rank signal | see record | Depends on grader domain; not claim acceptance |
| [EPI-OBJ-attempt-feedback](#epi-obj-attempt-feedback) | Explanations, errors and trace pointers | Human/model interpretation | see record | Aggregation and task-specific omission bound what reaches consumer |
| [RT-OBJ-task-config](runtime.md#rt-obj-task-config) | None for control settings; task assertions may be truth-apt | see record | see record | Configuration validation does not validate scientific objective |
| [RT-CMP-model-endpoints](runtime.md#rt-cmp-model-endpoints) | Not determinable in opaque parameter state | see record | see record | Parameter updates/version identity remain uninspected |

## Authority-route ledger

The ledger separates check, disposition, retention and consumption. Repeated citations denote different functions of one supplied container route, not new identities. Every route below is unobserved; architectural implementation is not evidence of compliance.

Route ID: [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-attempt](runtime.md#rt-obj-attempt)
Content/update relation: no content change
Transition or check target: Candidate commit and contemporaneous shared-state snapshot
Evaluator/condition and domain: Git/checkpoint machinery, not a truth evaluator
Activation and timing: At eval before grading
Possible or observed result: Pending attempt linked to code and shared state
Implemented force: Enforcing snapshot/queue protocol
Epistemic authority and scope: Lineage only; no endorsement of checkpointed notes
Operational authority: Publishes candidate for grading regardless of knowledge quality
Behavioral-authority path: Daemon via pending JSON, enforcing admission, current attempt
Evidence source ID and local anchor: SRC-1, `coral/hooks/post_commit.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation or benefit.

Route ID: [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-attempt-score](#epi-obj-attempt-score)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Candidate task output; concrete domain: 26-circle finite numeric outputs in unit square
Evaluator/condition and domain: Configured task grader; inspected example checks shapes, NaNs, radii, boundaries and pairwise overlap with 1e-6 tolerances, then recomputes sum
Activation and timing: After pending commit checkout
Possible or observed result: ScoreBundle or timeout/crash; feasible output receives recomputed radii sum / 2.635977
Implemented force: Enforcing computation of recorded metric, not universal correctness
Epistemic authority and scope: Conditional arithmetic/check outcome for inspected implementation and input domain; benchmark truth not independently established
Operational authority: Supplies score used by ranking and stopping; no deployment gate
Behavioral-authority path: Daemon to attempt JSON then manager/model, ranking/advisory, task iterations
Evidence source ID and local anchor: SRC-1, `examples/circle_packing/grader/src/circle_packing_grader/grader.py`
Claim IDs: [RT-CLM-agent-organizations](runtime.md#rt-clm-agent-organizations)
Mismatch marker: none
Gap/limit: Not proof of global optimality, source truth, transfer, hostile-code safety or grader correctness for all tasks. No execution. Actual benchmark provenance unverified.

Route ID: [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-attempt-score](#epi-obj-attempt-score)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Relative score vs same agent previous best
Evaluator/condition and domain: Daemon _compute_status, configured minimize/maximize
Activation and timing: After completed grader; first numeric attempt counts as improved
Possible or observed result: improved / baseline / regressed; missing score crashed; timeout retained separately
Implemented force: Enforcing status assignment
Epistemic authority and scope: Relative metric classification only, not evidence-consuming acceptance of a research claim
Operational authority: Keeps finalized result even if regressed; publishes feedback
Behavioral-authority path: Attempt store to manager and querying clients, ranking/advisory, later iterations
Evidence source ID and local anchor: SRC-1, `coral/grader/daemon.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: First numeric score being improved is a counterexample to interpreting status as proved quality gain over a baseline.

Route ID: [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-attempt-feedback](#epi-obj-attempt-feedback)
Content/update relation: non-truth-apt policy/content update: score-conditioned scheduling and guidance
Transition or check target: Continuation, plateau/interval intervention and stop policy
Evaluator/condition and domain: Manager and heartbeat symbolic rules; resumed model chooses substantive response
Activation and timing: On finalized new attempts subject to stop/budget/history rules
Possible or observed result: Interrupt/relaunch with selected score/title/feedback and prompts, or stop
Implemented force: Enforcing process changes; advisory requested reflection
Epistemic authority and scope: Score licenses triggering only; it is not an oracle for true consolidation
Operational authority: Changes next prompt and process continuation
Behavioral-authority path: Manager to committing agent via resume text, enforcing launch/advisory content, future turns
Evidence source ID and local anchor: SRC-1, `coral/agent/manager.py`
Claim IDs: [RT-CLM-agent-organizations](runtime.md#rt-clm-agent-organizations)
Mismatch marker: none
Gap/limit: See supplied record for batched arrival loss and tune counter qualifications. No demonstrated model behavior or improvement.

Route ID: [EPI-RTE-research-writing](#epi-rte-research-writing)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-raw-sources](#epi-obj-raw-sources)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: External claims into saved raw/ files
Evaluator/condition and domain: Agent using host WebFetch, source authority unverified
Activation and timing: Requested research phase or later research pass
Possible or observed result: Saved source text and provenance fields
Implemented force: Natural-language requirement; no inspected enforced capture check
Epistemic authority and scope: Source warrant unknown; local file existence preserves addressability, not authenticity
Operational authority: Makes sources reachable to research writer/reviewer
Behavioral-authority path: Agent tools to raw/ then later model reads, advisory, task/run horizon
Evidence source ID and local anchor: SRC-1, `coral/template/skills/deep-research/SKILL.md`
Claim IDs: [EPI-CLM-grounding-check](#epi-clm-grounding-check)
Mismatch marker: none
Gap/limit: External fetch implementation and actual capture unobserved; no claim of lossless import.

Route ID: [EPI-RTE-research-writing](#epi-rte-research-writing)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-research-notes](#epi-obj-research-notes)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Raw sources and experiment records into findings/mechanisms/synthesis
Evaluator/condition and domain: Model judgment under research and consolidation instructions
Activation and timing: After source retrieval or consolidation heartbeat
Possible or observed result: Requested synthesis claim, cited attempts, confidence/condition, contradictions or open questions
Implemented force: Advisory model writing instructions
Epistemic authority and scope: Neither entailment nor non-entailment established without actual input/output pair
Operational authority: Writes content future planning may use
Behavioral-authority path: Writer to shared notes/index, advisory, later agents and sessions
Evidence source ID and local anchor: SRC-1, `coral/hub/prompts/consolidate.md`
Claim IDs: [RT-CLM-agent-organizations](runtime.md#rt-clm-agent-organizations)
Mismatch marker: none
Gap/limit: Possible reshaping, derivation and conjecture remain; actual paired sources and claim plus checked interpretation are needed to decide. No accepted ampliative claim established.

Route ID: [EPI-RTE-synthesis-review](#epi-rte-synthesis-review)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-review-json](#epi-obj-review-json)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Each substantive note claim relative to its cited raw text
Evaluator/condition and domain: Requested separate model reviewer; textual support domain, not independent experiment
Activation and timing: After note creation/update; high confidence requires review in doctrine
Possible or observed result: grounded / partially-grounded / inferred / contradicted / unverifiable with source quotes
Implemented force: Requested advisory verdict saved beside note
Epistemic authority and scope: Textual attribution/support only, not external truth or causal identification
Operational authority: Returns report without editing target note
Behavioral-authority path: Reviewer JSON to author model, advisory, next revision and future reads
Evidence source ID and local anchor: SRC-1, `coral/template/skills/deep-research/agents/synthesis-reviewer.md`
Claim IDs: [EPI-CLM-grounding-check](#epi-clm-grounding-check)
Mismatch marker: none
Gap/limit: Subagent execution, independence and quality unobserved; no verdict artifact supplied.

Route ID: [EPI-RTE-confidence-disposition](#epi-rte-confidence-disposition)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-research-notes](#epi-obj-research-notes)
Content/update relation: non-truth-apt policy/content update: confidence and reliance labels
Transition or check target: High-confidence research use, source decay and contradiction
Evaluator/condition and domain: Calling agent consumes review/source evidence; no automatic semantic veto
Activation and timing: After review or discovery of invalid sources
Possible or observed result: Revise, downgrade, mark superseded or needs-reverification; defer partial rewrite
Implemented force: Advisory soft gate; author owns decision
Epistemic authority and scope: Intended criterion: supported claims against cited saved sources, for research-note reliance; actual acceptance unobserved
Operational authority: Changes labels/text and proposed future reliance, not enforced reader exclusion
Behavioral-authority path: Author file edits to later readers, advisory, retained note lifetime
Evidence source ID and local anchor: SRC-1, `coral/template/skills/deep-research/SKILL.md`
Claim IDs: [EPI-CLM-grounding-check](#epi-clm-grounding-check)
Mismatch marker: none
Gap/limit: A passed review and an evidence-consuming author decision were not supplied; integration after acceptance is therefore unestablished.

Route ID: [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-notes](#epi-obj-research-notes)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Local research/raw files: link existence, metadata and review-file existence
Evaluator/condition and domain: Offline script; structural domain, heuristic numeric citation scan
Activation and timing: Only when caller invokes script; default advisory, optional --strict
Possible or observed result: Findings, counts, grounding_score and exit 0/1
Implemented force: Advisory output; enforcing caller-visible failure only with --strict
Epistemic authority and scope: Warrant for tested structure, not semantic support or review pass
Operational authority: Can tell calling agent to repair; cannot prevent direct note retention/read
Behavioral-authority path: Script stdout/JSON/exit to caller, advisory or strict failure, current invocation
Evidence source ID and local anchor: SRC-1, `coral/template/skills/deep-research/scripts/check_grounding.py`
Claim IDs: [EPI-CLM-grounding-check](#epi-clm-grounding-check)
Mismatch marker: Mechanical grounding is narrower than semantic grounding
Gap/limit: File-existence counterexample in shared record. No automatic launch/eval gate established here.

Route ID: [EPI-RTE-note-lint](#epi-rte-note-lint)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-notes](#epi-obj-research-notes)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Authored-note metadata and index conventions
Evaluator/condition and domain: Bundled lint parser/vocabulary; confirmed requires truthy evidence.verified
Activation and timing: Optional invocation; underscore/meta and raw files excluded during directory walk
Possible or observed result: Warnings and optional nonzero exit
Implemented force: Advisory by default; strict exit can signal caller
Epistemic authority and scope: Metadata consistency only, not verified experiment or truthful confirmation
Operational authority: Requests repairs, does not gate shared-file read or eval submission
Behavioral-authority path: Lint stdout/exit to author, advisory/strict caller signal, invocation
Evidence source ID and local anchor: SRC-1, `coral/template/skills/create-notes/scripts/lint.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No attempt lookup, result comparison or semantic validation in inspected confirmed branch; skip rules limit coverage.

Route ID: [EPI-RTE-note-selection](#epi-rte-note-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-notes](#epi-obj-research-notes)
Content/update relation: no content change
Transition or check target: Which authored notes appear in list/status/graph results
Evaluator/condition and domain: Parsed status string equality only when filter requested; graph follows authored links
Activation and timing: On hub query; no status filter by default
Possible or observed result: Default all collected authored notes; requested casefolded/trimmed status subset; typed graph edges
Implemented force: Enforcing requested list selection, advisory knowledge display
Epistemic authority and scope: Metadata is author assertion, not adjudicated truth or endorsement
Operational authority: Can deliver refuted/untested notes unless caller filters; supersedes edges do not themselves withdraw nodes
Behavioral-authority path: Hub list/graph result to clients/model/human, selection/advisory, future queries
Evidence source ID and local anchor: SRC-1, `coral/hub/notes.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: Not a whole-client audit; no automatic universal withdrawal conclusion. Raw captures opt in for display and are excluded by default.

Route ID: [EPI-RTE-code-selection](#epi-rte-code-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-attempt](runtime.md#rt-obj-attempt)
Content/update relation: no content change
Transition or check target: Active candidate or exported Git branch
Evaluator/condition and domain: Caller selects hash; software checks known attempt/object and branch collision, not score criterion
Activation and timing: Explicit checkout/revert/export command
Possible or observed result: Reset current code to chosen attempt/previous commit or create branch
Implemented force: Enforcing filesystem/Git change
Epistemic authority and scope: No epistemic license or deployment correctness acceptance
Operational authority: Can select/export pending, failed or inferior candidate if structural prerequisites hold
Behavioral-authority path: CLI to Git/worktree or branch, enforcing, subsequent development
Evidence source ID and local anchor: SRC-1, `coral/cli/eval.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: Separate from manager rewind/archive route. Shared notes/model session not atomically restored; export is not deployment.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and evidence layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-agent-organizations](runtime.md#rt-clm-agent-organizations) | see record | see record | see record and [EPI-RTE-research-writing](#epi-rte-research-writing) | [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution), [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback) | None supplied | No independent component intervention or later-capacity comparison | Infrastructure for experiments and sharing; not demonstrated continuous improvement | Grading a solution is not accepting its explanation or proving that sharing helped |
| [EPI-CLM-grounding-check](#epi-clm-grounding-check) | see record | see record | [EPI-RTE-synthesis-review](#epi-rte-synthesis-review), [EPI-RTE-confidence-disposition](#epi-rte-confidence-disposition) | [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-note-lint](#epi-rte-note-lint) | None supplied | Structural checks cannot identify semantic support or source reliability | Implemented link/metadata checks plus requested model review | Review file existence is not a passed review; default exit success is not acceptance |

## Bounded conclusion

CORAL commits code and checkpoints shared files before evaluation, retaining lineage rather than certifying their truth: see [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission). Its task grader can produce a bounded measurement. In the inspected circle-packing route the reported objective is recomputed from returned radii, conditional on numeric checks, rather than trusting the candidate's returned sum. The comparison status means only relative score classification; even the first numeric score is called improved. The result has real operational force through scheduling, feedback and migration, without establishing global optimality, correct explanation, replay safety or transfer: see [RT-RTE-grader-execution](runtime.md#rt-rte-grader-execution), [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback), [RT-RTE-island-migration](runtime.md#rt-rte-island-migration).

Research doctrine requests acquisition, synthesis, counter-evidence, review and revision. Imported source warrant is unknown; saved text and citations are not independent validation. The note transformation remains indeterminate without actual inputs/outputs. Model review is a substantive counterexample to treating CORAL as having only score evaluators, but it is a requested advisory textual-support check, not an observed or enforced acceptance route: see [EPI-RTE-research-writing](#epi-rte-research-writing), [EPI-RTE-synthesis-review](#epi-rte-synthesis-review), [EPI-RTE-confidence-disposition](#epi-rte-confidence-disposition). No supplied evidence establishes a produced accepted ampliative claim or post-acceptance lifecycle integration. This is a local evidence limit, not a system-wide absence claim.

The implemented grounding and lint scripts judge structure. They neither read review verdicts for pass/fail nor verify that a confirmed note matches an experiment. The note consumer can select status strings and graph authored supersession relations without treating those relations as universal withdrawal: see [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-note-lint](#epi-rte-note-lint), [EPI-RTE-note-selection](#epi-rte-note-selection). Caller-directed code checkout/export also bypasses score approval: see [EPI-RTE-code-selection](#epi-rte-code-selection).

Direct score-conditioned process adaptation is implemented independently of knowledge acceptance. Improved future capacity, successful reflection, autonomous theory criticism and exercised self-improvement do not follow merely from that route or from persistent files. No observed chain shows an evidence-responsive note/skill change entering later behavior and causing improvement. Conversely, these limits do not erase the implemented orchestration or requested evidence-sensitive review. Provider parameter changes remain uninspected: see [RT-CMP-model-endpoints](runtime.md#rt-cmp-model-endpoints). Unassessed graders and maintenance evaluators preclude a complete-system negative.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-raw-sources
Label: Raw sources

Distinct from [RT-OBJ-attempt](runtime.md#rt-obj-attempt): external source assertions captured as natural-language Markdown on the shared notes filesystem, under raw/. Requested immutable evidence, not an attempt or score. SRC-1, `coral/template/skills/deep-research/SKILL.md` supplies doctrine/design only; no actual capture inspected.

> Use `WebFetch` to get the full page, then write it to `notes/raw/`. These are immutable — never edit raw sources, only reference them from research notes.
> --- `coral/template/skills/deep-research/SKILL.md`

#### EPI-OBJ-research-notes
Label: Research notes

Distinct from [RT-OBJ-attempt](runtime.md#rt-obj-attempt): natural-language research, experiment and synthesis claims stored as Markdown in shared notes, with symbolic status/confidence/lineage metadata. Retention precedes any established acceptance. SRC-1, `coral/hub/prompts/consolidate.md` and `coral/template/skills/deep-research/SKILL.md`, doctrine/design. No counterpart in supplied runtime for the note itself.

> 2. **Synthesize.** For any topic with 3+ notes, write or update a synthesis note. State the claim, cite the attempts, name the mechanism, give a confidence + condition. See skill Variant D.1.
> --- `coral/hub/prompts/consolidate.md`

#### EPI-OBJ-review-json
Label: Synthesis review JSON

Distinct from [RT-OBJ-attempt](runtime.md#rt-obj-attempt): requested sibling `<slug>.review.json` on the shared filesystem, symbolic per-claim verdicts plus natural-language evidence passages and judgments. This is not the task grader feedback. SRC-1, `coral/template/skills/deep-research/agents/synthesis-reviewer.md`, doctrine/design.

> Save results to `output_path` in the format below. Do not modify the research note itself — the calling agent decides how to act on your verdict.
> --- `coral/template/skills/deep-research/agents/synthesis-reviewer.md`

#### EPI-OBJ-attempt-score
Label: Attempt score and status
Part of: [RT-OBJ-attempt](runtime.md#rt-obj-attempt)

Symbolic numeric score, status and budget metadata in attempt JSON; fixed code consumes them for scheduling/ranking. This part differs from explanatory feedback in consumer rules. SRC-1, `coral/grader/daemon.py`, implementation.

> if not prev_scores:
>     return "improved"
> --- `coral/grader/daemon.py`

> if score == prev_best:
>     return "baseline"
> return "regressed"
> --- `coral/grader/daemon.py`

#### EPI-OBJ-attempt-feedback
Label: Attempt feedback
Part of: [RT-OBJ-attempt](runtime.md#rt-obj-attempt)

Natural-language explanation/error/trace pointer in persisted JSON, later model/human interpretation rather than numeric comparison. SRC-1, `coral/grader/daemon.py`, implementation; consumer see [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback).

> feedback = _build_feedback(bundle)
> --- `coral/grader/daemon.py`

> feedback = _append_eval_logs_hint(feedback, attempt.commit_hash, config.agents.runtime)
> --- `coral/grader/daemon.py`

### Routes

#### EPI-RTE-research-writing
Label: Research writing

Distinct from the process-control route [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback): model-requested source acquisition and note generation, not interrupt scheduling. Owner is the foreground agent, with optional specialists. Inputs are task, saved sources and attempts; outputs are raw captures, research and synthesis notes. Source warrant and transformation semantics remain unestablished.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested saved raw source or research note, no observed return.
- Later read-back: Shared raw/notes/index files are requested to inform later research and planning.
- Delegated visibility: Shared island notes; external harness determines actual tool/context access.
- Selection predicate: Task-derived coverage gaps, evidence strength, feasibility and agent judgment.
- Invalidation or expiry: Source decay should trigger reverification; raw sources are requested immutable, no enforced expiry demonstrated.
- Activation or effect: Requested shared-file writes; subsequent reliance and benefit unobserved.
- Evidence limits: No concrete generated claim, paired input/output or independent trace supplied.

Admission is agent-authored filesystem writing without a demonstrated per-note human gate. Guidance requests source-first acquisition, cited synthesis and confidence/conditions; rejection/recovery is agent revision, not an inspected semantic validator. Operating mode is task research within optimization; no universal answer oracle. For theory-like mechanism notes, formulation is requested, but no actual localized theory instance, content-dependent consumption, blame-bearing criticism or kept criticism shaping a next round is supplied: theory-builder conditions 1–4 each have operation conclusion status uninspected. Addressability is afforded by editable claim/evidence text, not measured semantic granularity. Persistence is requested across later task sessions; learning and reflective theory-building remain unestablished, independently of the implemented outer scheduling loop.

Evidence: SRC-1, `coral/template/skills/deep-research/SKILL.md`, `coral/hub/prompts/consolidate.md`; doctrine/design.

> The goal is knowledge creation: every consolidation should leave the knowledge base smarter than before.
> --- `coral/hub/prompts/consolidate.md`

#### EPI-RTE-synthesis-review
Label: Synthesis review

Distinct from [RT-RTE-specialist-delegation](runtime.md#rt-rte-specialist-delegation): a specific content-support evaluator, not the generic librarian delegation route. Foreground author requests separate reviewer; reviewer reads note and cited raw sources, produces per-claim verdict JSON without editing the note.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested per-claim verdict report.
- Later read-back: Sibling review JSON can be read by author and checked for existence by grounding script.
- Delegated visibility: Requested note and linked raw files in a separate host-owned context; actual isolation uninspected.
- Selection predicate: Every substantive factual, methodological, comparative and causal claim; missing sources recorded.
- Invalidation or expiry: A changed note can invalidate old support, but inspected script does not compare timestamps/content hashes.
- Activation or effect: Advisory support judgment requested; no inspected executed reviewer.
- Evidence limits: Model verdict quality, full-source reading and context independence unobserved.

Author proposes the note; requested reviewer judges textual support, not experimental truth; author can decline or revise. No expected-answer oracle beyond cited passages. Mode is bounded textual support audit. Contradiction verdicts can name challenged content, but no actual criticism/revision/iteration is supplied; theory-builder conditions 1–4 operation conclusion status is uninspected for each. This is not an inferred absence of model criticism.

Evidence: SRC-1, `coral/template/skills/deep-research/agents/synthesis-reviewer.md`; doctrine/design.

> - **You don't fix anything.** Your output is read by the calling agent, which decides whether to revise the note, downgrade `confidence`, or mark `superseded`. Don't propose edits in the JSON.
> --- `coral/template/skills/deep-research/agents/synthesis-reviewer.md`

#### EPI-RTE-confidence-disposition
Label: Confidence disposition

Distinct from [RT-RTE-eval-submission](runtime.md#rt-rte-eval-submission): author judgment over research reliance rather than Git/queue admission. Author consumes review/source-decay evidence and decides revision, confidence, supersession or deferred reverification.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested changed note/labels or preserved body pending reverification.
- Later read-back: Later readers receive revised labels/text; no universal exclusion by label established.
- Delegated visibility: Shared notes plus sibling reviews, actual consumer attention unobserved.
- Selection predicate: Review support and remaining source warrant; intended use is research/planning reliance.
- Invalidation or expiry: Invalid sources should trigger needs-reverification; lost support should mark superseded rather than delete.
- Activation or effect: Advisory author decision; actual evidence-consuming acceptance not observed.
- Evidence limits: No passed review and ensuing author decision available; no post-acceptance integration inferred.

Admission trigger is completed review or source invalidation; proposed change is confidence/body/reliance metadata. Calling model decides and can veto; no software gate verifies the review passed. Recovery preserves source and note history by requested nondeletion/deferred rewrite, not a transactional rollback. Criterion is claim support against saved sources for high-confidence research use; actual acceptance decision absent from supplied evidence. Supersession here is target-native metadata, not a record-contract amendment.

Evidence: SRC-1, `coral/template/skills/deep-research/SKILL.md`; doctrine/design.

> If the note loses *all* its supporting sources, set `superseded: true` rather than deleting the file — it preserves the audit trail for future agents who might rediscover the topic.
> --- `coral/template/skills/deep-research/SKILL.md`

#### EPI-RTE-grounding-check
Label: Grounding check

Distinct from [RT-RTE-machinery-admission](runtime.md#rt-rte-machinery-admission): optional offline structural research-note evaluator, not task/runtime import validation. Caller invokes bundled script, which reads disk and returns findings and summary.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Findings/summary as text or JSON and exit code.
- Later read-back: inapplicable — script writes no retained result; a caller could save its output, but none is supplied.
- Delegated visibility: Reads supplied notes roots and local file paths; no model/provider call.
- Selection predicate: Research non-meta Markdown, raw metadata, ledgers and existence of high-confidence sibling review file.
- Invalidation or expiry: Re-run against current filesystem; no persistent endorsement or expiry state created.
- Activation or effect: Default advisory output; strict mode returns nonzero on hard categories, without removing notes.
- Evidence limits: Checks source/review existence, not source truth, actual semantic support or passed review.

Concrete static trace: research/a.md with confidence high and a valid link to raw/b.md, a raw file carrying the three required fields, and an empty a.review.json avoids unreviewed-high-confidence. The code only calls review.exists(); it does not parse a verdict. An actually contradicted claim can therefore escape hard grounding findings. This deduction uses implementation, not target execution; the heuristic citation detector can still produce advisory findings depending on body text. The caller chooses invocation/strictness and may ignore output; no semantic acceptance or automatic rollback follows.

Evidence: SRC-1, `coral/template/skills/deep-research/scripts/check_grounding.py`; implementation.

> if str(meta.get("confidence", "")).strip().lower() == "high":
>     review = note.with_suffix(".review.json")
>     if not review.exists():
> --- `coral/template/skills/deep-research/scripts/check_grounding.py`

> return 1 if (args.strict and hard_total) else 0
> --- `coral/template/skills/deep-research/scripts/check_grounding.py:358-358`

#### EPI-RTE-note-lint
Label: Note lint

Distinct from [RT-RTE-machinery-admission](runtime.md#rt-rte-machinery-admission): metadata/style check on authored notes rather than grader/config admission. CLI script owns read/parse/warning generation; author decides repair.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Warnings, count and optional strict nonzero exit.
- Later read-back: inapplicable — script does not persist certification or revise notes.
- Delegated visibility: Caller-selected local notes; underscore/meta and raw excluded from directory scans.
- Selection predicate: Frontmatter vocabulary, creator/date, path/type and index references where enabled.
- Invalidation or expiry: Re-run checks current file; metadata can change without invalidating any stored certification because none is created.
- Activation or effect: Advisory by default; strict returns failure on warning.
- Evidence limits: Truthy verified flag is not checked against attempt/source; skip rules and optional fields limit coverage.

Caller proposes/edits notes and may invoke lint; program judges metadata criteria only. A parsed confirmed note with evidence.verified true clears that branch regardless of whether an experiment actually supports its claim. This static trace demonstrates the scope of the check, not that any observed note abused it. Repair is author revision; no installed admission or withdrawal gate is established.

Evidence: SRC-1, `coral/template/skills/create-notes/scripts/lint.py`; implementation.

> if status == "confirmed":
>     verified = isinstance(evidence, dict) and bool(evidence.get("verified"))
> --- `coral/template/skills/create-notes/scripts/lint.py`

> if args.strict and total_warnings:
>     return 1
> return 0
> --- `coral/template/skills/create-notes/scripts/lint.py`

#### EPI-RTE-note-selection
Label: Note selection

Distinct from [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback): file-query visibility and graph projection, not scored process scheduling. hub list_notes collects entries, optionally filters requested status; notes_graph returns authored nodes/edges.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List or graph dictionaries.
- Later read-back: Reads shared files changed by agents across later query invocations.
- Delegated visibility: Public/island root selected by caller; raw captures opt in for list display.
- Selection predicate: Exact parsed status equality after trimming/casefold, only if supplied; graph resolves authored link targets.
- Invalidation or expiry: Current file content/paths determine future query results; no semantic freshness check.
- Activation or effect: Implemented selection and typed graph projection; consumers may interpret content but compliance unobserved.
- Evidence limits: No full downstream-client audit; status/refutes/supersedes remain authored metadata.

Concrete static text trace: statuses " Confirmed ", "refuted", and absent yield only the first under a requested "confirmed" filter; no filter returns all three. No review verdict is consulted. Graph adds both nodes and supersedes/refutes edges rather than treating an edge as automatic deletion. Thus label-based selection can affect delivered candidates without establishing epistemic acceptance.

Evidence: SRC-1, `coral/hub/notes.py`; implementation.

> if status is None:
>     return entries
> --- `coral/hub/notes.py`

> expected = status.strip().casefold()
> return [
>     entry
>     for entry in entries
>     if "status" in entry and str(entry["status"]).strip().casefold() == expected
> ]
> --- `coral/hub/notes.py`

#### EPI-RTE-code-selection
Label: Code selection

Distinct from [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering): CLI direct reset/export operations, not manager ancestry matching, archival and relaunch. Caller chooses target/branch; Git performs effect after structural checks.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated worktree or exported branch; printed diagnostic on failure.
- Later read-back: Later development reads chosen code/branch; shared-state rollback is not part of these function bodies.
- Delegated visibility: Current worktree and resolved island attempt context; export uses run repository.
- Selection predicate: Known attempt/hash and object existence for checkout/export; previous commit for revert; branch collision check for export.
- Invalidation or expiry: Caller can select another target; no score invalidation or atomic knowledge/session restoration.
- Activation or effect: Enforcing Git changes; no score/pass predicate before checkout/export.
- Evidence limits: No execution performed; exporting a branch does not establish production deployment or correctness.

Explicit command triggers caller-proposed code selection/export; caller supplies criterion, program can reject missing attempt/object or branch conflict. No task-score oracle or per-operation human identity is established. Recovery is another Git selection, not restored note/model state. This counterexample qualifies any reading of graded status as a universal code admission barrier.

Evidence: SRC-1, `coral/cli/eval.py`; implementation.

> target = attempts_file.stem  # normalized 40-char hash
> --- `coral/cli/eval.py:247-260`

> cmd += [branch, target]
> --- `coral/cli/eval.py`

### Claims

#### EPI-CLM-grounding-check
Label: Mechanical grounding claim

Distinct from [RT-CLM-agent-organizations](runtime.md#rt-clm-agent-organizations): the research skill specifically claims mechanical enforcement of saved-source grounding, alongside the requested high-confidence reviewer soft gate. SRC-1, `coral/template/skills/deep-research/SKILL.md`, doctrine/design. The implementation warrants local structural checks, not semantic entailment, authenticity or a passed reviewer verdict; see [EPI-RTE-grounding-check](#epi-rte-grounding-check).

> Never write a number, a benchmark result, or a "X beats Y" into a research note that isn't backed by a file in `raw/`. The grounding check in step 6 enforces this mechanically.
> --- `coral/template/skills/deep-research/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
