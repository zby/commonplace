# Fresh batch for rerunnable failures

## Decision

Under the operator's 2026-10-15 request for all failures that a fresh rerun could
plausibly fix, retain then-unstarted scripts 15–16 and add **script 17**. Together
these form one **39-target fresh-failure batch**, without duplicate schedules:

| Script | Targets | Selection |
|---|---:|---|
| [bash-15.sh](./bash-15.sh) | 16 | Fifteen provider/transport failures and dense-mem's isolated write-scope failure |
| [bash-16.sh](./bash-16.sh) | 6 | Established disk-full interruptions |
| [bash-17.sh](./bash-17.sh) | 17 | Sixteen older provider/transport failures and o-o's coordinator prompt-path typo |

The [independent selection report](./retry-selection-2026-10-15.md) contains all
39 exact source URLs, latest old run/preparation identities, failure evidence,
publication exclusions and deferred cases. Its recommendation is scheduling
evidence, not audit clearance or a promise that provider availability has recovered.

The coordinator **releases the 16 older operational holds for fresh source-first
starts only**. This follows the new all-rerunnable-failures request, superseding
the earlier decision to leave these targets stopped. It does not authorize
recovery, repair or deletion of their preserved attempts, including substantial
accepted partial work. The four older target-level holds for ACE, Agentic
Harness Engineering, Agent Skills and ContextPilot remain. All 13 exact-run
semantic audit holds also remain, including alternatives to integrated sources.
A fresh-start release never converts an old held publication into an accepted one.

Script 17 covers AI-Context-OS, ai-memex-cli, Amazon Science SAGE, Apache Maka,
Archie, AREX-Skill, arsumbris, Auto-claude-code-research-in-sleep, auto-harness,
Autocontext, Autogenesis, AutoSci, Beever Atlas, Binder, browzy.ai, byterover-cli
and o-o. The six disk-full open attempts in script 16 remain preserved and open;
fresh-start permission does not close them. Dense-mem's unauthorized identity
write remains an unresolved deviation in its old run.

## Execution boundary

**Preparation did not launch analyses.** The scripts are sequential Bash pipelines using
fresh Sol/medium sessions and normal internal analytical workers. The script
passes only the source URL and external isolated-preparation instruction; it
does not forward old reports, this selection report or historical findings.

Each new preparation must use external
`outputs/commonplace-worktrees/batch-<15|16|17>-<output-key>` and continue with
its returned command environment. Logs use separate external batch directories.
Mount/write checks and existing output/worktree/preparation guards refuse an
unsafe destination; there is no primary-disk fallback. Preserve old logs and
worktrees. Do not restart earlier scripts or resume failed runs.

Before launch, recheck selected sources for new publications, current ownership,
active worker tokens, existing outputs/preparations and disk capacity. The
selection report's absence-of-process checks are point-in-time evidence, not
locks. Wait for the current pipelines to finish; do not add pipelines while four
are active. A zero process exit or an output file does not establish publication,
audit clearance or integrated completion. Namespace migration remains deferred
until all analysis runs finish.

Amazon Science SAGE also shares the project-only `sage` publication slug with
`https://github.com/l33tdawg/sage`, published in its own new worktree as
`AAS-2026-10-15-sage-d3843de6d2dd-01`. Neither was in the origin's 70 sets at
selection. Keep their source identities distinct and include this pair in the
deferred owner-qualified migration. If the other source is integrated before
Amazon's fresh preparation, recheck the resulting namespace blocker rather than
replacing its publication or patching a frozen method.

## Observed execution follow-up

A read-only process sample at **2026-10-15T08:49:37Z** found all three scripts
running: outer Bash PIDs **598562** (15), **660493** (16) and **660778** (17),
with child shells. This coordinator did not launch them, determine the launcher,
interrupt them or claim their ownership. Preparation-time “unstarted” language
is not current process status. No scripts 11–14 matched that same process query;
that does not independently reconcile every possible orphan worker.

Separate subsequent metadata reads found four ready preparations, all under
external `outputs/commonplace-worktrees/`, with external `.venv/bin` command
prefixes and method `26c5bf9df8ca39166fd6bdc39476689dad437cb5`:

| Batch/key | Exact own run | Observed engine metadata |
|---|---|---|
| 15 / claude-workstream-kit | `AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01` | Completed publish attempt/effect; not audited in this status check |
| 15 / cludebot | `AAS-2026-10-15-cludebot-cb70d11d215b-01` | Open synthesis attempt |
| 16 / kblam | `AAS-2026-10-15-kblam-5a0c2fe96cc1-01` | Open reconciliation attempt |
| 17 / ai-context-os | `AAS-2026-10-15-ai-context-os-4a0e34822f96-01` | Open report-verification attempt |

These are non-atomic observations, not acceptance, a worker-liveness proof or a
certification of prelaunch reconciliation. Preserve their evidence and do not
start duplicate pipelines. Their later publications do not expand the fixed
next-61 audit intake. Namespace migration remains deferred while analyses run.

## Deferred, not blind retries

Keep substantive profile/validator issues for Secure LLM Wiki and Agentic
Harness Engineering outside this batch. Preserve ACE's unresolved ownership,
Agent Skills' reservation and semantic hold, and ContextPilot's public selector
qualification hold. Keep source-exposed Fintool and Academic Research Skills out
until an authorized unexposed source-first path exists. Fragility Grid needs a
scope decision; ClawVault, Cortex, Pal and Semantic Engine need source/access
confirmation. Four colliding llm-wiki sources await the separately deferred
namespace migration.

Memori, OpenClerk and the separate beads_rust trial have open boundary attempts
without established terminal failure or worker-ownership reconciliation. Their
lack of a matching live process is not sufficient to label them transport
failures. Completed out-of-scope or blocked local outcomes are not retried.
Older refresh-workshop reservations remain excluded.

## Verification

The coordinator reconciled all 39 unique source/key pairs with the independent
selection. Bash syntax passed for scripts 15–17. Script 17's six mock scenarios
passed: normal 17 launches; continuation after an initial process exit 7; three
existing-output/worktree/preparation skips with bytes preserved; missing mount;
mount loss between targets; and unwritable external directories. Every mock
invocation used Sol/medium and the exact external preparation destination.
No real Pi process, analysis, acquisition or external-disk write ran in these checks.

`uv run pytest tests/commonplace/general tests/commonplace/agentic_analysis`
passed: **469 passed, 96 deselected**, in 57.70 seconds. This is selected general
and analysis coverage, not the complete suite. Markdown validation covers the
selection and decision records, not the historical analyses or failed runs.
