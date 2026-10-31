# Candidate definitions using formal semantics

Workshop draft, 2026-10-31. These candidates develop the [reductions note](./implementation-and-shared-semantics.md) and the subsequent operator discussion. They are for review; the current library definitions remain authoritative and unchanged.

## The proposed distinction

An implementation together with a sufficiently specified execution machine supplies a construction of a formal account of its behavior. This applies to compilers and LLMs alike. The construction includes implementation bugs and can represent explicitly modeled variation. Its cost does not prevent its availability in principle.

We can designate that account as defining an operation. Alternatively, we can assess it as an attempted interpretation of meaning specified independently. The same account can play the first role for an implemented operation and the second for the requirement that operation is supposed to satisfy.

Designation alone is insufficient for the distinction we need. Any frozen LLM could define an interface, but this would not make it an adequate reference for English. A reasonable reference must also preserve the linguistic distinctions relevant to the stated language and scope. The proposed property is its actual adequacy, not our belief in that adequacy; evidence for the property remains fallible.

The working hypothesis is that a computational interpreter can serve as a semantic reference when its command of the language is adequate within the stated scope. Better command could make reference-by-implementation reasonable for broader English uses. This is a hypothesis to test, not a claim that C implementations are uniformly correct or that English is inherently unformalizable.

## Candidate 1: Fixed formal semantics

> An artifact has a fixed formal semantics within a specified system when a designated account determines what behavior it permits, including explicitly allowed variation. Conforming interpreters must preserve that account. It can be specified mathematically or determined by a designated implementation and execution model.

The account need not have been separately written down as mathematical rules. An implementation and machine model can supply its construction. Equivalent mathematical presentations count as the same semantics; “fixed” does not require a single permitted output.

The scope fixes the language version, relevant execution conditions, and observations being compared. The designation establishes which rules define the operation. Whether a particular executor conforms to them is a separate question. Independent implementations agreeing under tests that could reveal violations corroborate conformance; passing tests does not prove it.

“Shared semantics” describes what conforming interpreters preserve. It need not be introduced as another registered term. A fixed account remains fixed even when an implementation fails to preserve it or nobody has yet established conformance.

## Candidate 2: Adequate reference interpreter

> A computational interpreter is an adequate semantic reference for a language within a stated scope when it preserves the language's relevant distinctions of meaning, permitted variation, and contextual interpretation. Its designation as a reference does not establish this adequacy. Its implementation and execution model provide a construction of the semantics it realizes.

Adequacy includes distinguishing legitimate readings from misunderstandings, preserving consequences under meaning-preserving reformulations, and changing interpretation when relevant context changes. Merely producing plausible responses or agreeing with a majority is insufficient.

A perfect reference would preserve all relevant distinctions throughout its scope. A practically acceptable reference may have documented limitations within an explicitly bounded use. The decision to accept those limitations is separate from the claim of perfect command. Tests corroborate competence; they do not convert approximate competence into perfection.

This candidate introduces a substantive correctness condition whose assessment is still open. Independent speaker judgments, controlled examples, and adversarial tests are possible evidence, not definitions of correctness. Linguistic competence must also be distinguished from factual knowledge, general reasoning ability, and willingness to follow instructions.

## Candidate 3: Symbolic representational form

Proposed replacement for the symbolic part of [representational form](../../theory/definitions/representational-form.md):

> Symbolic content is retained in identifiable units with fixed rules for permitted behavior. A formal account of those rules is either supplied explicitly or constructible from an adequate reference interpreter and its execution model. Where the interpreter is proposed as a reference for an independently understood language, it must preserve that language's relevant semantic distinctions within the stated scope; designation alone does not suffice.

The criterion concerns actual rules and fidelity to them, not our confidence in a semantic theory. Our knowledge of the rules, the construction, or the interpreter's fidelity can be incomplete. A reference can instead define a new language by stipulation, but its resulting semantics must not silently be presented as an adequate account of an existing language.

This candidate makes the classification depend on the specified language, scope, and operative part. It does not establish an intrinsic division between all C text and all English text. Whether this is the right refinement of representational form remains a review question.

