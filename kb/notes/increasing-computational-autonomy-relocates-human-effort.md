---
description: "In an open-ended system, increasing computational autonomy need not cut total human hours — attention moves to the frontier — so measure improvements per human judgment, not human time"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Increasing computational autonomy relocates human effort to the frontier instead of reducing it

The naive test of increasing computational autonomy is falling human hours: if more pathway functions become computationally closed, the human should be needed less and less. In an open-ended improvement system, that is usually not what happens. The observed pattern runs the other way around:

1. a class of routine work becomes computationally executable;
2. the system can therefore process more material or attempt harder improvements;
3. human attention moves to that new frontier;
4. total human time stays roughly constant — while the human contribution *per completed improvement* falls.

In miniature: once link checking becomes a validator, nobody banks the freed minutes. Review attention moves to whether the linked claims are actually right — a harder question that previously went unasked because the cheap question consumed the session. The hours are the same; what an hour buys has changed.

The mechanism is an elastic workload. An open-ended system has an unbounded backlog of possible improvements, so attention freed from routine work moves to work that previously went unattempted. Bainbridge's ironies of automation identified the broader pattern: automation transforms rather than removes the operator's role, leaving the residue that could not be automated ([Bainbridge 1983](https://doi.org/10.1016/0005-1098(83)90046-8)). Here that residue is the work past the oracles — noticing, objective-setting, and the shape judgments no automatic check covers, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

> As computational autonomy increases, a fixed amount of human judgment supports a larger volume, longer horizon, or greater difficulty of self-improvement.

Total hours confound a change in actor allocation with the ambition it enables. The relevant change is in what each human judgment supports.

## What to measure instead

Ratio and frontier measures separate the two:

- improvements completed per human judgment supplied;
- computational steps between human interventions;
- proportion of candidates accepted or rejected computationally;
- breadth of artifacts changeable without bespoke human instruction;
- the difficulty frontier at which human intervention becomes necessary.

Concretely: a session that drafts a note, validates it, discovers its connections, and commits, with one human judgment at the merge, has several computational steps per intervention; the same note produced by dictation has nearly none — at identical human hours.

These are proxies, and comparing them across time inherits the open commensurability problem — the function list itself changes as the system grows, [since measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md). What this note adds is the purpose such measurement should serve: not “are humans spending fewer hours?” but “is the intervention frontier moving outward?”

## Scope

- The claim concerns computational allocation, not methodological closure: a person can execute a settled gate, while an unattended model can improvise. The two often advance together when settled criteria become executable, [but they track different changes](./methodological-and-computational-closure-track-different-changes.md).
- The load-bearing premise is the elastic backlog. Where the workload is genuinely fixed — a bounded migration, a system in maintenance-only mode — increasing computational autonomy *should* reduce human hours, and observing it there would confirm the mechanism rather than refute this note.
- The pattern is stated from one system class (agent-operated knowledge systems, [Commonplace among them](../reference/commonplace-as-a-reflective-system.md)) and Bainbridge's industrial precedent; whether it holds across self-improving systems generally is the conjecture.

## Open Questions

- Whether intervention density and computational run length can be recovered retroactively from repository history, giving the frontier claim a cheap first test.
- Whether the difficulty frontier can be operationalized at all, or only ranked ordinally by cases that did and did not need intervention.

---

Relevant Notes:

- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: identifies computational closure as an actor-allocation endpoint rather than methodological settlement
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why the residue humans keep is exactly the frontier past the oracles
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: the commensurability problem the proposed measures inherit, now given a purpose
- [Commonplace as a reflective self-improving system](../reference/commonplace-as-a-reflective-system.md) — evidence: the human-inclusive system whose growing computational allocation alongside continued human involvement motivated the pattern
- [The tag-readme trace read as a self-improving loop](../reference/tag-readme-trace-as-self-improving-loop.md) — evidence: a worked instance of relocation — the automatable halves run in code and agents while the human keeps exactly the noticing and shape judgment
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: why the frontier is durable structure, not a temporary capability gap — automation stalls wherever verification is expensive
