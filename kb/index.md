# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a **living doctrine for agent-operated knowledge systems, developed and tested by running one**. The doctrine selects and coordinates how model-mediated and symbolic operations are used. Explicit artifacts can [activate](./notes/knowledge-storage-does-not-imply-contextual-activation.md) model capabilities and give their use project authority; code and validators can [faithfully execute](./notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) operations that should not be reconstructed on every call. The doctrine, prompts, code, and models can all change. Like the Ship of Theseus, Commonplace remains the same project through a governed sequence of revisions, not because any component is permanent.

Its first application is an **LLM wiki**, in the sense [AI researcher Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer around a person's or project's work. Human-directed agents develop ideas into retained notes, connect them to evidence and related claims, and revise both the knowledge base and its operating machinery. Humans direct the inquiry and remain responsible for judgments that current evidence and evaluation cannot settle.

The repository is Commonplace's current embodiment. It contains adopted doctrine, research and evidence that can challenge it, and the procedures and code that make it operative. Research does not become doctrine merely by being stored here.

Two separate pressures keep the design modular. Different collections support different kinds of work, so task-specific types and link conventions stay local. Structures can also become obsolete as questions, evidence, or model capabilities change, so local choices remain revisable rather than accumulating by default. Commonplace keeps shared invariants small for both reasons. See why [task-fitted structure costs cross-task reuse](./notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) and why [a framework rule with a boundary-preserving rival is not an inherited constraint](./notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md).

## Threads worth following

**Deployment-time learning.** Durable changes to behavior-shaping prompts, rules, tools, schemas, tests, and code can affect later sessions without updating model weights. Storage is insufficient: later operation must load or enforce the result. [Deploy-time learning](./notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) develops this path, while [bounded context](./notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) explains why selective routing remains necessary. The [learning theory index](./notes/learning-theory-README.md) maps the wider thread.

**Self-improving systems.** A system improves itself only when evidence-responsive change reaches its own behavior-determining organization. One architecture directly updates behavior; another searches candidates, evaluates them, and [retains an accepted proposal](./notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). [Reflection](./notes/definitions/reflective-system.md) is a separate property that provides [addressability](./notes/reflection-buys-addressability.md), not improvement by itself. The [self-improving systems index](./notes/self-improving-systems-README.md) and [Commonplace case](./notes/evidence/commonplace-as-a-reflective-system.md) develop the distinction.

**Agent-usable memory.** Agents need [discoverable, composable, and trusted knowledge under bounded context](./notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). [Explicit link semantics](./notes/links-README.md) expose support, contrast, and consequence; routing selects what reaches a task; provenance and review indicate how strongly to rely on it. Because [information value is observer-relative](./notes/information-value-is-observer-relative.md), useful condensation depends on the consuming agent and task.

**Systems compared.** We reviewed [148 agent memory systems](./agent-memory-systems/README.md), including Mem0, Graphiti, Cognee, and Letta. The [comparative analysis](./agent-memory-systems/agentic-memory-systems-comparative-review.md) finds that activation and verification distinguish the reviewed systems more than storage location. The collection over-samples file-based systems, so its counts describe this corpus rather than the field.

## Browse

- [Notes](./notes/README.md) and [Articles](./articles/README.md) — research claims and self-standing explanations
- [Reference](./reference/README.md) and [Types](./types/README.md) — the current system, decisions, and artifact contracts
- [Agent Memory Systems](./agent-memory-systems/README.md) and [Agentic Systems](./agentic-systems/README.md) — external-system reviews
- [Sources](./sources/README.md), [Instructions](./instructions/README.md), and [Workshops](./work/README.md) — evidence, procedures, and work in flight

## Use it yourself

Commonplace is open source. You can:

- **Vendor the knowledge base read-only** inside a project so agents can consult the research and external-system reviews.
- **Install the system** to give a project the types, conventions, skills, and commands for building its own agent-operated knowledge base.

The [GitHub README](https://github.com/zby/commonplace) covers the tool, [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) gives the setup flow, and the [installation architecture](./reference/architecture.md) explains the design.
