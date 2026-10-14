# Clean residue batch 09

## Commission and boundary

On 2026-10-14 the operator requested one more Bash batch, then specified that it
must include nothing from previous runs: only the clean residue. The resulting
[bash-09.sh](./bash-09.sh) contains **76 untouched eligible targets**, rather than
another ten-target sample. It runs them sequentially in one script. This is
preparation only; the script and no analysis were launched by this commission.

Selection uses [the checklist](./systems.md) at the acceptance checkpoint of
38 complete, 148 pending and 20 held. Historical reviews supply source identities
only; their findings are not passed to analysis workers. Those historical baseline
accounts do not make a target a previous run of this rerun workshop.

## Selection and exclusions

Checked every pending target against scripts 01–08, existing output filenames,
origin retained publications, prepared-worktree names and source identities in
129 preserved current-engine `run.json` files. Those run files identify 90 distinct
GitHub sources. Match repositories by owner/repository, case-insensitively, not
just publication slug. Also checked the seven document locators directly against
stored run parameters. No selected source matches a preserved current-engine run.

Of 148 pending targets, exclude **72**:

- **61** already scheduled in scripts 01–08, whether unstarted, running, stopped
  or published. No prior batch is silently retried.
- **8** reserved or explicitly excluded: A-mem, Agent-S, Basic Memory, HippoRAG,
  MemoryOS, OS-Copilot, Academic Research Skills and beads_rust. Preserve their
  coordination and source-isolation/recovery constraints.
- **3** separately attempted: Letta, Memori and OpenClerk. Preserved runs or
  existing outputs rule them out even though their checklist rows remain pending.

All 38 completed targets and 20 held targets are excluded before these checks.
ContextPilot is held and absent; the earlier separate rerun request is not folded
into this untouched-target batch. No held, failed, partial, experimental or
uncertain previous run is included for recovery.

LLM Wiki (nvk) remains eligible. The existing `llm-wiki` publication belongs to
cobusgreyling, not nvk. Use output key `nvk--llm-wiki` to avoid confusing those
source identities. Likewise use `isaacclupus-mnemosyn-spec` as the kebab-case
output key for the checklist's underscore-bearing Mnemosyne identifier.

## Source and execution contract

The script contains **69 repository sources and 7 document sources**. Repository
locators come from the targets' retained inclusion references. The document
sources are AIDE2, Claude Code dynamic workflows, Fintool, Incremental
Self-Improvement, NAMS, Trajectory-Informed Memory Generation and WikiSkill.
Document calls explicitly name a document-grounded source rather than presenting
an article or paper URL as a repository locator. No implementation repository
is inferred. Acquisition/freezing, scope and all analysis stop conditions remain
the skill's responsibility; no historical findings accompany either source route.

Execution otherwise keeps the previous scripts' Pi/Sol/medium invocation,
source-first skill, non-overwriting output guard and continuation after individual
nonzero process exits. No retry, automatic recovery, audit, integration, cleanup,
comparison refresh or push is added. A zero process exit remains insufficient
analysis evidence. Each analysis has its standard internal workers; sequential
outer execution does not cap total requests if other scripts remain active.

Run when desired:

```bash
bash kb/work/agentic-system-reruns/bash-09.sh
```

Starting it while existing batches are active adds another analysis pipeline;
recent overload errors remain a reason to choose timing deliberately, not proof
of a particular concurrency cause. Selection is a snapshot, not a reservation.
If execution is delayed or another operator starts these targets, recheck source
ownership and run state. The output-exists guard catches only the matching output
key and is not a source-level lock.

## Verification

Passed `bash -n` and a source-identity/checklist check: 76 unique output keys
and source locators; no intersection with scripts 01–08 or 129 preserved run
records; no existing selected outputs, reservations, holds or completed rows;
and exact coverage of the untouched eligible residue, including nvk. The check
accounts for all 72 excluded pending targets. An initial metadata extraction
included a Markdown backtick in a repository locator; correcting that extraction
made the check pass without changing batch membership.

This record and the changed workshop README passed `commonplace-validate` with
zero failures or warnings. General and agentic-analysis tests
(`uv run pytest tests/commonplace/general tests/commonplace/agentic_analysis`)
passed **469 tests**, with **96 deselected** by the default marker filter,
in 57.57 seconds. No slow-test behavior, production
method or engine code was changed. The real script was not executed as a test.

Preparation does not change checklist completion counts or mutate any run,
publication, source, original log or unrelated workshop work.
