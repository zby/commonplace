---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MemWiki's CLI, generated agent protocol, host hooks and project wiki at commit 8034a3da991ac2639b87875172a9572903ecf1d5."
run-id: AAS-2026-10-14-memwiki-79dcc4d04bcb-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "8034a3da991ac2639b87875172a9572903ecf1d5"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/hereisSwapnil/memwiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/memwiki-79dcc4d04bcb/related-systems/hereisSwapnil--memwiki
  revision: "8034a3da991ac2639b87875172a9572903ecf1d5"
  sha256: null
---

# MemWiki boundary

## Boundary and evidence

This analysis covers MemWiki as a project-memory system: its scaffold CLI, the agent protocol it installs, the host-facing instruction files, and the repository's retained wiki. Its intended use is carrying project context between AI coding sessions. The target is a **memory/knowledge/context-engineering system**, not an enclosing model runtime. The boundary is **whole-system** for the material shipped paths at the frozen commit. The evidence is **code-grounded** for scaffolding and file-update behavior, and doctrine/design-grounded for model-mediated memory maintenance and consumption. SRC-1, `src/index.ts`, `AGENTS.md`, `README.md`.

The shipped loop extends beyond the CLI. The CLI writes hook files, the master protocol and starter wiki pages in the invoking project's working directory. The protocol assigns later reading, synthesis, wiki expansion, session-end persistence and maintenance commands to an external coding agent. The root hooks route that agent to the protocol and hot cache. These prompts and retained pages are part of the target, not excluded callers. SRC-1, `src/index.ts`, `.cursorrules`, `CLAUDE.md`, `.github/copilot-instructions.md`, `AGENTS.md`.

> 1. READ `.memory/wiki/hot.md` immediately. This contains the immediate context, current state, and next steps.
> 2. If `hot.md` does not have enough context, consult `.memory/wiki/index.md` to find relevant domain pages.
> --- `AGENTS.md`

> 1. **Update Hot Cache:** You MUST update `.memory/wiki/hot.md` with the current state of the project and the immediate next steps for the next agent.
> 2. **Log Work:** You MUST append a timestamped summary of your work to `.memory/wiki/log.md`.
> --- `AGENTS.md`

These instructions make the system's memory loop model-dependent even though its own executable is a deterministic file writer. The included maintenance surface consists of `/memwiki-ingest`, `/memwiki-lint` and `/memwiki-fold` instructions, not executable CLI subcommands. The included admission surface is agent synthesis of raw documents and work findings into wiki pages, with index updates for new pages. SRC-1, `AGENTS.md`, `src/index.ts`.

The package entry point is declared as `dist/index.js`; `build` and `prepack` select TypeScript compilation, with `src` as the root and `dist` as output. The tracked TypeScript supports `init` and `update`, while the tracked generated `src/index.js` supports only `init` and contains an older protocol. Both are included rather than treating the latter as the current package entry point. No built `dist` file is tracked in the frozen tree. Thus this boundary supports conclusions about the source and declared build route, not verification of the bytes installed by `npx` from the npm registry. SRC-1, `package.json`, `tsconfig.json`, `src/index.ts`, `src/index.js`, `.gitignore`.

> "bin": {
>     "memwiki": "dist/index.js"
>   },
> --- `package.json`

> if (command !== 'init' && command !== 'update') {
>   console.log('Usage: npx memwiki init | npx memwiki update');
>   process.exit(1);
> }
> --- `src/index.ts`

External dependencies are Node.js and its filesystem APIs for scaffolding; TypeScript and Node type declarations for the declared build; and a host coding agent with local-file reading, editing and instruction-discovery behavior for ongoing memory use. `package.json` and `package-lock.json` also declare a runtime dependency on the npm package `memwiki`, despite the zero-dependency language in the documentation. The locked dependency's implementation is outside this Git source; its behavior and registry artifact equivalence cannot be established here. Model selection, host prompt precedence, filesystem permissions and actual compliance belong to those external hosts, not to MemWiki. SRC-1, `package.json`, `package-lock.json`, `README.md`, `src/index.ts`.

The frozen revision is `8034a3da991ac2639b87875172a9572903ecf1d5`; the applicability cutoff is 2026-10-14. HEAD matched that revision, and the source checkout was inspected read-only. No target execution, test execution or model invocation was performed. The repository's ingestion log is attributed reported operation, not an observed execution trace or a causal experiment. Its retained pages are included as concrete memory artifacts but do not prove cross-session improvement. SRC-1, `.memory/wiki/log.md`, `.memory/wiki/hot.md`.

### Tracked top-level coverage

