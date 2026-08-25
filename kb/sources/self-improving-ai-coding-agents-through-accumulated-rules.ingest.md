---
description: "Production evidence for review-derived coding-agent rules, bounded by an instance-to-rule oracle gap and an uncontrolled, fixed-architecture deployment."
source: https://arxiv.org/html/2607.13091v1?utm_source=chatgpt.com
captured: "2026-08-02"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 485cd1c053eef5f1717c2c6309d109500b0dfa1564efb9d8b347a438923684ff
ingested: "2026-08-02"
type: kb/sources/types/ingest-report.md
domains: [deploy-time-learning, agent-memory, evaluation, software-engineering]
---

# Ingest: Self-Improving AI Coding Agents Through Accumulated Behavioral Rules

## Classification

An arXiv preprint that defines a framework, reports observational deployment data, and situates the work against cited research.
Author: Aditya Aggarwal and Nahid Farhady Ghalaty report first-hand results from their own deployment; the preprint supplies methods and counts but no independent replication or controlled comparison.

## Summary

The paper proposes turning each accepted, generalizable code-review comment into a persistent behavioral rule in a version-controlled instruction file, then loading that file across coding-agent interfaces and running a self-review checklist before submission. In one four-week microservices deployment, the authors report growth from 5 to 18 behavioral rules plus 15+ code standards and a 15-item checklist, zero recurrences across nine tracked error classes and 74 post-rule session-exposures, and cross-repository or cross-tool transfer in 9 of 15 documented learning events. The architecture is a concrete readable-artifact learning loop, but the study has no no-rule or static-instruction control, and its evidence does not separately test immediate rule promotion, uniform always-loading, or monotonic accumulation.

## Quotes

- **Source extract (verbatim):** 1. The agent generates or modifies code in response to a task. 2. The agent executes its self-review checklist before presenting the code. 3. A human reviewer examines the code and provides feedback. 4. For each accepted comment that identifies a generalizable class of mistake (not a one-off typo), a new rule is added to the instruction file. 5. The updated instruction file is loaded in all subsequent sessions, preventing recurrence.
  - **Source location:** Section II-C, Feedback-to-Rule Loop.
- **Source extract (verbatim):** Who decides whether a comment represents a class of mistake versus a one-off issue? The engineer who receives the review feedback makes this judgment. The heuristic is: “Would this mistake plausibly recur in a different context?” If yes, it becomes a rule.
  - **Source location:** Section II-D, Rule Lifecycle and Governance.
- **Source extract (verbatim):** Deployment context: A microservices platform with 35+ services, 13 custom agent definitions, 10 operational skills, and 6 shared knowledge documents. Two agent interfaces consumed the same shared instruction file.
  - **Source location:** Section IV-A, Experimental Setup.
- **Source extract (verbatim):** Second, accumulated rules suppress the recurrence of previously-corrected error classes within the observation window. Across 9 tracked error classes and 74 cumulative post-rule session exposures, no recurrences were observed. We deliberately frame this as an observational result: it establishes that the suppression effect is large enough to be visible inside a four-week deployment without a controlled baseline, but it is not equivalent to a statistical guarantee.
  - **Source location:** Section V-A, Summary of Findings.
- **Source extract (verbatim):** Lack of controlled baseline or ablation: We do not have a parallel control group, and we did not run a paired ablation comparing the framework against static prompt engineering or a no-rule baseline on the same task stream. The suppression and review-shift results should therefore be read as initial empirical evidence, not as a causal proof.
  - **Source location:** Section VIII, Limitations and Threats to Validity.
- **Source extract (verbatim):** The critical property is that the file is append-friendly and monotonically growing. Rules are added and occasionally refined but rarely removed, accumulating the team’s collective engineering judgment over time.
  - **Source location:** Section II-A, The Structured Instruction File.
- **Source extract (verbatim):** When is an existing rule refined instead of adding a new rule? When a new review comment reveals that an existing rule is too broad or too narrow, the existing rule is updated in place. The rule ID is preserved; the constraint text is sharpened.
  - **Source location:** Section II-D, Rule Lifecycle and Governance.
- **Source extract (verbatim):** 1. Monotonic growth: Rules are added and refined but not removed, echoing the continuous improvement principle in DevOps practice [9].
  - **Source location:** Section VII, Design Principles.

## Connections Found

The source is an observational production anchor for [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [Constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md), and [Activate Behavior-Changing Memory Before The Mistake](../notes/agent-memory-requirements/activate-behavior-changing-memory.md): accepted feedback becomes a durable instruction artifact that is present before later actions and reportedly changes cross-session behavior. Its more important local role is a counterpoint to [An accepted edit verifies the change, not the rule](../notes/an-accepted-edit-verifies-the-change-not-the-rule.md). The paper promotes a correction after an engineer judges it generalizable, while the KB separates acceptance of the corrected instance from verification of the extracted rule. [Synapptic](../agent-memory-systems/reviews/synapptic.md) supplies the closest alternative lifecycle because it tests individual guards with WITH/WITHOUT comparisons and can exclude redundant or harmful rules. The source also compares with [Figma's agent security review account](./figma-agent-security-review-thread-2081739292859421118.ingest.md), where review-derived precedents are coupled to an explicit evaluation corpus and precision-improvement process.

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
