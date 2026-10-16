---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "cass_memory_system's shipped memory production, maintenance and consumption paths at commit 8aca3bbb6732321dca041b32c155617784687897"
run-id: AAS-2026-10-13-cass-memory-system-30c18219cf68-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "8aca3bbb6732321dca041b32c155617784687897"
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/Dicklesworthstone/cass_memory_system
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/cass-memory-system-30c18219cf68/related-systems/Dicklesworthstone--cass_memory_system
  revision: "8aca3bbb6732321dca041b32c155617784687897"
  sha256: null
---

# cass_memory_system boundary

## Boundary and evidence

This run analyses cass-memory (`cm`) as a memory system for coding agents, not as their enclosing execution runtime. Intended use is to characterize how its shipped software and instructions turn sessions into retained guidance, maintain that guidance, and expose it to later agent work. The target class is `memory/knowledge/context-engineering system`; the boundary kind is `whole-system`. The repository ships a CLI, an MCP-facing server, reflection and onboarding drivers, feedback and maintenance commands, and host hook templates. These are included responsibilities, not external applications merely because they call shared APIs (SRC-1: `package.json`, `src/cm.ts`, `src/commands/serve.ts`, `src/commands/hook.ts`, `src/commands/onboard.ts`).

The frozen evidence is repository `https://github.com/Dicklesworthstone/cass_memory_system` at full commit `8aca3bbb6732321dca041b32c155617784687897`. The acquired checkout's HEAD equals that revision and its working tree was clean on inspection. The applicability cutoff is the opening's run date, **2026-10-13**, not a claim that this revision represents every deployment on that date. The overall tier is `code-grounded`: executable source establishes the shipped mechanisms; target-authored instructions establish intent. No target execution, tests, model calls or services were run. Later revisions and outside repositories are not evidence in this run.

### Classification and shipped loop

The target explicitly describes a transformation from sessions to rules, and its implementation has both a retained-state producer and a later consumer. This establishes an in-scope memory system rather than merely a returning search utility (SRC-1: `README.md`, `src/orchestrator.ts`, `src/playbook.ts`, `src/commands/context.ts`).

> `cass-memory` implements a **three-layer cognitive architecture** that transforms raw session logs into actionable, confidence-tracked rules:
> --- `README.md`

The package compiles `src/cm.ts` and exposes both `cass-memory` and `cm`; that driver registers context, reflection, onboarding, playbook, mark, outcome, guard and other commands. Reflection discovers or accepts sessions, exports their content through the cass adapter, generates and saves diaries, proposes deltas through a model-backed reflector, validates them, curates them, and writes global and repository playbooks before recording processed sessions. Onboarding is a second shipped production route: it supplies extraction instructions to the calling agent, which uses playbook-add commands to persist its rules. Both routes belong to the boundary (SRC-1: `package.json`, `src/cm.ts`, `src/commands/reflect.ts`, `src/orchestrator.ts`, `src/diary.ts`, `src/reflect.ts`, `src/llm.ts`, `src/validate.ts`, `src/commands/onboard.ts`, `src/commands/playbook.ts`).

> You are analyzing a coding session to extract reusable rules for the playbook.
> --- `src/commands/onboard.ts`

> await savePlaybook(globalToSave, globalPath, { updateLastReflection: true });
> --- `src/orchestrator.ts`

Context generation reloads and merges retained playbooks for the requested workspace, scores active rules, selects within a budget, and combines them with history from cass. MCP `cm_context` uses the same generator; `memory_reflect` invokes the shipped orchestrator. Feedback commands update stored rule events and maturity. Project export can write instruction text to a caller-selected file. The installed session-end hook starts the CLI reflection driver; it is therefore inside the system's production loop, even though a host emits its input (SRC-1: `src/commands/context.ts`, `src/commands/serve.ts`, `src/commands/mark.ts`, `src/commands/project.ts`, `src/commands/hook.ts`).

> const playbook = sources.playbook;
>
> const keywords = extractKeywords(task);
> const cassQuery = buildCassHistoryQuery(task);
> --- `src/commands/context.ts`

