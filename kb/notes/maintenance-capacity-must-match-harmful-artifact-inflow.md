---
description: Stable quality depends on capacity to prevent, contain, detect, and repair harmful retained artifacts keeping pace with their risk-weighted inflow, for which gross generation volume is only a proxy
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [kb-maintenance]
---

# Maintenance capacity must match harmful-artifact inflow

An agent-maintained system keeps quality stable only while its effective maintenance capacity keeps pace with the risk-weighted inflow of harmful retained artifacts. Effective maintenance includes preventing defects before retention, quarantining material before exposure, detecting defects, and repairing or removing them. Gross generation throughput is only a proxy for that load.

The relevant rates can diverge. A system with strong generation-time checks can produce more artifacts without increasing its repair queue. By contrast, one rare but widely reused defect can create more maintenance demand than many harmless outputs. Artifact volume matters through defect incidence, expected harm, exposure time, detection latency, and remediation effort, not by itself.

The invariant is queue stability over the operating window. If repair-requiring artifacts enter the system, or become harmful, faster than the system prevents, contains, or repairs their effects, the harmful backlog or cumulative exposure grows. “Match” therefore means enough effective capacity to keep that backlog and exposure within the system's declared quality bound. It does not require one cleanup action per artifact or continuous execution.

## Evidence

OpenAI's Codex team reported this pressure in one agent-generated codebase at roughly one million lines. Early manual “AI slop cleanup” consumed 20% of engineering time. The team replaced Friday cleanup sessions with background agents that scan for pattern violations and open small refactoring changes, many of which are auto-merged. The case shows that recurring automated cleanup can stabilize a high-throughput repository where periodic manual cleanup did not scale. It does not measure a proportional relation between generated lines and cleanup work. ([Harness Engineering](https://openai.com/index/harness-engineering/))

Retained explanations create a recursive version of the same load. Generated comments and documentation can enter later agents' context, where those agents may trust, imitate, or elaborate on them. A misleading explanation can therefore increase exposure and seed further defects before removal. The [AI;DR discussion](../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) supplies practitioner reports of this path, but its self-selected anecdotes establish a possible mechanism, not prevalence or effect size.

## Implications for this KB

The KB already separates parts of the response: a [maintenance operations catalogue](./maintenance-operations-catalogue-should-stage-stable-procedures.md) names what can be cleaned, [external triggering](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) schedules work outside routing, and [staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) identifies some changes that need attention. Sizing that response requires a signal for harmful inflow, not a count of all new notes or links.

Generation volume can contribute to that signal when defect incidence and harm remain comparable. It stops being sufficient when prevention improves, artifact risk varies, or existing material becomes stale while generation stops. Maintenance frequency is likewise one capacity lever rather than the invariant: a periodic batch can suffice when material stays quarantined and the batch clears the queue, while immediately exposed and recursively reused errors may require continuous detection or repair.

This shifts the operational question from “How many artifacts did agents generate?” to “How quickly is harmful retained material entering use, and how much risk can the current prevention, containment, detection, and repair loop neutralize?” The first quantity is cheap to count. The second determines whether maintenance is keeping up.

---

Relevant Notes:

- [Notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — extends: risk-weighted ranking is one way to spend bounded maintenance capacity on the most consequential candidates
- [Stale self-description conceals its own staleness](./stale-self-description-conceals-its-own-staleness.md) — extends: time-driven reflexive drift can create harmful inflow even when artifact generation is low
- [Where change candidates come from in Commonplace](../reference/where-change-candidates-come-from-in-commonplace.md) — evidenced-by: the current system has several detection channels whose outputs still require capacity and prioritization
