# Candidate definitions for codification and symbolic form

Workshop draft, revised 2026-11-01. The current candidate replaces the formal-semantics candidates of 2026-10-31, which are retained in a footnote[^rejected]. The [reductions note](./implementation-and-shared-semantics.md) remains the supporting argument. The library definitions remain authoritative and unchanged.

## What the reductions settle

An implementation together with a sufficiently specified machine model supplies a formal account of its own behavior. This holds for a compiler and for a frozen language model alike. Therefore "a formal semantics exists for this artifact's language" cannot be the property that separates symbolic from natural-language content: every machine-consumed artifact satisfies it.

This exposes a defect in the current [codification](../../theory/definitions/codification.md) text. It says the reference rules are conjectured to admit a formal semantics and that consumer agreement is evidence for that conjecture. Agreement corroborates conformance to a reference, not formalizability, and formalizability is trivial. The same sentences appear in the assigned-consequences axis of [representational form](../../theory/definitions/representational-form.md).

The current candidate therefore stops grounding the distinction in formal semantics at all. The earlier candidates tried to repair the grounding with an adequacy condition on the reference interpreter; the footnote records why that fails.

## The current candidate: a constitutive criterion

The criterion is constitutive, not formal:

> An artifact is **symbolic** when a designated reference settles what it permits. The artifact's language means what that reference says it means, so a consumer that departs from the reference is wrong. An artifact is **natural-language** when no designated consumer constitutes its meaning. Its language exists independently of any interpreter, so two consumers can read it differently without either being wrong.

The designated reference is an implementation, a specification, or a specification plus implementation parameters. For CPython and a script, the implementation constitutes the language. For a schema and a validator, the validator constitutes what the fields permit. For a route table and a resolver, the resolver constitutes the table's format. In each case the question "what does this artifact permit" has an adjudicator.

English has no adjudicator. A model reading a prompt does not constitute what the prompt means. A second model reading it differently is not thereby wrong. This is the same point the current definitions make with "consumers held to one reference" and with the misuse case about repeatability. The candidate states it directly and drops the formal-semantics decoration around it.

Three consequences:

1. **Tests change role.** Independent implementations and conformance tests corroborate that a consumer conforms to the reference. They say nothing about formalizability, and never did. Agreement remains insufficient: consumers can share a bug and a suite can miss it.
2. **The clerk test stays.** A rule is a candidate for codification when a consumer forbidden insight could follow it ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)). The test concerns the rules the artifact states, not the consumer's machinery, so the observation that a model's computation is also mechanical does not touch it.
3. **The proxy-versus-requirement split stays.** A designated reference fixes what the artifact permits. Whether that is the right operation for the task remains open ([fixed artifacts split into exact specs and proxy theories](../../theory/exact-implementation-does-not-validate-a-requirement.md)).

## Proposed library wording

### Codification: opening

> Codification commits a rule or operation stated in natural language to a symbolic artifact, such as code or a schema, whose permitted behavior is settled by a designated reference. Fixed rules, implemented by a runtime, parser, validator, type checker, query engine, or resolver, determine what behavior is permitted, including any variation they explicitly allow. The consumer changes from a model or human who reinterprets the text on each use to one bound by those rules, so what the artifact permits no longer depends on who reads it.

### Codification: criterion and testing

> The criterion is constitutive, not formal. A symbolic artifact's language means what its designated reference says it means. The reference fixes the language version and any implementation or execution parameters needed to settle what is permitted. When two consumers held to that reference disagree about what the rules permit, one of them is wrong. Departures are failures to implement the committed rules, not alternative admissible interpretations. Natural language has no such reference: its meaning is independent of any consumer, so two readings can both be reasonable.
>
> Whether a formal semantics exists for the artifact's language is not the criterion. Any implemented consumer together with a machine model supplies a formal account of its own behavior, and this holds for a frozen language model as much as for a compiler. That account describes the consumer. It does not make the consumer constitutive of the artifact's meaning.

The clerk-test paragraph is kept as written. The testing paragraph is kept with one change: "corroborate the conjecture" becomes "corroborate conformance to the reference", and the sentence "Testing does not prove uniqueness or guarantee convergence on it" becomes "Testing does not prove conformance outside the tested cases."

The terminology section drops the explanation of the special phrase and keeps the ordinary-English contrast. The Plotkin and operationalism contrasts move to a one-line see-also, since the term they collide with is no longer used.

### Representational form: symbolic form

> **Symbolic** content sits in localized units whose permitted behavior is settled by a designated reference: fixed rules, implemented by a parser, interpreter, runtime, schema, validator, route table, or similar consumer, determine what behavior is permitted, including any variation they explicitly allow. The category is architectural, not a claim about classical symbolic AI.

### Representational form: assigned-consequences axis

> **Assigned consequences** — does a designated reference settle what the artifact permits, or is it reinterpreted on each consumption? A written formal semantics is neither necessary nor sufficient. Most programming languages have none and still sit on this side, because an implementation is designated as their reference. A frozen model's computation can be formally described without the model becoming the reference for the English it reads. Two consumers held to one reference disagreeing about what the rules permit means one of them is wrong ([codification](../../theory/definitions/codification.md) states the test). Natural language has no such adjudicator — two readings can both be reasonable — which is [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), not a defect of any particular text.

