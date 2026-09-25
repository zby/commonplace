---
description: "Definition - representational form classifies how content is encoded and consumed: natural-language, symbolic, distributed-parametric, or mixed"
type: definition
tags: [learning-theory, artifact-analysis]
---

# Representational form

Representational form classifies how content is encoded and consumed. This KB uses three coarse forms: **natural-language**, **symbolic**, and **distributed-parametric**. Mixed artifacts are split by [operative part](./operative-part.md) or consumption path when the parts have different review evidence, invalidation needs, or rollback paths.

## Scope

**Natural-language** content gets its consequences from interpretation by a language model or human. Prompts, reflections, notes, policies, playbooks, and many skills are natural-language.

**Symbolic** content sits in localized units with a unique operational semantics: fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, or similar consumer, determine what behavior is permitted, including any variation they explicitly allow. The category is architectural, not a claim about classical symbolic AI.

**Distributed-parametric** content is numerical state distributed across parameters or dense representations: weights, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and similar artifacts.

Form sets the default inspection method: read natural-language content, test or statically check symbolic artifacts, and probe distributed-parametric artifacts behaviorally.

Form also sets what a commitment leaves open: [constraining](./constraining.md) in natural language leaves reasonable readings at its edges and depends on an interpreter that fails to comply at some rate, while symbolic commitment settles by fixed rules what is permitted. Moves between forms are named operations: [codification](./codification.md) moves content from natural-language into symbolic form, [relaxing](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) replaces a constrained component with a more general one, and training moves content into distributed-parametric form.

## Derivation

Two axes generate the categories. **Assigned consequences** — does the artifact have a unique operational semantics — fixed rules that determine what it permits — or is it reinterpreted on each consumption? A formal semantics is sufficient but not necessary: most programming languages have none, and still sit on this side because their implementations aim at a unique operational semantics, so two consumers disagreeing about what the rules permit means one of them is wrong. Natural language has no such adjudicator — two readings can both be reasonable — which is [underspecification](../agentic-systems-interpret-underspecified-instructions.md), not a defect of any particular text. **Localization** — is there an identifiable unit carrying the content, or is it spread across numerical state with no addressable part?

| | localized | non-localized |
|---|---|---|
| **consequences assigned** | symbolic | — |
| **consequences not assigned** | natural-language | distributed-parametric |

The fourth cell is unoccupied in this domain rather than impossible. Vector symbolic architectures aim at exactly it, binding and bundling being algebraically defined operations over distributed hypervectors. The three-way carve therefore holds while agent systems retain nothing of that shape, and gains a fourth form if they do.

The inspection rule above follows from the axes instead of being stipulated per form: a localized unit with a unique operational semantics can be checked against it (test), a localized unit without one yields its content only to interpretation (read), and a non-localized artifact offers nothing to point at, so only its behavior is observable (probe). [Addressability](./addressable-theory.md) rides on the localization axis alone, which is why an instruction and a validator are both revisable one item at a time while weights are not. The parts available for inspection and separate revision in an addressable theory occupy the localized side, while the assigned-consequences axis fixes whether a contradiction is computed or interpreted.

Because natural-language and symbolic share the localized side of the table, the pair is referred to jointly as **the localized forms** — the class name reads the localization axis off rather than adding vocabulary. "Readable artifacts" and "the readable pair" remain informal aliases; prefer the derived name where the carve matters.

## Exclusions

Representational form is not storage substrate. Markdown in a repository can be natural-language, symbolic, or mixed depending on the consumer. A vector store can expose natural-language records while its retrieval behavior depends on distributed-parametric embeddings and ranking.

**Localized** is a claim about unit structure, not about locality of reference: it means an identifiable unit carries the content, not that the content is specific to one deployment. Deployment-specific facts can be retained in any form, including weights.

Representational form is not [behavioral authority](./behavioral-authority.md). Form says how content is encoded and gets its consequences; authority says which consumer applies it, through which channel, and with what force. A natural-language instruction can bind a worker, and a symbolic schema can be merely advisory.

Representational form is also not consumption path. **Prompt** is exact when material is supplied, or explicitly assembled to be supplied, as model input. A stored note, policy, or memory record is not thereby a prompt because it might later be retrieved; retain its precise artifact name, or call it natural-language when the representational category matters. A generated model-input view can be a prompt even when it assembles natural-language and symbolic operative parts. Apply the vocabulary in this order: name the precise artifact when the category adds nothing; use **prompt** when model-input supply is the point; use **natural-language** when representational form matters; keep **prose** for editorial meaning, quotations, historical terminology, and named review machinery.

## Misuse Cases

- Calling learned weights "opaque" as if opacity were the form. The form is distributed-parametric; opacity is a practical inspection property that [appears at sufficient scale](../opacity-is-a-scale-threshold.md) in natural-language and symbolic systems too.
- Calling natural-language content "prose". The boundary is interpretive, not editorial: fragments, facts, structured records, and rules are natural-language when they get their consequences through interpretation, though none of them is continuous prose.
- Counting a fixed prompt and model as symbolic because its behavior repeats. Repeatability is not a unique operational semantics: another model can read the same prompt differently without either being wrong.
- Calling every YAML or Markdown artifact symbolic. It is symbolic only where specific fields, values, or structures have a unique operational semantics.

---

Relevant Notes:

- [operative part](./operative-part.md) — defined-in: the unit for splitting mixed artifacts, not necessarily the whole stored object
- [constraining](./constraining.md) — defined-in: form decides what a commitment leaves open
- [codification](./codification.md) — defined-in: the move from natural-language into symbolic form
- [storage substrate](./storage-substrate.md) — contrasts: where content is stored, separate from how it is encoded
- [behavioral authority](./behavioral-authority.md) — contrasts: which consumer applies content, through which channel, and with what force
- [opacity is a scale threshold](../opacity-is-a-scale-threshold.md) — contrasts: practical opacity is not the same as distributed-parametric form
- [addressable theory](./addressable-theory.md) — extends: the localized side supplies parts for inspection and separate revision; the assigned-consequences axis fixes whether a contradiction is computed or interpreted
- [codification and relaxing navigate the bitter-lesson boundary](../codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: when to relax a symbolic commitment
