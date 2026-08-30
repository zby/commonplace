# Fingerprint a response analysis

Use this contract when an `analyse-agentic-system` result is emitted in a
response and needs a byte identity for a transfer scan, an authorized capture,
or an explicit caller request. It makes the stable analysis hashable without
putting its digest inside the bytes it identifies.

## Stable block

The stable block contains exactly one complete Markdown artifact conforming to
`kb/types/agentic-system-analysis-result.md`, including its frontmatter and all
required sections. The same shape applies to `complete`, `blocked`, and
`out-of-scope` dispositions. The stable block excludes the response delimiters,
fingerprint, operator report, and any transfer-scan output.

Emit it in this form, replacing `<run-id>` with the canonical result ID:

```text
<!-- AAS-STABLE-RESULT START <run-id> -->
<typed agentic-system-analysis-result artifact>
<!-- AAS-STABLE-RESULT END <run-id> -->
```

Use exactly one line feed after the start delimiter and exactly one line feed
before the end delimiter. The canonical bytes are the UTF-8 encoding of the
text between those two line feeds. Normalize internal line endings to line
feeds before hashing. Do not include either separator line feed, normalize
Unicode, trim whitespace, or hash renderer-produced text.

Record the canonical byte length and lowercase SHA-256 after the end delimiter.
Never hash the completed assistant message or any line that contains the
digest.

## Freeze and hand off

Assemble and hash the exact stable block before emission, then emit that block
unchanged between the delimiters. An in-memory buffer is sufficient. A file in
the environment's temporary directory is also permitted solely as a freeze
buffer; it is not publication, retention, or a source artifact. Remove it after
emission or an authorized response-capture handoff.

Any correction to the stable block invalidates its byte length and digest.
Reassemble and recompute both before a transfer scan consumes it.

A transfer scan that writes state retains the exact delimited stable block as
received and records the canonical byte length and digest. A response without
the delimiters cannot support written response-derived state; it may support a
response-only scan only when the complete analysis boundary is otherwise
unambiguous.
