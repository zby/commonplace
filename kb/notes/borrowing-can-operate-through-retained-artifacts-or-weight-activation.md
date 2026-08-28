---
description: Established external methodologies can become operative either by being explicitly retained in the system or by activating a model's pretrained representation; the two routes trade context economy against inspectability and revisability
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, methodology, context-engineering]
---

# Borrowing can operate through retained artifacts or weight activation

Commonplace has treated borrowing from programming, philosophy, law, cognitive science, and other fields mainly as **artifact borrowing**: interpret an external idea, justify its transfer, adapt it to the target system, and retain the resulting claim or methodology in the KB. Pretrained agents add a second route. If an external methodology is already coherently represented in model weights, a prompt can activate it directly without first restating it in Commonplace.

The two routes are:

```text
retained borrowing
external source → adaptation → retained artifact → context → behavior

weight-mediated borrowing
external tradition → pretraining → model weights → compact cue → behavior
```

The distinction changes what it means to borrow from a mature discipline. A field can contribute not only explicit concepts that Commonplace adopts into its writable theory, but also compact names and frames that select substantial pretrained methodological structure at execution time. Established traditions therefore form part of the usable intellectual substrate of an LLM agent even when their contents are not copied into the KB.

The routes have different properties:

| Property | Retained artifact | Weight activation |
|---|---|---|
| Context cost | requires loading some explicit content | can be very low when a compact cue suffices |
| Inspectability | high | low |
| Selective revisability | high | low |
| Versionability | high | model-dependent |
| Project-specific adaptation | direct | indirect unless supplemented in context |
| Fidelity to a canonical interpretation | can be specified | depends on the model's learned reconstruction |

This means the [source-adoption policy](../reference/source-adoption-policy.md) and weight-mediated activation answer different questions. The adoption policy asks whether an idea deserves to become part of Commonplace's retained theory or methodology. Weight activation asks whether an already learned external methodology can be used as part of the current computation. A concept can be useful through the second route without passing the bar for explicit adoption, because using model competence does not make that competence a retained Commonplace commitment.

The routes can also compose. When the model already contains most of a useful methodology but Commonplace needs a project-specific variation, the context can supply only the explicit delta:

```text
weight-resident baseline methodology
        +
retained project-specific modification
        +
current mission and constraints
        ↓
operative methodology for this task
```

For example, a task could invoke *Auftragstaktik* while adding explicit Commonplace-specific constraints on irreversible changes, evidence, or review. The weight-resident doctrine provides context-efficient background structure; retained artifacts specify the parts that must be precise, writable, auditable, or different from the conventional doctrine.

This hybrid explains why the existence of broad model knowledge does not remove the need for an external KB. The model weights provide a large but opaque and effectively read-only methodological library. The KB provides the writable complement: claims and methods whose exact content the system wants to inspect, revise, version, and selectively activate. The design question is therefore not simply whether knowledge exists in weights or in artifacts, but which parts deserve explicit retention and which can safely remain a parametric dependency.

The distinction also creates a new transfer risk. Artifact borrowing can be reviewed against a source and the target-side mechanism. Weight-mediated borrowing additionally depends on whether a particular model actually reconstructs the intended methodology from the cue. A familiar label may activate a distorted, underspecified, or internally mixed representation. Economical activation therefore trades context cost against methodological fidelity.

---

Relevant Notes:

- [Source-adoption policy](../reference/source-adoption-policy.md) — contrasts: governs which borrowed ideas become retained Commonplace commitments; weight activation can use external intellectual machinery without adopting it into retained theory
- [A borrowed pattern transfers only as far as source and target share a mechanism](./borrowed-patterns-transfer-only-over-shared-mechanism.md) — constrains: explicit adoption still requires a target-side transfer argument; pretrained familiarity does not establish valid transfer
- [Weight-resident methodologies provide context-efficient behavioral compression](./weight-resident-methodologies-provide-context-efficient-behavioral-compression.md) — mechanism: explains why the weight-mediated route can be much cheaper in context
- [Only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — distinguishes: model competence can govern behavior without becoming retained, writable project theory
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — mechanism: both retained and parametric knowledge still require activation before they affect behavior
