# Commonplace

**Research on knowledge systems, running as one.**

Commonplace studies how agentic systems can change after deployment through inspectable knowledge artifacts. It also puts that idea into practice: human-directed agents use and revise the Markdown, instructions, schemas, validators, tests, and code in this repository. When later work loads or enforces those artifacts, accepted changes can shape behavior without updating model weights. The repository makes both the mechanism and its governance visible.

The theory's most immediate target is an **LLM wiki**, in the sense [AI researcher Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer that agents build and maintain around a person's or project's work. An agent can turn a vague thought into a committed note, then [place it among relevant artifacts](./notes/links-README.md). Links help later readers find the note and decide what related material to follow. This turns an ephemeral exchange into inspectable material that can be reused. Agents can help draft, file, connect, and review it; humans direct the inquiry and remain responsible for judgments that the available evidence and review process cannot settle.

That ease creates a maintenance problem. Tags, indexes, and templates become debt when they outlive the questions that justified them. Commonplace therefore keeps shared invariants small and lets each collection's local contract define its task-specific types and link conventions. This design follows two related constraints: [task-fitted structure costs cross-task reuse](./notes/task-fitted-structure-costs-cross-task-reuse.md), and [a framework rule counts as an inherited constraint only when no rival preserves its boundary invariants](./notes/a-framework-rule-is-inherited-only-without-a-boundary-preserving-rival.md).

Commonplace is **self-hosting** in a limited, bootstrapping sense: its research corpus and parts of its operating machinery live together. `kb/` contains theory, procedures, and external evidence; `src/commonplace/`, schemas, validators, and tests implement the framework. Not every artifact describes Commonplace; some analyze external systems. The narrower claim is that selected artifacts describe or direct the system that consumes them, and that accepted changes can reach later operations through explicit loading or enforcement. Methodology and symbolic machinery need not change in lockstep. When a pattern [codifies](./notes/definitions/codification.md) into a command or check, however, its rationale and enforcement should remain traceable.

The core research thread is **[deploy-time learning](./notes/deploy-time-learning-is-the-missing-middle.md)**: durable behavior-shaping artifacts can be updated across sessions while a system is deployed. Storing an artifact is not enough; a later consumer must load or enforce it in a way that can affect behavior. Because agents operate under [bounded context](./notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), they need selective access to task-relevant artifacts rather than universal loading. Even when a change affects behavior, whether it improves performance remains an empirical question. The notes develop this theory and apply it to agent-operated knowledge bases.

Three distinctions keep these claims precise. A methodology is [actionable](./notes/definitions/actionable-methodology.md) only relative to an operator, available operations, a target, and a setting; here, human-directed LLM agents are among the operators. A system is [reflective](./notes/definitions/reflective-system.md) only where an internal process can use a representation of that same system. Changes in the represented aspects can update the representation, and operations mediated through it can affect later behavior. [Reflective coverage](./notes/reflective-coverage-is-graded-across-representational-forms.md) asks which representational forms and operations participate; coverage over natural-language and symbolic artifacts does not imply coverage over model weights. Coverage presupposes reflection. None of these properties alone shows that a change improved the system.

## Threads worth following

**How agents learn.** [Deploy-time learning](./notes/deploy-time-learning-is-the-missing-middle.md) names a third timescale alongside training and within-session adaptation: changes to durable behavior-shaping artifacts across sessions. [Constraining](./notes/definitions/constraining.md) narrows interpretation; at its far end, stable patterns can be [codified](./notes/definitions/codification.md) as deterministic checks or code. [Conjecture](./notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) supplies candidate explanations that may work beyond the cases that produced them. The [learning theory index](./notes/learning-theory-README.md) maps the full landscape.

**Self-improving systems.** [Membership](./notes/definitions/self-improving-system.md) requires operative, evidence-responsive change to the system's own behavior-determining organization. Evidence directly determines a change in one update architecture. In another, the system searches candidates, evaluates them, and [retains an accepted proposal](./notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md); hybrid pathways combine these functions. [Reflection](./notes/definitions/reflective-system.md) is a separate structural property. It provides [addressability](./notes/reflection-buys-addressability.md), but does not by itself establish improvement or cumulative dependence. The [self-improving systems index](./notes/self-improving-systems-README.md) routes the full cluster, and [Commonplace as a reflective system](./reference/commonplace-as-a-reflective-system.md) works through a local case.

**What makes memory agent-usable.** Agent memory needs [discoverable, composable, and trusted knowledge under bounded context](./notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). Discoverable knowledge can be selected for a task without loading everything. Composable knowledge exposes relationships through [explicit link semantics](./notes/links-README.md), so readers can follow lines of support, contrast, or consequence. Trusted knowledge offers enough signal—such as rationale, provenance, status, validation, ownership, or review—for an agent to rely on it at the right level of confidence. Whether using that knowledge improves future action is a separate evaluation question for the surrounding memory system.

**Information and bounded observers.** [Information value is observer-relative](./notes/information-value-is-observer-relative.md): the same data can expose extractable structure to one observer and noise to another. Condensing material for a bounded observer can therefore create value. By contrast, [reverse-compression](./notes/reverse-compression-is-when-llm-output-expands-without-adding.md) expands text without adding extractable structure.

**Agent memory systems compared.** We reviewed [148 agent memory systems](./agent-memory-systems/README.md) — Mem0, Graphiti, Cognee, Letta, and more — across shared architectural axes. The [comparative analysis](./agent-memory-systems/agentic-memory-systems-comparative-review.md) finds that how systems activate and verify memory distinguishes them more than where they store it. The collection over-samples file-based systems, so its counts describe this corpus rather than the field as a whole.

## Browse

Each top-level collection has a curated README, and those landing pages appear in the top menu:

- [Notes](./notes/README.md) — the research itself; the [tag indexes](./notes/tags-README.md) give finer-grained entry points
- [Articles](./articles/README.md) — self-standing technical writing distilled from the knowledge base
- [Reference](./reference/README.md) — the shipped system: architecture, type system, CLI, ADRs
- [Types](./types/README.md) — global artifact contracts and their deterministic schemas
- [Agent Memory Systems](./agent-memory-systems/README.md) and [Agentic Systems](./agentic-systems/README.md) — reviews of external systems
- [Sources](./sources/README.md) — snapshotted external material with analysis
- [Instructions](./instructions/README.md) — procedures, skills, and review gates
- [Workshops](./work/README.md) — work currently in flight

## Use it yourself

Commonplace is open source. You can use it in two ways.

**Vendor this knowledge base read-only inside your project.** Add it as a git submodule or plain copy, then give agents a routing instruction that says when and where to consult it. This makes the research, external-system reviews, and sources available; it does not guarantee that agents will activate every relevant item. Because the content is Markdown, reading it requires neither Python nor any particular implementation language.

**Install the system into your own project.** Your agents get the type system, conventions, and skills for accumulating knowledge about that project's domain. The installed package carries the methodology but not this repository's external-system reviews or source snapshots.

The [GitHub README](https://github.com/zby/commonplace) covers the tool side; [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) gives the setup flow; and the [installation architecture](./reference/architecture.md) explains the design. To contribute to the research itself, clone the repository; it is already a functioning knowledge base.
