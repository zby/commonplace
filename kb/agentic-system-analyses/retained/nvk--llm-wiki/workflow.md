---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "llm-wiki plan-mode research workflow: nested delegation, source rejection, serialized compilation, interrupted-path recovery and delivery."
run-id: AAS-2026-10-17-llm-wiki-a93f86f698d7-01
reviewed-boundary: "95a042c68998559305bc69ac8c482c4e1a415ad3"
---

# llm-wiki workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a single-round, standard topic research request with `--plan`, an existing named active wiki, and `--no-specialists`. It is selected because the same shipped command connects request interpretation, user-approved decomposition, nested research delegation, source admission, article synthesis and delivery. It also specifies interruption recovery. This is the referent already declared as [RT-RTE-research-paths](runtime.md#rt-rte-research-paths), not a newly discovered route. Compilation is supplied by [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki).

The account describes instructions interpreted by an external host model, not an executed llm-wiki scheduler. Source inspection adds detail from SRC-1, `claude-plugin/commands/research.md` (prelude, plan mode and single-round phases), `claude-plugin/skills/wiki-manager/references/research-infrastructure.md` (lifecycle, resume and plan schema), and `claude-plugin/skills/wiki-manager/references/compilation.md` (compile loop and quality standards). These passages supply doctrine/design evidence only. No host run, retained user wiki or worker-return trace is supplied. The external host's actual scheduling, grants and model compliance remain unobserved.

### Request, scope and plan acceptance

The user supplies the subject and target wiki. The foreground model resolves configuration and the registry, verifies the master index, then checks existing raw/article indexes and searches for coverage gaps. An archived target requires restoration or explicit inclusion; missing initialization stops rather than initiating ordinary research. In this selected mode, `--no-specialists` excludes personal method bodies and records an empty specialist list. These are instruction-level scope decisions, not filesystem interpositions (SRC-1, `claude-plugin/commands/research.md`).

From existing knowledge and gaps, the foreground model proposes three to five independently searchable paths. The user sees names, focus, search angles, source targets, estimated parallelism and the single-pass compilation plan. The approval boundary is explicit:

> 3. Wait for user confirmation. If "edit", let them modify paths. If "n", abort.
> --- `claude-plugin/commands/research.md`

This accepts or rejects a research plan. It does not approve each later source or article. The selected workflow is an open research request, not an expected-answer exercise. Neither existing wiki coverage nor the credibility rubric supplies a known correct answer to the topic question.

### Delegation and what crosses each boundary

After confirmation, the foreground model requests one host Agent invocation per path. Each receives its focus/search angles, the standard prompt template, instructions to perform search → credibility → ingest, and a path identifier for raw names. A standard path-agent then requests five search sub-agents: academic, technical, applied, news/trends and contrarian. The general template supplies an objective, role focus, search strategy, brief current-wiki summary, constraints, return schema and quality guide (SRC-1, `claude-plugin/commands/research.md`). Thus the handoff requests selected context rather than wholesale hub loading.

Search workers are instructed to vary queries, fetch promising results, avoid paywalls/spam/thin duplicates, and return ranked sources. The prose asks for extracted content; the explicit return template lists title, URL, quality score, key findings and ingestion rationale. Consequently this account does not assume that a complete fetched document necessarily crosses the worker-return boundary. The later compile stage separately requests full reads of retained raw sources (SRC-1, `claude-plugin/commands/research.md`, `claude-plugin/skills/wiki-manager/references/compilation.md`).

