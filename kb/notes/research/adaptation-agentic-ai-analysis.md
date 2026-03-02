---
description: Analysis of agentic AI adaptation paper and llm-do implications
---

# Analysis: Adaptation of Agentic AI (arXiv:2512.16301)

This note analyzes the paper "Adaptation of Agentic AI" and explores how its framework could inform llm-do's design and potential extensions.

## Paper Overview

The paper presents a taxonomy for adaptation in agentic systems, organizing strategies along two dimensions:

1. **What adapts**: Agent (LLM behavior) vs Tool (external capabilities)
2. **What triggers adaptation**: Tool-execution signals vs Agent-output signals

## Key Adaptation Mechanisms

### 1. Error-Driven Adaptation (Tool-Execution-Signaled)

When tools fail, the error propagates back to the LLM, which adjusts its approach.

**Current llm-do behavior**: This already happens naturally—when a tool call fails, the error message is returned to the LLM in the conversation, and it can retry with different parameters or try a different tool.

**Potential extension**: **Failure logging and analysis**

```yaml
# Hypothetical worker config
adaptation:
  log_failures: true
  failure_store: ./failures/{worker_name}/
```

The runtime could:
- Log every tool failure with context (worker, task input, tool called, error, LLM's recovery attempt)
- Aggregate patterns: "tool X fails 40% of the time when called with pattern Y"
- Surface insights: "Consider adding instruction about X" or "Tool X needs better error messages"

**Implementation sketch**:
```python
# In runtime/ctx.py, wrap tool execution
async def execute_tool_with_logging(tool, args, context):
    try:
        result = await tool(**args)
        log_success(context, tool, args, result)
        return result
    except Exception as e:
        log_failure(context, tool, args, e)
        raise  # Let LLM handle retry
```

### 2. Prompt Refinement (Agent Adaptation)

Adjusting worker instructions based on observed performance.

**Current llm-do support**: Manual—users edit `.worker` files based on observed behavior.

**Potential extension**: **Prompt evolution tracking**

Workers could track their own performance and suggest refinements:

```yaml
# In worker definition
adaptation:
  track_outcomes: true
  outcome_labels: ["success", "partial", "failed", "user_corrected"]
```

After each run, optionally prompt user: "How did this go?" Store outcome with task hash. After N runs, analyze:
- Which task patterns succeed?
- Which fail?
- What instructions might help?

**More ambitious**: An `improve_worker` meta-tool that:
1. Reads failure logs for a worker
2. Analyzes patterns
3. Proposes prompt modifications
4. User approves changes

This is "stabilizing" in llm-do terminology—but data-driven rather than intuition-driven.

### 3. Tool Selection Adaptation

Dynamically adjusting which tools are available based on task and past success.

**Current llm-do support**: Static—toolsets are declared in worker config.

**Potential extension**: **Conditional toolsets**

```yaml
toolsets:
  filesystem:
    tools: [read_file, write_file]
  shell:
    tools: [run_command]
    # Only enable after certain conditions
    enable_after:
      - successful_read_file: 2  # After 2 successful file reads
      - user_trust_level: high
```

Or dynamic tool recommendations:
```yaml
toolsets:
  delegation:
    workers: [analyzer, formatter]
    recommend_based_on:
      - task_keywords
      - past_success_rate
```

### 4. Online vs Offline Adaptation

**Online**: Real-time adjustments during execution (current LLM retry behavior)
**Offline**: Pre-computed refinements from historical analysis

**Current llm-do support**: Mostly online (LLM adapts in-session).

**Potential extension**: **Offline adaptation pipeline**

```bash
# Analyze past runs
llm-run analyze --entry orchestrator --since "7 days"

# Output:
# - 23 runs, 18 successful
# - Common failure: "file not found" when paths are relative
# - Suggested instruction addition: "Always use absolute paths"
# - Tool `formatter` called but failed 4/5 times → review formatter.worker
```

This could feed into a refinement workflow:
1. Run workers in production
2. Periodically analyze logs
3. Generate suggested improvements
4. Human reviews and applies

### 5. Agent-Output-Signaled Adaptation

Adaptation triggered by the agent's own reasoning/confidence, not external failures.

**Current llm-do support**: None explicit.

**Potential extension**: **Confidence signaling**

Workers could be instructed to signal uncertainty:

```markdown
# In worker instructions
If you are uncertain about the correct approach, use the `signal_uncertainty` tool
with a description of what you're unsure about. This will pause execution for human input.
```

Or structured output could include confidence:

```yaml
result_type:
  type: object
  properties:
    answer:
      type: string
    confidence:
      type: string
      enum: [high, medium, low]
    uncertainty_reason:
      type: string
```

Low-confidence results could trigger:
- Automatic human review
- Logging for later analysis
- Escalation to a more capable model

## Mapping to llm-do's Spectrum

The paper's framework maps to llm-do's neural/symbolic spectrum:

| Paper Concept | llm-do Equivalent |
|---------------|-------------------|
| Agent-agnostic tools | Pure Python tools (no worker calls) |
| Agent-supervised tools | Hybrid tools with `ctx.deps.call(...)` |
| Tool-execution-signaled | Error propagation to LLM (existing) |
| Agent-output-signaled | Confidence signals (potential extension) |
| Offline adaptation | Failure analysis → prompt refinement |
| Online adaptation | In-session LLM retry/adjustment |

## Proposed Features (Priority Order)

### P1: Failure Logging

Minimal invasive change. Log tool failures with context to enable later analysis.

```python
# runtime addition
class FailureLog:
    def log(self, worker: str, tool: str, args: dict, error: str, recovery: str):
        # Append to JSONL file
        ...
```

### P2: Run Outcome Tracking

After worker completion, optionally record outcome. Enables offline analysis.

```python
# CLI addition
llm-run worker.worker --track-outcome
# After completion: "Rate outcome: [s]uccess / [p]artial / [f]ailed / [enter] skip"
```

### P3: Analysis Command

Consume logs to surface patterns.

```bash
llm-run analyze orchestrator --since 7d
# Outputs failure patterns, success rates, suggestions
```

### P4: Confidence Signaling

Add optional `signal_uncertainty` tool to core toolsets. When called, pauses for human input or logs for review.

### P5: Prompt Evolution Suggestions

Meta-worker that reads failure logs and proposes instruction improvements.

## Implications for Bidirectional Refactoring

The paper reinforces llm-do's bidirectional refactoring principle with data-driven triggers:

**Stabilizing signals** (neural → symbolic):
- Tool consistently fails with certain input patterns → add validation in Python
- LLM always calls tools in same sequence → extract to Python orchestration
- Output structure is always identical → add stricter schema

**Softening signals** (symbolic → neural):
- Python tool has growing exception list → delegate edge cases to worker
- Validation rules have many special cases → use LLM for underspecified validation
- User frequently overrides tool behavior → add flexibility via worker

---

Relevant Notes:
- [three distinct mechanisms](../agentic-systems-learn-through-three-distinct-mechanisms.md) — the stabilising/softening signals catalogued here are the data-driven triggers for the continuous learning loop that crystallisation describes

## References

- Paper: https://arxiv.org/abs/2512.16301
- [agentic systems interpret underspecified instructions](../agentic-systems-interpret-underspecified-instructions.md) — underspecified vs precise semantics, interpretation narrowing, stabilise/soften
- llm-do architecture: [architecture.md](../../../docs/architecture.md)
