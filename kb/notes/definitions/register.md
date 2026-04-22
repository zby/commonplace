---
description: "Definition — a register is one of three content modes (theoretical, descriptive, prescriptive) that determines a collection's quality goal, title conventions, and linking rules"
type: kb/types/definition.md
tags: [document-system]
status: current
---

# Register

One of three content modes that classifies what a knowledge artifact *says* — its orientation toward knowledge. Each register has a distinct quality goal and writing conventions:

| Register | Orientation | Quality goal | Title style |
|---|---|---|---|
| **Theoretical** | Claims about what is true | Reach | Claim |
| **Descriptive** | Accounts for what exists | Fidelity + economy | Topical |
| **Prescriptive** | Directs what to do | Executability + precision | Imperative |

In this KB, registers map to collections: `kb/notes/` (theoretical), `kb/reference/` (descriptive), `kb/instructions/` (prescriptive). This is a design choice — registers could also be encoded in types, metadata, or convention. Directories work because they make conventions enforceable by path and visible to tooling.

The three registers are exhaustive because they correspond to the three fundamental orientations toward knowledge: understanding why, representing what exists, and directing action. Every question a consumer asks reduces to "Why is X a good idea?", "How does X work here?", or "How do I do X?"

Registers are orthogonal to operational roles (what an artifact *does* in the system — evidence, executable instruction, generated report, routing surface). A `note` type in `kb/notes/` is theoretical; the same type in `kb/reference/` is descriptive. Register × type gives the full picture.

Two properties make the distinction real: the **formulation constraint** (theories must be statable in general terms, without referencing a particular system) and **maintenance asymmetry** (changes flow downstream from theory through prescriptions into descriptions).

Register shapes link vocabulary through defaults, not inheritance. Each register has a characteristic link grammar — inference labels (extends, grounds, mechanism, contrasts) for theoretical, structural labels (part-of, implements) for descriptive, operational labels (composition, precondition, invokes) for prescriptive. These are *defaults* offered as starting templates when a new collection is authored; the authoritative home of a collection's outbound grammar is its own `COLLECTION.md`, not the register. Collections can diverge from the register default when their work requires it.

Cross-register links use a shared, smaller vocabulary (rationale, evidence, procedure, operates-on, defined-in) drawn from a common catalogue. A reader crossing a register boundary typically has a different unmet need (operational vs. evidential vs. definitional) than one moving within, and both endpoints need to recognise the label — so the vocabulary is shared across collections rather than owned by any single one.

---

Relevant Notes:

- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md) — foundation: the full argument for three exhaustive registers with formulation constraint and maintenance asymmetry
- [distillation](./distillation.md) — enables: distillation connects registers through the theory → prescription → implementation → description chain
- [constraining](./constraining.md) — co-equal mechanism: orthogonal to registers but interacts — prescriptions are more constrained than theories
