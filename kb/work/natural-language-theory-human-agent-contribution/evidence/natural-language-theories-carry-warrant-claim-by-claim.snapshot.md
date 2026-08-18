<!-- Frozen copy of kb/notes/natural-language-theories-carry-warrant-claim-by-claim.md, captured 2026-08-18. Do not update this evidence file when the source changes. -->

---
description: "Why natural-language theories can carry explanatory-reach while warrant remains limited to interpreted claims and supported scopes, and what formalization adds"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, learning-theory, discovery]
---

# Natural-language theories carry warrant claim by claim and scope by scope

Natural-language theories can carry explanatory-reach because they can state criticizable dependencies among conditions, mechanisms, and consequences. Their [representational form](./definitions/representational-form.md) makes those dependencies available through interpretation rather than through a parser, runtime, or proof system. That difference changes how the theory is assessed; it does not decide whether the theory can explain.

The form does not warrant what it carries. Warrant attaches to a particular interpretation of a claim and to the domain over which support licenses reliance. One document may therefore contain observations, derived consequences, abductive mechanisms, and transfer claims with different epistemic status.

Here, a **theory** means an account whose relevant premises or conditions, mechanism or invariant, consequences, and scope can be inspected and revised as named parts. A claim to explanatory-reach also needs an implication that could discriminate the account from a rival. This is a working definition for retained knowledge artifacts, not an exhaustive taxonomy of theories. **Epistemic warrant** means support that licenses reliance on a specified claim over a specified domain, conditional on its assumptions and proportional to the discriminating evidence or proof available.

## Criticizable structure makes reach possible

[Explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) is not fluency, breadth, or usefulness in the case that produced an account. It depends on capturing why a pattern works so that the account continues to work where the same structure is preserved. Reach is graded: a theory may carry a narrow family of cases because it captures one shared structure without supplying a complete generative model.

A criticizable explanation constrains how its conclusion should change when a load-bearing premise changes. Rival exclusion, a risky consequence, or a predicted failure gives the account discriminating content that post-hoc fit lacks. A stated boundary serves the same structural role by naming the condition under which transfer should stop.

Yet [being able to state a boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md) does not show that the boundary tracks the real mechanism. A consumer may match a new case to the stated condition while that condition follows only a correlate. Premise variation, rivals, boundaries, and falsifiers expose what evidence would count for or against a theory; they do not supply that evidence.

This separates two thresholds. A natural-language account crosses a structural threshold when it exposes dependencies and possible failure. It crosses an epistemic threshold only when evidence, proof, or a justified transfer relation supports reliance on those dependencies over a specified scope. [Reach-assessment](./definitions/reach-assessment.md) concerns the second threshold: it judges whether the claimed explanatory-reach is genuine rather than adaptive fit presented as explanation.

## Warrant attaches to claim-scope pairs

A **claim-scope pair** is bookkeeping for one material claim and the domain over which its support licenses reliance. It does not redefine explanatory-reach as a set. It prevents evidence for one claim or domain from spreading silently across a whole theory.

Support reaches these pairs by different routes. Derivation from independently supported constraints can supply starting warrant while those constraints remain operative. Inheritance from tested work can transfer starting warrant only when the source tests discriminated relevant rivals and the target preserves the constraints that made the source claim work. The existing account of [derivation, inheritance, and earned scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md) is framed for reusable decompositions; applying its pattern to claims inside a natural-language theory is an inference.

Discriminating tests, interventions, held-out comparisons, or risky predictions warrant the cases and failure modes they exercise. Examples that fit both the theory and its rivals add little discrimination. Transfer to an untested class requires a justified relation between the evidence and that class, such as coverage, sampling, independence, invariance, or a supported mechanism. Which relation suffices remains domain-dependent; case count and surface variety alone do not settle it.

These routes do not produce one document-wide truth label. A theory may combine observations, deductions, abductive mechanisms, and conjectured boundaries. Abduction may rank candidate mechanisms without earning their transfer scope. Because [mixed epistemic status must be preserved below the document level](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md), each material claim retains the scope and warrant of its own support.

