# Simplification passes

Passes that simplify one article or note whose claims are settled but whose
text is not; an assessment recommends the passes and they run without a
selection step. Each pass is a short worker packet: it states
what the pass exists to make true, what it must preserve, and what it returns.
The orchestrating procedure is
[revise an article or note](./revise-an-article-or-note.md).

For a generic editorial pass with no assessment, use
[revise-note](../revise-note.md) instead. For a full automated review pass,
use [run-full-improvement-pass-on-note](../run-full-improvement-pass-on-note.md);
the [audit pass](./audit-a-prior-pass.md) here is for checking what such a
pass did.

## Passes

Each pass declares `effort: simple` or `effort: judgment` in its frontmatter.
Simple passes run in a fresh worker on a cheaper model or lower effort;
judgment passes stay on the session model.

- [audit-a-prior-pass](./audit-a-prior-pass.md) (simple) — trace each passage an automated pass weakened to the finding that caused it, and restore what the finding did not justify.
- [narrow-overclaims](./narrow-overclaims.md) (judgment) — move claims from what cannot be observed to what can, and mark gaps instead of inventing precision.
- [opening-and-title](./opening-and-title.md) (judgment) — make the TL;DR read with only its own words and the title state the central contrast literally.
- [readability-and-flow](./readability-and-flow.md) (judgment) — structural moves and tightening with no change of claim.
- [plain-wording](./plain-wording.md) (simple) — replace decorative figures with literal statements and unusual words with common ones, after the operator approves the list.
- [abstractions](./abstractions.md) (judgment) — per term, either keep a coined or registered abstraction everywhere because one sentence needs its distinction, or replace it with the ordinary word everywhere.
- [split-out-a-treatment](./split-out-a-treatment.md) (simple) — keep the artifact's passage minimal and put the full argument in a separate file that later passes do not load.
- [place-external-systems](./place-external-systems.md) (simple) — position named systems against the artifact's criteria by reading generated main-review files, with source ingests identified separately.
