# Five-turn exploration of bootstrapping automation

## Intent

Commissioned by the operator on 2026-11-05. Explore beyond the current economic framing while keeping the main plan in view: a system useful across kinds of knowledge work that learns to automate methodologies through their development and use. The working premise is that LLMs make methodological knowledge executable before every judgment is reduced to code. Question the premise when useful; do not silently replace the operator's purpose.

This is also a trial of that approach: use delegated exploration, criticism and integration to learn both about the problem and about the method of investigating it. Success means useful changes or well-founded limits to the main plan, not five rounds of agreeable prose.

## Directions

Five conversational turns, with an operator response before proceeding to the next. These are starting directions, not fixed research questions; the coordinator may reframe the next turn from findings and operator feedback.

1. **Objectives:** what should increase, and how do present usefulness and future ability to automate conflict?
2. **Productive drift:** how can exploration discover possibilities outside the initial framing without becoming endless preparation?
3. **Executable methodology:** what turns experience into reusable, checkable application rather than merely more instructions?
4. **Investment:** how should work on user problems, methodology and automation compete or reinforce one another? Seek a bounded comparison with a simpler rival, not a general controller build.
5. **Learning from this trial:** what changed decisions, what did it cost, and what should change in the main plan or the exploration procedure?

## Execution and boundaries

- Each turn uses two fresh explorers with different angles, run sequentially without seeing each other's results, then a separate fresh critic, then a separate fresh integrator. Explorers may drift without demonstrating immediate applicability. Criticism tests mechanisms, evidence and alternatives; integration distinguishes useful changes within the plan from proposed changes to its purpose. The coordinator owns scheduling, recovery and the report to the operator.
- Engage with the whole KB, not just this workshop. Follow its navigation, collection and source rules. Existing notes are arguments and evidence to examine, not independent confirmation. External research is permitted when it could change the answer; explorers may delegate bounded source ingests to sub-sub-agents using `cp-skill-ingest`. Distinguish borrowed claims, analogies, conjectures and demonstrated results.
- Use `commonplace-worker` with project scope. Give each explorer `maxDepth: 2` and `maxWorkers: 2`. It may launch one ingest coordinator with `maxDepth: 1` and `maxWorkers: 1`, allowing the required fresh drafting worker. Run source jobs sequentially; release any delegated connection-discovery worker before drafting. The explorer and its descendants reserve three of the four slots. Finish one explorer before launching the other. Critics and integrators need no delegation budget. Every handoff states its question, accessible inputs, owned outputs and stop conditions. Nested work inherits the same limits; no broader delegation authority is implied.
- Keep research and synthesis outputs in this directory, under `turn-01/` through `turn-05/`. Give each agent a distinct file; the coordinator records assignments and returned session paths before moving on. Do not overwrite another agent's work. Source ingests, their required snapshots under `kb/sources/`, and generated connection reports under `kb/reports/cache/connect/sources/` are the exceptions to this directory boundary: coordinate unique destinations using the ingest workflow. No other library edits, implementation or commits are commissioned.
- The coordinator selects Sol (`openai/gpt-6.1-sol`) for exploration assignments dominated by large-volume file searches or other simple operations. Use explicit model overrides rather than relying on inheritance; do not assume Sol is the default for conceptual exploration, criticism or integration. Keep the same isolation, ownership and resource budgets. If an exploration mixes bulk retrieval with consequential synthesis, separate the bounded retrieval assignment from synthesis and schedule it within the four-slot limit rather than adding concurrent workers.
- Leave methods and source selection to the agents. Stop or return a partial result when evidence, tools or scope block progress; name what remains unknown. Escalate consequential scope changes rather than silently broadening the task. Do not force speculative numbers or treat a negative result as failure.
- Before each turn, record briefly why its question merits the investment. Afterwards retain discoveries, strongest objections, decisions changed, parked ideas, available costs and operator interventions. Mark unavailable measurements unknown. Preserve enough contemporaneous evidence to resist a polished hindsight account; avoid elaborate reporting machinery.

## Completion

After turn five, deliver a proposed revision of the main plan, surviving questions, and a judgment about which parts of this procedure deserve another trial. Useful findings do not by themselves demonstrate superiority to simpler conversation or delegation. Extraction, implementation and deletion require a separate decision; preserve the parent workshop's existing deletion hold.

Status: plan recorded; no exploration agents launched. The [parent framing](../README.md) supplies background and adjacent-work boundaries; this commission adds deliberate drift and the bootstrap purpose, not adoption of the resource-tier model or any objective function.
