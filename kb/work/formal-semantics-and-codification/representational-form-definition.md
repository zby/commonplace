# Representational form (proposed definition)

Workshop draft, 2026-11-01. This file is the complete proposed text of the library's [representational form](../../theory/definitions/representational-form.md) definition, written from the [account of symbolic form](./symbolic-form-and-codification.md). The natural-language and symbolic forms, the assigned-consequences question, the ordered presentation of the two questions, the inspection rule, the opaque modifier and the misuse cases are new; the distributed-parametric form, the localization question and the exclusions are carried over unchanged or with one phrase replaced. Links are written for this file's location and change on promotion. The library definition remains authoritative until then. Conceptual and presentation decisions, review checks and promotion tasks are explained in the [question register](./decisions-and-open-questions.md).

---

Representational form classifies how content is encoded and consumed. This KB uses three coarse forms: **natural-language**, **symbolic**, and **distributed-parametric**. Form is a property of an artifact under a consumption path: the same text can be natural-language under one path and symbolic under another, and the same weights are addressed unit by unit by the runtime that executes them and as a whole by the system that runs the model as its interpreter.

Mixed artifacts are split by [operative part](../../theory/definitions/operative-part.md) or consumption path when the parts have different review evidence, invalidation needs, or rollback paths.

## Scope

### The three forms

A policy that says "escalate serious incidents" is read by whoever handles the incident, and two handlers can disagree about what counts as serious without either being wrong. That is **natural-language** content: it gets its consequences from interpretation on each consumption, and its users hold consumers to no reference that fixes what it permits. The conventions of a language community make some readings wrong, whether or not the author is available, and two readings can both be reasonable. A consumer that cannot settle a reading asks the author, or chooses, and the choice is its own. Prompts, reflections, notes, policies, playbooks, and many skills are natural-language.

A route table read by its resolver, or a Python script run by CPython at a version, has consequences the resolver or the language reference fixes, and a resolver that departs from the table is wrong. That is **symbolic** content: it sits in localized units whose consequences, under the consumption path in question, are fixed by the reference of a language that has a formal semantics or is close to one.

A language is close to a formal semantics when its users hold its consumers to a reference, whether a standard or an implementation, from which a formal semantics could be derived. A consumer that is held to the reference and departs from it is wrong. Adopting a reference does not establish its adequacy to the task. Fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, adopted model package, or similar consumer, determine what behavior is permitted, including any variation, external selection, or clarification step they explicitly provide for. The category is architectural, not a claim about classical symbolic AI.

The weights of a model that a system runs as its interpreter carry what the model does with "summarize", and no part of them carries that item; the system addresses the weights as a whole. That is **distributed-parametric** content: numerical state distributed across parameters or dense representations, with no part the consumer on that path addresses. Weights, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and similar artifacts are distributed-parametric under the path on which a system runs them as models. The runtime that executes the same weights addresses them kernel by kernel and parameter by parameter, and under that path they are symbolic data, as the derivation below states.

### Opacity and inspection

A one-line prompt under an adopted model package can be easy to read while the effect of editing it is hard to predict. A large program can be readable line by line but difficult to understand as a whole. An obfuscated program is deliberately arranged to obstruct understanding. These illustrate three sources of opacity: the reference's form, the artifact's scale and deliberate obfuscation.

Symbolic content is **opaque** under a consumption path, relative to a behavior or change of interest, when the artifact together with its reference does not let an inspector establish that behavior, or the effect of that change, at acceptable cost. Evaluation then relies more on execution, other analysis such as abstraction or certificates, or explicitly retained uncertainty.

