# Source-span citations, not file-level links

Layer: ingestion / provenance.

Claims should point at the exact passage they rest on, not at a whole source file. This is already the first queued experiment in [`epistack-competition`](./../epistack-competition/README.md) ("does file-level linking suffice, or do claims need a source-span locator type?"). [ADR 023](../../reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md) already built *quote-anchored citations* for code-grounded reviews — the precedent to generalize into a `claim → source-span` locator, so a claim points at the exact passage it rests on and review can verify the quote still says what the claim says.

Prototype this and the [dialectical/evidential register](./fourth-register.md) first — everything else hangs off those two.
