# Workshop: epistack-submission

This workshop is building the entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, it has roughly six working days and closes at submission.

The two existing epistack workshops are inputs, not competitors to this one: [epistack-competition](../epistack-competition/README.md) holds the two-repo protocol (framework here, casework in the sibling `epistack-casebooks`), and [epistack-framework-additions](../epistack-framework-additions/README.md) holds the design menu of candidate additions. Neither decides what we submit. This workshop does.

## The thesis we lead on

**Unmarked design contingency is a neglected barrier to knowledge artifacts compounding. Commonplace makes that contingency legible and stress-tests what transfers, alongside the representational interoperability any shared artifact still needs.**

A wiki gives you unlimited structural freedom but no signal about what any given structure *is*. As a result, three very different things can emerge from a working session looking identical on disk:

- **Forced by the world** — you cannot cite more precisely than you captured. No design choice escapes that constraint.
- **Forced by this problem** — the COVID case needs a split institutional layer because three official bodies contradict one another; the LHC case does not because it has one safety review.
- **Freely chosen** — whether the grounding-layer marker is a prose word or a frontmatter field.

All three arrive as links and headings. Without explicit rationale, history, or an independent transfer case, their surface form does not reveal which parts would survive the trip. The brief names the symptom — "single-user artifacts tuned to one investigator's context, not the kind that travel, combine, or survive scrutiny" — and this thesis names one mechanism beneath it.

Commonplace's actual practice is a discipline for keeping the three apart by giving each a **different home and a different promotion rule**: proposals carry literal `## Forces` and `## Free choices` sections; problem-local structure stays collection-local; transferable structure must *earn* promotion by surviving a second, differently shaped case (build-local-first, upstream-what-survives, worked-case-first). The framework has already applied this discipline to itself: [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) demoted registers from universals to *default profiles*, keeping only the declared contract and answerability as universal ([the demotion note](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md)).

This matches the brief's **protocol** shape — "interoperability and compounding without flattening the underlying material… how to maintain them as sources, users, and AI capabilities change." Marking which structures are inherited, problem-local, or chosen gives a successor evidence about what to preserve or revisit; the entry must still show that this improves useful pickup rather than assume the mark is sufficient.

### The three cases are an instrument, not a demo

They are differently shaped **on purpose**: LHC is one load-bearing dependency chain; COVID is two parallel evidential structures plus a split institutional layer; eggs is dueling syntheses over a single relationship. Reuse and amendment across the three are observable transfer signals, not proof of universality: shared contract effects, operator carryover, vacuous rules, and case selection can also produce convergence. The fixed-contract, independent-builder rebuild below is the pending stress test that separates some of those alternatives by measuring reuse, amendment, and convergence within this sample.

It also gives us the critique the brief invites as an entry shape. Argument graphs can be useful conventional boundary objects without claims of metaphysical necessity. The narrower challenge is whether their chosen semantics are marked as choices, tested against differently shaped work, and revised when a transfer boundary appears. Our rig makes that contingency auditable.

### The supporting case: the assessment pipeline, where we are the ones who cannot tell

**[assessment-machinery-line.md](./assessment-machinery-line.md)** — a *supporting case*, not the lead. It earns that place by being the thesis applied to us.

We built one repeatable assessment pipeline: the `agent-memory-system-review` type, run over **141 code-grounded reviews**, parsed into a **55-column matrix**, yielding quantitative findings and an [ASIS&T position paper](../../sources/where-it-lives-retained-adaptation-2026-06-23.md). It works. It cost one type spec, one skill, and **~755 lines**, because the framework carried types, validation, production, provenance, and freshness.

And **we cannot tell, from inside it, which parts of it are forced and which are ours.** That is the whole thesis, stated about our own tooling. The tempting claim — "Commonplace makes assessment pipelines cheap; look at the matrix" — reads a general capability from a single bespoke instance, exactly the error the thesis indicts. The truth is n=1: ~755 lines shipped without a command, plus a generalization that the [bulk-operations workshop](../bulk-operations/README.md) has *identified but not built* (it already calls this corpus "the existing implicit precedent" and identifies the missing **document-set spec** as an open problem).

The honest claim is therefore narrower and checkable: **the domain-specific surface was small.** To find out what that surface really was, we must build a second instance and see what survives. This *tooling-layer* convergence test runs on the same rig, and the entry preregisters which of the 755 lines it expects to survive before measuring.

**Scope boundary — do not overpromise here.** The generic bulk-operations facility is *planned, large, and not ready*; six days will not build it. The entry's deliverable is the **second instance plus the measured split** and a written statement of what the generic layer would have to contain. That statement feeds the bulk-operations workshop as a requirement, not a shipped abstraction. Claiming the facility would be a second overclaim stacked on the one we just caught. Say plainly: *we ran the transfer test on our own tooling; here is what survived, here is what a general layer would need, and we have not built it.*

Two things fall out of it that the entry needs regardless:

