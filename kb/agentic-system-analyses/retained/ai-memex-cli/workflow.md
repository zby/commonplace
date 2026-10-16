---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of ai-memex-cli: bounded ingest, mechanical repair feedback and best-effort host-context delivery"
run-id: AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01
reviewed-boundary: 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f
---

# ai-memex-cli workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is `memex ingest <target> --loop`: delegate source integration, inspect the resulting wiki mechanically, feed defects to a subsequent child invocation, and refresh registered project contexts after a clean pass. It is selected because one shipped controller joins these steps; it is not an invented chain of independent capture and query capabilities. It overlaps [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair) and the after-clean portion of [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). The [boundary](boundary.md) supplies SRC-1 and the frozen revision. This account establishes source-level wiring and requested model behavior, not a successful run: no child transcript, resulting vault or host-consumption trace was supplied.

### Request and delegation

The CLI caller supplies a target hint, optional agent and vault, and iteration cap. The driver ensures vault/agent availability and calls `runIngestLintLoop`; this branch defaults to three iterations. The controller owns sequencing, while the child owns semantic integration. On each ingest stage it passes target, agent, vault and the previous lint report to `ingestCommand`. A fresh invocation reloads configuration, live schema and current index. The child receives these selected inputs, not the foreground conversation or the entire previous child's reasoning (SRC-1, `src/cli.ts`, `src/core/ingest-lint-loop.ts`, `src/commands/ingest.ts`; [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt)).

The selected external executable runs with the vault as working directory. It must discover and read actual source files and existing pages using its own tools, then create/update wiki pages and update index/log. The target is not a validated file allowlist. Model tools admit edits directly into the live vault, before verification. Raw preservation and schema compliance are instructions, not a CLI-enforced transaction or sandbox; the runtime's raw-preservation and approval limits therefore apply unchanged ([RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), SRC-1, `src/commands/ingest.ts`). The schema's request for discussion does not establish a human approval step in this headless loop.

The installed ingest reference explains semantic choices: update versus create, preserve conflicts, cite source material, and ask before uncertain merges. This is doctrine for an agent following the skill, not proof that every direct CLI child receives that reference separately. Its completion contract is more informative than process exit alone (SRC-1, `templates/skills/ai-memex/references/ingest-workflow.md`):

> Report:
>
> - raw files consumed
> - wiki pages created or updated
> - unresolved contradictions or questions
> - lint/link-check status if run
> --- `templates/skills/ai-memex/references/ingest-workflow.md`

The implementation streams child output and cleans temporary prompt files. It does not parse such a completion report or compare requested files with an approved edit set. A zero child exit establishes process completion only ([RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), SRC-1, `src/commands/ingest.ts`).

### Verification and another round

After ingestion returns, the controller runs `runLint` on the reloaded wiki. Its default checks are orphan pages, broken links and missing/invalid frontmatter. This is a deterministic structural evaluator, not a factual answer oracle. Semantic lint is a separate opt-in route, not an automatic stage in this workflow ([RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint), SRC-1, `src/commands/lint.ts`, `src/core/ingest-lint-loop.ts`).

Zero issues permits the controller's clean outcome. Nonzero issues reject *clean completion*, not the already-written pages: the controller prints findings and, if it can continue, retains the report for the next ingestion. The prompt prepends up to 200 issue descriptions and tells the next child to fix them before ingesting more raw material. Report fields become natural-language guidance; the model still chooses actual edits (SRC-1, `src/commands/ingest.ts`):

> lines.push('Do NOT mutate raw/ sources to silence lint — always fix the wiki side.');
> --- `src/commands/ingest.ts`

The next child gets freshly read schema/index plus that report, not the prior child's full working context. Filesystem changes and streamed output cross the child boundary; child history, provider persistence and eviction remain opaque. Thus delegation isolates the caller's supplied task context, but does not establish a host-level guarantee that all intermediate context is discarded ([RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair), SRC-1, `src/core/ingest-lint-loop.ts`, `src/commands/ingest.ts`).

