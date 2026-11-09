---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MindBase's shipped knowledge-maintenance artifact at c5273d2336c4d686df41c2a1495f14f085707f51, with an initially traced but non-exhaustive operational loop."
run-id: AAS-2026-11-08-mindbase-llm-wiki-32a62759e2b9-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: c5273d2336c4d686df41c2a1495f14f085707f51
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/frankchu91/mindbase-llm-wiki
  revision: c5273d2336c4d686df41c2a1495f14f085707f51
  path: /home/zby/llm/commonplace/.commonplace/worktrees/mindbase-llm-wiki-3a000ece3754/related-systems/frankchu91--mindbase-llm-wiki
  sha256: null
---

# MindBase boundary

## Boundary and evidence

This run analyses MindBase as a persistent, model-maintained knowledge system. Its intended use is to retain user sources, maintain synthesized Markdown knowledge, and supply that retained knowledge to later questions and agent sessions. It is not classified merely as its MCP tool interface or its core library. The repository ships the server that coordinates operations, instructions for an externally hosted builder, and a session-start consumer of persisted context (SRC-1, `README.md`, `apps/server/src/ops/runner.ts`, `apps/plugin/agents/builder.md`, `apps/plugin/hooks/session-start`).

The declared purpose is explicit:

> **An open-source implementation of Andrej Karpathy's LLM Wiki idea: an AI that builds and maintains a wiki from your sources.** Not RAG-in-a-vector-DB. A real markdown wiki on your disk, that an LLM gardens for you between conversations.
> --- `README.md`

The implementation connects model output to persistent knowledge updates. The server's build path gathers retained inputs, calls its model-completion helper, then applies the returned actions (SRC-1, `apps/server/src/ops/runner.ts`):

> const { system, user } = buildPrompt({ core, sources, today: new Date().toISOString().slice(0, 10) });
> const out = await completeJson(ctx, { system, user, schema: buildSchema, maxTokens: 8192 });
>
> emit({ kind: 'phase', phase: 'writing' });
> const result = await applyActions(ctx.projectRoot, out.actions);
> --- `apps/server/src/ops/runner.ts`

Retained state is subsequently reloaded, rather than existing only in the completion that produced it (SRC-1, `apps/server/src/ops/gather.ts`):

> const [context, indexYaml, readme] = await Promise.all([read('context.md'), read('index.yaml'), read('README.md')]);
> return { context, indexYaml, readme };
> --- `apps/server/src/ops/gather.ts`

The functional boundary includes the entire shipped repository artifact: core storage, compilation, retrieval and model adapters; server routes and background workers; web and command-line callers; MCP tools, resources and prompts; plugin commands, agents, hooks and templates; capture clients; and shipped tests and evaluation instructions. These are potential evidence for later jobs, not uniformly inspected implementations. No shipped caller is declared external simply because it invokes an API.

The boundary kind is **complete artifact, partial loop**, not whole-system. Initial inspection traced the server's contribution planning/application, build, research and lint coordinator; action persistence; project-input gathering; the ask route's answer/file-back integration; MCP registration and contribution persistence; and plugin skill, builder and session-start instructions. It did not exhaustively trace every capture client, background worker, legacy compilation path, search implementation or evaluator. Those are available but not yet inspected, not access gaps or deliberate functional exclusions. This prevents an initial claim of exhaustive lifecycle coverage, uniform approval, uniform storage semantics or equivalent behavior across clients. In particular, the README's approval doctrine is not a blanket implementation guarantee: the inspected server runner has distinct contribute, build and research paths (SRC-1, `README.md`, `apps/server/src/ops/runner.ts`).

### Initial coverage and remaining inspection

The tracked tree was enumerated at the frozen commit. The following map records inspection status, not a source-file allowlist.

