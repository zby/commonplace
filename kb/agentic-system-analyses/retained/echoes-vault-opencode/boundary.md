---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "EchoesVault for OpenCode, including its bundled portable memory runtime and shipped agent adapters, at commit 875c45aa45559529b87a7481b0c21e6dfd8c5eb0."
run-id: AAS-2026-10-15-echoes-vault-opencode-239c6738bb9e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "875c45aa45559529b87a7481b0c21e6dfd8c5eb0"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/psinetron/echoes-vault-opencode
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-echoes-vault-opencode/related-systems/psinetron--echoes-vault-opencode
  revision: 875c45aa45559529b87a7481b0c21e6dfd8c5eb0
  sha256: null
---

# EchoesVault for OpenCode boundary

## Boundary and evidence

This run examines repository-local project memory: how agents restore retained context, submit intermediate and final knowledge, and maintain a shared Markdown vault. The target is a **memory/knowledge/context-engineering system**, not an enclosing agent runtime. Its model-facing role is supported both by its intended use and by shipped command prompts, tool registrations and generated agent instructions (SRC-1, `README.md`, `index.ts`, `prompts/commands/echoes-start.md`, `scripts/echoes_vault.py`).

> An OpenCode adapter for repository-local, agent-neutral project memory.
> --- `README.md`

The **whole-system** boundary includes the packaged OpenCode server and TUI, Node-to-Python bridge, bundled portable Python launcher/runtime, protocol, command prompts, generated cross-agent guides and skills, migrations, local state, index generation, write admission, search and restoration. It also includes the shipped tests as source evidence of intended checks. The boundary is not restricted to the bridge API: its callers and the shared writer are part of the target (SRC-1, `package.json`, `index.ts`, `runtime.ts`, `tui.tsx`, `scripts/echoes_vault.py`, `tests/runtime.test.ts`).

The inspected production chain is `package.json` exports → `index.ts` tool/command hooks → `runtime.ts` process invocation → `scripts/echoes_vault.py` launcher delegation and command dispatch. The Python implementation installs the project-local runtime and generated agent adapters; append/upsert/end persist content; validation and index rebuilding admit and organize pages; start reloads the index and recent entries; search returns page matches. Generated instructions direct agents to read relevant complete pages and follow deprecation links. Separately, `tui.tsx` consumes marker/local-state files for display. These are source traces, not observed executions (SRC-1, those paths and `prompts/commands/echoes-start.md`).

> Loads the generated index and the three newest daily entries. It does not load the entire vault.
> --- `README.md`

> Read only the relevant returned pages and follow replacement links from deprecated pages.
> --- `scripts/echoes_vault.py`

The frozen evidence is repository `https://github.com/psinetron/echoes-vault-opencode` at full commit `875c45aa45559529b87a7481b0c21e6dfd8c5eb0`, applicable through **2026-10-15**. HEAD matched the supplied pin and the checkout had no reported changes. The overall tier is **code-grounded**. Documentation supplies intent and contracts, not proof that all requirements hold. Tests were read but not run; this boundary establishes neither operational reliability nor measured memory quality.

External dependencies are OpenCode's command/tool/session interfaces, its model-driven agent, Python and Node execution, the local filesystem, and optional Git workspace/readiness operations. Package dependencies also provide the TUI framework (SRC-1, `package.json`, `runtime.ts`, `scripts/echoes_vault.py`, `tui.tsx`). The external hosts decide actual model behavior and ordinary page-reading actions; they are not implemented here. Excluding host internals prevents conclusions about model selection, reasoning, instruction compliance or how returned text is ultimately placed in a provider request. Other agents' runtimes and independent EchoesVault implementations are outside the frozen repository: generated integration instructions are included, but cross-host interoperability in operation is not established. No execution traces, production vaults or causal experiments were supplied; therefore retrieval usefulness, factual correctness of saved knowledge and deployment outcomes remain unmeasured.

### Tracked top-level coverage

All tracked top-level entries are accounted for below. Included executable paths were inspected; documentation inspection is scoped explicitly. Exclusions are deliberate, not access failures.

