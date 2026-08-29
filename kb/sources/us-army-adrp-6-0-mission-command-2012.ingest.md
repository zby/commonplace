---
description: Army doctrine treats delegated execution as bounded autonomy supported by intent, trust, resources, feedback, and retained responsibility, anchoring and limiting mission-command analogies for agents.
source: https://home.army.mil/wood/application/files/7715/5751/8336/ADRP_6_0_Mission_Command.pdf
captured: "2026-08-28"
capture: pdftotext
capture_scope: partial-source
genre: official-statement
snapshot_sha256: 0d8051d92a9f0d048265ea02aa2c97b904b7e12cd079208568b61a4b3e6001b7
ingested: "2026-08-28"
type: kb/sources/types/ingest-report.md
domains: [agent-orchestration, delegation, intent, coordination]
---

# Ingest: ADRP 6-0: Mission Command

## Classification

This is prescriptive U.S. Army doctrine: an official institutional statement of how commanders and staffs should combine delegated execution with control under uncertainty. It has high authority for what the Army prescribed at this publication state, but it is not an independent evaluation of whether the doctrine produces better outcomes.

Author: Headquarters, Department of the Army. The U.S. Army Combined Arms Center is the proponent and its Combined Arms Doctrine Directorate prepared the publication, providing a direct institutional-authority signal for the doctrine.

## Summary

ADRP 6-0 presents mission command as a response to uncertain, adaptive operations: commanders communicate purpose, key tasks, desired end state, constraints, and resources, while trained subordinates choose situation-dependent means and act when orders no longer fit. This discretion is not hands-off delegation. It sits inside a system of mutual trust, shared understanding, lawful authority, feedback, risk management, staff support, information flow, adjustable control, and commander accountability. For Commonplace, the document is worth reading as a mature specification of intent-framed delegation and as a warning that copying its concise-order surface without its organizational preconditions does not reproduce its mechanism.

## Quotes

- **Source extract (verbatim):** Commanders understand that some decisions must be made quickly and are better made at the point of action. Mission command concentrates on the objectives of an operation, not how to achieve it. Commanders provide subordinates with their intent, the purpose of the operation, the key tasks, the desired end state, and resources. Subordinates then exercise disciplined initiative to respond to unanticipated problems.
  - **Source location:** Chapter 1, paragraph 1-9 (ADRP 6-0, p. 1-2)

- **Source extract (verbatim):** Commanders use mission orders to assign tasks, allocate resources, and issue broad guidance. Mission orders are directives that emphasize to subordinates the results to be attained, not how they are to achieve them (ADP 6-0). They provide subordinates the maximum freedom of action in determining how to best accomplish missions. Mission orders seek to maximize individual initiative, while relying on lateral coordination between units and vertical coordination up and down the chain of command.
  - **Source location:** Chapter 2, paragraph 2-20 (ADRP 6-0, p. 2-4)

- **Source extract (verbatim):** Commanders delegate authority to subordinates to assist commanders in fulfilling their responsibilities. Subordinates are accountable to their commanders for the use of delegated authority, but commanders remain solely responsible and accountable for the actions of their subordinates. Delegation allows subordinates to decide and act for the commander in specified areas. Once they delegate authority, commanders supervise just enough to assure subordinates’ success. While commanders can delegate authority, they cannot delegate their responsibility for the actions or omissions of their subordinates.
  - **Source location:** Chapter 2, paragraph 2-34 (ADRP 6-0, p. 2-6)
- **Source extract (verbatim):** Successful commanders understand that their leadership directs the development of teams and helps to establish mutual trust and shared understanding throughout the force. Commanders provide a clear intent to their forces that guides subordinates’ actions while promoting freedom of action and initiative. Subordinates, by understanding the commander’s intent and the overall common objective, are then able to adapt to rapidly changing situations and exploit fleeting opportunities. They are given the latitude to accomplish assigned tasks in a manner that best fits the situation.
  - **Source location:** Chapter 1, paragraph 1-12 (ADRP 6-0, p. 1-3)
- **Source extract (verbatim):** Commanders at all levels need education, rigorous training, and experience to apply these principles effectively. Mission command operates more on self-discipline than imposed discipline.
  - **Source location:** Chapter 1, paragraph 1-13 (ADRP 6-0, p. 1-3)

