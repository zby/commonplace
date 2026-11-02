# Fourth review by Astra, 2026-11-02

Review of the workshop after the third review's fixes and the example-first restructure of the definitions, by the agent Astra, pasted verbatim by the operator on 2026-11-02. The [framing](./README.md) records the resolution: all five points accepted, with point 1 treated as presentation, since the two questions are unchanged and only their order of application, the table's reading and a side prediction about a fourth form change.

---

The revision resolves most of the previous review, but the new derivation of representational form still has a structural problem. There are also two regressions in the compiler examples that directly contradict step 1.

I checked the current framing, main account, and both proposed definitions, plus the existing addressability definition. No files changed.

What is now resolved

I would close these previous findings:

- Opacity now concerns the artifact and its reference, relative to a behavior or change and an inspection cost. That covers the three intended sources.
- Conformance, specified behavior, and requirement adequacy are explicitly separated. The wrong-summary example works well.
- Declared behavior is no longer said to disappear under opacity.
- The human-judge exclusion is correctly narrowed to unformalized judgment.
- The main account no longer needs an impossibility claim about formal descriptions of English.
- The concrete opening examples improve the definitions' accessibility.

The decision to classify an adopted model's prompt as symbolic remains coherent. The remaining issue is how the rest of the classification is derived.

1. Blocking: the table is now a decision tree presented as two independent axes

In representational-form-definition.md:40 (kb/work/formal-semantics-and-codification/representational-form-definition.md), the draft says:

> "The fourth cell is therefore empty by construction … the row question has no subject in the non-localized column"

This is a defensible way to make a hierarchical classification:

1. Does the path expose identifiable content units?
2. If so, are their consequences fixed by a reference?

But then "assigned consequences" is not applicable, rather than false, for non-localized content. Placing it under "consequences not assigned" hides that difference.

The same paragraph then says vector symbolic architectures could occupy the fourth cell. That contradicts "empty by construction." Moreover, under the revised definition, making distributed state addressable would make it localized under that path, not populate the non-localized column.

Recommended repair: retain the operator's path-relative localization decision, but express the classification as a decision tree. Alternatively, mark the non-localized row question not applicable and remove the fourth-cell prediction. No need to abandon path-relative form to fix this.

2. High: specify what counts as an addressed content unit

The runtime/interpreter distinction is promising, but "the consumer addresses identifiable units" still admits two readings:

- the consumer mechanically accesses storage locations;
- the consumer exposes separately identifiable content or operations at the level being assessed.

These produce different classifications. A transformer accesses token positions and tensor elements. That does not by itself make the instruction's commitments separately addressable. Conversely, a caller can invoke a conventional compiled program without addressing anything inside it.

A useful boundary test would compare:

- an ordinary compiled program behind an API;
- a neural model behind the same API;
- an adopted prompt supplied to that model;
- the numerical tensors consumed by its runtime.

The definition should explain which units count on each path without switching between storage access and content structure.

There is also a concrete overstatement at representational-form-definition.md:44 (kb/work/formal-semantics-and-codification/representational-form-definition.md):

> "editing [a parameter] revises nothing under the interpreter's path"

Editing a parameter can change the interpreter's behavior. What it does not generally provide is a separately identified semantic commitment being revised.

Suggested replacement:

> Editing a parameter can change behavior without identifying which instruction-level commitment the edit revises.

That preserves the distinction the existing addressable-theory definition (kb/theory/definitions/addressable-theory.md) needs.

3. High: the new compiler examples undo step 1's distinctions

Two passages in the proposed form definition need correction.

### Different behavior can still conform

At line 27 (kb/work/formal-semantics-and-codification/representational-form-definition.md):

> "Two C compilers that disagree about what a program does cannot both be right"

They can produce different behavior where the standard permits variation or implementation choices. The later sentence about disagreement over what the rules permit is better, but does not repair the opening example.

Use:

> Where the reference requires one result, two compilers producing different results cannot both conform.

### Modeling GCC does not establish C semantics

At line 31 (kb/work/formal-semantics-and-codification/representational-form-definition.md):

> "The description of GCC is a formalization of C, because C's users hold every compiler to the standard GCC implements."

This is precisely the inference step 1 rejects. Holding GCC to the standard does not establish that GCC conforms; its formal behavioral description includes its bugs and extensions.

Use:

> A formal description of GCC describes that implementation. Whether it realizes the intended C semantics is a separate conformance claim.

The main account's "GCC up to its bugs" formulation also needs care: removing the bugs already requires identifying which behavior the independent reference permits.

4. Medium: declared undefined behavior still sits under "defect"

In symbolic-form-and-codification.md:58 (kb/work/formal-semantics-and-codification/symbolic-form-and-codification.md), undefined behavior appears under "A defect in the reference."

A deliberate absence of requirements is not necessarily a defective specification. The reference can completely specify that it makes no behavioral guarantee for a case.

Keep it separate from accidental ambiguity:

- permitted alternatives;
- externally supplied choices;
- explicitly excluded guarantees;
- defects or unresolved ambiguities in the reference.

This matters because both proposed definitions say that only the "defect" category represents a failure of the reference.

5. Medium: opacity still implies too much about verification

The improved definition ends with:

> "so that it must be found by running cases"

That does not follow from failure of affordable inspection. Running cases may also be inadequate or prohibitively expensive. Some properties can instead be established through abstraction, certificates, or automated analysis without understanding the implementation rule by rule.

The main account also says reading:

> "finds most inadequacies cheaply"

That is an unsupported empirical generalization.

I would narrow these to:

> Opacity removes an affordable inspection route for the question at hand. Evaluation may therefore rely more heavily on execution, other analysis methods, or explicitly retained uncertainty.

This keeps the practical point without making testing a guaranteed substitute for understanding.

Overall judgment

The account is converging. I would not request another broad philosophical rewrite. The next pass should be bounded:

1. Make the classification hierarchical, or explicitly handle the non-applicable axis.
2. Clarify content units versus storage addresses.
3. Restore step 1's compiler distinctions in the concrete examples.
4. Separate intentional absence of guarantees from reference defects.
5. Remove the remaining verification overclaims.

The codification definition is now substantially more stable than the representational-form definition. The main unresolved work is the classification machinery, not adoption, Tarski, or the existence of formal models.
