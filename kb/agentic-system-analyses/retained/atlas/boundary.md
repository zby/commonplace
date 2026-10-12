---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ATLAS's shipped logistics context, knowledge-maintenance and chat system at commit 65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988."
run-id: AAS-2026-10-12-atlas-b28ea1ea613f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/cargofy/ATLAS
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/atlas-b28ea1ea613f/related-systems/cargofy--ATLAS
  revision: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
  sha256: null
---

# ATLAS boundary

## Boundary and evidence

ATLAS qualifies as a memory/knowledge/context-engineering system, not merely a returning MCP query tool. Its intended use is to give agents logistics context from locally indexed operational data and enterprise knowledge. The shipped implementation includes model-driven extraction, knowledge-file maintenance and an internal conversational tool loop. The boundary covers the complete repository system, including its own callers and deployment entry points, rather than only the `KnowledgeEngine` library. Evidence is SRC-1, especially `README.md`, `package.json`, `src/ui-server.js`, `src/ai/extract-pipeline.js`, `src/ai/knowledge-engine.js` and `src/ai/chat.js`.

The retention-to-consumption connection is explicit in the shipped chat prompt (SRC-1, `src/ai/chat.js`):

> Use read_knowledge to fetch content. Use save_knowledge to store findings.
> --- `src/ai/chat.js`

The executor connects these tools to the same file store used by the knowledge engine (SRC-1, `src/ai/chat.js`):

> case 'read_knowledge':
>       return atlas.readKnowledgeFile(args.path);
>     case 'save_knowledge':
>       return atlas.writeKnowledgeFile(args.path, args.content);
> --- `src/ai/chat.js`

Model-generated maintenance is part of the shipped loop, not an excluded host responsibility. The knowledge engine sends new information and relevant retained files to its LLM, parses proposed updates and applies them through `Atlas`. Its admission point includes this passage (SRC-1, `src/ai/knowledge-engine.js`):

> const validUpdates = updates.filter(u => u && typeof u === 'object' && u.action && u.path);
>
>     // Apply updates
>     const applied = this.applyUpdates(validUpdates, source, date);
> --- `src/ai/knowledge-engine.js`

### Functional scope and entry-point trace

Included responsibilities are configuration and model routing; schema-guided extraction and record admission; database and Markdown persistence; connector and module progress state; scheduled enrichment; human knowledge editing; later knowledge retrieval and chat tool execution; MCP exposure; and the shipped evaluation code. The web server, CLI, browser callers and seed loaders belong to ATLAS. They are not external merely because they call its core API.

The inspected entry points establish these paths (all SRC-1):

- `package.json` starts `src/index.js` for stdio MCP and `src/ui-server.js` for the combined web/API/MCP server. Both bootstrap `Atlas` and `ConnectorRunner`. `bin/atlas.js` adds configuration, seeding, status and web-server startup. `Dockerfile` defaults to the web server.
- `src/ui-server.js` starts `ModelRegistry` and `ModuleLoader`; its import endpoints invoke record loading or `processFile`, and its enrichment endpoint invokes `KnowledgeEngine.enrichFromText`. `src/ai/extract-pipeline.js` reads files, invokes extraction, upserts records, records extraction metadata and optionally invokes knowledge enrichment.
- `src/modules/file-watch/index.js` and `src/modules/google-drive/index.js` provide shipped acquisition drivers that supply a knowledge engine to the extraction pipeline. `src/modules/knowledge-enricher/index.js` separately polls extraction-log metadata and calls text enrichment. `src/module-loader.js` persists module state through connector-state methods and schedules module runs.
- `src/atlas.js` supplies database initialization and upserts, record queries, retention pruning, and knowledge-file indexing/read/write/delete. `src/ai/knowledge-engine.js` reloads relevant files for subsequent enrichment. `src/ai/chat.js` indexes available knowledge in its prompt and executes read/save tools in its model loop.
- `src/ui/pages/chat.js` supplies conversation history to the server; `src/ui/pages/knowledge.js` reloads and edits retained files through the KB API. These browser consumers remain included. `src/ui-server.js` also supplies configuration reload and administrative pruning paths.
- `src/__tests__/knowledge-engine.test.js`, `src/__tests__/models.test.js` and `src/validate-models.js` provide inspectable test/validation designs. They were not executed.