Opacity does not change what the reference specifies, including declared variation and failure outputs. It removes an affordable inspection route for the question at hand. It is an inspection property, not a form ([opacity is a scale threshold](../../theory/opacity-depends-on-the-inspection-question-and-budget.md)). Write the modifier only where readability is at issue; unmodified "symbolic" says nothing about it. The [account](./symbolic-form-and-codification.md#opaque-symbolic-form) retains the mechanisms and obfuscation evidence for later promotion to the opacity note.

Form sets the default inspection method. Read natural-language content. Check symbolic artifacts against their reference, by reading where they are not opaque and by running cases or other analysis where they are. Probe distributed-parametric artifacts behaviorally.

### Commitments and moves between forms

Form also sets what a commitment leaves open. [Constraining](../../theory/definitions/constraining.md) in natural language leaves reasonable readings at its edges and depends on an interpreter that fails to comply at some rate. Symbolic commitment settles by fixed rules what is permitted, and what the reference leaves open is permitted variation, a required external selection, an excluded guarantee, or a defect. Only the last is a failure of the reference.

Moves between forms are named operations: [codification](./codification-definition.md) moves content from natural-language into symbolic form, by rewriting it or by adopting a consumer as its reference; [relaxing](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) replaces a constrained component with a more general one; and training moves content into distributed-parametric form.

## Derivation

Two questions generate the categories, both read under the consumption path in question: first localization, then assigned consequences where the content is localized.

### Localization

The runtime that executes a model addresses its weights kernel by kernel and parameter by parameter, and the pinned runtime fixes what each does. The system that runs the whole model as its interpreter addresses nothing in them. The same weights are localized under the first path and not under the second, and that is the localization question.

**Localization** — under the consumption path in question, are there separately identifiable units carrying the content that can be inspected or revised as such, an instruction, a claim, a field, an expression or a numerical operand, or is the content spread across numerical state with no such unit?

A unit counts when the consumer on that path takes it up as a unit to interpret, check or execute, not when storage is merely accessed. Whether anything fixes its consequences is the next question. A policy clause is a unit for its reader, though reading it requires interpretation. A schema field is a unit for its validator, and its consequences are assigned. A tensor operand is a unit for the runtime that executes it. The model's instruction-level commitments, what it does with "summarize", are exposed as no separate unit under the interpreter path: that path takes up the prompt's tokens, so the prompt is localized there, and the package's rule is not.

Localization is relative to the path as form is: under the runtime's path the weights are symbolic and opaque by scale, under the interpreter's path they are distributed-parametric, and adopting the package does not change that.

Behind an API, a compiled program and a neural model are alike under the caller's path, where the artifact is the request and the API contract its reference; they differ under the paths inside, where the program's rule for an input is a routine its compiler takes up as a unit and the model's instruction-level rule is not exposed as a separately identifiable unit under that path.

### Assigned consequences

Where the C standard requires one result, two compilers producing different results cannot both conform. Two readers of a policy who disagree about what it requires can both be reasonable. That difference is the assigned-consequences question.

**Assigned consequences** — under the consumption path in question, are the consequences of the artifact's units fixed by the reference of a language close to a formal semantics, or are the units reinterpreted on each consumption?

The question is asked of units, because a reference assigns consequences to units: what an expression evaluates to, what a field permits, what an instruction does. If two consumers held to one reference disagree about what the rules permit, one of them is wrong. Content no reference fixes can carry two reasonable readings, which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), not a defect of any particular text.

Python implementations are held to a language reference, with CPython supplying implementation-specific behavior. Classifying a Python script as symbolic does not require a separately written formal semantics.

A separately written formal semantics is not necessary: an implementation and a machine model can supply the formal account. Nor is a formal description of a consumer sufficient: the description must be adopted as the governing reference, or shown to conform to it.

A formal semantics can also be derived from a specification that states which expressions count and under what conditions an action is permitted. A contract clause under a designated arbitrator illustrates why designation alone is insufficient: unformalized judgment governs without supplying mechanically applicable rules. The exclusion is the unformalized judgment, not the human: a workflow step that waits for a human approval is symbolic, because the engine takes the decision as an input, a required external selection, without formalizing the judgment; and a human following a formal procedure is Turing's clerk.

### Formalizing a consumer and adopting a reference

GCC's behavior can be formally described, and so can a frozen model's. The description of GCC describes that implementation, bugs and extensions included. Whether it realizes C is a separate conformance claim, settled against the standard, because C's users hold every compiler to the standard. Where GCC departs from the standard, the description therefore records a bug in GCC and not a fact about C.

The description of the model answers to nothing that English's users hold readers to, so where the model departs from a reader's reading, the disagreement alone does not establish which reading is wrong: both may be reasonable, or either may violate the instruction, as a model that reads "exclude archived records" as "include" does.

A formalization of a consumer is not the semantics of the language it consumes: a frozen model's computation can be formally described without the model becoming the reference for the English it consumes. The model becomes the reference only for the prompts of a system that adopts it for an operation.

### Categories and their inspection methods

| Localized under the path | Consequences assigned | Form |
|---|---|---|
| yes | yes | symbolic |
| yes | no | natural-language |
| no, content distributed across numerical state | not applicable | distributed-parametric |

The third row answers the first question with no, and the second question is then not asked. Assigning consequences is a relation between a unit and a reference, so it has no subject where there are no units. An adopted package's behavior as a whole is fixed, and the package is still distributed-parametric under the interpreter's path, because the whole is the trivial unit, and if the trivial unit counted nothing would be non-localized.

The second row is a no to the second question, which is a different thing: natural-language units are reinterpreted on each consumption.

A system that addressed distributed state through algebraically defined operations, as vector symbolic architectures do with binding and bundling over hypervectors, would be localized under that path, so it would sit in the symbolic cell rather than open a fourth form.

A schema is checked against its validator, a note is read, and a model is probed with inputs. The inspection rule above follows from these questions instead of being stated separately for each form: a localized unit whose language's users hold consumers to a reference can be checked against that reference, a localized unit without one gives its content only through interpretation (read), and a non-localized artifact offers nothing to point at, so only its behavior is observable (probe).

Within the first case, whether inspection is affordable or the check needs execution or other analysis is the opaque modifier's question: a short script is read, and a prompt under an adopted package is run.

### Addressability and the localized forms

An instruction and a validator are both revisable one item at a time; the weights a system runs as its interpreter are not. [Addressability](../../theory/definitions/addressable-theory.md) depends on the localization question alone. A prompt under an adopted model is the opaque case: it stays revisable as a part while the rule assigning its consequences does not.

