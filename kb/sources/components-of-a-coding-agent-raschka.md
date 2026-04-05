---
source: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent
description: Raschka's breakdown of the six architectural components of a coding agent harness — distinguishing the harness from the model and arguing that context quality drives apparent model quality.
captured: 2026-04-05
capture: web-fetch
type: blog-post
---

# Components of A Coding Agent

Author: Sebastian Raschka, PhD
Source: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent
Date: April 4, 2026

## Overview

This article explores the architecture of coding agents and their harnesses—the software scaffolding that wraps LLMs to enhance performance on coding tasks. Rather than relying solely on model capabilities, effective coding agents combine the model with specialized tools, context management, and execution support.

## Key Distinctions

The article clarifies relationships between related concepts:

- **LLM**: The core next-token prediction model
- **Reasoning Model**: An LLM optimized for intermediate reasoning and verification
- **Agent**: A control loop using a model with tools, memory, and environment feedback
- **Agent Harness**: Software scaffold managing context, tools, prompts, state, and control flow
- **Coding Harness**: Task-specific harness for software engineering

As noted, "the harness can often be the distinguishing factor that makes one LLM work better than another."

## Six Core Components

### 1. Live Repo Context
Agents collect workspace information upfront—git status, branch, project layout, documentation—before executing tasks. This prevents starting from zero on each prompt.

### 2. Prompt Shape and Cache Reuse
Rather than rebuilding the entire prompt each turn, smart runtimes maintain a stable prefix containing general instructions, tool descriptions, and workspace summaries. Only the session state, memory, and user request change between interactions.

### 3. Tool Access and Use
Agents use predefined tools with clear inputs and boundaries rather than arbitrary command suggestions. The harness validates actions against security policies, path restrictions, and approval requirements before execution.

### 4. Minimizing Context Bloat
Coding agents employ two primary strategies:
- **Clipping**: Shortening verbose outputs and transcript entries
- **Transcript Reduction**: Compressing older events aggressively while preserving recent history

### 5. Structured Session Memory
Agents maintain two layers:
- **Working memory**: Small, distilled state explicitly maintained
- **Full transcript**: Complete history of requests, outputs, and responses

### 6. Delegation with Bounded Subagents
Subagents inherit sufficient context for useful work but operate within tighter constraints—read-only access, recursion depth limits, and task scoping.

## Practical Impact

"A lot of apparent 'model quality' is really context quality." The surrounding system—repo navigation, context management, and execution support—plays as significant a role as the base model itself. This explains why Claude Code or Codex feel substantially more capable than the same models in plain chat interfaces.
