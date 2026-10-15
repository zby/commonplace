---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MemWiki runtime baseline: scaffold and update CLI, host-agent protocol, maintenance requests and their enforcement limits."
run-id: AAS-2026-10-14-memwiki-79dcc4d04bcb-01
reviewed-boundary: "8034a3da991ac2639b87875172a9572903ecf1d5"
---

# MemWiki runtime report

## Runtime account

MemWiki installs a file-based memory protocol; it does not run the coding model. Its executable work is a synchronous scaffold/update pass. Its consequential continuing work—reading project context, recording discoveries and maintaining the wiki—is assigned in natural language to an external coding agent. This account uses SRC-1 implementation and doctrine/design evidence at the frozen boundary. The supplied boundary registers no observed model run or causal experiment. No target code or tests were executed. Actual activation, compliant maintenance and performance benefit remain unobserved. SRC-1, `src/index.ts`, `AGENTS.md`, `package.json`.

### Ordinary setup and later session

A project operator invokes `npx memwiki init` in the project root. The declared package executable is `dist/index.js`; `prepack` runs the TypeScript build, whose configuration maps `src` to `dist`. The frozen source lacks built `dist` bytes, so this traces the declared build route and inspected TypeScript, not the npm registry artifact. Node reads only `process.argv[2]`, accepts `init` or `update`, and rejects other values with exit 1. The invoking process supplies filesystem authority and `process.cwd()` supplies project identity; there is no MemWiki user identity or project registry. SRC-1, `package.json`, `tsconfig.json`, `src/index.ts`; [RT-RTE-cli-init](#rt-rte-cli-init).

> const targetDir = process.cwd();
> --- `src/index.ts`

The script ensures `.github`, `.memory/.raw` and `.memory/wiki`, then iterates eleven hardcoded templates: three host hooks, `AGENTS.md`, and seven wiki pages. During `init`, an existing destination is skipped, not merged or checked for validity. Missing files are written as UTF-8. Console messages identify created/skipped files and the terminal result; there is no agent invocation or structured return object. Synchronous operations order this one process, but no transaction, lock or rollback coordinates competing processes. An I/O exception can interrupt a partially completed pass; rerunning `init` fills missing destinations without repairing existing partial content. SRC-1, `src/index.ts`.

> } else if (!fs.existsSync(filePath)) {
>     fs.writeFileSync(filePath, content, 'utf8');
> --- `src/index.ts`

After setup, the external host must discover the relevant hook and grant file tools to its model. The shipped Claude hook calls the protocol and hot cache a primary source of truth. The protocol then requests hot-cache reading first; index/domain-page reading is conditional on insufficient context. Raw documents may be read and synthesized. During work the agent decides whether a discovery meets the pattern, complex-bug or architectural-decision trigger. Before ending a session, major task or loss of context, it is instructed to refresh hot context and append a timestamped work summary. These are host-model decisions and file-tool effects, not a background MemWiki daemon or deterministic CLI callback. The foreground agent retains next-step ownership; no MemWiki delegation or return handoff is specified. SRC-1, `CLAUDE.md`, `AGENTS.md`; [RT-RTE-agent-session](#rt-rte-agent-session), [RT-CMP-host-agent](#rt-cmp-host-agent), [RT-BAP-host-protocol](#rt-bap-host-protocol).

> Please read `AGENTS.md` and `.memory/wiki/hot.md` as your primary source of truth for this project before answering any queries or making changes.
> --- `CLAUDE.md`

Context control here is requested selective file reading: always hot, then index/domain material as needed. It is not an implemented context-window eviction rule, isolated worker frame, token budget or compaction interceptor. The roughly 500-word hot-cache description in the README is guidance, not a limit in the executable. `/memwiki-fold` summarizes an external retained log; it does not remove already loaded turns from a host model window. External host compaction and instruction precedence remain uninspected. SRC-1, `AGENTS.md`, `README.md`, `src/index.ts`.

### Selected forcing cases and guarantees

Three source-inspected forcing cases qualify the nominal setup loop. First, pre-existing hooks survive `init` even if they do not route to MemWiki, whereas `update` replaces those same files without merging local instructions. Second, an existing wiki page survives `update`, but a missing wiki page is recreated from its starter template; thus “untouched” does not mean the wiki directory receives no writes. Third, direct execution of tracked `src/index.js` admits only `init` and installs an older protocol without the scaling and slash-command sections. It is an executable alternate source path, not the package's declared bin. These cases were inspected, not experimentally exercised. SRC-1, `src/index.ts`, `src/index.js`, `README.md`; [RT-RTE-protocol-update](#rt-rte-protocol-update), [RT-RTE-legacy-init](#rt-rte-legacy-init).

> if (command === 'update' && isProtocolFile) {
>     fs.writeFileSync(filePath, content, 'utf8');
> --- `src/index.ts`

**Existing-wiki preservation:** owner: CLI author; enforcement point: the per-destination branch in `src/index.ts`; guarantee strength: invariant for an ordinary single-process pass over existing regular files. Covered paths: both TypeScript commands skip existing non-protocol destinations. Alternate paths: external host tools, manual editing and other processes are not covered. Required external contract: ordinary filesystem semantics and no concurrent replacement of checked paths. This is not a security boundary, atomic update, symlink protection or protection against a host agent overwriting a page. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/index.ts`; [RT-CLM-safe-update](#rt-clm-safe-update).

**Raw-source immutability, knowledge preservation and session persistence:** owner: cooperating host agent; enforcement point: interpretation of `AGENTS.md`; guarantee strength: protocol. Covered intended route: protocol-following host work. Alternate paths: direct editing, host shell/tool access and any provider-native or extension tool behavior outside that interpretation are not constrained by MemWiki. Required external contract: host discovery, sufficient context, tool grants and compliance. The executable merely creates `.raw`; it sets no read-only permissions and installs no validator. “Never delete knowledge” also coexists with explicit log condensation, which allows textual replacement while requesting semantic preservation. Implementation conclusion status: claimed. Operation conclusion status: uninspected. SRC-1, `AGENTS.md`, `src/index.ts`; [RT-RTE-agent-commands](#rt-rte-agent-commands).

> - Never delete knowledge from the wiki. Only append or refine.
> --- `AGENTS.md`

The capability surface is local file scaffolding plus requested agent read/edit/synthesis. Current host grants and deployed isolation are unknown: no included host implementation establishes approval behavior, sandbox roots, shell availability, subprocess controls or provider choices. MemWiki does not mediate direct model calls, remote workers or host callbacks. Its inspected CLI imports filesystem/path APIs and contains no model request; the provider internals and any host bypass surface remain outside this boundary. Consequently protocol compliance cannot be promoted to a deployment guarantee. SRC-1, `src/index.ts`, `AGENTS.md`, `package.json`.

### Changes and evidence limits

There are two distinct change-admission mechanisms. `update` mechanically installs fixed protocol/hook replacements on operator invocation. The host protocol asks a model to synthesize discoveries or raw documents into retained pages, propose health fixes and condense history. The first changes future instruction delivery; the second changes knowledge and later context. Neither supplies a per-content human approval gate, versioned rollback or answer oracle. A user's launch of ingestion is not approval of each resulting sentence. Repository code may itself be changed by the coding host, but MemWiki supplies no distinct product/capability/production-machinery admission pipeline beyond these instructions. SRC-1, `src/index.ts`, `AGENTS.md`.

The retained log reports ingestion and page population, not an inspectable model execution. It also repeats “zero runtime dependencies,” while package metadata declares a `memwiki` dependency. The CLI source uses only Node built-ins, but package installation cannot be characterized as dependency-free. These discrepancies bound reliability claims; they do not establish the absence of useful memory behavior. SRC-1, `.memory/wiki/log.md`, `package.json`, `src/index.ts`.

> "dependencies": {
>     "memwiki": "^1.0.0"
>   }
> --- `package.json`

All inspected files are within SRC-1's registered scope; no source or evidence layer was added. Memory content revision and epistemic assessment belong to the later specialists. Here the agent protocol establishes open-ended maintenance requests, not an observed theory-criticism iteration or demonstrated learning.

## Shared records

### Components

#### RT-CMP-host-agent
Label: External coding agent

Source-native identity: Cursor, Claude Code, GitHub Copilot or another local-file-reading coding host, as named by the README. Its interpreting model is a distributed-parametric component outside the checkout; tool control and protocol delivery are host machinery, not MemWiki code. Storage substrate: host/provider-managed parameters and context, opaque here. Parameter changes during operation: uninspected. Exact model version pinned: no; no model identifier is configured by MemWiki. Mutable endpoint resolving to another model: uninspected because no endpoint is supplied. These are unresolved host facts, not assertions that weights change or never change. SRC-1, `README.md`, `AGENTS.md`.

> AI coding agents (like Cursor, Claude Code, GitHub Copilot) suffer from "Agent Amnesia". When you start a new session, the agent forgets why certain architectural decisions were made, the project's tech stack quirks, known bugs, and the immediate context.
> --- `README.md`

### Operative objects

#### RT-OBJ-protocol-files
Label: Protocol and root hooks

Source-native identity: `AGENTS.md`, `.cursorrules`, `CLAUDE.md`, `.github/copilot-instructions.md`. Representational form: natural-language obligations consumed by a host/model. Storage substrate: UTF-8 project files, seeded from string templates in `src/index.ts`. Template dispatch paths and update membership are symbolic program data; the installed instructions are interpreted prose, not an executable permission policy. The four files share CLI admission but have distinct host entry consumers; the protocol supplies the detailed workflow after hook routing. SRC-1, `src/index.ts`, `AGENTS.md`, `CLAUDE.md`.

> const isProtocolFile = relativePath === 'AGENTS.md' || relativePath === '.cursorrules' || relativePath === '.github/copilot-instructions.md' || relativePath === 'CLAUDE.md';
> --- `src/index.ts`

### Routes

#### RT-RTE-cli-init
Label: CLI initialization

Endpoints/progression: operator process → Node command dispatch → directory creation → template iteration → console result. Owner: deterministic CLI; context is argv and cwd; state is destination existence and write counter; executor/effect boundary is the invoking process's filesystem permissions. SRC-1, `src/index.ts`, `package.json`, `tsconfig.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Console created/skipped messages and terminal completion message; invalid command exits 1.
- Later read-back: Newly installed wiki can subsequently be changed and consumed through the host session route; static starter files alone are not accumulated memory.
- Delegated visibility: inapplicable — CLI invokes no delegated model or worker.
- Selection predicate: `process.argv[2]` equals `init`; each absent destination among fixed templates is written.
- Invalidation or expiry: No expiry; an existing file is skipped regardless of its age or contents.
- Activation or effect: Source wires file creation, not discovery or use by a host agent.
- Evidence limits: No build, npm artifact or CLI execution supplied; partial writes and concurrency are not tested.

Admission: operator chooses launch and cwd; code chooses fixed installed content. There is no model proposer, per-file approval or answer oracle. Mode: fixed installation, not experiment. Existing files reject replacement by the existence branch. A failed pass has no transactional rollback; rerun can create missing files. Guidance: hardcoded protocol/templates; installed files persist in the project.

> if (command !== 'init' && command !== 'update') {
>   console.log('Usage: npx memwiki init | npx memwiki update');
>   process.exit(1);
> }
> --- `src/index.ts`

#### RT-RTE-protocol-update
Label: Protocol replacement

Endpoints/progression: operator's `update` → same directory/template loop → unconditional four-file protocol replacement, missing-file creation elsewhere → console result. Owner/executor: CLI process. Context/state: cwd, fixed protocol-file predicate and destination existence. Effect: replaces future host instructions without reading or merging old content. SRC-1, `src/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated/created/skipped messages and count-dependent terminal message.
- Later read-back: Replaced instructions can govern later host sessions; existing wiki knowledge remains available under the single-process conditions stated above.
- Delegated visibility: inapplicable — no delegation is called.
- Selection predicate: Command is `update`; four exact protocol paths are overwritten, other template paths only when absent.
- Invalidation or expiry: Old protocol contents are replaced immediately; no version comparison or expiry metadata.
- Activation or effect: File replacement is wired; downstream discovery and changed model behavior remain unobserved.
- Evidence limits: Source does not establish npm byte identity, host compliance or concurrency safety.

Admission: operator initiates, template author supplies content, code admits it without human diff review. No per-content veto/approval or answer oracle is installed. Operating mode: fixed replacement on explicit request. Trigger: operator seeks newer protocol. Guidance and persisted result: templates containing the full new hook/protocol text. Rejection requires not launching or external intervention; local customizations are not merged. No backup or rollback is implemented. Recovery requires an external copy/version-control mechanism, if the project has one.

> if (command === 'update' && isProtocolFile) {
>     fs.writeFileSync(filePath, content, 'utf8');
>     console.log(`🔄 Updated: ${relativePath}`);
>     updatedCount++;
> --- `src/index.ts`

#### RT-RTE-agent-session
Label: Host session memory loop

Endpoints/progression: host discovers hook → external coding agent reads protocol/hot → conditionally reads index/domain/raw material → performs user work and synthesizes findings → refreshes hot and logs work → later session reads retained context. Owner: foreground agent under host and user authority. Identities: project-relative file names; no MemWiki session ID, actor credential or coordination token. Context: project task, selected files and host working window. Executor: external file tools; permissions and approvals are host-controlled. SRC-1, `AGENTS.md`, `CLAUDE.md`, `src/index.ts`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Host task answer and requested file changes; MemWiki specifies no answer schema.
- Later read-back: Updated hot context, index-linked domain content and work history are intended to reach subsequent sessions.
- Delegated visibility: uninspected — host delegation and its context sharing are not specified by the protocol.
- Selection predicate: Always hot; index/domain files when hot is insufficient; synthesis after new patterns, complex bug fixes or significant decisions.
- Invalidation or expiry: Refinement and hot replacement are requested; no automatic stale-content detection, TTL or enforced deletion policy.
- Activation or effect: Protocol requests model decisions and edits; no supplied run demonstrates compliance or behavior caused by retained content.
- Evidence limits: File-edit ability, host discovery, tool grants and actual session-end execution are external assumptions.

Admission: model proposes and writes synthesized knowledge in ordinary open-ended coding work; raw documents may be supplied by a human. Protocol does not require human approval of each wiki edit or define an independent answer oracle. Human veto depends on the host and remains uninspected. Guidance: record relevant findings, scale pages and maintain the index, preserve knowledge, refresh hot/log at task end or before context loss. Result persists as project files. No lock, merge policy, commit checkpoint or content rollback is specified. Interrupted sessions may miss the requested end-of-session writes. This route supplies entry conditions for memory analysis, not a finding that retained knowledge is correct or that capacity improved.

> Before ending a session, completing a major task, or when you are about to lose context:
> 1. **Update Hot Cache:** You MUST update `.memory/wiki/hot.md` with the current state of the project and the immediate next steps for the next agent.
> 2. **Log Work:** You MUST append a timestamped summary of your work to `.memory/wiki/log.md`.
> --- `AGENTS.md`

#### RT-RTE-agent-commands
Label: Chat maintenance workflows

Endpoints/progression: user chat token → host agent interprets matching protocol instruction → repository scan/population, health proposals, or log condensation → host response and any resulting file effects. Owner: host agent, not CLI command dispatch. The three commands share natural-language admission but differ in requested output: ingest writes findings; lint proposes fixes; fold replaces older log detail with summary. SRC-1, `AGENTS.md`, `README.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Agent-maintained wiki content for ingestion, proposed health fixes for lint, and condensed history for fold; no fixed machine output contract.
- Later read-back: Persisted ingest/fold results can enter subsequent project context; lint proposals alone are not retained revisions unless acted on.
- Delegated visibility: uninspected — no separate worker or sharing protocol is specified.
- Selection predicate: `/memwiki-ingest` requests entire-repository scanning; `/memwiki-lint` targets outdated information, missing hot context and empty pages; `/memwiki-fold` targets older log entries.
- Invalidation or expiry: Lint requests detection, not a deterministic expiry rule; fold requests crucial-history preservation while condensing old entries.
- Activation or effect: A model is instructed to perform maintenance; source does not demonstrate execution, accurate coverage or preserved meaning.
- Evidence limits: Retained ingestion log is reported operation only; no transcript or before/after evaluation establishes the transformations.

Admission/diagnosis: user triggers the workflow; model selects findings, identifies health issues and chooses summaries. No independent expected-answer/reference oracle, scoring rule or required approval gate is specified. Human rejection power is host-dependent. Mode: open maintenance requests, not bounded experiments or curriculum. Guidance: repository findings for ingest, the stated health criteria for lint, crucial history for fold. Proposed changes persist only if written; lint's protocol says propose fixes whereas README describes fixing. No content-level rollback or mandated preservation audit is supplied. No guaranteed full-repository scan follows merely from the instruction.

> - `/memwiki-ingest`: Trigger an active ingestion pass. Scan the entire repository and populate `stack.md`, `patterns.md`, and `decisions.md` based on your findings.
> - `/memwiki-lint`: Perform a health check on the wiki. Look for outdated information, missing context in `hot.md`, or empty domain pages, and propose fixes.
> - `/memwiki-fold`: Condense older entries in `log.md` into a summarized paragraph to keep the file from becoming too long, while preserving crucial history.
> --- `AGENTS.md`

#### RT-RTE-legacy-init
Label: Tracked generated initialization

Endpoints/progression: direct Node execution of tracked `src/index.js` → init-only validation → same absent-file scaffold pattern → console result. Owner/executor: Node process with cwd permissions. This is distinct from the package bin and lacks the newer protocol's scaling and slash-command text. SRC-1, `src/index.js`, `package.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Init console messages; any command other than `init` exits 1.
- Later read-back: Installed older protocol/wiki files may reach later host sessions; existing newer files are skipped rather than downgraded by this route.
- Delegated visibility: inapplicable — no model or worker invocation.
- Selection predicate: Only `init`; absent template destinations are written.
- Invalidation or expiry: No update route or version check in this file.
- Activation or effect: Older file-writing behavior is implemented; use through npm is not established.
- Evidence limits: Tracked generated source is not evidence of registry artifact content or actual execution.

Admission: caller initiates deterministic template installation; no human per-file approval or model judgment, answer oracle or experiment. Existing files reject replacement. Guidance/persistence: the older hardcoded templates become files. No rollback or transaction; recovery has the same missing-file rerun limitation as current init.

> if (command !== 'init') {
>     console.log('Usage: npx memwiki init');
>     process.exit(1);
> }
> --- `src/index.js`

### Claims

#### RT-CLM-safe-update
Label: Safe protocol updates

Claimed operation: update evolves prompt/hook files without overwriting actual memory wiki. Source-native intent is supported for existing non-protocol files by the TypeScript branch, not for all possible filesystem effects or all writers. Missing starter wiki files are still created; host-agent edits and concurrent changes lie outside the branch's coverage. SRC-1, `README.md`, `src/index.ts`; [RT-RTE-protocol-update](#rt-rte-protocol-update).

> This safely updates `AGENTS.md` and your root hooks (`.cursorrules`, `CLAUDE.md`, etc.) while leaving the contents of `.memory/wiki/` completely untouched.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-protocol
Label: Host protocol delivery

Consumer: external coding agent. Channel: host-discovered hook files requesting reads of `AGENTS.md` and `.memory/wiki/hot.md`, then task-dependent domain reading. Force: requested instruction/primary-source priority, subject to external host precedence and compliance; not a MemWiki permission check. Horizon: subsequent tasks/sessions in the project, as long as files remain discoverable. Protocol updates change installed guidance; wiki updates change context supplied by that guidance. Delivery and behavioral dependence are not demonstrated by source presence. SRC-1, `CLAUDE.md`, `AGENTS.md`, `src/index.ts`; [RT-OBJ-protocol-files](#rt-obj-protocol-files), [RT-RTE-agent-session](#rt-rte-agent-session).

> 1. READ `.memory/wiki/hot.md` immediately. This contains the immediate context, current state, and next steps.
> 2. If `hot.md` does not have enough context, consult `.memory/wiki/index.md` to find relevant domain pages.
> --- `AGENTS.md`

## Annotations

none
