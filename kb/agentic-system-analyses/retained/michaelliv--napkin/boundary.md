---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Napkin's shipped vault CLI, SDK, agent skills and evaluators at commit 7582d6a46f5a11995956e60a59c41a5b242109f1."
run-id: AAS-2026-10-12-napkin-2b85bef38252-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7582d6a46f5a11995956e60a59c41a5b242109f1"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/Michaelliv/napkin
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/napkin-workflow-2b85bef38252/related-systems/Michaelliv--napkin
  revision: "7582d6a46f5a11995956e60a59c41a5b242109f1"
  sha256: null
---

# Napkin boundary

## Boundary and evidence

This run analyses Napkin as a file-based memory/knowledge/context-engineering system, not as an enclosing agent runtime. Its intended use is to give agents retained Markdown knowledge through staged orientation, search and reading, with agent instructions for admission and upkeep. The boundary is the whole shipped repository artifact: the CLI and SDK, vault scaffolding, state mutations and reload paths, packaged skills, design documents, compatibility forwarders and evaluator drivers. A model need not run inside the core for this target to qualify: the shipped skills direct model-dependent knowledge selection and maintenance, and shipped benchmarks feed stored notes to an external agent (SRC-1, `README.md`, `skills/distill/SKILL.md`, `skills/tend/SKILL.md`, `bench/longmemeval-eval.ts`).

> napkin is designed as a memory system for agents. Instead of dumping the full vault into context, it reveals information gradually:
> --- `README.md`

> You are preserving knowledge from this session into a napkin vault. Write the
> knowledge itself, not a record of the conversation.
> --- `skills/distill/SKILL.md`

Entry-point tracing starts with `package.json`: the executable is `dist/main.js`, the library export is `dist/index.js`, and the package includes `dist` and `skills`. Their source counterparts are `src/main.ts` and `src/index.ts`. The CLI registers read, search, overview, write, maintenance-inspection and auxiliary command groups. The SDK routes these responsibilities to `src/core/` and `src/utils/`; it is not the entire target by itself (SRC-1, `package.json`, `src/main.ts`, `src/index.ts`, `src/sdk.ts`).

The state loop includes scaffolding folders, templates and `NAPKIN.md`; creating, overwriting, appending, moving and deleting notes; discovering vault layout on subsequent construction; reading files again for retrieval; and loading or rebuilding search and overview caches. The distill skill supplies retention gates, deduplication searches and merge/create decisions. Tend supplies bounded link repair, retirement and duplicate merging. These are model-facing procedures, not an internally scheduled model service (SRC-1, `src/core/init.ts`, `src/templates/coding.ts`, `src/core/crud.ts`, `src/utils/vault.ts`, `src/core/search.ts`, `src/core/overview.ts`, `skills/distill/SKILL.md`, `skills/tend/SKILL.md`).

> const content = fs.readFileSync(path.join(vaultPath, resolved), "utf-8");
> return { path: resolved, content };
> --- `src/core/crud.ts`

The evaluators are included callers, not excluded applications. LongMemEval writes per-round notes into day directories, assigns modification times from session dates, writes a context note, launches pi with a substituted prompt, parses tool activity and scores answers. LoCoMo writes session notes with supplied summaries, observations and adjacent-session links; HotpotQA writes paragraph notes and related links. These paths establish distinct benchmark ingestion and later consumption responsibilities. They do not establish that a normal working session executes the distill or tend skills: benchmark invocations explicitly disable skills (SRC-1, `bench/longmemeval-eval.ts`, `bench/longmemeval-prompt.md`, `bench/locomo-eval.ts`, `bench/hotpotqa-eval.ts`).

> "--no-extensions",
> "--no-skills",
> "--no-prompt-templates",
> "--system-prompt", systemPrompt,
> userPrompt,
> --- `bench/longmemeval-eval.ts`

### Frozen evidence and external limits

The single frozen evidence source is the acquired Git checkout at full commit `7582d6a46f5a11995956e60a59c41a5b242109f1`. HEAD was checked against that pin and the tracked tree inspected read-only. The applicability cutoff is 2026-10-12; this says which evidence the run uses, not that the checkout represents the latest release on that date. Overall evidence is code-grounded. No target, test, benchmark or model call was executed. Code and prompts support an implementation/design account; reported benchmark numbers remain attributed reports rather than observed runs or causal experiments (SRC-1, `bench/README.md`).

