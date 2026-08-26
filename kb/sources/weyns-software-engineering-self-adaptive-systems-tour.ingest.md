---
description: "Weyns's six-wave engineering perspective supplies a bounded self-adaptation vocabulary and a warning that MAPE-K is an engineering reference model, not a membership definition."
source: https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf
captured: "2026-07-21"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 6166fb55b965bc7e20549a4aa9a89c24579631c4ddd2bd890f79fd606340f267
ingested: "2026-07-21"
type: kb/sources/types/ingest-report.md
domains: [self-adaptation, feedback-loops, uncertainty, systems-engineering]
---

# Ingest: Software Engineering of Self-Adaptive Systems: An Organised Tour and Future Challenges

## Classification

A scholarly handbook chapter that synthesizes research traditions, defines a conceptual model, and identifies future engineering problems.
Author: Danny Weyns is a leading self-adaptive-systems researcher; this is a synthesis chapter rather than a controlled empirical study.

## Summary

Weyns defines self-adaptation through complementary external and internal principles: autonomous handling of change and uncertainty, plus a distinction between a managed system serving domain concerns and a managing system serving adaptation concerns. The four-element model (environment, managed system, adaptation goals, managing system) organizes six research waves: automating tasks, architecture-based adaptation, runtime models, goal-driven adaptation, guarantees under uncertainty, and control-based adaptation. MAPE-K is presented as one engineering pattern within this history. The chapter's central value for Commonplace is a disciplined separation between a feedback-loop architecture and the harder question of what qualifies as self-improvement or self-adaptation.

## Quotes

- **Source extract (verbatim):** The adaptation plan is then executed by theExecuteelement that adapts the managed element as needed. MAPE-K provides a reference model for a manag- ing system. MAPE-K’s power is its intuitive structure of the different functions that are involved in realising the feedback control loop in a self-adaptive system.
  - **Source location:** Section 3.1, Wave I: Automating Tasks

## Connections Found

The source is a technical anchor for [a proposal-selection loop requires search, evaluation, and retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): both treat loop decompositions as conceptual engineering models rather than category definitions. It also directly supports [real self-improving systems occupy combinations no single rung captures](../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md), whose profile separates architecture, allocation, and governance instead of collapsing them into one autonomy score. No durable note currently uses Weyns's six-wave vocabulary as an operational taxonomy.

## Extractable Value

1. **External/internal two-principle test for self-adaptation** -- gives a compact way to check whether an alleged improvement loop has both autonomous response to changing conditions and a discernible adaptation concern distinct from domain work. [quick-win]
2. **Four-element conceptual model (environment, managed system, goals, managing system)** -- supplies a reusable schema for locating where Commonplace's notes, validators, agents, and human reviewers sit in an update pathway. [quick-win]
3. **Six-wave chronology** -- separates task automation, architecture, runtime models, goals, uncertainty guarantees, and control theory so future notes can state which layer they rely on instead of calling every loop “MAPE-K.” [quick-win]
4. **Uncertainty as a first-class engineering concern** -- strengthens the current profile's coverage and oracle questions: improvement claims without an uncertainty boundary are underspecified. [experiment]
5. **Socio-technical allowance** -- the model explicitly permits human participation and decentralised managing systems, supporting Commonplace's human-inclusive system boundary rather than equating autonomy with unattended execution. [quick-win]

## Limitations (our opinion)

This is a conceptual synthesis, not a benchmark or comparative evaluation. The six waves are an author's organizing perspective and may hide cross-wave disagreement or alternative histories. The external/internal principles are useful scope criteria but do not provide a formal test for every adaptive or self-organising system. Examples are drawn from software engineering; transfer to an agent-operated knowledge base remains an inference. “Autonomous” is qualified as minimal human interference but is not operationalised with measurable thresholds.

The source snapshot was refreshed from the user's full converted Markdown capture; the classification, connections, and recommended action remain supported. No inbound KB links to this ingest report required updating.

## Recommended Next Action

Add a short “reference-model versus membership-test” paragraph to [a proposal-selection loop requires search, evaluation, and retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), citing this snapshot and preserving the distinction between MAPE-K-style engineering structure and the separate self-improvement membership test.
