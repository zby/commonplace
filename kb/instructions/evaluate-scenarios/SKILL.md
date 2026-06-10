---
name: evaluate-scenarios
description: Decompose each scenario into clean-context forks, measure framework-overhead bytes and hops per fork, and report a feasibility signal (heaviest fork's net load) and a cost signal (overhead summed across forks). Use to measure the operational overhead the framework imposes per agent.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
context: fork
model: sonnet
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:
- empty → evaluate all scenarios in `test/scenarios/`
- a scenario name → evaluate only that scenario
- `compare` → evaluate all and compare against a previous run if one exists

This harness measures **operational overhead**: the framework instructions an agent must read on top of the task's own content. The unit is the **fork**, not the operation — every `cp-skill-*` runs `context: fork`, so each fork pays its overhead from a fresh context. See `kb/notes/feasibility-is-the-heaviest-forks-net-load.md` for the model.

### 1. Discover scenario files

```bash
ls test/scenarios/*.md
```

Read each scenario. Each has a `## Forks` section with one subsection per fork; each fork has a table of loads: `load | kind | source | hops`, where `kind` is `overhead`, `content`, or `spared`.

### 2. Config (override via $ARGUMENTS, e.g. `notesize=3000 candidates=4 budget=50000 agents_per_fork=on`)

| Knob | Default | Meaning |
|---|---|---|
| `notesize` | 2,000 B | average note/body read |
| `candidates` | 3 | content notes opened where a fork prospects bodies |
| `spared_bodies` | 3 | bodies an index or description-listing read lets a fork skip |
| `index_size` | 3,000 B | one curated index read or scoped description listing |
| `validate_out` | 500 B | bytes a `commonplace-validate` run returns into context |
| `budget` | 50,000 B | usable-window soft ceiling for the feasibility flag (overhead + content + room to reason) |
| `agents_per_fork` | off | if `on`, add AGENTS.md overhead to every fork, not only where the scenario lists it (the "is AGENTS.md re-injected?" assumption) |

### 3. Measure overhead bytes (per fork)

For each `overhead` row, read the file named in **source** and measure it:

```bash
wc -c < {source-path}
```

Measure each distinct file once and reuse the number, but **add it to every fork that lists it** — do not amortize across forks. A `commonplace-validate` (or other tool) source contributes `validate_out` bytes and 1 hop, not a file measurement. An index given as a concrete path is measured with `wc -c` like any file; `index_size` applies only to a generic unnamed index or scoped listing the scenario does not path. (Complete `dir-index.md` listings no longer exist in the repo — ADR 025; a legacy scenario that lists one should be re-costed as a scoped `rg` listing.)

Common overhead sources: `AGENTS.md`, the target `COLLECTION.md`, the type-spec (`kb/types/*.md`), the invoked skill body (`kb/instructions/cp-skill-*/SKILL.md`), and curated tag indexes.

### 4. Estimate content and spared bytes (per fork)

- `content` row: `notesize` per body, times the count implied by the hop range (use the midpoint). A row marked "the insight"/"already in session" with hops 0 contributes its rough size if stated, else `notesize`.
- `spared` row: a **negative** credit, `spared_bodies × notesize` minus the `index_size` that replaced them (the index or listing read is already counted as overhead).

### 5. Count hops (per fork)

Sum the **hops** column per fork; a range (`2-4`) uses its midpoint. Track overhead-hops and content-hops separately so the cost signal can report overhead hops.

### 6. Compute the two signals (per scenario)

- **Net load per fork** = overhead bytes + content bytes − spared credit (bytes); net hops = overhead + content hops.
- **Feasibility signal** = the single **heaviest** fork by net bytes — report that fork, its net bytes and net hops, and flag it if net bytes exceed `budget`.
- **Cost signal** = **overhead** bytes summed across **all** forks (gross — the spared credit applies only to feasibility), and overhead hops summed across all forks.

### 7. Output

```
## Scenario Overhead Report

Generated: {date}    Config: {knobs used}

### {Scenario} (frequency: {freq})

| Fork | Overhead B / hops | Content B / hops | Spared B | Net B | Net hops |
|------|-------------------|------------------|----------|-------|----------|
| 1 orchestrator | ... | ... | — | ... | ... |
| 2 cp-skill-write | ... | ... | ... | ... | ... |
| 3 cp-skill-connect | ... | ... | — | ... | ... |
| **Feasibility (heaviest fork)** | | | | **{B} ({fork})** {⚠ if > budget} | **{hops}** |
| **Cost (Σ overhead, gross)** | **{B} / {hops}** | | | | |

Overhead sources measured: {file: bytes, ...; note any counted in multiple forks}

{repeat per scenario}

### Summary

| Scenario | Freq | Feasibility (heaviest fork B / hops) | Cost (Σ overhead B / hops) |
|----------|------|--------------------------------------|----------------------------|
| ... | ... | ... | ... |

| Metric | Value |
|--------|-------|
| Worst feasibility across scenarios | {scenario / fork — bytes} |
| Frequency-weighted overhead cost | {Σ (cost × weight); common=1.0, occasional=0.3, rare=0.1} |

### Observations
- which fork drives feasibility, and how close it is to `budget`
- which overhead source dominates the cost sum (re-paid skill bodies? re-read COLLECTION.md?)
- what would cut each signal (merge forks lowers cost but raises feasibility; sparing more content lowers feasibility only)
- any fork flagged over `budget`
```

### 8. Verify plausibility

- AGENTS.md: ~15,000–18,000 B (root instructions + vocabulary + routing)
- COLLECTION.md: ~4,000–8,000 B
- type-spec (`kb/types/*.md`): ~2,000–4,000 B
- skill bodies (`cp-skill-*`): ~8,000–12,000 B
- scoped `rg` description listing: roughly 150 B per matching note — grows with the slice, not the collection

If a number is implausible, re-read and re-measure.

**START NOW.** Read the scenarios, measure overhead per fork, emit the per-scenario fork tables and the feasibility + cost signals.