| Tracked root | Included role and initial inspection | Limit on conclusions |
|---|---|---|
| `apps/` | Included shipped callers and operational drivers. Inspected `server/src/index.ts`, `server/src/ops/{runner,executors,gather}.ts`, `server/src/routes/ask.ts`, `mcp/src/index.ts`, `mcp/src/tools/contribute.ts`, `plugin/skills/mindbase/SKILL.md`, `plugin/agents/builder.md`, and `plugin/hooks/session-start`. Enumerated app launcher, CLI, web, Android, iOS and both extension trees; enumerated other MCP tools, plugin prompts/templates, server routes/workers and tests. | Remaining implementations and client-side consumption/admission controls are not yet traced. No complete cross-client or background-maintenance claim. |
| `packages/` | Included `core/src/` model adapters, storage, ingest, compile, graph/index, search, QA, synthesis, projects, migration, classification, brief and SRS modules, with colocated tests; tree enumerated, implementation not yet inspected. | No detailed core retrieval, migration or model-adapter guarantee established here. |
| `schema/` | Included `conventions.md`, `ingest.md`, `lint.md`, `query.md`, `synthesis.md`; enumerated, not yet read. | Their procedural contracts have not been characterized. |
| `docs/` | Included guide, LLM-wiki explanation, manual smoke checklist, testing walkthrough, remote-access documentation, product/design plans and assets; enumerated, not yet read. | No evaluator results, deployment assurance or realized roadmap conclusions. |
| `README.md` | Included and read: intended use, installation surfaces, data layout and architecture claims. | Doctrine/design evidence, not proof of all claimed implementation behavior. |
| `package.json` | Included and read: workspace build, test, verification and start command wiring. | Test command presence is not an observed test pass. |
| `.claude-plugin/` | Included marketplace integration; enumerated, not yet read. | Installation/discovery correctness not established. |
| `.github/` | Included CI and Pages workflow definitions; enumerated, not yet read. | No CI or publication outcome established. |
| `CHANGELOG.md`, `CLAUDE.md`, `CONTRIBUTING.md` | Included shipped history and contributor/agent instructions; enumerated, not yet read. | No history or contributor-process assessment. |
| `Dockerfile` | Included deployment packaging; enumerated, not yet read. | Container behavior not established. |
| `glama.json`, `mindbase.config.example.json` | Included registry metadata and example configuration; enumerated, not yet read. | No registry or configuration completeness claim. |
| `.gitignore`, `LICENSE` | Included repository policy and licensing material; enumerated, not yet read. | No licensing interpretation or packaging-policy assessment. |
| `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `tsconfig.base.json` | Included dependency/workspace/compiler declarations; enumerated, not yet read. | No reproducible-build or dependency-security claim. |
| `website/` | Included shipped public presentation, media and discovery files; enumerated, not yet read. | No live-site or demonstration-performance claim. |

External dependencies are not separate analysed systems: the Node/Express and MCP SDK runtime dependencies, model providers such as Ollama or optional cloud services, and enclosing clients such as Claude Code provide execution infrastructure. MindBase's shipped adapters, commands and hooks remain inside the boundary; the providers' model internals and the hosts' scheduling, permissions and prompt-obedience enforcement do not. This prevents attributing host-level enforcement or provider quality to MindBase itself. These dependency surfaces are identified by SRC-1, `apps/server/src/index.ts`, `apps/mcp/src/index.ts`, `README.md` and `apps/plugin/agents/builder.md`; their external implementations were not acquired.

The frozen evidence is the acquired Git checkout at **c5273d2336c4d686df41c2a1495f14f085707f51**, verified as HEAD with no working-tree changes reported. The applicability cutoff is **2026-11-08**, the supplied run date, not a claim about the date of the commit. Later repository revisions, linked external idea sources, npm releases, live websites, user knowledge directories and provider services are excluded from evidence. Their absence prevents conclusions about current releases, actual user retention, live deployment or model-output quality. There is no unavailable repository file established by this inspection. No target program, tests, examples or model calls were executed. The overall tier is **code-grounded**; there is no registered observed run or causal experiment.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/frankchu91/mindbase-llm-wiki` | c5273d2336c4d686df41c2a1495f14f085707f51 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/mindbase-llm-wiki-3a000ece3754/related-systems/frankchu91--mindbase-llm-wiki`. Entire tracked tree enumerated. Implementation: `package.json`, `apps/server/src/index.ts`, `apps/server/src/ops/runner.ts`, `apps/server/src/ops/executors.ts`, `apps/server/src/ops/gather.ts`, `apps/server/src/routes/ask.ts`, `apps/mcp/src/index.ts`, `apps/mcp/src/tools/contribute.ts`, `apps/plugin/hooks/session-start`. Doctrine/design: `README.md`, MCP server instructions in `apps/mcp/src/index.ts`, `apps/plugin/skills/mindbase/SKILL.md`, `apps/plugin/agents/builder.md`. Listed paths are initial inspection, not an allowlist. | Implementation: [server coordinator](https://github.com/frankchu91/mindbase-llm-wiki/blob/c5273d2336c4d686df41c2a1495f14f085707f51/apps/server/src/ops/runner.ts), [retained-input gathering](https://github.com/frankchu91/mindbase-llm-wiki/blob/c5273d2336c4d686df41c2a1495f14f085707f51/apps/server/src/ops/gather.ts), [session consumer](https://github.com/frankchu91/mindbase-llm-wiki/blob/c5273d2336c4d686df41c2a1495f14f085707f51/apps/plugin/hooks/session-start). Doctrine/design: [README](https://github.com/frankchu91/mindbase-llm-wiki/blob/c5273d2336c4d686df41c2a1495f14f085707f51/README.md), [builder contract](https://github.com/frankchu91/mindbase-llm-wiki/blob/c5273d2336c4d686df41c2a1495f14f085707f51/apps/plugin/agents/builder.md). | No repository access gap established. Available but uninspected material is identified above and prevents whole-system coverage claims. No observed execution, external host/provider implementation or user corpus: cannot establish operational success, model compliance, retention quality or host enforcement. |
