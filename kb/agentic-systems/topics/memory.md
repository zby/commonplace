# Agent Memory

Agent memory is retained information that can become available to later work.
The research problem is not just where information is stored: it is how
information is admitted, selected, revised and consumed under a limited
context budget.

Start with the [agent-memory landscape](../comparisons/memory/agent-memory-landscape.md),
a source-grounded snapshot of 191 analyses from October 2026. Use the
[comparison table](../comparisons/memory/memory-systems-table.md) to find
candidate mechanisms, then read the linked per-system records before making
an architectural claim.

## Focused comparisons

- [How memory reaches the next decision](../comparisons/memory/read-back-mechanisms.md) —
  compare whole-file loading, requested retrieval, automatic injection and
  maintenance-model inputs in Hermes, A-MEM, Hindsight and Basic Memory.
- [How corrections propagate through retained memory](../comparisons/memory/correction-propagation.md) —
  compare temporal invalidation, dependent-record cleanup and explicit
  replacement in Graphiti, Hindsight and Mem0, then test the consumers that
  can still receive stale information.

## Research questions

### What information is retained?

Distinguish raw conversations, extracted facts, summaries, procedures and
derived representations. A storage format does not by itself explain what
later work can use. The [memory accounts](../comparisons/memory/systems.md)
trace retained objects and consumers; the
[landscape's curation discussion](../comparisons/memory/agent-memory-landscape.md#curation-revision-and-forgetting-are-common-synthesis-is-rare)
compares the transformations identified in its frozen population.

### Who decides what enters memory?

An automatic write can still depend on model judgment, fixed rules or caller
selection. The [write-admission comparison](../comparisons/memory/agent-memory-landscape.md#write-admission-automatic-is-near-universal-manual-is-often-instructed-not-wired)
separates code-wired routes from instructions that merely ask an agent to save
something. Follow each table row to its scope and evidence basis.

### How is retained information selected for later use?

Ask who initiates a read, which selector runs, and who receives the result.
Memory selected for a maintenance model is not necessarily delivered to an
answering agent. Read [How memory reaches the next decision](../comparisons/memory/read-back-mechanisms.md)
for concrete contrasts, or begin with the
[landscape's read-back analysis](../comparisons/memory/agent-memory-landscape.md#read-back-push-usually-selects-coarsely)
and use the [per-system accounts](../comparisons/memory/systems.md) to trace
the full route.

### What happens when information changes or becomes invalid?

Updating a source, invalidating a fact and repairing every dependent summary
are different operations. [How corrections propagate](../comparisons/memory/correction-propagation.md)
traces those boundaries and proposes multi-interface experiments.
The [curation findings](../comparisons/memory/agent-memory-landscape.md#curation-revision-and-forgetting-are-common-synthesis-is-rare)
provide candidates for investigation, not a guarantee of complete correction.
Check which consumer and derived representation each inspected route reaches.

### How does experience modify future behavior?

Retaining a trace does not establish that later behavior changes.
The [trace-learning discussion](../comparisons/memory/agent-memory-landscape.md#trace-learning-widely-wired-uneven-in-depth)
distinguishes wired update routes and their limits. Follow the
[Workflow & Recovery topic](./workflow.md) when the experience comes from a
multi-step run, and [Knowledge & Verification](./epistemic.md) when a retained
conclusion must be checked before reliance.

### What evidence establishes that memory improves performance?

A retrieval route, an observed read and a controlled improvement are separate
findings. The frozen landscape reports
[static wiring or weaker evidence](../comparisons/memory/agent-memory-landscape.md#every-positive-finding-is-static-wiring-or-weaker),
not causal improvement. Experiments need to measure downstream decisions and
compare conditions with and without the relevant memory route.

## Find systems and data

- [Current memory accounts and profiles](../comparisons/memory/systems.md) —
  generated at each build from accepted analyses.
- [Memory comparison research and datasets](../comparisons/memory/README.md) —
  landscape, table and CSV, with their snapshot boundaries.
- [Systems Directory](../../agentic-system-analyses/current-analyses.md) —
  whole-system overviews and frozen evidence boundaries.
- [Methods & Data](../methods.md) — evidence classifications, population
  selection and interpretation.

[All research topics](./README.md) · [Comparisons](../comparisons/README.md)
