---
type: reference/types/design-proposal.md
description: "Proposal: source advisory analysis audits from native harness sessions instead of duplicate stdout traces, while leaving audit value and retention policy undecided."
brief: native-traces-for-advisory-analysis-audits.brief.md
---

# Native traces for advisory analysis audits

Advisory analysis audits currently depend on verbose subprocess logs that duplicate harness session traces. Native traces could supply the audit evidence while ordinary subprocess output retains only completion and model information. That could reduce duplicate storage, but reliable session association and evidence retention would need explicit support.

This proposal parks that option. It does not authorize implementation, an experiment, or audit removal. Whether advisory audits produce enough useful findings to justify their cost is unresolved; changing their trace source would not answer that question.

## Current state (as of 2026-11-18)

The automatic collector in `src/commonplace/lib/agentic_analysis/audit.py` enumerates every recorded Workjig attempt and scans its owned `stdout.log`. It deliberately excludes personal-session discovery and traces redirected outside the run's launch tree. The advisory audit does not decide publication acceptance.

The existing Claude scanner accepts persisted session JSONL as well as streaming stdout. The Pi scanner accepts persisted sessions through its `pi-session` format. Parsing native tool-failure records therefore already exists; associating native sessions with individual launches does not.

The auditor's own completion checks count tool calls from stdout. Its launch disables native session persistence with Claude's `no-session-persistence` or Pi's `no-session` flag. A migration covering the auditor itself would have to change those choices too.

The current storage concern arose while preparing a separate repository for ignored report state. Making that repository ignore subprocess logs does not itself reduce local log generation or preserve native traces elsewhere.

## Options and consequences

| Option | Consumer and effect | Feasibility and commitment |
|---|---|---|
| Keep audit stdout | The existing collector and auditor continue consuming per-launch streams. | Already implemented. Retains duplicate local traces but requires no new session lookup. Ignoring logs in the state repository is a separate backup decision. |
| Read native sessions in place | A new collector associates each attempt with one native session and passes only those files to the existing scanners and auditor. | Parsers exist. Exact launch association, bounded access and persistence for the auditor still need implementation. Avoids a second full trace copy, but evidence can disappear when machine-local session stores are cleaned or unavailable. |
| Capture native sessions into run state | A new collector freezes the associated native traces under the run; scanners and the auditor read those captures. | Shares the association work above and adds capture and integrity handling. Evidence survives native-store cleanup, but copying traces retains local duplication and requires an explicit backup policy. |
| Disable advisory audits | The analysis workflow stops launching the advisory scanner/model audit; production analysis acceptance remains separate. | A workflow change, not a trace migration. Avoids audit cost and its trace requirement, but gives up its findings. The operator has not decided whether that loss is acceptable. |

No option adds an acceptance gate or establishes that model judgments are correct. Existing failure scanners identify explicit events, not semantic defects or successful recovery. The advisory model's findings still require source-based verification; changing trace storage supplies no stronger warrant.

## Migration boundary if selected

A native-trace implementation would need to:

- Associate every attempt, including failed and interrupted launches, with its exact session. Assigning identity before launch is a candidate route; relying only on a successful final result leaves a coverage gap.
- Restrict lookup and auditor access to those associated sessions. Broad searches through personal session history would widen the current evidence boundary.
- Record trace identity and content hashes. Missing, mismatched or unsupported traces must remain explicitly unscanned, not count as clean.
- Preserve stable audit snapshots and replay behavior. A later session mutation must not silently change evidence behind an existing audit.
- Decide whether native-store cleanup may make old audits unverifiable, or whether run-owned captures must survive it.
- Cover the auditor's own completion and tool-call-budget checks, not only production worker failures.

The expected change is concentrated in the harness launch integration, audit collection/completion logic and their tests. It is not a scanner rewrite. A per-launch session-identity hook may require Workjig integration changes; that boundary has not been established. Cross-harness session lookup and interruption handling remain unverified.

## Deferred decision

Keep the current audit mechanism available while this proposal is parked. No additional evidence collection is commissioned. The waiting cost is continued audit execution and duplicate trace storage where verbose analysis output remains enabled; no expiry date is asserted.

Return this to the operator when audit cost or a consequential audit finding prompts reconsideration, or before implementing native-trace lookup. At that point, distinguish three decisions: whether to retain audits, whether to investigate their value, and—only if needed—which trace-retention option to implement. Evidence of useful, independently verified findings relative to cost could support retention; lack of such evidence is not by itself proof that audits have no value.

Adopting native traces would require demonstrated association for successful and interrupted attempts, bounded access, explicit missing-trace reporting, preserved completion and budget checks, and a selected retention policy. Disabling audits instead requires an explicit operator decision. Both changes are code-reversible, but deleted or expired historical traces would not be recovered by reverting code.
