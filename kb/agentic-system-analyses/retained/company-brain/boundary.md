---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Company Brain's shipped Slack agent, memory lifecycle, background work and administration at commit ef8a45ef3aed97b32599c7d8007edefab6d14e9a."
run-id: AAS-2026-10-14-company-brain-30a9e8cfaeca-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: ef8a45ef3aed97b32599c7d8007edefab6d14e9a
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/supermemoryai/company-brain
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/company-brain-30a9e8cfaeca/related-systems/supermemoryai--company-brain
  revision: ef8a45ef3aed97b32599c7d8007edefab6d14e9a
  sha256: null
---

# Company Brain boundary

## Boundary and evidence

This analysis covers the self-hostable Company Brain application, not merely its memory search API. Its intended use is to explain how the shipped Slack agent admits requests and observations, retains company knowledge, later retrieves it, acts through connected tools, and maintains its state. The frozen revision is `ef8a45ef3aed97b32599c7d8007edefab6d14e9a`; the applicability cutoff is 2026-10-14. The overall evidence tier is code-grounded. HEAD was checked against the acquired commit, and the checkout was inspected read-only.

**Classification: enclosing runtime; whole-system.** Company Brain owns the application-level model/tool loop and its Slack and scheduled callers. Cloudflare and the Agents SDK supply infrastructure underneath that runtime; their presence does not make the shipped Slack driver an excluded enclosing application. The deployed worker exports the Durable Object, mounts the shipped HTTP routes and serves the shipped UI (SRC-1, `src/worker.ts`, `wrangler.jsonc`). Slack events dispatch into the organization's agent; the model loop selects the model, messages, tools and stopping conditions (SRC-1, `src/routes/slack/index.ts`, `src/brain/turn/agent.ts`, `src/brain/turn/loop.ts`). Minimum implementation anchors for this classification:

