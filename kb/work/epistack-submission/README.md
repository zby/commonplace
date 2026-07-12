# Workshop: epistack-submission

Building the actual entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, so this workshop has roughly six working days and closes at submission.

The two existing epistack workshops are inputs, not competitors to this one: [epistack-competition](../epistack-competition/README.md) holds the two-repo protocol (framework here, casework in the sibling `epistack-casebooks`), and [epistack-framework-additions](../epistack-framework-additions/README.md) holds the design menu of candidate additions. Neither one decides what we submit. This workshop does.

## The lead: Commonplace makes a repeatable assessment instrument cheap to stand up

**[assessment-machinery-line.md](./assessment-machinery-line.md) — read this first; it now leads the submission.** You *declare* the methodology as a type; the framework supplies validation, production, provenance rules, freshness, and aggregation. The existence proof is not the casebooks — it is the **141 code-grounded agent-memory-system reviews**, parsed into a 55-column matrix, yielding quantitative findings and an ASIS&T position paper. Nobody wrote an application to get that; someone wrote a type spec and a skill.

This reframes what looked like our weakness. We said the epistemology tools can be built in Commonplace but aren't ready-made, and there are only six days. The right answer is that **ready-made is the wrong ask** — the bottleneck was never the shortage of assessment methodologies, it is that each one needs an apparatus before it can be applied repeatably and compared. Commonplace *is* the apparatus. So the six days become the demonstration, not the excuse.

Its honest limit is also its sharpest finding: **the method works where data can be gathered uniformly.** GitHub handed the 141-corpus that uniformity for free. Epistemic casework has no `git clone`. So the retarget aggregates over **provenance** (author, funding, genre, data dependency, independence, capture layer) — uniform across heterogeneous sources — rather than over contested content, which is not. Generalized: **the assessment layer's ceiling is set at ingestion.**

## The theory underneath it

**Bespoke structure is invisible from the inside. That — not representation — is why knowledge artifacts don't compound. We have a discipline that makes the boundary legible, and a rig that tests it.**

A wiki gives you unlimited structural freedom and no signal about what any given structure *is*. So three very different things come out of a working session looking identical on disk:

- **Forced by the world** — you cannot cite more precisely than you captured. No design choice escapes it.
- **Forced by this problem** — the COVID case needs a split institutional layer because three official bodies contradict each other; the LHC case does not, because it has one safety review.
- **Freely chosen** — whether the grounding-layer marker is a prose word or a frontmatter field.

All three arrive as links and headings. From inside one project they cannot be told apart. Knowledge artifacts fail to travel not because they *can't*, but because nobody can tell which parts would survive the trip. The brief names this as a symptom — "single-user artifacts tuned to one investigator's context, not the kind that travel, combine, or survive scrutiny" — and this thesis names the mechanism under it.

Commonplace's actual practice is a discipline for keeping the three apart, giving each a **different home and a different promotion rule**: proposals carry literal `## Forces` and `## Free choices` sections; problem-local structure lives collection-local; transferable structure must *earn* promotion by surviving a second, differently-shaped case (build-local-first, upstream-what-survives, worked-case-first). The framework has already run this on itself — [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) demoted registers from universals to *default profiles*, keeping only the declared contract and answerability as universal ([the demotion note](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md)).

