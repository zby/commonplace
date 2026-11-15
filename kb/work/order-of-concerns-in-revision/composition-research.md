# Composition research: Purdue ingest and paper-access gaps

## Outcome

Purdue OWL was ingested on 2026-11-13 through a fresh delegated
`openai/gpt-6.1-sol` drafter. The ingest passed the handoff check, was published
through the publish command, and passed final validation. Both connection
passes completed and validated. Faigley–Witte and Sommers remain access gaps;
the writing-centre guidance does not replace either composition study.

The initial launch failed with `Unknown agent: "worker". Available agents:
none.` This was an agent lookup failure in the default user scope, **not**
evidence that workers were unavailable. The parent agent supplied the correction:
`agent: commonplace-worker`, `agentScope: project`, repository-root `cwd`,
and `model: openai/gpt-6.1-sol`. That launch succeeded. No agent CLI,
installation, local drafting fallback, or replacement model was used.

The occasion fixed before source reading was:

> How should Commonplace order revision concerns, and does ordering by what a change invalidates differ from ordering by degrees of freedom?

Scope: composition research and writing-centre terminology only. The separate
editing/planning investigation is not assessed or changed here.

## First priority: Faigley and Witte

Bibliographic identity located, **not ingested**:

- Lester Faigley and Stephen Witte, “Analyzing Revision,” *College Composition
  and Communication* 32(4), December 1981, pp. 400–414.
