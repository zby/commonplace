---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AREX-Skill's repository-skill verification, repair, managed import and Researcher handoff workflow."
run-id: AAS-2026-10-19-arex-skill-089a5ed7476f-01
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill workflow report

## Workflow account

This account selects the shipped `verify-repo-skill` workflow: a request to verify an integrated repository-skill draft, followed by repair, an import decision, and delivery for a later Researcher. It is representative of the construction-to-consumption boundary because it combines explicit input handoffs, content checks, environment-dependent rejection, and an executable deployment transaction. It does not stand for every Creator strategy or task-oriented evaluator. The workflow begins with an existing draft; creation of that draft is an upstream responsibility, not reconstructed here.

Evidence is SRC-1 at the [boundary](boundary.md)'s frozen revision. Additional inspection covers the complete `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`, the opening evaluation/self-refine and native-verification sections of its `references/evaluation-verification-and-handoff.md`, and the importer transaction and error-handling code in its `scripts/import_repo_skill.mjs`. The canonical Creator entry and its direct-construction reference were also read to distinguish generic construction from this specialized managed-repository path. Skill/reference prose supplies doctrine/design; the importer supplies implementation. No target execution or example trace was inspected. Accordingly, prescribed checks and delegation are not reported as completed operations.

### Request and responsibility transfer