> const argv = [...selfInvocation(), "reflect", "--session", decision.transcriptPath!, "--json"];
> --- `src/commands/hook.ts`

The instruction surfaces also belong to the consumption and feedback loop: the skill and repository memory protocol tell agents to retrieve context before work and leave feedback references during work. Their claim that learning happens automatically is declared protocol, not an observed guarantee that every installation has automation configured (SRC-1: `SKILL.md`, `AGENTS.md`, `docs/planning/AGENTS.md.blurb`, `src/commands/hook.ts`).

> 1. START:    cm context "<task>" --json
> 2. WORK:     Reference rule IDs when following them (e.g., "Following b-8f3a2c...")
> 3. FEEDBACK: Leave inline comments when rules help/hurt
> 4. END:      Just finish. Learning happens automatically.
> --- `SKILL.md`

The safety-state path is included too: trauma storage persists global or project entries, and generated Python hooks reload active entries to check host commands or staged changes. This is a shipped consumer of retained content, not merely developer tooling (SRC-1: `src/trauma.ts`, `src/commands/guard.ts`, `src/trauma_guard_script.ts`). Evaluators include the source-level retrieval benchmark and stubbed CLI learning-loop tests. They are inspectable test designs, not results observed in this run (SRC-1: `test/context-retrieval-benchmark.test.ts`, `test/learning-loop.e2e.test.ts`).

### External dependencies and limits

- **cass search/index/export and originating agent logs:** the included adapter invokes the external cass executable and can query remote hosts through SSH. cass's index construction, remote corpus completeness and the hosts' transcript production are outside this repository boundary. This prevents claims about their internal behavior, exhaustive historical coverage, or cross-machine deployment success; it does not exclude CM's discovery, export, sanitization or retrieval adapter (SRC-1: `src/cass.ts`, `src/diary.ts`, `src/orchestrator.ts`).
- **Models and embedding backends:** provider SDKs and transformer dependencies are declared, and CM constructs model prompts and calls its generation wrapper. Provider internals, model weights, API availability and returned model quality are not frozen evidence. This prevents claims that generated lessons are correct or that configured backends work in deployment; prompt construction, validation and fallback code remain included (SRC-1: `package.json`, `src/llm.ts`, `src/reflect.ts`, `src/validate.ts`).
- **Enclosing agents, MCP clients, schedulers and Git:** CM supplies commands, protocol text and hook payload consumers, not the full hosts. No host transcript demonstrating actual compliance was supplied. This prevents attributing the hosts' task planning, command execution, hook delivery or adherence to returned guidance to CM (SRC-1: `SKILL.md`, `src/commands/hook.ts`, `src/commands/serve.ts`, `src/trauma_guard_script.ts`).
- **Execution evidence:** all available evidence here is source text. Tests were inspected but not executed, and no independently inspectable deployment trace or causal experiment was supplied. This prevents observed success-rate, performance, safety-effectiveness or causal learning claims. The benchmark's assertions and stubbed loop's expected behavior may be described as test contracts only (SRC-1: `test/context-retrieval-benchmark.test.ts`, `test/learning-loop.e2e.test.ts`).
- **Historical proposals and repository administration:** deliberately excluded from shipped behavioral claims as detailed below. Their existence does not narrow the shipped memory loop. No material shipped path was unavailable; files awaiting deeper analyst inspection are not access gaps.

### Top-level tracked coverage

The table accounts for every top-level tracked file or directory from the pinned Git tree. “Included” fixes the functional scope, not a claim of exhaustive line-by-line inspection. “Inventory only” and “selected inspection” distinguish material still to inspect from unavailable evidence. All anchors in this table refer to SRC-1. No top-level directory was inaccessible.

