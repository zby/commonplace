---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AREX-Skill's library and shipped DisCo runtime at ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6, with partial loop coverage."
run-id: AAS-2026-10-19-arex-skill-089a5ed7476f-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/VectorSpaceLab/AREX-Skill
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-arex-skill/related-systems/VectorSpaceLab--AREX-Skill
  revision: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
  sha256: null
---

# AREX-Skill boundary

## Boundary and evidence

This run examines AREX-Skill as a system for constructing, retaining, routing and consuming executable operating guidance for research agents. The target includes its shipped DisCo application, not just the portable skill library. The frozen checkout's HEAD matches the acquired revision above. The evidence cutoff is 2026-10-19; upstream changes, current package releases and linked live material are not evidence for this run.

The primary target class is **enclosing runtime**. DisCo supplies a CLI and SDK, constructs an agent, selects model and tools, restores session state and invokes its own interactive, print or RPC consumers. Its knowledge-construction plane and skill library are included responsibilities, not substitutes for that runtime. This is in scope because the shipped code issues model requests and supplies the operating context those requests consume. SRC-1: `cli/package.json`, `cli/packages/coding-agent/src/cli.ts`, `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/sdk.ts`.

> agent = new Agent({
> --- `cli/packages/coding-agent/src/core/sdk.ts`

> return modelRuntime.streamSimple(model, context, {
> --- `cli/packages/coding-agent/src/core/sdk.ts`

The traced application path is `disco` → `dist/cli.js` (built from the shipped TypeScript entry) → `main` → runtime/service construction → session construction → interactive, print or RPC mode. The SDK creates a default resource loader and session manager when callers do not supply them. Existing session messages are restored into agent state. The shipped caller is part of the target even though it uses the session API. SRC-1: `cli/package.json`, `cli/packages/coding-agent/src/cli.ts`, `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/sdk.ts`.

The initially inspected knowledge loop includes Creator's construction contract, repository-graph admission, official-library installation/update, role-filtered discovery, model-visible skill descriptions, router-guided deeper reads and session retention/reload. Creator produces a graph for a later Researcher rather than executing the downstream task in the same role. The importer validates a staged repository graph, installs it, updates the router and attempts rollback on mutation failure. The library manager stages skills, router and state before swapping live paths. Runtime skill loading filters by role before name-collision resolution; prompt formatting exposes only model-visible skills. Message-end handling persists ordinary user, assistant and tool-result messages through the session manager. These are source-level mechanisms, not observed success guarantees. SRC-1: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`, `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/sdk.ts`.

> Convert a distillation anchor into a verified operating skill
> graph that a later Researcher can load.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

> Start a new /researcher session to use the updated managed repo skill; no cross-agent export is required.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`

The preceding sentence is text emitted by the importer; the source does not establish that a new session actually occurred.

> const existingSession = sessionManager.buildSessionContext();
> --- `cli/packages/coding-agent/src/core/sdk.ts`

> agent.state.messages = existingSession.messages;
> --- `cli/packages/coding-agent/src/core/sdk.ts`

The boundary kind is **complete artifact, partial loop**, not whole-system. The entire Git artifact is frozen and available. Initial inspection establishes the runtime and repository-library loop, but does not trace every shipped paper-recovery, task-oriented evaluator, dynamic-workflow or cross-agent export path through its producers and later consumers. These are material paths, not inaccessible evidence and not external hosts. They remain within the registered source for subsequent inspection. This declaration does not support exhaustive claims about every shipped workflow's verification, deployment, failure recovery or state reuse.

### Artifact coverage and limits

The table classifies every top-level tracked entry. “Included” defines functional scope, not a claim that every descendant was read. Named uninspected material limits the partial-loop coverage.

| Top-level entry | Scope and role | Initial inspection and conclusion limit |
| --- | --- | --- |
| `.gitattributes` | Excluded repository transport metadata | Tree entry identified; no conclusion about checkout/export attribute behavior. |
| `.gitignore` | Excluded repository housekeeping | Tree entry identified; no conclusion about ignored local evidence or secrets. |
| `CONTRIBUTING.md` | Included contributor-side library production and maintenance contract | Listed and linked from `README.md`; full contributor procedure not inspected, so contribution compliance is not established. |
| `CONTRIBUTING_CN.md` | Included translated contributor contract | Not inspected; cross-language equivalence is not established. |
| `LICENSE` | Excluded legal terms as a subject of analysis | No independent license-compliance conclusion; executable license metadata checks remain in scope. |
| `README.md` | Included product intent, entry points, reported evaluation | Read completely; benchmark table is reported operation, not an inspected experiment. |
| `README.zh-CN.md` | Included translated product account | Not inspected; no cross-language equivalence claim. |
| `assets/` | Included presentation of architecture and reported results: `hero.png`, `library.png`, `method.png`, `results.png` | Tree inventoried; images not inspected. No additional quantitative evidence extracted from them. |
| `cli/` | Included shipped runtime, SDK, prompts, Creator workflows, import/export helpers, manager, tests, package/build/install support and examples | Inspected `package.json`, `packages/coding-agent/src/cli.ts`, `src/main.ts`, bounded portions of `src/core/{sdk,skills,agent-session,session-manager,repo-skills-library-manager}.ts`, `src/cli/repo-skills.ts`, `src/disco/modes/prompts.ts`, `src/disco/skills/distill-ml-knowledge/SKILL.md`, and the repository importer under `src/disco/skills/verify-repo-skill/scripts/`. Remaining dynamic workflows, specialized recovery/export helpers and test assertions are not yet traced; prevents whole-system guarantees. Paths after `packages/coding-agent/` in this cell share that prefix. |
| `docs/` | Included architecture, installation, workflows, provenance/catalog and refresh doctrine | `architecture.md` read completely; remaining guides not yet inspected. Architecture descriptions alone do not establish all helper behavior. |
| `examples/` | Included supplied session exports, generated skills, review artifacts and workflow starter configurations | `README.md` read; artifact tree inventoried. HTML traces and underlying result artifacts not inspected, so no observed-run layer is claimed here. |
| `scripts/` | Included managed installation, release preparation, source-build, reset and development helpers | Tree inventoried; executable deployment paths not yet traced. No installation portability or release reproducibility conclusion. |
| `skills/` | Included retained repository graphs, generated router/indexes and task-oriented graphs with scripts/tests | Read `README.md`, `repositories/repo-skills-router/SKILL.md` and the opening operating procedure of `task-oriented/PassNet/skills/passnet-skill/SKILL.md`; inventoried repository and task-oriented trees. Individual repository procedures and FrontierCS/PaperBench evaluator loops are not exhaustively inspected; no collection-wide correctness claim. |

All source-dependent coverage statements above refer to SRC-1 at the frozen commit. In particular, the tracked tree contains `skills/task-oriented/FrontierCS`, `skills/task-oriented/PaperBench` and `skills/task-oriented/PassNet`, although `skills/README.md` describes task-oriented content as reserved for future expansion. The actual tracked material remains in scope; the guide is not evidence that the paths are absent. The inspected PassNet skill directs graph inspection, pass-file creation and evaluation, establishing a task-specific operating consumer rather than a second generic library router. SRC-1: `skills/README.md`, `skills/task-oriented/PassNet/skills/passnet-skill/SKILL.md`.

### External dependencies and evidence limits

DisCo's copied coding-agent implementation is inside this target. Its pinned `@earendil-works/pi-agent-core`, `@earendil-works/pi-ai` and `@earendil-works/pi-tui` dependencies are external implementation dependencies, not inspected repositories. Provider services, user projects, research datasets/models, GPUs and upstream repositories described by skills are also external. Their internals and behavior are not attributed to AREX-Skill. Codex, Claude Code and separately installed Pi are external consuming hosts; shipped export tooling remains internal. These exclusions prevent conclusions about provider reliability, external-host enforcement, upstream package correctness and downstream scientific validity. SRC-1: `cli/package.json`, `docs/architecture.md`, `README.md`.

The overall tier is **code-grounded** because runtime entry points and state producers/consumers were inspected. Prompt instructions and workflow stages supply doctrine/design, not proof that an agent obeyed them. No target code, tests, examples, model calls or services were executed. Missing execution evidence prevents operational reliability and causal effectiveness claims. The README's comparative benchmark figures are attributed reports only; neither their full experimental record nor the external technical report was inspected. Available but unread source files are inspection limits, not access failures. SRC-1: `README.md`, `examples/README.md`, `cli/packages/coding-agent/src/disco/modes/prompts.ts`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/VectorSpaceLab/AREX-Skill` | ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-arex-skill/related-systems/VectorSpaceLab--AREX-Skill`. Implementation: CLI/package entry, `cli/packages/coding-agent/src/main.ts`, bounded core session/skill/manager paths and importer listed above. Doctrine/design: complete `README.md`, `docs/architecture.md`, `skills/README.md`, `examples/README.md`, router and Creator skill, role prompts, bounded PassNet procedure. Reported operation: README benchmark summary only. Tracked-tree inventory supplies artifact coverage, not execution evidence. | Implementation: [CLI entry](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/cli.ts), [session SDK](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/core/sdk.ts), [library manager](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/core/repo-skills-library-manager.ts). Doctrine/design: [architecture](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/docs/architecture.md), [Creator entry](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md), [router](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/skills/repositories/repo-skills-router/SKILL.md). Reported operation: [README](https://github.com/VectorSpaceLab/AREX-Skill/blob/ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6/README.md). | No checkout access gap found. Uninspected available paths are identified above and prevent exhaustive loop coverage. No observed-run or causal-experiment layer established; supplied example exports remain available for later inspection, not validated experiments. External dependency implementations and linked live sources are outside the frozen evidence. |
