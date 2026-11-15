# Editing and planning research

## Outcome

2026-11-13: **one ingest published**, with fresh Sol drafting and clean handoff
validation. Technical-editing acquisition is complete for the selected edition.
Planning acquisition remains blocked. No existing theory, proposal, index or
other worker file was edited; no commit was made.

Occasion fixed before reading sources:

> How should Commonplace order revision concerns, and does ordering by what a change invalidates differ from ordering by degrees of freedom?

Scope: technical editing and one primary planning precedent, at most two
ingests. Composition research and writing-centre sources belong to another
worker. This result is for discussion, not adoption of a library change.

## Source and acquisition

Published report: [The Levels of Edit, Second Edition](../../sources/levels-of-edit-1980.ingest.md).
Acquisition identity: Robert Van Buren and Mary Fran Buehler, January 1980,
JPL Publication 80-1. The acquisition also identified the March 1976 first
edition as SP 43-28; only the second edition was captured and ingested. No
edition comparison was performed.

- Download URL: https://ntrs.nasa.gov/api/citations/19800011701/downloads/19800011701.pdf
- Private snapshot path: `kb/sources/.snapshots/levels-of-edit-1980.md`
- Exact Markdown SHA-256: `1abdb131342c0ab5f117a727aeca8583e2033aa2d665cdaabe7c174d7b565710`
- Capture: `pdftotext`; all extracted bytes copied locally, full-source scope.
  The 33-page PDF has OCR noise, particularly in tables and some words. No
  model cleanup or full-source republication was performed. No DOI was found
  in the inspected document or PDF metadata.
- Duplicate search: `Van Buren|Buehler|ABSTRIPS|Sacerdoti|Levels of Edit|Stefik`
  across existing source ingests, relevant names across hidden snapshots, and
  the exact source URL. No matching existing ingest or capture was identified;
  incidental references were not treated as duplicates.

## Delegation, publication and validation

The first attempt used the wrong agent definition lookup and failed with
`Unknown agent: "worker". Available agents: none.` This was a dispatch error,
not evidence that delegation or Sol was unavailable. The initial handoff was
closed without publishing. On the parent agent's correction, `prepare` reopened
it against the same snapshot and occasion.

The successful fresh drafting launch used:

- `agent: commonplace-worker`
- `agentScope: project`
- `cwd: /home/zby/llm/commonplace`
- `model: openai/gpt-6.1-sol`

The drafting worker received only the standalone drafting instruction and
fixed inputs. The parent did not draft or repair the ingest. The worker and
parent both obtained **HANDOFF CLEAN**; `commonplace-ingest-handoff publish`
then published `kb/sources/levels-of-edit-1980.ingest.md`.

Operational record: `kb/reports/state/ingest/levels-of-edit-1980/handoff.yaml`.
The candidate and retained-quotes file remain beside it as workflow state.
Final standalone validation of the published ingest, both connect reports and
this research result returned **VALIDATION SUCCESS**, zero failures and zero
warnings for each artifact. The report's Quotes section remains canonically empty. No exact quotations
were added. Accepted analysis is not a substitute for retained source wording:
before a library change relies on JPL's specific statements, complete the
grounding workflow. This run does not authorize direct quote-pool mutation.

## Connection results

Pre-ingest report, completed locally:
`kb/reports/state/connect/sources/levels-of-edit-1980.connect.md`.
It validated with zero failures and warnings. Its historical dispatch flag
now records the recovery; it remains a pre-ingest discovery observation.

Post-ingest report, completed by a separate fresh Sol worker:
`kb/reports/state/connect/sources/levels-of-edit-1980.ingest.connect.md`.
The parent read its complete Bidirectional and Reverse-edge sections and
validated it independently. The source field is the published ingest path.

- **Bidirectional Candidates:** explicitly None.
- **Reverse-edge Candidates:** independently useful `see-also` links from the
  one-improvement proposal, the low-degree-of-freedom note and the
  author/executor note. Their reader needs are, respectively, distinguishing
  commissioned scope from invalidation order, distinguishing scope from
  option counts, and distinguishing detection from repair authority.
- **Additional outbound candidates:** comparison with the three-simplification-
  passes evidence note and the dynamic-variable-ordering CSP ingest.
- **Optional navigation:** a manually curated source entry at the
  goal-prioritization head, not generated membership or a tag assignment.

No suggested inbound, additional outbound or index edge was authored. The
published ingest itself contains its worker-authored comparisons to the three
main local targets. Connection discovery is complete, not pending.

## Discussion findings and recommendations

The accepted ingest's analysis recommends treating JPL as a comparison for
**commissioned edit scope**, not as proof of higher-order-first execution or
invalidation-based ordering. It also identifies detection versus repair scope
as a useful editorial comparison. These are the delegated report's analytical
results; its empty Quotes block means source-dependent library wording still
needs grounding. The report does not supply an empirical comparison of the
ordering rules.

Keep four questions distinct:

1. **Ordering:** which work happens first?
2. **Edit scope and commissioning:** which tasks are included or excluded?
3. **Decision ownership:** who may settle or authorize a change?
4. **Abstraction:** which details are temporarily omitted and how are they
   reinstated? The planning source needed to assess this precedent is absent.

The existing [low-degree-of-freedom note](../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md)
orders decisions by feasible-set size. The existing
[author/executor note](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md)
explicitly separates ownership from timing. The
[one-improvement proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)
orders claim/boundary/existence concerns before wording because the wording may
be discarded. These mechanisms are not interchangeable: many possible claim
choices can each replace the prose; a uniquely determined metadata value need
not discard it. This is target-side reasoning, not a result demonstrated by
JPL or an unread planning paper.

**Recommendation for discussion:** first clarify the proposal's ordering
rationale and its distinction from the existing feasible-set heuristic. Do not
use JPL's numbered levels as an attribution for that rationale. Keep a new note
on invalidation-based ordering as a candidate, not an automatic output: it must
explain a choice that the existing note does not already settle, with a worked
case where the criteria diverge. The post-ingest connect report likewise
prefers focused clarification over a note that merely restates the ingest.
The other worker's composition evidence and an accessible planning precedent
may change that disposition; neither has been assessed in this result.

No decision about new vocabulary, collision-ledger entries, or library changes
has been adopted. A later `cp-skill-connect` pass is appropriate for whichever
durable library artifact is selected.

## Planning acquisition gap

Priority target: Sacerdoti, *Planning in a hierarchy of abstraction spaces*
(1974). OpenAlex discovery returned DOI `10.1016/0004-3702(74)90026-5` and a
separate record pointing to
`http://elvex.ugr.es/decsai/iaio/doc/1974%20ABSTRIPS.pdf`.
These are discovery metadata, not verified primary-source content.

- HTTPS download at that host failed: `curl: (60) SSL certificate problem:
  unable to get local issuer certificate`.
- The discovered HTTP URL failed: `curl: (22) The requested URL returned
  error: 404`.
- Semantic Scholar's DOI lookup returned no open-access PDF URL.
- SRI and search-engine retrievals did not yield a usable primary PDF.

No Sacerdoti snapshot or ingest was created. Stefik was not substituted. The
parent agent permitted leaving this acquisition blocked on resumption.
All unique temporary download/extraction directories were removed. Full
external content remains only in the ignored snapshot.
