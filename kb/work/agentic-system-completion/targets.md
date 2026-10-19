# Sixteen unresolved analysis targets

**All sixteen remain unresolved at handoff on 2026-10-19.** This list carries
recorded decisions from the rerun campaign; it does not independently re-audit
source claims, clear incidents or authorize execution. The [workshop framing](./README.md)
governs later work. Start with the [local evidence index](./evidence/README.md)
for copied audit/incident records, selected intake bindings and 17 exact
publication captures. Historical `H/` locators below retain their original
meaning; the evidence manifest maps copied records to their local paths.

## Five publication-content holds

These are the exact batch-23 runs. Their common method-commit is
`3e2491c83a4613d410511af8c3cfde30f4b67689`. Audit findings are review evidence,
not instructions to fresh source-first analysts.

| Target key | Source identity | run-id | Recorded blocker / next decision |
| --- | --- | --- | --- |
| `jaz` | `https://github.com/jaz-lang/JAZ` | `AAS-2026-10-19-jaz-9d991c410bb9-01` | Replay omits sequential-nesting and queue/divergence qualifications; input-origin completeness is overstated. Decide the general method improvement and authorized next evaluation. |
| `autogenesis` | `https://github.com/DVampire/Autogenesis` | `AAS-2026-10-19-autogenesis-05936a4e4c3b-01` | Public account omits the startup consequence of missing local `tool.other`. Decide the general method improvement and authorized next evaluation; do not run target code to settle it without authority. |
| `arex-skill` | `https://github.com/VectorSpaceLab/AREX-Skill` | `AAS-2026-10-19-arex-skill-089a5ed7476f-01` | Reflection assessment does not distinguish the installed-library-state witness. Decide the general assessment/instruction improvement; no exercised self-improvement is established by this finding. |
| `contextpilot` | `https://github.com/Tencent/ContextPilot` | `AAS-2026-10-19-contextpilot-0826e2df5b2f-01` | Training selector prerequisite and generic fallback omitted; actual dataset selection unknown. Decide the general method improvement and authorized next evaluation. Older target hold remains. |
| `openrsi` | `https://github.com/FrontisAI/OpenRSI` | `AAS-2026-10-19-openrsi-4f870183cadd-01` | Default shared mount permits candidate reads of nominally private answers; actual leakage not established. Decide the general method improvement and authorized next evaluation. |

Worktree for each: `E/commonplace-worktrees/batch-23-<key>`.
Log: `E/batch-23/<key>.output`.
Historical exact audits: `H/audits/batch-23-<key>.md`.
Frozen identities and member/source/run maps: `H/batch-23-audit-intake.json`.
Parent decisions: `H/batch-23-audit-review.md` and `H/batch-23-audit-decisions.json`.

## Two timeout stops without publication

| Target key | Source identity | run-id | Recorded blocker / next decision |
| --- | --- | --- | --- |
| `mehmetgoekce--llm-wiki` | `https://github.com/MehmetGoekce/llm-wiki` | `AAS-2026-10-19-llm-wiki-ffa8c1bd1d63-01` | Final advance timed out after 120 seconds. Assembly completed; no publication effect recorded. Authorize bounded diagnosis and supported recovery or a fresh attempt only after checking ownership and uncertain effects. |
| `clawvault` | `https://github.com/Versatly/clawvault` | `AAS-2026-10-19-clawvault-c4e23c553266-01` | First advance timed out after 120 seconds during acquisition; no recorded attempts/effects. Acquisition unconfirmed. Authorize bounded diagnosis before choosing recovery or fresh acquisition. |

Worktrees and logs use the same batch-23 path convention above. Both preparations
record the batch-23 method commit above. Evidence: `H/batch-23-tally.md` and
external logs. Outer process exit zero did not establish completion.

## Three operational-incident holds

| Target key | Source identity | run-id | Recorded blocker / next decision |
| --- | --- | --- | --- |
| `ace` | `https://github.com/ace-agent/ace` | `AAS-2026-10-18-ace-007571102a54-01` | Verified unauthorized temporary-file write/removal; prior contents and collateral effects unknown. Explicit operator incident disposition required; old target hold also remains. |
| `fragility-grid` | `https://github.com/NikolaTesla-007/fragility-grid` | `AAS-2026-10-18-fragility-grid-38b12f71fceb-01` | Verified sibling-file write and ancestor cleanup attempt, with unresolved collateral history. Explicit operator incident disposition required. |
| `sift-kg` | `https://github.com/juanceresa/sift-kg` | `AAS-2026-10-18-sift-kg-e56bce0de992-01` | Verified new sibling-file write/removal and ancestor cleanup; older collateral incident remains separate. Explicit operator incident disposition required. |

