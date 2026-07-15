# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, roughly four working days left.

Inputs, not competitors: [epistack-competition](../epistack-competition/README.md) (two-repo protocol), [epistack-framework-additions](../epistack-framework-additions/README.md) (design menu). This workshop decides what we submit.

**Normative sources** (self-improvement cluster rewritten 2026-07-15; keep submission prose inside their qualified claims):

- The object: [self-improving system](../../notes/definitions/self-improving-system.md) — an adaptation loop run on the system itself, against an improvement objective. Reflection and autonomy are **separate gradients**, not part of the definition; *reflective self-improving system* and *autonomous self-improving system* are the reserved boundary terms, and Commonplace claims the first. What reflection buys is [addressability, not compounding](../../notes/reflection-buys-addressability-not-compounding.md).
- The loop: [an adaptation loop requires search, evaluation, and operative retention](../../notes/an-adaptation-loop-requires-search-evaluation-and-retention.md).
- The bound: [warranted autonomy is bounded by oracle reach](../../notes/warranted-autonomy-is-bounded-by-oracle-reach.md) and [the boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md).
- The asymmetry: [false-positive generation is filtered; false-positive acceptance becomes operative](../../notes/false-positive-generation-is-filtered-before-retention.md).
- The unit: [actionable methodology](../../notes/definitions/actionable-methodology.md) — a methodology is actionable only relative to an operator, available operations, a target, and a setting. This is what we are submitting.
- Classification: [Commonplace as a reflective system](../../reference/commonplace-as-a-reflective-system.md) — a **human-inclusive self-improving system**, with the autonomy profile stated.
- Method: [design rationale management](../../reference/design-rationale-management.md) — `81920ed9`, body edits from the [full-pass report](../../reports/full-pass/design-rationale-management/20260713T190521Z-ea26/full-pass-report.md).
- Curated head: [self-improving systems](../../notes/self-improving-systems-README.md).

> **The previous spine is retired.** This workshop used to lead with *"Commonplace **is** a reflective system — say it plainly."* Our own theory now says that claim is nearly empty: [human-inclusive boundaries make reflection cheap](../../notes/human-inclusive-boundaries-make-reflection-cheap.md), so under a declared boundary containing a maintainer, essentially every maintained system is reflective. Do not resurrect the reflective headline, the "reflection is aspect-bound" framing as the lead limit, or the maturity ladder. Reflection is machinery, and it is the cheap part.

## The pitch

**A knowledge system that improves is an adaptation loop — search, evaluation, operative retention — run on itself. In an agent-operated system, the thing it runs *through* is its methodology: the retained prose an agent reads before it acts. So methodology, not capability, is what compounds. We present a methodology for agent-operated epistemic investigation, a runnable reference implementation, and three stress-test casebooks — and we are candid that the binding constraint is the evaluator, which is the part we are actively building.**

The entry's distinguishing move is a refusal followed by a program. Most entries will present a stack whose assessment layer is an LLM judge. We ran that experiment, it failed silently, and we caught it — so we do not claim what we cannot yet verify. Instead we ship the methodology, the mechanical checks where ground truth is shared, an explicit record of the gates where judgment stays human, and **the procedure for moving gates out of that category one at a time**.

**The oracle is the frontier, and the frontier is where the work is.** Say it as a direction of travel, not a confession: an unattended gate is only as trustworthy as the oracle behind it, oracle strength is improvable, and the human retreats exactly as far as the oracles advance. That gives the methodology a measurable trajectory rather than a fixed apology — each gate hardened (rubric → documented criterion → labelled regression → validator → test) is a gate that moves from judgment to verification, and we can say which ones have moved.

**Why methodology is the unit.** In an agent-operated system the methodology is not documentation *about* the system; it is the system's operative rule. The agent reads the collection contract, the type spec, the skill, and derives its behavior from what it found. Editing that prose changes what the next agent does, with nobody deciding to re-derive — **provided retrieval surfaces it**. That is why the unglamorous parts (descriptions as retrieval filters, enforced rather than asserted index marks) are epistemic infrastructure: [a rule nobody can find is inert](../../notes/retrieval-failure-is-reflection-failure.md), and a completeness claim that stops an exhaustive reader while members are missing cuts the wire exactly where it is trusted.

