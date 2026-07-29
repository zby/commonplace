---
description: "Derivation from supported constraints and inheritance of a source-tested ontology give a decomposition conditional or transferred starting warrant; free choice gives only a pragmatic reason to adopt, and only refutation-capable use earns the claim"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, discovery, foundations]
---

# Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it

A decomposition claims more than it displays. Its categories are visible; its implied scope is not. By using those categories, the designer asserts that they will continue to cut the domain at consequential boundaries, including in cases the designer has not seen. That assertion is an [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) claim. Because [use tests a decomposition only locally](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), merely operating a system that contains the decomposition does not test its broader scope.

Two judgments about that claim are easy to conflate. Its provenance determines whether it begins with any scope warrant, what kind of warrant that is, and what remains to be tested. Whether the claim is *earned* is settled the only way [reach-assessment](./definitions/reach-assessment.md) recognizes: by surviving evidence that could have refuted it. Provenance determines the starting scope warrant; refutation-capable use earns the claim.

Three labels describe that provenance. They are not mutually exclusive bins applied once to an entire decomposition. They may differ by axis or boundary: derivation marks what independently supported constraints fix, inheritance marks what is borrowed together with evidence from a source domain, and free choice marks the residue that neither source fixes. One decomposition may therefore be derived and inherited in some respects while remaining free in others.

**Derivation from independently supported constraints** gives conditional warrant. Once the axes are fixed, the cells follow, including the empty ones. This derivation warrants the conditional *if these axes remain operative, these cells remain exhaustive*; it does not establish that the axes track consequential distinctions. Axes selected only because they produce the desired split remain free choices, even if their cells follow mechanically. When independently supported causal or operational constraints fix the axes, that support supplies the conditional's antecedent. The derivation may still be valid even when those constraints cease to matter in the next case: its warrant is conditional, not universal.

**Inheritance of a tested ontology** gives transferred warrant only when the source testing was discriminating. Repeated survival across cases that could have broken the ontology is the extensional route to a scope claim; borrowing the ontology acquires that evidence secondhand. Mere maturity or repeated use does not. Moreover, the evidence still concerns the *source* domain. It licenses the decomposition in a target domain only while the constraints that made its boundaries consequential at the source also hold at the target.

**Free choice** gives no starting warrant for the scope claim. A boundary underdetermined by constraints or evidence may have a pragmatic reason for adoption, such as convenience or preference, but there is no reason to expect it to remain consequential. It should therefore remain cheap to replace.

Direct mechanistic or predictive support is not a fourth provenance. If independent measurement fixes the axes, the decomposition is derived from that constraint. If the decomposition survives a held-out comparison, intervention, or risky prediction, that encounter is already discriminating use, even when it occurs before deployment. A theory-guided proposal that is neither fixed by independently supported constraints nor exposed to refutation-capable evidence remains free wherever it is underdetermined.

## Derivation and inheritance relocate the test; use runs it

A provenance label alone does not earn the target-domain scope claim. Derivation supplies no encounter with evidence that could have broken the decomposition, while inheritance rests on evidence from the source domain rather than the target. Both instead relocate the remaining test to somewhere statable. Derivation moves it to the antecedent: vary or intervene on the named constraints and ask whether the boundaries change as predicted. Inheritance moves it to the bridge: establish that the source testing was discriminating, then check whether the source's operative constraints still hold at the target. Free choice supplies no comparably targeted rationale. A single successful local use still establishes only local sufficiency, whereas an accumulating sample of varied, refutation-capable contexts can test transfer extensionally.

Earning is therefore open to every provenance. A decomposition that began as free choice can earn scope one context that could have broken it at a time. This is the route [an automated theory-search loop](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) must take for each proposal: a discriminating acceptance test contributes earned reach, while a merely confirmatory one manufactures an unearned claim.

[What scale replaces is a generalization whose scope was asserted rather than tested](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md), and a decomposition makes exactly such a generalization when it asserts that its boundaries will continue to matter. Starting warrant merely makes the remaining test statable. A free choice is not necessarily sloppy, but it should stay replaceable. Encoding it in a directory layout, schema field, or widely cited vocabulary term adds revision cost without adding warrant or evidence.

## The two triples relate but do not coincide

Retained rationale classifies each boundary by what it answers: an **inherited constraint**, a **local requirement**, or a **free choice**. Provenance classifies why a boundary or decomposition begins with any scope warrant: derivation, inheritance, or neither. The two classifications overlap but do not map one-to-one.

