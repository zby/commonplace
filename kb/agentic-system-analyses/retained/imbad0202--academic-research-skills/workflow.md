---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "academic-research-skills workflow account: full research-to-manuscript production, author-scoped revision, re-review and final delivery."
run-id: AAS-2026-10-17-academic-research-skills-6fe859d62c16-01
reviewed-boundary: "060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a"
---

# academic-research-skills workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is `/ars-full` starting without research materials, taking a first-review Minor/Major decision through revision and contract re-review, then final integrity and formatting. This is selected because it follows the package's declared end-to-end product and exposes its consequential divisions of responsibility: the orchestrator dispatches, specialized roles produce and judge artifacts, the author authorizes changes, and helper calls check selected artifact contracts. It is a source-supported possible route, not a reconstructed successful session. Screening is a separate workflow and is not joined into this trace. See [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch) and [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages).

The frozen source and exclusions are those in [the boundary](boundary.md). Additional SRC-1 inspection covers `academic-pipeline/SKILL.md` stage, checkpoint and handoff sections and `academic-pipeline/agents/pipeline_orchestrator_agent.md` revision sequencing, three-gate re-review and submission-package procedures. These are **doctrine/design** evidence. Searches also located final-output pre-check and terminal-state instructions in those files. No target code, example, test, host or service was executed. This account does not independently audit the revision apply, synthesis checker or package verifier implementations; statements about their required use and rejection behavior below characterize the shipped protocol. Runtime records supply the inspected adapter/helper evidence and their limits.

### Request, production and first verification

1. **Enter and agree the plan.** The user requests the full workflow. Command loading supplies pipeline instructions to the foreground model; Pi transforms input rather than executing the pipeline. The orchestrator classifies the supplied materials, recommends modes and obtains confirmation. Starting empty selects Stage 1. Actual scheduling and model inference belong to the external host, not this repository. [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch), [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages).
2. **Research to writing.** The orchestrator loads `deep-research` in the selected mode. Its handoff to Stage 2 supplies the research-question brief, methodology blueprint, bibliography and synthesis. `academic-paper` consumes those outputs and produces the draft; the pipeline reserves formatting for Stage 5. After each stage the orchestrator compiles deliverables, asks the tracker to update state and waits for the user's continuation. Thus a role result is not itself permission to dispatch the next stage. SRC-1, `academic-pipeline/SKILL.md`; [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages).

> 1. Pass the previous stage's deliverables as input to the next stage
> --- `academic-pipeline/SKILL.md`

3. **Draft to integrity to review.** The complete draft goes to `integrity_verification_agent` in pre-review mode at Stage 2.5. PASS supports proceeding to Stage 3, with a mandatory user checkpoint. FAIL invokes correction and re-verification, not a silent bypass. After three unresolved rounds the protocol requires listing unresolved items and recording the user's decision; continuation carries a partially-unverified warning. This is not equivalent to establishing PASS. Stage 3 full review returns five reports, an editorial decision and a revision roadmap. Accept routes toward final integrity; Minor/Major selects the revision route traced here; Reject offers restructuring or exit. These are model judgments and author choices, not a known-answer oracle. SRC-1, `academic-pipeline/SKILL.md`; [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages).

Mandatory checkpoints remain explicit interactions even if the user previously asked for automatic continuation. The tracker is a designated state writer, not a separately running scheduler. Persistence and optional fresh-session recovery are covered by [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery): retained passport references and ledger receipts can support resume, but host compaction or an in-session declaration does not physically remove old dialogue.

### Author authority, patch admission and rejection

At Stage 3 → 4 the review roadmap proposes changes; it does not authorize them. The orchestrator preserves it as an immutable artifact, prepares exact claim surfaces and collects explicit author choices into a separate sidecar. The writer receives the anchored draft, block manifest, roadmap, claim surfaces, complete author sidecar and exact hashes. It returns a patch and provisional response items, not an unrestricted replacement manuscript. If every item is declined, the prescribed result is a byte-identical no-op bundle round without writer/apply dispatch. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

The orchestrator owns the surrounding tool sequence: anchorize; validate authority; dispatch writer; invoke apply with all authority artifacts; run token-conservation checking and finalization; complete response fields from the apply report; append and validate the revision-evidence bundle. Only a valid continuous bundle moves forward. Token conservation and byte-preservation ratios are advisory evidence, not semantic-quality measurements. The persisted product is a revised manuscript plus its patch/report/authority chain, not an update to ARS's own prompts. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

The selected rejection path has two distinct recovery owners:

- **Invalid patch:** the orchestrator returns the structured rejection report to the writer for one re-emission under unchanged exact authority. A second failure requires re-binding, an explicit scope decision or abort. The protocol says the base remains untouched on rejection; implementation-level byte preservation is not independently established here.
- **Structural change:** a writer escalation or apply-time structural refusal stops at a mandatory author checkpoint. The author can narrow scope, explicitly expand exact scope and rebuild authority, or acknowledge the structural shape of an already-authorized patch. Shape acknowledgement does not expand authorization. Legacy full re-emission cannot count as a current evidence-bundle round.

SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

> **Apply-failure path (distinct from escalation):** a Phase 1 rejection feeds
> the structured report back for one patch re-emission against unchanged exact
> authority. If scope must change, build a new explicit sidecar first. Second
> failure → re-anchorize/rebuild bindings, narrow/expand explicit scope, or abort.
> The base is byte-untouched on every rejection.
> --- `academic-pipeline/agents/pipeline_orchestrator_agent.md`

