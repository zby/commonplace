# Worked case: agents-navigate-by-deciding-what-to-read-next

First pass through the whole chain by hand, per [Where to start](./README.md).
Executed 2026-08-24.

The object is **not** to disposition the note — that is
[literature-disposition](../literature-disposition/README.md)'s call. The
object is to find out what the existing ingest contract carries and what it
drops when you try to use an ingest to judge a note. The disposition signal
that falls out is a by-product, handed over at the end.

Order matters and was followed: claims enumerated from the note first, source
found second. Enumerating after reading the source would have let the source's
vocabulary decide what counts as a claim.

## 1. Claim inventory

Built from [the note](../../notes/agents-navigate-by-deciding-what-to-read-next.md)
before any source was read.

| id | Claim as stated |
|---|---|
| C1 | The follow/skip decision at a pointer "is the fundamental unit of navigation" |
| C2 | The decision is probabilistic — "how likely is this pointer to lead somewhere relevant, and what does it cost to find out?" |
| C3 | Context surrounding a pointer makes the decision tractable: it lets the reader judge relevance without loading the target |
| C4 | "The more context a pointer carries, the cheaper the navigation decision" |
| C5 | Pointer types carry different amounts of context — inline links most, search results least, indexes between |
| C6 | The system should therefore invest in different metadata per navigation mode: prose for link-following, titles and descriptions for search, both for indexes |
| C7 | Title-as-claim is a shortcut that works across all pointer types, making the pointer itself the cue |

C1–C4 are general claims about navigation under bounded resources. C5–C7 are
about Commonplace's own pointer surfaces.

## 2. The source

C1–C4 are information scent. The settling source chosen was Peter Pirolli, **The
Use of Proximal Information Scent to Forage for Distal Content on the World Wide
Web**, in Alex Kirlik (ed.), *Working with Technology in Mind: Brunswikian
Resources for Cognitive Science and Engineering* (PARC tech report UIR-2004-07).

Chosen over Pirolli & Card 1999 for three reasons: it is openly accessible where
the *Psychological Review* paper is not, so a reader routed to it can actually
follow the route; it is by the theory's own author, so it is primary rather than
a secondary gloss; and its subject is precisely the proximal/distal structure the
note's C3 states, applied to hypertext link labels rather than to foraging in
general.

Captured as `pirolli-proximal-information-scent-distal-content.md`, `pdftotext`,
sha256 `dcbc5653…`.

**Capture note worth recording, with its first diagnosis corrected.**
`cp-skill-snapshot-web` failed on this URL with an API content-filtering error at
the point of writing the snapshot, and the capture was completed directly with
`pdftotext`. That is *not* an extraction-tool difference: `pdftotext` is what the
skill itself uses ([SKILL.md](../../instructions/cp-skill-snapshot-web/SKILL.md),
step 2c). Extraction never failed.

The difference is the write path. The skill reads `extracted.txt` "in chunks
until EOF" into the agent's context and then requires it to "convert the
extracted text to clean Markdown," so the whole document — roughly 13k words,
including long runs of mangled equation glyphs — must be re-emitted as model
output through a single write. That output is what was blocked. The direct
capture concatenated frontmatter and extracted text with a shell redirect, so
the bytes never passed through model output and there was nothing to filter.

The direct capture is also the **worse** snapshot: 43 form feeds, 42 `Page N`
header artifacts interleaved mid-sentence, and one Markdown heading, the one
authored by hand. The skill's cleanup step would have produced a properly
sectioned reading copy. This is cruder-but-completed against better-but-blocked,
not a tooling win.

So the obstacle is the mandatory model-mediated cleanup on a source whose
extracted text is hostile to re-emission, and it is a design point rather than a
missing capability — write raw and skip cleanup for equation-heavy PDFs, or clean
in bounded chunks so no single output carries the whole document. It matters for
this workshop because the corpus it needs is largely equation-bearing PDFs.
Recorded as a finding; not fixed here, and the fix belongs to whoever owns the
skill, not to this workshop.

## 3. Claim by claim against the source

