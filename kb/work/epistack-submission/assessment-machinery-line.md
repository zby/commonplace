# The assessment-machinery line

**Recommendation: this leads the submission.** Not as an alternative to the transfer thesis — that becomes the theory explaining why it works. This is the evidence, and there is far more of it than the casebooks have.

## The claim

**Commonplace makes a repeatable assessment instrument cheap to stand up.** You *declare* the methodology as a type; the framework supplies the apparatus around it.

That is the submission line, and it reframes what looked like our biggest weakness. We said: *the epistemology tools the competition needs can be built in Commonplace, but we don't have them ready-made, and there are only six days.* The correct response is not to apologise for that. It is to say: **ready-made is the wrong ask, and six days is enough — here is us doing it, and here is the same thing already done once at scale in another domain.**

The bottleneck in epistemic investigation was never the shortage of assessment methodologies. Everyone has opinions about how to weigh evidence. The bottleneck is that every methodology needs an *apparatus* around it before it can be applied repeatably and compared — a schema, structural validation, a production pipeline, provenance rules, staleness tracking, and some way to aggregate N results into a comparable whole. Building that apparatus is expensive, so methodologies get applied once, by hand, by their author, and never travel. That is exactly the brief's complaint: *"single-user artifacts tuned to one investigator's context, not the kind that travel, combine, or survive scrutiny."*

Commonplace supplies the apparatus generically. The methodology becomes a declaration.

## The existence proof

The `agent-memory-system-review` type ([spec](../../agent-memory-systems/types/agent-memory-system-review.md)) is a codified assessment methodology, declared as a type, and run repeatably:

- **151 reviews on disk; 141 code-grounded** and admitted to the matrix.
- **A 55-column matrix** ([`systems.csv`](../../agent-memory-systems/systems.csv)), built by **parsing the review prose** (`scripts/build_systems_matrix.py`, `src/commonplace/lib/systems_matrix.py`).
- **Quantitative cross-corpus findings** with real *n*s ([comparative review](../../agent-memory-systems/agentic-memory-systems-comparative-review.md)): files/repo storage leads at 98/141 yet predicts little; 79/95 trace-derived systems push memory while 34/50 pull-only systems are not trace-derived; automatic activation is largely shipped untested.
- **Peer-review-grade output**: the ASIS&T 2026 position paper ([snapshot](../../sources/where-it-lives-retained-adaptation-2026-06-23.md)) applies the four-field vocabulary to the corpus.

Nobody wrote an application to get this. Someone wrote a **type spec** and a **skill**, and the framework did the rest.

## What the framework supplies, versus what the analyst declares

This table is the entry. It is what makes the claim concrete rather than a boast.

| The analyst declares | Commonplace supplies for free |
|---|---|
| The methodology's sections and axes (the type spec) | Structural validation against the schema — every review conforms or fails |
| The controlled vocabularies | A parser that one-hots authored tokens into a matrix; unassessed axes surface as a worklist, not as silent zeroes |
| The evidence rules (what grounds a claim) | Quote-anchored citations pinned to immutable revisions, plus a grounding check |
| The prose contract (how reviews are written) | `COLLECTION.md` conformance as a review gate — the contract *is* the criterion |
| What makes a review stale | Snapshot-anchored freshness baselines, partitioned by model |
| The production procedure | A skill owning source prep, delegation, QA, validation, reporting |

The analyst writes the epistemology. The framework writes everything that makes the epistemology *repeatable*.

## The transferable invention, named: the welded token

The mechanism worth submitting is not the memory-system vocabulary. It is how a value and its justification are bound together:

```
**Storage substrate:** `graph` — the retained state persists in a Neo4j-backed store, so …
```

The controlled, machine-parseable value is written **as the lead of its own justifying sentence**, in the prose, as part of the finding. The type spec says why in one line: *"so the value and its reasoning cannot drift apart."*

This resolves the exact tension the brief names as the hard problem for a protocol entry — *"how to link diverse subtopics and complex, multi-perspective investigations while preserving important detail."* Both obvious answers fail:

- **A structured layer beside the prose** → it drifts, and by our own [derived-copy rule](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) an unchecked derived copy is forbidden outright.
- **Flatten the prose into a schema** → the nuance that made the analysis worth doing is destroyed.

