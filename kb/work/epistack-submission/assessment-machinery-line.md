# The assessment-machinery line — an optional supporting demonstration

**Role: an optional supporting Assessment-layer demonstration for the [constraint-driven design submission](./README.md).** The provenance matrix and computed correlated-evidence clusters address one brief bullet explicitly, but they are not the entry's spine. Build the smallest usable version only if it does not displace the methodology write-up, three-case walkthroughs, or submission document.

If the retarget happens, it does double duty: retargeting the parser from software-repo reviews to epistemic sources **is** a transfer test on our own tooling, so preregistering the code split costs a diff. That secondary evidence is worth retaining, but it does not justify expanding the build.

What it does **not** do is prove we have a general assessment facility. The pipeline is n=1, and reading a general capability off a single bespoke instance is the precise error this document was written to catch.

## The overclaim we nearly made

The tempting line was: *Commonplace makes repeatable assessment instruments cheap to stand up — look, 141 reviews and a matrix.* That reads a **general capability off a single bespoke instance**, which is the bespoke-structure-invisible-from-the-inside failure, committed by us, in the document arguing against it. Stated plainly, so it stays caught:

- The pipeline is **n=1**. One domain, one uniform source (GitHub), one corpus.
- The pipeline code is **bespoke: ~755 lines** across `src/commonplace/lib/systems_matrix.py`, `scripts/build_systems_matrix.py`, `scripts/analyze_matrix.py`, `scripts/render_systems_table.py`. **None of it ships as a `commonplace-*` command.**
- The generalization is *identified but unbuilt*. The [bulk-operations workshop](../bulk-operations/README.md) already names `kb/agent-memory-systems/` as "the existing implicit precedent (`systems.csv` registry + review member type + generated matrix)" and names the missing abstraction — a **document-set spec** — as an open direction.

So we do not have assessment-pipeline machinery. We have **one worked pipeline and a hypothesis about what generalizes from it.** Say that.

## What we do have, stated at the strength the evidence supports

Two separable things, and only the first is proven.

**Shipped and real — the substrate.** Types with schema validation; collection contracts that act as review criteria; the review system (snapshot-anchored assays, criterion paths, model partitions, freshness baselines); skills owning production; quote-anchored citations with a grounding check. None of this was built for the memory corpus; all of it was available to it.

**Bespoke and unproven-as-general — the pipeline.** The parse-to-matrix layer: lead-token extraction, one-hot indicators, applicability rules, absence semantics, cross-corpus analysis. Written once, for one shape of data.

The checkable claim that survives is narrower and better: **the domain-specific surface was small.** A 141-subject, 55-column comparative corpus with quantitative findings and an [ASIS&T position paper](../../sources/where-it-lives-retained-adaptation-2026-06-23.md) cost **one type spec, one skill, and ~755 lines** — because the framework carried types, validation, production, provenance, and freshness. That is a defensible "not much effort." It is *not* "we have a generic facility," and the difference is the whole credibility of the entry.

## The existence proof, and what it is proof *of*

The `agent-memory-system-review` type ([spec](../../agent-memory-systems/types/agent-memory-system-review.md)), run repeatably:

- **151 reviews; 141 code-grounded** and admitted to the matrix.
- **A 55-column matrix** ([`systems.csv`](../../agent-memory-systems/systems.csv)) built by **parsing the review prose**.
- **Quantitative cross-corpus findings** with real *n*s ([comparative review](../../agent-memory-systems/agentic-memory-systems-comparative-review.md)): files/repo storage leads at 98/141 yet predicts little; 79/95 trace-derived systems push memory; automatic activation is largely shipped untested.

It proves the *shape* works and that the domain surface is small. It does **not** prove the shape transfers. Only a second instance can do that.

## Therefore: build the second instance

Build-local-first, upstream-what-survives is our own discipline, and it says a structure earns promotion by surviving a second, differently-shaped case. We have one. **The epistemic source-assessment pipeline is the second** — in a genuinely hostile domain, on a one-week clock.

**n=2 is the first point at which forced can be told from chosen.** What survives both instances was generic; what has to be rebuilt was domain-specific all along.

