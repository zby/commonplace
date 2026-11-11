# The cache and state areas hold the same kind of record

## Question and provenance

On 2026-11-11 the operator asked whether there is a clear criterion for what
belongs in untracked report storage. They then doubted that the cache area
holds any real cache, meaning output that can be deterministically
regenerated. This file records the inventory, the comparison of how the
records are read, and the operator's conclusion.

Evidence: a listing of `kb/reports/cache/` and `kb/reports/state/` on
2026-11-11, the [reports collection contract](../../reports/COLLECTION.md),
and the readers of review results and connect reports found in
`src/commonplace/` and `kb/instructions/`. The one-off directories were
classified from their names, dates and file listings, not by reading each
file. Read counts are expectations from code and instructions. This checkout
had no review result files on that date, so none is measured.

## What the contract says

The contract separates the two areas by regeneration. A cache entry is "safe
to delete and regenerate from authoritative inputs", and deleting it "must
lose no unique evidence, decision, or unresolved state". State is local and
ignored, "but not disposable merely because it was generated". The cache
landing page adds that outputs carrying "unique judgments" belong in state.

The contract gives no criterion for the other boundary: when non-regenerable
material may stay machine-local instead of entering Git.

## What the cache area holds

| Contents | Deterministically regenerable? |
|---|---|
| `promotion-candidates.md` | Yes. `commonplace-promotion-candidates` is code with no model call. |
| `connect/` (804 files), `critique/`, `friction/`, `premise-decomposition/` | No. Each is a paid model judgment. A rerun costs money and returns a different report. |
| `reachability-article-creation-evidence/` (1,230 files), `x-likes/`, `agentic-memory-refresh/`, `agentic-analysis-reliability/`, `agentic-analysis-output-documents/` and smaller one-off directories | Probably not. They look like evidence collected by finished investigations, last written in September 2026. |
| `snapshot-web/` | Not applicable. It is a scratch directory for captures in progress. |

One output meets the contract's own test. A connect report is a unique
judgment in the landing page's wording, and it is the first producer that
page lists.

The state area has the matching drift. It holds `x-likes/`, `tag-placement/`
and a pilot directory that no current workflow reads, and it held the
abandoned review store until the landing page named it.

## How the two record kinds are read

A review result is read in two ways.

- **Header (input hashes and outcome), by code, many times.** Every
  `commonplace-review status`, every `commonplace-status --review`, every
  sweep and every full pass reads it, for as long as the note's watched parts
  and the criterion are unchanged. Each sweep read replaces one paid review.
- **Body (the reviewer's text), by an agent, once or never.** Nothing reads
  the body of a `pass`. The fixer reads the body of a `warn` or `fail` once.
  If it edits the note, the result goes stale and the next sweep overwrites
  it. No history is kept.

A connect report's body is read once, by the agent drafting an ingest or
improving a note. Nothing reads it afterwards.

| | Review result | Connect report |
|---|---|---|
| Body reads | 0 for `pass`, about 1 for `warn` or `fail` | about 1 |
| Validity check | Input hashes, read on every status and sweep | None: the report records its source path and a date |
| Effect of deletion | The pair is reviewed again at cost | None, unless connect runs again |
| Effect of an input change | Shown stale, then replaced | Silently outdated |

Both are paid judgments over named inputs. The review result records the
hashes of those inputs, so code can tell whether it still holds, and it is
reused. The connect report records no hash, so it is spent after one read.

## The operator's conclusion

The operator concluded on 2026-11-11 that this is not a real difference:
connect should have freshness accounting similar to review. If the two areas
cannot be told apart clearly, something should unify them.

After the input problem below was raised, the operator set the disposition
the same day:

- Freshness for connect reports is parked. It is a sensible feature, but it
  looks very hard to do in any reasonable way. It is not to be implemented
  now.
- Because the feature is sensible, the absence of freshness accounting on
  connect reports is a missing feature, not a property of the record kind.
  The difference between the two classes therefore remains not well defined.

Nothing is built or changed in the reports contract. The cache and state
areas keep their present contents and wording. The undefined boundary is an
open question for this workshop, not a defect to repair now.

## What a unification would have to settle

- **The inputs of a connect report.** A review's inputs are one note and one
  criterion. Connect searches every destination collection that the source's
  `COLLECTION.md` permits, so its real input is much of the KB. Hashing only
  the source says "the source changed since this report". It does not say
  that a new candidate target has appeared. Hashing the searched collections
  would make every report stale after any edit. Review meets the same problem
  in smaller form and answers it with a criterion's `watches:` declaration.
- **The earlier attempt.** [ADR 052](../../reference/adr/052-general-freshness-store-review-first-migration.md)
  built a general freshness mechanism in the store, with review as its first
  target. No second target was adopted, and [ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md)
  deleted it. The [collection-as-artifact freshness proposal](../../reference/proposals/collection-as-artifact-freshness.md)
  addresses the whole-collection input and now names a mechanism that no
  longer exists. A second attempt should say what differs this time. One
  candidate difference: a result file needs no registration, only hashes in
  its own frontmatter.
- **What decides retention once the kinds are one.** Candidates are the
  expected number of further reads and the cost of replacement. Neither is
  measured.
- **Spent evidence.** The one-off evidence directories fit neither area. Their
  choice is to delete or to retain. That is this workshop's existing question
  about consumed outputs.

## Evidence limits

One checkout was inspected on one day. The comparison covers review results
and connect reports; critique, friction and premise-decomposition reports
were counted but their readers were not traced. Whether source-only freshness
would make connect reports reused in practice is untested.
