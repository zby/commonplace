# The Commonplace Casebook Protocol

*A Structure-layer protocol for compounding epistemic investigations without flattening their arguments.*

This is the submission's spine. It specifies a conformance target — a *casebook* — that any tool or team can build against, and names Commonplace as its running reference implementation. The governing rule is one sentence:

> **Standardize the connective tissue, not the contested substance.**

A conforming casebook standardizes source identity, artifact roles, relationship semantics, local contracts, verification, review state, and change semantics. Claims and their justification stay in attributed prose, where differences in framing, scope, and uncertainty remain visible. The protocol makes the *shape* of a dispute machine-navigable and machine-checkable; it never adjudicates the dispute.

---

## 1. Scope

### 1.1 What a casebook is

A casebook is a directory of addressable Markdown artifacts and retained source snapshots that, together, expose for one investigation:

- what was said, by whom, in what source;
- which claims bear on which sub-questions;
- what supports, qualifies, or contradicts what;
- what is settled, what is contested, and what is missing.

A casebook is **not** a verdict. It is the navigable substrate a reader (human or agent) reasons *over*. Adjudication — "what should I believe" — is a separate, downstream, attributed layer that links *into* the casebook and never overwrites it (§4.4).

### 1.2 What this protocol governs, and what it deliberately leaves free

| Governed (standardized) | Free (case-local, in prose) |
|---|---|
| How a source is identified and how faithfully it was captured | What the source *says* |
| The roles an artifact may declare and the contract it obeys | The substance of a claim |
| The vocabulary of relationships between artifacts | Which framing of a caveat is correct |
| Which checks are deterministic vs. which are LLM judgment | Whether a position is *right* |
| How change propagates and what goes stale | The credence a reader should hold |

The right-hand column is the "contested substance." The protocol's discipline is to keep its hands off it. This is what lets two investigators who *disagree about the case* still share, extend, and check each other's casebooks.

### 1.3 Conformance levels

- **Level 0 — Structural.** Every artifact declares a role and obeys a schema; every source resolves to a retained snapshot with a stated capture fidelity; every relationship link resolves and carries a label. Machine-checkable end to end.
- **Level 1 — Referential.** Every verbatim quotation resolves against the snapshot it cites and matches it exactly (§5.2). Level 0 plus dereferencing checks.
- **Level 2 — Reviewed.** Level 1 plus snapshot-anchored semantic review (§6): each artifact carries a freshness baseline for the criteria applied to it, under a named model partition.

A submission may claim any level per artifact; the level is evidence, not decoration. The reference implementation reaches Level 2 on its own corpus and Level 1 across the demonstration casebooks.

---

## 2. Sources and provenance

### 2.1 Source identity resolves to a retained snapshot

Every citation resolves to a **snapshot** — retained source material captured at a known time by a known method — not to a live URL. Live URLs rot, paywall, and edit under you; a contested question cannot rest on evidence that changes when no one is looking. The snapshot is the immutable referent; the URL is metadata about where it came from.

Required snapshot metadata:

- `source` — canonical origin (URL, DOI, filing number, archive id);
- `captured` — capture date;
- `capture` — capture method (`web-fetch`, `pdf-download`, `api`, `manual-transcript`, …), which bounds the *fidelity* of everything downstream;
- `genre` — a single open field naming the source kind (`preprint`, `court-filing`, `official-statement`, `essay`, `thread`, `intelligence-assessment`, …). Open, not enumerated: contested domains span genres no fixed list anticipates (ADR 045).

### 2.2 Capture fidelity is a ceiling, and it is declared

**A citation cannot assert more fidelity than its capture preserved.** A claim sourced to a screenshot of a screenshot is not the same evidence as a claim sourced to the published PDF, and the casebook must not let the difference silently disappear. The `capture` field records the method; the evidence-tier discipline (§6.4) uses it to decide what a downstream aggregation is *allowed to count*, not merely what a reader may see.

This is the protocol's honest floor: **the assessment layer's ceiling is set at ingestion.** What capture failed to preserve, no downstream analysis can recover.

