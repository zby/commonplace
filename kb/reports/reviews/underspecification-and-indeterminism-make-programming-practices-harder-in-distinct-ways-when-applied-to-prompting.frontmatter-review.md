<!-- REVIEW-METADATA
note-path: kb/notes/underspecification-and-indeterminism-make-programming-practices-harder-in-distinct-ways-when-applied-to-prompting.md
last-full-review-note-sha: c78e69a4a7e227051e53834043f9dad574d9e522
last-full-review-note-commit: 8155ada39cf93a9f62e3baa54e38ae42663d9b5a
last-full-review-at: 2026-03-25T09:26:42+01:00
last-accepted-note-sha: c78e69a4a7e227051e53834043f9dad574d9e522
last-accepted-note-commit: 8155ada39cf93a9f62e3baa54e38ae42663d9b5a
last-accepted-at: 2026-03-25T09:26:42+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: underspecification-and-indeterminism-make-programming-practices-harder-in-distinct-ways-when-applied-to-prompting.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "Programming practices — typing, testing, progressive compilation, version control — apply to LLM prompting and knowledge systems, with semantic underspecification and execution indeterminism making some practices harder in distinct ways" enumerates which practices transfer and names the two phenomena, but "making some practices harder in distinct ways" restates the title. The description adds no mechanism for HOW the difficulties differ. The note's core analytical contribution is the specific distinction: indeterminism requires statistical testing over distributions while underspecification requires structural analysis of the spec itself (doubling test runs vs. doubling test targets). Leading with that mechanism would discriminate this note from the several related notes that also discuss underspecification and indeterminism.
  Recommendation: Replace the tail clause with the specific mechanism, e.g.: "...indeterminism forces statistical testing over distributions; underspecification forces testing the spec itself, not just outputs — different techniques for different failure sources."

INFO:
- [Title-body alignment] The title frames the note as being about how two phenomena make practices harder, but the body is broader: it catalogues five practices, explains why they transfer, draws a comparison to legal drafting, and notes that agent statelessness turns pedagogical convenience into architectural necessity. The analytical core (the "hard cases" section) matches the title well, but the note's actual scope is "programming practices applied to prompting — survey, transfer rationale, and where two phenomena create friction." The title accurately captures the distinguishing insight but understates the note's range.

CLEAN:
- [Title composability] "since underspecification and indeterminism make programming practices harder in distinct ways when applied to prompting" reads naturally as a sentence fragment in linking prose. The title is long (103 characters) but grammatically functional as a clause.
- [Claim strength] The claim that the two phenomena create difficulties "in distinct ways" is specific and contestable — someone could argue the effects aren't truly separable, or that the difficulties mirror traditional programming challenges rather than being novel. The note commits to a particular decomposition (indeterminism vs. underspecification) that does real analytical work.

Overall: 1 warning, 1 info
===
