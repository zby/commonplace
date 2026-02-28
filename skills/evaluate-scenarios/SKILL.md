---
name: evaluate-scenarios
description: Read all scenario files, measure instruction bytes from referenced source files, and produce a cost report showing hops and byte counts per scenario weighted by frequency. Use to verify architectural claims about context loading costs.
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
context: fork
model: sonnet
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:
- If target is empty: evaluate all scenarios in `kb/scenarios/`
- If target is a scenario name: evaluate only that scenario
- If target is "compare": evaluate all and compare against a previous run if one exists

**Execute these steps:**

### 1. Discover scenario files

```bash
ls kb/scenarios/*.md
```

Read each scenario file. Parse the frontmatter for `frequency` and the step list for **Source** paths and **Hops** values.

### 2. Measure fixed instruction bytes

For each step marked **Fixed/Variable: fixed** or **Fixed/Variable: mixed**, read the file referenced in **Source** and measure its byte count:

```bash
wc -c < {source-path}
```

Common fixed sources you'll encounter:
- `CLAUDE.md` — always-loaded context (count once, not per-step)
- `kb/WRITING.md` — writing conventions and type templates
- `skills/connect/SKILL.md` — connection skill body
- `skills/ingest/SKILL.md` — ingestion skill body
- `skills/snapshot-web/SKILL.md` — snapshot skill body
- `kb/sources/types/source-review.md` — source review type template
- `kb/scenarios/types/scenario.md` — scenario type template

**Important:** Count CLAUDE.md bytes once per scenario (it's always loaded, not a per-step cost). Count other fixed sources once per scenario even if referenced in multiple steps (they stay in context after first load).

### 3. Estimate variable instruction bytes

For steps marked **Fixed/Variable: variable**, use these configurable defaults:

| Variable element | Default estimate |
|-----------------|-----------------|
| Search results (note count) | 3 notes |
| Average note size | 2,000 bytes |
| Link-follow reads | 2 notes |
| Area index reads | 1 index at ~3,000 bytes |
| External URL content | 5,000 bytes |

If $ARGUMENTS includes override estimates (e.g. "notes=5 notesize=3000"), use those instead.

### 4. Count hops per scenario

Parse the **Hops** field from each step. Sum:
- **Fixed hops:** steps where the hop count is a single number (e.g. "1")
- **Variable hops:** steps where the hop count is a range (e.g. "2-4") — use the midpoint
- **Total hops:** fixed + variable

For escalation steps, count separately and weight at 0.1 (estimated 10% occurrence).

### 5. Produce the cost table

Output format:

```
## Scenario Cost Report

Generated: {date}
Variable estimates: {defaults or overrides used}

### Per-Scenario Breakdown

#### {Scenario name} (frequency: {freq})

| Step | Hops | Fixed bytes | Variable bytes | Source |
|------|------|-------------|----------------|--------|
| 1. {name} | 0 | 5,251 | — | CLAUDE.md |
| 2. {name} | 3 | — | ~6,000 | search results |
| ... | | | | |
| **Subtotal (common path)** | **N** | **X** | **~Y** | |
| E1. {name} | ... | ... | ... | ... |
| **Subtotal (escalation, ×0.1)** | **N** | **X** | **~Y** | |

{Repeat for each scenario}

### Summary Table

| Scenario | Freq | Weight | Hops (common) | Hops (w/ esc.) | Bytes (fixed) | Bytes (total est.) |
|----------|------|--------|---------------|----------------|---------------|-------------------|
| Write a note | common | 1.0 | N | N | X | ~Y |
| Ingest a source | occasional | 0.3 | N | N | X | ~Y |
| Answer a question | common | 1.0 | N | N | X | ~Y |
| Respond to a change | occasional | 0.3 | N | N | X | ~Y |

### Weighted Totals

| Metric | Value |
|--------|-------|
| Weighted hops (common path) | N |
| Weighted hops (with escalation) | N |
| Weighted fixed bytes | X |
| Weighted total bytes | ~Y |

### Observations

{Note any architectural implications:
- Which scenario dominates the weighted cost?
- Where are the biggest variable cost drivers?
- What architectural changes would reduce costs?
- How does the current design compare to alternatives (e.g. inlining types saved N bytes at step X)?}
```

### 6. Verify plausibility

After producing the table, sanity-check key numbers:
- CLAUDE.md should be in the range of 4,000-7,000 bytes
- WRITING.md should be in the range of 8,000-12,000 bytes
- Skill files (connect, ingest) are typically 10,000-20,000 bytes
- If any number looks implausible, re-read the source file and re-measure

**START NOW.** Read all scenario files, measure all referenced source files, produce the cost table.
