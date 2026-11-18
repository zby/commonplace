---
description: "Deciding whether retained material supports a citation: a paraphrase keeps the idea but not the words, quotation marks cannot restore them, and a passing wording check certifies only a match against the text it compared"
type: types/note.md
tags: [document-system, claims-and-grounding, kb-maintenance]
---

# A citation cannot assert more fidelity than its capture preserved

A writer reads a passage and keeps a paraphrase of it. The paraphrase can preserve the author's idea. It does not preserve the author's words, and it may drop qualifiers such as population, time or strength. If the writer later puts that paraphrase in quotation marks, the citation claims exact wording that the retained material never held. The marks assert the words; they cannot recover them.

The limit is one of evidence. A citation is supported only as far as the material it rests on reaches. A paraphrase supports a paraphrased citation. A retained verbatim passage supports quoting those words and any use that the passage, read alone, can carry. Some uses depend on broader, distributed or contextual material that a few retained passages cannot represent; those need the full source ([ADR 073](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)).

When the retained material falls short of the citation you want, there are two honest moves:

- **Narrow the citation** to what the material supports: quote only words you kept, paraphrase what you kept as paraphrase, and state a claim at the strength the passage shows.
- **Return to the source** when the use needs exact wording, a dropped qualifier or surrounding context, and capture what is missing.

Stronger notation is not a third move.

Checks inherit the same limit. A wording check verifies that a quoted span matches the text it was compared against, under its comparison rule. It does not certify that the original author wrote that text, that the passage read in context supports the citing use, or that the claim is true. Missing evidence is not a pass: a check that could not read the source has verified nothing. Commonplace's quote checker illustrates this: it tests only quotations marked `verbatim`, by a normalized substring match against the linked source, and has nothing to test in a paraphrase, which never claimed exact words ([ADR 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)).

## Scope

- Covers textual sources whose retained text can be reread. Audio, images and oral quotation are out of scope.
- The claim rests on the reasoning above, not on measured citation errors.
