---
description: "Production evidence for review-derived coding-agent rules, bounded by an instance-to-rule oracle gap and an uncontrolled, fixed-architecture deployment."
source_snapshot: "kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.md"
ingested: "2026-08-02"
type: kb/sources/types/ingest-report.md
domains: [deploy-time-learning, agent-memory, evaluation, software-engineering]
---

# Ingest: Self-Improving AI Coding Agents Through Accumulated Behavioral Rules

Source: [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](./self-improving-ai-coding-agents-through-accumulated-rules.md)
Captured: 2026-08-02
From: https://arxiv.org/html/2607.13091v1?utm_source=chatgpt.com

## Classification

Genre: scientific-paper -- an arXiv preprint that defines a framework, reports observational deployment data, and situates the work against cited research.
Domains: deploy-time-learning, agent-memory, evaluation, software-engineering
Author: Aditya Aggarwal and Nahid Farhady Ghalaty report first-hand results from their own deployment; the preprint supplies methods and counts but no independent replication or controlled comparison.

## Summary

The paper proposes turning each accepted, generalizable code-review comment into a persistent behavioral rule in a version-controlled instruction file, then loading that file across coding-agent interfaces and running a self-review checklist before submission. In one four-week microservices deployment, the authors report growth from 5 to 18 behavioral rules plus 15+ code standards and a 15-item checklist, zero recurrences across nine tracked error classes and 74 post-rule session-exposures, and cross-repository or cross-tool transfer in 9 of 15 documented learning events. The architecture is a concrete readable-artifact learning loop, but the study has no no-rule or static-instruction control, and its evidence does not separately test immediate rule promotion, uniform always-loading, or monotonic accumulation.

## Connections Found

The source is an observational production anchor for [Deploy-time learning is the missing middle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [Constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md), and [Activate Behavior-Changing Memory Before The Mistake](../notes/agent-memory-requirements/activate-behavior-changing-memory.md): accepted feedback becomes a durable instruction artifact that is present before later actions and reportedly changes cross-session behavior. Its more important local role is a counterpoint to [An accepted edit verifies the change, not the rule](../notes/an-accepted-edit-verifies-the-change-not-the-rule.md). The paper promotes a correction after an engineer judges it generalizable, while the KB separates acceptance of the corrected instance from verification of the extracted rule. [Synapptic](../agent-memory-systems/reviews/synapptic.md) supplies the closest alternative lifecycle because it tests individual guards with WITH/WITHOUT comparisons and can exclude redundant or harmful rules. The source also compares with [Figma's agent security review account](./figma-agent-security-review-thread-2081739292859421118.ingest.md), where review-derived precedents are coupled to an explicit evaluation corpus and precision-improvement process.

## Extractable Value

1. **Readable behavioral rules are a plausible cross-session learning substrate in production coding work.** The reported zero recurrences across nine tracked classes and 74 post-rule exposures are useful feasibility evidence for deploy-time learning through system-definition artifacts, provided the result remains explicitly local and observational. [quick-win]
2. **Accepted review feedback is a strong capture signal but not a rule-level promotion oracle.** The framework's decisive step generalizes one accepted correction into future policy using engineer judgment alone; this makes the deployment a concrete test case for the KB's instance-versus-rule distinction and for adding independent effectiveness, redundancy, harm, and rollback checks. [deep-dive]
3. **Shared instruction files can transfer behavior across agent interfaces without specialized memory infrastructure.** Two heterogeneous agent surfaces consumed the same version-controlled rules, illustrating portability through a common natural-language representation; the paper does not isolate representation from shared loading or other deployment factors. [quick-win]
4. **Structural validation protects the container, not the semantic rule set.** Frontmatter, required-section, freshness, and file-presence checks can prevent malformed growth, but they cannot establish that a generalized rule is correct, non-conflicting, appropriately scoped, or beneficial. The reported manual conflict is evidence that semantic governance remains outside the validator. [quick-win]
5. **Behavioral consistency over time is a useful evaluation axis distinct from one-shot task success.** The proposed benchmark shape—correction-producing seed tasks followed by cross-session recurrence probes—could complement static coding benchmarks and directly test whether behavior-changing memory activates before repeated mistakes. [experiment]
6. **Monotonic rule growth exposes a lifecycle and context-budget contradiction.** The paper celebrates append-friendly accumulation while acknowledging a ~6,250-token always-loaded file, a real conflict, and future saturation; this supports treating retirement, scoping, routing, and rollback as first-class operations rather than optional future cleanup. [deep-dive]

## Limitations (our opinion)

The study does not support causal claims about the framework. It observes one team, one primary typed-language environment, two agent interfaces, four weeks, and 11 sessions without a no-rule, static-rule, or alternative-memory baseline. The “shift” toward design-level review is reported from a post-deployment category distribution without a captured pre-deployment comparison, and 74 session-exposures are not shown to be independent or equally capable of triggering each error. The claim that human reviewers are the highest-quality source follows from their 39% share of collected rules, but prevalence does not measure quality.

The fixed-decomposition boundary is also consequential. Behavior could condition on accepted review comments, production errors, prior rules, checklists, and task logs; maintainers could append or refine rule text, extend checklists, and resolve conflicts. The update space did not vary the Markdown rule representation, always-loaded delivery, source taxonomy, abstraction heuristic, review culture, semantic retrieval, retirement policy, or human decision about whether a comment generalizes. Improvement inside that space therefore shows that the compound setup was workable, not that those fixed choices were necessary or preferable. As [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, the experiment cannot repair or evaluate omissions outside its admitted operations. Finally, structural workspace validation cannot detect false or over-generalized rules, and monotonic retention risks amplifying reviewer mistakes, conflicts, and context dilution.

## Recommended Next Action

Update [An accepted edit verifies the change, not the rule](../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) with this snapshot as an `evidenced-by` deployment case, contrasting the paper's immediate promotion heuristic with Synapptic's rule-level ablation and exclusion lifecycle.
