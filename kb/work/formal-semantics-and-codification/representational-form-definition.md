# Representational form (proposed definition)

Workshop draft, 2026-11-01. This file is the complete proposed text of the library's [representational form](../../theory/definitions/representational-form.md) definition, written from the [account of symbolic form](./symbolic-form-and-codification.md). The natural-language and symbolic forms, the assigned-consequences axis, the inspection rule, the opaque modifier and the misuse cases are new; the distributed-parametric form, the localization axis, the table and the exclusions are carried over unchanged or with one phrase replaced. Links are written for this file's location and change on promotion. The library definition remains authoritative until then. Open questions about the wording are at the end.

---

Representational form classifies how content is encoded and consumed. This KB uses three coarse forms: **natural-language**, **symbolic**, and **distributed-parametric**. Form is a property of an artifact under a consumption path: the same text can be natural-language under one path and symbolic under another. Mixed artifacts are split by [operative part](../../theory/definitions/operative-part.md) or consumption path when the parts have different review evidence, invalidation needs, or rollback paths.

## Scope

**Natural-language** content gets its consequences from interpretation on each consumption. Its users hold consumers to no reference that fixes what it permits. The conventions of a language community make some readings wrong, whether or not the author is available, and two readings can both be reasonable. A consumer that cannot settle a reading asks the author, or chooses, and the choice is its own. Prompts, reflections, notes, policies, playbooks, and many skills are natural-language.

**Symbolic** content sits in localized units whose consequences, under the consumption path in question, are fixed by the reference of a language that has a formal semantics or is close to one. A language is close to a formal semantics when its users hold its consumers to a reference, whether a standard or an implementation, from which a formal semantics could be derived. A consumer that is held to the reference and departs from it is wrong. Fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, adopted model package, or similar consumer, determine what behavior is permitted, including any variation, external selection, or clarification step they explicitly provide for. The category is architectural, not a claim about classical symbolic AI.

**Distributed-parametric** content is numerical state distributed across parameters or dense representations: weights, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and similar artifacts.

Symbolic content is **opaque** under a consumption path when the reference that assigns its consequences cannot be read rule by rule. Opacity has three sources: the artifact's scale, where each unit is readable against the reference and the whole is not; the reference's form, where the reference is itself distributed-parametric, as a frozen model package is, so that even a one-line artifact's consequences cannot be read; and deliberate obfuscation, where a function-preserving transformation is chosen to show as little as possible. Opaque content is still symbolic: what counts as wrong is fixed. What it loses is checking by reading and revision by locating the rule. Where the reference is distributed-parametric it also loses declared gaps, since the package declares none and its gaps are found on use. Opacity is an inspection property, not a form ([opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md)). Write the modifier only where readability is at issue; unmodified "symbolic" says nothing about it.

Form sets the default inspection method. Read natural-language content. Check symbolic artifacts against their reference, by reading where they are not opaque and by running cases where they are. Probe distributed-parametric artifacts behaviorally.

Form also sets what a commitment leaves open. [Constraining](../../theory/definitions/constraining.md) in natural language leaves reasonable readings at its edges and depends on an interpreter that fails to comply at some rate. Symbolic commitment settles by fixed rules what is permitted, and what the reference leaves open is permitted variation, a required external selection, or a defect. Only the last is a failure of the reference. Moves between forms are named operations: [codification](./codification-definition.md) moves content from natural-language into symbolic form, by rewriting it or by adopting a consumer as its reference; [relaxing](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) replaces a constrained component with a more general one; and training moves content into distributed-parametric form.

## Derivation

Two axes generate the categories. **Assigned consequences** — under the consumption path in question, are the artifact's consequences fixed by the reference of a language close to a formal semantics, or is the artifact reinterpreted on each consumption? If two consumers held to one reference disagree about what the rules permit, one of them is wrong. Content no reference fixes can carry two reasonable readings, which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), not a defect of any particular text.

A written formal semantics is neither necessary nor sufficient for assigned consequences. Many programming languages have none and still sit on this side, because their users hold implementations to a reference from which one could be derived. A formal semantics can be derived from an implementation together with a machine model, or from a specification that states which expressions count and under what conditions an action is permitted. It cannot be derived from a human judge, so a reference that settles by judgment about what was intended governs without assigning consequences.

A formalization of a consumer is not the semantics of the language it consumes: a frozen model's computation can be formally described without the model becoming the reference for the English it consumes. The model becomes the reference only for the prompts of a system that adopts it for an operation.

**Localization** — is there an identifiable unit carrying the content, or is it spread across numerical state with no addressable part?

| | localized | non-localized |
|---|---|---|
| **consequences assigned** | symbolic | — |
| **consequences not assigned** | natural-language | distributed-parametric |

The fourth cell is unoccupied in this domain rather than impossible. Vector symbolic architectures aim at exactly this cell: binding and bundling are algebraically defined operations over distributed hypervectors. The three-way division therefore holds while agent systems retain nothing of that shape, and gains a fourth form if they do.

The inspection rule above follows from the axes instead of being stated separately for each form: a localized unit whose language's users hold consumers to a reference can be checked against that reference, a localized unit without one gives its content only through interpretation (read), and a non-localized artifact offers nothing to point at, so only its behavior is observable (probe). Within the first case, the reference has a form of its own, and that form decides whether the check is by reading or by running cases.