| id | Verdict |
|---|---|
| C1 | ~~Subsumed~~ → **Narrowing needed.** See the correction below |
| C2 | ~~Subsumed~~ → **Narrowing needed.** See the correction below |
| C3 | ~~Subsumed~~ → **Partly supported, needs narrowing.** See the correction below |
| C4 | **Not established — and the source separates the two things the note merges** |
| C5 | **Absent from the source.** Local, and locally untested |
| C6 | **Absent.** Local design consequence |
| C7 | **Absent.** Local design consequence |

**C1 and C3.** The source defines the construct directly: "Information scent
refers to the cues used by information foragers to make judgments related to the
selection of information sources to pursue and consume. These cues include items
such as Web links or bibliographic citations that **provide users with concise
information about content that is not immediately available**." And the framing
the note calls the fundamental unit: "Users' navigation in the Web environment
can be seen as involving assessments of proximal information scent cues in order
to make action choices that lead to distal information sources." The note's
"pointer hints at what the target contains, so you can judge without loading it"
is this, in different words, with no attribution.

**C2.** The source: foraging "involves uncertainties … about the location,
quality, relevance, veracity" — a "probabilistically textured information
environment" whose rationality must be analysed with "tools appropriate to
decision making under uncertainty." It then supplies what the note only gestures
at: a Bayesian log-odds account in which the estimate of distal feature *i* is
`A_i = B_i + Σ_j S_ji` — a base rate plus one strength term per proximal feature
— implemented as spreading activation and turned into a choice by a Random
Utility Model.

**Correction, 2026-08-24, from a stricter independent pass.** The
[claim-pull evidence summary](../claim-pull-implementation/claims-shape-evidence.md#pirolli)
re-ran this comparison under blind separation: one fresh worker reconstructed
the source's claims from the checksum-pinned observation without seeing this
note or this worked case, and a second judged C1–C4 against only the resulting
claim entries. It tightened three of the four verdicts, and it is right.

- **C1.** Pirolli models link choice, site leaving, keyword search, and URL
  search. The paper does not establish the "fundamental unit of navigation"
  wording. This worked case's own prose already said as much — "'fundamental
  unit' is the note's framing choice, not a claim the source makes or needs" —
  and the table above still said *subsumed*. The table overstated its own prose.
- **C2.** The source gives a stochastic link-choice account **and**, separately,
  a system-level value-over-cost tendency. It does not compose them into a
  pointer-level tradeoff, which is what C2 asserts.
- **C3.** The proximal/distal core is supported. "Surrounding context," "makes
  the decision tractable," and the avoided-load mechanism are not established as
  written and need narrowing.
- **C4.** Both passes agree.

**Why this matters beyond bookkeeping.** *Subsumed* and *needs narrowing* are
different dispositions. Reading thematic overlap as support is the exact error
that would license retiring a note into a source route that does not carry its
claims. The correction moves this note further from retirement, not closer:
more of its content survives contact with the source than this pass credited.

The method that caught it is worth keeping — blind separation of source-side
reconstruction from claim-side verification, neither worker seeing the other's
input. A single reader holding both the note and the source at once is the setup
that produces charitable over-attribution.

**C4 is where the note goes past the source, and does so by conflating two
quantities the source keeps apart.**

- *Estimate quality* (Equation 6): more proximal features add more evidence
  terms, and each term can be positive or negative according to how diagnostic
  the feature is. What improves the estimate is **diagnosticity**, not volume. A
  cue full of low-diagnosticity words adds terms near zero.
- *Cost* (Equation 1): the source's cost term is **cost of interaction** —
  "Human-information interaction systems will tend to maximize the value of
  external knowledge gained relative to the cost of interaction." That is the
  navigation cost the cue helps you avoid. **The cost of inspecting the cue
  itself is not modelled anywhere in the paper.** For a human scanning a link
  label before loading a page, that is a fair idealization.

The note's "the more context a pointer carries, the cheaper the navigation
decision" runs these together: it treats cue volume as if it reduced cost, when
in the source cue diagnosticity improves an estimate and cost is a separate term
the cue is not charged against.

The source's nearest approach to C4 confirms the reading. It cites Davison
(2000), who compared "elaborated anchor text (the anchor plus additional
surrounding text, having a mean of 11.02 terms)" against the page it links to
versus a random page, finding cosine similarity of `r = .16` linked against
`r ≈ 0` random. That is a test of the cue's **ecological validity**, not of its
length: it fixes one cue size and shows it beats chance. Nothing in the source
varies cue length and measures the result, so C4 has no support there even at
the level of direction.

