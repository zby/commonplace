# Known Limitations

## Client-rendered and access-controlled pages may have no extractable HTML

The ordinary-page pathway downloads and extracts the page with Trafilatura. It
does not execute JavaScript, authenticate, or bypass a paywall. A
client-rendered page, login wall, bot challenge, or error shell may therefore
yield no substantive content.

**How to detect:** Trafilatura produces an empty result or extracts only an
access message or application shell. Compare the result with the
browser-visible source before treating a short extraction as complete.

## Image-only PDFs require OCR

Poppler's `pdftotext` extracts text embedded in a PDF. A scanned or image-only
PDF may produce an empty file even when every page is visually readable. The
snapshot workflow has no OCR prerequisite or fallback; provide an OCR-produced
text copy or paste the content manually.

## PDF snapshots preserve extraction artifacts

The PDF pathway copies `pdftotext` output into the snapshot without requiring
the model to re-emit the document. The `-nopgbrk` option removes page-break
characters, but repeated page headers, line-break hyphenation, flattened
tables, and degraded equation glyphs may remain. This is a faithful,
completion-safe capture rather than polished Markdown. Cleanup is a separate
bounded transformation so a blocked model write cannot prevent capture.
