# Batch 23: eight fresh source-first restarts

**Prepare new analyses for the eight remaining targets that need no new source,
scope or operational-incident decision.** The operator requested this batch on
2026-10-19 after the eight cleared batch-21/22 publications were integrated.
This preparation launches nothing. Completion means separately audited,
integrated publications or an explicit later disposition, not eight process exits.

## Selection

| Target | Exact source | Reason for a fresh attempt |
| --- | --- | --- |
| JAZ | `https://github.com/jaz-lang/JAZ` | Batch-21 preparation refused; no fresh analysis started |
| Autogenesis | `https://github.com/DVampire/Autogenesis` | Batch-21 preparation refused; no fresh analysis started |
| LLM Wiki — MehmetGoekce | `https://github.com/MehmetGoekce/llm-wiki` | Batch-21 preparation refused; no fresh analysis started |
| ClawVault | `https://github.com/Versatly/clawvault` | Batch-21 preparation refused; no fresh analysis started |
| AREX-Skill | `https://github.com/VectorSpaceLab/AREX-Skill` | Batch-21 preparation refused; no fresh analysis started |
| ContextPilot | `https://github.com/Tencent/ContextPilot` | Predecessor stopped on an analytical input defect |
| OpenRSI | `https://github.com/FrontisAI/OpenRSI` | Predecessor interrupted during reconciliation |
| Supermemory | `https://github.com/supermemoryai/supermemory` | Held publication; retry under improved general instructions |

The [remainder reconciliation](./batch21-22-remainder.md) supplies selection
evidence, not worker inputs. Supermemory and ContextPilot may reproduce their
errors; fresh execution is not proof of repair. The generic instruction change
`83cb60e46` strengthens control-path checking and qualification preservation.
No audit finding, source locator for a known defect, expected verdict or old
correction packet enters these fresh analyst contexts.

## Execution

The [launcher](./bash-23.sh) starts one Pi session per target, sequentially,
using `openai/gpt-6.1-sol`, medium effort, and analytical/verification profile
`pi-sol`. It pins all eight preparations to the checkout's committed HEAD at
script startup. Commit this preparation before execution; method/startup files
must match that revision. Do not edit those files during the batch. Unrelated
dirty files are excluded by native preparation, not copied into fresh worktrees.

After confirming no other batch is working on these targets, run:

```bash
bash kb/work/agentic-system-reruns/bash-23.sh
```

Logs go under external `outputs/batch-23/`; worktrees use external
`outputs/commonplace-worktrees/batch-23-<key>`, with sibling preparation records.
An existing destination selects a new `-retry-N` key for both logs and worktree;
it never overwrites or resumes evidence. A later invocation attempts all eight
again, including any that have since completed. Run only one instance, and
inspect outcomes before invoking again. Do not launch old batches concurrently.

Acquire each exact repository remotely at its default-branch tip, then freeze
that commit through the ordinary analysis workflow. Preserve supplied identities;
never substitute similarly named repositories. Existing source revisions remain
historical evidence, not pins for the new run. The native skill's worker-launch
preflight, source isolation, ownership and failure stops still apply. No target
code execution or dependency installation is authorized by this batch.

Each coordinator stops on preparation or acquisition failure. The outer script
continues with independent targets and records process exits; Pi may return zero
while reporting such a failure. Inspect final coordinator messages and native
run/publication state, not exit codes or file presence alone. If a common
preflight failure recurs, stop the outer batch and resolve it before creating
more attempts. No automatic same-run retry or repair is commissioned.

## Exclusions and preserved state

Nine of the 17 unchecked inventory targets remain outside this batch:

- **ACE, Fragility Grid and Sift-KG:** operational-incident holds need explicit
  disposition; another fresh run does not clear collateral uncertainty.
- **Operational Ontology Framework:** conceptual-scope acceptance or implemented
  source/boundary selection remains open.
- **Awesome Agent Memory and Letta:** source/boundary selection or exclusion
  remains open after their local stops.
- **DualGraph and Fintool:** retain their operator deferrals.
- **Agentic Harness Engineering:** retains its separate technical gate.

Do not resume, reset, withdraw, modify or clean predecessor runs, publications,
sources, logs, preparation records or incident evidence. No audit, integration,
checklist acceptance, comparisons, transfer scan, landscape refresh, cleanup or
push is included. Preserve native stops for later review rather than force a
publication. After execution, audit exact new publication bytes separately and
reconcile all eight outcomes before selecting another batch.

Preparation changes no completion counts: **190 canonical sets / 2,470 members;
189 complete inventory targets, 14 pending and three older target holds**.
For optional broader relationship discovery on this preparation, use
`cp-skill-connect`; it is not an execution prerequisite.