The delegated contexts resemble separate task frames: selected instructions and summaries enter, findings return, and ingested artifacts remain independently reachable on disk. The target instructions do not establish when the host discards child contexts or how much returned text remains in the foreground window. Disk reachability is not proof that raw content is already model-visible. Actual host isolation and context disposal remain outside the inspected mechanism, as bounded in [RT-RTE-research-paths](runtime.md#rt-rte-research-paths).

### Review and source rejection before persistence

Within each path's requested full pipeline, returned search results undergo credibility review before ingestion. This is a second model judgment rather than accepting worker self-scores unchanged. The command scores peer review, recency, authority, bias and corroboration, deduplicates by URL/content, ranks by credibility multiplied by worker quality, and selects sources up to the target. The infrastructure clarifies that `--sources N` is per path in plan mode, not a total across the plan (SRC-1, `claude-plugin/commands/research.md`, `claude-plugin/skills/wiki-manager/references/research-infrastructure.md`).

The rejection path is source-level, not a failed workflow:

> - **Reject** (<0 points): Obvious spam, predatory journal, fabricated data → skip entirely
> --- `claude-plugin/commands/research.md`

Low-tier sources are retained only if no better source covers the angle and receive low confidence. Skipped sources and reasons enter the final report. The reviewing model owns these semantic assessments; no inspected classifier independently verifies peer review, bias or fabrication. No per-source human veto is prescribed after plan acceptance. This is policy-strength admission, not evidence that source reliability was successfully measured.

### Parallel persistence, then one compiler

Path agents write admitted material to typed raw files. The command requires path-prefixed names and defers index updates during parallel ingest. The infrastructure's concrete naming example uses `p<N>`; the command describes a path-slug prefix. Both express per-path name separation, but the precise spelling is not uniform across those instructions. Neither form establishes host-enforced write ownership (SRC-1, `claude-plugin/commands/research.md`, `claude-plugin/skills/wiki-manager/references/research-infrastructure.md`).

The key handoff is a barrier between raw-source production and article editing:

> After all path agents return, run a single compilation pass that:
>
> 1. Reads ALL newly ingested sources from all paths
> 2. Follows the standard compilation protocol in `references/compilation.md`
> 3. Draws cross-references between findings from different paths — this is the plan's primary value: the compiler sees the full picture across all paths simultaneously
> 4. Creates articles that synthesize across paths where findings connect
> --- `claude-plugin/commands/research.md`

The foreground compiler therefore receives retained source files, not just an aggregate worker verdict. It maps source concepts to existing or new articles, synthesizes rather than copying, preserves source links and adds reciprocal relationships. If a topic guide exists, it shapes article boundaries and scope; strict guide deviations require confirmation before writing, while advisory deviations are reported. Compilation's detailed standards and frontmatter checks remain those of [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki), not a second workflow-level admission transaction.

Serializing this phase narrows the intended same-article collision risk within the plan. It does not prevent another session from editing the same article. Derived-index repair addresses stale navigation, not lost article edits; the broader policy accepts last-write-wins ([RT-CLM-concurrent-writes](runtime.md#rt-clm-concurrent-writes)).

### Interruption, retry and delivery

The plan and per-path statuses are stored in `.research-session.json`. On a subsequent invocation, the model is instructed to inspect retained state and ask whether to continue or start fresh. The plan-specific recovery decisions are explicit:

> - **All `completed`** → skip to compilation (all sources are ingested, just need to compile)
> - **Some `pending`** → re-launch only pending paths (completed paths are not repeated)
> - **Some `in_progress`** → treat as `pending` (agent died mid-execution; raw files from partial execution are fine — deduplication handles any overlap)
> - **Some `failed`** → ask user: "Path '<name>' failed. Retry or skip?"
> --- `claude-plugin/skills/wiki-manager/references/research-infrastructure.md`

The foreground model owns resumption and dispatch; the user decides retry versus skip for a failed path. Partial raw files are kept and overlap is delegated to deduplication, not rolled back. Completed statuses are recovery hints, not an inspected independent check that every claimed file is present and valid. No generic compensation for already written articles is established by this protocol. The instructions do not fully specify the final barrier's interpretation after a user skips a failed path; successful all-path completion and the offered skip decision are supported, but a precise skip-state transition is not (SRC-1, `claude-plugin/skills/wiki-manager/references/research-infrastructure.md`).

Delivery comprises retained compiled articles and links, updated indexes/statistics, topic and hub log entries, and a foreground report. The report lists found/ingested/skipped sources, created/updated article paths, confidence reasons, connections, remaining gaps and follow-ups. Plan mode adds per-path yields and cross-path connections. No separate receiver acknowledgment or semantic acceptance test is prescribed in these inspected report phases (SRC-1, `claude-plugin/commands/research.md`). Report production is the instructed terminal step, not proof of an accepted or useful result.

On normal completion the ephemeral session file is deleted. The research infrastructure distinguishes durable `.session-events.jsonl` and `.session-checkpoint.json`, preserved for later briefings, from the disposable active plan. This supports a requested later resume/read-back channel, not observed successful recovery or replay. One-session-per-wiki overwrite policy also limits parallel recovery-state preservation (SRC-1, `claude-plugin/skills/wiki-manager/references/research-infrastructure.md`).

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

#### On [RT-RTE-research-paths](runtime.md#rt-rte-research-paths)

Workflow-specific coordination: nested search results undergo path-level credibility selection before path-owned raw writes; the foreground's all-path return barrier precedes the single cross-path compiler. User plan approval and failed-path retry/skip decisions are separate from model source/article admission. Deferred indexes and path prefixes coordinate the requested writes without supplying locks or a sandbox. The account above establishes these handoffs, their rejection/recovery branches and terminal reporting from SRC-1; all remain doctrine/design with operation uninspected.
