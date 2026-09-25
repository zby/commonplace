---
type: types/agentic-system-analysis-result.md
description: "AREX-Skill repository-skill construction, verification, deployment and consumption subsystem at ac3fe1af"
run-id: AAS-2026-09-25-arex-skill-01
system: "AREX-Skill"
run-date: "2026-09-25"
result-disposition: complete
target-class: "builder or improvement plane"
boundary-kind: subsystem-only
reviewed-boundary: "ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "Repository operating skills accumulated or revised through Creator construction, verification, refresh and extension; private construction handoffs/reports with later consumers; router/access metadata and managed deployment state; Researcher and documented exported-agent reads. Static imported library content establishes an admission alternative, not learning through use. Host conversation memory, paper construction and unrelated workflows are excluded."
  axes:
    storage_substrate:
      assessment: known
      basis: afforded
      values: [files]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6]
      note: "Operative stores are filesystem trees and JSON/JSONL/Markdown reports; the skill graph is links among files, not a graph database. Git is the acquisition source, not a required runtime memory store."
    representational_form:
      assessment: known
      basis: afforded
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6]
      note: "Readable instructions/reasons coexist with executable helpers, machine-consumed manifests, metadata and workflow environment fields. No opaque model-weight memory artifact is in scope."
    lineage:
      assessment: known
      basis: afforded
      values: [authored, imported, other-compiled, trace-extracted]
      records: [RTE-1, RTE-2, RTE-4, RTE-9, RTE-10, RTE-11]
      note: "Human/model authorship and imported published skills; deterministic router projections; trace-fed verification revisions and environment continuation handoffs. Trace extraction is afforded by authored model workflows, not an observed learning run."
    behavioral_authority:
      assessment: known
      basis: afforded
      values: [instruction, knowledge, routing, validation, enforcement]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, RTE-2, RTE-3, RTE-10]
      note: "Skills instruct; references/reports inform; metadata/routes select; checks and manifests validate or reject admission. Learning here produces instructions, not parametric updates or a separate learned authority."
    write_agency:
      assessment: known
      basis: afforded
      values: [automatic, manual]
      records: [RTE-1, RTE-2, RTE-4, RTE-5, RTE-9, RTE-10]
      note: "Models write and scripts derive/copy artifacts after human triggers; maintainers can edit working trees and retain local modifications under digest conflict checks."
    curation_operations:
      assessment: known
      basis: afforded
      values: [evolve, promote, decay]
      records: [RTE-4, RTE-2, RTE-9]
      note: "Revisions replace retained guidance; refresh explicitly promotes buried support routes; official updates remove upstream-deleted entries from live memory. No retained-history invalidation, semantic near-duplicate merge or novel-claim synthesis is established as a distinct operation."
    read_back_direction:
      assessment: known
      basis: afforded
      values: [pull, push]
      records: [RTE-3, RTE-5, RTE-9, RTE-10, RTE-11]
      note: "Researcher and Creator request retained files/handoffs; export affords named external agent reads. Environment continuation adds a separate push: lane startup automatically supplies the parent-selected environment fields to its checker before child-session creation. Static catalog announcement does not push accumulated memberships or skill bodies."
    read_back_signal:
      assessment: known
      basis: afforded
      values: [coarse]
      records: [RTE-10, RTE-3]
      note: "Lane startup selects a supplied environment object by presence and fixed field projection for the environment checker. Package/version comparisons validate the selected facts; they do not perform an identity match selecting stored memories. The fixed router catalog description adds no accumulated-memory push signal."
    trace_learning:
      assessment: known
      basis: afforded
      values: ["yes"]
      records: [RTE-9, RTE-10]
      note: "Authored workflows direct model writes from native/fresh-agent results into durable revised skills, and command results into persisted continuation handoffs. Neither observed completion nor causal improvement is established."
    trace_source:
      assessment: known
      basis: afforded
      values: [tool-traces, trajectories]
      records: [RTE-9, RTE-10]
      note: "Native/setup command results and fresh-agent task results supply the two trace branches; no host conversation compaction is included."
    learning_scope:
      assessment: known
      basis: afforded
      values: [per-task, cross-task]
      records: [RTE-9, RTE-10]
      note: "Environment continuation handoffs serve the current skill-building task; revised portable operating skills are expressly intended for multiple checkouts/projects/research tasks. No separate project-bound learned memory is established."
    learning_timing:
      assessment: known
      basis: afforded
      values: [staged]
      records: [RTE-9, RTE-10]
      note: "Both qualifying branches transform results at explicit preparation/verification stages before the later construction or Researcher consumer. This does not assert background learning or unconstrained updates during Researcher use."
    distilled_form:
      assessment: known
      basis: afforded
      values: [natural-language, symbolic]
      records: [RTE-9, RTE-10]
      note: "Revised prose and scripts plus machine-consumed workflowEnvironment fields and explanatory handoff text; model weights are not modified by these routes."
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-9, CLM-3]
      note: "Instructions ask for fresh-agent skill tests, but no retained executed dependence test was inspected. Native command success alone does not test reliance on recalled skills; reported aggregate benchmark improvements cannot fill this gap."
---

# AREX-Skill agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-arex-skill-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/arex-skill.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-arex-skill-01/memory-report.md`
**Memory analysis report SHA-256:** `94b575ed93aac5f899528793d7b051252e4a193ca9fbb573ee727ca794db1d35`

## Boundary and evidence

Independent code-grounded characterization of AREX-Skill's repository-skill subsystem, frozen at ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6 on 2026-09-25. Intended use: distinguish what constructs and admits reusable operating knowledge, what later loads it, and what verification warrants. Target class: builder or improvement plane; boundary-kind: subsystem-only. Includes Creator repository construction, verification, refresh/extension, managed import/install/update, portable export and Researcher role-filtered selection/loading. Host interfaces are included only where they implement those operations, including construction subagents and native verification commands.

The repository also ships a general DisCo runtime. General conversation persistence/compaction, arbitrary tool/extension behavior, paper-specific construction, new meta-skill design and unrelated dynamic workflows are excluded; these exclusions prevent whole-runtime learning, permission, reflection and reliability conclusions. The published library is not exhaustively audited: a selected graph may establish representational form but not correctness of every skill. External model/provider internals, pinned Pi dependencies and target repositories/environments are dependencies, not separately inspected evidence. Source-only allowlist is this repository at the commit; no prior review, ingest, paper or live service contributes findings. No target experiment is executed. Source-reported benchmark outcomes remain claims.

## Source register

| ID | Kind and identity/location | Revision | Evidence layer | Inspected scope and citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|
| SRC-1 | Git, `https://github.com/VectorSpaceLab/AREX-Skill`; access root `/home/zby/llm/commonplace/related-systems/VectorSpaceLab--AREX-Skill` | ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6 | Implementation | `cli/package.json`; `cli/packages/coding-agent/src/core/` selected skill/resource/managed-library and trust interfaces; `cli/packages/coding-agent/src/disco/modes/`; repository workflow scripts and `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` cited below | Code paths establish wiring, not actual model compliance, tests passing, installed dependency behavior or deployed isolation |
| SRC-2 | Git, `https://github.com/VectorSpaceLab/AREX-Skill` | ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6 | Doctrine/design | `README.md`, `docs/architecture.md`, `docs/disco-workflows.md`, `cli/docs/security.md`, bundled repository workflow SKILL.md/reference instructions and selected library content | Natural-language workflow stages require a model/operator to execute them; static files do not establish their production lifecycle |
| SRC-3 | Git, `https://github.com/VectorSpaceLab/AREX-Skill` | ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6 | Reported operation | `README.md:141-173` benchmark summary | No candidate-linked raw runs, comparison design or reproduction inspected; no observed or causal upgrade |

All evidence reads use full-commit Git blobs. The worktree and moving HEAD are not evidence. An initial overlarge create-skill read was truncated; the relevant ranges were re-read in bounded slices before use. No dynamic probe source is registered.

## Shared records

### Components

CMP-1 — DisCo host interface for this subsystem. TypeScript CLI/SDK owns resource loading, roles and helper execution; construction workflows combine natural-language SKILL.md guidance with executable scripts. It depends on pinned `@earendil-works/pi-agent-core`, `pi-ai` and `pi-tui` version 0.83.0, not an inspected implementation of those packages. Runtime/package interface conclusion status: **wired**; external dependency internals: **uninspected**. Source SRC-1 `cli/package.json:1-25,50-55`; SRC-2 `docs/architecture.md:46-65`.

>     "@earendil-works/pi-tui": "0.83.0",
>     "@silvia-odwyer/photon-node": "0.3.4",
>     "acorn": "8.16.0",
>     "chalk": "5.6.2",
>     "cross-spawn": "7.0.6",
>     "diff": "8.0.4",
> --- `cli/package.json` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


CMP-2 — External model/provider processing used by Creator, reviewers/subagents and Researcher. Distributed-parametric form; provider-managed storage is uninspected. Workflow model choice resolves explicit model/tier/session default; unresolved choice falls back with a warning. Parameter changes during operation: **uninspected** at provider boundary; exact-weight/version pinning: **uninspected**, because provider/model identifiers and package versions do not establish immutable weights. Local model selection and fallback: **wired**. No training operation is inferred from skill writes. Source SRC-1 `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts:551-591`, `cli/packages/coding-agent/src/core/agent-session.ts:1574-1592`.

