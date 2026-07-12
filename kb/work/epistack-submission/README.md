# Workshop: epistack-submission

Building the actual entry to the FLF [Epistemic Case Study Competition](../../sources/epistemic-case-study-competition.md). **Due 19 July 2026**; opened 12 July, so this workshop has roughly six working days and closes at submission.

The two existing epistack workshops are inputs, not competitors to this one: [epistack-competition](../epistack-competition/README.md) holds the two-repo protocol (framework here, casework in the sibling `epistack-casebooks`), and [epistack-framework-additions](../epistack-framework-additions/README.md) holds the design menu of candidate additions. Neither one decides what we submit. This workshop does.

## The thesis we are entering on

**Flatten the provenance, not the argument.**

Schematize only what is decidable — does this quoted span occur in that snapshot, does this link resolve, is this note stale with respect to the source version it cites — and machine-check it. Leave what is not decidable — what supports what, how much, whose reading is right — in constrained prose under a declared `COLLECTION.md` contract, reviewed by snapshot-anchored LLM gates. Interoperability comes from sharing the contract and the provenance layer; nuance survives because the argument was never forced into a schema too small to hold it.

This makes the entry the brief's **protocol** shape ("enabling interoperability and compounding without flattening the underlying material… how to maintain them as sources, users, and AI capabilities change"), not its prototype-tool shape.

### Why not enter on the structure layer

The casebooks' visible content *is* structure — position maps, contested joints, dependency chains. But structure is the layer where entrants with purpose-built argument graphs (Toulmin, IBIS, Bayesian nets, Rootclaim-style decomposition) will be strongest and most legible, and against those, prose notes with a link grammar read as *less* structured rather than more. Entering there invites the one comparison we lose.

Two of our own results already argue for the thesis above instead. The source-span experiment concluded a structured locator type was **not** needed — capture fidelity, not notation, is the binding constraint. The silently-averaged experiment found the real failure mode is prose contamination, not structural ambiguity. We have empirical grounds for the position, not just a preference.

Both results are written up as notes in the *sibling* repo (`epistack-casebooks`, `kb/notes/citation-granularity-is-capped-by-capture-fidelity.md` and `kb/notes/a-verdict-in-context-produces-register-drift-not-verdict-copying.md`) and reach this repo only through the backlog, so they are not linkable from here. If the submission leans on them as framework-level claims — and the thesis does — one of them may need promoting into `kb/notes/` here. Open question, not a decision.

### The four pieces of evidence

All four already exist; the entry's job is to assemble and narrate them, not to invent them.

1. **The contract transferred across three differently-shaped cases without amendment** — logged in the sibling repo's backlog (2026-07-09). The thing that generalized is the *contract*, not the code, which is a stronger generalization result than "we ran our pipeline three times."
2. **Deterministic provenance verification that found real defects in our own corpus** — `scripts/verify_quotes.py` over the 14 casebook notes: 88 candidates, 58 match, **24 mismatch**, 6 unresolved, no false mismatches on manual audit ([verifiable-quotes proposal](../../reference/proposals/verifiable-quotes.md)). The crispest single demo we have.
3. **The register-drift experiment** — a controlled 2×2 with a blind judge, clean separation, *and* a declared confound and n=2 caveat. The brief lists "a critique with counterexamples" as a valid entry shape on its own; the caveats are the credential with this audience.
4. **Freshness baselines and snapshot pinning** — the literal answer to "how do you maintain them as sources change." Other entrants' compounding stories will be aspirational; ours is running code that predates the competition.

## Evaluation boundary

- **The deliverable is the submission document.** The code is evidence for it. Nothing else in this workshop outranks getting the document written.
- **Casework stays in the sibling repo**, per the [existing protocol](../epistack-competition/README.md). Framework changes land here. This workshop may direct work in both, but does not relocate either.
- **No new framework machinery that a worked case hasn't earned.** Build-local-first still holds; the deadline is not a licence to ship speculative types.
- **Doctrine constraints are inputs, not open questions:** no stored confidence/authority scalars, adjudication stays a downstream labelled layer, frontmatter semantics stay type-owned.

## Build candidates

Ranked by judge-visible value per day. The plan below commits to the first two and rejects the third; anything else stays out of scope for the deadline.

### Ship the quote verifier properly (committed)

The prototype exists and has run. What is open is **where it lives**: promoting it from `scripts/` into `commonplace-validate` would make it prominent and make every consuming KB inherit the check, which is the maintainer's stated preference. The [proposal](../../reference/proposals/verifiable-quotes.md) notes the tension — it is a Level A deterministic check, but a cross-file body-text comparison, which does not fit the validator's frontmatter/structure schema machinery; it sits closer to link-health. Decide that, then run it clean across all three cases and report before/after numbers. The 24 mismatches each need a fix or a re-mark.

### An independence / correlated-evidence instrument (committed)

The one Assessment-layer item in the brief we can actually reach in the time ("flag correlated evidence being treated as independent"), and every case already contains a textbook instance that is identified but unmapped:

- **COVID** — the Andersen/Worobey/Pekar author overlap, *and* multiple analyses reusing the same Huanan-market metagenomic dataset. The case contract already flags this hazard; no note maps it. This is also the highest-value COVID depth work outstanding, so the two tasks are one.
- **LHC** — the whole safety case funnels through the cosmic-ray argument as a single load-bearing dependency, and Ord–Hillerbrand–Sandberg is literally an out-of-model-error critique of exactly that.
- **Eggs** — industry funding (Barnard 2019) as the correlation story.

Scope: a link-grammar addition plus one worked note per case plus a review gate. **Not** a general algorithm — cross-case coverage is what the brief rewards, generality is not reachable here.

### Author-authority ranking (rejected for this deadline)

The [authority-ranking workshop](../authority-ranking/README.md) says the order shape itself is unknown — possibly partial, possibly domain-conditional, non-additive under independence. Six days will not settle that, and a half-built scalar rank hands a judge the exact "flattening" critique this entry's thesis is built to refuse. Park it, and **name it in the submission as a documented open problem** — the brief explicitly asks entrants to make clear where design choices are uncertain.

## Plan

Days are working days from 12 July; submission 19 July.

| Days | Work |
|---|---|
| 1–2 | Quote verifier: settle where it lives, ship it, run clean across all three cases, fix or re-mark the 24 mismatches, record before/after |
| 3–4 | Independence instrument: link-grammar addition, one worked note per case, review gate |
| 5–6 | Write the submission document; buffer |

The document needs two full days and does not exist yet. If the schedule slips, the build shrinks — not the writing.

## Entry material we already have and should not hide

The brief rewards transparency about uncertainty and a visible compounding record. The sibling repo's `backlog-to-commonplace.md` (with its append-only Outcome lines), this repo's open workshops, and [rejected-candidates](../epistack-framework-additions/rejected-candidates.md) are *evidence for the protocol*, not embarrassments to tidy away. Plan to cite them as an appendix.

## What closes it

The submission is sent by 19 July. Then: extract the durable framework conclusions (whatever the quote-verifier siting decision and the independence instrument turn out to prove) into `kb/reference/` and `kb/notes/`, fold the two predecessor epistack workshops into whatever survives, and delete this directory.
