# The assessment layer: what we map, what we decline to score, and why

The brief's assessment desiderata are the most ambitious in the document: identify rhetorical-over-evidential moves, flag correlated evidence treated as independent, find cruxes, surface what's missing, provide calibration frameworks that account for out-of-model error, and distinguish settled from performed-settling.

The Casebook Protocol answers these in a deliberately asymmetric way. It **maps** the assessment-relevant structure — correlation, cruxes, gaps, contested joints — as first-class, checkable artifacts. It **declines to reduce** any of it to a stored score, credence, or authority rank. This document argues that the decline is not a gap but the correct design, states the mechanistic reason, and answers each assessment bullet at the strength the shipped evidence supports.

The one-line thesis: **a knowledge base that stores its own verdict corrupts the map it is supposed to preserve.** The right architecture maps the dispute in neutral, attributed structure and keeps every act of judgment in a separate, attributed, snapshot-anchored layer that reads *from* the map without writing *into* it.

---

## 1. The load-bearing finding: contradictions get silently averaged

The reason the assessment layer is thin-by-design is not modesty. It is a tested result.

When contradictory positions are loaded into a single reasoning context and that context is asked for a bottom line, the contradiction is **silently averaged** — not surfaced, not flagged, blended below the level at which the agent's compliance reasoning would notice. This was found in a register-drift experiment (blind judge, declared confound, n=2 caveat) that set out to confirm the *opposite* assumption and was falsified in an instructive direction; it promoted to the note *context contamination operates below an agent's compliance reasoning*.

The consequence for design is direct. If a casebook stores a `current_answer` or a `confidence: 0.7` in a claim's frontmatter, then every agent that reads that claim inherits a pre-averaged verdict *before* it sees the contradictory evidence — and, per the finding, cannot reliably recover from it by being told to. The stored verdict doesn't summarize the dispute; it pre-empts it. So:

- **No stance scalar on a claim node.** A claim is a neutral proposition. Support and rebuttal are edges, attributed to a party.
- **No stored confidence anywhere.** A credence isn't recomputable from ground truth, so as a cached field it is a stale-trusted-cache trap by our own derived-copy rule: it drifts from the prose that earned it and is believed anyway.
- **Adjudication is a downstream layer.** An assessment artifact *links into* the map and carries its bottom line in attributed prose ("on this evidence, and under these assumptions, I judge…"). It never overwrites a claim node.

This is the mechanistic spine under every "we decline to score" below. The decline is protective.

---

## 2. Correlated evidence treated as independent — mapped as a computed cluster

This is the one assessment bullet the protocol reaches in *shipped, mechanized* form, and it is the layer's strongest single demonstration.

### 2.1 The design move: provenance is uniform even when content is not

Heterogeneous sources cannot be asked the same *content* questions — you cannot put a court filing and a molecular-clock preprint on one claim axis without manufacturing precision that flattens exactly what must be preserved. But every source, whatever its genre, shares **uniform provenance facts**: an author (with institution and funding), a genre, a data dependency, a citation lineage, a capture layer, and a primary/secondary standing.

So the correlated-evidence instrument does **not** aggregate over claims and verdicts. Its rows are *sources* and its axes are *provenance and independence*. Two sources that share authors, share a dataset, share a funder, or sit in a citation chain are **entangled**, and treating them as independent double-counts their weight. That entanglement is computable from provenance metadata the ingestion layer already captures — so the correlated-evidence flag becomes a **computed cluster**, not a prose caveat a reader has to notice and remember.

### 2.2 Where it lands in each case

- **COVID.** The Andersen/Worobey/Pekar author overlap, *and* the multiple analyses reusing the same Huanan-market metagenomic dataset. Six independent Bayesian analyses of the same evidence spanned 23 orders of magnitude — a textbook case where "independent" analyses were entangled through shared inputs and shared decompositions. The cluster makes the entanglement visible instead of leaving it as a footnote.
- **LHC.** The safety case funnels through the cosmic-ray argument as a single load-bearing dependency; Ord–Hillerbrand–Sandberg is literally an out-of-model-error critique of exactly that node. The cluster shows that several reassurances are not independent — they lean on one argument.
- **Eggs.** Industry-funded studies (e.g. Barnard 2019 flags) cluster by funder; the funding entanglement is a provenance fact, computable, not a rhetorical accusation.

### 2.3 The uniform metadata that makes it work — epistemic metadata, already first-class

The brief asks what *supporting epistemic metadata would help assessment methodologies work better.* The reference implementation answers in shipped form:

- **Three distinct kinds of absence.** `not-determinable` (assessed, couldn't tell) ≠ `none` (assessed, verified absent) ≠ blank (not assessed). Most schemes collapse all three — which is precisely how "no evidence of X" quietly becomes "evidence of no X." Keeping them apart turns blanks into a *worklist of what to gather next* (§4, surfacing gaps) rather than false negatives.
- **Evidence tiers gate what may be counted.** A `source-tier` marks whether a finding is grounded in primary material or only in secondary description; low-tier sources are *excluded from aggregation*, not merely annotated. Provenance decides what may be counted, not only what may be read. This is the enforced form of the ingestion ceiling: the matrix cannot aggregate more than capture gathered uniformly.
- **Quote-anchored citations** pinned to immutable snapshots with a write-time grounding check.

### 2.4 Honest status

The provenance-matrix instrument has one fully worked precedent (a 141-subject, 55-column comparative corpus over agent-memory systems, built by parsing review prose) and is being retargeted to epistemic sources as the entry's supporting Assessment demonstration. It is **n→2**, not a general facility. The claim is exactly: *the domain-specific surface is small — one type spec and a config table over generic extraction machinery* — and that claim is measured against a sealed prediction, not asserted. Reading a general capability off a single instance is the error this whole document exists to catch; we do not commit it here.

---

## 3. Cruxes and contested joints — mapped, not scored

A **crux** is the specific factual or inferential disagreement that, if resolved, would most move the overall picture. The protocol represents cruxes structurally and declines to rank them numerically.

- **Representation.** A contested joint is an artifact linked by `contradicts` (a disagreement to resolve) and `contrasts` (neighbouring-but-distinct shapes), with each party's position attributed in prose and the sub-question it bears on made explicit via links to a sub-question map. The crux is *where the edges converge* — the node whose resolution the most `grounds` edges depend on.
- **Why not a crux score.** Ranking cruxes by "impact if resolved" requires a stored model of how much each resolution would move a stored credence — reintroducing exactly the pre-averaged verdict §1 forbids. The map shows *which joints are load-bearing* (how many downstream claims `grounds`-depend on them); which one *you* should prioritize depends on your priors, and the protocol keeps your priors out of the shared artifact.
- **Worked instance.** LHC's cosmic-ray argument is the structural crux: nearly the entire safety case `grounds`-depends on it, and its most speculative assumptions are one hop away. A reader walks to it by following the densest dependency, not by trusting a number someone else computed.

This is crux *mapping* — the durable, shareable, non-flattening part — with crux *scoring* deliberately left to the reader's downstream assessment artifact.

---

## 4. Surfacing what's missing — absence as a worklist

The protocol turns "what's missing" from a judgment call into a computed signal in two ways:

1. **Typed absence (§2.3).** A blank axis is *not assessed* — a discoverable gap — as opposed to `none` (assessed, absent). The set of blanks *is* the collection worklist: the sources not yet captured, the axes not yet answered, the sub-questions with no position attributed.
2. **Structural gaps.** Validation surfaces orphans (artifacts nothing links to) and one-sided contested joints (a `contradicts` with only one party attributed). A sub-question map with a position from party A and none from party B is a visible hole in the discourse structure.

Neither requires an analyst to *notice* the gap. The gap is a property of the artifact graph the tooling reports. This directly serves the brief's "toward further data collection."

---

## 5. Rhetorical-over-evidential weight, and settled-vs-performed settling

These two bullets are the hardest to mechanize and where the protocol is most honest about relying on *archival LLM judgment* rather than deterministic checks.

### 5.1 What the shipped gates already do

- **`confidence-miscalibration`** flags a framework or causal model *asserted* ("the stages are…", "requires…") when it is the note's own construction unsupported by cited evidence, and conversely flags well-grounded findings hedged past their support. Rhetorical weight exceeding evidential weight is often exactly this: assertion language over unsourced construction. The gate names it, per instance.
- **`concept-attribution`** flags prose claiming this artifact's concept *is* a linked source's concept when the source treats it differently — a common move by which a weak claim borrows a strong source's authority. That is a rhetorical-weight-over-evidential-weight detector for the specific case of borrowed identity.
- **`internal-consistency`** and **`grounding-alignment`** check that an artifact's claims cohere and that stated groundings actually support what they're cited for.

### 5.2 Settled vs. performed settling — a first-class distinction the protocol is built to hold

The brief's most sophisticated ask — *distinguish what the debate settled from what it merely performed settling* — maps onto a distinction the review system already enforces:

- A `pass` records that a closed gate *found nothing to flag* — explicitly **not** certification that the artifact is true. A fresh critique means the critique *matches current inputs* — explicitly **not** "critiqued and resolved."
- The protocol refuses to let "reviewed" collapse into "correct," and "captured" collapse into "settled." A heavily-cited, confidently-worded claim with a dense `grounds` subtree is *performing* settledness; whether it *is* settled is a separate judgment recorded in an attributed assessment artifact, under a named model partition, pinned to a snapshot.

The COVID debate is the sharp case: two expert judges ruled *decisively* for zoonosis, yet six Bayesian analyses spanned 23 orders of magnitude. The debate *performed* a resolution the underlying evidence did not *settle*. A casebook represents both facts without contradiction — the adjudication (judges' ruling, attributed) as one assessment artifact, the dispersion (the 23-orders spread, computed as a correlated-evidence + independence finding) as structure — and lets the reader see the gap between them. That gap is the answer to the bullet.

---

## 6. A calibration framework that accounts for out-of-model error

The brief asks for confidence-calibration frameworks that account for out-of-model error, adversarial information environments, and the limits of any single analyst. The protocol's answer is a *discipline*, not a number, and it addresses each of the three named hazards:

- **Out-of-model error.** No stored credence can express "and I might be wrong in a way my model doesn't contain." Attributed prose can, and out-of-model critiques (Ord–Hillerbrand–Sandberg on LHC) are attached as standing `grounds`-level objections to the very nodes they threaten — the out-of-model risk lives *on the map*, next to the argument it undercuts, not buried in a global confidence discount.
- **Adversarial information environments.** Two defenses. First, deterministic quote verification (§ protocol 5.2) means an adversary cannot slip a misquotation past the checker — the citation is mechanically pinned to the snapshot. Second, evidence-tier gating means an adversary cannot inflate a claim's weight by flooding low-fidelity secondary sources; those are excluded from aggregation by provenance, not by an analyst's vigilance.
- **The limits of a single analyst.** Model partitions (§ protocol 6.4) make the judging model an explicit, swappable axis, and decorrelated review — different model families, different criteria — is the built-in check against a single judge's blind spots. The correlated-evidence instrument extends the same logic to *sources*: it detects when apparent independence is illusory. The framework's own convergence discipline (independent builders, sealed predictions) is the same principle applied to structure.

The calibration framework, stated plainly: **do not store a number; attribute every judgment to a source, a model partition, and a snapshot; gate what may be counted by provenance; and keep the out-of-model objection on the map beside the claim it threatens.** Confidence lives where it can carry its own reasons and its own attribution — never as a scalar that outlives the evidence that earned it.

---

## 7. What we refuse to build, on the record

The discipline is legible in the negative. Two structures were designed and rejected, and the rejections belong in the submission:

- **An inquiry "control room" carrying `current_answer` / `confidence` in frontmatter.** Rejected: it fuses verdict into map, inviting the silent-averaging failure of §1. An inquiry root artifact is fine — it holds the question, scope, and hypotheses, and *links to* the assessment; the bottom line stays in the linked, attributed layer.
- **Author-authority ranking (a scalar credibility order over sources).** Rejected because the order's *shape* is unestablished — possibly partial, possibly domain-conditional, non-additive under independence — and six days will not settle it. A half-built scalar rank would hand a reader the exact flattening this layer exists to prevent. Provenance facts (funding, institution, primary/secondary standing) are captured and *attributed*; they are not reduced to a rank.

Declining to build a structure whose shape we have not established is the same restraint we would ask of any assessment methodology. The refusals are the calibration framework applied to our own design.

---

## 8. Summary table — bullet by bullet

| Brief assessment bullet | Protocol response | Status |
|---|---|---|
| Rhetorical > evidential weight | `confidence-miscalibration`, `concept-attribution` gates | Shipped, per-instance judgment |
| Correlated evidence treated as independent | Provenance/independence matrix → computed clusters | One worked precedent; retarget is the entry's supporting demo (n→2) |
| Identify cruxes | Contested-joint mapping via `contradicts`/`contrasts` + dependency density | Mapped, not scored (by design) |
| Surface what's missing | Typed absence as worklist + orphan/one-sided-joint checks | Shipped |
| Calibration under out-of-model error | Attributed judgment + partitions + evidence-tier gating + on-map objections | Discipline, not a number (by design) |
| Settled vs. performed settling | pass≠true, fresh≠resolved; adjudication as separate attributed layer | Enforced boundary |

The through-line: **map the dispute in shared, checkable, neutral structure; keep every verdict in a separate, attributed, snapshot-anchored layer.** Everything the protocol declines to store, it declines because storing it would silently average the very disagreement the casebook exists to preserve.