External dependencies include the filesystem, Node/Bun tooling, Commander, FerroSearch, Markdown/frontmatter parsers, SQL/expression support and optional Glimpse rendering. Their declarations are available; their implementations are not frozen here. This prevents conclusions about dependency internals, platform behavior and performance beyond Napkin's calling code (SRC-1, `package.json`, `src/core/search.ts`).

Pi, model providers, the separate pi-napkin integration and the benchmark's `.pi/extensions/napkin-context/index.ts` are outside the frozen tree. The benchmark references that extension and checks for it; the tracked tree contains no such file. This is an unavailable external dependency, not an omitted shipped driver. It prevents verification of actual context injection, external tool registration and host scheduling. Napkin's shipped callers and prompts remain included, but host responsibilities are not attributed to Napkin (SRC-1, `README.md`, `bench/longmemeval-eval.ts`, `bench/hotpotqa-eval.ts`).

> Napkin is LLM-free. The distill extension adds intelligence without coupling it to the core tool. The extension:
> --- `docs/distill.md`

`docs/distill.md` describes timer-driven automatic distillation in pi. It is included as doctrine/design, not evidence that the extension implementation ships in this checkout. Likewise, older progressive-disclosure design text is not proof of command availability; the CLI registrations and shipped skills control implementation conclusions (SRC-1, `docs/distill.md`, `docs/agent-memory-progressive-disclosure.md`, `src/main.ts`).

Benchmark datasets, result JSON, private `data-kbs/` corpora and generated build output are not tracked in the frozen tree. `.gitignore` declares these exclusions. Their absence prevents reproducing reported scores, inspecting run traces or auditing private-corpus exposure results. No new source or capture is introduced to fill those gaps (SRC-1, `.gitignore`, `bench/README.md`, `bench/exposure-all.sh`). Package metadata names a different repository URL; the run retains the supplied normalized source identity unchanged and does not follow that URL to another revision (SRC-1, `package.json`).

### Top-level coverage

“Included” establishes the functional boundary, not a claim that every line has already been inspected. Initial inspection follows the entry points through persistence, reload, admission instructions, maintenance and agent consumption. Available material pending detailed inspection is identified separately from unavailable evidence and deliberate exclusions. All rows refer to SRC-1.