---

## 3. Artifacts and local contracts

### 3.1 Every artifact declares a role (`type`)

Each Markdown artifact names a `type` — a path to a type specification that fixes its required frontmatter, required sections, and authoring contract. Types are the machine-checkable grammar of *what kind of thing this is*: a captured snapshot, a source analysis, a claim note, a sub-question map, an assessment, an index.

Types are schema-validated (§5.1). A note that claims to be a structured argument but has no reasoning section fails validation — the role is a promise the artifact must keep.

### 3.2 Collections declare a local contract (`COLLECTION.md`)

A **collection** is a subtree whose root holds a `COLLECTION.md`: the local authoring-and-routing contract for everything beneath it. It declares the collection's quality goal, its title/description conventions, its attribution requirements, and — critically — its **outbound link grammar** (§4.2).

This is where case-specific structure lives without becoming universal. COVID's split institutional layer, LHC's single dependency chain, and eggs' competing population-stratified syntheses are three *different* local contracts over one protocol. The framework does not know or care that COVID has three contradicting official bodies; COVID's `COLLECTION.md` does.

### 3.3 Non-flattening local extension

A casebook may introduce structure the protocol does not supply — a case-local artifact type, a case-local link label, a contract addendum — **as a visible local artifact**, never as silent convention smuggled into prose. Local structure stays local until it *earns* promotion by surviving a second, differently-shaped case (§7.3).

This is the protocol's answer to the interoperability-vs-nuance tension: interoperability is enforced on the *connective tissue* (roles, links, sources, checks), which is shared; nuance is preserved by letting the *substance* extend locally, which is not forced into a global ontology.

---

## 4. Relationship grammar

### 4.1 Links are authored reader-aids, not graph decoration

A link answers one question for a reader already inside the source artifact: *why might following this help me?* Every link carries a **label** naming a reader-need, and every link must pass the articulation test:

> `[source] connects to [target] because [specific reason].`

A relationship that cannot complete that sentence is not a link. This keeps the graph legible — every edge means something a reader can act on — and keeps it honest: the author had to *name* the relationship, so a contested "supports" cannot masquerade as a neutral "see also."

### 4.2 The label vocabulary is collection-owned

The protocol ships a label catalogue (a palette), but the authoritative vocabulary for any link is the *source* collection's `COLLECTION.md`, organized per destination collection. Each pairing declares which labels are authorized and when an agent should go looking for such links.

Labels relevant to epistemic discourse structure:

| label | reader-need it serves |
|---|---|
| `grounds` | wants to verify the premise / check the basis |
| `contradicts` | wants to resolve a disagreement (symmetric) |
| `contrasts` | wants the neighbouring-but-distinct-shape distinction |
| `extends` | wants the argument developed further |
| `mechanism` | wants to understand how the claim operates |
| `exemplifies` | wants the general claim this instance falls under |
| `correlated-with` / `independent-of` | needs to know whether two pieces of evidence are entangled (the independence-clustering primitive, §7 of the assessment layer) |

Discourse structure — who is addressing which sub-question, and where emphases differ — is represented by linking claim and position artifacts to sub-question map artifacts, with party attribution carried on the *edge* or in the attributed prose, never as a scalar stance field on a claim node (§4.4).

### 4.3 "Similar but not identical" is a first-class relationship

The brief asks for claims that are *similar but not identical* — different framings of a caveat, different uncertainty estimates for the same proposition. The protocol represents these with `contrasts` (neighbouring shape) rather than collapsing them, and the `concept-attribution` review gate (§6.3) actively flags prose that asserts two such claims are *the same* when the linked artifacts treat them differently. Non-collapse is not left to author discipline; it is checked.

### 4.4 Verdict/map separation is structural

Two rules, both load-bearing, both enforced by keeping them out of the schema rather than in it:

1. **No stance scalar on a claim node.** A claim artifact is a neutral proposition. `polarity: supports`, `status: disputed`, `confidence: 0.7` are prohibited *on the claim* — they smuggle a verdict into the map. Support and rebuttal live on attributed edges; a party's position lives in that party's attributed prose.
2. **No stored confidence cache anywhere.** A credence is not recomputable from ground truth, so as a frontmatter field it is a stale-trusted-cache trap: it will drift from the prose that earned it and be believed anyway. Confidence is *attributed and in prose* ("the WHO report states…", "Andersen et al. estimate…"), or it is derived-and-checked, or it is absent.

The mechanistic reason is a tested finding, not a preference: contradictions loaded into a single context get **silently averaged** below an agent's compliance reasoning (see the assessment-layer document). A map that stores its own bottom-line invites exactly that averaging on every read.

---

## 5. Deterministic verification

The protocol draws a hard line between what a machine can decide and what needs judgment. Deterministic checks *fail the build*; semantic checks (§6) *record judgments*.

### 5.1 Schema and structural checks

`commonplace-validate` enforces, deterministically: frontmatter validity against each artifact's type schema; required sections present; declared links resolve to existing artifacts; dates well-formed; batch signals (orphans, broken indexes). A false structural claim — a note asserting a type it does not satisfy, a link to a file that does not exist — is a hard failure.

### 5.2 Referential checks: the dereferencing frontier

The sharper line is not frontmatter-vs-body. The schema already checks body headings, links, and dates. The line is **dereferencing**: whether a check must *follow a path and look inside the artifact it names*.

- **Link health** — the cited artifact exists.
- **Verbatim-quote resolution** — a `verbatim`-marked quotation is fetched from the snapshot it cites and compared exactly. A mismatch **fails** (ADR 046). This is claim-level provenance for the claims that carry the most adversarial weight: the ones in quotation marks.

`commonplace-verify-quotes` runs this as a corpus sweep. It is the protocol's cheapest and most falsifiable adversarial guarantee: *a conforming casebook's quotations pass its own checker, and a judge can re-run the checker to confirm it.* (The demonstration document walks the one-command version.)

### 5.3 The honest architectural gap

Referential checks are a distinct class — ground truth in a *second* artifact — and the reference implementation names, in writing, that this class does not yet have a unified design (no shared severity model, no single owner). The protocol specifies the *class* and two members of it; a general referential-check engine is identified future work, not claimed as shipped. Naming the boundary is part of conformance.

---

## 6. Semantic review and change semantics

Deterministic checks cannot decide whether a claim is well-grounded, whether an argument is internally consistent, or whether a caveat is miscalibrated. Those are LLM judgments — and the protocol's contribution is to make them **archival**: pinned, partitioned, and freshness-tracked, rather than one-shot "the model said X."

### 6.1 Assays are snapshot-anchored

An **assay** is any LLM evaluation run through the pipeline `select → job → worker → finalize`. When an assay completes, the system stores DB-owned snapshots of *the exact artifact text* and *the exact criterion text* that produced the judgment. That pinned pair is a **freshness baseline**.

### 6.2 Freshness is computed, not remembered

Staleness is decided by comparing current file text against the stored baseline snapshots — independent of Git history. For each `(artifact, criterion, model-partition)` key:

- no baseline → `missing-baseline`;
- baseline criterion text ≠ current criterion → `criterion-changed`;
- baseline artifact text ≠ current artifact → `note-changed` (with a diff the reviewer can inspect);
- otherwise → **fresh**.

This directly answers *track how the structure evolves over time*: edit a source, and every judgment that depended on it goes visibly stale, with a diff, discoverable by any agent — no one has to remember what a change touched.

### 6.3 Two result kinds: closed gates and open critique