- [JSTOR record](https://www.jstor.org/stable/356602).
- [Current NCTE record](https://publicationsncte.org/content/journals/10.58680/ccc198115887).
- DOI identifiers returned by bibliographic services:
  `10.2307/356602` and `10.58680/ccc198115887`.
- Identity checked using the
  [Crossref bibliographic query](https://api.crossref.org/works?query.bibliographic=Faigley%20Witte%20Analyzing%20Revision&rows=2)
  and [OpenAlex DOI lookup](https://api.openalex.org/works/https://doi.org/10.2307/356602).
  These are discovery metadata, not primary-paper evidence.

Access limitations:

- JSTOR's record returned a “Client Challenge,” not the article.
- The ordinary [JSTOR PDF URL](https://www.jstor.org/stable/pdf/356602.pdf)
  returned HTML rather than a PDF; `pdfinfo` confirmed it was not readable as
  a PDF. No snapshot was made from that response.
- NCTE returned HTTP 403.
- OpenAlex listed the publisher DOI locations but no open PDF location.
- Google and DuckDuckGo discovery returned script/bot challenges; Bing
  results were empty or unrelated to the query. Brave returned HTTP 429;
  Yahoo retrieval failed. These did not establish another paper location.
- The apparent author-site root returned a generic Digital Writing and
  Research Lab page, not the paper.

The workshop's recalled surface/text-base distinction remains an unchecked
lead in this run. It is not promoted here into a source finding. In
particular, this run establishes neither the paper's exact classification
test nor any revision-order prescription from it.

## Authorized fallback: Sommers

Bibliographic identity located, **not ingested**:

- Nancy Sommers, “Revision Strategies of Student Writers and Experienced
  Adult Writers” (1980).
- [JSTOR DOI](https://doi.org/10.2307/356588).
- [Current NCTE record](https://publicationsncte.org/content/journals/10.58680/ccc198015930).
- [OpenAlex lookup](https://api.openalex.org/works/https://doi.org/10.2307/356588)
  confirmed the title and supplied the current NCTE identifier
  `10.58680/ccc198015930`, but no open PDF location.

NCTE returned HTTP 403. A Harvard Writing Project publications-page probe
also returned HTTP 403. A CSUN composition-process directory probe returned
HTTP 403. An exploratory University of Washington URL resolved to a different
handout and was rejected. No complete fallback paper was obtained.

**Gap:** neither a faithful Faigley–Witte capture nor a faithful Sommers
fallback capture is available from this run. Bibliographic metadata and
recollections cannot replace either primary source. No claim about student
versus experienced writers, or about the order of their revisions, is
asserted on this evidence.

## Writing-centre acquisition

**Snapshot saved:**
`kb/sources/.snapshots/purdue-higher-order-lower-order-concerns.md`

SHA-256 of the exact Markdown bytes:
`6b53eb2ba265e7a57f404dccc45bd23a5bec40b44a52b44058bc0e14e9aae06d`

- Source: [Purdue OWL: Higher Order Concerns (HOCs) and Lower Order Concerns (LOCs)](https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html).
- Source attribution shown on page: The Writing Lab & The OWL at Purdue and
  Purdue University. No named individual author was established.
- Capture date: 2026-11-13; method: `trafilatura`; scope: `full-source` for the
  handout's main content. The private snapshot retains the legal notice
  included by extraction. No full external copy is placed in this workshop.
- The canonical URL initially yielded unrelated Purdue homepage content.
  Purdue's own [sitemap](https://owl.purdue.edu/sitemap.xml) independently
  listed the canonical handout URL. A subsequent ordinary request with
  `?source=workshop` recovered the titled handout; extractor metadata
  identified the canonical URL without the query string.
- Capture-time inspection found substantive handout text rather than a shell.
  Capture fidelity was checked by byte-copy assembly and checksum. The
  unchanged capture subsequently received fresh delegated ingest analysis.
- The page's visible copyright range was 1995–2018. That range is not an
  established publication date or evidence that Purdue coined the terms.

**Terminology provenance: unresolved.** Locating a contemporary institutional
handout does not establish the first use of higher-order/lower-order
concerns. No historical priority is assigned here.

Other probes did not supply the commissioned primary definition: Wisconsin,
Nevada Reno and several guessed resource paths returned HTTP 404. Retrieved
George Mason revision/feedback pages and UNC's editing/proofreading page were
not substituted for the requested explicit definition source. They were not
ingested or retained as snapshots.

## Workflow and verification record

- Read the workshop framing and `kb/work/COLLECTION.md`; this result is
  frontmatter-free `text`, permitted by the workshop contract and checked
  against `kb/types/text.md`.
- Read `cp-skill-snapshot-web`, `cp-skill-ingest`, `cp-skill-connect`, the
  snapshot and connect-report types, and the sources collection contract.
- Searched existing source files and hidden snapshots for Faigley, Witte,
  Sommers and the terminology. No existing ingest for either commissioned
  paper or the Purdue canonical URL was found. One unrelated source search
  hit was not treated as a duplicate.
- Verified that private snapshot and temporary capture locations are ignored.
- Downloads used literal, standalone `curl -fsSL -o` invocations. Rejected
  responses were not represented as primary-source captures. Both temporary
  download/extraction directories were removed after the run.
- Opened the Purdue handoff with the occasion above and `--created-snapshot`.
  Record: `kb/reports/state/ingest/purdue-higher-order-lower-order-concerns/handoff.yaml`.
- The initial worker lookup failed before execution. Closed that initial
  handoff without publication. On the parent agent's correction, reopened it
  through `prepare` with the same occasion and unchanged paired snapshot.
- Sequential project-scoped fresh Sol workers completed snapshot connection
  discovery, ingest drafting, and post-ingest connection discovery. The
  drafter received only the standalone drafting instruction and fixed inputs;
  it wrote the candidate, not the published ingest. No local repair or
  replacement drafter was needed.
- Parent verification returned `HANDOFF CLEAN` for the candidate. Published
  through `commonplace-ingest-handoff publish`, not a direct source-file write.
- **Validation:** the published ingest and both connect reports each passed
  `commonplace-validate` with zero failures and zero warnings. This workshop
  record also passed validation. The snapshot SHA-256 is unchanged.
- **Grounding boundary:** the accepted ingest has the canonical empty Quotes
  section. This record summarizes its source account and analytical advice
  for discussion; it is not retained source support ready for library edits.
  A future source-dependent library change needs the grounding workflow.
- No existing theory, proposal, index or other worker's file was changed; no
  commit was made. Concurrent changes by others were left alone.

## Accepted ingest: findings and evidence boundary

Saved analysis: [Purdue OWL ingest](../../sources/purdue-higher-order-lower-order-concerns.ingest.md).
The following source account is the accepted drafter's reconstruction, not a
set of retained quotations:

- **Default priority:** higher-order concerns include thesis/focus,
  audience/purpose, organization and development. Lower-order concerns
  include sentence structure, punctuation, word choice and spelling.
- **Not an invariant sequence:** the page allows movement between levels.
  It recommends early lower-order repair when surface errors prevent readers
  from reaching the thesis. Thus its advice cannot support an unconditional
  prohibition on surface-first work.
- **Evidence kind:** institutional writing advice, not an experiment comparing
  schedules. No measured advantage for this ordering, agent-editing result,
  option-count calculation or downstream-invalidation model is supplied.
- **Terminology history:** the page demonstrates an institutional use of the
  vocabulary, not its invention or earliest use. Priority remains unresolved.

The ingest separates these source claims from its Commonplace analysis:

1. Ordering by remaining viable alternatives and ordering by discarded-edit
   risk are logically distinct criteria. A thesis can have many viable
   formulations while changes to it make substantial sentence work obsolete.
   That is a local counterexample to identifying the criteria, **not a Purdue
   finding or a comparative effectiveness result**.
2. Purdue puts organization among higher-order concerns. The local proposal's
   classification of flow as lower-order therefore needs an explicit mapping;
   matching labels do not establish matching categories.
3. Existence, boundary and placement checks are Commonplace extensions.
   Purdue does not supply those categories or establish that its advice
   generalizes to every revisable artifact.

## Final connection results

Both reports are generated discovery state, not library changes:

- Pre-ingest: `kb/reports/state/connect/sources/purdue-higher-order-lower-order-concerns.connect.md`.
- Post-ingest: `kb/reports/state/connect/sources/purdue-higher-order-lower-order-concerns.ingest.connect.md`.

Read the post-ingest report's Bidirectional Candidates and Reverse-edge
Candidates directly. It recommends:

- The improvement-procedure proposal → Purdue ingest, `evidenced-by`, to
  qualify borrowed categories and conditional priority. This does **not**
  evidence the proposal's discarded-work rationale.
- The low-degree-of-freedom note → Purdue ingest, `see-also`, to distinguish
  option preservation from concern priority and invalidation.
- A bidirectional `compares-with` connection between the Purdue and JPL
  ingests, distinguishing revision priority from commissioned editing scope.
  This is a discovery recommendation; the separate JPL investigation was not
  revised here.

No recommended inbound or new JPL comparison links were authored. The accepted
Purdue ingest contains its own authorized outbound links. Report validation
passed; these candidate recommendations still require target-side judgment
and source grounding before any library edit.

## Recommendations for discussion only

The accepted ingest recommends revising the proposal's default composition
to distinguish invalidation from option-count ordering, map organization and
flow explicitly, and preserve the reader-access exception. That is the
immediate discussion target, not an authorized edit in this run.

For the existing-note-versus-new-note decision, the present evidence favors
keeping the two criteria distinct rather than claiming Purdue derives one
from the other. A bounded comparison in the existing
[low-degree-of-freedom note](../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md)
could prevent conflation. A separate invalidation-order note would need its
own explanatory claim, conditions and checked support; this writing-centre
page does not establish that general theory. Its usefulness should be judged
against the other workshop findings rather than inferred merely from a
second terminology source.

The [procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)
can cite Purdue as a conditional writing-practice precedent only after the
needed source passages are grounded. Do not present the page as the source
of the vocabulary, as evidence of agent performance, or as proof of the
invalidation mechanism. Do not register a historical-origin claim. The
Faigley–Witte/Sommers acquisition gap remains material; further failed
acquisition attempts were not made on resumption, per the parent agent's bounded follow-up.
