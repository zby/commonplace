# ADR 089 was recorded as accepted before implementation

## Observation and provenance

Recorded on 2026-09-25 while opening this workshop. The operator identified
the latest ADR as already present in the ADR directory while implementation
was only starting. They also reported that agents often make this mistake:
the ADR text is needed before implementation, and the normal workaround is
to write that draft in the workshop first.

Repository inspection used commit
`df4ae037b8405e7bb811faa04b76f829932f4a83`. The facts below describe that
revision, not a claim that the inconsistency persists in a later checkout.
Live links identify the artifacts; `git show <commit>:<path>` recovers their
observed versions.

## Repository evidence

- The [ADR type](../../reference/types/adr.md) says: "Use an ADR for a concrete
  architectural decision that has been made and implemented". The [proposal
  type](../../reference/types/design-proposal.md) describes a proposal as a
  finished but unadopted design and excludes a decided choice from that role.
- [ADR 089](../../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)
  was already in `kb/reference/adr/`, with both frontmatter and visible status
  set to `accepted`. Its Decision section places tag heads in `kb/tags/`,
  replaces the old hub, and retires `index_source` and `index_key` from the
  tag-head type.
- The tag workshop, `kb/work/tag-contract-convergence/README.md` (deleted
  when the workshop closed in `b745bcc8`; recover it with `git show`),
  simultaneously said that ADR 089 adopted the choices, then stated: "No live participation
  declaration, consumer change, or relocation has landed."
- The observed git tree had no `kb/tags/` directory. It retained
  `kb/notes/tags-README.md`, and `kb/types/tag-readme.schema.yaml` still used
  `index_source` and `index_key`. These are concrete implementation witnesses,
  not an exhaustive audit of all seven decision clauses.
- The ADR was introduced in commit
  `c9926a11e8de8b2c474bdfc4678860247729ece8`, dated
  `2026-09-25T22:41:51+02:00`, titled "Adopt one tag namespace per KB with
  heads in kb/tags (ADR 089)". Its most recent edit at observation was commit
  `81efa680fe96c2b8f0586bbc038b97844edae7d8`, at
  `2026-09-25T23:00:22+02:00`. The inconsistency was therefore present in
  committed records, not only an unsaved draft.

## Why this was an easy mistake

The operator's account distinguishes the necessary activity from the error.
The intended decision must be written before implementation to guide that
implementation. Under the current convention it is drafted in the workshop,
then promoted to the ADR directory once implemented. The mistake is putting
that useful pre-implementation text directly in its eventual destination.

The working diagnosis is that the document form and destination encourage
conflation: an agent is asked to write an ADR, and `kb/reference/adr/` is the
obvious directory. But in Commonplace that placement asserts more than
"the choice has been made". It also asserts that implementation exists.
The proposal and ADR contracts do not provide an explicit durable category
for the intervening state, so the workshop carries the distinction through
practice. This diagnosis explains a plausible error path; no original agent
transcript was inspected to establish its actual reasoning.

The [ADR schema](../../reference/types/adr.schema.yaml) checks document shape
and admits `accepted`, `superseded`, or `deprecated`; those checks alone cannot
establish that a decision has been implemented. Adding a status field without
clarifying its meaning and evidence would leave the central problem open.

## Consequence and evidence limits

A reader treating the ADR as a description of shipped architecture can infer
a layout and rules that the observed checkout does not yet implement. The
workshop and ADR communicate different lifecycle states unless the reader
already knows the drafting convention.

This is one repository-supported occurrence plus an operator report of
recurrence. It does not establish an error rate, the original agent's motive,
or downstream harm. It also does not show that the decision itself was wrong.
Implementation belongs to the tag workshop. This record preserves the
earlier inconsistency even if that work later makes the ADR accurate.