### Failure, stalled repair and recovery ownership

A supported failure path is child ingestion failure followed by lint. `ingestCommand` catches child execution errors and cleans its prompt delivery resources. The controller also catches an escaping ingest-stage exception and proceeds to mechanical inspection (SRC-1, `src/commands/ingest.ts`, `src/core/ingest-lint-loop.ts`):

> // fall through to lint so the caller still gets a report
> --- `src/core/ingest-lint-loop.ts`

Consequently a clean report can follow a failed or ineffective ingestion when existing files already pass the checks. Clean is not evidence that the requested integration happened. Neither catch restores partial edits. Automatic recovery here means another model attempt guided by structural findings, not rollback or a guaranteed corrected artifact ([RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair)).

If consecutive reports have the same issue keys, the default no-change guard returns a stalled outcome. Keys compare issue type/page/source/target, not frontmatter error details. A cap stops further attempts even with outstanding issues. Neither stop undoes admitted pages or invokes a human remediation workflow; the caller must decide whether to edit inputs/pages, change settings or retry. The shared controller also permits cooperative cancellation between stages and disabling the no-change guard; these are controller/watcher controls, not all exposed by the selected ingest CLI branch. Lint exceptions are not caught by this controller's ingest catch, so the clean/stalled/capped result contract does not cover every failure (SRC-1, `src/core/ingest-lint-loop.ts`, `src/cli.ts`; [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair)).

### What makes the result delivered

The durable work product is the live wiki/index/log state requested from the child, independently of whether the loop ends clean. The controller's clean result means zero mechanical issues, then a best-effort refresh attempt. Its result includes iterations, stop reason and final report; the selected CLI awaits that result without rendering it as a separate structured delivery artifact, relying instead on stage logging and child output (SRC-1, `src/core/ingest-lint-loop.ts`, `src/cli.ts`).

After a clean pass, the controller calls context refresh for registered projects. Refresh rebuilds page metadata, renders a digest/bootstrap, and writes marker-bounded Markdown or a Cursor rule. This delivers a derived context projection rather than the full wiki. Per-host refresh errors are caught, and the outer refresh wrapper also swallows errors; therefore clean loop completion does not guarantee that all host files were updated (SRC-1, `src/commands/context.ts`, `src/core/ingest-lint-loop.ts`; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)):

> /* best-effort — never fail the loop because of context refresh */
> --- `src/core/ingest-lint-loop.ts`

A later host must load and act on the projection for it to affect answering. That dependency remains unobserved, as does actual child compliance. The bounded delivery claims are wired subprocess output, live-file write requests, structural stopping predicates and best-effort context-file refresh—not semantic correctness, convergence, host activation or improved future performance.

### Inspection coverage

Additional workflow inspection under SRC-1 covered the complete `src/core/ingest-lint-loop.ts`, `src/commands/ingest.ts` and `templates/skills/ai-memex/references/ingest-workflow.md`; the ingest dispatch in `src/cli.ts`; mechanical report construction in `src/commands/lint.ts`; and registered-host refresh in `src/commands/context.ts`. These supply implementation evidence and separately attributed workflow doctrine. No target code, tests, services or model providers were executed.

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

#### On [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write)

Workflow role: each iteration's delegated semantic writer. Its requested page/index/log effects precede mechanical verification. Completion output is not parsed into an artifact acceptance decision; a failed child can leave files that the following lint inspects. Human content approval remains a requested conversational practice, not a CLI inter-stage gate.

#### On [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair)

Workflow role: selected controller reached directly through `ingest --loop`, without requiring a watcher event. It accepts or rejects the clean outcome, not each page write. Cap/no-change stops retain existing edits and leave further remediation to the caller. Mechanical lint failure can escape rather than yield a normal loop result. No reliable semantic integration or theory revision follows from this feedback wiring alone.

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

Workflow role: downstream after-clean projection refresh. The loop's success does not require successful refresh of every registered host, and refreshed host files do not establish later model consumption. Delivery to files and behavioral activation remain separate conclusions.
