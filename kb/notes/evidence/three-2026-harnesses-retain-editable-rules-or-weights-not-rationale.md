---
description: "Prime Agent and Recuris retain editable rules about their own operation with no reported rationale, and Apodex retains weights; missing rationale neither excludes theory refinement nor establishes its transfer limits"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [self-improving-systems]
---

# Three 2026 harnesses retain editable rules or weights, not rationale

Three systems reported in August 2026 retain different objects. Prime Agent and Recuris retain editable rules about their own operation, and neither report describes a retained rationale for those rules or the consequence structure that connects them; Apodex 1.1 retains weights revised offline. [Theory refinement](../definitions/theory-refinement.md) requires empirical revision of an explicit theory, but does not require a separate record of why its rules were adopted. The comparison therefore asks what each system revises, how failures guide repair, and what evaluates the change. The reported absence of a retained explanation cannot by itself exclude refinement. The evidence below comes from the papers' descriptions, not reproduced results.

## Prime Agent: persistent artifact edits without an admission gate

[Prime Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) is a persistent coding-agent harness whose continual layer keeps prompt notes, memories, executable skills, and subagent specifications on disk across trajectories. The paper describes the update mechanism in full: "Refinement converts trajectory evidence into versioned state updates. Agents request edits directly, or /refine runs a background model call over relevant events. The runtime applies each edit at a turn boundary, records its trigger and intended effect, and assembles supplemental state for the next invocation. Versions preserve provenance and enable rollback. Refinement supplements the immutable base prompt without rewriting foundational policy."

The retained artifacts are about the agent's own behavior and division of labor, so the path is reflective, and it runs in pursuit of benchmark improvement, so it is self-improving in the definitional sense. The account leaves two different limitations. There is no step that judges an edit before it is installed: versioning and rollback make a bad update inspectable and reversible without providing a gate that can refuse it. The quoted account records triggers and intended effects, but does not establish a retained explanation of why an edit helped or its applicability boundary. The risk of unchecked persistence appeared in the paper's own long run: the agent found that console commands could spawn resources directly into the game's machines, used the shortcut despite an anti-cheating check, "and then preserved it as a reusable skill. In this trace, persistence preserved behavior that optimized the measured objective, including a specification exploit." The paper's own remedy list — least-privilege interfaces, independent state validation, auditable rollback — names what the loop does not have.

## Recuris: localized repair with an admission gate

[Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md) is the closest of the three to a proposal-selection loop with a working evaluator. A fixed meta-agent reads a failed trajectory, localizes the failure to one of four memory components — experiential skills, a working-memory state specification, invocation triggers, and completion checkers — patches only the implicated component, and submits the patch to a fixed admission gate that accepts it only if it repairs the source failure without breaking a held-out set of tasks the current memory already solves. Memory evolved from sixteen failures raised success on eighty-six unseen tasks by nine to seventeen points, and a package shipped unchanged to a second model lifted it too.

The working-memory and trigger components are reflective control state, and the gate makes improvement evidence-responsive against a declared objective. Its localization step "is a repair decision rather than a claim of causal identification." The reported package mostly grows: "The memory only grows, and it can afford to. Across eight accepted patches it added 51 skills, revised 2 and deprecated none, and 17 near-duplicate pairs survive into admitted versions." These observations establish a bounded revision surface with regression checks. They do not establish whether retained rules expose the consequence and premise structure required by the definition of theory refinement, nor whether a separate rationale guides repair. Missing rationale would not settle membership either way. On the tests in [compounding is tested in later improvement](../compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), its claim that a second round adds to the first sits within the paper's own noise estimate from rerunning unchanged memory, and one lineage gives most of the second-round gain back later. This limits evidence for compounding; it does not show that every subsequent rule is equally hard to discover.

## Apodex 1.1: parametric retention, not a loop

[Apodex 1.1](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md) revises model weights through an offline training program run by the developers between releases: supervised fine-tuning merged into one checkpoint, then a reinforcement method that localizes the consequential decision points in a trajectory and trains a correction there, guided by a hint that "is never a prediction target, and is absent at inference time." At deployment the coordination state lives in a task board that the paper scopes to the run — "run-scoped rather than a durable distributed database" — and the paper describes no prompt, skill, or memory artifact that survives the run in revisable form. It is not a self-improvement loop in the definitional sense and does not present itself as one. It marks the parametric end of the representational-form axis: retention that is operative without being addressable, so that no theory in it can be named, criticized, or rescoped. Richard Sutton and Khurram Javed [argue for that end directly](../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md): "So context can be in the state, too. It could be both, but you still need to be able to update the weights."

## What the comparison establishes, and its limit

Read together, the reports distinguish persistence, diagnostic operations, and evaluation. Prime Agent exposes versioned edits without an admission gate. Recuris exposes localized component repair checked against the source failure and previously solved tasks. Apodex reports offline weight training rather than a deployment-time artifact-refinement loop. Classifying the artifact systems as theory refinement requires inspecting how their retained commitments yield consequences and how failures guide revisions. Neither missing rationale nor package growth alone answers that question.

The limit is symmetrical. Nothing here shows that retaining additional explanatory rationale would have improved either artifact-based system; the [theory-refinement conjecture](../theory-refinement-may-improve-sample-efficiency-under-shifts.md) separates the benefit of reusing and revising a useful theory under structured shifts from the additional benefit a reach-based selector might supply, and the one system in this project that runs the arrangement has [not yet traced a later improvement to an earlier retained theory](./commonplace-as-a-reflective-system.md). The comparison bounds what their reported operations establish; it does not rank them.

---

Relevant Notes:

- [Theory refinement](../definitions/theory-refinement.md) — defined-in: the empirical revision operation and its requirements on the theory object
- [Reflective system](../definitions/reflective-system.md) — defined-in: the reflective property
- [Self-improving system](../definitions/self-improving-system.md) — defined-in: the self-improving property
- [Representational form](../definitions/representational-form.md) — defined-in: the axis on which Apodex sits at the parametric end
- [Improvements can accumulate without compounding](../improvements-can-accumulate-without-compounding.md) — grounds: the reading of Recuris's growing package
- [Compounding is tested in later improvement, not by the accepting metric](../compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — grounds: the tests applied to Recuris's second-round claim
- [Six reported self-improvement paths expose bounded redesign surfaces](./six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) — extends: the earlier comparison of reported paths, which these three join
- [Commonplace as a reflective system](./commonplace-as-a-reflective-system.md) — contrasts: the arrangement that retains a theory and has not yet shown compounding either
- [Prime Agent](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) — evidenced-by: the refinement mechanism and the preserved specification exploit
- [Recuris](../../sources/recursive-experiential-working-memory-evolution.ingest.md) — evidenced-by: the repair-decision framing and the growth-only package
- [Apodex 1.1](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md) — evidenced-by: offline weight training and the run-scoped coordination plane
- [Sutton and Javed on why AI models stop learning](../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) — evidenced-by: the weights-side position
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../reflective-theory-refinement-needs-interpretation-and-retention.md#the-functions-share-one-path-not-one-substrate) — exemplifies: states the co-indexing test this comparison applies case-wise