Every top-level tracked file or directory is accounted for below. Included rows were inspected at the frozen revision unless a narrower exception is stated. All source paths refer to SRC-1.

| Top-level path | Status | Material paths and role | Limit or conclusion prevented |
| --- | --- | --- | --- |
| `.cursorrules` | Included; inspected | Cursor hook directing initial reads to `AGENTS.md` and `.memory/wiki/hot.md` | Establishes the instruction, not Cursor's actual discovery or compliance. |
| `.github/` | Included; inspected | `.github/copilot-instructions.md`: Copilot-facing read hook; the tree contains no shipped CI or evaluator here | Host behavior is not demonstrated by the hook text. |
| `.gitignore` | Included; inspected | Ignores `node_modules/`, `dist/`, environment and local incidental files | Does not establish a published build's contents. |
| `.memory/` | Included; inspected | `.memory/wiki/hot.md` and `index.md`: initial context and routing; `log.md`: reported ingestion and work history; `stack.md`, `patterns.md`, `bugs.md`, `decisions.md`: retained domain knowledge and design records | No tracked raw inputs, model transcript or evaluator accompany these pages; cannot verify their production history or resulting agent performance. |
| `.npmignore` | Included; inspected | Packaging exclusions for wiki, host hooks, protocol, source and compiler configuration | Declared exclusions do not verify registry tarball contents. |
| `AGENTS.md` | Included; inspected | Session-start consumption, work-time synthesis, raw-source rules, page/index maintenance, session-end persistence and ingestion/lint/fold workflows | Protocol obligations are not runtime enforcement or evaluation results. |
| `CLAUDE.md` | Included; inspected | Claude-facing hook routing to protocol and hot cache | Does not demonstrate Claude host behavior. |
| `README.md` | Included; inspected | Intended use, setup/update route, raw-source ingestion and maintenance explanation | Compatibility and benefit assertions remain declared claims. |
| `package-lock.json` | Included; inspected | Locked package metadata, `memwiki` dependency and build dependency resolutions | Dependency package bytes are not included; no implementation claims about those packages. |
| `package.json` | Included; inspected | Package version, CLI/main entry, published-file selection, build/prepack commands and dependencies | Installed npm artifact and successful build are unverified. |
| `src/` | Included for material executable paths; ancillary maps excluded and not inspected | `src/index.ts`: command dispatch, templates, directory creation, initial writes and protocol updates; `src/index.js`: older tracked generated CLI; `src/index.d.ts`: empty exported API declaration. `src/index.js.map` and `src/index.d.ts.map` are ancillary mapping files | Excluding maps prevents claims about source-map fidelity, not inspection of either executable's file-writing loop. |
| `tsconfig.json` | Included; inspected | Compilation mode and `src` to `dist` output route | Configuration alone does not show build success. |

There is no tracked evaluator or separate runtime driver in the enumerated tree. The supplied host hooks and protocol are the shipped consumers of retained state. External host implementations, external project repositories, linked inspiration, npm artifacts and later revisions are deliberately outside the frozen source set; their exclusion prevents conclusions about host enforcement, deployment-specific results, upstream equivalence and subsequent fixes. The missing tracked `dist` output, raw-source examples and execution traces are unavailable evidence, not material files left uninspected. SRC-1, `package.json`, `README.md`, `AGENTS.md`, `src/index.ts`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/hereisSwapnil/memwiki` | 8034a3da991ac2639b87875172a9572903ecf1d5 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/memwiki-79dcc4d04bcb/related-systems/hereisSwapnil--memwiki`. Implementation: `src/index.ts`, `src/index.js`, `src/index.d.ts`, package/build/ignore metadata. Doctrine/design: `README.md`, `AGENTS.md`, all three root/host hooks and all seven tracked `.memory/wiki/` pages. Reported operation: ingestion account in `.memory/wiki/log.md`, reflected in `hot.md`. Full tracked-tree enumeration supplied coverage accounting. | Implementation: [CLI source](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.ts), [tracked generated CLI](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/src/index.js), [package entry/build](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/package.json). Doctrine/design: [protocol](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/AGENTS.md), [usage](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/README.md). Reported operation: [work log](https://github.com/hereisSwapnil/memwiki/blob/8034a3da991ac2639b87875172a9572903ecf1d5/.memory/wiki/log.md). | No frozen npm tarball or tracked `dist`, dependency implementation, external host code, raw input bundle, observed model run or causal evaluation. Cannot establish installed-byte identity, dependency behavior, host instruction compliance or memory effectiveness. Ancillary source maps deliberately not inspected; no source-map fidelity claim. |