Derivation can serve either of the first two rationale slots. A boundary may be fixed by an inherited constraint or by a local requirement. For example, [decomposing user stories into their step-by-step context needs](./scenario-decomposition-drives-architecture.md) derives boundaries from one application's local requirements without borrowing them. Its conditional warrant extends only to problems that share those requirements.

Inheritance describes where the rationale and its evidence came from, not which rationale slot each boundary occupies. When borrowing is undocumented or lossy, source-wide constraints and source-local requirements arrive bundled, making every boundary appear equally load-bearing. That hidden cost comes from the missing provenance record, not from inheritance itself. The distinction also explains why a technique can demonstrate transfer by working in the target while an ontology transfers only if it continues to cut at consequential places there. [Closeness of fields](./programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must.md) is evidence for that bridge, not a substitute for it.

## Two recorded instances

[Representational form](./definitions/representational-form.md), which classifies how retained content is encoded and consumed, is derived from the axes of consequence-assignment and localization. Those axes generate three occupied cells, an explicit empty fourth cell, and the read/test/probe rule. The starting warrant is conditional on the axes continuing to matter; whether they identify consequential distinctions remains the test.

A [reflective system](./definitions/reflective-system.md), which represents and acts through aspects of itself, is inherited. Causal connection, self-representation, and theory-relativity come from Maes's 1988 account and Smith's 1984 lineage. The definition separates retrieval-as-causal-connection as Commonplace's own extension. Because the source evidence concerns interpreters and metaobject protocols, applying those criteria when the causal wire is best-effort discovery creates a separate bridge claim.

## Scope

- **The quality of the source testing is the weak joint of inheritance.** Nothing here provides a criterion for judging it, and longevity is a poor proxy. An ontology can survive simply because it was never probed, reproducing the failure of a reach claim that no test could refute. The transferred warrant is only as good as the testing behind it, which a borrower often cannot audit.
- The provenances may combine. Re-deriving a borrowed decomposition from local constraints offers the strongest available position, but also the most expensive. It can be difficult to distinguish from rationalizing the borrowed split after the fact. An unfaithful rationale then inherits the [worse-than-none asymmetry](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md): it directs tests toward the wrong premise.
- The classification of direct support is analytic rather than demonstrated. A case whose axes are neither derived from constraints nor inherited, yet which has genuine starting scope warrant before any refutation-capable encounter, would require another provenance or a weaker title.
- **Commonplace has not demonstrated that this claim transfers.** The two instances were authored inside the system that states the claim and assessed by nobody outside it. They establish only that both warrants can be recorded and that the record makes departures auditable. They do not show that recording warrants produces better decompositions or that the discipline survives contact with a designer committed to a decomposition they already had.

## Open Questions

- What would make "already tested" checkable for a borrower who cannot rerun the source field's cases? Is there any evidence short of finding a case that should have broken the original decomposition but did not?
- Can a re-derivation of a borrowed decomposition be distinguished from a rationalization of it by anything other than intervention on the stated constraint?
- Can "stay replaceable" be operationalized as a forbidden position or a cost ceiling for a free-choice decomposition, or will it remain advice that loses force as soon as another artifact cites the decomposition?
- What makes a sample of contexts *discriminating* rather than merely accumulated? The extensional route earns scope only as fast as its sample could refute, and nothing here determines when varied use crosses that line.

---

Relevant Notes:

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — extends: supplies the local-versus-transfer gap and the intensional and extensional routes that this note grades as warrants, with inheritance added as the secondhand purchase of extensional evidence
- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: supplies the criterion that "earned" answers to — a claim has been tested against evidence that could have refuted it
- [The bitter lesson selects against unearned reach, not against structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — grounds: identifies asserted-versus-tested scope as the property on which scale selects, and supplies the search loop through which free-born decompositions must earn scope extensionally
- [Programming patterns get a fast pass but other borrowed ideas must earn first-principles support](./programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must.md) — contrasts: sets adoption bars for techniques by source field, whereas this note sets the bar for ontologies by whether the constraints behind their decompositions still hold
- [Scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) — contrasts: provides a decomposition derived from problem-local requirements with nothing borrowed, showing why the rationale triple's middle slot does not map to inheritance
- [Representational form](./definitions/representational-form.md) — grounds: provides a worked instance of conditional warrant, in which two axes generate the categories, the empty cell, and the downstream inspection rule while relocating the untested part to the axes
- [Reflective system](./definitions/reflective-system.md) — grounds: provides a worked instance of transferred warrant, in which the inherited criteria and local extension are separated in an auditable provenance record
