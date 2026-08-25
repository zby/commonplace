---
description: "Trace evidence that coding agents explicitly use instruction files and working notes heavily, while documentation-to-action and validation links remain unresolved"
source: https://arxiv.org/abs/2608.20195
captured: "2026-08-24"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: ed5ac4797ee35f236a62d10526e62b33f9765692ddcbff55ca0b634587bd4766
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [coding-agents, agent-documentation, context-engineering]
---

# Ingest: From Agent Behaviour to Agent-Friendly Documentation

## Classification

This scientific preprint reports an observational trace study over two public datasets, with separate process and artifact analyses rather than a controlled documentation intervention. Author: Zhijun Gao and Jing Chen of Peking University; the authors provide detailed operational definitions, uncertainty estimates, and a public replication package, but the captured source is an arXiv v1 preprint rather than a peer-review record.

## Summary

Across 557 coding-agent sessions with 3,033 classified documentation interactions and 33,097 agentic pull requests, the paper finds that agent instruction files and agent working notes dominate observed repository-local documentation activity, while API references and troubleshooting guides are rare. Explicit consultation most often leads to more reading or reasoning; its association with code editing changes between unadjusted and stage-adjusted models, testing and building are less frequent in the next three events, and no event matches the paper's explicit documentation-based validation pattern. Agents also produce documentation at 0.87 times the consultation rate, and code precedes documentation much more often than the reverse when commit order is observable. The paper is useful as behavior-side evidence for what agents explicitly touch and when, but not as causal evidence that prioritizing a documentation genre or making prose more executable improves task outcomes.

## Quotes

- **Source extract (verbatim):** Two verification actions are less frequent within the next three events and both survive adjustment: running a test (lift 0.23, cluster CI 0.08–0.45; adjusted OR 0.39 [0.25, 0.60]) and building (0.15, CI 0.02–0.33; OR 0.25 [0.14, 0.44]).
  - **Source location:** Section 4.2.2, "Actions following consultation," and Table 3.
- **Source extract (verbatim):** We therefore treat the lower frequency of test and build activity as the finding, and any consultation-to-authoring or consultation-to-code coupling as unresolved by these data.
  - **Source location:** Section 4.2.2, interpretation of Table 3.
- **Source extract (verbatim):** Transition probabilities are first-order. A near-zero adjacent transition from documentation read to code edit does not preclude longer-range influence.
  - **Source location:** Section 7.2, "Internal validity."

## Connections Found

The paper is an empirical anchor for [Human-LLM differences are load-bearing for knowledge system design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md): within its observable slice, coding agents concentrate documentation activity on agent-facing artifacts rather than the human-centered genres emphasized by prior research. It also supplies bounded evidence for the context-to-action gap in [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), because explicit reads do not produce a consistent immediate implementation-and-validation sequence. As a measurement counterpoint to [Context Engineering for AI Agents in Open-Source Software](./context-engineering-ai-agents-oss.ingest.md) and [Harness-IF](./harness-if-instruction-following-across-instruction-surfaces.ingest.md), it occupies the explicit-consultation layer between artifact presence and instruction compliance; none of those measurements alone establishes downstream task benefit. Its broad working-note category also compares with [Active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md), which requires lifecycle properties that path-based prevalence cannot establish.

## Extractable Value

1. **A staged evaluation ladder for agent-facing documentation** -- Artifact presence, automatic or explicit exposure, behavioral uptake or rule compliance, and downstream task effect are distinct measurements; combining them would prevent consultation counts from being mistaken for effectiveness. [quick-win]
2. **Behavior-side evidence for a distinct agent documentation audience** -- Instruction files and working notes account for 60.5% of pooled interactions and 55.1% after agent reweighting, supporting audience-specific KB design while keeping the exact share tied to this corpus and classifier. [quick-win]
3. **A bounded context-to-action gap** -- The adjacent read-to-code transition is nearly absent, the three-event code-edit association changes under adjustment, and immediate testing and building remain lower, so exposure and implementation should be evaluated separately. [quick-win]
4. **Working notes are a substantial but ungoverned maintenance surface** -- Plans, brainstorms, thoughts, and verification logs form a large observed category, but the study measures neither their lifecycle nor their staleness; this creates a focused comparison point for active-work-state designs. [deep-dive]
5. **Trace instrumentation can manufacture cross-agent differences** -- Shell-embedded paths and non-string tool outputs materially changed extraction coverage, while automatically loaded context remained invisible; agent-documentation evaluations need explicit visibility audits before comparing harnesses. [just-a-reference]
6. **Executable documentation is an intervention hypothesis** -- The absence of an observed prose-as-oracle sequence motivates a controlled comparison of prose, runnable examples, schemas, and tests, but the observational data do not establish that executability causes better verification. [experiment]

## Limitations (our opinion)

Our opinion: the source supports descriptive claims about explicit repository-local behavior, not causal documentation guidance. SWE-chat is opt-in telemetry dominated by one agent family, AIDev covers public early-adopter repositories, and the two datasets represent complementary rather than matched populations. Automatic startup injection, browser use, model-weight knowledge, docstrings, inline comments, and model-internal use are outside the observation surface, so instruction-file reads are lower bounds on exposure and a missing trace is not evidence of no influence.

The study's effective evidence space is fixed around repository paths, short event histories, a 20-symbol event alphabet, document categories, stage and trigger heuristics, and preselected statistical contrasts. Its operations can label, count, sequence, and compare only events represented in that scheme; no downstream model can recover an automatically injected instruction or latent reasoning step that the trace omitted. As [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, stable estimates inside those choices do not validate the fixed decomposition. In particular, zero validation events means zero matches for the defined read-then-test/build pattern, not the absence of all validation.

The 25.1% working-note result is especially provisional because the category emerged from language-model classification of ambiguous paths without human validation. The paper also uses “actionability” for a read-to-action document property, not the operator-relative relation defined by [Actionable methodology](../notes/definitions/actionable-methodology.md), and its observational zero does not test the cross-form prediction in [The verifiability gradient](../notes/verifiability-gradient.md). These vocabulary and measurement differences rule out importing the paper's negative findings as refutations of either Commonplace claim.

## Recommended Next Action

Update [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) with a staged evaluation ladder that distinguishes artifact presence, automatic or explicit exposure, instruction uptake or compliance, and downstream task effect, using this paper only for bounded explicit-consultation evidence.
