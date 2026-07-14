# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, roughly six working days to submission.

Inputs, not competitors: [epistack-competition](../epistack-competition/README.md) (two-repo protocol), [epistack-framework-additions](../epistack-framework-additions/README.md) (design menu). This workshop decides what we submit.

**Normative sources** (motivation thread revised 2026-07-14; keep submission prose inside their qualified claims):

- Motivation vocabulary: [actionable theory](../../notes/definitions/actionable-theory.md), [reflective system](../../notes/definitions/reflective-system.md), [cross-representational reflection](../../notes/cross-representational-reflection.md), [governed adaptation](../../notes/governed-adaptation-requires-search-evaluation-and-retention.md), [closure under recommendations](../../notes/closure-under-recommendations-bounds-governed-self-extension.md) — distinct properties, **not a maturity ladder**; do not inherit the former synthesis's ladder
- Classification: [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — discharges the five obligations against an observed repository trace (ADR 026 → schema → validator → changed agent behavior). **The deferral this workshop previously recorded is superseded.**
- Comparison: [Gödel machines](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — the sourced note the Gödel paragraph was waiting on now exists
- Method: [design-rationale-management.md](../../reference/design-rationale-management.md) — `81920ed9` (body edits from [full-pass report](../../kb/reports/full-pass/design-rationale-management/20260713T190521Z-ea26/full-pass-report.md))

## The pitch

**Investigations compound when a knowledge system's own rules are causally connected to its behavior — and in an agent-operated system that connection runs through retrieval. We present a governed adaptation loop (search → evaluation → operative retention) with heterogeneous verification and retained design rationale, demonstrated by a runnable reference implementation and three stress-test casebooks.**

Corollary the entry is built to earn: *a rule nobody can find is inert*, so findability is epistemic infrastructure, not housekeeping.

Two layers, one entry — do not submit them as parallel theses:

| Layer | Claim | Source |
|---|---|---|
| **Why (motivation)** | A knowledge system compounds when it holds a causally connected representation of its own rules — and that connection runs through **retrieval**, which is why findability is load-bearing rather than cosmetic | [Reflective system](../../notes/definitions/reflective-system.md) and [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) |
| **How (method)** | Design rationale management — established discipline; Commonplace distributes surfaces that *can retain* constraints, alternatives, evidence, and rejections when authors use them | [DRM reference](../../reference/design-rationale-management.md) |

The brief's hard problem is **methodology and workflow design**, not capability alone. Most entries will present **a stack**. We present **a governed adaptation loop**: search brings a candidate change into consideration, evaluation supplies grounds to accept or reject it, and operative retention preserves the accepted change *with behavioral authority* — so it binds the next pass instead of merely being on file ([governed adaptation](../../notes/governed-adaptation-requires-search-evaluation-and-retention.md)). The [Commonplace Casebook Protocol](../epistack-competition/README.md) is one closed-but-revisable instantiation, not a formal self-optimizing machine.

**Where we sit (say plainly):** Commonplace **is** a reflective system in the established computational sense — aspect-bound, socio-technical, and evidenced by an observed trace rather than by architecture. Its own type specs, collection contracts, and skills are a self-representation that its validators and agents consume *as their rule*, and changing that representation changes what the system subsequently requires, rejects, and searches ([classification](../../reference/commonplace-as-a-reflective-system.md)). The claim is on the **exercised** path, not the available one: intercession was performed, not merely permitted (the validator dispatches on the type spec's own path; in `dab163c6` the represented constraint reached back and forced edits to the represented system). Never argue this from architectural possibility — that reading sounds grander and is weaker.

**Keep two kinds of limit apart; a judge will conflate them.**

| Limit | What it bounds |
|---|---|
| Reflection is **aspect-bound** — most of the KB is knowledge, not self-representation | The reflective claim itself. State it wherever the claim appears. |
| **Search is substantially human** — the maintainer notices the problem; the methodology does not govern that. Evaluation is strong for structural constraints, weak for judgment-heavy ones. Retention passes through human merge | The **adaptation loop**, *not* reflection. |

This split is the answer to the obvious challenge ("but a person does the thinking — how is that self-reflective?"): a reflective architecture supplies a causal path by which the system can change itself; it does not supply the search, evaluation, and retention that governed adaptation requires ([governed adaptation](../../notes/governed-adaptation-requires-search-evaluation-and-retention.md)). Human-in-the-loop objections land on the loop, not on the classification. The converse holds too, and we say so: a change loop does **not** imply reflection — Ashby's ultrastable homeostat searches, evaluates, and retains while having no self-representation at all. The two properties are independent, which is why we evidence them separately. Reflection is also **not** autonomy, proof of improvement, or [closure under recommendations](../../notes/closure-under-recommendations-bounds-governed-self-extension.md).

**The mechanism that makes this more than a label.** In a system whose self-representation is a body of retained artifacts, the causal connection is *discovery*: an agent sweeps the artifacts, finds the ones bearing on the change it is making, and derives its behavior from what it found. Editing an artifact reaches later behavior with no one deciding to re-derive — **provided retrieval surfaces it**. So the search recipes, the descriptions that make an artifact findable, and the indexes that shortcut the sweep are the wire along which the system's rules act, and **retrieval failure is reflection failure**: a rule nobody can find is inert, and a completeness claim that stops an exhaustive reader while members are missing cuts the wire exactly where it is trusted. This is the general answer to why the unglamorous parts of the discipline — descriptions as retrieval filters, enforced rather than asserted index marks — are the parts that decide whether anything compounds.

An evaluation process determines whether there are sufficient grounds to retain a proposed change; an **oracle** here means the component or procedure supplying that judgment, such as deterministic checks, experiments, semantic review, human judgment, or a combination.

### The compounding barrier (judge-facing)

Compounding fails when the next investigator cannot recover **why** the system looks the way it does:

| Class | Example |
|---|---|
| **Forced by the world** | You cannot cite more precisely than you captured. |
| **Forced by this problem** | COVID needs an institutional layer; LHC needs dependency traversal. |
| **Freely chosen** | Grounding-layer marker as prose vs field — either works; record the pick and alternatives. |

In agent-built systems the barrier bites harder: without **retained** artifacts and **explicitly carried** rationale, each session re-pays interpretation and may diverge ([deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md)). Retained rationale **may then inform** the next pass — delimiting candidates, flagging disturbed premises, selecting verification — **when authors carry it forward**; surfaces support retention but do not guarantee continuity or reliable automatic recovery on every agent pass.

**Why it fails, mechanically.** The three failure modes judges will have seen — rationale nobody rereads, indexes that lie, conventions that drift from the code enforcing them — are one failure, not three. Each cuts the path from a retained rule to the next agent that should have obeyed it. That reframes the barrier from a discipline problem ("authors must be diligent") into an architecture problem with testable parts: *is the rule findable, is the finding enforced, and does the enforcement bind a consumer?* It also explains why diligence alone never fixed it.

### The governed adaptation loop (judge-facing spine)

```
search      — a candidate change enters consideration
  → evaluation   — grounds to accept or reject, under applicable criteria
  → operative retention — the accepted change is preserved *with authority over
                          a consumer*, not merely filed
  → changed conditions for the next pass — reached via retrieval
```

**Operative** is the load-bearing word: retention that no later process discovers changes nothing. Search reach and evaluation strength are independent limits — *evaluation cannot select a candidate that search never reaches* — which is why the submission reports both, and reports that our search is the human one.

**Evaluation is not an afterthought.** The same methodology must not be the sole judge of its own proposals (self-confirming loop risk). Separation of evaluation procedures is part of the design: mechanical checks where ground truth is shared; criterion-based review where judgment is local; experiments and labelled calibration where claims are empirical; explicit rejection records where shape is unknown. A retained change is accepted under those criteria, not thereby proved to be an improvement.

**Gödel machine (now admissible; one paragraph max).** The blocking condition — "not without a separate sourced note" — is met: [Gödel machines are a proof-governed case of reflective self-modification](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md). Use it as the *contrast that names our design choice*, not as an aspiration we fall short of. Schmidhuber's machine runs the same loop with a single proof gate: no rewrite without a proof it improves expected utility. That buys deductive rigor relative to a formalization and pays for it by making beneficial-but-unprovable changes unreachable. A knowledge system cannot formalize its own utility, so it substitutes **heterogeneous fallible oracles** — mechanical checks, experiments, criterion-based review, human judgment — and accepts a weaker guarantee (accepted under stated criteria) in exchange for a reachable candidate space. Same loop, different gate; naming the tradeoff is the point ([Schmidhuber, 2003](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html)).

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

1. **The loop** — architectural pattern for agent-built knowledge infrastructure. The [reflective-system](../../notes/definitions/reflective-system.md) classification is **no longer deferred**: it is discharged against an observed repository trace in [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md). Claim it, with its three shipped limits (aspect-bound, human search, not closure). Do not revive the former "reflexive executable" ladder — these are distinct properties, not stages.
2. **DRM** — established design discipline; Commonplace contribution is **distributed surfaces + author discipline** on worked material, not enforced end-to-end rationale continuity. The theory now says *why* that gap matters and what would close it: an unretrieved rule is an inert rule.
3. **Machinery** — three case shapes + observed contract transfer; transferability argument is **risk-framed**, not replication-proven ([replication-plan.md](./replication-plan.md) appendix carries the honest test).
4. **Spot experiments** — register drift (n=2); gate calibration (fitted on 4 notes). The classification rests on **one** worked maintenance trace (ADR 026), which is enough to establish the causal connection and not enough to characterize its reliability. Cite the epistack loop as construction evidence; cite the tag-readme trace for the classification. Do not merge the two.

## Submission document outline

Judge-facing; repos are evidence. **No Commonplace internal vocabulary** (operator note below).

| § | Title | Length | Content |
|---|---|---|---|
| 1 | Why compounding fails under agents | ½–1 page | Compounding barrier; the three classic failures are one failure (the rule → next-agent path is cut); retained rationale may inform next pass when carried forward; evaluation diversity + self-confirming risk |
| 2 | The governed adaptation loop | ½ page | Search / evaluation / operative retention; the system's rules are causally connected to its behavior **through retrieval**; Gödel-machine contrast (proof gate vs heterogeneous oracles); the three limits |
| 3 | Design rationale management | 1 page | Established lineage (DR/IDEF); surfaces *can retain*; **no** mechanical lineage; Epistack as sibling-repo illustration |
| 4 | Loop → epistemic stack | 1 page | Layer table; built vs rejected |
| 5 | Reference implementation | 1 page | Casebook Protocol + Commonplace; mechanical vs judgment boundary; falsification |
| 6 | Three stress tests | 1½ pages | Question + path per case |
| 7 | Evidence and limits | 1 page | Rebuild gates, experiments, audit trail, replication protocol; full-pass residuals (no traceability product, transfer claim unsupported, lifecycle gaps) |
| App | Runnable walkthrough | short | Clone, verify, planted failure |

**Tone:** §1–3 for naive readers. Framework operator docs (DRM and the foundational vocabulary notes) are optional appendix links, not required judge reading.

### Operator note (authors only)

Sync with [actionable theory](../../notes/definitions/actionable-theory.md), [reflective system](../../notes/definitions/reflective-system.md), [cross-representational reflection](../../notes/cross-representational-reflection.md), [governed adaptation](../../notes/governed-adaptation-requires-search-evaluation-and-retention.md), [the classification](../../reference/commonplace-as-a-reflective-system.md), and [DRM](../../reference/design-rationale-management.md). **Do not outrun qualified claims:** no "generative material" without "when authors carry forward"; no "safe reuse" without worked comparison; no "manages/preserves rationale" — use *surfaces can retain*. Internal vocabulary stays in framework notes.

**On the reflective claim specifically — the failure mode has flipped.** The risk was overclaiming; now that the classification is discharged, the risk is *inflating* it. Reflective ≠ autonomous, ≠ self-improving, ≠ proven-better. Never write it without the aspect bound and the human-search limit in the same breath. In judge-facing prose prefer the plain mechanism — "the system's own rules are what its validators and agents read, so changing a rule changes what it enforces and what it searches" — over the term "reflective system," which invites exactly the sci-fi reading §1–3 must avoid.

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
| Register-drift experiment | Evaluation procedure for the structure layer |
| Gate calibration | Evaluation calibration (charitable-reading failure) |
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
| Scale with AI/compute? | **§1–2:** methodology stays in executable prose; better models re-run criteria in new partitions; skills operationalize the loop. Scaling raises *evaluation* strength and *search* reach — the two independent limits — and the loop is built to absorb that without redesign |
| Compound? | **§1–2:** the loop compounds only when an accepted change is **operatively retained** — findable by the next pass and binding on a consumer. Filing it is not enough; a rule nobody retrieves is inert. This is why we report retrieval machinery (descriptions, enforced index marks) as *epistemic* infrastructure, not housekeeping |

## What closes it

Submission by 19 July: actionable methodology (bounded), design rationale management, epistemic-stack mapping, reference implementation, three-case evidence, limitations and negative results.

Then: promote durable conclusions; fold predecessor workshops; delete this directory.
