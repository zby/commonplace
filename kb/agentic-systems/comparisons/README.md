# Comparisons

Comparisons investigate architectural questions across selected systems.
They contribute to design-space exploration by identifying alternatives,
examining combinations and bounding claims about constraints and consequences.
They are not product rankings. Follow the citations to the frozen analysis
records to check a conclusion's scope. An unrepresented combination remains
open unless evidence rules it out.

## Agent memory

- [How memory reaches the next decision](./memory/read-back-mechanisms.md) —
  who initiates retrieval, how selection works, and which consumer receives
  the result. Contrasts Hermes, Nemsy, OpenKB, Hindsight and sqz; distinguishes
  catalog visibility, recoverable content and model-visible bodies from reliance.
- [How corrections propagate through retained memory](./memory/correction-propagation.md) —
  store changes, index freshness, prose repair and stale consumer copies across
  Graphiti, Hindsight, Mem0, OpenKB, SQLite Graph Memory and Project Wiki.
- [What the current corpus shows about agent memory mechanisms](./memory/agent-memory-landscape.md)
  — a frozen landscape of 243 analyses, dated 2026-11-09, at inputs commit
  `bf2da04db`. Covers admission, read-back, curation and trace learning,
  with evidence filters and withheld conclusions.
- [Memory comparison table](./memory/memory-systems-table.md) and
  [CSV](./memory/memory-systems.csv) — find candidate implementations and
  inspect their scoped evidence. See the [dataset boundary](./memory/README.md)
  before interpreting counts.
- [Current per-system memory accounts](./memory/systems.md) — build-time
  listing, which may be newer than the landscape and memory-table snapshots.

The [Agent Memory topic](../topics/memory.md) maps the research questions
these materials address.

## Further research topics

[Runtime & Control](../topics/runtime.md),
[Knowledge & Verification](../topics/epistemic.md) and
[Workflow & Recovery](../topics/workflow.md) currently provide questions and
per-system reading paths. The [future-work agenda](../topics/README.md#future-work)
prioritizes interactions and decision-critical uncertainties, rather than
coverage for its own sake. Cross-system articles can compare alternatives
where inspected evidence supports them; experiments are needed where the
question concerns actual behavior or benefit. No equivalent structured
datasets exist for these lenses yet.

## Interpret and reproduce

[Methods & Data](../methods.md) explains the analysis method and evidence
levels. [Comparison inputs and regeneration](./builds.md) is the operational
reference for population selection, profile versions, evidence interpretation
and rebuilding the memory outputs.

[Research Topics](../topics/README.md) ·
[Systems Directory](../../agentic-system-analyses/current-analyses.md)
