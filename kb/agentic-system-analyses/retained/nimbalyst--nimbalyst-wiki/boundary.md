---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Nimbalyst Wiki's released plugin instructions and integration manifests at 97c1ba1594d6e3d466a23d33c1bda084026b01b8, with external persistence and hook implementations outside the frozen evidence."
run-id: AAS-2026-11-08-nimbalyst-wiki-d9ff54186a76-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "97c1ba1594d6e3d466a23d33c1bda084026b01b8"
analysis-cutoff: "2026-11-08"
evidence-tier: doc-grounded
source:
  identity: https://github.com/nimbalyst/nimbalyst-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/nimbalyst-wiki-34dbf869503f/related-systems/nimbalyst--nimbalyst-wiki
  revision: "97c1ba1594d6e3d466a23d33c1bda084026b01b8"
  sha256: null
---

# Nimbalyst Wiki boundary

## Boundary and evidence

This run analyses the released Nimbalyst Wiki plugin artifact: agent instructions for creating, maintaining and recalling a project wiki, its local file contract, host integration declarations, and the optional team-server add-on. It is an in-scope knowledge and context-engineering system because its shipped prompts direct coding agents to persist session decisions and later read them before answering or changing code. It is not an enclosing model runtime. The instructions rely on the host agent's model and tools rather than supplying a model execution loop (SRC-1, `skills/capture/SKILL.md`, `skills/recall/SKILL.md`, `.mcp.json`).

> Find what the project's wiki already says before answering or changing code. This skill only reads; the `capture` and `update` skills write.
> --- `skills/recall/SKILL.md`

> Record what this session decided in the project's wiki. Load the `update` skill and follow it for every write; the `connect` skill covers choosing the wiki and finding the project.
> --- `skills/capture/SKILL.md`

The boundary is **complete artifact, partial loop**, not whole-system. All tracked plugin files at the frozen commit are eligible evidence, including the shipped callers and prompt references. However, persistence, retrieval tools, session transcript readers, browser editing and hook commands are delegated to code not shipped in this repository. Inspection traced the root Claude Code and Codex manifests into the local/session MCP declarations and hook declarations, then followed the seven skills' consumers of those tools. The team add-on points to a hosted MCP endpoint. These are material runtime responsibilities, not capabilities implemented by the Markdown prompts (SRC-1, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.mcp.json`, `.codex-mcp.json`, `hooks/hooks.json`, `nimbalyst-wiki-team/.mcp.json`, `CONTRIBUTING.md`).