[Addressability](../../theory/definitions/addressable-theory.md) depends on the localization axis alone, which is why an instruction and a validator are both revisable one item at a time while weights are not. A prompt under an adopted model is the opaque case: it stays revisable as a part while the rule assigning its consequences does not. The parts available for inspection and separate revision in an addressable theory occupy the localized side, while the assigned-consequences axis fixes whether a contradiction is computed or interpreted.

Because natural-language and symbolic share the localized side of the table, the pair is referred to jointly as **the localized forms**. The class name comes from the localization axis. "Readable artifacts" and "the readable pair" remain informal aliases. Prefer the derived name where the division matters. The alias is loose, since symbolic content can be opaque.

## Exclusions

Representational form is not storage substrate. Markdown in a repository can be natural-language, symbolic, or mixed depending on the consumer. A vector store can expose natural-language records while its retrieval behavior depends on distributed-parametric embeddings and ranking.

**Localized** means an identifiable unit carries the content. It does not mean the content is specific to one deployment. Deployment-specific facts can be retained in any form, including weights.

Representational form is not readability. "Symbolic" says that what counts as wrong is fixed; whether the reference can be read is the opaque modifier's question.

Representational form is not [behavioral authority](../../theory/definitions/behavioral-authority.md). Form says how content is encoded and gets its consequences; authority says which consumer applies it, through which channel, and with what force. A natural-language instruction can bind a worker, and a symbolic schema can be merely advisory.

Representational form is also not consumption path, though form is determined under one. **Prompt** is exact when material is supplied, or explicitly assembled to be supplied, as model input. A stored note, policy, or memory record does not become a prompt by being retrievable later. Keep its precise artifact name, or call it natural-language when the representational category matters. A generated model-input view can be a prompt even when it assembles natural-language and symbolic operative parts. Apply the vocabulary in this order: name the precise artifact when the category adds nothing; use **prompt** when model-input supply is the point; use **natural-language** when representational form matters; keep **prose** for editorial meaning, quotations, historical terminology, and named review machinery.

## Misuse Cases

- Calling learned weights "opaque" as if opacity were the form. The form is distributed-parametric; opacity is a modifier on symbolic form and a practical inspection property elsewhere, with [scale](../../theory/opacity-is-a-scale-threshold.md) as one of its sources.
- Calling natural-language content "prose". The boundary is interpretive, not editorial: fragments, facts, structured records, and rules are natural-language when they get their consequences through interpretation, though none of them is continuous prose.
- Counting a fixed prompt and model as symbolic because its behavior repeats. Repeatability is not adoption: a prompt becomes symbolic under a consumption path only when a system adopts the model package, decoding included, as the reference for that operation. Under any other consumption path the same prompt is natural-language, and no adoption makes the package a reference for English.
- Denying that a prompt under a pinned, adopted model is symbolic because the model cannot be read. It is symbolic and opaque under that consumption path, and it lacks the advantages of ordinary code for that reason.
- Taking a formalization of a consumer for the semantics of the language it consumes. Any implemented consumer together with a machine model has a formal account of its own behavior; that account is the semantics of a language only when the language's users hold consumers to it.
- Calling every YAML or Markdown artifact symbolic. It is symbolic only where a consumer holds specific fields, values, or structures to a reference.

---

Relevant Notes:

- [operative part](../../theory/definitions/operative-part.md) — defined-in: the unit for splitting mixed artifacts, not necessarily the whole stored object
- [constraining](../../theory/definitions/constraining.md) — defined-in: form decides what a commitment leaves open
- [codification](./codification-definition.md) — defined-in: the move from natural-language into symbolic form, by rewriting or by adoption
- [storage substrate](../../theory/definitions/storage-substrate.md) — contrasts: where content is stored, separate from how it is encoded
- [behavioral authority](../../theory/definitions/behavioral-authority.md) — contrasts: which consumer applies content, through which channel, and with what force
- [opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md) — contrasts: scale is one source of the opaque modifier, not the only one
- [addressable theory](../../theory/definitions/addressable-theory.md) — extends: the localized side supplies parts for inspection and separate revision; the assigned-consequences axis fixes whether a contradiction is computed or interpreted
- [codification and relaxing navigate the bitter-lesson boundary](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: when to relax a symbolic commitment
- [Barak and co-authors, On the (Im)possibility of Obfuscating Programs](../../sources/on-the-impossibility-of-obfuscating-programs.ingest.md) — evidenced-by: deliberate obfuscation as a non-scale source of opacity; the strong form of hiding is impossible in general because reading a program can exceed running it
- [Jain, Lin and Sahai, Indistinguishability Obfuscation from Well-Founded Assumptions](../../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md) — evidenced-by: the weaker provable notion exists under four assumptions; cited for existence and scope only

---

## Open questions about the wording

1. "Close to a formal semantics" names a graded thing with a two-valued gloss. Does the library want the three grades the account states, formal semantics, close, and neither, or only the boundary?
2. Should the three sources of opacity live here, in the opacity note, or in both? The note's title says opacity comes from scale, and two of the sources do not.
3. The criterion now sits in this definition and codification points to it, reversing the current pointer. Which library notes link codification for the test and need to link form instead?
4. The natural-language paragraph says conventions make some readings wrong "whether or not the author is available". That clause comes from the side theory, which the definitions must not depend on. Keep it as a claim of the definition, or cut it?
5. Does the boundary table in the [account](./symbolic-form-and-codification.md) survive a reviewer adding cases?
