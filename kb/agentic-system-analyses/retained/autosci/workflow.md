---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AutoSci workflow account: manifest-driven parallel initialization, paper-specific handoffs, parent verification, failure recovery and wiki delivery."
run-id: AAS-2026-10-15-autosci-430df584df8f-01
reviewed-boundary: f5c2fe009c6683b6aa5b668de759a0610c938aaf
---

# AutoSci workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects `/init` through parallel `/ingest` and parent fan-in. It is representative because it constructs the retained wiki that later research and question-answering skills consume, and explicitly allocates preparation, delegated writing, verification and recovery. The route already has a canonical declaration, [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest); the workflow detail below annotates it rather than declaring another route. Its paper-writing portion overlaps [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle).

All source evidence is SRC-1 at the frozen revision. Added inspection covered the complete active `.claude/skills/init/SKILL.md`, `.claude/skills/init/references/parallel-ingest.md`, `.claude/skills/ingest/SKILL.md` and `.claude/skills/ingest/references/init-mode.md` (doctrine/design), plus linked-worktree rebuild guards in `tools/research_wiki.py` and the main lint/fix/exit path in `tools/lint.py` (implementation). Correction inspection additionally read `.gitignore` and reread both parallel-ingest references (implementation of Git exclusion rules and doctrine/design for staging). These reveal a payload-transport contradiction, detailed below. The sources establish a prompted coordination protocol and narrower executable checks, not an observed initialization. No target commands, tests, providers or examples were executed. Successful delegation, scientific accuracy, conflict resolution and subsequent use remain unobserved.

### Request to prepared delegation set

The user supplies sources under `raw/` and optionally a topic. The foreground agent owns `/init`. It initializes the wiki, prepares local papers, plans discovery, trims the final set and fetches selected external sources. Notes/web express user intent and may seed explicitly provisional pages; they are not literature-grade support. Local papers preferentially receive canonical prepared paths under `raw/tmp/`; introduced papers go under `raw/discovered/`. The user must explicitly request local-only behavior. Starting `/init` is not per-paper or per-entity approval (SRC-1: `.claude/skills/init/SKILL.md`).

The handoff boundary is an explicit source manifest, not a fresh directory scan:

> - `.checkpoints/init-sources.json` is the single source of truth for downstream ingest order
> --- `.claude/skills/init/SKILL.md`

The agent is instructed to trim to 8–10 papers and stop/revise an out-of-range selection before fetch, with exceptions for local-only mode or more than ten user-supplied parseable papers. Tool code owns detailed ranking constants; this inspection did not independently audit that ranking implementation. The agent chooses content under qualitative relevance, freshness, connectivity and survey-coverage guidance. There is no reference-answer oracle. Preparation/API failures can degrade discovery or retain fallback local paths with warnings instead of aborting the entire request (SRC-1: `.claude/skills/init/SKILL.md`).

### Parent to paper workers

Before fan-out the parent is instructed to stash unrelated dirt, commit the scaffold/manifests, record the base branch/commit and stash reference, and verify union-merge attributes for shared index/log/graph files. A detached checkout stops the protocol. Each worktree is intended to branch from the same scaffold commit; ordering comes from the source manifest's `shortlist_rank`. Starting from the same commit excludes earlier workers' unmerged edits, but does not establish that required generated inputs are in that commit (SRC-1: `.claude/skills/init/references/parallel-ingest.md`, `.gitignore`).

The staging recipe uses unforced `git add` and explicitly names ignored checkpoints. The ignore rules exclude generated raw sources, wiki entity/graph content and `.checkpoints/`; the supplied runtime record retains the staging command and representative rules in [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest). Thus staging can report ignored-path errors, and newly generated payloads are not thereby included in `BASE_COMMIT`. Already tracked files can still be staged. No supplied tracking override or alternative transfer resolves this mismatch. This is a source-supported break in the preparation-to-worker handoff, not merely uncertainty about successful execution.

Each delegated task receives one canonical relative source path, INIT MODE restrictions, and a shell working directory in its own worktree. The parent requires `/ingest`, not an improvised substitute:

> - The subagent's shell working directory must be the worktree path (`$WT_PATH`), not the main repository root. All relative paths resolve from there.
> - Execute `/ingest` for exactly one relative source path.
> - Do not bypass `/ingest`.
> --- `.claude/skills/init/references/parallel-ingest.md`

The worktree exposes files actually present in `BASE_COMMIT`, not ignored local payloads merely named in a prompt. Required canonical sources and manifests are therefore not established as visible there. INIT MODE explicitly requires prepared `raw/tmp/` or `raw/discovered/` inputs and forbids workers from writing `raw/`, so that reference does not supply a worker-side source-repair route (SRC-1: `.claude/skills/ingest/references/init-mode.md`, `.gitignore`).

> - `raw/` is strictly read-only — do not write to `raw/tmp/`, `raw/discovered/`, or anywhere else under `raw/`
> --- `.claude/skills/ingest/references/init-mode.md`

The single-source rule constrains requested work, not filesystem access. Claude Code supplies the agent context and actual scheduling; the source does not establish a precise concurrency cap or host context-isolation guarantee. Per-task parsing and reasoning are intended to remain delegated; only actually committed files can cross back through Git, alongside the requested compact ingest result. This is frame-like context separation as intent, but input transport is unresolved, committed artifacts can survive the task, and host conversation retention is uninspected.

Workers resolve identity, stop on a matching existing paper, enrich metadata when services permit, write paper/entity pages, append graph relations and log the ingest. The model decides summaries and merge-versus-create choices. Entity creation limits and similarity checks discourage duplicates. Shape checks cover required fields, enum values and YAML parsing, not a complete semantic audit (SRC-1: `.claude/skills/ingest/SKILL.md`).

INIT MODE narrows normal ingest: raw inputs are read-only; citation sweeps, derived rebuilds, visualization, conflict-prone topics and reverse-link edits to existing pages are deferred. Relationships can instead be recorded as edges for parent reconciliation. This division avoids competing rewrites; it also makes worker completion alone insufficient to call the wiki integrated (SRC-1: `.claude/skills/ingest/references/init-mode.md`).

### Verification and fan-in

The worker must check that it is on an `init-` worktree branch and commit only successful work. An incomplete ingest is not an admissible success artifact:

> If the ingest fails part-way through (partial failure), do **not** commit the incomplete state. Let the parent `/init` handle the failed worktree at fan-in.
> --- `.claude/skills/ingest/references/init-mode.md`

The parent is instructed to wait for worker completion, then merge committed branches sequentially in planner order. However, the worker instruction to stage every created/modified wiki file supplies no force-staging or tracking override. Newly generated entity/graph files remain ignored under the shipped rules; a nonempty commit may contain tracked index/log changes without the intended paper payload. A commit or successful merge therefore does not verify payload inclusion (SRC-1: `.claude/skills/ingest/references/init-mode.md`, `.gitignore`). A missing ingest commit is an explicit rejection condition, not permission to merge an empty branch; the supplied runtime record retains that passage in [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest). The parent resolves concept/method conflicts conservatively. A second worker's same-slug concept creation can conflict even though shared append files use union merging. The INIT MODE reference tells the parent to retain the earlier write and rerun similarity matching for the later one. File-level merge success is not semantic acceptance (SRC-1: `.claude/skills/init/references/parallel-ingest.md`, `.claude/skills/ingest/references/init-mode.md`).

After the requested merges, the parent requests edge/citation deduplication, index/context/gap rebuilds and `lint.py --fix`. These operate on files actually available in the parent; they do not transport ignored worker output or repair missing source inheritance. Lint advertises deterministic repair of reverse links and defaults; its main function counts red issues from the initial scan, applies fixes and exits according to that initial count. Consequently, even a repairing invocation can exit nonzero; this body does not rescan to certify a clean final wiki:

> red = sum(1 for i in issues if i.level == "🔴")
> --- `tools/lint.py`

> sys.exit(1 if red > 0 else 0)
> --- `tools/lint.py`