**Where we sit — say it plainly, and say it early.** Commonplace is a **human-inclusive self-improving system**: the loop closes, it runs on the system's own artifacts, and it aims at an objective it could have failed. It is **not autonomous**, and that is a finding rather than an apology. Humans hold search and every judgment-heavy gate, and they sit exactly where no adequate oracle reaches ([classification](../../reference/commonplace-as-a-reflective-system.md), autonomy profile).

**Never write the loop as a maturity ladder, and never sell autonomy as progress.** Bare autonomy is free — hand a gate to a model with a rubric and nobody runs it tomorrow. The evaluator is fallible but it still rejects things, so the loop still closes and the system stays self-improving *while quietly getting worse*. What is bounded is [**warranted** autonomy](../../notes/warranted-autonomy-is-bounded-by-oracle-reach.md): the loop can run unattended only over candidates its oracles can assess with the required confidence.

An **oracle** is the component or procedure supplying the grounds to accept or reject — deterministic checks, experiments, criterion-based review, human judgment, or a combination.

### The compounding barrier (judge-facing)

Compounding fails when the next investigator — or the next agent pass — cannot recover **why** the system looks the way it does. Rationale nobody rereads, indexes that lie, conventions that drift from the code enforcing them: judges will have seen all three, and they are one failure, not three. Each cuts the path from a retained rule to the next agent that should have obeyed it.

That reframes the barrier from a discipline problem ("authors must be diligent") into an architecture problem with testable parts: *is the rule findable, is the finding enforced, and does the enforcement bind a consumer?* It also explains why diligence alone never fixed it.

Which rationale must be recoverable:

| Class | Example |
|---|---|
| **Forced by the world** | You cannot cite more precisely than you captured. |
| **Forced by this problem** | COVID needs an institutional layer; LHC needs dependency traversal. |
| **Freely chosen** | Grounding-layer marker as prose vs field — either works; record the pick and the alternatives. |

In agent-built systems the barrier bites harder: without **retained** artifacts and **explicitly carried** rationale, each session re-pays interpretation and may diverge ([deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md)). Retained rationale **may then inform** the next pass — delimiting candidates, flagging disturbed premises, selecting verification — **when authors carry it forward**. Surfaces support retention; they do not guarantee continuity.

### The loop (judge-facing spine)

```
search      — a candidate change enters consideration
  → evaluation   — grounds to accept or reject, under an objective it could fail
  → operative retention — the accepted change is preserved *with authority over
                          a consumer*, not merely filed
  → changed conditions for the next pass — reached via retrieval
```

Three things a judge should take from this and nothing more:

1. **Operative is the load-bearing word.** Retention that no later process discovers changes nothing. A reviewed note nothing loads has no consumer; a patch never merged has no channel; a validator nothing invokes has no force. In each, the work happened and the loop stayed open.
2. **Search reach and evaluation strength are independent limits.** *Evaluation cannot select a candidate that search never reaches.* We report both, and we report that our search is the human one.
3. **Acceptance is an improvement *claim*, not improvement.** The oracle certifies that the candidate met the criterion applied — not that the system got better. The criterion may be wrong, partial, or measuring the wrong thing.

**Why evaluation is where the design effort goes.** The two scarce functions fail asymmetrically: [false-positive generation is filtered; false-positive acceptance becomes operative](../../notes/false-positive-generation-is-filtered-before-retention.md). A candidate wrongly proposed meets the evaluator and costs effort; a candidate wrongly *accepted* is retained with behavioral authority and compounds. In an epistemic stack that is the whole ballgame — a wrongly rejected claim costs a re-read; a wrongly accepted one poisons every investigation downstream of it.

**We are still building the oracles — and we know how to tell whether we are getting anywhere.** The load-bearing result is a failure we caught. A semantic conformance criterion was authored, shipped, and trusted for three days while its central limb had a **zero firing rate against known positives**. It was ruled MET in **12 of 12** blind reviews — *including reviews of both known-drifted notes* — and produced articulate, plausible output throughout. Nothing readable in the twelve reviews distinguished the inert limbs from working ones.

