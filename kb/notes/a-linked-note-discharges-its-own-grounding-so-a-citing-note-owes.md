---
description: "A cited source imposes a grounding obligation; a claim-titled note that already passed its own grounding review imposes only a representation obligation — with the preconditions that keep the distinction and why it is not a paraphrase ledger"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance, links, evaluation]
---

# A linked note discharges its own grounding, so a citing note owes representation, not re-grounding

A note's outbound links do not all impose the same obligation. A cited source
and a linked note differ in what the citing note must be checked for, and only
one of the two obligations is a grounding obligation.

A cited source is raw material. It asserts nothing in the knowledge base's own
terms: the citing note asserts what the source supports, and a grounding check
exists to test that assertion by locating the supporting passage and judging
whether it carries the claim. Nothing about the source bounds that work — a
source has no title stating what it claims, and the passage may be anywhere in
it. The whole cost of establishing the link falls on the citing note's review.

A linked note arrives as a premise carrying its own certificate. Since
[its title states its claim](./title-as-claim-enables-traversal-as-reasoning.md),
the citing note can invoke it by name and a reader can tell from a title and a
paragraph whether that is the claim being relied on. It has passed its own
checks, including its own grounding review against its own sources. Its
grounding is a step already discharged, at its own review, against evidence the
citing note never has to open. What remains is a different obligation:
**representation** — that the claim invoked is the claim the linked note makes,
at the scope the linked note makes it. That check reads a title and an opening
paragraph instead of searching a document, and it is separable enough to run as
its own criterion. Commonplace runs it as two, on the citing note's own prose:
[concept attribution](../instructions/review-gates/sentence/concept-attribution.md),
for sentences that identify a concept here with a concept there, and
[misleading link text](../instructions/review-gates/sentence/misleading-link-text.md),
for link text that promises what the target does not say.

So a linked note is not free; it is charged to a different check. The
consequence for the graph is what makes traversal worth anything: a path
through claim-titled notes is an argument in which each step was checked once,
where it was made. Traversal composes inferences without recomposing their
evidence.

## Why this is not the paraphrase-ledger mistake

A linked note sits between the citing note and the sources, which is the shape
of an arrangement already rejected elsewhere. Commonplace declined to make a
ledger of paraphrased source claims the grounding surface for notes, because
[checking a note against a paraphrase that was itself checked against the
source is two semantic hops over one piece of evidence](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md),
and rewording at either hop can change the proposition. If two hops condemn the
ledger, why not the linked note?

Because a ledger paraphrase *stands in for* the source. It exists to be checked
instead of the source, over the same proposition; the second hop cannot recover
what the first one lost, and the intermediate has no claim of its own to be
right or wrong about. A linked note does not stand in for its sources. It
asserts a distinct proposition, which its own sources support at its own
grounding review, and the citing note relies on that proposition rather than on
the sources behind it. The two hops range over different propositions, each
checked where it lives. The count of hops is not the diagnostic; whether the
hops range over the same proposition is.

## Why the asymmetry is load-bearing

The distinction does practical work wherever a knowledge base bounds grounding
review on the artifact side and states the bound as a count of links, because
the same numeric bound is affordable or ruinous depending on which obligation
it counts. In Commonplace's `kb/notes/` collection at 344 notes, eight cite
more than five sources, so a bound of five stated in *sources* costs eight
notes. Counting every distinct linked artifact alike, the median offer across
337 measured targets was seven, so a bound of five stated in *artifacts* would
put more than half the corpus in violation. A separate claim — that [a note
is an atomic step relative to the check that reads it](./a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — depends on the exemption holding,
which is why the asymmetry has to be argued rather than assumed.

## Scope

The exemption holds only while three preconditions do, and where they fail the
honest reading is that the linked note has become a source.

- **Linked notes must actually pass their own grounding checks.** An ungrounded
  premise imports its debt to every note that cites it, and the citing note's
  own review sees nothing wrong.
- **Titles must actually be claims.** A topic-titled target offers nothing a
  representation check can test without opening it, at which point the check
  costs what a source costs.
- **The representation check must actually run.** It is cheap, not free, and no
  count of links detects its failure: in a paired assay of grounding reviews,
  one FAIL was a note attributing a broader mechanism to a linked artifact that
  explicitly disclaimed it.

The claim is about what a citing note owes its targets, not about what a
reviewer can afford in one pass. It says nothing about how large the checks
themselves may be, and nothing about sources cited without a bounded quoted
passage.

## Open Questions

- Is the representation check itself well bounded, or is it where the same
  problem reappears in smaller form? Reading a title and an opening paragraph
  is cheap per target, but nothing here establishes how many targets one pass
  can represent faithfully.
- Does a chain of representation checks degrade? Each step is checked once at
  its own review, but a long path's soundness is the conjunction of many
  independently checked steps, and no measurement here bears on that
  conjunction.

---

Relevant Notes:

- [A note is an atomic step relative to the check that reads it](./a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — extends: the artifact-side bound whose source-counting unit this exemption makes affordable
- [A five-link cap missed four grounding findings in twelve reviews](./evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — evidenced-by: supplies the misattribution FAIL that shows a representation failure no link count catches
- [Descriptive link labels may supply the self-sufficiency a reconstruction gate would check](./descriptive-link-labels-may-supply-claim-self-sufficiency.md) — evidenced-by: its label-ablation test attributes claim self-sufficiency to premises carried in the citing note's body, which is the text a representation check reads
- [079-Grounding reviews budget sixteen distinct linked artifacts](../reference/adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — evidenced-by: records the corpus measurement — median seven distinct artifacts over 337 targets — that makes the source-versus-artifact counting difference load-bearing