> 		// Resolve a requested model spec to a Model object. A given-but-unresolved
> 		// spec falls back to the session default (with a warning) rather than failing.
> 		let resolvedModel: Model<any> | undefined;
> 		if (modelSpec) {
> 			resolvedModel = await this.resolveModel(modelSpec);
> 			if (resolvedModel) {
> 				options.onModelResolved?.(`${resolvedModel.provider}/${resolvedModel.id}`);
> 			} else {
> 				console.warn(`[workflow] model "${modelSpec}" not found; using session default`);
> 				options.onModelFallback?.(modelSpec);
> 			}
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


### Operative objects

OBJ-1 — Repository operating skill graph: root/sub-skill SKILL.md files, references and optional executable helpers. Natural-language instructions and symbolic code/metadata, persisted as files. Producer Creator or imported library; consumer Researcher or compatible external agent. Intended self-containment, source provenance, role and visibility constraints are instructions; checked subsets are on RTE-2. Source SRC-2 `cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md:138-191`; SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs:324-342`. Detailed memory annotation follows.

OBJ-2 — Construction and verification records: evidence/coverage/backend plans, usability assertions, native execution reports, self-refine notes, external routing decisions and final handoff. Natural-language and JSON files. These are deliberately separate from public runtime skill content; construction/verification/refresh consumers may read them, while ordinary skill use is not required to load them. Retained reasons and their actual consumption are distinguished in the memory records. Source SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md:12-46,125-143`.


OBJ-3 — Repository-skill router and classification/access metadata. Runtime projection contains canonical repository/skill identity, current taxonomy hash, status and exact assignments; external classification retains rationale/evidence. Natural-language router views plus symbolic JSON. Minimal metadata is not a substitute for evidence supporting a taxonomy placement. Source SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md:169-185`; SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs:239-322`.

OBJ-4 — Installed official-library manifest/digest state. Managed ownership, commit and file identity support later status/update decisions, not truth of skill content. Source SRC-2 `docs/architecture.md:111-121`; implementation and read-back follow in the specialist annotation.

For OBJ-4, the manager derives next manifest state from inventory, the selected commit and staged live/router digests, persists it and swaps it with the installed trees. Later conflict/no-op decisions consume previous state. This is an operative self-representation of selected installed-library aspects: changes update the representation, and decisions mediated by it change later update/deployment behavior. Reflection conclusion status **wired** at that narrow operational boundary; a self-theory of the organization's theory-building methods and any improved capacity remain uninspected. Source SRC-1 `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts:1214-1249,1468-1545`.

> 				const stagedLiveTreeDigest = digestTree(stagedRepoSkills).digest;
> 				const stagedLiveRouterDigest = digestRouterTree(stagedRouter);
> 				const nextState = stateFromInventory(
> 					inventory,
> 					snapshot.commit,
> 					this.sourceRepository,
> 					this.now(),
> 					previousState,
> 					stagedLiveTreeDigest,
> 					stagedLiveRouterDigest,
> 				);
> 				mkdirSync(dirname(stagedState), { recursive: true });
> 				writeFileSync(stagedState, stableJson(nextState), "utf8");
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Memory annotation for OBJ-1 — Repository operating skill graph. Files: root/sub-skill `SKILL.md`, natural-language references and executable scripts. Produced by Creator/model authorship or imported as a published tree; updated after verification and refresh. Researcher consumes instructions/knowledge and may execute helpers. The graph's links do not imply graph-database storage. SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md:14-20`; representative shape as above. Conclusion status: afforded for generated content; wired for file loading.

> Keep two output areas separate:
> 
> - Runtime skill directory: the publishable repo skill, containing only
>   `SKILL.md`, `references/`, `scripts/`, `sub-skills/`, and optional runtime
>   assets/templates that future agents need to use the skill.
> - Review/test artifact directory: all check-only material, defaulting to
>   `<repository-path>/skills/tests/<chosen-skill-id>/`.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Memory annotation for OBJ-2 — Construction and verification records. Private file area defaults to `<repository-path>/skills/tests/<skill-id>/`, split into `test-cases/` and `reports/`. It contains native command results, model evaluation grades, iteration notes, source/coverage maps and staleness audits. These are mixed raw excerpts, structured execution metadata and derived judgments; they are not all raw trajectories. Verification/refresh consumes them as evidence. Runtime skill docs are explicitly prohibited from linking self-refine output as user-facing documentation. SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md:25-47,124-138`; SRC-1 native-case runner ranges above. Conclusion status: afforded for model-created records, wired for native JSON report writes.

> Save a short evaluation note when practical, for example
> `reports/self-refine/iteration-1.md` under the review/test artifact directory,
> with prompts, assertions, grades, failures, and revisions made.
> 
> Treat `reports/self-refine/` as a development artifact under the review/test
> artifact directory, not part of the public runtime skill. Do not link
> self-refine artifacts from generated root or sub-skill `SKILL.md` files as
> user-facing documentation.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Memory annotation for OBJ-3 — Router and classification/access metadata. Includes a fixed taxonomy, minimal per-skill routing JSON, generated repository/assignment JSONL ledgers and Markdown area/family navigation. Agent classification authors the decision; scripts validate and compile display pages. Researcher consumes routing descriptions; import/updater code consumes identities, hashes and assignment sets. Full rationale/evidence remains external; confidence survives in the assignment ledger. SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/update_repo_skills_router.mjs:441-505,535-555,648-714`. Conclusion status: wired for projection, afforded for semantic classification.

> 			return {
> 				repo_id: skill.metadata.repoId,
> 				legacy_repo_id: repository?.legacy_repo_id ?? null,
> 				skill_id: skill.id,
> 				area: assignment.area,
> 				family: assignment.family,
> 				confidence,
> 			};
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/update_repo_skills_router.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Memory annotation for OBJ-4 — Official-library manifest/digest state. JSON binds a fetched source commit, per-skill digests, managed root files and aggregate live/router digests to installed/update timestamps. Library-manager consumers compare old/current/desired states, detect modified local entries and stage replacement. This is operational memory with enforcement/validation force, not prose guidance or learned knowledge. SRC-1 `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts:637-660,1214-1249,1468-1545`. Conclusion status: wired.

> 			const previous = state?.managedSkills[skillId];
> 			if (!previous) {
> 				if (current.digest !== desired.digest) conflicts.push(`${skillId}: local skill uses an official skill ID`);
> 				continue;
> 			}
> 			if (current.digest !== previous.digest && current.digest !== desired.digest) {
> 				conflicts.push(`${skillId}: managed skill has local modifications`);
> 			}
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

OBJ-5 — private environment continuation report, `repo_env_report.json`, a specialized part of OBJ-2. Setup command traces feed readiness judgments, warnings, command outcomes and canonical `workflowEnvironment` fields. Creator reads that result to decide whether to draft and to provide exact executable/package/version to later workflow lanes. It is retained JSON with explanatory strings, not merely a printed execution log. Local machine details remain private. SRC-2 `cli/packages/coding-agent/src/disco/skills/prepare-repo-skill-env/references/verification-and-failure-report.md:105-170,179-212`; `cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md:111-115`. Conclusion status: afforded.

> Write the report from the observed command results after the gates finish. The
> report is private setup evidence, not generated skill content. Use this minimum
> shape:
> --- `cli/packages/coding-agent/src/disco/skills/prepare-repo-skill-env/references/verification-and-failure-report.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> The `environment` object is private setup evidence. In particular,
> `environment.pythonExecutable` is not the object to pass directly to workflow
> `agent()`. `create-repo-skill` must use `workflowEnvironment`, whose canonical
> runtime fields are `executable`, optional `cwd`, distribution `package`, and
> exact `version`. Older private reports may call the latter two
> `expectedDistribution` and `expectedVersion`; those names are report evidence,
> not the authored workflow contract.
> --- `cli/packages/coding-agent/src/disco/skills/prepare-repo-skill-env/references/verification-and-failure-report.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

OBJ-6 — external routing decision/handoff, `classification.json` plus `evidence.md`, a specialized construction record distinct from OBJ-3's delivered projection. It retains per-assignment rationale/evidence and the source identity and portable tree digest. Importer/updater consumes the handoff; normal Researcher routing does not read its reasons. Import validation requires rationale presence and source evidence paths; it does not evaluate the truth of that explanation. SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md:165-187,214-219`; SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs:239-285`. Conclusion status: wired for admission checks, afforded for authored decision.

>    Write the full decision outside the runtime skill, preferably under
>    `<repo-path>/skills/disco/routing_decision/`, with a machine-readable
>    `classification.json` and human-readable `evidence.md`. The runtime
>    `references/repo-routing-metadata.json` is only the minimal v2 projection:
>    `schema_version`, canonical `owner/repository` `repo_id`, `skill_id`, the
>    current taxonomy hash, `routing_status`, exact assignments, and an
>    `unclassified_reason` only when applicable. Do not store evidence or
>    rationale in that runtime JSON.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> 		if (handoff.status !== "classified") continue;
> 		if (typeof assignment.rationale !== "string" || !assignment.rationale.trim() || !Array.isArray(assignment.evidence) || assignment.evidence.length === 0) throw new ImportError("classified routing handoff assignments require rationale and evidence");
> 		let nonGeneratedEvidence = false;
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

#### Memory evidence for retained objects and access

AREX-Skill retains repository knowledge as portable operating instructions with linked references and executable helpers. It separates that usable graph from construction evidence. The next Researcher reads a task-relevant part of the graph; the next Creator verification or refresh can read prior reports. This makes the consumer route decisive: a retained report is not automatically Researcher memory.

For OBJ-1, the form is concretely illustrated by the Accelerate root: the file routes by workflow and instructs a future agent to inspect provenance before deciding whether to refresh. This is static content evidence, not an observed learning episode. SRC-2 `skills/repositories/repo-skills/accelerate/SKILL.md:32-44`.

> ## Shared References And Scripts
> 
> - Read `references/troubleshooting.md` first for cross-cutting install/import, CLI, optional dependency, hardware, and distributed hang triage.
> - Read `references/repo-provenance.md` before deciding whether this skill matches a current Accelerate checkout or should be refreshed.
> - Run `scripts/check_accelerate_environment.py --help` or the script itself for a safe import/CLI/backend availability diagnostic.
> --- `skills/repositories/repo-skills/accelerate/SKILL.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Construction improvements have a separate evidential status from deployment code. Native commands are run and summarized by executable code. Turning their failures into better skill content is an authored model procedure. The complete transformation is therefore afforded; it must not be called a hardcoded or observed learning loop. SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py:113-148,168-189`; SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md:143-164`.


>    PASS, SKILL_GAP, NATIVE_FAIL, BLOCKED_REQUIRED_BACKEND, SKIP_UNSAFE, and
>    SKIP_NOT_SELECTED results under the artifact directory. Use
>    `BLOCKED_REQUIRED_BACKEND` when required hardware/environment/runtime
>    evidence is unavailable. Treat it as a high or critical import blocker, not
>    a skip or pass. Use failures or gaps to revise the runtime skill before
>    static verification when the generated skill is wrong or thin.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Context reduction comes from a visible router and requested progressive reads, not an embedding retriever. The code excludes hidden root/sub-skill descriptions from the prompt. The router asks the Researcher to read one or two area pages, then relevant family pages and selected roots. That is an instructional selection budget, not a hard token limit. The complete read sequence depends on model compliance. SRC-1 `cli/packages/coding-agent/src/core/skills.ts:345-387`; SRC-2 `cli/packages/coding-agent/src/disco/skills/repo-skills-router/SKILL.md:21-37`.

> export function getModelVisibleSkills(skills: Skill[]): Skill[] {
> 	return skills.filter((skill) => !skill.disableModelInvocation);
> }
> --- `cli/packages/coding-agent/src/core/skills.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> 1. Identify the user's dominant capability, workflow, data/model format, and
>    runtime intent.
> 2. Read only the one or two most likely area pages.
> 3. Compare the relevant family pages, especially when training, inference,
>    evaluation, deployment, or similarly named repositories overlap.
> 4. Open the selected repository root at
>    `../repo-skills/<skill-id>/SKILL.md`, then read only its relevant sub-skills,
>    references, and scripts.
> --- `cli/packages/coding-agent/src/disco/skills/repo-skills-router/SKILL.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Provenance and admission controls establish identity, portability and consistency, not semantic truth. Import checks compare the portable tree digest with a routing handoff, and require evidence/rationale for classified assignments. The generated runtime projection discards that rationale. Rationale conclusions about reason retention must distinguish these surfaces.

### Routes

RTE-1 — Creator repository-skill construction and verification workflow. Trigger: an open user construction request/source anchor; owner: main model following bundled construction skills. Inputs include repository evidence, selected extraction scope, backend plan and user constraints. The model plans sub-skills, delegates generation when available, integrates directly written files, prepares routing evidence, then performs content review and native/static checks. The user normally approves scope/import; explicit delegated policies allow agent scope choice or import after successful verification. These are natural-language **policy** guarantees, conclusion status **claimed** for faithful end-to-end compliance; loading the guidance and helper execution are separately wired. Source SRC-2 `cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md:18-56,88-136,186-191`; RTE-7 is the concrete delegation surface.

>   scope approval.
> - `importAfterVerification: ask` by default, or `auto-import` when the user
>   delegates the final import decision.
> 
> This policy only skips the routine scope approval and final import approval. It
> does not authorize unsafe commands, broad dependency installation, mutation of a
> user-provided environment that may break it, overwriting an existing skill, or
> importing a skill that failed verification. `auto-import` also does not accept
> an unavailable or unverified required backend. A required-backend block must be
> resolved, removed by an explicitly narrowed extraction scope, or presented for
> an informed manual acceptance after final verification.
> --- `cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


Memory revisions and their retained evidence are annotated by the specialist. For this route the proposed change is a new or revised operating graph. Main-agent content judgment and user authorization determine readiness; a failed or partial required backend disables automatic import by instruction. Static helpers veto their own structural predicates, not arbitrary scientific claims. Ordinary output is the graph plus separate construction record; import creates later-consumable state; failure returns a bounded gap or revision request. Recovery is iterative refinement and re-verification, not an inspected guarantee that every candidate converges.

Guidance says to use source/installed-package facts, explicit coverage, assertion-backed cases and native tests. Truth-apt operational propositions can include when an API or method works, necessary prerequisites and how a failure is repaired. Such propositions can be individually inspected/revised across skill sections, sub-skills and helper code (addressability **afforded**). Theory formulation, operative use, content-directed criticism and revision are each **claimed** for this instructed review process; particular internal model theories are **uninspected**. Improved future capacity attributable to criticism is **uninspected**. Grading against authored assertions alone does not prove a correct answer; upstream tests/examples supply a separate reference where actually selected and run.

> If any assertion fails or the qualitative review reveals a gap, revise the generated skill before finishing and repeat the focused check.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


RTE-2 — Managed repository-skill admission/deployment/update. This includes dedicated single-skill importer and official-library manager branches, whose memory details follow. The inspected importer takes an external candidate and routing handoff, validates, stages, revalidates, installs the skill and updates the router/index under the import lock. Existing target replacement requires an explicit `--overwrite` flag; user approval is the upstream instruction, not proof encoded by that flag. Validation covers role/visibility/name/frontmatter, license consistency, contained links, metadata/taxonomy, matched content digest and referenced evidence-file existence/ranges. Classified assignments require rationale and non-generated evidence. The handoff's declared source commit and present local evidence path are not semantic verification of their relationship. Conclusion status **wired**, guarantee strength **protocol** at this helper, not universal authorization over direct filesystem writes. Source SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs:239-342,373-455`.

> function validateRepoSkill(skillRoot, routingEntryPath, manualUnrouted) {
> 	const files = collectPortableFiles(skillRoot);
> 	const rootSkillFile = path.join(skillRoot, "SKILL.md");
> 	if (!files.includes(rootSkillFile)) throw new ImportError(`runtime repo skill is missing a regular root SKILL.md: ${rootSkillFile}`);
> 	const seenNames = new Set();
> 	const markdownFiles = [];
> 	for (const file of files) {
> 		if (path.basename(file) === "SKILL.md") validateSkillFile(file, seenNames);
> 		if (path.extname(file).toLowerCase() === ".md") markdownFiles.push(file);
> 	}
> 	const skillId = parseFrontmatter(rootSkillFile).frontmatter.name;
> 	if (skillId === "repo-skills" || skillId === "repo-skills-router") throw new ImportError(`${skillId} is reserved for the managed repo-skill library`);
> 	const license = inspectRepoSkillLicenses(skillRoot);
> 	if (!license.valid) throw new ImportError(`repo skill license gate failed:\n${license.errors.map((error) => `- ${error}`).join("\n")}`);
> 	const metadata = validateRoutingMetadata(skillRoot, skillId, routingEntryPath, manualUnrouted);
> 	validateMarkdownLinks(skillRoot, markdownFiles);
> 	return { skillId, metadata, license };
> }
> 
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


For RTE-2's import helper, the caller proposes bytes and chooses the flag; validators can veto structure and identity; the script owns mutation/rollback. The admission function does not consume a successful native-test or semantic-review receipt: the full verification gate belongs to RTE-1's workflow instructions. This is a bounded distinction established by the inspected validation and import functions, not a claim that no other source has verification. It changes future available skills and routing, not model parameters. If mutation fails, restoration is attempted for skill/router/index; rollback failure preserves transaction artifacts and raises. Ordinary success removes temporary transaction state and tells the user to start a new Researcher session. Existing directories must be staged outside the live root. Crash/OS-failure recovery is uninspected. Immediate result: status/log output; later read-back: installed files and index; delegated visibility: caller-visible output and later host loading; invalidation: overwrite/update/removal, with no global stale-content truth guarantee.

> 	} catch (error) {
> 		if (mutationStarted) {
> 			const rollbackErrors = rollbackImport({ targetDir, targetBackup, routerDir, routerBackup, routerExisted, indexPath, indexBackup, indexExisted });
> 			if (rollbackErrors.length > 0) { preserveTransaction = true; throw new ImportError(`${error instanceof Error ? error.message : String(error)}; rollback failed:\n${rollbackErrors.join("\n")}\nRecovery artifacts remain at ${transactionDir}`); }
> 		}
> 		throw error;
> 	} finally {
> 		if (!preserveTransaction) {
> 			try { fs.rmSync(transactionDir, { recursive: true, force: true }); } catch (error) { console.warn(`warning: could not remove repo-skill transaction directory ${transactionDir}: ${error instanceof Error ? error.message : String(error)}`); }
> 		}
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


RTE-3 — Role-filtered selection and prompt/loading consumption. Creator and Researcher have distinct eligible role sets. Missing role defaults to operating; explicitly invalid role is excluded; shared is eligible in both. These are deterministic registration/visibility controls, not operating-system access controls. System prompts separately instruct models not to cross task roles and to use progressive disclosure. The semantic mismatch refusal is described by prompt policy at the inspected mode interface; do not substitute it for a proven mandatory semantic classifier. Source SRC-1 `cli/packages/coding-agent/src/disco/modes/skill-policy.ts:14-34`, `cli/packages/coding-agent/src/disco/modes/prompts.ts:3-36`. Skill discovery/body delivery and their later consumers follow in the specialist record.

> 	const value = (metadata as Record<string, unknown>)["disco-role"];
> 	if (value === "meta" || value === "operating" || value === "shared") {
> 		return { role: value };
> 	}
> 	return { invalidValue: value };
> }
> 
> export function isSkillEligibleForDiscoMode(role: DiscoSkillRole, mode: DiscoAgentMode): boolean {
> 	if (role === "shared") return true;
> 	return mode === "creator" ? role === "meta" : role === "operating";
> }
> --- `cli/packages/coding-agent/src/disco/modes/skill-policy.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


> 	"- Complete the task through investigation, implementation, experiments, and verification. Treat the current task, environment, constraints, and evaluator as authoritative; do not stop at advice when action is requested.",
> 	"- Follow progressive disclosure: load only the relevant operating skill, router branch, reference, or script needed for the next decision. Check visible guidance against the actual checkout and environment; do not preload the full skill graph.",
> 	"- If the visible operating context has a concrete capability gap, record the missing knowledge, desired source anchor, expected verification, failed evidence, and completed work. Suggest /creator and optionally write a handoff; do not carry chat context across the switch.",
> 	"- If asked to construct, refresh, validate, or import skills, state the mode mismatch and do not begin it. Ask the user to switch: interactive users run /creator; non-interactive users restart with --creator. Never switch implicitly or claim to have switched.",
> --- `cli/packages/coding-agent/src/disco/modes/prompts.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