The warning generalizes, and it is the entry's sharpest contribution to the assessment layer: **a fluent LLM judge is observationally identical to a working one, because the missing signal is exactly the signal the judge was supposed to provide.** Any epistemic stack that automates assessment without labelled calibration has bought bare autonomy and no warrant — and cannot find out by reading its own reviews.

What makes this a program rather than a confession is that the failure was *detectable and fixable*, cheaply:

| Step | Status |
|---|---|
| **Diagnosis** — a four-note labelled sample (2 drifted, 2 clean, 3 blind reviewers each) exposed both inert limbs in one afternoon | Done, on the sibling corpus |
| **Repair** — the rewritten criterion separated on that sample: drifted WARN 3/3, clean PASS 3/3 (in-sample; not a detection-rate estimate) | Done, once |
| **Protocol** — a non-leaking, human-labelled known-case regression suite required before any semantic gate advances; live detection rates reserved for a separately sampled field study | **Designed, not shipped** — [calibration proposal](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) |
| **Direction of travel** — [oracle hardening](../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) moves a gate from unwarranted to warranted autonomy: a rubric becomes a criterion, a criterion becomes a validator, a heuristic becomes a test | Ongoing; the type-spec/validator spine is what it looks like when it lands |

(Sibling repo `epistack-casebooks`, `kb/work/post-commonplace-upgrade/track-a/calibration/REPORT.md`.)

So the honest position is not *our evaluators are weak, sorry* but: **evaluator quality is the binding constraint on any epistemic stack, it is measurable, most stacks are not measuring it, and here is the instrument.** [Oracle hardening expands warranted reach](../../notes/warranted-autonomy-is-bounded-by-oracle-reach.md) — where the criteria still outrun the oracle, the system keeps a human at the gate rather than pretending.