The welded token does neither. There is **one artifact**; the matrix is *derived by parsing it*, so no second copy exists to drift, and the justification travels attached to the value it justifies. Interoperability and nuance out of the same line of prose — proven at n=141.

## Epistemic metadata that is already first-class

The brief asks what *"supporting epistemic metadata would help [assessment methodologies] work better."* The type spec answers, in shipped form:

- **Three distinct kinds of absence.** `not-determinable` (assessed, could not tell) ≠ `none` (assessed, verified absent) ≠ blank (not assessed). The parser keeps them apart and turns blanks into a worklist. Most schemes collapse all three — which is how "no evidence of X" quietly becomes "evidence of no X."
- **Evidence tiers gate aggregation.** `source-tier: code-grounded | doc-grounded`, and doc-grounded reviews are **excluded from the matrix**. Provenance decides what may be *counted*, not merely what may be read.
- **Structural/quality separation.** Mark what the evidence class cannot license as *not verified from code*.
- **Quote-anchored citations** pinned to immutable revisions, with a write-time grounding check ([verify-review-quote-grounding](../../instructions/verify-review-quote-grounding.md)) — the same discipline the [quote verifier](../../reference/proposals/verifiable-quotes.md) enforces on the casebooks.

## Why it answers the brief better than the casebooks

| The brief asks | The machinery answers |
|---|---|
| "Does it compound, with multiple people building on each other's work?" | **Mechanically.** Each new review adds a matrix row *by being parsed*. No integration step, no curator. Every entrant will promise this; we can show it. |
| "Does it scale with improvements to AI or more compute?" | **Linearly.** More reviews, more axes, more model partitions. 141 already ran. |
| "Does it generalize?" | One contract, 141 subjects, findings that hold across them — and now a second domain in six days. |
| Entry shape: *"comparative analysis repeatably applying two or more AI assessment methodologies to the same subquestions"* | Two type specs over the same claims. The machinery is built; see the gap below. |

It also lands on the **Assessment layer** — which I originally judged our weakest. That judgment was wrong, and it was wrong for an instructive reason: I was looking at the casebooks and not at the 141-system corpus next door. Worth saying in the submission, because it is the same blindness the entry is about.

## The six days are the experiment, not the constraint

The build is a **retarget of a known-good pattern**, and that is what makes it feasible *and* what makes it evidence:

1. **A `source-assessment` type spec** — rows are **sources**, axes are **provenance and independence** (author, institution, funding, genre, data dependency, independence relations, capture layer, primary/secondary), because those are the facts a heterogeneous corpus can answer uniformly. Same welded-token discipline, same three-kinds-of-absence, same evidence-tier gating.
2. **Retarget the matrix parser.** The machinery in `systems_matrix.py` is generic — lead-token regex, one-hot indicators, applicability rules, `not-determinable`/`none` handling. The domain vocabulary is a **config table at the top of the file**. Retargeting is a table swap, not a rewrite. *This is the single most important feasibility fact in this document.*
3. **Run it over the three cases' sources**; produce the provenance matrix. The immediate payoff is the correlated-evidence flag the brief asks for: COVID's Andersen/Worobey/Pekar author overlap and the analyses reusing the same Huanan metagenomic dataset stop being a prose caveat and become **a computed cluster** — which is what makes it checkable, and what makes it compound.
4. **Then the multi-method comparison** — two rival assessment specs over the same subquestions, divergence localized. Entry shape #4, and where the brief's own hook cashes out: **six independent Bayesian analyses of the same COVID evidence spanned 23 orders of magnitude.** That is a *bespoke-structure* failure — each analyst chose a decomposition, and from inside each the decomposition looked forced. Running *k* methodologies over the same pinned evidence and localizing **where** they diverge is the direct answer. Stretch goal; steps 1–3 stand alone.

**Preregister the split before running it**, exactly as the [rebuild plan](./replication-plan.md) does: predict that the *apparatus* (welded tokens, absence semantics, evidence tiers, freshness) survives the domain change untouched, and that the *domain vocabulary* is replaced wholesale. The retarget then **is** the transfer test — the thesis eating its own dog food, on a one-week clock, in public.

## The precondition, and the honest limit: uniform capture

**The method works where the data can be gathered uniformly.** The 141-system corpus had that handed to it: the source was **GitHub**. Every subject was the same kind of thing, reachable the same way, yielding the same evidence class. Clone the repo, read the code, answer the axes. `storage substrate: graph` is checkable against source, uniformly, for every row.