Memory annotation for RTE-1 — Creator construction/verification. User request initiates model inspection, scope planning and generation into an external runtime tree plus OBJ-2. Source evidence and prepared environment inform root/sub-skill writing; whole-tree review and usability/native tests lead to revisions, then import readiness. Persistence is model file writing plus dedicated native-result JSON production. Construction reasons/evidence maps remain in private review artifacts. The public graph retains usable rules and source provenance; no universal requirement puts every derivation reason beside its rule. SRC-2 `cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md:91-117,136-163`; `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md:126-221`. Conclusion status: afforded for end-to-end construction.

Memory annotation for RTE-2 — Admission/deployment/update. Dedicated importer validates root identity, recursive skill files, license consistency, portable Markdown links and routing handoff; then stages the tree, replaces it and regenerates the router under the import protocol. Failure restores skill/router/index. Official-library manager separately stages upstream imports using OBJ-4 and protects local modifications. Sources: SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs:324-340,381-437`; `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts:1214-1249,1290-1317,1468-1545`. Conclusion status: wired. Successful deployment means available files, not demonstrated use or semantic correctness.


> 		fs.renameSync(stagedDir, targetDir);
> 		validateRepoSkill(targetDir, routingEntryPath, args.manualUnrouted);
> 		maybeInjectTestFailure("after-install");
> 			runRouterUpdater(agentDir, routingEntryPath);
> 		if (!pathExists(path.join(targetDir, "SKILL.md"))) throw new ImportError(`installed repo skill disappeared before commit: ${targetDir}`);
> 		if (!pathExists(path.join(routerDir, "SKILL.md"))) throw new ImportError(`repo-skills-router was not created or updated: ${routerDir}`);
> 		maybeInjectTestFailure("after-router-update");
> 		console.log(`imported and routed repo skill ${skillId} at ${targetDir}`);
> 		console.log("Start a new /researcher session to use the updated managed repo skill; no cross-agent export is required.");
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Memory annotation for RTE-3 — Role-filtered catalog and skill consumption. Loading supplies only eligible roles; missing role defaults to operating. Creator gets meta, Researcher operating, and shared passes both. Visible skill name/description/location are appended to the prompt; read-tool guidance asks the model to request matching files. Explicit `/skill:<name>` loads registered skill body into the request. SRC-1 `cli/packages/coding-agent/src/disco/modes/skill-policy.ts:14-34`; `cli/packages/coding-agent/src/core/resource-loader.ts:696-721`; `cli/packages/coding-agent/src/core/system-prompt.ts:46-48`; `cli/packages/coding-agent/src/core/skills.ts:345-387`; `cli/packages/coding-agent/src/core/agent-session.ts:1301-1325`. Conclusion status: wired for eligibility, metadata announcement and explicit delivery; afforded for autonomous progressive selection. Role filtering is a discovery boundary, not proof that arbitrary file reads are prohibited.


> 	const lines = [
> 		"\n\nThe following skills provide specialized instructions for specific tasks.",
> 		"Use the read tool to load a skill's file when the task matches its description.",
> 		"When a skill file references a relative path, resolve it against the skill directory (parent of SKILL.md / dirname of the path) and use that absolute path in tool commands.",
> --- `cli/packages/coding-agent/src/core/skills.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> 			const content = readFileSync(skill.filePath, "utf-8");
> 			const body = stripFrontmatter(content).trim();
> 			const skillBlock = `<skill name="${skill.name}" location="${skill.filePath}">\nReferences are relative to ${skill.baseDir}.\n\n${body}\n</skill>`;
> 			return args ? `${skillBlock}\n\n${args}` : skillBlock;
> --- `cli/packages/coding-agent/src/core/agent-session.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

RTE-4 — Refresh/extension. Creator starts from existing skill/provenance, reads changed source and prior review artifacts, produces a staleness/capability audit, edits an external working copy, verifies and reimports. Provenance checker only compares commit/dirty state/evidence-path existence; Creator must audit material claims. Extension adds/regression-tests a capability while preserving stable identities. Source: SRC-1 `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/scripts/check_repo_provenance.py:97-169`; SRC-2 `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/references/change-detection-and-staleness-audit.md:28-63,81-96,138-148`; `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/references/refresh-editing.md:59-95`; `cli/packages/coding-agent/src/disco/skills/extend-repo-skill/references/editing-and-versioning.md:53-113`. Conclusion status: afforded for semantic refresh, wired for the comparison helper and reimport.

> Treat `status: current` as a fast signal, not the whole verification. If the
> user reports a concrete stale behavior, continue auditing claims even when the
> snapshot appears current.
> --- `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/references/change-detection-and-staleness-audit.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> 1. Update the nearest existing route, decision point, or instruction.
> 2. Replace stale sections in the nearest existing reference file.
> 3. Replace stale reusable scripts with current safe inspection, validation, or
>    conversion scripts.
> 4. Add a focused reference when current repo behavior needs more depth than the
>    existing file should carry.
> 5. Add or promote a support-workflow route when current repo evidence shows a
>    high-frequency data-preparation, validation, conversion, command-generation,
>    data-layout, optional-dependency, environment-check, or maintainer workflow
>    that was previously buried or missing.
> 6. Add a new sub-skill only when current repo behavior has distinct triggers or
>    workflows that would overload existing routing.
> 7. Remove guidance only when current repo evidence proves it is unsupported,
>    duplicated, or replaced.
> 8. Add or update `references/repo-provenance.md` with the current repository
>    snapshot.
> --- `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/references/refresh-editing.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

RTE-5 — Portable export. On an explicit export request, Creator resolves exact selected IDs and authorized replacements. Script copies selected skill trees, writes merged indexes, injects target Codex policy when requested, regenerates a scoped router, validates staged output and checks target snapshot before phased commit. Named future consumers are Codex/Claude Code/compatible external agents; their actual loading/activation is not executed here. SRC-1 `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/scripts/export_repo_skills_to_agent.mjs:933-963,975-1023`; SRC-2 `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/SKILL.md:10-17,71-101`. Conclusion status: wired for export; afforded for external consumer use.

> 	if (manifest.phase !== "validated") throw new ExportError(`cannot commit transaction from phase ${manifest.phase}`);
> 	if (digestTreeState(config.targetLibraryRoot) !== config.targetSnapshotSha256) {
> 		throw new ExportError("target repository collection changed after staging; refusing to commit stale output");
> 	}
> --- `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/scripts/export_repo_skills_to_agent.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

