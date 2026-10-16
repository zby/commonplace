---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MemWiki workflow: chat-requested repository ingestion, wiki persistence and next-session consumption, with verification and recovery limits."
run-id: AAS-2026-10-14-memwiki-79dcc4d04bcb-01
reviewed-boundary: "8034a3da991ac2639b87875172a9572903ecf1d5"
---

# MemWiki workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is a user's `/memwiki-ingest` request in a project with MemWiki installed: the host agent reads project context, scans repository material, writes synthesized domain knowledge, updates session context and work history, and leaves files for a later session. This workflow was selected because the shipped protocol names both its request and its target pages, while the session rules supply the persistence and later-consumption steps. It is not a constructed chain of independent CLI commands. The ingestion instruction is part of [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands); its session wrapper is [RT-RTE-agent-session](runtime.md#rt-rte-agent-session). SRC-1, `AGENTS.md`.

This is a doctrine/design-grounded workflow, not a demonstrated execution. The source also contains an attributed ingestion report, but no host transcript, tool trace or before/after validation accompanies it. Source inspection here covered `AGENTS.md`, `src/index.ts`, `README.md`, `.memory/wiki/log.md` and `.memory/wiki/index.md` at the frozen revision. All were already within the boundary's inspected scope; no new source or evidence layer is introduced. The CLI supplies implementation evidence only for setup and command rejection. SRC-1, `src/index.ts`, `.memory/wiki/log.md`.

### Request, handoff and decisions

