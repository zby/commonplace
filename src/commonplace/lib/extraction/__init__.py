"""Experimental KB extraction utilities.

Reusable building blocks for extracting structured information from a
Commonplace KB tree:

- ``frontmatter_aggregate.aggregate_field(field, roots)`` →
  ``{value: [files]}`` distribution of a frontmatter field across files.
- ``link_audit.find_links(roots, url_pattern)`` → list of ``LinkOccurrence``
  records with file/line/text/url. Backtick-aware (skips inline-code
  examples by default).
- ``source_url.extract_url(source_path, repo_root=)`` → external URL string
  or ``None``. Looks at frontmatter ``source:``, follows
  ``source_snapshot:`` pointers, falls back to body patterns.

These modules were extracted from one-off audit scripts written during the
``kb/commonplace/`` namespace migration (ADR-021). They are provided for
reuse in similar audits.

**Experimental.** Interfaces may change without notice. No backwards
compatibility commitments. Treat as building blocks for workshop scripts,
not as a stable API.
"""
