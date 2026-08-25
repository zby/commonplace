---
description: "Anthropic practitioner report separating context continuation from work continuation through persistent progress state, structured requirements, incremental commits, and end-to-end verification"
source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
captured: "2026-07-28"
capture: web-fetch
genre: practitioner-report
snapshot_sha256: 92e6ec34be4095dd3b069f401b108d983441e9aff28a5c3d9c322dd0d6fe9c03
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, agent-memory, agent-harnesses, verification]
---

# Ingest: Effective harnesses for long-running agents

## Classification

Anthropic describes an internal long-horizon coding experiment, the observed failure modes, and the harness changes its teams found useful.
Author: Justin Young, writing with acknowledgements to Anthropic's code RL and Claude Code teams; first-party credibility is high for the implemented setup and low for comparative effectiveness because no runs, baselines, or failure distribution are reported.

## Summary

Anthropic reports that repeatedly running a frontier coding model with compaction is insufficient for production-scale work across context windows: sessions either attempt too much and leave half-finished undocumented state, or inspect partial progress and declare the project complete. Its remedy separates initial environment construction from incremental execution. An initializer creates a comprehensive feature ledger, a progress file, an `init.sh`, and initial git state; later sessions read those artifacts and recent commits, verify the application still works, implement one feature, test it end to end, and leave a clean committed handoff. The report's main value is not another compaction technique but an architectural distinction: continuing context and continuing work are different problems, and the latter needs persistent task state plus externally checkable completion criteria.

## Quotes

- **Source extract (verbatim):** However, compaction isn’t sufficient. Out of the box, even a frontier coding model like Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows will fall short of building a production-quality web app if it’s only given a high-level prompt, such as “build a clone of claude.ai.”
  - **Source location:** “The long-running agent problem.”
- **Source extract (verbatim):** We developed a two-fold solution to enable the Claude Agent SDK to work effectively across many context windows: an initializer agent that sets up the environment on the first run, and a coding agent that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session.
  - **Source location:** Introduction.
- **Source extract (verbatim):** To address the problem of the agent one-shotting an app or prematurely considering the project complete, we prompted the initializer agent to write a comprehensive file of feature requirements expanding on the user’s initial prompt.
  - **Source location:** “Feature list.”
- **Source extract (verbatim):** In the case of building a web app, Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would.
  - **Source location:** “Testing.”

## Connections Found

The report is practitioner evidence for [session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md): a compacted conversational continuation does not reliably convey the selected state a fresh worker needs, while progress and git artifacts provide an explicit handoff. It also exemplifies the cold-start problem in [agent statelessness makes routing architectural, not learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md), because every coding session follows the same startup orientation procedure rather than relying on accumulated intuition. The persistent failing/passing feature ledger and mandatory end-to-end checks bear on [oracle accumulation](../notes/oracle-accumulation-improves-the-selection-environment.md), though the source shows a fixed selection environment rather than measuring its growth. Finally, the Opus 4.5 example adds a fourth practitioner case to [scaling absorbs scaffolding at fixed difficulty, not at the deployment frontier](../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md): stronger weights did not eliminate state, decomposition, and verification needs on a harder long-horizon assignment. The closest implemented comparisons are [Claude Context Guard](../agent-memory-systems/reviews/claude-context-guard.md), which broadens the safeguard and audit surface, and [Claude Workstream Kit](../agent-memory-systems/reviews/claude-workstream-kit.md), which adds a small active pointer and explicit closure lifecycle.

## Extractable Value

1. **Context continuation is not work continuation** -- Compaction preserves a lossy conversational thread; the progress file, feature ledger, and git history preserve an addressable work state with next actions and completion evidence. This sharpens the current session-history claim with a practitioner-visible failure boundary. [quick-win]

2. **The first context window has a different type signature** -- Treating initialization as a distinct role lets it produce the environment later workers consume: requirements, executable startup, progress state, and a rollback baseline. This is more precise than asking every session to rediscover and rebuild the same interface. [quick-win]

3. **A feature ledger counters premature completion by making incompleteness explicit** -- Expanding the initial prompt into more than 200 initially failing behaviors prevents a later agent from equating visible progress with task completion. The symbolic `passes` field is valuable because its mutation is narrow and tied to end-to-end evidence. [experiment]

4. **Clean-state handoff is a quality invariant, not merely a summary** -- Descriptive progress text is paired with a working commit and a basic end-to-end test on startup, so later sessions can detect divergence between the record and executable reality. This gives cross-session continuity a verification surface instead of trusting the progress text alone. [quick-win]

5. **Frontier scaffolding can be measured by function rather than file count** -- The source identifies four surviving functions around a frontier model: orientation, task decomposition, durable state, and verification. Those functions are a more stable longitudinal measurement target than the exact `claude-progress.txt`, JSON, and shell files used in this experiment. [deep-dive]

## Limitations (our opinion)

This is a first-party practitioner report built around one full-stack web-app experiment. It gives no task-success rates, number of runs, token or wall-clock overhead, comparison with a simple non-compacting baseline, or examples where the proposed harness made results worse. The observed benefit could partly come from spending more inference and verification effort rather than from the specific initializer/coding-agent split.

The report also bundles several interventions -- a feature ledger, incremental scope, git commits, progress summaries, startup scripts, and browser testing -- without ablation, so it cannot establish which mechanism is necessary. Its claim that JSON is less likely than Markdown to be rewritten inappropriately is especially context-bound and model-dependent. Treat the article as strong evidence that Anthropic encountered these failure modes and used this design, but only weak evidence that the design generalizes beyond Claude, coding, and repository-shaped work.

## Recommended Next Action

Update [scaling absorbs scaffolding at fixed difficulty, not at the deployment frontier](../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) with an `evidenced-by` link to this snapshot, framed narrowly as practitioner evidence that a frontier model on a longer-horizon assignment still required explicit work state, decomposition, and end-to-end verification.
