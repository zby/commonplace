# Claim skeleton

Inputs read: `brief.md`, `reconstruction.md`, `claim-disposition.md` (both sections), `kb/notes/COLLECTION.md`, `kb/types/note.md`. No source note opened: the disposition's resolutions settled every point the plan needed. Not read: `original.md`, the live target, `kb/reports/`, drafts. Labels: **R** = reconstruction item, **C/I** = disposition candidate / incumbent item, **U** = user direction (brief), **Inf** = inference.

## Central claim

A theory's prototype standing is its expected revision cost, the total in kind of external binding (consumers coupled to the current version, so a change propagates) and intrinsic reconstruction cost (investment a revision discards), so internal proof or model dependencies and lost evidential investment count before any external adoption. (C1, verbatim in substance.)

Modality (ADR 066): **universal** over theories in the inspectable-parts sense, declared in the thesis. The stipulative half ("standing is expected revision cost") is a definition and is not refuted. The substantive universal is that the two components are exhaustive and separable, and that form and epistemic status enter only through them. Refuted by (a) one theory whose revision cost is materially set by something reducible to neither component — authority and rollback cost (R10d) must reduce to binding (rollback propagates to consumers; authority is consumers obliged to follow) or they are the counterexample — or (b) a pair equal in both components that differs in standing (C8). Not ideal-type: no exception conceded.

## Frontmatter plan

```yaml
description: "A theory's prototype standing is its expected revision cost — external binding plus the investment a revision discards — so natural-language versus symbolic form determines neither component and acceptance status is a separate axis"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining, self-improving-systems]
```

Description is the reconciliation's proposal (I0b), 38 words; no other fields.

## Title

`# A theory's prototype standing is its revision cost: external binding plus lost investment` (U working title, fixed by I0a). Composability: "since a theory's prototype standing is its revision cost: external binding plus lost investment" reads as prose; the colon-list is the only friction and is acceptable because the two components are the content a citer wants. Strength: contestable (the incumbent and the pre-formal note both assert a binding-only version).

## Ordered paragraph plan

**(1) Opening thesis** — reader learns what standing is, what quantity measures it, and what it is not. Split the packed opening into short sentences:
- "Theory" in the inspectable-parts sense, inline at first use: `a theory in the sense of [title](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md)` (R1; cited premise, no claim).
- Definition: prototype standing is expected revision cost; the cost is the total in kind of what a revision propagates to (binding) and what it discards (reconstruction), assessed in advance for the scope the revision would touch; no formula, no weights; "expected" in the ordinary sense of anticipated at assessment time (disposition resolution; Inf).
- Declare the mode: universal over such theories; one sentence naming what would refute it is deferred to paragraph (7).
- Lifecycle standing, not epistemic status: whether a theory is [accepted](./definitions/discovery-lifecycle.md) is a recorded decision and by itself neither raises nor lowers revision cost (C3; R5, R6, R7; Inf). Two-corner illustration: an accepted theory can keep prototype standing; a conjecture can become entrenched or heavily invested before acceptance (I4).
- Gloss disclaimer, one sentence: "prototype" is an engineering gloss for a build kept cheap to revise while its commitments are tested; not the [collection-prototype](../reference/collection-prototypes.md) sense (clone-once creation-time contract text) nor an exemplar, because a gloss must carry visible scope `as [title](./vocabulary-collisions-prevented-at-write-time-not-read-time.md)` requires (C4; R12, R13; U(a)).

**(2a) External binding** — reader can recognise the first component and its mechanism. Consumers coupled to the current version: procedures, validators, executables, and for instance a certified procedure or a training regime (U consumer list; certification/training illustrative only, generic wording). Mechanism inline: replacement grows expensive as dependants and migration cost accumulate, `because [title](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md)` (C12; R6; transfer from the KB structural layer to theories stated as a transfer, Inf). Natural-language high-binding example in one clause: a harness-loaded instruction whose wire is guaranteed, `as in [title](./goedel-machines-are-a-proof-governed-case-of-self-modification.md)` (C14; R14; transfer from prompt self-editing, Inf).

**(2b) Intrinsic reconstruction cost** — reader can recognise the second component and see that it counts with no consumers at all. Investment discarded on revision: for instance a large proof development, an approved safety case, a trained model (U; trained model supported by R14 coevolution; the other two generic illustrations, not evidence). Ground the component in the pre-formal note's "sunk work" clause: `since [title](./unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md)` denies that the medium makes rejection cheap and names sunk work beside coupling (R10d). Modulator in one clause: a theory retained with a faithful rationale is repaired part by part, one without it is deleted and re-derived, `since [title](./selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md)` (C13; R14; reading repair-vs-replacement as a cost effect is Inf). Close with I31 corrected: with no consumers, standing is set by reconstruction cost alone; an artifact of either form with neither consumers nor investment is cheap to discard (R6, R10d; U for the two-component correction).