Code, schemas, grammars, and resolver-consumed tables are typical cases when their interpretation mechanisms define the relevant operations. Markdown, YAML, and JSON formatting alone does not establish that role. The criterion concerns the operative part and its consumption path, not the notation or the whole file indiscriminately.

## Candidate 4: Codification

Proposed replacement for the opening of [codification](../../theory/definitions/codification.md):

> Codification commits a rule or operation stated in natural language to a symbolic artifact with fixed rules for permitted behavior. The rules have an explicit formal account or one constructible from an adequate reference interpreter and execution model. The commitment fixes an interpretation for the operation; whether that interpretation satisfies the original requirement remains a separate question.

Codification remains the symbolic region of [constraining](../../theory/definitions/constraining.md): committing choices that narrow or rank permitted readings or behaviors. No revision of constraining as a whole is proposed here. Making prose more precise, extracting a skill from methodology, or adding frontmatter does not alone establish fixed formal semantics for its instructions.

Keep these limits:

- Codification can permit many results. It need not make execution deterministic.
- Defining an operation does not establish that it is the right operation for the task.
- Formalizing actual implementation behavior does not prove conformance to an independent specification.
- A codified check does not establish that it captures its intended requirement.

## The two-compilers test

Two C compilers can pass the same tests and disagree elsewhere. Each compiler, together with the relevant machine models, still supplies a formal account of its behavior. Their incompatibility does not defeat either construction.

There are two different questions:

1. **Choose one compiler to define the dialect.** Its implemented behavior fixes that dialect's interpretation. Another compiler is assessed against it. The choice does not prove that the selected dialect is useful or faithful to an independent C standard.
2. **Treat both compilers as implementations of independently specified C.** Their behavior is assessed against that specification. A disagreement outside permitted variation may expose an implementation bug or an unsettled part of the specification.

Selecting a reference answers which operation is defined. It does not answer whether that operation adequately captures a meaning or requirement that was specified independently.

This is why conformance tests are not evidence needed to establish bare formalizability. One specified implementation already provides a construction. Tests instead put claims of conformance or shared behavior at risk.

## Apply the same test to an LLM

Fix an LLM's weights, inference code, runtime, decoding procedure, and relevant execution conditions. Include context as an input and model sampling explicitly if it is part of the operation. Its response behavior then has a formal account under that machinery.

We can stipulate that this account defines an English-language interface: inputs mean what this designated system makes them mean. The stipulation supplies a formal interpretation. Whether calling it a semantics of English is reasonable depends on what the definition is for.

- **Defining an interface:** the stipulation establishes the implemented operation.
- **Describing ordinary English:** the claim that this operation captures English meaning remains independently assessable. A model can misunderstand; declaring its behavior definitive for the interface does not establish adequacy to ordinary English.

A frozen prompt–model package can define a computational operation by stipulation. That alone does not qualify it as an adequate semantic reference for the English in its prompt. For that stronger role, it must preserve independently assessable distinctions of English meaning in the stated scope.

Better linguistic competence could make such a reference reasonable. The conjecture is not that English becomes formalizable only when models improve: the computation is already formalizable. What improves is the fidelity of the resulting account to English. A compiler chosen as a reference faces the same adequacy question if the claim is that it captures independently specified C, rather than merely defines its own dialect.

The prompt can still express a requirement whose satisfaction is distinct from faithful interpretation. A model can understand an instruction and fail to execute it. Linguistic misunderstanding, execution failure, and a bad requirement must not be counted as the same defect.

## Assessing command of a language

Candidate evidence should test the interpreter's judgments of meaning, not just the appeal of its generated responses:

- Recover roles, reference, negation, and quantifier scope in controlled examples.
- Preserve meaning under paraphrase and detect small changes that alter commitments.
- Distinguish entailment, contradiction, permission, and what remains unsettled.
- Respond to relevant context while resisting irrelevant wording and leading questions.
- Identify legitimate ambiguity and use clarification to eliminate the appropriate readings.
- Generalize to independently constructed cases outside familiar examples.