The frozen revision is `65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988`; applicability ends at the run-date cutoff, 2026-10-12. The checkout HEAD matches the acquisition pin and its Git status is clean. The evidence tier is code-grounded: executable source and shipped design text, not an observed deployment or causal experiment.

### Top-level coverage

Every top-level tracked entry is classified below. Included paths identify responsibilities within the functional boundary. Inspection is initial boundary tracing, not an assertion that every line has been audited. Available but not yet inspected material is distinguished from unavailable evidence; later jobs may inspect any file at the same pin under SRC-1.

| Top-level entry | Classification and material paths | Inspection status and limits |
|---|---|---|
| `.dockerignore` | Included: build-input filtering | Enumerated; contents not yet inspected. No claim about effective build exclusions. |
| `.github/` | Excluded: issue templates for bugs, connectors and features | Paths enumerated; template contents not inspected. No conclusion about contributor intake procedures. |
| `.gitignore` | Included: local-state tracking policy | Enumerated; contents not yet inspected. No claim about all ignored deployment state. |
| `CONTRIBUTING.md` | Excluded: contributor process | Heading scan only. No conclusion about compliance with contribution rules. |
| `Dockerfile` | Included: dependency build, shipped files, runtime user, web-server entry point | Read completely; no image build or execution evidence. |
| `README.md` | Included: declared use, architecture, setup and capability claims | Read completely as doctrine, not proof of successful operation. |
| `ROADMAP.md` | Excluded: future/release planning | Heading scan only. Planned features cannot establish implemented behavior. |
| `SECURITY.md` | Included: deployment/security doctrine | Heading scan only; detailed policy not yet inspected. No security assurance from the boundary. |
| `bin/` | Included: `bin/atlas.js` setup, seeding, status and start commands | Read completely; shipped state-producing driver included. |
| `claude_desktop_config.json` | Included: external-host launch example | Read completely; host implementation and working interoperability not established. |
| `config.example.yml` | Included: storage, auth, AI role routing, connector and module configuration | Read completely; deployment-specific config and secrets unavailable. |
| `docker-compose.yml` | Included: data, knowledge and inbox persistence mounts | Read completely; deployed volumes not supplied. |
| `logo.png` | Excluded: branding asset | Enumerated, not inspected; no branding/rendering conclusions. |
| `models/` | Included: carrier, document, event, rate, route and shipment JSON schemas consumed by extraction and validation | Schema-title/required-field scan and caller tracing; full schema details not yet inspected. |
| `package-lock.json` | Included: pinned dependency resolution | Enumerated, not yet inspected. No transitive-dependency audit. |
| `package.json` | Included: scripts, CLI mapping and runtime dependencies | Read completely; package dependencies are interfaces, not independently inspected implementations. |
| `seed.js` | Included: sample-data database producer | Bootstrap read and writes searched; sample record bodies not fully inspected. |
| `seed/` | Included: JSON/CSV examples, extension data and Markdown frontmatter templates | Complete path enumeration, README read and seed/import caller trace; fixture bodies not yet inspected. No claim about their realism or correctness. |
| `server.json` | Included: registry metadata, package and remote declarations | Read completely; remote deployment not accessed. |
| `smithery.yaml` | Included: distribution description | Read completely as doctrine, not runtime evidence. |
| `src/` — core and services | Included: `atlas.js`, `models.js`, `mapper.js`, `connector-runner.js`, `module-loader.js`, `pg-adapter.js`, `health.js`, `webhooks.js` | Core bootstrap, persistence/KB/pruning ranges and connector/loader traces inspected; adapter, mapper, health and webhook files read. Remaining query/schema bodies not yet fully inspected. |
| `src/` — entry points and AI | Included: `index.js`, `ui-server.js`, `ai/chat.js`, `ai/extract.js`, `ai/extract-pipeline.js`, `ai/knowledge-engine.js`, `ai/llm-client.js`, `ai/model-registry.js` | Entrypoint bootstrap and service routes traced; all AI files read. MCP and unrelated REST handler details remain available for later inspection. |
| `src/` — acquisition modules | Included: `connectors/api.js`, `connectors/email.js`, `connectors/filesystem.js`; all three built-in module `index.js` and `manifest.json` paths | API/email stubs read; filesystem extraction read; file-watch and knowledge-enricher read; Google Drive processing path read; manifest config scanned. Remaining transport/parser helpers not yet inspected. |
| `src/` — browser consumers | Included: `ui/app.js`, `ui/index.html`, `ui/lib/`, `ui/pages/`, `ui/styles.css` | Page routing/import links searched; chat request and knowledge reload/edit paths read. Remaining presentation, settings and setup details not yet inspected, not excluded. |
| `src/` — evaluators | Included: `__tests__/knowledge-engine.test.js`, `__tests__/models.test.js`, `validate-models.js` | Knowledge test helpers read and test cases searched; model tests and validator read. No test results or quality measurements supplied. |

