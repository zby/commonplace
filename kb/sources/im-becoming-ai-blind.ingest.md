---
description: "Cymerys's AI-blindness essay adds a repeated-exposure account of channel-wide rejection beyond existing AI-writing triage reports"
source: https://cymerys.com/w/im-becoming-ai-blind
captured: "2026-08-22"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: c267cbb4a427d8b4f0dba9d7e6845cd6d479930719cf6ea12e18e9171b6b25ea
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [llm-writing, human-ai-collaboration, attention, credibility]
---

# Ingest: I'm becoming AI-blind

## Classification

This is a conceptual essay built from retrospective self-observation, three paraphrased workplace examples, and an analogy to banner blindness. It proposes an explanation for the author's reading behavior rather than reporting a controlled study.
Author: Rafal Cymerys writes from first-person workplace experience with design, marketing, and technical-requirements documents. The captured essay provides no credentials that add authority to its claims about AI-text detection, attention, or learning.

## Summary

Cymerys reports that he sometimes fails to process workplace documents, later asks questions those documents already answered, and has come to associate the episodes with low-effort AI-marked prose. His examples combine four complaints: simple material expanded at length, exploratory model reasoning left in a final document, irrelevant technical detail mixed into another discipline's artifact, and routine features presented as breakthroughs. He hypothesizes that repeated exposure to low-meaning AI text taught him to suppress familiar cues automatically, like banner blindness. The claim is scoped to low-effort output, not all AI-assisted writing; its distinctive consequence is that a tool meant to save author time can create reader and coordination costs even when a document contains useful material.

## Claims

No claims have been grounded yet.

## Connections Found

The essay is a bounded naturalistic case for [cheap generation breaking text volume as an effort signal](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) and for [reverse compression](../notes/reverse-compression-is-when-llm-output-expands-without-adding.md). Relative to the [AI;DR discussion](./hacker-news-ai-dr-ai-didnt-read.ingest.md), which already captures effort-based triage and false positives from AI-associated style, Cymerys adds a temporal self-report: repeated low-yield encounters allegedly turn a noisy cue into automatic suppression, which then misses present information and causes extra back-and-forth. Its strongest conceptual comparison is the [credibility-erosion mechanism](../notes/quality-signals-for-kb-evaluation.md#credibility-erosion), where agents learn to discount all links after enough links fail to deliver. This cross-domain resemblance suggests a general channel-level failure mode, but the essay does not establish that either case shares a causal learning mechanism.

## Extractable Value

1. **Bad outputs can impose a channel-wide credibility externality** -- Once consumers learn that a family of surface cues predicts low return, every later item carrying those cues starts with a lower inspection prior. Better outputs can therefore lose attention because earlier failures damaged the channel, not because their own content was assessed. This is the novel synthesis beyond the existing artifact-level triage account. [deep-dive]

2. **The claimed training effect can be separated from static triage** -- A learned-suppression account predicts that the same reader's willingness to inspect cue-matched text changes with exposure history. A static effort heuristic predicts cue-based screening without that temporal change; generic overload predicts broader withdrawal not specific to AI-associated cues. Crossing text quality, surface style, disclosed provenance, and exposure history would distinguish these accounts and measure false negatives. [experiment]

3. **Reader filtering can externalize author savings into coordination work** -- Cymerys reports asking questions that the ignored document had answered, producing repeated exchanges for both parties. This identifies a team-level outcome to measure: authoring time saved, reader inspection time, missed-information rate, and follow-up cost together, rather than document production speed alone. [quick-win]

4. **The reported artifacts fail on separable dimensions** -- The examples distinguish reverse compression (a simple concept made verbose), draft-state leakage (exploratory uncertainty presented as settled requirements), domain contamination (technical architecture inserted into a marketing concept), and rhetorical miscalibration (routine details framed as breakthroughs). Treating all four as “AI style” hides the different checks needed to catch them. [quick-win]

5. **Misclassification does not erase the operational effect** -- The author does not verify that the documents were AI-generated, yet his inferred provenance still changes how he reads them. For workflow design, AI-detection accuracy and cue-driven reader behavior are separate questions: even a false attribution can produce real dismissal, while a correctly detected but well-reviewed artifact need not deserve it. [quick-win]

## Limitations (our opinion)

The essay is a sample of one based on retrospective diagnosis. It does not reproduce the documents, verify their provenance, compare similar human-written material, count exposures, or measure the change in attention it attributes to learning. The examples could reflect poor editing, weak document ownership, generic information overload, prior distrust of particular senders, or an ordinary decision to ration attention rather than conditioning caused by AI output.

The banner-blindness analogy names a recognizable shape but does not establish a shared mechanism. The essay's disagreement with research on human AI-text detection is unsupported by a citation or test, and its own examples concern conspicuous low-effort output rather than representative model-assisted writing. Surface cues can correlate with poor review in one environment while producing false positives elsewhere.

Finally, automatic suppression may save more inspection time than its false negatives cost. Missing useful content and causing follow-up work demonstrates a possible cost, not net harm. The source supports a conjecture about channel-wide credibility erosion; it does not establish its prevalence, causal origin, or total effect on productivity.

## Recommended Next Action

Write a conjecture note titled `Repeated low-yield outputs can train consumers to reject a cue-marked channel`. Generalize cautiously from this human-reading case and the KB's link-credibility-erosion case, connect it to [cheap generation breaks text volume as an effort signal](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md), and make exposure-dependent change, false-negative cost, and net inspection utility the discriminating tests against static triage and generic overload.
