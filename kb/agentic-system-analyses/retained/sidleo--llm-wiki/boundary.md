---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llm-wiki's knowledge-bundle core and five shipped consumption forms at commit f70e680d852a78d48504425d87252531e68c5624."
run-id: AAS-2026-11-08-llm-wiki-97b740596442-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f70e680d852a78d48504425d87252531e68c5624
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/sidleo/llm-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-76ba8cd8a8db/related-systems/sidleo--llm-wiki
  revision: f70e680d852a78d48504425d87252531e68c5624
  sha256: null
---

# llm-wiki boundary

## Boundary and evidence

This run analyses llm-wiki as an agent-facing knowledge and context system, not as an enclosing agent runtime. Its intended use is to retain reusable domain knowledge in Markdown bundles, retrieve that knowledge during later work, maintain its structure, and deliver directory-specific behavioral instructions to a model's host. The frozen target includes the shared core, its vendored copies, and all five shipped consumption forms: DSH, pi, MCP, Codex, and skill/CLI. It also includes shipped maintenance procedures, migrations, sample bundles, and evaluation code. These are responsibilities of the target even when a host invokes them (SRC-1, `README.md`, `packages/core/index.mjs`, `packages/skill/SKILL.md`).

The repository describes the common retained state and its consumers:

> All five forms read and write **the same bundle** with identical behavior — they reuse `packages/core`, no duplicated implementation.
> --- `README.md`

This is design doctrine, not an established equivalence result. Initial implementation inspection traced the CLI's list/search/get/create/update dispatch to the core, the core's file writes and index/log maintenance, and its later reconstruction of concepts and backlinks from disk (SRC-1, `packages/skill/bin/wiki.mjs`, `packages/core/lib/write.mjs`, `packages/core/lib/bundle.mjs`). For example, creation retains the serialized concept before maintaining derived navigation:

> const text = serializeDoc({ meta, body: p.body || '' })
> await mkdir(dirname(file), { recursive: true })
> await writeFile(file, text)
> --- `packages/core/lib/write.mjs`

The boundary includes admission behavior in the shipped callers, not just the core library API. The core's write module explicitly assigns interactive gating to those callers; inspected CLI and MCP creation paths consult directory gates before invoking `createConcept` (SRC-1, `packages/core/lib/write.mjs`, `packages/skill/bin/wiki.mjs`, `packages/mcp/lib/tools.mjs`). This establishes where to inspect admission, not a claim that every mutation path enforces identical gates.

The later-consumption loop also includes prompt delivery. Initial inspection traced DSH's `apply` handler from bundle resolution and prompt collection into assembly sections and runtime contexts; pi's default extension into tool registration and its per-turn prompt hook; the MCP executable into server assembly and tool dispatch; and Codex's manifest/hooks into context snapshot generation and its bundled MCP executable (SRC-1, `packages/dsh/wiki.mjs`, `packages/pi/extensions/index.ts`, `packages/mcp/bin/wiki-mcp.mjs`, `packages/mcp/lib/server.mjs`, `packages/codex/.codex-plugin/plugin.json`, `packages/codex/hooks/hooks.json`, `packages/codex/hooks/inject-context.mjs`, `packages/codex/bin/wiki-mcp.mjs`). The pi hook exposes a concrete model-context consumption surface:

> const base = typeof event.systemPrompt === "string" ? event.systemPrompt : "";
> return { systemPrompt: `${base}\n\n${text}` };
> --- `packages/pi/extensions/index.ts`

Thus `whole-system` means the repository's complete knowledge-system responsibility, including its host adapters and maintenance paths. It does not mean the enclosing model-execution loop. The target serves model-dependent work through tools, prompts and skills; the external host selects and calls the model and decides whether to follow returned guidance. The skill itself identifies that host boundary (SRC-1, `packages/skill/SKILL.md`). No model compliance, model quality improvement, or autonomous knowledge acquisition is established by these entry points alone.

### Tracked top-level coverage

The tracked tree was enumerated at the frozen commit. Every top-level tracked file or directory is classified below. “Included” is functional scope, not a claim that every file has already been read. Initial inspection is listed separately; available but unread files remain eligible evidence under SRC-1 and are not access gaps.