> export class CompanyBrainAgent extends Agent<Env, CompanyBrainState> {
> --- `src/brain/turn/agent.ts`

> return args.deps.streamText({
> model: args.deps.getModel(args.profile.name, args.env),
> system: args.system(),
> messages: initialMessages,
> tools: args.tools,
> activeTools: resolveActiveTools(),
> abortSignal: args.abortSignal,
> stopWhen: [
> args.deps.stepCountIs(limit),
> () => args.suspendRequested?.() === true,
> ],
> --- `src/brain/turn/loop.ts`

The functional boundary includes installation and authentication, event admission, explicit and passive Slack turns, turn coordination and finalization, approvals and access leases, tool discovery and execution, sandbox integration, memory capture and retrieval, organization and personal configuration, skills, signup research, operator-triggered research, scheduled tasks and administration. Shipped callers remain inside the boundary even when they supply state to `computeTurn` rather than implement the loop themselves (SRC-1, `src/routes/index.ts`, `src/brain/slack/turn.ts`, `src/brain/tools/scheduling.ts`, `src/brain/auto-research/draft.ts`).

The memory loop was traced across its shipped producers and consumers. Completed interactive Slack turns call `writeMemories`; channel observation uses a model to select durable clusters and persists a batch before writing it. `writeMemory` passes documents through the compatibility adapter, registers tags and tree mappings, and initiates node splitting. Read scope is resolved before semantic search, and `search_company_brain` calls that search from the turn's tool set. Ambient profile, interaction style, workspace prompt and skills are loaded into turn context. Delayed post-turn observation writes team-level operating/style notes to the agent-self container, while research planning and scheduled turns consume retained context. These paths are included rather than treated as external maintenance (SRC-1, `src/brain/slack/turn.ts`, `src/brain/slack/channel-observe.ts`, `src/brain/memory/index.ts`, `src/brain/memory/read-scope.ts`, `src/brain/memory/search-brain.ts`, `src/brain/turn/tools.ts`, `src/brain/turn/compute.ts`, `src/brain/turn/post-turn-reflect.ts`, `src/brain/turn/interaction-observe.ts`, `src/brain/memory/split.ts`, `src/brain/auto-research/plan.ts`, `src/brain/tools/scheduling.ts`). This establishes scope and initial loop coverage, not the correctness of every permission or stale-write safeguard.

**External dependencies and evidence limits.** Supermemory's hosted service, model providers, Slack, remote MCP servers and connected applications, Cloudflare infrastructure, and optional Daytona infrastructure are outside the implementation source boundary. Their local clients, adapters, policies, deployment configuration and container recipe remain included. The memory adapter explicitly delegates processing to the external service:

> * Write one document into supermemory. Extraction, chunking and embedding all
> * happen server-side, so this is a single API call wrapped as an Effect so the
> * original call sites and their error handling stay intact.
> --- `src/compat/routes/memories/handler-effect.ts`

The inspected adapter calls `client.documents.add`; the memory client constructs a Supermemory SDK client from the deployment key (SRC-1, `src/compat/routes/memories/handler-effect.ts`, `src/memory/client.ts`). No service implementation or frozen remote response is supplied. Consequently this run can establish the application's requests and treatment of returned data, but cannot establish the service's extraction, deduplication, supersession, embedding, ranking or retention behavior internally. Similarly, source-level tool and approval policy cannot establish provider compliance, successful remote actions or end-to-end privacy in a deployed workspace. Dependencies listed in `package.json` and `bun.lock` are not separately acquired sources; only the shipped local patches are part of this implementation boundary (SRC-1, `package.json`, `wrangler.jsonc`, `sandbox/Dockerfile`).

No observed run or causal experiment was supplied. Tests, delivery guards, research draft flags and observability code are included as authored implementation/evaluation surfaces, not evidence that a test passed or a production outcome occurred (SRC-1, `package.json`, `test/workers-shim.ts`, `src/brain/slack/triage.test.ts`, `src/brain/codemode/quickjs-executor.test.ts`, `src/db/migrations.test.ts`, `src/brain/observability/reply-quality.ts`, `src/brain/auto-research/draft.ts`). The target, tests and examples were not executed.

Shipped documentation is eligible as doctrine/design, including declared operation, but is not authoritative over the current implementation. Some architecture references still name a prior monorepo and Postgres deployment; this run instead pins the current worker and D1 configuration (SRC-1, `docs/architecture.md`, `src/worker.ts`, `wrangler.jsonc`). The documentation itself warns:

> `spec.md` predates recent work and still has stale passages, so
> treat neither as authoritative over the code.
> --- `docs/README.md`

### Top-level tracked coverage

Every top-level tracked entry at the frozen commit is classified below. “Included” means eligible within the functional boundary, not exhaustively read. “Not initially inspected” denotes available material, not an access gap. Later analysis may inspect it at the same pin. Directory rows identify material paths, including the shipped state producers, maintenance paths, consumers and evaluation surfaces.

| Top-level entry | Classification and role | Initial inspection and limitation |
|---|---|---|
| `.dev.vars.example` | Included: deployment input template | Enumerated, not initially inspected; no claim about complete secret/default coverage. |
| `.gitattributes` | Excluded: repository attribute policy | Deliberate nonfunctional exclusion; prevents conclusions about checkout normalization policy, not the agent loop. |
| `.gitignore` | Excluded: ignored-file policy | Deliberate nonfunctional exclusion; no conclusions about untracked deployment state. |
| `LICENSE` | Excluded: licensing | Deliberate exclusion; no legal/licensing assessment. |
| `README.md` | Included: current product intent and self-hosted deployment contract | Read completely; claims of prior user counts and example Slack conversations are not observed-run evidence. |
| `bun.lock` | Included: dependency resolution | Enumerated, not initially inspected; no dependency audit or verification of installed bytes. |
| `bunfig.toml` | Included: test harness configuration | Read; points to `test/workers-shim.ts`. |
| `docs/` | Included: design, user permissions, connector/automation instructions and operational runbooks | Read `docs/README.md` and `docs/architecture.md`; searched selected passages of `docs/spec.md` and `docs/agent.md`. `docs/slack.md`, `docs/guide/`, `docs/local-dev.md`, `docs/do-split-runbook.md` and `docs/slack-app-manifest.yaml` are available, not initially read. Older deployment statements require code corroboration. |
| `drizzle.config.ts` | Included: schema-generation configuration | Enumerated, not initially inspected; no schema-generation correctness claim. |
| `drizzle/` | Included: D1 schema and migration history, specifically `0000_fluffy_sabretooth.sql` and `meta/` | Enumerated; migration bundling/application call sites and migration-test declarations were searched. Migration contents not initially read. |
| `env-supplement.d.ts` | Included: environment type supplements | Enumerated, not initially inspected; declaration completeness not established. |
| `package.json` | Included: build/deploy/test entry points, SDK dependencies and local patch bindings | Read completely; dependency runtime behavior not inspected. |
| `patches/` | Included: local changes to Code Mode and gateway provider, `@cloudflare%2Fcodemode@0.4.3.patch` and `ai-gateway-provider@3.1.3.patch` | Enumerated and linked from inspected package metadata; contents not initially inspected, not excluded from later implementation analysis. |
| `sandbox/` | Included: optional execution environment recipe, `Dockerfile` | Read completely; upstream container image contents and actual isolation are unavailable, so no runtime containment claim. |
| `scripts/` | Included: migration production, `bundle-migrations.ts` | Searched bundling inputs and generated output; not executed. |
| `src/` | Included: worker entry; auth/setup/config; database; memory clients and compatibility adapters; all agent and HTTP state paths | Read `src/worker.ts`, `src/routes/index.ts`, `src/routes/workspace-prompt.ts`, `src/memory/client.ts`, `src/memory/documents.ts`, `src/compat/routes/memories/handler-effect.ts`, `src/brain/memory/index.ts`, `read-scope.ts`, `search-brain.ts`, `src/brain/turn/loop.ts`, `finalization/index.ts`, and `src/brain/observability/reply-quality.ts`. Inspected bounded ranges/searches of `src/routes/slack/index.ts`, `src/routes/{skills,memories,graph}.ts`, `src/db/{index,migrate,migrations.test}.ts`, `src/brain/slack/{turn,channel-observe}.ts`, `src/brain/turn/{agent,agent.impl,compute,post-turn-reflect,interaction-observe,research,tools}.ts`, `src/brain/prompt/{build,system}.ts`, `src/brain/memory/{split,profile-sync,interaction-style}.ts`, `src/brain/auto-research/{run,plan,draft}.ts`, and `src/brain/tools/scheduling.ts`. Lease, journey, MCP, sandbox, skill-store, profile-recall and other leaf implementations remain eligible but not exhaustively inspected. Test declarations in Slack triage and QuickJS executor were inspected by search; no test results. |
| `test/` | Included: outside-workerd test support, `workers-shim.ts` | Read completely; inert mocks do not establish deployed Durable Object behavior. |
| `tsconfig.json` | Included: implementation module mapping | Read completely; confirms `@/lib/brain`, compatibility and `@repo/db` imports resolve inside this checkout rather than to an excluded host. |
| `web/` | Included: shipped administration and retained-state consumption UI | Read `web/app.tsx`; tree identifies `components/memory-graph/`, `components/settings/`, `components/configure-view.tsx`, `hooks/`, `lib/auth-context.tsx`, `main.tsx`, `build.ts`, `ui/` and `public/`. Entry routes include home, graph and configuration. Detailed UI editors, fetch hooks, build and decorative assets not initially inspected; no browser behavior or UI/API permission-equivalence conclusion. |
| `worker-configuration.d.ts` | Included: generated runtime binding declarations | Enumerated, not initially inspected; live binding provision is not verified. |
| `wrangler.jsonc` | Included: current shipped deployment entry and state bindings | Read completely: worker, UI assets, D1, KV, Durable Objects, AI and optional container configuration. Deployment success not observed. |
| `wrangler.reference.jsonc` | Included: reference deployment configuration | Enumerated, not initially inspected; equivalence with the active configuration is not assumed. |

The whole-system designation covers the shipped application responsibility loop; it does not claim exhaustive line-level inspection or include remote service internals. No material shipped path was found inaccessible. Available but unread leaf files above are follow-up evidence, not grounds for describing their mechanisms now.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/supermemoryai/company-brain` | ef8a45ef3aed97b32599c7d8007edefab6d14e9a | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/company-brain-30a9e8cfaeca/related-systems/supermemoryai--company-brain`. Implementation: tracked-tree enumeration; worker/deployment and package entry points; current router and Slack dispatch; agent shell and model loop; turn memory writeback, semantic search and read scopes; channel observation, post-turn style observation and node splitting; context assembly and shipped prompts; scheduled and research consumers; workspace-prompt administration, UI entry and evaluation/test surfaces, at the paths and read depths listed in the coverage table. Doctrine/design: complete root README and docs index/architecture, selected spec passages, and embedded system/maintenance prompts. | Implementation: [worker](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/worker.ts), [model loop](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/brain/turn/loop.ts), [memory write](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/brain/memory/index.ts), [channel observation](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/brain/slack/channel-observe.ts), [memory service adapter](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/compat/routes/memories/handler-effect.ts). Doctrine/design: [product README](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/README.md), [documentation warning](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/docs/README.md), [system prompt](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/brain/prompt/system.ts). | Implementation: external services, installed dependency implementations and actual deployment state are not supplied; prevents claims about their internal mechanisms or successful end-to-end operation. No observed-run or causal-experiment evidence; prevents measured effectiveness, production reliability and causal outcome claims. Doctrine/design: historical documentation contains stale paths/storage assumptions; prevents treating declared deployment behavior as current implementation without corroboration. Available unread files are identified separately in coverage, not classified as access gaps. |
