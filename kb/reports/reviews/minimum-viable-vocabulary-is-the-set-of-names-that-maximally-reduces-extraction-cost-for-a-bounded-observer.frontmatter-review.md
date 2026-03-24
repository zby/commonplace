<!-- REVIEW-METADATA
note-path: kb/notes/minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md
last-full-review-note-sha: b77523f2990522b492d5df6c46a681e1bbe455fe
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T20:56:02+01:00
last-accepted-note-sha: b77523f2990522b492d5df6c46a681e1bbe455fe
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T20:56:02+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md ===

Checks applied: 4

INFO:
- [Description discrimination] The description's first clause partially restates the title: "the vocabulary that, once acquired, maximally reduces a bounded observer's extraction cost for a domain" overlaps heavily with the title's own phrasing. The discriminating content -- the reframing origin ("minimum viable ontology") and the grounding claim ("grounds the pedagogical intuition of 'conceptual thresholds' in the KB's information-theoretic framework") -- is genuinely useful but shares space with the restatement. Trimming the restated portion would free characters for more discriminating detail (e.g., that two specific KB mechanisms -- naming-as-amortization and distillation -- do the grounding work).
  Recommendation: Consider tightening the first clause to something like "Reframes Kim's 'minimum viable ontology' as an optimization problem grounded in the KB's information-theoretic framework; naming amortizes discovery cost and distillation explains why the optimal set varies by observer." This drops the title echo and adds mechanism.

CLEAN:
- [Description discrimination] Despite the partial overlap noted above, the description does discriminate: it names the source concept being reframed ("minimum viable ontology," "conceptual thresholds") and the framework doing the grounding (information-theoretic). An agent seeing this among 5 results would know this note specifically regrounds a pedagogical intuition rather than, say, defining vocabulary selection criteria or proposing an algorithm.
- [Title composability] "since minimum viable vocabulary is the set of names that maximally reduces extraction cost for a bounded observer, we designed the glossary injection to..." reads as natural prose. The title is a complete clause that composes well in linking contexts.
- [Claim strength] The claim is specific and contestable. Someone could argue that vocabulary is not the right unit of extraction cost reduction (perhaps schemas or worked examples reduce extraction cost more effectively), or that the optimization framing mischaracterizes what is actually a satisficing problem. The claim does real work -- it is not a truism.
- [Title-body alignment] The body delivers what the title promises. It introduces the bounded observer's extraction gap, references Kim's concept, then grounds the claim via two mechanisms (naming amortizes discovery cost; distillation explains observer-relative variation). The open questions and testability discussion extend the title's claim without drifting from it.

Overall: 0 warnings, 1 info
===