- **The uniform-capture limit.** GitHub gave the 141-review corpus its uniformity for free: the same subject kind, access, and evidence class. The `source-tier` rule excluding doc-grounded reviews from the matrix *is* that precondition, already enforced for reasons predating this competition. Epistemic casework has no `git clone`. More generally, **the assessment layer's ceiling is set at ingestion**: a matrix cannot aggregate more than its capture gathered uniformly, just as a citation cannot assert more fidelity than its capture preserved.
- **The welded token.** `**Axis:** \`value\` — justification` in one line of prose, with the matrix *derived by parsing it*, so no second structured copy exists to drift. This is the concrete mechanism behind "flatten the provenance, not the argument," and the piece most likely to survive transfer.

### Subordinate result: flatten the provenance, not the argument

Schematize and machine-check only what is decidable: whether this quoted span occurs in that snapshot, this link resolves, or this note is stale with respect to the source version it cites. Leave what is not decidable — what supports what, how much, whose reading is right — in constrained prose under a declared `COLLECTION.md` contract, reviewed by snapshot-anchored LLM gates.

This is a **result of the discipline, not the thesis**, and it demonstrates it. We assumed a structured source-span locator type was needed; we built local-first, ran a worked case, and found the binding constraint was capture fidelity — an external limitation — while the locator type was a free choice we had nearly mistaken for a necessity.

### Why not enter on the structure layer

The casebooks' visible content *is* structure: position maps, contested joints, and dependency chains. But structure is where entrants with purpose-built argument graphs will be strongest and most legible. Against those systems, prose notes with a link grammar read as *less* structured rather than more. Entering there invites the one comparison we lose and concedes in advance the very assumption the thesis attacks.

### The evidence

The legacy evidence below already exists. The rebuild and second pipeline instance are preregistered evidence still to be generated; the final entry must keep observed results separate from pending tests.

1. **The contract was usable across three differently-shaped cases without amendment** (sibling backlog, 2026-07-09). This is motivating reuse evidence, not yet a discriminating result: the contract was fitted during the first build.
2. **The `source_type` gap recurred three times before promotion** — the rig's other mode: a structure proved it was not bespoke by recurring across cases and only then earned a place upstream ([ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md)).
3. **The source-span locator was *not* built** — the negative result, and the more valuable one: the discipline stopped a structure that felt necessary and wasn't.
4. **Deterministic provenance verification found real defects in our own corpus** — `scripts/verify_quotes.py` over the 14 casebook notes found 88 candidates: 58 matches, **24 mismatches**, 6 unresolved, and no false mismatches on manual audit ([ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)). This is the crispest single demo we have. The proposal also *admits in writing* that it "did not originate from a felt friction case" — the discipline catching its own violation on the page before the prototype supplied the missing evidence. Do not tidy this away; it is the strongest honesty signal in the entry.
5. **The register-drift experiment** — an assumption ("contradictions get silently averaged") tested and found wrong in an instructive way, with a blind judge, a declared confound, and an n=2 caveat.
6. **Freshness baselines and snapshot pinning** — the literal answer to "how do you maintain them as sources change." Others' compounding stories will be aspirational; ours is running code that predates the competition.

**Promotion done (2026-07-12).** Items 3 and 5 were promoted from sibling casework into [a citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) and [context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md). Both landed under pre-existing framework claims. This is evidence that the concepts were articulated before these cases, not proof that they caused the results.

## Evaluation boundary

- **The deliverable is the submission document.** The code is evidence for it. Nothing else in this workshop outranks getting the document written.
- **Casework stays in the sibling repo**, per the [existing protocol](../epistack-competition/README.md). Framework changes land here. This workshop may direct work in both, but does not relocate either.
- **No new framework machinery that a worked case hasn't earned.** Build-local-first still holds; the deadline is not a licence to ship speculative types.
- **Doctrine constraints are inputs, not open questions:** no stored confidence/authority scalars, adjudication stays a downstream labelled layer, frontmatter semantics stay type-owned.

## Build candidates

Ranked by judge-visible value per day. The plan below commits to the first two and rejects the third; anything else stays out of scope for the deadline.

### Ship the quote verifier (DONE — 2026-07-12)

Shipped as [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md): `commonplace-validate` now resolves every `verbatim`-marked quotation against the source it links (a false claim **fails**), plus `commonplace-verify-quotes` for corpus sweeps. The siting question is settled — it runs as a generic body-content check alongside link health, not a type rule, because the trigger is the citation rather than the note's type.

Baseline on the sibling casebooks: **63 match, 18 mismatch, 6 unresolved** across 87 candidates. The 18 are *deliberately not fixed*: those notes are slated for the from-scratch rebuild, so repairing them is throwaway work. The point of shipping the checker first is that the **rebuild's** citations land machine-checked rather than hand-trusted.

Shipping it surfaced an architectural gap worth naming in the submission. Validation now has two *body-content* checks — link health and verbatim quotes — that are hand-written regex passes with no shared model, no shared severity policy, and no declared owner, against a frontmatter-check class that is fully schema-driven and type-owned. The immediate divergence is fixed (both now share one code-fence primitive, after a fenced example was found being scanned as a live claim), but the class still has no design. Logged to [kb-graph-loader](../kb-graph-loader/README.md).

### Correlated evidence — a requirement of the second pipeline instance

