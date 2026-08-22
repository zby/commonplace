---
description: "Dex Horthy's staged human-review workflow moves maintainability judgment upstream and limits unchecked agent work with vertical slices"
source: https://x.com/dexhorthy/status/2081058573556306030
captured: "2026-07-26T07:26:05.314114+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: b0f6f5d21b59fdc5e4f87feca7313172cb1b6e147d199ddfcb742b9c5893569d
status_id: 2081058573556306030
conversation_id: 2081058573556306030
post_count: 6
ingested: "2026-07-26"
type: kb/sources/types/ingest-report.md
domains: [agentic-coding, specification, human-oversight, maintainability]
---

# Ingest: Why Software Factories Fail: Turning the lights back on

## Classification

Horthy prescribes the workflow his team adopted after its lights-off experiment: staged product, architecture, and program-design reviews followed by incrementally reviewed vertical slices.
Author: Dex Horthy writes as a coding-agent practitioner and HumanLayer cofounder. The workflow contains concrete artifacts and task-tiering rules, but the closing product pitch gives him a commercial interest in presenting human-agent collaboration as the durable answer.

## Summary

Part II responds to the maintainability-oracle gap diagnosed in [Part I](https://x.com/dexhorthy/status/2080697380379427275) by restoring humans at high-leverage decision surfaces rather than waiting to review a large generated diff. Horthy divides substantial work into product requirements, system architecture, program design, and vertical slices. Models draft product documents, mockups, diagrams, call-stack trees, file-tree diffs, types, and signatures; humans argue with and approve those artifacts before implementation. Agents then deliver one to three end-to-end slices at a time so functionality can be exercised and 100–200 lines can be reviewed before an error propagates through thousands. The process is risk-tiered: small tasks remain one-shot, medium tasks combine phases, and large or consequential work receives the full treatment. The claimed result is safer 2–3x leverage rather than lights-off 10–100x throughput.

## Connections Found

The article is a practitioner implementation of [Specification strategy should follow where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md): intent and high-leverage design choices are settled in upfront artifacts, while vertical slices keep a feedback path open for understanding that emerges through execution. This is also a broader instance of [Frontloading spares execution context](../notes/frontloading-spares-execution-context.md): human decisions are computed before the coding call so neither the model nor a later reviewer must reconstruct them from a large implementation. Short slices operationalize [Changing requirements conflate genuine change with disambiguation failure](../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) by bounding interpretation-error propagation. Its task tiers match the graded function-allocation precedent in [A Model for Types and Levels of Human Interaction with Automation](model-types-levels-human-interaction-automation.ingest.md), while [Professional Software Developers Don't Vibe, They Control](professional-software-developers-dont-vibe-they-control.ingest.md) independently observes the same planning, small-step, testing, and review posture. Part II retains a human maintainability oracle; unlike [The Bug That Shipped](the-bug-that-shipped-2035319413474206122.ingest.md), it supplies no experiment showing which explicit probes harden that oracle, and unlike our provisional synthesis it does not construct a stronger automated oracle from weak checks.

## Extractable Value

1. **Move an expensive oracle to the earliest truthful decision surface** -- Product intent is cheapest to correct in product review, service boundaries in architecture review, and code shape in program-design review. This combines specification timing with verification cost: judge a decision before downstream artifacts multiply its correction cost. [deep-dive]
2. **Shorten the unchecked span when the oracle cannot be automated** -- Vertical slices do not strengthen the human oracle, but they cap how much work can accumulate under one mistaken interpretation before observation and resteering. This is a distinct control lever from improving verifier accuracy. [quick-win]
3. **Program design is an intermediate human-agent contract** -- Call-stack trees, file-tree diffs, types, and signatures expose maintainability-relevant choices that architecture documents leave implicit and code review discovers too late. The useful abstraction is not “write more plans,” but “materialize decisions at the level where the expensive quality property becomes inspectable.” [deep-dive]
4. **Human involvement should be allocated by task risk, not globally enabled or disabled** -- The reported 40% one-shot share, compressed workflow for medium tasks, and full workflow for large changes form a practitioner instance of multidimensional automation allocation. The percentage is context-bound; the tiering principle has broader reach. [experiment]
5. **End-to-end slices are interpretation probes as well as delivery units** -- A browser-visible or `curl`-testable path tests whether product intent, architecture, and implementation agree, whereas horizontal layer completion can remain locally testable while postponing integration evidence. [experiment]
6. **The workflow manufactures better prompts but not yet a maintainability oracle** -- Structured reviews make expert judgment available to the model and reduce ambiguity, but “better verifiers for software maintainability” appears only as future product direction. The article therefore supports human-oracle placement, not the claim that weak automated checks have already been amplified into warranted lights-off review. [just-a-reference]

## Limitations (our opinion)

This is one commercially interested team's workflow report without comparative projects, defect rates, review-time measurements, or evidence for the headline “30 minutes of planning saves hours of review.” The apparent benefit could come from Horthy's expertise, smaller diffs, better product discipline, or selection of tasks suited to staged planning rather than from the four named phases themselves. Upfront artifacts can also fossilize guesses; [an author should fix what the executor cannot determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), and the article gives little procedure for feeding execution discoveries back into earlier documents. Most importantly for the series' central causal claim, Part II repeats that maintainability is a training and benchmark problem but does not distinguish absent model knowledge from maintainability knowledge that correctness-focused objectives underselect. Its method works under either explanation, so it cannot adjudicate between them.

## Recommended Next Action

Write a theory note titled **“When the oracle is expensive, move judgment upstream and shorten the unchecked span”**, using this workflow as the practitioner case and connecting it to specification timing, interpretation-error propagation, frontloading, and warranted function allocation; keep stronger automated maintainability-oracle construction as an open extension rather than claiming this source demonstrates it.
