---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "EchoWiki's shipped knowledge-compilation system, Obsidian integration and CLI at commit 11446997423e88177dba62d6a3d5c1e8b4886c62."
run-id: AAS-2026-10-14-echowiki-8d428f79523e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "11446997423e88177dba62d6a3d5c1e8b4886c62"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/mohammadmaso/echowiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/echowiki-8d428f79523e/related-systems/mohammadmaso--echowiki
  revision: "11446997423e88177dba62d6a3d5c1e8b4886c62"
  sha256: null
---

# EchoWiki boundary

## Boundary and evidence

This run analyses EchoWiki as a model-dependent knowledge-compilation system, not merely its compiler API. Its intended use is turning text notes and voice transcripts into a persistent, linked Markdown wiki for Obsidian. The boundary includes the shipped Obsidian plugin, optional CLI, shared compiler, storage adapters, prompts, editable instruction template, index/log maintenance and later reuse of existing wiki pages. The plugin is a shipped caller with ingestion, admission and persistence responsibilities; it is not an excluded enclosing application (SRC-1: `README.md`, `obsidian-plugin/src/main.ts`, `src/cli/compile.ts`, `src/compiler-api.ts`).

The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system**: all material shipped paths for producing, admitting, maintaining and consuming its retained state were traced. This describes source coverage, not proof that all intended capabilities work. The compiler issues model calls and consumes retained concept/entity descriptions and selected existing page bodies during later compilation. Browsing the resulting index and links is delegated to Obsidian rather than a shipped query/chat agent (SRC-1: `src/wiki/compiler.ts`, `src/wiki/briefs.ts`, `src/wiki/prompts.ts`, `README.md`).

Minimum classification evidence:

> const { text } = await generateText({ model, messages });
> --- `src/llm/client.ts`

> const conceptBriefs = await readConceptBriefs(storage);
> const entityBriefs = await readEntityBriefs(storage);
> --- `src/wiki/compiler.ts`

> Current content of this page:
> {existing_content}
>
> New information from document "{doc_name}" (summarized above) should be integrated into this page. Rewrite the full page incorporating the new information naturally — do not just append. Preserve the existing structure and intent of the page.
> --- `src/wiki/prompts.ts`