Worktree: `E/commonplace-worktrees/batch-22-<key>`.
Log: `E/batch-22/<key>.output`.
Exact reports: `H/audits/batch21-22-batch-22-<key>.md`.
Evidence maps/review: `H/batch21-22-intake.json`,
`H/batch21-22-parent-review.json` and `H/batch21-22-decisions.json`.
A fresh positive content audit cannot itself dispose of these incidents.

## Three source/scope decisions

| Target key | Supplied source identity | run-id | Recorded blocker / next decision |
| --- | --- | --- | --- |
| `operational-ontology-framework` | `https://github.com/fstech-digital/operational-ontology-framework` | `AAS-2026-10-18-operational-ontology-framework-2b5d9616baa4-01` | Conceptual publication received a positive content audit, but the implementation-source/scope gate was not waived. Obtain conceptual-scope acceptance or select a suitable implemented boundary/source. |
| `awesome-agent-memory` | `https://github.com/TeleAI-UAGI/Awesome-Agent-Memory` | `AAS-2026-10-18-awesome-agent-memory-8e0e01c02b3a-01` | Local `out-of-scope` catalog result, not publication or approved exclusion. Select a suitable source/boundary or obtain explicit exclusion. |
| `letta` | `https://github.com/letta-ai/letta` | `AAS-2026-10-18-letta-527f0244ee20-01` | Local `blocked` landing-page result, not publication. Select implementation source/boundary or obtain explicit scope/exclusion decision. |

Worktree: `E/commonplace-worktrees/batch-22-<key>-retry-1`.
Log: `E/batch-22/<key>-retry-1.output`.
Evidence: `H/batch21-22-outcomes.md`, `H/batch21-22-remainder.json` and
`H/batch21-22-remainder-intake.json`. Ontology additionally has
`H/batch21-22-ontology-scope-stop.md` and
`H/audits/batch21-22-batch-22-operational-ontology-framework-retry-1.md`.
Do not substitute a repository based only on a similar name.

## Two operator deferrals and one technical gate

| Target key | Supplied source identity | run-id | Recorded blocker / next decision |
| --- | --- | --- | --- |
| `dualgraph` | `https://github.com/microsoft/DKI_LLM` | `AAS-2026-10-14-dki-llm-da75a840ca8d-01` | Deferred pending intended system/boundary selection; no silent subproject substitution. Worktree: `L/dki-llm-da75a840ca8d`. |
| `fintool` | `https://x.com/nicbstme/status/2015174818497437834` | `AAS-2026-10-14-2015174818497437834-e109159e0559-01` | Deferred article-only/source-exposure decision. Preserve original capture and source identity; authorize the scope and fresh unexposed context before another analysis. Worktree: `L/fintool-e109159e0559`. |
| `agentic-harness-engineering` | `https://github.com/china-qijizhifeng/agentic-harness-engineering` | `AAS-2026-10-13-agentic-harness-engineering-914fd0094689-01` | Retained memory-profile refusal and stopped run, no publication. Decide supported refusal/contract disposition and recovery; no blind retry. Worktree: `L/agentic-harness-engineering-914fd0094689`. Older target hold remains. |

Evidence: `H/batch21-22-remainder.md`, `H/batch21-22-remainder.json` and
`H/batch21-22-remainder-intake.json`. The full historical inventory and earlier
run references remain in `H/systems.md`; it is not the current working list.

## Evidence retrieval after predecessor closure

The following prefixes are locators, not assurances of availability or authority:

- `E` = `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs`.
- `L` = `/home/zby/llm/commonplace/.commonplace/worktrees`.
- `H` = historical repository path `kb/work/agentic-system-reruns` at exact Git
  snapshot `defc4efaeeae631cff2a6f3f2370603df504b3ff`.

The snapshot fixes these records before the successor workshop's opening. It is
an evidence retrieval revision, not a method revision for future runs. Read a
historical record without restoring old files into the working tree:

```bash
git show defc4efaeeae631cff2a6f3f2370603df504b3ff:kb/work/agentic-system-reruns/batch-23-audit-results.md
```

Substitute the listed repository-relative historical path for another record.
The listed files must remain in reachable Git history if the old workshop is
deleted. If an exact report is later promoted to durable retention, add that
locator without changing the historical snapshot identity.

Within each worktree, the run is `kb/agentic-system-analyses/state/<run-id>`;
the sibling `<worktree>.preparation.json` records the original worktree, method
and command prefix. Never guess the runtime command environment from this
handoff: verify the preparation and native binding before an authorized effect.
Full source-revision and hash maps for audits are in the historical intakes;
recheck them against actual evidence, not only the summarized finding.

Opening this handoff did not alter external evidence. A subsequent authorized
transfer copied exact publication bytes into `evidence/publications/` after
checking their recorded membership/hashes, and copied relevant audit/incident
records. Original external logs, sources, worktrees and publications remain
unchanged. No raw trace archive was duplicated or reverified. The
five content holds + two timeout stops + three incident holds + three source/scope
stops + two deferrals + one technical gate total **16**.
