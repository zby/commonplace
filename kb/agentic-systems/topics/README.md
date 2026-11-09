# Research Topics

Start with a design decision, identify the choices that could change it, then
follow a comparison or inspect individual systems. These four topics are
reading paths through the same accepted analyses, not separate populations
or independent dimensions. A memory choice can change verification and
recovery requirements.

| Topic | Architectural questions |
|---|---|
| [Agent Memory](./memory.md) | What survives a task, how does it reach a later decision, and what happens when it is wrong? |
| [Runtime & Control](./runtime.md) | Who chooses and executes the next action, under which authority? |
| [Knowledge & Verification](./epistemic.md) | What is checked before an agent relies on a claim? |
| [Workflow & Recovery](./workflow.md) | How does multi-step work coordinate, recover and reach delivery? |

Memory currently has the most developed [comparison research](../comparisons/memory/README.md)
and structured dataset. The other topics begin with questions and generated
per-system accounts; they do not yet have equivalent comparison tables.

## Future work

The next research should reduce uncertainty about design choices, not merely
add systems to the directory. The following are candidate investigations,
not established findings or commissioned experiments.

### Memory delivery: when should retained information reach a decision?

- **Alternatives to investigate:** requested retrieval, automatic injection,
  or a combination; vary selection and context budget separately.
- **Evidence needed before commitment:** compare downstream decisions, missed
  relevant information, distracting context, latency and cost under matched tasks.
- **Topic:** [Memory delivery](./memory.md).

### Correction: how can revision coexist with derived summaries and cached context?

- **Alternatives to investigate:** invalidation on read, eager repair, or
  regeneration; trace all affected consumers.
- **Evidence needed before commitment:** introduce a correction and test whether
  stale claims still reach each interface, including after restart; measure repair cost.
- **Topic:** [Correction](./memory.md).

### Runtime control: how much execution can be model-directed while authority remains enforced?

- **Combinations to investigate:** fixed control flow, model-written programs
  and external scheduling combined with explicit permission boundaries.
- **Evidence needed before commitment:** trace enforcement on each effect path,
  then test bypass attempts and interruption; distinguish flexibility from
  uncontrolled authority.
- **Topic:** [Runtime control](./runtime.md).

### Verification: when must a check block further work?

- **Alternatives to investigate:** advisory review, executable gates and human
  decisions at different points in the workflow.
- **Evidence needed before commitment:** show whether failed or missing checks
  prevent the relevant downstream action; compare error escape, false rejection
  and review cost.
- **Topic:** [Verification](./epistemic.md).

### Recovery: which state is sufficient to resume safely?

- **Combinations to investigate:** checkpoints, replay and retained results
  combined with different side-effect and ownership rules.
- **Evidence needed before commitment:** interrupt before and after external
  effects; test duplicate actions, lost work and stale-result acceptance,
  alongside recovery cost.
- **Topic:** [Recovery](./workflow.md).

### Scope a study

A bounded study can address one interaction rather than map a whole topic.
Its useful result is a set of alternatives with supported compatibility or
constraint claims, remaining uncertainty, and the next evidence that could
change a decision. A negative or incomplete result can narrow a claim or
leave a combination open; it must not silently eliminate an alternative.

New source analyses are useful when they expose a missing mechanism or test
a proposed constraint. Existing analyses can support focused comparisons;
questions about exercised behavior or benefit call for separate tests. The
[methods page](../methods.md#what-the-evidence-can-settle) explains these
evidence boundaries. Commonplace-specific commitments belong in separately
commissioned transfer work, not in the source accounts.

Also browse [comparisons](../comparisons/README.md),
the [Systems Directory](../../agentic-system-analyses/current-analyses.md), or
[Methods & Data](../methods.md).