| Top-level tracked path | Scope and inspection status | Material paths and role; exclusion consequence |
|---|---|---|
| `.beads/` | Excluded; README/config inventory and scoped search | `.beads/README.md`, `.beads/config.yaml`, `.beads/metadata.json`, `.beads/issues.jsonl`, `.beads/deletions.jsonl.migrated`, `.beads/onboard-v2-plan.md`, `.beads/.gitignore`: developer issue tracking and plans. No shipped source/build reference was found in the scoped reference search. Exclusion prevents deriving shipped behavior or completion from issue status and plan text. |
| `.cass/` | Included; inspected | `.cass/playbook.yaml`: checked-in repository memory artifact, with an empty bullets list. It is not a populated deployment corpus and cannot support actual learned-rule effectiveness. |
| `.gitattributes` | Excluded; searched | Git merge configuration for developer issue records. No conclusion about merge-driver behavior. |
| `.github/` | Included as delivery/evaluation context; selected search | `.github/workflows/ci.yml`, `.github/workflows/release.yml`: typechecks, tests, compilation and release packaging; `.github/workflows/notify-acfs.yml` inventory only. No CI run or released binary was observed. |
| `.gitignore` | Included as persistence/build context; searched | Runtime, build, secret and tool exclusions. Does not establish whether any deployed state was retained. |
| `.ubsignore` | Excluded; searched | Developer static-scanner exclusions. No scanner effectiveness or vulnerability-absence conclusion. |
| `AGENTS.md` | Included memory protocol; selected inspection | Repository self-use onboarding, context retrieval and feedback instructions. Other developer coordination sections are excluded from CM runtime responsibilities; no claim about operation of those external developer tools. |
| `CHANGELOG.md` | Included as attributed release context; inventory only | Historical change declarations; not inspected initially and not evidence that fixes work. |
| `CONTRIBUTING.md` | Excluded; inventory only | Contributor policy, not shipped memory behavior. No conclusion about actual contribution/review process. |
| `LICENSE` | Excluded; inventory only | Legal terms. No licensing assessment. |
| `README.md` | Included; selected inspection and heading search | Declared architecture and operating guide, including onboarding, reflection automation, retrieval, feedback, safety and MCP sections. Examples and performance claims are not execution evidence. |
| `SKILL.md` | Included; selected inspection and heading search | Agent-facing retrieval/feedback protocol, maintenance and automation guidance. Actual caller compliance remains unobserved. |
| `bun.lock` | Included dependency context; inventory only | Bun dependency pinning; no dependency-source audit. |
| `bunfig.toml` | Included evaluation configuration; searched | Test setup and timeout configuration; not a test result. |
| `cm_illustration.webp` | Excluded; inventory only | Presentation image; no behavioral inference from artwork. |
| `competing_proposal_plans/` | Excluded; tree inventory and shipped-reference search | Gemini, Grok and GPT proposal text and `competing_proposal_plans/claude_version/` prototype (`cass-reflect.ts`, `package.json`, README and AGENTS). Not the package's shipped CLI entry point and no reference found in shipped source/build paths. Exclusion prevents treating alternative designs or prototype behavior as current CM behavior. |
| `docs/` | Included operating instructions; selected search/read | `docs/AGENT_NATIVE_ONBOARDING.md` and `docs/planning/AGENTS.md.blurb` describe caller-assisted extraction and later retrieval/feedback. Remaining `docs/planning/` plan, research, friendliness report and suggested cass improvements are inventory only and excluded from implemented-behavior claims; they cannot establish adoption or external cass changes. |
| `gh_og_share_image.png` | Excluded; inventory only | Social preview image; no mechanism or operation claim. |
| `install.sh` | Included delivery path; selected search | Installer chooses compiled artifacts or a Bun source build. No installation, artifact-integrity or platform-success observation. |
| `package-lock.json` | Included dependency context; inventory only | npm dependency lock; no dependency-source audit. |
| `package.json` | Included; inspected | Published CLI aliases, Bun compile entry points, scripts and dependencies. |
| `scripts/` | Included delivery/evaluation support; selected search | `scripts/patch-standalone-deps.mjs`, `scripts/coverage.sh`, `scripts/e2e-smoke.sh`: standalone dependency patching, coverage and smoke harnesses. Not executed. |
| `src/` | Included entire shipped implementation; selected loop tracing | Production: `src/cm.ts`, `src/commands/reflect.ts`, `src/orchestrator.ts`, `src/diary.ts`, `src/reflect.ts`, `src/llm.ts`, `src/commands/onboard.ts`, `src/onboard-state.ts`, `src/starters.ts`. Admission/persistence: `src/validate.ts`, `src/rule-validation.ts`, `src/curate.ts`, `src/playbook.ts`, `src/tracking.ts`, `src/lock.ts`. Reload/consumption: `src/commands/context.ts`, `src/cass.ts`, `src/scoring.ts`, `src/semantic.ts`, `src/commands/serve.ts`, `src/commands/project.ts`. Maintenance/feedback/safety: `src/commands/playbook.ts`, `src/commands/mark.ts`, `src/commands/outcome.ts`, `src/outcome.ts`, `src/commands/hook.ts`, `src/commands/guard.ts`, `src/trauma.ts`, `src/trauma_guard_script.ts`, plus the registered CLI's remaining commands and config/privacy/sanitization/workspace/output helpers. Entry points, producers, persistence, reload, host drivers and evaluators' consumers were located; deeper inspection of unquoted helper and maintenance paths remains for later jobs, with no access gap. |
| `test/` | Included evaluator and fixture contracts; selected inspection | `test/learning-loop.e2e.test.ts` traces stubbed reflect → context → feedback → curation; `test/context-retrieval-benchmark.test.ts` compares rankers on labelled queries; `test/ace-pipeline.e2e.test.ts` coverage inventory. CLI suites for context, reflect, onboard, serve, hook, playbook, outcome, privacy, trauma and guard, integration suites, helpers, fixtures, `test/E2E_PLAN.md` and `test/GAP_ANALYSIS.md` remain available for deeper inspection. No tests were run. |
| `tsconfig.ci.json` | Included build/evaluation context; inventory only | CI TypeScript configuration, not proof of typecheck success. |
| `tsconfig.json` | Included build context; inventory only | Compiler configuration, not a runtime mechanism. |
| `types.d.ts` | Included build/runtime typing context; searched | Ambient declarations for the shipped environment; runtime correctness not inferred from declarations. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Dicklesworthstone/cass_memory_system` | 8aca3bbb6732321dca041b32c155617784687897 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/cass-memory-system-30c18219cf68/related-systems/Dicklesworthstone--cass_memory_system`. Implementation: tracked tree and entry-point inventory; selected ranges in `package.json`, `src/cm.ts`, `src/commands/context.ts`, `src/commands/reflect.ts`, `src/orchestrator.ts`, `src/reflect.ts`, `src/llm.ts`, `src/diary.ts`, `src/validate.ts`, `src/playbook.ts`, `src/commands/onboard.ts`, `src/commands/playbook.ts`, `src/commands/mark.ts`, `src/commands/serve.ts`, `src/commands/hook.ts`, `src/commands/project.ts`, `src/trauma.ts`, `src/trauma_guard_script.ts`, `src/cass.ts`; selected test source and bounded searches of build, maintenance and delivery paths listed above. Doctrine/design: selected `README.md`, `SKILL.md`, `AGENTS.md`, `docs/planning/AGENTS.md.blurb`, onboarding guide search and `.cass/playbook.yaml`. Listed paths record initial inspection, not an allowlist. | Implementation: [entry point](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/src/cm.ts), [reflection driver](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/src/orchestrator.ts), [retained-state consumer](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/src/commands/context.ts), [host hook](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/src/commands/hook.ts), [evaluator contract](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/test/learning-loop.e2e.test.ts). Doctrine/design: [architecture](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/README.md), [agent protocol](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/SKILL.md), [onboarding prompt](https://github.com/Dicklesworthstone/cass_memory_system/blob/8aca3bbb6732321dca041b32c155617784687897/src/commands/onboard.ts). | No checkout access gap. External cass, originating agents, model services and deployed retained-state corpora are not supplied; their internals, completeness, compliance and deployment success cannot be concluded. No observed-run or causal-experiment layer: source tests and documentation do not establish actual performance, useful learning or safety outcomes. |
