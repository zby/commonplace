# Batches 21–22 observed outcomes

This is current observation, not a launch/recovery instruction. Exact hashes and native inspection output: [intake](./batch21-22-intake.json). All 30 process logs, including the first and retry attempts, are retained in the [log ledger](./batch21-22-log-outcomes.json). No conclusion below is inferred from process exit.

## Run outcomes

| Prepared worktree | Run | Native state / completion | Exact own publication |
| --- | --- | --- | --- |
| `batch-21-fresh-contextpilot` | `AAS-2026-10-18-contextpilot-1394d2080dc8-01` | stopped / not completed; failed 000009-workflow | none |
| `batch-21-fresh-modularrsi` | `AAS-2026-10-18-modularrsi-4218ceff5530-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-21-fresh-openrsi` | `AAS-2026-10-18-openrsi-29674d2f0830-01` | running / not completed; open 000019-reconciliation | none |
| `batch-21-fresh-supermemory` | `AAS-2026-10-18-supermemory-75d21b14316b-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-ace` | `AAS-2026-10-18-ace-007571102a54-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-agent-skills-for-context-engineering` | `AAS-2026-10-19-agent-skills-for-context-engineering-7e663338370b-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-ai-context-os-retry-1` | `AAS-2026-10-18-ai-context-os-82777c0c3926-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-awesome-agent-memory-retry-1` | `AAS-2026-10-18-awesome-agent-memory-8e0e01c02b3a-01` | completed / local / out-of-scope | none |
| `batch-22-fragility-grid` | `AAS-2026-10-18-fragility-grid-38b12f71fceb-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-letta-retry-1` | `AAS-2026-10-18-letta-527f0244ee20-01` | completed / local / blocked | none |
| `batch-22-llm-wiki-v3-retry-1` | `AAS-2026-10-18-llm-wiki-v3-0c553a3118eb-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-llmwiki-marimo-retry-1` | `AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-nams-retry-1` | `AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-operational-ontology-framework-retry-1` | `AAS-2026-10-18-operational-ontology-framework-2b5d9616baa4-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-secure-llm-wiki` | `AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-sift-kg` | `AAS-2026-10-18-sift-kg-e56bce0de992-01` | completed / publication-job-completed / complete | 13 members match completed effect |
| `batch-22-siftly-retry-1` | `AAS-2026-10-18-siftly-b81c94cf0f77-01` | completed / publication-job-completed / complete | 13 members match completed effect |

## Every process attempt

| Batch / log key | Exit marker | Established outcome |
| --- | --- | --- |
| batch-21 / `arex-skill` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-21 / `autogenesis` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-21 / `clawvault` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-21 / `contextpilot` | 0 | failed workflow input defect |
| batch-21 / `jaz` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-21 / `mehmetgoekce--llm-wiki` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-21 / `modularrsi` | 0 | published, byte-bound; audit separate |
| batch-21 / `openrsi` | absent | interrupted with reconciliation open; engine still running |
| batch-21 / `supermemory` | 0 | published, byte-bound; audit separate |
| batch-22 / `ace` | 0 | published, byte-bound; audit separate |
| batch-22 / `agent-skills-for-context-engineering` | 0 | published, byte-bound; audit separate |
| batch-22 / `ai-context-os-retry-1` | 0 | published, byte-bound; audit separate |
| batch-22 / `ai-context-os` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-22 / `awesome-agent-memory-retry-1` | 0 | completed local out-of-scope |
| batch-22 / `awesome-agent-memory` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-22 / `fragility-grid` | 0 | published, byte-bound; audit separate |
| batch-22 / `letta-retry-1` | 0 | completed local blocked |
| batch-22 / `letta` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-22 / `llm-wiki-v3-retry-1` | 0 | published, byte-bound; audit separate |
| batch-22 / `llm-wiki-v3` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-22 / `llmwiki-marimo-retry-1` | 0 | published, byte-bound; audit separate |
| batch-22 / `llmwiki-marimo` | absent | interrupted before any settled tool execution; no worktree/preparation/run found |
| batch-22 / `nams-retry-1` | 0 | published, byte-bound; audit separate |
| batch-22 / `nams` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-22 / `operational-ontology-framework-retry-1` | 0 | published, byte-bound; audit separate |
| batch-22 / `operational-ontology-framework` | 0 | preparation refused startup mismatch; no worktree/preparation/run found |
| batch-22 / `secure-llm-wiki` | 0 | published, byte-bound; audit separate |
| batch-22 / `sift-kg` | 0 | published, byte-bound; audit separate |
| batch-22 / `siftly-retry-1` | 0 | published, byte-bound; audit separate |
| batch-22 / `siftly` | absent | interrupted before any settled tool execution; no worktree/preparation/run found |

