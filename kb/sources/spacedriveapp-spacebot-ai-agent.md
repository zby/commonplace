---
source: https://github.com/spacedriveapp/spacebot
captured: 2026-02-23
capture: web-fetch
type: web-page
---

# Spacebot: AI Agent for Teams and Communities

Author: spacedriveapp
Source: https://github.com/spacedriveapp/spacebot

**Repository:** spacedriveapp/spacebot
**Description:** An AI agent for teams, communities, and multi-user environments
**Stars:** 1.2k | **Forks:** 154
**License:** FSL-1.1-ALv2
**Language:** Rust
**Website:** [spacebot.sh](https://spacebot.sh)

## Overview

Spacebot is a concurrent AI agent framework designed for multi-user environments. Rather than processing everything sequentially in a single session, it splits functionality across specialized processes that work in parallel—channels handle conversation, branches manage thinking, workers execute tasks, and a cortex supervises the entire system.

## Core Architecture

The system uses five process types:

- **Channels:** User-facing LLM processes that never block, always responsive to messages
- **Branches:** Independent thinking forks that inherit channel context for analysis
- **Workers:** Specialized task executors (shell, file, browser, coding) spawned by branches
- **Compactor:** Programmatic monitor that prevents context overflow without interrupting conversation
- **Cortex:** System-wide supervisor managing memory, process health, and knowledge synthesis

## Key Capabilities

**Task Execution:**
- Shell commands with configurable timeouts
- File operations (read, write, list with auto-creation)
- Program execution with environment variables
- Headless browser automation with accessibility trees
- OpenCode integration for deep coding sessions
- Brave web search integration

**Messaging:**
Message coalescing detects rapid-fire bursts and batches them into single LLM turns. Native adapters support Discord, Slack, Telegram, Twitch, and Webchat with rich formatting, threading, reactions, and per-channel permissions.

**Memory System:**
Eight typed memory categories (Fact, Preference, Decision, Identity, Event, Observation, Goal, Todo) with graph edges (RelatedTo, Updates, Contradicts, CausedBy, PartOf). Hybrid recall merges vector similarity and full-text search via Reciprocal Rank Fusion. Memory bulletin provides periodic briefings injected into conversations.

**Model Routing:**
Four-level system selecting appropriate models per call—process-type defaults, task-type overrides, prompt complexity scoring, and fallback chains. Supports Anthropic, OpenAI, OpenRouter, Z.ai, Groq, Together, Fireworks, DeepSeek, xAI, Mistral, NVIDIA, MiniMax, Moonshot AI, Ollama, and custom OpenAI/Anthropic-compatible endpoints.

**Extensibility:**
- MCP (Model Context Protocol) integration for arbitrary tool access
- skills.sh registry for installing community skills
- Hot-reloadable configuration for live updates

**Scheduling:**
Cron jobs with natural language creation, clock-aligned intervals, active hours, per-job timeouts, and circuit breaker auto-disabling after failures.

## Deployment Options

- **spacebot.sh:** One-click hosted deployment
- **Self-hosted:** Single Rust binary, no dependencies
- **Docker:** Container with volume persistence

## Getting Started

**Requirements:** Rust 1.85+ and an LLM API key

```bash
git clone https://github.com/spacedriveapp/spacebot
cd spacebot
cargo build --release
```

Minimal configuration connects Discord, Slack, or other platforms with routing to any supported LLM provider.

## Design Philosophy

"Thinks, executes, and responds — concurrently, not sequentially. Never blocks. Never forgets." The architecture prevents the bottlenecks found in traditional single-threaded agent frameworks where conversation freezes during context compaction or task execution.
