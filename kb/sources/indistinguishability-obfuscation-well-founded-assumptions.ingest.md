---
description: "Jain-Lin-Sahai build iO for all polynomial-size circuits from four standard subexponential assumptions; bears on opacity of symbolic form as a deliberate, scale-independent source"
source: https://arxiv.org/abs/2008.09317
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2
ingested: "2026-11-01"
occasion: "What does the construction establish, under which assumptions, and what does the paper itself say indistinguishability obfuscation guarantees or does not guarantee about hiding how a program works? What scope limits must accompany its use as evidence about opacity of symbolic form? The paper also appears as IACR ePrint 2020/1003, whose PDF returned 403 at capture, and at STOC 2021."
type: types/ingest-report.md
domains: [indistinguishability-obfuscation, program-obfuscation, cryptographic-assumptions, functional-encryption]
tags: [artifact-analysis]
---

# Ingest: Indistinguishability Obfuscation from Well-Founded Assumptions

## Classification

This is a theoretical cryptography paper. Its contribution is a construction with a security reduction. It reports no experiments or implementation. The captured text is arXiv 2008.09317v1 (dated 18 August 2020, posted 21 August 2020). The same work also appears as IACR ePrint 2020/1003 (https://eprint.iacr.org/2020/1003.pdf), which returned HTTP 403 at capture, and in the STOC 2021 proceedings. Neither of those versions was read, so differences between versions are unchecked.
Author: Aayush Jain (UCLA, NTT Research), Huijia Lin (University of Washington) and Amit Sahai (UCLA). Sahai co-authored the 2001 obfuscation-impossibility paper that first defined iO, and the paper builds on the authors' own earlier constructions (AJL+19, JLMS19, JLS19, GJLS20).

## Summary

Indistinguishability obfuscation (iO) is a probabilistic polynomial-time compiler with two properties. Its output computes the same function as its input (completeness). For any two functionally equivalent circuits of the same size, input length and output length, the two obfuscations are computationally indistinguishable (Definition 2.2). The paper constructs iO for all polynomial-size circuits. It assumes subexponential hardness of four assumptions with long histories: SXDH on asymmetric bilinear groups, LWE with subexponential modulus-to-noise ratio, LPN over large prime fields with polynomially low noise rate, and a Boolean PRG in NC0 with polynomial stretch (Theorem 1.1 and Theorem 5.5). Under only polynomial hardness of the same assumptions, it obtains collusion-resistant public-key functional encryption for all circuits. Earlier iO constructions relied on assumptions posed specifically for iO, and several of those were broken by cryptanalysis. Here, the new component is a structured-seed PRG built from LPN over fields. Its sparse noise lets a precomputation correct the seed's errors, so that the output is a degree-2 function of a short private seed (Sections 1.2 and 4). The remaining path from that PRG to iO reuses prior results: perturbation-resilient generators, then sublinearly compact functional encryption, then iO via the Ananth-Jain and Bitansky-Vaikuntanathan transformation (Section 5). The paper does not discuss what iO hides about how a program works. It states only the formal definition and attributes the notion to Barak et al.; it does not discuss virtual black-box obfuscation, "best-possible" interpretations, efficiency, or post-quantum security.

## Contribution assessment (our opinion)

Before this paper, whether iO exists under well-studied assumptions was a central open problem. The question matters because so much of cryptography now builds on iO, and the earlier assumption base kept being broken. The paper settles feasibility by reduction to four assumptions with independent histories, so iO's security now rests on the same kind of evidence as other primitives. Most of the pipeline is earlier work, including some by the same authors. The paper's own step, the LPN-based structured-seed PRG, is short, which makes the reduction easier to check and criticise. Our background knowledge (not this capture) says the result was widely treated as the landmark resolution of the problem. That knowledge also says later work removed or replaced some assumptions, and the construction as a whole is not post-quantum, because SXDH falls to Shor-type algorithms. Neither point is established here. The result is a feasibility theorem: subexponential hardness and polynomial blow-ups leave the construction far from practical, and the paper makes no efficiency claim. Its significance is theoretical existence, not a deployable obfuscator.

## Quotes

> Theorem 1.1. (Informal) Let τ be arbitrary constants greater than 0, and δ, ǫ in (0, 1). Assume
> sub-exponential security of the following assumptions, where λ is the security parameter, and the
> parameters ℓ, k, n below are large enough polynomials in λ:
> • the SXDH assumption on asymmetric bilinear groups of a prime order p = O(2λ),
> ǫ
> • the LWE assumption over Zp with subexponential modulus-to-noise ratio 2k , where k is the
> dimension of the LWE secret,
> • the LPN assumption over Zp with polynomially many LPN samples and error rate 1/ℓδ ,
> where ℓ is the dimension of the LPN secret,
> • the existence of a Boolean PRG in NC0 with stretch n1+τ ,
> Then, (subexponentially secure) indistinguishability obfuscation for all polynomial-size circuits exists.
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Section 1, Theorem 1.1; superscripts flattened by the PDF capture

> Further, assuming only polynomial security of the aforementioned assumptions,
> there exists collusion resistant public-key functional encryption for all polynomialsize circuits.
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Abstract

> Definition 2.2 (Indistinguishability Obfuscator (iO) for Circuits). A uniform PPT algorithm
> iO is called a (T, γ)-secure indistinguishability obfuscator for polynomial-sized circuits if the following holds:
> • Completeness: For every λ ∈ N, every circuit C with input length n, every input x ∈
> {0, 1}n , we have that
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Section 2, Definition 2.2, opening and completeness clause (formula omitted)

> • (T, γ)-Indistinguishability: For every two ensembles {C0,λ } {C1,λ} of polynomial-sized
> circuits that have the same size, input length, and output length, and are functionally equivalent, that is, ∀λ, C0,λ (x) = C1,λ (x) for every input x, the following distributions are (T, γ)indistinguishable.
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Section 2, Definition 2.2, indistinguishability clause

> Despite this success, until this work, all previously known iO constructions
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Section 1; citation list follows

> required
> new hardness assumptions that were postulated specifically for showing security of the
> iO schemes proposed. Indeed, the process of understanding these assumptions has been
> tortuous, with several of these assumptions broken by clever cryptanalysis
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Section 1, continuation after the citation list

> The remaining standing ones are based on new and novel computational problems that
> are different in nature from well-studied computational problems (for instance, LWE with
> leakage on noises).
> --- `kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md` @ `sha256:204b0c11eddb338d706cdd9da3f344c38181271a4ccfedd9ce95b98196c079d2` — Section 1

## Connections Found

The source's role in this KB is a narrow formal counterpoint on opacity. The KB has no cryptography scope, and this ingest records the paper only for what it implies about reading symbolic artifacts. [Representational form](../theory/definitions/representational-form.md) defines symbolic content by a unique operational semantics that a fixed consumer implements. An obfuscated circuit still meets that definition, because completeness fixes its input-output behaviour exactly. Under the indistinguishability definition, though, inspecting the artifact cannot computationally distinguish it from the obfuscation of any equivalent circuit of the same size. The artifact is therefore symbolic in form and opaque by deliberate construction. This bears on [Opacity is a scale threshold, not a class property](../theory/opacity-depends-on-the-inspection-question-and-budget.md) (is-evidence-for, in a bounding direction): that note names scale as the cause of opacity, but iO yields opacity from a transformation, independent of how large the original program is. The bearing on [Inspectable artifact, not supervision, defeats the blackbox problem](../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) is secondary. That note's claim that code is inspectable assumes the code has not been adversarially transformed. The "what is hidden" reading that these connections need is an inference from Definition 2.2, not a statement the paper makes.

- [arXiv 2008.09317](https://arxiv.org/abs/2008.09317) — derived-from: this ingest analyses the arXiv v1 text
- [Opacity is a scale threshold, not a class property](../theory/opacity-depends-on-the-inspection-question-and-budget.md) — is-evidence-for: deliberate obfuscation is an opacity source not governed by scale, which bounds the note's single-cause account
- [Representational form](../theory/definitions/representational-form.md) — defined-in: the symbolic form whose opacity modifier this source informs
- [On the (Im)possibility of Obfuscating Programs](./on-the-impossibility-of-obfuscating-programs.ingest.md) — compares-with: the paper that defines the notion this source constructs and proves the strong form impossible

## Extractable Value

1. **What the construction establishes, under which assumptions** -- iO for all polynomial-size circuits exists if SXDH, LWE (subexponential modulus-to-noise ratio), LPN over Zp (noise rate 1/ℓ^δ) and an NC0 PRG with polynomial stretch are all subexponentially hard (Theorems 1.1 and 5.5). Polynomial hardness of the same four assumptions yields collusion-resistant public-key functional encryption. A future opaque-modifier definition can cite this as conditional existence: deliberately opaque symbolic programs exist if standard assumptions hold. It should not present the result as unconditional or practical. [quick-win]
2. **The guarantee is relative indistinguishability among equivalent same-size circuits, nothing more** -- Definition 2.2 promises only completeness and indistinguishability between obfuscations of functionally equivalent circuits with the same size and input and output lengths. It promises nothing about circuits that are not equivalent, and it states no virtual black-box or "learns nothing beyond input-output behaviour" property. The paper itself never says what iO hides or fails to hide about how a program works. Any wording in the opaque modifier such as "reading reveals no more than any equivalent program" is therefore the KB's inference or comes from other literature (for example, Barak et al.'s impossibility paper). It must be sourced there, not to this paper. [quick-win]
3. **Opacity can be deliberate and independent of scale for symbolic artifacts** -- a symbolic artifact keeps its fixed operational semantics while being transformed so that inspection cannot distinguish it from equivalent alternatives. This qualifies the scale-threshold opacity note, which names only scale as the cause. It also supports treating opacity as a modifier on a form rather than as a form, as the representational-form misuse case already argues. [experiment]
4. **The paper's scope limits** -- the result is conditional on subexponential hardness of all four assumptions. It covers polynomial-size circuits, not Turing machines or RAM programs. It gives only computational indistinguishability. It makes no efficiency claim and does not discuss post-quantum security. These are the limits a KB citation must carry beside any use of the result. [just-a-reference]

## Limitations (our opinion)

The paper is a security reduction, so its conclusion is only as strong as the four assumptions. The authors argue that the assumptions are well-founded through their history and wide use, but that is evidence of resistance to attack, not proof. The capture also cannot tell us about cryptanalysis published after August 2020. For the commissioning question, the main limitation is absence: the paper does not discuss what iO means for hiding how a program works. It gives the formal definition and attributes the notion to Barak et al. Statements about what iO can and cannot hide, including the impossibility of virtual black-box obfuscation and the "best-possible obfuscation" interpretation, belong to other papers and need their own ingests. The construction has subexponential security loss and polynomial overheads with no stated concrete parameters, so it says nothing about whether opaque symbolic artifacts are feasible at practical sizes. The KB-side inference has its own limit. Cryptographic indistinguishability is a bound on computationally bounded adversaries, while the KB's opacity concerns practical inspection by agents and humans. Treating the two as the same notion of opacity is an analogy that the opaque-modifier text should state explicitly rather than assume. Only the arXiv v1 text was read. The ePrint and STOC versions may differ in theorem statements or parameters.

## Recommended Next Action

Revise [Opacity is a scale threshold, not a class property](../theory/opacity-depends-on-the-inspection-question-and-budget.md) to distinguish deliberate obfuscation from scale-driven opacity. Use this ingest only for conditional iO existence under the four named assumptions and Definition 2.2's equivalent-circuit indistinguishability guarantee; use the [Barak et al. ingest](./on-the-impossibility-of-obfuscating-programs.ingest.md) for the VBB limits and the reading-versus-running distinction.