**(3) Form determines neither component** — reader stops using form as a proxy for standing and learns what form does determine. Scope "form" to natural-language vs symbolic in the first clause (U; C15 handles parametric in Scope). "Determines neither" is universal: prose bound through a procedure, audit, or contract is expensive to revise; a low-authority formal sketch stays disposable (C2; R10b, R10d; I10 paired illustration). One sentence + link for C10: codification is a change of form and consumer kind — natural language into a symbolic artifact with assigned consequences, `as [codification](./definitions/codification.md) is defined` — and says nothing about deployment or acceptance (R3; note "committed to a symbolic consumer" means consequences assigned, not consumers coupled — Conflicts 2). I16 as availability, not tendency: codification makes formal consumption available; the standing change happens only when a validator or executable is actually coupled, so the added consumer, not the form, is the cause (R3, R6, R10e; Inf). I11 contrast clause so C2 does not read as "form is irrelevant": form changes which checks are available and what each use costs in interpretation, not what a revision costs, `since [title](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md)` (R2, R4, R10c). C2's weak-correlation clause: include only as one clause with its refuter — "symbolic artifacts may tend to carry construction investment prose does not, a tendency refuted by prevalence evidence that, at equal binding, form fails to predict discarded investment" — else drop it and keep only "determines neither" (U terminology section; Inf, no measurement). Omittable.

**(4) Warrant rule** — reader knows which act to withhold. Since binding is a cost component, binding a consumer before the theory is accepted for that consumer's scope spends standing that evidence has not licensed; acceptance for the bound scope — not current fit and not current form — licenses binding (C5; R6, R7, R10e; "for the bound scope" Inf from R2 + R6). Executable success is not acceptance: `because [title](./exact-implementation-does-not-validate-a-requirement.md)` (R7; U(b)). Coordination clause, one sentence: binding before acceptance may still be chosen for coordination value or forced by an enduring constraint, and is then knowingly spent standing priced by the current-task-fit note (Conflicts 3, resolved by scoping; no three-warrant taxonomy).

**(5) Grain** — reader can assess a partially codified theory. Standing is assessed per part at the grain consumers bind to, extending per-part warrant (R2) to per-part cost; parts differ in standing where *either* component differs; in partial codification binding is the component that usually differs, because codified and uncodified parts share the discarded investment unless the codified part carried its own construction such as a proof development (C6 consistency requirement; R4, R10c; "usually" is a scoped observation, not the claim). Illustration: a premise that becomes a checked operative invariant loses standing while the remainder keeps it (I20).

**(6) Cheap formalization** — reader can treat a formal model as an experiment. A symbolic artifact can exist unbound, so an unbound, lightly invested formal model has prototype standing (C7; R10d). Conditional: where construction, proof generation, or checking cost was the bottleneck, cheaper formalization lets formal models enter the prototype loop as experiments, and competing formal models preserve alternatives (R10f, R10 second paragraph; I12, I18 rival-models clause). Cost-bundle caveat by citation, not restatement: translation, construction, proof generation, checking, and world-fit evidence fall independently, per the pre-formal note (link already made in (2b); repeat inline only if the sentence needs the anchor). I28 entailment: cheaper checking leaves translation and world-fit costs where they were. One-clause pointer for what a proof warrants: entailment inside the model, not correspondence, `as [title](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) shows` (R8). The correspondence branch itself is not here (C9 fold).

**(7) What would refute this** — reader can test the claim. Short paragraph carrying C8 as a prediction: two theories of the same form and status differ in standing when binding or reconstruction cost differs; two of different form do not differ when both are equal; plus refuter (a) from the modality section (U(e); deduction from C1; no instantiating case — EVIDENCE NEEDED recorded in Open Questions, not hidden).

**(8) `## Scope`** bullets:
- Rejection retracts the claim and ends standing; revision and suspension preserve a surviving claim's standing only while both components stay low (I6/I33; R5, R14). Theory sense: procedures and state records are superseded, not refuted, and fall outside (I30; R14).
- Cheap and local are relative to named consumers and dependencies (I31; R6).
- Standing can be mixed across parts; only the grain consumers bind to is assessed (C6).
- Form scope: the "determines neither" bound covers natural-language versus symbolic form only.
- Distributed-parametric form — link at first use: `[distributed-parametric](./definitions/representational-form.md) form` — is outside that bound: a revision is a retraining rather than a per-item edit, so there the reconstruction component is set largely by the form (C15; R4, R14 coevolution).

