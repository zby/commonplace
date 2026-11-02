# Third review by Astra, 2026-11-01

Review of the workshop after step 2 was rewritten around the operator's decisions and the two definitions were written, by the agent Astra, pasted verbatim by the operator on 2026-11-02. The paste ends mid-word; the cut is kept as received. The [framing](./README.md) records the resolution: all five points accepted, with point 1 answered by making the localization axis relative to the consumption path, as form already is, rather than by revising the table.

---

The main decision is now coherent: an adopted frozen model makes its prompt symbolic under that consumption path, while opacity is a separate property. That resolves the previous prompt-classification blocker. I would not reopen that decision.

However, the revision is not yet ready for promotion. The new decision has consequences that the inherited classification table does not accommodate, and the opacity section makes claims stronger than the account supports.

I read the revised account, both complete definitions, the Tarski thread, the probe response, and the follow-up plan. No files changed.

1. Blocking: the two-axis table still conflicts with the adopted-model case

representational-form-definition.md, Derivation (kb/work/formal-semantics-and-codification/representational-form-definition.md) retains:

| | Localized | Non-localized |
|---|---|---|
| Consequences assigned | symbolic | empty |
| Consequences not assigned | natural-language | distributed-parametric |

But the adopted package includes weights whose computational consequences are fixed by the inference implementation and machine model. The system has adopted that behavior as authoritative. Why do those weights remain in "consequences not assigned"?

The account explicitly says that weights remain distributed-parametric under every path. That can be a sensible classification, but it no longer follows from this table without another distinction.

The previous contradiction about the prompt has been resolved; the same question now arises for the weights.

Required change: either revise the table or explain precisely why "assigned consequences" applies to the prompt but not to the numerical state that determines its execution. My preference is to stop requiring these two axes to generate all three categories. Encoding structure and normative commitment need not form a neat partition.

2. High: opacity is defined at the wrong level for two of its three examples

The proposed definition says symbolic content is opaque when:

> "the reference that assigns its consequences cannot be read rule by rule."

That covers the frozen-model example. It does not cover an enormous or obfuscated C program: the language reference can remain perfectly readable while the program is hard to understand.

The account also overstates the contrast:

- Large ordinary programs do not generally preserve locally predictable effects of local edits.
- Distributed-parametric references do not establish that no local prompt edit has a predictable effect.
- Opacity does not mean that all advantages of ordinary code disappear.
- Readable rules do not by themselves establish conformance to intent.

These are claims about degrees of practical understanding, coupling, and verification—not deductions from representational form.

Suggested repair: define opacity relative to understanding a specified behavior or change, using the artifact and its reference, at an acceptable inspection cost. Present scale, distributed implementation, and obfuscation as sources that can obstruct that understanding. Replace categorical "cannot," "entirely," and "no locally predictable effect" claims with scoped claims about what inspection does not reliably provide.

This affects both the account's opacity section (kb/work/formal-semantics-and-codification/symbolic-form-and-codification.md) and the proposed form definition (kb/work/formal-semantics-and-codification/representational-form-definition.md).

3. High: the account again mixes reference conformance with requirement adequacy

The opacity section says the frozen package loses declared gaps because:

> "the package never declares permitted variation or a defect"

Yet the earlier adoption section explicitly allows the output distribution to specify permitted variation. A package can also have explicit error, refusal, or clarification outputs.

More importantly, if the package's behavior constitutes the reference, an undesirable answer is not automatically a gap in that reference. It can be fully specified behavior that fails the original requirement.

For example:

> The adopted package always returns an incorrect summary for this input.

That can be exact execution of the adopted operation and a failure of the summarization requirement. Calling it a newly discovered semantic gap loses the distinction step 1 established.

Required change: keep three questions separate throughout the opacity section:

1. Did execution conform to the adopted package?
2. What behavior does the package specify, including variation and failure outputs?
3. Does that behavior satisfy the intended task?

Opacity primarily makes the third question—and prediction of the second—harder. It does not inherently remove declared behavior or turn inadequacy into an unspecified case.

Also, symbolic membership does not guarantee repeatability or determinism: the account deliberately permits stochastic references.

4. High: the side theory is again doing work the framing says it does not do

The account begins by saying nothing depends on the side theory. Later it says:

> "The side theory explains why this cannot be otherwise."

The opacity section then asserts that no frozen language supports repair, internal redefinition, or discovery of gaps on use. This conflicts with the earlier acceptance of the probe's point that fixed computational rules can support contextual repair and changing state.

The direction-of-authority distinction is sufficient for the bounded conclusion:

> Adopting this package for this operation does not, by that act alone, establish its adequacy as a semantics of English.

It does not require:

> No formalization could describe English without replacing it.

That stronger conclusion remains unsupported. A descriptive semantic account can answer to linguistic practice without being the authority that constitutes it.

Required change: keep the bounded adoption claim and remove the necessity argument. The Tarski thread is substantially improved; this part of the main account should match its restraint.

5. Medium: "no formal semantics can be derived from a human judge" is too strong

This claim appears in both the main account (kb/work/formal-semantics-and-codification/symbolic-form-and-codification.md) and codification definition (kb/work/formal-semantics-and-codification/codification-definition.md).

What follows is narrower:

> Designating a human judge does not supply an effectively specified rule for their judgments.

A human can follow a formal decision procedure. A formal protocol can also treat a human decision as an external input without formalizing the judgment itself. Neither requires solving the general problem of modeling human cognition.

The relevant exclusion is unformalized discretionary judgment, not the human identity of the consumer.

What I would now accept

Several previous problems are genuinely resolved:

- Adoption versus mere pinning is explicit.
- The prompt's changed classification is a deliberate consequence rather than an exception.
- Symbolic form is defined before codification.
- Tarski's undefinability result is scoped more carefully.
- Truth definition is separated from execution.
- The probe's update-rule objection has been recorded and partly incorporated.
- Permitted variation is distinguished from unresolved interpretation.

"Close to a formal semantics" is still awkward terminology for a binary criterion, but that is now secondary. I would fix the conceptual inconsistencies before polishing it.

Bottom line

Keep the adoption decision. Revise the table and narrow the opacity argument.

The strongest version of the account now says:

> Adoption can fix which behavior counts as conforming without making that behavior easy to understand, predict, revise, or justify against the requirement.

That is a useful result. The draft weakens it when it claims that adoption necessarily preserves repeatability, that opacity eliminates declared behavior, or that the difference requires proving English cannot be formally descri