RTE-9 — trace-fed verification refinement, a subroute of RTE-1 also reused by RTE-4. Native runner retains command/exit/output-tail records; optional fresh isolated agents produce task results against only the draft skill. Creator grades assertions, records failures/revisions, rewrites the durable runtime graph and repeats checks. Researcher later reads the installed result through RTE-3. Source: SRC-1 native-case runner above; SRC-2 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md:102-138`; `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md:143-164,188-219`. Conclusion status: afforded. The fallback branch is perspective-based review without executed agent traces; it must not be represented as observed trace learning.

> When subagents or isolated runs are available, run at least one fresh agent against the draft skill with no access to your research notes. Ask it to complete a test prompt using the generated skill and save or summarize the result. If isolated runs are not available, review from the perspective of a future agent that can only read the generated skill files.
> 
> Grade assertions with `PASS` or `FAIL` and cite evidence. Then perform a qualitative review:
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/references/evaluation-verification-and-handoff.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


>    the skill is ready to import. Record that a self-contained, versioned
>    repo/package skill is classified as high reuse because it is intended to
>    support multiple checkouts, projects, and research tasks. This classification
>    selects the specialized managed repo collection, not the generic managed
>    importer or the current project's `.agents/skills`. If
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

RTE-10 — trace-derived environment continuation, a subroute of RTE-1. Preparation agent summarizes actual setup/probe commands into OBJ-5; the calling Creator consumes status, limitations and verified environment fields before construction lanes and final verification. This is a staged per-task transformation with a later named consumer. It qualifies under the supplied trace-learning definition even though it is factual setup guidance rather than a new repository theory. Rationale retention is stronger than a bare success flag: commands, outcomes, warnings and blocked requirements are in the private report/handoff. The consumer uses the verified fields and readiness; the source does not require rereading every original command. The initial preparation return is pull, but subsequent lane startup automatically supplies the parent-selected environment fields to the checker before child-session creation. That distinct operation is push, with a coarse presence/field-projection selector; it does not deliver the private report into the child model prompt. Source: SRC-2 environment-report ranges above and `cli/packages/coding-agent/src/disco/skills/create-repo-skill/SKILL.md:111-115`. Conclusion status: afforded for the report-to-lane route. The downstream assertion is wired: SRC-1 `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts:293-344,369-405,551-589`. It selects canonical executable/optional arguments/cwd/package/version fields from the supplied object, probes that executable, and compares the detected version before starting a child session. No retrieval token budget applies to this machine-consumed field bundle; the probe has a 15-second timeout and 64-KiB output limit.

> 		const modelSpec = resolveAgentModelSpec(options, this.mainModel);
> 		if (options.environment) await assertAgentEnvironment(options.environment, runCwd);
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> 	const environment: AgentEnvironmentSpec = { executable };
> 	const args = optionalStringArray(source, "args");
> 	const cwd = optionalString(source, "cwd");
> 	const packageName = optionalString(source, "package");
> 	const version = optionalString(source, "version");
> 	const versionArgs = optionalStringArray(source, "versionArgs");
> 	if (args) environment.args = args;
> 	if (cwd) environment.cwd = cwd;
> 	if (packageName) environment.package = packageName;
> 	if (version) environment.version = version;
> 	if (versionArgs) environment.versionArgs = versionArgs;
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

RTE-11 — classification-to-router projection, under RTE-2. Agent classification creates OBJ-6 and minimal OBJ-3 metadata; importer checks matching source/skill identities, taxonomy, digest, rationale presence and evidence paths. Updater builds compact indexes and family descriptions for Researcher pulls. The reason is consulted during admission as a required field; the generated consumer-facing pages and assignment ledger omit it. Source: SRC-1 importer `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs:239-285`; router updater ranges attached to OBJ-3. Conclusion status: wired for transformation, afforded for classification judgment. Index rebuild is compilation, not learned semantic consolidation.

#### Memory write and rationale audit

For RTE-1, initial extraction can produce durable useful instructions without being trace learning: source reading alone is authorship. RTE-9 adds the qualifying trace-fed branch. Its native output tails are capped at 4,000 characters each; raw command output is reduced to a result object, then model interpretation may change runtime rules/scripts. That last semantic step has no deterministic correctness guarantee. The fresh-agent branch asks for saved or summarized results, so full trajectories need not survive.

For RTE-10 is a second qualifying branch with a different horizon. The persisted report includes the canonical environment object consumed by later construction. Neither private environment paths nor the report belong in the portable Researcher skill graph. Keeping this branch explicit prevents an unsupported assertion that all trace-derived memory is cross-task.

For RTE-4 revises existing rules using source drift and prior verification evidence. It prefers nearby edits, requires stable identities and re-verification, and can promote a missing/buried support route. Removal of unsupported guidance is replacement during evolution. Separately, official update code forgets upstream-deleted managed entries from the live tree; this supports decay as removal, without implying gradual relevance scoring or retained invalidation history. SRC-1 `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts:1290-1305`.

> 		for (const skillId of Object.keys(state?.managedSkills ?? {})) {
> 			if (!inventory.managedSkills.has(skillId)) {
> 				rmSync(join(stagedRepoSkills, skillId), { recursive: true, force: true });
> 			}
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

Manual control remains material: the operator sets scope/admission/overwrite policies and may keep local edits; digest conflict detection prevents silent replacement in the ordinary update path. The model can automatically author/revise files after those triggers. That mixture supports manual and automatic agency without treating every human-triggered extraction as manual.

Reason retention differs by artifact. OBJ-2 keeps grades, failures, revisions and review notes; refresh explicitly reads prior review reports when present, so diagnosis can consult retained reasons. OBJ-1 carries current usable guidance and selected provenance, while development history is retained in public guidance only when it helps current behavior. OBJ-6 keeps classification reasons outside the graph; RTE-11 discards them from normal runtime projections. None of these establishes that a Researcher receives the derivation reason for every rule.

> - Existing usability tests and index files.
> - Review reports, generation handoffs, or staleness notes when present.
> - `references/repo-provenance.md`, including commit, dirty state, package
>   versions, and relative evidence paths.
> 
> Focus on public runtime skill content first. Review artifacts can explain the
> change, but they should not drive future agent behavior.
> --- `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/references/change-detection-and-staleness-audit.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

