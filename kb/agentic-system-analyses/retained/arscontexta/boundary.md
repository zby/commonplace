---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Ars Contexta's shipped knowledge-system derivation and operating loop at commit 2acfd5cc4473c4d06c46be63df748e77e00e2746."
run-id: AAS-2026-10-12-arscontexta-f9e5f2f34166-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "2acfd5cc4473c4d06c46be63df748e77e00e2746"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/agenticnotetaking/arscontexta
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/arscontexta-f9e5f2f34166/related-systems/agenticnotetaking--arscontexta
  revision: 2acfd5cc4473c4d06c46be63df748e77e00e2746
  sha256: null
---

# Ars Contexta boundary

## Boundary and evidence

This run analyses Ars Contexta as a shipped memory/knowledge/context-engineering system, including both its conversational builder and the operating procedures it generates. The intended use is to explain how the plugin derives a persistent Markdown vault, supplies processing and maintenance instructions, and reloads retained state for later model work. It is not a standalone enclosing model runtime. The model-dependent paths are prompt procedures served to Claude Code; executable hooks provide a narrower deterministic layer. SRC-1: `.claude-plugin/plugin.json`, `skills/setup/SKILL.md`, `skill-sources/ralph/SKILL.md`, `hooks/hooks.json`.

The whole-system boundary includes plugin discovery, onboarding and derivation, context-file composition, presets, note and queue creation, quality checks, connection finding, backward updates, session persistence and orientation, retrieval of retained content, and approval-based architecture evolution. Generated artifacts are included as specified by the shipped procedures and templates, not as observed installations. Setup explicitly consumes the skill sources and writes them into the user's project (SRC-1: `skills/setup/SKILL.md`):

> 1. Read `${CLAUDE_PLUGIN_ROOT}/skill-sources/[name]/SKILL.md`
> 2. Apply vocabulary transformation — rename and update ALL internal references using the vocabulary mapping from `ops/derivation.md`
> 3. Adjust skill metadata (set `context: fork` for fresh context per invocation)
> 4. Write the transformed SKILL.md to the user's skills directory
> --- `skills/setup/SKILL.md`

The supplied queue driver is part of the target, not an excluded application. Its declared responsibility connects persisted queue state to model work and back to queue updates (SRC-1: `skill-sources/ralph/SKILL.md`):

> The lead session's ONLY job is: read queue, spawn subagent, evaluate return, update queue, repeat.
> --- `skill-sources/ralph/SKILL.md`

Consumers of retained content are also within scope. Reflect reads existing notes, follows curated topic maps and searches semantic neighbors; remember's declared learning loop writes operational guidance for later sessions. These are instructions, not demonstrated effects on model behavior (SRC-1: `skill-sources/reflect/SKILL.md`, `skill-sources/remember/SKILL.md`). The installed session hook provides inspectable reload behavior (SRC-1: `hooks/scripts/session-orient.sh`):

> if [ -f self/identity.md ]; then
>   cat self/identity.md self/methodology.md 2>/dev/null
>   echo ""
> fi
> --- `hooks/scripts/session-orient.sh`

Plugin hooks and generated hook templates are distinct surfaces within this boundary. The plugin registers SessionStart and PostToolUse, whereas setup specifies generated Stop capture and the platform ships its template. They must not be treated as one verified deployment. Similarly, the platform generator's claim that processing skills are inherited differs from setup's explicit copying procedure; both remain evidence for later reconciliation, not a reason to exclude either path (SRC-1: `hooks/hooks.json`, `skills/setup/SKILL.md`, `platforms/claude-code/generator.md`, `platforms/claude-code/hooks/session-capture.sh.template`).

### Frozen evidence and limits

The sole frozen source is SRC-1, the repository at full commit `2acfd5cc4473c4d06c46be63df748e77e00e2746`. The acquired checkout's HEAD matches that pin. The applicability cutoff is 2026-10-12, the opening's run date, not an assertion that the repository reflects all live behavior on that date. No other repository, website, moving documentation or source revision supplies evidence.

The overall tier is code-grounded because hook implementations, hook registration and the kernel validator are inspectable. Most derivation, semantic judgment and model orchestration remain doctrine/design expressed as Markdown prompts. No target code, tests or examples were executed. Source-native validation reports support only attributed reported operation, not independently observed runs or causal experiments (SRC-1: `reference/derivation-validation.md`).

External dependencies include Claude Code for skill loading, context loading, tool execution and subagent scheduling; shell utilities and Git for hooks and persistence; and optional qmd/MCP search for semantic retrieval (SRC-1: `README.md`, `skill-sources/reflect/SKILL.md`). These implementations are excluded: this run cannot establish host enforcement, subagent isolation, provider behavior or qmd indexing and ranking correctness. User vaults, actual generated files and live session transcripts are not supplied as run evidence. This prevents conclusions about successful installation, actual session continuity, retrieval quality or learning outcomes. Source-native test plans and fixtures remain included, but are not proof of test execution. Available source files not yet read are pending inspection, not access gaps.

### Top-level coverage

Every top-level tracked file or directory is classified below. All directory families remain included; initial inspection traces the material loop rather than claiming an exhaustive file audit. Each row uses SRC-1 at the frozen revision.