## Interpretation is a form-specific boundary

Natural language lets people and language models generate, criticize, and revise theories before a defined formal consumer exists. That openness makes a wider candidate space practically available, as conjectured in [theory-mediated learning](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). It is a capacity for working with theories, not evidence that reviewers reliably select theories with genuine reach.

Because natural-language consequences arise through semantic interpretation, reasonable readings can differ about a premise, prediction, or boundary. Human or language-model criticism can expose assumptions, rivals, counterexamples, and test targets, but the available account of natural-language reach-assessment does not explain or calibrate the reliability of that criticism. Semantic judgment can improve criticizability without itself guaranteeing warrant.

This leaves a second-order scope question. A theory's effective interpretation may depend on interpreter or model, context, wording, and task. That dependence follows plausibly from interpretive consumption, but it has not been established as a stability law. Until it is tested, semantic stability across those conditions remains part of the uncertainty rather than part of the theory's warranted reach.

## Formalization strengthens only the checks it defines

Formalization can translate a generality claim into a theorem, invariant, causal model, type property, or model-checking obligation. Proof and exhaustive model checking can establish a translated consequence throughout the states admitted by a formal model. Causal and invariance tests instead provide intervention- and assumption-relative empirical warrant; they do not inherit the exhaustive force of proof.

The warrant remains bounded by the translation. As [formal systems assess reach through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md), proof warrants entailment from axioms, and causal inference warrants conclusions relative to its assumptions. Neither establishes that the variables, axioms, domain, or model-to-world bridge represent the intended commitment. A wrong translation can pass its formal checks, and establishing one translated proposition does not retroactively warrant natural-language claims that the translation omitted or changed.

Formalization is required where the intended operation or guarantee depends on assigned symbolic consequences, such as proof over a formal domain or mechanically repeatable acceptance. An exact numerical claim still needs quantitative evidence or derivation, but it can be stated and tested in natural language; numerical content alone does not make symbolic form necessary. Formalization may also resolve an ambiguity, but it is not the only way to narrow interpretation. It strengthens consequence-checking inside a chosen representation and moves semantic judgment to construction of the model and its bridge to the world.

## One theory can cross the thresholds unevenly

The account that [agent context is constrained by soft degradation rather than hard limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) illustrates the distinction. It separates explicit limit rejection from well-formed but degraded performance, synthesizes evidence about volume, interference, and complexity, proposes a limited-workspace mechanism, and states predictions and a falsifier. Those features expose explanatory structure that can be criticized.

Its warrant is less uniform. Its empirical inputs are specific to tasks and models, while its headline is broader, and the workspace mechanism is a working hypothesis. The case therefore shows how a retained natural-language theory can cross the structural threshold while its mechanism and transfer scope remain unevenly warranted. It is an audit of claim-level status, not evidence that natural-language theories generally transfer.

## Scope

This argument establishes a route by which natural-language theories can carry epistemic warrant. It does not establish how often they achieve explanatory-reach, how reliable human or language-model reach-assessment is, or whether premise variation, rival exclusion, boundaries, and falsifiers predict transfer rather than merely producing explanation-shaped text. The conditions under which finite evidence warrants an unobserved class also remain domain-dependent.

Natural language therefore has epistemic standing as a theory-bearing form without receiving a form-wide guarantee. Broad reuse can propagate a successful explanation across cases, but it can propagate error just as broadly; a failed premise or revised boundary should change only the claims that depend on it.

---

Relevant Notes:

- [Representational form](./definitions/representational-form.md) — defined-in: distinguishes interpretive natural-language consequences from assigned symbolic consequences without making either an epistemic rank
- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: names the judgment that separates claimed explanatory-reach from adaptive fit
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — contrasts: shows what formal checks warrant inside a translation and what remains outside it
- [Mixed epistemic status must be preserved below the document level](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md) — grounds: warrant remains attached to material claims and inferential transitions rather than whole documents
