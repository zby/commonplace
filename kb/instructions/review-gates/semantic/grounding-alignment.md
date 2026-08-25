---
gate_id: semantic/grounding-alignment
name: Grounding alignment
description: 'The note cites sources or linked notes as if they ground a claim more directly or more broadly than they actually do.'
type: kb/types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

The note cites sources or linked notes as if they ground a claim more directly
or more broadly than they actually do.

## Test

For each material claim or conclusion that the note presents as grounded by a
link, extract the route the note gives: the claim, the cited material, and the
stated or implied inference from that material to the claim.

For linked notes and ordinary linked sources, read the linked material and
follow at most five links in total. For a direct link to a tracked
`kb/sources/<slug>.ingest.md`, use one of these two routes:

- When the ingest link text does not contain the exact marker `(snapshot
  required)`, read only the ingest's `## Quotes` section as source support.
  Its `Source extract (verbatim)` fields may be combined, and their `Source
  location` fields identify context, but no paraphrase or analysis elsewhere in
  the ingest supplies support. If the retained extracts do not contain enough
  source material to judge the note's use, return FAIL. Do not silently fall
  back to a local snapshot.
- When the ingest link text contains `(snapshot required)`, derive exactly
  `kb/sources/.snapshots/<slug>.md` from the resolved ingest path. Do not search
  for a substitute. Require that file to exist, require its exact-byte SHA-256
  to equal the ingest's `snapshot_sha256`, and require its frontmatter `source`
  to equal the ingest's canonical `source`. Return FAIL if any requirement is
  unmet. Otherwise read the snapshot and judge the note's use against it. The
  ingest's analysis is still not source support.

A purely adjacent link makes no support claim and passes. For an evidential
use, check attribution vocabulary, source scope, coverage across the whole
note, and every transfer from the source setting to the note's setting. Do not
substitute a better argument, outside evidence, another ingest, or a
reconstruction that merely reaches a similar conclusion.

Return FAIL when material support is absent, a required snapshot is
unavailable or invalid, or the note's inference is incompatible with the
linked material. Return WARN for support that is plausible but whose
qualification, modest scope extension, or transfer is not articulated clearly
enough to verify. Report INFO for plausible but non-load-bearing inferences
that are not airtight.
