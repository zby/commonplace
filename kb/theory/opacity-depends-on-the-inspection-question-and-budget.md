---
description: "Distinguishes scale, the reference's form, and deliberate obfuscation as inspection obstacles relative to a behavior or change, a consumption path, and an affordable budget."
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, artifact-analysis]
---

# Opacity depends on the inspection question and budget

Opacity depends on the inspection question and budget, not just the artifact's size or [representational form](./definitions/representational-form.md), how content is encoded and consumed. An artifact can be readable for one question and opaque for another. A short prompt may expose its wording without exposing what an adopted model package will do with an edit. A large program may be easy to inspect for one local effect and difficult to inspect for a system-wide invariant.

Symbolic content is **opaque** under a consumption path, relative to a behavior or change of interest, when the artifact together with its reference does not let an inspector establish that behavior, or the effect of that change, at acceptable cost. The question, available tools and evidence, and affordable inspection budget belong beside an opacity judgment. The same practical qualification applies when inspecting natural-language or distributed-parametric content. Opacity is an inspection property, not a fourth form.

## Three sources of opacity

### Scale

Reading each unit need not make an aggregate affordable to inspect. A program's lines can be readable against its language reference while tracing their interactions exceeds the inspector's budget. A natural-language KB can exceed the budget for reading all relevant claims and dependencies. Search, modularity, diffing and retrieval can extend affordable inspection; coupling can defeat local reasoning even where each unit remains readable.

Scale therefore matters relative to the question. There is no single size at which every question about an artifact becomes opaque. Nor does readable syntax guarantee an affordable answer to an arbitrary behavioral question.

### The reference's form

The reference has a form under the path on which it is read. Reading it on that path may not answer a question asked on another path.

Consider a system that pins a model package, including its decoding procedure, and adopts it as the reference for one operation. Under the runtime's path, kernels and numerical operands are addressed units with fixed consequences. Under the interpreter's path, the system runs the model as a whole; the rule assigning a consequence to an instruction such as "summarize" is not exposed as a separately readable unit. Reading the numerical operations does not by itself supply that instruction-level rule.

The gap is between the path on which the reference is readable and the path on which the inspection question is asked. It can matter for a one-line prompt: reading its words and the runtime's arithmetic does not supply an affordable prediction of the edit's effect. Inspection then needs behavioral cases or other analysis. This is not a claim that every question about every model is opaque, or that increasing the budget and improving tools cannot help.

### Deliberate obfuscation

A transformation can obstruct inspection without changing a program's function. Cryptographic definitions make particular hiding goals precise, but do not equate every hiding goal with practical unreadability.

[Barak and co-authors](../sources/on-the-impossibility-of-obfuscating-programs.ingest.md), Definition 2.2, define a virtual black-box goal: efficient computation from the obfuscated circuit should reveal no more than efficient computation with oracle access to its input–output behavior. Their Theorem 3.11 shows, assuming one-way functions, circuit families whose source can be reconstructed from any equivalent circuit but not from black-box access. A program is a description on which further computations can operate; oracle access need not provide an equivalent opportunity. Their counterexamples rule out a general virtual black-box obfuscator, not obfuscation of every useful program. The authors describe the counterexamples as contrived.

A weaker goal is indistinguishability obfuscation: obfuscations of equivalent, same-size circuits are computationally indistinguishable. [Jain, Lin and Sahai](../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md), Theorem 1.1, construct it for polynomial-size circuits under the stated sub-exponential security assumptions on SXDH, LWE, LPN and an NC0 pseudorandom generator. Read with the equivalence conditions in their Definition 2.2 and Barak's Definition 7.1, this hides which equivalent circuit was supplied, not everything about the function it computes.

The transfer to inspection is narrow. Deliberate transformation supplies an inspection obstacle other than aggregate size; the cryptographic guarantee concerns a specified computational distinction, not all human understanding. Conversely, the unobfuscatable families show why possessing a program can reveal more than running it. Symbolic form guarantees neither readability nor successful hiding.

## What opacity changes

Keep three questions separate:

1. Did execution conform to the reference?
2. What behavior does the reference specify, including permitted variation and failure outputs?
3. Does that behavior satisfy the requirement?

Opacity removes an affordable inspection route for the question at hand. Evaluation then relies more on execution, other analysis such as abstraction or certificates, or explicitly retained uncertainty. None is a guaranteed substitute for understanding. Where a relevant rule can be read, comparing it with the requirement provides a route to finding inadequacy; reading alone does not prove adequacy.

For an adopted frozen package, an undesirable specified output is an inadequacy against the requirement, not necessarily a gap in the reference or a failure to execute it. Changing the prompt can require experiments because its effect cannot be read off affordably. Adoption fixes what counts as conforming; it does not make adequacy cheap to establish.

## Scope

An opacity judgment is relative to a behavior or change, a consumption path, tools and evidence, and an acceptable cost. The three mechanisms can coexist. No universal ordering of forms by inspection cost follows, and increasing size need not obstruct every local question. The obfuscation results bound particular hiding claims; they do not establish a practical readability threshold for ordinary code or models.

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — grounds: form and consumption path identify what is being inspected
- [Inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — contrasts: readable code is an inspection opportunity, not a guarantee for every question and budget
- [On the impossibility of obfuscating programs](../sources/on-the-impossibility-of-obfuscating-programs.ingest.md) — evidenced-by: bounds the hiding claim; circuit descriptions can reveal more than oracle access, preventing general virtual black-box obfuscation
- [Indistinguishability obfuscation from well-founded assumptions](../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md) — evidenced-by: bounds deliberate hiding to indistinguishability among equivalent same-size circuits under the stated assumptions