| Top-level tracked path | Included or excluded | Role, material paths and initial inspection | Limit or conclusion prevented |
|---|---|---|---|
| `src/` | Included | Fully read `main.ts`, `index.ts`, `sdk.ts`, `core/init.ts`, `core/crud.ts`, `core/search.ts`, `utils/vault.ts`, `utils/vault-internals.ts`, cache/fingerprint utilities, `commands/overview.ts`, `commands/search.ts`, and `templates/coding.ts` plus the template registry. Read the overview result/cache/context entry point; searched daily, properties, templates, links, configuration and CRUD wrappers for their state paths. SDK and CLI expose bases, canvas, bookmarks, tasks, tags, file metadata, graph and update too. | Other template bodies, detailed overview/tokenizer selection, auxiliary core/command bodies, file/frontmatter utilities and test bodies are available but not yet fully inspected. These are included for later source tracing, not access gaps or evidence of successful execution. |
| `skills/` | Included | Fully read `distill/SKILL.md` and `tend/SKILL.md`: model-facing retention gates, placement, merge/create, verification and conservative upkeep. Packaged by `package.json`. | Instructions establish intended agent behavior, not compliance by a particular host or run. |
| `bench/` | Included | Read `README.md`, `longmemeval-prompt.md`, `overview-exposure.ts`, `exposure-all.sh`; read ingestion and pi invocation/scoring sections in `longmemeval-eval.ts`, `locomo-eval.ts`, `hotpotqa-eval.ts`; searched dataset, extension and output paths. Covers shipped callers that create and later consume retained content. | Remaining sampling, judge and aggregation details are available for later inspection. External extension, data and actual result traces are unavailable; no measured-success conclusion follows from source alone. |
| `docs/` | Included | Fully read `agent-memory-progressive-disclosure.md`, `configuration.md`, `designing-cli-for-agents.md`, `distill.md`, `overview-keyword-extraction.md`. Declared retrieval, configuration and host-distillation designs. | Design descriptions need implementation confirmation; no independent run evidence. |
| `legacy/` | Included | Read `napkin-ai/package.json`, `cli.js`, `index.js`: old-package CLI/library forwarders to the external package version declared there. README is available but not yet read. | Delegation is inspectable; the separately installed older package implementation is not frozen. No behavioral-equivalence claim. |
| `.github/` | Included | Fully read `workflows/ci.yml` and `workflows/release.yml`: build/test matrix, publication and deprecated-shim release path. | Workflow definitions are not successful CI or release traces. |
| `README.md` | Included | Fully read usage, SDK, progressive disclosure, templates, benchmarks and external pi integration declaration. | Reported scores and integration descriptions are not observed operation. |
| `AGENTS.md` | Included | Fully read repository development guidance and memory-system conventions. | Developer instructions are not agent execution evidence. |
| `CLAUDE.md` | Included | Tracked symlink entry inspected; companion instruction surface to `AGENTS.md`. | No independent behavioral evidence. |
| `NAPKIN.md` | Included | Tracked empty file verified. Context-note surface; generated template content is in `src/templates/`. | This repository-root instance supplies no substantive project-memory example. |
| `package.json` | Included | Fully read CLI/library exports, packaged skills, dependencies, build scripts and repository metadata. | Declarations do not establish installed-package contents or dependency behavior. |
| `package-lock.json` | Included | Dependency-lock surface identified in tracked tree; body not yet inspected. | Available but not inspected; no exact dependency-resolution assessment yet. |
| `.gitignore` | Included | Fully read; identifies generated output, local vaults, datasets, results and private evaluation corpora omitted from Git. | Omitted contents cannot supply this run's evidence. |
| `biome.json` | Excluded | Formatting/lint configuration, identified in tracked tree. | No assessment of style-tool configuration; does not exclude a memory-loop responsibility. |
| `tsconfig.json` | Included | Build/compiler configuration identified in tracked tree; body not yet inspected. | No compiler-option or emitted-code equivalence assessment yet. |
| `LICENSE` | Excluded | Legal text identified in tracked tree. | No independent licensing interpretation. |
| `.charts/` | Excluded | `.DS_Store`, five `output/longmemeval-*.png` presentation assets, and `settings.json`; settings read. | Chart rendering and visual benchmark presentation are not audited. Images are not treated as raw run evidence; benchmark drivers and reported tables remain included. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Michaelliv/napkin` | 7582d6a46f5a11995956e60a59c41a5b242109f1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/napkin-workflow-2b85bef38252/related-systems/Michaelliv--napkin`. Implementation: tracked tree and entry-point tracing through `package.json`, `src/main.ts`, `src/index.ts`, `src/sdk.ts`, `src/core/init.ts`, `src/core/crud.ts`, `src/core/search.ts`, overview entry point, vault discovery, caches/fingerprint, template registry/coding template, retrieval wrappers, benchmark ingestion and pi callers, evaluator helpers, legacy forwarders and workflows. Scoped searches add daily/properties/templates/links/configuration and wrapper state paths. Doctrine/design: README, AGENTS, both skill files and all five docs. Reported operation: README and benchmark README tables only. Coverage table distinguishes pending inspection from unavailable material. | Implementation: [CLI](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/main.ts), [SDK](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/sdk.ts), [persistence/read](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/src/core/crud.ts), [benchmark caller](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/longmemeval-eval.ts). Doctrine/design: [admission skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/distill/SKILL.md), [upkeep skill](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/skills/tend/SKILL.md), [external distillation design](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/docs/distill.md). Reported operation: [benchmark report](https://github.com/Michaelliv/napkin/blob/7582d6a46f5a11995956e60a59c41a5b242109f1/bench/README.md). | External pi/extension/provider and dependency implementations are not frozen: no verification of host scheduling, injection or provider/dependency behavior. Dataset/result/private-corpus contents and execution traces are unavailable: no reproduced accuracy, observed agent compliance or causal efficacy conclusion. Generated distribution is absent: source entry points, not an inspected installed build. No observed-run or causal-experiment layer is claimed. |