`r = .16` is also the only magnitude the source supplies for the cue-to-content
relation, and it is weak — eleven terms of surrounding prose explain very little
about the target in 1998 Web writing. Commonplace's descriptions are
deliberately engineered cues rather than incidental prose, so they ought to do
far better, but nobody here has measured it. That gap is a cheap evaluation
design and a real open question, not a rhetorical point.

## 4. The delta, and why it is not decoration

The idealization that makes C4 harmless for Pirolli is exactly what breaks for
an LLM agent: **the cue and the target are consumed through the same bounded
channel and priced in the same units.** Reading 40 tokens of link context costs
what reading 40 tokens of the target costs. The cue is no longer free to inspect.

Three consequences the source cannot supply, because its cost model does not
contain the term:

1. C4's monotone becomes an interior optimum. Pointer context pays until its
   token cost exceeds the expected saving from the loads it avoids.
2. The break-even is a property of the **result set, not the pointer**. Cue cost
   is paid on every pointer scanned; the saving accrues only on pointers that
   would otherwise have been loaded. So the same description length can pay in a
   three-hit result and lose in a two-hundred-line scoped slice.
3. It gives a principled reason for a description *length limit*, which the
   note's framing cannot produce — under C4 as written, longer is always better.

Commonplace has already reached (2) independently and empirically:
[description-length-optimization](../description-length-optimization/README.md)
exists to measure description variants "across small result sets and large
scoped slices" against "pointer-context cost," and closes on "an explicit
result-set budget." So the delta is live work in this KB while the note that
anchors the cluster still states the monotone.

**One refinement that cuts against the easy story.** The transfer breaks on
economics, not on psychology. Pirolli's scent mechanism is spreading activation
over word associations whose "network strengths are estimated directly from
statistics obtained from large corpora of language." That is closer to what an
LLM does when it judges a link label than one would assume from "a study of
humans." The mechanism carries; the cost structure does not. A transfer argument
that waved at "humans are different from LLMs" would get the right conclusion
for the wrong reason.

## 5. Scope conditions the source carries

Recorded because a disposition that routes a reader to this source is
transferring these limits along with the claim.

- N = 14 Stanford students, six tasks; the modelled protocols are **four
  participants on two tasks** (Antz, City), chosen for near-median completion
  time and most intact data.
- Windows 98 and Internet Explorer, tasks drawn from a 1998 survey — a Web two
  decades removed from the one an agent reads.
- Text cues only. The source names non-text scent as its open problem: "The most
  significant current problem for the future development of the models concerns
  the analysis of non-text information scent cues."
- Time-boxed at 10 minutes to a hint and 15 to the answer, so the tail of
  genuinely hard foraging is truncated by design.

This is a small-N cognitive-modelling result, not a broad empirical law. It
settles what the *construct* is; it does not settle magnitudes for anything.

## 6. What the pipeline carried — and the prediction it falsified

The pipeline was run for real: `cp-skill-connect` from the parent, then an
isolated drafting worker under `draft-ingest-report.md`. Every factual claim in
the resulting ingest was checked against the snapshot — the χ² values, `189`
coded actions, `91%`/`93%` inter-coder agreement, the Tipster/AltaVista strength
estimation, the Gumbel choice rule, the PMI equivalence. All present, none
confabulated. **The ingest is faithful.**

It also read the source better than this hand pass did. The hand pass missed the
χ² results, the 3.25-versus-1.25 mode-switching figure, and Figure 1 as a prior
taxonomy of pointer forms.

**The workshop README's "no slot for any of the four extractions" is falsified as
written.** Measured against what actually landed:

