# Fifth review by Astra, 2026-11-02

Review of the workshop after the fourth review's fixes, by the agent Astra, pasted verbatim by the operator on 2026-11-02. The [framing](./README.md) records the resolution: all three points accepted. The localization question now identifies units by what the consumer on the path takes up, not by what a reference's rules range over, so natural-language content can be localized without a held-to reference.

---

Most of the last review is now resolved. One substantive problem remains in the localization criterion, plus one incorrect sentence in the compiler/model comparison. I checked the current changes against the previous version; I would keep this next pass small.

1. Blocking: localization now requires what distinguishes symbolic from natural-language content

In representational-form-definition.md:33 (kb/work/formal-semantics-and-codification/representational-form-definition.md), localization asks:

> "does the reference on that path assign consequences to identifiable units carrying the content"

And:

> "A unit counts when the reference's rules range over it"

But natural-language content is defined as having no such held-to reference. It therefore cannot pass this localization test—even though the classification requires it to be localized before asking whether its consequences are assigned.

The proposed order is now sensible:

1. Is the content localized?
2. If so, are its consequences assigned?

However, the first question's definition already requires a yes to the second.

The fix is to identify units independently of whether a reference assigns their consequences. For example:

> Under the consumption path, are there separately identifiable content units that can be inspected or revised—such as an instruction, claim, field, expression, or numerical operand?

Then ask separately whether a governing reference fixes their consequences.

The examples should establish:
- a policy clause is identifiable despite requiring interpretation;
- a schema field is identifiable and has assigned consequences;
- a tensor operand is identifiable under the numerical execution path;
- a model's instruction-level commitments are not generally exposed as separately identifiable units under the interpreter path.

That preserves the operator's path-relative localization decision without making localization depend on symbolic membership.

2. High: disagreement with a model does not establish that neither reading is wrong

In representational-form-definition.md:31 (kb/work/formal-semantics-and-codification/representational-form-definition.md):

> "where the model departs from a reader's reading, neither is wrong."

This should be:

> Disagreement alone does not establish which reading is wrong; both may be reasonable, or either may violate the instruction.

For example, a model can read "exclude archived records" as "include archived records." The absence of a designated reference model does not make that reading acceptable.

The main account has a related overstatement:

> "a reader that departs from it is not wrong"

Change that to "is not thereby wrong." This is a small wording change with a substantial logical effect.

The GCC half is now correctly separated from the conformance claim. I would close that previous finding.

3. Minor: finish presenting the classification as ordered questions

The text now says the second question is not asked for non-localized content, but the table still places distributed-parametric content in the "consequences not assigned" row.

A simple table would avoid that residual mismatch:

| Localization under the path | Consequences assigned? | Form |
|---|---|---|
| Yes | Yes | Symbolic |
| Yes | No | Natural-language |
| No, with content distributed across numerical state | Not applicable | Distributed-parametric |

Also replace the remaining "follows from the axes" wording with "follows from these questions." These are presentation fixes, not a request to change the classification again.

Findings I would close

The revision now handles these adequately:

- Different compiler outputs can both conform where variation is permitted.
- A formal description of GCC is not automatically C's semantics.
- Undefined behavior is separated from a defect in the reference.
- Parameter edits can change behavior without identifying a revised semantic commitment.
- Opacity removes an affordable inspection route without guaranteeing that testing will replace it.
- Vector symbolic architectures no longer contradict an allegedly impossible fourth cell.

Bottom line: the codification account is stable enough for this stage. Fix localization so natural-language units can actually pass its test, correct "neither is wrong," and finish the table cleanup. I do not see a reason in this revision to reopen adoption, opacity, or the Tarski investigation.
