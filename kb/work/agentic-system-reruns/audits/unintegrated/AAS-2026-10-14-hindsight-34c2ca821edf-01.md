# Hindsight exact-publication audit

Disposition: **integrate with recorded limits**. No consequential defect established
in this bounded inspection; the relevant qualifications already appear publicly.
Blockers: none. This is readiness advice, not integration authorization.

## Identity and boundary

- Run: `AAS-2026-10-14-hindsight-34c2ca821edf-01`.
- Method/worktree HEAD: `f7732e9c6bc5622031571d2d429bc017253eb64f` (inventory).
- Auditor: `audit-hindsight`, independent Pi / `gpt-6.1-sol`;
  session `01a13b06-785b-7553-bfeb-8ee88864ce52`.
- W: `/home/zby/llm/commonplace/.commonplace/worktrees/hindsight-34c2ca821edf`.
- P: `W/kb/agentic-system-analyses/retained/hindsight`.
- R: `W/kb/agentic-system-analyses/state/` followed by the exact run ID.
- Source S: `W/related-systems/vectorize-io--hindsight`, identity
  `https://github.com/vectorize-io/hindsight`, frozen revision
  `610c135b6f2d0d8b972da94146ae635943f36271`.
  Read-only Git check confirmed that HEAD and a clean source working tree.
- Historical lead: `kb/agent-memory-systems/reviews/hindsight.md`, reviewed
  `7683f29004ab9d88e0ef3f0f18b8ffe6fc741905`, dated 2026-06-04.
  It remains a historical review; this new account is outside that collection,
  in `agentic-system-analyses/retained`. No integrated incumbent is listed.

## Method and consequential findings

Compared historical coverage with P's complete overview, synthesis, boundary and
report verification. Challenged three differences against S, not historical truth.
No new analysis, acquisition, target execution or output repair was undertaken.

1. **Integration-dependent delivery is retained, not generalized.** The historical
   review names LangGraph alongside hooks. P's canonical inventory omits its
   context lifecycle, but `synthesis.md#limitations` explicitly records that loss
   and withholds cross-integration equivalence. Static inspection of
   `S/hindsight-integrations/langgraph/hindsight_langgraph/nodes.py:114–257`
   confirms stable-ID system-message/custom-state delivery, prior-message removal
   on named no-memory branches, and latest enabled human/AI retention selection.
   This is a disclosed coverage limit, not evidence of observed graph operation.
2. **Hook progress is not ingestion success.**
   `S/hindsight-integrations/claude-code/scripts/retain.py:120–252` selects a
   sliding window or unretained suffix, commits progress on empty formatted
   content, and otherwise commits after `client.retain` returns. The synthesis
   states these qualifications and separately discloses the missing fine-grained
   progress-state inventory. Its automatic trace-fed path is an implementation
   claim, not an observed successful retention/host-reliance claim.
3. **Budgeted recall is not a hard ceiling.** The older account emphasizes token
   limits. `S/hindsight-api-slim/hindsight_api/engine/fact_budget.py:43–88`
   implements a positive-budget first-resolvable-fact floor that can overshoot.
   The new synthesis expressly states this countercase and separates lineage IDs
   from readable justification. No missing public budget qualification found.

The old platform breadth (transfer, embedded modes, other integrations and
operational stores) is not comprehensively reproduced. The boundary and synthesis
already disclose incomplete alternate-path coverage. Neither target operation,
truth acceptance, causal benefit nor whole-system parity is certified publicly.
Those explicit limits justify accepting a partial-loop account, not completeness.

## Publication and operational evidence

Read-only SHA-256 comparison of every actual file under P against
`R/effects/publish.json:new` matched the entire 13-file set, with no extras.
Manifest: `3e9e67f75bff2a28a6ffc32ceb894615058008641f960da1e24bc9d70fb38579`.
`R/state/attempts/000033-publish.json` is completed and pins that manifest.

Trace T: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/hindsight.output`.
T JSONL line 2428 contains the completed report-verifier worker result, model
`gpt-6.1-sol`, thinking `medium`, exit 0. Within that same worker's `messages`
(zero-based), call/result 65/66 (`call_cp5cjfLrxLccinmf51PBtUzP…`) actually reads
LangGraph nodes 114 onward; 55/58 reads the fact-budget module. These are executed
inspection, not proposals or copied verification prose. Pair 92/93 executes
`commonplace-run validate-output` on that worker's prompt and returns:
“Member content check passes; invocation residue not checked. This is not job
acceptance or claim support.” Publication acceptance alone would not prove this.
This sample does not certify every worker obligation or exhaustive compliance.

## Validation and remaining limits

From W, `.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/hindsight`
returned `VALIDATION SUCCESS`: 1 directory artifact, 0 failures, 0 warnings.
The `--full` invocation returned `Overall: PASS (clean)`, checked all 12 Markdown
members plus directory requirements, roles and relations; no excluded subtrees.
The same validator from W, targeting this report's absolute origin path, returned
`VALIDATION SUCCESS`: 1 text file, 0 failures, 0 warnings.
No pytest or target tests were run.

This audit is discrepancy-led, not a semantic recheck of every declaration. It
samples one verifier's operations, not all nested worker histories. Static source
wiring is not observed use, faithful model output or a causal improvement result.
Any future claim of exhaustive integration coverage needs separate inspection;
it is not a prerequisite for integrating this explicitly bounded publication.