The inspected `/init` instructions request lint but do not define a comprehensive rescan-and-accept loop or whole-pipeline transaction. Do not interpret their final report as proof of a clean semantic audit. Backlink repair is assigned to fan-in, but complete reconstruction for every possible omitted relation was not established by this selective implementation inspection (SRC-1: `.claude/skills/init/SKILL.md`, `.claude/skills/ingest/references/init-mode.md`, `tools/lint.py`).

Some separation is executable: selected rebuild wrappers reject linked worktrees with exit code 2, keeping those invocations parent-owned. This is narrower than a sandbox; Git-detection failure returns false and the context wrapper delegates to `compile_context`, so the guard does not prohibit arbitrary file writes or every compiler entry point (SRC-1: `tools/research_wiki.py`; see [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest)).

> def rebuild_context_brief(wiki_root: str, max_chars: int = 8000) -> None:
>     """Backward-compatible alias for ``compile_context --for general``."""
>     _refuse_in_linked_worktree("rebuild-context-brief")
>     compile_context(wiki_root, "general", max_chars)
> --- `tools/research_wiki.py`

### Failure recovery and delivered result

A single failed paper is checkpointed, skipped and reported while other papers continue. That is distinct from the empty-success-branch rejection: a known failure must not be treated as a successful ingest commit. Partial work remains for parent handling, rather than being automatically admitted. No atomic rollback of already merged successful papers is specified. User intervention is explicitly required for detached HEAD; parent/agent intervention owns failed worktree handling and merge conflicts (SRC-1: `.claude/skills/init/SKILL.md`, `.claude/skills/ingest/references/init-mode.md`, `.claude/skills/init/references/parallel-ingest.md`).

After merging, citation backfill is serial and best-effort. Visualization errors also warn without failing `/init`. The protocol requests worktree branch/directory removal after merge, but Git fan-in preserves only committed files. Ignored worker output is not thereby preserved; cleanup must not be read as proof of successful payload delivery. The parent restores the saved stash at the end; failure retains checkpoint metadata and requires a reported manual recovery step:

> If `stash_ref` exists, pop it at the end. If stash pop fails, keep the checkpoint and report the failure.
> --- `.claude/skills/init/references/parallel-ingest.md`

Intended delivery is a retained, integrated wiki plus the parent's categorized report: prepared local ingests, fallback local ingests, discovered papers, provisional pages, created/updated pages, failures/skips and visualization status. The shipped staging instructions do not establish that the selected sources reach workers or that new wiki payloads return through Git. A report or nonempty merge cannot establish that intended delivery. Actual tracking/staging conditions or another transfer mechanism would be needed; none is supplied. This is separate from the protocol's supported allowance for individual paper or optional rendering failures. The procedures contain stale HTML wording although their displayed visualization commands generate Obsidian configuration and Canvas; this account claims only those requested commands, not HTML generation. Source inspection establishes neither that delivery occurred nor that every derived relationship was restored (SRC-1: `.claude/skills/init/SKILL.md`).

Wiki payloads actually retained in the parent can enter later question-answering through [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). Those records distinguish retrieval instructions from demonstrated behavioral dependence. There is no exercised-learning or reliability claim here.

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

#### On [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest)

Workflow-specific acceptance boundaries: the parent selects a final manifest before intended delegation, but unforced staging against shipped ignore rules does not establish source/manifest inheritance. Workers are instructed to return committed paper-specific changes; neither the commit requirement nor a nonempty commit verifies inclusion of newly ignored wiki entities/graph. Parent fan-in admits only actually committed artifacts sequentially and owns semantic conflict resolution and shared rebuilds. A worker's textual success, a nonempty commit or a successful merge alone is insufficient to establish payload delivery. A failed worker is reported separately rather than merged as an empty success. The source assigns narrow shape checking to the worker and deterministic repair to parent lint, not scientific validation to either mechanism. Detailed handoffs, failure distinctions and delivery limits are traced above.

Workflow-specific recovery ownership: workers withhold partial commits; the parent handles failed worktrees and conflicts, records skipped papers and preserves stash-recovery metadata when restoration fails. External host execution and agent compliance remain necessary. The workflow intends partial delivery with explicit failures, not whole-request atomicity or a demonstrated clean final-state certificate.