| Top-level entry | Treatment and material paths | Role and limit |
|---|---|---|
| `.github/` | Included: `.github/workflows/ci.yml`; excluded: `.github/FUNDING.yml` | CI declares typecheck/tests/package checks, not their outcomes. Funding metadata has no memory-loop responsibility; sponsorship operation is not assessed. |
| `.gitignore` | Included; inspected | Checkout exclusions, including local vault and adapter directories; does not establish ignore rules in consuming projects. |
| `.npmignore` | Included; inspected | Package exclusions, including images and local vault data. |
| `EchoesProtocol.md` | Included; initially inspected introduction, conformance model and recommended agent lifecycle | Normative format and behavior contract. Other sections remain available at the pin but were not initially inspected; no full conformance audit is claimed. |
| `LICENSE` | Excluded; inspected for role | MIT licensing text; legal interpretation is not assessed. |
| `README.md` | Included; inspected | Installation, storage layout, lifecycle, tools and development claims. These are doctrine/design, not run evidence. |
| `images/` | Excluded: `images/EchoesVault.png` | Branding image referenced by README; image contents were not inspected. No visual-design conclusion follows. No memory-loop path is excluded. |
| `index.ts` | Included; inspected | Server entry, bundled prompt registration, lifecycle authorization map and all nine tools. |
| `package-lock.json` | Included as dependency-resolution metadata; contents not initially inspected | Available frozen lockfile, not an access gap. No transitive dependency/security audit is claimed. |
| `package.json` | Included; inspected | Package exports, shipped files, dependencies and test entry points. |
| `prompts/` | Included: all four `prompts/commands/echoes-{init,start,end,status}.md` files; inspected | Model-facing initialization, restoration, distillation and status procedures. |
| `runtime.ts` | Included; inspected | Workspace choice, Python invocation, payload transport and process result handling. |
| `scripts/` | Included: complete `scripts/echoes_vault.py`; inspected | Portable writer and launcher; generated protocol/root guides, skills, OpenCode commands and legacy redirects; initialization/migration/upgrades; lock, atomic replacement, metadata/hash admission, deterministic index, health/Git reporting, daily/page persistence, search and session reload. No shipped maintenance or consumption driver is treated as external. |
| `tests/` | Included: `tests/runtime.test.ts`; inspected, not executed | Runtime-byte integrity, non-mutating plugin load, workspace safety, lifecycle authorization, initialization, migration and hash-protected replacement checks. Not a model-quality evaluator or proof of passing tests. |
| `tsconfig.json` | Included; inspected | Type-check scope includes server, bridge, TUI and tests. |
| `tui.tsx` | Included; inspected | Polls retained marker/local-state metadata and presents session/health information. Not a second writer or model runtime. |

This inventory and the traced production/maintenance/consumption paths support whole-system coverage of the shipped artifact. Remaining uninspected documentation and dependency metadata are available evidence, not missing material loop components. All coverage statements above refer to SRC-1 at the frozen revision.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/psinetron/echoes-vault-opencode` | 875c45aa45559529b87a7481b0c21e6dfd8c5eb0 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-echoes-vault-opencode/related-systems/psinetron--echoes-vault-opencode`. Implementation: complete `index.ts`, `runtime.ts`, `tui.tsx`, `scripts/echoes_vault.py`, `tests/runtime.test.ts`; package/config/CI and tracked-tree inspection. Doctrine/design: complete README and four bundled command prompts; protocol introduction/conformance and recommended lifecycle; generated agent instructions embedded in Python. | Implementation: [server](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/index.ts), [bridge](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/runtime.ts), [writer and generated adapters](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/scripts/echoes_vault.py), [TUI](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/tui.tsx), [test definitions](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/tests/runtime.test.ts). Doctrine/design: [README](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/README.md), [protocol](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/EchoesProtocol.md), [restore prompt](https://github.com/psinetron/echoes-vault-opencode/blob/875c45aa45559529b87a7481b0c21e6dfd8c5eb0/prompts/commands/echoes-start.md). | No repository access gap encountered. External host internals and production/run artifacts are not supplied: cannot establish actual model consumption, compliance, interoperability, passing tests or memory effectiveness. No observed-run or causal-experiment layer. |
