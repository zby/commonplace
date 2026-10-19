---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AREX-Skill's library and DisCo runtime at ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6, with partial initial loop coverage."
run-id: AAS-2026-10-15-arex-skill-1871063034b5-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/VectorSpaceLab/AREX-Skill
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-arex-skill/related-systems/VectorSpaceLab--AREX-Skill
  revision: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
  sha256: null
---

# AREX-Skill boundary

## Boundary and evidence

This run examines AREX-Skill as shipped in its repository, including the DisCo agent that constructs and consumes its skill library. Its intended use is to explain how reusable operating instructions become available to a research agent, and where construction, verification, installation, routing, execution and later reuse sit in that arrangement. It is not limited to the Markdown library or an SDK API. The project's own distinction is explicit (SRC-1, `docs/architecture.md`):

> The AREX-Skill repository separates the published AREX-Skill Library from the
> DisCo runtime that routes, uses, creates, and maintains it.
> --- `docs/architecture.md`

The primary target class is **enclosing runtime**. DisCo ships its own CLI process entry, session construction and execution-mode dispatch, not merely instructions for an excluded host. The package exposes `disco` through `dist/cli.js` and an SDK through `dist/index.js` (SRC-1, `cli/package.json`). The process entry imports `main` and calls it with process arguments (SRC-1, `cli/packages/coding-agent/src/cli.ts`). The CLI builds services and a session runtime, while the SDK creates an Agent, supplies provider streaming and restores session messages (SRC-1, `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/sdk.ts`). The SDK includes:

