# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**.

It has two goals. The practical one is an **LLM wiki**, in the sense [Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer in which agents, directed by people, turn a person's or project's work into retained, connected notes. The theoretical one is a new learning paradigm, the **theory builder**: a system that states theories, acts on them, criticizes them, and keeps what criticism shows for the next round, following Karl Popper's method of conjecture and criticism. We bet that a fully automated theory builder that learns can be built with today's LLMs, their weights held fixed. No test of the bet has been run yet.

The goals reinforce each other, because memory is always about learning: a note is worth something when it changes what the system does next. Theories that are acted on, criticized, and revised are what make a wiki learn, and [real use of the wiki supplies the problems and criticism](./notes/system-use-selects-theory-fit-without-a-fixed-oracle.md) a theory builder learns from.

[Reflection](./notes/definitions/theory-builder.md#qualifiers) is the core of the method. Commonplace's doctrine, how it writes, connects, and revises notes, is one of the theories it criticizes and revises, so [an improvement to the method is reused by all later work](./notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md). People still perform many of its operations; the work is moving them to computation.

The site holds the adopted doctrine together with research and evidence that can challenge it. Research does not become doctrine merely by being stored here.

## Start here

The [theory builder definition](./notes/definitions/theory-builder.md) states the four conditions, the graded design commitments above them, and what the definition leaves open. [Commonplace builds a theory builder and tests whether it learns](./notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md) sets out the research program and its three conjectures. The [learning theory index](./tags/learning-theory-README.md) maps the wider thread.

## Other threads

**Deployment-time learning.** Durable changes to prompts, rules, tools, schemas, tests, and code can affect later sessions without updating model weights. Storing a change is not enough: later work must load or enforce it. [Deploy-time learning](./notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) develops this path, and [bounded context](./notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) explains why a system must still choose what each task loads. The [learning theory index](./tags/learning-theory-README.md) maps the wider thread.

**Self-improving systems.** A system improves itself when evidence changes the parts that determine its own behavior. One design updates behavior directly; another searches candidates, evaluates them, and [retains an accepted proposal](./notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). A theory builder is a further kind: its improvement runs through criticism of theories it has stated. The [self-improving systems index](./tags/self-improving-systems-README.md) and the [Commonplace case](./notes/evidence/commonplace-as-a-reflective-system.md) develop the distinction.

**Agent-usable memory.** Agents need [discoverable, composable, and trusted knowledge under bounded context](./notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). [Explicit link semantics](./tags/links-README.md) show support, contrast, and consequence; routing selects what reaches a task; provenance and review indicate how strongly to rely on it. Because [information value is observer-relative](./notes/information-value-is-observer-relative.md), useful condensation depends on the consuming agent and task.

**Systems compared.** We have reviewed [more than 150 agent memory systems](./agent-memory-systems/README.md), including Mem0, Graphiti, Cognee, and Letta. The [comparative analysis](./agent-memory-systems/agentic-memory-systems-comparative-review.md) finds that the reviewed systems differ less in where they store memory than in how memory reaches the agent's next action and whether anyone checks that it changed behavior. The reviews over-sample file-based systems, so their counts describe this set of reviews rather than the field.

## Browse

- [Notes](./notes/README.md) — research claims
- [Tags](./tags/README.md) — browse by topic across notes, reference, instructions, and system reviews
- [Reference](./reference/README.md) and [Types](./types/README.md) — the current system, decisions, and artifact contracts
- [Agent Memory Systems](./agent-memory-systems/README.md) and [Agentic Systems](./agentic-systems/README.md) — external-system reviews
- [Sources](./sources/README.md), [Instructions](./instructions/README.md), and [Workshops](./work/README.md) — evidence, procedures, and work in flight

## Use it yourself

Commonplace is open source. You can:

- **Vendor the knowledge base read-only** inside a project so agents can consult the research and external-system reviews.
- **Install the system** to give a project the types, conventions, skills, and commands for building its own agent-operated knowledge base.

The [GitHub README](https://github.com/zby/commonplace) covers the tool, [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) gives the setup flow, and the [installation architecture](./reference/architecture.md) explains the design.