The caller supplies a runtime skill directory outside the live repository collection, original repository context/evidence, coverage and sub-skill plans, review rubrics, integration notes, a backend verification plan and candidate map, prepared-environment readiness, and import policy. Missing candidate maps may be built during verification. The Creator verification workflow owns review and refinement of the integrated graph; it does not create a new graph from source in this phase. These responsibilities and the review boundary are declared by [WF-RTE-repo-verification](#wf-rte-repo-verification).

This is primarily a handoff between procedures and roles, not evidence of a mandatory separate process for every stage. The optional fresh-agent usability check is the specific isolated delegation described in the inspected reference: the delegated worker gets the draft and a test prompt without the research notes. Its result or summary returns to verification. If isolated runs are unavailable, the same agent reviews from the future user's perspective. No exact worker-launch API, context teardown, or observed isolated execution is established by that instruction.

### Verification, rejection and repair

The prescribed sequence is setup, license gate, assertion-backed usability cases, whole-skill self-refine, backend-classified native checks, static review/reporting, and router placement. Assertions precede judgment. Expected-behavior notes and `assertions.json` supply explicit grading references; native repository cases supply a separate reference for executable behavior. They are not one universal answer oracle. Native evidence is limited to selected safe cases in assigned environments, while agent judgment evaluates coverage, depth and routing. The workflow asks for focused iteration when an assertion fails, not merely an aggregate score.

Required accelerator evidence is a consequential rejection path. Missing required hardware or runtime evidence becomes `BLOCKED_REQUIRED_BACKEND`, not a passing synthetic test or ordinary skip. A partial environment handoff or required-backend block disables earlier auto-import authorization. The agent must expose the exact remaining limitation and obtain a new informed manual decision; alternatively it must verify the backend or explicitly narrow scope. High/critical failures must be fixed or explicitly accepted. These are model-interpreted workflow gates, not demonstrated checks performed by the importer. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`.

The verification agent repairs content when wrong or thin and repeats focused checks. An environmental/native failure is not automatically blamed on the skill. Runtime instructions, references and helpers remain separate from test cases, grading notes and verification reports. Thus later skill consumers do not automatically receive the whole review record. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md`.

### Admission and delivered result

For this specialized workflow, self-contained versioned repository/package output is routed to the managed repository collection, rather than the generic project/managed importer. Router placement requires exact taxonomy paths and non-generated repository evidence. The external classification handoff carries provenance and rationale; runtime routing JSON is a minimal projection without that rationale. If no exact family is supported, the instruction asks the user about import and requires approval before a taxonomy extension. These are declared responsibilities, not evidence of a taxonomy change in this run. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`.

Default admission asks the user; auto-import is permitted only when the original request delegated it and final verification has no unresolved disqualifying failures. Overwriting an existing unrelated target still requires separate approval. The agent supplies the external runtime tree and classification file to [RT-RTE-repo-import](runtime.md#rt-rte-repo-import). The importer performs structural/provenance admission, not an independent replay of the agent's usability or accelerator tests. Caller control of flags does not authenticate the human decisions prescribed above.

The importer owns deployment recovery. It copies into a transaction directory, validates, backs up existing skill/router/index state, installs and validates the target, and calls the router updater. A failure after mutation starts triggers restoration attempts; failed restoration retains recovery artifacts and reports their location. Existing-target rejection without `--overwrite` is separate from post-mutation recovery. These source-level branches establish best-effort recovery, not process-crash atomicity or observed restoration. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`.

Delivery has two bounded outcomes. Verification can return an explicitly-not-verified draft with coverage, native results and unresolved limitations. Successful import returns installed/routed status, with final reports outside the runtime tree. A new Researcher session is then the prescribed consumer, not a continuation that runs the downstream task inside Creator. [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) establishes how loaded guidance can reach that later model. Import success does not prove a later session occurred, that the model used the guidance, or that the downstream research succeeded.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-repo-verification
Label: Repository skill verification

This route runs from a caller's integrated external draft and verification inputs to a revised or explicitly-unverified graph, external review artifacts, and an admission decision. The Creator verification agent owns candidate selection, grading, repair and reporting; a user can authorize import or accept disclosed limitations. Distinct from [RT-RTE-repo-import](runtime.md#rt-rte-repo-import), this route establishes readiness and prepares the handoff before the executable import transaction. It applies the construction policy delivered by [RT-BAP-creator-guidance](runtime.md#rt-bap-creator-guidance), but does not duplicate that instruction-delivery referent. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md`.

> When subagents or isolated runs are available, run at least one fresh agent against the draft skill with no access to your research notes. Ask it to complete a test prompt using the generated skill and save or summarize the result. If isolated runs are not available, review from the perspective of a future agent that can only read the generated skill files.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md`

> If any assertion fails or the qualitative review reveals a gap, revise the generated skill before finishing and repeat the focused check.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md`

> A partial
> environment handoff or required-backend block disables auto-import even if
> the original request delegated it. Present the exact limitation and require
> a new informed manual import decision after final verification.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`

- Immediate return: verification handoff naming runtime/artifact paths, coverage, repairs, native results, gaps and import readiness; optionally an approved import invocation.
- Later read-back: revised operating guidance can persist through managed import for later Researcher sessions; review artifacts remain external, and their later use is uninspected.
- Delegated visibility: optional fresh agent receives draft guidance and test prompt without research notes; verifier receives saved or summarized results. Exact execution-frame implementation is uninspected.
- Selection predicate: user focus, coverage matrix, assertion-backed cases, safe native candidates, backend requirements and assigned prepared environments govern prescribed checks; taxonomy placement requires repository evidence.
- Invalidation or expiry: failed assertions or coverage gaps trigger revision and focused rechecking; partial environment evidence invalidates auto-import authorization; no timed expiry is specified in the inspected workflow.
- Activation or effect: instructions request graph revision, external report production and conditional import; no observed revision, isolated run or downstream activation is established.
- Evidence limits: doctrine/design only for verification behavior; no supplied grades or runs inspected, and native-run helper implementation and later portions of the verification reference were not inspected.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Operating mode: explicit bounded verification of an existing draft, not a recurring automatic trace-fed update. Guidance is natural-language procedure; assertions and routing metadata have symbolic consumers where tooling is used, but comprehensive automated grading is not established. The agent proposes repairs and decides readiness under the prescribed checks. User decisions govern default admission and disclosed exceptions. Assertion files/expected notes and native cases provide local reference outcomes, not a general scientific-validity oracle. Guarantee owner: verification agent following the workflow. Guarantee strength: policy. Persisted changes are operating guidance and external verification records, not model-weight updates. Content refinement alone does not establish a formulated-theory criticism cycle or improved future capacity.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-repo-import](runtime.md#rt-rte-repo-import)

Workflow role: this is the deployment transaction after verification and final admission, not the verifier's answer oracle. Its success boundary is installed skill plus router availability; downstream delivery remains a later Researcher load. Recovery ownership transfers from the verification agent's content repair to the importer's filesystem restoration attempts. Failure can return control to the caller with preserved artifacts rather than a delivered usable skill. The inspected transaction supports the baseline's best-effort characterization. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`.

> if (mutationStarted) {
> const rollbackErrors = rollbackImport({ targetDir, targetBackup, routerDir, routerBackup, routerExisted, indexPath, indexBackup, indexExisted });
> if (rollbackErrors.length > 0) { preserveTransaction = true; throw new ImportError(`${error instanceof Error ? error.message : String(error)}; rollback failed:\n${rollbackErrors.join("\n")}\nRecovery artifacts remain at ${transactionDir}`); }
> }
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`
