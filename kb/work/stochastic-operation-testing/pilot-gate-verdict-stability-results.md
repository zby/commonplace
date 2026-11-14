# Pilot results: gate verdict stability on unchanged text

Run 2026-11-14 under the [protocol](./pilot-gate-verdict-stability.md). Raw state is retained in `kb/reports/state/stochastic-operation-testing/gate-verdict-stability-20261114/`.

## Outcome

Four trials reviewed the same 44 (note, criterion) pairs on byte-identical inputs. 33 pairs gave the same outcome in all four trials: 29 always passed and 4 always warned. 11 pairs changed outcome at least once. They are spread over every bundle except frontmatter, plus both conformance lenses.

All four stably warning pairs repeated the same core finding in every trial. Their extra findings varied. Among unstable pairs, the warnings that did occur mostly named the same passage and defect as each other.

The sweep before the first run does not count as an observation. Its inputs are identical, but it ran on a different model (Opus, not the default Sonnet profile). A fifth trial would have replaced it, but it would have exceeded the hard cap, so it was not run.

## Accounting

| Trial | Run directory | Launches | Answered | Infra failures | Retries | Problem files | Cost (USD) |
|---|---|---|---|---|---|---|---|
| verification | 20261114T094033Z (one pair) | 1 | 1 | 0 | 0 | 0 | 0.11 |
| 1 | 20261114T094111Z | 44 | 44 | 0 | 0 | 0 | 5.26 |
| 2 | 20261114T094111Z | 44 | 44 | 0 | 0 | 0 | 5.15 |
| 3 | 20261114T094459Z | 44 | 44 | 0 | 0 | 0 | 5.21 |
| 4 | 20261114T094459Z | 44 | 44 | 0 | 0 | 0 | 5.23 |

Total: 177 launches, about 20.95 USD. Every pair has four answered trial observations, so no pair has a smaller denominator. Every result reports model `claude-sonnet-5-5`. Every run's checkout guard was clean. The verification launch only checked that the command works in a worktree; its pass is not counted as an observation.

## The prior sweep

Run `20261112T094905Z` in the main checkout is the only sweep of this note path before 07:26Z. It holds 44 launches, one per pair, all answered (36 pass, 8 warn). For all 44 pairs, its note input and criterion input are byte-identical to the trial inputs.

It still does not qualify as an observation:

- **Different model.** It ran with `--profile opus` (results report `claude-opus-5-5`). The trials used the default profile `sonnet`.
- **Different prompt for two pairs.** Its prompt wrapper for the type and collection pairs differs from the trials' wrapper. The trials ran HEAD code, which carries commit `b74423842`.

Its outcomes appear below in a reference column only.

## Per-pair outcomes

T1 to T4 are the trials. "Prior" is the Opus sweep and is not counted. "Stable" covers T1 to T4 only.

