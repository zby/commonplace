# Supplied evidence and synthesis

## Boundary
Synthetic system Birch, revision fixture-1. Only the supplied passages are evidence.

## Memory record MEM-01
Source docs/retrieval.md: "The client may request a namespace filter." Evidence status: documented optional request parameter. The passage does not say requests must include it or that the server rejects cross-namespace reads.

## Verification context
No unresolved conflict. No other claim or required limitation is at issue.

## Synthesis excerpt
Birch guarantees tenant isolation because "The client may request a namespace filter" (MEM-01). All cross-tenant retrieval is prevented.
