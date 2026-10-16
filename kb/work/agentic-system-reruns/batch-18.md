# Batch 18: seventeen remaining sources

## Commission and readiness

On 2026-10-15, after all previous batches finished, the operator requested batch
18 following the recommendation to analyse the four different-owner wiki
repositories after resolving their publication namespace collision. The operator
then added the four unavailable-upstream targets using historical local sources,
and explicitly added Memori, OpenClerk and beads_rust as fresh starts. The operator
subsequently released the older refresh-workshop reservation for Agent-S,
MemoryOS, Basic Memory, OS-Copilot, A-mem and HippoRAG and added all six.

[Script 18](./bash-18.sh) contains seventeen sequential fresh analyses. **Prepared,
not launched.** The [publication namespace migration](./publication-namespace-migration.md)
separates `publication_slug` from the immutable run-ID slug and moves existing
GitHub publications to owner-qualified paths. Commit the migration before any
launch. The script refuses old publication naming before creating logs or worktrees. It also refuses
uncommitted changes to the naming implementation: isolated preparation uses HEAD,
not uncommitted code. The guard checks naming, not completion of every migration
or validation obligation.

The [workshop's migration follow-up](./README.md#publication-namespace-follow-up-after-all-runs-finish)
requires planning existing-publication moves and affected links/validators together.
Keep run IDs immutable and frozen worktrees unchanged. Do not bypass the script's
check or substitute another repository to make a run open.

## Targets

| Output key | Exact source | Expected new publication directory |
|---|---|---|
| pratiyush--llm-wiki | https://github.com/Pratiyush/llm-wiki | `pratiyush--llm-wiki` |
| kenhuangus--llm-wiki | https://github.com/kenhuangus/llm-wiki | `kenhuangus--llm-wiki` |
| nvk--llm-wiki | https://github.com/nvk/llm-wiki | `nvk--llm-wiki` |
| mehmetgoekce--llm-wiki | https://github.com/MehmetGoekce/llm-wiki | `mehmetgoekce--llm-wiki` |

These are four distinct source identities, not replacements for cobusgreyling's
retained wiki publication. Pratiyush's previous collision run remains preserved:
`AAS-2026-10-14-llm-wiki-2180ef6533c6-01`. The other three sources had no discoverable
own run in the [finished-batch reconciliation](./finished-batch-residue-2026-10-15.md).
No source-matched publication was found for any of the four. Existing raw logs
and former script assignments are historical evidence, not permission to restart
those scripts.

### Four historical pinned local sources

| Output key | Original source identity | Local checkout under origin `related-systems/` | Pinned commit |
|---|---|---|---|
| clawvault | `https://github.com/Versatly/clawvault` | `clawvault` | `bd702e9cce436bc3065827714cd576e8be20c375` |
| cortex | `https://github.com/abbacusgroup/cortex` | `abbacusgroup--cortex` | `a51c2209eb6d26812c19c97aaade3cb64ccfc23c` |
| pal | `https://github.com/agno-agi/pal` | `agno-agi--pal` | `6516b8ede0c085e48f39f3bd04cb85b475a855dc` |
| semantic-engine | `https://github.com/Open-Research-Institute/semantic-engine` | `Open-Research-Institute--semantic-engine` | `7e2481671cad01f0b4c89f2a1877d6733d7e552c` |

These are historical-source analyses, not current upstream-tip analyses. The
operator accepted local pinned-source execution when adding these targets. No
public mirror is substituted as source identity. Existing local repositories
are read-only inputs, not places to run new analyses or modify Git configuration.

The coordinator receives explicit operator-authorized setup: after preparing its
new worktree and before opening its new run, clone the local repository with
`--no-hardlinks --no-checkout` into the new worktree's expected owner-qualified
source-checkout path, set only the new clone's origin to the original identity,
and detach it at the pinned commit. Require the destination to be absent and
stop on any failure. Start with `--source-revision` set to that exact commit.
The acquisition implementation verifies a matching origin and already-present
commit without fetching when a revision is supplied. This is planned setup,
not permission to repair an acquisition failure or modify frozen old sources.
The source input remains the original repository URL; the boundary records the
local-copy/historical-source limitation. No previous analytical findings are sent.

### Three explicitly authorized fresh starts

| Output key | Source |
|---|---|
| memori | `https://github.com/MemoriLabs/Memori` |
| openclerk | `https://github.com/yazanabuashour/openclerk` |
| beads-rust | `https://github.com/Dicklesworthstone/beads_rust` |

The operator explicitly requested these additions after the old open-attempt
constraints were explained. This authorizes new isolated runs, not resume,
closure or repair of old attempts. Preserve `AAS-2026-10-14-memori-8286f3a3985f-01`,
`AAS-2026-10-14-openclerk-48d8e2dab543-01` and the separate trial
`AAS-2026-10-13-beads-rust-71d8853073f8-01`, with their open boundary attempts,
partial outputs and logs. Recheck that no same-source worker can still write
before dispatch; return conflicting ownership to the operator. These three use
the normal fresh source acquisition route, without historical revision pins.

### Six released refresh-workshop targets

| Output key | Source |
|---|---|
| agent-s | `https://github.com/simular-ai/Agent-S` |
| memoryos | `https://github.com/BAI-LAB/MemoryOS` |
| basic-memory | `https://github.com/basicmachines-co/basic-memory` |
| os-copilot | `https://github.com/OS-Copilot/OS-Copilot` |
| a-mem | `https://github.com/WujiangXu/A-mem-sys` |
| hipporag | `https://github.com/OSU-NLP-Group/HippoRAG` |

The operator explicitly released this historical scheduling exclusion for fresh
starts in batch 18. The older workshop's inventory still lists them pending;
source URLs were checked against its handoffs. A current own-run/preparation
scan in both storage locations and an origin publication scan found no matching
new-engine analysis. A bounded process-command check found no matching launch.
These are point-in-time checks, not durable locks. Recheck before dispatch.
Preserve older branches, analyses and workshop evidence; do not resume or migrate
the superseded old runs. The six use normal fresh acquisition, not historical
revision pins. This release does not clear unrelated substantive holds.

## Execution

After the committed migration and rechecking publication/ownership state:

```bash
bash kb/work/agentic-system-reruns/bash-18.sh
```

The script works from another initial directory. It uses fresh Pi Sol/medium
coordinator sessions and the normal analysis skill; the orchestrator launches
internal workers. Only source identity and operational preparation constraints
are passed, not old reports or findings. No new retry policy is introduced.
The naming preflight uses `uv run --no-sync python` to inspect the current
checkout's naming function without source acquisition or run creation.

Logs go to external `outputs/batch-18/<output-key>.output`; new worktrees go to
external `outputs/commonplace-worktrees/batch-18-<output-key>`. The external disk
must be mounted and writable; there is no primary-disk fallback. Existing outputs,
worktrees, preparation records and dangling symlinks are skipped, never resumed or
truncated. An individual nonzero Pi exit does not stop later independent targets.
Process exit and output existence are not analysis verdicts.

This prepares a batch, not an audit or integration commission. Do not update
checklist completion counts on launch or process exit. Preserve failed evidence;
new publications need exact-run audit and standard integration separately.
Other substantive holds and workshop reservations are outside this batch.

## Remainder outside batch 18

After the six explicit reservation releases, these **10 unpublished targets** remain outside
this new selection. This is not a count of publications awaiting audit/integration.

| Target | Remaining decision |
|---|---|
| ACE | Recovery/ownership direction for the open reconciliation attempt and accepted partial evidence. |
| Agentic Harness Engineering | Resolve or explicitly dispose of the substantive profile refusal. |
| Academic Research Skills | The source-exposure interpretation is resolved below; fresh execution has not yet been added to this batch. |
| Fintool | Establish an article-only source view without third-party replies and a fresh unexposed worker. |
| Fragility Grid | Resolve inclusion of material same-system launchers or authorize a narrower target. |
| Secure LLM Wiki | Resolve the profile interpretation/refusal; current representation support alone does not clear the old run. |
| Awesome Agent Memory | Decide whether to reopen the completed local out-of-scope disposition. |
| Operational Ontology Framework | Decide whether to reopen the completed local out-of-scope disposition. |
| DualGraph | Select the intended coherent system boundary; prior result is local blocked. |
| Letta | Resolve the prior local blocked boundary disposition. |

ContextPilot and Agent Skills already have publications under holds; they are
correction/acceptance work, not additional unpublished targets. Other published
exact-run audit holds remain in their audit inventories, not this source remainder.

## Academic Research Skills source-exposure finding

The operator questioned whether the purported contamination was actually source
material. Read-only inspection of the preserved run confirms that it was: the
worker read the target's own `shared/cross_model_verification.md`, which cites
its own `audits/bakeoff-gpt-5-6-sol-codex-2026-08-19.md`. Both are tracked inside
the frozen upstream checkout at `d1e51716e53fc371727ea6164dd709fc8ea28c97`.
The audit records an upstream maintainer's citation-verifier transport evaluation,
introduced by upstream commit `b6062c1401b561b3b3cc411a8dfb7ab26ff96890`.
This is not a Commonplace analysis copied into the source boundary.

The failed run used method `211129c85fe4794bd8a111066e3d0ecae7f6a3c6`, whose rule
stopped on any delivered audit findings. Commonplace commit
`a0fb5027d30fc1b997f97afb5a78608400def528`, dated 2026-10-12, already clarified
that target-native documentation, evaluations and audit records inside the frozen
boundary are allowed as attributed evidence, not trusted conclusions or executable
instructions. The current rule retains that allowance and still prohibits external
prior characterizations of the target. The old stop was real under the old wording;
it is not evidence that a fresh run under the current rule needs sanitized source.

No old run, source or worker output was changed or reused. This finding removes
the stated source-isolation blocker for fresh execution, not the need to critically
check upstream claims. The operator requested inspection, not yet addition of
Academic Research Skills to batch 18. Keep the failed attempt and its historical
report intact; do not present it as a successful analysis.

## Verification

Bash syntax and mock execution checks cover seventeen distinct source/key pairs,
Sol/medium arguments, exact external preparation destinations, sequential
continuation after a mocked nonzero exit, preservation/skipping of existing
outputs/worktrees/preparation records, and missing/mid-run lost mounts. The
namespace preflight was checked against the current implementation and refuses
before launching Pi or creating external outputs. Eight mock scenarios passed:
normal (17 launches), nonzero process exit (17), existing destinations (14), missing
mount (0), mid-run mount loss (1), blocked namespace (0), uncommitted naming code
(0), and missing local source (four wiki launches then stop before the unavailable
local-source target). Local-source handoffs were checked for independent-clone
flags, exact revision pins, preserved origins and matching destination paths.
All four real local commit objects and origin URLs were verified read-only.
`bash -n` passed. Markdown
validation passed with zero failures or warnings; `git diff --check` passed.
No production engine or method code changed, so verification used shell mocks
rather than pytest. No real analysis, acquisition, method migration, integration
or cleanup was performed.