The repeatability misuse case is kept, with "Repeatability is not a unique operational semantics" becoming "Repeatability does not make the model a designated reference".

### Constraining

Two phrases change: "where the artifact has a unique operational semantics" becomes "where a designated reference settles what the artifact permits", in the misuse case and the footer label.

### Vocabulary collision ledger

The `operational` row loses its codification sense, since the fixed phrase is retired. The row keeps the lineage sense, the external senses, and the workshop-local sense. Its guidance changes from "write the fixed phrase whole" to "say that a designated reference settles what the artifact permits".

Other library uses of the fixed phrase are migrated to the same wording. The two source ingests that gloss the phrase keep it as a historical reference to the retired term.

## Boundary cases

| Artifact | Designated reference | Form | Note |
|---|---|---|---|
| Python script | CPython at a version | symbolic | the implementation constitutes the language |
| schema enum | the validator | symbolic | the validator constitutes what the field permits |
| route table | the resolver | symbolic | only the operative part the resolver reads |
| YAML frontmatter on a skill | the loader, for declared fields | mixed | declared fields symbolic, instructions natural-language |
| prose instruction run by a model | none | natural-language | the model reads English; it does not constitute it |
| exact numerical claim in prose | none | natural-language | needs symbolic form only when acceptance must be mechanical |
| frozen prompt–model package used as a reference for one operation | the package, for the operation | split | the packaged operation is symbolic; the prompt text stays natural-language, because another model reading it differently is not wrong |

The last row is the boundary the reductions note left open. The constitutive criterion resolves it by splitting on consumption path, which [representational form](../../theory/definitions/representational-form.md) already allows for mixed artifacts. Whether such a package would be a *good* reference for the English in its prompt is a different question; see below.

## Relegated questions

**Adequacy of an interpreter as a reference for English.** Whether a sufficiently competent model could reasonably be designated as a reference for a scoped variety of English is a research question about language fidelity, not a classification criterion. It is graded, currently unassessable, and would make every classification depend on an evaluation nobody can run. The [standalone question for other agents](./perfect-english-reference-question.md) retains it, and the [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the interpreter device.

**Semantic expansion.** "Return an integer greater than 10" permits several answers without disagreement about which integers qualify. A different case arises when interpreters disagree about what is permitted and the semantics is revised to settle it, then meets a further disagreement, indefinitely. That no stage is final does not establish that no fixed account of the sequence exists. No impossibility result about natural-language semantics is assumed by the current candidate, and none is needed: the candidate does not claim that English lacks a formal semantics, only that English lacks a designated reference.

## Review before adoption

1. Does "designated reference" need a definition of its own, or does the gloss in the criterion paragraph suffice? The main risk is a reader taking any machine consumer to be a designated reference, which would collapse the distinction again.
2. Does the boundary table survive a reviewer adding cases? Candidates: a regular expression, a Markdown table consumed only by readers, a test suite, a prompt whose output is parsed by a schema.
3. Is dropping the Plotkin and operationalism contrasts safe once the colliding phrase is gone, or do readers still arrive with the programming-language sense of "semantics"?
4. Does any library note rely on the formalizability conjecture rather than on the constitutive reading? The migration list should check each use of the retired phrase, not only replace it.

Promotion requires coordinated revisions of codification, representational form, constraining, the collision ledger, and the other library uses of the retired phrase. This workshop authorizes none of those edits.

[^rejected]: **Rejected candidates of 2026-10-31.** Four definitions tried to keep formal semantics as the ground. *Fixed formal semantics*: an artifact has one when a designated account determines its permitted behavior, specified mathematically or constructible from an implementation and execution model. *Adequate reference interpreter*: an interpreter is an adequate semantic reference for a language within a scope when it preserves the language's relevant distinctions of meaning; designation alone does not establish adequacy. *Symbolic form*: localized units with fixed rules whose formal account is explicit or constructible from an adequate reference interpreter. *Codification*: commitment to a symbolic artifact whose rules have such an account, where the commitment fixes an interpretation and satisfaction of the original requirement stays separate. They were rejected because the constructibility clause is satisfied by every machine-consumed artifact after the reductions, so all discriminating weight fell on "adequate", which is a graded language-fidelity judgment that nobody can run and that the workshop itself could not settle as a representational distinction. The candidates also smuggled the real discriminator in through an asymmetry: a compiler may "define a new language by stipulation" while a prompt–model package may not. Stated plainly, that asymmetry is the constitutive criterion above. The candidates additionally dropped the clerk test, which survives the reductions. The "fixed formal semantics" candidate would have replaced one KB-special phrase with another needing its own ledger row. The assessment programme that accompanied the adequacy candidate, namely recovering roles and scope, preserving meaning under paraphrase, distinguishing entailment from permission, and separating linguistic competence from knowledge and compliance, is retained in the [standalone question](./perfect-english-reference-question.md).
