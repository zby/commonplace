# Astra's answer to the probe, 2026-11-01

Answer to the [probe question](./perfect-english-reference-question.md) by the agent Astra, recorded verbatim. Part of the [workshop](./README.md). The question was sent through the Codex CLI, version 0.164.0, model gpt-6-astra, reasoning effort high, read-only sandbox, from an empty directory containing only the question file, so the answer draws on nothing else in the workshop. Codex session 01a19887-df49-7d73-8d3f-618e06886ec4. No files changed.

---

**Yes, conditionally: an LLM could serve as a reference interpreter for a specified variety and scope of English. But perfect conversational performance alone would not establish that role, and formalizing its computation would not establish semantic adequacy.** The substantive conjecture is that a particular computational interpreter preserves the distinctions independently warranted by the linguistic practice it models.

Your compiler analogy survives. The main difficulties concern what the reference interpreter must expose, what independently constrains its interpretation, and which demands exceed linguistic competence.

A defensible definition starts with a target specification \(T\) that fixes:

- The linguistic community or varieties, and a historical stage or rule for incorporating change.
- The discourse included: assertions, instructions, questions, quotation, irony, fiction, and so forth.
- The contextual information supplied, including perceptual information and conversational history where relevant.
- The semantic distinctions the account promises to preserve.
- The input and resource assumptions, distinguishing an ideal algorithm from a particular bounded deployment.

The fourth item matters especially. Preserving truth conditions alone may be insufficient for questions, permissions, presuppositions, or reports of belief. Equivalence for one purpose need not be equivalence for every linguistic purpose.

For an utterance and available context \(x\), let \(\Sigma_T(x)\) describe its warranted interpretation: commitments, permitted readings, unresolved contextual parameters, and distinctions among kinds of indeterminacy. This need not select one reading or resolve every parameter.

Then a suitable definition is:

> An interpreter has perfect semantic command relative to \(T\) if, for every admissible input, its interpretation preserves exactly the distinctions and commitments warranted by the target practice, including warranted alternatives and unresolvedness, without introducing unsupported commitments or omitting supported ones.

“Exactly” concerns semantic content, not a unique output notation. Different representations can satisfy the definition. An underspecified representation can also satisfy it if it expresses precisely what remains open.

This is an **objective but relational ideal**: perfection relative to a linguistic practice, context-access specification, and semantic task. It is not perfection relative to a benchmark or panel. It does not require knowing whether every understood assertion is true, deciding every consequence, or executing every understood instruction.

It is also deliberately not a complete theory of English. The definition identifies what adequacy would consist in; it does not supply \(\Sigma_T\). That remaining work is substantive rather than a defect that a clever definition can remove.

The definition is defensible provided linguistic practice supplies sufficiently determinate constraints. It does not assume that every case has a uniquely correct interpretation. Where the practice genuinely leaves something unsettled, accurately preserving that unsettledness is success. But uncertainty among investigators about the practice must not automatically be represented as uncertainty *within* the language.

Unrestricted perfection needs further qualifications. An interpreter cannot recover a hidden intention when two situations present identical accessible evidence but involve different intentions. It can represent the alternatives or request information. Likewise, it cannot predict arbitrary future lexical conventions before receiving evidence of them. A fixed context window cannot preserve arbitrarily much distinguishing information from an unbounded conversation without additional storage. These are informational and architectural limits, not proofs that English lacks formal semantics.

