# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, roughly six working days to submission.

Inputs, not competitors: [epistack-competition](../epistack-competition/README.md) (two-repo protocol), [epistack-framework-additions](../epistack-framework-additions/README.md) (design menu). This workshop decides what we submit.

**Normative sources** (full-pass revised 2026-07-13; keep submission prose inside their qualified claims):

- Motivation: [actionable-theories-and-reflexive-system-construction.md](../../notes/actionable-theories-and-reflexive-system-construction.md) — `b02cbc1c`, `28665b55`
- Method: [design-rationale-management.md](../../reference/design-rationale-management.md) — `81920ed9` (body edits from [full-pass report](../../kb/reports/full-pass/design-rationale-management/20260713T190521Z-ea26/full-pass-report.md))

## The pitch

**Actionable methodology for compounding epistemic investigations: an agent-executable construction loop with heterogeneous verification and retained design rationale — demonstrated with a runnable reference implementation and three stress-test casebooks.**

Two layers, one entry — do not submit them as parallel theses:

| Layer | Claim | Source |
|---|---|---|
| **Why (motivation)** | When agents build investigations, methodology must be executable and successful changes must be retained — otherwise every session re-pays interpretation and drifts | [Actionable theories note](../../notes/actionable-theories-and-reflexive-system-construction.md) |
| **How (method)** | Design rationale management — established discipline; Commonplace distributes surfaces that *can retain* constraints, alternatives, evidence, and rejections when authors use them | [DRM reference](../../reference/design-rationale-management.md) |

The brief's hard problem is **methodology and workflow design**, not capability alone. Most entries will present **a stack**. We present **a reflexive construction loop**: actionable theory and retained rationale → candidate change → verification → retained artifact → changed conditions for the next application. The [Commonplace Casebook Protocol](../epistack-competition/README.md) is one closed-but-revisable instantiation, not a formal self-optimizing machine.

**Where we sit (say plainly):** reflexive executable methodology (the system carrying the theory is among what the theory can construct or modify). **Not** verified reflexive extension — no proof that each change is globally optimal. Heterogeneous oracles (deterministic checks, experiments, semantic review, human judgment) bound reach instead.

### The compounding barrier (judge-facing)

Compounding fails when the next investigator cannot recover **why** the system looks the way it does:

| Class | Example |
|---|---|
| **Forced by the world** | You cannot cite more precisely than you captured. |
| **Forced by this problem** | COVID needs an institutional layer; LHC needs dependency traversal. |
| **Freely chosen** | Grounding-layer marker as prose vs field — either works; record the pick and alternatives. |

In agent-built systems the barrier bites harder: without **retained** artifacts and **explicitly carried** rationale, each session re-pays interpretation and may diverge ([actionable theories note](../../notes/actionable-theories-and-reflexive-system-construction.md)). Retained rationale **may then inform** the next pass — delimiting candidates, flagging disturbed premises, selecting verification — **when authors carry it forward**; surfaces support retention but do not guarantee continuity or reliable automatic recovery on every agent pass.

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

DRM is a **repository discipline** that can feed the loop — not an enforced traceability protocol: distributed surfaces *can retain* constraints, alternatives, decisions, and evidence; authors must still link and carry rationale explicitly. No mechanical lineage from implementation back to originating alternatives ([DRM](../../reference/design-rationale-management.md), full-pass open items).

| Rationale state | Surface (plain language) | Role in the loop |
|---|---|---|
| Active exploration | Workshops, experiments | Candidate changes not yet earned |
| Finished but undecided | Design proposals | Options, forces, free choices |
| Implemented decision | Architecture decision records | Committed changes + consequences |
| Local contract | Per-collection conventions | Problem-local bounds without universal claim |
| Shared machinery | Types, validators, package code | Promoted after scope and enforcement clear |
| Rejected / displaced | Backlog Outcomes, supersession, history | Why an alternative was not selected |

The submission shows the discipline **populated in practice** on sibling casework (`epistack-casebooks`, not artifacts in this repo) — examples of surfaces used, not proof of automatic compounding or safe transfer without author linking.

