# Second review by Astra, 2026-11-01

Review of the workshop after the simplification passes and the Tarski ingests, by the agent Astra, pasted verbatim by the operator. The [framing](./README.md) records the resolution: the operator decided that adopting a frozen prompt–model package as the reference is codification, with addressability a separate graded property.

---

The revision is substantially better, but I still would not promote the definitions. It now separates the established correction from the speculative account of natural language. The remaining problems are more specific: the frozen-model case contradicts the proposed classification rule, and the Tarski thread overstates several results.

I reviewed the current workshop and consulted its Tarski ingests. This is a conceptual review, not a fresh audit against the original papers. No files changed.

1. Blocking: commitment and representation are separated, then recombined

In codification-as-commitment.md:37–39, the draft says:

- adopting a frozen prompt–model package commits the operation;
- the prompt remains natural-language and the weights remain distributed-parametric;
- consequences are assigned whenever an artifact is consumed under such a commitment.

The third statement undermines the first two. The prompt is a localized artifact consumed under the stipulated commitment. Under the proposed assigned-consequences axis, it therefore appears to become symbolic.

Saying "split by consumption path" does not yet resolve this: the disputed case is precisely the prompt's consumption by the designated model.

The clerk test also passes the package at the computational level: a clerk could simulate inference. The table acknowledges this but does not explain which level the classification should use.

Required resolution: decide whether commitment is independent of representational form. If it is, it cannot also define the assigned-consequences axis without an additional criterion. The frozen-package case should be the test that determines the definition, not an exception appended to it.

My preference remains to separate these questions, but that means reconsidering the two-axis derivation of representational form rather than merely replacing its wording.

2. High: the Tarski theorem is stated too broadly

tarski-thread.md:15 says:

> "a consistent exactly specified language that can name its own sentences cannot define its own truth predicate"

Exact specification and names for sentences are not sufficient assumptions. The relevant result needs enough expressive resources for the diagonal/self-reference construction. A weak language does not acquire the full undefinability result merely by containing names.

The same paragraph says:

> "Arithmetic is not semantically closed, which is why it is consistent."

That reverses a necessary restriction into a sufficient explanation. Excluding an unrestricted truth predicate blocks this route to contradiction; it does not establish consistency.

And line 17 says undefinability holds "for programming languages" without specifying a truth-bearing language or theory. Operational evaluation and truth definition must remain separate here.

Required correction: state a scoped result—for example, the undefinability of arithmetic truth within first-order arithmetic—and distinguish it from the conditional liar argument. Do not generalize directly to all programming languages.

3. High: the metalanguage conjecture still crosses from truth to execution

tarski-thread.md:23 proposes:

> "a programming language's reference is stated in a metalanguage the language cannot absorb"

This does not follow from Tarski's restrictions on truth definitions. An interpreter can be written in the language it interprets. A programming language can encode semantic rules and implement their application. What it cannot necessarily provide is a total, adequate truth predicate or decision procedure for sufficiently expressive statements.

Those are different restrictions.

Likewise, codification-as-commitment.md:27 makes "the reference is stated outside the artifact's language" part of the main account. Being external in its governing role does not require being expressed in a different language.

I would retain the modest claim:

> An operation is interpreted relative to governing rules; its ability to describe or execute those rules does not remove the need to specify their interpretation.

That is useful, but not a categorical language distinction.

4. High: exact specification is being treated as effective recognition

The "settled" Tarski section says a clerk-followable reference presupposes sentences and assertion conditions that a clerk could recognize (tarski-thread.md:11).

This needs qualification. Precisely defining a set or relation does not imply an algorithm that decides membership. Checking a supplied formal proof is also different from deciding whether a sentence is provable.

The commitment account adds "or an action permitted" to Tarski's assertion conditions. That may be a useful adaptation, but it is the workshop's extension, not something established by the truth paper.

Required correction: separate:

- exact specification;
- effective execution or checking of individual steps;
- deciding all semantic consequences.

The first does not automatically supply the other two.

5. Medium: declared freedom and defects in a reference remain conflated

The draft acknowledges an ambiguous standard as a gap, then says every choice the reference leaves open is a declared gap (codification-as-commitment.md:29–31).

An accidental ambiguity is not declared. And specified freedom is not necessarily a gap at all: "return either A or B" can completely specify the permitted behavior.

C's unspecified, implementation-defined, and undefined behavior should not serve as one undifferentiated example.

I would distinguish:

1. Permitted variation: the rules settle the allowed alternatives.
2. Required external selection: an input or implementation parameter supplies a choice.
3. An unresolved defect in the reference: the rules fail to settle what they were supposed to settle.

This also preserves step 1's careful distinction between different permitted outputs and disagreement about what is permitted.

6. Medium: the candidate wording does not consistently implement the new account

In candidate-definitions.md:

- The constraining and collision-ledger replacements retain only "a designated reference settles," dropping the second conjunct that excludes human arbitration.
- The sentence about natural language having no designated reference reintroduces the side theory into the proposed definitions, despite the README's stated separation.
- "No consumer can settle the dispute by rule" is too absolute. A specific ambiguity may be resolved by an applicable convention or explicit instruction.
- Keeping the old clerk paragraph unchanged needs reconsideration: its "where such a semantics can exist" framing belongs to the justification being removed.

Also, the boundary table again infers designation from use: "a project that runs CPython" is treated as having adopted CPython's behavior as normative. Running an implementation does not establish that commitment.

What now works well

The revision has made real progress:

- Step 1 remains strong and independent.
- The natural-language theory is explicitly tentative rather than the foundation of the definitions.
- Clarification is no longer categorically excluded from codified execution.
- The source work records limits and counterevidence rather than merely collecting support.
- The perfect-English probe remains open-ended.

The narrower clarification claim is defensible as an execution-contract claim: execution follows declared transitions, while changes to the governing rules occur through a separately authorized process. I would not use the availability of an undeclared clarification channel as a standalone test of representational form.

Recommended next move

Resolve the frozen-package classification before doing more philosophical expansion. It exposes the central unresolved choice:

> Does adopting mechanically executable behavior as authoritative itself count as codification, or must codification also change how the operative content is represented?

The current draft answers both ways. Once that choice is explicit, the definitions can become coherent. Tarski can then qualify the account, rather than being asked to supply a distinction his truth results do not establish.

Minor cleanup: sources.md lists Clark and Brennan twice, once "in progress" and once "deferred."

Bottom line: the workshop has moved from an overbroad theory to a promising architectural account. Its main obstacle is now an internal classification conflict, not a lack of sources.