**Gödel machine (one paragraph max, as contrast — never as aspiration).** [Schmidhuber's machine](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) runs the same loop with a single proof gate: no rewrite without a proof it improves expected utility. It is the *autonomous* corner, bought with the strongest available oracle and paid for in reach — every improvement it cannot prove is unreachable. A knowledge system cannot formalize its own utility, so it substitutes heterogeneous fallible oracles and accepts a weaker guarantee in exchange for a reachable candidate space. Same loop, different gate; naming the trade is the point ([Schmidhuber, 2003](https://people.idsia.ch/~juergen/gmweb2/gmweb2.html)).

### The method — design rationale management

Established research, not a coinage ([MIT Design Rationale](https://rationale.csail.mit.edu/); [FSE framework](https://doi.org/10.1017/dsj.2024.19); IDEF9 discovers bounds, IDEF6 records rationale when bounds leave options open — [IDEF compendium](https://www.idef.com/wp-content/uploads/2016/02/compendium.pdf)).

DRM is a **repository discipline** that feeds the loop — not an enforced traceability protocol. Distributed surfaces *can retain* constraints, alternatives, decisions, and evidence; authors must still link and carry rationale explicitly. There is no mechanical lineage from an implementation back to its originating alternatives ([DRM](../../reference/design-rationale-management.md), full-pass open items).

| Rationale state | Surface (plain language) | Role in the loop |
|---|---|---|
| Active exploration | Workshops, experiments | Candidate changes not yet earned |
| Finished but undecided | Design proposals | Options, forces, free choices |
| Implemented decision | Architecture decision records | Committed changes + consequences |
| Local contract | Per-collection conventions | Problem-local bounds without universal claim |
| Shared machinery | Types, validators, package code | Promoted after scope and enforcement clear |
| Rejected / displaced | Backlog Outcomes, supersession, history | Why an alternative was not selected |

The submission shows the discipline **populated in practice** on sibling casework (`epistack-casebooks`, not artifacts in this repo) — examples of surfaces used, not proof of automatic compounding or safe transfer without author linking.

Epistack practice on top: `backlog-to-commonplace.md`; build-local-first; worked-case guard before framework promotion. DRM's Epistack paragraph frames a **transfer-assessment risk** (three-class distinction missing → reuse confidence drops), not a demonstrated safe-reuse theorem — the friction gate still rates that claim **unsupported** without a worked before/after reuse comparison.

**Standardize the connective tissue, not the contested substance** — a commitment recorded in rationale, not asserted as taste.

### Applying the loop to the epistemic stack

Read each layer as: *what bounds the design, and what oracle can actually assess a change to it?*

| Layer | What bounds the design | Oracle today | Autonomy | Next hardening step |
|---|---|---|---|---|
| **Ingestion** | Capture bounds citation; provenance without KB-voice ranking | **Hard** — verbatim spans checked against the cited snapshot (127/127) | Unattended, warranted | Already landed; extend coverage to paraphrase fidelity |
| **Structure** | Contested substance cannot flatten; a verdict in context contaminates the map | **Mixed** — schema and collection contracts mechanical; register drift only via experiment (n=2) | Partial | Turn the drift experiment into a standing check |
| **Assessment** | Shared ground → mechanical check; local judgment → documented criteria | **Soft and under construction** — semantic criteria are fallible and one was demonstrably inert until labelled calibration caught it | Human stays at the gate | Labelled known-case regression before any gate advances (designed, not shipped) |

The last column is the point. The methodology does not claim the assessment gate is solved; it claims to know **which gate is unwarranted, why, and what would warrant it** — and it keeps the human there until then.

The rejections belong in the same table's logic, not in a footnote: **crux scoring, authority ranking, and scalar credence were declined** — not because they are uninteresting but because we had no oracle of known shape for them, and an unverifiable score in frontmatter is a false-positive acceptance with a number on it. Recorded rejection *is* the discipline.

Brief bullets via **recorded rationale**, not omission:

- **Correlated evidence** — independence is not visible from agreement → standing fields, casebook prose; optional matrix cut first ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- **Cruxes** — contested joints are crux *mapping*; crux *scoring* declined.
- **Calibration** — partition-scoped review; register drift as evidence against scalar credences.

### Reference implementation (evidence)

Worked illustration of the loop on real material — not a proof of automatic closure:

- **Sibling casebooks** — rebuild **complete**: 0 validate failures, **127/127** quotes, **14/14** conformance PASS (with the calibration caveat above stated in the same breath), freshness demonstrated.
- **Framework** — validators, review store, skills — each promotion backed by proposal/ADR/backlog rationale.
- **The one observed self-improvement trace** — ADR 026 → schema → validator → *changed agent behavior*: an agent now skips a search it used to run, and the represented constraint reached back and forced edits to the represented system ([classification](../../reference/commonplace-as-a-reflective-system.md), `dab163c6`).

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

1. **The methodology** — the deliverable. Actionable for an agent operator with the stated operations in the stated setting ([actionable methodology](../../notes/definitions/actionable-methodology.md)); demonstrated on three casebooks. Not proven transferable — see 3.
2. **The loop** — the frame that positions the methodology and bounds what it may claim. Commonplace is a human-inclusive self-improving system, with humans at search and the judgment-heavy gates. This is discharged against **one** observed maintenance trace (ADR 026) — enough to establish the causal connection, not enough to characterize its reliability.
3. **DRM** — established design discipline; the Commonplace contribution is **distributed surfaces + author discipline** on worked material, not enforced end-to-end rationale continuity. The theory says *why* the gap matters: an unretrieved rule is an inert rule.
4. **Machinery** — three case shapes + observed contract transfer; the transferability argument is **risk-framed**, not replication-proven ([replication-plan.md](./replication-plan.md) carries the honest test).
5. **The oracle program** — evaluator quality is the binding constraint, it is measurable, and we have the instrument (labelled known-case regression) plus one worked diagnosis-and-repair. The *protocol* is designed, not shipped; claim the instrument and the direction of travel, never a solved assessment layer.
6. **Negative results are load-bearing, not disclaimers.** The inert-gate failure and the three recorded rejections are among the entry's more useful contributions. Give them their own section, framed as *caught and being fixed* — not as a list of things we got wrong.

## Submission document outline

Judge-facing; repos are evidence. **No Commonplace internal vocabulary** (operator note below).

| § | Title | Length | Content |
|---|---|---|---|
| 1 | Why compounding fails under agents | ½–1 page | The barrier; the three classic failures are one failure (the rule → next-agent path is cut); in an agent system the methodology *is* the operative rule, so methodology is what compounds |
| 2 | The loop, and where the human is | ½–1 page | Search / evaluation / operative retention; acceptance is a claim, not improvement; false-positive acceptance compounds while rejection only costs effort; **warranted** autonomy vs bare autonomy; Gödel-machine contrast |
| 3 | Design rationale management | 1 page | Established lineage (DR/IDEF); surfaces *can retain*; **no** mechanical lineage; Epistack as sibling-repo illustration |
| 4 | The stack, layer by layer, with its oracles | 1 page | Layer/oracle/autonomy table; built vs rejected, with the reason |
| 5 | Reference implementation | 1 page | Casebook Protocol + Commonplace; mechanical vs judgment boundary; falsification |
| 6 | Three stress tests | 1½ pages | Question + path per case |
| 7 | Where the oracles run out, and what we are building | 1 page | The 12/12 inert gate as a caught failure; the labelled-calibration instrument; the hardening path per gate; the rejected machinery; register drift n=2; full-pass residuals (no traceability product, transfer claim unsupported, lifecycle gaps) |
| App | Runnable walkthrough | short | Clone, verify, planted failure |

**Tone:** §1–3 for naive readers. Framework operator docs are optional appendix links, not required judge reading.

### Operator note (authors only)

Sync with [self-improving system](../../notes/definitions/self-improving-system.md), [the adaptation loop](../../notes/an-adaptation-loop-requires-search-evaluation-and-retention.md), [warranted autonomy](../../notes/warranted-autonomy-is-bounded-by-oracle-reach.md), [the false-positive asymmetry](../../notes/false-positive-generation-is-filtered-before-retention.md), [actionable methodology](../../notes/definitions/actionable-methodology.md), [the classification](../../reference/commonplace-as-a-reflective-system.md), and [DRM](../../reference/design-rationale-management.md).

**Do not outrun the qualified claims:**

- No "generative material" without "when authors carry it forward"; no "safe reuse" without a worked comparison; no "manages/preserves rationale" — use *surfaces can retain*.
- **Never present our evaluation as verification.** Mechanical checks verify; semantic review is fallible and once was inert. Say which is which every time a number appears — the 14/14 conformance figure must never travel without the calibration caveat.
- **State the oracle position as a program, not a confession.** "Evaluator quality is the binding constraint; it is measurable; here is the instrument and what it has already caught" — never a flat "our oracles are weak," which reads as an apology and throws away the strongest thing we have to say about the assessment layer. Equally, never let the program inflate into a promise: the labelled-regression protocol is **designed, not shipped**, and the one repair is an in-sample separation on four notes, not a detection rate.
- **Never present autonomy as an achievement.** Bare autonomy is free and always available; only warranted autonomy is earned. If the prose sounds proud of a machine doing a job a human used to do, check whether an oracle backs it.
- **Do not say "reflective system" in judge-facing prose.** The term invites a sci-fi reading, and under a human-inclusive boundary it barely discriminates. Prefer the plain mechanism: *the system's own rules are what its validators and agents read, so changing a rule changes what it enforces and what it searches.*
- **Do not say "self-improving" without the human-inclusive qualifier in the same sentence.** A judge will hear "autonomous," which is precisely what we are not claiming.

**§7 must name these limits (not solve them in prose):**

- Semantic evaluation is the binding constraint and is under construction; one shipped criterion was fluent and inert for three days before labelled calibration caught it, and the regression protocol that would prevent a repeat is designed, not shipped
- No enforced lineage from proposals → ADRs → implementations
- Selected-but-unimplemented designs: lifecycle gap (ADR 028 interval not fully governed)
- Epistack casework inspectable in the sibling repo only
- Transferability three-class argument: illustrative, not friction-cleared
- The self-improvement classification rests on one trace

Map evidence to loop stages explicitly when drafting §7:

| Evidence | Loop stage | Oracle strength |
|---|---|---|
| Backlog / proposals / ADRs | Retained rationale | n/a — retention, not evaluation |
| Standing block, local types, quote verifier | Candidate → verify → retain | Strong (mechanical) |
| 127/127 quotes, 14/14 conformance | Verification on shipped corpus | Strong / **weak** — do not merge them |
| Register-drift experiment | Evaluation procedure for the structure layer | Experimental, n=2 |
| Gate calibration (12/12 inert → 3/3 vs 3/3 after repair) | Evaluation *of the evaluator* | The instrument, and the failure it caught |
| Rejected ranking / crux scoring | Recorded rejection | No oracle of known shape **yet** — reopen if one arrives |

## Evaluation boundary

- Submission document outranks everything before 19 July.
- Casework in the sibling repo; framework changes here.
- No new machinery casework has not earned.
- Settled: no scalar credence/authority in frontmatter; adjudication downstream and labelled.
- Do not build bulk-operations or the independent-builder experiment on the critical path.
- Submission prose must stay **inside** the qualified normative notes — if the pitch outruns them, narrow the pitch.

## Build plan

### Done

| Item | Evidence |
|---|---|
| Quote verifier | ADR 046; **127/127** |
| Validation contract, shared runs | ADR 050 |
| Full-pass guard | ADR 051 |
| Three-case rebuild | Sibling workshop — all gates |
| Normative notes | Self-improvement cluster rewritten (2026-07-15); DRM full-pass revised (`81920ed9`, `b02cbc1c`, `28665b55`) |

### Must ship

1. **Submission document** per outline §1–7 — §1–2 and §4 are **new prose**, not edits of the old draft.
2. **Short methodology appendix** — the loop + DRM surfaces + Casebook Protocol conformance checklist (consolidate validation contract, review system, ADRs 038, 041, 046, 051, 052).
3. **Falsification package** — clean pass + planted failure.
4. **Naive-reader pass** + adversarial review.

### Should ship if time allows

- Hands-free transcript (one full loop iteration on a new source).
- §2 sidebar: scaling with AI — better models raise *evaluation strength* and *search reach*, the two independent limits, and the loop absorbs that without redesign. Frame as capacity, never as autonomy earned.

### Cut first

- Correlated-evidence matrix ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- Replication experiment execution.
- ADR laundry lists in main text.

### Rejected — on record

Authority ranking, crux scoring, scalar credence — no oracle of known shape *yet*, so the score would be an unverifiable acceptance with a number on it. The rejection is the discipline, it goes in §7 as content, and it is reopenable the moment an oracle for any of them exists.

## Schedule

| Days | Work |
|---|---|
| Done | Evidence landed; normative cluster rewritten |
| 1 | **Redraft §1–2 and §4** on the new spine — this is the work the cluster rewrite created |
| 2 | **Draft §3, §5–6.** DRM, implementation, case walkthroughs |
| 3 | §7 (negative results), falsification, optional transcript |
| 4 | Integrate, naive-reader pass, buffer |

**Priority if days run out:** submission doc (§1–7) → appendix → walkthroughs → falsification → transcript → matrix.

## Judging questions

| Question | Answer |
|---|---|
| Help reason about the case? | §6 walkthroughs |
| Generalize? | The methodology is the unit — actionable for an agent operator, exercised on three cases; the loop frame plus recorded rationale plus a replication appendix say how far it carries |
| Scale with AI/compute? | **§2:** the methodology stays in executable prose; better models re-run criteria in new partitions and widen search. Scaling raises evaluation *strength* and search *reach* — the two independent limits — and the loop absorbs that without redesign. It does not by itself buy warrant: a stronger judge still needs calibration before we trust it unattended |
| Compound? | **§1–2:** the loop compounds only when an accepted change is **operatively retained** — findable by the next pass and binding on a consumer. Filing it is not enough; a rule nobody retrieves is inert. Hence retrieval machinery (descriptions, enforced index marks) is *epistemic* infrastructure, not housekeeping |
| Why should we trust your assessments? | **Exactly as far as the oracle behind each one reaches — and we tell you which is which.** Mechanical checks verify. Semantic review is fallible: §7 shows a case where ours was fluent and completely inert, how a four-note labelled sample caught it, and the regression protocol that follows. Humans hold the gates the oracles do not yet reach, and the honest claim is that we are moving that line, not that we have erased it |
| What is the open problem? | **Building evaluators you can trust unattended.** Capability is not the bottleneck; verification is. That is the frontier this entry names, instruments, and works on in the open — and it is the question we would most like the field to take seriously |

## What closes it

Submission by 19 July: the methodology (bounded), design rationale management, the epistemic-stack mapping with its oracles, a reference implementation, three-case evidence, and the negative results.

Then: promote durable conclusions; fold predecessor workshops; delete this directory.