### Scope boundary: we are not building the generic facility

The deliverable is the **second instance and the measured split**, plus a written statement of what a general layer would have to contain. **Not the layer itself.**

The bulk-operations work is *planned, large, and not ready* — [its workshop](../bulk-operations/README.md) already names this corpus as "the existing implicit precedent" and the missing **document-set spec** as an open direction, and six days will not close it. Promising the facility would stack a second overclaim on the one this document was written to catch.

So the entry says exactly this, and no more: *we ran the transfer test on our own tooling; here is what survived; here is what a general layer would need; we have not built it, and here is why it is a lot of work.* The requirement feeds the bulk-operations workshop. The **finding** — not the facility — is the durable artifact, and it is honest, falsifiable, and tested inside the entry. Judges will trust it **because** we refused to claim the general capability from n=1.

### Preregister the split

Before the retarget, predict which of the ~755 lines is which, then measure. Same convergence instrument as the [rebuild](./replication-plan.md), applied to code.

- **Predicted generic (survives untouched):** lead-token regex; one-hot indicator construction; applicability rules; the three-kinds-of-absence semantics; the worklist-of-blanks; evidence-tier gating of matrix admission.
- **Predicted domain-specific (replaced wholesale):** the axis/vocabulary config table; the CSV column schema; the analysis queries.
- **Genuinely uncertain:** whether the *row unit* generalizes. Memory systems are naturally one-row-per-subject. Whether epistemic sources are too is the open question below.

If the "generic" list needs rewriting, the general facility does not exist and we say so. That is a publishable result and the brief names it as an entry shape.

## The transferable invention, named: the welded token

The mechanism worth submitting is not the memory-system vocabulary. It is how a value and its justification are bound:

```
**Storage substrate:** `graph` — the retained state persists in a Neo4j-backed store, so …
```

The controlled, machine-parseable value is the **lead of its own justifying sentence**, in the prose, as part of the finding. The type spec says why in one line: *"so the value and its reasoning cannot drift apart."*

This resolves the tension the brief names as the hard problem for a protocol entry — *"how to link diverse subtopics and complex, multi-perspective investigations while preserving important detail."* Both obvious answers fail:

- **A structured layer beside the prose** → it drifts, and by our own [derived-copy rule](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) an unchecked derived copy is forbidden outright.
- **Flatten the prose into a schema** → the nuance that made the analysis worth doing is destroyed.

The welded token does neither. **One artifact**; the matrix is *derived by parsing it*, so no second copy exists to drift, and the justification travels attached to the value it justifies. This is the piece most likely to survive the transfer, and the piece worth naming in the submission whatever else happens.

## Epistemic metadata that is already first-class

The brief asks what *"supporting epistemic metadata would help [assessment methodologies] work better."* The type spec answers, in shipped form:

- **Three distinct kinds of absence.** `not-determinable` (assessed, could not tell) ≠ `none` (assessed, verified absent) ≠ blank (not assessed). The parser keeps them apart and turns blanks into a worklist. Most schemes collapse all three — which is how "no evidence of X" quietly becomes "evidence of no X."
- **Evidence tiers gate aggregation.** `source-tier: code-grounded | doc-grounded`, and doc-grounded reviews are **excluded from the matrix**. Provenance decides what may be *counted*, not merely what may be read.
- **Structural/quality separation.** Mark what the evidence class cannot license as *not verified from code*.
- **Quote-anchored citations** pinned to immutable revisions with a write-time grounding check ([verify-review-quote-grounding](../../instructions/verify-review-quote-grounding.md)).

## The precondition, and the honest limit: uniform capture

**The method works where the data can be gathered uniformly.** The 141-corpus had that handed to it: the source was **GitHub**. Same kind of subject, same access method, same evidence class, every row. Clone, read, answer the axes.

The framework already knows this is binding — which is why `source-tier` exists. Systems with no reachable source are `doc-grounded` and **excluded from the matrix**. That exclusion *is* the uniformity precondition, enforced, for reasons that predate this competition.

