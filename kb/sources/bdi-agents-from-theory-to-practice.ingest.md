---
description: "Rao and Georgeff show why a BDI agent keeps a feasible schedule after conditions change. The commitment is to a current decision, not to a procedure learned for future use."
source: https://cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: e2b16c301b13a818d2089bef08b6f845b9281a3dfca5d6fd6b69b01f9a99696c
ingested: "2026-11-21"
occasion: "Which parts of deliberative learning, if any, have precedents in BDI agent deliberation and its retention judgments?"
type: types/ingest-report.md
domains: [belief-desire-intention, intention-reconsideration, resource-bounded-reasoning, air-traffic-management]
---

# Ingest: BDI Agents: From Theory to Practice

## Classification

In this 1995 ICMAS paper, Anand S. Rao and Michael P. Georgeff of the Australian Artificial Intelligence Institute synthesize their earlier work on agent logics and interpreters. They use an implemented air-traffic management system, OASIS, to illustrate the correspondence rather than to benchmark it.

## Summary

When the world changes during planning or execution, recomputing the best action after every change costs time, but following the original choice unconditionally can defeat its purpose. Rao and Georgeff distinguish what an agent believes, what it wants, and which course it has chosen. The third component, intention, lets the agent act on an earlier choice until a specified condition releases it. The authors map decision trees into possible worlds, formalize alternative commitment policies, and show what a practical interpreter leaves out: rather than deducing every option, it matches events and current beliefs to written plans and stores adopted plans on execution stacks. The OASIS arrival sequencer illustrates how an agent can react to evidence that its schedule is infeasible without recalculating it for every change in wind.

## Contribution assessment (our opinion)

The strongest contribution is the trace from a formal distinction to an observable difference in behavior: two agents can agree on the best initial schedule yet react differently to the same later observation because their commitments differ. That makes intention maintenance a design choice one can specify and test, rather than merely a name for whatever the agent does next. The paper integrates earlier results rather than claiming to originate the distinction. OASIS makes the design credible as an implementation; it does not establish which policy performs best.

## Quotes

No source quotes have been retained yet.

## Connections Found

The [BDI architecture survey](./bdi-agent-architectures-a-survey.ingest.md) distinguishes selecting an existing plan rule from learning one. OASIS supplies a precedent for a narrower part of deliberative learning: judging whether to stand by a previous choice on grounds that differ from those used to make it. What survives that judgment is the current landing schedule. Abandoning it neither removes the scheduling procedure from the library nor teaches the agent a replacement.

## Extractable Value

1. **Choosing and keeping need not use the same test.** The sequencer uses aircraft characteristics, separation requirements and a cost function to select a schedule. It then keeps that schedule until it believes the aircraft have landed in order or no longer considers the next aircraft's assigned arrival time achievable. A wind change alone need not reopen the choice, even if another sequence might now cost less. This is a precedent for separate selection and retention judgments, not for learning either judgment from experience. [quick-win]
2. **Ask who can change the retention test.** The formalism lets a designer choose between commitment policies: a single-minded agent admits changes of belief as grounds for dropping an intention; an open-minded agent also admits changes of desire. This variety across designs does not imply that an agent decides for itself which grounds should count in a new case. [quick-win]

## Limitations (our opinion)

Selective reconsideration saves work only if the agent can recognize relevant changes cheaply enough. OASIS gives one domain-specific trigger, not a procedure for discovering such triggers. The authors report parallel trials with live radar data but give no comparison of their sequencer against one that always replans or one that never does. The case therefore cannot quantify the computation saved or the cost of keeping a feasible but inferior schedule. Its written plan library also limits the inference about learning: the paper describes how developers add plans during debugging, not how execution revises the library.

## Recommended Next Action

Add the OASIS schedule example to the evidence in `kb/work/learning-method-name/` to distinguish keeping a current decision under a feasibility test from keeping a learned procedure for future tasks.