Addressability is read under the path too: a parameter is addressable under the runtime's path, and editing it can change behavior under the interpreter's path without identifying which instruction-level commitment the edit revises. The parts available for inspection and separate revision in an addressable theory occupy the localized side, while the assigned-consequences question fixes whether a contradiction is computed or interpreted.

Because natural-language and symbolic both answer the first question with yes, the pair is referred to jointly as **the localized forms**. The class name comes from the localization question. "Readable artifacts" and "the readable pair" remain informal aliases. Prefer the derived name where the division matters. The alias is loose, since symbolic content can be opaque.

## Exclusions

Representational form is not storage substrate. Markdown in a repository can be natural-language, symbolic, or mixed depending on the consumer. A vector store can expose natural-language records while its retrieval behavior depends on distributed-parametric embeddings and ranking.

**Localized** means an identifiable unit carries the content. It does not mean the content is specific to one deployment. Deployment-specific facts can be retained in any form, including weights.

Representational form is not readability. "Symbolic" says that what counts as wrong is fixed; whether the artifact and its reference can be inspected for the behavior in question is the opaque modifier's question.

Representational form is not [behavioral authority](../../theory/definitions/behavioral-authority.md). Form says how content is encoded and gets its consequences; authority says which consumer applies it, through which channel, and with what force. A natural-language instruction can bind a worker, and a symbolic schema can be merely advisory.

Representational form is also not consumption path, though form is determined under one. **Prompt** is exact when material is supplied, or explicitly assembled to be supplied, as model input. A stored note, policy, or memory record does not become a prompt by being retrievable later. Keep its precise artifact name, or call it natural-language when the representational category matters. A generated model-input view can be a prompt even when it assembles natural-language and symbolic operative parts. Apply the vocabulary in this order: name the precise artifact when the category adds nothing; use **prompt** when model-input supply is the point; use **natural-language** when representational form matters; keep **prose** for editorial meaning, quotations, historical terminology, and named review machinery.

## Misuse Cases

- Calling learned weights "opaque" as if opacity were the form. Under the path on which a system runs them as a model the form is distributed-parametric; under the runtime that executes them they are symbolic and opaque by scale. In both cases opacity is a modifier on symbolic form or a practical inspection property, not the form, with [scale](../../theory/opacity-depends-on-the-inspection-question-and-budget.md) as one of its sources.
- Calling natural-language content "prose". The boundary is interpretive, not editorial: fragments, facts, structured records, and rules are natural-language when they get their consequences through interpretation, though none of them is continuous prose.
- Counting a fixed prompt and model as symbolic because its behavior repeats. Repeatability is not adoption: a prompt becomes symbolic under a consumption path only when a system adopts the model package, decoding included, as the reference for that operation. Under any other consumption path the same prompt is natural-language, and no adoption makes the package a reference for English.
- Denying that a prompt under a pinned, adopted model is symbolic because the model cannot be read. It is symbolic and opaque under that consumption path; it loses the advantages that reading gives for that reason and keeps what membership gives.
- Treating an undesirable output of an adopted package as a gap in the reference. The package specifies the output, and execution conformed to it; whether that output satisfies the requirement is the adequacy question, which adoption leaves separate.
- Taking a formalization of a consumer for the semantics of the language it consumes. Any implemented consumer together with a machine model has a formal account of its own behavior; that account is the semantics of a language only when the language's users hold consumers to it.
- Calling every YAML or Markdown artifact symbolic. It is symbolic only where a consumer holds specific fields, values, or structures to a reference.

---

Relevant Notes:

- [operative part](../../theory/definitions/operative-part.md) — defined-in: the unit for splitting mixed artifacts, not necessarily the whole stored object
- [constraining](../../theory/definitions/constraining.md) — defined-in: form decides what a commitment leaves open
- [codification](./codification-definition.md) — defined-in: the move from natural-language into symbolic form, by rewriting or by adoption
- [storage substrate](../../theory/definitions/storage-substrate.md) — contrasts: where content is stored, separate from how it is encoded
- [behavioral authority](../../theory/definitions/behavioral-authority.md) — contrasts: which consumer applies content, through which channel, and with what force
- [opacity is a scale threshold](../../theory/opacity-depends-on-the-inspection-question-and-budget.md) — contrasts: scale is one source of the opaque modifier, not the only one
- [addressable theory](../../theory/definitions/addressable-theory.md) — extends: the localized side supplies parts for inspection and separate revision; the assigned-consequences question fixes whether a contradiction is computed or interpreted
- [codification and relaxing navigate the bitter-lesson boundary](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: when to relax a symbolic commitment

---

## Decisions and promotion

The [decision register](./decisions-and-open-questions.md) records the approved conceptual and presentation choices. The definition keeps the membership boundary and a short opacity treatment; the account retains the fuller explanations. [Review checks](./decisions-and-open-questions.md#review-checks-not-wording-decisions) and [promotion tasks](./follow-up-library-changes.md#promotion-checklist) remain separate from those decisions.
