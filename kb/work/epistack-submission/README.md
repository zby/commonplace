# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, roughly six working days to submission.

Inputs, not competitors: [epistack-competition](../epistack-competition/README.md) (two-repo protocol), [epistack-framework-additions](../epistack-framework-additions/README.md) (design menu). This workshop decides what we submit.

**Normative sources (still revising):**

- Motivation: [actionable-theories-and-reflexive-system-construction.md](../../notes/actionable-theories-and-reflexive-system-construction.md)
- Method: [design-rationale-management.md](../../reference/design-rationale-management.md)

## The pitch

**Actionable methodology for compounding epistemic investigations: an agent-executable construction loop with heterogeneous verification and retained design rationale — demonstrated with a runnable reference implementation and three stress-test casebooks.**

Two layers, one entry — do not submit them as parallel theses:

| Layer | Claim | Source |
|---|---|---|
| **Why (motivation)** | When agents build investigations, methodology must be executable and successful changes must be retained — otherwise every session re-pays interpretation and drifts | [Actionable theories note](../../notes/actionable-theories-and-reflexive-system-construction.md) |
| **How (method)** | Design rationale management — established discipline for recording constraints, alternatives, evidence, and rejections across repository surfaces | [DRM reference](../../reference/design-rationale-management.md) |

The brief's hard problem is **methodology and workflow design**, not capability alone. Most entries will present **a stack**. We present **a reflexive construction loop**: actionable theory and retained rationale → candidate change → verification → retained artifact → changed conditions for the next application. The [Commonplace Casebook Protocol](../epistack-competition/README.md) is one closed-but-revisable instantiation, not a formal self-optimizing machine.

**Where we sit (say plainly):** reflexive executable methodology (the system carrying the theory is among what the theory can construct or modify). **Not** verified reflexive extension — no proof that each change is globally optimal. Heterogeneous oracles (deterministic checks, experiments, semantic review, human judgment) bound reach instead.

### The compounding barrier (judge-facing)

Compounding fails when the next investigator cannot recover **why** the system looks the way it does:

| Class | Example |
|---|---|
| **Forced by the world** | You cannot cite more precisely than you captured. |
| **Forced by this problem** | COVID needs an institutional layer; LHC needs dependency traversal. |
| **Freely chosen** | Grounding-layer marker as prose vs field — either works; record the pick and alternatives. |

In agent-built systems the barrier bites harder: if rationale is not retained, the agent reconstructs the same extension from prose on every pass, paying again for interpretation and admitting fresh divergence ([actionable theories note](../../notes/actionable-theories-and-reflexive-system-construction.md)). **Rationale is then generative material**, not merely historical record — it delimits candidate changes, shows which premises a proposal would disturb, and selects an appropriate verification method.

### The construction loop (judge-facing spine)

```
actionable methodology + retained rationale
  → candidate change
  → verification (heterogeneous oracles)
  → retained system artifact
  → changed conditions for the next application
```

**Verification is not an afterthought.** The same methodology must not be the sole judge of its own proposals (self-confirming loop risk). Separation of oracles is part of the design: mechanical checks where ground truth is shared; criterion-based review where judgment is local; experiments and labelled calibration where claims are empirical; explicit rejection records where shape is unknown.

**Gödel machine (one paragraph max in submission):** architectural analogy only — self-description, candidate rewrite, proof of improvement, executed self-modification. Knowledge systems trade proof-bound reach for fallible reach via diverse verification. Not an equivalence claim ([Schmidhuber, 2003](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html) via actionable theories note).

### The method — design rationale management

