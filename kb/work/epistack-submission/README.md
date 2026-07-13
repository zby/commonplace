# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, roughly six working days to submission.

Inputs, not competitors: [epistack-competition](../epistack-competition/README.md) (two-repo protocol), [epistack-framework-additions](../epistack-framework-additions/README.md) (design menu). This workshop decides what we submit.

Normative spine (still revising): [design-rationale-management.md](../../reference/design-rationale-management.md).

## The pitch

**Design rationale management for compounding epistemic investigations: preserve why each commitment exists — constraints, alternatives, evidence, and transfer — across the epistemic stack, with a runnable reference implementation and three stress-test casebooks.**

The brief asks for workflows and methodologies that advance AI-assisted investigations and **compounding** knowledge bases. The hard problem it names is **methodology and workflow design**, not capability alone. Our answer is not a feature tour of one layer — it is an established design discipline applied to knowledge infrastructure that must evolve under agents: **design rationale management** ([MIT Design Rationale](https://rationale.csail.mit.edu/); [Feature, specification and evidence framework](https://doi.org/10.1017/dsj.2024.19); [Design Space Analysis](https://europe.naverlabs.com/history/past-research/design-space-analysis/)). The Commonplace Casebook Protocol is one worked instantiation buildable in six days.

The surprise we intend: most entries will present **a stack**. We present **how to build and hand off a stack when design choices look identical on disk but carry different authority** — and how to refuse commitments whose shape is unknown (scalar credence, authority ranking, crux scoring) until rationale and evidence support them.

### The compounding barrier (judge-facing)

Compounding fails when later readers cannot recover **why** a design looks the way it does — what was forced, what this problem required, what was freely chosen, and what was rejected:

| Class | Example |
|---|---|
| **Forced by the world** | You cannot cite more precisely than you captured. |
| **Forced by this problem** | COVID needs an institutional layer; LHC needs dependency traversal. |
| **Freely chosen** | Grounding-layer marker as prose word vs frontmatter field — either works; the pick must be recorded with alternatives. |

Without surfaces that preserve this, the next investigator treats every link and heading as equally authoritative. **Unmarked design contingency is a barrier to compounding.** Design rationale management — an established discipline, not a coinage — is the response. IDEF9/IDEF6 split is the accessible hook: discover what bounds the decision; record rationale when the bounds still leave more than one feasible option ([IDEF compendium](https://www.idef.com/wp-content/uploads/2016/02/compendium.pdf)).

### The method (what we submit)

**Design rationale management for evolving knowledge infrastructure** — discover constraints, record rationale and alternatives, test on worked cases, promote shared machinery only after evidence warrants it, enforce mechanically only where ground truth is shared.

| Mechanism | Commonplace surface | Role |
|---|---|---|
| **Active exploration** | `kb/work/` | Experiments, competing framings, provisional decisions |
| **Finished but undecided** | `kb/reference/proposals/` | Questions–options–criteria: forces, free choices, adoption criteria |
| **Implemented decision** | ADRs | Context, decision, consequences, supersession |
| **Local operating contract** | `COLLECTION.md`, collection-local types | Problem-local constraints without framework claim |
| **Shared commitment** | Global types, validators, package code | Promotion after scope and enforcement are clear |
| **Rejected / displaced** | Rejected options, backlog Outcomes, git history | Why an alternative was not selected |

Epistack-specific practice on top (not a separate method): sibling `backlog-to-commonplace.md` (append-only + Outcome lines); build-local-first; worked-case guard before framework promotion ([demotion note](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md), [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md)).

**Standardize the connective tissue, not the contested substance** — a design commitment that falls out of the constraints on controversy maps, recorded in rationale rather than asserted as taste.

### Applying rationale to the epistemic stack

The brief's ingestion / structure / assessment layers are **design outcomes whose rationale must be recoverable**, not a feature checklist:

| Layer | What bounds the design | What we built / refused (with rationale on record) |
|---|---|---|
| **Ingestion** | Capture bounds citation; provenance legible without the KB ranking sources | Snapshots, capture fidelity, typed genres, standing constituents (sibling note on standing); **rejected** scalar source credibility |
| **Structure** | Contested substance cannot be flattened; verdict in context contaminates downstream maps | Stance-neutral casebooks, verdict/map separation; register-drift experiment as evidence for the separation |
| **Assessment** | Shared ground → mechanical check; local judgment → documented criteria | Quote verification (127/127); collection-conformance + calibration; **rejected** crux scoring and authority ranking until shape is known |

Brief bullets answered **by recorded rationale** (not by omission):

- **Correlated evidence** — rationale: independence not visible from agreement → `standing.independence`, casebook prose; optional matrix supporting only ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- **Cruxes** — contested joints *are* crux mapping; crux *scoring* declined with written rationale (shape unknown).
- **Calibration** — partition-scoped review as calibration framework; register drift as rationale against scalar credences (sibling: `kb/notes/a-verdict-in-context-produces-register-drift-not-verdict-copying.md`).

### Reference implementation (evidence, not the spine)

The [Commonplace Casebook Protocol](../epistack-competition/README.md) shows the repository surfaces producing inspectable artifacts:

- **Sibling casebooks** — three stress tests; rebuild **complete** (2026-07-13): 0 validate failures, **127/127** quotes, **14/14** conformance PASS, freshness demonstrated (`kb/work/rebuild-from-scratch/README.md` there).
- **Framework** (this repo) — validators, review freshness ([ADR 052](../../reference/adr/052-general-freshness-store-review-first-migration.md)), skills — each with ADR/proposal/backlog rationale where promoted.

Judges who never clone still get the methodology. Judges who clone get **falsification** (quote demo below).

### Three cases as rationale stress tests

Cases show **which constraints and rationale commitments bit**, not which side is right:

| Case | Constraint / rationale surfaced | One navigational question |
|---|---|---|
| **COVID** | Institutional incommensurability; correlated cluster | "Do these three papers independently confirm zoonosis, or one programme thrice?" |
| **LHC** | Dependency chain; argument-reliability as contested sub-question | "What does the safety case rest on, and where is the argument's own reliability contested?" |
| **Eggs** | Competing syntheses; institutional divergence | "Why did the 2015 guideline reversal not settle the dispute?" |

Workflow on all three: source → ingest → note → validate → review → freshness. One walkthrough per case.

## Generalization — bounded claims

*Does it generalize?*

1. **The methodology** — design rationale management is established research applied to agent-operated knowledge infrastructure.
2. **The machinery** — three unlike case shapes + observed contract transfer (LHC-shaped → eggs, COVID); not independent replication. Say so plainly.
3. **Principled pressures** — claim-relative authority, context contamination below explicit compliance, type systems that assert false precision: recorded as rationale, not dismissed as implementation bugs.
4. **Spot experiments** — register drift (n=2); gate calibration (fitted on 4 labelled notes). Size claims to evidence.
5. **Designed, unrun replication** — [replication-plan.md](./replication-plan.md): convergence test for forced vs chosen structure. Appendix, not spine.

## Submission document outline

Judge-facing document; code and repos are evidence.

| § | Title | Length | Content |
|---|---|---|---|
| 1 | The compounding barrier | ½ page | Unmarked contingency; why rationale beats feature lists |
| 2 | Design rationale management | 1–1½ pages | Established lineage (DR/DSA/IDEF); three-class compounding barrier; repository surfaces in plain language |
| 3 | Rationale → epistemic stack | 1 page | Layer table; built vs rejected with alternatives named |
| 4 | Reference implementation | 1 page | Casebook Protocol + Commonplace; deterministic vs semantic boundary; falsification |
| 5 | Three stress tests | 1½ pages | One question + path per case |
| 6 | Evidence and limits | 1 page | Rebuild gates, experiments, backlog/ADR audit trail, replication protocol |
| App | Runnable walkthrough | short | Clone, verify-quotes, planted failure |

**Tone:** §1–2 for naive readers — no Commonplace internal vocabulary (see operator note below). ADR/CLI detail in §4–6. Optional footnote or appendix link to [design-rationale-management.md](../../reference/design-rationale-management.md) for framework operators, not required reading for judges.

### Operator note (authors only — not submission spine)

When syncing with [design-rationale-management.md](../../reference/design-rationale-management.md): Commonplace distinguishes **design constraints**, **design rationale**, and technical **constraining** (deploy-time interpretation narrowing). That boundary matters for framework docs and must not appear in the judge-facing submission — judges have no reason to learn our learning-theory vocabulary. Translate to plain language: *what bounded the choice, what was recorded, what was enforced mechanically, what stayed provisional.*

## Evaluation boundary

- **Submission document outranks everything.** No new machinery casework has not earned before 19 July.
- **Casework stays in sibling repo.** Framework changes land here.
- **Settled design commitments:** no scalar confidence/authority in frontmatter; adjudication downstream and labelled; frontmatter semantics type-owned.
- **Do not build** bulk-operations layer or independent-builder experiment on critical path.
- **Collection-as-artifact freshness** deferred; ADR 052 v1 sufficient ([proposal](../../reference/proposals/collection-as-artifact-freshness.md)).
- **Sync with DRM doc:** as `design-rationale-management.md` revises, align operator notes and §2 plain-language framing; keep internal vocabulary out of the submission document.

## Build plan

### Done (evidence landed)

| Item | Status | Evidence |
|---|---|---|
| Quote verifier | **DONE** | [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md); **127/127** |
| Validation contract + shared runs | **DONE** | [validation contract](../../reference/validation-contract.md), [ADR 050](../../reference/adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) |
| Full-pass guard | **DONE** | [ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) |
| Three-case rebuild | **DONE** | Sibling rebuild workshop — all closure gates |
| DRM reference doc | **in progress** | [design-rationale-management.md](../../reference/design-rationale-management.md) |

### Must ship (critical path)

**Extract submission-facing methodology + protocol guide:**

- Design rationale management as §2 spine (established research + three-class barrier + repository surfaces — plain language).
- Casebook Protocol appendix: surfaces, local-extension rules, conformance checklist, freshness tiers.

Consolidate from: [design-rationale-management.md](../../reference/design-rationale-management.md), [validation-contract.md](../../reference/validation-contract.md), [README-REVIEW-SYSTEM.md](../../reference/README-REVIEW-SYSTEM.md), ADRs 038, 041, 046, 051, 052.

Freshness tiers:

| Tier | Mechanism | Status |
|---|---|---|
| Review freshness | DB snapshots, selector, ack, model partitions | Shipped |
| Disposition guarding | Packet captures + `commonplace-guard-full-pass-report` | Shipped, narrow |
| General artifact freshness | Dependency baselines, reverse selection, collection snapshots | Designed; [workshop](../artifact-freshness-and-referential-checks/README.md) |

**Write submission document** per outline. Naive-reader pass + adversarial review.

**Falsification package:** clean corpus passes `commonplace-verify-quotes` / `commonplace-validate`; planted `verbatim` break fails.

### Should ship if time allows

- Hands-free transcript (source → note → validate → review).
- Scaling-with-AI half-page (partitions, criterion re-run, skills).

### Cut first

- Correlated-evidence matrix build ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- Replication experiment execution.
- ADR laundry lists in main text.

### Rejected — rationale on record (negative results)

**Author-authority ranking** — shape unknown; rejection is the discipline ([workshop](../authority-ranking/README.md)).

**Crux scoring, scalar credence** — same undetermined-shape rationale.

## Schedule

| Days | Work |
|---|---|
| 1 | **DONE.** Quote verifier, validation contract, rebuild closure |
| 1–2 | **Draft §2–3 + DRM sync.** Methodology spine, stack table; plain language only in submission prose |
| 2–3 | **Draft §4–5.** Reference implementation, case walkthroughs |
| 3 | **Falsification + optional transcript** |
| 4–6 | **Integrate, naive-reader pass, buffer** |

**Priority if days run out:** submission doc → methodology extract (DRM-centered) → case walkthroughs → falsification demo → transcript → matrix.

## Entry material — the audit trail is the method

Distributed rationale surfaces already populated:

- Sibling `backlog-to-commonplace.md` — friction → local build → Outcome
- Proposals: `## Forces` / `## Free choices`
- ADRs, rejected candidates, supersession links
- Quote-verifier proposal written before friction case — rationale catching its own violation
- Register-drift + gate calibration — predicted failure mode; rationale revised; mechanical enforcement added where ground truth was shared (quote verifier, revised review criteria)
- Rebuild closure — rationale → commitments → measurable gates

## Judging questions

| Question | Answer |
|---|---|
| Would this help someone reason about the case? | §5 walkthroughs; maps navigate contestation |
| Does it generalize? | Established DRM methodology + bounded machinery claims + replication protocol |
| Scales with AI/compute? | Partitions, re-runnable criteria, skills — §4 sidebar |
| Does it compound? | **Spine:** recoverable rationale across repository surfaces and handoffs |

## What closes it

Submission by 19 July: design rationale management methodology (judge-facing plain language), epistemic-stack mapping, reference-implementation walkthrough, three-case evidence, limitations and negative results.

Then: promote durable conclusions; fold predecessor workshops; delete this directory when done.