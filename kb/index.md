# Commonplace

**Research on knowledge systems, running as one.**

The premise is simple. LLM-written text can be useful even when no person reads it directly, because it can improve how an LLM answers your questions. Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**.

It has two goals. The practical one is an **LLM wiki**, in the sense [Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer in which agents, directed by people, turn a person's or project's work into retained, connected notes. The theoretical one is a learning paradigm, **[deliberative learning](./theory/definitions/deliberative-learning.md)**: a system learns by editing a store it can read and point at, made of prose, structured text, and code, and each edit is proposed, judged, and can be rejected. The process is old: teams run it when they maintain handbooks and linters. We bet that today's LLMs, their weights held fixed, can do the judging, weighing a change on balance where no single measure settles it, so that the whole loop runs without a person. No test of the bet has been run yet.

The goals reinforce each other, because memory is always about learning: a note is worth something when it changes what the system does next. A wiki that agents read and edit is the kind of store deliberative learning needs, and [real use of the wiki supplies the problems and criticism](./theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) that its judgments draw on.

[Reflection](./theory/definitions/reflective-system.md) is the core of the method. Commonplace's doctrine, how it writes, connects, and revises notes, is part of the store it edits, so [an improvement to the method is reused by all later work](./theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md). People still perform many of its operations; the work is moving them to computation.

The site holds the adopted doctrine together with research and evidence that can challenge it. Research does not become doctrine merely by being stored here.

## Start here

The draft article [Deliberative Learning: Judgment in Place of a Value Function](./articles/deliberative-learning-judgment-in-place-of-a-value-function.md) argues the central thesis: deliberative learning is a distinct learning paradigm, and a fully automated deliberative learner is compatible with the Bitter Lesson. The [deliberative learning definition](./theory/definitions/deliberative-learning.md) gives the two conditions and the separate verdict that a change was learned. [On-balance judgments can guide improvement without a global measure](./theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) says what the judgment asserts. The [deliberative learning index](./tags/deliberative-learning-README.md) lists the notes the thesis rests on.

## Other threads

**Deployment-time learning.** Durable changes to prompts, rules, tools, schemas, tests, and code can affect later sessions without updating model weights. Storing a change is not enough: later work must load or enforce it. [Deploy-time learning](./theory/retained-artifacts-enable-persistent-deployment-time-adaptation.md) develops this path, and [bounded context](./theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) explains why a system must still choose what each task loads. The [learning theory index](./tags/learning-theory-README.md) maps the wider thread.

**Self-improving systems.** A system improves itself when evidence changes the parts that determine its own behavior. One design updates behavior directly; another searches candidates, evaluates them, and [retains an accepted proposal](./theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). A deliberative learner is of the second design, with a store that can be read and pointed at. The [self-improving systems index](./tags/self-improving-systems-README.md) and the [Commonplace case](./theory/evidence/commonplace-as-a-reflective-system.md) develop the distinction.

**Agent-usable memory.** Agents need [discoverable, composable, and trusted knowledge under bounded context](./theory/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). [Explicit link semantics](./tags/links-README.md) show support, contrast, and consequence; routing selects what reaches a task; provenance and review indicate how strongly to rely on it. Because [information value is observer-relative](./theory/information-value-is-observer-relative.md), useful condensation depends on the consuming agent and task.

**Systems compared.** The [Agentic Systems research resource](./agentic-systems/README.md) investigates architectural alternatives through source-grounded analyses. Start with [Agent Memory](./agentic-systems/topics/memory.md) and its [October 2026 landscape of 191 analyses](./agentic-systems/comparisons/memory/agent-memory-landscape.md), or browse the generated [Systems Directory](./agentic-system-analyses/current-analyses.md). These populations are selected research corpora, not representative samples of the field. The [earlier comparative review](./agent-memory-systems/agentic-memory-systems-comparative-review.md) remains a historical snapshot of the older review corpus.

## Browse

- [Theory](./theory/README.md) — research claims
- [Notes](./notes/README.md) — replies, examples and comparisons to use as written
- [Tags](./tags/README.md) — browse by topic across notes, reference, instructions, and system reviews
- [Reference](./reference/README.md) — the current system, decisions, and artifact contracts
- [Agentic Systems](./agentic-systems/README.md) — research topics, architectural comparisons and source-grounded system analyses
- [Sources](./sources/README.md), [Instructions](./instructions/README.md), and [Workshops](./work/README.md) — evidence, procedures, and work in flight

## Use it yourself

Commonplace is open source. You can:

- **Vendor the knowledge base read-only** inside a project so agents can consult the research and external-system reviews.
- **Install the system** to give a project the types, conventions, skills, and commands for building its own agent-operated knowledge base.

The [GitHub README](https://github.com/zby/commonplace) covers the tool, [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) gives the setup flow, [Getting started](./reference/getting-started.md) walks through a first session with your agent, and the [installation architecture](./reference/architecture.md) explains the design.