## Meaning and limits

Batch 21 has **2 exact publications, 1 failed run, 1 interrupted run and 5 preparation refusals** across its nine targets. Batch 22 has **11 exact publications and 2 completed local results** across its thirteen targets; its eight earlier attempts are separately retained (six preparation refusals and two interruptions before a settled tool execution). In total: **30 process logs; 17 prepared runs; 13 publications / 169 members; 2 local completions; 1 failed run; 1 interrupted open run; 11 preparation refusals; 2 pre-preparation interruptions**. All 27 existing process exit markers say zero; the three missing markers are OpenRSI and the initial llmwiki-marimo/Siftly attempts. Zero was not publication success.

ContextPilot currently stops at failed `000009-workflow`: its supplied runtime conflates logger-export final-answer fallback with a different extraction method. OpenRSI currently retains open `000019-reconciliation`; no publication effect or matching retained set for this run exists. No resume/advance was attempted.

Awesome Agent Memory completed locally as `out-of-scope` at `07775180db1466826fda610af83d932c58d944eb`: the acquired repository is a catalog, not an operational memory system. Letta completed locally as `blocked` at `5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a`: the frozen source is a landing page; current implementation points elsewhere and archive is historical. Neither is a published result or an approved target exclusion. Both require an operator source/boundary decision, not another blind default-tip run.

The eleven preparation refusals name startup mismatches in `synthesize-analysis.md`, `trace-runtime.md`, `verify-reports.md` and `verify-synthesis.md` at selected method `b12b855f4224ee847eaec5f269188b02ac532ccc`. Origin now contains committed instruction improvements `83cb60e460a55b57bd69600c86d58f50b8c316db`; this does not change any frozen run or authorize retry. Five batch-21 targets (JAZ, Autogenesis, MehmetGoekce LLM Wiki, ClawVault, AREX-Skill) never reached a fresh worktree in this batch. Old held publications remain preserved; they are not successful new attempts.

The reused [Supermemory report](./audits/batch-21-supermemory-75d21b14316b.md) was read completely. Intake independently matches run/token, completed effect SHA-256 `00c1acc1966cb5fcef240bfa3157f8443870f87c05dd679e3e32e8873b5a0bd6` and 13-member digest `e53f36c7a16e31bed03dfacba6b593f173dfe65861632df8793ec387b8918a3d`. Its capture-qualification **hold** is reused without a redundant audit.

All discovered current batch worktrees have exactly one own run. Intake recursively hashes run state/effect/trace/version bytes and all publication members, not inherited retained copies. The [remainder intake](./batch21-22-remainder-intake.json) additionally inventories all 25 unchecked targets across registered and baseline worktrees, preserving older attempt maps and publication bindings. Read-only inspection may acquire an existing run lock; it does not recover or advance runs.

Interactive coordinator and auditor Pi processes exist. [Writer observation](./batch21-22-writers.json) found no batch analysis process or relevant open batch log descriptor; this is an observation, not future writer clearance or termination permission. Integration requires a fresh check after all audit writers finish.
