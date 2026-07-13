# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, roughly six working days to submission.

Inputs, not competitors: [epistack-competition](../epistack-competition/README.md) (two-repo protocol), [epistack-framework-additions](../epistack-framework-additions/README.md) (design menu). This workshop decides what we submit.

## The pitch

**Constraint-driven design for compounding epistemic investigations: derive stack machinery from explicit constraints, build local-first, promote only what survives heterogeneous cases — with a runnable reference implementation and three stress-test casebooks.**

The brief asks for workflows and methodologies that advance AI-assisted investigations and **compounding** knowledge bases. The hard problem it names is **methodology and workflow design**, not capability alone. Our answer is not "here is a Structure-layer protocol" as the title — it is a **design methodology for the epistemic stack** (ingestion, structure, assessment operating in concert), with the Commonplace Casebook Protocol as one disciplined instantiation that happened to be buildable in six days.

The surprise we intend: most entries will present **a stack**. We present **how to design a stack without smuggling in unmarked verdicts** — including verdicts disguised as metadata, scalar credences, authority rankings, or "neutral" synthesis prose.

### The compounding barrier

Compounding fails when three different things look identical on disk:

| Class | Example |
|---|---|
| **Forced by the world** | You cannot cite more precisely than you captured. |
| **Forced by this problem** | COVID needs an institutional layer because official bodies contradict; LHC needs dependency traversal because the case is mostly settled but hinges on a chain. |
| **Freely chosen** | Whether the grounding-layer marker is a prose word or a frontmatter field. |

Without explicit rationale, history, or transfer evidence, the next investigator cannot tell which parts would survive the trip. **Unmarked design contingency is a barrier to compounding** — and it is the problem constraint-driven design addresses.

### The method (what we submit as methodology)

**Constraint-driven design** — derive tooling from named constraints; refuse structures whose shape is unknown; keep forced, problem-local, and chosen decisions in different homes with different promotion rules.

| Mechanism | Role |
|---|---|
| **Name the constraint** | Forces in proposals; backlog entries record what friction proved what. |
| **Build local-first** | Collection-local types and conventions (`epistack-snapshot`, COVID `standing`) before framework promotion. |
| **Worked-case guard** | A structure earns promotion only after surviving real material — ideally a second, differently-shaped case ([demotion note](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md), [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md)). |
| **Deterministic where ground truth is shared** | Schema, link resolution, verbatim quotes ([validation contract](../../reference/validation-contract.md), [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)). |
| **Semantic where judgment is local** | Collection-conformance, type-conformance, criterion-anchored review — with calibration against labelled samples (gate rationalization finding). |
| **Negative results on the record** | Rejected authority ranking, unbuilt span locator, preregistered replication unrun, quote-verifier proposal written before friction case. |

**Standardize the connective tissue, not the contested substance** — the operational rule that falls out of the constraints, not the thesis itself.

### Applying constraints to the epistemic stack

The brief's ingestion / structure / assessment layers are **outputs of constraint satisfaction**, not a feature checklist. The submission maps each layer this way:

| Layer | Constraint (why) | What we built / refused |
|---|---|---|
| **Ingestion** | Capture bounds citation; provenance must be legible without KB-voice ranking | Retained snapshots, `capture_fidelity`, typed `genre`, COVID `standing` constituents (sibling repo: `kb/notes/standing-is-recorded-by-its-constituents-not-by-a-ranking.md`); **refused** scalar source credibility |
| **Structure** | Contested substance cannot be flattened; verdict in context contaminates downstream maps | Stance-neutral casebooks, verdict/map separation, attributed prose + labelled links; local extension without silent universalization |
| **Assessment** | Shared ground → mechanical check; local judgment → criterion review; some failures are locally defensible | `commonplace-verify-quotes` (127/127 on rebuilt corpus); collection-conformance gates; **refused** crux scoring and authority ranking until shape is known |

Brief bullets we answer **by constraint derivation** (not by omission):

- **Correlated evidence** — independence is not visible from agreement → `standing.independence`, prose clusters in casebooks; optional computed matrix is supporting only ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- **Cruxes** — contested joints and attributed positions *are* crux mapping; we decline crux *scoring* (shape unknown, same constraint that kills ranking).
- **Calibration** — snapshot-anchored, partition-scoped review *is* the calibration framework; register-drift experiment is the mechanistic argument against scalar credences in frontmatter (sibling repo: `kb/notes/a-verdict-in-context-produces-register-drift-not-verdict-copying.md`).

### Reference implementation (evidence, not the spine)

