---
source: https://arxiv.org/html/2603.10165v1
description: Framework that converts live next-state signals (user replies, tool outputs, terminal feedback, GUI state) into RL rewards and token-level supervision, enabling a single policy to personalize and improve on agentic tasks simultaneously.
captured: 2026-03-14
capture: web-fetch
type: academic-paper
---

# OpenClaw-RL: Train Any Agent Simply by Talking

Author: Yinjie Wang, Xuyang Chen, Xiaolong Jin, Mengdi Wang, Ling Yang
Source: https://arxiv.org/html/2603.10165v1
Date: 2026-03-10

## Abstract

This paper introduces OpenClaw-RL, a framework that leverages next-state signals—user replies, tool outputs, terminal feedback, or GUI state changes—as live learning sources for training agents. Rather than discarding this data, the system recovers two types of information: evaluative signals (how well an action performed) converted to scalar rewards via process reward models, and directive signals (how actions should differ) extracted through Hindsight-Guided On-Policy Distillation providing token-level supervision.

## Key Innovation

The framework recognizes that "next-state signals are universal" across personal conversations, terminal executions, GUI interactions, software engineering tasks, and tool-call traces. A single policy can learn simultaneously from all these interaction types using an asynchronous, fully decoupled architecture.

## Core Components

**Infrastructure:** Four independent asynchronous loops handle policy serving (SGLang), environment management, PRM judging, and training (Megatron) with zero coordination overhead.

**Binary RL:** Majority-vote PRM evaluation produces process rewards (+1, -1, 0) for each action based on environmental feedback.

**Hindsight-Guided OPD:** Extracts concise, actionable hints from next states, augments prompts with these hints, and computes per-token advantages by comparing hint-informed and base policy log-probabilities.

## Experimental Results

**Personal Agents:** Combined binary RL and OPD methods achieve significant personalization gains. A student agent learns natural writing style within 36 interactions; a teacher agent develops friendlier feedback within 24 interactions.

**General Agents:** The same infrastructure supports terminal, GUI, SWE, and tool-call settings. Integrating process and outcome rewards outperforms outcome-only training, though at increased computational cost.

## Significance

The work unifies previously separate training pipelines into one framework where "a model simultaneously personalizes to individual users and improves at long-horizon agentic tasks, trained entirely from interactions it is already having."
