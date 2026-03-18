---
source: https://arxiv.org/html/2603.15381v1
description: Dupoux, LeCun, and Malik argue current AI externalizes learning into human-run MLOps, then propose an A-B-M architecture where observation learning, action learning, and a meta-control plane are integrated for lifelong adaptation.
captured: 2026-03-18
capture: web-fetch
type: academic-paper
---

# Why AI systems don't learn and what to do about it

Author: Emmanuel Dupoux, Yann LeCun, Jitendra Malik
Source: https://arxiv.org/html/2603.15381v1
Date: March 16, 2026

## Abstract

This paper argues that current AI systems do not learn autonomously after deployment because learning has been externalized into a human-managed MLOps pipeline. The authors propose an architecture inspired by cognitive science that combines learning from observation (System A), learning from action (System B), and a meta-control layer (System M) that routes information, switches learning modes, and modulates rewards and objectives. They frame this as a roadmap toward agents that adapt from raw experience in open-ended environments rather than through periodic retraining by experts.

## Core Thesis

The paper's central claim is that present-day AI is powerful at offline optimization but structurally incapable of autonomous, lifelong adaptation. Human and animal learners do not merely optimize a fixed objective on a fixed dataset; they choose what to attend to, decide when to observe versus act, and adjust learning behavior based on internal signals like uncertainty, novelty, and error. The authors argue that these missing capabilities, not just larger datasets or more compute, are the main reason deployed AI systems fail to learn in the wild.

## Proposed Architecture

### System A: Learning from Observation

System A covers passive or observational learning: self-supervised learning, predictive modeling, representation learning, and multimodal world modeling. Its strength is scalable abstraction from data streams; its weakness is dependence on human-specified datasets, task generators, and training objectives.

### System B: Learning from Action

System B covers interactive learning: reinforcement learning, planning, adaptive control, and search over action sequences. Its strength is grounded adaptation through interaction; its weakness is sample inefficiency and difficulty handling rich, real-world environments.

### System M: Meta-Control

System M is the paper's distinctive addition. It functions as a control plane over the other systems, monitoring low-dimensional meta-signals such as uncertainty, prediction error, novelty, trust, or somatic state, then choosing meta-actions such as:

- selecting or filtering inputs
- modulating rewards, losses, and curricula
- switching between learning and inference modes
- routing data between Systems A, B, and episodic memory

The authors explicitly compare this to a software-defined networking control plane: System M does not process the high-bandwidth task stream directly, but dynamically assembles and disassembles learning pipelines.

## Interaction Between Systems

The paper argues that observation and action learning should not remain separate paradigms. System A can help System B by compressing state spaces, building predictive world models, and generating intrinsic rewards for exploration. System B can help System A by collecting better data, disambiguating perception through intervention, and generating task-relevant trajectories rather than passive, uncurated streams. System M sits above both, deciding when and how these interactions should occur.

## Bootstrapping Problem

The hardest problem is initialization. If System A needs action-generated data to learn grounded representations, and System B needs structured representations to act efficiently, then neither cleanly bootstraps the other. The paper proposes an evolutionary-developmental framing: an outer loop shapes priors, curricula, and meta-control policies, while an inner developmental loop lets the agent adapt within its environment. The authors treat current research practice itself as a crude substitute for this outer loop.

## Why This Matters

The paper claims autonomous learning would make AI more robust in non-stationary environments, less dependent on fixed pretraining distributions, and better suited to real-world deployment. It also presents autonomous learners as scientific instruments: building them could sharpen theories of animal and human cognition.

## Challenges and Open Problems

The authors identify three major obstacles:

1. integrating siloed learning paradigms such as self-supervised learning and reinforcement learning
2. building a unified meta-control architecture that automates data routing, objective shaping, and learning-mode arbitration
3. training these systems in realistic but efficient environments with suitable benchmarks for learning speed and adaptation

They also flag alignment and governance issues: more autonomous learners raise harder problems around controllability, proxy-signal hacking, over-trust, and possibly moral status if bodily or pain-analogous signals become functionally important.

## Conclusion

The paper is a conceptual roadmap rather than a concrete implementation. Its main contribution is reframing "AI that keeps learning after deployment" as an architectural problem: autonomous learning requires an integrated control plane over observation, action, memory, and internal meta-signals, not just better fine-tuning recipes or more inference-time compute.

---

**License:** CC BY 4.0