> return modelRuntime.streamSimple(model, context, {
> --- `cli/packages/coding-agent/src/core/sdk.ts`

> // Restore messages if session has existing data
> 	if (hasExistingSession) {
> 		agent.state.messages = existingSession.messages;
> --- `cli/packages/coding-agent/src/core/sdk.ts`

The target also has a builder/improvement plane and a knowledge/context mechanism. These are included responsibilities, not alternative targets. Creator instructions describe a graph built for a later Researcher session, while the published router directs the consumer toward a selected graph branch (SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`, `skills/repositories/repo-skills-router/SKILL.md`):

> Convert a distillation anchor into a verified operating skill
> graph that a later Researcher can load.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

> Open the selected repository root at `../repo-skills/<skill-id>/SKILL.md`, then read only its relevant sub-skills, references, and scripts.
> --- `skills/repositories/repo-skills-router/SKILL.md`

The boundary kind is **complete artifact, partial loop**. The complete repository at the acquired commit is frozen and available, but initial inspection does not establish end-to-end implementation coverage of every construction, verification, deployment, maintenance and consumption path. In particular, the transactional importer/exporter helpers, paper recovery validators, dynamic-workflow runners and task-oriented collections have been located but not traced end to end. They remain inside the evidence boundary, not excluded host responsibilities. Their availability is not an access gap. This boundary does not warrant a whole-system completeness claim or generalize inspected entry-point behavior to every shipped workflow.

### Functional scope and initial coverage

The inventory below separates inspection from inclusion. A directory included in the target does not mean every file in it has been read. The tracked tree, rather than a documentation snapshot's directory sketch, establishes which paths are present (SRC-1).

| Top-level tracked path | Treatment and role | Initial inspection and consequence |
| --- | --- | --- |
| `.gitattributes`, `.gitignore` | Excluded from operational mechanism analysis; repository tooling metadata | Tree presence only; no conclusions about checkout normalization or ignored runtime artifacts. |
| `CONTRIBUTING.md`, `CONTRIBUTING_CN.md` | Included as potential publication/maintenance doctrine | Located, not read; contributor review enforcement is not established. |
| `LICENSE` | Excluded from legal assessment | Located; no repository-wide licensing conclusion. |
| `README.md`, `README.zh-CN.md` | Included as declared purpose, installation and reported evaluation | English README read; Chinese version not inspected. Benchmark results remain attributed reports, not reproduced experiments. |
| `assets/` | Included as presentation material | Image paths inventoried, not inspected; no graphical benchmark or demo evidence is claimed. |
| `docs/` | Included as system design and maintenance doctrine | `architecture.md` read, remaining documents inventoried. It identifies the runtime, Creator/Researcher boundary, verification, router and deployment paths; those descriptions are not by themselves proof of every implementation guarantee. |
| `cli/` | Included: shipped CLI/SDK, owned coding-agent sources, resource discovery, session state, construction workflows, installers' package target, tests and examples | `package.json`, CLI entry, selected `main.ts` and `core/sdk.ts` ranges, and Creator entry instructions read. Services, resource-loader, session-manager and library-manager symbols searched. Bundled helper and dynamic-workflow paths inventoried. No exhaustive regression, transaction, role-switch or compaction audit is established. |
| `examples/` | Included: shipped Creator and Researcher artifacts and session exports | Paths inventoried, contents not inspected. Presence of an artifact does not establish observed operation or causal attribution. |
| `scripts/` | Included: installation, release preparation, source build and home-reset tooling | Seven tracked script paths inventoried, not read. Installer safety, release reproducibility and destructive-reset behavior are not established. |
| `skills/` | Included: retained repository graphs, router, and task-oriented instructions/helpers | `README.md` and published repository-router `SKILL.md` read; repository graphs, router indexes, and `task-oriented/FrontierCS`, `task-oriented/PaperBench`, `task-oriented/PassNet` paths inventoried. No individual graph's correctness, refresh status or benchmark performance is established. |

The task-oriented paths are present in the frozen tree even though `skills/README.md` describes that collection as reserved for future expansion. That documentation is therefore not used as an exhaustive inventory (SRC-1, `skills/README.md`, `skills/task-oriented/PassNet/skills/passnet-skill/SKILL.md`).

### External dependencies and exclusions

Model providers, network services, npm dependencies and the upstream repositories/papers from which skills were distilled are outside the frozen source set. The package pins `@earendil-works/pi-agent-core`, `@earendil-works/pi-ai` and `@earendil-works/pi-tui` to `0.83.0`; their implementations are not separately acquired (SRC-1, `cli/package.json`). This prevents attributing dependency-internal loop or transport guarantees from this checkout alone. DisCo's copied coding-agent implementation remains included; dependency use does not make its shipped driver external.

Codex, Claude Code and other destination agents are excluded enclosing hosts for exported skills. Export guidance and shipped exporter code remain included; the destination agents' discovery, permissions, model calls and actual compliance are not attributed to AREX-Skill (SRC-1, `README.md`, `docs/architecture.md`). Installed user state, trusted projects, live library updates and provider credentials are not captured. Consequently this run cannot establish what a particular deployed session actually loaded or did.

The source revision is **ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6**; the inspected checkout's HEAD matches the acquired pin. The analysis cutoff is **2026-10-15**, the supplied run date, not a claim about upstream freshness or commit time. Later releases, live URLs and unpinned documentation supply no evidence. Overall evidence is **code-grounded**, with design instructions distinguished from executable source. No target execution, tests, model calls or experiments were performed.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/VectorSpaceLab/AREX-Skill` | ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-arex-skill/related-systems/VectorSpaceLab--AREX-Skill`. Implementation: `cli/package.json`, `cli/packages/coding-agent/src/cli.ts`, selected session/runtime creation ranges in `cli/packages/coding-agent/src/main.ts` and `cli/packages/coding-agent/src/core/sdk.ts`; scoped symbol searches in `core/agent-session-services.ts`, `core/resource-loader.ts`, `core/session-manager.ts`, `core/repo-skills-library-manager.ts` under that same source subtree. Doctrine/design: `README.md`, `docs/architecture.md`, `skills/README.md`, `skills/repositories/repo-skills-router/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`. Reported operation: README benchmark table only. Tracked-tree inventory covers all top-level entries and identifies deeper runtime, workflow-helper, repository-library and task-oriented paths; inventory is not content inspection. | Implementation: [package](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/package.json), [CLI entry](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/cli.ts), [SDK](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/core/sdk.ts). Doctrine/design: [architecture](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/docs/architecture.md), [router](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/skills/repositories/repo-skills-router/SKILL.md). Reported operation: [README](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/README.md). | No source-access failure encountered. Available but uninspected paths are identified above, not access gaps. External dependencies and deployed state are not frozen. No inspected execution trace or intervention/comparison supports observed-run or causal-experiment claims; README results alone do not establish those layers. |