- A **gate** is a closed-ended criterion producing a `verdict`: `pass`, `warn`, or `fail`. Gates relevant to epistemic quality include `confidence-miscalibration` (speculation asserted as established, or findings hedged past their evidence), `concept-attribution` (a claim that X *is* the linked note's Y when the target treats Y differently), `internal-consistency`, and `grounding-alignment`.
- A **critique** is an open-ended criterion producing a `report` — a sampled space of findings, completing *without* a verdict, because "what is weak here" is not a pass/fail question.

Type-conformance and collection-conformance are themselves virtual gates: the type spec *is* the criterion, the `COLLECTION.md` contract *is* the criterion. Editing a contract stales exactly the artifacts it governs.

### 6.4 Model partitions: assessment survives capability change

Every review is partitioned by model. A judgment under `claude-opus` does not satisfy freshness under `codex`. A better model does not invalidate the archive — it opens a new partition over the same criteria, and the old and new partitions can be compared. This is the protocol's answer to *does it scale with improvements to AI*: the criteria and snapshots are durable; the model that judged them is a labelled, swappable axis.

### 6.5 What review does and does not mean

A `pass` records that a closed gate found nothing to flag — not that the artifact is true or certified. A fresh critique means the critique matches current inputs — not "critiqued and fixed." Freshness is *evidence pinned to snapshots*, never endorsement. The protocol is scrupulous about this boundary because conflating "reviewed" with "correct" is exactly the false settling the brief asks entrants to detect.

---

## 7. Compounding: how casebooks build on each other

### 7.1 Handoff is freshness-driven

Another investigator picks up where one left off by asking the system what is stale: `commonplace-review-target-selector` lists every `(artifact, criterion)` pair that is unreviewed or stale and *why*, with diffs. There is no "read the whole thing to find out what changed" step. The work-list is computed.

### 7.2 Casework and framework exchange through one channel

The reference implementation separates *casework* (the sibling `epistack-casebooks` repo — application-specific, one namespace per case) from *framework* (this repo — the reusable protocol machinery). A single append-only backlog moves needs one direction: casework builds a local version of any missing primitive first, proves it on a worked case, and logs the upstream need. The framework promotes *only what survived contact with a case*. This is the compounding mechanism made concrete — and auditable, because the backlog's outcome lines record what earned promotion and what didn't.

### 7.3 Promotion earns its way; contingency is marked

Three things emerge from a working session looking identical on disk — structure *forced by the world*, structure *forced by this problem*, and structure *freely chosen* — and their surface form doesn't reveal which is which. The protocol keeps them apart by giving each a different home and a different promotion rule: problem-local structure stays collection-local; transferable structure must survive a second differently-shaped case; design proposals carry literal `## Forces` and `## Free choices` sections. The framework has applied this to itself (ADR 042 demoted "registers" from universals to default profiles). Marked contingency is what lets a *different* team trust which parts of your casebook will survive the trip to their case.

---

## 8. Conformance checklist

A casebook conforms at the stated level when:

**Level 0 — Structural**
- [ ] Every artifact declares a `type` resolving to a type spec, and passes `commonplace-validate`.
- [ ] Every collection root has a `COLLECTION.md` declaring quality goal, conventions, and outbound link grammar.
- [ ] Every source citation resolves to a retained snapshot carrying `source`, `captured`, `capture`, and `genre`.
- [ ] Every relationship link resolves and carries a label authorized by the source collection's contract.
- [ ] No claim artifact carries a stance scalar; no artifact caches a confidence value.

**Level 1 — Referential** (Level 0 plus)
- [ ] Every `verbatim`-marked quotation resolves against its snapshot and matches exactly (`commonplace-verify-quotes` clean).

**Level 2 — Reviewed** (Level 1 plus)
- [ ] Each artifact carries a freshness baseline for its applicable gates and (where used) collection/type-conformance criteria, under a named model partition.
- [ ] No stale-but-unmarked judgments: the selector reports no unexpected `criterion-changed` / `note-changed` for the claimed scope.

**Discipline (all levels)**
- [ ] Any case-local extension exists as a visible local artifact, not silent prose convention.
- [ ] Design proposals mark forced vs. free choices; rejected structures are kept on record with reasons.

---

## 9. Worked path — the same workflow on each case

The identical pipeline runs on all three cases; only the *substance* differs. Each row is `capture → analyze → connect → structure → verify → review`, ending at one reader question the resulting structure makes easier to answer.

### 9.1 COVID — parallel evidential structures that must not collapse

- **Capture** snapshots across genres: the debate transcript, the Andersen "Proximal Origin" paper, the Worobey/Pekar spatial and molecular-clock analyses, the WHO report, an intelligence assessment, court/FOIA filings. Each carries its own `genre` and `capture` fidelity.
- **Structure** two parallel evidential lines (zoonotic-market vs. lab-leak) as distinct sub-question maps, plus a *split* institutional layer because three official bodies disagree — a case-local structure declared in COVID's `COLLECTION.md`, not a framework universal.
- **Verify** every quoted claim against its snapshot; the Wilf–Miller debate is quotation-dense and is where `verify-quotes` earns its keep.
- **Review** for `confidence-miscalibration` (a speculative reconstruction asserted as established) and `concept-attribution` (two analyses' "the same market cluster" that aren't).
- **Reader question made easier:** *Which pieces of the zoonosis case are evidentially independent, and which reuse the same Huanan-market metagenomic dataset or the same author cluster?* — answered as a computed correlated-evidence cluster (assessment layer), not a prose aside.

### 9.2 LHC — a settled conclusion whose dependency chain stays traversable

- **Capture** the CERN safety report (LSAG), the Giddings–Mangano analysis, the cosmic-ray argument, and the Ord–Hillerbrand–Sandberg out-of-model-error critique.
- **Structure** the safety case as a single load-bearing dependency chain funnelling through the cosmic-ray argument, with the speculative joints (Hawking-radiation assumptions, exotic stable-remnant scenarios) linked as `contrasts`/`grounds` so a reader can walk to the weakest link.
- **Verify** quotations; **review** for miscalibration on the speculative joints specifically.
- **Reader question made easier:** *What single assumption, if it failed, would most reopen this "closed" case?* — answered by walking the dependency chain to its most speculative `grounds` edge, where Ord–Hillerbrand–Sandberg is attached as the standing out-of-model critique.

### 9.3 Eggs — competing syntheses that must not be silently averaged

- **Capture** cohort studies, meta-analyses, and guideline documents across populations (general, diabetic), outcomes (CVD, mortality), and exposures (consumption levels), plus the industry-funding disclosures.
- **Structure** competing syntheses as `contrasts`-linked artifacts stratified by population/outcome/exposure — the whole point is that "eggs are fine" and "eggs raise risk" are *both* true under different scopes, and collapsing them is the failure.
- **Verify** quotations; **review** for `confidence-miscalibration` where a single-population finding is stated as a universal.
- **Reader question made easier:** *For my sub-population and outcome, which findings actually apply, and is the disagreement about the evidence or about the scope?* — answered by the stratified contrast structure plus a funding-correlation cluster flagging the Barnard-2019-style entanglement.

---

## 10. Stated limitations

The protocol is transparent about its edges, because a conformance target that hides its gaps cannot be trusted to check anyone else's:

- **Granularity is artifact-level, not claim-level, by default.** Sources are cited at the snapshot; individual claims are not each addressable nodes. Verbatim-quote verification is the claim-level exception, applied where it matters most. Finer granularity (a source-span locator) was considered and *not* built — it did not survive a felt-friction case.
- **The assessment layer is thin, on purpose.** The protocol maps cruxes, correlated evidence, and contested joints; it declines to *score* them, because stored scores are the flattening it exists to prevent. What it offers instead is attributed, partition-scoped, snapshot-anchored judgment — a calibration *discipline*, argued in the assessment-layer document, not a calibration number.
- **Generalization is demonstrated across three supplied cases, not proven universal.** The contract was co-developed with the first case. A clean-room convergence experiment that *would* separate forced from chosen structure is designed, preregistered, and unrun (see `replication-plan.md`); it is published as future evaluation with sealed predictions, not narrated as a result.
- **"Close to single click" applies to reading and checking, not to full install.** The adversarial demo (clone, run the checker, watch a broken citation fail) is one command; standing up your own casebook is a real setup.

The protocol is offered as a shared target others can build against and check against — deterministic where a machine can decide, judgment-based but archival where it cannot, and silent about the substance throughout.