### Re-review: evidence before persuasion

Stage 4 → 3' transfers both original and revised drafts, the immutable roadmap, author sidecar, replayable bundle, ordered patch/apply-report chain, first-round findings and reviewer cards, and response/editorial letters. These inputs have different consumers; their presence in the transfer does not mean every verifier sees them immediately. The orchestrator first hash-binds the manifest, then dispatches three sequential contract calls: criteria commitment without the revision, evidence judgment without the persuasive response, and claim matching with the letter revealed. Artifacts are persisted and linted between phases. Reviewer cards preserve the intended yardstick rather than re-running field analysis. These are requested visibility boundaries, not demonstrated host isolation; sequential inline execution cannot erase previously visible material. SRC-1, `academic-pipeline/SKILL.md`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

After the specified rebuttal, dissent and divergence passes where applicable, the orchestrator persists traceability and invokes `check_re_review_synthesis.py` before any decision surfaces. Its prescribed checks replay the bundle, match the final draft, bind the current roadmap/author pair and require trace rows to preserve the author choices. Model reviewers judge substantive satisfaction; artifact checking is not an oracle for manuscript truth. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

A pending `user_review_required` state returns the matrix and unresolved questions to the author. Answers become typed records; mandated scoped re-verification must complete; the sidecar is revised and the checker rerun. A crashed verifier is recorded as dispatch failure, not replaced by an orchestrator's substantive judgment. Manifest failure, criteria drift or synthesis mismatch instead produces a fail-closed abort with no decision. The user may repair and rerun, explicitly choose legacy mode, or abandon; silent legacy fallback is forbidden. A valid Accept/Minor goes to Stage 4.5; Major gets one final Stage 4' revision and then final integrity, with no further review cycle. Frozen previously-missed/indeterminate findings remain gate inputs on either route. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

### Final integrity, package checks and delivery

Stage 4.5 performs fresh final integrity rather than merely revisiting earlier findings. The revision cap bounds revision work; it does not establish convergence. Integrity failure again invokes correction and the bounded FAIL-loop decision procedure. A disposable-copy pre-check runs the citation finalizer and optional claim audit early enough to surface formatter refusal issues while correction remains possible; the accepted draft's bound bytes stay unchanged. Stage 5 still runs its required passes or validly reuses eligible audit results. SRC-1, `academic-pipeline/SKILL.md`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-final-output](runtime.md#rt-rte-final-output).

The mandatory Stage-5 entry checkpoint obtains explicit continuation and citation-style selection. The formatter receives the accepted draft and carried evidence/policies; working provenance remains separate from clean converted artifacts. It first produces Markdown, confirms the requested additional files and content, and uses available external converters for DOCX/PDF. An absent converter is a disclosed dependency limit, not a delivered PDF. The formatter's citation-marker refusal rules remain distinct from the later package gate. [RT-RTE-final-output](runtime.md#rt-rte-final-output).

After formatting, the orchestrator resolves `submission_package` policy, passes it explicitly to the package verifier and interprets stdout terminal signals. Advisory is the default. Under strict policy, a strict-eligible failure permits at most two formatter-fix rounds; missing required inputs/parser take a separate remediation path, not that fix loop. Content changes cannot be delegated to the formatter as formatting repairs. A fresh report is not automatically a pass: reuse must check current package, policy and input fingerprints and evaluate the re-emitted verdict. These are protocol obligations, not proof all shell conversions are mediated. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`; [RT-RTE-final-output](runtime.md#rt-rte-final-output).

> 3. **Gate on stdout tokens, NEVER on exit codes.**
> --- `academic-pipeline/agents/pipeline_orchestrator_agent.md`

Delivery has an explicit acceptance boundary. Stage 5 ends with a FULL checkpoint after the final files. The user may decline Stage 6, marking it skipped and the pipeline completed. Otherwise the orchestrator receives the final deliverables list and a selected process-history projection, produces the requested process-record language version/files and waits for terminal acknowledgement. A correction request keeps Stage 6 in progress; merely generating the manuscript or process record does not complete the protocol. SRC-1, `academic-pipeline/SKILL.md`; [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages).

Overall, coordination is artifact-specific delegation plus explicit user decisions. Its checks can reject malformed or inconsistent evidence and its prompts prescribe refusing selected outputs. Neither the presence of those checks nor the terminal state proves scholarly accuracy, independent reviewers, model compliance or successful execution. Host/tool alternate paths and Pi's prompt-level scope limits remain as in [RT-RTE-tool-scope](runtime.md#rt-rte-tool-scope).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-revision-review](runtime.md#rt-rte-revision-review)

Workflow-specific consequence: author authorization, artifact admission and substantive re-review are separate acceptance points. A patch rejection returns to the writer under the same authority; structural escalation returns to the author; a re-review abort returns to the checkpoint without a decision. None permits the orchestrator to substitute its own verification judgment. The return path retains the original draft and exact artifact chain rather than only a persuasive response letter. The inspected protocol supports these distinctions; successful recovery remains unobserved.

#### On [RT-RTE-final-output](runtime.md#rt-rte-final-output)

Workflow-specific delivery boundary: artifact production precedes the Stage-5 FULL acceptance checkpoint, and optional process-record delivery precedes terminal acknowledgement. Package freshness and current verdict are separate conditions; advisory report transcription is not another manuscript revision. Final integrity, citation-marker refusal and post-formatter package policy do not collapse into one universal quality gate.