1. **Setup prerequisite.** The operator launches initialization in the project root. The CLI creates absent hook, protocol and starter wiki files; it does not launch ingestion or a coding model. Existing hooks are skipped even if their contents do not route the host to MemWiki. Thus a successful scaffold message does not establish that the later workflow is reachable in a given host. The implemented installation and return boundary are [RT-RTE-cli-init](runtime.md#rt-rte-cli-init). SRC-1, `src/index.ts`.
2. **Host entry.** A host that discovers an installed hook is asked to supply `AGENTS.md` and hot context to its coding agent before work. Those local files supply guidance and prior project state, not a delegated-worker packet or authorization credential. The actual discovery, prompt precedence and file-tool grants remain external assumptions. See [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol). SRC-1, `src/index.ts`, `AGENTS.md`.
3. **Context selection.** At session/task start the foreground agent must read hot context and consult the index for domain pages if hot context is insufficient. The model decides sufficiency; the protocol supplies neither a measurable threshold nor a completeness check. This is requested selective loading, not an enforced context-window budget. SRC-1, `AGENTS.md`; [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).
4. **Ingestion request.** The user sends `/memwiki-ingest` in chat. The interpreting host agent, not MemWiki's Node dispatcher, owns the repository scan and synthesis. The request supplies the operation; repository files supply the content; the protocol names `stack.md`, `patterns.md` and `decisions.md` as destinations. Scan ordering, file selection details and parallelization are left to the agent. SRC-1, `AGENTS.md`; [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands).
5. **Knowledge admission.** The same foreground agent selects findings and writes the wiki using host tools. The session rules additionally request raw-source synthesis, preservation of knowledge, domain-specific pages when needed, and index links for newly created pages. The user initiates ingestion but is not specified as approving each resulting sentence. No separate reviewer or worker return is assigned in these instructions. SRC-1, `AGENTS.md`.

> - If you create a new file, you MUST add a link to it in `.memory/wiki/index.md`.
> - Synthesize any raw knowledge from `.memory/.raw/` into the wiki pages.
> - Never delete knowledge from the wiki. Only append or refine.
> --- `AGENTS.md`

### Verification, rejection and recovery

Ingestion is an open maintenance request. The inspected protocol provides no mandatory review between writing findings and retaining them, no expected-answer oracle, and no automatic accept/reject result for the scan. An agent can judge relevance and synthesize content, but that judgment is not independent verification. The exact ingestion instruction and its unobserved operation are retained in [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands). SRC-1, `AGENTS.md`.

The source-supported health path is a **separate user request**, `/memwiki-lint`, which asks the host agent to find outdated information, missing hot context or empty domain pages and propose fixes. It is not wired as a required ingestion gate or automatically invoked on ingestion failure. The README says lint fixes problems; the detailed protocol says propose fixes. This difference prevents treating a lint request as guaranteed repair or per-change approval. SRC-1, `AGENTS.md`, `README.md`.

> - `/memwiki-lint`: The agent will perform a health check on the wiki, fixing outdated information or filling in missing context.
> --- `README.md`

The executable has a concrete rejection path if the chat command is mistakenly supplied as a CLI argument: only `init` and `update` are admitted, so `/memwiki-ingest` reaches usage output and exit 1 before directory creation. Recovery is an operator correction of the invocation channel—send the ingestion request to the host chat—not an automatic retry. This follows the dispatch branch in [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), whose retained passage supplies the guard. SRC-1, `src/index.ts`.

For an interrupted or incorrect model-mediated ingestion, `AGENTS.md` specifies no checkpoint, rollback, retry owner or required preservation audit. The foreground host agent remains the named executor of requested edits and health proposals; external host approval, version control or human correction may exist but are uninspected. This bounded protocol finding does not imply that an external host cannot recover. Likewise the CLI's existing-file skip does not validate or repair malformed wiki content. SRC-1, `AGENTS.md`, `src/index.ts`; [RT-RTE-agent-session](runtime.md#rt-rte-agent-session), [RT-RTE-cli-init](runtime.md#rt-rte-cli-init).

### Delivery and next-session handoff

Within the protocol, delivery means the requested domain pages have been populated and the session-end persistence obligations performed: current state and next steps go into hot context, and a timestamped summary goes into the log. MemWiki defines no response schema, commit requirement or delivery acknowledgment. Those obligations, including their triggers, are quoted in [RT-RTE-agent-session](runtime.md#rt-rte-agent-session). Source instructions establish what should be left behind, not successful completion. SRC-1, `AGENTS.md`.

The consequential handoff is through project files rather than a direct agent-to-agent message. A later host agent is instructed to read hot context first; domain-page knowledge reaches it conditionally through index lookup. The log is retained but not an unconditional session-start read. The producer's instruction to write several pages therefore does not establish that every later consumer receives all findings or uses them correctly. The protocol does not define shared context for host subagents. SRC-1, `AGENTS.md`, `.memory/wiki/index.md`; [RT-BAP-host-protocol](runtime.md#rt-bap-host-protocol).

The retained work log illustrates the claimed delivery, while also showing why it cannot act as a verifier:

> - Triggered `/memwiki-ingest`. Scanned `package.json`, `tsconfig.json`, `src/index.ts`, and `README.md`.
> - Populated `stack.md`, `patterns.md`, and `decisions.md` based on project findings.
> --- `.memory/wiki/log.md`

That entry names four scanned paths; it does not establish compliance with an entire-repository scan. It also reports links to two new pages:

> - Updated `index.md` to link to the new `landscape.md` and `competitors.md` files.
> --- `.memory/wiki/log.md`

The inspected frozen index instead lists the seven standard wiki pages and contains neither link. Thus the reported index-update claim does not establish a surviving routing handoff at this revision. The artifact comparison supports that limited discrepancy, not a claim about when or why the reported change failed to persist. SRC-1, `.memory/wiki/log.md`, `.memory/wiki/index.md`.

> - [[decisions.md]]: Architecture Decision Records (ADRs).
>
> *(Agents: Create new files for specific features or domains as the project scales, and link them here).*
> --- `.memory/wiki/index.md`

The resulting account is a source-supported, single-foreground-agent workflow with durable file handoffs. Actual full scan coverage, accurate synthesis, session-end completion, later behavioral dependence and performance benefit remain unobserved. SRC-1, `AGENTS.md`, `.memory/wiki/log.md`; [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands), [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands)

Workflow selection: ingestion is the selected operation; lint is an optional separate diagnostic request, not its acceptance gate. The user assigns repository scanning and page population to the foreground host agent. The same agent decides what to retain; no separate reviewer handoff is assigned. Delivery lacks a machine-checkable completion contract. The retained ingestion report does not verify the requested scan scope or index-update survival.

#### On [RT-RTE-agent-session](runtime.md#rt-rte-agent-session)

Workflow persistence boundary: session-end hot/log edits wrap the selected ingestion task, and project files carry the handoff to a later session. The next consumer receives hot context first and domain knowledge only after conditional index lookup. There is no assigned recovery actor beyond the foreground executor, nor a specified direct worker-return channel. Successful persistence and subsequent use remain unobserved.