## Connections Found

The source's role is a doctrinal anchor and transfer-limiting counterpoint for intent-framed delegation. It is independent mature-domain evidence for [fixing what the executor cannot determine rather than its situation-dependent method](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), and it specifies the coherent practice cluster behind the *Auftragstaktik* example in [methodology selection](../notes/capable-agents-need-methodology-selection.md). It does not establish that a model reconstructs or follows that cluster from a compact cue. Its dependence on trained judgment, shared experience, trust, resources, feedback, lawful authority, and retained commander responsibility makes [mechanism-preserving transfer](../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) the governing limit. Relative to [coordination guarantees](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) and [Intelligent AI Delegation](./intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md), it shows dispersed execution as a governed control regime; the agent-domain accounts must separately supply verification, permission, isolation, and accountability mechanisms that military hierarchy provides socially and institutionally.

## Extractable Value

1. **Bounded delegation is a control regime, not task under-specification.** Clear intent and freedom over means work here only as part of a larger system containing competence, trust, authority bounds, resources, communication, feedback, risk acceptance, and answerability. This qualifies any attempt to equate a brief outcome-oriented agent prompt with mission command. [deep-dive]

2. **The appropriate degree of control depends on coupling and operational phase.** The doctrine combines tighter control for precisely synchronized activity with wider discretion where local adaptation matters. Agent orchestration could test the corresponding hypothesis that control policy should vary by task interdependence and execution phase instead of staying uniformly centralized or delegated. [experiment]

3. **Delegated authority must be matched by resources while responsibility remains upstream.** The source couples freedom to act with people, information, time, equipment, and support, yet does not treat delegation as absolving the commander. This adds a resource-sufficiency condition to existing local accounts of authority transfer and accountability. [quick-win]

4. **Information demand has an autonomy cost.** The doctrine treats excessive reporting and demands for completeness as burdens that can suppress initiative and damage trust. This suggests a target-side experiment on whether dense monitoring, status requests, or context collection improve agent oversight only up to the point where they consume execution capacity or bias local judgment. [experiment]

5. **Shared understanding is maintained, not merely transmitted.** Multidirectional dialogue, lateral coordination, feedback, records, and continuing reassessment do work that an initial statement of intent cannot do alone. This supplies a socio-organizational comparison for agent systems that treat a shared prompt or shared store as sufficient coordination. [deep-dive]

6. **The content warrant for a methodology cue is separate from its activation warrant.** ADRP 6-0 can ground what the mission-command cluster contains, but it cannot show that an LLM recalls that cluster faithfully, selects it over neighboring methods, or executes it successfully from the phrase *Auftragstaktik*. [just-a-reference]

## Limitations (our opinion)

The publication is normative doctrine, not an intervention or comparative study. Its institutional authority establishes what the Army prescribed; the historical illustrations and doctrinal assertions do not establish causal effectiveness, comparative advantage over detailed command, or the conditions under which the approach fails.

The mechanism is embedded in trained human teams inside a lawful military hierarchy. Professional formation, shared danger and experience, personal authority, enforceable orders, moral and legal responsibility, and human judgment are material assumptions, not decorative context. LLM agents do not automatically share them, so any transfer to prompts or multi-agent architectures remains a target-side conjecture under [the shared-mechanism test](../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md).

The document records doctrine dated 2012 with changes through 2014 and does not establish its own present-day currency. Its official authors also have an institutional interest in presenting the prescribed system as coherent. The retained capture is explicitly partial: it includes the substantive chapters but ends before the listed source notes, glossary, references, and index. That boundary prevents this report from auditing the doctrine's full source lineage, checking every formal definition against the glossary, or treating the snapshot as the complete publication.

## Recommended Next Action

Write a new note titled **Intent-framed delegation is a control regime, not a short prompt**, synthesizing the doctrine's competence, resource, feedback, control, and accountability conditions with the existing executor-boundary and coordination-guarantee notes while marking every agent-system implication as requiring target-side evidence.

---

Relevant Notes:

- [Intent-framed delegation is a control regime; prompt length does not establish it](../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — abstracted-from: point-of-action initiative remains coupled to intent, resources, specified authority, coordination, supervision, accountability, and retained upstream responsibility