Epistack practice on top: `backlog-to-commonplace.md`; build-local-first; worked-case guard before framework promotion. DRM's Epistack paragraph frames a **transfer-assessment risk** (three-class distinction missing → reuse confidence drops), not a demonstrated safe-reuse theorem — friction gate still rates that claim **unsupported** without a worked before/after reuse comparison ([full-pass report](../../kb/reports/full-pass/design-rationale-management/20260713T190521Z-ea26/full-pass-report.md) routed attention).

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

Worked illustration of loop stages on real material (not a proof of automatic closure):

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

1. **The loop** — architectural pattern for agent-built knowledge infrastructure; we claim **reflexive executable** scope only (mutable surround, heterogeneous oracles), not verified reflexive extension. LLM is one interpreter path; homoiconic prose is **conditional** on framing, not guaranteed ([actionable theories note](../../notes/actionable-theories-and-reflexive-system-construction.md)).
2. **DRM** — established design discipline; Commonplace contribution is **distributed surfaces + author discipline** on worked material, not enforced end-to-end rationale continuity.
3. **Machinery** — three case shapes + observed contract transfer; transferability argument is **risk-framed**, not replication-proven ([replication-plan.md](./replication-plan.md) appendix carries the honest test).
4. **Spot experiments** — register drift (n=2); gate calibration (fitted on 4 notes). Actionable-theories note still lacks a worked Commonplace maintenance trace (TODO in note) — cite epistack loop evidence instead until filled.

## Submission document outline

Judge-facing; repos are evidence. **No Commonplace internal vocabulary** (operator note below).

| § | Title | Length | Content |
|---|---|---|---|
| 1 | Why compounding fails under agents | ½–1 page | Compounding barrier; retained rationale may inform next pass when carried forward; loop diagram; oracle diversity + self-confirming risk |
| 2 | The construction loop | ½ page | Actionable methodology; reflexive scope (surround not weights); Gödel analogy with limits; level-2 only |
| 3 | Design rationale management | 1 page | Established lineage (DR/IDEF); surfaces *can retain*; **no** mechanical lineage; Epistack as sibling-repo illustration |
| 4 | Loop → epistemic stack | 1 page | Layer table; built vs rejected |
| 5 | Reference implementation | 1 page | Casebook Protocol + Commonplace; mechanical vs judgment boundary; falsification |
| 6 | Three stress tests | 1½ pages | Question + path per case |
| 7 | Evidence and limits | 1 page | Rebuild gates, experiments, audit trail, replication protocol; full-pass residuals (no traceability product, transfer claim unsupported, lifecycle gaps) |
| App | Runnable walkthrough | short | Clone, verify, planted failure |

**Tone:** §1–3 for naive readers. Framework operator docs (DRM, actionable theories) optional appendix links — not required judge reading.

### Operator note (authors only)

Sync with post-full-pass [actionable-theories note](../../notes/actionable-theories-and-reflexive-system-construction.md) and [DRM](../../reference/design-rationale-management.md). **Do not outrun qualified claims:** no "generative material" without "when authors carry forward"; no "safe reuse" without worked comparison; no "manages/preserves rationale" — use *surfaces can retain*. Internal vocabulary stays in framework notes.

**§7 must name limits from full-pass (not solved in prose):**

- No enforced lineage proposals → ADRs → implementations
- Selected-but-unimplemented designs: lifecycle gap (ADR 028 interval not fully governed)
- Epistack casework inspectable in sibling repo only
- Transferability three-class argument: illustrative, not friction-cleared

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
- Submission prose must stay **inside** full-pass-qualified normative docs — if the pitch outruns the reference notes, narrow the pitch.

## Build plan

### Done

| Item | Evidence |
|---|---|
| Quote verifier | ADR 046; **127/127** |
| Validation contract, shared runs | ADR 050 |
| Full-pass guard | ADR 051 |
| Three-case rebuild | Sibling workshop — all gates |
| Normative notes | Actionable theories + DRM — full-pass revised (`81920ed9`, `b02cbc1c`, `28665b55`) |

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
| Compound? | **§1:** loop compounds only when verified outputs are **retained artifacts** and rationale is **explicitly carried** — not automatic from distributed surfaces alone |

## What closes it

Submission by 19 July: actionable reflexive methodology (bounded), design rationale management, epistemic-stack mapping, reference implementation, three-case evidence, limitations and negative results.

Then: promote durable conclusions; fold predecessor workshops; delete this directory.