# Review by Astra, 2026-11-01

Review of the workshop as of commit 60a1e4b64, by the agent Astra, pasted verbatim by the operator. The [framing](./README.md) records what the workshop changed in response.

---

I read all five files, plus the current definitions. I think the workshop has a strong correction, but its replacement account overreaches. I would retain step 1, revise step 2 substantially, and hold off on promoting the candidate definitions.

What is solid

Implementation and shared semantics (kb/work/formal-semantics-and-codification/implementation-and-shared-semantics.md) is the strongest piece. It cleanly separates:

- a formal account of a consumer's computation;
- conformance to rules the consumer is supposed to implement;
- whether those rules satisfy the original requirement.

The compiler/LLM symmetry is important. Supplying a complete computational model does not establish that its behavior correctly interprets an independently intended language. Passing tests does not establish the bare existence of that model either.

That is enough to justify removing the current formalizability argument. This result does not depend on discovering a categorical difference between English and programming languages. I would protect it from becoming hostage to that larger question.

Where the replacement goes wrong

Where meaning is settled (kb/work/formal-semantics-and-codification/where-meaning-is-settled.md) finds a useful architectural distinction—what has this system committed to treating as authoritative?—but turns it into too strong an account of language.

### 1. Authority to settle a dispute is not the same as symbolic representation

A contract can designate an arbitrator whose interpretation is binding. A workflow can designate a human to decide what "sufficient evidence" means. Neither thereby becomes symbolic in the sense Commonplace needs.

Conversely, a programming-language specification can be authoritative while containing ambiguous prose. Designating it does not eliminate the interpretive work.

So there are at least two separate questions:

1. Which reference governs the operation?
2. Does that reference supply rules that settle the relevant choices without fresh judgment about what was intended?

The proposed criterion leans too heavily on the first. The second is closer to the practical distinction the existing definition is trying to capture. It still needs boundary testing; "designated reference" does not resolve it by itself.

The examples also need qualification: CPython does not automatically constitute all Python semantics, and a validator does not automatically constitute a schema's meaning. Either can be an implementation with a bug unless the particular system has deliberately adopted its behavior as the reference.

### 2. Codification does not close the clarification channel

This is the clearest counterexample to the new mechanism.

A program can encounter an unresolved choice, ask the user, and continue under fixed rules. An interactive parser can present two parses and ask which was intended. A protocol can specify an Ambiguous result and a clarification exchange.

What is fixed is how clarification participates in execution—not necessarily the answer to every future question.

That makes these claims too strong:

> "Once a rule is codified, its consumer cannot ask."

> "If the consumer can legitimately ask the author what the artifact means, the artifact is natural-language."

The ambiguity-exception proposal in the standalone question (kb/work/formal-semantics-and-codification/perfect-english-reference-question.md) actually provides a useful way to challenge those claims. A fixed protocol can govern an interaction whose answers require human interpretation. The result is mixed, not a contradiction.

### 3. Speakers are not sovereign adjudicators of English

Authors can clarify their intentions, but that does not make them final authorities over what their earlier words conventionally meant. They can misuse a word, revise a commitment, or discover that they had not decided what they meant.

Nor does natural-language understanding always depend on access to the author. We understand instructions from unavailable authors, and some readings are simply wrong.

The draft therefore slides between:

- what an expression means;
- what its author intended;
- what the parties agree to do next.

Repair can connect these, but it does not make them identical. "Meaning is settled by its author on request" is too simple to carry the proposed definition.

### 4. Several broader claims outrun the argument

I would remove or explicitly suspend these:

- "Codification closes the repair channel." Replace with a narrower account of which choices are committed and which interactions remain permitted.
- Programming-language consumers can know beforehand whether a case is settled. Fixed semantics do not imply decidable analysis. Whether a program encounters undefined behavior can depend on execution.
- Fuzzy logic failed in linguistics because speakers settle meaning locally. This is a substantial historical and causal claim; the workshop explicitly has not grounded it.
- English cannot have a reference because it has no state to capture. Variation and change do not establish this. A model might represent variation, context, and change rather than one static dictionary.
- Underspecification is derived from the repair channel. Repair helps explain why leaving things unstated can work, but missing context and unanticipated cases can arise without any expectation of repair.

What I would preserve from step 2

The useful core is narrower:

> For a specified operation, a system can commit to rules that determine permitted behavior rather than asking a consumer to recover the intended operation afresh from natural language. The commitment may include permitted variation, external inputs, and clarification steps. Its adequacy to the original requirement remains a separate question.

That is a promising account of codification (kb/theory/definitions/codification.md), not yet a complete definition. Its advantage is that it concerns a commitment made in a system, rather than requiring a theory of everything that distinguishes natural and programming languages.

It also makes the frozen-model case easier to discuss honestly: adopting a model package as authoritative commits an operation, but does not automatically change the representational form of its prompt or weights. Commitment and representation may need separate treatment, rather than forcing one criterion to explain both.

My recommendation

1. Keep step 1 as the established result of the workshop.
2. Reframe step 2 as an architectural account, not a categorical theory of language.
3. Test it against an authoritative human adjudicator, an ambiguous prose standard, an interactive parser, and a frozen model package.
4. Keep the perfect-English probe open-ended. Its current wording is more careful than the categorical prediction in step 2; I would not add that prediction as a premise.

My overall judgment: the workshop correctly dismantles a weak justification, but has not yet earned its replacement definition. The most productive next move is to separate what governs correctness, how content is represented, and how unresolved choices are handled. The current draft makes those three do each other's work.

---

## Follow-up comment, prompted by the Tarski thread

Pasted verbatim by the operator, 2026-11-01:

> I would explore this hypothesis:
>
> The practical difference is not formalizability versus non-formalizability. It is whether the operation has been committed to a delimited interpretation regime, or still relies on ordinary linguistic judgment to settle what its instructions require.