**(9) `## Open Questions`**:
- Which observable costs measure external binding and reconstruction cost, so the paragraph (7) comparison can be run? (I36 reworded; carries C8's EVIDENCE NEEDED.)
- How should a system inventory prose authorities whose binding is real but not machine-readable? (I37.)
- When consumers bind to partially codified theories at different grains, which grain should a review or acceptance decision target? (I38.)
- C11 (prevalence hypothesis) omitted.

**(10) Footer** `Relevant Notes:` — format `- [title](path) — label: context phrase`:
- superseded-choices-are-retained-superseded-beliefs-are-not — `extends`: explains what the rejection exit implies for retaining or removing the artifact.
- selective-revision-needs-a-faithful-rationale-not-just-a-legible-one — `grounds`: why a retained rationale lowers what revision discards; cheap editing still does not guarantee the revision targets the failed premise. (Used inline in (2b); the label adds the verify-the-premise need.)
- treat-continual-learning-as-representational-form-coevolution — `grounds`: retraining cost and cycle time behind the distributed-parametric scope bullet.
- the-bitter-lesson-defense-portfolio-has-one-load-bearing-member — `extends`: classifies the cheap-formalization objection as an objection to permanent form, not to a prototype stage.
- goedel-machines-are-a-proof-governed-case-of-self-modification — `contrasts`: proof-gated acceptance couples authority and retention; here acceptance and binding are separate acts, and the guaranteed wire is the maximal-binding natural-language corner.
- current-task-fit-alone-does-not-warrant-costly-entrenchment — `mechanism`: how coupled consumers turn external binding into revision cost, and what prices binding chosen before acceptance.

All other links stay inline only.

## Inferential links

- "Sunk work" (R10d) → second component: the pre-formal note names sunk work beside coupling as what makes rejection expensive; C1 promotes it from a listed cost source to a named component. Inf, entailed by admitting the component (disposition C1).
- Why the two bills are separable: they are paid to different parties — propagation lands on consumers, discarding lands on the theory's owner — so one can be zero while the other is large (unbound proof development; bound one-line policy). This is what licenses "total in kind" over a maximum (resolution) and what makes the "residual" a mechanism rather than an exception.
- Why status is a separate axis: acceptance is a recorded decision with no cost content (R5); adoption does not establish reversibility (R7); so status changes neither bill by itself. Inf.
- Why the grain point follows: warrant is per part (R2) and localized forms are revisable per item (R4), so binding and investment attach to parts; standing, being their total, is per part.
- Why the warrant rule follows: binding raises the first component; spending it before acceptance for the bound scope is spending unlicensed; fit licenses adoption, not entrenchment (R6, R7).
- Gödel and current-task-fit uses are transfers (from prompt self-editing and from KB structure to theories); state them as transfers, not as findings about theories.

## Definitions and comparisons needed for truth conditions

- **Expected revision cost**: total in kind of the two components, assessed in advance for the scope a revision would touch; ordinary "expected"; no formula.
- **External binding**: consumers coupled to the current version so a change propagates; includes non-machine-readable coupling (procedure, audit, contract).
- **Intrinsic reconstruction cost**: investment discarded on revision, independent of consumer count.
- **Form**: natural-language vs symbolic for every "determines neither" statement; distributed-parametric only in Scope.
- **Codification** and **accepted**: by their linked definitions (form/consumer-kind crossing; a recorded lifecycle decision), never as deployment or cost.

## Unresolved markers

- C8 has no instantiating case — **published open question** (I36); the prediction and refuter are stated, no observation cited.
- Safety case, certification, training examples — **illustrative only**, generic wording, "for instance", never listed as evidence; **omittable** individually.
- C2 weak-correlation clause — **omittable**; include only with the one-clause refuter.
- Coordination-value exception — resolved by scoping in (4); **published limitation** in one clause.
- Handoffs, not this note: C9 fold, pre-formal note definition wording, defense-portfolio citer link.
- **Blocking: none.**

## Tempting branches to omit

The correspondence branch (scheduler, Eigenius, DiscoverPhysics, purely-formal exception — folded to `formal-systems-…`); the prevalence hypothesis (C11) and its refuter text; the relaxed Gödel machine; the return-path/relaxing sentence (I24); "formalization is already ordinary agent operation"; the three-warrant taxonomy (import only "coupled consumers make replacement expensive"); the collection-prototype catalogue; the parameter/nondeterminism/quantification enumeration (I12); "which consumer benefits" (I15); the "larger share of uncertainty" tendency (I28); I39.
