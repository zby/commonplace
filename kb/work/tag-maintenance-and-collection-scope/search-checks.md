# Search checks before the tag audit

Baseline: `d47d4dce3`. These are expectations for searches, not proposed tag assignments. Keep paths relative to `kb/` below.

| Question | Expected result | Counterexample to exclude |
|---|---|---|
| Which artifacts are members of `evaluation`? | Include `reports/retained/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md`. | Exclude `sources/surgical-safety-checklist-haynes-2009.ingest.md`; it carries the tag for source discovery only. |
| Which sources address a topic? | Find the Haynes ingest for `evaluation` and `sources/hyra-2-next-step-for-auto-research.ingest.md` for `continual-learning`, even though the latter head declares `complete: true`. | Do not return theory notes, retained report copies or snapshots in this search. |
| What is a member of `architecture`? | Match the exact tag, not a substring. In a scratch example a line carrying only `commonplace-architecture` must not match. | Exclude `reference/proposals/archive/user-level-uv-tool-installation-for-commonplace-commands.md` even though its frontmatter says `architecture`. |
| Which theory notes should be considered for tagging? | Find `theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md` (`tags: []`) and `theory/language-models-for-bounded-judgments-form-an-emerging-category.md` (no tags field). | Do not list already-tagged notes, an intentionally untagged ADR or the maintenance instruction itself. |
| Who uses the Haynes ingest? | A cross-collection filename search finds `theory/methodological-and-computational-closure-track-different-changes.md`. | Do not require the dependent to carry `evaluation`. |

## Results

- **Exact membership.** The old five-root membership query returned 82 paths for `evaluation`. The collector returned 85: the three missing paths were retained reports. For `architecture` the old query returned 19 and the collector 17. Both extra paths were archived proposals. Separately, the old word-boundary expression matched a scratch line containing only `commonplace-architecture`; the new candidate expression did not. Do not attribute the two observed archive errors to the hyphen bug.
- **Source discovery.** The ingest-scoped inline-tag query returned the Haynes ingest for `evaluation` and two ingests for `continual-learning`, including Hyra. The complete head does not justify skipping the latter search. These are tagged candidates, not an exhaustive list of relevant sources.
- **Untagged notes.** The old command printed matching `tags:` lines: it happened to include the empty-list example but missed the field-absent example. The corrected recipe returned both, among 27 current theory artifacts of type `types/note.md` with no assigned tags. This is one eligible class, not an inventory of every collection or a recommendation to assign 27 tags.
- **Dependency control.** A fixed-string search for the Haynes ingest filename across KB Markdown found the theory note above; its tags do not include `evaluation`. The backlink search needed no change.

Ran both revised [maintenance recipes](../../instructions/maintain-curated-indexes.md) in the checkout and the [connect](../../instructions/cp-skill-connect/SKILL.md) candidate pipeline against the source destination. The next check is editorial: read a head, a clear member and a plausible non-member before deciding whether a placement or the head's wording needs to change.