The entry-point trace is plugin `src/main.ts` → `src/compiler-client.ts` → shared `src/compiler-api.ts` → `src/wiki/compiler.ts`, with `src/vault-storage.ts` persisting wiki pages through the Obsidian API. The CLI `src/cli/compile.ts` calls the same API with `src/storage/node-storage.ts`. Within the compiler, `briefs.ts` reloads prior page descriptions, update tasks read prior bodies, `page-writer.ts` writes pages and backlinks, and `index-writer.ts` updates the catalog and operations log. Watcher events, the pending approval queue, note copying and voice transcription are included at the plugin layer (SRC-1: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/compiler-client.ts`, `obsidian-plugin/src/vault-storage.ts`, `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/approval-modal.ts`, `obsidian-plugin/src/voice-modal.ts`, `obsidian-plugin/src/stt-client.ts`, `src/cli/compile.ts`, `src/compiler-api.ts`, `src/wiki/compiler.ts`, `src/wiki/briefs.ts`, `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`).

Instruction-driven maintenance is included rather than inferred solely from the API. The supplied `templates/wiki/AGENTS.md` is an optional user-installed runtime instruction file; the compiler loads a stored `AGENTS.md` or its code fallback. These instructions express conventions, not verified enforcement of every requested behavior (SRC-1: `README.md`, `templates/wiki/AGENTS.md`, `src/wiki/schema.ts`, `src/wiki/compiler.ts`).

> export async function getAgentsMd(storage: WikiStorage): Promise<string> {
>   const content = await storage.readText('AGENTS.md');
>   return content ?? DEFAULT_AGENTS_MD;
> }
> --- `src/wiki/schema.ts`

The frozen evidence is the repository at **11446997423e88177dba62d6a3d5c1e8b4886c62**, with applicability cutoff **2026-10-14**. HEAD matched the acquisition pin and the checkout status was clean on inspection. The evidence tier is **code-grounded**. Repository documentation supplies attributed intent; executable source determines which paths are shipped. In particular, the `.ai/` plans describe Mastra while the current client imports the Vercel AI SDK. These plans are not evidence that Mastra executes this revision (SRC-1: `.ai/02-TECH-SPEC.md`, `CLAUDE.md`, `src/llm/client.ts`, `package.json`).

### Tracked-root coverage

Every top-level tracked entry is classified below. “Included” covers its responsibility in this target; it does not mean every byte of packaging metadata was read. Unless indicated otherwise, the listed material source files were read completely. All rows refer to SRC-1.

| Top-level entry | Classification and inspection | Role / material paths | Conclusion prevented by exclusion or incomplete inspection |
|---|---|---|---|
| `.ai/` | Included; all three documents inspected | `01-PRD.md`, `02-TECH-SPEC.md`, `03-TASKS.md`: product intent, architecture plans, maintenance and manual-test tasks | Plans and unchecked tasks do not establish completed implementation or observed results. |
| `.env.example` | Included configuration surface; not yet inspected | CLI environment example; actual configuration traced in `src/config.ts` and `src/compiler-api.ts`, with variable descriptions in `README.md` | No claim about exact example-file defaults or completeness. No material execution path remains untraced. |
| `.github/` | Included; inspected | `workflows/release.yml`: dependency installation, plugin build and release packaging | No release execution evidence; cannot establish that a published bundle matches this checkout. |
| `.gitignore` | Included; inspected | Excludes personal `raw/`, `wiki/`, Obsidian data and build output from version control | Does not establish that users' local data are absent elsewhere or secure. |
| `.nvmrc` | Included packaging metadata; not yet inspected | Node version selection for release workflow; CLI engine requirement also declared in `package.json` | No exact `.nvmrc` value claimed. |
| `CLAUDE.md` | Included; inspected | Developer instructions, architectural intent and maintenance constraints | Instructions alone do not establish runtime compliance. |
| `LICENSE` | Excluded deliberately; not inspected | Legal terms, not the state-production/consumption loop | No licensing assessment. |
| `README.md` | Included; inspected | Installation, shipped commands, wiki browsing, optional instruction installation, manual test checklist | Checklist is not a recorded test run. |
| `manifest.json` | Included packaging metadata; not yet inspected | Root release manifest used by `.github/workflows/release.yml` | No exact manifest/version compatibility claim. |
| `obsidian-plugin/` | Included; material paths inspected | All `src/` files: `main.ts`, `raw-watcher.ts`, `approval-modal.ts`, `voice-modal.ts`, `stt-client.ts`, `compiler-client.ts`, `vault-storage.ts`, `settings.ts`, `settings-tab.ts`, `utils.ts`. `esbuild.config.mjs` and `package.json` inspected for bundling and the shared compiler alias. `manifest.json`, `styles.css`, `tsconfig.json`, `package-lock.json` not yet inspected | Full shipped integration is included, including persisted/reloaded approval state and connection-test buttons. No CSS, exact manifest, exhaustive dependency or compiler-configuration assessment. |
| `package-lock.json` | Included dependency metadata; not yet inspected | Root dependency lock | No exhaustive transitive dependency, vulnerability or reproducible-install conclusion. |
| `package.json` | Included; inspected | CLI and plugin scripts, AI SDK dependencies, placeholder test script | No automated test result. |
| `src/` | Included; material paths inspected | `compiler-api.ts`, `cli/compile.ts`, `config.ts`, `llm/client.ts`, `storage/node-storage.ts`; `wiki/compiler.ts`, `briefs.ts`, `schema.ts`, `prompts.ts`, `llm.ts`, `page-writer.ts`, `index-writer.ts`, `frontmatter.ts`, `wikilink.ts`, `tools.ts`. `storage/types.ts` and `utils.ts` inspected for the storage contract and document-name extraction | Includes source admission through callers, generation, writes, later reads, metadata/link maintenance and standalone file utilities. No material loop path withheld. |
| `templates/` | Included; inspected | `wiki/AGENTS.md`: user-editable compilation and maintenance instruction seed | Requested conflict handling and OKF conventions are doctrine, not proof of enforcement. |
| `tsconfig.json` | Included build metadata; not yet inspected | Root TypeScript configuration | No type-check success or exact compiler-setting claim. |
| `versions.json` | Included release metadata; not yet inspected | Plugin compatibility/version map | No published version compatibility conclusion. |

### Functional exclusions and evidence limits

- **External host and providers:** Obsidian's editor, graph renderer, vault implementation, device microphone/browser APIs, the installed AI SDK internals and remote LLM/STT services are dependencies, not additional frozen sources. Included adapters show how EchoWiki uses them. Their exclusion prevents conclusions about host durability, graph rendering correctness, provider reliability, model quality and device support from observed operation (SRC-1: `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/vault-storage.ts`, `obsidian-plugin/src/voice-modal.ts`, `obsidian-plugin/src/stt-client.ts`, `src/llm/client.ts`, `obsidian-plugin/esbuild.config.mjs`).
- **Private runtime state:** No user vault, audio sample, generated wiki, persisted settings file or actual pending queue is supplied. `raw/`, `wiki/` and `.obsidian/` are deliberately ignored by the source repository. This is unavailable operational evidence, not an exclusion of the code that creates, reloads or consumes those files. It prevents measuring knowledge accumulation, human edits, queue recovery or real compilation outcomes (SRC-1: `.gitignore`, `obsidian-plugin/src/main.ts`, `src/wiki/compiler.ts`).
- **Evaluators and maintenance breadth:** The source tree, package scripts and searches of `src/` and plugin `src/` expose connection probes and documented manual checks, not an implemented knowledge-quality evaluator or recorded experiment. Root `package.json` declares a placeholder test command. The `.ai/03-TASKS.md` lint task remains a declared task; schema mentions of reports are not a shipped health-report producer. This prevents claims of measured wiki quality, OKF conformance, regression coverage or causal improvement. Connection probes themselves remain included in the boundary (SRC-1: `package.json`, `README.md`, `.ai/03-TASKS.md`, `src/wiki/schema.ts`, `src/llm/client.ts`, `obsidian-plugin/src/stt-client.ts`, `obsidian-plugin/src/settings-tab.ts`).
- **Query and long-document surfaces:** `src/wiki/tools.ts` contains file/page/image helpers, but the inspected CLI and plugin compiler paths do not wire them to a query/chat agent. The tree and caller search establish the shipped compilation loop as the target, not a separately assumed query runtime. Plans name query/chat, Skill Factory, extra formats and long-document indexing as future scope. Their mention does not justify attributing an implemented consumer or evaluator to EchoWiki; no upstream repository was inspected (SRC-1: `src/wiki/tools.ts`, `src/compiler-api.ts`, `src/wiki/compiler.ts`, `src/cli/compile.ts`, `obsidian-plugin/src/main.ts`, `.ai/01-PRD.md`, `.ai/03-TASKS.md`).

> "test": "echo \"Error: no test specified\" && exit 1",
> --- `package.json`

No target code, tests, examples, provider calls or connection probes were executed. Absence of run evidence limits performance, reliability and outcome conclusions; it does not make the source boundary partial.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/mohammadmaso/echowiki` | 11446997423e88177dba62d6a3d5c1e8b4886c62 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/echowiki-8d428f79523e/related-systems/mohammadmaso--echowiki`. Implementation: tracked tree; shipped CLI/API/compiler, model client, storage, prompts, page/index/log maintenance, all plugin `src/` files, build/release paths and package scripts listed in the coverage table. Doctrine/design: `README.md`, `CLAUDE.md`, all `.ai/` documents, `templates/wiki/AGENTS.md` and the fallback schema. | Implementation: [compiler](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [plugin driver](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [CLI](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/cli/compile.ts), [retained-page reads](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [writers](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts). Doctrine/design: [README](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [editable instructions](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/templates/wiki/AGENTS.md), [technical plan](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/02-TECH-SPEC.md). | No source-access gap in material shipped paths. Packaging files not yet fully inspected are distinguished in the table. No private vault or execution trace, external dependency source or causal experiment supplied: cannot establish real outcomes, service behavior, measured quality or causal benefit. Doctrine/design supports intent only, including plans that differ from this implementation. |