| Top-level path | Scope and material paths | Initial inspection and role | Limit or conclusion prevented |
|---|---|---|---|
| `.gitignore` | Excluded: repository hygiene | Tree entry identified | No assessment of ignored local artifacts or packaging completeness from ignore rules. |
| `LICENSE` | Excluded: legal terms | Tree entry identified | No licensing analysis. Package-local license copies are likewise not behavioral evidence. |
| `README.md` | Included: system use, layout, forms, maintenance and test guidance | Read in full; doctrine/design | Descriptions and test counts are attributed declarations, not observed results. |
| `README.zh-CN.md` | Included: alternate-language system guidance | Tree identified; text not yet inspected | No translation-parity conclusion from the initial inspection. |
| `schema.md` | Included: bundle, reserved-file and concept contract | Opening format and frontmatter sections inspected | Remaining specification is available, not an access gap; full conformance is not established here. |
| `SPEC-EXTENSIONS.md` | Included: directory gates and prompt-delivery doctrine | Read in full | Host-channel equivalence is declared intent, not proven behavioral equivalence. |
| `packages/` | Included: `core/index.mjs` and `core/lib/` persistence, reload, rules, retrieval, validation/lint, index/log, registry, ingest and sync; `dsh/wiki.mjs`, `dsh/src/client/index.ts`, `dsh/lib/client.js`, deployment/build files and autosync; `pi/extensions/index.ts`; `mcp/bin/` and `mcp/lib/`; `codex/.codex-plugin/`, `.mcp.json`, `hooks/`, `skills/`, `bin/`, `lib/`; `skill/SKILL.md`, CLI, installation/build scripts; adapter `vendor-core/`, synchronization scripts and package tests | Core entry, bundle and write modules read in full; caller, transport and injection paths sampled as described above. DSH client introduction and deployment patch inspected; Codex manifest and hooks read. Other module bodies, generated client assets, adapter tests, package metadata and distribution scripts remain available for subsequent inspection. | No paths are excluded merely because they wrap core. Vendored code must be checked at the actual adapter load path before assuming equivalence with core. Initial inspection does not certify packaging, all tool paths, sync safety or UI behavior. |
| `examples/` | Included: `demo-bundle/` concepts, root/category indexes, log, root and references `AGENTS.md`, attesters, skills and SQL references | Full tree enumerated; root `AGENTS.md` read | Synthetic retained state and rule examples, not evidence of production use or successful computation/attestation. Remaining example bodies are available. |
| `obsidian/` | Included: `dataview-examples.md` and `templates/` for Tables, Pitfalls and Attested Computations | Dataview examples read in full; template paths enumerated | Shipped human-consumption/authoring adjuncts are in scope; external Obsidian behavior is not verified. Templates remain available. |
| `scripts/` | Included: `migrate.mjs`, `migrate-to-feishu.mjs`, `smoke-test.mjs` | Entrypoint imports and initial migration/evaluation setup inspected | Includes alternate state-production paths, not just developer utilities. Remaining bodies are available; no successful migration or smoke run is claimed. |
| `tests/` | Included: sync/autosync, deletion, Feishu, DSH host/client contracts, rules injection, cross-form consistency, references, overview, vendor parity and fixtures | Full tree enumerated; vendor-sync test read in full; three-forms setup and initial cases inspected | Tests supply executable expectations. No tests were executed; assertions are not observed passing results. Other tests and fixtures remain available. |

### Evidence and dependency limits

The immutable revision is `f70e680d852a78d48504425d87252531e68c5624`; checkout HEAD was checked against the acquired pin. The applicability cutoff is 2026-11-08. No later revision, live deployment or installed npm package is included. The overall tier is `code-grounded`: source inspection establishes implementation structure alongside documentation, but this job did not execute the target, tests or examples.

External dependencies are the enclosing DSH/pi/Codex/MCP-capable hosts and their model providers; Node and relevant transport/UI libraries; the Git executable and remote service; Feishu and `lark-cli`; and optional Obsidian/Dataview. Only the target-side contracts and adapters are in scope. Their external implementations, credentials, real user bundles and service state are not frozen here, preventing conclusions about live interoperability, successful synchronization, host prompt precedence or model adherence. The referenced upstream OKF specification and Karpathy pattern are not separate registered sources; the run may describe this repository's stated alignment, not independently establish alignment against unfrozen external documents (SRC-1, `README.md`, `schema.md`, `SPEC-EXTENSIONS.md`).

No observed execution trace or causal experiment was supplied. Test code and synthetic examples therefore cannot establish operational reliability, factual accuracy of retained knowledge, retrieval effectiveness on real workloads, or benefits to downstream model tasks. These are evidence limits, not unavailable repository paths.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sidleo/llm-wiki` | f70e680d852a78d48504425d87252531e68c5624 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-76ba8cd8a8db/related-systems/sidleo--llm-wiki`. Implementation: complete `packages/core/index.mjs`, `packages/core/lib/bundle.mjs`, `packages/core/lib/write.mjs`; bounded entrypoint/caller/prompt sections in `packages/skill/bin/wiki.mjs`, `packages/dsh/wiki.mjs`, `packages/pi/extensions/index.ts`, `packages/mcp/bin/wiki-mcp.mjs`, `packages/mcp/lib/tools.mjs`, `packages/codex/bin/wiki-mcp.mjs`; complete `packages/mcp/lib/server.mjs`, `packages/codex/hooks/inject-context.mjs`, Codex manifest/hooks and `tests/vendor-sync.test.mjs`; initial DSH client, migration, smoke and cross-form test sections. Doctrine/design: complete root English README, extensions declaration, core README, skill and demo root rules, Dataview examples, DSH patch; initial schema sections. | Implementation: [core writes](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/core/lib/write.mjs), [bundle reload](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/core/lib/bundle.mjs), [DSH caller](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/dsh/wiki.mjs), [pi caller](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/pi/extensions/index.ts), [MCP assembly](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/mcp/lib/server.mjs), [Codex context hook](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/codex/hooks/inject-context.mjs), [CLI](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/skill/bin/wiki.mjs). Doctrine/design: [README](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/README.md), [extensions](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/SPEC-EXTENSIONS.md), [skill](https://github.com/sidleo/llm-wiki/blob/f70e680d852a78d48504425d87252531e68c5624/packages/skill/SKILL.md). | No repository access gap encountered. Unread available files are distinguished in the coverage table. External hosts/services/specification are not frozen; no execution or causal evidence is supplied. Consequently this source supports implementation and declared contracts, not observed reliability, semantic correctness, external conformance or downstream model benefit. |
