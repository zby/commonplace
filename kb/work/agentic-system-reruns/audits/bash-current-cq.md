# CQ current-batch publication audit

## Disposition

**Integrate with recorded limits.** No consequential publication defect was established by this bounded audit. The synthesis already carries the incomplete independently addressed prose-criticism inventory, partial alternative-path coverage, and lack of observed operation or causal improvement evidence. Those qualifications are publication content, not repairs supplied only by this audit.

Blockers: **none**. Integration remains the coordinator's responsibility; this audit did not integrate or change accepted outputs.

## Identity and audit method

- Exact inventory target: **cq**, batch 02, run `AAS-2026-10-14-cq-8fb3dc41c334-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/cq-8fb3dc41c334`; its sibling `.preparation.json` identifies the same token, origin and command environment.
- Method/input revision: `4266dabc470929df0ff753e57fee0c55d7b87fc6`, matching worktree HEAD, preparation record and overview. Stored `run.json` pins plan SHA-256 `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd` and worker profile `pi-sol`.
- Publication: `kb/agentic-system-analyses/retained/cq/` inside that worktree.
- Frozen source: `https://github.com/mozilla-ai/cq`, SRC-1, revision `5765494a3840e5f5a7223c42101f41e85cb9d898`, under worktree `related-systems/mozilla-ai--cq/`. Source HEAD matches and `git status --short` is empty. Cutoff: `2026-10-14`.
- Auditor runtime: Pi; environment reports `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`; session `01a138f2-e0ec-75b1-8dd9-4ffb957b103b`. No delegation.

Method: legacy-led discrepancy screening followed by selective frozen-source checks, public-qualification review, exact-byte publication checks and bounded operational trace inspection. Read the overview, boundary, synthesis and all three verification results completely; inspected the reflection/reminder runtime records and selected source implementations. This was not a second analysis or exhaustive verification of every record.

## Historical comparison and consequential findings

The `systems.md` row links [the retained legacy review](../../../agent-memory-systems/reviews/cq.md). Scoped search of `kb/agent-memory-systems/`, `kb/agentic-systems/reviews/` and `reviews-archive/` found this matching review, not a moved replacement. Its source revision is `36ae42ae4b7c30628133455bde128efe91986235`, checked `2026-06-04`; the new publication reviews a different revision. Historical characterizations were discrepancy leads, not source truth. No old source revision was acquired or executed.

1. **Core coverage is preserved with stronger limits.** Both accounts cover structured summary/detail/action advice, skill-guided query/verify/feedback, five MCP operations, local persistence/fallback/drain, remote review eligibility and agent-led reflection. The new synthesis distinguishes submission permission, structural admission and retrieval eligibility rather than treating them as factual acceptance. Its absence of the legacy Commonplace comparison and borrowable-idea recommendations is not a system-coverage regression.

2. **Vectors are a supported difference, not an invented capability.** The old review found no implemented embedding read path at its pin. The new synthesis explicitly includes optional semantic retrieval. Independent inspection of frozen SRC-1 `server/backend/src/cq_server/semsearch/queries.py` confirms configured embedding calls, stored float32 vectors, vector candidate retrieval and final `(0.8 × relevance + 0.2 × (1 − normalized distance)) × confidence` ranking. Generic exception wrapping also supports the published fallback warning. This audit does not attribute the difference to a particular intervening commit or establish provider quality.

3. **Push context does not mean pushed knowledge units.** The historical review called KU retrieval pull-only but separately described a Cursor failure reminder. The new account includes automatic retained failure delivery and transport-cache reuse in its broader memory comparison. Frozen SRC-1 `cli/internal/hook/cursor.go` confirms failure-event persistence, interrupt exclusion, latest conversation-keyed state, clipped input/error, later stop output and clearing, plus session-start expiry. The synthesis and `RT-RTE-failure-reminder` explicitly deny automatic lesson admission and withhold host attention or benefit. No contradiction with requested KU querying was established.

