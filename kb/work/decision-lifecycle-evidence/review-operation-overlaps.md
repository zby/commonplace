# Overlaps among the review operations

## Purpose and status

The [one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)
treats review operations as one pool of atoms. Before the pool is unified,
the operator asked on 2026-11-14 for its duplications to be removed. This
file maps them. It is a reading of the criteria's texts, made by comparing
every failure mode and wrapper. It is not a measurement: no co-firing
rates were computed. The tables describe the pool before the changes
recorded under [what was done](#what-was-done-on-2026-11-14).

## The pool

| Family | Count | Form |
|---|---|---|
| Catalog gates in seven bundles | 43 | One failure mode and test each; pass, warn or fail |
| Type conformance | 1 per note | The type spec applied through a wrapper |
| Collection conformance | 1 per note | The collection contract applied through a wrapper |
| Compression bundle | 4 checks and a synthesis | Used by the full pass |
| Report methods | critique, composition friction, premise decomposition, connect | Open-ended reports |
| Higher-order check | 1, in calibration | Workshop wordings only |

## Three kinds of overlap

They need different remedies, so the map keeps them apart.

- **Same question, asked twice.** Two operations look for one failure. One
  of them can go, or they can merge.
- **One question at several scales.** A sentence gate, a passage gate and a
  note gate look at the same kind of defect at different sizes. These can
  stay, but each should say which scale is its own.
- **A whole-document check re-asking what a gate asks.** The type and
  collection checks apply an entire authoring text, so they re-judge things
  that dedicated gates already judge.

## Same question, asked twice

| Operations | The shared question | Suggested remedy |
|---|---|---|
| `prose/confidence-miscalibration` and `semantic/epistemic-status-blur` | Is a claim presented with more or less confidence than its support gives it? | Merge into the semantic gate, whose statement is the fuller one. |
| `prose/pseudo-formalism` and `complexity/framework-decoration` | Does a formal-looking device (notation, table, taxonomy) say more than a paragraph would? | Merge into one gate about formal devices that add nothing. |
| `prose/redundant-restatement` and `prose/bridge-paragraph-duplication` | Is the same content given twice at a section boundary? | Merge; the second is one position of the first. |
| `complexity/could-be-a-paragraph` and the higher-order check's parent-loss test | Does the note hold enough of its own to be a note? | Keep one. The question is about the note's existence, so it belongs to the higher-order check. |
| `frontmatter/title-body-alignment` and the higher-order check's title test | Does the body argue what the title says? | Already resolved on 2026-11-14: the test was dropped from the check. |
| `prose/proportion-mismatch` and the compression bundle's `detail-overhang` | Is space given to material out of proportion to its role? | The two state one defect from its two sides. Keep one when the pool is unified. |

## One question at several scales

| Question | Sentence | Passage | Note |
|---|---|---|---|
| Does the reader have to hold too much? | `sentence/clause-packing`, `sentence/parsing-ambiguity` | | `core-claim-obscured` (compression) |
| Is this earning its space? | `sentence/stock-phrases` | `marginal-value-redundancy`, `detail-overhang`, `branch-bloat` (compression) | `complexity/claim-to-section-ratio` |
| Does the claim reach further than its support? | `sentence/framing-mismatch` | `prose/unbridged-cross-domain`, `prose/source-residue` | `semantic/unwarranted-scope`, `semantic/unearned-generality`, the collection check's placement test |
| Does the linked note say what this text implies? | `sentence/concept-attribution` (every identity claim), `sentence/misleading-link-text` (every link) | | `semantic/grounding-alignment` |
| Could the claim be wrong? | | `semantic/completeness-boundary-cases`, `semantic/internal-consistency` | critique, premise decomposition, composition friction |

In the [first run](./first-run.md), `clause-packing` and `parsing-ambiguity`
warned on the same sentence, and three reviews remarked on the same
overlong section. Those are the only observed co-firings; the rest of this
table is read from the texts.

The three adversarial reports in the last row overlap most. Each tries to
break the note's central commitment by a different route. They are
experimental and run by hand or by the full pass, so they are left for
evidence to sort out.

## Whole-document checks re-asking gate questions

| What the wrapper asks | Dedicated gates that ask it |
|---|---|
| Collection check: title conventions. The theory contract states a composability test and a strength test. | `frontmatter/title-composability`, `frontmatter/claim-strength`, `frontmatter/title-as-claim` |
| Collection check: description conventions | `frontmatter/description-discrimination` |
| Type check: a description's routing quality and a title's claim shape, as the type-spec type describes the gate | The same four frontmatter gates |
| Collection check: outbound linking rules, including labels | `complexity/connection-inflation` in part; the link labels have no gate |
| Collection check: placement | `semantic/unwarranted-scope` and `prose/source-residue` in part; no gate asks placement itself |

So a title's claim shape is judged three times per note: by the type
check, by the collection check and by the frontmatter gates. The theory
contract even says the trait exists "so review gates check the promise",
which names the gates as the owner.

Two things in these wrappers have no other owner: placement, and the link
labels. They are what the collection check should keep.

## What was done on 2026-11-14

The operator asked for the plan to be executed. Reading the tests in full,
as the limits below require, changed two parts of it.

**Done.**

- Both conformance wrappers leave four title and description properties to
  the frontmatter gates and judge only the conventions their own document
  adds ([ADR 131](../../reference/adr/131-conformance-reviews-leave-titles-and-descriptions-to-their-gates.md)).
  A blanket exclusion was not used: types and collections add conventions
  that no gate knows, such as an instruction's trigger-shaped description.
- Three pairs of catalog gates were merged, and the catalog went from 43
  gates to 40: confidence miscalibration into epistemic status blur,
  pseudo-formalism into framework decoration, and bridge-paragraph
  duplication into redundant restatement.

**Not done, with the reason.**

- `sentence/concept-attribution` and `sentence/misleading-link-text` were
  not merged. [ADR 082](../../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md)
  gives them different units, every identity claim and every link, each
  with its own ladder. They belong in the second table, not the first.
- `semantic/unwarranted-scope` was not changed. The plan was to add a
  requirement to write the general claim instead of asserting it. The
  stored result for the prompting note shows the reviewer did write the
  claim, identified it as a derivation that does not depend on Commonplace,
  and passed it on that ground. `frontmatter/claim-strength` likewise
  argued that the title is contestable. The requirement would not have
  changed either verdict.
- The general-claim test was withdrawn from the fourth wording of the
  higher-order check, since its questions are those two gates'.
- The existence question stays in `complexity/could-be-a-paragraph` until
  the higher-order check is an atom.
- The compression bundle and the adversarial reports are untouched.

**What the prompting note actually shows.** Its general claim is real but
thin, and most of its text is an account of local decisions. One gate saw
this, `prose/proportion-mismatch`, and the collection review mentioned it
as an INFO finding. Nothing read those as a sign that the note might be
misplaced or need a split. The gap is in how a lower-order warning is
interpreted, not in a missing question.

## Agreed direction: retain diagnostic probes in review results

In the follow-up to the focused writing-tool comparison, the operator agreed
that review results should retain the concrete outputs of relevant diagnostic
probes. The purpose is to make the assessment inspectable, including why a
plausible finding was dismissed. This is an agreed design direction; criterion
instruction changes and their evaluation remain pending. It does not introduce
a new review type or change the live result schema.

The three probes are:

- **Flatten the rhetoric:** restate the passage's claim without its rhetorical
  cadence, preserving its qualifications; identify what substantive content
  remains and what the original form contributes.
- **State the implied relation:** restate the connection between claims
  explicitly, using a connective where appropriate. Identify whether the text
  supports that relation or whether supplying it would invent a connection.
- **Check both sides of a contrast:** identify the claims on each side and
  the contextual support for each. Nearby explanation can earn a contrast;
  support need not precede it. A supported contrast may still be replaceable
  under a separate editorial policy.

### What to retain

Use the explanatory body of the existing [review result](../../types/review-result.md),
not new schema fields. For each finding that relies on a probe, retain the
identified passage, the concrete paraphrase or relation, the support present
or missing, and the resulting assessment. A statement that the probe was
performed is not a substitute for its output. Keep the structured finding
focused on the passage and defect rather than duplicating the whole account.

Also retain consequential candidates that the probe cleared when they explain
an important boundary or a plausible false positive. Do not turn these into
warning findings. Do not mechanically apply all three probes to every passage
or record routine scanning. The owning criterion specifies which probes apply.

These are diagnostic accounts, not controlled experiments or proof that the
judgment is correct. Later evaluation must distinguish whether a probe faithfully
represents the passage and its context from whether the resulting finding is
correct. A persuasive account can fail either test.

### Ownership and next step

First assess these probes within the existing operations: literal paraphrase
in `prose/mannered-prose`, implicit inference in composition friction, and
materially unresolved meanings in `semantic/underspecified-assertions`. This
is a placement proposal, not a broadening of their failure modes. A clear but
unsupported inference is not semantic underspecification. Preserve composition
friction's report-only role; recording a probe does not grant verdict authority.

Read the current criteria and test retained cases before selecting instruction
changes. Add a gate only if those cases establish a coherent failure without
an existing owner. The [controlled-testing workshop](../stochastic-operation-testing/README.md)
owns evaluation of diagnostic fidelity and finding correctness; this entry owns
the agreed retention direction. No implementation or model trial is authorized
by this record.

## Limits

The map is a reading of failure modes, not of each gate's full test, and
two gates with similar failure modes may separate in their tests. Before a
merge, read both tests in full. A cheap check also exists and was not run:
count, over the stored results, how often two gates warn on the same note.
The local store holds results for few notes, so the count would be weak
evidence today.