This is the brief's **protocol** shape — "interoperability and compounding without flattening the underlying material… how to maintain them as sources, users, and AI capabilities change" — and it answers the brief's own top criterion (*does it compound, with multiple people building on each other's work?*) with a mechanism rather than a hope. It also cashes out at the case level, which is what the brief actually demands: a casebook that marks which of its structures are load-bearing on the world and which are the author's choices is precisely what lets a second investigator "usefully pick up where another left off."

### The three cases are an instrument, not a demo

They are differently shaped **on purpose**: LHC is one load-bearing dependency chain, COVID is two parallel evidential structures plus a split institutional layer, eggs is dueling syntheses over a single relationship. A structure that survives all three unamended is, by construction, not bespoke. One that needs amendment tells you exactly which limb was local. That is a transfer test rig, and it is the thing no six-week entrant can assemble.

It also gives us the critique the brief explicitly invites as an entry shape. Entrants building argument graphs are asserting a universal structure — claims, support/attack edges, weights — for all epistemic disputes. That is a design choice presented as a necessity, and *from inside one case you cannot tell the difference*. Our rig is the apparatus that would reveal it.

### Subordinate result: flatten the provenance, not the argument

Schematize only what is decidable — does this quoted span occur in that snapshot, does this link resolve, is this note stale with respect to the source version it cites — and machine-check it. Leave what is not decidable — what supports what, how much, whose reading is right — in constrained prose under a declared `COLLECTION.md` contract, reviewed by snapshot-anchored LLM gates.

This is a **result of the discipline, not the thesis**, and it demonstrates it. We assumed a structured source-span locator type was needed; we built local-first, ran a worked case, and found the binding constraint was capture fidelity — an external limitation — while the locator type was a free choice we had nearly mistaken for a necessity.

### Why not enter on the structure layer

The casebooks' visible content *is* structure — position maps, contested joints, dependency chains. But structure is where entrants with purpose-built argument graphs will be strongest and most legible, and against those, prose notes with a link grammar read as *less* structured rather than more. Entering there invites the one comparison we lose — and it concedes in advance the very assumption the thesis above attacks.

### The evidence

All of it already exists; the entry's job is to assemble and narrate it, not to invent it. Each item is an instance of the discipline, not just a feature.

1. **The contract transferred across three differently-shaped cases without amendment** — the rig's first positive result (sibling backlog, 2026-07-09). What generalized was the *contract*, not the code.
2. **The `source_type` gap recurred three times before promotion** — the rig's other mode: a structure proving it was not bespoke by recurring across cases, and only then earning a place upstream ([ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md)).
3. **The source-span locator was *not* built** — the negative result, and the more valuable one: the discipline stopped a structure that felt necessary and wasn't.
4. **Deterministic provenance verification found real defects in our own corpus** — `scripts/verify_quotes.py` over the 14 casebook notes: 88 candidates, 58 match, **24 mismatch**, 6 unresolved, no false mismatches on manual audit ([verifiable-quotes proposal](../../reference/proposals/verifiable-quotes.md)). The crispest single demo we have. Note also that the proposal *admits in writing* it "did not originate from a felt friction case" — the discipline catching its own violation on the page, before the prototype went and supplied the missing evidence. Do not tidy this away; it is the strongest honesty signal in the entry.
5. **The register-drift experiment** — an assumption ("contradictions get silently averaged") tested and found wrong in an instructive way, with a blind judge, a declared confound, and an n=2 caveat.
6. **Freshness baselines and snapshot pinning** — the literal answer to "how do you maintain them as sources change." Others' compounding stories will be aspirational; ours is running code that predates the competition.

**Promotion done (2026-07-12).** Items 3 and 5 existed only as casework notes in the sibling repo, unlinkable from here. Both are now promoted into this repo's library, reformulated for reach rather than copied — the sibling titles named *experiment results*; these name the *general claims* underneath, with the experiments demoted to evidence:

- [A citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) — the capture-fidelity claim. Reformulated around the fidelity/authority distinction (it composes with, rather than contradicts, [trace-derived memory earns authority per operation](../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md)), and grounded so that capture layering is shown to be an *inherited constraint* (context window, copyright, output filters) while the locator syntax is a *free design choice* — which is the entry's thesis applied to its own evidence.
- [Context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — the drift claim, retitled onto the general mechanism. "Detecting it confers no immunity" is now the load-bearing part, because it is the part that survives the pilot's declared confound.

Both sit under existing general lemmas rather than free-floating: the first `exemplifies` [history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md); the second `exemplifies` [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md). That the casework results landed *under* pre-existing framework claims is itself evidence for the entry — the theory was load-bearing before the cases were run.

## Evaluation boundary

- **The deliverable is the submission document.** The code is evidence for it. Nothing else in this workshop outranks getting the document written.
- **Casework stays in the sibling repo**, per the [existing protocol](../epistack-competition/README.md). Framework changes land here. This workshop may direct work in both, but does not relocate either.
- **No new framework machinery that a worked case hasn't earned.** Build-local-first still holds; the deadline is not a licence to ship speculative types.
- **Doctrine constraints are inputs, not open questions:** no stored confidence/authority scalars, adjudication stays a downstream labelled layer, frontmatter semantics stay type-owned.

## Build candidates

Ranked by judge-visible value per day. The plan below commits to the first two and rejects the third; anything else stays out of scope for the deadline.

### Ship the quote verifier properly (committed)

The prototype exists and has run. What is open is **where it lives**: promoting it from `scripts/` into `commonplace-validate` would make it prominent and make every consuming KB inherit the check, which is the maintainer's stated preference. The [proposal](../../reference/proposals/verifiable-quotes.md) notes the tension — it is a Level A deterministic check, but a cross-file body-text comparison, which does not fit the validator's frontmatter/structure schema machinery; it sits closer to link-health. Decide that, then run it clean across all three cases and report before/after numbers. The 24 mismatches each need a fix or a re-mark.

### An independence / correlated-evidence instrument — run as a live transfer test (committed)

The one Assessment-layer item in the brief we can reach in the time ("flag correlated evidence being treated as independent"), and every case already contains a textbook instance that is identified but unmapped. Crucially, correlated evidence takes a **different form in each case**:

- **COVID** — Andersen/Worobey/Pekar author overlap, *plus* multiple analyses reusing the same Huanan-market metagenomic dataset. The case contract already flags this hazard; no note maps it. This is also the outstanding COVID depth work, so the two tasks are one.
- **LHC** — the whole safety case funnels through the cosmic-ray argument as a single load-bearing dependency; Ord–Hillerbrand–Sandberg is literally an out-of-model-error critique of exactly that.
- **Eggs** — industry funding (Barnard 2019).

Because the forms differ, this is not just a feature build — **it is the rig running live, inside the entry**. Invent the structure on one case, then try it on the other two. If one structure covers all three, it has earned promotion and we say so. If it doesn't, we report precisely which limb was local and which was universal. **Both outcomes are publishable results**, and either one demonstrates the thesis. Write it up as a transfer test, not as a feature announcement.

Scope: a link-grammar addition plus one worked note per case plus a review gate. **Not** a general algorithm — generality is not reachable here, and claiming it would be the exact error the thesis indicts.

### Author-authority ranking (rejected — and the rejection is entry material)

The [authority-ranking workshop](../authority-ranking/README.md) says the order shape itself is unknown: possibly partial, possibly domain-conditional, non-additive under independence. Six days will not settle that.

The rejection is not merely "no time" — it is **the discipline in the negative**, and it belongs in the submission as such: we decline to build a structure whose shape we have not established, which is exactly the restraint we are indicting other approaches for lacking. A half-built scalar rank would hand a judge the precise flattening critique this entry exists to make. Name it in the submission as a documented open problem; the brief explicitly asks entrants to make clear where design choices are uncertain.

### Rebuild the three cases from scratch (committed — this is the experiment)

**[replication-plan.md](./replication-plan.md).** The first build got messy — contract invented in flight, a framework upgrade mid-stream, nearest-fit source types, lifecycle churn — and, more importantly, it *cannot test the thesis*: the contract was co-developed with case 1, so "transferred to cases 2 and 3 without amendment" is a fitted result, not a tested one. One operator, sequential builds, full memory, no independent arm. The headline evidence is consistent with the thesis and equally consistent with its negation.

The rebuild inverts the crucial condition: **the contract is now fixed in advance.** Every amendment the rebuild needs becomes a finding rather than a fitting, and every structure that survives unamended is a genuine transfer result. The instrument is convergence between builders who never saw each other's work (exclusion, not instruction — our own contamination finding forbids the cheap version), scoring which structures converge (forced) against which diverge (chosen), against predictions **sealed before the run**.

This is the workshop's most expensive item and the one most likely to embarrass us. That is why it goes first.

## Plan

Days are working days from 12 July; submission 19 July.

| Days | Work |
|---|---|
| 1 | Ship the quote verifier — must exist *before* the rebuild lands, so the rebuild's citations are machine-checked, not hand-trusted. Settle where it lives; run it on the old build to fix the 24/88 baseline |
| 1–3 | Rebuild, **in the background** — it is agent wall-clock, not our attention. Minimum-viable: COVID, two cross-family builders, contract frozen, predictions sealed ([replication-plan.md](./replication-plan.md)) |
| 1–4 | **Our attention goes here:** the `source-assessment` retarget — type spec, parser config-table swap, provenance matrix over the three cases' sources ([assessment-machinery-line.md](./assessment-machinery-line.md)). This *subsumes* the independence instrument: the correlated-evidence flag becomes a computed cluster rather than a bespoke link-grammar addition |
| 5–6 | Score the rebuild against the sealed predictions; write the submission; buffer |

The retarget and the rebuild compete for the same days. If only one runs, **run the retarget** — it has 141 data points behind it against the casebooks' three, answers more of the brief, and carries external validation. The rebuild is mostly background wall-clock, so try for both; if it slips, run the matrix over the existing cases and declare the mess.

The document needs two full days and does not exist yet. If the schedule slips, the build shrinks — not the writing, and not the replication. An entry whose central claim was tested and survived, or was tested and qualified, beats one whose central claim was merely asserted more fluently.

## Entry material we already have and should not hide

Under this thesis, the repo's own working record *is the primary evidence*, because the discipline is the claim. The sibling repo's `backlog-to-commonplace.md` (append-only, with its Outcome lines showing what earned promotion and what did not), this repo's open workshops, the `## Forces` / `## Free choices` sections in proposals, and [rejected-candidates](../epistack-framework-additions/rejected-candidates.md) are not embarrassments to tidy away before submitting — they are the audit trail that shows the boundary between forced and chosen being drawn in real time, by people who did not know the answer yet. Cite them, and cite them prominently rather than as an appendix.

## What closes it

The submission is sent by 19 July. Then: extract the durable framework conclusions (whatever the quote-verifier siting decision and the independence instrument turn out to prove) into `kb/reference/` and `kb/notes/`, fold the two predecessor epistack workshops into whatever survives, and delete this directory.