The [Commonplace Casebook Protocol](../epistack-competition/README.md) is the runnable proof that the method can produce inspectable artifacts:

- **Sibling casebooks** (`epistack-casebooks`) — three stress tests, from-scratch rebuild **complete** (2026-07-13): 0 validate failures, **127/127** quote matches, **14/14** collection-conformance PASS, freshness demonstrated. Entry points documented in `kb/work/rebuild-from-scratch/README.md` there.
- **Framework** (this repo) — `commonplace-validate`, `commonplace-verify-quotes`, review freshness ([ADR 052](../../reference/adr/052-general-freshness-store-review-first-migration.md)), skills layer.

Judges who never open a repo should still get the methodology. Judges who clone should get **falsification** (adversarial quote demo below).

### Three cases as constraint stress tests

Cases demonstrate **which constraints bit**, not which side is right:

| Case | Constraint surfaced | One navigational question for the write-up |
|---|---|---|
| **COVID** | Parallel institutional verdicts; correlated zoonotic cluster; scope must not collapse | "Do these three papers independently confirm zoonosis, or one programme thrice?" |
| **LHC** | Settled conclusion with load-bearing dependency chain and speculative joints | "What does the safety case rest on, and where is the argument's own reliability contested?" |
| **Eggs** | Competing syntheses; population/outcome caveats; institutional voices that diverged | "Why did the 2015 guideline reversal not settle the dispute?" |

Same workflow on all three: source → ingest → note → validate → review → freshness. One walkthrough per case in the submission document.

## Generalization — bounded claims

The judges ask: *does it generalize?* Constraint-driven design generalizes as **methodology** (any layer, any stack). Specific machinery generalizes only with evidence:

1. **Observed transfer across three unlike shapes** — LHC-shaped contract transferred to eggs and COVID without amendment; visibly different local structure (institutional layer, dependency map, synthesis dispute). LHC shaped the contract → two observed transfers, not independent replication. Say so plainly.
2. **Principled constraints** — authority is claim-relative; context contamination operates below compliance reasoning; closed enums can lie confidently. These are not "our bug reports"; they are design pressures any agent-operated controversy KB faces.
3. **Spot experiments** — register drift (n=2, confounded); gate calibration (fitted revision on 4 labelled notes). Calibrate claims to sample size.
4. **Designed, unrun replication** — [replication-plan.md](./replication-plan.md): clean-room convergence to separate material-forced from contract-induced structure. Appendix material, not spine. Honest uncertainty is an asset.

## Submission document outline

The deliverable is a **judge-facing document**. Code and repos are evidence. Target structure:

| § | Title | Length | Content |
|---|---|---|---|
| 1 | The compounding barrier | ½ page | Unmarked contingency; why methodology beats feature lists |
| 2 | Constraint-driven design | 1–1½ pages | Three constraint classes; promotion rules; three homes (framework / collection-local / proposal) |
| 3 | Constraints → epistemic stack | 1 page | Table above expanded; built vs refused per layer |
| 4 | Reference implementation | 1 page | Casebook Protocol + Commonplace; deterministic vs semantic boundary; falsification path |
| 5 | Three stress tests | 1½ pages | One question + one path through the map per case |
| 6 | Evidence and limits | 1 page | Rebuild gates, experiments, backlog audit trail, replication protocol, n=2 caveats |
| App | Runnable walkthrough | short | Clone path, commands, planted-failure demo |

**Tone:** lead with §1–2 for the naive reader. ADR numbers and CLI names live in §4–6 and the appendix.

## Evaluation boundary

- **The submission document outranks everything.** No new machinery that casework has not earned before 19 July.
- **Casework stays in the sibling repo.** Framework changes land here.
- **Doctrine constraints are settled:** no stored confidence/authority scalars; adjudication is downstream and labelled; frontmatter semantics stay type-owned.
- **Do not build** the generic bulk-operations layer or the independent-builder experiment on the critical path.
- **Collection-as-artifact freshness** remains deferred ([proposal](../../reference/proposals/collection-as-artifact-freshness.md)); ADR 052 v1 review-pair freshness is sufficient evidence.

## Build plan

### Done (evidence landed)

| Item | Status | Evidence |
|---|---|---|
| Quote verifier | **DONE** | [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md); rebuilt corpus **127/127** |
| Validation contract + shared runs | **DONE** | [validation contract](../../reference/validation-contract.md), [ADR 050](../../reference/adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) |
| Full-pass guard | **DONE** | [ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) |
| Three-case rebuild | **DONE** | Sibling `kb/work/rebuild-from-scratch/README.md` — all closure gates |

