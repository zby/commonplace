---
description: "A ten-day agent campaign illustrates bounded live state, clocked execution and review-based escalation; its retained operating changes offer limited evidence of adaptation without weight updates."
source: https://arxiv.org/abs/2609.19519
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: c8cc9287769c93455351c88bfd0d4678b66c33d17e1beb4906342d2e5e08974b
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, context-engineering, learning-theory, agent-orchestration]
learning_claims: true
---

# Ingest: An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence

## Classification

A scientific preprint combining an architectural argument with a retrospective deployment report. Its empirical contribution is one campaign, not a controlled comparison of agent architectures. Authors Erik Nijkamp, Anurag Koul, Egor Pakhomov and Bo Pang are affiliated with Salesforce AI Research and report their own system's operation.

## Summary

The paper proposes that agents working beyond context windows, process lifetimes and intervals of human attention need durable operation before continual learning. Its architecture combines levels organized by time scale, bounded files summarizing lower levels, clocked sessions called ticks, explicit file protocols, and model tiers that escalate work after review failures. One ten-day reinforcement-learning reproduction campaign, including eight days under the clock, reportedly completed 211 ticks and recovered across 47 context resets while a human attended daily. The authors report that retained decisions, recipes and a worker-stop guard changed later behavior without weight updates. These observations establish a reported example of the combined design working on one task; they do not isolate the benefits of its hierarchy, review cadence or model cascade. The principal contribution for Commonplace is a concrete account of how current state, operating rules and critical verdicts can remain effective across resets, with proposed learned scheduling and routing components left for future work.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source exemplifies [active work state](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md): the driver reconstructs unfinished work from a checkpoint, standing decisions, a plan, open unknowns and active experiment cards. A newer append-only journal overrides an older checkpoint. This adds a concrete recovery rule to the note's distinction between current state and retrospective history. The reported campaign supports feasibility of this combined arrangement; it does not show that bounded summaries never lose relevant information, and it leaves closure and removal of completed work less explicit than the note requires.

The source also compares with [governing behaviour-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md). Its strongest example is a recurring worker failure first addressed by instructions in every brief and then by an executable guard. That is a concrete change in how a retained rule determines behavior, rather than mere storage. The campaign does not establish systematic regression checking for such changes or compare alternative ways to install them.

## Learning Claims (our opinion)

The authors call their mechanism accumulation rather than learning: principal answers persist as decisions, reviewer findings shape later experiment rules, successful recipes enter routine workers' briefs, and recurring failures become harness guards. They reserve learned components for future policies selecting a worker tier or wake interval. No such policy is trained or evaluated here. The reinforcement-learning models being reproduced are the campaign's subject; their weight updates are not adaptation of the agent harness.

Under the [theory-builder](../notes/definitions/theory-builder.md) conditions, fixed model weights do not exclude the whole system, including its participating human. Decisions, experiment cards with hypotheses, recipes, and briefs are stated text (condition 1) that later workers act on (condition 2). The six ranked hypotheses used to diagnose slow training, and the reviewer's criticisms of task shortcuts and a misleading stop rule, are criticism of stated content followed by changes (condition 3, shown in selected narratives). The campaign runs a sequence of different experiments, and recipes, rules, and the worker-stop guard are carried into later ones; the guard reportedly prevented recurrence after an instruction-only remedy failed (condition 4 within the campaign; nothing is shown across campaigns). The campaign is a theory builder at the strength of selected narratives. Not every retained decision is shown to be a criticized theory. Learning is a separate claim: the paper supplies no comparison that isolates the contribution of retained criticism.

The proposed learned policies would operate within supplied tier choices, wake controls and review interfaces. Their success would therefore remain [improvement within a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), not evidence that those interfaces preserve every needed distinction or admit every needed response. The campaign itself revised recipes, task environments and a guard, so it was not wholly frozen. However, it did not compare alternative temporal hierarchies or protocol boundaries. Its useful challenge to a weight-centered account is that consequential adaptation already occurs in retained operating artifacts before those proposed learners exist.

## Extractable Value

1. **Preserve control signals through compression.** The architecture sends escalation lines, attention items and kill verdicts across levels without compression, while compressing ordinary work state. This is a specific design candidate for keeping stop conditions visible in a bounded context. Its advantage over other summary schemes remains untested. [experiment]
2. **Make resume order and stale-checkpoint recovery explicit.** Reading current state in a fixed order, with a newer journal taking precedence, operationalizes the active-work distinction already present in the KB. The single campaign supplies a reported implementation pattern, not a guarantee of complete recovery. [quick-win]
3. **Track when a prose rule needs enforcement.** The worker-stop vignette records a progression from repeated failure to a brief instruction and then a guard that reportedly stopped recurrence. It can ground discussion of how evidence changes a rule's form and authority, while leaving broader regression effects unresolved. [quick-win]
4. **Use retained-artifact adaptation as a learning baseline.** Comparing a future learner against a system that already preserves decisions, criticism and recipes would help separate gains from persistence from gains due to the new learning mechanism. The paper proposes this baseline but does not run the comparison. [experiment]

## Limitations (our opinion)

The central evidence is one author-reported reproduction campaign with daily human attendance, 25 escalations and nine principal-only decisions. No controlled harness baseline or component ablation tests whether seven levels, the forty-line read limit, fresh reviews, or review-based escalation are necessary or preferable. The reported fall from 958 to 180 seconds per training step follows a change to steered labor, but different worker sessions, additional diagnosis and recipe changes prevent assigning the gain solely to steering.

The reproduced comparisons concern stale-rollout training with and without a correction, and the full reinforcement-learning method against its control. They are task outcomes inside the harness, not comparisons between harness designs. Four redesigns of the evaluation environment and revision of a stop rule make evaluation governance part of the result. The paper reports those interventions but provides insufficient detail here to independently establish comparability or reproduce the campaign. No implementation was inspected or executed for this ingest.

External files do not themselves establish absence of forgetting: correct write-back, faithful compression and later use remain necessary. Similarly, the 86% routine and 14% strong shares of labor spend provide no total-cost comparison with an alternative system. Learned components staying inside retained checks would constrain only behavior those checks can detect; the source's stronger suggestion that learning cannot exceed verification is not established. These limits favor reuse of specific mechanisms as candidates, rather than promotion of the architecture as a generally validated prerequisite for continual learning.

## Recommended Next Action

Update [Active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) with the explicit resume order and newer-journal recovery rule as a reported single-campaign example, preserving the unresolved closure and compression-fidelity limits.