> The plugin itself holds no code. Both servers and both hooks run the [`@nimbalyst/cli`](https://www.npmjs.com/package/@nimbalyst/cli) package from npm through `npx`, pinned to the plugin's version, so its source is published with each release. The first session downloads it, including the browser app; later sessions use npm's cache and work offline.
> --- `README.md`

The manifests specify `@nimbalyst/cli@0.12.4`: local MCP invokes `mcp`, session MCP invokes `hook session-inputs`, and Claude Code hooks invoke `hook session-start` and `hook stop`. The team add-on declares `https://sync.nimbalyst.com/mcp`. This establishes the integration wiring, not the behavior of those external programs or services (SRC-1, `.mcp.json`, `.codex-mcp.json`, `hooks/hooks.json`, `nimbalyst-wiki-team/.mcp.json`, `nimbalyst-wiki-team/.codex-mcp.json`).

Intended use is a project wiki holding decisions, reasons, open questions and useful context. Functional inclusions cover choosing the current local/team destination; initial wiki construction; capturing decisions into affected pages; citations and identity rules; schema/type and link conventions; code-to-page coverage and maintenance instructions; recall before work; and team migration/invitation instructions. The local storage contract is included as declared design, not verified implementation (SRC-1, `README.md`, `FORMAT.md`, `skills/connect/SKILL.md`, `skills/setup/SKILL.md`, `skills/capture/SKILL.md`, `skills/update/SKILL.md`, `skills/recall/SKILL.md`, `skills/team/SKILL.md`).

The evidence is frozen at Git revision **97c1ba1594d6e3d466a23d33c1bda084026b01b8**, with applicability cutoff **2026-11-08**. The acquired checkout's HEAD was checked against that revision. The overall tier is **doc-grounded**: inspectable prompt text, configuration and format contracts support intended operation; no executable server implementation or observed execution establishes actual operation. No target code, tests, examples or providers were executed.

### Artifact coverage and limits

The inventory below accounts for every tracked top-level file or directory. It records initial inspection, not a restriction on later inspection at this same commit.

| Top-level path | Treatment and initial inspection | Role and conclusion limit |
| --- | --- | --- |
| `.claude-plugin/` | Included; `plugin.json`, `marketplace.json` read | Main plugin identity and registration of local/team artifacts; not evidence that a host loaded them. |
| `.codex-plugin/` | Included; `plugin.json` read | Codex skill and MCP entry points; not host execution evidence. |
| `.mcp.json` | Included; read | Claude local and session server command declarations; CLI behavior unavailable in this source. |
| `.codex-mcp.json` | Included; read | Codex local/session server declarations and environment forwarding; same implementation gap. |
| `hooks/` | Included; `hooks.json` read | SessionStart/Stop command declarations; actual nudge detection and injected context cannot be verified here. |
| `skills/` | Included; all seven `SKILL.md` files read in full; headings of setup/update reference files searched | Shipped state-producing and state-consuming instructions: `setup`, `capture`, `update`, `recall`, `connect`, `team`, `start`. References include strategic structure, writing guide, components, editor formats, legacy migration and example relations. Reference bodies have not yet been inspected; their details are not established by the heading search and remain available for later jobs. |
| `nimbalyst-wiki-team/` | Included; README, both plugin manifests and both MCP manifests read | Optional hosted team connection and its consumer relationship to the main skills. No hosted server implementation is present, preventing verification of authentication, permissions, migration or collaboration semantics. |
| `README.md` | Included; read in full | Usage, intended lifecycle, CLI/browser/desktop dependencies and reported feature availability. Not observed operation. |
| `FORMAT.md` | Included; read in full | Declared local page, ID, type, CSV, activity, link, trash and concurrency contracts. Cannot establish that external writers enforce them. |
| `CONTRIBUTING.md` | Included; read | Generated-artifact provenance and mapping to implementation packages outside this checkout. |
| `SOURCE` | Included; read | Staging provenance only; its monorepo commit is not a second frozen source. |
| `LICENSE` | Deliberately excluded; not read | Licensing text; no licensing analysis is made. No operational conclusion depends on it. |
| `docs/` | Deliberately excluded; tracked `images/` asset names inventoried, image contents not inspected | README screenshots and logos, not a runtime/evaluation path. Prevents independent visual confirmation of depicted interfaces; screenshots would not establish live behavior. |

The frozen tree has no shipped executable evaluator or test suite. The prompts prescribe read-backs, link checks and `wikiDoctor`, but those instructions are not evaluation results (SRC-1, `skills/setup/SKILL.md`, `skills/update/SKILL.md`; tracked-tree inventory). No supplied trace, benchmark or intervention is registered, so effectiveness, compliance, reliability and causal improvement remain unestablished.

### External dependencies and excluded responsibilities

- **CLI and local-wiki implementation:** npm's CLI package, the local-wiki library, browser app and transcript-reader implementation are outside the frozen repository. `CONTRIBUTING.md` maps these to monorepo packages. This prevents code-grounded conclusions about scanning, locking, conflict rejection, repair, search, freshness calculation, transcript isolation and browser security. `FORMAT.md` and skill descriptions may support only their declared contracts (SRC-1, `CONTRIBUTING.md`, `FORMAT.md`).
- **Agent hosts and desktop app:** Claude Code, Codex, other MCP clients and the Nimbalyst desktop app execute or supersede the plugin instructions. Their code is not included. This prevents verification of prompt loading, tool dispatch, model behavior, hook support or desktop duplicate-write avoidance. These responsibilities are not attributed to the plugin (SRC-1, `README.md`, `skills/connect/SKILL.md`).
- **Hosted teams:** authentication and shared storage live behind the declared team MCP endpoint and console. Their implementation and runtime state are unavailable within this source. This prevents verifying access enforcement, migration resumability, history, collaboration and invitations, while leaving their shipped usage instructions in scope (SRC-1, `nimbalyst-wiki-team/.mcp.json`, `skills/team/SKILL.md`).
- **Installation and update services:** Node.js/npm/npx, registry downloads and documented update endpoints are dependencies, not inspected evidence sources. Version pins in manifests do not freeze downloaded package bytes in this run. Availability, offline behavior and update safety are therefore not established (SRC-1, `.mcp.json`, `README.md`).

`SOURCE` names the upstream staging commit, but neither that monorepo nor npm package contents are acquired here. Following those references would change the evidence boundary; this run retains the supplied repository identity and revision unchanged (SRC-1, `SOURCE`, `CONTRIBUTING.md`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/nimbalyst/nimbalyst-wiki` | 97c1ba1594d6e3d466a23d33c1bda084026b01b8 | doctrine/design; implementation (integration declarations only); reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/nimbalyst-wiki-34dbf869503f/related-systems/nimbalyst--nimbalyst-wiki`. Doctrine/design: README, FORMAT, CONTRIBUTING, SOURCE and all seven skill entry points read; setup/update reference headings searched, bodies not yet inspected. Implementation: root plugin/marketplace and MCP manifests, hooks, team plugin and MCP manifests read. Reported operation: README feature and host-behavior claims, not independently observed. Tracked tree inventoried. | Doctrine/design: [capture](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/skills/capture/SKILL.md), [recall](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/skills/recall/SKILL.md), [update](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/skills/update/SKILL.md), [format](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/FORMAT.md). Integration declarations: [local/session MCP](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/.mcp.json), [hooks](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/hooks/hooks.json), [team MCP](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/nimbalyst-wiki-team/.mcp.json). Reported operation: [README](https://github.com/nimbalyst/nimbalyst-wiki/blob/97c1ba1594d6e3d466a23d33c1bda084026b01b8/README.md). | External CLI/library/browser, host and hosted-server implementations are not in the frozen source, preventing verified end-to-end runtime, persistence and access-control conclusions. No observed run or causal experiment. Available but uninspected reference bodies are not an access gap. Images/license deliberately excluded as above. |