| Criterion | T1 | T2 | T3 | T4 | Prior (Opus) | Stable |
|---|---|---|---|---|---|---|
| accessibility/jargon-persistence | warn | pass | pass | pass | pass | no |
| accessibility/notation-opacity | pass | pass | pass | pass | pass | yes |
| accessibility/undefined-terms | warn | warn | pass | warn | warn | no |
| accessibility/unidentified-references | warn | warn | warn | warn | pass | yes |
| complexity/claim-to-section-ratio | pass | pass | pass | pass | pass | yes |
| complexity/connection-inflation | warn | warn | warn | pass | pass | no |
| complexity/could-be-a-paragraph | pass | pass | pass | pass | pass | yes |
| complexity/framework-decoration | pass | pass | pass | pass | pass | yes |
| frontmatter/claim-strength | pass | pass | pass | pass | pass | yes |
| frontmatter/description-discrimination | pass | pass | pass | pass | pass | yes |
| frontmatter/title-as-claim | pass | pass | pass | pass | pass | yes |
| frontmatter/title-body-alignment | pass | pass | pass | pass | pass | yes |
| frontmatter/title-composability | pass | pass | pass | pass | pass | yes |
| kb/theory/COLLECTION (collection lens) | pass | warn | warn | warn | warn | no |
| kb/types/note (type lens) | pass | warn | pass | pass | pass | no |
| prose/anthropomorphic-framing | pass | pass | pass | pass | pass | yes |
| prose/bridge-paragraph-duplication | pass | pass | pass | pass | pass | yes |
| prose/confidence-miscalibration | warn | warn | warn | warn | pass | yes |
| prose/mannered-prose | pass | pass | pass | pass | pass | yes |
| prose/orphan-references | pass | pass | pass | pass | pass | yes |
| prose/proportion-mismatch | warn | warn | warn | warn | warn | yes |
| prose/pseudo-formalism | pass | pass | pass | pass | pass | yes |
| prose/redundant-restatement | pass | pass | pass | pass | pass | yes |
| prose/source-residue | pass | pass | pass | warn | warn | no |
| prose/unbridged-cross-domain | pass | pass | pass | pass | pass | yes |
| semantic/completeness-boundary-cases | pass | pass | pass | pass | pass | yes |
| semantic/conceptual-role-conflation | pass | pass | pass | pass | warn | yes |
| semantic/epistemic-status-blur | pass | pass | pass | pass | pass | yes |
| semantic/explanatory-reach | pass | pass | pass | pass | pass | yes |
| semantic/grounding-alignment | pass | warn | warn | pass | warn | no |
| semantic/internal-consistency | pass | pass | pass | pass | pass | yes |
| semantic/load-bearing-qualifiers | pass | pass | pass | pass | pass | yes |
| semantic/underspecified-assertions | pass | pass | pass | pass | pass | yes |
| semantic/unearned-generality | pass | pass | pass | pass | pass | yes |
| semantic/unwarranted-scope | pass | pass | pass | pass | pass | yes |
| sentence/clause-packing | warn | warn | warn | warn | warn | yes |
| sentence/concept-attribution | pass | pass | pass | pass | pass | yes |
| sentence/framing-mismatch | warn | pass | pass | warn | pass | no |
| sentence/misleading-link-text | pass | pass | pass | pass | pass | yes |
| sentence/parsing-ambiguity | pass | warn | pass | pass | warn | no |
| sentence/stock-phrases | warn | pass | pass | warn | pass | no |
| structural/bullet-capitalization | pass | pass | pass | pass | pass | yes |
| structural/compound-bullet | pass | warn | pass | pass | pass | no |
| structural/general-before-specific | pass | pass | pass | pass | pass | yes |

No trial returned FAIL. Five unstable pairs warned in only one trial: jargon-persistence, type lens, source-residue, parsing-ambiguity and compound-bullet. Six warned in two or three trials.

## Finding agreement for pairs with two or more warnings

I matched findings by reading each warning review. A match means the same quoted passage and the same named defect. Severity labels vary between runs of one gate (`warn`, `WARN`, `low`, `minor`, `medium`), so I compared all findings in a warning review, not only those labelled warn. Results are in `trial-N/review/results/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md/<criterion>.md`.

### Stable warning pairs (4 of 4 warn)

- **accessibility/unidentified-references: core agreement.** All four flag "Commonplace" as never identified ("[Commonplace's collections](...) are one application"). All four also flag "Commonplace's ADR 003 is the historical case..." for coming before its gloss. T2 and T3 add "superseded by [ADR 025]" with only a link. T4 adds the connect skill being named before its gloss.
- **prose/confidence-miscalibration: core agreement.** All four flag "the gap is structural, not marginal" and "you can't reliably detect redundancy between two notes from their descriptions alone". T1, T2 and T4 add "effectively lost to operations that work at index resolution". T3 and T4 add "This is where areas are most productive". T2, T3 and T4 add the assertive regime wording ("Orientation requires search...").
- **prose/proportion-mismatch: full agreement.** All four name the same two defects. First, the "Library/workshop separation keeps index-scan discovery viable" section is overdeveloped with ADR 003/025 history. Second, the core regimes are thin, with the ~40-note heuristic as the only concrete anchor.
- **sentence/clause-packing: core agreement.** All four flag "In the middle regime, they also serve as the compressed representation through which the agent orients and plans, so a note with a poor description is effectively lost...". T3 and T4 add the ADR 003 sentence with the dash aside ("ADR 003 explicitly identified this as a scaling constraint — ..."). T4 also adds the opening sentence and the `WRITING.md` sentence.

