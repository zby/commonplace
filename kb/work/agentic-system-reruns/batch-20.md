# Batch 20: nine ordinary fresh reruns

## Commission and status

The operator requested a regular Bash batch after separating fresh reruns from
[batch 19's selected-job recoveries](./batch-19.md). [Script 20](./bash-20.sh)
starts **nine fresh analyses**, sequentially, in new external worktrees. It does
not reset or resume preserved runs. Initial preparation launched nothing. The
operator subsequently ran the batch in another console; all nine runs completed
internally. They are now covered by the
[completed independent audit](./batches-19-20-audit-results.md): seven qualified
positive recommendations, with MehmetGoekce's LLM Wiki and ClawVault held. No
checklist acceptance or integration is implied.

```bash
bash kb/work/agentic-system-reruns/bash-20.sh
```

The script works from another initial directory. Each target gets a fresh Pi
coordinator using Sol/medium and the ordinary analysis skill. Analytical workers
still require the harness tool and the skill's worker-launch diagnostic. The
outer operator-run CLI processes are not substitutes for worker delegation.

## Selected targets

| Output key | Source identity | Revision policy |
| --- | --- | --- |
| academic-research-skills | `https://github.com/Imbad0202/academic-research-skills` | Normal fresh acquisition |
| kenhuangus--llm-wiki | `https://github.com/kenhuangus/llm-wiki` | Normal fresh acquisition |
| nvk--llm-wiki | `https://github.com/nvk/llm-wiki` | Normal fresh acquisition |
| mehmetgoekce--llm-wiki | `https://github.com/MehmetGoekce/llm-wiki` | Normal fresh acquisition |
| clawvault | `https://github.com/Versatly/clawvault` | Local historical commit `bd702e9cce436bc3065827714cd576e8be20c375` |
| cortex | `https://github.com/abbacusgroup/cortex` | Local historical commit `a51c2209eb6d26812c19c97aaade3cb64ccfc23c` |
| pal | `https://github.com/agno-agi/pal` | Local historical commit `6516b8ede0c085e48f39f3bd04cb85b475a855dc` |
| semantic-engine | `https://github.com/Open-Research-Institute/semantic-engine` | Local historical commit `7e2481671cad01f0b4c89f2a1877d6733d7e552c` |
| memori | `https://github.com/MemoriLabs/Memori` | Normal fresh acquisition |

Academic Research Skills was omitted from batch 18 after its old exposure stop
was resolved. The [source-exposure finding](./batch-18.md#academic-research-skills-source-exposure-finding)
establishes that the cited evaluations were tracked target-native source
material, not a prior Commonplace analysis. The current rule permits attributed,
critically checked target-native evaluations. Do not sanitize the source, inject
old findings, reuse the failed run or treat that run as completed.

The four historical inputs retain the [already authorized local-source setup](./batch-18.md#four-historical-pinned-local-sources).
The script names the same read-only repositories under origin `related-systems/`.
A coordinator makes an independent clone with `--no-hardlinks --no-checkout`,
changes only the new clone's origin, checks out the exact commit and starts with
`--source-revision`. These are historical-source analyses, not current-tip claims.
All four local commit objects were verified available without fetching. No old
analysis findings are supplied to any new coordinator.

## Reconciliation of batch 18

The [reconciliation record](./batch-20-reconciliation.json) retains exact old
run definitions, inspections, failed attempts and directory/source mismatches.
Seven runs stopped at `000001-opening`, with no open attempts, no uncertain
failure and no publication effect. They did not reach acquisition or analytical
workers. Each inherited a different publication whose directory was still
unqualified:

| Stopped target | Inherited directory | Required name |
| --- | --- | --- |
| kenhuangus wiki | `lhtb` | `zli12321--lhtb` |
| nvk wiki | `pageindex` | `vectifyai--pageindex` |
| MehmetGoekce wiki | `qwenpaw` | `niceirene--qwenpaw` |
| Cortex | `self-training-llm` | `wj210--self-training-llm` |
| PAL | `stash` | `alash3al--stash` |
| Semantic Engine | `synapptic` | `appcuarium--synapptic` |
| Memori | `wuphf` | `nex-crm--wuphf` |

Opening validates the entire inherited current corpus, not just the new target.
Thus an unrelated naming mismatch prevents opening. The earlier spot check found
Self-Training-LLM in Cortex; it was not the mismatched artifact in all seven.
Current origin has no such mismatch: the opening enumerator and full validation
both accept all 175 sets. Existing unavailable-source quotation notices remain;
this is not fresh grounding for those older quotations.

The new script validates the inherited corpus **before launching**, then fixes
all nine preparations to that validated launch-time `HEAD` via `--revision`.
This prevents later integrations' temporary legacy paths from entering the batch
through a newer preparation commit. It refuses relevant origin changes during
validation. If startup instructions change, normal preparation guards still
apply; do not bypass them or substitute another revision.

ClawVault's retained batch-18 final response reports an external-storage precheck
failure before preparation; no batch-18 worktree or preparation was found. The
mount root is not writable, but `outputs/` and the worktree parent are writable.
The new script and preparation instruction check the actual required output and
worktree parents, not write permission on the mount root. Preserve the old log;
its report does not establish that a preparation command actually executed.

A bounded process scan found no matching batch-18 shell, worktree/run argument
or worktree working-directory process at observation. This is not a permanent
lock or comprehensive compliance certification. **Do not restart batch 18 or run
another coordinator for these targets concurrently.** No old run, source,
worktree, environment or failed-attempt record was repaired or discarded.

## Outputs and stops

- Logs: external `outputs/batch-20/<output-key>.output`, with adjacent `.exit` files.
- New worktrees: external `outputs/commonplace-worktrees/batch-20-<output-key>`.
- Existing outputs, worktrees and preparation records are preserved and skipped.
- A source already published in origin is skipped for reconciliation, not counted
  as newly completed. No incumbent replacement is authorized.
- A missing mount or pinned local source stops the script. A failed coordinator
  is recorded and the next independent target proceeds, as in ordinary earlier
  Bash batches. No same-target retry, old-run recovery or automatic integration.
- Process exit 0 is not an analysis verdict. Inspect each new run and audit its
  exact published bytes before changing checklist acceptance or integrating.

Other boundary/refusal/local-disposition decisions and all content or operational
holds remain outside batch 20. Batch 19 keeps its separate six-run recovery scope.

## Verification

`bash -n` passed. Ten isolated shell mock scenarios passed: nine normal launches;
continuation after a coordinator exit 42; preservation/skipping of existing
outputs, worktrees and preparation records; skipping an already-published source;
refusal of an invalid inherited corpus, dirty relevant origin or origin change
during validation; missing or mid-run lost mount; and unavailable pinned source.
Prompts were checked for nine distinct sources, Sol/medium settings, exact
external destinations, one fixed preparation revision, four independent local
clone handoffs and absence of predecessor findings. No real Pi process launched
in these tests.

`uv run pytest tests/commonplace/general tests/commonplace/tooling`: **96 passed**
under the default marker filter. This is not the complete suite or production
workflow execution. Current-corpus validation passed. All seven old prepared
inspection commands returned 0 and reported stopped runs; four real local commit
objects exist.
Those were preparation-only checks. Subsequent operator execution produced nine
internally complete publications. The completed bounded audits above establish
seven qualified positive recommendations and two holds, not exhaustive worker
compliance, target operation or causal improvement.
