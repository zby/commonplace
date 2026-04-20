---
source: https://arxiv.org/html/2603.25723
description: "Proposes externalizing agent control logic (contracts, roles, stages, failure taxonomy) as portable natural-language artifacts (NLAHs) with an Intelligent Harness Runtime, evaluated on SWE-bench and OSWorld — key finding: explicit structure helps only when it tightens alignment with evaluator acceptance criteria."
captured: 2026-03-28
capture: web-fetch
type: snapshot
tags: [academic-paper]
---

# Natural-Language Agent Harnesses

Author: Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng
Source: https://arxiv.org/html/2603.25723
Date: March 26, 2026

## Abstract

The paper introduces Natural-Language Agent Harnesses (NLAHs) and an Intelligent Harness Runtime (IHR) to externalize agent control logic as executable, portable artifacts. Rather than burying harness design in controller code, this approach exposes orchestration patterns through structured natural language bound to explicit contracts and durable artifacts.

## Core Contribution

Modern agents increasingly succeed or fail based on their surrounding "harness"—the control stack managing multi-step reasoning, tool use, memory, and verification. The authors argue that harness logic should become "a first-class research artifact rather than incidental glue" by making it explicit, comparable, and ablatable.

## Key Components

**NLAHs expose:**
- Contracts (inputs, outputs, validation gates, retry rules)
- Roles (solver, verifier, researcher, orchestrator)
- Stage structure (plan → execute → verify → repair)
- Adapters and scripts (deterministic hooks for tests, retrieval)
- State semantics (artifact persistence across steps)
- Failure taxonomy (named recovery modes)

**IHR features:**
- In-loop LLM interpreting harness logic directly
- Separation of shared runtime charter from task-specific logic
- Agent calls bounded by explicit execution contracts
- File-backed state module for durability under context truncation

## Experimental Evidence

Evaluations on SWE-bench Verified and OSWorld examined:

1. **RQ1 (Behavioral Effect):** Process metrics changed significantly; most SWE instances showed concentrated effects on frontier cases rather than uniform improvement

2. **RQ2 (Module Ablation):** Self-evolution tightened solve loops; file-backed state improved auditability; verifier and search added structure but sometimes diverged from benchmark acceptance criteria

3. **RQ3 (Code-to-Text Migration):** Native code harnesses shifting to "file-backed state and artifact-backed verification" under natural-language execution, with improved observability but relocated reliability mechanisms

## Key Finding

"More explicit structure does not automatically improve end-task performance." Modules help most when they tighten alignment between intermediate behavior and evaluator acceptance—not simply by adding process layers.

## Design Philosophy

The work treats natural language as carrying "editable, inspectable orchestration logic" while code handles deterministic operations. It positions harness engineering as a controllable scientific object amenable to systematic study and automated optimization.