For instructions, judge candidate actions as satisfying the instruction, violating it, or depending on an unresolved legitimate reading. This separates disagreement about meaning from different permitted outputs.

Use independent competent-speaker judgments as fallible evidence. Retain clear agreement, accepted alternative readings, and unresolved disputes separately. Majority voting must not erase dialect differences or genuine ambiguity. Supply relevant facts where possible to distinguish linguistic misunderstanding from ignorance or failed reasoning.

Report separate error patterns, consistency across related cases, and recognition of uncertainty. A high average score can conceal systematic failures that make an interpreter unsuitable as a reference. Tests cannot establish perfect command over an unrestricted domain; they can reveal counterexamples and support bounded use. The standalone [question for other agents](./perfect-english-reference-question.md) asks how to define the stronger ideal and assess its coherence.

## What the reductions establish

1. **Explicit specification is optional.** A formal account can be constructed from specified computational machinery even when nobody has written a separate mathematical semantics.
2. **Belief is not the criterion.** Our judgment that an artifact satisfies the candidate definition can be mistaken without making the property belief-dependent.
3. **Bare procedure existence is insufficient.** For any finitely expressible semantics, a program can simply print it. That does not explain how it was obtained or why it should define the artifact.
4. **Implementation construction applies on both sides.** It works for a designated compiler and a designated LLM. Complexity and computational formalizability therefore do not by themselves separate code from natural-language meaning.
5. **Bugs do not defeat formal description.** They can defeat conformance to independently specified rules.
6. **Agreement is corroboration, not proof.** Different implementations can agree on tests while differing elsewhere.
7. **Variation is compatible with formal semantics.** Different permitted answers need not indicate different interpretations.
8. **Adequacy remains assessable.** Stipulating a semantics establishes an interpretation; it does not establish that the interpretation captures an independently intended meaning.

An executable and its machine model suffice for the implementation construction. Tracing its compilation history back to lambda calculus is unnecessary for describing its behavior; compilation history matters separately to claims of faithful compilation.

The progress is retained: Commonplace's special sense of “operational semantics” is unnecessary for these distinctions. Fixed formal rules, their implementation, and their adequacy to a requirement can be discussed separately.

## Semantic expansion remains a separate question

“Return an integer greater than 10” permits several answers without leaving interpreters in disagreement about which integers qualify. A different case arises when interpreters disagree about what is permitted. We might revise the semantics to admit both readings, reject one, or require additional words to disambiguate.

The operator's further question concerns an indefinitely continuing sequence:

1. Start with a proposed semantics.
2. Encounter a disagreement it does not settle.
3. Expand or revise the semantics to settle that case.
4. Encounter a further disagreement under the expanded semantics.
5. Repeat without reaching a final account.

This is different from infinitely many cases covered by one fixed rule. It also leaves two claims separate: no stage in the sequence is final; no fixed formal account can describe the sequence itself. The first does not establish the second. A sequence of unsuccessful accounts does not establish that every possible account must fail.

The discussion identified open texture and semantic-paradox literature as relevant. The search has not yet been retained as a source-grounded argument here. No impossibility result about natural-language semantics is assumed by the candidates above.

## Review before adoption

The revised candidates add adequacy of the reference interpreter to the construction of its semantics. Review must test this condition rather than treating it as an established classification:

1. Can adequate command of a language be defined without making the chosen interpreter or current speaker agreement correct by definition?
2. Does the criterion distinguish the cases we need, or describe a graded suitability for reference use rather than a binary representational form?
3. Can an LLM with perfect command of a scoped variety of English provide its semantics through a specified interface? What must that interface expose beyond a distribution of plausible replies?
4. Are language fidelity, conformance to adopted rules, successful execution, and adequacy to a task kept separate?
5. Are constructing a semantics, executing a program, and deciding every semantic question kept separate? The first need not decide every consequence of the semantics.
6. Which scope restrictions and residual errors permit practical adoption, and which claims must remain conjectural after testing?

Promotion would require coordinated revisions of codification, representational form, the codification passages in constraining, and the vocabulary collision ledger. This workshop authorizes none of those library edits.