**Epistemic casework has no such surface.** COVID alone spans peer-reviewed papers, an intelligence assessment, a WHO report, court filings, an essay, preprints, and threads — different genres, access methods, evidence classes, capture fidelities. There is no `git clone` for a contested question, and this heterogeneity is what drove the source-genre gap to recur three times before [ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) opened the field.

So the naive retarget — rows are *claims*, axes *adjudicate* them — fails twice: **non-uniform axes** (you cannot ask a court filing and a molecular-clock preprint the same question and get comparable answers) and **manufactured precision** (a controlled vocabulary over *"is the furin cleavage site evidence of engineering"* flattens exactly what must not be flattened).

### What *is* uniformly gatherable

The design move, and the contribution. Heterogeneous sources still share **uniform provenance facts**. Every source, whatever its genre, has an **author** (institution, funding), a **genre**, a **data dependency**, an **independence relation** to every other source (shared authors, shared data, shared funder, citation chain), a **capture layer** ([a citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md)), and a **primary/secondary** standing.

Those are answerable uniformly across a court filing *and* a preprint *and* a WHO report. **Provenance is uniform even when content is not.** So the matrix's rows are **sources**, and its axes are **provenance and independence** — not claims and verdicts.

That lands on the brief's reachable Assessment bullets (*"flag correlated evidence being treated as independent"*, *"surface what's missing"*), and it collapses two build items into one: **the independence instrument and the matrix retarget are the same thing.** COVID's Andersen/Worobey/Pekar author overlap and the analyses reusing the same Huanan metagenomic dataset stop being a prose caveat and become **a computed cluster**.

### The finding this yields

**The assessment layer's ceiling is set at ingestion.** A citation cannot assert more fidelity than its capture preserved; a matrix cannot aggregate more than its capture gathered *uniformly*. Same principle one level up — what ingestion failed to make comparable, no assessment methodology can make comparable afterwards. It explains `source-tier`, it explains why the epistemic retarget must aggregate over provenance, and it is falsifiable.

### The discipline that keeps it honest

**The matrix must be allowed to come out mostly `not-determinable`.** If the epistemic axes will not fill, that is the finding — contested material resists the treatment architectural facts accept — and we publish it rather than tuning axes until the cells populate.

## The build

1. **A `source-assessment` type spec** — rows are sources; axes are provenance and independence; same welded-token discipline, same absence semantics, same evidence-tier gating.
2. **Retarget the parser, measuring the split against the preregistered prediction.** The domain vocabulary is a config table; the extraction machinery is generic *by hypothesis*. Test it.
3. **Run it over the three cases' sources**; produce the provenance matrix and the correlated-evidence clusters.
4. **Score the split against the sealed prediction, and write down what a generic layer would need.** A requirement, filed to [bulk-operations](../bulk-operations/README.md) — **not** an implementation. This is the honest stopping point.
5. *(Stretch, only if 1–4 land early)* **Multi-method comparison** — two rival assessment specs over the same subquestions, divergence localized. Entry shape #4, and where the brief's hook cashes out: **six independent Bayesian analyses of the same COVID evidence spanned 23 orders of magnitude** — a bespoke-structure failure, where each analyst's decomposition looked forced from inside. Steps 1–4 stand alone without this.

## How it carries the generalization section

The entry's [generalization section](./README.md#does-it-generalize--the-transfer-discipline) needs to say how we tell forced structure from chosen structure. **Convergence is that test**, and it can be applied at three layers:

- **Structure** — do independent builders converge on the same casebook structure? ([the rebuild](./replication-plan.md) — designed, preregistered, **not run**)
- **Assessment** — do independent methodologies converge on the same verdict, and where do they diverge? (the multi-method comparison — stretch item 5 below)
- **Tooling** — does our own pipeline code survive a second domain, or was it bespoke all along? (**the preregistered code split — the one that actually runs**)

Only the third is eligible for the six-day scope, and only if the supporting matrix is built. If it runs, report it as one measured instance; if it is cut, leave the preregistered prediction unscored rather than implying a result. The protocol submission does not depend on this measurement.