Established research, not a coinage ([MIT Design Rationale](https://rationale.csail.mit.edu/); [FSE framework](https://doi.org/10.1017/dsj.2024.19); IDEF9 discovers bounds, IDEF6 records rationale when bounds leave options open — [IDEF compendium](https://www.idef.com/wp-content/uploads/2016/02/compendium.pdf)).

DRM is the **repository discipline** that feeds the loop: discover what bounds a decision; record what those bounds do and do not determine; test on worked cases; promote shared machinery only after evidence warrants it.

| Rationale state | Surface (plain language) | Role in the loop |
|---|---|---|
| Active exploration | Workshops, experiments | Candidate changes not yet earned |
| Finished but undecided | Design proposals | Options, forces, free choices |
| Implemented decision | Architecture decision records | Committed changes + consequences |
| Local contract | Per-collection conventions | Problem-local bounds without universal claim |
| Shared machinery | Types, validators, package code | Promoted after scope and enforcement clear |
| Rejected / displaced | Backlog Outcomes, supersession, history | Why an alternative was not selected |

DRM does **not** enforce end-to-end traceability — authors must still carry rationale forward explicitly ([DRM reference](../../reference/design-rationale-management.md)). The submission shows that discipline populated on real casework, not a perfect traceability product.

Epistack practice on top: sibling `backlog-to-commonplace.md`; build-local-first; worked-case guard before framework promotion.

**Standardize the connective tissue, not the contested substance** — a commitment recorded in rationale, not asserted as taste.

### Applying the loop to the epistemic stack

Brief layers as **outcomes the loop must recover and verify**:

| Layer | What bounds the design | Loop stage illustrated |
|---|---|---|
| **Ingestion** | Capture bounds citation; provenance without KB-voice ranking | Candidate: standing constituents; verify: schema + case use; retain: local types |
| **Structure** | Contested substance cannot flatten; verdict in context contaminates maps | Candidate: verdict/map separation; verify: register-drift experiment; retain: collection contracts |
| **Assessment** | Shared ground → mechanical check; local judgment → documented criteria | Verify: 127/127 quotes, conformance + calibration; **reject** crux scoring and authority ranking (shape unknown) |

Brief bullets via **recorded rationale**, not omission:

- **Correlated evidence** — independence not visible from agreement → standing fields, casebook prose; optional matrix cut first ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- **Cruxes** — contested joints are crux mapping; crux scoring declined (shape unknown).
- **Calibration** — partition-scoped review; register drift as evidence against scalar credences (sibling experiment note).

### Reference implementation (evidence)

Runnable proof the loop closes on real material:

- **Sibling casebooks** — rebuild **complete**: 0 validate failures, **127/127** quotes, **14/14** conformance PASS, freshness demonstrated.
- **Framework** — validators, review store, skills — each promotion backed by proposal/ADR/backlog rationale.

**Falsification:** clone → clean corpus passes checks → planted quote break fails.

### Three cases — stress tests of the loop

Cases show **which bounds and verifications bit**, not which side is right:

| Case | Loop pressure | Navigational question |
|---|---|---|
| **COVID** | Institutional incommensurability; correlated cluster | "Three confirming papers — or one programme thrice?" |
| **LHC** | Dependency chain; meta-critique of the argument | "What does safety rest on, and where is the argument's reliability contested?" |
| **Eggs** | Competing syntheses; institutional divergence | "Why didn't the 2015 reversal settle it?" |

One walkthrough per case: source → ingest → note → validate → review → freshness.

## Generalization — bounded claims

1. **The loop** — actionable methodology + retained rationale + heterogeneous verification applies to agent-built knowledge infrastructure generally; we demonstrate at reflexive-executable level, not proof-verified.
2. **DRM** — established design discipline; our contribution is distributed repository practice on worked material.
3. **Machinery** — three case shapes + observed contract transfer; not independent replication ([replication-plan.md](./replication-plan.md) appendix).
4. **Spot experiments** — register drift (n=2); gate calibration (fitted on 4 notes). Size claims to evidence.

## Submission document outline

Judge-facing; repos are evidence. **No Commonplace internal vocabulary** (operator note below).

| § | Title | Length | Content |
|---|---|---|---|
| 1 | Why compounding fails under agents | ½–1 page | Compounding barrier; rationale as generative material; loop diagram; verification diversity |
| 2 | The construction loop | ½ page | Actionable methodology; reflexive scope; Gödel analogy with limits; level-2 claim |
| 3 | Design rationale management | 1 page | Established lineage; three-class barrier; repository surfaces; honesty about non-enforced traceability |
| 4 | Loop → epistemic stack | 1 page | Layer table; built vs rejected |
| 5 | Reference implementation | 1 page | Casebook Protocol + Commonplace; mechanical vs judgment boundary; falsification |
| 6 | Three stress tests | 1½ pages | Question + path per case |
| 7 | Evidence and limits | 1 page | Rebuild gates, experiments, audit trail, replication protocol |
| App | Runnable walkthrough | short | Clone, verify, planted failure |

**Tone:** §1–3 for naive readers. Framework operator docs (DRM, actionable theories) optional appendix links — not required judge reading.

### Operator note (authors only)

Sync submission prose with [actionable-theories note](../../notes/actionable-theories-and-reflexive-system-construction.md) and [DRM](../../reference/design-rationale-management.md). Internal vocabulary (technical constraining, first principles, homoiconic medium) stays in framework notes — translate to: *what bounded the choice, what was recorded, what was verified how, what was retained*.

Map epistack evidence to loop stages explicitly when drafting §7:

| Evidence | Loop stage |
|---|---|
| Backlog / proposals / ADRs | Retained rationale |
| Standing block, local types, quote verifier | Candidate → verify → retain |
| Register-drift experiment | Verification oracle for structure layer |
| Gate calibration | Oracle calibration (charitable-reading failure) |
| 127/127 quotes, 14/14 conformance | Mechanical verification on shipped corpus |
| Rejected ranking / crux scoring | Recorded rejection |

## Evaluation boundary

- Submission document outranks everything before 19 July.
- Casework in sibling repo; framework changes here.
- No new machinery casework has not earned.
- Settled: no scalar credence/authority in frontmatter; adjudication downstream and labelled.
- Do not build bulk-operations or independent-builder experiment on critical path.
- Keep submission prose ahead of revising normative docs but not outrunning their claims.

## Build plan

### Done

| Item | Evidence |
|---|---|
| Quote verifier | ADR 046; **127/127** |
| Validation contract, shared runs | ADR 050 |
| Full-pass guard | ADR 051 |
| Three-case rebuild | Sibling workshop — all gates |
| Normative notes | Actionable theories + DRM (revising) |

### Must ship

1. **Submission document** per outline §1–7.
2. **Short methodology appendix** — loop + DRM surfaces + Casebook Protocol conformance checklist (consolidate validation contract, review system, ADRs 038, 041, 046, 051, 052).
3. **Falsification package** — clean pass + planted failure.
4. **Naive-reader pass** + adversarial review.

### Should ship if time allows

- Hands-free transcript (one full loop iteration on a new source).
- §2 sidebar: scaling with AI — partitions, criterion re-run, skills as re-executable methodology.

### Cut first

- Correlated-evidence matrix ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- Replication experiment execution.
- ADR laundry lists in main text.

### Rejected — on record

Authority ranking, crux scoring, scalar credence — shape unknown; rejection is the discipline.

## Schedule

| Days | Work |
|---|---|
| 1 | **DONE.** Evidence landed |
| 1–2 | **Draft §1–3.** Loop motivation + DRM method |
| 2–3 | **Draft §4–6.** Stack mapping, implementation, case walkthroughs |
| 3 | Falsification + optional transcript |
| 4–6 | Integrate, naive-reader pass, buffer |

**Priority if days run out:** submission doc (§1–7) → appendix → walkthroughs → falsification → transcript → matrix.

## Judging questions

| Question | Answer |
|---|---|
| Help reason about the case? | §6 walkthroughs |
| Generalize? | Loop as methodology + DRM as discipline + bounded machinery + replication appendix |
| Scale with AI/compute? | **§1–2:** methodology stays in executable prose; better models re-run criteria in new partitions; skills operationalize the loop |
| Compound? | **§1:** retained rationale changes initial conditions for the next agent; loop only compounds if verification outputs are retained |

## What closes it

Submission by 19 July: actionable reflexive methodology (bounded), design rationale management, epistemic-stack mapping, reference implementation, three-case evidence, limitations and negative results.

Then: promote durable conclusions; fold predecessor workshops; delete this directory.