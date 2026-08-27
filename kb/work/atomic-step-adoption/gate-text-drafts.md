# Decisions 1–2 — draft criterion text

Drafts for the three link-following gates under the artifact-side bound. These are copied into `kb/instructions/review-gates/` when the ADR lands, in one commit, because each edit stales its population once.

Shared reading rule for anything with a claim title — a linked note or another library artifact — stated once here and repeated in each gate (a gate's test must be self-contained, per the review-gate type):

> Read the target's title and opening paragraph. Judge there when the invoked claim is the target's title claim. When it is an interior concept, judge the note's verbatim quotation of the target if it gives one; only otherwise locate the target's treatment of that concept.

## `semantic/grounding-alignment` — new `## Test`

Frontmatter unchanged. Failure mode unchanged. Replace the `## Test` body with:

---

For each material claim or conclusion that the note presents as grounded by a
link, extract the route the note gives: the claim, the cited material, and the
stated or implied inference from that material to the claim.

Linked material is of three kinds, and each is read differently. There is no
reading budget: a conforming note bounds what this gate must open, and a note
that does not conform is the validator's finding, not this gate's.

**Linked library artifacts** — targets under `kb/notes/`, `kb/reference/`,
`kb/instructions/`, `kb/agent-memory-systems/`, or `kb/agentic-systems/`. A
linked note has passed its own grounding review against its own sources; this
gate does not re-ground it. Check representation instead: read the target's
title and opening paragraph and judge whether the claim the note invokes is the
claim the target makes, at the scope the target makes it. When the invoked
claim is an interior concept rather than the title claim, judge the note's
verbatim quotation of the target if it gives one; only otherwise locate the
target's treatment of that concept. A note that cites a linked artifact as
grounding a broader mechanism or wider scope than the target claims is this
gate's finding. Link text that promises what the target does not say belongs to
`sentence/misleading-link-text`, and a sentence identifying this note's concept
with the target's belongs to `sentence/concept-attribution`; do not flag those
here.

**Quoted sources.** When the note quotes a source verbatim — a quoted span
marked as verbatim, paired with a link to that source in the same paragraph —
`commonplace-validate` has already established that the words occur in the
source. Judge the quoted passage on the note's page: does this passage support
this claim, with the qualification the note gives it? Do not open the source to
find support. Open it only when the passage reads as lifted from a qualifying
context, and then only to check that context.

**Unquoted sources.** For a direct link to a tracked
`kb/sources/<slug>.ingest.md` with no paired quotation, use one of these two
routes:

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

A link to a source outside `kb/sources/` that carries evidential weight is
read for its supporting passage; such links should be rare, since untracked
sources require ingest grounding.

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

---

What changed: the sixteen-artifact budget and its disclosure clause are gone; linked notes get a head-first representation route and are never re-grounded; quoted sources are judged on the page; the two ingest routes are unchanged for unquoted sources.

## `sentence/misleading-link-text` — new `## Test`

---

For each markdown link, read the link text and the sentence it appears in. What
does the reader expect to find at the target? Then read the target's title and
opening paragraph. Does the target match the expectation? Open more of the
target only when its head does not settle the question.

Check every link. Repeated links to the same target are one check. Name any
target that cannot be resolved.

---

What changed: the five-target cap and its disclosure clause are gone; the head-first rule is explicit.

## `sentence/concept-attribution` — new `## Test`

---

For each sentence that identifies this note's concept with a concept from
another note — phrases like "this is the X problem from [note]," "this is X in
architectural form," "the same mechanism as [note]'s Y" — check the identity
against the target. Read the target's title and opening paragraph first; judge
there when the concept is the target's title claim. When it is an interior
concept, judge this note's verbatim quotation of the target if it gives one;
only otherwise locate the target's treatment of that concept.

Check every identity claim. Name any target that cannot be resolved.

An attribution is valid if the linked note's core concept supports the claim
being made, even if the exact phrasing differs. Only flag when the linked
note's treatment of the concept is substantively different — not merely when
the vocabulary doesn't match verbatim.

---

What changed: the five-target cap and its disclosure clause are gone; the head-first ladder is explicit. The paraphrased-interior case remains a finding-step outside the artifact-side bound (see [representation-gate-limits.md](./representation-gate-limits.md)).
