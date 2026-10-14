# ExpeL current-batch publication audit

## Decision

**Disposition: integrate with recorded limits.** No integration blocker was established within this bounded audit. The publication retains the central experience-to-guidance mechanisms and makes the consequential qualifications visible in its synthesis. Its `complete` disposition is analysis completion, not successful execution of ExpeL or demonstrated improvement.

## Identity and method

- Exact inventory row: ExpeL, batch 04, `AAS-2026-10-14-expel-efd908f05069-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/expel-efd908f05069`.
- Publication: `kb/agentic-system-analyses/retained/expel/` in that worktree.
- Method commit: `4266dabc470929df0ff753e57fee0c55d7b87fc6`, matching preparation and worktree HEAD. The stored run plan SHA-256, `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`, matches the worktree plan.
- Frozen source: `https://github.com/LeapLabTHU/ExpeL`, commit `e41ec9a24823e7b560c561ab191441b56d9bcefc`, at `related-systems/LeapLabTHU--ExpeL` in the prepared worktree. Acquisition effect, boundary, overview and synthesis agree; inspected source HEAD and remote match, with empty Git porcelain status. SRC-1 is the only registered source. External providers, dependency internals, simulators, WebShop service, live Wikipedia and the separately linked paper are outside this evidence boundary.
- Auditor runtime: Pi, `openai/gpt-6.1-sol`, medium reasoning, confirmed by `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`; session `01a138fd-9b60-7601-99c5-84ec8c3fb920`. No delegation.

Method: compare the complete legacy review with the overview, synthesis and three verification reports; inspect correction history and selected runtime/reconciliation passages; check consequential differences directly in frozen source; check publication hashes and stored attempts; sample paired nested worker actions in the retained outer process log. This is not a second analysis or exhaustive compliance audit.

## Historical comparison and source checks

The checklist links `kb/agent-memory-systems/reviews/expel.md`. Searches within `kb/agent-memory-systems/` found that exact review and secondary survey mentions. The retained review is dated 2026-06-04 and names the **same source commit** as this run, so revision drift does not explain the differences. No moved historical account was needed. Historical interpretation and Commonplace borrowing recommendations were comparison leads, not source evidence.

1. **Core coverage is preserved.** Both accounts cover separately invoked training, extraction and evaluation, retained trajectories/reflections, counted rules, automatic rule insertion, prompt-time trajectory retrieval and local file/pickle persistence. The new synthesis adds the reflection-to-retry chain explicitly and separates implemented feedback from observed learning efficacy. Omitting legacy Commonplace adoption suggestions is not a system-coverage regression.
2. **Held-out isolation is more accurately bounded.** The legacy introductory held-out-task framing is too broad if read as isolation of every evidence input. Frozen `agent/expel.py:329–381` distinguishes compare lookup through `idx2task`, success selection through dictionary enumeration position, and resumed reuse of saved groups. `agent/expel.py:423–572` builds retrieval from the full success-history pool and static examples, excludes the current task, and selects the shortest task-associated trajectory by character length. These checks support the synthesis's separate extraction alignment condition and broader retrieval pool; neither establishes actual leakage. The original report-verification version retained at `state/versions/248dd96d2360a8664086eb8ef7faec5e2700d5d13659dae4414d3c3fa9a055f0` demanded correction. The accepted runtime and public synthesis carry it. The remaining stale epistemic characterization is explicitly explained in reconciliation, accepted report verification and synthesis limitations, not concealed as an unsettled mechanism conflict.
3. **Legacy caveats are retained rather than lost.** FEVER's incomplete reflection/critique dispatch is concrete in frozen `prompts/__init__.py`: `None` reflection inputs, `None` compare instruction and misspelled `all_success_existing_riles`. The new synthesis withholds uniformly functioning benchmark integrations. It also preserves the legacy soft rule-count limit, copied cache lineage, rebuilt FAISS access store, local rather than global context budgets, and absence of item-level causal uptake evidence.
4. **Reporting gets a necessary new qualification.** Frozen `utils.py:277–321` counts WebShop score-marker text as success; `envs/webshop/webshop.py:210–226` requires numerical reward equal to one. Public synthesis limitations and both relevant verifications withhold quantitative equivalence without asserting observed aggregate error.
5. **The profile omission is already public.** Profile verification identifies an omitted separate authority classification for failed-trial input at reflection generation. Its inventory remains partial; the synthesis limitations explicitly prevent a complete per-update-consumer comparison. This does not erase the separately retained reflection chain or invalidate the supported extraction-consumer finding.

## Publication and operational evidence

The run directory is `kb/agentic-system-analyses/state/AAS-2026-10-14-expel-efd908f05069-01/` in the worktree. All 43 stored attempts report completed; the acquisition and publication effects report completed. The publication's exact 13-file inventory and all 13 SHA-256 hashes match `effects/publish.json`. All twelve Markdown members equal the run's working artifact bytes. Only `ARTIFACT.yaml` differs: publication adds the member hashes and worker identity to the working type-only manifest. That is not content drift. Manifest and model-attempt identity reports name `openai/gpt-6.1-sol`, medium, under `pi-sol`.

Worker evidence is available in `kb/work/agentic-system-reruns/outputs/expel.output`, not as standalone trace files in the run. Its nested tool-result records contain all fourteen model-attempt worker results, including the runtime repair and repeated reconciliation/report verification. A call-ID/result-ID inventory found no unpaired calls in those worker messages and exit code zero for each result. This is execution evidence beyond engine acceptance, not proof of every worker obligation.

The bounded deeper sample is final report verification `000032`, outer JSONL line 3334: 61 paired reads, three paired Bash calls and two paired writes. Successful paired reads include the frozen three drivers, all three acting/reflection/ExpeL classes, prompt dispatch and maintenance templates, and persistence/reporting bodies. For example, `call_V1QBYORydAisRtDgATAcbxFq|fc_0132da965db6a73b016aceeee1d7d487d280a0f02a5db02521` reads frozen `train.py`; its matched result is not marked error. This supports actual source access behind the verifier's claims. It does not certify complete comprehension, every truncation recovery, all prohibited-read boundaries or all worker output validation. No separate trace evidence is invented where absent.

## Validation and audit limits

Used the prepared worktree's `.venv/bin/commonplace-validate`, from that worktree, without state-writing inspect/advance commands or `--output`.

Publication command: `.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/expel`.

```text
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/expel
Scope: kb/agentic-system-analyses/retained/expel
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

This is directory-artifact validation, not a claim that thirteen independent text files were counted or semantically certified.

Report command: `.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-expel.md`.

```text
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-expel.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-expel.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

No ExpeL code, tests, services or model calls were run. Dataset contents, every retrieval strategy, dependency compatibility and comprehensive worker compliance were not re-audited. No generated ExpeL rule/checkpoint corpus or controlled experiment was supplied; operation, content warrant, successful delivery and causal benefit remain unobserved as the publication states. Only this audit report was written; no integration, cleanup, commit, source acquisition or shared bookkeeping was performed.

## Blockers

None established within the inspected scope. Preserve the publication's stated limits on integration. Any stronger claim of functioning FEVER support, complete authority inventory, unconditional holdout, exercised improvement or calibrated WebShop reporting requires the resolving evidence or changes named in the public synthesis; this audit grants no such claim.
