# Known Limitations

## WebFetch summarizes large pages

The WebFetch tool processes content through a small model and condenses long documents. Academic papers on arxiv HTML, long blog posts, and documentation pages may be reduced to short summaries rather than captured in full. Affected snapshots have `capture: web-fetch` in frontmatter.

**Workaround for academic papers:** Use the PDF URL instead (e.g. `arxiv.org/pdf/XXXX.XXXXX` rather than `arxiv.org/html/XXXX.XXXXXv1`). The PDF pathway downloads the file and reads it directly — no summarization occurs.

**How to detect:** If a web-fetch snapshot of a long-form source is under ~100 lines, it was likely summarized. Compare against the original URL to verify completeness.
