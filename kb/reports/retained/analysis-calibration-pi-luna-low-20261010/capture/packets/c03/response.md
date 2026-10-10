## Verification
The excerpt’s guarantee claim is not supported by MEM-01. The record documents only that the client may request a namespace filter; it expressly does not establish that requests must include the filter or that the server rejects cross-namespace reads. The evidence therefore supports an optional request parameter, not a tenant-isolation guarantee or prevention of all cross-tenant retrieval.

## Blockers
- The synthesis excerpt states, “Birch guarantees tenant isolation” and “All cross-tenant retrieval is prevented,” attributing this to MEM-01. This turns an optional client request parameter into a guaranteed enforcement mechanism and an exhaustive outcome, neither of which the record supports. A public reader would incorrectly infer that Birch prevents cross-tenant reads. That is a central security conclusion, so it cannot be contained by a limitation while leaving the bounded account publishable; the excerpt’s principal guarantee would remain misleading.

## Limits
none