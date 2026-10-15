---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Claude Code dynamic workflows: the documented deep-research request, cross-checking, recovery and report-delivery workflow."
run-id: AAS-2026-10-14-workflows-f9c2f80a3a94-01
reviewed-boundary: "workflows-2026-10-14"
---

# Claude Code dynamic workflows workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the bundled `/deep-research <question>` command. It is selected because the frozen page supplies a connected request-to-report procedure and a consequential distinction between rejected claims and claims that could not be checked. This is stronger workflow evidence than the page's example requests for migrations or adversarial audits, which do not supply the corresponding complete scripts. The account concerns documented coordination, not a successful research run. The entire SRC-1 capture was inspected; the bundled script, exact worker prompts, voting thresholds and execution traces are outside the [boundary](boundary.md). No research quality or reliability improvement is established.

The underlying mechanisms already have runtime identities: [RT-CLM-research-report](runtime.md#rt-clm-research-report), [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch), [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration), [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery) and [RT-RTE-run-replay](runtime.md#rt-rte-run-replay). This member adds workflow-specific interpretation through annotations rather than redeclaring those referents.

### Request and launch handoff

The human supplies a question with `/deep-research`; the command runs only when explicitly invoked and requires WebSearch availability. Claude Code launches the bundled orchestration through the Workflow permission path. Unlike a new task-specific workflow, this route selects existing orchestration rather than establishing that Claude authors a fresh script. In the manual CLI case the operator sees planned phases, can inspect or edit the script, and can approve or cancel. Approval can persist for the named workflow in that project. Auto, bypass and noninteractive cases do not provide the same per-run human veto; these alternatives are retained in [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch). Launch permission admits execution, not the truth of any eventual claim (SRC-1, `Run a bundled workflow`, `Bundled workflows`, `Approve the plan before it runs`).

### Research handoffs and next-step ownership

The documented progression is question → searches across several angles → fetching and cross-checking found sources → claim voting → synthesis of a cited report. This is one bundled workflow's stated progression, not a sequence constructed by joining unrelated capabilities (SRC-1, `Run the workflow`, `Bundled workflows`).

> Run `/deep-research` with a question you want investigated. It fans out web searches across several angles, fetches and cross-checks the sources it finds, and synthesizes a cited report.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

The script owns orchestration order and branching; model-backed workers perform research and assessment through their tools. The runtime executes the script in the background, retaining intermediate values outside the foreground conversation and returning its final answer to that conversation. These responsibilities are documented in [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) and [RT-BAP-script-control](runtime.md#rt-bap-script-control). They do not establish the actual research script's number of agents, exact concurrency pattern, or whether separate agents perform fetching and synthesis.

The page establishes the question as input, found sources as material for cross-checking, and claims as the units voted on and filtered. It does not expose the payload passed at each handoff: full source text versus extracts, citation identifiers, verifier context, or synthesis instructions. Consequently, neither complete evidence delivery to verifiers nor independent assessment by them is established. The separate small audit script illustrates API usage, but cannot fill these gaps in the research workflow (SRC-1, `Bundled workflows`, `What the saved script looks like`).

### Verification and rejection

Claim cross-checking and voting precede reporting. Claims that do not survive cross-checking are filtered out. A verifier unable to check a claim because of a rate limit or API error instead produces an unverified classification that remains visible in the report. The latter is a bounded failure path: operational inability is not counted as refutation. [RT-CLM-research-report](runtime.md#rt-clm-research-report) retains the supporting passage (SRC-1, `Read the report`, `Bundled workflows`).

The report's claim-selection mechanism is therefore distinct from launch permission. Research workers contribute findings and verifier judgments; the bundled workflow consumes their assessments to produce the filtered report. The page does not locate the final accept/reject rule in a specific worker or code expression. It also does not establish voting quorum, disagreement resolution, an independent expected-answer oracle, or what warrants an unverified claim's inclusion. Filtering and citations are declared safeguards, not a guarantee of factual correctness. No human approval of every surviving claim is stated in the supplied research procedure.

### Monitoring and recovery

While the research runs, the operator can inspect phase counts, worker prompts, recent tool calls and results through `/workflows`. Expanded details show full prompts and results, but only the beginning of each listed tool result. This is monitoring rather than evidence that the operator sees the full source material. The operator can pause/resume, restart a running agent or stop an agent or the whole run (SRC-1, `Watch the run`).

The workflow cannot solicit a new user decision between internal research stages under the documented runtime contract:

> | No mid-run user input | A run pauses on its own only for agent permission prompts and a [usage-limit wait](#when-a-run-hits-your-usage-limit). For sign-off between stages, run each stage as its own workflow |
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

Runtime liveness recovery is separate from substantive claim rejection. A stalled worker automatically retries its original prompt without the previous attempt's transcript; prior file effects and token expenditure remain. After exhausting retries, fan-out calls continue with a null result, whereas a directly awaited stalled call ends the run with an error. Those are generic runtime alternatives in [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery); the unavailable research script prevents determining which applies to a particular research stage or how it treats a null. The documented unverified-claim outcome must not be generalized into a promise that every worker failure still produces a report.

For a stopped run, the human asks Claude to relaunch the same script. Claude Code refuses while agents from the stopped run remain alive. Replay returns valid completed-prefix results and reruns from the first failed or changed-prompt slot onward, including later completed workers. Missing saved results instead produce `nothing to resume`; a fresh run requires an explicit request. This preserves work selectively, not transactionally, as documented in [RT-RTE-run-replay](runtime.md#rt-rte-run-replay) (SRC-1, `Resume after a pause`, `Which agents run again`, `Resume after you leave the session`). No successful research recovery was observed.

### Delivery boundary

Delivery occurs when the run finishes and its cited report appears in the foreground session. The consumer receives the post-cross-check report, not every raw search finding or the turn-by-turn worker transcripts. Rejected claims have already been omitted; uncheckable claims are marked unverified. Progress inspection remains a separate access path (SRC-1, `Read the report`, `Watch the run`). This terminal presentation does not imply independent operator acceptance, publication, full question coverage, or factual correctness. A stopped or terminally failed run does not meet the documented successful report-delivery condition merely because some workers completed.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-CLM-research-report](runtime.md#rt-clm-research-report)

Workflow selection: the bundled research procedure is the representative connected workflow because it specifies request, research phases, claim filtering and terminal report delivery. Handoff contents are only partially exposed: question, found sources and claims are named, but verifier payloads and the synthesis interface are uninspected. Its executable orchestration is not established by the separate audit-script example.

Verification outcome: failed cross-checks remove claims before delivery; an inability to check preserves an explicit unverified status rather than supplying evidence against the claim. The exact accept/reject owner within the bundled script and vote rule remain uninspected. Computational assessment contributes to report selection; human launch consent is not claim admission. Operating mode: open research questions. Answer oracle: uninspected — the captured procedure supplies no independent reference outcome or exact test beyond described source cross-checking and voting. No quality comparison is observed.

Delivery criterion: the run finishes and the selected, cited report appears in the session. This is delivery of a work product, not evidence of human endorsement or improved future capability.

#### On [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration)

Workflow handoff limit: generic script ownership of next-step selection explains how the research sequence can proceed without foreground turn-by-turn delegation. It does not resolve the bundled research script's worker assignments, evidence payloads or null-handling branches. Intermediate research-stage sign-off cannot be inferred from initial launch approval; the captured runtime directs users needing such sign-off to separate workflows (SRC-1, `Behavior and limits`).

#### On [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery)

Workflow recovery limit: runtime retries address absent output, while research cross-checking addresses claim content. A retry is not a refutation or a content-directed revision. The research script's call structure is uninspected, so fan-out continuation and direct-await terminal failure remain alternatives rather than a predicted outcome for every research worker.

#### On [RT-RTE-run-replay](runtime.md#rt-rte-run-replay)

Workflow continuity: completed research results can feed the relaunched script without fresh worker execution, subject to ordered-prefix reuse. A failure can force later research or synthesis work to repeat even if that work completed. Reuse does not establish a fresh source check, and the capture does not specify freshness invalidation for changing external web content. This limits any inference that a resumed report is newly verified throughout.
