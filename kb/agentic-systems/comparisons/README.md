# Comparisons

Comparisons investigate architectural questions across selected systems.
They explain mechanisms and consequences, not product rankings. Follow the
citations to the frozen analysis records to check a conclusion's scope.

## Agent memory

- [How memory reaches the next decision](./memory/read-back-mechanisms.md) —
  who initiates retrieval, how selection works, and which consumer receives
  the result. Contrasts Hermes, A-MEM, Hindsight and Basic Memory; distinguishes
  delivered context from demonstrated reliance.
- [How corrections propagate through retained memory](./memory/correction-propagation.md) —
  what changes after correction or withdrawal in Graphiti, Hindsight and Mem0,
  and which derived representations and consumer copies still need repair.
- [What the current corpus shows about agent memory mechanisms](./memory/agent-memory-landscape.md)
  — a frozen landscape of 191 analyses, dated 2026-10-22, at inputs commit
  `5f92f75e5`. Covers admission, read-back, curation and trace learning,
  with evidence filters and withheld conclusions.
- [Memory comparison table](./memory/memory-systems-table.md) and
  [CSV](./memory/memory-systems.csv) — find candidate implementations and
  inspect their scoped evidence. See the [dataset boundary](./memory/README.md)
  before interpreting counts.
- [Current per-system memory accounts](./memory/systems.md) — build-time
  listing, which may be newer than those snapshots.

The [Agent Memory topic](../topics/memory.md) maps the research questions
these materials address.

## Further research topics

[Runtime & Control](../topics/runtime.md),
[Knowledge & Verification](../topics/epistemic.md) and
[Workflow & Recovery](../topics/workflow.md) currently provide questions and
per-system reading paths. Cross-system articles will be added when inspected
evidence supports a useful comparison; no equivalent structured datasets
exist for these lenses yet.

## Interpret and reproduce

[Methods & Data](../methods.md) explains the analysis method and evidence
levels. [Comparison inputs and regeneration](./builds.md) is the operational
reference for population selection, profile versions, evidence interpretation
and rebuilding the memory outputs.

[Research Topics](../topics/README.md) ·
[Systems Directory](../../agentic-system-analyses/current-analyses.md)