This is the one assessment-layer item in the brief we can reach in the time ("flag correlated evidence being treated as independent"), and every case already contains a textbook instance that is identified but unmapped. Crucially, correlated evidence takes a **different form in each case**:

- **COVID** — Andersen/Worobey/Pekar author overlap, *plus* multiple analyses reusing the same Huanan-market metagenomic dataset. The case contract already flags this hazard; no note maps it. This is also the outstanding COVID depth work, so the two tasks are one.
- **LHC** — the whole safety case funnels through the cosmic-ray argument as a single load-bearing dependency; Ord–Hillerbrand–Sandberg is literally an out-of-model-error critique of exactly that.
- **Eggs** — industry funding (Barnard 2019).

These three forms are sealed requirements for the second assessment-pipeline instance. The authoritative plan is a computed correlation cluster in the provenance matrix, not the earlier bespoke link-grammar-plus-review-gate design. If one representation covers all three, it is a candidate for promotion; if not, report the measured local split. Either result informs the thesis without proving it.

### Author-authority ranking (rejected — and the rejection is entry material)

The [authority-ranking workshop](../authority-ranking/README.md) says the order shape itself is unknown: possibly partial, possibly domain-conditional, non-additive under independence. Six days will not settle that.

The rejection is not merely "no time" — it is **the discipline in the negative** and belongs in the submission as such. We decline to build a structure whose shape we have not established, exactly the restraint we are indicting other approaches for lacking. A half-built scalar rank would hand a judge the precise flattening critique this entry exists to make. Name it in the submission as a documented open problem; the brief explicitly asks entrants to make clear where design choices are uncertain.

### Rebuild the three cases from scratch (committed — this is the experiment)

**[replication-plan.md](./replication-plan.md).** The first build got messy — contract invented in flight, a framework upgrade mid-stream, nearest-fit source types, lifecycle churn — and, more importantly, it *cannot test the thesis*: the contract was co-developed with case 1, so "transferred to cases 2 and 3 without amendment" is a fitted result, not a tested one. One operator, sequential builds, full memory, no independent arm. The headline evidence is consistent with the thesis and equally consistent with its negation.

The rebuild inverts the crucial condition: **the contract is now fixed in advance.** Every amendment the rebuild needs becomes a finding rather than a fitting, and every structure that survives unamended is a genuine transfer result. The instrument measures convergence between builders who never saw one another's work (exclusion, not instruction — our own contamination finding forbids the cheap version). It scores converging (forced) and diverging (chosen) structures against predictions **sealed before the run**.

This is the workshop's most expensive item and the one most likely to embarrass us. That is why it goes first.

## Plan

Days are working days from 12 July; submission 19 July.

| Days | Work |
|---|---|
| 1 | Ship the quote verifier — it must exist *before* the rebuild lands so the rebuild's citations are machine-checked, not hand-trusted. Settle where it lives; run it on the old build to fix the 24/88 baseline |
| 1–3 | **Primary evidence — the rebuild.** Freeze the contract, seal predictions, run clean-room builders ([replication-plan.md](./replication-plan.md)). Mostly agent wall-clock, so it can run in the background while attention goes elsewhere |
| 1–4 | **The supporting case — the second pipeline instance.** Seal the code-split prediction, write the `source-assessment` type spec, retarget the parser, build the provenance matrix over the three cases' sources ([assessment-machinery-line.md](./assessment-machinery-line.md)). *Subsumes* the independence instrument: the correlated-evidence flag becomes a computed cluster, not a bespoke link-grammar addition. **Stops at the measured split** — it does not build the generic facility |
| 5–6 | Score both sealed predictions (rebuild convergence, code split); write the submission; buffer |

**Priority if the days run out.** The rebuild is the thesis's primary evidence and is on the competition's own subject matter, so it wins ties. The second pipeline instance is the supporting case and also delivers the correlated-evidence instrument the brief asks for, so it is not optional either — but it is the one to trim. **Neither may expand into building the generic bulk-operations layer**, which is planned, large, and not ready; the entry reports the requirement and stops.

The document needs two full days and does not exist yet. If the schedule slips, the build shrinks — not the writing, and not the replication. An entry whose central claim was tested and survived, or was tested and qualified, beats one whose central claim was merely asserted more fluently.

## Entry material we already have and should not hide

Under this thesis, the repo's own working record *is the primary evidence* because the discipline is the claim. The sibling repo's `backlog-to-commonplace.md` (append-only, with its Outcome lines showing what earned promotion and what did not), this repo's open workshops, the `## Forces` / `## Free choices` sections in proposals, and [rejected-candidates](../epistack-framework-additions/rejected-candidates.md) are not embarrassments to tidy away before submitting. They are the audit trail showing the boundary between forced and chosen being drawn in real time by people who did not yet know the answer. Cite them prominently, not as an appendix.

## What closes it

The submission is sent by 19 July. Then: extract the durable framework conclusions (whatever the quote-verifier siting decision and the independence instrument turn out to prove) into `kb/reference/` and `kb/notes/`, fold the two predecessor epistack workshops into whatever survives, and delete this directory.