| Needed | Predicted | What actually happened |
|---|---|---|
| Exact claims the source establishes | No slot | **Gap stands.** Summary and Extractable Value carry claim-level content, but there is no ledger — no enumerable list a later reader can cite an entry from |
| Population, costs, scope conditions | No slot; nearest is negative editorial framing | **Falsified.** Fully present: 14 participants, 4 protocols on 2 of 6 tasks, 189 actions, 1998–2003 Web, wall-clock cost, ten- and fifteen-minute hint scaffolding. The `scientific-paper` genre lens asks for exactly this |
| What transfers to LLM agents | No slot anywhere | **Falsified.** Explicit and per-mechanism: the structural claim transfers, the learned-strengths mechanism does not, because "our reader pays linear context per byte with no skim, and starts each session with no association strengths at all" |
| Which notes the source subsumes | Weak; duplicates instructed away | **Partly falsified.** Connect surfaced the overlap as its top edge and named the defect — the note "states the follow/skip model with no citation." The ingest repeated it and correctly withheld the verdict: "whether nearby notes are rediscoveries of this tradition is a separate disposition question this ingest does not settle" |

Two corrections follow.

**The isolation constraint was overstated.** The drafting worker cannot search
the corpus, but `cp-skill-connect` runs in the *parent* and can. The subsumption
signal reaches the worker through the connect report. The binding question is not
whether the worker can find overlap; it is whether connect's output and the
ingest's sections preserve it.

**The real gap is reliability, not capability.** Three of four extractions
landed, but only one of them (scope conditions) is actually *asked for* by the
contract. The transfer argument landed because this worker chose to write it. The
overlap survived even though `Connections Found` is instructed to "drop weak,
speculative, or duplicate edges" and `Extractable Value` is defined as "what is
new relative to the connection context" — a novelty polarity that points away
from recording that a claim is already held locally. The signal arrived *despite*
the contract's stated direction. That is fine for one careful run and not fine
for a corpus sweep.

## 7. The gap neither connect nor the ingest closed

Nothing in the pipeline evaluated the note's claims against the source. It
recorded that the note overlaps the source and cites nobody. It did not find that
**C4 is wrong by the source's own lights** — that the note merges estimate
quality with interaction cost where the source separates them, and that the
source's nearest test (Davison) fixes cue size rather than varying it.

That is structural, not an oversight by this worker. An ingest is source-centric
by construction: it asks what the source offers the KB. Asking whether a specific
local claim survives contact with the source is a different operation with a
different input — it needs the note's claim inventory, which nothing in the
pipeline builds.

So the division is:

- **overlap detection** — the pipeline does this well, unprompted;
- **contradiction detection** — the pipeline does not do this, and no field asks
  it to. It was the most valuable thing the hand pass produced.

## 8. Findings

1. The ingest contract carries more than predicted, but carries it *voluntarily*.
   The deliverable is not "add four fields"; it is "make the three that already
   land reliable, and add the one that does not."
2. A claim ledger is the missing artifact. Summary prose cannot be cited entry by
   entry, and a disposition that routes a reader to a source needs a claim it can
   point at, with its scope attached.
3. Scope conditions must attach to the claim, not to the source. This source
   settles what the construct *is* and settles no magnitudes; a ledger that drops
   that lets a later note inherit `r = .16` from 1998 Web prose as a general law.
4. The transfer argument is per-claim, not per-source. Here the structural claim
   transfers and the learned-strengths mechanism does not — within one source.
5. Contradiction detection needs the note's claim inventory as an input and
   therefore cannot live inside a source-centric ingest run.
6. `cp-skill-snapshot-web`'s model-mediated Markdown cleanup blocks on
   equation-heavy PDFs. See the capture note in section 2.

## 9. Handoff

To [literature-disposition](../literature-disposition/README.md): the overlap on
C1–C3 is now established against a read source rather than asserted from
resemblance, and C4 is a defect rather than a rediscovery. That is a different
input than the external critique assumed, and it does not settle the disposition
— a note whose central claim is wrong is not obviously a retirement candidate;
it may be a correction candidate.

Also handed over: connect found three artifacts carrying standing "survey is from
training data" TODOs inside this tradition — `links-README.md`,
`title-as-claim-enables-traversal-as-reasoning.md`, and
`information-value-is-observer-relative.md`. They are one batch, not three.

And connect **rejected** three cluster notes with reasons — `index-curation`
("nothing that discriminates *curated* from *generated* listings, which is the
note's entire claim"), `addressability-grain` ("the source assumes the target is
unknown, which is the premise the note discharges"), and
`fluid-resolution-switching` ("the source's switching is lateral, not vertical").
The external critique had guessed the latter two belonged to this tradition. A
reading contradicts it.