### External dependencies and evidence limits

External MCP hosts, including Claude Desktop and Cargofy agents, consume ATLAS but their larger action/negotiation loops are excluded. This prevents attributing their decisions, communications or memory lifecycle to ATLAS. The internal chat loop is included instead (SRC-1, `README.md`, `src/index.js`, `src/ui-server.js`, `src/ai/chat.js`).

Model providers and OpenAI-compatible endpoints are external services. ATLAS's provider calls, prompt construction and routing are included; provider internals and actual model responses are unavailable. Consequently this run cannot establish extraction accuracy, enrichment reliability, or unconditional local-only data processing. Source supports configured provider interfaces, not the README's privacy claims as demonstrated deployment facts (SRC-1, `src/ai/llm-client.js`, `src/ai/model-registry.js`, `config.example.yml`, `README.md`).

External REST sources, Google Drive, credentials, optional document parsers, database drivers and installed external modules are dependencies rather than additional frozen sources. Their shipped adapters are included; live data, external plugin implementations and service behavior are not supplied. This prevents conclusions about deployment-specific data completeness, transport success or third-party correctness (SRC-1, `src/connector-runner.js`, `src/connectors/filesystem.js`, `src/modules/google-drive/index.js`, `src/module-loader.js`, `package.json`).

The tree has no tracked `knowledge/` contents, while the Docker build requests that directory. The source therefore supplies knowledge-store code, not a frozen operational KB or a proven buildable image. Missing retained content does not prevent tracing the loop, but does prevent conclusions about deployed knowledge quality and historical evolution (SRC-1, `src/atlas.js`, `Dockerfile`). No target execution was performed. Mock-based tests support the existence of evaluation designs only, not passing tests or observed performance (SRC-1, `src/__tests__/knowledge-engine.test.js`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/cargofy/ATLAS` | 65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/atlas-b28ea1ea613f/related-systems/cargofy--ATLAS`. Implementation: tracked tree, package/CLI/server entry points, AI files, core KB/persistence/pruning ranges, connector runner, module scheduling/state and acquisition/enrichment drivers, browser chat/KB consumers, evaluator designs, deployment files. Doctrine/design: README and example config read; distribution metadata read; security and other document headings scanned. Detailed initial coverage and unread material are listed above; paths are not an allowlist. | Implementation: [web-server callers](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ui-server.js), [knowledge engine](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/knowledge-engine.js), [chat consumer](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/chat.js), [storage](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/atlas.js), [extraction pipeline](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/ai/extract-pipeline.js), [module loader](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/module-loader.js), [tests](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/src/__tests__/knowledge-engine.test.js). Doctrine/design: [README](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/README.md), [configuration](https://github.com/cargofy/ATLAS/blob/65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988/config.example.yml). | Frozen repository accessible. No deployment KB, live provider/service evidence, execution traces, test results or intervention/comparison supplied. Implementation supports source-level operation; doctrine supports attributed intent. Neither establishes observed effectiveness, end-to-end deployment success or causal benefit. |
