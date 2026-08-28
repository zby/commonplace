---
description: "Warp's human-feedback loop uses a scheduled improver and mandatory review to update file-based agent skills, but offers no downstream outcome evaluation."
source: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
captured: "2026-08-28"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: 52d13fbb8f9259ebb4b00cf1948b5a743b1bbb8ecd2839a2a8193f7595aff1e5
ingested: "2026-08-28"
type: kb/sources/types/ingest-report.md
domains: [agent-learning, human-feedback, instruction-update]
---

# Ingest: How Warp builds self-improving agents on Claude

## Classification

This is a first-party practitioner report: a Claude Platform customer story describes Warp's deployed workflow, illustrates it with one GitHub issue, and offers operating advice rather than controlled results. Author: Michael Segner; the central implementation account and rationale are attributed to Warp founder Zach Lloyd.

## Summary

Warp separates task execution from instruction improvement. A task-specific base skill produces work; humans leave feedback where that work already lives; a scheduled improver collects the feedback and proposes a small edit; and a human-reviewed PR determines whether the edit enters the base skill used by later runs. The account is worth reading for this explicit division of evidence collection, proposal generation, and landing authority, plus its advice to prefer specific explanations over binary reactions, but it does not show that accepted edits improve later task outcomes or make subsequent improvement more productive.

## Quotes

No source quotes have been retained yet.

## Connections Found

The report is a practitioner anchor for [proposal selection with operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) and [persistent deployment-time adaptation through retained system-definition artifacts](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md): a readable skill diff becomes operative only after human merge. It adds an explicit-feedback case to the [trace-learning survey](../agent-memory-systems/trace-learning-techniques-in-related-systems.md). Its advice about detailed reasons supports [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), while [an accepted edit verifies the change, not the rule](../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) and [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md) bound the article's approval and compounding claims. [Harness Updating Is Not Harness Benefit](harness-updating-is-not-harness-benefit.ingest.md) names the missing loading, procedural-match, and task-benefit measurements.

## Extractable Value

1. **Separate the human's outer-loop roles.** Detailed feedback supplies diagnostic evidence, PR review governs promotion, and later behavioral evaluation would test uptake; Warp reports the first two but not the third. This distinction prevents “human in the loop” from hiding which inference or authority a person actually supplies. [quick-win]
2. **Treat feedback specificity as a constraint on candidate search.** A reason tied to a codebase convention narrows the instruction an improver should infer, whereas a binary reaction says little about the failed mechanism. The source supplies a concrete practitioner case for the KB's diagnostic-richness claim. [just-a-reference]
3. **Use an editable skill as a bounded deployment-time update surface.** Warp changes task behavior through reviewable text while leaving feedback collection, scheduling, the improver, and the PR workflow outside the base skill's update space. That split makes both the mutable artifact and the fixed surrounding machinery inspectable. [quick-win]
4. **Separate reusable improvement machinery from task-specific knowledge.** Warp reports one improver pattern across triage, review, and specification agents while retaining distinct base skills. Testing which parts transfer would clarify whether reuse comes from a shared proposal protocol or merely from similar repository workflows. [experiment]
5. **Measure compounding beyond retained edits.** The reported workflow establishes accumulation because merged changes persist, but a compounding claim needs evidence that an earlier improvement increases the productivity of a later improvement, alongside loading and task-benefit checks. [experiment]

## Limitations (our opinion)

The article is a vendor-published account of one customer's successful pattern, so it exposes neither failed update attempts nor the team, infrastructure, review cost, and selection effects behind the result. Its worked issue shows that the machinery can propose and land a plausible skill edit, not that the edit was loaded reliably, generalized beyond that issue, improved downstream task outcomes, or avoided regressions. Human approval controls what changes, but does not by itself validate the inferred rule. The broad claim that the method works across Warp's repository and the claim that feedback compounds are unsupported by comparative, longitudinal, or causal measurements. The linked demonstration code was not independently inspected or executed for this ingest.

## Recommended Next Action

Write a note titled **Human feedback, promotion authority, and downstream evaluation are separate outer-loop roles**, synthesizing this practitioner case with the connected diagnostic-richness, accepted-edit, and harness-benefit boundaries.