> Do not add development history to public runtime guidance unless it helps future
> agents choose correct current behavior. Put migration notes, stale-claim tables,
> and baseline details under the review/test artifact directory instead.
> --- `cli/packages/coding-agent/src/disco/skills/refresh-repo-skill/references/refresh-editing.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`

#### Memory read-back audit

The later Researcher consumer has two scoped paths. In implicit use, the model sees the router's description/location and requests its body, then selected area/family pages and skill files with the read tool. In explicit use, a user requests `/skill:<name>` and code delivers the registered body in the request. These establish delivery affordances and code paths, not demonstrated task activation or benefit. The generated membership pages themselves are requested content; the static router catalog entry does not supply accumulated membership or skill bodies automatically. This is directly supported by the updater assigning the constant `ROUTER_DESCRIPTION` on every generation rather than deriving the catalog description from repository membership. SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/update_repo_skills_router.mjs:35,516-526`.

> 	frontmatter.name = ROUTER_ID;
> 	frontmatter.description = ROUTER_DESCRIPTION;
> 	frontmatter.metadata = { ...(frontmatter.metadata && typeof frontmatter.metadata === "object" ? frontmatter.metadata : {}), "disco-role": "operating" };
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/update_repo_skills_router.mjs` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


Creator reads persisted reports and prior skills on requested construction/verification/refresh tasks. Environment handoff returns answer a preparation request. A separate downstream operation automatically supplies selected retained fields to the environment checker at lane startup. The Creator/model selects the current report's `workflowEnvironment` for the authored call, then `run()` detects `options.environment`, normalizes the fixed field bundle and asserts it before creating the child session. This is push to a named machine consumer even though the earlier handoff was requested. It is not an automatic search across saved reports or a claim that the child model receives the whole report. RTE-5 exports actual files and target visibility metadata for named external roles, but does not prove the external host loaded or obeyed them. There is no commissioned basis for assigning inferred-embedding or inferred-lexical push. The environment branch supplies a coarse bundle; package identity/version comparisons govern validation rather than selection among stored memories.

The router reduces typical breadth by asking for one/two relevant area pages and the smallest useful repository set. It has no inspected retrieval-score threshold, item count cap for family tables, or hard token budget. Large family pages can still cost context. Direct slash invocation includes the complete selected body. These are practical limits of CLM-2.

RTE-6 — Optional native-case verification helper, an effectful evaluation route. Trigger: caller supplies a manifest of preselected cases and repository/Python parameters; next-step owner: Python loop, with model/operator responsible for case selection, safety labels and correct environment. It interprets required-backend metadata, skips disallowed or missing commands with distinct statuses, then renders and executes selected command through a shell in the repository with inherited environment and timeout. Exit zero becomes PASS; nonzero/timeout becomes NATIVE_FAIL; stdout/stderr tails and metadata are retained. This is **wired** execution and reporting, **protocol** over listed cases, not verification that safety labels are honest or that successful commands prove skill sufficiency. Source SRC-1 `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py:63-148`.

>         completed = subprocess.run(
>             rendered,
>             cwd=repo_root,
>             shell=True,
>             text=True,
>             stdout=subprocess.PIPE,
>             stderr=subprocess.PIPE,
>             timeout=timeout,
>             env={**os.environ, "PYTHONUNBUFFERED": "1"},
>         )
>         elapsed = time.monotonic() - started
>         result.update(
>             {
>                 "rendered_command": rendered,
>                 "exit_code": completed.returncode,
>                 "elapsed_seconds": round(elapsed, 3),
>                 "stdout_tail": completed.stdout[-4000:],
>                 "stderr_tail": completed.stderr[-4000:],
>                 "status": "PASS" if completed.returncode == 0 else "NATIVE_FAIL",
>             }
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/run_native_cases.py` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


For RTE-6, immediate return is a structured result; later consumer is RTE-1/RTE-4 model review according to instruction. Script execution does not itself rewrite a skill. Selected expected behavior comes from native tests/examples or authored usability assertions, with their providers distinct; helper exit status only warrants the chosen command's outcome. Output tails are bounded to 4,000 characters per stream, limiting retained diagnosis. No particular command executed in this analysis. A required accelerator case without a runnable command can be blocked, but this routine's metadata is caller-supplied and actual backend adequacy is not independently proven by the label. Tool effects run with host authority; rollback of arbitrary commands is not implemented by this helper, and is not assumed.

RTE-7 — Construction subagent host interface. Trigger: authored workflow invokes an agent lane; parent model supplies brief/subSkill, tools, working directory, environment and optional model/schema. Code applies tool policy, optionally asserts the supplied absolute prepared executable/version before startup, creates an in-memory session in the parent's DisCo role, invokes model with composed brief and Creator file-writing contract, returns structured output or final text, and disposes the session. Model resolution can fall back to session default. Parameter/provider internals are CMP-2. Status **wired** for interface; actual successful file production is not observed. Source SRC-1 `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts:365-418,535-662,670-713`.

> 
> 		const agentDir = getAgentDir();
> 		const safeSessionOptions = { ...this.sessionOptions };
> 		delete safeSessionOptions.discoMode;
> 		delete safeSessionOptions.resourceLoader;
> 		delete safeSessionOptions.sessionManager;
> 		const { session } = await createAgentSession({
> 			...safeSessionOptions,
> 			cwd: runCwd,
> 			agentDir,
> 			discoMode: this.discoMode,
> 			sessionManager: SessionManager.inMemory(runCwd, { discoMode: this.discoMode }),
> 			// Use real SettingsManager to inherit user's default provider/model settings.
> 			// SettingsManager.inMemory() doesn't load ~/.disco/agent/settings.json, so subagents
> 			// would fall back to the first available model (e.g. openai-codex) which may
> 			// not have valid auth, causing silent empty responses.
> 			settingsManager: safeSessionOptions.settingsManager ?? SettingsManager.create(runCwd, agentDir),
> 			customTools,
> 			// Per-call model wins over any sessionOptions.model.
> 			...(resolvedModel ? { model: resolvedModel } : {}),
> 		});
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


For RTE-7, role/session isolation prevents inheriting the previous lane's conversation by this constructor; filesystem and host permissions remain shared according to the chosen cwd/tools. A supplied environment assertion checks executable/package version, not complete backend adequacy; it is conditional on options.environment, although creation instructions require passing it. The parent receives result text/structured object and may receive history/usage callbacks; files are the actual proposed skill change. Blank final text raises a recoverable error; abort is forwarded; structured-output retries have their own interface, not a proof of content correctness. The main model must review direct file writes before admission by policy. Later read-back is retained files on RTE-2/RTE-3, not a claim that in-memory lane chat persists as learned memory. Guidance includes scope-specific evidence/rubric and requested failure-case creation. Correction/refinement beyond caller instructions is uninspected.

> 		const detectedVersion = environment.package || environment.versionArgs || environment.version ? lines.at(-1) : undefined;
> 		if (environment.version && detectedVersion !== environment.version) {
> 			throw new Error(
> 				`expected ${environment.package ?? "runtime"} version ${environment.version}, got ${detectedVersion ?? "no version output"}`,
> 			);
> 		}
> 		return { output, version: detectedVersion };
> 	} catch (error) {
> 		const message = redactEnvironmentPaths(error instanceof Error ? error.message : String(error), environment, defaultCwd);
> 		throw new WorkflowError(
> 			`Subagent environment assertion failed while executing the prepared environment: ${message}`,
> 			WorkflowErrorCode.ENVIRONMENT_ASSERTION_FAILED,
> 			{ recoverable: false, details: error },
> 		);
> 	}
> }
> 
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


RTE-8 — Project trust boundary at the host interface. On initial resource resolution, explicit run override wins; otherwise no protected resources permits loading, extension decision may own trust, saved decision applies, then global always/never/ask and optional UI decide. In non-UI ask, result is false. Consumer is resource loader (memory details on RTE-3); effect is admission of project-local resources, not a tool-execution sandbox. Source SRC-1 `cli/packages/coding-agent/src/core/project-trust.ts:47-96`; SRC-2 `cli/docs/security.md:3-38`. Status **wired** for decision function; deployment containment **uninspected**. This route governs loading, not semantic endorsement or content revision. Trust metadata can persist in host storage but is outside this skill-memory comparison. Granting trust is not proof that native code or prompts are safe.