### Must ship (critical path)

**Extract the methodology + protocol guide (main artifact).** One submission-facing document (or doc + short spec appendix) containing:

- Constraint-driven design as named methodology (§2–3 above).
- Casebook Protocol as reference implementation: artifact surfaces, local-extension rules, conformance checklist, freshness tiers.

Normative sources to consolidate: [validation-contract.md](../../reference/validation-contract.md) (deterministic half); [README-REVIEW-SYSTEM.md](../../reference/README-REVIEW-SYSTEM.md) + ADRs 038, 041, 051, 052 (semantic + freshness). State three freshness tiers:

| Tier | Mechanism | Status |
|---|---|---|
| Review freshness | DB snapshots, selector, ack, model partitions | Shipped |
| Disposition guarding | Packet captures + `commonplace-guard-full-pass-report` | Shipped, narrow |
| General artifact freshness | Dependency baselines, reverse selection, collection snapshots | Designed; [workshop](../artifact-freshness-and-referential-checks/README.md) |

**Write the submission document** following the outline. Run adversarial review and a **naive-reader pass** (judge may never clone).

**Package judge-facing falsification:**

- Clone casebooks → `commonplace-verify-quotes` + `commonplace-validate` on clean corpus → pass.
- Plant one broken `verbatim` span → fail. Full install is not the demo; this short path is.

### Should ship if time allows

- **Hands-free transcript** — one agent run: source → note → validate → review, unassisted. Weakens the scaling story if missing; cut after matrix, before weakening §5.
- **Scaling-with-AI half-page** — model partitions, criterion re-run, cheap gates, skills — currently under-told.

### Cut first

- **Correlated-evidence matrix build** — prose `standing.independence` and casebook callouts already satisfy the constraint story; matrix is optional ([assessment-machinery-line.md](./assessment-machinery-line.md)).
- **Replication experiment execution** — stays designed-but-unrun.
- **ADR laundry lists** in main text — footnote only.

### Rejected — entry material (negative results)

**Author-authority ranking** — [workshop](../authority-ranking/README.md): order shape unknown. Rejection *is* the discipline. A half-built scalar rank would be the flattening this entry argues against.

**Crux scoring, scalar credence in frontmatter** — same shape-unknown constraint.

## Schedule

Days are working days from 12 July; submission 19 July.

| Days | Work |
|---|---|
| 1 | **DONE.** Quote verifier, validation contract, rebuild closure |
| 1–2 | **Draft §2–3 + protocol appendix.** Methodology spine and constraint→stack table |
| 2–3 | **Draft §4–5.** Reference implementation, three case walkthroughs, results table |
| 3 | **Falsification package + optional transcript** |
| 4–6 | **Integrate, naive-reader pass, adversarial review, buffer** |

**Priority if days run out.** Protect, in order:

1. Submission document (§1–6)
2. Methodology + protocol guide (extracted spec)
3. Three case walkthroughs + rebuild evidence table
4. One-command falsification demo
5. Hands-free transcript
6. Correlated-evidence matrix

Do not weaken §2–5 to build optional Assessment machinery.

## Entry material we already have — do not hide

The audit trail **is** constraint-driven design in action:

- Sibling `backlog-to-commonplace.md` — append-only, Outcome lines for what earned promotion
- `## Forces` / `## Free choices` in proposals
- [rejected-candidates](../epistack-framework-additions/rejected-candidates.md)
- Quote-verifier proposal admitting it "did not originate from a felt friction case" — discipline catching violation on the page
- Register-drift experiment + gate calibration — constraints predicted failure modes; spot checks confirmed
- Rebuild workshop closure — constraints → machinery → measurable gates (127 quotes, 14/14 conformance)

## Judging questions — how we answer

| Question | Answer |
|---|---|
| Would this help someone reason about the case? | §5 walkthroughs; maps are stance-neutral navigation aids, not verdicts |
| Does it generalize? | Methodology generalizes; machinery bounded by three cases + replication protocol |
| Does it scale with AI/compute? | Partitions, re-runnable criteria, agent-operable skills — §4 sidebar |
| Does it compound? | **The spine:** constraint classes + promotion rules make handoffs legible |

## What closes it

Submission sent by 19 July: constraint-driven design methodology, epistemic-stack mapping, reference-implementation walkthrough, three-case evidence, explicit limitations and negative results.

Then: promote durable conclusions into `kb/reference/` and `kb/notes/`; fold predecessor workshops into what survives; delete this directory.