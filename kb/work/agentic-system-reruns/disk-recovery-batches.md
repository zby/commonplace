# Batch preparation after the disk-full interruption

## Commission

On 2026-10-14 the operator said they were moving the large output directory to
`/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/` and requested that the two
unstarted scripts use that disk, plus new scripts for systems with no results.
This prepares scripts only; it does not launch analyses or recover frozen runs.
The operator owns the log move. No original log, partial run or publication was
moved, deleted or modified by this preparation.

## Files and selection

- [bash-11.sh](./bash-11.sh): the same 20 untouched targets, now external logs.
- [bash-12.sh](./bash-12.sh): the same 16 untouched targets, now external logs.
- [bash-13.sh](./bash-13.sh): 20 targets from the disk-full empty-output residue.
- [bash-14.sh](./bash-14.sh): the remaining 18 eligible empty-output targets.

The 16:45 status check found 49 publications in batches 01–10, 30 nonempty
unpublished outputs, and 41 zero-byte outputs. None of those batch scripts or
workers remained running. Six interrupted runs retained open attempts: KBLaM,
LLM-WIKI-MCP, MiroShark, Origin, Mnemosyne spec and Quicky Wiki. Other unpublished
results include earlier failures, blocked boundaries and local out-of-scope
outcomes. Those are not equivalent to an unstarted target.

For these fresh batches, “no results” means an original zero-byte output **and
no recorded own run for that source**, not merely no public overview. All 41
empty-output sources were checked against preserved run parameters; none had
an own run. Keep the six partial runs, all prior nonempty failures, local
results, holds and reservations out of these scripts. Their recovery requires
its own supported decision; no accepted or rejected evidence is silently reset.

Three otherwise untouched sources are deferred: kenhuangus/llm-wiki,
nvk/llm-wiki and MehmetGoekce/llm-wiki. The shipped source-slug function uses the
repository's final segment, so all map to `llm-wiki`. That destination in main
belongs to cobusgreyling; the opening guard rejects a different source, as
already observed for Pratiyush/llm-wiki. Different output keys do not fix the
publication namespace. This is a code/namespace follow-up, not permission to
rename or replace existing publications. After excluding these three, the new
scripts cover **38** sources: 37 repositories and the NAMS document source.

## Output location and execution

Scripts 11–12 write to the moved directory:
`/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/`.
Scripts 13–14 write beneath its `batch-13/` and `batch-14/` subdirectories.
Those new paths preserve the original zero-byte files while avoiding the old
output-exists skip. Each new output retains the noclobber/existing-output guard;
no file is truncated or automatically retried.

All four scripts check that the disk is mounted before setup and every launch,
and that their output directory is writable. They do not fall back to repository
storage if the disk is unavailable. The destination directory must belong to or
be writable by the operator. During the move it was root-owned with mode 700;
after the operator completed the move it was zby-owned and writable. All 38
selected original logs were rechecked as zero-byte files at the moved destination.
This commission changes neither permissions nor mount state.

Run whichever pipelines are wanted after the move:

```bash
bash kb/work/agentic-system-reruns/bash-11.sh
bash kb/work/agentic-system-reruns/bash-12.sh
bash kb/work/agentic-system-reruns/bash-13.sh
bash kb/work/agentic-system-reruns/bash-14.sh
```

These run sequentially in one shell. Separate shells or `&` allow concurrency.
Do not restart scripts 01–10: they are historical execution records and still
use the former output location. The changed scripts retain Sol/medium, document
source handling and the distinction between process exit and analysis outcome.
Individual process failures do not stop subsequent independent targets, except
for failed disk mount/setup checks. No worker retry or analysis-state recovery
is added.

Moving logs addresses only log storage. Prepared worktrees, source checkouts,
Pi session files and temporary worker files remain on the primary filesystem.
After the operator's move, the check showed 48 GB available on the primary disk
and 774 GB on the output disk. External log capacity is not proof that the
primary disk can sustain every remaining analysis. Check both disks before
starting more pipelines.

## Audit handoff and verification

[Audit-unintegrated prompt](./audit-unintegrated-prompt.md) is the separately
requested prompt for inventorying and auditing every own-worktree publication
not integrated into main, including older alternatives. It grants no integration,
reanalysis or cleanup and follows moved/truncated log evidence carefully.

Passed Bash syntax for scripts 11–14, unchanged-target checks for 11–12,
38-source uniqueness and 20/18 partition checks, no-own-run checks for every
newly scheduled source, and non-overwriting mounted external-path checks.
All 38 original empty logs were verified at the moved destination. The three
namespace-collision sources remain excluded. This record, the audit prompt and
changed workshop navigation passed validation with zero failures or warnings.
`uv run pytest tests/commonplace/general tests/commonplace/agentic_analysis`
passed 469 tests, with 96 deselected by the default marker filter, in 52.56 seconds.
No relevant slow-test behavior, production engine or method was changed.
No real analysis or auditor was launched as a test or otherwise. Completion
counts are not changed by this preparation.