> ## Project Trust
> 
> Project trust controls whether disco loads project-local settings, resources, packages, and extensions. It is not a sandbox and it does not restrict what the model can ask tools to do after you start working in a directory.
> --- `cli/docs/security.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


#### Route return, read-back and effect audit

| Route | Immediate return and persistence | Later/delegated consumer and selector | Invalidation/expiry and effect limit |
|---|---|---|---|
| Audit of RTE-1 | Graph plus private construction/review files and handoff | Main model reviews child files; Researcher later requests deployed content | Model/user can revise/reject; no automatic correctness expiry; actual benefit unobserved |
| Audit of RTE-2 | Import/update status; live graph, router/index and official state | New sessions read installed files; updater requests recorded state on later command | Authorized overwrite/update/removal; rollback on handled failure; direct host writes outside guarantee |
| Audit of RTE-3 | Visible catalog and requested skill body in model input | Model selects requested branch by meaning or explicit name; metadata does not prove activation | Role/visibility filtering and reload/new session change access; stale loaded context not globally revoked |
| Audit of RTE-4 | Audit, modified external working copy, refreshed provenance, verification handoff | Creator reads prior records; deployed successor later selected through RTE-3 | Reverification/import gates and scoped edits; current hash alone does not expire or endorse claims |
| Audit of RTE-5 | Staged/committed portable collection and scoped router | Named external hosts may load exported skills; explicit selected IDs bound copy | Target-snapshot mismatch rejects stale commit; external host reload/activation uninspected |
| Audit of RTE-6 | JSON case result with bounded output tails | Creator requests results during refinement; no direct skill rewrite by runner | Old results remain historical; no expiry rule inspected; command effects are local host effects |
| Audit of RTE-7 | Child text/structured result; direct files plus optional diagnostic callbacks | Main model receives return and reviews files; role inherited, conversation starts in memory | Session disposed/abort; written files persist until changed; tools share host authority |
| Audit of RTE-8 | Boolean loading decision, optionally saved trust | Resource loader uses decision for protected project resources | Overrides/saved policy can change; not a tool sandbox; host trust store excluded from memory comparison |
| Audit of RTE-9 | Criticism/revision notes and changed portable graph | Creator requests failures/trajectories; later Researcher requests installed successor | Failed checks request further revision; perspective-only fallback is not trace evidence; no measured gain |
| Audit of RTE-10 | Private setup report and canonical environment fields | Creator pulls requested report; startup pushes coarse fields to checker before lane | New preparation can replace report; actual probe may reject stale environment; report is not sent whole to child model |
| Audit of RTE-11 | External reason-bearing decision and compact runtime/index projection | Importer reads decision; Researcher requests generated navigation | Taxonomy/content identity mismatch blocks; projection loses rationale; index rebuild is not semantic learning |

### Claims

CLM-1 — Repository knowledge becomes reusable verified operating skills. Conclusion status **claimed**, SRC-2 `README.md:70-107,175-180`; implemented helper support on RTE-2, RTE-6, RTE-7, and instructed construction/criticism on RTE-1. The strong adjective needs candidate-linked verification; shipped graph existence alone does not show all tests passed.

> 
> An AREX Skill is a self-contained, agent-readable unit of operating knowledge.
> It uses the open [Agent Skills format](https://github.com/agentskills/agentskills)
> as its portable packaging convention, then adds the operating context an agent
> needs: when to use a capability, what to run, how to validate it, and how to
> recover when an experiment fails. Each skill is organized around `SKILL.md`,
> with optional `references/` and `scripts/` resources:
> 
> ```text
> skill/
> --- `README.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


CLM-2 — Progressive disclosure selects relevant library branches without placing every body in initial context. Conclusion status **claimed** as a behavioral policy, with deterministic visibility/loading support on RTE-3 and specialist-recorded routes. No observed relevance/activation/cost effect. Source SRC-2 `docs/architecture.md:85-110`.

CLM-3 — Source reports benchmark gains for skill-equipped Codex with fixed setup, harness and budget. Conclusion status **claimed**, SRC-3 `README.md:143-171`. Reported comparison grain is the skill-equipped bundle, not any single skill, router or refinement stage. No independent observed run or causal design audit here; its table cannot establish current-code fidelity or general skill quality.

>     src="assets/results.png"
>     width="82%"
> --- `README.md` @ `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6`


Memory assessment of CLM-1, CLM-2 and CLM-3 agrees with their bounded records above: code checks structural admission and supports selective reads; full semantic verification and reported benefits require separate evidence.

### Evidenced absences

No ABS records asserted. Limits are scoped uninspected findings or positively described enforcement boundaries, not search-miss claims of universal absence.

### Behavioral-authority paths

BAP-1 — Creator model, bundled SKILL.md/references and mode prompt, instruction/policy force for construction session; RTE-1 and RTE-7. Proposal guidance and critics can change authored artifacts, but recorded instructions do not guarantee compliance.

BAP-2 — Import helper, serialized metadata/digests/flags, enforcing structural and byte-identity admission within a single managed import; RTE-2. Does not warrant skill semantics or real user approval from the flag alone.

BAP-3 — DisCo resource loader/model, role/visibility metadata and later selected skill content, registration/routing/instruction force over the current session; RTE-3. Detailed memory-consumer paths are integrated below.

BAP-4 — Creator reviewer, native results and assertion judgments, evidence/advisory force within RTE-1/RTE-4 refinement; external test expectations and model-authored assertions have different warrant. RTE-6 only supplies command outcome.

BAP-5 — Construction-lane environment checker, retained workflowEnvironment fields via startup options, validation/enforcement force before child-session creation; RTE-10 and RTE-7. Parent selection and coarse field delivery do not expose the full private report to the child model.

BAP-6 — Router updater/importer, external classification fields and rationale presence via structured handoff, validation/routing force at admission and projection; RTE-11. Researcher sees compact routing output rather than the external reasons.

## Runtime account

An ordinary repository construction request starts in Creator, resolves source/goal/scope and backend needs, loads construction guidance, and prepares selected environment evidence. The model plans and delegates sub-skill writing; child sessions produce files and return concise status. The main model integrates, performs assertion-backed review and selected native checks, revises gaps, classifies taxonomy placement, and requests or uses predelegated import authority. Dedicated importer validates staged bytes and routing handoff, publishes the graph and router/index with rollback handling, then a new Researcher session can select/load the deployed graph. The output is a reusable operating artifact plus separate construction record; downstream research execution belongs to the consuming host.

Owner/decision split: user supplies source/request/scope constraints and may veto or delegate routine choices; model proposes scope, structure, content, cases and semantic judgments; fixed scripts decide their encoded structural predicates and command outcomes. Domain answer oracle, when available, comes from upstream tests, fixtures, expected outputs and package behavior, not merely a critic's opinion. Generated assertions are model-authored criteria until grounded and checked. Operation supports open construction/maintenance requests with bounded selected experiments inside them; no autonomous recurring curriculum is established. Improvement triggers include critique, failed assertion, native-result gap, upstream drift and explicit extension request; disposition and later read-back remain route-specific.

Material alternatives: direct importer/official manager can deploy already-authored graphs without repeating model construction; explicit skill invocation differs from model/router selection; portable export changes external host integration; users may author/edit ordinary skill files outside managed transactions; generic host read/write/bash or extensions can have effects outside these helper gates. The latter are not covered by managed import guarantees. Delegation tools, caller-provided environments and provider model choices have separate controls. Arbitrary host effects and deployment isolation remain excluded.

Forcing cases traced statically: (1) required backend unavailable blocks automatic workflow import by instruction, while native helper preserves a specific blocked status; direct importer verifies its metadata contract instead of consuming backend-success evidence. (2) mutated candidate/routing metadata fails digest/taxonomy checks; importer restoration handles an ordinary post-install error, with rollback errors retained. (3) invalid/missing roles and disabled model visibility change registration versus explicit invocation; prompt role policy is separate from deterministic visibility. (4) subagent environment assertion or model-resolution failure: supplied bad environment prevents startup, unresolved model warns and falls back. These paths are code/design analysis, not executed results.

**Execution preflight:** no dynamic check planned. Considered importer fault-injection, native-helper fixtures and live model construction. Static code suffices to identify gates, effects and ownership; dynamic filesystem mutation or model/environment installation would not establish content-wide correctness and was not needed for this characterization. No target tests, external provider calls, native shell commands or package installs ran. Runtime reliability, latency/cost and actual quality improvement remain uninspected.

## Lens scoping

### Memory/context scope

Full depth. Trigger CLM-1, CLM-2 and OBJ-1, OBJ-2, OBJ-3 and OBJ-4: durable constructed/imported graphs, maintenance and later role-filtered consumption are the subsystem's central operation. Source scope SRC-1/SRC-2 selected repository-skill routes, with documented exclusions above and the specialist's exact profile scope. No host conversation compaction or opaque provider memory classification is inferred.

### Epistemic scope

Full depth. Trigger CLM-1's verification claim and CLM-3's outcome claim. Inspect RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7 and RTE-8, their operating claims, asserted tests, content critiques, admission checks, lineage/freshness and later behavioral authority. Epistemic question: what each route checks or licenses, and whether improved future capacity is evidenced. Source-only architecture with reported outcomes separated; no claim that all library items completed a discovery lifecycle.

## Lens outputs

### Memory/context lens

Inventoried operating graphs, private review/environment reports, routing decisions/projections and managed identity state, plus construction, refinement, refresh, deployment/export and later consumption. The shared records retain all adopted specialist findings and quotes. Most content-changing behavior is model-directed and therefore afforded; deterministic helpers are wired; none is observed to improve behavior here.

The frontmatter is a union over the declared subsystem, with the weakest basis of each union. File storage includes executable/JSON control artifacts as well as prose; no transient host caches or provider weights are treated as retained subsystem memory. `other-compiled` denotes router/index construction; `trace-extracted` denotes RTE-9 and RTE-10, not static published-library provenance. The static library import demonstrates an acquisition alternative only.

Instruction, knowledge, routing, validation and enforcement refer to distinct actual consumers: model instruction/references, route readers, admission/provenance validators, and rejection based on state/digest checks. They do not assert that advisory source prose is enforced. `learning` authority is not added merely because a route qualifies as trace learning.

Curation names are narrow: evolve is a changed existing entry, promote is increased discoverability of a support route, decay is explicit removal from the installed memory set. Duplicate identity checks and index regeneration are not dedup/consolidate. Synthetic test prompts do not establish novel repository-knowledge synthesis. No retained-history withdrawal operation was found in the inspected skill refresh/update route.

Read direction is a union of operations within a chain, not one label inherited from the first request. The environment-report branch establishes both its requested return and subsequent automatic checker consumption. Its coarse selector is presence of a supplied environment plus fixed field projection. An executable/package/version identifier used as a validation target is not an identifier-based memory-selection signal. The semantic bridge from retained report to authored lane options remains afforded; startup's automatic check is wired.

Both trace branches are staged. One updates portable cross-task skills; the other provides a per-task continuation report. Tool results and agent task trajectories are the relevant trace inputs, and natural-language/symbolic guidance the outputs. There is no evidence of parametric training. Optional fresh-agent verification instructions and ordinary native tests are insufficient for a known affirmative faithfulness result. The absence of commissioned executed evidence is retained as not-determinable, not a population-wide negative finding.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1, SRC-2 and SRC-3 at the frozen revision. Question: what turns repository evidence into operative guidance, what checks authorize reliance, and what evidence supports learning or improved capacity? Assessed families are repository construction/refinement, verification, managed deployment, refresh/export and role-filtered use, with material native/delegation/trust interfaces. Excluded host/paper/meta routes prevent a whole-runtime knowledge-production conclusion. CLM-1 asserts verified reusable skills, CLM-2 relevant progressive disclosure, and CLM-3 reported downstream improvement. No current candidate-linked execution or causal experiment is observed here.

#### 2. Epistemic-object inventory

| Object | Candidate truth-apt part or none | Producer/consumer and warrant limit |
|---|---|---|
| OBJ-1 | API behavior, prerequisites, applicability, failure diagnoses and method claims may be truth-apt; commands and routing instructions also prescribe actions | Creator/import source produces; later model follows selected parts. Instructions can express proposed operational solutions without retaining the reasons for adopting each one. Storage format alone does not decide whether content is a theory. |
| OBJ-2 | Evidence descriptions, asserted test outcomes, expected behaviors, criticisms and scope judgments; other fields only track execution | Models write many judgments; command helper writes execution facts within its own contract. Later review/refresh can use them. Native exit status is not the same proposition as skill sufficiency. |
| OBJ-3 | Repository membership, capability classification and provenance assertions; identifiers/hash fields mainly control access | Model classifies, scripts validate/project, model routes. Taxonomy membership is not a test of actual task success; file/digest validity is not semantic support. |
| OBJ-4 | Installed source identity/content state and drift assertions | Manager derives records from selected files and uses them on status/update. Byte equality is bounded integrity, not substantive correctness. |

OBJ-5 adds truth-apt setup/readiness and version assertions plus machine-consumed environment fields; preparation model produces, Creator and lane checker consume. Observed command results constrain its warrant, but report authorship and completeness are not proven by field presence. OBJ-6 adds the semantic classification/rationale and declared source lineage; importer checks its fields and byte identity, while ordinary runtime projection omits the reasons. New construction candidates have **no instance observed** in this analysis; any inspected shipped graph is an available artifact whose original production, criticism and acceptance states remain **not determinable** without linked run evidence.

#### 3. Authority-route ledger

Architectural statuses are separate from conclusion statuses. Authored workflow operations are **doctrine only** where their substantive check/change is specified in SKILL.md but not enforced by the inspected code. Executable helper functions are **implemented**. A prompt being loaded is implemented delivery; it does not establish every instructed operation. No route has an observed candidate-specific execution state here except availability of shipped artifacts; original lifecycle states remain not determinable.

| Route/function | Content/update relation and target | Evaluator, trigger, disposition and force | Epistemic authority versus operational authority | Architectural status and limit |
|---|---|---|---|---|
| RTE-1 content transformation | truth-apt transformation: indeterminate, repository evidence to operating claims; non-truth-apt policy/content update for procedural instructions | Creator model under user scope and bundled workflow constructs/revises graph | Candidate procedure eligible for review, not knowledge accepted merely by writing | doctrine only for substantive generation sequence; host model invocation implemented on RTE-7 |
| RTE-1 check/evidence production | no content change to reviewed claim; test/evaluation claims separately produced | Main model or fresh consumer judges asserted outcomes, coverage and grounded native behavior | Claims of fit within stated scope; external native references differ from model-generated assertions | doctrine only for full semantic review; RTE-6 implements optional command evidence |
| RTE-1 disposition/acceptance | no content change | Model determines readiness against instructions; user may approve, veto, delegate or accept a limited backend result | Scoped verification judgment grants import permission by policy; not universal scientific truth | doctrine only; code importer has a narrower criterion |
| RTE-1 behavior/policy adaptation | non-truth-apt policy/content update and indeterminate truth-apt revision | Failed assertion or critique leads model to revise/recheck | Proposed future procedure changes; observed improvement not established | doctrine only; trace-fed details in memory overlay |
| RTE-2 check/evidence production | truth-apt transformation: entailed derivation within bytes/schema/path domain | Validator checks content digest, taxonomy/metadata and file/range predicates | Warrants structural consistency/integrity under local filesystem assumptions | implemented; not a semantic review or source-history proof |
| RTE-2 disposition/acceptance | no content change | Valid staged tree plus flags admits managed import; mismatch throws | Enforces helper's admission contract and permits replacement; BAP-2 | implemented; human approval and content verification are upstream premises |
| RTE-2 retention | no content change | Files copied/swapped into managed tree and router/index updated | Makes bytes available to future session | implemented; installed is not epistemically accepted |
| RTE-2 lineage/freshness/recovery | no content change or non-ampliative metadata projection | Manifest/status/update and rollback use installed state | Protects managed ownership/identity and restores ordinary failed transactions | implemented within inspected branches; crash recovery and external edits limited |
| RTE-3 operational admission/selection/consumption | no content change | Role/visibility filter registers skills; model or explicit request selects later content | BAP-3 shapes available guidance and behavior; prompt policy is distinct from code exclusion | implemented registration/delivery; semantic routing behavior requires model adherence |
| RTE-4 content transformation | truth-apt transformation: indeterminate for source/criticism-driven guidance edits; policy update for procedural changes | Creator uses upstream changes and prior evidence to revise working graph | Candidate guidance, not accepted merely because newer | doctrine only for semantic revision; afforded interface |
| RTE-4 check/evidence production | entailed derivation for provenance/dirty/file checks; indeterminate for semantic critique | Provenance helper and model audit evaluate different targets | Current snapshot signal differs from correctness of each claim | implemented helper; doctrine only for content audit |
| RTE-4 disposition/acceptance | no content change | Model follows re-verification policy and authorized import calls RTE-2 | Scoped readiness judgment plus managed admission, with distinct vetoes | doctrine only semantic acceptance, implemented helper admission |
| RTE-5 retention | no content change to selected graph, non-ampliative compatibility projection | Export script stages and copies selected files/router | Retains selected operating content for named external consumer | implemented; target host behavior uninspected |
| RTE-5 operational admission/selection/consumption | no content change | Explicit export request, validation and target snapshot check govern commit | Export permitted within helper's contract; external host use afforded | implemented export admission, external activation uninspected |
| RTE-6 check/evidence production | truth-apt transformation: acquisition/import of actual command output and entailed derivation of exit-status classification | Caller-selected command runs; result/tail returned | BAP-4 gives evidence of selected command, not all assertions or backend quality | implemented; actual run no instance observed |
| RTE-7 operational admission/selection/consumption | no content change to supplied brief; model may generate new content | Tool/model/environment/session setup enables child work; optional schema controls returned shape | Environment identity check and role isolation are operational, not semantic approval of authored files | implemented; external model internals uninspected |
| RTE-8 operational admission/selection/consumption | no content change | Trust override/extension/saved/default/UI decision admits protected resources | Resource-loading permission, not knowledge endorsement or OS isolation | implemented decision function; concrete deployment uninspected |

Additional function rows for specialized memory routes:

| Route/function | Content/update relation and target | Evaluator/condition, result and force | Architectural status; epistemic and operational limit |
|---|---|---|---|
| RTE-9 content transformation | truth-apt transformation: indeterminate for criticized guidance; policy update for revised procedures | Creator rewrites durable graph from test/consumer feedback under BAP-1 | doctrine only; afforded whole route, no observed capacity gain |
| RTE-9 check/evidence production | no content change to candidate; derived grades/criticisms may be indeterminate | Native references or fresh-agent result plus authored assertions test different targets | implemented helper evidence, doctrine only for complete criticism and recheck |
| RTE-9 disposition/acceptance | no content change | Creator declares readiness under RTE-1; RTE-2 admission remains separate | doctrine only semantic acceptance; no candidate-linked accepted state |
| RTE-10 content transformation | truth-apt transformation: indeterminate for readiness synthesis; acquisition/import for command results | Preparation model writes OBJ-5 from probes and reports limitations | doctrine only semantic synthesis; later fields guide continuation, not a universal environment guarantee |
| RTE-10 operational admission/selection/consumption | no content change | Lane startup supplies fixed selected environment fields to checker; BAP-5 | implemented assertion, afforded report-to-lane chain; blocks that startup if check fails |
| RTE-11 content transformation | truth-apt transformation: indeterminate for taxonomy judgment; non-ampliative reshaping for projection | Model proposes OBJ-6; script derives OBJ-3 with rationale omitted | doctrine only judgment, implemented projection; source classification warrant not strengthened |
| RTE-11 check/evidence production | entailed derivation within field/digest/path rules | Importer validates structured handoff and rationale/evidence presence | implemented; presence and local path validity do not prove rationale truth |
| RTE-11 disposition/acceptance | no content change | Invalid taxonomy/digest/identity rejects; valid handoff permits projection/import | implemented, BAP-6 within admission; no broad epistemic endorsement |

Direct native execution, model judgment, metadata validation and user authority remain separate evaluators rather than one system-wide oracle.

#### 4. Per-object lifecycle disposition

OBJ-1 transformation is **indeterminate** between acquisition/non-ampliative reshaping of known package facts, entailed derivation of workflow steps and added conjectures about applicability or repair. Source inspection alone does not compare each generated proposition with its premises. Provenance and content-level checks are designed; an inspected published graph establishes that content exists, not which checking phases ran. For a new unexecuted candidate, observed candidate state is **no instance observed**. For a shipped artifact's creation/test/acceptance/integration, observed candidate state is **not determinable** unless a retained record links it to a particular phase. No accepted ampliative lifecycle is inferred from the word verified.

OBJ-2 native command reports and manifest-derived status are acquisition/import and bounded entailed derivation, discovery lifecycle **not applicable** to their direct recording function. Model-written explanations, assertions or critiques are **indeterminate** until their content/premises are inspected. The workflow calls for criticism and revision; it does not supply candidate-linked evidence that a criticism improved a procedure. Report retention is not post-acceptance integration.

OBJ-3 taxonomy classification is **indeterminate** as a semantic judgment; its schema/identity/hash projection is non-ampliative reshaping or entailed derivation within encoded rules. The latter has discovery lifecycle **not applicable**; it inherits any error in the classification. No lifecycle record for its identifier/control-only part: no candidate truth-apt output for this part; relevant selection/update routes are RTE-2 and RTE-3. OBJ-4 byte-state/digest bookkeeping is entailed derivation under filesystem assumptions, discovery lifecycle **not applicable**; no lifecycle record for its control-only identifiers, whose relevant route is RTE-2.

OBJ-5 is **indeterminate** for the model's readiness diagnosis and acquisition/import for preserved command facts. It has an afforded retention/later-consumer path; exact executable/version checks are implemented on RTE-7 and RTE-10. No candidate-linked report instance was executed here. Its machine-control-only fields have no candidate truth-apt output beyond their referenced identity; relevant routes are RTE-10 and RTE-7. OBJ-6's taxonomy/rationale is **indeterminate** without content-level source comparison; projection and presence checks are implemented, with no observed semantic acceptance. Identity/digest-only parts follow integrity lineage, discovery lifecycle **not applicable**. Neither is treated as accepted ampliative knowledge from metadata alone.

The prescribed self-refine process can formulate criticism of operating claims: it names a failed assertion or gap and asks for a targeted revision/recheck. This is stronger than merely ranking variants by score, but remains **claimed** as an executed epistemic operation here. Rationale can be external construction content while runtime guidance carries its operational consequence; missing historical rationale neither proves nor disproves criticism. Particular inaccessible model reasoning is uninspected. Retaining a corrected skill and later reading it can provide a capacity pathway, but does not itself establish improved future capacity.

#### 5. System claims versus routes

| Claim | Doctrine/design and implementation | Observed run and causal support | Supported conclusion and mismatch/unknown |
|---|---|---|---|
| CLM-1 | Detailed construction/refinement/native-check instructions plus helper gates RTE-1, RTE-2, RTE-6, RTE-7 | No production trace or accepted graph verification inspected | A designed verification workflow with executable substeps; not a code-enforced semantic certificate on every import |
| CLM-2 | Role/visibility rules and selected loading support the progressive disclosure policy, RTE-3 | No observed relevance, activation or context-cost comparison | Mechanism can reduce initial exposure and enable selective reads; actual task routing/effect remains uninspected |
| CLM-3 | README describes fixed agent setup/budget and reports a skill-equipped bundle comparison | Reported operation only, not raw observed/causal evidence in this boundary | Attributed empirical claim at bundle grain; no local replication or isolation of router/refinement/component effect |

#### 6. Bounded conclusion

The subsystem turns source material into proposed operating guidance, asks models to criticize it against explicit criteria and native references, and deploys retained files through narrower deterministic integrity gates. Later role-filtered and routed consumption gives the retained material behavioral force. These are several different authorities: a passing command, a model's scope judgment, a digest match, an import flag and a selected skill do not warrant the same proposition. The repository makes a substantive verification design inspectable; this source-only analysis does not establish that every published graph followed it, that a particular criticism increased future capacity, or that reported bundle gains identify a single causal mechanism.


## Reconciliation

The fresh report matches this run, repository/full revision, frozen input hash and reviewed subsystem. Final report SHA-256 is recorded in Run identity; input SHA-256 is `a236636c895927deee27a53f8bd5f161c8e77e1ceb86f4a28e30375b9cab8a63`; method SHA-256 is `7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675`; worker model is unknown. Source-code quotes and source-instruction quotes retain distinct status. All generic canonical referents shared with the specialist remain unchanged.

| Specialist proposal | Canonical disposition |
|---|---|
| MEM-OBJ-1 | OBJ-5: private environment continuation report, specialized content within OBJ-2 |
| MEM-OBJ-2 | OBJ-6: external classification decision, separate from OBJ-3's delivered projection |
| MEM-RTE-1 | RTE-9: complete trace-fed verification refinement; reuses RTE-6 native execution surface |
| MEM-RTE-2 | RTE-10: trace-derived environment continuation; RTE-7 is downstream machine consumption |
| MEM-RTE-3 | RTE-11: classification/admission/projection, within RTE-2 |

Material issues resolved: (1) preserve per-task environment guidance alongside cross-task skill revision across every dependent trace axis; (2) preserve external classification reasons while recognizing that runtime metadata and assignment projection omit them; (3) use afforded for the complete semantic feedback route and wired only for helper functions; (4) do not treat importer success as proof of backend/usability verification; (5) distinguish role/visibility discovery from arbitrary file-access control; (6) keep benchmark reports and example artifact shape below observed faithfulness.

A targeted specialist return corrected pull-only aggregation: initial preparation/requested file reads are pull; subsequent automatic supply of retained environment fields to the named lane checker is push. The selector is coarse presence/fixed-field projection, not an identity lookup among memories. The fixed router description does not add a push of accumulated membership pages. Specialist amended and revalidated the same frozen-input report; parent retained that explicit correction rather than independently changing its classification. This is reconciliation, not independent convergence. Parent reflection finding concerns the manager's installed-state representation only, not a reinterpretation of trace learning as improved capacity.


## Bounded synthesis

AREX-Skill's selected subsystem makes repository operating knowledge durable and selectively usable: Creator constructs a graph, separate reports retain evidence and criticism, managed scripts admit and project files, and later Researcher sessions request relevant guidance. Executable controls cover role visibility, content identity, taxonomy consistency, local drift and transactional replacement. They coexist with a model-directed verification process whose content judgments and backend-readiness obligations remain instructions.

The strongest supported learning contribution is a usable revision pathway: native/fresh-agent results can guide changes to cross-task operating skills, while setup results can produce per-task continuation guidance. Those pathways are **afforded**; executable helpers implement particular recording, checking and delivery steps. Criticism improving future capacity is separately **uninspected**: no candidate-linked before/after comparison or supported attribution is established here. The source-reported benchmark treatment is the equipped-skill bundle, not isolated refinement or routing.

Reflection has conclusion status **wired** for the manager's narrow representation of installed library state (OBJ-4 and RTE-2): mutations update the manifest and later update/conflict decisions depend on it. This does not establish that the system revises an explanatory self-theory, and it does not imply improved capacity. Model-directed reflection on a theory-building organization remains **uninspected**; the excluded meta-skill construction route is not evidence here.

Self-improvement through a demonstrated capacity-improving change is **uninspected** at this subsystem boundary. Operational skill revision and deployment are supported; neither digest consistency nor installation certifies that a revision improves later research. New meta-skill design is excluded, so no broader reflective theory-builder claim follows from this review.

For evaluating a particular skill, the relevant evidence is its current content, provenance, actual verification results and downstream consumer behavior, each at its own boundary. For maintaining a library, the transactional importer and official manager supply narrower integrity protections that remain useful even when semantic checks are incomplete. Candidate-linked construction traces, actual skill-dependent tests, repeated controlled outcomes and audited external-host consumption would strengthen the conclusions; inspecting excluded runtime and meta-construction families would be a separate scope expansion.

## Limitations

| Limitation | Affected records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No target execution | SRC-1, RTE-1, RTE-6, RTE-7 | Static code and authored workflows | Observed compliance, skill efficacy, timing/cost and reliable completion | Frozen candidate-linked traces and checks |
| Selected repository subsystem only | CMP-1 | Excludes host conversation/compaction, general extension behavior, paper and meta construction | Whole-runtime learning, control, reflection and reliability conclusions | Separate source-bounded route coverage |
| Verification and import have different contracts | CLM-1, RTE-1, RTE-2 | Workflow instructions versus importer checks | Import success as semantic certificate | Candidate-linked verification and enforcement of its receipt if required |
| Generated assertions and native references differ | OBJ-2, RTE-1, RTE-6 | Test-selection/model-review and optional shell helper | Ground-truth validity from model judgment or exit zero alone | Audited assertions, correct reference outcomes and case coverage |
| Sampled published content | OBJ-1 | Representative graph shape only | All library items verified or current | Item-specific evidence, provenance and maintained checks |
| Provider/dependency internals excluded | CMP-2 | Selected model IDs and package pins | Fixed weights, hidden updates or internal correctness | Immutable provider/dependency evidence or probes |
| Ordinary helper rollback only | RTE-2, RTE-5 | Staging and handled failure paths | Crash-safe or universal filesystem transactions | Failure-intervention and concurrency evidence |
| Role/trust are loading controls | RTE-3, RTE-8 | Registry and project resource interfaces | OS isolation or prevention of arbitrary file/tool effects | Concrete deployment boundary and tool policy audit |
| Rationale has different consumers | OBJ-1, OBJ-2, OBJ-3 | Private review/classification versus runtime projection | Researcher receives every derivation reason | Candidate-specific reason-to-consumer trace |
| Reported aggregate outcomes | SRC-3, CLM-3 | README summary only | Replicated current-code gains or individual component causality | Raw matched trials, design and independently varied interventions |

## Verification and blockers

### Semantic verification

Checked identity, source pin/allowlist, class/subsystem boundary, all canonical mappings and source layers. Reviewed distinct ordinary/alternate routes, who proposes/decides/vetoes, answer references, parameter identity and helper-versus-host effects. All memory findings are integrated here; the local report is provenance, not a required semantic dependency.

Checked scoped trace writes RTE-9 and RTE-10 with their respective tool/task-result inputs, cross-task/per-task horizons, staged timing and mixed output form. Initial source extraction, imported static skills, raw logs and index compilation alone are not counted as trace learning. Checked read direction across complete chains: requested skill/report returns are pull; automatic environment-field supply is coarse push to a named checker. No semantic/identifier push is inferred from package validation or static catalog location. Known aggregates retain the weakest warranted afforded basis; faithfulness remains not-determinable.

Semantic content review, native command results, source/routing integrity, user import policy, structural admission and installed-state reflection have separate scopes and force. Review/private rationale can guide Creator diagnosis without reaching ordinary Researcher context. Architecture and observed candidate states remain distinct in the epistemic lens. No source-reported benchmark or shipped skill is upgraded to a linked successful verification lifecycle. Quotes support the attached findings; source occurrence checks are additional structural evidence, not semantic clearance.

### Deterministic validation

`commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-arex-skill-01/result.md` is the exact validation target. Passed before publication. Artifact validation and pinned quote checks do not execute the target system.

### Blockers

none
