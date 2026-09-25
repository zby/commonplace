---
description: "Formalizes program quality relative to a machine and task environment, with bounded-optimal constructions for restricted real-time agent classes"
source: https://arxiv.org/abs/cs/9505103
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: aa67cc94c396a3c5f090073d9fd0de36336404e9a79f028eb7ccf673eee26da6
ingested: "2026-09-17"
occasion: "Evaluating a program relative to architecture and environment rather than an ideal reasoner; which classes the results cover."
learning_claims: true
type: ingest-report
domains: [bounded-optimality, agent-evaluation, real-time-systems, learning-theory]
---

# Ingest: Provably Bounded-Optimal Agents

## Classification

This is a scientific paper that defines bounded and asymptotic bounded optimality, proves construction results for specified program, architecture, and task-environment classes, and illustrates them with a modeled mail-sorting system. Author: Stuart Russell and Devika Subramanian are academic AI researchers developing the formal framework and its proofs; the paper was published in the *Journal of Artificial Intelligence Research*.

## Summary

Russell and Subramanian replace evaluation against an ideal action-selecting reasoner with optimization over programs executable by a specified architecture in a specified task environment. They define a program as bounded optimal when no other program in the architecture's language has greater expected utility over the environment class, then construct optimal sequences of decision procedures for restricted episodic real-time environments with fixed costs, fixed deadlines, or stochastic deadlines. They also derive a learning bound for approximately bounded-optimal programs within an agnostically learnable rule language and introduce asymptotic bounded optimality, including universal programs for families of time-dependent utility functions under further architectural conditions. The result is a precise basis for system-relative evaluation, but every optimality claim inherits the declared program language, machine, utility, environment class, and asymptotic comparison.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical basis for [treating the deployed system rather than the model alone as the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): value belongs to a program running on an architecture in a task environment, so the evaluated unit includes the machinery that turns computation into timely action. It also provides a formal comparison case for [warranted autonomy being bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) and for [methodological and computational closure tracking different changes](../notes/methodological-and-computational-closure-track-different-changes.md). In each case, the conclusion is only as broad as the declared architecture, environment class, objective, resource model, and horizon. Its role is therefore an anchor for architecture-and-environment-relative program evaluation, with explicit limits on which classes the proofs cover.

## Learning Claims (our opinion)

The paper's learning mechanism observes episodic interactions and their utilities, learns one decision procedure for each runtime class from a finite agnostically learnable language, estimates each procedure's quality, and then uses a fixed constructor to arrange the learned procedures. Theorem 7 bounds the resulting program's utility deficit relative to the best sequence available within those runtime-indexed classes, subject to the stated probability and estimation bounds. This is learning of program components and their selection values, not theory refinement: it does not revise an existing explicit theory with separately editable commitments.

The effective update space is narrow and explicit. Training episodes and utility values are the conditioning evidence; learned decision procedures recommend external actions; the hypothesis class contains programs in the fixed languages indexed by runtime; and the architecture, runtime partition, sequential composition rule, episodic decomposition, utility regime, and—in the proved setup—runtimes and deadline distribution remain fixed. Convergence inside this space supports approximately bounded-optimal selection among expressible procedures. It does not establish that the fixed signals, response basis, runtime classes, or sequence architecture are the best decomposition for the task.

## Extractable Value

1. **Use program-relative value as the evaluation primitive** -- Comparing `V(l, M, E)` makes the architecture and environment part of the proposition, preventing an ideal reasoner's unattainable behavior from serving as the operative baseline. [quick-win]
2. **Report the quantified class with every optimality result** -- The strict constructions cover sequences of decision procedures on a simple sequential architecture in episodic real-time environments under fixed-cost, fixed-deadline, or stochastic-deadline regimes; they do not establish optimality for arbitrary agent programs or environments. [quick-win]
3. **Separate strict, asymptotic, and universal claims** -- Strict bounded optimality maximizes within one architecture language and environment distribution, ABO permits constant-factor machine augmentation beyond an environment-complexity threshold, and UABO ranges over a family of value functions while retaining architecture and environment-class conditions. [deep-dive]
4. **Treat learning bounds as relative to a fixed effective update space** -- The approximately bounded-optimal result compares learned procedures with the best procedures in runtime-bounded hypothesis classes and leaves the surrounding architecture and decomposition untested. [quick-win]
5. **Retain the mail sorter as an illustration rather than the proof's scope** -- Its modeled performance comparisons show how the constructions behave under selected rule-quality and arrival distributions, while the formal claims depend on the assumptions stated in the theorems. [just-a-reference]

## Limitations (our opinion)

The central formal move is strong but conditional: bounded optimality becomes meaningful only after the program language, architecture, utility, and environment distribution or class are fixed. The strict construction uses simple agents composed from decision procedures and restricted stationary episodic real-time environments. The learning result further assumes finite agnostically learnable runtime-indexed languages and initially treats rule runtimes and deadline distributions as known. The UABO results require particular architecture operations, suitable component programs, restricted families of time-dependent value functions, and constant-factor machine speedups; “universal” does not mean independent of the architecture or environment class.

The mail-sorting results are generated from a modeled setup and selected quality and arrival distributions. They illustrate behavior within that decomposition, including a reported advantage for sequences, but do not compare alternative percept representations, action bases, program languages, architectures, or task decompositions. The paper therefore supports the formal framework and the stated within-class results, not a general empirical claim that its decomposition is best for deployed agents.

## Recommended Next Action

Update [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) to use bounded optimality as the formal basis for stating that a program's evaluation claim must name its architecture, task-environment class, objective, and resource model.