### Unstable pairs with two or three warnings

- **accessibility/undefined-terms (warn in T1, T2, T4): core agreement.** All three flag the same three terms: "per-window degradation" (link text without a gloss), "index resolution" / "full-text resolution", and "portioned loading" / "sub-passes". T1 and T4 add the ADR 003 or candidate-discovery gloss order. T4 adds "text-contract properties".
- **complexity/connection-inflation (warn in T1, T2, T3): partial agreement.** All three flag the quality-scores footer entry for repeating the body. T1 and T3 name the same three entries: ADR 003, workshop-layer and quality-scores. T2 names the areas-note and quality-scores entries instead, and it calls them non-failing.
- **kb/theory/COLLECTION (warn in T2, T3, T4): core agreement.** All three flag body composability, because the library/workshop section carries ADR 003/025 history. All three also flag the `WRITING.md` ~40-note residue. The third concern differs. T3 and T4 say the claim mode is undeclared. T2 instead says the library/workshop claim lacks stated conditions, and it flags inline links without a connective.
- **semantic/grounding-alignment (warn in T2, T3): agreement.** Both flag the citation of the context-efficiency note for "per-window degradation caps how many note bodies an agent can usefully reason about". They say that note does not claim such a cap.
- **sentence/framing-mismatch (warn in T1, T4): agreement.** Both flag the heading "Descriptions become load-bearing in the middle regime". They say its mechanism also holds above the index boundary. T1 adds "Parent areas ... serve collections in the middle regime".
- **sentence/stock-phrases (warn in T1, T4): agreement.** Both flag "This means the two operations hit different context limits, which creates distinct operational regimes." T1 adds "ADR 003's scaling strategy is implicitly a response to the index boundary:".

In this pilot, then, outcome disagreement was more common than finding disagreement. When a gate warned more than once, it usually named the same passage. Whether it warned at all varied. The listed extra findings also varied between trials.

## Unstable pairs per gate

| Bundle or lens | Pairs | Unstable |
|---|---|---|
| accessibility | 4 | 2 (jargon-persistence, undefined-terms) |
| complexity | 4 | 1 (connection-inflation) |
| frontmatter | 5 | 0 |
| prose | 10 | 1 (source-residue) |
| semantic | 10 | 1 (grounding-alignment) |
| sentence | 6 | 3 (framing-mismatch, parsing-ambiguity, stock-phrases) |
| structural | 3 | 1 (compound-bullet) |
| type lens (kb/types/note) | 1 | 1 |
| collection lens (kb/theory/COLLECTION) | 1 | 1 |

## What was not controlled or verified

- **Hosted model.** The `sonnet` profile resolved to `claude-sonnet-5-5` in every result. The provider-side serving state is not observable.
- **Review code.** `commonplace-review` ran from the main checkout's editable install at HEAD `a9215100d`, not at the fixture commit. `src/` had no uncommitted edits. HEAD's prompt wrappers for the type and collection lenses differ from the fixture commit's (`b74423842`). Those two pairs were therefore judged under the current wrapper text, not the wrapper of the fixture's time.
- **Worker environment.** The workers loaded the worktree's project configuration plus the user-level Claude Code configuration, as the harness intends. User-level configuration was not pinned. `COMMONPLACE_REVIEW_MODEL=opus-4-6` was set in the environment; no code in `src/` reads it.
- **Concurrency.** Two trials ran at once. Each used the command's default worker count. No launch failed.
- **Worker reads.** The workers could read the rest of the worktree, such as linked notes. That context is fixed by the commit but is not part of the hashed inputs. I checked the file paths read only for the verification launch.
- **Cost.** Cost is each launch's `total_cost_usd` as the harness reported it, not a billing record.
- **Scope of the evidence.** This is one note, selected because its re-review looked unstable. These counts estimate nothing about the collection, and they say nothing about whether any verdict is correct.
