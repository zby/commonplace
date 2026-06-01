---
description: Verify that quote-anchored citations in a code-grounded review resolve to verbatim text in the reviewed source, run against the live checkout before it is discarded.
type: kb/types/instruction.md
---

# Verify review quote grounding

**Target: $ARGUMENTS** — the review note path (e.g. `kb/agent-memory-systems/reviews/a-mem.md`) and the source checkout directory it was written against.

Confirm every quote-anchored citation in a code-grounded review quotes its source verbatim. A quote-anchored citation is a blockquote whose final line is a `---` attribution naming a source location, as defined in the `agent-memory-system-review` type spec's Citations section.

## When to use

- Right after writing or updating a review, while the source checkout still exists. The reviewed source is not retained in the KB, so this cannot be run later from the KB alone.
- Before committing a review whose load-bearing claims use quote-anchored citations.

Skip when the review uses no quote-anchored citations (no blockquotes with `---` attribution lines). There is nothing to resolve.

## Inputs

- `note_path` — the review note.
- `source_dir` — the checkout the review was written against. Verify it is readable (`test -d "$source_dir"`). If it is missing, **stop and report** — resolution is impossible without it; do not pass the review as verified.
- `reviewed_revision` — the commit the review pins (from the review's `**Reviewed revision:**` line). Used to report mismatches, not to re-checkout.

## Procedure

1. **Extract citations.** From `note_path`, collect each quote-anchored citation as a pair: the **quote** (the blockquote body, all lines above the `---` attribution line, with the leading `> ` markers removed) and the **attribution** (the source path or blob URL, and the commit if present).

2. **Resolve the source path.** For each citation, map the attribution to a file under `source_dir`:
   - A code-span path (`` `src/memory/store.py` ``) → `source_dir/src/memory/store.py`.
   - A blob URL → the path component after `/blob/<commit>/`.
   If the file does not exist under `source_dir`, record a **FAIL** (`missing source file`) and continue.

3. **Resolve the quote.** Read the file and check the quote appears in it, comparing with whitespace normalized — collapse runs of whitespace (spaces, tabs, newlines) to a single space and trim ends, on both the quote and the file text, before searching. Exact-substring after that normalization counts as resolved.
   - Resolves → **PASS**.
   - Does not resolve → **FAIL** (`quote not found in source`). Report the quote (truncated) and the file.

4. **Check the pinned commit (if present in the attribution).** If the attribution names a commit, confirm it matches the review's `reviewed_revision`. A mismatch is a **WARN** (`citation commit differs from reviewed revision`), not a FAIL — the quote may still resolve, but the pin is inconsistent.

5. **Report.** List each citation with its verdict. If any citation FAILs, the review is **not** verified — fix the quote (copy the source verbatim) or the path, then re-run. Resolution failures must be fixed before commit; a paraphrased blockquote is the common cause.

## Scope

- This checks **structural grounding** only — that the quoted text exists in the source. It does **not** check whether the quote supports the claim; that is semantic faithfulness, covered by the `semantic/grounding-alignment` review gate.
- This does not validate ordinary document-level citations (a bare file path with no blockquote). Those are not quote-anchored and have nothing to resolve.