| Top-level path | Classification and material paths | Role and initial inspection / exclusion limit |
|---|---|---|
| `.claude-plugin/` | Included: `plugin.json`, `marketplace.json` | Plugin identity and installation entry. Manifest read; marketplace enumerated, not yet inspected. |
| `.gitignore` | Excluded | Checkout hygiene; no claim about ignored local artifacts or their retention. |
| `LICENSE` | Excluded | Licensing; legal permissions are not assessed. |
| `README.md` | Included; read | Install path, advertised workflow, dependency declarations and repository map. Claims remain attributed design. |
| `agents/` | Included: `knowledge-guide.md`; read | Shipped proactive guidance consumer of methodology and claim-map; not equated with the queue's differently named worker. |
| `generators/` | Included: `claude-md.md`, `features/processing-pipeline.md`, `features/session-rhythm.md`, `features/maintenance.md`, `features/self-evolution.md`, `features/semantic-search.md`, schema and other feature blocks | Context composition, session rhythm, navigation and evolution rules. Generator routing and selected feature headings searched; full blocks pending. |
| `hooks/` | Included: `hooks.json`, `scripts/session-orient.sh`, `scripts/write-validate.sh`, `scripts/auto-commit.sh`, `scripts/vaultguard.sh`, `scripts/read_config.sh` | Registered deterministic path for reload, post-write warnings and persistence. Registration, orientation and write validation read; guard/config/commit bodies pending. |
| `methodology/` | Included: `index.md`, `derivation-engine.md`, `memory-architecture.md`, `processing-workflows.md`, `maintenance-patterns.md` and linked claim corpus | Bundled knowledge consumed by setup, ask and guidance. Tree and consumer routing inspected; individual claims pending, with no endorsement of their research validity. |
| `platforms/` | Included: `claude-code/generator.md`, `claude-code/hooks/*.template`, `shared/skill-blocks/*.md`, `shared/features/README.md`, `shared/templates/README.md` | Platform adaptation, generated persistence/reload hooks and alternate skill-generation surfaces. Generator routing searched, Stop template read, reflect/remember/next block structure searched; remaining templates pending. |
| `presets/` | Included: research/personal/experimental `preset.yaml`, `vocabulary.yaml`, `categories.yaml`, `starter/` | Configuration, vocabulary, extraction categories and starter navigation. Research preset read; other preset files enumerated, pending inspection. |
| `reference/` | Included: `kernel.yaml`, `validate-kernel.sh`, `templates/`, `test-fixtures/`, `testing-milestones.md`, `derivation-validation.md`, claim/dimension maps and architecture/evolution references | Contracts, schemas, evaluator implementation, test plans and source-native reports. Validator start read and later checks searched; milestone/test headings and first self-derivation report inspected. Other reference bodies, including native audit, pending. |
| `scripts/` | Included: `sync-thinking.sh`; read | Maintainer-side import of research content from an external vault to `thinking/`. The external vault is not evidence; source script does not establish that its output matches bundled `methodology/`. |
| `skill-sources/` | Included: all 16 `*/SKILL.md` and metadata; particularly seed/reduce/pipeline/ralph, reflect/reweave/verify/validate, graph/next/tasks/stats, learn/remember/rethink/refactor | Retained-source admission, extraction and note creation, queue reload/advancement, retrieval and connection updates, quality gates, operational learning and restructuring. All skill descriptions/headings searched; ralph queue/driver, reflect retrieval, verify checks and remember feedback loop read in bounded ranges. Other bodies and metadata pending. |
| `skills/` | Included: setup, help, tutorial, ask, health, recommend, architect, add-domain, reseed and upgrade | Model-served plugin entry points, bundled-knowledge retrieval, diagnosis and configuration evolution. Descriptions/headings searched across all commands; setup generation/hook installation read and ask routing searched. Other command bodies pending. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/agenticnotetaking/arscontexta` | 2acfd5cc4473c4d06c46be63df748e77e00e2746 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/arscontexta-f9e5f2f34166/related-systems/agenticnotetaking--arscontexta`. Implementation: `hooks/hooks.json`, `hooks/scripts/session-orient.sh`, `hooks/scripts/write-validate.sh`, capture hook template, `scripts/sync-thinking.sh`, portions of `reference/validate-kernel.sh`. Doctrine/design: README, manifest, setup skill-generation and hook sections, ralph queue/driver, reflect retrieval, verify checks, remember learning loop, research preset; scoped heading/routing searches as detailed above. Reported operation: first self-derivation report in `reference/derivation-validation.md`. | Implementation: [session orientation](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/hooks/scripts/session-orient.sh), [kernel validator](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/reference/validate-kernel.sh). Doctrine/design: [setup](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skills/setup/SKILL.md), [queue driver](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/skill-sources/ralph/SKILL.md). Reported operation: [derivation report](https://github.com/agenticnotetaking/arscontexta/blob/2acfd5cc4473c4d06c46be63df748e77e00e2746/reference/derivation-validation.md). | No checkout access gap established. External host, search/provider implementations and actual user vault/run artifacts are outside the frozen evidence. Implementation supports source behavior, not successful execution; prompts support intended model procedure, not compliance; native reports do not establish independently observed or causal outcomes. |