4. **Reflection and approval remain instructions, not universal endpoint guarantees.** Frozen SRC-1 `sdk/go/prompts/reflect.md` explicitly assigns extraction to the foreground agent, requires interactive candidate decisions and near-match querying, permits explicit approval of an original hard-finding candidate, and continues after individual proposal errors. This supports the synthesis's narrowed approval/safety account rather than the legacy shorthand of user-approved reflection as a universal invariant. The public synthesis also preserves conflicting server-extraction doctrine instead of hiding it.

5. **Tier is not established confidentiality.** The legacy local/private-to-remote promotion wording could suggest stronger governance than the new account warrants. Frozen SRC-1 `server/backend/src/cq_server/repositories/_queries.py` defines approved-ID and approved-data reads by status, not ownership or tier, and review updates by ID without a pending-state predicate. These inspected SQL definitions support the public qualifications; they do not establish deployed access behavior independently.

6. **The criticism inventory gap is already public.** Report, profile and synthesis verification each retain the missing independent prose-criticism declaration in mixed feedback containers. The first synthesis Limitations row states the resulting inability to claim complete part-addressed inventories or independent admission/consumption/lifecycle comparisons. This is a bounded inventory limitation, not concealed absence of criticism or evidence that arithmetic evaluates a prose objection. No audit-only qualification is needed to make this result usable.

## Publication and operational evidence

Read-only state inspection used the run directory named above. All **12 published Markdown members** are byte-identical to the working artifact members and match the SHA-256 versions pinned by `state/attempts/000046-publish.json`. The published `ARTIFACT.yaml` matches that attempt's assembled manifest pin (`8d2fcd66aa8707273424c810f716e9203b9f7c90be7296a5b1a10666c7d415aa`). Its difference from the type-only working manifest is the assembled member hashes and worker metadata, not content drift. The publish receipt version `40b8310c01daa5a34e9b5d33fc78f115db3db1cd27aa040c60cdb67475f10f82` identifies the same destination, run and member hashes and records `published: true`.

Stored attempts show corrected runtime and epistemic outputs followed by completed report/profile/synthesis verification and publication. Those engine states alone do not prove worker compliance.

The batch output `kb/work/agentic-system-reruns/outputs/cq.output` retains nested worker messages, so worker evidence is not missing here. Bounded inspection found completed worker result envelopes for all 15 analytical attempts, including superseded/correction attempts. Matching tool-call/result IDs within each worker show `commonplace-run validate-output` results reporting content passes. For example, output JSONL line 5023 contains synthesis-verification call `call_jk8yw8TM5q2jbuawzbN5x8WB|fc_033c72a43242da52016acef717bc9c87d29677e743c3724474` and its matching pass result; line 3756 similarly retains the corrected report-verification check. These checks explicitly disclaim job acceptance and claim support. The synthesis-verification trace also shows separate bounded input reads rather than only a final completion assertion.

This inspection does **not** certify full prompt/truncation recovery, every source read, all write-authority obligations, or lack of historical exposure across every worker. Nor do analysis-worker traces supply missing CQ execution evidence. No target, test, example, provider or service was executed by this audit.

## Validation

Called the prepared worktree's command from that worktree, with its `.venv/bin` prepended to PATH, without output/state-writing options:

```text
commonplace-validate kb/agentic-system-analyses/retained/cq
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/cq
Scope: kb/agentic-system-analyses/retained/cq
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Exit status: 0. This is the command's artifact-scoped output, not a claim that it reported twelve separate file checks.

Report check, from the same prepared command environment:

```text
commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cq.md
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cq.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cq.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Exit status: 0.

## Remaining coverage limits

This audit did not independently retrace all client/store variants, duplicate-flag failures, discovery recovery, maintenance migrations or the entire feedback loop. Those findings were screened through the public synthesis and verification records, not independently certified. The selected historical discrepancies have supported dispositions; broader investigation is not needed for this bounded integration recommendation. Actual CQ host compliance, reliable factual acceptance, private-tier confidentiality, faithful transfer and learning benefit remain unestablished as the publication states.