The framework already knows this is the binding constraint — which is why `source-tier` exists at all. Systems with no reachable source are `doc-grounded` and **excluded from the matrix**. That exclusion *is* the uniformity precondition, enforced. We did not add it because it was elegant; we added it because non-uniform evidence cannot be aggregated honestly.

**Epistemic casework has no such uniform surface.** COVID alone spans peer-reviewed papers, an intelligence assessment, a WHO report, court filings, a Bulletin essay, preprints, and social threads — different genres, different access methods, different evidence classes, different capture fidelities. There is no `git clone` for a contested question. This is exactly the heterogeneity that drove the source-genre gap to recur three times before [ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) opened the field.

So the naive retarget — a matrix whose rows are *claims* and whose axes *adjudicate* them — will not work, and we should say so before a judge says it for us. Two obvious failure modes:

- **Non-uniform axes.** You cannot ask a court filing and a molecular-clock preprint the same architectural question and get comparable answers.
- **Manufactured precision.** A controlled vocabulary over *"is the furin cleavage site evidence of engineering"* flattens precisely what must not be flattened — the failure this entry exists to indict.

### What *is* uniformly gatherable

This is the design move, and it is the contribution. Heterogeneous sources still share **uniform provenance facts**. Every source, whatever its genre, has:

- an **author** (and an institution, and a funding status);
- a **genre**;
- a **data dependency** — which datasets, samples, or prior results it rests on;
- an **independence relation** to every other source — shared authors, shared data, shared funder, or a citation chain;
- a **capture layer** — verbatim, paraphrase, or second-hand ([a citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md));
- a **primary/secondary** standing.

Those axes are answerable uniformly across a court filing *and* a preprint *and* a WHO report. **Provenance is uniform even when content is not.** So the matrix's rows should be **sources**, and its axes should be **provenance and independence** — not claims and adjudications.

And that lands precisely on the brief's Assessment bullets we can actually reach: *"flag correlated evidence being treated as independent"*, *"surface what's missing"*, *"identify rhetorical moves that carry more persuasive weight than evidential weight."* It also collapses two build items into one: **the independence instrument and the matrix retarget are the same thing**, done with proven machinery instead of a bespoke link-grammar addition.

### The finding this yields

There is a real, transferable claim here, and it unifies the layers:

**The assessment layer's ceiling is set at ingestion.** A citation cannot assert more fidelity than its capture preserved; a matrix cannot aggregate more than its capture gathered *uniformly*. Same principle, one level up — what the ingestion layer failed to make comparable, no assessment methodology can make comparable afterwards. That is why `source-tier` gates the matrix, and it is why the epistemic retarget must aggregate over provenance rather than over content.

That claim is worth the submission on its own, it is falsifiable, and it explains a design decision we made for other reasons long before this competition.

### The discipline that keeps it honest

**The matrix must be allowed to come out mostly `not-determinable`.** If the epistemic axes will not fill, that is the finding — that contested material resists the treatment architectural facts accept — and we publish it rather than tuning the axes until the cells populate. The brief names "a critique with counterexamples" as an entry shape in its own right.

## How it unifies with the transfer thesis

One idea, demonstrated at two layers:

**Convergence is the test of forced-versus-chosen.**

- **Structure layer** — do independent builders converge on the same casebook structure? ([the rebuild](./replication-plan.md))
- **Assessment layer** — do independent methodologies converge on the same verdict, and *where exactly* do they diverge? (the multi-method matrix)

The welded token is what makes both cheap, repeatable, and machine-aggregable without flattening. The 141-system corpus proves the mechanism at scale *in a domain where the answers can be checked* — which is what earns the right to try it where they cannot.

## The tension to resolve

The rebuild and this line compete for the same days.

- **If only one runs: this one.** More evidence, more of the brief answered, external validation, a nameable mechanism.
- **They compose in sequence** — the rebuild produces clean casebooks; the matrix runs over them. A matrix built on the messy first build inherits the mess.
- **Practical resolution:** the rebuild is mostly agent wall-clock rather than our attention. Start it in the background (minimum-viable: COVID, two cross-family builders) and spend our attention on the retarget. If the rebuild slips, run the matrix over the existing cases and declare the mess.