The strongest impossible requirements arise when “command” includes complete, terminating semantic decision procedures. If a language fragment can express arbitrary first-order formulas and the interface must always decide their logical validity, it would solve an undecidable problem. Turing’s §11 establishes the relevant decision-theoretic obstruction. Applying it here requires the effective translation from formulas into the fragment and a universally correct, terminating judgment interface; it does not follow merely from calling the system an English interpreter. [Turing, *On Computable Numbers*, §11](https://www.verostko.com/turing/1936-paper.html)

Thus **representing a meaning and deciding every property of that meaning must remain separate requirements**.

The next issue is what the model would expose. A useful semantic interface could accept an utterance, structured context, discourse state, and declared interpretation policy, and return something like:

```text
Interpretation:
    semantic content or constraints
    alternative readings and their conditions
    unresolved references or contextual parameters
    assertion / question / instruction / permission force
    presuppositions and defeasible contextual inferences
    proposed discourse update
    interpretation status and relevant limitations
```

These need not all be distinct fields in every implementation. Their distinctions must nevertheless be recoverable and testable. Assertions, implications, defaults, and permissions should not collapse into one undifferentiated collection of statements.

For instructions, a central output is an **acceptance condition**, possibly over complete execution traces rather than final answers alone. Your example can be represented as

\[
A(n)\iff n\in\mathbb Z\land n>10.
\]

Returning 11 and returning 12 are different successful executions of this condition. Returning a condition that accepts every positive integer is a different interpretation, even if the interpreter happens to output 11.

This demonstrates why perfect generation of appropriate replies is insufficient under an ordinary reading of “appropriate.” A system that always returns 11 for that instruction reveals neither the full permitted range nor its boundary. Successful behavior can underdetermine the acceptance condition.

More generally, many interpretations can support the same conversational response. “Okay” might be appropriate without exposing any interpretation at all. If “perfect generation” instead requires correct responses to every sufficiently discriminating semantic query, then it already includes the additional semantic interface capability. Recoverability follows only with assumptions about which queries are available, what counts as a correct answer, and whether the system answers completely.

Returning English paraphrases can provide valuable evidence, but their interpretation remains another task. Returning formal expressions makes their structure and consequences mechanically inspectable, provided the output language has independently specified semantics. It does not automatically establish that the English was translated correctly.

There is no requirement to ground every symbol without using any prior understanding. For a bounded domain, objects can have stable identifiers, predicates can denote explicitly supplied relations, and actions can denote defined state transitions. We can then assess whether an English expression was mapped to the appropriate structure. For ordinary discourse, names, perceptual references, and socially established categories require additional grounding commitments. **Formal semantics makes those commitments explicit; it does not create interpretation from uninterpreted marks alone.**

An equivalence or entailment oracle would also be insufficient by itself for some purposes. It could characterize relationships among expressions without identifying their worldly referents. Moreover, equivalence based only on truth conditions can discard distinctions relevant to belief reports or other intensional contexts.

Your ambiguity exception is a promising interface contract, with two important qualifications: it belongs to an interpreter-plus-controller system, and its trigger must be more precise than “there is more than one possible reading.”

Suppose the live readings are \(r_1,\ldots,r_k\), each with acceptance condition \(A_i\).

- Multiple actions satisfying one \(A_i\) constitute permitted freedom.
- Uncertainty about which \(A_i\) governs the task constitutes unresolved interpretation.
- A policy authorizing selection among the readings can resolve the operational choice.
- Depending on the contract, an action satisfying every live reading can sometimes proceed without resolving the ambiguity.

The last possibility deserves inclusion. An execution task may be completed without settling every interpretive distinction. An interface asked to *report the meaning*, however, must still preserve those distinctions.

Absent authorization, executing an action merely because it satisfies **some** live reading generally treats ambiguity as permission. Conversely, demanding clarification whenever an acceptance condition permits several actions mistakes ordinary freedom for missing meaning.

A defensible exception therefore carries more than a question:

```text
Ambiguity:
    unresolved interpretive dimension
    live alternatives or constraints describing them
    why the distinction matters to the requested operation
    commitments already established
    clarification needed, or available authorized policies
```

A clarification handler should narrow the relevant alternatives while preserving unaffected commitments. If “next Friday” is clarified to a date, that should not silently change the meeting’s duration or participants. If the reply also changes the duration, the system should record an amendment rather than treating everything as mere disambiguation. Clarification can also be incomplete or introduce another unresolved issue.

This architecture should distinguish several statuses, which can coexist:

| Status | What remains unsettled |
|---|---|
| Linguistic ambiguity | Which supported interpretation is intended |
| Missing context | A needed referent, parameter, or contextual fact |
| Semantic indeterminacy | The practice itself leaves a boundary or application unsettled |
| Interpreter limitation | The system cannot reliably interpret the input |
| Reasoning limitation | The content is represented, but a requested consequence is unresolved |
| Execution failure | The understood operation cannot be completed |

For example, identifying the grammatical role of “she” can be straightforward while its referent remains unavailable. A vague predicate may have a borderline application without two discrete readings for the speaker to select. A coherent instruction can be impossible to execute without being ambiguous.

**Perfectly detecting task-relevant ambiguity can demand more than perfect linguistic interpretation.** If relevance means determining whether two arbitrary acceptance conditions ever differ, that requires deciding their inequivalence. For sufficiently expressive conditions, no terminating algorithm can always do that. The formal decision limit above applies through this additional reduction.

The consequence is not to abandon exceptions. It is to scope the relevance test, permit conservative reasoning, or expose inability to establish whether a distinction matters. The strongest contract—always ask exactly when necessary, never otherwise, for arbitrary English instructions—requires more than the linguistic ideal alone guarantees.

Missed ambiguities and unnecessary requests are therefore separate failures. Always asking avoids some guesses but fails progress and precision requirements. Never asking fails to preserve unresolved choices. Neither strategy satisfies the proposed contract.

The question of independent correctness remains substantial. My preferred account is that interpretations are constrained by historically situated conventions, patterns of use and correction, referential circumstances, and contextually available communicative intentions. These are social facts, but they are not identical to the verdict of a particular panel or designated model.

On that account, competent speakers provide fallible evidence about a practice they also participate in maintaining. Their disagreement can indicate dialect differences, ambiguity, changing conventions, missing context, or individual error. Identifying which explanation applies requires evidence; counting votes cannot settle it automatically.

This is a philosophical account of the target, not a formal theorem. It also leaves room for genuine underdetermination between semantic theories. Two theories might preserve every distinction relevant to the declared scope while organizing meanings differently. A reference interpreter need not determine a uniquely privileged internal ontology.

To keep this account nonvacuous:

- It must rule out interpretations in clear cases.
- It must specify which contextual changes warrant interpretive changes.
- It must distinguish established alternatives from speculative ones.
- It must retain unresolved cases explicitly instead of counting every model response as acceptable.
- Its predictions must be assessed on cases not used to construct it.

“Everything might mean anything” is not a successful treatment of ambiguity. It fails the exclusion requirement just as a single unsupported guess fails the inclusion requirement.

The construction, adequacy claim, and evidence can now be separated:

| Claim | What supports it |
|---|---|
| The implementation has a mathematical account of its computation | A sufficiently complete specification of the implementation and environment |
| Its outputs define a model-specific interpretation relation | A specified semantic interface and interpretation of its output notation |
| That relation adequately represents the scoped English practice | A substantive adequacy argument, supported by independent evidence |
| Its clarification policy is correct within stated conditions | A separate argument about detection, relevance, authorization, and state preservation |
| It is universally perfect within its scope | A universal claim that ordinary finite testing alone cannot establish |

The second row is stronger than a token distribution but still does not establish the third. A mathematically precise wrong translation remains wrong.

Finite tests can refute a universal perfection claim through one adequately established counterexample. They can corroborate bounded competence and estimate performance under a specified sampling distribution. Exhaustive testing can establish correctness on a genuinely finite domain with a reliable independent oracle. It does not establish correctness beyond that domain.

For a stochastic interpreter, the contract should also specify whether correctness is required for every permitted random outcome or with probability one. A small error probability is compatible with excellent reliability, but not with an unqualified zero-error interpretation contract.

A useful assessment would use small simulated worlds with explicit entities, relations, action rules, and dialogue histories. The point is to make world knowledge and much of the reasoning independently controllable while leaving the English interpretation problem exposed.

Concrete cases would include:

| Weak criterion | Counterexample or diagnostic |
|---|---|
| Produces a permitted answer | Always returns 11; cannot distinguish “greater than 10” from “greater than 0.” |
| Recognizes familiar words | Treats “The dog chased the cat” and “The cat chased the dog” alike. |
| Treats paraphrase as loose similarity | Equates “Not every lamp is on” with “Every lamp is off.” |
| Gives one plausible reading | Omits a supported scope reading of “Every student read a book” in a context permitting both. |
| Resolves reference confidently | Assigns “she” in “Mira told Lena that she had won” despite insufficient context. |
| Equates understanding with truth knowledge | Cannot distinguish interpreting “The sealed box contains a red ball” from knowing its contents. |
| Equates understanding with compliance | Correctly represents “Output exactly `BLUE`” but outputs `RED`. |
| Equates caution with competence | Asks which integer to choose after “Return any integer greater than 10.” |

The scope example should not assume that every theoretically conceivable reading is live in every context. Contextual licensing is part of what the assessment must establish.

I would use four linked assessment conditions:

1. **Interpretation:** Provide all relevant facts and request structured content, alternatives, and open parameters. Use simple domains so difficult reasoning contributes little.
2. **Reasoning:** Supply the correct formal interpretation directly and ask for consequences. This tests reasoning without requiring the English translation step.
3. **Knowledge:** Hold the sentence fixed while supplying or withholding a relevant fact. Check whether the interpretation stays stable while the factual answer changes appropriately.
4. **Compliance and execution:** Supply the interpreted instruction and test action selection and execution separately.

The separation is diagnostic rather than absolute: some pragmatic interpretation inherently uses knowledge and reasoning. The design should expose those dependencies rather than assume complete modularity.

For clarification, include paired cases with genuine missing choices, explicitly granted discretion, irrelevant ambiguities, insufficient factual information, and impossible execution. After each clarification, check preservation of unrelated commitments. Include novel combinations, changed entity names, meaning-preserving paraphrases, misleading framing, and genuinely relevant context changes.

Report omitted readings, invented readings, incorrect commitments, missed consequential ambiguities, unnecessary clarification requests, and lost commitments separately. Record disputed judgments separately from clear failures. An aggregate accuracy score would conceal the distinctions the proposal is trying to protect.

Finally, endless revision does not establish that no fixed formal account is possible. Three situations differ:

- A fixed rule handles indefinitely many new cases.
- A fixed update procedure changes the interpretation system as new linguistic evidence arrives.
- No effective procedure can track the relevant development under the stipulated access and resource conditions.

The first two are compatible with a fixed computational specification. For example,

\[
S_{t+1}=U(S_t,e_t)
\]

describes a fixed update rule operating on changing linguistic evidence. It need not predict the evidence in advance. Whether a suitable \(U\) exists for unrestricted language development is a substantive question; the mere occurrence of continuing revisions does not answer it.

Conversely, writing down an arbitrary sequence of correct future interpretations as a mathematical object does not show that an executable model can compute it. Formal describability, effective computability, predictive access, and semantic adequacy remain distinct.

For the C comparison, **there is no established categorical divide in formalizability**. Both a compiler and an LLM can receive formal behavioral descriptions. Both can define an implementation-specific dialect by stipulation. Both require a separate adequacy claim when evaluated against an independently intended language.

The differences extend beyond the present quality of interpreters, however. C has a deliberately restricted semantic target and an institutional specification of conformance. Its specification also explicitly permits some implementation choices and leaves some behavior undefined; disagreement between compilers therefore need not indicate a bug. These distinctions appear in the C11 committee draft, §§3.4.1–3.4.4. [WG14 N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)

English interpretation ordinarily draws on a wider, evolving social practice and richer context, without one comparable authority deciding all disputed cases. A more capable model would not by itself remove that difference in how correctness is established.

Your conjecture is therefore defensible as an empirical and engineering possibility: **a sufficiently adequate interpreter, equipped with an explicit semantic interface, could become a warranted reference implementation for scoped English.** Its authority would rest on demonstrated fidelity to that scope. Its formalization would then provide an implementation-based semantic account whose adequacy remains open to criticism—much as selecting a compiler can define a dialect without proving that it perfectly implements independently intended C.