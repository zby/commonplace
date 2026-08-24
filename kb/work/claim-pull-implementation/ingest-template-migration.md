# Ingest-template migration

Add this section immediately before `## Connections Found` in every tracked
ingest:

```markdown
## Claims

No claims have been grounded yet.
```

## Boundary

Freeze the live `kb/sources/*.ingest.md` path list before editing. Add only the
heading, blank line, and empty sentence. Do not infer claims, reflow prose, or
change frontmatter, checksums, links, or analysis. Stop for an ingest that
already has an experimental Claims representation.

## Order

1. Validate the frozen corpus and separate pre-existing failures.
2. Make same-checksum re-ingest preserve Claims and restore the exact incumbent
   bytes after a handled final failure.
3. Update the template and drafting instruction.
4. Insert the section using each file's newline convention.
5. Update the type and require exactly one Claims heading in the existing
   schema.
6. Validate and review the diff against the frozen paths.

Separate commits are fine. Do not enable populated grounding until refresh,
template, corpus, and schema agree.

Completion requires one Claims heading per frozen ingest and no other change to
existing artifacts.
