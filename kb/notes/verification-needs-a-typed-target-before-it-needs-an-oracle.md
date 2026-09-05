---
description: "A check's warrant depends on a declared target class, so an unverifiable heterogeneous layer is usually blocked by missing artifact classification, not oracle difficulty — ontology precedes oracle"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, artifact-analysis]
---

# Verification needs a typed target before it needs an oracle

An oracle is a check with a domain — the candidates it can assess with the required confidence, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). A domain is a set of artifacts, so stating one requires being able to say which artifacts fall inside it and which do not. That is a classification. Where the artifacts are unclassified, a check can still be run and still return a verdict, but the verdict ranges over nothing statable: passing implies only that this instance passed. The check yields judgments without warrant.

So a layer can be unverifiable for two quite different reasons, and they call for opposite work. Either no oracle exists that discriminates what matters, or no target class exists for an oracle to range over. The second is prior — not merely earlier in a sensible order, but a precondition for the first being well-posed.

The claim concerns *reusable* verification. A check can always be aimed at one artifact — name the file, run the suite whenever it changes — and that check's domain is the singleton it names. What a class buys is coverage of instances that do not exist yet: a domain stated over a kind holds for the next member without anyone extending anything. Where a layer is edited continuously by the system it governs, per-artifact checks are precisely the ones that fall silently behind.

## Why the ontology cost is invisible

In code the classification is free, which is why it goes unnoticed. The language supplies it: a file has a declared kind, a module has a boundary, a function has a signature, a record has fields. Every familiar check presupposes a partition the substrate already made — a compiler targets a translation unit, a test targets a named unit, a linter targets a syntax class, a type checker targets declarations. The ontology was paid for by the language designer and never appears on the project's ledger.

Natural-language content has no such substrate. Markdown supplies a file boundary and nothing else: no declared kind, no membership, no contract. A team that extends self-modification from code into natural-language content therefore carries across the oracle habit without the ontology habit, having never seen itself pay for one.

That is what makes the resulting failure easy to misdiagnose. Facing an unverifiable natural-language layer, the natural move is to reach for a better judge — a stronger model, a sharper rubric, a panel of reviewers. But a judge with no declared target class inherits the undefined domain. The judge can be improved indefinitely without producing warrant, because what is missing sits upstream of judgment.

## The classification has to be readable by the check

An ontology held only in the maintainers' heads, or described in prose *about* the layer, does not do this work. To dispatch a check, the class must be legible in the artifact itself — frontmatter, path, declared type — which is the natural-language-to-symbolic crossing [codification](./definitions/codification.md) names. And the class must assert something structural, [since document types should be verifiable](./document-types-should-be-verifiable.md): a label that adds no checkable information is decoration, and restores the undefined domain under a more confident name.

## Heterogeneity is what makes the claim bite

The cost scales with how mixed the layer is. Where a layer holds one kind of artifact, classification is free again — the class is the layer, and there is nothing to partition. A directory of test fixtures needs no ontology.

What makes a natural-language layer resist verification is that it mixes consumption paths in one substrate: text injected into every call, text loaded on demand, text read only by humans, text consumed as binding policy, text consumed as reference. Under [artifact analysis](./axes-of-artifact-analysis.md) those differ in behavioral authority and therefore in what evidence would review them at all. On disk they are the same kind of thing, edited the same way. The ontology's job is to make the distinctions the checks depend on visible to the checks.

[Exo](../agentic-systems/reviews/exo.md) is the case to check, since both layers sit in one repository under one agent — and checking it carefully corrects the tempting version of the story. Its natural-language content is not unclassified. Its self-control document partitions durable state into eight kinds by lifecycle, with routing rules sending user-specific memory to the local profile and behavioral changes to checked-in prompts; memory and todos have dedicated tools with enforced count and length caps; skills carry required frontmatter validated at install.

What is striking is where the line falls. Every natural-language kind Exo declared has a check. Every kind it left undeclared has none — including the persona prompt that defines the agent, the self map injected into every turn, and the design documents holding its actual theory of itself. The checks landed exactly where there was a class to attach them to.

The same case bounds the claim. Those checks are shape checks: field presence, length caps, lifecycle placement. Declaring a class supplies the attachment point, not the contract that would make a check semantic. Classification is what verification needs *first*, not what it needs *most*.

## Scope

- Necessity, not sufficiency. A fully classified layer with no oracle remains unverified. The claim orders two requirements; it does not collapse one into the other.
- Logical priority, not a development waterfall. Classes are often discovered by attempting checks and finding what the check needed to know, which is how [progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md) works. The claim is that a check is not well-defined until its target class is — not that the ontology must be designed before any check is attempted. An ontology authored ahead of worked cases is the failure mode on the other side.
- Stated for symbolic and natural-language layers, where classification is authored. The parametric case appears to rhyme — an eval suite declares the behavior classes a model is judged over, and under-specified benchmarks produce the same unwarranted pass — but that extension is asserted here, not argued.

## Open Questions

- Whether a heterogeneous layer's classes can be reliably proposed by an agent reading it, or whether declaring them is irreducibly a commitment about the system's structure that something outside the loop must make.
- What the minimum viable ontology is: how few classes buy how much verifiability, and whether the first partition to draw is by behavioral authority or by representational form.
- Whether any case exists where a sufficiently strong judge substitutes for classification rather than merely masking its absence.

---

Relevant Notes:

- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the oracle-domain concept the argument turns on, and why an undefined domain cannot bound anything
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — extends: verification cost determines what automates; this adds that part of that cost is ontological and falls due before oracle construction
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — mechanism: the four-field record is one such ontology, and supplies the consumption-path unit that heterogeneity mixes
- [Document types should be verifiable](./document-types-should-be-verifiable.md) — extends: constrains which classifications serve a check, once a classification exists
- [Codification](./definitions/codification.md) — defined-in: the natural-language-to-symbolic crossing a class must make to be readable by a check
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — contrasts: guards the scope against reading logical priority as up-front ontology design
- [Representational form](./definitions/representational-form.md) — defined-in: why form sets the default review method, so mixing forms in one layer mixes review regimes
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — see-also: the strength axis this claim is orthogonal to — a weak oracle over a declared class still has a domain
- [Exo](../agentic-systems/reviews/exo.md) — evidenced-by: verified code and unverified natural-language in one system, with the single typed natural-language class the only one carrying a check
